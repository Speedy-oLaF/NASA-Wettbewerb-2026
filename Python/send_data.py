import json
import os
from datetime import datetime

pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "send_data.json")

with open(pfad, "r", encoding="utf-8") as file:
    all_data = json.load(file)

def collect_data(obj):
    sum = []
    if isinstance(obj, list):
        for entry in obj:
            sum.extend(collect_data(entry))
    elif isinstance(obj, dict):
        own = {k: v for k, v in obj.items() if not isinstance(v, (dict, list))}
        if "timestamp" in own:
            sum.append(own)
        for v in obj.values():
            if isinstance(v, (dict, list)):
                sum.extend(collect_data(v))
    return sum

alle = collect_data(all_data)

latest_data = max(
    alle,
    key=lambda data: datetime.fromisoformat(data["timestamp"])
)

print(json.dumps(latest_data, ensure_ascii=False))