<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:25:41+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "da"
}
-->
# Introduktion til Neurale Netværk. Flerlaget Perceptron

I det forrige afsnit lærte du om den simpleste neurale netværksmodel - enlaget perceptron, en lineær to-klasse klassifikationsmodel.

I dette afsnit vil vi udvide denne model til en mere fleksibel ramme, der giver os mulighed for at:

* udføre **multiklasse klassifikation** udover to-klasse
* løse **regressionsproblemer** udover klassifikation
* adskille klasser, der ikke er lineært adskillelige

Vi vil også udvikle vores egen modulære ramme i Python, der gør det muligt for os at konstruere forskellige neurale netværksarkitekturer.

## Formalisering af Maskinlæring

Lad os starte med at formalisere maskinlæringsproblemet. Antag, at vi har et træningsdatasæt **X** med etiketter **Y**, og vi skal bygge en model *f*, der vil lave de mest præcise forudsigelser. Kvaliteten af forudsigelserne måles ved **Tabsfunktion** ℒ. Følgende tabsfunktioner bruges ofte:

* For regressionsproblemer, når vi skal forudsige et tal, kan vi bruge **absolut fejl** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadreret fejl** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For klassifikation bruger vi **0-1 tab** (som i det væsentlige er det samme som **nøjagtigheden** af modellen), eller **logistisk tab**.

For enlaget perceptron blev funktionen *f* defineret som en lineær funktion *f(x)=wx+b* (her er *w* vægtmatricen, *x* er vektoren af inputfunktioner, og *b* er biasvektoren). For forskellige neurale netværksarkitekturer kan denne funktion antage en mere kompleks form.

> I tilfældet med klassifikation er det ofte ønskværdigt at få sandsynligheder for de tilsvarende klasser som netværksoutput. For at konvertere vilkårlige tal til sandsynligheder (f.eks. for at normalisere outputtet), bruger vi ofte **softmax** funktionen σ, og funktionen *f* bliver *f(x)=σ(wx+b)*

I definitionen af *f* ovenfor kaldes *w* og *b* **parametre** θ=⟨*w,b*⟩. Givet datasættet ⟨**X**,**Y**⟩ kan vi beregne en samlet fejl på hele datasættet som en funktion af parametrene θ.

> ✅ **Målet med træning af neurale netværk er at minimere fejlen ved at variere parametrene θ**

## Gradient Descent Optimering

Der er en velkendt metode til funktionsoptimering kaldet **gradient descent**. Ideen er, at vi kan beregne en afledet (i flerdimensionelt tilfælde kaldet **gradient**) af tabsfunktionen med hensyn til parametrene, og variere parametrene på en sådan måde, at fejlen ville falde. Dette kan formaliseres som følger:

* Initialiser parametrene med nogle tilfældige værdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gentag følgende trin mange gange:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under træning skal optimeringstrinene beregnes med hensyn til hele datasættet (husk, at tabet beregnes som en sum gennem alle træningsprøver). Men i virkeligheden tager vi små dele af datasættet kaldet **minibatches**, og beregner gradienter baseret på en delmængde af data. Fordi delmængden tages tilfældigt hver gang, kaldes en sådan metode **stokastisk gradient descent** (SGD).

## Flerlaget Perceptrons og Backpropagation

Et enlaget netværk, som vi har set ovenfor, er i stand til at klassificere lineært adskillelige klasser. For at bygge en rigere model kan vi kombinere flere lag af netværket. Matematisk ville det betyde, at funktionen *f* ville have en mere kompleks form og vil blive beregnet i flere trin:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **ikke-lineær aktiveringsfunktion**, σ er en softmax funktion, og parametrene θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradient descent algoritmen ville forblive den samme, men det ville være mere vanskeligt at beregne gradienter. Givet kæderegel for differentiering kan vi beregne afledte som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kæderegel for differentiering bruges til at beregne afledte af tabsfunktionen med hensyn til parametrene.

Bemærk, at den venstre del af alle disse udtryk er den samme, og derfor kan vi effektivt beregne afledte startende fra tabsfunktionen og gå "baglæns" gennem den beregningsmæssige graf. Således kaldes metoden til træning af et flerlaget perceptron **backpropagation**, eller 'backprop'.

> TODO: billedkilde

> ✅ Vi vil dække backprop i meget mere detaljer i vores notesbogseksempel.  

## Konklusion

I denne lektion har vi bygget vores eget neurale netværksbibliotek, og vi har brugt det til en simpel todimensional klassifikationsopgave.

## 🚀 Udfordring

I den medfølgende notesbog vil du implementere din egen ramme til at bygge og træne flerlaget perceptrons. Du vil kunne se i detaljer, hvordan moderne neurale netværk fungerer.

Gå videre til OwnFramework notesbogen og arbejd igennem den.

## Gennemgang & Selvstudie

Backpropagation er en almindelig algoritme brugt i AI og ML, værd at studere i mere detaljeret.

## Opgave

I dette laboratorium bliver du bedt om at bruge den ramme, du konstruerede i denne lektion, til at løse MNIST håndskrevet cifre klassifikation.

* Instruktioner
* Notesbog

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.