import json


def save_report_data(file_path, report_data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report_data, file, ensure_ascii=False, indent=4)

    print()
    print(f"Rapor verisi {file_path} dosyasına kaydedildi.")