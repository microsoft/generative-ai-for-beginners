# Grundläggande om Prompt Engineering

[![Grundläggande om Prompt Engineering](../../../translated_images/sv/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduktion
Denna modul täcker viktiga begrepp och tekniker för att skapa effektiva prompts i generativa AI-modeller. Hur du formulerar din prompt till en LLM spelar också roll. En noggrant utformad prompt kan ge bättre kvalitet på svaret. Men vad betyder egentligen termer som _prompt_ och _prompt engineering_? Och hur förbättrar jag promptens _input_ som jag skickar till LLM? Dessa är frågor vi ska försöka besvara i detta kapitel och nästa.

_Generativ AI_ kan skapa nytt innehåll (t.ex. text, bilder, ljud, kod etc.) som svar på användarförfrågningar. Den gör detta med hjälp av _stora språkmodeller_ som OpenAIs GPT ("Generative Pre-trained Transformer")-serie som är tränade för att använda naturligt språk och kod.

Användare kan nu interagera med dessa modeller med välbekanta paradigm som chatt, utan teknisk expertis eller utbildning. Modellerna är _prompt-baserade_ – användare skickar en textinmatning (prompt) och får tillbaka AI-svaret (komplettering). De kan sedan "chatta med AI:n" iterativt, i fleromgångssamtal, och förbättra sin prompt tills svaret motsvarar deras förväntningar.

"Prompter" blir nu det primära _programmeringsgränssnittet_ för generativa AI-appar, som berättar för modellerna vad de ska göra och påverkar kvaliteten på de återlämnade svaren. "Prompt Engineering" är ett snabbt växande studiefält som fokuserar på _design och optimering_ av prompts för att leverera konsekventa och kvalitativa svar i stor skala.

## Lärandemål

I denna lektion lär vi oss vad prompt engineering är, varför det är viktigt och hur vi kan skapa mer effektiva prompts för en given modell och applikationsmål. Vi kommer att förstå kärnbegrepp och bästa praxis för prompt engineering – och lära oss om en interaktiv Jupyter Notebook "sandbox"-miljö där vi kan se dessa begrepp tillämpas på riktiga exempel.

I slutet av denna lektion kommer vi att kunna:

1. Förklara vad prompt engineering är och varför det är viktigt.
2. Beskriva komponenterna i en prompt och hur de används.
3. Lära oss bästa praxis och tekniker för prompt engineering.
4. Använda inlärda tekniker på riktiga exempel, med en OpenAI-endpoint.

## Nyckeltermer

Prompt Engineering: Praktiken att utforma och finjustera indata för att vägleda AI-modeller att producera önskade resultat.
Tokenisering: Processen att omvandla text till mindre enheter, kallade tokens, som en modell kan förstå och bearbeta.
Instruktionsjusterade LLM: Stora språkmodeller (LLM) som finjusterats med specifika instruktioner för att förbättra deras svarens noggrannhet och relevans.

## Lärande sandbox

Prompt engineering är för närvarande mer konst än vetenskap. Det bästa sättet att förbättra vår intuition för det är att _träna mer_ och anta ett trial-and-error tillvägagångssätt som kombinerar expertis inom applikationsdomänen med rekommenderade tekniker och modell-specifika optimeringar.

Jupyter Notebook som hör till denna lektion erbjuder en _sandbox_-miljö där du kan prova det du lär dig – löpande eller som en del av kodutmaningen i slutet. För att genomföra övningarna behöver du:

1. **En Azure OpenAI API-nyckel** – tjänstens endpoint för en installerad LLM.
2. **En Python runtime** – där Notebook kan köras.
3. **Lokala miljövariabler** – _slutför [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) stegen nu för att bli redo_.

Notebooken levereras med _börjarter_övningar – men du uppmuntras att lägga till egna _Markdown_- (beskrivning) och _Code_- (promptförfrågningar) sektioner för att prova fler exempel eller idéer – och bygga din intuition för promptdesign.

## Illustrerad guide

Vill du få en överblick över vad denna lektion täcker innan du börjar? Kolla in denna illustrerade guide som ger dig en känsla av huvudämnena som behandlas och viktiga punkter för dig att fundera över i varje. Lektionens vägkarta tar dig från att förstå kärnbegrepp och utmaningar till att hantera dem med relevanta prompt engineering-tekniker och bästa praxis. Observera att avsnittet "Avancerade tekniker" i denna guide avser innehåll som täcks i _nästa_ kapitel i denna kursplan.

![Illustrerad guide till Prompt Engineering](../../../translated_images/sv/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vårt startup

Nu, låt oss prata om hur _detta ämne_ förhåller sig till vår startup-uppdrag att [bringa AI-innovation till utbildning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi vill bygga AI-drivna applikationer för _personligt anpassat lärande_ – så låt oss tänka på hur olika användare av vår applikation kan "designa" prompts:

- **Administratörer** kan be AI:n _analysera läroplansdata för att identifiera täckningsluckor_. AI:n kan sammanfatta resultat eller visualisera dem med kod.
- **Pedagoger** kan be AI:n _generera en lektionsplan för en målgrupp och ämne_. AI:n kan skapa en personlig plan i ett angivet format.
- **Studenter** kan be AI:n _lära dem i ett svårt ämne_. AI:n kan nu vägleda studenter med lektioner, tips och exempel anpassade efter deras nivå.

Det är bara toppen av isberget. Kolla in [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – ett open-source promptsbibliotek kuraterat av utbildningsexperter – för att få en bredare känsla av möjligheterna! _Testa att köra några av dessa prompts i sandlådan eller med OpenAI Playground för att se vad som händer!_

<!--
LEKTIONSMALL:
Denna enhet ska täcka kärnbegrepp #1.
Stärka begreppet med exempel och referenser.

BEGREPP #1:
Prompt Engineering.
Definiera det och förklara varför det behövs.
-->

## Vad är Prompt Engineering?

Vi började denna lektion med att definiera **Prompt Engineering** som processen att _designa och optimera_ textinmatningar (prompter) för att leverera konsekventa och kvalitativa svar (kompletteringar) för ett givet applikationsmål och modell. Vi kan tänka på detta som en 2-stegsprocess:

- _designa_ den ursprungliga prompten för en given modell och mål
- _förfina_ prompten iterativt för att förbättra svarskvaliteten

Detta är nödvändigtvis en trial-and-error process som kräver användarintution och ansträngning för att nå optimala resultat. Så varför är det viktigt? För att svara på den frågan behöver vi först förstå tre begrepp:

- _Tokenisering_ = hur modellen "ser" prompten
- _Bas-LLM_ = hur grundmodellen "bearbetar" en prompt
- _Instruktionsjusterade LLM_ = hur modellen nu kan se "uppgifter"

### Tokenisering

En LLM ser prompts som en _sekvens av tokens_ där olika modeller (eller versioner av en modell) kan tokenisera samma prompt på olika sätt. Eftersom LLM-tränas på tokens (och inte rå text) har hur prompts tokeniseras direkt påverkan på kvaliteten på det genererade svaret.

För att få en intuition för hur tokenisering fungerar, prova verktyg som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) nedan. Kopiera in din prompt – och se hur den omvandlas till tokens, med uppmärksamhet på hur mellanslags-tecken och skiljetecken hanteras. Observera att detta exempel visar en äldre LLM (GPT-3) – så att prova med en nyare modell kan ge ett annat resultat.

![Tokenisering](../../../translated_images/sv/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Begrepp: Grundmodeller

När en prompt är tokeniserad är det huvudsakliga syftet med ["Bas-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grundmodell) att förutsäga token som kommer nästa i sekvensen. Eftersom LLM är tränade på massiva textdatamängder har de en god känsla för statistiska samband mellan tokens och kan göra den förutsägelsen med viss säkerhet. Observera att de inte förstår _meningen_ i orden i prompten eller token; de ser bara ett mönster de kan "komplettera" med sin nästa förutsägelse. De kan fortsätta förutsäga sekvensen tills användaren avbryter eller en förutbestämd villkor uppfylls.

Vill du se hur promptbaserad generering fungerar? Skriv in prompten ovan i [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) med standardinställningarna. Systemet är konfigurerat för att behandla prompts som informationsförfrågningar – så du bör se en generering som passar detta sammanhang.

Men om användaren ville se något specifikt som uppfyller vissa kriterier eller uppgiftsmål? Det är här _instruktionsjusterade_ LLM kommer in i bilden.

![Bas-LLM Chat Completion](../../../translated_images/sv/04-playground-chat-base.65b76fcfde0caa67.webp)

### Begrepp: Instruktionsjusterade LLM

En [Instruktionsjusterad LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) börjar med grundmodellen och finjusteras med exempel eller indata/utdata-par (t.ex. fleromgångs "meddelanden") som kan innehålla tydliga instruktioner – och svaret från AI försöker följa den instruktionen.

Detta använder tekniker som förstärkningsinlärning med mänsklig återkoppling (RLHF) som kan träna modellen att _följa instruktioner_ och _lära av feedback_ så att den producerar svar som är bättre anpassade för praktiska tillämpningar och mer relevanta för användarens mål.

Låt oss prova – gå tillbaka till prompten ovan, men ändra nu _systemmeddelandet_ till att ge följande instruktion som kontext:

> _Sammanfatta innehåll du får för en elev i årskurs två. Håll resultatet till ett stycke med 3-5 punktlistor._

Ser du hur resultatet nu är justerat för att spegla det önskade målet och formatet? En pedagog kan nu direkt använda detta svar i sina presentationer för den klassen.

![Instruktionsjusterad LLM Chat Completion](../../../translated_images/sv/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Varför behöver vi Prompt Engineering?

Nu när vi vet hur prompts bearbetas av LLM, låt oss prata om _varför_ vi behöver prompt engineering. Svaret ligger i att nuvarande LLM har flera utmaningar som gör det svårare att uppnå _pålitliga och konsekventa svar_ utan att lägga ansträngning på konstruktion och optimering av prompten. Till exempel:

1. **Modellens svar är stokastiska.** _Samma prompt_ kommer sannolikt att producera olika svar beroende på modell eller modellversion. Och det kan till och med ge olika svar med _samma modell_ vid olika tidpunkter. _Prompt engineering-tekniker kan hjälpa oss att minimera dessa variationer genom att ge bättre styrning_.

1. **Modeller kan hitta på svar.** Modeller är förtränade med _stora men begränsade_ dataset, vilket innebär att de saknar kunskap om koncept utanför det träningsomfånget. Som ett resultat kan de producera svar som är felaktiga, påhittade eller direkt motsägelsefulla gentemot kända fakta. _Prompt engineering hjälper användare att identifiera och mildra sådana påhitt, t.ex. genom att be AI:n om källhänvisningar eller resonemang_.

1. **Modellernas kapabiliteter varierar.** Nyare modeller eller generationsskiften har rikare kapabiliteter men för med sig unika egenheter och kompromisser i kostnad och komplexitet. _Prompt engineering hjälper oss att utveckla bästa praxis och arbetsflöden som abstraherar skillnader och anpassar sig till modell-specifika krav på ett skalbart och sömlöst sätt_.

Låt oss se detta i praktiken i OpenAI eller Azure OpenAI Playground:

- Använd samma prompt med olika LLM-implementeringar (t.ex. OpenAI, Azure OpenAI, Hugging Face) – såg du variationerna?
- Använd samma prompt upprepade gånger med _samma_ LLM-implementering (t.ex. Azure OpenAI playground) – hur skiljde sig dessa variationer?

### Exempel på påhittade svar

I denna kurs använder vi termen **"påhitt"** för att referera till fenomenet att LLM ibland genererar faktamässigt inkorrekt information på grund av begränsningar i deras träning eller andra begränsningar. Du kan också ha hört detta kallat _"hallucinationer"_ i populärvetenskapliga artiklar eller forskningspublikationer. Vi rekommenderar dock starkt att använda _"påhitt"_ som term för att undvika att antropomorfisera beteendet genom att tillskriva en mänsklig egenskap till en maskinbaserad process. Detta stärker också [ansvarsfull AI-riktlinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ur ett terminologiskt perspektiv, genom att ta bort termer som kan uppfattas som stötande eller icke-inkluderande i vissa sammanhang.

Vill du få en känsla för hur påhitt fungerar? Tänk på en prompt som instruerar AI att generera innehåll för ett icke-existerande ämne (för att säkerställa att det inte finns i träningsdata). Till exempel – jag testade denna prompt:

> **Prompt:** generera en lektionsplan om Marskriget år 2076.

En webbsökning visade att det finns fiktiva skildringar (t.ex. tv-serier eller böcker) om Marskrig – men inga från 2076. Sunt förnuft säger oss också att 2076 är _i framtiden_ och därför inte kan kopplas till en verklig händelse.


Vad händer då när vi kör denna prompt med olika LLM-leverantörer?

> **Svar 1**: OpenAI Playground (GPT-35)

![Svar 1](../../../translated_images/sv/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Svar 2](../../../translated_images/sv/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Svar 3](../../../translated_images/sv/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som förväntat producerar varje modell (eller modellversion) något olika svar tack vare stokastiskt beteende och variationer i modellens kapacitet. Till exempel riktar sig en modell till en åttondeklassare medan den andra antar en gymnasieelev. Men alla tre modeller genererade svar som skulle kunna övertyga en oinformerad användare om att händelsen var verklig.

Prompttekniker såsom _metaprompting_ och _temperaturinställning_ kan i viss mån minska modellens fabriceringar. Nya prompttekniska _arkitekturer_ integrerar också nya verktyg och tekniker sömlöst i promptflödet för att mildra eller minska några av dessa effekter.

## Fallstudie: GitHub Copilot

Låt oss avsluta detta avsnitt med att få en känsla för hur promptteknik används i verkliga lösningar genom att titta på en fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot är din "AI-parprogrammerare" – den konverterar textpromptar till kodkompletteringar och är integrerad i din utvecklingsmiljö (t.ex. Visual Studio Code) för en sömlös användarupplevelse. Som dokumenterat i bloggsserien nedan baserades den tidigaste versionen på OpenAI Codex-modellen – med ingenjörer som snabbt insåg behovet av att finjustera modellen och utveckla bättre prompttekniker för att förbättra kodkvaliteten. I juli [lanserade de en förbättrad AI-modell som går bortom Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) för ännu snabbare förslag.

Läs inläggen i ordning för att följa deras läranderesa.

- **Maj 2023** | [GitHub Copilot blir bättre på att förstå din kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inifrån GitHub: Att arbeta med LLM:er bakom GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Hur man skriver bättre promptar för GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot går bortom Codex med förbättrad AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En utvecklares guide till promptteknik och LLM:er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hur man bygger en företags-LLM-app: Lärdomar från GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan också bläddra i deras [Ingenjörsblogg](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) för fler inlägg som [det här](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som visar hur dessa modeller och tekniker _tillämpas_ för att driva verkliga tillämpningar.

---

<!--
LEKTIONSMALL:
Den här enheten bör täcka kärnkoncept #2.
Förstärk konceptet med exempel och referenser.

KONCEPT #2:
Promptdesign.
Illustrerat med exempel.
-->

## Promptuppbyggnad

Vi har sett varför promptteknik är viktigt – nu ska vi förstå hur promptar _konstrueras_ så att vi kan utvärdera olika tekniker för mer effektiv promptdesign.

### Grundläggande prompt

Låt oss börja med en grundläggande prompt: en textinmatning skickad till modellen utan annan kontext. Här är ett exempel – när vi skickar de första orden i USA:s nationalsång till OpenAI:s [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) fullbordar den omedelbart svaret med nästa rader, vilket illustrerar grundläggande förutsägelsebeteende.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det låter som att du börjar med texten till "The Star-Spangled Banner", USA:s nationalsång. Den fullständiga texten är ...                    |

### Avancerad prompt

Nu lägger vi till kontext och instruktioner till den grundläggande prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) låter oss konstruera en komplex prompt som en samling av _meddelanden_ med:

- Inmatnings-/utmatningspar som speglar _användarens_ inmatning och _assistentens_ svar.
- Systemmeddelande som sätter kontext för assistentens beteende eller personlighet.

Förfrågan är nu i formen nedan, där _tokenisering_ effektivt fångar relevant information från kontext och konversation. Att ändra systemkontexten kan nu vara lika påverkningsfullt för kvaliteten på svar som användarens inmatningar.

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

I exemplen ovan var användarprompten en enkel textfråga som kan tolkas som en informationsförfrågan. Med _instruktions_-promptar kan vi använda den texten för att specificera en uppgift mer i detalj och ge AI:n bättre vägledning. Här är ett exempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruktionstyp    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returnerade ett enkelt stycke_                                                                                          | Enkel              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returnerade ett stycke följt av en lista med viktiga datum och beskrivningar av händelser_                                | Komplex            |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returnerar mer utförliga detaljer i en textruta, formaterad som JSON som du kan kopiera och validera vid behov_             | Komplex. Formaterad. |

## Primärt innehåll

I exemplen ovan var prompten fortfarande ganska öppen, vilket tillät LLM att avgöra vilken del av dess förtränade dataset som var relevant. Med designmönstret _primärt innehåll_ delas inmatningstexten upp i två delar:

- en instruktion (åtgärd)
- relevant innehåll (som påverkar åtgärden)

Här är ett exempel där instruktionen är att "sammanfatta detta i 2 meningar".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter är den femte planeten från solen och den största i solsystemet. Den är en gasjätte med en massa av en tusendel av solens men två och en halv gånger massan av alla andra planeter tillsammans. Jupiter är ett av de ljusaste objekten synliga för blotta ögat på natthimlen och har varit känd av forntida civilisationer sedan innan historien skrevs ner. Den är uppkallad efter den romerska guden Jupiter.[19] När den ses från jorden kan Jupiter vara tillräckligt ljus för att kasta synliga skuggor,[20] och är i genomsnitt det tredje ljusaste naturliga objektet på natthimlen efter månen och Venus. <br/> **Sammanfatta detta i 2 korta meningar** | Jupiter, den femte planeten från solen, är den största i solsystemet och är känd för att vara ett av de ljusaste objekten på natthimlen. Uppkallad efter den romerska guden Jupiter, är det en gasjätte vars massa är två och en halv gånger så stor som alla andra planeter i solsystemet tillsammans. |

Segmentet med primärt innehåll kan användas på olika sätt för att driva mer effektiva instruktioner:

- **Exempel** - istället för att berätta för modellen vad den ska göra med en explicit instruktion, ge den exempel på vad den ska göra och låt den dra slutsatser om mönstret.
- **Ledtrådar** - följ instruktionen med en "ledtråd" som förbereder utmatningen, vilket riktar modellen mot mer relevanta svar.
- **Mall** - detta är upprepbara 'recept' för prompts med platshållare (variabler) som kan anpassas med data för specifika användningsfall.

Låt oss utforska dessa i praktiken.

### Använda exempel

Detta är en metod där du använder det primära innehållet för att "mata modellen" med exempel på önskat resultat för en given instruktion och låta den dra slutsatsen om mönstret för det önskade resultatet. Baserat på antalet exempel kan vi ha zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nu av tre komponenter:

- En uppgiftsbeskrivning
- Några exempel på önskat resultat
- Början på ett nytt exempel (vilket blir en implicit uppgiftsbeskrivning)

| Inlärningstyp | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Översätt till spanska                                                                                                         | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Spelaren sprang baserna => Baseball <br/> Spelaren slog ess => Tennis <br/> Spelaren slog sexa => Cricket <br/> Spelaren gjorde en dunk =>             | Basket                      |
|               |                                                                                                                                                       |                             |

Notera hur vi behövde ge en explicit instruktion ("Översätt till spanska") i zero-shot prompting, men att det dras slutsatser i one-shot-exemplet. Few-shot-exemplet visar hur fler exempel låter modeller göra mer exakta slutsatser utan fler instruktioner.

### Promptledtrådar

En annan teknik för att använda primärt innehåll är att ge _ledtrådar_ snarare än exempel. I det här fallet ger vi modellen en knuff åt rätt håll genom att _starta_ med ett utdrag som speglar önskat svarsformat. Modellen "tar då ledtråden" och fortsätter i samma stil.

| Antal ledtrådar | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter är den femte planeten från solen och den största i solsystemet. Den är en gasjätte med en massa av en tusendel av solens men två och en halv gånger massan av alla andra planeter tillsammans. Jupiter är ett av de ljusaste objekten synliga för blotta ögat på natthimlen, och har varit känd av forntida civilisationer sedan innan historien skrevs ner. <br/>**Sammanfatta detta**                                                   | Jupiter är den största planeten i vårt solsystem och den femte från solen. Det är en gasjätte med en massa som är en tusendel av solens, men tyngre än alla andra planeter tillsammans. Forntida civilisationer har känt till Jupiter länge, och den är lätt synlig på natthimlen.               |
| 1              | Jupiter är den femte planeten från solen och den största i solsystemet. Den är en gasjätte med en massa av en tusendel av solens men två och en halv gånger massan av alla andra planeter tillsammans. Jupiter är ett av de ljusaste objekten synliga för blotta ögat på natthimlen, och har varit känd av forntida civilisationer sedan innan historien skrevs ner. <br/>**Sammanfatta detta** <br/> Vad vi lärde oss är att Jupiter | är den femte planeten från solen och den största i solsystemet. Den är en gasjätte med en massa av en tusendel av solens men två och en halv gånger massan av alla andra planeter tillsammans. Den är lätt synlig för blotta ögat och har varit känd sedan forntiden.                     |

| 2              | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger massan av alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusstarkaste objekten som är synliga för blotta ögat på natthimlen och har varit känt för gamla civilisationer sedan före den nedskrivna historien. <br/>**Sammanfatta detta** <br/> Topp 3 fakta vi lärde oss:         | 1. Jupiter är den femte planeten från solen och den största i solsystemet. <br/> 2. Det är en gasjätte med en massa som är en tusendel av solens...<br/> 3. Jupiter har varit synlig för blotta ögat sedan antiken ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Mallar för promptar

En promptmall är ett _fördefinierat recept för en prompt_ som kan sparas och återanvändas vid behov, för att skapa mer konsekventa användarupplevelser i stor skala. I sin enklaste form är det helt enkelt en samling promptexempel som [det här från OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) som tillhandahåller både interaktiva promptkomponenter (användar- och systemmeddelanden) och API-styrd förfrågningsformat - för att stödja återanvändning.

I sin mer komplexa form som [detta exempel från LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) innehåller den _platshållare_ som kan ersättas med data från olika källor (användarinmatning, systemkontext, externa datakällor etc.) för att dynamiskt generera en prompt. Detta gör att vi kan skapa ett bibliotek av återanvändbara promptar som kan användas för att programmässigt skapa konsekventa användarupplevelser i stor skala.

Slutligen ligger det verkliga värdet i mallarna i möjligheten att skapa och publicera _promptbibliotek_ för vertikala applikationsdomäner - där promptmallen nu är _optimerad_ för att spegla kontext eller exempel specifika för applikationen som gör svaren mer relevanta och korrekta för den målgrupp som avses. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)-arkivet är ett utmärkt exempel på detta tillvägagångssätt, som curerar ett bibliotek av promptar för utbildningsområdet med fokus på nyckelmål som lektionsplanering, kursplanering, handledning av studenter etc.

## Stödjande innehåll

Om vi tänker på promptkonstruktion som att ha en instruktion (uppgift) och ett mål (primärt innehåll), är _sekundärt innehåll_ som ytterligare kontext vi tillhandahåller för att **påverka utdata på något sätt**. Det kan vara justeringsparametrar, formateringsinstruktioner, ämnestaxonomier etc. som hjälper modellen att _anpassa_ sitt svar för att passa önskade användarmål eller förväntningar.

Till exempel: Givet en kurskatalog med omfattande metadata (namn, beskrivning, nivå, metadatataggar, instruktör etc.) över alla tillgängliga kurser i kursplanen:

- kan vi definiera en instruktion för att "sammanfatta kurskatalogen för hösten 2023"
- kan vi använda det primära innehållet för att ge några exempel på önskad utdata
- kan vi använda det sekundära innehållet för att identifiera topp 5 "taggar" av intresse.

Nu kan modellen ge en sammanfattning i det format som visas av de få exemplen – men om ett resultat har flera taggar kan den prioritera de 5 taggar som identifieras i sekundärt innehåll.

---

<!--
LEKTIONSMALL:
Den här enheten bör täcka kärnbegrepp #1.
Förstärk begreppet med exempel och referenser.

KÄRJEBREPP #3:
Tekniker för promptutformning.
Vad är några grundläggande tekniker för promptutformning?
Illustrera med några övningar.
-->

## Bästa praxis för promptning

Nu när vi vet hur promptar kan _konstrueras_, kan vi börja tänka på hur man _designar_ dem för att spegla bästa praxis. Vi kan se på detta i två delar – att ha rätt _tänkande_ och att tillämpa rätt _tekniker_.

### Tänkande för promptutformning

Promptutformning är en process med försök och misstag, så håll tre breda vägledande faktorer i åtanke:

1. **Domänförståelse är viktigt.** Svars noggrannhet och relevans är en funktion av den _domän_ som applikationen eller användaren verkar inom. Använd din intuition och domänkompetens för att **anpassa tekniker** ytterligare. Definiera till exempel _domänspecifika personligheter_ i dina systempromptar, eller använd _domänspecifika mallar_ i dina användarpromptar. Tillhandahåll sekundärt innehåll som speglar domänspecifika kontexter, eller använd _domänspecifika ledtrådar och exempel_ för att guida modellen mot välbekanta användningsmönster.

2. **Förståelse av modellen är viktigt.** Vi vet att modeller är stokastiska till sin natur. Men modellimplementationer kan också variera vad gäller den träningsdatamängd de använder (förtränad kunskap), de funktioner de ger (t.ex. via API eller SDK) och vilken typ av innehåll de är optimerade för (t.ex. kod vs bilder vs text). Förstå styrkor och begränsningar hos den modell du använder, och använd den kunskapen för att _prioritera uppgifter_ eller bygga _anpassade mallar_ som är optimerade för modellens funktioner.

3. **Iteration och validering är viktigt.** Modeller utvecklas snabbt, och det gör också teknikerna för promptutformning. Som domänexpert kan du ha annan kontext eller kriterier för _din_ specifika applikation som kanske inte gäller för den bredare gemenskapen. Använd verktyg och tekniker för promptutformning för att "kickstarta" promptkonstruktionen, iterera sedan och validera resultat med din egen intuition och domänkunskap. Dokumentera dina insikter och skapa en **kunskapsbas** (t.ex. promptbibliotek) som andra kan använda som ny baslinje för snabbare iterationer i framtiden.

## Bästa praxis

Nu ska vi titta på vanliga bästa praxis som rekommenderas av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) och [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktiker.

| Vad                              | Varför                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Utvärdera de senaste modellerna. | Nya modellgenerationer förväntas ha förbättrade funktioner och kvalitet - men kan också medföra högre kostnader. Utvärdera deras effekt och fatta beslut om migrering.                                                                             |
| Separera instruktioner och kontext| Kontrollera om din modell/leverantör definierar _avgränsare_ för att tydligare skilja instruktioner, primärt och sekundärt innehåll. Detta kan hjälpa modeller att tilldela vikt mer exakt till tokens.                                            |
| Var specifik och tydlig           | Ge mer detaljer om önskad kontext, resultat, längd, format, stil etc. Detta förbättrar både kvalitet och konsekvens i svaren. Dokumentera recept i återanvändbara mallar.                                                                        |
| Var beskrivande, använd exempel   | Modeller svarar ofta bättre på en "visa och berätta"-metod. Börja med en `zero-shot`-metod där du ger en instruktion (men inga exempel) och prova sedan `few-shot` som förfining genom att ge några exempel på önskat resultat. Använd analogier.     |
| Använd ledtrådar för att starta svar | Styr modellen mot önskat resultat genom att ge några ledande ord eller fraser som den kan använda som startpunkt för svaret.                                                                                                                    |
| Dubbelkolla                      | Ibland kan du behöva upprepa dig för modellen. Ge instruktioner före och efter ditt primära innehåll, använd en instruktion och en ledtråd, osv. Iterera och validera för att se vad som fungerar.                                                  |
| Ordningen spelar roll             | Ordningen du presenterar information för modellen kan påverka resultatet, även i inlärningsexemplen, tack vare färskhetsbias. Prova olika alternativ för att se vad som fungerar bäst.                                                            |
| Ge modellen en "utväg"            | Ge modellen ett _reservsvar_ som den kan ge om den inte kan slutföra uppgiften av någon anledning. Detta kan minska risken att modeller genererar falska eller påhittade svar.                                                                     |
|                                   |                                                                                                                                                                                                                                                   |

Som med all bästa praxis, kom ihåg att _din erfarenhet kan variera_ beroende på modell, uppgift och domän. Använd dessa som utgångspunkt och iterera för att hitta vad som fungerar bäst för dig. Utvärdera kontinuerligt din promptutformningsprocess i takt med att nya modeller och verktyg blir tillgängliga, med fokus på processens skalbarhet och svarskvalitet.

<!--
LEKTIONSMALL:
Den här enheten bör erbjuda en kodutmaning om tillämpligt.

UTMANING:
Länk till en Jupyter Notebook med enbart kodkommentarer i instruktionerna (kodsektioner är tomma).

LÖSNING:
Länk till en kopia av den Notebook där promptarna är ifyllda och körda som visar ett exempel på en lösning.
-->

## Uppgift

Grattis! Du har kommit till slutet av lektionen! Det är dags att testa några av dessa koncept och tekniker med verkliga exempel!

För vår uppgift kommer vi att använda en Jupyter Notebook med övningar som du kan göra interaktivt. Du kan också utöka Notebooken med egna Markdown- och kodceller för att utforska idéer och tekniker på egen hand.

### För att komma igång, forka repot, och sedan

- (Rekommenderat) Starta GitHub Codespaces
- (Alternativt) Klona repot till din lokala enhet och använd det med Docker Desktop
- (Alternativt) Öppna Notebooken med din föredragna Notebook-runtime-miljö.

### Nästa, konfigurera dina miljövariabler

- Kopiera filen `.env.copy` i roten av repot till `.env` och fyll i värdena för `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` och `AZURE_OPENAI_DEPLOYMENT`. Gå tillbaka till [Learning Sandbox-avsnittet](#lärande-sandbox) för att lära dig hur.

### Nästa, öppna Jupyter Notebooken

- Välj runtime-kärnan. Om du använder alternativ 1 eller 2, välj helt enkelt standard Python 3.10.x-kärna som tillhandahålls av devcontainern.

Du är redo att köra övningarna. Observera att det inte finns några _rätta och fel_ svar här – bara att utforska alternativ genom försök och misstag och bygga intuition för vad som fungerar för en given modell och applikationsdomän.

_Av denna anledning finns det inga kodlösningssegment i denna lektion. Istället kommer Notebooken att ha Markdown-celler med titeln "Min lösning:" som visar ett exempel på utdata för referens._

 <!--
LEKTIONSMALL:
Avsluta avsnittet med en sammanfattning och resurser för självstyrd lärande.
-->

## Kontrollfrågor

Vilken av följande är en bra prompt som följer några rimliga bästa praxis?

1. Visa mig en bild på en röd bil
2. Visa mig en bild på en röd bil av märket Volvo och modellen XC90 parkerad vid en klippa med solnedgången
3. Visa mig en bild på en röd bil av märket Volvo och modellen XC90

Svar: 2, det är den bästa prompten eftersom den ger detaljer om "vad" och går in på specifika detaljer (inte vilken bil som helst utan ett specifikt märke och modell) och den beskriver också den övergripande miljön. 3 är näst bäst eftersom den också innehåller mycket beskrivning.

## 🚀 Utmaning

Se om du kan använda "ledtråd"-tekniken med prompten: Kompletta meningen "Visa mig en bild på en röd bil av märket Volvo och ". Vad svarar den med och hur skulle du förbättra den?

## Bra jobbat! Fortsätt ditt lärande

Vill du lära dig mer om olika koncept inom promptutformning? Gå till [fortsatt lärande-sidan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att hitta andra utmärkta resurser om detta ämne.

Gå vidare till Lektion 5 där vi kommer att titta på [avancerade promptningstekniker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->