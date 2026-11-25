# Contenido pedagógico de la portada de cada parte. Es dato, no código: lo lee
# `tools/build_navigation.py`, que lo combina con lo que ya declaran las clases
# (títulos, duración, entregables y conceptos) para generar el README de la parte.
#
# Cada entrada:
#   lema        frase corta que resume la parte
#   intro       dos párrafos: por qué importa y cuál es su eje
#   previo      [(parte, qué aporta)] lo que hay que traer
#   aprendizajes  resultados observables de la parte
#   grupos      [(primera_clase, ultima_clase, texto)] cómo se encadenan las clases
#   riesgos     errores característicos de esta materia
#   conecta     cómo se enlaza con las partes siguientes
#   evidencia   lo que queda al terminar

PARTES = {}


def parte(n, **datos):
    PARTES[n] = datos


parte(0,
    lema='Responder por un resultado antes de tener un cargo',
    intro=[
        'Esta parte es la puerta de entrada. El programa entero parte de una idea incómoda: el liderazgo no empieza con el título, empieza cuando alguien responde por un resultado que no era estrictamente suyo. Quien espera el cargo para liderar llega al cargo sin evidencia.',
        'El eje es la **responsabilidad demostrable**: pasar de ejecutar tareas a cuidar resultados, y de pedir confianza a producirla con registros. Termina con un sistema personal de ejecución que sostiene el resto del programa.',
    ],
    previo=[],
    aprendizajes=[
        '**Distinguir** autoridad formal, influencia y responsabilidad, y actuar sobre las dos últimas sin esperar la primera.',
        '**Construir** credibilidad con evidencia verificable en lugar de percepción.',
        '**Gobernar** atención, energía y prioridades con un sistema propio y revisable.',
        '**Reunir** un registro de fortalezas, brechas y reputación que evolucione con el rol.',
    ],
    grupos=[
        (1, 4, 'Las clases **1 a 4** fijan el terreno: qué es liderar sin cargo, qué significa responder por un resultado, cómo se gana credibilidad y dónde están los límites éticos del poder.'),
        (5, 9, 'Las clases **5 a 9** convierten esa postura en método: contribución, prioridades, sistema de ejecución, energía y aprendizaje deliberado.'),
        (10, 12, 'Las clases **10 a 12** consolidan: la reputación como evidencia, el mapa de fortalezas y riesgos propios, y el capstone que integra todo en un sistema operativo de liderazgo.'),
    ],
    riesgos=[
        'Esperar el cargo para asumir responsabilidad.',
        'Confundir visibilidad con credibilidad.',
        'Gestionar el tiempo y no la atención ni la energía.',
        'Tratar la marca personal como relato y no como registro de hechos.',
    ],
    conecta='Alimenta la parte 01, que lleva esa responsabilidad a la calidad de las decisiones, y la parte 02, donde la credibilidad se ejerce al comunicar. Cada artefacto de esta parte se reutiliza en el portafolio final.',
    evidencia=[
        'Un registro de evidencia reputacional con hechos corroborables.',
        'Un sistema personal de ejecución con revisión semanal.',
        'Un mapa de fortalezas, brechas y riesgos propios.',
        'El capstone: tu sistema operativo de liderazgo.',
    ])

parte(1,
    lema='Decidir bien cuando la información es incompleta',
    intro=[
        'Casi todas las decisiones ejecutivas se toman sin los datos que se querrían tener. La diferencia entre un buen y un mal decisor no es la información disponible sino cómo trata lo que no sabe. Esta parte entrena esa disciplina.',
        'El eje es **separar lo que se sabe de lo que se supone** y dejar rastro de la decisión. Se evalúa el proceso, no solo el resultado: una buena decisión puede salir mal y una mala puede salir bien.',
    ],
    previo=[(0, 'Responsabilidad por resultados y un sistema personal de ejecución.')],
    aprendizajes=[
        '**Formular** un problema de modo que pueda decidirse y no solo discutirse.',
        '**Separar** hechos, opiniones, hipótesis y supuestos.',
        '**Reconocer** sesgos propios y ajenos, incluida la influencia indebida.',
        '**Comparar** alternativas con costo de oportunidad, efectos de segundo orden y reversibilidad.',
        '**Registrar** decisiones y aprender de ellas con un After Action Review.',
    ],
    grupos=[
        (13, 16, 'Las clases **13 a 16** ordenan el pensamiento: el problema, la evidencia, el sistema y los sesgos que lo deforman.'),
        (17, 21, 'Las clases **17 a 21** dan las herramientas de la incertidumbre: probabilidad, trade-offs, causa raíz, efectos de segundo orden y escenarios.'),
        (22, 24, 'Las clases **22 a 24** crean el hábito: decision journal, After Action Review y el capstone de un comité de decisión.'),
    ],
    riesgos=[
        'Decidir sobre el problema mal formulado.',
        'Juzgar la decisión por su resultado y no por su proceso.',
        'Aceptar una afirmación por quién la dice y no por su evidencia.',
        'No dejar registro y reescribir la historia después.',
    ],
    conecta='Es la base de toda decisión posterior: la parte 02 la usa para comunicar decisiones, la 08 para medir, la 13 para elegir estrategia y la 17 para gobernar.',
    evidencia=[
        'Un decision journal con al menos cinco decisiones.',
        'Una tabla de hechos, supuestos y datos faltantes.',
        'Un análisis de causa raíz y de segundo orden.',
        'El capstone: decisión de comité bajo incertidumbre.',
    ])

parte(2,
    lema='Hacerse entender, persuadir con ética y sostener la conversación difícil',
    intro=[
        'Un ejecutivo trabaja casi por completo con lenguaje. Una decisión excelente mal comunicada no se ejecuta, y una mala bien comunicada sí. Esta parte trata la comunicación como un **sistema de liderazgo**, no como una habilidad blanda.',
        'El eje es que **los hechos no cambian entre audiencias; cambian el orden, el detalle y el lenguaje**. Incluye escucha, escritura, presentación, feedback, conflicto, mapa de interesados y presencia.',
    ],
    previo=[(0, 'Credibilidad y responsabilidad por lo que se dice.'), (1, 'Decisiones con supuestos explícitos que luego hay que comunicar.')],
    aprendizajes=[
        '**Estructurar** un mensaje para que la audiencia decida.',
        '**Escuchar** y preguntar para obtener información que nadie ofrece.',
        '**Conducir** feedback, conversaciones difíciles y conflicto productivo.',
        '**Mapear** interesados por poder, legitimidad y urgencia.',
        '**Comunicar** una decisión impopular sin perder la confianza.',
    ],
    grupos=[
        (25, 29, 'Las clases **25 a 29** construyen el oficio: sistema de comunicación, escucha, escritura, presentaciones y relato.'),
        (30, 33, 'Las clases **30 a 33** cubren la interacción con personas: feedback, conversación difícil, conflicto y persuasión ética.'),
        (34, 36, 'Las clases **34 a 36** amplían al entorno: interesados y legitimidad, presencia ejecutiva y el capstone de comunicar una decisión impopular.'),
    ],
    riesgos=[
        'Cambiar los hechos según la audiencia.',
        'Confundir persuasión con manipulación.',
        'Evitar la conversación difícil hasta que es una crisis.',
        'Tratar la presencia como imagen y no como claridad y criterio.',
    ],
    conecta='Alimenta la parte 04 (liderar equipos), la 16 (comunicación del CEO) y las crisis de la parte 15. La vocería y la gestión de reputación se profundizan en las clases 190, 200 y 286.',
    evidencia=[
        'Un memo ejecutivo de una página.',
        'Un mapa de interesados con poder, legitimidad y urgencia.',
        'Una conversación difícil preparada y reflexionada.',
        'El capstone: comunicación de una decisión impopular.',
    ])

parte(3,
    lema='Mantener criterio y capacidad de conducción cuando hay presión',
    intro=[
        'Las partes anteriores enseñan qué hacer; esta enseña a poder hacerlo cuando la presión, el cambio o la ambigüedad empujan en contra. Un líder que pierde la regulación pierde primero el juicio y después al equipo.',
        'El eje es la **autorregulación con exigencia**: empatía sin renunciar al estándar, resiliencia sin negar el límite, y valores que se sostienen cuando cuesta. Cierra con una crisis humana donde todo se prueba.',
    ],
    previo=[(0, 'Gobierno de energía y sistema personal.'), (2, 'Comunicación y conversación difícil.')],
    aprendizajes=[
        '**Observar** las propias reacciones bajo presión y regularlas.',
        '**Combinar** empatía y exigencia en una misma conversación.',
        '**Crear** seguridad psicológica sin bajar el estándar.',
        '**Diferenciar** problemas técnicos de adaptativos y actuar en consecuencia.',
        '**Resolver** dilemas éticos con método y conducir una crisis humana.',
    ],
    grupos=[
        (37, 41, 'Las clases **37 a 41** trabajan la persona: autoconciencia, autorregulación, empatía, motivación y resiliencia.'),
        (42, 45, 'Las clases **42 a 45** pasan al entorno: seguridad psicológica, problemas adaptativos, incertidumbre y dilemas éticos.'),
        (46, 48, 'Las clases **46 a 48** cierran con cambio personal, sostenibilidad y el capstone de liderar una crisis humana.'),
    ],
    riesgos=[
        'Confundir empatía con complacencia.',
        'Tratar un problema adaptativo con una solución técnica.',
        'Sostener ritmos que agotan al líder y al equipo.',
        'Decidir un dilema ético por intuición sin método ni registro.',
    ],
    conecta='Prepara las partes de equipos (04) y personas (05), y es la base humana de la gestión de crisis de las partes 15 y 16.',
    evidencia=[
        'Un registro de reacciones bajo presión y su regulación.',
        'Un análisis de un problema adaptativo real.',
        'Una resolución documentada de un dilema ético.',
        'El capstone: conducción de una crisis humana.',
    ])

parte(4,
    lema='Un grupo de personas no es un equipo hasta que comparte objetivos, roles y responsabilidad',
    intro=[
        'La primera responsabilidad de un jefe es que el trabajo de otros sea posible y se haga bien. Esta parte parte de una pregunta práctica: qué debe existir para que un grupo rinda como equipo y no como suma de individuos.',
        'El eje es la **claridad antes del control**: propósito, roles, confianza y delegación por resultados. La accountability se sostiene con acuerdos visibles, no con microgestión.',
    ],
    previo=[(2, 'Comunicación, feedback y conversación difícil.'), (3, 'Regulación y seguridad psicológica.')],
    aprendizajes=[
        '**Definir** un team charter con propósito, objetivos y reglas de trabajo.',
        '**Aclarar** roles, responsabilidades y expectativas sin ambigüedad.',
        '**Delegar** por resultados y mantener accountability sin microgestión.',
        '**Conducir** one-on-ones y reuniones que producen decisiones.',
        '**Recuperar** un equipo disfuncional con un diagnóstico y un plan.',
    ],
    grupos=[
        (49, 52, 'Las clases **49 a 52** construyen el equipo: qué es uno real, su propósito, sus roles y su confianza.'),
        (53, 58, 'Las clases **53 a 58** son el oficio diario: delegación, coaching, one-on-ones, reuniones, motivación y accountability.'),
        (59, 60, 'Las clases **59 y 60** extienden a equipos híbridos y cierran con el capstone de recuperar un equipo disfuncional.'),
    ],
    riesgos=[
        'Delegar tareas en lugar de resultados.',
        'Reemplazar la accountability por vigilancia.',
        'Llenar la agenda de reuniones sin decisiones.',
        'Evitar confrontar el bajo desempeño por proteger el clima.',
    ],
    conecta='La parte 05 profundiza en cómo se contrata, evalúa y desarrolla a las personas del equipo; la 14 lleva el diseño del equipo al de toda la organización.',
    evidencia=[
        'Un team charter acordado con el equipo.',
        'Un plan de delegación por resultados.',
        'Una serie de one-on-ones con registro.',
        'El capstone: plan de recuperación de un equipo.',
    ])

parte(5,
    lema='Contratar, desarrollar y evaluar personas con criterio y justicia',
    intro=[
        'Las decisiones sobre personas son las de mayor consecuencia y las que más se toman por intuición. Esta parte las trata como decisiones con método, evidencia y trazabilidad, porque afectan a quien se contrata y a quien se desvincula.',
        'El eje es **el cargo antes que la persona**: se diseña el rol, se selecciona con estructura, se evalúa con criterios conocidos y se desvincula con documentación. Incluye los límites legales y éticos que un gerente debe conocer.',
    ],
    previo=[(4, 'Equipos, delegación y one-on-ones.'), (1, 'Decisiones con evidencia y registro.')],
    aprendizajes=[
        '**Diseñar** cargos con resultados esperados.',
        '**Seleccionar** con entrevistas estructuradas y criterios previos.',
        '**Gestionar** desempeño con feedback, coaching y planes de mejora.',
        '**Plantear** compensación, aprendizaje y sucesión con coherencia.',
        '**Conducir** una desvinculación responsable y documentada.',
    ],
    grupos=[
        (61, 65, 'Las clases **61 a 65** cubren la entrada: diseño de cargo, dotación, selección, entrevistas y onboarding.'),
        (66, 70, 'Las clases **66 a 70** cubren la permanencia: desempeño, feedback, compensación, aprendizaje y sucesión.'),
        (71, 72, 'Las clases **71 y 72** cubren la salida y el cierre: desvinculación responsable y el capstone de un sistema de talento.'),
    ],
    riesgos=[
        'Contratar por afinidad y no por criterios del cargo.',
        'Evaluar desempeño sin criterios previos ni registro.',
        'Desvincular sin documentación ni proceso.',
        'Aplicar normas laborales sin verificar la fuente vigente.',
    ],
    conecta='Alimenta la parte 14 (diseño organizacional) y 16 (sucesión del CEO). El marco laboral chileno se amplía en la parte 21.',
    evidencia=[
        'Un diseño de cargo con resultados esperados.',
        'Una guía de entrevista estructurada.',
        'Un plan de desempeño y una desvinculación documentada.',
        'El capstone: sistema de talento.',
    ])

parte(6,
    lema='Convertir un objetivo ambiguo en entregables, fechas y responsables',
    intro=[
        'La mayoría de los proyectos fracasa por alcance mal definido y riesgos no declarados, no por falta de esfuerzo. Esta parte da las herramientas para que una iniciativa sea ejecutable y recuperable.',
        'El eje es **alcance, capacidad y riesgo explícitos**. Agile se trata como sistema adaptativo, no como ceremonia, y se enseña cuándo Scrum, Kanban o un plan clásico corresponden.',
    ],
    previo=[(1, 'Decisiones con supuestos y trade-offs.'), (4, 'Equipos y delegación.')],
    aprendizajes=[
        '**Distinguir** proyecto, producto, operación y programa.',
        '**Definir** alcance y éxito antes de planificar.',
        '**Estimar** con capacidad real y gestionar riesgos y dependencias.',
        '**Elegir** Scrum, Kanban o un enfoque clásico con criterio.',
        '**Rescatar** un proyecto atrasado con un plan creíble.',
    ],
    grupos=[
        (73, 77, 'Las clases **73 a 77** construyen la base: tipo de trabajo, alcance, descomposición, estimación y riesgos.'),
        (78, 82, 'Las clases **78 a 82** cubren la ejecución: Agile, Scrum, Kanban, gobernanza y calidad.'),
        (83, 84, 'Las clases **83 y 84** enseñan a recuperar: proyectos atrasados y el capstone de rescate de una iniciativa crítica.'),
    ],
    riesgos=[
        'Planificar antes de definir el éxito.',
        'Estimar sin considerar capacidad ni dependencias.',
        'Adoptar un marco por moda y no por el tipo de trabajo.',
        'Ocultar el atraso hasta que ya no tiene remedio.',
    ],
    conecta='Alimenta la parte 07 (operaciones), la 08 (gestión por indicadores) y la 19 (entrega tecnológica).',
    evidencia=[
        'Una carta de proyecto con alcance y criterios de éxito.',
        'Un registro de riesgos y dependencias.',
        'Un plan de recuperación de un proyecto atrasado.',
        'El capstone: rescate de una iniciativa.',
    ])

parte(7,
    lema='Diseñar una operación repetible, medible y resistente a fallas',
    intro=[
        'Una empresa es un conjunto de procesos que entregan algo a alguien. Cuando dependen de héroes, fallan en cuanto el héroe falta. Esta parte enseña a verlos como sistema.',
        'El eje es **flujo, capacidad y variabilidad**: dónde está el cuello de botella, qué se estandariza, qué nivel de servicio se promete y qué pasa cuando algo se interrumpe.',
    ],
    previo=[(6, 'Planificación, riesgos y entrega.'), (1, 'Pensamiento sistémico y causa raíz.')],
    aprendizajes=[
        '**Mapear** un proceso de extremo a extremo.',
        '**Estandarizar** trabajo con SOP sin rigidizar.',
        '**Hallar** cuellos de botella y reducir desperdicio.',
        '**Definir** SLA y niveles de servicio realistas.',
        '**Planificar** continuidad y gestión de proveedores.',
    ],
    grupos=[
        (85, 88, 'Las clases **85 a 88** describen la operación: sistema, mapa, estándar y capacidad.'),
        (89, 92, 'Las clases **89 a 92** la mejoran: restricciones, Lean, calidad y niveles de servicio.'),
        (93, 96, 'Las clases **93 a 96** la protegen y la rediseñan: terceros, continuidad, automatización y el capstone de rediseño.'),
    ],
    riesgos=[
        'Optimizar un tramo que no es el cuello de botella.',
        'Estandarizar un proceso que no se entiende.',
        'Prometer un nivel de servicio sin capacidad.',
        'Depender de un proveedor sin plan alternativo.',
    ],
    conecta='La parte 08 mide estos procesos; la 15 gobierna su riesgo y continuidad; la 22 los convierte en sistemas que funcionan sin el fundador.',
    evidencia=[
        'Un mapa de proceso con cuellos de botella.',
        'Un SOP y un acuerdo de nivel de servicio.',
        'Un plan de continuidad operacional.',
        'El capstone: rediseño de una operación.',
    ])

parte(8,
    lema='Dirigir con objetivos, métricas y ritmos de revisión',
    intro=[
        'Medir no es dirigir. Muchos tableros muestran actividad y ocultan si el negocio avanza. Esta parte enseña a elegir qué medir, con qué cadencia revisarlo y qué decisión se espera de cada número.',
        'El eje es **de actividad a resultado**: objetivos bien formulados, indicadores adelantados y rezagados, y reuniones de revisión que deciden en lugar de informar.',
    ],
    previo=[(1, 'Decisiones con evidencia.'), (7, 'Procesos que se pueden medir.')],
    aprendizajes=[
        '**Diferenciar** actividad, producto y resultado.',
        '**Diseñar** objetivos y decidir cuándo conviene OKR.',
        '**Elegir** KPI con indicadores adelantados y rezagados.',
        '**Establecer** un ritmo semanal, mensual y trimestral.',
        '**Conducir** business reviews y gestionar por excepción.',
    ],
    grupos=[
        (97, 99, 'Las clases **97 a 99** fijan qué se persigue: resultado, objetivos y OKR con sus límites.'),
        (100, 102, 'Las clases **100 a 102** definen cómo se mide: KPI, indicadores y tableros.'),
        (103, 108, 'Las clases **103 a 108** cubren cómo se gobierna: ritmo, business reviews, priorización, recursos, escalamiento y el capstone de operating review.'),
    ],
    riesgos=[
        'Medir lo fácil y no lo importante.',
        'Aplicar OKR como ritual sin estrategia.',
        'Revisar números sin decidir nada.',
        'Premiar una métrica que se manipula.',
    ],
    conecta='Alimenta la parte 09 (finanzas), la 13 (estrategia) y los tableros del CEO en la parte 16 y del dueño en la 22.',
    evidencia=[
        'Un árbol de KPI conectado con el objetivo.',
        'Un tablero con 5 a 7 indicadores.',
        'Un calendario de revisiones con agenda y decisiones.',
        'El capstone: operating review gerencial.',
    ])

parte(9,
    lema='Leer la economía real del negocio y decidir con números',
    intro=[
        'Un gerente que no lee estados financieros delega el control a quien sí. Esta parte da el lenguaje mínimo para interpretar resultados, balance y caja, y para decidir inversiones con retorno y escenarios.',
        'El eje es que **utilidad no es caja**: se distingue lo que se gana de lo que se cobra, y se aprende a ver el negocio por sus márgenes, su capital de trabajo y su economía unitaria.',
    ],
    previo=[(8, 'Indicadores y revisión.'), (1, 'Probabilidad, trade-offs y escenarios.')],
    aprendizajes=[
        '**Leer** estado de resultados, balance y flujo de caja.',
        '**Calcular** márgenes, punto de equilibrio y capital de trabajo.',
        '**Construir** presupuesto y forecast con supuestos explícitos.',
        '**Evaluar** unit economics: CAC, LTV, churn y payback.',
        '**Decidir** inversiones con ROI, ROIC y fundamentos de valoración.',
    ],
    grupos=[
        (109, 112, 'Las clases **109 a 112** enseñan a leer: lenguaje financiero, resultados, balance y caja.'),
        (113, 117, 'Las clases **113 a 117** enseñan a gestionar: márgenes, capital de trabajo, presupuesto, break-even y economía unitaria.'),
        (118, 120, 'Las clases **118 a 120** enseñan a decidir: retorno, valoración y el capstone de comité de inversión.'),
    ],
    riesgos=[
        'Confundir utilidad con caja.',
        'Proyectar con supuestos que nadie declara.',
        'Evaluar una inversión sin escenario adverso.',
        'Usar un indicador sin conocer su definición.',
    ],
    conecta='Alimenta la parte 10 y 11 (economía comercial), la 18 (finanzas corporativas) y el runway de las partes 20 y 23.',
    evidencia=[
        'Un modelo financiero simple con supuestos.',
        'Un análisis de unit economics.',
        'Un memo de decisión de inversión.',
        'El capstone: comité de inversión.',
    ])

parte(10,
    lema='Un sistema comercial repetible, no una racha de ventas',
    intro=[
        'Vender bien no es talento sino proceso: a quién, con qué promesa, por qué canal y con qué economía. Esta parte trata las ventas como un sistema medible y la negociación como diseño de acuerdos.',
        'El eje es **intereses antes que posiciones**: descubrir el problema real del cliente, construir un caso de negocio, manejar objeciones sin presionar y conceder solo con contrapartida.',
    ],
    previo=[(9, 'Márgenes y economía unitaria.'), (2, 'Escucha, persuasión ética y conversación difícil.')],
    aprendizajes=[
        '**Definir** el cliente ideal y generar oportunidades.',
        '**Diagnosticar** con discovery y construir un business case.',
        '**Gestionar** pipeline y forecast con honestidad.',
        '**Negociar** por intereses y fijar precio y concesiones.',
        '**Expandir** y retener cuentas.',
    ],
    grupos=[
        (121, 124, 'Las clases **121 a 124** abren el sistema: ventas como proceso, cliente ideal, prospección y discovery.'),
        (125, 130, 'Las clases **125 a 130** cubren la conversación comercial: valor, pipeline, objeciones, negociación, precio y cierre.'),
        (131, 132, 'Las clases **131 y 132** cubren la relación posterior y cierran con el capstone de negociación enterprise.'),
    ],
    riesgos=[
        'Hacer forecast con optimismo y sin evidencia.',
        'Conceder precio sin pedir nada a cambio.',
        'Vender a clientes que no encajan con la oferta.',
        'Descuidar la retención por perseguir nuevas cuentas.',
    ],
    conecta='Se complementa con la parte 11 (marketing) y alimenta la parte 20 (primeros clientes) y la 23 (sistema semanal de ventas).',
    evidencia=[
        'Un perfil de cliente ideal con criterios de exclusión.',
        'Un pipeline con etapas y criterios de salida.',
        'Un plan de negociación con intereses y concesiones.',
        'El capstone: negociación enterprise.',
    ])

parte(11,
    lema='Elegir a quién servir y hacer que la oferta se reconozca y se confíe',
    intro=[
        'El marketing responde cuatro preguntas: quién es el cliente, qué problema resuelve la oferta, por qué canal llega y por qué debería creer. Esta parte trabaja las cuatro con evidencia y no con eslóganes.',
        'El eje es **evidencia de demanda antes de gasto**. Marca y confianza se tratan como señales verificables, no como imagen. Es una introducción para quien dirige; el detalle disciplinar vive en el programa de marketing, al que se remite.',
    ],
    previo=[(10, 'Cliente ideal, valor y economía comercial.'), (9, 'Unit economics.')],
    aprendizajes=[
        '**Dimensionar** mercado y demanda con evidencia.',
        '**Segmentar** y posicionar una oferta.',
        '**Sostener** la marca con señales de confianza verificables.',
        '**Mapear** el recorrido del cliente, los canales y el funnel.',
        '**Diseñar** retención y experimentos de crecimiento.',
    ],
    grupos=[
        (133, 137, 'Las clases **133 a 137** definen a quién y con qué promesa: mercado, investigación, segmentación, posicionamiento y confianza.'),
        (138, 141, 'Las clases **138 a 141** definen cómo llega: recorrido del cliente, canales, adquisición y conversión.'),
        (142, 144, 'Las clases **142 a 144** definen cómo se mantiene y crece: retención, loops de crecimiento y el capstone de go-to-market.'),
    ],
    riesgos=[
        'Segmentar por conveniencia interna y no por comportamiento.',
        'Confundir marca con logotipo.',
        'Comprar tráfico antes de entender la conversión.',
        'Medir adquisición e ignorar la retención.',
    ],
    conecta='Enlaza con producto (parte 12) y con la validación del fundador (parte 20). La reparación de confianza se trabaja con la clase 286.',
    evidencia=[
        'Un análisis de mercado con fuentes.',
        'Una declaración de posicionamiento sustentada.',
        'Un funnel con tasas y supuestos.',
        'El capstone: plan de go-to-market.',
    ])

parte(12,
    lema='Decidir qué construir, para quién y por qué antes de gastar',
    intro=[
        'Construir lo que nadie necesita es el desperdicio más caro de una empresa. Esta parte da el método para descubrir problemas reales, probar hipótesis con poco costo y decidir con evidencia.',
        'El eje es **aprendizaje validado**: el MVP es una prueba de hipótesis, el roadmap se ordena por resultados y la señal de ajuste se verifica con conducta, no con opiniones.',
    ],
    previo=[(11, 'Segmentación y recorrido del cliente.'), (1, 'Hipótesis, experimentos y causa raíz.')],
    aprendizajes=[
        '**Distinguir** producto de proyecto y el problema de la solución.',
        '**Descubrir** necesidades con entrevistas y Jobs to Be Done.',
        '**Probar** con prototipos y MVP como hipótesis.',
        '**Ordenar** un roadmap por resultados y costo de oportunidad.',
        '**Interpretar** métricas de producto y señales de product-market fit.',
    ],
    grupos=[
        (145, 148, 'Las clases **145 a 148** definen el problema: producto, usuario, discovery y Jobs to Be Done.'),
        (149, 153, 'Las clases **149 a 153** lo prueban: prototipos, MVP, roadmap, priorización y experimentos.'),
        (154, 156, 'Las clases **154 a 156** lo evalúan: métricas, product-market fit y el capstone de comité de producto.'),
    ],
    riesgos=[
        'Construir sin haber validado el problema.',
        'Tratar el MVP como versión pequeña y no como prueba.',
        'Priorizar por quien insiste más.',
        'Declarar ajuste con producto sin retención.',
    ],
    conecta='Alimenta la parte 13 (estrategia), la 19 (tecnología) y la validación del fundador de la parte 20.',
    evidencia=[
        'Un resumen de discovery con entrevistas reales o simuladas.',
        'Un MVP definido como hipótesis con criterio de éxito.',
        'Un roadmap por resultados.',
        'El capstone: comité de producto.',
    ])

parte(13,
    lema='Hacer elecciones coherentes sobre dónde competir, cómo ganar y qué no hacer',
    intro=[
        'Estrategia no es un plan ni un deseo: es un conjunto de elecciones que renuncian a algo. Esta parte enseña a diagnosticar, elegir y hacer coherentes las decisiones con esa elección.',
        'El eje es **trade-off explícito**. Una estrategia que no deja nada fuera no es estrategia. Se estudian industria, capacidades, ventaja, modelo de negocio, escenarios y crecimiento.',
    ],
    previo=[(9, 'Economía del negocio.'), (11, 'Mercado y posicionamiento.'), (12, 'Producto y evidencia.')],
    aprendizajes=[
        '**Diferenciar** estrategia de plan y de aspiración.',
        '**Diagnosticar** industria, competidores y capacidades.',
        '**Sustentar** una ventaja y los trade-offs que exige.',
        '**Comparar** modelos de negocio y opciones de crecimiento.',
        '**Redactar** un strategy memo que pueda ser refutado.',
    ],
    grupos=[
        (157, 160, 'Las clases **157 a 160** diagnostican: qué es estrategia, el diagnóstico, la industria y las capacidades.'),
        (161, 165, 'Las clases **161 a 165** eligen: ventaja, trade-offs, modelo de negocio, escenarios y crecimiento.'),
        (166, 168, 'Las clases **166 a 168** ejecutan y cierran: alianzas, adaptación y el capstone de strategy memo.'),
    ],
    riesgos=[
        'Llamar estrategia a una lista de iniciativas.',
        'No renunciar a nada.',
        'Copiar la ventaja de otro sin sus capacidades.',
        'No definir qué señal obligaría a cambiar de rumbo.',
    ],
    conecta='Alimenta la parte 14 (organización), la 17 (supervisión de estrategia en el directorio) y la 18 (capital y M&A).',
    evidencia=[
        'Un diagnóstico estratégico con evidencia.',
        'Una matriz de trade-offs explícitos.',
        'Escenarios con señales de cambio.',
        'El capstone: strategy memo.',
    ])

parte(14,
    lema='Una estructura, una cultura y un incentivo coherentes con la estrategia',
    intro=[
        'Las organizaciones no fallan por falta de estrategia sino porque su diseño empuja en otra dirección. Esta parte enseña a ver estructura, derechos de decisión, incentivos y cultura como un sistema diseñable.',
        'El eje es **derechos de decisión claros**: quién decide qué, con qué información y con qué incentivo. Cierra con cambio y transformación, y con los riesgos humanos de reorganizar.',
    ],
    previo=[(13, 'Estrategia a la que el diseño debe servir.'), (5, 'Cargos, dotación y desempeño.')],
    aprendizajes=[
        '**Evaluar** una estructura funcional, divisional o matricial.',
        '**Dimensionar** spans, layers y carga gerencial.',
        '**Asignar** derechos de decisión con RACI o RAPID.',
        '**Leer** la cultura por artefactos e incentivos.',
        '**Conducir** un cambio con diagnóstico, coalición y adopción.',
    ],
    grupos=[
        (169, 173, 'Las clases **169 a 173** diseñan: organización, estructuras, spans, operating model y derechos de decisión.'),
        (174, 175, 'Las clases **174 y 175** leen lo que no está en el organigrama: cultura e incentivos.'),
        (176, 180, 'Las clases **176 a 180** conducen el cambio: diagnóstico, coalición, transformación, reorganización y el capstone de rediseño.'),
    ],
    riesgos=[
        'Reorganizar sin aclarar quién decide.',
        'Declarar valores que los incentivos contradicen.',
        'Lanzar un cambio sin diagnóstico ni coalición.',
        'Subestimar el costo humano de una reorganización.',
    ],
    conecta='Alimenta la parte 16 (equipo ejecutivo) y la 22 (empresa menos dependiente del fundador).',
    evidencia=[
        'Un diseño organizacional con spans y capas.',
        'Una matriz de derechos de decisión.',
        'Un diagnóstico y plan de cambio.',
        'El capstone: rediseño organizacional.',
    ])

parte(15,
    lema='Supervisar riesgos que exigen especialistas sin delegar la responsabilidad',
    intro=[
        'Un ejecutivo no necesita ser abogado, ingeniero de seguridad ni auditor, pero responde por lo que ocurre. Esta parte enseña a hacer las preguntas correctas, entender las respuestas y decidir con riesgos que otros miden.',
        'El eje es **responsabilidad indelegable**. Cubre riesgo empresarial, controles, marco legal, contratos, datos, ciberseguridad, IA, ética, crisis y continuidad, e incorpora la gestión de crisis con comité y vocería.',
    ],
    previo=[(1, 'Decisión bajo incertidumbre.'), (7, 'Procesos y continuidad.'), (3, 'Dilemas éticos.')],
    aprendizajes=[
        '**Fijar** apetito y límites de riesgo.',
        '**Revisar** controles y segregación de funciones.',
        '**Detectar** riesgos legales y contractuales antes de firmar.',
        '**Supervisar** privacidad, ciberseguridad e IA sin sustituir al especialista.',
        '**Constituir** un comité de crisis con autoridad, escalamiento y vocería.',
    ],
    grupos=[
        (181, 183, 'Las clases **181 a 183** fijan el marco: gestión de riesgo, apetito y controles.'),
        (184, 188, 'Las clases **184 a 188** cubren los dominios: legal, contratos, datos, ciberseguridad y IA.'),
        (189, 192, 'Las clases **189 a 192** cubren la cultura y la respuesta: ética, crisis y escalamiento, continuidad y el capstone de comité de riesgos.'),
    ],
    riesgos=[
        'Delegar el riesgo y creer que se delegó la responsabilidad.',
        'Confiar en un control sin probarlo.',
        'Firmar un contrato sin entender qué riesgo transfiere.',
        'Improvisar la autoridad durante la crisis.',
    ],
    conecta='La parte 16 lleva la crisis al nivel del CEO, la 17 la supervisa desde el directorio y la 23 cierra con ética y reputación. El impacto reputacional se detalla en [docs/REPUTATION_AND_CRISIS_LEADERSHIP.md](../../docs/REPUTATION_AND_CRISIS_LEADERSHIP.md).',
    evidencia=[
        'Un registro de riesgos con apetito y controles.',
        'Una revisión de contrato con riesgos detectados.',
        'Un acta de comité de crisis con matriz de responsabilidades.',
        'El capstone: comité integrado de riesgos.',
    ])

parte(16,
    lema='Dirigir la empresa completa, no una función',
    intro=[
        'El paso de gerente a ejecutivo no es de más trabajo sino de otro trabajo: integrar estrategia, personas, capital y stakeholders, y decidir qué no hacer. Esta parte entrena esa perspectiva de empresa.',
        'El eje es **asignar y responder**: el CEO asigna atención, capital y talento, comunica ante todas las audiencias y responde por decisiones difíciles de revertir. Incluye crisis, comunicación y sucesión.',
    ],
    previo=[(13, 'Estrategia.'), (14, 'Diseño organizacional.'), (15, 'Riesgo y crisis.'), (8, 'Gestión por indicadores.')],
    aprendizajes=[
        '**Transitar** de gerente a ejecutivo y pensar a nivel empresa.',
        '**Construir** el equipo ejecutivo y su arquitectura de decisiones.',
        '**Asignar** atención, capital y talento con criterio.',
        '**Comunicar** como CEO ante empleados, directorio, clientes y mercado.',
        '**Decidir** en crisis y planificar la sucesión.',
    ],
    grupos=[
        (193, 197, 'Las clases **193 a 197** definen el rol: transición, visión de empresa, equipo, decisiones y agenda.'),
        (198, 201, 'Las clases **198 a 201** cubren el ejercicio: capital y talento, balance entre grupos de interés, comunicación y pipeline de liderazgo.'),
        (202, 204, 'Las clases **202 a 204** cubren la prueba: crisis y decisiones irreversibles, sucesión y el capstone de primeros 100 días.'),
    ],
    riesgos=[
        'Seguir resolviendo problemas de la función de origen.',
        'Decidir lo que otro debía decidir.',
        'Decir al mercado algo que los hechos internos contradicen.',
        'No preparar la sucesión hasta que es urgente.',
    ],
    conecta='La parte 17 sitúa al CEO frente al directorio y la 22 lleva estas capacidades al dueño de empresa. La vocería ejecutiva se entrena con las plantillas del programa.',
    evidencia=[
        'Un calendario del CEO auditado.',
        'Un acta de equipo ejecutivo y su arquitectura de decisiones.',
        'Un manual de vocería ejecutiva.',
        'El capstone: plan de primeros 100 días.',
    ])

parte(17,
    lema='Entender quién manda, quién controla y quién rinde cuentas',
    intro=[
        'El directorio es la institución que separa la propiedad de la administración. Quien llega a CEO o funda una empresa con socios debe entender su funcionamiento, sus deberes y los conflictos que gestiona.',
        'El eje es **supervisar sin administrar**: el directorio hace preguntas, controla y evalúa; no dirige. Cubre comités, deberes, independencia, información, evaluación del CEO y efectividad del propio directorio.',
    ],
    previo=[(16, 'El rol del CEO.'), (15, 'Riesgo y controles.')],
    aprendizajes=[
        '**Distinguir** propiedad, directorio y administración.',
        '**Precisar** el rol del presidente y del CEO.',
        '**Explicar** la función de los comités de auditoría, riesgo y compensación.',
        '**Gestionar** deberes, conflictos de interés e independencia.',
        '**Preparar** un board pack que permita decidir.',
    ],
    grupos=[
        (205, 208, 'Las clases **205 a 208** definen la institución: propiedad y gobierno, qué hace un directorio, presidente y CEO, y comités.'),
        (209, 211, 'Las clases **209 a 211** definen la conducta: deberes y conflictos, información y board pack.'),
        (212, 216, 'Las clases **212 a 216** definen la supervisión: estrategia, riesgo, evaluación del CEO, efectividad y el capstone de reunión de directorio.'),
    ],
    riesgos=[
        'Confundir supervisar con administrar.',
        'Aprobar sin información suficiente.',
        'Tolerar un conflicto de interés por costumbre.',
        'Evaluar al CEO solo por resultados de corto plazo.',
    ],
    conecta='Alimenta la parte 18 (decisiones de capital) y la 22 (gobierno proporcional al tamaño). Las simulaciones de directorio de la clase 202 usan este marco.',
    evidencia=[
        'Un board pack con decisión solicitada.',
        'Una declaración de conflictos.',
        'Una evaluación del CEO con criterios previos.',
        'El capstone: reunión de directorio simulada.',
    ])

parte(18,
    lema='Financiar, valorar y adquirir con criterio de propietario',
    intro=[
        'Las decisiones de capital son las más difíciles de revertir y las que más afectan al patrimonio de los dueños. Esta parte da el marco para financiar, valorar, levantar capital y comprar o integrar empresas.',
        'El eje es **retorno ajustado por riesgo y control**: cuánto cuesta el capital, qué se cede al financiarse y qué se promete al comprar.',
    ],
    previo=[(9, 'Lectura financiera y retorno.'), (17, 'Gobierno y deberes.')],
    aprendizajes=[
        '**Decidir** estructura de capital y comparar deuda con capital propio.',
        '**Estimar** el costo de capital.',
        '**Valorar** por flujos y por múltiplos, y señalar sus límites.',
        '**Leer** un cap table y un term sheet en economía y control.',
        '**Evaluar** una adquisición y su integración.',
    ],
    grupos=[
        (217, 221, 'Las clases **217 a 221** cubren el valor: estructura y costo de capital, deuda frente a capital, valoración por flujos y por múltiplos.'),
        (222, 224, 'Las clases **222 a 224** cubren el levantamiento: relato financiero, cap table y term sheets.'),
        (225, 228, 'Las clases **225 a 228** cubren las adquisiciones: lógica estratégica, due diligence, integración y el capstone de comité de capital.'),
    ],
    riesgos=[
        'Valorar con un único método y sin escenarios.',
        'Ceder control sin haberlo valorado.',
        'Comprar por tamaño y no por lógica estratégica.',
        'Subestimar la integración.',
    ],
    conecta='Alimenta la parte 20 (equity entre cofundadores), la 22 (adquisiciones y holdings) y la 23 (runway y concentración de riesgo).',
    evidencia=[
        'Una valoración con rangos y supuestos.',
        'Un análisis de cap table y dilución.',
        'Una tesis de adquisición con riesgos de due diligence.',
        'El capstone: comité de capital.',
    ])

parte(19,
    lema='Dirigir la inversión tecnológica por valor, riesgo y capacidad',
    intro=[
        'La tecnología ya no es una función de apoyo: es parte del modelo de negocio. Un ejecutivo debe decidir sin ser técnico, entendiendo qué preguntar y qué riesgos aceptar.',
        'El eje es **valor antes que moda**: cada inversión en nube, datos o IA se justifica por un caso de negocio, un riesgo gobernado y una capacidad organizacional que la sostiene.',
    ],
    previo=[(13, 'Estrategia.'), (15, 'Gobierno de datos, ciberseguridad e IA.'), (9, 'Casos de negocio.')],
    aprendizajes=[
        '**Entender** la tecnología como capacidad empresarial.',
        '**Evaluar** economía de nube y plataformas.',
        '**Tratar** los datos como activo con dueño y calidad.',
        '**Decidir** build, buy, partner o retire.',
        '**Gobernar** un portafolio de IA, con supervisión humana y responsable.',
    ],
    grupos=[
        (229, 232, 'Las clases **229 a 232** definen la estrategia: tecnología, estrategia digital, nube y datos.'),
        (233, 236, 'Las clases **233 a 236** cubren la decisión: IA, automatización, ciberseguridad y build o buy.'),
        (237, 240, 'Las clases **237 a 240** cubren la gestión: deuda técnica, métricas de entrega, cambio laboral por IA y el capstone de transformation board.'),
    ],
    riesgos=[
        'Invertir en IA sin un caso de negocio.',
        'Ignorar la deuda técnica hasta que paraliza.',
        'Delegar en el sistema una decisión que exige responsable humano.',
        'Subestimar el efecto en el trabajo y las personas.',
    ],
    conecta='Se conecta con la parte 15 (gobierno de IA) y con la clase 202, donde el error de un agente de IA exige responsabilidad humana. Alimenta la parte 22.',
    evidencia=[
        'Un caso de negocio de IA con riesgos.',
        'Una decisión build, buy, partner o retire.',
        'Un plan de cambio laboral.',
        'El capstone: transformation board.',
    ])

parte(20,
    lema='De un problema real a una oferta con disposición a pagar demostrada',
    intro=[
        'Fundar es decidir con riesgo propio. La mayoría de las empresas nuevas fracasa por construir antes de validar. Esta parte reemplaza la idea brillante por una oferta probada con clientes que pagan.',
        'El eje es **evidencia de pago**: hipótesis, discovery, validación, MVP, pricing y primeros diez clientes. Incluye el acuerdo entre cofundadores, que pocos tratan a tiempo.',
    ],
    previo=[(10, 'Venta y negociación.'), (11, 'Mercado y cliente.'), (12, 'Discovery y MVP.'), (9, 'Economía unitaria.')],
    aprendizajes=[
        '**Elegir** entre fundar, ser independiente o emprender.',
        '**Encontrar** problemas valiosos y formular hipótesis de cliente.',
        '**Validar** antes de construir y probar un MVP.',
        '**Fijar** precio temprano y conseguir los primeros clientes.',
        '**Acordar** equity y reglas entre cofundadores.',
    ],
    grupos=[
        (241, 244, 'Las clases **241 a 244** definen la oportunidad: el rol, los problemas, el discovery y las hipótesis.'),
        (245, 249, 'Las clases **245 a 249** la prueban: propuesta de valor, modelo, validación, MVP y precio.'),
        (250, 252, 'Las clases **250 a 252** la lanzan: primeros clientes, cofundadores y el capstone de launch readiness.'),
    ],
    riesgos=[
        'Construir antes de validar.',
        'Tomar el elogio por intención de compra.',
        'Fijar precio por costo y no por valor.',
        'Postergar el acuerdo entre cofundadores.',
    ],
    conecta='La parte 21 formaliza la empresa en Chile y la 22 la escala. Para el ciclo completo de creación de empresa existe un programa hermano, referenciado en los documentos.',
    evidencia=[
        'Una validación con evidencia de pago.',
        'Un MVP con criterios de éxito.',
        'Un acuerdo de cofundadores.',
        'El capstone: launch readiness.',
    ])

parte(21,
    lema='Formalizar y operar una empresa en Chile sabiendo cuándo pedir apoyo',
    intro=[
        'Operar una empresa implica obligaciones tributarias, laborales, contables y sectoriales. Esta parte da el mapa para entender qué se debe, a quién y cuándo, y reconocer cuándo corresponde un especialista.',
        'El eje es **qué decisión dispara qué obligación**. Todo el material normativo se presenta con su fecha de verificación y debe revalidarse en la fuente oficial. No es asesoría legal ni tributaria.',
    ],
    previo=[(20, 'Una oferta validada que formalizar.'), (15, 'Alfabetización legal y contratos.')],
    aprendizajes=[
        '**Ubicar** el ciclo empresarial en Chile y sus hitos.',
        '**Comparar** persona natural y jurídica y los tipos societarios.',
        '**Entender** inicio de actividades, documentos tributarios y registros.',
        '**Ordenar** contabilidad, tesorería, pagos y control documental.',
        '**Reconocer** obligaciones laborales, de propiedad intelectual y permisos.',
    ],
    grupos=[
        (253, 256, 'Las clases **253 a 256** cubren la constitución: ciclo, forma jurídica, tipos societarios e inicio de actividades.'),
        (257, 260, 'Las clases **257 a 260** cubren la operación: documentos tributarios, contabilidad, pagos y obligaciones laborales.'),
        (261, 264, 'Las clases **261 a 264** cubren la protección y el ecosistema: propiedad intelectual, permisos, apoyo público y el capstone de cumplimiento.'),
    ],
    riesgos=[
        'Decidir la forma jurídica sin considerar tributación y responsabilidad.',
        'Operar sin control documental.',
        'Contratar sin conocer las obligaciones laborales.',
        'Usar una norma sin revisar si sigue vigente.',
    ],
    conecta='Alimenta la parte 22 (controles para crecer). Para el detalle de constitución y operación en Chile existe el programa hermano de creación de empresas.',
    evidencia=[
        'Un mapa de obligaciones con su fuente oficial y fecha.',
        'Un calendario de cumplimiento.',
        'Una lista de verificación de operación.',
        'El capstone: empresa operable.',
    ])

parte(22,
    lema='Pasar de operar el negocio a ser dueño de un sistema',
    intro=[
        'El fundador que lo hace todo crea un empleo, no una empresa. Esta parte enseña a construir sistemas, equipos de liderazgo y controles que permiten crecer sin que el negocio dependa de una persona.',
        'El eje es **menor dependencia con más control**: delegar decisiones sin perder visibilidad, escalar ventas sin destruir margen y gobernar en proporción al tamaño.',
    ],
    previo=[(21, 'Empresa formalizada y operable.'), (14, 'Diseño organizacional.'), (17, 'Gobierno.')],
    aprendizajes=[
        '**Transitar** de fundador-operador a propietario.',
        '**Construir** sistemas antes que heroicidad.',
        '**Contratar** líderes y delegar decisiones con control.',
        '**Escalar** ventas cuidando el margen.',
        '**Gobernar** un portafolio o una estructura de propiedad.',
    ],
    grupos=[
        (265, 269, 'Las clases **265 a 269** cambian el rol: de operador a propietario, sistemas, líderes, ventas y controles.'),
        (270, 273, 'Las clases **270 a 273** amplían la estructura: gobierno proporcional, multiunidad, holdings y adquisiciones.'),
        (274, 276, 'Las clases **274 a 276** cierran el traspaso: delegación, tablero del dueño y el capstone de una empresa menos dependiente del fundador.'),
    ],
    riesgos=[
        'Contratar un líder y seguir decidiendo por él.',
        'Crecer en ventas deteriorando el margen.',
        'Gobernar de forma informal cuando ya hay terceros afectados.',
        'Estructurar la propiedad sin entender sus consecuencias.',
    ],
    conecta='Prepara la parte 23, donde se integra todo en un plan de independencia y en el capstone final.',
    evidencia=[
        'Un mapa de dependencias del fundador.',
        'Un tablero del dueño.',
        'Un plan de delegación con control.',
        'El capstone: empresa menos dependiente.',
    ])

parte(23,
    lema='Integrar todo en una estrategia de independencia y defenderla como CEO, founder y owner',
    intro=[
        'La parte final cierra el programa. Se construye una estrategia de independencia con ingresos diversificados, disciplina comercial, protección de caja y una defensa ante pares.',
        'El eje es **independencia sostenible**: no depender de un único cliente, canal o persona, y sostener la integridad cuando la decisión sale cara. Incluye riesgo, ética y reputación.',
    ],
    previo=[(22, 'Empresa que funciona con menos dependencia.'), (20, 'Validación.'), (16, 'Perspectiva de CEO.')],
    aprendizajes=[
        '**Definir** independencia en términos económicos y profesionales.',
        '**Inventariar** capacidades monetizables y elegir un modelo de ingresos.',
        '**Diversificar** el portafolio y proteger la caja.',
        '**Sostener** un sistema semanal de ventas.',
        '**Defender** la integridad y la reputación bajo presión.',
    ],
    grupos=[
        (277, 281, 'Las clases **277 a 281** definen la base: independencia, capacidades, consultoría, servicios productizados y producto digital.'),
        (282, 285, 'Las clases **282 a 285** gestionan el sistema: modelos recurrentes, portafolio de ingresos, runway y ventas semanales.'),
        (286, 288, 'Las clases **286 a 288** cierran: riesgo, ética y reputación, plan de 90 días y anual, y la defensa final.'),
    ],
    riesgos=[
        'Depender de un único cliente o canal.',
        'Confundir ingresos con caja protegida.',
        'Decidir bajo presión sin registro ni límites.',
        'Proteger la imagen antes que reparar el hecho.',
    ],
    conecta='Es el cierre del programa. Sus artefactos forman el portafolio ejecutivo que puede usarse en entrevistas, promociones o consultoría.',
    evidencia=[
        'Un plan de independencia.',
        'Una simulación integrada de riesgo y reputación.',
        'Un plan de 90 días y anual.',
        'La defensa final como CEO, founder y owner.',
    ])
