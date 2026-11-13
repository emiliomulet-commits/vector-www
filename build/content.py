# -*- coding: utf-8 -*-
# Site content for vectorconsultingltd.com — EN and ES.

EMAIL = "alison.lindsay@vectorconsultingltd.com"
ADDRESS = "Rooms 1705-1709, 17/F, Tung Chiu Commercial Centre, 193 Lockhart Road, Wanchai, Hong Kong"
BRN = "72876645"

# page key -> (en path, es path)
PATHS = {
    "home":      ("/", "/es/"),
    "services":  ("/services/", "/es/servicios/"),
    "ai":        ("/services/ai-data/", "/es/ia-y-datos/"),
    "how":       ("/services/how-we-work/", "/es/como-trabajamos/"),
    "industries":("/industries/", "/es/sectores/"),
    "cases":     ("/case-studies/", "/es/casos-de-exito/"),
    "insights":  ("/insights/", "/es/perspectivas/"),
    "about":     ("/about/", "/es/quienes-somos/"),
    "careers":   ("/about/careers/", "/es/empleo/"),
    "contact":   ("/contact/", "/es/contacto/"),
    "art-ai":    ("/insights/ai-with-control-over-your-data/", "/es/perspectivas/ia-con-control-de-tus-datos/"),
    "art-ds":    ("/insights/running-a-data-space-in-production/", "/es/perspectivas/espacio-de-datos-en-produccion/"),
    "art-act":   ("/insights/preparing-for-the-eu-ai-act/", "/es/perspectivas/prepararse-para-el-reglamento-europeo-de-ia/"),
}

UI = {
 "en": {
  "nav": [("services","Services"),("ai","AI & Data"),("industries","Industries"),("cases","Case studies"),("insights","Insights"),("about","About")],
  "cta":"Talk to an expert", "lang":"Español", "skip":"Skip to content",
  "footer_tag":"Software engineering, AI and data for companies that build to scale.",
  "f_company":"Company","f_services":"Services","f_contact":"Contact",
  "brn":"Business Registration No.","rights":"All rights reserved.",
  "read":"Read more","back":"All insights","min":"min read",
  "cta_title":"Have a project in mind?","cta_text":"Tell us about your challenge. A senior member of our team will come back to you with a clear next step.",
  "email_us":"Email us",
 },
 "es": {
  "nav": [("services","Servicios"),("ai","IA y Datos"),("industries","Sectores"),("cases","Casos de éxito"),("insights","Perspectivas"),("about","Quiénes somos")],
  "cta":"Hablar con un experto", "lang":"English", "skip":"Saltar al contenido",
  "footer_tag":"Ingeniería de software, IA y datos para empresas que construyen para crecer.",
  "f_company":"Empresa","f_services":"Servicios","f_contact":"Contacto",
  "brn":"Nº de Registro Mercantil","rights":"Todos los derechos reservados.",
  "read":"Leer más","back":"Todas las perspectivas","min":"min de lectura",
  "cta_title":"¿Tienes un proyecto en mente?","cta_text":"Cuéntanos tu reto. Una persona senior de nuestro equipo te responderá con un siguiente paso claro.",
  "email_us":"Escríbenos",
 },
}

SERVICES = {
 "en": [
  ("code","Software Engineering","Reliable, maintainable software across the full lifecycle: requirements, architecture, development, testing and operation. Every project ships with documentation, automated tests and a clear handover.",
   ["Web platforms and APIs","Cloud-native architecture","Modernisation of legacy systems","QA and test automation"]),
  ("team","Dedicated Teams","A senior engineering team that works as part of your organisation. We select profiles that match your stack and culture, and stay accountable for continuity, performance and replacement.",
   ["Profiles matched to your stack","Onboarding into your tools","Continuity and replacement guaranteed","You keep control of priorities"]),
  ("ai","AI & Data","Applied AI and trusted data infrastructure designed for European standards: GDPR, the EU AI Act and federated data spaces built on Gaia-X and IDSA principles.",
   ["AI use cases to production","Data platforms and pipelines","Federated data spaces","Sovereign and on-premise AI"]),
  ("compass","Technology Consulting","Independent senior advice for the decisions that shape your technology. Hands-on engineering experience combined with knowledge of European regulation and funding programmes.",
   ["Architecture and due diligence","Technology roadmaps","EU-funded R&D projects","Compliance by design"]),
 ],
 "es": [
  ("code","Ingeniería de Software","Software fiable y mantenible en todo su ciclo de vida: requisitos, arquitectura, desarrollo, pruebas y operación. Cada proyecto incluye documentación, pruebas automatizadas y un traspaso claro.",
   ["Plataformas web y APIs","Arquitectura cloud-native","Modernización de sistemas heredados","QA y automatización de pruebas"]),
  ("team","Equipos Dedicados","Un equipo de ingeniería senior que trabaja como parte de tu organización. Seleccionamos perfiles acordes a tu tecnología y cultura, y respondemos de la continuidad, el rendimiento y las sustituciones.",
   ["Perfiles adaptados a tu stack","Integración en tus herramientas","Continuidad y sustitución garantizadas","Tú mantienes el control de las prioridades"]),
  ("ai","IA y Datos","IA aplicada e infraestructura de datos de confianza diseñadas para los estándares europeos: RGPD, el Reglamento Europeo de IA y espacios de datos federados según los principios de Gaia-X e IDSA.",
   ["Casos de uso de IA hasta producción","Plataformas y pipelines de datos","Espacios de datos federados","IA soberana y on-premise"]),
  ("compass","Consultoría Tecnológica","Asesoramiento senior e independiente para las decisiones que definen tu tecnología. Experiencia práctica de ingeniería unida al conocimiento de la regulación y los programas de financiación europeos.",
   ["Arquitectura y due diligence","Hojas de ruta tecnológicas","Proyectos de I+D con fondos europeos","Cumplimiento desde el diseño"]),
 ],
}

WHY = {
 "en": [("Senior by default","Every engagement is staffed with experienced engineers and architects, not trainees learning on your project."),
        ("One accountable partner","Strategy, architecture and delivery under one roof, with named people and a single point of contact."),
        ("Built for European rules","GDPR, the EU AI Act and data sovereignty are designed in from day one, not bolted on before an audit."),
        ("Asia–Europe reach","A Hong Kong company with delivery capacity in Spain and the UK, working across time zones.")],
 "es": [("Seniority por defecto","Cada proyecto cuenta con ingenieros y arquitectos con experiencia, no con perfiles que aprenden en tu proyecto."),
        ("Un único socio responsable","Estrategia, arquitectura y ejecución bajo un mismo techo, con personas con nombre y un único interlocutor."),
        ("Pensado para las normas europeas","RGPD, Reglamento Europeo de IA y soberanía del dato integrados desde el primer día, no añadidos antes de una auditoría."),
        ("Alcance Asia–Europa","Una empresa de Hong Kong con capacidad de entrega en España y Reino Unido, trabajando entre husos horarios.")],
}

PROCESS = {
 "en": [("Discover","We understand your goals, constraints and data. You get a written scope, risks and a costed plan."),
        ("Design","Architecture, security and compliance decisions are made and documented before code is written."),
        ("Build","Short iterations, working software every sprint, automated tests and transparent reporting."),
        ("Run","Handover to your team or ongoing support, with monitoring, documentation and clear service levels.")],
 "es": [("Descubrir","Entendemos tus objetivos, restricciones y datos. Recibes un alcance escrito, riesgos y un plan valorado."),
        ("Diseñar","Las decisiones de arquitectura, seguridad y cumplimiento se toman y documentan antes de escribir código."),
        ("Construir","Iteraciones cortas, software funcionando en cada sprint, pruebas automatizadas e informes transparentes."),
        ("Operar","Traspaso a tu equipo o soporte continuo, con monitorización, documentación y niveles de servicio claros.")],
}

MODELS = {
 "en": [("Project delivery","Fixed scope, defined outcome","Best when the goal is clear. We commit to scope, timeline and budget, and own delivery end to end."),
        ("Dedicated team","Long-term capacity","A stable, senior team that works inside your organisation and your rituals, with Vector accountable for continuity."),
        ("Specialists","Targeted expertise","Individual architects, data engineers or AI specialists who join your team for a defined period."),
        ("Advisory","Independent guidance","Architecture reviews, technology roadmaps and due diligence, on a project or retainer basis.")],
 "es": [("Proyecto cerrado","Alcance fijo, resultado definido","Ideal cuando el objetivo está claro. Nos comprometemos con alcance, plazo y presupuesto, y asumimos la entrega de principio a fin."),
        ("Equipo dedicado","Capacidad a largo plazo","Un equipo senior y estable que trabaja dentro de tu organización y tus rutinas, con Vector responsable de la continuidad."),
        ("Especialistas","Experiencia concreta","Arquitectos, ingenieros de datos o especialistas en IA que se incorporan a tu equipo durante un periodo definido."),
        ("Asesoramiento","Criterio independiente","Revisiones de arquitectura, hojas de ruta tecnológicas y due diligence, por proyecto o con iguala.")],
}

INDUSTRIES = {
 "en": [("health","Healthcare & life sciences","Health data platforms where patient privacy, consent and interoperability are requirements. We built the technology behind a federated health data space in Spain."),
        ("procure","Procurement & public sector","Data sharing between buyers, suppliers and public bodies, with traceable usage policies and audit trails."),
        ("chip","Technology companies","Scale-ups and software vendors that need senior capacity to ship faster without losing quality."),
        ("factory","Industry & data spaces","Manufacturers and industrial ecosystems joining European data spaces under Gaia-X and IDSA rules.")],
 "es": [("health","Salud y ciencias de la vida","Plataformas de datos sanitarios donde la privacidad, el consentimiento y la interoperabilidad son requisitos. Desarrollamos la tecnología de un espacio de datos de salud federado en España."),
        ("procure","Compras y sector público","Compartición de datos entre compradores, proveedores y administraciones, con políticas de uso trazables y registros de auditoría."),
        ("chip","Empresas tecnológicas","Scale-ups y fabricantes de software que necesitan capacidad senior para entregar más rápido sin perder calidad."),
        ("factory","Industria y espacios de datos","Fabricantes y ecosistemas industriales que se incorporan a espacios de datos europeos bajo las reglas de Gaia-X e IDSA.")],
}

CASES = {
 "en": [
  {"title":"Global Data Care: a federated health data space","client":"Accuro Technology (Spain)","sector":"Healthcare","tags":["Gaia-X","Pontus-X","ODRL","GDPR"],
   "challenge":"Create a trusted way for hospitals, research groups and health technology companies to share data without giving up control of it.",
   "work":"Vector delivered the full technology development and the technological and functional consulting: federated architecture, connectors, usage policies, identity and trust lists, and the participant onboarding flow.",
   "result":"A working federated health data space in which each participant keeps its data at source and decides, policy by policy, who can use it and for what."},
  {"title":"PROCUREDATA: a procurement data space","client":"Agile Procurement, through Accuro Technology","sector":"Procurement","tags":["Data spaces","Interoperability","Usage policies"],
   "challenge":"Help buyers and suppliers share procurement data in a reliable, interoperable way.",
   "work":"Vector advises on the federated architecture and the data space design, bringing the patterns proven in the health sector.",
   "result":"A federated procurement platform design aligned with European data space standards."},
  {"title":"International talent for Spanish technology companies","client":"Accuro Technology and other Spanish companies","sector":"Technology","tags":["Dedicated specialists","Remote delivery"],
   "challenge":"Find senior specialists quickly for demanding projects, without long hiring cycles.",
   "work":"Vector provides high-value engineers working from several countries, including specialists in London through Technova Corp Ltd, integrated into the client's teams.",
   "result":"Senior capacity available when the project needs it, with Vector accountable for continuity."},
 ],
 "es": [
  {"title":"Global Data Care: espacio de datos de salud federado","client":"Accuro Technology (España)","sector":"Salud","tags":["Gaia-X","Pontus-X","ODRL","RGPD"],
   "challenge":"Crear una forma de confianza para que hospitales, grupos de investigación y empresas de tecnología sanitaria compartan datos sin perder su control.",
   "work":"Vector realizó todo el desarrollo tecnológico y la consultoría tecnológica y funcional: arquitectura federada, conectores, políticas de uso, identidad y listas de confianza, y el proceso de alta de participantes.",
   "result":"Un espacio de datos de salud federado en funcionamiento, en el que cada participante mantiene sus datos en origen y decide, política a política, quién puede usarlos y para qué."},
  {"title":"PROCUREDATA: espacio de datos de compras","client":"Agile Procurement, a través de Accuro Technology","sector":"Compras","tags":["Espacios de datos","Interoperabilidad","Políticas de uso"],
   "challenge":"Ayudar a compradores y proveedores a compartir datos de compras de forma fiable e interoperable.",
   "work":"Vector asesora en la arquitectura federada y el diseño del espacio de datos, aportando los patrones probados en el sector salud.",
   "result":"Un diseño de plataforma federada de compras alineado con los estándares europeos de espacios de datos."},
  {"title":"Talento internacional para empresas tecnológicas españolas","client":"Accuro Technology y otras empresas españolas","sector":"Tecnología","tags":["Especialistas dedicados","Trabajo en remoto"],
   "challenge":"Incorporar especialistas senior con rapidez para proyectos exigentes, sin largos procesos de selección.",
   "work":"Vector aporta ingenieros de alto valor que trabajan desde varios países, incluidos especialistas en Londres a través de Technova Corp Ltd, integrados en los equipos del cliente.",
   "result":"Capacidad senior disponible cuando el proyecto la necesita, con Vector responsable de la continuidad."},
 ],
}

LEADERS = {
 "en": [("Emilio Mulet","Managing Director","Specialist in European technology programmes, federated data spaces and sovereign AI. Leads strategy and client advisory."),
        ("Alison Lindsay","Managing Director","Leads operations, finance and client relations from Hong Kong."),
        ("Diego Castellanos","Technical Lead","Leads engineering delivery on data space and platform projects.")],
 "es": [("Emilio Mulet","Director General","Especialista en programas tecnológicos europeos, espacios de datos federados e IA soberana. Dirige la estrategia y el asesoramiento a clientes."),
        ("Alison Lindsay","Directora General","Dirige operaciones, finanzas y relación con clientes desde Hong Kong."),
        ("Diego Castellanos","Responsable Técnico","Dirige la ejecución técnica de los proyectos de espacios de datos y plataformas.")],
}

VALUES = {
 "en": [("Seniority","Experienced people on every engagement."),("Accountability","Named owners and clear commitments."),("Transparency","Open reporting, open pricing, no surprises."),("Trust","Security and compliance designed in.")],
 "es": [("Seniority","Personas con experiencia en cada proyecto."),("Responsabilidad","Responsables con nombre y compromisos claros."),("Transparencia","Informes y precios abiertos, sin sorpresas."),("Confianza","Seguridad y cumplimiento desde el diseño.")],
}

ROLES = {
 "en": ["Full-stack and back-end developers","Cloud and DevOps engineers","Data engineers","AI / machine learning engineers","Solution architects","Technical project managers"],
 "es": ["Desarrolladores full-stack y back-end","Ingenieros cloud y DevOps","Ingenieros de datos","Ingenieros de IA / machine learning","Arquitectos de soluciones","Jefes de proyecto técnicos"],
}

ARTICLES = {
 "art-ai": {
  "date":"2026-10-20","mins":4,
  "en":("How to adopt AI without losing control of your data",
        "Most AI pilots stall for the same reason: the data they need cannot leave the building. A practical path to useful AI that respects that limit.",
        ["Companies rarely lack ideas for AI. What they lack is a safe way to let a model work with real data. Customer records, medical histories, contracts and production data are exactly what makes AI useful, and exactly what legal and security teams are right to protect.",
         "## Start from the decision, not the model",
         "We begin with one concrete decision the business makes often: classifying incoming documents, prioritising tickets, drafting a first answer. A narrow use case keeps the data scope small, which makes the privacy review short and the value easy to measure.",
         "## Bring the model to the data",
         "When data cannot travel, the model has to. Open-weight models running in your own cloud tenant or on-premise hardware remove the need to send sensitive records to a third party. For many tasks they perform close to the large hosted models, at predictable cost.",
         "## Make governance part of the architecture",
         "Logging every prompt and answer, keeping humans in the loop for consequential decisions, and documenting training and evaluation data are not paperwork. They are what lets an auditor, and your own team, trust the system a year from now.",
         "## Measure, then scale",
         "A pilot earns the right to scale when it has a baseline, a target and an owner. With those three in place, extending to the next use case is a repeatable step rather than a new project."]),
  "es":("Cómo adoptar la IA sin perder el control de tus datos",
        "La mayoría de los pilotos de IA se atascan por lo mismo: los datos que necesitan no pueden salir de casa. Un camino práctico hacia una IA útil que respeta ese límite.",
        ["A las empresas rara vez les faltan ideas para la IA. Lo que les falta es una forma segura de que un modelo trabaje con datos reales. Los expedientes de clientes, las historias clínicas, los contratos y los datos de producción son justo lo que hace útil a la IA, y justo lo que los equipos legales y de seguridad hacen bien en proteger.",
         "## Empezar por la decisión, no por el modelo",
         "Partimos de una decisión concreta que el negocio toma a menudo: clasificar documentos entrantes, priorizar incidencias, redactar una primera respuesta. Un caso de uso acotado limita los datos implicados, lo que acorta la revisión de privacidad y facilita medir el valor.",
         "## Llevar el modelo a los datos",
         "Cuando los datos no pueden viajar, tiene que viajar el modelo. Los modelos de pesos abiertos ejecutados en tu propia nube o en hardware on-premise evitan enviar información sensible a terceros. Para muchas tareas rinden cerca de los grandes modelos alojados, con un coste predecible.",
         "## La gobernanza, parte de la arquitectura",
         "Registrar cada consulta y respuesta, mantener a una persona en las decisiones relevantes y documentar los datos de entrenamiento y evaluación no es burocracia. Es lo que permite que un auditor, y tu propio equipo, confíen en el sistema dentro de un año.",
         "## Medir y después escalar",
         "Un piloto se gana el derecho a escalar cuando tiene una línea base, un objetivo y un responsable. Con esas tres piezas, extenderlo al siguiente caso de uso es un paso repetible, no un proyecto nuevo."]),
 },
 "art-ds": {
  "date":"2026-09-15","mins":5,
  "en":("Running a data space in production: lessons from health",
        "A federated data space is easy to demonstrate and hard to operate. What we learned taking one from pilot to production.",
        ["Demonstrators prove that two connectors can exchange a file under a usage policy. Production asks harder questions: who is allowed in, how trust is revoked, what happens when a policy changes after data has already been shared.",
         "## Onboarding is the product",
         "Participants judge a data space by how long it takes to join. Clear identity checks, a published trust list and a guided first exchange matter more than any single technical feature.",
         "## Policies need a vocabulary people understand",
         "ODRL makes usage policies machine-readable. Participants still need them in plain language. We maintain a small library of approved policy templates, each with a human summary, so legal teams can review once and reuse.",
         "## Plan for revocation from day one",
         "Trust is not permanent. Certificates expire, organisations leave, consent is withdrawn. The architecture must make revocation fast and visible to every connector.",
         "## Operate it like any critical service",
         "Monitoring, incident response, versioned releases and documented service levels turn a research project into infrastructure that hospitals and companies can rely on."]),
  "es":("Operar un espacio de datos en producción: lecciones del sector salud",
        "Un espacio de datos federado es fácil de demostrar y difícil de operar. Lo que aprendimos al llevar uno del piloto a producción.",
        ["Los demostradores prueban que dos conectores pueden intercambiar un fichero bajo una política de uso. La producción plantea preguntas más difíciles: quién puede entrar, cómo se revoca la confianza, qué ocurre cuando una política cambia después de haber compartido los datos.",
         "## El alta de participantes es el producto",
         "Los participantes juzgan un espacio de datos por lo que tardan en unirse. Unas comprobaciones de identidad claras, una lista de confianza publicada y un primer intercambio guiado importan más que cualquier funcionalidad técnica aislada.",
         "## Políticas con un vocabulario comprensible",
         "ODRL hace que las políticas de uso sean legibles por máquinas, pero los participantes las necesitan en lenguaje claro. Mantenemos una pequeña biblioteca de plantillas de políticas aprobadas, cada una con un resumen humano, para que los equipos legales revisen una vez y reutilicen.",
         "## Planificar la revocación desde el primer día",
         "La confianza no es permanente. Los certificados caducan, las organizaciones se van y el consentimiento se retira. La arquitectura debe hacer que la revocación sea rápida y visible para todos los conectores.",
         "## Operarlo como cualquier servicio crítico",
         "La monitorización, la respuesta a incidentes, las versiones controladas y los niveles de servicio documentados convierten un proyecto de investigación en una infraestructura en la que hospitales y empresas pueden confiar."]),
 },
 "art-act": {
  "date":"2026-08-25","mins":4,
  "en":("Preparing for the EU AI Act: a practical checklist for technology teams",
        "The AI Act is now being applied in stages. What engineering and product teams should have in place, in plain terms.",
        ["The EU AI Act sorts AI systems by risk. Most business tools fall into the lower tiers, but teams still need to know where each system sits and be able to show why.",
         "## Keep an inventory",
         "List every AI system you build or buy, what it decides or recommends, and who is affected. This single document answers most of the questions a regulator, a customer or an auditor will ask.",
         "## Classify and document",
         "For each system, record its risk category and the reasoning. Higher-risk uses require risk management, data governance, technical documentation, logging and human oversight.",
         "## Be transparent with users",
         "People should know when they are talking to an AI system or reading AI-generated content. Simple notices in the interface cover most cases.",
         "## Assign ownership",
         "Every system needs a named owner responsible for its documentation, monitoring and updates. Compliance is easiest when it is part of normal engineering work rather than a separate project."]),
  "es":("Prepararse para el Reglamento Europeo de IA: lista práctica para equipos tecnológicos",
        "El Reglamento de IA se está aplicando por fases. Lo que los equipos de ingeniería y producto deberían tener preparado, en términos claros.",
        ["El Reglamento Europeo de IA clasifica los sistemas de IA según su riesgo. La mayoría de las herramientas empresariales están en los niveles bajos, pero los equipos deben saber dónde está cada sistema y poder justificarlo.",
         "## Mantener un inventario",
         "Lista cada sistema de IA que desarrollas o compras, qué decide o recomienda y a quién afecta. Este único documento responde a la mayoría de las preguntas de un regulador, un cliente o un auditor.",
         "## Clasificar y documentar",
         "Para cada sistema, registra su categoría de riesgo y el razonamiento. Los usos de mayor riesgo exigen gestión de riesgos, gobernanza de datos, documentación técnica, registros y supervisión humana.",
         "## Transparencia con los usuarios",
         "Las personas deben saber cuándo hablan con un sistema de IA o leen contenido generado por IA. Avisos sencillos en la interfaz cubren la mayoría de los casos.",
         "## Asignar responsables",
         "Cada sistema necesita un responsable con nombre que se ocupe de su documentación, monitorización y actualizaciones. El cumplimiento es más fácil cuando forma parte del trabajo normal de ingeniería y no es un proyecto aparte."]),
 },
}
