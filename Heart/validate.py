"""Check the published Heart table and, optionally, its UCI code crosswalk."""

import argparse
import csv
import hashlib
from collections import Counter
from pathlib import Path

DATA_HASH = "f0b030c6bd7d5342bc40e1c27582bff70cbbdb01efcf4181c732673093353551"
SOURCE_HASH = "a74b7efa387bc9d108d7d0115d831fe9b414b29ae7124f331b622b4efa0427c8"
COLUMNS = "id age sex cp trestbps chol fbs restecg thalach exang oldpeak slope ca thal diagnosis".split()
SOURCE_COLUMNS = COLUMNS[1:-1] + ["num"]
KEY = "age sex trestbps chol thalach oldpeak".split()
MAPS = {
    "cp": {0: 4, 1: 2, 2: 3, 3: 1},
    "restecg": {0: 2, 1: 0, 2: 1},
    "slope": {0: 3, 1: 2, 2: 1},
    "ca": {0: 0, 1: 1, 2: 2, 3: 3, 4: None},
    "thal": {0: None, 1: 6, 2: 3, 3: 7},
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def key(row):
    return tuple(row[name] for name in KEY)


def check(data, source=None):
    payload = data.read_bytes()
    require(not payload.startswith(b"version https://git-lfs.github.com/spec/v1"),
            "Heart.tsv is an LFS pointer. Download its payload first.")
    require(hashlib.sha256(payload).hexdigest() == DATA_HASH,
            "Data checksum differs from this documented release.")
    reader = csv.DictReader(payload.decode("utf-8").splitlines(), delimiter="\t")
    require(reader.fieldnames == COLUMNS, "Unexpected column names or order.")
    rows = [{name: float(value) for name, value in row.items()} for row in reader]
    require(len(rows) == 303, "Expected 303 rows.")
    require([row["id"] for row in rows] == list(range(1, 304)), "Unexpected row IDs.")
    require(Counter(row["diagnosis"] for row in rows) == {1: 165, 0: 138},
            "Unexpected diagnosis counts.")
    require(sum(row["ca"] == 4 for row in rows) == 5, "Expected five missing ca codes.")
    require(sum(row["thal"] == 0 for row in rows) == 2, "Expected two missing thal codes.")
    measurements = [tuple(row[name] for name in COLUMNS[1:]) for row in rows]
    require(len(set(measurements)) == 302 and measurements[163] == measurements[164],
            "Unexpected repeated-record pattern.")
    print("Heart.tsv: checksum and documented 303-row schema passed.")
    if source is None:
        return

    raw = source.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == SOURCE_HASH,
            "Source checksum differs from the audited processed Cleveland file.")
    original = []
    for values in csv.reader(raw.decode("utf-8").splitlines()):
        require(len(values) == len(SOURCE_COLUMNS), "Unexpected source column count.")
        original.append(dict(zip(SOURCE_COLUMNS,
                                 [None if value == "?" else float(value) for value in values])))
    require(len(original) == 303, "Expected 303 source records.")
    by_key = {key(row): row for row in original}
    require(len(by_key) == 303, "Source comparison keys are not unique.")
    seen = set()
    for row in rows:
        source_key = key(row)
        require(source_key in by_key, f"No source match for local row {int(row['id'])}.")
        original_row = by_key[source_key]
        seen.add(source_key)
        for name in COLUMNS[1:-1]:
            value = row[name]
            if name in MAPS:
                require(value in MAPS[name], f"Unexpected {name} code.")
                value = MAPS[name][value]
            require(value == original_row[name],
                    f"Crosswalk mismatch for {name}, local row {int(row['id'])}.")
        require(row["diagnosis"] == int(original_row["num"] == 0),
                f"Diagnosis mismatch for local row {int(row['id'])}.")
    require(len(seen) == 302, "Expected coverage of 302 distinct source records.")
    print("UCI comparison: all 303 local rows match; 302 distinct source records covered.")
    print("Known differences: one repeated local record and one unrepresented source record.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path(__file__).with_name("Heart.tsv"))
    parser.add_argument("--source", type=Path, help="Original processed.cleveland.data file")
    args = parser.parse_args()
    try:
        check(args.data, args.source)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
