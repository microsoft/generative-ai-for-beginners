<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:50:21+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "ro"
}
-->
# Utilizarea AI Generativ în Mod Responsabil

> _Apasă pe imaginea de mai sus pentru a viziona videoclipul acestei lecții_

Este ușor să fii fascinat de AI și, în special, de AI generativ, dar trebuie să iei în considerare cum să-l utilizezi în mod responsabil. Trebuie să te gândești la lucruri precum cum să te asiguri că rezultatele sunt corecte, non-dăunătoare și multe altele. Acest capitol își propune să îți ofere contextul menționat, ce să iei în considerare și cum să faci pași activi pentru a îmbunătăți utilizarea AI.

## Introducere

Această lecție va acoperi:

- De ce ar trebui să prioritizezi AI Responsabil atunci când construiești aplicații de AI Generativ.
- Principiile de bază ale AI Responsabil și cum se raportează la AI Generativ.
- Cum să aplici aceste principii ale AI Responsabil prin strategie și instrumente.

## Obiective de Învățare

După ce vei finaliza această lecție vei ști:

- Importanța AI Responsabil atunci când construiești aplicații de AI Generativ.
- Când să gândești și să aplici principiile de bază ale AI Responsabil atunci când construiești aplicații de AI Generativ.
- Ce instrumente și strategii sunt disponibile pentru a pune în practică conceptul de AI Responsabil.

## Principiile AI Responsabil

Entuziasmul pentru AI Generativ nu a fost niciodată mai mare. Acest entuziasm a adus mulți dezvoltatori noi, atenție și finanțare în acest domeniu. Deși acest lucru este foarte pozitiv pentru oricine dorește să construiască produse și companii folosind AI Generativ, este, de asemenea, important să procedăm responsabil.

Pe parcursul acestui curs, ne concentrăm pe construirea startup-ului nostru și a produsului nostru educațional AI. Vom folosi principiile AI Responsabil: Echitate, Incluziune, Fiabilitate/Siguranță, Securitate și Confidențialitate, Transparență și Responsabilitate. Cu aceste principii, vom explora cum se raportează la utilizarea AI Generativ în produsele noastre.

## De ce ar trebui să prioritizezi AI Responsabil

Când construiești un produs, adoptând o abordare centrată pe oameni și având în vedere interesul utilizatorului duce la cele mai bune rezultate.

Unicitatea AI Generativ constă în puterea sa de a crea răspunsuri utile, informații, ghiduri și conținut pentru utilizatori. Acest lucru poate fi realizat fără multe etape manuale, ceea ce poate duce la rezultate foarte impresionante. Fără planificare și strategii adecvate, poate, din păcate, duce la rezultate dăunătoare pentru utilizatorii tăi, produsul tău și societatea în ansamblu.

Să ne uităm la câteva (dar nu toate) dintre aceste rezultate potențial dăunătoare:

### Halucinații

Halucinațiile sunt un termen folosit pentru a descrie când un LLM produce conținut care este fie complet nonsensical, fie ceva despre care știm că este greșit factual pe baza altor surse de informații.

Să luăm, de exemplu, construim o funcție pentru startup-ul nostru care permite studenților să pună întrebări istorice unui model. Un student pune întrebarea `Who was the sole survivor of Titanic?`

Modelul produce un răspuns precum cel de mai jos:

Aceasta este un răspuns foarte încrezător și detaliat. Din păcate, este incorect. Chiar și cu o cantitate minimă de cercetare, cineva ar descoperi că au fost mai mulți supraviețuitori ai dezastrului Titanic. Pentru un student care abia începe să cerceteze acest subiect, acest răspuns poate fi suficient de convingător pentru a nu fi pus la îndoială și tratat ca un fapt. Consecințele acestui lucru pot duce la sistemul AI fiind nesigur și pot afecta negativ reputația startup-ului nostru.

Cu fiecare iterație a unui LLM dat, am observat îmbunătățiri ale performanței în minimizarea halucinațiilor. Chiar și cu această îmbunătățire, noi, ca dezvoltatori de aplicații și utilizatori, trebuie să rămânem conștienți de aceste limitări.

### Conținut Dăunător

Am acoperit în secțiunea anterioară când un LLM produce răspunsuri incorecte sau nonsensicale. Un alt risc de care trebuie să fim conștienți este când un model răspunde cu conținut dăunător.

Conținutul dăunător poate fi definit ca:

- Oferirea de instrucțiuni sau încurajarea auto-vătămării sau vătămării anumitor grupuri.
- Conținutul urât sau denigrator.
- Ghidarea planificării oricărui tip de atac sau acte violente.
- Oferirea de instrucțiuni despre cum să găsești conținut ilegal sau să comiți acte ilegale.
- Afișarea conținutului sexual explicit.

Pentru startup-ul nostru, dorim să ne asigurăm că avem instrumentele și strategiile potrivite pentru a preveni ca acest tip de conținut să fie văzut de studenți.

### Lipsa Echității

Echitatea este definită ca "asigurarea că un sistem AI este liber de prejudecăți și discriminare și că tratează pe toată lumea corect și egal." În lumea AI Generativ, dorim să ne asigurăm că viziunile excluzionare ale grupurilor marginalizate nu sunt întărite de rezultatele modelului.

Aceste tipuri de rezultate nu sunt doar distructive pentru construirea de experiențe de produs pozitive pentru utilizatorii noștri, dar cauzează și un prejudiciu social suplimentar. Ca dezvoltatori de aplicații, ar trebui să avem întotdeauna în vedere o bază largă și diversă de utilizatori atunci când construim soluții cu AI Generativ.

## Cum să folosești AI Generativ în mod Responsabil

Acum că am identificat importanța AI Generativ Responsabil, să ne uităm la 4 pași pe care îi putem face pentru a construi soluțiile noastre AI în mod responsabil:

### Măsurarea Potențialelor Daune

În testarea software-ului, testăm acțiunile așteptate ale unui utilizator asupra unei aplicații. În mod similar, testarea unui set divers de solicitări pe care utilizatorii sunt cel mai probabil să le folosească este o modalitate bună de a măsura daunele potențiale.

Deoarece startup-ul nostru construiește un produs educațional, ar fi bine să pregătim o listă de solicitări legate de educație. Acest lucru ar putea fi pentru a acoperi un anumit subiect, fapte istorice și solicitări despre viața de student.

### Atenuarea Potențialelor Daune

Acum este timpul să găsim modalități prin care putem preveni sau limita daunele potențiale cauzate de model și de răspunsurile acestuia. Putem privi acest lucru în 4 straturi diferite:

- **Model**. Alegerea modelului potrivit pentru cazul de utilizare potrivit. Modelele mai mari și mai complexe, cum ar fi GPT-4, pot cauza un risc mai mare de conținut dăunător atunci când sunt aplicate la cazuri de utilizare mai mici și mai specifice. Utilizarea datelor tale de instruire pentru a ajusta fin reduce, de asemenea, riscul de conținut dăunător.

- **Sistem de Siguranță**. Un sistem de siguranță este un set de instrumente și configurații pe platforma care servește modelul și care ajută la atenuarea daunelor. Un exemplu în acest sens este sistemul de filtrare a conținutului de pe serviciul Azure OpenAI. Sistemele ar trebui să detecteze, de asemenea, atacurile de jailbreak și activitățile nedorite, cum ar fi solicitările de la roboți.

- **Metaprompt**. Metapromptele și ancorarea sunt modalități prin care putem direcționa sau limita modelul pe baza anumitor comportamente și informații. Acest lucru ar putea fi folosirea intrărilor sistemului pentru a defini anumite limite ale modelului. În plus, oferirea de rezultate care sunt mai relevante pentru domeniul sau domeniul sistemului.

De asemenea, poate fi utilizarea tehnicilor precum Generarea Augmentată de Recuperare (RAG) pentru a face ca modelul să extragă informații doar dintr-o selecție de surse de încredere. Există o lecție mai târziu în acest curs pentru [construirea aplicațiilor de căutare](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiența Utilizatorului**. Ultimul strat este locul unde utilizatorul interacționează direct cu modelul prin intermediul interfeței aplicației noastre într-un fel. În acest mod, putem proiecta UI/UX pentru a limita utilizatorul în tipurile de intrări pe care le pot trimite modelului, precum și textul sau imaginile afișate utilizatorului. Când implementăm aplicația AI, trebuie să fim, de asemenea, transparenți cu privire la ce poate și ce nu poate face aplicația noastră AI Generativ.

Avem o lecție întreagă dedicată [Proiectării UX pentru Aplicații AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluarea modelului**. Lucrul cu LLM-urile poate fi provocator deoarece nu avem întotdeauna control asupra datelor pe care modelul a fost instruit. Indiferent, ar trebui să evaluăm întotdeauna performanța și rezultatele modelului. Este important să măsurăm acuratețea, similaritatea, ancorarea și relevanța rezultatului modelului. Acest lucru ajută la oferirea de transparență și încredere pentru părțile interesate și utilizatori.

### Operarea unei soluții AI Generativ Responsabile

Construirea unei practici operaționale în jurul aplicațiilor tale AI este etapa finală. Aceasta include colaborarea cu alte părți ale startup-ului nostru, cum ar fi Legal și Securitate, pentru a ne asigura că suntem conformi cu toate politicile de reglementare. Înainte de lansare, dorim, de asemenea, să construim planuri în jurul livrării, gestionării incidentelor și retragerii pentru a preveni orice daune pentru utilizatorii noștri de la creștere.

## Instrumente

Deși munca de dezvoltare a soluțiilor AI Responsabile poate părea multă, este o muncă care merită efortul. Pe măsură ce domeniul AI Generativ crește, mai multe instrumente pentru a ajuta dezvoltatorii să integreze eficient responsabilitatea în fluxurile lor de lucru vor evolua. De exemplu, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) poate ajuta la detectarea conținutului și imaginilor dăunătoare printr-o cerere API.

## Verificare a Cunoștințelor

Care sunt unele lucruri de care trebuie să te îngrijești pentru a asigura utilizarea responsabilă a AI?

1. Ca răspunsul să fie corect.
1. Utilizarea dăunătoare, ca AI să nu fie folosit pentru scopuri criminale.
1. Asigurarea că AI este liber de prejudecăți și discriminare.

A: 2 și 3 sunt corecte. AI Responsabil te ajută să consideri cum să atenuezi efectele dăunătoare și prejudecățile și multe altele.

## 🚀 Provocare

Citește despre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) și vezi ce poți adopta pentru utilizarea ta.

## Felicitări, Continuă Învățarea Ta

După ce ai finalizat această lecție, verifică colecția noastră de [Învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți îmbunătățești cunoștințele despre AI Generativ!

Mergi la Lecția 4 unde vom privi [Fundamentele Ingineriei Solicitărilor](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți de faptul că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană profesională. Nu suntem responsabili pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.