"""Lab 06 class starter: complete the two marked function bodies.

File input, CSV output, and a correct classifier are supplied. Initially the
report is empty and all counts are zero because the coding tasks are unfinished.
"""

from pathlib import Path
import pandas as pd

MAX_CLOUD = 20
BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "scenes.csv"
OUTPUT_PATH = BASE_DIR / "results" / "scene_review.csv"

def assess_scene(scene, max_cloud):
    """Return INVALID, CLOUDY, or ELIGIBLE in priority order."""
    if scene["cloud_percent"] < 0 or scene["cloud_percent"] > 100 or scene["size_mb"] <= 0:
        return "INVALID"
    elif scene["cloud_percent"] > max_cloud:
        return "CLOUDY"
    else:
        return "ELIGIBLE"


def review_scenes(records, max_cloud):
    """Return a new scene_id/status dictionary for every input record."""
    results = []
    # TASK C2: write a loop that assesses each scene and appends its result.
    return results


def summarize_results(results):
    """Count the stored statuses, including three zero counts for empty input."""
    counts = {"ELIGIBLE": 0, "CLOUDY": 0, "INVALID": 0}
    # TASK C3: write a loop that counts the status in each result dictionary.
    return counts


def main():
    """Load records, call the functions, and save and display the report."""
    scenes = pd.read_csv(INPUT_PATH)
    records = scenes.to_dict(orient="records")
    results = review_scenes(records, MAX_CLOUD)
    counts = summarize_results(results)

    report = pd.DataFrame(results, columns=["scene_id", "status"])
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT_PATH, index=False)

    print("Input records:", len(records))
    print("Report rows:", len(results))
    print(report.to_string(index=False))
    print("Counts:", counts)
    print("Saved:", OUTPUT_PATH)


# Supplied entry point: executing this file calls main.
if __name__ == "__main__":
    main()
