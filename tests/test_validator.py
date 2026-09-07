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


def test_purchase_request_missing_supplier():
    purchase_requests = [
        {
            FIELD_ID: "PR001",
            FIELD_AMOUNT: 9000,
            FIELD_DEPARTMENT: "IT"
        }
    ]

    is_valid, errors = validate_purchase_requests(purchase_requests)

    assert is_valid is False
    assert "Hata: PR001 kaydında supplier alanı eksik." in errors


def test_purchase_request_amount_must_be_number():
    purchase_requests = [
        {
            FIELD_ID: "PR001",
            FIELD_AMOUNT: "9000",
            FIELD_DEPARTMENT: "IT",
            FIELD_SUPPLIER: "ABC Teknoloji"
        }
    ]

    is_valid, errors = validate_purchase_requests(purchase_requests)

    assert is_valid is False
    assert "Hata: PR001 kaydında amount alanı sayı olmalıdır." in errors