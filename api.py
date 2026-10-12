from fastapi import FastAPI

from datetime import datetime
from report_builder import build_report_data
from report_summary import calculate_report_summaries
from config_validator import validate_config
from validator import validate_purchase_requests
from config_loader import load_config
from risk_analyzer import (
    add_risk_status_to_all,
    calculate_risk_summary
)
from constants import (
    CONFIG_FILE_PATH,
    FIELD_DEPARTMENT,
    FIELD_SUPPLIER,
    FIELD_RISK_STATUS
)

app = FastAPI()

def load_and_validate_api_config():
    config = load_config(CONFIG_FILE_PATH)

    is_config_valid, config_errors = validate_config(config)

    if not is_config_valid:
        return None, config_errors

    return config, []


def validate_api_purchase_requests(purchase_requests):
    is_valid, validation_errors = validate_purchase_requests(purchase_requests)


    if not is_valid:
        return validation_errors

    return []


@app.get("/")
def home():
    return {
    "message": "SAP Purchase Risk Analysis API is running."
    }

@app.post("/analyze-purchase-requests")
def analyze_purchase_requests(purchase_requests: list[dict]):
    config, config_errors = load_and_validate_api_config()

    if config is None:
        return {
            "errors": config_errors
        }

    very_risky_limit = config["very_risky_limit"]
    risky_limit = config["risky_limit"]

    validation_errors = validate_api_purchase_requests(purchase_requests)

    if len(validation_errors) > 0:
        return {
            "errors": validation_errors
        }

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

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    return report_data