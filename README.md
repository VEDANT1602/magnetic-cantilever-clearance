# A better tip-height estimate can still miss the clearance decision

Consider a modeled beam whose tip reaches 0.5961 beam lengths, just below a gap at 0.6000. Two displacement readings predict 0.5873. Using displacement and angle predicts 0.6027. The angle-based estimate is closer to the reference height, yet it puts the tip on the wrong side of the gap. These are two predictions for the same soft-base beam and the same 1.5% slope perturbation. [Paired predictions](results.csv?plain=1#L1497)

The calibration has a budget of two weak-field slope measurements. Repeating displacement fits a homogeneous compliance. Adding the tip angle lets the model fit two zones, at the price of greater sensitivity to noise. Each comparison covers 144 operating cases, four perturbation-sign assignments and four gap thresholds. The signs coincide at zero noise.

| Slope perturbation | Wrong gap decisions with repeated displacement | Wrong decisions with displacement and angle |
| --- | ---: | ---: |
| 0% | 16 / 2,304 | 4 / 2,304 |
| 1.5% | 18 / 2,304 | 19 / 2,304 |
| 5% | 24 / 2,304 | 49 / 2,304 |

The gap check uses simulated pre-contact tip height. An independent adaptive solver checks the spatial discretization in 24 configurations. Neither calculation models electrical contact or establishes a device's tolerance. [Solver comparison](validation.csv) · [Calculation](run.py#L47) · [Model and derivation](manuscript.md) · [Paper PDF](manuscript.pdf)

## Reproduce the comparison

Run from the repository root with Python 3.11. The study used Python 3.11.9, NumPy 1.26.0 and SciPy 1.11.2. It generates all beam profiles locally.

```bash
python -m pip install -r requirements.txt
python run.py
python verify.py
```

`run.py` writes the finite-field predictions to `results.csv` and compares two spatial resolutions with an adaptive collocation solver in `validation.csv`. `verify.py` uses the Python standard library to recompute gap crossings from the saved heights, check the six table rows and check the independent solver discrepancies.

Repository maintained by **Vedant Thaker**.
