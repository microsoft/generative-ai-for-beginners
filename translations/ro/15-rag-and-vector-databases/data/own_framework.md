<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:26:45+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "ro"
}
-->
# Introducere în Rețele Neuronale. Perceptron Multi-Stratificat

În secțiunea anterioară, ai învățat despre cel mai simplu model de rețea neuronală - perceptronul cu un singur strat, un model liniar de clasificare în două clase.

În această secțiune vom extinde acest model într-un cadru mai flexibil, care ne va permite să:

* efectuăm **clasificare multi-clasă** pe lângă cea în două clase
* rezolvăm **probleme de regresie** pe lângă clasificare
* separăm clase care nu sunt separabile liniar

Vom dezvolta, de asemenea, propriul nostru cadru modular în Python, care ne va permite să construim diferite arhitecturi de rețele neuronale.

## Formalizarea Învățării Automate

Să începem prin formalizarea problemei de Învățare Automată. Presupunem că avem un set de date de antrenament **X** cu etichete **Y**, și trebuie să construim un model *f* care să facă predicții cât mai precise. Calitatea predicțiilor este măsurată prin **Funcția de Pierdere** ℒ. Următoarele funcții de pierdere sunt adesea utilizate:

* Pentru problema de regresie, când trebuie să prezicem un număr, putem folosi **eroarea absolută** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| sau **eroarea pătratică** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pentru clasificare, folosim **pierdere 0-1** (care este esențial același lucru cu **acuratețea** modelului) sau **pierdere logistică**.

Pentru perceptronul cu un singur nivel, funcția *f* a fost definită ca o funcție liniară *f(x)=wx+b* (aici *w* este matricea de greutăți, *x* este vectorul de caracteristici de intrare, și *b* este vectorul de bias). Pentru diferite arhitecturi de rețele neuronale, această funcție poate lua o formă mai complexă.

> În cazul clasificării, este adesea de dorit să obținem probabilitățile claselor corespunzătoare ca rezultat al rețelei. Pentru a converti numerele arbitrare în probabilități (de exemplu, pentru a normaliza rezultatul), folosim adesea funcția **softmax** σ, iar funcția *f* devine *f(x)=σ(wx+b)*

În definiția *f* de mai sus, *w* și *b* sunt numite **parametri** θ=⟨*w,b*⟩. Dat fiind setul de date ⟨**X**,**Y**⟩, putem calcula o eroare generală pe întregul set de date ca o funcție a parametrilor θ.

> ✅ **Scopul antrenării rețelei neuronale este de a minimiza eroarea prin varierea parametrilor θ**

## Optimizarea prin Gradient Descent

Există o metodă bine cunoscută de optimizare a funcțiilor numită **gradient descent**. Ideea este că putem calcula o derivată (în cazul multidimensional numită **gradient**) a funcției de pierdere în raport cu parametrii și să variem parametrii astfel încât eroarea să scadă. Acest lucru poate fi formalizat astfel:

* Inițializează parametrii cu unele valori aleatoare w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetă următorul pas de mai multe ori:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

În timpul antrenării, pașii de optimizare ar trebui să fie calculați luând în considerare întregul set de date (amintiți-vă că pierderea este calculată ca o sumă pe toate exemplele de antrenament). Totuși, în viața reală luăm porțiuni mici ale setului de date numite **minibatches** și calculăm gradientele pe baza unui subset de date. Deoarece subsetul este luat aleatoriu de fiecare dată, această metodă este numită **stochastic gradient descent** (SGD).

## Perceptron Multi-Stratificat și Backpropagation

Rețeaua cu un singur strat, așa cum am văzut mai sus, este capabilă să clasifice clasele separabile liniar. Pentru a construi un model mai bogat, putem combina mai multe straturi ale rețelei. Matematic, ar însemna că funcția *f* ar avea o formă mai complexă și va fi calculată în mai mulți pași:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aici, α este o **funcție de activare non-liniară**, σ este o funcție softmax, iar parametrii θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmul de gradient descent ar rămâne același, dar ar fi mai dificil de calculat gradientele. Dată regula de diferențiere în lanț, putem calcula derivatele astfel:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Regula de diferențiere în lanț este folosită pentru a calcula derivatele funcției de pierdere în raport cu parametrii.

Observați că partea cea mai din stânga a tuturor acestor expresii este aceeași și, astfel, putem calcula eficient derivatele începând de la funcția de pierdere și mergând "înapoi" prin graful computațional. Astfel, metoda de antrenare a unui perceptron multi-stratificat este numită **backpropagation**, sau 'backprop'.

> TODO: citare imagine

> ✅ Vom aborda backprop în mult mai multe detalii în exemplul nostru din notebook.

## Concluzie

În această lecție, am construit propria noastră bibliotecă de rețele neuronale și am folosit-o pentru o sarcină simplă de clasificare bidimensională.

## 🚀 Provocare

În notebook-ul însoțitor, vei implementa propriul tău cadru pentru construirea și antrenarea perceptronilor multi-stratificați. Vei putea vedea în detaliu cum funcționează rețelele neuronale moderne.

Continuă cu notebook-ul OwnFramework și parcurge-l.

## Revizuire & Studiu Individual

Backpropagation este un algoritm comun utilizat în AI și ML, merită studiat în detaliu.

## Sarcină

În acest laborator, ți se cere să folosești cadrul pe care l-ai construit în această lecție pentru a rezolva clasificarea cifrelor scrise de mână MNIST.

* Instrucțiuni
* Notebook

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.