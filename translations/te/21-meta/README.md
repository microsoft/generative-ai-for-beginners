# మెటా ఫ్యామిలీ మోడల్స్‌తో నిర్మించడం

## పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:

- రెండు ప్రధాన మెటా ఫ్యామిలీ మోడల్స్‌ను అన్వేషించడం - ల్లామా 3.1 మరియు ల్లామా 3.2
- ప్రతి మోడల్ కోసం వాడుకకేసులు మరియు సందర్భాలను అర్థం చేసుకోవడం
- ప్రతి మోడల్ యొక్క ప్రత్యేక లక్షణాలను చూపించే కోడ్ ఉదాహరణ


## మెటా ఫ్యామిలీ ఆఫ్ మోడల్స్

ఈ పాఠంలో, మేము మెటా ఫ్యామిలీ లేదా "ల్లామా హర్డ్" నుండి 2 మోడల్స్‌ను అన్వేషించబోతున్నాము - ల్లామా 3.1 మరియు ల్లామా 3.2.

ఈ మోడల్స్ వివిధ వేరియంట్లలో అందుబాటులో ఉన్నాయి మరియు [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) లో లభ్యమవుతాయి.

> **గమనిక:** GitHub Models జూలై 2026 చివరలో రిటైర్ అవుతోంది. [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ఉపయోగించి AI మోడల్స్‌తో ప్రోటోటైప్ చేయడంపై మరిన్ని వివరాలు ఇవి.

మోడల్ వేరియంట్స్:
- ల్లామా 3.1 - 70B ఇన్‌స్ట్రక్ట్
- ల్లామా 3.1 - 405B ఇన్‌స్ట్రక్ట్
- ల్లామా 3.2 - 11B విజన్ ఇన్‌స్ట్రక్ట్
- ల్లామా 3.2 - 90B విజన్ ఇన్‌స్ట్రక్ట్

*గమనిక: ల్లామా 3 కూడా Microsoft Foundry Models లో అందుబాటులో ఉంది కానీ ఈ పాఠంలో చర్చించబడదని దయచేసి గమనించండి*

## ల్లామా 3.1

405 బిలియన్ ప్యారామీటర్స్‌తో, ల్లామా 3.1 ఓపెన్ సోర్స్ LLM వర్గంలోకి వస్తుంది.

ఈ మోడల్ ముందు విడుదలైన ల్లామా 3 కంటే మెరుగైనందున:

- పెద్ద కాంటెక్స్ట్ విండో - 128k టోకెన్స్ 8k టోకెన్స్ జతగా
- ఎక్కువ గరిష్ట అవుట్పుట్ టోకెన్స్ - 4096 vs 2048
- మెరుగైన బహుభాషా మద్దతు - శిక్షణ టోకెన్స్ పెరుగుదల కారణంగా

ఇవి ల్లామా 3.1 కి కాంప్లెక్స్ వినియోగ కేసులను నిర్వహించడంలో సహాయపడతాయి, జెన్‌ఎఐ అప్లికేషన్స్ నిర్మాణంలో:
- స్థానిక ఫంక్షన్ కాలింగ్ - LLM వర్క్‌ఫ్లోకి వెలుపల ఉన్న బయటి టూల్స్, ఫంక్షన్లు పిలవగల సామర్థ్యం
- మెరుగైన RAG పనితీరు - పెద్ద కాంటెక్స్ట్ విండో కారణంగా
- సింథటిక్ డేటా జనరేషన్ - ఫైన్-ట్యూనింగ్ వంటి టాస్కులకు సమర్థవంతమైన డేటాను సృష్టించే సామర్థ్యం

### స్థానిక ఫంక్షన్ కాలింగ్

ల్లామా 3.1 ని ఫంక్షన్ లేదా టూల్ కాల్స్ చేయడంలో మరింత సమర్థవంతంగా తీర్చిదిద్దారు. దీనికి రెండు లోపల ఉన్న టూల్స్ ఉన్నాయ్, వాటిని మోడల్ యూజర్ తోటి ప్రాంప్ట్ ఆధారంగా ఉపయోగించాల్సిన అవసరం ఉన్నదిగా గుర్తించగలదు. ఈ టూల్స్:

- **బ్రేవ్ సెర్చ్** - వెబ్ సెర్చ్ చేయడం ద్వారా తాజా సమాచారాన్ని (ఉదాహరణకు వాతావరణం) పొందగలదు
- **వోల్ఫ్రాం అల్ఫా** - క్లిష్ట గణిత లెక్కింపులకు ఉపయోగించవచ్చు, మీ స్వంత ఫంక్షన్లు రాయడం అవసరం లేదు

మీరు కూడా LLM పిలవగలిగే మీ స్వంత కస్టమ్ టూల్స్ సృష్టించవచ్చు.

క్రింది కోడ్ ఉదాహరణలో:

- ఉపయోగించే టూల్స్ (brave_search, wolfram_alpha) న систему ప్రాంప్ట్ లో నిర్వచించాము.
- ఒక యూజర్ ప్రాంప్ట్ పంపించాము, అది ఒక నగరంలో వాతావరణం గురించి అడుగుతుంది.
- LLM బ్రేవ్ సెర్చ్ టూల్‌కు టూల్ కాల్ ద్వారా స్పందిస్తుంది, ఇది ఇలా ఉంటుంది `<|python_tag|>brave_search.call(query="Stockholm weather")`

*గమనిక: ఈ ఉదాహరణ కేవలం టూల్ కాల్ మాత్రమే చేస్తుంది, ఫలితాలను పొందాలనుకుంటే, మీరు బ్రేవ్ API పేజీలో ఫ్రీ ఖాతా సృష్టించి ఫంక్షన్‌ను నిర్వచించాల్సి ఉంటుంది.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# మీ Microsoft Foundry ప్రాజెక్ట్ యొక్క "సారాంశం" పేజీ నుండి ఇవి పొందండి
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## ల్లామా 3.2

LLM అయినప్పటికీ, ల్లామా 3.1 యొక్క ఒక పరిమితి దీని మల్టీమోడాలిటీ లేకపోవడం అంటే, బహుళ రకాల ఇన్‌పుట్లను (ఉదాహరణకు చిత్రాల) ప్రాంప్ట్‌లుగా ఉపయోగించి ప్రతిస్పందన ఇవ్వలేని సామర్థ్యం. ఈ సామర్థ్యం ల్లామా 3.2 యొక్క ముఖ్య లక్షణాలలో ఒకటి. మరిన్ని లక్షణాలు:

- మల్టీమోడాలిటీ - టెక్స్ట్ మరియు చిత్ర ప్రాంప్ట్‌లు రెండింటినీ మూల్యాంకనం చేయగలదు
- చిన్న నుండి మధ్యవరకు పరిమాణ వేరియంట్లు (11B మరియు 90B) - అనువైన డిప్లాయ్‌మెంట్ ఎంపికలు అందజేస్తుంది,
- కేవలం టెక్స్ట్ వేరియంట్లు (1B మరియు 3B) - ఈ మోడల్‌ను ఎడ్జ్ / మొబైల్ పరికరాలపై డిప్లాయ్ చేయడానికి అనుమతించి తక్కువ లేటెన్సీ అందిస్తుంది

మల్టీమోడల్ మద్దతు ఓపెన్ సోర్స్ మోడల్స్ ప్రపంచంలో పెద్ద అడుగు. క్రింది కోడ్ ఉదాహరణ చిత్రం మరియు టెక్స్ట్ ప్రాంప్ట్‌లను తీసుకుని ల్లామా 3.2 90B నుండి చిత్ర విశ్లేషణ పొందుతుంది.


### ల్లామా 3.2 తో మల్టీమోడల్ మద్దతు

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# మీ Microsoft Foundry ప్రాజెక్ట్ యొక్క "సమీక్ష" పేజీ నుండి ఇవి తీసుకోండి
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## నేర్చుకోవడం ఇక్కడ ఆగదు, ప్రయాణం కొనసాగించండి

ఈ పాఠం పూర్తయిన తరువాత, మా [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ని పరిశీలించి, మీ జనరేటివ్ AI జ్ఞానాన్ని వద్దనుకుంటూ కొనసాగండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->