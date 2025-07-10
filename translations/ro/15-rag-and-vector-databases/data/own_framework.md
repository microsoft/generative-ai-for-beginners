<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:51:07+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "ro"
}
-->
# Introducere în Rețele Neuronale. Perceptron Multi-Stratificat

În secțiunea anterioară, ai învățat despre cel mai simplu model de rețea neuronală - perceptronul cu un singur strat, un model liniar de clasificare binară.

În această secțiune vom extinde acest model într-un cadru mai flexibil, care ne va permite să:

* realizăm **clasificare multi-clasă** pe lângă clasificarea binară
* rezolvăm **probleme de regresie** pe lângă clasificare
* separăm clase care nu sunt liniar separabile

De asemenea, vom dezvolta propriul nostru cadru modular în Python care ne va permite să construim diferite arhitecturi de rețele neuronale.

## Formalizarea Învățării Automate

Să începem prin a formaliza problema Învățării Automate. Presupunem că avem un set de date de antrenament **X** cu etichete **Y**, și trebuie să construim un model *f* care să facă predicții cât mai precise. Calitatea predicțiilor este măsurată prin **funcția de pierdere** ℒ. Următoarele funcții de pierdere sunt frecvent utilizate:

* Pentru problema de regresie, când trebuie să prezicem un număr, putem folosi **eroarea absolută** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, sau **eroarea pătratică** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pentru clasificare, folosim **pierdere 0-1** (care este practic aceeași cu **acuratețea** modelului), sau **pierdere logistică**.

Pentru perceptronul cu un singur strat, funcția *f* a fost definită ca o funcție liniară *f(x)=wx+b* (aici *w* este matricea de greutăți, *x* este vectorul caracteristicilor de intrare, iar *b* este vectorul de bias). Pentru diferite arhitecturi de rețele neuronale, această funcție poate lua o formă mai complexă.

> În cazul clasificării, este adesea de dorit să obținem probabilitățile claselor corespunzătoare ca ieșire a rețelei. Pentru a converti numere arbitrare în probabilități (de exemplu, pentru a normaliza ieșirea), folosim frecvent funcția **softmax** σ, iar funcția *f* devine *f(x)=σ(wx+b)*

În definiția lui *f* de mai sus, *w* și *b* sunt numiți **parametri** θ=⟨*w,b*⟩. Având setul de date ⟨**X**,**Y**⟩, putem calcula eroarea totală pe întregul set de date ca o funcție a parametrilor θ.

> ✅ **Scopul antrenării rețelei neuronale este de a minimiza eroarea variind parametrii θ**

## Optimizarea prin Gradient Descendent

Există o metodă bine cunoscută de optimizare a funcțiilor numită **gradient descendent**. Ideea este că putem calcula derivata (în cazul multidimensional numită **gradient**) a funcției de pierdere în raport cu parametrii, și să modificăm parametrii astfel încât eroarea să scadă. Acest lucru poate fi formalizat astfel:

* Inițializăm parametrii cu niște valori aleatorii w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetăm următorul pas de multe ori:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

În timpul antrenării, pașii de optimizare trebuie calculați luând în considerare întregul set de date (amintește-ți că pierderea este calculată ca sumă peste toate exemplele de antrenament). Totuși, în practică luăm porțiuni mici din setul de date numite **minibatch-uri**, și calculăm gradientul pe baza unui subset de date. Deoarece subsetul este ales aleator de fiecare dată, această metodă se numește **gradient descendent stocastic** (SGD).

## Perceptron Multi-Stratificat și Backpropagation

Rețeaua cu un singur strat, așa cum am văzut mai sus, este capabilă să clasifice clase liniar separabile. Pentru a construi un model mai complex, putem combina mai multe straturi ale rețelei. Matematic, asta înseamnă că funcția *f* va avea o formă mai complexă și va fi calculată în mai mulți pași:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aici, α este o **funcție de activare non-liniară**, σ este funcția softmax, iar parametrii θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmul gradient descendent rămâne același, dar calculul gradientului devine mai dificil. Aplicând regula de derivare în lanț, putem calcula derivatele astfel:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Regula de derivare în lanț este folosită pentru a calcula derivatele funcției de pierdere în raport cu parametrii.

Observă că partea din stânga a tuturor acestor expresii este aceeași, astfel încât putem calcula eficient derivatele începând de la funcția de pierdere și mergând „înapoi” prin graful computațional. Astfel, metoda de antrenare a perceptronului multi-stratificat se numește **backpropagation**, sau „backprop”.

> TODO: citare imagine

> ✅ Vom detalia backprop în exemplul din notebook-ul nostru.

## Concluzie

În această lecție, am construit propria noastră bibliotecă de rețele neuronale și am folosit-o pentru o sarcină simplă de clasificare bidimensională.

## 🚀 Provocare

În notebook-ul însoțitor, vei implementa propriul cadru pentru construirea și antrenarea perceptronilor multi-stratificați. Vei putea vedea în detaliu cum funcționează rețelele neuronale moderne.

Continuă cu notebook-ul OwnFramework și parcurge-l.

## Recapitulare & Studiu Individual

Backpropagation este un algoritm comun folosit în AI și ML, merită studiat în detaliu.

## Tema

În acest laborator, ți se cere să folosești cadrul pe care l-ai construit în această lecție pentru a rezolva clasificarea cifrelor scrise de mână din setul MNIST.

* Instrucțiuni
* Notebook

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.