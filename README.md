# Uzman Akademi — Yeni Web Tasarımı

uzmanakademi.com.tr için yeniden tasarlanmış, bağımlılığı olmayan statik HTML/CSS/JS site.
Tüm metinler ve görseller mevcut siteden alınmıştır.

## Sayfalar (48)

| Dosya | Açıklama |
| --- | --- |
| `index.html` | Anasayfa |
| `iletisim.html` | Şubeler / İletişim — aranabilir, bölgeye göre filtrelenebilir şube listesi |
| `hakkimizda.html` | Hakkımızda + Sıkça Sorulan Sorular |
| `programlarimiz.html` | Sınav, İlkokul (ODAK), Okuma Yazma, Temel Matematik, ÖdevLab |
| `kucuk-yas-okuma-anlama-kursu.html` | İlkokul grupları |
| `lgs-gruplarina-yonelik-kurslarimiz.html` | LGS grupları |
| `yks-gruplarina-yonelik-kurslarimiz.html` | YKS grupları |
| `canli-online-kurslarimiz.html` | Canlı online kurslar |
| `mental-aritmetik.html` | Mental Aritmetik |
| `calismalarimiz.html` | Çalışmalarımız |
| `referanslarimiz.html` | 44 başarı hikâyesi videosu, veli yorumları, anlaşmalı kurumlar |
| `ogretmenlerimiz-cevapliyor.html` | 33 öğretmen videosu |
| `okuyalim-ogrenelim.html` + `blog-*.html` | Blog ve 4 yazı |
| `*-subesi.html`, `basaksehir.html` | 29 şube sayfası |
| `gizlilik-politikasi.html`, `dilek-sikayet.html` | Gizlilik politikası, dilek & şikayet formu |

Ayrıca `sitemap.xml` ve `robots.txt` üretilir.

## Yapı

```
css/style.css        Ortak stiller (renkler :root içinde)
js/main.js           Menü, şube arama/filtre, formlar, video penceresi, harita
assets/img/          Optimize edilmiş görseller (sayfa/, sube/, video/, referanslar/)
_build/build.py      Sayfa üreticisi
_build/icerik.json   Sayfa metinleri, şube metinleri, blog yazıları, video listeleri
```

## Sayfaları değiştirme

Header, footer ve tüm sayfalar `_build/build.py` ile üretilir. Bir metni, şubeyi ya da menüyü
değiştirmek için `_build/build.py` veya `_build/icerik.json` dosyasını düzenleyip sayfaları yeniden üretin:

```bash
python3 _build/build.py
```

HTML dosyalarını doğrudan düzenlerseniz değişiklikler bir sonraki üretimde kaybolur.

## Yerelde açma

```bash
python3 -m http.server 8000
```

Ardından `http://localhost:8000` adresini açın.

## Yayına alırken

- Sayfalar `.html` uzantılıdır; `canonical` ve `sitemap.xml` adresleri ise mevcut sitedeki uzantısız
  adresleri kullanır (ör. `/hakkimizda`). Barındırma tarafında "uzantısız adres" (clean/pretty URLs)
  açılmalıdır — Netlify, Vercel, Cloudflare Pages bunu destekler.
- Mevcut sitedeki farklı adresler için yönlendirme önerisi:
  - `/blank-1` → `/dilek-sikayet`
  - `/post/bilmedigi-kelimede-takilan-cocuk` → `/blog-bilmedigi-kelimede-takilan-cocuk`
  - `/post/sinavda-soruyu-yanlis-okumak` → `/blog-sinavda-soruyu-yanlis-okumak`
  - `/post/hızlı-okuyan-çocuk-okuduğunu-anlar-mı-velilerin-en-çok-sorduğu-7-soru` → `/blog-hizli-okuyan-cocuk-okudugunu-anlar-mi`
  - `/post/okula-uyum-sürecini-kolaylaştırmanın-7-etkili-yolu` → `/blog-okula-uyum-surecini-kolaylastirmanin-7-etkili-yolu`

## Formlar

Bilgi formu ve dilek & şikayet formu varsayılan olarak bilgileri doldurulmuş bir e-postayla
`info@uzmanakademi.com.tr` adresine yönlendirir. Bir form servisine bağlamak için `<form>` etiketine adres ekleyin:

```html
<form data-lead-form data-endpoint="https://ornek.com/form" novalidate>
```

## Videolar ve harita

YouTube videoları ve Google Haritalar yalnızca ziyaretçi tıkladığında yüklenir (sayfa hızı ve gizlilik için).
Videolar `youtube-nocookie.com` üzerinden oynatılır.
