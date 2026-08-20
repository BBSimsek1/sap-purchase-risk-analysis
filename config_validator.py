def validate_config(config):
    errors = []

    required_fields = ["very_risky_limit", "risky_limit"]

    for field in required_fields:
        if field not in config:
            errors.append(f"Hata: config dosyasında {field} alanı eksik.")
        
    if "very_risky_limit" in config:
        if not isinstance(config["very_risky_limit"], (int, float)):
            errors.append("Hata: very_risky_limit sayı olmalıdır.")
        elif config["very_risky_limit"] <= 0:
            errors.append("Hata: very_risky_limit 0'dan büyük olmalıdır.")
    
    if "risky_limit" in config:
        if not isinstance(config["risky_limit"], (int, float)):
            errors.append("Hata: risky_limit sayı olmalıdır.")
        elif config["risky_limit"] <= 0:
            errors.append("Hata: risky_limit 0'dan büyük olmalıdır.")

    if(
        "very_risky_limit" in config
        and "risky_limit" in config
        and isinstance(config["very_risky_limit"], (int, float))
        and isinstance(config["risky_limit"], (int, float))
    ):
        if config["very_risky_limit"] <= config["risky_limit"]:
            errors.append("Hata: very_risky_limit, risky_limit değerinden büyük olmalıdır.")

    if len(errors) > 0:
        return False, errors

    return True, []