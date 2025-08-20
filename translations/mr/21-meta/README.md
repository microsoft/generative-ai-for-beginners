<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:08:22+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "mr"
}
-->
# Meta कुटुंब मॉडेल्ससह बांधकाम

## परिचय

या धड्यात आपण खालील गोष्टी पाहणार आहोत:

- दोन मुख्य Meta कुटुंब मॉडेल्स - Llama 3.1 आणि Llama 3.2 यांचा अभ्यास
- प्रत्येक मॉडेलसाठी वापराचे प्रकार आणि परिस्थिती समजून घेणे
- प्रत्येक मॉडेलच्या खास वैशिष्ट्यांचे प्रदर्शन करणारा कोड नमुना

## Meta कुटुंबातील मॉडेल्स

या धड्यात आपण Meta कुटुंबातील किंवा "Llama Herd" मधील 2 मॉडेल्स - Llama 3.1 आणि Llama 3.2 यांचा अभ्यास करू.

हे मॉडेल्स विविध प्रकारांमध्ये उपलब्ध आहेत आणि GitHub Model मार्केटप्लेसवर मिळतात. GitHub Models वापरून [AI मॉडेल्ससह प्रोटोटायपिंग](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) कसे करायचे याबाबत अधिक माहिती येथे आहे.

मॉडेल प्रकार:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*टीप: Llama 3 देखील GitHub Models वर उपलब्ध आहे पण या धड्यात त्याचा समावेश नाही*

## Llama 3.1

405 अब्ज पॅरामीटर्ससह, Llama 3.1 हे ओपन सोर्स LLM श्रेणीत येते.

हे मॉडेल पूर्वीच्या Llama 3 च्या तुलनेत सुधारित आहे आणि खालील सुविधा देते:

- मोठा संदर्भ विंडो - 128k टोकन्स विरुद्ध 8k टोकन्स
- जास्तीत जास्त आउटपुट टोकन्स - 4096 विरुद्ध 2048
- सुधारित बहुभाषिक समर्थन - प्रशिक्षण टोकन्सच्या वाढीमुळे

हे Llama 3.1 ला अधिक गुंतागुंतीच्या वापराच्या प्रकरणांमध्ये GenAI अ‍ॅप्लिकेशन्स तयार करताना सक्षम बनवते, जसे की:
- नेटिव फंक्शन कॉलिंग - LLM वर्कफ्लोच्या बाहेर असलेल्या बाह्य टूल्स आणि फंक्शन्स कॉल करण्याची क्षमता
- सुधारित RAG कामगिरी - मोठ्या संदर्भ विंडोमुळे
- सिंथेटिक डेटा जनरेशन - फाइन-ट्यूनिंगसारख्या कामांसाठी प्रभावी डेटा तयार करण्याची क्षमता

### नेटिव फंक्शन कॉलिंग

Llama 3.1 ला फंक्शन किंवा टूल कॉल करण्यासाठी अधिक प्रभावी बनवण्यासाठी फाइन-ट्यून केले गेले आहे. यामध्ये दोन अंगभूत टूल्स आहेत जे मॉडेल वापरकर्त्याच्या प्रॉम्प्टनुसार वापरावयाचे असल्याचे ओळखू शकते. ही टूल्स आहेत:

- **Brave Search** - वेब शोध करून हवामानासारखी अद्ययावत माहिती मिळवण्यासाठी वापरली जाते
- **Wolfram Alpha** - अधिक गुंतागुंतीच्या गणिती गणनांसाठी वापरली जाते, ज्यामुळे स्वतःचे फंक्शन्स लिहिण्याची गरज नाही

तुम्ही तुमचे स्वतःचे कस्टम टूल्स देखील तयार करू शकता जे LLM कॉल करू शकते.

खालील कोड उदाहरणात:

- आपण उपलब्ध टूल्स (brave_search, wolfram_alpha) सिस्टम प्रॉम्प्टमध्ये परिभाषित करतो.
- वापरकर्त्याचा प्रॉम्प्ट पाठवतो जो एखाद्या शहरातील हवामानाबद्दल विचारतो.
- LLM Brave Search टूल कॉलसह प्रतिसाद देईल, जे असे दिसेल `<|python_tag|>brave_search.call(query="Stockholm weather")`

*टीप: हे उदाहरण फक्त टूल कॉल करते, जर तुम्हाला निकाल हवे असतील तर Brave API पेजवर मोफत खाते तयार करावे लागेल आणि फंक्शन स्वतः परिभाषित करावे लागेल*

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

LLM असतानाही, Llama 3.1 मध्ये एक मर्यादा म्हणजे मल्टीमॉडॅलिटी. म्हणजे, वेगवेगळ्या प्रकारच्या इनपुट्स जसे की प्रतिमा प्रॉम्प्ट म्हणून वापरणे आणि त्यावर प्रतिसाद देणे. ही क्षमता Llama 3.2 ची मुख्य वैशिष्ट्ये आहेत. यामध्ये खालील गोष्टीही आहेत:

- मल्टीमॉडॅलिटी - टेक्स्ट आणि इमेज प्रॉम्प्ट दोन्हीचे मूल्यांकन करण्याची क्षमता
- लहान ते मध्यम आकाराचे प्रकार (11B आणि 90B) - लवचिक तैनातीसाठी पर्याय
- फक्त टेक्स्ट प्रकार (1B आणि 3B) - हे मॉडेल एज/मोबाईल डिव्हाइसेसवर तैनात करता येते आणि कमी विलंब प्रदान करते

मल्टीमॉडॅल समर्थन हे ओपन सोर्स मॉडेल्सच्या जगात मोठा टप्पा आहे. खालील कोड उदाहरण Llama 3.2 90B कडून प्रतिमा आणि टेक्स्ट प्रॉम्प्ट दोन्ही घेऊन प्रतिमेचे विश्लेषण करते.

### Llama 3.2 सह मल्टीमॉडॅल समर्थन

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

## शिकणे येथे थांबत नाही, प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला भेट द्या आणि तुमचे Generative AI ज्ञान अधिक वाढवा!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.