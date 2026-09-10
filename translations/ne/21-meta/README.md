# Meta परिवार मोडेलहरूसँग निर्माण

## परिचय

यस पाठले समेट्नेछ:

- दुई मुख्य Meta परिवार मोडेलहरूको अन्वेषण - Llama 3.1 र Llama 3.2
- प्रत्येक मोडेलका प्रयोग मामला र परिदृश्यहरूको बुझाइ
- प्रत्येक मोडेलका अद्वितीय विशेषताहरू देखाउने कोड नमुना


## Meta परिवारका मोडेलहरू

यस पाठमा, हामी Meta परिवार वा "Llama Herd" का २ मोडेलहरू - Llama 3.1 र Llama 3.2 अन्वेषण गर्नेछौं।

यी मोडेलहरू विभिन्न भेरियन्टहरूमा आउँछन् र [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मा उपलब्ध छन्।

> **सूचना:** GitHub Models जुलाई २०२६ को अन्त्यमा अवसान हुन्छ। AI मोडेलहरूसँग प्रोटोटाइप गर्न [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) प्रयोग गर्ने बारे थप विवरणहरू यहाँ छन्।

मोडेल भेरियन्टहरू:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*ध्यान दिनुहोस्: Llama 3 पनि Microsoft Foundry Models मा उपलब्ध छ तर यस पाठमा समेटिने छैन*

## Llama 3.1

४०५ अर्ब प्यारामिटरहरू सहित, Llama 3.1 खुला स्रोत LLM को श्रेणीमा पर्छ।

यो मोडेल पहिलेको रिलिज Llama 3 को अपग्रेड हो जसले प्रदान गर्छ:

- ठूलो कन्टेक्स्ट विन्डो - १२८k टोकनहरू बनाम ८k टोकनहरू
- बढी बढी आउटपुट टोकनहरू - ४०९६ बनाम २०४८
- सुधारिएको बहुभाषिक समर्थन - प्रशिक्षण टोकनहरूमा वृद्धि हुँदा

यीले Llama 3.1 लाई जेनएआई अनुप्रयोगहरू निर्माण गर्दा धेरै जटिल प्रयोग मामिलाहरू ह्यान्डल गर्न सक्षम बनाउँछन् जस्तै:
- नेटिभ फंक्शन कलिङ - LLM कार्यप्रवाह बाहेक बाह्य उपकरणहरू र फंक्शनहरू कल गर्न सक्ने क्षमता
- राम्रो RAG प्रदर्शन - माथिल्लो कन्टेक्स्ट विन्डोको कारणले
- सिंथेटिक डाटा उत्पादन - फाइन-ट्यूनिंग जस्ता कार्यहरूको लागि प्रभावकारी डाटा सिर्जना गर्ने क्षमता

### नेटिभ फंक्शन कलिङ

Llama 3.1 लाई फाइन-ट्यून गरिएको छ ताकि यो फंक्शन वा उपकरण कलहरू अझ प्रभावकारी रूपमा गर्न सकून्। यसमा दुई बिल्ट-इन उपकरणहरू छन् जुन मोडेलले प्रयोगकर्ताबाट प्राप्त प्रॉम्प्टको आधारमा प्रयोग गर्न आवश्यक मान्न सक्छ। यी उपकरणहरू हुन्:

- **Brave Search** - वेब खोज गरेर हालको जानकारी जस्तै मौसम प्राप्त गर्न प्रयोग गर्न सकिन्छ
- **Wolfram Alpha** - अधिक जटिल गणितीय हिसाबहरूका लागि प्रयोग गर्न सकिन्छ जसले तपाइँलाई आफ्नै फंक्शनहरू लेख्न आवश्यक छैन।

तपाइँ आफ्नो आफ्नै कस्टम उपकरणहरू पनि बनाउन सक्नुहुन्छ जुन LLM ले कल गर्न सक्छ।

तलको कोड उदाहरणमा:

- हामी प्रणाली प्रॉम्प्टमा उपलब्ध उपकरणहरू (brave_search, wolfram_alpha) परिभाषित गर्छौं।
- प्रयोगकर्ताको प्रॉम्प्ट पठाउँछ जुन कुनै निश्चित सहरको मौसम बारे सोध्छ।
- LLM ले Brave Search उपकरण कलको साथ प्रत्युत्तर दिनेछ जुन यसरी देखिन्छ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ध्यान दिनुहोस्: यस उदाहरणले केवल उपकरण कल मात्र गर्दछ, यदि तपाईँ नतिजा प्राप्त गर्न चाहनुहुन्छ भने, तपाईँलाई Brave API पृष्ठमा नि:शुल्क खाता बनाउन र फंक्शन आफैँ परिभाषित गर्न आवश्यक हुनेछ।*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# यी तपाईंको Microsoft Foundry परियोजनाको "ओभरभ्यू" पृष्ठबाट प्राप्त गर्नुहोस्
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

## Llama 3.2

Llama 3.1 हुनु हुँदाहुँदै पनि, यसको एउटा सीमितता भनेको मल्टिमोडालिटीको अभाव हो। अर्थात्, विभिन्न प्रकारका इन्पुटहरू जस्तै तस्वीरहरूलाई प्रॉम्प्टको रूपमा प्रयोग गर्न र प्रतिक्रियाहरू दिन असमर्थता। यो क्षमता Llama 3.2 को मुख्य विशेषताहरूमध्ये एक हो। यी विशेषताहरूमा समावेश छन्:

- मल्टिमोडालिटी - दुवै पाठ र छवि प्रॉम्प्टहरूको मुल्यांकन गर्ने क्षमता
- सानो देखि मध्यम आकारका भेरियन्टहरू (11B र 90B) - लचिलो तैनाती विकल्पहरू प्रदान गर्दछ,
- पाठ मात्र भेरियन्टहरू (1B र 3B) - मोडेललाई एज / मोबाइल उपकरणहरूमा तैनाथ गर्न अनुमति दिन्छ र कम विलम्बता प्रदान गर्दछ

मल्टिमोडल समर्थनले खुला स्रोत मोडेलहरूको दुनियाँमा ठूलो कदम प्रतिनिधित्व गर्दछ। तलको कोड उदाहरणले छवि र पाठ दुवै प्रॉम्प्ट लिएर Llama 3.2 90B बाट छविको विश्लेषण प्राप्त गर्छ।


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

# यी तपाईंको Microsoft Foundry परियोजनाको "सामग्री" पृष्ठबाट लिनुहोस्
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

## सिकाई यहाँ रोकिँदैन, यात्रालाई निरन्तरता दिनुहोस्

यस पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो Generative AI ज्ञान स्तर बढाउँदै जानुहोस्!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->