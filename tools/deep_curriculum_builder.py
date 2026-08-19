#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import csv, importlib.util, re, textwrap, json

ROOT=Path(__file__).resolve().parents[1]

# Bibliografía existente del programa. Los identificadores permiten seleccionar fuentes
# pertinentes sin duplicar texto protegido dentro de las clases.
BOOKS={}
with (ROOT/'data'/'books.csv').open(encoding='utf-8') as fh:
    for row in csv.DictReader(fh): BOOKS[row['key']]=row

PARTS={
0: dict(level='Etapa 1 — Profesional → Líder', outcome='pasar de ejecutar tareas a producir contribución, criterio y confianza',
refs=['drucker-effective','drucker-management','grove-output','extra-089','extra-090','extra-086','extra-087','clear-atomic','extra-002','extra-001']),
1: dict(level='Etapa 1 — Profesional → Líder', outcome='decidir con evidencia, incertidumbre, causalidad y pensamiento sistémico',
refs=['kahneman-thinking','klein-sources','duke-thinking','extra-031','extra-101','extra-102','extra-029','senge-fifth','extra-096','extra-028']),
2: dict(level='Etapa 1 — Profesional → Líder', outcome='convertir comunicación, influencia y negociación en sistemas de decisión y relación',
refs=['heath-made','cialdini-influence','fisher-getting','extra-012','extra-013','extra-minto','extra-duarte','extra-humbleinquiry','carnegie-friends','voss-never']),
3: dict(level='Etapa 1 — Profesional → Líder', outcome='regularse, sostener exigencia humana y liderar adaptación bajo presión',
refs=['goleman-ei','goleman-primal','heifetz-line','extra-003','edmondson-fearless','duckworth-grit','extra-016','extra-083','extra-084','extra-064']),
4: dict(level='Etapa 2 — Líder → Jefe', outcome='crear equipos con propósito, coordinación, confianza, aprendizaje y accountability',
refs=['hackman-leading','lencioni-five','extra-katzenbach','grove-output','scott-radical','extra-019','extra-020','extra-023','extra-080','extra-teamofteams']),
5: dict(level='Etapa 2 — Líder → Jefe', outcome='diseñar un sistema de talento desde el cargo hasta la salida responsable',
refs=['armstrong-hrm','noe-hrm','buckingham-first','sutton-goodboss','extra-021','extra-022','scott-radical','extra-019','extra-090','extra-091']),
6: dict(level='Etapa 2 — Jefe → Manager', outcome='entregar proyectos con alcance, flujo, riesgo, calidad y gobernanza adaptativa',
refs=['pmi-pmbok','kerzner-project','schwaber-scrum','anderson-kanban','forsgren-accelerate','goldratt-goal','extra-024','extra-025','extra-026','extra-093']),
7: dict(level='Etapa 2 — Jefe → Manager', outcome='operar procesos end-to-end con capacidad, calidad, continuidad y mejora',
refs=['slack-operations','goldratt-goal','womack-lean','deming-crisis','rummler-process','extra-095','extra-094','extra-iso9001','extra-iso22301','extra-093']),
8: dict(level='Etapa 3 — Manager → Gerente', outcome='dirigir mediante outcomes, métricas, revisiones y asignación explícita de recursos',
refs=['doerr-okrs','kaplan-scorecard','marr-kpi','grove-output','extra-052','charan-execution','rumelt-good','extra-053','extra-054','drucker-management']),
9: dict(level='Etapa 3 — Manager → Gerente', outcome='leer la economía del negocio y decidir con estados, caja, márgenes, retorno y valoración',
refs=['kieso-accounting','penman-fsa','palepu-analysis','horngren-managerial','brealey-corpfin','ross-corpfin','koller-valuation','damodaran-valuation','schilit-shenanigans','extra-050']),
10: dict(level='Etapa 3 — Manager → Gerente', outcome='construir ingresos mediante un proceso comercial medible y negociación disciplinada',
refs=['rackham-spin','dixon-challenger','fisher-getting','voss-never','malhotra-negotiation','extra-046','extra-047','extra-049','extra-pricing','cialdini-influence']),
11: dict(level='Etapa 3 — Manager → Gerente', outcome='entender mercado, posicionamiento, canales, conversión, retención y crecimiento',
refs=['kotler-marketing','sharp-brands','dunford-obvious','moore-chasm','ellis-hacking','extra-043','extra-044','extra-042','extra-048','osterwalder-business']),
12: dict(level='Etapa 3 — Manager → Gerente', outcome='convertir problemas de clientes en productos validados y outcomes medibles',
refs=['cagan-inspired','torres-discovery','osterwalder-testing','christensen-competing','ries-lean','extra-039','extra-040','extra-041','extra-038','extra-036']),
13: dict(level='Etapa 4 — Gerente → Director', outcome='formular y ejecutar elecciones coherentes sobre dónde jugar y cómo ganar',
refs=['porter-strategy','porter-advantage','rumelt-good','lafley-winning','extra-033','extra-034','extra-032','extra-051','kaplan-scorecard','kim-blue']),
14: dict(level='Etapa 4 — Gerente → Director', outcome='diseñar estructura, derechos de decisión, cultura y cambio como un sistema',
refs=['galbraith-design','schein-culture','kotter-leading','heath-switch','lencioni-advantage','extra-060','extra-061','extra-teamofteams','extra-053','extra-063']),
15: dict(level='Etapa 4 — Gerente → Director', outcome='gobernar riesgo, legal, cumplimiento, ciberseguridad, datos e IA de forma integrada',
refs=['coso-erm','hull-risk','nist-csf','nist-airmf','oecd-ai','extra-iso31000','extra-075','extra-076','oecd-governance','tricker-governance']),
16: dict(level='Etapa 5 — Director → CEO', outcome='pensar y decidir a nivel empresa, construir el equipo ejecutivo y asignar capital y talento',
refs=['horowitz-hard','mochary-ceo','charan-execution','drucker-effective','drucker-management','extra-090','extra-091','extra-092','goleman-primal','rumelt-good']),
17: dict(level='Etapa 5 — Director → CEO', outcome='separar propiedad, administración y supervisión para gobernar estrategia, riesgo y sucesión',
refs=['tricker-governance','oecd-governance','lebanc-boards','charan-boards','monks-governance','coso-erm','koller-valuation','extra-065','extra-066','drucker-management']),
18: dict(level='Etapa 5 — CEO → Capital allocator', outcome='decidir estructura de capital, valoración, fundraising y transacciones',
refs=['brealey-corpfin','ross-corpfin','koller-valuation','damodaran-valuation','feld-venture','dePamphilis-ma','extra-050','oecd-governance','horowitz-hard','wasserman-founders']),
19: dict(level='Etapa 5 — CEO → Transformador digital', outcome='gobernar tecnología, datos e IA como capacidades económicas y organizacionales',
refs=['iansiti-ai','davenport-allin','westerman-digital','mcafee-machine','forsgren-accelerate','extra-027','extra-068','extra-069','nist-csf','nist-airmf']),
20: dict(level='Etapa 6 — Founder', outcome='descubrir, validar y lanzar una empresa antes de escalarla',
refs=['blank-four','osterwalder-business','aulet-disciplined','wasserman-founders','ries-lean','osterwalder-testing','extra-041','extra-038','horowitz-hard','drucker-effective']),
21: dict(level='Etapa 6 — Founder en Chile', outcome='formalizar y operar una empresa chilena con comprensión ejecutiva de obligaciones y escalamiento profesional',
refs=['sii-official','res-official','dt-official','bcn-labor','suseso-official','previsionsocial-official','sp-official','afc-official','inapi-official','sercotec-official','chilecompra-official','corfo-official','cmf-official','drucker-management','armstrong-hrm','noe-hrm','oecd-governance','coso-erm']),
22: dict(level='Etapa 6 — Business Owner', outcome='reducir dependencia del fundador mediante sistemas, líderes, controles y gobierno proporcional',
refs=['gerber-emyth','harnish-scaling','sutton-scaling','extra-057','extra-058','horowitz-hard','drucker-management','galbraith-design','oecd-governance','koller-valuation']),
23: dict(level='Etapa 6 — Independencia', outcome='construir independencia mediante capacidades monetizables, sistemas comerciales y diversificación prudente',
refs=['drucker-effective','drucker-management','gerber-emyth','taleb-antifragile','aulet-disciplined','ries-lean','extra-086','extra-087','extra-090','wasserman-founders']),
}

# Cada fila: core | conceptos (term=definition;...) | método (step;...) | evidencia (metric;...) | caso | límite
SPECS: dict[int,dict] = {}
TOPIC_NOTES={}

def add(i, core, concepts, method, evidence, case, limit):
    SPECS[i]=dict(core=core, concepts=concepts, method=method, evidence=evidence, case=case, limit=limit)

def parse_pairs(s):
    out=[]
    for item in s.split(';'):
        item=item.strip()
        if not item: continue
        if '=' in item:
            a,b=item.split('=',1); out.append((a.strip(),b.strip()))
        else: out.append((item,item))
    return out

def parse_list(s): return [x.strip() for x in s.split(';') if x.strip()]

def title_from_dir(d):
    t=d.name.split('-',1)[1].replace('-',' ')
    return t[0].upper()+t[1:]

def cite_book(key, topic):
    b=BOOKS.get(key)
    if not b: return f'- {key} — referencia temática para {topic}.'
    return f"- {b['author']} — *{b['title']}*. Lectura dirigida: secciones relacionadas con **{topic.lower()}**."

def sources_for(part, cid, title):
    keys=PARTS[part]['refs']
    # Rotación controlada: conserva las fuentes rectoras y cambia las complementarias por clase.
    n=len(keys); offset=(cid-1)%n
    chosen=[]
    for k in [keys[0],keys[1],keys[(offset+2)%n],keys[(offset+4)%n],keys[(offset+6)%n],keys[(offset+8)%n]]:
        if k not in chosen: chosen.append(k)
    while len(chosen)<6:
        for k in keys:
            if k not in chosen: chosen.append(k)
            if len(chosen)>=6: break
    return [cite_book(k,title) for k in chosen[:6]]

def official_extra(part,title,cid):
    low=title.lower()
    extra=[]
    if part==9:
        if any(x in low for x in ('estado','balance','flujo','margen','capital de trabajo')):
            extra.append('- IFRS Foundation — *IFRS Accounting Standards*. **Uso en esta clase:** normas IFRS/IAS aplicables a la presentación y lectura de estados financieros. Verificar edición vigente en <https://www.ifrs.org/>.')
    if part==15:
        if 'ciber' in low: extra.append('- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** funciones de gobierno, identificación, protección, detección, respuesta y recuperación como marco de la decisión. Fuente primaria: <https://www.nist.gov/cyberframework>.')
        if 'ia' in low: extra.append('- NIST — *AI Risk Management Framework (AI RMF 1.0)*. **Uso en esta clase:** gobernar, mapear, medir y gestionar el riesgo de sistemas de IA en la decisión de la clase. Fuente primaria: <https://www.nist.gov/itl/ai-risk-management-framework>.')
        if 'riesgo' in low or 'controles' in low: extra.append('- COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. **Uso en esta clase:** integrar riesgo, estrategia y desempeño en el diseño de controles. Fuente institucional: <https://www.coso.org/>.')
    if part==17:
        extra.append('- OECD — *G20/OECD Principles of Corporate Governance 2023*. **Uso en esta clase:** derechos de accionistas, deberes del directorio y divulgación como referencia de gobierno. Fuente primaria: <https://www.oecd.org/en/publications/2023/09/g20-oecd-principles-of-corporate-governance-2023_60836fcb.html>.')
    if part==19:
        if 'ciber' in low: extra.append('- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** funciones de gobierno, identificación, protección, detección, respuesta y recuperación como marco de la decisión. Fuente primaria: <https://www.nist.gov/cyberframework>.')
        if 'ia' in low: extra.append('- NIST — *AI Risk Management Framework (AI RMF 1.0)*. **Uso en esta clase:** gobernar, mapear, medir y gestionar el riesgo de sistemas de IA en la decisión de la clase. Fuente primaria: <https://www.nist.gov/itl/ai-risk-management-framework>.')
    if part==21:
        # Las clases chilenas reciben fuentes oficiales específicas más abajo.
        mapping={
        253:['- Servicio de Impuestos Internos (Chile) — *SII Educa: inicio de actividades y formalización de un negocio*. **Uso en esta clase:** comprobar en origen los pasos de formalización de un negocio en Chile. Fuente primaria: <https://www.sii.cl/siieduca/aprende-con-nosotros/inicio-de-actividades-y-formalizacion-de-un-negocio.html>.','- Registro de Empresas y Sociedades (Chile) — *Portal y documentación oficial*. **Uso en esta clase:** verificar en origen el ciclo de constitución societaria del régimen simplificado. Fuente primaria: <https://www.registrodeempresasysociedades.cl/>.'],
        254:['- Registro de Empresas y Sociedades (Chile) — *Preguntas frecuentes del portal oficial*. **Uso en esta clase:** contrastar las formas societarias disponibles antes de elegir persona natural o jurídica. Fuente primaria: <https://www.registrodeempresasysociedades.cl/FAQ.aspx>.','- Servicio de Impuestos Internos (Chile) — *Portal Emprendedor*. **Uso en esta clase:** verificar obligaciones tributarias iniciales según la forma jurídica elegida. Fuente primaria: <https://www.sii.cl/portales/emprendedor/>.'],
        255:['- Registro de Empresas y Sociedades (Chile) — *Preguntas frecuentes del portal oficial*. **Uso en esta clase:** cotejar el panorama de tipos societarios que la clase compara. Fuente primaria: <https://www.registrodeempresasysociedades.cl/FAQ.aspx>.','- Biblioteca del Congreso Nacional de Chile — *LeyChile: Ley N.º 20.659 y normativa vinculada*. **Uso en esta clase:** leer el texto vigente del régimen simplificado antes de decidir el tipo societario. Fuente primaria: <https://www.bcn.cl/leychile/>.'],
        256:['- Servicio de Impuestos Internos (Chile) — *Ciclo de vida del contribuyente: inicio de actividades*. **Uso en esta clase:** situar el inicio de actividades dentro del ciclo tributario completo. Fuente primaria: <https://www.sii.cl/destacados/educacion/ciclo_vida_contribuyente/paso_02.html>.','- Servicio de Impuestos Internos (Chile) — *Ayudas para el inicio de actividades*. **Uso en esta clase:** comprobar requisitos y formularios reales del trámite antes de planificarlo. Fuente primaria: <https://www.sii.cl/pagina/registro_contribuyentes/ayudas_inicio_actividades.htm>.'],
        257:['- Servicio de Impuestos Internos (Chile) — *Guías, normativa y servicios oficiales*. **Uso en esta clase:** verificar en origen documentos tributarios electrónicos e IVA vigentes. Fuente primaria: <https://www.sii.cl/>.','- Biblioteca del Congreso Nacional de Chile — *LeyChile: Código Tributario y Ley sobre Impuesto a las Ventas y Servicios*. **Uso en esta clase:** leer el texto vigente que sostiene las obligaciones descritas en la clase. Fuente primaria: <https://www.bcn.cl/leychile/>.'],
        258:['- Servicio de Impuestos Internos (Chile) — *Guías, normativa y servicios oficiales*. **Uso en esta clase:** confirmar declaraciones, registros y calendario tributario aplicables. Fuente primaria: <https://www.sii.cl/>.','- Colegio de Contadores de Chile — *Normativa contable aplicable y NIIF según tipo de entidad*. **Uso en esta clase:** determinar qué marco contable rige a la entidad antes de diseñar el control documental. Verificar alcance según entidad; localizador pendiente de fuente primaria estable.'],
        259:['- Comisión para el Mercado Financiero (Chile) — *Normativa e información del mercado financiero*. **Uso en esta clase:** verificar qué instituciones y productos financieros están regulados y supervisados. Fuente primaria: <https://www.cmfchile.cl/>.','- Servicio de Impuestos Internos (Chile) — *Acreditación de inicio de actividades y obligaciones tributarias*. **Uso en esta clase:** comprobar qué acredita el banco al abrir la cuenta de la empresa. Fuente primaria: <https://www.sii.cl/destacados/ley_cumplimiento_obligaciones_tributarias/inicio_actividades.html>.'],
        260:['- Dirección del Trabajo (Chile) — *Contrato individual de trabajo*. **Uso en esta clase:** contrastar el contrato descrito con la orientación oficial vigente. Fuente primaria: <https://dt.gob.cl/portal/1626/w3-article-100172.html>.','- Dirección del Trabajo (Chile) — *Cláusulas mínimas del contrato de trabajo*. **Uso en esta clase:** verificar qué cláusulas son obligatorias antes de redactar. Fuente primaria: <https://www.dt.gob.cl/portal/1628/w3-article-60800.html>.','- Dirección del Trabajo (Chile) — *Implementación de la rebaja de jornada a 42 horas (Ord. N°253/21)*. **Uso en esta clase:** comprobar la fecha y el alcance de la rebaja de jornada antes de planificar turnos. Fuente primaria: <https://dt.gob.cl/legislacion/1624/w3-article-129189.html>.','- Dirección del Trabajo (Chile) — *Ley Karin y dictámenes asociados*. **Uso en esta clase:** revisar las obligaciones de prevención e investigación que impone la ley. Fuente primaria: <https://www.dt.gob.cl/legislacion/1624/w3-propertyvalue-194488.html>.','- Biblioteca del Congreso Nacional de Chile — *LeyChile: Código del Trabajo (texto vigente)*. **Uso en esta clase:** leer el articulado que regula la relación laboral analizada. Fuente primaria: <https://www.bcn.cl/leychile/navegar?idNorma=207436>.','- Subsecretaría de Previsión Social (Chile) — *Decreto Supremo N°44 y material de implementación*. **Uso en esta clase:** verificar las obligaciones de prevención de riesgos que recaen en el empleador. Fuente primaria: <https://previsionsocial.gob.cl/ds44/>.','- Superintendencia de Seguridad Social (Chile) — *Normativa del Seguro de Accidentes del Trabajo y Enfermedades Profesionales*. **Uso en esta clase:** confirmar cobertura y obligaciones de la Ley N°16.744 en el caso de la clase. Fuente primaria: <https://www.suseso.cl/>.'],
        261:['- INAPI (Chile) — *Propiedad industrial y orientación oficial*. **Uso en esta clase:** comprobar qué protege una marca o patente y cómo se solicita. Fuente primaria: <https://www.inapi.cl/>.','- Departamento de Derechos Intelectuales (Chile) — *Derecho de autor: registro y orientación oficial*. **Uso en esta clase:** distinguir qué queda cubierto por derecho de autor y no por propiedad industrial. Fuente primaria: <https://www.propiedadintelectual.gob.cl/>.'],
        262:['- ChileAtiende — *Trámites y orientación del Estado*. **Uso en esta clase:** ubicar el trámite de permisos y patente y la municipalidad competente según giro. Fuente primaria: <https://www.chileatiende.gob.cl/>.','- Servicio de Impuestos Internos (Chile) — *SII Educa: inicio de actividades y formalización de un negocio*. **Uso en esta clase:** comprobar en origen qué exige la formalización antes de tramitar permisos y patente. Fuente primaria: <https://www.sii.cl/siieduca/aprende-con-nosotros/inicio-de-actividades-y-formalizacion-de-un-negocio.html>.'],
        263:['- Dirección ChileCompra — *Mercado Público y normativa de compras públicas*. **Uso en esta clase:** verificar cómo se accede realmente a la demanda del Estado. Fuente primaria: <https://www.chilecompra.cl/>.','- Sercotec (Chile) — *Programas, capacitación y Centros de Desarrollo de Negocios*. **Uso en esta clase:** comprobar qué apoyo público está disponible y con qué requisitos. Fuente primaria: <https://www.sercotec.cl/>.','- Corporación de Fomento de la Producción (Chile) — *Programas, instrumentos y apoyo empresarial*. **Uso en esta clase:** contrastar los instrumentos de financiamiento e innovación vigentes. Fuente primaria: <https://www.corfo.cl/>.'],
        264:['- Servicio de Impuestos Internos (Chile) — *Portal Emprendedor*. **Uso en esta clase:** verificar obligaciones tributarias iniciales según la forma jurídica elegida. Fuente primaria: <https://www.sii.cl/portales/emprendedor/>.','- Registro de Empresas y Sociedades (Chile) — *Portal y documentación oficial*. **Uso en esta clase:** revisar el estado societario y los trámites pendientes del checklist de la clase. Fuente primaria: <https://www.registrodeempresasysociedades.cl/>.','- Dirección del Trabajo (Chile) — *Normativa y orientación oficial*. **Uso en esta clase:** revisar las obligaciones laborales pendientes del checklist. Fuente primaria: <https://www.dt.gob.cl/>.','- INAPI (Chile) — *Propiedad industrial y orientación oficial*. **Uso en esta clase:** revisar el estado de los activos de propiedad industrial del checklist. Fuente primaria: <https://www.inapi.cl/>.'],
        }
        extra.extend(mapping.get(cid,[]))
    return extra

def artifact_for(title,cid):
    low=title.lower()
    if any(x in low for x in ('financ','margen','roi','valor','capital','presupuesto','cash','flujo','break-even','unit economics')): return 'modelo-financiero-y-memo-de-decision.md'
    if any(x in low for x in ('equipo','talento','feedback','coaching','one-on-one','desempeno','desempeño','cargo','seleccion','selección','sucesion','sucesión')): return 'people-decision-brief.md'
    if any(x in low for x in ('estrateg','compet','modelo de negocio','crecimiento','portfolio','portafolio')): return 'strategy-memo.md'
    if any(x in low for x in ('proceso','operacion','operación','calidad','capacidad','sla','automatizacion','automatización')): return 'operating-improvement-brief.md'
    if any(x in low for x in ('venta','pipeline','pricing','negoci','cliente','marketing','marca','canal','funnel','retencion','retención')): return 'commercial-decision-brief.md'
    if any(x in low for x in ('producto','mvp','discovery','protot','roadmap','market fit','experimento')): return 'product-evidence-brief.md'
    if any(x in low for x in ('riesgo','legal','contrato','privacidad','ciber','compliance','continuidad','ia')): return 'risk-governance-brief.md'
    if any(x in low for x in ('directorio','board','gobierno','ceo')): return 'board-or-executive-memo.md'
    if cid>=241: return 'founder-owner-decision-brief.md'
    return 'leadership-decision-brief.md'

def book_label(key):
    b=BOOKS.get(key, {})
    return f"{b.get('author', key)} — *{b.get('title', key)}*"

SOURCE_PERSPECTIVES={
'drucker-effective':'efectividad ejecutiva, contribución, prioridades y uso consciente del tiempo',
'drucker-management':'responsabilidad gerencial, propósito, organización y resultados',
'grove-output':'output managerial, leverage, reuniones, indicadores y gestión por procesos',
'kahneman-thinking':'sesgos, juicio bajo incertidumbre y límites de la intuición',
'klein-sources':'reconocimiento de patrones y decisión naturalista en contextos reales',
'duke-thinking':'calidad de la decisión separada del resultado y razonamiento probabilístico',
'senge-fifth':'pensamiento sistémico, bucles de retroalimentación y aprendizaje organizacional',
'fisher-getting':'negociación basada en intereses, opciones y criterios objetivos',
'voss-never':'negociación táctica, escucha, calibración y manejo de información imperfecta',
'cialdini-influence':'mecanismos de influencia y sus límites éticos',
'heath-made':'diseño de mensajes memorables, concretos y accionables',
'goleman-ei':'autoconciencia, autorregulación, empatía y habilidades sociales',
'goleman-primal':'impacto emocional del liderazgo y estilos de conducción',
'heifetz-line':'distinción entre problemas técnicos y desafíos adaptativos',
'edmondson-fearless':'seguridad psicológica, aprendizaje, voz y manejo productivo del error',
'hackman-leading':'condiciones de efectividad de equipos y diseño del trabajo colectivo',
'lencioni-five':'confianza, conflicto, compromiso, accountability y resultados',
'extra-katzenbach':'propósito compartido, habilidades complementarias y responsabilidad mutua',
'armstrong-hrm':'arquitectura de recursos humanos, desempeño, recompensa y relaciones laborales',
'noe-hrm':'selección, desarrollo, evaluación, compensación y gestión estratégica de personas',
'buckingham-first':'rol del manager, fortalezas, expectativas y desempeño individual',
'sutton-goodboss':'conductas concretas de buenos jefes y reducción de daño organizacional',
'pmi-pmbok':'gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor',
'kerzner-project':'integración de proyectos, control, madurez y alineación organizacional',
'schwaber-scrum':'empirismo, transparencia, inspección y adaptación',
'anderson-kanban':'flujo, trabajo en proceso, políticas explícitas y evolución del sistema',
'forsgren-accelerate':'métricas de entrega, capacidades técnicas y desempeño organizacional',
'goldratt-goal':'restricciones, throughput, inventario y pensamiento de flujo',
'slack-operations':'capacidad, procesos, variabilidad, calidad y estrategia de operaciones',
'deming-crisis':'variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad',
'womack-lean':'valor, flujo, pull, desperdicio y mejora continua',
'doerr-okrs':'objetivos, resultados clave, foco, transparencia y cadencia de seguimiento',
'kaplan-scorecard':'traducción de estrategia a objetivos, indicadores y relaciones causales',
'marr-kpi':'selección de métricas útiles y conexión entre indicadores y decisiones',
'charan-execution':'disciplina de ejecución, personas, estrategia y operaciones',
'brealey-corpfin':'valor del dinero, riesgo, costo de capital, inversión y financiación',
'ross-corpfin':'decisiones de inversión, financiación, capital de trabajo y valoración',
'koller-valuation':'drivers de valor, ROIC, crecimiento y valoración por flujo descontado',
'damodaran-valuation':'valoración, riesgo, narrativas, costo de capital y supuestos explícitos',
'horngren-managerial':'costos relevantes, presupuestos, variaciones y decisiones gerenciales',
'kieso-accounting':'reconocimiento, medición y presentación de estados financieros y sus partidas',
'penman-fsa':'reformulación de estados, calidad del resultado y análisis de rentabilidad para valoración',
'palepu-analysis':'estrategia, análisis contable, análisis financiero y proyección integrados',
'schilit-shenanigans':'señales de calidad de resultados, partidas no recurrentes y posibles distorsiones contables',
'rackham-spin':'venta consultiva basada en preguntas de situación, problema, implicación y necesidad',
'dixon-challenger':'venta compleja, insight comercial, enseñanza y control constructivo del proceso',
'kotler-marketing':'segmentación, targeting, posicionamiento, propuesta de valor y marketing mix',
'sharp-brands':'disponibilidad mental y física, penetración y patrones empíricos de crecimiento de marcas',
'dunford-obvious':'posicionamiento desde alternativas competitivas, atributos, valor y segmento',
'moore-chasm':'adopción tecnológica y transición entre segmentos de mercado',
'ellis-hacking':'experimentación de crecimiento, loops y aprendizaje orientado a métricas',
'cagan-inspired':'equipos de producto, discovery, riesgos de producto y outcomes',
'torres-discovery':'discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia',
'osterwalder-testing':'hipótesis de negocio, experimentos, evidencia y reducción de riesgo',
'christensen-competing':'jobs to be done y comprensión causal de por qué un cliente elige una solución',
'ries-lean':'build-measure-learn, MVP y aprendizaje validado',
'porter-strategy':'trade-offs, posicionamiento, fit y ventaja competitiva',
'porter-advantage':'cadena de valor, actividades y fuentes de ventaja de costo o diferenciación',
'rumelt-good':'diagnóstico, política guía y acciones coherentes',
'lafley-winning':'elecciones integradas de dónde jugar y cómo ganar',
'galbraith-design':'alineación de estrategia, estructura, procesos, recompensas y personas',
'schein-culture':'supuestos básicos, valores declarados y artefactos culturales',
'kotter-leading':'urgencia, coalición, visión, movilización y consolidación del cambio',
'heath-switch':'dirección racional, motivación emocional y diseño del entorno para cambiar conducta',
'coso-erm':'riesgo integrado con estrategia, desempeño, revisión e información',
'hull-risk':'identificación y medición de riesgos financieros y no financieros',
'nist-csf':'gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad',
'nist-airmf':'gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida',
'oecd-ai':'principios para IA confiable, responsable y centrada en las personas',
'horowitz-hard':'decisiones difíciles de CEO, organización, personas y ejecución bajo presión',
'mochary-ceo':'sistemas operativos del CEO, comunicación, accountability y equipo ejecutivo',
'tricker-governance':'separación entre dirección, supervisión, accountability y gobierno corporativo',
'oecd-governance':'derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno',
'lebanc-boards':'comportamiento efectivo del directorio, composición y dinámica de gobierno',
'charan-boards':'directorios que contribuyen a estrategia, talento, riesgo y sucesión',
'feld-venture':'term sheets, economics/control y negociación de venture capital',
'dePamphilis-ma':'proceso de M&A, valoración, due diligence, negociación e integración',
'iansiti-ai':'modelo operativo AI-first, escala digital, redes y arquitectura de decisión',
'davenport-allin':'casos empresariales, estrategia y organización para inteligencia artificial',
'westerman-digital':'transformación digital desde capacidades de liderazgo y capacidades digitales',
'blank-four':'customer development y búsqueda sistemática de un modelo de negocio',
'osterwalder-business':'diseño de modelos de negocio mediante propuesta, clientes, recursos y economía',
'aulet-disciplined':'secuencia disciplinada desde mercado inicial hasta economía y diseño del negocio',
'wasserman-founders':'dilemas de fundador, equity, control, equipo y decisiones tempranas',
'gerber-emyth':'diferencia entre técnico, manager y empresario; sistematización del negocio',
'harnish-scaling':'personas, estrategia, ejecución y caja durante el escalamiento',
'sutton-scaling':'cómo propagar excelencia sin multiplicar burocracia y daño',
'taleb-antifragile':'fragilidad, opcionalidad, redundancia y exposición asimétrica al riesgo',
'extra-pricing':'arquitectura de precios basada en valor, segmentación y respuesta competitiva',
'extra-minto':'estructura piramidal para razonamiento y comunicación ejecutiva',
'extra-duarte':'diseño narrativo de presentaciones que movilizan una audiencia',
'extra-humbleinquiry':'preguntas que reducen jerarquía defensiva y mejoran información',
'extra-teamofteams':'adaptabilidad, conciencia compartida y ejecución descentralizada',
'extra-iso31000':'principios, marco y proceso de gestión de riesgos',
'extra-iso22301':'sistema de gestión de continuidad y preparación ante disrupciones',
'extra-iso9001':'gestión de calidad basada en procesos, evidencia y mejora',
'sii-official':'obligaciones tributarias y ciclo de vida del contribuyente en Chile',
'res-official':'constitución y modificaciones societarias en el Registro de Empresas y Sociedades',
'dt-official':'relaciones laborales, contratos, jornada y fiscalización laboral chilena',
'inapi-official':'propiedad industrial, marcas, patentes y activos intangibles en Chile',
'sercotec-official':'desarrollo empresarial y apoyo a micro y pequeñas empresas en Chile',
'bcn-labor':'texto legal vigente del Código del Trabajo y leyes laborales chilenas',
'suseso-official':'seguro de accidentes y enfermedades profesionales, prevención y jurisprudencia administrativa',
'previsionsocial-official':'gestión preventiva de riesgos laborales y marco del Decreto Supremo N°44',
'sp-official':'obligaciones y reglas del sistema previsional chileno',
'afc-official':'Seguro de Cesantía, cotizaciones y prestaciones',
'cmf-official':'regulación e información financiera y de mercados en Chile',
'chilecompra-official':'compras públicas, registro de proveedores y Mercado Público',
'corfo-official':'instrumentos de desarrollo productivo, innovación y financiamiento empresarial',
}

def source_perspective(key):
    b=BOOKS.get(key,{})
    return SOURCE_PERSPECTIVES.get(key, f"perspectiva de {b.get('area','la disciplina')} aplicada al problema de la clase")

def class_sources(part,cid,title):
    keys=PARTS[part]['refs']
    low=title.lower()
    priority=[]
    if part==9:
        if any(x in low for x in ('estado de resultados','balance','estado de situacion','estado de situación','flujo de efectivo','estados financieros')):
            priority=['kieso-accounting','penman-fsa','palepu-analysis','schilit-shenanigans']
        elif any(x in low for x in ('costo','presupuesto','break-even','margen','unit economics')):
            priority=['horngren-managerial','brealey-corpfin','ross-corpfin']
        elif any(x in low for x in ('valor','roi','roic','capital de trabajo')):
            priority=['koller-valuation','damodaran-valuation','brealey-corpfin','ross-corpfin']
    if part==21:
        if cid==260: priority=['dt-official','bcn-labor','suseso-official','previsionsocial-official','noe-hrm','armstrong-hrm']
        elif cid==261: priority=['inapi-official','drucker-management','oecd-governance']
        elif cid==259: priority=['cmf-official','sii-official','res-official','drucker-management']
        elif cid in (253,256,257,258): priority=['sii-official','res-official','drucker-management']
        elif cid==263: priority=['chilecompra-official','sercotec-official','corfo-official','drucker-management']
        else: priority=['res-official','sii-official','dt-official']
    offset=(cid-1)%len(keys)
    order=priority+[keys[0],keys[1],keys[(offset+2)%len(keys)],keys[(offset+5)%len(keys)],keys[(offset+7)%len(keys)],keys[(offset+9)%len(keys)]]
    chosen=[]
    for k in order+keys:
        if k in BOOKS and k not in chosen: chosen.append(k)
        if len(chosen)==6: break
    return chosen

def concept_development(title, concepts, method, evidence, source_keys, spec):
    # Cinco funciones pedagógicas distintas. La estructura es estable, el desarrollo no.
    c=concepts[:5]
    while len(c)<5: c.append(c[-1])
    m=method or ['formular','diagnosticar','decidir','ejecutar','revisar']
    e=evidence or ['evidencia observable']
    def src(i):
        k=source_keys[i%len(source_keys)]
        return book_label(k), source_perspective(k)
    s0,p0=src(0); s1,p1=src(1); s2,p2=src(2); s3,p3=src(3); s4,p4=src(4)
    return f'''### 1. {c[0][0]}: mecanismo central

**{c[0][0]}** se entiende aquí como **{c[0][1]}**. Esta es la pieza causal o estructural desde la que se inicia **{title.lower()}**: antes de {m[0].lower()}, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es {s0}. Su aporte se usa para examinar **{p0}**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **{e[0]}**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **{c[1][0]}**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. {c[1][0]}: frontera conceptual y error de clasificación

**Definición operacional:** {c[1][1]}. Su valor está en distinguirlo de **{c[0][0]}** y **{c[2][0]}**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con {s1}, que aporta una mirada sobre **{p1}**. Formula dos mini-casos: uno que sí satisface la definición de **{c[1][0]}** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **{e[1%len(e)]}** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de {m[1%len(m)].lower()}, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. {c[2][0]}: operacionalización y medición

**{c[2][0]}** significa **{c[2][1]}**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

{s2} orienta este bloque mediante **{p2}**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **{e[2%len(e)]}**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a {m[2%len(m)].lower()}, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. {c[3][0]}: trade-offs y efectos de segundo orden

**Definición:** {c[3][1]}. Este concepto obliga a abandonar la idea de que **{title.lower()}** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de {m[3%len(m)].lower()}, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

{s3} aporta una lente sobre **{p3}**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **{e[3%len(e)]}** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **{title.lower()}**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **{c[3][0]}** y otro de una hipótesis del caso que nunca fue validada.

### 5. {c[4][0]}: gobernanza, límites e integración

**{c[4][0]}** se define como **{c[4][1]}** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

{s4} se utiliza para estudiar **{p4}** y contrastar la recomendación final. Al ejecutar {m[4%len(m)].lower()}, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **{spec['limit']}**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **{c[0][0]}**, **{c[1][0]}**, **{c[2][0]}**, **{c[3][0]}** y **{c[4][0]}** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.'''


def worked_example(title, spec, concepts, method, evidence):
    rows=[]
    for i,step in enumerate(method):
        metric=evidence[i%len(evidence)] if evidence else 'evidencia disponible'
        concept=concepts[i%len(concepts)][0]
        rows.append(f'''**Paso {i+1} — {step}.** La gerencia escribe primero el supuesto asociado a **{concept}** y evita convertirlo en hecho. Luego busca **{metric}** para contrastarlo en el caso de **{title.lower()}**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.''')
    return '\n\n'.join(rows)

def build(cid, d, part):
    title=title_from_dir(d)
    spec=SPECS[cid]
    concepts=parse_pairs(spec['concepts'])
    method=parse_list(spec['method'])
    evidence=parse_list(spec['evidence'])
    profile=PARTS[part]
    source_keys=class_sources(part,cid,title)
    concept_rows='\n'.join(f'| **{a}** | {b} | Distingue un hecho compatible y otro que lo refute. |' for a,b in concepts)
    pipeline=' → '.join(f'{i+1}. {s}' for i,s in enumerate(method))
    method_rows='\n'.join(f'| {i+1} | {s} | {evidence[i%len(evidence)] if evidence else "evidencia disponible"} | Decisión/supuesto fechado |' for i,s in enumerate(method))
    ev_rows='\n'.join(f'| **{x}** | Baseline + tendencia + segmentación | ¿Qué interpretación alternativa también explicaría la señal? |' for x in evidence)
    source_rows='\n'.join(f'| {book_label(k)} | {source_perspective(k)} | ¿Qué supuesto de **{title.lower()}** ayuda a desafiar? |' for k in source_keys[:5])
    development=concept_development(title,concepts,method,evidence,source_keys,spec)
    toolbox=TOPIC_NOTES.get(cid,'')
    toolbox_section=(f'\n\n## 🔧 Profundización específica\n\n{toolbox}' if toolbox else '')
    example=worked_example(title,spec,concepts,method,evidence)
    err=[
      (f'Usar {concepts[0][0]} y {concepts[1][0]} como sinónimos',f'Se pierde la distinción entre “{concepts[0][1]}” y “{concepts[1][1]}”','Vuelve a los observables y exige una señal distinta para cada concepto.'),
      (f'Empezar por “{method[-1]}”',f'Se saltó “{method[0]}” y la solución llegó antes que el diagnóstico',f'Reconstruye la cadena {pipeline} y marca el primer supuesto no demostrado.'),
      (f'Optimizar solo {evidence[0] if evidence else "una métrica"}','La métrica local sustituyó al resultado del sistema',f'Contrástala con {evidence[1] if len(evidence)>1 else "una segunda señal"} y explicita el costo de oportunidad.'),
      ('Generalizar desde un caso favorable',f'Se confundió evidencia local con una regla universal sobre {title.lower()}',spec['limit']),
      ('No fijar revisión',f'Una decisión sobre {title.lower()} se vuelve permanente por inercia','Define responsable, fecha, señal de éxito y condición de stop.'),
    ]
    err_rows='\n'.join(f'| {a} | {b} | {c} |' for a,b,c in err)
    lens=[
      ('Profesional',f'usa **{title.lower()}** para mejorar una contribución propia y explicar sus supuestos con evidencia.'),
      ('Jefe / Team Lead',f'aplica **{concepts[0][0]}** y **{concepts[1][0]}** para coordinar personas sin sustituir conversación por métricas.'),
      ('Manager / Gerente',f'conecta {evidence[0] if evidence else "la evidencia"} con capacidad, presupuesto, dependencias y riesgo interáreas.'),
      ('CEO / Director',f'decide si {title.lower()} cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio.'),
      ('Founder / Owner',f'pregunta si la solución de {title.lower()} reduce dependencia del fundador, preserva caja y puede operar como sistema repetible.'),
    ]
    lens_rows='\n'.join(f'| **{a}** | {b} |' for a,b in lens)
    q=[
      f'Explica la diferencia entre **{concepts[0][0]}** y **{concepts[1][0]}** usando un ejemplo donde elegir mal cambie la decisión.',
      f'¿Qué observarías para validar **{concepts[2][0]}** y qué observación obligaría a rechazar tu interpretación?',
      f'Aplica **{method[0]} → {method[1] if len(method)>1 else method[0]}** al caso de la clase. ¿Qué dato todavía falta?',
      f'¿Por qué **{evidence[0] if evidence else "la señal principal"}** no basta por sí sola para atribuir causalidad?',
      f'Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **{title.lower()}**?',
      f'¿Qué decisión equivocada podría producirse si se ignora este límite: **{spec["limit"]}**?',
    ]
    questions='\n'.join(f'{i+1}. {x}' for i,x in enumerate(q))
    art=artifact_for(title,cid)
    refs=[]
    for k in source_keys:
        b=BOOKS[k]
        refs.append(f"- {b['author']} — *{b['title']}*. **Uso en esta clase:** {source_perspective(k)}. Lectura selectiva: índice/capítulos pertinentes a **{title.lower()}**; registra edición y páginas consultadas.")
    refs += official_extra(part,title,cid)
    refs += [
      f'- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **{title.lower()}** sobre conocimiento previo verificable.',
      f'- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **{title.lower()}**.',
      f'- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **{title.lower()}** desde el desempeño observable y no desde el temario.',
      f'- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **{title.lower()}** en práctica deliberada con criterios explícitos.',
      f'- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **{title.lower()}** como problema, evidencia, alternativas y recomendación.',
    ]
    # Una misma obra puede llegar por la bibliografia de la parte y por la lista
    # de fuentes oficiales. Se cita una sola vez, y gana la linea que trae el
    # enlace a la fuente primaria.
    unicas={}; orden=[]
    for linea in refs:
        clave=linea.split('**Uso en esta clase:**')[0]
        if clave in unicas:
            pos=unicas[clave]
            if 'Fuente primaria' in linea and 'Fuente primaria' not in orden[pos]:
                orden[pos]=linea
            continue
        unicas[clave]=len(orden); orden.append(linea)
    refs=orden
    source_text='\n'.join(refs)
    return f'''# Clase {cid:03d} — {title}

**Parte:** {part:02d} — {d.parents[1].name.split('-',1)[1].replace('-', ' ').title()}  
**Nivel:** {profile['level']}  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

{spec['core']}

La salida de esta parte es **{profile['outcome']}**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **{title.lower()}** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** {', '.join('`'+a+'`' for a,_ in concepts[:5])} mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de {profile['level'].split('—')[-1].strip().lower()}.
3. **Aplicar** la secuencia **{pipeline}** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** {', '.join(evidence[:3])} sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define {concepts[0][0]} y {concepts[1][0]} sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con {evidence[0] if evidence else 'evidencia'} y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
{concept_rows}

## 🧠 Modelo mental

```text
{pipeline}
```

La secuencia nace del problema de esta clase: **{spec['core']}** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **{spec['limit']}**

## 📖 Desarrollo

{development}

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **{title.lower()}** no consiste en sumar cinco definiciones. Empieza por **{concepts[0][0]}**, contrasta **{concepts[1][0]}** con **{concepts[2][0]}**, incorpora **{concepts[3][0]}** como restricción o mecanismo y usa **{concepts[4][0]}** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **{pipeline}**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.{toolbox_section}

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
{source_rows}

En **{title.lower()}**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **{concepts[0][0]}**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** {spec['case']}

{example}

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **{title.lower()}**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **{concepts[0][0]}** | {concepts[0][1]} | Cuando {evidence[0] if evidence else 'la evidencia principal'} es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **{concepts[1][0]}** | {concepts[1][1]} | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** {spec['limit']}

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre {title.lower()} |
|---|---|
{lens_rows}

El cambio de nivel en **{title.lower()}** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

{spec['case']}

Entrega un **decision brief de {title.lower()}** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **{title.lower()}** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **{pipeline}** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta {', '.join(evidence[:2])}; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
{err_rows}

## ❓ Preguntas de comprobación

{questions}

## 📥 Entregable

Guarda en `portfolio/{cid:03d}-{d.name.split('-',1)[1]}/`:

- `{art}` con el problema específico de **{title.lower()}**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **{title.lower()}** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **{concepts[0][0]}**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **{spec['case']}** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

{source_text}

> **Regla de fuentes para {title}:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **{title.lower()}** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
'''

def lesson_yaml(cid,d,part):
    title=title_from_dir(d); spec=SPECS[cid]
    concepts=parse_pairs(spec['concepts']); method=parse_list(spec['method']); evidence=parse_list(spec['evidence'])
    source_keys=class_sources(part,cid,title)
    def q(x): return '"'+str(x).replace('\\','\\\\').replace('\"','\\\"').replace('\n',' ')+'"'
    lines=[f'id: {cid}',f'part: {part:02d}',f'title: {q(title)}','duration_minutes: 150',f'level: {q(PARTS[part]["level"])}',f'outcome: {q(PARTS[part]["outcome"])}','depth_standard: deep-class-v2','source_mode: books-plus-primary','pedagogy: retrieval-case-deliberate-practice','objectives:']
    objs=[
      f'Distinguir {concepts[0][0]} de {concepts[1][0]} mediante evidencia observable.',
      f'Aplicar la secuencia: {" → ".join(method)}.',
      f'Interpretar {", ".join(evidence[:3])} sin atribuir causalidad automática.',
      f'Resolver el caso de {title.lower()} con dos alternativas y trade-offs.',
      'Contrastar dos fuentes y modificar la decisión cuando la evidencia lo exija.'
    ]
    lines += [f'  - {q(x)}' for x in objs]
    lines += [f'deliverable: {q(artifact_for(title,cid))}','references:']
    for k in source_keys:
        lines.append(f'  - {q(book_label(k))}')
    for x in official_extra(part,title,cid):
        lines.append(f'  - {q(x[2:] if x.startswith("- ") else x)}')
    lines += ['limits:',f'  - {q(spec["limit"])}','evidence_signals:']+[f'  - {q(x)}' for x in evidence]
    return '\n'.join(lines)+'\n'

def assessment(cid,d,part):
    title=title_from_dir(d); spec=SPECS[cid]
    concepts=parse_pairs(spec['concepts']); method=parse_list(spec['method']); evidence=parse_list(spec['evidence'])
    return f'''# Evaluación — Clase {cid:03d}: {title}

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **{concepts[0][0]}** de **{concepts[1][0]}** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **{concepts[2][0]}** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **{concepts[3][0]}** con **{concepts[4][0]}**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** {spec['case']}

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **{' → '.join(method)}**. Debes utilizar o diseñar cómo obtener **{', '.join(evidence[:3])}**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **{spec['limit']}**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
'''


def cargar_datos_del_curriculo(nombre, entorno):
    """Carga un módulo de datos del currículo con el entorno que necesita.

    `deep_specs.py` y `topic_notes.py` son datos, no bibliotecas: son miles de
    llamadas a `add()` y a `note()`. Antes se cargaban con `exec(compile(...))`
    sobre `globals()`, lo que mezclaba sus nombres con los de este script y hacía
    que cualquier análisis estático lo tratara —con razón— como ejecución de
    código arbitrario.

    Ahora se cargan con la maquinaria de importación: cada módulo obtiene su
    propio espacio de nombres, recibe explícitamente lo que necesita del
    entorno, y aparece con su nombre real en las trazas de error.
    """
    ruta = ROOT / 'curriculum' / nombre
    if not ruta.exists():
        return {}
    spec = importlib.util.spec_from_file_location(f'curriculum.{ruta.stem}', ruta)
    modulo = importlib.util.module_from_spec(spec)
    modulo.__dict__.update(entorno)
    spec.loader.exec_module(modulo)
    return modulo.__dict__


# `add` escribe directamente en SPECS, así que basta con prestárselo.
cargar_datos_del_curriculo('deep_specs.py', {'add': add})

# `topic_notes.py` define su propio TOPIC_NOTES; se recoge de vuelta.
TOPIC_NOTES.update(cargar_datos_del_curriculo('topic_notes.py', {}).get('TOPIC_NOTES', {}))

def main():
    missing=[]; written=0
    for m in sorted((ROOT/'modules').glob('[0-9][0-9]-*')):
        part=int(m.name[:2])
        for d in sorted((m/'classes').glob('*')):
            if not d.is_dir(): continue
            cid=int(d.name[:3])
            if cid not in SPECS:
                missing.append((cid,d.name)); continue
            (d/'README.md').write_text(build(cid,d,part),encoding='utf-8')
            (d/'assessment.md').write_text(assessment(cid,d,part),encoding='utf-8')
            (d/'lesson.yaml').write_text(lesson_yaml(cid,d,part),encoding='utf-8')
            written+=1
    if missing:
        print('Missing specs:',len(missing),missing[:20])
        return 2
    print('Written',written,'deep classes')
    return 0

if __name__=='__main__': raise SystemExit(main())
