[![Open Source Models](../../../translated_images/ko/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 소개

AI 에이전트는 생성 AI 분야에서 흥미로운 발전을 나타내며, 대형 언어 모델(LLM)이 단순한 조수에서 행동을 취할 수 있는 에이전트로 진화하도록 합니다. AI 에이전트 프레임워크는 개발자가 LLM에 도구와 상태 관리를 제공하는 애플리케이션을 만들 수 있게 도와줍니다. 이러한 프레임워크는 또한 가시성을 향상시켜, 사용자와 개발자가 LLM이 계획한 행동을 모니터링하고 경험 관리를 개선할 수 있도록 합니다.

이 강의에서는 다음 영역을 다룹니다:

- AI 에이전트가 무엇인지 이해하기 - AI 에이전트란 정확히 무엇인가요?
- 다섯 가지 AI 에이전트 프레임워크 탐색 - 각각의 특징은 무엇인가요?
- 다양한 사용 사례에 AI 에이전트 적용하기 - 언제 AI 에이전트를 사용해야 하나요?

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- AI 에이전트가 무엇인지 설명하고, 어떻게 활용할 수 있는지 알 수 있습니다.
- 인기 있는 AI 에이전트 프레임워크들의 차이점을 이해하고 비교할 수 있습니다.
- AI 에이전트가 어떻게 작동하는지 이해하여 이를 활용한 애플리케이션을 구축할 수 있습니다.

## AI 에이전트란 무엇인가?

AI 에이전트는 생성 AI 세계에서 매우 흥미로운 분야입니다. 이러한 흥미로 인해 용어와 적용에 혼란이 생기기도 합니다. 대부분의 AI 에이전트 관련 도구를 포괄하며 간단하게 정의하기 위해, 우리는 다음 정의를 사용합니다:

AI 에이전트는 대형 언어 모델(LLM)이 <strong>상태</strong>와 <strong>도구</strong>에 접근할 수 있도록 하여 작업을 수행할 수 있게 합니다.

![Agent Model](../../../translated_images/ko/what-agent.21f2893bdfd01e6a.webp)

이제 이 용어들을 정의해 보겠습니다:

**대형 언어 모델** - 이 강의에서 언급하는 GPT-5, GPT-4o, Llama 3.3 등과 같은 모델들입니다.

<strong>상태</strong> - LLM이 작업하는 문맥을 의미합니다. LLM은 과거 행동과 현재 문맥을 바탕으로 후속 행동을 결정합니다. AI 에이전트 프레임워크는 개발자가 이 문맥을 더 쉽게 관리할 수 있도록 도와줍니다.

<strong>도구</strong> - 사용자가 요청하고 LLM이 계획한 작업을 완수하기 위해 LLM은 도구에 접근해야 합니다. 도구의 예로는 데이터베이스, API, 외부 애플리케이션 또는 다른 LLM 등이 있습니다.

이러한 정의는 향후 구현 방식을 이해하는 데 좋은 기반이 될 것입니다. 이제 몇 가지 AI 에이전트 프레임워크를 살펴보겠습니다:

## LangChain 에이전트

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst)는 위에서 제시한 정의를 구현한 예시입니다.

<strong>상태</strong> 관리를 위해 `AgentExecutor`라는 내장 기능을 사용합니다. 이것은 정의된 `agent`와 사용 가능한 `tools`를 입력받습니다.

`Agent Executor`는 대화 기록도 저장하여 대화 문맥을 제공합니다.

![Langchain Agents](../../../translated_images/ko/langchain-agents.edcc55b5d5c43716.webp)

LangChain은 커뮤니티와 팀에서 만든 [도구 카탈로그](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)를 제공하여, 애플리케이션에 가져와 LLM이 액세스할 수 있습니다.

이러한 도구를 정의하고 `Agent Executor`에 전달할 수 있습니다.

AI 에이전트를 이야기할 때 가시성도 매우 중요한 요소입니다. 애플리케이션 개발자가 LLM이 어떤 도구를 왜 사용하는지 이해하는 것이 중요합니다. 이를 위해 LangChain 팀은 LangSmith를 개발했습니다.

## AutoGen

다음으로 알아볼 AI 에이전트 프레임워크는 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)입니다. AutoGen의 주요 초점은 대화입니다. 에이전트는 **대화 가능(conversable)** 하고 **사용자 정의 가능(customizable)** 합니다.

**대화 가능 -** LLM은 작업을 완수하기 위해 다른 LLM과 대화를 시작하고 이어갈 수 있습니다. 이는 특정 시스템 메시지를 전달하여 `AssistantAgents`를 생성함으로써 수행됩니다.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**사용자 정의 가능** - 에이전트는 LLM뿐 아니라 사용자나 도구로도 정의할 수 있습니다. 개발자는 작업 완료 피드백을 받기 위해 사용자와 상호작용하는 `UserProxyAgent`를 정의할 수 있습니다. 이 피드백은 작업을 계속 실행하거나 중단하는 데 사용할 수 있습니다.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 상태 및 도구

상태를 변경하고 관리하기 위해 어시스턴트 에이전트는 작업을 완료할 파이썬 코드를 생성합니다.

다음은 그 과정의 예입니다:

![AutoGen](../../../translated_images/ko/autogen.dee9a25a45fde584.webp)

#### 시스템 메시지로 정의된 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

이 시스템 메시지는 해당 LLM에 작업에 관련된 기능을 지정합니다. AutoGen에서는 서로 다른 시스템 메시지를 가진 여러 AssistantAgents를 가질 수 있음을 기억하세요.

#### 사용자가 대화를 시작함

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

user_proxy(사람)로부터의 이 메시지가 에이전트가 실행할 기능을 탐색하는 과정을 시작합니다.

#### 기능 실행

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

초기 대화가 처리된 후 에이전트는 호출할 도구를 제안합니다. 이 경우 `get_weather` 함수입니다. 구성에 따라 이 함수는 에이전트가 자동으로 실행하고 읽거나 사용자 입력에 따라 실행할 수 있습니다.

[AutoGen 코드 샘플](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)을 통해 빌드 시작 방법을 더 탐색할 수 있습니다.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)는 Python과 .NET에서 AI 에이전트 및 다중 에이전트 시스템을 구축하기 위한 Microsoft의 오픈 소스 SDK입니다. 이 프레임워크는 이전 두 프로젝트인 <strong>Semantic Kernel</strong>의 기업 기능과, <strong>AutoGen</strong>의 다중 에이전트 오케스트레이션을 단일 지원 프레임워크로 통합했습니다. 오늘 새 프로젝트를 시작한다면 AutoGen의 권장 후속작입니다.

이 프레임워크는 단일 <strong>채팅 에이전트</strong>부터 복잡한 <strong>다중 에이전트 워크플로우</strong>까지 확장 가능하며, Microsoft Foundry, Azure OpenAI, OpenAI와 직접 통합됩니다. OpenTelemetry를 통해 에이전트의 활동을 정확히 추적할 수 있는 내장 가시성도 제공합니다.

### 상태 및 도구

<strong>상태</strong> - 프레임워크는 <strong>스레드(thread)</strong>를 통해 대화 문맥을 관리합니다. 에이전트는 메시지 기록(사용자 요청, 도구 호출 및 결과)을 추적하여 각 턴이 이전 내용을 이어갑니다. 스레드는 저장되어 대화를 중단했다가 다시 시작할 수 있습니다.

<strong>도구</strong> - 에이전트에 도구를 주려면 일반 Python 함수를 전달합니다. 타입 주석 매개변수는 자동으로 스키마로 변환되어 모델이 호출 방법과 시기를 알게 됩니다(함수 호출). 또한 MCP 서버와 코드 인터프리터 등 호스팅 도구도 지원합니다.

다음은 사용자 정의 도구가 있는 단일 에이전트 예시입니다:

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

Microsoft Foundry에서 Azure OpenAI에 연결하려면, 클라이언트에 엔드포인트와 자격증명을 전달하면 됩니다:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 다중 에이전트 워크플로우

프레임워크가 빛을 발하는 부분은 여러 에이전트를 함께 오케스트레이션하는 부분입니다. 예를 들어, 에이전트를 순차적으로 실행(각각 컨텍스트를 다음으로 전달)하거나 여러 에이전트에 병렬로 요청하고 결과를 종합할 수 있습니다:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 에이전트를 순차적으로 실행하여 대화 맥락을 연결 고리로 전달합니다
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 에이전트들에게 병렬로 분산 실행한 후, 그들의 응답을 집계합니다
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

프레임워크 설치 및 시작 방법:

```bash
pip install agent-framework-core
# 선택적 통합
pip install agent-framework-openai       # OpenAI 및 Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

[Microsoft Agent Framework 저장소](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst)와 [공식 문서](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)에서 더 많은 내용을 탐험할 수 있습니다.

## Taskweaver

다음으로 살펴볼 에이전트 프레임워크는 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)입니다. 이 프레임워크는 `string` 대신 파이썬의 DataFrame을 사용한다는 점에서 "코드 우선(code-first)" 에이전트로 알려져 있습니다. 이것은 데이터 분석과 생성 작업에서 매우 유용합니다. 예를 들어 그래프나 차트 작성, 무작위 수 생성 등이 가능합니다.

### 상태 및 도구

대화 상태 관리를 위해 TaskWeaver는 `Planner` 개념을 사용합니다. `Planner`는 사용자의 요청을 받아 이를 완수하기 위한 작업들을 계획하는 LLM입니다.

이 작업들을 완료하기 위해 `Planner`는 `Plugins`라는 도구 모음에 접근합니다. 이 도구는 파이썬 클래스나 일반 코드 인터프리터일 수 있습니다. 이 플러그인들은 임베딩으로 저장되어 LLM이 더 정확한 플러그인을 찾아 사용할 수 있습니다.

![Taskweaver](../../../translated_images/ko/taskweaver.da8559999267715a.webp)

다음은 이상 탐지를 처리하는 플러그인 예시입니다:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

코드는 실행 전에 검증됩니다. Taskweaver에서 문맥을 관리하는 또 다른 기능은 `experience`입니다. Experience는 대화 문맥을 장기적으로 YAML 파일에 저장할 수 있게 하여, 이전 대화를 기반으로 LLM이 특정 작업을 점점 더 잘 수행하도록 설정할 수 있습니다.

## JARVIS

마지막으로 살펴볼 에이전트 프레임워크는 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)입니다. JARVIS가 독특한 점은 LLM이 대화의 `상태`를 관리하고, `도구`로서 다른 AI 모델들을 사용한다는 점입니다. 각 AI 모델은 객체 인식, 전사, 이미지 캡션 등 특정 작업을 수행하는 전문화된 모델입니다.

![JARVIS](../../../translated_images/ko/jarvis.762ddbadbd1a3a33.webp)

범용 모델인 LLM은 사용자의 요청을 받고, 특정 작업과 작업 완수에 필요한 인자/데이터를 식별합니다.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

그런 다음 LLM은 AI 모델이 해석할 수 있는 JSON과 같은 형식으로 요청을 변환합니다. AI 모델이 작업을 바탕으로 예측을 반환하면, LLM이 그 응답을 받습니다.

만약 작업 완료에 여러 모델이 필요하면, LLM은 각 모델의 응답을 해석한 후 이를 종합하여 사용자에게 최종 답변을 생성합니다.

아래 예시는 사용자가 사진 속 객체의 설명과 개수를 요청할 때 작동하는 방식을 보여줍니다:

## 과제

AI 에이전트 학습을 계속하기 위해 Microsoft Agent Framework를 사용하여 만들어 볼 수 있는 과제:

- 교육 스타트업의 여러 부서와 비즈니스 미팅을 시뮬레이션하는 애플리케이션.
- LLM이 다양한 페르소나와 우선순위를 이해하도록 안내하는 시스템 메시지를 만들고, 사용자가 신제품 아이디어를 발표할 수 있도록 지원.
- LLM은 각 부서에서 후속 질문을 생성해 발표와 제품 아이디어를 정교화하고 개선.

## 학습은 여기서 멈추지 않습니다, 여정을 계속하세요

이 강의를 마친 후, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상시키세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->