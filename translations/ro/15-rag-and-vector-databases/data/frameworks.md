<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:10:33+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "ro"
}
-->
# Frameworkuri de rețele neuronale

Așa cum am învățat deja, pentru a putea antrena rețele neuronale eficient, trebuie să facem două lucruri:

* Să operăm pe tensori, de exemplu să înmulțim, adunăm și să calculăm unele funcții precum sigmoid sau softmax
* Să calculăm gradientele tuturor expresiilor, pentru a realiza optimizarea prin coborârea gradientului

În timp ce biblioteca `numpy` poate face prima parte, avem nevoie de un mecanism pentru a calcula gradientele. În cadrul pe care l-am dezvoltat în secțiunea anterioară, a trebuit să programăm manual toate funcțiile derivate în metoda `backward`, care realizează backpropagation. Ideal, un cadru ar trebui să ne ofere oportunitatea de a calcula gradientele *oricărei expresii* pe care o putem defini.

Un alt aspect important este să putem efectua calcule pe GPU sau orice alte unități de calcul specializate, cum ar fi TPU. Antrenarea rețelelor neuronale profunde necesită *multe* calcule, iar abilitatea de a paraleliza aceste calcule pe GPU-uri este foarte importantă.

> ✅ Termenul 'paralelizare' înseamnă distribuirea calculelor pe mai multe dispozitive.

În prezent, cele mai populare două cadre neuronale sunt: TensorFlow și PyTorch. Ambele oferă o API de nivel scăzut pentru a opera cu tensori atât pe CPU, cât și pe GPU. Pe lângă API-ul de nivel scăzut, există și API-uri de nivel înalt, numite Keras și, respectiv, PyTorch Lightning.

API de nivel scăzut | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API de nivel înalt| Keras| Pytorch

**API-urile de nivel scăzut** din ambele cadre vă permit să construiți așa-numitele **grafice computaționale**. Acest grafic definește cum să se calculeze ieșirea (de obicei funcția de pierdere) cu parametrii de intrare dați și poate fi trimis pentru calcul pe GPU, dacă este disponibil. Există funcții pentru a diferenția acest grafic computațional și a calcula gradientele, care pot fi apoi utilizate pentru optimizarea parametrilor modelului.

**API-urile de nivel înalt** consideră în mare parte rețelele neuronale ca o **succesiune de straturi**, și fac construcția majorității rețelelor neuronale mult mai ușoară. Antrenarea modelului necesită de obicei pregătirea datelor și apoi apelarea unei funcții `fit` pentru a face treaba.

API-ul de nivel înalt vă permite să construiți rețele neuronale tipice foarte rapid, fără să vă faceți griji cu privire la multe detalii. În același timp, API-ul de nivel scăzut oferă mult mai mult control asupra procesului de antrenare și, astfel, este utilizat mult în cercetare, atunci când lucrați cu noi arhitecturi de rețele neuronale.

Este important să înțelegeți că puteți folosi ambele API-uri împreună, de exemplu, puteți dezvolta propria arhitectură de strat de rețea folosind API-ul de nivel scăzut și apoi să o folosiți în cadrul rețelei mai mari construită și antrenată cu API-ul de nivel înalt. Sau puteți defini o rețea folosind API-ul de nivel înalt ca o succesiune de straturi și apoi să folosiți propriul ciclu de antrenare de nivel scăzut pentru a efectua optimizarea. Ambele API-uri folosesc aceleași concepte de bază și sunt concepute să funcționeze bine împreună.

## Învățare

În acest curs, oferim majoritatea conținutului atât pentru PyTorch, cât și pentru TensorFlow. Puteți alege cadrul preferat și să parcurgeți doar notebook-urile corespunzătoare. Dacă nu sunteți sigur ce cadru să alegeți, citiți câteva discuții pe internet despre **PyTorch vs. TensorFlow**. Puteți, de asemenea, să aruncați o privire asupra ambelor cadre pentru a obține o înțelegere mai bună.

Unde este posibil, vom folosi API-urile de nivel înalt pentru simplitate. Totuși, considerăm că este important să înțelegem cum funcționează rețelele neuronale de la bază, astfel că la început vom lucra cu API-ul de nivel scăzut și tensori. Totuși, dacă doriți să începeți rapid și nu doriți să petreceți mult timp învățând aceste detalii, puteți sări peste acestea și să mergeți direct la notebook-urile API-ului de nivel înalt.

## ✍️ Exerciții: Frameworkuri

Continuați învățarea în următoarele notebook-uri:

API de nivel scăzut | Notebook TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API de nivel înalt| Keras | *PyTorch Lightning*

După ce ați stăpânit frameworkurile, să recapitulăm noțiunea de overfitting.

# Overfitting

Overfitting este un concept extrem de important în învățarea automată și este foarte important să îl înțelegeți corect!

Luați în considerare următoarea problemă de aproximare a 5 puncte (reprezentate de `x` pe graficele de mai jos):

!linear | overfit
-------------------------|--------------------------
**Model liniar, 2 parametri** | **Model neliniar, 7 parametri**
Eroare de antrenare = 5.3 | Eroare de antrenare = 0
Eroare de validare = 5.1 | Eroare de validare = 20

* În stânga, vedem o bună aproximare cu o linie dreaptă. Deoarece numărul de parametri este adecvat, modelul înțelege corect distribuția punctelor.
* În dreapta, modelul este prea puternic. Deoarece avem doar 5 puncte și modelul are 7 parametri, acesta se poate ajusta în așa fel încât să treacă prin toate punctele, făcând eroarea de antrenare să fie 0. Totuși, acest lucru împiedică modelul să înțeleagă corect modelul din spatele datelor, astfel eroarea de validare este foarte mare.

Este foarte important să găsim un echilibru corect între bogăția modelului (numărul de parametri) și numărul de exemple de antrenare.

## De ce apare overfitting

  * Nu sunt suficiente date de antrenare
  * Model prea puternic
  * Prea mult zgomot în datele de intrare

## Cum să detectăm overfitting

Așa cum puteți vedea din graficul de mai sus, overfitting-ul poate fi detectat printr-o eroare de antrenare foarte mică și o eroare de validare mare. În mod normal, în timpul antrenării vom vedea atât erorile de antrenare, cât și cele de validare începând să scadă, și apoi la un moment dat eroarea de validare poate înceta să scadă și să înceapă să crească. Acesta va fi un semn de overfitting și un indicator că ar trebui probabil să oprim antrenarea în acest moment (sau cel puțin să facem un snapshot al modelului).

overfitting

## Cum să prevenim overfitting-ul

Dacă observați că apare overfitting, puteți face una dintre următoarele:

 * Creșteți cantitatea de date de antrenare
 * Reduceți complexitatea modelului
 * Utilizați o tehnică de regularizare, cum ar fi Dropout, pe care o vom analiza mai târziu.

## Overfitting și compromis Bias-Varianță

Overfitting-ul este de fapt un caz al unei probleme mai generale în statistică numită compromis Bias-Varianță. Dacă luăm în considerare sursele posibile de eroare în modelul nostru, putem vedea două tipuri de erori:

* **Erorile de bias** sunt cauzate de faptul că algoritmul nostru nu poate captura corect relația dintre datele de antrenare. Acest lucru poate rezulta din faptul că modelul nostru nu este suficient de puternic (**underfitting**).
* **Erorile de varianță**, care sunt cauzate de modelul care aproximează zgomotul în datele de intrare în loc de relația semnificativă (**overfitting**).

În timpul antrenării, eroarea de bias scade (pe măsură ce modelul nostru învață să aproximeze datele), iar eroarea de varianță crește. Este important să oprim antrenarea - fie manual (când detectăm overfitting) fie automat (prin introducerea regularizării) - pentru a preveni overfitting-ul.

## Concluzie

În această lecție, ați învățat despre diferențele dintre diversele API-uri pentru cele două cadre AI cele mai populare, TensorFlow și PyTorch. În plus, ați învățat despre un subiect foarte important, overfitting-ul.

## 🚀 Provocare

În notebook-urile însoțitoare, veți găsi 'sarcini' la final; parcurgeți notebook-urile și completați sarcinile.

## Revizuire și Studii Individuale

Faceți cercetări pe următoarele subiecte:

- TensorFlow
- PyTorch
- Overfitting

Întrebați-vă următoarele întrebări:

- Care este diferența între TensorFlow și PyTorch?
- Care este diferența între overfitting și underfitting?

## Temă

În acest laborator, vi se cere să rezolvați două probleme de clasificare folosind rețele complet conectate cu un singur strat și cu mai multe straturi, utilizând PyTorch sau TensorFlow.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană profesională. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care ar putea rezulta din utilizarea acestei traduceri.