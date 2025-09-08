<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:08:34+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ne"
}
-->
# Meta परिवारका मोडेलहरूसँग निर्माण

## परिचय

यस पाठले समेट्नेछ:

- दुई मुख्य Meta परिवारका मोडेलहरू - Llama 3.1 र Llama 3.2 को अन्वेषण
- प्रत्येक मोडेलका प्रयोगका केसहरू र परिदृश्यहरू बुझ्ने
- प्रत्येक मोडेलका अनौठा विशेषताहरू देखाउन कोड नमूना

## Meta परिवारका मोडेलहरू

यस पाठमा, हामी Meta परिवार वा "Llama Herd" का २ मोडेलहरू अन्वेषण गर्नेछौं - Llama 3.1 र Llama 3.2

यी मोडेलहरू विभिन्न भेरियन्टहरूमा उपलब्ध छन् र GitHub Model बजारमा पाइन्छन्। GitHub मोडेलहरू प्रयोग गरेर [AI मोडेलहरूसँग प्रोटोटाइप गर्ने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) बारे थप जानकारी यहाँ छ।

मोडेल भेरियन्टहरू:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Note: Llama 3 पनि GitHub मोडेलहरूमा उपलब्ध छ तर यस पाठमा समेटिने छैन*

## Llama 3.1

४०५ अर्ब प्यारामिटरहरूसँग, Llama 3.1 खुला स्रोत LLM वर्गमा पर्छ।

यो मोडेल पहिलेको Llama 3 को अपग्रेड हो जसले प्रदान गर्छ:

- ठूलो सन्दर्भ विन्डो - १२८k टोकनहरू बनाम ८k टोकनहरू  
- ठूलो अधिकतम आउटपुट टोकन - ४०९६ बनाम २०४८  
- राम्रो बहुभाषिक समर्थन - प्रशिक्षण टोकनहरूको वृद्धिका कारण  

यीले Llama 3.1 लाई जेनएआई एप्लिकेसनहरू निर्माण गर्दा जटिल प्रयोग केसहरू सम्हाल्न सक्षम बनाउँछन्, जस्तै:  
- नेटिभ फंक्शन कलिङ - LLM कार्यप्रवाह बाहिरका बाह्य उपकरण र फंक्शनहरू कल गर्ने क्षमता  
- राम्रो RAG प्रदर्शन - उच्च सन्दर्भ विन्डोका कारण  
- सिंथेटिक डाटा उत्पादन - फाइन-ट्युनिङ जस्ता कार्यहरूका लागि प्रभावकारी डाटा सिर्जना गर्ने क्षमता  

### नेटिभ फंक्शन कलिङ

Llama 3.1 लाई फंक्शन वा उपकरण कल गर्न अझ प्रभावकारी बनाउन फाइन-ट्युन गरिएको छ। यसमा दुई बिल्ट-इन उपकरणहरू छन् जुन मोडेलले प्रयोगकर्ताको प्रॉम्प्ट अनुसार प्रयोग गर्न आवश्यक ठान्छ। ती उपकरणहरू हुन्:

- **Brave Search** - वेब खोज गरेर मौसम जस्ता अद्यावधिक जानकारी प्राप्त गर्न प्रयोग गर्न सकिन्छ  
- **Wolfram Alpha** - जटिल गणितीय गणनाहरूका लागि प्रयोग गर्न सकिन्छ, जसले आफ्नै फंक्शन लेख्न आवश्यक पर्दैन  

तपाईंले आफ्नै कस्टम उपकरणहरू पनि बनाउन सक्नुहुन्छ जुन LLM ले कल गर्न सक्छ।

तलको कोड उदाहरणमा:

- हामी उपलब्ध उपकरणहरू (brave_search, wolfram_alpha) सिस्टम प्रॉम्प्टमा परिभाषित गर्छौं।  
- प्रयोगकर्ताबाट कुनै शहरको मौसम बारे सोध्ने प्रॉम्प्ट पठाउँछौं।  
- LLM ले Brave Search उपकरण कल गर्नेछ जुन यसरी देखिन्छ `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Note: यो उदाहरणले मात्र उपकरण कल गर्छ, यदि तपाईं परिणामहरू प्राप्त गर्न चाहनुहुन्छ भने, तपाईंले Brave API पृष्ठमा निःशुल्क खाता बनाउन र फंक्शन आफैं परिभाषित गर्नुपर्नेछ*

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

LLM भए पनि, Llama 3.1 को एउटा सीमा भनेको मल्टिमोडालिटी हो। अर्थात्, विभिन्न प्रकारका इनपुटहरू जस्तै छविहरूलाई प्रॉम्प्टको रूपमा प्रयोग गर्न र प्रतिक्रिया दिन सक्ने क्षमता। यो क्षमता Llama 3.2 को मुख्य विशेषता हो। यी विशेषताहरूमा समावेश छन्:

- मल्टिमोडालिटी - पाठ र छवि दुवै प्रॉम्प्टहरू मूल्याङ्कन गर्ने क्षमता  
- साना देखि मध्यम आकारका भेरियन्टहरू (11B र 90B) - लचिलो डिप्लोयमेन्ट विकल्पहरू प्रदान गर्छ  
- पाठ मात्र भेरियन्टहरू (1B र 3B) - मोडेललाई एज / मोबाइल उपकरणहरूमा डिप्लोय गर्न र कम विलम्बता प्रदान गर्न सक्षम बनाउँछ  

मल्टिमोडल समर्थन खुला स्रोत मोडेलहरूको दुनियाँमा ठूलो प्रगति हो। तलको कोड उदाहरणले छवि र पाठ दुवै प्रॉम्प्ट लिएर Llama 3.2 90B बाट छविको विश्लेषण प्राप्त गर्छ।

### Llama 3.2 सँग मल्टिमोडल समर्थन

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

## सिकाइ यहाँ रोकिँदैन, यात्रा जारी राख्नुहोस्

यस पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो Generative AI ज्ञानलाई अझ उचाइमा पुर्‍याउनुहोस्!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।