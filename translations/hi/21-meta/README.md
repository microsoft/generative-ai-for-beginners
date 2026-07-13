# मेटा परिवार मॉडल के साथ निर्माण 

## परिचय 

इस पाठ में यह शामिल होगा: 

- दो मुख्य मेटा परिवार मॉडलों का अन्वेषण - लामा 3.1 और लामा 3.2 
- प्रत्येक मॉडल के उपयोग के मामले और परिदृश्यों की समझ 
- प्रत्येक मॉडल की विशिष्ट विशेषताओं को दिखाने के लिए कोड उदाहरण 


## मेटा परिवार के मॉडल 

इस पाठ में, हम मेटा परिवार या "लामा हर्ड" से 2 मॉडलों - लामा 3.1 और लामा 3.2 का अन्वेषण करेंगे।

ये मॉडल विभिन्न प्रकारों में उपलब्ध हैं और [Microsoft Foundry Models कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) में पाये जा सकते हैं।

> **ध्यान दें:** GitHub Models जुलाई 2026 के अंत में सेवा समाप्त कर रहा है। AI मॉडल्स के साथ प्रोटोटाइप बनाने के लिए [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) का उपयोग करने का अधिक विवरण यहां है।

मॉडल प्रकार: 
- लामा 3.1 - 70B इंस्ट्रक्ट 
- लामा 3.1 - 405B इंस्ट्रक्ट 
- लामा 3.2 - 11B विज़न इंस्ट्रक्ट 
- लामा 3.2 - 90B विज़न इंस्ट्रक्ट 

*ध्यान दें: लामा 3 भी Microsoft Foundry Models में उपलब्ध है लेकिन इस पाठ में इसका कवर नहीं किया जाएगा*

## लामा 3.1 

405 बिलियन पैरामीटर्स के साथ, लामा 3.1 ओपन सोर्स LLM श्रेणी में आता है। 

यह मॉडल पिछले संस्करण लामा 3 की तुलना में अपग्रेड है जो प्रदान करता है: 

- बड़ा संदर्भ विंडो - 128k टोकन बनाम 8k टोकन 
- बड़ा अधिकतम आउटपुट टोकन - 4096 बनाम 2048 
- बेहतर बहुभाषी समर्थन - प्रशिक्षण टोकन में वृद्धि के कारण 

ये लामा 3.1 को जेनएआई एप्लिकेशन बनाने के दौरान अधिक जटिल उपयोग मामलों को संभालने में सक्षम बनाते हैं, जिनमें शामिल हैं: 
- नेटिव फंक्शन कॉलिंग - LLM वर्कफ़्लो के बाहर बाहरी टूल और फ़ंक्शन कॉल करने की क्षमता 
- बेहतर RAG प्रदर्शन - उच्च संदर्भ विंडो के कारण 
- सिंथेटिक डेटा जेनरेशन - फाइन-ट्यूनिंग जैसे कार्यों के लिए प्रभावी डेटा बनाने की क्षमता 

### नेटिव फंक्शन कॉलिंग 

लामा 3.1 को फाइन-ट्यून किया गया है जिससे यह फ़ंक्शन या टूल कॉल करने में अधिक प्रभावी हो गया है। इसमें दो अंतर्निहित टूल्स भी हैं जिन्हें मॉडल उपयोगकर्ता से प्राप्त प्रम्प्ट के आधार पर उपयोग किए जाने योग्य पहचान सकता है। ये टूल हैं: 

- **ब्रेव सर्च** - वेब खोज करके मौसम जैसी अद्यतन जानकारी प्राप्त करने के लिए उपयोग किया जा सकता है 
- **वोल्फ्राम अल्फा** - अधिक जटिल गणितीय गणनाओं के लिए उपयोग किया जाता है जिससे अपनी खुद की फ़ंक्शन लिखने की आवश्यकता नहीं पड़ती। 

आप अपने स्वयं के कस्टम टूल भी बना सकते हैं जिन्हें LLM कॉल कर सकता है। 

नीचे कोड उदाहरण में: 

- हम सिस्टम प्रम्प्ट में उपलब्ध टूल्स (brave_search, wolfram_alpha) को परिभाषित करते हैं। 
- उपयोगकर्ता से एक प्रम्प्ट भेजते हैं जो किसी शहर के मौसम के बारे में पूछता है। 
- LLM ब्रेव सर्च टूल को कॉल करके प्रतिक्रिया देगा जो इस प्रकार दिखेगा `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ध्यान दें: यह उदाहरण केवल टूल कॉल करता है, यदि आप परिणाम प्राप्त करना चाहते हैं, तो आपको ब्रेव API पेज पर एक मुफ्त खाता बनाना होगा और स्वयं फ़ंक्शन को परिभाषित करना होगा।*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# इन्हें अपने Microsoft Foundry परियोजना के "ओवरव्यू" पृष्ठ से प्राप्त करें
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

## लामा 3.2 

लामा 3.1 एक LLM होते हुए भी, इसकी एक सीमा इसकी मल्टीमॉडलिटी की कमी है। अर्थात, इमेज के रूप में विभिन्न प्रकार के इनपुट का उपयोग करने और प्रतिक्रियाएं देने में असमर्थता। यह योग्यता लामा 3.2 की मुख्य विशेषताओं में से एक है। इनमें शामिल अन्य विशेषताएँ हैं: 

- मल्टीमॉडलिटी - दोनों टेक्स्ट और इमेज प्रम्प्ट्स का मूल्यांकन करने की क्षमता 
- छोटे से मध्यम आकार के विकल्प (11B और 90B) - यह लचीलापन तैनाती विकल्प प्रदान करता है, 
- केवल टेक्स्ट विकल्प (1B और 3B) - यह मॉडल को एज/मोबाइल डिवाइस पर तैनात करने देता है और कम विलंबता प्रदान करता है 

मल्टीमॉडल समर्थन खुले स्रोत मॉडलों की दुनिया में एक बड़ा कदम है। नीचे दिया गया कोड उदाहरण एक इमेज और टेक्स्ट दोनों प्रम्प्ट लेकर लामा 3.2 90B से इमेज का विश्लेषण प्राप्त करता है। 


### लामा 3.2 के साथ मल्टीमॉडल समर्थन

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

## सीखना यहाँ नहीं रुकता, यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जेनरेटिव AI ज्ञान को अगले स्तर तक बढ़ा सकें!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->