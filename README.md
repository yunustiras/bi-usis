# bi-usis
  * Bi-usis, Yıldız Teknik Üniversitesi Bilgisayar Mühendisliği Sistem Programlama dersi için oluşturulmuş web tabanlı öğrenci bilgileri ve danışmanlık sistemi yönetim platformudur.

### Documentation Link
  * https://docs.google.com/document/d/14VpVzDIwbfFgsFLYoF8S2NRH8x-am4g0eatJj1V4LZQ/edit?ts=5a9be923

### Kurulum
  * https://github.com/yunustiras/bi-usis/blob/master/DEVELOPMENT.md

# Sistem Analizi
  * Bir öğrencinin, öğrencilik kaydının başlangıcında itibaren tüm kişisel bilgilerinin yönetimini, öğrenci ve öğretmenler arasındaki danışmanlık sistemin yönetimi ve idari personelin bu aksiyonlar içerisinde etkin olmasını sağlayacak bir sistem tasarlanacaktır. Sistem, yetkisi dahilinde bireylere verileri ekleme, güncelleme, görüntüleme ve silme olanağı sağlamaktadır. Yetkilendirilmiş kullanıcılar sistem üzerindeki öğrenciler hakkında istatistiksel veri alabilecektir.
### Kullanilacak Teknolojiler
  * Python 3.6
  * Flask 1.0 (A Python Microframework)
  * Jinja2 (Template Engine)
  * Bootstrap (HTML, CSS, JS library)
  * JQuery (Javascript Library)
  * Icon : Font Awesome fontawesome.com, Icon Finder iconfinder.com
  * Mysql 5.6
  * Git(Version Control System)
  * Docker (Virtualization Platform)

### Kullanıcı Rolleri ve Fonksiyonları
  * Ogrenci
      * Kendi Kaydini tamamlayabilir.
      * Kendi Verilerinin bir kısmını guncelleyebilir.
      * Kendi verilerini goruntuleyebilir.
      * Danışman ile görüşmelerini görüntüleyebilir
      * Danışman ile görüşme ayarlayabilir

  * Idari Personel
      * Bireysel olarak veya toplu (bir dosyadan veriler alınıyor) şekilde yeni Ogrenci kaydı yapabilir
      * Ogrencilerin bilgilerini Güncelleme
      * Ogrencilerin bilgilerini Görüntüleme
      * Ogrenciye danisman atayabilme
      * Ogrenci hakkinda gorus yazma
      * Öğrenci hakkında yazılan görüşleri görüntüleme
      * Öğrenci ve danışman arasındaki görüşmeleri görüntüleyebilme
      * Danışmanın görüşme sonucu yaptığı yorumları görüntüleyebilme
      * Yeni danışman oluşturabilir
      * Danışmanların tüm bilgilerini güncellleyebilir
      * Danışmanların tüm bilgilerini görüntüleyebilir
      * Yeni öğretmen oluşturabilir
      * Öğretmenlerin tüm bilgilerini güncellleyebilir
      * Öğretmenlerin tüm bilgilerini görüntüleyebilir

  * Ogretmen
      * Ogrencilerin bilgilerini görüntüleme
      * Ogrenci hakkinda gorus bildirebilir
      * Öğrenci hakkındaki görüşleri görüntüleyebilir

  * Danisman
      * Danışmanı olduğu öğrenci ile görüşme ayarlayabilir
      * Danışmanı olduğu öğrenci ile görüşme sonunda görüşünü belirtebilir
      * Danışmanı olduğu öğrencinin bir kısım verilerini güncelleyebilir

# Veritabanı
![Veritabanı](https://github.com/yunustiras/bi-usis/blob/master/database/database.png)
# Takım Üyeleri
  * Yunus Tıraş
  * Emre Guler
