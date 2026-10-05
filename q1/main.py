import json
def analyze_log(filepath: str) -> dict:
    total = 0
    by_level = {}
    by_user = {}
    last_error = None

    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    log = json.loads(line)
                except json.JSONDecodeError:
                    continue
                total += 1
    except FileNotFoundError:
        pass

    return {
        "total": total,
        "by_level": by_level,
        "by_user": by_user,
        "last_error": last_error
    }
if __name__ == "__main__":
    result = analyze_log("app.jsonl")
    print(json.dumps(result, indent=4, ensure_ascii=False))

