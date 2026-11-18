# Introduktion till små språkmodeller för generativ AI för nybörjare
Generativ AI är ett fascinerande område inom artificiell intelligens som fokuserar på att skapa system som kan generera nytt innehåll. Detta innehåll kan sträcka sig från text och bilder till musik och till och med hela virtuella miljöer. En av de mest spännande tillämpningarna av generativ AI är inom området för språkmodeller.

## Vad är små språkmodeller?

En små språkmodell (SLM) representerar en nedskalad variant av en stor språkmodell (LLM) och använder många av de arkitektoniska principerna och teknikerna från LLM, samtidigt som den visar ett betydligt reducerat beräkningsavtryck. 

SLM:er är en undergrupp av språkmodeller som är utformade för att generera människoliknande text. Till skillnad från deras större motsvarigheter, såsom GPT-4, är SLM:er mer kompakta och effektiva, vilket gör dem idealiska för tillämpningar där beräkningsresurser är begränsade. Trots sin mindre storlek kan de fortfarande utföra en mängd olika uppgifter. Vanligtvis konstrueras SLM:er genom att komprimera eller destillera LLM:er, med målet att behålla en betydande del av den ursprungliga modellens funktionalitet och språkliga kapaciteter. Denna minskning av modellstorleken minskar den totala komplexiteten, vilket gör SLM:er mer effektiva vad gäller både minnesanvändning och beräkningskrav. Trots dessa optimeringar kan SLM:er fortfarande utföra ett brett spektrum av naturliga språkbehandlingsuppgifter (NLP):

- Textgenerering: Skapa sammanhängande och kontextuellt relevanta meningar eller stycken.
- Textkomplettering: Förutsäga och fullborda meningar baserat på en given prompt.
- Översättning: Översätta text från ett språk till ett annat.
- Sammanfattning: Kondensera långa texter till kortare, mer lättsmälta sammanfattningar.

Om än med vissa kompromisser i prestanda eller djup av förståelse jämfört med deras större motsvarigheter. 

## Hur fungerar små språkmodeller?
SLM:er tränas på stora mängder textdata. Under träningen lär de sig språkets mönster och strukturer, vilket gör det möjligt för dem att generera text som både är grammatiskt korrekt och kontextuellt lämplig. Träningsprocessen involverar:

- Datainsamling: Samla stora datasets med text från olika källor.
- Förbehandling: Rensa och organisera data för att göra den lämplig för träning.
- Träning: Använda maskininlärningsalgoritmer för att lära modellen hur man förstår och genererar text.
- Finjustering: Justera modellen för att förbättra dess prestanda på specifika uppgifter.

Utvecklingen av SLM:er är i linje med det ökande behovet av modeller som kan distribueras i resursbegränsade miljöer, såsom mobila enheter eller edge computing-plattformar, där fullskaliga LLM:er kan vara opraktiska på grund av deras höga resurskrav. Genom att fokusera på effektivitet balanserar SLM:er prestanda med tillgänglighet, vilket möjliggör bredare tillämpning över olika domäner.

![slm](../../../translated_images/sv/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Lärandemål

I denna lektion hoppas vi introducera kunskapen om SLM och kombinera den med Microsoft Phi-3 för att lära oss olika scenarier inom textinnehåll, vision och MoE.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är SLM?
- Vad är skillnaden mellan SLM och LLM?
- Vad är Microsoft Phi-3/3.5-familjen?
- Hur kör man inferens med Microsoft Phi-3/3.5-familjen?

Redo? Låt oss börja.

## Skillnaderna mellan stora språkmodeller (LLM) och små språkmodeller (SLM)

Både LLM och SLM bygger på grundläggande principer för sannolikhetsbaserad maskininlärning och följer liknande metoder i deras arkitektoniska design, träningsmetoder, datagenereringsprocesser och modelleringsutvärdering. Dock skiljer sig flera viktiga faktorer dessa två typer av modeller åt.

## Tillämpningar av små språkmodeller

SLM:er har ett brett användningsområde, inklusive:

- Chatbots: Ge kundsupport och interagera med användare på ett konverserande sätt.
- Innehållsskapande: Hjälpa skribenter genom att generera idéer eller till och med utarbeta hela artiklar.
- Utbildning: Hjälpa elever med skrivuppgifter eller att lära sig nya språk.
- Tillgänglighet: Skapa verktyg för personer med funktionsnedsättningar, såsom text-till-tal-system.

**Storlek**
  
En primär skillnad mellan LLM och SLM ligger i modellernas skala. LLM, såsom ChatGPT (GPT-4), kan bestå av uppskattningsvis 1,76 biljoner parametrar, medan open source-SLM:er som Mistral 7B är designade med betydligt färre parametrar—ungefär 7 miljarder. Denna skillnad beror huvudsakligen på skillnader i modellarkitektur och träningsprocesser. Till exempel använder ChatGPT en självuppmärksamhetsmekanism inom en kodar-avkodar-ram, medan Mistral 7B använder sliding window-attention, vilket möjliggör mer effektiv träning inom en enbart avkodare-modell. Denna arkitektoniska skillnad har djupgående konsekvenser för modellernas komplexitet och prestanda.

**Förståelse**

SLM är vanligtvis optimerade för prestanda inom specifika domäner, vilket gör dem mycket specialiserade men potentiellt begränsade i deras förmåga att erbjuda bred kontextuell förståelse över flera kunskapsfält. I kontrast syftar LLM att efterlikna människolik intelligens på en mer omfattande nivå. Tränade på omfattande och mångsidiga datasets är LLM utformade för att prestera väl över olika domäner, vilket erbjuder större mångsidighet och anpassningsbarhet. Följaktligen är LLM mer lämpliga för ett bredare spektrum av efterföljande uppgifter, såsom naturlig språkbehandling och programmering.

**Beräkning**

Träning och implementering av LLM är resursintensiva processer som ofta kräver betydande beräkningsinfrastruktur, inklusive storskaliga GPU-kluster. Till exempel kan träning av en modell som ChatGPT från grunden kräva tusentals GPU:er under långa perioder. I kontrast är SLM, med sina mindre antal parametrar, mer tillgängliga vad gäller beräkningsresurser. Modeller som Mistral 7B kan tränas och köras på lokala maskiner utrustade med måttliga GPU-kapaciteter, även om träning fortfarande kräver flera timmar över flera GPU:er.

**Fördomar**

Fördomar är ett känt problem i LLM, främst på grund av träningens datanatur. Dessa modeller förlitar sig ofta på rå, öppet tillgänglig data från internet, som kan underrepresentera eller felrepresentera vissa grupper, införa felmärkning eller spegla språkliga fördomar som påverkas av dialekt, geografiska variationer och grammatiska regler. Dessutom kan komplexiteten hos LLM-arkitekturer ofrivilligt förstärka fördomar, vilket kan gå obemärkt utan noggrann finjustering. Å andra sidan, eftersom SLM tränas på mer begränsade, domänspecifika datasets, är de i grunden mindre mottagliga för sådana fördomar, även om de inte är immuna.

**Inferens**

Den reducerade storleken hos SLM ger dem en betydande fördel vad gäller inferenshastighet, vilket gör att de kan generera resultat effektivt på lokal hårdvara utan behov av omfattande parallell bearbetning. I kontrast kräver LLM, på grund av deras storlek och komplexitet, ofta betydande parallella beräkningsresurser för att uppnå acceptabla inferenstider. Närvaro av flera samtidiga användare saktar dessutom ner LLM:s svarstider, särskilt vid storskalig distribution.

Sammanfattningsvis, medan både LLM:er och SLM:er delar en grundläggande bas i maskininlärning, skiljer de sig avsevärt vad gäller modellstorlek, resursbehov, kontextuell förståelse, mottaglighet för fördomar och inferenshastighet. Dessa skillnader speglar deras respektive lämplighet för olika användningsområden, där LLM är mer mångsidiga men resurskrävande, och SLM erbjuder mer domänspecifik effektivitet med reducerade beräkningskrav.

***Notera: I denna lektion kommer vi att introducera SLM med Microsoft Phi-3 / 3.5 som exempel.***

## Introduktion till Phi-3 / Phi-3.5-familjen

Phi-3 / 3.5-familjen riktar sig främst till text-, vision- och Agent (MoE) applikationsscenarier:

### Phi-3 / 3.5 Instruct

Huvudsakligen för textgenerering, chattkomplettering och informationsutvinning från innehåll, etc.

**Phi-3-mini**

Den 3.8 miljarder parametrar stora språkmodellen är tillgänglig på Microsoft Foundry, Hugging Face och Ollama. Phi-3 modeller presterar avsevärt bättre än språkmodeller av lika och större storlek på viktiga benchmarks (se benchmark-siffror nedan, högre siffror är bättre). Phi-3-mini överträffar modeller som är dubbelt så stora, medan Phi-3-small och Phi-3-medium överträffar ännu större modeller, inklusive GPT-3.5.

**Phi-3-small & medium**

Med bara 7 miljarder parametrar slår Phi-3-small GPT-3.5T på en rad språk-, resonemangs-, kodnings- och matematikbenchmarks.

Phi-3-medium med 14 miljarder parametrar fortsätter denna trend och presterar bättre än Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan se det som en uppgradering av Phi-3-mini. Även om antalet parametrar är oförändrat, förbättras stödet för flera språk (stödjer 20+ språk: arabiska, kinesiska, tjeckiska, danska, holländska, engelska, finska, franska, tyska, hebreiska, ungerska, italienska, japanska, koreanska, norska, polska, portugisiska, ryska, spanska, svenska, thailändska, turkiska, ukrainska) och tillför starkare stöd för långa kontexter.

Phi-3.5-mini med 3.8 miljarder parametrar presterar bättre än språkmodeller av samma storlek och är i nivå med modeller som är dubbelt så stora.

### Phi-3 / 3.5 Vision

Vi kan se Instruct-modellen av Phi-3/3.5 som Phis förmåga att förstå, och Vision är vad som ger Phi ögon att förstå världen.


**Phi-3-Vision**

Phi-3-vision, med endast 4.2 miljarder parametrar, fortsätter denna trend och presterar bättre än större modeller som Claude-3 Haiku och Gemini 1.0 Pro V på generella visuella resonemangsuppgifter, OCR samt tabell- och diagramförståelse.


**Phi-3.5-Vision**

Phi-3.5-Vision är också en uppgradering av Phi-3-Vision och lägger till stöd för multipla bilder. Du kan se det som en förbättring inom vision; nu kan du inte bara se bilder utan även videor.

Phi-3.5-vision överträffar större modeller som Claude-3.5 Sonnet och Gemini 1.5 Flash inom OCR, tabell- och diagramförståelse, och är i nivå med dem på generella visuella kunskapsresonemangsuppgifter. Stöder multi-frame inmatning, dvs. resonemang över flera inmatningsbilder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** möjliggör att modeller kan förtränas med mycket mindre beräkningskraft, vilket innebär att du dramatiskt kan skala upp modell- eller datasetstorleken med samma beräkningsbudget som en tät modell. Specifikt ska en MoE-modell uppnå samma kvalitet som sin täta motsvarighet mycket snabbare under förträning.

Phi-3.5-MoE består av 16x3.8 miljarder expermoduler. Phi-3.5-MoE med endast 6.6 miljarder aktiva parametrar uppnår liknande nivåer av resonemang, språkförståelse och matematik som mycket större modeller.

Vi kan använda Phi-3/3.5-familjemodellen i olika scenarier. Till skillnad från LLM kan du distribuera Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheter.


## Hur man använder Phi-3/3.5-familjemodeller

Vi hoppas använda Phi-3/3.5 i olika scenarier. Nästa steg är att använda Phi-3/3.5 beroende på olika scenarier.

![phi3](../../../translated_images/sv/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens via moln-API:er

**Microsoft Foundry-modeller**

> **Notera:** GitHub-modeller tas ur bruk i slutet av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) är den direkta ersättaren.

> **Notera:** Hela Phi-3/3.5-familjen (Instruct, Vision och MoE-varianter) drogs tillbaka från Microsoft Foundry Models-katalogen den 2025-08-30. Använd `Phi-4` (Instruct) eller `Phi-4-mini-instruct` där istället — Phi-3/3.5-exemplen nedan fungerar fortfarande via Hugging Face, Ollama, ONNX Runtime och NVIDIA NIM.

Microsoft Foundry Models erbjuder nu efterföljare till Phi-4. Använd `Phi-4` eller `Phi-4-mini-instruct` istället för de utgågna Phi-3/3.5-modellerna när du följer moln-API-exemplen.

- Demo: Jämförelse av effekterna av Phi-3-mini och Phi-3.5-mini i kinesiska scenarier

![phi3](../../../translated_images/sv/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sv/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Om du vill använda vision (multimodala) modeller i molnet, använd den nu tillgängliga `Phi-4-multimodal-instruct` genom Microsoft Foundry istället för de utgågna Phi-3/3.5 Vision-modellerna; för textuppgifter använd `Phi-4` eller `Phi-4-mini-instruct`. Phi-3.5 MoE-modellen är utgången från Microsoft Foundry, så använd andra alternativ som beskrivs i denna lektion (t.ex. Hugging Face) om du vill experimentera med den. Om du är intresserad kan du läsa Phi Cookbook för att lära dig hur man anropar Phi-modeller via Microsoft Foundry [Klicka på denna länk](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Förutom den molnbaserade Microsoft Foundry Models-katalogen kan du också använda [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) för att genomföra relaterade anrop. Besök NVIDIA NIM för att utföra API-anrop för Phi-3/3.5-familjen. NVIDIA NIM (NVIDIA Inference Microservices) är en uppsättning accelererade inferensmikrotjänster utformade för att hjälpa utvecklare att effektivt distribuera AI-modeller över olika miljöer, inklusive moln, datacenter och arbetsstationer.

Här är några nyckelfunktioner hos NVIDIA NIM:

- **Enkel distribution:** NIM tillåter distribution av AI-modeller med ett enda kommando, vilket gör det enkelt att integrera i befintliga arbetsflöden.
- **Optimerad prestanda:** Det utnyttjar NVIDIAs föroptimerade inferensmotorer, såsom TensorRT och TensorRT-LLM, för att säkerställa låg latens och hög genomströmning.
- **Skalbarhet:** NIM stöder autoskalning på Kubernetes, vilket möjliggör effektiv hantering av varierande arbetsbelastningar.
- **Säkerhet och kontroll:** Organisationer kan behålla kontroll över sina data och applikationer genom att självdrifta NIM-mikrotjänster på sin egen hanterade infrastruktur.
- **Standardiserade API:er:** NIM erbjuder branschstandard-API:er, vilket gör det enkelt att bygga och integrera AI-applikationer som chattbotar, AI-assistenter och mer.

NIM är en del av NVIDIA AI Enterprise, som syftar till att förenkla distribution och drift av AI-modeller, och säkerställer att de körs effektivt på NVIDIA GPU:er.

- Demo: Använda NVIDIA NIM för att anropa Phi-3.5-Vision-API [[Klicka på denna länk](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Köra Phi-3/3.5 Lokalt
Inferens i relation till Phi-3, eller vilken språkmodell som helst som GPT-3, avser processen att generera svar eller förutsägelser baserat på den input den får. När du ger en prompt eller fråga till Phi-3 använder den sitt tränade neurala nätverk för att dra slutsatsen om det mest sannolika och relevanta svaret genom att analysera mönster och samband i den data den tränats på.

**Hugging Face Transformer**
Hugging Face Transformers är ett kraftfullt bibliotek utformat för naturlig språkbehandling (NLP) och andra maskininlärningsuppgifter. Här är några viktiga punkter om det:

1. **Förtränade modeller**: Det erbjuder tusentals förtränade modeller som kan användas för olika uppgifter som textklassificering, namngiven enhetsigenkänning, frågesvar, sammanfattning, översättning och textgenerering.

2. **Ramverksinteroperabilitet**: Biblioteket stödjer flera djupinlärningsramverk, inklusive PyTorch, TensorFlow och JAX. Detta gör att du kan träna en modell i ett ramverk och använda den i ett annat.

3. **Multimodala funktioner**: Förutom NLP stödjer Hugging Face Transformers även uppgifter inom datorseende (t.ex. bildklassificering, objektigenkänning) och ljudbehandling (t.ex. taligenkänning, ljudklassificering).

4. **Användarvänlighet**: Biblioteket erbjuder API:er och verktyg för att enkelt ladda ner och finjustera modeller, vilket gör det tillgängligt för både nybörjare och experter.

5. **Community och resurser**: Hugging Face har ett livfullt community och omfattande dokumentation, tutorials och guider för att hjälpa användare att komma igång och få ut det mesta av biblioteket.
[officiell dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deras [GitHub-repo](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Detta är den mest använda metoden, men den kräver också GPU-acceleration. Scenarier såsom Vision och MoE kräver många beräkningar, vilket kommer vara mycket långsamt på CPU om de inte är kvantiserade.


- Demo: Använda Transformer för att anropa Phi-3.5-Instruct [Klicka på denna länk](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Använda Transformer för att anropa Phi-3.5-Vision [Klicka på denna länk](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Använda Transformer för att anropa Phi-3.5-MoE [Klicka på denna länk](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) är en plattform utformad för att göra det enklare att köra stora språkmodeller (LLM) lokalt på din maskin. Den stöder olika modeller som Llama 3.1, Phi 3, Mistral och Gemma 2, bland andra. Plattformen förenklar processen genom att paketera modellvikter, konfiguration och data i ett enda paket, vilket gör det mer tillgängligt för användare att anpassa och skapa sina egna modeller. Ollama är tillgängligt för macOS, Linux och Windows. Det är ett utmärkt verktyg om du vill experimentera med eller distribuera LLM utan att förlita dig på molntjänster. Ollama är det mest direkta sättet, du behöver bara köra följande kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) är Microsofts offline, på-enheten-runtime för att köra modeller som Phi helt på din egen hårdvara - ingen Azure-prenumeration, API-nyckel eller nätverksanslutning krävs. Den väljer automatiskt den bästa exekveringsleverantören tillgänglig (NPU, GPU eller CPU) och exponerar en OpenAI-kompatibel endpoint, så befintlig `openai`/Azure AI Inference SDK-kod kan peka mot den med minimala ändringar. Se [Foundry Local dokumentationen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) för att komma igång.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) är en plattformsoberoende accelerator för inferens och träning inom maskininlärning. ONNX Runtime för Generative AI (GENAI) är ett kraftfullt verktyg som hjälper dig att köra generativa AI-modeller effektivt över flera plattformar.

## Vad är ONNX Runtime?
ONNX Runtime är ett open-source projekt som möjliggör högpresterande inferens av maskininlärningsmodeller. Det stödjer modeller i Open Neural Network Exchange (ONNX)-formatet, vilket är en standard för att representera maskininlärningsmodeller. ONNX Runtime inferens kan möjliggöra snabbare kundupplevelser och lägre kostnader, genom att stödja modeller från djupinlärningsramverk såsom PyTorch och TensorFlow/Keras samt klassiska maskininlärningsbibliotek som scikit-learn, LightGBM, XGBoost, med flera. ONNX Runtime är kompatibelt med olika hårdvaror, drivrutiner och operativsystem, och levererar optimal prestanda genom att utnyttja hårdvaruacceleration där det är tillämpligt tillsammans med grafoptimeringar och transformeringar.

## Vad är Generativ AI?
Generativ AI avser AI-system som kan generera nytt innehåll, såsom text, bilder eller musik, baserat på den data de tränats på. Exempel inkluderar språkmodeller som GPT-3 och bildgenereringsmodeller som Stable Diffusion. ONNX Runtime för GenAI-biblioteket tillhandahåller den generativa AI-loopen för ONNX-modeller, inklusive inferens med ONNX Runtime, logit-behandling, sökning och sampling samt hantering av KV-cache.

## ONNX Runtime för GENAI
ONNX Runtime för GENAI utökar ONNX Runtimes kapaciteter för att stödja generativa AI-modeller. Här är några viktiga funktioner:

- **Brett plattformsstöd:** Det fungerar på olika plattformar, inklusive Windows, Linux, macOS, Android och iOS.
- **Modellstöd:** Det stödjer många populära generativa AI-modeller, som LLaMA, GPT-Neo, BLOOM och fler.
- **Prestandaoptimering:** Det inkluderar optimeringar för olika hårdvaruacceleratorer som NVIDIA GPU:er, AMD GPU:er med mera.
- **Användarvänlighet:** Det erbjuder API:er för enkel integration i applikationer, vilket låter dig generera text, bilder och annat innehåll med minimal kod.
- Användare kan anropa en hög-nivå generate()-metod, eller köra varje iteration av modellen i en loop, generera en token i taget och valfritt uppdatera generationsparametrar inuti loopen.
- ONNX runtime har också stöd för girig-/beam-sökning och TopP, TopK-sampling för att generera tokensekvenser och inbyggd logit-behandling som repetitionsstraff. Du kan också enkelt lägga till egen poängsättning.

## Kom igång
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


**Andra**

Utöver referensmetoderna ONNX Runtime, Ollama och Foundry Local, kan vi även fullborda referensen för kvantitativa modeller baserat på modellreferensmetoder som tillhandahålls av olika tillverkare. Såsom Apple MLX-ramverket med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU med mera. Du kan också få mer innehåll från [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lärt oss grunderna om Phi-3/3.5-familjen, men för att lära oss mer om SLM behöver vi mer kunskap. Du kan hitta svaren i Phi-3 Cookbook. Om du vill lära dig mer, vänligen besök [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->