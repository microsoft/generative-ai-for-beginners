<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:43:33+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ro"
}
-->
# Introducere în Rețele Neurale: Perceptron

Una dintre primele încercări de a implementa ceva asemănător cu o rețea neurală modernă a fost realizată de Frank Rosenblatt de la Cornell Aeronautical Laboratory în 1957. A fost o implementare hardware numită "Mark-1", proiectată pentru a recunoaște figuri geometrice primitive, precum triunghiuri, pătrate și cercuri.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imagini de pe Wikipedia

O imagine de intrare era reprezentată de o matrice de fotocelule de 20x20, astfel încât rețeaua neurală avea 400 de intrări și o ieșire binară. O rețea simplă conținea un neuron, numit și **unitate logică de prag**. Greutățile rețelei neurale acționau ca niște potențiometre care necesitau ajustare manuală în timpul fazei de antrenament.

> ✅ Un potențiometru este un dispozitiv care permite utilizatorului să ajusteze rezistența unui circuit.

> The New York Times a scris despre perceptron la acea vreme: *embrionul unui computer electronic pe care [Marina] se așteaptă să fie capabil să meargă, să vorbească, să vadă, să scrie, să se reproducă și să fie conștient de existența sa.*

## Modelul Perceptron

Să presupunem că avem N caracteristici în modelul nostru, caz în care vectorul de intrare ar fi un vector de dimensiune N. Un perceptron este un model de **clasificare binară**, adică poate distinge între două clase de date de intrare. Vom presupune că pentru fiecare vector de intrare x, ieșirea perceptronului nostru va fi fie +1, fie -1, în funcție de clasă. Ieșirea va fi calculată folosind formula:

y(x) = f(w<sup>T</sup>x)

unde f este o funcție de activare treaptă

## Antrenarea Perceptronului

Pentru a antrena un perceptron, trebuie să găsim un vector de greutăți w care să clasifice corect majoritatea valorilor, adică să rezulte în cel mai mic **eroare**. Această eroare este definită de **criteriul perceptronului** în următorul mod:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

unde:

* suma se face pe acele puncte de date de antrenament i care duc la clasificare greșită
* x<sub>i</sub> este datele de intrare, iar t<sub>i</sub> este fie -1, fie +1 pentru exemple negative și pozitive, respectiv.

Acest criteriu este considerat ca o funcție a greutăților w și trebuie să-l minimizăm. Adesea, se folosește o metodă numită **descendentă a gradientului**, în care începem cu unele greutăți inițiale w<sup>(0)</sup>, și apoi la fiecare pas actualizăm greutățile conform formulei:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Aici η este așa-numita **rată de învățare**, iar ∇E(w) denotă **gradientul** lui E. După ce calculăm gradientul, ajungem la

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmul în Python arată astfel:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Concluzie

În această lecție, ați învățat despre un perceptron, care este un model de clasificare binară, și cum să-l antrenați folosind un vector de greutăți.

## 🚀 Provocare

Dacă doriți să încercați să construiți propriul perceptron, încercați acest laborator pe Microsoft Learn care folosește designerul Azure ML.

## Recenzie și Studiu Individual

Pentru a vedea cum putem folosi perceptronul pentru a rezolva o problemă de jucărie, precum și probleme din viața reală, și pentru a continua învățarea - mergeți la notebook-ul Perceptron.

Iată și un articol interesant despre perceptroni.

## Temă

În această lecție, am implementat un perceptron pentru o sarcină de clasificare binară și l-am folosit pentru a clasifica între două cifre scrise de mână. În acest laborator, vi se cere să rezolvați problema clasificării cifrelor în întregime, adică să determinați care cifră este cel mai probabil să corespundă unei imagini date.

* Instrucțiuni
* Notebook

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană profesională. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.