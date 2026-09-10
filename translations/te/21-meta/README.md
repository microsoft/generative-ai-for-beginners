# మెటా ఫ్యామిలీ మోడల్స్ తో నిర్మాణం 

## పరిచయం 

ఈ పాఠం కవర్ చేస్తుంది: 

- రెండు ప్రధాన మెటా ఫ్యామిలీ మోడల్స్ - ల్లామా 3.1 మరియు ల్లామా 3.2 ని అన్వేష్‌ణ చేయడం 
- ప్రతి మోడల్ కోసం వినియోగ కేసులు మరియు సందర్భాలను అర్థం చేసుకోవడం 
- ప్రతి మోడల్ యొక్క ప్రత్యేక లక్షణాలను చూపించడానికి కోడ్ ఉదాహరణ 


## మెటా ఫ్యామిలీ ఆఫ్ మోడల్స్ 

ఈ పాఠంలో, మేము మెటా ఫ్యామిలీ లేదా "ల్లామా హెర్డ్" నుంచి 2 మోడల్స్ ని అన్వేష్‌ణ చేస్తాం - ల్లామా 3.1 మరియు ల్లామా 3.2.

ఈ మోడల్స్ వివిధ రకాల్లో ఉంటాయి మరియు [మైక్రోసాఫ్ట్ ఫౌండ్రీ మోడల్స్ క్యాటలాగ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) లో లభ్యమవుతాయి.

> **గమనిక:** GitHub Models జూలై 2026 చివరికి రిటైర్ అవుతుంది. AI మోడల్స్ తో ప్రోటోటైపింగ్ కోసం [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ఉపయోగించడానికి మరిన్ని వివరాలు చూడండి.

మోడల్ రకాలు: 
- ల్లామా 3.1 - 70B ఇన్‌స్ట్రక్ట్ 
- ల్లామా 3.1 - 405B ఇన్‌స్ట్రక్ట్ 
- ల్లామా 3.2 - 11B విజన్ ఇన్‌స్ట్రక్ట్ 
- ల్లామా 3.2 - 90B విజన్ ఇన్‌స్ట్రక్ట్ 

*గమనిక: ల్లామా 3 కూడా Microsoft Foundry Models లో అందుబాటులో ఉంది కానీ ఈ పాఠంలో ఇందులో చర్చించబడదు*

## ల్లామా 3.1 

405 బిలియన్ పరిమాణాలతో, ల్లామా 3.1 ఓపెన్ సోర్స్ LLM వర్గంలోకి వస్తుంది. 

ఈ మోడల్ ముందునిన్ని విడుదల అయిన ల్లామా 3 కంటే అప్‌గ్రేడ్ అయింది: 

- పెద్ద కాంటెక్స్ట్ విండో - 128k టోకెన్లు vs 8k టోకెన్లు 
- పెద్ద గరిష్ట అవుట్పుట్ టోకెన్లు - 4096 vs 2048 
- మెరుగైన బహుభాషా మద్దతు - ట్రైనింగ్ టోకెన్లలో పెరుగుదల వల్ల 

ఇవి ల్లామా 3.1కు జెన్‌ఎఐ యాప్‌లు నిర్మించడం లో మరింత క్లిష్టమైన వినియోగ కేసులను నిర్వహించడంలో సహాయపడతాయి: 
- స్థానిక ఫంక్షన్ కాలింగ్ - LLM వర్క్‌ఫ్లో బయట ఉన్న బయటి టూల్స్ మరియు ఫంక్షన్లను పిలవగల సామర్థ్యం 
- మెరుగైన RAG పనితీరు - పెరిగిన కాంటెక్స్ట్ విండో వల్ల 
- సింథటిక్ డేటా ఉత్పత్తి - ఫైన్-ట్యూనింగ్ వంటి టాస్కులకు సమర్ధవంతమైన డేటాను సృష్టించగల సామర్థ్యం 

### స్థానిక ఫంక్షన్ కాలింగ్ 

ల్లామా 3.1 ఫంక్షన్ లేదా టూల్ కాల్స్ చేయడంలో మరింత సమర్థవంతంగా ఉండేలా ఫైన్-ట్యూన్ చేయబడింది. ఇది రెండు బిల్ట్-ఇన్ టూల్స్ కలిగి ఉంది, మోడల్ వాటిని వినియోగదారు ప్రాంప్ట్ ప్రకారం ఉపయోగించవలసినవి అని గుర్తించగలదు. ఆ టూల్స్: 

- **బ్రేవ్ సెర్చ్** - వెబ్ సెర్చ్ ద్వారా తాజా సమాచారం (వాతావరణం వంటి) పొందడానికి ఉపయోగించవచ్చు 
- **వోల్ఫ్రాం ఆల్ఫా** - మరింత క్లిష్టమైన గణిత గణనలకు ఉపయోగించవచ్చు, మీ స్వంత ఫంక్షన్లు రాయాల్సిన అవసరం లేదు. 

మీరు మీ సొంత కస్టమ్ టూల్స్ కూడా సృష్టించవచ్చు, ఆ టూల్స్ LLM పిలవగలవు. 

క్రింది కోడ్ ఉదాహరణలో: 

- సిస్టమ్ ప్రాంప్ట్ లో అందుబాటులో ఉన్న టూల్స్ (brave_search, wolfram_alpha) నిర్వచించడం 
- నివేదిక మధ్య ఒక నగర వాతావరణం గురించి అడిగే యూజర్ ప్రాంప్ట్ పంపడం 
- LLM బ్రేవ్ సెర్చ్ టూల్ కు టూల్ కాల్ తో స్పందిస్తుంది, ఇది ఇలా కనిపిస్తుంది `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*గమనిక: ఈ ఉదాహరణ కేవలం టూల్ కాల్ మాత్రమే చేస్తుంది, మీరు ఫలితాలు పొందాలనుకుంటే, బ్రేవ్ API పేజీపై ఉచిత ఖాతా సృష్టించి ఫంక్షన్ ను నిర్వచించాలి.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# మీ Microsoft Foundry ప్రాజెక్ట్ యొక్క "సమీక్ష" పేజీ నుండి ఇవి పొందండి
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

ఒక LLM అయినప్పటికీ, ల్లామా 3.1 లో ఒక పరిమితి ఉంది - దీని బహుమాధ్యమతా రహితం. అంటే, చిత్రాలను ప్రాంప్టుగా ఉపయోగించి ప్రతిస్పందనలు ఇవ్వలేమని. ఈ సామర్థ్యం ల్లామా 3.2 ప్రధాన లక్షణాల్లో ఒకటి. ఈ లక్షణాలు కూడా ఉన్నాయి: 

- బహుమాధ్యమత - టెక్స్ట్ మరియు చిత్ర ప్రాంప్ట్‌లను రెండింటినీ అంచనా వేయగల సామర్థ్యం 
- చిన్న నుండి మధ్యరాత్రి పరిమాణం తేడాలు (11B మరియు 90B) - ఇది ఫ్లెక్సిబల్ డిప్లాయ్‌మెంట్ ఎంపికలు అందిస్తుంది, 
- టెక్స్ట్- మాత్రమే వేరియెంట్లు (1B మరియు 3B) - ఇది మోడల్ ను ఎడ్జ్ / మొబైల్ పరికరాలలో అమలు చేయడానికి మరియు తక్కువ ఆలస్యం కోసం అనుమతిస్తుంది 

బహుమాధ్యమ మద్దతు ఓపెన్ సోర్స్ మోడల్స్ లో ఒక పెద్ద అభివృద్ధి సూచిస్తుంది. క్రింది కోడ్ ఉదాహరణ చిత్రం మరియు టెక్స్ట్ ప్రాంప్ట్ రెండింటినీ తీసుకొని ల్లామా 3.2 90B నుండి ఆ చిత్రంపై విశ్లేషణ పొందుతుంది. 


### ల్లామా 3.2 తో బహుమాధ్యమ మద్దతు

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

# Microsoft Foundry ప్రాజెక్ట్ యొక్క "సామగ్రి" పేజీ నుండి ఇవి పొందండి
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

## నేర్చుకోవడం ఇక్కడ ఆగదు, ప్రయాణాన్ని కొనసాగించండి

ఈ పాఠం పూర్తి చేసిన తరువాత, మా [జెనరేటివ్ AI లెర్నింగ్ కలెక్షన్](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) చూడండి మరియు మీ జెనరేటివ్ AI జ్ఞానాన్ని మరింత మెరుగుపర్చండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->