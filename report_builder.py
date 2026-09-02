from constants import (
    REPORT_TYPE_PURCHASE_RISK_ANALYSIS,
    REPORT_VERSION,
    INPUT_FILE_PATH,
)


def build_report_data(
    generated_at,
    risky_limit,
    very_risky_limit,
    summary,
    department_summary,
    department_amount_summary,
    supplier_amount_summary,
    risk_amount_summary,
    updated_requests
):
    report_data = {
        "report_type": REPORT_TYPE_PURCHASE_RISK_ANALYSIS,
        "report_version": REPORT_VERSION,
        "generated_at": generated_at,
        "source_file": INPUT_FILE_PATH,
        "risk_limits": {
            "risky_limit": risky_limit,
            "very_risky_limit": very_risky_limit
        },
        "summary": summary,
        "department_summary": department_summary,
        "department_amount_summary": department_amount_summary,
        "supplier_amount_summary": supplier_amount_summary,
        "risk_amount_summary": risk_amount_summary,
        "requests": updated_requests
    }

    return report_data