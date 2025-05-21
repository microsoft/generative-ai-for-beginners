<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-05-19T21:24:28+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "bn"
}
-->
# ফাংশন কলিংয়ের সাথে একীভূতকরণ

আপনি ইতিমধ্যে আগের পাঠে অনেক কিছু শিখেছেন। তবে, আমরা আরও উন্নতি করতে পারি। কিছু বিষয় যা আমরা সমাধান করতে পারি তা হলো কিভাবে আমরা আরও সামঞ্জস্যপূর্ণ প্রতিক্রিয়া ফরম্যাট পেতে পারি যা প্রতিক্রিয়ার সাথে কাজ করা সহজ করে তোলে। এছাড়াও, আমরা আমাদের অ্যাপ্লিকেশনকে আরও সমৃদ্ধ করতে অন্যান্য উৎস থেকে ডেটা যোগ করতে চাইতে পারি।

উপরোক্ত সমস্যাগুলি এই অধ্যায়ে সমাধান করা হবে।

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- ফাংশন কলিং কী এবং এর ব্যবহার ক্ষেত্র ব্যাখ্যা করা।
- Azure OpenAI ব্যবহার করে একটি ফাংশন কল তৈরি করা।
- কিভাবে একটি অ্যাপ্লিকেশনে ফাংশন কল একীভূত করা যায়।

## শেখার লক্ষ্য

এই পাঠ শেষে, আপনি সক্ষম হবেন:

- ফাংশন কলিংয়ের উদ্দেশ্য ব্যাখ্যা করতে।
- Azure OpenAI সেবা ব্যবহার করে ফাংশন কল সেটআপ করতে।
- আপনার অ্যাপ্লিকেশনের ব্যবহার ক্ষেত্রে কার্যকর ফাংশন কল ডিজাইন করতে।

## দৃশ্যপট: ফাংশনের মাধ্যমে আমাদের চ্যাটবট উন্নত করা

এই পাঠের জন্য, আমরা আমাদের শিক্ষা স্টার্টআপের জন্য একটি ফিচার তৈরি করতে চাই যা ব্যবহারকারীদের চ্যাটবট ব্যবহার করে প্রযুক্তিগত কোর্স খুঁজে পেতে দেয়। আমরা তাদের দক্ষতা স্তর, বর্তমান ভূমিকা এবং আগ্রহের প্রযুক্তির সাথে মিলে যায় এমন কোর্স সুপারিশ করব।

এই দৃশ্যপট সম্পূর্ণ করতে, আমরা একটি সংমিশ্রণ ব্যবহার করব:

- `Azure OpenAI` ব্যবহারকারীর জন্য একটি চ্যাট অভিজ্ঞতা তৈরি করতে।
- `Microsoft Learn Catalog API` ব্যবহারকারীদের অনুরোধের ভিত্তিতে কোর্স খুঁজে পেতে সাহায্য করতে।
- `Function Calling` ব্যবহারকারীর অনুসন্ধান নিয়ে ফাংশনে পাঠিয়ে API অনুরোধ করতে।

শুরু করতে, প্রথমে দেখে নিই কেন আমরা ফাংশন কলিং ব্যবহার করতে চাই:

## কেন ফাংশন কলিং

ফাংশন কলিংয়ের আগে, LLM থেকে প্রতিক্রিয়াগুলি ছিল অসংগঠিত এবং অসমঞ্জস্যপূর্ণ। ডেভেলপারদের প্রতিটি প্রতিক্রিয়ার বৈচিত্র্য পরিচালনা করার জন্য জটিল বৈধতা কোড লিখতে হতো। ব্যবহারকারীরা "স্টকহোমের বর্তমান আবহাওয়া কেমন?" এর মত প্রশ্নের উত্তর পেতে পারত না। কারণ মডেলগুলি ডেটা প্রশিক্ষণের সময় সীমাবদ্ধ ছিল।

ফাংশন কলিং Azure OpenAI সেবার একটি বৈশিষ্ট্য যা নিম্নলিখিত সীমাবদ্ধতাগুলি অতিক্রম করতে সাহায্য করে:

- **সামঞ্জস্যপূর্ণ প্রতিক্রিয়া ফরম্যাট**। যদি আমরা প্রতিক্রিয়া ফরম্যাটটি ভালভাবে নিয়ন্ত্রণ করতে পারি তবে আমরা সহজেই প্রতিক্রিয়াটি অন্যান্য সিস্টেমের সাথে সংহত করতে পারি।
- **বহিরাগত ডেটা**। একটি চ্যাট প্রসঙ্গে অ্যাপ্লিকেশনের অন্যান্য উৎসের ডেটা ব্যবহার করার ক্ষমতা।

## দৃশ্যপটের মাধ্যমে সমস্যার চিত্রায়ন

> আপনি যদি নিচের দৃশ্যটি চালাতে চান তবে আমরা আপনাকে [অন্তর্ভুক্ত নোটবুক](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) ব্যবহার করার পরামর্শ দিই। আপনি শুধুমাত্র পড়তে পারেন যেমন আমরা একটি সমস্যা চিত্রায়ন করার চেষ্টা করছি যেখানে ফাংশনগুলি সমস্যা সমাধানে সাহায্য করতে পারে।

চলুন দেখি উদাহরণটি যা প্রতিক্রিয়া ফরম্যাট সমস্যাটি চিত্রিত করে:

ধরুন আমরা ছাত্রদের ডেটাবেস তৈরি করতে চাই যাতে আমরা তাদের সঠিক কোর্স সুপারিশ করতে পারি। নিচে দুটি ছাত্রের বর্ণনা দেওয়া আছে যেগুলি তাদের অন্তর্ভুক্ত ডেটায় খুবই অনুরূপ।

1. আমাদের Azure OpenAI রিসোর্সের সাথে একটি সংযোগ তৈরি করুন:

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

   নিচে কিছু পাইথন কোড আছে যা আমাদের Azure OpenAI এর সাথে সংযোগ কনফিগার করার জন্য যেখানে আমরা `api_type`, `api_base`, `api_version` and `api_key`.

1. Creating two student descriptions using variables `student_1_description` and `student_2_description` সেট করি।

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   আমরা উপরের ছাত্র বর্ণনাগুলি একটি LLM এ পাঠাতে চাই যাতে ডেটা বিশ্লেষণ করা যায়। এই ডেটা পরে আমাদের অ্যাপ্লিকেশনে ব্যবহার করা যেতে পারে এবং একটি API তে পাঠানো বা একটি ডেটাবেসে সংরক্ষণ করা যেতে পারে।

1. আসুন দুটি অভিন্ন প্রম্পট তৈরি করি যেখানে আমরা LLM কে কোন তথ্যের প্রতি আগ্রহী তা নির্দেশ করি:

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

   উপরের প্রম্পটগুলি LLM কে তথ্য বের করতে এবং JSON ফরম্যাটে প্রতিক্রিয়া ফেরত দিতে নির্দেশ করে।

1. প্রম্পট এবং Azure OpenAI এর সাথে সংযোগ সেটআপ করার পরে, আমরা এখন `openai.ChatCompletion`. We store the prompt in the `messages` variable and assign the role to `user` ব্যবহার করে LLM এ প্রম্পটগুলি পাঠাব। এটি একটি ব্যবহারকারীর কাছ থেকে একটি বার্তা চ্যাটবটে লেখা হচ্ছে এমনটি অনুকরণ করতে।

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

এখন আমরা উভয় অনুরোধ LLM এ পাঠাতে পারি এবং আমরা যে প্রতিক্রিয়া পাই তা পরীক্ষা করতে পারি যেমন `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we can convert the response to JSON format by calling `json.loads` দিয়ে:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   প্রতিক্রিয়া 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   প্রতিক্রিয়া 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   যদিও প্রম্পটগুলি একই এবং বর্ণনাগুলি অনুরূপ, আমরা `Grades` property formatted differently, as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function flow](../../../translated_images/Function-Flow.01a723a374f79e5856d9915c39e16c59fa2a00c113698b22a28e616224f407e1.bn.png)

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

![LLM Flow](../../../translated_images/LLM-Flow.7df9f166be50aa324705f2ccddc04a27cfc7b87e57b1fbe65eb534059a3b8b66.bn.png)

### Step 1 - creating messages

The first step is to create a user message. This can be dynamically assigned by taking the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message.

The `role` can be either `system` (creating rules), `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` এবং একটি উদাহরণ প্রশ্নের মানগুলি দেখতে পাই।

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

বিভিন্ন ভূমিকা বরাদ্দ করে, এটি LLM কে স্পষ্ট করে দেয় যে এটি সিস্টেমের কিছু বলছে বা ব্যবহারকারীর কিছু বলছে, যা LLM এর উপর ভিত্তি করে একটি কথোপকথনের ইতিহাস গড়ে তুলতে সাহায্য করে।

### ধাপ ২ - ফাংশন তৈরি করা

পরবর্তী, আমরা একটি ফাংশন এবং সেই ফাংশনের প্যারামিটারগুলি সংজ্ঞায়িত করব। আমরা এখানে কেবল একটি ফাংশন ব্যবহার করব যা `search_courses` but you can create multiple functions.

> **Important** : Functions are included in the system message to the LLM and will be included in the amount of available tokens you have available.

Below, we create the functions as an array of items. Each item is a function and has properties `name`, `description` and `parameters` নামে পরিচিত:

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

নিচে প্রতিটি ফাংশন উদাহরণ আরও বিস্তারিতভাবে বর্ণনা করা হয়েছে:

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

Here's some code below where we call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` এবং এইভাবে LLM কে আমাদের প্রদত্ত ফাংশনগুলি কখন কল করতে হবে তা নির্ধারণের স্বাধীনতা দেওয়া হয়েছে:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

প্রতিক্রিয়াটি এখন এমনভাবে ফিরে আসে:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

এখানে আমরা দেখতে পারি কিভাবে ফাংশন `search_courses` was called and with what arguments, as listed in the `arguments` property in the JSON response.

The conclusion the LLM was able to find the data to fit the arguments of the function as it was extracting it from the value provided to the `messages` parameter in the chat completion call. Below is a reminder of the `messages` মান:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

যেমন আপনি দেখতে পাচ্ছেন, `student`, `Azure` and `beginner` was extracted from `messages` and set as input to the function. Using functions this way is a great way to extract information from a prompt but also to provide structure to the LLM and have reusable functionality.

Next, we need to see how we can use this in our app.

## Integrating Function Calls into an Application

After we have tested the formatted response from the LLM, we can now integrate this into an application.

### Managing the flow

To integrate this into our application, let's take the following steps:

1. First, let's make the call to the OpenAI services and store the message in a variable called `response_message`।

   ```python
   response_message = response.choices[0].message
   ```

1. এখন আমরা একটি ফাংশন সংজ্ঞায়িত করব যা Microsoft Learn API কে একটি কোর্সের তালিকা পেতে কল করবে:

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

   লক্ষ্য করুন কিভাবে আমরা এখন একটি প্রকৃত পাইথন ফাংশন তৈরি করি যা `functions` variable. We're also making real external API calls to fetch the data we need. In this case, we go against the Microsoft Learn API to search for training modules.

Ok, so we created `functions` variables and a corresponding Python function, how do we tell the LLM how to map these two together so our Python function is called?

1. To see if we need to call a Python function, we need to look into the LLM response and see if `function_call` এর অংশ এবং নির্দেশিত ফাংশনটি কল করি। নিচে আপনি কিভাবে উল্লেখিত যাচাইকরণ করতে পারেন তা দেখানো হয়েছে:

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

   এই তিনটি লাইন নিশ্চিত করে যে আমরা ফাংশনের নাম, আর্গুমেন্টগুলি বের করি এবং কল করি:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   নিচে আমাদের কোড চালানোর আউটপুট দেওয়া হল:

   **আউটপুট**

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

1. এখন আমরা আপডেট করা বার্তা, `messages` LLM এ পাঠাব যাতে আমরা API JSON ফরম্যাটের প্রতিক্রিয়ার পরিবর্তে একটি প্রাকৃতিক ভাষার প্রতিক্রিয়া পেতে পারি।

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

   **আউটপুট**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## নিয়োগ

Azure OpenAI ফাংশন কলিংয়ের আপনার শেখা চালিয়ে যেতে আপনি তৈরি করতে পারেন:

- ফাংশনের আরও প্যারামিটার যা শিক্ষার্থীদের আরও কোর্স খুঁজে পেতে সাহায্য করতে পারে।
- আরও একটি ফাংশন কল তৈরি করুন যা শিক্ষার্থীর স্থানীয় ভাষার মত আরও তথ্য নেয়।
- যখন ফাংশন কল এবং/অথবা API কল কোন উপযুক্ত কোর্স ফেরত দেয় না তখন ত্রুটি পরিচালনা তৈরি করুন।

সংকেত: কিভাবে এবং কোথায় এই ডেটা পাওয়া যায় তা দেখতে [Learn API রেফারেন্স ডকুমেন্টেশন](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) পৃষ্ঠাটি অনুসরণ করুন।

## চমৎকার কাজ! যাত্রা চালিয়ে যান

এই পাঠটি সম্পন্ন করার পরে, আমাদের [Generative AI লার্নিং সংগ্রহ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার Generative AI জ্ঞান আরও উন্নত হয়!

পাঠ ১২-এ যান, যেখানে আমরা দেখব কিভাবে [AI অ্যাপ্লিকেশনের জন্য UX ডিজাইন করা যায়](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**অস্বীকৃতি**:  
এই নথিটি এআই অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় লেখা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকবো না।