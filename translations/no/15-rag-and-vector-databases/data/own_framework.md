<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:47:48+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "no"
}
-->
# Introduksjon til nevrale nettverk. Flerlaget perceptron

I forrige seksjon lærte du om den enkleste modellen for nevrale nettverk – enlaget perceptron, en lineær to-klasses klassifiseringsmodell.

I denne seksjonen vil vi utvide denne modellen til en mer fleksibel rammeverk som lar oss:

* utføre **flere-klasse klassifisering** i tillegg til to-klasses
* løse **regresjonsproblemer** i tillegg til klassifisering
* skille klasser som ikke er lineært separerbare

Vi vil også utvikle vårt eget modulære rammeverk i Python som gjør det mulig å bygge ulike nevrale nettverksarkitekturer.

## Formalisering av maskinlæring

La oss starte med å formalisere maskinlæringsproblemet. Anta at vi har et treningsdatasett **X** med etiketter **Y**, og vi trenger å bygge en modell *f* som gir mest nøyaktige prediksjoner. Kvaliteten på prediksjonene måles med en **tapfunksjon** ℒ. Følgende tapfunksjoner brukes ofte:

* For regresjonsproblemer, når vi skal forutsi et tall, kan vi bruke **absolutt feil** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratisk feil** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For klassifisering bruker vi **0-1 tap** (som i praksis tilsvarer **modellens nøyaktighet**), eller **logistisk tap**.

For en ett-lags perceptron var funksjonen *f* definert som en lineær funksjon *f(x)=wx+b* (her er *w* vektmatrisen, *x* er vektor av input-funksjoner, og *b* er bias-vektoren). For ulike nevrale nettverksarkitekturer kan denne funksjonen ha en mer kompleks form.

> I klassifisering er det ofte ønskelig å få sannsynligheter for de respektive klassene som nettverksutgang. For å konvertere vilkårlige tall til sannsynligheter (f.eks. for å normalisere output), bruker vi ofte **softmax**-funksjonen σ, og funksjonen *f* blir *f(x)=σ(wx+b)*

I definisjonen av *f* over kalles *w* og *b* for **parametere** θ=⟨*w,b*⟩. Gitt datasettet ⟨**X**,**Y**⟩ kan vi beregne total feil på hele datasettet som en funksjon av parametrene θ.

> ✅ **Målet med trening av nevrale nettverk er å minimere feilen ved å justere parametrene θ**

## Gradientnedstigning-optimalisering

Det finnes en velkjent metode for funksjonsoptimalisering kalt **gradientnedstigning**. Ideen er at vi kan beregne en deriverte (i flerdimensjonalt tilfelle kalt **gradient**) av tapfunksjonen med hensyn til parametrene, og justere parametrene slik at feilen reduseres. Dette kan formaliseres slik:

* Initialiser parametrene med noen tilfeldige verdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gjenta følgende steg mange ganger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under trening skal optimaliseringsstegene beregnes med tanke på hele datasettet (husk at tapet beregnes som summen over alle treningsprøver). I praksis tar vi imidlertid små deler av datasettet kalt **minibatcher**, og beregner gradienter basert på et delsett av data. Fordi delsettet tas tilfeldig hver gang, kalles denne metoden **stokastisk gradientnedstigning** (SGD).

## Flerlagede perceptroner og bakoverpropagasjon

En ett-lags nettverk, som vi har sett over, kan klassifisere lineært separerbare klasser. For å bygge en rikere modell kan vi kombinere flere lag i nettverket. Matematisk betyr det at funksjonen *f* får en mer kompleks form, og beregnes i flere steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **ikke-lineær aktiveringsfunksjon**, σ er softmax-funksjonen, og parametrene θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen er den samme, men det blir vanskeligere å beregne gradientene. Ved hjelp av kjerneregelen for derivasjon kan vi beregne deriverte som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kjerneregelen brukes for å beregne deriverte av tapfunksjonen med hensyn til parametrene.

Merk at den venstre delen av alle disse uttrykkene er den samme, og derfor kan vi effektivt beregne deriverte ved å starte fra tapfunksjonen og gå "bakover" gjennom beregningsgrafen. Metoden for å trene et flerlaget perceptron kalles derfor **bakoverpropagasjon**, eller 'backprop'.



> TODO: bildehenvisning

> ✅ Vi vil gå mer i detalj på backprop i vårt notatbok-eksempel.  

## Konklusjon

I denne leksjonen har vi bygget vårt eget nevrale nettverksbibliotek, og brukt det til en enkel todimensjonal klassifiseringsoppgave.

## 🚀 Utfordring

I den medfølgende notatboken skal du implementere ditt eget rammeverk for å bygge og trene flerlagede perceptroner. Du vil kunne se i detalj hvordan moderne nevrale nettverk fungerer.

Gå videre til OwnFramework-notatboken og jobb deg gjennom den.



## Gjennomgang & Selvstudium

Bakoverpropagasjon er en vanlig algoritme brukt i AI og ML, og det er verdt å studere den nærmere.

## Oppgave

I denne labben skal du bruke rammeverket du bygde i denne leksjonen for å løse MNIST håndskriftgjenkjenningsoppgave.

* Instruksjoner
* Notatbok

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.