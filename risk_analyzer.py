from constants import (
    FIELD_AMOUNT,
    FIELD_DEPARTMENT,
    FIELD_RISK_STATUS,
    FIELD_AI_COMMENT,
    FIELD_RECOMMENDED_ACTION,
    RISK_STATUS_VERY_RISKY,
    RISK_STATUS_RISKY,
    RISK_STATUS_NORMAL,
    SUMMARY_TOTAL_COUNT,
    SUMMARY_NORMAL_COUNT,
    SUMMARY_RISKY_COUNT,
    SUMMARY_VERY_RISKY_COUNT
)


def add_risk_status(purchase_request, very_risky_limit, risky_limit):
    if purchase_request[FIELD_AMOUNT] > very_risky_limit:
        risk_status = RISK_STATUS_VERY_RISKY
        ai_comment = "Bu talep çok yüksek tutarlı olduğu için üst yönetim onayı önerilir."
        recommended_action = "Üst yönetim onayına gönder."
    elif purchase_request[FIELD_AMOUNT] > risky_limit:
        risk_status = RISK_STATUS_RISKY
        ai_comment = "Bu talep yüksek tutarlı olduğu için yönetici onayı önerilir."
        recommended_action = "Yönetici onayına gönder."
    else:
        risk_status = RISK_STATUS_NORMAL
        ai_comment = "Bu talep belirlenen risk limitleri içinde gözüküyor."
        recommended_action = "Standart onay sürecine devam et."

    purchase_request[FIELD_RISK_STATUS] = risk_status
    purchase_request[FIELD_AI_COMMENT] = ai_comment
    purchase_request[FIELD_RECOMMENDED_ACTION] = recommended_action

    return purchase_request


def add_risk_status_to_all(purchase_requests, very_risky_limit, risky_limit):
    updated_requests = []

    for request in purchase_requests:
        updated_request = add_risk_status(request, very_risky_limit, risky_limit)
        updated_requests.append(updated_request)

    return updated_requests


def calculate_risk_summary(updated_requests):
    normal_count = 0
    risky_count = 0
    very_risky_count = 0

    for request in updated_requests:
        if request[FIELD_RISK_STATUS] == RISK_STATUS_VERY_RISKY:
            very_risky_count += 1
        elif request[FIELD_RISK_STATUS] == RISK_STATUS_RISKY:
            risky_count += 1
        else:
            normal_count += 1

    summary = {
        SUMMARY_TOTAL_COUNT: len(updated_requests),
        SUMMARY_NORMAL_COUNT: normal_count,
        SUMMARY_RISKY_COUNT: risky_count,
        SUMMARY_VERY_RISKY_COUNT: very_risky_count
    }

    return summary


def calculate_department_summary(updated_requests):
    department_summary = {}

    for request in updated_requests:
        department = request[FIELD_DEPARTMENT]

        if department in department_summary:
            department_summary[department] += 1
        else:
            department_summary[department] = 1
    
    return department_summary


def calculate_amount_summary_by_field(updated_requests, field_name):
    amount_summary = {}

    for request in updated_requests:
        field_value = request[field_name]
        amount = request[FIELD_AMOUNT]

        if field_value in amount_summary:
            amount_summary[field_value] += amount
        else:
            amount_summary[field_value] = amount
    
    return amount_summary