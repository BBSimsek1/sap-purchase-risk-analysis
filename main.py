from risk_analyzer import add_risk_status_to_all, calculate_risk_summary, calculate_department_summary, calculate_amount_summary_by_field
from data_writer import save_report_data
from reporter import show_purchase_report
from logger import write_log
from datetime import datetime
from report_builder import build_report_data
from app_loader import (
    load_and_validate_config,
    load_and_validate_purchase_requests
)
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
    SUMMARY_VERY_RISKY_COUNT,
    REPORT_TYPE_PURCHASE_RISK_ANALYSIS,
    REPORT_VERSION
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

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    show_purchase_report(
        updated_requests, 
        summary, 
        department_summary, 
        department_amount_summary, 
        supplier_amount_summary, 
        risk_amount_summary,
        risky_limit,
        very_risky_limit,
        generated_at,
    )

    report_data = build_report_data(
        generated_at,
        risky_limit,
        very_risky_limit,
        summary,
        department_summary,
        department_amount_summary,
        supplier_amount_summary,
        risk_amount_summary,
        updated_requests
    )

    save_report_data(OUTPUT_FILE_PATH, report_data)


def main():
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, "Program başlatıldı.")

    config = load_and_validate_config()

    if config is None:
        return

    very_risky_limit = config["very_risky_limit"]
    risky_limit = config["risky_limit"]

    purchase_requests = load_and_validate_purchase_requests()

    if purchase_requests is None:
        return

    generate_purchase_risk_report(
        purchase_requests,
        very_risky_limit,
        risky_limit
    )

if __name__ == "__main__":
    main()