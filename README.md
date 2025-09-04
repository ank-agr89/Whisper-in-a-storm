# Finding a Whisper in a Storm — LIGO-Style Matched Filtering (Toy)

An intuitive, reproducible demo of how matched filtering pulls a weak, chirping signal out of noise—mirroring the core idea behind LIGO’s searches. Includes a short LaTeX paper, figures, and a minimal Python workflow.

## What’s here
- `ligo_toy_matched_filter.tex` — Overleaf-ready paper (story + numbered equations).
- `parameters.tex` — Auto-generated table included by the paper.
- `fig1_timeseries.png` — Noisy data with injected chirp.
- `fig2_correlation.png` — Matched-filter (correlation) output.
- `fig3_residual_hist.png` — Residual histogram with Gaussian fit.
- `fig4_spectrogram.png` — **Whitened, median-subtracted STFT** (long window, high overlap, 95–99.5% contrast clipping).
- `appendix_code.py` — Code listing used in the paper.
- `timeseries.csv` — Optional time-series export.

> Scope: pedagogical toy. It illustrates the core ideas but is not a full LIGO pipeline (no template banks, chi-square reweighting, multi-detector coherence, or formal false-alarm rates).

## Quick start

**Option A — Use the existing outputs**
1. Open `ligo_toy_matched_filter.tex` in Overleaf.
2. Upload `parameters.tex` and all `fig*.png` to the same folder.
3. Recompile.

**Option B — Regenerate everything locally**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy scipy matplotlib pandas
python scripts/make_outputs.py
