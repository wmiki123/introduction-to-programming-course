# Lab 06: continue with scripts

Complete notebook A1 and A2 first. Use VS Code or a text editor from this point. Record short answers in the supplied `lab06_notes.md`. Class coding and review take about 60 minutes in total, including the notebook. A separate 15 minute quiz is reserved in the 90 minute session.

## C1. Run a Python file | about 5 minutes

Open `scene_report.py`. Locate the settings, the supplied `assess_scene` function, the two unfinished functions, and `main`.

The supplied classifier uses the same rules you implemented in A2, so you can continue even if your notebook version needs more work. The script's input and output code is already complete. You will write its processing loops.

From a terminal in this folder, execute:

```bash
python scene_report.py
```

The initial script loads eight records but creates an empty report and three zero counts. Those are the visible effects of the unfinished functions. Running without an exception is not enough to complete the task.

Each command starts a fresh Python process. Unlike a notebook kernel, this process has no values remembered from previous cell runs. Save edits before executing again: Python reads the saved file from disk.

`main()` connects the functions. The final supplied `if __name__ == "__main__":` block calls it when the file is executed. You do not need to write that pattern from memory today. The `Path` expressions locate files beside the script and create the output folder; leave that support code unchanged.

## C2. Build the row report | about 15 minutes

Complete the marked body of `review_scenes(records, max_cloud)`:

1. Visit every input scene using a `for` loop.
2. Call `assess_scene(scene, max_cloud)` and store the returned status.
3. Append a new dictionary with exactly `scene_id` and `status` to `results`.
4. Return the complete list after the loop, using the existing return line.

For example, a single result dictionary has this form:

```python
{"scene_id": scene["scene_id"], "status": status}
```

Keep all input records in order, including repeated labels and invalid scenes. An empty input must return an empty list. Use the supplied classifier instead of copying its decision chain into the report function. The function returns data; `main` handles printing and saving.

Save and run again:

```bash
python scene_report.py
```

The report should now contain eight rows matching the status sequence in notebook A2. Both A records must appear. Open `results/scene_review.csv` in a text editor and check the header and two chosen rows. The summary counts still need C3.

The supplied pandas code writes the result dictionaries as a CSV. `index=False` avoids adding the DataFrame's row labels as an extra output column. Each run replaces this generated report; the input CSV is unchanged.

If you get stuck, describe one row's journey through the loop before adding more code. Ask for a hint about the next operation rather than replacing the whole program.

## C3. Count the decisions | about 5 minutes

Complete the marked loop in `summarize_results(results)`. Read each stored `status` and increment its entry in the existing counts dictionary. Do not classify again. Keep the initialization before the loop and return after it.

You have used this pattern before: if `status` contains a key, `counts[status] = counts[status] + 1` updates that key's value.

Save and run:

```bash
python scene_report.py
```

Expected counts at a cloud limit of 20:

| ELIGIBLE | CLOUDY | INVALID |
|---:|---:|---:|
| 5 | 1 | 2 |

Inspect individual rows as well as totals. The total alone cannot establish that the categories are correct. You do not need assertions or an automated test file for this exercise.

## Compare and explain | about 5 minutes

Run the unchanged script again. Check that the report still has eight rows and counts have not accumulated. In `lab06_notes.md`, explain one of these:

- Why `return results` belongs after the loop.
- Why a function can execute without an exception and still produce the wrong report.
- Why both records labeled A belong in the result.

If you finish early, predict the counts at `MAX_CLOUD = 10`. Edit that one setting, save, run, and compare with your prediction. Restore 20 afterward. This extension is optional.

Stop at the announced time for the separate individual quiz. The quiz is not included in this public student package.

## Finish

Save the notebook, script, and notes. Use a fresh notebook kernel to check the completed A1 and A2 work when time allows. Follow the existing Git start/finish checklist and commit the class work separately from the homework. Generated reports are excluded by `.gitignore`.

If setup prevents finishing, record the agreed stopping point with your instructor. Do not automatically add unfinished class tasks to the homework below.

## At home: select scenes by two limits | about 30–40 minutes

Open `home_selection.py`. The classifier, CSV import, saving, and display are supplied. Your required coding task is one function: `choose_scenes(records, max_cloud, max_size_mb)`.

Write a loop that:

1. Visits every scene in input order.
2. Calls `assess_scene` for that scene.
3. Selects it only if it is ELIGIBLE and its size is no greater than `max_size_mb`.
4. Appends a new dictionary with exactly `scene_id` and `size_mb` for each selected record.
5. Returns the completed list after the loop.

Apply the size limit independently to each scene. Do not subtract selected sizes from it. Preserve repeated labels, leave the input unchanged, and return an empty list if nothing qualifies. Keep printing and file handling in the supplied `main` function.

Use the existing settings: `data/home_scenes.csv`, a cloud limit of 20, and an individual size limit of 250 MB. Before coding, inspect the CSV and predict the selected labels and sizes in `lab06_notes.md`.

Save and execute:

```bash
python home_selection.py
```

Open `results/home_selection.csv` and compare its saved rows with your prediction. Check one row exactly at a limit and one excluded row. The repeated H1 label can refer to two different records: retain both if both qualify.

For one additional check, predict what happens at an individual size limit of 100 MB, change that setting, save, and run again. Record the result, then restore 250 and rerun. No new dataset, reversed input, shared capacity planner, assertions, or separate verification program is required.

Write only these three short answers:

1. What selected labels and sizes did you predict at 250 MB, and did the saved report agree?
2. What changed at 100 MB? Give one included or excluded record as evidence.
3. If you used an LLM, what suggestion did you accept or change, and which exact example checked it? If you did not use one, say so and describe one check you made yourself.

At home assistance is allowed. Make your initial prediction and coding attempt first, then ask for a hint or help with one part if needed. You remain responsible for explaining your loop and the two limits.

Submit the completed `home_selection.py` and `lab06_notes.md` through the existing repository workflow. Keep generated CSVs in the ignored results folder. This homework is separate from any agreed class catch-up work.
