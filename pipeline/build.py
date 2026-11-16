"""Build one part: TTS per beat -> scene timelines -> scene MP4s -> concat -> loudnorm -> mux, + SRT.
Usage: python build.py p1|p2 --voice /path/model.onnx  [--only scene_substring]"""
import argparse, hashlib, json, os, subprocess, sys, wave, re
import numpy as np
from PIL import Image
from speech import to_speech

ROOT = "/home/claude/work/video"
FPS, W, H = 30, 1920, 1080
LEAD, GAP, TAIL, XF, SFADE = 0.35, 0.45, 0.8, 0.35, 0.3
BG_RGB = np.array([15, 23, 42], dtype=np.float32)
SR = 22050


# ------------------------------------------------------------------ TTS
class Piper:
    def __init__(self, model):
        from piper import PiperVoice
        self.v = PiperVoice.load(model)

    def synth(self, text, path):
        with wave.open(path, "wb") as wf:
            if hasattr(self.v, "synthesize_wav"):
                from piper import SynthesisConfig
                self.v.synthesize_wav(text, wf, syn_config=SynthesisConfig(length_scale=1.05))
            else:
                self.v.synthesize(text, wf, length_scale=1.05)


def wav_info(path):
    with wave.open(path) as w:
        return w.getframerate(), w.getnframes(), w.getnchannels(), w.getsampwidth()


def read_wav(path):
    with wave.open(path) as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    if sr != SR:
        n = int(len(x) * SR / sr)
        x = np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)
    return x


def write_wav(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


class Fake:
    """Pipeline test only: a soft tone whose length mimics speech."""
    def synth(self, text, path):
        d = len(text.split()) / 2.6
        t = np.arange(int(d * SR)) / SR
        write_wav(path, 0.1 * np.sin(2 * np.pi * 220 * t) * (np.sin(2 * np.pi * 3 * t) > 0))


# ------------------------------------------------------------------ helpers
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:]); sys.exit(1)
    return r


def srt_time(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def split_cues(text, start, dur):
    """Split a beat into sentence-sized cues, timed by character share."""
    parts = [p.strip() for p in re.split(r"(?<=[.?!])\s+", text) if p.strip()]
    tot = sum(len(p) for p in parts)
    cues, t = [], start
    for p in parts:
        d = dur * len(p) / tot
        cues.append((t, t + d, p)); t += d
    return cues


# ------------------------------------------------------------------ scene render
def render_scene(sc, beat_starts, n_frames, out):
    states = [np.asarray(Image.open(f"{ROOT}/states/{sc['id']}_{k:02d}.png").convert("RGB"), dtype=np.float32)
              for k in range(len(sc["beats"]))]
    tmp = out[:-4] + ".part.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast",
                          "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
    last_key, buf = None, None
    for f in range(n_frames):
        t = f / FPS
        k = max(i for i, b in enumerate(beat_starts) if b <= t + 1e-9) if t >= beat_starts[0] else 0
        a = 1.0
        if k > 0 and t - beat_starts[k] < XF:
            a = (t - beat_starts[k]) / XF
        fade = min(1.0, t / SFADE, (n_frames / FPS - t) / SFADE)
        key = (k, round(a, 3), round(fade, 3))
        if key != last_key:
            img = states[k] if a >= 1 else states[k - 1] * (1 - a) + states[k] * a
            if fade < 1:
                img = BG_RGB + (img - BG_RGB) * max(fade, 0)
            buf, last_key = img.astype(np.uint8).tobytes(), key
        p.stdin.write(buf)
    p.stdin.close()
    if p.wait() != 0:
        sys.exit("ffmpeg failed on " + sc["id"])
    os.replace(tmp, out)


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("part"); ap.add_argument("--voice", required=True); ap.add_argument("--only", default="")
    ap.add_argument("--name", default=None)
    a = ap.parse_args()
    mod = __import__(f"scenes_{a.part}")
    tts = Fake() if a.voice == "fake" else Piper(a.voice)
    os.makedirs(f"{ROOT}/tts", exist_ok=True); os.makedirs(f"{ROOT}/scenes_out", exist_ok=True)

    timeline, all_audio, cues, t0 = [], [], [], 0.0
    for sc in mod.SCENES:
        if a.only and a.only not in sc["id"]:
            continue
        clips, starts, t = [], [], LEAD
        for b in sc["beats"]:
            spoken = to_speech(b)
            h = hashlib.md5((a.voice + spoken).encode()).hexdigest()[:12]
            wp = f"{ROOT}/tts/{h}.wav"
            if not os.path.exists(wp):
                tts.synth(spoken, wp + ".tmp.wav"); os.replace(wp + ".tmp.wav", wp)
            x = read_wav(wp)
            starts.append(t); clips.append(x)
            d = len(x) / SR
            cues += split_cues(b, t0 + t, d)
            t += d + GAP
        dur = t - GAP + TAIL
        n_frames = int(round(dur * FPS)); dur = n_frames / FPS
        audio = np.zeros(int(round(dur * SR)), dtype=np.float32)
        for st, x in zip(starts, clips):
            i = int(st * SR); audio[i:i + len(x)] += x[: len(audio) - i]
        all_audio.append(audio)
        out = f"{ROOT}/scenes_out/{sc['id']}.mp4"
        sig = hashlib.md5(json.dumps([starts, n_frames]).encode() +
                          b"".join(open(f"{ROOT}/states/{sc['id']}_{k:02d}.png", "rb").read()[-64:] for k in range(len(starts)))).hexdigest()
        sigp = out + ".sig"
        if not (os.path.exists(out) and os.path.exists(sigp) and open(sigp).read() == sig):
            render_scene(sc, starts, n_frames, out)
            open(sigp, "w").write(sig)
        timeline.append(dict(id=sc["id"], start=t0, dur=dur, beats=[t0 + s for s in starts]))
        print(f"{sc['id']:28s} {dur:6.1f}s", flush=True)
        t0 += dur

    name = a.name or f"cours-5ANA1D-01-partie-{a.part[-1]}"
    outdir = f"{ROOT}/out"; os.makedirs(outdir, exist_ok=True)
    lst = f"{ROOT}/scenes_out/{a.part}.txt"
    with open(lst, "w") as f:
        for s in timeline:
            f.write(f"file '{ROOT}/scenes_out/{s['id']}.mp4'\n")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", f"{outdir}/{name}.video.mp4"])
    write_wav(f"{outdir}/{name}.raw.wav", np.concatenate(all_audio))
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{outdir}/{name}.raw.wav", "-af",
         "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", f"{outdir}/{name}.norm.wav"])
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{outdir}/{name}.video.mp4", "-i", f"{outdir}/{name}.norm.wav",
         "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest",
         "-movflags", "+faststart", f"{outdir}/{name}.mp4"])
    with open(f"{outdir}/{name}.srt", "w") as f:
        for i, (s, e, txt) in enumerate(cues, 1):
            f.write(f"{i}\n{srt_time(s)} --> {srt_time(e)}\n{txt}\n\n")
    json.dump(timeline, open(f"{outdir}/{name}.timeline.json", "w"), indent=1)
    print("TOTAL", round(t0, 1), "s")


if __name__ == "__main__":
    main()
