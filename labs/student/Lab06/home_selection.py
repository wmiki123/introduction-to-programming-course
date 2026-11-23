"""Lab 06 home starter: write choose_scenes; the file handling is complete."""

from pathlib import Path
import pandas as pd

MAX_CLOUD = 20
MAX_SIZE_MB = 250
BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "home_scenes.csv"
OUTPUT_PATH = BASE_DIR / "results" / "home_selection.csv"

def assess_scene(scene, max_cloud):
    """Return INVALID, CLOUDY, or ELIGIBLE in priority order."""
    if scene["cloud_percent"] < 0 or scene["cloud_percent"] > 100 or scene["size_mb"] <= 0:
        return "INVALID"
    elif scene["cloud_percent"] > max_cloud:
        return "CLOUDY"
    else:
        return "ELIGIBLE"


def choose_scenes(records, max_cloud, max_size_mb):
    """Select eligible scenes no larger than the individual scene size limit."""
    selected = []
    # HOME TASK: write the selection loop here.
    return selected


def main():
    scenes = pd.read_csv(INPUT_PATH)
    records = scenes.to_dict(orient="records")
    selected = choose_scenes(records, MAX_CLOUD, MAX_SIZE_MB)
    report = pd.DataFrame(selected, columns=["scene_id", "size_mb"])
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT_PATH, index=False)
    print("Input records:", len(records))
    print("Selected records:", len(selected))
    print(report.to_string(index=False))
    print("Saved:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
