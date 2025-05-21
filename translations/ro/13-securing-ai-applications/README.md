<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:10:33+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "ro"
}
-->
# Securizarea aplicațiilor tale de AI generativ

[![Securizarea aplicațiilor tale de AI generativ](../../../translated_images/13-lesson-banner.c21a3a479f9ff14ad1f7c9b02bfe0d9a549b43497588334356f91073466a1283.ro.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Introducere

Această lecție va acoperi:

- Securitatea în contextul sistemelor AI.
- Riscuri și amenințări comune pentru sistemele AI.
- Metode și considerații pentru securizarea sistemelor AI.

## Obiective de învățare

După completarea acestei lecții, vei avea o înțelegere a:

- Amenințărilor și riscurilor pentru sistemele AI.
- Metode și practici comune pentru securizarea sistemelor AI.
- Cum implementarea testării de securitate poate preveni rezultate neașteptate și erodarea încrederii utilizatorilor.

## Ce înseamnă securitatea în contextul AI generativ?

Pe măsură ce tehnologiile de Inteligență Artificială (AI) și Învățare Automată (ML) ne modelează tot mai mult viețile, este esențial să protejăm nu doar datele clienților, ci și sistemele AI în sine. AI/ML este utilizat tot mai mult pentru susținerea proceselor de luare a deciziilor de mare valoare în industrii unde o decizie greșită poate avea consecințe serioase.

Iată punctele cheie de luat în considerare:

- **Impactul AI/ML**: AI/ML au impacturi semnificative asupra vieții de zi cu zi și, ca atare, protejarea lor a devenit esențială.
- **Provocări de securitate**: Acest impact pe care îl au AI/ML necesită atenție adecvată pentru a aborda necesitatea de a proteja produsele bazate pe AI de atacuri sofisticate, fie de la troli, fie de la grupuri organizate.
- **Probleme strategice**: Industria tehnologică trebuie să abordeze proactiv provocările strategice pentru a asigura siguranța pe termen lung a clienților și securitatea datelor.

În plus, modelele de Învățare Automată nu pot discerne între inputuri malițioase și date anomale benigne. O sursă semnificativă de date de antrenament este derivată din seturi de date publice necurate și nemoderate, deschise contribuțiilor de la terți. Atacatorii nu trebuie să compromită seturile de date când pot contribui liber la ele. În timp, datele malițioase cu încredere scăzută devin date de încredere cu încredere ridicată, dacă structura/formatul datelor rămâne corect.

De aceea este crucial să asigurăm integritatea și protecția depozitelor de date pe care modelele tale le folosesc pentru a lua decizii.

## Înțelegerea amenințărilor și riscurilor AI

În termeni de AI și sisteme conexe, otrăvirea datelor se evidențiază ca cea mai semnificativă amenințare de securitate astăzi. Otrăvirea datelor este atunci când cineva modifică intenționat informațiile folosite pentru a antrena un AI, cauzându-l să facă greșeli. Aceasta se datorează absenței metodelor standardizate de detectare și atenuare, combinată cu dependența noastră de seturi de date publice necurate sau neîncredere pentru antrenament. Pentru a menține integritatea datelor și a preveni un proces de antrenament defectuos, este crucial să urmărim originea și linia datelor tale. Altfel, vechea zicală „gunoi intră, gunoi iese” se aplică, ducând la compromiterea performanței modelului.

Iată exemple de cum otrăvirea datelor poate afecta modelele tale:

1. **Inversarea etichetelor**: Într-o sarcină de clasificare binară, un adversar inversează intenționat etichetele unui subset mic de date de antrenament. De exemplu, mostrele benigne sunt etichetate ca malițioase, determinând modelul să învețe asocieri incorecte.\
   **Exemplu**: Un filtru de spam care clasifică greșit emailurile legitime ca spam din cauza etichetelor manipulate.
2. **Otrăvirea caracteristicilor**: Un atacator modifică subtil caracteristicile în datele de antrenament pentru a introduce bias sau a induce în eroare modelul.\
   **Exemplu**: Adăugarea de cuvinte-cheie irelevante la descrierile produselor pentru a manipula sistemele de recomandare.
3. **Injectarea datelor**: Injectarea de date malițioase în setul de antrenament pentru a influența comportamentul modelului.\
   **Exemplu**: Introducerea de recenzii false ale utilizatorilor pentru a denatura rezultatele analizei sentimentului.
4. **Atacuri prin ușă din spate**: Un adversar introduce un model ascuns (ușă din spate) în datele de antrenament. Modelul învață să recunoască acest model și se comportă malițios când este declanșat.\
   **Exemplu**: Un sistem de recunoaștere facială antrenat cu imagini cu ușă din spate care identifică greșit o persoană specifică.

Corporația MITRE a creat [ATLAS (Peisajul Amenințărilor Adversariale pentru Sistemele de Inteligență Artificială)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), o bază de cunoștințe despre tactici și tehnici utilizate de adversari în atacurile reale asupra sistemelor AI.

> Există un număr tot mai mare de vulnerabilități în sistemele activate de AI, pe măsură ce integrarea AI crește suprafața de atac a sistemelor existente dincolo de cele ale atacurilor cibernetice tradiționale. Am dezvoltat ATLAS pentru a crește conștientizarea acestor vulnerabilități unice și în evoluție, pe măsură ce comunitatea globală integrează tot mai mult AI în diverse sisteme. ATLAS este modelat după cadrul MITRE ATT&CK® și tacticile, tehnicile și procedurile (TTP) ale acestuia sunt complementare celor din ATT&CK.

La fel ca cadrul MITRE ATT&CK®, care este utilizat pe scară largă în securitatea cibernetică tradițională pentru planificarea scenariilor avansate de emulare a amenințărilor, ATLAS oferă un set de TTP-uri ușor de căutat care pot ajuta la o mai bună înțelegere și pregătire pentru apărarea împotriva atacurilor emergente.

În plus, Proiectul de Securitate a Aplicațiilor Web Deschise (OWASP) a creat o "[listă de top 10](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" a celor mai critice vulnerabilități găsite în aplicațiile care utilizează LLM-uri. Lista evidențiază riscurile amenințărilor precum otrăvirea datelor menționată anterior, împreună cu altele precum:

- **Injectarea de sugestii**: o tehnică prin care atacatorii manipulează un Model de Limbaj Mare (LLM) prin intrări atent elaborate, determinându-l să se comporte în afara comportamentului său intenționat.
- **Vulnerabilități ale lanțului de aprovizionare**: Componentele și software-ul care alcătuiesc aplicațiile utilizate de un LLM, cum ar fi modulele Python sau seturile de date externe, pot fi ele însele compromise, ducând la rezultate neașteptate, introducerea de biasuri și chiar vulnerabilități în infrastructura de bază.
- **Supradependență**: LLM-urile sunt imperfecte și au fost predispuse să halucineze, oferind rezultate inexacte sau nesigure. În mai multe circumstanțe documentate, oamenii au luat rezultatele la valoarea nominală, ducând la consecințe negative neintenționate în lumea reală.

Rod Trent, Cloud Advocate la Microsoft, a scris un ebook gratuit, [Trebuie să înveți securitatea AI](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), care aprofundează aceste și alte amenințări emergente ale AI și oferă îndrumări extinse despre cum să abordezi cel mai bine aceste scenarii.

## Testarea securității pentru sistemele AI și LLM-uri

Inteligența artificială (AI) transformă diverse domenii și industrii, oferind noi posibilități și beneficii pentru societate. Cu toate acestea, AI prezintă și provocări și riscuri semnificative, cum ar fi confidențialitatea datelor, biasul, lipsa de explicabilitate și utilizarea potențială greșită. Prin urmare, este crucial să ne asigurăm că sistemele AI sunt securizate și responsabile, ceea ce înseamnă că respectă standardele etice și legale și pot fi de încredere de către utilizatori și părțile interesate.

Testarea securității este procesul de evaluare a securității unui sistem AI sau LLM, prin identificarea și exploatarea vulnerabilităților lor. Aceasta poate fi realizată de către dezvoltatori, utilizatori sau auditori terți, în funcție de scopul și domeniul testării. Unele dintre cele mai comune metode de testare a securității pentru sistemele AI și LLM-uri sunt:

- **Sanitizarea datelor**: Acesta este procesul de eliminare sau anonimizare a informațiilor sensibile sau private din datele de antrenament sau intrările unui sistem AI sau LLM. Sanitizarea datelor poate ajuta la prevenirea scurgerii de date și manipulării malițioase prin reducerea expunerii datelor confidențiale sau personale.
- **Testarea adversarială**: Acesta este procesul de generare și aplicare a exemplelor adversariale la intrările sau ieșirile unui sistem AI sau LLM pentru a evalua robustețea și rezistența acestuia împotriva atacurilor adversariale. Testarea adversarială poate ajuta la identificarea și atenuarea vulnerabilităților și slăbiciunilor unui sistem AI sau LLM care pot fi exploatate de atacatori.
- **Verificarea modelului**: Acesta este procesul de verificare a corectitudinii și completitudinii parametrilor modelului sau arhitecturii unui sistem AI sau LLM. Verificarea modelului poate ajuta la detectarea și prevenirea furtului de model prin asigurarea că modelul este protejat și autentificat.
- **Validarea ieșirii**: Acesta este procesul de validare a calității și fiabilității ieșirii unui sistem AI sau LLM. Validarea ieșirii poate ajuta la detectarea și corectarea manipulării malițioase prin asigurarea că ieșirea este consistentă și precisă.

OpenAI, un lider în sistemele AI, a stabilit o serie de _evaluări de siguranță_ ca parte a inițiativei lor de rețea de echipă roșie, menită să testeze ieșirile sistemelor AI în speranța de a contribui la siguranța AI.

> Evaluările pot varia de la teste simple de întrebări și răspunsuri la simulări mai complexe. Ca exemple concrete, iată evaluări de probă dezvoltate de OpenAI pentru evaluarea comportamentelor AI din mai multe unghiuri:

#### Persuasiune

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Cât de bine poate un sistem AI păcăli un alt sistem AI să spună un cuvânt secret?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Cât de bine poate un sistem AI convinge un alt sistem AI să doneze bani?
- [Propunere de vot](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Cât de bine poate un sistem AI influența sprijinul unui alt sistem AI pentru o propunere politică?

#### Steganografie (mesaje ascunse)

- [Steganografie](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Cât de bine poate un sistem AI să transmită mesaje secrete fără a fi prins de un alt sistem AI?
- [Compresia textului](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Cât de bine poate un sistem AI comprima și decomprima mesaje, pentru a permite ascunderea mesajelor secrete?
- [Punctul Schelling](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Cât de bine poate un sistem AI să se coordoneze cu un alt sistem AI, fără comunicare directă?

### Securitatea AI

Este imperativ să ne propunem să protejăm sistemele AI de atacuri malițioase, utilizare greșită sau consecințe neintenționate. Acest lucru include luarea de măsuri pentru a asigura siguranța, fiabilitatea și încrederea sistemelor AI, cum ar fi:

- Securizarea datelor și algoritmilor care sunt folosiți pentru a antrena și rula modele AI
- Prevenirea accesului neautorizat, manipulării sau sabotării sistemelor AI
- Detectarea și atenuarea biasului, discriminării sau problemelor etice în sistemele AI
- Asigurarea responsabilității, transparenței și explicabilității deciziilor și acțiunilor AI
- Alinierea obiectivelor și valorilor sistemelor AI cu cele ale oamenilor și societății

Securitatea AI este importantă pentru asigurarea integrității, disponibilității și confidențialității sistemelor și datelor AI. Unele dintre provocările și oportunitățile securității AI sunt:

- Oportunitate: Integrarea AI în strategiile de securitate cibernetică, deoarece poate juca un rol crucial în identificarea amenințărilor și îmbunătățirea timpilor de răspuns. AI poate ajuta la automatizarea și augmentarea detectării și atenuării atacurilor cibernetice, cum ar fi phishing-ul, malware-ul sau ransomware-ul.
- Provocare: AI poate fi folosită și de adversari pentru a lansa atacuri sofisticate, cum ar fi generarea de conținut fals sau înșelător, impersonarea utilizatorilor sau exploatarea vulnerabilităților în sistemele AI. Prin urmare, dezvoltatorii AI au o responsabilitate unică de a proiecta sisteme care sunt robuste și rezistente împotriva utilizării greșite.

### Protecția datelor

LLM-urile pot prezenta riscuri pentru confidențialitatea și securitatea datelor pe care le utilizează. De exemplu, LLM-urile pot memora și scurge informații sensibile din datele lor de antrenament, cum ar fi nume personale, adrese, parole sau numere de carduri de credit. Ele pot fi, de asemenea, manipulate sau atacate de actori malițioși care doresc să exploateze vulnerabilitățile sau biasurile lor. Prin urmare, este important să fim conștienți de aceste riscuri și să luăm măsuri adecvate pentru a proteja datele utilizate cu LLM-uri. Există câțiva pași pe care îi poți lua pentru a proteja datele utilizate cu LLM-uri. Acești pași includ:

- **Limitarea cantității și tipului de date pe care le partajezi cu LLM-uri**: Partajează doar datele care sunt necesare și relevante pentru scopurile intenționate și evită partajarea oricăror date care sunt sensibile, confidențiale sau personale. Utilizatorii ar trebui, de asemenea, să anonimizeze sau să cripteze datele pe care le partajează cu LLM-uri, cum ar fi prin eliminarea sau mascarea oricărei informații de identificare sau utilizarea canalelor de comunicare securizate.
- **Verificarea datelor pe care le generează LLM-urile**: Verifică întotdeauna acuratețea și calitatea ieșirii generate de LLM-uri pentru a te asigura că nu conțin informații nedorite sau nepotrivite.
- **Raportarea și alertarea oricăror breșe de date sau incidente**: Fii vigilent la orice activități sau comportamente suspecte sau anormale ale LLM-urilor, cum ar fi generarea de texte care sunt irelevante, inexacte, ofensatoare sau dăunătoare. Acesta ar putea fi un indiciu al unei breșe de date sau al unui incident de securitate.

Securitatea, guvernanța și conformitatea datelor sunt critice pentru orice organizație care dorește să valorifice puterea datelor și AI într-un mediu multi-cloud. Securizarea și guvernarea tuturor datelor tale este o întreprindere complexă

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.