# మెటా ఫ్యామిలీ మోడల్స్‌తో నిర్మాణం

## పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:

- రెండు ప్రధాన మెటా ఫ్యామిలీ మోడల్స్ - ల్లామా 3.1 మరియు ల్లామా 3.2 ని అన్వేషించడం
- ప్రతి మోడల్ కోసం ఉపయోగాల మరియు పరిస్థితులను అర్థం చేసుకోవడం
- ప్రతి మోడల్ యొక్క ప్రత్యేక లక్షణాలను చూపించే కోడ్ నమూనా

## మెటా ఫ్యామిలీ మోడల్స్

ఈ పాఠంలో, మేము మెటా ఫ్యామిలీ లేదా "ల్లామా హర్డ్" నుండి 2 మోడల్స్ - ల్లామా 3.1 మరియు ల్లామా 3.2 ని అన్వేషిస్తాము

ఈ మోడల్స్ వివిధ వేరియంట్లలో వస్తాయి మరియు GitHub మోడల్ మార్కెట్‌ప్లేస్‌లో అందుబాటులో ఉన్నాయి. GitHub మోడల్స్ ఉపయోగించి [AI మోడల్స్‌తో ప్రోటోటైపింగ్](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) గురించి మరిన్ని వివరాలు ఇక్కడ ఉన్నాయి.

మోడల్ వేరియంట్లు:
- ల్లామా 3.1 - 70B ఇన్‌స్ట్రక్ట్
- ల్లామా 3.1 - 405B ఇన్‌స్ట్రక్ట్
- ల్లామా 3.2 - 11B విజన్ ఇన్‌స్ట్రక్ట్
- ల్లామా 3.2 - 90B విజన్ ఇన్‌స్ట్రక్ట్

*గమనిక: ల్లామా 3 కూడా GitHub మోడల్స్‌లో అందుబాటులో ఉంది కానీ ఈ పాఠంలో కవర్ చేయబడదు*

## ల్లామా 3.1

405 బిలియన్ పరామితులతో, ల్లామా 3.1 ఓపెన్ సోర్స్ LLM వర్గంలోకి వస్తుంది.

ఈ మోడల్ ముందటి విడుదల అయిన ల్లామా 3 కి అప్‌గ్రేడ్‌గా ఉంది:

- పెద్ద కాంటెక్స్ట్ విండో - 128k టోకెన్లు vs 8k టోకెన్లు
- పెద్ద గరిష్ట అవుట్‌పుట్ టోకెన్లు - 4096 vs 2048
- మెరుగైన బహుభాషా మద్దతు - శిక్షణ టోకెన్ల పెరుగుదల కారణంగా

ఇవి ల్లామా 3.1 కి జెన్‌ఎఐ అప్లికేషన్లు నిర్మించేటప్పుడు మరింత క్లిష్టమైన ఉపయోగాల నిర్వహణను సాధ్యమవుతాయి, వాటిలో:
- స్థానిక ఫంక్షన్ కాలింగ్ - LLM వర్క్‌ఫ్లో వెలుపల ఉన్న బాహ్య టూల్స్ మరియు ఫంక్షన్లను పిలవగల సామర్థ్యం
- మెరుగైన RAG పనితీరు - పెద్ద కాంటెక్స్ట్ విండో కారణంగా
- సింథటిక్ డేటా ఉత్పత్తి - ఫైన్-ట్యూనింగ్ వంటి పనుల కోసం సమర్థవంతమైన డేటాను సృష్టించే సామర్థ్యం

### స్థానిక ఫంక్షన్ కాలింగ్

ల్లామా 3.1 ఫంక్షన్ లేదా టూల్ కాల్స్ చేయడంలో మరింత సమర్థవంతంగా ఉండేందుకు ఫైన్-ట్యూన్ చేయబడింది. ఇది రెండు బిల్ట్-ఇన్ టూల్స్ కలిగి ఉంది, అవి యూజర్ ప్రాంప్ట్ ఆధారంగా ఉపయోగించాల్సిన అవసరం ఉన్నట్లు మోడల్ గుర్తించగలదు. ఈ టూల్స్:

- **బ్రేవ్ సెర్చ్** - వెబ్ సెర్చ్ ద్వారా వాతావరణం వంటి తాజా సమాచారాన్ని పొందడానికి ఉపయోగించవచ్చు
- **వోల్ఫ్రామ్ ఆల్ఫా** - మరింత క్లిష్టమైన గణిత లెక్కింపులకు ఉపయోగించవచ్చు, కాబట్టి మీ స్వంత ఫంక్షన్లు రాయాల్సిన అవసరం లేదు

మీరు కూడా మీ స్వంత కస్టమ్ టూల్స్ సృష్టించవచ్చు, వాటిని LLM పిలవగలదు.

క్రింది కోడ్ ఉదాహరణలో:

- మేము సిస్టమ్ ప్రాంప్ట్‌లో అందుబాటులో ఉన్న టూల్స్ (brave_search, wolfram_alpha) ని నిర్వచిస్తాము.
- ఒక యూజర్ ప్రాంప్ట్ పంపిస్తాము, అది ఒక నగరంలో వాతావరణం గురించి అడుగుతుంది.
- LLM బ్రేవ్ సెర్చ్ టూల్‌కు టూల్ కాల్‌తో స్పందిస్తుంది, ఇది ఇలా కనిపిస్తుంది `<|python_tag|>brave_search.call(query="Stockholm weather")`

*గమనిక: ఈ ఉదాహరణ కేవలం టూల్ కాల్ చేస్తుంది, మీరు ఫలితాలు పొందాలనుకుంటే, బ్రేవ్ API పేజీలో ఉచిత ఖాతాను సృష్టించి ఫంక్షన్‌ను నిర్వచించాలి*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

LLM అయినప్పటికీ, ల్లామా 3.1 కి ఒక పరిమితి ఉంది, అది మల్టిమోడాలిటీ. అంటే, ఇమేజ్‌లను ప్రాంప్ట్‌లుగా ఉపయోగించి స్పందనలు ఇవ్వగల సామర్థ్యం. ఈ సామర్థ్యం ల్లామా 3.2 యొక్క ప్రధాన లక్షణాలలో ఒకటి. ఈ లక్షణాలు కూడా ఉన్నాయి:

- మల్టిమోడాలిటీ - టెక్స్ట్ మరియు ఇమేజ్ ప్రాంప్ట్‌లను రెండింటినీ అంచనా వేయగల సామర్థ్యం
- చిన్న నుండి మధ్యస్థ పరిమాణ వేరియంట్లు (11B మరియు 90B) - ఇది అనువైన డిప్లాయ్‌మెంట్ ఎంపికలను అందిస్తుంది
- టెక్స్ట్-ఓన్లీ వేరియంట్లు (1B మరియు 3B) - ఇది మోడల్‌ను ఎడ్జ్ / మొబైల్ పరికరాలపై డిప్లాయ్ చేయడానికి మరియు తక్కువ లేటెన్సీని అందిస్తుంది

మల్టిమోడల్ మద్దతు ఓపెన్ సోర్స్ మోడల్స్ ప్రపంచంలో పెద్ద అడుగు. క్రింది కోడ్ ఉదాహరణ ఇమేజ్ మరియు టెక్స్ట్ ప్రాంప్ట్ రెండింటినీ తీసుకుని ల్లామా 3.2 90B నుండి ఇమేజ్ విశ్లేషణ పొందుతుంది.

### ల్లామా 3.2 తో మల్టిమోడల్ మద్దతు

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

ఈ పాఠం పూర్తి చేసిన తర్వాత, మా [జెనరేటివ్ AI లెర్నింగ్ కలెక్షన్](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ను చూడండి, మీ జెనరేటివ్ AI జ్ఞానాన్ని మరింత పెంచుకోండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->