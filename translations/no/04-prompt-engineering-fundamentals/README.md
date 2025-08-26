<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcbaaae026cb50fee071e690685b5843",
  "translation_date": "2025-08-26T17:37:03+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "no"
}
-->
# Grunnleggende om Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.no.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introduksjon
Dette modulen dekker viktige konsepter og teknikker for å lage effektive prompt til generative AI-modeller. Måten du skriver prompten til en LLM på har også mye å si. En nøye utformet prompt kan gi bedre kvalitet på svaret. Men hva betyr egentlig begreper som _prompt_ og _prompt engineering_? Og hvordan kan jeg forbedre prompt-_inputen_ jeg sender til LLM-en? Dette er spørsmålene vi skal prøve å svare på i dette og neste kapittel.

_Generativ AI_ kan lage nytt innhold (f.eks. tekst, bilder, lyd, kode osv.) som svar på brukerforespørsler. Dette gjøres ved hjelp av _Large Language Models_ som OpenAIs GPT-serie ("Generative Pre-trained Transformer") som er trent til å bruke naturlig språk og kode.

Brukere kan nå samhandle med disse modellene gjennom kjente grensesnitt som chat, uten å trenge teknisk kunnskap eller opplæring. Modellene er _prompt-baserte_ – brukeren sender inn en tekst (prompt) og får AI-svaret (completion) tilbake. De kan så "chatte med AI-en" i flere runder, og forbedre prompten til svaret matcher forventningene.

"Prompts" har dermed blitt det viktigste _programmeringsgrensesnittet_ for generative AI-apper, og forteller modellene hva de skal gjøre og påvirker kvaliteten på svarene. "Prompt Engineering" er et raskt voksende fagfelt som handler om _design og optimalisering_ av prompts for å levere konsistente og gode svar i stor skala.

## Læringsmål

I denne leksjonen lærer vi hva Prompt Engineering er, hvorfor det er viktig, og hvordan vi kan lage mer effektive prompts for en gitt modell og applikasjonsmål. Vi går gjennom sentrale konsepter og beste praksis for prompt engineering – og blir kjent med et interaktivt Jupyter Notebooks "sandbox"-miljø hvor vi kan se disse konseptene i praksis med ekte eksempler.

Etter denne leksjonen skal du kunne:

1. Forklare hva prompt engineering er og hvorfor det er viktig.
2. Beskrive komponentene i en prompt og hvordan de brukes.
3. Lære beste praksis og teknikker for prompt engineering.
4. Bruke lærte teknikker på ekte eksempler, med en OpenAI-endepunkt.

## Viktige begreper

Prompt Engineering: Praksisen med å designe og forbedre input for å styre AI-modeller mot ønskede resultater.
Tokenisering: Prosessen med å gjøre om tekst til mindre enheter, kalt tokens, som en modell kan forstå og behandle.
Instruction-Tuned LLMs: Store språkmodeller (LLMs) som er finjustert med spesifikke instruksjoner for å forbedre nøyaktighet og relevans i svarene.

## Lærings-sandkasse

Prompt engineering er foreløpig mer kunst enn vitenskap. Den beste måten å utvikle intuisjon på, er å _øve mye_ og bruke en prøv-og-feil-tilnærming som kombinerer domenekunnskap med anbefalte teknikker og modellspesifikke optimaliseringer.

Jupyter-notebooken som følger med denne leksjonen gir deg et _sandkasse_-miljø hvor du kan teste det du lærer – underveis eller som del av kodeutfordringen til slutt. For å kjøre øvelsene trenger du:

1. **En Azure OpenAI API-nøkkel** – tjenesteendepunktet for en utplassert LLM.
2. **Et Python-miljø** – hvor notebooken kan kjøres.
3. **Lokale miljøvariabler** – _fullfør [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)-stegene nå for å bli klar_.

Notatboken har _startøvelser_ – men du oppfordres til å legge til egne _Markdown_- (beskrivelse) og _Kode_- (prompt-forespørsler) seksjoner for å teste flere eksempler eller ideer – og bygge opp din egen intuisjon for prompt-design.

## Illustrert guide

Vil du få oversikt over hva denne leksjonen dekker før du setter i gang? Ta en titt på denne illustrerte guiden, som gir deg et inntrykk av hovedtemaene og viktige poenger du bør tenke på i hver del. Leksjonskartet tar deg fra å forstå kjernebegrepene og utfordringene til å løse dem med relevante prompt engineering-teknikker og beste praksis. Merk at delen "Advanced Techniques" i denne guiden viser til innhold som dekkes i _neste_ kapittel av dette kurset.

![Illustrated Guide to Prompt Engineering](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.no.png)

## Vår startup

La oss se hvordan _dette temaet_ henger sammen med vår startup-misjon om å [bringe AI-innovasjon til utdanning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker å bygge AI-drevne applikasjoner for _personlig tilpasset læring_ – så la oss tenke på hvordan ulike brukere av appen vår kan "designe" prompts:

- **Administratorer** kan be AI-en _analysere læreplan-data for å finne hull i dekningen_. AI-en kan oppsummere resultatene eller visualisere dem med kode.
- **Lærere** kan be AI-en _lage en undervisningsplan for en bestemt målgruppe og tema_. AI-en kan lage en personlig plan i ønsket format.
- **Elever** kan be AI-en _hjelpe dem med et vanskelig fag_. AI-en kan nå veilede eleven med leksjoner, hint og eksempler tilpasset deres nivå.

Dette er bare starten. Sjekk ut [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et åpent bibliotek med prompts kuratert av utdanningseksperter – for å få et bredere inntrykk av mulighetene! _Prøv å kjøre noen av disse promptene i sandkassen eller i OpenAI Playground for å se hva som skjer!_

<!--
LESSON TEMPLATE:
Denne enheten bør dekke kjernebegrep #1.
Forsterk begrepet med eksempler og referanser.

KONSEPT #1:
Prompt Engineering.
Definer det og forklar hvorfor det trengs.
-->

## Hva er Prompt Engineering?

Vi startet denne leksjonen med å definere **Prompt Engineering** som prosessen med å _designe og optimalisere_ tekstinput (prompts) for å levere konsistente og gode svar (completions) for et gitt applikasjonsmål og modell. Vi kan se på dette som en 2-stegs prosess:

- _designe_ den første prompten for en gitt modell og mål
- _forbedre_ prompten stegvis for å øke kvaliteten på svaret

Dette er nødvendigvis en prøv-og-feil-prosess som krever brukerens intuisjon og innsats for å få best mulig resultat. Men hvorfor er det viktig? For å svare på det må vi først forstå tre begreper:

- _Tokenisering_ = hvordan modellen "ser" prompten
- _Base LLMs_ = hvordan grunnmodellen "behandler" en prompt
- _Instruction-Tuned LLMs_ = hvordan modellen nå kan se "oppgaver"

### Tokenisering

En LLM ser prompts som en _sekvens av tokens_ der ulike modeller (eller versjoner av en modell) kan tokenisere samme prompt på ulike måter. Siden LLM-er er trent på tokens (og ikke rå tekst), har måten prompts blir tokenisert på direkte innvirkning på kvaliteten på det genererte svaret.

For å få en følelse av hvordan tokenisering fungerer, kan du prøve verktøy som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist under. Lim inn prompten din – og se hvordan den blir gjort om til tokens, og legg merke til hvordan mellomrom og tegnsetting håndteres. Merk at dette eksempelet viser en eldre LLM (GPT-3) – så å prøve dette med en nyere modell kan gi et annet resultat.

![Tokenization](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.no.png)

### Konsept: Grunnmodeller

Når en prompt er tokenisert, er hovedfunksjonen til ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grunnmodell) å forutsi neste token i sekvensen. Siden LLM-er er trent på enorme tekstmengder, har de god oversikt over statistiske sammenhenger mellom tokens og kan gjøre denne forutsigelsen med en viss sikkerhet. Merk at de ikke forstår _meningen_ med ordene i prompten eller tokenet; de ser bare et mønster de kan "fullføre" med neste forutsigelse. De kan fortsette å forutsi sekvensen til brukeren stopper dem eller en forhåndsdefinert betingelse er oppfylt.

Vil du se hvordan prompt-basert fullføring fungerer? Skriv inn prompten over i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinnstillinger. Systemet er satt opp til å behandle prompts som forespørsler om informasjon – så du bør få et svar som passer til denne konteksten.

Men hva om brukeren ønsker å se noe spesifikt som oppfyller visse kriterier eller oppgavemål? Det er her _instruction-tuned_ LLMs kommer inn i bildet.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.no.png)

### Konsept: Instruction Tuned LLMs

En [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grunnmodellen og finjusterer den med eksempler eller input/output-par (f.eks. samtaler med flere meldinger) som kan inneholde tydelige instruksjoner – og AI-svaret prøver å følge denne instruksjonen.

Dette bruker teknikker som Reinforcement Learning with Human Feedback (RLHF) som kan trene modellen til å _følge instruksjoner_ og _lære av tilbakemeldinger_ slik at den gir svar som er bedre egnet til praktiske bruksområder og mer relevante for brukerens mål.

La oss prøve det – bruk prompten over igjen, men endre nå _systemmeldingen_ til å gi følgende instruksjon som kontekst:

> _Oppsummer innholdet du får for en andreklassing. Hold resultatet til ett avsnitt med 3-5 punktlister._

Ser du hvordan resultatet nå er tilpasset ønsket mål og format? En lærer kan nå bruke dette svaret direkte i presentasjonen for den klassen.

![Instruction Tuned LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.no.png)

## Hvorfor trenger vi Prompt Engineering?

Nå som vi vet hvordan prompts behandles av LLM-er, la oss snakke om _hvorfor_ vi trenger prompt engineering. Svaret ligger i at dagens LLM-er har flere utfordringer som gjør det _vanskeligere å få pålitelige og konsistente svar_ uten å legge innsats i utforming og optimalisering av prompts. For eksempel:

1. **Modellsvar er stokastiske.** _Samme prompt_ vil sannsynligvis gi ulike svar med forskjellige modeller eller modellversjoner. Og det kan til og med gi ulike resultater med _samme modell_ til forskjellige tider. _Prompt engineering-teknikker kan hjelpe oss å minimere disse variasjonene ved å gi bedre rammer._

1. **Modeller kan finne på svar.** Modellene er forhåndstrent på _store, men begrensede_ datasett, noe som betyr at de mangler kunnskap om konsepter utenfor treningsgrunnlaget. Derfor kan de gi svar som er unøyaktige, oppdiktede eller direkte i strid med kjente fakta. _Prompt engineering-teknikker hjelper brukere å oppdage og redusere slike oppdiktede svar, for eksempel ved å be AI-en om kilder eller resonnement._

1. **Modellenes evner vil variere.** Nyere modeller eller generasjoner har flere muligheter, men kan også ha egne særegenheter og kompromisser i kostnad og kompleksitet. _Prompt engineering kan hjelpe oss å utvikle beste praksis og arbeidsflyter som skjuler forskjeller og tilpasser seg modellspesifikke krav på en skalerbar og sømløs måte._

La oss se dette i praksis i OpenAI eller Azure OpenAI Playground:

- Bruk samme prompt med ulike LLM-implementasjoner (f.eks. OpenAI, Azure OpenAI, Hugging Face) – ser du variasjonene?
- Bruk samme prompt flere ganger med _samme_ LLM-implementasjon (f.eks. Azure OpenAI playground) – hvordan varierte svarene?

### Eksempel på oppdiktede svar

I dette kurset bruker vi begrepet **"fabrication"** for å beskrive fenomenet der LLM-er noen ganger genererer faktuelt feil informasjon på grunn av begrensninger i treningen eller andre forhold. Du har kanskje også hørt dette omtalt som _"hallusinasjoner"_ i artikler eller forskningsartikler. Vi anbefaler imidlertid å bruke _"fabrication"_ for å unngå å tillegge maskinen menneskelige egenskaper. Dette støtter også [Retningslinjer for ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologiperspektiv, og fjerner begreper som kan oppfattes som støtende eller ekskluderende i noen sammenhenger.

Vil du se hvordan oppdiktede svar fungerer? Tenk ut en prompt som ber AI-en lage innhold om et ikke-eksisterende tema (slik at det ikke finnes i treningsdataene). For eksempel – jeg prøvde denne prompten:
# Undervisningsplan: Den martianske krigen i 2076

## Mål

- Forstå de viktigste hendelsene og årsakene til den martianske krigen i 2076.
- Utforske de politiske, sosiale og teknologiske konsekvensene av konflikten.
- Analysere hvordan krigen påvirket forholdet mellom Jorden og Mars.

## Introduksjon

Den martianske krigen i 2076 var en avgjørende konflikt mellom koloniene på Mars og myndighetene på Jorden. Krigen endret maktbalansen i solsystemet og førte til store endringer i både teknologi og samfunn.

## Leksjonens innhold

### 1. Bakgrunn og årsaker

- Diskuter de økonomiske og politiske spenningene mellom Mars og Jorden.
- Undersøk hvordan ressursmangel og økende uavhengighetsbevegelser på Mars bidro til konflikten.
- Se på de første tegnene til opprør og hvordan de ble håndtert av jordiske myndigheter.

### 2. Viktige hendelser under krigen

- Gå gjennom de største slagene, inkludert Slaget om Olympus Mons og beleiringen av New Valles.
- Diskuter bruken av avansert teknologi, som autonome droner og energivåpen.
- Analyser strategiene til begge sider og hvordan de påvirket krigens utfall.

### 3. Konsekvenser og etterspill

- Utforsk de politiske endringene etter krigen, inkludert Mars’ uavhengighetserklæring.
- Diskuter de sosiale og økonomiske effektene på både Mars og Jorden.
- Vurder hvordan krigen førte til nye diplomatiske og teknologiske samarbeid.

## Aktiviteter

- Grupperefleksjon: Del klassen inn i grupper for å diskutere hvordan krigen kunne vært unngått.
- Tidslinje: Lag en tidslinje over de viktigste hendelsene under krigen.
- Debatt: Arranger en debatt om hvorvidt Mars burde ha fått uavhengighet.

## Vurdering

- Skriftlig oppgave: Skriv en rapport om en av de sentrale hendelsene i krigen og dens betydning.
- Presentasjon: Presenter en analyse av krigens langsiktige konsekvenser for solsystemet.

## Ressurser

- Anbefalte bøker og artikler om den martianske krigen i 2076.
- Dokumentarer og intervjuer med historikere og eksperter på rompolitikk.

## Oppsummering

Den martianske krigen i 2076 var en milepæl i menneskehetens historie. Gjennom denne leksjonen har vi sett på årsakene, hendelsene og konsekvensene av konflikten, og reflektert over hvordan den har formet fremtiden for både Mars og Jorden.
Et nettsøk viste meg at det finnes fiktive beretninger (f.eks. TV-serier eller bøker) om kriger på Mars – men ingen fra 2076. Sunn fornuft tilsier også at 2076 er _i fremtiden_, og derfor ikke kan knyttes til en virkelig hendelse.

Så hva skjer når vi kjører denne prompten hos ulike LLM-leverandører?

> **Respons 1**: OpenAI Playground (GPT-35)

![Respons 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.no.png)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Respons 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.no.png)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

![Respons 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.no.png)

Som forventet gir hver modell (eller modellversjon) litt ulike svar, takket være stokastisk oppførsel og variasjoner i modellens evner. For eksempel retter én modell seg mot et publikum på ungdomsskolen, mens en annen antar at brukeren er videregående elev. Men alle tre modellene genererte svar som kunne overbevise en uvitende bruker om at hendelsen var ekte.

Teknikker innen prompt engineering som _metaprompting_ og _temperaturinnstillinger_ kan redusere modellens tendens til å dikte opp ting til en viss grad. Nye _arkitekturer_ for prompt engineering integrerer også nye verktøy og metoder sømløst i promptflyten, for å motvirke eller redusere noen av disse effektene.

## Case Study: GitHub Copilot

La oss avslutte denne delen med å se hvordan prompt engineering brukes i virkelige løsninger, ved å se på ett case: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI-parprogrammerer" – den gjør tekstprompter om til kodeforslag og er integrert i utviklingsmiljøet ditt (f.eks. Visual Studio Code) for en sømløs brukeropplevelse. Som dokumentert i bloggserien under, var den første versjonen basert på OpenAI Codex-modellen – og ingeniørene innså raskt behovet for å finjustere modellen og utvikle bedre prompt engineering-teknikker for å forbedre kodekvaliteten. I juli [lanserte de en forbedret AI-modell som går utover Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for enda raskere forslag.

Les innleggene i rekkefølge for å følge deres læringsreise.

- **Mai 2023** | [GitHub Copilot blir bedre til å forstå koden din](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inne i GitHub: Arbeid med LLM-ene bak GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Slik skriver du bedre promter for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juli 2023** | [.. GitHub Copilot går utover Codex med forbedret AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juli 2023** | [En utviklers guide til prompt engineering og LLM-er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Slik bygger du en bedriftsapp med LLM: Lærdom fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også bla gjennom deres [Engineering-blogg](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere innlegg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som viser hvordan disse modellene og teknikkene _brukes_ for å drive reelle applikasjoner.

---

<!--
LEKSJONSMAL:
Denne enheten skal dekke kjernebegrep #2.
Styrk begrepet med eksempler og referanser.

KONSEPT #2:
Promptdesign.
Illustrert med eksempler.
-->

## Oppbygging av promter

Vi har sett hvorfor prompt engineering er viktig – nå skal vi forstå hvordan promter _bygges opp_ slik at vi kan vurdere ulike teknikker for mer effektiv promptdesign.

### Enkel prompt

La oss starte med den enkle prompten: et tekstinnspill sendt til modellen uten annen kontekst. Her er et eksempel – når vi sender de første ordene fra USAs nasjonalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) fullfører den straks svaret med de neste linjene, og illustrerer den grunnleggende prediksjonsatferden.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det høres ut som du begynner på teksten til "The Star-Spangled Banner", USAs nasjonalsang. Hele teksten er ... |

### Kompleks prompt

Nå legger vi til kontekst og instruksjoner til den enkle prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lar oss bygge en kompleks prompt som en samling _meldinger_ med:

- Input/output-par som gjenspeiler _brukerens_ innspill og _assistentens_ svar.
- Systemmelding som setter konteksten for assistentens oppførsel eller personlighet.

Forespørselen ser nå ut som under, der _tokeniseringen_ effektivt fanger relevant informasjon fra kontekst og samtale. Å endre systemkonteksten kan nå ha like stor innvirkning på kvaliteten på svarene som brukerens innspill.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruksjonsprompt

I eksemplene over var brukerens prompt et enkelt tekstspørsmål som kan tolkes som en forespørsel om informasjon. Med _instruksjonspromter_ kan vi bruke teksten til å spesifisere en oppgave mer detaljert, og gi bedre veiledning til AI-en. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Skriv en beskrivelse av den amerikanske borgerkrigen                                                                                                                                                                                   | _returnerte et enkelt avsnitt_                                                                                             | Enkel               |
| Skriv en beskrivelse av den amerikanske borgerkrigen. Oppgi viktige datoer og hendelser og beskriv deres betydning                                                                                                                     | _returnerte et avsnitt etterfulgt av en liste med viktige datoer og beskrivelser_                                          | Kompleks            |
| Skriv en beskrivelse av den amerikanske borgerkrigen i ett avsnitt. Oppgi 3 punkter med viktige datoer og deres betydning. Oppgi 3 punkter med sentrale historiske personer og deres bidrag. Returner svaret som en JSON-fil            | _returnerer mer omfattende detaljer i en tekstboks, formatert som JSON som du kan kopiere til en fil og validere ved behov_ | Kompleks. Formatert. |

## Primært innhold

I eksemplene over var prompten fortsatt ganske åpen, og lot LLM-en bestemme hvilken del av det forhåndstrente datasettet som var relevant. Med _primært innhold_-mønsteret deles innholdet i to deler:

- en instruksjon (handling)
- relevant innhold (som påvirker handlingen)

Her er et eksempel der instruksjonen er "oppsummer dette i 2 setninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger så stor som alle de andre planetene til sammen. Jupiter er et av de klareste objektene synlig for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historisk tid. Den er oppkalt etter den romerske guden Jupiter.[19] Sett fra jorden kan Jupiter være så lyssterk at det reflekterte lyset kaster synlige skygger,[20] og er i snitt det tredje klareste naturlige objektet på nattehimmelen etter månen og Venus. <br/> **Oppsummer dette i 2 korte setninger** | Jupiter, den femte planeten fra solen, er den største i solsystemet og kjent for å være et av de klareste objektene på nattehimmelen. Oppkalt etter den romerske guden Jupiter, er den en gasskjempe med en masse som er to og en halv ganger så stor som alle de andre planetene til sammen. |

Segmentet med primært innhold kan brukes på ulike måter for å gi mer effektive instruksjoner:

- **Eksempler** – i stedet for å fortelle modellen hva den skal gjøre med en eksplisitt instruksjon, gir du den eksempler på ønsket utdata og lar den utlede mønsteret.
- **Cues** – følg instruksjonen med et "hint" som gir modellen et startpunkt, og leder den mot mer relevante svar.
- **Maler** – dette er repeterbare 'oppskrifter' for promter med plassholdere (variabler) som kan tilpasses med data for spesifikke bruksområder.

La oss se nærmere på disse i praksis.

### Bruk av eksempler

Dette er en metode der du bruker primært innhold til å "mate modellen" med noen eksempler på ønsket utdata for en gitt instruksjon, og lar den utlede mønsteret for ønsket utdata. Avhengig av antall eksempler kan vi ha zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nå av tre komponenter:

- En oppgavebeskrivelse
- Noen eksempler på ønsket utdata
- Starten på et nytt eksempel (som blir en implisitt oppgavebeskrivelse)

| Læringstype | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot   | "The Sun is Shining". Oversett til spansk                                                                                                             | "El Sol está brillando".    |
| One-shot    | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot    | Spilleren løp basene => Baseball <br/> Spilleren slo et ess => Tennis <br/> Spilleren slo en sekser => Cricket <br/> Spilleren gjorde en slam-dunk => | Basketball                  |
|             |                                                                                                                                                       |                             |

Legg merke til at vi måtte gi eksplisitt instruksjon ("Oversett til spansk") i zero-shot prompting, men at det blir utledet i one-shot eksempelet. Few-shot eksempelet viser hvordan flere eksempler gir modellen mulighet til å gjøre mer presise slutninger uten ekstra instruksjoner.

### Prompt-hint

En annen teknikk for å bruke primært innhold er å gi _hint_ i stedet for eksempler. Her gir vi modellen et lite dytt i riktig retning ved å _starte_ med et utdrag som gjenspeiler ønsket svarformat. Modellen "tar hintet" og fortsetter i samme stil.

| Antall hint | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0           | Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger så stor som alle de andre planetene til sammen. Jupiter er et av de klareste objektene synlig for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historisk tid.

**Oppsummer Dette**                                       | Jupiter er den største planeten i vårt solsystem og den femte fra sola. Det er en gasskjempe med en masse på 1/1000 av solas, men den er tyngre enn alle de andre planetene til sammen. Gamle sivilisasjoner har kjent til Jupiter i lang tid, og den er lett synlig på nattehimmelen. |
| 1              | Jupiter er den femte planeten fra sola og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solas, men to og en halv ganger så stor som alle de andre planetene i solsystemet til sammen. Jupiter er et av de klareste objektene som er synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historien ble skrevet. <br/>**Oppsummer Dette** <br/> Det vi lærte er at Jupiter | er den femte planeten fra sola og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solas, men to og en halv ganger så stor som alle de andre planetene til sammen. Den er lett synlig for det blotte øye og har vært kjent siden oldtiden.                        |
| 2              | Jupiter er den femte planeten fra sola og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solas, men to og en halv ganger så stor som alle de andre planetene i solsystemet til sammen. Jupiter er et av de klareste objektene som er synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historien ble skrevet. <br/>**Oppsummer Dette** <br/> Topp 3 fakta vi lærte:         | 1. Jupiter er den femte planeten fra sola og den største i solsystemet. <br/> 2. Det er en gasskjempe med en masse som er en tusendel av solas...<br/> 3. Jupiter har vært synlig for det blotte øye siden oldtiden ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Promptmaler

En promptmal er en _forhåndsdefinert oppskrift på en prompt_ som kan lagres og gjenbrukes etter behov, for å skape mer konsistente brukeropplevelser i stor skala. I sin enkleste form er det bare en samling av prompteksempler som [dette fra OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) som gir både de interaktive promptkomponentene (bruker- og systemmeldinger) og det API-drevne forespørselsformatet – for å støtte gjenbruk.

I en mer avansert form, som [dette eksempelet fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), inneholder den _plassholdere_ som kan erstattes med data fra ulike kilder (brukerinndata, systemkontekst, eksterne datakilder osv.) for å generere en prompt dynamisk. Dette lar oss lage et bibliotek av gjenbrukbare prompts som kan brukes til å skape konsistente brukeropplevelser **programmatisk** i stor skala.

Den virkelige verdien av maler ligger til slutt i muligheten til å lage og publisere _promptbiblioteker_ for spesifikke bruksområder – der promptmalen nå er _optimalisert_ for å reflektere applikasjonsspesifikk kontekst eller eksempler som gjør svarene mer relevante og presise for den tiltenkte brukergruppen. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) er et godt eksempel på denne tilnærmingen, og samler et bibliotek av prompts for utdanningssektoren med vekt på nøkkelmål som leksjonsplanlegging, læreplanutforming, elevveiledning osv.

## Støtteinnhold

Hvis vi ser på promptkonstruksjon som å ha en instruksjon (oppgave) og et mål (hovedinnhold), så er _sekundært innhold_ som ekstra kontekst vi gir for å **påvirke svaret på en eller annen måte**. Det kan være justeringsparametere, formateringsinstruksjoner, tematiske taksonomier osv. som kan hjelpe modellen å _tilpasse_ svaret sitt slik at det passer brukerens mål eller forventninger.

For eksempel: Gitt en emnekatalog med omfattende metadata (navn, beskrivelse, nivå, metadatamerker, instruktør osv.) på alle tilgjengelige kurs i læreplanen:

- vi kan definere en instruksjon om å "oppsummere emnekatalogen for høsten 2023"
- vi kan bruke hovedinnholdet til å gi noen eksempler på ønsket utdata
- vi kan bruke sekundært innhold til å identifisere de 5 viktigste "taggene" av interesse.

Nå kan modellen gi en oppsummering i formatet vist av eksemplene – men hvis et resultat har flere tagger, kan den prioritere de 5 som er identifisert i sekundært innhold.

---

<!--
LEKSJONSMAL:
Denne enheten bør dekke kjernebegrep #1.
Forsterk begrepet med eksempler og referanser.

BEGREP #3:
Prompt Engineering-teknikker.
Hva er noen grunnleggende teknikker for prompt engineering?
Illustrer med noen øvelser.
-->

## Beste praksis for prompting

Nå som vi vet hvordan prompts kan _bygges opp_, kan vi begynne å tenke på hvordan vi kan _designe_ dem for å følge beste praksis. Vi kan se på dette i to deler – å ha riktig _tankesett_ og bruke riktige _teknikker_.

### Tankesett for Prompt Engineering

Prompt Engineering er en prøving-og-feiling-prosess, så husk tre brede retningslinjer:

1. **Domeneinnsikt er viktig.** Svarets nøyaktighet og relevans avhenger av _domenet_ applikasjonen eller brukeren opererer i. Bruk din intuisjon og fagkunnskap til å **tilpasse teknikker** ytterligere. For eksempel, definer _domene-spesifikke personligheter_ i systemprompts, eller bruk _domene-spesifikke maler_ i brukerprompts. Gi sekundært innhold som reflekterer domene-spesifikk kontekst, eller bruk _domene-spesifikke signaler og eksempler_ for å veilede modellen mot kjente bruksmønstre.

2. **Forståelse av modellen er viktig.** Vi vet at modeller er stokastiske av natur. Men modellimplementasjoner kan også variere når det gjelder treningsdatasettet de bruker (forhåndstrent kunnskap), hvilke muligheter de gir (f.eks. via API eller SDK) og hvilken type innhold de er optimalisert for (f.eks. kode vs. bilder vs. tekst). Forstå styrker og begrensninger ved modellen du bruker, og bruk den kunnskapen til å _prioritere oppgaver_ eller bygge _tilpassede maler_ som er optimalisert for modellens egenskaper.

3. **Iterasjon og validering er viktig.** Modeller utvikler seg raskt, og det gjør også teknikkene for prompt engineering. Som fagekspert har du kanskje annen kontekst eller kriterier for _din_ spesifikke applikasjon, som ikke gjelder for resten av miljøet. Bruk verktøy og teknikker for prompt engineering for å "kickstarte" promptkonstruksjon, og iterer og valider resultatene med din egen intuisjon og fagkunnskap. Noter innsiktene dine og lag en **kunnskapsbase** (f.eks. promptbiblioteker) som andre kan bruke som et nytt utgangspunkt for raskere iterasjoner i fremtiden.

## Beste praksis

La oss se på vanlige beste praksiser som anbefales av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Hva                              | Hvorfor                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluer de nyeste modellene.       | Nye modellgenerasjoner har sannsynligvis bedre funksjoner og kvalitet – men kan også koste mer. Vurder effekten, og ta deretter en beslutning om å bytte.                                                                                |
| Skill instruksjoner og kontekst   | Sjekk om modellen/leverandøren din definerer _avgrensere_ for å skille instruksjoner, hoved- og sekundærinnhold tydeligere. Dette kan hjelpe modeller å tildele vekt mer nøyaktig til tokens.                                                         |
| Vær spesifikk og tydelig             | Gi flere detaljer om ønsket kontekst, resultat, lengde, format, stil osv. Dette vil forbedre både kvaliteten og konsistensen på svarene. Ta vare på oppskrifter i gjenbrukbare maler.                                                          |
| Vær beskrivende, bruk eksempler      | Modeller kan svare bedre på en "vis og fortell"-tilnærming. Start med en `zero-shot`-tilnærming der du gir en instruksjon (men ingen eksempler), og prøv deretter `few-shot` som en forbedring, med noen eksempler på ønsket utdata. Bruk analogier. |
| Bruk signaler for å starte svar | Dytt modellen mot ønsket resultat ved å gi noen ledende ord eller fraser som den kan bruke som utgangspunkt for svaret.                                                                                                               |
| Gjenta instruksjoner                       | Noen ganger må du kanskje gjenta deg selv for modellen. Gi instruksjoner både før og etter hovedinnholdet, bruk en instruksjon og et signal, osv. Iterer og valider for å se hva som fungerer.                                                         |
| Rekkefølge har betydning                     | Rekkefølgen du presenterer informasjon til modellen i, kan påvirke svaret, også i eksemplene, på grunn av "recency bias". Prøv ulike alternativer for å se hva som fungerer best.                                                               |
| Gi modellen en “utvei”           | Gi modellen et _fallback_-svar den kan bruke hvis den ikke kan fullføre oppgaven. Dette kan redusere sjansen for at modellen genererer feilaktige eller oppdiktede svar.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Som med all beste praksis, husk at _dine erfaringer kan variere_ avhengig av modell, oppgave og domene. Bruk dette som et utgangspunkt, og iterer for å finne det som fungerer best for deg. Evaluer prompt engineering-prosessen din jevnlig etter hvert som nye modeller og verktøy blir tilgjengelige, med fokus på skalerbarhet og kvalitet på svarene.

<!--
LEKSJONSMAL:
Denne enheten bør gi en kodeutfordring hvis aktuelt

UTFORDRING:
Lenke til en Jupyter Notebook med kun kodekommentarer i instruksjonene (kodene er tomme).

LØSNING:
Lenke til en kopi av den Notebooken med prompts fylt ut og kjørt, som viser et eksempel på løsning.
-->

## Oppgave

Gratulerer! Du har kommet til slutten av leksjonen! Nå er det på tide å teste ut noen av konseptene og teknikkene med ekte eksempler!

I denne oppgaven bruker vi en Jupyter Notebook med øvelser du kan løse interaktivt. Du kan også utvide Notebooken med egne Markdown- og kodeceller for å utforske ideer og teknikker på egenhånd.

### For å komme i gang, lag en fork av repoet, og deretter

- (Anbefalt) Start GitHub Codespaces
- (Alternativt) Klon repoet til din lokale enhet og bruk det med Docker Desktop
- (Alternativt) Åpne Notebooken med ditt foretrukne Notebook-miljø.

### Deretter, konfigurer miljøvariablene dine

- Kopier `.env.copy`-filen i rotmappen til `.env` og fyll inn verdiene for `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT`. Gå tilbake til [Learning Sandbox-delen](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) for å lære hvordan.

### Deretter, åpne Jupyter Notebooken

- Velg runtime-kjernen. Hvis du bruker alternativ 1 eller 2, velg bare standard Python 3.10.x-kjernen som følger med dev-containeren.

Nå er du klar til å kjøre øvelsene. Merk at det ikke finnes _riktige eller gale_ svar her – det handler om å utforske alternativer gjennom prøving og feiling og bygge opp intuisjon for hva som fungerer for en gitt modell og applikasjonsdomene.

_Derfor er det ingen kodefasit-segmenter i denne leksjonen. I stedet vil Notebooken ha Markdown-celler med tittelen "Min løsning:" som viser ett eksempel på utdata til referanse._

 <!--
LEKSJONSMAL:
Avslutt seksjonen med en oppsummering og ressurser for selvstudium.
-->

## Kunnskapssjekk

Hvilken av følgende er en god prompt som følger noen fornuftige beste praksiser?

1. Vis meg et bilde av en rød bil
2. Vis meg et bilde av en rød bil av merket Volvo og modellen XC90 parkert ved en klippe med solnedgang
3. Vis meg et bilde av en rød bil av merket Volvo og modellen XC90

A: 2, det er den beste prompten fordi den gir detaljer om "hva" og går i dybden (ikke bare hvilken som helst bil, men et spesifikt merke og modell) og den beskriver også omgivelsene. 3 er nest best fordi den også inneholder mye beskrivelse.

## 🚀 Utfordring

Se om du kan bruke "signal"-teknikken med prompten: Fullfør setningen "Vis meg et bilde av en rød bil av merket Volvo og ". Hva svarer den, og hvordan ville du forbedret det?

## Flott jobbet! Fortsett læringen din

Vil du lære mer om ulike konsepter innen Prompt Engineering? Gå til [videre læring-siden](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å finne flere gode ressurser om dette emnet.

Gå videre til leksjon 5 hvor vi ser på [avanserte prompting-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.