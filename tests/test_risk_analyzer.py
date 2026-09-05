from risk_analyzer import add_risk_status
from constants import (
    FIELD_AMOUNT,
    FIELD_RISK_STATUS,
    RISK_STATUS_NORMAL,
    RISK_STATUS_RISKY,
    RISK_STATUS_VERY_RISKY,
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