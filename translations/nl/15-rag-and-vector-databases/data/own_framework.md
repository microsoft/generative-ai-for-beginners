<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:48:25+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "nl"
}
-->
# Introductie tot Neurale Netwerken. Multi-Layered Perceptron

In de vorige sectie heb je geleerd over het eenvoudigste neurale netwerkmodel - de eendelige perceptron, een lineair tweeklassenclassificatiemodel.

In deze sectie breiden we dit model uit naar een flexibeler kader, waarmee we kunnen:

* **multi-klasse classificatie** uitvoeren naast tweeklassenclassificatie
* **regressieproblemen** oplossen naast classificatie
* klassen scheiden die niet lineair scheidbaar zijn

We ontwikkelen ook ons eigen modulaire framework in Python waarmee we verschillende neurale netwerkarchitecturen kunnen bouwen.

## Formele beschrijving van Machine Learning

Laten we beginnen met het formaliseren van het Machine Learning probleem. Stel dat we een trainingsdataset **X** hebben met labels **Y**, en we moeten een model *f* bouwen dat zo nauwkeurig mogelijk voorspellingen doet. De kwaliteit van de voorspellingen wordt gemeten met een **verliesfunctie** ℒ. De volgende verliesfuncties worden vaak gebruikt:

* Voor regressieproblemen, waarbij we een getal moeten voorspellen, kunnen we de **absolute fout** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| gebruiken, of de **kwadratische fout** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Voor classificatie gebruiken we de **0-1 verliesfunctie** (wat in feite hetzelfde is als de **nauwkeurigheid** van het model), of de **logistische verliesfunctie**.

Voor de eendelige perceptron werd de functie *f* gedefinieerd als een lineaire functie *f(x)=wx+b* (hier is *w* de gewichtsmatrix, *x* de vector van invoerkenmerken, en *b* de biasvector). Voor verschillende neurale netwerkarchitecturen kan deze functie complexer zijn.

> In het geval van classificatie is het vaak wenselijk om waarschijnlijkheden van de corresponderende klassen als netwerkoutput te krijgen. Om willekeurige getallen om te zetten in waarschijnlijkheden (bijvoorbeeld om de output te normaliseren), gebruiken we vaak de **softmax** functie σ, en wordt de functie *f* *f(x)=σ(wx+b)*

In de bovenstaande definitie van *f* worden *w* en *b* **parameters** genoemd θ=⟨*w,b*⟩. Gegeven de dataset ⟨**X**,**Y**⟩ kunnen we de totale fout over de hele dataset berekenen als een functie van de parameters θ.

> ✅ **Het doel van het trainen van een neuraal netwerk is om de fout te minimaliseren door de parameters θ aan te passen**

## Gradient Descent Optimalisatie

Er is een bekende methode voor functieoptimalisatie genaamd **gradient descent**. Het idee is dat we de afgeleide (in het meerdimensionale geval de **gradiënt**) van de verliesfunctie ten opzichte van de parameters kunnen berekenen, en de parameters zo kunnen aanpassen dat de fout afneemt. Dit kan als volgt worden geformaliseerd:

* Initialiseer de parameters met willekeurige waarden w<sup>(0)</sup>, b<sup>(0)</sup>
* Herhaal de volgende stap meerdere keren:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijdens het trainen worden de optimalisatiestappen berekend over de hele dataset (onthoud dat de verliesfunctie wordt berekend als een som over alle trainingsvoorbeelden). In de praktijk nemen we echter kleine delen van de dataset, zogenaamde **minibatches**, en berekenen we de gradiënten op basis van een subset van de data. Omdat deze subset elke keer willekeurig wordt gekozen, heet deze methode **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons en Backpropagation

Een eendelig netwerk, zoals hierboven gezien, kan lineair scheidbare klassen classificeren. Om een rijker model te bouwen, kunnen we meerdere lagen van het netwerk combineren. Wiskundig betekent dit dat de functie *f* een complexere vorm krijgt en in meerdere stappen wordt berekend:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hier is α een **niet-lineaire activatiefunctie**, σ is de softmaxfunctie, en de parameters zijn θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Het gradient descent algoritme blijft hetzelfde, maar het wordt moeilijker om de gradiënten te berekenen. Met behulp van de kettingregel voor afgeleiden kunnen we de afgeleiden als volgt berekenen:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ De kettingregel wordt gebruikt om de afgeleiden van de verliesfunctie ten opzichte van de parameters te berekenen.

Merk op dat het meest linkse deel van al deze uitdrukkingen hetzelfde is, waardoor we effectief de afgeleiden kunnen berekenen door te beginnen bij de verliesfunctie en "achteruit" te gaan door de computationele grafiek. Daarom wordt de methode om een multi-layered perceptron te trainen **backpropagation**, of kortweg 'backprop' genoemd.

> TODO: afbeelding bronvermelding

> ✅ We zullen backprop in veel meer detail behandelen in ons notebookvoorbeeld.

## Conclusie

In deze les hebben we onze eigen neurale netwerkbibliotheek gebouwd en deze gebruikt voor een eenvoudige tweedimensionale classificatietaak.

## 🚀 Uitdaging

In het bijbehorende notebook ga je je eigen framework implementeren voor het bouwen en trainen van multi-layered perceptrons. Je zult in detail kunnen zien hoe moderne neurale netwerken werken.

Ga verder naar het OwnFramework notebook en werk het door.

## Review & Zelfstudie

Backpropagation is een veelgebruikt algoritme in AI en ML, het is de moeite waard om dit grondiger te bestuderen.

## Opdracht

In dit practicum wordt van je gevraagd om het framework dat je in deze les hebt gebouwd te gebruiken om de MNIST handgeschreven cijferclassificatie op te lossen.

* Instructies  
* Notebook

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.