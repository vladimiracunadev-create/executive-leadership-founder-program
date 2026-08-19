# 📗 Fuentes

**Todas las obras, normas y portales oficiales en los que se apoya el programa, uno
por uno y con el enlace para ir a comprobarlos.**

[⬅️ Documentación](README.md) ·
[🏠 Inicio](../README.md) ·
[📚 Catálogo orientativo](BOOKS.md) ·
[🗺️ Mapa de fuentes por parte](REFERENCE_MAP.md) ·
[🔗 Fuentes oficiales](OFFICIAL_SOURCES.md)

---

Esta página existe para responder a una pregunta concreta: **¿de dónde sale lo que
dice cada clase?** No es un resumen ni una recomendación de lectura: es el
inventario completo de lo que el material cita, con el localizador de cada obra.

La fuente de verdad no es esta página, sino
**[`sources/bibliography.json`](../sources/bibliography.json)**, donde cada obra
tiene emisor, localizador y fecha de comprobación. Esta página se **genera** desde
ese registro: si alguien añadiera aquí una obra a mano,
`python scripts/verify-sources` haría fallar la integración continua.

> **Criterio de aceptación.** Una obra entra en el registro con un localizador
> resoluble: **ISBN-13** para un libro, **DOI** para un artículo, o la **URL
> oficial** de la fuente primaria para una norma. Lo que no se pudo resolver queda
> como **pendiente**, con el motivo escrito. Un hueco declarado es información; un
> hueco rellenado por intuición sería una invención con formato de bibliografía.

---

## 🔍 Cómo leer una cita del programa

Cada clase cierra con una sección `📗 Fuentes y verificación` donde cada línea tiene
esta forma:

```text
- Peter F. Drucker — *The Effective Executive* (Collins, 2002).
  **Uso en esta clase:** efectividad ejecutiva, contribución, prioridades y uso
  consciente del tiempo. Lectura selectiva sobre **qué significa liderar sin cargo
  formal**. **Localizador:** [ISBN-13 9780060516079](https://openlibrary.org/isbn/9780060516079).
```

| Elemento | Para qué sirve |
|---|---|
| Autor y obra | Identificar de quién es la tesis que sostiene el bloque |
| Editorial y año, entre paréntesis | Pedir **el ejemplar exacto**: las ediciones difieren |
| **Uso en esta clase** | Saber qué sostiene esa obra **aquí**, y no solo que se citó |
| Lectura selectiva | Qué buscar dentro del libro, en vez de leerlo entero |
| **Localizador** | Ir a comprobarlo: ISBN-13, DOI o la URL del organismo |

La tercera fila es la que distingue una bibliografía de un adorno. Citar una obra sin
decir qué se toma de ella deja al lector sin forma de comprobar la afirmación: tendría
que leerse el libro entero para averiguar si dice lo que la clase supone. Por eso el
verificador exige esa frase en **todas** las citas del programa, sin excepción.

Editorial y año no se escriben a mano: salen de la ficha de la edición que resolvió el
ISBN. Y como la línea de la clase se deriva del registro, **no puede desviarse de él**
sin que el CI lo diga.

---

<!-- registro-de-fuentes:inicio -->
## 🧾 El registro en cifras

El programa cita **3200** veces un total de
**207** obras a lo largo de sus **288** clases.
De esas obras, **201** tienen hoy un localizador comprobado
—ISBN-13, DOI o URL oficial con fecha de acceso— y **6**
siguen pendientes de resolver.

| Tipo | Obras | Localizador que exige |
|---|---:|---|
| Libro | 164 | ISBN-13 con dígito de control válido |
| Artículo | 2 | DOI |
| Referencia | 1 | URL https de la fuente primaria, con fecha de acceso |
| Norma o documento oficial | 40 | URL https de la fuente primaria, con fecha de acceso |

El ISBN-13 se resuelve contra Open Library comparando título y autores, y de ahí
salen también la editorial y el año que ves abajo: no se escriben de memoria.
Cuando ni el título ni los autores coinciden con seguridad, la entrada se queda
pendiente antes que arriesgar un ISBN casi correcto, que es peor que ninguno
porque aparenta una comprobación que nadie hizo.

## 📖 Bibliografía de gestión

Las obras que sostienen el contenido. La columna **Clases** dice en cuántas de
las 288 clases se apoya cada una.

| Autor | Obra | Editorial | Año | Localizador | Clases |
|---|---|---|---:|---|---:|
| Aaker, David | *Building Strong Brands* | Simon & Schuster Ltd | 2002 | [ISBN-13 9780743232135](https://openlibrary.org/isbn/9780743232135) | 4 |
| Ambrose, Susan A. | *How Learning Works* | John Wiley & Sons, Incorporated | 2010 | [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601) | 288 |
| Anderson, David J. | *Kanban* | Blue hole press | 2010 | [ISBN-13 9780984521401](https://openlibrary.org/isbn/9780984521401) | 7 |
| Anderson, Ross | *Security Engineering* | John Wiley & Sons, Incorporated | 2001 | [ISBN-13 9781119642831](https://openlibrary.org/isbn/9781119642831) | 5 |
| Armstrong, Michael | *Armstrong's Handbook of Human Resource Management Practice* | Kogan Page, Limited | 2023 | [ISBN-13 9781398606654](https://openlibrary.org/isbn/9781398606654) | 14 |
| Aulet, Bill | *Disciplined Entrepreneurship* | John Wiley & Sons, Incorporated | 2013 | [ISBN-13 9781299848641](https://openlibrary.org/isbn/9781299848641) | 17 |
| Bazerman, Max H. | *Judgment in Managerial Decision Making* | John Wiley & Sons Inc | — | [ISBN-13 9781119427384](https://openlibrary.org/isbn/9781119427384) | 5 |
| Bland, David J. | *Testing Business Ideas* | Wiley | 2019 | [ISBN-13 9781119551447](https://openlibrary.org/isbn/9781119551447) | 17 |
| Blank, Steve | *The Four Steps to the Epiphany* | [Steve Blank?] | 2013 | [ISBN-13 9780989200509](https://openlibrary.org/isbn/9780989200509) | 12 |
| Bossidy, Larry | *Execution* | — | 2002 | [ISBN-13 9781598954838](https://openlibrary.org/isbn/9781598954838) | 17 |
| Boudreau, John | *Beyond HR* | Harvard Business School Press | 2007 | [ISBN-13 9781422104156](https://openlibrary.org/isbn/9781422104156) | 5 |
| Brealey, Richard et al. | *Principles of Corporate Finance* | McGraw-Hill International Book Co | 1984 | [ISBN-13 9780070662025](https://openlibrary.org/isbn/9780070662025) | 21 |
| Brown, Brené | *Dare to Lead* | Ebury Publishing | 2018 | [ISBN-13 9781473562523](https://openlibrary.org/isbn/9781473562523) | 4 |
| Brown, Peter C. et al. | *Make It Stick* | Harvard University Press | 2014 | [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572) | 288 |
| Buckingham, Marcus | *First, Break All the Rules* | Simon and Schuster | 1999 | [ISBN-13 9780684852867](https://openlibrary.org/isbn/9780684852867) | 12 |
| Cagan, Marty | *Inspired* | Shroff | 2008 | [ISBN-13 9789352131501](https://openlibrary.org/isbn/9789352131501) | 12 |
| Carnegie, Dale | *How to Win Friends and Influence People* | Min zhu yu jian she chu ban she | 2004 | [ISBN-13 9787801121820](https://openlibrary.org/isbn/9787801121820) | 4 |
| Charan, Ram | *Boards That Deliver* | John Wiley & Sons, Incorporated | 2007 | [ISBN-13 9781118046616](https://openlibrary.org/isbn/9781118046616) | 8 |
| Charan, Ram et al. | *The Leadership Pipeline* | Jossey-Bass | 2000 | [ISBN-13 9780787951726](https://openlibrary.org/isbn/9780787951726) | 9 |
| Charan, Ram | *What the CEO Wants You to Know* | Crown | 2001 | [ISBN-13 9780609504239](https://openlibrary.org/isbn/9780609504239) | 5 |
| Christensen, Clayton | *How Will You Measure Your Life?* | Harvard Business Review Press | 2017 | [ISBN-13 9781633692565](https://openlibrary.org/isbn/9781633692565) | 5 |
| Christensen, Clayton M. | *Competing Against Luck* | HarperBusiness | 2016 | [ISBN-13 9780062435613](https://openlibrary.org/isbn/9780062435613) | 8 |
| Christensen, Clayton M. | *The Innovator's Dilemma* | Harvard Business School Press | 1997 | [ISBN-13 9780875845852](https://openlibrary.org/isbn/9780875845852) | 5 |
| Cialdini, Robert B. | *Influence* | HarperCollins Publishers and Blackstone Audio | 2016 | [ISBN-13 9781624608049](https://openlibrary.org/isbn/9781624608049) | 17 |
| Clarke, Richard A. | *The Fifth Domain* | Penguin Press | 2019 | [ISBN-13 9780525561965](https://openlibrary.org/isbn/9780525561965) | 5 |
| Clear, James | *Atomic Habits* | Avery, an Imprint of Penguin Random House LLC | 2018 | [ISBN-13 9780735211292](https://openlibrary.org/isbn/9780735211292) | 5 |
| Damodaran, Aswath | *Investment Valuation* | John Wiley & Sons, Incorporated | 2012 | [ISBN-13 9781118206546](https://openlibrary.org/isbn/9781118206546) | 14 |
| Davenport, Thomas H. | *All-In on AI* | Harvard Business Review Press | 2022 | [ISBN-13 9781647824693](https://openlibrary.org/isbn/9781647824693) | 12 |
| Davenport, Thomas H. | *Competing on Analytics* | Harvard Business School Press | 2007 | [ISBN-13 9781422103326](https://openlibrary.org/isbn/9781422103326) | 5 |
| Deming, W. Edwards | *Out of the Crisis* | The MIT Press | 2000 | [ISBN-13 9780262541152](https://openlibrary.org/isbn/9780262541152) | 8 |
| DePamphilis, Donald | *Mergers, Acquisitions, and Other Restructuring Activities* | Elsevier Science & Technology Books | 2001 | [ISBN-13 9780323910545](https://openlibrary.org/isbn/9780323910545) | 5 |
| Dignan, Aaron | *Brave New Work* | Portfolio | 2019 | [ISBN-13 9780525536208](https://openlibrary.org/isbn/9780525536208) | 5 |
| Dixit, Avinash K. | *The Art of Strategy* | Norton & Company, Incorporated, W. W. | 2008 | [ISBN-13 9780393069952](https://openlibrary.org/isbn/9780393069952) | 5 |
| Dixon, Matthew | *The Challenger Sale* | Portfolio/Penguin | 2011 | [ISBN-13 9781591844358](https://openlibrary.org/isbn/9781591844358) | 12 |
| Doerr, John | *Measure What Matters* | Penguin Random House USA Ex | 2018 | [ISBN-13 9780525538349](https://openlibrary.org/isbn/9780525538349) | 12 |
| Doerr, John | *Speed & Scale* | Penguin Publishing Group | 2021 | [ISBN-13 9780593420478](https://openlibrary.org/isbn/9780593420478) | 5 |
| Drucker, Peter F. | *Management: Tasks, Responsibilities, Practices* | Harper & Row | 1974 | [ISBN-13 9780060110925](https://openlibrary.org/isbn/9780060110925) | 52 |
| Drucker, Peter F. | *The Effective Executive* | Collins | 2002 | [ISBN-13 9780060516079](https://openlibrary.org/isbn/9780060516079) | 36 |
| Duarte, Nancy | *Resonate* | John Wiley & Sons, Incorporated | 2010 | [ISBN-13 9781118014875](https://openlibrary.org/isbn/9781118014875) | 5 |
| Duckworth, Angela | *Grit* | Collins | 2018 | [ISBN-13 9781443442329](https://openlibrary.org/isbn/9781443442329) | 5 |
| Duke, Annie | *How to Decide* | Portfolio | 2020 | [ISBN-13 9780593418482](https://openlibrary.org/isbn/9780593418482) | 7 |
| Duke, Annie | *Thinking in Bets* | Portfolio/Penguin | 2019 | [ISBN-13 9780735216358](https://openlibrary.org/isbn/9780735216358) | 12 |
| Dunford, April | *Obviously Awesome* | Ambient Press | 2019 | [ISBN-13 9781999023003](https://openlibrary.org/isbn/9781999023003) | 12 |
| Edmondson, Amy C. | *The Fearless Organization* | Wiley | 2018 | [ISBN-13 9781119477242](https://openlibrary.org/isbn/9781119477242) | 5 |
| Ellet, William | *The Case Study Handbook* | Harvard Business Review Press | 2018 | [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150) | 288 |
| Ellis, Sean | *Hacking Growth* | Ebury Publishing | 2017 | [ISBN-13 9780753545386](https://openlibrary.org/isbn/9780753545386) | 5 |
| Ericsson, Anders | *Peak* | Penguin Random House | 2016 | [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143) | 288 |
| Feld, Brad | *Venture Deals* | Wiley | 2011 | [ISBN-13 9781118443613](https://openlibrary.org/isbn/9781118443613) | 5 |
| Fisher, Roger et al. | *Getting to Yes* | Hutchinson | 1983 | [ISBN-13 9780091493714](https://openlibrary.org/isbn/9780091493714) | 24 |
| Fitzpatrick, Rob | *The Mom Test* | CreateSpace | 2014 | [ISBN-13 9781492180746](https://openlibrary.org/isbn/9781492180746) | 10 |
| Forsgren, Nicole et al. | *Accelerate* | IT Revolution Press | 2018 | [ISBN-13 9781942788379](https://openlibrary.org/isbn/9781942788379) | 10 |
| Galbraith, Jay R. | *Designing Organizations* | Jossey-Bass Publishers | 1995 | [ISBN-13 9780787900915](https://openlibrary.org/isbn/9780787900915) | 17 |
| Gawande, Atul | *The Checklist Manifesto* | Penguin Random House | 2014 | [ISBN-13 9780143423225](https://openlibrary.org/isbn/9780143423225) | 4 |
| Gerber, Michael E. | *The E-Myth Revisited* | HarperAudio | 1995 | [ISBN-13 9780060574901](https://openlibrary.org/isbn/9780060574901) | 24 |
| Gil, Elad | *High Growth Handbook* | Stripe Matter Inc | 2018 | [ISBN-13 9781953953377](https://openlibrary.org/isbn/9781953953377) | 5 |
| Goldratt, Eliyahu M. | *The Goal* | HighBridge Audio | 2014 | [ISBN-13 9781622313945](https://openlibrary.org/isbn/9781622313945) | 17 |
| Goleman, Daniel | *Emotional Intelligence* | Bloomsbury | 1996 | [ISBN-13 9780747528302](https://openlibrary.org/isbn/9780747528302) | 12 |
| Goleman, Daniel et al. | *Primal Leadership* | Harvard Business School Press | 2002 | [ISBN-13 9781578514861](https://openlibrary.org/isbn/9781578514861) | 17 |
| Grant, Adam | *Think Again* | PENGUIN US | 2021 | [ISBN-13 9780593298749](https://openlibrary.org/isbn/9780593298749) | 5 |
| Grove, Andrew S. | *High Output Management* | Random House | 1983 | [ISBN-13 9780394532349](https://openlibrary.org/isbn/9780394532349) | 26 |
| Hackman, J. Richard | *Leading Teams* | Harvard Business School Press | 2002 | [ISBN-13 9781578513338](https://openlibrary.org/isbn/9781578513338) | 12 |
| Hammer, Michael | *Reengineering the Corporation* | HarperBusiness | 2001 | [ISBN-13 9780066621128](https://openlibrary.org/isbn/9780066621128) | 10 |
| Harnish, Verne | *Scaling Up* | Gazelles, Inc. | 2014 | [ISBN-13 9780986019555](https://openlibrary.org/isbn/9780986019555) | 12 |
| Heath, Chip | *Made to Stick* | Penguin Random House | 2007 | [ISBN-13 9781905211562](https://openlibrary.org/isbn/9781905211562) | 12 |
| Heath, Chip | *Switch* | Penguin Random House | 1999 | [ISBN-13 9781847940308](https://openlibrary.org/isbn/9781847940308) | 7 |
| Heifetz, Ronald | *Leadership on the Line* | Harvard Business Review Press | 2017 | [ISBN-13 9781633692831](https://openlibrary.org/isbn/9781633692831) | 12 |
| Heifetz, Ronald A. | *Leadership Without Easy Answers* | Belknap Press of Harvard University Press | 1994 | [ISBN-13 9780674518582](https://openlibrary.org/isbn/9780674518582) | 7 |
| Helmer, Hamilton | *7 Powers* | Deep Strategy | 2016 | [ISBN-13 9780998116303](https://openlibrary.org/isbn/9780998116303) | 5 |
| Hoffman, Reid | *Blitzscaling* | HarperCollins Publishers Limited | 2018 | [ISBN-13 9780008303648](https://openlibrary.org/isbn/9780008303648) | 8 |
| Horngren, Charles | *Cost Accounting: A Managerial Emphasis* | Prentice Hall College Div | 2002 | [ISBN-13 9780130650061](https://openlibrary.org/isbn/9780130650061) | 6 |
| Horowitz, Ben | *The Hard Thing About Hard Things* | HarperCollins Publishers | 2014 | [ISBN-13 9780062273215](https://openlibrary.org/isbn/9780062273215) | 26 |
| Hull, John C. | *Risk Management and Financial Institutions* | John Wiley & Sons, Incorporated | 2006 | [ISBN-13 9781118286388](https://openlibrary.org/isbn/9781118286388) | 12 |
| Iansiti, Marco | *Competing in the Age of AI* | Harvard Business Review Press | 2020 | [ISBN-13 9781633697621](https://openlibrary.org/isbn/9781633697621) | 12 |
| Ibarra, Herminia | *Act Like a Leader, Think Like a Leader* | Harvard Business Review Press | 2015 | [ISBN-13 9781422184127](https://openlibrary.org/isbn/9781422184127) | 7 |
| Institute, Project Management | *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | Project Management Institute | 1996 | [ISBN-13 9781880410127](https://openlibrary.org/isbn/9781880410127) | 12 |
| Kahneman, Daniel | *Thinking, Fast and Slow* | Farrar, Straus and Giroux | 2011 | [ISBN-13 9780374275631](https://openlibrary.org/isbn/9780374275631) | 12 |
| Kaplan, Robert S. | *Strategy Maps* | Harvard Business School Press | 2004 | [ISBN-13 9781591391340](https://openlibrary.org/isbn/9781591391340) | 5 |
| Kaplan, Robert S. | *The Balanced Scorecard* | Harvard Business School Press | 1996 | [ISBN-13 9780875846514](https://openlibrary.org/isbn/9780875846514) | 17 |
| Katzenbach, Jon R. | *The Wisdom of Teams* | McGraw-Hill | 2005 | [ISBN-13 9780077111687](https://openlibrary.org/isbn/9780077111687) | 12 |
| Kerzner, Harold | *Project Management* | John Wiley & Sons Inc | 2003 | [ISBN-13 9780471281580](https://openlibrary.org/isbn/9780471281580) | 12 |
| Kieso, Donald E. et al. | *Intermediate Accounting* | John Wiley & Sons, Incorporated | 2006 | [ISBN-13 9780470098189](https://openlibrary.org/isbn/9780470098189) | 12 |
| Kim, Gene | *The Phoenix Project* | IT Revolution Press | 2018 | [ISBN-13 9781942788294](https://openlibrary.org/isbn/9781942788294) | 5 |
| Kim, Gene | *The Unicorn Project* | IT Revolution Press | 2019 | [ISBN-13 9781942788768](https://openlibrary.org/isbn/9781942788768) | 5 |
| Kim, W. Chan | *Blue Ocean Strategy* | Coach Series | 2006 | [ISBN-13 9781596590687](https://openlibrary.org/isbn/9781596590687) | 5 |
| Klein, Gary | *Sources of Power* | The MIT Press | 1999 | [ISBN-13 9780262611466](https://openlibrary.org/isbn/9780262611466) | 12 |
| Kleppmann, Martin | *Designing Data-Intensive Applications* | O'Reilly publications | 2017 | [ISBN-13 9789352135240](https://openlibrary.org/isbn/9789352135240) | 5 |
| Koller, Tim et al. | *Valuation: Measuring and Managing the Value of Companies* | Wiley | 2005 | [ISBN-13 9780471702191](https://openlibrary.org/isbn/9780471702191) | 29 |
| Kotler, Philip | *Marketing Management* | Pearson Education | 2016 | [ISBN-13 9781292092621](https://openlibrary.org/isbn/9781292092621) | 12 |
| Kotter, John P. | *Accelerate* | Harvard Business Review Press | 2014 | [ISBN-13 9781625271747](https://openlibrary.org/isbn/9781625271747) | 4 |
| Kotter, John P. | *Leading Change* | Harvard Business School Press | 1996 | [ISBN-13 9780875847474](https://openlibrary.org/isbn/9780875847474) | 12 |
| Lafley, A.G. | *Playing to Win* | Harvard Business Review Press | 2013 | [ISBN-13 9781422187395](https://openlibrary.org/isbn/9781422187395) | 7 |
| Laloux, Frederic | *Reinventing Organizations* | Nelson Parker | 2014 | [ISBN-13 9782960133516](https://openlibrary.org/isbn/9782960133516) | 5 |
| Leblanc, Richard | *Inside the Boardroom* | John Wiley & Sons, Incorporated | 2009 | [ISBN-13 9780470739952](https://openlibrary.org/isbn/9780470739952) | 12 |
| Lencioni, Patrick | *Death by Meeting* | Audio Renaissance | 2004 | [ISBN-13 9781593974411](https://openlibrary.org/isbn/9781593974411) | 5 |
| Lencioni, Patrick | *The Advantage* | John Wiley & Sons, Incorporated | 2012 | [ISBN-13 9781118147856](https://openlibrary.org/isbn/9781118147856) | 5 |
| Lencioni, Patrick | *The Five Dysfunctions of a Team* | Pfeiffer | 2012 | [ISBN-13 9781118127308](https://openlibrary.org/isbn/9781118127308) | 12 |
| Liker, Jeffrey K. | *The Toyota Way* | American Media International | 2005 | [ISBN-13 9781932378702](https://openlibrary.org/isbn/9781932378702) | 4 |
| Malhotra, Deepak | *Negotiation Genius* | Tantor Media | 2007 | [ISBN-13 9781400135400](https://openlibrary.org/isbn/9781400135400) | 4 |
| Mankins, Michael C. | *Time, Talent, Energy* | Harvard Business Review Press | 2017 | [ISBN-13 9781633691766](https://openlibrary.org/isbn/9781633691766) | 9 |
| Marr, Bernard | *Key Performance Indicators* | Pearson Financial Times Pub. | 2012 | [ISBN-13 9780273750116](https://openlibrary.org/isbn/9780273750116) | 12 |
| McAfee, Andrew | *Machine, Platform, Crowd* | Norton & Company, Incorporated, W. W. | 2017 | [ISBN-13 9780393254303](https://openlibrary.org/isbn/9780393254303) | 7 |
| McChrystal, Stanley | *Team of Teams* | Penguin Books, Limited | 2015 | [ISBN-13 9780241250846](https://openlibrary.org/isbn/9780241250846) | 9 |
| McGrath, Rita Gunther | *The End of Competitive Advantage* | Harvard Business Review Press | 2013 | [ISBN-13 9781422172810](https://openlibrary.org/isbn/9781422172810) | 5 |
| McKeown, Greg | *Essentialism* | Virgin Books | 2014 | [ISBN-13 9780753555163](https://openlibrary.org/isbn/9780753555163) | 9 |
| Meadows, Donella H. | *Thinking in Systems* | Earthscan | 2009 | [ISBN-13 9781849773386](https://openlibrary.org/isbn/9781849773386) | 5 |
| Minto, Barbara | *The Pyramid Principle* | Financial Times/ Prentice Hall | 2005 | [ISBN-13 9781405822145](https://openlibrary.org/isbn/9781405822145) | 4 |
| Mochary, Matt | *The Great CEO Within* | Mochary Films | 2019 | [ISBN-13 9780578599281](https://openlibrary.org/isbn/9780578599281) | 12 |
| Monks, Robert A. G. | *Corporate Governance* | John Wiley & Sons, Incorporated | 2001 | [ISBN-13 9781118874899](https://openlibrary.org/isbn/9781118874899) | 5 |
| Moore, Geoffrey A. | *Crossing the Chasm* | HarperBusiness | 1995 | [ISBN-13 9780887307171](https://openlibrary.org/isbn/9780887307171) | 7 |
| Nagle, Thomas T. et al. | *The Strategy and Tactics of Pricing* | Taylor & Francis Group | 1987 | [ISBN-13 9781315266220](https://openlibrary.org/isbn/9781315266220) | 5 |
| Newport, Cal | *Deep Work* | Grand Central Publishing | 2016 | [ISBN-13 9781455586691](https://openlibrary.org/isbn/9781455586691) | 10 |
| Noe, Raymond | *Human Resource Management* | Irwin/McGraw-Hill | 2002 | [ISBN-13 9780072469943](https://openlibrary.org/isbn/9780072469943) | 13 |
| Northouse, Peter G. | *Leadership: Theory and Practice* | Sage Publications (CA) | 2012 | [ISBN-13 9781452226378](https://openlibrary.org/isbn/9781452226378) | 5 |
| Olsen, Dan | *The Lean Product Playbook* | Wiley | 2015 | [ISBN-13 9781118960875](https://openlibrary.org/isbn/9781118960875) | 5 |
| Osterwalder, Alexander | *Business Model Generation* | Wiley  | 2010 | [ISBN-13 9780470876411](https://openlibrary.org/isbn/9780470876411) | 17 |
| Osterwalder, Alexander | *Value Proposition Design* | John Wiley & Sons, Incorporated | 2014 | [ISBN-13 9781118968062](https://openlibrary.org/isbn/9781118968062) | 9 |
| Palepu, Krishna G. et al. | *Business Analysis and Valuation* | South-Western College Pub | 1996 | [ISBN-13 9780324375817](https://openlibrary.org/isbn/9780324375817) | 5 |
| Patterson, Kerry | *Crucial Conversations* | McGraw Hill | 2012 | [ISBN-13 9781259005213](https://openlibrary.org/isbn/9781259005213) | 5 |
| Penman, Stephen H. | *Financial Statement Analysis and Security Valuation* | McGraw-Hill/Irwin | 2001 | [ISBN-13 9780072903331](https://openlibrary.org/isbn/9780072903331) | 12 |
| Perri, Melissa | *Escaping the Build Trap* | O'Reilly | 2019 | [ISBN-13 9781491973790](https://openlibrary.org/isbn/9781491973790) | 4 |
| Pink, Daniel H. | *Drive* | Riverhead Books | 2009 | [ISBN-13 9781594488849](https://openlibrary.org/isbn/9781594488849) | 5 |
| Polman, Paul | *Net Positive* | Harvard Business Review Press | 2021 | [ISBN-13 9781647821302](https://openlibrary.org/isbn/9781647821302) | 4 |
| Porter, Michael E. | *Competitive Advantage* | Free Press | 1985 | [ISBN-13 9780029250907](https://openlibrary.org/isbn/9780029250907) | 12 |
| Porter, Michael E. | *Competitive Strategy* | Free Press | 1980 | [ISBN-13 9780684841489](https://openlibrary.org/isbn/9780684841489) | 12 |
| Porter, Michael E. | *Creating Shared Value* | Managing Sustainable Business | 2018 | [DOI](https://doi.org/10.1007/978-94-024-1144-7_16) | 5 |
| Provost, Foster | *Data Science for Business* | SHROFF - O'REILLY | 2013 | [ISBN-13 9789351102670](https://openlibrary.org/isbn/9789351102670) | 5 |
| Rackham, Neil | *Major Account Sales Strategy* | McGraw-Hill | 1989 | [ISBN-13 9780070511149](https://openlibrary.org/isbn/9780070511149) | 5 |
| Rackham, Neil | *SPIN Selling* | Highbridge Audio | 1998 | [ISBN-13 9781565112605](https://openlibrary.org/isbn/9781565112605) | 12 |
| Raiffa, Howard | *Decision Analysis* | McGraw-Hill | 1997 | [ISBN-13 9780070525795](https://openlibrary.org/isbn/9780070525795) | 5 |
| Ries, Al | *Positioning* | American Media International | 2004 | [ISBN-13 9781932378252](https://openlibrary.org/isbn/9781932378252) | 5 |
| Ries, Eric | *The Lean Startup* | Crown Business | 2011 | [ISBN-13 9780307887894](https://openlibrary.org/isbn/9780307887894) | 14 |
| Roberge, Mark | *The Sales Acceleration Formula* | — | 2015 | [ISBN-13 9781119047070](https://openlibrary.org/isbn/9781119047070) | 5 |
| Ross, Aaron | *From Impossible to Inevitable* | John Wiley & Sons, Incorporated | 2016 | [ISBN-13 9781119166726](https://openlibrary.org/isbn/9781119166726) | 5 |
| Ross, Aaron | *Predictable Revenue* | Pebblestorm | 2020 | [ISBN-13 9780984380244](https://openlibrary.org/isbn/9780984380244) | 5 |
| Ross, Stephen et al. | *Corporate Finance* | McGraw-Hill Education | 2018 | [ISBN-13 9781259918940](https://openlibrary.org/isbn/9781259918940) | 21 |
| Rumelt, Richard | *Good Strategy/Bad Strategy* | Profile Books | 2011 | [ISBN-13 9781846684807](https://openlibrary.org/isbn/9781846684807) | 22 |
| Rummler, Geary A. | *Improving Performance* | Jossey-Bass | 1995 | [ISBN-13 9780787900908](https://openlibrary.org/isbn/9780787900908) | 5 |
| Schein, Edgar H. | *Humble Inquiry* | ReadHowYouWant.com, Limited | 2013 | [ISBN-13 9780369308443](https://openlibrary.org/isbn/9780369308443) | 5 |
| Schein, Edgar H. | *Organizational Culture and Leadership* | John Wiley & Sons, Incorporated | 1991 | [ISBN-13 9780470640562](https://openlibrary.org/isbn/9780470640562) | 12 |
| Schilit, Howard et al. | *Financial Shenanigans* | McGraw-Hill Education on Brilliance Audio | 2018 | [ISBN-13 9781978605459](https://openlibrary.org/isbn/9781978605459) | 5 |
| Scott, Kim | *Radical Candor* | PAN MACMILLAN U.K | 2017 | [ISBN-13 9781509845385](https://openlibrary.org/isbn/9781509845385) | 10 |
| Senge, Peter M. | *The Fifth Discipline* | Random House Audio | 1994 | [ISBN-13 9780553473216](https://openlibrary.org/isbn/9780553473216) | 5 |
| Sharp, Byron | *How Brands Grow* | BookBaby | 2010 | [ISBN-13 9781483534701](https://openlibrary.org/isbn/9781483534701) | 12 |
| Slack, Nigel | *Operations Management* | Pearson Education, Limited | 2019 | [ISBN-13 9781292254036](https://openlibrary.org/isbn/9781292254036) | 12 |
| Stanier, Michael Bungay | *The Coaching Habit* | Page Two/Portfolio/Canongate Books/Simon & Schuster UK | 2016 | [ISBN-13 9780978440749](https://openlibrary.org/isbn/9780978440749) | 5 |
| Stone, Douglas et al. | *Difficult Conversations* | Random House Audio | 1999 | [ISBN-13 9780553525687](https://openlibrary.org/isbn/9780553525687) | 8 |
| Sutton, Robert I. | *Good Boss, Bad Boss* | Business Plus | 2010 | [ISBN-13 9780446556088](https://openlibrary.org/isbn/9780446556088) | 7 |
| Sutton, Robert I. | *Scaling Up Excellence* | Random House Canada | 2014 | [ISBN-13 9780307363428](https://openlibrary.org/isbn/9780307363428) | 12 |
| Taleb, Nassim Nicholas | *Antifragile* | Random House | 2012 | [ISBN-13 9780679645276](https://openlibrary.org/isbn/9780679645276) | 7 |
| Teece, David J. et al. | *Dynamic Capabilities and Strategic Management* | Strategic Management Journal | 1997 | [DOI](https://doi.org/10.1002/(SICI)1097-0266(199708)18:7<509::AID-SMJ882>3.0.CO;2-Z) | 4 |
| Tetlock, Philip | *Superforecasting* | Crown | 2015 | [ISBN-13 9781101905562](https://openlibrary.org/isbn/9781101905562) | 4 |
| Thaler, Richard | *Nudge* | Penguin Books | 2009 | [ISBN-13 9780143115267](https://openlibrary.org/isbn/9780143115267) | 5 |
| Torres, Teresa | *Continuous Discovery Habits* | Product Talk LLC | 2021 | [ISBN-13 9781736633304](https://openlibrary.org/isbn/9781736633304) | 12 |
| Tricker, Bob | *Corporate Governance* | Oxford University Press | 2019 | [ISBN-13 9780198809869](https://openlibrary.org/isbn/9780198809869) | 17 |
| Ulrich, Dave | *Human Resource Champions* | Harvard Business School Press | 1997 | [ISBN-13 9780875847191](https://openlibrary.org/isbn/9780875847191) | 4 |
| Voss, Chris | *Never Split the Difference* | Penguin Random House | 2016 | [ISBN-13 9781847941480](https://openlibrary.org/isbn/9781847941480) | 12 |
| Wasserman, Noam | *The Founder's Dilemmas* | Princeton University Press | 2012 | [ISBN-13 9780691149134](https://openlibrary.org/isbn/9780691149134) | 17 |
| Watkins, Michael D. | *The First 90 Days* | Harvard Business School Press | 2003 | [ISBN-13 9781591391104](https://openlibrary.org/isbn/9781591391104) | 19 |
| Weinberg, Gabriel | *Traction* | Gildan Media | 2015 | [ISBN-13 9781469096230](https://openlibrary.org/isbn/9781469096230) | 5 |
| Westerman, George et al. | *Leading Digital* | Harvard Business Review Press | 2014 | [ISBN-13 9781625272478](https://openlibrary.org/isbn/9781625272478) | 12 |
| Whitmore, John | *Coaching for Performance* | Ediciones Paidos Iberica | 2003 | [ISBN-13 9788449314322](https://openlibrary.org/isbn/9788449314322) | 10 |
| Wiggins, Grant | *Understanding by Design* | Pearson Education, Inc. | 2006 | [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849) | 288 |
| Wiseman, Liz | *Multipliers* | — | 2017 | [ISBN-13 9780062663078](https://openlibrary.org/isbn/9780062663078) | 5 |
| Womack, James P. | *Lean Thinking* | Free Press | 2003 | [ISBN-13 9780743231640](https://openlibrary.org/isbn/9780743231640) | 12 |
| Womack, James P. et al. | *The Machine That Changed the World* | Free Press | 2007 | [ISBN-13 9780743299794](https://openlibrary.org/isbn/9780743299794) | 5 |
| Yukl, Gary | *Leadership in Organizations* | Prentice Hall | 2010 | [ISBN-13 9780132424318](https://openlibrary.org/isbn/9780132424318) | 5 |

## 🏛️ Fuentes oficiales y normas

No son bibliografía y no se tratan igual: no se contrastan, se verifican en
origen y **caducan**. Por eso cada fila lleva la fecha en que se comprobó que
respondía y las partes del programa que la usan.

| Organismo | Documento | Localizador | Consultado | Partes |
|---|---|---|---|---|
| AFC Chile | Seguro de Cesantía: información y operación oficial | [www.afc.cl](https://www.afc.cl/) | 2026-08-19 | 21 |
| Biblioteca del Congreso Nacional de Chile | LeyChile: Código del Trabajo (texto vigente) | [www.bcn.cl](https://www.bcn.cl/leychile/navegar?idNorma=207436) | 2026-08-19 | 21 |
| Biblioteca del Congreso Nacional de Chile | LeyChile: Código del Trabajo y legislación laboral vigente | [www.bcn.cl](https://www.bcn.cl/leychile/) | 2026-08-19 | 21 |
| Biblioteca del Congreso Nacional de Chile | LeyChile: Código Tributario y Ley sobre Impuesto a las Ventas y Servicios | [www.bcn.cl](https://www.bcn.cl/leychile/) | 2026-08-19 | 21 |
| Biblioteca del Congreso Nacional de Chile | LeyChile: Ley N.º 20.659 y normativa vinculada | [www.bcn.cl](https://www.bcn.cl/leychile/) | 2026-08-19 | 21 |
| ChileAtiende | Trámites y orientación del Estado | [www.chileatiende.gob.cl](https://www.chileatiende.gob.cl/) | 2026-08-19 | 21 |
| Colegio de Contadores de Chile | Normativa contable aplicable y NIIF según tipo de entidad | — pendiente | — | 21 |
| Comisión para el Mercado Financiero (Chile) | Normativa e información del mercado financiero | [www.cmfchile.cl](https://www.cmfchile.cl/) | 2026-08-19 | 21 |
| Corporación de Fomento de la Producción (Chile) | Programas, instrumentos y apoyo empresarial | [www.corfo.cl](https://www.corfo.cl/) | 2026-08-19 | 21 |
| COSO | Enterprise Risk Management—Integrating with Strategy and Performance | [www.coso.org](https://www.coso.org/) | 2026-08-19 | 15, 17 |
| Departamento de Derechos Intelectuales (Chile) | Derecho de autor: registro y orientación oficial | [www.propiedadintelectual.gob.cl](https://www.propiedadintelectual.gob.cl/) | 2026-08-19 | 21 |
| Dirección ChileCompra | Mercado Público y normativa de compras públicas | [www.chilecompra.cl](https://www.chilecompra.cl/) | 2026-08-19 | 21 |
| Dirección del Trabajo (Chile) | Cláusulas mínimas del contrato de trabajo | [www.dt.gob.cl](https://www.dt.gob.cl/portal/1628/w3-article-60800.html) | 2026-08-19 | 21 |
| Dirección del Trabajo (Chile) | Contrato individual de trabajo | [dt.gob.cl](https://dt.gob.cl/portal/1626/w3-article-100172.html) | 2026-08-19 | 21 |
| Dirección del Trabajo (Chile) | Implementación de la rebaja de jornada a 42 horas (Ord. N°253/21) | [dt.gob.cl](https://dt.gob.cl/legislacion/1624/w3-article-129189.html) | 2026-08-19 | 21 |
| Dirección del Trabajo (Chile) | Ley Karin y dictámenes asociados | [www.dt.gob.cl](https://www.dt.gob.cl/legislacion/1624/w3-propertyvalue-194488.html) | 2026-08-19 | 21 |
| Dirección del Trabajo (Chile) | Normativa y orientación oficial | [www.dt.gob.cl](https://www.dt.gob.cl/) | 2026-08-19 | 21 |
| For Entrepreneurs (Matrix Partners) | SaaS Metrics resources | [www.forentrepreneurs.com](https://www.forentrepreneurs.com/saas-metrics-2/) | 2026-08-19 | 18 |
| IFRS Foundation | IFRS Accounting Standards | [www.ifrs.org](https://www.ifrs.org/) | — | 09 |
| INAPI (Chile) | Propiedad industrial y orientación oficial | [www.inapi.cl](https://www.inapi.cl/) | 2026-08-19 | 21 |
| ISO | ISO 22301 Business continuity management systems | — pendiente | — | 07 |
| ISO | ISO 31000 Risk management | — pendiente | — | 15 |
| ISO | ISO 9001 Quality management systems | — pendiente | — | 07 |
| NIST | AI Risk Management Framework (AI RMF 1.0) | [www.nist.gov](https://www.nist.gov/itl/ai-risk-management-framework) | 2026-08-19 | 15, 19 |
| NIST | Cybersecurity Framework (CSF) 2.0 | [www.nist.gov](https://www.nist.gov/cyberframework) | 2026-08-19 | 15, 19 |
| OECD | G20/OECD Principles of Corporate Governance 2023 | [www.oecd.org](https://www.oecd.org/en/publications/2023/09/g20-oecd-principles-of-corporate-governance-2023_60836fcb.html) | — | 15, 17, 18, 21, 22 |
| OECD | OECD AI Principles | [oecd.ai](https://oecd.ai/en/ai-principles) | 2026-08-19 | 15 |
| Registro de Empresas y Sociedades (Chile) | Portal y documentación oficial | [www.registrodeempresasysociedades.cl](https://www.registrodeempresasysociedades.cl/) | 2026-08-19 | 21 |
| Registro de Empresas y Sociedades (Chile) | Preguntas frecuentes del portal oficial | [www.registrodeempresasysociedades.cl](https://www.registrodeempresasysociedades.cl/FAQ.aspx) | 2026-08-19 | 21 |
| Scrum.org / Scrum Alliance | The Scrum Guide | [scrumguides.org](https://scrumguides.org/) | 2026-08-19 | 06 |
| Sercotec (Chile) | Programas, capacitación y Centros de Desarrollo de Negocios | [www.sercotec.cl](https://www.sercotec.cl/) | 2026-08-19 | 21 |
| Servicio de Impuestos Internos (Chile) | Acreditación de inicio de actividades y obligaciones tributarias | [www.sii.cl](https://www.sii.cl/destacados/ley_cumplimiento_obligaciones_tributarias/inicio_actividades.html) | 2026-08-19 | 21 |
| Servicio de Impuestos Internos (Chile) | Ayudas para el inicio de actividades | [www.sii.cl](https://www.sii.cl/pagina/registro_contribuyentes/ayudas_inicio_actividades.htm) | 2026-08-19 | 21 |
| Servicio de Impuestos Internos (Chile) | Ciclo de vida del contribuyente: inicio de actividades | [www.sii.cl](https://www.sii.cl/destacados/educacion/ciclo_vida_contribuyente/paso_02.html) | 2026-08-19 | 21 |
| Servicio de Impuestos Internos (Chile) | Guías, normativa y servicios oficiales | [www.sii.cl](https://www.sii.cl/) | 2026-08-19 | 21 |
| Servicio de Impuestos Internos (Chile) | Portal Emprendedor | [www.sii.cl](https://www.sii.cl/portales/emprendedor/) | 2026-08-19 | 21 |
| Servicio de Impuestos Internos (Chile) | SII Educa: inicio de actividades y formalización de un negocio | [www.sii.cl](https://www.sii.cl/siieduca/aprende-con-nosotros/inicio-de-actividades-y-formalizacion-de-un-negocio.html) | 2026-08-19 | 21 |
| Subsecretaría de Previsión Social (Chile) | Decreto Supremo N°44 y material de implementación | [previsionsocial.gob.cl](https://previsionsocial.gob.cl/ds44/) | 2026-08-19 | 21 |
| Subsecretaría de Previsión Social (Chile) | Seguridad y Salud Laboral / Decreto Supremo N°44 | [previsionsocial.gob.cl](https://previsionsocial.gob.cl/ds44/) | 2026-08-19 | 21 |
| Superintendencia de Pensiones (Chile) | Normativa y sistema previsional | [www.spensiones.cl](https://www.spensiones.cl/) | 2026-08-19 | 21 |
| Superintendencia de Seguridad Social (Chile) | Normativa del Seguro de Accidentes del Trabajo y Enfermedades Profesionales | [www.suseso.cl](https://www.suseso.cl/) | 2026-08-19 | 21 |

## 🕓 Qué queda pendiente y por qué

Una fuente pendiente no se borra ni se disimula: se declara con su motivo.

| Fuente | Clases | Motivo |
|---|---:|---|
| OECD — G20/OECD Principles of Corporate Governance 2023 | 28 | HTTP 403 (el servidor rechaza clientes automatizados) |
| IFRS Foundation — IFRS Accounting Standards | 5 | URLError: <urlopen error [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)> |
| ISO — ISO 31000 Risk management | 5 | iso.org responde HTTP 403 a cualquier cliente automatizado, así que el verificador no puede comprobar la página de la norma; consultar el catálogo oficial de ISO a mano |
| ISO — ISO 9001 Quality management systems | 5 | iso.org responde HTTP 403 a cualquier cliente automatizado, así que el verificador no puede comprobar la página de la norma; consultar el catálogo oficial de ISO a mano |
| ISO — ISO 22301 Business continuity management systems | 4 | iso.org responde HTTP 403 a cualquier cliente automatizado, así que el verificador no puede comprobar la página de la norma; consultar el catálogo oficial de ISO a mano |
| Colegio de Contadores de Chile — Normativa contable aplicable y NIIF según tipo de entidad | 1 | el Colegio de Contadores de Chile no publica un localizador estable para este material; verificar el marco contable aplicable con el contador de la entidad |

Última revalidación en red: **2026-08-19**. La ejecuta
`scripts/refresh-sources`, que resuelve ISBN contra Open Library, DOI contra
Crossref y consulta cada URL oficial. Esa capa **no bloquea el CI**: si un
organismo reorganiza su sitio, el programa no se rompe, se entera.

<!-- registro-de-fuentes:fin -->

---

## 🚧 Qué hacer si una fuente ya no está disponible

Los enlaces a documentos oficiales cambian. Si uno no responde:

1. Busca el **título exacto** en el sitio del organismo emisor.
2. Para normas chilenas, el texto vigente está en **[BCN LeyChile](https://www.bcn.cl/leychile/)**.
3. Si el documento fue sustituido, la versión vigente suele citarlo en su introducción.
4. Para un libro, el ISBN-13 sigue siendo válido aunque el enlace falle: sirve en
   cualquier biblioteca o librería.

Si detectas una fuente rota o superada,
**[abre un issue](https://github.com/vladimiracunadev-create/executive-leadership-founder-program/issues)**
indicando la clase y la referencia.

Lo que el repositorio **no** hace es borrarla. Cuando `scripts/refresh-sources`
encuentra un enlace que dejó de responder, la entrada se conserva con su motivo y pasa
a `pendiente`. Un enlace caído dice algo sobre el enlace, no sobre la obra, y eliminar
la referencia haría desaparecer la única pista para reencontrarla.

---

**Ver también:** [Fuentes oficiales](OFFICIAL_SOURCES.md) ·
[Método de lectura](READING_METHOD.md) · [Ética y límites](ETHICS_AND_LIMITATIONS.md) ·
[Temario](../SYLLABUS.md)
