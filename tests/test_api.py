from fastapi.testclient import TestClient

from api import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "SAP Purchase Risk Analysis API is running."
    }


def test_analyze_purchase_requests_endpoint():
    request_body = [
        {
            "id": "PR001",
            "amount": 9000,
            "department": "IT",
            "supplier": "ABC Teknoloji"
        }
    ]

    response = client.post(
        "/analyze-purchase-requests",
        json=request_body
    )

    response_data = response.json()

    assert response.status_code == 200
    assert response_data["summary"]["total_count"] == 1
    assert response_data["summary"]["risky_count"] == 1
    assert response_data["requests"][0]["risk_status"] == "Riskli Talep"


def test_analyze_purchase_requests_endpoint_with_invalid_amount():
    request_body = [
        {
            "id": "PR001",
            "amount": "9000",
            "department": "IT",
            "supplier": "ABC Teknoloji"
        }
    ]

    response = client.post(
        "/analyze-purchase-requests",
        json=request_body
    )

    response_data = response.json()

    assert response.status_code == 200
    assert "errors" in response_data
    assert "Hata: PR001 kaydında amount alanı sayı olmalıdır." in response_data["errors"]