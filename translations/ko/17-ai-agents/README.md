[![Open Source Models](../../../translated_images/ko/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 소개

AI 에이전트는 생성 AI 분야에서 흥미로운 발전을 나타내며, 대형 언어 모델(LLM)을 단순한 보조자에서 행동을 수행할 수 있는 에이전트로 발전시킵니다. AI 에이전트 프레임워크는 개발자들이 LLM이 도구와 상태 관리를 사용할 수 있게 하는 애플리케이션을 만들 수 있도록 합니다. 이 프레임워크는 또한 가시성을 향상시켜 사용자와 개발자가 LLM이 계획한 행동을 모니터링할 수 있게 하여 경험 관리를 개선합니다.

이 강의에서는 다음 내용을 다룹니다:

- AI 에이전트가 무엇인지 이해하기 - AI 에이전트란 정확히 무엇인가?
- 다섯 가지 AI 에이전트 프레임워크 탐색 - 무엇이 각각을 독특하게 만드는가?
- 다양한 사용 사례에 AI 에이전트 적용하기 - 언제 AI 에이전트를 사용해야 하는가?

## 학습 목표

이 강의를 수강한 후, 다음을 할 수 있습니다:

- AI 에이전트가 무엇이며 어떻게 사용될 수 있는지 설명할 수 있습니다.
- 인기 있는 AI 에이전트 프레임워크 간의 차이점과 그것들이 어떻게 다른지 이해할 수 있습니다.
- AI 에이전트가 어떻게 작동하는지 이해하여 그들과 함께 애플리케이션을 구축할 수 있습니다.

## AI 에이전트란 무엇인가?

AI 에이전트는 생성 AI 세계에서 매우 흥미로운 분야입니다. 이 흥분과 함께 때로는 용어와 적용에 혼동이 생깁니다. 대부분의 AI 에이전트 도구를 포괄적으로 포함하도록 간단하게 하기 위해 다음 정의를 사용하겠습니다:

AI 에이전트는 대형 언어 모델(LLM)이 <strong>상태</strong>와 <strong>도구</strong>에 접근할 수 있게 하여 작업을 수행할 수 있도록 합니다.

![Agent Model](../../../translated_images/ko/what-agent.21f2893bdfd01e6a.webp)

다음 용어들을 정의해봅시다:

**대형 언어 모델** - 이 강의에서 언급하는 GPT-3.5, GPT-4, Llama-2 등과 같은 모델들입니다.

<strong>상태</strong> - LLM이 작업 중인 문맥을 의미합니다. LLM은 과거 행동과 현재 문맥을 사용하여 이후 행동에 대한 결정을 내립니다. AI 에이전트 프레임워크는 개발자가 이 문맥을 더 쉽게 유지하도록 도와줍니다.

<strong>도구</strong> - 사용자가 요청하고 LLM이 계획한 작업을 완료하기 위해 LLM은 도구에 접근해야 합니다. 도구의 예로 데이터베이스, API, 외부 애플리케이션 또는 또 다른 LLM 등이 있습니다!

이러한 정의는 앞으로 구현 방식을 살펴볼 때 좋은 기초가 될 것입니다. 이제 몇 가지 다른 AI 에이전트 프레임워크를 탐험해 봅시다:

## LangChain 에이전트

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst)는 위에서 제공한 정의의 구현입니다.

<strong>상태</strong>를 관리하기 위해, `AgentExecutor`라는 내장 함수를 사용합니다. 이것은 정의된 `agent`와 이용 가능한 `tools`를 받습니다.

`Agent Executor`는 대화 기록도 저장하여 대화의 문맥을 제공합니다.

![Langchain Agents](../../../translated_images/ko/langchain-agents.edcc55b5d5c43716.webp)

LangChain은 LLM이 접근할 수 있는[도구 모음](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)을 제공합니다. 이 도구들은 커뮤니티와 LangChain 팀에 의해 만들어졌습니다.

그런 다음 이 도구들을 정의하고 `Agent Executor`에 전달할 수 있습니다.

가시성도 AI 에이전트에 대해 이야기할 때 중요한 측면입니다. 애플리케이션 개발자는 LLM이 어떤 도구를 왜 사용하는지 이해하는 것이 중요합니다. 이를 위해 LangChain 팀은 LangSmith를 개발했습니다.

## AutoGen

다음으로 살펴볼 AI 에이전트 프레임워크는 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)입니다. AutoGen의 주요 포커스는 대화입니다. 에이전트는 <strong>대화 가능</strong>하며 <strong>사용자 정의 가능</strong>합니다.

**대화 가능 -** LLM은 작업을 완료하기 위해 다른 LLM과 대화를 시작하고 계속할 수 있습니다. 이는 `AssistantAgents`를 생성하고 특정 시스템 메시지를 제공하여 수행됩니다.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**사용자 정의 가능** - 에이전트는 LLM뿐만 아니라 사용자나 도구로도 정의할 수 있습니다. 개발자로서 `UserProxyAgent`를 정의할 수 있으며, 이 에이전트는 사용자의 피드백을 받아 작업 완료에 상호작용합니다. 이 피드백은 작업 실행을 계속하거나 중지할 수 있습니다.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 상태 및 도구

상태를 변경하고 관리하기 위해, 보조 에이전트는 작업을 완료하기 위한 Python 코드를 생성합니다.

과정의 예는 다음과 같습니다:

![AutoGen](../../../translated_images/ko/autogen.dee9a25a45fde584.webp)

#### 시스템 메시지로 정의된 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

이 시스템 메시지는 이 특정 LLM에 어떤 함수가 작업에 관련 있는지 지시합니다. AutoGen에서는 서로 다른 시스템 메시지를 가진 여러 `AssistantAgents`를 가질 수 있다는 점을 기억하세요.

#### 사용자가 대화 시작

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

사용자 프록시(사람)로부터의 이 메시지가 에이전트가 어떤 함수를 실행할지를 탐색하기 시작하는 과정입니다.

#### 함수 실행

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

초기 대화가 처리되면, 에이전트는 호출할 제안 도구를 보냅니다. 이 경우는 `get_weather`라는 함수입니다. 설정에 따라 이 함수는 자동 실행되어 에이전트가 읽거나, 사용자 입력에 따라 실행될 수 있습니다.

[AutoGen 코드 샘플](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) 목록을 찾아 더 많은 빌드 시작 방법을 탐색할 수 있습니다.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 는 Python과 .NET에서 AI 에이전트 및 다중 에이전트 시스템을 구축하기 위한 Microsoft의 오픈 소스 SDK입니다. 이는 두 가지 이전 Microsoft 프로젝트의 강점인 엔터프라이즈 기능을 지닌 <strong>Semantic Kernel</strong>과 다중 에이전트 오케스트레이션인 <strong>AutoGen</strong>을 단일, 지원되는 프레임워크로 통합합니다. 오늘 새로운 에이전트 프로젝트를 시작한다면, AutoGen의 추천 후속작입니다.

이 프레임워크는 단일 <strong>채팅 에이전트</strong>에서 복잡한 <strong>다중 에이전트 워크플로우</strong>에 이르기까지 확장되며, Microsoft Foundry, Azure OpenAI, OpenAI와 직접 통합됩니다. 또한 OpenTelemetry를 통한 내장 가시성을 제공하여 에이전트가 수행하는 일을 정확히 추적할 수 있습니다.

### 상태 및 도구

<strong>상태</strong> - 프레임워크는 <strong>스레드</strong>를 통해 대화 문맥을 관리합니다. 에이전트는 메시지 기록(사용자 요청, 도구 호출 및 결과)을 추적하여 각 턴이 이전 내용을 기반으로 구축됩니다. 스레드는 저장 가능하여 대화를 일시 중지했다가 나중에 재개할 수 있습니다.

<strong>도구</strong> - 에이전트에 도구를 제공할 때는 단순한 Python 함수를 전달합니다. 타입 주석이 있는 매개변수는 자동으로 스키마로 변환되어 모델이 호출 시기와 방법을 알 수 있습니다(함수 호출). 이 프레임워크는 또한 Model Context Protocol(MCP) 서버와 호스팅 도구(예: 코드 인터프리터)를 지원합니다.

다음은 사용자 지정 도구가 있는 단일 에이전트의 예시입니다:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Microsoft Foundry에서 Azure OpenAI에 연결하려면, 클라이언트에 엔드포인트와 자격 증명을 전달하세요:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 다중 에이전트 워크플로우

이 프레임워크가 진가를 발휘하는 부분은 여러 에이전트를 함께 오케스트레이션하는 것입니다. 예를 들어, 에이전트를 차례대로 실행하거나(각각의 문맥을 다음 에이전트에 전달), 여러 에이전트를 병렬로 실행해 결과를 종합할 수 있습니다:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 에이전트를 순차적으로 실행하여 대화 컨텍스트를 체인으로 전달합니다
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 에이전트에게 병렬로 분산시킨 다음, 응답을 집계합니다
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

프레임워크 설치 및 시작하기:

```bash
pip install agent-framework-core
# 선택적 통합
pip install agent-framework-openai       # OpenAI 및 Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

[Microsoft Agent Framework 저장소](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst)와 [공식 문서](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)를 더 탐색할 수 있습니다.

## Taskweaver

다음으로 탐험할 에이전트 프레임워크는 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)입니다. 이것은 "코드 우선" 에이전트로 알려져 있는데, 문자열(`strings`) 대신 Python의 DataFrame으로 작업할 수 있습니다. 이는 데이터 분석과 생성 작업에 매우 유용합니다. 그래프나 차트를 만들거나 랜덤 수를 생성하는 작업 등이 포함됩니다.

### 상태 및 도구

대화 상태를 관리하기 위해 TaskWeaver는 `Planner` 개념을 사용합니다. `Planner`는 사용자의 요청을 받아 완료해야 할 작업을 매핑하는 LLM입니다.

작업을 완료하기 위해 `Planner`는 `Plugins`라는 도구 모음에 접근합니다. 이는 Python 클래스거나 일반 코드 인터프리터일 수 있습니다. 이 플러그인들은 임베딩으로 저장되어 LLM이 올바른 플러그인을 더 잘 탐색할 수 있게 합니다.

![Taskweaver](../../../translated_images/ko/taskweaver.da8559999267715a.webp)

이상 탐지(anomaly detection)를 처리하는 플러그인 예시입니다:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

코드는 실행 전에 검증됩니다. Taskweaver에서 문맥 관리를 위한 또 다른 기능은 `experience`입니다. 경험은 대화 문맥을 장기적으로 YAML 파일에 저장합니다. 이것은 LLM이 이전 대화에 노출되면서 특정 작업에서 시간이 지나면서 개선되도록 설정할 수 있습니다.

## JARVIS

마지막으로 탐험할 에이전트 프레임워크는 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)입니다. JARVIS의 독특한 점은 LLM이 대화의 `상태`를 관리하는 반면, `도구`는 다른 AI 모델이라는 점입니다. 각 AI 모델은 객체 탐지, 전사 또는 이미지 캡셔닝과 같은 특정 작업을 수행하는 전문화된 모델입니다.

![JARVIS](../../../translated_images/ko/jarvis.762ddbadbd1a3a33.webp)

일반 목적 모델인 LLM은 사용자로부터 요청을 받아 특정 작업과 작업 완료에 필요한 인수/데이터를 식별합니다.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

그 다음 LLM은 요청을 전문 AI 모델이 해석할 수 있는 형식(예: JSON)으로 포맷합니다. AI 모델이 작업을 기반으로 예측을 반환하면, LLM이 응답을 받습니다.

작업 완료에 여러 모델이 필요할 경우, LLM은 각 모델의 응답을 해석하여 최종 사용자 응답을 생성하기 전에 통합합니다.

다음 예시는 사용자가 사진 내 객체의 설명과 개수를 요청할 때 어떻게 작동하는지 보여줍니다:

## 과제

AI 에이전트 학습을 계속하기 위해 Microsoft Agent Framework를 사용해 다음을 구축할 수 있습니다:

- 교육 스타트업의 다양한 부서와의 비즈니스 회의를 시뮬레이션하는 애플리케이션.
- LLM이 다양한 페르소나와 우선순위를 이해하도록 안내하는 시스템 메시지 생성, 사용자가 새로운 제품 아이디어를 피칭할 수 있게 하기.
- LLM이 각 부서에서 후속 질문을 생성하여 피칭과 제품 아이디어를 정제하고 개선하게 하기.

## 학습은 여기서 끝나지 않습니다, 여정을 계속하세요

이 강의를 마친 후, 우리의 [생성 AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속해서 향상시키세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->