from config_validator import validate_config


def test_valid_config():
    config = {
        "very_risky_limit": 10000,
        "risky_limit": 5000
    }

    is_valid, errors = validate_config(config)

    assert is_valid is True
    assert errors == []