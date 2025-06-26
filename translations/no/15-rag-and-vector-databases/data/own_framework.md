<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:26:03+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "no"
}
-->
# Introduksjon til Nevrale Nettverk. Flerlagsperseptron

I forrige seksjon lærte du om den enkleste modellen for nevrale nettverk - en en-lags perseptron, en lineær to-klasses klassifiseringsmodell.

I denne seksjonen vil vi utvide denne modellen til et mer fleksibelt rammeverk, som gjør det mulig for oss å:

* utføre **flerklasses klassifisering** i tillegg til to-klasses
* løse **regresjonsproblemer** i tillegg til klassifisering
* skille klasser som ikke er lineært separerbare

Vi vil også utvikle vårt eget modulære rammeverk i Python som vil tillate oss å konstruere ulike arkitekturer for nevrale nettverk.

## Formalisering av Maskinlæring

La oss starte med å formalisere maskinlæringsproblemet. Anta at vi har et treningsdatasett **X** med etiketter **Y**, og vi trenger å bygge en modell *f* som vil gi de mest nøyaktige prediksjonene. Kvaliteten på prediksjonene måles av **tapfunksjonen** ℒ. Følgende tapfunksjoner brukes ofte:

* For regresjonsproblemer, når vi trenger å forutsi et tall, kan vi bruke **absolutt feil** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratisk feil** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For klassifisering, bruker vi **0-1 tap** (som i hovedsak er det samme som **nøyaktigheten** til modellen), eller **logistisk tap**.

For en-lags perseptron ble funksjonen *f* definert som en lineær funksjon *f(x)=wx+b* (her er *w* vektmatrisen, *x* er vektoren av inngangsfunksjoner, og *b* er bias-vektoren). For ulike arkitekturer av nevrale nettverk kan denne funksjonen ha en mer kompleks form.

> I tilfelle av klassifisering er det ofte ønskelig å få sannsynligheter for de tilsvarende klassene som nettverksutgang. For å konvertere vilkårlige tall til sannsynligheter (for eksempel for å normalisere utgangen), bruker vi ofte **softmax**-funksjonen σ, og funksjonen *f* blir *f(x)=σ(wx+b)*

I definisjonen av *f* ovenfor kalles *w* og *b* **parametere** θ=⟨*w,b*⟩. Gitt datasettet ⟨**X**,**Y**⟩, kan vi beregne en total feil på hele datasettet som en funksjon av parametrene θ.

> ✅ **Målet med trening av nevrale nettverk er å minimere feilen ved å variere parametrene θ**

## Gradientnedstigning Optimalisering

Det finnes en velkjent metode for funksjonsoptimalisering kalt **gradientnedstigning**. Ideen er at vi kan beregne en derivert (i flerdimensjonalt tilfelle kalt **gradient**) av tapfunksjonen med hensyn til parametere, og variere parametrene på en slik måte at feilen ville reduseres. Dette kan formaliseres som følger:

* Initialiser parametere med noen tilfeldige verdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gjenta følgende trinn mange ganger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under trening skal optimaliseringstrinnene beregnes med tanke på hele datasettet (husk at tapet beregnes som en sum gjennom alle treningsprøver). Men i virkeligheten tar vi små deler av datasettet kalt **minibatcher**, og beregner gradienter basert på en delmengde av data. Fordi delmengden tas tilfeldig hver gang, kalles en slik metode **stokastisk gradientnedstigning** (SGD).

## Flerlagsperseptroner og Tilbakepropagering

En-lags nettverk, som vi har sett ovenfor, er i stand til å klassifisere lineært separerbare klasser. For å bygge en rikere modell kan vi kombinere flere lag av nettverket. Matematisk vil det bety at funksjonen *f* vil ha en mer kompleks form, og vil bli beregnet i flere trinn:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **ikke-lineær aktiveringsfunksjon**, σ er en softmax-funksjon, og parametrene θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen vil forbli den samme, men det vil være mer komplisert å beregne gradienter. Gitt reglen for kjedederivasjon, kan vi beregne deriverte som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Regelen for kjedederivasjon brukes til å beregne deriverte av tapfunksjonen med hensyn til parametere.

Merk at den venstre delen av alle disse uttrykkene er den samme, og dermed kan vi effektivt beregne deriverte ved å starte fra tapfunksjonen og gå "bakover" gjennom den beregningsmessige grafen. Dermed kalles metoden for å trene et flerlagsperseptron **tilbakepropagering**, eller 'backprop'.

> TODO: bildehenvisning

> ✅ Vi vil dekke tilbakepropagering i mye mer detalj i vårt notatbokeksempel.  

## Konklusjon

I denne leksjonen har vi bygget vårt eget bibliotek for nevrale nettverk, og vi har brukt det til en enkel to-dimensjonal klassifiseringsoppgave.

## 🚀 Utfordring

I den medfølgende notatboken vil du implementere ditt eget rammeverk for å bygge og trene flerlagsperseptroner. Du vil kunne se i detalj hvordan moderne nevrale nettverk opererer.

Gå videre til OwnFramework-notatboken og arbeid deg gjennom den.

## Gjennomgang & Selvstudium

Tilbakepropagering er en vanlig algoritme brukt i AI og ML, verdt å studere i mer detalj.

## Oppgave

I dette laboratoriet blir du bedt om å bruke rammeverket du konstruerte i denne leksjonen for å løse MNIST håndskrevet sifferklassifisering.

* Instruksjoner
* Notatbok

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi streber etter nøyaktighet, men vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.