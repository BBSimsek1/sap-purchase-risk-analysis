from risk_analyzer import (
    add_risk_status,
    calculate_risk_summary
)
from constants import (
    FIELD_AMOUNT,
    FIELD_RISK_STATUS,
    RISK_STATUS_NORMAL,
    RISK_STATUS_RISKY,
    RISK_STATUS_VERY_RISKY,
    SUMMARY_TOTAL_COUNT,
    SUMMARY_NORMAL_COUNT,
    SUMMARY_RISKY_COUNT,
    SUMMARY_VERY_RISKY_COUNT
)


def test_normal_request():
    purchase_request = {
        FIELD_AMOUNT: 3000
    }

    updated_request = add_risk_status(
        purchase_request,
        very_risky_limit=10000,
        risky_limit=5000
    )

    assert updated_request[FIELD_RISK_STATUS] == RISK_STATUS_NORMAL


def test_risky_request():
    purchase_request = {
        FIELD_AMOUNT: 9000
    }

    updated_request = add_risk_status(
        purchase_request,
        very_risky_limit=10000,
        risky_limit=5000
    )

    assert updated_request[FIELD_RISK_STATUS] == RISK_STATUS_RISKY


def test_very_risky_request():
    purchase_request = {
        FIELD_AMOUNT: 15000
    }

    updated_request = add_risk_status(
        purchase_request,
        very_risky_limit=10000,
        risky_limit=5000
    )

    assert updated_request[FIELD_RISK_STATUS] == RISK_STATUS_VERY_RISKY


def test_calculate_risk_summary():
    updated_requests = [
        {
            FIELD_RISK_STATUS: RISK_STATUS_NORMAL
        },
        {
            FIELD_RISK_STATUS: RISK_STATUS_RISKY
        },
        {
            FIELD_RISK_STATUS: RISK_STATUS_VERY_RISKY
        },
    ]

    summary = calculate_risk_summary(updated_requests)

    assert summary[SUMMARY_TOTAL_COUNT] == 3
    assert summary[SUMMARY_NORMAL_COUNT] == 1
    assert summary[SUMMARY_RISKY_COUNT] == 1
    assert summary[SUMMARY_VERY_RISKY_COUNT] == 1