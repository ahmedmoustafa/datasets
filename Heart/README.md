# Cleveland Heart Disease Data

This teaching dataset contains 303 rows and 15 columns: a row ID, 13 predictors, and a binary diagnosis label. It is a modified copy of the processed Cleveland data from the [UCI Heart Disease collection](https://doi.org/10.24432/C52P4X).

**In this file, `diagnosis = 1` means no disease and `diagnosis = 0` means disease.** The file contains 165 rows labeled 1 and 138 labeled 0. Several predictor codes also differ from the original UCI codes. Use the definitions below when working with this copy.

## Download and load

[Browse Heart.tsv](Heart.tsv) or [download the data](https://media.githubusercontent.com/media/ahmedmoustafa/datasets/4f2478a00774897b3a3cfce99466bc97a620eb5a/Heart/Heart.tsv). The download is pinned to the audited data version.

This UTF-8, tab-separated file is 12,131 bytes. Git stores it with Git LFS. The usual raw GitHub URL may return a pointer instead of the data. After cloning the repository, run this command from its root:

```sh
git lfs pull --include="Heart/Heart.tsv"
```

Python, with pandas installed:

```python
import pandas as pd

url = "https://media.githubusercontent.com/media/ahmedmoustafa/datasets/4f2478a00774897b3a3cfce99466bc97a620eb5a/Heart/Heart.tsv"
heart = pd.read_csv(url, sep="\t")
assert heart.shape == (303, 15)
assert "diagnosis" in heart.columns
```

R:

```r
url <- "https://media.githubusercontent.com/media/ahmedmoustafa/datasets/4f2478a00774897b3a3cfce99466bc97a620eb5a/Heart/Heart.tsv"
heart <- read.delim(url)
stopifnot(nrow(heart) == 303, ncol(heart) == 15)
stopifnot("diagnosis" %in% names(heart))
```

## Data dictionary

The codes in this table describe the local file, not the original UCI file.

| Column | Definition in this file |
| --- | --- |
| `id` | Local row ID; not a verified participant identifier. |
| `age` | Age in years. |
| `sex` | Recorded sex: 0 = female, 1 = male. |
| `cp` | Chest pain: 0 = asymptomatic, 1 = atypical angina, 2 = non-anginal pain, 3 = typical angina. |
| `trestbps` | Resting blood pressure, mm Hg. |
| `chol` | Serum cholesterol, mg/dL. |
| `fbs` | Fasting blood sugar above 120 mg/dL: 0 = no, 1 = yes. |
| `restecg` | Resting ECG: 0 = probable/definite left ventricular hypertrophy, 1 = normal, 2 = ST-T wave abnormality. |
| `thalach` | Maximum heart rate achieved, beats per minute. |
| `exang` | Exercise-induced angina: 0 = no, 1 = yes. |
| `oldpeak` | Exercise-induced ST depression relative to rest. |
| `slope` | Peak exercise ST segment: 0 = downsloping, 1 = flat, 2 = upsloping. |
| `ca` | Major vessels seen by fluoroscopy: 0–3; 4 represents a missing source value. |
| `thal` | Thallium test: 1 = fixed defect, 2 = normal, 3 = reversible defect; 0 represents a missing source value. |
| `diagnosis` | Binary outcome: 0 = disease present, 1 = disease absent. |

## Missing values and record differences

The table has no empty cells, but it does contain missing-value codes. Treat `ca = 4` (five rows) and `thal = 0` (two rows) as missing during analysis. Do not interpret them as measured clinical categories.

Rows with IDs 164 and 165 have identical values in all columns except `id`. Comparison with the original processed Cleveland file maps both to the same source record. Another source record has no match in this copy. The 303 local rows therefore match 302 distinct source records; this file is not an exact copy of the original 303-record cohort.

The local recoding was checked against the original file using age, sex, resting blood pressure, cholesterol, maximum heart rate, and ST depression as a composite key. These keys are unique in the source. The crosswalk is:

| Field | Local code → original UCI code |
| --- | --- |
| `cp` | 0 → 4; 1 → 2; 2 → 3; 3 → 1 |
| `restecg` | 0 → 2; 1 → 0; 2 → 1 |
| `slope` | 0 → 3; 1 → 2; 2 → 1 |
| `ca` | 0–3 unchanged; 4 → missing |
| `thal` | 0 → missing; 1 → 6; 2 → 3; 3 → 7 |
| `diagnosis` | 1 → UCI `num = 0`; 0 → UCI `num` in 1–4 |

The original transformation script is not available. The September 2026 documentation correction preserves the existing table, including its repeated record and missing-value codes. It does not reconstruct or replace the original cohort.

## Appropriate use

Use this copy for learning data loading, categorical encoding, missing-value handling, and exploratory analysis. It is a historical clinical sample, not a representative population survey or a validated diagnostic tool. Associations do not establish causes. Keep the repeated record together when splitting data, and fit preprocessing on training data only.

For research that requires the original Cleveland cohort, obtain the source file directly and document its version and your preprocessing.

## Source, citation, and license

Janosi, A., Steinbrunn, W., Pfisterer, M., and Detrano, R. (1989). *Heart Disease* [Dataset]. UCI Machine Learning Repository. [doi:10.24432/C52P4X](https://doi.org/10.24432/C52P4X).

UCI distributes the source dataset under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). That license applies to the source data in this directory; the repository's general CC0 notice does not replace it. Retain the citation, license link, and a description of modifications when redistributing this copy. The local modifications identified here are row IDs, category recoding, a binary outcome, missing-value codes, and the record differences described above.

## Verify this version

After downloading the LFS payload, run from the repository root:

```sh
python3 Heart/validate.py
```

To also check the code crosswalk against an independently downloaded `processed.cleveland.data` file:

```sh
python3 Heart/validate.py --source /path/to/processed.cleveland.data
```

The validator uses the Python standard library. It checks this release's checksum, shape, IDs, label counts, missing-value codes, and repeated record. With `--source`, it also checks all matched fields and reports the source record coverage. A changed data release needs a reviewed update to these expectations.
