# LLM ప్రొవైడర్ ఎంచుకోవడం & కాన్ఫిగర్ చేయడం 🔑

అసైన్మెంట్లు **గాని** ఒక లేదా ఎక్కువ Large Language Model (LLM) డిప్లాయ్‌మెంట్‌లతో పనిచేయడానికి సపోర్ట్ చేసే సర్వీస్ ప్రొవైడర్‌లైన OpenAI, Azure లేదా Hugging Face ద్వారా సెటప్ చేయబడవచ్చు. ఇవి మనం సరైన క్రెడెన్షియల్స్ (API కీ లేదా టోకెన్)తో ప్రోగ్రామేటిక్గా 접근ించగల _హోస్టెడ్ ఎండ్‌పాయింట్_ (API)ని అందిస్తాయి. ఈ కోర్సులో, మేము ఈ ప్రొవైడర్‌ల గురించి చర్చిస్తున్నాము:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) వివిధ మోడళ్ళతో పాటు కోర్ GPT సిరీస్‌ను కలిగి ఉంది.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) వెనుక OpenAI మోడళ్ళ కోసం ఎంటర్‌ప్రైజ్ రెడినెస్‌పై దృష్టి సారించి ఉంటుంది
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ఒకే ఎండ్‌పాయింట్ మరియు API కీతో OpenAI, Meta, Mistral, Cohere, Microsoft మరియు మరెన్నో నుండి హండ్రడ్ల మోడళ్ళను యాక్సెస్ చేయడానికి (GitHub Models స్థానంలో, ఇది 2026 జూలై చివరిలో విరమించనుంది)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ఓపెన్-సోర్స్ మోడళ్ళ కోసం మరియు ఇన్‌ఫెరెన్స్ సర్వర్ కోసం
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) లేదా [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) మీరు మీ స్వంత పరికరంలో పూర్తి గా ఆఫ్‌లైన్‌గా మోడళ్లను నడిపించడానికి కావాలనుకుంటే, ఎలాంటి క్లౌడ్ సబ్స్క్రిప్షన్ అవసరం లేదు

**ఈ వ్యాయామాల కోసం మీ స్వంత అకౌంట్లు ఉపయోగించాల్సి ఉంటుంది**. అసైన్మెంట్లు ఐచ్ఛికం కాబట్టి మీరు ఒకటి, అందరినీ లేదా ఎవరినీ సెటప్ చేయకపోవచ్చు - మీ ఆసక్తుల ఆధారంగా ప్రొవైడర్లు ఎంచుకోండి. సైన్ అప్ కోసం కొన్ని మార్గదర్శకాలు:

| సైన్ అప్ | ఖర్చు | API కీ | ప్లేగ్రౌండ్ | వ్యాఖ్యలు |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ధరల వివరాలు](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ప్రాజెక్ట్ ఆధారిత](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [నో-కోడ్, వెబ్](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | అనేక మోడళ్ళు उपलब्धo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ధరల వివరాలు](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK క్విక్ స్టార్ట్](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [స్టూడియో క్విక్ స్టార్ట్](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ప్రాప్యతకు ముందుగా అప్లై చేయాలి](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ధరల వివరాలు](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ప్రాజెక్ట్ అవలోకనం](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry ప్లేగ్రౌండ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ఉచిత టియర్ అందుబాటులో ఉంది; అనేక మోడల్ ప్రొవైడర్లకు ఒకే ఎండ్‌పాయింట్ + కీ |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ధరల వివరాలు](https://huggingface.co/pricing) | [యాక్సెస్ టోకెన్లు](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat కి పరిమిత మోడళ్ళు ఉన్నాయి](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ఉచితం (మీ పరికరంపై నడుస్తుంది) | అవసరం లేదు | [లోకల్ CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | పూర్తి ఆఫ్‌లైన్, OpenAI-అనుకూల ఎండ్‌పాయింట్ |
| | | | | |

ఈ రిపోజిటరీని విభిన్న ప్రొవైడర్‌లతో ఉపయోగించడానికి _కాన్ఫిగర్_ చేయడానికి క్రింద ఇచ్చిన దిశానిర్దేశాలను అనుసరించండి. నిర్దిష్ట ప్రొవైడర్ అవసరమైన అసైన్మెంట్ల ఫైల్ పేరులో ఈ ట్యాగ్‌లలో ఒకటి ఉంటుంది:

- `aoai` - Azure OpenAI ఎండ్‌పాయింట్, కీ అవసరం
- `oai` - OpenAI ఎండ్‌పాయింట్, కీ అవసరం
- `hf` - Hugging Face టోకెన్ అవసరం
- `githubmodels` - Microsoft Foundry Models ఎండ్‌పాయింట్, కీ అవసరం (GitHub Models 2026 జూలై చివరిలో విరమించనుంది)

మీరు ఒకటి, ఎటువంటి లేదా అన్ని ప్రొవైడర్‌లను కాన్ఫిగర్ చేయవచ్చు. సంబంధిత అసైన్మెంట్లు క్రెడెన్షియల్స్ లేమి ఐతే error చూపిస్తాయి.

## `.env` ఫైల్ సృష్టించండి

మీరు ఇప్పటికే పై మార్గదర్శకాలను చదివి, సంబంధిత ప్రొవైడర్‌లో సైన్ అప్ చేసి అవసరమైన ప్రామాణీకరణ క్రెడెన్షియల్స్ (API_KEY లేదా టోకెన్) పొందిందని మేము అనుకుంటున్నాము. Azure OpenAI సందర్భంలో, మీరు కనీసం ఒక GPT మోడల్‌తో Azure OpenAI సర్వీస్ (ఎండ్‌పాయింట్) ని సరైనDeployment తో కలిగి ఉండాలి అని భావిస్తున్నాము.

తర్వాతి దశ మీ **లోకల్ ఎన్విరాన్‌మెంట్ వేరియబుల్స్**ను కింది విధంగా కాన్ఫిగర్ చేయడం:

1. రూట్ ఫోల్డర్ లో `.env.copy` ఫైల్ ఉన్నదో చూస్తారు, అది ఈ విధంగా ఉంటుంది:

   ```bash
   # OpenAI ప్రొవైడర్
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## మైక్రోసాఫ్ట్ ఫౌండ్రీలో ఆజ్యూర్ OpenAI
   ## (ఆజ్యూర్ OpenAI సేవ ఇప్పుడు మైక్రోసాఫ్ట్ ఫౌండ్రీలో భాగంగా ఉంది: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # డిఫాల్ట్ సెట్ చేయబడింది! (ప్రస్తుత స్థిరమైన GA API వెర్షన్)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## మైక్రోసాఫ్ట్ ఫౌండ్రీ మోడల్స్ (బహుముఖ ప్రొవైడర్ మోడల్ క్యాటలాగ్, గిట్హబ్ మోడల్స్‌ను మార్చుతుంది, జూలై 2026 చివరికి వదిలివేస్తుంది)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## హగ్గింగ్ ఫేస్
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ఆ ఫైల్‌ను `.env`గా కాపీ చేయడానికి క్రింద ఇచ్చిన కమాండ్ ఉపయోగించండి. ఈ ఫైల్ _gitignore_ లో ఉంటుంది, రహస్యాలు సురక్షితం.

   ```bash
   cp .env.copy .env
   ```

3. విలువలను పూరించండి (`=`కి కుడివైపున ఉన్న ప్లేస్‌హోల్డర్లను మార్చండి) తదుపరి విభాగంలో వివరించిన విధంగా.

4. (ఐచ్ఛికం) మీరు GitHub Codespaces ఉపయోగిస్తే, మీరు ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను ఈ రిపోజిటరీకి సంబంధించిన _Codespaces రహస్యాలు_గా సేవ్ చేయవచ్చు. ఆ సందర్భంలో, మీరు లోకల్ .env ఫైల్ సెటప్ చేయాల్సిన అవసరం లేదు. ** అయితే, ఈ ఐచ్ఛికం GitHub Codespaces ఉపయోగించే సందర్భంలో మాత్రమే పనిచేస్తుంది.** మీరు Docker Desktop ఉపయోగిస్తే ఇంకా .env ఫైల్ సెటప్ చేయాలి.

## `.env` ఫైల్‌ను పూరించండి

వాటి అర్థం ఏమిటో అర్థం చేసుకునేందుకు వేరియబుల్ నేంలను త్వరితంగా చూద్దాం:

| వేరియబుల్  | వివరణ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | మీరు మీ ప్రొఫైల్‌లో సెటప్ చేసిన యూజర్ యాక్సెస్ టోకెన్ |
| OPENAI_API_KEY | ఆ సర్వీస్ స్థాయిలో ఉపయోగించే అథారైజేషన్ కీ, Azure OpenAI కాకుండా ఉన్న ఎండ్‌పాయింట్లు కోసం |
| AZURE_OPENAI_API_KEY | ఆ సర్వీస్ కోసం అథారైజేషన్ కీ |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI వనరు కోసం డిప్లాయ్ చేసిన ఎండ్‌పాయింట్ |
| AZURE_OPENAI_DEPLOYMENT | _టెక్క్ జనరేషన్_ మోడల్ డిప్లాయ్‌మెంట్ ఎండ్‌పాయింట్ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _టెక్క్ ఎంబెడ్డింగ్స్_ మోడల్ డిప్లాయ్‌మెంట్ ఎండ్‌పాయింట్ |
| AZURE_INFERENCE_ENDPOINT | మీ Microsoft Foundry ప్రాజెక్ట్ ఎండ్‌పాయింట్, Microsoft Foundry Models కోసం |
| AZURE_INFERENCE_CREDENTIAL | మీ Microsoft Foundry ప్రాజెక్ట్ API కీ |
| | |

గమనిక: చివరి రెండు Azure OpenAI వేరియబుల్స్ చాట్ కంప్లీషన్ (టెక్క్ జనరేషన్) మరియు వెక్టర్ సెర్చ్ (ఎంబెడ్డింగ్స్) కొరకు డిఫాల్ట్ మోడల్‌ను ప్రతిబింబిస్తాయి. వాటిని సెటప్ చేయడానికి సూచనలు సంబంధిత అసైన్మెంట్లలో ఇవ్వబడతాయి.

## Azure OpenAI ను కాన్ఫిగర్ చేయడం: పోర్టల్ నుండి

> **గమనిక:** Azure OpenAI సర్వీస్ ఇప్పుడు [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) లో భాగంగా ఉంది. వనరులు మరియు డిప్లాయ్‌మెంట్‌లు ఇంకా Azure పోర్టల్‌లో కనిపిస్తాయి, కానీ రోజువారీ మోడల్ నిర్వహణ (డిప్లాయ్‌మెంట్లు, ప్లేగ్రౌండ్, మానిటరింగ్) ఇప్పుడు పాత 'Azure OpenAI స్టూడియో'కి బదులు Foundry పోర్టల్‌లో జరుగుతుంది.

Azure OpenAI ఎండ్‌పాయింట్ మరియు కీ విలువలు [Azure పోర్టల్](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) లో ఉంటాయి కాబట్టి అక్కడినుంచి ప్రారంభిద్దాం.

1. [Azure పోర్టల్](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) కి వెళ్లండి
1. సైడ్‌బార్‌లో (ఎడమ మెను) **Keys and Endpoint** ఎంపిక క్లిక్ చేయండి.
1. **Show Keys** క్లిక్ చేయండి - మీరు KEY 1, KEY 2 మరియు ఎండ్‌పాయింట్‌ని చూడగలరు.
1. AZURE_OPENAI_API_KEY కోసం KEY 1 విలువను ఉపయోగించండి
1. AZURE_OPENAI_ENDPOINT కోసం ఎండ్‌పాయింట్ విలువను ఉపయోగించండి

తరువాత, మనం డిప్లాయ్ చేసిన ప్రత్యేక మోడల్స్ కోసం ఎండ్‌పాయింట్లను అవసరం.

1. Azure OpenAI వనరుకు బలమైన సైడ్‌బార్‌లో **Model deployments** ఎంపిక క్లిక్ చేయండి.
1. గమ్యస్థల పేజీలో, **Go to Microsoft Foundry portal** (లేదా **Manage Deployments**, మీ వనరు రకం ఆధారంగా) క్లిక్ చేయండి

ఇది Microsoft Foundry పోర్టల్‌కు తీసుకెళుతుంది, అక్కడ మేము క్రింద వివరించిన ఇతర విలువలను కనుగొంటాము.

## Microsoft Foundry పోర్టల్ నుండి Azure OpenAI కాన్ఫిగర్ చేయడం

1. పై చెప్పినట్లుగా మీ వనరువరపు ద్వారా [Microsoft Foundry పోర్టల్](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) కి వెళ్లండి.
1. సైడ్‌బార్‌లో ఎడమవైపు **Deployments** ట్యాబ్ క్లిక్ చేసి ప్రస్తుత డిప్లాయ్ అయిన మోడల్స్ చూడండి.
1. మీ కోరుకున్న మోడల్ డిప్లాయ్ కాలేదంటే, [మోడల్ క్యాటలాగ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) నుండి అదే డిప్లాయ్ చేయడానికి **Deploy model** ఉపయోగించండి.
1. ఒక _టెక్క్-జనరేషన్_ మోడల్ అవసరం — మేము సిఫార్సు చేస్తున్నాము: **gpt-5-mini**
1. ఒక _టెక్క్-ఎంబెడ్డింగ్_ మోడల్ అవసరం — మేము సిఫార్సు చేస్తున్నాము: **text-embedding-3-small**

ఇప్పుడు డిప్లాయ్‌మెంట్ పేరు ప్రతిబింబించేలా ఎన్విరాన్‌మెంట్ వేరియబుల్స్ నవీకరించండి. మీరు స్పష్టంగా మార్చకపోతే, ఇది సాధారణంగా మోడల్ పేరుతో సమానమై ఉంటుంది. ఉదాహరణకు, మీరు ఇలా ఉండవచ్చు:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**పూర్తయిన తర్వాత .env ఫైల్ సేవ్ చేయడం మర్చిపోకండి**. ఇప్పుడు మీరు ఫైల్నుంచి బయటికి వచ్చి నోట‌బుక్ నడిపించే సూచనలకు తిరిగి వెళ్లండి.

## ప్రొఫైల్ నుండి OpenAI కాన్ఫిగర్ చేయడం

మీ OpenAI API కీ మీ [OpenAI ఖాతాలో](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) కనుగొనవచ్చు. మీకు API కీ అందుముందుగా మీరు అకౌంట్ క్రియేట్ చేసుకోవాలి. కీ వచ్చిన తరువాత `.env` ఫైల్‌లో `OPENAI_API_KEY` వేరియబుల్ ను పూరించండి.

## ప్రొఫైల్ నుండి Hugging Face కాన్ఫిగరేషన్

మీ Hugging Face టోకెన్ మీ ప్రొఫైల్‌లో [యాక్సెస్ టోకెన్స్](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) లో ఉంటుంది. దయచేసి వీటిని పబ్లిక్‌గా పోస్ట్ చేయవద్దు లేదా పంచుకోవద్దు. ఈ ప్రాజెక్టు కోసం కొత్త టోకెన్ సృష్టించి, దాన్ని `.env` ఫైల్‌లో `HUGGING_FACE_API_KEY` వేరియబుల్ క్రింద కాపీ చేయండి. _గమనిక:_ ఇది సాంకేతికంగా API కీ కాదు కానీ ఆథెంటికేషన్ కొరకు ఉపయోగించే టోకెన్ కాబట్టి, అనుసరించడానికి అదే పేరు కల్పించాము.

## పోర్టల్ నుండి Microsoft Foundry Models కాన్ఫిగర్ చేయడం

> **గమనిక:** GitHub Models 2026 జూలై చివరిలో విరమించనుంది. Microsoft Foundry Models ప్రత్యక్ష మార్చు, అదే ఉచిత ప్రయోగం కలిగిన మోడల్ క్యాటలాగ్ మరియు Azure AI ఇన్ఫెరెన్స్ SDK / OpenAI SDK అనుభవాన్ని అందిస్తుంది.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) కి వెళ్లి Foundry ప్రాజెక్ట్‌ని సృష్టించండి (లేదా తెరవండి).
1. [మోడల్ క్యాటలాగ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ని బ్రౌజ్ చేసి `gpt-5-mini` వంటి మోడల్ డిప్లాయ్ చేయండి.
1. ప్రాజెక్ట్ యొక్క **అవలోకనం** పేజీలో ఎండ్‌పాయింట్ మరియు API కీని కాపీ చేయండి.
1. `.env` ఫైల్‌లో `AZURE_INFERENCE_ENDPOINT` కోసం ఎండ్‌పాయింట్ విలువను, `AZURE_INFERENCE_CREDENTIAL` కోసం కీ విలువను ఉపయోగించండి.

## ఆఫ్‌లైన్ / లోకల్ ప్రొవైడర్లు

క్లౌడ్ సబ్స్క్రిప్షన్ ఉపయోగించకూడదని మీరు కోరుకుంటే, సరిపోయే ఓపెన్ మోడళ్ళను మీ స్వంత పరికరంలో నేరుగా నడిపించవచ్చు:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft యొక్క పరికరంపై రన్‌టైమ్. ఇది ఆటోమేటిగ్గా ఉత్తమ ఎగ్జిక్యూషన్ ప్రొవైడర్‌ను (NPU, GPU లేదా CPU) ఎంచుకుంటుంది మరియు OpenAI-అనుకూల ఎండ్‌పాయింట్‌ని అందిస్తుంది, కాబట్టి ఈ కోర్సులోని నమూనా కోడ్‌ను తక్కువ మార్పులతో మళ్ళీ ఉపయోగించవచ్చు. ప్రారంభించడానికి [Foundry Local డాక్యుమెంటేషన్](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) చూడండి, లేదా `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) తో ఇన్స్టాల్ చేసుకోండి.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma లాంటి ఓపెన్ మోడళ్ళను లోకల్‌గా నడిపించడానికి ప్రాచుర్యం పొందిన ప్రత్యామ్నాయం.


రెండు ఎంపికలను ఉపయోగించి ప్రాక్టికల్ ఉదాహరణలకు [పాఠం 19: SLMsతో నిర్మించడం](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ని చూడండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->