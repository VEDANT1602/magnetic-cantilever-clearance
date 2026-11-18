# Two weak-field measurements for predicting magnetic cantilever clearance

Two magnetic cantilevers can bend by the same amount in a weak field and still fall on opposite sides of a gap at a stronger field. One extra reading is available. Is it better to repeat the displacement measurement or measure the tip angle?

With exact calibration readings, adding angle lowers mean tip-height error from 0.00644 to 0.00157 beam lengths. With 5% perturbations, repeating displacement gives the lower error. Even at intermediate precision, the calibration with the smaller mean error can make more wrong clearance decisions.

[Read the manuscript (PDF)](manuscript.pdf) · [Browse the manuscript (Markdown)](manuscript.md) · [Inspect predictions (CSV)](results.csv) · [Inspect the independent solver check (CSV)](validation.csv)

## What is measured

A weak-field tip displacement samples a weighted average of bending compliance. A tip angle samples a different average. Together these two slopes identify the compliances of two equal-length zones, but the inversion amplifies measurement error. The comparison gives each calibration two slope readings. One model averages two displacements and assumes homogeneous compliance. The other uses displacement and angle to fit two zones.

The finite-field test contains six generated compliance profiles, three overall compliance scales, two beam lengths and four field strengths. Four possible signs for the two measurement errors are evaluated at each perturbation magnitude. The movement is planar, the field is uniform and only the pre-contact shape is solved.

## Which calibration gets the gap right?

Height error is measured in beam lengths. A clearance decision asks whether the reference or predicted tip height reaches a gap. Each row covers 144 operating cases, four perturbation-sign assignments and four gap levels, for 2,304 decisions. The four assignments coincide at 0% perturbation.

| Relative slope perturbation | Calibration | Mean absolute height error | Wrong decisions / 2,304 |
|---|---|---:|---:|
| 0% | Repeated displacement | 0.00644 | 16 |
| 0% | Displacement and angle | 0.00157 | 4 |
| 1.5% | Repeated displacement | 0.00698 | 18 |
| 1.5% | Displacement and angle | 0.00478 | 19 |
| 5% | Repeated displacement | 0.00937 | 24 |
| 5% | Displacement and angle | 0.01439 | 49 |

The perturbations are a deterministic sensitivity test. To transfer the result to a device, the experiment would need measured angle and displacement errors, a measured clearance and a separate check for electrical contact.

## Reproduce the comparison

Run from the repository root with Python 3.11. The study used Python 3.11.9, NumPy 1.26.0 and SciPy 1.11.2. It generates all beam profiles locally.

```bash
python -m pip install -r requirements.txt
python run.py
python verify.py
```

`run.py` writes the finite-field predictions to `results.csv` and compares two spatial resolutions with an adaptive collocation solver in `validation.csv`. `verify.py` uses the Python standard library to recompute gap crossings from the saved heights, check the six table rows and check the independent solver discrepancies.

Repository maintained by **Vedant Thaker**.
