from config_validator import validate_config


def test_valid_config():
    config = {
        "very_risky_limit": 10000,
        "risky_limit": 5000
    }

    is_valid, errors = validate_config(config)

    assert is_valid is True
    assert errors == []


def test_config_missing_risky_limit():
    config = {
        "very_risky_limit": 10000
    }

    is_valid, errors = validate_config(config)

    assert is_valid is False
    assert "Hata: config dosyasında risky_limit alanı eksik." in errors