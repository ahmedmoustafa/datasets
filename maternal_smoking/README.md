# Maternal Smoking and Birth Weight

![Maternal Smoking](images/smoking.jpeg)

Maternal smoking has been shown to have harmful effects on the newborn, including reduced birth weight. This [dataset](maternal_smoking.tsv) is a subset of a much larger study by the Child Health and Development Study (CHDS) that was conducted over several years.

The columns included in the subset described in the table below:

| Column | Description |
| -- | -- |
| `id` | id number |
| `date` | birth date |
| `gestation` | gestation days |
| `weight` | birth weight in ounce (`999` unknown) |
| `parity` | `0`=first born |
| `mom.race` | mom race |
| `mom.age` | mom age in years |
| `mom.edu` | mom eduction `0`=(<8), `1`=(8-<12), `2`=12, `3`=12+trade, `4`=12+some college, `5`=16, `6`, `7` trade (hs unclear), `9` = unknown |
| `mom.height` | mom height in inches |
| `mom.weight` | mom prepreganncy weight in pounds |
| `dad.race` | dad race |
| `dad.age` | dad age |
| `dad.edu` | dad eduction |
| `dad.height` | dad height |
| `dad.weight` | dad weight |
| `marital` | `1`=married, `2`=seperated, `3`=divorced, `4`=widowed, `5`=never married |
| `income` | total income in 2500 increements `0`=under 2500, `1`=2500-4999, ...., `9`=15000+, `98`=unknown, `99`=not asked |
| `smoke` | mom smoking
| `quit.time` | how long ago quit `0`=never, `1`=still, `2`=during preggancy, `3`=1 year, `4`=2 years, `5`=3 years, `6`=4 years, `7`=5-9 years, `8`=10+ years, `9`=quit and don't know when, `98`=unknown |
| `cigs` | number of cigs smoked a day for past and current smokers `0`=never, `1`=1-4, `2`=5-9, `3`=10-14, `4`=15-19, `5`=20-29, `6`=30-39, `7`=40-60, `8`=60+, `9`=smoke but don't know, `98`=unknown |

Given the [dataset](maternal_smoking.tsv), address the following questions visually and numerically, if possible, and state your conclusion:

<img src="images/baby.jpeg" width="300px" align="right" style="border-radius: 30px;">

- **Q1.** How many unique entries are in the following categorical column (`mom.race` and `smoke`)?
- **Q2.** What are the average ages of mothers and fathers in the dataset?
- **Q3.** What percentage of mothers never smoked, smoked until pregnancy, or smoked throughout?
- **Q4.** What is the average number of cigarettes smoked per day among mothers who smoked throughout their pregnancy?
- **Q5.** Show the distribution of newborns' weights.
- **Q6.** Does the mom's smoking pattern affect the newborn birth weight?
- **Q7.** Does the mom’s race affect the newborn birth weight?
- **Q8.** Is there a correlation between the mom’s weight and the baby’s weight?
- **Q9.** Is there a correlation between the dad’s weight and the baby’s weight?
- **Q10.** From Q3 and Q4, which is a stronger correlation?
- **Q11.** Is there a correlation between the mom’s weight and the dad’s weight?
- **Q12.** On average, does the mom’s weight change across the races?
- **Q13.** Does mom’s smoking pattern change with the mom’s education?
- **Q14.** Does mom’s smoking pattern change with the family income?
- **Q15.** Is there a relationship between the mom’s race and the dad’s race?

You can start by opening the following notebook using Google Colaboratory then *copying* it into your Google Drive:

- [Python notebook](maternal_smoking_py.ipynb)
- [R notebook](maternal_smoking_r.ipynb)

## Resources
Here are some cheat sheets that might be helpful:

- Python
	- [`pandas`](resources/python_pandas_cheatsheet.pdf)
	- [`matplotlib`](resources/python_matplotlib_cheatsheet.pdf)
	- [`seaborn`](resources/python_seaborn_cheatsheet.pdf)
- R
	- [`dplyr`](resources/r_dplyr_cheatsheet.pdf)
	- [`ggplot2`](resources/r_ggplot_cheatsheet.pdf)
- [Visual Vocabulary](resources/visual_vocabulary.pdf)
