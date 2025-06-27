<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:26:52+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "nl"
}
-->
# Introductie tot Neurale Netwerken. Multi-Layered Perceptron

In de vorige sectie leerde je over het eenvoudigste neurale netwerkmodel - de enkelvoudige perceptron, een lineair tweeklassen classificatiemodel.

In deze sectie breiden we dit model uit naar een flexibeler kader, waardoor we:

* **multiklassen classificatie** kunnen uitvoeren naast tweeklassen
* **regressieproblemen** kunnen oplossen naast classificatie
* klassen kunnen scheiden die niet lineair scheidbaar zijn

We zullen ook ons eigen modulaire kader in Python ontwikkelen waarmee we verschillende neurale netwerkarchitecturen kunnen bouwen.

## Formulering van Machine Learning

Laten we beginnen met het formaliseren van het Machine Learning probleem. Stel dat we een trainingsdataset **X** hebben met labels **Y**, en we moeten een model *f* bouwen dat de meest nauwkeurige voorspellingen maakt. De kwaliteit van de voorspellingen wordt gemeten door de **verliesfunctie** ℒ. De volgende verliesfuncties worden vaak gebruikt:

* Voor regressieproblemen, wanneer we een getal moeten voorspellen, kunnen we **absolute fout** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, of **kwadratische fout** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> gebruiken.
* Voor classificatie gebruiken we **0-1 verlies** (wat in wezen hetzelfde is als de **nauwkeurigheid** van het model), of **logistisch verlies**.

Voor een enkelvoudige perceptron was functie *f* gedefinieerd als een lineaire functie *f(x)=wx+b* (hier is *w* de gewichts matrix, *x* de vector van invoerkenmerken, en *b* de bias vector). Voor verschillende neurale netwerkarchitecturen kan deze functie een complexere vorm aannemen.

> In het geval van classificatie is het vaak wenselijk om waarschijnlijkheden van de corresponderende klassen als netwerkuitvoer te krijgen. Om willekeurige getallen om te zetten in waarschijnlijkheden (bijvoorbeeld om de uitvoer te normaliseren), gebruiken we vaak de **softmax** functie σ, en de functie *f* wordt *f(x)=σ(wx+b)*

In de definitie van *f* hierboven worden *w* en *b* **parameters** genoemd θ=⟨*w,b*⟩. Gegeven de dataset ⟨**X**,**Y**⟩, kunnen we een totale fout op de hele dataset berekenen als een functie van parameters θ.

> ✅ **Het doel van het trainen van een neuraal netwerk is om de fout te minimaliseren door de parameters θ te variëren**

## Optimalisatie met Gradient Descent

Er is een bekende methode voor functieoptimalisatie genaamd **gradient descent**. Het idee is dat we een afgeleide (in het multidimensionale geval de **gradiënt** genoemd) van de verliesfunctie ten opzichte van de parameters kunnen berekenen, en de parameters zodanig kunnen variëren dat de fout zou afnemen. Dit kan als volgt worden geformaliseerd:

* Initialiseer parameters met enkele willekeurige waarden w<sup>(0)</sup>, b<sup>(0)</sup>
* Herhaal de volgende stap vele malen:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijdens het trainen moeten de optimalisatiestappen worden berekend met inachtneming van de hele dataset (onthoud dat verlies wordt berekend als een som over alle trainingsvoorbeelden). In de praktijk nemen we echter kleine delen van de dataset, zogenaamde **minibatches**, en berekenen we de gradiënten op basis van een subset van gegevens. Omdat de subset elke keer willekeurig wordt genomen, wordt deze methode **stochastische gradient descent** (SGD) genoemd.

## Multi-Layered Perceptrons en Backpropagation

Een eenlaagse netwerk, zoals we hierboven hebben gezien, is in staat om lineair scheidbare klassen te classificeren. Om een rijker model te bouwen, kunnen we meerdere lagen van het netwerk combineren. Wiskundig gezien zou dit betekenen dat de functie *f* een complexere vorm zou hebben, en in verschillende stappen zou worden berekend:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hier is α een **niet-lineaire activatiefunctie**, σ is een softmax functie, en parameters θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Het gradient descent algoritme zou hetzelfde blijven, maar het zou moeilijker zijn om de gradiënten te berekenen. Gegeven de kettingregel voor differentiatie, kunnen we de afgeleiden berekenen als:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ De kettingregel voor differentiatie wordt gebruikt om de afgeleiden van de verliesfunctie ten opzichte van de parameters te berekenen.

Merk op dat het meest linkse deel van al deze uitdrukkingen hetzelfde is, en dus kunnen we effectief de afgeleiden berekenen, te beginnen bij de verliesfunctie en "achterwaarts" door de computationele grafiek te gaan. Daarom wordt de methode voor het trainen van een meerlagige perceptron **backpropagation** genoemd, of 'backprop'.

> TODO: afbeelding citeren

> ✅ We zullen backprop in veel meer detail behandelen in ons notebookvoorbeeld.  

## Conclusie

In deze les hebben we onze eigen neurale netwerkbibliotheek gebouwd en hebben we deze gebruikt voor een eenvoudige tweedimensionale classificatietaak.

## 🚀 Uitdaging

In het bijbehorende notebook implementeer je je eigen kader voor het bouwen en trainen van meerlaagse perceptrons. Je zult in detail kunnen zien hoe moderne neurale netwerken werken.

Ga verder naar het OwnFramework notebook en werk het door.

## Herziening & Zelfstudie

Backpropagation is een veelgebruikt algoritme in AI en ML, het is de moeite waard om het in meer detail te bestuderen.

## Opdracht

In dit lab wordt je gevraagd om het kader dat je in deze les hebt gebouwd te gebruiken om de MNIST handgeschreven cijferclassificatie op te lossen.

* Instructies
* Notebook

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.