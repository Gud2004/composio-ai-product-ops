import os
import json
import time
import glob
import pandas as pd

from agents.research_agent import research_app


# -------------------------------
# Read CSV
# -------------------------------
apps = pd.read_csv("data/apps.csv")

# Create output folder
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

failed = []

TOTAL = len(apps)

print("=" * 60)
print(f"Starting Research Pipeline ({TOTAL} Apps)")
print("=" * 60)

for index, row in apps.iterrows():

    app = str(row["app"]).strip()

    if app == "" or app.lower() == "nan":
        continue

    filename = (
        app.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    ) + ".json"

    filepath = os.path.join(OUTPUT_DIR, filename)

    # Skip already researched
    if os.path.exists(filepath):
        print(f"[{index+1}/{TOTAL}] ⏭ Skipping {app} (already researched)")
        continue

    print(f"\n[{index+1}/{TOTAL}] 🔍 Researching {app}...")

    try:

        result = research_app(app)

        print("Saving to:", os.path.abspath(filepath))

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        if os.path.exists(filepath):
            print(f"✅ Saved {filename}")
        else:
            print(f"❌ Failed to save {filename}")

    except Exception as e:

        print(f"❌ Failed: {app}")
        print("Reason:", e)

        failed.append({
            "app": app,
            "error": str(e)
        })

    time.sleep(5)


# ----------------------------------------
# Build all_results.json
# ----------------------------------------

combined_results = []

json_files = glob.glob(os.path.join(OUTPUT_DIR, "*.json"))

for file in json_files:

    name = os.path.basename(file)

    if name in ["all_results.json", "failed_apps.json"]:
        continue

    try:
        with open(file, "r", encoding="utf-8") as f:
            combined_results.append(json.load(f))
    except Exception as e:
        print(f"Could not read {name}: {e}")

with open(
    os.path.join(OUTPUT_DIR, "all_results.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(combined_results, f, indent=4, ensure_ascii=False)

with open(
    os.path.join(OUTPUT_DIR, "failed_apps.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(failed, f, indent=4, ensure_ascii=False)


print("\n" + "=" * 60)
print("Research Complete")
print("=" * 60)
print(f"Successful : {len(combined_results)}")
print(f"Failed     : {len(failed)}")

print("\nOutput Folder:")
print(os.path.abspath(OUTPUT_DIR))