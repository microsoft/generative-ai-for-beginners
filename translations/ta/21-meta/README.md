# மேட்டா குடும்ப மாதிரிகளுடன் கட்டமைத்தல்

## அறிமுகம்

இந்த பாடத்தில் இதுகள் கவரப்படும்:

- இரண்டு முக்கிய மேட்டா குடும்ப மாதிரிகள் - லாமா 3.1 மற்றும் லாமா 3.2 பரிசோதனை
- ஒவ்வொரு மாதிரிக்கும் பயன்பாடுகள் மற்றும் சூழல்களை புரிந்துகொள்ளுதல்
- ஒவ்வொரு மாதிரியின் தனித்துவ வாய்ப்புகளை காட்டும் குறியீட்டுக்கான உதாரணம்


## மேட்டா குடும்ப மாதிரிகள்

இந்த பாடத்தில், நாங்கள் மேட்டா குடும்பத்திலிருந்து அல்லது "லாமா குபாய்"யில் இருந்து 2 மாதிரிகளை ஆராய்வோம் - லாமா 3.1 மற்றும் லாமா 3.2.

இந்த மாதிரிகள் வெவ்வேறு வேரியண்ட்களில் வரும் மற்றும் [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) இல் கிடைக்கின்றன.

> **குறிப்பு:** GitHub Models 2026 ஜூலை இறுதியில் ஓய்வு பெறுகிறது. AI மாதிரிகளோடு ஆரம்பிக்க [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) பற்றி மேலும் விவரங்கள்.

மாதிரி வேரியண்டுகள்:
- லாமா 3.1 - 70B Instruct
- லாமா 3.1 - 405B Instruct
- லாமா 3.2 - 11B Vision Instruct
- லாமா 3.2 - 90B Vision Instruct

*குறிப்பு: லாமா 3 Microsoft Foundry மாதிரிகளில் கிடைக்கிறது ஆனால் இந்த பாடத்தில் நடைபெறாது*

## லாமா 3.1

405 பில்லியன் பண்புகளுடன், லாமா 3.1 திறந்த மூல LLM வகையை சேர்ந்தது.

இந்த மாதிரி முன்பு வெளியிடப்பட்ட லாமா 3 ஐ மேம்படுத்துகிறது:

- பெரிய சூழல் ஜன்னல் - 128k டோக்கன்கள் مقابل 8k டோக்கன்கள்
- அதிகபட்ச வெளியீட்டு டோக்கன்கள் - 4096 مقابل 2048
- மேம்பட்ட பன்மொழி ஆதரவு - பயிற்சி டோக்கன்களை அதிகரிப்பதால்

இவை லாமா 3.1-க்கு ஜென்ஏஇ செயலிகள் கட்டும் போது கூடுதல் சிக்கலான பயன்பாடுகளை கையாள உதவுகின்றன:
- இயல்பான செயல்பாட்டு அழைத்தல் - LLM பணி ஓட்டத்தில் வெளியக கருவிகளையும் செயல்பாடுகளையும் அழைக்க கூடிய திறன்
- மேம்பட்ட RAG செயல்திறன் - உயர் சூழல் ஜன்னலால்
- செயற்கை தரவு உருவாக்கம் - சிறந்த அழுத்தத்திற்கு பயனுள்ள தரவை உருவாக்க திறன்

### இயல்பான செயல்பாட்டு அழைத்தல்

லாமா 3.1 செயல்கள் அல்லது கருவிகளை அழைப்பதில் சிறந்த தாக்கம் மீது சிறப்படுத்தப்பட்டுள்ளது. இதனுடன் இரண்டு கட்டமைக்கப்பட்ட கருவிகள் இருக்கும், மாதிரி பயனரின் குறியீட்டு அடிப்படையில் அவற்றைப் பயன்படுத்த வேண்டியதாக அடையாளம் காண்கிறது. இந்த கருவிகள்:

- **Brave Search** - இணையத் தேடல் மூலம் காலநிலைக்கான தகவல் பெற பயன்படும்
- **Wolfram Alpha** - அதிக மருத்துவ கணக்கீடுகளுக்கு பயன்படும்; உங்களது சொந்த செயல்பாடுகளை எழுத தேவையில்லை.

நீங்கள் உங்கள் சொந்த தனிப்பயன் கருவிகளையும் உருவாக்கலாம், அவ்வாறு LLM அழைக்கலாம்.

கீழே உள்ள குறியீட்டு உதாரணத்தில்:

- கிடைக்கும் கருவிகள் (brave_search, wolfram_alpha) ஐ அமைப்பு குறியீட்டில் வரையறுக்கின்றோம்.
- ஒரு பயனர் கோரிக்கை அனுப்புதல், குறிப்பாக ஒரு நகரத்தில் காலநிலை பற்றி கேள்வி கேட்பது.
- LLM Brave Search கருவியை அழைக்கும், இது `<|python_tag|>brave_search.call(query="Stockholm weather")` போன்றதாக தோற்றமளிக்கும்.

*குறிப்பு: இந்த உதாரணம் கருவி அழைப்பை மட்டுமே செய்கிறது, முடிவுகளை பெற விரும்பினால், Brave API பக்கத்தில் இலவச கணக்கைத் திறக்கவும் மற்றும் செயல்பாட்டை வரையறுக்கவும்.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# உங்கள் Microsoft Foundry திட்டத்தின் "மேலோட்டம்" பக்கத்திலிருந்து இதை பெறுங்கள்
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

LLM ஆக இருந்தும், லாமா 3.1 ஓர் வரம்பு உள்ளது அது பன்முகத்தன்மை இல்லை என்பது. அதாவது, படங்களை போன்ற வித்தியாசமான உள்ளீடுகளைப் பயன்படுத்த முடியாது, மற்றும் பதில்களை அளிக்க முடியாது. இது லாமா 3.2 இன் பிரதான அம்சங்களில் ஒன்றாகும். இவை மேலும் உள்ளன:

- பன்முகத்தன்மை - உரையும் படங்களும் உள்ளீடாக மதிப்பீடு செய்யும் திறன்
- சிறிய முதல் நடுத்தர அளவுகளுக்கு மாறுபாடுகள் (11B மற்றும் 90B) - நெகிழ்வான அமைப்புக்கு வாய்ப்பு வழங்குகிறது,
- உரை மட்டும் மாறுபாடுகள் (1B மற்றும் 3B) - இதனால் மாதிரி முனை/மொபைல் சாதனங்களில் செயல்படுத்த முடியும் மற்றும் குறைந்த பின்னடைவு உள்ளது

பன்முகத்தன்மை ஆதரவு திறந்த மூல மாதிரிகளின் உலகில் ஒரு பெரிய முன்னேற்றமாகும். கீழே உள்ள குறியீட்டுக்கான உதாரணம் படமும் உரை கோரிக்கையும் எடுத்துக் கொண்டு லாமா 3.2 90B இல் இருந்து படத்தின் பகுப்பாய்வை பெறுகிறது.


### லாமா 3.2 உடன் பன்முக ஆதரவு

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

# உங்கள் Microsoft Foundry திட்டத்தின் "மேலோட்டம்" பக்கத்திலிருந்து இதை பெறுக
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

## கற்றல் இங்கே நிற்கவில்லை, பயணத்தை தொடரவும்

இந்த பாடத்தை முடித்த பிறகு, எங்கள் [திருத்துதல் AI கற்றல் தொகுப்பு](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ஐப் பாருங்கள், உங்கள் திருத்துதல் AI அறிவை மேம்படுத்த தொடர!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->