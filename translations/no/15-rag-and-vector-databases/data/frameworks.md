<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:33:14+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "no"
}
-->
# Nevrale nettverksrammeverk

Som vi allerede har lært, for å kunne trene nevrale nettverk effektivt må vi gjøre to ting:

* Å operere på tensorer, f.eks. å multiplisere, legge til, og beregne noen funksjoner som sigmoid eller softmax
* Å beregne gradienter av alle uttrykk, for å kunne utføre gradientnedstigningsoptimalisering

Mens `numpy`-biblioteket kan gjøre den første delen, trenger vi en mekanisme for å beregne gradienter. I rammeverket vi utviklet i forrige seksjon måtte vi programmere alle deriverte funksjoner manuelt inne i `backward`-metoden, som utfører backpropagation. Ideelt sett bør et rammeverk gi oss muligheten til å beregne gradienter av *hvilket som helst uttrykk* vi kan definere.

En annen viktig ting er å kunne utføre beregninger på GPU, eller andre spesialiserte beregningsenheter, som TPU. Dyp nevralt nettverkstrening krever *mye* beregninger, og det er svært viktig å kunne parallellisere disse beregningene på GPUer.

> ✅ Begrepet 'parallellisere' betyr å fordele beregningene over flere enheter.

For øyeblikket er de to mest populære nevrale rammeverkene: TensorFlow og PyTorch. Begge tilbyr et lavnivå-API for å operere med tensorer på både CPU og GPU. I tillegg til lavnivå-API finnes det også høyere nivå API, kalt Keras og PyTorch Lightning henholdsvis.

Lavnivå-API | TensorFlow | PyTorch  
------------|-------------------------------|-----------------------------  
Høynivå-API | Keras | PyTorch

**Lavnivå-APIer** i begge rammeverkene lar deg bygge såkalte **beregningsgrafer**. Denne grafen definerer hvordan man beregner output (vanligvis tapsfunksjonen) med gitte inputparametere, og kan kjøres på GPU hvis det er tilgjengelig. Det finnes funksjoner for å differensiere denne beregningsgrafen og beregne gradienter, som deretter kan brukes til å optimalisere modellparametere.

**Høynivå-APIer** ser på nevrale nettverk som en **sekvens av lag**, og gjør det mye enklere å bygge de fleste nevrale nettverk. Trening av modellen krever vanligvis å forberede dataene og deretter kalle en `fit`-funksjon for å utføre treningen.

Høynivå-API lar deg raskt bygge typiske nevrale nettverk uten å bekymre deg for mange detaljer. Samtidig gir lavnivå-API mye mer kontroll over treningsprosessen, og brukes derfor mye i forskning når man jobber med nye nevrale nettverksarkitekturer.

Det er også viktig å forstå at du kan bruke begge APIene sammen, f.eks. kan du utvikle din egen nettverkslagarkitektur med lavnivå-API, og deretter bruke den i et større nettverk bygget og trent med høynivå-API. Eller du kan definere et nettverk med høynivå-API som en sekvens av lag, og deretter bruke din egen lavnivå treningssløyfe for å utføre optimalisering. Begge APIene bruker de samme grunnleggende konseptene, og er designet for å fungere godt sammen.

## Læring

I dette kurset tilbyr vi mesteparten av innholdet både for PyTorch og TensorFlow. Du kan velge ditt foretrukne rammeverk og kun gå gjennom de tilhørende notatbøkene. Hvis du er usikker på hvilket rammeverk du skal velge, kan du lese noen diskusjoner på internett om **PyTorch vs. TensorFlow**. Du kan også se på begge rammeverkene for å få bedre forståelse.

Der det er mulig, vil vi bruke høynivå-API for enkelhets skyld. Vi mener imidlertid det er viktig å forstå hvordan nevrale nettverk fungerer helt fra bunnen av, så i starten jobber vi med lavnivå-API og tensorer. Men hvis du vil komme raskt i gang og ikke ønsker å bruke mye tid på å lære disse detaljene, kan du hoppe over dem og gå rett til høynivå-API-notatbøkene.

## ✍️ Øvelser: Rammeverk

Fortsett læringen i følgende notatbøker:

Lavnivå-API | TensorFlow+Keras Notebook | PyTorch  
------------|-------------------------------|-----------------------------  
Høynivå-API | Keras | *PyTorch Lightning*

Etter å ha mestret rammeverkene, la oss oppsummere begrepet overtilpasning.

# Overtilpasning

Overtilpasning er et ekstremt viktig konsept innen maskinlæring, og det er veldig viktig å få det riktig!

Se for deg følgende problem med å tilnærme 5 punkter (representert med `x` på grafene under):

!linear | overfit  
-------------------------|--------------------------  
**Lineær modell, 2 parametere** | **Ikke-lineær modell, 7 parametere**  
Treningsfeil = 5.3 | Treningsfeil = 0  
Valideringsfeil = 5.1 | Valideringsfeil = 20

* Til venstre ser vi en god rett linje-tilnærming. Fordi antallet parametere er passende, fanger modellen opp fordelingen av punktene riktig.
* Til høyre er modellen for kraftig. Fordi vi bare har 5 punkter og modellen har 7 parametere, kan den justere seg slik at den går gjennom alle punktene, og treningsfeilen blir 0. Dette hindrer modellen i å forstå det riktige mønsteret bak dataene, og valideringsfeilen blir derfor veldig høy.

Det er svært viktig å finne en riktig balanse mellom modellens kompleksitet (antall parametere) og antall treningsprøver.

## Hvorfor overtilpasning oppstår

  * Ikke nok treningsdata
  * For kraftig modell
  * For mye støy i inputdata

## Hvordan oppdage overtilpasning

Som du kan se fra grafen over, kan overtilpasning oppdages ved veldig lav treningsfeil og høy valideringsfeil. Vanligvis under trening vil både trenings- og valideringsfeil begynne å synke, men på et tidspunkt kan valideringsfeilen slutte å synke og begynne å øke. Dette er et tegn på overtilpasning, og en indikasjon på at vi sannsynligvis bør stoppe treningen på dette tidspunktet (eller i det minste ta et øyeblikksbilde av modellen).

overfitting

## Hvordan forhindre overtilpasning

Hvis du ser at overtilpasning oppstår, kan du gjøre en av følgende:

 * Øke mengden treningsdata
 * Redusere modellens kompleksitet
 * Bruke en form for regularisering, som Dropout, som vi vil se nærmere på senere.

## Overtilpasning og Bias-Variance Tradeoff

Overtilpasning er egentlig et tilfelle av et mer generelt problem i statistikk kalt Bias-Variance Tradeoff. Hvis vi ser på mulige feilkilder i modellen vår, kan vi skille to typer feil:

* **Bias-feil** skyldes at algoritmen vår ikke klarer å fange forholdet i treningsdataene riktig. Dette kan komme av at modellen ikke er kraftig nok (**undertilpasning**).
* **Variansfeil** skyldes at modellen tilpasser seg støy i inputdataene i stedet for meningsfulle sammenhenger (**overtilpasning**).

Under trening minker bias-feilen (etter hvert som modellen lærer å tilnærme dataene), mens variansfeilen øker. Det er viktig å stoppe treningen – enten manuelt (når vi oppdager overtilpasning) eller automatisk (ved å innføre regularisering) – for å forhindre overtilpasning.

## Konklusjon

I denne leksjonen har du lært om forskjellene mellom de ulike APIene for de to mest populære AI-rammeverkene, TensorFlow og PyTorch. I tillegg har du lært om et svært viktig tema, overtilpasning.

## 🚀 Utfordring

I de medfølgende notatbøkene finner du 'oppgaver' nederst; jobb deg gjennom notatbøkene og fullfør oppgavene.

## Gjennomgang & Selvstudium

Gjør litt research på følgende temaer:

- TensorFlow  
- PyTorch  
- Overtilpasning

Still deg selv følgende spørsmål:

- Hva er forskjellen mellom TensorFlow og PyTorch?  
- Hva er forskjellen mellom overtilpasning og undertilpasning?

## Oppgave

I dette laboratoriet skal du løse to klassifiseringsproblemer ved hjelp av enkelt- og flerlags fulltilkoblede nettverk ved bruk av PyTorch eller TensorFlow.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.