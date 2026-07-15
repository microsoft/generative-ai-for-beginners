# Utforska och jämföra olika LLM:er

[![Utforska och jämföra olika LLM:er](../../../translated_images/sv/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klicka på bilden ovan för att se videon av denna lektion_

Med den föregående lektionen har vi sett hur Generativ AI förändrar teknologilandskapet, hur stora språkmodeller (LLM) fungerar och hur ett företag – som vår startup – kan tillämpa dem på sina användningsfall och växa! I detta kapitel ska vi jämföra och kontrastera olika typer av stora språkmodeller (LLM) för att förstå deras för- och nackdelar.

Nästa steg på vår startups resa är att utforska det nuvarande landskapet av LLM:er och förstå vilka som är lämpliga för vårt användningsfall.

## Introduktion

Denna lektion kommer att täcka:

- Olika typer av LLM:er i det nuvarande landskapet.
- Testa, iterera och jämföra olika modeller för ditt användningsfall i Azure.
- Hur man distribuerar en LLM.

## Lärandemål

Efter att ha genomfört denna lektion kommer du att kunna:

- Välja rätt modell för ditt användningsfall.
- Förstå hur man testar, itererar och förbättrar prestandan hos din modell.
- Veta hur företag distribuerar modeller.

## Förstå olika typer av LLM:er

LLM:er kan kategoriseras på flera sätt baserat på deras arkitektur, träningsdata och användningsfall. Att förstå dessa skillnader hjälper vår startup att välja rätt modell för scenariot och förstå hur man testar, itererar och förbättrar prestandan.

Det finns många olika typer av LLM-modeller, ditt val av modell beror på vad du avser använda dem till, din data, hur mycket du är villig att betala och mer.

Beroende på om du avser använda modellerna för text, ljud, video, bildgenerering och så vidare, kan du välja en annan typ av modell.

- **Ljud- och taligenkänning**. Whisper-liknande modeller är fortfarande användbara allmänt användbara taligenkänningsmodeller, men produktionsval inkluderar nu även nyare tal-till-text-modeller såsom `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` och diariseringsvarianter. Utvärdera språkstöd, diariseringsfunktion, realtidssupport, latens och kostnad för ditt scenario. Läs mer i [OpenAI:s tal-till-text dokumentation](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Bildgenerering**. DALL-E och Midjourney är välkända alternativ för bildgenerering, men nuvarande OpenAI bild-API:er kretsar kring GPT-bildmodeller som `gpt-image-2`, medan Stable Diffusion, Imagen, Flux och andra modellsfamiljer också är vanliga val. Jämför uppfyllande av prompt, stöd för redigering, stilkontroll, säkerhetskrav och licensiering. Läs mer i [OpenAI guiden för bildgenerering](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) och kapitel 9 i detta läroplan.

- **Textgenerering**. Textmodeller inkluderar nu frontmodell, resonemangsmodeller, mindre låglatensmodeller och öppna viktsmodeller. Nuvarande exempel inkluderar OpenAI GPT-5.x modeller, Anthropic Claude 4.x modeller, Google Gemini 3.x modeller, Meta Llama 4 modeller och Mistral-modeller. Välj inte bara efter releasedatum eller pris; jämför uppgiftskvalitet, latens, kontextfönster, verktygsanvändning, säkerhetsbeteende, regional tillgänglighet och totalkostnad. [Microsoft Foundry:s modellkatalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) är en bra plats att jämföra modeller som finns tillgängliga på Azure.

- **Multimodalitet**. Många nuvarande modeller kan bearbeta mer än text. Vissa accepterar bild-, ljud- eller videoingångar; några kan anropa verktyg; och specialiserade modeller kan generera bilder, ljud eller video. Exempelvis stödjer nuvarande OpenAI-modeller text- och bildinmatning, Gemini-modeller kan stödja text, kod, bild, ljud och video beroende på variant, och Llama 4 Scout och Maverick är öppna vikt- och nativt multimodala modeller. Kontrollera alltid varje modellkort för stöd för ingångs- och utgångsmodaliteter innan du bygger en arbetsflöde kring det.

Att välja en modell innebär att du får vissa grundläggande funktioner, vilket dock ibland inte räcker. Ofta har företaget specifik data som du på något sätt behöver informera LLM om. Det finns några olika val för hur du kan närma dig detta, mer om det i kommande avsnitt.

### Foundation Models kontra LLM:er

Termen Foundation Model myntades av [Stanford-forskare](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) och definierades som en AI-modell som följer vissa kriterier, såsom:

- **De tränas med osupervised learning eller self-supervised learning**, vilket innebär att de tränas på oetiketterad multimodal data och kräver inte manuell annotering eller märkning av data för träningsprocessen.
- **De är mycket stora modeller**, baserade på mycket djupa neurala nätverk tränade på miljarder parametrar.
- **De är normalt avsedda att tjäna som en 'grund' för andra modeller**, vilket innebär att de kan användas som utgångspunkt för att bygga andra modeller ovanpå, vilket kan göras genom fine-tuning.

![Foundation Models versus LLMs](../../../translated_images/sv/FoundationModel.e4859dbb7a825c94.webp)

Bildkälla: [Essential Guide to Foundation Models and Large Language Models | av Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

För att ytterligare förtydliga denna skillnad, låt oss ta ChatGPT som ett historiskt exempel. Tidigare versioner av ChatGPT använde GPT-3.5 som en foundation-modell. OpenAI använde sedan chatt-specifik data och anpassningstekniker för att skapa en finjusterad version som presterade bättre i konversationsscenarier, såsom chatbots. Moderna AI-tjänster växlar ofta mellan flera modellvarianter, så tjänstens namn och den underliggande modellens namn är inte alltid samma sak.

![Foundation Model](../../../translated_images/sv/Multimodal.2c389c6439e0fc51.webp)

Bildkälla: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Öppen vikt/öppen källkod kontra proprietära modeller

Ett annat sätt att kategorisera LLM:er är om de är öppna vikt, öppen källkod eller proprietära.

Öppen källkod och öppna vikt-modeller gör modellartefakterna tillgängliga för inspektion, nedladdning eller anpassning, men deras licenser skiljer sig. Vissa är helt open source, medan andra är öppna vikt-modeller med användningsbegränsningar. De kan vara användbara när ett företag behöver mer kontroll över distribution, datalokalitet, kostnad eller anpassning. Dock måste team fortfarande granska licensvillkor, driftskostnader, underhåll, säkerhetsuppdateringar och utvärderingskvalitet innan de används i produktion. Exempel inkluderar [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), vissa [Mistral-modeller](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) och många modeller på [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietära modeller ägs och hostas av en leverantör. Dessa modeller är ofta optimerade för hanterad produktionsanvändning och kan erbjuda stark support, säkerhetssystem, verktygsintegration och skalbarhet. Men kunder kan vanligtvis inte inspektera eller modifiera modellvikterna, och de måste granska leverantörsvillkor för integritet, lagring, efterlevnad och acceptabel användning. Exempel inkluderar [OpenAI modeller](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) och [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Inbäddning kontra bildgenerering kontra text- och kodgenerering

LLM:er kan också kategoriseras efter den output de genererar.

Inbäddningar är en uppsättning modeller som kan omvandla text till en numerisk form, kallad inbäddning, vilket är en numerisk representation av inmatningstexten. Inbäddningar gör det enklare för maskiner att förstå relationer mellan ord eller meningar och kan användas som inputs till andra modeller, som klassificeringsmodeller eller klusteringsmodeller som presterar bättre på numeriska data. Inbäddningsmodeller används ofta för transfer learning, där en modell byggs för en surrogatuppgift med rikligt data, och sedan återanvänds modellvikterna (inbäddningarna) för andra nedströmsuppgifter. Ett exempel på denna kategori är [OpenAI inbäddningar](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/sv/Embedding.c3708fe988ccf760.webp)

Bildgenereringsmodeller är modeller som genererar bilder. Dessa modeller används ofta för bildredigering, bildsyntes och bildöversättning. Bildgenereringsmodeller tränas ofta på stora bilddataset, såsom [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), och kan användas för att generera nya bilder eller redigera befintliga bilder med inpainting, super-upplösning och koloreringstekniker. Exempel inkluderar [GPT Image-modeller](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion-modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) och Imagen-modeller.

![Image generation](../../../translated_images/sv/Image.349c080266a763fd.webp)

Text- och kodgenereringsmodeller är modeller som genererar text eller kod. Dessa modeller används ofta för textsammanfattning, översättning och frågesvar. Textgenereringsmodeller tränas ofta på stora textdataset, såsom [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), och kan användas för att generera ny text eller svara på frågor. Kodgenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), tränas ofta på stora koddataset, som GitHub, och kan användas för att generera ny kod eller fixa buggar i befintlig kod.

![Text and code generation](../../../translated_images/sv/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder kontra Decoder-only

För att prata om olika typer av arkitekturer för LLM:er, låt oss använda en analogi.

Föreställ dig att din chef gav dig i uppgift att skriva en quiz för studenterna. Du har två kollegor; en ansvarar för att skapa innehåll och den andra för att granska det.

Innehållsskaparen är som en decoder-only modell: de kan titta på ämnet, se vad du redan skrivit, och sedan fortsätta generera innehåll baserat på den kontexten. De är mycket bra på att skriva engagerande och informativt innehåll, men är inte alltid bäst när uppgiften enbart är klassificering, hämtning eller kodning av information. Exempel på decoder-only modellfamiljer inkluderar GPT och Llama modeller.

Granskaren är som en Encoder-only modell, de tittar på det skrivna materialet och svaren, noterar relationen mellan dem och förstår kontexten, men är inte bra på att generera innehåll. Ett exempel på Encoder-only modell är BERT.

Föreställ dig att vi även kan ha någon som både kan skapa och granska quizet, detta är en Encoder-Decoder modell. Några exempel är BART och T5.

### Tjänst kontra Modell

Låt oss nu prata om skillnaden mellan en tjänst och en modell. En tjänst är en produkt som erbjuds av en molntjänstleverantör och är ofta en kombination av modeller, data och andra komponenter. En modell är den kärnkomponent i en tjänst och är ofta en foundation-modell, såsom en LLM.

Tjänster är ofta optimerade för produktionsanvändning och är ofta lättare att använda än modeller, via ett grafiskt användargränssnitt. Dock är tjänster inte alltid gratis och kan kräva prenumeration eller betalning för användning, i utbyte mot att använda tjänsteägarens utrustning och resurser, optimera kostnader och skala enkelt. Ett exempel på en tjänst är [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), som erbjuder en betal-efter-användningsmodell, där användare debiteras proportionellt efter hur mycket de använder tjänsten. Azure OpenAI Service erbjuder också företagsklassad säkerhet och ett framework för ansvarsfull AI ovanpå modellernas kapacitet.

Modeller är artefakterna från neurala nätverk: parametrar, vikter, arkitektur, tokenizer och stödjande konfiguration. Att köra en modell lokalt eller i en privat miljö kräver lämplig hårdvara, infrastruktur för drift, övervakning och antingen en kompatibel öppen källkod/öppen vikt-licens eller en kommersiell licens. Öppen vikt-modeller som Llama 4 eller Mistral-modeller kan hostas själv, men kräver fortfarande beräkningskraft och driftsexpertis.

## Hur man testar och itererar med olika modeller för att förstå prestanda på Azure


När vårt team har utforskat det aktuella landskapet för LLM och identifierat några bra kandidater för deras scenarier, är nästa steg att testa dem på deras data och arbetsbelastning. Detta är en iterativ process som görs genom experiment och mätningar.
De flesta av de modeller vi nämnde i tidigare stycken (OpenAI-modeller, öppenviktsmodeller som Llama 4 och Mistral, och Hugging Face-modeller) finns tillgängliga i [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), tidigare Azure AI Studio/Azure AI Foundry, är en enhetlig Azure-plattform för att bygga AI-appar och agenter. Den hjälper utvecklare att hantera hela livscykeln från experimentering och utvärdering till distribution, övervakning och styrning. Modellkatalogen i Microsoft Foundry gör det möjligt för användaren att:

- Hitta den grundläggande modellen av intresse i katalogen, inklusive modeller som säljs av Azure och modeller från partners och community-leverantörer. Användare kan filtrera efter uppgift, leverantör, licens, distributionsalternativ eller namn.

![Model catalog](../../../translated_images/sv/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Granska modellkortet, inklusive en detaljerad beskrivning av avsedd användning och träningsdata, kodexempel och utvärderingsresultat från det interna utvärderingsbiblioteket.

![Model card](../../../translated_images/sv/ModelCard.598051692c6e400d.webp)

- Jämföra benchmarks mellan modeller och dataset tillgängliga i branschen för att bedöma vilken som passar affärsscenariot, genom [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)-panelen.

![Model benchmarks](../../../translated_images/sv/ModelBenchmarks.254cb20fbd06c03a.webp)

- Finjustera stödjade modeller på anpassad träningsdata för att förbättra modellens prestanda i en specifik arbetsbelastning, med hjälp av experimenterings- och spårningsfunktionerna i Microsoft Foundry.

![Model fine-tuning](../../../translated_images/sv/FineTuning.aac48f07142e36fd.webp)

- Distribuera den ursprungliga förtränade modellen eller den finjusterade versionen till en fjärrstyrd realtids-inferenspunktsloppsände, med hjälp av hanterad beräkning eller serverlösa distributionsalternativ, för att möjliggöra att applikationer kan konsumera den.

![Model deployment](../../../translated_images/sv/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Inte alla modeller i katalogen är för närvarande tillgängliga för finjustering och/eller pay-as-you-go-distribution. Kontrollera modellkortet för detaljer om modellens kapabiliteter och begränsningar.

## Förbättra LLM-resultat

Vi har med vårt startupteam utforskat olika typer av LLM och en molnplattform (Microsoft Foundry) som gör det möjligt för oss att jämföra olika modeller, utvärdera dem på testdata, förbättra prestanda och distribuera dem på inferenspunkter.

Men när bör de överväga att finjustera en modell istället för att använda en förtränad? Finns det andra metoder för att förbättra modellprestanda på specifika arbetsbelastningar?

Det finns flera metoder som ett företag kan använda för att få de resultat de behöver från en LLM. Du kan välja olika typer av modeller med olika grader av träning när du distribuerar en LLM i produktion, med olika nivåer av komplexitet, kostnad och kvalitet. Här är några olika metoder:

- **Prompt engineering med kontext**. Idén är att ge tillräckligt med kontext när du promptar för att säkerställa att du får de svar du behöver.

- **Retrieval Augmented Generation, RAG**. Dina data kan finnas i en databas eller web-endpoint till exempel, för att säkerställa att denna data, eller en delmängd av den, inkluderas vid promptningstiden, kan du hämta relevant data och göra den till en del av användarens prompt.

- **Finjusterad modell**. Här har du tränat modellen vidare på dina egna data vilket leder till att modellen blir mer exakt och lyhörd för dina behov, men det kan vara kostsamt.

![LLMs deployment](../../../translated_images/sv/Deploy.18b2d27412ec8c02.webp)

Bildkälla: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering med Kontext

Förtränade LLM fungerar mycket bra på generaliserade naturliga språkuppgifter, även genom att anropa dem med en kort prompt, som en mening att slutföra eller en fråga – den så kallade ”zero-shot”-inlärningen.

Ju mer användaren kan rama in sin fråga, med en detaljerad förfrågan och exempel – Kontexten – desto mer exakt och närmare användarens förväntningar blir svaret. I detta fall talar vi om ”one-shot” inlärning om prompten inkluderar endast ett exempel och ”few-shot learning” om den inkluderar flera exempel.
Prompt engineering med kontext är den mest kostnadseffektiva metoden att börja med.

### Retrieval Augmented Generation (RAG)

LLM har den begränsningen att de endast kan använda data som har använts under deras träning för att generera ett svar. Det betyder att de inte vet något om fakta som inträffade efter deras träningsprocess, och de kan inte komma åt icke-offentlig information (som företagsdata).
Detta kan övervinnas genom RAG, en teknik som förstärker prompten med externa data i form av delar av dokument, med hänsyn till begränsningar i promptlängd. Detta stöds av vektordatabasverktyg (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) som hämtar relevanta delar från olika fördefinierade datakällor och lägger till dem i promptens Kontext.

Denna teknik är mycket hjälpsam när ett företag inte har tillräckligt med data, tillräckligt med tid eller resurser för att finjustera en LLM men ändå vill förbättra prestandan på en specifik arbetsbelastning och minska riskerna för hallucinerade, föråldrade eller icke-understödda svar.

### Finjusterad modell

Finjustering är en process som utnyttjar överföringsinlärning för att ”anpassa” modellen till en nedströmsuppgift eller för att lösa ett specifikt problem. Till skillnad från few-shot learning och RAG resulterar det i att en ny modell genereras, med uppdaterade vikter och parametrar. Det kräver ett set av träningsexempel bestående av en enda inmatning (prompten) och dess tillhörande utdata (slutförandet).
Detta skulle vara den föredragna metoden om:

- **Använda mindre uppgiftsspecifika modeller**. Ett företag vill finjustera en mindre modell för en smal uppgift snarare än att upprepade gånger prompta en större frontier-modell, vilket resulterar i en mer kostnadseffektiv och snabbare lösning.

- **Ta hänsyn till latens**. Latens är viktigt för ett specifikt användningsfall, så det är inte möjligt att använda mycket långa promtar eller antalet exempel som modellen ska lära sig av inte passar med promptlängdsgränsen.

- **Anpassa stabilt beteende**. Ett företag har många högkvalitativa exempel och vill att modellen konsekvent ska följa ett uppgiftsmönster, utdataformat, ton eller domänspecifik stil. Om huvudproblemet är färska fakta eller privat kunskap som förändras ofta, använd RAG istället för att enbart förlita dig på finjustering.

### Tränad modell

Att träna en LLM från grunden är utan tvekan den svåraste och mest komplexa metod att anta, och kräver enorma mängder data, kunniga resurser och lämplig beräkningskapacitet. Detta alternativ bör endast övervägas i ett scenario där ett företag har ett domänspecifikt användningsfall och en stor mängd domäncentrerad data.

## Kunskapskontroll

Vad kan vara en bra metod för att förbättra LLM-svar?

1. Prompt engineering med kontext
1. RAG
1. Finjusterad modell

Svar: Alla tre kan hjälpa. Börja med prompt engineering och kontext för snabba förbättringar, och använd RAG när modellen behöver aktuella fakta eller privat företagsdata. Välj finjustering när du har tillräckligt med högkvalitativa exempel och behöver att modellen konsekvent följer en uppgift, format, ton eller domänmönster.

## 🚀 Utmaning

Läs mer om hur du kan [använda RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) för ditt företag.

## Bra jobbat, fortsätt din lärande

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta att förbättra din kunskap om Generativ AI!

Gå vidare till Lektion 3 där vi kommer att titta på hur man [bygger med Generativ AI Ansvarsfullt](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->