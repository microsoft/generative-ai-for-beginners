<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:48:31+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sv"
}
-->
# Grundläggande om Prompt Engineering

## Introduktion
Detta avsnitt täcker viktiga koncept och tekniker för att skapa effektiva prompts i generativa AI-modeller. Hur du skriver din prompt till en LLM spelar också roll. En noggrant utformad prompt kan uppnå en bättre kvalitet på svaret. Men vad betyder egentligen termer som _prompt_ och _prompt engineering_? Och hur förbättrar jag promptens _inmatning_ som jag skickar till LLM? Dessa är frågor vi försöker besvara i detta kapitel och det nästa.

_Generativ AI_ är kapabel att skapa nytt innehåll (t.ex. text, bilder, ljud, kod etc.) som svar på användarförfrågningar. Detta uppnås med hjälp av _Stora språkmodeller_ som OpenAI:s GPT-serie ("Generative Pre-trained Transformer") som är tränade för att använda naturligt språk och kod.

Användare kan nu interagera med dessa modeller genom välbekanta paradigm som chatt, utan att behöva någon teknisk expertis eller utbildning. Modellerna är _prompt-baserade_ - användare skickar en textinmatning (prompt) och får tillbaka AI-svaret (completion). De kan sedan "chatta med AI" iterativt, i flerskiktade konversationer, och förfina sin prompt tills svaret motsvarar deras förväntningar.

"Prompts" blir nu det primära _programmeringsgränssnittet_ för generativa AI-appar, som talar om för modellerna vad de ska göra och påverkar kvaliteten på de återkommande svaren. "Prompt Engineering" är ett snabbt växande forskningsområde som fokuserar på _design och optimering_ av prompts för att leverera konsekventa och kvalitativa svar i stor skala.

## Lärandemål

I denna lektion lär vi oss vad Prompt Engineering är, varför det är viktigt och hur vi kan skapa mer effektiva prompts för en given modell och applikationsmål. Vi kommer att förstå kärnkoncept och bästa praxis för prompt engineering - och lära oss om en interaktiv Jupyter Notebooks "sandbox"-miljö där vi kan se dessa koncept tillämpas på verkliga exempel.

I slutet av denna lektion kommer vi att kunna:

1. Förklara vad prompt engineering är och varför det är viktigt.
2. Beskriva komponenterna i en prompt och hur de används.
3. Lära oss bästa praxis och tekniker för prompt engineering.
4. Tillämpa inlärda tekniker på verkliga exempel, med hjälp av en OpenAI-endpoint.

## Nyckeltermer

Prompt Engineering: Praktiken att designa och förfina inmatningar för att styra AI-modeller mot att producera önskade utdata.
Tokenisering: Processen att konvertera text till mindre enheter, kallade tokens, som en modell kan förstå och bearbeta.
Instruktionsanpassade LLMs: Stora språkmodeller (LLMs) som har finjusterats med specifika instruktioner för att förbättra deras svarsnoggrannhet och relevans.

## Lärandesandlåda

Prompt engineering är för närvarande mer konst än vetenskap. Det bästa sättet att förbättra vår intuition för det är att _öva mer_ och anta en trial-and-error-strategi som kombinerar applikationsdomänexpertis med rekommenderade tekniker och modell-specifika optimeringar.

Jupyter Notebook som följer med denna lektion ger en _sandlåda_-miljö där du kan prova det du lär dig - under tiden eller som en del av kodutmaningen i slutet. För att genomföra övningarna behöver du:

1. **En Azure OpenAI API-nyckel** - tjänstens slutpunkt för en distribuerad LLM.
2. **En Python-runtime** - där Notebooks kan köras.
3. **Lokala miljövariabler** - _slutför [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) stegen nu för att förbereda dig_.

Noteboken kommer med _start_-övningar - men du uppmuntras att lägga till dina egna _Markdown_- (beskrivning) och _Kod_- (promptförfrågningar) sektioner för att prova fler exempel eller idéer - och bygga din intuition för promptdesign.

## Illustrerad guide

Vill du få en överblick över vad denna lektion täcker innan du dyker in? Kolla in denna illustrerade guide, som ger dig en känsla för de huvudsakliga ämnena som täcks och de viktigaste slutsatserna för dig att tänka på i varje avsnitt. Lektionens vägkarta tar dig från att förstå kärnkoncept och utmaningar till att hantera dem med relevanta prompt engineering-tekniker och bästa praxis. Observera att avsnittet "Avancerade tekniker" i denna guide hänvisar till innehåll som täcks i nästa kapitel av denna läroplan.

## Vårt Startup

Låt oss nu prata om hur _detta ämne_ relaterar till vårt startups uppdrag att [föra AI-innovation till utbildning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi vill bygga AI-drivna applikationer för _personligt lärande_ - så låt oss tänka på hur olika användare av vår applikation kan "designa" prompts:

- **Administratörer** kan be AI att _analysera läroplansdata för att identifiera luckor i täckningen_. AI kan sammanfatta resultat eller visualisera dem med kod.
- **Lärare** kan be AI att _skapa en lektionsplan för en målgrupp och ämne_. AI kan bygga den personliga planen i ett specificerat format.
- **Studenter** kan be AI att _handleda dem i ett svårt ämne_. AI kan nu vägleda studenter med lektioner, tips och exempel anpassade till deras nivå.

Detta är bara toppen av isberget. Kolla in [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - ett open-source prompts-bibliotek kuraterat av utbildningsexperter - för att få en bredare känsla för möjligheterna! _Prova att köra några av dessa prompts i sandlådan eller använd OpenAI Playground för att se vad som händer!_

## Vad är Prompt Engineering?

Vi började denna lektion med att definiera **Prompt Engineering** som processen att _designa och optimera_ textinmatningar (prompts) för att leverera konsekventa och kvalitativa svar (completions) för ett givet applikationsmål och modell. Vi kan tänka på detta som en tvåstegsprocess:

- _designa_ den initiala prompten för en given modell och mål
- _förfina_ prompten iterativt för att förbättra kvaliteten på svaret

Detta är nödvändigtvis en trial-and-error-process som kräver användarens intuition och ansträngning för att få optimala resultat. Så varför är det viktigt? För att svara på den frågan behöver vi först förstå tre koncept:

- _Tokenisering_ = hur modellen "ser" prompten
- _Bas-LLMs_ = hur grundmodellen "bearbetar" en prompt
- _Instruktionsanpassade LLMs_ = hur modellen nu kan se "uppgifter"

### Tokenisering

En LLM ser prompts som en _sekvens av tokens_ där olika modeller (eller versioner av en modell) kan tokenisera samma prompt på olika sätt. Eftersom LLMs är tränade på tokens (och inte på rå text), har sättet som prompts blir tokeniserade en direkt inverkan på kvaliteten på det genererade svaret.

För att få en intuition för hur tokenisering fungerar, prova verktyg som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) som visas nedan. Kopiera in din prompt - och se hur den omvandlas till tokens, med fokus på hur blanksteg och skiljetecken hanteras. Observera att detta exempel visar en äldre LLM (GPT-3) - så att prova detta med en nyare modell kan ge ett annat resultat.

### Koncept: Grundmodeller

När en prompt är tokeniserad är den primära funktionen för ["Bas-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grundmodell) att förutsäga token i den sekvensen. Eftersom LLMs är tränade på massiva textdataset har de en god känsla för de statistiska relationerna mellan tokens och kan göra den förutsägelsen med viss säkerhet. Observera att de inte förstår _betydelsen_ av orden i prompten eller token; de ser bara ett mönster de kan "slutföra" med sin nästa förutsägelse. De kan fortsätta förutsäga sekvensen tills den avslutas av användarens ingripande eller någon förutbestämd villkor.

Vill du se hur prompt-baserad completion fungerar? Ange prompten ovan i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinställningarna. Systemet är konfigurerat för att behandla prompts som förfrågningar om information - så du bör se en completion som uppfyller detta sammanhang.

Men vad händer om användaren ville se något specifikt som uppfyllde några kriterier eller uppgiftsmål? Det är här _instruktionsanpassade_ LLMs kommer in i bilden.

### Koncept: Instruktionsanpassade LLMs

En [Instruktionsanpassad LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) börjar med grundmodellen och finjusterar den med exempel eller in-/utmatningspar (t.ex. flerskiktade "meddelanden") som kan innehålla tydliga instruktioner - och svaret från AI försöker följa den instruktionen.

Detta använder tekniker som förstärkningsinlärning med mänsklig feedback (RLHF) som kan träna modellen att _följa instruktioner_ och _lära sig av feedback_ så att den producerar svar som är bättre lämpade för praktiska tillämpningar och mer relevanta för användarens mål.

Låt oss prova det - återvänd till prompten ovan, men ändra nu _systemmeddelandet_ för att ge följande instruktion som sammanhang:

> _Sammanfatta innehållet du får för en andra klassens elev. Håll resultatet till ett stycke med 3-5 punkter._

Ser du hur resultatet nu är anpassat för att återspegla det önskade målet och formatet? En lärare kan nu direkt använda detta svar i sina presentationer för den klassen.

## Varför behöver vi Prompt Engineering?

Nu när vi vet hur prompts bearbetas av LLMs, låt oss prata om _varför_ vi behöver prompt engineering. Svaret ligger i det faktum att nuvarande LLMs utgör ett antal utmaningar som gör _pålitliga och konsekventa completions_ mer utmanande att uppnå utan att lägga ansträngning på promptkonstruktion och optimering. Till exempel:

1. **Modellens svar är stokastiska.** _Samma prompt_ kommer sannolikt att producera olika svar med olika modeller eller modellversioner. Och det kan till och med producera olika resultat med _samma modell_ vid olika tidpunkter. _Prompt engineering-tekniker kan hjälpa oss att minimera dessa variationer genom att tillhandahålla bättre skyddsräcken_.

2. **Modeller kan fabricera svar.** Modeller är förtränade med _stora men ändliga_ dataset, vilket innebär att de saknar kunskap om koncept utanför det träningsområdet. Som ett resultat kan de producera completions som är felaktiga, imaginära eller direkt motsägande mot kända fakta. _Prompt engineering-tekniker hjälper användare att identifiera och mildra sådana fabricationer t.ex. genom att be AI om källhänvisningar eller resonemang_.

3. **Modellernas förmågor kommer att variera.** Nyare modeller eller modellgenerationer kommer att ha rikare förmågor men också medföra unika egenskaper och avvägningar i kostnad och komplexitet. _Prompt engineering kan hjälpa oss att utveckla bästa praxis och arbetsflöden som abstraherar bort skillnader och anpassar sig till modell-specifika krav på ett skalbart och sömlöst sätt_.

Låt oss se detta i aktion i OpenAI eller Azure OpenAI Playground:

- Använd samma prompt med olika LLM-distributioner (t.ex., OpenAI, Azure OpenAI, Hugging Face) - såg du variationerna?
- Använd samma prompt upprepade gånger med _samma_ LLM-distribution (t.ex., Azure OpenAI Playground) - hur skiljde sig dessa variationer?

### Fabrications Exempel

I denna kurs använder vi termen **"fabrication"** för att hänvisa till fenomenet där LLMs ibland genererar faktuellt felaktig information på grund av begränsningar i deras träning eller andra begränsningar. Du kanske också har hört detta hänvisas till som _"hallucinationer"_ i populära artiklar eller forskningsartiklar. Vi rekommenderar dock starkt att använda _"fabrication"_ som termen så att vi inte av misstag antropomorfiserar beteendet genom att tillskriva en mänsklig egenskap till ett maskindrivet resultat. Detta förstärker också [Ansvarsfull AI-riktlinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ur ett terminologiskt perspektiv, vilket tar bort termer som också kan anses vara stötande eller icke-inkluderande i vissa sammanhang.

Vill du få en känsla av hur fabricationer fungerar? Tänk på en prompt som instruerar AI att generera innehåll för ett icke-existerande ämne (för att säkerställa att det inte finns i träningsdatasetet). Till exempel - jag provade denna prompt:

> **Prompt:** generera en lektionsplan om det Marsianska kriget 2076.

En webbsökning visade mig att det fanns fiktiva berättelser (t.ex., TV-serier eller böcker) om Marsianska krig - men inga 2076. Sunt förnuft säger oss också att 2076 är _i framtiden_ och därmed inte kan associeras med en verklig händelse.

Så vad händer när vi kör denna prompt med olika LLM-leverantörer?

Som förväntat producerar varje modell (eller modellversion) något olika svar tack vare stokastiskt beteende och modellförmågevariationer. Till exempel riktar sig en modell till en åttonde klassens publik medan den andra antar en gymnasieelev. Men alla tre modellerna genererade svar som kunde övertyga en oinformerad användare att händelsen var verklig.

Prompt engineering-tekniker som _metaprompting_ och _temperaturkonfiguration_ kan minska modellfabricationer till viss del. Nya prompt engineering-_arkitekturer_ införlivar också nya verktyg och tekniker sömlöst i promptflödet, för att mildra eller minska några av dessa effekter.

## Fallstudie: GitHub Copilot

Låt oss avsluta detta avsnitt genom att få en känsla för hur prompt engineering används i verkliga lösningar genom att titta på en fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot är din "AI Pair Programmer" - den konverterar textprompts till kodcompletions och är integrerad i din utvecklingsmiljö (t.ex., Visual Studio Code) för en sömlös användarupplevelse. Som dokumenterat i serien av bloggar nedan, var den tidigaste versionen baserad på OpenAI Codex-modellen - med ingenjörer som snabbt insåg behovet av att finjustera modellen och utveckla bättre prompt engineering-tekniker, för att förbättra kodkvaliteten. I juli [debuterade de en förbättrad AI-modell som går bortom Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) för ännu snabbare förslag.

Läs inläggen i ordning, för att följa deras läranderesa.

- **Maj 2023** | [GitHub Copilot blir bättre på att förstå din kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inuti GitHub: Arbeta med LLMs bakom GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Hur man skriver bättre prompts för GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot går bortom Codex med förbättrad AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [En utvecklares guide till Prompt Engineering och LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai
Slutligen ligger det verkliga värdet av mallar i förmågan att skapa och publicera _promptbibliotek_ för vertikala applikationsdomäner - där promptmallen nu är _optimerad_ för att återspegla applikationsspecifik kontext eller exempel som gör svaren mer relevanta och korrekta för den riktade användargruppen. Repositoriet [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) är ett utmärkt exempel på detta tillvägagångssätt, som kuraterar ett bibliotek av prompts för utbildningsdomänen med fokus på nyckelmål som lektionsplanering, läroplansdesign, elevhandledning etc.

## Stödjande innehåll

Om vi tänker på promptkonstruktion som att ha en instruktion (uppgift) och ett mål (primärt innehåll), så är _sekundärt innehåll_ som ytterligare kontext vi tillhandahåller för att **påverka utfallet på något sätt**. Det kan vara justeringsparametrar, formateringsinstruktioner, ämnestaxonomier etc. som kan hjälpa modellen att _anpassa_ sitt svar för att passa de önskade användarmålen eller förväntningarna.

Till exempel: Givet en kurskatalog med omfattande metadata (namn, beskrivning, nivå, metadatataggar, instruktör etc.) för alla tillgängliga kurser i läroplanen:

- vi kan definiera en instruktion för att "sammanfatta kurskatalogen för hösten 2023"
- vi kan använda det primära innehållet för att tillhandahålla några exempel på det önskade resultatet
- vi kan använda det sekundära innehållet för att identifiera de fem främsta "taggarna" av intresse.

Nu kan modellen tillhandahålla en sammanfattning i det format som visas av de få exemplen - men om ett resultat har flera taggar kan den prioritera de fem taggar som identifierats i det sekundära innehållet.

---

## Bästa praxis för prompt

Nu när vi vet hur prompts kan _konstrueras_ kan vi börja tänka på hur man _designar_ dem för att återspegla bästa praxis. Vi kan tänka på detta i två delar - att ha rätt _mentalitet_ och att tillämpa rätt _tekniker_.

### Mentalitet för prompt engineering

Prompt engineering är en process av försök och misstag, så håll tre breda vägledande faktorer i åtanke:

1. **Domänförståelse är viktigt.** Svarens noggrannhet och relevans är en funktion av _domänen_ där den applikationen eller användaren verkar. Använd din intuition och domänexpertis för att **anpassa tekniker** ytterligare. Till exempel, definiera _domänspecifika personligheter_ i dina systemprompts, eller använd _domänspecifika mallar_ i dina användarprompts. Tillhandahåll sekundärt innehåll som återspeglar domänspecifika kontexter, eller använd _domänspecifika signaler och exempel_ för att vägleda modellen mot bekanta användningsmönster.

2. **Modellförståelse är viktigt.** Vi vet att modeller är stokastiska till sin natur. Men modellimplementeringar kan också variera beroende på träningsdatasetet de använder (förtränad kunskap), de funktioner de erbjuder (t.ex. via API eller SDK) och typen av innehåll de är optimerade för (t.ex. kod vs. bilder vs. text). Förstå styrkorna och begränsningarna hos den modell du använder och använd den kunskapen för att _prioritera uppgifter_ eller bygga _anpassade mallar_ som är optimerade för modellens kapabiliteter.

3. **Iteration och validering är viktigt.** Modeller utvecklas snabbt, och det gör även teknikerna för prompt engineering. Som domänexpert kan du ha andra kontexter eller kriterier för _din_ specifika applikation, som kanske inte gäller för den bredare gemenskapen. Använd verktyg och tekniker för prompt engineering för att "snabbstarta" promptkonstruktionen, iterera sedan och validera resultaten med din egen intuition och domänexpertis. Dokumentera dina insikter och skapa en **kunskapsbas** (t.ex. promptbibliotek) som kan användas som en ny baslinje av andra, för snabbare iterationer i framtiden.

## Bästa praxis

Låt oss nu titta på vanliga bästa praxis som rekommenderas av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) och [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktiker.

| Vad                               | Varför                                                                                                                                                                                                                                              |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Utvärdera de senaste modellerna.  | Nya modellgenerationer har sannolikt förbättrade funktioner och kvalitet - men kan också medföra högre kostnader. Utvärdera dem för påverkan, fatta sedan migrationsbeslut.                                                                         |
| Separera instruktioner & kontext  | Kontrollera om din modell/leverantör definierar _avgränsare_ för att tydligare skilja instruktioner, primärt och sekundärt innehåll. Detta kan hjälpa modeller att tilldela vikter mer exakt till tokens.                                          |
| Var specifik och tydlig           | Ge mer detaljer om önskad kontext, resultat, längd, format, stil etc. Detta kommer att förbättra både kvaliteten och konsistensen i svaren. Fånga recept i återanvändbara mallar.                                                                  |
| Var beskrivande, använd exempel   | Modeller kan svara bättre på ett "visa och berätta"-tillvägagångssätt. Börja med en `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` värden. Återkom till [Learning Sandbox-sektionen](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) för att lära dig hur.

### Nästa steg, öppna Jupyter Notebook

- Välj runtime-kärnan. Om du använder alternativ 1 eller 2, välj bara den förvalda Python 3.10.x-kärnan som tillhandahålls av utvecklingsbehållaren.

Du är redo att köra övningarna. Observera att det inte finns några _rätt och fel_ svar här - bara att utforska alternativ genom försök och misstag och bygga intuition för vad som fungerar för en given modell och applikationsdomän.

_Av denna anledning finns det inga Kodlösningssegment i denna lektion. Istället kommer Notebook att ha Markdown-celler med titeln "My Solution:" som visar ett exempel på output för referens._

## Kunskapskontroll

Vilken av följande är en bra prompt enligt några rimliga bästa praxis?

1. Visa mig en bild av röd bil
2. Visa mig en bild av röd bil av märke Volvo och modell XC90 parkerad vid en klippa med solnedgång
3. Visa mig en bild av röd bil av märke Volvo och modell XC90

A: 2, det är den bästa prompten eftersom den ger detaljer om "vad" och går in på detaljer (inte bara vilken bil som helst utan ett specifikt märke och modell) och den beskriver också den övergripande miljön. 3 är näst bäst eftersom den också innehåller mycket beskrivning.

## 🚀 Utmaning

Se om du kan utnyttja "signal"-tekniken med prompten: Komplettera meningen "Visa mig en bild av röd bil av märke Volvo och ". Vad svarar den med, och hur skulle du förbättra den?

## Bra jobbat! Fortsätt din inlärning

Vill du lära dig mer om olika koncept inom Prompt Engineering? Gå till [sidan för fortsatt lärande](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att hitta andra fantastiska resurser om detta ämne.

Gå vidare till Lektion 5 där vi kommer att titta på [avancerade promptingtekniker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår från användningen av denna översättning.