#!/usr/bin/env python3
"""Uzman Akademi statik sayfa üreticisi (iletisim.html + index.html)."""
import html, sys, urllib.parse, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else ROOT
O = "https://www.uzmanakademi.com.tr/"
YT = "https://www.youtube.com/channel/UCaJ9dKDHjo6WDYuh16v4AeQ"
IG = "https://www.instagram.com/uzmanakademii/"
FB = "https://www.facebook.com/uzmanakademi"
LOGIN = "https://www.uzmanlarakademi.com"
e = html.escape

# ---------------------------------------------------------------- ikonlar
P = {
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/><path d="m10 8 5 2-5 2z"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "right": '<path d="m9 18 6-6-6-6"/>',
 "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
 "arrow-ur": '<path d="M7 17 17 7M7 7h10v10"/>',
 "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
 "nav": '<path d="m3 11 19-9-9 19-2-8-8-2z"/>',
 "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
 "landmark": '<path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7z"/><path d="M12 6v6M9 9h6"/>',
 "check": '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
 "check-s": '<path d="M20 6 9 17l-5-5"/>',
 "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
 "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>',
 "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
 "star": '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="currentColor" stroke="none"/>',
 "play": '<circle cx="12" cy="12" r="10"/><path d="m10 8 6 4-6 4z" fill="currentColor"/>',
 "login": '<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><path d="m10 17 5-5-5-5M15 12H3"/>',
 "fb": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
 "ig": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
 "yt": '<path d="M2.5 17a24.1 24.1 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.6 49.6 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.1 24.1 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.6 49.6 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/>',
}
def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{P[name]}</svg>')

# ---------------------------------------------------------------- şubeler
# (ad, bölge, il etiketi, adres, yer tarifi, orijinal sayfa)
BR = [
 ("Bakırköy","istanbul","İstanbul","Zuhuratbaba Mah. Şükrançiftliği Sok. No: 21 D: 1-2-3-4 Bakırköy","Bakırköy Meydan","bakirkoy-subesi"),
 ("Beylikdüzü","istanbul","İstanbul","Cumhuriyet Mah. Atatürk Bulvarı No: 3 Kat 2 Beycity AVM, Beylikdüzü","Metrobüs durağına 150 metre","beylikduzu-subesi"),
 ("Halkalı","istanbul","İstanbul","Halkalı Merkez Mah. Karakol Sok. No: 1/1 My Plaza Kat 2, Küçükçekmece","Halkalı Meydan","halkali-subesi"),
 ("Üsküdar","istanbul","İstanbul","Sultantepe Mah. Cumhuriyet Cad. No: 39 Kat 4, Üsküdar","Fıstıkağacı Metro yanı","uskudar-subesi"),
 ("Şişli","istanbul","İstanbul","Mecidiyeköy Mah. Lati Lokum Sok. No: 2 Kadriye Ap. D: 4, Şişli","Mecidiyeköy Meydan","sisli-subesi"),
 ("Maltepe","istanbul","İstanbul","Cevizli Mah. Bağdat Cad. No: 543 Karaca Rezidans Kat 1 B-46, Maltepe","Marmaray durağına 50 metre","maltepe-subesi"),
 ("Sancaktepe","istanbul","İstanbul","Eyüp Sultan Mah. Kızılay Cad. No: 3 Kat 1, 34785 Sancaktepe / İstanbul","","sancaktepe-subesi"),
 ("Gaziosmanpaşa","istanbul","İstanbul","Merkez Mah. Salihpaşa Cad. No: 15 D: 166 Novi Bazaar, Gaziosmanpaşa","Gaziosmanpaşa Meydan","gaziosmanpasa-subesi"),
 ("Ataşehir","istanbul","İstanbul","Küçükbakkalköy Mah. Ali Ay Sok. No: 3 D: 2, Ataşehir","Kaymakamlık Sokağı","atasehir-subesi"),
 ("Pendik","istanbul","İstanbul","Doğu Mah. Erol Kaya Cad. Aralık Sok. No: 4 D: 1, Pendik","Pendik Meydan","pendik-subesi"),
 ("Başakşehir","istanbul","İstanbul","Kayabaşı Mah. Gazi Yaşargil Cad. No: 1/2 Daire: 2, Başakşehir / İstanbul","","basaksehir"),
 ("Çankaya","ankara","Ankara","Meşrutiyet Mah. Atatürk Blv. No: 127 Selcan İş Hanı K: 4 Kapı No: 403-406, Çankaya","Kızılay","ankara-subesi"),
 ("Etimesgut","ankara","Ankara","Kazım Karabekir Mah. 2052 Sok. No: 8 D: 1-2, Etimesgut / Ankara","Belediye karşısı","etimesgut-subesi"),
 ("Konak","izmir","İzmir","Alsancak Mah. Kıbrıs Şehitleri Cad. No: 152 Aksoy Rezidans K: 1, Konak","","izmir-subesi"),
 ("Karşıyaka","izmir","İzmir","Tersane Mah. Şehit Asım Aksoy Cad. No: 20/B, Karşıyaka / İzmir","","izmir-karsiyaka-subesi"),
 ("Kocaeli","kocaeli","Kocaeli · İzmit","Yenişehir, Dönmez Sk. Birlik İş Merkezi No: 6 Kat: 1 Daire: 3-4, 41300 İzmit / Kocaeli","","kocaeli-subesi"),
 ("Gebze","kocaeli","Kocaeli","Osman Yılmaz Mah. Atatürk Cd. No: 48 Kat: 3 Daire: 7, 41400 Gebze / Kocaeli","","gebze-subesi"),
 ("Bursa","diger","Bursa","Doğanbey Mah. 1. Doğanbey Sok. M. Özer İş Merkezi No: 4, Osmangazi","Şehreküstü Metro","bursa-subesi"),
 ("Adana","diger","Adana","Reşatbey Mah. 62008. Sokak No: 10 Dr. Suat Erem Ap., Seyhan","","adana-subesi"),
 ("Antalya","diger","Antalya","Tahılpazarı Mah. 471 Sok. Temizkan 2 İş Merkezi No: 5/B, Muratpaşa","MarkAntalya karşısı","antalya-subesi"),
 ("Konya","diger","Konya","İhsaniye Mah. İnce Minare Sok. No: 33","Zafer Meydanı'nda, Civil mağazasının bulunduğu sokakta","konya-subesi"),
 ("Gaziantep","diger","Gaziantep","Mücahitler Mah. Ali Fuat Cebesoy Blv. No: 4 Sebzeci Plaza Dükkan No: 5, Şehitkamil","","gaziantep-subesi"),
 ("Kayseri","diger","Kayseri","Gevher Nesibe Mah. Kenarcık Sk. No: 5 Karum Plaza D: 14, Kocasinan","","kayseri-subesi"),
 ("Sakarya","diger","Sakarya","Semerciler Mah. Sait Faik Sk. No: 41, Adapazarı","","sakarya-subesi"),
 ("Mersin","diger","Mersin","Güvenevler Mah. 1917 Sok. Doğanyıldız İş Hanı E Blok Kat 2, Yenişehir","","mersin-subesi"),
 ("Samsun","diger","Samsun","Hançerli Mah. Dervişzade Sok. Albayrak İş Hanı No: 10/2, İlkadım","","samsun-subesi"),
 ("Diyarbakır","diger","Diyarbakır","Fırat Mah. 507. Sok. No: 13A Daire: 22 Çeysa Serhat Plaza, Urfa Bulvarı, Kayapınar","","diyarbakir-subesi"),
 ("Denizli","diger","Denizli","Siteler Mah. İncilipınar Cad. No: 16-A Zemin Kat, Pamukkale / Denizli","","denizli-subesi"),
 ("Eskişehir","diger","Eskişehir","Hacı Ali Bey Mah. Sakarya Cad. Gürdal Abacı Plaza No: 50 D: 7, Tepebaşı / Eskişehir","","eskisehir-subesi"),
]
REGIONS = [("istanbul","İstanbul"),("ankara","Ankara"),("izmir","İzmir"),("kocaeli","Kocaeli"),("diger","Diğer iller")]
# Menü/altbilgide orijinal sitedeki sıra
MENU_ORDER = ["Bakırköy","Beylikdüzü","Üsküdar","Halkalı","Şişli","Maltepe","Sancaktepe","Gaziosmanpaşa","Ataşehir","Pendik",
              "Çankaya","Etimesgut","Kocaeli","Konak","Karşıyaka","Bursa","Adana","Antalya","Konya","Gaziantep","Kayseri",
              "Sakarya","Mersin","Samsun","Diyarbakır","Gebze","Denizli","Eskişehir","Başakşehir"]
BYNAME = {b[0]: b for b in BR}
# Her şubenin bağlı olduğu il, ilçe ve (İstanbul için) yaka
LOC = {
    "Bakırköy": ("İstanbul", "Bakırköy", "Avrupa Yakası"), "Başakşehir": ("İstanbul", "Başakşehir", "Avrupa Yakası"),
    "Beylikdüzü": ("İstanbul", "Beylikdüzü", "Avrupa Yakası"), "Gaziosmanpaşa": ("İstanbul", "Gaziosmanpaşa", "Avrupa Yakası"),
    "Halkalı": ("İstanbul", "Küçükçekmece", "Avrupa Yakası"), "Şişli": ("İstanbul", "Şişli", "Avrupa Yakası"),
    "Ataşehir": ("İstanbul", "Ataşehir", "Anadolu Yakası"), "Maltepe": ("İstanbul", "Maltepe", "Anadolu Yakası"),
    "Pendik": ("İstanbul", "Pendik", "Anadolu Yakası"), "Sancaktepe": ("İstanbul", "Sancaktepe", "Anadolu Yakası"),
    "Üsküdar": ("İstanbul", "Üsküdar", "Anadolu Yakası"),
    "Çankaya": ("Ankara", "Çankaya", ""), "Etimesgut": ("Ankara", "Etimesgut", ""),
    "Konak": ("İzmir", "Konak", ""), "Karşıyaka": ("İzmir", "Karşıyaka", ""),
    "Kocaeli": ("Kocaeli", "İzmit", ""), "Gebze": ("Kocaeli", "Gebze", ""),
    "Adana": ("Adana", "Seyhan", ""), "Antalya": ("Antalya", "Muratpaşa", ""), "Bursa": ("Bursa", "Osmangazi", ""),
    "Denizli": ("Denizli", "Pamukkale", ""), "Diyarbakır": ("Diyarbakır", "Kayapınar", ""),
    "Eskişehir": ("Eskişehir", "Tepebaşı", ""), "Gaziantep": ("Gaziantep", "Şehitkamil", ""),
    "Kayseri": ("Kayseri", "Kocasinan", ""), "Konya": ("Konya", "Selçuklu", ""), "Mersin": ("Mersin", "Yenişehir", ""),
    "Sakarya": ("Sakarya", "Adapazarı", ""), "Samsun": ("Samsun", "İlkadım", ""),
}
PLATE = {"İstanbul": "34", "Ankara": "06", "İzmir": "35", "Kocaeli": "41", "Adana": "01", "Antalya": "07",
         "Bursa": "16", "Denizli": "20", "Diyarbakır": "21", "Eskişehir": "26", "Gaziantep": "27", "Kayseri": "38",
         "Konya": "42", "Mersin": "33", "Sakarya": "54", "Samsun": "55"}
_TR = "abcçdefgğhıijklmnoöprsştuüvyz"
def tr_key(t):
    t = t.replace("I", "ı").replace("İ", "i").lower()
    return [(_TR.index(ch) if ch in _TR else 100 + ord(ch)) for ch in t]
BIG = ["İstanbul", "Ankara", "İzmir", "Kocaeli"]
IL_ORDER = BIG + sorted({v[0] for v in LOC.values()} - set(BIG), key=tr_key)
YAKA_ORDER = ["Avrupa Yakası", "Anadolu Yakası"]

def il_groups():
    """[(il, [(yaka, [şube, ...]), ...]), ...] — şubeler ilçe adına göre sıralı."""
    out = []
    for il in IL_ORDER:
        items = sorted([b for b in BR if LOC[b[0]][0] == il], key=lambda b: tr_key(LOC[b[0]][1]))
        yakas = [y for y in YAKA_ORDER if any(LOC[b[0]][2] == y for b in items)]
        if yakas:
            out.append((il, [(y, [b for b in items if LOC[b[0]][2] == y]) for y in yakas]))
        else:
            out.append((il, [("", items)]))
    return out

def loc_label(b):
    il, ilce, _ = LOC[b[0]]
    return f"{il} / {ilce}"
def label(b):
    n, r = b[0], b[1]
    if r == "ankara": return f"Ankara/{n}"
    if r == "izmir": return f"İzmir/{n}"
    return n

def maps(b):
    q = f"Uzman Akademi {b[0]} Şubesi, {b[3]}"
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(q)

# ---------------------------------------------------------------- ortak parçalar
def head(title, desc, canonical):
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#15125a">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Uzman Akademi">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="assets/img/ekip-1.jpg">
<link rel="icon" type="image/png" href="assets/img/logo-mark.png">
<link rel="apple-touch-icon" href="assets/img/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
"""

def header(active):
    def cur(k): return ' aria-current="page"' if active == k else ""
    G = dict(il_groups())
    def grp(title, items, label=lambda b: b[0]):
        return (f'<div class="dd-group"><span class="dd-group__title">{e(title)}</span>' +
                "".join(f'<a href="{b[5]}.html">{e(label(b))}</a>' for b in items) + "</div>")
    ist = dict(G["İstanbul"])
    cols = [grp("İstanbul · Avrupa", ist["Avrupa Yakası"]), grp("İstanbul · Anadolu", ist["Anadolu Yakası"]),
            '<div class="dd-stack">' + "".join(grp(il, G[il][0][1]) for il in ("Ankara", "İzmir", "Kocaeli")) + "</div>",
            grp("Diğer iller", [b for il in IL_ORDER if il not in BIG for b in G[il][0][1]], lambda b: LOC[b[0]][0])]
    branch_links = "\n".join("              " + c for c in cols)
    return f"""<a class="skip-link" href="#icerik">İçeriğe geç</a>

<div class="topbar">
  <div class="container">
    <div class="topbar__info">
      <a href="tel:4443644">{ic("phone")} 444 3 644</a>
      <a href="mailto:info@uzmanakademi.com.tr">{ic("mail")} info@uzmanakademi.com.tr</a>
      <span>{ic("clock")} Hafta içi / Hafta sonu 09:00 – 19:00</span>
    </div>
    <div class="topbar__right">
    <a class="topbar__login" href="{LOGIN}" target="_blank" rel="noopener">{ic("login")} Dijital platform girişi</a>
    <div class="topbar__social">
      <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ic("fb")}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ic("ig")}</a>
      <a href="{YT}" target="_blank" rel="noopener" aria-label="YouTube">{ic("yt")}</a>
    </div>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Uzman Akademi — Anasayfa">
      <img src="assets/img/logo-mark.png" width="52" height="52" alt="">
      <span class="brand__text"><span class="brand__name">Uzman Akademi</span><span class="brand__tag">Hızlı Okuma Kursu</span></span>
    </a>

    <nav class="nav" id="site-nav" aria-label="Ana menü">
      <ul class="nav__list">
        <li class="nav__item"><a class="nav__link" href="index.html"{cur("home")}>Anasayfa</a></li>
        <li class="nav__item">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="dd-about"{cur("about")}>Kurumsal {ic("chev")}</button>
          <div class="dropdown" id="dd-about">
            <a href="hakkimizda.html">Hakkımızda</a>
            <a href="calismalarimiz.html">Çalışmalarımız</a>
            <a href="referanslarimiz.html">Referanslarımız</a>
            <a href="ogretmenlerimiz-cevapliyor.html">Öğretmenlerimiz cevaplıyor</a>
          </div>
        </li>
        <li class="nav__item">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="dd-programs"{cur("programs")}>Programlarımız {ic("chev")}</button>
          <div class="dropdown" id="dd-programs">
            <a href="programlarimiz.html">Tüm programlarımız</a>
            <a href="kucuk-yas-okuma-anlama-kursu.html">İlkokul gruplarına yönelik kurslarımız</a>
            <a href="lgs-gruplarina-yonelik-kurslarimiz.html">LGS gruplarına yönelik kurslarımız</a>
            <a href="yks-gruplarina-yonelik-kurslarimiz.html">YKS gruplarına yönelik kurslarımız</a>
            <a href="canli-online-kurslarimiz.html">Canlı Online Kurslarımız</a>
            <a href="mental-aritmetik.html">Mental Aritmetik</a>
          </div>
        </li>
        <li class="nav__item"><a class="nav__link" href="okuyalim-ogrenelim.html"{cur("blog")}>Okuyalım Öğrenelim</a></li>
        <li class="nav__item">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="dd-branches"{cur("contact")}>Şubeler/İletişim {ic("chev")}</button>
          <div class="dropdown dropdown--wide" id="dd-branches">
{branch_links}
              <a class="dropdown__all" href="iletisim.html">Tüm şubeler ve iletişim bilgileri →</a>
          </div>
        </li>
      </ul>
      <div class="nav__mobile-extra">
        <a class="btn btn--primary btn--block" href="tel:4443644">{ic("phone")} 444 3 644’ü ara</a>
        <a class="btn btn--navy btn--block" href="{LOGIN}" target="_blank" rel="noopener">{ic("login")} Dijital platforma giriş</a>
      </div>
    </nav>

    <div class="header-actions">
      <a class="header-phone" href="tel:4443644">
        <span class="header-phone__icon">{ic("phone")}</span>
        <span><small>Bize ulaşın</small>444 3 644</span>
      </a>
      <a class="btn btn--primary btn--sm" href="#bilgi-formu">Bilgi Al</a>
    </div>

    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Menüyü aç"><span></span></button>
  </div>
</header>
"""

def lead_section():
    opts = "".join(f'<option>{x}</option>' for x in
                   ["1. Sınıf","2. Sınıf","3. Sınıf","4. Sınıf","5. Sınıf","6. Sınıf","7. Sınıf","8. Sınıf",
                    "9. Sınıf","10. Sınıf","11. Sınıf","12. Sınıf","Mezun/Yetişkin"])
    return f"""
<section class="section lead-section" id="bilgi-formu" aria-labelledby="form-title">
  <div class="container lead-grid">
    <div class="lead-copy reveal">
      <span class="eyebrow eyebrow--light">Ücretsiz bilgi</span>
      <h2 class="section-title" id="form-title">Öğretmenlerimizden detaylı bilgi almak ister misiniz?</h2>
      <p class="section-lead">Formu doldurun; size en yakın şubemizdeki öğretmenlerimiz çocuğunuzun seviyesine uygun program için sizinle iletişime geçsin.</p>
      <ul class="lead-points">
        <li>{ic("check")} Okuma ölçümü ile detaylı seviye analizi</li>
        <li>{ic("check")} Kişiye özel hızlı okuma kurs programı</li>
        <li>{ic("check")} Ücretsiz uzman psikolog desteği</li>
      </ul>
      <div class="lead-photos">
        <figure><img src="assets/img/ekip-2.jpg" width="1200" height="796" loading="lazy" alt="Uzman Akademi öğretmeni iki öğrenciyle birlikte çalışıyor"></figure>
        <figure><img src="assets/img/ekip-3.jpg" width="1200" height="578" loading="lazy" alt="Öğrenciler masa başında birlikte kitap okuyor"></figure>
      </div>
    </div>

    <div class="form-card reveal">
      <h3 class="form-card__title">Detaylı bilgi alın</h3>
      <p class="form-card__sub">Yıldızlı (<span class="req" style="color:var(--orange-600)">*</span>) alanlar zorunludur.</p>
      <form data-lead-form novalidate>
        <div class="form-grid">
          <div class="field">
            <label for="f-isim">İsim</label>
            <input id="f-isim" name="isim" type="text" autocomplete="name" placeholder="Adınız Soyadınız">
          </div>
          <div class="field">
            <label for="f-tel">Telefon <span class="req">*</span></label>
            <div class="phone-input">
              <span class="phone-input__code" aria-hidden="true">🇹🇷 +90</span>
              <input id="f-tel" name="telefon" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="5xx xxx xx xx" required aria-describedby="e-tel">
            </div>
            <span class="field__error" id="e-tel">Lütfen 10 haneli telefon numaranızı girin.</span>
          </div>
          <div class="field">
            <label for="f-il">İl ve İlçe <span class="req">*</span></label>
            <input id="f-il" name="il_ilce" type="text" autocomplete="address-level2" placeholder="Örn. İstanbul / Bakırköy" required aria-describedby="e-il">
            <span class="field__error" id="e-il">Lütfen il ve ilçenizi yazın.</span>
          </div>
          <div class="field">
            <label for="f-sinif">Sınıf/Düzey</label>
            <select id="f-sinif" name="sinif"><option value="">Seçiniz</option>{opts}</select>
          </div>
          <div class="field field--full">
            <label for="f-mesaj">Mesajınız <span class="opt">(İsteğe bağlı)</span></label>
            <textarea id="f-mesaj" name="mesaj" placeholder="Sormak istediklerinizi yazabilirsiniz"></textarea>
          </div>
        </div>
        <button class="btn btn--primary btn--block" type="submit" style="margin-top:20px">{ic("send")} Detaylı Bilgi Al</button>
        <p class="form-success" role="status" tabindex="-1">{ic("check")} <span>Teşekkürler! Talebiniz alındı, öğretmenlerimiz en kısa sürede sizinle iletişime geçecek.</span></p>
        <p class="form-note">Formu göndererek <a href="gizlilik-politikasi.html">Gizlilik Politikamızı</a> kabul etmiş olursunuz.</p>
      </form>
    </div>
  </div>
</section>
"""

def footer():
    fgroups = []
    for il, yakas in il_groups():
        if il not in BIG:
            continue
        items = [b for y, its in yakas for b in its]
        fgroups.append(f'<div class="fb-group"><span class="fb-group__title">{e(il)}</span><ul>' +
                       "".join(f'<li><a href="{b[5]}.html">{e(b[0])}</a></li>' for b in items) + "</ul></div>")
    others = [b for il, yakas in il_groups() if il not in BIG for y, its in yakas for b in its]
    fgroups.append('<div class="fb-group"><span class="fb-group__title">Diğer iller</span><ul>' +
                   "".join(f'<li><a href="{b[5]}.html">{e(LOC[b[0]][0])}</a></li>' for b in others) + "</ul></div>")
    branches = "\n".join("        " + g for g in fgroups)
    return f"""
<footer class="site-footer">
  <div class="container footer-top">
    <div class="footer-brand">
      <a class="brand" href="index.html">
        <img src="assets/img/logo-mark.png" width="52" height="52" alt="" loading="lazy">
        <span class="brand__text"><span class="brand__name">Uzman Akademi</span><span class="brand__tag">Hızlı Okuma Kursu</span></span>
      </a>
      <p>30 şube, binlerce öğrenci — Türkiye’nin en büyük hızlı okuma kursu. Canlı online olarak tüm Türkiye’de hizmetinizdeyiz.</p>
      <div class="footer-contact">
        <a href="tel:4443644">{ic("phone")} 444 3 644</a>
        <a href="tel:+902125420076">{ic("phone")} 0212 542 0076</a>
        <a href="mailto:info@uzmanakademi.com.tr">{ic("mail")} info@uzmanakademi.com.tr</a>
        <span>{ic("pin")} İstanbul / TÜRKİYE</span>
      </div>
    </div>
    <div class="footer-col">
      <h4>Hızlı menü</h4>
      <ul>
        <li><a href="index.html">Anasayfa</a></li>
        <li><a href="hakkimizda.html">Hakkımızda</a></li>
        <li><a href="calismalarimiz.html">Çalışmalar</a></li>
        <li><a href="programlarimiz.html">Programlar</a></li>
        <li><a href="referanslarimiz.html">Referanslar</a></li>
        <li><a href="okuyalim-ogrenelim.html">Makaleler</a></li>
        <li><a href="gizlilik-politikasi.html">Politikamız</a></li>
        <li><a href="iletisim.html">İletişim</a></li>
        <li><a href="dilek-sikayet.html">Dilek &amp; Şikayet</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Bağlantıda kalın</h4>
      <ul>
        <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
        <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="{YT}" target="_blank" rel="noopener">YouTube</a></li>
      </ul>
      <div class="social">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ic("fb")}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ic("ig")}</a>
        <a href="{YT}" target="_blank" rel="noopener" aria-label="YouTube">{ic("yt")}</a>
      </div>
    </div>
    <div class="footer-col footer-branches">
      <h4>Şubelerimiz</h4>
      <div class="fb-groups">
{branches}
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <p>© <span data-year>2026</span> Tüm hakları Uzman Akademi’ye aittir.</p>
      <nav aria-label="Yasal">
        <a href="gizlilik-politikasi.html">Gizlilik Politikamız</a>
        <a href="dilek-sikayet.html">Dilek &amp; Şikayet</a>
      </nav>
    </div>
  </div>
</footer>

<div class="mobile-cta">
  <a class="btn btn--navy" href="tel:4443644">{ic("phone")} Hemen Ara</a>
  <a class="btn btn--primary" href="#bilgi-formu">Bilgi Al</a>
</div>

<script src="js/main.js" defer></script>
</body>
</html>
"""

def org_jsonld():
    import json
    locs = [{"@type": "EducationalOrganization", "name": f"Uzman Akademi {b[0]} Şubesi",
             "address": {"@type": "PostalAddress", "streetAddress": b[3], "addressCountry": "TR"}} for b in BR]
    data = {"@context": "https://schema.org", "@type": "EducationalOrganization", "name": "Uzman Akademi",
            "description": "Türkiye'nin en büyük hızlı okuma kursu — okuma ve anlama eğitimi.",
            "url": "https://www.uzmanakademi.com.tr/", "telephone": "+90-444-3-644",
            "email": "info@uzmanakademi.com.tr",
            "sameAs": [FB, IG, YT], "subOrganization": locs}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>\n'

# ---------------------------------------------------------------- İLETİŞİM
def branch_card(b):
    name, reg, city, addr, lm, slug = b
    lmh = f'\n          <span class="branch-card__landmark">{ic("landmark")} {e(lm)}</span>' if lm else ""
    return f"""        <article class="branch-card" data-region="{reg}">
          <div class="branch-card__head">
            <span class="branch-card__pin">{ic("pin")}</span>
            <h3>{e(name)} Şubesi<small>{e(loc_label(b))}</small></h3>
          </div>
          <address>{e(addr)}</address>{lmh}
          <div class="branch-card__actions">
            <a href="{maps(b)}" target="_blank" rel="noopener" aria-label="{e(name)} Şubesi için yol tarifi al">{ic("nav")} Yol tarifi</a>
            <a href="{slug}.html" aria-label="{e(name)} Şubesi sayfası">{ic("info")} Şube sayfası</a>
          </div>
        </article>"""

def district_row(b):
    name, reg, city, addr, lm, slug = b
    il, ilce, yaka = LOC[name]
    tag = f'<span class="district__tag">{e(name)} Şubesi</span>' if name != ilce else ""
    lmh = f'<span class="district__lm">{ic("landmark")} {e(lm)}</span>' if lm else ""
    kw = " ".join(x for x in (il, ilce, name, yaka) if x)
    return f"""          <li class="district" data-branch data-region="{reg}" data-keywords="{e(kw)}">
            <div class="district__main">
              <h4 class="district__name">{e(ilce)}{tag}</h4>
              <address>{e(addr)}</address>
              {lmh}
            </div>
            <div class="district__actions">
              <a href="{maps(b)}" target="_blank" rel="noopener" aria-label="{e(name)} Şubesi için yol tarifi al">{ic("nav")} Yol tarifi</a>
              <a href="{slug}.html" aria-label="{e(name)} Şubesi sayfası">{ic("info")} Şube sayfası</a>
            </div>
          </li>"""


def il_card(il, yakas):
    n = sum(len(x) for _, x in yakas)
    wide = len(yakas) > 1
    parts = []
    for y, items in yakas:
        rows = "\n".join(district_row(b) for b in items)
        sub = f'<p class="il-card__sub">{e(y)} <span>{len(items)} şube</span></p>' if y else ""
        parts.append(f"""        <div class="il-card__part" data-group>
          {sub}
          <ul class="district-list">
{rows}
          </ul>
        </div>""")
    slug = il.replace("İ", "i").replace("I", "ı").lower().translate(str.maketrans("çğıöşü", "cgiosu"))
    return f"""      <section class="il-card{" il-card--wide" if wide else ""}" data-group id="il-{slug}" aria-label="{e(il)} şubeleri">
        <header class="il-card__head">
          <span class="il-card__plate" aria-hidden="true">{PLATE.get(il, "")}</span>
          <h3>{e(il)}</h3>
          <span class="il-card__count">{n} şube</span>
        </header>
        <div class="il-card__body">
{chr(10).join(parts)}
        </div>
      </section>"""


def contact_page():
    cards = [il_card(il, yakas) for il, yakas in il_groups()]
    groups = ['    <div class="il-grid">\n' + "\n".join(cards) + "\n    </div>"]
    chips = '<button class="chip" type="button" data-filter="all" aria-pressed="true">Tümü</button>' + "".join(
        f'<button class="chip" type="button" data-filter="{k}" aria-pressed="false">{t}</button>' for k, t in REGIONS)

    return head("Şubelerimiz ve İletişim | Uzman Akademi Hızlı Okuma Kursu",
                "Uzman Akademi şubeleri, adresleri ve iletişim bilgileri. Merkez telefon 444 3 644. 30 farklı şubede ve canlı online olarak tüm Türkiye'de hizmetinizdeyiz.",
                O + "iletisim") + org_jsonld() + "</head>\n<body>\n" + header("contact") + f"""
<main id="icerik">

<section class="page-hero">
  <div class="container page-hero__grid">
    <div>
      <nav class="breadcrumb" aria-label="Sayfa yolu">
        <a href="index.html">Anasayfa</a> {ic("right")} <span aria-current="page">Şubeler / İletişim</span>
      </nav>
      <span class="eyebrow eyebrow--light">İletişim bilgilerimiz</span>
      <h1>Size en yakın <em>Uzman Akademi</em> burada.</h1>
      <p class="page-hero__lead">Uzman Akademi olarak <strong>30 farklı şubede</strong>, canlı online olarak ise tüm Türkiye’de hizmetinizde olmaktan gurur duyuyoruz…</p>
      <div class="page-hero__actions">
        <a class="btn btn--primary" href="#subeler">{ic("pin")} Şubemi bul</a>
        <a class="btn btn--ghost-light" href="#bilgi-formu">Bilgi formunu doldur {ic("arrow")}</a>
      </div>
    </div>
    <div class="hero-photo">
      <div class="hero-photo__frame">
        <img src="assets/img/ekip-1.jpg" width="1200" height="564" alt="Uzman Akademi öğretmenleri ellerinde kitaplarla" fetchpriority="high">
      </div>
      <div class="hero-photo__badge">
        <span class="hero-photo__badge-icon">{ic("users")}</span>
        <span><b>30 şube</b><small>Binlerce öğrenci</small></span>
      </div>
    </div>
  </div>
</section>

<section class="quick-contact" aria-label="Hızlı iletişim">
  <div class="container">
    <div class="quick-contact__grid">
      <a class="qc-card qc-card--accent" href="tel:4443644">
        {ic("arrow-ur","qc-card__arrow")}
        <span class="qc-card__icon">{ic("phone")}</span>
        <span class="qc-card__label">Merkez telefon</span>
        <span class="qc-card__value">444 3 644</span>
        <span class="qc-card__sub">Tüm şubeler için tek numara</span>
      </a>
      <a class="qc-card" href="tel:+902125420076">
        {ic("arrow-ur","qc-card__arrow")}
        <span class="qc-card__icon">{ic("phone")}</span>
        <span class="qc-card__label">Sabit hat</span>
        <span class="qc-card__value">0212 542 0076</span>
        <span class="qc-card__sub">İstanbul merkez</span>
      </a>
      <a class="qc-card" href="mailto:info@uzmanakademi.com.tr">
        {ic("arrow-ur","qc-card__arrow")}
        <span class="qc-card__icon">{ic("mail")}</span>
        <span class="qc-card__label">Sorularınız için</span>
        <span class="qc-card__value qc-card__value--sm">info@<wbr>uzmanakademi.com.tr</span>
        <span class="qc-card__sub">E-posta adresimiz</span>
      </a>
      <div class="qc-card">
        <span class="qc-card__icon">{ic("clock")}</span>
        <span class="qc-card__label">Çalışma saatlerimiz</span>
        <span class="qc-card__value">09:00 – 19:00</span>
        <span class="qc-card__sub">Hafta içi ve hafta sonu</span>
      </div>
    </div>
  </div>
</section>

<section class="section" id="subeler" aria-labelledby="branches-title">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Adreslerimiz</span>
      <h2 class="section-title" id="branches-title">Şubelerimiz</h2>
      <p class="section-lead">Şubelerimiz il ve ilçelere göre listelenmiştir. İl, ilçe veya semt adıyla arayabilir; yol tarifi alabilir ya da şube sayfasını ziyaret edebilirsiniz.</p>
    </div>

    <div class="branches-toolbar">
      <label class="search">
        <span class="visually-hidden">Şube ara</span>
        {ic("search")}
        <input id="branch-search" type="search" placeholder="Şube, ilçe veya semt ara…" autocomplete="off">
      </label>
      <div class="chips" role="group" aria-label="Bölgeye göre filtrele">{chips}</div>
    </div>
    <p class="visually-hidden" id="branch-status" role="status" aria-live="polite"></p>

    <div data-branches>
{chr(10).join(groups)}
      <div class="empty-state">
        <strong>Bu aramaya uygun şube bulunamadı.</strong>
        Bulunduğunuz ilde şubemiz yoksa <b>canlı online kurslarımızla</b> tüm Türkiye’deyiz.
        <div style="margin-top:16px"><button class="btn btn--navy btn--sm" type="button" data-reset-filter>Tüm şubeleri göster</button></div>
      </div>
    </div>

    <div class="online-band reveal" style="margin-top:56px">
      <span class="online-band__icon">{ic("monitor")}</span>
      <div>
        <h3>Şubemiz size uzak mı? Canlı online derslerle evinizdesiniz.</h3>
        <p>Canlı online olarak tüm Türkiye’de hizmetinizdeyiz.</p>
      </div>
      <a class="btn" href="canli-online-kurslarimiz.html">Canlı Online Kurslarımız {ic("arrow")}</a>
    </div>
  </div>
</section>
""" + lead_section() + "\n</main>\n" + footer()

# ---------------------------------------------------------------- ANASAYFA
BENEFITS = [
 "Dakikada 2–3 kat daha hızlı okur.", "Kitap okuma alışkanlığı edinir.", "Ödev bilinci ve çalışma disiplini kazanır.",
 "Ödevlerini başkasına ihtiyaç duymadan yapar.", "Hayal gücü gelişir, düşünce ufku genişler.",
 "Kendi geleceğini planlayabilen bir birey haline gelir.", "Sınavlarda süre kontrolünü eline alır.",
 "Sınavlara sadece bilgiyle değil stratejiyle girer.", "Derslerine aktif katılım sağlar, okul başarısı yükselir.",
 "Okuduğunu iyi anlar, karmaşık metinlerde bile anlamı kaçırmaz.",
 "Zihinsel esneklik kazanır, problemleri farklı açılardan çözmeyi öğrenir.",
 "Kendine güveni artar, topluluk içinde kendini daha iyi ifade eder.",
 "Sorumluluk bilinci kazanır; sadece akademik değil, kişisel gelişimde de ilerler.",
 "Sadece bir kurs almış olmaz; düşünmeyi ve kendini tanımayı öğrenmiş olur.",
]
WHAT = ["Okuma ölçümü ile detaylı seviye analizi", "Kursiyer eğitim planlama ve hedef tespiti",
        "Kişiye özel hızlı okuma kurs programı", "Dikkat-odaklanma ve hafıza çalışmaları",
        "Sınavlarda stres, kaygı ve süre kontrolü", "Kişiye özel analiz, uzman psikolog desteği",
        "Kitap sevgisi ve okuma alışkanlığı edinme", "En az 3 kat hızlı okuma, %100 anlama oranı!"]
WHY = ["Anlık ölçümler ile öğrenci gelişim testleri", "Her yaşa özel farklı kurs programları",
       "Tümü formasyonlu Türkçe öğretmenleri", "Ücretsiz uzman psikolog desteği",
       "Profesyonel veli rehberlik hizmetleri", "Yapay zekâ destekli özel dijital sistem",
       "MEB onaylı hızlı okuma kurs programı", "%100 memnuniyet garantili eğitim!"]
NEWS = [
 ("trt-haber.jpg", 1000, 667, "Uzman Akademi TRT Haber’de"),
 ("temel-matematik.jpg", 700, 752, "Matematiği sevdirerek öğreten Temel Matematik dijital platformumuz çok yakında sizlerle!"),
 ("mezun-ogrenci.jpg", 700, 1244, "Öğrencimiz okuma hatalarına son vererek %100 anlama oranıyla mezun oldu!"),
 ("sosyal-sorumluluk.jpg", 700, 1244, "Sosyal sorumluluk projesi kapsamında yeni bir köy okulumuzla daha iş birliği yaptık."),
 ("level-up.jpg", 700, 887, "Sadece 12 derste sınav performansını artır! | Level Up – Uzman Akademi"),
 ("kayit-sureci.jpg", 700, 1244, "Başarıya uzanan bu yolculukta; hızlı okuma kurs sürecimizde sizleri neler bekliyor?"),
]
BLOG = [
 ("blog-kelime.jpg", "Mutfak masasında resimli kitap okurken kalemiyle bir kelimeyi gösterip düşünen çocuk ve ona gülümseyerek bakan annesi",
  "Bilmediği Kelimede Takılan Çocuk: Kelime Hazinesi Okuduğunu Anlamayı Nasıl Etkiler?", "blog-bilmedigi-kelimede-takilan-cocuk.html"),
 ("blog-sinav.jpg", "Sınavda soruyu dikkatle okuyan öğrencinin kalemle soru kitapçığını işaretlemesi",
  "Sınavda Soruyu Yanlış Okumak: Dikkatsizlik mi, Okuma Alışkanlığı mı?", "blog-sinavda-soruyu-yanlis-okumak.html"),
 ("blog-anne-cocuk.jpg", "Kitap okuyan anne ve çocuğu",
  "“Hızlı Okuyan Çocuk Okuduğunu Anlar mı?” Velilerin En Çok Sorduğu 7 Soru",
  "blog-hizli-okuyan-cocuk-okudugunu-anlar-mi.html"),
]
TESTI = [
 ("Meltem Orhanoğlu", "Güvenle teslim edebileceğiniz samimi, sıcak bir kurum. Öğretmenimizin samimiyeti okumaya teşvik ediyor. Hasan 89 kelime ile girdiği kurstan 534 kelime ile çıktı 🙏 Her şey için teşekkürler ❤️"),
 ("Semiha Gökküç", "Merhaba, hızlı okuma eğitimini hem kendim hem de 2. sınıfa geçen oğlum için aldık. Oğlum başlangıçta heceleyerek okuyordu ama kurs bitiminde akıcı okumaya geçtik ve artık kitap okumayı da seviyoruz. İlgileri için Melis Hanım ve Özge Hanım’a da çok teşekkür ederim. Kursa gitmeyi düşünüyorsanız tereddüt etmeden tercih edebilirsiniz."),
 ("Derya Kamberoğlu", "6. sınıf öğrencisi kızım için Özge Hanım’dan 12 derslik hızlı okuma dersleri aldık. Okuma hızımız ciddi derecede arttı. Çok memnun kaldık. Emekleri ve güler yüzü için Özge öğretmenimize çok teşekkür ederiz."),
 ("Özlem Çevik Gödekli", "Instagram’da gördüğüm paylaşımlar ile kurumla iletişime geçtim. Salgından dolayı online ve birebir dersi tercih ettik. Ben son derece memnun kaldım; gerçekten kurumsal, profesyonel yaklaşımla çalışıyorlar. Kızım Özce son derece severek derslerine katıldı, Yonca öğretmenimizi çok sevdi. İyi ki bireysel gelişimine katkıda bulunacak bu eğitimi tercih etmişiz."),
 ("Neslihan Aytekin", "8. sınıf öğrencisi kızım Mira, Yaren Hanım ile tamamladığı 6 haftalık çalışma sonrasında okuma hızını dakikada 130’dan 221’e çıkardı. Kurs, okuma hızı ve anlamadaki katkısı dışında dikkat konusunda da çok etkili oldu. Kızım artık sorularda çok daha az dikkat hatası yapıyor. Kurs süresince pozitif yaklaşımı ve enerjisiyle derslere katılımı daha da zevkli kılan Yaren Hanım’a katkılarından dolayı çok teşekkür ederiz."),
 ("Safiye Süne", "Uzman Akademi Maltepe şubesinde Elif öğretmenimizle karşılaştığımız için çok şanslıyız. 5. sınıfa giden kızım ve 3. sınıfa giden oğlum artık daha hızlı ve severek okuma yapıyorlar. En önemli katkısı da okuduklarını anlamada çok gelişme oldu 🙏 Elif öğretmenimizin karşılaması, samimiyeti ve disiplininden çok memnun kaldık. Öğretmenlerimizin emeğine sağlık 👏 Çok teşekkür ederiz."),
]
REFS = [("barolar-birligi","Türkiye Barolar Birliği"),("turk-metal","Türk Metal Sendikası"),("kartal-belediyesi","Kartal Belediyesi"),
        ("kamu-sen","Türkiye Kamu-Sen"),("kayseri-harb-is","Kayseri Harb-İş Yardımlaşma Derneği"),("turk-telekom-bys","Türk Telekom BYS")]

def initials(n):
    p = n.split()
    return (p[0][0] + p[-1][0]).upper()

def home_page():
    benefits = "\n".join(f'        <li><span>{i+1:02d}</span>{e(t)}</li>' for i, t in enumerate(BENEFITS))
    what = "\n".join(f'            <li>{ic("check-s")} {e(t)}</li>' for t in WHAT)
    why = "\n".join(f'            <li>{ic("check-s")} {e(t)}</li>' for t in WHY)
    news = "\n".join(f"""      <a class="news-card reveal" href="calismalarimiz.html">
        <div class="news-card__img"><img src="assets/img/{f}" width="{w}" height="{h}" loading="lazy" alt=""></div>
        <div class="news-card__body">{e(t)}</div>
      </a>""" for f, w, h, t in NEWS)
    blog = "\n".join(f"""      <a class="blog-card reveal" href="{u}">
        <div class="blog-card__img"><img src="assets/img/{f}" width="800" height="448" loading="lazy" alt="{e(a)}"></div>
        <div class="blog-card__body"><h3>{e(t)}</h3><span class="blog-card__more">Yazıyı oku {ic("arrow")}</span></div>
      </a>""" for f, a, t, u in BLOG)
    stars = ic("star") * 5
    testi = "\n".join(f"""      <figure class="t-card reveal">
        <div class="t-card__stars" aria-label="5 üzerinden 5 yıldız">{stars}</div>
        <p>{e(t)}</p>
        <footer><span class="t-card__avatar" aria-hidden="true">{initials(n)}</span><span class="t-card__who"><b>{e(n)}</b><small>Veli</small></span></footer>
      </figure>""" for n, t in TESTI)
    refs = "\n".join(f'      <div class="ref-logo"><img src="assets/img/referanslar/{f}.png" alt="{e(a)}" loading="lazy" width="150" height="150"></div>' for f, a in REFS)

    return head("Türkiye'nin En Büyük Hızlı Okuma Kursu | Uzman Akademi",
                "Uzman Akademi Hızlı Okuma Kursu: %100 anlama oranı ile okuma hızınız en az 3 kat artsın! 30 şube, binlerce öğrenci, MEB onaylı program, ücretsiz uzman psikolog desteği.",
                O) + org_jsonld() + "</head>\n<body>\n" + header("home") + f"""
<main id="icerik">

<section class="home-hero">
  <div class="container home-hero__grid">
    <div>
      <span class="home-hero__pill"><b>MEB ONAYLI</b> Hızlı Okuma Kursu · Okuma ve Anlama Eğitimi</span>
      <h1>%100 anlama oranı ile okuma hızınız en az <span class="hl">3 kat</span> artsın!</h1>
      <p class="home-hero__lead"><strong>30 şube, binlerce öğrenci</strong> — Türkiye’nin en büyük hızlı okuma kursu.</p>
      <div class="home-hero__actions">
        <a class="btn btn--primary" href="#bilgi-formu">Detaylı bilgi al {ic("arrow")}</a>
        <a class="btn btn--ghost" href="calismalarimiz.html" style="color:var(--navy-800)">Çalışmalarımız</a>
      </div>
      <div class="home-hero__stats">
        <div class="stat"><b>30</b><span>Şube</span></div>
        <div class="stat"><b>3×</b><span>Daha hızlı okuma</span></div>
        <div class="stat"><b>%100</b><span>Anlama oranı</span></div>
      </div>
    </div>
    <div class="home-hero__visual">
      <div class="home-hero__img"><img src="assets/img/ogretmen-tahta.jpg" width="900" height="1201" alt="Uzman Akademi sınıfında tahtada ders anlatan öğretmen ve öğrenci" fetchpriority="high"></div>
      <div class="float-card float-card--a"><span class="float-card__icon">{ic("award")}</span><span><b>2026 LGS</b>Türkiye birincisi</span></div>
      <div class="float-card float-card--b"><span class="float-card__icon">{ic("heart")}</span><span><b>Ücretsiz</b>Uzman psikolog desteği</span></div>
    </div>
  </div>
</section>

<section class="section benefits" aria-labelledby="benefits-title">
  <div class="container benefits__grid">
    <div class="benefits__aside reveal">
      <span class="eyebrow">Neden önemli?</span>
      <h2 class="section-title" id="benefits-title">Uzman Akademi ile öğrenci geleceğini inşa eder, çünkü:</h2>
      <p class="benefits__quote">Uzman Akademi, bir öğrenciyi sadece “başarılı” değil; <em>“özgüvenli, bilinçli ve güçlü”</em> bir birey haline getirir.</p>
    </div>
    <ul class="benefit-list reveal">
{benefits}
    </ul>
  </div>
</section>

<section class="section champion" aria-labelledby="champ-title">
  <div class="container champion__grid">
    <div class="champion__img reveal"><img src="assets/img/lgs-birincisi.jpg" width="900" height="1205" loading="lazy" alt="2026 LGS Türkiye birincisi Mücteba Yusuf Aksoy, elinde Uzman Akademi 1000 Soru kitabı"></div>
    <figure class="reveal" style="margin:0">
      <span class="eyebrow eyebrow--light" id="champ-title">2026 LGS Türkiye Birincisi</span>
      <blockquote>500 tam puan alarak LGS Türkiye birincisi oldum. Hızlı okuma ve anlama eğitimi sayesinde tek bir hata dahi yapmadım!</blockquote>
      <figcaption>
        <span><b>Mücteba Yusuf Aksoy</b><span>2026 LGS TÜRKİYE BİRİNCİSİ</span></span>
        <a class="btn btn--ghost-light btn--sm" href="{YT}" target="_blank" rel="noopener" style="margin-left:auto">{ic("play")} YouTube’da izle</a>
      </figcaption>
    </figure>
  </div>
</section>

<section class="section" aria-labelledby="what-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Eğitim yaklaşımımız</span>
      <h2 class="section-title" id="what-title">Ölçüyoruz, planlıyoruz, birlikte büyüyoruz</h2>
    </div>
    <div class="feature-pair">
      <article class="feature reveal">
        <div class="feature__img"><img src="assets/img/hero-sinif.jpg" width="1800" height="939" loading="lazy" alt="Uzman Akademi sınıfında öğretmen ve öğrenci birlikte çalışıyor"></div>
        <div class="feature__body">
          <h3>Neler yapıyoruz?</h3>
          <ul class="check-list">
{what}
          </ul>
          <a class="btn btn--navy" href="programlarimiz.html">Eğitim programlarımız {ic("arrow")}</a>
        </div>
      </article>
      <article class="feature reveal">
        <div class="feature__img"><img src="assets/img/ogretmen-ogrenci.jpg" width="1000" height="682" loading="lazy" alt="Öğretmen, öğrencisiyle birlikte kitap üzerinde çalışıyor"></div>
        <div class="feature__body">
          <h3>Neden Uzman Akademi?</h3>
          <ul class="check-list">
{why}
          </ul>
          <a class="btn btn--navy" href="referanslarimiz.html">Referanslarımız {ic("arrow")}</a>
        </div>
      </article>
    </div>
    <p class="reveal" style="text-align:center;margin-top:40px;font-size:18px;color:var(--ink-2)">
      <b style="color:var(--navy-900)">Öğretmenlerimizden kısa kısa…</b> Kadromuzla tanışmak ister misiniz?
      <a href="ogretmenlerimiz-cevapliyor.html" style="color:var(--orange-600);font-weight:700">Tıklayın →</a>
    </p>
  </div>
</section>

<section class="section programs" aria-labelledby="prog-title">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Programlarımız</span>
      <h2 class="section-title" id="prog-title">Her yaşa özel kurs programları</h2>
    </div>
    <div class="program-grid">
      <article class="program reveal">
        <span class="program__tag">LGS · YKS</span>
        <h3>Sınavlara yönelik hızlı okuma kursu</h3>
        <p>Günümüzde rekabetin artması ülke olarak sınav müfredatımızda değişikliğe gidilmesini zorunlu kılmıştır. Yeni nesil sınav sistemimizde artık başarıya ulaşmak; kısıtlı sürede bilgiyi çok iyi işlemeyi, okunan paragrafı bir kerede anlamayı, kısa sürede çeldirici sorular arasındaki bağlantıyı kurabilmeyi ve dikkat-odaklanma seviyesini maksimuma çıkartabilmeyi mecburiyet haline getirmiştir. Uzman Akademi Hızlı Okuma Kursu ile bunu başarabilirsiniz.</p>
        <span class="program__spacer"></span>
        <a class="btn btn--primary" href="programlarimiz.html">Daha fazla bilgi alın {ic("arrow")}</a>
      </article>
      <article class="program program--light reveal">
        <span class="program__tag">İlkokul · ODAK</span>
        <h3>İlkokul grubu okuma geliştirme kursu</h3>
        <p>İlkokul seviye öğrencilerimize özel olarak geliştirdiğimiz “Okuma Geliştirme ve Anlama” (ODAK) eğitim modelimiz ile okuma konusunda başarıyı garantilemekteyiz.</p>
        <p>“ODAK” eğitimi ile öğrencilerimizin kelime hatalarına, heceleme sorunlarına, hızlı, akıcı ve doğru okurken okuduklarını tam olarak anlamalarına, ayrıca dikkat ve algılarını maksimum seviyeye çıkartmalarına odaklanıyoruz. Uzman Akademi Hızlı Okuma Kursu ile okuma problemlerimizi çözebiliriz!</p>
        <span class="program__spacer"></span>
        <a class="btn btn--navy" href="programlarimiz.html">Daha fazla bilgi alın {ic("arrow")}</a>
      </article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="news-title">
  <div class="container">
    <div class="section-head reveal" style="display:flex;flex-wrap:wrap;gap:16px;align-items:end;justify-content:space-between;max-width:none">
      <div><span class="eyebrow">Çalışmalarımız</span><h2 class="section-title" id="news-title">Uzman Akademi’den haberler</h2></div>
      <a class="btn btn--ghost btn--sm" href="{IG}" target="_blank" rel="noopener" style="color:var(--navy-800)">{ic("ig")} #uzmanakademii</a>
    </div>
    <div class="news-grid">
      <a class="news-card reveal" href="{YT}" target="_blank" rel="noopener" style="background:var(--navy-800);color:#fff;justify-content:space-between;padding:24px">
        <span class="eyebrow eyebrow--light">Video</span>
        <span style="font-size:24px;font-weight:800;line-height:1.2;letter-spacing:-0.02em">Çocuğunuz başarısız değil, sadece okuduğunu anlamıyor!</span>
        <span class="blog-card__more" style="color:var(--orange-400)">{ic("play")} İzleyin</span>
      </a>
{news}
      <a class="news-card reveal" href="{YT}" target="_blank" rel="noopener" style="background:var(--orange-500);color:#fff;justify-content:space-between;padding:24px">
        <span class="eyebrow" style="color:#fff">Başarı hikâyesi</span>
        <span style="font-size:24px;font-weight:800;line-height:1.2;letter-spacing:-0.02em">Öğrencimizin okul başarısını ikiye katladık! Peki bunu nasıl başardık?</span>
        <span class="blog-card__more" style="color:#fff">{ic("play")} İzleyin</span>
      </a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="platform-title">
  <div class="container">
    <div class="platform-band reveal">
      <div>
        <span class="eyebrow eyebrow--light">Online interaktif dijital platform</span>
        <h2 id="platform-title">Uzman Akademi ile okuma hızın artsın, hafızan güçlensin</h2>
        <p>Uzman öğretmenlerimiz tarafından hazırlanmış, her yaşa uygun benzersiz hızlı okuma egzersizleri sizleri bekliyor.</p>
        <a class="btn btn--primary" href="{LOGIN}" target="_blank" rel="noopener">{ic("login")} Giriş için tıklayın</a>
      </div>
      <div class="platform-band__img"><img src="assets/img/okuma-hizi.jpg" width="700" height="1244" loading="lazy" alt="Eğitimlerimiz ile okuma hızın artsın, hafızan güçlensin — Uzman Akademi dijital platform tanıtımı"></div>
    </div>
  </div>
</section>

<section class="section programs" aria-labelledby="blog-title">
  <div class="container">
    <div class="section-head reveal" style="display:flex;flex-wrap:wrap;gap:16px;align-items:end;justify-content:space-between;max-width:none">
      <div><span class="eyebrow">Okuyalım Öğrenelim</span><h2 class="section-title" id="blog-title">Velilere rehber yazılar</h2></div>
      <a class="btn btn--navy btn--sm" href="okuyalim-ogrenelim.html">Tüm yazılarımız {ic("arrow")}</a>
    </div>
    <div class="blog-grid">
{blog}
    </div>

    <div class="online-band reveal" style="margin-top:48px;background:linear-gradient(120deg,var(--navy-800),var(--navy-600))">
      <span class="online-band__icon">{ic("music")}</span>
      <div>
        <h3>Harf şarkılarımız YouTube’da!</h3>
        <p>Çocuklara özel hazırladığımız harf şarkılarıyla sesleri birlikte keşfediyor, şarkılar söyleyerek öğrendiklerimizi tekrar ediyoruz. Birlikte söylediğiniz her şarkı, birlikte geçirdiğiniz keyifli bir öğrenme anına dönüşsün.</p>
      </div>
      <a class="btn" href="{YT}" target="_blank" rel="noopener">{ic("play")} Dinleyin</a>
    </div>
  </div>
</section>

<section class="section testimonials" aria-labelledby="t-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Veli yorumları</span>
      <h2 class="section-title" id="t-title">Velilerimiz ne diyor?</h2>
    </div>
    <div class="t-grid">
{testi}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ref-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Referanslarımız</span>
      <h2 class="section-title" id="ref-title">Anlaşmalı kurumlar</h2>
    </div>
    <div class="references-strip reveal">
{refs}
    </div>
  </div>
</section>
""" + lead_section() + "\n</main>\n" + footer()

with open(os.path.join(OUT, "iletisim.html"), "w", encoding="utf-8") as f:
    f.write(contact_page())
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_page())
print("ok", len(BR), "şube")

# ================================================================ İÇ SAYFALAR
import json, re
C = json.load(open(os.path.join(ROOT, "_build", "icerik.json"), encoding="utf-8"))
PG = C["pages"]
SIZES = C["imgsize"]
P["playtri"] = '<path d="M7 4v16l13-8z" fill="currentColor" stroke="none"/>'
P["calendar"] = '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'
P["user"] = '<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 14 0v1"/>'
P["target"] = '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'
P["bulb"] = '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>'
P["clipboard"] = '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>'
P["calc"] = '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01M16 18h.01"/>'


def T(page, i):
    return PG[page][i]


def dims(path):
    if path in SIZES:
        return SIZES[path]
    try:
        from PIL import Image
        with Image.open(os.path.join(ROOT, path)) as im:
            return list(im.size)
    except Exception:
        return None


def img(path, alt="", lazy=True, extra=""):
    d = dims(path)
    wh = f' width="{d[0]}" height="{d[1]}"' if d else ""
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{path}"{wh}{lz} alt="{e(alt)}"{extra}>'


def ps(*texts):
    return "\n".join(f"<p>{e(t)}</p>" for t in texts if t)


def write(fname, html_):
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html_)
    WRITTEN.append(fname)


WRITTEN = ["index.html", "iletisim.html"]


def page(fname, title, desc, active, body, canon=None, ld=""):
    canon = canon or (O + fname[:-5])
    html_ = (head(title, desc, canon) + ld + "</head>\n<body>\n" + header(active)
             + '\n<main id="icerik">\n' + body + "\n</main>\n" + footer())
    if 'id="bilgi-formu"' not in body:
        html_ = html_.replace('href="#bilgi-formu"', 'href="iletisim.html#bilgi-formu"')
    write(fname, html_)


def crumbs_html(crumbs):
    out = []
    for i, (lab, href) in enumerate(crumbs):
        if i:
            out.append(ic("right"))
        if href:
            out.append(f'<a href="{href}">{e(lab)}</a>')
        else:
            out.append(f'<span aria-current="page">{e(lab)}</span>')
    return " ".join(out)


def crumbs_ld(crumbs):
    items = []
    for i, (lab, href) in enumerate(crumbs, 1):
        it = {"@type": "ListItem", "position": i, "name": lab}
        if href:
            it["item"] = O + ("" if href == "index.html" else href[:-5])
        items.append(it)
    return ('<script type="application/ld+json">' + json.dumps(
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items},
        ensure_ascii=False) + "</script>\n")


def inner_hero(crumbs, eyebrow, title_html, lead="", image=None, alt="", actions="", meta=""):
    lead_h = f'<p class="page-hero__lead">{lead}</p>' if lead else ""
    act_h = f'<div class="page-hero__actions">{actions}</div>' if actions else ""
    meta_h = f'<div class="page-hero__meta">{meta}</div>' if meta else ""
    text = f"""    <div>
      <nav class="breadcrumb" aria-label="Sayfa yolu">{crumbs_html(crumbs)}</nav>
      <span class="eyebrow eyebrow--light">{eyebrow}</span>
      <h1>{title_html}</h1>
      {lead_h}
      {meta_h}
      {act_h}
    </div>"""
    if image:
        pic = f"""
    <div class="hero-photo">
      <div class="hero-photo__frame hero-photo__frame--photo">{img(image, alt, lazy=False)}</div>
    </div>"""
        return f"""<section class="page-hero page-hero--compact">
  <div class="container page-hero__grid">
{text}{pic}
  </div>
</section>
"""
    return f"""<section class="page-hero page-hero--compact">
  <div class="container" style="max-width:920px">
{text}
  </div>
</section>
"""


def tiles(items, cols="", numbered=False, icon="check-s", accent=False):
    out = []
    for i, it in enumerate(items, 1):
        t, d = (it if isinstance(it, tuple) else (it, ""))
        badge = f"{i:02d}" if numbered else ic(icon)
        dh = f"<p>{e(d)}</p>" if d else ""
        out.append(f'<div class="tile{" tile--accent" if accent else ""}"><span class="tile__icon">{badge}</span><h3>{e(t)}</h3>{dh}</div>')
    return f'<div class="tile-grid {cols} reveal">' + "".join(out) + "</div>"


def mini_list(items):
    return '<ul class="mini-list">' + "".join(f"<li>{ic('check')} {e(t)}</li>" for t in items) + "</ul>"


def section_head(eyebrow, title, lead="", center=False, tag="h2"):
    c = " section-head--center" if center else ""
    lh = f'<p class="section-lead">{lead}</p>' if lead else ""
    return f'<div class="section-head{c} reveal"><span class="eyebrow">{eyebrow}</span><{tag} class="section-title">{title}</{tag}>{lh}</div>'


def media(*figs):
    out = []
    for path, alt, cls in figs:
        out.append(f'<figure class="{cls}">{img(path, alt)}</figure>')
    return '<div class="split__media reveal">' + "".join(out) + "</div>"


def video_card(v, hidden=False):
    d = dims(v["img"]) or [1, 1]
    vertical = d[1] > d[0] * 1.2
    desc = f"<p>{e(v['desc'])}</p>" if v["desc"] and v["desc"] != v["title"] else ""
    return (f'<article class="video-card"{" hidden" if hidden else ""}>'
            f'<button class="video-card__thumb" type="button" data-yt="{v["yt"]}" data-title="{e(v["title"])}"{" data-vertical" if vertical else ""}>'
            f'{img(v["img"])}<span class="video-card__play"><span>{ic("playtri")}</span></span>'
            f'<span class="visually-hidden">Videoyu izle: {e(v["title"])}</span></button>'
            f'<div class="video-card__body"><h3>{e(v["title"])}</h3>{desc}</div></article>')


def video_grid(gid, videos, first=12):
    cards = "\n".join(video_card(v, i >= first) for i, v in enumerate(videos))
    more = ""
    if len(videos) > first:
        more = f'<div class="load-more"><button class="btn btn--navy" type="button" data-more="{gid}" data-step="12">Daha fazla göster</button></div>'
    return f'<div class="video-grid" id="{gid}">\n{cards}\n</div>{more}'


def cta_band(title, text, href, label, icon="phone", dark=False):
    style = ' style="background:linear-gradient(120deg,var(--navy-800),var(--navy-600))"' if dark else ""
    return f"""<div class="online-band reveal"{style}>
      <span class="online-band__icon">{ic(icon)}</span>
      <div><h3>{title}</h3><p>{text}</p></div>
      <a class="btn" href="{href}">{label} {ic("arrow")}</a>
    </div>"""


HOME = ("Anasayfa", "index.html")
KUR = ("Kurumsal", None)
PRG = ("Programlarımız", "programlarimiz.html")

# ---------------------------------------------------------------- Hakkımızda
def about_page():
    pg = "hakkimizda"
    first, rest = T(pg, 2).split(". ", 1)
    faq = []
    for i in range(15, 34, 2):
        q = re.sub(r"^\d+\.\s*", "", T(pg, i))
        faq.append(f"<details><summary>{e(q)}</summary><p>{e(T(pg, i + 1))}</p></details>")
    body = inner_hero([HOME, KUR, ("Hakkımızda", None)], "Hakkımızda",
                      "Okumayı sevdirmek için <em>bu yola çıktık…</em>", e(first + "."),
                      "assets/img/sayfa/hakkimizda-cocuk.jpg", "Kütüphanede kitap okuyan çocuk",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Detaylı bilgi al {ic("arrow")}</a><a class="btn btn--ghost-light" href="programlarimiz.html">Programlarımız</a>')
    body += f"""
<section class="section" style="padding-bottom:0">
  <div class="container">
    <div class="stat-band reveal">
      <div class="stat"><b>2011</b><span>Yola çıktığımız yıl</span></div>
      <div class="stat"><b>30</b><span>Şube ve canlı online eğitim</span></div>
      <div class="stat"><b>7 gün</b><span>Haftanın her günü açığız</span></div>
      <div class="stat"><b>%100</b><span>Anlama oranı ile okuma</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="prose reveal">
      <p class="lead-text">{e(re.split(r"(?<!vs)\. (?=[A-ZÇĞİÖŞÜ])", rest, maxsplit=1)[0])}.</p>
      {ps(re.split(r"(?<!vs)\. (?=[A-ZÇĞİÖŞÜ])", rest, maxsplit=1)[1])}
      <h3>Her yaş grubuna özel eğitim</h3>
      {ps(T(pg, 3))}
      <h3>Küçük yaş grupları için “Okuma ve Anlama”</h3>
      {ps(T(pg, 4))}
      <h3>Sınavlarda 30-40 dakika kazanın</h3>
      {ps(T(pg, 5))}
    </div>
    {media(("assets/img/sayfa/hakkimizda-kadin.jpg", "Kütüphanede kitap okuyan kadın", "is-wide"), ("assets/img/ekip-2.jpg", "Uzman Akademi öğretmeni öğrencileriyle", "is-wide"))}
  </div>
</section>

<section class="section section--white" aria-labelledby="sss">
  <div class="container">
    {section_head("Merak edilenler", "Sıkça Sorulan Sorular", center=True).replace('class="section-title"', 'class="section-title" id="sss"')}
    <div class="faq reveal">
      {"".join(faq)}
    </div>
  </div>
</section>
""" + lead_section()
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub(r"^\d+\.\s*", "", T(pg, i)),
         "acceptedAnswer": {"@type": "Answer", "text": T(pg, i + 1)}} for i in range(15, 34, 2)]}
    page("hakkimizda.html", "Hakkımızda | Uzman Akademi Hızlı Okuma Kursu",
         "2011'den bu yana okumayı sevdirmek için çalışan Uzman Akademi'yi tanıyın. Sıkça sorulan sorular: kurs süresi, sertifika, online eğitim, kayıt ve daha fazlası.",
         "about", body, ld=crumbs_ld([HOME, ("Hakkımızda", "hakkimizda.html")]) +
         '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + "</script>\n")


# ---------------------------------------------------------------- Programlarımız
def programs_page():
    pg = "programlarimiz"
    katki = [(T(pg, 29).rstrip(":"), T(pg, 30)), (T(pg, 31).rstrip(":"), T(pg, 32)),
             tuple(x.strip() for x in T(pg, 33).split(":", 1)), (T(pg, 34).rstrip(":"), T(pg, 35)),
             (T(pg, 36).rstrip(":"), T(pg, 37)), (T(pg, 38).rstrip(":"), T(pg, 39)), (T(pg, 40).rstrip(":"), T(pg, 41))]
    kazan = [tuple(x.strip() for x in T(pg, i).split(":", 1)) for i in range(55, 64)]
    sorun = []
    for i in range(70, 82, 2):
        t = T(pg, i).lstrip("✔ ").strip()
        if t.endswith("düşüklüğ"):
            t += "ü"
        sorun.append((t, T(pg, i + 1)))
    lists = [(T(pg, 82), [T(pg, i) for i in range(83, 88)]), (T(pg, 88), [T(pg, i) for i in range(89, 98)]),
             (T(pg, 98), [T(pg, i) for i in range(99, 105)])]
    lists_h = "".join(f'<div class="reveal"><h3 style="font-size:19px;color:var(--navy-900);margin-bottom:14px">{e(h)}</h3>{mini_list(items)}</div>' for h, items in lists)

    body = inner_hero([HOME, ("Programlarımız", None)], "Programlarımız",
                      "Başarı <em>uzman</em> işidir…",
                      "Sınav gruplarından ilkokula, okuma yazmadan temel matematiğe kadar her yaşa özel eğitim programlarımız.",
                      "assets/img/sayfa/program-okul.jpg", "Sınıfta öğretmen ve öğrenciler",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Detaylı bilgi al {ic("arrow")}</a>')
    body += f"""
<nav class="subnav" aria-label="Programlar">
  <div class="container">
    <a href="#sinav">Sınavlara yönelik</a>
    <a href="#ilkokul">İlkokul · ODAK</a>
    <a href="#okuma-yazma">Okuma Yazma</a>
    <a href="#temel-matematik">Temel Matematik</a>
    <a href="#odevlab">ÖdevLab</a>
    <a href="mental-aritmetik.html">Mental Aritmetik</a>
    <a href="canli-online-kurslarimiz.html">Canlı Online</a>
  </div>
</nav>

<section class="section">
  <div class="container">

    <article class="program-block" id="sinav">
      <div class="split">
        <div>
          <div class="program-block__head reveal"><span class="eyebrow">{e(T(pg, 2))}</span><h2 class="section-title">{e(T(pg, 3))}</h2></div>
          <div class="prose reveal">
            {ps(T(pg, 4))}
            <h3>{e(T(pg, 5))}</h3>
            {ps(T(pg, 6))}
            <h3>{e(T(pg, 7))}</h3>
            {ps(T(pg, 8))}
            <p style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn--navy btn--sm" href="lgs-gruplarina-yonelik-kurslarimiz.html" style="text-decoration:none;color:#fff">LGS grupları {ic("arrow")}</a><a class="btn btn--navy btn--sm" href="yks-gruplarina-yonelik-kurslarimiz.html" style="text-decoration:none;color:#fff">YKS grupları {ic("arrow")}</a></p>
          </div>
        </div>
        {media(("assets/img/sayfa/program-sinav.jpg", "Öğretmen sınav grubundaki öğrencisiyle birebir çalışıyor", "is-square"))}
      </div>
    </article>

    <article class="program-block" id="ilkokul">
      <div class="split split--rev">
        <div>
          <div class="program-block__head reveal"><span class="eyebrow">{e(T(pg, 9))}</span><h2 class="section-title">{e(T(pg, 10))}</h2></div>
          <div class="prose reveal">
            {ps(T(pg, 11) + " " + T(pg, 12))}
            <h3>{e(T(pg, 13))}</h3>
            {ps(T(pg, 14))}
            <p><a class="btn btn--navy btn--sm" href="kucuk-yas-okuma-anlama-kursu.html" style="text-decoration:none;color:#fff">İlkokul gruplarına yönelik kurslarımız {ic("arrow")}</a></p>
          </div>
        </div>
        {media(("assets/img/sayfa/program-birebir.jpg", "İlkokul öğrencisi öğretmeniyle birebir okuma çalışması yapıyor", ""))}
      </div>
    </article>

    <article class="program-block" id="okuma-yazma">
      <div class="split">
        <div>
          <div class="program-block__head reveal"><span class="eyebrow">İlkokul</span><h2 class="section-title">{e(T(pg, 15))}</h2></div>
          <div class="prose reveal">
            {ps(T(pg, 16))}
            <h3>{e(T(pg, 17))}</h3>
            <ul>{"".join(f"<li>{e(T(pg, i))}</li>" for i in range(18, 22))}</ul>
            {ps(T(pg, 22))}
            <h3>{e(T(pg, 23))}</h3>
            {ps(T(pg, 24), T(pg, 25), "Programımızda her öğrenci; oyun temelli etkinlikler, dikkat geliştirici çalışmalar ve motivasyonu yüksek sınıf ortamı sayesinde öğrenmeyi keyifli bir deneyim haline getirir.")}
          </div>
        </div>
        {media(("assets/img/sayfa/program-okuma-yazma.jpg", "Öğretmen ve öğrenci okuma yazma çalışmasında", ""))}
      </div>
      <h3 class="reveal" style="font-size:24px;color:var(--navy-900);margin:48px 0 20px">{e(T(pg, 28))}</h3>
      {tiles(katki, numbered=True)}
      <div class="split split--center" style="margin-top:40px">
        <div class="reveal"><h3 style="font-size:24px;color:var(--navy-900);margin-bottom:16px">{e(T(pg, 42))}</h3>{mini_list([T(pg, i) for i in range(43, 48)])}</div>
        <p class="note-card reveal">{e(T(pg, 48))}</p>
      </div>
    </article>

    <article class="program-block" id="temel-matematik">
      <div class="split split--rev">
        <div>
          <div class="program-block__head reveal"><span class="eyebrow">{e(T(pg, 51))} · {e(T(pg, 52))}</span><h2 class="section-title">{e(T(pg, 49))}</h2><p class="section-lead">{e(T(pg, 50))}</p></div>
          <div class="prose reveal">{ps(T(pg, 53))}</div>
        </div>
        {media(("assets/img/sayfa/program-matematik.jpg", "Öğretmen ve öğrenci sayı kartlarıyla matematik çalışıyor", "is-square"))}
      </div>
      <h3 class="reveal" style="font-size:24px;color:var(--navy-900);margin:48px 0 20px">{e(T(pg, 54))}</h3>
      {tiles(kazan, icon="calc", accent=True)}
    </article>

    <article class="program-block" id="odevlab">
      <div class="split">
        <div>
          <div class="program-block__head reveal"><span class="eyebrow">ÖdevLab · {e(T(pg, 65))}</span><h2 class="section-title">{e(T(pg, 66))}</h2></div>
          <div class="prose reveal">{ps(T(pg, 67) + " " + T(pg, 68))}</div>
        </div>
        {media(("assets/img/sayfa/program-odevlab.jpg", "Ödev atölyesinde çalışan öğrenciler", ""))}
      </div>
      <h3 class="reveal" style="font-size:24px;color:var(--navy-900);margin:48px 0 20px">{e(T(pg, 69))}</h3>
      {tiles(sorun, icon="check-s")}
      <div class="tile-grid" style="margin-top:40px;align-items:start">{lists_h}</div>
      <p class="note-card reveal" style="margin-top:32px;text-align:center;font-size:18px"><b>{e(T(pg, 105))}</b></p>
    </article>

  </div>
</section>
""" + lead_section()
    page("programlarimiz.html", "Programlarımız | Uzman Akademi Hızlı Okuma Kursu",
         "Sınavlara yönelik hızlı okuma, ilkokul ODAK okuma anlama, okuma yazma, temel matematik ve ÖdevLab programları. Her yaşa özel eğitim.",
         "programs", body, ld=crumbs_ld([HOME, ("Programlarımız", "programlarimiz.html")]))


# ---------------------------------------------------------------- İlkokul
def primary_page():
    pg = "kucuk-yas-okuma-anlama-kursu"
    q = T(pg, 23)
    quote, author = q.rsplit("”", 1)
    body = inner_hero([HOME, PRG, ("İlkokul grupları", None)], e(T(pg, 5)),
                      "Küçük yaş gruplarına özel <em>“ODAK”</em> eğitim modeli", e(T(pg, 6)),
                      "assets/img/sayfa/ilkokul-1.jpg", "Öğretmen ilkokul öğrencisine bilgisayarda okuma egzersizi yaptırıyor",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Ücretsiz bilgi al {ic("arrow")}</a>')
    body += f"""
<section class="section">
  <div class="container split">
    <div class="prose reveal">
      {ps(T(pg, 8), T(pg, 9))}
    </div>
    {media(("assets/img/sayfa/ilkokul-2.jpg", "Öğretmen ilkokul öğrencisiyle birebir kitap okuyor", ""))}
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow eyebrow--light">ODAK eğitimi</span><h2 class="section-title">{e(T(pg, 10))}</h2><p class="section-lead">{e(T(pg, 11))}</p></div>
    <p class="note-card reveal" style="margin-bottom:32px;background:rgba(245,135,31,.14);border-color:rgba(245,135,31,.35);color:#fff">{ic("info", "icon")} B{e(T(pg, 12))}</p>
    <h3 class="reveal" style="font-size:20px;margin-bottom:18px">{e(T(pg, 13))}</h3>
    {tiles([T(pg, i) for i in range(14, 22)], cols="tile-grid--4", numbered=True)}
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:860px">
    <div class="prose reveal">{ps(T(pg, 22))}</div>
    <blockquote class="pull-quote reveal" style="margin-top:28px">{e(quote)}”<cite>{e(author.strip())}</cite></blockquote>
  </div>
</section>
""" + lead_section()
    page("kucuk-yas-okuma-anlama-kursu.html", "İlkokul Okuma Anlama Kursu (ODAK) | Uzman Akademi",
         "İlkokul gruplarına özel ODAK okuma geliştirme ve anlama eğitimi: hecelemeden akıcı okuma, %100 anlama, dikkat ve odaklanma. 10 saatlik birebir özel ders paketi.",
         "programs", body, ld=crumbs_ld([HOME, ("Programlarımız", "programlarimiz.html"), ("İlkokul grupları", "kucuk-yas-okuma-anlama-kursu.html")]))


# ---------------------------------------------------------------- LGS
def lgs_page():
    pg = "lgs-gruplarina-yonelik-kurslarimiz"
    points = [T(pg, i).lstrip("- ").strip() for i in (12, 13, 14)]
    titles = ["Okuduğunu anlama", "Dikkat ve odaklanma", "Zaman yönetimi"]
    body = inner_hero([HOME, PRG, ("LGS grupları", None)], e(T(pg, 5)),
                      "Sınavlarda <em>bir adım önde</em> olun", e(T(pg, 6)),
                      "assets/img/sayfa/lgs-1.jpg", "LGS grubu öğrencileri sınıfta hızlı okuma dersinde",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Ücretsiz ölçüm için bilgi al {ic("arrow")}</a>')
    body += f"""
<section class="section">
  <div class="container split">
    <div class="prose reveal">
      {ps(T(pg, 8))}
      <p class="lead-text">{e(T(pg, 9))}</p>
      {ps(T(pg, 10))}
    </div>
    {media(("assets/img/sayfa/lgs-2.jpg", "Öğrenci birebir hızlı okuma özel dersinde", ""))}
  </div>
</section>

<section class="section section--white">
  <div class="container">
    {section_head("Paragraf soruları", e(T(pg, 11)))}
    {tiles(list(zip(titles, points)), icon="target", accent=True)}
    <div class="prose reveal" style="max-width:860px;margin-top:40px">{ps(T(pg, 15), T(pg, 16))}</div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:960px">
    <p class="note-card reveal" style="font-weight:500;font-size:16.5px;line-height:1.7">{e(T(pg, 17))}</p>
  </div>
</section>
""" + lead_section()
    page("lgs-gruplarina-yonelik-kurslarimiz.html", "LGS Gruplarına Yönelik Hızlı Okuma Kursu | Uzman Akademi",
         "LGS'ye hazırlanan öğrencilere özel hızlı okuma ve anlama teknikleri: sınavlarda 35-40 dakika kazanın, paragraf sorularında dikkat ve zaman yönetimi.",
         "programs", body, ld=crumbs_ld([HOME, ("Programlarımız", "programlarimiz.html"), ("LGS grupları", "lgs-gruplarina-yonelik-kurslarimiz.html")]))


# ---------------------------------------------------------------- YKS
def yks_page():
    pg = "yks-gruplarina-yonelik-kurslarimiz"
    body = inner_hero([HOME, PRG, ("YKS grupları", None)], e(T(pg, 5)),
                      "Sınavlarda zamanı <em>siz yönetin!</em>", e(T(pg, 6)),
                      "assets/img/sayfa/yks-1.jpg", "YKS grubu öğrencisi öğretmeniyle çalışıyor",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Detaylı bilgi al {ic("arrow")}</a>')
    body += f"""
<section class="section">
  <div class="container split">
    <div class="prose reveal">
      <p class="lead-text">{e(T(pg, 8))}</p>
      {ps(T(pg, 9), T(pg, 10))}
    </div>
    {media(("assets/img/sayfa/yks-2.jpg", "Sertifika alan Uzman Akademi öğrencileri", ""))}
  </div>
</section>

<section class="section section--white">
  <div class="container" style="max-width:860px">
    {section_head("Benzersiz teknikler", e(T(pg, 11)))}
    <div class="prose reveal">
      {ps(T(pg, 12))}
      <blockquote class="pull-quote">{e(T(pg, 13))}</blockquote>
      {ps(T(pg, 14), T(pg, 15))}
      <blockquote class="pull-quote">{e(T(pg, 16))}</blockquote>
      <p class="note-card">{e(T(pg, 17))}</p>
    </div>
  </div>
</section>
""" + lead_section()
    page("yks-gruplarina-yonelik-kurslarimiz.html", "YKS Gruplarına Yönelik Hızlı Okuma Kursu | Uzman Akademi",
         "YKS'ye hazırlanan öğrencilere anlayarak hızlı okuma: yeni nesil sorularda zaman yönetimi, sınavlarda ekstra 30-40 dakika, dikkat ve odaklanma.",
         "programs", body, ld=crumbs_ld([HOME, ("Programlarımız", "programlarimiz.html"), ("YKS grupları", "yks-gruplarina-yonelik-kurslarimiz.html")]))


# ---------------------------------------------------------------- Canlı online
def online_page():
    pg = "canli-online-kurslarimiz"
    body = inner_hero([HOME, PRG, ("Canlı Online Kurslarımız", None)], e(T(pg, 5)),
                      "Online eğitimden <em>çok daha fazlası…</em>", e(T(pg, 6)),
                      "assets/img/sayfa/online-2.jpg", "Öğretmen canlı online hızlı okuma dersi veriyor",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Online kurs için bilgi al {ic("arrow")}</a>')
    body += f"""
<section class="section">
  <div class="container split">
    <div class="prose reveal">
      <p class="lead-text">{e(T(pg, 8))}</p>
      {ps(*[x for x in PG[pg][9:10]])}
    </div>
    {media(("assets/img/sayfa/online-1.jpg", "Öğrenci evden canlı online derse katılıyor", ""))}
  </div>
</section>

<section class="section section--white">
  <div class="container" style="max-width:860px">
    {section_head("Fark", e(T(pg, 10)))}
    <div class="prose reveal">{ps(T(pg, 11), T(pg, 12))}</div>
    <blockquote class="pull-quote reveal" style="margin-top:32px">{e(T(pg, 13))}<cite>{e(T(pg, 14))}</cite></blockquote>
  </div>
</section>
""" + lead_section()
    page("canli-online-kurslarimiz.html", "Canlı Online Hızlı Okuma Kursu | Uzman Akademi",
         "Yüz yüze eğitimlerimizle aynı müfredat, uzman öğretmenler ve 5-6 kişilik gruplarla tüm Türkiye'de canlı online hızlı okuma ve anlama eğitimi.",
         "programs", body, ld=crumbs_ld([HOME, ("Programlarımız", "programlarimiz.html"), ("Canlı Online Kurslarımız", "canli-online-kurslarimiz.html")]))


# ---------------------------------------------------------------- Mental aritmetik
def mental_page():
    pg = "mental-aritmetik"
    vids = C["mental_videos"]
    traits = [T(pg, i).replace("berecileri", "becerileri") for i in range(17, 23)]

    def embed(vid, title):
        return (f'<div class="video-embed video-embed--vertical reveal"><button class="video-card__thumb" type="button" data-yt="{vid}" data-inline data-title="{e(title)}">'
                f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">'
                f'<span class="video-card__play"><span>{ic("playtri")}</span></span><span class="visually-hidden">Videoyu oynat: {e(title)}</span></button></div>')

    body = inner_hero([HOME, PRG, ("Mental Aritmetik", None)], e(T(pg, 1)),
                      "Minik <em>dahiler</em> okulu", e(T(pg, 4)),
                      "assets/img/sayfa/mental-4.jpg", "Halkalı şubesinde mental aritmetik grubu",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Detaylı bilgi al {ic("arrow")}</a>',
                      meta=f'<span>{ic("users")} 4-12 yaş</span><span>{ic("award")} {e(T(pg, 3))}</span>')
    body += f"""
<section class="section">
  <div class="container split split--center">
    <div class="prose reveal">
      <h2>{e(T(pg, 5))}</h2>
      <p class="lead-text">{e(T(pg, 6))}</p>
      {ps(T(pg, 15), T(pg, 16))}
    </div>
    <div style="display:grid;gap:16px">{embed(vids[0], "Mental Aritmetik tanıtım videosu")}</div>
  </div>
</section>

<section class="section section--white">
  <div class="container split">
    <div>
      <div class="section-head reveal"><span class="eyebrow">{e(T(pg, 29))}</span><h2 class="section-title">{e(T(pg, 30))}</h2></div>
      <div class="prose reveal">{ps(T(pg, 31))}<p class="lead-text">{e(T(pg, 32))}</p></div>
    </div>
    <div class="reveal">
      {mini_list(traits)}
      <p style="margin-top:14px;font-weight:700;color:var(--orange-600);font-size:18px">…{e(T(pg, 23))}</p>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container split split--center">
    <div class="reveal">
      <span class="eyebrow eyebrow--light">Şubelerimizde</span>
      <h2 class="section-title" style="margin-top:12px">{e(T(pg, 25))}</h2>
      <p class="section-lead">{e(T(pg, 24))}</p>
      <p class="section-lead">{e(T(pg, 26))}</p>
      <p class="section-lead">{e(T(pg, 27) + " " + T(pg, 28))}</p>
    </div>
    {embed(vids[1], "Mental Aritmetik ders videosu")}
  </div>
</section>

<section class="section" style="padding-bottom:0">
  <div class="container">
    <div class="work-grid">
      <figure class="work-card reveal" style="margin:0"><div class="work-card__img">{img("assets/img/sayfa/mental-1.jpg", "Tahtada matematik işlemi yapan kız çocuğu")}</div></figure>
      <figure class="work-card reveal" style="margin:0"><div class="work-card__img">{img("assets/img/sayfa/mental-2.jpg", "Kâğıt üzerinde matematik formülleri")}</div></figure>
      <figure class="work-card reveal" style="margin:0"><div class="work-card__img">{img("assets/img/sayfa/mental-3.jpg", "Sınıfta tahtaya bakan öğrenciler")}</div></figure>
    </div>
    <div style="margin-top:40px">{cta_band("Ayrıca hızlı okuma kurslarımızı ziyaret edebilirsiniz", "Her yaşa özel hızlı okuma ve anlama programlarımızı inceleyin.", "programlarimiz.html", "Programlarımız", icon="book", dark=True)}</div>
  </div>
</section>
""" + lead_section()
    page("mental-aritmetik.html", "Mental Aritmetik Kursu (4-12 Yaş) | Uzman Akademi",
         "Abaküs mental aritmetik eğitimi ile 4-12 yaş çocuklar karmaşık işlemleri zihinden, saniyeler içinde yapmayı öğrenir. Dikkat, hafıza ve özgüven gelişimi.",
         "programs", body, ld=crumbs_ld([HOME, ("Programlarımız", "programlarimiz.html"), ("Mental Aritmetik", "mental-aritmetik.html")]))


# ---------------------------------------------------------------- Çalışmalarımız
def works_page():
    pg = "calismalarimiz"
    cards = [
        (T(pg, 2), T(pg, 3), "kucuk-yas-okuma-anlama-kursu.html", "assets/img/sayfa/calisma-bireysel.jpg", "Bireysel hızlı okuma eğitimi"),
        (T(pg, 5), T(pg, 6), "lgs-gruplarina-yonelik-kurslarimiz.html", "assets/img/sayfa/calisma-grup.jpg", "Hızlı okuma grup eğitimi"),
        (T(pg, 8), T(pg, 9), "yks-gruplarina-yonelik-kurslarimiz.html", "assets/img/sayfa/calisma-sinav.jpg", "Sınavlara yönelik bireysel ders"),
        (T(pg, 11), T(pg, 12), "canli-online-kurslarimiz.html", "assets/img/sayfa/calisma-online.jpg", "Uzman Akademi online eğitim"),
        (T(pg, 14), T(pg, 15), "#bilgi-formu", "assets/img/sayfa/calisma-birebir.jpg", "Bireysel eğitim"),
        (T(pg, 16), T(pg, 17), "referanslarimiz.html", "assets/img/sayfa/calisma-mezun.jpg", "Sertifikalarıyla mezun öğrencilerimiz"),
    ]
    more = ["Daha fazla bilgi al"] * 4 + ["Bilgi al", "Referanslarımız"]
    cards_h = "\n".join(f"""      <a class="work-card reveal" href="{href}">
        <div class="work-card__img">{img(im, alt)}</div>
        <div class="work-card__body"><h3>{e(t)}</h3><p>{e(d)}</p><span class="blog-card__more">{m} {ic("arrow")}</span></div>
      </a>""" for (t, d, href, im, alt), m in zip(cards, more))
    steps = "".join(f'<div class="step reveal">{e(T(pg, i))}</div>' for i in range(19, 25))
    body = inner_hero([HOME, KUR, ("Çalışmalarımız", None)], "Çalışmalarımız",
                      "Çalışmalarımızdan <em>kısa kısa…</em>",
                      "İlkokuldan üniversite hazırlığa, yüz yüze ve canlı online; her ihtiyaca özel hızlı okuma çalışmalarımız.",
                      "assets/img/hero-sinif.jpg", "Uzman Akademi sınıfında öğretmen ve öğrenci")
    body += f"""
<section class="section">
  <div class="container">
    <div class="work-grid">
{cards_h}
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow eyebrow--light">Nasıl çalışıyoruz?</span><h2 class="section-title">{e(T(pg, 18))}</h2></div>
    <div class="steps">{steps}</div>
  </div>
</section>
""" + lead_section()
    page("calismalarimiz.html", "Çalışmalarımız | Uzman Akademi Hızlı Okuma Kursu",
         "İlkokul okuma anlama, LGS ve YKS grupları, canlı online ve bireysel hızlı okuma kurslarımız. Ücretsiz okuma ölçümü ve %100 anlama oranı garantisi.",
         "about", body, ld=crumbs_ld([HOME, ("Çalışmalarımız", "calismalarimiz.html")]))


# ---------------------------------------------------------------- Referanslar
def refs_page():
    stars = ic("star") * 5
    testi = "\n".join(f"""      <figure class="t-card reveal">
        <div class="t-card__stars" aria-label="5 üzerinden 5 yıldız">{stars}</div>
        <p>{e(t)}</p>
        <footer><span class="t-card__avatar" aria-hidden="true">{initials(n)}</span><span class="t-card__who"><b>{e(n)}</b><small>Veli</small></span></footer>
      </figure>""" for n, t in TESTI)
    refs = "\n".join(f'      <div class="ref-logo"><img src="assets/img/referanslar/{f}.png" alt="{e(a)}" loading="lazy" width="150" height="150"></div>' for f, a in REFS)
    body = inner_hero([HOME, KUR, ("Referanslarımız", None)], "Veli ve kursiyer yorumlarımız",
                      "Onlar bizlere güvendi. <em>Şimdi sıra sizde!</em>",
                      "Veli ve öğrencilerimiz almış oldukları eğitimi değerlendiriyor…",
                      actions=f'<a class="btn btn--primary" href="#bilgi-formu">Detaylı bilgi al {ic("arrow")}</a><a class="btn btn--ghost-light" href="#yorumlar">Veli yorumları</a>')
    body += f"""
<section class="section">
  <div class="container">
    {section_head("Başarı hikâyeleri", "Öğrencilerimiz ve velilerimiz anlatıyor", "Videoya tıklayarak izleyebilirsiniz.")}
    {video_grid("ref-videolar", C["reference_videos"])}
  </div>
</section>

<section class="section testimonials" id="yorumlar">
  <div class="container">
    {section_head("Veli yorumları", "Velilerimiz ne diyor?", center=True)}
    <div class="t-grid">
{testi}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Kurumsal", "Anlaşmalı kurumlar", center=True)}
    <div class="references-strip reveal">
{refs}
    </div>
  </div>
</section>
""" + lead_section()
    page("referanslarimiz.html", "Referanslarımız ve Veli Yorumları | Uzman Akademi",
         "Uzman Akademi öğrencilerinin başarı hikâyeleri, veli ve kursiyer yorumları, hızlı okuma Türkiye dereceleri ve anlaşmalı kurumlarımız.",
         "about", body, ld=crumbs_ld([HOME, ("Referanslarımız", "referanslarimiz.html")]))


# ---------------------------------------------------------------- Öğretmenlerimiz
def teachers_page():
    body = inner_hero([HOME, KUR, ("Öğretmenlerimiz", None)], "Öğretmenlerimizden kısa kısa…",
                      "Benzersiz ve geniş <em>uzman kadro</em>",
                      "Uzman öğretmenlerimiz sizler için cevaplıyor… Tüm öğretmenlerimiz Türkçe, Edebiyat ve Sınıf Öğretmenliği branşlarında uzman olup gerekli pedagojik formasyonlara sahiptir.",
                      "assets/img/ekip-1.jpg", "Uzman Akademi öğretmenleri ellerinde kitaplarla",
                      actions=f'<a class="btn btn--primary" href="#videolar">Videoları izle {ic("arrow")}</a>')
    body += f"""
<section class="section" id="videolar">
  <div class="container">
    {section_head("Soru-cevap", "Öğretmenlerimiz cevaplıyor", "Hızlı okuma, dikkat ve odaklanma, ODAK programı ve sınav başarısı hakkında en çok merak edilenler.")}
    {video_grid("ogretmen-videolar", C["teacher_videos"])}
  </div>
</section>
""" + lead_section()
    page("ogretmenlerimiz-cevapliyor.html", "Öğretmenlerimiz Cevaplıyor | Uzman Akademi",
         "Uzman Akademi öğretmenleri hızlı okuma, anlama, dikkat ve odaklanma, ilkokul ODAK programı ve sınav başarısı hakkındaki soruları videolarla yanıtlıyor.",
         "about", body, ld=crumbs_ld([HOME, ("Öğretmenlerimiz", "ogretmenlerimiz-cevapliyor.html")]))


# ---------------------------------------------------------------- Blog
POSTS = [
    {"file": "blog-bilmedigi-kelimede-takilan-cocuk.html", "img": "assets/img/blog-kelime.jpg",
     "alt": BLOG[0][1], "canon": O + "post/bilmedigi-kelimede-takilan-cocuk"},
    {"file": "blog-sinavda-soruyu-yanlis-okumak.html", "img": "assets/img/blog-sinav.jpg",
     "alt": BLOG[1][1], "canon": O + "post/sinavda-soruyu-yanlis-okumak"},
    {"file": "blog-hizli-okuyan-cocuk-okudugunu-anlar-mi.html", "img": "assets/img/blog-anne-cocuk.jpg",
     "alt": BLOG[2][1], "canon": O + "post/" + urllib.parse.quote("hızlı-okuyan-çocuk-okuduğunu-anlar-mı-velilerin-en-çok-sorduğu-7-soru")},
    {"file": "blog-okula-uyum-surecini-kolaylastirmanin-7-etkili-yolu.html", "img": "assets/img/sayfa/blog-okula-uyum.jpg",
     "alt": "Okula birlikte yürüyen anne, baba ve çocuk illüstrasyonu", "canon": O + "post/" + urllib.parse.quote("okula-uyum-sürecini-kolaylaştırmanın-7-etkili-yolu")},
]
for pmeta, pdata in zip(POSTS, C["posts"]):
    pmeta.update(pdata)
    pmeta["title"] = pmeta["title"].strip()
    pmeta["read"] = pmeta["meta"][1] if len(pmeta["meta"]) > 1 else ""
    lines = PG["okuyalim-ogrenelim"]
    idx = lines.index(pmeta["title"]) if pmeta["title"] in lines else -1
    ex = lines[idx + 1] if idx >= 0 else ""
    if len(ex) > 230:
        ex = ex[:230].rsplit(" ", 1)[0] + "…"
    pmeta["excerpt"] = ex


def post_blocks(p):
    blocks = p["blocks"]
    out, ul = [], []
    def flush():
        if ul:
            out.append("<ul>" + "".join(f"<li>{e(x)}</li>" for x in ul) + "</ul>")
            ul.clear()
    skip = False
    for kind, text, *_ in blocks:
        if kind == "h3" and text.strip() == "İlgili yazılar":
            skip = True
        if skip:
            continue
        if kind == "li":
            ul.append(text)
            continue
        if kind == "p" and text.startswith("- "):
            ul.append(text[2:])
            continue
        flush()
        if kind in ("h2", "h3"):
            out.append(f"<{kind}>{e(text)}</{kind}>")
        elif kind == "p" and re.match(r"^\d\. [^.]{5,80}$", text):
            out.append(f"<h2>{e(text)}</h2>")
        elif kind == "p" and text == "Okula Uyum Süreciyle İlgili Sık Sorulan Sorular":
            out.append(f"<h2>{e(text)}</h2>")
        elif kind == "p" and text.endswith("?") and len(text) < 80 and p["file"].startswith("blog-okula"):
            out.append(f"<h3>{e(text)}</h3>")
        elif kind == "p" and text.startswith("Uzman Notu:"):
            out.append(f'<p class="note-card"><b>Uzman Notu:</b>{e(text[len("Uzman Notu:"):])}</p>')
        else:
            out.append(f"<p>{e(text)}</p>")
    flush()
    return "\n".join(out)


def post_card(p, featured=False):
    cls = "blog-card reveal" + (" blog-card--featured" if featured else "")
    tag = "h2" if featured else "h3"
    return f"""      <a class="{cls}" href="{p['file']}">
        <div class="blog-card__img">{img(p['img'], p['alt'])}</div>
        <div class="blog-card__body">
          <div class="blog-card__meta"><span>{ic("user")} Uzman Akademi</span><span>{ic("clock")} {e(p['read'])}</span></div>
          <{tag} style="font-size:{'clamp(22px,2.6vw,30px)' if featured else '19px'};color:var(--navy-900);line-height:1.3">{e(p['title'])}</{tag}>
          <p class="blog-card__excerpt">{e(p['excerpt'])}</p>
          <span class="blog-card__more">Yazıyı oku {ic("arrow")}</span>
        </div>
      </a>"""


def blog_pages():
    body = inner_hero([HOME, ("Okuyalım Öğrenelim", None)], "Uzmanlar yazıyor",
                      "Okuyalım <em>Öğrenelim</em>",
                      "Öğretmenlerimizden velilere ve öğrencilere okuma, anlama ve sınav başarısı üzerine rehber yazılar.")
    cards = post_card(POSTS[0], True) + "\n" + "\n".join(post_card(p) for p in POSTS[1:])
    body += f"""
<section class="section">
  <div class="container">
    <div class="post-grid">
{cards}
    </div>
    <div style="margin-top:56px">{cta_band("Harf şarkılarımız YouTube’da!", "Çocuklara özel hazırladığımız harf şarkılarıyla sesleri birlikte keşfediyoruz.", YT, "YouTube kanalımız", icon="music", dark=True).replace('href="' + YT + '"', 'href="' + YT + '" target="_blank" rel="noopener"')}</div>
  </div>
</section>
""" + lead_section()
    page("okuyalim-ogrenelim.html", "Okuyalım Öğrenelim — Uzmanlar Yazıyor | Uzman Akademi",
         "Uzman Akademi öğretmenlerinden okuma, anlama, kelime hazinesi, sınav başarısı ve okula uyum üzerine velilere rehber yazılar.",
         "blog", body, ld=crumbs_ld([HOME, ("Okuyalım Öğrenelim", "okuyalim-ogrenelim.html")]))

    for p in POSTS:
        others = [x for x in POSTS if x is not p][:3]
        other_h = "\n".join(post_card(x) for x in others)
        body = inner_hero([HOME, ("Okuyalım Öğrenelim", "okuyalim-ogrenelim.html"), (p["title"], None)],
                          "Okuyalım Öğrenelim", e(p["title"]),
                          meta=f'<span>{ic("user")} Uzman Akademi</span><span>{ic("clock")} {e(p["read"])}</span>')
        body += f"""
<section class="section">
  <article class="container article">
    <figure class="article__cover">{img(p['img'], p['alt'], lazy=False)}</figure>
    <div class="prose">
{post_blocks(p)}
    </div>
    <div class="article-cta">
      <div><h3>Çocuğunuzun okuma düzeyini öğrenin</h3><p>Ücretsiz okuma ölçümü için öğretmenlerimizden bilgi alın.</p></div>
      <div style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn--primary" href="#bilgi-formu">Bilgi al</a><a class="btn btn--ghost-light" href="tel:4443644">{ic("phone")} 444 3 644</a></div>
    </div>
  </article>
</section>

<section class="section section--tint">
  <div class="container">
    {section_head("Okumaya devam edin", "Diğer yazılarımız")}
    <div class="blog-grid">
{other_h}
    </div>
  </div>
</section>
""" + lead_section()
        art_ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
                  "image": p["img"], "author": {"@type": "Organization", "name": "Uzman Akademi"},
                  "publisher": {"@type": "Organization", "name": "Uzman Akademi"}}
        desc = p["excerpt"] if len(p["excerpt"]) < 200 else p["excerpt"][:190].rsplit(" ", 1)[0] + "…"
        page(p["file"], p["title"] + " | Uzman Akademi", desc, "blog", body, canon=p["canon"],
             ld=crumbs_ld([HOME, ("Okuyalım Öğrenelim", "okuyalim-ogrenelim.html"), (p["title"], p["file"])]) +
             '<script type="application/ld+json">' + json.dumps(art_ld, ensure_ascii=False) + "</script>\n")


# ---------------------------------------------------------------- Gizlilik
def privacy_page():
    pg = "gizlilik-politikasi"
    L = PG[pg]
    heads = {6, 8, 10, 17, 20, 22, 24, 26}
    out = []
    i = 2
    while i < len(L):
        t = L[i]
        if i == 2:
            out.append(f"<p class=\"lead-text\">{e(t + ' ' + L[3])}</p>"); i = 4; continue
        if i in heads:
            out.append(f"<h2>{e(t)}</h2>")
        elif 12 <= i <= 16:
            out.append("<ul>" + "".join(f"<li>{e(L[j])}</li>" for j in range(12, 17)) + "</ul>"); i = 17; continue
        elif i == 28:
            out.append(f'<p>{e(t.replace("info@uzmanakademi.com.tr", "").strip())} <a href="mailto:info@uzmanakademi.com.tr">info@uzmanakademi.com.tr</a> {e(L[29])}</p>'); i = 30; continue
        elif i == 30:
            out.append(f'<p style="font-size:14px;color:var(--ink-3)">{e(t)}</p>')
        else:
            out.append(f"<p>{e(t)}</p>")
        i += 1
    body = inner_hero([HOME, ("Gizlilik Politikamız", None)], "Gizlilik Politikamız",
                      "Hizmet koşulları ve <em>gizlilik politikası</em>")
    body += f"""
<section class="section">
  <div class="container article">
    <div class="prose">
{chr(10).join(out)}
    </div>
  </div>
</section>
"""
    page("gizlilik-politikasi.html", "Gizlilik Politikası | Uzman Akademi",
         "Uzman Akademi hizmet koşulları ve gizlilik politikası: kişisel bilgilerin toplanması, kullanımı ve korunması.",
         "", body)


# ---------------------------------------------------------------- Dilek & Şikayet
def complaint_page():
    sube_opts = "".join(
        f'<optgroup label="{e(il)}">' + "".join(f"<option>{e(b[0])}</option>" for y, its in yakas for b in its) + "</optgroup>"
        for il, yakas in il_groups()) + "<option>Canlı Online</option>"
    konu_opts = "".join(f"<option>{x}</option>" for x in ["Öneri", "Şikayet", "Talep", "Teşekkür", "Diğer"])
    body = inner_hero([HOME, ("Dilek & Şikayet", None)], "İletişim formu",
                      "Görüşleriniz bizim için <em>değerli</em>",
                      "Öneri, şikayet, talep ya da teşekkürlerinizi aşağıdaki formla bize iletebilirsiniz.")
    body += f"""
<section class="section">
  <div class="container form-page">
    <div class="form-card reveal">
      <h2 class="form-card__title">Dilek &amp; Şikayet formu</h2>
      <p class="form-card__sub">Yıldızlı (<span style="color:var(--orange-600)">*</span>) alanlar zorunludur.</p>
      <form data-lead-form data-subject="Dilek &amp; Şikayet" novalidate>
        <div class="form-grid">
          <div class="field">
            <label for="d-ad">Ad <span class="req">*</span></label>
            <input id="d-ad" name="ad" type="text" autocomplete="given-name" required aria-describedby="e-ad">
            <span class="field__error" id="e-ad">Lütfen adınızı yazın.</span>
          </div>
          <div class="field">
            <label for="d-soyad">Soyad</label>
            <input id="d-soyad" name="soyad" type="text" autocomplete="family-name">
          </div>
          <div class="field">
            <label for="d-sube">Şube</label>
            <select id="d-sube" name="sube"><option value="">Seçiniz</option>{sube_opts}</select>
          </div>
          <div class="field">
            <label for="d-konu">Konu <span class="req">*</span></label>
            <select id="d-konu" name="konu" required aria-describedby="e-konu"><option value="">Konu seçiniz</option>{konu_opts}</select>
            <span class="field__error" id="e-konu">Lütfen bir konu seçin.</span>
          </div>
          <div class="field field--full">
            <label for="d-tel">Telefon <span class="req">*</span></label>
            <div class="phone-input">
              <span class="phone-input__code" aria-hidden="true">🇹🇷 +90</span>
              <input id="d-tel" name="telefon" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="5xx xxx xx xx" required aria-describedby="e-dtel">
            </div>
            <span class="field__error" id="e-dtel">Lütfen 10 haneli telefon numaranızı girin.</span>
          </div>
          <div class="field field--full">
            <label for="d-mesaj">Mesajınız</label>
            <textarea id="d-mesaj" name="mesaj" style="min-height:160px"></textarea>
          </div>
        </div>
        <button class="btn btn--primary btn--block" type="submit" style="margin-top:20px">{ic("send")} Gönder</button>
        <p class="form-success" role="status" tabindex="-1">{ic("check")} <span>Teşekkürler! Mesajınız alındı.</span></p>
        <p class="form-note">Formu göndererek <a href="gizlilik-politikasi.html">Gizlilik Politikamızı</a> kabul etmiş olursunuz.</p>
      </form>
    </div>
    <div class="quick-contact__grid qc-grid-3" style="margin-top:24px">
      <a class="qc-card qc-card--accent" href="tel:4443644"><span class="qc-card__icon">{ic("phone")}</span><span class="qc-card__label">Merkez telefon</span><span class="qc-card__value">444 3 644</span></a>
      <a class="qc-card" href="mailto:info@uzmanakademi.com.tr"><span class="qc-card__icon">{ic("mail")}</span><span class="qc-card__label">E-posta</span><span class="qc-card__value qc-card__value--sm">info@<wbr>uzmanakademi.com.tr</span></a>
      <div class="qc-card"><span class="qc-card__icon">{ic("clock")}</span><span class="qc-card__label">Çalışma saatleri</span><span class="qc-card__value">09:00 – 19:00</span></div>
    </div>
  </div>
</section>
"""
    page("dilek-sikayet.html", "Dilek ve Şikayet | Uzman Akademi",
         "Uzman Akademi'ye öneri, şikayet, talep ve teşekkürlerinizi iletin.", "", body,
         canon=O + "blank-1")


# ---------------------------------------------------------------- Şube sayfaları
WHAT_SHORT = WHAT[:6]


def split_para(t):
    if len(t) < 700:
        return [t]
    sents = re.split(r"(?<=[.!?])\s+", t)
    half, acc, a = len(t) / 2, 0, []
    for i, s in enumerate(sents):
        acc += len(s)
        a.append(s)
        if acc >= half:
            return [" ".join(a), " ".join(sents[i + 1:])]
    return [t]


def clean_alt(alt, name):
    a = re.sub(r"\.(webp|jpe?g|png)$", "", alt.strip(), flags=re.I).strip()
    if not a or re.search(r"(?i)adsız|görsel|kampanya|^\d+$|tasarım", a):
        return f"Uzman Akademi {name} şubesinde ders"
    return f"{a} — Uzman Akademi {name} şubesi"


def branch_pages():
    BD = C["branches"]
    for b in BR:
        name, reg, city, addr, lm, slug = b
        d = BD[slug]
        heading = d["heading"]  # "Bakırköy Şubemiz"
        paras = [x for p in d["text"].split("\n") for x in split_para(p)]
        same = sorted([x for x in BR if x[1] == reg and x[5] != slug],
                      key=lambda x: (LOC[x[0]][2] != LOC[name][2], tr_key(LOC[x[0]][1])))
        if len(same) < 3:
            same += [x for x in BR if x[1] != reg and x[5] != slug and x[1] == "diger"][: 3 - len(same)]
        near = "\n".join(branch_card(x) for x in same[:6])
        q = f"Uzman Akademi {name} Şubesi, {addr}"
        lm_h = f'<span>{ic("landmark")} {e(lm)}</span>' if lm else ""
        body = inner_hero([HOME, ("Şubeler", "iletisim.html"), (f"{name} Şubesi", None)], f"Hızlı Okuma Kursu · {e(loc_label(b))}",
                          f"{e(heading.replace(' Şubemiz', ''))} <em>Şubemiz</em>", e(addr),
                          f"assets/img/sube/{slug}.jpg", clean_alt(d["alt"], name),
                          actions=f'<a class="btn btn--primary" href="tel:4443644">{ic("phone")} 444 3 644</a><a class="btn btn--ghost-light" href="{maps(b)}" target="_blank" rel="noopener">{ic("nav")} Yol tarifi al</a>',
                          meta=f'{lm_h}<span>{ic("clock")} Her gün 09:00 – 19:00</span>')
        body += f"""
<section class="section">
  <div class="container split">
    <div>
      <div class="prose reveal">
        <h2>{e(name)} Uzman Akademi Hızlı Okuma Kursu</h2>
        {ps(*paras)}
      </div>
      <h3 class="reveal" style="font-size:20px;color:var(--navy-900);margin:36px 0 16px">Şubemizde neler yapıyoruz?</h3>
      <div class="reveal">{mini_list(WHAT_SHORT)}</div>
    </div>
    <div class="split__media reveal" style="gap:0">
      <div class="branch-info">
        <div class="qc-card qc-card--wide"><span class="qc-card__icon">{ic("pin")}</span><span class="qc-card__label">Adres</span><span class="qc-card__sub" style="font-size:15.5px;color:var(--ink)">{e(addr)}</span><a class="qc-card__sub" href="{maps(b)}" target="_blank" rel="noopener" style="font-weight:700;color:var(--navy-700)">Yol tarifi al →</a></div>
        <a class="qc-card qc-card--accent" href="tel:4443644"><span class="qc-card__icon">{ic("phone")}</span><span class="qc-card__label">Merkez telefon</span><span class="qc-card__value" style="font-size:19px">444 3 644</span><span class="qc-card__sub">0212 542 0076</span></a>
        <div class="qc-card"><span class="qc-card__icon">{ic("clock")}</span><span class="qc-card__label">Çalışma saatleri</span><span class="qc-card__value" style="font-size:19px">09:00 – 19:00</span><span class="qc-card__sub">Hafta içi / hafta sonu</span></div>
        <a class="qc-card qc-card--wide" href="mailto:info@uzmanakademi.com.tr"><span class="qc-card__icon">{ic("mail")}</span><span class="qc-card__label">Sorularınız için</span><span class="qc-card__value qc-card__value--sm">info@uzmanakademi.com.tr</span></a>
      </div>
      <div class="map-box">
        <div class="map-box__placeholder">
          <span class="branch-card__pin" style="margin:auto">{ic("pin")}</span>
          <p>Harita Google Haritalar’dan yüklenir. Görüntülemek için tıklayın.</p>
          <button class="btn btn--navy btn--sm" type="button" data-map="{e(q)}" data-title="{e(name)} Şubesi haritası">Haritayı göster</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal" style="display:flex;flex-wrap:wrap;gap:16px;align-items:end;justify-content:space-between;max-width:none">
      <div><span class="eyebrow">{"Bölgedeki şubelerimiz" if reg != "diger" else "Şubelerimiz"}</span><h2 class="section-title">{"Size yakın diğer şubeler" if reg != "diger" else "Diğer şubelerimiz"}</h2></div>
      <a class="btn btn--navy btn--sm" href="iletisim.html#subeler">Tüm şubeler {ic("arrow")}</a>
    </div>
    <div class="branch-grid">
{near}
    </div>
    <div style="margin-top:40px">{cta_band("Şubemiz size uzak mı?", "Canlı online olarak tüm Türkiye’de hizmetinizdeyiz.", "canli-online-kurslarimiz.html", "Canlı Online Kurslarımız", icon="monitor")}</div>
  </div>
</section>
""" + lead_section()
        ld = {"@context": "https://schema.org", "@type": "EducationalOrganization",
              "name": f"Uzman Akademi Hızlı Okuma Kursu — {name} Şubesi", "telephone": "+90-444-3-644",
              "email": "info@uzmanakademi.com.tr", "url": O + slug, "image": f"assets/img/sube/{slug}.jpg",
              "address": {"@type": "PostalAddress", "streetAddress": addr, "addressLocality": city.split(" · ")[0], "addressCountry": "TR"},
              "openingHours": "Mo-Su 09:00-19:00", "parentOrganization": {"@type": "EducationalOrganization", "name": "Uzman Akademi"}}
        page(f"{slug}.html", f"{name} Hızlı Okuma Kursu | Uzman Akademi {name} Şubesi",
             f"Uzman Akademi {name} şubesi: {addr}. Hızlı okuma ve anlama, ilkokul okuma geliştirme, LGS ve YKS kursları. Tel: 444 3 644.",
             "contact", body,
             ld=crumbs_ld([HOME, ("Şubeler", "iletisim.html"), (f"{name} Şubesi", f"{slug}.html")]) +
             '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n")


about_page()
programs_page()
primary_page()
lgs_page()
yks_page()
online_page()
mental_page()
works_page()
refs_page()
teachers_page()
blog_pages()
privacy_page()
complaint_page()
branch_pages()

# ---------------------------------------------------------------- site haritası
urls = []
for f in WRITTEN:
    if f == "index.html":
        urls.append(O)
    elif f.startswith("blog-"):
        urls.append(next(p["canon"] for p in POSTS if p["file"] == f))
    elif f == "dilek-sikayet.html":
        urls.append(O + "blank-1")
    else:
        urls.append(O + f[:-5])
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{e(u)}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: " + O + "sitemap.xml\n")
print(len(WRITTEN), "sayfa yazıldı")
