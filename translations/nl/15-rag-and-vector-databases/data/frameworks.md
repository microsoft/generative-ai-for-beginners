<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:33:53+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "nl"
}
-->
# Neural Network Frameworks

Zoals we al hebben geleerd, moeten we om neurale netwerken efficiënt te kunnen trainen twee dingen doen:

* Werken met tensors, bijvoorbeeld vermenigvuldigen, optellen en functies berekenen zoals sigmoid of softmax
* Gradiënten van alle uitdrukkingen berekenen om zo gradient descent optimalisatie uit te voeren

Hoewel de `numpy`-bibliotheek het eerste deel kan doen, hebben we een mechanisme nodig om gradiënten te berekenen. In ons framework dat we in de vorige sectie hebben ontwikkeld, moesten we alle afgeleide functies handmatig programmeren binnen de `backward`-methode, die backpropagation uitvoert. Idealiter zou een framework ons de mogelijkheid moeten bieden om gradiënten te berekenen van *elke uitdrukking* die we kunnen definiëren.

Een ander belangrijk punt is dat we berekeningen moeten kunnen uitvoeren op GPU, of andere gespecialiseerde rekeneenheden zoals TPU. Het trainen van diepe neurale netwerken vereist *veel* berekeningen, en het is erg belangrijk om deze berekeningen te kunnen paralleliseren op GPU’s.

> ✅ De term 'paralleliseren' betekent het verdelen van berekeningen over meerdere apparaten.

Op dit moment zijn de twee populairste neurale frameworks: TensorFlow en PyTorch. Beide bieden een low-level API om met tensors te werken op zowel CPU als GPU. Bovenop de low-level API is er ook een high-level API, respectievelijk Keras en PyTorch Lightning.

Low-Level API | TensorFlow | PyTorch  
--------------|-------------------------------|------------------------------  
High-level API| Keras                         | PyTorch  

**Low-level API’s** in beide frameworks stellen je in staat zogenaamde **computational graphs** te bouwen. Deze grafiek definieert hoe de output (meestal de lossfunctie) wordt berekend met gegeven inputparameters, en kan worden uitgevoerd op GPU als die beschikbaar is. Er zijn functies om deze computational graph te differentiëren en gradiënten te berekenen, die vervolgens gebruikt kunnen worden om modelparameters te optimaliseren.

**High-level API’s** beschouwen neurale netwerken vooral als een **reeks lagen**, en maken het bouwen van de meeste neurale netwerken veel eenvoudiger. Het trainen van het model vereist meestal het voorbereiden van de data en daarna het aanroepen van een `fit`-functie om het werk te doen.

De high-level API stelt je in staat typische neurale netwerken snel te bouwen zonder je zorgen te maken over veel details. Tegelijkertijd bieden low-level API’s veel meer controle over het trainingsproces, en worden ze daarom veel gebruikt in onderzoek, wanneer je met nieuwe neurale netwerkarchitecturen werkt.

Het is ook belangrijk te begrijpen dat je beide API’s samen kunt gebruiken, bijvoorbeeld door je eigen netwerklaagarchitectuur te ontwikkelen met de low-level API en die vervolgens te gebruiken binnen een groter netwerk dat is gebouwd en getraind met de high-level API. Of je definieert een netwerk met de high-level API als een reeks lagen, en gebruikt daarna je eigen low-level trainingslus om de optimalisatie uit te voeren. Beide API’s gebruiken dezelfde onderliggende basisconcepten en zijn ontworpen om goed samen te werken.

## Leren

In deze cursus bieden we de meeste inhoud zowel voor PyTorch als TensorFlow. Je kunt je favoriete framework kiezen en alleen de bijbehorende notebooks doorlopen. Als je niet zeker weet welk framework je moet kiezen, lees dan wat discussies op internet over **PyTorch vs. TensorFlow**. Je kunt ook beide frameworks bekijken om een beter begrip te krijgen.

Waar mogelijk gebruiken we High-Level API’s voor eenvoud. We vinden het echter belangrijk dat je begrijpt hoe neurale netwerken vanaf de basis werken, dus beginnen we met werken met low-level API en tensors. Als je echter snel aan de slag wilt en niet veel tijd wilt besteden aan deze details, kun je die overslaan en direct met de high-level API-notebooks aan de slag gaan.

## ✍️ Oefeningen: Frameworks

Ga verder met leren in de volgende notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch  
--------------|-----------------------------|------------------------------  
High-level API| Keras                      | *PyTorch Lightning*

Na het beheersen van de frameworks, herhalen we het begrip overfitting.

# Overfitting

Overfitting is een uiterst belangrijk concept in machine learning, en het is heel belangrijk om het goed te begrijpen!

Beschouw het volgende probleem van het benaderen van 5 punten (aangeduid met `x` in de onderstaande grafieken):

!linear | overfit  
-------------------------|--------------------------  
**Lineair model, 2 parameters** | **Niet-lineair model, 7 parameters**  
Trainingsfout = 5.3 | Trainingsfout = 0  
Validatiefout = 5.1 | Validatiefout = 20  

* Links zien we een goede rechte lijn benadering. Omdat het aantal parameters passend is, begrijpt het model de verdeling van de punten goed.
* Rechts is het model te krachtig. Omdat we slechts 5 punten hebben en het model 7 parameters, kan het zich zo aanpassen dat het door alle punten gaat, waardoor de trainingsfout 0 wordt. Dit voorkomt echter dat het model het juiste patroon achter de data begrijpt, waardoor de validatiefout erg hoog is.

Het is erg belangrijk om een goede balans te vinden tussen de complexiteit van het model (aantal parameters) en het aantal trainingsvoorbeelden.

## Waarom overfitting optreedt

  * Niet genoeg trainingsdata
  * Te krachtig model
  * Te veel ruis in de inputdata

## Hoe overfitting te detecteren

Zoals je in de grafiek hierboven ziet, kan overfitting worden gedetecteerd door een zeer lage trainingsfout en een hoge validatiefout. Normaal gesproken zien we tijdens het trainen dat zowel trainings- als validatiefouten afnemen, maar op een gegeven moment kan de validatiefout stoppen met dalen en weer gaan stijgen. Dit is een teken van overfitting en een indicatie dat we waarschijnlijk moeten stoppen met trainen op dat moment (of in ieder geval een snapshot van het model moeten maken).

overfitting

## Hoe overfitting te voorkomen

Als je ziet dat overfitting optreedt, kun je een van de volgende dingen doen:

 * Verhoog de hoeveelheid trainingsdata
 * Verminder de complexiteit van het model
 * Gebruik een regularisatietechniek, zoals Dropout, die we later zullen behandelen.

## Overfitting en Bias-Variance Tradeoff

Overfitting is eigenlijk een geval van een algemener probleem in de statistiek, genaamd Bias-Variance Tradeoff. Als we kijken naar mogelijke foutenbronnen in ons model, zien we twee soorten fouten:

* **Bias-fouten** worden veroorzaakt doordat ons algoritme de relatie tussen trainingsdata niet goed kan vastleggen. Dit kan komen doordat ons model niet krachtig genoeg is (**underfitting**).
* **Variance-fouten** worden veroorzaakt doordat het model ruis in de inputdata benadert in plaats van de betekenisvolle relatie (**overfitting**).

Tijdens het trainen neemt de bias-fout af (omdat ons model leert de data te benaderen) en neemt de variance-fout toe. Het is belangrijk om het trainen te stoppen – of handmatig (wanneer we overfitting detecteren) of automatisch (door regularisatie toe te passen) – om overfitting te voorkomen.

## Conclusie

In deze les heb je geleerd over de verschillen tussen de verschillende API’s van de twee populairste AI-frameworks, TensorFlow en PyTorch. Daarnaast heb je een heel belangrijk onderwerp behandeld: overfitting.

## 🚀 Uitdaging

In de bijbehorende notebooks vind je onderaan 'taken'; werk de notebooks door en voltooi de taken.

## Review & Zelfstudie

Doe wat onderzoek naar de volgende onderwerpen:

- TensorFlow  
- PyTorch  
- Overfitting  

Stel jezelf de volgende vragen:

- Wat is het verschil tussen TensorFlow en PyTorch?  
- Wat is het verschil tussen overfitting en underfitting?  

## Opdracht

In dit lab word je gevraagd om twee classificatieproblemen op te lossen met behulp van single- en multi-layer fully-connected netwerken met PyTorch of TensorFlow.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.