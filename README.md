# Akıllı Ders Çalışma Verimlilik Sistemi

Bu proje, bulanık mantık yöntemi kullanılarak öğrencinin ders çalışma verimliliğini analiz eden Python tabanlı bir karar destek sistemidir.

## Proje Amacı

Sistem; çalışma süresi, telefon kullanımı, uyku kalitesi ve mola düzeni gibi değişkenleri değerlendirerek öğrencinin verimlilik skorunu hesaplar.

## Kullanılan Teknolojiler

- Python
- Streamlit
- NumPy
- SciPy
- Scikit-Fuzzy
- Matplotlib

## Giriş Değişkenleri

| Değişken | Aralık | Dilsel Değerler |
|---|---:|---|
| Çalışma Süresi | 0 - 8 saat | Düşük, Orta, Yüksek |
| Telefon Kullanımı | 0 - 6 saat | Az, Orta, Fazla |
| Uyku Kalitesi | 0 - 10 | Kötü, Orta, İyi |
| Mola Düzeni | 0 - 10 | Yetersiz, Dengeli, Aşırı |

## Çıkış Değişkeni

| Değişken | Aralık | Dilsel Değerler |
|---|---:|---|
| Verimlilik Skoru | 0 - 100 | Düşük, Orta, Yüksek, Çok Yüksek |

## Bulanık Mantık Yöntemi

Projede Mamdani tipi bulanık çıkarım sistemi kullanılmıştır. Giriş değerleri üyelik fonksiyonları ile bulanıklaştırılmış, kural tabanı üzerinden çıkarım yapılmış ve sonuç centroid yöntemiyle durulaştırılmıştır.

## Proje Dosyaları

```text
study_efficiency_fuzzy/
│
├── app.py
├── fuzzy_system.py
├── plots.py
├── test_scenarios.py
├── README.md
├── rapor.md
└── requirements.txt