// Vector Consulting — menu, contact form and hero vector field
(function () {
  var btn = document.querySelector(".menu"), nav = document.getElementById("nav");
  if (btn && nav) btn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  var form = document.getElementById("contact-form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    var f = new FormData(form);
    var subject = "Project enquiry — " + (f.get("company") || f.get("name"));
    var body = f.get("message") + "\n\n" + f.get("name") + (f.get("company") ? " · " + f.get("company") : "") + "\n" + f.get("email");
    window.location.href = "mailto:" + form.dataset.to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
  });

  // Animated explainer videos in a lightbox (iframe); closes on Esc, backdrop or the player's close button.
  var box = null, last = null;
  function closeVideo() {
    if (!box || box.hidden) return;
    box.querySelector("iframe").src = "about:blank"; box.hidden = true;
    document.documentElement.style.overflow = ""; if (last) last.focus();
  }
  document.querySelectorAll("[data-video]").forEach(function (b) {
    b.addEventListener("click", function () {
      if (!box) {
        box = document.createElement("div"); box.className = "vbox"; box.hidden = true;
        box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true");
        box.innerHTML = '<div class="vbox-in"><iframe allow="autoplay; fullscreen" allowfullscreen title="Video"></iframe></div>';
        box.addEventListener("click", function (e) { if (e.target === box) closeVideo(); });
        document.body.appendChild(box);
      }
      last = b; box.hidden = false; document.documentElement.style.overflow = "hidden";
      var f = box.querySelector("iframe"); f.title = b.getAttribute("aria-label") || b.textContent.trim();
      f.src = b.getAttribute("data-video"); f.focus();
    });
  });
  window.addEventListener("message", function (e) { if (e.data && e.data.vector === "cerrar") closeVideo(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeVideo(); });

  // Vector field: short strokes aligned to a slowly drifting flow field.
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll("canvas.field").forEach(function (cv) {
    var ctx = cv.getContext("2d"), w, h, dpr, t = 0, raf;
    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = cv.clientWidth; h = cv.clientHeight;
      cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    function draw() {
      ctx.clearRect(0, 0, w, h);
      var step = 34;
      for (var y = step / 2; y < h; y += step) {
        for (var x = step / 2; x < w; x += step) {
          var a = Math.sin(x * 0.006 + t) * 1.2 + Math.cos(y * 0.008 - t * 0.7) * 1.1;
          var fade = Math.min(1, x / (w * 0.55));
          var len = 9 + 5 * Math.sin(x * 0.01 + y * 0.01 + t);
          ctx.strokeStyle = "rgba(" + (x / w > 0.7 ? "62,230,200," : "120,150,255,") + (0.12 + 0.35 * fade) + ")";
          ctx.lineWidth = 1.3;
          ctx.beginPath();
          ctx.moveTo(x, y);
          ctx.lineTo(x + Math.cos(a) * len, y + Math.sin(a) * len);
          ctx.stroke();
        }
      }
    }
    function loop() { t += 0.004; draw(); raf = requestAnimationFrame(loop); }
    size(); draw();
    window.addEventListener("resize", function () { size(); draw(); });
    if (!reduce) loop();
  });
})();
