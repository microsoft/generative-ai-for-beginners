<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:02:07+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "nl"
}
-->
# Neuraal Netwerk Frameworks

Zoals we al hebben geleerd, moeten we twee dingen doen om neurale netwerken efficiënt te kunnen trainen:

* Opereren op tensors, bijvoorbeeld vermenigvuldigen, optellen en enkele functies berekenen zoals sigmoid of softmax
* Gradienten van alle uitdrukkingen berekenen, om optimalisatie via gradient descent uit te voeren

Hoewel de `numpy` bibliotheek het eerste deel kan doen, hebben we een mechanisme nodig om gradients te berekenen. In ons framework dat we in de vorige sectie hebben ontwikkeld, moesten we alle afgeleide functies handmatig programmeren binnen de `backward` methode, die backpropagation uitvoert. Idealiter zou een framework ons de mogelijkheid moeten geven om gradients van *elke uitdrukking* die we kunnen definiëren te berekenen.

Een andere belangrijke zaak is om berekeningen op GPU of andere gespecialiseerde rekenunits, zoals TPU, te kunnen uitvoeren. Diepe neurale netwerktraining vereist *veel* berekeningen, en het is erg belangrijk om die berekeningen op GPU's te kunnen paralleliseren.

> ✅ De term 'paralleliseren' betekent het verdelen van de berekeningen over meerdere apparaten.

Momenteel zijn de twee meest populaire neurale frameworks: TensorFlow en PyTorch. Beide bieden een low-level API om met tensors te werken op zowel CPU als GPU. Bovenop de low-level API is er ook een high-level API, respectievelijk Keras en PyTorch Lightning genoemd.

Low-Level API | TensorFlow | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | Pytorch

**Low-level API's** in beide frameworks stellen je in staat om zogenaamde **berekeningsgrafieken** te bouwen. Deze grafiek definieert hoe de uitvoer (meestal de verliesfunctie) wordt berekend met gegeven invoerparameters, en kan voor berekening op GPU worden gezet, als deze beschikbaar is. Er zijn functies om deze berekeningsgrafiek te differentiëren en gradients te berekenen, die vervolgens kunnen worden gebruikt voor het optimaliseren van modelparameters.

**High-level API's** beschouwen neurale netwerken als een **reeks lagen**, en maken het construeren van de meeste neurale netwerken veel eenvoudiger. Het trainen van het model vereist meestal het voorbereiden van de gegevens en vervolgens het aanroepen van een `fit` functie om de taak uit te voeren.

De high-level API stelt je in staat om typische neurale netwerken zeer snel te construeren zonder je zorgen te maken over veel details. Tegelijkertijd bieden low-level API's veel meer controle over het trainingsproces, en daarom worden ze veel gebruikt in onderzoek, wanneer je te maken hebt met nieuwe neurale netwerkarchitecturen.

Het is ook belangrijk om te begrijpen dat je beide API's samen kunt gebruiken, bijvoorbeeld door je eigen netwerklaagarchitectuur te ontwikkelen met de low-level API, en deze vervolgens te gebruiken binnen het grotere netwerk dat is geconstrueerd en getraind met de high-level API. Of je kunt een netwerk definiëren met de high-level API als een reeks lagen, en vervolgens je eigen low-level trainingslus gebruiken om optimalisatie uit te voeren. Beide API's gebruiken dezelfde basisconcepten en zijn ontworpen om goed samen te werken.

## Leren

In deze cursus bieden we de meeste inhoud zowel voor PyTorch als TensorFlow. Je kunt je voorkeursframework kiezen en alleen de bijbehorende notitieboeken doorlopen. Als je niet zeker weet welk framework je moet kiezen, lees dan enkele discussies op internet over **PyTorch vs. TensorFlow**. Je kunt ook beide frameworks bekijken om een beter begrip te krijgen.

Waar mogelijk zullen we High-Level API's gebruiken voor eenvoud. We vinden het echter belangrijk om te begrijpen hoe neurale netwerken vanaf de basis werken, dus beginnen we met werken met low-level API en tensors. Als je echter snel aan de slag wilt en niet veel tijd wilt besteden aan het leren van deze details, kun je deze overslaan en direct naar de high-level API-notitieboeken gaan.

## ✍️ Oefeningen: Frameworks

Zet je leerproces voort in de volgende notitieboeken:

Low-Level API | TensorFlow+Keras Notitieboek | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Nadat je de frameworks hebt beheerst, laten we het begrip overfitting herhalen.

# Overfitting

Overfitting is een uiterst belangrijk concept in machine learning, en het is erg belangrijk om het goed te begrijpen!

Overweeg het volgende probleem van het benaderen van 5 punten (weergegeven door `x` op de onderstaande grafieken):

!linear | overfit
-------------------------|--------------------------
**Lineair model, 2 parameters** | **Niet-lineair model, 7 parameters**
Trainingsfout = 5.3 | Trainingsfout = 0
Validatiefout = 5.1 | Validatiefout = 20

* Links zien we een goede rechte lijn benadering. Omdat het aantal parameters adequaat is, begrijpt het model de idee achter de puntverdeling goed.
* Rechts is het model te krachtig. Omdat we slechts 5 punten hebben en het model 7 parameters heeft, kan het zich zo aanpassen dat het door alle punten gaat, waardoor de trainingsfout 0 wordt. Dit voorkomt echter dat het model het correcte patroon achter de gegevens begrijpt, waardoor de validatiefout erg hoog is.

Het is erg belangrijk om een juiste balans te vinden tussen de rijkdom van het model (aantal parameters) en het aantal trainingsvoorbeelden.

## Waarom overfitting optreedt

  * Niet genoeg trainingsdata
  * Te krachtig model
  * Te veel ruis in invoergegevens

## Hoe overfitting te detecteren

Zoals je kunt zien op de bovenstaande grafiek, kan overfitting worden gedetecteerd door een zeer lage trainingsfout en een hoge validatiefout. Normaal gesproken zullen we tijdens de training zien dat zowel de trainings- als validatiefouten beginnen te dalen, en dan kan op een gegeven moment de validatiefout stoppen met dalen en beginnen te stijgen. Dit is een teken van overfitting en een indicatie dat we waarschijnlijk op dit punt moeten stoppen met trainen (of in ieder geval een momentopname van het model moeten maken).

## Hoe overfitting te voorkomen

Als je ziet dat overfitting optreedt, kun je een van de volgende dingen doen:

 * Vergroot de hoeveelheid trainingsdata
 * Verminder de complexiteit van het model
 * Gebruik een regularisatietechniek, zoals Dropout, die we later zullen behandelen.

## Overfitting en Bias-Variance Afweging

Overfitting is eigenlijk een geval van een meer algemeen probleem in de statistiek genaamd Bias-Variance Afweging. Als we de mogelijke bronnen van fouten in ons model beschouwen, kunnen we twee soorten fouten zien:

* **Biasfouten** worden veroorzaakt doordat ons algoritme niet in staat is om de relatie tussen trainingsdata correct vast te leggen. Dit kan het gevolg zijn van het feit dat ons model niet krachtig genoeg is (**underfitting**).
* **Variantie fouten**, die worden veroorzaakt doordat het model ruis in de invoergegevens benadert in plaats van een betekenisvolle relatie (**overfitting**).

Tijdens de training neemt de biasfout af (naarmate ons model leert de gegevens te benaderen), en neemt de variantiefout toe. Het is belangrijk om de training te stoppen - ofwel handmatig (wanneer we overfitting detecteren) of automatisch (door regularisatie in te voeren) - om overfitting te voorkomen.

## Conclusie

In deze les heb je geleerd over de verschillen tussen de verschillende API's voor de twee meest populaire AI-frameworks, TensorFlow en PyTorch. Daarnaast heb je geleerd over een zeer belangrijk onderwerp, overfitting.

## 🚀 Uitdaging

In de bijbehorende notitieboeken vind je 'taken' onderaan; werk de notitieboeken door en voltooi de taken.

## Review & Zelfstudie

Doe wat onderzoek naar de volgende onderwerpen:

- TensorFlow
- PyTorch
- Overfitting

Stel jezelf de volgende vragen:

- Wat is het verschil tussen TensorFlow en PyTorch?
- Wat is het verschil tussen overfitting en underfitting?

## Opdracht

In dit lab word je gevraagd om twee classificatieproblemen op te lossen met behulp van enkel- en meerlagige volledig verbonden netwerken met PyTorch of TensorFlow.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.