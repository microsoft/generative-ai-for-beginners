<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:14:50+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "no"
}
-->
# Bygge applikasjoner for bildegenerering

Det er mer til LLMs enn tekstgenerering. Det er også mulig å generere bilder fra tekstbeskrivelser. Å ha bilder som en modalitet kan være svært nyttig på flere områder som MedTech, arkitektur, turisme, spillutvikling og mer. I dette kapittelet skal vi se nærmere på de to mest populære bildegenereringsmodellene, DALL-E og Midjourney.

## Introduksjon

I denne leksjonen vil vi dekke:

- Bildegenerering og hvorfor det er nyttig.
- DALL-E og Midjourney, hva de er og hvordan de fungerer.
- Hvordan du kan bygge en bildegenereringsapp.

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Bygge en applikasjon for bildegenerering.
- Definere grenser for applikasjonen din med metaprompts.
- Arbeide med DALL-E og Midjourney.

## Hvorfor bygge en applikasjon for bildegenerering?

Applikasjoner for bildegenerering er en flott måte å utforske mulighetene til Generativ AI. De kan brukes til, for eksempel:

- **Bildebehandling og syntese**. Du kan generere bilder for en rekke bruksområder, som bildebehandling og bildesyntese.

- **Anvendt på en rekke industrier**. De kan også brukes til å generere bilder for en rekke industrier som MedTech, turisme, spillutvikling og mer.

## Scenario: Edu4All

Som en del av denne leksjonen vil vi fortsette å jobbe med vår oppstart, Edu4All, i denne leksjonen. Studentene vil lage bilder for sine vurderinger, nøyaktig hvilke bilder er opp til studentene, men de kan være illustrasjoner for sitt eget eventyr eller lage en ny karakter for sin historie eller hjelpe dem med å visualisere sine ideer og konsepter.

Her er hva Edu4Alls studenter kunne generere for eksempel hvis de jobber i klassen med monumenter:

ved å bruke en prompt som

> "Hund ved siden av Eiffeltårnet i tidlig morgensol"

## Hva er DALL-E og Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) og [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) er to av de mest populære bildegenereringsmodellene, de lar deg bruke prompts til å generere bilder.

### DALL-E

La oss starte med DALL-E, som er en Generativ AI-modell som genererer bilder fra tekstbeskrivelser.

- **CLIP**, er en modell som genererer embeddings, som er numeriske representasjoner av data, fra bilder og tekst.

- **Diffused attention**, er en modell som genererer bilder fra embeddings. DALL-E er trent på et datasett av bilder og tekst og kan brukes til å generere bilder fra tekstbeskrivelser. For eksempel kan DALL-E brukes til å generere bilder av en katt med hatt, eller en hund med mohawk.

### Midjourney

Midjourney fungerer på en lignende måte som DALL-E, den genererer bilder fra tekstprompts. Midjourney kan også brukes til å generere bilder ved hjelp av prompts som “en katt med hatt”, eller en “hund med mohawk”.

## Hvordan fungerer DALL-E og Midjourney

Først, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E er en Generativ AI-modell basert på transformer-arkitektur med en _autoregressiv transformer_.

En _autoregressiv transformer_ definerer hvordan en modell genererer bilder fra tekstbeskrivelser, den genererer én piksel om gangen, og bruker deretter de genererte pikslene til å generere neste piksel. Passerer gjennom flere lag i et nevralt nettverk, til bildet er komplett.

Med denne prosessen kontrollerer DALL-E attributter, objekter, egenskaper og mer i bildet den genererer. Imidlertid har DALL-E 2 og 3 mer kontroll over det genererte bildet.

## Bygge din første applikasjon for bildegenerering

Så hva kreves det for å bygge en applikasjon for bildegenerering? Du trenger følgende biblioteker:

- **python-dotenv**, du anbefales sterkt å bruke dette biblioteket for å holde hemmelighetene dine i en _.env_ fil borte fra koden.
- **openai**, dette biblioteket er det du vil bruke for å samhandle med OpenAI API.
- **pillow**, for å arbeide med bilder i Python.
- **requests**, for å hjelpe deg med å gjøre HTTP-forespørsler.

1. Opprett en fil _.env_ med følgende innhold:

   Finn denne informasjonen i Azure Portal for ressursen din i "Keys and Endpoint" seksjonen.

1. Samle de ovennevnte bibliotekene i en fil kalt _requirements.txt_ slik:

1. Deretter, opprett et virtuelt miljø og installer bibliotekene:

   For Windows, bruk følgende kommandoer for å opprette og aktivere ditt virtuelle miljø:

1. Legg til følgende kode i en fil kalt _app.py_:

La oss forklare denne koden:

- Først importerer vi de nødvendige bibliotekene, inkludert OpenAI-biblioteket, dotenv-biblioteket, requests-biblioteket og Pillow-biblioteket.

- Deretter laster vi inn miljøvariablene fra _.env_ filen.

- Etter det setter vi endepunktet, nøkkelen for OpenAI API, versjon og type.

- Deretter genererer vi bildet:

  Koden over svarer med et JSON-objekt som inneholder URL-en til det genererte bildet. Vi kan bruke URL-en til å laste ned bildet og lagre det til en fil.

- Til slutt åpner vi bildet og bruker den standard bildefremviseren for å vise det:

### Mer detaljer om generering av bildet

La oss se nærmere på koden som genererer bildet:

- **prompt**, er tekstprompten som brukes til å generere bildet. I dette tilfellet bruker vi prompten "Kaninen på hest, holder en kjærlighet, på en tåket eng hvor det vokser påskeliljer".
- **size**, er størrelsen på bildet som genereres. I dette tilfellet genererer vi et bilde som er 1024x1024 piksler.
- **n**, er antallet bilder som genereres. I dette tilfellet genererer vi to bilder.
- **temperature**, er en parameter som kontrollerer tilfeldigheten i outputen til en Generativ AI-modell. Temperaturen er en verdi mellom 0 og 1 hvor 0 betyr at outputen er deterministisk og 1 betyr at outputen er tilfeldig. Standardverdien er 0.7.

Det er flere ting du kan gjøre med bilder som vi vil dekke i neste seksjon.

## Tilleggsfunksjoner for bildegenerering

Du har så langt sett hvordan vi kunne generere et bilde ved hjelp av noen få linjer i Python. Imidlertid er det flere ting du kan gjøre med bilder.

Du kan også gjøre følgende:

- **Utføre redigeringer**. Ved å gi et eksisterende bilde en maske og en prompt, kan du endre et bilde. For eksempel kan du legge til noe i en del av et bilde. Forestill deg vårt kaninbilde, du kan legge til en hatt på kaninen. Hvordan du ville gjort det er ved å gi bildet, en maske (identifisere delen av området for endringen) og en tekstprompt for å si hva som skal gjøres.

  Basebildet ville bare inneholde kaninen, men det endelige bildet ville ha hatten på kaninen.

- **Lage variasjoner**. Ideen er at du tar et eksisterende bilde og ber om at variasjoner blir laget. For å lage en variasjon, gir du et bilde og en tekstprompt og kode som så:

  > Merk, dette støttes kun på OpenAI

## Temperatur

Temperatur er en parameter som kontrollerer tilfeldigheten i outputen til en Generativ AI-modell. Temperaturen er en verdi mellom 0 og 1 hvor 0 betyr at outputen er deterministisk og 1 betyr at outputen er tilfeldig. Standardverdien er 0.7.

La oss se på et eksempel på hvordan temperatur fungerer, ved å kjøre denne prompten to ganger:

> Prompt : "Kaninen på hest, holder en kjærlighet, på en tåket eng hvor det vokser påskeliljer"

Nå la oss kjøre den samme prompten bare for å se at vi ikke vil få det samme bildet to ganger:

Som du kan se, er bildene like, men ikke de samme. La oss prøve å endre temperaturverdien til 0.1 og se hva som skjer:

### Endre temperaturen

Så la oss prøve å gjøre responsen mer deterministisk. Vi kunne observere fra de to bildene vi genererte at i det første bildet er det en kanin, og i det andre bildet er det en hest, så bildene varierer sterkt.

La oss derfor endre koden vår og sette temperaturen til 0, slik:

Nå når du kjører denne koden, får du disse to bildene:

Her kan du tydelig se hvordan bildene ligner hverandre mer.

## Hvordan definere grenser for applikasjonen din med metaprompts

Med vår demo kan vi allerede generere bilder for våre klienter. Imidlertid må vi lage noen grenser for applikasjonen vår.

For eksempel ønsker vi ikke å generere bilder som ikke er trygge for arbeid, eller som ikke er passende for barn.

Vi kan gjøre dette med _metaprompts_. Metaprompts er tekstprompts som brukes til å kontrollere outputen til en Generativ AI-modell. For eksempel kan vi bruke metaprompts til å kontrollere outputen, og sikre at de genererte bildene er trygge for arbeid, eller passende for barn.

### Hvordan fungerer det?

Nå, hvordan fungerer metaprompts?

Metaprompts er tekstprompts som brukes til å kontrollere outputen til en Generativ AI-modell, de er plassert før tekstprompten, og brukes til å kontrollere outputen til modellen og innbakt i applikasjoner for å kontrollere outputen til modellen. Innkapsler prompt-inngangen og metaprompt-inngangen i en enkelt tekstprompt.

Et eksempel på en metaprompt ville være følgende:

Nå, la oss se hvordan vi kan bruke metaprompts i vår demo.

Fra prompten ovenfor kan du se hvordan alle bilder som opprettes tar hensyn til metaprompten.

## Oppgave - la oss gjøre studentene i stand

Vi introduserte Edu4All i begynnelsen av denne leksjonen. Nå er det på tide å gjøre studentene i stand til å generere bilder for sine vurderinger.

Studentene vil lage bilder for sine vurderinger som inneholder monumenter, nøyaktig hvilke monumenter er opp til studentene. Studentene blir bedt om å bruke sin kreativitet i denne oppgaven for å plassere disse monumentene i forskjellige kontekster.

## Løsning

Her er en mulig løsning:

## Flott arbeid! Fortsett din læring

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

Gå videre til leksjon 10 hvor vi vil se på hvordan man [bygger AI-applikasjoner med lavkode](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

Sure, here's the translation of the disclaimer into Norwegian:

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.