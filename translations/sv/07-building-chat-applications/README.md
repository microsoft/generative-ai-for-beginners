# Bygga Generativa AI-Drivna Chattapplikationer

[![Bygga Generativa AI-Drivna Chattapplikationer](../../../translated_images/sv/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klicka på bilden ovan för att se videon till denna lektion)_

Nu när vi har sett hur vi kan bygga textgenereringsappar, låt oss titta närmare på chattapplikationer.

Chattapplikationer har blivit integrerade i våra dagliga liv och erbjuder mer än bara ett sätt för vardagliga konversationer. De är viktiga delar av kundservice, teknisk support och till och med avancerade rådgivningssystem. Det är troligt att du nyligen fått hjälp från en chattapplikation. När vi integrerar mer avancerad teknik som generativ AI i dessa plattformar ökar komplexiteten och också utmaningarna.

Några frågor vi behöver svar på är:

- **Bygga applikationen**. Hur bygger vi effektivt och integrerar sömlöst dessa AI-drivna applikationer för specifika användningsfall?
- **Övervakning**. När applikationerna är i drift, hur kan vi övervaka och säkerställa att de fungerar på högsta kvalitetsnivå, både vad gäller funktionalitet och efterlevnad av [sex principer för ansvarsfull AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

När vi går vidare in i en era definierad av automation och sömlösa människa-maskin-interaktioner blir det viktigt att förstå hur generativ AI förändrar omfattningen, djupet och anpassningsförmågan hos chattapplikationer. Denna lektion kommer att undersöka arkitekturens aspekter som stödjer dessa komplexa system, fördjupa sig i metoder för finjustering för domänspecifika uppgifter och utvärdera mått och överväganden som är viktiga för att säkerställa ansvarsfull AI-implementering.

## Introduktion

Denna lektion omfattar:

- Tekniker för effektivt byggande och integration av chattapplikationer.
- Hur man tillämpar anpassning och finjustering på applikationer.
- Strategier och överväganden för effektiv övervakning av chattapplikationer.

## Lärandemål

Vid slutet av denna lektion kommer du att kunna:

- Beskriva överväganden för att bygga och integrera chattapplikationer i befintliga system.
- Anpassa chattapplikationer för specifika användningsfall.
- Identifiera viktiga mått och överväganden för att effektivt övervaka och upprätthålla kvaliteten på AI-drivna chattapplikationer.
- Säkerställa att chattapplikationer använder AI på ett ansvarsfullt sätt.

## Integrera Generativ AI i Chattapplikationer

Att förbättra chattapplikationer med generativ AI handlar inte bara om att göra dem smartare; det handlar om att optimera deras arkitektur, prestanda och användargränssnitt för att leverera en kvalitativ användarupplevelse. Detta inkluderar att undersöka arkitektoniska grunder, API-integrationer och användargränssnittsöverväganden. Denna sektion syftar till att erbjuda en omfattande vägkarta för att navigera i dessa komplexa landskap, oavsett om du ansluter dem till befintliga system eller bygger dem som fristående plattformar.

Vid slutet av denna sektion kommer du vara utrustad med den expertis som krävs för att effektivt konstruera och integrera chattapplikationer.

### Chattbot eller Chattapplikation?

Innan vi dyker in i att bygga chattapplikationer, låt oss jämföra 'chattbottar' med 'AI-drivna chattapplikationer', som tjänar skilda roller och funktioner. En chattbots huvudsakliga syfte är att automatisera specifika konversationsuppgifter, såsom att svara på vanliga frågor eller spåra ett paket. Den styrs typiskt av regelbaserad logik eller komplexa AI-algoritmer. I kontrast är en AI-driven chattapplikation en mycket mer omfattande miljö utformad för att möjliggöra olika former av digital kommunikation, såsom text-, röst- och videosamtal mellan mänskliga användare. Dess utmärkande drag är integrationen av en generativ AI-modell som simulerar nyanserade, människoliknande samtal och genererar svar baserade på en mängd olika indata och kontextuella signaler. En generativ AI-driven chattapplikation kan delta i öppna diskussioner, anpassa sig till föränderliga konversationskontexter och till och med producera kreativa eller komplexa dialoger.

Tabellen nedan visar nyckelskillnader och likheter för att hjälpa oss förstå deras unika roller i digital kommunikation.

| Chattbot                               | Generativ AI-Drivna Chattapplikationer |
| ------------------------------------- | -------------------------------------- |
| Uppgiftsfokuserad och regelbaserad    | Konstektmedveten                        |
| Ofta integrerad i större system        | Kan vara värd för en eller flera chattbottar |
| Begränsad till programmerade funktioner | Inkluderar generativa AI-modeller      |
| Specialiserade och strukturerade interaktioner | Kapabel till öppna domän-diskussioner   |

### Utnyttja färdiga funktionaliteter med SDK:er och API:er

När du bygger en chattapplikation är ett utmärkt första steg att utvärdera vad som redan finns. Att använda SDK:er och API:er för att bygga chattapplikationer är en fördelaktig strategi av flera skäl. Genom att integrera väl dokumenterade SDK:er och API:er positionerar du strategiskt din applikation för långsiktig framgång och hanterar frågor kring skalbarhet och underhåll.

- **Påskyndar utvecklingsprocessen och minskar overhead**: Att förlita sig på förbyggda funktioner istället för den dyra processen att bygga dem själv gör att du kan fokusera på andra aspekter av din applikation som du kanske anser viktigare, såsom affärslogik.
- **Bättre prestanda**: När du bygger funktionalitet från grunden kommer du förr eller senare att fråga dig själv "Hur skalar detta? Är denna applikation kapabel att hantera en plötslig användartillströmning?" Väl underhållna SDK:er och API:er har ofta inbyggda lösningar för dessa problem.
- **Enklare underhåll**: Uppdateringar och förbättringar är lättare att hantera eftersom de flesta API:er och SDK:er helt enkelt kräver en uppdatering av biblioteket när en ny version släpps.
- **Tillgång till banbrytande teknik**: Att utnyttja modeller som har finjusterats och tränats på omfattande datamängder ger din applikation naturliga språkförmågor.

Att få tillgång till funktionaliteten i ett SDK eller API innebär vanligtvis att man får tillstånd att använda de tillhandahållna tjänsterna, vilket ofta sker genom användning av en unik nyckel eller autentiseringstoken. Vi kommer att använda OpenAI Python-biblioteket för att utforska hur detta ser ut. Du kan också prova det själv i följande [notebook för OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) eller [notebook för Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) för denna lektion.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Exemplet ovan använder GPT-4o mini-modellen med Responses API för att slutföra prompten, men observera att API-nyckeln är inställd innan det görs. Du skulle få ett fel om du inte satte nyckeln.

## Användarupplevelse (UX)

Allmänna UX-principer gäller för chattapplikationer, men här är några ytterligare överväganden som blir särskilt viktiga på grund av de maskininlärningskomponenter som är involverade.

- **Mekanism för att hantera tvetydighet**: Generativa AI-modeller genererar ibland otydliga svar. En funktion som låter användare fråga om förtydligande kan vara till hjälp om de stöter på detta problem.
- **Behållande av kontext**: Avancerade generativa AI-modeller har förmågan att minnas kontext inom en konversation, vilket kan vara en nödvändig tillgång för användarupplevelsen. Att ge användare möjlighet att kontrollera och hantera kontext förbättrar användarupplevelsen men introducerar risken att behålla känslig användarinformation. Överväganden kring hur länge denna information lagras, som att införa en retention policy, kan balansera behovet av kontext mot integritet.
- **Personalisering**: Med förmågan att lära sig och anpassa sig erbjuder AI-modeller en individuell upplevelse för användaren. Att skräddarsy användarupplevelsen via funktioner som användarprofiler gör inte bara att användaren känner sig förstådd, det hjälper också i att hitta specifika svar och skapar en mer effektiv och tillfredsställande interaktion.

Ett sådant exempel på personalisering är inställningen "Custom instructions" i OpenAI:s ChatGPT. Den tillåter dig att ge information om dig själv som kan vara viktig kontext för dina promptar. Här är ett exempel på en anpassad instruktion.

![Inställningar för Custom Instructions i ChatGPT](../../../translated_images/sv/custom-instructions.b96f59aa69356fcf.webp)

Denna "profil" uppmanar ChatGPT att skapa en lektionsplan för länkade listor. Observera att ChatGPT tar hänsyn till att användaren kan vilja ha en mer djupgående lektionsplan baserat på hennes erfarenhet.

![En prompt i ChatGPT för en lektionsplan om länkade listor](../../../translated_images/sv/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsofts Systemmeddelanderamverk för Stora Språkmodeller

[Microsoft har tillhandahållit riktlinjer](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) för att skriva effektiva systemmeddelanden när man genererar svar från LLM:er, uppdelat i 4 områden:

1. Definiera vem modellen är för, samt dess kapaciteter och begränsningar.
2. Definiera modellens output-format.
3. Ge specifika exempel som visar avsedd beteende för modellen.
4. Ge ytterligare beteendegrindar.

### Tillgänglighet

Oavsett om en användare har syn-, hörsel-, motoriska eller kognitiva nedsättningar ska en väl utformad chattapplikation vara användbar för alla. Följande lista bryter ner specifika funktioner som syftar till att förbättra tillgängligheten för olika användarhinder.

- **Funktioner för synnedsättning**: Teman med hög kontrast och justerbar textstorlek, skärmläsarkompatibilitet.
- **Funktioner för hörselnedsättning**: Text-till-tal och tal-till-text funktioner, visuella signaler för ljudnotiser.
- **Funktioner för motoriska funktionsnedsättningar**: Stöd för tangentbordsnavigering, röstkommandon.
- **Funktioner för kognitiva nedsättningar**: Förenklade språkalternativ.

## Anpassning och finjustering för Domänspecifika Språkmodeller

Föreställ dig en chattapplikation som förstår ditt företags jargong och förutser specifika frågor som användarbasen oftast har. Det finns några tillvägagångssätt värda att nämna:

- **Utnyttja DSL-modeller**. DSL står för domänspecifikt språk. Du kan använda en så kallad DSL-modell tränad på ett specifikt område för att förstå dess begrepp och scenarier.
- **Applicera finjustering**. Finjustering är processen att ytterligare träna din modell med specifik data.

## Anpassning: Använda en DSL

Att utnyttja domänspecifika språkmodeller (DSL-modeller) kan förbättra användarengagemang genom att erbjuda specialiserade, kontextuellt relevanta interaktioner. Det är en modell som tränats eller finjusterats för att förstå och generera text relaterad till ett specifikt fält, bransch eller ämne. Alternativ för att använda en DSL-modell kan variera från att träna en från grunden till att använda befintliga via SDK:er och API:er. Ett annat alternativ är finjustering, vilket innebär att ta en befintlig förtränad modell och anpassa den för ett specifikt domänområde.

## Anpassning: Applicera finjustering

Finjustering övervägs ofta när en förtränad modell inte räcker till inom ett specialiserat område eller för en specifik uppgift.

Till exempel är medicinska frågor komplexa och kräver mycket kontext. När en medicinsk professionell ställer en diagnos baseras det på en rad faktorer som livsstil eller befintliga sjukdomar och kan till och med vara beroende av senaste medicinska tidskrifter för att validera diagnosen. I sådana nyanserade scenarier kan en allmän AI-chattapplikation inte vara en pålitlig källa.

### Scenario: en medicinsk applikation

Tänk på en chattapplikation designad för att assistera medicinska yrkesverksamma genom att tillhandahålla snabba referenser till behandlingsriktlinjer, läkemedelsinteraktioner eller senaste forskningsresultat.

En allmän modell kan vara tillräcklig för att svara på grundläggande medicinska frågor eller ge allmän rådgivning, men den kan ha svårt med följande:

- **Mycket specifika eller komplexa fall**. Till exempel kan en neurolog fråga applikationen, "Vilka är de aktuella bästa metoderna för hantering av läkemedelsresistent epilepsi hos barn?"
- **Brist på senaste framsteg**. En allmän modell kan ha svårt att ge ett aktuellt svar som inkluderar de senaste framstegen inom neurologi och farmakologi.

I sådana fall kan finjustering av modellen med ett specialiserat medicinskt dataset avsevärt förbättra dess förmåga att hantera dessa komplexa medicinska frågor mer exakt och pålitligt. Detta kräver tillgång till en stor och relevant datamängd som representerar domänspecifika utmaningar och frågor som behöver adresseras.

## Överväganden för en Högkvalitativ AI-Drivna Chattupplevelse

Denna sektion beskriver kriterierna för "högkvalitativa" chattapplikationer, vilka inkluderar insamling av handlingsbara mått och efterlevnad av ett ramverk som ansvarsfullt använder AI-teknologi.

### Nyckelmått

För att upprätthålla högkvalitativ prestanda i en applikation är det viktigt att följa nyckelmått och överväganden. Dessa mätningar säkerställer inte bara applikationens funktionalitet utan bedömer även kvaliteten på AI-modellen och användarupplevelsen. Nedan följer en lista som täcker grundläggande, AI- och användarupplevelsemått som bör beaktas.

| Mått                           | Definition                                                                                                            | Överväganden för chapputvecklare                                      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Drifttid**                   | Mäter hur lång tid applikationen är operativ och åtkomlig för användare.                                              | Hur kommer du att minimera driftstopp?                                |
| **Svarstid**                   | Den tid det tar för applikationen att svara på en användares fråga.                                                   | Hur kan du optimera frågebehandlingen för att förbättra svarstiden?   |
| **Precision**                  | Andelen sanna positiva förutsägelser i relation till totalt antal positiva förutsägelser                             | Hur kommer du validera precisionen i din modell?                      |
| **Recall (Känslighet)**        | Andelen sanna positiva förutsägelser i förhållande till det faktiska antalet positiva fall                            | Hur kommer du mäta och förbättra recall?                             |
| **F1-Score**                  | Det harmoniska medelvärdet av precision och recall, som balanserar avvägningen mellan båda.                           | Vad är din målsatta F1-score? Hur ska du balansera precision och recall? |
| **Perplexity**                 | Mäter hur väl sannolikhetsfördelningen som förutsägs av modellen överensstämmer med den faktiska fördelningen av data. | Hur kommer du minimera perplexity?                                     |
| **Användartillfredsställelse** | Mäter användarens uppfattning om applikationen. Ofta insamlad via undersökningar.                                     | Hur ofta kommer du samla in användarfeedback? Hur kommer du anpassa baserat på den? |
| **Felaktivitet**              | Hastigheten med vilken modellen gör misstag i förståelse eller output.                                               | Vilka strategier har du för att minska felaktighetsfrekvensen?        |
| **Omträningcykler**           | Hur ofta modellen uppdateras för att inkludera ny data och insikter.                                                | Hur ofta kommer du träna om modellen? Vad triggar en omträningcykel?  |

| **Avvikelsedetektering**         | Verktyg och tekniker för att identifiera ovanliga mönster som inte överensstämmer med förväntat beteende.                        | Hur kommer du att reagera på avvikelser?                                        |

### Implementering av Ansvarsfull AI i chattapplikationer

Microsofts syn på Ansvarsfull AI har identifierat sex principer som bör vägleda AI-utveckling och användning. Nedan följer principerna, deras definition och saker som en chattutvecklare bör överväga samt varför dessa bör tas på allvar.

| Principer             | Microsofts definition                                | Överväganden för chattutvecklare                                      | Varför det är viktigt                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Rättvisa               | AI-system ska behandla alla människor rättvist.            | Säkerställ att chattapplikationen inte diskriminerar baserat på användardata.  | För att bygga förtroende och inkludering bland användare; undviker juridiska följder.    |
| Tillförlitlighet och Säkerhet | AI-system ska fungera tillförlitligt och säkert.        | Genomför tester och felsäkerheter för att minimera fel och risker.         | Säkerställer användarnöjdhet och förhindrar potentiell skada.                            |
| Integritet och Säkerhet   | AI-system ska vara säkra och respektera integriteten.      | Implementera stark kryptering och dataskyddsåtgärder.              | För att skydda känsliga användardata och följa integritetslagar.                        |
| Inkludering          | AI-system ska stärka alla och engagera människor. | Designa UI/UX som är tillgängligt och lättanvänt för olika målgrupper. | Säkerställer att en bredare publik kan använda applikationen effektivt.                 |
| Transparens           | AI-system ska vara begripliga.                  | Ge tydlig dokumentation och förklaringar för AI:s svar.            | Användare är mer benägna att lita på ett system om de kan förstå hur beslut fattas.    |
| Ansvarsskyldighet         | Människor ska vara ansvariga för AI-system.          | Etablera en tydlig process för granskning och förbättring av AI-beslut.     | Möjliggör kontinuerliga förbättringar och korrigerande åtgärder vid misstag.          |

## Uppgift

Se [assignment](../../../07-building-chat-applications/python). Den tar dig igenom en serie övningar från att köra dina första chattpromptar, till klassificering och sammanfattning av text och mer. Observera att uppgifterna finns tillgängliga i olika programmeringsspråk!

## Bra jobbat! Fortsätt resan

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom generativ AI!

Gå över till Lektion 8 för att se hur du kan börja [bygga sökapplikationer](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->