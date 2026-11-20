/* Uzman Akademi — ortak etkileşimler */
(function () {
  "use strict";

  var doc = document;
  var body = doc.body;

  /* ---------- Header gölgesi ---------- */
  var header = doc.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobil menü ---------- */
  var toggle = doc.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
    });
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && body.classList.contains("menu-open")) {
        body.classList.remove("menu-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Açılır menüler (dokunmatik + klavye) ---------- */
  doc.querySelectorAll(".nav__item > button.nav__link").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.parentElement;
      var willOpen = !item.classList.contains("is-open");
      doc.querySelectorAll(".nav__item.is-open").forEach(function (el) {
        if (el !== item) {
          el.classList.remove("is-open");
          el.querySelector("button.nav__link").setAttribute("aria-expanded", "false");
        }
      });
      item.classList.toggle("is-open", willOpen);
      btn.setAttribute("aria-expanded", String(willOpen));
    });
  });
  doc.addEventListener("click", function (e) {
    if (!e.target.closest(".nav__item")) {
      doc.querySelectorAll(".nav__item.is-open").forEach(function (el) {
        el.classList.remove("is-open");
        el.querySelector("button.nav__link").setAttribute("aria-expanded", "false");
      });
    }
  });

  /* ---------- Görünür olunca belirme ---------- */
  var reveals = doc.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Türkçe uyumlu metin normalleştirme ---------- */
  function norm(s) {
    return (s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i").replace(/ğ/g, "g").replace(/ü/g, "u")
      .replace(/ş/g, "s").replace(/ö/g, "o").replace(/ç/g, "c")
      .replace(/[^a-z0-9 ]/g, " ").replace(/\s+/g, " ").trim();
  }

  /* ---------- Şube arama ve filtre ---------- */
  var branchRoot = doc.querySelector("[data-branches]");
  if (branchRoot) {
    var input = doc.getElementById("branch-search");
    var chips = doc.querySelectorAll(".chip[data-filter]");
    var cards = branchRoot.querySelectorAll(".branch-card");
    var groups = branchRoot.querySelectorAll(".branch-group");
    var empty = doc.querySelector(".empty-state");
    var status = doc.getElementById("branch-status");
    var active = "all";

    cards.forEach(function (c) { c._text = norm(c.textContent + " " + (c.dataset.keywords || "")); });

    var apply = function () {
      var q = norm(input ? input.value : "");
      var shown = 0;
      cards.forEach(function (c) {
        var okRegion = active === "all" || c.dataset.region === active;
        var okText = !q || q.split(" ").every(function (w) { return c._text.indexOf(w) !== -1; });
        var visible = okRegion && okText;
        c.hidden = !visible;
        if (visible) shown++;
      });
      groups.forEach(function (g) {
        g.hidden = !g.querySelector(".branch-card:not([hidden])");
      });
      if (empty) empty.classList.toggle("is-visible", shown === 0);
      if (status) status.textContent = shown === 0 ? "Eşleşen şube bulunamadı." : shown + " şube gösteriliyor.";
    };

    if (input) input.addEventListener("input", apply);
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        active = chip.dataset.filter;
        chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
        apply();
      });
    });
    var reset = doc.querySelector("[data-reset-filter]");
    if (reset) {
      reset.addEventListener("click", function () {
        if (input) input.value = "";
        active = "all";
        chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c.dataset.filter === "all")); });
        apply();
        if (input) input.focus();
      });
    }
  }

  /* ---------- Bilgi formu ---------- */
  doc.querySelectorAll("form[data-lead-form]").forEach(function (form) {
    var success = form.querySelector(".form-success");
    var phone = form.querySelector("input[name='telefon']");

    if (phone) {
      phone.addEventListener("input", function () {
        var d = phone.value.replace(/\D/g, "").replace(/^90/, "").replace(/^0/, "").slice(0, 10);
        var out = d;
        if (d.length > 3) out = d.slice(0, 3) + " " + d.slice(3);
        if (d.length > 6) out = out.slice(0, 7) + " " + d.slice(6);
        if (d.length > 8) out = out.slice(0, 10) + " " + d.slice(8);
        phone.value = out;
      });
    }

    var setError = function (field, on) {
      var wrap = field.closest(".field");
      if (wrap) wrap.classList.toggle("has-error", on);
      field.setAttribute("aria-invalid", on ? "true" : "false");
    };

    form.querySelectorAll("input, select").forEach(function (f) {
      f.addEventListener("input", function () { if (f.closest(".has-error")) setError(f, false); });
      f.addEventListener("change", function () { if (f.closest(".has-error")) setError(f, false); });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstBad = null;
      form.querySelectorAll("[required]").forEach(function (f) {
        var bad = !f.value.trim();
        if (f === phone) bad = f.value.replace(/\D/g, "").length !== 10;
        setError(f, bad);
        if (bad && !firstBad) firstBad = f;
      });
      if (firstBad) { firstBad.focus(); return; }

      var data = new FormData(form);
      var endpoint = form.dataset.endpoint;

      var done = function () {
        form.reset();
        if (success) {
          success.classList.add("is-visible");
          success.focus();
        }
      };

      if (endpoint) {
        fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
          .then(function (r) { if (!r.ok) throw new Error(); done(); })
          .catch(function () { alert("Form gönderilemedi. Lütfen 444 3 644 numarasından bize ulaşın."); });
        return;
      }

      /* Sunucu bağlantısı tanımlı değilse e-posta istemcisiyle gönder */
      var lines = [];
      form.querySelectorAll("input[name], select[name], textarea[name]").forEach(function (f) {
        var lab = form.querySelector("label[for='" + f.id + "']");
        var name = lab ? lab.firstChild.textContent.trim() : f.name;
        var val = f.value.trim() || "-";
        if (f === phone && f.value.trim()) val = "+90 " + val;
        lines.push(name + ": " + val);
      });
      var subject = (form.dataset.subject || "Detaylı bilgi talebi") +
        (data.get("il_ilce") ? " — " + data.get("il_ilce") : "");
      var href = "mailto:info@uzmanakademi.com.tr?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(lines.join("\n"));
      window.location.href = href;
      done();
    });
  });

  /* ---------- YouTube videoları (tıklayınca yüklenir) ---------- */
  var modal = null;
  var lastTrigger = null;
  function closeModal() {
    if (!modal) return;
    modal.classList.remove("is-open");
    modal.querySelector(".video-modal__box").innerHTML = "";
    body.style.overflow = "";
    if (lastTrigger) lastTrigger.focus();
  }
  function openVideo(id, title, vertical, trigger) {
    if (!modal) {
      modal = doc.createElement("div");
      modal.className = "video-modal";
      modal.setAttribute("role", "dialog");
      modal.setAttribute("aria-modal", "true");
      modal.innerHTML = '<div class="video-modal__wrap" style="position:relative"><button class="video-modal__close" type="button" aria-label="Videoyu kapat">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button>' +
        '<div class="video-modal__box"></div></div>';
      body.appendChild(modal);
      modal.addEventListener("click", function (e) { if (e.target === modal) closeModal(); });
      modal.querySelector(".video-modal__close").addEventListener("click", closeModal);
      doc.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("is-open")) closeModal(); });
    }
    lastTrigger = trigger;
    var box = modal.querySelector(".video-modal__box");
    box.classList.toggle("is-vertical", !!vertical);
    var iframe = doc.createElement("iframe");
    iframe.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0&playsinline=1";
    iframe.title = title || "Video";
    iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    iframe.allowFullScreen = true;
    box.innerHTML = "";
    box.appendChild(iframe);
    modal.setAttribute("aria-label", title || "Video");
    modal.classList.add("is-open");
    body.style.overflow = "hidden";
    modal.querySelector(".video-modal__close").focus();
  }
  doc.addEventListener("click", function (e) {
    var t = e.target.closest("[data-yt]");
    if (!t) return;
    e.preventDefault();
    if (t.dataset.inline !== undefined) {
      var iframe = doc.createElement("iframe");
      iframe.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(t.dataset.yt) + "?autoplay=1&rel=0&playsinline=1";
      iframe.title = t.dataset.title || "Video";
      iframe.allow = "autoplay; encrypted-media; picture-in-picture";
      iframe.allowFullScreen = true;
      iframe.style.cssText = "position:absolute;inset:0;width:100%;height:100%;border:0";
      t.replaceWith(iframe);
      return;
    }
    openVideo(t.dataset.yt, t.dataset.title, t.dataset.vertical !== undefined, t);
  });

  /* ---------- Daha fazla göster ---------- */
  doc.querySelectorAll("[data-more]").forEach(function (btn) {
    var grid = doc.getElementById(btn.dataset.more);
    var step = parseInt(btn.dataset.step || "12", 10);
    if (!grid) return;
    btn.addEventListener("click", function () {
      var hidden = grid.querySelectorAll(":scope > [hidden]");
      for (var i = 0; i < Math.min(step, hidden.length); i++) hidden[i].hidden = false;
      if (grid.querySelectorAll(":scope > [hidden]").length === 0) btn.parentElement.remove();
    });
  });

  /* ---------- Harita (tıklayınca yüklenir) ---------- */
  doc.querySelectorAll("[data-map]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var box = btn.closest(".map-box");
      var iframe = doc.createElement("iframe");
      iframe.src = "https://maps.google.com/maps?q=" + encodeURIComponent(btn.dataset.map) + "&z=16&output=embed";
      iframe.title = btn.dataset.title || "Harita";
      iframe.loading = "lazy";
      iframe.referrerPolicy = "no-referrer-when-downgrade";
      box.innerHTML = "";
      box.appendChild(iframe);
    });
  });

  /* ---------- Sayfa içi menü vurgusu ---------- */
  var subLinks = doc.querySelectorAll(".subnav a[href^='#']");
  if (subLinks.length && "IntersectionObserver" in window) {
    var map = {};
    subLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          subLinks.forEach(function (a) { a.classList.remove("is-active"); });
          var a = map[en.target.id];
          if (a) {
            a.classList.add("is-active");
            var bar = a.parentElement;
            bar.scrollTo({ left: a.offsetLeft - (bar.clientWidth - a.offsetWidth) / 2, behavior: "smooth" });
          }
        }
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    Object.keys(map).forEach(function (id) { var el = doc.getElementById(id); if (el) so.observe(el); });
  }

  /* ---------- Yıl ---------- */
  doc.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
