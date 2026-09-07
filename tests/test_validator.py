from validator import validate_purchase_requests
from constants import (
    FIELD_ID,
    FIELD_AMOUNT,
    FIELD_DEPARTMENT,
    FIELD_SUPPLIER,
)


def test_valid_purchase_request():
    purchase_requests = [
        {
            FIELD_ID: "PR001",
            FIELD_AMOUNT: 9000,
            FIELD_DEPARTMENT: "IT",
            FIELD_SUPPLIER: "ABC Teknoloji"
        }
    ]

    is_valid, errors = validate_purchase_requests(purchase_requests)

    assert is_valid is True
    assert errors == []