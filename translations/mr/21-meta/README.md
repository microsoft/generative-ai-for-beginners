# मेटा कुटुंब मॉडेल्ससह बांधकाम 

## परिचय 

ह्या धड्यात समाविष्ट आहे: 

- दोन प्रमुख मेटा कुटुंब मॉडेल्स - ल्लामा 3.1 आणि ल्लामा 3.2 यांची माहिती 
- प्रत्येक मॉडेलसाठी वापराचे प्रकार आणि परिस्थिती समजून घेणे 
- प्रत्येक मॉडेलच्या वैशिष्ट्यांची ओळख देणारा कोड नमुना 


## मेटा कुटुंबातील मॉडेल्स 

ह्या धड्यात, आपण मेटा कुटुंबातील किंवा "ल्लामा हिरड" मधील 2 मॉडेल्स - л्लामा 3.1 आणि ल्लामा 3.2 यांचा अभ्यास करू. 

हे मॉडेल्स विविध प्रकारांमध्ये उपलब्ध आहेत आणि [मायक्रोसॉफ्ट फाउंड्री मॉडेल्स कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मध्ये सापडतात.

> **टीप:** GitHub Models जुलै 2026 च्या शेवटी बंद होणार आहे. [मायक्रोसॉफ्ट फाउंड्री मॉडेल्स](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) वापरून AI मॉडेल्ससह प्रोटोटाइप कसे तयार करावे याची आणखी माहिती येथे मिळवू शकता.

मॉडेल प्रकार: 
- ल्लामा 3.1 - 70B इंस्ट्रक्ट 
- ल्लामा 3.1 - 405B इंस्ट्रक्ट 
- ल्लामा 3.2 - 11B व्हिजन इंस्ट्रक्ट 
- ल्लामा 3.2 - 90B व्हिजन इंस्ट्रक्ट 

*टीप: ल्लामा 3 मायक्रोसॉफ्ट फाउंड्री मॉडेल्समध्येही उपलब्ध आहे पण ह्या धड्यात त्याचा समावेश नाही*

## ल्लामा 3.1 

405 अब्ज पॅरामीटर्ससह, ल्लामा 3.1 खुले स्रोत LLM वर्गात फिट होते. 

हा मॉडेल पूर्वीच्या ल्लामा 3 च्या आवृत्तीचा सुधारित प्रकार आहे, जे खालीलप्रमाणे आहे: 

- मोठा संदर्भ विंडो - 128k टोकन vs 8k टोकन 
- जास्तीत जास्त आउटपुट टोकन्स - 4096 vs 2048 
- उत्तम बहुभाषिक समर्थन - प्रशिक्षण टोकन्सच्या वाढीमुळे 

हे ल्लामा 3.1 ला अधिक जटिल वापर परिस्थितींना सामना करण्यास सक्षम करतात जे जनरेटिव्ह AI अनुप्रयोग तयार करताना उपयुक्त ठरतात, जसे की: 
- मूळ फंक्शन कॉलिंग - LLM कार्यप्रवाहाबाहेर बाह्य साधने आणि फंक्शन्स कॉल करण्याची क्षमता
- उच्च RAG कार्यक्षमता - मोठ्या संदर्भ विंडोमुळे 
- कृत्रिम डेटा निर्मिती - उदा. फाईन-ट्यूनिंगसाठी प्रभावी डेटा तयार करण्याची क्षमता 

### मूळ फंक्शन कॉलिंग 

ल्लामा 3.1 ला फंक्शन किंवा टूल कॉल्स अधिक प्रभावीपणे करण्यासाठी फाईन-ट्यून केले गेले आहे. यात दोन अंगभूत साधने आहेत जी वापरकर्त्याच्या प्रॉम्प्टनुसार वापरण्यासाठी ओळखली जातात. ही साधने आहेत: 

- **Brave Search** - वेब शोध करून हवामानासारखी अद्ययावत माहिती मिळवण्यासाठी वापरली जाते 
- **Wolfram Alpha** - अधिक जटिल गणिती गणनांसाठी वापरली जाते, म्हणून स्वतःचे फंक्शन्स लिहिण्याची गरज नाही. 

आपण आपल्या स्वतःच्या सानुकूल साधनाही तयार करू शकता ज्यांना LLM कॉल करू शकतो. 

खाली दिलेल्या कोड उदाहरणात: 

- आपण सिस्टम प्रॉम्प्टमध्ये उपलब्ध साधने (brave_search, wolfram_alpha) परिभाषित करतो. 
- एका विशिष्ट शहरातील हवामानाबाबत वापरकर्त्याचा प्रॉम्प्ट पाठवतो. 
- LLM लोकप्रिय साधना Brave Search ला कॉल करेल ज्याचे स्वरूप असे दिसेल `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*टीप: हे उदाहरण फक्त टूल कॉल करते, जर तुम्हाला निकाल हवे असतील तर Brave API पानावर मुक्त खाते तयार करावे लागेल व फंक्शन स्वतः परिभाषित करावे लागेल.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# हे आपला Microsoft Foundry प्रकल्पाच्या "आढावा" पानातून घ्या
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

LLM असूनही, ल्लामा 3.1 ची एक मर्यादा म्हणजे त्यात बहुमाध्यम अभाव आहे. म्हणजे, वेगवेगळ्या प्रकारच्या इनपुटचा वापर, उदा. प्रतिमा प्रॉम्प्ट म्हणून वापरून संवाद देणे शक्य नाही. ही क्षमता ल्लामा 3.2 ची मुख्य वैशिष्ट्ये आहे. ह्या वैशिष्ट्यांमध्ये यांचा समावेश आहे: 

- बहुमाध्यम क्षमता - टेक्स्ट आणि प्रतिमा प्रॉम्प्ट्स दोन्हीचे मूल्यांकन करण्याची क्षमता 
- लहान ते मध्यम आकाराचे प्रकार (11B आणि 90B) - हे विविध तैनाती पर्याय उपलब्ध करतो, 
- फक्त टेक्स्ट प्रकार (1B आणि 3B) - हे मॉडेल एज / मोबाइल डिव्हाइसेसवर तैनात करता येते आणि कमी विलंब प्रदान करते 

बहुमाध्यम समर्थन हे खुले स्रोत मॉडेल्सच्या जगात मोठ्या प्रगतीचे प्रतीक आहे. खालील कोड उदाहरण ल्लामा 3.2 90B कडून प्रतिमा आणि टेक्स्ट प्रॉम्प्ट घेऊन प्रतिमेचे विश्लेषण करते. 


### ल्लामा 3.2 सह बहुमाध्यम समर्थन

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

# हे तुमच्या Microsoft Foundry प्रकल्पाच्या "अवलोकन" पृष्ठावरून मिळवा
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

## शिकणे येथे थांबू नका, प्रवास चालू ठेवा

हा धडा पूर्ण केल्यानंतर, आमची [जनरेटिव्ह AI शिकण्याची संकलन](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पहा आणि तुमचे जनरेटिव्ह AI ज्ञान वाढवत राहा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->