# SAP Satın Alma Risk Analizi

Bu proje, satın alma taleplerini JSON dosyasından okur, talepleri tutarlarına göre risk seviyelerine ayırır ve sonuçları terminalde raporlar.

## Projenin Amacı

Satın alma taleplerini analiz ederek:

- Normal talepleri belirlemek
- Riskli talepleri belirlemek
- Çok riskli talepleri belirlemek
- Departman, tedarikçi ve risk durumuna göre toplam tutarları hesaplamak
- Güncellenmiş talepleri yeni bir JSON dosyasına kaydetmek
- Program çalışmasını log dosyasına kaydetmek
- Veri doğrulama hatalarını terminalde ve log dosyasında göstermek

## Dosya Yapısı

```text
week3/
├── main.py
├── constants.py
├── data_loader.py
├── data_writer.py
├── validator.py
├── risk_analyzer.py
├── reporter.py
├── logger.py
├── purchase_requests.json
├── updated_purchase_requests.json
├── app.log
└── README.md
```

## Dosyaların Görevleri

```text
main.py
→ Programın ana akışını yönetir.

constants.py
→ Ortak sabitleri, dosya yollarını, risk limitlerini, log seviyelerini ve summary key değerlerini tutar.

data_loader.py
→ purchase_requests.json dosyasından veri okur.

data_writer.py
→ Güncellenmiş talepleri updated_purchase_requests.json dosyasına yazar.

validator.py
→ Satın alma taleplerinin veri formatını kontrol eder ve hata listesini döndürür.

risk_analyzer.py
→ Risk durumu, AI yorumu, önerilen aksiyon ve özet hesaplamalarını yapar.

reporter.py
→ Raporu terminale yazdırır.

logger.py
→ Program çalışırken oluşan önemli olayları app.log dosyasına yazar.

purchase_requests.json
→ Ham satın alma taleplerinin bulunduğu giriş dosyası.

updated_purchase_requests.json
→ Risk bilgileri eklenmiş çıktı dosyası.

app.log
→ Program çalışma kayıtlarının tutulduğu log dosyası.
```

## Çalıştırma

Terminalde `week3` klasöründeyken şu komut çalıştırılır:

```bash
python3 main.py
```

## Risk Kuralları

```text
10000 üstü → Çok Riskli Talep
5000 üstü  → Riskli Talep
5000 ve altı → Normal Talep
```

## Loglama

Program çalışırken önemli olayları `app.log` dosyasına yazar.

Log formatı:

```text
[Tarih Saat] [Log Seviyesi] Mesaj
```

Örnek:

```text
[2026-08-06 14:19:36] [INFO] Program başlatıldı.
[2026-08-06 14:19:36] [INFO] Satın alma risk raporu oluşturuldu.
[2026-08-06 14:19:36] [WARNING] Rapor oluşturulamadı: satın alma talebi bulunamadı.
[2026-08-06 14:19:36] [ERROR] Rapor oluşturulamadı: veri formatı eksik veya hatalı.
```

Log seviyeleri:

```text
INFO
→ Normal bilgilendirme mesajları.

WARNING
→ Programın çalışmasını engelleyebilecek uyarı durumları.

ERROR
→ Raporun oluşturulmasını engelleyen hata durumları.
```

## Veri Doğrulama

Program, rapor oluşturmadan önce `purchase_requests.json` içindeki verileri kontrol eder.

Kontrol edilen alanlar:

```text
id
amount
department
supplier
```

Validasyon kuralları:

```text
id, department ve supplier metin olmalıdır.
id, department ve supplier boş olamaz.
amount sayı olmalıdır.
amount 0'dan büyük olmalıdır.
Zorunlu alanlar eksik olmamalıdır.
```

Veri hatalıysa program rapor oluşturmaz. Hataları terminale yazdırır ve `app.log` dosyasına kaydeder.

## Örnek Girdi

```json
[
    {
        "id": "PR001",
        "amount": 9000,
        "department": "IT",
        "supplier": "ABC Teknoloji"
    }
]
```

## Örnek Çıktı

Program talebe şu alanları ekler:

```json
{
    "risk_status": "Riskli Talep",
    "ai_comment": "Bu talep yüksek tutarlı olduğu için yönetici onayı önerilir.",
    "recommended_action": "Yönetici onayına gönder."
}
```

## Test Senaryoları

Bu projede aşağıdaki veri senaryoları test edilmiştir.

### 1. Boş Liste

```json
[]
```

Beklenen sonuç:

```text
Rapor oluşturulamadı: satın alma talebi bulunamadı.
```

### 2. Eksik Alan

```json
[
    {
        "id": "PR001",
        "amount": 9000,
        "department": "IT"
    }
]
```

Beklenen sonuç:

```text
Hata: PR001 kaydında supplier alanı eksik.
```

### 3. Amount Metin Gelirse

```json
[
    {
        "id": "PR001",
        "amount": "9000",
        "department": "IT",
        "supplier": "ABC Teknoloji"
    }
]
```

Beklenen sonuç:

```text
Hata: PR001 kaydında amount alanı sayı olmalıdır.
```

### 4. Amount 0 veya Negatif Gelirse

```json
[
    {
        "id": "PR001",
        "amount": 0,
        "department": "IT",
        "supplier": "ABC Teknoloji"
    }
]
```

Beklenen sonuç:

```text
Hata: PR001 kaydında amount alanı 0'dan büyük olmalıdır.
```

### 5. Department Boş Gelirse

```json
[
    {
        "id": "PR001",
        "amount": 9000,
        "department": "",
        "supplier": "ABC Teknoloji"
    }
]
```

Beklenen sonuç:

```text
Hata: PR001 kaydında department alanı boş olamaz.
```

### 6. Supplier Sadece Boşluklardan Oluşursa

```json
[
    {
        "id": "PR001",
        "amount": 9000,
        "department": "IT",
        "supplier": "   "
    }
]
```

Beklenen sonuç:

```text
Hata: PR001 kaydında supplier alanı boş olamaz.
```

Bu hatalar terminale yazdırılır ve `app.log` dosyasına `[ERROR]` seviyesiyle kaydedilir.

## Kurulum

Bu proje harici bir Python paketine ihtiyaç duymaz. Gerekli dosyalar repository içinde bulunmaktadır.

Yine de standart Python proje yapısını göstermek için `requirements.txt` dosyası eklenmiştir.

Bağımlılıkları kurmak için:

```bash
pip install -r requirements.txt
```

Bu projede `requirements.txt` içinde harici paket bulunmamaktadır.

## Örnek Terminal Çıktısı

Program çalıştırıldığında terminalde aşağıdakine benzer bir rapor üretilir:

```text
Satın Alma Risk Raporu
----------------------

Talep ID: PR001
Tutar: 9000
Departman: IT
Tedarikçi: ABC Teknoloji
Risk Durumu: Riskli Talep
AI Yorumu: Bu talep yüksek tutarlı olduğu için yönetici onayı önerilir.
Önerilen Aksiyon: Yönetici onayına gönder.

Talep ID: PR002
Tutar: 3000
Departman: Finance
Tedarikçi: XYZ AŞ
Risk Durumu: Normal Talep
AI Yorumu: Bu talep belirlenen risk limitleri içinde görünüyor.
Önerilen Aksiyon: Standart onay sürecine devam et.

Talep ID: PR003
Tutar: 15000
Departman: Operations
Tedarikçi: Mega Lojistik
Risk Durumu: Çok Riskli Talep
AI Yorumu: Bu talep çok yüksek tutarlı olduğu için üst yönetim onayı önerilir.
Önerilen Aksiyon: Üst yönetim onayına gönder.
```

Bu çıktı, satın alma taleplerinin risk seviyelerine göre analiz edildiğini ve her talep için önerilen aksiyon üretildiğini gösterir.

## Kullanılan Teknolojiler ve Kavramlar

Bu projede aşağıdaki teknolojiler ve Python kavramları kullanılmıştır:

- Python
- JSON dosya okuma ve yazma
- Fonksiyonlar
- Modüler dosya yapısı
- Veri doğrulama
- Hata yönetimi
- Loglama
- Git ve GitHub
- Markdown dokümantasyonu

## Proje Mimarisi

Proje modüler bir yapıda tasarlanmıştır. Her dosyanın tek bir temel sorumluluğu vardır.

```text
main.py
→ Programın ana akışını yönetir.

data_loader.py
→ JSON dosyasından satın alma taleplerini okur.

validator.py
→ Satın alma taleplerinin veri formatını kontrol eder.

risk_analyzer.py
→ Taleplere risk durumu, AI yorumu ve önerilen aksiyon ekler.
→ Özet hesaplamalarını yapar.

reporter.py
→ Analiz sonuçlarını terminalde raporlar.

data_writer.py
→ Güncellenmiş talepleri JSON dosyasına kaydeder.

logger.py
→ Program akışını ve hata durumlarını app.log dosyasına yazar.

constants.py
→ Ortak sabitleri, dosya yollarını, alan adlarını ve risk limitlerini tutar.

## Config Ayarları

Risk limitleri `config.json` dosyasından okunur.

Örnek `config.json`:

```json
{
    "very_risky_limit": 10000,
    "risky_limit": 5000
}