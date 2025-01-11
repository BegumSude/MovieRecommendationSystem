# MOVIE RECOMMENDATION SYSTEM 🎬🍿🎥 #

### **Proje Açıklaması**

Bu proje, kullanıcıların seçtikleri film türü (**genre**) ve anahtar kelime (**keyword**) doğrultusunda öneriler almasını sağlayan bir **Film Öneri Sistemi**dir. Proje, **The Movie Database (TMDb)** API'sini kullanarak filmler hakkında bilgi toplar ve bu bilgileri kullanıcıya görsel bir arayüzle sunar. Kullanıcılar filmleri afişleriyle birlikte görüntüleyebilir ve detaylı açıklamalarına ulaşabilir.

---

### **Kullanılan Teknolojiler 💻**

- **Python**: Projenin temel programlama dili.
- **Streamlit**: Kullanıcı arayüzü oluşturmak için kullanıldı.
- **Pandas**: Veri manipülasyonu ve işlenmesi için.
- **Pillow (PIL)**: Film afişlerini indirmek ve kaydetmek için.
- **Requests**: API ile iletişim kurmak için HTTP istekleri gönderir.
- **Kaggle**: Film veri setine erişmek için.

---

### **Projede Kullanılan Veriler 🔍**

- **Film Verileri**: Kaggle'dan indirilen `tmdb_10_movies.csv` dosyası kullanıldı. Bu dosya filmlerle ilgili başlık, tür, açıklama gibi bilgileri içerir.
- **API Kullanımı**: 
  - **TMDb API Key**: Afişleri ve diğer ek bilgileri almak için TMDb API kullanıldı.
  - **Poster URL'leri**: Filmlerin afişlerini indirip yerel olarak kaydetmek için.

---

### **Özellikler 🚀**

1. **Film Afişlerini İndirme ve Kaydetme**:
   - TMDb API'sinden alınan bilgilerle filmlerin afiş URL'leri belirlenir ve `Posters` klasörüne kaydedilir.
   - Afiş bilgileri `movie_posters.csv` dosyasına kaydedilir.

2. **Film Türleri ve Anahtar Kelimeler ile Arama**:
   - Kullanıcılar **film türü** ve **anahtar kelime** seçerek arama yapabilir.
   - İlgili kriterlere uyan filmler listelenir.

3. **Streamlit ile Görsel Arayüz**:
   - Kullanıcı dostu bir arayüzle filmler listelenir.
   - Afişler, film açıklamaları ve oylamalar görsel olarak sunulur.
   - Filmin ana sayfasına bağlantı (varsa) sağlanır.
  


## Arayüz Görselleri

Aşağıda, Movie Recommendation System'in kullanıcı arayüzüne ait bazı ekran görüntüleri yer almaktadır.<br/>

### Kullanıcı Giriş Ekranı ###
<img width="1440" alt="1" src="https://github.com/user-attachments/assets/49fe16f1-1968-4669-a86d-ab60e0b0cb67" />
<br>

### Film Önerileri Arayüzü ###
<img width="1440" alt="3" src="https://github.com/user-attachments/assets/cb04fef6-cbed-4259-9a47-ebabc45fba03" />

