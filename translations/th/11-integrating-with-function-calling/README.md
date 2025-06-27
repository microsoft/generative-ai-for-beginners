<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-06-25T19:54:43+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "th"
}
-->
# การรวมเข้ากับการเรียกฟังก์ชัน

คุณได้เรียนรู้มาพอสมควรจากบทเรียนก่อนหน้านี้ แต่เราสามารถพัฒนาเพิ่มเติมได้ สิ่งที่เราควรพิจารณาคือการทำให้รูปแบบการตอบสนองมีความสม่ำเสมอมากขึ้น เพื่อให้ง่ายต่อการทำงานกับการตอบสนองในขั้นตอนต่อไป นอกจากนี้ เราอาจต้องการเพิ่มข้อมูลจากแหล่งอื่นเพื่อเพิ่มคุณค่าของแอปพลิเคชันของเรา

ปัญหาที่กล่าวมาข้างต้นคือสิ่งที่บทนี้ต้องการแก้ไข

## บทนำ

บทเรียนนี้จะครอบคลุมถึง:

- อธิบายว่า Function Calling คืออะไรและกรณีการใช้งาน
- การสร้างการเรียกฟังก์ชันโดยใช้ Azure OpenAI
- วิธีการรวมการเรียกฟังก์ชันเข้ากับแอปพลิเคชัน

## เป้าหมายการเรียนรู้

เมื่อสิ้นสุดบทเรียนนี้ คุณจะสามารถ:

- อธิบายวัตถุประสงค์ของการใช้ Function Calling
- ตั้งค่าการเรียกฟังก์ชันโดยใช้ Azure OpenAI Service
- ออกแบบการเรียกฟังก์ชันที่มีประสิทธิภาพสำหรับกรณีการใช้งานของแอปพลิเคชันของคุณ

## สถานการณ์: ปรับปรุงแชทบอทของเราด้วยฟังก์ชัน

สำหรับบทเรียนนี้ เราต้องการสร้างฟีเจอร์สำหรับสตาร์ทอัพด้านการศึกษาของเราที่อนุญาตให้ผู้ใช้ใช้แชทบอทเพื่อค้นหาคอร์สเทคนิค เราจะแนะนำคอร์สที่เหมาะกับระดับทักษะ บทบาทปัจจุบัน และเทคโนโลยีที่สนใจ

เพื่อทำให้สถานการณ์นี้สมบูรณ์ เราจะใช้การผสมผสานของ:

- `Azure OpenAI` เพื่อสร้างประสบการณ์การแชทสำหรับผู้ใช้
- `Microsoft Learn Catalog API` เพื่อช่วยผู้ใช้ค้นหาคอร์สตามคำร้องขอของผู้ใช้
- `Function Calling` เพื่อรับคำถามของผู้ใช้และส่งไปยังฟังก์ชันเพื่อทำการเรียก API

เริ่มต้นด้วยการดูว่าทำไมเราถึงต้องการใช้การเรียกฟังก์ชันตั้งแต่แรก:

## ทำไมต้องใช้ Function Calling

ก่อนการเรียกฟังก์ชัน การตอบสนองจาก LLM ไม่มีโครงสร้างและไม่สม่ำเสมอ นักพัฒนาจำเป็นต้องเขียนโค้ดตรวจสอบความถูกต้องที่ซับซ้อนเพื่อให้แน่ใจว่าสามารถจัดการกับแต่ละรูปแบบของการตอบสนองได้ ผู้ใช้ไม่สามารถได้รับคำตอบเช่น "สภาพอากาศปัจจุบันในสต็อกโฮล์มเป็นอย่างไร?" นี่เป็นเพราะโมเดลถูกจำกัดอยู่กับเวลาที่ข้อมูลถูกฝึกฝน

Function Calling เป็นคุณสมบัติของ Azure OpenAI Service ที่ช่วยแก้ไขข้อจำกัดดังต่อไปนี้:

- **รูปแบบการตอบสนองที่สม่ำเสมอ** หากเราสามารถควบคุมรูปแบบการตอบสนองได้ดีขึ้น เราสามารถรวมการตอบสนองเข้ากับระบบอื่นๆ ได้ง่ายขึ้น
- **ข้อมูลภายนอก** ความสามารถในการใช้ข้อมูลจากแหล่งอื่นของแอปพลิเคชันในบริบทของการแชท

## การแสดงปัญหาผ่านสถานการณ์

> เราแนะนำให้คุณใช้ [notebook ที่รวมไว้](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) หากคุณต้องการเรียกใช้สถานการณ์ด้านล่าง คุณยังสามารถอ่านตามได้เมื่อเราพยายามแสดงปัญหาที่ฟังก์ชันสามารถช่วยแก้ไขได้

มาดูตัวอย่างที่แสดงปัญหารูปแบบการตอบสนอง:

สมมติว่าเราต้องการสร้างฐานข้อมูลของข้อมูลนักเรียนเพื่อที่เราจะสามารถแนะนำคอร์สที่เหมาะสมให้พวกเขาได้ ด้านล่างเรามีคำอธิบายของนักเรียนสองคนที่มีข้อมูลคล้ายคลึงกันมาก

1. สร้างการเชื่อมต่อกับทรัพยากร Azure OpenAI ของเรา:

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

   ด้านล่างเป็นโค้ด Python สำหรับการกำหนดค่าการเชื่อมต่อกับ Azure OpenAI ซึ่งเราตั้งค่า `api_type`, `api_base`, `api_version` and `api_key`.

1. Creating two student descriptions using variables `student_1_description` and `student_2_description`

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   เราต้องการส่งคำอธิบายนักเรียนข้างต้นไปยัง LLM เพื่อแยกวิเคราะห์ข้อมูล ข้อมูลนี้สามารถใช้ในแอปพลิเคชันของเราและส่งไปยัง API หรือเก็บไว้ในฐานข้อมูลได้ในภายหลัง

1. มาสร้างพรอมต์สองแบบที่เหมือนกันซึ่งเราสั่งให้ LLM ว่าเราสนใจข้อมูลอะไร:

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

   พรอมต์ข้างต้นสั่งให้ LLM สกัดข้อมูลและส่งคืนการตอบสนองในรูปแบบ JSON

1. หลังจากตั้งค่าพรอมต์และการเชื่อมต่อกับ Azure OpenAI แล้ว เราจะส่งพรอมต์ไปยัง LLM โดยใช้ `openai.ChatCompletion`. We store the prompt in the `messages` variable and assign the role to `user` เพื่อเลียนแบบข้อความจากผู้ใช้ที่ถูกเขียนไปยังแชทบอท

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

ตอนนี้เราสามารถส่งคำขอทั้งสองไปยัง LLM และตรวจสอบการตอบสนองที่เราได้รับโดยค้นหาเช่นนี้ `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we can convert the response to JSON format by calling `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   การตอบสนอง 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   การตอบสนอง 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   แม้ว่าพรอมต์จะเหมือนกันและคำอธิบายจะคล้ายคลึงกัน แต่เราก็เห็นค่าของ `Grades` property formatted differently, as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.th.png)

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

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.th.png)

### Step 1 - creating messages

The first step is to create a user message. This can be dynamically assigned by taking the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message.

The `role` can be either `system` (creating rules), `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` และตัวอย่างคำถาม

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

โดยการกำหนดบทบาทที่แตกต่างกัน จะทำให้ LLM เข้าใจได้ว่ามันเป็นระบบที่พูดบางอย่างหรือผู้ใช้ ซึ่งช่วยสร้างประวัติการสนทนาที่ LLM สามารถสร้างต่อไปได้

### ขั้นตอนที่ 2 - การสร้างฟังก์ชัน

ถัดไป เราจะกำหนดฟังก์ชันและพารามิเตอร์ของฟังก์ชันนั้น เราจะใช้ฟังก์ชันเพียงฟังก์ชันเดียวที่นี่ที่เรียกว่า `search_courses` but you can create multiple functions.

> **Important** : Functions are included in the system message to the LLM and will be included in the amount of available tokens you have available.

Below, we create the functions as an array of items. Each item is a function and has properties `name`, `description` and `parameters`:

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

มาดูรายละเอียดของแต่ละอินสแตนซ์ฟังก์ชันด้านล่าง:

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

Here's some code below where we call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` และให้ LLM เลือกว่าจะเรียกฟังก์ชันเมื่อใดที่เรามอบให้:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

การตอบสนองที่กลับมาตอนนี้มีลักษณะดังนี้:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

ที่นี่เราสามารถเห็นว่าฟังก์ชัน `search_courses` was called and with what arguments, as listed in the `arguments` property in the JSON response.

The conclusion the LLM was able to find the data to fit the arguments of the function as it was extracting it from the value provided to the `messages` parameter in the chat completion call. Below is a reminder of the `messages` ค่า:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

ตามที่คุณเห็น `student`, `Azure` and `beginner` was extracted from `messages` and set as input to the function. Using functions this way is a great way to extract information from a prompt but also to provide structure to the LLM and have reusable functionality.

Next, we need to see how we can use this in our app.

## Integrating Function Calls into an Application

After we have tested the formatted response from the LLM, we can now integrate this into an application.

### Managing the flow

To integrate this into our application, let's take the following steps:

1. First, let's make the call to the OpenAI services and store the message in a variable called `response_message`

   ```python
   response_message = response.choices[0].message
   ```

1. ตอนนี้เราจะกำหนดฟังก์ชันที่จะเรียก Microsoft Learn API เพื่อรับรายการคอร์ส:

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

   สังเกตว่าเราสร้างฟังก์ชัน Python จริงที่แมปกับชื่อฟังก์ชันที่นำเสนอใน `functions` variable. We're also making real external API calls to fetch the data we need. In this case, we go against the Microsoft Learn API to search for training modules.

Ok, so we created `functions` variables and a corresponding Python function, how do we tell the LLM how to map these two together so our Python function is called?

1. To see if we need to call a Python function, we need to look into the LLM response and see if `function_call` เป็นส่วนหนึ่งของมันและเรียกฟังก์ชันที่ชี้ไว้ นี่คือวิธีที่คุณสามารถทำการตรวจสอบที่กล่าวถึงด้านล่าง:

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

   สามบรรทัดนี้ทำให้แน่ใจว่าเราสกัดชื่อฟังก์ชัน อาร์กิวเมนต์ และทำการเรียก:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   ด้านล่างคือผลลัพธ์จากการรันโค้ดของเรา:

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

1. ตอนนี้เราจะส่งข้อความที่อัปเดต `messages` ไปยัง LLM เพื่อให้เราได้รับการตอบสนองภาษาธรรมชาติแทนการตอบสนองที่มีรูปแบบ API JSON

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

## การมอบหมายงาน

เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับ Azure OpenAI Function Calling คุณสามารถสร้าง:

- พารามิเตอร์เพิ่มเติมของฟังก์ชันที่อาจช่วยให้ผู้เรียนค้นหาคอร์สเพิ่มเติม
- สร้างการเรียกฟังก์ชันอื่นที่รับข้อมูลเพิ่มเติมจากผู้เรียนเช่นภาษาพื้นเมืองของพวกเขา
- สร้างการจัดการข้อผิดพลาดเมื่อการเรียกฟังก์ชันและ/หรือการเรียก API ไม่ส่งคืนคอร์สที่เหมาะสม

คำแนะนำ: ทำตามหน้าข้อมูลอ้างอิงของ [Learn API](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) เพื่อดูว่าข้อมูลนี้มีอยู่ที่ไหนและอย่างไร

## งานดี! เดินทางต่อไป

หลังจากจบบทเรียนนี้ ลองดูคอลเล็กชัน [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อยกระดับความรู้ด้าน Generative AI ของคุณ!

ไปที่บทเรียนที่ 12 ซึ่งเราจะดูวิธี [ออกแบบ UX สำหรับแอปพลิเคชัน AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปล AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อให้ได้ความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญแนะนำให้ใช้การแปลโดยมนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้