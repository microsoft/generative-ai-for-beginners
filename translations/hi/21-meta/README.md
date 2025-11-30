<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:07:56+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hi"
}
-->
# Meta परिवार के मॉडल के साथ निर्माण

## परिचय

इस पाठ में निम्नलिखित विषयों को कवर किया जाएगा:

- Meta परिवार के दो मुख्य मॉडल - Llama 3.1 और Llama 3.2 का अन्वेषण
- प्रत्येक मॉडल के उपयोग के मामले और परिदृश्यों को समझना
- प्रत्येक मॉडल की अनूठी विशेषताओं को दिखाने के लिए कोड उदाहरण

## Meta परिवार के मॉडल

इस पाठ में, हम Meta परिवार या "Llama Herd" के 2 मॉडल - Llama 3.1 और Llama 3.2 का अन्वेषण करेंगे।

ये मॉडल विभिन्न वेरिएंट्स में उपलब्ध हैं और GitHub Model मार्केटप्लेस पर मिलते हैं। GitHub Models का उपयोग करके [AI मॉडल के साथ प्रोटोटाइप बनाने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) के बारे में अधिक जानकारी यहाँ है।

मॉडल वेरिएंट्स:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Note: Llama 3 भी GitHub Models पर उपलब्ध है लेकिन इस पाठ में इसे शामिल नहीं किया जाएगा*

## Llama 3.1

405 बिलियन पैरामीटर्स के साथ, Llama 3.1 ओपन सोर्स LLM श्रेणी में आता है।

यह मॉडल पहले के Llama 3 रिलीज का अपग्रेड है, जो निम्नलिखित सुधार प्रदान करता है:

- बड़ा कॉन्टेक्स्ट विंडो - 128k टोकन बनाम 8k टोकन  
- अधिकतम आउटपुट टोकन की संख्या - 4096 बनाम 2048  
- बेहतर बहुभाषी समर्थन - प्रशिक्षण टोकन की वृद्धि के कारण  

ये सुधार Llama 3.1 को जेनएआई एप्लिकेशन बनाने में अधिक जटिल उपयोग मामलों को संभालने में सक्षम बनाते हैं, जिनमें शामिल हैं:  
- नेटिव फंक्शन कॉलिंग - LLM वर्कफ़्लो के बाहर बाहरी टूल और फंक्शन कॉल करने की क्षमता  
- बेहतर RAG प्रदर्शन - उच्च कॉन्टेक्स्ट विंडो के कारण  
- सिंथेटिक डेटा जनरेशन - फाइन-ट्यूनिंग जैसे कार्यों के लिए प्रभावी डेटा बनाने की क्षमता  

### नेटिव फंक्शन कॉलिंग

Llama 3.1 को फंक्शन या टूल कॉल करने में अधिक प्रभावी बनाने के लिए फाइन-ट्यून किया गया है। इसमें दो बिल्ट-इन टूल्स हैं जिन्हें मॉडल उपयोगकर्ता के प्रॉम्प्ट के आधार पर उपयोग करने की आवश्यकता समझ सकता है। ये टूल्स हैं:

- **Brave Search** - वेब सर्च करके मौसम जैसी ताज़ा जानकारी प्राप्त करने के लिए उपयोग किया जा सकता है  
- **Wolfram Alpha** - जटिल गणितीय गणनाओं के लिए उपयोग किया जा सकता है, जिससे अपनी खुद की फंक्शन लिखने की जरूरत नहीं होती  

आप अपने कस्टम टूल भी बना सकते हैं जिन्हें LLM कॉल कर सकता है।

नीचे दिए गए कोड उदाहरण में:

- हम सिस्टम प्रॉम्प्ट में उपलब्ध टूल्स (brave_search, wolfram_alpha) को परिभाषित करते हैं।  
- एक यूजर प्रॉम्प्ट भेजते हैं जो किसी विशेष शहर के मौसम के बारे में पूछता है।  
- LLM Brave Search टूल को कॉल करेगा, जो इस तरह दिखेगा `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Note: यह उदाहरण केवल टूल कॉल करता है, यदि आप परिणाम प्राप्त करना चाहते हैं, तो आपको Brave API पेज पर एक मुफ्त खाता बनाना होगा और फंक्शन को परिभाषित करना होगा।*

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

LLM होते हुए भी, Llama 3.1 की एक सीमा मल्टीमॉडलिटी है। यानी, विभिन्न प्रकार के इनपुट जैसे कि इमेज को प्रॉम्प्ट के रूप में उपयोग करना और प्रतिक्रिया देना। यह क्षमता Llama 3.2 की मुख्य विशेषताओं में से एक है। इन विशेषताओं में शामिल हैं:

- मल्टीमॉडलिटी - टेक्स्ट और इमेज दोनों प्रकार के प्रॉम्प्ट का मूल्यांकन करने की क्षमता  
- छोटे से मध्यम आकार के वेरिएंट्स (11B और 90B) - जो लचीले डिप्लॉयमेंट विकल्प प्रदान करते हैं  
- केवल टेक्स्ट वेरिएंट्स (1B और 3B) - जो मॉडल को एज/मोबाइल डिवाइस पर डिप्लॉय करने और कम विलंबता प्रदान करने की अनुमति देते हैं  

मल्टीमॉडल सपोर्ट ओपन सोर्स मॉडल की दुनिया में एक बड़ा कदम है। नीचे दिया गया कोड उदाहरण Llama 3.2 90B से इमेज और टेक्स्ट दोनों प्रॉम्प्ट लेकर इमेज का विश्लेषण प्राप्त करता है।

### Llama 3.2 के साथ मल्टीमॉडल सपोर्ट

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

## सीखना यहीं खत्म नहीं होता, यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें और अपनी Generative AI की जानकारी को और बढ़ाते रहें!

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।