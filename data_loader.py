import json
def load_purchase_requests(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            purchase_requests = json.load(file)

        return purchase_requests

    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
        return[]

    except json.JSONDecodeError:
        print(f"Hata: {file_path} dosyası geçerli bir JSON formatında değil.")
        return[]