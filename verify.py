"""Check the manuscript table against tip heights and independent collocation results."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


GAPS = (0.15, 0.30, 0.45, 0.60)
EXPECTED = {
    (0.0, "two_y"): ("0.00644", 16),
    (0.0, "y_angle"): ("0.00157", 4),
    (0.015, "two_y"): ("0.00698", 18),
    (0.015, "y_angle"): ("0.00478", 19),
    (0.05, "two_y"): ("0.00937", 24),
    (0.05, "y_angle"): ("0.01439", 49),
}


def verify(directory):
    groups = defaultdict(list)
    with (directory / "results.csv").open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            groups[float(row["noise"]), row["model"]].append(
                (float(row["reference_y"]), float(row["predicted_y"])))
    for key, expected in EXPECTED.items():
        pairs = groups[key]
        if len(pairs) * len(GAPS) != 2304:
            raise ValueError(f"Incorrect decision denominator for {key}")
        error = mean(abs(ref - prediction) for ref, prediction in pairs)
        wrong = sum((ref >= gap) != (prediction >= gap) for ref, prediction in pairs for gap in GAPS)
        if (f"{error:.5f}", wrong) != expected:
            raise ValueError(f"{key} gave {error:.5f}, {wrong} errors. Expected {expected}")
    with (directory / "validation.csv").open(encoding="utf-8", newline="") as stream:
        checks = list(csv.DictReader(stream))
    if len(checks) != 24:
        raise ValueError("Expected 24 collocation comparisons")
    for field, bound in (("n96", 0.00000814), ("n192", 0.00000204)):
        worst = max(abs(float(row[field]) - float(row["collocation"])) for row in checks)
        if worst > bound:
            raise ValueError(f"{field} maximum solver discrepancy exceeded {bound}: {worst}")
    print("Verified all six clearance table rows and both spatial-resolution checks.")


if __name__ == "__main__":
    verify(Path(__file__).resolve().parent)
