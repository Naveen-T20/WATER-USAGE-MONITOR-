# water_usage_monitor.py

import random
import time
import json
from datetime import datetime

def simulate_water_flow():
    """Simulate water flow data in liters per minute."""
    return round(random.uniform(0.5, 10.0), 2)

def log_usage(log_file="water_usage_log.json"):
    data = []
    try:
        with open(log_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    for _ in range(10):  # simulate 10 readings
        flow = simulate_water_flow()
        timestamp = datetime.now().isoformat()
        usage_entry = {"timestamp": timestamp, "flow_rate_lpm": flow}
        data.append(usage_entry)
        print(f"{timestamp} - Flow Rate: {flow} L/min")
        time.sleep(1)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)

def analyze_usage(log_file="water_usage_log.json"):
    with open(log_file, "r") as f:
        data = json.load(f)

    total_usage = sum(entry["flow_rate_lpm"] for entry in data)
    avg_usage = total_usage / len(data) if data else 0
    print(f"\nTotal Usage: {total_usage:.2f} L")
    print(f"Average Flow Rate: {avg_usage:.2f} L/min")

if __name__ == "__main__":
    log_usage()
    analyze_usage()