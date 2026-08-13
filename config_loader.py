import json

def load_config(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        return config
    
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
        return {}

    except json.JSONDecodeError:
        print(f"Hata: {file_path} dosyası geçerli bir JSON formatında değil.")
        return{}