# Akıllı Ders Çalışma Verimlilik Sistemi

## 1. Proje Konusu

Bu projede bulanık mantık yöntemi kullanılarak öğrencilerin ders çalışma verimliliğini analiz eden bir sistem geliştirilmiştir. Sistem; çalışma süresi, telefon kullanımı, uyku kalitesi ve mola düzeni gibi faktörleri değerlendirerek öğrencinin verimlilik seviyesini hesaplamaktadır.

---

## 2. Projenin Amacı

Projede amaç, öğrencilerin ders çalışma alışkanlıklarını klasik kesin kurallar yerine bulanık mantık yaklaşımı ile daha gerçekçi şekilde analiz etmektir.

Gerçek hayatta “iyi uyku”, “fazla telefon kullanımı” veya “orta seviye çalışma” gibi kavramlar kesin sınırlarla ifade edilemez. Bu nedenle bulanık mantık kullanılarak daha esnek ve insan düşüncesine yakın bir sistem geliştirilmiştir.

---

## 3. Kullanılan Teknolojiler

- Python
- Streamlit
- NumPy
- SciPy
- Scikit-Fuzzy
- Matplotlib

---

## 4. Sistemin Giriş Parametreleri

Sistemde dört adet giriş değişkeni bulunmaktadır.

| Parametre | Aralık |
|---|---|
| Çalışma Süresi | 0 - 8 Saat |
| Telefon Kullanımı | 0 - 6 Saat |
| Uyku Kalitesi | 0 - 10 |
| Mola Düzeni | 0 - 10 |

---

## 5. Çıkış Parametresi

Sistem çıktısı öğrencinin verimlilik skorudur.

| Çıkış | Aralık |
|---|---|
| Verimlilik Skoru | 0 - 100 |

Verimlilik sonucu aşağıdaki seviyelerden biri olarak yorumlanmaktadır:

- Düşük Verimlilik
- Orta Verimlilik
- Yüksek Verimlilik
- Çok Yüksek Verimlilik

---

## 6. Bulanık Mantık Yapısı

Projede Mamdani tipi bulanık çıkarım sistemi kullanılmıştır.

Sistem aşağıdaki aşamalardan oluşmaktadır:

1. Giriş değerlerinin alınması
2. Üyelik fonksiyonları ile bulanıklaştırma
3. Kural tabanının çalıştırılması
4. Çıkarım işlemi
5. Centroid yöntemi ile durulaştırma
6. Sonucun kullanıcıya gösterilmesi

---

## 7. Üyelik Fonksiyonları

Her giriş değişkeni için üç adet üyelik fonksiyonu tanımlanmıştır.

Örnek:

### Çalışma Süresi

- Düşük
- Orta
- Yüksek

### Telefon Kullanımı

- Az
- Orta
- Fazla

### Uyku Kalitesi

- Kötü
- Orta
- İyi

### Mola Düzeni

- Yetersiz
- Dengeli
- Aşırı

Çıkış değişkeni olan verimlilik için ise dört adet üyelik fonksiyonu oluşturulmuştur.

- Düşük
- Orta
- Yüksek
- Çok Yüksek

---

## 8. Kural Tabanı

Sistemde farklı durumları değerlendiren bulanık kurallar bulunmaktadır.

Örnek kurallar:

- Eğer çalışma süresi yüksek VE telefon kullanımı az ise verimlilik yüksek olur.
- Eğer uyku kalitesi kötü VE telefon kullanımı fazla ise verimlilik düşük olur.
- Eğer çalışma süresi orta VE mola düzeni dengeli ise verimlilik orta olur.

Bu kurallar sayesinde sistem insan benzeri karar verebilmektedir.

---

## 9. Arayüz Tasarımı

Projede Streamlit tabanlı kullanıcı arayüzü geliştirilmiştir.

Arayüz içerisinde:

- Slider ile giriş değerleri değiştirme
- Verimlilik skorunu görüntüleme
- Verimlilik seviyesini gösterme
- Üyelik fonksiyonlarını grafiksel gösterme
- Durulaştırma grafiğini görüntüleme
- Aktif kuralları listeleme

özellikleri bulunmaktadır.

---

## 10. Test Senaryoları

### Senaryo 1

| Parametre | Değer |
|---|---|
| Çalışma Süresi | 7 |
| Telefon Kullanımı | 1 |
| Uyku Kalitesi | 9 |
| Mola Düzeni | 7 |

Sonuç: Çok yüksek verimlilik

---

### Senaryo 2

| Parametre | Değer |
|---|---|
| Çalışma Süresi | 2 |
| Telefon Kullanımı | 5 |
| Uyku Kalitesi | 3 |
| Mola Düzeni | 2 |

Sonuç: Düşük verimlilik

---

### Senaryo 3

| Parametre | Değer |
|---|---|
| Çalışma Süresi | 5 |
| Telefon Kullanımı | 2 |
| Uyku Kalitesi | 6 |
| Mola Düzeni | 6 |

Sonuç: Orta verimlilik

---

## 11. Sonuç

Bu projede bulanık mantık yöntemi kullanılarak öğrencilerin ders çalışma verimliliğini analiz eden bir sistem geliştirilmiştir.

Sistem klasik kesin kurallar yerine esnek karar mekanizması kullanarak daha gerçekçi sonuçlar üretmektedir. Geliştirilen uygulama sayesinde kullanıcılar çalışma alışkanlıklarını analiz ederek verimlilik seviyelerini gözlemleyebilmektedir.

Proje, bulanık mantık sistemlerinin gerçek hayat problemlerinde nasıl kullanılabileceğini başarılı şekilde göstermektedir.