<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:40:01+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sv"
}
-->
# Grunderna i Prompt Engineering

## Introduktion
Detta modul täcker viktiga koncept och tekniker för att skapa effektiva prompts i generativa AI-modeller. Hur du skriver din prompt till en LLM spelar också roll. En noggrant utformad prompt kan ge en bättre svarskvalitet. Men vad betyder egentligen termer som _prompt_ och _prompt engineering_? Och hur förbättrar jag promptens _inmatning_ som jag skickar till LLM? Dessa är de frågor vi kommer att försöka besvara i detta kapitel och det nästa.

_Generativ AI_ kan skapa nytt innehåll (t.ex. text, bilder, ljud, kod etc.) som svar på användarförfrågningar. Den uppnår detta genom _Large Language Models_ som OpenAI:s GPT ("Generative Pre-trained Transformer")-serie som är tränade för att använda naturligt språk och kod.

Användare kan nu interagera med dessa modeller genom bekanta paradigmer som chatt, utan att behöva teknisk expertis eller utbildning. Modellerna är _prompt-baserade_ - användare skickar en textinmatning (prompt) och får tillbaka AI-svaret (komplettering). De kan sedan "chatta med AI" iterativt, i fleromgångskonversationer, och förfina sin prompt tills svaret matchar deras förväntningar.

"Prompts" blir nu det primära _programmeringsgränssnittet_ för generativa AI-appar, som berättar för modellerna vad de ska göra och påverkar kvaliteten på de returnerade svaren. "Prompt Engineering" är ett snabbt växande studieområde som fokuserar på _design och optimering_ av prompts för att leverera konsekventa och kvalitativa svar i stor skala.

## Lärandemål

I denna lektion lär vi oss vad Prompt Engineering är, varför det är viktigt och hur vi kan skapa mer effektiva prompts för en given modell och applikationsmål. Vi kommer att förstå kärnkoncept och bästa praxis för prompt engineering - och lära oss om en interaktiv Jupyter Notebooks "sandbox"-miljö där vi kan se dessa koncept tillämpade på verkliga exempel.

I slutet av denna lektion kommer vi att kunna:

1. Förklara vad prompt engineering är och varför det är viktigt.
2. Beskriva komponenterna i en prompt och hur de används.
3. Lära oss bästa praxis och tekniker för prompt engineering.
4. Tillämpa inlärda tekniker på verkliga exempel, med hjälp av en OpenAI-endpoint.

## Nyckeltermer

Prompt Engineering: Praktiken att designa och förfina inmatningar för att styra AI-modeller mot att producera önskade utgångar.
Tokenisering: Processen att konvertera text till mindre enheter, kallade tokens, som en modell kan förstå och bearbeta.
Instruktionsanpassade LLMs: Stora språkmodeller (LLMs) som har finjusterats med specifika instruktioner för att förbättra deras svarsnoggrannhet och relevans.

## Lärandesandbox

Prompt engineering är för närvarande mer konst än vetenskap. Det bästa sättet att förbättra vår intuition för det är att _öva mer_ och anta en trial-and-error-ansats som kombinerar expertis inom applikationsdomänen med rekommenderade tekniker och modellspecifika optimeringar.

Jupyter Notebook som följer med denna lektion ger en _sandbox_-miljö där du kan prova vad du lär dig - medan du går eller som en del av kodutmaningen i slutet. För att utföra övningarna behöver du:

1. **En Azure OpenAI API-nyckel** - tjänstens slutpunkt för en distribuerad LLM.
2. **En Python Runtime** - där Notebook kan köras.
3. **Lokala miljövariabler** - _slutför [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) stegen nu för att förbereda dig_.

Noteboken kommer med _start_-övningar - men du uppmuntras att lägga till dina egna _Markdown_ (beskrivning) och _Code_ (promptförfrågningar) sektioner för att prova fler exempel eller idéer - och bygga din intuition för promptdesign.

## Illustrerad Guide

Vill du få en helhetsbild av vad denna lektion täcker innan du dyker in? Kolla in denna illustrerade guide, som ger dig en känsla av de huvudsakliga ämnena som täcks och de viktigaste insikterna för dig att tänka på i varje avsnitt. Lektionens vägkarta tar dig från att förstå kärnkoncepten och utmaningarna till att adressera dem med relevanta prompt engineering-tekniker och bästa praxis. Observera att avsnittet "Avancerade tekniker" i denna guide hänvisar till innehåll som täcks i _nästa_ kapitel av denna läroplan.

## Vårt Startup

Låt oss nu prata om hur _detta ämne_ relaterar till vårt startup-uppdrag att [föra AI-innovation till utbildning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi vill bygga AI-drivna applikationer för _personlig inlärning_ - så låt oss tänka på hur olika användare av vår applikation kan "designa" prompts:

- **Administratörer** kan be AI att _analysera läroplansdata för att identifiera luckor i täckningen_. AI kan sammanfatta resultat eller visualisera dem med kod.
- **Lärare** kan be AI att _generera en lektionsplan för en målgrupp och ämne_. AI kan bygga den personliga planen i ett specificerat format.
- **Studenter** kan be AI att _handleda dem i ett svårt ämne_. AI kan nu guida studenter med lektioner, ledtrådar och exempel anpassade till deras nivå.

Det är bara toppen av isberget. Kolla in [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - ett öppen källkod-promptsbibliotek kuraterat av utbildningsexperter - för att få en bredare känsla av möjligheterna! _Försök att köra några av dessa prompts i sandboxen eller använd OpenAI Playground för att se vad som händer!_

## Vad är Prompt Engineering?

Vi började denna lektion med att definiera **Prompt Engineering** som processen att _designa och optimera_ textinmatningar (prompts) för att leverera konsekventa och kvalitativa svar (kompletteringar) för ett givet applikationsmål och modell. Vi kan tänka på detta som en 2-stegsprocess:

- _designa_ den initiala prompten för en given modell och mål
- _förfina_ prompten iterativt för att förbättra kvaliteten på svaret

Detta är nödvändigtvis en trial-and-error-process som kräver användarens intuition och ansträngning för att få optimala resultat. Så varför är det viktigt? För att svara på den frågan behöver vi först förstå tre koncept:

- _Tokenisering_ = hur modellen "ser" prompten
- _Bas LLMs_ = hur grundmodellen "bearbetar" en prompt
- _Instruktionsanpassade LLMs_ = hur modellen nu kan se "uppgifter"

### Tokenisering

En LLM ser prompts som en _sekvens av tokens_ där olika modeller (eller versioner av en modell) kan tokenisera samma prompt på olika sätt. Eftersom LLMs är tränade på tokens (och inte på råtext), har sättet som prompts tokeniseras en direkt påverkan på kvaliteten på det genererade svaret.

För att få en intuition för hur tokenisering fungerar, prova verktyg som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) som visas nedan. Kopiera in din prompt - och se hur den omvandlas till tokens, och notera hur blanksteg och skiljetecken hanteras. Observera att detta exempel visar en äldre LLM (GPT-3) - så att prova detta med en nyare modell kan ge ett annat resultat.

### Koncept: Grundmodeller

När en prompt är tokeniserad är huvudfunktionen för ["Bas LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller Grundmodell) att förutsäga token i den sekvensen. Eftersom LLMs är tränade på massiva textdatamängder, har de en god känsla för de statistiska relationerna mellan tokens och kan göra den förutsägelsen med viss säkerhet. Observera att de inte förstår _meningen_ med orden i prompten eller token; de ser bara ett mönster de kan "komplettera" med sin nästa förutsägelse. De kan fortsätta förutsäga sekvensen tills den avslutas av användarens ingripande eller någon förutbestämd villkor.

Vill du se hur prompt-baserad komplettering fungerar? Skriv in ovanstående prompt i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinställningarna. Systemet är konfigurerat för att behandla prompts som förfrågningar om information - så du bör se en komplettering som uppfyller detta sammanhang.

Men vad händer om användaren ville se något specifikt som uppfyllde några kriterier eller uppgiftsmål? Det är här _instruktionsanpassade_ LLMs kommer in i bilden.

### Koncept: Instruktionsanpassade LLMs

En [Instruktionsanpassad LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) börjar med grundmodellen och finjusterar den med exempel eller inmatnings-/utgångspar (t.ex. fleromgångs-"meddelanden") som kan innehålla tydliga instruktioner - och svaret från AI försöker följa den instruktionen.

Detta använder tekniker som Reinforcement Learning with Human Feedback (RLHF) som kan träna modellen att _följa instruktioner_ och _lära sig av feedback_ så att den producerar svar som är bättre lämpade för praktiska tillämpningar och mer relevanta för användarens mål.

Låt oss prova det - gå tillbaka till prompten ovan, men ändra nu _systemmeddelandet_ för att ge följande instruktion som sammanhang:

> _Sammanfatta innehållet du får för en andraklassare. Håll resultatet till ett stycke med 3-5 punkter._

Ser du hur resultatet nu är anpassat för att återspegla det önskade målet och formatet? En lärare kan nu direkt använda detta svar i sina bilder för den klassen.

## Varför behöver vi Prompt Engineering?

Nu när vi vet hur prompts bearbetas av LLMs, låt oss prata om _varför_ vi behöver prompt engineering. Svaret ligger i det faktum att nuvarande LLMs ställer ett antal utmaningar som gör _tillförlitliga och konsekventa kompletteringar_ svårare att uppnå utan att lägga ner ansträngning på promptkonstruktion och optimering. Till exempel:

1. **Modellsvar är stokastiska.** Samma prompt kommer sannolikt att producera olika svar med olika modeller eller modellversioner. Och det kan till och med producera olika resultat med _samma modell_ vid olika tidpunkter. _Prompt engineering-tekniker kan hjälpa oss att minimera dessa variationer genom att tillhandahålla bättre skyddsräcken_.

2. **Modeller kan fabricera svar.** Modeller är förtränade med _stora men begränsade_ datamängder, vilket innebär att de saknar kunskap om koncept utanför det träningsområdet. Som ett resultat kan de producera kompletteringar som är felaktiga, imaginära eller direkt motsägande till kända fakta. _Prompt engineering-tekniker hjälper användare att identifiera och mildra sådana fabrikationer, t.ex. genom att be AI om citat eller resonemang_.

3. **Modellers kapabiliteter varierar.** Nyare modeller eller modellgenerationer kommer att ha rikare kapabiliteter men också medföra unika egenheter och avvägningar i kostnad och komplexitet. _Prompt engineering kan hjälpa oss att utveckla bästa praxis och arbetsflöden som abstraherar bort skillnader och anpassar sig till modellspecifika krav på skalbara, sömlösa sätt_.

Låt oss se detta i aktion i OpenAI eller Azure OpenAI Playground:

- Använd samma prompt med olika LLM-distributioner (t.ex. OpenAI, Azure OpenAI, Hugging Face) - såg du variationerna?
- Använd samma prompt upprepade gånger med _samma_ LLM-distribution (t.ex. Azure OpenAI playground) - hur skiljde sig dessa variationer?

### Exempel på fabrikationer

I denna kurs använder vi termen **"fabrikation"** för att referera till fenomenet där LLMs ibland genererar faktuellt felaktig information på grund av begränsningar i deras träning eller andra begränsningar. Du kanske också har hört detta kallas _"hallucinationer"_ i populära artiklar eller forskningsrapporter. Men vi rekommenderar starkt att använda _"fabrikation"_ som termen så att vi inte av misstag tillskriver mänskliga egenskaper till en maskindriven utgång. Detta förstärker också [Riktlinjer för Ansvarsfull AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) från ett terminologiskt perspektiv, och tar bort termer som också kan betraktas som stötande eller icke-inkluderande i vissa sammanhang.

Vill du få en känsla av hur fabrikationer fungerar? Tänk på en prompt som instruerar AI att generera innehåll för ett icke-existerande ämne (för att säkerställa att det inte finns i träningsdatamängden). Till exempel - jag provade denna prompt:

> **Prompt:** generera en lektionsplan om Marskriget 2076.

En webbsökning visade mig att det fanns fiktiva berättelser (t.ex. tv-serier eller böcker) om Marskrig - men inga år 2076. Sunt förnuft säger också att 2076 är _i framtiden_ och därför inte kan associeras med en verklig händelse.

Så vad händer när vi kör denna prompt med olika LLM-leverantörer?

Som förväntat producerar varje modell (eller modellversion) något olika svar tack vare stokastiskt beteende och modellkapabilitetsvariationer. Till exempel riktar sig en modell till en åttondeklassare medan den andra antar en gymnasieelev. Men alla tre modeller genererade svar som kunde övertyga en oinformerad användare om att händelsen var verklig.

Prompt engineering-tekniker som _metaprompting_ och _temperaturkonfiguration_ kan minska modellers fabrikationer till viss del. Nya prompt engineering-_arkitekturer_ integrerar också nya verktyg och tekniker sömlöst i promptflödet, för att mildra eller minska några av dessa effekter.

## Fallstudie: GitHub Copilot

Låt oss avsluta detta avsnitt genom att få en känsla av hur prompt engineering används i verkliga lösningar genom att titta på en fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot är din "AI Pair Programmer" - den konverterar textprompts till kodkompletteringar och är integrerad i din utvecklingsmiljö (t.ex. Visual Studio Code) för en sömlös användarupplevelse. Som dokumenterat i serien av bloggar nedan, var den tidigaste versionen baserad på OpenAI Codex-modellen - med ingenjörer som snabbt insåg behovet av att finjustera modellen och utveckla bättre prompt engineering-tekniker, för att förbättra kodkvaliteten. I juli [debuterade de en förbättrad AI-modell som går bortom Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) för ännu snabbare förslag.

Läs inläggen i ordning, för att följa deras inlärningsresa.

Du kan också bläddra i deras [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) för fler inlägg som [detta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som visar hur dessa modeller och tekniker _tillämpas_ för att driva verkliga applikationer.

## Promptkonstruktion

Vi har sett varför prompt engineering är viktigt - nu låt oss förstå hur prompts _konstrueras_ så vi kan utvärdera olika tekniker för mer effektiv promptdesign.

### Grundläggande Prompt

Låt oss börja med den grundläggande prompten: en textinmatning som skickas till modellen utan någon annan kontext. Här är ett exempel - när vi skickar de första orden i USA:s nationalsång till OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) kompletterar den omedelbart svaret med de nästa raderna, vilket illustrerar det grundläggande förutsägbara beteendet.

### Komplex Prompt

Nu låt oss lägga till kontext och instruktioner till den grundläggande prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to
Det verkliga värdet av mallar ligger i förmågan att skapa och publicera _prompt-bibliotek_ för vertikala applikationsdomäner - där promptmallen nu är _optimerad_ för att återspegla applikationsspecifik kontext eller exempel som gör svaren mer relevanta och korrekta för den avsedda användargruppen. Repositoriet [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) är ett utmärkt exempel på detta tillvägagångssätt, där man samlar ett bibliotek av prompts för utbildningsdomänen med fokus på nyckelmål som lektionsplanering, kursplanedesign, studenthandledning etc.

## Stödjande innehåll

Om vi tänker på promptkonstruktion som att ha en instruktion (uppgift) och ett mål (primärt innehåll), då är _sekundärt innehåll_ som ytterligare kontext vi tillhandahåller för att **påverka resultatet på något sätt**. Det kan vara justeringsparametrar, formateringsinstruktioner, ämnestaxonomier etc. som kan hjälpa modellen att _anpassa_ sitt svar för att passa de önskade användarmålen eller förväntningarna.

Till exempel: Givet en kurskatalog med omfattande metadata (namn, beskrivning, nivå, metadatataggar, instruktör etc.) om alla tillgängliga kurser i kursplanen:

- vi kan definiera en instruktion för att "sammanfatta kurskatalogen för hösten 2023"
- vi kan använda det primära innehållet för att ge några exempel på det önskade resultatet
- vi kan använda det sekundära innehållet för att identifiera de fem främsta "taggarna" av intresse.

Nu kan modellen ge en sammanfattning i det format som visas av de få exemplen - men om ett resultat har flera taggar, kan den prioritera de fem taggar som identifierats i det sekundära innehållet.

---

<!--
LEKTIONSMALL:
Denna enhet bör täcka kärnkoncept #1.
Förstärk konceptet med exempel och referenser.

KONCEPT #3:
Prompttekniker.
Vilka är några grundläggande tekniker för promptteknik?
Illustrera det med några övningar.
-->

## Bästa praxis för prompt

Nu när vi vet hur prompts kan _konstrueras_, kan vi börja tänka på hur man _designar_ dem för att återspegla bästa praxis. Vi kan tänka på detta i två delar - att ha rätt _mentalitet_ och att tillämpa rätt _tekniker_.

### Mentalitet för promptteknik

Promptteknik är en process av försök och misstag, så håll tre breda vägledande faktorer i åtanke:

1. **Domänförståelse är viktigt.** Svarens noggrannhet och relevans är en funktion av _domänen_ där applikationen eller användaren verkar. Använd din intuition och domänexpertis för att **anpassa tekniker** ytterligare. Till exempel, definiera _domänspecifika personligheter_ i dina systemprompts, eller använd _domänspecifika mallar_ i dina användarprompts. Tillhandahåll sekundärt innehåll som återspeglar domänspecifika kontexter, eller använd _domänspecifika ledtrådar och exempel_ för att vägleda modellen mot välbekanta användningsmönster.

2. **Modellförståelse är viktigt.** Vi vet att modeller är stokastiska till sin natur. Men modellimplementationer kan också variera när det gäller träningsdatasetet de använder (förtränad kunskap), de funktioner de tillhandahåller (t.ex. via API eller SDK) och typen av innehåll de är optimerade för (t.ex. kod vs. bilder vs. text). Förstå styrkorna och begränsningarna hos den modell du använder, och använd den kunskapen för att _prioritera uppgifter_ eller bygga _anpassade mallar_ som är optimerade för modellens kapabiliteter.

3. **Iteration och validering är viktigt.** Modeller utvecklas snabbt, och det gör också teknikerna för promptteknik. Som domänexpert kan du ha annan kontext eller kriterier för _din_ specifika applikation, som kanske inte gäller för den bredare gemenskapen. Använd verktyg och tekniker för promptteknik för att "komma igång" med promptkonstruktion, iterera sedan och validera resultaten med din egen intuition och domänexpertis. Dokumentera dina insikter och skapa en **kunskapsbas** (t.ex. promptbibliotek) som kan användas som en ny utgångspunkt av andra, för snabbare iterationer i framtiden.

## Bästa praxis

Låt oss nu titta på vanliga bästa praxis som rekommenderas av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) och [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktiker.

| Vad                                | Varför                                                                                                                                                                                                                                               |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Utvärdera de senaste modellerna.   | Nya modellgenerationer har sannolikt förbättrade funktioner och kvalitet - men kan också innebära högre kostnader. Utvärdera dem för påverkan och fatta sedan migrationsbeslut.                                                                     |
| Separera instruktioner och kontext | Kontrollera om din modell/leverantör definierar _avgränsare_ för att tydligare skilja instruktioner, primärt och sekundärt innehåll. Detta kan hjälpa modeller att tilldela vikter mer exakt till tokens.                                              |
| Var specifik och tydlig            | Ge mer detaljer om den önskade kontexten, resultatet, längden, formatet, stilen etc. Detta kommer att förbättra både kvaliteten och konsistensen i svaren. Fånga recept i återanvändbara mallar.                                                       |
| Var beskrivande, använd exempel    | Modeller kan svara bättre på ett "visa och berätta"-tillvägagångssätt. Börja med ett `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` värden. Återkom till [Learning Sandbox avsnittet](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) för att lära dig hur.

### Nästa steg, öppna Jupyter Notebook

- Välj runtime-kärnan. Om du använder alternativ 1 eller 2, välj helt enkelt den förvalda Python 3.10.x kärnan som tillhandahålls av utvecklingscontainern.

Du är redo att köra övningarna. Observera att det inte finns några _rätt och fel_ svar här - bara att utforska alternativ genom försök och misstag och bygga intuition för vad som fungerar för en given modell och applikationsdomän.

_Av denna anledning finns det inga Kodlösningssegment i denna lektion. Istället kommer Notebooken att ha Markdown-celler med titeln "Min lösning:" som visar ett exempel på resultat för referens._

 <!--
LEKTIONSMALL:
Avsluta avsnittet med en sammanfattning och resurser för självstyrt lärande.
-->

## Kunskapskontroll

Vilket av följande är en bra prompt som följer några rimliga bästa praxis?

1. Visa mig en bild av en röd bil
2. Visa mig en bild av en röd bil av märket Volvo och modellen XC90 parkerad vid en klippa med solnedgången
3. Visa mig en bild av en röd bil av märket Volvo och modellen XC90

A: 2, det är den bästa prompten eftersom den ger detaljer om "vad" och går in på specifika detaljer (inte bara vilken bil som helst utan ett specifikt märke och modell) och den beskriver också den övergripande miljön. 3 är nästa bästa eftersom den också innehåller mycket beskrivning.

## 🚀 Utmaning

Se om du kan använda "ledtrådstekniken" med prompten: Fyll i meningen "Visa mig en bild av en röd bil av märket Volvo och ". Vad svarar den med, och hur skulle du förbättra det?

## Bra jobbat! Fortsätt ditt lärande

Vill du lära dig mer om olika koncept inom Prompt Engineering? Gå till [sidan för fortsatt lärande](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att hitta andra bra resurser om detta ämne.

Gå vidare till Lektion 5 där vi kommer att titta på [avancerade promptingtekniker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår vid användning av denna översättning.