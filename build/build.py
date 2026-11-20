# -*- coding: utf-8 -*-
"""Static site generator for vectorconsultingltd.com. Run: python3 build.py -> ../site"""
import os, json, html, shutil, datetime
from content import *

SITE = "https://www.vectorconsultingltd.com"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
E = html.escape

ICON = {
 "code":'<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>',
 "team":'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 2 6 5.5"/>',
 "ai":'<rect x="5" y="5" width="14" height="14" rx="3"/><path d="M9 1v4M15 1v4M9 19v4M15 19v4M1 9h4M1 15h4M19 9h4M19 15h4M9.5 15l2.5-6 2.5 6M10.3 13h3.4"/>',
 "compass":'<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "health":'<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 10c0 6-8 11-8 11z"/><path d="M8 12h2.5l1-2 2 4 1-2H16"/>',
 "procure":'<path d="M4 4h16v16H4z"/><path d="M8 9h8M8 13h8M8 17h5"/>',
 "chip":'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 2v4M14 2v4M10 18v4M14 18v4M2 10h4M2 14h4M18 10h4M18 14h4"/>',
 "factory":'<path d="M3 21V10l6 3V10l6 3V6h6v15z"/><path d="M7 17h2M11 17h2M15 17h2"/>',
 "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
 "check":'<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "pin":'<path d="M12 21s-7-6.2-7-11.5a7 7 0 0114 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
}
def icon(n, cls="ic"): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICON[n]}</svg>'

def LOGO_SVG(u):
    """Vector mark: two overlapping capsules forming a V, with an animated light sweep (CSS in site.css)."""
    L = '<rect x="17" y="2.75" width="16" height="56.5" rx="8" transform="rotate(-20.2 25 31)"/>'
    R = '<rect x="31" y="2.75" width="16" height="56.5" rx="8" transform="rotate(20.2 39 31)"/>'
    return (f'<svg class="logo-mark" viewBox="0 0 64 64" aria-hidden="true"><defs>'
            f'<clipPath id="vl-{u}">{L}</clipPath><clipPath id="va-{u}">{L}{R}</clipPath>'
            f'<linearGradient id="vs-{u}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
            f'{L.replace("/>"," fill=\"#4a72ff\"/>")}{R.replace("/>"," fill=\"#2f5bff\"/>")}'
            f'<g clip-path="url(#vl-{u})">{R.replace("/>"," fill=\"#1b39b8\"/>")}</g>'
            f'<g clip-path="url(#va-{u})"><rect class="logo-sweep" x="-6" y="-4" width="14" height="72" fill="url(#vs-{u})"/></g>'
            f'<path class="logo-spark" d="M51 0 L52.5 4.5 L57 6 L52.5 7.5 L51 12 L49.5 7.5 L45 6 L49.5 4.5 Z" fill="#fff"/></svg>')
BRAND_TXT = '<span class="brand-txt"><span class="w1">VECTOR</span><span class="w2">CONSULTING</span></span>'


def url(key, lang): return PATHS[key][0 if lang=="en" else 1]

def head(lang, key, title, desc, extra_ld=None):
    en, es = PATHS[key]
    canon = SITE + url(key, lang)
    ld = {"@context":"https://schema.org","@type":"ProfessionalService","name":"Vector Consulting Limited",
          "url":SITE+"/","logo":SITE+"/assets/logo.png","email":EMAIL,"image":SITE+"/assets/og.png",
          "description":"Hong Kong technology consultancy: software engineering, dedicated teams, applied AI and federated data spaces for companies in Europe and Asia.",
          "address":{"@type":"PostalAddress","streetAddress":"Rooms 1705-1709, 17/F, Tung Chiu Commercial Centre, 193 Lockhart Road","addressLocality":"Wanchai","addressRegion":"Hong Kong","addressCountry":"HK"},
          "areaServed":["Europe","Asia"],"knowsAbout":["Software engineering","Artificial intelligence","Data spaces","Gaia-X","IDSA","GDPR","EU AI Act"]}
    lds = [ld] + ([extra_ld] if extra_ld else [])
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{SITE}{en}">
<link rel="alternate" hreflang="es" href="{SITE}{es}">
<link rel="alternate" hreflang="x-default" href="{SITE}{en}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vector Consulting">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:locale" content="{'en_GB' if lang=='en' else 'es_ES'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1526">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts.css">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{json.dumps(lds if len(lds)>1 else ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{UI[lang]["skip"]}</a>
'''

def header(lang, key):
    u = UI[lang]
    other = "es" if lang=="en" else "en"
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{url(k,lang)}"{cur if k==key else ""}>{E(l)}</a>' for k,l in u["nav"])
    if key not in PATHS: key = "home"
    return f'''<header class="top">
 <div class="wrap bar">
  <a class="brand" href="{url("home",lang)}" aria-label="Vector Consulting">{LOGO_SVG("h")}{BRAND_TXT}</a>
  <button class="menu" aria-expanded="false" aria-controls="nav" type="button"><span></span><span></span><span class="sr">Menu</span></button>
  <nav id="nav" aria-label="Main">{nav}
   <a class="lang" href="{url(key,other)}" hreflang="{other}" lang="{other}">{u["lang"]}</a>
   <a class="btn btn-sm" href="{url("contact",lang)}">{u["cta"]}</a>
  </nav>
 </div>
</header>
<main id="main">
'''

def cta_band(lang):
    u = UI[lang]
    return f'''<section class="band cta-band"><div class="wrap cta-in">
 <div><h2>{u["cta_title"]}</h2><p>{u["cta_text"]}</p></div>
 <div class="cta-actions"><a class="btn btn-light" href="{url("contact",lang)}">{u["cta"]} {icon("arrow")}</a>
 <a class="mail" href="mailto:{EMAIL}">{icon("mail")} {EMAIL}</a></div>
</div></section>
'''

def footer(lang):
    u = UI[lang]
    t = {"en":("Services","AI & Data","How we work","Industries","Case studies","Insights","About","Careers","Contact"),
         "es":("Servicios","IA y Datos","Cómo trabajamos","Sectores","Casos de éxito","Perspectivas","Quiénes somos","Empleo","Contacto")}[lang]
    year = datetime.date.today().year
    lg = {"en":("Legal notice","Privacy","Cookies"),"es":("Aviso legal","Privacidad","Cookies")}[lang]
    return f'''</main>
<footer class="foot"><div class="wrap">
 <div class="foot-grid">
  <div class="foot-brand"><a class="brand brand-light" href="{url("home",lang)}" aria-label="Vector Consulting">{LOGO_SVG("f")}{BRAND_TXT}</a><p>{u["footer_tag"]}</p></div>
  <div><h3>{u["f_services"]}</h3><a href="{url("services",lang)}">{t[0]}</a><a href="{url("ai",lang)}">{t[1]}</a><a href="{url("how",lang)}">{t[2]}</a><a href="{url("industries",lang)}">{t[3]}</a></div>
  <div><h3>{u["f_company"]}</h3><a href="{url("cases",lang)}">{t[4]}</a><a href="{url("insights",lang)}">{t[5]}</a><a href="{url("about",lang)}">{t[6]}</a><a href="{url("careers",lang)}">{t[7]}</a></div>
  <div><h3>{u["f_contact"]}</h3><a href="mailto:{EMAIL}">{EMAIL}</a><p class="addr">{icon("pin")}<span>Vector Consulting Limited<br>{E(ADDRESS)}</span></p></div>
 </div>
 <div class="legal"><span>© {year} Vector Consulting Limited · {u["brn"]} {BRN} · {u["rights"]}</span><span class="legal-links"><a href="{url("legal",lang)}">{lg[0]}</a> · <a href="{url("privacy",lang)}">{lg[1]}</a> · <a href="{url("cookies",lang)}">{lg[2]}</a></span></div>
</div></footer>
<script src="/assets/site.js" defer></script>
</body></html>
'''

def page_hero(kicker, title, lead, small=False):
    return f'''<section class="phero{' phero-sm' if small else ''}"><canvas class="field" aria-hidden="true"></canvas><div class="wrap">
 <p class="kicker">{E(kicker)}</p><h1>{title}</h1><p class="lead">{E(lead)}</p>
</div></section>
'''

def svc_cards(lang, detail=False):
    out = []
    for ic, t, d, bullets in SERVICES[lang]:
        b = "".join(f"<li>{icon('check','ck')}{E(x)}</li>" for x in bullets) if detail else ""
        out.append(f'<article class="card svc">{icon(ic)}<h3>{E(t)}</h3><p>{E(d)}</p>{"<ul class=checks>"+b+"</ul>" if detail else ""}</article>')
    return '<div class="grid g4">' + "".join(out) + "</div>"


# ---------------- animated explainer videos ----------------
import videos as VIDS
VT = {"en": dict(sec=("See it in under a minute", "Four short animated explainers on who we are and what we have built."), watch="Watch the video", play="Play video", tx="Transcript", sec_k="Videos",
                 cases={1: "v02", 2: "v03", 3: "v04"}, case_btn="Watch the {d}-second video"),
      "es": dict(sec=("Míralo en menos de un minuto", "Cuatro vídeos animados breves sobre quiénes somos y lo que hemos construido."), watch="Ver el vídeo", play="Reproducir vídeo", tx="Transcripción", sec_k="Vídeos",
                 cases={1: "v02", 2: "v03", 3: "v04"}, case_btn="Ver el vídeo de {d} segundos")}

def vid_url(vid, lang): return f"/videos/{vid}/" + ("es/" if lang == "es" else "") + "?voz=1"
def vid_secs(vid, lang):
    tm = VIDS.timing().get(f"{vid}-{lang}")
    t = tm["total"] if tm else VIDS.estimate(VIDS.VIDEOS[vid][lang]["scenes"])[1]
    return int(round(t / 5.0) * 5)
def vid_transcript(vid, lang):
    return " ".join(s["vo"] for s in VIDS.VIDEOS[vid][lang]["scenes"])

def video_gallery(lang):
    out = []
    for vid in VIDS.ORDER:
        v = VIDS.VIDEOS[vid][lang]
        out.append(f'''<button class="card vcard" type="button" data-video="{vid_url(vid, lang)}" aria-label="{VT[lang]["play"]}: {E(v["title"])}">
 <span class="vthumb"><img src="/videos/{vid}/poster-{lang}.webp" alt="" loading="lazy" width="640" height="360"><span class="vplay" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span><span class="vdur">{vid_secs(vid, lang)} s</span></span>
 <h3>{E(v["title"])}</h3><p>{E(v["desc"])}</p></button>''')
    note = {"en":"Voice-over generated with AI (ElevenLabs). Captions and transcripts available.","es":"Locución generada con IA (ElevenLabs). Con subtítulos y transcripción."}[lang]
    return '<div class="grid g4 vgrid">' + "".join(out) + f'</div><p class="vnote">{note}</p>'

def case_video(i, lang):
    vid = VT[lang]["cases"].get(i)
    if not vid: return ""
    return (f'<div class="case-video"><button class="btn btn-sm" type="button" data-video="{vid_url(vid, lang)}">'
            f'<svg viewBox="0 0 24 24" class="ic" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor" stroke="none"/></svg> {VT[lang]["case_btn"].format(d=vid_secs(vid, lang))}</button>'
            f'<details class="tx"><summary>{VT[lang]["tx"]}</summary><p>{E(vid_transcript(vid, lang))}</p></details></div>')

def case_cards(lang, full=False):
    L = {"en":("Client","Sector","Challenge","What we did","Outcome"),"es":("Cliente","Sector","Reto","Qué hicimos","Resultado")}[lang]
    out=[]
    for i,c in enumerate(CASES[lang]):
        tags="".join(f'<span class="tag">{E(t)}</span>' for t in c["tags"])
        if full:
            out.append(f'''<article class="case-full" id="case-{i+1}">
 <div class="case-meta"><p class="num">0{i+1}</p><dl><dt>{L[0]}</dt><dd>{E(c["client"])}</dd><dt>{L[1]}</dt><dd>{E(c["sector"])}</dd></dl><div class="tags">{tags}</div></div>
 <div class="case-body"><h2>{E(c["title"])}</h2>
  {case_video(i+1, lang)}<h3>{L[2]}</h3><p>{E(c["challenge"])}</p><h3>{L[3]}</h3><p>{E(c["work"])}</p><h3>{L[4]}</h3><p>{E(c["result"])}</p></div>
</article>''')
        else:
            out.append(f'<a class="card case" href="{url("cases",lang)}#case-{i+1}"><p class="eyebrow">{E(c["sector"])} · {E(c["client"])}</p><h3>{E(c["title"])}</h3><p>{E(c["result"])}</p><div class="tags">{tags}</div><span class="more">{UI[lang]["read"]} {icon("arrow")}</span></a>')
    return ("".join(out)) if full else '<div class="grid g3">'+"".join(out)+"</div>"

def industry_cards(lang):
    return '<div class="grid g4">' + "".join(f'<article class="card ind">{icon(ic)}<h3>{E(t)}</h3><p>{E(d)}</p></article>' for ic,t,d in INDUSTRIES[lang]) + "</div>"

def process(lang):
    return '<ol class="steps">' + "".join(f'<li><span class="sn">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i,(t,d) in enumerate(PROCESS[lang])) + "</ol>"

def models(lang):
    return '<div class="grid g4">' + "".join(f'<article class="card model"><p class="eyebrow">{E(s)}</p><h3>{E(t)}</h3><p>{E(d)}</p></article>' for t,s,d in MODELS[lang]) + "</div>"

def article_cards(lang):
    out=[]
    for k in ("art-ai","art-ds","art-act"):
        a=ARTICLES[k]; t,ex,_=a[lang]
        d=datetime.date.fromisoformat(a["date"])
        ds=d.strftime("%d %b %Y") if lang=="en" else f'{d.day} {["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"][d.month-1]} {d.year}'
        out.append(f'<a class="card art" href="{url(k,lang)}"><p class="eyebrow">{ds} · {a["mins"]} {UI[lang]["min"]}</p><h3>{E(t)}</h3><p>{E(ex)}</p><span class="more">{UI[lang]["read"]} {icon("arrow")}</span></a>')
    return '<div class="grid g3">'+"".join(out)+"</div>"

def sec(title, intro, body, kicker="", cls=""):
    k = f'<p class="kicker">{E(kicker)}</p>' if kicker else ""
    i = f'<p class="intro">{E(intro)}</p>' if intro else ""
    return f'<section class="sec {cls}"><div class="wrap"><div class="sh">{k}<h2>{title}</h2>{i}</div>{body}</div></section>\n'

# ---------------- pages ----------------
def home(lang):
    T = {"en":dict(
      title="Vector Consulting · Software, AI and data engineering",
      desc="Hong Kong technology consultancy delivering senior engineering teams, applied AI and federated data spaces to companies across Europe and Asia.",
      kicker="Technology consultancy · Hong Kong · Europe",
      h1="Software engineering, AI and data for companies that <em>build to scale</em>",
      lead="Senior engineering teams and expert advice for companies in Europe and Asia. From idea to production, with one accountable partner.",
      b2="See our work", stats=[("2","European data spaces built or advised"),("4","engagement models, combinable"),("3","countries with delivery capacity"),("2","continents, one accountable team")],
      s1=("What we do","Strategic technology advice combined with senior engineering capacity."), s2=("Why companies choose Vector",""),
      s3=("Selected work","European federated data spaces in regulated sectors, from architecture to production."),
      s4=("Industries we serve","Particular depth in regulated, data-intensive markets."),
      s5=("How we deliver","A disciplined process with named people and transparent reporting."),
      s6=("Insights","Short perspectives on the questions our clients ask most."),
      trust="Standards and frameworks we build with"),
     "es":dict(
      title="Vector Consulting · Ingeniería de software, IA y datos",
      desc="Consultora tecnológica de Hong Kong que aporta equipos de ingeniería senior, IA aplicada y espacios de datos federados a empresas de Europa y Asia.",
      kicker="Consultora tecnológica · Hong Kong · Europa",
      h1="Ingeniería de software, IA y datos para empresas que <em>construyen para crecer</em>",
      lead="Equipos de ingeniería senior y asesoramiento experto para empresas de Europa y Asia. De la idea a producción, con un único socio responsable.",
      b2="Ver nuestro trabajo", stats=[("2","espacios de datos europeos construidos o asesorados"),("4","modelos de colaboración, combinables"),("3","países con capacidad de entrega"),("2","continentes, un único equipo responsable")],
      s1=("Qué hacemos","Asesoramiento tecnológico estratégico unido a capacidad de ingeniería senior."), s2=("Por qué nos eligen",""),
      s3=("Trabajo destacado","Espacios de datos federados europeos en sectores regulados, de la arquitectura a producción."),
      s4=("Sectores","Especial experiencia en mercados regulados e intensivos en datos."),
      s5=("Cómo trabajamos","Un proceso riguroso, con personas con nombre e informes transparentes."),
      s6=("Perspectivas","Reflexiones breves sobre las preguntas que más nos hacen nuestros clientes."),
      trust="Estándares y marcos con los que trabajamos")}[lang]
    stats="".join(f'<div class="stat"><strong>{E(n)}</strong><span>{E(l)}</span></div>' for n,l in T["stats"])
    why="".join(f'<div class="why"><span class="dot"></span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t,d in WHY[lang])
    logos="".join(f"<span>{x}</span>" for x in ["Gaia-X","IDSA","Pontus-X","ODRL","GDPR","EU AI Act","EHDS"])
    body = f'''<section class="hero"><canvas class="field" aria-hidden="true"></canvas><div class="wrap hero-in">
 <p class="kicker">{E(T["kicker"])}</p><h1>{T["h1"]}</h1><p class="lead">{E(T["lead"])}</p>
 <div class="hero-cta"><a class="btn" href="{url("contact",lang)}">{UI[lang]["cta"]} {icon("arrow")}</a><a class="btn btn-ghost" href="{url("cases",lang)}">{E(T["b2"])}</a></div>
 <div class="stats">{stats}</div>
</div></section>
<section class="trust"><div class="wrap"><p>{E(T["trust"])}</p><div class="logos">{logos}</div></div></section>
'''
    body += sec(VT[lang]["sec"][0], VT[lang]["sec"][1], video_gallery(lang), kicker=VT[lang]["sec_k"], cls="tint vsec")
    body += sec(T["s1"][0], T["s1"][1], svc_cards(lang))
    body += f'<section class="sec dark"><div class="wrap split"><div class="sh"><h2>{T["s2"][0]}</h2></div><div class="whys">{why}</div></div></section>\n'
    body += sec(T["s3"][0], T["s3"][1], case_cards(lang))
    body += sec(T["s4"][0], T["s4"][1], industry_cards(lang), cls="tint")
    body += sec(T["s5"][0], T["s5"][1], process(lang))
    body += sec(T["s6"][0], T["s6"][1], article_cards(lang), cls="tint")
    return T["title"], T["desc"], body

def services(lang):
    T={"en":("Services · Vector Consulting","Software engineering, dedicated teams, AI and data, and technology consulting: end-to-end services from strategy to production.","Services","End-to-end technology services, <em>from strategy to production</em>","Four practices that work together, so you can start with one and add the others as your needs grow.","Engagement models","Choose the model that fits your stage, budget and level of control, and combine them as needs evolve."),
       "es":("Servicios · Vector Consulting","Ingeniería de software, equipos dedicados, IA y datos, y consultoría tecnológica: servicios integrales de la estrategia a producción.","Servicios","Servicios tecnológicos integrales, <em>de la estrategia a producción</em>","Cuatro prácticas que trabajan juntas: puedes empezar por una y sumar las demás a medida que crecen tus necesidades.","Modelos de colaboración","Elige el modelo que encaja con tu fase, presupuesto y nivel de control, y combínalos según evolucionen tus necesidades.")}[lang]
    body = page_hero(T[2], T[3], T[4]) + sec("", "", svc_cards(lang, True)).replace('<div class="sh"><h2></h2></div>','') + sec(T[5], T[6], models(lang), cls="tint")
    return T[0],T[1],body

def ai(lang):
    T={"en":dict(t="AI & Data · Vector Consulting",d="Applied AI and trusted data infrastructure designed for European standards: GDPR, EU AI Act, Gaia-X and IDSA data spaces.",k="AI & Data",h="Applied AI and trusted data, <em>built for European standards</em>",l="From first use case to production, we help you adopt AI and data responsibly and at scale.",
        cap=[("Applied AI","Document understanding, assistants and decision support built on your real data, evaluated against a measurable baseline."),("Sovereign AI","Open-weight models running in your cloud tenant or on-premise, so sensitive data never leaves your control."),("Data platforms","Pipelines, warehouses and APIs that turn scattered data into a reliable, documented asset."),("Federated data spaces","Connectors, usage policies (ODRL), identity and trust lists on Gaia-X, IDSA and Pontus-X principles."),("Governance & compliance","GDPR, EU AI Act and EHDS requirements translated into architecture, logging and human oversight."),("MLOps","Monitoring, evaluation and versioning so models keep performing after go-live.")],
        s1="Capabilities",s2="Our approach",ap=[("Start from a decision","We pick one concrete business decision and the data it needs, which keeps scope and privacy review small."),("Bring the model to the data","Where data cannot travel, we deploy the model next to it."),("Design governance in","Logging, evaluation and human oversight are part of the architecture."),("Measure, then scale","Every pilot has a baseline, a target and an owner before it grows.")]),
       "es":dict(t="IA y Datos · Vector Consulting",d="IA aplicada e infraestructura de datos de confianza para los estándares europeos: RGPD, Reglamento de IA, espacios de datos Gaia-X e IDSA.",k="IA y Datos",h="IA aplicada y datos de confianza, <em>pensados para Europa</em>",l="Del primer caso de uso a producción, te ayudamos a adoptar la IA y los datos de forma responsable y a escala.",
        cap=[("IA aplicada","Comprensión de documentos, asistentes y apoyo a la decisión sobre tus datos reales, evaluados frente a una línea base medible."),("IA soberana","Modelos de pesos abiertos en tu nube o en tus instalaciones, para que los datos sensibles nunca salgan de tu control."),("Plataformas de datos","Pipelines, almacenes y APIs que convierten datos dispersos en un activo fiable y documentado."),("Espacios de datos federados","Conectores, políticas de uso (ODRL), identidad y listas de confianza según Gaia-X, IDSA y Pontus-X."),("Gobernanza y cumplimiento","Requisitos del RGPD, el Reglamento de IA y el EHDS traducidos a arquitectura, registros y supervisión humana."),("MLOps","Monitorización, evaluación y versionado para que los modelos sigan rindiendo tras la puesta en producción.")],
        s1="Capacidades",s2="Nuestro enfoque",ap=[("Partir de una decisión","Elegimos una decisión concreta del negocio y los datos que necesita, lo que limita el alcance y la revisión de privacidad."),("Llevar el modelo a los datos","Si los datos no pueden viajar, desplegamos el modelo junto a ellos."),("Gobernanza desde el diseño","Registros, evaluación y supervisión humana forman parte de la arquitectura."),("Medir y después escalar","Cada piloto tiene línea base, objetivo y responsable antes de crecer.")])}[lang]
    caps='<div class="grid g3">'+"".join(f'<article class="card"><h3>{E(a)}</h3><p>{E(b)}</p></article>' for a,b in T["cap"])+"</div>"
    ap='<ol class="steps">'+"".join(f'<li><span class="sn">{i+1:02d}</span><h3>{E(a)}</h3><p>{E(b)}</p></li>' for i,(a,b) in enumerate(T["ap"]))+"</ol>"
    body=page_hero(T["k"],T["h"],T["l"])+sec(T["s1"],"",caps)+sec(T["s2"],"",ap,cls="tint")
    return T["t"],T["d"],body

def how(lang):
    T={"en":("How we work · Vector Consulting","Clear engagement models, senior people and disciplined delivery: discover, design, build, run.","How we work","Clear models, senior people, <em>disciplined delivery</em>","Every engagement starts with a clear scope, named people and transparent commercial terms.","Our delivery process","Engagement models"),
       "es":("Cómo trabajamos · Vector Consulting","Modelos de colaboración claros, personas senior y ejecución rigurosa: descubrir, diseñar, construir y operar.","Cómo trabajamos","Modelos claros, personas senior, <em>ejecución rigurosa</em>","Cada proyecto empieza con un alcance claro, personas con nombre y condiciones comerciales transparentes.","Nuestro proceso","Modelos de colaboración")}[lang]
    body=page_hero(T[2],T[3],T[4])+sec(T[5],"",process(lang))+sec(T[6],"",models(lang),cls="tint")
    return T[0],T[1],body

def industries(lang):
    T={"en":("Industries · Vector Consulting","Sector expertise for regulated, data-intensive markets: healthcare, procurement and public sector, technology companies and industrial data spaces.","Industries","Sector expertise for <em>regulated, data-intensive</em> markets","We have delivered platforms where data protection, interoperability and auditability are requirements, not options."),
       "es":("Sectores · Vector Consulting","Experiencia sectorial en mercados regulados e intensivos en datos: salud, compras y sector público, empresas tecnológicas y espacios de datos industriales.","Sectores","Experiencia en mercados <em>regulados e intensivos en datos</em>","Hemos entregado plataformas donde la protección de datos, la interoperabilidad y la auditabilidad son requisitos, no opciones.")}[lang]
    body=page_hero(T[2],T[3],T[4])+sec("","",industry_cards(lang)).replace('<div class="sh"><h2></h2></div>','')
    return T[0],T[1],body

def cases(lang):
    T={"en":("Case studies · Vector Consulting","Selected engagements: Global Data Care federated health data space, PROCUREDATA procurement data space and senior specialists for Spanish technology companies.","Case studies","Selected <em>engagements</em>","Technology work for companies in Spain and across Europe."),
       "es":("Casos de éxito · Vector Consulting","Proyectos destacados: espacio de datos de salud Global Data Care, espacio de datos de compras PROCUREDATA y especialistas senior para empresas españolas.","Casos de éxito","Proyectos <em>destacados</em>","Trabajo tecnológico para empresas de España y del resto de Europa.")}[lang]
    body=page_hero(T[2],T[3],T[4])+f'<section class="sec"><div class="wrap cases">{case_cards(lang,True)}</div></section>'
    return T[0],T[1],body

def insights(lang):
    T={"en":("Insights · Vector Consulting","Perspectives on software, AI and data across Europe and Asia: AI with control over data, data spaces in production, the EU AI Act.","Insights","Perspectives on software, <em>AI and data</em>","Short pieces from our team on the questions our clients ask most often."),
       "es":("Perspectivas · Vector Consulting","Reflexiones sobre software, IA y datos en Europa y Asia: IA con control de los datos, espacios de datos en producción, Reglamento Europeo de IA.","Perspectivas","Reflexiones sobre software, <em>IA y datos</em>","Textos breves de nuestro equipo sobre las preguntas que más nos hacen nuestros clientes.")}[lang]
    body=page_hero(T[2],T[3],T[4])+sec("","",article_cards(lang)).replace('<div class="sh"><h2></h2></div>','')
    return T[0],T[1],body

def about(lang):
    T={"en":dict(t="About · Vector Consulting",d="Vector Consulting Limited is a Hong Kong technology consultancy connecting Asia and Europe, with senior engineering teams in several countries.",k="About us",h="A technology partner <em>connecting Asia and Europe</em>",l="We help companies design, build and run software, AI and data solutions, combining strategic advice with senior engineering teams.",
        who="Who we are",wt=["Vector Consulting Limited is a technology consultancy registered in Hong Kong. Our work is concentrated in regulated, data-intensive sectors where security, compliance and reliability are not optional.","Our mission is to give ambitious companies access to senior technology expertise with the flexibility, transparency and accountability of a long-term partner.","We work with senior technicians in several countries, including specialists in London through Technova Corp Ltd, to give clients the right expertise wherever it is."],
        v="Our values",ld="Leadership",fa=[("Registered in","Hong Kong"),("Business Reg. No.",BRN),("Delivery","Spain · UK · Hong Kong"),("Focus","Software · AI · Data spaces")]),
       "es":dict(t="Quiénes somos · Vector Consulting",d="Vector Consulting Limited es una consultora tecnológica de Hong Kong que conecta Asia y Europa, con equipos de ingeniería senior en varios países.",k="Quiénes somos",h="Un socio tecnológico <em>que conecta Asia y Europa</em>",l="Ayudamos a las empresas a diseñar, construir y operar soluciones de software, IA y datos, combinando asesoramiento estratégico con equipos de ingeniería senior.",
        who="Quiénes somos",wt=["Vector Consulting Limited es una consultora tecnológica registrada en Hong Kong. Nuestro trabajo se concentra en sectores regulados e intensivos en datos, donde la seguridad, el cumplimiento y la fiabilidad no son opcionales.","Nuestra misión es dar a las empresas ambiciosas acceso a experiencia tecnológica senior con la flexibilidad, la transparencia y la responsabilidad de un socio a largo plazo.","Trabajamos con técnicos senior en varios países, incluidos especialistas en Londres a través de Technova Corp Ltd, para ofrecer a cada cliente la experiencia adecuada esté donde esté."],
        v="Nuestros valores",ld="Dirección",fa=[("Registrada en","Hong Kong"),("Nº Registro Mercantil",BRN),("Entrega","España · Reino Unido · Hong Kong"),("Foco","Software · IA · Espacios de datos")])}[lang]
    facts="".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a,b in T["fa"])
    who=f'<div class="split2"><div class="prose">{"".join(f"<p>{E(p)}</p>" for p in T["wt"])}</div><dl class="facts">{facts}</dl></div>'
    vals='<div class="grid g4">'+"".join(f'<article class="card val"><h3>{E(a)}</h3><p>{E(b)}</p></article>' for a,b in VALUES[lang])+"</div>"
    leaders='<div class="grid g3">'+"".join(f'<article class="card person"><span class="avatar">{"".join(w[0] for w in n.split()[:2])}</span><h3>{E(n)}</h3><p class="role">{E(r)}</p><p>{E(b)}</p></article>' for n,r,b in LEADERS[lang])+"</div>"
    body=page_hero(T["k"],T["h"],T["l"])+sec(T["who"],"",who)+sec(T["v"],"",vals,cls="tint")+sec(T["ld"],"",leaders)
    return T["t"],T["d"],body

def careers(lang):
    T={"en":dict(t="Careers · Vector Consulting",d="Work with senior engineers on meaningful projects across Europe and Asia. Remote-friendly roles in software, cloud, data and AI.",k="Careers",h="Work with senior engineers on <em>meaningful projects</em>",l="Regulated, data-intensive projects across Europe and Asia, with people who care about doing them well.",
        why="Why join Vector",wy=[("Real responsibility","You own meaningful parts of production systems, not tickets in isolation."),("European frontier work","Data spaces, sovereign AI and compliance-heavy platforms that few teams get to build."),("Flexible and international","Remote-friendly work with colleagues in Spain, the UK and Hong Kong.")],
        pr="Profiles we look for",ap="How to apply",at="Send your CV and a short note about the projects you are most proud of to"),
       "es":dict(t="Empleo · Vector Consulting",d="Trabaja con ingenieros senior en proyectos con sentido en Europa y Asia. Puestos con trabajo en remoto en software, cloud, datos e IA.",k="Empleo",h="Trabaja con ingenieros senior en <em>proyectos con sentido</em>",l="Proyectos regulados e intensivos en datos en Europa y Asia, con personas a las que les importa hacerlos bien.",
        why="Por qué Vector",wy=[("Responsabilidad real","Te ocupas de partes relevantes de sistemas en producción, no de tareas aisladas."),("Proyectos europeos punteros","Espacios de datos, IA soberana y plataformas con alto nivel de cumplimiento que pocos equipos llegan a construir."),("Flexible e internacional","Trabajo en remoto con compañeros en España, Reino Unido y Hong Kong.")],
        pr="Perfiles que buscamos",ap="Cómo presentar tu candidatura",at="Envía tu CV y una breve nota sobre los proyectos de los que estás más orgulloso/a a")}[lang]
    wy='<div class="grid g3">'+"".join(f'<article class="card"><h3>{E(a)}</h3><p>{E(b)}</p></article>' for a,b in T["wy"])+"</div>"
    roles='<ul class="roles">'+"".join(f"<li>{icon('check','ck')}{E(r)}</li>" for r in ROLES[lang])+"</ul>"
    apply=f'<div class="apply"><p>{E(T["at"])}</p><a class="btn" href="mailto:{EMAIL}?subject=Careers">{icon("mail")} {EMAIL}</a></div>'
    body=page_hero(T["k"],T["h"],T["l"])+sec(T["why"],"",wy)+sec(T["pr"],"",roles,cls="tint")+sec(T["ap"],"",apply)
    return T["t"],T["d"],body

def contact(lang):
    T={"en":dict(t="Contact · Vector Consulting",d="Tell us about your project. Vector Consulting will come back to you with a clear next step.",k="Contact",h="Tell us about <em>your project</em>",l="We will come back to you with a clear next step.",
        f=("Your name","Company","Email","What would you like to discuss?","Send message"),note="We use your data only to answer your enquiry. See our <a href=\"/privacy/\">privacy policy</a>.",ok="Thank you. Your message has been sent; we will reply shortly.",err="We could not send the form. Please write to us directly at",
        nx="What happens next",steps=["We read your message and reply with questions or a proposed call.","A short call with a senior consultant to understand your goals.","A written proposal: scope, team, timeline and cost."],o="Office"),
       "es":dict(t="Contacto · Vector Consulting",d="Cuéntanos tu proyecto. Vector Consulting te responderá con un siguiente paso claro.",k="Contacto",h="Cuéntanos <em>tu proyecto</em>",l="Te responderemos con un siguiente paso claro.",
        f=("Tu nombre","Empresa","Email","¿De qué te gustaría hablar?","Enviar mensaje"),note="Usamos tus datos solo para responder a tu consulta. Consulta nuestra <a href=\"/es/privacidad/\">política de privacidad</a>.",ok="Gracias. Tu mensaje se ha enviado; te responderemos en breve.",err="No hemos podido enviar el formulario. Escríbenos directamente a",
        nx="Qué pasa después",steps=["Leemos tu mensaje y te respondemos con preguntas o una propuesta de llamada.","Una llamada breve con un consultor senior para entender tus objetivos.","Una propuesta por escrito: alcance, equipo, plazos y coste."],o="Oficina")}[lang]
    f=T["f"]
    steps="".join(f"<li><span class='sn'>{i+1:02d}</span><p>{E(s)}</p></li>" for i,s in enumerate(T["steps"]))
    body=page_hero(T["k"],T["h"],T["l"],small=True)+f'''<section class="sec"><div class="wrap contact-grid">
 <form class="form" id="contact-form" data-to="{EMAIL}" data-ok="{E(T["ok"])}" data-err="{E(T["err"])}" data-lang="{lang}" novalidate>
  <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="row"><label for="cf-name">{f[0]}</label><input id="cf-name" name="name" required autocomplete="name"></div>
  <div class="row"><label for="cf-company">{f[1]}</label><input id="cf-company" name="company" autocomplete="organization"></div>
  <div class="row"><label for="cf-email">{f[2]}</label><input id="cf-email" name="email" type="email" required autocomplete="email"></div>
  <div class="row"><label for="cf-msg">{f[3]}</label><textarea id="cf-msg" name="message" rows="6" required></textarea></div>
  <button class="btn" type="submit">{f[4]} {icon("arrow")}</button>
  <p class="note">{T["note"]}</p>
  <p class="form-status" role="status" aria-live="polite"></p>
 </form>
 <aside class="side">
  <div class="card"><h3>Email</h3><a class="big-mail" href="mailto:{EMAIL}">{EMAIL}</a></div>
  <div class="card"><h3>{T["o"]}</h3><p>Vector Consulting Limited<br>{E(ADDRESS)}</p><p class="muted">{UI[lang]["brn"]} {BRN}</p></div>
  <div class="card"><h3>{T["nx"]}</h3><ol class="mini-steps">{steps}</ol></div>
 </aside>
</div></section>'''
    return T["t"],T["d"],body

def article(key, lang):
    a=ARTICLES[key]; t,ex,paras=a[lang]
    parts=[]
    for p in paras:
        parts.append(f"<h2>{E(p[3:])}</h2>" if p.startswith("## ") else f"<p>{E(p)}</p>")
    ld={"@context":"https://schema.org","@type":"Article","headline":t,"description":ex,"datePublished":a["date"],"inLanguage":lang,
        "author":{"@type":"Organization","name":"Vector Consulting"},"publisher":{"@type":"Organization","name":"Vector Consulting Limited"},"mainEntityOfPage":SITE+url(key,lang)}
    d=datetime.date.fromisoformat(a["date"])
    ds=d.strftime("%d %B %Y") if lang=="en" else f'{d.day} de {["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"][d.month-1]} de {d.year}'
    body=f'''<section class="phero phero-sm"><canvas class="field" aria-hidden="true"></canvas><div class="wrap narrow">
 <p class="kicker"><a href="{url("insights",lang)}">← {UI[lang]["back"]}</a></p><h1>{E(t)}</h1><p class="lead">{E(ex)}</p><p class="meta">{ds} · {a["mins"]} {UI[lang]["min"]} · Vector Consulting</p>
</div></section>
<article class="sec"><div class="wrap narrow prose">{"".join(parts)}</div></article>'''
    SEO_TITLE = {("art-act","en"):"EU AI Act: a practical checklist for tech teams",
                 ("art-act","es"):"Reglamento Europeo de IA: lista práctica para equipos",
                 ("art-ds","es"):"Espacio de datos en producción: lecciones de salud"}
    st = SEO_TITLE.get((key, lang), t)
    return (st+" · Vector Consulting" if len(st) <= 45 else st), ex, body, ld

import legal as LG
def legal_page(key):
    def fn(lang):
        title, desc, paras = LG.LEGAL[key][lang]
        parts = [f"<h2>{E(p[3:])}</h2>" if p.startswith("## ") else f"<p>{E(p)}</p>" for p in paras]
        body = page_hero({"en":"Legal","es":"Legal"}[lang], E(title), desc, small=True) + \
               f'<article class="sec"><div class="wrap narrow prose">{"".join(parts)}<p class="meta">{LG.UPDATED[lang]}</p></div></article>'
        return f"{title} · Vector Consulting", desc, body
    return fn

PAGES = {"legal":legal_page("legal"),"privacy":legal_page("privacy"),"cookies":legal_page("cookies"),"home":home,"services":services,"ai":ai,"how":how,"industries":industries,"cases":cases,"insights":insights,"about":about,"careers":careers,"contact":contact}

def write(path, content):
    fp=os.path.join(OUT, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp,"w",encoding="utf-8").write(content)

def redirect(frm, to):
    write(frm, f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Redirecting</title><link rel="canonical" href="{SITE}{to}"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={to}"></head><body><a href="{to}">{SITE}{to}</a></body></html>')

def main():
    if os.path.isdir(OUT):
        for n in os.listdir(OUT):
            p=os.path.join(OUT,n)
            if n in (".git",): continue
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)
    shutil.copytree(os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets"), os.path.join(OUT,"assets"))
    # animated explainer videos (pages + voice-over audio)
    import videos as VID
    vsrc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")
    for vid in VID.ORDER:
        write(f"/videos/{vid}/", VID.page(vid, "en"))
        write(f"/videos/{vid}/es/", VID.page(vid, "es"))
        for lang in ("en", "es"):
            a = os.path.join(vsrc, vid, f"voz-{lang}.mp3")
            if os.path.exists(a): shutil.copy(a, os.path.join(OUT, "videos", vid, f"voz-{lang}.mp3"))
            pst = os.path.join(vsrc, vid, f"poster-{lang}.webp")
            if os.path.exists(pst): shutil.copy(pst, os.path.join(OUT, "videos", vid, f"poster-{lang}.webp"))
    urls=[]
    for lang in ("en","es"):
        for key,fn in PAGES.items():
            t,d,b=fn(lang)
            write(url(key,lang), head(lang,key,t,d)+header(lang,key)+b+cta_band(lang)+footer(lang)); urls.append(url(key,lang))
        for key in ARTICLES:
            t,d,b,ld=article(key,lang)
            write(url(key,lang), head(lang,key,t,d,ld)+header(lang,"insights")+b+cta_band(lang)+footer(lang)); urls.append(url(key,lang))
    # old Google Sites URLs
    for frm,to in [("/home/","/"),("/es/casos-de-éxito/","/es/casos-de-exito/"),("/es/cómo-trabajamos/","/es/como-trabajamos/"),("/es/quiénes-somos/","/es/quienes-somos/"),("/es/ia-y-datos/index-old/","/es/ia-y-datos/")]:
        if "index-old" in frm: continue
        redirect(frm,to)
    # 404
    write("/404.html", head("en","home","Page not found · Vector Consulting","Page not found")+header("en","")+page_hero("404","Page <em>not found</em>","The page you are looking for has moved. Try the main sections above or go to the home page.")+footer("en"))
    today=datetime.date.today().isoformat()
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    for key in PATHS:
        for lang in ("en","es"):
            sm+=f'<url><loc>{SITE}{url(key,lang)}</loc><lastmod>{today}</lastmod><xhtml:link rel="alternate" hreflang="en" href="{SITE}{url(key,"en")}"/><xhtml:link rel="alternate" hreflang="es" href="{SITE}{url(key,"es")}"/></url>\n'
    sm+="</urlset>\n"
    write("/sitemap.xml", sm)
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    llms=f"""# Vector Consulting Limited

> Hong Kong technology consultancy delivering senior engineering teams, applied AI and federated data spaces to companies in Europe and Asia.

- Registered in Hong Kong, Business Registration No. {BRN}. Address: {ADDRESS}.
- Contact: {EMAIL}
- Services: software engineering, dedicated engineering teams, AI and data (sovereign AI, data platforms, federated data spaces on Gaia-X / IDSA / Pontus-X with ODRL usage policies), technology consulting including EU-funded R&D.
- Industries: healthcare and life sciences, procurement and public sector, technology companies, industrial data spaces.
- Engagement models: project delivery, dedicated team, specialists, advisory.
- Selected work: Global Data Care federated health data space (technology development for Accuro Technology, Spain); PROCUREDATA procurement data space (advisory for Agile Procurement via Accuro Technology); senior specialists for Spanish technology companies, including through Technova Corp Ltd (London).

## Pages
- [Services]({SITE}/services/)
- [AI & Data]({SITE}/services/ai-data/)
- [How we work]({SITE}/services/how-we-work/)
- [Industries]({SITE}/industries/)
- [Case studies]({SITE}/case-studies/)
- [Insights]({SITE}/insights/)
- [About]({SITE}/about/)
- [Careers]({SITE}/about/careers/)
- [Contact]({SITE}/contact/)
- [Español]({SITE}/es/)
- [Legal notice]({SITE}/legal/) · [Privacy]({SITE}/privacy/) · [Cookies]({SITE}/cookies/)

## Videos (animated explainers, EN/ES, AI-generated voice-over)
""" + "".join(f"- [{VIDS.VIDEOS[v]['en']['title']}]({SITE}/videos/{v}/): {vid_transcript(v,'en')}\n" for v in VIDS.ORDER)
    write("/llms.txt", llms)
    write("/CNAME","www.vectorconsultingltd.com\n")
    write("/.nojekyll","")
    print("pages:",len(urls))

if __name__=="__main__": main()
