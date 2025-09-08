<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:32:57+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "da"
}
-->
# Neural Network Frameworks

Som vi allerede har lært, for at kunne træne neurale netværk effektivt, skal vi gøre to ting:

* At kunne arbejde med tensors, fx multiplicere, lægge sammen og beregne funktioner som sigmoid eller softmax
* At kunne beregne gradienter af alle udtryk for at udføre gradient descent optimering

Selvom `numpy`-biblioteket kan klare den første del, har vi brug for en mekanisme til at beregne gradienter. I vores framework, som vi udviklede i det foregående afsnit, måtte vi manuelt programmere alle afledte funktioner inde i `backward`-metoden, som udfører backpropagation. Ideelt set bør et framework give os mulighed for at beregne gradienter af *ethvert udtryk*, vi kan definere.

En anden vigtig ting er at kunne udføre beregninger på GPU eller andre specialiserede beregningsenheder som TPU. Træning af dybe neurale netværk kræver *mange* beregninger, og det er meget vigtigt at kunne parallelisere disse beregninger på GPU’er.

> ✅ Begrebet 'parallelisere' betyder at fordele beregningerne over flere enheder.

I øjeblikket er de to mest populære neurale frameworks: TensorFlow og PyTorch. Begge tilbyder en lavniveau-API til at arbejde med tensors på både CPU og GPU. Oven på lavniveau-API’en findes også en højere niveau API, kaldet Keras og PyTorch Lightning henholdsvis.

Low-Level API | TensorFlow| PyTorch  
--------------|-------------------------------------|--------------------------------  
High-level API| Keras| PyTorch  

**Low-level API’er** i begge frameworks giver dig mulighed for at bygge såkaldte **computational graphs**. Denne graf definerer, hvordan output (normalt tab-funktionen) beregnes ud fra givne inputparametre, og kan sendes til beregning på GPU, hvis det er tilgængeligt. Der findes funktioner til at differentiere denne computational graph og beregne gradienter, som derefter kan bruges til at optimere modelparametre.

**High-level API’er** betragter neurale netværk som en **sekvens af lag**, og gør det meget nemmere at konstruere de fleste neurale netværk. Træning af modellen kræver normalt, at data forberedes, hvorefter man kalder en `fit`-funktion for at udføre træningen.

High-level API’en gør det muligt at bygge typiske neurale netværk meget hurtigt uden at bekymre sig om mange detaljer. Samtidig giver low-level API’en langt mere kontrol over træningsprocessen, og derfor bruges den ofte i forskning, når man arbejder med nye neurale netværksarkitekturer.

Det er også vigtigt at forstå, at du kan bruge begge API’er sammen, fx kan du udvikle din egen netværkslagsarkitektur ved hjælp af low-level API’en og derefter bruge den i et større netværk, der er konstrueret og trænet med high-level API’en. Eller du kan definere et netværk med high-level API’en som en sekvens af lag og derefter bruge din egen low-level træningsløkke til at udføre optimering. Begge API’er bygger på de samme grundlæggende koncepter og er designet til at fungere godt sammen.

## Learning

I dette kursus tilbyder vi det meste af indholdet både for PyTorch og TensorFlow. Du kan vælge dit foretrukne framework og kun gennemgå de tilhørende notebooks. Hvis du er i tvivl om, hvilket framework du skal vælge, kan du læse nogle diskussioner på internettet om **PyTorch vs. TensorFlow**. Du kan også kigge på begge frameworks for at få en bedre forståelse.

Hvor det er muligt, vil vi bruge High-Level API’er for enkelhedens skyld. Vi mener dog, det er vigtigt at forstå, hvordan neurale netværk fungerer helt fra bunden, så i starten arbejder vi med low-level API og tensors. Hvis du derimod vil hurtigt i gang og ikke ønsker at bruge meget tid på at lære disse detaljer, kan du springe dem over og gå direkte til high-level API-notebooks.

## ✍️ Øvelser: Frameworks

Fortsæt din læring i følgende notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch  
--------------|-------------------------------------|--------------------------------  
High-level API| Keras | *PyTorch Lightning*

Når du har mestret frameworks, lad os opsummere begrebet overfitting.

# Overfitting

Overfitting er et ekstremt vigtigt begreb inden for maskinlæring, og det er meget vigtigt at forstå det korrekt!

Overvej følgende problem med at tilnærme 5 punkter (repræsenteret ved `x` på graferne nedenfor):

!linear | overfit  
-------------------------|--------------------------  
**Lineær model, 2 parametre** | **Ikke-lineær model, 7 parametre**  
Træningsfejl = 5.3 | Træningsfejl = 0  
Valideringsfejl = 5.1 | Valideringsfejl = 20  

* Til venstre ser vi en god lineær tilnærmelse. Fordi antallet af parametre er passende, fanger modellen den underliggende fordeling af punkterne korrekt.
* Til højre er modellen for kraftfuld. Fordi vi kun har 5 punkter, og modellen har 7 parametre, kan den tilpasse sig sådan, at den går igennem alle punkterne, hvilket giver en træningsfejl på 0. Det forhindrer dog modellen i at forstå det korrekte mønster bag dataene, og derfor er valideringsfejlen meget høj.

Det er meget vigtigt at finde den rette balance mellem modellens kompleksitet (antal parametre) og antallet af træningsprøver.

## Hvorfor overfitting opstår

  * Ikke nok træningsdata  
  * For kraftfuld model  
  * For meget støj i inputdata  

## Hvordan man opdager overfitting

Som du kan se på grafen ovenfor, kan overfitting opdages ved en meget lav træningsfejl og en høj valideringsfejl. Normalt vil både trænings- og valideringsfejl falde under træningen, men på et tidspunkt kan valideringsfejlen stoppe med at falde og begynde at stige. Det er et tegn på overfitting og en indikator for, at vi sandsynligvis bør stoppe træningen på dette tidspunkt (eller i det mindste tage et snapshot af modellen).

overfitting

## Hvordan man forhindrer overfitting

Hvis du kan se, at overfitting opstår, kan du gøre en af følgende:

 * Øge mængden af træningsdata  
 * Mindske modellens kompleksitet  
 * Bruge en form for regularisering, som Dropout, som vi vil se nærmere på senere.

## Overfitting og Bias-Variance Tradeoff

Overfitting er faktisk et tilfælde af et mere generelt problem i statistik kaldet Bias-Variance Tradeoff. Hvis vi ser på mulige fejlkilder i vores model, kan vi identificere to typer fejl:

* **Bias-fejl** skyldes, at vores algoritme ikke kan fange sammenhængen i træningsdata korrekt. Det kan skyldes, at modellen ikke er kraftfuld nok (**underfitting**).
* **Variance-fejl** skyldes, at modellen tilpasser sig støj i inputdata i stedet for meningsfulde sammenhænge (**overfitting**).

Under træningen falder bias-fejlen (efterhånden som modellen lærer at tilnærme data), mens variance-fejlen stiger. Det er vigtigt at stoppe træningen – enten manuelt (når vi opdager overfitting) eller automatisk (ved at indføre regularisering) – for at forhindre overfitting.

## Konklusion

I denne lektion har du lært om forskellene mellem de forskellige API’er i de to mest populære AI-frameworks, TensorFlow og PyTorch. Derudover har du lært om et meget vigtigt emne, overfitting.

## 🚀 Udfordring

I de tilhørende notebooks finder du 'opgaver' nederst; arbejd dig igennem notebooks og løs opgaverne.

## Review & Selvstudie

Lav lidt research om følgende emner:

- TensorFlow  
- PyTorch  
- Overfitting  

Stil dig selv følgende spørgsmål:

- Hvad er forskellen på TensorFlow og PyTorch?  
- Hvad er forskellen på overfitting og underfitting?  

## Opgave

I dette laboratorium skal du løse to klassifikationsproblemer ved hjælp af enkelt- og flerlags fuldt forbundne netværk ved brug af PyTorch eller TensorFlow.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.