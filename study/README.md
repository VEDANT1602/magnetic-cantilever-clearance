# Magnetic strip calibration

These programs calibrate reading designs on the experimental points in Fig. 6 of Yan, Abbasi and Reis. The article and the digitized measurements are available from the original source and are excluded from this distribution. Outputs contain aggregate quantities only.

## Reproduction

1. Obtain the [article PDF from EPFL](https://www.epfl.ch/labs/flexlab/wp-content/uploads/2022/05/98_Yan_IJSS_MagneticBeams.pdf). Check its SHA-256 against d815d7567a2d42e5b0436125203211d2a3f970270000721e0be1b0a1cc880361. The extractor requires the matching document layout.
2. In a Python 3.12 environment install requirements with `python -m pip install -r requirements.txt`.
3. Run `python strip_holdout.py /path/to/article.pdf` and `python reading_sensitivity.py /path/to/article.pdf`. The scripts read the source locally and write only the aggregate CSVs alongside themselves.

With index 0 at zero field, indices 1 and 2 provide the primary calibration pair. Indices 4–21 are the held-out loads for all three windows. For the height-plus-angle design, both readings come from the first index of the indicated pair. Results for windows 1/2 and 1/3 therefore coincide for that design. The two-height comparator measures at two distinct weak fields. It is not a pair of identical-load replicates.

`strip_results.csv` contains one line per specimen × calibration window × fitted model. The two-zone penalty grid is 0, 0.001, 0.01 and 0.1. Both uniform and two-zone structures are fitted for each reading design. MAE is normalized by length. Continuous-cutoff risk is dimensionless. Averages give each specimen and its held-out loads equal weight.

`reading_sensitivity.csv` gives the eight signed low-field reading perturbations for the uniform model. Height offsets are ±0.002 length and angular offsets ±0.25 degrees. These are specified perturbations, not estimates of actual measurement uncertainty. The held-out physical responses are unchanged in each comparison. The program contains no copied figure, curves or coordinates. The numerical derived summaries and original analysis software may be reused under the repository’s terms. The original source retains its own rights.

## Converting the uniform-fit difference to micrometres

Run `python length_scale.py`. For each strip the input is the difference d between its two stored normalized MAEs. Multiplying by 13,200 µm, the common published mean length, gives nominal differences. The difference between this common-length mean and the unknown physical length-weighted mean equals the covariance of specimen length with d. Conditional on taking the reported length summaries literally, its absolute magnitude is at most 200 µm × the population SD of d, or 0.098 µm. The published mean and SD are rounded. This bound applies to that conversion only; it excludes optical errors, digitization errors and specimen variability.
