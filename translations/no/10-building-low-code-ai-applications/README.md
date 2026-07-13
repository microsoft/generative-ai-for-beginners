# Bygge lavkode AI-applikasjoner

[![Bygge lavkode AI-applikasjoner](../../../translated_images/no/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klikk på bildet over for å se videoen av denne leksjonen)_

## Introduksjon

Nå som vi har lært hvordan man bygger bildeproduserende applikasjoner, la oss snakke om lavkode. Generativ AI kan brukes til en rekke forskjellige områder inkludert lavkode, men hva er lavkode og hvordan kan vi legge til AI i det?

Å bygge apper og løsninger har blitt enklere for tradisjonelle utviklere og ikke-utviklere gjennom bruk av plattformer for lavkodeutvikling. Lavkodeutviklingsplattformer gjør det mulig å bygge apper og løsninger med liten eller ingen koding. Dette oppnås ved å tilby et visuelt utviklingsmiljø som lar deg dra og slippe komponenter for å bygge apper og løsninger. Dette gjør at du kan bygge apper og løsninger raskere og med færre ressurser. I denne leksjonen dykker vi dypt inn i hvordan man bruker lavkode og hvordan man forbedrer lavkodeutvikling med AI ved hjelp av Power Platform.

Power Platform gir organisasjoner muligheten til å styrke teamene sine til å bygge egne løsninger gjennom et intuitivt lavkode- eller nokode-miljø. Dette miljøet forenkler prosessen med å bygge løsninger. Med Power Platform kan løsninger bygges på dager eller uker i stedet for måneder eller år. Power Platform består av fem nøkkelprodukter: Power Apps, Power Automate, Power BI, Power Pages og Copilot Studio.

Denne leksjonen dekker:

- Introduksjon til generativ AI i Power Platform
- Introduksjon til Copilot og hvordan bruke det
- Bruke generativ AI for å bygge apper og flyter i Power Platform
- Forstå AI-modellene i Power Platform med AI Builder
- Bygge intelligente agenter med Microsoft Copilot Studio

## Læringsmål

På slutten av denne leksjonen vil du kunne:

- Forstå hvordan Copilot fungerer i Power Platform.

- Bygge en app for sporing av studentoppgaver til vårt utdanningsstartup.

- Bygge en fakturabehandlingsflyt som bruker AI for å hente informasjon fra fakturaer.

- Anvende beste praksis når du bruker Create Text med GPT AI-modellen.

- Forstå hva Microsoft Copilot Studio er og hvordan bygge intelligente agenter med det.

Verktøyene og teknologiene du vil bruke i denne leksjonen er:

- **Power Apps**, for appen Student Assignment Tracker, som tilbyr et lavkodeutviklingsmiljø for å bygge apper for sporing, administrasjon og interaksjon med data.

- **Dataverse**, for lagring av dataene for Student Assignment Tracker-appen hvor Dataverse vil tilby en lavkode dataplattform for lagring av appens data.

- **Power Automate**, for fakturabehandlingsflyten hvor du vil ha et lavkodeutviklingsmiljø for å bygge arbeidsflyter til å automatisere fakturabehandlingsprosessen.

- **AI Builder**, for fakturabehandlings AI-modellen hvor du bruker forhåndsbygde AI-modeller for å behandle fakturaene for vår startup.

## Generativ AI i Power Platform

Å forbedre lavkodeutvikling og applikasjoner med generativ AI er et hovedfokusområde for Power Platform. Målet er å gjøre det mulig for alle å bygge AI-drevne apper, nettsteder, dashboards og automatisere prosesser med AI, _uten behov for spesiell datavitenskapelig ekspertise_. Dette målet oppnås ved å integrere generativ AI i lavkodeutviklingsopplevelsen i Power Platform i form av Copilot og AI Builder.

### Hvordan fungerer dette?

Copilot er en AI-assistent som gjøre det mulig å bygge Power Platform-løsninger ved å beskrive dine krav i en serie samtaletrinn med naturlig språk. Du kan for eksempel instruere AI-assistenten til å angi hvilke felt appen din skal bruke, og den vil både lage appen og den underliggende datamodellen, eller du kan spesifisere hvordan sette opp en flyt i Power Automate.

Du kan bruke Copilot-drevne funksjonaliteter som en funksjon i appskjermene dine for å la brukere avdekke innsikter gjennom konversasjonelle interaksjoner.

AI Builder er en lavkode AI-funksjon tilgjengelig i Power Platform som gjør det mulig å bruke AI-modeller til å hjelpe deg å automatisere prosesser og forutsi utfall. Med AI Builder kan du bringe AI til appene og flytene dine som kobler til data i Dataverse eller i ulike skylagringskilder som SharePoint, OneDrive eller Azure.

Copilot er tilgjengelig i alle Power Platform-produktene: Power Apps, Power Automate, Power BI, Power Pages og Copilot Studio (tidligere Power Virtual Agents). AI Builder er tilgjengelig i Power Apps og Power Automate. I denne leksjonen vil vi fokusere på hvordan bruke Copilot og AI Builder i Power Apps og Power Automate for å bygge en løsning for vårt utdanningsstartup.

### Copilot i Power Apps

Som en del av Power Platform tilbyr Power Apps et lavkodeutviklingsmiljø for å bygge apper til å spore, administrere og interagere med data. Det er en apputviklingstjeneste med en skalerbar dataplattform og evnen til å koble til skyløsninger og lokale data. Power Apps lar deg bygge apper som kjører i nettlesere, nettbrett og telefoner, og kan deles med kollegaer. Power Apps gjør apputvikling enkelt med en enkel brukergrensesnitt slik at alle forretningsbrukere eller profesjonelle utviklere kan bygge tilpassede apper. Apputviklingsopplevelsen forbedres også med generativ AI gjennom Copilot.

Copilot AI-assistentfunksjonen i Power Apps lar deg beskrive hvilken type app du trenger og hvilken informasjon du vil at appen skal spore, samle eller vise. Copilot genererer da en responsiv Canvas-app basert på beskrivelsen din. Du kan deretter tilpasse appen for dine behov. AI Copilot genererer også og foreslår en Dataverse-tabell med de feltene du trenger for å lagre dataene du ønsker å spore, i tillegg til noe eksempeldata. Vi vil se nærmere på hva Dataverse er og hvordan du kan bruke det i Power Apps senere i denne leksjonen. Du kan deretter tilpasse tabellen for dine behov ved å bruke AI Copilot-assistentfunksjonen gjennom samtaletrinn. Denne funksjonen er lett tilgjengelig fra Power Apps- startsiden.

### Copilot i Power Automate

Som en del av Power Platform lar Power Automate brukere lage automatiserte arbeidsflyter mellom applikasjoner og tjenester. Det hjelper med å automatisere repetitive forretningsprosesser som kommunikasjon, datainnsamling og godkjenning av beslutninger. Den enkle brukergrensesnittet gjør det mulig for brukere med ulik teknisk kompetanse (fra nybegynnere til erfarne utviklere) å automatisere arbeidsoppgaver. Arbeidsflytutviklingsopplevelsen forbedres også med generativ AI gjennom Copilot.

Copilot AI-assistentfunksjonen i Power Automate lar deg beskrive hvilken type flyt du trenger og hvilke handlinger flyten skal utføre. Copilot genererer da en flyt basert på beskrivelsen din. Du kan deretter tilpasse flyten etter dine behov. AI Copilot genererer også og foreslår handlingene du trenger for å utføre oppgaven du ønsker å automatisere. Vi vil se på hva flyter er og hvordan du kan bruke dem i Power Automate senere i denne leksjonen. Du kan deretter tilpasse handlingene etter dine behov ved å bruke AI Copilot-assistentfunksjonen gjennom samtaletrinn. Denne funksjonen er lett tilgjengelig fra Power Automate-startsiden.

## Bygge intelligente agenter med Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (tidligere Power Virtual Agents) er lavkode-medlemmet i Power Platform for å bygge **AI-agenter** — konversasjonscopiloter som kan svare på spørsmål, utføre handlinger og automatisere oppgaver på vegne av brukerne dine. Akkurat som resten av Power Platform bygger du disse agentene i en visuell, naturlig språk-først-opplevelse: du beskriver hva du vil at agenten skal gjøre, og Copilot Studio hjelper med å legge grunnlaget for instruksjoner, kunnskap og handlinger.

For vårt utdanningsstartup kunne du bygge en agent som svarer på studenters spørsmål om kurs, sjekker innleveringsfrister for oppgaver, og til og med sender e-post til en instruktør — alt uten å måtte kode.

Her er noen av de nyeste funksjonene som gjør Copilot Studio kraftfull:

- **Generative svar fra kunnskapen din**. I stedet for å forfatte hver samtale manuelt, kan du koble til **kunnskapskilder** — offentlige nettsteder, SharePoint, OneDrive, Dataverse, opplastede filer eller bedriftsdata gjennom tilkoblinger — og agenten genererer begrunnede svar fra disse.

- **Generativ orkestrering**. I stedet for å stole på rigide utløserfraser, bruker agenten AI til å forstå en forespørsel og dynamisk bestemme hvilken kunnskap, hvilke temaer og handlinger som skal kombineres for å oppfylle den, inkludert å knytte sammen flere trinn.

- **Handlinger og tilkoblinger**. Agenter kan *gjøre* ting, ikke bare chatte. Du kan gi en agent handlinger støttet av de 1500+ forhåndsbygde Power Platform-tilkoblingene, Power Automate-flyter, egendefinerte REST-APIer, ledetekster eller **Model Context Protocol (MCP)**-servere.

- **Autonome agenter**. Agenter er ikke begrenset til å svare i et chattevindu. Du kan bygge **autonome agenter** som utløses av hendelser — som en ny e-post, en ny post i Dataverse, eller en fil som blir lastet opp — og deretter handler i bakgrunnen for å fullføre en oppgave.

- **Multi-agent orkestrering**. Agenter kan kalle på andre agenter. En Copilot Studio-agent kan overlevere til, eller bli utvidet av, andre agenter, inkludert agenter publisert til Microsoft 365 Copilot og agenter bygget i Microsoft Foundry.

- **Modellvalg**. Utover de innebygde modellene kan du ta med modeller fra Microsoft Foundry-modellkatalogen for å tilpasse hvordan agenten resonerer og svarer.

- **Publiser hvor som helst**. Når den er bygget, kan en agent publiseres til flere kanaler — Microsoft Teams, Microsoft 365 Copilot, et nettsted eller tilpasset app, og mer — med sikkerhet, autentisering og analyse administrert gjennom Power Platform-administrasjonsopplevelsen.

Du kan starte byggingen av din første agent på [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) og lære mer i [Microsoft Copilot Studio-dokumentasjonen](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Oppgave: Administrer studentoppgaver og fakturaer for vår startup, ved bruk av Copilot

Vårt startup tilbyr nettkurs til studenter. Startupen har vokst raskt og strever nå med å følge etterspørselen etter kursene sine. Startupen har ansatt deg som Power Platform-utvikler for å hjelpe dem med å bygge en lavkode-løsning for å hjelpe dem med å håndtere studentoppgavene og fakturaene sine. Løsningen deres bør kunne hjelpe dem med å spore og administrere studentoppgaver gjennom en app og automatisere fakturabehandlingsprosessen gjennom en arbeidsflyt. Du har blitt bedt om å bruke generativ AI for å utvikle løsningen.

Når du kommer i gang med å bruke Copilot, kan du bruke [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) for å komme i gang med promptene. Dette biblioteket inneholder en liste over prompt som du kan bruke til å bygge apper og flyter med Copilot. Du kan også bruke promptene i biblioteket for å få en idé om hvordan du skal beskrive kravene dine til Copilot.

### Bygg en Student Assignment Tracker-app for vårt startup

Lærerne ved vårt startup har hatt problemer med å holde oversikt over studentoppgaver. De har brukt et regneark til å spore oppgavene, men dette har blitt vanskelig å administrere etter hvert som antallet studenter har økt. De har bedt deg om å bygge en app som hjelper dem å spore og administrere studentoppgaver. Appen skal gjøre det mulig å legge til nye oppgaver, se oppgaver, oppdatere oppgaver og slette oppgaver. Appen skal også gjøre det mulig for både lærere og studenter å se oppgavene som har blitt vurdert og de som ikke har blitt vurdert.

Du vil bygge appen ved å bruke Copilot i Power Apps ved å følge stegene nedenfor:

1. Naviger til [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) startskjerm.

1. Bruk tekstområdet på startskjermen for å beskrive appen du vil bygge. For eksempel, **_Jeg vil bygge en app for å spore og administrere studentoppgaver_**. Klikk på **Send**-knappen for å sende prompten til AI Copilot.

![Beskriv appen du vil bygge](../../../translated_images/no/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot vil foreslå en Dataverse-tabell med feltene du trenger for å lagre dataene du vil spore og noe eksempeldata. Du kan deretter tilpasse tabellen for å møte dine behov ved hjelp av AI Copilot-assistentfunksjonen gjennom samtaletrinn.

   > **Viktig**: Dataverse er den underliggende dataplattformen for Power Platform. Det er en lavkode dataplattform for lagring av appens data. Det er en fullstendig administrert tjeneste som sikrer lagring av data i Microsoft Cloud og provisjoneres innenfor ditt Power Platform-miljø. Den har innebygde datastyringsmuligheter, som dataklassifisering, datalinjer, detaljert tilgangskontroll og mer. Du kan lære mer om Dataverse [her](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Foreslåtte felt i din nye tabell](../../../translated_images/no/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Lærerne vil sende e-poster til studentene som har levert oppgavene sine for å holde dem oppdatert på framdriften. Du kan bruke Copilot til å legge til et nytt felt i tabellen for å lagre studentenes e-post. For eksempel, du kan bruke følgende prompt for å legge til et nytt felt i tabellen: **_Jeg vil legge til en kolonne for å lagre studentens e-post_**. Klikk på **Send**-knappen for å sende prompten til AI Copilot.

![Legge til et nytt felt](../../../translated_images/no/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot vil generere et nytt felt, og du kan deretter tilpasse feltet for å møte dine behov.


1. Når du er ferdig med tabellen, klikker du på **Create app**-knappen for å opprette appen.

1. AI Copilot vil generere en responsiv Canvas-app basert på beskrivelsen din. Du kan deretter tilpasse appen for å dekke dine behov.

1. For lærere som skal sende e-post til studenter, kan du bruke Copilot til å legge til en ny skjerm i appen. For eksempel kan du bruke følgende prompt for å legge til en ny skjerm i appen: **_I want to add a screen to send emails to students_**. Klikk på **Send**-knappen for å sende prompten til AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/no/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot vil generere en ny skjerm, og du kan deretter tilpasse skjermen slik at den passer dine behov.

1. Når du er ferdig med appen, klikker du på **Save**-knappen for å lagre appen.

1. For å dele appen med lærerne, klikker du på **Share**-knappen og deretter klikker du på **Share**-knappen igjen. Deretter kan du dele appen med lærerne ved å skrive inn e-postadressene deres.

> **Din lekse**: Appen du nettopp laget er en god start, men kan forbedres. Med e-postfunksjonen kan lærerne bare sende e-post til studenter manuelt ved å måtte skrive inn e-postadressene deres. Kan du bruke Copilot til å bygge en automatisering som gjør det mulig for lærerne å automatisk sende e-post til studenter når de leverer inn oppgavene sine? Tipset ditt er at med riktig prompt kan du bruke Copilot i Power Automate til å bygge dette.

### Bygg en fakturainformasjonstabell for oppstartsselskapet vårt

Økonomiteamet i oppstartsselskapet vårt har hatt problemer med å holde oversikt over fakturaer. De har brukt et regneark for å spore fakturaene, men dette har blitt vanskelig å administrere etter hvert som antallet fakturaer har økt. De har bedt deg om å bygge en tabell som vil hjelpe dem med å lagre, spore og administrere informasjonen om fakturaene de har mottatt. Tabellen skal brukes til å bygge en automatisering som vil hente ut all fakturainformasjon og lagre den i tabellen. Tabellen skal også gjøre det mulig for økonomiteamet å se hvilke fakturaer som er betalt og hvilke som ikke er betalt.

Power Platform har en underliggende dataplattform kalt Dataverse som gjør det mulig å lagre data for appene og løsningene dine. Dataverse tilbyr en lavkode-dataplattform for lagring av appens data. Det er en fullt administrert tjeneste som lagrer data sikkert i Microsoft-skyen og er tilgjengelig innenfor Power Platform-miljøet ditt. Den kommer med innebygde datastyringsmuligheter, som dataklassifisering, dataflyt, finmasket tilgangskontroll og mer. Du kan lære mer [om Dataverse her](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Hvorfor bør vi bruke Dataverse for oppstartsselskapet vårt? Standard- og egendefinerte tabeller i Dataverse gir et sikkert og skybasert lagringsalternativ for dataene dine. Tabeller lar deg lagre forskjellige typer data, på samme måte som du kan bruke flere regneark i én Excel-arbeidsbok. Du kan bruke tabeller til å lagre data som er spesifikke for organisasjonen eller virksomheten din. Noen av fordelene vårt oppstartsselskap vil få ved å bruke Dataverse inkluderer, men er ikke begrenset til:

- **Enkelt å administrere**: Både metadata og data lagres i skyen, så du trenger ikke å bekymre deg for detaljene om hvordan de lagres eller administreres. Du kan fokusere på å bygge appene og løsningene dine.

- **Sikkert**: Dataverse tilbyr et sikkert og skybasert lagringsalternativ for dataene dine. Du kan kontrollere hvem som har tilgang til dataene i tabellene dine og hvordan de kan få tilgang ved hjelp av rollebasert sikkerhet.

- **Rik metadata**: Datatyper og relasjoner brukes direkte i Power Apps.

- **Logikk og validering**: Du kan bruke forretningsregler, kalkulerte felt og valideringsregler for å håndheve forretningslogikk og opprettholde datanøyaktighet.

Nå som du vet hva Dataverse er og hvorfor du bør bruke det, la oss se på hvordan du kan bruke Copilot til å opprette en tabell i Dataverse for å møte kravene til økonomiteamet vårt.

> **Merk**: Du vil bruke denne tabellen i neste seksjon for å bygge en automatisering som vil hente ut all fakturainformasjon og lagre den i tabellen.

For å opprette en tabell i Dataverse ved hjelp av Copilot, følg trinnene nedenfor:

1. Gå til [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) startsiden.

2. På venstre navigasjonslinje, velg **Tables** og klikk deretter på **Describe the new Table**.

![Select new table](../../../translated_images/no/describe-new-table.0792373eb757281e.webp)

1. På skjermen **Describe the new Table**, bruk tekstområdet til å beskrive tabellen du vil opprette. For eksempel, **_I want to create a table to store invoice information_**. Klikk på **Send**-knappen for å sende prompten til AI Copilot.

![Describe the table](../../../translated_images/no/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot vil foreslå en Dataverse-tabell med feltene du trenger for å lagre dataene du vil spore og noe eksempelddata. Du kan deretter tilpasse tabellen for å dekke dine behov ved å bruke AI Copilot-assistentfunksjonen gjennom konversasjonstrinn.

![Suggested Dataverse table](../../../translated_images/no/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Økonomiteamet ønsker å sende en e-post til leverandøren for å oppdatere dem om statusen på fakturaen. Du kan bruke Copilot til å legge til et nytt felt i tabellen som lagrer leverandørens e-post. For eksempel kan du bruke følgende prompt for å legge til et nytt felt i tabellen: **_I want to add a column to store supplier email_**. Klikk på **Send**-knappen for å sende prompten til AI Copilot.

1. AI Copilot vil generere et nytt felt, og du kan deretter tilpasse feltet for å dekke dine behov.

1. Når du er ferdig med tabellen, klikker du på **Create**-knappen for å opprette tabellen.

## AI-modeller i Power Platform med AI Builder

AI Builder er en lavkode AI-funksjonalitet tilgjengelig i Power Platform som gjør det mulig å bruke AI-modeller for å hjelpe til med å automatisere prosesser og forutsi resultater. Med AI Builder kan du integrere AI i appene og flytene dine som kobler til dataene dine i Dataverse eller i ulike skylagringskilder, som SharePoint, OneDrive eller Azure.

## Ferdigbygde AI-modeller vs egendefinerte AI-modeller

AI Builder tilbyr to typer AI-modeller: Ferdigbygde AI-modeller og egendefinerte AI-modeller. Ferdigbygde AI-modeller er klart-til-bruk AI-modeller som er trent av Microsoft og tilgjengelig i Power Platform. Disse hjelper deg å tilføre intelligens til appene og flytene dine uten at du må samle data og deretter bygge, trene og publisere dine egne modeller. Du kan bruke disse modellene til å automatisere prosesser og forutsi resultater.

Noen av de ferdigbygde AI-modellene som er tilgjengelige i Power Platform inkluderer:

- **Nøkkelsetningsekstraksjon**: Denne modellen trekker ut nøkkelsetninger fra tekst.
- **Språkdeteksjon**: Denne modellen oppdager språket i en tekst.
- **Sentimentanalyse**: Denne modellen oppdager positiv, negativ, nøytral eller blandet følelse i tekst.
- **Visittkortleser**: Denne modellen trekker ut informasjon fra visittkort.
- **Tekstgjenkjenning**: Denne modellen trekker ut tekst fra bilder.
- **Objektdeteksjon**: Denne modellen oppdager og trekker ut objekter fra bilder.
- **Dokumentbehandling**: Denne modellen trekker ut informasjon fra skjemaer.
- **Fakturabehandling**: Denne modellen trekker ut informasjon fra fakturaer.

Med egendefinerte AI-modeller kan du ta med din egen modell inn i AI Builder slik at den kan fungere som en hvilken som helst egendefinert AI Builder-modell, som lar deg trene modellen med dine egne data. Du kan bruke disse modellene til å automatisere prosesser og forutsi resultater både i Power Apps og Power Automate. Når du bruker din egen modell, gjelder det visse begrensninger. Les mer om disse [begrensningene](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/no/ai-builder-models.8069423b84cfc47f.webp)

## Oppgave #2 - Bygg en fakturabehandlingsflyt for oppstartsselskapet vårt

Økonomiteamet har hatt problemer med å behandle fakturaer. De har brukt et regneark for å spore fakturaene, men dette har blitt vanskelig å administrere etter hvert som antallet fakturaer har økt. De har bedt deg om å bygge en arbeidsflyt som vil hjelpe dem med å behandle fakturaer ved hjelp av AI. Arbeidsflyten skal gjøre det mulig å hente informasjon fra fakturaer og lagre informasjonen i en Dataverse-tabell. Arbeidsflyten skal også gjøre det mulig å sende en e-post til økonomiteamet med den hentede informasjonen.

Nå som du vet hva AI Builder er og hvorfor du bør bruke det, la oss se på hvordan du kan bruke AI-modellen for fakturabehandling i AI Builder, som vi dekket tidligere, for å bygge en arbeidsflyt som vil hjelpe økonomiteamet med å behandle fakturaer.

For å bygge en arbeidsflyt som vil hjelpe økonomiteamet med å behandle fakturaer ved hjelp av AI-modellen for fakturabehandling i AI Builder, følg trinnene nedenfor:

1. Gå til [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) startsiden.

2. Bruk tekstområdet på startsiden til å beskrive arbeidsflyten du vil bygge. For eksempel, **_Process an invoice when it arrives in my mailbox_**. Klikk på **Send**-knappen for å sende prompten til AI Copilot.

   ![Copilot power automate](../../../translated_images/no/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot vil foreslå handlingene du trenger for å utføre oppgaven du vil automatisere. Du kan klikke på **Next**-knappen for å gå gjennom neste trinn.

4. I neste trinn vil Power Automate be deg sette opp tilkoblingene som kreves for flyten. Når du er ferdig, klikker du på **Create flow**-knappen for å opprette flyten.

5. AI Copilot vil generere en flyt, og du kan deretter tilpasse flyten til dine behov.

6. Oppdater utløseren for flyten og sett **Mappe** til mappen der fakturaene skal lagres. For eksempel kan du sette mappen til **Inbox**. Klikk på **Show advanced options** og sett **Only with Attachments** til **Yes**. Dette sikrer at flyten bare kjører når en e-post med vedlegg mottas i mappen.

7. Fjern følgende handlinger fra flyten: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** og **Compose 4** fordi du ikke skal bruke dem.

8. Fjern **Condition**-handlingen fra flyten fordi du ikke skal bruke den. Det skal se ut som skjermbildet nedenfor:

   ![power automate, remove actions](../../../translated_images/no/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klikk på **Add an action**-knappen og søk etter **Dataverse**. Velg handlingen **Add a new row**.

10. På handlingen **Extract Information from invoices**, oppdater **Invoice File** til å peke til **Attachment Content** fra e-posten. Dette sikrer at flyten henter informasjon fra fakturavedlegget.

11. Velg **Tabellen** du opprettet tidligere. For eksempel kan du velge tabellen **Invoice Information**. Velg det dynamiske innholdet fra forrige handling for å fylle inn følgende felt:

    - ID
    - Beløp
    - Dato
    - Navn
    - Status - Sett **Status** til **Pending**.
    - Leverandørens e-post - Bruk det dynamiske innholdet **From** fra utløseren **When a new email arrives**.

    ![power automate add row](../../../translated_images/no/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Når du er ferdig med flyten, klikker du på **Save**-knappen for å lagre flyten. Du kan deretter teste flyten ved å sende en e-post med en faktura til mappen du angav i utløseren.

> **Din lekse**: Flyten du nettopp bygde er en god start, nå må du tenke på hvordan du kan bygge en automatisering som gjør det mulig for økonomiteamet vårt å sende en e-post til leverandøren for å oppdatere dem om statusen på fakturaen. Tipset ditt: flyten må kjøre når statusen på fakturaen endres.

## Bruk en tekstgenererings-AI-modell i Power Automate

AI-modellen Create Text with GPT i AI Builder gjør det mulig å generere tekst basert på en prompt og drives av Microsoft Azure OpenAI-tjenesten. Med denne funksjonaliteten kan du integrere GPT (Generative Pre-Trained Transformer)-teknologi i appene og flytene dine for å bygge ulike automatiserte flyter og innsiktsfulle applikasjoner.

GPT-modeller gjennomgår omfattende trening på store mengder data, noe som gjør dem i stand til å produsere tekst som ligner menneskelig språk når de får en prompt. Når de er integrert med arbeidsflytautomatisering, kan AI-modeller som GPT brukes til å effektivisere og automatisere et bredt spekter av oppgaver.

For eksempel kan du bygge flyter som automatisk genererer tekst for ulike bruksområder, som utkast til e-poster, produktbeskrivelser og mer. Du kan også bruke modellen til å generere tekst for ulike apper, som chatboter og kundeserviceapper som gjør det mulig for kundeservicemedarbeidere å svare effektivt og raskt på kundehenvendelser.

![create a prompt](../../../translated_images/no/create-prompt-gpt.69d429300c2e870a.webp)


For å lære hvordan du bruker denne AI-modellen i Power Automate, gå gjennom [Legg til intelligens med AI Builder og GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) modulen.

## Flott jobbet! Fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å forbedre din kunnskap om Generativ AI!

Vil du tilpasse og få mer ut av Copilot? Utforsk [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — en fellesskapsbidratt samling av instruksjoner, agenter, ferdigheter og konfigurasjoner som hjelper deg med å få mest mulig ut av GitHub Copilot.

Gå videre til Leksjon 11 hvor vi ser på hvordan du kan [integrere Generativ AI med funksjonsanrop](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->