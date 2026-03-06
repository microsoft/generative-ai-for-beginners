# मेटा फैमिली मॉडल्स के साथ बिल्डिंग

## परिचय

इस पाठ में हम कवर करेंगे:

- दो मुख्य मेटा फैमिली मॉडल्स - ल्लामा 3.1 और ल्लामा 3.2 का अन्वेषण
- प्रत्येक मॉडल के उपयोग के मामलों और परिदृश्यों को समझना
- प्रत्येक मॉडल की अनूठी विशेषताओं को दिखाने के लिए कोड उदाहरण

## मेटा फैमिली ऑफ मॉडल्स

इस पाठ में, हम मेटा फैमिली या "ल्लामा हर्ड" के 2 मॉडल्स का अन्वेषण करेंगे - ल्लामा 3.1 और ल्लामा 3.2।

ये मॉडल विभिन्न प्रकारों में उपलब्ध हैं और GitHub मॉडल मार्केटप्लेस पर उपलब्ध हैं। GitHub मॉडल्स का उपयोग कर [एआई मॉडल्स के साथ प्रोटोटाइपिंग](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) के बारे में अधिक जानकारी यहां है।

मॉडल वैरिएंट्स:
- ल्लामा 3.1 - 70B इंस्ट्रकट
- ल्लामा 3.1 - 405B इंस्ट्रकट
- ल्लामा 3.2 - 11B विजन इंस्ट्रकट
- ल्लामा 3.2 - 90B विजन इंस्ट्रकट

*ध्यान दें: ल्लामा 3 भी GitHub मॉडल्स पर उपलब्ध है लेकिन इसे इस पाठ में शामिल नहीं किया जाएगा*

## ल्लामा 3.1

405 बिलियन पैरामीटर्स के साथ, ल्लामा 3.1 ओपन सोर्स LLM श्रेणी में आता है।

यह मॉडल पूर्व रिलीज़ ल्लामा 3 का अपग्रेड है और यह प्रदान करता है:

- बड़ा कॉन्टेक्स्ट विंडो - 128k टोकन बनाम 8k टोकन
- बड़ा मैक्स आउटपुट टोकन - 4096 बनाम 2048
- बेहतर बहुभाषी समर्थन - प्रशिक्षण टोकन में वृद्धि के कारण

ये ल्लामा 3.1 को जेनएआई एप्लिकेशन बनाने के दौरान अधिक जटिल उपयोग मामलों को संभालने में सक्षम बनाते हैं, जिसमें शामिल हैं:
- नेटिव फंक्शन कॉलिंग - LLM वर्कफ़्लो के बाहर बाहरी टूल्स और फंक्शंस को कॉल करने की क्षमता
- बेहतर RAG प्रदर्शन - उच्च कॉन्टेक्स्ट विंडो के कारण
- सिंथेटिक डेटा जेनरेशन - फाइन-ट्युनिंग जैसे कार्यों के लिए प्रभावी डेटा बनाने की क्षमता

### नेटिव फंक्शन कॉलिंग

ल्लामा 3.1 को फंक्शन या टूल कॉल करने में अधिक प्रभावी बनाने के लिए फाइन-ट्यून किया गया है। इसमें दो इन-बिल्ट टूल्स भी हैं जिन्हें मॉडल यूजर के प्रॉम्प्ट के आधार पर उपयोग करने के लिए पहचान सकता है। ये टूल्स हैं:

- **ब्रेव सर्च** - वेब सर्च करके मौसम जैसी अद्यतित जानकारी प्राप्त करने के लिए उपयोग किया जा सकता है
- **वोल्फ्राम अल्फा** - अधिक जटिल गणितीय गणनाओं के लिए उपयोग किया जाता है, इसलिए अपनी खुद की गणनाएँ लिखने की आवश्यकता नहीं है।

आप अपने स्वयं के कस्टम टूल्स भी बना सकते हैं जिन्हें LLM कॉल कर सकता है।

नीचे कोड उदाहरण में:

- हम सिस्टम प्रॉम्प्ट में उपलब्ध टूल्स (brave_search, wolfram_alpha) को परिभाषित करते हैं।
- एक यूजर प्रॉम्प्ट भेजा जाता है जिसमें किसी शहर के मौसम के बारे में पूछा जाता है।
- LLM एक टूल कॉल के साथ उत्तर देगा जो इस प्रकार दिखेगा `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ध्यान दें: यह उदाहरण केवल टूल कॉल करता है, यदि आप परिणाम प्राप्त करना चाहते हैं, तो आपको ब्रेव API पेज पर एक मुफ्त खाता बनाना होगा और फंक्शन को परिभाषित करना होगा।*

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

## ल्लामा 3.2

LLM होने के बावजूद, ल्लामा 3.1 की एक सीमा इसका मल्टीमॉडलिटी का अभाव है। अर्थात, यह विभिन्न प्रकार के इनपुट जैसे कि छवियों को प्रॉम्प्ट के रूप में उपयोग करने और उत्तर प्रदान करने में सक्षम नहीं है। यह क्षमता ल्लामा 3.2 की मुख्य विशेषताओं में से एक है। इन विशेषताओं में शामिल हैं:

- मल्टीमॉडलिटी - टेक्स्ट और इमेज दोनों प्रॉम्प्ट का मूल्यांकन करने की क्षमता
- छोटे से मध्यम आकार के वैरिएंट (11B और 90B) - यह लचीली तैनाती विकल्प प्रदान करता है,
- केवल टेक्स्ट वैरिएंट (1B और 3B) - यह मॉडल को एज / मोबाइल डिवाइसों पर तैनात करने की अनुमति देता है और कम विलंबता प्रदान करता है

मल्टीमॉडल सपोर्ट ओपन सोर्स मॉडल्स की दुनिया में एक बड़ा कदम दर्शाता है। नीचे कोड उदाहरण में ल्लामा 3.2 90B से एक छवि और टेक्स्ट दोनों प्रॉम्प्ट लेकर छवि का विश्लेषण प्राप्त किया जाता है।

### ल्लामा 3.2 के साथ मल्टीमॉडल सपोर्ट

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

इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव एआई लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव एआई ज्ञान को और बढ़ा सकें!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। यद्यपि हम सटीकता के लिए प्रयासरत हैं, कृपया यह समझें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में उपलब्ध दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->