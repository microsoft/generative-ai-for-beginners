<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:22:06+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "sv"
}
-->
# Introduktion till Generativ AI och Stora Språkmodeller

_(Klicka på bilden ovan för att se videon av denna lektion)_

Generativ AI är artificiell intelligens som kan generera text, bilder och andra typer av innehåll. Vad som gör det till en fantastisk teknologi är att det demokratiserar AI; vem som helst kan använda det med så lite som en textprompt, en mening skriven på naturligt språk. Du behöver inte lära dig ett språk som Java eller SQL för att uppnå något värdefullt, allt du behöver göra är att använda ditt språk, ange vad du vill och få ett förslag från en AI-modell. Användningsområdena och påverkan är enorma; du kan skriva eller förstå rapporter, skapa applikationer och mycket mer, allt på några sekunder.

I denna kursplan kommer vi att utforska hur vår startup utnyttjar generativ AI för att låsa upp nya scenarier inom utbildningsvärlden och hur vi hanterar de oundvikliga utmaningarna kopplade till de sociala konsekvenserna av dess användning och teknikens begränsningar.

## Introduktion

Denna lektion kommer att täcka:

- Introduktion till affärsscenariot: vår startupidé och mission.
- Generativ AI och hur vi landade i det nuvarande tekniklandskapet.
- Den inre funktionen hos en stor språkmodell.
- Huvudkapaciteter och praktiska användningsfall för Stora Språkmodeller.

## Lärandemål

Efter att ha avslutat denna lektion kommer du att förstå:

- Vad generativ AI är och hur Stora Språkmodeller fungerar.
- Hur du kan utnyttja stora språkmodeller för olika användningsfall, med fokus på utbildningsscenarier.

## Scenario: vår utbildningsstartup

Generativ artificiell intelligens (AI) representerar toppen av AI-teknologi, och tänjer på gränserna för vad som en gång ansågs omöjligt. Generativa AI-modeller har flera kapaciteter och användningsområden, men för denna kursplan kommer vi att utforska hur det revolutionerar utbildning genom en fiktiv startup. Vi kommer att referera till denna startup som _vår startup_. Vår startup arbetar inom utbildningsområdet med det ambitiösa uppdragsbeskrivningen:

> _att förbättra tillgängligheten i lärandet, på global skala, säkerställa rättvis tillgång till utbildning och erbjuda personliga lärandeupplevelser till varje elev, enligt deras behov_.

Vårt startupteam är medvetna om att vi inte kommer att kunna uppnå detta mål utan att utnyttja ett av de mest kraftfulla verktygen i modern tid – Stora Språkmodeller (LLMs).

Generativ AI förväntas revolutionera sättet vi lär oss och undervisar idag, med elever som har tillgång till virtuella lärare 24 timmar om dygnet som tillhandahåller stora mängder information och exempel, och lärare som kan utnyttja innovativa verktyg för att bedöma sina elever och ge feedback.

För att börja, låt oss definiera några grundläggande begrepp och terminologi som vi kommer att använda genom kursplanen.

## Hur fick vi Generativ AI?

Trots den extraordinära _hype_ som skapats nyligen av tillkännagivandet av generativa AI-modeller, har denna teknologi utvecklats under decennier, med de första forskningsinsatserna som går tillbaka till 60-talet. Vi är nu vid en punkt där AI har mänskliga kognitiva förmågor, som konversation, vilket visas av exempelvis [OpenAI ChatGPT](https://openai.com/chatgpt) eller [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), som också använder en GPT-modell för webbsökning Bing-konversationer.

Om vi backar lite, bestod de allra första prototyperna av AI av skrivna chatbots, som förlitade sig på en kunskapsbas extraherad från en grupp experter och representerad i en dator. Svaren i kunskapsbasen utlöste av nyckelord som dök upp i inputtexten. Men det blev snart klart att en sådan metod, med skrivna chatbots, inte skalar väl.

### En statistisk metod för AI: Maskininlärning

En vändpunkt kom under 90-talet, med tillämpningen av en statistisk metod för textanalys. Detta ledde till utvecklingen av nya algoritmer – kända som maskininlärning – som kan lära sig mönster från data utan att vara uttryckligen programmerade. Denna metod gör det möjligt för maskiner att simulera mänsklig språkförståelse: en statistisk modell tränas på text-etikett parningar, vilket gör det möjligt för modellen att klassificera okänd inputtext med en fördefinierad etikett som representerar meddelandets intention.

### Neurala nätverk och moderna virtuella assistenter

Under de senaste åren har den teknologiska utvecklingen av hårdvara, som kan hantera större mängder data och mer komplexa beräkningar, uppmuntrat forskning inom AI, vilket ledde till utvecklingen av avancerade maskininlärningsalgoritmer kända som neurala nätverk eller djupa inlärningsalgoritmer.

Neurala nätverk (och i synnerhet Recurrent Neural Networks – RNNs) förbättrade avsevärt naturlig språkbehandling, vilket möjliggjorde representationen av textens betydelse på ett mer meningsfullt sätt, genom att värdera sammanhanget av ett ord i en mening.

Detta är teknologin som drev de virtuella assistenterna som föddes under det första decenniet av det nya århundradet, mycket skickliga på att tolka mänskligt språk, identifiera ett behov och utföra en åtgärd för att tillfredsställa det – som att svara med ett fördefinierat manus eller använda en tredjepartstjänst.

### Nutid, Generativ AI

Så här kom vi till Generativ AI idag, som kan ses som en underkategori av djup inlärning.

Efter decennier av forskning inom AI-fältet övervann en ny modellarkitektur – kallad _Transformer_ – begränsningarna hos RNNs, genom att kunna ta mycket längre textsekvenser som input. Transformatorer är baserade på uppmärksamhetsmekanismen, vilket gör det möjligt för modellen att ge olika vikter till de inputs den får, 'lägga mer uppmärksamhet' där den mest relevanta informationen är koncentrerad, oavsett deras ordning i textsekvensen.

De flesta av de senaste generativa AI-modellerna – även kända som Stora Språkmodeller (LLMs), eftersom de arbetar med textuella inputs och outputs – är faktiskt baserade på denna arkitektur. Det som är intressant med dessa modeller – tränade på en enorm mängd oetiketterad data från olika källor som böcker, artiklar och webbplatser – är att de kan anpassas till en mängd olika uppgifter och generera grammatiskt korrekt text med en sken av kreativitet. Så, de har inte bara otroligt förbättrat en maskins förmåga att 'förstå' en inputtext, utan de har möjliggjort dess förmåga att generera ett originalsvar på mänskligt språk.

## Hur fungerar stora språkmodeller?

I nästa kapitel kommer vi att utforska olika typer av Generativa AI-modeller, men för nu låt oss titta på hur stora språkmodeller fungerar, med fokus på OpenAI GPT (Generative Pre-trained Transformer) modeller.

- **Tokenizer, text till siffror**: Stora Språkmodeller tar emot en text som input och genererar en text som output. Men eftersom de är statistiska modeller, fungerar de mycket bättre med siffror än textsekvenser. Därför bearbetas varje input till modellen av en tokenizer, innan den används av kärnmodellen. En token är en bit text – bestående av ett variabelt antal tecken, så tokenizer's huvuduppgift är att dela upp inputen i en array av tokens. Sedan mappas varje token med ett tokenindex, vilket är den heltaliga kodningen av den ursprungliga textbiten.

- **Förutsäga outputtokens**: Givet n tokens som input (med max n som varierar från en modell till en annan), kan modellen förutsäga en token som output. Denna token inkorporeras sedan i inputen vid nästa iteration, i ett expanderande fönstermönster, vilket möjliggör en bättre användarupplevelse av att få en (eller flera) mening som svar. Detta förklarar varför, om du någonsin har lekt med ChatGPT, du kanske har märkt att det ibland ser ut som att det stannar mitt i en mening.

- **Urvalsprocess, sannolikhetsfördelning**: Outputtoken väljs av modellen enligt dess sannolikhet att förekomma efter den aktuella textsekvensen. Detta beror på att modellen förutspår en sannolikhetsfördelning över alla möjliga 'nästa tokens', beräknad baserat på dess träning. Men inte alltid väljs token med högst sannolikhet från den resulterande fördelningen. En grad av slumpmässighet läggs till detta val, på ett sätt som gör att modellen agerar på ett icke-deterministiskt sätt - vi får inte exakt samma output för samma input. Denna grad av slumpmässighet läggs till för att simulera processen av kreativt tänkande och kan justeras med en modellparameter som kallas temperatur.

## Hur kan vår startup utnyttja Stora Språkmodeller?

Nu när vi har en bättre förståelse för den inre funktionen hos en stor språkmodell, låt oss se några praktiska exempel på de vanligaste uppgifterna de kan utföra ganska bra, med fokus på vårt affärsscenario. Vi sa att huvudkapaciteten hos en Stor Språkmodell är _att generera en text från grunden, med start från en textuell input, skriven på naturligt språk_.

Men vilken typ av textuell input och output?
Inputen till en stor språkmodell är känd som en prompt, medan outputen är känd som en completion, ett begrepp som refererar till modellens mekanism att generera nästa token för att komplettera den aktuella inputen. Vi kommer att dyka djupt in i vad en prompt är och hur man designar den på ett sätt som får ut det mesta av vår modell. Men för nu, låt oss bara säga att en prompt kan inkludera:

- En **instruktion** som specificerar typen av output vi förväntar oss från modellen. Denna instruktion kan ibland innehålla några exempel eller ytterligare data.

  1. Sammanfattning av en artikel, bok, produktrecensioner och mer, tillsammans med extraktion av insikter från ostrukturerad data.
  
  2. Kreativ idéutveckling och design av en artikel, en uppsats, en uppgift eller mer.

- En **fråga**, ställd i form av en konversation med en agent.

- En bit **text att komplettera**, vilket implicit är en begäran om skrivhjälp.

- En bit **kod** tillsammans med begäran om att förklara och dokumentera den, eller en kommentar som ber om att generera en kodbit som utför en specifik uppgift.

Exemplen ovan är ganska enkla och är inte avsedda att vara en uttömmande demonstration av Stora Språkmodellers kapaciteter. De är avsedda att visa potentialen av att använda generativ AI, särskilt men inte begränsat till utbildningssammanhang.

Dessutom är outputen från en generativ AI-modell inte perfekt och ibland kan modellens kreativitet motarbeta den, vilket resulterar i en output som är en kombination av ord som den mänskliga användaren kan tolka som en förvrängning av verkligheten, eller som kan vara stötande. Generativ AI är inte intelligent - åtminstone inte i den mer omfattande definitionen av intelligens, inklusive kritiskt och kreativt tänkande eller emotionell intelligens; den är inte deterministisk, och den är inte pålitlig, eftersom fabriceringar, såsom felaktiga referenser, innehåll och uttalanden, kan kombineras med korrekt information och presenteras på ett övertygande och självsäkert sätt. I de följande lektionerna kommer vi att hantera alla dessa begränsningar och vi kommer att se vad vi kan göra för att mildra dem.

## Uppgift

Din uppgift är att läsa mer om [generativ AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) och försöka identifiera ett område där du skulle lägga till generativ AI idag som inte har det. Hur skulle påverkan vara annorlunda än att göra det på det "gamla sättet", kan du göra något du inte kunde tidigare, eller är du snabbare? Skriv en sammanfattning på 300 ord om hur din dröm-AI-startup skulle se ut och inkludera rubriker som "Problem", "Hur jag skulle använda AI", "Påverkan" och eventuellt en affärsplan.

Om du gjorde denna uppgift kanske du till och med är redo att ansöka till Microsofts inkubator, [Microsoft för Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) vi erbjuder krediter för både Azure, OpenAI, mentorskap och mycket mer, kolla in det!

## Kunskapskontroll

Vad är sant om stora språkmodeller?

1. Du får exakt samma svar varje gång.
1. Det gör saker perfekt, är bra på att lägga till siffror, producera fungerande kod etc.
1. Svaret kan variera trots att du använder samma prompt. Det är också bra på att ge dig ett första utkast av något, vare sig det är text eller kod. Men du behöver förbättra resultaten.

A: 3, en LLM är icke-deterministisk, svaret varierar, men du kan kontrollera dess variation via en temperaturinställning. Du bör inte heller förvänta dig att den gör saker perfekt, den är här för att göra det tunga lyftet åt dig vilket ofta betyder att du får ett bra första försök på något som du behöver förbättra gradvis.

## Bra jobbat! Fortsätt resan

Efter att ha avslutat denna lektion, kolla in vår [Generativ AI Lärandesamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta höja din kunskap om Generativ AI!

Gå vidare till Lektion 2 där vi kommer att titta på hur man [utforskar och jämför olika LLM-typer](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.