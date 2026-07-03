# Grundlæggende om Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/da/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduktion
Dette modul dækker essentielle koncepter og teknikker til at skabe effektive prompts i generative AI-modeller. Den måde, du skriver din prompt til et LLM på, betyder også noget. En omhyggeligt udformet prompt kan opnå en bedre kvalitet af svaret. Men hvad præcist betyder termer som _prompt_ og _prompt engineering_? Og hvordan forbedrer jeg prompt-_input_ som jeg sender til LLM? Det er disse spørgsmål, vi vil forsøge at besvare i dette kapitel og det næste.

_Generativ AI_ er i stand til at skabe nyt indhold (f.eks. tekst, billeder, lyd, kode osv.) som svar på brugerforespørgsler. Det opnår dette ved hjælp af _Store Sprogmodeller_ som OpenAIs GPT ("Generative Pre-trained Transformer") serie, der er trænet til at bruge naturligt sprog og kode.

Brugere kan nu interagere med disse modeller ved hjælp af velkendte paradigmer som chat, uden at have brug for teknisk ekspertise eller træning. Modellerne er _prompt-baserede_ - brugere sender en tekstinput (prompt) og får AI-svaret tilbage (fuldførelse). De kan så "chatte med AI’en" iterativt i samtaler med flere runder, forfine deres prompt indtil svaret matcher deres forventninger.

"Prompts" bliver nu den primære _programmeringsgrænseflade_ for generative AI-apps, der fortæller modellerne, hvad de skal gøre, og påvirker kvaliteten af de returnerede svar. "Prompt Engineering" er et hastigt voksende studieområde, der fokuserer på _design og optimering_ af prompts for at levere konsistente og kvalitetsfulde svar i stor skala.

## Læringsmål

I denne lektion lærer vi, hvad Prompt Engineering er, hvorfor det er vigtigt, og hvordan vi kan udforme mere effektive prompts til en given model og anvendelsesformål. Vi vil forstå kernebegreber og bedste praksis for prompt engineering - og lære om et interaktivt Jupyter Notebooks "sandbox"-miljø, hvor vi kan se disse begreber anvendt på reelle eksempler.

Ved slutningen af denne lektion vil vi kunne:

1. Forklare hvad prompt engineering er, og hvorfor det betyder noget.
2. Beskrive komponenterne i en prompt og hvordan de bruges.
3. Lære bedste praksis og teknikker til prompt engineering.
4. Anvende lærte teknikker på reelle eksempler ved at bruge en OpenAI-endpoint.

## Vigtige Begreber

Prompt Engineering: Praksissen med at designe og forfine input for at lede AI-modeller mod at producere ønskede output.
Tokenisering: Processen med at omdanne tekst til mindre enheder, kaldet tokens, som en model kan forstå og bearbejde.
Instruction-Tuned LLMs: Store Sprogmodeller (LLMs), der er finjusteret med specifikke instruktioner for at forbedre deres svarnøjagtighed og relevans.

## Læringssandbox

Prompt engineering er i øjeblikket mere en kunst end en videnskab. Den bedste måde at forbedre vores intui­tion for det på er at _øve mere_ og anvende en prøve-og-fejl tilgang, som kombinerer domæneekspertise med anbefalede teknikker og model-specifikke optimeringer.

Den Jupyter Notebook, der følger med denne lektion, giver et _sandbox_-miljø, hvor du kan prøve det, du lærer – løbende eller som en del af kodeudfordringen til sidst. For at udføre øvelserne, skal du have:

1. **En Azure OpenAI API-nøgle** – tjenesteendpoint til en udrullet LLM.
2. **Et Python Runtime** – hvor Notebooken kan køres.
3. **Lokale miljøvariabler** – _fuldfør nu [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) trin for at blive klar_.

Notebooken kommer med _starter_-øvelser – men du opfordres til at tilføje dine egne _Markdown_ (beskrivelser) og _Code_ (prompt-forespørgsler) sektioner for at prøve flere eksempler eller idéer – og opbygge din forståelse af promptdesign.

## Illustreret Guide

Vil du have et overblik over, hvad denne lektion dækker, før du går i gang? Se denne illustrerede guide, der giver dig en fornemmelse af hovedemnerne og de vigtigste pointer, du kan tænke over inden for hvert emne. Lektionens køreplan tager dig fra forståelse af kernebegreber og udfordringer til at tackle dem med relevante prompt engineering teknikker og bedste praksis. Bemærk at afsnittet "Avancerede teknikker" i denne guide refererer til indhold dækket i det _næste_ kapitel i dette kursusforløb.

![Illustreret Guide til Prompt Engineering](../../../translated_images/da/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vores Startup

Lad os nu tale om, hvordan _dette emne_ relaterer til vores startup-mission om at [bringe AI-innovation til uddannelse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker at bygge AI-drevne applikationer til _personaliseret læring_ – så lad os tænke over, hvordan forskellige brugere af vores applikation kan "designe" prompts:

- **Administratorer** kunne bede AI om at _analysere læseplansdata for at identificere huller i dækningen_. AI’en kan opsummere resultater eller visualisere dem med kode.
- **Undervisere** kunne bede AI om at _generere en lektionsplan for en målgruppe og et emne_. AI’en kan bygge den personaliserede plan i et bestemt format.
- **Studerende** kunne bede AI om at _tutorere dem i et vanskeligt fag_. AI’en kan nu guide eleverne med lektioner, hints og eksempler tilpasset deres niveau.

Det er bare toppen af isbjerget. Tjek [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et open source bibliotek af prompts kurateret af uddannelseseksperter – for at få et bredere indtryk af mulighederne! _Prøv at køre nogle af disse prompts i sandboxen eller brug OpenAI Playground for at se, hvad der sker!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Hvad er Prompt Engineering?

Vi startede denne lektion med at definere **Prompt Engineering** som processen at _designe og optimere_ tekstinput (prompts) for at levere konsistente og kvalitetsfulde svar (fuldførelser) for et givent anvendelsesformål og model. Vi kan tænke på dette som en 2-trins proces:

- _designe_ den oprindelige prompt for en given model og formål
- _forfine_ prompten iterativt for at forbedre kvaliteten af svaret

Dette er nødvendigvis en prøve-og-fejl proces, der kræver brugerintuition og indsats for at opnå optimale resultater. Så hvorfor er det vigtigt? For at besvare det spørgsmål, skal vi først forstå tre begreber:

- _Tokenisering_ = hvordan modellen "ser" prompten
- _Base LLMs_ = hvordan grundmodellen "bearbejder" en prompt
- _Instruction-Tuned LLMs_ = hvordan modellen nu kan se "opgaver"

### Tokenisering

En LLM ser prompts som en _sekvens af tokens_, hvor forskellige modeller (eller versioner af en model) kan tokenisere den samme prompt på forskellige måder. Da LLM'er trænes på tokens (og ikke rå tekst), har måden, prompts bliver tokeniseret på, direkte indflydelse på kvaliteten af det genererede svar.

For at få en intuition om, hvordan tokenisering virker, kan du prøve værktøjer som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Kopier din prompt ind – og se hvordan den bliver konverteret til tokens, med opmærksomhed på, hvordan mellemrum og tegnsætning håndteres. Bemærk, at dette eksempel viser en ældre LLM (GPT-3) – så at prøve det med en nyere model kan give et andet resultat.

![Tokenisering](../../../translated_images/da/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Begreb: Grundmodeller (Foundation Models)

Når en prompt er tokeniseret, er hovedfunktionen af ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grundmodel) at forudsige token i sekvensen. Da LLM'er trænes på enorme tekstdatamængder, har de en god fornemmelse for de statistiske relationer mellem tokens og kan lave en sådan forudsigelse med en vis sikkerhed. Bemærk, at de ikke forstår _betydningen_ af ordene i prompten eller token; de ser bare et mønster, de kan "fuldføre" med deres næste forudsigelse. De kan fortsætte med at forudsige sekvensen, indtil det afbrydes af brugerintervention eller en forhåndsdefineret betingelse.

Vil du se, hvordan prompt-baseret fuldførelse fungerer? Indtast den ovenstående prompt i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardindstillingerne. Systemet er konfigureret til at behandle prompts som informationsforespørgsler – så du burde se en fuldførelse, der opfylder denne kontekst.

Men hvad hvis brugeren ønskede at se noget specifikt, som mødte visse kriterier eller opgaveformål? Det er her, _instruction-tunede_ LLM’er kommer ind i billedet.

![Base LLM Chat Completion](../../../translated_images/da/04-playground-chat-base.65b76fcfde0caa67.webp)

### Begreb: Instruction Tuned LLMs

En [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grundmodellen og finjusterer den med eksempler eller input/output-par (f.eks. multi-turn "beskeder"), som kan indeholde klare instruktioner – og AI'ens svar forsøger at følge denne instruktion.

Dette bruger teknikker som Forstærkningslæring med Menneskelig Feedback (RLHF), som kan træne modellen til at _følge instruktioner_ og _lære af feedback_, så den producerer svar, der er bedre egnet til praktiske anvendelser og mere relevante for brugerens mål.

Lad os prøve det – gå tilbage til prompten ovenfor, men skift nu _systemmeddelelsen_ til at give følgende instruktion som kontekst:

> _Opsummer det indhold, du får, så det passer til en elev i anden klasse. Hold resultatet til ét afsnit med 3-5 punktopstillinger._

Se hvordan resultatet nu er finjusteret til at afspejle det ønskede mål og format? En underviser kan nu direkte bruge dette svar i deres præsentationer til den klasse.

![Instruction Tuned LLM Chat Completion](../../../translated_images/da/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Hvorfor har vi brug for Prompt Engineering?

Nu hvor vi ved, hvordan prompts behandles af LLM’er, så lad os tale om _hvorfor_ vi har brug for prompt engineering. Svaret ligger i det faktum, at nuværende LLM’er stiller en række udfordringer, som gør _pålidelige og konsistente fuldførelser_ sværere at opnå uden at lægge indsats i promptkonstruktion og optimering. For eksempel:

1. **Modelsvar er stokastiske.** Den _samme prompt_ vil sandsynligvis producere forskellige svar med forskellige modeller eller modelversioner. Og den kan endda give forskellige resultater med den _samme model_ på forskellige tidspunkter. _Prompt engineering teknikker kan hjælpe os med at minimere disse variationer ved at give bedre sikkerhedsforanstaltninger_.

1. **Modeller kan finde på svar.** Modeller er forhåndstrænede med _store men begrænsede_ datasæt, hvilket betyder, at de mangler viden om begreber uden for træningsmaterialets omfang. Som resultat kan de producere fuldførelser, der er unøjagtige, opdigtede eller direkte modsiger kendte fakta. _Prompt engineering teknikker hjælper brugere med at identificere og afbøde sådanne opdigtelser f.eks. ved at bede AI om henvisninger eller ræsonnement_.

1. **Modellernes kapabiliteter varierer.** Nyere modeller eller modelgenerationer har rigere kapabiliteter, men bringer også unikke særheder og kompromiser i omkostning og kompleksitet. _Prompt engineering kan hjælpe os med at udvikle bedste praksis og arbejdsgange, der abstraherer forskelle væk og tilpasser sig modelspecifikke krav på skalerbare og sømløse måder_.

Lad os se dette i praksis i OpenAI eller Azure OpenAI Playground:

- Brug den samme prompt med forskellige LLM-udrulninger (f.eks. OpenAI, Azure OpenAI, Hugging Face) – så du variationerne?
- Brug den samme prompt gentagne gange med _samme_ LLM-udrulning (f.eks. Azure OpenAI Playground) – hvordan adskilte disse variationer sig?

### Eksempel på opdigtede svar

I dette kursus bruger vi begrebet **"fabrication"** (opdigtelse) til at referere til det fænomen, hvor LLM'er nogle gange genererer faktuelt ukorrekte oplysninger på grund af begrænsninger i deres træning eller andre forhold. Du har måske også hørt dette omtalt som _"hallucinationer"_ i populære artikler eller forskningsartikler. Vi anbefaler dog stærkt at bruge _"fabrication"_ som begreb, så vi undgår utilsigtet antropomorfisering af adfærden ved at tillægge en menneskelig egenskab til et maskindrevet resultat. Dette styrker også [Ansvarlig AI-retningslinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologisk perspektiv ved at fjerne termer, som også kan opfattes som stødende eller ikke-inkluderende i nogle sammenhænge.

Vil du have en fornemmelse af, hvordan opdigtede svar opstår? Tænk på en prompt, der instruerer AI om at generere indhold om et ikke-eksisterende emne (for at sikre, at det ikke findes i træningsdatasættet). For eksempel prøvede jeg denne prompt:

> **Prompt:** generer en lektionsplan om Den Marsianske Krig i 2076.
Et websøgningsresultat viste mig, at der fandtes fiktive fortællinger (f.eks. tv-serier eller bøger) om marskrige – men ingen i 2076. Sund fornuft fortæller os også, at 2076 er _i fremtiden_ og derfor ikke kan forbindes med en reel begivenhed.

Så hvad sker der, når vi kører denne prompt med forskellige LLM-udbydere?

> **Respons 1**: OpenAI Playground (GPT-35)

![Respons 1](../../../translated_images/da/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Respons 2](../../../translated_images/da/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

![Respons 3](../../../translated_images/da/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som forventet producerer hver model (eller modelversion) lidt forskellige svar takket være stokastisk adfærd og variationer i modelkapabilitet. For eksempel retter en model sig mod et 8. klasses publikum, mens en anden antager en gymnasieelev. Men alle tre modeller genererede svar, som kunne overbevise en uvidende bruger om, at begivenheden var reel.

Prompt engineering-teknikker som _metaprompting_ og _temperaturkonfiguration_ kan til en vis grad reducere model-fabrikeringer. Nye prompt engineering _arkitekturer_ integrerer også nye værktøjer og teknikker problemfrit i prompt-flowet for at afbøde eller reducere nogle af disse effekter.

## Case Study: GitHub Copilot

Lad os afslutte dette afsnit med at få en fornemmelse af, hvordan prompt engineering bruges i løsninger i den virkelige verden ved at se på et case study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI Pair Programmer" – den konverterer tekstprompter til kodeforslag og er integreret i dit udviklingsmiljø (f.eks. Visual Studio Code) for en problemfri brugeroplevelse. Som dokumenteret i nedenstående blogserier var den tidligste version baseret på OpenAI Codex-modellen – med ingeniører, der hurtigt indså behovet for at finjustere modellen og udvikle bedre prompt engineering-teknikker for at forbedre kodekvaliteten. I juli [præsenterede de en forbedret AI-model, der går ud over Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for endnu hurtigere forslag.

Læs indlæggene i rækkefølge for at følge deres læringsrejse.

- **Maj 2023** | [GitHub Copilot bliver bedre til at forstå din kode](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inde i GitHub: Arbejde med LLM'erne bag GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jun 2023** | [Sådan skriver du bedre prompts til GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [.. GitHub Copilot går ud over Codex med forbedret AI-model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En udviklers guide til prompt engineering og LLM'er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Sådan bygger du en enterprise LLM-app: Lærdomme fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også gennemse deres [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere indlæg som [dette her](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), der viser, hvordan disse modeller og teknikker _anvendes_ til at drive virkelige applikationer.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Prompt Konstruktion

Vi har set, hvorfor prompt engineering er vigtigt – lad os nu forstå, hvordan prompts _konstrueres_, så vi kan evaluere forskellige teknikker for en mere effektiv promptdesign.

### Grundlæggende Prompt

Lad os starte med den grundlæggende prompt: en tekstinput sendt til modellen uden anden kontekst. Her er et eksempel – når vi sender de første ord af USAs nationalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), _færdiggør_ den straks svaret med de næste linjer, hvilket illustrerer den grundlæggende forudsigelsesadfærd.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det lyder som om, du starter teksten til "The Star-Spangled Banner," USA's nationalsang. Den fulde tekst er ...                           |

### Kompleks Prompt

Lad os nu tilføje kontekst og instruktioner til den grundlæggende prompt. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) giver os mulighed for at konstruere en kompleks prompt som en samling af _beskeder_ med:

- Input/output par, der reflekterer _brugerens_ input og _assistentens_ svar.
- Systembesked, der sætter konteksten for assistentens adfærd eller personlighed.

Forespørgslen har nu formen nedenfor, hvor _tokenisering_ effektivt fanger relevant information fra kontekst og samtale. Nu kan ændring af systemkonteksten have lige så stor indflydelse på kvaliteten af fuldførelser som de brugerinput, der gives.

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

### Instruktionsprompt

I ovenstående eksempler var brugerprompten en simpel tekstforespørgsel, som kan tolkes som en anmodning om information. Med _instruktions_-prompter kan vi bruge den tekst til at specificere en opgave mere detaljeret og give AI'en bedre vejledning. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruktionstype    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returnerede et simpelt afsnit_                                                                                              | Simpel              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returnerede et afsnit efterfulgt af en liste med nøglebegivenheders datoer og beskrivelser_                                             | Kompleks             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returnerer mere omfattende detaljer i en tekstboks, formateret som JSON, som du kan kopiere og indsætte til en fil og validere efter behov_ | Kompleks. Formateret. |

## Primært Indhold

I ovenstående eksempler var prompten stadig ret åben, hvilket tillod LLM’en at afgøre, hvilken del af sit fortrænede datasæt der var relevant. Med designmønstret _primært indhold_ opdeles inputteksten i to dele:

- en instruktion (handling)
- relevant indhold (der påvirker handlingen)

Her er et eksempel, hvor instruktionen er at "opsummere dette i 2 sætninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planet fra Solen og den største i Solsystemet. Den er en gaskæmpe med en masse, der er en tusindedel af Solens, men to og en halv gange massen af alle de andre planeter i Solsystemet tilsammen. Jupiter er et af de klareste objekter, som kan ses med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før den skrevne historie. Den er opkaldt efter den romerske gud Jupiter.[19] Når Jupiter ses fra Jorden, kan den være så lysstærk, at det reflekterede lys kaster synlige skygger,[20] og den er i gennemsnit det tredje mest lysende naturlige objekt på nattehimlen efter Månen og Venus. <br/> **Opsummer dette i 2 korte sætninger** | Jupiter, den femte planet fra Solen, er den største i Solsystemet og kendt for at være et af de lyseste objekter på nattehimlen. Opkaldt efter den romerske gud Jupiter, er det en gaskæmpe med en masse, der er to og en halv gang større end massen af alle de andre planeter i Solsystemet tilsammen. |

Den primære indholdsdel kan bruges på forskellige måder til at styre mere effektive instruktioner:

- **Eksempler** – i stedet for at fortælle modellen hvad den skal gøre med en eksplicit instruktion, giv den eksempler på, hvad der skal gøres, og lad den udlede mønsteret.
- **Signaler** – følg instruktionen med et "signal", der forbereder færdiggørelsen og guider modellen mod mere relevante svar.
- **Skabeloner** – disse er gentagelige ’opskrifter’ for prompts med pladsholdere (variabler), der kan tilpasses med data til specifikke anvendelsestilfælde.

Lad os udforske disse i praksis.

### Brug af Eksempler

Dette er en tilgang, hvor du bruger det primære indhold til at "fodre modellen" med nogle eksempler på det ønskede output for en given instruktion og lader den udlede mønsteret for det ønskede output. Afhængigt af antallet af eksempler kan vi have zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nu af tre komponenter:

- En opgavebeskrivelse
- Nogle få eksempler på det ønskede output
- Starten på et nyt eksempel (som bliver til en implicit opgavebeskrivelse)

| Læringstype  | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Oversæt til spansk                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Spilleren løb baserne => Baseball <br/> Spilleren ramte en ace => Tennis <br/> Spilleren slog en seks’er => Cricket <br/> Spilleren lavede et slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Bemærk, hvordan vi måtte give en eksplicit instruktion ("Oversæt til spansk") i zero-shot prompting, men det udledes i one-shot prompting-eksemplet. Few-shot-eksemplet viser, hvordan flere eksempler tillader modeller at foretage mere præcise slutninger uden yderligere instruktioner.

### Prompt Signaler

En anden teknik til brug af primært indhold er at give _signaler_ i stedet for eksempler. I dette tilfælde giver vi modellen et skub i den rigtige retning ved at _starte den_ med et uddrag, som afspejler den ønskede svarform. Modellen "tager signalet" for at fortsætte i samme stil.

| Antal signaler | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter er den femte planet fra Solen og den største i Solsystemet. Den er en gaskæmpe med en masse, der er en tusindedel af Solens, men to og en halv gange massen af alle de andre planeter i Solsystemet tilsammen. Jupiter er et af de klareste objekter, som kan ses med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før den skrevne historie. <br/>**Opsummer dette**                                       | Jupiter er den største planet i vores Solsystem og den femte fra Solen. Den er en gaskæmpe med en masse på 1/1000 af Solens, men den er tungere end alle de andre planeter tilsammen. Gamle civilisationer har kendt til Jupiter i lang tid, og den er nem at se på nattehimlen. |
| 1              | Jupiter er den femte planet fra Solen og den største i solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gang større end alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter synlige for det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før den skrevne historie. <br/>**Sammenfat dette** <br/> Hvad vi lærte er, at Jupiter | er den femte planet fra Solen og den største i solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gang større end alle de andre planeter tilsammen. Den er nemt synlig for det blotte øje og har været kendt siden oldtiden.                        |
| 2              | Jupiter er den femte planet fra Solen og den største i solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gang større end alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter synlige for det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før den skrevne historie. <br/>**Sammenfat dette** <br/> Top 3 fakta vi lærte:         | 1. Jupiter er den femte planet fra Solen og den største i solsystemet. <br/> 2. Det er en gasplanet med en masse, der er en tusindedel af Solens...<br/> 3. Jupiter har været synlig for det blotte øje siden oldtiden ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-skabeloner

En prompt-skabelon er en _foruddefineret opskrift til en prompt_, som kan gemmes og genbruges efter behov for at skabe mere konsekvente brugeroplevelser i stor skala. I sin enkleste form er det blot en samling af promt-eksempler som [dette fra OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), som både tilbyder de interaktive prompt-komponenter (bruger- og systemmeddelelser) og API-baseret anmodningsformat — for at støtte genbrug.

I en mere kompleks form som [dette eksempel fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) indeholder det _pladsholdere_, som kan erstattes med data fra forskellige kilder (brugerinput, systemkontekst, eksterne datakilder osv.) til dynamisk at generere en prompt. Dette gør det muligt at oprette et bibliotek af genanvendelige prompts, som kan bruges til at skabe konsekvente brugeroplevelser **programmatisk** i stor skala.

Endelig ligger den egentlige værdi i skabeloner i evnen til at oprette og publicere _prompt-biblioteker_ til vertikale applikationsdomæner – hvor prompt-skabelonen nu er _optimeret_ til at reflektere applikationsspecifik kontekst eller eksempler, der gør svarene mere relevante og præcise for den målrettede brugergruppe. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repositioriet er et glimrende eksempel på denne tilgang, hvor man kuraterer et bibliotek af prompts til uddannelsessektoren med fokus på nøglemål som lektionsplanlægning, curriculum design, studentervejledning osv.

## Understøttende indhold

Hvis vi betragter prompt-konstruktion som bestående af en instruktion (opgave) og et mål (primært indhold), så er _sekundært indhold_ som yderligere kontekst, vi giver for at **influere output på en eller anden måde**. Det kan være tuningparametre, formateringsinstruktioner, emnetaksonomier osv., som kan hjælpe modellen med at _tilpasse_ sit svar, så det passer til de ønskede brugerformål eller forventninger.

For eksempel: Givet en kursuskatalog med omfattende metadata (navn, beskrivelse, niveau, metadata-tags, underviser osv.) for alle tilgængelige kurser i pensum:

- kan vi definere en instruktion til "opsummere kursuskataloget for efteråret 2023"
- kan vi bruge det primære indhold til at give nogle få eksempler på ønsket output
- kan vi bruge det sekundære indhold til at identificere de 5 vigtigste "tags".

Nu kan modellen levere et sammendrag i det format, som vises i eksemplerne – men hvis et resultat har flere tags, kan den prioritere de 5 tags, der er identificeret i det sekundære indhold.

---

<!--
LEKTIONSSKABELON:
Denne enhed skal dække kernekoncept #1.
Styrk konceptet med eksempler og referencer.

KONCEPT #3:
Prompt Engineering-teknikker.
Hvad er nogle grundlæggende teknikker inden for prompt engineering?
Illustrer det med nogle øvelser.
-->

## Bedste praksis for promptning

Nu, hvor vi ved, hvordan prompts kan _konstrueres_, kan vi begynde at tænke over, hvordan man _designer_ dem, så de afspejler bedste praksis. Vi kan tænke på dette i to dele – at have den rette _tankegang_ og anvende de rette _teknikker_.

### Prompt Engineering-tankegang

Prompt Engineering er en process med prøve og fejl, så husk tre brede vejledende faktorer:

1. **Domæneforståelse betyder noget.** Svart nøjagtighed og relevans afhænger af det _domæne_, som applikationen eller brugeren arbejder i. Anvend din intuition og domæneekspertise til at **tilpasse teknikkerne** yderligere. Definer for eksempel _domænespecifikke personligheder_ i dine system-prompt, eller brug _domænespecifikke skabeloner_ i dine bruger-prompt. Giv sekundært indhold, der afspejler domænespecifik kontekst, eller brug _domænespecifikke signaler og eksempler_ for at guide modellen hen mod kendte brugsmønstre.

2. **Modelforståelse betyder noget.** Vi ved, at modeller er stokastiske af natur. Men modelimplementeringer kan også variere med hensyn til træningsdatasæt (forudtrænet viden), kapaciteter (fx via API eller SDK) og typen af indhold, de er optimeret til (fx kode vs. billeder vs. tekst). Forstå styrker og begrænsninger ved den model, du bruger, og brug den viden til at _prioritere opgaver_ eller bygge _tilpassede skabeloner_, der er optimeret til modellens kapaciteter.

3. **Iteration & validering betyder noget.** Modeller udvikler sig hurtigt, og det gør teknikkerne til prompt engineering også. Som domæneekspert kan du have anden kontekst eller kriterier for _din_ specifikke applikation, som ikke gælder for det bredere fællesskab. Brug prompt engineering-værktøjer og teknikker til at "sætte gang i" prompt-konstrueringen, og iterer og valider resultaterne ved hjælp af din egen intuition og domæneekspertise. Optag dine indsigter og opret en **vidensbase** (fx prompt-biblioteker), der kan bruges som et nyt udgangspunkt af andre for hurtigere iterationer i fremtiden.

## Bedste praksis

Lad os nu se på almindelige bedste praksis, som anbefales af [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikere.

| Hvad                              | Hvorfor                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluer de nyeste modeller.       | Nye modelgenerationer har sandsynligvis forbedrede funktioner og kvalitet – men kan også medføre højere omkostninger. Evaluer deres effekt og træf så beslutninger om migrering.                                                                    |
| Adskil instruktioner & kontekst   | Undersøg om din model/udbyder definerer _afgrænsere_ til tydeligere at skelne instruktioner, primært og sekundært indhold. Dette kan hjælpe modeller med mere præcist at tildele vægte til tokens.                                                 |
| Vær specifik og klar              | Giv flere detaljer om ønsket kontekst, resultat, længde, format, stil osv. Dette vil forbedre både kvalitet og konsistens i svarene. Fang opskrifter i genanvendelige skabeloner.                                                                     |
| Vær beskrivende, brug eksempler   | Modeller reagerer ofte bedre på en "vis og fortæl"-metode. Start med en `zero-shot`-metode, hvor du giver en instruktion (men ingen eksempler), og prøv derefter `few-shot` som en forbedring ved at give nogle få eksempler på det ønskede output. Brug analogier. |
| Brug cues til at kickstarte svar  | Få modellen til at bevæge sig mod et ønsket resultat ved at give nogle førende ord eller vendinger, som den kan bruge som udgangspunkt for svaret.                                                                                                |
| Gentag                           | Nogle gange skal du gentage dig selv over for modellen. Giv instruktioner før og efter dit primære indhold, brug en instruktion og en cue osv. Iterer og valider for at se, hvad der virker.                                                         |
| Rækkefølgen betyder noget        | Den rækkefølge, du præsenterer information for modellen i, kan påvirke output, også i læringseksempler, på grund af recent bias. Prøv forskellige muligheder for at se, hvad der virker bedst.                                                       |
| Giv modellen en “udvej”           | Giv modellen et _backup_-svar, den kan bruge, hvis den ikke kan fuldføre opgaven af en eller anden grund. Dette kan reducere risikoen for, at modeller laver falske eller fabrikerede svar.                                                             |
|                                  |                                                                                                                                                                                                                                                     |

Som med enhver bedste praksis, så husk at _din oplevelse kan variere_ baseret på model, opgave og domæne. Brug disse som udgangspunkt, og iterer for at finde, hvad der fungerer bedst for dig. Evaluér løbende din prompt engineering-proces, efterhånden som nye modeller og værktøjer bliver tilgængelige, med fokus på proces-skalerbarhed og svar-kvalitet.

<!--
LEKTIONSSKABELON:
Denne enhed skal tilbyde en kodeudfordring, hvis relevant

UDFORDRING:
Link til en Jupyter Notebook med kun kodekommentarerne i instruktionerne (kodeafsnit er tomme).

LØSNING:
Link til en kopi af den Notebook med udfyldte og kørte prompts, som viser, hvordan et eksempel kan se ud.
-->

## Opgave

Tillykke! Du nåede til slutningen af lektionen! Det er tid til at prøve nogle af de koncepter og teknikker af med rigtige eksempler!

Til vores opgave vil vi bruge en Jupyter Notebook med øvelser, du kan gennemføre interaktivt. Du kan også udvide Notebooken med dine egne Markdown- og kodeceller for at udforske ideer og teknikker på egen hånd.

### For at komme i gang, fork repositoriet, og

- (Anbefalet) Start GitHub Codespaces
- (Alternativt) Klon repositoriet til din lokale enhed og brug det med Docker Desktop
- (Alternativt) Åbn Notebooken i dit foretrukne Notebook-runtime miljø.

### Dernæst konfigurer dine miljøvariabler

- Kopiér `.env.copy`-filen i repository-roden til `.env` og udfyld `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT` værdierne. Kom tilbage til afsnittet [Learning Sandbox](#læringssandbox) for at lære hvordan.

### Dernæst åbn Jupyter Notebooken

- Vælg runtime-kernen. Hvis du bruger metode 1 eller 2, skal du blot vælge den forudindstillede Python 3.10.x-kernel, som dev-containeren leverer.

Du er klar til at køre øvelserne. Bemærk, at der ikke findes _rigtige og forkerte_ svar her – det handler blot om at udforske muligheder gennem prøve og fejl og opbygge intuition for, hvad der virker for en bestemt model og applikationsdomæne.

_Afstemningsmæssigt er der derfor ikke kode-løsningssegmenter i denne lektion. I stedet indeholder Notebooken markdown-celler med titlen "Min løsning:", som viser et eksempel på output til reference._

 <!--
LEKTIONSSKABELON:
Afslut afsnittet med et resumé og ressourcer til selvstyret læring.
-->

## Videnscheck

Hvilken af følgende er en god prompt, der følger rimelig bedste praksis?

1. Vis mig et billede af en rød bil  
2. Vis mig et billede af en rød bil af mærke Volvo og model XC90 parkeret ved en klippe med solen gående ned  
3. Vis mig et billede af en rød bil af mærke Volvo og model XC90

A: 2, det er den bedste prompt, fordi den giver detaljer om "hvad" og går i detaljer (ikke bare en hvilken som helst bil, men et specifikt mærke og model) og beskriver også den overordnede scene. 3 er næstbedst, da den også indeholder mange beskrivelser.

## 🚀 Udfordring

Se om du kan udnytte "cue"-teknikken med prompten: Fuldfør sætningen "Vis mig et billede af en rød bil af mærke Volvo og ". Hvad svarer den, og hvordan vil du forbedre det?

## Fantastisk arbejde! Fortsæt din læring

Vil du lære mere om forskellige begreber inden for Prompt Engineering? Gå til [den fortsatte læringsside](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at finde andre gode ressourcer om dette emne.

Tag hen til Lektion 5, hvor vi vil se på [avancerede prompting-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->