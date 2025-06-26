<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2f686f2eb794941761252ac5e8e090b",
  "translation_date": "2025-06-25T10:44:01+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "sv"
}
-->
# Utforska och jämföra olika LLMs

[![Utforska och jämföra olika LLMs](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.sv.png)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _Klicka på bilden ovan för att se videon av denna lektion_

I den tidigare lektionen såg vi hur Generativ AI förändrar tekniklandskapet, hur stora språkmodeller (LLMs) fungerar och hur ett företag - som vår startup - kan tillämpa dem på sina användningsfall och växa! I detta kapitel kommer vi att jämföra och kontrastera olika typer av stora språkmodeller (LLMs) för att förstå deras fördelar och nackdelar.

Nästa steg i vår startups resa är att utforska det aktuella landskapet av LLMs och förstå vilka som är lämpliga för vårt användningsfall.

## Introduktion

Denna lektion kommer att täcka:

- Olika typer av LLMs i det nuvarande landskapet.
- Testa, iterera och jämföra olika modeller för ditt användningsfall i Azure.
- Hur man distribuerar en LLM.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Välja rätt modell för ditt användningsfall.
- Förstå hur man testar, itererar och förbättrar modellens prestanda.
- Veta hur företag distribuerar modeller.

## Förstå olika typer av LLMs

LLMs kan ha flera kategoriseringar baserade på deras arkitektur, träningsdata och användningsfall. Att förstå dessa skillnader hjälper vår startup att välja rätt modell för scenariot och förstå hur man testar, itererar och förbättrar prestanda.

Det finns många olika typer av LLM-modeller, ditt val av modell beror på vad du avser att använda dem för, din data, hur mycket du är beredd att betala och mer.

Beroende på om du avser att använda modellerna för text, ljud, video, bildgenerering och så vidare, kan du välja en annan typ av modell.

- **Ljud och taligenkänning**. För detta ändamål är Whisper-typ modeller ett utmärkt val eftersom de är allmänna och inriktade på taligenkänning. De är tränade på olika ljud och kan utföra flerspråkig taligenkänning. Läs mer om [Whisper-typ modeller här](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Bildgenerering**. För bildgenerering är DALL-E och Midjourney två mycket välkända val. DALL-E erbjuds av Azure OpenAI. [Läs mer om DALL-E här](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) och även i kapitel 9 av denna läroplan.

- **Textgenerering**. De flesta modeller är tränade på textgenerering och du har ett stort urval av val från GPT-3.5 till GPT-4. De kommer till olika kostnader med GPT-4 som den dyraste. Det är värt att titta på [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) för att utvärdera vilka modeller som bäst passar dina behov när det gäller kapacitet och kostnad.

- **Multi-modality**. Om du letar efter att hantera flera typer av data i input och output, kan du vilja titta på modeller som [gpt-4 turbo med vision eller gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - de senaste versionerna av OpenAI-modeller - som är kapabla att kombinera naturlig språkbehandling med visuell förståelse, vilket möjliggör interaktioner genom multimodala gränssnitt.

Att välja en modell innebär att du får vissa grundläggande kapaciteter, men de kanske inte är tillräckliga. Ofta har du företagsspecifik data som du på något sätt behöver informera LLM om. Det finns några olika val på hur man kan närma sig detta, mer om det i de kommande avsnitten.

### Foundation Models versus LLMs

Termen Foundation Model myntades av [Stanford-forskare](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) och definieras som en AI-modell som följer vissa kriterier, såsom:

- **De tränas med osupervised learning eller självövervakad inlärning**, vilket innebär att de tränas på oetiketterad multimodal data och de kräver inte mänsklig annotering eller etikettering av data för sin träningsprocess.
- **De är mycket stora modeller**, baserade på mycket djupa neurala nätverk tränade på miljarder parametrar.
- **De är normalt avsedda att tjäna som en 'grund' för andra modeller**, vilket innebär att de kan användas som en utgångspunkt för att bygga andra modeller ovanpå, vilket kan göras genom finjustering.

![Foundation Models versus LLMs](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.sv.png)

Bildkälla: [Essential Guide to Foundation Models and Large Language Models | av Babar M Bhatti | Medium](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

För att ytterligare klargöra denna skillnad, låt oss ta ChatGPT som exempel. För att bygga den första versionen av ChatGPT tjänade en modell kallad GPT-3.5 som grundmodell. Detta betyder att OpenAI använde vissa chattspecifika data för att skapa en justerad version av GPT-3.5 som var specialiserad på att prestera väl i konversationsscenarier, såsom chattbottar.

![Foundation Model](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.sv.png)

Bildkälla: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Öppen källkod versus Proprietära modeller

Ett annat sätt att kategorisera LLMs är om de är öppen källkod eller proprietära.

Öppen källkod modeller är modeller som görs tillgängliga för allmänheten och kan användas av vem som helst. De görs ofta tillgängliga av företaget som skapade dem, eller av forskarsamhället. Dessa modeller får inspekteras, modifieras och anpassas för de olika användningsfallen i LLMs. De är dock inte alltid optimerade för produktionsanvändning och kanske inte är lika presterande som proprietära modeller. Dessutom kan finansiering för öppen källkod modeller vara begränsad, och de kanske inte underhålls långsiktigt eller uppdateras med den senaste forskningen. Exempel på populära öppen källkod modeller inkluderar [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) och [LLaMA](https://llama.meta.com).

Proprietära modeller är modeller som ägs av ett företag och inte görs tillgängliga för allmänheten. Dessa modeller är ofta optimerade för produktionsanvändning. De får dock inte inspekteras, modifieras eller anpassas för olika användningsfall. Dessutom är de inte alltid tillgängliga gratis och kan kräva en prenumeration eller betalning för att använda. Användare har inte heller kontroll över de data som används för att träna modellen, vilket innebär att de måste lita på modellägaren för att säkerställa åtagande till datasekretess och ansvarsfull användning av AI. Exempel på populära proprietära modeller inkluderar [OpenAI modeller](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) eller [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Inbäddning versus Bildgenerering versus Text- och Kodgenerering

LLMs kan också kategoriseras efter den output de genererar.

Inbäddningar är en uppsättning modeller som kan omvandla text till en numerisk form, kallad inbäddning, vilket är en numerisk representation av inmatningstexten. Inbäddningar gör det enklare för maskiner att förstå relationerna mellan ord eller meningar och kan konsumeras som input av andra modeller, såsom klassificeringsmodeller eller klustermodeller som har bättre prestanda på numerisk data. Inbäddningsmodeller används ofta för transfer learning, där en modell byggs för en surrogatuppgift för vilken det finns en överflöd av data, och sedan återanvänds modellvikterna (inbäddningarna) för andra nedströmsuppgifter. Ett exempel på denna kategori är [OpenAI inbäddningar](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Inbäddning](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.sv.png)

Bildgenereringsmodeller är modeller som genererar bilder. Dessa modeller används ofta för bildredigering, bildsyntes och bildöversättning. Bildgenereringsmodeller tränas ofta på stora dataset av bilder, såsom [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), och kan användas för att generera nya bilder eller för att redigera befintliga bilder med tekniker för inpainting, superupplösning och färgläggning. Exempel inkluderar [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) och [Stable Diffusion modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Bildgenerering](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.sv.png)

Text- och kodgenereringsmodeller är modeller som genererar text eller kod. Dessa modeller används ofta för textsammanfattning, översättning och frågehantering. Textgenereringsmodeller tränas ofta på stora dataset av text, såsom [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), och kan användas för att generera ny text eller för att svara på frågor. Kodgenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), tränas ofta på stora dataset av kod, såsom GitHub, och kan användas för att generera ny kod eller för att fixa buggar i befintlig kod.

![Text och kodgenerering](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.sv.png)

### Encoder-Decoder versus Endast Decoder

För att prata om de olika typerna av arkitekturer för LLMs, låt oss använda en analogi.

Föreställ dig att din chef gav dig en uppgift att skriva ett quiz för studenterna. Du har två kollegor; en ansvarar för att skapa innehållet och den andra ansvarar för att granska dem.

Innehållsskaparen är som en Endast Decoder-modell, de kan titta på ämnet och se vad du redan har skrivit och sedan kan han skriva en kurs baserat på det. De är mycket bra på att skriva engagerande och informativt innehåll, men de är inte särskilt bra på att förstå ämnet och inlärningsmålen. Några exempel på Decoder-modeller är GPT-familjens modeller, såsom GPT-3.

Granskaren är som en Endast Encoder-modell, de tittar på den skrivna kursen och svaren, märker relationen mellan dem och förstår sammanhanget, men de är inte bra på att generera innehåll. Ett exempel på Endast Encoder-modell skulle vara BERT.

Föreställ dig att vi också kan ha någon som både kan skapa och granska quizet, detta är en Encoder-Decoder-modell. Några exempel skulle vara BART och T5.

### Tjänst versus Modell

Nu, låt oss prata om skillnaden mellan en tjänst och en modell. En tjänst är en produkt som erbjuds av en molntjänstleverantör och är ofta en kombination av modeller, data och andra komponenter. En modell är kärnkomponenten i en tjänst och är ofta en grundmodell, såsom en LLM.

Tjänster är ofta optimerade för produktionsanvändning och är ofta lättare att använda än modeller, via ett grafiskt användargränssnitt. Tjänster är dock inte alltid tillgängliga gratis och kan kräva en prenumeration eller betalning för att använda, i utbyte mot att utnyttja tjänsteägarens utrustning och resurser, optimera kostnader och skala enkelt. Ett exempel på en tjänst är [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), som erbjuder en pay-as-you-go-prisplan, vilket innebär att användare debiteras proportionellt till hur mycket de använder tjänsten. Dessutom erbjuder Azure OpenAI Service säkerhet i företagsklass och en ansvarsfull AI-ram ovanpå modellernas kapaciteter.

Modeller är bara det neurala nätverket, med parametrarna, vikterna och andra. Det tillåter företag att köra lokalt, men skulle behöva köpa utrustning, bygga en struktur för att skala och köpa en licens eller använda en öppen källkod modell. En modell som LLaMA är tillgänglig att använda, vilket kräver beräkningskraft för att köra modellen.

## Hur man testar och itererar med olika modeller för att förstå prestanda på Azure

När vårt team har utforskat det nuvarande LLMs-landskapet och identifierat några bra kandidater för deras scenarier, är nästa steg att testa dem på deras data och deras arbetsbelastning. Detta är en iterativ process, gjord genom experiment och mätningar. De flesta av de modeller vi nämnde i tidigare stycken (OpenAI-modeller, öppen källkod modeller som Llama2 och Hugging Face-transformatorer) finns tillgängliga i [Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) i [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) är en molnplattform designad för utvecklare att bygga generativa AI-applikationer och hantera hela utvecklingslivscykeln - från experiment till utvärdering - genom att kombinera alla Azure AI-tjänster i ett enda nav med ett praktiskt GUI. Modellkatalogen i Azure AI Studio gör det möjligt för användaren att:

- Hitta den Foundation Model av intresse i katalogen - antingen proprietär eller öppen källkod, filtrera efter uppgift, licens eller namn. För att förbättra sökbarheten är modellerna organiserade i samlingar, som Azure OpenAI-samling, Hugging Face-samling och mer.

![Model catalog](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.sv.png)

- Granska modellkortet, inklusive en detaljerad beskrivning av avsedd användning och träningsdata, kodexempel och utvärderingsresultat i det interna utvärderingsbiblioteket.

![Model card](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.sv.png)
- Jämför benchmarks mellan modeller och dataset som finns tillgängliga i branschen för att bedöma vilken som uppfyller affärsscenariot, genom [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) panelen.

![Model benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.sv.png)

- Finjustera modellen på anpassad träningsdata för att förbättra modellens prestanda i en specifik arbetsbelastning, med hjälp av experimentering och spårningsfunktioner i Azure AI Studio.

![Model fine-tuning](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.sv.png)

- Distribuera den ursprungliga förtränade modellen eller den finjusterade versionen till en fjärrbaserad realtidsinferens - hanterad beräkning - eller serverlös API-endpunkt - [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - för att möjliggöra applikationer att använda den.

![Model deployment](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.sv.png)

> [!NOTE]
> Alla modeller i katalogen är för närvarande inte tillgängliga för finjustering och/eller pay-as-you-go distribution. Kontrollera modellkortet för detaljer om modellens kapaciteter och begränsningar.

## Förbättra LLM-resultat

Vi har tillsammans med vårt startupteam utforskat olika typer av LLMs och en molnplattform (Azure Machine Learning) som gör det möjligt för oss att jämföra olika modeller, utvärdera dem på testdata, förbättra prestanda och distribuera dem på inferensendpunkter.

Men när ska de överväga att finjustera en modell istället för att använda en förtränad? Finns det andra metoder för att förbättra modellens prestanda på specifika arbetsbelastningar?

Det finns flera metoder som ett företag kan använda för att få de resultat de behöver från en LLM. Du kan välja olika typer av modeller med olika grader av träning när du distribuerar en LLM i produktion, med olika nivåer av komplexitet, kostnad och kvalitet. Här är några olika metoder:

- **Promptteknik med kontext**. Idén är att ge tillräckligt med kontext när du ger en prompt för att säkerställa att du får de svar du behöver.

- **Retrieval Augmented Generation, RAG**. Dina data kan finnas i en databas eller webbendpunkt, till exempel, för att säkerställa att dessa data, eller en delmängd av dem, inkluderas vid tidpunkten för prompten, kan du hämta de relevanta data och göra dem till en del av användarens prompt.

- **Finjusterad modell**. Här har du tränat modellen ytterligare på dina egna data vilket har lett till att modellen blir mer exakt och svarar bättre på dina behov men kan vara kostsamt.

![LLMs deployment](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.sv.png)

Bildkälla: [Fyra sätt som företag distribuerar LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Promptteknik med kontext

Förtränade LLMs fungerar mycket bra på generaliserade naturliga språkuppgifter, även genom att kalla dem med en kort prompt, som en mening att slutföra eller en fråga – det så kallade “zero-shot” lärandet.

Men ju mer användaren kan rama in sin fråga, med en detaljerad begäran och exempel – kontexten – desto mer exakt och närmare användarens förväntningar kommer svaret att vara. I detta fall pratar vi om “one-shot” lärande om prompten innehåller endast ett exempel och “few-shot learning” om det innehåller flera exempel.
Promptteknik med kontext är det mest kostnadseffektiva sättet att komma igång.

### Retrieval Augmented Generation (RAG)

LLMs har begränsningen att de endast kan använda data som har använts under deras träning för att generera ett svar. Detta innebär att de inte vet något om fakta som inträffat efter deras träningsprocess, och de kan inte komma åt icke-offentlig information (som företagsdata).
Detta kan övervinnas genom RAG, en teknik som förstärker prompten med extern data i form av dokumentdelar, med hänsyn till promptens längdgränser. Detta stöds av verktyg för vektordatabaser (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) som hämtar de användbara delarna från varierade fördefinierade datakällor och lägger till dem i promptens kontext.

Denna teknik är mycket hjälpsam när ett företag inte har tillräckligt med data, tillräckligt med tid eller resurser för att finjustera en LLM, men ändå önskar förbättra prestanda på en specifik arbetsbelastning och minska riskerna för fabriceringar, dvs. mystifikation av verkligheten eller skadligt innehåll.

### Finjusterad modell

Finjustering är en process som utnyttjar transferlärande för att 'anpassa' modellen till en nedströmsuppgift eller för att lösa ett specifikt problem. Till skillnad från få-skott lärande och RAG resulterar det i en ny modell som genereras, med uppdaterade vikter och fördomar. Det kräver en uppsättning träningsexempel som består av ett enda input (prompten) och dess associerade output (slutförandet).
Detta skulle vara den föredragna metoden om:

- **Använda finjusterade modeller**. Ett företag skulle vilja använda finjusterade mindre kapabla modeller (som inbäddningsmodeller) istället för högpresterande modeller, vilket resulterar i en mer kostnadseffektiv och snabb lösning.

- **Beakta latens**. Latens är viktig för ett specifikt användningsfall, så det är inte möjligt att använda mycket långa promptar eller antalet exempel som bör läras av modellen passar inte med promptens längdgräns.

- **Hålla sig uppdaterad**. Ett företag har mycket högkvalitativa data och grundsanning etiketter och de resurser som krävs för att hålla dessa data uppdaterade över tid.

### Tränad modell

Att träna en LLM från grunden är utan tvekan det mest svåra och mest komplexa tillvägagångssättet att anta, vilket kräver massiva mängder data, skickliga resurser och lämplig beräkningskraft. Detta alternativ bör endast övervägas i ett scenario där ett företag har ett domänspecifikt användningsfall och en stor mängd domäncentrerade data.

## Kunskapskontroll

Vad kan vara en bra metod för att förbättra LLM-slutföringsresultat?

1. Promptteknik med kontext
1. RAG
1. Finjusterad modell

A:3, om du har tid och resurser och högkvalitativa data är finjustering det bättre alternativet för att hålla sig uppdaterad. Men om du tittar på att förbättra saker och du saknar tid är det värt att överväga RAG först.

## 🚀 Utmaning

Läs mer om hur du kan [använda RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) för ditt företag.

## Bra arbete, fortsätt din lärande

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta öka din kunskap om generativ AI!

Gå vidare till Lektion 3 där vi kommer att titta på hur man [bygger med generativ AI ansvarsfullt](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi är inte ansvariga för eventuella missförstånd eller feltolkningar som uppstår vid användningen av denna översättning.