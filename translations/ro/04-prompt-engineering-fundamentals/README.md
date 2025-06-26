<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:27:26+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "ro"
}
-->
# Fundamentele Ingineriei de Prompts

## Introducere
Acest modul acoperă concepte și tehnici esențiale pentru crearea de prompts eficiente în modelele AI generative. Modul în care scrii un prompt pentru un LLM contează de asemenea. Un prompt bine conceput poate obține un răspuns de calitate mai bună. Dar ce înseamnă exact termeni precum _prompt_ și _inginerie de prompts_? Și cum pot îmbunătăți _inputul_ promptului pe care îl trimit către LLM? Acestea sunt întrebările la care vom încerca să răspundem în acest capitol și în următorul.

_AI generativă_ este capabilă să creeze conținut nou (de exemplu, text, imagini, audio, cod etc.) ca răspuns la cererile utilizatorilor. Aceasta realizează acest lucru folosind _Modele de Limbaj de Mare Anvergură_ precum seria GPT ("Generative Pre-trained Transformer") de la OpenAI, care sunt antrenate pentru utilizarea limbajului natural și a codului.

Utilizatorii pot acum interacționa cu aceste modele folosind paradigme familiare precum chatul, fără a avea nevoie de expertiză tehnică sau instruire. Modelele sunt _bazate pe prompts_ - utilizatorii trimit un input de text (prompt) și primesc un răspuns AI (completare). Ei pot apoi să "chatuiască cu AI-ul" în mod iterativ, în conversații cu mai multe runde, rafinându-și promptul până când răspunsul corespunde așteptărilor lor.

"Prompts" devin acum principala _interfață de programare_ pentru aplicațiile AI generative, spunând modelelor ce să facă și influențând calitatea răspunsurilor returnate. "Ingineria de Prompts" este un domeniu de studiu în creștere rapidă care se concentrează pe _designul și optimizarea_ prompturilor pentru a oferi răspunsuri consistente și de calitate la scară.

## Obiective de Învățare

În această lecție, învățăm ce este Ingineria de Prompts, de ce este importantă și cum putem crea prompts mai eficiente pentru un model și un obiectiv de aplicație dat. Vom înțelege conceptele de bază și cele mai bune practici pentru ingineria de prompts - și vom învăța despre un mediu interactiv de tip "sandbox" Jupyter Notebooks unde putem vedea aceste concepte aplicate la exemple reale.

La sfârșitul acestei lecții, vom putea:

1. Explica ce este ingineria de prompts și de ce este importantă.
2. Descrie componentele unui prompt și cum sunt folosite.
3. Învăța cele mai bune practici și tehnici pentru ingineria de prompts.
4. Aplica tehnicile învățate la exemple reale, folosind un endpoint OpenAI.

## Termeni Cheie

Ingineria de Prompts: Practica de a proiecta și rafina inputurile pentru a ghida modelele AI către producerea rezultatelor dorite.
Tokenizare: Procesul de conversie a textului în unități mai mici, numite tokeni, pe care un model le poate înțelege și procesa.
LLM-uri Ajustate pe Instrucțiuni: Modele de Limbaj de Mare Anvergură (LLM-uri) care au fost ajustate cu instrucțiuni specifice pentru a îmbunătăți acuratețea și relevanța răspunsurilor lor.

## Sandbox de Învățare

Ingineria de prompts este în prezent mai mult o artă decât o știință. Cel mai bun mod de a ne îmbunătăți intuiția pentru aceasta este să _practicăm mai mult_ și să adoptăm o abordare de încercare și eroare care combină expertiza în domeniul aplicației cu tehnicile recomandate și optimizările specifice modelului.

Jupyter Notebook-ul care însoțește această lecție oferă un mediu de tip _sandbox_ unde poți încerca ceea ce înveți - pe parcurs sau ca parte a provocării de cod de la final. Pentru a executa exercițiile, vei avea nevoie de:

1. **O cheie API Azure OpenAI** - endpointul de serviciu pentru un LLM implementat.
2. **Un Runtime Python** - în care Notebook-ul poate fi executat.
3. **Variabile de Mediu Locale** - _completați pașii din [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) acum pentru a vă pregăti_.

Notebook-ul vine cu exerciții de _început_ - dar ești încurajat să adaugi propriile secțiuni de _Markdown_ (descriere) și _Cod_ (cereri de prompt) pentru a încerca mai multe exemple sau idei - și a-ți construi intuiția pentru designul prompturilor.

## Ghid Ilustrat

Vrei să obții o imagine de ansamblu a ceea ce acoperă această lecție înainte de a te aprofunda? Consultă acest ghid ilustrat, care îți oferă o idee despre principalele subiecte acoperite și punctele cheie pe care să le iei în considerare la fiecare. Harta lecției te duce de la înțelegerea conceptelor și provocărilor de bază la abordarea acestora cu tehnici și practici de inginerie a prompturilor relevante. Observă că secțiunea "Tehnici Avansate" din acest ghid se referă la conținutul acoperit în capitolul _următor_ al acestui curriculum.

## Startup-ul Nostru

Acum, să vorbim despre cum _acest subiect_ se leagă de misiunea noastră de startup de a [aduce inovația AI în educație](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vrem să construim aplicații alimentate de AI pentru _învățare personalizată_ - așa că să ne gândim cum ar putea "proiecta" prompts utilizatorii diferiți ai aplicației noastre:

- **Administratorii** ar putea cere AI-ului să _analizeze datele curriculare pentru a identifica lacunele de acoperire_. AI-ul poate rezuma rezultatele sau le poate vizualiza cu cod.
- **Educatorii** ar putea cere AI-ului să _genereze un plan de lecție pentru un public țintă și un subiect_. AI-ul poate construi planul personalizat într-un format specificat.
- **Studenții** ar putea cere AI-ului să _îi îndrume într-un subiect dificil_. AI-ul poate acum ghida studenții cu lecții, sugestii și exemple adaptate nivelului lor.

Aceasta este doar vârful aisbergului. Consultă [Prompts pentru Educație](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - o bibliotecă open-source de prompts curată de experți în educație - pentru a obține o imagine mai largă a posibilităților! _Încearcă să rulezi unele dintre acele prompts în sandbox sau folosind OpenAI Playground pentru a vedea ce se întâmplă!_

## Ce este Ingineria de Prompts?

Am început această lecție definind **Ingineria de Prompts** ca procesul de _proiectare și optimizare_ a inputurilor textuale (prompts) pentru a oferi răspunsuri consistente și de calitate (completări) pentru un obiectiv de aplicație și model dat. Putem considera acest lucru ca un proces în două etape:

- _proiectarea_ promptului inițial pentru un model și un obiectiv dat
- _rafinarea_ promptului în mod iterativ pentru a îmbunătăți calitatea răspunsului

Acesta este în mod necesar un proces de încercare și eroare care necesită intuiția și efortul utilizatorului pentru a obține rezultate optime. De ce este important? Pentru a răspunde la această întrebare, trebuie mai întâi să înțelegem trei concepte:

- _Tokenizare_ = cum "vede" modelul promptul
- _LLM-uri de Bază_ = cum "procesează" modelul de bază un prompt
- _LLM-uri Ajustate pe Instrucțiuni_ = cum poate modelul acum să vadă "sarcini"

### Tokenizare

Un LLM vede prompts ca o _secvență de tokeni_ unde diferite modele (sau versiuni ale unui model) pot tokeniza același prompt în moduri diferite. Deoarece LLM-urile sunt antrenate pe tokeni (și nu pe text brut), modul în care prompts sunt tokenizate are un impact direct asupra calității răspunsului generat.

Pentru a obține o intuiție despre cum funcționează tokenizarea, încearcă instrumente precum [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prezentat mai jos. Copiază-ți promptul - și vezi cum este convertit în tokeni, acordând atenție modului în care sunt gestionate caracterele de spațiu alb și semnele de punctuație. Observă că acest exemplu arată un LLM mai vechi (GPT-3) - așa că încercarea acestuia cu un model mai nou poate produce un rezultat diferit.

### Concept: Modele de Bază

Odată ce un prompt este tokenizat, funcția principală a ["LLM-ului de Bază"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (sau model de bază) este să prezică tokenul în acea secvență. Deoarece LLM-urile sunt antrenate pe seturi masive de date textuale, au un bun simț al relațiilor statistice dintre tokeni și pot face acea predicție cu o anumită încredere. Observă că nu înțeleg _sensul_ cuvintelor din prompt sau token; doar văd un model pe care îl pot "completa" cu următoarea lor predicție. Pot continua să prezică secvența până când sunt întrerupte de intervenția utilizatorului sau de o condiție prestabilită.

Vrei să vezi cum funcționează completarea bazată pe prompts? Introdu promptul de mai sus în Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) cu setările implicite. Sistemul este configurat să trateze prompts ca cereri de informații - așa că ar trebui să vezi o completare care satisface acest context.

Dar ce se întâmplă dacă utilizatorul dorește să vadă ceva specific care să îndeplinească anumite criterii sau obiective de sarcină? Aici intră în scenă LLM-urile _ajustate pe instrucțiuni_.

### Concept: LLM-uri Ajustate pe Instrucțiuni

Un [LLM Ajustat pe Instrucțiuni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) pornește de la modelul de bază și îl ajustează fin cu exemple sau perechi de input/output (de exemplu, "mesaje" cu mai multe runde) care pot conține instrucțiuni clare - și răspunsul AI-ului încearcă să urmeze acea instrucțiune.

Acest lucru folosește tehnici precum Învățarea prin Recompensă cu Feedback Uman (RLHF) care pot antrena modelul să _urmeze instrucțiuni_ și să _învețe din feedback_ astfel încât să producă răspunsuri mai potrivite pentru aplicații practice și mai relevante pentru obiectivele utilizatorului.

Să încercăm - revizuiește promptul de mai sus, dar acum schimbă _mesajul sistemului_ pentru a oferi următoarea instrucțiune ca context:

> _Rezumați conținutul care vă este oferit pentru un elev de clasa a doua. Păstrați rezultatul la un paragraf cu 3-5 puncte._

Vezi cum rezultatul este acum ajustat pentru a reflecta obiectivul și formatul dorit? Un educator poate acum folosi direct acest răspuns în slide-urile pentru acea clasă.

## De ce avem nevoie de Ingineria de Prompts?

Acum că știm cum sunt procesate prompts de către LLM-uri, să vorbim despre _de ce_ avem nevoie de ingineria de prompts. Răspunsul constă în faptul că LLM-urile actuale prezintă o serie de provocări care fac _completările fiabile și consistente_ mai greu de obținut fără a depune efort în construcția și optimizarea prompturilor. De exemplu:

1. **Răspunsurile modelului sunt stocastice.** _Același prompt_ va produce probabil răspunsuri diferite cu modele sau versiuni de modele diferite. Și poate produce chiar rezultate diferite cu _același model_ în momente diferite. _Tehnicile de inginerie de prompts ne pot ajuta să minimizăm aceste variații prin oferirea unor ghidaje mai bune_.

2. **Modelele pot fabrica răspunsuri.** Modelele sunt pre-antrenate cu _seturi de date mari dar finite_, ceea ce înseamnă că nu au cunoștințe despre concepte din afara acelei sfere de antrenament. Ca urmare, pot produce completări care sunt inexacte, imaginare sau direct contradictorii cu faptele cunoscute. _Tehnicile de inginerie de prompts ajută utilizatorii să identifice și să atenueze astfel de fabricații, de exemplu, prin cererea de citări sau raționamente AI_.

3. **Capabilitățile modelelor vor varia.** Modelele mai noi sau generațiile de modele vor avea capacități mai bogate, dar vor aduce și ciudățenii unice și compromisuri în cost și complexitate. _Ingineria de prompts ne poate ajuta să dezvoltăm cele mai bune practici și fluxuri de lucru care să abstractizeze diferențele și să se adapteze la cerințele specifice modelului în mod scalabil și fără probleme_.

Să vedem acest lucru în acțiune în OpenAI sau Azure OpenAI Playground:

- Folosește același prompt cu implementări diferite de LLM (de exemplu, OpenAI, Azure OpenAI, Hugging Face) - ai observat variațiile?
- Folosește același prompt în mod repetat cu aceeași implementare de LLM (de exemplu, Azure OpenAI playground) - cum au diferit aceste variații?

### Exemplu de Fabricații

În acest curs, folosim termenul **"fabricație"** pentru a face referire la fenomenul în care LLM-urile generează uneori informații factual incorecte din cauza limitărilor în antrenamentul lor sau a altor constrângeri. Poate ai auzit de asemenea acest lucru menționat ca _"halucinații"_ în articole populare sau lucrări de cercetare. Cu toate acestea, recomandăm cu tărie utilizarea termenului _"fabricație"_ pentru a nu antropomorfiza accidental comportamentul prin atribuirea unei trăsături umane unui rezultat condus de mașină. Acest lucru întărește de asemenea [ghidurile AI Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dintr-o perspectivă terminologică, eliminând termeni care pot fi considerați ofensatori sau neincluzivi în anumite contexte.

Vrei să obții o idee despre cum funcționează fabricațiile? Gândește-te la un prompt care instruiește AI-ul să genereze conținut pentru un subiect inexistent (pentru a te asigura că nu se găsește în setul de date de antrenament). De exemplu - am încercat acest prompt:

> **Prompt:** generează un plan de lecție despre Războiul Marțian din 2076.

O căutare pe web mi-a arătat că existau conturi fictive (de exemplu, seriale de televiziune sau cărți) despre războaie marțiene - dar niciunul în 2076. Bunul simț ne spune de asemenea că 2076 este _în viitor_ și, prin urmare, nu poate fi asociat cu un eveniment real.

Așa că ce se întâmplă când rulăm acest prompt cu diferiți furnizori de LLM?

> **Răspuns 1**: OpenAI Playground (GPT-35)

> **Răspuns 2**: Azure OpenAI Playground (GPT-35)

> **Răspuns 3**: : Hugging Face Chat Playground (LLama-2)

Așa cum era de așteptat, fiecare model (sau versiune de model) produce răspunsuri ușor diferite datorită comportamentului stocastic și variațiilor de capabilități ale modelului. De exemplu, un model țintește un public de clasa a 8-a, în timp ce altul presupune un elev de liceu. Dar toate cele trei modele au generat răspunsuri care ar putea convinge un utilizator neinformat că evenimentul era real.

Tehnicile de inginerie de prompts precum _metaprompting_ și _configurarea temperaturii_ pot reduce fabricațiile modelului într-o anumită măsură. Noile _arhitecturi_ de inginerie de prompts încorporează de asemenea
În cele din urmă, adevărata valoare a șabloanelor constă în capacitatea de a crea și publica _biblioteci de prompturi_ pentru domenii de aplicație verticale - unde șablonul de prompt este acum _optimizat_ pentru a reflecta contextul sau exemplele specifice aplicației, ceea ce face ca răspunsurile să fie mai relevante și mai precise pentru publicul țintă. Repozitoriul [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) este un exemplu excelent al acestei abordări, curând o bibliotecă de prompturi pentru domeniul educației, cu accent pe obiectivele cheie precum planificarea lecțiilor, designul curriculumului, tutoratul studenților etc.

## Conținut Suport

Dacă ne gândim la construirea de prompturi ca având o instrucțiune (sarcină) și un țintă (conținut principal), atunci _conținutul secundar_ este ca un context suplimentar pe care îl oferim pentru a **influența ieșirea într-un anumit fel**. Acesta ar putea fi parametrii de ajustare, instrucțiuni de formatare, taxonomii de subiecte etc. care pot ajuta modelul să _personalizeze_ răspunsul pentru a se potrivi cu obiectivele sau așteptările utilizatorului dorit.

De exemplu: Având un catalog de cursuri cu metadate extinse (nume, descriere, nivel, etichete de metadate, instructor etc.) pentru toate cursurile disponibile în curriculum:

- putem defini o instrucțiune pentru "a rezuma catalogul de cursuri pentru toamna 2023"
- putem folosi conținutul principal pentru a oferi câteva exemple de ieșire dorită
- putem folosi conținutul secundar pentru a identifica primele 5 "etichete" de interes.

Acum, modelul poate oferi un rezumat în formatul arătat de câteva exemple - dar dacă un rezultat are mai multe etichete, poate prioritiza cele 5 etichete identificate în conținutul secundar.

---

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să acopere conceptul de bază #1.
Consolidați conceptul cu exemple și referințe.

CONCEPT #3:
Tehnici de Inginerie a Prompturilor.
Care sunt câteva tehnici de bază pentru ingineria prompturilor?
Ilustrați-le cu câteva exerciții.
-->

## Cele mai bune practici pentru Prompturi

Acum că știm cum pot fi _construite_ prompturile, putem începe să ne gândim cum să le _proiectăm_ pentru a reflecta cele mai bune practici. Putem gândi acest lucru în două părți - având _mentalitatea_ corectă și aplicând _tehnicile_ corecte.

### Mentalitatea de Inginerie a Prompturilor

Ingineria Prompturilor este un proces de încercare și eroare, așa că păstrați în minte trei factori largi de ghidare:

1. **Înțelegerea domeniului contează.** Precizia și relevanța răspunsului este o funcție a _domeniului_ în care operează acea aplicație sau utilizator. Aplicați intuiția și expertiza de domeniu pentru a **personaliza tehnicile** mai departe. De exemplu, definiți _personalități specifice domeniului_ în prompturile sistemului sau folosiți _șabloane specifice domeniului_ în prompturile utilizatorului. Oferiți conținut secundar care reflectă contexte specifice domeniului sau folosiți _indicii și exemple specifice domeniului_ pentru a ghida modelul către modele de utilizare familiare.

2. **Înțelegerea modelului contează.** Știm că modelele sunt stocastice prin natura lor. Dar implementările de modele pot varia și în funcție de setul de date de antrenament pe care îl folosesc (cunoștințe pre-antrenate), capacitățile pe care le oferă (de exemplu, prin API sau SDK) și tipul de conținut pentru care sunt optimizate (de exemplu, cod vs. imagini vs. text). Înțelegeți punctele forte și limitările modelului pe care îl utilizați și folosiți acea cunoaștere pentru a _prioritiza sarcinile_ sau a construi _șabloane personalizate_ care sunt optimizate pentru capacitățile modelului.

3. **Iterarea și validarea contează.** Modelele evoluează rapid, la fel și tehnicile de inginerie a prompturilor. Ca expert în domeniu, s-ar putea să aveți alt context sau criterii pentru _aplicația_ dumneavoastră specifică, care nu se aplică comunității mai largi. Folosiți instrumente și tehnici de inginerie a prompturilor pentru a "încerca" construcția de prompturi, apoi iterați și validați rezultatele folosind propria intuiție și expertiză de domeniu. Înregistrați-vă observațiile și creați o **bază de cunoștințe** (de exemplu, biblioteci de prompturi) care poate fi folosită ca un nou punct de plecare de către alții, pentru iterații mai rapide în viitor.

## Cele mai bune practici

Acum să aruncăm o privire la cele mai bune practici comune recomandate de practicienii [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) și [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ce                               | De ce                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluați cele mai recente modele. | Noile generații de modele sunt susceptibile să aibă caracteristici și calitate îmbunătățite - dar pot implica și costuri mai mari. Evaluați-le pentru impact, apoi luați decizii de migrare.                                                                                |
| Separați instrucțiunile și contextul   | Verificați dacă modelul/provizorul dvs. definește _delimitatori_ pentru a distinge instrucțiunile, conținutul principal și secundar mai clar. Acest lucru poate ajuta modelele să atribuie greutăți mai precise tokenurilor.                                                         |
| Fiți specific și clar             | Oferiți mai multe detalii despre contextul dorit, rezultat, lungime, format, stil etc. Acest lucru va îmbunătăți atât calitatea, cât și consistența răspunsurilor. Capturați rețete în șabloane reutilizabile.                                                          |
| Fiți descriptiv, folosiți exemple      | Modelele pot răspunde mai bine la o abordare de "arată și spune". Începeți cu `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valori. Reveniti la [Secțiunea Sandbox de Învățare](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) pentru a învăța cum.

### În continuare, deschideți Jupyter Notebook

- Selectați kernelul de runtime. Dacă utilizați opțiunile 1 sau 2, selectați pur și simplu kernelul implicit Python 3.10.x oferit de containerul de dezvoltare.

Sunteți gata să rulați exercițiile. Rețineți că nu există _răspunsuri corecte sau greșite_ aici - doar explorarea opțiunilor prin încercare și eroare și construirea intuiției pentru ceea ce funcționează pentru un model și domeniu de aplicație dat.

_Din acest motiv nu există segmente de Soluție Cod în această lecție. În schimb, Notebook-ul va avea celule Markdown intitulate "Soluția Mea:" care arată un exemplu de ieșire pentru referință._

 <!--
ȘABLON LECȚIE:
Încheiați secțiunea cu un rezumat și resurse pentru învățare autodirijată.
-->

## Verificarea cunoștințelor

Care dintre următoarele este un prompt bun urmând câteva practici rezonabile?

1. Arată-mi o imagine a unei mașini roșii
2. Arată-mi o imagine a unei mașini roșii marca Volvo și model XC90 parcată lângă o stâncă cu soarele apunând
3. Arată-mi o imagine a unei mașini roșii marca Volvo și model XC90

R: 2, este cel mai bun prompt deoarece oferă detalii despre "ce" și intră în specific (nu doar orice mașină, ci o marcă și un model specific) și descrie, de asemenea, cadrul general. 3 este următorul cel mai bun, deoarece conține și multe descrieri.

## 🚀 Provocare

Vezi dacă poți valorifica tehnica "indiciului" cu promptul: Completează propoziția "Arată-mi o imagine a unei mașini roșii marca Volvo și ". Ce răspunde și cum ai îmbunătăți-o?

## Lucru Grozav! Continuă Învățarea Ta

Vrei să afli mai multe despre diferite concepte de Inginerie a Prompturilor? Accesează [pagina de învățare continuă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a găsi alte resurse excelente pe acest subiect.

Mergi la Lecția 5 unde vom analiza [tehnici avansate de prompturi](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți de faptul că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană profesională. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.