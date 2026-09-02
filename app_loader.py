from config_loader import load_config
from config_validator import validate_config
from data_loader import load_purchase_requests
from validator import validate_purchase_requests
from logger import write_log
from constants import (
    CONFIG_FILE_PATH,
    INPUT_FILE_PATH,
    LOG_FILE_PATH,
    LOG_LEVEL_ERROR,
    LOG_LEVEL_WARNING,
)


def load_and_validate_config():
    config = load_config(CONFIG_FILE_PATH)

    if len(config) == 0:
        print("Rapor oluşturulamadı: config dosyası okunamadı.")
        write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, "Rapor oluşturulamadı: config dosyası okunamadı.")
        return None

    is_config_valid, config_errors = validate_config(config)

    if not is_config_valid:
        print("Config doğrulama hataları:")
        print("--------------------------")

        for error in config_errors:
            print(error)
            write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, error)

        print("Rapor oluşturulamadı: config dosyası hatalı.")
        write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, "Rapor oluşturulamadı: config dosyası hatalı.")
        return None

    return config


def load_and_validate_purchase_requests():
    purchase_requests = load_purchase_requests(INPUT_FILE_PATH)

    if len(purchase_requests) == 0:
        print("Rapor oluşturulamadı: satın alma talebi bulunamadı.")
        write_log(LOG_FILE_PATH, LOG_LEVEL_WARNING, "Rapor oluşturulamadı: satın alma talebi bulunamadı.")
        return None

    is_valid, validation_errors = validate_purchase_requests(purchase_requests)

    if not is_valid:
        print("Veri doğrulama hataları:")
        print("------------------------")

        for error in validation_errors:
            print(error)
            write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, error)

        print("Rapor oluşturulamadı: veri formatı eksik veya hatalı.")
        write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, "Rapor oluşturulamadı: veri formatı eksik veya hatalı.")
        return None

    return purchase_requests