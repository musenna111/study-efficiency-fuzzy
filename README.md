# Akıllı Ders Çalışma Verimlilik Sistemi

Bu proje, bulanık mantık (Fuzzy Logic) kullanılarak öğrencilerin ders çalışma verimliliğini analiz eden bir karar destek sistemidir. Sistem; çalışma süresi, telefon kullanımı, uyku kalitesi ve mola düzeni gibi parametreleri değerlendirerek 0-100 arasında bir verimlilik skoru üretmektedir.

## Proje Amacı

Günümüzde öğrencilerin çalışma performansı birçok farklı faktörden etkilenmektedir. Bu projede, kesin sınırlar yerine insan düşünce yapısına daha yakın sonuçlar üretebilmek için bulanık mantık yaklaşımı kullanılmıştır.

Sistem sayesinde kullanıcı:

- Verimlilik skorunu görebilir
- Verimlilik seviyesini öğrenebilir
- Üyelik fonksiyonlarını inceleyebilir
- Durulaştırma (defuzzification) sürecini analiz edebilir
- Aktif kuralları görüntüleyebilir

---

# Kullanılan Teknolojiler

- Python
- Streamlit
- NumPy
- Matplotlib
- Scikit-Fuzzy

---

# Girdi Parametreleri

Sistem 4 farklı girdi parametresi kullanmaktadır:

| Parametre | Açıklama |
|---|---|
| Çalışma Süresi | Günlük ders çalışma süresi |
| Telefon Kullanımı | Günlük telefon kullanım süresi |
| Uyku Kalitesi | Uyku düzeni ve kalitesi |
| Mola Düzeni | Ders çalışma sırasındaki mola düzeni |

---

# Çıktı

Sistem aşağıdaki verimlilik seviyelerini üretmektedir:

- Düşük
- Orta
- Yüksek
- Çok Yüksek

---

# Özellikler

- Bulanık üyelik fonksiyonları
- Kural tabanlı çıkarım sistemi
- Centroid durulaştırma yöntemi
- Grafiksel analiz ekranları
- Aktif kural görüntüleme
- Etkileşimli Streamlit arayüzü

---

# Kurulum

Projeyi çalıştırmak için:

```bash
git clone https://github.com/musenna111/study-efficiency-fuzzy.git
cd study-efficiency-fuzzy