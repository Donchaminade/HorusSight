from engine.core.engine import run_scan
import json

if __name__ == "__main__":
    target = input("Enter target URL: ")
    result = run_scan(target)

    print(json.dumps(result, indent=2))
