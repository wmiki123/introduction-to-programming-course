# Lab 06: CSV Files, pandas, and Your First Script

Introduction to Programming | 17 November 2026

Complete A1 and A2 in `lab06_csv_to_scripts.ipynb`, then C1–C3 in `LAB06.md` using `scene_report.py`. Homework uses a separate, supplied `home_selection.py` starter.

## Session plan

| Activity | Minutes |
|---|---:|
| Setup | 5 |
| A1: CSV loading and inspection | 10 |
| A2: write a classifier and selection loop | 20 |
| C1–C3: execute a script, build a report, count statuses | 25 |
| Compare results and explain | 5 |
| Separate individual quiz | 15 |
| Save and commit | 5 |
| Buffer | 5 |
| Total | 90 |

The required coding and review portion is about an hour. The quiz is provided separately and is not in this student package. Homework is one small selection function plus two manual comparisons, planned for 30–40 minutes. No assertions or separate test suite are required.

## Setup

Copy the folder into your course repository as `lab06`, keeping the notebook, scripts, guide, and data folder together. If the repository root is your current folder, navigate into the lab:

```bash
cd lab06
```

Use your existing course environment. Check pandas:

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

If pandas is missing, install it in the existing course environment:

```bash
conda install pandas
```

Launch JupyterLab from this folder if needed:

```bash
python -m jupyterlab
```

Open the notebook with the course Python kernel. Its relative input path assumes the working folder contains `data/`. If a file is not found, check the notebook kernel's folder in a temporary code cell:

```python
from pathlib import Path
print(Path.cwd())
```

For the script portion, open this folder in VS Code and select the existing course Python interpreter, or use another text editor and the same terminal. Save the file, then execute:

```bash
python scene_report.py
```

The script can run before the tasks are complete, but it initially produces an empty report and zero counts. Complete the marked functions to obtain the required results. Input loading, paths, output writing, and the entry point are supplied support code.

The CSVs are synthetic teaching records. Required columns and parseable numbers are guaranteed. Invalid physical values are intentional inputs to the classifier. Scientific data downloads, missing value treatment, command line arguments, and advanced pandas operations are not part of this lab.

## Files to use

| File | Purpose |
|---|---|
| lab06_csv_to_scripts.ipynb | A1 and A2 only |
| LAB06.md | Class script tasks and short homework |
| scene_report.py | Class script with two functions to complete |
| home_selection.py | Home script with one function to complete |
| lab06_notes.md | Short answer and comparison template |
| data/scenes.csv | Class input |
| data/home_scenes.csv | Home input |
| requirements.txt | Additional Python dependency |

Keep source and original inputs in Git. The included `.gitignore` excludes generated results, notebook checkpoints, and Python caches. No instructor solutions or actual quiz questions are included.

## Reference documentation

- pandas import and inspection: https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html
- Table to dictionaries: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
- CSV output: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
- VS Code Python introduction: https://code.visualstudio.com/docs/python/python-tutorial
