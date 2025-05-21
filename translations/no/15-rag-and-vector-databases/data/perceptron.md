<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:37:44+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "no"
}
-->
# Innføring i nevrale nettverk: Perceptron

En av de første forsøkene på å implementere noe som ligner på et moderne nevralt nettverk ble gjort av Frank Rosenblatt fra Cornell Aeronautical Laboratory i 1957. Det var en maskinvareimplementasjon kalt "Mark-1", designet for å gjenkjenne primitive geometriske figurer, som trekanter, firkanter og sirkler.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Bilder fra Wikipedia

Et inngangsbilde ble representert av et 20x20 fotocelle-array, så det nevrale nettverket hadde 400 innganger og en binær utgang. Et enkelt nettverk inneholdt en nevron, også kalt en **terskel logikkenhet**. Vektene i det nevrale nettverket fungerte som potensiometre som krevde manuell justering under treningsfasen.

> ✅ Et potensiometer er en enhet som lar brukeren justere motstanden i en krets.

> The New York Times skrev om perceptron på den tiden: *embryoet til en elektronisk datamaskin som [Navy] forventer vil kunne gå, snakke, se, skrive, reprodusere seg selv og være bevisst på sin eksistens.*

## Perceptron-modell

La oss anta at vi har N funksjoner i modellen vår, i så fall vil inngangsvektoren være en vektor av størrelse N. En perceptron er en **binær klassifikasjons**modell, dvs. den kan skille mellom to klasser av inngangsdata. Vi vil anta at for hver inngangsvektor x vil utgangen av vår perceptron være enten +1 eller -1, avhengig av klassen. Utgangen vil bli beregnet ved hjelp av formelen:

y(x) = f(w<sup>T</sup>x)

hvor f er en trinnaktiveringsfunksjon

## Trening av Perceptron

For å trene en perceptron må vi finne en vektvektor w som klassifiserer de fleste verdiene riktig, dvs. resulterer i den minste **feilen**. Denne feilen er definert av **perceptronkriteriet** på følgende måte:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

hvor:

* summen tas på de treningsdatapunktene i som resulterer i feil klassifisering
* x<sub>i</sub> er inngangsdataene, og t<sub>i</sub> er enten -1 eller +1 for henholdsvis negative og positive eksempler.

Dette kriteriet betraktes som en funksjon av vektene w, og vi må minimere det. Ofte brukes en metode kalt **gradient descent**, der vi starter med noen innledende vekter w<sup>(0)</sup>, og deretter på hvert trinn oppdaterer vektene i henhold til formelen:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Her er η den såkalte **læringsraten**, og ∇E(w) betegner **gradienten** til E. Etter at vi har beregnet gradienten, ender vi opp med

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmen i Python ser slik ut:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Konklusjon

I denne leksjonen lærte du om en perceptron, som er en binær klassifikasjonsmodell, og hvordan man trener den ved å bruke en vektvektor.

## 🚀 Utfordring

Hvis du har lyst til å prøve å bygge din egen perceptron, prøv dette laboratoriet på Microsoft Learn som bruker Azure ML designer.

## Gjennomgang og selvstudie

For å se hvordan vi kan bruke perceptron til å løse et leketøyproblem så vel som virkelige problemer, og for å fortsette å lære - gå til Perceptron-notatboken.

Her er også en interessant artikkel om perceptroner.

## Oppgave

I denne leksjonen har vi implementert en perceptron for en binær klassifikasjonsoppgave, og vi har brukt den til å klassifisere mellom to håndskrevne sifre. I dette laboratoriet blir du bedt om å løse problemet med sifferklassifisering helt, dvs. bestemme hvilket siffer som mest sannsynlig tilsvarer et gitt bilde.

* Instruksjoner
* Notatbok

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.