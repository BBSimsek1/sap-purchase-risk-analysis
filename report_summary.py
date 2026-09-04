from risk_analyzer import (
    calculate_risk_summary,
    calculate_department_summary,
    calculate_amount_summary_by_field,
)

from constants import (
    FIELD_DEPARTMENT,
    FIELD_SUPPLIER,
    FIELD_RISK_STATUS,
)


def calculate_report_summaries(updated_requests):
    summary = calculate_risk_summary(updated_requests)
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

    return (
        summary,
        department_summary,
        department_amount_summary,
        supplier_amount_summary,
        risk_amount_summary
    )