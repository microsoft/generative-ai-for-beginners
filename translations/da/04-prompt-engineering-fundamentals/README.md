<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:51:04+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "da"
}
-->
# Grundlæggende om Prompt Engineering

## Introduktion
Dette modul dækker væsentlige begreber og teknikker til at skabe effektive prompts i generative AI-modeller. Den måde, du skriver din prompt til en LLM, har også betydning. En omhyggeligt udformet prompt kan opnå en bedre kvalitet af svar. Men hvad betyder udtryk som _prompt_ og _prompt engineering_ egentlig? Og hvordan forbedrer jeg prompt _input_, som jeg sender til LLM'en? Det er de spørgsmål, vi vil forsøge at besvare i dette kapitel og det næste.

_Generativ AI_ er i stand til at skabe nyt indhold (f.eks. tekst, billeder, lyd, kode osv.) som svar på brugerforespørgsler. Den opnår dette ved hjælp af _Large Language Models_ som OpenAI's GPT ("Generative Pre-trained Transformer") serier, der er trænet til at bruge naturligt sprog og kode.

Brugere kan nu interagere med disse modeller ved hjælp af velkendte paradigmer som chat, uden at skulle have teknisk ekspertise eller træning. Modellerne er _prompt-baserede_ - brugerne sender en tekstinput (prompt) og får AI-svaret (completion) tilbage. De kan derefter "chatte med AI'en" iterativt i samtaler med flere omgange, og finjustere deres prompt, indtil svaret matcher deres forventninger.

"Prompts" bliver nu det primære _programmeringsinterface_ for generative AI-apps, der fortæller modellerne, hvad de skal gøre, og påvirker kvaliteten af de returnerede svar. "Prompt Engineering" er et hurtigt voksende studieområde, der fokuserer på _design og optimering_ af prompts for at levere konsistente og kvalitetsmæssige svar i stor skala.

## Læringsmål

I denne lektion lærer vi, hvad Prompt Engineering er, hvorfor det er vigtigt, og hvordan vi kan udforme mere effektive prompts til en given model og applikationsmål. Vi vil forstå kernebegreber og bedste praksis for prompt engineering - og lære om et interaktivt Jupyter Notebooks "sandbox"-miljø, hvor vi kan se disse begreber anvendt på virkelige eksempler.

Ved slutningen af denne lektion vil vi være i stand til at:

1. Forklare, hvad prompt engineering er, og hvorfor det er vigtigt.
2. Beskrive komponenterne i en prompt og hvordan de bruges.
3. Lære bedste praksis og teknikker til prompt engineering.
4. Anvende lærte teknikker på virkelige eksempler ved hjælp af en OpenAI-endpoint.

## Nøglebegreber

Prompt Engineering: Praksis med at designe og forfine input for at guide AI-modeller mod at producere ønskede output.
Tokenisering: Processen med at konvertere tekst til mindre enheder, kaldet tokens, som en model kan forstå og behandle.
Instruktions-justerede LLM'er: Store sprogmodeller (LLM'er), der er blevet finjusteret med specifikke instruktioner for at forbedre deres svarnøjagtighed og relevans.

## Læringsmiljø

Prompt engineering er i øjeblikket mere kunst end videnskab. Den bedste måde at forbedre vores intuition for det er at _øve mere_ og vedtage en trial-and-error tilgang, der kombinerer applikationsdomæneekspertise med anbefalede teknikker og model-specifikke optimeringer.

Den Jupyter Notebook, der ledsager denne lektion, giver et _sandbox_-miljø, hvor du kan prøve, hvad du lærer - som du går eller som en del af kodeudfordringen i slutningen. For at udføre øvelserne skal du bruge:

1. **En Azure OpenAI API-nøgle** - serviceendpointet for en implementeret LLM.
2. **Et Python Runtime** - hvor Notebooken kan udføres.
3. **Lokale miljøvariabler** - _fuldfør [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) trin nu for at blive klar_.

Notebooken kommer med _start_-øvelser - men du opfordres til at tilføje dine egne _Markdown_ (beskrivelse) og _Kode_ (prompt forespørgsler) sektioner for at prøve flere eksempler eller ideer - og opbygge din intuition for prompt design.

## Illustreret guide

Vil du få det store billede af, hvad denne lektion dækker, før du dykker ned? Tjek denne illustrerede guide, der giver dig en fornemmelse af de vigtigste emner, der dækkes, og de vigtigste punkter, du skal tænke over i hver enkelt. Lektionens køreplan tager dig fra at forstå kernebegreberne og udfordringerne til at adressere dem med relevante prompt engineering teknikker og bedste praksis. Bemærk, at afsnittet "Avancerede teknikker" i denne guide refererer til indhold, der dækkes i det _næste_ kapitel af denne læseplan.

## Vores Startup

Lad os nu tale om, hvordan _dette emne_ relaterer til vores startup-mission om at [bringe AI-innovation til uddannelse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker at bygge AI-drevne applikationer til _personlig læring_ - så lad os tænke over, hvordan forskellige brugere af vores applikation kan "designe" prompts:

- **Administratorer** kan bede AI'en om at _analysere læseplansdata for at identificere huller i dækningen_. AI'en kan opsummere resultaterne eller visualisere dem med kode.
- **Lærere** kan bede AI'en om at _generere en lektionsplan for en målgruppe og et emne_. AI'en kan bygge den personlige plan i et specificeret format.
- **Studerende** kan bede AI'en om at _tutore dem i et vanskeligt emne_. AI'en kan nu guide studerende med lektioner, hints og eksempler tilpasset deres niveau.

Det er kun toppen af isbjerget. Tjek [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - et open-source prompts bibliotek kurateret af uddannelseseksperter - for at få en bredere fornemmelse af mulighederne! _Prøv at køre nogle af de prompts i sandkassen eller ved hjælp af OpenAI Playground for at se, hvad der sker!_

## Hvad er Prompt Engineering?

Vi startede denne lektion med at definere **Prompt Engineering** som processen med _at designe og optimere_ tekstinput (prompts) for at levere konsistente og kvalitetsmæssige svar (completions) for en given applikationsmål og model. Vi kan tænke på dette som en 2-trins proces:

- _designe_ den indledende prompt til en given model og mål
- _forfine_ prompten iterativt for at forbedre kvaliteten af svaret

Dette er nødvendigvis en trial-and-error proces, der kræver brugerens intuition og indsats for at opnå optimale resultater. Så hvorfor er det vigtigt? For at besvare det spørgsmål skal vi først forstå tre begreber:

- _Tokenisering_ = hvordan modellen "ser" prompten
- _Base LLM'er_ = hvordan grundmodellen "behandler" en prompt
- _Instruktions-justerede LLM'er_ = hvordan modellen nu kan se "opgaver"

### Tokenisering

En LLM ser prompts som en _sekvens af tokens_, hvor forskellige modeller (eller versioner af en model) kan tokenisere den samme prompt på forskellige måder. Da LLM'er er trænet på tokens (og ikke på rå tekst), har den måde, som prompts bliver tokeniseret på, en direkte indvirkning på kvaliteten af det genererede svar.

For at få en intuition om, hvordan tokenisering fungerer, prøv værktøjer som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Kopier din prompt ind - og se, hvordan det bliver konverteret til tokens, og læg mærke til, hvordan mellemrumstegn og tegnsætning håndteres. Bemærk, at dette eksempel viser en ældre LLM (GPT-3) - så at prøve dette med en nyere model kan give et andet resultat.

### Begreb: Grundmodeller

Når en prompt er tokeniseret, er den primære funktion af ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller Grundmodel) at forudsige tokenet i den sekvens. Da LLM'er er trænet på massive tekstdatasæt, har de en god fornemmelse af de statistiske relationer mellem tokens og kan lave den forudsigelse med en vis sikkerhed. Bemærk, at de ikke forstår _betydningen_ af ordene i prompten eller tokenet; de ser bare et mønster, de kan "fuldføre" med deres næste forudsigelse. De kan fortsætte med at forudsige sekvensen, indtil den afsluttes af brugerintervention eller en forudbestemt betingelse.

Vil du se, hvordan prompt-baseret fuldførelse fungerer? Indtast ovenstående prompt i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardindstillingerne. Systemet er konfigureret til at behandle prompts som anmodninger om information - så du bør se en fuldførelse, der opfylder denne kontekst.

Men hvad hvis brugeren ønskede at se noget specifikt, der opfyldte nogle kriterier eller opgavemål? Det er her, _instruktions-justerede_ LLM'er kommer ind i billedet.

### Begreb: Instruktions-justerede LLM'er

En [Instruktions-justeret LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grundmodellen og finjusterer den med eksempler eller input/output-par (f.eks. multi-turn "beskeder"), der kan indeholde klare instruktioner - og svaret fra AI'en forsøger at følge den instruktion.

Dette bruger teknikker som Reinforcement Learning with Human Feedback (RLHF), der kan træne modellen til _at følge instruktioner_ og _lære af feedback_, så den producerer svar, der er bedre egnet til praktiske applikationer og mere relevante for brugerens mål.

Lad os prøve det - genbesøg prompten ovenfor, men ændr nu _systembeskeden_ for at give følgende instruktion som kontekst:

> _Opsummer det indhold, du får, for en andenklasses elev. Hold resultatet til et afsnit med 3-5 punkttegn._

Se, hvordan resultatet nu er justeret for at afspejle det ønskede mål og format? En underviser kan nu direkte bruge dette svar i deres slides til den klasse.

## Hvorfor har vi brug for Prompt Engineering?

Nu hvor vi ved, hvordan prompts behandles af LLM'er, lad os tale om _hvorfor_ vi har brug for prompt engineering. Svaret ligger i det faktum, at nuværende LLM'er udgør en række udfordringer, der gør _pålidelige og konsistente fuldførelser_ mere udfordrende at opnå uden at lægge indsats i promptkonstruktion og optimering. For eksempel:

1. **Modelresponser er stokastiske.** Den _samme prompt_ vil sandsynligvis producere forskellige svar med forskellige modeller eller modelversioner. Og det kan endda producere forskellige resultater med den _samme model_ på forskellige tidspunkter. _Prompt engineering teknikker kan hjælpe os med at minimere disse variationer ved at give bedre retningslinjer_.

2. **Modeller kan fabrikere svar.** Modeller er forudtrænet med _store, men endelige_ datasæt, hvilket betyder, at de mangler viden om begreber uden for den træningsomfang. Som et resultat kan de producere fuldførelser, der er unøjagtige, imaginære eller direkte modstridende med kendte fakta. _Prompt engineering teknikker hjælper brugere med at identificere og afbøde sådanne fabrikationer, f.eks. ved at bede AI om citater eller ræsonnering_.

3. **Modellernes kapaciteter vil variere.** Nyere modeller eller modelgenerationer vil have rigere kapaciteter, men også bringe unikke quirks og afvejninger i omkostninger og kompleksitet. _Prompt engineering kan hjælpe os med at udvikle bedste praksis og arbejdsgange, der abstraherer forskelle og tilpasser sig model-specifikke krav på skalerbare, sømløse måder_.

Lad os se dette i aktion i OpenAI eller Azure OpenAI Playground:

- Brug den samme prompt med forskellige LLM-implementeringer (f.eks. OpenAI, Azure OpenAI, Hugging Face) - så du variationerne?
- Brug den samme prompt gentagne gange med den _samme_ LLM-implementering (f.eks. Azure OpenAI playground) - hvordan adskilte disse variationer sig?

### Eksempel på fabrikationer

I dette kursus bruger vi udtrykket **"fabrikation"** til at referere til fænomenet, hvor LLM'er nogle gange genererer faktuelt ukorrekt information på grund af begrænsninger i deres træning eller andre begrænsninger. Du har måske også hørt dette omtalt som _"hallucinationer"_ i populære artikler eller forskningspapirer. Vi anbefaler dog stærkt at bruge _"fabrikation"_ som termen, så vi ikke utilsigtet antropomorfiserer adfærden ved at tilskrive en menneskelignende egenskab til et maskindrevet resultat. Dette understøtter også [Responsible AI retningslinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologiperspektiv, idet vi fjerner termer, der også kan betragtes som stødende eller ikke-inkluderende i nogle sammenhænge.

Vil du få en fornemmelse af, hvordan fabrikationer fungerer? Tænk på en prompt, der instruerer AI'en til at generere indhold for et ikke-eksisterende emne (for at sikre, at det ikke findes i træningsdatasættet). For eksempel - jeg prøvede denne prompt:

> **Prompt:** generer en lektionsplan om den Martianske Krig i 2076.

En websøgen viste mig, at der var fiktive beretninger (f.eks. tv-serier eller bøger) om martianske krige - men ingen i 2076. Sund fornuft fortæller os også, at 2076 er _i fremtiden_ og derfor ikke kan være forbundet med en reel begivenhed.

Så hvad sker der, når vi kører denne prompt med forskellige LLM-udbydere?

Som forventet producerer hver model (eller modelversion) lidt forskellige svar takket være stokastisk adfærd og variationer i modelkapacitet. For eksempel målretter en model et 8. klasses publikum, mens en anden antager en gymnasieelev. Men alle tre modeller genererede svar, der kunne overbevise en uinformeret bruger om, at begivenheden var reel.

Prompt engineering teknikker som _metaprompting_ og _temperaturkonfiguration_ kan reducere modelfabrikeringer til en vis grad. Nye prompt engineering _arkitekturer_ inkorporerer også nye værktøjer og teknikker sømløst i promptflowet for at afbøde eller reducere nogle af disse effekter.

## Case Study: GitHub Copilot

Lad os afslutte dette afsnit ved at få en fornemmelse af, hvordan prompt engineering bruges i virkelige løsninger ved at se på en Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI Pair Programmer" - den konverterer tekstprompts til kodefuldførelser og er integreret i dit udviklingsmiljø (f.eks. Visual Studio Code) for en sømløs brugeroplevelse. Som dokumenteret i serien af blogs nedenfor var den tidligste version baseret på OpenAI Codex-modellen - med ingeniører, der hurtigt indså behovet for at finjustere modellen og udvikle bedre prompt engineering teknikker for at forbedre kodekvaliteten. I juli debuterede de med en forbedret AI-model, der går ud over Codex for endnu hurtigere forslag.

Læs indlæggene i rækkefølge for at følge deres læringsrejse.

Du kan også gennemse deres [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere indlæg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), der viser, hvordan disse modeller og teknikker anvendes til at drive virkelige applikationer.

## Prompt Konstruktion

Vi har set, hvorfor prompt engineering er vigtig - lad os nu forstå, hvordan prompts er _konstrueret_, så vi kan evaluere forskellige teknikker til mere effektivt promptdesign.

### Grundlæggende Prompt

Lad os starte med den grundlæggende prompt: en tekstinput sendt til modellen uden anden kontekst. Her er et eksempel - når vi sender de første ord af den amerikanske nationalsang til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), fuldfører den straks svaret med de næste linjer, hvilket illustrerer den grundlæggende forudsigelses
Endelig ligger den reelle værdi af skabeloner i evnen til at skabe og udgive _prompt-biblioteker_ til vertikale applikationsdomæner - hvor prompt-skabelonen nu er _optimeret_ til at afspejle applikationsspecifik kontekst eller eksempler, der gør svarene mere relevante og præcise for den målrettede brugergruppe. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repositoryet er et godt eksempel på denne tilgang, der samler et bibliotek af prompts til uddannelsesområdet med vægt på nøglemål som lektionsplanlægning, læseplanlægning, elevvejledning osv.

## Understøttende indhold

Hvis vi tænker på prompt-konstruktion som at have en instruktion (opgave) og et mål (primært indhold), så er _sekundært indhold_ som yderligere kontekst, vi giver for at **påvirke output på en eller anden måde**. Det kan være justeringsparametre, formateringsinstruktioner, emnetaksonomier osv., der kan hjælpe modellen med at _tilpasse_ sit svar, så det passer til de ønskede brugerformål eller forventninger.

For eksempel: Givet en kursuskatalog med omfattende metadata (navn, beskrivelse, niveau, metadata tags, underviser osv.) på alle de tilgængelige kurser i læseplanen:

- vi kan definere en instruktion til "at opsummere kursuskataloget for efteråret 2023"
- vi kan bruge det primære indhold til at give nogle få eksempler på det ønskede output
- vi kan bruge det sekundære indhold til at identificere de 5 mest interessante "tags".

Nu kan modellen levere en opsummering i det format, der vises af de få eksempler - men hvis et resultat har flere tags, kan den prioritere de 5 tags, der er identificeret i det sekundære indhold.

---

## Bedste praksis for prompt-konstruktion

Nu hvor vi ved, hvordan prompts kan _konstrueres_, kan vi begynde at tænke på, hvordan man _designer_ dem til at afspejle bedste praksis. Vi kan tænke på dette i to dele - at have den rette _tankegang_ og anvende de rette _teknikker_.

### Tankegang inden for prompt-konstruktion

Prompt-konstruktion er en trial-and-error-proces, så husk tre brede vejledende faktorer:

1. **Domæneforståelse betyder noget.** Svarnøjagtighed og relevans er en funktion af det _domæne_, hvori applikationen eller brugeren opererer. Brug din intuition og domæneekspertise til at **tilpasse teknikker** yderligere. For eksempel kan du definere _domænespecifikke personligheder_ i dine systemprompts eller bruge _domænespecifikke skabeloner_ i dine brugerprompts. Giv sekundært indhold, der afspejler domænespecifikke kontekster, eller brug _domænespecifikke signaler og eksempler_ til at guide modellen mod velkendte brugsmønstre.

2. **Model forståelse betyder noget.** Vi ved, at modeller er stokastiske af natur. Men modelimplementeringer kan også variere i forhold til det træningsdatasæt, de bruger (forudindlært viden), de kapabiliteter, de tilbyder (f.eks. via API eller SDK) og den type indhold, de er optimeret til (f.eks. kode vs. billeder vs. tekst). Forstå styrkerne og begrænsningerne ved den model, du bruger, og brug den viden til at _prioritere opgaver_ eller bygge _tilpassede skabeloner_, der er optimeret til modellens kapabiliteter.

3. **Iteration & Validering betyder noget.** Modeller udvikler sig hurtigt, og det samme gør teknikkerne til prompt-konstruktion. Som domæneekspert kan du have anden kontekst eller kriterier for _din_ specifikke applikation, der muligvis ikke gælder for det bredere samfund. Brug prompt-konstruktion værktøjer & teknikker til at "starte" prompt-konstruktionen, og iterer og valider resultaterne ved hjælp af din egen intuition og domæneekspertise. Registrer dine indsigter og opret en **vidensbase** (f.eks. prompt-biblioteker), der kan bruges som en ny baseline af andre, for hurtigere iterationer i fremtiden.

## Bedste praksis

Lad os nu se på almindelige bedste praksis, der anbefales af [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikere.

| Hvad                              | Hvorfor                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluér de nyeste modeller.       | Nye modelgenerationer har sandsynligvis forbedrede funktioner og kvalitet - men kan også medføre højere omkostninger. Evaluér dem for påvirkning, og tag derefter migrationsbeslutninger.                                                              |
| Adskil instruktioner & kontekst   | Tjek om din model/udbyder definerer _afgrænsere_ til at skelne mellem instruktioner, primært og sekundært indhold mere tydeligt. Dette kan hjælpe modeller med at tildele vægte mere præcist til tokens.                                              |
| Vær specifik og klar              | Giv flere detaljer om den ønskede kontekst, resultat, længde, format, stil osv. Dette vil forbedre både kvaliteten og konsistensen af svarene. Indfang opskrifter i genanvendelige skabeloner.                                                         |
| Vær beskrivende, brug eksempler   | Modeller kan reagere bedre på en "vis og fortæl"-tilgang. Start med en `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` værdier. Gå tilbage til [Learning Sandbox-sektionen](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) for at lære hvordan.

### Åbn derefter Jupyter Notebook

- Vælg runtime-kernen. Hvis du bruger mulighederne 1 eller 2, skal du blot vælge den standard Python 3.10.x kerne, der leveres af udviklingscontaineren.

Du er klar til at køre øvelserne. Bemærk, at der ikke er nogen _rigtige og forkerte_ svar her - bare udforske muligheder ved trial-and-error og opbygge intuition for, hvad der virker for en given model og applikationsdomæne.

_Af denne grund er der ingen Code Solution segmenter i denne lektion. I stedet vil Notebook have Markdown-celler med titlen "Min løsning:", der viser et eksempeloutput til reference._

## Videnscheck

Hvilket af følgende er en god prompt efter nogle rimelige bedste praksis?

1. Vis mig et billede af en rød bil
2. Vis mig et billede af en rød bil af mærket Volvo og modellen XC90 parkeret ved en klippe med solen, der går ned
3. Vis mig et billede af en rød bil af mærket Volvo og modellen XC90

A: 2, det er den bedste prompt, da den giver detaljer om "hvad" og går i detaljer (ikke bare en hvilken som helst bil, men et specifikt mærke og model), og den beskriver også den overordnede indstilling. 3 er det næstbedste, da det også indeholder en masse beskrivelse.

## 🚀 Udfordring

Se om du kan udnytte "signal"-teknikken med prompten: Færdiggør sætningen "Vis mig et billede af en rød bil af mærket Volvo og ". Hvad svarer den med, og hvordan ville du forbedre det?

## Godt arbejde! Fortsæt din læring

Vil du lære mere om forskellige begreber inden for prompt-konstruktion? Gå til [siden for fortsat læring](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at finde andre gode ressourcer om dette emne.

Gå videre til Lektion 5, hvor vi vil se på [avancerede prompt-teknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.