# 第十一章：为生成式 AI 添加 function calling

[![Integrating with function calling](../../images/11-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

到目前为止，您在之前的章节中已经学到了相当多的知识。 然而，我们可以进一步改进。 可以解决的一些问题是如何获得更一致的响应格式，以便更轻松地处理下游响应。 此外，我们可能希望添加来自其他来源的数据以进一步丰富我们的应用程序。

上述问题正是本章要解决的问题。

## 本章概述

在本章中，您将学习到:

- 解释什么是 function calling 及其用例。
- 使用 Azure OpenAI 创建 function calling。
- 如何将 function calling 集成到应用程序中。

## 学习目标

在完成本章的学习，您将能够：

- 解释使用 function calling 的目的。
- 使用 Azure OpenAI Service 设置 function calling 。
- 为您的应用程序用例设计有效的 function calling 。
  。

## 场景：通过功能改进我们的聊天机器人

在本课程中，我们希望为 "Our Startup" 构建一个功能，允许用户使用聊天机器人来查找技术课程。 我们将推荐适合他们的技能水平、当前角色和感兴趣的技术的课程。

为了完成这个场景，我们将使用以下组合：

- “Azure Open AI” 为用户创建聊天体验。
- “Microsoft Learn Catalog API” 帮助用户根据用户的请求查找课程。
- “Function Calling” 接受用户的查询并将其发送到相关函数以发出 API 请求。

首先，让我们看看为什么我们要首先使用 Function Calling：

## 为什么需要 Function Calling

在函数调用之前，LLMs 的回复是非结构化且不一致的。 开发人员需要编写复杂的验证代码，以确保他们能够处理响应的每种变化。 用户无法获得诸如“斯德哥尔摩现在的天气怎么样？”之类的答案。 这是因为模型局限于数据训练的时间。

Function Calling 是 Azure Open AI Service 的一项功能，旨在克服以下限制：

- **一致的响应格式**。 如果我们能够更好地控制响应格式，我们就可以更轻松地将响应下游集成到其他系统。
- **外部数据**。 能够在聊天上下文中使用应用程序其他来源的数据

## 通过场景说明问题

> 如果您想运行以下场景，我们建议您创建一个文件 _Notebook.ipynb_ 并将以下代码粘贴到单独的代码单元格中。 您也可以继续阅读，因为我们正在尝试说明函数可以帮助解决问题的问题。

让我们看一下说明响应格式问题的示例：

假设我们想要创建一个学生数据数据库，以便我们可以向他们建议正确的课程。 下面我们有两个对学生的描述，它们所包含的数据非常相似。

1. 创建与我们的 Azure OpenAI 资源的连接：

   ```python
   import os
   import openai
   import json
   openai.api_type = "azure"
   openai.api_base = "YOUR OPENAI API BASE URL"
   openai.api_version = "2023-07-01-preview"
   openai.api_key = os.getenv("OPENAI_API_KEY")
   ```

   Below is some Python code for configuring our connection to Azure Open AI where we set `api_type`, `api_base`, `api_version` and `api_key`.

2. 使用变量 'student_1_description' 和 'student_2_description' 创建两个学生描述。

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   We want to send the above student descriptions to an LLM to parse the data. This data can later be used in our application and be sent to an API or stored in a database.

3. 让我们创建两个相同的提示，指引 LLM 给我们指出哪些兴趣点：

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

   上述提示指示 LLM 提取信息并以 JSON 格式返回响应。

4. 设置提示并连接到 Azure OpenAI 后，我们现在将使用 `openai.ChatCompletion` 将提示发送到 LLM。 我们将提示存储在 `messages` 变量中，并将角色分配给 `user`.。 这是为了模仿用户写入聊天机器人的消息。

   ```python
   # response from prompt one
   openai_response1 = openai.ChatCompletion.create(
     engine="gpt-function",
     messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1['choices'][0]['message']['content']

   # response from prompt two
   openai_response2 = openai.ChatCompletion.create(
     engine="gpt-function",
     messages = [{'role': 'user', 'content': prompt2 }]
   )
   openai_response2['choices'][0]['message']['content']
   ```

现在我们可以将两个请求发送到 LLM 并通过查找 `openai_response1['choices'][0]['message']['content']` 来检查我们收到的响应。

1. 最后，我们可以通过调用 `json.loads` 将响应结果转换为 JSON 格式：

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1['choices'][0]['message']['content'])
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

   尽管提示相同且描述相似，但我们看到 `Grades` 属性值的格式不同，例如有时我们可以获得“3.7”或“3.7 GPA”格式。

   这个结果是因为 LLM 以书面提示的形式获取非结构化数据并返回非结构化数据。 我们需要有一个结构化的格式，以便我们知道在存储或使用这些数据时会发生什么

那么我们该如何解决格式化问题呢？ 通过使用 function calling，我们可以确保收到返回的结构化数据。 当使用 function calling 时，LLM 实际上并不调用或运行任何函数。 相反，我们为 LLMs 创建了一个响应结构。 然后，我们使用这些结构化响应来了解要在应用程序中运行哪些功能。.

![function flow](../../images/Function-Flow.png?WT.mc_id=academic-105485-koreyst)

然后我们可以获取函数返回的内容并将其发送回 LLM。 然后， LLM 将使用自然语言来回答用户的查询。

## 使用 function calling 的用例

在许多不同的用例中，function calling 可以改进您的应用程序，例如：

- **调用外部工具**。 聊天机器人非常擅长回答用户的问题。 通过使用函数调用，聊天机器人可以使用来自用户的消息来完成某些任务。 例如，学生可以要求聊天机器人“向我的老师发送电子邮件，说我需要有关该主题的更多帮助”。 这可以对 'send_email(to: string, body: string)' 进行函数调用

- **创建 API 或数据库查询**。 用户可以使用自然语言查找信息，并将其转换为格式化查询或 API 请求。 举个例子，老师请求“谁是完成最后作业的学生”，该老师可以调用名为 'get_completed(student_name: string, assignment: int, current_status: string)' 的函数

- **创建结构化数据**。 用户可以获取一段文本或 CSV 并使用 LLM 从中提取重要信息。 例如，学生可以将有关和平协议的维基百科文章转换为创建人工智能闪存卡。 这可以通过使用名为 'get_important_facts（agreement_name：string，date_signed：string，partys_involved：list）' 的函数来完成

## 创建您的第一个 function calling

创建 function calling 的过程包括 3 个主要步骤：

1. **调用** Chat Completions API，并提供您的函数列表和用户消息。
2. **读取**模型的响应以执行操作，即执行函数或 API 调用。
3. **使用**函数的响应再次调用 Chat Completions API，以使用该信息创建对用户的响应。

![LLM Flow](../../images/LLM-Flow.png?WT.mc_id=academic-105485-koreyst)

### Step 1 - 创建消息

Step 1 是创建用户消息。 这可以通过获取文本输入的值来动态分配，或者您可以在此处分配一个值。 如果这是您第一次使用聊天完成 API，我们需要定义消息的“角色”和“内容”。

`role` 可以是`system` （创建规则）、`assistant` 模型）或`user`最终用户）。 对于函数调用，我们将其指定为 `user` 和一个示例问题。

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

通过分配不同的角色， LLMs 可以清楚地知道是系统在说话还是用户在说话，这有助于建立 LLMs 可以建立的对话历史记录。

### Step 2 - 创建 functions

接下来，我们将定义一个函数以及该函数的参数。 我们在这里仅使用一个名为“search_courses”的函数，但您可以创建多个函数。

> **重要**：功能包含在发给 LLM 的系统消息中，并将包含在您拥有的可用 tokens 数量中。

下面，我们将函数创建为项目数组。 每个项目都是一个函数，并具有属性 `name`, `description` 和 `parameters`：

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

下面让我们更详细地描述每个函数实例：

- `name` - 我们想要调用的函数的名称。
- `description` - 这是函数如何工作的描述。 在这里，重要的是要具体和清晰。
- `parameters` - 您希望模型在其响应中生成的值和格式的列表。 参数数组由项目组成，其中项目具有以下属性：
  1. `type` - 将存储属性的数据类型。
  2. `properties` - 模型将用于其响应的特定值的列表
     1. `name` - 键是模型将在其格式化响应中使用的属性的名称，例如，`product`。
     2. `type` - 该属性的数据类型，例如，`string`。
     3. `description` - 特定属性的描述。

还有一个可选属性“required” - 完成 function call 所需的属性。

### Step 3 - 进行 function call

定义函数后，我们现在需要将其包含在对聊天完成 API 的调用中。 我们通过向请求添加 `functions` 来做到这一点。 在这种情况下 `functions=functions`。

还有一个选项可以将“function_call”设置为“auto”。 这意味着我们将让 LLM 根据用户消息决定应该调用哪个函数，而不是我们自己分配它。

下面是我们调用 `ChatCompletion.create` 的一些代码，请注意我们如何设置 `functions=functions` 和 `function_call="auto"` ，从而让 LLM 选择何时调用我们提供的函数：

```python
response = openai.ChatCompletion.create( engine="gpt-function",
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto", )

print(response['choices'][0]['message'])
```

现在返回的响应结果如下所示：

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

在这里，我们可以看到如何调用函数 `search_courses` 以及使用哪些参数，如 JSON 响应中的 `arguments` 属性中所列。

结论是，LLMs 能够找到适合函数参数的数据，因为它从聊天完成调用中提供给“messages”参数的值中提取数据。 下面是“messages”值的提醒：

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

如您所见，`student`, `Azure` 和 `beginner` 是从`messages` 中提取的，并设置为函数的输入。 以这种方式使用函数是从提示中提取信息的好方法，同时也可以为 LLM 提供结构并具有可重用的功能。

接下来，我们需要看看如何在我们的应用程序中使用它。

## 将 function calling 集成到应用程序中

在我们测试了 LLM 的格式化响应后，现在我们可以将其集成到应用程序中。

### 管理流程

要将其集成到我们的应用程序中，我们需要执行以下步骤：

1. 首先，我们调用 Open AI 服务并将消息存储在名为 `response_message` 的变量中。

   ```python
   response_message = response["choices"][0]["message"]
   ```

2. 现在我们将定义调用 Microsoft Learn API 来获取课程列表的函数：

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

   请注意我们现在如何创建一个实际的 Python 函数，该函数映射到 `functions` 变量中引入的函数名称。 我们还进行真正的外部 API 调用来获取我们需要的数据。 在这种情况下，我们根据 Microsoft Learn API 来搜索培训模块。

   好的，我们创建了 `functions` 变量和相应的 Python 函数，我们如何告诉 LLM 如何将这两个映射在一起，以便调用我们的 Python 函数？

3. 要查看是否需要调用 Python 函数，我们需要查看 LLM 响应并查看“function_call”是否是其中的一部分并调用所指出的函数。 以下是进行下面提到的检查的方法：

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

   These three lines, ensure we extract the function name, the arguments and make the call:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message["function_call"]["arguments"])
   function_response = function_to_call(**function_args)
   ```

   以下是运行代码的输出：

   **Output**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/en-us/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/en-us/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/en-us/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/en-us/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

4. 现在我们将向 LLM 发送更新后的消息 `messages` ，以便我们可以接收自然语言响应，而不是 API JSON 格式的响应。

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
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## 作业

要继续学习 Azure 开放 AI function calling，您可以构建：

- 该功能的更多参数可以帮助学习者找到更多课程。 您可以在此处找到可用的 API 参数：
- 创建另一个函数调用，从学习者那里获取更多信息，例如他们的母语
- 当函数调用和/或 API 调用未返回任何合适的课程时创建错误处理

  提示：按照 [Learn API 参考文档](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) 页面了解此操作的方式和和哪些数据是可用的

## Great Work! Continue the Journey

## 继续学习

想要了解有关 Function Calling 的更多信息？ 转至[进阶学习的页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 查找有关此主章节的其他学习资源。

前往第十二章，我们将学习 [为人工智能应用程序添加用户体验](../../../12-designing-ux-for-ai-applications/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)!
