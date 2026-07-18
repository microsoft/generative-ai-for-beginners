# मेटा फॅमिली मॉडेल्ससह बिल्डिंग 

## परिचय 

हा धडा यावर आधारित आहे: 

- दोन मुख्य मेटा फॅमिली मॉडेल्सची ओळख - ल्लामा 3.1 आणि ल्लामा 3.2 
- प्रत्येक मॉडेलसाठी वापर प्रकरणे आणि परिस्थिती समजून घेणे 
- प्रत्येक मॉडेलच्या वैशिष्ट्यांचे कोड नमुना दाखवणे 


## मेटा फॅमिली ऑफ मॉडेल्स 

या धड्यात, आपण मेटा कुटुंबातील किंवा "ल्लामा संघटनेतील" 2 मॉडेल्स - ल्लामा 3.1 आणि ल्लामा 3.2 यांचा अभ्यास करू.

हे मॉडेल्स विविध प्रकारांमध्ये उपलब्ध आहेत आणि [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मध्ये सापडतात.

> **टीप:** GitHub Models ही सेवा जुलै 2026 च्या शेवटी बंद होणार आहे. येथे [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) वापरत AI मॉडेल्ससह प्रोटोटाइप कसे तयार करावे याचे अधिक तपशील दिले आहेत.

मॉडेल प्रकार: 
- ल्लामा 3.1 - 70B इंस्ट्रक्ट 
- ल्लामा 3.1 - 405B इंस्ट्रक्ट 
- ल्लामा 3.2 - 11B व्हिजन इंस्ट्रक्ट 
- ल्लामा 3.2 - 90B व्हिजन इंस्ट्रक्ट 

*टीप: ल्लामा 3 ही Microsoft Foundry Models मध्ये उपलब्ध आहे परंतु या धड्यात याचा समावेश नाही*

## ल्लामा 3.1 

405 अब्ज पॅरामीटर्ससह, ल्लामा 3.1 ओपन सोर्स LLM श्रेणीत येते. 

हे मॉडेल पूर्वीच्या ल्लामा 3 च्या तुलनेत सुधारित आहे आणि खालील गोष्टींची ऑफर देते: 

- मोठा संदर्भ विंडो - 128k टोकन्स विरुद्ध 8k टोकन्स 
- मोठे कमाल आउटपुट टोकन्स - 4096 विरुद्ध 2048 
- चांगले बहुभाषिक समर्थन - प्रशिक्षण टोकन्सच्या वाढीमुळे 

हे ल्लामा 3.1 ला अधिक कॉम्प्लेक्स वापर प्रकरणे हाताळण्यासाठी सक्षम करतात, ज्यामध्ये समाविष्ट आहे: 
- नॅटिव्ह फंक्शन कॉलिंग - LLM वर्कफ्लोच्या बाहेर बाह्य साधने आणि फंक्शन्स कॉल करण्याची क्षमता
- चांगली RAG कामगिरी - उच्च संदर्भ विंडोमुळे 
- संश्लेषित डेटा निर्मिती - कार्यांसाठी प्रभावी डेटा तयार करण्याची क्षमता जसे की फाईन-ट्युनिकिंग 

### नॅटिव्ह फंक्शन कॉलिंग 

ल्लामा 3.1 अधिक प्रभावी फंक्शन किंवा टूल कॉल करण्यासाठी फाइन-ट्यून करण्यात आला आहे. त्यामध्ये दोन अंगभूत साधने आहेत जी मॉडेल वापरकर्त्याच्या प्रॉम्प्टच्या आधारावर वापरायची गरज ओळखू शकते. ही साधने आहेत: 

- **Brave Search** - वेब सर्च करून हवामानासारखी अद्ययावत माहिती मिळवण्यासाठी वापरता येते 
- **Wolfram Alpha** - अधिक कॉम्प्लेक्स गणितीय गणनांसाठी वापरली जाऊ शकते त्यामुळे स्वतःचे फंक्शन्स लिहिण्याची गरज नाही. 

तुम्ही स्वतःची सानुकूल साधने देखील तयार करू शकता जी LLM कॉल करू शकते. 

खालील कोड उदाहरणात: 

- आम्ही सिस्टम प्रॉम्प्टमध्ये उपलब्ध साधने (brave_search, wolfram_alpha) परिभाषित करतो. 
- वापरकर्त्याकडून एका विशिष्ट शहरातील हवामानाबाबत विचारणा करणारा प्रॉम्प्ट पाठवतो. 
- LLM Brave Search साधनाला कॉल करेल जे असे दिसेल `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*टीप: हा उदाहरण केवळ साधन कॉल करतो, जर तुम्हाला निकाल हवे असतील तर तुम्हाला Brave API पेजवर एक मोफत खाते तयार करावे लागेल आणि फंक्शन स्वतः परिभाषित करावे लागेल.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# आपल्या Microsoft Foundry प्रोजेक्टच्या "अवलोकन" पृष्ठावरून हे मिळवा
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

## ल्लामा 3.2 

LLM असतानाही, ल्लामा 3.1 ची एक मर्यादा म्हणजे मल्टीमॉडॅलिटीचा अभाव. म्हणजे, वेगवेगळ्या इनपुट प्रकारांचा उपयोग करू न शकणे जसे की प्रतिमा प्रॉम्प्ट म्हणून आणि त्यानुसार प्रतिसाद देणे. ही क्षमता ल्लामा 3.2 ची मुख्य वैशिष्ट्ये आहेत. या वैशिष्ट्यांमध्ये समाविष्ट आहेत: 

- मल्टीमॉडॅलिटी - दोन्ही टेक्स्ट आणि प्रतिमा प्रॉम्प्टचे मूल्यांकन करण्याची क्षमता 
- लहान ते मध्यम आकाराचे प्रकार (11B आणि 90B) - यामुळे लवचिक डिप्लॉयमेंट पर्याय उपलब्ध आहेत, 
- फक्त टेक्स्ट प्रकार (1B आणि 3B) - यामुळे मॉडेल एज / मोबाइल उपकरणांवर डिप्लॉय केले जाऊ शकते आणि कमी विलंब प्रदान करतो 

मल्टीमॉडॅल समर्थन हे ओपन सोर्स मॉडेल्सच्या जगात मोठा टप्पा आहे. खालील कोड उदाहरण ल्लामा 3.2 90B कडून प्रतिमेचे विश्लेषण मिळवण्यासाठी प्रतिमा आणि टेक्स्ट प्रॉम्प्ट दोन्ही घेते. 


### ल्लामा 3.2 सह मल्टीमॉडॅल समर्थन

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

# आपल्या Microsoft Foundry प्रकल्पाच्या "आढावा" पानावरून हे मिळवा
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

## शिक्षण येथे थांबत नाही, प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) चे दर्शन करून तुमचे जेनेरेटीव्ह AI ज्ञान वाढवत राहा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->