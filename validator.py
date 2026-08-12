from constants import (
    FIELD_ID,
    FIELD_AMOUNT,
    FIELD_DEPARTMENT,
    FIELD_SUPPLIER
)


def validate_purchase_requests(purchase_requests):
    required_fields = [FIELD_ID, FIELD_AMOUNT, FIELD_DEPARTMENT, FIELD_SUPPLIER]
    text_fields = [FIELD_ID, FIELD_DEPARTMENT, FIELD_SUPPLIER]
    errors = []

    for request in purchase_requests:
        request_id = request.get(FIELD_ID, "Bilinmeyen talep")

        for field in required_fields:
            if field not in request:
                errors.append(f"Hata: {request_id} kaydında {field} alanı eksik.")
        
        for field in text_fields:
            if field in request:
                if not isinstance(request[field], str):
                    errors.append(f"Hata: {request_id} kaydında {field} alanı metin olmalıdır.")
                
                elif request[field].strip() == "":
                    errors.append(f"Hata: {request_id} kaydından {field} alanı boş olamaz.")

                else:
                    request[field] = request[field].strip()
                
        if FIELD_AMOUNT in request:
            if not isinstance(request[FIELD_AMOUNT], (int, float)):
                errors.append(f"Hata: {request_id} kaydından {FIELD_AMOUNT} alanı sayı olmalıdır.")
            
            elif request[FIELD_AMOUNT] <= 0:
                errors.append(f"Hata: {request_id} kaydından {FIELD_AMOUNT} alanı 0'dan büyük olmalıdır.")

    if len(errors) > 0:
        return False, errors
    
    return True, []