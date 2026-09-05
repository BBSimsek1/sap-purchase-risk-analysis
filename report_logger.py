from logger import write_log
from constants import (
    LOG_FILE_PATH,
    LOG_LEVEL_INFO,
    SUMMARY_TOTAL_COUNT,
    SUMMARY_NORMAL_COUNT,
    SUMMARY_RISKY_COUNT,
    SUMMARY_VERY_RISKY_COUNT,
)


def log_report_summary(summary):
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, "Satın alma risk raporu oluşturuldu.")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Toplam talep sayısı: {summary[SUMMARY_TOTAL_COUNT]}")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Normal talep sayısı: {summary[SUMMARY_NORMAL_COUNT]}")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Riskli talep sayısı: {summary[SUMMARY_RISKY_COUNT]}")
    write_log(LOG_FILE_PATH, LOG_LEVEL_INFO, f"Çok riskli talep sayısı: {summary[SUMMARY_VERY_RISKY_COUNT]}")