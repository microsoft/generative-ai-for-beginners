<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:18:31+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "ro"
}
-->
# Fundamentele Ingineriei Prompturilor

## Introducere

Acest modul acoperă concepte și tehnici esențiale pentru crearea de prompturi eficiente în modelele AI generative. Modul în care scrii un prompt pentru un LLM contează. Un prompt bine construit poate obține un răspuns de calitate mai bună. Dar ce înseamnă exact termeni precum _prompt_ și _ingineria prompturilor_? Și cum îmbunătățesc _intrarea promptului_ pe care o trimit la LLM? Acestea sunt întrebările la care vom încerca să răspundem în acest capitol și în cel următor.

AI generativă este capabilă să creeze conținut nou (de exemplu, text, imagini, audio, cod etc.) ca răspuns la cererile utilizatorilor. Realizează acest lucru folosind _Modele de Limbaj de Mari Dimensiuni_ precum seria GPT ("Generative Pre-trained Transformer") de la OpenAI, care sunt antrenate pentru a folosi limbajul natural și codul.

Utilizatorii pot interacționa acum cu aceste modele folosind paradigme familiare precum chat-ul, fără a avea nevoie de expertiză tehnică sau instruire. Modelele sunt bazate pe _prompturi_ - utilizatorii trimit o intrare text (prompt) și primesc înapoi răspunsul AI (completare). Ei pot apoi "conversa cu AI" iterativ, în conversații pe mai multe runde, rafinându-și promptul până când răspunsul corespunde așteptărilor lor.

"Prompturile" devin acum interfața principală de _programare_ pentru aplicațiile AI generative, spunând modelelor ce să facă și influențând calitatea răspunsurilor returnate. "Ingineria Prompturilor" este un domeniu de studiu în creștere rapidă care se concentrează pe _designul și optimizarea_ prompturilor pentru a livra răspunsuri consistente și de calitate la scară.

## Obiectivele Învățării

În această lecție, învățăm ce este Ingineria Prompturilor, de ce contează și cum putem crea prompturi mai eficiente pentru un model și un obiectiv de aplicație dat. Vom înțelege concepte de bază și bune practici pentru ingineria prompturilor - și vom învăța despre un mediu interactiv de tip "sandbox" în Jupyter Notebooks unde putem vedea aceste concepte aplicate la exemple reale.

Până la sfârșitul acestei lecții vom putea:

1. Explica ce este ingineria prompturilor și de ce contează.
2. Descrie componentele unui prompt și cum sunt folosite.
3. Învăța bune practici și tehnici pentru ingineria prompturilor.
4. Aplica tehnicile învățate la exemple reale, folosind un endpoint OpenAI.

## Termeni Cheie

Ingineria Prompturilor: Practica de a proiecta și rafina intrările pentru a ghida modelele AI să producă rezultatele dorite.
Tokenizarea: Procesul de conversie a textului în unități mai mici, numite tokeni, pe care un model le poate înțelege și procesa.
LLM-uri Ajustate prin Instrucțiuni: Modele de Limbaj de Mari Dimensiuni (LLM-uri) care au fost ajustate cu instrucțiuni specifice pentru a îmbunătăți acuratețea și relevanța răspunsurilor lor.

## Sandbox de Învățare

Ingineria prompturilor este în prezent mai mult o artă decât o știință. Cea mai bună modalitate de a ne îmbunătăți intuiția pentru aceasta este să _practicăm mai mult_ și să adoptăm o abordare de încercare și eroare care combină expertiza în domeniul aplicației cu tehnicile recomandate și optimizările specifice modelului.

Notebook-ul Jupyter care însoțește această lecție oferă un mediu _sandbox_ unde poți încerca ceea ce înveți - pe măsură ce avansezi sau ca parte a provocării de cod la final. Pentru a executa exercițiile, vei avea nevoie de:

1. **O cheie API Azure OpenAI** - punctul de serviciu pentru un LLM implementat.
2. **Un Runtime Python** - în care Notebook-ul poate fi executat.
3. **Variabile de Mediu Locale** - _completă acum pașii [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) pentru a te pregăti_.

Notebook-ul vine cu exerciții _de început_ - dar ești încurajat să adaugi propriile tale secțiuni de _Markdown_ (descriere) și _Cod_ (cereri de prompt) pentru a încerca mai multe exemple sau idei - și a-ți construi intuiția pentru designul prompturilor.

## Ghid Ilustrat

Vrei să obții o imagine de ansamblu a ceea ce acoperă această lecție înainte de a te aprofunda? Verifică acest ghid ilustrat, care îți oferă o idee despre principalele subiecte acoperite și concluziile cheie pentru a reflecta asupra fiecăruia. Harta lecției te duce de la înțelegerea conceptelor de bază și a provocărilor la abordarea lor cu tehnici și bune practici relevante de inginerie a prompturilor. Reține că secțiunea "Tehnici Avansate" din acest ghid se referă la conținutul acoperit în _capitolul următor_ al acestui curriculum.

## Startup-ul Nostru

Acum, să vorbim despre cum _acest subiect_ se leagă de misiunea noastră de startup de a [aduce inovația AI în educație](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Dorim să construim aplicații AI de _învățare personalizată_ - așa că să ne gândim cum ar putea diferiți utilizatori ai aplicației noastre să "proiecteze" prompturi:

- **Administratorii** ar putea cere AI să _analizeze datele curriculumului pentru a identifica lacunele în acoperire_. AI poate rezuma rezultatele sau le poate vizualiza cu cod.
- **Educații** ar putea cere AI să _genereze un plan de lecție pentru un public țintă și un subiect_. AI poate construi planul personalizat într-un format specificat.
- **Studenții** ar putea cere AI să _le ofere meditații într-un subiect dificil_. AI poate ghida acum studenții cu lecții, indicii și exemple adaptate nivelului lor.

Aceasta este doar vârful aisbergului. Verifică [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - o bibliotecă de prompturi open-source curată de experți în educație - pentru a obține o înțelegere mai largă a posibilităților! _Încearcă să rulezi unele dintre aceste prompturi în sandbox sau folosind OpenAI Playground pentru a vedea ce se întâmplă!_

## Ce este Ingineria Prompturilor?

Am început această lecție definind **Ingineria Prompturilor** ca procesul de _proiectare și optimizare_ a intrărilor text (prompturi) pentru a livra răspunsuri consistente și de calitate (completări) pentru un obiectiv de aplicație și model dat. Putem considera aceasta ca un proces în 2 pași:

- _proiectarea_ promptului inițial pentru un model și un obiectiv dat
- _rafinarea_ promptului iterativ pentru a îmbunătăți calitatea răspunsului

Aceasta este în mod necesar un proces de încercare și eroare care necesită intuiția și efortul utilizatorului pentru a obține rezultate optime. De ce este important? Pentru a răspunde la această întrebare, trebuie mai întâi să înțelegem trei concepte:

- _Tokenizarea_ = cum "vede" modelul promptul
- _LLM-uri de Bază_ = cum "procesează" modelul de bază un prompt
- _LLM-uri Ajustate prin Instrucțiuni_ = cum poate modelul să vadă acum "sarcini"

### Tokenizarea

Un LLM vede prompturile ca o _secvență de tokeni_ unde diferite modele (sau versiuni ale unui model) pot tokeniza același prompt în moduri diferite. Deoarece LLM-urile sunt antrenate pe tokeni (și nu pe text brut), modul în care prompturile sunt tokenizate are un impact direct asupra calității răspunsului generat.

Pentru a obține o intuiție despre cum funcționează tokenizarea, încearcă instrumente precum [Tokenizer-ul OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prezentat mai jos. Copiază-ți promptul - și vezi cum este transformat în tokeni, acordând atenție modului în care sunt tratate caracterele de spațiu și semnele de punctuație. Reține că acest exemplu arată un LLM mai vechi (GPT-3) - așa că încercarea cu un model mai nou poate produce un rezultat diferit.

### Concept: Modele de Bază

Odată ce un prompt este tokenizat, funcția principală a ["LLM-ului de Bază"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (sau model de bază) este să prezică tokenul din acea secvență. Deoarece LLM-urile sunt antrenate pe seturi de date masive de text, au o bună înțelegere a relațiilor statistice dintre tokeni și pot face acea predicție cu un anumit nivel de încredere. Reține că nu înțeleg _semnificația_ cuvintelor din prompt sau token; văd doar un model pe care îl pot "completa" cu următoarea lor predicție. Pot continua să prezică secvența până când este întreruptă de intervenția utilizatorului sau de o condiție prestabilită.

Vrei să vezi cum funcționează completarea bazată pe prompt? Introdu promptul de mai sus în [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) din Azure OpenAI Studio cu setările implicite. Sistemul este configurat să trateze prompturile ca cereri de informații - așa că ar trebui să vezi o completare care satisface acest context.

Dar ce se întâmplă dacă utilizatorul dorea să vadă ceva specific care să îndeplinească anumite criterii sau un obiectiv de sarcină? Aici intră în joc LLM-urile _ajustate prin instrucțiuni_.

### Concept: LLM-uri Ajustate prin Instrucțiuni

Un [LLM Ajustat prin Instrucțiuni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) începe cu modelul de bază și îl ajustează fin cu exemple sau perechi de intrare/ieșire (de exemplu, "mesaje" pe mai multe runde) care pot conține instrucțiuni clare - iar răspunsul AI încearcă să urmeze acea instrucțiune.

Acest lucru folosește tehnici precum Învățarea prin Recompensă cu Feedback Uman (RLHF) care pot antrena modelul să _urmeze instrucțiuni_ și să _învețe din feedback_ astfel încât să producă răspunsuri mai potrivite pentru aplicații practice și mai relevante pentru obiectivele utilizatorului.

Să încercăm - revizitează promptul de mai sus, dar acum schimbă _mesajul sistemului_ pentru a oferi următoarea instrucțiune ca context:

> _Rezumați conținutul pe care îl primiți pentru un elev de clasa a doua. Păstrați rezultatul la un paragraf cu 3-5 puncte._

Vezi cum rezultatul este acum ajustat pentru a reflecta scopul și formatul dorit? Un educator poate acum folosi direct acest răspuns în diapozitivele pentru acea clasă.

## De ce avem nevoie de Ingineria Prompturilor?

Acum că știm cum sunt procesate prompturile de către LLM-uri, să vorbim despre _de ce_ avem nevoie de ingineria prompturilor. Răspunsul constă în faptul că LLM-urile actuale prezintă o serie de provocări care fac _completările fiabile și consistente_ mai greu de realizat fără a depune eforturi în construcția și optimizarea prompturilor. De exemplu:

1. **Răspunsurile modelului sunt stochastice.** _Același prompt_ va produce probabil răspunsuri diferite cu modele sau versiuni de model diferite. Și poate produce chiar și rezultate diferite cu _același model_ la momente diferite. _Tehnicile de inginerie a prompturilor ne pot ajuta să minimizăm aceste variații prin oferirea unor ghidaje mai bune_.

1. **Modelele pot fabrica răspunsuri.** Modelele sunt pre-antrenate cu _seturi de date mari, dar finite_, ceea ce înseamnă că nu au cunoștințe despre concepte în afara acelui domeniu de antrenament. Drept urmare, pot produce completări care sunt inexacte, imaginare sau direct contradictorii cu faptele cunoscute. _Tehnicile de inginerie a prompturilor ajută utilizatorii să identifice și să atenueze astfel de fabricații, de exemplu, prin cererea de citări sau raționamente AI_.

1. **Capacitățile modelelor vor varia.** Modelele mai noi sau generațiile de modele vor avea capacități mai bogate, dar vor aduce și particularități unice și compromisuri în cost și complexitate. _Ingineria prompturilor ne poate ajuta să dezvoltăm bune practici și fluxuri de lucru care să abstractizeze diferențele și să se adapteze la cerințele specifice modelului în moduri scalabile și fără probleme_.

Să vedem acest lucru în acțiune în OpenAI sau Azure OpenAI Playground:

- Folosește același prompt cu diferite implementări LLM (de exemplu, OpenAI, Azure OpenAI, Hugging Face) - ai observat variațiile?
- Folosește același prompt în mod repetat cu aceeași implementare LLM (de exemplu, Azure OpenAI playground) - cum au diferit aceste variații?

### Exemplu de Fabricații

În acest curs, folosim termenul **"fabricație"** pentru a face referire la fenomenul în care LLM-urile generează uneori informații factually incorecte din cauza limitărilor în antrenamentul lor sau a altor constrângeri. Poate ai auzit de asemenea de acest lucru referit ca _"halucinații"_ în articole populare sau lucrări de cercetare. Cu toate acestea, recomandăm cu tărie utilizarea termenului _"fabricație"_ pentru a nu antropomorfiza accidental comportamentul atribuind o trăsătură umană unui rezultat generat de mașină. Acest lucru întărește, de asemenea, [ghidurile AI Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) din perspectiva terminologiei, eliminând termenii care pot fi considerați ofensatori sau neincluzivi în unele contexte.

Vrei să obții o idee despre cum funcționează fabricațiile? Gândește-te la un prompt care instruiește AI să genereze conținut pentru un subiect inexistent (pentru a te asigura că nu se găsește în setul de date de antrenament). De exemplu - am încercat acest prompt:

> **Prompt:** generează un plan de lecție despre Războiul Marțian din 2076.

O căutare pe web mi-a arătat că existau conturi fictive (de exemplu, seriale de televiziune sau cărți) despre războaie marțiene - dar niciunul în 2076. Bunul simț ne spune de asemenea că 2076 este _în viitor_ și, prin urmare, nu poate fi asociat cu un eveniment real.

Deci, ce se întâmplă când rulăm acest prompt cu diferiți furnizori LLM?

> **Răspuns 1**: OpenAI Playground (GPT-35)

> **Răspuns 2**: Azure OpenAI Playground (GPT-35)

> **Răspuns 3**: : Hugging Face Chat Playground (LLama-2)

Așa cum era de așteptat, fiecare model (sau versiune de model) produce răspunsuri ușor diferite datorită comportamentului stocastic și variațiilor de capacitate ale modelului. De exemplu, un model țintește un public de clasa a VIII-a, în timp ce altul presupune un elev de liceu. Dar toate cele trei modele au generat răspunsuri care ar putea convinge un utilizator neinformat că evenimentul era real.

Tehnici de inginerie a prompturilor precum _metaprompting_ și _configurarea temperaturii_ pot reduce fabricațiile modelului într-o anumită măsură. Noi _arhitecturi_ de inginerie a prompturilor încorporează de asemenea noi instrumente și tehnici în mod fluid în fluxul de prompturi, pentru a
Valoarea reală a șabloanelor constă în capacitatea de a crea și publica _biblioteci de prompturi_ pentru domenii de aplicație verticale - unde șablonul de prompt este acum _optimizat_ pentru a reflecta contextul sau exemplele specifice aplicației, ceea ce face ca răspunsurile să fie mai relevante și mai precise pentru publicul țintă. Repozitoriul [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) este un exemplu excelent al acestei abordări, curând o bibliotecă de prompturi pentru domeniul educației, cu accent pe obiective cheie precum planificarea lecțiilor, proiectarea curriculumului, tutoratul studenților etc.

## Conținut de Suport

Dacă ne gândim la construcția prompturilor ca având o instrucțiune (sarcină) și un țintă (conținut principal), atunci _conținutul secundar_ este ca un context suplimentar pe care îl oferim pentru a **influența într-un fel ieșirea**. Poate fi ajustarea parametrilor, instrucțiuni de formatare, taxonomii de subiecte etc., care pot ajuta modelul să _adapteze_ răspunsul său pentru a corespunde obiectivelor sau așteptărilor utilizatorului dorit.

De exemplu: Având un catalog de cursuri cu metadate extinse (nume, descriere, nivel, etichete de metadate, instructor etc.) pentru toate cursurile disponibile în curriculum:

- putem defini o instrucțiune pentru "a rezuma catalogul de cursuri pentru toamna 2023"
- putem folosi conținutul principal pentru a oferi câteva exemple de ieșire dorită
- putem folosi conținutul secundar pentru a identifica primele 5 "etichete" de interes.

Acum, modelul poate oferi un rezumat în formatul arătat de câteva exemple - dar dacă un rezultat are mai multe etichete, poate prioritiza cele 5 etichete identificate în conținutul secundar.

---

## Cele mai bune practici pentru Prompturi

Acum că știm cum pot fi _construite_ prompturile, putem începe să ne gândim cum să le _proiectăm_ pentru a reflecta cele mai bune practici. Putem gândi acest lucru în două părți - având mentalitatea corectă și aplicând tehnicile potrivite.

### Mentalitatea de Inginerie a Prompturilor

Ingineria Prompturilor este un proces de încercare și eroare, așa că țineți cont de trei factori generali de ghidare:

1. **Înțelegerea domeniului contează.** Acuratețea și relevanța răspunsului sunt o funcție a _domeniului_ în care acea aplicație sau utilizator operează. Aplicați intuiția și expertiza de domeniu pentru a **personaliza tehnicile** în continuare. De exemplu, definiți _personalități specifice domeniului_ în prompturile sistemului dumneavoastră sau folosiți _șabloane specifice domeniului_ în prompturile utilizatorului. Oferiți conținut secundar care reflectă contexte specifice domeniului sau folosiți _indicii și exemple specifice domeniului_ pentru a ghida modelul către tipare de utilizare familiare.

2. **Înțelegerea modelului contează.** Știm că modelele sunt stocastice prin natura lor. Dar implementările modelelor pot varia și în funcție de setul de date de antrenament pe care îl folosesc (cunoștințe pre-antrenate), capacitățile pe care le oferă (de exemplu, prin API sau SDK) și tipul de conținut pentru care sunt optimizate (de exemplu, cod vs. imagini vs. text). Înțelegeți punctele forte și limitările modelului pe care îl folosiți și folosiți acele cunoștințe pentru a _prioritiza sarcinile_ sau a construi _șabloane personalizate_ care sunt optimizate pentru capacitățile modelului.

3. **Iterația și validarea contează.** Modelele evoluează rapid, la fel și tehnicile pentru ingineria prompturilor. Ca expert în domeniu, este posibil să aveți alt context sau criterii pentru _aplicația dumneavoastră specifică_, care s-ar putea să nu se aplice comunității mai largi. Folosiți instrumente și tehnici de inginerie a prompturilor pentru a "porni" construcția prompturilor, apoi iterați și validați rezultatele folosindu-vă propria intuiție și expertiză de domeniu. Înregistrați-vă perspectivele și creați o **bază de cunoștințe** (de exemplu, biblioteci de prompturi) care poate fi folosită ca un nou punct de plecare de către alții, pentru iterații mai rapide în viitor.

## Cele mai bune practici

Acum să vedem practicile comune recomandate de practicienii [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) și [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ce                              | De ce                                                                                                                                                                                                                                               |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluați cele mai recente modele.       | Generațiile noi de modele sunt susceptibile să aibă caracteristici și calitate îmbunătățite - dar pot genera și costuri mai mari. Evaluați-le pentru impact, apoi luați decizii de migrare.                                                                                |
| Separați instrucțiunile și contextul   | Verificați dacă modelul/furnizorul dumneavoastră definește _delimitatori_ pentru a distinge instrucțiunile, conținutul principal și cel secundar mai clar. Acest lucru poate ajuta modelele să aloce greutăți mai precis la tokenuri.                                                         |
| Fiți specific și clar             | Oferiți mai multe detalii despre contextul dorit, rezultatul, lungimea, formatul, stilul etc. Acest lucru va îmbunătăți atât calitatea cât și consistența răspunsurilor. Capturați rețete în șabloane reutilizabile.                                                          |
| Fiți descriptiv, folosiți exemple      | Modelele pot răspunde mai bine la o abordare de tip "arată și spune". Începeți cu un `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valori. Reveniți la [Secțiunea Sandbox de Învățare](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) pentru a învăța cum.

### În continuare, deschideți Jupyter Notebook

- Selectați nucleul de execuție. Dacă folosiți opțiunile 1 sau 2, selectați pur și simplu nucleul implicit Python 3.10.x furnizat de containerul de dezvoltare.

Sunteți gata să rulați exercițiile. Rețineți că nu există _răspunsuri corecte și greșite_ aici - doar explorând opțiunile prin încercare și eroare și construind intuiția pentru ceea ce funcționează pentru un model și un domeniu de aplicație dat.

_Din acest motiv, nu există segmente de Soluții de Cod în această lecție. În schimb, Notebook-ul va avea celule Markdown intitulate "Soluția mea:" care arată un exemplu de ieșire pentru referință._

## Verificarea cunoștințelor

Care dintre următoarele este un prompt bun, urmând câteva practici de bază rezonabile?

1. Arată-mi o imagine cu o mașină roșie
2. Arată-mi o imagine cu o mașină roșie de marcă Volvo și model XC90 parcată lângă o stâncă cu soarele la apus
3. Arată-mi o imagine cu o mașină roșie de marcă Volvo și model XC90

A: 2, este cel mai bun prompt deoarece oferă detalii despre "ce" și intră în specificații (nu doar orice mașină, ci o marcă și un model specific) și, de asemenea, descrie setarea generală. 3 este următorul cel mai bun, deoarece conține și o mulțime de descrieri.

## 🚀 Provocare

Vezi dacă poți valorifica tehnica "indiciului" cu promptul: Completează propoziția "Arată-mi o imagine cu o mașină roșie de marcă Volvo și ". Cu ce răspunde și cum ai îmbunătăți-o?

## Muncă excelentă! Continuă să înveți

Vrei să înveți mai multe despre diferite concepte de Inginerie a Prompturilor? Accesează [pagina de învățare continuă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a găsi alte resurse excelente pe acest subiect.

Mergi la Lecția 5 unde vom analiza [tehnici avansate de prompturi](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană profesională. Nu suntem responsabili pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.