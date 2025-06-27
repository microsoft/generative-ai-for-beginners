<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:05:58+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "nl"
}
-->
# Neural Network Frameworks

Zoals we al hebben geleerd, om neurale netwerken efficiënt te kunnen trainen moeten we twee dingen doen:

* Werken met tensors, bijvoorbeeld vermenigvuldigen, optellen, en functies zoals sigmoid of softmax berekenen
* De gradients van alle expressies berekenen, om optimalisatie met gradient descent uit te voeren

Hoewel de `numpy` bibliotheek het eerste deel kan doen, hebben we een mechanisme nodig om gradients te berekenen. In ons framework dat we in de vorige sectie hebben ontwikkeld, moesten we alle afgeleide functies handmatig programmeren binnen de `backward` methode, die backpropagation uitvoert. Idealiter zou een framework ons de mogelijkheid moeten geven om gradients van *elke expressie* die we kunnen definiëren te berekenen.

Een ander belangrijk aspect is om berekeningen op een GPU of andere gespecialiseerde rekeneenheden, zoals TPU, te kunnen uitvoeren. Het trainen van diepe neurale netwerken vereist *veel* berekeningen, en het is heel belangrijk om die berekeningen te kunnen paralleliseren op GPU's.

> ✅ De term 'paralleliseren' betekent het verdelen van de berekeningen over meerdere apparaten.

Momenteel zijn de twee meest populaire neurale frameworks: TensorFlow en PyTorch. Beide bieden een low-level API om met tensors te werken op zowel CPU als GPU. Bovenop de low-level API is er ook een high-level API, respectievelijk Keras en PyTorch Lightning.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**Low-level APIs** in beide frameworks stellen je in staat zogenaamde **computational graphs** te bouwen. Deze grafiek definieert hoe de output (meestal de verliesfunctie) met gegeven invoerparameters wordt berekend, en kan voor berekening op GPU worden gezet, indien beschikbaar. Er zijn functies om deze computational graph te differentiëren en gradients te berekenen, die vervolgens kunnen worden gebruikt voor het optimaliseren van modelparameters.

**High-level APIs** beschouwen neurale netwerken vrijwel als een **reeks van lagen**, en maken het construeren van de meeste neurale netwerken veel gemakkelijker. Het trainen van het model vereist meestal het voorbereiden van de data en vervolgens het aanroepen van een `fit` functie om het werk te doen.

De high-level API stelt je in staat typische neurale netwerken heel snel te construeren zonder je zorgen te maken over veel details. Tegelijkertijd biedt de low-level API veel meer controle over het trainingsproces, en wordt daarom veel gebruikt in onderzoek, wanneer je te maken hebt met nieuwe neurale netwerkarchitecturen.

Het is ook belangrijk te begrijpen dat je beide APIs samen kunt gebruiken, bijvoorbeeld je kunt je eigen netwerklaagarchitectuur ontwikkelen met low-level API, en deze vervolgens gebruiken binnen het grotere netwerk dat met de high-level API is geconstrueerd en getraind. Of je kunt een netwerk definiëren met de high-level API als een reeks lagen, en vervolgens je eigen low-level trainingsloop gebruiken om optimalisatie uit te voeren. Beide APIs gebruiken dezelfde basisconcepten en zijn ontworpen om goed samen te werken.

## Leren

In deze cursus bieden we de meeste inhoud zowel voor PyTorch als TensorFlow. Je kunt je voorkeursframework kiezen en alleen de bijbehorende notebooks doorlopen. Als je niet zeker weet welk framework je moet kiezen, lees dan enkele discussies op internet over **PyTorch vs. TensorFlow**. Je kunt ook beide frameworks bekijken voor een beter begrip.

Waar mogelijk zullen we High-Level APIs gebruiken voor eenvoud. Echter, we vinden het belangrijk om te begrijpen hoe neurale netwerken vanaf de basis werken, dus in het begin starten we met werken met low-level API en tensors. Maar als je snel aan de slag wilt en niet veel tijd wilt besteden aan het leren van deze details, kun je die overslaan en direct naar de high-level API notebooks gaan.

## ✍️ Oefeningen: Frameworks

Ga verder met leren in de volgende notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Na het beheersen van de frameworks, laten we het concept van overfitting herzien.

# Overfitting

Overfitting is een uiterst belangrijk concept in machine learning, en het is heel belangrijk om het goed te begrijpen!

Beschouw het volgende probleem van het benaderen van 5 punten (vertegenwoordigd door `x` op de grafieken hieronder):

!linear | overfit
-------------------------|--------------------------
**Lineair model, 2 parameters** | **Niet-lineair model, 7 parameters**
Trainingsfout = 5.3 | Trainingsfout = 0
Validatiefout = 5.1 | Validatiefout = 20

* Links zien we een goede rechte lijn benadering. Omdat het aantal parameters adequaat is, begrijpt het model het idee achter de puntendistributie goed.
* Rechts is het model te krachtig. Omdat we slechts 5 punten hebben en het model 7 parameters heeft, kan het zich zo aanpassen dat het door alle punten gaat, waardoor de trainingsfout 0 is. Dit verhindert echter dat het model het juiste patroon achter de data begrijpt, waardoor de validatiefout erg hoog is.

Het is heel belangrijk om een juiste balans te vinden tussen de rijkdom van het model (aantal parameters) en het aantal trainingssamples.

## Waarom overfitting optreedt

  * Niet genoeg trainingsdata
  * Te krachtig model
  * Te veel ruis in invoergegevens

## Hoe overfitting te detecteren

Zoals je kunt zien in de grafiek hierboven, kan overfitting worden gedetecteerd door een zeer lage trainingsfout en een hoge validatiefout. Normaal gesproken zien we tijdens de training zowel de trainings- als validatiefouten beginnen te dalen, en dan kan op een gegeven moment de validatiefout stoppen met dalen en beginnen te stijgen. Dit zal een teken zijn van overfitting, en de indicator dat we waarschijnlijk moeten stoppen met trainen op dit punt (of in ieder geval een momentopname van het model moeten maken).

overfitting

## Hoe overfitting te voorkomen

Als je ziet dat overfitting optreedt, kun je een van de volgende dingen doen:

 * Verhoog de hoeveelheid trainingsdata
 * Verlaag de complexiteit van het model
 * Gebruik een regularisatietechniek, zoals Dropout, die we later zullen bespreken.

## Overfitting en Bias-Variance Tradeoff

Overfitting is eigenlijk een geval van een meer algemeen probleem in statistiek, genaamd Bias-Variance Tradeoff. Als we de mogelijke bronnen van fouten in ons model beschouwen, kunnen we twee soorten fouten zien:

* **Biasfouten** worden veroorzaakt doordat ons algoritme de relatie tussen trainingsdata niet correct kan vastleggen. Het kan het gevolg zijn van het feit dat ons model niet krachtig genoeg is (**underfitting**).
* **Variantiefouten**, die worden veroorzaakt doordat het model ruis in de invoergegevens benadert in plaats van een betekenisvolle relatie (**overfitting**).

Tijdens de training neemt de biasfout af (aangezien ons model leert de data te benaderen), en neemt de variantiefout toe. Het is belangrijk om de training te stoppen - ofwel handmatig (wanneer we overfitting detecteren) of automatisch (door regularisatie in te voeren) - om overfitting te voorkomen.

## Conclusie

In deze les heb je geleerd over de verschillen tussen de verschillende APIs voor de twee meest populaire AI-frameworks, TensorFlow en PyTorch. Daarnaast heb je geleerd over een heel belangrijk onderwerp, overfitting.

## 🚀 Uitdaging

In de bijbehorende notebooks vind je 'taken' onderaan; werk door de notebooks en voltooi de taken.

## Review & Zelfstudie

Doe wat onderzoek naar de volgende onderwerpen:

- TensorFlow
- PyTorch
- Overfitting

Stel jezelf de volgende vragen:

- Wat is het verschil tussen TensorFlow en PyTorch?
- Wat is het verschil tussen overfitting en underfitting?

## Opdracht

In dit lab wordt je gevraagd twee classificatieproblemen op te lossen met behulp van enkel- en meerlaagse volledig verbonden netwerken met PyTorch of TensorFlow.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of misinterpretaties die voortvloeien uit het gebruik van deze vertaling.