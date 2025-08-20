<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-07-09T10:21:45+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sv"
}
-->
# Grundläggande om Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.sv.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introduktion  
Den här modulen täcker viktiga begrepp och tekniker för att skapa effektiva prompts i generativa AI-modeller. Hur du formulerar din prompt till en LLM spelar också roll. En noggrant utformad prompt kan ge bättre svarskvalitet. Men vad betyder egentligen termer som _prompt_ och _prompt engineering_? Och hur förbättrar jag prompt-_inputen_ som jag skickar till LLM? Det är de frågor vi ska försöka besvara i detta kapitel och nästa.

_Generativ AI_ kan skapa nytt innehåll (t.ex. text, bilder, ljud, kod osv.) som svar på användarförfrågningar. Det görs med hjälp av _Large Language Models_ som OpenAI:s GPT ("Generative Pre-trained Transformer")-serie, som är tränade för att använda naturligt språk och kod.

Användare kan nu interagera med dessa modeller via välbekanta gränssnitt som chatt, utan att behöva teknisk expertis eller utbildning. Modellerna är _prompt-baserade_ – användare skickar in en textinput (prompt) och får tillbaka AI:s svar (completion). De kan sedan "chatta med AI:n" iterativt, i flerstegs-konversationer, och förfina sin prompt tills svaret motsvarar deras förväntningar.

"Prompts" blir nu det primära _programmeringsgränssnittet_ för generativa AI-appar, som talar om för modellerna vad de ska göra och påverkar kvaliteten på de svar som returneras. "Prompt Engineering" är ett snabbt växande forskningsområde som fokuserar på _design och optimering_ av prompts för att leverera konsekventa och kvalitativa svar i stor skala.

## Lärandemål

I denna lektion lär vi oss vad Prompt Engineering är, varför det är viktigt och hur vi kan skapa mer effektiva prompts för en given modell och applikationsmål. Vi kommer att förstå kärnbegrepp och bästa praxis för prompt engineering – och lära oss om en interaktiv Jupyter Notebook-"sandbox" där vi kan se dessa koncept tillämpas på verkliga exempel.

I slutet av lektionen ska vi kunna:

1. Förklara vad prompt engineering är och varför det är viktigt.  
2. Beskriva komponenterna i en prompt och hur de används.  
3. Lära oss bästa praxis och tekniker för prompt engineering.  
4. Tillämpa inlärda tekniker på verkliga exempel, med hjälp av en OpenAI-endpoint.

## Nyckelbegrepp

Prompt Engineering: Praktiken att designa och förfina input för att styra AI-modeller mot att producera önskade resultat.  
Tokenisering: Processen att omvandla text till mindre enheter, kallade tokens, som en modell kan förstå och bearbeta.  
Instruction-Tuned LLMs: Stora språkmodeller (LLMs) som finjusterats med specifika instruktioner för att förbättra svarens noggrannhet och relevans.

## Lärande Sandbox

Prompt engineering är för närvarande mer en konst än en exakt vetenskap. Det bästa sättet att förbättra vår intuition är att _övning ger färdighet_ och att använda en trial-and-error-metod som kombinerar domänkunskap med rekommenderade tekniker och modell-specifika optimeringar.

Jupyter Notebook som följer med denna lektion erbjuder en _sandbox_-miljö där du kan prova det du lär dig – löpande eller som en del av kodutmaningen i slutet. För att köra övningarna behöver du:

1. **En Azure OpenAI API-nyckel** – tjänstens endpoint för en distribuerad LLM.  
2. **En Python-runtime** – där Notebook kan köras.  
3. **Lokala miljövariabler** – _slutför [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) stegen nu för att vara redo_.

Notebooken innehåller _startövningar_ – men du uppmuntras att lägga till egna _Markdown_- (beskrivning) och _Code_- (promptförfrågningar) sektioner för att testa fler exempel eller idéer – och bygga din intuition för promptdesign.

## Illustrerad guide

Vill du få en överblick över vad denna lektion handlar om innan du dyker in? Kolla in denna illustrerade guide som ger dig en känsla för huvudämnena och viktiga insikter att fundera på i varje del. Lektionens färdplan tar dig från att förstå kärnbegrepp och utmaningar till att hantera dem med relevanta prompt engineering-tekniker och bästa praxis. Observera att avsnittet "Avancerade tekniker" i denna guide hänvisar till innehåll som täcks i _nästa_ kapitel i denna kurs.

![Illustrerad guide till Prompt Engineering](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.sv.png)

## Vårt startup

Nu ska vi prata om hur _detta ämne_ relaterar till vår startup-mission att [föra AI-innovation till utbildning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi vill bygga AI-drivna applikationer för _personanpassat lärande_ – så låt oss fundera på hur olika användare av vår applikation kan "designa" prompts:

- **Administratörer** kan be AI:n att _analysera läroplansdata för att identifiera luckor i täckningen_. AI:n kan sammanfatta resultaten eller visualisera dem med kod.  
- **Lärare** kan be AI:n att _generera en lektionsplan för en målgrupp och ett ämne_. AI:n kan skapa den personliga planen i ett angivet format.  
- **Studenter** kan be AI:n att _handleda dem i ett svårt ämne_. AI:n kan nu guida studenter med lektioner, tips och exempel anpassade efter deras nivå.

Det är bara toppen av isberget. Kolla in [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – ett open source-bibliotek med prompts sammanställt av utbildningsexperter – för att få en bredare bild av möjligheterna! _Testa att köra några av dessa prompts i sandboxen eller i OpenAI Playground för att se vad som händer!_

<!--  
LESSON TEMPLATE:  
This unit should cover core concept #1.  
Reinforce the concept with examples and references.  

CONCEPT #1:  
Prompt Engineering.  
Define it and explain why it is needed.  
-->

## Vad är Prompt Engineering?

Vi började denna lektion med att definiera **Prompt Engineering** som processen att _designa och optimera_ textinput (prompts) för att leverera konsekventa och kvalitativa svar (completions) för ett givet applikationsmål och modell. Vi kan se detta som en tvåstegsprocess:

- _designa_ den initiala prompten för en given modell och mål  
- _förfina_ prompten iterativt för att förbättra svarskvaliteten

Detta är nödvändigtvis en trial-and-error-process som kräver användarens intuition och ansträngning för att nå optimala resultat. Så varför är det viktigt? För att svara på det behöver vi först förstå tre begrepp:

- _Tokenisering_ = hur modellen "ser" prompten  
- _Bas-LLMs_ = hur grundmodellen "bearbetar" en prompt  
- _Instruction-Tuned LLMs_ = hur modellen nu kan tolka "uppgifter"

### Tokenisering

En LLM ser prompts som en _sekvens av tokens_ där olika modeller (eller versioner av en modell) kan tokenisera samma prompt på olika sätt. Eftersom LLMs tränas på tokens (och inte råtext) påverkar hur prompten tokeniseras direkt kvaliteten på det genererade svaret.

För att få en känsla för hur tokenisering fungerar, prova verktyg som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) som visas nedan. Klistra in din prompt – och se hur den omvandlas till tokens, med fokus på hur mellanslag och skiljetecken hanteras. Observera att detta exempel visar en äldre LLM (GPT-3) – så att testa med en nyare modell kan ge ett annat resultat.

![Tokenisering](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.sv.png)

### Begrepp: Grundmodeller

När en prompt är tokeniserad är huvudfunktionen för ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grundmodellen) att förutsäga nästa token i sekvensen. Eftersom LLMs tränas på enorma textdatamängder har de god förståelse för statistiska samband mellan tokens och kan göra denna förutsägelse med viss säkerhet. Observera att de inte förstår _innebörden_ av orden i prompten eller token; de ser bara ett mönster som de kan "komplettera" med sin nästa förutsägelse. De kan fortsätta förutsäga sekvensen tills användaren avbryter eller någon förutbestämd villkor uppfylls.

Vill du se hur prompt-baserad completion fungerar? Skriv in prompten ovan i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinställningarna. Systemet är konfigurerat att behandla prompts som informationsförfrågningar – så du bör se ett svar som passar detta sammanhang.

Men vad händer om användaren vill ha något specifikt som uppfyller vissa kriterier eller mål? Här kommer _instruction-tuned_ LLMs in i bilden.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.sv.png)

### Begrepp: Instruction Tuned LLMs

En [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bygger på grundmodellen och finjusteras med exempel eller input/output-par (t.ex. flerstegs-"meddelanden") som kan innehålla tydliga instruktioner – och AI:s svar försöker följa dessa instruktioner.

Detta använder tekniker som Reinforcement Learning with Human Feedback (RLHF) som kan träna modellen att _följa instruktioner_ och _lära sig av feedback_ så att den producerar svar som är bättre anpassade för praktiska tillämpningar och mer relevanta för användarens mål.

Låt oss prova – gå tillbaka till prompten ovan, men ändra nu _systemmeddelandet_ för att ge följande instruktion som kontext:

> _Sammanfatta innehållet du får för en elev i årskurs 2. Håll resultatet till ett stycke med 3-5 punkter._

Ser du hur resultatet nu är anpassat för att spegla det önskade målet och formatet? En lärare kan nu direkt använda detta svar i sina presentationer för den klassen.

![Instruction Tuned LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.sv.png)

## Varför behöver vi Prompt Engineering?

Nu när vi vet hur prompts bearbetas av LLMs, låt oss prata om _varför_ vi behöver prompt engineering. Svaret ligger i att dagens LLMs har flera utmaningar som gör det svårare att uppnå _pålitliga och konsekventa svar_ utan att lägga ner arbete på promptkonstruktion och optimering. Till exempel:

1. **Modellens svar är stokastiska.** _Samma prompt_ kan ge olika svar med olika modeller eller modellversioner. Och det kan till och med ge olika resultat med _samma modell_ vid olika tillfällen. _Prompt engineering-tekniker kan hjälpa oss att minimera dessa variationer genom att ge bättre styrning_.

1. **Modeller kan hitta på svar.** Modeller är förtränade på _stora men begränsade_ dataset, vilket innebär att de saknar kunskap om koncept utanför träningsmaterialet. Som en följd kan de generera svar som är felaktiga, påhittade eller direkt motsäger kända fakta. _Prompt engineering hjälper användare att identifiera och minska sådana påhitt, t.ex. genom att be AI:n om källhänvisningar eller resonemang_.

1. **Modellernas kapacitet varierar.** Nyare modeller eller modellgenerationer har rikare kapaciteter men medför också unika egenheter och kompromisser i kostnad och komplexitet. _Prompt engineering kan hjälpa oss att utveckla bästa praxis och arbetsflöden som döljer skillnader och anpassar sig till modell-specifika krav på ett skalbart och smidigt sätt_.

Låt oss se detta i praktiken i OpenAI eller Azure OpenAI Playground:

- Använd samma prompt med olika LLM-distributioner (t.ex. OpenAI, Azure OpenAI, Hugging Face) – såg du variationerna?  
- Använd samma prompt upprepade gånger med _samma_ LLM-distribution (t.ex. Azure OpenAI playground) – hur skiljde sig dessa variationer?

### Exempel på påhittade svar

I denna kurs använder vi termen **"fabrication"** för att beskriva fenomenet där LLMs ibland genererar faktamässigt felaktig information på grund av begränsningar i deras träning eller andra faktorer. Du har kanske också hört detta kallat _"hallucinationer"_ i populära artiklar eller forskningsrapporter. Vi rekommenderar dock starkt att använda _"fabrication"_ som term för att undvika att antropomorfisera beteendet genom att tillskriva en mänsklig egenskap till ett maskindrivet resultat. Detta stärker också [Responsible AI-riktlinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ur ett terminologiskt perspektiv, genom att ta bort termer som kan uppfattas som stötande eller icke-inkluderande i vissa sammanhang.

Vill du få en känsla för hur fabrications fungerar? Tänk på en prompt som instruerar AI:n att generera innehåll för ett icke-existerande ämne (för att säkerställa att det inte finns i träningsdata). Till exempel – jag testade denna prompt:
# Lektionplan: Marskriget 2076

## Översikt
I denna lektion kommer vi att utforska Marskriget som ägde rum år 2076. Vi kommer att undersöka orsakerna till konflikten, de viktigaste händelserna under kriget, samt dess konsekvenser för mänskligheten och rymdforskningen.

## Mål
- Förstå bakgrunden till Marskriget 2076
- Identifiera de viktigaste aktörerna och händelserna
- Analysera krigets påverkan på samhället och teknologin
- Diskutera lärdomar från konflikten

## Material
- Textdokument om Marskriget 2076
- Kartor över Mars och jordens kolonier
- Videoklipp med intervjuer från överlevande och experter
- Diskussionfrågor

## Lektionens gång

### 1. Introduktion (10 minuter)
- Kort presentation av Marskriget 2076
- Visa en tidslinje över viktiga händelser
- Diskutera varför konflikten uppstod

### 2. Bakgrund och orsaker (15 minuter)
- Gå igenom de politiska och ekonomiska faktorerna
- Beskriv de olika grupperna och deras mål
- Analysera resursbrist och territoriella tvister

### 3. Viktiga händelser under kriget (20 minuter)
- Beskriv de största slagen och strategierna
- Diskutera teknologiska innovationer som användes
- Visa kartor för att illustrera rörelser och kontrollområden

### 4. Konsekvenser och efterspel (15 minuter)
- Analysera krigets påverkan på Mars och jorden
- Diskutera förändringar i internationell politik och rymdlagstiftning
- Reflektera över hur kriget påverkade framtida rymdexpeditioner

### 5. Diskussion och reflektion (10 minuter)
- Ställ frågor till eleverna om vad de lärt sig
- Diskutera möjliga alternativa utfall
- Uppmuntra eleverna att tänka på hur konflikter kan undvikas i framtiden

## Uppgifter
- Skriv en kort uppsats om en viktig händelse under Marskriget 2076
- Skapa en presentation om en av de teknologier som utvecklades under kriget
- Delta i en debatt om krigets rättfärdigande och konsekvenser

## Bedömning
- Aktivt deltagande i diskussioner
- Kvalitet på skriftliga uppgifter och presentationer
- Förmåga att analysera och reflektera över historiska händelser

## Kommentarer
- Anpassa materialet efter elevernas förkunskaper
- Använd visuella hjälpmedel för att öka förståelsen
- Uppmuntra kritiskt tänkande och källkritik under hela lektionen
En webbsökning visade att det fanns fiktiva berättelser (t.ex. TV-serier eller böcker) om marskrig – men inga från 2076. Sunt förnuft säger också att 2076 är _i framtiden_ och därför inte kan kopplas till en verklig händelse.

Så vad händer när vi kör denna prompt med olika LLM-leverantörer?

> **Svar 1**: OpenAI Playground (GPT-35)

![Svar 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.sv.png)

> **Svar 2**: Azure OpenAI Playground (GPT-35)

![Svar 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.sv.png)

> **Svar 3**: : Hugging Face Chat Playground (LLama-2)

![Svar 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.sv.png)

Som väntat ger varje modell (eller modellversion) något olika svar tack vare stokastiskt beteende och variationer i modellens kapacitet. Till exempel riktar sig en modell till en åttondeklassare medan en annan antar att användaren är gymnasieelev. Men alla tre modeller genererade svar som skulle kunna övertyga en oinformerad användare om att händelsen var verklig.

Prompttekniker som _metaprompting_ och _temperaturinställning_ kan till viss del minska modellens fabriceringar. Nya prompttekniska _arkitekturer_ integrerar också nya verktyg och metoder sömlöst i promptflödet för att mildra eller minska några av dessa effekter.

## Fallstudie: GitHub Copilot

Låt oss avsluta detta avsnitt med att få en känsla för hur promptteknik används i verkliga lösningar genom att titta på en fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot är din "AI-parprogrammerare" – den omvandlar textpromptar till kodkompletteringar och är integrerad i din utvecklingsmiljö (t.ex. Visual Studio Code) för en sömlös användarupplevelse. Som dokumenterat i bloggsserien nedan baserades den tidigaste versionen på OpenAI Codex-modellen – där ingenjörer snabbt insåg behovet av att finjustera modellen och utveckla bättre prompttekniker för att förbättra kodkvaliteten. I juli [lanserade de en förbättrad AI-modell som går bortom Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) för ännu snabbare förslag.

Läs inläggen i ordning för att följa deras läranderesa.

- **Maj 2023** | [GitHub Copilot blir bättre på att förstå din kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inside GitHub: Att arbeta med LLM:erna bakom GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jun 2023** | [Hur man skriver bättre prompts för GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [.. GitHub Copilot går bortom Codex med förbättrad AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En utvecklares guide till promptteknik och LLM:er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hur man bygger en företags-LLM-app: Lärdomar från GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan också bläddra i deras [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) för fler inlägg som [det här](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som visar hur dessa modeller och tekniker _tillämpas_ för att driva verkliga applikationer.

---

<!--
LESSON TEMPLATE:
Denna enhet bör täcka kärnkoncept #2.
Förstärk konceptet med exempel och referenser.

KONCEPT #2:
Promptdesign.
Illustrerat med exempel.
-->

## Promptkonstruktion

Vi har sett varför promptteknik är viktigt – nu ska vi förstå hur prompts _konstrueras_ så att vi kan utvärdera olika tekniker för mer effektiv promptdesign.

### Grundläggande prompt

Låt oss börja med den grundläggande prompten: en textinmatning som skickas till modellen utan annan kontext. Här är ett exempel – när vi skickar de första orden i USA:s nationalsång till OpenAI:s [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) fullbordar den omedelbart svaret med de följande raderna, vilket illustrerar det grundläggande prediktionsbeteendet.

| Prompt (Inmatning)     | Komplettering (Utmatning)                                                                                                                        |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see      | Det låter som att du börjar med texten till "The Star-Spangled Banner", USA:s nationalsång. Den fullständiga texten är ...                      |

### Komplex prompt

Nu lägger vi till kontext och instruktioner till den grundläggande prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) låter oss bygga en komplex prompt som en samling _meddelanden_ med:

- Inmatning/utmatningspar som speglar _användarens_ input och _assistentens_ svar.
- Systemmeddelande som sätter kontext för assistentens beteende eller personlighet.

Förfrågan ser nu ut som nedan, där _tokeniseringen_ effektivt fångar relevant information från kontext och konversation. Att ändra systemkontexten kan nu påverka kvaliteten på kompletteringarna lika mycket som användarens inmatningar.

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

I exemplen ovan var användarprompten en enkel textfråga som kan tolkas som en informationsförfrågan. Med _instruktionsprompter_ kan vi använda texten för att specificera en uppgift mer detaljerat och ge AI:n bättre vägledning. Här är ett exempel:

| Prompt (Inmatning)                                                                                                                                                                                                                         | Komplettering (Utmatning)                                                                                                        | Instruktionstyp     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returnerade ett enkelt stycke_                                                                                                 | Enkel              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returnerade ett stycke följt av en lista med viktiga datum och beskrivningar_                                                  | Komplex            |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returnerar mer omfattande detaljer i en textruta, formaterad som JSON som du kan kopiera och klistra in i en fil och validera vid behov_ | Komplex. Formaterad.|

## Primärt innehåll

I exemplen ovan var prompten fortfarande ganska öppen, vilket tillät LLM att avgöra vilken del av dess förtränade dataset som var relevant. Med designmönstret _primärt innehåll_ delas inmatningstexten upp i två delar:

- en instruktion (åtgärd)
- relevant innehåll (som påverkar åtgärden)

Här är ett exempel där instruktionen är att "sammanfatta detta i 2 meningar".

| Prompt (Inmatning)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Komplettering (Utmatning)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger massan av alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusaste objekten som är synliga för blotta ögat på natthimlen och har varit känt för forntida civilisationer sedan innan historien skrevs. Den är uppkallad efter den romerska guden Jupiter.[19] När man ser Jupiter från jorden kan den vara tillräckligt ljus för att dess reflekterade ljus ska kasta synliga skuggor,[20] och är i genomsnitt det tredje ljusaste naturliga objektet på natthimlen efter månen och Venus. <br/> **Sammanfatta detta i 2 korta meningar** | Jupiter, den femte planeten från solen, är den största i solsystemet och är känd för att vara ett av de ljusaste objekten på natthimlen. Uppkallad efter den romerska guden Jupiter, är det en gasjätte vars massa är två och en halv gånger massan av alla andra planeter i solsystemet tillsammans. |

Segmentet med primärt innehåll kan användas på olika sätt för att driva mer effektiva instruktioner:

- **Exempel** – istället för att tala om för modellen vad den ska göra med en explicit instruktion, ge den exempel på vad som ska göras och låt den dra slutsatser om mönstret.
- **Ledtrådar** – följ instruktionen med en "ledtråd" som förbereder kompletteringen och styr modellen mot mer relevanta svar.
- **Mall** – detta är upprepbara 'recept' för prompts med platshållare (variabler) som kan anpassas med data för specifika användningsfall.

Låt oss utforska dessa i praktiken.

### Använda exempel

Detta är en metod där du använder det primära innehållet för att "mata modellen" med exempel på önskat resultat för en given instruktion och låter den dra slutsatser om mönstret för önskat resultat. Beroende på antalet exempel kan vi ha zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nu av tre komponenter:

- En uppgiftsbeskrivning
- Några exempel på önskat resultat
- Början på ett nytt exempel (som blir en implicit uppgiftsbeskrivning)

| Inlärningstyp | Prompt (Inmatning)                                                                                                                                        | Komplettering (Utmatning)         |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                              | "El Sol está brillando".          |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                   | "Es un día frío y ventoso".       |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk =>       | Basketball                       |
|               |                                                                                                                                                           |                                 |

Notera hur vi behövde ge en explicit instruktion ("Translate to Spanish") i zero-shot prompting, men den härleds i one-shot-exemplet. Few-shot-exemplet visar hur fler exempel gör att modeller kan göra mer exakta slutsatser utan extra instruktioner.

### Promptledtrådar

En annan teknik för att använda primärt innehåll är att ge _ledtrådar_ istället för exempel. I detta fall ger vi modellen en knuff i rätt riktning genom att _starta den_ med ett utdrag som speglar önskat svarformat. Modellen "tar ledtråden" och fortsätter i samma stil.

| Antal ledtrådar | Prompt (Inmatning)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Komplettering (Utmatning)                                                                                                                                                                                                                                                                                       |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0               | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger massan av alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusaste objekten som är synliga för blotta ögat på natthimlen, och har varit känt för forntida civilisationer sedan innan historien skrevs.

**Sammanfatta detta**                                       | Jupiter är den största planeten i vårt solsystem och den femte från solen. Det är en gasjätte med en massa som är 1/1000 av solens, men den är tyngre än alla andra planeter tillsammans. Forntida civilisationer har känt till Jupiter länge, och den är lätt synlig på natthimlen. |
| 1              | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger tyngre än alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusstarkaste objekten som är synliga för blotta ögat på natthimlen och har varit känt för forntida civilisationer långt innan historien skrevs ned. <br/>**Sammanfatta detta** <br/> Det vi lärde oss är att Jupiter | är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger tyngre än alla andra planeter tillsammans. Den är lätt synlig för blotta ögat och har varit känd sedan urminnes tider.                        |
| 2              | Jupiter är den femte planeten från solen och den största i solsystemet. Det är en gasjätte med en massa som är en tusendel av solens, men två och en halv gånger tyngre än alla andra planeter i solsystemet tillsammans. Jupiter är ett av de ljusstarkaste objekten som är synliga för blotta ögat på natthimlen och har varit känt för forntida civilisationer långt innan historien skrevs ned. <br/>**Sammanfatta detta** <br/> Topp 3 fakta vi lärde oss:         | 1. Jupiter är den femte planeten från solen och den största i solsystemet. <br/> 2. Det är en gasjätte med en massa som är en tusendel av solens...<br/> 3. Jupiter har varit synlig för blotta ögat sedan urminnes tider ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Promptmallar

En promptmall är ett _fördefinierat recept för en prompt_ som kan sparas och återanvändas vid behov för att skapa mer konsekventa användarupplevelser i stor skala. I sin enklaste form är det helt enkelt en samling promptexempel som [det här från OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) som innehåller både de interaktiva promptkomponenterna (användar- och systemmeddelanden) och API-drivna förfrågningsformatet – för att stödja återanvändning.

I en mer komplex form som [det här exemplet från LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) innehåller den _platshållare_ som kan ersättas med data från olika källor (användarinmatning, systemkontext, externa datakällor etc.) för att generera en prompt dynamiskt. Detta gör att vi kan skapa ett bibliotek av återanvändbara prompts som kan användas för att programmässigt driva konsekventa användarupplevelser i stor skala.

Slutligen ligger det verkliga värdet i mallar i möjligheten att skapa och publicera _promptbibliotek_ för vertikala applikationsdomäner – där promptmallen nu är _optimerad_ för att spegla applikationsspecifik kontext eller exempel som gör svaren mer relevanta och korrekta för den riktade användargruppen. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)-arkivet är ett utmärkt exempel på detta tillvägagångssätt, där man samlar ett bibliotek av prompts för utbildningsområdet med fokus på viktiga mål som lektionsplanering, läroplansdesign, handledning av studenter med mera.

## Stödjande innehåll

Om vi ser på promptkonstruktion som att ha en instruktion (uppgift) och ett mål (primärt innehåll), så är _sekundärt innehåll_ som ytterligare kontext vi tillhandahåller för att **påverka resultatet på något sätt**. Det kan vara justeringsparametrar, formateringsinstruktioner, ämnestaxonomier etc. som hjälper modellen att _anpassa_ sitt svar för att passa önskade användarmål eller förväntningar.

Till exempel: Givet en kurskatalog med omfattande metadata (namn, beskrivning, nivå, metadatataggar, instruktör etc.) för alla tillgängliga kurser i läroplanen:

- kan vi definiera en instruktion för att "sammanfatta kurskatalogen för hösten 2023"
- vi kan använda det primära innehållet för att ge några exempel på önskat resultat
- vi kan använda det sekundära innehållet för att identifiera de 5 viktigaste "taggarna" av intresse.

Nu kan modellen ge en sammanfattning i det format som visas av de få exemplen – men om ett resultat har flera taggar kan den prioritera de 5 taggar som identifierats i det sekundära innehållet.

---

<!--
LEKTIONSMALL:
Denna enhet bör täcka kärnkoncept #1.
Förstärk konceptet med exempel och referenser.

KONCEPT #3:
Prompt Engineering-tekniker.
Vilka är några grundläggande tekniker för prompt engineering?
Illustrera med några övningar.
-->

## Bästa praxis för prompting

Nu när vi vet hur prompts kan _konstrueras_ kan vi börja fundera på hur vi _designar_ dem för att följa bästa praxis. Vi kan se detta i två delar – att ha rätt _inställning_ och att använda rätt _tekniker_.

### Inställning för prompt engineering

Prompt Engineering är en process med försök och misstag, så håll tre breda vägledande faktorer i åtanke:

1. **Domänförståelse är viktigt.** Svarens noggrannhet och relevans beror på den _domän_ där applikationen eller användaren verkar. Använd din intuition och domänkunskap för att **anpassa teknikerna** ytterligare. Definiera till exempel _domänspecifika personligheter_ i dina systemprompter, eller använd _domänspecifika mallar_ i dina användarprompter. Ge sekundärt innehåll som speglar domänspecifika kontexter, eller använd _domänspecifika ledtrådar och exempel_ för att styra modellen mot bekanta användningsmönster.

2. **Modellförståelse är viktigt.** Vi vet att modeller är stokastiska till sin natur. Men modellimplementationer kan också skilja sig åt vad gäller träningsdata (förtränad kunskap), vilka funktioner de erbjuder (t.ex. via API eller SDK) och vilken typ av innehåll de är optimerade för (t.ex. kod vs. bilder vs. text). Förstå styrkor och begränsningar hos den modell du använder och använd den kunskapen för att _prioritera uppgifter_ eller bygga _anpassade mallar_ som är optimerade för modellens kapacitet.

3. **Iteration och validering är viktigt.** Modeller utvecklas snabbt, och det gör även teknikerna för prompt engineering. Som domänexpert kan du ha annan kontext eller kriterier för _din_ specifika applikation som kanske inte gäller för den bredare gemenskapen. Använd verktyg och tekniker för prompt engineering för att "komma igång" med promptkonstruktion, iterera sedan och validera resultaten med din egen intuition och domänkunskap. Dokumentera dina insikter och skapa en **kunskapsbas** (t.ex. promptbibliotek) som kan användas som ny baslinje av andra för snabbare iterationer i framtiden.

## Bästa praxis

Låt oss nu titta på vanliga bästa praxis som rekommenderas av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) och [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) experter.

| Vad                              | Varför                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Utvärdera de senaste modellerna. | Nya modellgenerationer har sannolikt förbättrade funktioner och kvalitet – men kan också innebära högre kostnader. Utvärdera deras påverkan och fatta sedan beslut om migrering.                                                                     |
| Separera instruktioner och kontext | Kontrollera om din modell/leverantör definierar _avgränsare_ för att tydligare skilja instruktioner, primärt och sekundärt innehåll. Detta kan hjälpa modeller att tilldela vikt mer exakt till tokens.                                            |
| Var specifik och tydlig           | Ge mer detaljer om önskad kontext, resultat, längd, format, stil etc. Detta förbättrar både kvalitet och konsekvens i svaren. Spara recept i återanvändbara mallar.                                                                                 |
| Var beskrivande, använd exempel   | Modeller kan svara bättre på en "visa och berätta"-metod. Börja med en `zero-shot`-metod där du ger en instruktion (men inga exempel) och prova sedan `few-shot` som förfining, där du ger några exempel på önskat resultat. Använd analogier.         |
| Använd ledtrådar för att starta svar | Styr modellen mot önskat resultat genom att ge några inledande ord eller fraser som den kan använda som startpunkt för svaret.                                                                                                                   |
| Upprepa vid behov                 | Ibland kan du behöva upprepa dig för modellen. Ge instruktioner före och efter ditt primära innehåll, använd en instruktion och en ledtråd etc. Iterera och validera för att se vad som fungerar.                                                    |
| Ordningen spelar roll             | I vilken ordning du presenterar information för modellen kan påverka resultatet, även i inlärningsexemplen, på grund av nyhetsbias. Prova olika alternativ för att se vad som fungerar bäst.                                                        |
| Ge modellen en “utväg”            | Ge modellen ett _fallback_-svar som den kan använda om den av någon anledning inte kan slutföra uppgiften. Detta kan minska risken för att modellen genererar falska eller påhittade svar.                                                            |
|                                 |                                                                                                                                                                                                                                                   |

Som med all bästa praxis, kom ihåg att _dina erfarenheter kan variera_ beroende på modell, uppgift och domän. Använd dessa som en utgångspunkt och iterera för att hitta vad som fungerar bäst för dig. Utvärdera kontinuerligt din prompt engineering-process när nya modeller och verktyg blir tillgängliga, med fokus på skalbarhet och svarskvalitet.

<!--
LEKTIONSMALL:
Denna enhet bör innehålla en kodutmaning om tillämpligt

UTMANING:
Länk till en Jupyter Notebook med endast kodkommentarer i instruktionerna (kodavsnitten är tomma).

LÖSNING:
Länk till en kopia av den Notebook med ifyllda prompts och körd, som visar ett exempel på resultat.
-->

## Uppgift

Grattis! Du har nått slutet av lektionen! Det är dags att testa några av de koncept och tekniker vi gått igenom med riktiga exempel!

För vår uppgift kommer vi att använda en Jupyter Notebook med övningar som du kan göra interaktivt. Du kan också utöka Notebooken med egna Markdown- och kodceller för att utforska idéer och tekniker på egen hand.

### För att komma igång, fork:a repot och sedan

- (Rekommenderat) Starta GitHub Codespaces
- (Alternativt) Klona repot till din lokala enhet och använd det med Docker Desktop
- (Alternativt) Öppna Notebooken i din föredragna Notebook-miljö.

### Nästa steg, konfigurera dina miljövariabler

- Kopiera filen `.env.copy` i repots rotmapp till `.env` och fyll i värdena för `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` och `AZURE_OPENAI_DEPLOYMENT`. Gå tillbaka till [Learning Sandbox-sektionen](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) för att lära dig hur.

### Nästa, öppna Jupyter Notebook

- Välj runtime-kärnan. Om du använder alternativ 1 eller 2, välj helt enkelt standard Python 3.10.x-kärnan som tillhandahålls av utvecklingscontainern.

Du är redo att köra övningarna. Observera att det inte finns några _rätt eller fel_ svar här – det handlar om att utforska alternativ genom försök och misstag och bygga intuition för vad som fungerar för en viss modell och applikationsdomän.

_För denna anledning finns inga kodlösningsavsnitt i denna lektion. Istället kommer Notebooken att ha Markdown-celler med titeln "Min lösning:" som visar ett exempel på output för referens._

<!--
LEKTIONSMALL:
Avsluta avsnittet med en sammanfattning och resurser för självstudier.
-->

## Kunskapskontroll

Vilken av följande är en bra prompt som följer rimliga bästa praxis?

1. Visa mig en bild på en röd bil  
2. Visa mig en bild på en röd bil av märket Volvo och modellen XC90 parkerad vid en klippa med solen som går ner  
3. Visa mig en bild på en röd bil av märket Volvo och modellen XC90

Svar: 2, det är den bästa prompten eftersom den ger detaljer om "vad" och går in på specifika detaljer (inte bara vilken bil som helst utan ett specifikt märke och modell) och den beskriver även den övergripande miljön. 3 är näst bäst eftersom den också innehåller mycket beskrivning.

## 🚀 Utmaning

Se om du kan använda "ledtråds"-tekniken med prompten: Fyll i meningen "Visa mig en bild på en röd bil av märket Volvo och ". Vad svarar den med, och hur skulle du förbättra det?

## Bra jobbat! Fortsätt din lärande

Vill du lära dig mer om olika koncept inom Prompt Engineering? Gå till [sidan för fortsatt lärande](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att hitta fler bra resurser om detta ämne.

Gå vidare till Lektion 5 där vi tittar på [avancerade prompting-tekniker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.