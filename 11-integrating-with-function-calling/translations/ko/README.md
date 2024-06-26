# Function Calling과 통합하기

[![Integrating with function calling](../../images/11-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

지금까지 이전 레슨에서 많은 것을 배웠습니다. 그러나 더 나아갈 수 있습니다. 우리가 해결할 수 있는 몇 가지 문제는 응답 형식을 더 일관되게 만들어 응답을 더 쉽게 처리할 수 있도록 하는 것이며, 또한 응용 프로그램을 더 풍부하게 만들기 위해 다른 소스에서 데이터를 추가할 수도 있습니다.

위에서 언급한 문제들은 이번 챕터에서 다루고자 하는 내용입니다.

## 소개

이 레슨에서는 다음을 다룹니다:

- function calling이란 무엇이며 사용 사례는 무엇인지 설명합니다.
- Azure OpenAI를 사용하여 function calling을 만드는 방법을 알아봅니다.
- function calling을 응용 프로그램에 통합하는 방법을 알아봅니다.

## 학습 목표

이 레슨을 마치면 다음을 할 수 있게 됩니다:

- function calling을 사용하는 목적을 설명할 수 있습니다.
- Azure Open AI 서비스를 사용하여 function calling을 설정할 수 있습니다.
- 응용 프로그램의 사용 사례에 맞는 효과적인 function calling을 설계할 수 있습니다.

## 시나리오: 함수를 사용하여 챗봇 개선하기

이 레슨에서는 교육 스타트업을 위한 기능을 구축하려고 합니다. 사용자가 챗봇을 사용하여 기술적인 과목을 찾을 수 있는 기능을 추가할 것입니다. 우리는 사용자의 기술 수준, 현재 역할 및 관심 기술에 맞는 과목을 추천할 것입니다.

이 시나리오를 완료하기 위해 다음을 조합하여 사용할 것입니다:

- 사용자에게 채팅 경험을 제공하기 위해 `Azure Open AI` 사용.
- 사용자의 요청에 기반하여 과목을 찾는 데 도움을 주는 `Microsoft Learn Catalog API` 사용.
- 사용자의 쿼리를 가져와 API 요청을 수행하는 함수에 전달하기 위해 `function calling` 사용.

시작하기 전에, 왜 우리가 처음부터 function calling을 사용하고자 하는지 살펴보겠습니다:

## Function calling의 필요성

function calling 이전에 LLM에서의 응답은 구조화되지 않고 일관성이 없었습니다. 개발자는 각 응답의 변형을 처리할 수 있도록 복잡한 유효성 검사 코드를 작성해야 했습니다. 사용자는 "스톡홀름의 현재 날씨는 어떻게 되나요?"와 같은 답변을 받을 수 없었습니다. 이는 모델이 데이터를 훈련한 시점으로 제한되었기 때문입니다.

function calling은 다음과 같은 제한 사항을 극복하기 위한 Azure Open AI 서비스의 기능입니다:

- **일관된 응답 형식**. 응답 형식을 더 잘 제어할 수 있다면 응답을 다른 시스템과 더 쉽게 통합할 수 있습니다.
- **외부 데이터**. 채팅 컨텍스트에서 응용 프로그램의 다른 소스 데이터를 사용할 수 있는 능력.

## 시나리오를 통해 문제 설명하기

> 아래 시나리오를 실행하려면 [제공된 노트북](../../aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst)을 사용하는 것을 권장합니다. 문제를 설명하기 위해 함수가 문제를 해결하는 데 도움이 되는 시나리오를 보여주려고 하므로 읽기만 해도 됩니다.

응답 형식 문제를 보여주는 예제를 살펴보겠습니다:

학생 데이터베이스를 생성하여 학생들에게 적합한 과목을 제안할 수 있도록 하려고 합니다. 아래에는 데이터 내용이 매우 유사한 두 학생의 설명이 있습니다.

1. Azure Open AI 리소스에 연결을 만듭니다:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_KEY'],  # 이것은 기본값이며, 생략 가능합니다.
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   다음은 `api_type`, `api_base`, `api_version` 및 `api_key`를 설정하는 Azure Open AI에 대한 연결을 구성하기 위한 일부 Python 코드입니다.

2. Creating two student descriptions using variables `student_1_description` and `student_2_description`.

   ```python
   student_1_description="Emily Johnson는 Duke 대학교에서 컴퓨터 공학을 전공하는 2학년 학생입니다. 그녀는 3.7의 평점을 가지고 있습니다. Emily는 대학의 체스 동아리와 토론 팀의 활발한 회원입니다. 졸업 후 소프트웨어 엔지니어링 분야에서 경력을 쌓고자 합니다."

   student_2_description = "Michael Lee는 Stanford 대학교에서 컴퓨터 공학을 전공하는 2학년 학생입니다. 그는 3.8의 평점을 가지고 있습니다. Michael은 프로그래밍 기술로 유명하며 대학의 로봇 공학 동아리의 활발한 회원입니다. 그는 학업을 마친 후 인공지능 분야에서 경력을 쌓고자 합니다."
   ```

   위의 학생 설명을 LLM에게 보내 데이터를 구문 분석하도록 하려고 합니다. 이 데이터는 나중에 우리의 애플리케이션에서 사용되어 API로 전송되거나 데이터베이스에 저장될 수 있습니다.

3. LLM에게 우리가 관심 있는 정보를 지시하는 두 개의 동일한 프롬프트를 생성해 봅시다:

   ```python
   prompt1 = f'''
   다음 텍스트에서 다음 정보를 추출하여 JSON 객체로 반환해주세요:

   이름
   전공
   학교
   성적
   동아리

   다음 텍스트에서 정보를 추출해주세요:
   {student_1_description}
   '''

   prompt2 = f'''
   다음 텍스트에서 다음 정보를 추출하여 JSON 객체로 반환해주세요:

   이름
   전공
   학교
   성적
   동아리

   다음 텍스트에서 정보를 추출해주세요:
   {student_2_description}
   '''
   ```

   위의 프롬프트는 LLM에게 정보를 추출하고 응답을 JSON 형식으로 반환하도록 지시합니다.

4. 프롬프트와 Azure Open AI와의 연결을 설정한 후, `openai.ChatCompletion`을 사용하여 프롬프트를 LLM에게 전송합니다. 프롬프트를 `messages` 변수에 저장하고 역할을 `user`로 지정합니다. 이는 챗봇에게 사용자의 메시지를 모방하기 위한 것입니다.

   ```python
   # prompt one에 대한 응답
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # prompt two에 대한 응답
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

이제 우리는 두 요청을 LLM에게 보내고, `openai_response1['choices'][0]['message']['content']`와 같이 응답을 받을 수 있습니다.

1. 마지막으로, `json.loads`를 호출하여 응답을 JSON 형식으로 변환할 수 있습니다:

   ```python
   # 응답을 JSON 객체로 로드합니다.
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   응답 1:

   ```json
   {
     "이름": "Emily Johnson",
     "전공": "컴퓨터 공학",
     "학교": "Duke 대학교",
     "성적": "3.7",
     "동아리": "체스 동아리"
   }
   ```

   응답 2:

   ```json
   {
     "이름": "Michael Lee",
     "전공": "컴퓨터 공학",
     "학교": "Stanford 대학교",
     "성적": "3.8 GPA",
     "동아리": "로봇 공학 동아리"
   }
   ```

   프롬프트는 동일하고 설명은 유사하지만, `Grades` 속성의 값은 때로는 `3.7` 또는 `3.7 GPA`와 같이 서로 다른 형식으로 포맷되는 것을 볼 수 있습니다.

   이 결과는 LLM이 쓰인 프롬프트의 구조화되지 않은 (unstructured) 데이터를 받아들이고 구조화되지 않은 (unstructured) 데이터를 반환하기 때문입니다. 이 데이터를 저장하거나 사용할 때 어떤 형식을 기대해야 하는지 알기 위해 구조화된 (structured) 형식이 필요합니다.

   그렇다면 포맷팅 문제를 어떻게 해결할까요? functional calling을 사용하여 구조화된 데이터를 받을 수 있도록 할 수 있습니다. function calling을 사용할 때, LLM은 실제로 함수를 호출하거나 실행하지 않습니다. 대신, LLM에게 응답을 따르기 위한 구조를 만듭니다. 그런 다음, 우리는 응답을 사용하여 응용 프로그램에서 어떤 함수를 실행할지 알 수 있습니다.

![function flow](../../images/Function-Flow.png?WT.mc_id=academic-105485-koreyst)

함수에서 반환된 값을 가져와서 LLM에게 다시 전송할 수 있습니다. 그럼 LLM은 자연어를 사용하여 사용자의 질문에 답변합니다.

## function call을 사용하는 사용 사례

function call을 사용하여 앱을 개선할 수 있는 다양한 사용 사례가 있습니다. 예를 들어 다음과 같은 경우입니다:

- **외부 도구 호출**: 챗봇은 사용자의 질문에 대한 답변을 제공하는 데에 탁월합니다. function calling을 사용하면 챗봇은 사용자의 메시지를 사용하여 특정 작업을 완료할 수 있습니다. 예를 들어, 학생이 챗봇에게 "이 주제에 대해 더 많은 도움이 필요하다는 내 강사에게 이메일을 보내주세요"라고 요청할 수 있습니다. 이는 `send_email(to: string, body: string)` function calling을 수행할 수 있습니다.

- **API 또는 데이터베이스 쿼리 생성**: 사용자는 자연어를 사용하여 형식화된 쿼리나 API 요청을 통해 정보를 찾을 수 있습니다. 예를 들어, 선생님이 "최근 과제를 완료한 학생들은 누구인가요?"라고 요청할 수 있으며, 이는 `get_completed(student_name: string, assignment: int, current_status: string)`라는 함수를 호출할 수 있습니다.

- **구조화된 데이터 생성**: 사용자는 텍스트 블록이나 CSV에서 중요한 정보를 추출하기 위해 LLM을 사용할 수 있습니다. 예를 들어, 학생이 평화 협정에 대한 위키피디아 문서를 가져와 AI 플래시 카드를 만들 수 있습니다. 이는 `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`라는 함수를 사용하여 수행할 수 있습니다.

## 첫 번째 Function Call 생성

Function Call을 생성하는 과정은 다음 3단계로 이루어집니다:

1. 함수 목록과 사용자 메시지를 사용하여 Chat Completions API를 **호출**합니다.
2. 모델의 응답을 **읽어** 함수를 실행하거나 API 호출을 수행합니다.
3. 함수의 응답을 사용하여 사용자에게 응답을 생성하기 위해 Chat Completions API에 **다시 호출**합니다.

![LLM Flow](../../images/LLM-Flow.png?WT.mc_id=academic-105485-koreyst)

### 단계 1 - 메시지 생성

첫 번째 단계는 사용자 메시지를 생성하는 것입니다. 이는 동적으로 텍스트 입력의 값을 가져와 할당할 수도 있고, 여기에서 값을 직접 할당할 수도 있습니다. Chat Completions API를 처음 사용하는 경우, `role`과 `content`를 메시지에 정의해야 합니다.

`role`은 `system` (규칙 생성), `assistant` (모델), `user` (최종 사용자) 중 하나일 수 있습니다. function calling을 위해 `user`로 할당하고 예시 질문을 작성합니다.

```python
messages= [ {"role": "user", "content": "Azure를 배우기 위한 초보 학생에게 좋은 강좌를 찾아주세요."} ]
```

다른 역할을 할당함으로써, 시스템이 무언가를 말하는지 사용자가 말하는지 LLM에게 명확하게 전달되어 LLM이 대화 기록을 구축하는 데 도움이 됩니다.

### 단계 2 - 함수 생성

다음으로, 함수와 해당 함수의 매개변수를 정의합니다. 여기에서는 `search_courses`라는 하나의 함수만 사용하지만 여러 개의 함수를 생성할 수 있습니다.

> **중요**: 함수는 LLM에게 시스템 메시지에 포함되며 사용 가능한 토큰의 양에 포함됩니다.

아래에서는 각 항목이 함수인 배열로 함수를 생성합니다. 각 항목은 `name`, `description`, `parameters` 속성을 가지고 있습니다:

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

아래에서 각 함수 인스턴스를 자세히 설명하겠습니다:

- `name` - 호출하려는 함수의 이름입니다.
- `description` - 함수가 작동하는 방식에 대한 설명입니다. 여기서는 구체적이고 명확하게 작성하는 것이 중요합니다.
- `parameters` - 모델이 응답에서 생성할 값과 형식의 목록입니다. 매개변수 배열은 다음 속성을 가진 항목으로 구성됩니다:
  1.  `type` - 속성의 데이터 유형이 저장됩니다.
  1.  `properties` - 모델이 응답에 사용할 구체적인 값의 목록입니다.
      1.  `name` - 모델이 형식화된 응답에서 사용할 속성의 이름입니다. 예를 들어, `product`입니다.
      1.  `type` - 이 속성의 데이터 유형입니다. 예를 들어, `string`입니다.
      1.  `description` - 특정 속성에 대한 설명입니다.

function call이 완료되기 위해 선택적으로 `required` 속성도 있습니다.

### 단계 3 - function call 만들기

함수를 정의한 후에는 Chat Completions API 호출에 해당 함수를 포함해야 합니다. 이를 위해 요청에 `functions`를 추가합니다. 이 경우 `functions=functions`로 설정합니다.

`function_call`을 `auto`로 설정하는 옵션도 있습니다. 이는 우리가 직접 할당하는 대신 LLM이 사용자 메시지를 기반으로 어떤 함수를 호출할지 결정하도록 합니다.

아래 코드에서는 `ChatCompletion.create`를 호출하는 방법을 보여줍니다. `functions=functions`와 `function_call="auto"`를 설정하여 LLM에게 우리가 제공한 함수를 언제 호출할지 결정하도록 합니다:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

The response coming back now looks like so:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

여기에서는 `search_courses` 함수가 어떻게 호출되고 어떤 인수로 호출되었는지를 볼 수 있습니다. 이는 JSON 응답의 `arguments` 속성에 나열된 것과 동일합니다.

LLM은 `messages` 매개변수에 제공된 값에서 데이터를 추출하여 함수의 인수와 일치하는 데이터를 찾을 수 있었습니다. 아래는 `messages` 값의 복습입니다:

```python
messages= [ {"role": "user", "content": "초보 학생이 Azure를 배우기 위한 좋은 강좌를 찾아주세요."} ]
```

`messages`에서 `student`, `Azure` 및 `beginner`가 추출되어 함수의 입력으로 설정되었음을 확인할 수 있습니다. 함수를 이렇게 사용하는 것은 프롬프트에서 정보를 추출하는 좋은 방법이며 LLM에 구조를 제공하고 재사용 가능한 기능을 갖도록 하는 데 유용합니다.

다음으로, 이를 앱에 통합하는 방법을 살펴보겠습니다.

## Function Call을 애플리케이션에 통합하기

LLM에서 서식이 지정된 응답을 테스트한 후, 이제 이를 애플리케이션에 통합할 수 있습니다.

### 흐름 관리

애플리케이션에 이를 통합하기 위해 다음 단계를 수행해 보겠습니다:

1. 먼저 Open AI 서비스에 호출을 수행하고 메시지를 `response_message`라는 변수에 저장합니다.

   ```python
   response_message = response.choices[0].message
   ```

1. 이제 Microsoft Learn API를 호출하여 강좌 목록을 가져올 함수를 정의합니다:

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

   이제 우리는 `functions` 변수에 도입된 함수 이름과 매핑되는 실제 Python 함수를 생성합니다. 또한 필요한 데이터를 가져오기 위해 실제 외부 API 호출을 수행합니다. 이 경우에는 Microsoft Learn API를 사용하여 교육 모듈을 검색합니다.

   그래서 `functions` 변수와 해당하는 Python 함수를 생성했는데, 어떻게 LLM에게 이 둘을 매핑하여 Python 함수를 호출하도록 알려줄까요?

   1. Python 함수를 호출해야 하는지 확인하기 위해 LLM 응답을 살펴보고 `function_call`이 포함되어 있는지 확인한 후 해당 함수를 호출해야 합니다. 아래에 언급된 확인 방법을 사용하여 이를 수행할 수 있습니다:

   ```python
      # 모델이 함수를 호출하려는지 확인합니다.
      if response_message.function_call.name:
      print("추천 function call:")
      print(response_message.function_call.name)
      print()

      # 함수를 호출합니다.
      function_name = response_message.function_call.name

      available_functions = {
            "search_courses": search_courses,
      }
      function_to_call = available_functions[function_name]

      function_args = json.loads(response_message.function_call.arguments)
      function_response = function_to_call(**function_args)

      print("function call 결과:")
      print(function_response)
      print(type(function_response))


      # 어시스턴트 응답과 함수 응답을 메시지에 추가합니다.
      messages.append( # 어시스턴트 응답을 메시지에 추가
         {
            "role": response_message.role,
            "function_call": {
               "name": function_name,
               "arguments": response_message.function_call.arguments,
            },
            "content": None
         }
      )
      messages.append( # 함수 응답을 메시지에 추가
         {
            "role": "function",
            "name": function_name,
            "content":function_response,
         }
      )
   ```

   이 세 줄은 함수 이름, 인수를 추출하고 호출을 수행하는 것을 보장합니다:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   아래는 코드를 실행한 결과입니다:

   **결과**

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

1. 이제 우리는 업데이트된 메시지 `messages`를 LLM에 보내서 API JSON 형식의 응답 대신 자연어 응답을 받을 것입니다.

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
          )  # GPT에서 함수 응답을 볼 수 있는 새로운 응답을 받습니다.


   print(second_response.choices[0].message)
   ```

   **Output**

   ```python
   {
     "role": "assistant",
   "content": "Azure를 배우기 위한 초보 학생들을 위한 좋은 강의를 찾았어요:\n\n1. [암호학 개념 설명](https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [TensorFlow를 사용한 오디오 분류 소개](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Azure SQL Database에서 성능이 우수한 데이터 모델 설계](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Azure를 위한 Microsoft Cloud Adoption Framework 시작하기](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Rust 개발 환경 설정하기](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\n링크를 클릭하여 강의에 접속할 수 있습니다."
   }

   ```

## 과제

Azure Open AI Function Calling 학습을 계속 진행하기 위해 다음을 구현해 볼 수 있습니다:

- 학습자가 더 많은 강의를 찾을 수 있도록 함수의 추가 매개변수를 만들어보세요.
- 학습자의 모국어와 같은 추가 정보를 받아들이는 다른 function call을 생성하세요.
- function call 및/또는 API 호출이 적합한 강의를 반환하지 않을 경우 오류 처리를 만들어보세요.

힌트: [Learn API 참조 문서](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) 페이지를 참고하여 이 데이터가 어떻게 사용 가능한지 확인하세요.

## 훌륭합니다! 계속해서 학습하세요

이 레슨을 완료한 후, [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 Generative AI 지식을 더욱 향상시킬 수 있습니다!

12번 레슨으로 이동하여 [AI 애플리케이션을 위한 UX 디자인](../../../12-designing-ux-for-ai-applications/translations/ko/README.md?WT.mc_id=academic-105485-koreyst)에 대해 알아보세요!
