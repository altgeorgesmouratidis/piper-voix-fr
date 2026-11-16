# Vidéos de cours

Vidéos explicatives narrées, générées à partir des chapitres de cours annotés (projet Claude « Cours théorique »).

## Organisation
- `fr_FR-siwis-medium.onnx` + `.onnx.json` : voix Piper française utilisée pour la voix off.
- `pipeline/` : code commun de rendu.
  - `style.py` : charte visuelle (couleurs, police Inter, formules mathtext, tableaux, graphiques, bandeau).
  - `speech.py` : conversion du texte pour la synthèse (nombres en belge : septante, nonante).
  - `render_states.py` : une image PNG par étape de chaque scène.
  - `build.py` : voix Piper par étape → scènes MP4 (fondus synchronisés) → concaténation → loudnorm → MP4 + SRT.
- `[COURS]/chapitre-XX/` : un dossier par chapitre.
  - `scenes_p1.py`, `scenes_p2.py`… : texte de la voix off et dessin de chaque scène.
  - les MP4, SRT, le script de la voix off et la fiche récap.

## Régénérer une vidéo (Python 3, ffmpeg)
```
pip install matplotlib numpy pillow num2words piper-tts
cp pipeline/*.py ANA/chapitre-01/
cd ANA/chapitre-01
python render_states.py p1
python build.py p1 --voice ../../fr_FR-siwis-medium.onnx
```
Les chemins de travail sont définis par `ROOT` dans `build.py` et `OUT` dans `render_states.py` : adapte-les à ton dossier.

## Chapitres
| Cours | Chapitre | Parties | Durée |
|---|---|---|---|
| 5ANA1D | 1 — Statistique descriptive | 1 : vocabulaire et discret · 2 : continu et qualitatif | 8 min 20 · 11 min 17 |
