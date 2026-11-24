# Choosing two calibration readings on three nominally uniform magnetic strips

Vedant Thaker  
Independent Researcher, Jeffersonville, Indiana, USA  
vedant.thaker1602@gmail.com

Calibration sensitivity report · November 24, 2026

### Abstract

A second calibration reading on a magnetic cantilever can come from its displacement at a higher field or from its tip angle at the first field. Digitized measurements from three nominally uniform strips allow both choices to be tested against the same eighteen higher-field displacements per specimen. With the first two nonzero calibration fields, mean absolute prediction error was 0.731% of strip length for two heights and 0.693% for height and angle. Moving the calibration window up one field level reversed the ordering (0.805% and 0.859%). One strip contributed 93% of the first window’s signed difference. On these measurements, the choice between the two designs depends on which weak fields are used for calibration.

## The measurement decision

When a soft cantilever bends under a magnetic field, both its tip position and its angle carry information about compliance. With two low-field readings available, a calibration can use two tip heights at distinct loads, or height and angle at the same load. The practical test here is which pair predicts an unobserved high-field height more accurately on the same strip.

Hard-magnetic elastica models have been compared with beam experiments [1]. Yan, Abbasi and Reis measured both displacement and angle on three nominally uniform, longitudinally magnetized strips [2]. Their paired curves make this retrospective comparison possible. The recorded endpoint is geometric. A magnetic switch with electrical contacts [3] would require a different endpoint.

## Specimens, held-out fields and forward model

Yan et al. report means of 13.2 mm for length (SD 0.2 mm), 0.50 mm for thickness and 1.27 mm for width [2, §5.4]. Figure 6 plots experimental markers at 22 load levels per strip in height and angle panels. The analysis digitizes only the experimental symbols. The origin gives the unloaded configuration. The first three nonzero dimensionless loads q are approximately 0.42, 0.85 and 1.28. Calibration uses pairs drawn from these three levels. Indices 4 through 21 yield the same eighteen held-out heights for every calibration window. All cases and scoring rules were chosen after publication of the source curves.

For each strip, height h is normalized by its length. The solver uses dimensionless arclength x, local angle θ, bending moment m and relative compliance j. The governing equations are dθ/dx = j m and dm/dx = −q cos θ + G(1 − x) sin θ, with θ(0) = 0 and m(1) = 0. The integral of sin θ gives tip height. The gravity coefficient G = 12ρgL³/(Et²) is 1.877 using the source’s mean dimensions and material properties. Continuation follows the branch connected to the undeformed strip.

The main comparison fits one constant compliance per strip, between 0.12 and 4 times nominal. It minimizes the sum of squared residuals for the two observed values. Residuals enter as 3Δh/q for height and 2Δθ/q for angle in radians. These factors put both on the compliance scale of a uniform weightless beam at weak field. Individual measurement-error variances are unavailable. The height-and-angle fit uses the lower field in each window. Its predictions therefore coincide for windows 1–2 and 1–3. Errors are averaged first over the eighteen held-out loads and then equally over the three strips.

## The comparison changes with the calibration fields

| Strip | Two heights, fields 1–2 | Height + angle, field 1 | Difference, fields 1–2 | Difference, fields 1–3 | Difference, fields 2–3 |
| --- | --- | --- | --- | --- | --- |
| s1-1 | 1.243 | 1.136 | +0.107 | +0.132 | +0.064 |
| s1-2 | 0.553 | 0.542 | +0.011 | +0.006 | −0.065 |
| s1-3 | 0.398 | 0.401 | −0.003 | −0.002 | −0.161 |
| Mean | 0.731 | 0.693 | +0.038 | +0.046 | −0.054 |

Table 1. Mean absolute height error as a percentage of strip length. Differences in percentage points equal the two-height error minus the height-and-angle error. A positive difference favors using the tip angle.

With fields 1–2, strip s1-1 supplies 93% of the signed mean contrast. With fields 2–3 it still favors height and angle. The other two favor two heights, and s1-3 has the largest difference. The sign reversal therefore persists even though every design is evaluated on the same higher-field loads.

At the reported mean length, the +0.038 percentage-point difference for fields 1–2 corresponds to about 5 µm. Omitting strip s1-1 reduces that conversion to about 0.5 µm. Individual lengths were unavailable. The conversion describes the difference between two fitted errors. Establishing an improvement of that size would require raw instrument precision and repeatability, neither of which is recoverable from marker centers.

To examine reading sensitivity, each of the two low-field heights was shifted by ±0.002 strip lengths and the low-field angle by ±0.25°. Across the eight sign combinations, the paired contrast ranged from −0.057 to +0.084 percentage points, and four favored each design. These perturbations explore possible errors at the calibration step. Their magnitudes were assigned independently of the apparatus.

## Limits of the calibration design

For comparison, the supplementary analysis allows separate compliances on the two halves of a strip. Two nearby height readings weakly constrain their difference. On fields 1–2, the unpenalized model gave 5.367% mean error for two heights, and at least one distal compliance reached the upper bound. Adding a squared penalty of 0.01 on the compliance difference brought that error to 0.733%, close to the uniform fit. The exercise shows how a weakly constrained parameter can affect extrapolation for these specimens. All three strips were fabricated to be uniform. Testing calibration on graded strips requires specimens with independently characterized gradients.

## Data and code availability

The study files include fitting scripts, specimen-level errors, perturbation results and a hash for the source article PDF. The extractor reads Figure 6 from the lab-hosted paper [2]. Original instrument output and per-strip lengths have been requested from the source authors. The reported fits use published markers and pooled dimensions. Full numerical results and instructions accompany this report and are in the [public study repository](https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/main/study).

## Author and disclosures

Vedant Thaker is the sole author and set the research question. OpenAI Codex assisted with extracting measurements from the cited experiment, implementing the calibration comparisons, checking the specimen-level unit conversion and drafting the analysis.

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The author declares no competing interests.

## References

[1] L. Wang, Y. Kim, C. F. Guo and X. Zhao. Hard-magnetic elastica. Journal of the Mechanics and Physics of Solids 142, 104045 (2020). <https://doi.org/10.1016/j.jmps.2020.104045>

[2] D. Yan, A. Abbasi and P. M. Reis. A comprehensive framework for hard-magnetic beams: Reduced-order theory, 3D simulations, and experiments. International Journal of Solids and Structures 257, 111319 (2022). <https://doi.org/10.1016/j.ijsolstr.2021.111319>

[3] Y. Wang et al. A miniature magnetic switch unlocking multimodal, chip-free, and batteryless airway sensing. Science Advances 12, eaed3998 (2026). <https://doi.org/10.1126/sciadv.aed3998>
