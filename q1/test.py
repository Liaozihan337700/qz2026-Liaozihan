import json
from main import analyze_log
def test_analyze_log():
    test_data = """
{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}
{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "数据库连接失败", "user": "李四"}
{"timestamp": "2026-10-01 10:25:12", "level": "INFO", "message": "用户登出", "user": "张三"}
{"timestamp": "2026-10-01 10:26:30", "level": "ERROR", "message": "超时", "user": "李四"}
{"timestamp": "2026-10-01 10:27:00", "level": "INFO", "message": "任务完成", "user": "王五"}
"""
    with open("test_tmp.jsonl", "w", encoding="utf-8") as f:
        f.write(test_data.strip())
    res = analyze_log("test_tmp.jsonl")
    print(json.dumps(res, indent=4, ensure_ascii=False))
    assert res["total"] == 5
    assert res["by_level"]["INFO"] == 3
    assert res["by_level"]["ERROR"] == 2
    assert res["by_user"]["张三"] == 2
    assert res["by_user"]["李四"] == 2
    assert res["by_user"]["王五"] == 1
    assert res["last_error"] == "超时"
    print("test past")
if __name__ == "__main__":
    test_analyze_log()


