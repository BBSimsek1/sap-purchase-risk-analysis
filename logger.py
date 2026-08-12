from datetime import datetime

def write_log(file_path, level, message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"[{current_time}] [{level}] {message}\n")