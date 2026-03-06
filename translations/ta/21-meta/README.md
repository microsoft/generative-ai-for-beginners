# மெட்டா குடும்ப மாதிரிகளுடன் கட்டமைத்தல்

## அறிமுகம்

இந்த பாடத்தில் பரவலாக கவரப்படும்:

- இரு முக்கிய மெட்டா குடும்ப மாதிரிகளான - லாமா 3.1 மற்றும் லாமா 3.2-ஐ ஆராய்வு
- ஒவ்வொரு மாதிரிக்கும் பயன்பாடுகள் மற்றும் சூழ்நிலைகளை புரிந்து கொள்ளல்
- ஒவ்வொரு மாதிரியின் தனித்தன்மை அம்சங்களை காட்டும் குறியீடு உதாரணம்

## மெட்டா குடும்ப மாதிரிகள்

இந்த பாடத்தில், நாங்கள் மெட்டா குடும்பத்திலிருந்து அல்லது "லாமா கூட்டம்" என்ற 2 மாதிரிகளை ஆராய்வோம் - லாமா 3.1 மற்றும் லாமா 3.2.

இந்த மாதிரிகள் வெவ்வேறு வகைகளில் கிடைக்கின்றன மற்றும் GitHub மாதிரி சந்தையில் கிடைக்கின்றன. AI மாதிரிகளுடன் [prototype செய்ய GitHub மாதிரிகள் பயன்படுத்துதல்](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) பற்றிய மேலும் விவரங்கள் கீழே உள்ளன.

மாதிரி வகைகள்:
- லாமா 3.1 - 70B அனுப்பி அமைப்பு
- லாமா 3.1 - 405B அனுப்பி அமைப்பு
- லாமா 3.2 - 11B வானிலை அனுப்பி அமைப்பு
- லாமா 3.2 - 90B வானிலை அனுப்பி அமைப்பு

*குறிப்பு: லாமா 3 GitHub மாதிரிகளில் கிடைக்கிறது ஆனால் இந்த பாடத்தில் கையாளப்படாது*

## லாமா 3.1

405 பில்லியன் பரிமாணங்கள் கொண்ட லாமா 3.1 திறந்த மூல LLM வகைக்கு உட்பட்டது.

இந்த மாதிரி முந்தைய வெளியீடு லாமா 3 இன் மேம்பட்ட பதிப்பாக:

- பெரிய உள்ளடக்க சாளரம் - 8k டோக்கன்களுக்கு 128k டோக்கன்கள்
- அதிகபட்ச வெளியீடு டோக்கன்கள் - 2048 க்கு பதிலாக 4096
- சிறந்த பன்மொழி ஆதரவு - பயிற்சி டோக்கன்கள் அதிகரிப்பு காரணமாக

இவை லாமா 3.1-ஐ GenAI பயன்பாடுகள் உருவாக்கும் போது அதிக சிக்கலான பயன்பாடுகளை கையாள மூலமாகின்றன, כגון:
- கோட்பிரதி இயந்திர செயல்பாட்டை அழைப்பது - LLM பண்முறைவழியில் வெளியிலுள்ள கருவிகள் மற்றும் செயல்பாடுகளை அழைக்கும் திறன்
- சிறந்த RAG செயல்திறன் - அதிக உள்ளடக்க சாளரத்தால்
- செயற்கை தரவு உருவாக்கல் - சிறந்த டிரெய்னிங் போன்ற பணிகளுக்கு பொருத்தமான தரவை உருவாக்கும் திறன்

### நேட்டிவ் செயல்பாட்டு அழைப்பு

லாமா 3.1 செயல்பாடுகள் அல்லது கருவி அழைப்புகள் செய்ய அதிக திறன் பெற உயிருக்குத்துறை செய்யப்பட்டிருக்கிறது. இரண்டு முன்னிருப்பு கருவிகள் உள்ளன, அவை பயனாளர் வழங்கும் கோரிக்கையின் அடிப்படையில் பயன்படுத்தப்படவேண்டியவை என்று மாதிரி கூற முடியும்.

இவை:

- **Brave Search** - வலை தேடல் மூலம் மீதியான தகவல்களைப் பெற உதவும், போலியான உதவி தகவல்களைப் போன்ற தகவல்களை பெற பயன்படுத்தலாம்
- **Wolfram Alpha** - சிக்கலான கணிதக் கணக்குகளை செய்வதற்கு; உங்கள் சொந்த செயல்பாடுகளை எழுத தேவையில்லை

நீங்கள் உங்கள் சொந்த தனிப்பயன் கருவிகளை உருவாக்கி LLM அழைக்க வைக்கலாம்.

கீழ்க்கண்ட குறியீடு உதாரணத்தில்:

- பயன்படுத்தப்படும் கருவிகள் (brave_search, wolfram_alpha) அமைப்பு வேண்டுகோலில் வரையறுக்கப்பட்டுள்ளன.
- ஒரு பயனர் கோரிக்கை அனுப்பப்படுகிறது, ஒரு குறிப்பிட்ட நகரின் வானிலை பற்றி கேட்கின்றது.
- LLM Brave Search கருவிக்கு அழைப்பை அனுப்பும், இது இவ்விதமாக இருக்கும் `<|python_tag|>brave_search.call(query="Stockholm weather")`

*குறிப்பு: இந்த உதாரணம் கருவி அழைப்பை மட்டுமே செய்யும், நீங்கள் முடிவுகளைப் பெற விரும்பினால் Brave API பக்கம் இலவச கணக்கை உருவாக்கி செயல்பாட்டை வரையறுக்க வேண்டும்.*

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

## லாமா 3.2

LLM ஆக இருந்தாலும், லாமா 3.1 இன் ஒரு குறைவு அதன் பன்மோதிர்தன்மையின் இல்லாமை ஆகும். அதாவது, படங்களை போன்ற வேறு வகை உள்ளீடுகளை மேம்படுத்தும் திறன் இல்லாதது. இது லாமா 3.2 இன் முக்கிய அம்சங்களில் ஒன்று. இவை மேலும் கொண்டுள்ளன:

- பன்மோதிர்தன்மை - உரை மற்றும் பட கோரிக்கைகளை இரண்டும் மதிப்பாய்வு செய்யும் திறன்
- சிறிய மற்றும் நடுத்தர அளவு மாற்றுகள் (11B மற்றும் 90B) - இது தளவமைப்பில் பல்வேறு விருப்பங்களை வழங்குகிறது
- உரை மட்டுமே மாறுபாடுகள் (1B மற்றும் 3B) - இது விளிம்பு / கைபேசி சாதனங்களில் மாதிரியை இயக்க உதவுகிறது மற்றும் குறைந்த தாமதத்துடன் செயல்படுகிறது

பன்மோதிர ஆதரவு திறந்த மூல மாதிரிகளின் உலகில் பெரிய முன்னேற்றமாகும். கீழ்க்காணும் குறியீடு உதாரணம் லாமா 3.2 90B-இல் இருந்து புகைப்படம் மற்றும் உரை கோரிக்கையை இணைத்து படத்தைப் பகுப்பாய்வு செய்கிறது.

### லாமா 3.2 உடன் பன்மோதிர்தன்மை ஆதரவு

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

## கற்றல் இங்கு நிற்கவில்லை, பயணத்தை தொடருங்கள்

இந்த பாடத்தை முடித்த பிறகு, எங்கள் [ஜெனரேட்டிவ் AI கற்றல் தொகுப்பை](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) பார்வையிட்டு உங்கள் ஜெனரேட்டிவ் AI அறிவை மேம்படுத்தத் தொடங்குங்கள்!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**வெளியுறுத்தல்**:
இந்த ஆவணம் AI மொழி மாற்ற சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயல்வதும் உண்மைதானாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். தமிழில் உள்ள அசல் ஆவணம் அதிகாரபூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவலுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்படுத்தலால் ஏற்பட்ட எந்தவொரு தவறான புரிதலுக்கும் அல்லது தவறான விளக்கங்களுக்கும் எங்களால் பொறுப்பு ஏற்றுக்கொள்ளப்படமாட்டாது.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->