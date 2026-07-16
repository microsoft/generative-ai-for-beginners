# मेटा परिवार मोडेलहरूसँग निर्माण गर्दै 

## परिचय 

यो पाठले समेट्नेछ: 

- मेटा परिवारका दुई मुख्य मोडेलहरू - Llama 3.1 र Llama 3.2 को अन्वेषण 
- प्रत्येक मोडेलका प्रयोग-केस र परिदृश्यहरूको बुझाइ 
- प्रत्येक मोडेलका अद्वितीय सुविधाहरू देखाउने कोड नमूना 


## मेटा परिवारका मोडेलहरू 

यस पाठमा, हामी मेटा परिवार वा "Llama Herd" का २ मोडेलहरू - Llama 3.1 र Llama 3.2 को अन्वेषण गर्नेछौं।

यी मोडेलहरू विभिन्न भेरियन्टहरूमा उपलब्ध छन् र [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मा पाइन्छन्।

> **नोट:** GitHub Models जुलाई २०२६ को अन्त्यमा बन्द हुँदैछ। AI मोडेलहरूसँग प्रोटोटाइप गर्न [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) प्रयोग गर्ने बारे थप विवरणहरू यहाँ छन्।

मोडेल भेरियन्टहरू: 
- Llama 3.1 - ७०B इन्स्ट्रक्ट 
- Llama 3.1 - ४०५B इन्स्ट्रक्ट 
- Llama 3.2 - ११B भिजन इन्स्ट्रक्ट 
- Llama 3.2 - ९०B भिजन इन्स्ट्रक्ट 

*नोट: Llama 3 पनि Microsoft Foundry Models मा उपलब्ध छ तर यो पाठमा समेटिने छैन*

## Llama 3.1 

४०५ अरब पेरामिटरहरूसँग, Llama 3.1 खुला स्रोत LLM वर्गमा पर्दछ। 

मोडेल पहिलेको Llama 3 रिलीजको अपग्रेड हो जसले प्रदान गर्दछ: 

- ठूलो कन्टेक्स्ट विन्डो - १२८k टोकन्स बनाम ८k टोकन्स 
- ठूलो अधिकतम आउटपुट टोकन्स - ४०९६ बनाम २०४८ 
- राम्रो बहुभाषिक समर्थन - प्रशिक्षण टोकन्सको वृद्धिका कारण 

यीले Llama 3.1 लाई जेनएआई अनुप्रयोगहरू निर्माण गर्दा जटिल प्रयोग-केसहरू ह्यान्डल गर्न सक्षम बनाउँछन्, जस्तै: 
- नेटिभ फङ्सन कलिङ - LLM कार्यप्रवाह बाहिरका बाह्य उपकरण र फङ्सनहरू कल गर्न सक्ने क्षमता
- राम्रो RAG प्रदर्शन - उच्च कन्टेक्स्ट विन्डोका कारण 
- सिंथेटिक डेटा उत्पादन - फाइन-ट्यूनिङ जस्ता कार्यहरूका लागि प्रभावकारी डेटा सिर्जना गर्न सक्ने क्षमता 

### नेटिभ फङ्सन कलिङ 

Llama 3.1 लाई फङ्सन वा उपकरण कलहरू गर्न अझ प्रभावकारी बनाउन फाइन-ट्यून गरिएको छ। यसमा दुई इनबिल्ट उपकरणहरू छन् जुन मोडेलले प्रयोगकर्ताबाट आएको प्रॉम्प्टको आधारमा प्रयोग गर्नुपर्छ भनी चिन्हित गर्न सक्छ। यी उपकरणहरू हुन्: 

- **Brave Search** - वेब खोज गरेर वर्तमान जानकारी जस्तै मौसम पत्ता लगाउन प्रयोग गर्न सकिन्छ 
- **Wolfram Alpha** - जटिल गणितीय गणनाहरूका लागि प्रयोग गर्न सकिन्छ जसले आफ्नै फंक्शन लेख्न आवश्यक पर्दैन। 

तपाईं आफ्नै कस्टम उपकरणहरू पनि बनाउन सक्नुहुन्छ जुन LLM ले कल गर्न सक्छ। 

तलको कोड उदाहरणमा: 

- प्रणाली प्रॉम्प्टमा उपलब्ध उपकरणहरू (brave_search, wolfram_alpha) परिभाषित गरिएका छन्। 
- मौसमको बारेमा सोध्ने प्रयोगकर्ता प्रॉम्प्ट पठाइन्छ। 
- LLM ले Brave Search उपकरण कलको साथ प्रतिक्रिया दिनेछ जसले यस्तो देखिन्छ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*नोट: यो उदाहरणले केवल उपकरण कल गर्दछ, यदि तपाईं परिणाम प्राप्त गर्न चाहनुहुन्छ भने Brave API पृष्ठमा निशुल्क खाता बनाउन र फङ्सन आफैं परिभाषित गर्नुपर्नेछ।

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# यी तपाईंको Microsoft Foundry परियोजनाको "अवलोकन" पृष्ठबाट लिनुहोस्
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

यद्यपि LLM भए तापनि, Llama 3.1 को एउटा सीमा यसको मल्टि-मोडालिटीको अभाव हो। अर्थात्, विभिन्न प्रकारका इनपुट जस्तै चित्रहरू प्रॉम्प्टको रूपमा प्रयोग गर्न र प्रतिक्रिया दिन असमर्थता। यो क्षमता Llama 3.2 को मुख्य सुविधाहरू मध्ये एक हो। यी सुविधाहरूमा समावेश छन्: 

- मल्टि-मोडालिटी - पाठ र चित्र दुबै प्रॉम्प्टहरू मूल्याङ्कन गर्ने क्षमता 
- सानादेखि मध्यम आकारका भेरियन्टहरू (११B र ९०B) - यसले लचीलो डिप्लोयमेन्ट विकल्पहरू प्रदान गर्दछ, 
- पाठ-केवल भेरियन्टहरू (१B र ३B) - यसले मोडेललाई एज / मोबाइल उपकरणहरूमा अनुकूल बनाउन र कम लेटेंसी दिन सक्षम बनाउँछ 

मल्टि-मोडाल समर्थनले खुला स्रोत मोडेलहरूको संसारमा ठूलो कदम प्रतिनिधित्व गर्छ। तलको कोड उदाहरणले चित्र र पाठ प्रॉम्प्ट दुवै लिएर Llama 3.2 ९०B बाट चित्रको विश्लेषण प्राप्त गर्दछ। 


### Llama 3.2 संग मल्टि-मोडाल समर्थन

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

# यी तपाईंको Microsoft Foundry परियोजनाको "सम्पर्क" पृष्ठबाट प्राप्त गर्नुहोस्
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

## सिकाइ यहाँ रोकिँदैन, यात्रा जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र तपाईंको जनरेटिभ AI ज्ञानलाई अझ उन्नत बनाउन जारी राख्नुहोस्!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->