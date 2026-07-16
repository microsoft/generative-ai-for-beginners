# Construirea Aplicațiilor de Chat Bazate pe AI Generativ

[![Construirea Aplicațiilor de Chat Bazate pe AI Generativ](../../../translated_images/ro/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Acum că am văzut cum putem construi aplicații de generare a textului, să analizăm aplicațiile de chat.

Aplicațiile de chat au devenit integrate în viața noastră de zi cu zi, oferind mai mult decât un simplu mijloc de conversație ocazională. Ele sunt părți integrante ale serviciului clienți, suportului tehnic și chiar ale sistemelor sofisticate de consultanță. Probabil că ai primit recent ajutor de la o aplicație de chat. Pe măsură ce integrăm tehnologii mai avansate precum AI generativ în aceste platforme, complexitatea crește, la fel și provocările.

Unele întrebări la care trebuie să răspundem sunt:

- **Construirea aplicației**. Cum construim eficient și integrăm perfect aceste aplicații alimentate de AI pentru cazuri de utilizare specifice?
- **Monitorizarea**. Odată implementate, cum putem monitoriza și asigura că aplicațiile funcționează la cel mai înalt nivel de calitate, atât din punct de vedere funcțional, cât și în conformitate cu [cele șase principii ale AI responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Pe măsură ce înaintează epoca definită de automatizare și interacțiuni fluide om-mașină, înțelegerea modului în care AI-ul generativ transformă domeniul, profunzimea și adaptabilitatea aplicațiilor de chat devine esențială. Această lecție va investiga aspectele arhitecturale care susțin aceste sisteme complexe, va explora metodologiile pentru ajustarea fină a lor pentru sarcini specifice domeniului și va evalua metricile și considerațiile relevante pentru asigurarea implementării responsabile a AI.

## Introducere

Această lecție acoperă:

- Tehnici pentru construirea și integrarea eficientă a aplicațiilor de chat.
- Cum să aplici personalizarea și ajustarea fină în aplicații.
- Strategii și considerații pentru monitorizarea eficientă a aplicațiilor de chat.

## Obiectivele de Învățare

Până la finalul acestei lecții, vei putea să:

- Descrii considerațiile pentru construirea și integrarea aplicațiilor de chat în sisteme existente.
- Personalizezi aplicațiile de chat pentru cazuri de utilizare specifice.
- Identifici metricile cheie și considerațiile pentru a monitoriza și menține eficient calitatea aplicațiilor de chat alimentate de AI.
- Asiguri utilizarea responsabilă a AI în aplicațiile de chat.

## Integrarea AI Generativ în Aplicațiile de Chat

Îmbunătățirea aplicațiilor de chat prin AI generativ nu este doar despre a le face mai inteligente; este despre optimizarea arhitecturii, performanței și interfeței cu utilizatorul pentru a oferi o experiență de calitate. Aceasta implică investigarea fundamentelor arhitecturale, integrarea API-urilor și considerații referitoare la interfața utilizatorului. Această secțiune își propune să ofere o foaie de parcurs cuprinzătoare pentru navigarea pe aceste terenuri complexe, fie că le introduci în sisteme existente, fie că le construiești ca platforme independente.

La finalul acestei secțiuni, vei dispune de expertiza necesară pentru a construi eficient și a încorpora aplicații de chat.

### Chatbot sau Aplicație de Chat?

Înainte să ne apucăm de construirea aplicațiilor de chat, să comparăm „chatbot-urile” cu „aplicațiile de chat alimentate de AI,” care servesc roluri și funcționalități distincte. Scopul principal al unui chatbot este de a automatiza sarcini conversaționale specifice, cum ar fi răspunsul la întrebări frecvente sau urmărirea unui colet. De obicei, este guvernat de o logică bazată pe reguli sau algoritmi AI complexi. În contrast, o aplicație de chat alimentată de AI generativ este un mediu mult mai larg, conceput pentru a facilita diverse forme de comunicare digitală, cum ar fi chat text, voce și video între utilizatori umani. Caracteristica sa definitorie este integrarea unui model AI generativ care simulează conversații nuanțate, asemănătoare celor umane, generând răspunsuri bazate pe o gamă largă de intrări și indicii contextuale. O aplicație de chat alimentată de AI generativ poate purta discuții open-domain, se poate adapta la contexte conversaționale în evoluție și chiar poate produce dialog creativ sau complex.

Tabelul de mai jos evidențiază principalele diferențe și asemănări pentru a înțelege rolurile lor unice în comunicarea digitală.

| Chatbot                               | Aplicație de Chat Bazată pe AI Generativ                         |
| ------------------------------------- | -------------------------------------- |
| Orientat spre sarcini și bazat pe reguli | Conștient de context                                         |
| De multe ori integrat în sisteme mai mari | Poate găzdui unul sau mai multe chatbot-uri                  |
| Limitat la funcții programate           | Încorporează modele AI generative                             |
| Interacțiuni specializate și structurate | Capabil de discuții open-domain                                |

### Folosirea funcționalităților predefinite prin SDK-uri și API-uri

Când construiești o aplicație de chat, un prim pas excelent este să evaluezi ce există deja. Utilizarea SDK-urilor și API-urilor pentru a construi aplicații de chat este o strategie avantajoasă din mai multe motive. Prin integrarea SDK-urilor și API-urilor bine documentate, poziționezi strategic aplicația pentru succes pe termen lung, abordând preocupările privind scalabilitatea și întreținerea.

- **Accelerează procesul de dezvoltare și reduce efortul**: Bazarea pe funcționalități preconstruite în locul construirii costisitoare a acestora îți permite să te concentrezi pe alte aspecte ale aplicației pe care le consideri mai importante, cum ar fi logica de afaceri.
- **Performanță mai bună**: Construind funcționalitatea de la zero, te vei întreba în cele din urmă „Cum se scalează? Este această aplicație capabilă să gestioneze un aflux brusc de utilizatori?” SDK-urile și API-urile bine întreținute oferă adesea soluții integrate pentru aceste probleme.
- **Întreținere mai ușoară**: Actualizările și îmbunătățirile sunt mai ușor de gestionat deoarece majoritatea API-urilor și SDK-urilor necesită doar actualizarea unei biblioteci când apare o versiune nouă.
- **Acces la tehnologie de ultimă generație**: Folosirea modelelor care au fost optimizate și antrenate pe seturi extinse de date oferă aplicației tale capacități avansate de procesare a limbajului natural.

Accesarea funcționalității unui SDK sau API implică de obicei obținerea permisiunii de a utiliza serviciile oferite, adesea printr-o cheie unică sau un token de autentificare. Vom folosi Biblioteca Python OpenAI pentru a explora cum arată acest proces. Poți încerca și tu în [notebook-ul pentru OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) sau în [notebook-ul pentru Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) aferent acestei lecții.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Exemplul de mai sus folosește modelul GPT-5 mini cu API-ul Responses pentru a completa încurajarea, dar observă că cheia API este setată înainte de aceasta. Ai primi o eroare dacă nu ai seta cheia.

## Experiența Utilizatorului (UX)

Principiile generale de UX se aplică aplicațiilor de chat, dar iată câteva considerații suplimentare care devin deosebit de importante datorită componentelor de învățare automată implicate.

- **Mecanism pentru rezolvarea ambiguității**: Modelele AI generative uneori generează răspunsuri ambigue. O funcție care permite utilizatorilor să ceară clarificări poate fi utilă dacă se întâlnesc cu această problemă.
- **Reținerea contextului**: Modelele AI generative avansate au capacitatea de a memora contextul în cadrul unei conversații, ceea ce poate fi un atu necesar pentru experiența utilizatorului. Oferirea utilizatorilor posibilitatea de a controla și gestiona contextul îmbunătățește experiența, dar introduce riscul de reținere a informațiilor sensibile. Considerațiile privind durata stocării acestor informații, cum ar fi introducerea unei politici de retenție, pot echilibra necesitatea contextului cu confidențialitatea.
- **Personalizarea**: Cu abilitatea de a învăța și adapta, modelele AI oferă o experiență individualizată utilizatorului. Adaptarea experienței utilizatorului prin funcții precum profilurile utilizatorilor nu doar că îl face pe utilizator să se simtă înțeles, dar ajută și în găsirea de răspunsuri specifice, creând o interacțiune mai eficientă și satisfăcătoare.

Un astfel de exemplu de personalizare este setarea „Instrucțiuni personalizate” în ChatGPT de la OpenAI. Aceasta îți permite să furnizezi informații despre tine care pot fi un context important pentru solicitările tale. Iată un exemplu de instrucțiune personalizată.

![Setări Instrucțiuni Personalizate în ChatGPT](../../../translated_images/ro/custom-instructions.b96f59aa69356fcf.webp)

Acest „profil” îl determină pe ChatGPT să creeze un plan de lecție despre liste înlănțuite. Observă că ChatGPT ia în considerare că utilizatorul ar putea dori un plan de lecție mai detaliat bazat pe experiența sa.

![O solicitare în ChatGPT pentru un plan de lecție despre liste înlănțuite](../../../translated_images/ro/lesson-plan-prompt.cc47c488cf1343df.webp)

### Cadrul Sistemului de Mesaje Microsoft pentru Modelele Mari de Limbaj

[Microsoft a oferit îndrumări](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) pentru scrierea unor mesaje de sistem eficiente când generează răspunsuri din LLM-uri, grupate în 4 domenii:

1. Definirea pentru cine este modelul, precum și capabilitățile și limitările acestuia.
2. Definirea formatului de ieșire al modelului.
3. Oferirea de exemple specifice care demonstrează comportamentul dorit al modelului.
4. Oferirea de reguli suplimentare de comportament.

### Accesibilitate

Indiferent dacă un utilizator are deficiențe vizuale, auditive, motorii sau cognitive, o aplicație de chat bine proiectată ar trebui să fie utilizabilă de către toți. Lista următoare detaliază caracteristici specifice menite să îmbunătățească accesibilitatea pentru diverse deficiențe ale utilizatorilor.

- **Caracteristici pentru deficiențe vizuale**: Teme cu contrast înalt și text redimensionabil, compatibilitate cu cititoarele de ecran.
- **Caracteristici pentru deficiențe auditive**: Funcții text-vorbire și vorbire-text, indicatoare vizuale pentru notificările audio.
- **Caracteristici pentru deficiențe motorii**: Suport pentru navigare cu tastatura, comenzi vocale.
- **Caracteristici pentru deficiențe cognitive**: Opțiuni de limbaj simplificat.

## Personalizare și Ajustare Fină pentru Modele de Limbaj Domain-Specifice

Imaginează-ți o aplicație de chat care înțelege jargonul companiei tale și anticipează întrebările specifice pe care baza ta de utilizatori le are frecvent. Există câteva abordări demne de menționat:

- **Folosirea modelelor DSL**. DSL înseamnă limbaj specific domeniului. Poți utiliza un așa-numit model DSL antrenat pe un domeniu specific pentru a înțelege conceptele și scenariile acestuia.
- **Aplicarea ajustării fine**. Ajustarea fină este procesul de antrenare suplimentară a modelului cu date specifice.

## Personalizare: Folosirea unui DSL

Folosirea modelelor de limbaj specifice domeniului (Model DSL) poate spori implicarea utilizatorului prin oferirea de interacțiuni specializate, relevante contextului. Este un model antrenat sau ajustat fin pentru a înțelege și genera text legat de un domeniu, industrie sau subiect specific. Opțiunile pentru utilizarea unui model DSL pot varia de la antrenarea unuia de la zero, la folosirea celor preexistente prin SDK-uri și API-uri. O altă opțiune este ajustarea fină, care implică luarea unui model pre-antrenat existent și adaptarea sa pentru un domeniu specific.

## Personalizare: Aplicarea ajustării fine

Ajustarea fină este frecvent luată în considerare atunci când un model pre-antrenat este insuficient într-un domeniu specializat sau pentru o sarcină specifică.

De exemplu, întrebările medicale sunt complexe și necesită mult context. Când un profesionist medical diagnostică un pacient, se bazează pe o varietate de factori precum stilul de viață sau condițiile preexistente, și poate chiar folosi jurnale medicale recente pentru a-și valida diagnosticul. În astfel de scenarii nuanțate, o aplicație de chat AI cu scop general nu poate fi o sursă de încredere.

### Scenariu: o aplicație medicală

Gândește-te la o aplicație de chat concepută să asiste practicienii medicali prin oferirea de referințe rapide la ghiduri de tratament, interacțiuni medicamentoase sau descoperiri de cercetare recente.

Un model cu scop general ar putea fi adecvat pentru răspunsuri la întrebări medicale de bază sau oferirea de sfaturi generale, dar ar putea întâmpina dificultăți în următoarele situații:

- **Cazuri foarte specifice sau complexe**. De exemplu, un neurolog ar putea întreba aplicația, „Care sunt cele mai bune practici actuale pentru gestionarea epilepsiei rezistente la medicamente la pacienții pediatrici?”
- **Lipsa de avansuri recente**. Un model general ar putea avea dificultăți să ofere un răspuns actualizat care să includă cele mai recente avansuri în neurologie și farmacologie.

În astfel de cazuri, ajustarea fină a modelului cu un set de date medicale specializate poate îmbunătăți semnificativ capacitatea acestuia de a gestiona aceste întrebări medicale complexe cu acuratețe și fiabilitate. Aceasta necesită acces la un set mare și relevant de date care să reprezinte provocările și întrebările specifice domeniului ce trebuie abordate.

## Considerații pentru o Experiență de Chat AI de Înaltă Calitate

Această secțiune descrie criteriile pentru aplicațiile de chat „de înaltă calitate”, care includ capturarea metricelor acționabile și respectarea unui cadru care folosește responsabil tehnologia AI.

### Metrici Cheie

Pentru a menține performanța de înaltă calitate a unei aplicații, este esențial să urmărim metricile și considerațiile cheie. Aceste măsurători nu doar asigură funcționalitatea aplicației, ci și evaluează calitatea modelului AI și experiența utilizatorului. Mai jos este o listă ce acoperă metricile de bază, cele AI și ale experienței utilizatorului de luat în considerare.

| Metrica                      | Definiție                                                                                                             | Considerații pentru Dezvoltatorul Chat                                |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Timp de funcționare (Uptime)** | Măsoară perioada în care aplicația este operațională și accesibilă utilizatorilor.                                      | Cum vei minimiza timpul de nefuncționare?                            |
| **Timp de răspuns**           | Timpul necesar aplicației pentru a răspunde la o interogare a utilizatorului.                                           | Cum poți optimiza procesarea interogărilor pentru a îmbunătăți timpul de răspuns? |
| **Precizie**                  | Raportul predicțiilor corecte pozitive față de numărul total de predicții pozitive.                                    | Cum vei valida precizia modelului tău?                               |
| **Recall (Sensibilitate)**    | Raportul predicțiilor corecte pozitive față de numărul real de cazuri pozitive.                                        | Cum vei măsura și îmbunătăți recall-ul?                             |
| **Scor F1**                  | Media armonică a preciziei și recall-ului, care echilibrează compromisurile dintre cele două.                          | Care este scorul F1 țintă? Cum vei echilibra precizia și recall-ul?  |
| **Perplexitate**             | Măsoară cât de bine se aliniază distribuția probabilistică prezisă de model cu distribuția reală a datelor.           | Cum vei minimiza perplexitatea?                                     |
| **Metrici de satisfacție a utilizatorului** | Măsoară percepția utilizatorului asupra aplicației. Deseori capturate prin sondaje.                                   | Cât de des vei colecta feedback de la utilizatori? Cum te vei adapta pe baza acestuia?   |
| **Rata erorilor**            | Rata la care modelul face greșeli în înțelegere sau în rezultat.                                                       | Ce strategii ai pentru a reduce rata erorilor?                       |
| **Cicluri de reantrenare**  | Frecvența cu care modelul este actualizat pentru a include date și informații noi.                                   | Cât de des vei reantrena modelul? Ce declanșează un ciclu de reantrenare?               |

| **Detectarea Anomaliilor**         | Instrumente și tehnici pentru identificarea tiparelor neobișnuite care nu corespund comportamentului așteptat.                        | Cum veți răspunde la anomalii?                                        |

### Implementarea practicilor de Inteligență Artificială Responsabilă în aplicațiile de chat

Abordarea Microsoft pentru Inteligența Artificială Responsabilă a identificat șase principii care ar trebui să ghideze dezvoltarea și utilizarea AI. Mai jos sunt principiile, definiția lor și aspectele pe care un dezvoltator de chat ar trebui să le ia în considerare și de ce ar trebui să le abordeze cu seriozitate.

| Principii             | Definiția Microsoft                                | Considerații pentru Dezvoltatorul de Chat                                      | De ce este important                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Echitate               | Sistemele AI ar trebui să trateze toți oamenii în mod echitabil.            | Asigurați-vă că aplicația de chat nu discriminează pe baza datelor utilizatorului.  | Pentru a construi încredere și incluziune între utilizatori; evită implicațiile legale.                |
| Fiabilitate și Siguranță | Sistemele AI ar trebui să funcționeze în mod fiabil și sigur.        | Implementați teste și mecanisme de siguranță pentru a minimiza erorile și riscurile.         | Asigură satisfacția utilizatorilor și previne eventuale daune.                                 |
| Confidențialitate și Securitate   | Sistemele AI ar trebui să fie securizate și să respecte confidențialitatea.      | Implementați criptare puternică și măsuri de protecție a datelor.              | Pentru a proteja datele sensibile ale utilizatorilor și a respecta legile privind confidențialitatea.                         |
| Incluziune          | Sistemele AI ar trebui să dea putere tuturor și să implice oamenii. | Proiectați interfața și experiența utilizatorului astfel încât să fie accesibilă și ușor de folosit pentru diverse audiențe. | Asigură că un număr mai mare de persoane poate folosi eficient aplicația.                   |
| Transparență           | Sistemele AI ar trebui să fie înțelese.                  | Oferiți documentație clară și justificări pentru răspunsurile AI.            | Utilizatorii au mai multe șanse să aibă încredere într-un sistem dacă pot înțelege cum sunt luate deciziile. |
| Responsabilitate         | Oamenii ar trebui să fie responsabili pentru sistemele AI.          | Stabiliți un proces clar pentru auditarea și îmbunătățirea deciziilor AI.     | Permite îmbunătățirea continuă și măsuri corective în cazul greșelilor.               |

## Tema

Consultați [tema](../../../07-building-chat-applications/python). Aceasta vă va ghida printr-o serie de exerciții, de la rularea primelor promturi de chat, clasificarea și rezumarea textului și multe altele. Observați că temele sunt disponibile în diferite limbaje de programare!

## Excelent! Continuați călătoria

După ce ați terminat această lecție, verificați colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să vă dezvoltați cunoștințele despre Inteligența Artificială Generativă!

Mergeți la Lecția 8 pentru a vedea cum puteți începe să [construiți aplicații de căutare](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->