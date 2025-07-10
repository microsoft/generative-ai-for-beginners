<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:58:40+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "no"
}
-->
# Introduksjon til nevrale nettverk: Perceptron

Et av de første forsøkene på å implementere noe som ligner på et moderne nevralt nettverk ble gjort av Frank Rosenblatt ved Cornell Aeronautical Laboratory i 1957. Det var en maskinvareimplementering kalt "Mark-1", designet for å gjenkjenne primitive geometriske figurer, som trekanter, firkanter og sirkler.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Bilder fra Wikipedia

Et inngangsbilde ble representert av et 20x20 fotocelle-array, så det nevrale nettverket hadde 400 innganger og én binær utgang. Et enkelt nettverk besto av én nevron, også kalt en **threshold logic unit**. Vektene i det nevrale nettverket fungerte som potensiometre som krevde manuell justering under treningsfasen.

> ✅ Et potensiometer er en enhet som lar brukeren justere motstanden i en krets.

> The New York Times skrev om perceptron på den tiden: *embryoen til en elektronisk datamaskin som [Marinen] forventer vil kunne gå, snakke, se, skrive, reprodusere seg selv og være bevisst sin egen eksistens.*

## Perceptron-modellen

Anta at vi har N egenskaper i modellen vår, i så fall vil inngangsvektoren være en vektor av størrelse N. En perceptron er en **binær klassifiseringsmodell**, altså kan den skille mellom to klasser av inndata. Vi antar at for hver inngangsvektor x vil utgangen til perceptronen være enten +1 eller -1, avhengig av klassen. Utgangen beregnes med formelen:

y(x) = f(w<sup>T</sup>x)

hvor f er en trinnaktiveringsfunksjon

## Trening av perceptron

For å trene en perceptron må vi finne en vektor med vekter w som klassifiserer de fleste verdiene korrekt, altså gir minst mulig **feil**. Denne feilen defineres av **perceptron-kriteriet** på følgende måte:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

hvor:

* summen tas over de treningsdataene i som fører til feil klassifisering
* x<sub>i</sub> er inndata, og t<sub>i</sub> er enten -1 eller +1 for henholdsvis negative og positive eksempler.

Dette kriteriet betraktes som en funksjon av vektene w, og vi må minimere det. Ofte brukes en metode kalt **gradient descent**, hvor vi starter med noen initiale vekter w<sup>(0)</sup>, og deretter oppdaterer vektene i hvert steg etter formelen:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Her er η den såkalte **læringsraten**, og ∇E(w) betegner **gradienten** til E. Etter å ha beregnet gradienten får vi

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

I denne leksjonen lærte du om perceptron, som er en binær klassifiseringsmodell, og hvordan du kan trene den ved å bruke en vektor med vekter.

## 🚀 Utfordring

Hvis du vil prøve å bygge din egen perceptron, prøv dette laboratoriet på Microsoft Learn som bruker Azure ML designer


## Gjennomgang & Selvstudium

For å se hvordan vi kan bruke perceptron til å løse både en enkel oppgave og virkelige problemer, og for å fortsette læringen – gå til Perceptron-notatboken.

Her er også en interessant artikkel om perceptrons.

## Oppgave

I denne leksjonen har vi implementert en perceptron for en binær klassifiseringsoppgave, og vi har brukt den til å klassifisere mellom to håndskrevne sifre. I dette laboratoriet skal du løse problemet med siffersklassifisering fullstendig, altså avgjøre hvilket siffer som mest sannsynlig tilsvarer et gitt bilde.

* Instruksjoner
* Notatbok

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.