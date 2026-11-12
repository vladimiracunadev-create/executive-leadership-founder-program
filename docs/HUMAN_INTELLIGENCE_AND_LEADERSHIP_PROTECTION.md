# Inteligencia humana, influencia y protección del liderazgo

**Fecha de corte:** 2026-11-12
**Alcance:** reconocimiento y gestión de influencia indebida, manipulación
interpersonal, conflictos de interés y protección de información directiva.
**Restricción de diseño:** ampliar las clases existentes sin alterar la
arquitectura de 288 clases, 24 partes y 96 laboratorios, sin crear herramientas
de vigilancia y sin investigar la vida privada de ninguna persona.

## 1. Diagnóstico

La auditoría revisó las partes de liderazgo, inteligencia emocional, ética,
gobierno corporativo, directorios, oficina del CEO, gestión de crisis, toma de
decisiones y conflictos de interés. Cada clase conserva sus 16 secciones y sus
prerrequisitos.

Hallazgos:

- Existía cobertura sólida de sesgos (clase 016), dilemas éticos (045),
  compliance (189), crisis (190, 202), conflictos de directorio (209) y
  supervisión de riesgo (213).
- Esa cobertura trataba los conflictos como un asunto de **gobierno formal**.
  No trabajaba la **dimensión humana de la influencia**: cómo alguien puede
  orientar el juicio de un ejecutivo mediante afinidad, reciprocidad, presión o
  dependencia emocional, y cómo se previene sin vigilar a nadie.
- No había un protocolo que separe **hechos, alegaciones y juicios sobre la
  vida privada** cuando aparece una alegación sobre una persona clave.

## 2. Matriz de brechas

| Tema solicitado | Clase | Estado previo | Ampliación |
|---|---|---|---|
| Sesgo de autoridad, exceso de confianza, reciprocidad | 016 | Sesgos generales | Sesgos como vías de influencia indebida, con pregunta de control |
| Persuasión, manipulación y coerción | 016 | No distinguidas | Criterio de transparencia del interés y libertad de decidir |
| Información incompleta y juicio bajo presión | 016 | Parcial | Regla de detener, consultar y registrar |
| Dependencia emocional, lealtades | 045 | Dilemas genéricos | Prueba de tres preguntas y dilema relación-cargo |
| Canales de declaración, asesoramiento independiente | 189 | Cultura ética general | Cinco elementos de un sistema de declaración |
| Gestión de crisis y reputación ante alegaciones | 190 | Incidentes y escalamiento | Protocolo de 72 horas, presunción de inocencia |
| Decisiones irreversibles sobre personas clave | 202 | Crisis y decisiones difíciles | Cuatro escenarios con reversibilidad y disparador |
| Conflictos, influencia indebida, casos históricos | 209 | Reales, potenciales y percibidos | Cuatro casos históricos por su mecanismo |
| HUMINT, honey trap, kompromat, intermediarios | 213 | Ausentes | Glosario operacional y señales para consultar |
| Seguridad en viajes y negociaciones | 213 | Ausente | Protocolos defensivos proporcionales |

## 3. Plan de ampliación

Se amplían siete clases existentes mediante `curriculum/topic_notes.py`
(`note` y `CLASS_EXTENSIONS`) y se regeneran con
`python tools/deep_curriculum_builder.py --class N`. No se crean clases nuevas:
una ruta paralela duplicaría 16, 45, 189, 190, 202, 209 y 213, y alteraría el
conteo que validan los documentos generados. Se añade además la plantilla
`templates/influence-and-conflict-disclosure-brief.md`.

## 4. Progresión profesional

El riesgo de influencia crece con el acceso a información y el poder de
decisión; la medida de prevención pasa de la conducta personal al diseño
institucional.

| Rol | Riesgo típico | Responsabilidad | Prevención |
|---|---|---|---|
| Profesional individual | Favores, afinidad, presión de un tercero | Confidencialidad y declarar ofertas inusuales | Conocer la política, consultar antes de aceptar |
| Jefe de equipo | Presión de pares y proveedores; lealtad al equipo | Declarar conflictos que afecten evaluaciones | Doble revisión de decisiones sobre personas |
| Gerente | Acceso a información comercial y a proveedores | Abstención en decisiones con interés propio | Rotación en compras, canal confidencial |
| Director | Intermediarios y acceso a estrategia | Separar relaciones personales de evaluación | Asesoramiento independiente, registro de declaraciones |
| CEO | Atención constante; aislamiento; decisiones irreversibles | Rendir cuentas al directorio sobre relaciones relevantes | Cultura de declaración, protocolos de viaje y negociación |
| Fundador | Dependencia emocional del proyecto; poca supervisión | Crear gobierno antes de que lo exija un tercero | Asesor independiente, consejo asesor, reglas escritas |
| Propietario de empresa | Confunde patrimonio personal y empresa | Separar roles de propietario, administrador y familiar | Estatutos claros, reunión de familia y directorio mixto |

## 5. Casos históricos

Se usan por su **mecanismo**, no por la intimidad de nadie. Las fechas y
detalles deben verificarse en fuentes primarias antes de citarlos.

- **Enron y las sociedades LJM (1999–2001):** conflicto de interés dispensado
  por el directorio sin controles compensatorios reales.
- **Hewlett-Packard (2006):** investigación interna de una filtración con
  métodos engañosos para obtener registros telefónicos; abuso de autoridad.
- **Caso Profumo (1963):** el problema de gobierno fue el ocultamiento ante el
  Parlamento y el riesgo de acceso, no la vida privada en sí.
- **Caso Guillaume (1974):** un colaborador cercano de la cancillería alemana
  fue agente de la inteligencia de la RDA.
- **Cambridge Five (décadas de 1930–1950):** captación por ideología, no por
  intimidad; ilustra que el marco MICE (dinero, ideología, compromiso o
  coerción, ego) abarca más que el honey trap.

## 6. Estudio de caso: NVIDIA (en desarrollo)

**Corte de la información: 2026-11-12.** El caso sigue abierto: no existen
conclusiones públicas del comité independiente. Se usa para entrenar
razonamiento, no para emitir un juicio sobre ninguna persona.

### Hechos y alegaciones

| Afirmación | Atribución | Estado |
|---|---|---|
| El directorio de NVIDIA abrió una investigación independiente | Comunicado de la compañía, 8 de noviembre de 2026 | Hecho declarado por la empresa |
| El CEO reconoció una relación extramatrimonial en un mensaje a empleados | Mensaje del CEO publicado por la compañía | Hecho declarado por el CEO |
| El directorio dijo no tener razón para creer que se comprometió información de seguridad nacional o secretos de la empresa | Comunicado de la compañía | Declaración, no verificada de forma independiente |
| Autoridades de Estados Unidos habrían concluido que la otra persona recopilaba información para Pekín | The New York Times, según fuentes | Alegación; la evidencia no es pública |
| El Ministerio de Relaciones Exteriores de China calificó la imputación como infundada | Portavoz del Ministerio | Negación |
| El CEO conocía o participó en actividad de espionaje | Ninguna fuente lo establece | No establecido |
| Influencia para flexibilizar licencias comerciales | Una sola fuente | Dato débil; tratar con cautela |

### Preguntas de análisis

1. **Responsabilidad ejecutiva:** ¿qué debe declarar un CEO a su directorio y
   cuándo? ¿La reserva de la relación fue un problema de conducta privada o de
   declaración tardía de un riesgo del cargo?
2. **Decisiones del directorio:** ¿por qué constituir un comité de directores
   independientes con asesores externos? ¿Qué independencia exige cada rol?
3. **Escenarios alternativos:** mantener con salvaguardas, reasignar, apartar
   temporalmente o separar (clase 202). ¿Qué evidencia reabre cada decisión?
4. **Comunicación y reputación:** ¿qué se sabe, qué no y qué se hace?
5. **Evitar el juicio por intimidad:** el análisis se centra en el riesgo para
   el cargo, la información y la organización, y en el proceso de decisión.

Fuente principal (prensa): La Nación, que recoge cobertura de AP y de The New
York Times (9 de noviembre de 2026). Antes de usar el caso en clase, el docente
debe contrastarlo con fuentes primarias y con su estado a esa fecha.

## 7. Glosario

| Término | Definición |
|---|---|
| **HUMINT** | Información obtenida de y a través de personas. |
| **Contrainteligencia ejecutiva** | Prácticas defensivas que reducen la probabilidad e impacto de la influencia indebida sobre quienes tienen acceso. |
| **Honey trap** | Aproximación que usa intimidad o atracción como instrumento para obtener acceso o ventaja. |
| **Kompromat** | Material comprometedor, real o fabricado, retenido para presionar. |
| **Intermediario** | Tercero que oculta el interés real detrás de una aproximación. |
| **Influencia indebida** | Orientación de una decisión mediante medios que ocultan el interés o explotan una debilidad. |
| **Persuasión** | Influencia con propósito expuesto que deja decidir libremente. |
| **Manipulación** | Influencia que oculta el propósito o explota una debilidad. |
| **Coerción** | Condicionar una decisión con una amenaza. |
| **Conflicto de interés** | Interés personal que puede afectar, o parecer afectar, el juicio en el cargo; real, potencial o percibido. |
| **Persona clave** | Quien concentra acceso, autoridad o conocimiento crítico. |
| **MICE** | Dinero, ideología, compromiso o coerción, ego. |

## 8. Bibliografía de apoyo

Las obras ya registradas en `docs/FUENTES.md` que sustentan este bloque son
Daniel Kahneman, *Thinking, Fast and Slow*; Robert Cialdini, *Influence*;
Amy Edmondson, *The Fearless Organization*, y las lecturas de gobierno y
riesgo de las partes 15 a 17. Para los casos históricos, consulta fuentes
primarias: informes del Congreso de Estados Unidos sobre Enron, el informe
Denning sobre el caso Profumo y las actas de las investigaciones sobre
Hewlett-Packard.

## 9. Resultados de validación

Ejecutados en local el 2026-11-12, todos en verde:

- `validate_repository.py --strict`: 24 partes, 288 clases, 96 laboratorios y
  48 escenarios.
- `validate_depth.py`: 288 clases con estructura, profundidad y originalidad.
- `verify-sources`: citas y registro de fuentes coherentes.
- `build_syllabus`, `build_status`, `build_manifest` y `build_file_index` con
  `--check`: documentos generados al día.
- `check_links.py` y `build_site.py --check`: enlaces resueltos y portal
  generado.
- `pytest`: 42 pruebas aprobadas.

El lint de Markdown y la matriz de sistemas operativos corren en el CI.
