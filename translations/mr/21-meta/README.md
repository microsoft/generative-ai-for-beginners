<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:09:02+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "mr"
}
-->
# Meta कुटुंबातील मॉडेल्ससह बांधकाम 

## परिचय 

या धड्यात आपण कव्हर करू: 

- दोन मुख्य Meta कुटुंबातील मॉडेल्स - Llama 3.1 आणि Llama 3.2 ची शोध 
- प्रत्येक मॉडेलसाठी वापरकेस आणि परिस्थिती समजून घेणे 
- प्रत्येक मॉडेलच्या अनोख्या वैशिष्ट्ये दर्शविण्यासाठी कोड नमुना 


## Meta कुटुंबातील मॉडेल्स 

या धड्यात, आपण Meta कुटुंबातील किंवा "Llama Herd" मधील 2 मॉडेल्स - Llama 3.1 आणि Llama 3.2 ची शोध घेऊ 

हे मॉडेल्स विविध प्रकारांमध्ये उपलब्ध आहेत आणि GitHub Model मार्केटप्लेसवर उपलब्ध आहेत. GitHub Models वापरून [AI मॉडेल्ससह प्रोटोटाइप](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) करण्यासाठी अधिक तपशील येथे आहेत.

मॉडेल प्रकार: 
- Llama 3.1 - 70B निर्देश 
- Llama 3.1 - 405B निर्देश 
- Llama 3.2 - 11B व्हिजन निर्देश 
- Llama 3.2 - 90B व्हिजन निर्देश 

*टीप: Llama 3 GitHub Models वर देखील उपलब्ध आहे पण ते या धड्यात कव्हर केले जाणार नाही*

## Llama 3.1 

405 बिलियन पॅरामीटर्ससह, Llama 3.1 ओपन सोर्स LLM श्रेणीत फिट होते. 

हे मोडेल पूर्वीच्या रिलीज Llama 3 चे अपग्रेड आहे, जे प्रदान करते: 

- मोठे कॉन्टेक्स्ट विंडो - 128k टोकन्स विरुद्ध 8k टोकन्स 
- मोठे मॅक्स आउटपुट टोकन्स - 4096 विरुद्ध 2048 
- अधिक चांगले बहुभाषिक समर्थन - प्रशिक्षण टोकन्सच्या वाढीमुळे 

हे Llama 3.1 ला GenAI अनुप्रयोग तयार करताना अधिक जटिल वापरकेस हाताळण्यास सक्षम करतात, ज्यामध्ये समाविष्ट आहे: 
- नेटिव्ह फंक्शन कॉलिंग - बाह्य साधने आणि फंक्शन्सला LLM कार्यप्रवाहाच्या बाहेर कॉल करण्याची क्षमता 
- चांगली RAG कार्यक्षमता - उच्च कॉन्टेक्स्ट विंडोमुळे 
- सिंथेटिक डेटा जनरेशन - फाइन-ट्यूनिंगसारख्या कार्यांसाठी प्रभावी डेटा तयार करण्याची क्षमता 

### नेटिव्ह फंक्शन कॉलिंग 

Llama 3.1 ला फंक्शन किंवा टूल कॉल्स बनविण्यात अधिक प्रभावी बनवण्यासाठी फाइन-ट्यून केले गेले आहे. त्यात दोन अंगभूत साधने आहेत ज्यांना मॉडेल वापरकर्त्याच्या प्रॉम्प्टवर आधारित वापरले जाणे आवश्यक आहे असे ओळखू शकते. ही साधने आहेत: 

- **Brave Search** - वेब शोध करून हवामानासारखी अद्ययावत माहिती मिळविण्यासाठी वापरली जाऊ शकते 
- **Wolfram Alpha** - अधिक जटिल गणितीय गणनांसाठी वापरली जाऊ शकते त्यामुळे आपले स्वतःचे फंक्शन्स लिहिणे आवश्यक नाही. 

आपण स्वतःची कस्टम साधने देखील तयार करू शकता जी LLM कॉल करू शकते. 

खालील कोड उदाहरणात: 

- आम्ही उपलब्ध साधने (brave_search, wolfram_alpha) सिस्टम प्रॉम्प्टमध्ये परिभाषित करतो. 
- एका विशिष्ट शहरातील हवामानाबद्दल विचारणारा वापरकर्ता प्रॉम्प्ट पाठवतो. 
- LLM Brave Search साधनाला कॉल करून प्रतिसाद देईल ज्याचे असे दिसेल `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*टीप: हे उदाहरण फक्त टूल कॉल करते, जर आपण परिणाम मिळवू इच्छित असाल तर, आपण Brave API पृष्ठावर एक मोफत खाते तयार करणे आणि फंक्शन स्वतः परिभाषित करणे आवश्यक आहे` 

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

एक LLM असूनही, Llama 3.1 ची एक मर्यादा आहे ती म्हणजे मल्टीमोडालिटी. म्हणजेच, प्रतिमा सारख्या विविध प्रकारच्या इनपुटचा प्रॉम्प्ट म्हणून वापर करण्याची आणि प्रतिसाद देण्याची क्षमता. ही क्षमता Llama 3.2 ची मुख्य वैशिष्ट्यांपैकी एक आहे. या वैशिष्ट्यांमध्ये समाविष्ट आहे: 

- मल्टीमोडालिटी - मजकूर आणि प्रतिमा प्रॉम्प्ट्स दोन्हीचे मूल्यांकन करण्याची क्षमता आहे 
- लहान ते मध्यम आकाराचे प्रकार (11B आणि 90B) - हे लवचिक वितरण पर्याय प्रदान करते, 
- फक्त मजकूर प्रकार (1B आणि 3B) - हे मॉडेलला एज / मोबाइल उपकरणांवर वितरित करण्याची परवानगी देते आणि कमी विलंब प्रदान करते 

मल्टीमोडल समर्थन ओपन सोर्स मॉडेल्सच्या जगात एक मोठे पाऊल दर्शवते. खालील कोड उदाहरण प्रतिमा आणि मजकूर प्रॉम्प्ट दोन्ही घेतो आणि Llama 3.2 90B कडून प्रतिमेचे विश्लेषण मिळवतो. 


### Llama 3.2 सह मल्टीमोडल समर्थन

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

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) वर जा आणि आपल्या Generative AI ज्ञानाचे स्तर वाढवा!

**अस्वीकृती**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अशुद्धता असू शकतात. मूळ भाषेतील मूळ दस्तऐवज अधिकृत स्रोत मानला जावा. महत्त्वपूर्ण माहितीसाठी, व्यावसायिक मानव भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.