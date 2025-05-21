<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:22:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "nl"
}
-->
# Introductie tot Neurale Netwerken. Multi-Laags Perceptron

In het vorige gedeelte heb je geleerd over het eenvoudigste neurale netwerkmodel - eenlaags perceptron, een lineair tweeklassen classificatiemodel.

In dit gedeelte zullen we dit model uitbreiden naar een flexibeler kader, waardoor we in staat zijn om:

* **multi-klasse classificatie** uit te voeren naast tweeklassen
* **regressieproblemen** op te lossen naast classificatie
* klassen te scheiden die niet lineair scheidbaar zijn

We zullen ook ons eigen modulaire kader in Python ontwikkelen dat ons in staat stelt om verschillende neurale netwerkarchitecturen te bouwen.

## Formulering van Machine Learning

Laten we beginnen met het formaliseren van het Machine Learning probleem. Stel dat we een trainingsdataset **X** hebben met labels **Y**, en we moeten een model *f* bouwen dat de meest nauwkeurige voorspellingen zal maken. De kwaliteit van voorspellingen wordt gemeten door **verliesfunctie** ℒ. De volgende verliesfuncties worden vaak gebruikt:

* Voor regressieproblemen, wanneer we een getal moeten voorspellen, kunnen we **absolute fout** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, of **kwadratische fout** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> gebruiken.
* Voor classificatie gebruiken we **0-1 verlies** (wat in wezen hetzelfde is als **nauwkeurigheid** van het model), of **logistisch verlies**.

Voor een eenlaags perceptron werd functie *f* gedefinieerd als een lineaire functie *f(x)=wx+b* (hier is *w* de gewichts matrix, *x* is de vector van invoerfuncties, en *b* is de bias vector). Voor verschillende neurale netwerkarchitecturen kan deze functie een complexere vorm aannemen.

> In het geval van classificatie is het vaak wenselijk om waarschijnlijkheden van overeenkomstige klassen als netwerkuitvoer te krijgen. Om willekeurige getallen om te zetten naar waarschijnlijkheden (bijv. om de uitvoer te normaliseren), gebruiken we vaak de **softmax** functie σ, en wordt de functie *f* *f(x)=σ(wx+b)*

In de definitie van *f* hierboven worden *w* en *b* **parameters** genoemd θ=⟨*w,b*⟩. Gegeven de dataset ⟨**X**,**Y**⟩, kunnen we een totale fout op de hele dataset berekenen als een functie van parameters θ.

> ✅ **Het doel van neurale netwerktraining is om de fout te minimaliseren door parameters θ te variëren**

## Optimalisatie met Gradiente Daling

Er is een bekende methode voor functieoptimalisatie genaamd **gradiente daling**. Het idee is dat we een afgeleide (in het multidimensionale geval genaamd **gradiënt**) van de verliesfunctie kunnen berekenen ten opzichte van parameters, en parameters kunnen variëren op een manier dat de fout zou afnemen. Dit kan als volgt worden geformaliseerd:

* Initialiseer parameters met willekeurige waarden w<sup>(0)</sup>, b<sup>(0)</sup>
* Herhaal de volgende stap vele malen:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijdens de training moeten de optimalisatiestappen worden berekend met inachtneming van de hele dataset (onthoud dat verlies wordt berekend als een som over alle trainingsmonsters). Echter, in de praktijk nemen we kleine porties van de dataset genaamd **minibatches**, en berekenen we gradiënten op basis van een subset van gegevens. Omdat de subset elke keer willekeurig wordt genomen, wordt deze methode **stochastische gradiente daling** (SGD) genoemd.

## Multi-Laags Perceptrons en Terugpropagatie

Eenlaags netwerk, zoals we hierboven hebben gezien, is in staat om lineair scheidbare klassen te classificeren. Om een rijker model te bouwen, kunnen we verschillende lagen van het netwerk combineren. Wiskundig zou dit betekenen dat de functie *f* een complexere vorm zou hebben, en in verschillende stappen zal worden berekend:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hier is α een **niet-lineaire activatiefunctie**, σ is een softmax functie, en parameters θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Het gradiente daling algoritme zou hetzelfde blijven, maar het zou moeilijker zijn om gradiënten te berekenen. Gegeven de kettingregel voor differentiatie, kunnen we afgeleiden berekenen als:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ De kettingregel voor differentiatie wordt gebruikt om afgeleiden van de verliesfunctie ten opzichte van parameters te berekenen.

Merk op dat het meest linkse deel van al deze uitdrukkingen hetzelfde is, en dus kunnen we effectief afgeleiden berekenen, beginnend bij de verliesfunctie en "achterwaarts" door de computationele grafiek gaand. Daarom wordt de methode voor het trainen van een multi-laags perceptron **terugpropagatie**, of 'backprop', genoemd.

> TODO: afbeelding referentie

> ✅ We zullen terugpropagatie veel gedetailleerder behandelen in ons notitieboekvoorbeeld.

## Conclusie

In deze les hebben we onze eigen neurale netwerkbibliotheek gebouwd, en we hebben deze gebruikt voor een eenvoudige tweedimensionale classificatietaak.

## 🚀 Uitdaging

In het bijbehorende notitieboek implementeer je je eigen kader voor het bouwen en trainen van multi-laags perceptrons. Je zult in detail kunnen zien hoe moderne neurale netwerken werken.

Ga verder naar het OwnFramework notitieboek en werk het door.

## Herziening & Zelfstudie

Terugpropagatie is een veelgebruikt algoritme in AI en ML, de moeite waard om in meer detail te bestuderen.

## Opdracht

In dit lab word je gevraagd om het kader dat je in deze les hebt geconstrueerd te gebruiken om de MNIST handgeschreven cijferclassificatie op te lossen.

* Instructies
* Notitieboek

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, moet u zich ervan bewust zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.