import json

def save_updated_requests(file_path, updated_requests):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(updated_requests, file, ensure_ascii=False, indent=4)

    print()
    print(f"Güncellenmiş talepler {file_path} dosyasına kaydedildi.")