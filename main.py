from risk_analyzer import add_risk_status_to_all
from data_writer import save_report_data
from reporter import show_purchase_report
from logger import write_log
from datetime import datetime
from report_logger import log_report_summary
from report_summary import calculate_report_summaries
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
    FIELD_RISK_STATUS,
    LOG_LEVEL_INFO,
    LOG_LEVEL_WARNING,
    LOG_LEVEL_ERROR,
    REPORT_TYPE_PURCHASE_RISK_ANALYSIS,
    REPORT_VERSION
)


def generate_purchase_risk_report(purchase_requests, very_risky_limit, risky_limit):
    updated_requests = add_risk_status_to_all(
        purchase_requests,
        very_risky_limit,
        risky_limit
    )

    (
        summary,
        department_summary,
        department_amount_summary,
        supplier_amount_summary,
        risk_amount_summary
    ) = calculate_report_summaries(updated_requests)

    log_report_summary(summary)
    
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