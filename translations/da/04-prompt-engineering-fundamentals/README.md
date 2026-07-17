# Grundlæggende om Prompt Engineering

[![Grundlæggende om Prompt Engineering](../../../translated_images/da/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduktion
Denne modul dækker væsentlige koncepter og teknikker til at skabe effektive prompts i generative AI-modeller. Måden du skriver din prompt til en LLM på, betyder også noget. En omhyggeligt udformet prompt kan opnå en bedre kvalitet af svaret. Men hvad betyder termer som _prompt_ og _prompt engineering_ egentlig? Og hvordan forbedrer jeg det prompt _input_, jeg sender til LLM'en? Det er de spørgsmål, vi vil forsøge at besvare i dette kapitel og det næste.

_Generativ AI_ kan skabe nyt indhold (fx tekst, billeder, lyd, kode osv.) som svar på brugerforespørgsler. Det gør den ved hjælp af _Large Language Models_ som OpenAI’s GPT ("Generative Pre-trained Transformer") serie, der er trænet til at bruge naturligt sprog og kode.

Brugere kan nu interagere med disse modeller ved hjælp af velkendte paradigmer som chat, uden at have teknisk ekspertise eller træning. Modellerne er _prompt-baserede_ – brugere sender en tekstinput (prompt) og får AI-svaret (completion) tilbage. De kan derefter "chatte med AI'en" iterativt, i flere runder, og forbedre deres prompt, indtil svaret matcher deres forventninger.

"Prompts" bliver nu det primære _programmeringsinterface_ for generative AI-apps, der fortæller modellerne, hvad de skal gøre, og påvirker kvaliteten af de returnerede svar. "Prompt Engineering" er et hastigt voksende studieområde, der fokuserer på _design og optimering_ af prompts for at levere konsistente og kvalitetsmæssige svar i stor skala.

## Læringsmål

I denne lektion lærer vi, hvad Prompt Engineering er, hvorfor det betyder noget, og hvordan vi kan udforme mere effektive prompts til en given model og applikationsmål. Vi vil forstå kernekoncepter og bedste praksis for prompt engineering – og lære om et interaktivt Jupyter Notebook "sandbox"-miljø, hvor vi kan se disse koncepter anvendt i virkelige eksempler.

I slutningen af denne lektion vil vi kunne:

1. Forklare hvad prompt engineering er og hvorfor det er vigtigt.
2. Beskrive komponenterne i en prompt og hvordan de bruges.
3. Lære bedste praksis og teknikker til prompt engineering.
4. Anvende lærte teknikker på virkelige eksempler ved hjælp af et OpenAI-endpoint.

## Centrale termer

Prompt Engineering: Praksis med at designe og forfine input for at guide AI-modeller mod at producere ønskede output.
Tokenisering: Processen med at omdanne tekst til mindre enheder, kaldet tokens, som en model kan forstå og behandle.
Instruktions-trænede LLM'er: Store sprogmodeller (LLM'er), der er finjusteret med specifikke instruktioner for at forbedre deres svarkvalitet og relevans.

## Læringssandbox

Prompt engineering er i øjeblikket mere en kunst end en videnskab. Den bedste måde at forbedre vores intuition på er at _øve mere_ og anvende en trial-and-error tilgang, der kombinerer domæneekspertise med anbefalede teknikker og model-specifikke optimeringer.

Jupyter Notebook'en, der følger med denne lektion, tilbyder et _sandbox_-miljø, hvor du kan prøve det, du lærer – løbende eller som en del af kodeudfordringen til sidst. For at udføre øvelserne skal du bruge:

1. **En Azure OpenAI API-nøgle** – service-endpointet for en udrullet LLM.
2. **Et Python Runtime** – hvor Notebook kan køres.
3. **Lokale miljøvariabler** – _fuldfør [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) trin nu for at være klar_.

Notebook'en indeholder _starter_-øvelser – men du opfordres til at tilføje dine egne _Markdown_ (beskrivelse) og _Code_ (prompt-forespørgsler) sektioner for at prøve flere eksempler eller idéer – og opbygge din intuition for prompt-design.

## Illustreret guide

Vil du have det store overblik over, hvad denne lektion dækker, inden du går i gang? Tjek denne illustrerede guide, som giver dig en fornemmelse af hovedemnerne og nøglepointerne til eftertanke i hver enkelt. Lektionens køreplan tager dig fra forståelse af kernekoncepter og udfordringer til at håndtere dem med relevante prompt-engineering teknikker og bedste praksis. Bemærk at sektionen "Avancerede teknikker" i denne guide henviser til indhold, der dækkes i det _næste_ kapitel i dette kursusforløb.

![Illustreret guide til Prompt Engineering](../../../translated_images/da/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vores Startup

Lad os nu tale om, hvordan _dette emne_ relaterer sig til vores startup-mission om at [bringe AI-innovation til uddannelse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker at bygge AI-drevne applikationer til _personlig læring_ – så lad os tænke over, hvordan forskellige brugere af vores applikation kunne "designe" prompts:

- **Administratorer** kunne bede AI'en om at _analysere læseplansdata for at identificere huller i dækningen_. AI'en kan opsummere resultater eller visualisere dem med kode.
- **Undervisere** kunne bede AI om at _generere en lektionsplan for en målgruppe og et emne_. AI'en kan bygge den personlige plan i et specificeret format.
- **Studerende** kunne bede AI om at _vejlede dem i et svært fag_. AI'en kan nu guide studerende med lektioner, hints og eksempler tilpasset deres niveau.

Det er kun toppen af isbjerget. Tjek [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et open-source prompts bibliotek kurateret af uddannelseseksperter – for at få et bredere indblik i mulighederne! _Prøv at køre nogle af disse prompts i sandkassen eller brug OpenAI Playground for at se, hvad der sker!_

<!--
LESSON TEMPLATE:
Denne enhed skal dække kernekoncept #1.
Understøt konceptet med eksempler og referencer.

KONCEPT #1:
Prompt Engineering.
Definer det og forklar hvorfor det er nødvendigt.
-->

## Hvad er Prompt Engineering?

Vi startede denne lektion med at definere **Prompt Engineering** som processen med at _designe og optimere_ tekstinput (prompts) for at levere konsistente og kvalitetsmæssige svar (completions) til et givet applikationsmål og model. Vi kan tænke på dette som en 2-trins proces:

- _designe_ den oprindelige prompt til en given model og målsætning
- _forfine_ prompten iterativt for at forbedre kvaliteten af svaret

Dette er nødvendigvis en trial-and-error proces, der kræver brugerintuition og indsats for at opnå optimale resultater. Så hvorfor er det vigtigt? For at besvare det spørgsmål, skal vi først forstå tre koncepter:

- _Tokenisering_ = hvordan modellen "ser" prompten
- _Basis LLM'er_ = hvordan fundamentmodellen "behandler" en prompt
- _Instruktions-trænede LLM'er_ = hvordan modellen nu kan "se opgaver"

### Tokenisering

En LLM opfatter prompts som en _sekvens af tokens_, hvor forskellige modeller (eller versioner af en model) kan tokenisere den samme prompt på forskellige måder. Da LLM'er er trænet på tokens (og ikke rå tekst), har måden prompts bliver tokeniseret på en direkte indflydelse på kvaliteten af det genererede svar.

For at få en intuition for, hvordan tokenisering fungerer, kan du prøve værktøjer som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), vist nedenfor. Kopiér din prompt ind – og se hvordan det bliver konverteret til tokens, med opmærksomhed på, hvordan mellemrumstegn og tegnsætning håndteres. Bemærk, at dette eksempel viser en ældre LLM (GPT-3) – så at prøve dette med en nyere model kan give et andet resultat.

![Tokenisering](../../../translated_images/da/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Foundation Models

Når en prompt er tokeniseret, er hovedfunktionen for ["Basis LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller Fundamentmodellen) at forudsige det næste token i sekvensen. Da LLM'er er trænet på massive tekstdatasæt, har de en god fornemmelse af de statistiske relationer mellem tokens og kan lave denne forudsigelse med en vis sikkerhed. Bemærk, at de ikke forstår _meningen_ med ordene i prompten eller tokenet; de ser blot et mønster, de kan "fuldføre" med deres næste forudsigelse. De kan fortsætte med at forudsige sekvensen indtil de bliver stoppet af brugerens indgriben eller en forudbestemt betingelse.

Vil du se, hvordan prompt-baseret completion virker? Indtast den ovenstående prompt i [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) med standardindstillingerne. Systemet er konfigureret til at behandle prompts som informationsforespørgsler – så du skulle se et svar, der tilfredsstiller denne kontekst.

Men hvad hvis brugeren ønskede at se noget specifikt, der opfyldte nogle kriterier eller et opgaveformål? Det er her, _instruktions-trænede_ LLM'er kommer i spil.

![Basis LLM Chat Completion](../../../translated_images/da/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruktions-trænede LLM'er

En [Instruktions-trænet LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med fundamentmodellen og finjusterer den med eksempler eller input/output par (fx multi-turn "beskeder"), som kan indeholde klare instruktioner – og AI'ens svar forsøger at følge disse instruktioner.

Dette bruger teknikker som Forstærkningslæring med Menneskelig Feedback (RLHF), som kan træne modellen til at _følge instruktioner_ og _lære af feedback_, så den producerer svar, der er bedre egnet til praktiske anvendelser og mere relevante for brugerens mål.

Lad os prøve det – vend tilbage til prompten ovenfor, men ændr nu _systembeskeden_ til at give følgende instruktion som kontekst:

> _Opsummer det indhold, du får, til en elev i 2. klasse. Hold resultatet til ét afsnit med 3-5 punktopstillinger._

Se hvordan resultatet nu er tilpasset til det ønskede mål og format? En underviser kan nu bruge dette svar direkte i deres slides til den klasse.

![Instruktions-trænet LLM Chat Completion](../../../translated_images/da/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Hvorfor har vi brug for Prompt Engineering?

Nu hvor vi ved, hvordan prompts behandles af LLM'er, lad os tale om _hvorfor_ vi har brug for prompt engineering. Svaret ligger i, at de nuværende LLM'er udgør en række udfordringer, som gør _pålidelige og konsistente svar_ sværere at opnå uden indsats i promptkonstruktion og optimering. For eksempel:

1. **Modellernes svar er stokastiske.** Den _samme prompt_ vil sandsynligvis producere forskellige svar med forskellige modeller eller modelversioner. Det kan endda give forskellige resultater med _samme model_ på forskellige tidspunkter. _Prompt engineering teknikker kan hjælpe os med at minimere disse variationer ved at give bedre rammer_.

1. **Modeller kan finde på svar.** Modeller er fortrænet med _store men begrænsede_ datasæt, hvilket betyder, at de mangler viden om begreber uden for træningssættet. Som følge heraf kan de producere svar, der er unøjagtige, opdigtede eller direkte modstridende med kendte fakta. _Prompt engineering teknikker hjælper brugere med at identificere og afbøde sådanne opdigtninger, fx ved at bede AI’en om kildeangivelser eller begrundelser_.

1. **Modellers kapaciteter vil variere.** Nyere modeller eller modelgenerationer vil have rigere kapaciteter, men også bringe unikke særheder og afvejninger i pris og kompleksitet. _Prompt engineering kan hjælpe os med at udvikle bedste praksis og arbejdsprocesser, der abstraherer forskelle og tilpasses model-specifikke krav på skalerbare, sømløse måder_.

Lad os se dette i praksis i OpenAI eller Azure OpenAI Playground:

- Brug den samme prompt med forskellige LLM-udrulninger (fx OpenAI, Azure OpenAI, Hugging Face) – så du variationerne?
- Brug den samme prompt gentagne gange med _samme_ LLM-udrulning (fx Azure OpenAI playground) – hvordan adskilte disse variationer sig?

### Eksempel på opdigtninger

I dette kursus bruger vi termen **"opdigtning"** til at referere til fænomenet, hvor LLM'er nogle gange genererer faktuelt forkerte oplysninger på grund af begrænsninger i deres træning eller andre begrænsninger. Du har måske også hørt dette omtalt som _"hallucinationer"_ i populære artikler eller forskningspapirer. Vi anbefaler dog kraftigt at bruge _"opdigtning"_ som termen for ikke utilsigtet at menneskeliggøre adfærden ved at tillægge en menneskelig egenskab til et maskindrevet resultat. Dette understøtter også [Ansvarlig AI-retningslinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologiperspektiv ved at fjerne termer, som også kan opfattes som stødende eller ikke-inkluderende i visse kontekster.

Vil du have en fornemmelse af, hvordan opdigtninger virker? Tænk på en prompt, der instruerer AI'en til at generere indhold om et ikke-eksisterende emne (for at sikre, at det ikke findes i træningsdatasættet). For eksempel prøvede jeg denne prompt:

> **Prompt:** generer en lektionsplan om den marsianske krig i 2076.

Et websøg viste mig, at der findes fiktive beretninger (fx tv-serier eller bøger) om marsianske krige – men ingen i 2076. Sund fornuft fortæller os også, at 2076 er _i fremtiden_ og derfor ikke kan associeres med en virkelig begivenhed.


Så hvad sker der, når vi kører denne prompt med forskellige LLM-udbydere?

> **Svar 1**: OpenAI Playground (GPT-35)

![Svar 1](../../../translated_images/da/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Svar 2](../../../translated_images/da/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Svar 3](../../../translated_images/da/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som forventet producerer hver model (eller modelversion) lidt forskellige svar takket være stokastisk adfærd og variationer i modelkapacitet. For eksempel retter én model sig mod et 8. klasses publikum, mens en anden antager en gymnasieelev. Men alle tre modeller genererede svar, der kunne overbevise en uvidende bruger om, at begivenheden var ægte.

Prompt-engineering teknikker som _metaprompting_ og _temperaturkonfiguration_ kan til en vis grad reducere model-opdigtninger. Nye prompt engineering _arkitekturer_ integrerer også nye værktøjer og teknikker problemfrit i prompt-flowet for at afbøde eller reducere nogle af disse effekter.

## Case Study: GitHub Copilot

Lad os afslutte dette afsnit med at få en fornemmelse af, hvordan prompt engineering bruges i virkelige løsninger ved at kigge på et Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI parprogrammer" - det konverterer tekstprompter til kodefuldførelser og er integreret i dit udviklingsmiljø (f.eks. Visual Studio Code) for en problemfri brugeroplevelse. Som dokumenteret i serien af blogs nedenfor, var den tidligste version baseret på OpenAI Codex-modellen – med ingeniører der hurtigt indså behovet for at finjustere modellen og udvikle bedre prompt engineering-teknikker for at forbedre kodekvaliteten. I juli [introducede de en forbedret AI-model, der går ud over Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for endnu hurtigere forslag.

Læs indlæggene i rækkefølge for at følge deres læringsrejse.

- **Maj 2023** | [GitHub Copilot bliver bedre til at forstå din kode](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inside GitHub: Arbejde med LLM'erne bag GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Hvordan man skriver bedre prompts til GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juli 2023** | [.. GitHub Copilot går ud over Codex med forbedret AI-model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juli 2023** | [En udviklers guide til prompt engineering og LLM'er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hvordan man bygger en enterprise LLM-app: Lærdomme fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også browse deres [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere indlæg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), som viser, hvordan disse modeller og teknikker _anvendes_ til at drive virkelige applikationer.

---

<!--
LEKTIONSSKABELON:
Denne enhed bør dække kernebegreb #2.
Forstærk begrebet med eksempler og referencer.

BEGREB #2:
Prompt Design.
Illustreret med eksempler.
-->

## Prompt-opbygning

Vi har set, hvorfor prompt engineering er vigtigt - nu lad os forstå, hvordan prompter _opbygges_ så vi kan evaluere forskellige teknikker til mere effektiv promptdesign.

### Grundlæggende Prompt

Lad os starte med den grundlæggende prompt: en tekstinput sendt til modellen uden anden kontekst. Her er et eksempel – når vi sender de første par ord af USA's nationalhymne til OpenAI's [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), fuldfører den straks svaret med de næste linjer, og illustrerer den grundlæggende forudsigelsesadfærd.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det lyder som om, du starter teksten til "The Star-Spangled Banner," USA's nationalhymne. Hele teksten er ... |

### Kompleks Prompt

Lad os nu tilføje kontekst og instruktioner til den grundlæggende prompt. [Chat Completion API'en](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) giver os mulighed for at konstruere en kompleks prompt som en samling af _beskeder_ med:

- Input/output-par, der afspejler _bruger_-input og _assistent_-svar.
- Systembesked, der sætter konteksten for assistentens adfærd eller personlighed.

Anmodningen er nu i formen nedenfor, hvor _tokeniseringen_ effektivt fanger relevant information fra kontekst og samtale. At ændre systemets kontekst kan nu have lige så stor indvirkning på kvaliteten af fuldførelserne som brugerens input.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruktionsprompt

I ovenstående eksempler var brugerprompten en simpel tekstforespørgsel, der kan tolkes som en anmodning om information. Med _instruktions_-prompter kan vi bruge den tekst til at specificere en opgave mere detaljeret, hvilket giver bedre vejledning til AI'en. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruktionstype   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returnerede et simpelt afsnit_                                                                                             | Simpel             |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returnerede et afsnit efterfulgt af en liste over nøglebegivenhedsdatoer med beskrivelser_                                  | Kompleks           |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returnerer mere omfattende detaljer i en tekstboks, formateret som JSON, som du kan kopiere og validere efter behov_         | Kompleks. Formateret. |

## Primært Indhold

I ovenstående eksempler var prompten stadig ret åben, hvilket tillod LLM at beslutte, hvilken del af dets fortrænede datasæt der var relevant. Med designmønsteret _primært indhold_ opdeles inputteksten i to dele:

- en instruktion (handling)
- relevant indhold (der påvirker handlingen)

Her er et eksempel, hvor instruktionen er "opsummér dette i 2 sætninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planet fra Solen og den største i Solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gange massen af alle de andre planeter i Solsystemet tilsammen. Jupiter er et af de klart lysende objekter, der er synlige med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før nedskrevet historie. Den er opkaldt efter den romerske gud Jupiter.[19] Når man ser på Jupiter fra Jorden, kan den være så lysstærk, at det reflekterede lys kan kaste synlige skygger,[20] og den er i gennemsnit det tredjelysteste naturlige objekt på nattehimlen efter Månen og Venus. <br/> **Opsummér dette i 2 korte sætninger** | Jupiter, den femte planet fra Solen, er den største i Solsystemet og er kendt for at være et af de klareste objekter på nattehimlen. Opkaldt efter den romerske gud Jupiter, er det en gasplanet med en masse, der er to og en halv gang så stor som alle andre planeter i Solsystemet tilsammen. |

Segmentet for det primære indhold kan bruges på forskellige måder til at drive mere effektive instruktioner:

- **Eksempler** - i stedet for at fortælle modellen, hvad den skal gøre med en eksplicit instruktion, giv den eksempler på, hvad den skal gøre og lad den udlede mønsteret.
- **Knep** - følg instruktionen med et "kneb", der primet fuldførelsen og guider modellen mod mere relevante svar.
- **Skabeloner** - det er gentagelige 'opskrifter' til prompter med pladsholdere (variable), der kan tilpasses med data til specifikke anvendelsestilfælde.

Lad os udforske disse i praksis.

### Brug af Eksempler

Dette er en tilgang, hvor du bruger det primære indhold til at "fodre modellen" med nogle eksempler på det ønskede output for en given instruktion og lade den udlede mønsteret for det ønskede output. Baseret på antallet af leverede eksempler kan vi have zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nu af tre komponenter:

- En opgavebeskrivelse
- Nogle få eksempler på det ønskede output
- Starten på et nyt eksempel (der bliver en implicit opgavebeskrivelse)

| Læringstype | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Oversæt til spansk                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Spilleren løb omkring baserne => Baseball <br/> Spilleren servede en ace => Tennis <br/> Spilleren slog en six'er => Cricket <br/> Spilleren lavede en slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Bemærk hvordan vi måtte give eksplicit instruktion ("Oversæt til spansk") i zero-shot prompting, men det udledes i one-shot prompt-eksemplet. Few-shot-eksemplet viser, hvordan tilføjelse af flere eksempler tillader modeller mere præcise slutninger uden yderligere instruktioner.

### Prompt Knep

En anden teknik til brug af primært indhold er at give _knep_ frem for eksempler. I dette tilfælde giver vi modellen et skub i den rigtige retning ved at _starte den_ med et uddrag, der reflekterer ønsket svartype. Modellen "tager så signalet" og fortsætter i samme stil.

| Antal Knep | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0          | Jupiter er den femte planet fra Solen og den største i Solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gange massen af alle de andre planeter i Solsystemet tilsammen. Jupiter er et af de klart lysende objekter, der er synlige med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før nedskrevet historie. <br/>**Opsummér dette**                                       | Jupiter er den største planet i vores Solsystem og den femte fra Solen. Det er en gasplanet med en masse på 1/1000 af Solens, men den er tungere end alle de andre planeter tilsammen. Gamle civilisationer har kendt til Jupiter i lang tid, og den er let synlig på nattehimlen.. |
| 1          | Jupiter er den femte planet fra Solen og den største i Solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gange massen af alle de andre planeter i Solsystemet tilsammen. Jupiter er et af de klart lysende objekter, der er synlige med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før nedskrevet historie. <br/>**Opsummér dette** <br/> Det, vi lærte, er, at Jupiter | er den femte planet fra Solen og den største i Solsystemet. Det er en gasplanet med en masse, der er en tusindedel af Solens, men to og en halv gange massen af alle de andre planeter tilsammen. Den er let synlig for det blotte øje og har været kendt siden oldtiden.                        |

| 2              | Jupiter er den femte planet fra Solen og den største i solsystemet. Det er en gas-kæmpe med en masse på en tusindedel af Solens, men to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. Jupiter er et af de lyseste objekter synlige med det blotte øje på nattehimlen og har været kendt af gamle civilisationer siden før den skrevne historie. <br/>**Opsummer dette** <br/> Top 3 fakta vi lærte:         | 1. Jupiter er den femte planet fra Solen og den største i solsystemet. <br/> 2. Det er en gas-kæmpe med en masse på en tusindedel af Solens...<br/> 3. Jupiter har været synlig med det blotte øje siden oldtiden ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-skabeloner

En prompt-skabelon er en _foruddefineret opskrift på en prompt_, der kan gemmes og genbruges efter behov for at skabe mere konsistente brugeroplevelser i stor skala. I sin enkleste form er det blot en samling af promt-eksempler som [dette fra OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), der både giver de interaktive prompt-komponenter (bruger- og systembeskeder) og det API-drevne anmodningsformat - for at understøtte genbrug.

I dens mere komplekse form som [dette eksempel fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) indeholder den _pladsholdere_, der kan erstattes med data fra forskellige kilder (brugerinput, systemkontekst, eksterne datakilder osv.) for dynamisk at generere en prompt. Dette giver os mulighed for at skabe et bibliotek af genanvendelige prompts, der kan bruges til at skabe konsistente brugeroplevelser **programmatisk** i stor skala.

Endelig ligger den reelle værdi af skabeloner i evnen til at skabe og offentliggøre _prompt-biblioteker_ for vertikale anvendelsesområder - hvor prompt-skabelonen nu er _optimeret_ til at afspejle applikationsspecifik kontekst eller eksempler, der gør svarene mere relevante og præcise for den målrettede brugerskare. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)-arkivet er et godt eksempel på denne tilgang, der kuraterer et bibliotek af prompts til uddannelsesdomænet med fokus på nøglemål som lektionsplanlægning, læseplan-design, elevvejledning osv.

## Understøttende indhold

Hvis vi tænker på prompt-konstruktion som at have en instruktion (opgave) og et mål (primært indhold), så er _sekundært indhold_ som yderligere kontekst, vi giver for at **påvirke outputtet på en eller anden måde**. Det kan være justeringsparametre, formateringsinstruktioner, emnetaksonomier osv., der kan hjælpe modellen med at _tilpasse_ sit svar, så det passer til de ønskede brugerformål eller forventninger.

For eksempel: Givet et kursuskatalog med omfattende metadata (navn, beskrivelse, niveau, metadatatags, underviser osv.) for alle tilgængelige kurser i læseplanen:

- vi kan definere en instruktion om at "opsummere kursuskataloget for efteråret 2023"
- vi kan bruge det primære indhold til at give nogle få eksempler på det ønskede output
- vi kan bruge det sekundære indhold til at identificere de 5 vigtigste "tags" af interesse.

Nu kan modellen levere en opsummering i det format, som vises af de få eksempler - men hvis et resultat har flere tags, kan den prioritere de 5 tags identificeret i det sekundære indhold.

---

<!--
LEKTIONS SKABELON:
Denne enhed skal dække kernekoncept #1.
Forstærk konceptet med eksempler og referencer.

KONCEPT #3:
Prompt Engineering teknikker.
Hvad er nogle grundlæggende teknikker til prompt engineering?
Illustrer det med nogle øvelser.
-->

## De bedste praksisser for promptning

Nu hvor vi ved, hvordan prompts kan _konstrueres_, kan vi begynde at tænke over, hvordan man _designer_ dem for at afspejle bedste praksis. Vi kan tænke på dette i to dele - at have den rette _mindset_ og anvende de rette _teknikker_.

### Mindset for Prompt Engineering

Prompt Engineering er en prøv-og-fejl proces, så husk på tre brede vejledende faktorer:

1. **Domæneforståelse betyder noget.** Svarenes nøjagtighed og relevans afhænger af det _domæne_, hvor applikationen eller brugeren opererer. Anvend din intuition og domænefaring til at **tilpasse teknikkerne** yderligere. For eksempel, definer _domænespecifikke personligheder_ i dine systemprompter, eller brug _domænespecifikke skabeloner_ i dine brugerprompter. Giv sekundært indhold, der afspejler domænespecifikke kontekster, eller brug _domænespecifikke hints og eksempler_ til at styre modellen mod velkendte brugsmønstre.

2. **Modelforståelse betyder noget.** Vi ved, at modeller er stokastiske af natur. Men modelimplementeringer kan også variere med hensyn til det træningsdataset, de bruger (forudindlært viden), de funktioner de tilbyder (f.eks. via API eller SDK) og den type indhold, de er optimeret til (f.eks. kode vs. billeder vs. tekst). Forstå styrker og begrænsninger ved den model, du bruger, og brug den viden til at _prioritere opgaver_ eller bygge _tilpassede skabeloner_, der er optimeret til modellens kapaciteter.

3. **Iteration & validering betyder noget.** Modeller udvikler sig hurtigt, og det samme gør teknikkerne for prompt engineering. Som domæneekspert kan du have andre kontekster eller kriterier for _din_ specifikke applikation, som måske ikke gælder for det bredere fællesskab. Brug værktøjer og teknikker til prompt engineering for at "kickstarte" prompt-konstruktionen, og iterer derefter og valider resultaterne ved hjælp af din egen intuition og domænefaring. Optag dine indsigter og opret en **vidensbase** (f.eks. prompt-biblioteker), der kan bruges som en ny baseline af andre til hurtigere iterationer i fremtiden.

## Bedste Praksisser

Lad os nu se på de almindelige bedste praksisser, som anbefales af [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikere.

| Hvad                             | Hvorfor                                                                                                                                                                                                                                            |
| :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluer de nyeste modeller.      | Nye modelgenerationer har sandsynligvis forbedrede funktioner og kvalitet - men kan også medføre højere omkostninger. Evaluer dem for effekt, og træf så beslutninger om migration.                                                               |
| Adskil instruktioner & kontekst  | Tjek om din model/udbyder definerer _afgrænsere_ til klarere at skelne mellem instruktioner, primært og sekundært indhold. Dette kan hjælpe modeller med at tildele vægt mere præcist til tokens.                                                  |
| Vær specifik og klar             | Giv flere detaljer om den ønskede kontekst, resultat, længde, format, stil osv. Dette forbedrer både kvalitet og konsistens af svarene. Capturere opskrifter i genanvendelige skabeloner.                                                        |
| Vær beskrivende, brug eksempler | Modeller reagerer ofte bedre på en "vis og fortæl" tilgang. Start med en `zero-shot` tilgang, hvor du giver en instruktion (men ingen eksempler), prøv så `few-shot` som en forbedring, ved at give nogle få eksempler på det ønskede output. Brug analogier. |
| Brug hints til at sætte gang i svarene | Skub den hen imod et ønsket resultat ved at give nogle ledende ord eller sætninger, den kan bruge som udgangspunkt for svaret.                                                                                                                 |
| Gentag dig selv                 | Nogle gange skal du gentage dig overfor modellen. Giv instruktioner før og efter dit primære indhold, brug en instruktion og et hint osv. Iterer og valider for at se, hvad der fungerer.                                                           |
| Rækkefølgen betyder noget       | Den rækkefølge, du præsenterer information for modellen, kan påvirke outputtet, også i læringseksemplerne, takket være recency bias. Prøv forskellige muligheder for at se, hvad der virker bedst.                                                |
| Giv modellen en “udvej”          | Giv modellen et _fallback_-svar, den kan give, hvis den ikke kan fuldføre opgaven af en eller anden grund. Dette kan reducere risikoen for, at modeller genererer falske eller fabrikerede svar.                                                     |
|                                 |                                                                                                                                                                                                                                                    |

Som med enhver bedste praksis, husk at _din oplevelse kan variere_ baseret på model, opgave og domæne. Brug disse som et udgangspunkt, og iterer for at finde, hvad der fungerer bedst for dig. Evaluer konstant din prompt engineering-proces, efterhånden som nye modeller og værktøjer bliver tilgængelige, med fokus på proces-skalerbarhed og svar-kvalitet.

<!--
LEKTIONS SKABELON:
Denne enhed skal indeholde en kodeudfordring, hvis relevant

UDFORDRING:
Link til en Jupyter Notebook med kun kodekommentarer i instruktionerne (kodeafsnit er tomme).

LØSNING:
Link til en kopi af den Notebook med udfyldte prompts og kørsel, der viser, hvordan et eksempel kunne se ud.
-->

## Opgave

Tillykke! Du er nået til slutningen af lektionen! Det er tid til at teste nogle af de koncepter og teknikker med rigtige eksempler!

Til vores opgave bruger vi en Jupyter Notebook med øvelser, du kan gennemføre interaktivt. Du kan også udvide notebooken med dine egne Markdown- og kodeceller for at udforske ideer og teknikker på egen hånd.

### For at komme i gang, fork repoet, og så

- (Anbefalet) Start GitHub Codespaces
- (Alternativt) Klon repoet til din lokale enhed og brug det med Docker Desktop
- (Alternativt) Åbn notebooken med dit foretrukne notebook-runtime-miljø.

### Dernæst, konfigurer dine miljøvariabler

- Kopiér `.env.copy`-filen i repo-roden til `.env` og udfyld værdierne for `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT`. Kom tilbage til [Learning Sandbox-sektionen](#læringssandbox) for at lære hvordan.

### Dernæst, åbn Jupyter Notebook

- Vælg runtime-kernen. Hvis du bruger mulighederne 1 eller 2, skal du blot vælge standard Python 3.10.x-kernen, som leveres af dev-containeren.

Du er nu klar til at køre øvelserne. Bemærk, at der ikke findes _rigtige eller forkerte_ svar her - det handler bare om at prøve sig frem og opbygge intuition for, hvad der fungerer for en given model og anvendelsesdomæne.

_Af den grund er der ingen Kodeløsningssegmenter i denne lektion. I stedet vil notebooken have markdown-celler med titlen "Min løsning:", der viser et eksempel på output til reference._

 <!--
LEKTIONS SKABELON:
Afslut sektionen med et sammendrag og ressourcer for selvstyret læring.
-->

## Videnskontrol

Hvilken af følgende er en god prompt, der følger nogle fornuftige bedste praksisser?

1. Vis mig et billede af en rød bil
2. Vis mig et billede af en rød bil af mærket Volvo og model XC90 parkeret ved en klippe med solen gående ned
3. Vis mig et billede af en rød bil af mærket Volvo og model XC90

A: 2, det er den bedste prompt, da den giver detaljer om "hvad" og går i detaljer (ikke bare en bil, men et specifikt mærke og model) og den beskriver også hele omgivelserne. 3 er næstbedst, da den også indeholder meget beskrivelse.

## 🚀 Udfordring

Prøv at bruge "hint"-teknikken med prompten: Fuldfør sætningen "Vis mig et billede af en rød bil af mærket Volvo og ". Hvad svarer den, og hvordan vil du forbedre den?

## Flot arbejde! Fortsæt din læring

Vil du lære mere om forskellige koncepter indenfor Prompt Engineering? Gå til [siden for fortsat læring](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at finde andre gode ressourcer om dette emne.

Gå videre til Lektion 5, hvor vi vil se på [avancerede prompt-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->