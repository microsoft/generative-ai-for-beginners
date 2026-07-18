# मेटा फैमिली मॉडल के साथ निर्माण  

## परिचय  

इस पाठ में कवर किया जाएगा:  

- दो मुख्य मेटा फैमिली मॉडलों का अन्वेषण - Llama 3.1 और Llama 3.2  
- प्रत्येक मॉडल के उपयोग के मामले और परिदृश्यों को समझना  
- प्रत्येक मॉडल की अनूठी विशेषताओं को दिखाने के लिए कोड नमूना  


## मेटा मॉडल परिवार  

इस पाठ में, हम मेटा परिवार या "Llama Herd" के 2 मॉडल्स का अन्वेषण करेंगे - Llama 3.1 और Llama 3.2।  

ये मॉडल विभिन्न वैरिएंट्स में उपलब्ध हैं और [Microsoft Foundry Models कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) में उपलब्ध हैं।  

> **नोट:** GitHub Models जुलाई 2026 के अंत में बंद हो रहा है। AI मॉडलों के साथ प्रोटोटाइप बनाने के लिए [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) का उपयोग करने के बारे में अधिक जानकारी यहाँ देखें।  

मॉडल वैरिएंट्स:  
- Llama 3.1 - 70B इंस्ट्रक्ट  
- Llama 3.1 - 405B इंस्ट्रक्ट  
- Llama 3.2 - 11B विज़न इंस्ट्रक्ट  
- Llama 3.2 - 90B विज़न इंस्ट्रक्ट  

*नोट: Llama 3 Microsoft Foundry Models में भी उपलब्ध है लेकिन इस पाठ में इसे शामिल नहीं किया गया है*  

## Llama 3.1  

405 अरब पैरामीटर्स के साथ, Llama 3.1 ओपन सोर्स LLM श्रेणी में आता है।  

यह मॉडल पहले रिलीज़ Llama 3 के अपग्रेड के रूप में निम्नलिखित विशेषताएं प्रदान करता है:  

- बड़ा कॉन्टेक्स्ट विंडो - 128k टोकन बनाम 8k टोकन  
- अधिकतम आउटपुट टोकन अधिक - 4096 बनाम 2048  
- बेहतर बहुभाषी समर्थन - प्रशिक्षण टोकन में वृद्धि के कारण  

ये सुविधाएं Llama 3.1 को जेनएआई अनुप्रयोगों को बनाते समय अधिक जटिल उपयोग मामलों को संभालने में सक्षम बनाती हैं जिनमें शामिल हैं:  
- नेटिव फंक्शन कॉलिंग - बाहरी टूल और फंक्शन को LLM वर्कफ़्लो के बाहर कॉल करने की क्षमता  
- बेहतर RAG प्रदर्शन - अधिक कॉन्टेक्स्ट विंडो के कारण  
- सिंथेटिक डेटा जनरेशन - फाइन-ट्यूनिंग जैसे कार्यों के लिए प्रभावी डेटा बनाने की क्षमता  

### नेटिव फंक्शन कॉलिंग  

Llama 3.1 को फंक्शन या टूल कॉल करने में अधिक प्रभावी बनने के लिए फाइन-ट्यून किया गया है। इसमें दो बिल्ट-इन टूल्स भी शामिल हैं जिन्हें मॉडल उपयोगकर्ता के प्रॉम्प्ट के आधार पर उपयोग करने की आवश्यकता पहचान सकता है। ये टूल हैं:  

- **ब्रेव सर्च** - वेब सर्च करके नवीनतम जानकारी जैसे मौसम प्राप्त करने के लिए इस्तेमाल किया जा सकता है  
- **वोल्फ्राम अल्फा** - और अधिक जटिल गणितीय गणनाओं के लिए इस्तेमाल किया जा सकता है, इसलिए अपनी स्वयं की फंक्शन लिखने की जरूरत नहीं है।  

आप अपने स्वयं के कस्टम टूल भी बना सकते हैं जिन्हें LLM कॉल कर सकता है।  

नीचे दिए गए कोड उदाहरण में:  

- सिस्टम प्रॉम्प्ट में उपलब्ध टूल्स (brave_search, wolfram_alpha) परिभाषित किए गए हैं।  
- एक उपयोगकर्ता प्रॉम्प्ट भेजा जाता है जो किसी विशेष शहर के मौसम के बारे में पूछता है।  
- LLM ब्रेव सर्च टूल को कॉल के साथ जवाब देगा जो इस प्रकार दिखेगा `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*नोट: यह उदाहरण केवल टूल कॉल करता है, यदि आप परिणाम प्राप्त करना चाहते हैं, तो आपको ब्रेव API पेज पर एक मुफ्त खाता बनाना होगा और फंक्शन को परिभाषित करना होगा।  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# इन्हें अपने Microsoft Foundry प्रोजेक्ट के "अवलोकन" पृष्ठ से प्राप्त करें
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

LLM होते हुए भी, Llama 3.1 की एक सीमा इसकी मल्टीमॉडलिटी की कमी है। अर्थात्, यह इमेज जैसे विभिन्न प्रकार के इनपुट को प्रॉम्प्ट के रूप में उपयोग करने और प्रतिक्रिया प्रदान करने में सक्षम नहीं है। यह क्षमता Llama 3.2 की मुख्य विशेषताओं में से एक है। ये विशेषताएं भी शामिल हैं:  

- मल्टीमॉडलिटी - टेक्स्ट और इमेज दोनों प्रॉम्प्ट का मूल्यांकन करने की क्षमता  
- छोटे से मध्यम आकार के वैरिएंट्स (11B और 90B) - जिससे लचीली डिप्लॉयमेंट विकल्प मिलते हैं,  
- केवल टेक्स्ट वैरिएंट्स (1B और 3B) - यह मॉडल को एज / मोबाइल उपकरणों पर डिप्लॉय करने की अनुमति देता है और कम लेटेंसी प्रदान करता है  

मल्टीमॉडल समर्थन खुले स्रोत मॉडलों की दुनिया में एक बड़ा कदम है। नीचे दिया गया कोड उदाहरण इमेज और टेक्स्ट प्रॉम्प्ट दोनों लेता है ताकि Llama 3.2 90B से इमेज का विश्लेषण प्राप्त किया जा सके।  


### Llama 3.2 के साथ मल्टीमॉडल समर्थन  

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

# इन्हें अपने Microsoft Foundry प्रोजेक्ट के "ओवरव्यू" पेज से प्राप्त करें
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

## सीखना यहीं खत्म नहीं होता, यात्रा जारी रखें  

इस पाठ को पूरा करने के बाद, हमारी [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) देखें ताकि आपके Generative AI ज्ञान को और बढ़ाया जा सके!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->