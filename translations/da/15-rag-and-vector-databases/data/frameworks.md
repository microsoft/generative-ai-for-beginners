<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:04:40+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "da"
}
-->
# Neurale Netværksrammer

Som vi allerede har lært, skal vi kunne gøre to ting for at kunne træne neurale netværk effektivt:

* At operere på tensorer, fx at multiplicere, lægge til og beregne nogle funktioner såsom sigmoid eller softmax
* At beregne gradienter af alle udtryk for at udføre gradient descent-optimering

Mens biblioteket `numpy` kan klare den første del, har vi brug for en mekanisme til at beregne gradienter. I vores ramme, som vi har udviklet i det forrige afsnit, var vi nødt til manuelt at programmere alle afledede funktioner inde i metoden `backward`, som udfører backpropagation. Ideelt set bør en ramme give os mulighed for at beregne gradienter af *ethvert udtryk*, som vi kan definere.

En anden vigtig ting er at kunne udføre beregninger på GPU eller andre specialiserede beregningsenheder som TPU. Træning af dybe neurale netværk kræver *mange* beregninger, og det er meget vigtigt at kunne parallelisere disse beregninger på GPU'er.

> ✅ Udtrykket 'parallelisere' betyder at distribuere beregningerne over flere enheder.

I øjeblikket er de to mest populære neurale rammer: TensorFlow og PyTorch. Begge tilbyder et lav-niveau API til at operere med tensorer på både CPU og GPU. Oven på lav-niveau API'en er der også en høj-niveau API, kaldet henholdsvis Keras og PyTorch Lightning.

Lav-niveau API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Høj-niveau API| Keras| Pytorch

**Lav-niveau API'er** i begge rammer giver dig mulighed for at bygge såkaldte **beregningsgrafer**. Denne graf definerer, hvordan man beregner output (normalt tab-funktionen) med givne inputparametre og kan skubbes til beregning på GPU, hvis den er tilgængelig. Der er funktioner til at differentiere denne beregningsgraf og beregne gradienter, som derefter kan bruges til at optimere modelparametre.

**Høj-niveau API'er** betragter stort set neurale netværk som en **sekvens af lag**, og gør konstruktionen af de fleste neurale netværk meget lettere. Træning af modellen kræver normalt forberedelse af dataene og derefter at kalde en `fit` funktion for at udføre arbejdet.

Høj-niveau API'en giver dig mulighed for hurtigt at konstruere typiske neurale netværk uden at bekymre dig om mange detaljer. Samtidig tilbyder lav-niveau API'en meget mere kontrol over træningsprocessen, og derfor bruges de meget i forskning, når man arbejder med nye neurale netværksarkitekturer.

Det er også vigtigt at forstå, at du kan bruge begge API'er sammen, fx kan du udvikle din egen netværkslagsarkitektur ved hjælp af lav-niveau API'en og derefter bruge den inde i det større netværk konstrueret og trænet med høj-niveau API'en. Eller du kan definere et netværk ved hjælp af høj-niveau API'en som en sekvens af lag og derefter bruge din egen lav-niveau træningssløjfe til at udføre optimering. Begge API'er bruger de samme grundlæggende underliggende koncepter, og de er designet til at fungere godt sammen.

## Læring

I denne kursus tilbyder vi det meste af indholdet både for PyTorch og TensorFlow. Du kan vælge din foretrukne ramme og kun gennemgå de tilsvarende notebooks. Hvis du ikke er sikker på, hvilken ramme du skal vælge, kan du læse nogle diskussioner på internettet om **PyTorch vs. TensorFlow**. Du kan også kigge på begge rammer for at få en bedre forståelse.

Hvor det er muligt, vil vi bruge høj-niveau API'er for enkelhedens skyld. Vi mener dog, at det er vigtigt at forstå, hvordan neurale netværk fungerer fra bunden, så i starten begynder vi med at arbejde med lav-niveau API og tensorer. Men hvis du vil komme hurtigt i gang og ikke ønsker at bruge meget tid på at lære disse detaljer, kan du springe dem over og gå direkte til høj-niveau API notebooks.

## ✍️ Øvelser: Rammer

Fortsæt din læring i de følgende notebooks:

Lav-niveau API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
Høj-niveau API| Keras | *PyTorch Lightning*

Efter at have mestret rammerne, lad os genopfriske begrebet overfitting.

# Overfitting

Overfitting er et ekstremt vigtigt koncept i maskinlæring, og det er meget vigtigt at få det rigtigt!

Overvej det følgende problem med at tilnærme 5 punkter (repræsenteret ved `x` på graferne nedenfor):

!linear | overfit
-------------------------|--------------------------
**Lineær model, 2 parametre** | **Ikke-lineær model, 7 parametre**
Træningsfejl = 5.3 | Træningsfejl = 0
Validationsfejl = 5.1 | Validationsfejl = 20

* Til venstre ser vi en god lige linje tilnærmelse. Fordi antallet af parametre er passende, får modellen idéen bag punktfordelingen korrekt.
* Til højre er modellen for kraftfuld. Fordi vi kun har 5 punkter, og modellen har 7 parametre, kan den justere sig på en sådan måde, at den passerer gennem alle punkter, hvilket gør træningsfejlen til 0. Dette forhindrer dog modellen i at forstå det korrekte mønster bag dataene, hvilket gør validationsfejlen meget høj.

Det er meget vigtigt at finde en korrekt balance mellem modellens rigdom (antal parametre) og antallet af træningsprøver.

## Hvorfor overfitting opstår

  * Ikke nok træningsdata
  * For kraftfuld model
  * For meget støj i inputdata

## Hvordan man opdager overfitting

Som du kan se fra grafen ovenfor, kan overfitting opdages ved en meget lav træningsfejl og en høj validationsfejl. Normalt under træning vil vi se både trænings- og validationsfejl begynde at falde, og så på et tidspunkt kan validationsfejlen stoppe med at falde og begynde at stige. Dette vil være et tegn på overfitting og en indikator for, at vi sandsynligvis bør stoppe træningen på dette tidspunkt (eller i det mindste tage et snapshot af modellen).

## Hvordan man forhindrer overfitting

Hvis du kan se, at overfitting opstår, kan du gøre en af følgende:

 * Øge mængden af træningsdata
 * Mindske modellens kompleksitet
 * Bruge en form for regulariseringsteknik, såsom Dropout, som vi vil overveje senere.

## Overfitting og Bias-Variance Tradeoff

Overfitting er faktisk et tilfælde af et mere generisk problem i statistik kaldet Bias-Variance Tradeoff. Hvis vi overvejer de mulige kilder til fejl i vores model, kan vi se to typer fejl:

* **Bias-fejl** er forårsaget af, at vores algoritme ikke er i stand til at fange forholdet mellem træningsdataene korrekt. Det kan skyldes, at vores model ikke er kraftfuld nok (**underfitting**).
* **Variansfejl**, som er forårsaget af, at modellen tilnærmer støj i inputdataene i stedet for et meningsfuldt forhold (**overfitting**).

Under træning falder bias-fejlen (da vores model lærer at tilnærme dataene), og variansfejlen stiger. Det er vigtigt at stoppe træningen - enten manuelt (når vi opdager overfitting) eller automatisk (ved at indføre regularisering) - for at forhindre overfitting.

## Konklusion

I denne lektion lærte du om forskellene mellem de forskellige API'er for de to mest populære AI-rammer, TensorFlow og PyTorch. Derudover lærte du om et meget vigtigt emne, overfitting.

## 🚀 Udfordring

I de medfølgende notebooks finder du 'opgaver' nederst; arbejd dig igennem notebooks og fuldfør opgaverne.

## Gennemgang & Selvstudie

Lav noget research om følgende emner:

- TensorFlow
- PyTorch
- Overfitting

Spørg dig selv følgende spørgsmål:

- Hvad er forskellen mellem TensorFlow og PyTorch?
- Hvad er forskellen mellem overfitting og underfitting?

## Opgave

I dette laboratorium bliver du bedt om at løse to klassifikationsproblemer ved hjælp af enkelt- og multilags fuldt forbundne netværk ved hjælp af PyTorch eller TensorFlow.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.