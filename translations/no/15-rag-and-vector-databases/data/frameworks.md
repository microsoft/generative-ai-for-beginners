<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:05:06+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "no"
}
-->
# Nevrale nettverksrammeverk

Som vi allerede har lært, for å kunne trene nevrale nettverk effektivt, må vi gjøre to ting:

* Operere på tensorer, for eksempel multiplisere, legge til og beregne noen funksjoner som sigmoid eller softmax
* Beregne gradienter av alle uttrykk, for å utføre gradient descent-optimalisering

Mens `numpy`-biblioteket kan gjøre den første delen, trenger vi en mekanisme for å beregne gradienter. I rammeverket vårt som vi har utviklet i forrige seksjon, måtte vi manuelt programmere alle deriverte funksjoner inne i `backward`-metoden, som utfører bakoverpropagasjon. Ideelt sett bør et rammeverk gi oss muligheten til å beregne gradienter av *ethvert uttrykk* som vi kan definere.

En annen viktig ting er å kunne utføre beregninger på GPU, eller andre spesialiserte beregningsenheter, som TPU. Dyp læring av nevrale nettverk krever *mange* beregninger, og det er veldig viktig å kunne parallellisere disse beregningene på GPU-er.

> ✅ Begrepet 'parallellisere' betyr å distribuere beregningene over flere enheter.

For tiden er de to mest populære nevrale rammeverkene: TensorFlow og PyTorch. Begge gir et lavnivå-API for å operere med tensorer på både CPU og GPU. På toppen av lavnivå-API-en finnes det også høyere nivå-API-er, kalt henholdsvis Keras og PyTorch Lightning.

Lav-nivå API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Høy-nivå API | Keras| Pytorch

**Lav-nivå API-er** i begge rammeverkene lar deg bygge såkalte **beregningsgrafer**. Denne grafen definerer hvordan man beregner utgangen (vanligvis tapfunksjonen) med gitte inngangsparametere, og kan skyves for beregning på GPU, hvis den er tilgjengelig. Det finnes funksjoner for å differensiere denne beregningsgrafen og beregne gradienter, som deretter kan brukes til å optimalisere modellparametere.

**Høy-nivå API-er** betrakter stort sett nevrale nettverk som en **sekvens av lag**, og gjør konstruksjonen av de fleste nevrale nettverk mye enklere. Å trene modellen krever vanligvis å forberede dataene og deretter kalle en `fit`-funksjon for å utføre jobben.

Høy-nivå API-en lar deg konstruere typiske nevrale nettverk veldig raskt uten å bekymre deg for mange detaljer. Samtidig gir lav-nivå API mye mer kontroll over treningsprosessen, og derfor brukes de mye i forskning, når man jobber med nye arkitekturer for nevrale nettverk.

Det er også viktig å forstå at du kan bruke begge API-ene sammen, for eksempel kan du utvikle din egen nettverkslagsarkitektur ved hjelp av lav-nivå API, og deretter bruke den i det større nettverket konstruert og trent med høy-nivå API. Eller du kan definere et nettverk ved hjelp av høy-nivå API som en sekvens av lag, og deretter bruke din egen lav-nivå treningssløyfe for å utføre optimalisering. Begge API-ene bruker de samme grunnleggende underliggende konseptene, og de er designet for å fungere godt sammen.

## Læring

I dette kurset tilbyr vi det meste av innholdet både for PyTorch og TensorFlow. Du kan velge ditt foretrukne rammeverk og bare gå gjennom de tilsvarende notatbøkene. Hvis du ikke er sikker på hvilket rammeverk du skal velge, les noen diskusjoner på internett om **PyTorch vs. TensorFlow**. Du kan også se på begge rammeverkene for å få en bedre forståelse.

Der det er mulig, vil vi bruke høy-nivå API-er for enkelhetens skyld. Imidlertid mener vi det er viktig å forstå hvordan nevrale nettverk fungerer fra bunnen av, derfor starter vi i begynnelsen med å jobbe med lav-nivå API og tensorer. Men hvis du vil komme i gang raskt og ikke vil bruke mye tid på å lære disse detaljene, kan du hoppe over dem og gå rett til høy-nivå API-notatbøker.

## ✍️ Øvelser: Rammeverk

Fortsett læringen din i følgende notatbøker:

Lav-nivå API | TensorFlow+Keras Notatbok | PyTorch
--------------|-------------------------------------|--------------------------------
Høy-nivå API | Keras | *PyTorch Lightning*

Etter å ha mestret rammeverkene, la oss oppsummere begrepet overtilpasning.

# Overtilpasning

Overtilpasning er et ekstremt viktig konsept i maskinlæring, og det er veldig viktig å få det riktig!

Vurder følgende problem med å tilnærme 5 punkter (representert ved `x` på grafene nedenfor):

!linear | overfit
-------------------------|--------------------------
**Lineær modell, 2 parametere** | **Ikke-lineær modell, 7 parametere**
Treningsfeil = 5.3 | Treningsfeil = 0
Valideringsfeil = 5.1 | Valideringsfeil = 20

* Til venstre ser vi en god rett linje-tilnærming. Fordi antall parametere er tilstrekkelig, forstår modellen ideen bak punktfordelingen riktig.
* Til høyre er modellen for kraftig. Fordi vi bare har 5 punkter og modellen har 7 parametere, kan den justere seg på en slik måte at den går gjennom alle punktene, noe som gjør treningsfeilen til å være 0. Dette forhindrer imidlertid modellen i å forstå det riktige mønsteret bak dataene, og dermed er valideringsfeilen veldig høy.

Det er veldig viktig å finne en riktig balanse mellom modellens rikdom (antall parametere) og antall treningsprøver.

## Hvorfor overtilpasning oppstår

  * Ikke nok treningsdata
  * For kraftig modell
  * For mye støy i inngangsdataene

## Hvordan oppdage overtilpasning

Som du kan se fra grafen ovenfor, kan overtilpasning oppdages ved en veldig lav treningsfeil og en høy valideringsfeil. Normalt under trening vil vi se både trenings- og valideringsfeil begynne å avta, og deretter på et tidspunkt kan valideringsfeilen slutte å avta og begynne å stige. Dette vil være et tegn på overtilpasning, og indikatoren for at vi sannsynligvis bør stoppe treningen på dette tidspunktet (eller i det minste ta et øyeblikksbilde av modellen).

overtilpasning

## Hvordan forhindre overtilpasning

Hvis du ser at overtilpasning oppstår, kan du gjøre en av følgende:

 * Øk mengden treningsdata
 * Reduser modellens kompleksitet
 * Bruk en eller annen regulariseringsteknikk, som Dropout, som vi vil vurdere senere.

## Overtilpasning og Bias-Variance Tradeoff

Overtilpasning er faktisk et tilfelle av et mer generisk problem i statistikk kalt Bias-Variance Tradeoff. Hvis vi vurderer de mulige kildene til feil i modellen vår, kan vi se to typer feil:

* **Bias-feil** er forårsaket av at algoritmen vår ikke klarer å fange forholdet mellom treningsdataene riktig. Det kan skyldes at modellen vår ikke er kraftig nok (**undertilpasning**).
* **Variansfeil**, som er forårsaket av at modellen tilnærmer seg støy i inngangsdataene i stedet for meningsfulle forhold (**overtillpasning**).

Under trening avtar bias-feilen (ettersom modellen vår lærer å tilnærme dataene), og variansfeilen øker. Det er viktig å stoppe treningen - enten manuelt (når vi oppdager overtilpasning) eller automatisk (ved å innføre regularisering) - for å forhindre overtilpasning.

## Konklusjon

I denne leksjonen lærte du om forskjellene mellom de ulike API-ene for de to mest populære AI-rammeverkene, TensorFlow og PyTorch. I tillegg lærte du om et veldig viktig emne, overtilpasning.

## 🚀 Utfordring

I de medfølgende notatbøkene finner du 'oppgaver' nederst; arbeid deg gjennom notatbøkene og fullfør oppgavene.

## Gjennomgang & Selvstudie

Gjør litt research på følgende emner:

- TensorFlow
- PyTorch
- Overtilpasning

Still deg selv følgende spørsmål:

- Hva er forskjellen mellom TensorFlow og PyTorch?
- Hva er forskjellen mellom overtilpasning og undertilpasning?

## Oppgave

I dette laboratoriet blir du bedt om å løse to klassifiseringsproblemer ved å bruke enkelt- og flerlags fullt tilkoblede nettverk ved å bruke PyTorch eller TensorFlow.

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi etterstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.