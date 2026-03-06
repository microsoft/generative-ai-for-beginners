# मेटा परिवार मोडेलहरूसँग निर्माण 

## परिचय 

यस पाठले समेट्नेछ: 

- दुई मुख्य मेटा परिवार मोडेलहरू अन्वेषण गर्ने - Llama 3.1 र Llama 3.2 
- प्रत्येक मोडेलका उपयोग केसहरू र परिदृश्यहरू बुझ्ने 
- प्रत्येक मोडेलका अद्वितीय विशेषताहरू देखाउन कोड नमूना 

## मेटा परिवारका मोडेलहरू 

यस पाठमा, हामी मेटा परिवार वा "Llama Herd" का २ मोडेलहरू अन्वेषण गर्नेछौं - Llama 3.1 र Llama 3.2।

यी मोडेलहरू भिन्न प्रकारहरूमा उपलब्ध छन् र GitHub मोडेल मार्केटप्लेसमा उपलब्ध छन्। यहाँ GitHub मोडेलहरू प्रयोग गरेर [AI मोडेलहरूसँग प्रोटोटाइप गर्ने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) थप विवरणहरू छन्।

मोडेल भेरियन्टहरू: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*टिप्पणी: Llama 3 पनि GitHub मोडेलहरूमा उपलब्ध छ तर यस पाठमा समेटिएको छैन*

## Llama 3.1 

४०५ बिलियन प्यारामिटरहरूको साथ, Llama 3.1 खुला स्रोत LLM को वर्गमा पर्छ। 

यो मोडेल पहिलेको रिलीज Llama 3 को उन्नत संस्करण हो जसले निम्न प्रदान गर्छ: 

- ठूलो कन्टेक्स्ट विन्डो - १२८k टोकनहरू बनाम ८k टोकनहरू 
- ठूलो अधिकतम आउटपुट टोकनहरू - ४०९६ बनाम २०४८ 
- बेहतर बहुभाषी समर्थन - प्रशिक्षण टोकनहरूमा वृद्धि भएको कारण 

यीहरूले Llama 3.1 लाई जेनएआई अनुप्रयोगहरू विकास गर्दा थप जटिल केसहरू सम्हाल्न सक्षम बनाउँछन् जसमा: 
- नेटिभ फंक्शन कलिङ - एलएलएम कार्यप्रवाह बाहिरको टुलहरू र फंक्शनहरू कॉल गर्ने क्षमता 
- बेहतर RAG प्रदर्शन - उच्च कन्टेक्स्ट विन्डोको कारण 
- सिंथेटिक डाटा जेनेरेसन - फाइन-ट्यूनिङ जस्ता कार्यहरूको लागि प्रभावकारी डाटा बनाउने क्षमता 

### नेटिभ फंक्शन कलिङ 

Llama 3.1 लाई फंक्शन वा टुल कल गर्न अझ प्रभावकारी बनाउन फाइन-ट्यून गरिएको छ। यसमा दुई इन-बिल्ट टुलहरू छन् जुन मोडेलले प्रयोगकर्ताको प्रॉम्प्ट अनुसार प्रयोग गर्नुपर्ने ठानेर चिन्हित गर्न सक्छ। यी टुलहरू हुन्: 

- **Brave Search** - वेब खोज गरेर मौसम जस्तो अपडेट गरिएको जानकारी लिन प्रयोग गर्न सकिन्छ 
- **Wolfram Alpha** - थप जटिल गणितीय गणनाहरूका लागि प्रयोग गर्न सकिन्छ ताकि आफ्नै फंक्शन लेख्न नपरोस्। 

तपाईंले आफ्नै कस्टम टुलहरू पनि सिर्जना गर्न सक्नुहुन्छ जुन एलएलएमले कल गर्न सक्छ। 

तलको कोड उदाहरणमा: 

- हामी सिस्टम प्रॉम्प्टमा उपलब्ध टुलहरू (brave_search, wolfram_alpha) परिभाषित गर्छौं। 
- एक प्रयोगकर्ता प्रॉम्प्ट पठाउँछौं जसले कुनै विशेष शहरको मौसम बारे सोध्छ। 
- एलएलएमले Brave Search टुल कलसँग प्रतिक्रिया दिनेछ जुन यस प्रकार देखिनेछ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*टिप्पणी: यो उदाहरणले मात्र टुल कल गर्छ, परिणामहरू प्राप्त गर्न चाहनुहुन्छ भने तपाईंले Brave API पृष्ठमा निःशुल्क खाता बनाउनुपर्नेछ र फंक्शन आफैं परिभाषित गर्नुपर्नेछ।*

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

एलएलएम भए तापनि, Llama 3.1 को एक सीमा भनेको यसको बहुमाध्यमता अभाव हो। अर्थात, छविहरू जस्ता विभिन्न प्रकारका इनपुटलाई प्रॉम्प्टको रूपमा प्रयोग गर्न र जवाफ दिन नसक्ने। यो क्षमता Llama 3.2 को मुख्य विशेषता मध्ये एक हो। यी विशेषताहरूमा समावेश छन्: 

- बहुमाध्यमता - पाठ र छवि दुवै प्रॉम्प्टहरू मूल्यांकन गर्ने क्षमता 
- सानो देखि मध्यम आकारका भेरियन्टहरू (११B र ९०B) - लचिलो कार्यान्वयन विकल्पहरू प्रदान गर्दछ, 
- पाठ मात्र भेरियन्टहरू (१B र ३B) - मोडेललाई एज / मोबाइल उपकरणहरूमा चलाउन योग्य बनाउँछ र कम विलम्बता प्रदान गर्दछ 

बहुमाध्यमिक समर्थनले खुला स्रोत मोडेलहरूको संसारमा ठूलो कदम प्रतिनिधित्व गर्दछ। तलको कोड उदाहरणले Llama 3.2 90B बाट छवि र पाठ दुवै प्रॉम्प्ट लिएर छविको विश्लेषण प्राप्त गर्दछ। 

### Llama 3.2 सँग बहुमाध्यमिक समर्थन

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

## सिकाइ यहाँ रोकिन्छैन, यात्रालाई जारी राख्नुहोस्

यस पाठ सकिए पछि, हाम्रो [Generative AI सिकाइ संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) अवलोकन गर्नुहोस् र आफ्नो जेनरेटिभ एआई ज्ञानलाई अझ उच्च स्तरमा पुर्‍याउनुहोस्!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अनावश्यक सूचना**:
यो दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असत्यता हुनसक्छ। मूल भाषामा रहेको दस्तावेज नै अधिकारिक स्रोत मानिनु पर्छ। महत्त्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार रहने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->