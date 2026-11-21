# Decision loss for weak-field calibration of a magnetic cantilever

**Vedant Thaker**  
Independent Researcher, Jeffersonville, Indiana, United States  
Correspondence: vthaker1@asu.edu  
21 November 2026

## Abstract

A second weak-field channel can improve a beam-height estimate yet worsen predictions at particular contact gaps. This study compares repeated displacement, displacement plus tip angle, and a regularized two-zone inversion. The main decision loss in this revision is the fraction of uniformly weighted gaps from 0.10 to 0.70 beam lengths placed on the wrong side of the predicted height. Across 144 prescribed operating configurations and signed 1.5% slope perturbations, the mean loss was 0.904% for repeated displacement and 0.661% for displacement plus angle. At 5%, direct inversion gave 2.111%; regularizing the compliance contrast lowered that to 1.596%, while repeated displacement gave 1.276%. A separate forward check used 24 published load observations from three homogeneous strips. Including self-weight reduced mean absolute height discrepancy from 0.0499 to 0.0153 beam lengths. Those experiments test the forward response of uniform strips. Choosing the better calibration for heterogeneous specimens still requires measured slopes and operating gaps on those specimens.

## Spending the second weak-field reading

Hard-magnetic elastica theory predicts large deflections under an applied field [1]. Comparisons of reduced-order beam models, three-dimensional simulations and experiments test when those predictions carry over to specimens [2]. A magnetic switch offers a concrete example of why a threshold can matter more than mean displacement [3]. This study takes the equilibrium equations as given and asks a calibration question: which two weak-field readings best predict whether the free tip will reach a specified gap at a stronger field?

Chang and Guo used time histories of free-end transverse displacement and slope to identify beam properties from boundary measurements [4]. Here the measurement budget is two static weak-field readings. The repeat-displacement estimator spends both readings on the same observable and fits a uniform compliance. Its competitor spends the second reading on tip angle and fits proximal and distal compliance separately. Both estimators face the same finite-field heights and contact thresholds. The comparison stops at the predicted crossing; neither post-contact force nor switch operation enters the model.

## Tip-angle and tip-height slopes identify two compliance zones

Let s ∈ [0, 1] denote arc length divided by beam length. The relative compliance J(s) is the ratio of reference bending rigidity to local bending rigidity. The strip is slender, inextensible, initially straight and magnetized along the local tangent. A transverse uniform field supplies a distributed torque. Define q as zero-angle magnetic torque per unit length times length squared divided by reference bending rigidity. Let θ, m and h denote tangent angle, dimensionless moment and height divided by beam length. With derivatives taken in s, θ′ = Jm, m′ = −q cos θ and h′ = sin θ. The boundary conditions are θ(0) = h(0) = m(1) = 0.

At first order, m = q(1 − s). The weak-field tip-angle slope t is the integral of (1 − s)J(s) from 0 to 1. The normalized tip-height slope d is the integral of (1 − s)²J(s) over the same interval. For equal proximal and distal halves of compliances P and D, d = (7P + D)/24 and t = (3P + D)/8. These equations invert to P = 6d − 2t and D = −18d + 14t.

Two beams demonstrate what the second observable resolves. The pairs (P, D) = (1, 1) and (0.9, 1.7) both have d = 1/3, but t equals 0.50 and 0.55 respectively. At q = 4.761 their computed tip heights at unit compliance scale are 0.70476 and 0.68690. A gap of 0.695 would separate them. This illustrative gap is distinct from the scored grid. The inverse also explains the cost of measuring angle: for a uniform unit beam, independent signed fractional slope errors of magnitude at most ε permit absolute errors up to 3ε in P and 13ε in D before clipping.

## Compliance profiles, slope errors and clearance thresholds

The six compliance profiles, from clamp to tip in four equal quarters, are (1, 1, 1, 1), (1.4, 1.4, 0.6, 0.6), (0.6, 0.6, 1.4, 1.4), (0.9, 0.9, 1.7, 1.7), (1.6, 0.8, 0.8, 0.8) and (0.65, 1.35, 0.65, 1.35). Each profile is scaled by 0.65, 1 or 1.5. The first four fall in the two-zone fitted family. A localized patch and an alternating profile test model mismatch. Two relative lengths (0.85, 1.15) and four relative fields (0.4, 1, 2, 3.6) give 144 configurations. The dimensionless load equals the field times the squared relative length and ranges from 0.289 to 4.761.

The nominal estimator assumes unit compliance. Repeated displacement fits a homogeneous compliance equal to three times the mean of the two readings. The angle-assisted estimator fits P and D from one displacement and one angle slope and clips each compliance to [0.12, 4]. Signed relative errors of 0%, 1.5% or 5% multiply the exact slopes. At each level the design assigns equal weight to (++), (+−), (−+) and (−−). These signs specify perturbation cases. They have no measured frequency, and at zero error all four cases coincide.

Gap decisions compare the predicted and true-model heights with 0.15, 0.30, 0.45 and 0.60 beam lengths, treating equality as a crossing. Each method at each perturbation level yields 576 signed heights and 2,304 decisions. The latter share 144 structural configurations. A separate calculation rescored the operating design with 61 equally spaced gaps between 0.10 and 0.70 and varied angle and displacement precision separately.

For this revision the main modeled decision loss gives every gap g in [0.10, 0.70] the same weight. Given a modeled reference height h and a prediction ĥ, the probability of opposite threshold decisions is |clip(ĥ, 0.10, 0.70) − clip(h, 0.10, 0.70)|/0.60. The average over the finite structural and sign grid is exact for this assumed gap distribution. No empirical contact frequencies specify that distribution. The original four exact gaps remain relevant if a switch has four discrete contacts. The prior four-gap and dense-grid results were already known when this revision selected the continuous endpoint.

## Decision loss across a continuous range of gaps

The direct inverse uses one displacement and one angle slope and clips the inferred compliances independently. A second fit minimizes the squared residuals in the normalized observations 3d and 2t plus λ(P − D)², subject to 0.12 ≤ P,D ≤ 4. The corresponding observation matrix has rows (7/8, 1/8) and (3/4, 1/4). A uniform strip gives the same value in both normalized channels. The penalty reduces proximal–distal contrast and introduces bias for heterogeneous strips. The box-constrained minimum was obtained by testing the interior optimum and the four boundary minimizers. At λ = 0 the fit can still differ from clipping a separately calculated inverse.

Table 1 gives mean decision loss on the declared uniform-gap range. At 1.5% perturbation the unregularized angle estimate gives 0.661%, below 0.904% with repeated displacement. At 5%, enforcing the bounds during inversion improves on separate clipping. Mild contrast penalties improve the angle estimator further. The repeat-displacement fit remains preferable to all tested angle estimators at 5% on this endpoint. The penalty grid spans two orders of magnitude; none of its weights was calibrated to measurements or a new specimen set.

| Estimator | 0% perturbation | 1.5% | 5% |
| --- | --- | --- | --- |
| Repeat displacement | 0.825% | 0.904% | 1.276% |
| Direct inverse + clip | 0.179% | 0.661% | 2.111% |
| Constrained fit, λ = 0 | 0.179% | 0.661% | 1.963% |
| λ = 0.001 | 0.396% | 0.660% | 1.853% |
| λ = 0.01 | 1.227% | 1.294% | 1.596% |
| λ = 0.1 | 1.884% | 1.928% | 2.072% |

Table 1. Mean probability of crossing misclassification under a uniform operating-gap distribution, expressed as a percentage. The 192-cell predictions cover 144 configurations and four signed slope cases with equal weights. The target is a model-based loss, not an observed switching frequency.

## Height accuracy and four-gap classification

The nominal unit model gives mean height error 0.07335 and 256 wrong gap decisions at each level. With exact slopes, fitting two zones resolves heterogeneity in the four in-family profiles. The residual two-zone error arises from the other two. At 1.5% the distal-soft family’s mean error falls from 0.00779 under repeated displacement to 0.00390 when angle is used. On the same family the wrong-decision count rises from zero to five. Improving estimates far from a gap can coexist with a small error on the wrong side of a particular gap.

At 5% relative perturbation, 48 of 576 angle-assisted estimates (8.33%) reach a clipping bound in at least one zone. The inversion amplifies distal slope errors, and the reported comparison includes the imposed bounds. Isolating the effect of clipping itself would require rerunning the estimator with different bounds.

| Slope perturbation | Calibration | Mean height error | Wrong / 2,304 |
| --- | --- | --- | --- |
| 0% | Repeat displacement | 0.00644 | 16 |
| 0% | Displacement + angle | 0.00157 | 4 |
| 1.5% | Repeat displacement | 0.00698 | 18 |
| 1.5% | Displacement + angle | 0.00478 | 19 |
| 5% | Repeat displacement | 0.00937 | 24 |
| 5% | Displacement + angle | 0.01439 | 49 |

Table 2. Original 96-cell calculations on four fixed thresholds. Mean absolute height error is measured in beam lengths. All results are descriptive of this finite design.

## A clearance distribution changes the value of angle sensing

An independent 192-cell implementation reproduces every four-gap count in Table 2. On 61 equally spaced gaps, the 1.5% ordering reverses. Repeated displacement gives 328 wrong decisions, while displacement plus angle gives 229 out of 35,136. At 5%, the respective counts are 441 and 730. In the limiting case where the gap is uniform over an interval, the probability of opposite decisions is the length of the interval between the two heights that lies inside the gap range, divided by that range. A dense equally weighted grid therefore tests a different objective from four discrete contacts.

The sensitivity calculation also holds displacement error at 1.5% and changes angle error alone. At 0.5% angle error, the angle-assisted model gives 23 mistakes on the four-gap grid. At 3% angle error it gives 19. The repeated-displacement count stays at 18. The corresponding angle-assisted 61-gap counts are 229 and 233. A one-count change on the original scoring grid cannot identify the better sensor for a device. Its relevant contact heights and error frequencies must be specified.

The apparent improvement on four gaps when angle-error magnitude increases from 0.5% to 3% has a direct case-level explanation. With displacement perturbation fixed at 1.5%, seven formerly wrong decisions cross back to the correct side and three formerly correct decisions cross to the wrong side (23 − 7 + 3 = 19). None of the ten changed decisions hits the compliance bounds at the larger perturbation. For example, a proximal-soft specimen of scale 1.5, length 0.85 and field 2 has reference height 0.59614. With two positive error signs its predicted height moves from 0.60100 to 0.59864 and crosses the 0.60 threshold. For a distal-soft specimen of scale 1, length 1.15 and field 2, the signs (−,+) shift the estimate from 0.45147 to 0.44825, crossing below 0.45 while the reference is 0.45801. The 61-gap count rises from 229 to 233 over the same change. A lower count on four selected gaps therefore does not identify a more accurate angle sensor.

| Slope errors (d, t) | Repeated, 4 gaps | Angle, 4 gaps | Repeated, 61 | Angle, 61 |
| --- | --- | --- | --- | --- |
| 0%, 0% | 16 | 4 | 296 | 68 |
| 1.5%, 1.5% | 18 | 19 | 328 | 229 |
| 5%, 5% | 24 | 49 | 441 | 730 |
| 1.5%, 0.5% | 18 | 23 | 328 | 229 |
| 1.5%, 3% | 18 | 19 | 328 | 233 |

Table 3. Wrong decisions from the 192-cell sensitivity calculation. Denominators are 2,304 for four gaps and 35,136 for 61 gaps. In the repeat model both readings receive the specified displacement error.

## External forward check on three published magnetic strips

Yan, Abbasi and Reis measured deflection and tip angle on three longitudinally magnetized, nominally uniform hard-magnetic strips in a transverse Helmholtz field [2, sections 5.2, 5.4 and 6.1, Fig. 6]. The colored experimental symbols in panels 6a and 6b were extracted from the vector PDF, excluding the FEM symbols and fitted curves. Of the 22 loads plotted per strip, eight nonzero loads per strip lie within the simulated loading range. The 24 retained measurements span approximately q = 0.419 to 4.071. The plotted coordinates have finite precision and the 24 readings are repeated loads on three strips.

The strips hang vertically. For a uniform strip, the gravity-aware comparison adds G(1 − s)sin θ to the moment derivative, with G = 12ρgL³/(Eh²), following their equation 64. Published mean dimensions L = 13.2 mm and h = 0.50 mm, density 2,010 kg/m³ and modulus 1.16 MPa give G = 1.877. Both versions use the reported dimensionless load with no fitted parameter. Mean absolute discrepancies were 0.0499 beam lengths and 5.10° without gravity and 0.0153 beam lengths and 1.72° with gravity. Scored against 61 hypothetical gaps per load, the corresponding wrong decisions were 120 and 42 of 1,464. No physical contacts were measured. The published Fig. 6 specimens do not provide a two-zone matched-slope pair, so this comparison tests the physical forward response of a uniform strip and the effect of an omitted load.

## Solver agreement and the remaining calibration experiment

The primary solver integrates torque backward from the free tip and curvature forward from the clamp on 96 cells. All quarter-length interfaces lie on cell boundaries. An adaptive collocation solver imposes continuity across those interfaces for three profiles at compliance scale 1.5 across all eight field-length pairs. Its largest absolute discrepancy is below 0.00000814 beam lengths at 96 cells and 0.00000204 at 192 cells. A separate piecewise shooting calculation in the supplement reproduced these error scales for uniform, matched-slope and alternating profiles. All solvers share the same equilibrium equations.

The main calibration model leaves out clamp flexibility, field gradients, rate-dependent response and post-contact forces. Slopes measured on a bench require multiple applied fields, and the relative cost and errors of optical angle and displacement channels remain unknown. A transfer test would measure both channels on matched-slope coupons, make blind height and crossing predictions for predefined contacts, and compare them with independent observations. Current results concern pre-contact heights and assigned thresholds. They provide no measured switching, airway or safety performance.

## Data and code availability

The baseline repository contains the code, 5,184 predictions and 24 solver comparisons. Run python run.py and python verify.py in that checkout. The companion supplement includes clearance_sensitivity.py, its environment, its signed predictions, both gap-grid summaries and shooting comparisons. Run python clearance_sensitivity.py to regenerate all three supplemental CSVs. All profiles are specified numerically. The supplement includes separate Linux x86_64 environment locks for the baseline and revision. The new programs gap_risk.py and published_beam.py regenerate the regularized decision risks, per-threshold reversals and the forward check on published experimental markers. The supplement gives the source PDF hash and a script for extracting the markers from the separately obtained PDF. Per-marker vectors and the source figure are excluded from redistribution.

[Pinned baseline](https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/48461d762b32c54be2fff4e839d2522956a14515) · [Revision code and data](https://github.com/VEDANT1602/magnetic-cantilever-clearance/tree/main/revision/supplement) · [Preparation record](https://github.com/VEDANT1602/magnetic-cantilever-clearance/blob/main/revision/PREPARATION.md)

## Computational verification

A fresh run reproduced the archived prediction and validation fields to within 2.23 × 10⁻¹⁶ absolute difference. The original verifier reconstructed the six height-error and gap-decision rows and both resolution bounds. The new implementation recovered all four-gap counts at 192 cells and added the dense-gap, unequal-error and shooting checks. The bounded solver checks the interior and every box edge. The supplied transition ledger identifies all ten changed decisions between the unequal-error cases. The physical forward check uses the published Fig. 6 experimental markers and measured mean material properties. Its digitized heights are approximate.

## Author contribution

Vedant Thaker is the sole author. He designed the original magnetic cantilever calibration study, wrote its manuscript, developed its original software, and requested the comparisons and checks reported in this revision.

## Use of computational assistance

OpenAI Codex assisted with the bounded calibration and decision-loss calculations, solver and threshold checks, extraction of published strip-marker coordinates, and gravity-aware forward comparison, as well as literature checks and preparation of the revised text. The author set the research question and requested the revision.

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Competing interests

The author declares no competing interests.

## References

[1] L. Wang, Y. Kim, C. F. Guo and X. Zhao. Hard-magnetic elastica. Journal of the Mechanics and Physics of Solids 142, 104045 (2020). https://doi.org/10.1016/j.jmps.2020.104045

[2] D. Yan, A. Abbasi and P. M. Reis. A comprehensive framework for hard-magnetic beams: Reduced-order theory, 3D simulations, and experiments. International Journal of Solids and Structures 257, 111319 (2022). https://doi.org/10.1016/j.ijsolstr.2021.111319

[3] Y. Wang, M. Kim, H. Fan, R. Ge, D. Wang, F. Maldonado, C. Demarest, Y. Zhou and X. Dong. A miniature magnetic switch unlocking multimodal, chip-free, and batteryless airway sensing. Science Advances 12(16), eaed3998 (2026). https://doi.org/10.1126/sciadv.aed3998

[4] J.-D. Chang and B.-Z. Guo. Identification of variable spacial coefficients for a beam equation from boundary measurements. Automatica 43, 732–737 (2007). https://doi.org/10.1016/j.automatica.2006.11.002
