# LLM ప్రొవైడర్ ఎంపిక మరియు కాన్ఫిగర్ చేసుకోవడం 🔑

అసైన్మెంట్లు ఒకటి లేదా ఎక్కువ లార్జ్ లాంగ్వేజ్ మోడల్ (LLM) డిప్లాయ్‌మెంట్లను OpenAI, Azure లేదా Hugging Face వంటి మద్దతు పొందిన సర్వీస్ ప్రొవైడర్ ద్వారా పనిచేయడానికి కూడా సెటప్ చేయవచ్చు. ఇవి ఒక _హోస్టెడ్ ఎండ్‌పాయింట్_ (API) అందిస్తాయి, దీన్ని సరైన ఆథెంటికేషన్ (API కీ లేదా టోకెన్) తో ప్రోగ్రామాటిక్‌గా యాక్సెస్ చేయవచ్చు. ఈ కోర్సులో, మనం ఈ ప్రొవైడర్ల గురించి చర్చిస్తాము:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) వివిధ మోడల్స్‌తో సహా ప్రాథమిక GPT సిరీస్.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) ఎంటర్‌ప్రైజ్ రెడీనెస్‌పై ఫోకస్‌తో OpenAI మోడల్స్ కోసం
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ఒకే ఎండ్‌పాయింట్ మరియు API కీతో OpenAI, Meta, Mistral, Cohere, Microsoft మరియు మరెన్నో నుంచి వందలాది మోడల్స్ అందుబాటులో (GitHub Models కి ప్రత్యామ్నాయం, ఇది జూలై 2026 చివరికి రిటైర్ అవుతుంది)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ఓపెన్-సోర్స్ మోడల్స్ మరియు ఇన్ఫరెన్స్ సర్వర్ కోసం
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) లేదా [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) మీరు మీ స్వంత డివైస్‌పై పూర్తిగా ఆఫ్లైన్‌గా మోడల్స్ నడపాలనుకుంటే, క్లౌడ్ సబ్‌స్క్రిప్షన్ అవసరం లేదు

**ఈ వ్యాయామాల కోసం మీ స్వంత ఖాతాలు ఉపయోగించాలి**. అసైన్మెంట్లు ఐచ్ఛికం, కాబట్టి మీ ఆసక్తుల ఆధారంగా మీరు ఒకటి, అంతా లేదా ఒకదానిని కూడా ఎంచుకోవచ్చు. సైగ్నప్ కోసం కొన్ని మార్గదర్శకాలు:

| సైనప్ | ఖర్చు | API కీ | ప్లేగ్రౌండ్ | వ్యాఖ్యలు |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ధరలు](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ప్రాజెక్ట్ బేస్డ్](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [నో-కోడ్, వెబ్](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | బహుళ మోడల్స్ అందుబాటులో ఉన్నాయి |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ధరలు](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK క్విక్స్టార్ట్](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [స్టూడియో క్విక్స్టార్ట్](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ప్రవేశం కోసం ముందుగా దరఖాస్తు చేయాలి](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ధరలు](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ప్రాజెక్ట్ అవలోకన పৃষ্ঠা](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry ప్లేగ్రౌండ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ఉచిత టియర్ అందుబాటులో ఉంది; ఒకే ఎండ్‌పాయింట్ + కీ బహుళ మోడల్ ప్రొవైడర్ల కోసం |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ధరలు](https://huggingface.co/pricing) | [అాక్సెస్ టోకెన్లు](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging చాట్](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging చాట్ పరిమితి ఉన్న మోడల్స్](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ఉచితం (మీ డివైస్‌పై నడుస్తుంది) | అవసరం లేదు | [లోకల్ CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | పూర్తిగా ఆఫ్లైన్, OpenAI-అనుకూల ఎండ్‌పాయింట్ |
| | | | | |

ఈ రిపాజిటరీని వేర్వేరు ప్రొవైడర్లతో ఉపయోగించడానికి _కాన్ఫిగర్_ చేయడానికి క్రింద దగ్గర సూచనలను అనుసరించండి. ఒక నిర్దిష్ట ప్రొవైడర్ అవసరమయ్యే అసైన్మెంట్ల ఫైల్ పేరులో ఈ ట్యాగ్లలో ఒకటి ఉంటుంది:

- `aoai` - Azure OpenAI ఎండ్‌పాయింట్, కీ అవసరం
- `oai` - OpenAI ఎండ్‌పాయింట్, కీ అవసరం
- `hf` - Hugging Face టోకెన్ అవసరం
- `githubmodels` - Microsoft Foundry Models ఎండ్‌పాయింట్, కీ అవసరం (GitHub Models జూలై 2026 చివరికి రిటైర్ అవుతుంది)

మీరు ఒకటి, ఎవరూ లేకపోవచ్చు లేదా అందరినీ కాన్ఫిగర్ చేయవచ్చు. సంబంధిత అసైన్మెంట్లు అవసరమైన ఆథెంటికేషన్ లేకపోతే ఎర్రర్ ఇవ్వగలవు.

## `.env` ఫైల్ సృష్టించండి

మీరు ఇప్పటికే పై సూచనల్ని చదివి సంబంధిత ప్రొవైడర్‌తో సైన్ అప్ చేసి అవసరమైన ఆథెంటికేషన్ క్రెడెన్షియల్స్ (API_KEY లేదా టోకెన్) పొందారని మేము అనుకుంటున్నాము. Azure OpenAI సందర్భంలో, మీరు Azure OpenAI సేవ (ఎండ్‌పాయింట్) లో కనీసం ఒక GPT మోడల్‌ను చాట్ కంప్లిషన్ కోసం డిప్లాయ్ కలిగి ఉన్నారని కూడా మేము అనుకుంటున్నాము.

తదుపరి దశ మీ **స్థానిక పర్యావరణ వేరియబుల్‌లను** క్రింది విధంగా కాన్ఫిగర్ చేయడం:

1. రూట్ ఫోల్డర్‌లో `.env.copy` ఫైల్‌ని చూడండి, ఇందులో ఈ రకమైన కంటెంట్ ఉంటుంది:

   ```bash
   # OpenAI ప్రొవైడర్
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundryలో Azure OpenAI
   ## (Azure OpenAI Service ఇప్పుడు Microsoft Foundry భాగం: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # డిఫాల్ట్ సెట్ అయింది! (ప్రస్తుత స్థిరమైన GA API వెర్షన్)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry మోడళ్లు (బహు-ప్రొవైడర్ మోడల్ క్యాటలాగ్, GitHub మోడళ్లను మార్చింది, జూలై 2026 చివరగా అవినీతి అవుతుంది)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ఆ ఫైల్‌ను క్రింద ఇచ్చిన కమాండ్ ఉపయోగించి `.env` గా కాపీ చేయండి. ఈ ఫైల్ _gitignore_ లో ఉంటుంది, రహస్యాలను సురక్షితంగా ఉంచడానికి.

   ```bash
   cp .env.copy .env
   ```

3. ఈవాటిని భర్తీ చేయండి (ఇన్పుట్ లోని `=` కుడి పక్షంలో ప్లేస్‌హోల్డర్లను మార్చండి) తదుపరి సెక్షన్ లో వివరిస్తున్న విధంగా.

4. (ఐచ్ఛికం) మీరు GitHub Codespaces ఉపయోగిస్తే, ఈ రిపాజిటరీకి సంబంధించిన _Codespaces సీక్రెట్స్_ గా ఎన్విరాన్‌మెంట్ వేరియబుల్స్ నిల్వ చేయవచ్చు. అప్పుడు, మీరు స్థానిక `.env` ఫైల్ సెటప్ చేయాల్సిన అవసరం లేదు. **అయితే, ఈ ఆప్షన్ GitHub Codespaces ఉపయోగిస్తున్నప్పుడు మాత్రమే పనిచేస్తుంది**. Docker Desktop ఉపయోగిస్తే `.env` ఫైల్ సెటప్ ఇంకా అవసరం.

## `.env` ఫైల్ పూరించండి

వేరియబుల్ పేర్లను త్వరగా చూస్తాము అంటే అవి ఏం సూచిస్తున్నాయన్నది అర్థం చేసుకోవడానికి:

| వేరియబుల్  | వివరణ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ఇది మీరు ప్రొఫైల్‌లో సెటప్ చేసిన యూజర్ యాక్సెస్ టోకెన్ |
| OPENAI_API_KEY | ఇది సర్వీస్ ఉపయోగించడానికి ఆథరైజేషన్ కీ, నాన్-Azure OpenAI ఎండ్‌పాయింట్ల కోసం |
| AZURE_OPENAI_API_KEY | ఈ సర్వీస్‌కి ఉపయోగించే ఆథరైజేషన్ కీ |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI రిసోర్స్‌కి డిప్లాయ్ చేసిన ఎండ్‌పాయింట్ |
| AZURE_OPENAI_DEPLOYMENT | ఇది _టెక్స్ట్ జనరేషన్_ మోడల్ డిప్లాయ్‌మెంట్ ఎండ్‌పాయింట్ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ఇది _టెక్స్ట్ ఎంబెడ్డింగ్స్_ మోడల్ డిప్లాయ్‌మెంట్ ఎండ్‌పాయింట్ |
| AZURE_INFERENCE_ENDPOINT | ఇది మీ Microsoft Foundry ప్రాజెక్ట్ ఎండ్‌పాయింట్, Microsoft Foundry Models కోసం |
| AZURE_INFERENCE_CREDENTIAL | ఇది Microsoft Foundry ప్రాజెక్ట్ ఆ PI కీ |
| | |

గమనిక: చివరి రెండు Azure OpenAI వేరియబుల్స్ చాట్ కంప్లిషన్ (టెక్స్ట్ జనరేషన్) మరియు వెక్టర్ సెర్చ్ (ఎంబెడ్డింగ్స్) కోసం డిఫాల్ట్ మోడల్‌ను సూచిస్తాయి. వాటిని సెటప్ చేయడానికి మార్గదర్శకాలు సంబంధిత అసైన్మెంట్స్ లో ఇవ్వబడ్డాయి.

## Azure OpenAI కాన్ఫిగర్ చేయండి: పోర్టల్ నుండి

> **గమనిక:** Azure OpenAI సర్వీస్ ఇప్పుడు [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) భాగం అయింది. వనరులు మరియు డిప్లాయ్‌మెంట్లు ఇంకా Azure పోర్టల్‌లో కనపడతాయి, కానీ రోజూ మోడల్ నిర్వహణ (డిప్లాయ్‌మెంట్లు, ప్లేగ్రౌండ్, మానిటరింగ్) ఇప్పుడు Foundry పోర్టల్ లో జరుగుతుంది, పాత "Azure OpenAI స్టూడియో"కి బదులు.

Azure OpenAI ఎండ్‌పాయింట్ మరియు కీ విలువలు [Azure పోర్టల్](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) లో ఉంటాయి కాబట్టి అక్కడ నుంచే ప్రారంభిద్దాం.

1. [Azure పోర్టల్](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) కి వెళ్లండి
1. సైడ్బార్ (ఎడమ మెనూ)లో ఉన్న **కీస్ మరియు ఎండ్‌పాయింట్** ఎంపికపై క్లిక్ చేయండి.
1. **కీస్ చూపించు** పై క్లిక్ చేయండి - మీరు KEY 1, KEY 2 మరియు ఎండ్‌పాయింట్ చూడగలరు.
1. AZURE_OPENAI_API_KEY కు KEY 1 విలువ ఉపయోగించండి
1. AZURE_OPENAI_ENDPOINT కు ఎండ్‌పాయింట్ విలువ ఉపయోగించండి

తరువాత, మనం డిప్లాయ్ చేసిన నిర్దిష్ట మోడల్స్ కోసం ఎండ్‌పాయింట్లను కావాలి.

1. Azure OpenAI రిసోర్స్ కోసం సైడ్బార్‌లో **మోడల్ డిప్లాయ్‌మెంట్లు** ఎంపికపై క్లిక్ చేయండి.
1. లక్ష్య పేజీలో **Microsoft Foundry పోర్టల్ కి విభక్తి ఇవ్వండి** (లేదా మీ వనరు రకం ఆధారంగా **డిప్లాయ్‌మెంట్లు నిర్వహించండి**) పై క్లిక్ చేయండి

ఇది Microsoft Foundry పోర్టల్‌కి తీసుకువెళ్లుతుంది, అక్కడ మిగతా విలువలు క్రింద వివరించినట్లు పొందుతాము.

## Azure OpenAI కాన్ఫిగర్ చేయండి: Microsoft Foundry పోర్టల్ నుండి

1. పై విధంగా మీ వనరుని ఉపయోగించి [Microsoft Foundry పోర్టల్](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) కి వెళ్లండి.
1. ప్రస్తుతమున్న మోడల్స్ చూడాలంటే **డిప్లాయ్‌మెంట్లు** టాబ్ (సైడ్బార్, ఎడము) పై క్లిక్ చేయండి.
1. కావలసిన మోడల్ డిప్లాయ్ కాకపోతే, [మోడల్ క్యాటలాగ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) నుండి దాన్ని డిప్లాయ్ చేయడానికి **Deploy model** ఉపయోగించండి.
1. మీరు _టెక్స్ట్-జనరేషన్_ మోడల్ అవసరం - మేము సూచిస్తున్నది: **gpt-4o-mini**
1. మీరు _టెక్స్ట్-ఎంబెడ్డింగ్_ మోడల్ అవసరం - మేము సూచిస్తున్నది **text-embedding-3-small**

ఇప్పుడు పర్యావరణ వేరియబుల్స్‌ను _డిప్లాయ్‌మెంట్_ పేరును ప్రతిబింబించ도록 నవీకరించండి. ఇది సాధారణంగా మోడల్ పేరుతో సమానం ఉంటుంది, మీరు స్పష్టంగా మార్చకపోతే. ఉదాహరణకు:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**పని పూర్తయ్యాక .env ఫైల్ సేవ్ చేయడం మర్చిపోవద్దు**. ఇప్పుడు మీరు ఫైల్ నుండి బయటకు వచ్చి నోట్‌బుక్ నడపడం కోసం సూచనలను అనుసరించండి.

## OpenAI కాన్ఫిగర్ చేయండి: ప్రొఫైల్ నుండి

మీ OpenAI API కీ మీ [OpenAI ఖాతాలో](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ఉంటుంది. మీ దగ్గర అది లేకపోతే, ఖాతాకు సైన్ అప్ చేసి API కీ సృష్టించండి. కీ పొందిన తర్వాత, `.env` ఫైల్ లో `OPENAI_API_KEY` వేరియబుల్ ను పూరించండి.

## Hugging Face కాన్ఫిగర్ చేయండి: ప్రొఫైల్ నుండి

మీ Hugging Face టోకెన్ మీ ప్రొఫైల్ లో [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) క్రింద ఉంటుంది. దీన్ని పబ్లిక్‌గా పోస్ట్ లేదా పంచుకోకండి. దీనికి బదులు, ఈ ప్రాజెక్టు కోసం కొత్త టోకెన్ సృష్టించి, `.env` ఫైల్ లో `HUGGING_FACE_API_KEY` వేరియబుల్ క్రింద కాపీ చేయండి. _గమనిక:_ ఇది సాంకేతికంగా API కీ కాదు కానీ ఆథెంటికేషన్ కోసం ఉపయోగిస్తారు కాబట్టి అనుసరణ కోసం ఆ పేరును ఉంచాము.

## Microsoft Foundry Models కాన్ఫిగర్ చేయండి: పోర్టల్ నుండి

> **గమనిక:** GitHub Models జూలై 2026 చివరికి రిటైర్ అవుతోంది. Microsoft Foundry Models ప్రత్యామ్నాయం, అదే ఉచిత ట్రై మోడల్ క్యాటలాగ్ మరియు Azure AI ఇన్ఫరెన్స్ SDK / OpenAI SDK అనుభవాన్ని ఇస్తుంది.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) కి వెళ్లి Foundry ప్రాజెక్ట్ సృష్టించండి (లేదా ఓపెన్ చేయండి).
1. [మోడల్ క్యాటలాగ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) బ్రౌజ్ చేసి, ఉదాహరణకు `gpt-4o-mini` మోడల్‌ను డిప్లాయ్ చేయండి.
1. ప్రాజెక్ట్ యొక్క **అవలోకనం** పేజీపై నుండి **ఎండ్‌పాయింట్** మరియు **API కీ**ని కాపీ చేసుకోండి.
1. `.env` ఫైల్‌లో `AZURE_INFERENCE_ENDPOINT` కు ఎండ్‌పాయింట్ విలువ మరియు `AZURE_INFERENCE_CREDENTIAL` కు కీ విలువ ఉపయోగించండి.

## ఆఫ్లైన్ / లోకల్ ప్రొవైడర్లు

మీరు మ‌రే క్లౌడ్ సబ్‌స్క్రిప్షన్ ఉపయోగించకూడదనుకుంటే, సారూప్య ఓపెన్ మోడల్స్‌ను నేరుగా మీ డివైస్‌పై నడపవచ్చు:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft యొక్క ఆన్-డివైస్ రన్‌టైమ్. ఇది ఆటోమేటిక్‌గా ఉత్తమ కార్యాచరణ ప్రొవైడర్‌ను (NPU, GPU, లేదా CPU) ఎంచుకుంటుంది మరియు OpenAI-అనుకూల ఎండ్‌పాయింట్ ను అందిస్తుంది, కాబట్టి ఈ కోర్సులో ఉన్న చాలా సాంపుల్ కోడ్‌ను తక్కువ మార్పులతో ఉపయోగించవచ్చు. ప్రారంభించడానికి [Foundry Local డాక్యూమెంటేషన్](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) చూడండి, లేదా Windows మీద `winget install Microsoft.FoundryLocal` / macOS మీద `brew install microsoft/foundrylocal/foundrylocal` ఉపయోగించి ఇన్స్టాల్ చేయండి.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, మరియు Gemma వంటి ఓపెన్ మోడల్స్‌ను లోకల్‌గా నడపడానికి ఒక პოპულర్ ప్రత్యామ్నాయం.


రెండు ఆప్షన్లను ఉపయోగించే ప్రాయోగిక ఉదాహరణల కోసం [పాఠం 19: SLMలతో నిర్మాణం](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) చూడండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->