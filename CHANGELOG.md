# Changelog

Bu dosya, projede yapılan önemli değişiklikleri takip etmek için kullanılır.

## [1.0.0] - 2026-08-13

### Added

- İlk çalışan satın alma risk analizi projesi oluşturuldu.
- JSON dosyasından satın alma talepleri okuma özelliği eklendi.
- Satın alma taleplerine risk durumu, AI yorumu ve önerilen aksiyon ekleme özelliği geliştirildi.
- Veri doğrulama kuralları eklendi.
- Hatalı veri durumlarında rapor oluşturmayı durdurma mantığı eklendi.
- Terminal raporlama özelliği eklendi.
- Güncellenmiş talepleri JSON dosyasına yazma özelliği eklendi.
- Loglama sistemi eklendi.
- README dokümantasyonu güncellendi.
- requirements.txt, .gitignore ve LICENSE dosyaları eklendi.
- Risk limitlerini `config.json` dosyasından okuma özelliği eklendi.
- Config dosyasını okumak için `config_loader.py` modülü eklendi.
- Config dosyasındaki değerleri doğrulamak için `config_validator.py` modülü eklendi.
- Config hatalı olduğunda programın rapor oluşturmadan kontrollü şekilde durması sağlandı.
- Terminal raporunda kullanılan risk limitlerinin gösterilmesi sağlandı.
- `purchase_risk_report.json` dosyasına tam rapor verisinin kaydedilmesi sağlandı.
- JSON çıktı yapısı; genel özet, departman özeti, tedarikçi tutar özeti, risk tutar özeti ve detay talepleri içerecek şekilde genişletildi.
- JSON rapor çıktısına `generated_at` alanı eklenerek raporun üretim zamanının kaydedilmesi sağlandı.
- Terminal raporunda `generated_at` bilgisinin gösterilmesi sağlandı.
- JSON rapor çıktısına analizde kullanılan risk limitlerini gösteren `risk_limits` alanı eklendi.
- JSON rapor çıktısına raporun hangi giriş dosyasından üretildiğini gösteren `source_file` alanı eklendi.
- JSON rapor çıktısına rapor türünü gösteren `report_type` alanı eklendi.
- JSON rapor çıktısına rapor format versiyonunu gösteren `report_version` alanı eklendi.
- `report_type` değeri `constants.py` içinde sabit olarak yönetilecek şekilde düzenlendi.
- `build_report_data()` fonksiyonu `report_builder.py` modülüne taşındı.
- JSON rapor verisi oluşturma sorumluluğu `main.py` dosyasından ayrıldı.
- Rapor yazma fonksiyonu `save_report_data()` olarak yeniden adlandırıldı.
- Config okuma ve doğrulama süreci `load_and_validate_config()` fonksiyonuna taşındı.
- Satın alma taleplerini okuma ve doğrulama süreci `load_and_validate_purchase_requests()` fonksiyonuna taşındı.
- `main()` fonksiyonu sadeleştirilerek uygulamanın ana iş akışını daha net gösterecek hale getirildi.