# Choosing two calibration readings on three nominally uniform magnetic strips

Vedant Thaker  
Independent Researcher, Jeffersonville, Indiana, USA  
vedant.thaker1602@gmail.com

Calibration report

### Abstract

On three nominally uniform magnetic cantilevers, does a low-field tip-angle reading improve prediction of high-field displacement compared with a second displacement reading? Each specimen supplied two calibration readings and eighteen held-out heights. Fitting one compliance gave mean absolute errors of 0.731% of strip length with two heights and 0.693% with height and angle. Their difference corresponds to about 5 µm at the published mean length, with one specimen contributing most of it. Moving the calibration loads or perturbing the plotted readings reversed the ordering. Allowing separate compliances on the two halves increased the unpenalized two-height error to 5.367%. In these three strips, assuming a spatially varying stiffness mattered more than the choice of the second reading.

## A measurement choice with a testable consequence

A cantilever can cross a prescribed gap even when its inferred stiffness profile is wrong. A practical calibration therefore needs an endpoint outside the readings used to fit the profile. Here the endpoint is the tip displacement of the same specimen under a stronger transverse magnetic field. A clearance decision can then be evaluated for any specified gap.

Wang et al. compared hard-magnetic elastica predictions with beam experiments [1]. Yan, Abbasi and Reis measured both position and tip orientation on three longitudinally magnetized strips [2]. This combination lets two equally sized calibration designs use distinct measurements of the same physical system. An actual magnetic switch, such as the four-pad device of Wang et al. [3], also involves contact and electrical response. Only geometric clearance is observable in the strip data.

## Separate the calibration loads from the scoring loads

Yan et al., §5.4, report a mean length of 13.2 mm (SD 0.2 mm), mean thickness 0.50 mm and mean width 1.27 mm across the three strips. The publication gives no strip-by-strip lengths. Figure 6 reports 22 loads per strip. Experimental symbols in its two panels give normalized transverse deflection h and tip angle θ. Simulated curves and finite-element markers were excluded. The origin defines the unloaded state. The first two nonzero dimensionless loads q are about 0.42 and 0.85. The third, about 1.28, was reserved for calibration-window sensitivity. Loads 4 through 21 after the origin, spanning approximately 1.67 to 42.85 across specimens, give 54 held-out heights. Each specimen contributes equally. These are repeated loads on three independent physical strips, not 54 independent coupons.

One design observes h(q₁) and h(q₂). The other observes h(q₁) and θ(q₁). In both cases the solver uses finite-field responses directly. Dividing residuals by q places the fit on a secant-response scale without treating a finite-load ratio as a derivative. The test fields never enter parameter estimation. The split and scoring rules were chosen retrospectively for a published dataset.

## Forward mechanics and calibration

Let x denote arclength divided by strip length, θ the local tangent angle and m the dimensionless bending moment. With relative compliance j, the equations are dθ/dx = j m and dm/dx = −q cos θ + G(1 − x) sin θ. The clamped end has θ(0) = 0 and the free tip has m(1) = 0. The transverse height is the integral of sin θ from zero to one. The gravity coefficient G = 12ρgL³/(Et²) is 1.877 at the dimensions and material values in [2]. Continuation from a smaller load follows the branch connected to the initially straight vertical strip.

The known fabrication design favors a common j. A competing fit assigns separate compliances to the proximal and distal halves, with continuity of angle and moment at midspan. The fitted range is 0.12 to 4 times nominal, a numerical sensitivity bound. Displacement residuals enter as 3Δh/q and angle residuals as 2Δθ/q in radians. The factors put both on the uniform, weightless beam’s weak-field compliance scale. They do not estimate the instruments’ error variances. The two-zone fits add λ(j₁ − j₂)² to the squared residuals, with λ in {0, 0.001, 0.01, 0.1}. All settings are reported in the supplement. No test load selects a penalty.

## Identifiability matters more than the second instrument

The uncalibrated nominal strip missed the held-out transverse height by 1.210% of strip length on average. Fitting a single compliance reduced the errors on this panel for both reading designs. For strips s1-1, s1-2 and s1-3 respectively, the two-height error minus the height-and-angle error was +0.1069, +0.0109 and −0.0028 percentage points of strip length. At 13.2 mm these correspond to +14.11, +1.44 and −0.37 µm; their mean is +5.06 µm. These are nominal length conversions. The bound on the effect of unknown individual lengths is about 0.10 µm on the mean if the published mean and SD are taken as exact (derivation in the supplement). The conversion supplies a physical scale; it does not establish instrument accuracy. One specimen accounts for nearly the entire summed improvement.

Two nearby displacement readings gave an unstable two-zone solution. With no penalty, the fitted distal compliance ranged from 2.55 to the upper bound of 4, and the average held-out error reached 5.367%. Angle supplied different spatial information and reduced that figure, but its unpenalized two-zone fit still predicted less accurately than a uniform fit. For a gap drawn uniformly on [a,b], the probability that predicted and measured heights fall on opposite sides is |clip(ĥ,a,b) − clip(h,a,b)|/(b − a). This scores a virtual clearance against measured heights. The narrower operating band gives little weight to errors once both heights exceed 0.70.


| Calibration | Model | λ | Height MAE (% L) | Risk¹ (%) |
| --- | --- | --- | --- | --- |
| No reading | Nominal | — | 1.210 | 0.876 |
| Two heights | Uniform | — | 0.731 | 0.234 |
| Height + angle | Uniform | — | 0.693 | 0.215 |
| Two heights | Two zones | 0 | 5.367 | 3.201 |
| Height + angle | Two zones | 0 | 0.985 | 0.523 |
| Two heights | Two zones | 0.01 | 0.733 | 0.233 |
| Height + angle | Two zones | 0.01 | 0.744 | 0.300 |
| Two heights | Two zones | 0.1 | 0.732 | 0.234 |
| Height + angle | Two zones | 0.1 | 0.696 | 0.226 |
Table 1. Each entry averages 18 held-out loads on each of three strips. ¹Threshold disagreement under a uniform gap between 0.10 and 0.70 strip lengths.

## Which conclusions survive a different calibration window?

Moving the calibration window to nonzero readings 2 and 3 reversed the ranking of the two uniform fits. Average absolute error became 0.805% of length for two heights and 0.859% for height plus angle. The unpenalized two-zone fit from two heights still had 2.483% error. In a separate reading sensitivity check, each calibration height was shifted by ±0.002 strip lengths and the angle by ±0.25°. The eight sign combinations are stress cases, not instrument confidence limits. The change in uniform-model error from replacing the second height by an angle ranged from −0.084 to +0.057 percentage points of length. Four combinations favored each measurement.

Three nominally uniform strips cannot establish the calibration required on a graded coupon. The thresholds were evaluated after the fact from measured height, and neither circuit closure nor contact force was recorded. For these three strips, constraining compliance to be uniform avoided the largest extrapolation errors observed here. Assessing graded strips would require independently measured stiffness contrasts, repeated low-field readings with measurement uncertainties and held-out responses on graded specimens. The present data supply none of those observations.

## Data and code availability

The companion supplement includes the collocation solver, calibration and sensitivity scripts, aggregate specimen results and source-access instructions. The published trace was digitized from Fig. 6 of Yan et al. [2]. The authors’ article and EPFL publication record provide the plotted measurements. A tabulated raw file or specimen-specific lengths could not be located there. A source-hash check identifies the authorized lab-hosted PDF used for extraction. Related project repository: https://github.com/VEDANT1602/magnetic-cantilever-clearance.

[Study files, software and source records](https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/main/study)

## Author and disclosures

Vedant Thaker is the sole author and set the research question. OpenAI Codex assisted with extracting measurements from the cited experiment, implementing the calibration comparisons, checking the specimen-level unit conversion and drafting the analysis.

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The author declares no competing interests.

## References

[1] L. Wang, Y. Kim, C. F. Guo and X. Zhao. Hard-magnetic elastica. Journal of the Mechanics and Physics of Solids 142, 104045 (2020). <https://doi.org/10.1016/j.jmps.2020.104045>

[2] D. Yan, A. Abbasi and P. M. Reis. A comprehensive framework for hard-magnetic beams: Reduced-order theory, 3D simulations, and experiments. International Journal of Solids and Structures 257, 111319 (2022). <https://doi.org/10.1016/j.ijsolstr.2021.111319>

[3] Y. Wang et al. A miniature magnetic switch unlocking multimodal, chip-free, and batteryless airway sensing. Science Advances 12, eaed3998 (2026). <https://doi.org/10.1126/sciadv.aed3998>
