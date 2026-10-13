# student_utils.py
def parse_student(line):
    line = line.strip()
    if not line:
        raise ValueError("空行")
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误，分割得到{len(parts)}个字段")
    name_str, score_str = parts
    name_str = name_str.strip()
    score_str = score_str.strip()
    if len(name_str) == 0:
        raise ValueError("姓名为空")
    score = int(score_str)
    if not (0 <= score <= 100):
        raise ValueError(f"成绩{score}不在0‑100范围")
    return {"name": name_str, "score": score}
