"""Recompute the reported specimen and field-window comparisons from the released tables."""
import csv
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
with (HERE / "strip_results.csv").open() as stream:
    entries = list(csv.DictReader(stream))
errors = {}
for row in entries:
    if row["structure"] == "uniform":
        key = (row["specimen"], row["training_indices"], row["method"])
        assert key not in errors and int(row["heldout_count"]) == 18
        errors[key] = 100 * float(row["mae_over_length"])

expected = {"1/2": [0.107, 0.011, -0.003],
            "1/3": [0.132, 0.006, -0.002],
            "2/3": [0.064, -0.065, -0.161]}
strips = ("s1-1", "s1-2", "s1-3")
for window, contrasts in expected.items():
    values = [errors[strip, window, "two heights"] - errors[strip, window, "height + angle"]
              for strip in strips]
    assert [round(value, 3) for value in values] == contrasts

for window, pair in (("1/2", (0.731, 0.693)), ("2/3", (0.805, 0.859))):
    observed = tuple(round(mean(errors[strip, window, method] for strip in strips), 3)
                     for method in ("two heights", "height + angle"))
    assert observed == pair
with (HERE / "reading_sensitivity.csv").open() as stream:
    signed = [-100 * float(row["dual_minus_height"]) for row in csv.DictReader(stream)]
assert len(signed) == 8 and sum(x > 0 for x in signed) == sum(x < 0 for x in signed) == 4
assert (round(min(signed), 3), round(max(signed), 3)) == (-0.057, 0.084)
print("Confirmed three strips × three windows, held-out means, and the 4–4 perturbation split.")
