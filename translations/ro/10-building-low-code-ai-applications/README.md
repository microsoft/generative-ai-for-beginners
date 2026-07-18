# Construirea Aplicațiilor AI cu Cod Redus

[![Construirea Aplicațiilor AI cu Cod Redus](../../../translated_images/ro/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

## Introducere

Acum că am învățat cum să construim aplicații pentru generarea de imagini, să vorbim despre low code. AI generativ poate fi folosit pentru o varietate de domenii diferite, inclusiv low code, dar ce este low code și cum putem adăuga AI la acesta?

Construirea de aplicații și soluții a devenit mai ușoară pentru dezvoltatorii tradiționali și non-dezvoltatori prin utilizarea Platformelor de Dezvoltare Low Code. Platformele de Dezvoltare Low Code vă permit să construiți aplicații și soluții cu puțin sau fără cod. Acest lucru se realizează prin oferirea unui mediu vizual de dezvoltare care vă permite să trageți și să plasați componente pentru a construi aplicații și soluții. Acest lucru vă permite să construiți aplicații și soluții mai rapid și cu mai puține resurse. În această lecție, vom explora în profunzime cum să folosim Low Code și cum să îmbunătățim dezvoltarea low code cu AI folosind Power Platform.

Power Platform oferă organizațiilor oportunitatea de a-și împuternici echipele să construiască propriile soluții printr-un mediu intuitiv low-code sau no-code. Acest mediu ajută la simplificarea procesului de creare a soluțiilor. Cu Power Platform, soluțiile pot fi construite în zile sau săptămâni în loc de luni sau ani. Power Platform constă din cinci produse cheie: Power Apps, Power Automate, Power BI, Power Pages și Copilot Studio.

Această lecție acoperă:

- Introducere în AI generativ în Power Platform
- Introducere în Copilot și cum să îl utilizați
- Folosirea AI generativ pentru a construi aplicații și fluxuri în Power Platform
- Înțelegerea modelelor AI în Power Platform cu AI Builder
- Construirea agenților inteligenți cu Microsoft Copilot Studio

## Obiectivele de învățare

La finalul acestei lecții, veți putea:

- Înțelege cum funcționează Copilot în Power Platform.

- Construi o aplicație Student Assignment Tracker pentru startup-ul nostru educațional.

- Construi un flux de procesare a facturilor care utilizează AI pentru a extrage informații din facturi.

- Aplica cele mai bune practici atunci când folosești modelul AI Create Text with GPT.

- Înțelege ce este Microsoft Copilot Studio și cum să construiești agenți inteligenți cu acesta.

Instrumentele și tehnologiile pe care le vei folosi în această lecție sunt:

- **Power Apps**, pentru aplicația Student Assignment Tracker, care oferă un mediu de dezvoltare low-code pentru construirea aplicațiilor de urmărire, gestionare și interacțiune cu datele.

- **Dataverse**, pentru stocarea datelor aplicației Student Assignment Tracker, unde Dataverse va oferi o platformă low-code pentru stocarea datelor aplicației.

- **Power Automate**, pentru fluxul de procesare a facturilor, unde vei avea un mediu de dezvoltare low-code pentru construirea fluxurilor de automatizare a procesului de procesare a facturilor.

- **AI Builder**, pentru modelul AI de procesare a facturilor, unde vei folosi modele AI preconstruite pentru a procesa facturile pentru startup-ul nostru.

## AI generativ în Power Platform

Îmbunătățirea dezvoltării low-code și a aplicațiilor cu AI generativ este o zonă cheie de interes pentru Power Platform. Scopul este să permită tuturor să construiască aplicații, site-uri, tablouri de bord alimentate de AI și să automatizeze procesele cu AI, _fără a necesita expertiză în știința datelor_. Acest scop este atins prin integrarea AI generativ în experiența de dezvoltare low-code în Power Platform sub forma Copilot și AI Builder.

### Cum funcționează?

Copilot este un asistent AI care îți permite să construiești soluții Power Platform descriind cerințele tale într-o serie de pași conversaționali folosind limbaj natural. Poți, de exemplu, să îi spui asistentului tău AI ce câmpuri va folosi aplicația ta și acesta va crea atât aplicația, cât și modelul de date subiacente sau poți specifica cum să configurezi un flux în Power Automate.

Poți folosi funcționalități bazate pe Copilot ca o caracteristică în ecranele aplicației tale pentru a permite utilizatorilor să descopere insight-uri prin interacțiuni conversaționale.

AI Builder este o capacitate AI low-code disponibilă în Power Platform care îți permite să folosești modele AI pentru a te ajuta să automatizezi procese și să prevezi rezultate. Cu AI Builder poți aduce AI în aplicațiile și fluxurile tale care se conectează la datele din Dataverse sau în diverse surse cloud, cum ar fi SharePoint, OneDrive sau Azure.

Copilot este disponibil în toate produsele Power Platform: Power Apps, Power Automate, Power BI, Power Pages și Copilot Studio (fost Power Virtual Agents). AI Builder este disponibil în Power Apps și Power Automate. În această lecție, ne vom concentra asupra modului de utilizare a Copilot și AI Builder în Power Apps și Power Automate pentru a construi o soluție pentru startup-ul nostru educațional.

### Copilot în Power Apps

Ca parte a Power Platform, Power Apps oferă un mediu low-code de dezvoltare pentru construirea aplicațiilor de urmărire, gestionare și interacțiune cu datele. Este o suită de servicii de dezvoltare aplicații cu o platformă de date scalabilă și abilitatea de a se conecta la servicii cloud și date locale. Power Apps îți permite să construiești aplicații care rulează pe browsere, tablete și telefoane, și pot fi partajate cu colegii de muncă. Power Apps introduce utilizatorii în dezvoltarea de aplicații cu o interfață simplă, astfel încât fiecare utilizator de business sau dezvoltator profesionist să poată construi aplicații personalizate. Experiența de dezvoltare a aplicației este de asemenea îmbunătățită cu AI generativ prin Copilot.

Caracteristica asistentului AI Copilot în Power Apps îți permite să descrii ce fel de aplicație ai nevoie și ce informații vrei să urmărească, să colecteze sau să afișeze aplicația ta. Copilot generează apoi o aplicație Canvas responsivă bazată pe descrierea ta. Poți apoi personaliza aplicația pentru a corespunde nevoilor tale. AI Copilot generează și sugerează, de asemenea, un tabel Dataverse cu câmpurile de care ai nevoie pentru a stoca datele pe care dorești să le urmărești și câteva date de probă. Vom arunca o privire mai târziu în această lecție asupra a ce este Dataverse și cum îl poți folosi în Power Apps. Poți apoi personaliza tabelul pentru a corespunde nevoilor tale folosind caracteristica asistentului AI Copilot prin pași conversaționali. Această caracteristică este disponibilă direct de pe ecranul principal Power Apps.

### Copilot în Power Automate

Ca parte a Power Platform, Power Automate permite utilizatorilor să creeze fluxuri de lucru automate între aplicații și servicii. Ajută la automatizarea proceselor repetitive de business, cum ar fi comunicarea, colectarea de date și aprobările deciziilor. Interfața sa simplă permite utilizatorilor cu orice nivel tehnic (de la începători la dezvoltatori experimentați) să automatizeze sarcinile de lucru. Experiența de dezvoltare a fluxului de lucru este de asemenea îmbunătățită cu AI generativ prin Copilot.

Caracteristica asistentului AI Copilot în Power Automate îți permite să descrii ce fel de flux ai nevoie și ce acțiuni vrei ca fluxul tău să efectueze. Copilot generează apoi un flux pe baza descrierii tale. Poți apoi personaliza fluxul pentru a corespunde nevoilor tale. AI Copilot generează și sugerează acțiunile de care ai nevoie pentru a executa sarcina pe care vrei să o automatizezi. Vom discuta mai târziu în această lecție ce sunt fluxurile și cum le poți folosi în Power Automate. Poți apoi personaliza acțiunile pentru a corespunde nevoilor tale folosind caracteristica asistentului AI Copilot prin pași conversaționali. Această caracteristică este disponibilă direct de pe ecranul principal Power Automate.

## Construirea Agenților Inteligenți cu Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (fost Power Virtual Agents) este membrul low-code al Power Platform pentru construirea **agenților AI** — copiloți conversaționali care pot răspunde la întrebări, pot lua acțiuni și pot automatiza sarcini în numele utilizatorilor tăi. La fel ca restul Power Platform, acești agenți se construiesc într-o experiență vizuală, cu prioritate pe limbaj natural: descrii ce vrei să facă agentul, iar Copilot Studio ajută la structurarea instrucțiunilor, cunoștințelor și acțiunilor sale.

Pentru startup-ul nostru educațional, ai putea construi un agent care să răspundă la întrebările studenților despre cursuri, să verifice termenele limită pentru teme și chiar să trimită e-mailuri unui instructor — toate fără a scrie cod.

Iată câteva dintre cele mai recente capabilități care fac Copilot Studio puternic:

- **Răspunsuri generative din cunoștințele tale**. În loc să scrii manual fiecare conversație, poți conecta **surse de cunoștințe** — site-uri publice, SharePoint, OneDrive, Dataverse, fișiere încărcate sau date enterprise prin conectori — iar agentul generează răspunsuri fundamentate din acestea.

- **Orchestrare generativă**. În loc să se bazeze pe fraze trigger rigide, agentul folosește AI pentru a înțelege o cerere și decide dinamic ce cunoștințe, subiecte și acțiuni să combine pentru a o îndeplini, inclusiv legând împreună mai mulți pași.

- **Acțiuni și conectori**. Agenții pot *face* lucruri, nu doar conversa. Poți oferi unui agent acțiuni susținute de peste 1.500 conectori predefiniți Power Platform, fluxuri Power Automate, API-uri REST custom, prompturi sau servere **Model Context Protocol (MCP)**.

- **Agenți autonomi**. Agenții nu sunt limitați să răspundă într-o fereastră de chat. Poți construi **agenți autonomi** care sunt declanșați de evenimente — cum ar fi un e-mail nou, un nou record în Dataverse sau un fișier încărcat — și acționează în fundal pentru a finaliza o sarcină.

- **Orchestrare multi-agent**. Agenții pot apela alți agenți. Un agent Copilot Studio poate preda lucrul altor agenți sau poate fi extins de aceștia, inclusiv agenți publicați în Microsoft 365 Copilot și agenți construiți în Microsoft Foundry.

- **Opțiunea modelului**. Dincolo de modelele integrate, poți aduce modele din catalogul Microsoft Foundry pentru a adapta modul în care agentul tău raționează și răspunde.

- **Publică oriunde**. Odată construit, un agent poate fi publicat pe mai multe canale — Microsoft Teams, Microsoft 365 Copilot, un site web sau aplicație custom și altele — cu securitate, autentificare și analiză gestionate prin experiența de administrare Power Platform.

Poți începe să construiești primul agent la [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) și să afli mai multe în [documentația Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Tema: Gestionează temele studenților și facturile pentru startup-ul nostru, folosind Copilot

Startup-ul nostru oferă cursuri online pentru studenți. Startup-ul a crescut rapid și acum întâmpină dificultăți în a face față cererii pentru cursurile sale. Startup-ul te-a angajat ca dezvoltator Power Platform pentru a-i ajuta să construiască o soluție low code care să-i ajute să gestioneze temele studenților și facturile. Soluția lor ar trebui să îi ajute să urmărească și să gestioneze temele studenților printr-o aplicație și să automatizeze procesul de procesare a facturilor printr-un flux de lucru. Ți s-a cerut să folosești AI generativ pentru a dezvolta soluția.

Când începi să folosești Copilot, poți folosi [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) pentru a începe să folosești prompturile. Această bibliotecă conține o listă de prompturi pe care le poți folosi pentru a construi aplicații și fluxuri cu Copilot. De asemenea, poți folosi prompturile din bibliotecă pentru a-ți face o idee despre cum să descrii cerințele tale către Copilot.

### Construiește o aplicație Student Assignment Tracker pentru startup-ul nostru

Profesorii de la startup-ul nostru au avut dificultăți în a ține evidența temelor studenților. Au folosit un tabel Excel pentru a urmări temele, dar acest lucru a devenit dificil de gestionat pe măsură ce numărul studenților a crescut. Ei ți-au cerut să construiești o aplicație care să îi ajute să urmărească și să gestioneze temele studenților. Aplicația ar trebui să le permită să adauge teme noi, să vadă temele, să actualizeze temele și să șteargă temele. Aplicația ar trebui, de asemenea, să le permită profesorilor și studenților să vadă temele care au fost notate și cele care nu au fost notate.

Vei construi aplicația folosind Copilot în Power Apps urmând pașii de mai jos:

1. Navighează la ecranul principal [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Folosește zona de text de pe ecranul principal pentru a descrie aplicația pe care vrei să o construiești. De exemplu, **_Vreau să construiesc o aplicație pentru a urmări și gestiona temele studenților_**. Apasă butonul **Send** pentru a trimite promptul către AI Copilot.

![Descrie aplicația pe care vrei să o construiești](../../../translated_images/ro/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot va sugera un tabel Dataverse cu câmpurile necesare pentru a stoca datele pe care vrei să le urmărești și câteva date de probă. Poți apoi personaliza tabelul pentru a corespunde nevoilor tale folosind caracteristica asistentului AI Copilot prin pași conversaționali.

   > **Important**: Dataverse este platforma de date subiacente pentru Power Platform. Este o platformă de date low-code pentru stocarea datelor aplicației. Este un serviciu complet gestionat care stochează datele securizat în Microsoft Cloud și este provisionat în mediul tău Power Platform. Vine cu capabilități integrate de guvernanță a datelor, cum ar fi clasificarea datelor, trasabilitate date, control granular al accesului și altele. Poți afla mai multe despre Dataverse [aici](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Câmpuri sugerate în noul tău tabel](../../../translated_images/ro/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Profesorii doresc să trimită e-mailuri studenților care au predat temele pentru a-i ține la curent cu progresul temelor lor. Poți folosi Copilot pentru a adăuga un câmp nou în tabel pentru stocarea email-ului studentului. De exemplu, poți folosi promptul următor pentru a adăuga un câmp nou în tabel: **_Vreau să adaug o coloană pentru stocarea email-ului studentului_**. Apasă butonul **Send** pentru a trimite promptul AI Copilot.

![Adăugarea unui câmp nou](../../../translated_images/ro/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot va genera un câmp nou și apoi poți personaliza câmpul pentru a corespunde nevoilor tale.


1. Odată ce ați terminat cu tabelul, faceți clic pe butonul **Create app** pentru a crea aplicația.

1. AI Copilot va genera o aplicație Canvas responsive bazată pe descrierea dvs. Puteți apoi personaliza aplicația pentru a vă satisface nevoile.

1. Pentru ca educatorii să trimită e-mailuri către elevi, puteți folosi Copilot pentru a adăuga un ecran nou aplicației. De exemplu, puteți folosi următorul prompt pentru a adăuga un ecran nou aplicației: **_Vreau să adaug un ecran pentru a trimite e-mailuri către elevi_**. Faceți clic pe butonul **Send** pentru a trimite promptul către AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/ro/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot va genera un ecran nou și puteți apoi personaliza ecranul pentru a vă satisface nevoile.

1. Odată ce ați terminat cu aplicația, faceți clic pe butonul **Save** pentru a salva aplicația.

1. Pentru a partaja aplicația cu educatorii, faceți clic pe butonul **Share** și apoi faceți clic din nou pe butonul **Share**. Puteți apoi să partajați aplicația cu educatorii introducând adresele lor de e-mail.

> **Temă pentru acasă**: Aplicația pe care tocmai ați construit-o este un început bun, dar poate fi îmbunătățită. Cu funcția de e-mail, educatorii pot trimite doar manual e-mailuri către elevi, trebuind să tasteze adresele lor de e-mail. Puteți folosi Copilot pentru a construi o automatizare care să permită educatorilor să trimită e-mailuri elevilor automat atunci când aceștia își predau temele? Indiciul este că, cu promptul potrivit, puteți folosi Copilot în Power Automate pentru a construi acest lucru.

### Construiți un Tabel cu Informații despre Facturi pentru Startup-ul Nostru

Echipa financiară a startup-ului nostru a avut dificultăți în a urmări facturile. Aceștia au folosit un fișier de calcul pentru a urmări facturile, dar acesta a devenit greu de gestionat pe măsură ce numărul facturilor a crescut. V-au cerut să construiți un tabel care să îi ajute să stocheze, urmărească și să gestioneze informațiile facturilor pe care le-au primit. Tabelul trebuie folosit pentru a construi o automatizare care să extragă toate informațiile facturilor și să le stocheze în tabel. Tabelul trebuie, de asemenea, să permită echipei financiare să vadă facturile care au fost plătite și cele care nu au fost plătite.

Power Platform are o platformă de date subiacente numită Dataverse care vă permite să stocați datele pentru aplicațiile și soluțiile dvs. Dataverse oferă o platformă de date low-code pentru stocarea datelor aplicației. Este un serviciu complet gestionat care stochează în siguranță datele în Microsoft Cloud și este provisionat în mediul dvs. Power Platform. Vine cu capacități încorporate de guvernanță a datelor, cum ar fi clasificarea datelor, proveniența datelor, controlul fin al accesului și multe altele. Puteți afla mai multe [despre Dataverse aici](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

De ce ar trebui să folosim Dataverse pentru startup-ul nostru? Tabelele standard și personalizate din Dataverse oferă o opțiune de stocare securizată și bazată pe cloud pentru datele dvs. Tabelele vă permit să stocați diferite tipuri de date, similar cu modul în care ați putea folosi mai multe foi de calcul într-un singur registru Excel. Puteți folosi tabele pentru a stoca date specifice organizației sau nevoilor dvs. de afaceri. Unele dintre beneficiile pe care startup-ul nostru le va obține folosind Dataverse includ, dar nu se limitează la:

- **Ușor de gestionat**: Atât metadatele, cât și datele sunt stocate în cloud, deci nu trebuie să vă faceți griji despre detaliile felului în care sunt stocate sau gestionate. Puteți să vă concentrați pe construirea aplicațiilor și soluțiilor.

- **Securizat**: Dataverse oferă o opțiune de stocare securizată și bazată pe cloud pentru datele dvs. Puteți controla cine are acces la datele din tabelele dvs. și cum le pot accesa folosind securitatea bazată pe roluri.

- **Metadate bogate**: Tipurile de date și relațiile sunt utilizate direct în Power Apps

- **Logică și validare**: Puteți folosi reguli de afaceri, câmpuri calculate și reguli de validare pentru a impune logica de afaceri și a menține acuratețea datelor.

Acum că știți ce este Dataverse și de ce ar trebui să îl folosiți, să vedem cum puteți folosi Copilot pentru a crea un tabel în Dataverse pentru a satisface cerințele echipei noastre financiare.

> **Notă** : Veți folosi acest tabel în secțiunea următoare pentru a construi o automatizare care să extragă toate informațiile facturii și să le stocheze în tabel.

Pentru a crea un tabel în Dataverse folosind Copilot, urmați pașii de mai jos:

1. Navigați la ecranul de start [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Pe bara de navigare din stânga, selectați **Tables** și apoi faceți clic pe **Describe the new Table**.

![Select new table](../../../translated_images/ro/describe-new-table.0792373eb757281e.webp)

1. Pe ecranul **Describe the new Table**, folosiți zona de text pentru a descrie tabelul pe care doriți să îl creați. De exemplu, **_Vreau să creez un tabel pentru a stoca informații despre facturi_**. Faceți clic pe butonul **Send** pentru a trimite promptul către AI Copilot.

![Describe the table](../../../translated_images/ro/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot va sugera un tabel Dataverse cu câmpurile de care aveți nevoie pentru a stoca datele pe care doriți să le urmăriți și câteva date de probă. Puteți apoi personaliza tabelul pentru a îndeplini nevoile dvs. folosind funcția asistent AI Copilot prin pași conversaționali.

![Suggested Dataverse table](../../../translated_images/ro/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Echipa financiară dorește să trimită un e-mail furnizorului pentru a-l actualiza cu starea curentă a facturii. Puteți folosi Copilot pentru a adăuga un câmp nou în tabel pentru a stoca e-mailul furnizorului. De exemplu, puteți folosi următorul prompt pentru a adăuga un câmp nou în tabel: **_Vreau să adaug o coloană pentru a stoca e-mailul furnizorului_**. Faceți clic pe butonul **Send** pentru a trimite promptul către AI Copilot.

1. AI Copilot va genera un câmp nou și apoi îl puteți personaliza pentru a satisface nevoile dvs.

1. Odată ce ați terminat cu tabelul, faceți clic pe butonul **Create** pentru a crea tabelul.

## Modele AI în Power Platform cu AI Builder

AI Builder este o capacitate AI low-code disponibilă în Power Platform care vă permite să folosiți Modele AI pentru a vă ajuta să automatizați procesele și să preziceți rezultate. Cu AI Builder puteți aduce AI în aplicațiile și fluxurile dvs. care se conectează la datele dvs. în Dataverse sau în diverse surse de date cloud, cum ar fi SharePoint, OneDrive sau Azure.

## Modele AI preconstruite vs Modele AI personalizate

AI Builder oferă două tipuri de modele AI: Modele AI preconstruite și Modele AI personalizate. Modelele AI preconstruite sunt modele AI gata de utilizat, antrenate de Microsoft și disponibile în Power Platform. Acestea vă ajută să adăugați inteligență aplicațiilor și fluxurilor dvs. fără a fi nevoie să colectați date și să construiți, antrenați și publicați propriile modele. Puteți folosi aceste modele pentru a automatiza procesele și a prezice rezultate.

Unele dintre Modelele AI preconstruite disponibile în Power Platform includ:

- **Extracția frazelor-cheie**: Acest model extrage fraze cheie din text.
- **Detecția limbajului**: Acest model detectează limba unui text.
- **Analiza sentimentului**: Acest model detectează sentimente pozitive, negative, neutre sau mixte în text.
- **Cititor de cărți de vizită**: Acest model extrage informații din cărți de vizită.
- **Recunoașterea textului**: Acest model extrage text din imagini.
- **Detecția obiectelor**: Acest model detectează și extrage obiecte din imagini.
- **Procesarea documentelor**: Acest model extrage informații din formulare.
- **Procesarea facturilor**: Acest model extrage informații din facturi.

Cu Modele AI personalizate puteți aduce propriul model în AI Builder astfel încât să funcționeze ca orice model AI personalizat AI Builder, permițându-vă să antrenați modelul folosindu-vă propriile date. Puteți folosi aceste modele pentru a automatiza procese și a prezice rezultate atât în Power Apps, cât și în Power Automate. Când folosiți propriul model există limitări care se aplică. Citiți mai multe despre aceste [limitări](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/ro/ai-builder-models.8069423b84cfc47f.webp)

## Tema #2 - Construiți un Flux pentru Procesarea Facturilor pentru Startup-ul Nostru

Echipa financiară a avut dificultăți în procesarea facturilor. Au folosit un fișier de calcul pentru a urmări facturile, dar acest lucru a devenit greu de gestionat pe măsură ce numărul facturilor a crescut. V-au cerut să construiți un flux de lucru care să îi ajute să proceseze facturile folosind AI. Fluxul de lucru trebuie să le permită să extragă informații din facturi și să stocheze aceste informații într-un tabel Dataverse. Fluxul de lucru trebuie, de asemenea, să le permită să trimită un e-mail echipei financiare cu informațiile extrase.

Acum că știți ce este AI Builder și de ce ar trebui să îl folosiți, să vedem cum puteți folosi Modelul AI Procesare Facturi din AI Builder, pe care l-am prezentat mai devreme, pentru a construi un flux de lucru care să ajute echipa financiară să proceseze facturi.

Pentru a construi un flux de lucru care să ajute echipa financiară să proceseze facturile folosind Modelul AI Procesare Facturi din AI Builder, urmați pașii de mai jos:

1. Navigați la ecranul de start [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Folosiți zona de text de pe ecranul de start pentru a descrie fluxul de lucru pe care doriți să îl construiți. De exemplu, **_Procesează o factură când ajunge în căsuța mea poștală_**. Faceți clic pe butonul **Send** pentru a trimite promptul către AI Copilot.

   ![Copilot power automate](../../../translated_images/ro/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot va sugera acțiunile necesare pentru a îndeplini sarcina pe care doriți să o automatizați. Puteți face clic pe butonul **Next** pentru a parcurge pașii următori.

4. La pasul următor, Power Automate vă va solicita să configurați conexiunile necesare pentru flux. Odată ce ați terminat, faceți clic pe butonul **Create flow** pentru a crea fluxul.

5. AI Copilot va genera un flux și puteți apoi să-l personalizați pentru a satisface nevoile dvs.

6. Actualizați déclanșatorul fluxului și setați **Folder-ul** la folderul unde vor fi stocate facturile. De exemplu, puteți seta folderul la **Inbox**. Faceți clic pe **Show advanced options** și setați opțiunea **Only with Attachments** la **Yes**. Aceasta va asigura că fluxul rulează doar când se primește un e-mail cu atașament în folder.

7. Înlăturați următoarele acțiuni din flux: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** și **Compose 4** pentru că nu le veți folosi.

8. Înlăturați acțiunea **Condition** din flux întrucât nu o veți folosi. Fluxul ar trebui să arate ca în captura de ecran următoare:

   ![power automate, remove actions](../../../translated_images/ro/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Faceți clic pe butonul **Add an action** și căutați **Dataverse**. Selectați acțiunea **Add a new row**.

10. La acțiunea **Extract Information from invoices**, actualizați **Invoice File** pentru a indica către **Attachment Content** din e-mail. Aceasta va asigura că fluxul extrage informații din atașamentul facturii.

11. Selectați **Table**-ul pe care l-ați creat anterior. De exemplu, puteți selecta tabelul **Invoice Information**. Alegeți conținutul dinamic din acțiunea anterioară pentru a completa următoarele câmpuri:

    - ID
    - Amount
    - Date
    - Name
    - Status - Setați **Status** la **Pending**.
    - Supplier Email - Folosiți conținutul dinamic **From** de la déclanșatorul **When a new email arrives**.

    ![power automate add row](../../../translated_images/ro/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Odată ce ați terminat cu fluxul, faceți clic pe butonul **Save** pentru a salva fluxul. Puteți apoi testa fluxul trimițând un e-mail cu o factură în folderul pe care l-ați specificat în déclanșator.

> **Temă pentru acasă**: Fluxul pe care tocmai l-ați construit este un început bun, acum trebuie să vă gândiți cum puteți construi o automatizare care să permită echipei noastre financiare să trimită un e-mail furnizorului pentru a-l actualiza cu starea curentă a facturii lor. Indiciul dvs.: fluxul trebuie să ruleze atunci când starea facturii se schimbă.

## Folosiți un Model AI de Generare Text în Power Automate

Modelul AI Create Text with GPT în AI Builder vă permite să generați text bazat pe un prompt și este alimentat de serviciul Microsoft Azure OpenAI. Cu această capacitate, puteți introduce tehnologia GPT (Generative Pre-Trained Transformer) în aplicațiile și fluxurile dvs. pentru a construi o varietate de fluxuri automate și aplicații insightful.

Modelele GPT trec printr-un antrenament extins pe volume mari de date, permițându-le să producă texte care seamănă foarte mult cu limbajul uman atunci când li se oferă un prompt. Atunci când sunt integrate cu automatizarea fluxurilor de lucru, modelele AI ca GPT pot fi folosite pentru a simplifica și automatiza o gamă largă de sarcini.

De exemplu, puteți construi fluxuri care să genereze automat texte pentru diverse cazuri de utilizare, cum ar fi: schițe de e-mailuri, descrieri de produse și altele. De asemenea, puteți folosi modelul pentru a genera text pentru o varietate de aplicații, cum ar fi chatbot-uri și aplicații de servicii pentru clienți, care permit agenților de suport să răspundă eficient și eficace solicitărilor clienților.

![create a prompt](../../../translated_images/ro/create-prompt-gpt.69d429300c2e870a.webp)


Pentru a învăța cum să folosești acest Model AI în Power Automate, parcurge modulul [Adăugarea inteligenței cu AI Builder și GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Lucru grozav! Continuă să înveți

După ce ai terminat această lecție, consultă colecția noastră [Învață despre AI Generativ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți aprofunda cunoștințele despre AI Generativ!

Dorești să personalizezi și să profiți mai mult de Copilot? Explorează [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — o colecție creată de comunitate cu instrucțiuni, agenți, abilități și configurații care te ajută să profiți la maxim de GitHub Copilot.

Mergi la Lecția 11, unde vom vedea cum să [integrazți AI Generativ cu Funcția de Apelare](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->