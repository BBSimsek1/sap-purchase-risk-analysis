from constants import (
    FIELD_ID,
    FIELD_AMOUNT,
    FIELD_DEPARTMENT,
    FIELD_SUPPLIER,
    FIELD_RISK_STATUS,
    FIELD_AI_COMMENT,
    FIELD_RECOMMENDED_ACTION,
    SUMMARY_TOTAL_COUNT,
    SUMMARY_NORMAL_COUNT,
    SUMMARY_RISKY_COUNT,
    SUMMARY_VERY_RISKY_COUNT
)


def show_purchase_report(
    updated_requests, 
    summary, 
    department_summary, 
    department_amount_summary, 
    supplier_amount_summary, 
    risk_amount_summary
):

    for request in updated_requests:
        print(f"Talep no: {request[FIELD_ID]}")
        print(f"Tutar: {request[FIELD_AMOUNT]}")
        print(f"Departman: {request[FIELD_DEPARTMENT]}")
        print(f"Tedarikçi: {request[FIELD_SUPPLIER]}")
        print(f"Risk durumu: {request[FIELD_RISK_STATUS]}")
        print(f"AI yorumu: {request[FIELD_AI_COMMENT]}")
        print(f"Önerilen aksiyon: {request[FIELD_RECOMMENDED_ACTION]}")
        print()
        
    print("Rapor Özeti")
    print("-----------")
    print(f"Toplam talep sayısı: {summary[SUMMARY_TOTAL_COUNT]}")
    print(f"Normal talep sayısı: {summary[SUMMARY_NORMAL_COUNT]}")
    print(f"Riskli talep sayısı: {summary[SUMMARY_RISKY_COUNT]}")
    print(f"Çok riskli talep sayısı: {summary[SUMMARY_VERY_RISKY_COUNT]}")

    print()
    print("Departman Özeti")
    print("---------------")

    for department in department_summary:
        print(f"{department}: {department_summary[department]} talep")
    
    print()
    print("Departman Tutar Özeti")
    print("---------------------")

    for department in department_amount_summary:
        print(f"{department}: {department_amount_summary[department]}")

    print()
    print("Tedarikçi Tutar Özeti")
    print("---------------------")

    for supplier in supplier_amount_summary:
        print(f"{supplier}: {supplier_amount_summary[supplier]}")
    
    print()
    print("Risk Tutar Özeti")
    print("---------------------")

    for risk_status in risk_amount_summary:
        print(f"{risk_status}: {risk_amount_summary[risk_status]}")
 