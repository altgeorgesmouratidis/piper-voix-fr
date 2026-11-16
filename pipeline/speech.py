"""Turn narration (with digits) into text a French TTS reads correctly, Belgian style."""
import re
from num2words import num2words


def be(n: int) -> str:
    w = num2words(n, lang="fr_BE")
    w = w.replace("quatre-vingt et un", "quatre-vingt-un")
    w = re.sub(r"cents(?=[ -])", "cent", w)
    if n == 80:
        w = "quatre-vingts"
    return w


def dec(m):
    ip, fp = m.group(1), m.group(2)
    lead = len(fp) - len(fp.lstrip("0"))
    rest = fp.lstrip("0")
    words = be(int(ip)) + " virgule " + " ".join(["zéro"] * lead)
    if rest:
        words += (" " if lead else "") + be(int(rest))
    return words.replace("  ", " ")


def to_speech(t: str) -> str:
    t = t.replace("%", " pour cent")
    t = t.replace("°", " degrés")
    t = re.sub(r"(\d+),(\d+)", dec, t)
    t = re.sub(r"\d+", lambda m: be(int(m.group(0))), t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


if __name__ == "__main__":
    for s in ["0,035 fois 8, plus 0,25. Soit 0,53 : 53 %.", "80 étudiants, 72,1 kilos, 189°, 0,875 et 81 et 1,33",
              "52,375 grammes", "0,05 divisé par 0,035"]:
        print(to_speech(s))
