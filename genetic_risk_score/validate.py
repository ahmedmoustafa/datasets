"""Validate the fictional marker table and the lesson's arithmetic examples."""

import csv
import math
import tempfile
from pathlib import Path

from generate import MARKERS, ROWS, generate


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    path = Path(__file__).with_name("toy_genotypes.csv")
    with tempfile.TemporaryDirectory() as directory:
        regenerated = Path(directory) / path.name
        generate(regenerated)
        require(path.read_bytes() == regenerated.read_bytes(), "Regeneration differs.")
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        require(reader.fieldnames == ["record_id"] + [m[0] for m in MARKERS],
                "Unexpected columns.")
        rows = list(reader)
    require(len(rows) == ROWS, "Unexpected row count.")
    require([int(row["record_id"]) for row in rows] == list(range(1, ROWS + 1)),
            "Unexpected IDs.")
    multipliers = [1.6, 1.3, 1.5, 1.2, 1.4]
    scores = []
    for row in rows:
        score = 0.0
        for (name, counted, other, _), multiplier in zip(MARKERS, multipliers):
            pair = row[name]
            require(len(pair) == 2 and set(pair) <= {counted, other},
                    f"Invalid symbols in {name}.")
            require(pair == "".join(sorted(pair)), "Unsorted symbol pair.")
            score += pair.count(counted) * math.log(multiplier)
        scores.append(score)
    maximum = 2 * sum(math.log(value) for value in multipliers)
    require(all(0 <= score <= maximum for score in scores), "Score outside bounds.")
    require(math.isclose(scores[0], math.log(1.3) + math.log(1.4)),
            "First-record calculation differs.")
    order = sorted(range(ROWS), key=lambda i: (-scores[i], int(rows[i]["record_id"])))
    cutoff = scores[order[49]]
    print("Passed: exact regeneration, 1,000 records, valid symbols, and example score.")
    print(f"First score: {scores[0]:.6f}; 50th score: {cutoff:.6f}")
    print(f"Records at or above cutoff: {sum(score >= cutoff for score in scores)}")


if __name__ == "__main__":
    main()
