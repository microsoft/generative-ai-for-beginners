<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:47:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "da"
}
-->
# Introduktion til Neurale Netværk. Multi-Layered Perceptron

I det forrige afsnit lærte du om den simpleste model for neurale netværk – en enkeltlags perceptron, en lineær to-klasses klassifikationsmodel.

I dette afsnit udvider vi denne model til en mere fleksibel ramme, der giver os mulighed for at:

* udføre **multi-klasse klassifikation** ud over to-klasses
* løse **regressionsproblemer** ud over klassifikation
* adskille klasser, der ikke er lineært separable

Vi vil også udvikle vores eget modulære framework i Python, som gør det muligt at konstruere forskellige neurale netværksarkitekturer.

## Formalisering af Maskinlæring

Lad os starte med at formalisere maskinlæringsproblemet. Antag, at vi har et træningsdatasæt **X** med labels **Y**, og vi skal bygge en model *f*, der kan lave de mest præcise forudsigelser. Kvaliteten af forudsigelserne måles ved en **loss-funktion** ℒ. Følgende loss-funktioner bruges ofte:

* Til regressionsproblemer, hvor vi skal forudsige et tal, kan vi bruge **absolut fejl** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadreret fejl** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Til klassifikation bruger vi **0-1 loss** (som i praksis svarer til modellens **nøjagtighed**), eller **logistisk loss**.

For en enkeltlags perceptron var funktionen *f* defineret som en lineær funktion *f(x)=wx+b* (her er *w* vægtmatricen, *x* er inputfeature-vektoren, og *b* er bias-vektoren). For forskellige neurale netværksarkitekturer kan denne funktion antage en mere kompleks form.

> I tilfælde af klassifikation er det ofte ønskeligt at få sandsynligheder for de tilsvarende klasser som netværkets output. For at omdanne vilkårlige tal til sandsynligheder (f.eks. for at normalisere output) bruger vi ofte **softmax**-funktionen σ, og funktionen *f* bliver *f(x)=σ(wx+b)*

I definitionen af *f* ovenfor kaldes *w* og *b* for **parametre** θ=⟨*w,b*⟩. Givet datasættet ⟨**X**,**Y**⟩ kan vi beregne den samlede fejl på hele datasættet som en funktion af parametrene θ.

> ✅ **Målet med træning af neurale netværk er at minimere fejlen ved at variere parametrene θ**

## Gradient Descent Optimering

Der findes en velkendt metode til funktionsoptimering kaldet **gradient descent**. Ideen er, at vi kan beregne en afledt funktion (i flerdimensionelle tilfælde kaldet **gradient**) af loss-funktionen med hensyn til parametrene, og variere parametrene på en måde, så fejlen mindskes. Dette kan formaliseres som følger:

* Initialiser parametrene med nogle tilfældige værdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gentag følgende trin mange gange:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under træningen forventes optimeringstrinene at blive beregnet ud fra hele datasættet (husk at loss beregnes som summen over alle træningsprøver). I praksis tager vi dog små portioner af datasættet kaldet **minibatches**, og beregner gradienterne ud fra et delmængde af data. Fordi delmængden vælges tilfældigt hver gang, kaldes denne metode **stokastisk gradient descent** (SGD).

## Multi-Layered Perceptrons og Backpropagation

Et enkeltlags netværk, som vi har set ovenfor, kan klassificere lineært separable klasser. For at bygge en mere kompleks model kan vi kombinere flere lag i netværket. Matematisk betyder det, at funktionen *f* får en mere kompleks form og beregnes i flere trin:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **non-lineær aktiveringsfunktion**, σ er softmax-funktionen, og parametrene θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradient descent-algoritmen forbliver den samme, men det bliver sværere at beregne gradienterne. Ved hjælp af kædereglen for differentiation kan vi beregne afledte som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kædereglen bruges til at beregne afledte af loss-funktionen med hensyn til parametrene.

Bemærk, at den venstre del af alle disse udtryk er den samme, og derfor kan vi effektivt beregne afledte ved at starte fra loss-funktionen og bevæge os "baglæns" gennem beregningsgrafen. Derfor kaldes metoden til træning af et multi-lags perceptron for **backpropagation**, eller blot 'backprop'.

> TODO: billedhenvisning

> ✅ Vi vil gennemgå backprop i meget større detaljer i vores notebook-eksempel.

## Konklusion

I denne lektion har vi bygget vores eget neurale netværksbibliotek, og vi har brugt det til en simpel todimensionel klassifikationsopgave.

## 🚀 Udfordring

I den tilhørende notebook skal du implementere dit eget framework til at bygge og træne multi-lags perceptrons. Du vil kunne se i detaljer, hvordan moderne neurale netværk fungerer.

Fortsæt til OwnFramework-notebooken og arbejd dig igennem den.

## Gennemgang & Selvstudie

Backpropagation er en almindelig algoritme brugt i AI og ML, som er værd at studere nærmere.

## Opgave

I dette laboratorium skal du bruge det framework, du har konstrueret i denne lektion, til at løse MNIST håndskrevne cifre-klassifikation.

* Instruktioner
* Notebook

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.