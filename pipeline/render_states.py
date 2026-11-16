"""Render one PNG per (scene, beat) state. Usage: python render_states.py p1|p2 [scene_id_substring]"""
import sys, os, importlib, warnings
from multiprocessing import Pool
warnings.filterwarnings("ignore")
import logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

from style import Canvas

OUT = "/home/claude/work/video/states"


def job(args):
    mod, idx, s = args
    sc = importlib.import_module(mod).SCENES[idx]
    c = Canvas(sc["notion"], sc["part"])
    sc["draw"](c, s)
    path = f"{OUT}/{sc['id']}_{s:02d}.png"
    c.save(path)
    return path


if __name__ == "__main__":
    part = sys.argv[1]
    filt = sys.argv[2] if len(sys.argv) > 2 else ""
    mod = f"scenes_{part}"
    os.makedirs(OUT, exist_ok=True)
    scenes = importlib.import_module(mod).SCENES
    jobs = [(mod, i, s) for i, sc in enumerate(scenes) if filt in sc["id"] for s in range(len(sc["beats"]))]
    with Pool(2) as p:
        for path in p.imap_unordered(job, jobs):
            pass
    print(len(jobs), "states rendered")
