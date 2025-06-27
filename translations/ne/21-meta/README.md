<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:29:10+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ne"
}
-->
# मेटा परिवार मोडेलहरूसँग निर्माण गर्दै

## परिचय

यस पाठले समेट्नेछ:

- दुई मुख्य मेटा परिवार मोडेलहरू - लामा ३.१ र लामा ३.२को अन्वेषण
- प्रत्येक मोडेलको प्रयोग-केसहरू र परिदृश्यहरूको बुझाइ
- प्रत्येक मोडेलको विशेषताहरू देखाउन कोड नमूना

## मेटा परिवारको मोडेलहरू

यस पाठमा, हामी मेटा परिवार वा "लामा हर्ड"बाट २ मोडेलहरू अन्वेषण गर्नेछौं - लामा ३.१ र लामा ३.२

यी मोडेलहरू विभिन्न प्रकारहरूमा उपलब्ध छन् र गिटहब मोडेल बजारमा उपलब्ध छन्। गिटहब मोडेलहरू प्रयोग गरेर [एआई मोडेलहरूसँग प्रोटोटाइप बनाउने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) बारे थप विवरणहरू यहाँ छन्।

मोडेल प्रकारहरू:
- लामा ३.१ - ७०बी निर्देश
- लामा ३.१ - ४०५बी निर्देश
- लामा ३.२ - ११बी भिजन निर्देश
- लामा ३.२ - ९०बी भिजन निर्देश

*नोट: लामा ३ पनि गिटहब मोडेलमा उपलब्ध छ तर यो पाठमा समेटिने छैन*

## लामा ३.१

४०५ अर्ब प्यारामिटरमा, लामा ३.१ खुला स्रोत एलएलएम श्रेणीमा फिट हुन्छ।

यो मोडेलले पहिलेको संस्करण लामा ३लाई सुधार गर्दै निम्न सुविधाहरू प्रदान गर्दछ:

- ठूलो सन्दर्भ विन्डो - १२८k टोकनहरू बनाम ८k टोकनहरू
- ठूलो अधिकतम आउटपुट टोकनहरू - ४०९६ बनाम २०४८
- राम्रो बहुभाषिक समर्थन - प्रशिक्षण टोकनहरूको वृद्धि भएको कारणले

यी सुविधाहरूले लामा ३.१लाई जेनएआई एप्लिकेसनहरू निर्माण गर्दा थप जटिल प्रयोग-केसहरूलाई सम्हाल्न सक्षम बनाउँछ, जस्तै:
- देशी फङ्सन कलिङ - बाह्य उपकरणहरू र फङ्सनहरूलाई एलएलएम कार्यप्रवाह बाहिरबाट कल गर्न सक्ने क्षमता
- राम्रो आरएजी प्रदर्शन - उच्च सन्दर्भ विन्डोको कारणले
- कृत्रिम डाटा उत्पादन - फाइन-ट्युनिङ जस्ता कार्यहरूको लागि प्रभावकारी डाटा सिर्जना गर्न सक्ने क्षमता

### देशी फङ्सन कलिङ

लामा ३.१लाई फङ्सन वा उपकरण कलिङमा थप प्रभावकारी बनाइने गरी फाइन-ट्युन गरिएको छ। यसमा दुई निर्माण गरिएको उपकरणहरू छन् जसलाई मोडेलले प्रयोगकर्ताको प्रम्प्टको आधारमा प्रयोग गर्न आवश्यक ठान्न सक्छ। यी उपकरणहरू हुन्:

- **ब्रेव सर्च** - वेब खोज गरेर मौसम जस्ता अद्यावधिक जानकारी प्राप्त गर्न प्रयोग गर्न सकिन्छ
- **वोल्फ्राम अल्फा** - जटिल गणितीय गणनाहरूको लागि प्रयोग गर्न सकिन्छ, त्यसैले आफ्नै फङ्सनहरू लेख्न आवश्यक पर्दैन।

तपाईं आफ्नो आफ्नै कस्टम उपकरणहरू पनि बनाउन सक्नुहुन्छ जसलाई एलएलएमले कल गर्न सक्छ।

नीचको कोड उदाहरणमा:

- हामी प्रणाली प्रम्प्टमा उपलब्ध उपकरणहरू (ब्रेव_सर्च, वोल्फ्राम_अल्फा) परिभाषित गर्छौं।
- प्रयोगकर्ताको प्रम्प्ट पठाउँछौं जसले निश्चित शहरको मौसमको बारेमा सोध्छ।
- एलएलएमले ब्रेव सर्च उपकरणको कलिङको रूपमा प्रतिक्रिया दिनेछ जसले यस प्रकार देखिनेछ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*नोट: यो उदाहरणले केवल उपकरण कलिङ गर्छ, यदि तपाईंलाई परिणामहरू प्राप्त गर्न चाहनुहुन्छ भने, तपाईंले ब्रेव एपीआई पृष्ठमा एक निःशुल्क खाता सिर्जना गर्न आवश्यक छ र फङ्सनलाई परिभाषित गर्न आवश्यक छ।*

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

एलएलएम भएता पनि, लामा ३.१को एक सीमितता भनेको मल्टिमोडालिटी हो। अर्थात्, छविहरू जस्ता विभिन्न प्रकारका इनपुटहरूलाई प्रम्प्टको रूपमा प्रयोग गर्न र प्रतिक्रियाहरू प्रदान गर्न सक्षम हुनु। यो क्षमता लामा ३.२को मुख्य विशेषताहरू मध्ये एक हो। यी विशेषताहरूमा समावेश छन्:

- मल्टिमोडालिटी - पाठ र छवि प्रम्प्टहरू दुबैको मूल्यांकन गर्न सक्षम छ
- सानोदेखि मध्यम आकारका भेरिएसनहरू (११बी र ९०बी) - यसले लचिलो परिनियोजन विकल्पहरू प्रदान गर्दछ,
- केवल पाठ भेरिएसनहरू (१बी र ३बी) - यसले मोडेललाई किनार/मोबाइल उपकरणहरूमा परिनियोजन गर्न अनुमति दिन्छ र कम विलम्बता प्रदान गर्दछ

मल्टिमोडल समर्थनले खुला स्रोत मोडेलहरूको दुनियाँमा ठूलो कदमको प्रतिनिधित्व गर्छ। नीचको कोड उदाहरणले छवि र पाठ प्रम्प्ट दुबैलाई लामा ३.२ ९०बीबाट छविको विश्लेषण प्राप्त गर्न प्रयोग गर्छ।

### लामा ३.२सँग मल्टिमोडल समर्थन

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

यस पाठ पूरा गरेपछि, हाम्रो [जेनरेटिभ एआई लर्निङ संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) जाँच गर्नुहोस् र जेनरेटिभ एआईको ज्ञानलाई अझ बढाउनुहोस्!

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। यसको मौलिक भाषामा रहेको दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यो अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्या प्रति हामी जिम्मेवार छैनौं।