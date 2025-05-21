<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:38:00+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "ro"
}
-->
# Introducere în AI Generativ și Modele de Limbaj de Mari Dimensiuni

_(Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

AI generativ este inteligența artificială capabilă să genereze text, imagini și alte tipuri de conținut. Ceea ce o face o tehnologie fantastică este că democratizează AI-ul, oricine poate să o folosească cu doar un prompt text, o propoziție scrisă într-un limbaj natural. Nu este nevoie să înveți un limbaj precum Java sau SQL pentru a realiza ceva semnificativ, tot ce ai nevoie este să folosești limbajul tău, să spui ce vrei și vei primi o sugestie de la un model AI. Aplicațiile și impactul sunt uriașe, poți scrie sau înțelege rapoarte, scrie aplicații și multe altele, toate în câteva secunde.

În acest curriculum, vom explora cum startup-ul nostru utilizează AI generativ pentru a debloca noi scenarii în lumea educației și cum abordăm provocările inevitabile asociate cu implicațiile sociale ale aplicării sale și limitările tehnologice.

## Introducere

Această lecție va acoperi:

- Introducerea în scenariul de afaceri: ideea și misiunea startup-ului nostru.
- AI generativ și cum am ajuns la peisajul tehnologic actual.
- Funcționarea internă a unui model de limbaj de mari dimensiuni.
- Principalele capabilități și cazuri de utilizare practică ale modelelor de limbaj de mari dimensiuni.

## Obiective de învățare

După finalizarea acestei lecții, vei înțelege:

- Ce este AI generativ și cum funcționează modelele de limbaj de mari dimensiuni.
- Cum poți folosi modelele de limbaj de mari dimensiuni pentru diferite cazuri de utilizare, cu un accent pe scenariile educaționale.

## Scenariu: startup-ul nostru educațional

Inteligența Artificială (AI) Generativă reprezintă vârful tehnologiei AI, depășind limitele a ceea ce odată părea imposibil. Modelele de AI generativ au mai multe capabilități și aplicații, dar pentru acest curriculum vom explora cum revoluționează educația printr-un startup fictiv. Vom face referire la acest startup ca _startup-ul nostru_. Startup-ul nostru activează în domeniul educației cu o misiune ambițioasă de

> _îmbunătățire a accesibilității în învățare, la nivel global, asigurând acces echitabil la educație și oferind experiențe de învățare personalizate fiecărui cursant, conform nevoilor sale_.

Echipa noastră de startup este conștientă că nu vom putea atinge acest obiectiv fără a folosi unul dintre cele mai puternice instrumente ale vremurilor moderne – Modelele de Limbaj de Mari Dimensiuni (LLMs).

AI generativ este așteptat să revoluționeze modul în care învățăm și predăm astăzi, cu studenți care au la dispoziție profesori virtuali 24 de ore pe zi, care oferă cantități vaste de informații și exemple, și profesori care pot folosi instrumente inovatoare pentru a evalua studenții și a oferi feedback.

Pentru a începe, să definim câteva concepte de bază și termeni pe care îi vom folosi pe parcursul curriculumului.

## Cum am ajuns la AI generativ?

În ciuda _hype-ului_ extraordinar creat recent de anunțurile modelelor de AI generativ, această tehnologie este în dezvoltare de zeci de ani, cu primele eforturi de cercetare datând din anii '60. Suntem acum într-un punct în care AI are capacități cognitive umane, cum ar fi conversația, așa cum arată, de exemplu, [OpenAI ChatGPT](https://openai.com/chatgpt) sau [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), care folosește și un model GPT pentru conversațiile de căutare pe web Bing.

Întorcându-ne puțin, primele prototipuri de AI au constat în chatbots scrise, bazându-se pe o bază de cunoștințe extrasă dintr-un grup de experți și reprezentată într-un computer. Răspunsurile din baza de cunoștințe erau declanșate de cuvinte cheie apărute în textul de intrare. Cu toate acestea, a devenit curând clar că o astfel de abordare, folosind chatbots scrise, nu se scala bine.

### O abordare statistică a AI: Învățarea Automată

Un punct de cotitură a sosit în anii '90, odată cu aplicarea unei abordări statistice în analiza textului. Acest lucru a condus la dezvoltarea de noi algoritmi – cunoscuți sub numele de învățare automată – capabili să învețe tipare din date fără a fi programați explicit. Această abordare permite mașinilor să simuleze înțelegerea limbajului uman: un model statistic este antrenat pe perechi text-etichete, permițând modelului să clasifice textul de intrare necunoscut cu o etichetă predefinită care reprezintă intenția mesajului.

### Rețele neuronale și asistenții virtuali moderni

În ultimii ani, evoluția tehnologică a hardware-ului, capabil să gestioneze cantități mai mari de date și calcule mai complexe, a încurajat cercetarea în AI, conducând la dezvoltarea de algoritmi avansați de învățare automată cunoscuți sub numele de rețele neuronale sau algoritmi de învățare profundă.

Rețelele neuronale (și în special Rețelele Neuronale Recurente – RNNs) au îmbunătățit semnificativ procesarea limbajului natural, permițând reprezentarea semnificației textului într-un mod mai semnificativ, valorificând contextul unui cuvânt într-o propoziție.

Aceasta este tehnologia care a alimentat asistenții virtuali născuți în primul deceniu al noului secol, foarte competenți în interpretarea limbajului uman, identificarea unei nevoi și îndeplinirea unei acțiuni pentru a o satisface – cum ar fi răspunsul cu un script predefinit sau consumarea unui serviciu terț.

### Prezentul, AI Generativ

Așa am ajuns la AI generativ de astăzi, care poate fi văzut ca un subset al învățării profunde.

După decenii de cercetare în domeniul AI, o nouă arhitectură de model – numită _Transformer_ – a depășit limitele RNN-urilor, fiind capabilă să primească secvențe mult mai lungi de text ca intrare. Transformerele se bazează pe mecanismul de atenție, permițând modelului să acorde greutăți diferite intrărilor pe care le primește, „acordând mai multă atenție” acolo unde informațiile cele mai relevante sunt concentrate, indiferent de ordinea lor în secvența de text.

Cele mai recente modele de AI generativ – cunoscute și sub numele de Modele de Limbaj de Mari Dimensiuni (LLMs), deoarece lucrează cu intrări și ieșiri textuale – sunt într-adevăr bazate pe această arhitectură. Ceea ce este interesant la aceste modele – antrenate pe o cantitate uriașă de date nelabelate din surse diverse, cum ar fi cărți, articole și site-uri web – este că pot fi adaptate la o varietate largă de sarcini și pot genera text gramatical corect cu o aparență de creativitate. Așadar, nu numai că au îmbunătățit incredibil capacitatea unei mașini de a „înțelege” un text de intrare, dar au permis capacitatea lor de a genera un răspuns original în limbaj uman.

## Cum funcționează modelele de limbaj de mari dimensiuni?

În capitolul următor vom explora diferite tipuri de modele de AI generativ, dar pentru moment să vedem cum funcționează modelele de limbaj de mari dimensiuni, cu un accent pe modelele OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizare, text în numere**: Modelele de Limbaj de Mari Dimensiuni primesc un text ca intrare și generează un text ca ieșire. Totuși, fiind modele statistice, funcționează mult mai bine cu numere decât cu secvențe de text. De aceea, fiecare intrare în model este procesată de un tokenizer, înainte de a fi utilizată de modelul de bază. Un token este un fragment de text – constând dintr-un număr variabil de caractere, astfel încât sarcina principală a tokenizer-ului este să împartă intrarea într-un șir de tokenuri. Apoi, fiecare token este mapat cu un index de token, care este codificarea în număr întreg a fragmentului de text original.

- **Prezicerea tokenurilor de ieșire**: Dat fiind n tokenuri ca intrare (cu max n variind de la un model la altul), modelul este capabil să prezică un token ca ieșire. Acest token este apoi încorporat în intrarea iterației următoare, într-un model de fereastră extinsă, permițând o experiență mai bună a utilizatorului de a obține o (sau mai multe) propoziții ca răspuns. Acest lucru explică de ce, dacă ai folosit vreodată ChatGPT, ai observat că uneori pare să se oprească la mijlocul unei propoziții.

- **Procesul de selecție, distribuția probabilității**: Tokenul de ieșire este ales de model în funcție de probabilitatea sa de a apărea după secvența curentă de text. Acest lucru se datorează faptului că modelul prezice o distribuție a probabilității asupra tuturor „următoarelor tokenuri” posibile, calculată pe baza antrenamentului său. Totuși, nu întotdeauna este ales tokenul cu cea mai mare probabilitate din distribuția rezultată. Se adaugă un grad de aleatoriu acestei alegeri, în așa fel încât modelul să acționeze într-o manieră nedeterministă - nu obținem același rezultat exact pentru aceeași intrare. Acest grad de aleatoriu este adăugat pentru a simula procesul de gândire creativă și poate fi ajustat folosind un parametru de model numit temperatură.

## Cum poate startup-ul nostru să utilizeze Modelele de Limbaj de Mari Dimensiuni?

Acum că avem o mai bună înțelegere a funcționării interne a unui model de limbaj de mari dimensiuni, să vedem câteva exemple practice ale celor mai comune sarcini pe care le pot îndeplini destul de bine, cu un ochi la scenariul nostru de afaceri. Am spus că principala capacitate a unui Model de Limbaj de Mari Dimensiuni este _generarea unui text de la zero, pornind de la o intrare textuală, scrisă într-un limbaj natural_.

Dar ce fel de intrare și ieșire textuală?
Intrarea unui model de limbaj de mari dimensiuni este cunoscută ca un prompt, în timp ce ieșirea este cunoscută ca o completare, termen care se referă la mecanismul modelului de generare a următorului token pentru a completa intrarea curentă. Vom aprofunda ce este un prompt și cum să-l proiectăm într-un mod care să obținem maximum din modelul nostru. Dar pentru moment, să spunem doar că un prompt poate include:

- O **instrucțiune** care specifică tipul de ieșire pe care o așteptăm de la model. Această instrucțiune uneori poate include exemple sau date suplimentare.

  1. Rezumarea unui articol, a unei cărți, a recenziilor de produse și altele, împreună cu extragerea de informații din date nestructurate.
  
  2. Crearea și proiectarea creativă a unui articol, a unui eseu, a unei teme sau altele.

- O **întrebare**, adresată sub formă de conversație cu un agent.

- Un fragment de **text de completat**, care implicit este o cerere de asistență la scriere.

- Un fragment de **cod** împreună cu cererea de a-l explica și documenta, sau un comentariu care cere generarea unei bucăți de cod care să îndeplinească o sarcină specifică.

Exemplele de mai sus sunt destul de simple și nu sunt menite să fie o demonstrație exhaustivă a capacităților Modelelor de Limbaj de Mari Dimensiuni. Ele sunt menite să arate potențialul utilizării AI generativ, în special, dar nu limitat la contexte educaționale.

De asemenea, ieșirea unui model de AI generativ nu este perfectă și uneori creativitatea modelului poate lucra împotriva sa, rezultând într-o ieșire care este o combinație de cuvinte pe care utilizatorul uman o poate interpreta ca o mistificare a realității, sau poate fi ofensivă. AI generativ nu este inteligent - cel puțin în definiția mai cuprinzătoare a inteligenței, care include raționamentul critic și creativ sau inteligența emoțională; nu este determinist și nu este de încredere, deoarece fabricațiile, cum ar fi referințele eronate, conținutul și afirmațiile, pot fi combinate cu informații corecte și prezentate într-o manieră convingătoare și încrezătoare. În lecțiile următoare, ne vom ocupa de toate aceste limitări și vom vedea ce putem face pentru a le atenua.

## Sarcină

Sarcina ta este să citești mai multe despre [AI generativ](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) și să încerci să identifici un domeniu în care ai adăuga AI generativ astăzi care nu îl are. Cum ar fi diferit impactul față de a face lucrurile în modul "vechi", poți face ceva ce nu puteai înainte sau ești mai rapid? Scrie un rezumat de 300 de cuvinte despre cum ar arăta startup-ul tău AI de vis și include titluri precum "Problema", "Cum aș folosi AI", "Impactul" și opțional un plan de afaceri.

Dacă ai făcut această sarcină, s-ar putea să fii gata să aplici la incubatorul Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) oferim credite pentru Azure, OpenAI, mentorat și multe altele, verifică-l!

## Verificarea cunoștințelor

Ce este adevărat despre modelele de limbaj de mari dimensiuni?

1. Primești același răspuns de fiecare dată.
2. Face lucrurile perfect, excelent la adunarea numerelor, produce cod funcțional etc.
3. Răspunsul poate varia în ciuda utilizării aceluiași prompt. Este, de asemenea, excelent la oferirea unui prim draft de ceva, fie text sau cod. Dar trebuie să îmbunătățești rezultatele.

R: 3, un LLM este nedeterminist, răspunsul variază, totuși, poți controla variația sa printr-o setare de temperatură. De asemenea, nu ar trebui să te aștepți să facă lucrurile perfect, este aici pentru a face munca grea pentru tine, ceea ce înseamnă adesea că obții o primă încercare bună la ceva pe care trebuie să o îmbunătățești treptat.

## Lucru Grozav! Continuă Călătoria

După finalizarea acestei lecții, verifică colecția noastră de învățare [Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți îmbunătățești cunoștințele despre AI generativ!

Treci la Lecția 2 unde vom analiza cum să [explorăm și să comparăm diferite tipuri de LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să obținem acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu suntem responsabili pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.