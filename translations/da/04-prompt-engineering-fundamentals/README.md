# Grundlæggende Principper for Prompt Engineering

[![Grundlæggende Principper for Prompt Engineering](../../../translated_images/da/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduktion
Denne modul dækker essentielle begreber og teknikker til at skabe effektive prompts i generative AI-modeller. Den måde, du skriver din prompt til et LLM, har også betydning. En omhyggeligt udformet prompt kan opnå en bedre kvalitet af svar. Men hvad betyder udtryk som _prompt_ og _prompt engineering_ egentlig? Og hvordan kan jeg forbedre prompt _input_, som jeg sender til LLM? Disse er spørgsmål, vi vil forsøge at besvare i dette kapitel og det næste.

_Generativ AI_ er i stand til at skabe nyt indhold (f.eks. tekst, billeder, lyd, kode osv.) som svar på brugerforespørgsler. Det opnås ved hjælp af _Store Sprogmodeller_ som OpenAIs GPT ("Generative Pre-trained Transformer") serie, som er trænet til at bruge naturligt sprog og kode.

Brugere kan nu interagere med disse modeller ved hjælp af velkendte paradigmer som chat, uden at skulle have teknisk ekspertise eller træning. Modellerne er _prompt-baserede_ - brugere sender en tekstinput (prompt) og får AI-svaret (completion) tilbage. De kan ændre "chatte med AI'en" iterativt i flertrins samtaler, hvor de finjusterer deres prompt, indtil svaret matcher deres forventninger.

"Prompts" bliver nu den primære _programmeringsgrænseflade_ for generative AI-apps, der fortæller modellerne, hvad de skal gøre, og påvirker kvaliteten af de returnerede svar. "Prompt Engineering" er et hurtigt voksende studieområde, der fokuserer på _design og optimering_ af prompts for at levere konsistente og kvalitetsmæssige svar i stor skala.

## Læringsmål

I denne lektion lærer vi, hvad Prompt Engineering er, hvorfor det er vigtigt, og hvordan vi kan skabe mere effektive prompts for en given model og applikationsformål. Vi vil forstå kernebegreber og bedste praksis for prompt engineering – og lære om et interaktivt Jupyter Notebooks "sandbox" miljø, hvor vi kan se disse begreber anvendt på virkelige eksempler.

Når vi er færdige med denne lektion, vil vi kunne:

1. Forklare hvad prompt engineering er, og hvorfor det er vigtigt.
2. Beskrive komponenterne i en prompt og hvordan de bruges.
3. Lære bedste praksis og teknikker til prompt engineering.
4. Anvende lærte teknikker på virkelige eksempler ved hjælp af et OpenAI-endpoint.

## Centrale Begreber

Prompt Engineering: Praksis med at designe og forfine input for at guide AI-modeller til at producere ønskede output.
Tokenisering: Processen med at omsætte tekst til mindre enheder, kaldet tokens, som en model kan forstå og behandle.
Instruktions-tilpassede LLM'er: Store Sprogmodeller (LLM'er), der er finjusteret med specifikke instruktioner for at forbedre deres svarpræcision og relevans.

## Læringssandbox

Prompt engineering er i øjeblikket mere kunst end videnskab. Den bedste måde at forbedre vores intuition på er at _øve sig mere_ og anvende en prøv-og-fejl tilgang, der kombinerer domæneekspertise med anbefalede teknikker og model-specifikke optimeringer.

Jupyter Notebooken, der følger med denne lektion, giver et _sandbox_ miljø, hvor du kan prøve det, du lærer – enten løbende eller som en del af kodeudfordringen til sidst. For at kunne udføre øvelserne skal du bruge:

1. **En Azure OpenAI API-nøgle** - service-endpointet for en udrullet LLM.
2. **Et Python-runtime** - hvor Notebooken kan køres.
3. **Lokale miljøvariabler** - _fuldfør nu [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) for at være klar_.

Notebooken indeholder _starter_-øvelser – men du opfordres til at tilføje dine egne _Markdown_ (beskrivelser) og _Kode_ (prompt-forespørgsler) sektioner for at prøve flere eksempler eller idéer – og bygge din intuition for prompt-design.

## Illustreret Guide

Vil du have det store overblik over, hvad denne lektion dækker, før du går i gang? Tjek denne illustrerede guide, som giver dig en fornemmelse af de vigtigste emner og nøglepointer, du kan tænke over i hver af dem. Lektionens køreplan fører dig fra forståelse af kernebegreber og udfordringer til at adressere dem med relevante prompt engineering teknikker og bedste praksis. Bemærk at sektionen "Avancerede teknikker" i denne guide refererer til indhold dækket i det _næste_ kapitel i dette kursusforløb.

![Illustreret Guide til Prompt Engineering](../../../translated_images/da/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vores Startup

Lad os nu tale om, hvordan _dette emne_ relaterer til vores startup-mission om at [bringe AI-innovation til uddannelse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker at bygge AI-drevne applikationer til _personlig læring_ – så lad os tænke på, hvordan forskellige brugere af vores applikation kunne "designe" prompts:

- **Administratorer** kunne bede AI om at _analysere læseplansdata for at identificere mangler i dækningen_. AI'en kan opsummere resultater eller visualisere dem med kode.
- **Undervisere** kunne bede AI om at _generere en lektionsplan for en målgruppe og emne_. AI'en kan bygge den personlige plan i et specificeret format.
- **Studerende** kunne bede AI om at _vejlede dem i et vanskeligt fag_. AI'en kan nu guide elever med lektioner, hints & eksempler skræddersyet til deres niveau.

Det er kun toppen af isbjerget. Tjek [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et open source prompt-bibliotek kurateret af uddannelseseksperter – for at få en bredere forståelse af mulighederne! _Prøv at køre nogle af disse prompts i sandkassen eller brug OpenAI Playground for at se, hvad der sker!_

<!--
LEKTIONSMAL:
Denne enhed skal dække kernebegreb #1.
Forstærk begrebet med eksempler og referencer.

BEGREB #1:
Prompt Engineering.
Definér det og forklar, hvorfor det er nødvendigt.
-->

## Hvad er Prompt Engineering?

Vi startede denne lektion med at definere **Prompt Engineering** som processen med _at designe og optimere_ tekstinput (prompts) for at levere konsistente og kvalitetsmæssige svar (completions) til et givet applikationsformål og model. Vi kan tænke på dette som en 2-trins proces:

- _at designe_ den indledende prompt til en given model og formål
- _at finjustere_ prompten iterativt for at forbedre svarenes kvalitet

Dette er nødvendigvis en prøv-og-fejl proces, der kræver brugerintuition og indsats for at opnå optimale resultater. Så hvorfor er det vigtigt? For at besvare det spørgsmål, skal vi først forstå tre begreber:

- _Tokenisering_ = hvordan modellen "ser" prompten
- _Base LLM'er_ = hvordan grundmodellen "behandler" en prompt
- _Instruktions-tilpassede LLM'er_ = hvordan modellen nu kan "se opgaver"

### Tokenisering

En LLM ser prompts som en _sekvens af tokens_, hvor forskellige modeller (eller versioner af en model) kan tokenisere den samme prompt forskelligt. Da LLM'er er trænet på tokens (og ikke rå tekst), har måden, hvorpå prompts tokeniseres, direkte indflydelse på kvaliteten af det genererede svar.

For at få en intuition for, hvordan tokenisering fungerer, prøv værktøjer som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Kopiér din prompt ind - og se, hvordan den omdannes til tokens, og læg mærke til, hvordan mellemrumstegn og tegnsætning håndteres. Bemærk, at dette eksempel viser en ældre LLM (GPT-3) – så at prøve med en nyere model kan give et anderledes resultat.

![Tokenisering](../../../translated_images/da/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Begreb: Grundmodeller

Når en prompt er tokeniseret, er hovedfunktionen for ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller Grundmodel) at forudsige tokenet i sekvensen. Da LLM'er er trænet på enorme tekstdatasæt, har de en god fornemmelse af statistiske sammenhænge mellem tokens og kan lave den forudsigelse med en vis sikkerhed. Bemærk, at de ikke forstår _meningen_ med ordene i prompten eller token; de ser blot et mønster, de kan "fuldføre" med deres næste forudsigelse. De kan fortsætte med at forudsige sekvensen, indtil det afbrydes af brugerens indgreb eller en forudbestemt tilstand.

Vil du se, hvordan prompt-baseret completion fungerer? Indtast ovenstående prompt i [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) med standardindstillingerne. Systemet er konfigureret til at behandle prompts som informationsforespørgsler, så du bør se et svar, der opfylder denne kontekst.

Men hvad hvis brugeren ønskede at se noget specifikt, der opfylder nogle kriterier eller et opgaveformål? Her kommer _instruktions-tilpassede_ LLM'er ind i billedet.

![Grundmodel LLM Chat Completion](../../../translated_images/da/04-playground-chat-base.65b76fcfde0caa67.webp)

### Begreb: Instruktions-tilpassede LLM'er

En [Instruktions-Tilpasset LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grundmodellen og finjusterer den med eksempler eller input/output-par (f.eks. flertrins "beskeder"), som kan indeholde klare instruktioner – og AI'ens svar forsøger at følge den instruktion.

Dette bruger teknikker som Forstærkningslæring med Menneskelig Feedback (RLHF), som kan træne modellen til _at følge instruktioner_ og _lære af feedback_, så den producerer svar, der er bedre egnet til praktiske anvendelser og mere relevante for brugerens mål.

Lad os prøve det – gå tilbage til prompten ovenfor, men ændr nu _systembeskeden_ til at give følgende instruktion som kontekst:

> _Opsummer indhold, du får stillet til rådighed, til en elev i anden klasse. Hold resultatet til et afsnit med 3-5 punktformspunkter._

Se hvordan resultatet nu er tilpasset det ønskede mål og format? En underviser kan nu direkte bruge dette svar i deres slides til den klasse.

![Instruktions-Tilpasset LLM Chat Completion](../../../translated_images/da/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Hvorfor har vi brug for Prompt Engineering?

Nu hvor vi ved, hvordan prompts behandles af LLM'er, lad os tale om, _hvorfor_ vi har brug for prompt engineering. Svaret ligger i, at nuværende LLM'er stiller en række udfordringer, som gør _pålidelige og konsistente svar_ sværere at opnå uden indsats i promptkonstruktion og optimering. For eksempel:

1. **Modellers svar er stokastiske.** Den _samme prompt_ vil sandsynligvis producere forskellige svar med forskellige modeller eller modelversioner. Og den kan endda give forskellige resultater med _samme model_ på forskellige tidspunkter. _Prompt engineering teknikker kan hjælpe os med at minimere disse variationer ved at give bedre retningslinjer_.

1. **Modeller kan finde på svar.** Modeller er fortrænet med _store men begrænsede_ datasæt, hvilket betyder, at de mangler viden om begreber uden for træningsomfanget. Som følge heraf kan de producere svar, der er upræcise, opdigtede eller direkte modstridende med kendte fakta. _Prompt engineering teknikker hjælper brugere med at identificere og reducere sådanne opdigtninger, fx ved at bede AI om kildehenvisninger eller ræsonnement_.

1. **Modellers evner varierer.** Nyere modeller eller modelgenerationer får rigere kapaciteter, men bringer også unikke særheder og afvejninger i omkostninger og kompleksitet. _Prompt engineering hjælper os med at udvikle bedste praksis og arbejdsgange, der abstraherer forskelle og tilpasser til model-specifikke krav på skalerbare, sømløse måder_.

Lad os se dette i praksis i OpenAI eller Azure OpenAI Playground:

- Brug den samme prompt med forskellige LLM-udrulninger (f.eks. OpenAI, Azure OpenAI, Hugging Face) – så du variationerne?
- Brug den samme prompt gentagne gange med _samme_ LLM-udrulning (f.eks. Azure OpenAI playground) – hvordan adskilte disse variationer sig?

### Eksempel på opdigtninger

I dette kursus bruger vi udtrykket **"opdigtning"** for at henvise til fænomenet, hvor LLM'er til tider genererer faktuelt ukorrekte oplysninger på grund af begrænsninger i deres træning eller andre begrænsninger. Du har måske også hørt det omtalt som _"hallucinationer"_ i populære artikler eller videnskabelige artikler. Vi anbefaler dog stærkt at bruge _"opdigtning"_ som udtryk, så vi ikke utilsigtet antropomorfiserer adfærden ved at tillægge en maskindrevet handling menneskelige karaktertræk. Dette understøtter også [Ansvarlig AI-retningslinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologiperspektiv ved at fjerne termer, der også kan opfattes som stødende eller ikke-inkluderende i visse kontekster.

Vil du have en fornemmelse af, hvordan opdigtninger fungerer? Tænk på en prompt, der instruerer AI til at generere indhold om et ikke-eksisterende emne (for at sikre det ikke findes i træningsdatasættet). For eksempel - jeg prøvede denne prompt:

> **Prompt:** generer en lektionsplan om Den Marsianske Krig i 2076.

Et websøg viste mig, at der findes fiktive fortællinger (f.eks. tv-serier eller bøger) om marsianske krige – men ingen i 2076. Almindelig sund fornuft fortæller os også, at 2076 er _i fremtiden_ og derfor ikke kan forbindes med en virkelig begivenhed.


Hvad sker der så, når vi kører denne prompt med forskellige LLM-udbydere?

> **Svar 1**: OpenAI Playground (GPT-35)

![Svar 1](../../../translated_images/da/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Svar 2](../../../translated_images/da/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Svar 3](../../../translated_images/da/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som forventet producerer hver model (eller modelversion) lidt forskellige svar takket være stokastisk opførsel og variationer i modelkapacitet. For eksempel retter den ene model sig mod et 8. klasses publikum, mens den anden antager en gymnasieelev. Men alle tre modeller genererede svar, der kunne overbevise en uvidende bruger om, at begivenheden var ægte.

Prompt engineering-teknikker som _metaprompting_ og _temperaturkonfiguration_ kan til en vis grad reducere modelleres fabrikationer. Nye prompt engineering-_arkitekturer_ integrerer også problemfrit nye værktøjer og teknikker i promptforløbet for at afbøde eller reducere nogle af disse effekter.

## Case Study: GitHub Copilot

Lad os afslutte dette afsnit med at få en fornemmelse af, hvordan prompt engineering bruges i virkelige løsninger ved at se på en Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI parprogrammer" - den omsætter tekstprompter til kodekompletteringer og er integreret i dit udviklingsmiljø (f.eks. Visual Studio Code) for en problemfri brugeroplevelse. Som dokumenteret i blogserien nedenfor var den tidligste version baseret på OpenAI Codex-modellen - med ingeniører, der hurtigt indså behovet for at finjustere modellen og udvikle bedre prompt engineering-teknikker for at forbedre kodekvaliteten. I juli [debuterede de en forbedret AI-model, der går ud over Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for endnu hurtigere forslag.

Læs indlæggene i rækkefølge for at følge deres læringsrejse.

- **Maj 2023** | [GitHub Copilot bliver bedre til at forstå din kode](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inde hos GitHub: Arbejde med LLM’erne bag GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Hvordan man skriver bedre prompts til GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot går ud over Codex med forbedret AI-model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En udviklers guide til prompt engineering og LLM’er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hvordan man bygger en enterprise LLM app: Læringer fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også gennemse deres [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere indlæg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), der viser, hvordan disse modeller og teknikker _anvendes_ til at drive virkelige applikationer.

---

<!--
LESSON TEMPLATE:
Dette afsnit skal dække kernedokument #2.
Understøt konceptet med eksempler og referencer.

KONCEPT #2:
Prompt Design.
Illustreret med eksempler.
-->

## Prompt Konstruktion

Vi har set, hvorfor prompt engineering er vigtigt – nu lad os forstå, hvordan prompter _konstrueres_, så vi kan evaluere forskellige teknikker til mere effektiv promptdesign.

### Basal Prompt

Lad os starte med den basale prompt: en tekstinput sendt til modellen uden anden kontekst. Her er et eksempel - når vi sender de første få ord af USA's nationalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), fuldfører den øjeblikkeligt svaret med de næste linjer, hvilket illustrerer grundlæggende forudsigelsesadfærd.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det lyder som om, du er ved at starte teksten til "The Star-Spangled Banner," USA's nationalsang. Den fulde tekst er ...                   |

### Kompleks Prompt

Lad os nu tilføje kontekst og instruktioner til den basale prompt. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lader os konstruere en kompleks prompt som en samling af _beskeder_ med:

- Input/output-par, der afspejler _bruger_ input og _assistent_ respons.
- Systembesked, der sætter konteksten for assistentens adfærd eller personlighed.

Anmodningen er nu i nedenstående form, hvor _tokeniseringen_ effektivt fanger relevant information fra kontekst og samtale. At ændre systemkonteksten kan nu have lige så stor indflydelse på kvaliteten af svar som de givne brugerinput.

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

### Instruktionsprompt

I ovenstående eksempler var brugerprompten en simpel tekstforespørgsel, der kan tolkes som en anmodning om information. Med _instruktions_ prompter kan vi bruge den tekst til at specificere en opgave i detaljer og give AI bedre vejledning. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruktionstype   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Skriv en beskrivelse af Borgerkrigen                                                                                                                                                                                                   | _returnerede et simpelt afsnit_                                                                                              | Simpel             |
| Skriv en beskrivelse af Borgerkrigen. Angiv vigtige datoer og begivenheder, og beskriv deres betydning                                                                                                                                 | _returnerede et afsnit efterfulgt af en liste over vigtige begivenhedsdatoer med beskrivelser_                               | Kompleks           |
| Skriv en beskrivelse af Borgerkrigen i 1 afsnit. Giv 3 punktformspunkter med vigtige datoer og deres betydning. Giv 3 flere punktformspunkter med vigtige historiske personer og deres bidrag. Returner output som en JSON-fil                              | _returnerer mere omfattende detaljer i en tekstboks, formateret som JSON, som du kan kopiere til en fil og validere efter behov_ | Kompleks. Formateret. |

## Primært Indhold

I ovenstående eksempler var prompten stadig ret åben, hvilket tillod LLM’en at beslutte, hvilken del af sit fortrænede datasæt der var relevant. Med designmønsteret _primært indhold_ deles inputteksten op i to dele:

- en instruktion (handling)
- relevant indhold (der påvirker handlingen)

Her er et eksempel, hvor instruktionen er at "opsummere dette i 2 sætninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse på en tusindedel af solen, men to og en halv gang mere end alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter synlige for det blotte øje på nattehimlen, og har været kendt af oldtidscivilisationer siden før registreret historie. Den er opkaldt efter den romerske gud Jupiter.[19] Når den ses fra Jorden, kan Jupiter være lysstærk nok til, at det reflekterede lys kan kaste synlige skygger,[20] og den er gennemsnitligt det tredje-lyseste naturlige objekt på nattehimlen efter Månen og Venus. <br/> **Opsummer dette i 2 korte sætninger** | Jupiter, den femte planet fra solen, er den største i solsystemet og er kendt for at være et af de klareste objekter på nattehimlen. Opkaldt efter den romerske gud Jupiter, er det en gasgigant, hvis masse er to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. |

Segmentet med primært indhold kan bruges på forskellige måder til at drive mere effektive instruktioner:

- **Eksempler** - i stedet for at fortælle modellen, hvad den skal gøre med en eksplicit instruktion, giv den eksempler på hvad den skal gøre, og lad den udlede mønstret.
- **Signaler** - følg instruktionen med et "signal", der forbereder fuldførelsen og guider modellen mod mere relevante svar.
- **Skabeloner** - disse er gentagelige ’opskrifter’ for prompter med pladsholdere (variabler), der kan tilpasses med data til specifikke brugssituationer.

Lad os udforske disse i praksis.

### Brug af eksempler

Dette er en tilgang, hvor du bruger det primære indhold til at "fodre modellen" med nogle eksempler på det ønskede output for en given instruktion, og lader den udlede mønstret for det ønskede output. Afhængigt af antallet af givne eksempler kan vi have zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nu af tre komponenter:

- En opgavebeskrivelse
- Et par eksempler på det ønskede output
- Starten på et nyt eksempel (som bliver til en implicit opgavebeskrivelse)

| Læringstype | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Oversæt til spansk                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Spilleren løb baserne => Baseball <br/> Spilleren slog en ace => Tennis <br/> Spilleren slog en seks’er => Cricket <br/> Spilleren lavede en slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Bemærk, hvordan vi måtte give en eksplicit instruktion ("Oversæt til spansk") i zero-shot prompting, men den udledes i one-shot prompting-eksemplet. Few-shot-eksemplet viser, hvordan tilføjelse af flere eksempler giver modeller mulighed for at lave mere præcise slutninger uden ekstra instruktioner.

### Prompt Signaler

En anden teknik til at bruge primært indhold er at give _signaler_ i stedet for eksempler. Her giver vi modellen en skub i den rigtige retning ved at _starte den_ med et uddrag, der afspejler det ønskede svarformat. Modellen "tager så signalet" og fortsætter i den retning.

| Antal signaler | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse på en tusindedel af solen, men to og en halv gang mere end alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter synlige for det blotte øje på nattehimlen, og har været kendt af oldtidscivilisationer siden før registreret historie. <br/>**Opsummer dette**                                       | Jupiter er den største planet i vores solsystem og den femte fra solen. Det er en gasgigant med en masse på 1/1000 af solens, men er tungere end alle de andre planeter tilsammen. Oldtidscivilisationer har kendt til Jupiter i lang tid, og den er let synlig på nattehimlen. |
| 1              | Jupiter er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse på en tusindedel af solen, men to og en halv gang mere end alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter synlige for det blotte øje på nattehimlen, og har været kendt af oldtidscivilisationer siden før registreret historie. <br/>**Opsummer dette** <br/> Hvad vi lærte er, at Jupiter | er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse på en tusindedel af solen, men to og en halv gang mere end alle de andre planeter tilsammen. Den er let synlig for det blotte øje og har været kendt siden oldtiden.                        |

| 2              | Jupiter er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse, der er en tusindedel af solens, men to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter synlige med det blotte øje på nattehimlen og har været kendt af gamle civilisationer siden før den skrevne historie. <br/>**Opsummer dette** <br/> Top 3 fakta vi har lært:         | 1. Jupiter er den femte planet fra solen og den største i solsystemet. <br/> 2. Det er en gasgigant med en masse, der er en tusindedel af solen...<br/> 3. Jupiter har været synlig med det blotte øje siden oldtiden ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-skabeloner

En prompt-skabelon er en _foruddefineret opskrift for en prompt_, der kan gemmes og genbruges efter behov for at skabe mere konsistente brugeroplevelser i stor skala. I sin simpleste form er det blot en samling af prompexempler som [dette fra OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), der både indeholder de interaktive prompt-komponenter (bruger- og systembeskeder) og API-drevne anmodningsformater - for at støtte genbrug.

I en mere kompleks form som [dette eksempel fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) indeholder den _pladsholdere_, der kan udskiftes med data fra forskellige kilder (brugerinput, systemkontekst, eksterne datakilder osv.) for at generere en prompt dynamisk. Dette gør det muligt at skabe et bibliotek af genanvendelige prompts, der kan bruges til at drive konsistente brugeroplevelser **programmatisk** i stor skala.

Endelig ligger den reelle værdi af skabeloner i muligheden for at oprette og udgive _prompt-biblioteker_ for vertikale anvendelsesdomæner - hvor prompt-skabelonen nu er _optimeret_ til at afspejle applikationsspecifik kontekst eller eksempler, der gør svarene mere relevante og præcise for den målrettede brugergruppe. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) depotet er et godt eksempel på denne tilgang, hvor der samles et bibliotek af prompts til uddannelsesdomænet med fokus på nøglemål som lektionsplanlægning, læseplansdesign, elevundervisning osv.

## Støtteindhold

Hvis vi tænker på prompt-konstruktion som at have en instruktion (opgave) og et mål (primært indhold), så er _sekundært indhold_ som yderligere kontekst, vi giver for at **påvirke output på en eller anden måde**. Det kan være justeringsparametre, formateringsinstruktioner, emnetaksonomier osv., der kan hjælpe modellen med at _tilpasse_ sit svar, så det passer til de ønskede brugerformål eller forventninger.

For eksempel: Givet en kursuskatalog med omfattende metadata (navn, beskrivelse, niveau, metadatatags, underviser osv.) for alle tilgængelige kurser i pensum:

- kan vi definere en instruktion om at "opsummere kursuskataloget for efteråret 2023"
- kan vi bruge det primære indhold til at give nogle få eksempler på det ønskede output
- kan vi bruge det sekundære indhold til at identificere de top 5 "tags" af interesse.

Nu kan modellen levere en opsummering i det format, der vises af de få eksempler - men hvis et resultat har flere tags, kan den prioritere de 5 tags, der er identificeret i sekundært indhold.

---

<!--
LEKTIONSSKABELON:
Denne enhed skal dække kernekoncept #1.
Forstærk konceptet med eksempler og referencer.

KONCEPT #3:
Prompt Engineering Teknikker.
Hvad er nogle grundlæggende teknikker til prompt-udformning?
Illustrer det med nogle øvelser.
-->

## Bedste Praksis for Prompting

Nu hvor vi ved, hvordan prompts kan _konstrueres_, kan vi begynde at tænke på, hvordan de kan _designes_ til at afspejle bedste praksis. Vi kan tænke på det i to dele - have den rigtige _tankegang_ og anvende de rigtige _teknikker_.

### Prompt Engineering Tankegang

Prompt Engineering er en prøve-og-fejl proces, så hold tre brede vejledende faktorer i tankerne:

1. **Domæneforståelse betyder noget.** Svarkorrekthed og relevans er en funktion af det _domæne_, som applikationen eller brugeren opererer i. Anvend din intuition og domæneekspertise til at **tilpasse teknikker** yderligere. For eksempel, definer _domænespecifikke personligheder_ i dine systemprompts, eller brug _domænespecifikke skabeloner_ i dine brugerprompts. Giv sekundært indhold, der afspejler domænespecifikke kontekster, eller brug _domænespecifikke signaler og eksempler_ for at guide modellen mod velkendte brugsmønstre.

2. **Modelforståelse betyder noget.** Vi ved, at modeller er stokastiske af natur. Men modelimplementeringer kan også variere med hensyn til det træningsdatasæt, de bruger (forudtrænet viden), de kapaciteter, de tilbyder (f.eks. via API eller SDK) og den type indhold, de er optimeret til (f.eks. kode vs. billeder vs. tekst). Forstå styrker og begrænsninger ved den model, du bruger, og brug den viden til at _prioritere opgaver_ eller bygge _tilpassede skabeloner_, der er optimeret til modellens kapaciteter.

3. **Iteration & Validering betyder noget.** Modeller udvikler sig hurtigt, og det samme gør teknikkerne til prompt engineering. Som domæneekspert kan du have anden kontekst eller kriterier for _din_ specifikke applikation, som måske ikke gælder for det bredere fællesskab. Brug værktøjer og teknikker til prompt engineering for at "komme hurtigt i gang" med prompt-konstruktionen, iterér derefter og valider resultaterne med din egen intuition og domæneekspertise. Optag dine indsigter og opret en **vidensbase** (f.eks. promptbiblioteker), der kan bruges som en ny baseline af andre for hurtigere iterationer fremover.

## Bedste Praksis

Lad os nu kigge på almindelige bedste praksisser, som anbefales af [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikere.

| Hvad                              | Hvorfor                                                                                                                                                                                                                                            |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluer de nyeste modeller.       | Nye modelgenerationer vil sandsynligvis have forbedrede funktioner og kvalitet - men kan også medføre højere omkostninger. Evaluer dem for indvirkning, og tag derefter migrationsbeslutninger.                                                         |
| Adskil instruktioner og kontekst  | Undersøg om din model/udbyder definerer _afgrænsere_ til tydeligere at skelne instruktioner, primært og sekundært indhold. Dette kan hjælpe modeller med at tildele vægte mere præcist til tokens.                                                    |
| Vær specifik og klar              | Giv flere detaljer om den ønskede kontekst, resultat, længde, format, stil osv. Dette vil forbedre både kvaliteten og konsistensen af svarene. Fang opskrifter i genanvendelige skabeloner.                                                          |
| Vær beskrivende, brug eksempler   | Modeller kan reagere bedre på en "vis og fortæl" tilgang. Start med en `zero-shot` tilgang, hvor du giver en instruktion (men ingen eksempler) og prøv derefter `few-shot` som en forbedring, hvor du giver nogle få eksempler på det ønskede output. Brug analogier. |
| Brug signaler til at kickstarte udfald | Skub modellen mod et ønsket resultat ved at give nogle ledende ord eller sætninger, den kan bruge som udgangspunkt for svaret.                                                                                                                   |
| Dobbelt op                       | Nogle gange skal du gentage dig selv for modellen. Giv instruktioner både før og efter dit primære indhold, brug en instruktion og et signal osv. Iterér og valider for at se, hvad der fungerer.                                                      |
| Rækkefølge betyder noget         | Den rækkefølge, du præsenterer information for modellen i, kan påvirke output, også i læringseksempler, takket være recent bias. Prøv forskellige muligheder for at se, hvad der fungerer bedst.                                                     |
| Giv modellen en “vej ud”          | Giv modellen et _fallback_-svar, den kan give, hvis den af en eller anden grund ikke kan fuldføre opgaven. Dette kan mindske risikoen for, at modeller genererer falske eller fabrikerede svar.                                                      |
|                                   |                                                                                                                                                                                                                                                    |

Som med enhver bedste praksis skal du huske, at _din erfaring kan variere_ baseret på model, opgave og domæne. Brug disse som udgangspunkt, og iterér for at finde ud af, hvad der fungerer bedst for dig. Evaluer konstant din prompt engineering proces, efterhånden som nye modeller og værktøjer bliver tilgængelige, med fokus på proces-skalering og svar kvalitet.

<!--
LEKTIONSSKABELON:
Denne enhed skal give en kodeudfordring, hvis relevant

UDFORDRING:
Link til en Jupyter Notebook med kun kodekommentarer i instruktionerne (kodeafsnit er tomme).

LØSNING:
Link til en kopi af den Notebook med udfyldte prompts og kørt, som viser et eksempel på output.
-->

## Opgave

Tillykke! Du er nået til slutningen af lektionen! Det er tid til at teste nogle af disse koncepter og teknikker med rigtige eksempler!

Til vores opgave vil vi bruge en Jupyter Notebook med øvelser, du kan gennemføre interaktivt. Du kan også udvide Notebook’en med dine egne Markdown- og kodeceller for at udforske idéer og teknikker på egen hånd.

### For at komme i gang, fork repoet, og så

- (Anbefalet) Start GitHub Codespaces
- (Alternativt) Klon repoet til din lokale enhed og brug det med Docker Desktop
- (Alternativt) Åbn Notebook’en i dit foretrukne runtime-miljø til Notebooks.

### Dernæst, konfigurer dine miljøvariabler

- Kopier `.env.copy` filen i repo-roden til `.env` og udfyld `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT` værdierne. Gå tilbage til [Learning Sandbox sektion](#læringssandbox) for at lære hvordan.

### Dernæst, åbn Jupyter Notebook’en

- Vælg runtime-kerne. Hvis du bruger mulighed 1 eller 2, skal du blot vælge den standard Python 3.10.x-kerne, der leveres af udviklingscontaineren.

Du er klar til at køre øvelserne. Bemærk, at der ikke findes _rigtige eller forkerte_ svar her – blot at udforske muligheder ved prøve-og-fejl og opbygge intuition for, hvad der virker for en given model og applikationsdomæne.

_Af den grund findes der ingen Kode Løsnings-segmenter i denne lektion. I stedet vil Notebook’en have Markdown-celler med titlen "Min Løsning:", der viser et eksempel på output som reference._

 <!--
LEKTIONSSKABELON:
Afslut afsnittet med et resume og ressourcer til selvstyret læring.
-->

## Videnstest

Hvilket af følgende er en god prompt, der følger rimelige bedste praksisser?

1. Vis mig et billede af en rød bil
2. Vis mig et billede af en rød bil af mærket Volvo og model XC90 parkeret ved en klippe med solen gående ned
3. Vis mig et billede af en rød bil af mærket Volvo og model XC90

A: 2, det er den bedste prompt, da den giver detaljer om "hvad" og går i detaljer (ikke bare en hvilken som helst bil, men et specifikt mærke og model) og den beskriver også den overordnede scene. 3 er næstbedst, da den også indeholder meget beskrivelse.

## 🚀 Udfordring

Se om du kan bruge "signal"-teknikken med prompten: Fuldfør sætningen "Vis mig et billede af en rød bil af mærket Volvo og ". Hvad svarer den, og hvordan vil du forbedre den?

## Godt arbejde! Fortsæt din læring

Vil du lære mere om forskellige koncepter inden for Prompt Engineering? Gå til [fortsat læringsside](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at finde andre gode ressourcer om dette emne.

Gå videre til lektion 5, hvor vi vil se på [avancerede prompting teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->