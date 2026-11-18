# Two weak-field measurements for predicting magnetic cantilever clearance

**Vedant Thaker**  
Working paper · 18 November 2026

## Abstract

A magnetic cantilever that matches a small-field deflection can still miss a clearance threshold in a stronger field. Tip displacement gives one weighted average of bending compliance. Measuring the tip angle supplies a second average and can distinguish two compliance regions, although the inversion amplifies measurement error. Across 144 synthetic configurations of compliance profile, stiffness scale, field and length, we compare two displacement readings with one displacement and one angle reading. With exact calibration, adding the angle reduces mean tip displacement error from 0.00644 to 0.00157 beam lengths. With signed perturbations of 1.5%, it still lowers mean error but produces 19 incorrect clearance decisions across 2,304 determinations, compared with 18 for repeated displacement. At 5%, repeated displacement performs better on both measures. A calibration bench intended to predict clearance must resolve how often the measured error changes the threshold decision.

## The calibration decision

A flexible probe must cross a gap before it can touch a contact. A small-field displacement can be measured without contact, then used to predict clearance under a stronger field. It is tempting to fit a single bending stiffness to the first measurement. That fit quietly assumes that changes near the clamp and changes near the tip affect all operating points in the same way.

Wang, Kim, Guo and Zhao developed the nonlinear hard-magnetic elastica for large deflections [1]. Yan, Abbasi and Reis compared reduced beam models with three-dimensional simulations and cantilever experiments in uniform and gradient fields [2]. A different application of magnetic deflection appears in the miniature multichannel switch of Wang and colleagues, whose steerable probe connects an induction circuit to selectable sensors [3]. The present calculation isolates the clearance question that precedes contact. It considers a planar, continuously magnetized strip with a single geometric threshold. Reconstructing a multichannel device would also require its probe geometry, magnetization, contact forces and electrical behaviour.

The comparison uses two scalar calibration readings per specimen. One option repeats tip displacement to average down measurement error. The other spends the second reading on tip angle. A mathematical example establishes what angle resolves in ideal conditions. A finite-field calculation then tests whether the extra information survives perturbation strongly enough to help with a clearance decision.

## A beam with spatially varying bending compliance

Let s measure arc length from the clamp on the unit interval. Let J(s) be the ratio of a reference bending rigidity to local bending rigidity, so a higher J denotes a more compliant segment. The strip is slender, inextensible and initially straight, with uniform remanent magnetization along its local tangent. A spatially uniform transverse field exerts distributed torque. If q is the field-induced torque per unit length at zero deflection times length squared divided by reference bending rigidity, the dimensionless equations are angle' = J times moment, moment' = -q cos(angle), and height' = sin(angle). The clamp angle and height vanish. The free-end moment is zero. The predicted output is tip height divided by beam length.

In the weak-field limit, moment is q times (1 - s). Integrating curvature once gives the tip-angle slope t = integral of (1 - s) J(s). Integrating the angle through the length gives the normalized tip-displacement slope d = integral of (1 - s) squared times J(s). Each integral runs from clamp to tip. For equal-length proximal and distal zones with compliances P and D, these reduce to d = (7P + D)/24 and t = (3P + D)/8.

This pair of equations illustrates the problem with a single displacement fit. A uniform beam P = D = 1 and a beam with P = 0.9 and D = 1.7 have exactly the same displacement slope, one third. Their angle slopes are 0.50 and 0.55. Recovering both zones gives P = 6d - 2t and D = -18d + 14t. The relatively large coefficients in the second expression reveal the cost of identifying distal compliance. Two nearly equal slope measurements can lead to appreciably different inferred distal stiffnesses.

## Calibration and test cases

Six compliance profiles use four equal-length segments. In clamp-to-tip order, the profiles are (1, 1, 1, 1), (1.4, 1.4, 0.6, 0.6), (0.6, 0.6, 1.4, 1.4), (0.9, 0.9, 1.7, 1.7), (1.6, 0.8, 0.8, 0.8) and (0.65, 1.35, 0.65, 1.35). Each is multiplied by 0.65, 1 or 1.5. The first four fit the two-zone assumption exactly. The localized and alternating profiles deliberately violate it. This leaves a controlled source of error even with exact calibration slopes.

The nominal model uses one uniform reference throughout. The repeated-displacement model estimates homogeneous compliance as three times the mean observed displacement slope. The angle-assisted model solves for P and D from one observed d and one observed t. Inferred zone compliances are clipped to [0.12, 4], outside the full range of the true design. The cap prevents a nonphysical negative compliance from entering the response model. It is part of the tested estimator.

Calibration readings are perturbed by 0%, 1.5% or 5% of their exact slope. At each nonzero level, the four sign pairs (++,+-,-+,--) give an equally weighted error grid. The first sign affects the first displacement reading. The second sign affects either the repeated displacement or the angle. Repeated displacement therefore benefits from averaging when signs differ. These are deterministic perturbations of a measured slope. An experimental estimate of a slope would itself require measurements at multiple applied fields. Counting two slope channels as equally costly leaves the relative cost of optical angle and displacement estimation unresolved.

The finite-field tests cross lengths 0.85 and 1.15 relative to the reference length with four relative field levels of 0.4, 1, 2 and 3.6. Thus q ranges from 0.289 to 4.761. The four gap heights are 0.15, 0.30, 0.45 and 0.60 times the current beam length. A clearance prediction is positive when the tip reaches or exceeds the gap. Truth refers to the solution for the generated compliance profile under the same beam equations. No experimental calibrations are used.

## Does the second observable earn its place?

Table 1 pairs mean absolute tip-height error, in beam lengths, with the number of wrong gap decisions. At each perturbation level the denominator is 144 operating cases times four sign assignments times four gaps, or 2,304 decisions. The zero-error sign assignments are identical replicates included only to keep denominators comparable.

| Slope perturbation | Calibration | Mean height error | Wrong gap decisions |
|---|---|---:|---:|
| 0% | Repeated displacement | 0.00644 | 16 |
| 0% | Displacement and angle | 0.00157 | 4 |
| 1.5% | Repeated displacement | 0.00698 | 18 |
| 1.5% | Displacement and angle | 0.00478 | 19 |
| 5% | Repeated displacement | 0.00937 | 24 |
| 5% | Displacement and angle | 0.01439 | 49 |

The nominal uniform model has mean height error 0.07335 and makes 256 wrong decisions at each perturbation level. Calibrating each specimen accounts for most of the improvement. At exact calibration, the two-zone model further reduces height error because two slopes determine both unknown compliances in four of the six families. Residual error comes from profiles outside that model. In the equal-slope witness at q = 4.761, numerical tip heights are 0.70476 and 0.68690 for the uniform and matched-slope beams. A gap at 0.695 beam lengths would separate their decisions even though their weak-field displacement readings coincide. That illustrative gap lies outside the four-gap scoring grid.

The 1.5% results show why the choice of outcome matters. For the distal-soft family the angle-assisted model has mean error 0.00390, about half the repeated-displacement error of 0.00779, yet makes five wrong gap decisions where repeated displacement makes none. Displacement errors can shrink far away from all four thresholds and grow slightly near one of them. At 5%, the imposed bounds clip an inferred zone compliance in 8.33% of angle-assisted cases. The noise amplification is large enough to reverse even the mean-error ranking. The clipping rule also contributes to the numerical ranking in that regime.

## Numerical checks and physical limits

The reference calculation integrates distributed torque backward from the free end and curvature forward from the clamp, iterating the two fields on 96 equal cells. Quarter-length interfaces land on cell boundaries. An independent adaptive collocation solver integrates angle, moment and height on four separate subintervals and enforces continuity at each interface. It checks three profiles at compliance scale 1.5 under all eight length-field combinations. The maximum absolute discrepancy is 0.00000814 beam lengths on the 96-cell grid and 0.00000204 on a 192-cell grid. Agreement checks the numerical solution of the chosen equations. A biased magnetization estimate, clamp compliance, field gradient or rate-dependent polymer response could produce a larger, shared error in the physical model.

The prescribed perturbations cover relative slope error with equal positive and negative signs. They do not represent a measured noise distribution. Tip direction recovered from a short image segment may have substantial systematic error, particularly at weak fields. A specimen's contact state can also change the force balance after first touch. A clearance crossing alone cannot establish electrical connection, switching reliability or operating safety. No medical performance is inferred.

## Conclusion and reproducibility

Two observables identify a two-zone compliance profile in the small-field model. Whether that matters at operating field depends on angle precision and how closely the operating height approaches a contact. A bench test could image matched-slope coupons at low fields, independently measure clamp-to-tip stiffness variation and blind the clearance predictions before increasing the field. Measuring both the tip-height residual and the contact outcome would distinguish parameter recovery from the decision the device must make.

Running `python run.py` regenerates results.csv and validation.csv. The first contains all predictions, reference heights, calibration perturbations and model bounds flags. The second contains the independent solver comparisons. The study used Python 3.11.9, NumPy 1.26.0 and SciPy 1.11.2.

## Research and writing assistance

Vedant Thaker supplied the research brief and source materials. OpenAI Codex assisted with study design, implementation, execution, literature review and drafting. Clever Humanizer suggested edits to the abstract. The final wording was checked against the analysis.

## References

[1] L. Wang, Y. Kim, C. F. Guo and X. Zhao. Hard-magnetic elastica. Journal of the Mechanics and Physics of Solids 142, 104045 (2020). https://doi.org/10.1016/j.jmps.2020.104045

[2] D. Yan, A. Abbasi and P. M. Reis. A comprehensive framework for hard-magnetic beams: reduced-order theory, 3D simulations, and experiments. Author preprint (2021). https://arxiv.org/abs/2106.14878

[3] Y. Wang and colleagues, including X. Dong. A miniature magnetic switch unlocking multimodal, chip-free, and batteryless airway sensing. Science Advances 12, eaed3998 (2026). https://doi.org/10.1126/sciadv.aed3998
