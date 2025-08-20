<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-07-09T10:24:39+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "da"
}
-->
# Grundlæggende om Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.da.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introduktion  
Dette modul dækker væsentlige begreber og teknikker til at skabe effektive prompts i generative AI-modeller. Måden, du skriver din prompt til en LLM på, har også betydning. En omhyggeligt udformet prompt kan opnå en bedre kvalitet i svaret. Men hvad betyder begreber som _prompt_ og _prompt engineering_ egentlig? Og hvordan forbedrer jeg det prompt-_input_, jeg sender til LLM’en? Det er de spørgsmål, vi vil forsøge at besvare i dette kapitel og det næste.

_Generativ AI_ kan skabe nyt indhold (f.eks. tekst, billeder, lyd, kode osv.) som svar på brugerforespørgsler. Det opnås ved hjælp af _Large Language Models_ som OpenAI’s GPT ("Generative Pre-trained Transformer") serie, der er trænet til at bruge naturligt sprog og kode.

Brugere kan nu interagere med disse modeller via velkendte paradigmer som chat, uden at have teknisk ekspertise eller træning. Modellerne er _prompt-baserede_ – brugere sender en tekstinput (prompt) og får AI’s svar (completion) tilbage. De kan derefter "chatte med AI’en" iterativt i samtaler med flere runder, hvor de finjusterer deres prompt, indtil svaret matcher deres forventninger.

"Prompts" bliver nu den primære _programmeringsgrænseflade_ for generative AI-apps, der fortæller modellerne, hvad de skal gøre, og påvirker kvaliteten af de returnerede svar. "Prompt Engineering" er et hurtigt voksende studieområde, der fokuserer på _design og optimering_ af prompts for at levere konsistente og kvalitetsmæssige svar i stor skala.

## Læringsmål

I denne lektion lærer vi, hvad Prompt Engineering er, hvorfor det er vigtigt, og hvordan vi kan skabe mere effektive prompts til en given model og applikationsformål. Vi vil forstå kernebegreber og bedste praksis for prompt engineering – og lære om et interaktivt Jupyter Notebooks "sandbox"-miljø, hvor vi kan se disse koncepter anvendt på virkelige eksempler.

Ved slutningen af denne lektion vil vi kunne:

1. Forklare, hvad prompt engineering er, og hvorfor det er vigtigt.  
2. Beskrive komponenterne i en prompt og hvordan de bruges.  
3. Lære bedste praksis og teknikker til prompt engineering.  
4. Anvende lærte teknikker på virkelige eksempler ved brug af en OpenAI-endpoint.

## Centrale Begreber

Prompt Engineering: Praksissen med at designe og forfine input for at styre AI-modeller mod at producere ønskede output.  
Tokenization: Processen med at omdanne tekst til mindre enheder, kaldet tokens, som en model kan forstå og behandle.  
Instruction-Tuned LLMs: Store sprogmodeller (LLMs), der er finjusteret med specifikke instruktioner for at forbedre deres svarnøjagtighed og relevans.

## Læringssandbox

Prompt engineering er i øjeblikket mere en kunst end en videnskab. Den bedste måde at forbedre vores intuition for det på er at _øve sig mere_ og anvende en trial-and-error tilgang, der kombinerer domæneekspertise med anbefalede teknikker og model-specifikke optimeringer.

Jupyter Notebook, der følger med denne lektion, giver et _sandbox_-miljø, hvor du kan prøve det, du lærer – løbende eller som en del af kodeudfordringen til sidst. For at kunne udføre øvelserne skal du bruge:

1. **En Azure OpenAI API-nøgle** – service-endpoint for en implementeret LLM.  
2. **Et Python-runtime** – hvor Notebook’en kan køres.  
3. **Lokale miljøvariabler** – _fuldfør [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) trin nu for at være klar_.

Notebook’en indeholder _startøvelser_ – men du opfordres til at tilføje dine egne _Markdown_ (beskrivelser) og _Code_ (prompt-forespørgsler) sektioner for at prøve flere eksempler eller idéer – og opbygge din intuition for promptdesign.

## Illustreret Guide

Vil du have et overblik over, hvad denne lektion dækker, inden du går i gang? Tjek denne illustrerede guide, som giver dig en fornemmelse af hovedemnerne og de vigtigste pointer, du kan tænke over i hver del. Lektionens køreplan tager dig fra forståelsen af kernebegreber og udfordringer til at håndtere dem med relevante prompt engineering-teknikker og bedste praksis. Bemærk, at afsnittet "Avancerede teknikker" i denne guide henviser til indhold, der dækkes i det _næste_ kapitel i dette kursusforløb.

![Illustreret Guide til Prompt Engineering](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.da.png)

## Vores Startup

Lad os nu tale om, hvordan _dette emne_ relaterer sig til vores startup-mission om at [bringe AI-innovation til uddannelse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker at bygge AI-drevne applikationer til _personlig læring_ – så lad os tænke over, hvordan forskellige brugere af vores applikation kunne "designe" prompts:

- **Administratorer** kunne bede AI’en om at _analysere læseplansdata for at identificere huller i dækningen_. AI’en kan opsummere resultater eller visualisere dem med kode.  
- **Undervisere** kunne bede AI’en om at _generere en lektionsplan for en målgruppe og et emne_. AI’en kan bygge den personlige plan i et specificeret format.  
- **Studerende** kunne bede AI’en om at _vejlede dem i et svært fag_. AI’en kan nu guide elever med lektioner, hints og eksempler tilpasset deres niveau.

Det er kun toppen af isbjerget. Tjek [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – et open source prompt-bibliotek kurateret af uddannelseseksperter – for at få en bredere fornemmelse af mulighederne! _Prøv at køre nogle af disse prompts i sandboxen eller brug OpenAI Playground for at se, hvad der sker!_

<!--  
LESSON TEMPLATE:  
This unit should cover core concept #1.  
Reinforce the concept with examples and references.  

CONCEPT #1:  
Prompt Engineering.  
Define it and explain why it is needed.  
-->

## Hvad er Prompt Engineering?

Vi startede denne lektion med at definere **Prompt Engineering** som processen med at _designe og optimere_ tekstinput (prompts) for at levere konsistente og kvalitetsmæssige svar (completions) til et givent applikationsformål og model. Vi kan tænke på det som en 2-trins proces:

- _designe_ den oprindelige prompt til en given model og formål  
- _forfine_ prompten iterativt for at forbedre kvaliteten af svaret

Dette er nødvendigvis en trial-and-error proces, der kræver brugerintuiton og indsats for at opnå optimale resultater. Så hvorfor er det vigtigt? For at besvare det spørgsmål skal vi først forstå tre begreber:

- _Tokenization_ = hvordan modellen "ser" prompten  
- _Base LLMs_ = hvordan grundmodellen "behandler" en prompt  
- _Instruction-Tuned LLMs_ = hvordan modellen nu kan se "opgaver"

### Tokenization

En LLM ser prompts som en _sekvens af tokens_, hvor forskellige modeller (eller versioner af en model) kan tokenisere den samme prompt på forskellige måder. Da LLM’er er trænet på tokens (og ikke rå tekst), har måden, prompts tokeniseres på, direkte indflydelse på kvaliteten af det genererede svar.

For at få en fornemmelse af, hvordan tokenization fungerer, kan du prøve værktøjer som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Kopiér din prompt ind – og se, hvordan den bliver omdannet til tokens, med særlig opmærksomhed på, hvordan mellemrum og tegnsætning håndteres. Bemærk, at dette eksempel viser en ældre LLM (GPT-3) – så prøv med en nyere model for at se, om resultatet bliver anderledes.

![Tokenization](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.da.png)

### Begreb: Foundation Models

Når en prompt er tokeniseret, er hovedfunktionen for ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grundmodellen) at forudsige det næste token i sekvensen. Da LLM’er er trænet på enorme tekstdatasæt, har de en god fornemmelse af de statistiske sammenhænge mellem tokens og kan lave denne forudsigelse med en vis sikkerhed. Bemærk, at de ikke forstår _meningen_ med ordene i prompten eller tokenet; de ser blot et mønster, de kan "fuldføre" med deres næste forudsigelse. De kan fortsætte med at forudsige sekvensen, indtil brugeren afbryder eller en forudbestemt betingelse opfyldes.

Vil du se, hvordan prompt-baseret completion fungerer? Indtast ovenstående prompt i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardindstillingerne. Systemet er konfigureret til at behandle prompts som informationsforespørgsler – så du bør se et svar, der opfylder denne kontekst.

Men hvad hvis brugeren ønskede at se noget specifikt, der opfylder visse kriterier eller et opgaveformål? Her kommer _instruction-tuned_ LLM’er ind i billedet.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.da.png)

### Begreb: Instruction Tuned LLMs

En [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grundmodellen og finjusterer den med eksempler eller input/output-par (f.eks. multi-turn "beskeder"), der kan indeholde klare instruktioner – og AI’ens svar forsøger at følge disse instruktioner.

Dette bruger teknikker som Reinforcement Learning with Human Feedback (RLHF), der kan træne modellen til at _følge instruktioner_ og _lære af feedback_, så den producerer svar, der er bedre tilpasset praktiske anvendelser og mere relevante for brugerens mål.

Lad os prøve det – gå tilbage til prompten ovenfor, men skift nu _systembeskeden_ til at give følgende instruktion som kontekst:

> _Opsummer det indhold, du får, for en elev i 2. klasse. Hold resultatet til et afsnit med 3-5 punktopstillinger._

Kan du se, hvordan resultatet nu er tilpasset det ønskede mål og format? En underviser kan nu direkte bruge dette svar i deres slides til den klasse.

![Instruction Tuned LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.da.png)

## Hvorfor har vi brug for Prompt Engineering?

Nu hvor vi ved, hvordan prompts behandles af LLM’er, lad os tale om _hvorfor_ vi har brug for prompt engineering. Svaret ligger i, at nuværende LLM’er har en række udfordringer, der gør det sværere at opnå _pålidelige og konsistente svar_ uden at lægge indsats i promptkonstruktion og optimering. For eksempel:

1. **Model-svar er stokastiske.** Den _samme prompt_ vil sandsynligvis give forskellige svar med forskellige modeller eller modelversioner. Og den kan endda give forskellige resultater med den _samme model_ på forskellige tidspunkter. _Prompt engineering-teknikker kan hjælpe os med at minimere disse variationer ved at give bedre rammer_.

1. **Modeller kan finde på svar.** Modeller er fortrænet med _store, men begrænsede_ datasæt, hvilket betyder, at de mangler viden om begreber uden for træningsområdet. Som følge heraf kan de producere svar, der er unøjagtige, opdigtede eller direkte modstridende med kendte fakta. _Prompt engineering-teknikker hjælper brugere med at identificere og afbøde sådanne opdigtninger, f.eks. ved at bede AI om kildehenvisninger eller begrundelser_.

1. **Modellers kapaciteter vil variere.** Nyere modeller eller modelgenerationer vil have rigere kapaciteter, men også bringe unikke særheder og kompromiser i omkostninger og kompleksitet. _Prompt engineering kan hjælpe os med at udvikle bedste praksis og arbejdsgange, der abstraherer forskelle og tilpasser sig model-specifikke krav på skalerbare og sømløse måder_.

Lad os se dette i praksis i OpenAI eller Azure OpenAI Playground:

- Brug den samme prompt med forskellige LLM-implementeringer (f.eks. OpenAI, Azure OpenAI, Hugging Face) – så du variationerne?  
- Brug den samme prompt gentagne gange med den _samme_ LLM-implementering (f.eks. Azure OpenAI playground) – hvordan adskilte disse variationer sig?

### Eksempel på opdigtninger

I dette kursus bruger vi begrebet **"fabrication"** til at referere til fænomenet, hvor LLM’er nogle gange genererer faktuelt ukorrekte oplysninger på grund af begrænsninger i deres træning eller andre forhold. Du har måske også hørt dette omtalt som _"hallucinationer"_ i populære artikler eller forskningspapirer. Vi anbefaler dog kraftigt at bruge _"fabrication"_ som betegnelse, så vi undgår at antropomorfisere adfærden ved at tillægge en menneskelig egenskab til et maskindrevet resultat. Dette understøtter også [Responsible AI-retningslinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologisk perspektiv ved at fjerne termer, der i visse sammenhænge kan opfattes som stødende eller ikke inkluderende.

Vil du have en fornemmelse af, hvordan fabrication fungerer? Tænk på en prompt, der instruerer AI’en til at generere indhold om et ikke-eksisterende emne (for at sikre, at det ikke findes i træningsdatasættet). For eksempel – jeg prøvede denne prompt:
# Lektionplan: Den Marsianske Krig i 2076

## Introduktion
I denne lektion vil vi udforske den Marsianske Krig, der fandt sted i 2076. Vi vil undersøge årsagerne til konflikten, de vigtigste begivenheder og dens konsekvenser for både Jorden og Mars.

## Mål
- Forstå baggrunden for den Marsianske Krig
- Identificere nøgleaktører og begivenheder i krigen
- Analysere krigens indvirkning på fremtidige interplanetariske relationer

## Materialer
- Historiske dokumenter og rapporter om Marsianske Krig
- Kort over Mars og Jorden under konflikten
- Videoer og øjenvidneberetninger

## Lektionens forløb

### 1. Baggrund og årsager (20 minutter)
- Diskuter de politiske og økonomiske spændinger mellem Jorden og Mars
- Gennemgå de vigtigste begivenheder, der førte til krigen

### 2. Krigens forløb (30 minutter)
- Gennemgå de vigtigste slag og strategier brugt af begge sider
- Analyser teknologier og våben, der blev anvendt

### 3. Konsekvenser og efterspil (20 minutter)
- Diskuter krigens indvirkning på Mars' kolonisering og Jordens politik
- Overvej hvordan krigen har formet nutidens interplanetariske samarbejde

### 4. Diskussion og refleksion (15 minutter)
- Lad eleverne diskutere, hvad de mener kunne have forhindret krigen
- Reflekter over betydningen af fred og samarbejde i rummet

## Afslutning
Opsummer de vigtigste punkter fra lektionen og opfordr eleverne til at læse yderligere materiale om emnet.

## Ekstra ressourcer
- Links til dokumentarer og artikler om den Marsianske Krig
- Forslag til projekter og opgaver relateret til emnet
Et web-søg viste mig, at der fandtes fiktive beretninger (f.eks. tv-serier eller bøger) om marskrige – men ingen i 2076. Sund fornuft fortæller os også, at 2076 er _i fremtiden_ og derfor ikke kan forbindes med en virkelig begivenhed.

Så hvad sker der, når vi kører denne prompt med forskellige LLM-udbydere?

> **Response 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.da.png)

> **Response 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.da.png)

> **Response 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.da.png)

Som forventet producerer hver model (eller modelversion) lidt forskellige svar takket være stokastisk adfærd og variationer i modelkapacitet. For eksempel retter én model sig mod et 8. klasses publikum, mens en anden antager en gymnasieelev. Men alle tre modeller genererede svar, der kunne overbevise en uinformeret bruger om, at begivenheden var ægte.

Prompt engineering-teknikker som _metaprompting_ og _temperature configuration_ kan til en vis grad reducere model-fabrikationer. Nye prompt engineering-_arkitekturer_ integrerer også nye værktøjer og teknikker problemfrit i prompt-flowet for at afbøde eller mindske nogle af disse effekter.

## Case Study: GitHub Copilot

Lad os afslutte dette afsnit med at få en fornemmelse af, hvordan prompt engineering bruges i virkelige løsninger ved at se på et Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI Pair Programmer" – den omsætter tekstprompter til kodeforslag og er integreret i dit udviklingsmiljø (f.eks. Visual Studio Code) for en problemfri brugeroplevelse. Som dokumenteret i blogserien nedenfor, var den tidligste version baseret på OpenAI Codex-modellen – hvor ingeniører hurtigt indså behovet for at finjustere modellen og udvikle bedre prompt engineering-teknikker for at forbedre kodekvaliteten. I juli [præsenterede de en forbedret AI-model, der går ud over Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for endnu hurtigere forslag.

Læs indlæggene i rækkefølge for at følge deres læringsrejse.

- **Maj 2023** | [GitHub Copilot bliver bedre til at forstå din kode](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Indenfor GitHub: Arbejde med LLM’erne bag GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jun 2023** | [Sådan skriver du bedre prompts til GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [.. GitHub Copilot går ud over Codex med forbedret AI-model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En udviklers guide til prompt engineering og LLM’er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Sådan bygger du en enterprise LLM-app: Læringer fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også bladre i deres [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere indlæg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), der viser, hvordan disse modeller og teknikker _anvendes_ til at drive virkelige applikationer.

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

Vi har set, hvorfor prompt engineering er vigtigt – nu skal vi forstå, hvordan prompts _konstrueres_, så vi kan evaluere forskellige teknikker for mere effektiv promptdesign.

### Grundlæggende Prompt

Lad os starte med den grundlæggende prompt: en tekstinput sendt til modellen uden anden kontekst. Her er et eksempel – når vi sender de første par ord af den amerikanske nationalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), fuldfører den straks svaret med de næste linjer, hvilket illustrerer den grundlæggende forudsigelsesadfærd.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det lyder som om, du starter teksten til "The Star-Spangled Banner," USA’s nationalsang. Hele teksten er ... |

### Kompleks Prompt

Lad os nu tilføje kontekst og instruktioner til den grundlæggende prompt. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) giver os mulighed for at konstruere en kompleks prompt som en samling af _beskeder_ med:

- Input/output-par, der afspejler _bruger_-input og _assistent_-svar.
- Systembesked, der sætter konteksten for assistentens adfærd eller personlighed.

Anmodningen er nu i nedenstående form, hvor _tokeniseringen_ effektivt fanger relevant information fra kontekst og samtale. At ændre systemkonteksten kan nu have lige så stor indflydelse på kvaliteten af fuldførelser som de givne brugerinput.

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

I ovenstående eksempler var brugerprompten en simpel tekstforespørgsel, der kan tolkes som en anmodning om information. Med _instruktionsprompter_ kan vi bruge den tekst til at specificere en opgave mere detaljeret og give AI’en bedre vejledning. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruktionstype    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returnerede et simpelt afsnit_                                                                                            | Simpel              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returnerede et afsnit efterfulgt af en liste med nøglebegivenheder og beskrivelser_                                       | Kompleks            |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returnerer mere omfattende detaljer i en tekstboks, formateret som JSON, som du kan kopiere og indsætte i en fil og validere efter behov_ | Kompleks. Formateret.|

## Primært Indhold

I ovenstående eksempler var prompten stadig ret åben, hvilket tillod LLM’en at afgøre, hvilken del af dens fortrænede datasæt der var relevant. Med designmønsteret _primært indhold_ opdeles inputteksten i to dele:

- en instruktion (handling)
- relevant indhold (der påvirker handlingen)

Her er et eksempel, hvor instruktionen er at "opsummere dette i 2 sætninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planet fra Solen og den største i solsystemet. Det er en gasgigant med en masse, der er en tusindedel af Solens, men to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter, der kan ses med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før den skrevne historie. Den er opkaldt efter den romerske gud Jupiter.[19] Når man ser på Jupiter fra Jorden, kan den være så lysstærk, at dens reflekterede lys kaster synlige skygger,[20] og den er i gennemsnit det tredje mest lysstærke naturlige objekt på nattehimlen efter Månen og Venus. <br/> **Opsummer dette i 2 korte sætninger** | Jupiter, den femte planet fra Solen, er den største i solsystemet og kendt for at være et af de mest lysstærke objekter på nattehimlen. Opkaldt efter den romerske gud Jupiter, er det en gasgigant med en masse, der er to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. |

Segmentet med primært indhold kan bruges på forskellige måder til at skabe mere effektive instruktioner:

- **Eksempler** – i stedet for at fortælle modellen, hvad den skal gøre med en eksplicit instruktion, giver man den eksempler på, hvad den skal gøre, og lader den udlede mønsteret.
- **Signaler** – følg instruktionen med et "signal", der forbereder fuldførelsen og guider modellen mod mere relevante svar.
- **Skabeloner** – disse er gentagelige ’opskrifter’ til prompts med pladsholdere (variabler), der kan tilpasses med data til specifikke brugsscenarier.

Lad os udforske disse i praksis.

### Brug af Eksempler

Dette er en tilgang, hvor du bruger det primære indhold til at "fodre modellen" med nogle eksempler på det ønskede output for en given instruktion og lader den udlede mønsteret for det ønskede output. Afhængigt af antallet af eksempler kan vi have zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nu af tre komponenter:

- En opgavebeskrivelse
- Nogle få eksempler på det ønskede output
- Starten på et nyt eksempel (som bliver en implicit opgavebeskrivelse)

| Læringstype | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot    | "The Sun is Shining". Translate to Spanish                                                                                                          | "El Sol está brillando".    |
| One-shot     | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                               | "Es un día frío y ventoso". |
| Few-shot     | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk =>   | Basketball                  |
|              |                                                                                                                                                      |                             |

Bemærk, hvordan vi måtte give en eksplicit instruktion ("Translate to Spanish") i zero-shot prompting, men den udledes i one-shot prompting-eksemplet. Few-shot-eksemplet viser, hvordan flere eksempler gør det muligt for modeller at lave mere præcise slutninger uden yderligere instruktioner.

### Prompt Signaler

En anden teknik til at bruge primært indhold er at give _signaler_ i stedet for eksempler. I dette tilfælde giver vi modellen et skub i den rigtige retning ved at _starte den_ med et uddrag, der afspejler det ønskede svarformat. Modellen "tager signalet" og fortsætter i samme stil.

| Antal Signaler | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter er den femte planet fra Solen og den største i solsystemet. Det er en gasgigant med en masse, der er en tusindedel af Solens, men to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter, der kan ses med det blotte øje på nattehimlen, og har været kendt af gamle civilisationer siden før den skrevne historie.

**Summarize This**                                       | Jupiter er den største planet i vores solsystem og den femte fra solen. Det er en gasgigant med en masse, der er 1/1000 af solens, men den er tungere end alle de andre planeter tilsammen. Oldtidens civilisationer har kendt til Jupiter i lang tid, og den er let synlig på nattehimlen. |
| 1              | Jupiter er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse, der er en tusindedel af solens, men to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter, der kan ses med det blotte øje på nattehimlen, og den har været kendt af oldtidens civilisationer siden før historisk tid. <br/>**Summarize This** <br/> Det vi lærte er, at Jupiter | er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse, der er en tusindedel af solens, men to og en halv gang så stor som alle de andre planeter tilsammen. Den er let synlig med det blotte øje og har været kendt siden oldtiden.                        |
| 2              | Jupiter er den femte planet fra solen og den største i solsystemet. Det er en gasgigant med en masse, der er en tusindedel af solens, men to og en halv gang så stor som alle de andre planeter i solsystemet tilsammen. Jupiter er et af de klareste objekter, der kan ses med det blotte øje på nattehimlen, og den har været kendt af oldtidens civilisationer siden før historisk tid. <br/>**Summarize This** <br/> Top 3 fakta vi lærte:         | 1. Jupiter er den femte planet fra solen og den største i solsystemet. <br/> 2. Det er en gasgigant med en masse, der er en tusindedel af solens...<br/> 3. Jupiter har været synlig for det blotte øje siden oldtiden ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

En prompt-skabelon er en _foruddefineret opskrift på en prompt_, som kan gemmes og genbruges efter behov for at skabe mere konsistente brugeroplevelser i stor skala. I sin enkleste form er det blot en samling af prompt-eksempler som [dette fra OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), der både indeholder de interaktive prompt-komponenter (bruger- og systembeskeder) og API-drevne anmodningsformater – for at understøtte genbrug.

I en mere kompleks form som [dette eksempel fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) indeholder den _pladsholdere_, som kan erstattes med data fra forskellige kilder (brugerinput, systemkontekst, eksterne datakilder osv.) for at generere en prompt dynamisk. Det giver os mulighed for at opbygge et bibliotek af genanvendelige prompts, der kan bruges til at skabe konsistente brugeroplevelser **programmatisk** i stor skala.

Endelig ligger den egentlige værdi i skabeloner i muligheden for at oprette og offentliggøre _prompt-biblioteker_ til vertikale anvendelsesområder – hvor prompt-skabelonen nu er _optimeret_ til at afspejle applikationsspecifik kontekst eller eksempler, der gør svarene mere relevante og præcise for den målrettede brugergruppe. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) er et godt eksempel på denne tilgang, hvor man samler et bibliotek af prompts til uddannelsesområdet med fokus på nøglemål som lektionsplanlægning, læseplanlægning, elevvejledning osv.

## Supporting Content

Hvis vi ser på prompt-konstruktion som bestående af en instruktion (opgave) og et mål (primært indhold), så er _sekundært indhold_ som ekstra kontekst, vi giver for at **påvirke output på en eller anden måde**. Det kan være justeringsparametre, formateringsinstruktioner, emnetaksonomier osv., som hjælper modellen med at _tilpasse_ sit svar, så det passer til de ønskede brugerformål eller forventninger.

For eksempel: Givet en kursuskatalog med omfattende metadata (navn, beskrivelse, niveau, metadata-tags, underviser osv.) for alle tilgængelige kurser i læseplanen:

- kan vi definere en instruktion om at "opsummere kursuskataloget for efteråret 2023"
- kan vi bruge det primære indhold til at give nogle eksempler på det ønskede output
- kan vi bruge det sekundære indhold til at identificere de 5 vigtigste "tags" af interesse.

Nu kan modellen levere et resumé i det format, som eksemplerne viser – men hvis et resultat har flere tags, kan den prioritere de 5 tags, der er identificeret i det sekundære indhold.

---

<!--
LESSON TEMPLATE:
Denne enhed skal dække kernebegreb #1.
Understøt begrebet med eksempler og referencer.

BEGREB #3:
Prompt Engineering teknikker.
Hvad er nogle grundlæggende teknikker til prompt engineering?
Illustrer det med nogle øvelser.
-->

## Prompting Best Practices

Nu hvor vi ved, hvordan prompts kan _konstrueres_, kan vi begynde at tænke over, hvordan vi _designer_ dem, så de afspejler bedste praksis. Vi kan opdele det i to dele – at have den rette _tankegang_ og anvende de rette _teknikker_.

### Prompt Engineering Mindset

Prompt Engineering er en prøve-og-fejl proces, så husk tre brede vejledende faktorer:

1. **Domæneforståelse er vigtig.** Svarenes nøjagtighed og relevans afhænger af det _domæne_, som applikationen eller brugeren opererer i. Brug din intuition og domæneekspertise til at **tilpasse teknikkerne** yderligere. For eksempel kan du definere _domænespecifikke personligheder_ i dine systemprompter eller bruge _domænespecifikke skabeloner_ i dine brugerprompter. Giv sekundært indhold, der afspejler domænespecifik kontekst, eller brug _domænespecifikke signaler og eksempler_ for at guide modellen mod velkendte brugsmønstre.

2. **Modelforståelse er vigtig.** Vi ved, at modeller er stokastiske af natur. Men modelimplementeringer kan også variere med hensyn til træningsdatasættet (forudindlært viden), de funktioner, de tilbyder (f.eks. via API eller SDK) og typen af indhold, de er optimeret til (f.eks. kode vs. billeder vs. tekst). Forstå styrker og begrænsninger ved den model, du bruger, og brug den viden til at _prioritere opgaver_ eller bygge _tilpassede skabeloner_, der er optimeret til modellens kapaciteter.

3. **Iteration & validering er vigtig.** Modeller udvikler sig hurtigt, og det samme gør teknikkerne til prompt engineering. Som domæneekspert kan du have anden kontekst eller kriterier for _din_ specifikke applikation, som måske ikke gælder for det bredere fællesskab. Brug prompt engineering-værktøjer og teknikker til at "komme godt i gang" med prompt-konstruktionen, og iterer og valider resultaterne med din egen intuition og domæneekspertise. Registrer dine indsigter og opbyg en **vidensbase** (f.eks. prompt-biblioteker), som andre kan bruge som ny baseline for hurtigere iterationer fremover.

## Best Practices

Lad os nu se på almindelige bedste praksisser, som anbefales af [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikere.

| Hvad                              | Hvorfor                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluer de nyeste modeller.       | Nye modelgenerationer har sandsynligvis forbedrede funktioner og kvalitet – men kan også medføre højere omkostninger. Evaluer dem for effekt, og træf derefter beslutning om migrering.                                                                |
| Adskil instruktioner & kontekst   | Tjek om din model/udbyder definerer _afgrænsere_ for tydeligere at adskille instruktioner, primært og sekundært indhold. Det kan hjælpe modeller med at tildele vægte mere præcist til tokens.                                                         |
| Vær specifik og klar              | Giv flere detaljer om ønsket kontekst, resultat, længde, format, stil osv. Det forbedrer både kvalitet og konsistens i svarene. Gem opskrifter i genanvendelige skabeloner.                                                                            |
| Vær beskrivende, brug eksempler   | Modeller reagerer ofte bedre på en "vis og fortæl"-tilgang. Start med en `zero-shot` tilgang, hvor du giver en instruktion (men ingen eksempler), og prøv derefter `few-shot` som en finjustering, hvor du giver nogle få eksempler på ønsket output. Brug analogier. |
| Brug signaler til at kickstarte svar | Skub modellen mod et ønsket resultat ved at give nogle ledende ord eller sætninger, som den kan bruge som udgangspunkt for svaret.                                                                                                               |
| Gentag for at forstærke           | Nogle gange skal du gentage dig selv over for modellen. Giv instruktioner før og efter dit primære indhold, brug en instruktion og et signal osv. Iterer og valider for at se, hvad der virker.                                                         |
| Rækkefølge betyder noget          | Den rækkefølge, du præsenterer information for modellen i, kan påvirke output, også i læringseksempler, på grund af recency bias. Prøv forskellige muligheder for at finde det, der virker bedst.                                                       |
| Giv modellen en “udvej”            | Giv modellen et _fallback_-svar, den kan bruge, hvis den ikke kan fuldføre opgaven af en eller anden grund. Det kan mindske risikoen for, at modellen genererer falske eller opdigtede svar.                                                             |
|                                   |                                                                                                                                                                                                                                                   |

Som med enhver bedste praksis, husk at _din oplevelse kan variere_ afhængigt af model, opgave og domæne. Brug disse som udgangspunkt, og iterer for at finde det, der virker bedst for dig. Evaluer løbende din prompt engineering-proces, efterhånden som nye modeller og værktøjer bliver tilgængelige, med fokus på skalerbarhed og svar-kvalitet.

<!--
LESSON TEMPLATE:
Denne enhed skal indeholde en kodeudfordring, hvis relevant

UDFORDRING:
Link til en Jupyter Notebook med kun kodekommentarer i instruktionerne (kodeafsnit er tomme).

LØSNING:
Link til en kopi af den Notebook med udfyldte prompts og kørsel, der viser et eksempel.
-->

## Assignment

Tillykke! Du er nået til slutningen af lektionen! Det er tid til at prøve nogle af de koncepter og teknikker af med rigtige eksempler!

Til vores opgave bruger vi en Jupyter Notebook med øvelser, du kan gennemføre interaktivt. Du kan også udvide Notebooken med dine egne Markdown- og kodeceller for at udforske ideer og teknikker på egen hånd.

### For at komme i gang, fork repoet, og

- (Anbefalet) Start GitHub Codespaces
- (Alternativt) Klon repoet til din lokale enhed og brug det med Docker Desktop
- (Alternativt) Åbn Notebooken i dit foretrukne Notebook-runtime-miljø.

### Dernæst, konfigurer dine miljøvariabler

- Kopiér `.env.copy`-filen i repoets rod til `.env` og udfyld værdierne for `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT`. Gå tilbage til [Learning Sandbox sektionen](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) for at lære hvordan.

### Dernæst, åbn Jupyter Notebooken

- Vælg runtime-kernen. Hvis du bruger mulighed 1 eller 2, vælg blot den standard Python 3.10.x kerne, som dev-containeren leverer.

Du er klar til at køre øvelserne. Bemærk, at der ikke findes _rigtige eller forkerte_ svar her – det handler om at prøve sig frem og opbygge intuition for, hvad der virker for en given model og applikationsdomæne.

_Af denne grund er der ingen kode-løsningsafsnit i denne lektion. I stedet vil Notebooken indeholde Markdown-celler med titlen "My Solution:", som viser et eksempel på output til reference._

 <!--
LESSON TEMPLATE:
Afslut afsnittet med en opsummering og ressourcer til selvstyret læring.
-->

## Knowledge check

Hvilken af følgende er en god prompt, der følger nogle rimelige bedste praksisser?

1. Vis mig et billede af en rød bil  
2. Vis mig et billede af en rød bil af mærket Volvo og model XC90 parkeret ved en klippe med solen gående ned  
3. Vis mig et billede af en rød bil af mærket Volvo og model XC90

A: 2, det er den bedste prompt, da den giver detaljer om "hvad" og går i dybden med specifikationer (ikke bare en hvilken som helst bil, men et bestemt mærke og model) og beskriver også omgivelserne. 3 er næstbedst, da den også indeholder mange beskrivelser.

## 🚀 Challenge

Prøv at bruge "cue"-teknikken med prompten: Fuldfør sætningen "Vis mig et billede af en rød bil af mærket Volvo og ". Hvad svarer den, og hvordan ville du forbedre det?

## Godt arbejde! Fortsæt din læring

Vil du lære mere om forskellige Prompt Engineering-koncept? Gå til [den fortsatte læringsside](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at finde andre gode ressourcer om emnet.

Gå videre til Lektion 5, hvor vi ser på [avancerede prompting-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.