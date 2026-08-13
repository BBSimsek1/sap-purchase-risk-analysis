from data_loader import load_purchase_requests
from validator import validate_purchase_requests
from risk_analyzer import add_risk_status_to_all, calculate_risk_summary, calculate_department_summary, calculate_amount_summary_by_field
from data_writer import save_updated_requests
from reporter import show_purchase_report
from logger import write_log
from config_loader import load_config
from constants import (
    INPUT_FILE_PATH,
    OUTPUT_FILE_PATH,
    LOG_FILE_PATH,
    CONFIG_FILE_PATH,
    FIELD_DEPARTMENT,
    FIELD_SUPPLIER,
    FIELD_RISK_STATUS,
    LOG_LEVEL_INFO,
    LOG_LEVEL_WARNING,
    LOG_LEVEL_ERROR,
    SUMMARY_TOTAL_COUNT,
    SUMMARY_NORMAL_COUNT,
    SUMMARY_RISKY_COUNT,
    SUMMARY_VERY_RISKY_COUNT
)
   

def generate_purchase_risk_report(purchase_requests, very_risky_limit, risky_limit):
    updated_requests = add_risk_status_to_all(
        purchase_requests,
        very_risky_limit,
        risky_limit
    )

    summary = calculate_risk_summary(updated_requests)

    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, "Satın alma risk raporu oluşturuldu.")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Toplam talep sayısı: {summary[SUMMARY_TOTAL_COUNT]}")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Normal talep sayısı: {summary[SUMMARY_NORMAL_COUNT]}")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Riskli talep sayısı: {summary[SUMMARY_RISKY_COUNT]}")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Çok riskli talep sayısı: {summary[SUMMARY_VERY_RISKY_COUNT]}")

    department_summary = calculate_department_summary(updated_requests)

    department_amount_summary = calculate_amount_summary_by_field(
        updated_requests, 
        FIELD_DEPARTMENT
    )

    supplier_amount_summary = calculate_amount_summary_by_field(
        updated_requests, 
        FIELD_SUPPLIER
    )

    risk_amount_summary = calculate_amount_summary_by_field(
        updated_requests, 
        FIELD_RISK_STATUS
    )

    show_purchase_report(
        updated_requests, 
        summary, 
        department_summary, 
        department_amount_summary, 
        supplier_amount_summary, 
        risk_amount_summary
    )

    save_updated_requests(OUTPUT_FILE_PATH, updated_requests)


def main():
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, "Program başlatıldı.")

    config = load_config(CONFIG_FILE_PATH)

    if len(config) == 0:
        print("Rapor oluşturulamadı: config dosyası okunamadı.")
        write_log(LOG_FILE_PATH, LOG_LEVEL_WARNING, "Rapor oluşturulamadı: config dosyası okunamadı.")
        return    
    
    very_risky_limit = config["very_risky_limit"]
    risky_limit = config["risky_limit"]

    purchase_requests = load_purchase_requests(INPUT_FILE_PATH)
    
    is_valid, validation_errors = validate_purchase_requests(purchase_requests)

    if not is_valid:
        print("Veri doğrulama hataları:")
        print("------------------------")

        for error in validation_errors:
            print(error)
            write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, error)
        
        print("Rapor oluşturulamadı: veri formatı eksik veya hatalı.")
        write_log(LOG_FILE_PATH, LOG_LEVEL_ERROR, "Rapor oluşturulamadı: veri formatı eksik veya hatalı.")

        return

    generate_purchase_risk_report(
        purchase_requests, 
        very_risky_limit, 
        risky_limit
    )

if __name__ == "__main__":
    main()