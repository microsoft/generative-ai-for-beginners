<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:21:39+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "no"
}
-->
# Introduksjon til Nevrale Nettverk. Flerlagsperceptron

I den forrige seksjonen lærte du om den enkleste modellen for nevrale nettverk - en-lags perceptron, en lineær to-klasse klassifikasjonsmodell.

I denne seksjonen vil vi utvide denne modellen til et mer fleksibelt rammeverk, som lar oss:

* utføre **multiklasseklassifikasjon** i tillegg til to-klasse
* løse **regresjonsproblemer** i tillegg til klassifikasjon
* skille klasser som ikke er lineært separerbare

Vi vil også utvikle vårt eget modulære rammeverk i Python som vil tillate oss å konstruere forskjellige arkitekturer for nevrale nettverk.

## Formalisering av Maskinlæring

La oss starte med å formalisere maskinlæringsproblemet. Anta at vi har et treningsdatasett **X** med etiketter **Y**, og vi trenger å bygge en modell *f* som vil gi de mest nøyaktige prediksjonene. Kvaliteten på prediksjonene måles med **tapfunksjon** ℒ. Følgende tapfunksjoner brukes ofte:

* For regresjonsproblemer, når vi trenger å forutsi et tall, kan vi bruke **absolutt feil** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratisk feil** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For klassifikasjon, bruker vi **0-1 tap** (som i hovedsak er det samme som **nøyaktigheten** til modellen), eller **logistisk tap**.

For en-lags perceptron ble funksjonen *f* definert som en lineær funksjon *f(x)=wx+b* (her er *w* vektmatrisen, *x* er vektoren av inngangsfunksjoner, og *b* er bias-vektoren). For forskjellige arkitekturer for nevrale nettverk kan denne funksjonen ta en mer kompleks form.

> I tilfelle klassifikasjon er det ofte ønskelig å få sannsynligheter for de tilsvarende klassene som nettverksutgang. For å konvertere vilkårlige tall til sannsynligheter (f.eks. for å normalisere utgangen), bruker vi ofte **softmax**-funksjonen σ, og funksjonen *f* blir *f(x)=σ(wx+b)*

I definisjonen av *f* ovenfor, kalles *w* og *b* **parametere** θ=⟨*w,b*⟩. Gitt datasettet ⟨**X**,**Y**⟩, kan vi beregne en samlet feil på hele datasettet som en funksjon av parametere θ.

> ✅ **Målet med trening av nevrale nettverk er å minimere feilen ved å variere parametere θ**

## Gradientnedstigningsoptimalisering

Det finnes en velkjent metode for funksjonsoptimalisering kalt **gradientnedstigning**. Ideen er at vi kan beregne en derivert (i flerdimensjonal tilfelle kalt **gradient**) av tapfunksjonen med hensyn til parametere, og variere parametere på en slik måte at feilen vil avta. Dette kan formaliseres som følger:

* Initialiser parametere med noen tilfeldige verdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gjenta følgende steg mange ganger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under treningen skal optimaliseringsstegene beregnes med tanke på hele datasettet (husk at tap beregnes som en sum gjennom alle treningsprøver). Imidlertid, i virkeligheten tar vi små deler av datasettet kalt **minibatcher**, og beregner gradienter basert på en delmengde av data. Fordi delmengden tas tilfeldig hver gang, kalles en slik metode **stokastisk gradientnedstigning** (SGD).

## Flerlagsperceptroner og Tilbakepropagering

En-lags nettverk, som vi har sett ovenfor, er i stand til å klassifisere lineært separerbare klasser. For å bygge en rikere modell, kan vi kombinere flere lag av nettverket. Matematisk ville det bety at funksjonen *f* ville ha en mer kompleks form, og vil bli beregnet i flere trinn:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **ikke-lineær aktiveringsfunksjon**, σ er en softmax-funksjon, og parametere θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen ville forbli den samme, men det ville være vanskeligere å beregne gradienter. Gitt kjederegelen for derivasjon, kan vi beregne derivater som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kjederegelen for derivasjon brukes til å beregne derivater av tapfunksjonen med hensyn til parametere.

Merk at den venstre delen av alle disse uttrykkene er den samme, og dermed kan vi effektivt beregne derivater fra tapfunksjonen og gå "bakover" gjennom den beregningsmessige grafen. Dermed kalles metoden for å trene en flerlagsperceptron **tilbakepropagering**, eller 'backprop'.

> TODO: bildehenvisning

> ✅ Vi vil dekke tilbakepropagering mye mer detaljert i vårt notatbokeksempel.

## Konklusjon

I denne leksjonen har vi bygget vårt eget bibliotek for nevrale nettverk, og vi har brukt det til en enkel todimensjonal klassifikasjonsoppgave.

## 🚀 Utfordring

I den medfølgende notatboken vil du implementere ditt eget rammeverk for å bygge og trene flerlagsperceptroner. Du vil kunne se i detalj hvordan moderne nevrale nettverk fungerer.

Fortsett til OwnFramework-notatboken og jobb deg gjennom den.

## Gjennomgang & Selvstudium

Tilbakepropagering er en vanlig algoritme brukt i AI og ML, verdt å studere mer detaljert

## Oppgave

I dette laboratoriet blir du bedt om å bruke rammeverket du konstruerte i denne leksjonen for å løse MNIST håndskrevne sifferklassifikasjon.

* Instruksjoner
* Notatbok

**Ansvarsfraskrivelse**: 
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.