<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:30:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "ro"
}
-->
# Introducere în Rețele Neurale. Perceptron Multi-Stratificat

În secțiunea anterioară, ai învățat despre cel mai simplu model de rețea neurală - perceptronul cu un singur strat, un model liniar de clasificare cu două clase.

În această secțiune, vom extinde acest model într-un cadru mai flexibil, care ne va permite să:

* realizăm **clasificare multi-clasă** pe lângă cea cu două clase
* rezolvăm **probleme de regresie** pe lângă clasificare
* separăm clase care nu sunt liniar separabile

De asemenea, vom dezvolta propriul nostru cadru modular în Python care ne va permite să construim diferite arhitecturi de rețele neurale.

## Formalizarea Învățării Automate

Să începem prin a formaliza problema Învățării Automate. Să presupunem că avem un set de date de antrenament **X** cu etichete **Y**, și trebuie să construim un model *f* care să facă predicții cât mai precise. Calitatea predicțiilor este măsurată prin **funcția de pierdere** ℒ. Următoarele funcții de pierdere sunt adesea utilizate:

* Pentru problema de regresie, când trebuie să prezicem un număr, putem folosi **eroarea absolută** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, sau **eroarea pătratică** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pentru clasificare, folosim **pierdere 0-1** (care este în esență același lucru cu **acuratețea** modelului), sau **pierdere logistică**.

Pentru perceptronul cu un singur nivel, funcția *f* a fost definită ca o funcție liniară *f(x)=wx+b* (aici *w* este matricea de greutăți, *x* este vectorul de caracteristici de intrare, și *b* este vectorul de bias). Pentru diferite arhitecturi de rețele neurale, această funcție poate lua o formă mai complexă.

> În cazul clasificării, este adesea de dorit să obținem probabilitățile claselor corespunzătoare ca ieșire a rețelei. Pentru a converti numere arbitrare în probabilități (de exemplu, pentru a normaliza ieșirea), folosim adesea funcția **softmax** σ, iar funcția *f* devine *f(x)=σ(wx+b)*

În definiția de mai sus a lui *f*, *w* și *b* sunt numite **parametri** θ=⟨*w,b*⟩. Dat fiind setul de date ⟨**X**,**Y**⟩, putem calcula o eroare totală pe întregul set de date ca o funcție a parametrilor θ.

> ✅ **Scopul antrenării rețelei neurale este de a minimiza eroarea prin varierea parametrilor θ**

## Optimizarea prin Gradient Descent

Există o metodă bine cunoscută de optimizare a funcțiilor numită **gradient descent**. Ideea este că putem calcula o derivată (în cazul multidimensional numită **gradient**) a funcției de pierdere în raport cu parametrii și să variem parametrii astfel încât eroarea să scadă. Aceasta poate fi formalizată astfel:

* Inițializează parametrii cu niște valori aleatoare w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetă următorul pas de mai multe ori:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

În timpul antrenării, pașii de optimizare ar trebui calculați având în vedere întregul set de date (amintiți-vă că pierderea este calculată ca o sumă prin toate exemplele de antrenament). Totuși, în realitate luăm porțiuni mici ale setului de date numite **miniloturi**, și calculăm gradientele pe baza unui subset de date. Deoarece subsetul este luat aleatoriu de fiecare dată, o astfel de metodă se numește **stochastic gradient descent** (SGD).

## Perceptron Multi-Stratificat și Backpropagation

Rețeaua cu un singur strat, așa cum am văzut mai sus, este capabilă să clasifice clasele liniar separabile. Pentru a construi un model mai bogat, putem combina mai multe straturi ale rețelei. Matematic, aceasta ar însemna că funcția *f* ar avea o formă mai complexă și va fi calculată în mai mulți pași:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aici, α este o **funcție de activare non-liniară**, σ este o funcție softmax, iar parametrii θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmul de gradient descent ar rămâne același, dar ar fi mai dificil să calculăm gradientele. Datorită regulii de diferențiere în lanț, putem calcula derivatele astfel:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Regula de diferențiere în lanț este folosită pentru a calcula derivatele funcției de pierdere în raport cu parametrii.

Observați că partea din stânga a tuturor acestor expresii este aceeași și, astfel, putem calcula eficient derivatele începând de la funcția de pierdere și mergând "înapoi" prin graful computațional. Astfel, metoda de antrenare a unui perceptron multi-stratificat se numește **backpropagation**, sau 'backprop'.

> TODO: citare imagine

> ✅ Vom acoperi backprop în mult mai multe detalii în exemplul nostru din caietul de notițe.

## Concluzie

În această lecție, ne-am construit propria bibliotecă de rețele neurale și am folosit-o pentru o sarcină simplă de clasificare bidimensională.

## 🚀 Provocare

În caietul de notițe însoțitor, vei implementa propriul tău cadru pentru construirea și antrenarea perceptronilor multi-stratificați. Vei putea vedea în detaliu cum operează rețelele neurale moderne.

Accesează caietul de notițe OwnFramework și parcurge-l.

## Recapitulare & Studiu Individual

Backpropagation este un algoritm comun folosit în AI și ML, merită studiat în detaliu.

## Temă

În acest laborator, ți se cere să folosești cadrul pe care l-ai construit în această lecție pentru a rezolva clasificarea cifrelor scrise de mână MNIST.

* Instrucțiuni
* Caiet de notițe

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.