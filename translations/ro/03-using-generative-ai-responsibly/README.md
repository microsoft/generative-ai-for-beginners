<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T22:06:14+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "ro"
}
-->
# Utilizarea AI Generativ în mod responsabil

[![Utilizarea AI Generativ în mod responsabil](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.ro.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții_

Este ușor să fii fascinat de AI și, în special, de AI generativ, dar trebuie să te gândești cum să îl folosești în mod responsabil. Trebuie să iei în considerare aspecte precum asigurarea că rezultatele sunt corecte, non-nocive și multe altele. Acest capitol își propune să îți ofere contextul menționat, ce să iei în considerare și cum să faci pași activi pentru a îmbunătăți utilizarea AI.

## Introducere

Această lecție va acoperi:

- De ce ar trebui să prioritizezi AI Responsabil atunci când construiești aplicații de AI Generativ.
- Principiile de bază ale AI Responsabil și cum se raportează acestea la AI Generativ.
- Cum să aplici aceste principii ale AI Responsabil prin strategii și instrumente.

## Obiective de învățare

După finalizarea acestei lecții vei ști:

- Importanța AI Responsabil atunci când construiești aplicații de AI Generativ.
- Când să te gândești și să aplici principiile de bază ale AI Responsabil în construirea aplicațiilor de AI Generativ.
- Ce instrumente și strategii sunt disponibile pentru a pune în practică conceptul de AI Responsabil.

## Principiile AI Responsabil

Entuziasmul pentru AI Generativ nu a fost niciodată mai mare. Acest entuziasm a atras mulți dezvoltatori noi, atenție și finanțare în acest domeniu. Deși acest lucru este foarte pozitiv pentru oricine dorește să construiască produse și companii folosind AI Generativ, este, de asemenea, important să procedăm responsabil.

Pe parcursul acestui curs, ne concentrăm pe construirea startup-ului nostru și a produsului nostru educațional bazat pe AI. Vom folosi principiile AI Responsabil: Echitate, Incluziune, Fiabilitate/Siguranță, Securitate și Confidențialitate, Transparență și Responsabilitate. Cu ajutorul acestor principii, vom explora cum se raportează acestea la utilizarea AI Generativ în produsele noastre.

## De ce ar trebui să prioritizezi AI Responsabil

Atunci când construiești un produs, adoptarea unei abordări centrate pe om, având în vedere interesul cel mai bun al utilizatorului, duce la cele mai bune rezultate.

Unicitatea AI Generativ constă în puterea sa de a crea răspunsuri utile, informații, îndrumări și conținut pentru utilizatori. Acest lucru poate fi realizat fără prea mulți pași manuali, ceea ce poate duce la rezultate foarte impresionante. Fără o planificare și strategii adecvate, acest lucru poate, din păcate, să ducă și la rezultate nocive pentru utilizatori, produsul tău și societatea în ansamblu.

Să analizăm câteva (dar nu toate) dintre aceste rezultate potențial nocive:

### Halucinații

Halucinațiile sunt un termen folosit pentru a descrie momentul în care un LLM produce conținut care este fie complet lipsit de sens, fie ceva ce știm că este greșit din punct de vedere factual, bazat pe alte surse de informații.

Să luăm, de exemplu, cazul în care construim o funcție pentru startup-ul nostru care permite studenților să pună întrebări istorice unui model. Un student întreabă: `Cine a fost singurul supraviețuitor al Titanicului?`

Modelul produce un răspuns precum cel de mai jos:

![Prompt care spune "Cine a fost singurul supraviețuitor al Titanicului"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Sursa: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Acesta este un răspuns foarte încrezător și detaliat. Din păcate, este incorect. Chiar și cu o cantitate minimă de cercetare, cineva ar descoperi că au existat mai mulți supraviețuitori ai dezastrului Titanic. Pentru un student care abia începe să cerceteze acest subiect, acest răspuns poate fi suficient de convingător încât să nu fie pus la îndoială și să fie tratat ca un fapt. Consecințele acestui lucru pot duce la un sistem AI nesigur și pot afecta negativ reputația startup-ului nostru.

Cu fiecare iterație a unui LLM dat, am observat îmbunătățiri ale performanței în reducerea halucinațiilor. Chiar și cu această îmbunătățire, noi, ca dezvoltatori de aplicații și utilizatori, trebuie să rămânem conștienți de aceste limitări.

### Conținut nociv

Am discutat în secțiunea anterioară despre momentul în care un LLM produce răspunsuri incorecte sau lipsite de sens. Un alt risc de care trebuie să fim conștienți este atunci când un model răspunde cu conținut nociv.

Conținutul nociv poate fi definit ca:

- Oferirea de instrucțiuni sau încurajarea auto-vătămării sau vătămării anumitor grupuri.
- Conținut ofensator sau denigrator.
- Ghidarea planificării oricărui tip de atac sau acte violente.
- Oferirea de instrucțiuni despre cum să găsești conținut ilegal sau să comiți acte ilegale.
- Afișarea de conținut explicit sexual.

Pentru startup-ul nostru, dorim să ne asigurăm că avem instrumentele și strategiile potrivite pentru a preveni ca acest tip de conținut să fie văzut de studenți.

### Lipsa echității

Echitatea este definită ca „asigurarea că un sistem AI este lipsit de prejudecăți și discriminare și că tratează pe toată lumea în mod echitabil și egal.” În lumea AI Generativ, dorim să ne asigurăm că viziunile excluzive asupra grupurilor marginalizate nu sunt întărite de rezultatele modelului.

Aceste tipuri de rezultate nu sunt doar distructive pentru construirea unor experiențe pozitive de produs pentru utilizatorii noștri, ci cauzează și daune sociale suplimentare. Ca dezvoltatori de aplicații, ar trebui să avem întotdeauna în vedere o bază largă și diversă de utilizatori atunci când construim soluții cu AI Generativ.

## Cum să folosești AI Generativ în mod responsabil

Acum că am identificat importanța AI Generativ Responsabil, să analizăm 4 pași pe care îi putem face pentru a construi soluții AI în mod responsabil:

![Ciclul de atenuare](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.ro.png)

### Măsurarea riscurilor potențiale

În testarea software, testăm acțiunile așteptate ale unui utilizator pe o aplicație. În mod similar, testarea unui set divers de solicitări pe care utilizatorii sunt cel mai probabil să le folosească este o modalitate bună de a măsura riscurile potențiale.

Deoarece startup-ul nostru construiește un produs educațional, ar fi bine să pregătim o listă de solicitări legate de educație. Acestea ar putea acoperi un anumit subiect, fapte istorice și solicitări despre viața studenților.

### Atenuarea riscurilor potențiale

Este momentul să găsim modalități prin care putem preveni sau limita riscurile potențiale cauzate de model și de răspunsurile acestuia. Putem privi acest aspect în 4 straturi diferite:

![Straturi de atenuare](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.ro.png)

- **Model**. Alegerea modelului potrivit pentru cazul de utilizare potrivit. Modelele mai mari și mai complexe, cum ar fi GPT-4, pot prezenta un risc mai mare de conținut nociv atunci când sunt aplicate la cazuri de utilizare mai mici și mai specifice. Utilizarea datelor de antrenament pentru ajustare fină reduce, de asemenea, riscul de conținut nociv.

- **Sistem de siguranță**. Un sistem de siguranță este un set de instrumente și configurații pe platforma care servește modelul, care ajută la atenuarea riscurilor. Un exemplu este sistemul de filtrare a conținutului din serviciul Azure OpenAI. Sistemele ar trebui să detecteze atacurile de tip jailbreak și activitățile nedorite, cum ar fi cererile de la roboți.

- **Metaprompt**. Metaprompturile și ancorarea sunt modalități prin care putem direcționa sau limita modelul pe baza anumitor comportamente și informații. Acest lucru ar putea însemna utilizarea intrărilor de sistem pentru a defini anumite limite ale modelului. În plus, oferirea de rezultate mai relevante pentru domeniul sau scopul sistemului.

De asemenea, se pot folosi tehnici precum Generarea Augmentată prin Recuperare (RAG) pentru ca modelul să extragă informații doar dintr-o selecție de surse de încredere. Există o lecție mai târziu în acest curs despre [construirea aplicațiilor de căutare](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiența utilizatorului**. Ultimul strat este acolo unde utilizatorul interacționează direct cu modelul prin interfața aplicației noastre într-un fel. În acest fel, putem proiecta UI/UX pentru a limita utilizatorul în privința tipurilor de intrări pe care le poate trimite modelului, precum și textul sau imaginile afișate utilizatorului. Când implementăm aplicația AI, trebuie să fim transparenți cu privire la ceea ce aplicația noastră AI Generativ poate și nu poate face.

Avem o lecție dedicată [Proiectării UX pentru Aplicații AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluarea modelului**. Lucrul cu LLM-uri poate fi provocator deoarece nu avem întotdeauna control asupra datelor pe care modelul a fost antrenat. Indiferent de acest aspect, ar trebui să evaluăm întotdeauna performanța și rezultatele modelului. Este important să măsurăm acuratețea, similaritatea, ancorarea și relevanța rezultatelor modelului. Acest lucru ajută la oferirea de transparență și încredere părților interesate și utilizatorilor.

### Operarea unei soluții AI Generativ Responsabile

Construirea unei practici operaționale în jurul aplicațiilor AI este etapa finală. Aceasta include colaborarea cu alte părți ale startup-ului nostru, cum ar fi departamentele juridice și de securitate, pentru a ne asigura că respectăm toate politicile de reglementare. Înainte de lansare, dorim, de asemenea, să construim planuri legate de livrare, gestionarea incidentelor și revenirea la o versiune anterioară pentru a preveni orice prejudiciu pentru utilizatorii noștri.

## Instrumente

Deși munca de dezvoltare a soluțiilor AI Responsabile poate părea multă, este o muncă bine meritată. Pe măsură ce domeniul AI Generativ crește, mai multe instrumente care să ajute dezvoltatorii să integreze eficient responsabilitatea în fluxurile lor de lucru vor evolua. De exemplu, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) poate ajuta la detectarea conținutului și imaginilor nocive printr-o cerere API.

## Verificarea cunoștințelor

Care sunt câteva lucruri de care trebuie să ții cont pentru a asigura utilizarea responsabilă a AI?

1. Că răspunsul este corect.  
1. Utilizarea nocivă, ca AI să nu fie folosit pentru scopuri ilegale.  
1. Asigurarea că AI este lipsit de prejudecăți și discriminare.  

R: 2 și 3 sunt corecte. AI Responsabil te ajută să iei în considerare cum să atenuezi efectele nocive și prejudecățile și multe altele.

## 🚀 Provocare

Citește despre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) și vezi ce poți adopta pentru utilizarea ta.

## Felicitări, continuă să înveți

După ce ai finalizat această lecție, consultă [colecția de învățare AI Generativ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți îmbunătăți cunoștințele despre AI Generativ!

Mergi la Lecția 4, unde vom analiza [Fundamentele Ingineriei Prompturilor](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.