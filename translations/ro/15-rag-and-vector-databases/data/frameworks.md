<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:07:18+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "ro"
}
-->
# Framework-uri pentru rețele neuronale

Așa cum am învățat deja, pentru a putea antrena rețele neuronale eficient trebuie să facem două lucruri:

* Să operăm pe tensori, de exemplu să înmulțim, să adunăm și să calculăm funcții precum sigmoid sau softmax
* Să calculăm gradientele tuturor expresiilor, pentru a efectua optimizarea prin gradient descent

Deși biblioteca `numpy` poate face prima parte, avem nevoie de un mecanism pentru a calcula gradientele. În cadrul nostru pe care l-am dezvoltat în secțiunea anterioară, a trebuit să programăm manual toate funcțiile derivate în metoda `backward`, care face backpropagation. Ideal, un cadru ar trebui să ne ofere oportunitatea de a calcula gradientele *oricărei expresii* pe care o putem defini.

Un alt aspect important este să putem efectua calcule pe GPU sau pe alte unități de calcul specializate, precum TPU. Antrenamentul rețelelor neuronale profunde necesită *foarte multe* calcule, iar posibilitatea de a paraleliza aceste calcule pe GPU-uri este foarte importantă.

> ✅ Termenul 'paralelizare' înseamnă distribuirea calculelor pe mai multe dispozitive.

În prezent, cele mai populare două cadre pentru rețele neuronale sunt: TensorFlow și PyTorch. Ambele oferă o API de nivel scăzut pentru a opera cu tensori atât pe CPU, cât și pe GPU. Pe lângă API-ul de nivel scăzut, există și un API de nivel înalt, numit Keras și, respectiv, PyTorch Lightning.

API de nivel scăzut | TensorFlow | PyTorch
--------------------|-------------------------------------|--------------------------------
API de nivel înalt  | Keras | PyTorch Lightning

**API-urile de nivel scăzut** din ambele cadre îți permit să construiești așa-numitele **grafuri computaționale**. Acest graf definește cum să se calculeze ieșirea (de obicei funcția de pierdere) cu parametrii de intrare dați și poate fi transferat pentru calcul pe GPU, dacă este disponibil. Există funcții pentru a diferenția acest graf computațional și a calcula gradientele, care pot fi apoi folosite pentru optimizarea parametrilor modelului.

**API-urile de nivel înalt** consideră în mare parte rețelele neuronale ca o **secvență de straturi** și fac construirea majorității rețelelor neuronale mult mai ușoară. Antrenarea modelului necesită de obicei pregătirea datelor și apoi apelarea unei funcții `fit` pentru a face treaba.

API-ul de nivel înalt îți permite să construiești rețele neuronale tipice foarte rapid, fără să te îngrijorezi de multe detalii. În același timp, API-urile de nivel scăzut oferă mult mai mult control asupra procesului de antrenament și astfel sunt folosite mult în cercetare, când te ocupi de noi arhitecturi de rețele neuronale.

Este, de asemenea, important să înțelegi că poți folosi ambele API-uri împreună, de exemplu, poți dezvolta propria arhitectură de strat de rețea folosind API-ul de nivel scăzut și apoi să o folosești în rețeaua mai mare construită și antrenată cu API-ul de nivel înalt. Sau poți defini o rețea folosind API-ul de nivel înalt ca o secvență de straturi și apoi să folosești propriul tău ciclu de antrenament de nivel scăzut pentru a efectua optimizarea. Ambele API-uri folosesc aceleași concepte de bază și sunt proiectate să funcționeze bine împreună.

## Învățare

În acest curs, oferim majoritatea conținutului atât pentru PyTorch, cât și pentru TensorFlow. Poți alege cadrul preferat și să parcurgi doar notițele corespunzătoare. Dacă nu ești sigur ce cadru să alegi, citește câteva discuții pe internet despre **PyTorch vs. TensorFlow**. Poți, de asemenea, să arunci o privire asupra ambelor cadre pentru a obține o înțelegere mai bună.

Acolo unde este posibil, vom folosi API-urile de nivel înalt pentru simplitate. Totuși, credem că este important să înțelegi cum funcționează rețelele neuronale de la bază, așa că la început începem prin a lucra cu API-ul de nivel scăzut și tensori. Totuși, dacă vrei să începi rapid și nu vrei să petreci mult timp învățând aceste detalii, poți să le sari și să mergi direct la notițele cu API-ul de nivel înalt.

## ✍️ Exerciții: Framework-uri

Continuă învățarea în următoarele notițe:

API de nivel scăzut | Notiță TensorFlow+Keras | PyTorch
--------------------|-------------------------------------|--------------------------------
API de nivel înalt  | Keras | *PyTorch Lightning*

După ce ai stăpânit cadrele, să recapitulăm noțiunea de overfitting.

# Overfitting

Overfitting este un concept extrem de important în învățarea automată și este foarte important să-l înțelegi corect!

Consideră următoarea problemă de aproximare a 5 puncte (reprezentate de `x` pe graficele de mai jos):

!liniear | overfit
-------------------------|--------------------------
**Model liniar, 2 parametri** | **Model neliniar, 7 parametri**
Eroare antrenament = 5.3 | Eroare antrenament = 0
Eroare validare = 5.1 | Eroare validare = 20

* În stânga, vedem o bună aproximare printr-o linie dreaptă. Deoarece numărul de parametri este adecvat, modelul înțelege corect distribuția punctelor.
* În dreapta, modelul este prea puternic. Deoarece avem doar 5 puncte și modelul are 7 parametri, se poate ajusta astfel încât să treacă prin toate punctele, făcând ca eroarea de antrenament să fie 0. Totuși, acest lucru împiedică modelul să înțeleagă corect modelul datelor, astfel că eroarea de validare este foarte mare.

Este foarte important să găsești un echilibru corect între bogăția modelului (numărul de parametri) și numărul de eșantioane de antrenament.

## De ce apare overfitting-ul

  * Nu sunt suficiente date de antrenament
  * Model prea puternic
  * Prea mult zgomot în datele de intrare

## Cum să detectezi overfitting-ul

După cum poți vedea din graficul de mai sus, overfitting-ul poate fi detectat printr-o eroare de antrenament foarte mică și o eroare de validare mare. În mod normal, în timpul antrenamentului vom vedea atât erorile de antrenament, cât și cele de validare începând să scadă, și apoi la un moment dat eroarea de validare s-ar putea opri din scădere și să înceapă să crească. Acesta va fi un semn de overfitting și un indicator că probabil ar trebui să oprim antrenamentul în acest punct (sau cel puțin să facem o captură de moment a modelului).

overfitting

## Cum să previi overfitting-ul

Dacă vezi că apare overfitting-ul, poți face unul dintre următoarele lucruri:

 * Crește cantitatea de date de antrenament
 * Redu complexitatea modelului
 * Folosește o tehnică de regularizare, cum ar fi Dropout, pe care o vom considera mai târziu.

## Overfitting și compromisul Bias-Varianță

Overfitting-ul este de fapt un caz al unei probleme mai generale în statistică numită Compromisul Bias-Varianță. Dacă luăm în considerare sursele posibile de eroare în modelul nostru, putem vedea două tipuri de erori:

* **Erorile de bias** sunt cauzate de faptul că algoritmul nostru nu poate captura corect relația dintre datele de antrenament. Poate rezulta din faptul că modelul nostru nu este suficient de puternic (**underfitting**).
* **Erorile de varianță**, care sunt cauzate de modelul care aproximează zgomotul din datele de intrare în loc de relația semnificativă (**overfitting**).

În timpul antrenamentului, eroarea de bias scade (pe măsură ce modelul nostru învață să aproximeze datele), iar eroarea de varianță crește. Este important să oprim antrenamentul - fie manual (când detectăm overfitting-ul) fie automat (introducând regularizare) - pentru a preveni overfitting-ul.

## Concluzie

În această lecție, ai învățat despre diferențele dintre diversele API-uri pentru cele mai populare două cadre AI, TensorFlow și PyTorch. În plus, ai învățat despre un subiect foarte important, overfitting-ul.

## 🚀 Provocare

În notițele însoțitoare, vei găsi 'sarcini' la final; parcurge notițele și completează sarcinile.

## Recapitulare și auto-studiu

Fă câteva cercetări pe următoarele subiecte:

- TensorFlow
- PyTorch
- Overfitting

Întreabă-te următoarele întrebări:

- Care este diferența dintre TensorFlow și PyTorch?
- Care este diferența dintre overfitting și underfitting?

## Temă

În acest laborator, ți se cere să rezolvi două probleme de clasificare folosind rețele complet conectate cu un singur strat și cu mai multe straturi folosind PyTorch sau TensorFlow.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem responsabili pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.