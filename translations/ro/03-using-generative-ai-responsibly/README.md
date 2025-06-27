<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:32:49+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "ro"
}
-->
# Utilizarea AI Generativ în Mod Responsabil

> _Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții_

Este ușor să fii fascinat de AI și, în special, de AI generativ, dar trebuie să iei în considerare cum să îl folosești în mod responsabil. Trebuie să te gândești la aspecte precum cum să te asiguri că rezultatul este corect, nepericulos și multe altele. Acest capitol își propune să îți ofere contextul menționat, ce să iei în considerare și cum să faci pași activi pentru a îmbunătăți utilizarea AI.

## Introducere

Această lecție va acoperi:

- De ce ar trebui să prioritizezi AI Responsabil atunci când construiești aplicații de AI Generativ.
- Principiile de bază ale AI Responsabil și cum se relaționează cu AI Generativ.
- Cum să pui aceste principii de AI Responsabil în practică prin strategie și unelte.

## Obiective de Învățare

După completarea acestei lecții vei ști:

- Importanța AI Responsabil atunci când construiești aplicații de AI Generativ.
- Când să te gândești și să aplici principiile de bază ale AI Responsabil atunci când construiești aplicații de AI Generativ.
- Ce unelte și strategii sunt disponibile pentru a pune în practică conceptul de AI Responsabil.

## Principiile AI Responsabil

Entuziasmul pentru AI Generativ nu a fost niciodată mai mare. Acest entuziasm a adus mulți noi dezvoltatori, atenție și finanțare în acest domeniu. Deși acest lucru este foarte pozitiv pentru oricine dorește să construiască produse și companii folosind AI Generativ, este de asemenea important să procedăm responsabil.

Pe parcursul acestui curs, ne concentrăm pe construirea startup-ului nostru și a produsului nostru educațional AI. Vom folosi principiile AI Responsabil: Corectitudine, Incluziune, Fiabilitate/Siguranță, Securitate & Confidențialitate, Transparență și Responsabilitate. Cu aceste principii, vom explora cum se relaționează cu utilizarea AI Generativ în produsele noastre.

## De ce Ar Trebui să Prioritizezi AI Responsabil

Când construiești un produs, adoptarea unei abordări centrate pe om, având în vedere cel mai bun interes al utilizatorului, duce la cele mai bune rezultate.

Unicitatea AI Generativ constă în puterea sa de a crea răspunsuri utile, informații, îndrumări și conținut pentru utilizatori. Acest lucru se poate face fără multe etape manuale, ceea ce poate duce la rezultate foarte impresionante. Fără planificare și strategii adecvate, din păcate, poate duce și la unele rezultate dăunătoare pentru utilizatorii tăi, produsul tău și societatea în ansamblu.

Să ne uităm la unele (dar nu toate) dintre aceste rezultate potențial dăunătoare:

### Halucinații

Halucinațiile sunt un termen folosit pentru a descrie când un LLM produce conținut care este fie complet fără sens, fie ceva despre care știm că este greșit din punct de vedere factual pe baza altor surse de informații.

Să luăm, de exemplu, construim o funcție pentru startup-ul nostru care permite studenților să pună întrebări istorice unui model. Un student pune întrebarea `Who was the sole survivor of Titanic?`

Modelul produce un răspuns precum cel de mai jos:

Aceasta este un răspuns foarte încrezător și detaliat. Din păcate, este incorect. Chiar și cu o cantitate minimă de cercetare, cineva ar descoperi că au fost mai mulți supraviețuitori ai dezastrului Titanic. Pentru un student care abia începe să cerceteze acest subiect, acest răspuns poate fi suficient de convingător pentru a nu fi pus sub semnul întrebării și tratat ca fapt. Consecințele acestui lucru pot duce la faptul că sistemul AI este nesigur și afectează negativ reputația startup-ului nostru.

Cu fiecare iterație a unui LLM dat, am văzut îmbunătățiri ale performanței în ceea ce privește minimizarea halucinațiilor. Chiar și cu această îmbunătățire, noi, ca dezvoltatori de aplicații și utilizatori, trebuie să rămânem conștienți de aceste limitări.

### Conținut Dăunător

Am acoperit în secțiunea anterioară când un LLM produce răspunsuri incorecte sau fără sens. Un alt risc de care trebuie să fim conștienți este când un model răspunde cu conținut dăunător.

Conținutul dăunător poate fi definit ca:

- Oferirea de instrucțiuni sau încurajarea auto-vătămării sau vătămării anumitor grupuri.
- Conținut urăcios sau denigrator.
- Ghidarea planificării oricărui tip de atac sau acte violente.
- Oferirea de instrucțiuni despre cum să găsești conținut ilegal sau să comiți acte ilegale.
- Afișarea conținutului explicit sexual.

Pentru startup-ul nostru, vrem să ne asigurăm că avem uneltele și strategiile corecte pentru a preveni ca acest tip de conținut să fie văzut de studenți.

### Lipsa Corectitudinii

Corectitudinea este definită ca "asigurarea că un sistem AI este liber de prejudecăți și discriminare și că tratează pe toată lumea corect și egal." În lumea AI Generativ, vrem să ne asigurăm că viziunile exclusioniste ale grupurilor marginalizate nu sunt întărite de rezultatul modelului.

Aceste tipuri de rezultate nu sunt doar distructive pentru construirea unor experiențe pozitive ale produsului pentru utilizatorii noștri, dar cauzează și daune sociale suplimentare. Ca dezvoltatori de aplicații, ar trebui să avem mereu în minte o bază largă și diversă de utilizatori atunci când construim soluții cu AI Generativ.

## Cum să Folosești AI Generativ în Mod Responsabil

Acum că am identificat importanța AI Generativ Responsabil, să vedem 4 pași pe care îi putem face pentru a construi soluțiile noastre AI în mod responsabil:

### Măsurarea Posibilelor Daune

În testarea software, testăm acțiunile așteptate ale unui utilizator pe o aplicație. În mod similar, testarea unui set divers de solicitări pe care utilizatorii sunt cel mai probabil să le folosească este o modalitate bună de a măsura posibilele daune.

Deoarece startup-ul nostru construiește un produs educațional, ar fi bine să pregătim o listă de solicitări legate de educație. Acestea ar putea acoperi un anumit subiect, fapte istorice și solicitări despre viața de student.

### Atenuarea Posibilelor Daune

Este acum momentul să găsim modalități prin care putem preveni sau limita daunele potențiale cauzate de model și de răspunsurile sale. Putem privi acest lucru în 4 straturi diferite:

- **Model**. Alegerea modelului potrivit pentru cazul de utilizare potrivit. Modele mai mari și mai complexe, cum ar fi GPT-4, pot cauza mai multe riscuri de conținut dăunător atunci când sunt aplicate la cazuri de utilizare mai mici și mai specifice. Utilizarea datelor de antrenament pentru ajustare fină reduce, de asemenea, riscul de conținut dăunător.

- **Sistem de Siguranță**. Un sistem de siguranță este un set de unelte și configurații pe platforma care servește modelul, care ajută la atenuarea daunelor. Un exemplu este sistemul de filtrare a conținutului pe serviciul Azure OpenAI. Sistemele ar trebui să detecteze și atacurile de jailbreak și activitatea nedorită, cum ar fi cererile de la roboți.

- **Metaprompt**. Metaprompturile și fundamentarea sunt modalități prin care putem direcționa sau limita modelul pe baza anumitor comportamente și informații. Acest lucru ar putea fi utilizarea de intrări de sistem pentru a defini anumite limite ale modelului. În plus, oferirea de rezultate mai relevante pentru domeniul sau scopul sistemului.

Poate fi, de asemenea, utilizarea tehnicilor precum Generarea Augmentată de Recuperare (RAG) pentru a face ca modelul să extragă informații doar dintr-o selecție de surse de încredere. Există o lecție mai târziu în acest curs pentru [construirea aplicațiilor de căutare](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiența Utilizatorului**. Stratul final este unde utilizatorul interacționează direct cu modelul prin interfața aplicației noastre într-un anumit mod. În acest fel, putem proiecta UI/UX pentru a limita utilizatorul la tipurile de intrări pe care le pot trimite modelului, precum și textul sau imaginile afișate utilizatorului. Când lansăm aplicația AI, trebuie să fim, de asemenea, transparenți cu privire la ceea ce poate și nu poate face aplicația noastră de AI Generativ.

Avem o lecție întreagă dedicată [Proiectării UX pentru Aplicații AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluarea modelului**. Lucrul cu LLM-urile poate fi provocator deoarece nu avem întotdeauna control asupra datelor pe care modelul a fost antrenat. Indiferent, ar trebui să evaluăm întotdeauna performanța și rezultatele modelului. Este încă important să măsurăm acuratețea, similitudinea, fundamentarea și relevanța rezultatului modelului. Acest lucru ajută la oferirea de transparență și încredere părților interesate și utilizatorilor.

### Operarea unei soluții de AI Generativ Responsabil

Construirea unei practici operaționale în jurul aplicațiilor tale AI este etapa finală. Acest lucru include colaborarea cu alte părți ale startup-ului nostru, cum ar fi Legal și Securitate, pentru a ne asigura că suntem conformi cu toate politicile de reglementare. Înainte de lansare, dorim să construim planuri în jurul livrării, gestionării incidentelor și rollback-ului pentru a preveni orice daune pentru utilizatorii noștri de la creștere.

## Unelte

Deși munca de dezvoltare a soluțiilor de AI Responsabil poate părea multă, este o muncă bine meritată. Pe măsură ce domeniul AI Generativ crește, mai multe unelte pentru a ajuta dezvoltatorii să integreze eficient responsabilitatea în fluxurile lor de lucru vor maturiza. De exemplu, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) poate ajuta la detectarea conținutului și imaginilor dăunătoare printr-o cerere API.

## Verificarea Cunoștințelor

Care sunt unele lucruri de care trebuie să te îngrijești pentru a asigura utilizarea responsabilă a AI?

1. Că răspunsul este corect.
1. Utilizare dăunătoare, că AI nu este folosit în scopuri criminale.
1. Asigurarea că AI este liber de prejudecăți și discriminare.

A: 2 și 3 sunt corecte. AI Responsabil te ajută să iei în considerare cum să atenuezi efectele dăunătoare și prejudecățile și mai mult.

## 🚀 Provocare

Citește despre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) și vezi ce poți adopta pentru utilizarea ta.

## Felicitări, Continuă Învățarea

După ce ai completat această lecție, verifică colecția noastră de [Învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți dezvolți cunoștințele despre AI Generativ!

Mergi la Lecția 4 unde vom analiza [Fundamentele Ingineriei Solicitărilor](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să obținem acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem responsabili pentru niciun fel de neînțelegeri sau interpretări greșite care apar din utilizarea acestei traduceri.