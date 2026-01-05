<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-11-12T08:53:31+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "pcm"
}
-->
# How to join function call

[![How to join function call](../../../translated_images/11-lesson-banner.d78860d3e1f041e2.pcm.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

You don learn plenty things for di previous lessons. But we fit still improve am. Some things we fit look into na how we fit get response wey dey consistent so e go easy to work with di response later. Plus, we fit wan add data from other places to make our app better.

Na di problems wey we mention above dis chapter wan solve.

## Introduction

Dis lesson go cover:

- Wetin function call be and di kain things we fit use am do.
- How to create function call with Azure OpenAI.
- How to join function call inside app.

## Learning Goals

By di end of dis lesson, you go sabi:

- Explain why we dey use function call.
- Setup Function Call with Azure OpenAI Service.
- Design better function calls for di kain things wey your app dey do.

## Scenario: Make our chatbot better with functions

For dis lesson, we wan build one feature for our education startup wey go allow users use chatbot to find technical courses. We go recommend courses wey match their skill level, current role, and di technology wey dem dey interested in.

To finish dis scenario, we go use:

- `Azure OpenAI` to create chat experience for di user.
- `Microsoft Learn Catalog API` to help users find courses based on wetin dem dey ask.
- `Function Calling` to take di user's query and send am to one function to make di API request.

Make we start by looking why we go wan use function call first:

## Why Function Calling

Before function call, di response wey LLM dey give no dey structured and e dey inconsistent. Developers go need write plenty validation code to make sure say dem fit handle di different kain response wey dem dey get. Users no fit get answers like "Wetin be di current weather for Stockholm?". Dis na because di models dey limited to di time wey dem train di data.

Function Calling na one feature for Azure OpenAI Service wey dey help solve dis problems:

- **Consistent response format**. If we fit control di response format well, e go easy to join di response with other systems later.
- **External data**. E go allow us use data from other places for di app inside chat.

## Show di problem with one scenario

> We dey recommend make you use di [notebook wey dey here](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) if you wan run di scenario wey dey below. You fit also just read am as we dey try show di problem wey functions fit help solve.

Make we look di example wey dey show di response format problem:

Make we say we wan create one database of student data so we fit suggest di correct course to dem. Below we get two descriptions of students wey dey similar for di data wey dem contain.

1. Create connection to our Azure OpenAI resource:

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

   Below na Python code wey dey configure our connection to Azure OpenAI where we set `api_type`, `api_base`, `api_version` and `api_key`.

1. Create two student descriptions using variables `student_1_description` and `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   We wan send di student descriptions above to LLM to parse di data. Dis data fit later dey used for our app and fit dey sent to API or stored inside database.

1. Make we create two prompts wey dey identical where we dey tell di LLM wetin we wan make e extract:

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

   Di prompts above dey tell di LLM to extract information and return di response for JSON format.

1. After we don set di prompts and di connection to Azure OpenAI, we go now send di prompts to di LLM by using `openai.ChatCompletion`. We go store di prompt inside di `messages` variable and assign di role to `user`. Dis na to act like message wey user dey write to chatbot.

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

Now we fit send di two requests to di LLM and check di response wey we receive by finding am like dis `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we fit change di response to JSON format by calling `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Response 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Response 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Even though di prompts dey di same and di descriptions dey similar, we dey see di values for di `Grades` property dey formatted differently, like `3.7` or `3.7 GPA`.

   Dis result na because di LLM dey take unstructured data for di written prompt and e dey return unstructured data too. We need structured format so we go sabi wetin to expect when we dey store or use di data.

So how we go solve di formatting problem? By using functional calling, we fit make sure say we dey receive structured data back. When we dey use function calling, di LLM no dey actually call or run any function. Instead, we dey create structure for di LLM to follow for di responses. We go then use di structured responses to sabi wetin function to run for our apps.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb.pcm.png)

We fit then take wetin di function return and send am back to di LLM. Di LLM go then respond using natural language to answer di user's query.

## Use Cases for using function calls

Plenty different use cases dey where function calls fit make your app better like:

- **Calling External Tools**. Chatbots dey good for answering questions from users. By using function calling, di chatbots fit use messages from users to complete certain tasks. For example, student fit ask chatbot "Send email to my instructor say I need more help for dis subject". Dis fit make function call to `send_email(to: string, body: string)`

- **Create API or Database Queries**. Users fit find information using natural language wey go change to formatted query or API request. Example fit be teacher wey dey ask "Who be di students wey finish di last assignment" wey fit call function wey dem name `get_completed(student_name: string, assignment: int, current_status: string)`

- **Creating Structured Data**. Users fit take block of text or CSV and use di LLM to extract di important information from am. For example, student fit change Wikipedia article about peace agreements to create AI flashcards. Dis fit happen by using function wey dem call `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## How to Create Your First Function Call

Di process to create function call get 3 main steps:

1. **Call** di Chat Completions API with list of your functions and user message.
2. **Read** di model response to do action like run function or API Call.
3. **Make** another call to Chat Completions API with di response from your function to use di information to create response for di user.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7.pcm.png)

### Step 1 - create messages

Di first step na to create user message. Dis fit dey assigned dynamically by taking di value of text input or you fit assign value here. If dis na your first time to work with Chat Completions API, we need to define di `role` and di `content` of di message.

Di `role` fit be `system` (create rules), `assistant` (di model) or `user` (di end-user). For function calling, we go assign am as `user` and example question.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

By assigning different roles, e dey clear to di LLM if na di system dey talk or di user, wey dey help build conversation history wey di LLM fit use.

### Step 2 - create functions

Next, we go define one function and di parameters of di function. We go use just one function here wey dem call `search_courses` but you fit create plenty functions.

> **Important** : Functions dey included for di system message to di LLM and go dey count for di amount of tokens wey you get.

Below, we dey create di functions as array of items. Each item na one function and e get properties `name`, `description` and `parameters`:

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

Make we explain each function instance more:

- `name` - Di name of di function wey we wan make e dey called.
- `description` - Dis na di description of how di function dey work. E dey important to dey clear and specific here.
- `parameters` - List of values and format wey you wan make di model produce for di response. Di parameters array get items wey get di following properties:
  1.  `type` - Di data type wey di properties go dey stored in.
  1.  `properties` - List of di specific values wey di model go use for di response
      1. `name` - Di key na di name of di property wey di model go use for di formatted response, like `product`.
      1. `type` - Di data type of dis property, like `string`.
      1. `description` - Description of di specific property.

E get optional property `required` - required property for di function call to complete.

### Step 3 - Make di function call

After we don define function, we go now need include am for di call to di Chat Completion API. We go do dis by adding `functions` to di request. For dis case `functions=functions`.

E get option to set `function_call` to `auto`. Dis mean we go allow di LLM decide which function e go call based on di user message instead of assigning am ourselves.

Here na code below where we dey call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` and allow di LLM choose when to call di functions we provide:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Di response wey dey come back now go look like dis:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Here we dey see how di function `search_courses` dey called and di arguments wey e use, as e dey listed for di `arguments` property for di JSON response.

Di conclusion na say di LLM fit find di data to match di arguments of di function as e dey extract am from di value wey dey provided to di `messages` parameter for di chat completion call. Below na reminder of di `messages` value:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

As you dey see, `student`, `Azure` and `beginner` dey extracted from `messages` and set as input to di function. To use functions like dis na better way to extract information from prompt but also to provide structure to di LLM and get reusable functionality.

Next, we go see how we fit use dis for our app.

## How to Join Function Calls Inside App

After we don test di formatted response from di LLM, we fit now join dis inside app.

### Manage di flow

To join dis inside our app, make we take di following steps:

1. First, make we call di OpenAI services and store di message inside variable wey dem call `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Now we go define di function wey go call di Microsoft Learn API to get list of courses:

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

   Note how we dey now create real Python function wey match di function names wey dey di `functions` variable. We dey also make real external API calls to get di data we need. For dis case, we dey go against di Microsoft Learn API to search for training modules.

Ok, so we don create `functions` variables and di Python function wey match am, how we go tell di LLM how to match di two together so our Python function go dey called?

1. To see if we need call Python function, we need check di LLM response and see if `function_call` dey part of am and call di function wey e point out. Here na how you fit make di check below:

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

   Dis three lines, dey make sure say we extract di function name, di arguments and make di call:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Below na di output from running our code:

   **Output**

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

1. Now we go send di updated message, `messages` to di LLM so we fit receive natural language response instead of API JSON formatted response.

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

   **Output**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Assignment

To continue your learning of Azure OpenAI Function Calling you fit build:

- Add more parameters for di function wey fit help learners find more courses.
- Create another function call wey go take more information from di learner like di language wey dem dey speak.
- Make error handling for when di function call and/or API call no return any correct courses

Hint: Check di [Learn API reference documentation](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) page to see how and where dis data dey available.

## Good Job! Continue di Journey

After you finish dis lesson, go check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more about Generative AI!

Go Lesson 12, where we go talk about how to [design UX for AI applications](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->