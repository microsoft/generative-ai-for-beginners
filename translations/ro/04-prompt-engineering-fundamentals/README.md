# Fundamentele ingineriei prompturilor

[![Fundamentele ingineriei prompturilor](../../../translated_images/ro/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introducere
Acest modul acoperă conceptele și tehnicile esențiale pentru crearea unor prompturi eficiente în modelele generative AI. Modul în care formulezi promptul către un LLM contează de asemenea. Un prompt atent elaborat poate obține o calitate mai bună a răspunsului. Dar ce înseamnă exact termenii _prompt_ și _ingineria prompturilor_? Și cum îmbunătățesc promptul _input_ pe care îl trimit la LLM? Acestea sunt întrebările la care vom încerca să răspundem în acest capitol și în următorul.

_IA generativă_ este capabilă să creeze conținut nou (de ex., text, imagini, audio, cod etc.) ca răspuns la solicitările utilizatorilor. Face acest lucru folosind _Modele Mari de Limbaj_ precum seria GPT ("Generative Pre-trained Transformer") de la OpenAI, antrenate pentru a utiliza limbaj natural și cod.

Utilizatorii pot interacționa acum cu aceste modele folosind paradigme familiare, cum ar fi chat-ul, fără a avea nevoie de cunoștințe tehnice sau instruire. Modelele sunt _bazate pe prompturi_ – utilizatorii trimit un text (prompt) și primesc înapoi răspunsul AI (completarea). Pot apoi să "converseze cu AI-ul" iterativ, în conversații pe mai multe runde, rafinând promptul până când răspunsul corespunde așteptărilor lor.

"Prompturile" devin acum interfața principală de _programare_ pentru aplicațiile AI generative, spunând modelelor ce să facă și influențând calitatea răspunsurilor returnate. "Ingineria prompturilor" este un domeniu în rapidă dezvoltare care se concentrează pe _proiectarea și optimizarea_ prompturilor pentru a oferi răspunsuri consistente și de calitate la scară.

## Obiective de învățare

În această lecție, învățăm ce este ingineria prompturilor, de ce este importantă și cum putem crea prompturi mai eficiente pentru un anumit model și obiectiv de aplicație. Vom înțelege conceptele de bază și cele mai bune practici pentru ingineria prompturilor și vom învăța despre un mediu interactiv tip Jupyter Notebooks „sandbox” în care putem vedea aceste concepte aplicate pe exemple reale.

La finalul acestei lecții vom putea:

1. Explica ce este ingineria prompturilor și de ce contează.
2. Descrie componentele unui prompt și modul în care sunt folosite.
3. Învăța cele mai bune practici și tehnici pentru ingineria prompturilor.
4. Aplica tehnicile învățate pe exemple reale, folosind un endpoint OpenAI.

## Termeni cheie

Ingineria prompturilor: Practica de a proiecta și rafina inputuri pentru a ghida modelele AI să producă ieșiri dorite.  
Tokenizare: Procesul de a transforma textul în unități mai mici, numite tokeni, pe care un model le poate înțelege și procesa.  
LLM-uri instruite cu instrucțiuni: Modele mari de limbaj care au fost ajustate fin cu instrucțiuni specifice pentru a îmbunătăți acuratețea și relevanța răspunsurilor.

## Mediu de testare

Ingineria prompturilor este în prezent mai mult o artă decât o știință. Cel mai bun mod de a ne îmbunătăți intuiția este să _practicăm mai mult_ și să adoptăm o abordare de încercare și eroare care să combine expertiza domeniului aplicației cu tehnicile recomandate și optimizările specifice modelului.

Notebook-ul Jupyter care însoțește această lecție oferă un mediu _sandbox_ în care poți încerca ce înveți – pe parcurs sau ca parte a provocării de cod de la final. Pentru a rula exercițiile, ai nevoie de:

1. **O cheie API Azure OpenAI** – endpoint-ul serviciului pentru un LLM deja implementat.  
2. **Un runtime Python** – în care să poți executa Notebook-ul.  
3. **Variabile de mediu locale** – _finalizează pașii din [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) acum pentru a fi pregătit_.

Notebook-ul vine cu exerciții _de start_ – dar e încurajat să adaugi propriile secțiuni de _Markdown_ (descriere) și _Code_ (cereri de prompt) pentru a testa mai multe exemple sau idei și a-ți dezvolta intuiția pentru crearea prompturilor.

## Ghid ilustrat

Vrei să ai o vedere de ansamblu asupra a ceea ce acoperă această lecție înainte să începi? Consultă acest ghid ilustrat, care îți oferă o perspectivă asupra principalelor subiecte abordate și asupra punctelor cheie pe care să le iei în considerare pentru fiecare. Planul lecției te conduce de la înțelegerea conceptelor și provocărilor de bază la abordarea lor cu tehnici relevante de inginerie a prompturilor și cele mai bune practici. Reține că secțiunea „Tehnici avansate” din acest ghid face referire la conținutul acoperit în _următorul_ capitol al acestui curriculum.

![Ghid ilustrat pentru ingineria prompturilor](../../../translated_images/ro/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startup-ul nostru

Acum, să vorbim despre cum _acest subiect_ se raportează la misiunea startup-ului nostru de a [aduce inovația AI în educație](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Ne dorim să construim aplicații AI pentru _învățare personalizată_, așa că să ne gândim cum diferiți utilizatori ai aplicației noastre ar putea „proiecta” prompturi:

- **Administratorii** ar putea cere AI-ului să _analizeze datele curriculare pentru a identifica lacune în acoperire_. AI-ul poate sumariza rezultatele sau să le vizualizeze folosind cod.  
- **Educatorii** ar putea cere AI-ului să _genereze un plan de lecție pentru un public țintă și un subiect_. AI-ul poate construi planul personalizat într-un format specificat.  
- **Elevii** ar putea cere AI-ului să _le ofere meditații la o materie dificilă_. AI-ul poate ghida elevii cu lecții, sugestii și exemple adaptate nivelului lor.

Acesta este doar vârful aisbergului. Consultă [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – o bibliotecă open-source de prompturi curatoriată de experți în educație – pentru a înțelege mai bine posibilitățile! _Încearcă să rulezi unele dintre aceste prompturi în sandbox sau folosind OpenAI Playground pentru a vedea ce se întâmplă!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Ce este ingineria prompturilor?

Am început această lecție definind **ingineria prompturilor** ca procesul de _proiectare și optimizare_ a inputurilor text (prompturi) pentru a livra răspunsuri consistente și de calitate (completări) pentru un anumit obiectiv de aplicație și un model dat. Putem privi acest proces în două etape:

- _proiectarea_ promptului inițial pentru un model și un obiectiv date  
- _rafinarea_ iterativă a promptului pentru a îmbunătăți calitatea răspunsului

Acesta este un proces necesar de încercare și eroare care solicită intuițiile și efortul utilizatorului pentru a obține rezultate optime. Atunci, de ce este important? Pentru a răspunde, trebuie mai întâi să înțelegem trei concepte:

- _Tokenizare_ = cum „vede” modelul promptul  
- _LLM-uri de bază_ = cum „procesează” modelul de bază promptul  
- _LLM-uri instruite cu instrucțiuni_ = cum modelul poate vedea acum „sarcinile”

### Tokenizarea

Un LLM vede prompturile ca o _secvență de tokeni_, iar diferite modele (sau versiuni ale unui model) pot tokeniza același prompt în moduri diferite. Deoarece LLM-urile sunt antrenate pe tokeni (și nu pe text brut), modul în care prompturile sunt tokenizate are un impact direct asupra calității răspunsului generat.

Pentru a-ți face o idee despre cum funcționează tokenizarea, încearcă instrumente precum [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) afișat mai jos. Copiază promptul tău și vezi cum se convertește în tokeni, observând cum sunt tratate caracterele de spațiu și semnele de punctuație. Reține că acest exemplu arată un LLM mai vechi (GPT-3) – deci încercarea cu un model mai nou poate da un rezultat diferit.

![Tokenizare](../../../translated_images/ro/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concept: Modele de bază

După ce promptul este tokenizat, funcția principală a ["LLM-ului de bază"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (sau modelului fundație) este să prezică următorul token din secvență. Deoarece LLM-urile sunt antrenate pe seturi uriașe de date text, ele au o bună înțelegere a relațiilor statistice între tokeni și pot face această predicție cu un anumit grad de încredere. Reține că ele nu înțeleg _sensul_ cuvintelor din prompt sau token; văd doar un tipar pe care îl pot „completa” cu predicția următoare. Pot continua să prezică secvența până când sunt oprite de intervenția utilizatorului sau o condiție predefinită.

Vrei să vezi cum funcționează completarea bazată pe prompt? Introdu promptul de mai sus în Azure OpenAI Studio în [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) cu setările implicite. Sistemul este configurat să trateze prompturile ca solicitări de informații – așa că ar trebui să vezi o completare care să satisfacă acest context.

Dar ce dacă utilizatorul ar dori să vadă ceva specific care să îndeplinească anumite criterii sau obiective de sarcină? Aici intră în scenă LLM-urile _instruit cu instrucțiuni_.

![Completare chat LLM de bază](../../../translated_images/ro/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concept: LLM-uri instruite cu instrucțiuni

Un [LLM instruit cu instrucțiuni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) pornește de la modelul fundație și îl ajustează fin folosind exemple sau perechi input/ieșire (de ex., „mesaje” multi-rundă) care pot conține instrucțiuni clare – iar răspunsul AI încearcă să urmeze acea instrucțiune.

Acest lucru folosește tehnici precum Învățarea prin Recompensă cu Feedback Uman (RLHF) care antrenează modelul să _urmărească instrucțiunile_ și să _învețe din feedback_, astfel încât să producă răspunsuri mai bine adaptate aplicațiilor practice și mai relevante pentru obiectivele utilizatorului.

Să încercăm – revizuiește promptul de mai sus, dar acum schimbă _mesajul sistem_ pentru a oferi următoarea instrucțiune ca context:

> _Rezumați conținutul furnizat pentru un elev de clasa a doua. Menține rezultatul într-un singur paragraf cu 3-5 puncte principale._

Vezi cum rezultatul este acum adaptat pentru a reflecta scopul și formatul dorit? Un educator poate folosi direct acest răspuns în slide-urile pentru acea clasă.

![Completare chat LLM instruit cu instrucțiuni](../../../translated_images/ro/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## De ce avem nevoie de ingineria prompturilor?

Acum că știm cum sunt procesate prompturile de către LLM-uri, să vorbim despre _de ce_ avem nevoie de ingineria prompturilor. Răspunsul stă în faptul că LLM-urile actuale prezintă o serie de provocări care fac ca _completările fiabile și consistente_ să fie mai greu de obținut fără a depune efort în construcția și optimizarea promptului. De exemplu:

1. **Răspunsurile modelului sunt stocastice.** _Același prompt_ va produce probabil răspunsuri diferite la modele sau versiuni diferite de model. Și poate produce chiar rezultate diferite cu _același model_ în momente diferite. _Tehnicile de inginerie a prompturilor ne pot ajuta să minimizăm aceste variații prin oferirea unor limite mai bune_.

1. **Modelele pot fabrica răspunsuri.** Modelele sunt pre-antrenate pe seturi de date _mari, dar finite_, ceea ce înseamnă că nu cunosc concepte în afara acestui antrenament. Ca rezultat, pot genera completări inexacte, imaginative sau direct contradictorii cu faptele cunoscute. _Tehnicile de inginerie a prompturilor ajută utilizatorii să identifice și să atenueze astfel de fabricări, de ex. prin solicitarea de citări sau raționamente AI-ului_.

1. **Capabilitățile modelelor vor varia.** Modelele noi sau generațiile ulterioare vor avea capabilități mai bogate, dar și particularități unice, compromisuri de cost și complexitate. _Ingineria prompturilor ne poate ajuta să dezvoltăm bune practici și fluxuri de lucru care abstractizează diferențele și se adaptează cerințelor specifice fiecărui model în mod scalabil și transparent_.

Să vedem asta în acțiune în OpenAI sau Azure OpenAI Playground:

- Folosește același prompt cu implementări diferite de LLM (de ex., OpenAI, Azure OpenAI, Hugging Face) – ai observat variațiile?  
- Folosește același prompt repetat cu _aceeași_ implementare LLM (de ex., Azure OpenAI playground) – cum s-au diferențiat aceste variații?

### Exemplu de fabricări

În acest curs, folosim termenul **„fabricare”** pentru a desemna fenomenul în care LLM-urile uneori generează informații factual incorecte din cauza limitărilor antrenamentului sau altor constrângeri. Ai putea întâlni și termenul _„halucinații”_ în articole populare sau lucrări de cercetare. Totuși, recomandăm folosirea termenului _„fabricare”_ pentru a evita antropomorfizarea comportamentului, atribuind o trăsătură umană unui rezultat generat de mașină. Aceasta sprijină și [ghidurile AI responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) din perspectiva terminologiei, eliminând termeni care pot fi considerați ofensatori sau neinclusivi în anumite contexte.

Vrei să înțelegi cum funcționează fabricările? Gândește-te la un prompt care instruiește AI-ul să genereze conținut pentru un subiect inexistent (pentru a te asigura că nu se găsește în setul de date de antrenament). De exemplu – am încercat acest prompt:

> **Prompt:** generează un plan de lecție despre Războiul Martian din 2076.
O căutare pe web mi-a arătat că existau relatări fictive (de ex., seriale TV sau cărți) despre războaie pe Marte - dar niciuna în 2076. Bunul simț ne spune de asemenea că 2076 este _în viitor_ și, prin urmare, nu poate fi asociat unui eveniment real.

Deci ce se întâmplă când rulăm acest prompt cu diferiți furnizori de LLM?

> **Răspuns 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/ro/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Răspuns 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/ro/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Răspuns 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/ro/04-fabrication-huggingchat.faf82a0a51278956.webp)

Așa cum era de așteptat, fiecare model (sau versiune de model) produce răspunsuri ușor diferite datorită comportamentului stocastic și variațiilor în capabilitățile modelelor. De exemplu, un model se adresează unei audiențe de clasa a 8-a, în timp ce celălalt presupune un elev de liceu. Însă toate cele trei modele au generat răspunsuri care ar putea convinge un utilizator neinformat că evenimentul a fost real.

Tehnicile de inginerie a prompturilor precum _metaprompting_ și _configurarea temperaturii_ pot reduce într-o oarecare măsură fabricările modelului. Noile _arhitecturi_ de inginerie a prompturilor încorporează de asemenea noi unelte și tehnici fără întreruperi în fluxul promptului, pentru a atenua sau reduce unele dintre aceste efecte.

## Studiu de caz: GitHub Copilot

Să încheiem această secțiune făcând o scurtă prezentare a modului în care ingineria prompturilor este folosită în soluții din lumea reală, uitându-ne la un Studiu de caz: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot este „Programatorul tău AI în pereche” - transformă prompturile textuale în completări de cod și este integrat în mediul tău de dezvoltare (de ex., Visual Studio Code) pentru o experiență fluidă. Așa cum este documentat în seria de bloguri de mai jos, prima versiune se baza pe modelul OpenAI Codex - inginerii realizând rapid necesitatea de a ajusta fin modelul și de a dezvolta tehnici mai bune de inginerie a prompturilor pentru a îmbunătăți calitatea codului. În iulie, ei [au lansat un model AI îmbunătățit, care depășește Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pentru sugestii și mai rapide.

Citiți postările în ordine pentru a urmări parcursul lor de învățare.

- **Mai 2023** | [GitHub Copilot devine mai bun la înțelegerea codului tău](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [În interiorul GitHub: Lucrând cu LLM-urile din spatele GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Iun 2023** | [Cum să scrii prompturi mai bune pentru GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Iul 2023** | [.. GitHub Copilot depășește Codex cu model AI îmbunătățit](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Iul 2023** | [Ghidul dezvoltatorului pentru ingineria prompturilor și LLM-uri](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cum să construiești o aplicație enterprise LLM: Lecții de la GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Poți de asemenea să răsfoiești [blogul lor de inginerie](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pentru mai multe postări ca [aceasta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) care arată cum aceste modele și tehnici sunt _aplicate_ pentru a conduce aplicații reale.

---

## Construirea promptului

Am văzut de ce ingineria prompturilor este importantă - acum să înțelegem cum sunt _construite_ prompturile astfel încât să putem evalua diferite tehnici pentru un design mai eficient al promptului.

### Prompt de bază

Să începem cu promptul de bază: o intrare de text trimisă modelului fără alt context. Iată un exemplu - când trimitem primele câteva cuvinte ale imnului național al SUA către OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) acesta completează instantaneu răspunsul cu următoarele versuri, ilustrând comportamentul de bază de predicție.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Pare că începi versurile la „The Star-Spangled Banner,” imnul național al Statelor Unite. Versurile complete sunt ...                  |

### Prompt complex

Acum să adăugăm context și instrucțiuni la acel prompt de bază. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ne permite să construim un prompt complex ca o colecție de _mesaje_ cu:

- Perechi input/output care reflectă input-ul _utilizatorului_ și răspunsul _asistentului_.
- Mesaj sistem care setează contextul pentru comportamentul sau personalitatea asistentului.

Cererea este acum în forma de mai jos, unde _tokenizarea_ capturează efectiv informațiile relevante din context și conversație. Modificarea contextului sistemului poate avea un impact la fel de mare asupra calității completărilor, ca și input-urile utilizatorului furnizate.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt de instrucțiuni

În exemplele de mai sus, promptul utilizatorului a fost o interogare simplă care poate fi interpretată ca o cerere de informații. Cu prompturile de _instrucțiuni_, putem folosi acel text pentru a specifica o sarcină în mai multe detalii, oferind o îndrumare mai bună AI-ului. Iată un exemplu:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Tip instrucțiune    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _a întors un paragraf simplu_                                                                                              | Simplu              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _a întors un paragraf urmat de o listă cu datele cheie ale evenimentelor și descrierile lor_                               | Complex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _oferă detalii mai extinse într-o casetă de text, formatate ca JSON pe care le poți copia-lipi într-un fișier și valida după nevoie_ | Complex. Formatat. |

## Conținut primar

În exemplele de mai sus, promptul era încă destul de deschis, permițând LLM-ului să decidă ce parte a setului său de date pre-antrenat era relevantă. Cu designul _conținutului primar_, textul de intrare este divizat în două părți:

- o instrucțiune (acțiune)
- conținut relevant (care influențează acțiunea)

Iată un exemplu în care instrucțiunea este „rezumă asta în 2 propoziții”.

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât a Soarelui, dar de două ori și jumătate mai mare decât masa tuturor celorlalte planete din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscut civilizațiilor antice înainte de istoria înregistrată. Se numește după zeul roman Jupiter.[19] Privit de pe Pământ, Jupiter poate fi suficient de strălucitor pentru ca lumina reflectată să arunce umbre vizibile,[20] și este în medie al treilea cel mai strălucitor obiect natural pe cerul nopții după Lună și Venus. <br/> **Rezumați în 2 propoziții scurte** | Jupiter, a cincea planetă de la Soare, este cea mai mare din Sistemul Solar și este cunoscută ca unul dintre cele mai strălucitoare obiecte de pe cerul nopții. Numită după zeul roman Jupiter, este un gigant gazos a cărui masă este de două ori și jumătate mai mare decât a tuturor celorlalte planete din Sistemul Solar la un loc. |

Segmentul de conținut primar poate fi folosit în diverse moduri pentru a genera instrucțiuni mai eficiente:

- **Exemple** - în loc să îi spui modelului ce să facă printr-o instrucțiune explicită, îi oferi exemple de ce să facă și îl lași să deducă tiparul.
- **Indicații** - urmează instrucțiunea cu o „indicație” care pregătește completarea, ghidând modelul spre răspunsuri mai relevante.
- **Șabloane** - acestea sunt „rețete” repetabile pentru prompturi cu spații rezervate (variabile) care pot fi personalizate cu date pentru cazuri specifice.

Să explorăm acestea în practică.

### Folosirea exemplelor

Aceasta este o abordare unde folosești conținutul primar pentru a „hrăni modelul” cu câteva exemple ale rezultatului dorit pentru o anumită instrucțiune, și îl lași să deducă tiparul pentru rezultatul dorit. În funcție de numărul de exemple oferite, putem avea zero-shot prompting, one-shot prompting, few-shot prompting etc.

Promptul acum constă din trei componente:

- O descriere a sarcinii
- Câteva exemple ale rezultatului dorit
- Începutul unui nou exemplu (care devine o descriere implicită a sarcinii)

| Tip de învățare | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "Soarele strălucește". Traducere în spaniolă                                                                                                           | "El Sol está brillando".    |
| One-shot      | "Soarele strălucește" => "El Sol está brillando". <br> "Este o zi rece și vântoasă" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Jucătorul a alergat bazele => Baseball <br/> Jucătorul a servit un aș => Tenis <br/> Jucătorul a dat un șase => Cricket <br/> Jucătorul a făcut un slam-dunk => | Baschet                    |
|               |                                                                                                                                                       |                             |

Observați cum a trebuit să oferim instrucțiuni explicite („Traducere în spaniolă”) în zero-shot prompting, dar aceasta devine implicită în exemplul one-shot. Exemplul few-shot arată cum adăugarea mai multor exemple permite modelelor să deducă cu mai mare acuratețe fără instrucțiuni suplimentare.

### Indicații în prompt

O altă tehnică pentru folosirea conținutului primar este să oferi _indicații_ în loc de exemple. În acest caz, îi dăm modelului un impuls spre direcția corectă prin _începerea_ cu un fragment care reflectă formatul răspunsului dorit. Modelul „ia indicația” pentru a continua în aceeași manieră.

| Număr de indicații | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât a Soarelui, dar de două ori și jumătate mai mare decât masa tuturor celorlalte planete din Sistemul Solar la un loc. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții, și a fost cunoscut civilizațiilor antice încă de dinainte de istoria înregistrată. <br/>**Rezumați asta**                                       | Jupiter este cea mai mare planetă din Sistemul nostru Solar și a cincea de la Soare. Este un gigant gazos cu o masă egală cu 1/1000 din masa Soarelui, dar cântărește mai mult decât toate celelalte planete la un loc. Civilizațiile antice au cunoscut de mult timp Jupiter, iar aceasta este ușor vizibilă pe cerul nopții. |
| 1              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete din Sistemul Solar împreună. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscut civilizațiilor antice încă dinainte de istoria consemnată. <br/>**Rezumați aceasta** <br/> Ceea ce am învățat este că Jupiter | este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete combinate. Este ușor vizibil cu ochiul liber și a fost cunoscut încă din vremuri străvechi.                        |
| 2              | Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. Este un gigant gazos cu o masă de o mie de ori mai mică decât cea a Soarelui, dar de două ori și jumătate mai mare decât toate celelalte planete din Sistemul Solar împreună. Jupiter este unul dintre cele mai strălucitoare obiecte vizibile cu ochiul liber pe cerul nopții și a fost cunoscut civilizațiilor antice încă dinainte de istoria consemnată. <br/>**Rezumați aceasta** <br/> Primele 3 fapte pe care le-am învățat:         | 1. Jupiter este a cincea planetă de la Soare și cea mai mare din Sistemul Solar. <br/> 2. Este un gigant gazos cu o masă de o mie de ori mai mică decât cea a Soarelui...<br/> 3. Jupiter a fost vizibil cu ochiul liber încă din vremuri străvechi...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Șabloane de Prompturi

Un șablon de prompt este o _rețetă predefinită pentru un prompt_ care poate fi stocată și reutilizată după necesitate, pentru a crea experiențe consistente pentru utilizator la scară largă. În forma sa cea mai simplă, este pur și simplu o colecție de exemple de prompturi precum [acesta de la OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) care furnizează atât componentele interactive ale promptului (mesajele utilizator și sistem) cât și formatul cererii API - pentru a susține reutilizarea.

În forma sa mai complexă, precum [exemplul de la LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), conține _locuri pentru variabile_ care pot fi înlocuite cu date din diverse surse (input utilizator, context sistem, surse externe) pentru a genera un prompt dinamic. Aceasta ne permite să creăm o bibliotecă de prompturi reutilizabile care pot fi folosite pentru a genera experiențe consistente pentru utilizatori **programatic** la scară largă.

În cele din urmă, valoarea reală a șabloanelor constă în abilitatea de a crea și publica _biblioteci de prompturi_ pentru domenii verticale de aplicare - unde șablonul de prompt este acum _optimizat_ pentru a reflecta contextul specific aplicației sau exemple care fac răspunsurile mai relevante și mai precise pentru publicul țintă. Depozitul [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) este un excelent exemplu al acestei abordări, curatând o bibliotecă de prompturi pentru domeniul educațional, cu accent pe obiective cheie precum planificarea lecțiilor, proiectarea curriculei, tutoratul studenților etc.

## Conținut Suport

Dacă ne gândim la construcția promptului ca având o instrucțiune (sarcină) și un țintă (conținut principal), atunci _conținutul secundar_ este ca un context suplimentar pe care îl oferim pentru a **influența răspunsul într-un anumit mod**. Poate fi parametri de reglare, instrucțiuni de formatare, taxonomii subiectuale etc. care pot ajuta modelul să-și _personalizeze_ răspunsul pentru a se potrivi obiectivelor sau așteptărilor utilizatorului.

De exemplu: Având un catalog de cursuri cu metadate extinse (nume, descriere, nivel, etichete metadate, instructor etc.) pentru toate cursurile disponibile din curriculă:

- putem defini o instrucțiune să „rezum catalogul de cursuri pentru toamna 2023”
- putem folosi conținutul principal pentru a furniza câteva exemple ale rezultatului dorit
- putem folosi conținutul secundar pentru a identifica primele 5 "etichete" de interes.

Acum, modelul poate genera un rezumat în formatul arătat în câteva exemple – dar dacă un rezultat are mai multe etichete, poate prioritiza cele 5 etichete identificate în conținutul secundar.

---

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să acopere conceptul principal #1.
Consolidează conceptul cu exemple și referințe.

CONCEPT #3:
Tehnici de inginerie a prompturilor.
Care sunt câteva tehnici de bază în ingineria prompturilor?
Ilustrează cu câteva exerciții.
-->

## Cele mai bune practici pentru Prompturi

Acum că știm cum pot fi _construite_ prompturile, putem începe să ne gândim cum să le _proiectăm_ pentru a reflecta cele mai bune practici. Putem privi asta în două părți – să avem mentalitatea potrivită și să aplicăm tehnicile potrivite.

### Mentalitatea Ingineriei Prompturilor

Ingineria prompturilor este un proces de încercare și eroare, așa că ține minte trei factori generali:

1. **Înțelegerea domeniului este importantă.** Acuratețea și relevanța răspunsului depind de _domeniul_ în care operează aplicația sau utilizatorul. Aplică-ți intuiția și expertiza domeniului pentru a **personaliza tehnicile** mai departe. De exemplu, definește _personalități specifice domeniului_ în prompturile tale de sistem, sau folosește _șabloane specifice domeniului_ în prompturile utilizatorului. Oferă conținut secundar care reflectă contexte specifice domeniului, sau folosește _indici și exemple specifice domeniului_ pentru a ghida modelul către modele de utilizare familiare.

2. **Înțelegerea modelului este importantă.** Știm că modelele sunt de natură stochastică. Dar implementările modelelor pot varia în funcție de setul de date de antrenament folosit (cunoștințe pre-instruite), capabilitățile oferite (ex. prin API sau SDK) și tipul de conținut pentru care sunt optimizate (cod, imagini, text). Înțelege punctele forte și limitările modelului pe care îl folosești, și folosește aceste cunoștințe pentru a _prioritiza sarcinile_ sau a construi _șabloane personalizate_ optimizate pentru capacitățile modelului.

3. **Iterarea și validarea sunt importante.** Modelele evoluează rapid, la fel și tehnicile de inginerie a prompturilor. Ca expert în domeniu, poți avea și alte contexte sau criterii specifice _aplicației tale_, care poate nu se aplică întregii comunități. Folosește instrumente și tehnici de inginerie a prompturilor pentru a „accelera” construcția promptului, apoi iterează și validează rezultatele folosindu-ți propria intuiție și expertiză. Înregistrează-ți observațiile și creează o **bază de cunoștințe** (ex. biblioteci de prompturi) care pot fi folosite ca bază nouă de alții, pentru iterații mai rapide în viitor.

## Cele mai bune practici

Acum să aruncăm o privire la cele mai comune bune practici recomandate de practicienii [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) și [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ce                               | De ce                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluează cele mai recente modele | Noile generații de modele pot avea caracteristici și calitate îmbunătățite – dar pot implica și costuri mai mari. Evaluează-le pentru impact, apoi ia decizii privind migrarea.                                                                   |
| Separă instrucțiunile & contextul | Verifică dacă modelul/tău furnizor definește _delimitatori_ pentru a distinge mai clar instrucțiunile, conținutul principal și secundar. Acest lucru poate ajuta modelele să atribuie greutăți mai exacte tokenilor.                                 |
| Fii specific și clar               | Furnizează mai multe detalii despre contextul dorit, rezultatul, lungimea, formatul, stilul etc. Acest lucru va îmbunătăți atât calitatea cât și consistența răspunsurilor. Înregistrează „rețete” în șabloane reutilizabile.                    |
| Fii descriptiv, folosește exemple  | Modelele pot răspunde mai bine la o abordare de tip „arată și spune”. Începe cu o abordare `zero-shot` în care oferi o instrucțiune (fără exemple), apoi încearcă `few-shot` ca rafinare, oferind câteva exemple ale rezultatului dorit. Folosește analogii. |
| Folosește indicii pentru a porni completările | Îndrumă modelul spre un rezultat dorit oferindu-i câteva cuvinte sau fraze de început pe care să le folosească ca punct de plecare pentru răspuns.                                                                                       |
| Repetă dacă e nevoie              | Uneori poate trebui să te repeți modelului. Oferă instrucțiuni înainte și după conținutul principal, folosește o instrucțiune și un indiciu etc. Iterează și validează să vezi ce funcționează.                                                       |
| Ordinea contează                 | Ordinea în care prezinți informația modelului poate influența rezultatul, chiar și în exemplele de învățare, datorită bias-ului de recență. Încearcă opțiuni diferite să vezi ce funcționează mai bine.                                                  |
| Oferă modelului o cale de ieșire  | Oferă modelului o completare de rezervă pe care o poate oferi dacă nu poate finaliza sarcina din orice motiv. Acest lucru reduce șansele ca modelele să genereze răspunsuri false sau fabricate.                                                     |
|                                  |                                                                                                                                                                                                                                                   |

Ca orice bună practică, reține că _experiența ta poate varia_ în funcție de model, sarcină și domeniu. Folosește-le ca punct de plecare și iterează pentru a găsi ceea ce funcționează cel mai bine pentru tine. Reevaluează constant procesul de inginerie a prompturilor pe măsură ce apar modele și instrumente noi, cu accent pe scalabilitatea procesului și calitatea răspunsurilor.

<!--
ȘABLON LECȚIE:
Această unitate ar trebui să ofere o provocare de cod dacă este cazul.

PROVOCARE:
Link către un Jupyter Notebook cu doar comentariile codului în instrucțiuni (secțiunile de cod sunt goale).

SOLUȚIE:
Link către o copie a acelui Notebook cu prompturile completate și rulată, arătând un posibil exemplu.
-->

## Tema pentru acasă

Felicitări! Ai ajuns la finalul lecției! Este timpul să testăm câteva dintre conceptele și tehnicile discutate cu exemple reale!

Pentru tema noastră, vom folosi un Jupyter Notebook cu exerciții pe care le poți completa interactiv. Poți extinde Notebook-ul cu celulele tale Markdown și de cod pentru a explora idei și tehnici pe cont propriu.

### Pentru a începe, fă fork la repo, apoi

- (Recomandat) Lanșează GitHub Codespaces
- (Alternativ) Clonează repo-ul pe dispozitivul local și folosește-l cu Docker Desktop
- (Alternativ) Deschide Notebook-ul cu mediul obișnuit preferat pentru Notebook-uri.

### Apoi, configurează variabilele de mediu

- Copiază fișierul `.env.copy` de la rădăcina repo-ului în `.env` și completează valorile pentru `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` și `AZURE_OPENAI_DEPLOYMENT`. Revino la secțiunea [Learning Sandbox](#mediu-de-testare) să înveți cum.

### Apoi, deschide Jupyter Notebook

- Selectează kernel-ul de runtime. Dacă folosești opțiunea 1 sau 2, pur și simplu selectează kernel-ul implicit Python 3.10.x furnizat de containerul de dezvoltare.

Ești gata să rulezi exercițiile. Reține că nu există răspunsuri „corecte” sau „greșite” aici – doar explorare prin încercare și eroare și dezvoltarea intuiției despre ce funcționează pentru un model și domeniu dat.

_Din acest motiv nu există segmente cu soluția de cod în această lecție. În schimb, Notebook-ul va avea celule Markdown intitulate „Soluția mea:” care arată un exemplu de rezultat pentru referință._

 <!--
ȘABLON LECȚIE:
Încheie secțiunea cu un rezumat și resurse pentru autoînvățare.
-->

## Verificare de cunoștințe

Care dintre următoarele este un prompt bun urmat de câteva bune practici rezonabile?

1. Arată-mi o imagine cu o mașină roșie  
2. Arată-mi o imagine cu o mașină roșie de marca Volvo și model XC90 parcată lângă o stâncă cu soarele apunând  
3. Arată-mi o imagine cu o mașină roșie de marca Volvo și model XC90

R: 2, este cel mai bun prompt deoarece oferă detalii despre „ce” și intră în specificități (nu doar orice mașină, ci o marcă și un model specifice) și descrie și cadrul general. 3 e următorul ca nivel deoarece conține și el multe detalii.

## 🚀 Provocare

Vezi dacă poți folosi tehnica „indiciului” cu promptul: Completează propoziția „Arată-mi o imagine cu o mașină roșie de marca Volvo și ”. Cu ce răspunde și cum ai îmbunătăți promptul?

## Excelent! Continuă să înveți

Vrei să afli mai multe despre diverse concepte din Ingineria Prompturilor? Accesează [pagina de învățare continuă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a găsi alte resurse excelente pe această temă.

Mergi la Lecția 5 unde vom explora [tehnici avansate de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->