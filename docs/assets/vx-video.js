/* Vector Consulting · animated explainer engine (SVG + GSAP)
   Same interaction model as the ARGOS presentations: 7 scenes, chapter bar,
   optional voice-over synchronised to the timeline, captions always visible,
   Esc / close button posts {vector:"cerrar"} to the parent lightbox.
   A video page defines window.VX = {id, lang, audio, title, scenes:[...], starts:[...], total}. */
(function () {
  "use strict";
  const V = window.VX, L = V.lang === "es" ? "es" : "en";
  const T = {
    en: {play: "Play (space)", pause: "Pause (space)", prev: "Previous scene", next: "Next scene", replay: "Replay", close: "Close (Esc)",
         voiceOn: "🔊 Enable voice-over", voiceOff: "🔇 Mute", start: "▶ Play", reduced: "Animation reduced (your device prefers reduced motion)"},
    es: {play: "Reproducir (espacio)", pause: "Pausa (espacio)", prev: "Escena anterior", next: "Escena siguiente", replay: "Repetir", close: "Cerrar (Esc)",
         voiceOn: "🔊 Activar locución", voiceOff: "🔇 Silenciar", start: "▶ Reproducir", reduced: "Animación reducida (tu dispositivo prefiere menos movimiento)"}
  }[L];
  const NS = "http://www.w3.org/2000/svg";
  const $ = s => document.querySelector(s), $$ = s => Array.from(document.querySelectorAll(s));
  const q = new URLSearchParams(location.search);
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const C = {ink: "#0b1526", ink2: "#13223a", vector: "#2f5bff", v2: "#4a72ff", deep: "#1b39b8", signal: "#3ee6c8", muted: "#9fb0cc", line: "rgba(255,255,255,.14)", warn: "#ff7a7a"};
  const FD = "'Bricolage Grotesque',system-ui,sans-serif", FB = "'IBM Plex Sans',system-ui,sans-serif", FP = "Poppins,system-ui,sans-serif";

  /* ---------- tiny SVG helpers */
  function el(tag, attrs, parent, text) {
    const e = document.createElementNS(NS, tag);
    for (const k in (attrs || {})) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  const ICON = {
    code: '<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>',
    team: '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 2 6 5.5"/>',
    ai: '<rect x="5" y="5" width="14" height="14" rx="3"/><path d="M9 1v4M15 1v4M9 19v4M15 19v4M1 9h4M1 15h4M19 9h4M19 15h4M9.5 15l2.5-6 2.5 6M10.3 13h3.4"/>',
    compass: '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    health: '<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 10c0 6-8 11-8 11z"/><path d="M8 12h2.5l1-2 2 4 1-2H16"/>',
    db: '<ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/>',
    lab: '<path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 006.2 21.5h11.6a2 2 0 001.7-3L14 9V3"/><path d="M7 15h10"/>',
    chip: '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 2v4M14 2v4M10 18v4M14 18v4M2 10h4M2 14h4M18 10h4M18 14h4"/>',
    lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 018 0v4"/>',
    shield: '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    doc: '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    x: '<path d="M6 6l12 12M18 6L6 18"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/>',
    building: '<path d="M4 21V5l8-3v19M12 9l8 3v9M8 8h1M8 12h1M8 16h1M15 14h2M15 18h2"/>',
    form: '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
    swap: '<path d="M4 8h13l-3-3M20 16H7l3 3"/>',
    tools: '<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    chat: '<path d="M4 5h16v11H9l-5 4z"/>',
    board: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16M15 4v16"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    spark: '<path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>',
    erp: '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 21h8M12 18v3"/>',
    policy: '<path d="M6 3h12v18H6z"/><path d="M9 8h6M9 12h6M9 16h3"/><circle cx="17" cy="17" r="3.2" fill="#0b1526"/><path d="M15.7 17l.9.9 1.6-1.7"/>'
  };
  function icon(name, x, y, s, color, parent) {
    const g = el("g", {transform: `translate(${x - s / 2} ${y - s / 2}) scale(${s / 24})`, fill: "none", stroke: color, "stroke-width": 1.8, "stroke-linecap": "round", "stroke-linejoin": "round"}, parent);
    g.innerHTML = ICON[name] || ICON.spark;
    return g;
  }
  let uid = 0;
  function mark(x, y, s, parent, withSweep) {          // the Vector capsule mark (64 grid)
    const u = "m" + (++uid);
    const outer = el("g", {}, parent);
    const g = el("g", {transform: `translate(${x - s / 2} ${y - s / 2}) scale(${s / 64})`}, outer);
    const Lr = '<rect x="17" y="2.75" width="16" height="56.5" rx="8" transform="rotate(-20.2 25 31)"/>';
    const Rr = '<rect x="31" y="2.75" width="16" height="56.5" rx="8" transform="rotate(20.2 39 31)"/>';
    g.innerHTML = `<defs><clipPath id="${u}l">${Lr}</clipPath><clipPath id="${u}a">${Lr}${Rr}</clipPath>
      <linearGradient id="${u}s" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
      ${Lr.replace("/>", ' fill="#4a72ff"/>')}${Rr.replace("/>", ' fill="#2f5bff"/>')}
      <g clip-path="url(#${u}l)">${Rr.replace("/>", ' fill="#1b39b8"/>')}</g>
      <g clip-path="url(#${u}a)"><rect class="msweep" x="-20" y="-4" width="14" height="72" fill="url(#${u}s)" transform="skewX(-22)"/></g>
      <path class="mspark" opacity="0" d="M51 0 L52.5 4.5 L57 6 L52.5 7.5 L51 12 L49.5 7.5 L45 6 L49.5 4.5 Z" fill="#fff"/>`;
    return outer;
  }
  function card(parent, x, y, w, h, opts) {
    opts = opts || {};
    const g = el("g", {class: "card"}, parent);
    el("rect", {x, y, width: w, height: h, rx: 18, fill: opts.fill || "rgba(255,255,255,.06)", stroke: opts.stroke || "rgba(255,255,255,.18)", "stroke-width": 1.5}, g);
    const glow = el("rect", {class: "glow", x: x - 2, y: y - 2, width: w + 4, height: h + 4, rx: 20, fill: "none", stroke: C.signal, "stroke-width": 3, opacity: 0}, g);
    if (opts.icon) icon(opts.icon, x + w / 2, y + (opts.label ? h * .38 : h / 2), opts.iconSize || 46, opts.iconColor || C.signal, g);
    if (opts.label) wrapText(g, opts.label, x + w / 2, y + h * (opts.icon ? .74 : .5), w - 28, opts.fs || 24, "#fff", 600, "middle");
    g._glow = glow;
    return g;
  }
  function wrapText(parent, str, x, y, maxW, fs, fill, weight, anchor, family) {
    const t = el("text", {x, y, "font-size": fs, "font-weight": weight || 600, fill, "text-anchor": anchor || "middle", "font-family": family || FB}, parent);
    const words = String(str).split(" "), lines = [];
    let line = "";
    const approx = s => s.length * fs * .52;
    words.forEach(w => { const tryL = line ? line + " " + w : w; if (approx(tryL) > maxW && line) { lines.push(line); line = w; } else line = tryL; });
    lines.push(line);
    const lh = fs * 1.18, y0 = y - (lines.length - 1) * lh / 2 + fs * .34;
    lines.forEach((ln, i) => el("tspan", {x, y: y0 + i * lh}, t, ln));
    return t;
  }
  function header(g, s) {
    const h = el("g", {class: "hdr"}, g);
    const kw = Math.max(150, s.kicker.length * 11.5 + 44);
    el("rect", {x: 80, y: 52, width: kw, height: 40, rx: 20, fill: "rgba(62,230,200,.14)", stroke: "rgba(62,230,200,.55)"}, h);
    el("text", {x: 80 + kw / 2, y: 78, "text-anchor": "middle", "font-size": 17, "font-weight": 600, fill: C.signal, "font-family": FB, "letter-spacing": "1.5"}, h, s.kicker.toUpperCase());
    const t = el("text", {class: "ttl", x: 80, y: 160, "font-size": s.title.length > 46 ? 46 : 54, "font-weight": 700, fill: "#fff", "font-family": FD, "data-full": s.title}, h, "");
    const ul = el("rect", {class: "ul", x: 80, y: 176, width: 0, height: 6, rx: 3, fill: C.signal}, h);
    return {h, t, ul};
  }
  function typeIn(textEl, dur) {
    const full = textEl.getAttribute("data-full"), o = {n: 0};
    return gsap.to(o, {n: full.length, duration: dur, ease: "none", onUpdate: () => { textEl.textContent = full.slice(0, Math.round(o.n)); }});
  }
  function underline(t, ul, word) {          // measure the highlighted word once the title is complete
    return () => {
      if (!word) return;
      const full = t.getAttribute("data-full"); t.textContent = full;
      const i = full.indexOf(word); if (i < 0) return;
      const x = t.getStartPositionOfChar(i).x, w = t.getSubStringLength(i, word.length);
      ul.setAttribute("x", x); ul.setAttribute("width", w);
    };
  }

  /* ---------- stage */
  const svg = $("#stage");
  const defs = el("defs", {}, svg);
  defs.innerHTML = `<linearGradient id="bgG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1526"/><stop offset="1" stop-color="#16274a"/></linearGradient>
    <radialGradient id="haloG"><stop offset="0" stop-color="#2f5bff" stop-opacity=".55"/><stop offset="1" stop-color="#2f5bff" stop-opacity="0"/></radialGradient>
    <radialGradient id="dotG"><stop offset="0" stop-color="#fff"/><stop offset=".4" stop-color="#3ee6c8"/><stop offset="1" stop-color="#3ee6c8" stop-opacity="0"/></radialGradient>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#3ee6c8"/></marker>`;
  el("rect", {width: 1600, height: 900, fill: "url(#bgG)"}, svg);
  const field = el("g", {opacity: .5}, svg);        // vector field, like the website hero
  for (let y = 20; y < 900; y += 40) for (let x = 20; x < 1600; x += 40) {
    const a = Math.sin(x / 260) + Math.cos(y / 180) + x / 1400, t = x / 1600;
    el("line", {x1: x - 6 * Math.cos(a), y1: y - 6 * Math.sin(a), x2: x + 6 * Math.cos(a), y2: y + 6 * Math.sin(a),
      stroke: t > .5 ? C.signal : C.vector, "stroke-opacity": .12 + .25 * t * (y / 900), "stroke-width": 1.6, "stroke-linecap": "round"}, field);
  }
  const brand = el("g", {opacity: .9}, svg);
  mark(1520, 128, 40, brand);
  el("text", {x: 1482, y: 135, "text-anchor": "end", "font-size": 15, "font-weight": 600, fill: "#fff", "font-family": FP, "letter-spacing": 4}, brand, "VECTOR");

  /* ---------- scene builders: each returns a function(tl, at, dur) that schedules the animation */
  const B = {};
  B.q = (g, s) => {
    const halo = el("circle", {cx: 800, cy: 330, r: 210, fill: "url(#haloG)"}, g);
    const m = mark(800, 330, 190, g);
    const t = el("text", {x: 800, y: 610, "text-anchor": "middle", "font-size": s.text.length > 44 ? 50 : 58, "font-weight": 700, fill: "#fff", "font-family": FD, "data-full": s.text}, g, "");
    gsap.set(m, {opacity: 0, scale: .6, svgOrigin: "800 330"}); gsap.set(halo, {scale: 0, svgOrigin: "800 330"});
    return (tl, at, d) => {
      tl.to(halo, {scale: 1, duration: .9, ease: "expo.out"}, at)
        .to(m, {opacity: 1, scale: 1, duration: .7, ease: "back.out(2)"}, at + .1)
        .add(typeIn(t, Math.min(1.6, d * .45)), at + .7);
      sweep(tl, m, at + 1.2);
    };
  };
  function sweep(tl, m, at) {
    const sw = m.querySelector(".msweep"), sp = m.querySelector(".mspark");
    tl.fromTo(sw, {attr: {x: -30}}, {attr: {x: 90}, duration: 1.1, ease: "power2.inOut"}, at)
      .fromTo(sp, {opacity: 0, scale: .2, svgOrigin: "51 6"}, {opacity: 1, scale: 1.2, rotation: 45, duration: .3}, at + .8)
      .to(sp, {opacity: 0, scale: .2, rotation: 90, duration: .35}, at + 1.15);
  }
  function hdrAnim(tl, H, s, at) {
    gsap.set(H.h, {opacity: 0, x: -30});
    tl.to(H.h, {opacity: 1, x: 0, duration: .5}, at).add(typeIn(H.t, Math.min(1.2, s.title.length * .028)), at + .15)
      .add(underline(H.t, H.ul, s.hl), at + .25 + Math.min(1.2, s.title.length * .028));
  }
  function row(n, w, gap, cx) { const tot = n * w + (n - 1) * gap; return Array.from({length: n}, (_, i) => cx - tot / 2 + i * (w + gap)); }
  B.cards = (g, s) => {            // items: [{icon,label}] ; variant: "broken" | "repeat" | default
    const H = header(g, s), n = s.items.length, w = n > 4 ? 240 : n > 3 ? 300 : 340, h = s.variant ? 200 : 230;
    const xs = row(n, w, 30, 800), y = 330;
    const cs = s.items.map((it, i) => card(g, xs[i], y + (s.variant === "broken" ? (i % 2 ? 40 : -20) : 0), w, h,
      {icon: it.icon, label: it.label, stroke: s.variant === "broken" ? "rgba(255,122,122,.45)" : null, fs: n > 4 ? 22 : 24}));
    const extra = el("g", {}, g);
    if (s.variant === "broken") cs.forEach((c, i) => { const cx = xs[i] + w - 16, cy = y + (i % 2 ? 40 : -20) + 18;
      el("circle", {cx, cy, r: 18, fill: C.warn}, extra); el("text", {x: cx, y: cy + 8, "text-anchor": "middle", "font-size": 24, "font-weight": 700, fill: C.ink, "font-family": FD}, extra, "?"); });
    if (s.note) wrapText(g, s.note, 800, 640, 1300, 26, C.muted, 500, "middle");
    const note = g.lastChild;
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set(cs, {opacity: 0, y: 40}); gsap.set(extra, {opacity: 0});
      if (s.note) gsap.set(note, {opacity: 0});
      const step = Math.min(.45, (d * .6) / n);
      cs.forEach((c, i) => {
        const t0 = at + .9 + i * step;
        tl.to(c, {opacity: 1, y: 0, duration: .45, ease: "back.out(2)"}, t0)
          .to(c._glow, {opacity: 1, duration: .15}, t0).to(c._glow, {opacity: 0, duration: .5}, t0 + .35);
      });
      tl.to(extra, {opacity: 1, duration: .3}, at + .9 + n * step);
      if (s.note) tl.to(note, {opacity: 1, duration: .5}, at + 1.2 + n * step);
    };
  };
  B.merge = (g, s) => {            // small cards fly into one big card
    const H = header(g, s), n = s.from.length, xs = row(n, 200, 24, 800);
    const small = s.from.map((lb, i) => card(g, xs[i], 300, 200, 110, {label: lb, fs: 21}));
    const big = el("g", {}, g);
    el("rect", {x: 480, y: 270, width: 640, height: 380, rx: 26, fill: "rgba(47,91,255,.18)", stroke: C.vector, "stroke-width": 2.5}, big);
    mark(800, 340, 84, big);
    el("text", {x: 800, y: 425, "text-anchor": "middle", "font-size": 30, "font-weight": 600, fill: "#fff", "font-family": FP, "letter-spacing": 9}, big, "VECTOR");
    s.rows.forEach((r, i) => { const yy = 490 + i * 52; icon("check", 600, yy - 8, 26, C.signal, big);
      el("text", {x: 628, y: yy, "font-size": 27, "font-weight": 600, fill: "#fff", "font-family": FB}, big, r); });
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set(small, {opacity: 0}); gsap.set(big, {opacity: 0, scale: .85, svgOrigin: "800 460"});
      small.forEach((c, i) => tl.to(c, {opacity: 1, duration: .3}, at + .6 + i * .12));
      tl.to(small, {x: (i) => 800 - (xs[i] + 100), y: 120, scale: .4, opacity: 0, svgOrigin: "800 360", duration: .8, ease: "power3.in", stagger: .05}, at + 1.8)
        .to(big, {opacity: 1, scale: 1, duration: .7, ease: "back.out(1.8)"}, at + 2.3);
      sweep(tl, big.querySelector("g"), at + 3);
    };
  };
  B.map = (g, s) => {              // cities joined by arcs with light pulses
    const H = header(g, s);
    const P = s.cities.map(c => ({...c}));
    const arcs = [], pulses = [];
    for (let i = 1; i < P.length; i++) {
      const a = P[0], b = P[i], mx = (a.x + b.x) / 2, my = Math.min(a.y, b.y) - 140;
      const p = el("path", {d: `M${a.x} ${a.y} Q${mx} ${my} ${b.x} ${b.y}`, fill: "none", stroke: C.signal, "stroke-width": 3, "stroke-opacity": .7, "stroke-dasharray": "2 10", "stroke-linecap": "round"}, g);
      arcs.push(p);
      pulses.push(el("circle", {r: 12, fill: "url(#dotG)", opacity: 0}, g));
    }
    const nodes = P.map((c, i) => {
      const n = el("g", {}, g);
      el("circle", {cx: c.x, cy: c.y, r: i === 0 ? 30 : 22, fill: i === 0 ? C.vector : C.v2, stroke: "#fff", "stroke-width": 3}, n);
      el("circle", {cx: c.x, cy: c.y, r: i === 0 ? 52 : 40, fill: "none", stroke: C.signal, "stroke-opacity": .5, "stroke-width": 2, class: "ring"}, n);
      el("text", {x: c.x, y: c.y + (c.below ? 86 : -62), "text-anchor": "middle", "font-size": 30, "font-weight": 700, fill: "#fff", "font-family": FD}, n, c.name);
      if (c.sub) el("text", {x: c.x, y: c.y + (c.below ? 118 : -30 - 62 + 30 - 30), "text-anchor": "middle", "font-size": 20, fill: C.muted, "font-family": FB}, n, c.sub);
      return n;
    });
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set(nodes, {opacity: 0, scale: .4, transformOrigin: "50% 50%"}); gsap.set(arcs, {opacity: 0});
      nodes.forEach((n, i) => tl.to(n, {opacity: 1, scale: 1, duration: .5, ease: "back.out(2.5)"}, at + .7 + i * .35));
      arcs.forEach((a, i) => {
        const t0 = at + 1.6 + i * .3, len = a.getTotalLength(), o = {p: 0};
        tl.to(a, {opacity: 1, duration: .4}, t0)
          .to(pulses[i], {opacity: 1, duration: .2}, t0 + .2)
          .to(o, {p: 1, duration: 1.4, ease: "power1.inOut", repeat: 2, onUpdate: () => { const pt = a.getPointAtLength(o.p * len); pulses[i].setAttribute("cx", pt.x); pulses[i].setAttribute("cy", pt.y); }}, t0 + .2);
      });
    };
  };
  B.chips = (g, s) => {
    const H = header(g, s), per = Math.ceil(s.items.length / 2);
    const chips = s.items.map((lb, i) => {
      const r = Math.floor(i / per), inRow = r ? s.items.length - per : per, j = i - r * per, w = 300;
      const x0 = 800 - (inRow * w + (inRow - 1) * 26) / 2 + j * (w + 26), y = 300 + r * 130;
      const c = el("g", {}, g);
      el("rect", {x: x0, y, width: w, height: 96, rx: 48, fill: "rgba(255,255,255,.06)", stroke: "rgba(62,230,200,.5)", "stroke-width": 1.6}, c);
      icon("shield", x0 + 52, y + 48, 34, C.signal, c);
      el("text", {x: x0 + 86, y: y + 58, "font-size": 28, "font-weight": 700, fill: "#fff", "font-family": FD}, c, lb);
      return c;
    });
    if (s.note) wrapText(g, s.note, 800, 640, 1300, 26, C.muted, 500, "middle");
    const note = s.note ? g.lastChild : null;
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set(chips, {opacity: 0, scale: .7, transformOrigin: "50% 50%"}); if (note) gsap.set(note, {opacity: 0});
      tl.to(chips, {opacity: 1, scale: 1, duration: .4, ease: "back.out(2.4)", stagger: Math.min(.3, d * .5 / chips.length)}, at + .9);
      if (note) tl.to(note, {opacity: 1, duration: .5}, at + 1.2 + chips.length * .25);
    };
  };
  B.flow = (g, s) => {             // nodes in a row; a token travels; optional gate that rejects one token
    const H = header(g, s), n = s.nodes.length, w = n > 3 ? 250 : 300, xs = row(n, w, n > 3 ? 90 : 140, 800), y = 330, h = 210;
    const cs = s.nodes.map((nd, i) => card(g, xs[i], y, w, h, {icon: nd.icon, label: nd.label, fill: nd.hl ? "rgba(47,91,255,.22)" : null, stroke: nd.hl ? C.vector : null, fs: 23}));
    const arrows = [];
    for (let i = 0; i < n - 1; i++) arrows.push(el("path", {d: `M${xs[i] + w + 14} ${y + h / 2} H${xs[i + 1] - 14}`, stroke: C.signal, "stroke-width": 3.5, fill: "none", "marker-end": "url(#arr)"}, g));
    const tok = el("g", {opacity: 0}, g);
    const tw_ = Math.max(140, (s.token || "").length * 11 + 40);
    el("rect", {x: -tw_ / 2, y: -24, width: tw_, height: 48, rx: 24, fill: C.signal}, tok);
    el("text", {x: 0, y: 8, "text-anchor": "middle", "font-size": 19, "font-weight": 700, fill: C.ink, "font-family": FB}, tok, s.token || "");
    let bad = null;
    if (s.reject) { bad = el("g", {opacity: 0}, g);
      const bw_ = Math.max(140, s.reject.length * 11 + 40);
      el("rect", {x: -bw_ / 2, y: -24, width: bw_, height: 48, rx: 24, fill: C.warn}, bad);
      el("text", {x: 0, y: 8, "text-anchor": "middle", "font-size": 19, "font-weight": 700, fill: C.ink, "font-family": FB}, bad, s.reject); }
    if (s.note) wrapText(g, s.note, 800, 660, 1300, 26, C.muted, 500, "middle");
    const note = s.note ? g.lastChild : null;
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set(cs, {opacity: 0, y: 30}); arrows.forEach(a => { const L = a.getTotalLength(); a.style.strokeDasharray = L; a.style.strokeDashoffset = L; });
      if (note) gsap.set(note, {opacity: 0});
      cs.forEach((c, i) => { tl.to(c, {opacity: 1, y: 0, duration: .45, ease: "back.out(2)"}, at + .8 + i * .45);
        if (i < n - 1) tl.to(arrows[i], {strokeDashoffset: 0, duration: .4}, at + 1.1 + i * .45); });
      const t1 = at + 1.2 + n * .45, ty = y - 40;
      if (s.token) {
        tl.set(tok, {x: xs[0] + w / 2, y: ty}, t1).to(tok, {opacity: 1, duration: .25}, t1)
          .to(tok, {x: xs[n - 1] + w / 2, duration: Math.max(1.4, d * .3), ease: "power1.inOut"}, t1 + .2);
        cs.forEach((c, i) => tl.to(c._glow, {opacity: 1, duration: .15}, t1 + .2 + i * Math.max(1.4, d * .3) / Math.max(1, n - 1))
          .to(c._glow, {opacity: 0, duration: .5}, t1 + .55 + i * Math.max(1.4, d * .3) / Math.max(1, n - 1)));
      }
      if (bad) {
        const gx = xs[s.gateAt || 1] + w / 2, t2 = t1 + Math.max(1.4, d * .3) + .3;
        tl.set(bad, {x: xs[0] + w / 2, y: y + h + 46}, t2).to(bad, {opacity: 1, duration: .25}, t2)
          .to(bad, {x: gx - 40, duration: .9, ease: "power1.in"}, t2 + .2)
          .to(bad, {x: gx - 70, duration: .15, yoyo: true, repeat: 3}, t2 + 1.1)
          .to(bad, {opacity: .25, duration: .4}, t2 + 1.8);
        tl.to(cs[s.gateAt || 1].querySelector("rect"), {stroke: C.warn, duration: .2, yoyo: true, repeat: 3}, t2 + 1.1);
      }
      if (note) tl.to(note, {opacity: 1, duration: .5}, t1 + 1.2);
    };
  };
  B.consent = (g, s) => {          // patient record: 6 sections, only consented ones leave the server
    const H = header(g, s);
    const srv = card(g, 200, 260, 420, 420, {});
    icon("db", 410, 310, 44, C.signal, srv);
    el("text", {x: 410, y: 370, "text-anchor": "middle", "font-size": 24, "font-weight": 700, fill: "#fff", "font-family": FD}, srv, s.server);
    const secs = s.sections.map((lb, i) => {
      const ok = s.allowed.includes(i), yy = 400 + i * 44, r = el("g", {}, srv);
      el("rect", {x: 240, y: yy, width: 340, height: 34, rx: 10, fill: ok ? "rgba(62,230,200,.18)" : "rgba(255,255,255,.06)", stroke: ok ? C.signal : "rgba(255,255,255,.18)"}, r);
      el("text", {x: 258, y: yy + 23, "font-size": 18, fill: "#fff", "font-family": FB}, r, lb);
      icon(ok ? "check" : "lock", 556, yy + 17, 20, ok ? C.signal : C.muted, r);
      return {r, ok, yy};
    });
    const dst = card(g, 1010, 280, 390, 380, {});
    icon("user", 1205, 340, 46, C.signal, dst);
    el("text", {x: 1205, y: 405, "text-anchor": "middle", "font-size": 25, "font-weight": 700, fill: "#fff", "font-family": FB}, dst, s.viewer);
    const packs = secs.filter(x => x.ok).map((x, i) => { const p = el("g", {opacity: 0}, g);
      el("rect", {x: -90, y: -20, width: 180, height: 40, rx: 12, fill: C.signal}, p);
      el("text", {x: 0, y: 7, "text-anchor": "middle", "font-size": 17, "font-weight": 700, fill: C.ink, "font-family": FB}, p, s.sections[s.allowed[i]]);
      return {p, x}; });
    const wall = el("path", {d: "M800 250 V690", stroke: C.signal, "stroke-width": 4, "stroke-dasharray": "10 10", opacity: 0}, g);
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set([srv, dst], {opacity: 0, y: 30}); gsap.set(secs.map(x => x.r), {opacity: 0, x: -20});
      tl.to(srv, {opacity: 1, y: 0, duration: .5}, at + .8).to(dst, {opacity: 1, y: 0, duration: .5}, at + 1)
        .to(secs.map(x => x.r), {opacity: 1, x: 0, duration: .3, stagger: .12}, at + 1.2).to(wall, {opacity: .8, duration: .4}, at + 2);
      packs.forEach(({p, x}, i) => tl.set(p, {x: 470, y: x.yy + 17}, at + 2.4 + i * .5).to(p, {opacity: 1, duration: .2}, at + 2.4 + i * .5)
        .to(p, {x: 1205, y: 480 + i * 56, duration: 1.1, ease: "power2.inOut"}, at + 2.5 + i * .5));
      secs.filter(x => !x.ok).forEach((x, i) => tl.to(x.r, {opacity: .45, duration: .3}, at + 3.6 + i * .05));
    };
  };
  B.form = (g, s) => {             // ERP form fields fill themselves
    const H = header(g, s);
    const pk = card(g, 140, 290, 380, 330, {icon: "policy", label: s.package, fs: 24});
    const f = card(g, 780, 250, 680, 440, {});
    icon("erp", 840, 300, 40, C.signal, f);
    el("text", {x: 876, y: 310, "font-size": 26, "font-weight": 700, fill: "#fff", "font-family": FD}, f, s.erp);
    const fields = s.fields.map((fl, i) => { const yy = 350 + i * 78, r = el("g", {}, f);
      el("text", {x: 830, y: yy + 4, "font-size": 18, fill: C.muted, "font-family": FB}, r, fl[0]);
      el("rect", {x: 830, y: yy + 14, width: 580, height: 44, rx: 10, fill: "rgba(255,255,255,.07)", stroke: "rgba(255,255,255,.2)"}, r);
      const v = el("text", {x: 848, y: yy + 43, "font-size": 21, "font-weight": 600, fill: "#fff", "font-family": FB, "data-full": fl[1]}, r, "");
      const ok = icon("check", 1385, yy + 36, 24, C.signal, r); ok.setAttribute("opacity", 0);
      return {v, ok}; });
    const lanes = el("g", {opacity: 0}, g);
    el("path", {d: "M530 400 H770", stroke: C.signal, "stroke-width": 3.5, fill: "none", "marker-end": "url(#arr)"}, lanes);
    el("path", {d: "M770 520 H530", stroke: C.v2, "stroke-width": 3.5, fill: "none", "marker-end": "url(#arr)"}, lanes);
    el("text", {x: 650, y: 385, "text-anchor": "middle", "font-size": 19, "font-weight": 700, fill: C.signal, "font-family": FB}, lanes, s.push);
    el("text", {x: 650, y: 552, "text-anchor": "middle", "font-size": 19, "font-weight": 700, fill: "#9fb6ff", "font-family": FB}, lanes, s.pull);
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set([pk, f], {opacity: 0, y: 30});
      tl.to(pk, {opacity: 1, y: 0, duration: .5}, at + .8).to(f, {opacity: 1, y: 0, duration: .5}, at + 1).to(lanes, {opacity: 1, duration: .5}, at + 1.4);
      fields.forEach((x, i) => tl.add(typeIn(x.v, .5), at + 1.9 + i * .55).to(x.ok, {opacity: 1, duration: .2}, at + 2.4 + i * .55));
    };
  };
  B.swap = (g, s) => {             // one profile replaced, the project bar never stops
    const H = header(g, s), xs = row(3, 280, 40, 800);
    const cs = s.people.map((p, i) => card(g, xs[i], 270, 280, 230, {icon: "user", label: p, fs: 23}));
    const nw = card(g, xs[1], 270, 280, 230, {icon: "user", label: s.newcomer, fs: 23, stroke: C.signal, fill: "rgba(62,230,200,.12)"});
    el("rect", {x: 300, y: 580, width: 1000, height: 22, rx: 11, fill: "rgba(255,255,255,.1)"}, g);
    const bar = el("rect", {x: 300, y: 580, width: 0, height: 22, rx: 11, fill: C.signal}, g);
    el("text", {x: 300, y: 640, "font-size": 22, fill: C.muted, "font-family": FB}, g, s.bar);
    return (tl, at, d) => {
      hdrAnim(tl, H, s, at);
      gsap.set(cs, {opacity: 0, y: 30}); gsap.set(nw, {opacity: 0, y: -140});
      tl.to(cs, {opacity: 1, y: 0, duration: .45, stagger: .2, ease: "back.out(2)"}, at + .8)
        .to(bar, {attr: {width: 1000}, duration: Math.max(3, d - 1.5), ease: "none"}, at + 1)
        .to(cs[1], {opacity: 0, y: 140, duration: .6, ease: "power2.in"}, at + 2.2)
        .to(nw, {opacity: 1, y: 0, duration: .6, ease: "back.out(1.8)"}, at + 2.6)
        .to(nw._glow, {opacity: 1, duration: .2}, at + 3).to(nw._glow, {opacity: 0, duration: .6}, at + 3.4);
    };
  };
  B.close = (g, s) => {
    const halo = el("circle", {cx: 800, cy: 300, r: 190, fill: "url(#haloG)"}, g);
    const m = mark(800, 300, 170, g);
    el("text", {x: 800, y: 470, "text-anchor": "middle", "font-size": 50, "font-weight": 600, fill: "#fff", "font-family": FP, "letter-spacing": 18}, g, "VECTOR");
    el("text", {x: 800, y: 512, "text-anchor": "middle", "font-size": 18, "font-weight": 500, fill: C.muted, "font-family": FP, "letter-spacing": 12}, g, "CONSULTING");
    const tag = el("text", {x: 800, y: 610, "text-anchor": "middle", "font-size": s.text.length > 50 ? 36 : 42, "font-weight": 700, fill: C.signal, "font-family": FD, "data-full": s.text}, g, "");
    const url = el("text", {x: 800, y: 680, "text-anchor": "middle", "font-size": 24, fill: "#c7d3e8", "font-family": FB}, g, s.sub || "vectorconsultingltd.com");
    return (tl, at, d) => {
      gsap.set([halo, m], {opacity: 0, scale: .6, svgOrigin: "800 300"}); gsap.set(url, {opacity: 0});
      tl.to([halo, m], {opacity: 1, scale: 1, duration: .8, ease: "back.out(1.8)"}, at).add(typeIn(tag, Math.min(1.4, d * .4)), at + .7)
        .to(url, {opacity: 1, duration: .5}, at + 1.6);
      sweep(tl, m, at + 1.4);
    };
  };

  /* ---------- build the timeline from the scene list (starts come from the voice-over cut) */
  const N = V.scenes.length, starts = V.starts, total = V.total;
  const groups = V.scenes.map(() => el("g", {opacity: 0}, svg));
  svg.appendChild(brand);
  const tl = gsap.timeline({paused: true, defaults: {ease: "power3.out"}});
  V.scenes.forEach((s, i) => {
    const at = starts[i], d = (i < N - 1 ? starts[i + 1] : total) - at;
    tl.addLabel("s" + (i + 1), at);
    const sched = B[s.type](groups[i], s);
    tl.to(groups[i], {opacity: 1, duration: .35}, at);
    if (i > 0) tl.to(groups[i - 1], {opacity: 0, duration: .35}, at);
    sched(tl, at + .05, d);
  });
  tl.to({}, {duration: Math.max(0, total - tl.duration())});
  tl.addLabel("end", total);
  const labels = V.scenes.map((_, i) => starts[i]).concat(total);

  /* ---------- captions + controls */
  const cap = $("#cap"), sc = $("#scenes");
  V.scenes.forEach((s, i) => { const b = document.createElement("button"); b.type = "button"; b.innerHTML = `<b>${i + 1}</b><span>${s.chapter}</span><i></i>`;
    b.title = `${i + 1} · ${s.chapter}`; b.onclick = () => go(i); sc.appendChild(b); });
  const sbtn = $$(".scenes button");
  const cur = () => { const t = tl.time(); let k = 0; labels.forEach((l, i) => { if (i < N && t >= l - .001) k = i; }); return k; };
  let lastK = -1;
  function paint() {
    const t = tl.time(), k = cur();
    sbtn.forEach((b, i) => { b.classList.toggle("on", i === k); const a = labels[i], z = labels[i + 1];
      b.querySelector("i").style.width = (t >= z ? 100 : t <= a ? 0 : (t - a) / (z - a) * 100) + "%"; });
    if (k !== lastK) { lastK = k; cap.textContent = V.scenes[k].vo; }
    const playing = voice.on ? !au.paused : tl.isActive();
    $("#pi").setAttribute("d", playing ? "M7 5h4v14H7zM13 5h4v14h-4z" : "M8 5v14l11-7z");
    $("#play").title = playing ? T.pause : T.play; $("#play").setAttribute("aria-label", $("#play").title);
    document.body.classList.toggle("at-start", t < .01 && !playing);
    document.body.classList.toggle("at-end", t >= total - .05);
  }
  gsap.ticker.add(paint);

  /* voice-over: when enabled, the audio clock drives the timeline (timeline time == audio time) */
  const au = new Audio(V.audio || ""); au.preload = "none";
  const voice = {on: false};
  gsap.ticker.add(() => { if (voice.on && !au.paused) tl.seek(Math.min(au.currentTime, total), false); });
  au.onended = () => { tl.seek(au.duration, false); tl.play(); };
  function go(i) {
    i = Math.max(0, Math.min(N - 1, i));
    if (voice.on) { au.currentTime = labels[i]; tl.seek(labels[i], false); tl.pause(); au.play().catch(() => {}); }
    else { tl.seek(labels[i], false); tl.play(); }
  }
  function toggle() {
    const atEnd = tl.time() >= total - .05;
    if (voice.on) {
      if (atEnd || (au.ended)) { go(0); return; }
      if (au.paused) { tl.pause(); au.currentTime = Math.min(tl.time(), au.duration || tl.time()); au.play().catch(() => {}); } else au.pause();
      return;
    }
    if (atEnd) { go(0); return; }
    tl.isActive() ? tl.pause() : tl.play();
  }
  const vb = $("#voz-btn");
  const paintV = () => { vb.textContent = voice.on ? T.voiceOff : T.voiceOn; vb.setAttribute("aria-pressed", voice.on); };
  vb.onclick = e => {
    e.stopPropagation();
    if (!voice.on) { voice.on = true; tl.pause(); au.preload = "auto"; au.currentTime = Math.min(tl.time(), total); au.play().catch(() => {}); }
    else { voice.on = false; au.pause(); tl.play(); }
    paintV();
  };
  paintV();
  if (!V.audio) vb.hidden = true;
  $("#play").onclick = toggle; $("#start span").onclick = toggle;
  $("#next").onclick = () => go(cur() + 1); $("#prev").onclick = () => { const k = cur(); go(tl.time() - labels[k] < 1 ? k - 1 : k); };
  $("#replay").onclick = () => go(0);
  $("#wrap").addEventListener("click", toggle);
  const close = () => { try { window.parent.postMessage({vector: "cerrar"}, "*"); } catch (e) {} au.pause(); };
  $("#close").onclick = e => { e.stopPropagation(); close(); };
  if (window.parent === window) $("#close").hidden = true;
  ["prev", "next", "replay", "close"].forEach(id => { const b = $("#" + id); b.title = T[id]; b.setAttribute("aria-label", T[id]); });
  $("#start span").textContent = T.start;
  document.addEventListener("keydown", e => {
    if (e.key === " ") { e.preventDefault(); toggle(); }
    else if (e.key === "ArrowRight") $("#next").onclick();
    else if (e.key === "ArrowLeft") $("#prev").onclick();
    else if (e.key === "Escape") close();
    else if (/^[1-9]$/.test(e.key) && +e.key <= N) go(+e.key - 1);
  });
  if (window.parent !== window) {
    let armed = false;
    gsap.ticker.add(() => { const t = tl.time(); if (t > .5 && t < total - 1) armed = true; if (armed && t >= total - .05) { armed = false; try { window.parent.postMessage({vector: "fin"}, "*"); } catch (e) {} } });
  }

  /* reduced motion: show each scene complete, no movement; captions and chapters still work */
  if (reduced) {
    document.body.classList.add("reduced"); $(".rm-note").textContent = T.reduced;
    tl.seek(labels[1] - .01, false);
    go = i => { tl.seek(Math.max(0, (labels[i + 1] || total) - .05), false); if (voice.on) { au.currentTime = labels[i]; au.play().catch(() => {}); } };
    sbtn.forEach((b, i) => b.onclick = () => go(i));
    tl.seek(labels[1] - .05, false);
  } else if (q.get("render")) {
    window.__tl = tl;                 // used to export MP4 frames
  } else if (q.get("voz") === "1" && V.audio) {
    /* opened from the website by a click: start with the voice-over; if the browser blocks audio, play silently */
    document.fonts.ready.then(() => setTimeout(() => {
      voice.on = true; au.preload = "auto"; au.currentTime = 0; paintV();
      au.play().catch(() => { voice.on = false; paintV(); tl.play(); });
    }, 250));
  } else if (q.get("auto") !== "0") {
    document.fonts.ready.then(() => setTimeout(() => tl.play(), 250));
  }
  window.VXtl = tl;
})();
