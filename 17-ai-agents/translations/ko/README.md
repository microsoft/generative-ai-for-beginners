## 소개

AI 에이전트는 생성형 AI에서 흥미로운 발전을 나타내며, 대형 언어 모델(Large Language Models, LLMs)이 보조 역할에서 행동을 취할 수 있는 에이전트로 진화하도록 합니다. AI 에이전트 프레임워크는 개발자가 LLM에 도구와 상태 관리에 대한 접근을 제공하는 애플리케이션을 만들 수 있도록 합니다. 이러한 프레임워크는 또한 가시성을 향상시켜 사용자와 개발자가 LLM이 계획한 행동을 모니터링할 수 있게 하여 경험 관리를 개선합니다.

이번 강의는 다음 영역을 다룰 것입니다:

- AI 에이전트란 무엇인가 이해하기 - AI 에이전트가 정확히 무엇인가?
- 네 가지 다른 AI 에이전트 프레임워크 탐구 - 이들 프레임워크의 고유한 점은 무엇인가?
- 다양한 사용 사례에 AI 에이전트 적용하기 - 언제 AI 에이전트를 사용해야 하는가?

## 학습 목표

이 수업을 마친 후에는 다음을 할 수 있을 것입니다:

- AI 에이전트가 무엇이며 어떻게 사용되는지 설명할 수 있습니다.
- 인기 있는 AI 에이전트 프레임워크들 간의 차이점을 이해하고, 그들이 어떻게 다른지 설명할 수 있습니다.
- AI 에이전트가 어떻게 작동하는지 이해하여 이를 기반으로 애플리케이션을 구축할 수 있습니다.

## AI 에이전트란 무엇인가?

AI 에이전트는 생성형 AI 분야에서 매우 흥미로운 분야입니다. 그러나 이와 같은 흥미로움은 때로는 용어와 그 적용에 대한 혼란을 초래하기도 합니다. 이러한 혼란을 방지하고 대부분의 AI 에이전트 도구를 포괄하기 위해, 우리는 다음과 같은 정의를 사용하려고 합니다:

AI 에이전트는 대형 언어 모델(LLMs)에게 **상태**와 **도구**에 대한 접근 권한을 제공하여 작업을 수행할 수 있게 합니다.

![Agent Model](../../images/what-agent.png?WT.mc_id=academic-105485-koreyst)

다음 용어들을 정의해보겠습니다:

**대형 언어 모델** - 이는 GPT-3.5, GPT-4, Llama-2 등 이 과정에서 언급된 모델을 의미합니다.

**상태** - 이는 LLM이 작업하는 컨텍스트를 의미합니다. LLM은 과거의 행동과 현재의 컨텍스트를 사용하여 이후 행동에 대한 의사 결정을 내립니다. AI 에이전트 프레임워크는 개발자가 이 컨텍스트를 더 쉽게 유지할 수 있도록 도와줍니다.

**도구** - 사용자가 요청한 작업을 완료하고 LLM이 계획한 작업을 수행하기 위해, LLM은 도구에 대한 접근 권한이 필요합니다. 도구의 예로는 데이터베이스, API, 외부 애플리케이션 또는 다른 LLM 등이 있습니다.

이 정의들이 앞으로 우리가 AI 에이전트 프레임워크를 어떻게 구현하는지 살펴볼 때 도움이 되기를 바랍니다. 몇 가지 다른 AI 에이전트 프레임워크를 탐구해 봅시다:

## LangChain 에이전트

[LangChain 에이전트](https://python.langchain.com/docs/modules/agents/?WT.mc_id=academic-105485-koreyst)는 우리가 위에서 제공한 정의를 구현한 것입니다.

**상태**를 관리하기 위해 `AgentExecutor`라는 내장 함수를 사용합니다. 이는 정의된 `agent`와 사용할 수 있는 `tools`를 입력받습니다.

`AgentExecutor`는 또한 대화 기록을 저장하여 대화의 맥락을 제공합니다.

![LangChain 에이전트](../../images/langchain-agents.png?WT.mc_id=academic-105485-koreyst)

LangChain은 LLM이 접근할 수 있는 [도구 카탈로그](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)를 애플리케이션에 가져올 수 있게 제공합니다. 이러한 도구들은 커뮤니티와 LangChain 팀에 의해 만들어졌습니다.

이후 이러한 도구들을 정의하고 `AgentExecutor`에 전달할 수 있습니다.

가시성은 AI 에이전트에 대해 이야기할 때 또 하나의 중요한 측면입니다. 애플리케이션 개발자가 LLM이 어떤 도구를 사용하고 있는지, 그리고 그 이유를 이해하는 것이 중요합니다. 이를 위해 LangChain 팀은 LangSmith를 개발했습니다.

## AutoGen

다음으로 논의할 AI 에이전트 프레임워크는 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)입니다. AutoGen의 주요 초점은 대화입니다. 에이전트는 **대화 가능**하며 **맞춤 설정 가능**합니다.

**대화 가능 -** LLM은 작업을 완료하기 위해 다른 LLM과 대화를 시작하고 지속할 수 있습니다. 이는 `AssistantAgents`를 생성하고 특정 시스템 메시지를 전달함으로써 수행됩니다.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**맞춤 설정 가능 -** 에이전트는 단순한 LLM뿐만 아니라 사용자가 될 수도 있고 도구가 될 수도 있습니다. 개발자로서, 작업을 완료하는 데 있어서 피드백을 위해 사용자와 상호 작용하는 `UserProxyAgent`를 정의할 수 있습니다. 이 피드백은 작업을 계속 진행하거나 멈출 수 있습니다.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 상태와 도구들

상태를 변경하고 관리하기 위해, 보조 에이전트는 작업을 완료하기 위한 Python 코드를 생성합니다.

여기에 과정의 예시가 있습니다:

![AutoGen](../../images/autogen.png?WT.mc_id=academic-105485-koreyst)

#### 시스템 메시지가 포함된 LLM 정의

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

이 시스템 메시지는 특정 LLM에게 해당 작업에 관련된 함수들만 사용하도록 지시합니다. AutoGen을 사용하면 다른 시스템 메시지를 갖는 여러 AssistantAgents를 정의할 수 있다는 점을 기억하세요.

#### 사용자가 대화를 시작함

```python
user_proxy.initiate_chat( chatbot, message="다음 주에 뉴욕 여행을 계획하고 있는데, 옷 고르는 데 도움을 줄 수 있니?", )
```

이 메시지는 사용자 프록시(인간)로부터 에이전트가 실행해야 할 가능한 기능을 탐색하는 프로세스를 시작하는 신호입니다.

#### 함수가 실행됨

```bash
chatbot (to user_proxy):

***** 제안된 도구 호출: get_weather ***** 인수: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> 함수 get_weather 실행 중... user_proxy (to chatbot): ***** 함수 "get_weather" 호출의 응답 ***** 112.22727272727272 EUR ****************************************************************

```

초기 채팅이 처리되면, 에이전트는 호출할 제안된 도구를 보낼 것입니다. 이 경우, 이는 `get_weather`라는 함수입니다. 구성에 따라, 이 함수는 에이전트에 의해 자동으로 실행되고 읽히거나 사용자 입력에 따라 실행될 수 있습니다.

시작하는 방법을 더 탐색하려면 [AutoGen 코드 샘플](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) 목록을 확인할 수 있습니다.

## Taskweaver

다음으로 탐구할 에이전트 프레임워크는 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)입니다. 이 프레임워크는 "코드 우선" 에이전트로 알려져 있습니다. 이는 엄격하게 `문자열`과 작업하는 대신에, Python에서 DataFrames과 작업할 수 있다는 것을 의미합니다. 이것은 데이터 분석 및 생성 작업에 매우 유용합니다. 예를 들어, 그래프와 차트를 생성하거나 랜덤 숫자를 생성하는 작업 등이 이에 포함됩니다.

### 상태 및 도구

대화의 상태를 관리하기 위해 TaskWeaver는 `Planner`의 개념을 사용합니다. `Planner`는 사용자의 요청을 받아들이고 이 요청을 충족시키기 위해 완료해야 할 작업을 계획하는 LLM입니다.

작업을 완료하기 위해 `Planner`는 `Plugins`라고 불리는 도구 모음에 접근합니다. 이 도구들은 Python 클래스나 일반적인 코드 인터프리터일 수 있습니다. 이 플러그인들은 임베딩으로 저장되어 LLM이 적절한 플러그인을 더 잘 검색할 수 있도록 합니다.

![Taskweaver](../../images/taskweaver.png?WT.mc_id=academic-105485-koreyst)

다음은 이상 탐지를 처리하기 위한 플러그인의 예입니다:

```python
class AnomalyDetectionPlugin(Plugin):
    def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

코드는 실행되기 전에 검증됩니다. Taskweaver에서 컨텍스트를 관리하는 또 다른 기능은 `경험`입니다. 경험을 통해 대화의 컨텍스트가 장기적으로 YAML 파일에 저장될 수 있습니다. 이를 구성함으로써 LLM이 이전 대화에 노출된 특정 작업에서 시간이 지남에 따라 개선될 수 있습니다.

## JARVIS

우리가 탐구할 마지막 에이전트 프레임워크는 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst)입니다. JARVIS의 독특한 점은 대화의 `상태`를 관리하는 데 LLM을 사용하고 `도구`로 다른 AI 모델들을 활용한다는 것입니다. 각 AI 모델은 객체 감지, 전사, 이미지 캡션 작성 등 특정 작업을 수행하는 특수 모델들로 구성됩니다.

![JARVIS](../../images/jarvis.png?WT.mc_id=academic-105485-koreyst)

LLM은 범용 모델로서 사용자로부터 요청을 받아 해당 작업과 작업을 완료하는 데 필요한 인수/데이터를 식별합니다.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

그러면 LLM은 특수 AI 모델이 해석할 수 있는 형식, 예를 들어 JSON으로 요청을 포맷합니다. AI 모델이 작업 기반으로 예측을 반환하면 LLM은 응답을 수신합니다.

여러 모델이 작업을 완료하는 데 필요한 경우, LLM은 이러한 모델들의 응답도 해석한 후 사용자에게 제공할 응답을 생성하기 위해 이들을 결합합니다.

다음 예제는 사용자가 사진 속 객체의 설명과 개수를 요청할 때 어떻게 동작하는지 보여줍니다:

## 과제

AutoGen을 사용하여 구축할 수 있는 AI 에이전트 학습을 계속하기 위해 다음을 수행하십시오:

- 교육 스타트업의 다양한 부서와의 비즈니스 회의를 시뮬레이션하는 애플리케이션을 만드십시오.
- LLM이 다른 페르소나와 우선순위를 이해하고 사용자가 새로운 제품 아이디어를 제안할 수 있도록 하는 시스템 메시지를 작성하십시오.
- 그런 다음 각 부서에서 후속 질문을 생성하여 제안 및 제품 아이디어를 개선하고 정제하도록 하십시오.

## 학습은 여기서 멈추지 않습니다. 여정을 계속하세요

이 수업을 마친 후, 우리의 [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성형 AI 지식을 계속해서 높여보세요!
