"""Generate fictional diploid markers for a weighted-score exercise."""

import argparse
import csv
import random
from pathlib import Path

SEED = 20260930
ROWS = 1000
# Marker, counted symbol, other symbol, counted-symbol probability.
# All names and probabilities are illustrative, not biological estimates.
MARKERS = [
    ("marker_1", "C", "A", 0.25),
    ("marker_2", "G", "A", 0.30),
    ("marker_3", "G", "A", 0.20),
    ("marker_4", "A", "T", 0.35),
    ("marker_5", "T", "A", 0.25),
]


def generate(output):
    rng = random.Random(SEED)
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["record_id"] + [marker[0] for marker in MARKERS])
        for record_id in range(1, ROWS + 1):
            row = [record_id]
            for _, counted, other, probability in MARKERS:
                pair = [counted if rng.random() < probability else other for _ in range(2)]
                row.append("".join(sorted(pair)))
            writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("toy_genotypes.csv"))
    args = parser.parse_args()
    generate(args.output)


if __name__ == "__main__":
    main()
