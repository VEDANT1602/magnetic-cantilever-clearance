"""Calibration experiment for a planar magnetoelastic beam; Python 3, NumPy, SciPy."""
from pathlib import Path
import csv
from itertools import product

import numpy as np
from scipy.integrate import solve_bvp


ROOT = Path(__file__).resolve().parent
# Piecewise-constant compliance in four equal quarters, starting at the clamp.
FAMILIES = {"uniform": [1, 1, 1, 1], "base_soft": [1.4, 1.4, .6, .6],
            "tip_soft": [.6, .6, 1.4, 1.4], "matched_slope": [.9, .9, 1.7, 1.7],
            "short_patch": [1.6, .8, .8, .8], "alternating": [.65, 1.35, .65, 1.35]}
MATRIX = np.array([[7/24, 1/24], [3/8, 1/8]])


def predict(profiles, q, n=96):
    """Midpoint integration of moment from free end, angle from clamped end."""
    j = np.repeat(np.asarray(profiles), n // 4, axis=1)
    angle = np.zeros_like(j)
    for _ in range(340):
        load = q * np.cos(angle) / n
        moment = np.cumsum(load[:, ::-1], axis=1)[:, ::-1] - 0.5 * load
        bend = j * moment / n
        target = np.cumsum(bend, axis=1) - 0.5 * bend
        delta = target - angle
        if np.max(abs(delta)) < 2e-11:
            break
        angle += .23 * delta
    else:
        raise RuntimeError("Moment-angle iteration did not converge")
    return np.sin(angle).mean(axis=1)


def independent(profile, q):
    # Collocate four smooth subintervals, enforcing all interface conditions.
    def ode(x, states):
        d = np.zeros_like(states)
        for i, compliance in enumerate(profile):
            theta, moment, _ = states[3*i:3*i+3]
            d[3*i:3*i+3] = np.vstack([compliance * moment, -q * np.cos(theta), np.sin(theta)]) / 4
        return d
    def bc(a, b):
        return np.r_[a[0], a[2], b[10], b[:9] - a[3:]]
    x = np.linspace(0, 1, 12)
    sol = solve_bvp(ode, bc, x, np.zeros((12, len(x))), tol=2e-9)
    assert sol.success
    return sol.y[-1, -1]


def slopes(profile):
    edges = 1 - np.arange(5) / 4
    return np.array([np.dot((edges[:-1] ** p - edges[1:] ** p) / p, profile) for p in (3, 2)])


def main():
    configs, all_profiles = [], []
    for family, values in FAMILIES.items():
        for scale, noise, signs in product((.65, 1., 1.5), (0., .015, .05), list(product((-1, 1), repeat=2))):
            true = np.array(values) * scale
            dy, dt = slopes(true)
            y1, y2 = dy * (1 + noise * np.array(signs))
            a2 = dt * (1 + noise * signs[1])
            inferred = np.linalg.solve(MATRIX, [y1, a2])
            clipped = np.clip(inferred, .12, 4.)
            assert np.isclose(slopes(np.ones(4))[0], 1 / 3)
            methods = {"reference": true, "nominal": np.ones(4), "two_y": np.full(4, 1.5*(y1+y2)),
                       "y_angle": np.repeat(clipped, 2)}
            for method, model in methods.items():
                configs.append((family, scale, noise, *signs, method, int(np.any(clipped != inferred)) if method == "y_angle" else 0))
                all_profiles.append(model)
    all_profiles = np.array(all_profiles)
    unique, inverse = np.unique(all_profiles.round(13), axis=0, return_inverse=True)
    fields = "family compliance_scale noise sign1 sign2 model clipped length_ratio field q reference_y predicted_y".split()
    with (ROOT / "results.csv").open("w", newline="") as f, (ROOT / "validation.csv").open("w", newline="") as audit:
        w, v = csv.writer(f), csv.writer(audit)
        w.writerow(fields)
        v.writerow(["length_ratio","field","family","scale","n96","n192","collocation"])
        for length_ratio, field in product((.85, 1.15), (.4, 1., 2., 3.6)):
            q = field * length_ratio ** 2
            y = predict(unique, q)[inverse]
            for group in range(0, len(configs), 4):
                for idx in range(group+1, group+4):
                    w.writerow([*configs[idx], length_ratio, field, q, y[group], y[idx]])
            for family in ("base_soft","matched_slope","alternating"):
                p = np.array(FAMILIES[family], dtype=float) * 1.5
                lo, hi, cert = predict([p],q)[0], predict([p],q,192)[0], independent(p,q)
                assert abs(lo-cert) < .00008
                v.writerow([length_ratio, field, family, 1.5, lo, hi, cert])
    records = np.genfromtxt(ROOT / "results.csv", delimiter=",", names=True, dtype=None, encoding="utf-8")
    gaps = np.array([.15, .3, .45, .6])
    print("Relative slope perturbation, model, mean absolute height error, incorrect gap decisions, total decisions:")
    for noise, method in product((0, .015, .05), ("nominal", "two_y", "y_angle")):
        rows = records[(records["noise"] == noise) & (records["model"] == method)]
        ref, estimate = rows["reference_y"], rows["predicted_y"]
        wrong = (ref[:, None] >= gaps) != (estimate[:, None] >= gaps)
        print(noise, method, round(np.mean(abs(ref-estimate)), 5), wrong.sum(), wrong.size)


if __name__ == "__main__":
    main()
