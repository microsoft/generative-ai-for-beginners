# Introduktion till Små Språkmodeller för Generativ AI för Nybörjare
Generativ AI är ett fascinerande område inom artificiell intelligens som fokuserar på att skapa system som kan generera nytt innehåll. Detta innehåll kan sträcka sig från text och bilder till musik och till och med hela virtuella miljöer. En av de mest spännande tillämpningarna av generativ AI är inom området språkmodeller.

## Vad är Små Språkmodeller?

En Små Språkmodell (SLM) representerar en nedskalad variant av en stor språkmodell (LLM), som använder många av arkitekturprinciperna och teknikerna från LLM, samtidigt som den uppvisar en avsevärt reducerad beräkningsmässig belastning.

SLM är en undergrupp av språkmodeller designade för att generera mänsklig-lik text. Till skillnad från deras större motsvarigheter, som GPT-4, är SLM mer kompakta och effektiva, vilket gör dem idealiska för applikationer där beräkningsresurser är begränsade. Trots sin mindre storlek kan de fortfarande utföra en mängd olika uppgifter. Vanligtvis konstrueras SLM genom att komprimera eller destillera LLM, med målet att behålla en betydande del av den ursprungliga modellens funktionalitet och språkliga förmåga. Denna minskning i modellstorlek minskar den övergripande komplexiteten, vilket gör SLM mer effektiva både vad gäller minnesanvändning och beräkningskrav. Trots dessa optimeringar kan SLM fortfarande utföra en bred uppsättning naturlig språkbehandling (NLP) uppgifter:

- Textgenerering: Skapa sammanhängande och kontextuellt relevanta meningar eller stycken.
- Textkomplettering: Förutsäga och komplettera meningar baserat på en given prompt.
- Översättning: Översätta text från ett språk till ett annat.
- Sammanfattning: Kondensera långa texter till kortare, mer hanterbara sammanfattningar.

Om än med vissa kompromisser i prestanda eller djup i förståelsen jämfört med deras större motsvarigheter.

## Hur Fungerar Små Språkmodeller?
SLM tränas på enorma mängder textdata. Under träningen lär de sig språkets mönster och strukturer, vilket gör dem kapabla att generera text som är både grammatiskt korrekt och kontextuellt lämplig. Träningsprocessen innefattar:

- Datainsamling: Samla stora dataset med text från olika källor.
- Förbehandling: Rensa och organisera data för att göra den lämplig för träning.
- Träning: Använda maskininlärningsalgoritmer för att lära modellen att förstå och generera text.
- Finjustering: Justera modellen för att förbättra dess prestanda på specifika uppgifter.

Utvecklingen av SLM ligger i linje med det ökande behovet av modeller som kan distribueras i resursbegränsade miljöer, såsom mobila enheter eller edge computing-plattformar, där fullskaliga LLM kan vara opraktiska på grund av deras stora resurskrav. Genom att fokusera på effektivitet balanserar SLM prestation med tillgänglighet och möjliggör bredare användning över olika områden.

![slm](../../../translated_images/sv/slm.4058842744d0444a.webp)

## Lärandemål

I denna lektion hoppas vi introducera kunskap om SLM och kombinera den med Microsoft Phi-3 för att lära oss olika scenarier inom textinnehåll, vision och MoE.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är SLM?
- Vad är skillnaden mellan SLM och LLM?
- Vad är Microsoft Phi-3/3.5-familjen?
- Hur gör man inferens med Microsoft Phi-3/3.5-familjen?

Redo? Vi kör igång.

## Skillnaderna mellan Stora Språkmodeller (LLMs) och Små Språkmodeller (SLMs)

Både LLM och SLM bygger på grundläggande principer inom probabilistisk maskininlärning, och följer liknande tillvägagångssätt i arkitekturdesign, träningsmetoder, datagenereringsprocesser och modelevalueringsmetoder. Dock skiljer flera viktiga faktorer dessa två typer av modeller åt.

## Tillämpningar av Små Språkmodeller

SLM har ett brett spektrum av tillämpningar, inklusive:

- Chatbots: Erbjuda kundsupport och interagera med användare på ett konverserande sätt.
- Innehållsskapande: Assistera författare genom att generera idéer eller till och med utkast till hela artiklar.
- Utbildning: Hjälpa studenter med skrivuppgifter eller att lära sig nya språk.
- Tillgänglighet: Skapa verktyg för personer med funktionshinder, såsom text-till-tal system.

**Storlek**
  
En huvudsaklig skillnad mellan LLM och SLM ligger i modellernas skala. LLM, som ChatGPT (GPT-4), kan bestå av uppskattningsvis 1,76 biljoner parametrar, medan open source SLM som Mistral 7B är designade med betydligt färre parametrar—ungefär 7 miljarder. Denna skillnad beror främst på skillnader i modellarkitektur och träningsprocesser. Till exempel använder ChatGPT en självuppmärksamhetsmekanism inom en kodare-avkodare-struktur, medan Mistral 7B använder glidande fönster-uppmärksamhet, vilket möjliggör mer effektiv träning inom en endast-avkodare-modell. Denna arkitekturella skillnad har djupgående konsekvenser för komplexitet och prestanda hos modellerna.

**Förståelse**

SLM är vanligtvis optimerade för prestanda inom specifika domäner, vilket gör dem mycket specialiserade men potentiellt begränsade i deras förmåga att tillhandahålla bred kontextuell förståelse över flera kunskapsfält. I kontrast strävar LLM att simulera mänsklig-lik intelligens på en mer omfattande nivå. Tränade på stora, varierade dataset är LLM designade för att prestera bra över olika domäner, och erbjuder större mångsidighet och anpassningsförmåga. Därför är LLM mer lämpade för ett bredare spektrum av efterföljande uppgifter, såsom naturlig språkbehandling och programmering.

**Beräkning**

Träningen och driftsättningen av LLM är resursintensiva processer, som ofta kräver betydande beräkningsinfrastruktur, inklusive stora GPU-kluster. Till exempel kan träning av en modell som ChatGPT från grunden kräva tusentals GPU:er under långa perioder. I kontrast är SLM, med sina mindre antal parametrar, mer tillgängliga vad gäller beräkningsresurser. Modeller som Mistral 7B kan tränas och köras på lokala maskiner utrustade med måttliga GPU-kapaciteter, även om träning fortfarande kräver flera timmar över flera GPU:er.

**Bias**

Bias är ett känt problem i LLM, främst på grund av karaktären på träningsdata. Dessa modeller förlitar sig ofta på rådata, öppet tillgänglig på internet, vilket kan underrepresentera eller misstolka vissa grupper, introducera felaktig märkning, eller återspegla språkliga bias påverkade av dialekt, geografiska variationer och grammatiska regler. Dessutom kan komplexiteten i LLM-arkitekturer oavsiktligt förstärka bias, vilket kan gå obemärkt utan noggrann finjustering. Å andra sidan, eftersom SLM tränas på mer begränsade, domänspecifika dataset, är de naturligtvis mindre mottagliga för sådana bias, men inte immuna mot dem.

**Inferens**

Den reducerade storleken hos SLM ger dem en betydande fördel i inferenshastighet, vilket tillåter dem att generera resultat effektivt på lokal hårdvara utan behov av omfattande parallell bearbetning. I kontrast kräver LLM på grund av sin storlek och komplexitet ofta stora parallella beräkningsresurser för att uppnå acceptabla inferenstider. Förekomsten av flera samtidiga användare saktar dessutom ner LLMs svarstider, särskilt vid storskalig distribution.

Sammanfattningsvis, även om både LLM och SLM delar en grundläggande bas i maskininlärning, skiljer de sig avsevärt vad gäller modellstorlek, resurskrav, kontextuell förståelse, mottaglighet för bias och inferenshastighet. Dessa skillnader speglar deras respektive lämplighet för olika användningsområden, där LLM är mer mångsidiga men resurskrävande, och SLM erbjuder mer domänspecifik effektivitet med minskade beräkningsbehov.

***Notera: I denna lektion kommer vi att introducera SLM med Microsoft Phi-3 / 3.5 som exempel.***

## Introduktion till Phi-3 / Phi-3.5-familjen

Phi-3 / 3.5-familjen riktar sig främst mot text-, vision- och Agent (MoE) applikationsscenarier:

### Phi-3 / 3.5 Instruct

Huvudsakligen för textgenerering, chattkomplettering och innehållsinformationsextraktion, etc.

**Phi-3-mini**

Den 3,8 miljarder parametrars språkmodellen är tillgänglig på Microsoft Foundry, Hugging Face och Ollama. Phi-3-modeller presterar avsevärt bättre än språkmodeller av lika och större storlek på viktiga benchmarks (se benchmarks nedan, högre värden är bättre). Phi-3-mini presterar bättre än modeller dubbelt så stora, medan Phi-3-small och Phi-3-medium presterar bättre än större modeller, inklusive GPT-3.5.

**Phi-3-small & medium**

Med endast 7 miljarder parametrar slår Phi-3-small GPT-3.5T på en mängd språk-, resonemangs-, kodnings- och matematikbenchmarks.

Phi-3-medium med 14 miljarder parametrar fortsätter denna trend och presterar bättre än Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan se det som en uppgradering av Phi-3-mini. Parametrarna förblir oförändrade, men den förbättrar förmågan att stödja flera språk (stöder 20+ språk: arabiska, kinesiska, tjeckiska, danska, nederländska, engelska, finska, franska, tyska, hebreiska, ungerska, italienska, japanska, koreanska, norska, polska, portugisiska, ryska, spanska, svenska, thailändska, turkiska, ukrainska) och lägger till starkare stöd för långt kontext.

Phi-3.5-mini med 3,8 miljarder parametrar presterar bättre än språkmodeller av samma storlek och är jämförbar med modeller dubbelt så stora.

### Phi-3 / 3.5 Vision

Vi kan se Instruct-modellen i Phi-3/3.5 som Phis förmåga att förstå, och Vision är vad som ger Phi ögon att förstå världen.


**Phi-3-Vision**

Phi-3-vision, med endast 4,2 miljarder parametrar, fortsätter denna trend och presterar bättre än större modeller som Claude-3 Haiku och Gemini 1.0 Pro V på allmänna visuella resonemangsuppgifter, OCR och tabell- och diagramförståelseuppgifter.


**Phi-3.5-Vision**

Phi-3.5-Vision är också en uppgradering av Phi-3-Vision, med tillägg för stöd av flera bilder. Du kan se det som en förbättring av vision, där du inte bara kan se bilder utan även videor.

Phi-3.5-vision presterar bättre än större modeller som Claude-3.5 Sonnet och Gemini 1.5 Flash över OCR-, tabell- och diagramförståelseuppgifter och jämförbart på uppgifter för allmän visuell kunskapsresonemang. Stöder flerframes-inmatning, dvs utför resonemang på flera inmatningsbilder


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** möjliggör att modeller kan förtränas med mycket mindre beräkningsresurser, vilket innebär att du dramatiskt kan skala upp modell- eller datasetstorleken med samma beräkningsbudget som en tät modell. Specifikt bör en MoE-modell uppnå samma kvalitet som sin täta motsvarighet mycket snabbare under förträningen.

Phi-3.5-MoE består av 16x3,8 miljarder expertmoduler. Phi-3.5-MoE med endast 6,6 miljarder aktiva parametrar uppnår en liknande nivå av resonemang, språkförståelse och matematik som mycket större modeller.

Vi kan använda Phi-3/3.5-familjsmodellen baserat på olika scenarier. Till skillnad från LLM kan du distribuera Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheter.


## Hur man använder Phi-3/3.5-familjsmodeller

Vi hoppas använda Phi-3/3.5 i olika scenarier. Nästa steg är att använda Phi-3/3.5 baserat på olika scenarier.

![phi3](../../../translated_images/sv/phi3.655208c3186ae381.webp)

### Inferens via Moln-API:er

**Microsoft Foundry Modeller**

> **Notera:** GitHub Models avvecklas i slutet av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) är den direkta ersättaren.

Microsoft Foundry Models är det mest direkta sättet. Du kan snabbt få tillgång till Phi-3/3.5-Instruct-modellen via Foundry-modellkatalogen. Kombinerat med Azure AI Inference SDK / OpenAI SDK kan du använda API:et via kod för att slutföra Phi-3/3.5-Instruct-anropet. Du kan också testa olika effekter via Playground.

- Demo: Jämförelse av effekterna av Phi-3-mini och Phi-3.5-mini i kinesiska scenarier

![phi3](../../../translated_images/sv/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/sv/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Eller om vi vill använda vision- och MoE-modellerna kan du använda Microsoft Foundry för att slutföra anropet. Om du är intresserad kan du läsa Phi-3 Cookbook för att lära dig hur du anropar Phi-3/3.5 Instruct, Vision, MoE genom Microsoft Foundry [Klicka på denna länk](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Förutom den molnbaserade Microsoft Foundry Models-katalogen kan du också använda [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) för att slutföra relaterade anrop. Du kan besöka NVIDIA NIM för att slutföra API-anrop av Phi-3/3.5-familjen. NVIDIA NIM (NVIDIA Inference Microservices) är en uppsättning accelererade inferensmikrotjänster som är utformade för att hjälpa utvecklare att distribuera AI-modeller effektivt över olika miljöer, inklusive moln, datacenter och arbetsstationer.

Här är några nyckelfunktioner i NVIDIA NIM:

- **Enkel distribution:** NIM möjliggör distribution av AI-modeller med ett enda kommando, vilket gör det enkelt att integrera i befintliga arbetsflöden.

- **Optimerad prestanda:** Den utnyttjar NVIDIA:s föroptimerade inferensmotorer, såsom TensorRT och TensorRT-LLM, för att säkerställa låg latens och hög genomströmning.
- **Skalbarhet:** NIM stöder autoskalning på Kubernetes, vilket möjliggör effektiv hantering av varierande arbetsbelastningar.
- **Säkerhet och kontroll:** Organisationer kan behålla kontrollen över sina data och applikationer genom att självhosta NIM-mikrotjänster på sin egen hanterade infrastruktur.
- **Standard-API:er:** NIM tillhandahåller branschstandard-API:er, vilket gör det enkelt att bygga och integrera AI-applikationer som chattbotar, AI-assistenter och mer.

NIM är en del av NVIDIA AI Enterprise, som syftar till att förenkla distributionen och operationaliseringen av AI-modeller, för att säkerställa att de körs effektivt på NVIDIA-GPU:er.

- Demo: Använda NVIDIA NIM för att anropa Phi-3.5-Vision-API [[Klicka på denna länk](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Köra Phi-3/3.5 Lokalt
Inferens i relation till Phi-3, eller någon språkmodell som GPT-3, avser processen att generera svar eller förutsägelser baserat på den input den får. När du ger en prompt eller fråga till Phi-3 använder den sitt tränade neurala nätverk för att dra slutsatsen om det mest sannolika och relevanta svaret genom att analysera mönster och samband i den data den tränats på.

**Hugging Face Transformer**
Hugging Face Transformers är ett kraftfullt bibliotek designat för naturlig språkbehandling (NLP) och andra maskininlärningsuppgifter. Här är några viktiga punkter om det:

1. **Förtränade modeller**: Det erbjuder tusentals förtränade modeller som kan användas för olika uppgifter såsom textklassificering, namngiven entityigenkänning, frågesvar, sammanfattning, översättning och textgenerering.

2. **Ramverksinteroperabilitet**: Biblioteket stöder flera djupa inlärningsramverk, inklusive PyTorch, TensorFlow och JAX. Detta gör att du kan träna en modell i ett ramverk och använda den i ett annat.

3. **Multimodala möjligheter**: Utöver NLP stöder Hugging Face Transformers även uppgifter inom datorseende (t.ex. bildklassificering, objektigenkänning) och ljudbehandling (t.ex. taligenkänning, ljudklassificering).

4. **Lättanvändlighet**: Biblioteket erbjuder API:er och verktyg för att enkelt ladda ner och finjustera modeller, vilket gör det tillgängligt för både nybörjare och experter.

5. **Gemenskap och resurser**: Hugging Face har en levande gemenskap och omfattande dokumentation, handledningar och guider för att hjälpa användare att komma igång och få ut det mesta av biblioteket.
[officiell dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deras [GitHub-förråd](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Detta är den vanligaste använda metoden, men den kräver också GPU-acceleration. När allt kommer omkring kräver scenarier som Vision och MoE mycket beräkningar, vilket kommer att vara mycket långsamt på CPU om de inte kvantifieras.


- Demo: Använda Transformer för att anropa Phi-3.5-Instruct [Klicka på denna länk](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Använda Transformer för att anropa Phi-3.5-Vision [Klicka på denna länk](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Använda Transformer för att anropa Phi-3.5-MoE [Klicka på denna länk](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) är en plattform skapad för att göra det enklare att köra stora språkmodeller (LLM) lokalt på din maskin. Den stöder olika modeller som Llama 3.1, Phi 3, Mistral och Gemma 2, bland andra. Plattformen förenklar processen genom att paketera modellvikter, konfiguration och data i ett enda paket, vilket gör det mer tillgängligt för användare att anpassa och skapa egna modeller. Ollama finns tillgängligt för macOS, Linux och Windows. Det är ett utmärkt verktyg om du vill experimentera med eller distribuera LLM utan att förlita dig på molntjänster. Ollama är det mest direkta sättet, du behöver bara köra följande kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) är Microsofts offline, på-enheten-körtidsmiljö för att köra modeller som Phi helt på din egen hårdvara – inget Azure-abonnemang, API-nyckel eller nätverksanslutning behövs. Den väljer automatiskt den bästa exekveringsleverantören som finns tillgänglig (NPU, GPU eller CPU) och exponerar en OpenAI-kompatibel slutpunkt, så befintlig `openai`/Azure AI Inference SDK-kod kan peka på den med minimala ändringar. Se [Foundry Local dokumentationen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) för att komma igång.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) är en plattformsoberoende accelerator för inferens och träning av maskininlärning. ONNX Runtime för Generativ AI (GENAI) är ett kraftfullt verktyg som hjälper dig att köra generativa AI-modeller effektivt över olika plattformar.

## Vad är ONNX Runtime?
ONNX Runtime är ett open source-projekt som möjliggör inferens av maskininlärningsmodeller med hög prestanda. Det stöder modeller i Open Neural Network Exchange (ONNX)-formatet, vilket är en standard för att representera maskininlärningsmodeller. ONNX Runtime-inferens kan möjliggöra snabbare kundupplevelser och lägre kostnader, och stöder modeller från djupinlärningsramverk som PyTorch och TensorFlow/Keras samt klassiska maskininlärningsbibliotek som scikit-learn, LightGBM, XGBoost med flera. ONNX Runtime är kompatibel med olika hårdvaror, drivrutiner och operativsystem och ger optimal prestanda genom att utnyttja hårdvaruacceleratorer där det är tillämpligt tillsammans med grafoptimeringar och transformationer.

## Vad är Generativ AI?
Generativ AI avser AI-system som kan generera nytt innehåll, såsom text, bilder eller musik, baserat på den data de tränats på. Exempel inkluderar språkmodeller som GPT-3 och bildgenereringsmodeller som Stable Diffusion. ONNX Runtime för GenAI-biblioteket tillhandahåller den generativa AI-loopen för ONNX-modeller, inklusive inferens med ONNX Runtime, logitbearbetning, sökning och sampling samt KV-cachehantering.

## ONNX Runtime för GENAI
ONNX Runtime för GENAI utökar funktionaliteten i ONNX Runtime för att stödja generativa AI-modeller. Här är några viktiga funktioner:

- **Brett plattformsstöd:** Det fungerar på flera plattformar, inklusive Windows, Linux, macOS, Android och iOS.
- **Modellstöd:** Det stöder många populära generativa AI-modeller, såsom LLaMA, GPT-Neo, BLOOM och fler.
- **Prestandaoptimering:** Det inkluderar optimeringar för olika hårdvaruacceleratorer såsom NVIDIA GPU:er, AMD GPU:er och fler2.
- **Lättanvänt:** Det tillhandahåller API:er för enkel integration i applikationer, vilket gör att du kan generera text, bilder och annat innehåll med minimal kod.
- Användare kan anropa en högre nivå generate()-metod, eller köra varje iteration av modellen i en loop, generera en token åt gången och eventuellt uppdatera genereringsparametrar i loopen.
- ONNX Runtime har även stöd för greedy/beam-sökning och TopP, TopK-sampling för att generera tokensekvenser och inbyggd logitbearbetning som repetitionsstraff. Du kan också enkelt lägga till egen poängsättning.

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
### Demo: Använd ONNX Runtime GenAI för att anropa Phi-3.5-Vision


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

Förutom ONNX Runtime, Ollama och Foundry Local referensmetoder kan vi också fullborda referenser till kvantitativa modeller baserat på modellreferensmetoder som tillhandahålls av olika tillverkare. Som exempel Apple MLX-ramverket med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU med mera. Du kan också få mer innehåll från [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lärt oss grunderna i Phi-3/3.5-familjen, men för att lära oss mer om SLM behöver vi ytterligare kunskap. Du kan hitta svaren i Phi-3 Cookbook. Om du vill veta mer, vänligen besök [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->