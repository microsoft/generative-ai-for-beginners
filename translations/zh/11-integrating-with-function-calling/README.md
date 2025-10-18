<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-17T23:20:54+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "zh"
}
-->
# 集成函数调用

[![集成函数调用](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.zh.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

在之前的课程中，你已经学到了不少内容。然而，我们仍然可以进一步改进。我们可以解决的一些问题包括如何获得更一致的响应格式，以便更容易在后续处理响应。此外，我们可能希望从其他来源添加数据，以进一步丰富我们的应用程序。

上述问题正是本章要解决的内容。

## 简介

本课程将涵盖：

- 解释什么是函数调用及其使用场景。
- 使用 Azure OpenAI 创建函数调用。
- 如何将函数调用集成到应用程序中。

## 学习目标

完成本课程后，你将能够：

- 解释使用函数调用的目的。
- 使用 Azure OpenAI 服务设置函数调用。
- 为你的应用场景设计有效的函数调用。

## 场景：通过函数改进我们的聊天机器人

在本课程中，我们希望为我们的教育初创公司构建一个功能，让用户可以使用聊天机器人找到技术课程。我们将推荐符合他们技能水平、当前角色和感兴趣技术的课程。

为了完成这个场景，我们将结合以下内容：

- 使用 `Azure OpenAI` 为用户创建聊天体验。
- 使用 `Microsoft Learn Catalog API` 帮助用户根据他们的请求找到课程。
- 使用 `Function Calling` 将用户的查询发送到一个函数以发起 API 请求。

首先，让我们看看为什么我们需要使用函数调用：

## 为什么使用函数调用

在使用函数调用之前，LLM 的响应是非结构化且不一致的。开发人员需要编写复杂的验证代码，以确保能够处理每种响应的变化。用户无法获得像“斯德哥尔摩当前天气如何？”这样的答案。这是因为模型仅限于其训练数据的时间范围。

函数调用是 Azure OpenAI 服务的一项功能，用于克服以下限制：

- **一致的响应格式**。如果我们能够更好地控制响应格式，就可以更轻松地将响应集成到其他系统中。
- **外部数据**。能够在聊天上下文中使用应用程序的其他数据源。

## 通过场景说明问题

> 如果你想运行以下场景，我们建议使用[包含的笔记本](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst)。你也可以直接阅读，我们将通过场景说明函数如何帮助解决问题。

让我们看看一个例子，说明响应格式问题：

假设我们想创建一个学生数据的数据库，以便向他们推荐合适的课程。下面是两个学生描述，它们包含的数据非常相似。

1. 创建与 Azure OpenAI 资源的连接：

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

   以下是一些用于配置与 Azure OpenAI 连接的 Python 代码，其中设置了 `api_type`、`api_base`、`api_version` 和 `api_key`。

1. 使用变量 `student_1_description` 和 `student_2_description` 创建两个学生描述。

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   我们希望将上述学生描述发送到 LLM 以解析数据。这些数据可以稍后用于我们的应用程序，并发送到 API 或存储到数据库中。

1. 创建两个相同的提示，指示 LLM 我们感兴趣的信息：

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

1. 设置提示和与 Azure OpenAI 的连接后，我们现在将使用 `openai.ChatCompletion` 将提示发送到 LLM。我们将提示存储在 `messages` 变量中，并将角色分配为 `user`，以模拟用户向聊天机器人发送消息。

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

现在我们可以将两个请求发送到 LLM，并通过以下方式检查收到的响应：`openai_response1['choices'][0]['message']['content']`。

1. 最后，我们可以通过调用 `json.loads` 将响应转换为 JSON 格式：

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   响应 1：

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   响应 2：

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   尽管提示相同且描述相似，但我们看到 `Grades` 属性的值格式不同，例如有时是 `3.7` 或 `3.7 GPA`。

   这是因为 LLM 接收的是非结构化数据（书面提示），返回的也是非结构化数据。我们需要一个结构化的格式，以便在存储或使用这些数据时知道该期待什么。

那么我们如何解决格式化问题呢？通过使用函数调用，我们可以确保收到结构化数据。当使用函数调用时，LLM 实际上并不会调用或运行任何函数。相反，我们为 LLM 创建一个结构，以便其响应遵循该结构。然后我们使用这些结构化响应来确定在我们的应用程序中运行哪些函数。

![函数流程](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.zh.png)

然后我们可以将函数返回的内容发送回 LLM。LLM 随后会使用自然语言回答用户的查询。

## 使用函数调用的场景

函数调用可以在许多不同的场景中改进你的应用程序，例如：

- **调用外部工具**。聊天机器人非常擅长回答用户的问题。通过使用函数调用，聊天机器人可以使用用户的消息完成某些任务。例如，学生可以要求聊天机器人“发送一封邮件给我的导师，说我需要更多关于这个主题的帮助”。这可以调用一个函数 `send_email(to: string, body: string)`。

- **创建 API 或数据库查询**。用户可以使用自然语言查找信息，这些信息会被转换为格式化的查询或 API 请求。例如，老师可以请求“哪些学生完成了最后的作业”，这可以调用一个名为 `get_completed(student_name: string, assignment: int, current_status: string)` 的函数。

- **创建结构化数据**。用户可以从文本块或 CSV 中提取重要信息。例如，学生可以将关于和平协议的维基百科文章转换为 AI 闪卡。这可以通过使用一个名为 `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)` 的函数来完成。

## 创建你的第一个函数调用

创建函数调用的过程包括三个主要步骤：

1. **调用** Chat Completions API，提供函数列表和用户消息。
2. **读取**模型的响应以执行操作，例如运行函数或 API 调用。
3. **再次调用** Chat Completions API，使用函数的响应生成用户的自然语言回复。

![LLM 流程](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.zh.png)

### 第一步 - 创建消息

第一步是创建用户消息。这可以通过获取文本输入的值动态分配，也可以直接在此处分配一个值。如果这是你第一次使用 Chat Completions API，我们需要定义消息的 `role` 和 `content`。

`role` 可以是 `system`（创建规则）、`assistant`（模型）或 `user`（最终用户）。对于函数调用，我们将其分配为 `user` 并提供一个示例问题。

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

通过分配不同的角色，可以明确告诉 LLM 是系统在说话还是用户在说话，这有助于构建 LLM 可以基于的对话历史。

### 第二步 - 创建函数

接下来，我们将定义一个函数及其参数。我们将在这里使用一个名为 `search_courses` 的函数，但你可以创建多个函数。

> **重要提示**：函数包含在发送给 LLM 的系统消息中，并会占用可用的 token 数量。

下面，我们将函数创建为一个项目数组。每个项目都是一个函数，并具有属性 `name`、`description` 和 `parameters`：

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

让我们更详细地描述每个函数实例：

- `name` - 我们希望调用的函数名称。
- `description` - 这是对函数如何工作的描述。这里需要具体和清晰。
- `parameters` - 一个值列表和格式，指定模型在响应中生成的内容。`parameters` 数组由项目组成，每个项目具有以下属性：
  1.  `type` - 属性将存储的数据类型。
  1.  `properties` - 模型将在响应中使用的具体值列表。
      1. `name` - 键是模型在格式化响应中使用的属性名称，例如 `product`。
      1. `type` - 此属性的数据类型，例如 `string`。
      1. `description` - 对具体属性的描述。

还有一个可选属性 `required` - 函数调用完成所需的属性。

### 第三步 - 发起函数调用

定义函数后，我们需要在调用 Chat Completion API 时将其包含在请求中。我们通过将 `functions` 添加到请求中来实现这一点。在这种情况下，`functions=functions`。

还有一个选项可以将 `function_call` 设置为 `auto`。这意味着我们将让 LLM 根据用户消息决定应该调用哪个函数，而不是自己分配。

以下是调用 `ChatCompletion.create` 的代码，注意我们如何设置 `functions=functions` 和 `function_call="auto"`，从而让 LLM 自行决定何时调用我们提供的函数：

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

现在返回的响应如下所示：

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

我们可以看到函数 `search_courses` 被调用，并且在 JSON 响应中的 `arguments` 属性中列出了调用的参数。

LLM 能够从提供给 `messages` 参数的值中提取数据以匹配函数的参数。以下是 `messages` 的值：

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

如你所见，`student`、`Azure` 和 `beginner` 是从 `messages` 中提取的，并作为函数的输入。以这种方式使用函数是从提示中提取信息的好方法，同时也为 LLM 提供结构化数据并实现可重用功能。

接下来，我们需要看看如何在应用程序中使用它。

## 将函数调用集成到应用程序中

在测试了 LLM 的格式化响应后，我们现在可以将其集成到应用程序中。

### 管理流程

为了将其集成到我们的应用程序中，让我们采取以下步骤：

1. 首先，调用 OpenAI 服务并将消息存储在一个名为 `response_message` 的变量中。

   ```python
   response_message = response.choices[0].message
   ```

1. 现在我们将定义一个函数，该函数将调用 Microsoft Learn API 以获取课程列表：

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

   注意我们现在创建了一个实际的 Python 函数，该函数映射到 `functions` 变量中引入的函数名称。我们还进行了真正的外部 API 调用以获取所需的数据。在这种情况下，我们调用 Microsoft Learn API 来搜索培训模块。

好的，我们创建了 `functions` 变量和一个对应的 Python 函数，那么我们如何告诉 LLM 将这两者映射在一起，以便调用我们的 Python 函数呢？

1. 要查看是否需要调用 Python 函数，我们需要检查 LLM 响应中是否包含 `function_call`，并调用指定的函数。以下是如何进行上述检查的代码：

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

   以下三行代码确保我们提取函数名称、参数并进行调用：

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   以下是运行代码后的输出：

   **输出**

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

1. 现在我们将更新后的消息 `messages` 发送给 LLM，以便我们可以接收到自然语言响应，而不是 API 的 JSON 格式响应。

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

   **输出**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## 作业

为了继续学习 Azure OpenAI 函数调用，你可以尝试：

- 为函数添加更多参数，以帮助学习者找到更多课程。
- 创建另一个函数调用，获取学习者的更多信息，例如他们的母语。
- 创建错误处理机制，当函数调用和/或 API 调用未返回任何合适的课程时

提示：请参考 [Learn API 参考文档](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) 页面，了解这些数据的获取方式和位置。

## 干得好！继续学习之旅

完成本课后，查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

前往第 12 课，我们将探讨如何 [设计 AI 应用的用户体验](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。