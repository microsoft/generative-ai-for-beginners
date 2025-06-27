<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-06-25T19:24:21+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "ro"
}
-->
# Construirea aplicațiilor AI cu cod redus

[![Construirea aplicațiilor AI cu cod redus](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.ro.png)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

## Introducere

Acum că am învățat cum să construim aplicații de generare de imagini, să discutăm despre codul redus. AI generativ poate fi utilizat într-o varietate de domenii, inclusiv cod redus, dar ce este codul redus și cum putem adăuga AI la acesta?

Construirea aplicațiilor și soluțiilor a devenit mai ușoară pentru dezvoltatorii tradiționali și non-dezvoltatori prin utilizarea platformelor de dezvoltare cu cod redus. Aceste platforme permit construirea aplicațiilor și soluțiilor cu puțin sau deloc cod. Acest lucru se realizează prin oferirea unui mediu de dezvoltare vizual care permite tragerea și plasarea componentelor pentru a construi aplicații și soluții. Astfel, se pot construi aplicații și soluții mai rapid și cu mai puține resurse. În această lecție, vom aprofunda modul de utilizare al codului redus și cum să îmbunătățim dezvoltarea cu cod redus folosind AI și Power Platform.

Power Platform oferă organizațiilor oportunitatea de a împuternici echipele lor să își construiască propriile soluții printr-un mediu intuitiv de cod redus sau fără cod. Acest mediu ajută la simplificarea procesului de construire a soluțiilor. Cu Power Platform, soluțiile pot fi construite în zile sau săptămâni în loc de luni sau ani. Power Platform constă din cinci produse cheie: Power Apps, Power Automate, Power BI, Power Pages și Copilot Studio.

Această lecție acoperă:

- Introducerea AI generativ în Power Platform
- Introducerea Copilot și cum să-l utilizăm
- Utilizarea AI generativ pentru a construi aplicații și fluxuri în Power Platform
- Înțelegerea modelelor AI în Power Platform cu AI Builder

## Obiective de învățare

Până la sfârșitul acestei lecții, vei putea:

- Înțelege cum funcționează Copilot în Power Platform.

- Construi o aplicație de urmărire a temelor studenților pentru startup-ul nostru educațional.

- Construi un flux de procesare a facturilor care utilizează AI pentru a extrage informații din facturi.

- Aplica cele mai bune practici atunci când utilizezi modelul AI Create Text cu GPT.

Instrumentele și tehnologiile pe care le vei utiliza în această lecție sunt:

- **Power Apps**, pentru aplicația de urmărire a temelor studenților, care oferă un mediu de dezvoltare cu cod redus pentru construirea aplicațiilor care urmăresc, gestionează și interacționează cu datele.

- **Dataverse**, pentru stocarea datelor pentru aplicația de urmărire a temelor studenților unde Dataverse va oferi o platformă de date cu cod redus pentru stocarea datelor aplicației.

- **Power Automate**, pentru fluxul de procesare a facturilor unde vei avea un mediu de dezvoltare cu cod redus pentru construirea fluxurilor de lucru care automatizează procesul de procesare a facturilor.

- **AI Builder**, pentru modelul AI de procesare a facturilor unde vei folosi modele AI preconstruite pentru a procesa facturile pentru startup-ul nostru.

## AI generativ în Power Platform

Îmbunătățirea dezvoltării și aplicării cu cod redus cu AI generativ este o zonă cheie de focalizare pentru Power Platform. Scopul este de a permite tuturor să construiască aplicații, site-uri, tablouri de bord și să automatizeze procesele cu AI, _fără a necesita expertiză în știința datelor_. Acest obiectiv este atins prin integrarea AI generativ în experiența de dezvoltare cu cod redus în Power Platform sub formă de Copilot și AI Builder.

### Cum funcționează acest lucru?

Copilot este un asistent AI care îți permite să construiești soluții Power Platform descriindu-ți cerințele într-o serie de pași conversaționali folosind limbajul natural. Poți, de exemplu, să instruiți asistentul AI să menționeze ce câmpuri va folosi aplicația ta și acesta va crea atât aplicația, cât și modelul de date subiacente sau poți specifica cum să configurezi un flux în Power Automate.

Poți utiliza funcționalitățile conduse de Copilot ca o caracteristică în ecranele aplicației tale pentru a permite utilizatorilor să descopere informații prin interacțiuni conversaționale.

AI Builder este o capacitate AI cu cod redus disponibilă în Power Platform care îți permite să folosești modele AI pentru a te ajuta să automatizezi procesele și să prezici rezultatele. Cu AI Builder poți aduce AI în aplicațiile și fluxurile tale care se conectează la datele tale în Dataverse sau în diverse surse de date cloud, cum ar fi SharePoint, OneDrive sau Azure.

Copilot este disponibil în toate produsele Power Platform: Power Apps, Power Automate, Power BI, Power Pages și Power Virtual Agents. AI Builder este disponibil în Power Apps și Power Automate. În această lecție, ne vom concentra pe cum să folosim Copilot și AI Builder în Power Apps și Power Automate pentru a construi o soluție pentru startup-ul nostru educațional.

### Copilot în Power Apps

Ca parte a Power Platform, Power Apps oferă un mediu de dezvoltare cu cod redus pentru construirea aplicațiilor care urmăresc, gestionează și interacționează cu datele. Este o suită de servicii de dezvoltare a aplicațiilor cu o platformă de date scalabilă și capacitatea de a se conecta la servicii cloud și date locale. Power Apps îți permite să construiești aplicații care rulează pe browsere, tablete și telefoane și pot fi partajate cu colegii. Power Apps facilitează utilizatorii în dezvoltarea aplicațiilor cu o interfață simplă, astfel încât fiecare utilizator de afaceri sau dezvoltator profesionist să poată construi aplicații personalizate. Experiența de dezvoltare a aplicațiilor este, de asemenea, îmbunătățită cu AI generativ prin Copilot.

Caracteristica asistentului AI copilot în Power Apps îți permite să descrii ce fel de aplicație ai nevoie și ce informații vrei ca aplicația ta să urmărească, colecteze sau afișeze. Copilot generează apoi o aplicație Canvas receptivă bazată pe descrierea ta. Poți personaliza apoi aplicația pentru a îndeplini nevoile tale. AI Copilot generează și sugerează o tabelă Dataverse cu câmpurile de care ai nevoie pentru a stoca datele pe care vrei să le urmărești și câteva date de exemplu. Vom analiza ce este Dataverse și cum poți să-l folosești în Power Apps în această lecție mai târziu. Poți personaliza apoi tabela pentru a îndeplini nevoile tale folosind caracteristica asistentului AI Copilot prin pași conversaționali. Această caracteristică este disponibilă direct de pe ecranul de start al Power Apps.

### Copilot în Power Automate

Ca parte a Power Platform, Power Automate permite utilizatorilor să creeze fluxuri de lucru automate între aplicații și servicii. Ajută la automatizarea proceselor de afaceri repetitive, cum ar fi comunicarea, colectarea datelor și aprobările de decizii. Interfața sa simplă permite utilizatorilor cu orice nivel de competență tehnică (de la începători la dezvoltatori experimentați) să automatizeze sarcinile de lucru. Experiența de dezvoltare a fluxului de lucru este, de asemenea, îmbunătățită cu AI generativ prin Copilot.

Caracteristica asistentului AI copilot în Power Automate îți permite să descrii ce fel de flux ai nevoie și ce acțiuni vrei ca fluxul tău să efectueze. Copilot generează apoi un flux bazat pe descrierea ta. Poți personaliza apoi fluxul pentru a îndeplini nevoile tale. AI Copilot generează și sugerează acțiunile de care ai nevoie pentru a efectua sarcina pe care vrei să o automatizezi. Vom analiza ce sunt fluxurile și cum le poți folosi în Power Automate în această lecție mai târziu. Poți personaliza apoi acțiunile pentru a îndeplini nevoile tale folosind caracteristica asistentului AI Copilot prin pași conversaționali. Această caracteristică este disponibilă direct de pe ecranul de start al Power Automate.

## Sarcină: Gestionarea temelor studenților și a facturilor pentru startup-ul nostru, folosind Copilot

Startup-ul nostru oferă cursuri online studenților. Startup-ul a crescut rapid și acum se luptă să țină pasul cu cererea pentru cursurile sale. Startup-ul te-a angajat ca dezvoltator Power Platform pentru a-i ajuta să construiască o soluție cu cod redus pentru a-i ajuta să gestioneze temele studenților și facturile. Soluția lor ar trebui să îi ajute să urmărească și să gestioneze temele studenților printr-o aplicație și să automatizeze procesul de procesare a facturilor printr-un flux de lucru. Ți s-a cerut să folosești AI generativ pentru a dezvolta soluția.

Când începi să folosești Copilot, poți utiliza [Biblioteca de sugestii Copilot pentru Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) pentru a începe cu sugestiile. Această bibliotecă conține o listă de sugestii pe care le poți folosi pentru a construi aplicații și fluxuri cu Copilot. Poți folosi, de asemenea, sugestiile din bibliotecă pentru a obține o idee despre cum să îți descrii cerințele către Copilot.

### Construiește o aplicație de urmărire a temelor studenților pentru startup-ul nostru

Educatorii de la startup-ul nostru s-au luptat să țină evidența temelor studenților. Au folosit o foaie de calcul pentru a urmări temele, dar acest lucru a devenit dificil de gestionat pe măsură ce numărul de studenți a crescut. Ei te-au rugat să construiești o aplicație care să îi ajute să urmărească și să gestioneze temele studenților. Aplicația ar trebui să le permită să adauge teme noi, să vizualizeze temele, să actualizeze temele și să șteargă temele. Aplicația ar trebui să permită, de asemenea, educatorilor și studenților să vizualizeze temele care au fost notate și cele care nu au fost notate.

Vei construi aplicația folosind Copilot în Power Apps urmând pașii de mai jos:

1. Accesează ecranul de start [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Folosește zona de text de pe ecranul de start pentru a descrie aplicația pe care vrei să o construiești. De exemplu, **_Vreau să construiesc o aplicație pentru a urmări și gestiona temele studenților_**. Apasă pe butonul **Trimite** pentru a trimite sugestia către AI Copilot.

![Descrie aplicația pe care vrei să o construiești](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.ro.png)

1. AI Copilot va sugera o tabelă Dataverse cu câmpurile de care ai nevoie pentru a stoca datele pe care vrei să le urmărești și câteva date de exemplu. Poți personaliza apoi tabela pentru a îndeplini nevoile tale folosind caracteristica asistentului AI Copilot prin pași conversaționali.

   > **Important**: Dataverse este platforma de date subiacente pentru Power Platform. Este o platformă de date cu cod redus pentru stocarea datelor aplicației. Este un serviciu gestionat complet care stochează datele în siguranță în Cloud-ul Microsoft și este provisionat în cadrul mediului tău Power Platform. Vine cu capabilități de guvernare a datelor integrate, cum ar fi clasificarea datelor, linia de date, controlul accesului fin și multe altele. Poți afla mai multe despre Dataverse [aici](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Câmpuri sugerate în noua ta tabelă](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.ro.png)

1. Educatorii doresc să trimită emailuri studenților care și-au depus temele pentru a-i ține la curent cu progresul temelor lor. Poți folosi Copilot pentru a adăuga un nou câmp în tabelă pentru a stoca emailul studentului. De exemplu, poți folosi următoarea sugestie pentru a adăuga un nou câmp în tabelă: **_Vreau să adaug o coloană pentru a stoca emailul studentului_**. Apasă pe butonul **Trimite** pentru a trimite sugestia către AI Copilot.

![Adăugarea unui nou câmp](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.ro.png)

1. AI Copilot va genera un nou câmp și poți personaliza câmpul pentru a îndeplini nevoile tale.

1. După ce ai terminat cu tabela, apasă pe butonul **Creează aplicația** pentru a crea aplicația.

1. AI Copilot va genera o aplicație Canvas receptivă bazată pe descrierea ta. Poți personaliza apoi aplicația pentru a îndeplini nevoile tale.

1. Pentru ca educatorii să trimită emailuri studenților, poți folosi Copilot pentru a adăuga un nou ecran în aplicație. De exemplu, poți folosi următoarea sugestie pentru a adăuga un nou ecran în aplicație: **_Vreau să adaug un ecran pentru a trimite emailuri studenților_**. Apasă pe butonul **Trimite** pentru a trimite sugestia către AI Copilot.

![Adăugarea unui nou ecran printr-o sugestie](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.ro.png)

1. AI Copilot va genera un nou ecran și poți personaliza ecranul pentru a îndeplini nevoile tale.

1. După ce ai terminat cu aplicația, apasă pe butonul **Salvează** pentru a salva aplicația.

1. Pentru a partaja aplicația cu educatorii, apasă pe butonul **Partajează** și apoi apasă din nou pe butonul **Partajează**. Poți partaja aplicația cu educatorii introducând adresele lor de email.

> **Tema ta pentru acasă**: Aplicația pe care tocmai ai construit-o este un început bun, dar poate fi îmbunătățită. Cu funcția de email, educatorii pot trimite emailuri studenților doar manual, fiind nevoiți să introducă emailurile. Poți folosi Copilot pentru a construi o automatizare care va permite educatorilor să trimită emailuri studenților automat atunci când își depun temele? Indiciul tău este că, cu sugestia potrivită, poți folosi Copilot în Power Automate pentru a construi acest lucru.

### Construiește o tabelă de informații despre facturi pentru startup-ul nostru

Echipa financiară a startup-ului nostru s-a luptat să țină evidența facturilor. Au folosit o foaie de calcul pentru a urmări facturile, dar acest lucru a devenit dificil de gestionat pe măsură ce numărul de facturi a crescut. Ei te-au rugat să construiești o tabelă care să îi ajute să stocheze, să urmărească și să gestioneze informațiile facturilor primite. Tabela ar trebui să fie utilizată pentru a construi o automatizare care va extrage toate informațiile facturii și le va stoca în tabelă. Tabela ar trebui să permită, de asemenea, echipei financiare să vizualizeze facturile care au fost plătite și cele care nu au fost plătite.

Power Platform are o platformă de date subiacente numită Dataverse care îți permite să stochezi datele pentru aplicațiile și soluțiile tale. Dataverse oferă o platformă de date cu cod redus pentru stocarea datelor aplicației. Este un serviciu gestionat complet care stochează datele în siguranță în Cloud-ul Microsoft și este provisionat în cadrul mediului tău Power Platform. Vine cu capabilități de guvernare a datelor integrate, cum ar fi clasificarea datelor, linia de date, controlul accesului fin și multe altele. Poți afla mai multe [despre Dataverse aici](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

De ce ar trebui să folosim Dataverse pentru startup-ul nostru? Tabelele standard și personalizate din Dataverse oferă o opțiune de stocare securizată și bazată pe cloud pentru datele tale. Tabelele îți permit să stochezi diferite tipuri de date, similar cu modul în care ai putea folosi mai multe foi de lucru într-un singur registru de lucru Excel. Poți folosi tabelele pentru a stoca date care sunt specifice organizației sau nevoilor tale de afaceri. Unele dintre beneficiile pe care startup-ul nostru le va
un text. - **Analiza Sentimentelor**: Acest model detectează sentimente pozitive, negative, neutre sau mixte în text. - **Cititor de Cărți de Vizită**: Acest model extrage informații din cărți de vizită. - **Recunoașterea Textului**: Acest model extrage text din imagini. - **Detectarea Obiectelor**: Acest model detectează și extrage obiecte din imagini. - **Procesarea Documentelor**: Acest model extrage informații din formulare. - **Procesarea Facturilor**: Acest model extrage informații din facturi. Cu Modelele AI Personalizate, poți aduce propriul tău model în AI Builder astfel încât să funcționeze ca orice model personalizat AI Builder, permițându-ți să antrenezi modelul folosind propriile date. Poți folosi aceste modele pentru a automatiza procesele și a prezice rezultate atât în Power Apps, cât și în Power Automate. Când folosești propriul model, există limitări care se aplică. Citește mai multe despre aceste [limitări](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst). ![Modele AI Builder](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.ro.png) 

## Sarcina #2 - Construiește un Flux de Procesare a Facturilor pentru Startup-ul nostru

Echipa de finanțe se confruntă cu dificultăți în procesarea facturilor. Au folosit un tabel pentru a urmări facturile, dar a devenit dificil de gestionat pe măsură ce numărul de facturi a crescut. Te-au rugat să construiești un flux de lucru care să-i ajute să proceseze facturile folosind AI. Fluxul de lucru ar trebui să le permită să extragă informații din facturi și să stocheze informațiile într-un tabel Dataverse. Fluxul de lucru ar trebui, de asemenea, să le permită să trimită un email echipei de finanțe cu informațiile extrase. Acum că știi ce este AI Builder și de ce ar trebui să-l folosești, să vedem cum poți folosi Modelul AI de Procesare a Facturilor din AI Builder, pe care l-am acoperit mai devreme, pentru a construi un flux de lucru care va ajuta echipa de finanțe să proceseze facturile. Pentru a construi un flux de lucru care va ajuta echipa de finanțe să proceseze facturile folosind Modelul AI de Procesare a Facturilor din AI Builder, urmează pașii de mai jos: 

1. Navighează la ecranul de start [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst). 
2. Folosește zona de text de pe ecranul de start pentru a descrie fluxul de lucru pe care vrei să-l construiești. De exemplu, **_Procesează o factură când ajunge în căsuța mea de email_**. Apasă pe butonul **Trimite** pentru a trimite solicitarea către AI Copilot. ![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.ro.png) 
3. AI Copilot va sugera acțiunile necesare pentru a realiza sarcina pe care vrei să o automatizezi. Poți apăsa pe butonul **Următorul** pentru a parcurge pașii următori. 
4. În pasul următor, Power Automate te va solicita să configurezi conexiunile necesare pentru flux. După ce ai terminat, apasă pe butonul **Creează flux** pentru a crea fluxul. 
5. AI Copilot va genera un flux și apoi poți personaliza fluxul pentru a se potrivi nevoilor tale. 
6. Actualizează declanșatorul fluxului și setează **Folderul** la folderul unde vor fi stocate facturile. De exemplu, poți seta folderul la **Inbox**. Apasă pe **Afișează opțiuni avansate** și setează **Numai cu atașamente** la **Da**. Acest lucru va asigura că fluxul rulează doar când un email cu un atașament este primit în folder. 
7. Elimină următoarele acțiuni din flux: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** și **Compose 4** deoarece nu le vei folosi. 
8. Elimină acțiunea **Condition** din flux deoarece nu o vei folosi. Ar trebui să arate ca în următoarea captură de ecran: ![power automate, remove actions](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.ro.png) 
9. Apasă pe butonul **Adaugă o acțiune** și caută **Dataverse**. Selectează acțiunea **Adaugă un nou rând**. 
10. La acțiunea **Extrage Informații din facturi**, actualizează **Fișierul Factură** pentru a indica **Conținutul Atașamentului** din email. Acest lucru va asigura că fluxul extrage informații din atașamentul facturii. 
11. Selectează **Tabelul** pe care l-ai creat anterior. De exemplu, poți selecta tabelul **Informații Factură**. Alege conținutul dinamic din acțiunea anterioară pentru a completa următoarele câmpuri: 
    - ID 
    - Sumă 
    - Dată 
    - Nume 
    - Status 
    - Setează **Statusul** la **În așteptare**. 
    - Email Furnizor 
    - Folosește conținutul dinamic **De la** din declanșatorul **Când un email nou sosește**. ![power automate add row](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.ro.png) 
12. După ce ai terminat cu fluxul, apasă pe butonul **Salvează** pentru a salva fluxul. Poți testa apoi fluxul trimițând un email cu o factură către folderul specificat în declanșator. 

> **Temă pentru acasă**: Fluxul pe care tocmai l-ai construit este un început bun, acum trebuie să te gândești cum poți construi o automatizare care va permite echipei noastre de finanțe să trimită un email către furnizor pentru a-i actualiza cu statusul curent al facturii lor. Sugestia ta: fluxul trebuie să ruleze când statusul facturii se schimbă.

## Folosește un Model AI de Generare Text în Power Automate

Modelul AI de Creare Text cu GPT în AI Builder îți permite să generezi text bazat pe o solicitare și este alimentat de Microsoft Azure OpenAI Service. Cu această capacitate, poți integra tehnologia GPT (Generative Pre-Trained Transformer) în aplicațiile și fluxurile tale pentru a construi o varietate de fluxuri automate și aplicații pline de informații.

Modelele GPT sunt antrenate extensiv pe cantități mari de date, permițându-le să producă text care seamănă îndeaproape cu limbajul uman atunci când li se oferă o solicitare. Când sunt integrate cu automatizarea fluxurilor de lucru, modelele AI precum GPT pot fi valorificate pentru a simplifica și automatiza o gamă largă de sarcini.

De exemplu, poți construi fluxuri pentru a genera automat text pentru o varietate de utilizări, cum ar fi: ciorne de emailuri, descrieri de produse și multe altele. De asemenea, poți folosi modelul pentru a genera text pentru o varietate de aplicații, cum ar fi chatbot-uri și aplicații de servicii pentru clienți care permit agenților de servicii pentru clienți să răspundă eficient și eficient la întrebările clienților.

![creează o solicitare](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.ro.png)

Pentru a învăța cum să folosești acest Model AI în Power Automate, parcurge modulul [Adaugă inteligență cu AI Builder și GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Felicitări! Continuă să înveți

După ce ai finalizat această lecție, consultă colecția noastră de [Învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți dezvolți cunoștințele despre AI Generativă!

Mergi la Lecția 11 unde vom analiza cum să [integrezi AI Generativă cu Apelarea Funcțiilor](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu suntem responsabili pentru niciun fel de neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.