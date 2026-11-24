"""Convert specimen-level protocol differences using the published mean length."""
import csv
from pathlib import Path
from statistics import mean, pstdev

DIRECTORY = Path(__file__).resolve().parent


def contrast(input_table):
    with input_table.open(newline="") as source:
        rows = [r for r in csv.DictReader(source)
                if r["training_indices"] == "1/2" and r["structure"] == "uniform"]
    by_strip = {}
    for r in rows:
        by_strip.setdefault(r["specimen"], {})[r["method"]] = float(r["mae_over_length"])
    with (DIRECTORY / "length_scale.csv").open("w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["specimen", "two_height_minus_mixed_fraction",
                         "um_at_common_13_2_mm", "length_covariance_bound_um"])
        diffs = []
        for strip, metrics in sorted(by_strip.items()):
            diff = metrics["two heights"] - metrics["height + angle"]
            diffs.append(diff)
            writer.writerow([strip, diff, 13200 * diff, ""])
        # Section 5.4 reports 13.2 mm mean and 0.2 mm SD, with rounding.
        # The population SD is no larger if 0.2 denotes the sample SD.
        # Cauchy–Schwarz bounds the unobserved covariance E[(L-E L)(d-E d)].
        writer.writerow(["mean", mean(diffs), 13200 * mean(diffs),
                         1000 * 0.2 * pstdev(diffs)])

    # With three specimens, a leave-one-out mean is the average of the other two
    # physical-strip contrasts. The signed sum is appropriate for the net change.
    scaled = dict(zip(sorted(by_strip), (13200 * d for d in diffs), strict=True))
    with (DIRECTORY / "specimen_influence.csv").open("w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["omitted_specimen", "remaining_specimens", "mean_change_um",
                         "omitted_pct_of_net_change"])
        for name, difference in scaled.items():
            others = [v for k, v in scaled.items() if k != name]
            writer.writerow([name, len(others), mean(others), 100 * difference / sum(scaled.values())])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, nargs="?", default=DIRECTORY/"strip_results.csv")
    contrast(parser.parse_args().input_csv)
