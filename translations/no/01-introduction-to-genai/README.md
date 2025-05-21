<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:23:43+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "no"
}
-->
# Introduksjon til Generativ AI og Store Språkmodeller

Generativ AI er kunstig intelligens som kan generere tekst, bilder og andre typer innhold. Det som gjør det til en fantastisk teknologi er at det demokratiserer AI, hvem som helst kan bruke det med så lite som et tekstprompt, en setning skrevet i et naturlig språk. Du trenger ikke lære et språk som Java eller SQL for å oppnå noe verdifullt, alt du trenger er å bruke ditt eget språk, si hva du vil, og ut kommer et forslag fra en AI-modell. Anvendelsene og innvirkningen av dette er enorme; du kan skrive eller forstå rapporter, lage applikasjoner og mye mer, alt på sekunder.

I denne læreplanen vil vi utforske hvordan vår startup utnytter generativ AI for å åpne nye scenarier i utdanningsverdenen og hvordan vi håndterer de uunngåelige utfordringene knyttet til de sosiale implikasjonene av dens anvendelse og teknologibegrensningene.

## Introduksjon

Denne leksjonen vil dekke:

- Introduksjon til forretningsscenariet: vår startup-idé og misjon.
- Generativ AI og hvordan vi landet på dagens teknologilandskap.
- Indre arbeid av en stor språkmodell.
- Hovedfunksjoner og praktiske brukstilfeller av store språkmodeller.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du forstå:

- Hva generativ AI er og hvordan store språkmodeller fungerer.
- Hvordan du kan utnytte store språkmodeller for ulike brukstilfeller, med fokus på utdanningsscenarier.

## Scenario: vår utdanningsstartup

Generativ Kunstig Intelligens (AI) representerer toppen av AI-teknologi, og presser grensene for hva man en gang trodde var umulig. Generative AI-modeller har flere kapasiteter og anvendelser, men for denne læreplanen vil vi utforske hvordan det revolusjonerer utdanning gjennom en fiktiv startup. Vi vil referere til denne startupen som _vår startup_. Vår startup arbeider innen utdanningsområdet med den ambisiøse misjonserklæringen

> _å forbedre tilgjengeligheten i læring, på global skala, sikre lik tilgang til utdanning og tilby personlige læringsopplevelser til hver elev, i henhold til deres behov_.

Vårt startup-team er klar over at vi ikke vil kunne oppnå dette målet uten å utnytte et av de mest kraftfulle verktøyene i moderne tid – Store Språkmodeller (LLMs).

Generativ AI forventes å revolusjonere måten vi lærer og underviser på i dag, med studenter som har virtuelle lærere tilgjengelig 24 timer i døgnet som gir store mengder informasjon og eksempler, og lærere som kan utnytte innovative verktøy for å vurdere sine studenter og gi tilbakemelding.

For å begynne, la oss definere noen grunnleggende begreper og terminologi vi vil bruke gjennom hele læreplanen.

## Hvordan fikk vi Generativ AI?

Til tross for den ekstraordinære _hypen_ som nylig er skapt av annonseringen av generative AI-modeller, er denne teknologien tiår i utvikling, med de første forskningsinnsatsene som dateres tilbake til 60-tallet. Vi er nå på et punkt hvor AI har menneskelige kognitive evner, som samtale, som vist for eksempel av [OpenAI ChatGPT](https://openai.com/chatgpt) eller [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), som også bruker en GPT-modell for websøket Bing samtaler.

Hvis vi går litt tilbake, besto de aller første prototypene av AI av maskinskrevne chatbots, som stolte på en kunnskapsbase hentet fra en gruppe eksperter og representert i en datamaskin. Svarene i kunnskapsbasen ble utløst av nøkkelord som dukket opp i input-teksten. Imidlertid ble det snart klart at en slik tilnærming, ved bruk av maskinskrevne chatbots, ikke skalerte godt.

### En statistisk tilnærming til AI: Maskinlæring

Et vendepunkt kom på 90-tallet, med anvendelsen av en statistisk tilnærming til tekstanalyse. Dette førte til utviklingen av nye algoritmer – kjent som maskinlæring – som var i stand til å lære mønstre fra data uten å være eksplisitt programmert. Denne tilnærmingen lar maskiner simulere menneskelig språkforståelse: en statistisk modell trenes på tekst-label paringer, slik at modellen kan klassifisere ukjent input-tekst med en forhåndsdefinert label som representerer intensjonen i meldingen.

### Nevrale nettverk og moderne virtuelle assistenter

I de senere årene har den teknologiske utviklingen av maskinvare, som er i stand til å håndtere større datamengder og mer komplekse beregninger, oppmuntret forskning innen AI, som førte til utviklingen av avanserte maskinlæringsalgoritmer kjent som nevrale nettverk eller dyp læringsalgoritmer.

Nevrale nettverk (og spesielt Recurrent Neural Networks – RNNs) forbedret betydelig naturlig språkbehandling, og gjorde det mulig å representere betydningen av tekst på en mer meningsfull måte, verdsette konteksten av et ord i en setning.

Dette er teknologien som drev de virtuelle assistentene som ble født i det første tiåret av det nye århundret, svært dyktige i å tolke menneskelig språk, identifisere et behov og utføre en handling for å tilfredsstille det – som å svare med et forhåndsdefinert manus eller konsumere en tredjepartstjeneste.

### Nåtid, Generativ AI

Sånn kom vi til Generativ AI i dag, som kan sees som en delmengde av dyp læring.

Etter tiår med forskning innen AI-feltet, overkom en ny modellarkitektur – kalt _Transformer_ – begrensningene til RNNs, ved å kunne få mye lengre tekstsekvenser som input. Transformere er basert på oppmerksomhetsmekanismen, som gjør det mulig for modellen å gi forskjellige vekter til inputene den mottar, 'gi mer oppmerksomhet' der den mest relevante informasjonen er konsentrert, uavhengig av deres rekkefølge i tekstsekvensen.

De fleste av de nylige generative AI-modellene – også kjent som Store Språkmodeller (LLMs), siden de arbeider med tekstuelle input og output – er faktisk basert på denne arkitekturen. Det som er interessant med disse modellene – trent på en enorm mengde umerkede data fra ulike kilder som bøker, artikler og nettsteder – er at de kan tilpasses et bredt spekter av oppgaver og generere grammatisk korrekt tekst med et snev av kreativitet. Så, ikke bare forbedret de utrolig maskinens evne til å 'forstå' en input-tekst, men de gjorde det mulig for dem å generere et originalt svar i menneskelig språk.

## Hvordan fungerer store språkmodeller?

I neste kapittel skal vi utforske ulike typer generative AI-modeller, men for nå la oss se på hvordan store språkmodeller fungerer, med fokus på OpenAI GPT (Generative Pre-trained Transformer) modeller.

- **Tokenizer, tekst til tall**: Store Språkmodeller mottar en tekst som input og genererer en tekst som output. Men siden de er statistiske modeller, fungerer de mye bedre med tall enn tekstsekvenser. Derfor blir hver input til modellen behandlet av en tokenizer, før den brukes av kjernemodellen. En token er en del av tekst – bestående av et variabelt antall tegn, så tokenizerens hovedoppgave er å dele inputen inn i en rekke tokens. Deretter blir hver token kartlagt med en token-indeks, som er den heltalls koding av den opprinnelige tekstdelen.

- **Prediksjon av output-tokens**: Gitt n tokens som input (med maks n som varierer fra en modell til en annen), er modellen i stand til å forutsi én token som output. Denne tokenen blir deretter innlemmet i inputen til neste iterasjon, i et ekspanderende vindusmønster, som gir en bedre brukeropplevelse av å få en (eller flere) setninger som svar. Dette forklarer hvorfor, hvis du noen gang har lekt med ChatGPT, du kanskje har lagt merke til at det noen ganger ser ut som om det stopper midt i en setning.

- **Utvalg prosess, sannsynlighetsfordeling**: Output-tokenen velges av modellen i henhold til dens sannsynlighet for å forekomme etter den nåværende tekstsekvensen. Dette er fordi modellen forutsier en sannsynlighetsfordeling over alle mulige 'neste tokens', beregnet basert på dens trening. Imidlertid er det ikke alltid tokenen med høyest sannsynlighet som velges fra den resulterende fordelingen. En grad av tilfeldighet legges til dette valget, på en måte som modellen oppfører seg på en ikke-deterministisk måte - vi får ikke nøyaktig samme output for samme input. Denne graden av tilfeldighet legges til for å simulere prosessen med kreativ tenkning, og den kan justeres ved hjelp av en modellparameter kalt temperatur.

## Hvordan kan vår startup utnytte Store Språkmodeller?

Nå som vi har en bedre forståelse av den indre virkemåten til en stor språkmodell, la oss se noen praktiske eksempler på de vanligste oppgavene de kan utføre ganske bra, med et øye til vårt forretningsscenario. Vi sa at hovedkapasiteten til en stor språkmodell er _å generere en tekst fra bunnen av, med utgangspunkt i en tekstinput, skrevet i naturlig språk_.

Men hva slags tekstinput og output?
Inputen til en stor språkmodell er kjent som et prompt, mens outputen er kjent som en completion, et begrep som refererer til modellens mekanisme for å generere den neste tokenen for å fullføre den nåværende inputen. Vi skal dykke dypt inn i hva et prompt er og hvordan man designer det på en måte som får mest mulig ut av vår modell. Men for nå, la oss bare si at et prompt kan inkludere:

- En **instruksjon** som spesifiserer typen output vi forventer fra modellen. Denne instruksjonen kan noen ganger inneholde noen eksempler eller noen tilleggsdata.

  1. Sammendrag av en artikkel, bok, produktanmeldelser og mer, sammen med utvinning av innsikter fra ustrukturert data.

  2. Kreativ ideutvikling og design av en artikkel, et essay, en oppgave eller mer.

- Et **spørsmål**, stilt i form av en samtale med en agent.

- En del av **tekst å fullføre**, som implisitt er en forespørsel om skriveassistanse.

- En del av **kode** sammen med forespørselen om å forklare og dokumentere den, eller en kommentar som ber om å generere et stykke kode som utfører en spesifikk oppgave.

Eksemplene ovenfor er ganske enkle og er ikke ment å være en uttømmende demonstrasjon av Store Språkmodellers kapasiteter. De er ment å vise potensialet ved å bruke generativ AI, spesielt men ikke begrenset til utdanningskontekster.

Også, outputen av en generativ AI-modell er ikke perfekt og noen ganger kan modellens kreativitet virke mot den, resulterende i en output som er en kombinasjon av ord som den menneskelige brukeren kan tolke som en mystifikasjon av virkeligheten, eller det kan være støtende. Generativ AI er ikke intelligent - i det minste ikke i den mer omfattende definisjonen av intelligens, inkludert kritisk og kreativ resonnement eller emosjonell intelligens; den er ikke deterministisk, og den er ikke pålitelig, siden fabrikasjoner, som feilaktige referanser, innhold og uttalelser, kan kombineres med korrekt informasjon og presenteres på en overbevisende og selvsikker måte. I de følgende leksjonene vil vi håndtere alle disse begrensningene og se hva vi kan gjøre for å dempe dem.

## Oppgave

Din oppgave er å lese mer om [generativ AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) og prøve å identifisere et område der du ville legge til generativ AI i dag som ikke har det. Hvordan ville innvirkningen være annerledes fra å gjøre det på den "gamle måten", kan du gjøre noe du ikke kunne før, eller er du raskere? Skriv et 300 ords sammendrag om hvordan din drømme AI-startup ville se ut og inkluder overskrifter som "Problem", "Hvordan jeg ville bruke AI", "Innvirkning" og eventuelt en forretningsplan.

Hvis du gjorde denne oppgaven, kan du til og med være klar til å søke på Microsofts inkubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) vi tilbyr kreditter for både Azure, OpenAI, veiledning og mye mer, sjekk det ut!

## Kunnskapssjekk

Hva er sant om store språkmodeller?

1. Du får nøyaktig samme respons hver gang.
1. Den gjør ting perfekt, flink til å legge til tall, produsere fungerende kode osv.
1. Responsen kan variere til tross for at du bruker samme prompt. Den er også flink til å gi deg et første utkast av noe, enten det er tekst eller kode. Men du må forbedre resultatene.

A: 3, en LLM er ikke-deterministisk, responsen varierer, men du kan kontrollere dens variasjon via en temperaturinnstilling. Du bør heller ikke forvente at den gjør ting perfekt, den er her for å gjøre det tunge løftet for deg, noe som ofte betyr at du får et godt første forsøk på noe som du trenger å forbedre gradvis.

## Flott arbeid! Fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generativ AI Læringssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å heve din Generativ AI-kunnskap!

Gå videre til Leksjon 2 hvor vi vil se på hvordan man [utforsker og sammenligner forskjellige LLM-typer](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.