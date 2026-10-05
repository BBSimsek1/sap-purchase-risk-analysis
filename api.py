from fastapi import FastAPI

from risk_analyzer import (
    add_risk_status_to_all,
    calculate_risk_summary
)

app = FastAPI()


@app.get("/")
def home():
    return {
    "message": "SAP Purchase Risk Analysis API is running."
    }

@app.post("/analyze-purchase-requests")
def analyze_purchase_requests(purchase_requests: list[dict]):
    very_risky_limit = 10000
    risky_limit = 5000

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