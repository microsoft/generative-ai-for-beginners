<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:28:53+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "mr"
}
-->
# Meta कुटुंबाच्या मॉडेल्ससह बांधकाम 

## परिचय 

या धड्यात आपण कव्हर करू: 

- दोन मुख्य Meta कुटुंब मॉडेल्स - Llama 3.1 आणि Llama 3.2 ची तपासणी 
- प्रत्येक मॉडेलसाठी उपयोग-केसेस आणि परिस्थिती समजून घेणे 
- प्रत्येक मॉडेलच्या अनोख्या वैशिष्ट्ये दाखवण्यासाठी कोड नमुना 


## Meta कुटुंब मॉडेल्स 

या धड्यात, आम्ही Meta कुटुंब किंवा "Llama Herd" मधील 2 मॉडेल्स - Llama 3.1 आणि Llama 3.2 तपासणार आहोत 

हे मॉडेल्स विविध प्रकारांमध्ये येतात आणि GitHub मॉडेल मार्केटप्लेसवर उपलब्ध आहेत. GitHub मॉडेल्स वापरून [AI मॉडेल्ससह प्रोटोटायपिंग](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) करण्याच्या अधिक तपशीलांसाठी येथे पहा.

मॉडेल प्रकार: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*टीप: Llama 3 देखील GitHub मॉडेल्सवर उपलब्ध आहे परंतु या धड्यात कव्हर केले जाणार नाही*

## Llama 3.1 

405 अब्ज पॅरामीटर्ससह, Llama 3.1 खुल्या स्रोत LLM श्रेणीमध्ये बसतो. 

मोडेल पूर्वीच्या Llama 3 रिलीजमध्ये अपग्रेड आहे आणि हे देते: 

- मोठे संदर्भ विंडो - 128k टोकन्स vs 8k टोकन्स 
- मोठे Max Output Tokens - 4096 vs 2048 
- उत्तम बहुभाषिक समर्थन - प्रशिक्षण टोकन्सच्या वाढीमुळे 

हे Llama 3.1 ला अधिक जटिल उपयोग केसेस हाताळण्यास सक्षम करते जेव्हा GenAI अनुप्रयोग तयार करणे समाविष्ट आहे: 
- नेटिव फंक्शन कॉलिंग - बाह्य साधने आणि फंक्शन्स LLM वर्कफ्लोच्या बाहेर कॉल करण्याची क्षमता 
- उत्तम RAG कामगिरी - उच्च संदर्भ विंडोमुळे 
- सिंथेटिक डेटा जनरेशन - फाइन-ट्यूनिंग सारख्या कार्यांसाठी प्रभावी डेटा तयार करण्याची क्षमता 

### नेटिव फंक्शन कॉलिंग 

Llama 3.1 ला फंक्शन किंवा टूल कॉल्स अधिक प्रभावी बनवण्यासाठी फाइन-ट्यून केले गेले आहे. यात दोन अंगभूत साधने आहेत ज्यांना मॉडेल ओळखू शकते की वापरकर्त्याच्या प्रॉम्प्टवर आधारित वापरण्याची आवश्यकता आहे. ही साधने आहेत: 

- **Brave Search** - वेब शोध करून हवामानासारखी अद्ययावत माहिती मिळवण्यासाठी वापरली जाऊ शकते 
- **Wolfram Alpha** - अधिक जटिल गणितीय गणनांसाठी वापरली जाऊ शकते जेणेकरून स्वतःचे फंक्शन्स लिहिण्याची आवश्यकता नाही. 

आपण स्वतःची सानुकूल साधने देखील तयार करू शकता जी LLM कॉल करू शकते. 

खालील कोड उदाहरणात: 

- आम्ही सिस्टम प्रॉम्प्टमध्ये उपलब्ध साधने (brave_search, wolfram_alpha) परिभाषित करतो. 
- एका विशिष्ट शहरातील हवामानाबद्दल विचारणारा वापरकर्ता प्रॉम्प्ट पाठवा. 
- LLM Brave Search साधनाला कॉल करून प्रतिसाद देईल ज्याचा स्वरूप असा दिसेल `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*टीप: हे उदाहरण फक्त साधन कॉल करते, जर तुम्हाला परिणाम मिळवायचे असतील, तर तुम्हाला Brave API पृष्ठावर एक मोफत खाते तयार करावे लागेल आणि फंक्शन स्वतः परिभाषित करावे लागेल*

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

एक LLM असूनही, Llama 3.1 मध्ये मल्टीमोडॅलिटी ही एक मर्यादा आहे. म्हणजे, प्रतिमा प्रॉम्प्ट्स सारख्या विविध प्रकारच्या इनपुटचा वापर करण्याची आणि प्रतिसाद प्रदान करण्याची क्षमता. ही क्षमता Llama 3.2 च्या मुख्य वैशिष्ट्यांपैकी एक आहे. या वैशिष्ट्यांमध्ये हे देखील समाविष्ट आहे: 

- मल्टीमोडॅलिटी - मजकूर आणि प्रतिमा प्रॉम्प्ट्स दोन्हीचे मूल्यांकन करण्याची क्षमता आहे 
- लहान ते मध्यम आकाराचे प्रकार (11B आणि 90B) - हे लवचिक वितरण पर्याय प्रदान करते, 
- फक्त मजकूर प्रकार (1B आणि 3B) - हे मॉडेलला एज / मोबाइल डिव्हाइसवर वितरित करण्यास आणि कमी विलंब प्रदान करण्यास अनुमती देते 

मल्टीमोडल समर्थन हे ओपन सोर्स मॉडेल्सच्या जगात एक मोठे पाऊल आहे. खालील कोड उदाहरण प्रतिमा आणि मजकूर प्रॉम्प्ट दोन्ही घेते जेणेकरून Llama 3.2 90B कडून प्रतिमेचे विश्लेषण मिळेल.


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

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला तपासा जेणेकरून आपल्या Generative AI ज्ञानाला पुढे वाढवू शकता!

**अस्वीकृती:**
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अपूर्णता असू शकतात. मूळ भाषेतील दस्तऐवज अधिकृत स्रोत मानला पाहिजे. महत्त्वपूर्ण माहिती साठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.