# Grundläggande om Prompt Engineering

[![Grundläggande om Prompt Engineering](../../../translated_images/sv/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduktion
Den här modulen täcker grundläggande koncept och tekniker för att skapa effektiva prompts i generativa AI-modeller. Hur du formulerar din prompt till en LLM spelar också roll. En omsorgsfullt utformad prompt kan ge en bättre kvalitativ respons. Men vad innebär egentligen termer som _prompt_ och _prompt engineering_? Och hur förbättrar jag prompt-_input_ som jag skickar till LLM? Det här är frågor vi kommer försöka besvara i det här kapitlet och nästa.

_Generativ AI_ kan skapa nytt innehåll (t.ex. text, bilder, ljud, kod etc.) som svar på användarförfrågningar. Detta uppnås med hjälp av _stora språkmodeller_ som OpenAIs GPT ("Generative Pre-trained Transformer")-serie som tränas för att använda naturligt språk och kod.

Användare kan nu interagera med dessa modeller med bekanta paradigmer som chatt, utan behov av teknisk expertis eller utbildning. Modellerna är _prompt-baserade_ – användare skickar en textinput (prompt) och får tillbaka AI-svar (completion). De kan sedan "chatta med AI" iterativt, i flera turer, och förfina sin prompt tills svaret motsvarar deras förväntningar.

"Prompter" blir nu primära _programmeringsgränssnitt_ för generativa AI-appar, som talar om för modellerna vad de ska göra och påverkar kvaliteten på de svar som returneras. "Prompt Engineering" är ett snabbt växande forskningsområde som fokuserar på _design och optimering_ av prompts för att leverera konsekventa och kvalitativa svar i stor skala.

## Lärandemål

I denna lektion lär vi oss vad Prompt Engineering är, varför det är viktigt, och hur vi kan skapa mer effektiva prompts för en given modell och applikationsmål. Vi kommer att förstå grundläggande koncept och bästa praxis för prompt engineering – och lära oss om en interaktiv Jupyter Notebooks-"sandlåda" där vi kan se dessa koncept tillämpade på riktiga exempel.

I slutet av lektionen ska vi kunna:

1. Förklara vad prompt engineering är och varför det är viktigt.
2. Beskriva komponenterna i en prompt och hur de används.
3. Lära oss bästa praxis och tekniker för prompt engineering.
4. Använda inlärda tekniker på verkliga exempel, med en OpenAI-endpoint.

## Nyckeltermer

Prompt Engineering: Praktiken att designa och förfina input för att styra AI-modeller mot att producera önskade resultat.  
Tokenisering: Processen att omvandla text till mindre enheter, kallade tokens, som en modell kan förstå och bearbeta.  
Instruction-Tuned LLMs: Stora språkmodeller (LLMs) som finjusterats med specifika instruktioner för att förbättra noggrannhet och relevans i svaren.

## Lär-sandlåda

Prompt engineering är för närvarande mer konst än vetenskap. Det bästa sättet att förbättra vår intuition är att _övning ger färdighet_ och att adoptera en trial-and-error-approach som kombinerar domänexpertis med rekommenderade tekniker och modell-specifika optimeringar.

Jupyter Notebook som hör till denna lektion erbjuder en _sandlåda_-miljö där du kan prova det du lär dig – allt eftersom eller som en del av kodutmaningen i slutet. För att genomföra övningarna behöver du:

1. **En Azure OpenAI API-nyckel** – servicens endpoint för en utplacerad LLM.  
2. **En Python-runtime** – där Notebook kan köras.  
3. **Lokala miljövariabler** – _slutför [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)-stegen nu för att vara redo_.

Noteboken levereras med _startövningar_ – men du uppmuntras att lägga till egna _Markdown_-beskrivningar och _Code_-sektioner (prompt-förfrågningar) för att testa fler exempel eller idéer – och bygga din intuition för promptdesign.

## Illustrerad guide

Vill du få en översikt över vad denna lektion innehåller innan du dyker in? Kolla in denna illustrerade guide som ger dig en känsla för huvudämnena och viktiga insikter att fundera över i varje avsnitt. Lektionens färdplan leder dig från förståelse av grundläggande begrepp och utmaningar till att hantera dem med relevanta tekniker och bästa praxis för prompt engineering. Observera att avsnittet "Avancerade tekniker" i denna guide avser innehåll som täcks i det _nästa_ kapitlet i denna kurs.

![Illustrerad guide till Prompt Engineering](../../../translated_images/sv/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Vårt startup-företag

Nu, låt oss prata om hur _detta ämne_ relaterar till vårt startup-uppdrag att [ta AI-innovation till utbildning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi vill bygga AI-drivna applikationer för _personanpassat lärande_ – så låt oss tänka på hur olika användare av vår applikation kan "designa" promts:

- **Administratörer** kan be AI att _analysera kursplansdata för att identifiera luckor i täckningen_. AI kan sammanfatta resultaten eller visualisera dem med kod.  
- **Lärare** kan be AI att _generera en lektionsplan för en specifik målgrupp och ämne_. AI kan bygga den personanpassade planen i önskat format.  
- **Studenter** kan be AI att _handleda dem i ett svårt ämne_. AI kan guida studenter med lektioner, ledtrådar och exempel anpassade efter deras nivå.

Det är bara toppen av isberget. Kolla in [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – ett öppet bibliotek med prompts kuraterat av utbildningsexperter – för att få en bredare känsla för möjligheterna! _Prova att köra några av dessa prompts i sandlådan eller med OpenAI Playground för att se vad som händer!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Vad är Prompt Engineering?

Vi började denna lektion med att definiera **Prompt Engineering** som processen att _designa och optimera_ textinput (prompter) för att leverera konsekventa och kvalitativa svar (completion) för ett givet applikationsmål och modell. Vi kan se det som en tvåstegsprocess:

- _designa_ den initiala prompten för en viss modell och mål  
- _förfina_ prompten iterativt för att förbättra svarskvaliteten

Detta är nödvändigtvis en trial-and-error-process som kräver användarintuition och ansträngning för att uppnå optimala resultat. Så varför är det viktigt? För att svara på den frågan behöver vi först förstå tre begrepp:

- _Tokenisering_ = hur modellen "ser" prompten  
- _Bas-LLMs_ = hur grundmodellen "bearbetar" en prompt  
- _Instruction-Tuned LLMs_ = hur modellen nu kan se "uppgifter"

### Tokenisering

En LLM ser prompter som en _sekvens av tokens_ där olika modeller (eller versioner av en modell) kan tokenisera samma prompt på olika sätt. Eftersom LLMs tränas på tokens (inte på rå text), påverkar hur prompter tokeniseras direkt kvaliteten på det genererade svaret.

För att få en intuition för hur tokenisering fungerar, prova verktyg som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) som visas nedan. Klistra in din prompt – och se hur den konverteras till tokens, med uppmärksamhet på hur mellanslagstecken och skiljetecken hanteras. Observera att detta exempel visar en äldre LLM (GPT-3) – så att testa med en nyare modell kan ge ett annat resultat.

![Tokenisering](../../../translated_images/sv/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Begrepp: Grundmodeller

När en prompt har tokeniserats är huvudfunktionen för ["Bas-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grundmodell) att förutsäga nästa token i sekvensen. Eftersom LLMs är tränade på enorma textdatasets har de god förståelse för statistiska relationer mellan tokens och kan göra den förutsägelsen med viss säkerhet. Observera att de inte förstår _meningen_ i orden i prompten eller token; de ser bara ett mönster de kan "komplettera" med sin nästa förutsägelse. De kan fortsätta förutsäga sekvensen tills de avbryts av användare eller någon förutbestämd villkor.

Vill du se hur promptbaserad completion fungerar? Mata in prompten ovan i Azure OpenAI Studios [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinställningar. Systemet är konfigurerat att behandla prompter som informationsförfrågningar – så du bör se ett svar som passar den kontexten.

Men vad händer om användaren vill se något specifikt som uppfyller ett kriterium eller uppgiftsmål? Då kommer _instruction-tuned_ LLMs in i bilden.

![Bas-LLM Chat Completion](../../../translated_images/sv/04-playground-chat-base.65b76fcfde0caa67.webp)

### Begrepp: Instruction Tuned LLMs

En [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) börjar med grundmodellen och finjusteras med exempel eller input/output-par (t.ex. flerturs "meddelanden") som kan innehålla tydliga instruktioner – och AI:s svar försöker följa dessa instruktioner.

Det här använder tekniker som förstärkningsinlärning med mänsklig återkoppling (RLHF) som kan träna modellen att _följa instruktioner_ och _lära av återkoppling_ så att den producerar svar som är bättre anpassade till praktiska tillämpningar och mer relevanta för användarens mål.

Låt oss testa – återvänd till prompten ovan, men ändra nu _systemmeddelandet_ för att ge följande instruktion som kontext:

> _Sammanfatta innehållet du får till en elev i årskurs 2. Håll resultatet till ett stycke med 3-5 punktpunkter._

Ser du hur resultatet nu är anpassat för att spegla det önskade målet och formatet? En lärare kan nu direkt använda detta svar i sina presentationsbilder för den lektionen.

![Instruction Tuned LLM Chat Completion](../../../translated_images/sv/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Varför behöver vi Prompt Engineering?

Nu när vi vet hur prompter bearbetas av LLMs, låt oss prata om _varför_ vi behöver prompt engineering. Svaret ligger i att dagens LLMs har ett antal utmaningar som gör det svårt att uppnå _pålita och konsekventa svar_ utan att lägga möda på promptkonstruktion och optimering. Till exempel:

1. **Modellens svar är stokastiska.** _Samma prompt_ kommer sannolikt att ge olika svar med olika modeller eller modellversioner. Och den kan till och med ge olika resultat med _samma modell_ vid olika tillfällen. _Prompt engineering-tekniker kan hjälpa oss att minimera dessa variationer genom bättre styrning_.

1. **Modeller kan hitta på svar.** Modeller är förtränade på _stora men begränsade_ datasets, vilket innebär att de saknar kunskap om begrepp utanför träningsområdet. Som en följd kan de leverera svar som är felaktiga, påhittade eller direkt motsägs av kända fakta. _Prompt engineering-tekniker hjälper användare att identifiera och hantera sådana påhitt, t.ex. genom att be AI om källhänvisningar eller resonemang_.

1. **Modellernas kapacitet varierar.** Nyare modeller eller modellevanter ger rikare kapaciteter men medför också unika egenheter och kompromisser i kostnad och komplexitet. _Prompt engineering kan hjälpa oss utveckla bästa praxis och arbetsflöden som abstraherar skillnader och anpassar sig till modell-specifika krav på skalbara, sömlösa sätt_.

Låt oss se detta i praktiken i OpenAI eller Azure OpenAI Playground:

- Använd samma prompt med olika LLM-utplaceringar (t.ex. OpenAI, Azure OpenAI, Hugging Face) – såg du variationerna?  
- Använd samma prompt upprepade gånger med _samma_ LLM-utplacering (t.ex. Azure OpenAI Playground) – hur skiljde sig variationerna?

### Exempel på påhitt

I denna kurs använder vi termen **"påhitt"** för att referera till fenomenet där LLMs ibland genererar faktamässigt felaktig information på grund av begränsningar i deras träning eller andra faktorer. Du kan också ha hört detta kallas _"hallucinationer"_ i populärvetenskapliga artiklar eller forskningspapper. Vi rekommenderar dock starkt att använda _"påhitt"_ som term för att undvika att antropomorfisera beteendet genom att tillskriva en mänsklig egenskap till en maskindriven utgång. Detta stärker också [ansvarsfull AI:s riktlinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ur ett terminologiperspektiv genom att ta bort termer som kan anses stötande eller icke-inkluderande i vissa sammanhang.

Vill du få en känsla för hur påhitt fungerar? Tänk dig en prompt som instruerar AI att generera innehåll för ett icke-existerande ämne (för att säkerställa att det inte finns i träningsdatan). Till exempel – jag testade denna prompt:

> **Prompt:** generera en lektionsplan om Marskriget 2076.


En webbsökning visade mig att det fanns fiktiva berättelser (t.ex. TV-serier eller böcker) om marskrig – men inget år 2076. Sunt förnuft säger också att 2076 är _i framtiden_ och därmed inte kan kopplas till en verklig händelse.

Så vad händer när vi kör denna prompt med olika LLM-leverantörer?

> **Svar 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/sv/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/sv/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/sv/04-fabrication-huggingchat.faf82a0a51278956.webp)

Som förväntat producerar varje modell (eller modellversion) något olika svar tack vare stokastiskt beteende och variationer i modellens kapacitet. Till exempel riktar sig en modell till en målgrupp på åttonde klass medan en annan antar en gymnasieelev. Men alla tre modeller genererade svar som skulle kunna övertyga en oinformerad användare om att händelsen var verklig.

Prompttekniker som _metaprompting_ och _temperaturkonfiguration_ kan minska modellfabriceringar till viss del. Nya promptteknik _arkitekturer_ integrerar dessutom nya verktyg och tekniker sömlöst i promptflödet för att mildra eller reducera några av dessa effekter.

## Fallstudie: GitHub Copilot

Vi avslutar denna sektion med att ge en inblick i hur promptteknik används i verkliga lösningar genom att titta på en fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot är din "AI-parprogrammerare" – den omvandlar textpromptar till kodkompletteringar och är integrerad i din utvecklingsmiljö (t.ex. Visual Studio Code) för en sömlös användarupplevelse. Som dokumenterat i serien av blogginlägg nedan baserades den tidigaste versionen på OpenAI Codex-modellen – där ingenjörer snabbt insåg behovet av att finjustera modellen och utveckla bättre prompttekniker för att förbättra kodkvaliteten. I juli [lanserade de en förbättrad AI-modell som går bortom Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) för ännu snabbare förslag.

Läs inläggen i ordning för att följa deras lärandeprocess.

- **Maj 2023** | [GitHub Copilot blir bättre på att förstå din kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inside GitHub: Att arbeta med LLMs bakom GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Hur man skriver bättre prompts för GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot går bortom Codex med förbättrad AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En utvecklares guide till prompt engineering och LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hur man bygger en företags-LLM-app: Lärdomar från GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan också bläddra i deras [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) för fler inlägg som [det här](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som visar hur dessa modeller och tekniker _tillämpas_ för att driva verkliga applikationer.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Konstruktion av prompt

Vi har sett varför promptteknik är viktigt – nu ska vi förstå hur promptar _konstrueras_ så att vi kan utvärdera olika tekniker för mer effektiv promptdesign.

### Bas-prompt

Låt oss börja med basprompten: en textinmatning som skickas till modellen utan annan kontext. Här är ett exempel – när vi skickar de första orden i USAs nationalsång till OpenAI:s [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) fullbordar den direkt svaret med de följande raderna, vilket illustrerar det grundläggande prediktiva beteendet.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det låter som att du börjar sjunga texten till "The Star-Spangled Banner", USA:s nationalsång. Den fullständiga texten är ... |

### Komplex prompt

Nu lägger vi till kontext och instruktioner till den basala prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) låter oss konstruera en komplex prompt som en samling av _meddelanden_ med:

- In-/utmatningspar som speglar _användarens_ input och _assistentens_ svar.
- Systemmeddelande som sätter kontexten för assistentens beteende eller personlighet.

Begäran har nu formen nedan, där _tokeniseringen_ effektivt fångar relevant information från kontext och konversation. Att ändra systemkontexten kan nu vara lika avgörande för kvaliteten på svaren som de givna användaringångarna.

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

I exemplen ovan var användarprompten en enkel textfråga som kan tolkas som en förfrågan om information. Med _instruktionspromptar_ kan vi använda den texten för att specificera en uppgift mer i detalj, och på så vis ge AI:n bättre vägledning. Här är ett exempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruktions-typ    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returnerade ett enkelt stycke_                                                                                           | Enkel               |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returnerade ett stycke följt av en lista med nyckeldatum och beskrivningar av viktiga händelser_                           | Komplex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returnerar mer utförliga detaljer i en textruta, formatterad som JSON som du kan kopiera-klistra in i en fil och validera vid behov_ | Komplex. Formaterad.|

## Primärt innehåll

I exemplen ovan var prompten fortfarande ganska öppen, vilket tillät LLM att själv avgöra vilken del av dess förtränade datamängd som var relevant. Med designmönstret _primärt innehåll_ delas inmatningstexten upp i två delar:

- en instruktion (åtgärd)
- relevant innehåll (som påverkar åtgärden)

Här är ett exempel där instruktionen är att "sammanfatta detta i 2 meningar".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger så mycket som alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusaste objekten synliga för blotta ögat på natthimlen och har varit känd av forntida civilisationer sedan innan historien skrevs. Den är uppkallad efter den romerska guden Jupiter.[19] När man tittar från jorden kan Jupiter vara så ljus att dess reflekterade ljus kan kasta synliga skuggor,[20] och är i genomsnitt det tredje ljusaste naturliga objektet på natthimlen efter månen och Venus. <br/> **Sammanfatta detta i 2 korta meningar** | Jupiter, den femte planeten från solen, är den största i solsystemet och är känd för att vara ett av de ljusaste objekten på natthimlen. Den är uppkallad efter den romerska guden Jupiter och är en gasjätte med en massa som är två och en halv gånger större än alla andra planeter i solsystemet tillsammans. |

Det primära innehållsavsnittet kan användas på olika sätt för att driva mer effektiva instruktioner:

- **Exempel** – istället för att tala om för modellen vad den ska göra genom en explicit instruktion, ge den exempel på vad som ska göras och låt den härleda mönstret.
- **Signaler** – följ instruktionen med en "signal" som förbereder svaret och styr modellen mot mer relevanta svar.
- **Mallarna** – dessa är upprepningsbara "recept" för promptar med platshållare (variabler) som kan anpassas med data för specifika användningsfall.

Låt oss utforska dessa i praktiken.

### Använda exempel

Detta är en metod där du använder det primära innehållet för att "mata modellen" med exempel på önskat utdata för en given instruktion, och låter den härleda mönstret för önskat utdata. Baserat på antalet givna exempel kan vi ha nollskotts-promptning, enskotts-promptning, få-skottspromptning och så vidare.

Prompten består nu av tre komponenter:

- En uppgiftsbeskrivning
- Några exempel på önskat utdata
- Början på ett nytt exempel (som blir en implicit uppgiftsbeskrivning)

| Lärandetyp | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Nollskott  | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| Enskott    | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Få-skott   | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basket                      |
|            |                                                                                                                                                       |                             |

Lägg märke till hur vi behövde ge en explicit instruktion ("Translate to Spanish") vid nollskotts-prompt, men den härleds i enskotts-prompt-exemplet. Få-skott-exemplet visar hur fler exempel tillåter modeller att göra mer noggranna antaganden utan ytterligare instruktioner.

### Promptsignaler

En annan teknik för att använda primärt innehåll är att ge _signaler_ istället för exempel. I det här fallet ger vi modellen en knuff i rätt riktning genom att _starta med_ ett utdrag som speglar önskat svarsformat. Modellen "tar signalen" och fortsätter i samma stil.

| Antal signaler | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger så mycket som alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusaste objekten synliga för blotta ögat på natthimlen och har varit känd av forntida civilisationer sedan innan historien skrevs. <br/>**Sammanfatta detta**                                       | Jupiter är den största planeten i vårt solsystem och den femte från solen. Det är en gasjätte med en massa som är 1/1000 av solens, men tyngre än alla andra planeter tillsammans. Forntida civilisationer har känt till Jupiter länge, och den är lätt synlig på natthimlen. |
| 1              | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger större än alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusstarkaste objekten som är synliga för blotta ögat på natthimlen och har varit känt för forntida civilisationer sedan innan skriftlig historia. <br/>**Sammanfatta detta** <br/> Vad vi lärde oss är att Jupiter | är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger större än alla andra planeter tillsammans. Den är lätt synlig för blotta ögat och har varit känd sedan antiken.                        |
| 2              | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger större än alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusstarkaste objekten som är synliga för blotta ögat på natthimlen och har varit känt för forntida civilisationer sedan innan skriftlig historia. <br/>**Sammanfatta detta** <br/> Topp 3 fakta vi lärde oss:         | 1. Jupiter är den femte planeten från solen och den största i solsystemet. <br/> 2. Det är en gasjätte med en massa som är en tusendel av solens...<br/> 3. Jupiter har varit synlig för blotta ögat sedan antiken ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

En promptmall är ett _fördefinierat recept för en prompt_ som kan sparas och återanvändas vid behov för att skapa mer konsekventa användarupplevelser i stor skala. I sin enklaste form är det helt enkelt en samling av prompexempel som [det här från OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) som både innehåller de interaktiva promptskomponenterna (användar- och systemmeddelanden) och API-drivna förfrågningsformat - för att stödja återanvändning.

I dess mer komplexa form som [det här exemplet från LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) innehåller den _platshållare_ som kan ersättas med data från olika källor (användarinput, systemkontext, externa datakällor med mera) för att generera en prompt dynamiskt. Detta gör det möjligt för oss att skapa ett bibliotek med återanvändbara prompts som kan användas för att driva konsekventa användarupplevelser **programmeringsmässigt** i stor skala.

Slutligen ligger det verkliga värdet av mallar i möjligheten att skapa och publicera _promptbibliotek_ för vertikala applikationsdomäner – där promptmallen nu är _optimerad_ för att spegla applikationsspecifik kontext eller exempel som gör svaren mer relevanta och korrekta för den målgrupp användaren tillhör. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)-arkivet är ett utmärkt exempel på detta tillvägagångssätt, där ett bibliotek av prompts för utbildningsdomänen samlats med fokus på viktiga mål som lektionsplanering, kursdesign, studenthandledning med mera.

## Supporting Content

Om vi tänker på promptkonstruktion som att ha en instruktion (uppgift) och ett mål (primärt innehåll), då är _sekundärt innehåll_ som ytterligare kontext vi ger för att **påverka utdata på något sätt**. Det kan vara justeringsparametrar, formateringsinstruktioner, ämnestaxonomier med mera som kan hjälpa modellen att _anpassa_ sitt svar för att passa de önskade användarmålen eller förväntningarna.

Till exempel: Givet en kurskatalog med omfattande metadata (namn, beskrivning, nivå, metadatataggar, instruktör med mera) för alla tillgängliga kurser i läroplanen:

- vi kan definiera en instruktion för att "sammanfatta kurskatalogen för hösten 2023"
- vi kan använda primärt innehåll för att tillhandahålla några exempel på önskat resultat
- vi kan använda sekundärt innehåll för att identifiera de 5 mest intressanta "taggarna".

Nu kan modellen ge en sammanfattning i det format som visas av exemplen – men om ett resultat har flera taggar kan den prioritera de 5 taggar som identifierats i det sekundära innehållet.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Prompting Best Practices

Nu när vi vet hur prompts kan _konstrueras_, kan vi börja tänka på hur vi _designar_ dem för att spegla bästa praxis. Vi kan tänka på detta i två delar – att ha rätt _inställning_ och att tillämpa rätt _tekniker_.

### Prompt Engineering Mindset

Prompt Engineering är en process med försök och misstag, så håll tre breda vägledande faktorer i åtanke:

1. **Domänförståelse är viktig.** Svarsnoggrannhet och relevans är en funktion av den _domän_ som applikationen eller användaren verkar inom. Använd din intuition och domänexpertis för att **anpassa tekniker** ytterligare. Definiera till exempel _domänspecifika personligheter_ i dina systemprompts, eller använd _domänspecifika mallar_ i dina användarprompts. Tillhandahåll sekundärt innehåll som speglar domänspecifik kontext, eller använd _domänspecifika signaler och exempel_ för att vägleda modellen mot välbekanta användningsmönster.

2. **Modellförståelse är viktig.** Vi vet att modeller är stokastiska till sin natur. Men modellimplementationer kan också skilja sig åt när det gäller vilken träningsdata de använder (förtränad kunskap), vilka funktioner de erbjuder (t.ex. via API eller SDK) och vilken typ av innehåll de är optimerade för (t.ex. kod kontra bilder kontra text). Förstå styrkor och begränsningar i den modell du använder, och använd den kunskapen för att _prioritera uppgifter_ eller bygga _anpassade mallar_ som är optimerade för modellens kapabiliteter.

3. **Iteration & validering är viktiga.** Modeller utvecklas snabbt, liksom teknikerna för prompt engineering. Som domänexpert kanske du har annan kontext eller kriterier för _din_ specifika applikation som inte gäller för den bredare gemenskapen. Använd verktyg och tekniker för prompt engineering för att "kickstarta" promptkonstruktionen, iterera sedan och validera resultaten med din egen intuition och domänexpertis. Dokumentera dina insikter och skapa en **kunskapsbas** (t.ex. promptbibliotek) som kan användas som en ny baslinje av andra för snabbare iterationer i framtiden.

## Best Practices

Nu tittar vi på vanliga bästa praxis som rekommenderas av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) och [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktiker.

| Vad                                | Varför                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Utvärdera de senaste modellerna.   | Nya modellgenerationer har sannolikt förbättrade funktioner och kvalitet – men kan också medföra högre kostnader. Utvärdera deras påverkan och fatta migreringsbeslut.                                                                             |
| Separera instruktioner & kontext   | Kontrollera om din modell/leverantör definierar _avgränsare_ för att tydligare skilja instruktioner, primärt och sekundärt innehåll. Detta kan hjälpa modeller att tilldela vikt mer exakt på tokens.                                               |
| Var specifik och tydlig             | Ge mer detaljer om önskad kontext, resultat, längd, format, stil med mera. Detta förbättrar både kvalitet och konsekvens i svaren. Fånga upp recept i återanvändbara mallar.                                                                       |
| Var beskrivande, använd exempel     | Modeller kan svara bättre på ett "visa och berätta"-sätt. Börja med en `zero-shot`-metod där du ger en instruktion (men inga exempel) och prova sedan `few-shot` som förfining genom att tillhandahålla några exempel på önskat utdata. Använd analogier. |
| Använd signaler för att kickstarta  | Styr den mot ett önskat resultat genom att ge den inledande ord eller fraser som den kan använda som utgångspunkt för svaret.                                                                                                                     |
| Upprepa vid behov                   | Ibland behöver du upprepa dig för modellen. Ge instruktioner före och efter ditt primära innehåll, använd både instruktion och signal, med mera. Iterera och validera för att se vad som fungerar.                                               |
| Ordningen spelar roll               | I vilken ordning du presenterar information för modellen kan påverka resultatet, även i lärandeexempel, tack vare nyhetsbias. Prova olika alternativ för att se vad som fungerar bäst.                                                             |
| Ge modellen en "utväg"              | Ge modellen ett _fallback_-svar den kan använda om den inte kan slutföra uppgiften av någon anledning. Detta kan minska risken att modellen genererar felaktiga eller fabricerade svar.                                                            |
|                                   |                                                                                                                                                                                                                                                   |

Som med alla bästa praxis, kom ihåg att _din erfarenhet kan variera_ baserat på modell, uppgift och domän. Använd dessa som en startpunkt och iterera för att hitta vad som fungerar bäst för dig. Utvärdera kontinuerligt din prompt engineering-process allteftersom nya modeller och verktyg blir tillgängliga, med fokus på processens skalbarhet och svarskvalitet.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Uppgift

Grattis! Du har kommit till slutet av lektionen! Det är dags att testa några av de koncept och tekniker med riktiga exempel!

För vår uppgift kommer vi att använda en Jupyter Notebook med övningar som du kan genomföra interaktivt. Du kan också utöka Notebook med egna Markdown- och kodceller för att utforska idéer och tekniker på egen hand.

### För att komma igång, fork:a repot, sedan

- (Rekommenderas) Starta GitHub Codespaces
- (Alternativt) Klona repot till din lokala enhet och använd det med Docker Desktop
- (Alternativt) Öppna Notebooken i din föredragna Notebook-miljö.

### Nästa steg, konfigurera dina miljövariabler

- Kopiera filen `.env.copy` i repots rot till `.env` och fyll i värdena för `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` och `AZURE_OPENAI_DEPLOYMENT`. Kom tillbaka till [Learning Sandbox-sektionen](#lär-sandlåda) för att lära dig hur.

### Därefter, öppna Jupyter Notebook

- Välj runtimemiljö. Om du använder alternativ 1 eller 2, välj helt enkelt standard Python 3.10.x-kärnan som tillhandahålls av utvecklingscontainern.

Du är nu redo att köra övningarna. Observera att det här inte finns några _rätt eller fel_ svar här – det handlar bara om att utforska alternativ genom försök och misstag och utveckla intuition för vad som fungerar för en given modell och applikationsdomän.

_För denna anledning finns inga kodlösningar i den här lektionen. Istället kommer Notebooken att ha Markdown-celler med titeln "Min lösning:" som visar ett exempel på output för referens._

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Kunskapskontroll

Vilken av följande är en bra prompt som följer några rimliga bästa praxis?

1. Visa mig en bild på en röd bil
2. Visa mig en bild på en röd bil av märket Volvo och modellen XC90 parkerad vid en klippa med solnedgång
3. Visa mig en bild på en röd bil av märket Volvo och modellen XC90

Svar: 2, det är den bästa prompten eftersom den ger detaljer om "vad" och går in på specifika detaljer (inte bara någon bil utan en viss märkes- och modell), och den beskriver även hela miljön. 3 är näst bäst eftersom den också innehåller mycket beskrivning.

## 🚀 Utmaning

Se om du kan använda "cue"-tekniken med prompten: Slutför meningen "Visa mig en bild på en röd bil av märket Volvo och ". Vad svarar den med, och hur skulle du förbättra den?

## Bra jobbat! Fortsätt din lärresa

Vill du lära dig mer om olika koncept inom prompt engineering? Gå till [fortsättningssidan för lärande](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att hitta andra utmärkta resurser om detta ämne.

Gå vidare till Lektion 5 där vi tittar på [avancerade prompttekniker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->