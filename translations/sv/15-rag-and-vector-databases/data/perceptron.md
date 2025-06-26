<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:40:38+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sv"
}
-->
# Introduktion till neurala nätverk: Perceptron

Ett av de första försöken att implementera något liknande ett modernt neuralt nätverk gjordes av Frank Rosenblatt från Cornell Aeronautical Laboratory 1957. Det var en hårdvaruimplementation kallad "Mark-1", designad för att känna igen enkla geometriska figurer, såsom trianglar, kvadrater och cirklar.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Bilder från Wikipedia

En inmatningsbild representerades av en 20x20 fotocellmatris, så det neurala nätverket hade 400 ingångar och en binär utgång. Ett enkelt nätverk innehöll en neuron, även kallad en **tröskellogikenhet**. Neurala nätverksvikterna fungerade som potentiometrar som krävde manuell justering under träningsfasen.

> ✅ En potentiometer är en enhet som låter användaren justera motståndet i en krets.

> The New York Times skrev om perceptron vid den tiden: *embryot till en elektronisk dator som [flottan] förväntar sig kommer att kunna gå, prata, se, skriva, reproducera sig själv och vara medveten om sin existens.*

## Perceptronmodell

Anta att vi har N funktioner i vår modell, i vilket fall inmatningsvektorn skulle vara en vektor av storlek N. En perceptron är en **binär klassificerings**modell, dvs. den kan skilja mellan två klasser av inmatningsdata. Vi antar att för varje inmatningsvektor x skulle utgången från vår perceptron vara antingen +1 eller -1, beroende på klassen. Utgången beräknas med formeln:

y(x) = f(w<sup>T</sup>x)

där f är en stegaktiveringsfunktion

## Träna perceptronen

För att träna en perceptron behöver vi hitta en viktvektor w som klassificerar de flesta av värdena korrekt, dvs. resulterar i det minsta **felet**. Detta fel definieras av **perceptronkriteriet** på följande sätt:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

där:

* summan tas på de träningsdatapunkter i som resulterar i felaktig klassificering
* x<sub>i</sub> är inmatningsdata, och t<sub>i</sub> är antingen -1 eller +1 för negativa respektive positiva exempel.

Detta kriterium betraktas som en funktion av vikterna w, och vi behöver minimera det. Ofta används en metod kallad **gradientnedstigning**, där vi börjar med några initiala vikter w<sup>(0)</sup>, och sedan vid varje steg uppdaterar vikterna enligt formeln:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Här är η den så kallade **inlärningshastigheten**, och ∇E(w) betecknar **gradienten** av E. Efter att vi beräknar gradienten, hamnar vi med

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmen i Python ser ut så här:

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

## Slutsats

I denna lektion lärde du dig om en perceptron, som är en binär klassificeringsmodell, och hur man tränar den genom att använda en viktvektor.

## 🚀 Utmaning

Om du vill prova att bygga din egen perceptron, prova denna labb på Microsoft Learn som använder Azure ML designer.

## Granskning & Självstudier

För att se hur vi kan använda perceptron för att lösa ett leksaksproblem såväl som verkliga problem, och för att fortsätta lära - gå till Perceptron-notebook.

Här är en intressant artikel om perceptroner också.

## Uppgift

I denna lektion har vi implementerat en perceptron för en binär klassificeringsuppgift, och vi har använt den för att klassificera mellan två handskrivna siffror. I denna labb blir du ombedd att lösa problemet med sifferklassificering helt och hållet, dvs. bestämma vilken siffra som mest sannolikt motsvarar en given bild.

* Instruktioner
* Notebook

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår vid användning av denna översättning.