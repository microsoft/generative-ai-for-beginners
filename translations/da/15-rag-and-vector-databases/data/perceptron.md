<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:40:53+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "da"
}
-->
# Introduktion til Neurale Netværk: Perceptron

En af de første forsøg på at implementere noget, der ligner et moderne neuralt netværk, blev udført af Frank Rosenblatt fra Cornell Aeronautical Laboratory i 1957. Det var en hardwareimplementering kaldet "Mark-1", designet til at genkende primitive geometriske figurer som trekanter, firkanter og cirkler.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Billeder fra Wikipedia

Et inputbillede blev repræsenteret af en 20x20 fotocellematrix, så det neurale netværk havde 400 input og en binær output. Et simpelt netværk indeholdt en neuron, også kaldet en **tærskel logikenhed**. Neurale netværksvægte fungerede som potentiometre, der krævede manuel justering under træningsfasen.

> ✅ Et potentiometer er en enhed, der giver brugeren mulighed for at justere modstanden i en kreds.

> The New York Times skrev om perceptron på det tidspunkt: *embryoet til en elektronisk computer, som [flåden] forventer vil kunne gå, tale, se, skrive, reproducere sig selv og være bevidst om sin eksistens.*

## Perceptron Model

Antag, at vi har N funktioner i vores model, i hvilket tilfælde inputvektoren ville være en vektor af størrelse N. En perceptron er en **binær klassifikations**model, dvs. den kan skelne mellem to klasser af inputdata. Vi vil antage, at for hver inputvektor x vil output fra vores perceptron være enten +1 eller -1, afhængigt af klassen. Outputtet beregnes ved hjælp af formlen:

y(x) = f(w<sup>T</sup>x)

hvor f er en trinaktiveringsfunktion

## Træning af Perceptron

For at træne en perceptron skal vi finde en vægtvektor w, der klassificerer de fleste af værdierne korrekt, dvs. resulterer i den mindste **fejl**. Denne fejl defineres af **perceptron kriteriet** på følgende måde:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

hvor:

* summen tages over de træningsdatapunkter i, der resulterer i forkert klassifikation
* x<sub>i</sub> er inputdata, og t<sub>i</sub> er enten -1 eller +1 for henholdsvis negative og positive eksempler.

Dette kriterium betragtes som en funktion af vægtene w, og vi skal minimere det. Ofte bruges en metode kaldet **gradient descent**, hvor vi starter med nogle indledende vægte w<sup>(0)</sup>, og derefter opdaterer vægtene ved hver trin i henhold til formlen:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Her er η den såkaldte **læringsrate**, og ∇E(w) betegner **gradienten** af E. Efter vi har beregnet gradienten, ender vi med

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmen i Python ser sådan ud:

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

## Konklusion

I denne lektion lærte du om en perceptron, som er en binær klassifikationsmodel, og hvordan man træner den ved hjælp af en vægtvektor.

## 🚀 Udfordring

Hvis du gerne vil prøve at bygge din egen perceptron, så prøv dette laboratorium på Microsoft Learn, som bruger Azure ML designer.

## Gennemgang & Selvstudie

For at se, hvordan vi kan bruge perceptron til at løse et legetøjsproblem samt virkelige problemer, og for at fortsætte med at lære - gå til Perceptron-notesbogen.

Her er også en interessant artikel om perceptrons.

## Opgave

I denne lektion har vi implementeret en perceptron til en binær klassifikationsopgave, og vi har brugt den til at klassificere mellem to håndskrevne cifre. I dette laboratorium bliver du bedt om at løse problemet med cifreklassifikation fuldstændigt, dvs. bestemme hvilket ciffer der sandsynligvis svarer til et givet billede.

* Instruktioner
* Notesbog

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår ved brugen af denne oversættelse.