# मेटा फॅमिली मॉडेल्ससह बिल्डिंग

## परिचय

या धड्यांत आपण यावर चर्चा करू:

- दोन मुख्य मेटा फॅमिली मॉडेल्स - लामा ३.१ आणि लामा ३.२ यांचा शोध घेणे
- प्रत्येक मॉडेलसाठी वापर प्रकरणे आणि परिस्थिती समजून घेणे
- प्रत्येक मॉडेलच्या वैशिष्ट्यांचे प्रदर्शन करणारा कोड नमुना

## मेटा फॅमिली ऑफ मॉडेल्स

या धड्यात आपण मेटा कुटुंबातील किंवा "लामा हरड" मधील २ मॉडेल्स - लामा ३.१ आणि लामा ३.२ यांचा शोध घेणार आहोत.

हे मॉडेल्स वेगवेगळ्या व्हेरियंट्समध्ये येतात आणि GitHub मॉडेल मार्केटप्लेसवर उपलब्ध आहेत. GitHub मॉडेल्स वापरून [AI मॉडेल्ससह प्रोटोटायपिंग](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) कसे करायचे याची अधिक माहिती खाली दिली आहे.

मॉडेल व्हेरियंट्स:
- लामा ३.१ - ७०B इन्स्ट्रक्ट
- लामा ३.१ - ४०५B इन्स्ट्रक्ट
- लामा ३.२ - ११B व्हिजन इन्स्ट्रक्ट
- लामा ३.२ - ९०B व्हिजन इन्स्ट्रक्ट

*टीप: लामा ३ देखील GitHub मॉडेल्सवर उपलब्ध आहे परंतु या धड्यात त्यावर चर्चा होणार नाही.*

## लामा ३.१

४०५ अब्ज पॅरामीटर्ससह, लामा ३.१ खुल्या स्रोतातील LLM वर्गात येतो.

हे मॉडेल पूर्वीच्या लामा ३ रिलीजचे उन्नत रूप आहे जे खालील बाबतीत सुधारणा करते:

- मोठा संदर्भ विंडो - १२८k टोकन्स विरुद्ध ८k टोकन्स
- जास्तीत जास्त आउटपुट टोकन्स - ४०९६ विरुद्ध २०४८
- चांगले बहुभाषिक समर्थन - प्रशिक्षण टोकन्सच्या वाढीमुळे

हे लामा ३.१ ला अधिक क्लिष्ट वापर प्रकरणे हाताळण्यास सक्षम करतात, जे GenAI ऍप्लिकेशन्स तयार करताना उपयुक्त आहेत जसे की:
- नैसर्गिक फंक्शन कॉलिंग - LLM कार्यप्रवाहाच्या बाहेर बाह्य टूल्स आणि फंक्शन्स कॉल करण्याची क्षमता
- चांगली RAG कामगिरी - मोठ्या संदर्भ विंडोमुळे
- सिंथेटिक डेटा जनरेशन - सूक्ष्म-सुधारणा सारख्या कामांसाठी प्रभावी डेटा तयार करण्याची क्षमता

### नैसर्गिक फंक्शन कॉलिंग

लामा ३.१ फंक्शन किंवा टूल कॉल करताना अधिक प्रभावी व्हावे यासाठी फाइन-ट्युन केलेले आहे. यामध्ये दोन अंगभूत टूल्स आहेत ज्यांना वापरकर्त्याच्या प्रॉम्प्टवरून वापरण्याची गरज ओळखता येते. हे टूल्स आहेत:

- **Brave Search** - वेब शोध करून हवामान वगैरे अद्ययावत माहिती मिळवण्यास वापरू शकतो
- **Wolfram Alpha** - अधिक जटिल गणितीय गणनेसाठी वापरले जाऊ शकते त्यामुळे स्वतः फंक्शन्स लिहिण्याची गरज नाही

तुम्ही स्वतःचे कस्टम टूल्स देखील तयार करू शकता जे LLM कॉल करू शकतो.

खालील कोड उदाहरणात:

- आपण प्रणाली प्रॉम्प्टमध्ये उपलब्ध टूल्स (brave_search, wolfram_alpha) परिभाषित करतो.
- वापरकर्त्याचा प्रॉम्प्ट पाठवतो जो एखाद्या शहरातील हवामानाबद्दल विचारतो.
- LLM नवीन कॉल म्हणून Brave Search टूलला प्रतिसाद देईल, जे असे दिसेल `<|python_tag|>brave_search.call(query="Stockholm weather")`

*टीप: हा उदाहरण फक्त टूल कॉल करतो, जर तुम्हाला परिणाम मिळवायचा असेल तर Brave API पृष्ठावर मुक्त खाते तयार करावे लागेल आणि फंक्शन स्वतः परिभाषित करावे लागेल.*

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

LLM असूनही, लामा ३.१ चा एक मर्यादा म्हणजे त्यात मल्टीमॉडॅलिटीचा अभाव आहे. म्हणजे, इमेजसारख्या वेगवेगळ्या प्रकारच्या इनपुटचा वापर करून प्रॉम्प्ट देणे आणि त्यावर प्रतिसाद देणे शक्य नाही. ही क्षमता लामा ३.२ ची मुख्य वैशिष्ट्ये आहेत. यामध्ये पुढील वैशिष्ट्ये देखील आहेत:

- मल्टीमॉडॅलिटी - टेक्स्ट आणि इमेज प्रॉम्प्ट्स दोन्हीचे मूल्यमापन करण्याची क्षमता
- लहान ते मध्यम आकाराचे व्हेरियंट्स (११B आणि ९०B) - लवचिक तैनाती पर्याय प्रदान करतात,
- टेक्स्ट-फक्त व्हेरियंट्स (१B आणि ३B) - या मॉडेलला एज / मोबाइल डिव्हाइसेसवर तैनात करता येते आणि कमी विलंब प्रदान करते

मल्टीमॉडल समर्थन हे खुले स्रोत मॉडेल्सच्या विश्वात मोठा टप्पा आहे. खालील कोड उदाहरण लामा ३.२ ९०B कडून चित्राचे विश्लेषण मिळवण्यासाठी इमेज आणि टेक्स्ट प्रॉम्प्ट दोन्ही वापरते.

### लामा ३.२ सोबत मल्टीमॉडॅल समर्थन

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

## शिक्षण येथे थांबत नाही, प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला भेट द्या आणि तुमचे Generative AI ज्ञान अधिक विकसित करा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सूचना**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी भाषांतर शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणार्‍या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावणीसाठी आम्ही जबाबदार नाही आहोत.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->