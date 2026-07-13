import json
from collections import Counter

# Load all research results
with open("output/all_results.json", "r", encoding="utf-8") as f:
    apps = json.load(f)

auth_counter = Counter()
selfserve_counter = Counter()
mcp_counter = Counter()
buildability_counter = Counter()
category_counter = Counter()
blocker_counter = Counter()

for app in apps:

    category_counter[app.get("category", "Unknown")] += 1

    auth_counter[app.get("authentication", "Unknown")] += 1

    selfserve_counter[app.get("self_serve", "Unknown")] += 1

    mcp_counter[app.get("mcp", "Unknown")] += 1

    buildability_counter[app.get("buildability", "Unknown")] += 1

    blocker = app.get("main_blocker", "Unknown")

    blocker_counter[blocker] += 1


print("="*70)
print("TOTAL APPS :", len(apps))
print("="*70)

print("\nCATEGORY DISTRIBUTION")
for k,v in category_counter.items():
    print(f"{k:<35} {v}")

print("\nAUTHENTICATION")
for k,v in auth_counter.most_common():
    print(f"{k:<45} {v}")

print("\nSELF SERVE")
for k,v in selfserve_counter.items():
    print(f"{k:<35} {v}")

print("\nMCP SUPPORT")
for k,v in mcp_counter.items():
    print(f"{k:<35} {v}")

print("\nBUILDABILITY")
for k,v in buildability_counter.items():
    print(f"{k:<35} {v}")

print("\nTOP 10 BLOCKERS")

for blocker,count in blocker_counter.most_common(10):
    print(f"{count:>3}  {blocker}")