<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-07-09T14:28:53+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "mr"
}
-->
# फंक्शन कॉलिंगसह एकत्रीकरण

[![फंक्शन कॉलिंगसह एकत्रीकरण](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.mr.png)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

आपण मागील धड्यांमध्ये बरंच काही शिकलात. मात्र, आपण अजून सुधारणा करू शकतो. काही गोष्टी ज्या आपण हाताळू शकतो त्या म्हणजे प्रतिसादाचा अधिक सुसंगत फॉरमॅट मिळवणे जेणेकरून प्रतिसादासह पुढील काम करणे सोपे होईल. तसेच, आपल्याला आपल्या अॅप्लिकेशनला अधिक समृद्ध करण्यासाठी इतर स्रोतांमधून डेटा जोडायचा असू शकतो.

वरील नमूद केलेल्या समस्या या प्रकरणात हाताळण्याचा प्रयत्न केला आहे.

## परिचय

हा धडा खालील गोष्टींचा आढावा घेईल:

- फंक्शन कॉलिंग म्हणजे काय आणि त्याचे उपयोग काय आहेत हे समजावून सांगणे.
- Azure OpenAI वापरून फंक्शन कॉल तयार करणे.
- फंक्शन कॉल कसे अॅप्लिकेशनमध्ये एकत्रित करायचे.

## शिकण्याचे उद्दिष्ट

या धड्याच्या शेवटी, आपण सक्षम असाल:

- फंक्शन कॉलिंग वापरण्याचा उद्देश समजावून सांगणे.
- Azure OpenAI सेवा वापरून फंक्शन कॉल सेटअप करणे.
- आपल्या अॅप्लिकेशनच्या वापरासाठी प्रभावी फंक्शन कॉल डिझाइन करणे.

## परिस्थिती: फंक्शन्ससह आमचा चॅटबॉट सुधारित करणे

या धड्यासाठी, आपल्याला आपल्या शिक्षण स्टार्टअपने एक अशी सुविधा तयार करायची आहे ज्यात वापरकर्ते तांत्रिक कोर्स शोधण्यासाठी चॅटबॉट वापरू शकतील. आम्ही त्यांच्या कौशल्य पातळी, सध्याच्या भूमिकेनुसार आणि आवडत्या तंत्रज्ञानानुसार कोर्सची शिफारस करू.

ही परिस्थिती पूर्ण करण्यासाठी, आपण खालील संयोजन वापरणार आहोत:

- `Azure OpenAI` वापरून वापरकर्त्यासाठी चॅट अनुभव तयार करणे.
- `Microsoft Learn Catalog API` वापरून वापरकर्त्यांच्या विनंतीनुसार कोर्स शोधण्यात मदत करणे.
- `Function Calling` वापरून वापरकर्त्याच्या क्वेरीला फंक्शनकडे पाठवणे जेणेकरून API विनंती करता येईल.

सुरू करण्यासाठी, आपण पाहूया की आपण फंक्शन कॉलिंग का वापरू इच्छितो:

## फंक्शन कॉलिंग का?

फंक्शन कॉलिंगपूर्वी, LLM कडून मिळणारे प्रतिसाद असंरचित आणि असुसंगत होते. विकसकांना प्रत्येक प्रतिसादाच्या विविधतेस हाताळण्यासाठी गुंतागुंतीचा व्हॅलिडेशन कोड लिहावा लागायचा. वापरकर्ते "स्टॉकहोममधील सध्याचा हवामान काय आहे?" यासारखे प्रश्न विचारू शकत नव्हते. कारण मॉडेल्सना फक्त प्रशिक्षण दिलेल्या डेटाच्या कालावधीपुरतेच मर्यादा होत्या.

Azure OpenAI सेवेतील फंक्शन कॉलिंग ही खालील मर्यादा दूर करण्यासाठी एक वैशिष्ट्य आहे:

- **सुसंगत प्रतिसाद फॉरमॅट**. जर आपण प्रतिसादाचा फॉरमॅट चांगल्या प्रकारे नियंत्रित करू शकतो, तर प्रतिसाद पुढील प्रणालींमध्ये सहजपणे एकत्रित करता येतो.
- **बाह्य डेटा**. चॅट संदर्भात अॅप्लिकेशनमधील इतर स्रोतांमधील डेटा वापरण्याची क्षमता.

## समस्येचे उदाहरणात्मक स्पष्टीकरण

> आपण खालील परिस्थिती चालवायची असल्यास, [संपूर्ण नोटबुक](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) वापरण्याची शिफारस करतो. आपण फक्त वाचतही राहू शकता कारण आम्ही एक समस्या स्पष्ट करण्याचा प्रयत्न करत आहोत ज्यात फंक्शन्स मदत करू शकतात.

चला प्रतिसाद फॉरमॅट समस्येचे उदाहरण पाहूया:

समजा, आपण विद्यार्थ्यांचा डेटा संग्रहित करण्यासाठी एक डेटाबेस तयार करू इच्छितो जेणेकरून त्यांना योग्य कोर्स सुचवता येईल. खाली दोन विद्यार्थ्यांचे वर्णन दिले आहे जे डेटा संदर्भात खूपच समान आहेत.

1. Azure OpenAI संसाधनाशी कनेक्शन तयार करा:

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

   खाली काही Python कोड आहे ज्यात आपण Azure OpenAI कनेक्शनसाठी `api_type`, `api_base`, `api_version` आणि `api_key` सेट करत आहोत.

1. दोन विद्यार्थी वर्णने तयार करणे, `student_1_description` आणि `student_2_description` या व्हेरिएबल्स वापरून.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   आपण वरील विद्यार्थी वर्णने LLM कडे पाठवू इच्छितो जेणेकरून डेटा पार्स केला जाईल. हा डेटा नंतर आपल्या अॅप्लिकेशनमध्ये वापरला जाऊ शकतो, API कडे पाठवला जाऊ शकतो किंवा डेटाबेसमध्ये साठवला जाऊ शकतो.

1. दोन सारखे प्रॉम्प्ट तयार करूया ज्यात आपण LLM ला सांगतो की आपल्याला कोणती माहिती हवी आहे:

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

   वरील प्रॉम्प्ट LLM ला माहिती काढण्याचे आणि JSON फॉरमॅटमध्ये प्रतिसाद देण्याचे निर्देश देतात.

1. प्रॉम्प्ट आणि Azure OpenAI कनेक्शन सेट केल्यानंतर, आपण आता `openai.ChatCompletion` वापरून प्रॉम्प्ट LLM कडे पाठवू. प्रॉम्प्ट `messages` व्हेरिएबलमध्ये साठवतो आणि `user` ही भूमिका देतो. हे वापरकर्त्याचा संदेश चॅटबॉटला लिहिल्याप्रमाणे अनुकरण करण्यासाठी आहे.

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

आता आपण दोन्ही विनंत्या LLM कडे पाठवू शकतो आणि प्रतिसाद तपासू शकतो, जसे की `openai_response1['choices'][0]['message']['content']` वापरून.

1. शेवटी, आपण प्रतिसाद JSON फॉरमॅटमध्ये रूपांतरित करू शकतो `json.loads` कॉल करून:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   प्रतिसाद 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   प्रतिसाद 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   जरी प्रॉम्प्ट सारखेच आहेत आणि वर्णने समान आहेत, तरी `Grades` प्रॉपर्टीचे मूल्य वेगवेगळ्या स्वरूपात आहे, कधी `3.7` तर कधी `3.7 GPA` असे.

   हा परिणाम असा आहे कारण LLM अनस्ट्रक्चर्ड डेटा (लेखन प्रॉम्प्ट) घेतो आणि अनस्ट्रक्चर्ड डेटा परत करतो. आपल्याला एक संरचित फॉरमॅट हवा आहे जेणेकरून आपण डेटा साठवताना किंवा वापरताना काय अपेक्षित आहे हे समजू शकेल.

तर आपण फॉरमॅटिंगची समस्या कशी सोडवू? फंक्शन कॉलिंग वापरून, आपण सुनिश्चित करू शकतो की आपल्याला संरचित डेटा परत मिळेल. फंक्शन कॉलिंग वापरताना, LLM प्रत्यक्षात कोणतेही फंक्शन कॉल करत नाही किंवा चालवत नाही. त्याऐवजी, आपण LLM साठी प्रतिसादांसाठी एक संरचना तयार करतो. नंतर आपण त्या संरचित प्रतिसादांचा वापर करून आपल्या अॅप्लिकेशनमध्ये कोणते फंक्शन चालवायचे ते ठरवतो.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.mr.png)

आपण नंतर फंक्शनकडून परत आलेले डेटा घेऊन तो पुन्हा LLM कडे पाठवू शकतो. LLM नंतर वापरकर्त्याच्या प्रश्नाला नैसर्गिक भाषेत उत्तर देईल.

## फंक्शन कॉल वापरण्याचे उपयोग

फंक्शन कॉल्स वापरून आपले अॅप सुधारू शकणाऱ्या अनेक उपयोगांपैकी काही:

- **बाह्य साधने कॉल करणे**. चॅटबॉट वापरकर्त्यांच्या प्रश्नांची उत्तरे देण्यात उत्कृष्ट असतात. फंक्शन कॉलिंग वापरून, चॅटबॉट वापरकर्त्यांच्या संदेशांचा वापर करून विशिष्ट कार्ये पूर्ण करू शकतो. उदाहरणार्थ, विद्यार्थी चॅटबॉटला म्हणू शकतो "माझ्या शिक्षकाला ईमेल पाठवा की मला या विषयात अधिक मदत हवी आहे". हे `send_email(to: string, body: string)` फंक्शन कॉल करू शकते.

- **API किंवा डेटाबेस क्वेरी तयार करणे**. वापरकर्ते नैसर्गिक भाषेत माहिती शोधू शकतात जी नंतर फॉरमॅटेड क्वेरी किंवा API विनंतीमध्ये रूपांतरित होते. उदाहरणार्थ, शिक्षक विचारू शकतो "शेवटचे असाइनमेंट पूर्ण करणारे विद्यार्थी कोण आहेत?" जे `get_completed(student_name: string, assignment: int, current_status: string)` नावाचे फंक्शन कॉल करू शकते.

- **संरचित डेटा तयार करणे**. वापरकर्ते मजकूराचा किंवा CSV चा ब्लॉक घेऊन LLM वापरून महत्त्वाची माहिती काढू शकतात. उदाहरणार्थ, विद्यार्थी Wikipedia लेख शांती करारांबद्दल AI फ्लॅशकार्ड तयार करण्यासाठी रूपांतरित करू शकतो. हे `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)` नावाच्या फंक्शनने करता येते.

## आपला पहिला फंक्शन कॉल तयार करणे

फंक्शन कॉल तयार करण्याची प्रक्रिया 3 मुख्य टप्प्यांत विभागली आहे:

1. आपल्या फंक्शन्सची यादी आणि वापरकर्त्याचा संदेश वापरून Chat Completions API कॉल करणे.
2. मॉडेलच्या प्रतिसादाचे वाचन करून क्रिया करणे म्हणजे फंक्शन किंवा API कॉल चालवणे.
3. आपल्या फंक्शनकडून आलेल्या प्रतिसादासह पुन्हा Chat Completions API कॉल करणे जेणेकरून वापरकर्त्यासाठी प्रतिसाद तयार करता येईल.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.mr.png)

### टप्पा 1 - संदेश तयार करणे

पहिला टप्पा म्हणजे वापरकर्त्याचा संदेश तयार करणे. हा संदेश डायनॅमिकली टेक्स्ट इनपुटमधून घेतला जाऊ शकतो किंवा आपण येथे थेट मूल्य देऊ शकता. जर आपण Chat Completions API सह प्रथमच काम करत असाल, तर आपल्याला `role` आणि `content` परिभाषित करावे लागेल.

`role` हे `system` (नियम तयार करणे), `assistant` (मॉडेल) किंवा `user` (अंतिम वापरकर्ता) असू शकते. फंक्शन कॉलिंगसाठी, आपण हे `user` म्हणून सेट करू आणि एक उदाहरण प्रश्न देऊ.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

वेगवेगळ्या भूमिका देऊन, LLM ला स्पष्ट होते की कोणती भूमिका कोणती आहे, ज्यामुळे संभाषणाचा इतिहास तयार होतो ज्यावर LLM पुढे काम करू शकतो.

### टप्पा 2 - फंक्शन्स तयार करणे

नंतर, आपण एक फंक्शन आणि त्याचे पॅरामीटर्स परिभाषित करू. येथे आपण `search_courses` नावाचे एक फंक्शन वापरणार आहोत, पण आपण अनेक फंक्शन्स तयार करू शकता.

> **महत्त्वाचे** : फंक्शन्स LLM ला दिलेल्या सिस्टम संदेशात समाविष्ट असतात आणि उपलब्ध टोकन्सच्या मर्यादेत गणले जातात.

खाली, आपण फंक्शन्स आयटम्सच्या अ‍ॅरेमध्ये तयार करतो. प्रत्येक आयटम एक फंक्शन आहे ज्यात `name`, `description` आणि `parameters` या प्रॉपर्टीज असतात:

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

प्रत्येक फंक्शनची अधिक सविस्तर माहिती खाली दिली आहे:

- `name` - कॉल करायच्या फंक्शनचे नाव.
- `description` - फंक्शन कसे कार्य करते याचे वर्णन. येथे स्पष्ट आणि विशिष्ट असणे महत्त्वाचे आहे.
- `parameters` - मूल्ये आणि फॉरमॅटची यादी जी मॉडेलने प्रतिसादात तयार करायची आहे. `parameters` अ‍ॅरेमध्ये खालील प्रॉपर्टीज असतात:
  1. `type` - प्रॉपर्टीचा डेटा प्रकार.
  2. `properties` - मॉडेल प्रतिसादात वापरणार्‍या विशिष्ट मूल्यांची यादी.
      1. `name` - प्रॉपर्टीचे नाव, जसे `product`.
      2. `type` - या प्रॉपर्टीचा डेटा प्रकार, जसे `string`.
      3. `description` - प्रॉपर्टीचे वर्णन.

`required` ही एक ऐच्छिक प्रॉपर्टी आहे जी फंक्शन कॉल पूर्ण होण्यासाठी आवश्यक असलेल्या प्रॉपर्टी दर्शवते.

### टप्पा 3 - फंक्शन कॉल करणे

फंक्शन परिभाषित केल्यानंतर, आता आपल्याला ते Chat Completion API कॉलमध्ये समाविष्ट करायचे आहे. आपण `functions` या विनंतीत जोडतो. येथे `functions=functions` असे सेट केले आहे.

`function_call` हे `auto` असे सेट करण्याचा पर्याय देखील आहे. याचा अर्थ LLM वापरकर्त्याच्या संदेशावरून कोणते फंक्शन कॉल करायचे ते ठरवेल, आपण स्वतः ठरवणार नाही.

खालील कोडमध्ये आपण `ChatCompletion.create` कॉल करत आहोत, जिथे `functions=functions` आणि `function_call="auto"` सेट केले आहे, ज्यामुळे LLM ला फंक्शन्स कॉल करण्याचा निर्णय घेण्याची मुभा मिळते:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

आता परत आलेला प्रतिसाद असा दिसतो:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

येथे आपण पाहू शकतो की `search_courses` फंक्शन कॉल झाले आहे आणि कोणते आर्ग्युमेंट्स दिले गेले आहेत, जे JSON प्रतिसादातील `arguments` प्रॉपर्टीमध्ये आहेत.

निष्कर्ष असा की LLM ला `messages` पॅरामीटरमध्ये दिलेल्या मूल्यांमधून डेटा काढून फंक्शनच्या आर्ग्युमेंट्ससाठी योग्य डेटा सापडला.

खाली `messages` चे मूल्य पुन्हा दिले आहे:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

जसे आपण पाहू शकता, `student`, `Azure` आणि `beginner` या शब्दांचा वापर करून फंक्शनसाठी इनपुट तयार केले गेले. अशा प्रकारे फंक्शन्स वापरणे म्हणजे प्रॉम्प्टमधून माहिती काढणे आणि LLM ला संरचित प्रतिसाद देण्याची क्षमता देणे.

आता पाहूया की आपण हे आपल्या अॅपमध्ये कसे वापरू शकतो.

## अॅप्लिकेशनमध्ये फंक्शन कॉल्स एकत्रित करणे

LLM कडून सुसंगत प्रतिसाद मिळाल्यानंतर, आपण आता ते अॅप्लिकेशनमध्ये एकत्रित करू शकतो.

### फ्लो व्यवस्थापन

हे आपल्या अॅप्लिकेशनमध्ये एकत्रित करण्यासाठी, खालील टप्पे घ्या:

1. प्रथम, OpenAI सेवांना कॉल करा आणि प्रतिसाद संदेश `response_message` नावाच्या व्हेरिएबलमध्ये साठवा.

   ```python
   response_message = response.choices[0].message
   ```

1. आता आपण Microsoft Learn API कॉल करणारे फंक्शन परिभाषित करू:

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

   येथे आपण प्रत्यक्ष Python फंक्शन तयार करत आहोत जे `functions` व्हेरिएबलमध्ये दिलेल्या फंक्शन नावाशी जुळते. तसेच, आपण प्रत्यक्ष बाह्य API कॉल करत आहोत जेणेकरून आवश्यक डेटा मिळेल. या प्रकरणात, आपण Microsoft Learn API कडे प्रशिक्षण मॉड्यूल शोधण्यासाठी विनंती करतो.

आता आपण `functions` व्हेरिएबल तयार केले आणि त्यास अनुरूप Python फंक्शन तयार केले, तर LLM ला कसे सांगू की या दोन्हींचा नकाशा कसा करायचा म्हणजे Python फंक्शन कॉल व्हावे?

1. Python फंक्शन कॉल करायची गरज आहे का ते पाहण्यासाठी, आपण LLM च्या प्रतिसादात `function_call` आहे का ते तपासावे आणि नंतर निर्देशित फंक्शन कॉल करावे. खाली यासाठी तपासणी कशी करायची ते दाखवले आहे:

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

   या तीन ओळींमध्ये आपण फंक्शनचे नाव, आर्ग्युमेंट्स काढतो आणि कॉल करतो:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   खाली आपला कोड चालवल्यानंतरचा आउटपुट आहे:

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

1. आता आपण अपडेट केलेला संदेश `messages` LLM कडे पाठवू जेणेकरून आपल्याला API JSON फॉरमॅटेड प्रतिसादाऐवजी नैसर्गिक भाषेतील प्रतिसाद मिळेल.

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

Azure OpenAI Function Calling चे शिक्षण पुढे सुरू ठेवण्यासाठी आपण तयार करू शकता:

- फंक्शनचे अधिक पॅरामीटर्स जे शिकणाऱ्यांना अधिक कोर्स शोधण्यात मदत करू शकतील.
- आणखी एक फंक्शन कॉल तयार करा जे शिकणाऱ्याची मातृभाषा यासारखी अधिक माहिती घेईल.
- फंक्शन कॉल किंवा API कॉल योग्य कोर्स परत न केल्यास त्रुटी हाताळणी तयार करा.
## छान काम! प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मध्ये नक्की पहा आणि तुमचे Generative AI ज्ञान अधिक वाढवा!

आता धडा 12 कडे चला, जिथे आपण पाहणार आहोत की [AI अनुप्रयोगांसाठी UX कसे डिझाइन करायचे](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.