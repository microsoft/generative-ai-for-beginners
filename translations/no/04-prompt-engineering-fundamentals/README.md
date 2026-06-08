# Grunnleggende om Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/no/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduksjon
Denne modulen dekker essensielle konsepter og teknikker for å lage effektive prompts i generative AI-modeller. Måten du skriver prompten til en LLM på, er også viktig. En nøye utformet prompt kan gi et bedre svar av høy kvalitet. Men hva betyr egentlig begrepene _prompt_ og _prompt engineering_? Og hvordan kan jeg forbedre prompt-_inputen_ jeg sender til LLM-en? Dette er spørsmålene vi vil prøve å svare på i dette kapitlet og det neste.

_Generativ AI_ er i stand til å skape nytt innhold (f.eks. tekst, bilder, lyd, kode osv.) som svar på brukerforespørsler. Dette oppnås ved hjelp av _Large Language Models_ som OpenAIs GPT ("Generative Pre-trained Transformer")-serie, som er trent til å bruke naturlig språk og kode.

Brukere kan nå interagere med disse modellene ved hjelp av kjente paradigmer som chat, uten å trenge teknisk ekspertise eller opplæring. Modellene er _prompt-baserte_ – brukere sender inn tekst (prompt) og får tilbake AI-responsen (ferdigstilling). De kan deretter "chatte med AI-en" iterativt, i samtaler med flere runder, og forbedre prompten sin til svaret møter forventningene.

"Prompter" blir nå det primære _programmeringsgrensesnittet_ for generative AI-apper, som forteller modellene hva de skal gjøre og påvirker kvaliteten på svarene som kommer tilbake. "Prompt Engineering" er et raskt voksende studieområde som fokuserer på _design og optimalisering_ av prompts for å levere konsistente og kvalitetsmessige svar i stor skala.

## Læringsmål

I denne leksjonen lærer vi hva Prompt Engineering er, hvorfor det er viktig, og hvordan vi kan lage mer effektive prompts for en gitt modell og applikasjonsmål. Vi skal forstå kjernebegreper og beste praksis for prompt engineering – og lære om et interaktivt Jupyter Notebook-"sandbox"-miljø hvor vi kan se disse konseptene anvendt på ekte eksempler.

Ved slutten av denne leksjonen skal vi kunne:

1. Forklare hva prompt engineering er og hvorfor det er viktig.
2. Beskrive komponentene i en prompt og hvordan de brukes.
3. Lære beste praksis og teknikker for prompt engineering.
4. Anvende lærte teknikker på ekte eksempler, med en OpenAI-endepunkt.

## Nøkkelbegreper

Prompt Engineering: Praksisen med å designe og raffinere input for å styre AI-modeller mot å produsere ønskede utdata.  
Tokenisering: Prosessen med å konvertere tekst til mindre enheter, kalt tokens, som en modell kan forstå og behandle.  
Instruksjonsjusterte LLM-er: Store språkmodeller (LLM) som har blitt finjustert med spesifikke instruksjoner for å forbedre nøyaktighet og relevans i responsen.

## Læringssandbox

Prompt engineering er for tiden mer kunst enn vitenskap. Den beste måten å forbedre intuisjonen på, er å _øve mer_ og bruke en prøve-og-feil-tilnærming som kombinerer ekspertise innen applikasjonsdomene med anbefalte teknikker og modellspesifikke optimaliseringer.

Jupyter Noteboken som følger med denne leksjonen tilbyr et _sandbox_-miljø hvor du kan prøve ut det du lærer – enten fortløpende eller som en del av kodeutfordringen til slutt. For å utføre øvelsene trenger du:

1. **En Azure OpenAI API-nøkkel** – serviceendepunkt for en distribuert LLM.  
2. **En Python-runtime** – hvor notebooken kan kjøres.  
3. **Lokale miljøvariabler** – _fullfør [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)-steg nå for å være klar_.

Notebooken leveres med _startøvelser_ – men du oppfordres til å legge til egne _Markdown_ (beskrivelse) og _Code_ (prompt-forespørsler) seksjoner for å prøve ut flere eksempler eller ideer – og bygge din intuisjon for prompt-design.

## Illustrert guide

Vil du få et overblikk over hva denne leksjonen dekker før du går i gang? Sjekk ut denne illustrerte guiden som gir deg en følelse av hovedtemaene og nøkkelinnsiktene du kan reflektere over i hvert tema. Leksjonsplanen tar deg fra å forstå kjernebegreper og utfordringer til å takle dem med relevante prompt engineering-teknikker og beste praksis. Merk at avsnittet "Avanserte teknikker" i denne guiden refererer til innholdet i _neste_ kapittel i denne læreplanen.

![Illustrert guide til Prompt Engineering](../../../translated_images/no/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vår oppstart

La oss nå snakke om hvordan _dette temaet_ relaterer seg til vår oppstartsvisjon om å [bringe AI-innovasjon til utdanning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker å bygge AI-drevne applikasjoner for _personlig tilpasset læring_ – så la oss tenke på hvordan ulike brukere av applikasjonen vår kan "designe" prompts:

- **Administratorer** kan be AI-en om å _analysere læreplandata for å identifisere hull i dekning_. AI-en kan oppsummere resultater eller visualisere dem med kode.  
- **Lærere** kan be AI-en om å _generere en leksjonsplan for en målgruppe og tema_. AI-en kan bygge den personlige planen i et spesifisert format.  
- **Studenter** kan be AI-en om å _veilede dem i et vanskelig fag_. AI-en kan nå veilede studenter med leksjoner, hint og eksempler tilpasset deres nivå.

Dette er bare toppen av isfjellet. Sjekk ut [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et åpent kildekode-bibliotek med prompts kuratert av utdanningseksperter – for å få en bedre forståelse av mulighetene! _Prøv å kjøre noen av disse promptene i sandkassen eller ved hjelp av OpenAI Playground for å se hva som skjer!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Hva er Prompt Engineering?

Vi startet denne leksjonen med å definere **Prompt Engineering** som prosessen med å _designe og optimalisere_ tekstinput (prompter) for å levere konsistente og kvalitetsmessige svar (ferdigstillinger) for en gitt applikasjonsmål og modell. Vi kan tenke på dette som en to-stegs prosess:

- _designe_ den innledende prompten for en gitt modell og målsetting  
- _finjustere_ prompten iterativt for å forbedre kvaliteten på svaret

Dette er nødvendigvis en prøve-og-feil-prosess som krever brukerintuisjon og innsats for å oppnå optimale resultater. Så hvorfor er det viktig? For å svare på det spørsmålet må vi først forstå tre begreper:

- _Tokenisering_ = hvordan modellen "ser" prompten  
- _Base LLMer_ = hvordan grunnmodellen "behandler" en prompt  
- _Instruksjonsjusterte LLMer_ = hvordan modellen nå kan se "oppgaver"

### Tokenisering

En LLM ser prompter som en _sekvens av tokens_ hvor ulike modeller (eller versjoner av en modell) kan tokenisere samme prompt på forskjellige måter. Siden LLM-er er trent på tokens (og ikke rå tekst), har måten promptene tokeniseres på direkte innvirkning på kvaliteten av det genererte svaret.

For å få en intuisjon for hvordan tokenisering fungerer, prøv verktøy som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Lim inn prompten din – og se hvordan den konverteres til tokens, med oppmerksomhet på hvordan mellomromstegn og skilletegn håndteres. Merk at dette eksempelet viser en eldre LLM (GPT-3) – så å prøve dette med en nyere modell kan gi et annet resultat.

![Tokenisering](../../../translated_images/no/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsept: Grunnmodeller

Når en prompt er tokenisert, er hovedfunksjonen til ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grunnmodellen) å forutsi det neste token i sekvensen. Siden LLM-er er trent på enorme tekstdatasett, har de en god forståelse av de statistiske relasjonene mellom tokens og kan gjøre denne prediksjonen med viss selvtillit. Merk at de ikke forstår _meningen_ med ordene i prompten eller tokenet; de ser bare et mønster de kan "komplettere" med sin neste prediksjon. De kan fortsette å forutsi sekvensen til brukeren stopper eller en forhåndsbestemt betingelse nås.

Vil du se hvordan promptbasert ferdigstilling fungerer? Skriv inn den overnevnte prompten i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinnstillinger. Systemet er konfigurert til å behandle prompter som informasjonsforespørsler – så du bør se en fullføring som tilfredsstiller denne konteksten.

Men hva om brukeren ønsket å se noe spesifikt som møter visse kriterier eller oppgaveformål? Her kommer _instruksjonsjusterte_ LLM-er inn.

![Base LLM Chat Completion](../../../translated_images/no/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsept: Instruksjonsjusterte LLM-er

En [Instruksjonsjustert LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grunnmodellen og finjusteres med eksempler eller input/output-par (f.eks. fler-runde "meldinger") som kan inneholde klare instruksjoner – og responsen fra AI prøver å følge den instruksen.

Dette bruker teknikker som Forsterkningslæring med menneskelig tilbakemelding (RLHF) som kan lære modellen å _følge instruksjoner_ og _lære av tilbakemeldinger_ slik at den produserer svar som er bedre egnet for praktiske anvendelser og mer relevante for brukerens mål.

La oss prøve det – gå tilbake til prompten over, men endre nå _systemmeldingen_ til å gi følgende instruksjon som kontekst:

> _Oppsummer innhold du får for en elev på andre trinn. Hold resultatet til ett avsnitt med 3-5 punktlister._

Ser du hvordan resultatet nå er justert for å gjenspeile ønsket mål og format? En lærer kan nå direkte bruke dette svaret i lysbildene sine til den klassen.

![Instruksjonsjustert LLM Chat Completion](../../../translated_images/no/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Hvorfor trenger vi Prompt Engineering?

Nå som vi vet hvordan prompter behandles av LLM-er, la oss snakke om _hvorfor_ vi trenger prompt engineering. Svaret ligger i det faktum at dagens LLM-er byr på flere utfordringer som gjør at _pålitelige og konsistente ferdigstillinger_ er vanskeligere å oppnå uten innsats i utforming og optimalisering av prompt.

For eksempel:

1. **Modellresponser er stokastiske.** Samme prompt vil sannsynligvis gi ulike svar med forskjellige modeller eller modellversjoner. Og den kan til og med gi forskjellige resultater med _samme modell_ til ulike tider. _Teknikker for prompt engineering kan hjelpe oss å minimere disse variasjonene ved å tilby bedre retningslinjer_.

1. **Modeller kan finne på svar.** Modeller er forhåndstrent på _store, men begrensede_ datasett, noe som betyr at de mangler kunnskap om konsepter utenfor opplæringsomfanget. Som følge kan de produsere svar som er unøyaktige, fiktive, eller direkte i strid med kjente fakta. _Prompt engineering-teknikker hjelper brukere å identifisere og redusere slike fabrikasjoner, f.eks. ved å be AI om kilder eller resonnementer_.

1. **Modellens evner vil variere.** Nyere modeller eller modellgenerasjoner vil ha rikere kapasiteter, men også bringe unike særegenheter og kompromisser i kostnad og kompleksitet. _Prompt engineering kan hjelpe oss å utvikle beste praksis og arbeidsflyter som skjuler forskjellene og tilpasser seg modell-spesifikke krav på skalerbare og sømløse måter_.

La oss se dette i aksjon i OpenAI eller Azure OpenAI Playground:

- Bruk samme prompt med forskjellige LLM-distribusjoner (f.eks. OpenAI, Azure OpenAI, Hugging Face) – så du variasjonene?  
- Bruk samme prompt gjentatte ganger med _samme_ LLM-distribusjon (f.eks. Azure OpenAI playground) – hvordan var forskjellene?

### Eksempel på fabrikasjoner

I dette kurset bruker vi begrepet **"fabrikasjon"** for å referere til fenomenet hvor LLM-er noen ganger genererer faktuelt feilaktig informasjon på grunn av begrensninger i treningen eller andre forhold. Du har kanskje også hørt dette omtalt som _"hallusinasjoner"_ i populære artikler eller forskningspapirer. Vi anbefaler imidlertid sterkt å bruke _"fabrikasjon"_ som begrep slik at vi ikke utilsiktet antropomorfiserer atferden ved å tillegge en menneskelig egenskap til et maskindrevet resultat. Dette styrker også [Retningslinjer for Ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologiperspektiv, ved å fjerne ord som også kan oppfattes som støtende eller ikke-inkluderende i noen sammenhenger.

Vil du få en følelse av hvordan fabrikasjoner fungerer? Tenk på en prompt som instruerer AI-en til å generere innhold om et ikke-eksisterende tema (for å sikre at det ikke finnes i treningsdatasettet). For eksempel – jeg prøvde denne prompten:

> **Prompt:** lag en leksjonsplan om Martian War of 2076.
Et nettsøk viste meg at det fantes fiktive fortellinger (f.eks. TV-serier eller bøker) om marskriger – men ingen i 2076. Sunn fornuft forteller oss også at 2076 er _i fremtiden_ og derfor ikke kan knyttes til en virkelig hendelse.

Så hva skjer når vi kjører denne prompten hos forskjellige LLM-leverandører?

> **Svar 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/no/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/no/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/no/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som forventet, produserer hver modell (eller modellversjon) litt forskjellige svar takket være stokastisk oppførsel og variasjoner i modellkapasitet. For eksempel retter en modell seg mot et 8. klasses publikum mens en annen antar en videregåendestudent. Men alle tre modellene genererte svar som kunne overbevise en uinformert bruker om at hendelsen var ekte.

Prompt engineering-teknikker som _metaprompting_ og _temperaturkonfigurasjon_ kan til en viss grad redusere modellens fabrikerte svar. Nye prompt engineering-_arkitekturer_ integrerer også sømløst nye verktøy og teknikker i promptflyten for å dempe eller redusere noen av disse effektene.

## Casestudie: GitHub Copilot

La oss avslutte denne seksjonen ved å få et inntrykk av hvordan prompt engineering brukes i virkelige løsninger ved å se på en casestudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI Parprogrammerer" – den omdanner tekstprompt til kodeforslag og er integrert i ditt utviklingsmiljø (f.eks. Visual Studio Code) for en sømløs brukeropplevelse. Som dokumentert i serien av blogginnlegg under, var den tidligste versjonen basert på OpenAI Codex-modellen — med ingeniører som raskt innså behovet for å finjustere modellen og utvikle bedre prompt engineering-teknikker for å forbedre kodekvaliteten. I juli lanserte de en forbedret AI-modell som går utover Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for enda raskere forslag.

Les innleggene i rekkefølge for å følge deres læringsreise.

- **Mai 2023** | [GitHub Copilot blir bedre til å forstå koden din](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Bak kulissene i GitHub: Jobbe med LLM-ene bak GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Hvordan skrive bedre prompts for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juli 2023** | [.. GitHub Copilot går utover Codex med forbedret AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juli 2023** | [En utviklers guide til prompt engineering og LLM-er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hvordan bygge en bedrifts-LLM-app: Lærdom fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også bla gjennom deres [engineering-blogg](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere innlegg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som viser hvordan disse modellene og teknikkene _anvendes_ for å drive virkelige applikasjoner.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Prompt-konstruksjon

Vi har sett hvorfor prompt engineering er viktig – nå la oss forstå hvordan prompts _konstrueres_ slik at vi kan evaluere ulike teknikker for mer effektiv promptdesign.

### Grunnleggende prompt

La oss begynne med den grunnleggende prompten: en tekstinngang sendt til modellen uten annen kontekst. Her er et eksempel – når vi sender de første ordene i USAs nasjonalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) fullfører den umiddelbart svaret med de neste linjene og illustrerer modellens grunnleggende prediksjonsadferd.

| Prompt (Input)     | Kompletering (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det høres ut som du starter teksten til "The Star-Spangled Banner," USAs nasjonalsang. Hele teksten er ... |

### Komplekst prompt

Nå legger vi til kontekst og instruksjoner til den grunnleggende prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lar oss konstruere en kompleks prompt som en samling av _meldinger_ med:

- Inngangs-/utgangspar som reflekterer _bruker_-inngang og _assistent_-respons.
- Systemmelding som setter konteksten for assistentens oppførsel eller personlighet.

Forespørselen har nå formen nedenfor, der _tokeniseringen_ effektivt fanger relevant informasjon fra kontekst og samtale. Å endre systemkonteksten kan nå ha like stor betydning for kvaliteten på kompletteringene som brukerinputtet.

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

I eksemplene ovenfor var brukerprompt en enkel tekstforespørsel som kan tolkes som en informasjonsforespørsel. Med _instruksjons_ prompts kan vi bruke teksten til å spesifisere en oppgave mer detaljert og gi bedre veiledning til AI-en. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Kompletering (Output)                                                                                                        | Instruksjonstype    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Skriv en beskrivelse av den amerikanske borgerkrigen                                                                                                                                                                                   | _returnerte et enkelt avsnitt_                                                                                              | Enkel               |
| Skriv en beskrivelse av den amerikanske borgerkrigen. Oppgi viktige datoer og hendelser og beskriv deres betydning                                                                                                                   | _returnerte et avsnitt etterfulgt av en liste med viktige datoer og beskrivelser av hendelsene_                              | Kompleks            |
| Skriv en beskrivelse av den amerikanske borgerkrigen i 1 avsnitt. Gi 3 punktlister med viktige datoer og deres betydning. Gi 3 punkter til med viktige historiske personer og deres bidrag. Returner resultatet som en JSON-fil        | _returnerer mer omfattende detaljer i en tekstboks, formatert som JSON som du kan kopiere og lime inn i en fil og validere etter behov_ | Kompleks. Formatert.|

## Primært innhold

I eksemplene ovenfor var prompten fremdeles ganske åpen, og lot LLM-en avgjøre hvilken del av treningsdataene som var relevant. Med designmønsteret _primært innhold_ deles inngangsteksten i to deler:

- en instruksjon (handling)
- relevant innhold (som påvirker handlingen)

Her er et eksempel hvor instruksjonen er å "oppsummere dette i 2 setninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Kompletering (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planeten fra solen og den største i solsystemet. Det er en gasskjemp med en masse som er en tusendel av solens, men to og en halv gang så stor som alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige med det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før skriftlig historie. Den er oppkalt etter den romerske guden Jupiter.[19] Når den ses fra jorden, kan Jupiter være så lyssterk at det reflekterte lyset kaster synlige skygger,[20] og er i gjennomsnitt det tredje mest lyssterke naturlige objektet på nattehimmelen etter månen og venus. <br/> **Oppsummer dette i 2 korte setninger** | Jupiter, den femte planeten fra solen, er den største i solsystemet og er kjent for å være et av de lyseste objektene på nattehimmelen. Den er oppkalt etter den romerske guden Jupiter, en gasskjemp med en masse som er to og en halv ganger så stor som alle de andre planetene i solsystemet til sammen. |

Segmentet med primært innhold kan brukes på forskjellige måter for å drive mer effektive instruksjoner:

- **Eksempler** – i stedet for å fortelle modellen hva den skal gjøre med en eksplisitt instruksjon, gi eksempler på hva som skal gjøres og la den trekke mønsteret.
- **Signalord** – følg instruksjonen med et "signal" som gir starten på svaret, og leder modellen mot mer relevante svar.
- **Mal** – dette er repeterbare 'oppskrifter' på prompts med plassholdere (variabler) som kan tilpasses med data til spesifikke bruksområder.

La oss utforske disse i praksis.

### Bruke eksempler

Dette er en tilnærming der du bruker det primære innholdet til å "mate modellen" med noen eksempler på ønsket output for en gitt instruksjon, og lar den trekke ut mønsteret for ønsket resultat. Basert på antallet eksempler kan vi ha zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nå av tre komponenter:

- En oppgavebeskrivelse
- Noen få eksempler på ønsket output
- Begynnelsen på et nytt eksempel (som blir en implicit oppgavebeskrivelse)

| Læringstype  | Prompt (Input)                                                                                                                                        | Kompletering (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Oversett til spansk                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Spilleren løp basene => Baseball <br/> Spilleren slo et ess => Tennis <br/> Spilleren slo en sekser => Cricket <br/> Spilleren dunket ballen =>         | Basketball                  |
|               |                                                                                                                                                       |                             |

Legg merke til at vi måtte legge inn eksplisitt instruksjon ("Oversett til spansk") i zero-shot prompting, men det fremgår implisitt i one-shot-eksemplet. Few-shot-eksemplet viser hvordan flere eksempler lar modellene gjøre mer presise slutninger uten ekstra instruksjoner.

### Signalord for prompt

En annen teknikk for å bruke primært innhold er å gi _signalord_ i stedet for eksempler. I dette tilfellet gir vi modellen et puff i riktig retning ved å _starte_ med et utdrag som reflekterer ønsket svarformat. Modellen "tar signalet" og fortsetter i samme stil.

| Antall signalord | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Kompletering (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter er den femte planeten fra solen og den største i solsystemet. Det er en gasskjemp med en masse som er en tusendel av solens, men to og en halv gang så stor som alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige med det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før skriftlig historie. <br/>**Oppsummer dette**                                       | Jupiter er den største planeten i vårt solsystem og den femte fra solen. Det er en gasskjemp med en masse som er 1/1000 av solens, men tyngre enn alle de andre planetene til sammen. Gamle sivilisasjoner har lenge kjent til Jupiter, og den er lett synlig på nattehimmelen.. |
| 1              | Jupiter er den femte planeten fra solen og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solen, men to og en halv ganger massen av alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historisk tid. <br/>**Oppsummer dette** <br/> Det vi lærte er at Jupiter | er den femte planeten fra solen og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solen, men to og en halv ganger massen av alle de andre planetene til sammen. Den er lett synlig for det blotte øye og har vært kjent siden oldtiden.                        |
| 2              | Jupiter er den femte planeten fra solen og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solen, men to og en halv ganger massen av alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historisk tid. <br/>**Oppsummer dette** <br/> Topp 3 fakta vi lærte:         | 1. Jupiter er den femte planeten fra solen og den største i solsystemet. <br/> 2. Det er en gasskjempe med en masse som er en tusendel av solen...<br/> 3. Jupiter har vært synlig for det blotte øye siden oldtiden ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

En prompt-mal er en _forhåndsdefinert oppskrift på en prompt_ som kan lagres og gjenbrukes etter behov, for å skape mer konsistente brukeropplevelser i stor skala. I sin enkleste form er det rett og slett en samling prompt-eksempler som [dette fra OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) som gir både de interaktive prompt-komponentene (bruker- og systemmeldinger) og API-baserte forespørselsformat - for å støtte gjenbruk.

I en mer kompleks form som [dette eksempelet fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) inneholder den _plassholdere_ som kan erstattes med data fra ulike kilder (brukerinput, systemkontekst, eksterne datakilder osv.) for å generere en prompt dynamisk. Dette lar oss lage et bibliotek av gjenbrukbare prompts som kan brukes til å drive konsistente brukeropplevelser **programmatisk** i stor skala.

Til slutt ligger den virkelige verdien i maler i muligheten til å lage og publisere _prompt-biblioteker_ for vertikale applikasjonsdomener - hvor prompt-malen nå er _optimalisert_ for å reflektere applikasjonsspesifikk kontekst eller eksempler som gjør svarene mer relevante og presise for målgruppen. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)-arkivet er et godt eksempel på denne tilnærmingen, som kuraterer et bibliotek av prompts for utdanningssektoren med fokus på nøkkelområder som leksjonsplanlegging, pensumdesign, studentveiledning osv.

## Støttende innhold

Hvis vi ser på promptkonstruksjon som å ha en instruksjon (oppgave) og et mål (primært innhold), så er _sekundært innhold_ som ekstra kontekst vi gir for å **påvirke output på en eller annen måte**. Det kan være justeringsparametere, formatinstruksjoner, emnetaksonomier osv. som hjelper modellen med å _skreddersy_ svaret til å passe de ønskede bruker-målene eller forventningene.

For eksempel: Gitt en kurskatalog med omfattende metadata (navn, beskrivelse, nivå, metadatatagger, instruktør osv.) på alle tilgjengelige kurs i pensum:

- kan vi definere en instruksjon til å "oppsummere kurskatalogen for høsten 2023"
- vi kan bruke hovedinnholdet til å gi noen eksempler på ønsket output
- vi kan bruke sekundært innhold til å identifisere de 5 viktigste "taggene" av interesse.

Nå kan modellen gi et sammendrag i formatet vist av de få eksemplene - men hvis et resultat har flere tagger, kan den prioritere de 5 taggene identifisert i sekundært innhold.

---

<!--
LESSON TEMPLATE:
Denne enheten skal dekke kjernekonsept #1.
Forsterk konseptet med eksempler og referanser.

KONSEPT #3:
Prompt Engineering-teknikker.
Hva er noen grunnleggende teknikker for prompt engineering?
Illustrer det med noen øvelser.
-->

## Beste fremgangsmåter for prompt

Nå som vi vet hvordan prompts kan _konstrueres_, kan vi begynne å tenke på hvordan de skal _designes_ for å reflektere beste praksis. Vi kan dele dette i to deler - å ha riktig _tankesett_ og å bruke riktige _teknikker_.

### Tankesett for prompt engineering

Prompt Engineering er en prøving-og-feiling-prosess, så hold tre brede veiledende punkter i bakhodet:

1. **Domeneinnsikt er viktig.** Svarnøyaktighet og relevans er avhengig av _domenet_ applikasjonen eller brukeren opererer innenfor. Bruk intuisjonen og domenekunnskapen din til å **tilpasse teknikkene** videre. For eksempel kan du definere _domene-spesifikke personligheter_ i systempromptene dine, eller bruke _domene-spesifikke maler_ i brukerpromptene dine. Gi sekundært innhold som reflekterer domene-spesifikk kontekst, eller bruk _domene-spesifikke hint og eksempler_ for å styre modellen mot kjente mønstre.

2. **Modellforståelse er viktig.** Vi vet at modeller er stokastiske av natur. Men modellimplementeringer kan også variere i treningsdatasett (forhåndslært kunnskap), muligheter de tilbyr (f.eks. via API eller SDK) og typen innhold de er optimalisert for (f.eks. kode vs. bilder vs. tekst). Forstå styrker og begrensninger ved modellen du bruker, og bruk den kunnskapen for å _prioritere oppgaver_ eller bygge _tilpassede maler_ som er optimalisert for modellens evner.

3. **Iterasjon og validering er viktig.** Modeller utvikler seg raskt, og det gjør også teknikkene for prompt engineering. Som domenekspert kan du ha annen kontekst eller kriterier for _din_ spesifikke applikasjon, som kanskje ikke gjelder resten av fellesskapet. Bruk verktøy og teknikker for prompt engineering for å "komme raskt i gang" med prompt-konstruksjon, og iterer og valider resultatene ved hjelp av din egen intuisjon og fagkunnskap. Dokumenter innsiktene dine og bygg en **kunnskapsbase** (f.eks. prompt-biblioteker) som kan brukes som ny baseline av andre for raskere iterasjoner i fremtiden.

## Beste praksis

La oss nå se på vanlige anbefalte beste praksiser fra [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)-fagfolk.

| Hva                               | Hvorfor                                                                                                                                                                                                                                             |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluer de nyeste modellene.      | Nye modellgenerasjoner har sannsynligvis forbedrede funksjoner og kvalitet - men kan også medføre høyere kostnader. Evaluer dem for effekt, og ta migrasjonsbeslutninger.                                                                             |
| Skill instruksjoner og kontekst   | Sjekk om modellen/leverandøren din definerer _avgrensere_ for bedre å skille mellom instruksjoner, primært og sekundært innhold. Dette hjelper modellen til å tildele vekter mer nøyaktig til tokens.                                               |
| Vær spesifikk og tydelig           | Gi mer detaljer om ønsket kontekst, utfall, lengde, format, stil osv. Dette vil forbedre både kvalitet og konsistens i svarene. Fang oppskrifter i gjenbrukbare maler.                                                                              |
| Vær beskrivende, bruk eksempler    | Modeller responderer ofte bedre på en "vis og forklar"-tilnærming. Start gjerne med `zero-shot` der du gir instruksjon uten eksempler, deretter prøv `few-shot` ved å gi få eksempler på ønsket output. Bruk analogier.                              |
| Bruk hint for å starte fullføringer| Gi modellen noen ledende ord eller fraser som den kan bruke som startpunkt for svaret, for å veilede den mot ønsket resultat.                                                                                                                    |
| Gjenta for å forsterke            | Noen ganger må du gjenta instruksjoner for modellen. Gi instruksjoner både før og etter hovedinnholdet, bruk både en instruksjon og et hint osv. Iterer og valider for å se hva som fungerer best.                                               |
| Rekkefølge betyr noe               | Rekkefølgen du presenterer informasjon til modellen kan påvirke output, også i læringseksempler, på grunn av nylig bias. Prøv forskjellige alternativer for å finne hva som fungerer best.                                                        |
| Gi modellen en “utvei”             | Gi modellen et _tilbakefall_-svar den kan bruke hvis den ikke kan fullføre oppgaven. Dette kan redusere sjansen for at modellen genererer feilaktige eller fabrikerte svar.                                                                      |
|                                  |                                                                                                                                                                                                                                                    |

Som med all beste praksis, husk at _din erfaring kan variere_ avhengig av modell, oppgave og domene. Bruk disse som et utgangspunkt, og iterer for å finne det som fungerer best for deg. Evaluer kontinuerlig prompt engineering-prosessen din når nye modeller og verktøy blir tilgjengelige, med fokus på skalerbarhet og svart kvalitet.

<!--
LESSON TEMPLATE:
Denne enheten skal inneholde en kodeutfordring om relevant

UTFORDRING:
Lenke til en Jupyter Notebook med bare kodekommentarer i instruksjonene (kodeseksjoner er tomme).

LØSNING:
Lenke til en kopi av den Notebooken med fylt inn prompts og kjørt, som viser ett eksempel på løsning.
-->

## Oppgave

Gratulerer! Du er kommet til slutten av leksjonen! Nå er det tid for å prøve noen av konseptene og teknikkene i praksis med ekte eksempler!

For oppgaven bruker vi en Jupyter Notebook med øvelser du kan jobbe samlet med. Du kan også utvide Notebooken med egne Markdown- og Kode-celler for å utforske ideer og teknikker på egenhånd.

### For å komme i gang, forkk repoet, så

- (Anbefalt) Start GitHub Codespaces
- (Alternativt) Klon repoet til din lokale maskin og bruk det med Docker Desktop
- (Alternativt) Åpne Notebooken med foretrukket runtime-miljø for Notebooks.

### Deretter konfigurer miljøvariablene dine

- Kopier `.env.copy`-filen i repo-roten til `.env` og fyll inn verdiene for `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT`. Gå tilbake til [Learning Sandbox-delen](#læringssandbox) for instruksjoner om hvordan.

### Neste, åpne Jupyter Notebook

- Velg runtime-kjernen. Hvis du bruker alternativ 1 eller 2, velger du bare standard Python 3.10.x-kjerne som tilbys av dev container.

Du er klar til å kjøre øvelsene. Merk at det ikke finnes _riktige eller gale_ svar her – bare utforske alternativer gjennom prøving og feiling og bygge intuisjon for hva som fungerer for en gitt modell og applikasjonsdomene.

_For denne grunn finnes det ingen ferdigkodede løsningsdeler i denne leksjonen. I stedet vil Notebook ha Markdown-celler med tittelen "Min løsning:" som viser ett eksempel på output for referanse._

 <!--
LESSON TEMPLATE:
Avslutt seksjonen med en oppsummering og ressurser for selvstyrt læring.
-->

## Kunnskapsjekk

Hvilken av følgende er en god prompt som følger noen rimelige beste praksiser?

1. Vis meg et bilde av en rød bil
2. Vis meg et bilde av en rød bil av merke Volvo og modell XC90 parkert ved en klippe med solnedgang
3. Vis meg et bilde av en rød bil av merke Volvo og modell XC90

A: 2, det er den beste prompten fordi den gir detaljer om "hva" og går i spesifikasjon (ikke bare en hvilken som helst bil, men en spesifikk merke og modell) og beskriver også miljøet. 3 er nest best fordi den også inneholder mye beskrivelse.

## 🚀 Utfordring

Se om du kan bruke "hint"-teknikken med prompten: Fullfør setningen "Vis meg et bilde av en rød bil av merke Volvo og ". Hva svarer den med, og hvordan ville du forbedre det?

## Flott arbeid! Fortsett læringen

Vil du lære mer om ulike konsepter innen Prompt Engineering? Gå til [siden for videre læring](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å finne flere gode ressurser om dette temaet.

Gå videre til Leksjon 5 hvor vi ser på [avanserte prompting-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->