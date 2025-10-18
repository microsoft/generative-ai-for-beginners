<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-18T00:11:08+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "hi"
}
-->
# फ़ंक्शन कॉलिंग के साथ एकीकरण

[![फ़ंक्शन कॉलिंग के साथ एकीकरण](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.hi.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

आपने पिछले पाठों में अब तक काफी कुछ सीखा है। हालांकि, हम इसे और बेहतर बना सकते हैं। कुछ चीजें जिन्हें हम संबोधित कर सकते हैं, वे हैं कि हम प्रतिक्रिया प्रारूप को अधिक सुसंगत कैसे बना सकते हैं ताकि प्रतिक्रिया को आगे काम करना आसान हो। साथ ही, हम अपनी एप्लिकेशन को और समृद्ध करने के लिए अन्य स्रोतों से डेटा जोड़ना चाह सकते हैं।

उपरोक्त उल्लिखित समस्याएं इस अध्याय में संबोधित की जा रही हैं।

## परिचय

इस पाठ में शामिल होगा:

- फ़ंक्शन कॉलिंग क्या है और इसके उपयोग के मामले समझाना।
- Azure OpenAI का उपयोग करके फ़ंक्शन कॉल बनाना।
- एप्लिकेशन में फ़ंक्शन कॉल को एकीकृत कैसे करें।

## सीखने के लक्ष्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- फ़ंक्शन कॉलिंग का उपयोग करने का उद्देश्य समझाना।
- Azure OpenAI सेवा का उपयोग करके फ़ंक्शन कॉल सेटअप करना।
- अपने एप्लिकेशन के उपयोग के मामले के लिए प्रभावी फ़ंक्शन कॉल डिज़ाइन करना।

## परिदृश्य: हमारे चैटबॉट को फ़ंक्शंस के साथ सुधारना

इस पाठ के लिए, हम अपनी शिक्षा स्टार्टअप के लिए एक फीचर बनाना चाहते हैं जो उपयोगकर्ताओं को तकनीकी पाठ्यक्रम खोजने के लिए चैटबॉट का उपयोग करने की अनुमति देता है। हम उनके कौशल स्तर, वर्तमान भूमिका और रुचि की तकनीक के अनुसार पाठ्यक्रमों की सिफारिश करेंगे।

इस परिदृश्य को पूरा करने के लिए, हम निम्नलिखित का संयोजन उपयोग करेंगे:

- `Azure OpenAI` उपयोगकर्ता के लिए चैट अनुभव बनाने के लिए।
- `Microsoft Learn Catalog API` उपयोगकर्ताओं को उनके अनुरोध के आधार पर पाठ्यक्रम खोजने में मदद करने के लिए।
- `Function Calling` उपयोगकर्ता की क्वेरी को लेने और इसे API अनुरोध करने के लिए एक फ़ंक्शन को भेजने के लिए।

शुरू करने के लिए, आइए देखें कि हम पहले स्थान पर फ़ंक्शन कॉलिंग का उपयोग क्यों करना चाहेंगे:

## फ़ंक्शन कॉलिंग क्यों

फ़ंक्शन कॉलिंग से पहले, LLM से प्रतिक्रियाएं असंरचित और असंगत थीं। डेवलपर्स को यह सुनिश्चित करने के लिए जटिल सत्यापन कोड लिखने की आवश्यकता थी कि वे प्रतिक्रिया के प्रत्येक भिन्नता को संभाल सकें। उपयोगकर्ता "स्टॉकहोम में वर्तमान मौसम क्या है?" जैसे उत्तर प्राप्त नहीं कर सकते थे। ऐसा इसलिए है क्योंकि मॉडल उस समय तक सीमित थे जब डेटा प्रशिक्षित किया गया था।

Azure OpenAI सेवा की फ़ंक्शन कॉलिंग निम्नलिखित सीमाओं को दूर करने के लिए एक सुविधा है:

- **सुसंगत प्रतिक्रिया प्रारूप**। यदि हम प्रतिक्रिया प्रारूप को बेहतर तरीके से नियंत्रित कर सकते हैं तो हम प्रतिक्रिया को अन्य सिस्टम में एकीकृत करना आसान बना सकते हैं।
- **बाहरी डेटा**। चैट संदर्भ में एप्लिकेशन के अन्य स्रोतों से डेटा का उपयोग करने की क्षमता।

## समस्या को एक परिदृश्य के माध्यम से चित्रित करना

> हम अनुशंसा करते हैं कि आप [शामिल नोटबुक](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) का उपयोग करें यदि आप नीचे दिए गए परिदृश्य को चलाना चाहते हैं। आप केवल पढ़ सकते हैं क्योंकि हम एक समस्या को चित्रित करने की कोशिश कर रहे हैं जहां फ़ंक्शंस समस्या को हल करने में मदद कर सकते हैं।

आइए उस उदाहरण को देखें जो प्रतिक्रिया प्रारूप समस्या को चित्रित करता है:

मान लें कि हम छात्र डेटा का एक डेटाबेस बनाना चाहते हैं ताकि हम उन्हें सही पाठ्यक्रम सुझा सकें। नीचे हमारे पास छात्रों के दो विवरण हैं जो उनके द्वारा शामिल डेटा में बहुत समान हैं।

1. हमारे Azure OpenAI संसाधन से कनेक्शन बनाएं:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   नीचे कुछ Python कोड है जो हमारे Azure OpenAI कनेक्शन को कॉन्फ़िगर करता है, जहां हम `api_type`, `api_base`, `api_version` और `api_key` सेट करते हैं।

1. दो छात्र विवरण बनाना, `student_1_description` और `student_2_description` का उपयोग करके।

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   हम ऊपर दिए गए छात्र विवरणों को LLM को भेजना चाहते हैं ताकि डेटा को पार्स किया जा सके। इस डेटा का उपयोग बाद में हमारे एप्लिकेशन में किया जा सकता है और इसे API में भेजा जा सकता है या डेटाबेस में संग्रहीत किया जा सकता है।

1. आइए दो समान प्रॉम्प्ट बनाएं जिसमें हम LLM को निर्देश दें कि हमें किस जानकारी में रुचि है:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   ऊपर दिए गए प्रॉम्प्ट LLM को जानकारी निकालने और JSON प्रारूप में प्रतिक्रिया लौटाने का निर्देश देते हैं।

1. प्रॉम्प्ट और Azure OpenAI से कनेक्शन सेट करने के बाद, अब हम प्रॉम्प्ट को LLM को भेजेंगे `openai.ChatCompletion` का उपयोग करके। हम प्रॉम्प्ट को `messages` वेरिएबल में स्टोर करते हैं और भूमिका को `user` असाइन करते हैं। यह चैटबॉट को लिखे गए उपयोगकर्ता के संदेश की नकल करने के लिए है।

   ```python
   # response from prompt one
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # response from prompt two
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

अब हम दोनों अनुरोधों को LLM को भेज सकते हैं और प्रतिक्रिया की जांच कर सकते हैं जो हमें इस तरह मिलती है `openai_response1['choices'][0]['message']['content']`।

1. अंत में, हम प्रतिक्रिया को JSON प्रारूप में `json.loads` को कॉल करके परिवर्तित कर सकते हैं:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   प्रतिक्रिया 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   प्रतिक्रिया 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   हालांकि प्रॉम्प्ट समान हैं और विवरण समान हैं, हम देखते हैं कि `Grades` प्रॉपर्टी के मान अलग-अलग स्वरूपित हैं, जैसे कि हमें कभी-कभी `3.7` या `3.7 GPA` प्रारूप मिलता है।

   यह परिणाम इसलिए है क्योंकि LLM लिखित प्रॉम्प्ट के रूप में असंरचित डेटा लेता है और असंरचित डेटा भी लौटाता है। हमें एक संरचित प्रारूप की आवश्यकता है ताकि हम यह जान सकें कि इस डेटा को संग्रहीत या उपयोग करते समय क्या उम्मीद करनी चाहिए।

तो फिर हम स्वरूपण समस्या को कैसे हल करें? फ़ंक्शनल कॉलिंग का उपयोग करके, हम यह सुनिश्चित कर सकते हैं कि हमें संरचित डेटा वापस मिले। फ़ंक्शन कॉलिंग का उपयोग करते समय, LLM वास्तव में किसी भी फ़ंक्शन को कॉल या चलाता नहीं है। इसके बजाय, हम LLM को उसके प्रतिक्रियाओं के लिए पालन करने के लिए एक संरचना बनाते हैं। फिर हम उन संरचित प्रतिक्रियाओं का उपयोग यह जानने के लिए करते हैं कि हमारे एप्लिकेशन में कौन सा फ़ंक्शन चलाना है।

![फ़ंक्शन फ्लो](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.hi.png)

हम फिर फ़ंक्शन से जो लौटाया जाता है उसे ले सकते हैं और इसे LLM को वापस भेज सकते हैं। फिर LLM उपयोगकर्ता की क्वेरी का उत्तर देने के लिए प्राकृतिक भाषा का उपयोग करके प्रतिक्रिया देगा।

## फ़ंक्शन कॉल का उपयोग करने के उपयोग के मामले

ऐसे कई अलग-अलग उपयोग के मामले हैं जहां फ़ंक्शन कॉल आपके ऐप को बेहतर बना सकते हैं जैसे:

- **बाहरी उपकरणों को कॉल करना**। चैटबॉट उपयोगकर्ताओं से प्रश्नों के उत्तर प्रदान करने में बहुत अच्छे हैं। फ़ंक्शन कॉलिंग का उपयोग करके, चैटबॉट उपयोगकर्ताओं के संदेशों का उपयोग कुछ कार्यों को पूरा करने के लिए कर सकते हैं। उदाहरण के लिए, एक छात्र चैटबॉट से पूछ सकता है, "मेरे प्रशिक्षक को एक ईमेल भेजें जिसमें कहा गया हो कि मुझे इस विषय में अधिक सहायता की आवश्यकता है।" यह `send_email(to: string, body: string)` नामक फ़ंक्शन कॉल कर सकता है।

- **API या डेटाबेस क्वेरी बनाना**। उपयोगकर्ता प्राकृतिक भाषा का उपयोग करके जानकारी पा सकते हैं जो एक स्वरूपित क्वेरी या API अनुरोध में परिवर्तित हो जाती है। इसका एक उदाहरण एक शिक्षक हो सकता है जो अनुरोध करता है, "वे छात्र कौन हैं जिन्होंने अंतिम असाइनमेंट पूरा किया" जो `get_completed(student_name: string, assignment: int, current_status: string)` नामक फ़ंक्शन को कॉल कर सकता है।

- **संरचित डेटा बनाना**। उपयोगकर्ता टेक्स्ट या CSV का एक ब्लॉक ले सकते हैं और LLM का उपयोग करके उससे महत्वपूर्ण जानकारी निकाल सकते हैं। उदाहरण के लिए, एक छात्र शांति समझौतों के बारे में विकिपीडिया लेख को एआई फ्लैशकार्ड बनाने के लिए परिवर्तित कर सकता है। इसे `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)` नामक फ़ंक्शन का उपयोग करके किया जा सकता है।

## अपना पहला फ़ंक्शन कॉल बनाना

फ़ंक्शन कॉल बनाने की प्रक्रिया में 3 मुख्य चरण शामिल हैं:

1. **कॉल करना** चैट कम्प्लीशन API को आपके फ़ंक्शंस की सूची और उपयोगकर्ता संदेश के साथ।
2. **पढ़ना** मॉडल की प्रतिक्रिया को एक क्रिया करने के लिए, जैसे कि फ़ंक्शन या API कॉल को निष्पादित करना।
3. **बनाना** चैट कम्प्लीशन API को आपके फ़ंक्शन की प्रतिक्रिया के साथ एक और कॉल ताकि उपयोगकर्ता को प्रतिक्रिया बनाने के लिए उस जानकारी का उपयोग किया जा सके।

![LLM फ्लो](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.hi.png)

### चरण 1 - संदेश बनाना

पहला चरण उपयोगकर्ता संदेश बनाना है। इसे टेक्स्ट इनपुट के मान को लेकर गतिशील रूप से असाइन किया जा सकता है या आप यहां एक मान असाइन कर सकते हैं। यदि यह आपका पहली बार चैट कम्प्लीशन API के साथ काम करना है, तो हमें संदेश की `role` और `content` को परिभाषित करना होगा।

`role` `system` (नियम बनाना), `assistant` (मॉडल) या `user` (अंतिम उपयोगकर्ता) हो सकता है। फ़ंक्शन कॉलिंग के लिए, हम इसे `user` के रूप में असाइन करेंगे और एक उदाहरण प्रश्न देंगे।

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

विभिन्न भूमिकाओं को असाइन करके, यह LLM के लिए स्पष्ट हो जाता है कि यह सिस्टम कुछ कह रहा है या उपयोगकर्ता, जो LLM को बातचीत का इतिहास बनाने में मदद करता है जिस पर वह निर्माण कर सकता है।

### चरण 2 - फ़ंक्शंस बनाना

अगला, हम एक फ़ंक्शन और उस फ़ंक्शन के पैरामीटर को परिभाषित करेंगे। हम यहां केवल एक फ़ंक्शन का उपयोग करेंगे जिसे `search_courses` कहा जाता है लेकिन आप कई फ़ंक्शंस बना सकते हैं।

> **महत्वपूर्ण** : फ़ंक्शंस LLM को सिस्टम संदेश में शामिल किए जाते हैं और आपके पास उपलब्ध टोकन की मात्रा में शामिल किए जाएंगे।

नीचे, हम फ़ंक्शंस को आइटम्स की एक सूची के रूप में बनाते हैं। प्रत्येक आइटम एक फ़ंक्शन है और इसमें `name`, `description` और `parameters` प्रॉपर्टीज़ होती हैं:

```python
functions = [
   {
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

आइए प्रत्येक फ़ंक्शन उदाहरण को नीचे अधिक विस्तार से वर्णित करें:

- `name` - उस फ़ंक्शन का नाम जिसे हम कॉल करना चाहते हैं।
- `description` - यह फ़ंक्शन कैसे काम करता है इसका विवरण। यहां विशिष्ट और स्पष्ट होना महत्वपूर्ण है।
- `parameters` - मानों और प्रारूप की सूची जिसे आप चाहते हैं कि मॉडल अपनी प्रतिक्रिया में उत्पन्न करे। पैरामीटर सूची में आइटम होते हैं जहां आइटम में निम्नलिखित प्रॉपर्टीज़ होती हैं:
  1.  `type` - प्रॉपर्टीज़ किस डेटा प्रकार में संग्रहीत की जाएंगी।
  1.  `properties` - विशिष्ट मानों की सूची जिसे मॉडल अपनी प्रतिक्रिया के लिए उपयोग करेगा।
      1. `name` - कुंजी प्रॉपर्टी का नाम है जिसे मॉडल अपनी स्वरूपित प्रतिक्रिया में उपयोग करेगा, उदाहरण के लिए, `product`।
      1. `type` - इस प्रॉपर्टी का डेटा प्रकार, उदाहरण के लिए, `string`।
      1. `description` - विशिष्ट प्रॉपर्टी का विवरण।

एक वैकल्पिक प्रॉपर्टी `required` भी है - फ़ंक्शन कॉल को पूरा करने के लिए आवश्यक प्रॉपर्टी।

### चरण 3 - फ़ंक्शन कॉल बनाना

फ़ंक्शन को परिभाषित करने के बाद, अब हमें इसे चैट कम्प्लीशन API के कॉल में शामिल करना होगा। हम इसे अनुरोध में `functions` जोड़कर करते हैं। इस मामले में `functions=functions`।

`function_call` को `auto` पर सेट करने का विकल्प भी है। इसका मतलब है कि हम LLM को उपयोगकर्ता संदेश के आधार पर तय करने देंगे कि कौन सा फ़ंक्शन कॉल किया जाना चाहिए बजाय इसके कि हम इसे स्वयं असाइन करें।

नीचे कुछ कोड है जहां हम `ChatCompletion.create` को कॉल करते हैं, ध्यान दें कि हम `functions=functions` और `function_call="auto"` सेट करते हैं और इस प्रकार LLM को यह तय करने का विकल्प देते हैं कि हमारे द्वारा प्रदान किए गए फ़ंक्शंस को कब कॉल करना है:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

अब वापस आने वाली प्रतिक्रिया इस प्रकार दिखती है:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

यहां हम देख सकते हैं कि फ़ंक्शन `search_courses` को किस तर्कों के साथ कॉल किया गया था, जैसा कि JSON प्रतिक्रिया में `arguments` प्रॉपर्टी में सूचीबद्ध है।

निष्कर्ष यह है कि LLM तर्कों के लिए डेटा खोजने में सक्षम था क्योंकि यह इसे चैट कम्प्लीशन कॉल में `messages` पैरामीटर को प्रदान किए गए मान से निकाल रहा था। नीचे `messages` मान की याद दिलाई गई है:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

जैसा कि आप देख सकते हैं, `student`, `Azure` और `beginner` को `messages` से निकाला गया और फ़ंक्शन में इनपुट के रूप में सेट किया गया। इस तरह फ़ंक्शंस का उपयोग करना प्रॉम्प्ट से जानकारी निकालने का एक शानदार तरीका है लेकिन LLM को संरचना प्रदान करने और पुन: उपयोग योग्य कार्यक्षमता प्राप्त करने का भी।

अब, हमें यह देखना होगा कि हम इसे अपने ऐप में कैसे उपयोग कर सकते हैं।

## एप्लिकेशन में फ़ंक्शन कॉल्स को एकीकृत करना

LLM से स्वरूपित प्रतिक्रिया का परीक्षण करने के बाद, अब हम इसे अपने एप्लिकेशन में एकीकृत कर सकते हैं।

### फ्लो का प्रबंधन

इसे हमारे एप्लिकेशन में एकीकृत करने के लिए, आइए निम्नलिखित चरणों को लें:

1. सबसे पहले, आइए OpenAI सेवाओं को कॉल करें और संदेश को `response_message` नामक वेरिएबल में स्टोर करें।

   ```python
   response_message = response.choices[0].message
   ```

1. अब हम एक फ़ंक्शन को परिभाषित करेंगे जो Microsoft Learn API को कॉल करेगा ताकि पाठ्यक्रमों की सूची प्राप्त की जा सके:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   ध्यान दें कि अब हम एक वास्तविक Python फ़ंक्शन बनाते हैं जो `functions` वेरिएबल में पेश किए गए फ़ंक्शन नामों से मेल खाता है। हम डेटा प्राप्त करने के लिए वास्तविक बाहरी API कॉल भी कर रहे हैं। इस मामले में, हम प्रशिक्षण मॉड्यूल खोजने के लिए Microsoft Learn API के खिलाफ जाते हैं।

ठीक है, तो हमने `functions` वेरिएबल और एक संबंधित Python फ़ंक्शन बनाया, हम LLM को यह कैसे बताते हैं कि इन दोनों को एक साथ कैसे मैप करें ताकि हमारा Python फ़ंक्शन कॉल हो?

1. यह देखने के लिए कि क्या हमें Python फ़ंक्शन कॉल करने की आवश्यकता है, हमें LLM प्रतिक्रिया में देखना होगा और जांचना होगा कि क्या `function_call` इसका हिस्सा है और निर्दिष्ट फ़ंक्शन को कॉल करना होगा। नीचे दिए गए तरीके से आप उल्लिखित जांच कर सकते हैं:

   ```python
   # Check if the model wants to call a function
   if response_message.function_call.name:
    print("Recommended Function call:")
    print(response_message.function_call.name)
    print()

    # Call the function.
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   ये तीन लाइनें सुनिश्चित करती हैं कि हम फ़ंक्शन का नाम, तर्क निकालें और कॉल करें:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   नीचे हमारे कोड को चलाने से आउटपुट है:

   **आउटपुट**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. अब हम अपडेटेड संदेश, `messages` को LLM को भेजेंगे ताकि हमें API JSON स्वरूपित प्रतिक्रिया के बजाय प्राकृतिक भाषा प्रतिक्रिया प्राप्त हो सके।

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # get a new response from GPT where it can see the function response


   print(second_response.choices[0].message)
   ```

   **आउटपुट**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## असाइनमेंट

Azure OpenAI फ़ंक्शन कॉलिंग के अपने सीखने को जारी रखने के लिए आप निम्नलिखित बना सकते हैं:

- फ़ंक्शन के अधिक पैरामीटर जो शिक्षार्थियों को अधिक पाठ्यक्रम खोजने में मदद कर सकते हैं।
- एक और फ़ंक्शन कॉल बनाएं जो शिक्षार्थी से उनकी मूल भाषा जैसी अधिक जानकारी ले।
- जब फ़ंक्शन कॉल और/या API कॉल कोई उपयुक्त पाठ्यक्रम वापस नहीं करता है, तो त्रुटि हैंडलिंग बनाएं

संकेत: यह डेटा कैसे और कहाँ उपलब्ध है, यह देखने के लिए [Learn API संदर्भ दस्तावेज़](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) पृष्ठ का अनुसरण करें।

## शानदार काम! यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें और अपनी Generative AI ज्ञान को और बढ़ाएं!

पाठ 12 पर जाएं, जहां हम देखेंगे कि [AI एप्लिकेशन के लिए UX कैसे डिज़ाइन करें](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।