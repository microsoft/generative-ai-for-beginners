# Fundamentele Ingineriei Prompturilor

[![Fundamentele Ingineriei Prompturilor](../../../translated_images/ro/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introducere
Acest modul acoperă concepte și tehnici esențiale pentru crearea de prompturi eficiente în modelele AI generative. Modul în care scrii promptul pentru un LLM contează de asemenea. Un prompt atent elaborat poate obține o calitate mai bună a răspunsului. Dar ce înseamnă exact termeni precum _prompt_ și _ingineria prompturilor_? Și cum pot îmbunătăți promptul _input_ pe care îl trimit către LLM? Acestea sunt întrebările la care vom încerca să răspundem în acest capitol și în următorul.

_AI generativă_ este capabilă să creeze conținut nou (de exemplu, text, imagini, audio, cod etc.) ca răspuns la cerințele utilizatorului. Aceasta se realizează folosind _Modele Mari de Limbaj_ precum seria GPT de la OpenAI ("Generative Pre-trained Transformer") antrenate pentru a folosi limbajul natural și codul.

Utilizatorii pot interacționa acum cu aceste modele folosind paradigme familiare, precum chat, fără să aibă nevoie de expertiză tehnică sau instruire. Modelele sunt _bazate pe prompturi_ - utilizatorii trimit un input text (prompt) și primesc răspunsul AI-ului (completare). Ei pot apoi să "discută cu AI-ul" iterativ, în conversații cu mai multe runde, rafinând promptul până când răspunsul corespunde așteptărilor lor.

„Prompturile” devin acum interfața principală de _programare_ pentru aplicațiile AI generative, spunând modelelor ce să facă și influențând calitatea răspunsurilor returnate. „Ingineria prompturilor” este un domeniu în expansiune rapidă, care se concentrează pe _proiectarea și optimizarea_ prompturilor pentru a oferi răspunsuri consistente și de calitate la scară.

## Obiectivele Învățării

În această lecție, învățăm ce este Ingineria Prompturilor, de ce contează și cum putem construi prompturi mai eficiente pentru un model și un obiectiv de aplicație date. Vom înțelege conceptele de bază și cele mai bune practici în ingineria prompturilor - și vom afla despre un mediu interactiv Jupyter Notebooks "sandbox", unde putem vedea aceste concepte aplicate pe exemple reale.

La finalul acestei lecții vom putea:

1. Explica ce este ingineria prompturilor și de ce este importantă.
2. Descrie componentele unui prompt și cum sunt folosite.
3. Învață cele mai bune practici și tehnici pentru ingineria prompturilor.
4. Aplică tehnicile învățate pe exemple reale, folosind un endpoint OpenAI.

## Termeni Cheie

Ingineria Prompturilor: Practica de proiectare și rafinare a intrărilor pentru a ghida modelele AI să producă ieșirile dorite.
Tokenizare: Procesul de transformare a textului în unități mai mici, numite tokeni, pe care un model le poate înțelege și procesa.
LLM-uri Ajustate prin Instrucțiuni: Modele Mari de Limbaj (LLM) care au fost ajustate fin cu instrucțiuni specifice pentru a îmbunătăți acuratețea și relevanța răspunsurilor lor.

## Mediu de Învățare Sandbox

Ingineria prompturilor este în prezent mai mult o artă decât o știință. Cel mai bun mod de a ne îmbunătăți intuiția este să _exersăm mai mult_ și să adoptăm o abordare de încercare și eroare care combină expertiza domeniului de aplicare cu tehnici recomandate și optimizări specifice modelului.

Notebook-ul Jupyter asociat acestei lecții oferă un mediu _sandbox_ unde poți încerca ceea ce înveți - pe parcurs sau ca parte a provocării cod la final. Pentru a executa exercițiile vei avea nevoie de:

1. **O cheie API Azure OpenAI** - endpoint-ul de serviciu pentru un LLM implementat.
2. **Un mediu de execuție Python** - în care notebook-ul poate fi rulat.
3. **Variabile de mediu locale** - _finalizează pașii din [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) acum pentru a te pregăti_.

Notebook-ul vine cu exerciții _de start_ - dar ești încurajat să adaugi propriile tale secțiuni de _Markdown_ (descriere) și _Cod_ (cereri de prompt) pentru a încerca mai multe exemple sau idei - și a-ți construi intuiția pentru proiectarea prompturilor.

## Ghid Ilustrat

Vrei să înțelegi panorama completă a ceea ce acoperă această lecție înainte să începi? Vezi acest ghid ilustrat, care îți oferă o idee despre principalele subiecte abordate și concluziile cheie la care să reflectezi pentru fiecare. Harta lecției te conduce de la înțelegerea conceptelor de bază și a provocărilor către modul de a le aborda cu tehnici relevante de inginerie a prompturilor și cele mai bune practici. Reține că secțiunea „Tehnici Avansate” din acest ghid se referă la conținutul acoperit în capitolul _următor_ al acestui curriculum.

![Ghid Ilustrat pentru Ingineria Prompturilor](../../../translated_images/ro/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startup-ul Nostru

Acum, să vorbim despre cum _acest subiect_ se leagă de misiunea startup-ului nostru de a [aduce inovație AI în educație](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Ne dorim să construim aplicații AI pentru _învățare personalizată_ - așa că să ne gândim cum diferiți utilizatori ai aplicației noastre ar putea „proiecta” prompturi:

- **Administratorii** ar putea cere AI-ului să _analizeze datele curriculare pentru a identifica lacune în acoperire_. AI-ul poate sumariza rezultatele sau le poate vizualiza cu cod.
- **Profesorii** ar putea cere AI-ului să _genereze un plan de lecție pentru un public și subiect țintă_. AI-ul poate construi planul personalizat într-un format specificat.
- **Elevii** ar putea cere AI-ului să _le fie tutor în unei materii dificile_. AI-ul poate ghida acum elevii cu lecții, indicii și exemple adaptate nivelului lor.

Aceasta este doar suprafața icebergului. Consultă [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - o bibliotecă open-source de prompturi curatoriată de experți în educație - pentru a avea o imagine mai largă a posibilităților! _Încearcă să rulezi câteva din acele prompturi în sandbox sau folosind OpenAI Playground pentru a vedea ce se întâmplă!_

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să acopere conceptul de bază #1.
Consolidează conceptul cu exemple și referințe.

CONCEPT #1:
Ingineria Prompturilor.
Definește-l și explică de ce este necesar.
-->

## Ce este Ingineria Prompturilor?

Am început această lecție definind **Ingineria Prompturilor** ca procesul de _proiectare și optimizare_ a intrărilor textuale (prompturi) pentru a oferi răspunsuri consistente și de calitate (completări) pentru un obiectiv specific de aplicație și model. Putem gândi acest lucru ca un proces în 2 pași:

- _proiectarea_ promptului inițial pentru un anumit model și obiectiv
- _rafinarea_ promptului iterativ pentru a îmbunătăți calitatea răspunsului

Este un proces necesar de încercare și eroare care necesită intuiția și efortul utilizatorului pentru a obține rezultate optime. Deci, de ce este important? Pentru a răspunde, trebuie mai întâi să înțelegem trei concepte:

- _Tokenizarea_ = cum „vede” modelul promptul
- _LLM-uri de bază_ = cum „procesează” un prompt modelul fundație
- _LLM-uri ajustate prin instrucțiuni_ = cum poate modelul acum să „vadă sarcini”

### Tokenizarea

Un LLM vede prompturile ca o _sequență de tokeni_ unde diferite modele (sau versiuni ale unui model) pot tokeniza același prompt în moduri diferite. Deoarece LLM-urile sunt antrenate pe tokeni (și nu pe text brut), modul în care prompturile sunt tokenizate are un impact direct asupra calității răspunsului generat.

Pentru a înțelege intuitiv cum funcționează tokenizarea, încearcă instrumente precum [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prezentat mai jos. Copiază promptul tău și vezi cum se convertește în tokeni, observând cum sunt gestionate caracterele de spațiu alb și semnele de punctuație. Reține că acest exemplu arată un LLM mai vechi (GPT-3) - așa că încercarea cu un model mai nou poate produce un rezultat diferit.

![Tokenizare](../../../translated_images/ro/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concept: Modele Fundație

Odată ce un prompt este tokenizat, funcția primară a ["LLM-ului de bază"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (sau modelul fundație) este să prezică tokenul următor în acea secvență. Deoarece LLM-urile sunt antrenate pe date masive de text, ele au o bună înțelegere a relațiilor statistice dintre tokeni și pot face acea predicție cu ceva încredere. Reține că nu înțeleg _semnificația_ cuvintelor din prompt sau token; văd doar un tipar pe care îl pot „completa” cu următoarea lor prezicere. Pot continua să prezică secvența până când sunt oprite prin intervenția utilizatorului sau o condiție prestabilită.

Vrei să vezi cum funcționează completarea bazată pe prompt? Introdu promptul de mai sus în [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) cu setările implicite. Sistemul este configurat să trateze prompturile ca cereri de informații - așa că ar trebui să vezi o completare care satisface acest context.

Dar ce se întâmplă dacă utilizatorul vrea să vadă ceva specific, care să îndeplinească anumite criterii sau obiectiv de sarcină? Aici intră în scenă LLM-urile _ajustate prin instrucțiuni_.

![Completare Chat LLM de bază](../../../translated_images/ro/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concept: LLM-uri Ajustate prin Instrucțiuni

Un [LLM ajustat prin instrucțiuni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) pornește de la modelul fundație și îl ajustează fin cu exemple sau perechi input/output (de ex., mesaje multi-rundă) care pot conține instrucțiuni clare - iar răspunsul AI încearcă să urmeze acea instrucțiune.

Aceasta folosește tehnici precum Învățarea prin Recompensare cu Feedback Uman (RLHF) care pot antrena modelul să _urmeze instrucțiuni_ și să _învețe din feedback_ astfel încât să producă răspunsuri mai potrivite aplicațiilor practice și mai relevante pentru obiectivele utilizatorului.

Hai să încercăm - revizuiește promptul de mai sus, dar schimbă acum mesajul _sistem_ pentru a furniza următoarea instrucțiune ca și context:

> _Rezuma conținutul primit pentru un elev din clasa a doua. Păstrează rezultatul într-un paragraf cu 3-5 puncte importante._

Vezi cum rezultatul este acum ajustat pentru a reflecta scopul și formatul dorite? Un educator poate folosi acum direct acest răspuns în slide-urile pentru acea clasă.

![Completare Chat LLM Ajustat prin Instrucțiuni](../../../translated_images/ro/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## De ce avem nevoie de Ingineria Prompturilor?

Acum că știm cum sunt procesate prompturile de LLM-uri, să vorbim despre _de ce_ avem nevoie de ingineria prompturilor. Răspunsul constă în faptul că LLM-urile actuale ridică o serie de provocări care fac ca _completările fiabile și consistente_ să fie mai greu de realizat fără efort în construcția și optimizarea prompturilor. De exemplu:

1. **Răspunsurile modelului sunt stocastice.** Același prompt va produce probabil răspunsuri diferite cu modele sau versiuni diferite ale modelului. Și poate chiar produce rezultate diferite cu _același model_ în momente diferite. _Tehnicile de inginerie a prompturilor ne pot ajuta să minimizăm aceste variații oferind ghidaje mai bune_.

1. **Modelele pot fabrica răspunsuri.** Modelele sunt pre-antrenate cu seturi de date _mari dar finite_, ceea ce înseamnă că le lipsesc cunoștințe despre concepte în afara acelui domeniu de antrenare. Ca rezultat, pot produce completări inexacte, imaginare sau direct contradictorii cu fapte cunoscute. _Tehnicile de inginerie a prompturilor ajută utilizatorii să identifice și să atenueze astfel de fabricări, de exemplu prin cererea de citări sau raționament de la AI_.

1. **Capabilitățile modelelor vor varia.** Modelele mai noi sau generațiile de modele vor avea capabilități mai bogate, dar vin și cu particularități și compromisuri unice în ceea ce privește costul și complexitatea. _Ingineria prompturilor ne poate ajuta să dezvoltăm cele mai bune practici și fluxuri de lucru care să abstractizeze diferențele și să se adapteze cerințelor specifice modelului în mod scalabil și fără întreruperi_.

Să vedem asta în acțiune în OpenAI sau Azure OpenAI Playground:

- Folosește același prompt cu implementări diferite de LLM (de exemplu, OpenAI, Azure OpenAI, Hugging Face) - ai observat variațiile?
- Folosește în mod repetat același prompt cu _aceeași_ implementare LLM (de exemplu, playground-ul Azure OpenAI) - cum au diferit aceste variații?

### Exemplu de Fabricări

În acest curs, folosim termenul **„fabricare”** pentru a desemna fenomenul în care LLM-urile generează uneori informații factual incorecte din cauza limitărilor în antrenarea lor sau alte constrângeri. Ai putea auzi acest fenomen numit și _„halucinații”_ în articole populare sau lucrări de cercetare. Totuși, recomandăm insistent folosirea termenului _„fabricare”_ pentru a nu antropomorfiza comportamentul atribuindu-i un trăsătură umană unui rezultat determinat de mașină. Aceasta susține și [ghidurile AI Responsabil](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) din perspectiva terminologiei, eliminând termeni care ar putea fi considerați ofensatori sau neincluzivi în anumite contexte.

Vrei să înțelegi cum funcționează fabricările? Gândește-te la un prompt care îi cere AI-ului să genereze conținut pentru un subiect inexistent (pentru a te asigura că nu se găsește în datasetul de antrenament). De exemplu - am încercat acest prompt:

> **Prompt:** generează un plan de lecție despre Războiul Marțian din 2076.

Căutarea web mi-a arătat că au existat relatări fictive (de ex., seriale televizate sau cărți) despre războaie marțiene - dar niciodată în 2076. Logica comună ne spune de asemenea că 2076 este _în viitor_ și, prin urmare, nu poate fi asociat unui eveniment real.


Ce se întâmplă atunci când rulăm acest prompt cu diferiți furnizori de LLM?

> **Răspuns 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/ro/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Răspuns 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/ro/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Răspuns 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/ro/04-fabrication-huggingchat.faf82a0a51278956.webp)

Așa cum era de așteptat, fiecare model (sau versiune de model) produce răspunsuri ușor diferite datorită comportamentului stocastic și variațiilor în capacitatea modelului. De exemplu, un model țintește către un public de clasa a 8-a, în timp ce altul presupune un elev de liceu. Dar toate cele trei modele au generat răspunsuri care ar putea convinge un utilizator neinformat că evenimentul a fost real.

Tehnicile de inginerie a promptului precum _metaprompting_ și _configurarea temperaturii_ pot reduce într-o anumită măsură fabricările modelului. Noi _arhitecturi_ de inginerie a promptului integrează, de asemenea, noi unelte și tehnici fără întrerupere în fluxul promptului, pentru a atenua sau reduce unele dintre aceste efecte.

## Studiu de caz: GitHub Copilot

Să încheiem această secțiune obținând o perspectivă asupra modului în care ingineria promptului este folosită în soluții reale, uitându-ne la un studiu de caz: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot este „Programatorul Tău Asistent AI” – convertește prompturile text în completări de cod și este integrat în mediul tău de dezvoltare (de exemplu Visual Studio Code) pentru o experiență de utilizare fără întreruperi. Așa cum este documentat în seria de bloguri de mai jos, prima versiune a fost bazată pe modelul OpenAI Codex – cu ingineri realizând rapid necesitatea ajustării fine a modelului și dezvoltării unor tehnici mai bune de inginerie a prompturilor, pentru a îmbunătăți calitatea codului. În iulie, au [lansat un model AI îmbunătățit care depășește Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pentru sugestii și mai rapide.

Citește postările în ordine, pentru a urmări traseul lor de învățare.

- **Mai 2023** | [GitHub Copilot devine mai bun la înțelegerea codului tău](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [În interiorul GitHub: Lucrând cu LLM-urile din spatele GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Iun 2023** | [Cum să scrii prompturi mai bune pentru GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Iul 2023** | [.. GitHub Copilot depășește Codex cu un model AI îmbunătățit](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Iul 2023** | [Ghidul dezvoltatorului pentru ingineria prompturilor și LLM-uri](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cum să construiești o aplicație LLM pentru întreprinderi: lecții de la GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Poți, de asemenea, să răsfoiești [blogul lor de inginerie](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pentru mai multe postări precum [aceasta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), care arată cum aceste modele și tehnici sunt _aplicate_ pentru a conduce aplicații în lumea reală.

---

<!--
ȘABLON PENTRU LECȚIE:
Această unitate ar trebui să acopere conceptul de bază #2.
Consolidarea conceptului cu exemple și referințe.

CONCEPTUL #2:
Designul promptului.
Ilustrat cu exemple.
-->

## Construirea Promptului

Am văzut de ce ingineria promptului este importantă – acum să înțelegem cum sunt _construite_ prompturile pentru a putea evalua tehnici diferite pentru un design mai eficient al promptului.

### Prompt de bază

Să începem cu promptul de bază: un input text trimis modelului fără alt context. Iată un exemplu – când trimitem primele câteva cuvinte ale imnului național al SUA către OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), acesta imediat _completează_ răspunsul cu următoarele rânduri, ilustrând comportamentul de predicție de bază.

| Prompt (Input)     | Completare (Output)                                                                                                                            |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Se pare că începi versurile imnului „The Star-Spangled Banner,” imnul național al Statelor Unite. Textul complet este ...                   |

### Prompt complex

Acum să adăugăm context și instrucțiuni la acel prompt simplu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ne permite să construim un prompt complex ca o colecție de _mesaje_ cu:

- Perechi input/output care reflectă inputul _utilizatorului_ și răspunsul _asistentului_.
- Mesaj de sistem care setează contextul pentru comportamentul sau personalitatea asistentului.

Cererea este acum în forma de mai jos, unde _tokenizarea_ capturează eficient informații relevante din context și conversație. Acum, schimbarea contextului sistemului poate avea un impact la fel de mare asupra calității completărilor ca și inputurile utilizatorului oferite.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt de instrucțiuni

În exemplele de mai sus, promptul utilizatorului a fost o interogare simplă în text care poate fi interpretată ca o cerere de informații. Cu prompturile de _instrucțiuni_, putem folosi acel text pentru a specifica o sarcină în detaliu, oferind o îndrumare mai bună AI-ului. Iată un exemplu:

| Prompt (Input)                                                                                                                                                                                                                         | Completare (Output)                                                                                                        | Tip instrucțiune    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Scrie o descriere a Războiului Civil                                                                                                                                                                                                 | _a returnat un paragraf simplu_                                                                                            | Simplu              |
| Scrie o descriere a Războiului Civil. Oferă date și evenimente cheie și descrie semnificația lor                                                                                                                                       | _a returnat un paragraf urmat de o listă cu datele evenimentelor cheie și descrieri_                                       | Complex             |
| Scrie o descriere a Războiului Civil în 1 paragraf. Oferă 3 puncte cu date cheie și semnificația lor. Oferă încă 3 puncte cu figuri istorice importante și contribuțiile lor. Returnează rezultatul ca un fișier JSON                                          | _returnează detalii mai extinse într-o casetă de text, formatată ca JSON, pe care o poți copia-lipi într-un fișier și valida după nevoie_ | Complex. Formatat. |

## Conținut Primar

În exemplele de mai sus, promptul era încă destul de deschis, permițând LLM-ului să decidă ce parte din setul său de date pre-antrenat este relevantă. Cu modelul de design _conținut primar_, textul de intrare este împărțit în două părți:

- o instrucțiune (acțiune)
- conținut relevant (care influențează acțiunea)

Iată un exemplu în care instrucțiunea este „rezumă asta în 2 fraze”.

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completare (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și era cunoscut civilizațiilor antice încă dinainte de istoria înregistrată. Poartă numele zeului roman Jupiter.[19] Văzut de pe Pământ, Jupiter poate fi destul de strălucitor încât lumina reflectată să proiecteze umbre vizibile,[20] și este în medie al treilea obiect natural cel mai luminos pe cerul nopții după Lună și Venus. <br/> **Rezumați asta în 2 propoziții scurte** | Jupiter, a cincea planetă de la Soare, este cea mai mare din Sistemul Solar și este cunoscută pentru a fi unul dintre cele mai strălucitoare obiecte de pe cerul nopții. Numită după zeul roman Jupiter, este un gigant gazos a cărui masă este de două ori și jumătate mai mare decât a tuturor celorlalte planete din Sistemul Solar combinate. |

Segmentul de conținut primar poate fi folosit în diverse moduri pentru a conduce instrucțiuni mai eficiente:

- **Exemple** – în loc să spui modelului ce să facă cu o instrucțiune explicită, oferă-i exemple a ceea ce să facă și lasă-l să deducă tiparul.
- **Indici** – urmează instrucțiunea cu un „indiciu” care pregătește completarea, ghidând modelul către răspunsuri mai relevante.
- **Șabloane** – acestea sunt „rețete” repetabile pentru prompturi cu spații rezervate (variabile) care pot fi personalizate cu date pentru cazuri specifice.

Să explorăm acestea în acțiune.

### Folosind exemple

Aceasta este o abordare în care folosești conținutul primar pentru a „hrană modelului” cu câteva exemple ale rezultatului dorit pentru o instrucțiune dată, lăsându-l să deducă tiparul rezultatului dorit. Pe baza numărului de exemple oferite, putem avea zero-shot prompting, one-shot prompting, few-shot prompting etc.

Promptul acum constă din trei componente:

- O descriere a sarcinii
- Câteva exemple ale rezultatului dorit
- Începutul unui nou exemplu (care devine o descriere implicită a sarcinii)

| Tip de învățare | Prompt (Input)                                                                                                                                        | Completare (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | „The Sun is Shining”. Tradu în spaniolă                                                                                                            | „El Sol está brillando”.    |
| One-shot      | „The Sun is Shining” => „El Sol está brillando”. <br> „It's a Cold and Windy Day” =>                                                                 | „Es un día frío y ventoso”. |
| Few-shot      | Jucătorul a alergat în jurul bazelor => Baseball <br/> Jucătorul a dat un as => Tenis <br/> Jucătorul a dat un șase => Cricket <br/> Jucătorul a făcut un slam-dunk => | Baschet                    |
|               |                                                                                                                                                       |                             |

Observă cum a trebuit să oferim instrucțiuni explicite („Tradu în spaniolă”) în zero-shot prompting, dar aceasta este dedusă în exemplul one-shot prompting. Exemplul few-shot arată cum adăugarea mai multor exemple permite modelelor să facă deducții mai precise fără instrucțiuni suplimentare.

### Indici pentru prompt

O altă tehnică pentru folosirea conținutului primar este să oferi _indici_ în loc de exemple. În acest caz, îi dăm modelului un impuls în direcția corectă prin _începerea lui_ cu un extract care reflectă formatul răspunsului dorit. Modelul „prinde indiciul” pentru a continua în aceeași linie.

| Număr de indici | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completare (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și era cunoscut civilizațiilor antice încă dinainte de istoria înregistrată. <br/>**Rezumați asta**                                       | Jupiter este cea mai mare planetă din Sistemul Solar și a cincea de la Soare. Este un gigant gazos cu o masă de 1/1000 din a Soarelui, dar este mai greu decât toate celelalte planete împreună. Civilizațiile antice au cunoscut Jupiter de mult timp și este ușor vizibil pe cerul nopții. |
| 1              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și era cunoscut civilizațiilor antice încă dinainte de istoria înregistrată. <br/>**Rezumați asta** <br/> Ce am învățat este că Jupiter | este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete împreună. Este ușor vizibil cu ochiul liber și a fost cunoscut încă din cele mai vechi timpuri.                        |

| 2              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât masa tuturor celorlalte planete din Sistemul Solar combinate. Jupiter este unul dintre cele mai luminoase obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscut civilizațiilor antice încă dinaintea istoriei înregistrate. <br/>**Rezumat** <br/> Top 3 fapte învățate:         | 1. Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. <br/> 2. Este un gigant gazos cu o masă o mie de ori mai mică decât cea a Soarelui...<br/> 3. Jupiter a fost vizibil cu ochiul liber încă din vremuri antice ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Șabloane de Prompturi

Un șablon de prompt este o _rețetă predefinită pentru un prompt_ care poate fi stocată și reutilizată după nevoie, pentru a genera experiențe utilizator mai consistente la scară largă. În forma sa cea mai simplă, este pur și simplu o colecție de exemple de prompturi precum [acesta de la OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) care oferă atât componentele interactive ale promptului (mesaje ale utilizatorului și ale sistemului), cât și formatul cererii pe bază de API - pentru a susține reutilizarea.

În forma sa mai complexă, precum [acest exemplu de la LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) conține _locuri rezervate_ care pot fi înlocuite cu date din diverse surse (input de la utilizator, context de sistem, surse externe de date etc.) pentru a genera un prompt dinamic. Acest lucru ne permite să creăm o bibliotecă de prompturi reutilizabile care pot fi folosite pentru a genera experiențe utilizator **programatice** și consistente la scară.

În final, adevărata valoare a șabloanelor constă în abilitatea de a crea și publica _biblioteci de prompturi_ pentru domenii specifice de aplicație - unde șablonul de prompt este acum _optimizat_ pentru a reflecta contextul sau exemplele specifice aplicației care fac răspunsurile mai relevante și corecte pentru publicul țintă. Repozitoriul [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) este un exemplu excelent al acestei abordări, curatorind o bibliotecă de prompturi pentru domeniul educațional, cu accent pe obiective cheie cum ar fi planificarea lecțiilor, proiectarea curriculumului, tutoratul elevilor etc.

## Conținut Suport

Dacă ne gândim la construcția promptului ca având o instrucțiune (sarcină) și un țintă (conținut primar), atunci _conținutul secundar_ este ca un context suplimentar pe care îl oferim pentru a **influența rezultatul într-un fel**. Acesta poate fi parametri de optimizare, instrucțiuni de formatare, taxonomii de subiecte etc. care pot ajuta modelul să-și _personalizeze_ răspunsul pentru a se potrivi obiectivelor sau așteptărilor utilizatorului.

De exemplu: Având un catalog de cursuri cu metadate extinse (nume, descriere, nivel, etichete metadate, instructor etc.) pentru toate cursurile disponibile din curriculum:

- putem defini o instrucțiune de tipul „rezumă catalogul de cursuri pentru toamna lui 2023”
- putem folosi conținutul primar pentru a oferi câteva exemple ale rezultatului dorit
- putem folosi conținutul secundar pentru a identifica primele 5 „etichete” de interes.

Acum, modelul poate oferi un rezumat în formatul arătat de câteva exemple – dar dacă un rezultat are mai multe etichete, poate prioritiza cele 5 etichete identificate în conținutul secundar.

---

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să acopere conceptul principal #1.
Consolidează conceptul cu exemple și referințe.

CONCEPTUL #3:
Tehnici de inginerie a prompturilor.
Care sunt câteva tehnici de bază pentru ingineria promptului?
Ilustrează-le cu câteva exerciții.
-->

## Cele mai bune practici pentru prompturi

Acum că știm cum pot fi _construite_ prompturile, putem începe să ne gândim cum să le _proiectăm_ pentru a reflecta cele mai bune practici. Putem împărți acest lucru în două părți - să avem mentalitatea corectă și să aplicăm tehnicile corecte.

### Mentalitatea Ingineriei Prompturilor

Ingineria prompturilor este un proces de încercare și eroare, așa că ține cont de trei factori generali îndrumători:

1. **Înțelegerea domeniului contează.** Precizia și relevanța răspunsului depind de _domeniul_ în care acea aplicație sau utilizator operează. Aplică-ți intuiția și expertiza în domeniu pentru a **personaliza tehnicile** și mai mult. De exemplu, definește _personalități specifice domeniului_ în prompturile tale de sistem sau folosește _șabloane specifice domeniului_ în prompturile utilizatorului. Oferă conținut secundar care reflectă contexte specifice domeniului sau folosește _indicații și exemple specifice domeniului_ pentru a ghida modelul către pattern-uri de utilizare familiare.

2. **Înțelegerea modelului contează.** Știm că modelele sunt în mod natural stocastice. Dar implementările modelelor pot varia în funcție de setul de date cu care sunt antrenate (cunoaștere pre-antrenată), capacitățile pe care le oferă (de ex., prin API sau SDK) și tipul de conținut pentru care sunt optimizate (de ex., cod față de imagini față de text). Înțelege punctele forte și limitările modelului pe care îl folosești și folosește această cunoaștere pentru a _prioritiza sarcinile_ sau pentru a crea _șabloane personalizate_ optimizate pentru capacitățile modelului.

3. **Iterarea & validarea contează.** Modelele evoluează rapid, la fel și tehnicile pentru ingineria prompturilor. Ca expert în domeniu, poți avea alte contexte sau criterii specifice aplicației tale, care nu se aplică comunității largi. Folosește uneltele și tehnicile de inginerie a prompturilor pentru a „porni rapid” construcția promptului, apoi iterează și validează rezultatele folosindu-ți propria intuiție și expertiză. Înregistrează-ți observațiile și creează o **bază de cunoștințe** (de ex., biblioteci de prompturi) care poate fi folosită ca o nouă bază pentru alții, pentru iterații mai rapide pe viitor.

## Cele mai bune practici

Să analizăm acum câteva bune practici comune recomandate de practicienii [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) și [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ce                                | De ce                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluează cele mai noi modele.     | Noile generații de modele probabil au caracteristici și calitate îmbunătățite - dar pot implica și costuri mai mari. Evaluează-le pentru impact, apoi ia decizii privind migrarea.                                                                      |
| Separează instrucțiunile și contextul | Verifică dacă modelul/titularul definește _delimitatori_ pentru a distinge mai clar instrucțiunile, conținutul primar și secundar. Acest lucru poate ajuta modelele să atribuie greutăți mai precis tokenilor.                                           |
| Fii specific și clar              | Oferă mai multe detalii despre contextul dorit, rezultat, lungime, format, stil etc. Acest lucru va îmbunătăți atât calitatea cât și consistența răspunsurilor. Salvează rețetele în șabloane reutilizabile.                                            |
| Fii descriptiv, folosește exemple  | Modelele pot răspunde mai bine la o abordare „arată și spune”. Începe cu o abordare `zero-shot` în care îi oferi o instrucțiune (fără exemple), apoi încearcă `few-shot` ca rafinare, oferind câteva exemple ale rezultatului dorit. Folosește analogii. |
| Folosește indicii pentru a impulsiona completările | Împinge modelul spre un rezultat dorit oferindu-i câteva cuvinte sau fraze de start pe care să le poată folosi ca punct de plecare pentru răspuns.                                                                                              |
| Repetă (Double Down)               | Uneori trebuie să te repeți față de model. Oferă instrucțiuni înainte și după conținutul primar, folosește o instrucțiune și un indiciu etc. Iterează și validează pentru a vedea ce funcționează.                                                   |
| Ordinea contează                  | Ordinea în care prezinți informația modelului poate afecta rezultatul, chiar și în exemplele de învățare, datorită biasului de recență. Testează opțiuni diferite pentru a vedea ce merge cel mai bine.                                            |
| Oferă modelului o "ieșire de rezervă" | Oferă modelului un răspuns completare _fallback_ pe care să-l poată folosi dacă nu poate finaliza sarcina din orice motiv. Acest lucru poate reduce șansele ca modelele să genereze răspunsuri false sau fabricate.                                   |
|                                   |                                                                                                                                                                                                                                                   |

Ca orice bună practică, amintește-ți că _experiența ta poate varia_ în funcție de model, sarcină și domeniu. Folosește aceste recomandări ca punct de plecare, și iterează pentru a găsi ce funcționează cel mai bine pentru tine. Reevaluează constant procesul de inginerie a prompturilor pe măsură ce apar modele și unelte noi, cu accent pe scalabilitatea procesului și calitatea răspunsurilor.

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să ofere o provocare de cod dacă este cazul

PROVOCARE:
Link către un Jupyter Notebook care cuprinde doar comentariile codului în instrucțiuni (secțiunile de cod sunt goale).

SOLUȚIE:
Link către o copie a acelui Notebook cu prompturile completate și rulate, arătând un exemplu posibil.
-->

## Tema

Felicitări! Ai ajuns la finalul lecției! Este timpul să testezi unele dintre conceptele și tehnicile prezentate cu exemple reale!

Pentru tema noastră, vom folosi un Jupyter Notebook cu exerciții pe care le poți completa interactiv. Poți de asemenea să extinzi Notebook-ul cu propriile celule Markdown și Cod pentru a explora singur idei și tehnici.

### Pentru a începe, fă un fork al repo-ului, apoi

- (Recomandat) Lansează GitHub Codespaces
- (Alternativ) Clonează repo-ul pe dispozitivul tău local și folosește-l cu Docker Desktop
- (Alternativ) Deschide Notebook-ul în mediul preferat pentru rularea Notebook-urilor.

### Apoi configurează variabilele tale de mediu

- Copiază fișierul `.env.copy` din rădăcina repo-ului în `.env` și completează valorile `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` și `AZURE_OPENAI_DEPLOYMENT`. Revino la [secțiunea Playground de învățare](#mediu-de-învățare-sandbox) pentru a afla cum.

### Apoi, deschide Jupyter Notebook-ul

- Selectează kernel-ul de rulare. Dacă folosești opțiunile 1 sau 2, selectează pur și simplu kernel-ul Python 3.10.x implicit oferit de containerul de dezvoltare.

Ești gata să rulezi exercițiile. Reține că nu există răspunsuri _corecte sau greșite_ aici - doar explorări prin încercare și eroare și construirea intuiției despre ce funcționează pentru un anumit model și domeniu de aplicație.

_Din acest motiv nu există segmente cu Soluția Codului în această lecție. În schimb, Notebook-ul va avea celule Markdown intitulate "Soluția mea:" care arată un exemplu de ieșire pentru referință._

 <!--
ȘABLON LECȚIE:
Încheie secțiunea cu un rezumat și resurse pentru învățare autodirijată.
-->

## Verificarea cunoștințelor

Care dintre următoarele este un prompt bun care urmează unele bune practici raționale?

1. Arată-mi o imagine cu o mașină roșie
2. Arată-mi o imagine cu o mașină roșie marca Volvo model XC90 parcată lângă o stâncă cu apusul soarelui
3. Arată-mi o imagine cu o mașină roșie marca Volvo model XC90

R: 2, este cel mai bun prompt deoarece oferă detalii despre „ce” și intră în specific (nu orice mașină, ci o marcă și model specific) și descrie de asemenea contextul general. 3 este pe locul doi deoarece conține și multă descriere.

## 🚀 Provocare

Vezi dacă poți folosi tehnica „indiciu” cu promptul: Completează propoziția "Arată-mi o imagine cu o mașină roșie marca Volvo și ". Cum răspunde și cum ai putea să-l îmbunătățești?

## Foarte bine! Continuă să înveți

Vrei să afli mai multe despre diferite concepte de Inginerie a Prompturilor? Accesează [pagina de învățare continuă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a găsi alte resurse grozave pe această temă.

Mergi la Lecția 5 unde vom analiza [tehnici avansate de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->