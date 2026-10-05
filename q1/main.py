import json
def analyze_log(filepath: str) -> dict:
    total = 0
    by_level = {}
    by_user = {}
    last_error = None

    return {
        "total": total,
        "by_level": by_level,
        "by_user": by_user,
        "last_error": last_error
    }
if __name__ == "__main__":
    result = analyze_log("app.jsonl")
    print(json.dumps(result, indent=4, ensure_ascii=False))

