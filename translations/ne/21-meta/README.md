<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:09:19+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ne"
}
-->
# मेटा परिवारका मोडेलहरूसँग निर्माण

## परिचय

यस पाठले समेट्नेछ:

- दुई मुख्य मेटा परिवारका मोडेलहरू - लामा ३.१ र लामा ३.२ अन्वेषण गर्दै
- प्रत्येक मोडेलको प्रयोगका केसहरू र परिदृश्यहरू बुझ्दै
- प्रत्येक मोडेलको विशेषताहरू देखाउन कोड नमूना

## मेटा परिवारका मोडेलहरू

यस पाठमा, हामी मेटा परिवार वा "लामा हर्ड" का २ मोडेलहरू - लामा ३.१ र लामा ३.२ अन्वेषण गर्नेछौं।

यी मोडेलहरू विभिन्न भेरिएन्टहरूमा आउँछन् र गिटहब मोडेल मार्केटप्लेसमा उपलब्ध छन्। यहाँ गिटहब मोडेलहरू प्रयोग गरेर [एआई मोडेलहरूसँग प्रोटोटाइप बनाउने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) थप विवरणहरू छन्।

मोडेल भेरिएन्टहरू:
- लामा ३.१ - ७०बी इन्स्ट्रक्ट
- लामा ३.१ - ४०५बी इन्स्ट्रक्ट
- लामा ३.२ - ११बी भिजन इन्स्ट्रक्ट
- लामा ३.२ - ९०बी भिजन इन्स्ट्रक्ट

*नोट: लामा ३ पनि गिटहब मोडेलहरूमा उपलब्ध छ तर यस पाठमा समेटिने छैन*

## लामा ३.१

४०५ अर्ब प्यारामिटरहरूमा, लामा ३.१ खुला स्रोत LLM को श्रेणीमा पर्छ।

मोडेलले पहिलेको रिलीज लामा ३ को अपग्रेड हो जसले प्रदान गर्दछ:

- ठूलो सन्दर्भ विन्डो - १२८k टोकनहरू बनाम ८k टोकनहरू
- ठूलो म्याक्स आउटपुट टोकनहरू - ४०९६ बनाम २०४८
- राम्रो बहुभाषिक समर्थन - प्रशिक्षण टोकनहरूमा वृद्धि भएको कारण

यीले लामा ३.१ लाई GenAI अनुप्रयोगहरू निर्माण गर्दा थप जटिल प्रयोगका केसहरूलाई सम्हाल्न सक्षम बनाउँछ:
- नेटिभ फङ्सन कलिङ - बाह्य उपकरणहरू र कार्यहरूलाई LLM वर्कफ्लो बाहिर कल गर्ने क्षमता
- राम्रो RAG प्रदर्शन - उच्च सन्दर्भ विन्डोको कारण
- कृत्रिम डेटा उत्पादन - फाइन-ट्युनिङ जस्ता कार्यहरूको लागि प्रभावकारी डेटा सिर्जना गर्ने क्षमता

### नेटिभ फङ्सन कलिङ

लामा ३.१ लाई फङ्सन वा उपकरण कलहरू बनाउनेमा थप प्रभावकारी बनाउन फाइन-ट्युन गरिएको छ। यसमा दुई बिल्ट-इन उपकरणहरू छन् जसलाई मोडेलले प्रयोगकर्ताबाट प्राप्त संकेतको आधारमा प्रयोग गर्न आवश्यक भएको पहिचान गर्न सक्छ। यी उपकरणहरू हुन्:

- **ब्रेव सर्च** - वेब सर्च गरेर मौसम जस्ता हालसालका जानकारी प्राप्त गर्न प्रयोग गर्न सकिन्छ
- **वोल्फ्राम अल्फा** - जटिल गणितीय गणनाहरूको लागि प्रयोग गर्न सकिन्छ जसले गर्दा आफ्नै फङ्सनहरू लेख्न आवश्यक पर्दैन।

तपाईंले आफ्नो कस्टम उपकरणहरू पनि बनाउन सक्नुहुन्छ जसलाई LLM ले कल गर्न सक्छ।

नीचेको कोड उदाहरणमा:

- हामी सिस्टम संकेतमा उपलब्ध उपकरणहरू (brave_search, wolfram_alpha) परिभाषित गर्छौं।
- एक प्रयोगकर्ता संकेत पठाउँछ जसले एक निश्चित सहरको मौसमको बारेमा सोध्छ।
- LLM ले ब्रेव सर्च उपकरणमा एक उपकरण कलको साथ प्रतिक्रिया दिनेछ जुन यसरी देखिनेछ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*नोट: यो उदाहरणले केवल उपकरण कल बनाउँछ, यदि तपाईं परिणाम प्राप्त गर्न चाहनुहुन्छ भने, तपाईंले ब्रेव API पृष्ठमा एक नि:शुल्क खाता बनाउन आवश्यक छ र फङ्सनलाई आफैं परिभाषित गर्न आवश्यक छ*

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

## लामा ३.२

LLM भए तापनि, लामा ३.१ को एक सीमितता मल्टिमोडालिटी हो। अर्थात्, चित्रहरू जस्ता विभिन्न प्रकारका इनपुटहरू संकेतको रूपमा प्रयोग गर्न र प्रतिक्रियाहरू प्रदान गर्न सक्षम हुनु। यो क्षमता लामा ३.२ को मुख्य विशेषताहरू मध्ये एक हो। यी विशेषताहरू पनि समावेश छन्:

- मल्टिमोडालिटी - टेक्स्ट र इमेज संकेतहरू दुबै मूल्याङ्कन गर्ने क्षमता छ
- सानो देखि मध्यम आकार भेरिएन्टहरू (११बी र ९०बी) - यसले लचिलो तैनाती विकल्पहरू प्रदान गर्दछ,
- केवल टेक्स्ट भेरिएन्टहरू (१बी र ३बी) - यसले मोडेललाई किनारा / मोबाइल उपकरणहरूमा तैनात गर्न अनुमति दिन्छ र कम विलम्बता प्रदान गर्दछ

मल्टिमोडल समर्थनले खुला स्रोत मोडेलहरूको संसारमा ठूलो कदमको प्रतिनिधित्व गर्दछ। नीचेको कोड उदाहरणले लामा ३.२ ९०बी बाट चित्रको विश्लेषण प्राप्त गर्न इमेज र टेक्स्ट संकेत दुबै लिन्छ।

### लामा ३.२ संग मल्टिमोडल समर्थन

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

यस पाठ पूरा गरेपछि, हाम्रो [जनरेटिव एआई सिकाइ संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) जाँच गर्नुहोस् आफ्नो जनरेटिव एआई ज्ञानलाई स्तरवृद्धि गर्न जारी राख्न!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्दछौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको दस्तावेजलाई प्राधिकृत स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।