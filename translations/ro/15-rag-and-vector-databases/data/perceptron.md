<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:01:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ro"
}
-->
# Introducere în Rețele Neuronale: Perceptron

Una dintre primele încercări de a implementa ceva similar cu o rețea neuronală modernă a fost realizată de Frank Rosenblatt de la Cornell Aeronautical Laboratory în 1957. A fost o implementare hardware numită „Mark-1”, concepută să recunoască figuri geometrice primitive, cum ar fi triunghiuri, pătrate și cercuri.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imagini de pe Wikipedia

O imagine de intrare era reprezentată printr-un tablou de 20x20 celule foto, astfel încât rețeaua neuronală avea 400 de intrări și o ieșire binară. O rețea simplă conținea un singur neuron, numit și **unitate logică cu prag**. Greutățile rețelei neuronale funcționau ca potențiometre care necesitau ajustare manuală în timpul fazei de antrenament.

> ✅ Un potențiometru este un dispozitiv care permite utilizatorului să ajusteze rezistența unui circuit.

> The New York Times scria despre perceptron în acea perioadă: *embrionul unui calculator electronic care [Marina] se așteaptă să poată merge, vorbi, vedea, scrie, să se reproducă și să fie conștient de existența sa.*

## Modelul Perceptronului

Să presupunem că avem N caracteristici în modelul nostru, caz în care vectorul de intrare ar fi un vector de dimensiune N. Un perceptron este un model de **clasificare binară**, adică poate distinge între două clase de date de intrare. Vom presupune că pentru fiecare vector de intrare x, ieșirea perceptronului nostru va fi fie +1, fie -1, în funcție de clasă. Ieșirea va fi calculată folosind formula:

y(x) = f(w<sup>T</sup>x)

unde f este o funcție de activare treaptă

## Antrenarea Perceptronului

Pentru a antrena un perceptron trebuie să găsim un vector de greutăți w care să clasifice corect majoritatea valorilor, adică să conducă la cea mai mică **eroare**. Această eroare este definită prin **criteriul perceptronului** în felul următor:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

unde:

* suma se face peste acele puncte de date de antrenament i care duc la clasificare greșită
* x<sub>i</sub> este datele de intrare, iar t<sub>i</sub> este fie -1, fie +1 pentru exemple negative și pozitive, respectiv.

Acest criteriu este considerat o funcție a greutăților w, iar noi trebuie să îl minimizăm. Adesea, se folosește o metodă numită **gradient descent** (coborâre pe gradient), în care începem cu niște greutăți inițiale w<sup>(0)</sup>, iar apoi la fiecare pas actualizăm greutățile conform formulei:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Aici η este așa-numita **rată de învățare**, iar ∇E(w) reprezintă **gradientul** lui E. După ce calculăm gradientul, ajungem la:

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

În această lecție, ai învățat despre perceptron, un model de clasificare binară, și cum să îl antrenezi folosind un vector de greutăți.

## 🚀 Provocare

Dacă vrei să încerci să construiești propriul perceptron, încearcă acest laborator pe Microsoft Learn care folosește Azure ML designer


## Recapitulare & Studiu Individual

Pentru a vedea cum putem folosi perceptronul pentru a rezolva o problemă simplă, dar și probleme din viața reală, și pentru a continua să înveți - accesează notebook-ul Perceptron.

Iată și un articol interesant despre perceptroni.

## Tema

În această lecție, am implementat un perceptron pentru o sarcină de clasificare binară și l-am folosit pentru a clasifica între două cifre scrise de mână. În acest laborator, ți se cere să rezolvi problema clasificării cifrelor în întregime, adică să determini care cifră este cea mai probabilă pentru o imagine dată.

* Instrucțiuni
* Notebook

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.