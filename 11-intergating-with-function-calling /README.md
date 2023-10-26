![](./images/genai_course_11[90].png)

**Video Coming Soon** 
## Introduction 

This lesson will cover: 
- What is function calling and its use cases 
- How to create a function call using Azure OpenAI 
- How to integrate a function call into an application 

## Learning Goals 

After completing this lesson you will know how to and understand: 

-  The purpose of using function calling 
- Setup Function Call using the Azure Open AI Service 
- Design effective function calls for your applications use case 


## Understanding Function Calls 

For this lesson, we want to build a feature for our education startup that allows users to use a chatbot to find technical courses. We will recommend courses that fit their skill level, current role and technology of interest. 

To complete this we will use a combination of: 
 - `Azure Open AI` to create a chat experience for the user
 - `Microsoft Learn Catalog API` to help users find courses based on the request of the user 
 - `Function Calling` to take the user's query and send it to a function to make the API request. 

To get started, let's look at why we would want to use function calling in the first place: 

### Why Function Calling 

If you have completed any other lesson in this course, you probably understand the power of using Large Language Models (LLMs). Hopefully you can also see some of their limitations as well. 

Function Calling is a feature of the Azure Open AI Service to overcome to the following limitations: 
1) Consistent response format 
2) Ability to use data from other sources of an application in a chat context 

Before function calling, responses from an LLM were unstructured and inconsistent.  Developers were required to write complex validation code to make sure they are able to handle each variation of a response. 

Users could not get answers like "What is the current weather in Stockholm?". This is because  models were limited to the time the data was trained on. 

Let's look at the example below that illustrates this problem: 

Let's say we want to create a database of student data so we can suggest the right course to them. Below we have two descriptions of students that are very similar in the data they contain.


```python 
student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."
 
student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finshing his studies."

```

We want send this to an LLM to parse the data. This can later be used in our an application to send this to an API or store into a database. 

Let's create two identical prompts that we instruct the LLM on what information that we are interested in: 

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

After creating these two prompts, we will send them to the LLM by using `openai.ChatCompletion`.  We store the prompt in the `messages` variable and assign the role to `user`. This is to mimic a message from a user being written to a chatbot. 

```python 
import os
import openai
import json
openai.api_type = "azure"
openai.api_base = "YOUR OPENAI API BASE URL"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

```


Now we can send both requests to the LLM and examine the response we receive. 
```python 

openai_response1 = openai.ChatCompletion.create(
 engine="gpt-function",    
 messages = [{'role': 'user', 'content': prompt1}]
)
openai_response1['choices'][0]['message']['content'] 

``` 

```python
openai_response2 = openai.ChatCompletion.create(
    engine="gpt-function",
    messages = [{'role': 'user', 'content': prompt2 }]
)
openai_response2['choices'][0]['message']['content'] 

````

```python 
# Loading the response as a JSON object
json_response1 = json.loads(openai_response1['choices'][0]['message']['content'])
json_response1

```

Response 1: 

```json
{'name': 'Emily Johnson',
 'major': 'computer science',
 'school': 'Duke University',
 'grades': '3.7',
 'club': 'Chess Club'}
```

Response 2: 

```json 
{'name': 'Michael Lee',
 'major': 'computer science',
 'school': 'Stanford University',
 'grades': '3.8 GPA',
 'club': 'Robotics Club'}

```


Even though the prompts are the same and the descriptions are similar, we can different formats of the `Grades` property. 

If you run the above cell multiple times, the format can be `3.7` or `3.7 GPA`. 

This is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have structured format so that we know what to expect when storing or using this dat

By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actual call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.  
 
 ![](./images/Function-Flow.png)

We can then take what is returned from the function and send this back to the LLM. The LLM will then respond using natural language to answer the user's query. 

### Use Cases for using function calls 

**Calling External Tools** 
Chatbots are great at providing answers to questions from users. By using function calling, the chatbots can use messages from users to complete certain tasks. For example, a student can ask the chatbot to "Send email to my instructor saying I need more assistance with this subject". This can make a function call to `send_email(to: string, body: string)`


**Create API or Database Queries**
Users can find information using natural language that gets converted into a formatted query or API request. An example of this could be a teacher that request "Who are the students that completed the last assignment" which could call a function named `get_completed(student_name: string, assignment: int, current_status: string)`


**Creating Structured Data**
Users can take the a block of text or CSV and use the LLM to extract important information from it. For example, a student can convert Wikipedia article about peace agreements  to create AI flash cards. This can be done by using a function called  `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## 2. Creating Your First Function Call 

The process of creating a function call includes 3 main steps: 
1. Calling the Chat Completions API with a list of your functions and a user message 
2. Read the model's response to perform an action ie execute a function or API Call 
3. Make another call  to Chat Completions API with the response from your function to use that information to create a response to the user. 

![](./images/LLM-Flow.png)

### Elements of a function call 

#### Users Input 

The first step is to create a user message. This can be dynamically assigned by take the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message. 

The `role` can be either `system` (creating rules) , `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` and an example question. 

```python 
messages= [ {"role": "user", "content": "Find me a good course for a beginner students to learn Azure."} ]
```

### Creating functions

Next we will can define a function and their parameters of that function. We will use just one function here called `search_courses` but you can create multiple functions.

**Important** : Functions are included in thee system message to the LLM and will be included in the amount of available tokens you have available. 

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

**Definitions** 

`name` -  The name of the function that we want to have called. 

`description` - This is the description of how the function works. Here its important to be specific and clear 

`parameters` - A list of values and format that you want the model to produce in its response 


`type` -  The data type of the properties will be stored in 
`properties` - List of the specific values that the model will use for its response 


`name` - the name of the property that model will use in its formatted response 

`type` - The data type of the this property 

`description` - Description of the specific property 


**Optional**

`required` - required property for the function call to be completed 

### Making the function call 
After defining a function, we now need to include it in the call to the Chat Completion API.  We do this by adding `functions` to the request. In this case `functions=functions` 

There is also an option to set `function_call` to `auto`. This means we will let the LLM decide which function should be called based on the user message rather than assigning it ourselves.

```python 
response = openai.ChatCompletion.create( engine="gpt-function", 
                                        messages=messages, 
                                        functions=functions, 
                                        function_call="auto", ) 

print(response['choices'][0]['message'])
```

**Output** 
```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Now let's let's look at the response and see how it is formatted: 

{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}

You can see that the name of the function is called and from the user message, the LLM was able to find the data to fit the arguments of the function. 

## 3.Integrating Function Calls into an Application. 


After we have tested the formatted response from the LLM, now we can integrate this into an application. 

### Managing the flow 

To integrate this into our application, let's take the following steps: 

First, lets make the call to the Open AI services and store the message in a variable called `response_message`. 

```python 
response_message = response["choices"][0]["message"]
```

Now we will define the function that will call the Microsoft Learn API to get a list of courses: 

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

As a best practice, we will then see if the model wants to call a function.  After that, we will create a of the available functions and match it to the function that is being called. 
We will then take the arguments of the function and map them to arguments of from the LLM.

Lastly, we will append the function call message and the values that were returned by the `search_courses` message. This gives the LLM all the information it needs to
respond to the user using natural language. 

```python 
# Check if the model wants to call a function
if response_message.get("function_call"):
    print("Recommended Function call:")
    print(response_message.get("function_call"))
    print()


    # Call the function. 
    function_name = response_message["function_call"]["name"]

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name] 

    function_args = json.loads(response_message["function_call"]["arguments"])
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message["role"],
            "function_call": {
                "name": function_name,
                "arguments": response_message["function_call"]["arguments"],
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

**Output** 
```Recommended Function call:
{
  "name": "search_courses",
  "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
}

Output of function call:
[{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/en-us/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/en-us/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url': 'https://learn.microsoft.com/en-us/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the Rust development environment', 'url': 'https://learn.microsoft.com/en-us/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
<class 'str'> 

```



Now we will send the updated message to the LLM so we can recieve a natural language response instead of an API JSON formatted response. 

```python

print("Messages in next request:")
print(messages)
print()

second_response = openai.ChatCompletion.create(
    messages=messages,
    engine="gpt-function",
    function_call="auto",
    functions=functions,
    temperature=0
        )  # get a new response from GPT where it can see the function response


print(second_response["choices"][0]["message"])

```

**Output** 

```python
{
  "role": "assistant",
  "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography](https://learn.microsoft.com/en-us/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/en-us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/en-us/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/en-us/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/en-us/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
}

```

## Code Challenge 

To continue your learning of Azure Open AI Function Calling you can build:
 - More parameters of the function that might help learners find more courses. You can find the available API parameters here: 
 - Create another function call that takes more information from the learner like their native language 
 - Create error handling on when the function call and/or API call does not return any suitable courses 

 Hint: Follow the [Learn API reference documentation](https://learn.microsoft.com/en-us/training/support/catalog-api-developer-reference) page to see how and where this data is available. 

 ## Great Work! Continue the Journey

Want to learn more about different Function Calling? Go to the [contiuned learning page](../13-continued-learning/README.md) to find other great resources on this topic.


Head over to the Lesson 12 where we will look at how to [design UX for AI applications](/12-designing-ux-for-ai-applications/README.md)!
