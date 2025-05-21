<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:08:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hi"
}
-->
# मेटा फैमिली मॉडल्स के साथ निर्माण 

## परिचय 

इस पाठ में शामिल होगा: 

- दो मुख्य मेटा फैमिली मॉडल्स - Llama 3.1 और Llama 3.2 का अन्वेषण 
- प्रत्येक मॉडल के उपयोग के मामले और परिदृश्यों को समझना 
- प्रत्येक मॉडल की अनूठी विशेषताओं को दिखाने के लिए कोड उदाहरण 

## मेटा फैमिली के मॉडल्स 

इस पाठ में, हम मेटा फैमिली या "Llama Herd" के 2 मॉडल्स - Llama 3.1 और Llama 3.2 का अन्वेषण करेंगे 

ये मॉडल्स विभिन्न वेरिएंट्स में आते हैं और GitHub मॉडल मार्केटप्लेस पर उपलब्ध हैं। GitHub मॉडल्स का उपयोग करके [AI मॉडल्स के साथ प्रोटोटाइप बनाने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) पर अधिक विवरण यहां दिए गए हैं।

मॉडल वेरिएंट्स: 
- Llama 3.1 - 70B इंस्ट्रक्ट 
- Llama 3.1 - 405B इंस्ट्रक्ट 
- Llama 3.2 - 11B विज़न इंस्ट्रक्ट 
- Llama 3.2 - 90B विज़न इंस्ट्रक्ट 

*नोट: Llama 3 भी GitHub मॉडल्स पर उपलब्ध है लेकिन इस पाठ में शामिल नहीं किया जाएगा*

## Llama 3.1 

405 बिलियन पैरामीटर्स पर, Llama 3.1 ओपन सोर्स LLM श्रेणी में फिट बैठता है। 

यह मोड पहले रिलीज Llama 3 का अपग्रेड है जो निम्नलिखित प्रदान करता है: 

- बड़ा संदर्भ विंडो - 128k टोकन्स बनाम 8k टोकन्स 
- बड़ा मैक्स आउटपुट टोकन्स - 4096 बनाम 2048 
- बेहतर बहुभाषी समर्थन - प्रशिक्षण टोकन्स में वृद्धि के कारण 

ये Llama 3.1 को GenAI एप्लिकेशन्स बनाने के दौरान अधिक जटिल उपयोग के मामलों को संभालने में सक्षम बनाते हैं, जिनमें शामिल हैं: 
- नेटिव फंक्शन कॉलिंग - LLM वर्कफ़्लो के बाहर बाहरी टूल्स और फंक्शन्स को कॉल करने की क्षमता 
- बेहतर RAG प्रदर्शन - उच्च संदर्भ विंडो के कारण 
- सिंथेटिक डेटा जनरेशन - फाइन-ट्यूनिंग जैसे कार्यों के लिए प्रभावी डेटा बनाने की क्षमता 

### नेटिव फंक्शन कॉलिंग 

Llama 3.1 को फंक्शन या टूल कॉल्स बनाने में अधिक प्रभावी बनाने के लिए फाइन-ट्यून किया गया है। इसमें दो अंतर्निहित टूल्स हैं जिन्हें मॉडल उपयोगकर्ता के प्रॉम्प्ट के आधार पर उपयोग करने की आवश्यकता के रूप में पहचान सकता है। ये टूल्स हैं: 

- **ब्रेव सर्च** - वेब सर्च करके मौसम जैसी अद्यतन जानकारी प्राप्त करने के लिए उपयोग किया जा सकता है 
- **वोल्फ्राम अल्फा** - अधिक जटिल गणितीय गणनाओं के लिए उपयोग किया जा सकता है ताकि आपको अपने स्वयं के फंक्शन्स लिखने की आवश्यकता न हो। 

आप अपने स्वयं के कस्टम टूल्स भी बना सकते हैं जिन्हें LLM कॉल कर सकता है। 

नीचे दिए गए कोड उदाहरण में: 

- हम सिस्टम प्रॉम्प्ट में उपलब्ध टूल्स (brave_search, wolfram_alpha) को परिभाषित करते हैं। 
- एक उपयोगकर्ता प्रॉम्प्ट भेजते हैं जो किसी निश्चित शहर के मौसम के बारे में पूछता है। 
- LLM ब्रेव सर्च टूल के लिए एक टूल कॉल के साथ प्रतिक्रिया देगा जो इस तरह दिखेगा `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*नोट: यह उदाहरण केवल टूल कॉल करता है, यदि आप परिणाम प्राप्त करना चाहते हैं, तो आपको ब्रेव API पेज पर एक मुफ्त खाता बनाना होगा और फंक्शन को स्वयं परिभाषित करना होगा` 

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

हालांकि यह एक LLM है, Llama 3.1 की एक सीमा मल्टीमोडालिटी है। अर्थात, विभिन्न प्रकार के इनपुट जैसे कि इमेजेज का उपयोग प्रॉम्प्ट के रूप में करने और प्रतिक्रियाएं प्रदान करने की क्षमता। यह क्षमता Llama 3.2 की मुख्य विशेषताओं में से एक है। इन विशेषताओं में शामिल हैं: 

- मल्टीमोडालिटी - टेक्स्ट और इमेज प्रॉम्प्ट्स दोनों का मूल्यांकन करने की क्षमता है 
- छोटे से मध्यम आकार के वेरिएंट्स (11B और 90B) - यह लचीले डिप्लॉयमेंट विकल्प प्रदान करता है, 
- केवल टेक्स्ट वेरिएंट्स (1B और 3B) - यह मॉडल को किनारे/मोबाइल डिवाइस पर डिप्लॉय करने की अनुमति देता है और कम विलंबता प्रदान करता है 

मल्टीमोडल समर्थन ओपन सोर्स मॉडल्स की दुनिया में एक बड़ा कदम है। नीचे दिए गए कोड उदाहरण में Llama 3.2 90B से इमेज का विश्लेषण प्राप्त करने के लिए एक इमेज और टेक्स्ट प्रॉम्प्ट दोनों लिया गया है। 

### Llama 3.2 के साथ मल्टीमोडल समर्थन

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

## सीखना यहां समाप्त नहीं होता, यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव AI लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव AI जानकारी को और अधिक बढ़ा सकें!

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में मूल दस्तावेज़ को प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।