<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:59:04+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "nl"
}
-->
# Introductie tot Neurale Netwerken: Perceptron

Een van de eerste pogingen om iets te maken dat lijkt op een modern neuraal netwerk werd gedaan door Frank Rosenblatt van het Cornell Aeronautical Laboratory in 1957. Het was een hardware-implementatie genaamd "Mark-1", ontworpen om primitieve geometrische figuren te herkennen, zoals driehoeken, vierkanten en cirkels.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Afbeeldingen van Wikipedia

Een invoerafbeelding werd weergegeven door een 20x20 fotocel-array, dus het neurale netwerk had 400 inputs en één binaire output. Een eenvoudig netwerk bestond uit één neuron, ook wel een **drempellogica-eenheid** genoemd. De gewichten van het neurale netwerk werkten als potentiometers die handmatig moesten worden aangepast tijdens de trainingsfase.

> ✅ Een potentiometer is een apparaat waarmee de gebruiker de weerstand van een circuit kan aanpassen.

> The New York Times schreef destijds over de perceptron: *het embryo van een elektronische computer waarvan [de marine] verwacht dat hij kan lopen, praten, zien, schrijven, zichzelf reproduceren en zich bewust zijn van zijn bestaan.*

## Perceptron Model

Stel dat we N kenmerken in ons model hebben, in dat geval is de invoervector een vector van grootte N. Een perceptron is een **binair classificatiemodel**, dat wil zeggen dat het kan onderscheiden tussen twee klassen van invoergegevens. We gaan ervan uit dat voor elke invoervector x de output van onze perceptron ofwel +1 of -1 is, afhankelijk van de klasse. De output wordt berekend met de formule:

y(x) = f(w<sup>T</sup>x)

waarbij f een stapactivatiefunctie is

## Het trainen van de Perceptron

Om een perceptron te trainen moeten we een gewichtsvector w vinden die de meeste waarden correct classificeert, oftewel resulteert in de kleinste **fout**. Deze fout wordt gedefinieerd door het **perceptroncriterium** op de volgende manier:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

waarbij:

* de som wordt genomen over die trainingsdata punten i die leiden tot een verkeerde classificatie
* x<sub>i</sub> de invoergegevens zijn, en t<sub>i</sub> is ofwel -1 of +1 voor respectievelijk negatieve en positieve voorbeelden.

Dit criterium wordt beschouwd als een functie van de gewichten w, en we moeten het minimaliseren. Vaak wordt een methode gebruikt die **gradient descent** heet, waarbij we beginnen met een initiële gewichtsvector w<sup>(0)</sup>, en vervolgens bij elke stap de gewichten bijwerken volgens de formule:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hier is η de zogenaamde **leersnelheid**, en ∇E(w) staat voor de **gradiënt** van E. Nadat we de gradiënt hebben berekend, krijgen we:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Het algoritme in Python ziet er als volgt uit:

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

## Conclusie

In deze les heb je geleerd wat een perceptron is, een binair classificatiemodel, en hoe je het kunt trainen met behulp van een gewichtsvector.

## 🚀 Uitdaging

Als je zelf een perceptron wilt bouwen, probeer dan deze lab op Microsoft Learn die gebruikmaakt van de Azure ML designer


## Review & Zelfstudie

Om te zien hoe we een perceptron kunnen gebruiken om een eenvoudig probleem en ook echte problemen op te lossen, en om verder te leren - ga naar het Perceptron notebook.

Hier is ook een interessant artikel over perceptrons.

## Opdracht

In deze les hebben we een perceptron geïmplementeerd voor een binaire classificatietaak, en hebben we het gebruikt om te classificeren tussen twee handgeschreven cijfers. In deze lab wordt van je gevraagd het probleem van cijferclassificatie volledig op te lossen, oftewel te bepalen welk cijfer het meest waarschijnlijk overeenkomt met een gegeven afbeelding.

* Instructies
* Notebook

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.