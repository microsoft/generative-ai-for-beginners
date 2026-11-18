# Contribuții

Acest proiect primește cu plăcere contribuții și sugestii. Majoritatea contribuțiilor necesită să
fii de acord cu un Acord de Licență a Contribuitorului (CLA) prin care declari că ai dreptul,
și chiar acorzi, drepturile de a folosi contribuția ta. Pentru detalii, vizitează
<https://cla.microsoft.com>.

> Important: când traduci text în acest depozit, te rugăm să nu folosești traduceri automate. Vom verifica traducerile prin comunitate, deci te rugăm să te oferi voluntar pentru traduceri doar în limbile în care ai competență.

Când trimiți o cerere de pull, un CLA-bot va determina automat dacă trebuie
să furnizezi un CLA și va decora PR-ul corespunzător (ex., etichetă, comentariu). Urmează pur și simplu
instrucțiunile oferite de bot. Va trebui să faci acest lucru o singură dată pentru toate depozitele care folosesc CLA-ul nostru.

## Codul de conduită

Acest proiect a adoptat [Codul de Conduită Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Pentru mai multe informații citește [Întrebări frecvente despre Codul de Conduită](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) sau contactează [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Întrebare sau problemă?

Te rugăm să nu deschizi probleme pe GitHub pentru întrebări generale de suport, deoarece lista GitHub ar trebui folosită pentru cereri de funcționalități și raportări de erori. Astfel putem urmări mai ușor probleme reale sau bug-uri din cod și păstrăm discuția generală separată de codul efectiv.

## Greșeli de tastare, probleme, bug-uri și contribuții

Ori de câte ori trimiți modificări în depozitul Generative AI for Beginners, te rugăm să urmezi aceste recomandări.

* Întotdeauna fă fork la depozit în contul tău înainte de a face modificările
* Nu combina mai multe modificări într-o singură cerere de pull. De exemplu, trimite orice remediere de bug și actualizări de documentație în PR-uri separate
* Dacă cererea ta de pull arată conflicte de merge, asigură-te că actualizezi ramura locală main să fie o oglindă a depozitului principal înainte de a face modificări
* Dacă trimiți o traducere, te rugăm să creezi un singur PR pentru toate fișierele traduse, deoarece nu acceptăm traduceri parțiale pentru conținut
* Dacă trimiți corecturi de typo-uri sau documentație, poți combina modificările într-un singur PR acolo unde este potrivit

## Domeniul editorial și produse terțe

Acest curriculum se concentrează pe tehnologiile Microsoft și standarde deschise, neutre față de vendori. Contribuțiile trebuie să aibă un scop educațional clar și să nu fie destinate în principal introducerii sau promovării unui produs comercial terț, serviciu găzduit, rutare de modele, SDK, server MCP sau alte oferte specifice unui vendor.

Software-ul open-source și dependențele terțe pot fi menționate atunci când sunt necesare pentru a explica un standard deschis sau un scenariu de interoperabilitate, sunt prezentate neutru și nu sunt centrale pe un produs al unui vendor sau un punct final găzduit. Dacă propunerea ta include un produs sau serviciu specific unui vendor, deschide o problemă și obține aprobarea unui administrator înainte de a trimite un pull request.

Contribuitorii trebuie să dezvăluie orice angajare, proprietate, sponsorizare sau alte afilieri relevante cu un produs sau serviciu menționat în contribuția lor. Nu include afirmații nesusținute despre preț, performanță, securitate, confidențialitate sau comparații. Exemplele rulabile nu trebuie să transmită date ale cursanților sau să efectueze acțiuni publice printr-un serviciu terț extern în mod implicit.

## Ghid general pentru scris

- Asigură-te că toate URL-urile tale sunt încadrate în paranteze drepte urmate de paranteze rotunde fără spații suplimentare în jurul lor sau în interiorul lor `[]()`.
- Asigură-te că orice link relativ (adică linkuri către alte fișiere și foldere din depozit) începe cu un `./` referind un fișier sau folder din directorul de lucru curent sau un `../` referind un fișier sau folder dintr-un director părinte.
- Asigură-te că orice link relativ (adică linkuri către alte fișiere și foldere din depozit) are un ID de urmărire (adică `?` sau `&` apoi `wt.mc_id=` sau `WT.mc_id=`) la final.
- Asigură-te că orice URL din domeniile _github.com, microsoft.com, visualstudio.com, aka.ms și azure.com_ are un ID de urmărire (adică `?` sau `&` apoi `wt.mc_id=` sau `WT.mc_id=`) la final.
- Asigură-te că linkurile tale nu conțin o locație geografică specifică țării (ex., `/en-us/` sau `/en/`).
- Asigură-te că toate imaginile sunt stocate în folderul `./images`.
- Asigură-te că imaginile au nume descriptive folosind caractere englezești, cifre și cratime în numele imaginii tale.

## Fluxuri de lucru GitHub

Când trimiți o cerere de pull, patru fluxuri de lucru diferite vor fi declanșate pentru a valida regulile de mai sus.
Pur și simplu urmează instrucțiunile aici listate pentru a trece verificările fluxului de lucru.

- [Verifică căile relative rupte](#check-broken-relative-paths)
- [Verifică căile au urmărire](#check-paths-have-tracking)
- [Verifică că URL-urile au urmărire](#check-urls-have-tracking)
- [Verifică că URL-urile nu au locație geografică](#check-urls-dont-have-locale)

### Verifică căile relative rupte

Acest flux de lucru se asigură că orice cale relativă din fișierele tale funcționează.
Acest depozit este publicat pe pagini GitHub, așa că trebuie să fii foarte atent când tastezi linkurile care leagă totul pentru a nu direcționa pe cineva în locul greșit.

Pentru a te asigura că linkurile tale funcționează corect, folosește pur și simplu VS code pentru a verifica asta.

De exemplu, când treci cursorul peste orice link din fișierele tale, ți se va cere să urmezi linkul apăsând **ctrl + click**

![Captură de ecran VS code urmare linkuri](../../translated_images/ro/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Captură din VS code care arată promptul de a urma un link când treci cursorul pe el.")

Dacă dai clic pe un link și nu funcționează local, cu siguranță va declanșa fluxul de lucru și nu va funcționa pe GitHub.

Pentru a remedia această problemă, încearcă să tastezi linkul cu ajutorul VS code.

Când tastezi `./` sau `../`, VS code îți va sugera opțiuni disponibile conform a ceea ce ai tastat.

![Captură de ecran VS code selectare cale relativă](../../translated_images/ro/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Captură din VS code care arată promptul de a selecta o cale relativă dintr-o listă pop-up.")

Urmează calea dând clic pe fișierul sau folderul dorit și vei fi sigur că calea ta nu este ruptă.

Odată ce adaugi calea relativă corectă, salvează și împinge modificările, fluxul de lucru va fi declanșat din nou pentru a verifica modificările tale.
Dacă treci verificarea, poți continua.

### Verifică căile au urmărire

Acest flux de lucru se asigură că orice cale relativă are un cod de urmărire.
Acest depozit este publicat pe pagini GitHub, așa că trebuie să urmărim mișcarea între diferitele fișiere și foldere.

Pentru a te asigura că căile relative conțin cod de urmărire, verifică textul `?wt.mc_id=` la finalul căii.
Dacă este adăugat la căile tale relative, vei trece această verificare.

Dacă nu, poți primi următoarea eroare.

![Captură comentariu GitHub verificare lipsă urmărire căi](../../translated_images/ro/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Captură din comentariul github care arată lipsa codului de urmărire în căile relative")

Pentru a remedia această problemă, deschide calea fișierului semnalată de fluxul de lucru și adaugă ID-ul de urmărire la finalul căilor relative.

Odată ce adaugi ID-ul de urmărire, salvează și împinge modificările, fluxul de lucru va fi declanșat din nou pentru a verifica modificările.
Dacă treci verificarea, poți continua.

### Verifică că URL-urile au urmărire

Acest flux de lucru asigură că orice URL web conține cod de urmărire.
Acest depozit este disponibil tuturor, așa că trebuie să urmărim accesul pentru a ști de unde vine traficul.

Pentru a te asigura că URL-urile tale au cod de urmărire, verifică textul `?wt.mc_id=` la finalul URL-ului.
Dacă este adăugat la URL-urile tale, vei trece această verificare.

Dacă nu, poți primi următoarea eroare.

![Captură comentariu GitHub verificare lipsă urmărire URL](../../translated_images/ro/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Captură din comentariul github care arată lipsa codului de urmărire în URL-uri")

Pentru a remedia această problemă, deschide calea fișierului semnalată de fluxul de lucru și adaugă ID-ul de urmărire la finalul URL-urilor.

Odată ce adaugi ID-ul de urmărire, salvează și împinge modificările, fluxul de lucru va fi declanșat din nou pentru a verifica modificările.
Dacă treci verificarea, poți continua.

### Verifică că URL-urile nu conțin locație geografică

Acest flux de lucru asigură că niciun URL web nu conține o locație geografică specifică unei țări.
Acest depozit este disponibil tuturor din întreaga lume, așa că trebuie să te asiguri că nu incluzi locația geografică a țării tale în URL-uri.

Pentru a te asigura că URL-urile tale nu conțin o locație geografică specifică, verifică dacă textul `/en-us/` sau `/en/` sau orice altă locație de limbă nu apare nicăieri în URL.
Dacă nu este prezent în URL-urile tale, vei trece această verificare.

Dacă este prezent, poți primi următoarea eroare.

![Captură comentariu GitHub verificare locație țară în URL](../../translated_images/ro/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Captură din comentariul github care arată adăugarea locației țării în URL-uri")

Pentru a remedia această problemă, deschide calea fișierului semnalată de fluxul de lucru și elimină locația geografică din URL-uri.

Odată ce elimini locația geografică, salvează și împinge modificările, fluxul de lucru va fi declanșat din nou pentru a verifica modificările.
Dacă treci verificarea, poți continua.

Felicitări! Te vom contacta cât de curând posibil cu feedback despre contribuția ta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->