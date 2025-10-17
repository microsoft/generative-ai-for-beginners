<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T19:01:28+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "sv"
}
-->
# Utforska och jämför olika LLM:er

[![Utforska och jämför olika LLM:er](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.sv.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klicka på bilden ovan för att se videon av denna lektion_

I den föregående lektionen såg vi hur Generativ AI förändrar tekniklandskapet, hur stora språkmodeller (LLM:er) fungerar och hur ett företag - som vår startup - kan tillämpa dem på sina användningsområden och växa! I detta kapitel ska vi jämföra och kontrastera olika typer av stora språkmodeller (LLM:er) för att förstå deras för- och nackdelar.

Nästa steg i vår startups resa är att utforska det aktuella landskapet för LLM:er och förstå vilka som är lämpliga för vårt användningsområde.

## Introduktion

Denna lektion kommer att täcka:

- Olika typer av LLM:er i det aktuella landskapet.
- Testa, iterera och jämföra olika modeller för ditt användningsområde i Azure.
- Hur man distribuerar en LLM.

## Lärandemål

Efter att ha avslutat denna lektion kommer du att kunna:

- Välja rätt modell för ditt användningsområde.
- Förstå hur man testar, itererar och förbättrar modellens prestanda.
- Veta hur företag distribuerar modeller.

## Förstå olika typer av LLM:er

LLM:er kan kategoriseras på olika sätt baserat på deras arkitektur, träningsdata och användningsområde. Att förstå dessa skillnader hjälper vår startup att välja rätt modell för scenariot och förstå hur man testar, itererar och förbättrar prestandan.

Det finns många olika typer av LLM-modeller, och ditt val av modell beror på vad du vill använda dem till, din data, hur mycket du är beredd att betala och mer.

Beroende på om du vill använda modellerna för text, ljud, video, bildgenerering och så vidare, kan du välja en annan typ av modell.

- **Ljud- och taligenkänning**. För detta ändamål är modeller av typen Whisper ett utmärkt val eftersom de är allmänna och inriktade på taligenkänning. De är tränade på varierande ljud och kan utföra flerspråkig taligenkänning. Läs mer om [Whisper-modeller här](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Bildgenerering**. För bildgenerering är DALL-E och Midjourney två mycket välkända val. DALL-E erbjuds av Azure OpenAI. [Läs mer om DALL-E här](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) och även i kapitel 9 av denna kurs.

- **Textgenerering**. De flesta modeller är tränade för textgenerering och det finns ett stort urval från GPT-3.5 till GPT-4. De har olika kostnader, där GPT-4 är den dyraste. Det är värt att titta på [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) för att utvärdera vilka modeller som bäst passar dina behov när det gäller kapacitet och kostnad.

- **Multimodalitet**. Om du vill hantera flera typer av data i in- och utmatning kan du vilja titta på modeller som [gpt-4 turbo med vision eller gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - de senaste versionerna av OpenAI-modeller - som kan kombinera naturlig språkbehandling med visuell förståelse och möjliggöra interaktioner genom multimodala gränssnitt.

Att välja en modell innebär att du får vissa grundläggande funktioner, men det kanske inte räcker. Ofta har du företagsspecifik data som du på något sätt behöver informera LLM:en om. Det finns några olika sätt att närma sig detta, mer om det i kommande avsnitt.

### Grundmodeller kontra LLM:er

Begreppet Grundmodell myntades av [forskare vid Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) och definieras som en AI-modell som uppfyller vissa kriterier, såsom:

- **De tränas med hjälp av osupervised learning eller självövervakad inlärning**, vilket innebär att de tränas på oetiketterad multimodal data och inte kräver mänsklig annotering eller etikettering av data för sin träningsprocess.
- **De är mycket stora modeller**, baserade på mycket djupa neurala nätverk tränade på miljarder parametrar.
- **De är normalt avsedda att fungera som en "grund" för andra modeller**, vilket innebär att de kan användas som utgångspunkt för att bygga andra modeller ovanpå, vilket kan göras genom finjustering.

![Grundmodeller kontra LLM:er](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.sv.png)

Bildkälla: [Essential Guide to Foundation Models and Large Language Models | av Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

För att ytterligare klargöra denna skillnad, låt oss ta ChatGPT som exempel. För att bygga den första versionen av ChatGPT användes en modell som heter GPT-3.5 som grundmodell. Detta innebär att OpenAI använde viss chatt-specifik data för att skapa en finjusterad version av GPT-3.5 som var specialiserad på att prestera bra i konversationsscenarier, såsom chatbotar.

![Grundmodell](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.sv.png)

Bildkälla: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Öppen källkod kontra Proprietära modeller

Ett annat sätt att kategorisera LLM:er är om de är öppen källkod eller proprietära.

Modeller med öppen källkod är modeller som görs tillgängliga för allmänheten och kan användas av vem som helst. De görs ofta tillgängliga av företaget som skapade dem eller av forskarsamhället. Dessa modeller får inspekteras, modifieras och anpassas för olika användningsområden inom LLM:er. Dock är de inte alltid optimerade för produktionsanvändning och kanske inte är lika presterande som proprietära modeller. Dessutom kan finansiering för modeller med öppen källkod vara begränsad, och de kanske inte underhålls långsiktigt eller uppdateras med den senaste forskningen. Exempel på populära modeller med öppen källkod inkluderar [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) och [LLaMA](https://llama.meta.com).

Proprietära modeller är modeller som ägs av ett företag och inte görs tillgängliga för allmänheten. Dessa modeller är ofta optimerade för produktionsanvändning. Dock får de inte inspekteras, modifieras eller anpassas för olika användningsområden. Dessutom är de inte alltid tillgängliga gratis och kan kräva en prenumeration eller betalning för att användas. Användare har heller inte kontroll över den data som används för att träna modellen, vilket innebär att de måste lita på att modellägaren säkerställer datasekretess och ansvarsfull användning av AI. Exempel på populära proprietära modeller inkluderar [OpenAI-modeller](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) eller [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Inbäddning kontra Bildgenerering kontra Text- och kodgenerering

LLM:er kan också kategoriseras efter den output de genererar.

Inbäddningar är en uppsättning modeller som kan konvertera text till en numerisk form, kallad inbäddning, vilket är en numerisk representation av den inmatade texten. Inbäddningar gör det enklare för maskiner att förstå relationer mellan ord eller meningar och kan användas som indata av andra modeller, såsom klassificeringsmodeller eller klustermodeller som har bättre prestanda på numerisk data. Inbäddningsmodeller används ofta för transfer learning, där en modell byggs för en surrogatuppgift för vilken det finns gott om data, och sedan återanvänds modellvikterna (inbäddningarna) för andra nedströmsuppgifter. Ett exempel på denna kategori är [OpenAI inbäddningar](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Inbäddning](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.sv.png)

Bildgenereringsmodeller är modeller som genererar bilder. Dessa modeller används ofta för bildredigering, bildsyntes och bildöversättning. Bildgenereringsmodeller tränas ofta på stora dataset av bilder, såsom [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), och kan användas för att generera nya bilder eller redigera befintliga bilder med tekniker som inpainting, superupplösning och färgläggning. Exempel inkluderar [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) och [Stable Diffusion-modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Bildgenerering](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.sv.png)

Text- och kodgenereringsmodeller är modeller som genererar text eller kod. Dessa modeller används ofta för textsammanfattning, översättning och frågesvar. Textgenereringsmodeller tränas ofta på stora dataset av text, såsom [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), och kan användas för att generera ny text eller svara på frågor. Kodgenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), tränas ofta på stora dataset av kod, såsom GitHub, och kan användas för att generera ny kod eller fixa buggar i befintlig kod.

![Text- och kodgenerering](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.sv.png)

### Encoder-Decoder kontra Endast Decoder

För att prata om de olika typerna av arkitekturer för LLM:er, låt oss använda en analogi.

Föreställ dig att din chef ger dig i uppdrag att skriva ett quiz för studenterna. Du har två kollegor; en ansvarar för att skapa innehållet och den andra för att granska det.

Innehållsskaparen är som en modell med endast Decoder, de kan titta på ämnet och se vad du redan har skrivit och sedan skriva en kurs baserat på det. De är mycket bra på att skriva engagerande och informativt innehåll, men de är inte särskilt bra på att förstå ämnet och lärandemålen. Några exempel på Decoder-modeller är GPT-familjemodeller, såsom GPT-3.

Granskaren är som en modell med endast Encoder, de tittar på den skrivna kursen och svaren, märker relationen mellan dem och förstår sammanhanget, men de är inte bra på att generera innehåll. Ett exempel på en modell med endast Encoder skulle vara BERT.

Föreställ dig att vi också kan ha någon som både kan skapa och granska quizet, detta är en Encoder-Decoder-modell. Några exempel skulle vara BART och T5.

### Tjänst kontra Modell

Nu ska vi prata om skillnaden mellan en tjänst och en modell. En tjänst är en produkt som erbjuds av en molntjänstleverantör och är ofta en kombination av modeller, data och andra komponenter. En modell är kärnkomponenten i en tjänst och är ofta en grundmodell, såsom en LLM.

Tjänster är ofta optimerade för produktionsanvändning och är ofta enklare att använda än modeller, via ett grafiskt användargränssnitt. Dock är tjänster inte alltid tillgängliga gratis och kan kräva en prenumeration eller betalning för att användas, i utbyte mot att utnyttja tjänsteägarens utrustning och resurser, optimera kostnader och skala enkelt. Ett exempel på en tjänst är [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), som erbjuder en betalningsplan baserad på användning, vilket innebär att användare debiteras proportionellt till hur mycket de använder tjänsten. Dessutom erbjuder Azure OpenAI Service säkerhet på företagsnivå och en ansvarsfull AI-ram ovanpå modellernas kapacitet.

Modeller är bara det neurala nätverket, med parametrar, vikter och annat. Detta gör det möjligt för företag att köra lokalt, men skulle kräva att köpa utrustning, bygga en struktur för att skala och köpa en licens eller använda en modell med öppen källkod. En modell som LLaMA är tillgänglig att använda, vilket kräver beräkningskraft för att köra modellen.

## Hur man testar och itererar med olika modeller för att förstå prestanda i Azure

När vårt team har utforskat det aktuella LLM-landskapet och identifierat några bra kandidater för sina scenarier, är nästa steg att testa dem på deras data och arbetsbelastning. Detta är en iterativ process som görs genom experiment och mätningar.
De flesta av modellerna vi nämnde i tidigare stycken (OpenAI-modeller, öppna källkodsmodeller som Llama2 och Hugging Face transformers) finns tillgängliga i [Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) i [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) är en molnplattform utformad för utvecklare att bygga generativa AI-applikationer och hantera hela utvecklingslivscykeln - från experimentering till utvärdering - genom att kombinera alla Azure AI-tjänster i en enda hub med ett användarvänligt gränssnitt. Model Catalog i Azure AI Studio gör det möjligt för användaren att:

- Hitta den Foundation Model som är av intresse i katalogen - antingen proprietär eller öppen källkod, filtrera efter uppgift, licens eller namn. För att förbättra sökbarheten är modellerna organiserade i samlingar, som Azure OpenAI-samlingen, Hugging Face-samlingen och fler.

![Model catalog](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.sv.png)

- Granska modellkortet, inklusive en detaljerad beskrivning av avsedd användning och träningsdata, kodexempel och utvärderingsresultat från det interna utvärderingsbiblioteket.

![Model card](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.sv.png)

- Jämföra benchmarks mellan modeller och dataset som finns tillgängliga i branschen för att bedöma vilken som bäst uppfyller affärsscenariot, via [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)-panelen.

![Model benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.sv.png)

- Finjustera modellen med anpassad träningsdata för att förbättra modellens prestanda i en specifik arbetsbelastning, med hjälp av experimenterings- och spårningsfunktionerna i Azure AI Studio.

![Model fine-tuning](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.sv.png)

- Distribuera den ursprungliga förtränade modellen eller den finjusterade versionen till en fjärrbaserad realtidsinferens - hanterad beräkning - eller serverlös API-slutpunkt - [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - för att möjliggöra att applikationer kan använda den.

![Model deployment](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.sv.png)

> [!NOTE]
> Alla modeller i katalogen är för närvarande inte tillgängliga för finjustering och/eller pay-as-you-go-distribution. Kontrollera modellkortet för detaljer om modellens kapabiliteter och begränsningar.

## Förbättra LLM-resultat

Vi har tillsammans med vårt startup-team utforskat olika typer av LLM:er och en molnplattform (Azure Machine Learning) som gör det möjligt för oss att jämföra olika modeller, utvärdera dem på testdata, förbättra prestanda och distribuera dem på inferensslutpunkter.

Men när bör de överväga att finjustera en modell istället för att använda en förtränad? Finns det andra metoder för att förbättra modellens prestanda för specifika arbetsbelastningar?

Det finns flera metoder som ett företag kan använda för att få de resultat de behöver från en LLM. Du kan välja olika typer av modeller med olika grader av träning när du distribuerar en LLM i produktion, med olika nivåer av komplexitet, kostnad och kvalitet. Här är några olika metoder:

- **Prompt engineering med kontext**. Idén är att ge tillräckligt med kontext när du ställer en fråga för att säkerställa att du får de svar du behöver.

- **Retrieval Augmented Generation, RAG**. Din data kan finnas i en databas eller webbtjänst, till exempel, för att säkerställa att denna data, eller en del av den, inkluderas vid tidpunkten för frågan, kan du hämta relevant data och göra den till en del av användarens fråga.

- **Finjusterad modell**. Här tränar du modellen vidare på din egen data vilket gör att modellen blir mer exakt och anpassad till dina behov, men det kan vara kostsamt.

![LLMs deployment](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.sv.png)

Bildkälla: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering med Kontext

Förtränade LLM:er fungerar mycket bra på generella naturliga språkuppgifter, även när de används med en kort fråga, som en mening att komplettera eller en fråga – det så kallade "zero-shot"-lärandet.

Men ju mer användaren kan formulera sin fråga, med en detaljerad begäran och exempel – Kontexten – desto mer exakt och närmare användarens förväntningar blir svaret. I detta fall talar vi om "one-shot"-lärande om frågan innehåller endast ett exempel och "few-shot"-lärande om den innehåller flera exempel. Prompt engineering med kontext är det mest kostnadseffektiva sättet att börja med.

### Retrieval Augmented Generation (RAG)

LLM:er har begränsningen att de endast kan använda den data som har använts under deras träning för att generera ett svar. Detta innebär att de inte vet något om fakta som inträffat efter deras träningsprocess, och de kan inte komma åt icke-offentlig information (som företagsdata).
Detta kan övervinnas genom RAG, en teknik som förstärker frågan med extern data i form av dokumentfragment, med hänsyn till begränsningar i frågelängd. Detta stöds av verktyg för vektordatabaser (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) som hämtar användbara fragment från olika fördefinierade datakällor och lägger till dem i frågans kontext.

Denna teknik är mycket användbar när ett företag inte har tillräckligt med data, tid eller resurser för att finjustera en LLM, men ändå vill förbättra prestanda för en specifik arbetsbelastning och minska risken för fabriceringar, dvs. förvrängning av verkligheten eller skadligt innehåll.

### Finjusterad modell

Finjustering är en process som utnyttjar transfer learning för att "anpassa" modellen till en nedströmsuppgift eller för att lösa ett specifikt problem. Till skillnad från few-shot-lärande och RAG resulterar det i en ny modell som genereras, med uppdaterade vikter och förskjutningar. Det kräver en uppsättning träningsexempel bestående av en enda input (frågan) och dess associerade output (slutförandet).
Detta skulle vara den föredragna metoden om:

- **Använda finjusterade modeller**. Ett företag vill använda finjusterade mindre kapabla modeller (som inbäddningsmodeller) istället för högpresterande modeller, vilket resulterar i en mer kostnadseffektiv och snabb lösning.

- **Beakta latens**. Latens är viktigt för ett specifikt användningsfall, så det är inte möjligt att använda mycket långa frågor eller antalet exempel som modellen ska lära sig från passar inte med frågelängdsbegränsningen.

- **Hålla sig uppdaterad**. Ett företag har mycket högkvalitativ data och sanningsenliga etiketter samt de resurser som krävs för att hålla denna data uppdaterad över tid.

### Tränad modell

Att träna en LLM från grunden är utan tvekan det svåraste och mest komplexa tillvägagångssättet att anta, vilket kräver enorma mängder data, kvalificerade resurser och lämplig beräkningskraft. Detta alternativ bör endast övervägas i ett scenario där ett företag har ett domänspecifikt användningsfall och en stor mängd domäncentrerad data.

## Kunskapskontroll

Vad kan vara ett bra tillvägagångssätt för att förbättra LLM-slutföringsresultat?

1. Prompt engineering med kontext  
1. RAG  
1. Finjusterad modell  

A:3, om du har tid och resurser samt högkvalitativ data, är finjustering det bättre alternativet för att hålla sig uppdaterad. Men om du vill förbättra saker och saknar tid är det värt att överväga RAG först.

## 🚀 Utmaning

Läs mer om hur du kan [använda RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) för ditt företag.

## Bra jobbat, fortsätt din inlärning

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om generativ AI!

Gå vidare till Lektion 3 där vi kommer att titta på hur man [bygger med Generativ AI på ett ansvarsfullt sätt](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.