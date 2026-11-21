# Pre-contact clearance sensitivity

The original implementation, all 5,184 prediction rows, 24 adaptive collocation comparisons, and the table verifier are pinned at https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/48461d762b32c54be2fff4e839d2522956a14515 . Run `python run.py` then `python verify.py` in that checkout. It uses a 96-cell grid for the manuscript's primary table.

Run `python clearance_sensitivity.py` in this folder to regenerate the three supplemental CSVs. The independent implementation uses a 192-cell midpoint solver for predictions and a separate piecewise shooting calculation to check three example profiles at two resolutions. It uses exact analytical weak-field slopes, equal deterministic sign combinations and no random samples.

* `clearance_predictions.csv` contains one row per perturbation combination, profile, scale, operating condition, sign pair and calibration method.
* `clearance_sensitivity.csv` summarizes wrong decisions on the four original thresholds and on 61 equally spaced thresholds from 0.10 to 0.70. Each method/error combination includes 576 signed predicted heights, 2,304 four-gap decisions and 35,136 dense-grid decisions. Four identical sign combinations at zero error are retained for comparison.
* `shooting_check.csv` contains two midpoint results per shooting reference (three profiles, eight field/length combinations). Root-finding enforces zero tip moment on the branch approached from the straight state. This tests the same physical equations.

Rows share predicted heights and thresholds; there is no implied sample of devices. The revision used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. Its requirements are provided. The original environment is described in the linked snapshot.

## Environment lock

Create separate Linux x86_64 virtual environments with CPython 3.12.14 for the revision and 3.11.9 for the baseline. In the activated revision environment run `python -m pip install --require-hashes -r revision-cp312-linux-x86_64.lock`. For the original checkout, install `baseline-cp311-linux-x86_64.lock` the same way in the baseline environment, then run the commands above. The baseline lock pins the original NumPy/SciPy pair; the revision lock pins the versions used for the separate numerical sensitivity check. The lock headers identify the platform; the baseline transitive pins reconstruct a compatible environment for the published direct requirements.

## Uniform-gap loss, regularization and exact threshold changes

Run `python gap_risk.py`. `decision_risk.csv` gives direct clipping, repeated displacement and four bounded least-squares fits with penalties. It contains 30 rows (five perturbation pairs × six estimators). `threshold_crossings.csv` identifies all ten individual cases that changed correct/incorrect status on the four-gap grid when angle-error amplitude rose from 0.5% to 3%, with displacement error fixed at 1.5%. Signs and underlying configurations are paired. Loss over the continuous uniform interval [0.10, 0.70] is calculated analytically from each predicted/true height pair before averaging. The estimator penalty is defined using scaled slope channels 3d and 2t.

## Reanalysis of published forward-response measurements

Run `python published_beam.py` with the extracted coordinates present. `yan_fig6_observations.csv` contains approximate *plot coordinates*, obtained from colored experimental markers in Yan, Abbasi & Reis, Fig. 6. The 66 rows cover three specimens and 22 field levels (including zero). `yan_forward_check.csv` retains eight nonzero operating points per specimen, evaluates both forward models for each point, and records height and angle errors and threshold scores. The normalized field, tip angle and height are all read from the published figure. No image or author-provided raw data file was distributed with this supplement.

To regenerate measurements without the CSV, download the authors’ PDF from https://www.epfl.ch/labs/flexlab/wp-content/uploads/2022/05/98_Yan_IJSS_MagneticBeams.pdf into your workspace. In a CPython 3.12 Linux x86_64 environment, run `python -m pip install --require-hashes -r source-extraction-cp312-linux-x86_64.lock`, then `python published_beam.py --extract /path/to/98_Yan_IJSS_MagneticBeams.pdf`. The script checks the PDF hash, selects the experimental markers rather than the plotted model/FEM, and checks consistency between the loading axes in panels a and b. Expected SHA-256: d815d7567a2d42e5b0436125203211d2a3f970270000721e0be1b0a1cc880361. Reported residuals use the published mean dimensions and material properties. Samples are repeated loads on three uniform strips. No heterogeneous or matched-slope coupon outcomes are available from this source.

Source credit: Dong Yan, Arefeh Abbasi and Pedro M. Reis. *A comprehensive framework for hard-magnetic beams: Reduced-order theory, 3D simulations, and experiments*, International Journal of Solids and Structures 257, 111319 (2022), https://doi.org/10.1016/j.ijsolstr.2021.111319 . The source PDF notices CC BY-NC-ND 4.0 (https://creativecommons.org/licenses/by-nc-nd/4.0/). The original PDF and figures are not included. The numerical extraction, coordinate transformations, added model comparison and threshold summaries are identified here to distinguish them from the authors’ observations.
