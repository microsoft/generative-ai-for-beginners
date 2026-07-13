# Grunnleggende om Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/no/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduksjon
Denne modulen dekker grunnleggende konsepter og teknikker for å lage effektive prompts i generative AI-modeller. Måten du skriver prompten til en LLM på, er også viktig. En nøye utformet prompt kan oppnå bedre kvalitet på responsen. Men hva betyr egentlig begrepene _prompt_ og _prompt engineering_? Og hvordan kan jeg forbedre prompt-_inputen_ jeg sender til LLM-en? Dette er spørsmålene vi skal prøve å besvare i dette kapitlet og det neste.

_Generativ AI_ er i stand til å lage nytt innhold (f.eks. tekst, bilder, lyd, kode osv.) som svar på brukerforespørsler. Den oppnår dette ved å bruke _Store Språkmodeller_ som OpenAIs GPT ("Generative Pre-trained Transformer")-serie som er trent for bruk av naturlig språk og kode.

Brukere kan nå interagere med disse modellene ved hjelp av kjente paradigmer som chat, uten å trenge teknisk ekspertise eller opplæring. Modellene er _prompt-baserte_ – brukere sender inn tekst (prompt) og får tilbake AI-respons (fullføring). De kan deretter "chatte med AI" iterativt, i flerturssamtaler, og forbedre prompten til responsen møter forventningene.

"Prompter" blir nå det primære _programmeringsgrensesnittet_ for generative AI-apper, som forteller modellene hva de skal gjøre og påvirker kvaliteten på de returnerte responsene. "Prompt Engineering" er et raskt voksende fagfelt som fokuserer på _design og optimalisering_ av prompter for å levere konsistente og kvalitetsmessige svar i stor skala.

## Læringsmål

I denne leksjonen lærer vi hva Prompt Engineering er, hvorfor det er viktig, og hvordan vi kan lage mer effektive prompter for en gitt modell og applikasjonsmål. Vi vil forstå kjernebegrepene og beste praksis for prompt engineering – og lære om et interaktivt Jupyter Notebooks "sandbox"-miljø hvor vi kan se disse konseptene anvendt på ekte eksempler.

Mot slutten av denne leksjonen vil vi kunne:

1. Forklare hva prompt engineering er og hvorfor det er viktig.
2. Beskrive komponentene i en prompt og hvordan de brukes.
3. Lære beste praksis og teknikker for prompt engineering.
4. Anvende lærte teknikker på ekte eksempler, ved å bruke et OpenAI-endepunkt.

## Nøkkelbegreper

Prompt Engineering: Praksisen med å designe og forbedre input for å styre AI-modeller mot å produsere ønskede utdata.
Tokenisering: Prosessen med å konvertere tekst til mindre enheter, kalt tokens, som en modell kan forstå og behandle.
Instruksjonsjusterte LLM-er: Store språkmodeller (LLM-er) som er finjustert med spesifikke instrukser for å forbedre presisjonen og relevansen i responsene.

## Læringsmiljø

Prompt engineering er for tiden mer kunst enn vitenskap. Den beste måten å forbedre intuisjonen for det på er å _øve mer_ og bruke en prøving-og-feiling-tilnærming som kombinerer fagspesifikk ekspertise med anbefalte teknikker og modellspesifikke optimaliseringer.

Jupyter Notebook som følger med denne leksjonen tilbyr et _sandbox_-miljø hvor du kan prøve ut det du lærer – enten løpende eller som en del av kodeutfordringen på slutten. For å gjennomføre øvelsene trenger du:

1. **En Azure OpenAI API-nøkkel** – tjenesteendepunkt for en distribuert LLM.
2. **Et Python-runtime** – hvor Notebook kan kjøres.
3. **Lokale miljøvariabler** – _fullfør [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)-stegene nå for å være klar_.

Notatboken inneholder _startøvelser_ – men du oppfordres til å legge til egen _Markdown_ (beskrivelse) og _Kode_ (prompt-forespørsler) seksjoner for å prøve flere eksempler eller ideer – og bygge intuisjon for promptdesign.

## Illustrert guide

Vil du få et overblikk over hva denne leksjonen dekker før du dykker inn? Se denne illustrerte guiden, som gir deg en oversikt over hovedtemaene og nøkkelpunktene du kan reflektere over i hver del. Leksjonsplanen tar deg fra å forstå kjernebegrepene og utfordringene til å adressere dem med relevante prompt engineering-teknikker og beste praksis. Merk at seksjonen "Avanserte teknikker" i denne guiden viser til innhold dekket i det _neste_ kapitlet i denne pensum.

![Illustrated Guide to Prompt Engineering](../../../translated_images/no/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vår Startup

Nå, la oss snakke om hvordan _dette emnet_ relaterer seg til vår startup-oppdrag om å [bringe AI-innovasjon til utdanning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker å bygge AI-drevne applikasjoner for _personlig tilpasset læring_ – så la oss tenke på hvordan ulike brukere av applikasjonen vår kan "designe" prompter:

- **Administratorer** kan be AI om å _analysere læreplandata for å identifisere hull i dekningen_. AI-en kan oppsummere resultater eller visualisere dem med kode.
- **Lærere** kan be AI om å _generere en leksjonsplan for et målrettet publikum og emne_. AI-en kan lage den personlige planen i et spesifisert format.
- **Studenter** kan be AI om å _veilede dem i et vanskelig fag_. AI kan nå veilede studenter med leksjoner, hint og eksempler tilpasset deres nivå.

Dette er bare toppen av isfjellet. Sjekk ut [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et åpen kildekode-bibliotek med prompter kuratert av eksperter innen utdanning – for å få en bredere forståelse av mulighetene! _Prøv å kjøre noen av disse promptene i sandkassen eller bruk OpenAI Playground for å se hva som skjer!_

<!--
LEKSJONS MAL:
Denne enheten bør dekke kjernebegrep #1.
Forsterke konseptet med eksempler og referanser.

KONSEPT #1:
Prompt Engineering.
Definer det og forklar hvorfor det er nødvendig.
-->

## Hva er Prompt Engineering?

Vi startet denne leksjonen med å definere **Prompt Engineering** som prosessen med _å designe og optimalisere_ tekst-input (prompter) for å levere konsistente og kvalitetskvalitative svar (fullføringer) for et gitt applikasjonsmål og modell. Vi kan tenke på dette som en 2-trinns prosess:

- _designe_ den innledende prompten for en gitt modell og målsetting
- _forbedre_ prompten iterativt for å forbedre responskvaliteten

Dette er nødvendigvis en prøve-og-feile-prosess som krever brukerintuisjon og innsats for å oppnå optimale resultater. Så hvorfor er det viktig? For å svare på det må vi først forstå tre konsepter:

- _Tokenisering_ = hvordan modellen "ser" prompten
- _Basis-LLMer_ = hvordan grunnmodellen "behandler" en prompt
- _Instruksjonsjusterte LLMer_ = hvordan modellen nå kan se "oppgaver"

### Tokenisering

En LLM ser prompter som en _sekvens av tokens_ hvor ulike modeller (eller versjoner av en modell) kan tokenisere samme prompt på ulike måter. Siden LLM-er er trent på tokens (og ikke råtekst), påvirker måten prompter tokeniseres på direkte kvaliteten på den genererte responsen.

For å få en intuisjon for hvordan tokenisering fungerer, prøv verktøy som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Lim inn din prompt – og se hvordan den konverteres til tokens, med oppmerksomhet på hvordan mellomromstegn og skilletegn håndteres. Merk at dette eksempelet viser en eldre LLM (GPT-3) – så å prøve dette med en nyere modell kan gi et annet resultat.

![Tokenization](../../../translated_images/no/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsept: Grunnmodeller

Når en prompt er tokenisert, er hovedfunksjonen til ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grunnmodellen) å forutsi token i denne sekvensen. Siden LLM-er er trent på massive tekst datasett, har de en god forståelse av statistiske relasjoner mellom tokens og kan gjøre den prediksjonen med en viss sikkerhet. Merk at de ikke forstår _meningen_ med ordene i prompten eller token; de ser bare et mønster de kan "fullføre" med sin neste prediksjon. De kan fortsette å forutsi sekvensen til den avbrytes av brukeren eller en forhåndsbestemt betingelse.

Vil du se hvordan prompt-basert fullføring fungerer? Skriv inn prompten ovenfor i [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) med standardinnstillinger. Systemet er konfigurert til å behandle prompter som forespørsler om informasjon – så du bør se en fullføring som tilfredsstiller denne konteksten.

Men hva om brukeren ønsket å se noe spesifikt som oppfylte visse kriterier eller oppgave-mål? Her kommer _instruksjonsjusterte_ LLM-er inn i bildet.

![Base LLM Chat Completion](../../../translated_images/no/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsept: Instruksjonsjusterte LLM-er

En [instruksjonsjustert LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grunnmodellen og finjusterer den med eksempler eller input/output-par (f.eks. flerturns "meldinger") som kan inneholde klare instruksjoner – og AI-responsen forsøker å følge denne instruksen.

Dette bruker teknikker som Forsterkningslæring med Menneskelig Tilbakemelding (RLHF) som kan trene modellen til å _følge instruksjoner_ og _lære av tilbakemeldinger_ slik at den produserer svar som er bedre egnet for praktiske applikasjoner og mer relevante for brukermål.

La oss prøve det – gå tilbake til prompten ovenfor, men endre nå _systemmeldingen_ slik at den gir følgende instruksjon som kontekst:

> _Oppsummer innholdet du får for en elev på andre trinn. Hold resultatet til ett avsnitt med 3-5 punktlister._

Ser du hvordan resultatet nå er tilpasset for å reflektere mål og format? En lærer kan nå bruke denne responsen direkte i sine lysbilder for den timen.

![Instruction Tuned LLM Chat Completion](../../../translated_images/no/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Hvorfor trenger vi Prompt Engineering?

Nå som vi vet hvordan prompter behandles av LLM-er, la oss snakke om _hvorfor_ vi trenger prompt engineering. Svaret ligger i at dagens LLM-er byr på en rekke utfordringer som gjør det vanskeligere å oppnå _pålitelige og konsistente fullføringer_ uten innsats i prompt-konstruksjon og optimalisering. For eksempel:

1. **Modellsvar er stokastiske.** Den _samme prompten_ vil sannsynligvis gi ulike svar med forskjellige modeller eller modellversjoner. Og den kan til og med gi ulike resultater med _samme modell_ til ulike tidspunkter. _Prompt engineering-teknikker kan hjelpe oss å minimere disse variasjonene ved å gi bedre rammer_.

1. **Modeller kan fabrikkere svar.** Modeller er forhåndstrent med _store men begrensede_ datasett, noe som betyr at de mangler kunnskap om konsepter utenfor treningsområdet. Som et resultat kan de produsere fullføringer som er unøyaktige, oppdiktede eller direkte motstridende med kjente fakta. _Prompt engineering-teknikker hjelper brukere med å identifisere og begrense slike fabrikasjoner, f.eks. ved å be AI om kilder eller resonnement_.

1. **Modellens evner vil variere.** Nyere modeller eller modellgenerasjoner vil ha rikere evner, men også unike egenskaper og kompromisser i kostnad og kompleksitet. _Prompt engineering kan hjelpe oss å utvikle beste praksis og arbeidsflyter som abstraherer bort forskjeller og tilpasser seg modellspesifikke krav på skalerbare og sømløse måter_.

La oss se dette i praksis i OpenAI- eller Azure OpenAI Playground:

- Bruk samme prompt med forskjellige LLM-distribusjoner (f.eks. OpenAI, Azure OpenAI, Hugging Face) – så du variasjonene?
- Bruk samme prompt flere ganger med _samme_ LLM-distribusjon (f.eks. Azure OpenAI playground) – hvordan skilte disse variasjonene seg?

### Eksempel på fabrikasjoner

I dette kurset bruker vi begrepet **"fabrikasjon"** for å referere til fenomenet der LLM-er noen ganger genererer faktuelt ukorrekt informasjon på grunn av begrensninger i treningen eller andre forhold. Du har kanskje også hørt dette omtalt som _"hallusinasjoner"_ i populære artikler eller forskningsartikler. Vi anbefaler imidlertid sterkt å bruke _"fabrikasjon"_ som term slik at vi ikke utilsiktet antropomorfiserer oppførselen ved å tilskrive et menneskelignende trekk til et maskindrevet resultat. Dette støtter også [retningslinjene for Ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologisk perspektiv, ved å fjerne begreper som kan oppfattes som støtende eller ikke inkluderende i noen sammenhenger.

Vil du få en følelse av hvordan fabrikasjoner fungerer? Tenk på en prompt som instruerer AI til å generere innhold for et ikke-eksisterende emne (for å sikre at det ikke finnes i treningsdatasettet). For eksempel prøvde jeg denne prompten:

> **Prompt:** lag en leksjonsplan om den marsianske krigen i 2076.

Et nettsøk viste at det finnes fiktive beskrivelser (f.eks. TV-serier eller bøker) om marsianske kriger – men ingen i 2076. Sunn fornuft forteller oss også at 2076 er _i fremtiden_ og derfor ikke kan knyttes til en virkelig hendelse.


Så hva skjer når vi kjører denne prompten med forskjellige LLM-leverandører?

> **Svar 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/no/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/no/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/no/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som forventet produserer hver modell (eller modellversjon) litt forskjellige svar takket være stokastisk atferd og variasjoner i modellens kapasitet. For eksempel retter én modell seg mot et 8. klasses publikum, mens en annen antar en videregående elev. Men alle tre modellene genererte svar som kunne overbevise en uinformert bruker om at hendelsen var ekte.

Prompt engineering-teknikker som _metaprompting_ og _temperaturkonfigurasjon_ kan redusere modellfabrikasjoner noe. Nye prompt engineering _arkitekturer_ integrerer også nye verktøy og teknikker sømløst i promptflyten for å motvirke eller redusere noen av disse effektene.

## Case Study: GitHub Copilot

La oss avslutte dette avsnittet med å få en følelse av hvordan prompt engineering brukes i virkelige løsninger ved å se på ett Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI Parprogrammerer" - den konverterer tekstprompt til kodefullføringer og er integrert i ditt utviklingsmiljø (f.eks. Visual Studio Code) for en sømløs brukeropplevelse. Som dokumentert i serien av blogginnlegg nedenfor, var den tidligste versjonen basert på OpenAI Codex-modellen - med ingeniører som raskt innså behovet for finjustering av modellen og utvikling av bedre prompt engineering-teknikker for å forbedre kodekvaliteten. I juli [lanserte de en forbedret AI-modell som går utover Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for enda raskere forslag.

Les innleggene i rekkefølge for å følge deres læringsreise.

- **Mai 2023** | [GitHub Copilot blir bedre til å forstå koden din](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Innside GitHub: Arbeid med LLM-ene bak GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Hvordan skrive bedre prompt for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juli 2023** | [.. GitHub Copilot går utover Codex med forbedret AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juli 2023** | [En utviklers guide til prompt engineering og LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hvordan bygge en enterprise LLM-app: Lærdom fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også bla gjennom deres [Engineering-blogg](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere innlegg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som viser hvordan disse modellene og teknikkene _anvendes_ for å drive virkelige applikasjoner.

---

<!--
LEKSJONSSKJEMA:
Denne enheten bør dekke kjernebegrep #2.
Forsterk konseptet med eksempler og referanser.

KONSEPT #2:
Promptdesign.
Illustrert med eksempler.
-->

## Promptkonstruksjon

Vi har sett hvorfor prompt engineering er viktig - nå la oss forstå hvordan prompts _konstrues_ slik at vi kan evaluere ulike teknikker for mer effektiv promptdesign.

### Grunnleggende Prompt

La oss starte med den grunnleggende prompten: en tekstinnsending sendt til modellen uten annen kontekst. Her er et eksempel - når vi sender de første få ordene i USAs nasjonalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), fullfører den umiddelbart svaret med de neste linjene, og illustrerer grunnleggende prediksjonsatferd.

| Prompt (Inndata)     | Fullføring (Utdata)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det høres ut som du starter teksten til "The Star-Spangled Banner," USAs nasjonalsang. Hele teksten er ...                               |

### Kompleks Prompt

Nå legger vi til kontekst og instruksjoner til den grunnleggende prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lar oss konstruere en kompleks prompt som en samling av _meldinger_ med:

- Inndata/utdata-par som reflekterer _bruker_innsending og _assistent_svar.
- Systemmelding som setter konteksten for assistentens oppførsel eller personlighet.

Forespørselen er nå i formen nedenfor, hvor _tokeniseringen_ effektivt fanger relevant informasjon fra kontekst og samtale. Å endre systemkonteksten kan nå påvirke kvaliteten på fullføringene like mye som brukerens inndata.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruksjonsprompt

I eksemplene ovenfor var brukerprompten en enkel tekstforespørsel som kan tolkes som en anmodning om informasjon. Med _instruksjonsprompter_ kan vi bruke den teksten til å spesifisere en oppgave mer detaljert og gi bedre veiledning til AI-en. Her er et eksempel:

| Prompt (Inndata)                                                                                                                                                                                                                         | Fullføring (Utdata)                                                                                                        | Instruksjonstype    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Skriv en beskrivelse av borgerkrigen                                                                                                                                                                                                   | _returnerte et enkelt avsnitt_                                                                                            | Enkel               |
| Skriv en beskrivelse av borgerkrigen. Oppgi viktige datoer og hendelser og beskriv deres betydning                                                                                                                                      | _returnerte et avsnitt etterfulgt av en liste med viktige hendelsesdatoer med beskrivelser_                               | Kompleks            |
| Skriv en beskrivelse av borgerkrigen i 1 avsnitt. Gi 3 kulepunkter med viktige datoer og deres betydning. Gi 3 flere kulepunkter med viktige historiske personer og deres bidrag. Returner utdata som en JSON-fil      | _returnerer mer omfattende detaljer i en tekstboks, formatert som JSON som du kan kopiere til en fil og validere ved behov_ | Kompleks. Formatert.|

## Primært innhold

I eksemplene ovenfor var prompten fortsatt ganske åpen, slik at LLM kunne avgjøre hvilken del av dens forhåndstrente datasett som var relevant. Med designmønsteret _primært innhold_ deles inndatateksten i to deler:

- en instruksjon (handling)
- relevant innhold (som påvirker handling)

Her er et eksempel der instruksjonen er å "oppsummere dette i 2 setninger".

| Prompt (Inndata)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Fullføring (Utdata)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen til alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige med det blotte øye på nattehimmelen, og har vært kjent av gamle sivilisasjoner siden før historisk tid. Den er oppkalt etter den romerske guden Jupiter.[19] Når den ses fra jorden, kan Jupiter være lyssterk nok til at det reflekterte lyset kaster synlige skygger,[20] og er i gjennomsnitt det tredje lyseste naturlige objektet på nattehimmelen etter månen og Venus. <br/> **Oppsummer dette i 2 korte setninger** | Jupiter, den femte planeten fra solen, er den største i solsystemet og er kjent for å være et av de lyseste objektene på nattehimmelen. Oppkalt etter den romerske guden Jupiter, er den en gasskjempe med en masse to og en halv ganger den til alle de andre planetene i solsystemet til sammen. |

Segmentet for primært innhold kan brukes på ulike måter for å drive mer effektive instruksjoner:

- **Eksempler** - i stedet for å fortelle modellen hva den skal gjøre med en eksplisitt instruksjon, gi den eksempler på hva den skal gjøre og la den utlede mønsteret.
- **Signaler** - følg instruksjonen med et "signal" som forbereder fullføringen, og guider modellen mot mer relevante svar.
- **Malverk** - dette er repeterbare 'oppskrifter' for prompt med plassholdere (variabler) som kan tilpasses med data for spesifikke bruksområder.

La oss utforske disse i praksis.

### Bruke eksempler

Dette er en tilnærming der du bruker primært innhold for å "mate modellen" med noen eksempler på ønsket utdata for en gitt instruksjon, og lar den utlede mønsteret for det ønskede utdataet. Basert på antall eksempler som gis, har vi zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nå av tre komponenter:

- En oppgavebeskrivelse
- Noen eksempler på ønsket utdata
- Starten på et nytt eksempel (som blir en implisitt oppgavebeskrivelse)

| Læringstype | Prompt (Inndata)                                                                                                                                        | Fullføring (Utdata)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Oversett til spansk                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Spilleren løp basene => Baseball <br/> Spilleren slo en ess => Tennis <br/> Spilleren slo en sekser => Cricket <br/> Spilleren utførte en slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Se hvordan vi måtte gi eksplisitt instruksjon ("Oversett til spansk") i zero-shot prompting, men den utledes i one-shot prompting-eksemplet. Few-shot-eksemplet viser hvordan flere eksempler lar modeller gjøre mer presise slutninger uten ekstra instruksjoner.

### Promptsignaler

En annen teknikk for å bruke primært innhold er å gi _signaler_ i stedet for eksempler. I dette tilfellet gir vi modellen et dytt i riktig retning ved å _starte den_ med et utdrag som reflekterer ønsket svarformat. Modellen "tar signalet" og fortsetter i samme stil.

| Antall signaler | Prompt (Inndata)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Fullføring (Utdata)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen til alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige med det blotte øye på nattehimmelen, og har vært kjent av gamle sivilisasjoner siden før historisk tid. <br/>**Oppsummer dette**                                       | Jupiter er den største planeten i vårt solsystem og den femte fra solen. Den er en gasskjempe med en masse som er 1/1000 av solens, men den er tyngre enn alle de andre planetene til sammen. Gamle sivilisasjoner har kjent til Jupiter lenge, og den er lett synlig på nattehimmelen. |
| 1              | Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen til alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige med det blotte øye på nattehimmelen, og har vært kjent av gamle sivilisasjoner siden før historisk tid. <br/>**Oppsummer dette** <br/> Det vi lærte er at Jupiter | er den femte planeten fra solen og den største i solsystemet. Den er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen til alle de andre planetene til sammen. Den er lett synlig for det blotte øye og har vært kjent siden antikken.                     |

| 2              | Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gassgigant med en masse på en tusendel av solens, men to og en halv ganger massen av alle de andre planetene i solsystemet til sammen. Jupiter er et av de mest lyssterke objektene synlige med det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før dokumentert historie. <br/>**Oppsummer dette** <br/> Topp 3 fakta vi lærte:         | 1. Jupiter er den femte planeten fra solen og den største i solsystemet. <br/> 2. Den er en gassgigant med en masse på en tusendel av solen...<br/> 3. Jupiter har vært synlig for det blotte øye siden eldgamle tider ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Maler for prompt

En prompt-mal er en _forhåndsdefinert oppskrift for en prompt_ som kan lagres og gjenbrukes etter behov, for å skape mer konsistente brukeropplevelser i stor skala. I sin enkleste form er det rett og slett en samling av prompleksempler som [dette fra OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) som gir både de interaktive promptkomponentene (bruker- og systemmeldinger) og API-drevne forespørselsformat – for å støtte gjenbruk.

I en mer kompleks form som [dette eksempelet fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) inneholder den _plassholdere_ som kan erstattes med data fra ulike kilder (brukerinput, systemkontekst, eksterne datakilder osv.) for å generere en prompt dynamisk. Dette lar oss lage et bibliotek med gjenbrukbare prompts som kan brukes til å drive konsistente brukeropplevelser **programmatisk** i stor skala.

Til slutt ligger den virkelige verdien av maler i muligheten til å lage og publisere _prompt-biblioteker_ for vertikale bruksområder – der prompt-malen nå er _optimalisert_ til å reflektere brukerspesifikk kontekst eller eksempler som gjør svarene mer relevante og nøyaktige for målgruppen. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) er et godt eksempel på denne tilnærmingen, som kuraterer et bibliotek av prompts for utdanningssektoren med fokus på nøkkelobjektiver som leksjonsplanlegging, læreplanutforming, studentveiledning osv.

## Støttende innhold

Hvis vi ser på promptkonstruksjon som å ha en instruksjon (oppgave) og et mål (primært innhold), så er _sekundært innhold_ som tilleggsinformasjon vi gir for å **påvirke utdata på en eller annen måte**. Dette kan være tuningparametere, formateringsinstruksjoner, emnetaksonomier osv. som kan hjelpe modellen med å _skreddersy_ sitt svar for å passe ønskede brukerobjektiver eller forventninger.

For eksempel: Gitt en kurskatalog med omfattende metadata (navn, beskrivelse, nivå, metadatakategorier, instruktør osv.) for alle tilgjengelige kurs i læreplanen:

- kan vi definere en instruksjon for å "oppsummere kurskatalogen for høsten 2023"
- kan vi bruke det primære innholdet til å gi noen eksempler på ønsket utdata
- kan vi bruke sekundært innhold til å identifisere de 5 mest relevante "kategoriene"

Nå kan modellen gi en oppsummering i formatet vist ved de få eksemplene – men hvis et resultat har flere kategorier, kan den prioritere de 5 identifiserte i sekundært innhold.

---

<!--
LEKSJONSMAL:
Denne enheten bør dekke kjernebegrep #1.
Forsterk begrepet med eksempler og referanser.

KONSEPT #3:
Prompt engineering teknikker.
Hva er noen grunnleggende teknikker for prompt engineering?
Illustrer det med noen øvelser.
-->

## Beste praksis for prompt

Nå som vi vet hvordan prompts kan _konstrueres_, kan vi begynne å tenke på hvordan vi kan _designe_ dem for å reflektere beste praksis. Vi kan tenke på dette i to deler – ha riktig _tankesett_ og bruke riktige _teknikker_.

### Tankesett for prompt engineering

Prompt engineering er en prøving og feiling-prosess, så husk tre brede veiledende faktorer:

1. **Domeneinnsikt er viktig.** Svarenes nøyaktighet og relevans er en funksjon av _domenet_ som applikasjonen eller brukeren opererer i. Bruk din intuisjon og domeneekspertise til å **tilpasse teknikker** ytterligere. For eksempel, definer _domene-spesifikke personligheter_ i system-promptene dine, eller bruk _domene-spesifikke maler_ i brukerpromptene. Gi sekundært innhold som reflekterer domene-spesifikk kontekst, eller bruk _domene-spesifikke hint og eksempler_ for å guide modellen mot kjente bruksområder.

2. **Modellforståelse er viktig.** Vi vet at modeller er stokastiske av natur. Men modellimplementasjoner kan også variere med hensyn til treningsdata de bruker (forhåndstrent kunnskap), kapasitetene de tilbyr (f.eks. via API eller SDK) og typen innhold de er optimalisert for (f.eks. kode vs. bilder vs. tekst). Forstå styrkene og begrensningene til modellen du bruker, og bruk den kunnskapen til å _prioritere oppgaver_ eller bygge _tilpassede maler_ optimalisert for modellens kapasiteter.

3. **Iterasjon og validering er viktig.** Modeller utvikles raskt, og det samme gjør teknikkene for prompt engineering. Som domenekspert kan du ha annen kontekst eller kriterier for _din_ spesifikke applikasjon, som kanskje ikke gjelder for det bredere samfunnet. Bruk prompt engineering-verktøy og teknikker for å "komme raskt i gang" med prompt-konstruksjon, så iterer og valider resultatene med din egen intuisjon og domeneekspertise. Registrer innsiktene dine og bygg en **kunnskapsbase** (f.eks. prompt-biblioteker) som kan brukes som ny referanse for andre, for raskere iterasjoner i fremtiden.

## Beste praksis

Nå skal vi se på vanlige anbefalinger fra [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikere.

| Hva                              | Hvorfor                                                                                                                                                                                                                                            |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluer de nyeste modellene.      | Nye modellgenerasjoner har sannsynligvis forbedrede funksjoner og kvalitet – men kan også medføre høyere kostnader. Evaluer for effekt, og ta så beslutninger om migrasjon.                                                                      |
| Skill mellom instruksjoner og kontekst | Sjekk om modellen/tilbyderen definerer _avgrensere_ som tydeliggjør instrukser, primært og sekundært innhold. Dette kan hjelpe modellene å tildele vekter mer presist til tokens.                                                               |
| Vær spesifikk og tydelig           | Gi flere detaljer om ønsket kontekst, resultat, lengde, format, stil osv. Dette forbedrer både kvalitet og konsistens i svarene. Dokumenter oppskrifter i gjenbrukbare maler.                                                                     |
| Vær beskrivende, bruk eksempler    | Modeller responderer kanskje bedre på en "vis og fortell"-tilnærming. Start med en `zero-shot`-tilnærming hvor du gir en instruksjon (uten eksempler), prøv så `few-shot` som en forbedring, med noen eksempler på ønsket utdata. Bruk analogier.          |
| Bruk hint for å kickstarte svarene | Gi modellen noen innledende ord eller setninger den kan bruke som utgangspunkt for svaret.                                                                                                                 |
| Dobbelt opp                      | Noen ganger må du gjenta deg for modellen. Gi instruksjoner både før og etter det primære innholdet, bruk en instruksjon og et hint, osv. Iterer og valider for å se hva som fungerer.                                                              |
| Rekkefølge betyr noe              | Rekkefølgen du presenterer informasjon til modellen kan påvirke utdata, også i opplæringseksempler, på grunn av nylighetsbias. Prøv ulike alternativer for å finne det som fungerer best.                                                          |
| Gi modellen en "utgang"           | Gi modellen en _reserve_-svar den kan gi om den ikke kan fullføre oppgaven av en eller annen grunn. Dette kan redusere sjansen for at modeller genererer falske eller fabrikerte svar.                                                              |
|                                   |                                                                                                                                                                                                                                                   |

Som med alle beste praksiser, husk at _dine erfaringer kan variere_ avhengig av modell, oppgave og domene. Bruk disse som et utgangspunkt, og iterer for å finne det som fungerer best for deg. Evaluer kontinuerlig prompt engineering-prosessen din når nye modeller og verktøy blir tilgjengelige, med fokus på skalering og svar-kvalitet.

<!--
LEKSJONSMAL:
Denne enheten skal tilby en kodeutfordring hvis relevant.

UTFORDRING:
Lenke til en Jupyter Notebook hvor kun kodekommentarene er i instruksjonene (kodeavsnitt er tomme).

LØSNING:
Lenke til en kopi av den Noteboken med promptene fylt inn og kjørt, som viser hvordan ett eksempel kan være.
-->

## Oppgave

Gratulerer! Du har kommet til slutten av leksjonen! Nå er det tid for å prøve ut noen av disse konseptene og teknikkene med ekte eksempler!

Til oppgaven skal vi bruke en Jupyter Notebook med øvelser du kan fullføre interaktivt. Du kan også utvide Noteboken med dine egne Markdown- og Kode-celler for å utforske ideer og teknikker på egenhånd.

### For å komme i gang, fork repoet, så

- (Anbefalt) Start GitHub Codespaces
- (Alternativt) Klon repoet til en lokal enhet og bruk det med Docker Desktop
- (Alternativt) Åpne Noteboken med ditt foretrukne Notebook-kjøremiljø.

### Deretter konfigurer miljøvariablene dine

- Kopier `.env.copy`-filen i repo-roten til `.env` og fyll inn verdiene for `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT`. Gå tilbake til [Learning Sandbox-seksjonen](#læringsmiljø) for å lære hvordan.

### Deretter åpner du Jupyter Noteboken

- Velg runtime-kjernen. Hvis du bruker alternativ 1 eller 2, velg bare standard Python 3.10.x-kjerne som tilbys av utviklingscontaineren.

Du er klar til å kjøre øvelsene. Merk at det ikke finnes noen _riktige eller gale_ svar her – bare utforske alternativer gjennom prøving og feiling, og bygge intuisjon for hva som fungerer for en gitt modell og applikasjonsdomene.

_Av denne grunn finnes det ingen Kodeløsnings-segmenter i denne leksjonen. I stedet vil Noteboken ha Markdown-celler med tittelen "Min løsning:" som viser ett eksempel på svar som referanse._

 <!--
LEKSJONSMAL:
Avslutt seksjonen med en oppsummering og ressurser for selvstyrt læring.
-->

## Kunnskapssjekk

Hvilken av følgende er en god prompt med rimelige beste praksiser?

1. Vis meg et bilde av en rød bil
2. Vis meg et bilde av en rød bil av merke Volvo og modell XC90 parkert ved en klippe med solnedgang
3. Vis meg et bilde av en rød bil av merke Volvo og modell XC90

A: 2, det er den beste prompten siden den gir detaljer om "hva" og går inn på spesifikke detaljer (ikke bare en bil, men et spesifikt merke og modell) og den beskriver også omgivelsene. 3 er nest best da den også inneholder mye beskrivelse.

## 🚀 Utfordring

Se om du kan bruke "hint"-teknikken med prompten: Fullfør setningen "Vis meg et bilde av en rød bil av merke Volvo og ". Hva svarer den, og hvordan kan du forbedre den?

## Flott jobba! Fortsett læringen

Vil du lære mer om ulike konsepter innen prompt engineering? Gå til [siden for videre læring](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å finne andre gode ressurser om dette emnet.

Gå videre til Leksjon 5 hvor vi ser på [avanserte prompting-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->