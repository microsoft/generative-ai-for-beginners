<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:37:08+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "ro"
}
-->
# Framework-uri pentru Rețele Neuronale

Așa cum am învățat deja, pentru a putea antrena rețele neuronale eficient, trebuie să facem două lucruri:

* Să operăm cu tensori, de exemplu să înmulțim, să adunăm și să calculăm funcții precum sigmoid sau softmax
* Să calculăm gradientele tuturor expresiilor, pentru a putea efectua optimizarea prin gradient descendent

Deși biblioteca `numpy` poate face prima parte, avem nevoie de un mecanism pentru a calcula gradientele. În cadrul nostru, pe care l-am dezvoltat în secțiunea anterioară, a trebuit să programăm manual toate funcțiile derivate în metoda `backward`, care realizează backpropagation. Ideal, un framework ar trebui să ne ofere posibilitatea de a calcula gradientele *oricărei expresii* pe care o putem defini.

Un alt aspect important este să putem efectua calcule pe GPU sau pe alte unități specializate de calcul, cum ar fi TPU. Antrenarea rețelelor neuronale profunde necesită *foarte multe* calcule, iar posibilitatea de a paraleliza aceste calcule pe GPU-uri este esențială.

> ✅ Termenul „paraleliza” înseamnă distribuirea calculelor pe mai multe dispozitive.

În prezent, cele două framework-uri de rețele neuronale cele mai populare sunt: TensorFlow și PyTorch. Ambele oferă o API la nivel scăzut pentru a opera cu tensori atât pe CPU, cât și pe GPU. Deasupra acestei API la nivel scăzut, există și o API la nivel înalt, numită Keras, respectiv PyTorch Lightning.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| PyTorch

**API-urile la nivel scăzut** din ambele framework-uri permit construirea așa-numitelor **grafuri computaționale**. Acest graf definește cum să calculăm ieșirea (de obicei funcția de pierdere) pentru parametrii de intrare dați și poate fi trimis pentru calcul pe GPU, dacă este disponibil. Există funcții pentru a diferenția acest graf computațional și a calcula gradientele, care pot fi apoi folosite pentru optimizarea parametrilor modelului.

**API-urile la nivel înalt** tratează rețelele neuronale ca o **secvență de straturi** și facilitează mult construirea majorității rețelelor neuronale. Antrenarea modelului necesită de obicei pregătirea datelor și apoi apelarea funcției `fit` pentru a face treaba.

API-ul la nivel înalt îți permite să construiești rapid rețele neuronale tipice fără să te preocupi de multe detalii. În același timp, API-ul la nivel scăzut oferă mult mai mult control asupra procesului de antrenare, motiv pentru care este folosit frecvent în cercetare, când lucrezi cu arhitecturi noi de rețele neuronale.

Este important să înțelegi că poți folosi ambele API-uri împreună, de exemplu poți dezvolta propria arhitectură de strat de rețea folosind API-ul la nivel scăzut și apoi să o folosești într-o rețea mai mare construită și antrenată cu API-ul la nivel înalt. Sau poți defini o rețea folosind API-ul la nivel înalt ca o secvență de straturi și apoi să folosești propriul tău ciclu de antrenare la nivel scăzut pentru optimizare. Ambele API-uri folosesc aceleași concepte de bază și sunt proiectate să funcționeze bine împreună.

## Învățare

În acest curs, oferim majoritatea conținutului atât pentru PyTorch, cât și pentru TensorFlow. Poți alege framework-ul preferat și să parcurgi doar notebook-urile corespunzătoare. Dacă nu ești sigur ce framework să alegi, citește câteva discuții de pe internet despre **PyTorch vs. TensorFlow**. Poți, de asemenea, să arunci o privire la ambele framework-uri pentru a înțelege mai bine.

Ori de câte ori este posibil, vom folosi API-urile la nivel înalt pentru simplitate. Totuși, considerăm că este important să înțelegi cum funcționează rețelele neuronale de la bază, așa că la început vom lucra cu API-ul la nivel scăzut și cu tensori. Dacă vrei să începi rapid și nu vrei să pierzi mult timp cu aceste detalii, poți sări peste ele și să mergi direct la notebook-urile cu API la nivel înalt.

## ✍️ Exerciții: Framework-uri

Continuă-ți învățarea în următoarele notebook-uri:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

După ce stăpânești framework-urile, să recapitulăm noțiunea de overfitting.

# Overfitting

Overfitting-ul este un concept extrem de important în învățarea automată și este esențial să îl înțelegem corect!

Consideră următoarea problemă de aproximare a 5 puncte (reprezentate prin `x` pe graficele de mai jos):

!linear | overfit
-------------------------|--------------------------
**Model liniar, 2 parametri** | **Model neliniar, 7 parametri**
Eroare de antrenare = 5.3 | Eroare de antrenare = 0
Eroare de validare = 5.1 | Eroare de validare = 20

* În stânga, vedem o aproximare bună printr-o linie dreaptă. Deoarece numărul de parametri este adecvat, modelul surprinde corect distribuția punctelor.
* În dreapta, modelul este prea puternic. Pentru că avem doar 5 puncte, iar modelul are 7 parametri, acesta se poate ajusta astfel încât să treacă prin toate punctele, făcând eroarea de antrenare să fie 0. Totuși, acest lucru împiedică modelul să înțeleagă corect tiparul din spatele datelor, astfel eroarea de validare este foarte mare.

Este foarte important să găsim un echilibru corect între complexitatea modelului (numărul de parametri) și numărul de exemple de antrenament.

## De ce apare overfitting-ul

  * Date insuficiente pentru antrenament
  * Model prea complex
  * Prea mult zgomot în datele de intrare

## Cum detectăm overfitting-ul

După cum se vede în graficul de mai sus, overfitting-ul poate fi detectat printr-o eroare foarte mică la antrenament și o eroare mare la validare. De obicei, în timpul antrenamentului, atât eroarea de antrenament, cât și cea de validare scad, iar apoi, la un moment dat, eroarea de validare se oprește din scăzut și începe să crească. Acesta este un semn de overfitting și indică faptul că probabil ar trebui să oprim antrenamentul în acel punct (sau cel puțin să salvăm o copie a modelului).

overfitting

## Cum prevenim overfitting-ul

Dacă observi că apare overfitting, poți face una dintre următoarele:

 * Crește cantitatea de date pentru antrenament
 * Scade complexitatea modelului
 * Folosește o tehnică de regularizare, cum ar fi Dropout, pe care o vom analiza mai târziu.

## Overfitting și compromisului Bias-Varianță

Overfitting-ul este, de fapt, un caz particular al unei probleme mai generale din statistică numită compromis Bias-Varianță. Dacă analizăm sursele posibile de eroare în modelul nostru, putem identifica două tipuri de erori:

* **Erorile de bias** sunt cauzate de incapacitatea algoritmului de a surprinde corect relația dintre datele de antrenament. Acestea pot apărea dacă modelul nu este suficient de puternic (**underfitting**).
* **Erorile de varianță**, care apar atunci când modelul încearcă să aproximeze zgomotul din datele de intrare în loc de relația semnificativă (**overfitting**).

În timpul antrenamentului, eroarea de bias scade (pe măsură ce modelul învață să aproximeze datele), iar eroarea de varianță crește. Este important să oprim antrenamentul – fie manual (când detectăm overfitting) sau automat (prin introducerea regularizării) – pentru a preveni overfitting-ul.

## Concluzie

În această lecție, ai învățat despre diferențele dintre diversele API-uri pentru cele două framework-uri AI cele mai populare, TensorFlow și PyTorch. În plus, ai aflat despre un subiect foarte important, overfitting-ul.

## 🚀 Provocare

În notebook-urile însoțitoare vei găsi „sarcini” la final; parcurge notebook-urile și rezolvă sarcinile.

## Recapitulare & Studiu individual

Caută informații despre următoarele subiecte:

- TensorFlow
- PyTorch
- Overfitting

Răspunde-ți la următoarele întrebări:

- Care este diferența dintre TensorFlow și PyTorch?
- Care este diferența dintre overfitting și underfitting?

## Tema

În acest laborator, ți se cere să rezolvi două probleme de clasificare folosind rețele complet conectate cu un singur strat și cu mai multe straturi, folosind PyTorch sau TensorFlow.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.