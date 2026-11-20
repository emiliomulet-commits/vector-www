# -*- coding: utf-8 -*-
"""Animated explainer videos (wave 1: V01-V04), EN + ES.
Each scene: type (see assets/vx-video.js), chapter label, on-screen texts and the voice-over line (vo).
The voice-over text in `say` (if present) is what is sent to ElevenLabs when pronunciation needs help;
otherwise `vo` is read as written. Timing (scene starts) comes from build/videos/timing.json,
produced by cutting the ElevenLabs voice-over at its pauses."""
import json, os, html

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))

VIDEOS = {
"v01": {
 "en": {"title": "One accountable partner", "desc": "Who Vector Consulting is, in under a minute.", "scenes": [
  {"type":"q","chapter":"Opening","text":"Who owns your project when it gets hard?","vo":"Who owns your project when it gets hard?"},
  {"type":"cards","variant":"broken","chapter":"The problem","kicker":"The usual way","title":"Five vendors, nobody accountable","hl":"nobody accountable",
   "items":[{"icon":"compass","label":"Strategy"},{"icon":"board","label":"Architecture"},{"icon":"code","label":"Development"},{"icon":"db","label":"Data"},{"icon":"tools","label":"Support"}],
   "vo":"Five vendors, five contracts… and nobody accountable."},
  {"type":"merge","chapter":"One partner","kicker":"The Vector way","title":"One partner, end to end","hl":"One partner",
   "from":["Strategy","Architecture","Development","Data","Support"],"rows":["Strategy","Architecture","Delivery"],
   "vo":"Vector brings strategy, architecture and delivery under one roof."},
  {"type":"map","chapter":"Asia–Europe","kicker":"Where we work","title":"Hong Kong base, European delivery","hl":"European delivery",
   "cities":[{"name":"Hong Kong","x":1230,"y":520,"below":True,"sub":"Headquarters"},{"name":"Madrid","x":420,"y":560,"below":True,"sub":"Delivery"},{"name":"London","x":560,"y":340,"sub":"Specialists"}],
   "vo":"From Hong Kong, with delivery capacity in Madrid and London."},
  {"type":"cards","chapter":"What we do","kicker":"Four practices","title":"Four practices that work together","hl":"work together",
   "items":[{"icon":"code","label":"Software engineering"},{"icon":"team","label":"Dedicated teams"},{"icon":"ai","label":"AI & data"},{"icon":"compass","label":"Technology consulting"}],
   "vo":"Software engineering, dedicated teams, AI and data, and technology consulting."},
  {"type":"chips","chapter":"European rules","kicker":"Built for Europe","title":"Compliance designed in from day one","hl":"day one",
   "items":["GDPR","EU AI Act","EHDS","Gaia-X","IDSA","ODRL"],
   "vo":"Built for European rules: GDPR, the AI Act and Gaia-X data spaces.","say":"Built for European rules: G D P R, the A I Act, and Gaia X data spaces."},
  {"type":"close","chapter":"Close","text":"Senior by default. One accountable partner.","vo":"Senior by default. One accountable partner. Vector Consulting."}]},
 "es": {"title": "Un único socio responsable", "desc": "Quién es Vector Consulting, en menos de un minuto.", "scenes": [
  {"type":"q","chapter":"Apertura","text":"¿Quién responde cuando tu proyecto se complica?","vo":"¿Quién responde cuando tu proyecto se complica?"},
  {"type":"cards","variant":"broken","chapter":"El problema","kicker":"Lo habitual","title":"Cinco proveedores, ningún responsable","hl":"ningún responsable",
   "items":[{"icon":"compass","label":"Estrategia"},{"icon":"board","label":"Arquitectura"},{"icon":"code","label":"Desarrollo"},{"icon":"db","label":"Datos"},{"icon":"tools","label":"Soporte"}],
   "vo":"Cinco proveedores, cinco contratos… y nadie responsable."},
  {"type":"merge","chapter":"Un socio","kicker":"Con Vector","title":"Un único socio, de principio a fin","hl":"Un único socio",
   "from":["Estrategia","Arquitectura","Desarrollo","Datos","Soporte"],"rows":["Estrategia","Arquitectura","Entrega"],
   "vo":"Vector reúne la estrategia, la arquitectura y la entrega bajo un mismo techo."},
  {"type":"map","chapter":"Asia–Europa","kicker":"Dónde trabajamos","title":"Sede en Hong Kong, entrega en Europa","hl":"entrega en Europa",
   "cities":[{"name":"Hong Kong","x":1230,"y":520,"below":True,"sub":"Sede"},{"name":"Madrid","x":420,"y":560,"below":True,"sub":"Entrega"},{"name":"Londres","x":560,"y":340,"sub":"Especialistas"}],
   "vo":"Desde Hong Kong, con capacidad de entrega en Madrid y Londres.","say":"Desde Hong Kong, con capacidad de entrega en Madrid y en Londres."},
  {"type":"cards","chapter":"Qué hacemos","kicker":"Cuatro prácticas","title":"Cuatro prácticas que trabajan juntas","hl":"trabajan juntas",
   "items":[{"icon":"code","label":"Ingeniería de software"},{"icon":"team","label":"Equipos dedicados"},{"icon":"ai","label":"IA y datos"},{"icon":"compass","label":"Consultoría tecnológica"}],
   "vo":"Ingeniería de software, equipos dedicados, inteligencia artificial y datos, y consultoría tecnológica."},
  {"type":"chips","chapter":"Reglas europeas","kicker":"Hecho para Europa","title":"Cumplimiento desde el primer día","hl":"primer día",
   "items":["RGPD","Reglamento de IA","EHDS","Gaia-X","IDSA","ODRL"],
   "vo":"Diseñado para las reglas europeas: RGPD, Reglamento de IA y espacios de datos Gaia-X.","say":"Diseñado para las reglas europeas: el Reglamento de Protección de Datos, el Reglamento de Inteligencia Artificial y los espacios de datos Gaia equis."},
  {"type":"close","chapter":"Cierre","text":"Senior por defecto. Un único socio responsable.","vo":"Senior por defecto. Un único socio responsable. Vector Consulting."}]},
},
"v02": {
 "en": {"title": "Global Data Care: the data stays home", "desc": "How we built a federated health data space.", "scenes": [
  {"type":"q","chapter":"Opening","text":"How do hospitals share data without giving it away?","vo":"How do hospitals share data without giving it away?"},
  {"type":"cards","chapter":"Participants","kicker":"Global Data Care","title":"Every participant keeps its data at source","hl":"at source",
   "items":[{"icon":"health","label":"Hospitals"},{"icon":"lab","label":"Research groups"},{"icon":"chip","label":"Health-tech companies"}],
   "note":"No central copy. No data lake.","vo":"Hospitals, researchers and health-tech companies each keep their data at source."},
  {"type":"flow","chapter":"Usage policy","kicker":"Federated by design","title":"The data stays. The policy travels.","hl":"The policy travels.",
   "nodes":[{"icon":"health","label":"Data provider"},{"icon":"policy","label":"Connector + ODRL policy","hl":True},{"icon":"lab","label":"Data user"}],
   "token":"who · why · until","vo":"The data stays home. What travels is a usage policy: who, for what, and until when."},
  {"type":"flow","chapter":"Trust list","kicker":"Identity and trust","title":"Only verified participants get in","hl":"verified",
   "nodes":[{"icon":"user","label":"Participant"},{"icon":"shield","label":"Trust list","hl":True},{"icon":"globe","label":"Data space"}],
   "token":"verified ✓","reject":"unknown ✕","gateAt":1,"vo":"Only verified participants on the trust list can join."},
  {"type":"consent","chapter":"Consent","kicker":"Privacy by design","title":"Consent enforced on the server","hl":"on the server",
   "server":"Health record","viewer":"Professional","sections":["Allergies","Medication","Lab results","Imaging","Mental health","Genetics"],"allowed":[0,1],
   "vo":"Patient consent is enforced on the server, not just hidden on screen."},
  {"type":"chips","chapter":"Standards","kicker":"European standards","title":"A working federated health data space","hl":"working",
   "items":["Gaia-X","Pontus-X","ODRL","GDPR","EHDS"],"vo":"A working federated health data space, built on European standards.","say":"A working, federated health data space, built on European standards."},
  {"type":"close","chapter":"Close","text":"Built by Vector for Accuro Technology.","sub":"Global Data Care · vectorconsultingltd.com","vo":"Global Data Care. Built by Vector for Accuro Technology."}]},
 "es": {"title": "Global Data Care: el dato se queda en casa", "desc": "Cómo construimos un espacio de datos de salud federado.", "scenes": [
  {"type":"q","chapter":"Apertura","text":"¿Cómo comparten datos los hospitales sin cederlos?","vo":"¿Cómo comparten datos los hospitales sin cederlos?"},
  {"type":"cards","chapter":"Participantes","kicker":"Global Data Care","title":"Cada participante guarda sus datos en origen","hl":"en origen",
   "items":[{"icon":"health","label":"Hospitales"},{"icon":"lab","label":"Grupos de investigación"},{"icon":"chip","label":"Empresas de tecnología sanitaria"}],
   "note":"Sin copia central. Sin lago de datos.","vo":"Hospitales, investigadores y empresas de tecnología sanitaria mantienen sus datos en origen."},
  {"type":"flow","chapter":"Política de uso","kicker":"Federado por diseño","title":"El dato se queda. La política viaja.","hl":"La política viaja.",
   "nodes":[{"icon":"health","label":"Proveedor de datos"},{"icon":"policy","label":"Conector + política ODRL","hl":True},{"icon":"lab","label":"Usuario de datos"}],
   "token":"quién · para qué · hasta","vo":"El dato se queda en casa. Lo que viaja es una política de uso: quién, para qué y hasta cuándo."},
  {"type":"flow","chapter":"Lista de confianza","kicker":"Identidad y confianza","title":"Solo entran participantes verificados","hl":"verificados",
   "nodes":[{"icon":"user","label":"Participante"},{"icon":"shield","label":"Lista de confianza","hl":True},{"icon":"globe","label":"Espacio de datos"}],
   "token":"verificado ✓","reject":"desconocido ✕","gateAt":1,"vo":"Solo entran los participantes verificados en la lista de confianza."},
  {"type":"consent","chapter":"Consentimiento","kicker":"Privacidad desde el diseño","title":"El consentimiento se aplica en el servidor","hl":"en el servidor",
   "server":"Historia clínica","viewer":"Profesional","sections":["Alergias","Medicación","Analíticas","Imagen","Salud mental","Genética"],"allowed":[0,1],
   "vo":"El consentimiento del paciente se aplica en el servidor, no solo se oculta en la pantalla."},
  {"type":"chips","chapter":"Estándares","kicker":"Estándares europeos","title":"Un espacio de datos de salud que funciona","hl":"que funciona",
   "items":["Gaia-X","Pontus-X","ODRL","RGPD","EHDS"],"vo":"Un espacio de datos de salud federado y en funcionamiento, sobre estándares europeos."},
  {"type":"close","chapter":"Cierre","text":"Construido por Vector para Accuro Technology.","sub":"Global Data Care · vectorconsultingltd.com","vo":"Global Data Care. Construido por Vector para Accuro Technology."}]},
},
"v03": {
 "en": {"title": "PROCUREDATA: data entered once", "desc": "A procurement data space where suppliers publish once.", "scenes": [
  {"type":"q","chapter":"Opening","text":"How many times does a supplier type the same data?","vo":"How many times does a supplier type the same data?"},
  {"type":"cards","variant":"broken","chapter":"The problem","kicker":"Today","title":"The same certificate, portal after portal","hl":"portal after portal",
   "items":[{"icon":"doc","label":"Buyer portal A"},{"icon":"doc","label":"Buyer portal B"},{"icon":"doc","label":"Tender platform"},{"icon":"doc","label":"Supplier register"}],
   "vo":"The same certificate, re-entered in portal after portal."},
  {"type":"flow","chapter":"Publish once","kicker":"PROCUREDATA","title":"Published once, as a data package","hl":"once",
   "nodes":[{"icon":"building","label":"Supplier"},{"icon":"policy","label":"Data package","hl":True},{"icon":"globe","label":"Procurement data space"}],
   "token":"publish once","vo":"With PROCUREDATA, the supplier publishes it once, as a data package.","say":"With Procure Data, the supplier publishes it once, as a data package."},
  {"type":"flow","chapter":"The gate","kicker":"Governed sharing","title":"No approval, no policy, no data","hl":"no data",
   "nodes":[{"icon":"policy","label":"Data package"},{"icon":"shield","label":"Approved transaction + ODRL policy","hl":True},{"icon":"building","label":"Buyer"}],
   "token":"approved ✓","reject":"no policy ✕","gateAt":1,"vo":"Nothing flows without an approved transaction and a valid usage policy."},
  {"type":"form","chapter":"ERP autofill","kicker":"Into the buyer's ERP","title":"The form fills itself","hl":"fills itself",
   "package":"Supplier data package","erp":"Buyer ERP · supplier form","push":"push · on approval","pull":"pull · on demand",
   "fields":[["Company","Acme Components S.L."],["Tax ID","B-12345678"],["Quality certificate","ISO 9001 · valid"],["Bank details","Verified"]],
   "vo":"The buyer's ERP fills in the form automatically, on approval or on demand.","say":"The buyer's E R P fills in the form automatically, on approval, or on demand."},
  {"type":"flow","chapter":"AI + policy","kicker":"Governed AI","title":"AI proposes. The policy decides.","hl":"The policy decides.",
   "nodes":[{"icon":"ai","label":"AI assistant proposes"},{"icon":"policy","label":"Policy decides","hl":True},{"icon":"lock","label":"No central data store"}],
   "vo":"AI proposes; the policy decides. And there is no central data store.","say":"A I proposes. The policy decides. And there is no central data store."},
  {"type":"close","chapter":"Close","text":"Data entered once, consumed under governance.","sub":"PROCUREDATA · with Accuro Technology for Agile Procurement","vo":"Data entered once, consumed under governance. PROCUREDATA.","say":"Data entered once, consumed under governance. Procure Data."}]},
 "es": {"title": "PROCUREDATA: el dato se introduce una vez", "desc": "Un espacio de datos de compras donde el proveedor publica una sola vez.", "scenes": [
  {"type":"q","chapter":"Apertura","text":"¿Cuántas veces teclea un proveedor el mismo dato?","vo":"¿Cuántas veces teclea un proveedor el mismo dato?"},
  {"type":"cards","variant":"broken","chapter":"El problema","kicker":"Hoy","title":"El mismo certificado, portal tras portal","hl":"portal tras portal",
   "items":[{"icon":"doc","label":"Portal comprador A"},{"icon":"doc","label":"Portal comprador B"},{"icon":"doc","label":"Plataforma de licitación"},{"icon":"doc","label":"Registro de proveedores"}],
   "vo":"El mismo certificado, introducido portal tras portal."},
  {"type":"flow","chapter":"Publicar una vez","kicker":"PROCUREDATA","title":"Publicado una sola vez, como paquete de datos","hl":"una sola vez",
   "nodes":[{"icon":"building","label":"Proveedor"},{"icon":"policy","label":"Paquete de datos","hl":True},{"icon":"globe","label":"Espacio de datos de compras"}],
   "token":"publicar una vez","vo":"Con PROCUREDATA, el proveedor lo publica una sola vez, como paquete de datos.","say":"Con Procure Data, el proveedor lo publica una sola vez, como paquete de datos."},
  {"type":"flow","chapter":"La verja","kicker":"Intercambio gobernado","title":"Sin aprobación ni política, no hay dato","hl":"no hay dato",
   "nodes":[{"icon":"policy","label":"Paquete de datos"},{"icon":"shield","label":"Transacción aprobada + política ODRL","hl":True},{"icon":"building","label":"Comprador"}],
   "token":"aprobada ✓","reject":"sin política ✕","gateAt":1,"vo":"Nada fluye sin una transacción aprobada y una política de uso vigente."},
  {"type":"form","chapter":"Autorrelleno ERP","kicker":"En el ERP del comprador","title":"El formulario se rellena solo","hl":"se rellena solo",
   "package":"Paquete de datos del proveedor","erp":"ERP del comprador · ficha de proveedor","push":"push · al aprobar","pull":"pull · bajo demanda",
   "fields":[["Empresa","Acme Componentes S.L."],["NIF","B-12345678"],["Certificado de calidad","ISO 9001 · vigente"],["Datos bancarios","Verificados"]],
   "vo":"El ERP del comprador rellena el formulario solo, al aprobar o bajo demanda.","say":"El E R P del comprador rellena el formulario solo, al aprobar, o bajo demanda."},
  {"type":"flow","chapter":"IA + política","kicker":"IA gobernada","title":"La IA propone. La política decide.","hl":"La política decide.",
   "nodes":[{"icon":"ai","label":"El asistente de IA propone"},{"icon":"policy","label":"La política decide","hl":True},{"icon":"lock","label":"Sin almacén central"}],
   "vo":"La IA propone; la política decide. Y sin almacén central de datos.","say":"La inteligencia artificial propone. La política decide. Y sin almacén central de datos."},
  {"type":"close","chapter":"Cierre","text":"El dato se introduce una vez y se consume gobernado.","sub":"PROCUREDATA · con Accuro Technology para Agile Procurement","vo":"El dato se introduce una vez y se consume gobernado. PROCUREDATA.","say":"El dato se introduce una vez, y se consume gobernado. Procure Data."}]},
},
"v04": {
 "en": {"title": "Senior talent, one accountable partner", "desc": "How our dedicated teams and specialists work.", "scenes": [
  {"type":"q","chapter":"Opening","text":"Need a senior engineer next month, not next quarter?","vo":"Need a senior engineer next month, not next quarter?"},
  {"type":"flow","chapter":"The problem","kicker":"Traditional hiring","title":"Projects can't wait for hiring","hl":"can't wait",
   "nodes":[{"icon":"doc","label":"Job ad"},{"icon":"chat","label":"Interviews"},{"icon":"clock","label":"Notice period"},{"icon":"user","label":"Onboarding"}],
   "token":"months…","vo":"Traditional hiring is slow, and projects can't wait."},
  {"type":"cards","chapter":"The right profile","kicker":"Selection","title":"Profiles matched to your stack and culture","hl":"your stack",
   "items":[{"icon":"db","label":"Data engineer"},{"icon":"board","label":"Solution architect"},{"icon":"ai","label":"AI specialist"},{"icon":"code","label":"Senior developer"}],
   "vo":"Vector selects senior profiles that match your stack and your culture."},
  {"type":"cards","chapter":"Your team","kicker":"Embedded","title":"Your tools, your rituals, your priorities","hl":"your priorities",
   "items":[{"icon":"code","label":"Your repositories"},{"icon":"board","label":"Your board"},{"icon":"chat","label":"Your daily stand-up"}],
   "note":"You keep control of priorities.","vo":"They join your tools and rituals. You keep control of priorities."},
  {"type":"map","chapter":"Several countries","kicker":"Remote delivery","title":"Senior specialists from several countries","hl":"several countries",
   "cities":[{"name":"Hong Kong","x":1230,"y":520,"below":True,"sub":"Accountability"},{"name":"London","x":560,"y":340,"sub":"Specialists"},{"name":"Madrid","x":420,"y":560,"below":True,"sub":"Delivery"}],
   "vo":"Specialists working from several countries, including London."},
  {"type":"swap","chapter":"Continuity","kicker":"Guaranteed","title":"Continuity, even when people change","hl":"Continuity",
   "people":["Data engineer","Architect","Developer"],"newcomer":"New architect","bar":"Your project keeps moving",
   "vo":"And if someone has to change, we guarantee continuity."},
  {"type":"close","chapter":"Close","text":"Senior capacity, when your project needs it.","vo":"Senior capacity, when your project needs it. Vector Consulting."}]},
 "es": {"title": "Talento senior, un único responsable", "desc": "Cómo trabajan nuestros equipos dedicados y especialistas.", "scenes": [
  {"type":"q","chapter":"Apertura","text":"¿Necesitas un ingeniero senior el mes que viene?","vo":"¿Necesitas un ingeniero senior el mes que viene, y no el próximo trimestre?"},
  {"type":"flow","chapter":"El problema","kicker":"Contratación tradicional","title":"Los proyectos no pueden esperar","hl":"no pueden esperar",
   "nodes":[{"icon":"doc","label":"Oferta"},{"icon":"chat","label":"Entrevistas"},{"icon":"clock","label":"Preaviso"},{"icon":"user","label":"Incorporación"}],
   "token":"meses…","vo":"Contratar por la vía tradicional es lento, y los proyectos no esperan."},
  {"type":"cards","chapter":"El perfil adecuado","kicker":"Selección","title":"Perfiles a la medida de tu tecnología","hl":"tu tecnología",
   "items":[{"icon":"db","label":"Ingeniero de datos"},{"icon":"board","label":"Arquitecto de soluciones"},{"icon":"ai","label":"Especialista en IA"},{"icon":"code","label":"Desarrollador senior"}],
   "vo":"Vector selecciona perfiles senior a la medida de tu tecnología y de tu cultura."},
  {"type":"cards","chapter":"Tu equipo","kicker":"Integrados","title":"Tus herramientas, tus rutinas, tus prioridades","hl":"tus prioridades",
   "items":[{"icon":"code","label":"Tus repositorios"},{"icon":"board","label":"Tu tablero"},{"icon":"chat","label":"Tu reunión diaria"}],
   "note":"Tú mantienes el control de las prioridades.","vo":"Se integran en tus herramientas y rutinas. Tú mantienes el control de las prioridades."},
  {"type":"map","chapter":"Varios países","kicker":"Entrega en remoto","title":"Especialistas senior desde varios países","hl":"varios países",
   "cities":[{"name":"Hong Kong","x":1230,"y":520,"below":True,"sub":"Responsabilidad"},{"name":"Londres","x":560,"y":340,"sub":"Especialistas"},{"name":"Madrid","x":420,"y":560,"below":True,"sub":"Entrega"}],
   "vo":"Especialistas que trabajan desde varios países, incluido Londres."},
  {"type":"swap","chapter":"Continuidad","kicker":"Garantizada","title":"Continuidad, aunque cambien las personas","hl":"Continuidad",
   "people":["Ingeniero de datos","Arquitecto","Desarrollador"],"newcomer":"Nuevo arquitecto","bar":"Tu proyecto no se detiene",
   "vo":"Y si alguien tiene que cambiar, garantizamos la continuidad."},
  {"type":"close","chapter":"Cierre","text":"Capacidad senior cuando tu proyecto la necesita.","vo":"Capacidad senior cuando tu proyecto la necesita. Vector Consulting."}]},
},
}

ORDER = ["v01", "v02", "v03", "v04"]

def timing():
    p = os.path.join(HERE, "videos", "timing.json")
    return json.load(open(p)) if os.path.exists(p) else {}

def estimate(scenes):
    """Fallback timing before the real voice-over exists: ~2.6 words/s plus breathing room."""
    starts, t = [], 0.0
    for s in scenes:
        starts.append(round(t, 2))
        t += max(4.2, len(s["vo"].split()) / 2.6 + 1.6)
    return starts, round(t + 0.8, 2)

def page(vid, lang, site_css_ver=""):
    v = VIDEOS[vid][lang]
    tm = timing().get(f"{vid}-{lang}")
    starts, total = (tm["starts"], tm["total"]) if tm else estimate(v["scenes"])
    data = {"id": vid, "lang": lang, "audio": (f"/videos/{vid}/voz-{lang}.mp3" if os.path.exists(os.path.join(HERE, "videos", vid, f"voz-{lang}.mp3")) else None), "title": v["title"], "scenes": v["scenes"], "starts": starts, "total": total}
    data["scenes"] = [{k: x for k, x in s.items() if k != "say"} for s in v["scenes"]]
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(v["title"])} · Vector Consulting</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=IBM+Plex+Sans:wght@400;500;600;700&family=Poppins:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/vx-video.css">
</head>
<body class="at-start">
<div id="wrap"><svg id="stage" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid meet" role="img" aria-label="{E(v["title"])}"></svg></div>
<p id="cap" aria-live="polite"></p>
<div id="start"><span></span></div>
<p class="rm-note"></p>
<button id="voz-btn" type="button" aria-pressed="false"></button>
<div class="ui">
 <button id="play" type="button"><svg viewBox="0 0 24 24" fill="currentColor"><path id="pi" d="M8 5v14l11-7z"/></svg></button>
 <button id="prev" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M15 6l-6 6 6 6"/></svg></button>
 <button id="next" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M9 6l6 6-6 6"/></svg></button>
 <div class="scenes" id="scenes"></div>
 <button id="replay" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v4h4"/></svg></button>
 <button id="close" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
</div>
<script>window.VX={js};</script>
<script src="/assets/gsap.min.js"></script>
<script src="/assets/vx-video.js"></script>
</body>
</html>'''

def voice_scripts():
    """Text blocks for ElevenLabs: scene lines separated by long pauses, one block per video and language."""
    out = {}
    for vid in ORDER:
        for lang in ("en", "es"):
            lines = [s.get("say", s["vo"]) for s in VIDEOS[vid][lang]["scenes"]]
            out[f"{vid}-{lang}"] = '\n\n[pause]\n\n'.join(lines)
    return out

if __name__ == "__main__":
    for k, t in voice_scripts().items():
        print(f"=== {k} ({len(t)} chars)\n{t}\n")
