<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:00:54+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "no"
}
-->
# Nevrale nettverksrammeverk

Som vi allerede har lært, for å kunne trene nevrale nettverk effektivt, må vi gjøre to ting:

* Operere på tensorer, for eksempel å multiplisere, legge til, og beregne noen funksjoner som sigmoid eller softmax
* Beregne gradienter av alle uttrykk, for å utføre gradientdescent-optimalisering

Mens `numpy`-biblioteket kan gjøre den første delen, trenger vi en mekanisme for å beregne gradienter. I vårt rammeverk som vi har utviklet i forrige seksjon, måtte vi manuelt programmere alle deriverte funksjoner inne i `backward`-metoden, som utfører backpropagation. Ideelt sett bør et rammeverk gi oss muligheten til å beregne gradienter av *ethvert uttrykk* som vi kan definere.

En annen viktig ting er å kunne utføre beregninger på GPU, eller andre spesialiserte beregningsenheter, som TPU. Trening av dype nevrale nettverk krever *mye* beregninger, og det er veldig viktig å kunne parallellisere disse beregningene på GPUer.

> ✅ Begrepet 'parallellisere' betyr å fordele beregningene over flere enheter.

For tiden er de to mest populære nevrale rammeverkene: TensorFlow og PyTorch. Begge gir et lavnivå-API for å operere med tensorer på både CPU og GPU. På toppen av lavnivå-APIet er det også et høyere nivå API, kalt henholdsvis Keras og PyTorch Lightning.

Lavnivå-API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Høynivå-API| Keras| Pytorch

**Lavnivå-APIer** i begge rammeverkene lar deg bygge såkalte **beregningsgrafer**. Denne grafen definerer hvordan man beregner utgangen (vanligvis tapsfunksjonen) med gitte inngangsparametere, og kan skyves for beregning på GPU, hvis den er tilgjengelig. Det finnes funksjoner for å differensiere denne beregningsgrafen og beregne gradienter, som deretter kan brukes til å optimalisere modellparametere.

**Høynivå-APIer** betrakter stort sett nevrale nettverk som en **sekvens av lag**, og gjør konstruksjonen av de fleste nevrale nettverk mye enklere. Å trene modellen krever vanligvis å forberede dataene og deretter kalle en `fit`-funksjon for å gjøre jobben.

Høynivå-APIet lar deg konstruere typiske nevrale nettverk veldig raskt uten å bekymre deg for mange detaljer. Samtidig tilbyr lavnivå-APIet mye mer kontroll over treningsprosessen, og derfor brukes de mye i forskning, når du jobber med nye nevrale nettverksarkitekturer.

Det er også viktig å forstå at du kan bruke begge APIene sammen, for eksempel kan du utvikle din egen nettverkslagsarkitektur ved hjelp av lavnivå-APIet, og deretter bruke den inne i det større nettverket konstruert og trent med høynivå-APIet. Eller du kan definere et nettverk ved hjelp av høynivå-APIet som en sekvens av lag, og deretter bruke din egen lavnivå treningssløyfe for å utføre optimalisering. Begge APIene bruker de samme grunnleggende underliggende konseptene, og de er designet for å fungere godt sammen.

## Læring

I dette kurset tilbyr vi det meste av innholdet både for PyTorch og TensorFlow. Du kan velge ditt foretrukne rammeverk og bare gå gjennom de tilsvarende notatbøkene. Hvis du ikke er sikker på hvilket rammeverk du skal velge, les noen diskusjoner på internett angående **PyTorch vs. TensorFlow**. Du kan også se på begge rammeverkene for å få en bedre forståelse.

Der det er mulig, vil vi bruke høynivå-APIer for enkelhets skyld. Imidlertid tror vi det er viktig å forstå hvordan nevrale nettverk fungerer fra grunnen av, derfor begynner vi med å jobbe med lavnivå-APIet og tensorer. Men hvis du vil komme i gang raskt og ikke ønsker å bruke mye tid på å lære disse detaljene, kan du hoppe over disse og gå rett inn i notatbøkene for høynivå-APIet.

## ✍️ Øvelser: Rammeverk

Fortsett læringen i følgende notatbøker:

Lavnivå-API | TensorFlow+Keras Notatbok | PyTorch
--------------|-------------------------------------|--------------------------------
Høynivå-API| Keras | *PyTorch Lightning*

Etter å ha mestret rammeverkene, la oss oppsummere begrepet overtilpasning.

# Overtilpasning

Overtilpasning er et ekstremt viktig konsept innen maskinlæring, og det er veldig viktig å få det riktig!

Tenk på følgende problem med å tilnærme 5 punkter (representert av `x` på grafene nedenfor):

!lineær | overtilpasning
-------------------------|--------------------------
**Lineær modell, 2 parametere** | **Ikke-lineær modell, 7 parametere**
Treningsfeil = 5.3 | Treningsfeil = 0
Valideringsfeil = 5.1 | Valideringsfeil = 20

* Til venstre ser vi en god rett linje tilnærming. Fordi antall parametere er tilstrekkelig, får modellen ideen bak punktfordelingen riktig.
* Til høyre er modellen for kraftig. Fordi vi bare har 5 punkter og modellen har 7 parametere, kan den justere seg slik at den passerer gjennom alle punktene, noe som gjør at treningsfeilen blir 0. Imidlertid forhindrer dette modellen fra å forstå det riktige mønsteret bak dataene, og dermed er valideringsfeilen veldig høy.

Det er veldig viktig å finne en riktig balanse mellom modellens rikdom (antall parametere) og antall treningsprøver.

## Hvorfor overtilpasning oppstår

  * Ikke nok treningsdata
  * For kraftig modell
  * For mye støy i inngangsdataene

## Hvordan oppdage overtilpasning

Som du kan se fra grafen ovenfor, kan overtilpasning oppdages ved en veldig lav treningsfeil, og en høy valideringsfeil. Normalt under trening vil vi se både trenings- og valideringsfeil begynne å avta, og deretter på et tidspunkt kan valideringsfeilen slutte å avta og begynne å stige. Dette vil være et tegn på overtilpasning, og indikatoren på at vi sannsynligvis bør stoppe treningen på dette punktet (eller i det minste ta et øyeblikksbilde av modellen).

## Hvordan forhindre overtilpasning

Hvis du kan se at overtilpasning oppstår, kan du gjøre en av følgende:

 * Øke mengden treningsdata
 * Redusere modellens kompleksitet
 * Bruke en eller annen reguleringsteknikk, som Dropout, som vi vil vurdere senere.

## Overtilpasning og skjevhet-varians-avveining

Overtilpasning er faktisk et tilfelle av et mer generisk problem i statistikk kalt skjevhet-varians-avveining. Hvis vi vurderer de mulige kildene til feil i vår modell, kan vi se to typer feil:

* **Skjevhetsfeil** skyldes at algoritmen vår ikke klarer å fange forholdet mellom treningsdataene riktig. Det kan skyldes at modellen vår ikke er kraftig nok (**undertilpasning**).
* **Variansfeil**, som skyldes at modellen tilnærmer støy i inngangsdataene i stedet for meningsfullt forhold (**overtilpasning**).

Under trening avtar skjevhetsfeilen (ettersom modellen vår lærer å tilnærme dataene), og variansfeilen øker. Det er viktig å stoppe treningen - enten manuelt (når vi oppdager overtilpasning) eller automatisk (ved å introdusere regulering) - for å forhindre overtilpasning.

## Konklusjon

I denne leksjonen lærte du om forskjellene mellom de ulike APIene for de to mest populære AI-rammeverkene, TensorFlow og PyTorch. I tillegg lærte du om et veldig viktig emne, overtilpasning.

## 🚀 Utfordring

I de medfølgende notatbøkene finner du 'oppgaver' nederst; arbeid deg gjennom notatbøkene og fullfør oppgavene.

## Gjennomgang og selvstudium

Gjør litt research på følgende emner:

- TensorFlow
- PyTorch
- Overtilpasning

Spør deg selv følgende spørsmål:

- Hva er forskjellen mellom TensorFlow og PyTorch?
- Hva er forskjellen mellom overtilpasning og undertilpasning?

## Oppgave

I dette laboratoriet blir du bedt om å løse to klassifiseringsproblemer ved hjelp av enkelt- og flerlags fullt tilkoblede nettverk ved hjelp av PyTorch eller TensorFlow.

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi streber etter nøyaktighet, men vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.