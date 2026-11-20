# Uzman Akademi — Yeni Web Tasarımı

uzmanakademi.com.tr için yeniden tasarlanmış, bağımlılığı olmayan statik HTML/CSS/JS site.
İçerik ve görseller mevcut siteden alınmıştır.

## Sayfalar

| Dosya | Açıklama |
| --- | --- |
| `iletisim.html` | Şubeler / İletişim: hızlı iletişim kartları, aranabilir ve bölgeye göre filtrelenebilir 29 şube, yol tarifi bağlantıları, bilgi formu |
| `index.html` | Anasayfa: hero, kazanımlar, LGS birincisi, programlar, çalışmalar, blog, veli yorumları, anlaşmalı kurumlar, bilgi formu |

Henüz yeniden tasarlanmamış sayfalara (Hakkımızda, Programlarımız, şube sayfaları vb.) verilen bağlantılar mevcut siteye gider.

## Yapı

```
css/style.css        Ortak stiller (renkler :root içinde)
js/main.js           Menü, şube arama/filtre, form doğrulama
assets/img/          Optimize edilmiş görseller
```

## Yerelde açma

Herhangi bir statik sunucu yeterlidir:

```bash
python3 -m http.server 8000
```

Ardından `http://localhost:8000/iletisim.html` adresini açın.

## Bilgi formu

Form varsayılan olarak bilgileri doldurulmuş bir e-postayla `info@uzmanakademi.com.tr` adresine yönlendirir.
Bir form servisine (ör. kendi API'niz, Formspree vb.) bağlamak için `<form>` etiketine adres ekleyin:

```html
<form data-lead-form data-endpoint="https://ornek.com/form" novalidate>
```
