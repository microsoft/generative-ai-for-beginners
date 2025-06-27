<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:41:54+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "nl"
}
-->
# Introductie tot Neurale Netwerken: Perceptron

Een van de eerste pogingen om iets vergelijkbaars met een modern neuraal netwerk te implementeren werd in 1957 gedaan door Frank Rosenblatt van het Cornell Aeronautical Laboratory. Het was een hardware-implementatie genaamd "Mark-1", ontworpen om primitieve geometrische figuren te herkennen, zoals driehoeken, vierkanten en cirkels.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Afbeeldingen van Wikipedia

Een invoerafbeelding werd weergegeven door een 20x20 fotocelmatrix, dus het neurale netwerk had 400 ingangen en één binaire uitvoer. Een eenvoudig netwerk bevatte één neuron, ook wel een **drempellogica-eenheid** genoemd. De gewichten van het neurale netwerk fungeerden als potentiometers die handmatig moesten worden aangepast tijdens de trainingsfase.

> ✅ Een potentiometer is een apparaat waarmee de gebruiker de weerstand van een circuit kan aanpassen.

> De New York Times schreef destijds over de perceptron: *het embryo van een elektronische computer waarvan [de Marine] verwacht dat het kan lopen, praten, zien, schrijven, zichzelf reproduceren en zich bewust is van zijn bestaan.*

## Perceptron Model

Stel dat we N kenmerken in ons model hebben, in welk geval de invoervector een vector van grootte N zou zijn. Een perceptron is een **binaire classificatie** model, dat wil zeggen dat het onderscheid kan maken tussen twee klassen van invoergegevens. We zullen aannemen dat voor elke invoervector x de uitvoer van onze perceptron ofwel +1 of -1 zou zijn, afhankelijk van de klasse. De uitvoer wordt berekend met behulp van de formule:

y(x) = f(w<sup>T</sup>x)

waarbij f een stap-activatiefunctie is

## Het trainen van de Perceptron

Om een perceptron te trainen moeten we een gewichtenvector w vinden die de meeste waarden correct classificeert, dat wil zeggen resulteert in de kleinste **fout**. Deze fout wordt gedefinieerd door het **perceptroncriterium** op de volgende manier:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

waarbij:

* de som wordt genomen over die trainingsgegevenspunten i die resulteren in de verkeerde classificatie
* x<sub>i</sub> de invoergegevens zijn, en t<sub>i</sub> ofwel -1 of +1 is voor respectievelijk negatieve en positieve voorbeelden.

Dit criterium wordt beschouwd als een functie van gewichten w, en we moeten het minimaliseren. Vaak wordt een methode genaamd **gradient descent** gebruikt, waarbij we beginnen met enkele initiële gewichten w<sup>(0)</sup>, en vervolgens bij elke stap de gewichten bijwerken volgens de formule:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hier is η de zogenaamde **leersnelheid**, en ∇E(w) duidt de **gradiënt** van E aan. Nadat we de gradiënt hebben berekend, eindigen we met

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

In deze les heb je geleerd over een perceptron, een binaire classificatiemodel, en hoe je het kunt trainen met behulp van een gewichtenvector.

## 🚀 Uitdaging

Als je je eigen perceptron wilt bouwen, probeer dan deze lab op Microsoft Learn die de Azure ML designer gebruikt.

## Herziening & Zelfstudie

Om te zien hoe we perceptron kunnen gebruiken om zowel een speelgoedprobleem als echte problemen op te lossen, en om verder te leren - ga naar het Perceptron-notitieboek.

Hier is ook een interessant artikel over perceptrons.

## Opdracht

In deze les hebben we een perceptron geïmplementeerd voor een binaire classificatietaak, en we hebben het gebruikt om te classificeren tussen twee handgeschreven cijfers. In dit lab wordt je gevraagd het probleem van cijferclassificatie volledig op te lossen, dat wil zeggen te bepalen welk cijfer het meest waarschijnlijk overeenkomt met een gegeven afbeelding.

* Instructies
* Notitieboek

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of misinterpretaties die voortvloeien uit het gebruik van deze vertaling.