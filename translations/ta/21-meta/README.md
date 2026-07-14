# மெட்டா குடும்ப மாதிரிகளுடன் கட்டமைத்தல் 

## அறிமுகம் 

இந்த பாடத்தில் கையாளப்படும் பொருட்கள்: 

- இரண்டு முக்கிய மெட்டா குடும்ப மாதிரிகள் - லாமா 3.1 மற்றும் லாமா 3.2-ஐ ஆராய்தல் 
- ஒவ்வொரு மாதிரிக்கு இருக்கும் பயன்படுத்தும் சூழ்நிலைகளையும் சாத்தியமான प्रस்ர்திகளையும் புரியத்தல் 
- ஒவ்வொரு மாதிரியின் தனித்துவமான அம்சங்களை காட்டும் குறியீட்டு எடுத்துக்காட்டு  


## மெட்டா குடும்ப மாதிரிகள் 

இந்த பாடத்தில், மெட்டா குடும்பத்தில் அல்லது "லாமா கூட்டம்" எனப்படும் 2 மாதிரிகள் - லாமா 3.1 மற்றும் லாமா 3.2 ஆகியவற்றை ஆராயப்போகிறோம்.

இவை பல்வேறு வகைகளில் கிடைக்கின்றன மற்றும் [Microsoft Foundry Models பொருள் பட்டியலில்](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) உள்ளன.

> **குறிப்பு:** GitHub மொடல்ஸ் 2026 ஜூலை இறுதியில் நிறுத்தப்பெறும். AI மாதிரிகளுடன் உருவாக்க Microsoft Foundry Models-ஐ பயன்படுத்துவது பற்றி மேலும் விவரங்களை [இங்கே](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) பார்க்கலாம்.

மாதிரி வகைப்பாடு: 
- லாமா 3.1 - 70 பி இன்ஸ்ட்ரக்ட் 
- லாமா 3.1 - 405 பி இன்ஸ்ட்ரக்ட் 
- லாமா 3.2 - 11 பி விசென் இன்ஸ்ட்ரக்ட் 
- லாமா 3.2 - 90 பி விசென் இன்ஸ்ட்ரக்ட் 

*குறிப்பு: லாமா 3 Microsoft Foundry Models-ல் கிடைக்கிறது ஆனால் இந்த பாடத்தில் விளக்கப்பட மாட்டாது*

## லாமா 3.1 

405 பில்லியன் பராமிடர்களுடன் லாமா 3.1 திறந்த மூல LLM வகைக்கு உட்பட்டது. 

இந்த மாதிரி முன்னைய வெளியீடு லாமா 3-ஐ மேம்படுத்துவதற்காக வழங்கப்படுகிறது: 

- பெரிய உள்ளடக்க சாளரம் - 128k டோக்கன்கள் مقابل 8k டோக்கன்கள் 
- அதிகமான அதிகபட்ச வெளியீடு டோக்கன்கள் - 4096 مقابل 2048 
- சிறந்த பன்மொழி ஆதரவு - பயிற்சி டோக்கன்களில் அதிகரிப்பு காரணமாக 

இவை லாமா 3.1-க்கு உருவாக்கியா்ந்துள்ள GenAI பயன்பாடுகளில் அதிக சிக்கலான பயன்பாடுகளை கையாள அனுமதிக்கின்றன: 
- இயல்புநிலை செயல்பாட்டு அழைப்புகள் - LLM பணிச்சூழல் அப்புறம் வெளிப்புற கருவிகள் மற்றும் செயல்பாடுகளை அழைக்கும் திறன்
- சிறந்த RAG செயல்திறன் - அதிக உள்ளடக்க சாளரம் காரணமாக 
- மோசமான தரவு உருவாக்கம் - சிறந்த தரவுத்திறன் பெற்றுக்கொள்ள செயல்களை எளிதாக்குதல் 

### இயல்புநிலை செயல்பாட்டு அழைப்புகள் 

லாமா 3.1 செயல்பாடுகள் அல்லது கருவி அழைப்புகளில் சிறந்த முக்கியத்துவம் பெறும் வகையில் நுணுக்கமாக பயிற்சி பெற்றுள்ளது. அதிலும், மாதிரிக்கு இரண்டு தனிப்பட்ட கருவிகள் உள்ளன, அவை பயனரின் கேள்வித் தூண்டுதலின் அடிப்படையில் பயன்படுத்தப்பட வேண்டும் என மாதிரி அறிந்துகொள்ள முடியும். அந்த கருவிகள்: 

- **Brave Search** - வலை தேடல் மூலம் புதுப்பிக்கப்பட்ட தகவல்களைப் பெற உதவும், உதாரணமாக வானிலை 
- **Wolfram Alpha** - அதிகமான கணிதக்கூறுகளை செய்ய பயன்படும் ஆகவே தனித்துவமான செயல்பாடுகளை எழுத தேவையில்லை. 

நீங்கள் உங்கள் சொந்த தனிப்பயன் கருவிகளையும் உருவாக்கி மாதிரி அழைக்கச் செய்யலாம். 

கீழே உள்ள குறியீட்டு உதாரணத்தில்: 

- கிடைக்கக்கூடிய கருவிகள் (brave_search, wolfram_alpha) பயன்படுத்தப்படுகிறன என அமைப்பு தூண்டுதலில் குறிப்பிடுகிறோம். 
- ஒரு பயனர் கேள்வியை அனுப்புகிறோம், அது ஒரு குறிப்பிட்ட நகரத்தில் வானிலை பற்றி கேட்கிறது. 
- LLM Brave Search கருவி அழைப்பை வழங்கும், இது இவ்வாறு இருக்கும் `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*குறிப்பு: இந்த எடுத்துக்காட்டு கருவி அழைப்பையே செய்கிறது, முடிவுகளை பெறவிருந்தால் Brave API பக்கத்தில் இலவச கணக்கை உருவாக்கி செயல்பாட்டை தீர்மானிக்க வேண்டும்.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# உங்கள் Microsoft Foundry திட்டத்தின் "மேலோட்டம்" பக்கத்திலிருந்து இதeket பெறுக
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

## லாமா 3.2 

LLM ஆனாலும், லாமா 3.1-இன் ஒரு குறைவு அதன் பன்முறை காட்சி திறன் இல்லாததாகும். அதாவது, படங்கள் போன்ற வெவ்வேறு வகையான உள்ளீடுகளை பேராசையாகப் பயன்படுத்த முடியாமலும் பதிலளிக்க முடியாமலும் இருப்பது. இந்த திறன் லாமா 3.2 இன் முக்கிய அம்சங்களில் ஒன்று ஆகும். இவற்றுடன் கீழ்க்கண்ட அம்சங்களும் உள்ளன: 

- பன்முறை காட்சி - உரை மற்றும் பட தூண்டுதல்களை இரண்டு வகையும் மதிப்பாய்வு செய்யும் திறன் 
- சிறிய முதல் நடுத்தர அளவிலான வகைகள் (11B மற்றும் 90B) - இது தளவமைப்புகளை நெகிழ்வான முறையில் பயன்படுத்த உதவும், 
- உரைத்தாழ்த்தல் வகைகள் (1B மற்றும் 3B) - இது மாதிரியை எல்லையோர / மொபைல் சாதனங்களில் பயன்படுத்த வைக்கும் மற்றும் குறைந்த தாமதம் வழங்கும் 

பன்முறை ஆதரவு திறன் திறந்த மூல மாதிரிகளின் உலகத்தில் மிகப்பெரிய முன்னேற்றமாகும். கீழ்க்காணும் குறியீட்டு எடுத்துக்காட்டில் ஒரே நேரத்தில் ஒரு படம் மற்றும் உரை தூண்டுதலைப் பயன்படுத்தி, லாமா 3.2 90B-இல் இருந்து படத்தின் ஆய்வைக் பெறுகிறது. 


### லாமா 3.2 உடன் பன்முறை ஆதரவு

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

# உங்கள் Microsoft Foundry திட்டத்தின் "அवलோకனம்" பக்கத்திலிருந்து இதைப் பெற்றுக்கொள்ளவும்
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

## கற்றல் இங்கு நிற்காது, பயணத்தை தொடருங்கள்

இந்த பாடம் முடிந்தவுடன், எங்கள் [உருவாக்கும் AI கற்றல் தொகுப்பை](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) பாருங்கள் உங்கள் உருவாக்கும் AI அறிவை மேம்படுத்த!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->