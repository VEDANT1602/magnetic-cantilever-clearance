# Preparation record

Decision loss for weak-field calibration of a magnetic cantilever

Vedant Thaker · 21 November 2026

## Original work

Vedant Thaker is the sole author. He designed the original magnetic cantilever calibration study, wrote its manuscript, developed its original software, and requested the comparisons and checks reported in this revision.

The author reports that the research project began on 2 August 2026. The previous versions and the new revision represent different stages of the work.

## Revision activities

OpenAI Codex assisted with the bounded calibration and decision-loss calculations, solver and threshold checks, extraction of published strip-marker coordinates, and gravity-aware forward comparison, as well as literature checks and preparation of the revised text. The author set the research question and requested the revision.

## Computational checks

A fresh run reproduced the archived prediction and validation fields to within 2.23 × 10⁻¹⁶ absolute difference. The original verifier reconstructed the six height-error and gap-decision rows and both resolution bounds. The new implementation recovered all four-gap counts at 192 cells and added the dense-gap, unequal-error and shooting checks. The bounded solver checks the interior and every box edge. The supplied transition ledger identifies all ten changed decisions between the unequal-error cases. The physical forward check uses the published Fig. 6 experimental markers and measured mean material properties. Its digitized heights are approximate.

## Data and version records

The baseline repository contains the code, 5,184 predictions and 24 solver comparisons. Run python run.py and python verify.py in that checkout. The companion supplement includes clearance_sensitivity.py, its environment, its signed predictions, both gap-grid summaries and shooting comparisons. Run python clearance_sensitivity.py to regenerate all three supplemental CSVs. All profiles are specified numerically. The supplement includes separate Linux x86_64 environment locks for the baseline and revision. The new programs gap_risk.py and published_beam.py regenerate the regularized decision risks, per-threshold reversals and the forward check on published experimental markers. The supplement gives the source PDF hash and a script for extracting the markers from the separately obtained PDF. Per-marker vectors and the source figure are excluded from redistribution.

[Original pinned software](https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/48461d762b32c54be2fff4e839d2522956a14515) · [Revision code and data](https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/main/revision/supplement)

The reported checks are computational. No independent personal rerun or line-by-line review of these revisions by the author is asserted here.
