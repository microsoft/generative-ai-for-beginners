# Fundamentele Ingineriei Prompturilor

[![Fundamentele Ingineriei Prompturilor](../../../translated_images/ro/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introducere
Acest modul acoperă conceptele și tehnicile esențiale pentru crearea prompturilor eficiente în modelele generative de AI. Modul în care scrieți promptul către un LLM contează de asemenea. Un prompt creat cu grijă poate obține un răspuns de calitate superioară. Dar ce înseamnă exact termeni ca _prompt_ și _ingineria prompturilor_? Și cum îmbunătățesc promptul _input_ pe care îl trimit către LLM? Acestea sunt întrebările la care vom încerca să răspundem în acest capitol și în următorul.

_AI generativ_ este capabilă să creeze conținut nou (de exemplu, text, imagini, sunet, cod etc.) ca răspuns la cererile utilizatorilor. Acest lucru este realizat folosind _Modele Mari de Limbaj_ precum seria GPT ("Generative Pre-trained Transformer") de la OpenAI, care sunt antrenate să utilizeze limbaj natural și cod.

Utilizatorii pot interacționa acum cu aceste modele folosind paradigme familiare, cum ar fi chat-ul, fără a avea nevoie de expertiză tehnică sau instruire. Modelele sunt _bazate pe prompturi_ – utilizatorii trimit un text (prompt) și primesc răspunsul AI (completarea). Apoi pot „discuta cu AI” iterativ, în conversații în mai multe tururi, rafinând promptul până când răspunsul corespunde așteptărilor lor.

„Prompturile” devin acum interfața principală de _programare_ pentru aplicațiile AI generative, indicând modelelor ce să facă și influențând calitatea răspunsurilor returnate. „Ingineria Prompturilor” este un domeniu în rapidă creștere care se concentrează pe _proiectarea și optimizarea_ prompturilor pentru a livra răspunsuri coerente și de calitate la scară.

## Obiective de Învățare

În această lecție învățăm ce este Ingineria Prompturilor, de ce este importantă și cum putem crea prompturi mai eficiente pentru un model și un scop aplicațional dat. Vom înțelege conceptele de bază și cele mai bune practici pentru ingineria prompturilor – și vom învăța despre un mediu interactiv de tip Jupyter Notebooks „sandbox” unde putem vedea aceste concepte aplicate în exemple reale.

La finalul acestei lecții vom putea:

1. Explica ce este ingineria prompturilor și de ce este importantă.
2. Descrie componentele unui prompt și cum sunt folosite.
3. Înțelege cele mai bune practici și tehnici de inginerie a prompturilor.
4. Aplica tehnicile învățate în exemple reale, folosind un endpoint OpenAI.

## Termeni Cheie

Ingineria Prompturilor: Practica proiectării și rafinării inputurilor pentru a ghida modelele AI să producă rezultatele dorite.
Tokenizare: Procesul de conversie a textului în unități mai mici, numite tokenuri, pe care un model le poate înțelege și procesa.
LLM-uri Tuned pe Instrucțiuni: Modele Mari de Limbaj (LLM-uri) care au fost ajustate fin cu instrucțiuni specifice pentru a îmbunătăți acuratețea și relevanța răspunsurilor.

## Mediu de Învățare Sandbox

Ingineria prompturilor este în prezent mai mult o artă decât o știință. Cea mai bună metodă de a ne îmbunătăți intuiția este să _exersăm mai mult_ și să adoptăm o abordare de tip încercare și eroare care combină expertiza în domeniul aplicației cu tehnicile recomandate și optimizările specifice modelului.

Jupyter Notebook-ul care însoțește această lecție oferă un mediu _sandbox_ în care poți încerca ceea ce înveți – pe măsură ce avansezi sau ca parte a provocării cu cod la final. Pentru a executa exercițiile, vei avea nevoie de:

1. **O cheie API Azure OpenAI** - endpoint-ul serviciului pentru un LLM implementat.
2. **Un Runtime Python** - în care poate fi executat Notebook-ul.
3. **Variabile locale de mediu** - _completează pașii din [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) pentru a fi pregătit_.

Notebook-ul oferă exerciții _starter_ - dar ești încurajat să adaugi propriile secțiuni de _Markdown_ (descriere) și _Cod_ (cereri de prompturi) pentru a încerca și alte exemple sau idei – și să-ți construiești intuiția pentru proiectarea prompturilor.

## Ghid Ilustrat

Vrei să ai o imagine de ansamblu a ceea ce acoperă această lecție înainte să te arunci în detalii? Aruncă o privire peste acest ghid ilustrat, care îți oferă o idee asupra principalelor subiecte abordate și asupra concluziilor cheie pentru a le reflecta în fiecare dintre ele. Parcursul lecției te duce de la înțelegerea conceptelor și provocărilor de bază până la abordarea lor cu tehnici relevante de inginerie a prompturilor și bune practici. Observă că secțiunea „Tehnici Avansate” din acest ghid se referă la conținutul acoperit în capitolul următor al acestui curriculum.

![Ghid Ilustrat pentru Ingineria Prompturilor](../../../translated_images/ro/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startup-ul Nostru

Acum, să discutăm cum _acest subiect_ se leagă de misiunea startup-ului nostru de a [aduce inovația AI în educație](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Dorim să construim aplicații AI pentru _învățare personalizată_ – deci să ne gândim cum diferiți utilizatori ai aplicației noastre ar putea „proiecta” prompturi:

- **Administratorii** ar putea cere AI-ului să _analizeze datele din curriculum pentru a identifica goluri în acoperire_. AI poate sumariza rezultatele sau le poate vizualiza cu cod.
- **Educatorii** ar putea cere AI-ului să _genereze un plan de lecție pentru un public țintă și un subiect_. AI poate construi planul personalizat într-un format specificat.
- **Elevii** ar putea cere AI-ului să _le fie tutor într-un subiect dificil_. AI poate ghida acum elevii cu lecții, sugestii și exemple adaptate nivelului lor.

Aceasta este doar vârful aisbergului. Verifică [Prompturi Pentru Educație](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – o bibliotecă open-source de prompturi curată de experți în educație – pentru a vedea o perspectivă mai largă a posibilităților! _Încearcă să execuți unele dintre aceste prompturi în sandbox sau folosind OpenAI Playground pentru a vedea ce se întâmplă!_

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să acopere conceptul de bază #1.
Consolidarea conceptului cu exemple și referințe.

CONCEPT #1:
Ingineria Prompturilor.
Definirea lui și explicarea motivului pentru care este necesar.
-->

## Ce este Ingineria Prompturilor?

Am început această lecție definind **Ingineria Prompturilor** ca procesul de _proiectare și optimizare_ a inputurilor textuale (prompturi) pentru a livra răspunsuri coerente și de calitate (completări) pentru un scop aplicațional și model dat. Putem vedea acest proces în două etape:

- _proiectarea_ promptului inițial pentru un model și scop dat
- _rafinarea_ promptului iterativ pentru a îmbunătăți calitatea răspunsului

Acesta este neapărat un proces de încercare și eroare care necesită intuiție și efort din partea utilizatorului pentru a obține rezultate optime. Deci, de ce este important? Pentru a răspunde, trebuie mai întâi să înțelegem trei concepte:

- _Tokenizarea_ = cum „vede” modelul promptul
- _LLM-urile de bază_ = cum „procesează” modelul fundația promptul
- _LLM-urile Tuned pe Instrucțiuni_ = cum modelul poate acum „vedea sarcini”

### Tokenizarea

Un LLM vede prompturile ca o _secvență de tokenuri_ unde diferite modele (sau versiuni ale unui model) pot tokeniza același prompt în moduri diferite. Deoarece LLM-urile sunt antrenate pe tokenuri (și nu pe text brut), modul în care prompturile sunt tokenizate are un impact direct asupra calității răspunsului generat.

Pentru a înțelege cum funcționează tokenizarea, încearcă unelte precum [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prezentate mai jos. Copiază promptul tău – și vezi cum este convertit în tokenuri, acordând atenție modului în care sunt gestionate spațiile și semnele de punctuație. Reține că acest exemplu arată un LLM mai vechi (GPT-3) – deci încercarea cu un model mai nou poate produce un rezultat diferit.

![Tokenizare](../../../translated_images/ro/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concept: Modele Fundație

Odată ce un prompt este tokenizat, funcția principală a ["LLM-ului de bază"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (sau modelului fundație) este să prezică tokenul următor din acea secvență. Deoarece LLM-urile sunt antrenate pe seturi mari de date textuale, ele au o bună înțelegere a relațiilor statistice între tokenuri și pot face această predicție cu oarecare încredere. Reține că ele nu înțeleg _sensul_ cuvintelor din prompt sau token; văd doar un tipar pe care îl pot „completa” cu următoarea predicție. Pot continua să prezică secvența până când este oprită prin intervenția utilizatorului sau o condiție predefinită.

Vrei să vezi cum funcționează completarea pe bază de prompt? Introdu promptul de mai sus în [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) cu setările implicite. Sistemul este configurat să trateze prompturile ca cereri de informații – deci ar trebui să vezi o completare care satisface acest context.

Dar ce faci dacă utilizatorul dorește să vadă ceva specific care îndeplinește anumite criterii sau obiective ale sarcinii? Aici intră în scenă LLM-urile _tuned pe instrucțiuni_.

![Completare chat LLM de bază](../../../translated_images/ro/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concept: LLM-uri Tuned pe Instrucțiuni

Un [LLM Tuned pe Instrucțiuni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) pornește de la modelul fundație și îl ajustează fin cu exemple sau perechi input/output (de exemplu, „mesaje” în mai multe runde) care pot conține instrucțiuni clare – iar răspunsul AI încearcă să urmeze acea instrucțiune.

Aceasta folosește tehnici precum Învățarea cu Recompensă bazată pe Feedback Uman (RLHF) care pot antrena modelul să _urmeze instrucțiuni_ și să _învețe din feedback_, astfel încât să producă răspunsuri mai potrivite aplicațiilor practice și mai relevante pentru obiectivele utilizatorului.

Să încercăm – revizuiește promptul de mai sus, dar acum schimbă _mesajul sistem_ pentru a oferi următoarea instrucțiune ca context:

> _Rezuma conținutul care ți-a fost oferit pentru un elev de clasa a doua. Păstrează rezultatul într-un paragraf cu 3-5 puncte cheie._

Vezi cum rezultatul este acum ajustat să reflecte scopul și formatul dorit? Un educator poate folosi acum direct acest răspuns în diapozitivele pentru acea clasă.

![Completare chat LLM Tuned pe Instrucțiuni](../../../translated_images/ro/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## De ce avem nevoie de Ingineria Prompturilor?

Acum că știm cum sunt procesate prompturile de către LLM-uri, să discutăm despre _de ce_ avem nevoie de ingineria prompturilor. Răspunsul constă în faptul că LLM-urile actuale prezintă o serie de provocări care fac _finalizările de încredere și constante_ mai greu de realizat fără efort în construirea și optimizarea prompturilor. De exemplu:

1. **Răspunsurile modelelor sunt stocastice.** _Același prompt_ va produce probabil răspunsuri diferite cu modele diferite sau versiuni diferite ale aceluiași model. Și poate produce răspunsuri diferite chiar cu _același model_ în momente diferite. _Tehnicile de inginerie a prompturilor ne pot ajuta să minimizăm aceste variații oferind limitări mai bune_.

1. **Modelele pot fabrica răspunsuri.** Modelele sunt pre-antrenate cu seturi de date _mari dar finite_, ceea ce înseamnă că nu cunosc concepte din afara acestui domeniu de antrenament. Ca urmare, ele pot produce completări inexacte, imaginare sau chiar contradictorii cu faptele cunoscute. _Tehnicile de inginerie a prompturilor ajută utilizatorii să identifice și să atenueze astfel de fabricații, de exemplu, cerând AI-ului citări sau raționamente_.

1. **Capabilitățile modelelor variază.** Modelele noi sau generațiile noi de modele vor avea capabilități mai bogate, dar și particularități unice și compromisuri în cost și complexitate. _Ingineria prompturilor ne poate ajuta să dezvoltăm bune practici și fluxuri de lucru care abstractizează diferențele și se adaptează cerințelor specifice ale modelului în mod scalabil și fără întreruperi_.

Să vedem acest lucru în acțiune în OpenAI sau Azure OpenAI Playground:

- Folosește același prompt cu implementări diferite de LLM-uri (ex., OpenAI, Azure OpenAI, Hugging Face) - ai observat variațiile?
- Folosește același prompt repetat cu _aceeași_ implementare LLM (ex., playground Azure OpenAI) - cum au diferit aceste variații?

### Exemplu de fabricații

În acest curs folosim termenul **„fabricație”** pentru a face referire la fenomenul în care LLM-urile uneori generează informații factual incorecte din cauza limitărilor antrenamentului sau a altor constrângeri. Poate ai auzit acest fenomen denumit _„halucinații”_ în articole populare sau lucrări de cercetare. Totuși, recomandăm insistent folosirea termenului _„fabricație”_ pentru a nu antropomorfiza accidental comportamentul, atribuind o trăsătură umană unui rezultat generat de mașină. Aceasta întărește și [ghidurile AI Responsabil](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) din perspectivă terminologică, eliminând termeni care pot fi considerați ofensatori sau neincluzivi în anumite contexte.

Vrei să înțelegi cum funcționează fabricațiile? Gândește-te la un prompt care îi spune AI-ului să genereze conținut pentru un subiect inexistent (pentru a te asigura că nu se găsește în setul de date de antrenament). De exemplu – am încercat acest prompt:

> **Prompt:** generează un plan de lecție despre Războiul Marțian din 2076.

O căutare pe web mi-a arătat că există relatări fictive (de exemplu, seriale TV sau cărți) despre războaie marțiene – dar niciuna din 2076. Simțul comun ne spune că anul 2076 este _în viitor_ și, prin urmare, nu poate fi asociat cu un eveniment real.


Deci ce se întâmplă când rulăm acest prompt cu diferiți furnizori LLM?

> **Răspuns 1**: OpenAI Playground (GPT-35)

![Răspuns 1](../../../translated_images/ro/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Răspuns 2**: Azure OpenAI Playground (GPT-35)

![Răspuns 2](../../../translated_images/ro/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Răspuns 3**: : Hugging Face Chat Playground (LLama-2)

![Răspuns 3](../../../translated_images/ro/04-fabrication-huggingchat.faf82a0a51278956.webp)

După cum era de așteptat, fiecare model (sau versiune a modelului) produce răspunsuri ușor diferite datorită comportamentului aleatoriu și variațiilor în capacitățile modelului. De exemplu, un model se adresează unui public de clasa a 8-a, în timp ce celălalt presupune un elev de liceu. Dar toate cele trei modele au generat răspunsuri care ar putea convinge un utilizator neinformat că evenimentul a fost real.

Tehnicile de inginerie a promptului precum _metaprompting_ și _configurarea temperaturii_ pot reduce fabricările modelelor până la un anumit punct. Noi _arhitecturi_ de inginerie a promptului încorporează, de asemenea, fără probleme noi instrumente și tehnici în fluxul promptului, pentru a atenua sau reduce unele dintre aceste efecte.

## Studiu de caz: GitHub Copilot

Să încheiem această secțiune obținând o idee despre cum este folosită ingineria promptului în soluții reale, uitându-ne la un Studiu de Caz: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot este „Programatorul tău AI în pereche” - convertește prompturi text în completări de cod și este integrat în mediul tău de dezvoltare (de exemplu, Visual Studio Code) pentru o experiență utilizator fluidă. Așa cum este documentat în seria de bloguri de mai jos, cea mai timpurie versiune a fost bazată pe modelul OpenAI Codex - cu inginerii realizând rapid necesitatea finețării modelului și dezvoltării unor tehnici mai bune de inginerie a promptului, pentru a îmbunătăți calitatea codului. În iulie, au [lansat un model AI îmbunătățit care merge dincolo de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pentru sugestii și mai rapide.

Citește postările în ordine, pentru a urmări călătoria lor de învățare.

- **Mai 2023** | [GitHub Copilot devine mai bun la înțelegerea codului tău](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [În interiorul GitHub: Lucrul cu LLM-urile din spatele GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Iun 2023** | [Cum să scrii prompturi mai bune pentru GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Iul 2023** | [.. GitHub Copilot merge dincolo de Codex cu model AI îmbunătățit](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Iul 2023** | [Ghidul unui dezvoltator pentru ingineria promptului și LLM-uri](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cum să construiești o aplicație enterprise LLM: Lecții de la GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Poți răsfoi și [blogul lor de inginerie](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pentru mai multe postări precum [aceasta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) care arată cum aceste modele și tehnici sunt _aplicate_ pentru a conduce aplicații reale.

---

<!--
ȘABLON DE LECȚIE:
Această unitate ar trebui să acopere conceptul de bază #2.
Întărește conceptul cu exemple și referințe.

CONCEPT #2:
Proiectarea promptului.
Ilustrat cu exemple.
-->

## Construcția promptului

Am văzut de ce este importantă ingineria promptului - acum să înțelegem cum sunt _construite_ prompturile pentru a putea evalua diferite tehnici pentru un design mai eficient al promptului.

### Prompt de bază

Să începem cu promptul de bază: o intrare text trimisă modelului fără alt context. Iată un exemplu - când trimitem primele câteva cuvinte ale imnului național al SUA către OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), acesta _completează_ instantaneu răspunsul cu următoarele câteva versuri, ilustrând comportamentul de bază al predicției.

| Prompt (Intrare)     | Completare (Ieșire)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Se pare că începi versurile la „The Star-Spangled Banner”, imnul național al Statelor Unite. Versurile complete sunt ... |

### Prompt complex

Acum să adăugăm context și instrucțiuni la acel prompt de bază. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ne permite să construim un prompt complex ca o colecție de _mesaje_ cu:

- Perechi intrare/ieșire reflectând input-ul _utilizatorului_ și răspunsul _asistentului_.
- Mesajul sistem care setează contextul comportamentului sau personalității asistentului.

Cererea este acum în forma de mai jos, unde _tokenizarea_ capturează eficient informațiile relevante din context și conversație. Modificarea contextului sistemului poate avea un impact la fel de mare asupra calității completărilor ca și input-urile utilizatorului furnizate.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt cu instrucțiuni

În exemplele de mai sus, promptul utilizatorului a fost o interogare simplă text care poate fi interpretată ca o cerere de informații. Cu prompturile de _instrucțiuni_, putem folosi acel text pentru a specifica o sarcină mai detaliat, oferind o îndrumare mai bună AI-ului. Iată un exemplu:

| Prompt (Intrare)                                                                                                                                                                                                                         | Completare (Ieșire)                                                                                                        | Tipul instrucțiunii |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Scrie o descriere a Războiului Civil                                                                                                                                                                                                   | _a returnat un paragraf simplu_                                                                                              | Simplu              |
| Scrie o descriere a Războiului Civil. Oferă date și evenimente cheie și descrie semnificația lor                                                                                                                                         | _a returnat un paragraf urmat de o listă de date cheie ale evenimentelor cu descrieri_                                             | Complex             |
| Scrie o descriere a Războiului Civil în 1 paragraf. Oferă 3 puncte cu date cheie și semnificația lor. Oferă încă 3 puncte cu figuri istorice cheie și contribuțiile lor. Returnează ieșirea ca un fișier JSON | _returnează detalii mai ample într-o casetă de text, formatată ca JSON pe care o poți copia-lipi într-un fișier și valida cum este necesar_ | Complex. Formatat.  |

## Conținut primar

În exemplele de mai sus, promptul era încă destul de deschis, permițând LLM-ului să decidă ce parte a setului de date pre-antrenat este relevantă. Cu modelul de design _conținut primar_, textul de intrare este împărțit în două părți:

- o instrucțiune (acțiune)
- conținut relevant (care influențează acțiunea)

Iată un exemplu unde instrucțiunea este „rezumă asta în 2 propoziții”.

| Prompt (Intrare)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completare (Ieșire)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este o gigantă gazoasă cu o masă o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât a tuturor planetelor din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscută de civilizațiile antice încă dinainte de istoria înregistrată. Este numită după zeul roman Jupiter.[19] Văzută de pe Pământ, Jupiter poate fi suficient de strălucitoare pentru ca lumina reflectată să arunce umbre vizibile,[20] și este, în medie, al treilea cel mai strălucitor obiect natural pe cerul nopții după Lună și Venus. <br/> **Rezumați asta în 2 propoziții scurte** | Jupiter, a cincea planetă de la Soare, este cea mai mare din Sistemul Solar și este cunoscută pentru a fi unul dintre cele mai luminoase obiecte de pe cerul nopții. Numele provine de la zeul roman Jupiter, fiind o gigantă gazoasă care are o masă de două ori și jumătate mai mare decât a tuturor celorlalte planete din Sistemul Solar la un loc. |

Segmentul de conținut primar poate fi folosit în diverse moduri pentru a genera instrucțiuni mai eficiente:

- **Exemple** - în loc să spui modelului ce să facă cu o instrucțiune explicită, oferă-i exemple de ce să facă și lasă-l să deducă modelul.
- **Indiciu** - urmează instrucțiunea cu un „indiciu” care pregătește completarea, ghidând modelul spre răspunsuri mai relevante.
- **Șabloane** - acestea sunt „rețete” repetitive pentru prompturi cu spații rezervate (variabile) care pot fi personalizate cu date pentru cazuri de utilizare specifice.

Să explorăm acestea în practică.

### Folosind exemple

Aceasta este o abordare unde folosești conținutul primar pentru a „hrăni modelul” cu câteva exemple de ieșire dorită pentru o instrucțiune dată și îl lași să deducă modelul pentru ieșirea dorită. În funcție de numărul de exemple oferite, putem avea prompting zero-shot, prompting one-shot, few-shot prompting etc.

Promptul constă acum în trei componente:

- O descriere a sarcinii
- Câteva exemple de ieșire dorită
- Începutul unui nou exemplu (care devine o descriere implicită a sarcinii)

| Tip de învățare | Prompt (Intrare)                                                                                                                                        | Completare (Ieșire)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Tradu în spaniolă                                                                                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Jucătorul a alergat pe baze => Baseball <br/> Jucătorul a dat un as => Tenis <br/> Jucătorul a dat șase => Cricket <br/> Jucătorul a făcut un slam-dunk => | Baschet                    |
|               |                                                                                                                                                       |                             |

Observă cum a trebuit să furnizăm instrucțiune explicită („Tradu în spaniolă”) la prompting zero-shot, dar aceasta este dedusă în exemplul one-shot prompting. Exemplul few-shot arată că adăugarea mai multor exemple permite modelelor să facă deducții mai precise fără instrucțiuni suplimentare.

### Indiciu la prompt

O altă tehnică pentru folosirea conținutului primar este să oferi _indiciu_ în loc de exemple. În acest caz, dăm modelului un impuls corect prin _începerea_ cu un fragment care reflectă formatul dorit al răspunsului. Modelul „primește indiciul” și continuă în aceeași direcție.

| Numărul indiciilor | Prompt (Intrare)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completare (Ieșire)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este o gigantă gazoasă cu o masă o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât a tuturor planetelor din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscută de civilizațiile antice încă dinainte de istoria înregistrată. <br/>**Rezumați asta**                                       | Jupiter este cea mai mare planetă din Sistemul nostru Solar și a cincea de la Soare. Este o gigantă gazoasă cu o masă de 1/1000 din cea a Soarelui, dar mai grea decât toate celelalte planete împreună. Civilizațiile antice au cunoscut mult timp despre Jupiter, iar aceasta este ușor vizibilă pe cerul nopții.. |
| 1              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este o gigantă gazoasă cu o masă o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât a tuturor planetelor din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscută de civilizațiile antice încă dinainte de istoria înregistrată. <br/>**Rezumați asta** <br/> Ce am învățat este că Jupiter | este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este o gigantă gazoasă cu o masă o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât a tuturor planetelor la un loc. Este ușor vizibil cu ochiul liber și este cunoscut încă din antichitate.                        |

| 2              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o miime din cea a Soarelui, dar de două ori și jumătate mai mare decât cea a tuturor celorlalte planete din Sistemul Solar combinate. Jupiter este unul dintre cele mai luminoase obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscut de civilizațiile antice încă dinainte de istoria consemnată. <br/>**Rezumatul** <br/> Primele 3 fapte pe care le-am învățat:         | 1. Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. <br/> 2. Este un gigant gazos cu o masă de o miime din cea a Soarelui...<br/> 3. Jupiter a fost vizibil cu ochiul liber încă din antichitate ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Șabloane de prompturi

Un șablon de prompt este o _rețetă predefinită pentru un prompt_ care poate fi stocată și reutilizată după nevoie, pentru a genera experiențe mai coerente pentru utilizatori la scară largă. În forma sa cea mai simplă, este pur și simplu o colecție de exemple de prompturi cum este [acest exemplu de la OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) care oferă atât componentele interactive ale promptului (mesaje pentru utilizator și sistem) cât și formatul cererii API - pentru a susține reutilizarea.

În forma sa mai complexă, cum este [acest exemplu de la LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), conține _locuri rezervate_ care pot fi înlocuite cu date dintr-o varietate de surse (input de la utilizator, context de sistem, surse de date externe etc.) pentru a genera un prompt în mod dinamic. Aceasta ne permite să creăm o bibliotecă de prompturi reutilizabile care pot fi folosite pentru a genera experiențe consistente pentru utilizatori **programatic** la scară mare.

În final, valoarea reală a șabloanelor constă în capacitatea de a crea și publica _biblioteci de prompturi_ pentru domenii verticale de aplicație - unde șablonul de prompt este acum _optimizat_ pentru a reflecta contextul specific aplicației sau exemplele care fac răspunsurile mai relevante și precise pentru publicul țintă. Repozitoriul [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) este un exemplu excelent de această abordare, curând o bibliotecă de prompturi pentru domeniul educației cu accent pe obiective cheie precum planificarea lecțiilor, proiectarea curriculumului, tutoring pentru studenți etc.

## Conținut de suport

Dacă ne gândim la construcția unui prompt ca având o instrucțiune (sarcină) și un țintă (conținut primar), atunci _conținutul secundar_ este ca un context suplimentar pe care îl oferim pentru a **influența răspunsul într-un fel**. Acesta poate fi parametri de reglare, instrucțiuni de formatare, taxonomii tematice etc. care pot ajuta modelul să _personalizeze_ răspunsul pentru a se potrivi obiectivelor sau așteptărilor utilizatorului dorite.

De exemplu: Având un catalog de cursuri cu metadate extinse (nume, descriere, nivel, etichete metadate, instructor etc.) pentru toate cursurile disponibile din curriculum:

- putem defini o instrucțiune pentru „a rezuma catalogul de cursuri pentru toamna 2023”
- putem folosi conținutul primar pentru a oferi câteva exemple de rezultat dorit
- putem folosi conținutul secundar pentru a identifica primele 5 „etichete” de interes.

Acum, modelul poate oferi un rezumat în formatul indicat de acele câteva exemple - dar dacă un rezultat are mai multe etichete, poate prioritiza cele 5 etichete identificate în conținutul secundar.

---

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să acopere conceptul de bază #1.
Consolidarea conceptului cu exemple și referințe.

CONCEPTUL #3:
Tehnici de inginerie a promptului.
Care sunt câteva tehnici de bază pentru ingineria promptului?
Ilustrează-le cu câteva exerciții.
-->

## Cele mai bune practici pentru prompturi

Acum că știm cum pot fi _construite_ prompturile, putem începe să ne gândim cum să le _proiectăm_ pentru a reflecta cele mai bune practici. Putem gândi acest lucru în două părți - având mentalitatea potrivită și aplicând tehnicile potrivite.

### Mentalitatea pentru ingineria promptului

Ingineria promptului este un proces de încercare și eroare, așa că ține cont de trei factori generali călăuzitori:

1. **Înțelegerea domeniului contează.** Acuratețea și relevanța răspunsului este o funcție a _domeniului_ în care aplicația sau utilizatorul operează. Aplică-ți intuiția și expertiza domeniului pentru a **personaliza tehnicile**. De exemplu, definește _personalități specifice domeniului_ în prompturile de sistem sau folosește _șabloane specifice domeniului_ în prompturile pentru utilizator. Oferă conținut secundar care reflectă contexte specifice domeniului sau folosește _indici și exemple specifice domeniului_ pentru a ghida modelul către tiparele de utilizare familiare.

2. **Înțelegerea modelului contează.** Știm că modelele sunt, prin natura lor, stocastice. Dar implementările modelelor pot varia și în funcție de setul de date de instruire folosit (cunoștințele pre-antrenate), capabilitățile oferite (de exemplu, prin API sau SDK) și tipul de conținut pentru care sunt optimizate (de exemplu, cod vs imagini vs text). Înțelege punctele forte și limitările modelului pe care îl folosești și utilizează această cunoaștere pentru a _prioritiza sarcinile_ sau a construi _șabloane personalizate_ care sunt optimizate pentru capabilitățile modelului.

3. **Iterația și validarea contează.** Modelele evoluează rapid, la fel și tehnicile pentru ingineria promptului. Ca expert în domeniu, s-ar putea să ai un context sau criterii specifice aplicației tale care să nu se aplice comunității largi. Folosește uneltele și tehnicile de inginerie a promptului pentru a „porni construcția promptului”, apoi iterează și validează rezultatele folosindu-ți propria intuiție și expertiză în domeniu. Înregistrează-ți descoperirile și creează o **bază de cunoștințe** (de exemplu, biblioteci de prompturi) care poate fi folosită ca o nouă bază de referință de către alții, pentru iterări mai rapide în viitor.

## Cele mai bune practici

Acum să vedem cele mai comune bune practici recomandate de practicienii [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) și [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ce                              | De ce                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluează cele mai noi modele     | Noile generații de modele probabil că au caracteristici și calitate îmbunătățite - dar pot genera și costuri mai mari. Evaluează-le pentru impact, apoi ia decizii pentru migrare.                                                                   |
| Separă instrucțiunile și contextul| Verifică dacă modelul/tău furnizorul definește _delimitatori_ pentru a distinge mai clar instrucțiunile, conținutul primar și cel secundar. Aceasta poate ajuta modelele să aloce greutăți mai corecte tokenilor.                                     |
| Fii specific și clar             | Oferă mai multe detalii despre contextul dorit, rezultat, lungime, format, stil etc. Aceasta va îmbunătăți atât calitatea, cât și consistența răspunsurilor. Capturează rețetele în șabloane reutilizabile.                                           |
| Fii descriptiv, folosește exemple | Modelele pot răspunde mai bine la o abordare „arată și spune”. Începe cu un mod `zero-shot` în care îi dai o instrucțiune (dar fără exemple), apoi încearcă `few-shot` ca rafinare, oferind câteva exemple ale rezultatului dorit. Folosește analogii.  |
| Folosește semnale pentru a începe completările | Îndrumă-l către un rezultat dorit oferindu-i niște cuvinte sau fraze inițiale pe care le poate folosi ca punct de pornire pentru răspuns.                                                                                                         |
| Repetă                          | Uneori e nevoie să te repeți pentru model. Dă instrucțiuni înainte și după conținutul principal, folosește o instrucțiune și un indiciu, etc. Iterează și validează ca să vezi ce funcționează.                                                     |
| Ordinea contează                | Ordinea în care prezinți informația modelului poate influența rezultatul, chiar și în exemplele de învățare, din cauza bias-ului de recență. Încearcă opțiuni diferite pentru a vedea ce funcționează cel mai bine.                                  |
| Oferă modelului o „ieșire de siguranță” | Oferă modelului un răspuns de completare de rezervă pe care să îl poată furniza dacă nu poate finaliza sarcina din orice motiv. Aceasta poate reduce șansele ca modelele să genereze răspunsuri false sau fabricate.                                  |
|                                   |                                                                                                                                                                                                                                                   |

Ca în cazul oricărei bune practici, amintește-ți că _experiența ta poate varia_ în funcție de model, sarcină și domeniu. Folosește-le ca punct de plecare și iterează pentru a găsi ce funcționează cel mai bine pentru tine. Reevaluează constant procesul de inginerie al prompturilor pe măsură ce apar modele și unelte noi, concentrându-te pe scalabilitatea procesului și calitatea răspunsurilor.

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să ofere o provocare de cod dacă este cazul

PROVOCARE:
Link către un Jupyter Notebook cu numai comentariile codului în instrucțiuni (secțiunile de cod sunt goale).

SOLUȚIE:
Link către o copie a acelui Notebook cu prompturile completate și rulate, arătând cum ar putea arăta un exemplu.
-->

## Sarcina

Felicitări! Ai ajuns la finalul lecției! Este timpul să pui la încercare câteva dintre conceptele și tehnicile învățate cu exemple reale!

Pentru sarcina noastră, vom folosi un Jupyter Notebook cu exerciții pe care le poți completa interactiv. De asemenea, poți extinde Notebook-ul cu propriile celule Markdown și Code pentru a explora idei și tehnici pe cont propriu.

### Pentru a începe, fă fork la repo, apoi

- (Recomandat) Pornește GitHub Codespaces
- (Alternativ) Clonează repo-ul pe dispozitivul tău local și folosește-l cu Docker Desktop
- (Alternativ) Deschide Notebook-ul cu mediul tău de rulare preferat pentru Notebook-uri.

### Apoi, configurează variabilele de mediu

- Copiază fișierul `.env.copy` din rădăcina repo-ului în `.env` și completează valorile `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` și `AZURE_OPENAI_DEPLOYMENT`. Revino la [secțiunea Learning Sandbox](#mediu-de-învățare-sandbox) pentru a învăța cum.

### Apoi, deschide Jupyter Notebook

- Selectează kernel-ul de rulare. Dacă folosești opțiunile 1 sau 2, pur și simplu selectează kernel-ul Python 3.10.x implicit oferit de containerul de dezvoltare.

Ești gata să execuți exercițiile. Reține că aici nu există răspunsuri _corecte sau greșite_ - doar explorarea opțiunilor prin încercare și eroare și construirea unei intuiții pentru ceea ce funcționează pentru un model și un domeniu de aplicație dat.

_Din acest motiv nu există segmente de soluții de cod în această lecție. În schimb, Notebook-ul va avea celule Markdown intitulate "Soluția mea:" care arată un exemplu de rezultat ca referință._

 <!--
ȘABLON LECȚIE:
Încheie secțiunea cu un sumar și resurse pentru învățare autodidactă.
-->

## Verificare cunoștințe

Care dintre următoarele este un prompt bun urmând câteva bune practici rezonabile?

1. Arată-mi o imagine cu o mașină roșie
2. Arată-mi o imagine cu o mașină roșie de marcă Volvo și model XC90 parcată lângă o stâncă cu soarele apunând
3. Arată-mi o imagine cu o mașină roșie de marcă Volvo și model XC90

Răspuns: 2 este cel mai bun prompt deoarece oferă detalii despre „ce” și intră în specific (nu o mașină oarecare, ci o marcă și un model specifice) și descrie și cadrul general. 3 este următorul cel mai bun deoarece conține, de asemenea, multe descrieri.

## 🚀 Provocare

Vezi dacă poți folosi tehnica „indiciului” cu promptul: Completează propoziția „Arată-mi o imagine cu o mașină roșie de marcă Volvo și „. Cu ce răspunde și cum ai îmbunătăți-o?

## Foarte bine! Continuă să înveți

Vrei să afli mai multe despre diferite concepte de Inginerie a Prompturilor? Mergi la [pagina de studii continue](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a găsi alte resurse excelente pe acest subiect.

Mergi la Lecția 5 unde vom analiza [tehnici avansate de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->