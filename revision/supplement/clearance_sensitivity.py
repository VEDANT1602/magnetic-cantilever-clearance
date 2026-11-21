"""Independent numerical reconstruction of the pre-contact cantilever benchmark."""
import csv
from itertools import product
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

OUT = Path(__file__).resolve().parent
PROFILES = {
    "uniform": (1, 1, 1, 1),
    "proximal_soft": (1.4, 1.4, .6, .6),
    "distal_soft": (.6, .6, 1.4, 1.4),
    "matched_slope": (.9, .9, 1.7, 1.7),
    "localized": (1.6, .8, .8, .8),
    "alternating": (.65, 1.35, .65, 1.35)}
GAPS = np.array([.15, .30, .45, .60])
ALTERNATE_GAPS = np.arange(.1, .701, .01)


def slopes(profile):
    ends = 1 - np.linspace(0, 1, 5)
    return [sum(profile * -np.diff(ends**power) / power) for power in [3, 2]]


def height(profile, q, cells=192):
    """Damped midpoint iteration on the branch reached from the straight state."""
    if cells % 4:
        raise ValueError("Quartile interfaces must lie on cell boundaries.")
    j = np.repeat(profile, cells // 4)
    theta = np.zeros(cells)
    for _ in range(1200):
        torque = q * np.cos(theta) / cells
        moment_mid = np.cumsum(torque[::-1])[::-1] - .5 * torque
        bend = j * moment_mid / cells
        new_theta = np.cumsum(bend) - .5 * bend
        if np.max(np.abs(new_theta - theta)) < 2e-12:
            return np.sin(new_theta).mean()
        theta += .3 * (new_theta - theta)
    raise RuntimeError("Boundary-value iteration failed")


def shooting_height(profile, q):
    """Independent piecewise initial-value solves plus a scalar free-tip condition."""
    def solve(m0):
        state = [0., m0, 0.]
        for j in profile:
            def ode(_, y):
                return [j*y[1], -q*np.cos(y[0]), np.sin(y[0])]
            result = solve_ivp(ode, [0, .25], state, rtol=1e-10, atol=1e-12, method="DOP853")
            if not result.success:
                raise RuntimeError(result.message)
            state = result.y[:, -1]
        return state
    m0 = brentq(lambda m: solve(m)[1], 0, q, xtol=1e-12)
    return solve(m0)[2]


def save(path, rows):
    with (OUT / path).open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)


def main():
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def cached(profile, q):
        return height(profile, q)
    items = []
    for displacement_error, angle_error in [(0,0), (.015,.015), (.05,.05), (.015,.005), (.015,.030)]:
        for (family, base), scale, length, field in product(PROFILES.items(), [.65,1,1.5], [.85,1.15], [.4,1.,2.,3.6]):
            true_j = tuple(np.array(base)*scale)
            q = length**2 * field
            actual = cached(true_j, q)
            d, t = slopes(true_j)
            for s1, s2 in product([-1,1],repeat=2):
                d1, d2 = d*(1+s1*displacement_error), d*(1+s2*displacement_error)
                t2 = t*(1+s2*angle_error)
                p, z = 6*d1-2*t2, -18*d1+14*t2
                fits = {"repeat": (1.5*(d1 + d2),)*4, "angle": (p,p,z,z)}
                for method, fit in fits.items():
                    fitted = tuple(np.clip(fit,.12,4))
                    pred = cached(fitted, q)
                    discrete = np.count_nonzero((pred>=GAPS) != (actual>=GAPS))
                    dense = np.count_nonzero((pred>=ALTERNATE_GAPS) != (actual>=ALTERNATE_GAPS))
                    items.append(dict(d_error=displacement_error, t_error=angle_error, family=family,
                               scale=scale,length=length,field=field,sign_d=s1,sign_other=s2,
                               method=method,true_height=actual,predicted_height=pred,clipped=(fit!=fitted),
                               absolute_error=abs(pred-actual),wrong_four=discrete,wrong_61=dense))
    save("clearance_predictions.csv",items)
    summaries=[]
    for de, te, method in dict.fromkeys((r["d_error"],r["t_error"],r["method"]) for r in items):
        group=[r for r in items if (r["d_error"],r["t_error"],r["method"])==(de,te,method)]
        summaries.append(dict(displacement_error=de,angle_error=te,method=method,n=len(group),
                    mean_error=np.mean([r["absolute_error"] for r in group]),
                    wrong_four=sum(r["wrong_four"] for r in group),
                    wrong_61=sum(r["wrong_61"] for r in group),
                    clipped=sum(r["clipped"] for r in group)))
    save("clearance_sensitivity.csv",summaries)
    check=[]
    for name in ["uniform","matched_slope","alternating"]:
        profile=np.array(PROFILES[name])*1.5
        for length,field in product([.85,1.15],[.4,1.,2.,3.6]):
            q=length**2*field
            independent=shooting_height(profile,q)
            for cells in [96,192]:
                estimate=height(profile,q,cells)
                check.append(dict(profile=name,length=length,field=field,cells=cells,
                             shooting=independent,midpoint=estimate,difference=abs(estimate-independent)))
    save("shooting_check.csv",check)


if __name__ == "__main__":
    main()
