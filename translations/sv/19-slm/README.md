# Introduktion till Små Språkmodeller för Generativ AI för Nybörjare
Generativ AI är ett fascinerande område inom artificiell intelligens som fokuserar på att skapa system kapabla att generera nytt innehåll. Detta innehåll kan vara allt från text och bilder till musik och till och med hela virtuella miljöer. En av de mest spännande tillämpningarna av generativ AI är inom området språkmodeller.

## Vad är Små Språkmodeller?

En Små Språkmodell (SLM) representerar en nedskalad variant av en stor språkmodell (LLM), som använder många av de arkitektoniska principerna och teknikerna hos LLM:er, samtidigt som den uppvisar ett betydligt reducerat beräkningsavtryck.

SLM är en undergrupp av språkmodeller designade för att generera mänskligt liknande text. Till skillnad från deras större motsvarigheter, som GPT-4, är SLM mer kompakta och effektiva, vilket gör dem idealiska för applikationer där beräkningsresurser är begränsade. Trots sin mindre storlek kan de fortfarande utföra en rad uppgifter. Vanligtvis konstrueras SLM genom att komprimera eller destillera LLM:er, i syfte att behålla en stor del av den ursprungliga modellens funktionalitet och språkliga förmågor. Denna minskning i modellstorlek reducerar den totala komplexiteten, vilket gör SLM mer effektiva vad gäller både minnesanvändning och beräkningskrav. Trots dessa optimeringar kan SLM fortfarande utföra ett brett spektrum av uppgifter inom naturlig språkbearbetning (NLP):

- Textgenerering: Skapa sammanhängande och kontextuellt relevanta meningar eller stycken.
- Textkomplettering: Förutsäga och slutföra meningar baserat på en given prompt.
- Översättning: Översätta text från ett språk till ett annat.
- Sammanfattning: Förkorta långa textstycken till kortare, mer lättsmälta sammanfattningar.

Om än med vissa avvägningar i prestanda eller djup i förståelse jämfört med deras större motsvarigheter.

## Hur fungerar Små Språkmodeller?
SLM tränas på stora mängder textdata. Under träningen lär de sig språkets mönster och strukturer, vilket gör att de kan generera text som är både grammatiskt korrekt och kontextuellt passande. Träningsprocessen innefattar:

- Datainsamling: Insamling av stora dataset med text från olika källor.
- Förbehandling: Rengöring och organisering av data för att göra den lämplig för träning.
- Träning: Använda maskininlärningsalgoritmer för att lära modellen att förstå och generera text.
- Finjustering: Justera modellen för att förbättra dess prestanda i specifika uppgifter.

Utvecklingen av SLM sammanfaller med det ökande behovet av modeller som kan köras i resursbegränsade miljöer, som mobila enheter eller edge computing-plattformar, där fullskaliga LLM kan vara opraktiska på grund av deras höga resursbehov. Genom att fokusera på effektivitet balanserar SLM prestanda med tillgänglighet, vilket möjliggör bredare tillämpning inom olika domäner.

![slm](../../../translated_images/sv/slm.4058842744d0444a.webp)

## Lärandemål

I denna lektion hoppas vi introducera kunskap om SLM och kombinera den med Microsoft Phi-3 för att lära oss olika scenarier inom textinnehåll, vision och MoE.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är SLM?
- Vad är skillnaden mellan SLM och LLM?
- Vad är Microsoft Phi-3/3.5-familjen?
- Hur kör man inferens med Microsoft Phi-3/3.5-familjen?

Redo? Då kör vi igång.

## Skillnaderna mellan Stora Språkmodeller (LLMs) och Små Språkmodeller (SLMs)

Både LLM och SLM bygger på grundläggande principer för probabilistisk maskininlärning, med liknande tillvägagångssätt i deras arkitektoniska design, träningsmetodik, data-genereringsprocesser och modellutvärderingstekniker. Dock skiljer sig flera nyckelfaktorer mellan dessa två typer av modeller.

## Tillämpningar av Små Språkmodeller

SLM har ett brett användningsområde, bland annat:

- Chattbottar: Tillhandahålla kundsupport och interagera med användare på ett samtalsliknande sätt.
- Innehållsskapande: Assistera författare genom att generera idéer eller till och med skriva hela artiklar.
- Utbildning: Hjälpa studenter med skrivuppgifter eller att lära sig nya språk.
- Tillgänglighet: Skapa verktyg för personer med funktionsnedsättningar, som text-till-tal-system.

**Storlek**
 
En huvudskillnad mellan LLM och SLM ligger i modellernas skala. LLM, som ChatGPT (GPT-4), kan bestå av uppskattningsvis 1,76 biljoner parametrar, medan open-source SLM som Mistral 7B är designade med betydligt färre parametrar – ungefär 7 miljarder. Denna skillnad beror främst på variationer i modellarkitektur och träningsprocesser. Exempelvis använder ChatGPT en självuppmärksamhetsmekanism inom en encoder-decoder-arkitektur, medan Mistral 7B använder sliding window attention, vilket möjliggör mer effektiv träning inom en decoder-only-modell. Denna arkitektoniska olikhet har djupgående konsekvenser för modellernas komplexitet och prestanda.

**Förståelse**

SLM optimeras typiskt för prestanda inom specifika domäner, vilket gör dem mycket specialiserade men potentiellt begränsade i förmågan att erbjuda bred kontextuell förståelse över flera kunskapsområden. I kontrast syftar LLM till att simulera mänsklig intelligens på en mer omfattande nivå. Tränade på stora och mångsidiga dataset är LLM designade för att prestera väl över flera fält och erbjuda större mångsidighet och anpassningsförmåga. Följaktligen är LLM mer lämpade för en bredare uppsättning av efterföljande uppgifter, såsom naturlig språkbearbetning och programmering.

**Beräkning**

Träning och implementering av LLM är resurskrävande processer som ofta kräver omfattande beräkningsinfrastruktur, inklusive storskaliga GPU-kluster. Till exempel kan träning av en modell som ChatGPT från grunden kräva tusentals GPU:er under lång tid. I kontrast är SLM med sin mindre parametrar mer tillgängliga vad gäller beräkningsresurser. Modeller som Mistral 7B kan tränas och köras på lokala maskiner med måttliga GPU-kapaciteter, även om träning fortfarande kräver flera timmar över flera GPU:er.

**Bias**

Bias är ett känt problem i LLM, främst på grund av naturen hos träningsdata. Dessa modeller förlitar sig ofta på rå, offentligt tillgänglig data från internet, som kan underrepresentera eller missrepresentera vissa grupper, införa felaktig märkning eller återspegla språkliga biaser påverkade av dialekt, geografiska variationer och grammatiska regler. Dessutom kan komplexiteten i LLM:s arkitektur ofrivilligt förvärra bias, vilket kan gå obemärkt utan noggrann finjustering. Å andra sidan, då SLM ofta tränas på mer begränsade och domänspecifika dataset, är de av naturen mindre benägna att drabbas av sådana bias, även om de inte är helt immuna.

**Inferens**

Den mindre storleken hos SLM ger dem en betydande fördel vad gäller inferenshastighet, vilket möjliggör effektiv generering av utsignaler på lokal hårdvara utan behov av omfattande parallell bearbetning. I kontrast kräver LLM, på grund av sin storlek och komplexitet, ofta stora parallella beräkningsresurser för att uppnå acceptabla inferenstider. Närvaro av flera samtidiga användare saktar dessutom ner LLM:s svarstider, särskilt vid storskalig implementering.

Sammanfattningsvis, trots att både LLM och SLM delar en grund i maskininlärning, skiljer de sig markant vad gäller modellstorlek, resurskrav, kontextuell förståelse, benägenhet för bias och inferenshastighet. Dessa skillnader speglar deras respektive lämplighet för olika användningsfall, där LLM är mer mångsidiga men resursintensiva, medan SLM erbjuder mer domänspecifik effektivitet med lägre beräkningsbehov.

***Notera: I denna lektion kommer vi att introducera SLM med Microsoft Phi-3 / 3.5 som exempel.***

## Introduktion till Phi-3 / Phi-3.5 Familjen

Phi-3 / 3.5-familjen riktar sig främst till scenarier för text, vision och Agent (MoE) applikationer:

### Phi-3 / 3.5 Instruct

Huvudsakligen för textgenerering, chattkomplettering och innehållsinformationsutvinning, med mera.

**Phi-3-mini**

3,8 miljarder språkmodell finns tillgänglig på Microsoft Foundry, Hugging Face och Ollama. Phi-3-modeller presterar betydligt bättre än språkmodeller av samma eller större storlek på nyckelmått (se benchmark-tal nedan, högre siffror är bättre). Phi-3-mini överträffar modeller dubbelt så stora, medan Phi-3-small och Phi-3-medium överträffar större modeller, inklusive GPT-3.5.

**Phi-3-small & medium**

Med endast 7 miljarder parametrar slår Phi-3-small GPT-3.5T på en mängd språk-, resonemangs-, kodnings- och matematikbenchmarkar.

Phi-3-medium med 14 miljarder parametrar fortsätter denna trend och presterar bättre än Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan betrakta den som en uppgradering av Phi-3-mini. Även om parametrarna förblir oförändrade, förbättrar den möjligheten att stödja flera språk (stöder 20+ språk: arabiska, kinesiska, tjeckiska, danska, nederländska, engelska, finska, franska, tyska, hebreiska, ungerska, italienska, japanska, koreanska, norska, polska, portugisiska, ryska, spanska, svenska, thailändska, turkiska, ukrainska) och ger starkare stöd för långt kontext.

Phi-3.5-mini med 3,8 miljarder parametrar överträffar språkmodeller i samma storlek och är i nivå med modeller dubbelt så stora.

### Phi-3 / 3.5 Vision

Vi kan tänka på Instruct-modellen i Phi-3/3.5 som Phis förmåga att förstå, och Vision är det som ger Phi ögon för att förstå världen.


**Phi-3-Vision**

Phi-3-vision, med endast 4,2 miljarder parametrar, fortsätter denna trend och överträffar större modeller som Claude-3 Haiku och Gemini 1.0 Pro V vad gäller generella visuella resonemangsuppgifter, OCR, samt tabell- och diagramförståelse.


**Phi-3.5-Vision**

Phi-3.5-Vision är också en uppgradering av Phi-3-Vision, som lägger till stöd för flera bilder. Du kan betrakta det som en förbättring inom vision: inte bara ser du bilder, utan också videor.

Phi-3.5-vision överträffar större modeller såsom Claude-3.5 Sonnet och Gemini 1.5 Flash inom OCR, tabell- och diagramförståelse och är i nivå med dem i generella visuella kunskapsresonemangsuppgifter. Stöder inmatning av flera ramar, dvs utför resonemang på flera bilder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** möjliggör för modeller att förtränas med mycket mindre beräkningar, vilket betyder att du dramatiskt kan skala upp modell- eller datasetstorlek med samma beräkningsbudget som en tätmodell. Specifikt bör en MoE-modell kunna uppnå samma kvalitet som sin täta motsvarighet mycket snabbare under förträning.

Phi-3.5-MoE består av 16x3,8 miljarder expertmoduler. Phi-3.5-MoE med endast 6,6 miljarder aktiva parametrar uppnår en liknande nivå av resonemang, språkförståelse och matematik som mycket större modeller.

Vi kan använda Phi-3/3.5-familjemodellen baserat på olika scenarier. Till skillnad från LLM kan du distribuera Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheter.


## Hur man använder Phi-3/3.5-familjemodeller

Vi hoppas kunna använda Phi-3/3.5 i olika scenarier. Nästa steg är att vi använder Phi-3/3.5 baserat på olika scenarier.

![phi3](../../../translated_images/sv/phi3.655208c3186ae381.webp)

### Inferens via moln-API:er

**Microsoft Foundry-modeller**

> **Notera:** GitHub Models läggs ner i slutet av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) är den direkta ersättaren.

Microsoft Foundry-modeller är det mest direkta sättet. Du kan snabbt komma åt Phi-3/3.5-Instruct-modellen via Foundry modellkatalog. Kombinerat med Azure AI Inferens-SDK / OpenAI SDK kan du nå API:t via kod för att göra Phi-3/3.5-Instruct-anrop. Du kan även testa olika effekter via Playground.

- Demo: Jämförelse av effekterna mellan Phi-3-mini och Phi-3.5-mini i kinesiska scenarier

![phi3](../../../translated_images/sv/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/sv/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Eller om vi vill använda vision- och MoE-modellerna kan du använda Microsoft Foundry för att göra anrop. Om du är intresserad kan du läsa Phi-3 Cookbook för att lära dig hur man kallar Phi-3/3.5 Instruct, Vision och MoE via Microsoft Foundry [Klicka på denna länk](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Utöver molnbaserade Microsoft Foundry Models-katalog kan du även använda [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) för att genomföra relaterade anrop. Du kan besöka NVIDIA NIM för att slutföra API-anrop för Phi-3/3.5-familjen. NVIDIA NIM (NVIDIA Inference Microservices) är en uppsättning accelererade inferens-mikrotjänster designade för att hjälpa utvecklare att effektivt distribuera AI-modeller över olika miljöer, inklusive moln, datacenter och arbetsstationer.

Här är några nyckelfunktioner i NVIDIA NIM:

- **Enkel distribution:** NIM möjliggör distribution av AI-modeller med ett enda kommando, vilket gör det lätt att integrera i befintliga arbetsflöden.

- **Optimerad prestanda:** Den utnyttjar NVIDIA:s föroptimerade inferensmotorer, såsom TensorRT och TensorRT-LLM, för att säkerställa låg latens och hög genomströmning.
- **Skalbarhet:** NIM stöder autoskalning på Kubernetes, vilket gör att den effektivt kan hantera varierande arbetsbelastningar.
- **Säkerhet och kontroll:** Organisationer kan behålla kontrollen över sina data och applikationer genom att själv hosta NIM-mikrotjänster på sin egen hanterade infrastruktur.
- **Standard-API:er:** NIM tillhandahåller branschstandard-API:er, vilket gör det enkelt att bygga och integrera AI-applikationer som chatbots, AI-assistenter och mer.

NIM är en del av NVIDIA AI Enterprise, som syftar till att förenkla distributionen och operationaliseringen av AI-modeller och säkerställa att de körs effektivt på NVIDIA GPU:er.

- Demo: Använda NVIDIA NIM för att anropa Phi-3.5-Vision-API [[Klicka på denna länk](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Köra Phi-3/3.5 Lokalt
Inferens i relation till Phi-3, eller någon språkmodell som GPT-3, avser processen att generera svar eller förutsägelser baserat på den input den tar emot. När du ger en prompt eller fråga till Phi-3 använder den sitt tränade neurala nätverk för att sluta sig till det mest sannolika och relevanta svaret genom att analysera mönster och samband i den data den tränats på.

**Hugging Face Transformer**
Hugging Face Transformers är ett kraftfullt bibliotek utformat för naturlig språkbehandling (NLP) och andra maskininlärningsuppgifter. Här är några viktiga punkter om det:

1. **Förtränade modeller**: Det erbjuder tusentals förtränade modeller som kan användas för olika uppgifter som textklassificering, namngiven entity-igenkänning, frågesvar, sammanfattning, översättning och textgenerering.

2. **Ramverksinteroperabilitet:** Biblioteket stöder flera djupinlärningsramverk, inklusive PyTorch, TensorFlow och JAX. Det gör att du kan träna en modell i ett ramverk och använda den i ett annat.

3. **Multimodala möjligheter:** Förutom NLP stöder Hugging Face Transformers även uppgifter inom datorseende (t.ex. bildklassificering, objektigenkänning) och ljudbehandling (t.ex. taligenkänning, ljudklassificering).

4. **Användarvänlighet:** Biblioteket erbjuder API:er och verktyg för att enkelt ladda ner och finjustera modeller, vilket gör det tillgängligt för både nybörjare och experter.

5. **Community och resurser:** Hugging Face har en livlig community och omfattande dokumentation, handledningar och guider för att hjälpa användare att komma igång och få ut mesta möjliga av biblioteket.
[officiell dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deras [GitHub-förråd](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Detta är den vanligast använda metoden, men den kräver också GPU-acceleration. Scenarier som Vision och MoE kräver trots allt mycket beräkningar, vilket blir mycket långsamt på CPU om de inte kvantiseras.


- Demo: Använda Transformer för att anropa Phi-3.5-Instruct [Klicka på denna länk](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Använda Transformer för att anropa Phi-3.5-Vision [Klicka på denna länk](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Använda Transformer för att anropa Phi-3.5-MoE [Klicka på denna länk](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) är en plattform designad för att göra det enklare att köra stora språkmodeller (LLMs) lokalt på din maskin. Den stöder olika modeller som Llama 3.1, Phi 3, Mistral och Gemma 2, bland andra. Plattformen förenklar processen genom att paketera modellvikter, konfiguration och data i ett enda paket, vilket gör det mer tillgängligt för användare att anpassa och skapa sina egna modeller. Ollama finns för macOS, Linux och Windows. Det är ett utmärkt verktyg om du vill experimentera med eller distribuera LLM:er utan att förlita dig på molntjänster. Ollama är det mest direkta sättet, du behöver bara köra följande kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) är Microsofts offline-körtid på enheten för att köra modeller som Phi helt på din egen hårdvara - inget Azure-prenumeration, API-nyckel eller nätverksanslutning krävs. Den väljer automatiskt den bästa exekveringsleverantören som finns tillgänglig (NPU, GPU eller CPU) och exponerar en OpenAI-kompatibel slutpunkt, så befintlig `openai`/Azure AI Inference SDK-kod kan peka på den med minimala ändringar. Se [Foundry Locals dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) för att komma igång.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Eller använd SDK direkt i Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime för GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) är en plattformsoberoende accelerator för inferens och träning av maskininlärning. ONNX Runtime för Generative AI (GENAI) är ett kraftfullt verktyg som hjälper dig att köra generativa AI-modeller effektivt över olika plattformar.

## Vad är ONNX Runtime?
ONNX Runtime är ett open source-projekt som möjliggör högpresterande inferens av maskininlärningsmodeller. Den stöder modeller i Open Neural Network Exchange (ONNX)-format, som är en standard för att representera maskininlärningsmodeller. ONNX Runtime-inferens kan möjliggöra snabbare kundupplevelser och lägre kostnader, och stöder modeller från djupinlärningsramverk som PyTorch och TensorFlow/Keras, liksom klassiska maskininlärningsbibliotek som scikit-learn, LightGBM, XGBoost med mera. ONNX Runtime är kompatibelt med olika hårdvaror, drivrutiner och operativsystem och ger optimal prestanda genom att utnyttja hårdvaruacceleratorer där det är möjligt, tillsammans med grafoptimeringar och transformationer.

## Vad är Generativ AI?
Generativ AI avser AI-system som kan generera nytt innehåll, såsom text, bilder eller musik, baserat på den data de har tränats på. Exempel inkluderar språkmodeller som GPT-3 och bildgenereringsmodeller som Stable Diffusion. ONNX Runtime för GenAI-biblioteket tillhandahåller den generativa AI-loopen för ONNX-modeller, inklusive inferens med ONNX Runtime, logitsbehandling, sökning och sampling samt hantering av KV-cache.

## ONNX Runtime för GENAI
ONNX Runtime för GENAI utökar ONNX Runtimes möjligheter för att stödja generativa AI-modeller. Här är några viktiga funktioner:

- **Brett plattformsstöd:** Den fungerar på olika plattformar, inklusive Windows, Linux, macOS, Android och iOS.
- **Modellstöd:** Den stödjer många populära generativa AI-modeller, såsom LLaMA, GPT-Neo, BLOOM och fler.
- **Prestandaoptimering:** Den inkluderar optimeringar för olika hårdvaruacceleratorer som NVIDIA GPU:er, AMD GPU:er och fler2.
- **Användarvänlighet:** Den tillhandahåller API:er för enkel integration i applikationer, vilket gör att du kan generera text, bilder och annat innehåll med minimal kod.
- Användare kan anropa en hög-nivå generate()-metod eller köra varje iteration av modellen i en loop, generera en token i taget och valfritt uppdatera genereringsparametrar inom loopen.
- ONNX Runtime har även stöd för girig/strålsökning och TopP, TopK-sampling för att generera tokensekvenser samt inbyggd logitsbehandling som repetitionsstraff. Du kan också enkelt lägga till egen poängsättning.

## Komma igång
För att komma igång med ONNX Runtime för GENAI kan du följa dessa steg:

### Installera ONNX Runtime:
```Python
pip install onnxruntime
```
### Installera Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Kör en modell: Här är ett enkelt exempel i Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Använda ONNX Runtime GenAI för att anropa Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Övrigt**

Förutom ONNX Runtime, Ollama och Foundry Local-referensmetoder, kan vi även komplettera referensen för kvantitativa modeller baserat på modellreferensmetoder som tillhandahålls av olika tillverkare. Som Apple MLX-ramverk med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU och så vidare. Du kan också hitta mer innehåll i [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lärt oss grunderna i Phi-3/3.5-familjen, men för att lära oss mer om SLM behöver vi mer kunskap. Du kan hitta svaren i Phi-3 Cookbook. Om du vill veta mer, besök [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->