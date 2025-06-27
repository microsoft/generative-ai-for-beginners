<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-06-25T19:49:18+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "mr"
}
-->
# फंक्शन कॉलिंगसह एकत्रीकरण

आपण आतापर्यंतच्या पूर्वीच्या धड्यांमध्ये बरेच काही शिकलात. तथापि, आपण आणखी सुधार करू शकतो. काही गोष्टी आम्ही संबोधित करू शकतो म्हणजे आम्ही उत्तराचा अधिक सुसंगत स्वरूप कसा मिळवू शकतो ज्यामुळे उत्तरासह काम करणे सोपे होईल. तसेच, आम्ही आमच्या अनुप्रयोगाला अधिक समृद्ध करण्यासाठी इतर स्रोतांकडून डेटा जोडू इच्छितो.

वरील समस्यांचे निराकरण करण्यासाठी हा अध्याय आहे.

## परिचय

हा धडा कव्हर करेल:

- फंक्शन कॉलिंग म्हणजे काय आणि त्याचे वापराचे केस काय आहेत हे स्पष्ट करा.
- Azure OpenAI वापरून फंक्शन कॉल तयार करणे.
- फंक्शन कॉलला अनुप्रयोगात एकत्रित कसे करावे.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, आपण सक्षम असाल:

- फंक्शन कॉलिंग वापरण्याचा हेतू स्पष्ट करा.
- Azure OpenAI सेवा वापरून फंक्शन कॉल सेटअप करा.
- आपल्या अनुप्रयोगाच्या वापराच्या केससाठी प्रभावी फंक्शन कॉल डिझाइन करा.

## प्रसंग: आमच्या चॅटबॉटला फंक्शनसह सुधारित करणे

या धड्यासाठी, आम्ही आमच्या शिक्षण स्टार्टअपसाठी एक वैशिष्ट्य तयार करू इच्छितो जे वापरकर्त्यांना तांत्रिक कोर्स शोधण्यासाठी चॅटबॉट वापरण्याची परवानगी देते. आम्ही त्यांच्या कौशल्य स्तर, वर्तमान भूमिका आणि तंत्रज्ञानाच्या आवडीशी जुळणारे कोर्स शिफारस करू.

या प्रसंग पूर्ण करण्यासाठी, आम्ही एकत्रितपणे वापरू:

- `Azure OpenAI` वापरकर्त्यासाठी चॅट अनुभव तयार करण्यासाठी.
- `Microsoft Learn Catalog API` वापरकर्त्याच्या विनंतीनुसार कोर्स शोधण्यात वापरकर्त्यांना मदत करण्यासाठी.
- `Function Calling` वापरकर्त्याच्या क्वेरीला घेऊन API विनंती करण्यासाठी फंक्शनला पाठविण्यासाठी.

सुरु करण्यासाठी, आपण प्रथम फंक्शन कॉलिंग का वापरू इच्छितो ते पाहू:

## फंक्शन कॉलिंग का

फंक्शन कॉलिंगपूर्वी, LLM मधील प्रतिसाद असंरचित आणि असुसंगत होते. विकासकांना प्रत्येक प्रतिसादाचा प्रकार हाताळण्यासाठी जटिल सत्यापन कोड लिहिणे आवश्यक होते. वापरकर्त्यांना "स्टॉकहोममधील सध्याचे हवामान काय आहे?" सारख्या प्रश्नांची उत्तरे मिळू शकत नव्हती. कारण मॉडेल्स त्यांच्या प्रशिक्षणाच्या वेळेपर्यंत मर्यादित होते.

Azure OpenAI सेवा हे फंक्शन कॉलिंगचे वैशिष्ट्य खालील मर्यादा ओलांडण्यासाठी आहे:

- **सुसंगत प्रतिसाद स्वरूप**. जर आपण प्रतिसाद स्वरूप चांगल्या प्रकारे नियंत्रित करू शकतो तर आम्ही प्रतिसादास इतर प्रणालींमध्ये एकत्रित करणे सोपे करू शकतो.
- **बाह्य डेटा**. चॅट संदर्भात अनुप्रयोगाच्या इतर स्रोतांकडून डेटा वापरण्याची क्षमता.

## समस्या एक प्रसंगाद्वारे स्पष्ट करणे

> जर आपण खालील प्रसंग चालवू इच्छित असाल तर आम्ही [समाविष्ट केलेला नोटबुक](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) वापरण्याची शिफारस करतो. आपण फक्त वाचू शकता कारण आम्ही एक समस्या स्पष्ट करण्याचा प्रयत्न करीत आहोत जिथे फंक्शन्स समस्या सोडविण्यात मदत करू शकतात.

चला उदाहरण पाहूया जे प्रतिसाद स्वरूप समस्या स्पष्ट करते:

मानूया की आम्हाला विद्यार्थ्यांच्या डेटाचा डेटाबेस तयार करायचा आहे ज्यामुळे आम्ही त्यांना योग्य कोर्स सुचवू शकतो. खाली विद्यार्थ्यांचे दोन वर्णन आहेत जे त्यांच्या डेटामध्ये खूप समान आहेत.

1. आमच्या Azure OpenAI संसाधनाशी कनेक्शन तयार करा:

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

   खाली Azure OpenAI कनेक्शन कॉन्फिगर करण्यासाठी काही Python कोड आहे जिथे आम्ही `api_type`, `api_base`, `api_version` and `api_key`.

1. Creating two student descriptions using variables `student_1_description` and `student_2_description` सेट करतो.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   आम्हाला वरील विद्यार्थ्यांचे वर्णन LLMला पाठवायचे आहे जेणेकरून ते डेटा पार्स करेल. हा डेटा नंतर आमच्या अनुप्रयोगात वापरला जाऊ शकतो आणि APIला पाठविला जाऊ शकतो किंवा डेटाबेसमध्ये संग्रहित केला जाऊ शकतो.

1. चला दोन समान प्रॉम्प्ट तयार करूया ज्यात आम्ही LLMला कोणती माहिती आमच्यासाठी स्वारस्यपूर्ण आहे ते सांगतो:

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

   वरील प्रॉम्प्ट्स LLMला माहिती काढण्यासाठी आणि JSON स्वरूपात प्रतिसाद परत करण्यासाठी सूचना देतात.

1. प्रॉम्प्ट्स आणि Azure OpenAI कनेक्शन सेट केल्यानंतर, आता आम्ही प्रॉम्प्ट्सला LLMला `openai.ChatCompletion`. We store the prompt in the `messages` variable and assign the role to `user` वापरून पाठवू. हे चॅटबॉटला लिहिलेला वापरकर्त्याचा संदेश अनुकरण करण्यासाठी आहे.

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

आता आम्ही दोन्ही विनंत्या LLMला पाठवू शकतो आणि आम्हाला मिळालेला प्रतिसाद `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we can convert the response to JSON format by calling `json.loads` द्वारे शोधून पाहू:

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

   जरी प्रॉम्प्ट्स समान आहेत आणि वर्णने समान आहेत, तरीही आम्हाला `Grades` property formatted differently, as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.mr.png)

We can then take what is returned from the function and send this back to the LLM. The LLM will then respond using natural language to answer the user's query.

## Use Cases for using function calls

There are many different use cases where function calls can improve your app like:

- **Calling External Tools**. Chatbots are great at providing answers to questions from users. By using function calling, the chatbots can use messages from users to complete certain tasks. For example, a student can ask the chatbot to "Send an email to my instructor saying I need more assistance with this subject". This can make a function call to `send_email(to: string, body: string)`

- **Create API or Database Queries**. Users can find information using natural language that gets converted into a formatted query or API request. An example of this could be a teacher who requests "Who are the students that completed the last assignment" which could call a function named `get_completed(student_name: string, assignment: int, current_status: string)`

- **Creating Structured Data**. Users can take a block of text or CSV and use the LLM to extract important information from it. For example, a student can convert a Wikipedia article about peace agreements to create AI flashcards. This can be done by using a function called `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## Creating Your First Function Call

The process of creating a function call includes 3 main steps:

1. **Calling** the Chat Completions API with a list of your functions and a user message.
2. **Reading** the model's response to perform an action i.e. execute a function or API Call.
3. **Making** another call to Chat Completions API with the response from your function to use that information to create a response to the user.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.mr.png)

### Step 1 - creating messages

The first step is to create a user message. This can be dynamically assigned by taking the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message.

The `role` can be either `system` (creating rules), `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` आणि एक उदाहरण प्रश्नाच्या मूल्ये दिसतात.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

विविध भूमिका नियुक्त करून, LLMला स्पष्ट केले जाते की ते सिस्टम बोलत आहे की वापरकर्ता, ज्यामुळे LLM एक संवाद इतिहास तयार करू शकतो.

### चरण 2 - फंक्शन तयार करणे

आता, आम्ही एक फंक्शन आणि त्या फंक्शनचे पॅरामीटर्स परिभाषित करू. आम्ही येथे फक्त एक फंक्शन वापरू `search_courses` but you can create multiple functions.

> **Important** : Functions are included in the system message to the LLM and will be included in the amount of available tokens you have available.

Below, we create the functions as an array of items. Each item is a function and has properties `name`, `description` and `parameters` नावाचे:

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

आता प्रत्येक फंक्शन उदाहरण अधिक तपशीलात वर्णन करूया:

- `name` - The name of the function that we want to have called.
- `description` - This is the description of how the function works. Here it's important to be specific and clear.
- `parameters` - A list of values and format that you want the model to produce in its response. The parameters array consists of items where the items have the following properties:
  1.  `type` - The data type of the properties will be stored in.
  1.  `properties` - List of the specific values that the model will use for its response
      1. `name` - The key is the name of the property that the model will use in its formatted response, for example, `product`.
      1. `type` - The data type of this property, for example, `string`.
      1. `description` - Description of the specific property.

There's also an optional property `required` - required property for the function call to be completed.

### Step 3 - Making the function call

After defining a function, we now need to include it in the call to the Chat Completion API. We do this by adding `functions` to the request. In this case `functions=functions`.

There is also an option to set `function_call` to `auto`. This means we will let the LLM decide which function should be called based on the user message rather than assigning it ourselves.

Here's some code below where we call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` आणि त्यामुळे आम्ही प्रदान केलेल्या फंक्शनला कधी कॉल करावे हे LLMला निवडण्याची परवानगी देतो:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

आता परत येणारा प्रतिसाद असा दिसतो:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

येथे आपण कसे पाहू शकतो की फंक्शन `search_courses` was called and with what arguments, as listed in the `arguments` property in the JSON response.

The conclusion the LLM was able to find the data to fit the arguments of the function as it was extracting it from the value provided to the `messages` parameter in the chat completion call. Below is a reminder of the `messages` मूल्य:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

जसे आपण पाहू शकता, `student`, `Azure` and `beginner` was extracted from `messages` and set as input to the function. Using functions this way is a great way to extract information from a prompt but also to provide structure to the LLM and have reusable functionality.

Next, we need to see how we can use this in our app.

## Integrating Function Calls into an Application

After we have tested the formatted response from the LLM, we can now integrate this into an application.

### Managing the flow

To integrate this into our application, let's take the following steps:

1. First, let's make the call to the OpenAI services and store the message in a variable called `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. आता आम्ही Microsoft Learn APIला कोर्सेसची यादी मिळविण्यासाठी कॉल करणार्या फंक्शनला परिभाषित करू:

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

   लक्षात घ्या की आम्ही आता एक वास्तविक Python फंक्शन तयार करतो जे `functions` variable. We're also making real external API calls to fetch the data we need. In this case, we go against the Microsoft Learn API to search for training modules.

Ok, so we created `functions` variables and a corresponding Python function, how do we tell the LLM how to map these two together so our Python function is called?

1. To see if we need to call a Python function, we need to look into the LLM response and see if `function_call` मध्ये दर्शविलेल्या फंक्शन नावांना नकाशा करते आणि ते भाग आहे आणि दर्शविलेल्या फंक्शनला कॉल करते. खाली आपण उल्लेख केलेला तपासणी कसा करू शकता ते येथे आहे:

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

   या तीन ओळी, फंक्शनचे नाव, तर्कसंगत गोष्टी काढणे आणि कॉल करणे सुनिश्चित करतात:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   खाली आमचा कोड चालवण्याचे आउटपुट आहे:

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

1. आता आम्ही अद्ययावत संदेश `messages` LLMला पाठवू जेणेकरून आम्ही API JSON स्वरूपित प्रतिसादाऐवजी नैसर्गिक भाषा प्रतिसाद प्राप्त करू शकू.

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

Azure OpenAI फंक्शन कॉलिंगचे शिक्षण सुरू ठेवण्यासाठी आपण तयार करू शकता:

- फंक्शनचे अधिक पॅरामीटर्स जे शिकणाऱ्यांना अधिक कोर्स शोधण्यात मदत करू शकतात.
- दुसरा फंक्शन कॉल तयार करा जो शिकणाऱ्याच्या मातृभाषेसारखी अधिक माहिती घेईल.
- जेव्हा फंक्शन कॉल आणि/किंवा API कॉल कोणतेही योग्य कोर्स परत करत नाही तेव्हा त्रुटी हाताळणी तयार करा.

सूचना: [Learn API संदर्भ दस्तऐवजीकरण](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) पृष्ठाचे अनुसरण करा जेणेकरून आपण पाहू शकता की डेटा कसा आणि कुठे उपलब्ध आहे.

## उत्कृष्ट काम! प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [जनरेटिव AI लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) वर जा आणि आपल्या जनरेटिव AI ज्ञानाची पातळी वाढवा!

पाठ 12 मध्ये जा, जिथे आपण AI अनुप्रयोगांसाठी UX कसे [डिझाइन करायचे](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ते पाहू!

**अस्वीकृती**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अपूर्णता असू शकते. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरातून उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.