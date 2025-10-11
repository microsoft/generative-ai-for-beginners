<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-10-11T11:35:05+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ta"
}
-->
# மெட்டா குடும்ப மாடல்களுடன் கட்டமைத்தல்

## அறிமுகம்

இந்த பாடத்தில் நாம் கற்றுக்கொள்ளப் போவது:

- மெட்டா குடும்பத்தின் இரண்டு முக்கிய மாடல்களை ஆராய்வது - Llama 3.1 மற்றும் Llama 3.2  
- ஒவ்வொரு மாடலின் பயன்பாடுகள் மற்றும் சூழல்களைப் புரிந்துகொள்வது  
- ஒவ்வொரு மாடலின் தனித்துவமான அம்சங்களை காட்டும் குறியீட்டு உதாரணம்  

## மெட்டா குடும்ப மாடல்கள்

இந்த பாடத்தில், மெட்டா குடும்பத்திலிருந்து அல்லது "Llama Herd" என அழைக்கப்படும் 2 மாடல்களை ஆராய்வோம் - Llama 3.1 மற்றும் Llama 3.2  

இந்த மாடல்கள் பல்வேறு மாறுபாடுகளில் கிடைக்கின்றன மற்றும் GitHub Model சந்தையில் கிடைக்கின்றன. AI மாடல்களுடன் [prototype செய்ய GitHub Models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) பயன்படுத்துவது பற்றிய கூடுதல் விவரங்கள் இங்கே உள்ளன.

மாடல் மாறுபாடுகள்:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*குறிப்பு: Llama 3 GitHub Models-ல் கிடைக்கிறது, ஆனால் இந்த பாடத்தில் அது கையாளப்படாது.*

## Llama 3.1

405 பில்லியன் அளவிலான அளவுகோல்களுடன், Llama 3.1 திறந்த மூல LLM வகையில் பொருந்துகிறது.

இந்த மாடல் Llama 3-ன் முந்தைய வெளியீட்டின் மேம்படுத்தலாக செயல்படுகிறது, மேலும் இது வழங்குகிறது:

- பெரிய சூழல் சாளரம் - 128k டோக்கன்கள் vs 8k டோக்கன்கள்  
- அதிகபட்ச வெளியீடு டோக்கன்கள் - 4096 vs 2048  
- மேம்பட்ட பன்மொழி ஆதரவு - பயிற்சி டோக்கன்களின் அதிகரிப்பால்  

இவை Llama 3.1-ஐ GenAI பயன்பாடுகளை உருவாக்குவதற்கான சிக்கலான பயன்பாடுகளை கையாள உதவுகிறது, இதில்:  
- இயல்நிலை செயல்பாடு அழைப்புகள் - LLM வேலைப்பாடுகளுக்கு வெளியே வெளிப்புற கருவிகள் மற்றும் செயல்பாடுகளை அழைக்கும் திறன்  
- மேம்பட்ட RAG செயல்திறன் - அதிக சூழல் சாளரத்தால்  
- செயற்கை தரவுத் தயாரிப்பு - நுணுக்கமாக்கல் போன்ற பணிகளுக்கு பயனுள்ள தரவுகளை உருவாக்கும் திறன்  

### இயல்நிலை செயல்பாடு அழைப்புகள்

Llama 3.1 செயல்பாடு அல்லது கருவி அழைப்புகளைச் செய்ய மேலும் திறமையாக இருக்க பயிற்சி அளிக்கப்பட்டுள்ளது. இது பயனர் கேள்வியின் அடிப்படையில் பயன்படுத்தப்பட வேண்டியதாக மாடல் அடையாளம் காணும் இரண்டு உள்ளமைக்கப்பட்ட கருவிகளை கொண்டுள்ளது. இந்த கருவிகள்:

- **Brave Search** - வலை தேடலின் மூலம் வானிலை போன்ற தற்போதைய தகவல்களைப் பெற பயன்படுத்தலாம்  
- **Wolfram Alpha** - உங்கள் சொந்த செயல்பாடுகளை எழுத தேவையில்லாமல் சிக்கலான கணித கணக்குகளைச் செய்ய பயன்படுத்தலாம்  

நீங்கள் LLM அழைக்கக்கூடிய உங்கள் சொந்த தனிப்பயன் கருவிகளை உருவாக்கவும் முடியும்.

கீழே உள்ள குறியீட்டு உதாரணத்தில்:

- நாம் கிடைக்கக்கூடிய கருவிகளை (brave_search, wolfram_alpha) system prompt-ல் வரையறுக்கிறோம்.  
- ஒரு குறிப்பிட்ட நகரத்தின் வானிலை பற்றி கேட்கும் பயனர் கேள்வியை அனுப்புகிறோம்.  
- LLM Brave Search கருவிக்கு ஒரு கருவி அழைப்பை பதிலளிக்கும், இது `<|python_tag|>brave_search.call(query="Stockholm weather")` போன்றதாக இருக்கும்.  

*குறிப்பு: இந்த உதாரணம் கருவி அழைப்பை மட்டுமே செய்கிறது, முடிவுகளைப் பெற விரும்பினால், Brave API பக்கத்தில் இலவச கணக்கை உருவாக்கி செயல்பாட்டை வரையறுக்க வேண்டும்.*

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


## Llama 3.2

LLM ஆக இருந்தாலும், Llama 3.1-க்கு ஒரு வரம்பு உள்ளது, அது பன்முகத்தன்மை. அதாவது, படங்களை prompt-களாக பயன்படுத்தி பதில்களை வழங்கும் திறன். இந்த திறன் Llama 3.2-ன் முக்கிய அம்சங்களில் ஒன்றாகும். இந்த அம்சங்கள் மேலும் உள்ளன:

- பன்முகத்தன்மை - உரை மற்றும் பட prompt-களை மதிப்பீடு செய்யும் திறன்  
- சிறிய முதல் நடுத்தர அளவிலான மாறுபாடுகள் (11B மற்றும் 90B) - இது நெகிழ்வான பிரயோக விருப்பங்களை வழங்குகிறது  
- உரை மட்டும் மாறுபாடுகள் (1B மற்றும் 3B) - இது edge / mobile சாதனங்களில் மாடலை பிரயோகப்படுத்த அனுமதிக்கிறது மற்றும் குறைந்த latency-ஐ வழங்குகிறது  

பன்முக ஆதரவு திறந்த மூல மாடல்களின் உலகில் ஒரு பெரிய முன்னேற்றத்தை பிரதிநிதித்துவப்படுத்துகிறது. கீழே உள்ள குறியீட்டு உதாரணம் Llama 3.2 90B-இல் இருந்து ஒரு படத்தின் பகுப்பாய்வைப் பெற ஒரு படம் மற்றும் உரை prompt-ஐ எடுத்துக்கொள்கிறது.

### Llama 3.2 உடன் பன்முக ஆதரவு

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


## கற்றல் இங்கே நிற்காது, பயணத்தை தொடருங்கள்

இந்த பாடத்தை முடித்த பிறகு, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ஐப் பாருங்கள், உங்கள் Generative AI அறிவை மேலும் மேம்படுத்த!

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறையை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.