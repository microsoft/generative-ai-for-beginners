# మెటా కుటుంబ నమూనాలతో నిర్మాణం

## పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:

- రెండు ప్రధాన మెటా కుటుంబ నమూనాలను అన్వేషించడం - ల్లామా 3.1 మరియు ల్లామా 3.2
- ప్రతి నమూనా కోసం ఉపయోగకరమైన సందర్భాలు మరియు పరిస్థితులను అర్థం చేసుకోవడం
- ప్రతి నమూనా యొక్క ప్రత్యేక ఫీచర్లను చూపించే కోడ్ నమూనా

## మెటా కుటుంబ నమూనాలు

ఈ పాఠంలో, మనం మెటా కుటుంబం లేదా "లామా హర్డ్" నుండి 2 నమూనాలను అన్వేషిస్తాము - ల్లామా 3.1 మరియు ల్లామా 3.2.

ఈ నమూనాలు వేరియంట్లలో అందుబాటులో ఉన్నాయి మరియు GitHub మోడల్ మార్కెట్‌ప్లేస్‌లో పొందుపర్చబడ్డాయి. GitHub మోడల్స్ ఉపయోగించి [AI మోడల్స్‌తో ప్రోటోటైపింగ్](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) పై మరింత వివరాలు ఇక్కడ ఉన్నాయి.

మోడల్ వేరియంట్లు:
- ల్లామా 3.1 - 70B ఇన్‌స్ట్రక్ట్
- ల్లామా 3.1 - 405B ఇన్‌స్ట్రక్ట్
- ల్లామా 3.2 - 11B విజన్ ఇన్‌స్ట్రక్ట్
- ల్లామా 3.2 - 90B విజన్ ఇన్‌స్ట్రక్ట్

*గమనిక: ల్లామా 3 కూడా GitHub మోడల్స్‌లో అందుబాటులో ఉంది కానీ ఈ పాఠంలో కవర్ చేయబడదు*

## ల్లామా 3.1

405 బిలియన్ పారా మీటర్లతో, ల్లామా 3.1 ఓపెన్ సోర్స్ LLM కేటగిరీ లో సరిపోతుంది.

ఈ మోడల్ పూర్వ విడుదల అయిన ల్లామా 3కు ఒక అప్‌గ్రేడ్ గా అందుబాటులో ఉంది:

- పెద్ద కాంటెక్ట్ విండో - 128k టోకెన్లు vs 8k టోకెన్లు
- పెద్ద గరిష్ట అవుట్‌పుట్ టోకెన్లు - 4096 vs 2048
- మెరుగైన బహుభాషా మద్దతు - శిక్షణ టోకెన్ల పెరుగుదల కారణంగా

ఇవి ల్లామా 3.1 కు మరింత క్లిష్టమైన ఉపయోగ పరిస్థితులను నిర్వహించడానికి అనుమతిస్తాయి, GenAI అప్లికేషన్లను రూపొందించే సమయంలో:

- నేటివ్ ఫంక్షన్ కాలింగ్ - LLM ప్రవర్తనా ప్రదేశం నుండి బయట ఎక్స్‌టెర్నల్ టూల్స్ మరియు ఫంక్షన్లను పిలవగల సామర్ధ్యం
- మెరుగైన RAG పనితీరు - ఎక్కువ కాంటెక్ట్ విండో కారణంగా
- సింథటిక్ డేటా సృష్టి - ఫైన్-ట్యూనింగ్ వంటి పని కోసం ప్రభావవంతమైన డేటాను సృష్టించే సామర్థ్యం

### నేటివ్ ఫంక్షన్ కాలింగ్

ల్లామా 3.1 ఫంక్షన్ లేదా టూల్ కాల్స్ చేయడంలో మరింత సమర్థవంతంగా ఉండేలా ఫైన్ ట్యూన్ చేయబడింది. ఇది రెండు బిల్ట్-ఇన్ టూల్స్ కలిగి ఉంది, యూజర్ యొక్క ప్రాంప్ట్ ఆధారంగా మోడల్ వాటిని ఉపయోగించాల్సిన అవసరం ఉన్నట్లు గుర్తించగలదు. ఈ టూల్స్:

- **బ్రేవ్ సెర్చ్** - వెబ్ సెర్చ్ చేసి తాజా సమాచారం (ఉదా: వాతావరణం) పొందడానికి ఉపయోగపడుతుంది
- **వోల్ఫ్రామ్ ఆల్ఫా** - మరింత క్లిష్ట గణిత లెక్కింపులు చేయడానికి ఉపయోగపడుతుంది, మీ స్వంత ఫంక్షన్లు రాయవసరం లేదు

మీరు కూడా మీ స్వంత కస్టమ్ టూల్స్ సృష్టించవచ్చు, అవి LLM పిలవగలవు.

కింద ఉన్న కోడ్ ఉదాహరణలో:

- మేము సిస్టమ్ ప్రాంప్ట్‌లో అందుబాటులో ఉన్న టూల్స్ (brave_search, wolfram_alpha) ను నిర్వచిస్తాము.
- ఒక యూజర్ ప్రాంప్ట్ పంపుతాము, ఇది ఒక నిర్దిష్ట నగరంలో వాతావరణం గురించిన ప్రశ్న అడుగుతుంది.
- LLM బ్రేవ్ సెర్చ్ టూల్‌ను పిలిచేలా స్పందిస్తుంది, ఇది ఇలా ఉంటుంది `<|python_tag|>brave_search.call(query="Stockholm weather")`

*గమనిక: ఈ ఉదాహరణ కేవలం టూల్ కాల్ మాత్రమే చేస్తుంది, మీరు ఫలితాలు పొందాలనుకుంటే, Brave API పేజీపై ఉచిత ఖాతాను సృష్టించుకుని, ఫంక్షన్‌ను నిర్వచించాలి.*

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

ఒక LLM అయినప్పటికీ, ల్లామా 3.1 లో ఒక పరిమితి ఉంది - బహుమాధుర్యత లేకపోవడం. అంటే, ఇమేజిలాంటి వేరే రకాల ఇన్పుట్‌లను ప్రాంప్ట్‌లుగా ఉపయోగించి స్పందనలు ఇవ్వడం కాని. ఈ సామర్థ్యం ల్లామా 3.2 యొక్క ముఖ్య ఫీచర్లలో ఒకటి. ఆ ఫీచర్లు కూడా:

- బహుమాధుర్యత - టెక్స్ట్ మరియు ఇమేజ్ ప్రాంప్ట్‌లను రెండింటినీ విశ్లేషించగల సామర్థ్యం
- చిన్న మరియు మధ్యస్థల పరిమాణ వేరియంట్లు (11B మరియు 90B) - ఇది అనుకూలమైన డిప్లాయ్‌మెంట్ ఎంపికలని అందిస్తుంది
- కేవలం టెక్స్ట్ వేరియంట్లు (1B మరియు 3B) - ఇది మోడల్ను ఎడ్జ్/మొబైల్ డివైసెస్‌పై డిప్లాయ్ చేయడానికి మరియు తక్కువ లేటెన్సీని అందించడానికి అనుమతిస్తుంది

బహుమాధుర్యత మద్దతు ఓపెన్ సోర్స్ మోడల్స్ ప్రపంచంలో ఒక పెద్ద అడుగు.

కింద ఉన్న కోడ్ ఉదాహరణలో ఇమేజ్ మరియు టెక్స్ట్ ప్రాంప్ట్‌లను రెండింటినీ తీసుకొని ల్లామా 3.2 90B నుండి ఇమేజ్ విశ్లేషణను పొందుతుంది.

### ల్లామా 3.2 తో బహుమాధుర్యత మద్దతు

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

## నేర్చుకుంటూ ప్రయాణం ఇక్కడ ఆగదు, జెర్నీని కొనసాగించండి

ఈ పాఠాన్ని పూర్తి చేసిన తర్వాత, మా [జెనరేటివ్ ఏఐ లెర్నింగ్ సేకరణ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ని సందర్శించి, మీ జెనరేటివ్ ఏఐ జ్ఞానాన్ని మరింత మెరుగుపర్చుకోండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**నిరాకరణ**:  
ఈ డాక్యూమెంట్ ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము సరిగా ఉండేందుకు ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు. అసలు డాక్యూమెంట్ దాని మాతృభాషలోనే అధికారపూర్వక మూలం అని పరిగణించాలి. ముఖ్యమైన సమాచారం కోసం ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫార్సు చేస్తాము. ఈ అనువాదం వాడకంలో ఇలాంటి అపార్థాలు లేదా తప్పుగా అర్థముచేసుకున్న పరిణామాలకు మేము బాధ్యులం కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->