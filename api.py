from fastapi import FastAPI

from config_validator import validate_config
from validator import validate_purchase_requests
from config_loader import load_config
from risk_analyzer import (
    add_risk_status_to_all,
    calculate_risk_summary
)
from constants import CONFIG_FILE_PATH

app = FastAPI()


@app.get("/")
def home():
    return {
    "message": "SAP Purchase Risk Analysis API is running."
    }

@app.post("/analyze-purchase-requests")
def analyze_purchase_requests(purchase_requests: list[dict]):
    config = load_config(CONFIG_FILE_PATH)

    is_config_valid, config_errors = validate_config(config)

    if not is_config_valid:
        return{
            "errors": config_errors
        }

    very_risky_limit = config["very_risky_limit"]
    risky_limit = config["risky_limit"]

    is_valid, validation_errors = validate_purchase_requests(purchase_requests)

    if not is_valid:
        return {
            "errors": validation_errors
        }

    updated_requests = add_risk_status_to_all(
        purchase_requests,
        very_risky_limit,
        risky_limit
    )

    summary = calculate_risk_summary(updated_requests)

    return {
        "summary": summary,
        "requests": updated_requests
    }