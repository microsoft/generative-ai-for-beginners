[![Open Source Models](../../../translated_images/zh-HK/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介紹

AI 代理代表生成式 AI 領域中的一個令人興奮的發展，使大型語言模型（LLM）能夠從助理發展為能夠採取行動的代理。AI 代理框架讓開發人員能夠創建應用程式，賦予 LLM 訪問工具與狀態管理的能力。這些框架還增強了可視性，讓用戶和開發者能夠監控 LLM 計劃的行動，從而改善體驗管理。

本課程將涵蓋以下幾個方面：

- 理解什麼是 AI 代理 - AI 代理到底是什麼？
- 探索五種不同的 AI 代理框架 - 它們有何獨特之處？
- 將這些 AI 代理應用於不同用例 - 什麼時候應該使用 AI 代理？

## 學習目標

完成本課程後，您將能夠：

- 解釋什麼是 AI 代理以及它們如何被使用。
- 了解一些流行的 AI 代理框架之間的差異及其不同之處。
- 理解 AI 代理的運作方式，從而構建相應的應用程式。

## 什麼是 AI 代理？

AI 代理是生成式 AI 領域中一個非常令人興奮的領域。但隨著興奮也可能帶來術語和應用上的混淆。為了保持簡單並涵蓋多數被稱為 AI 代理的工具，我們採用以下定義：

AI 代理允許大型語言模型（LLM）通過賦予其訪問<strong>狀態</strong>和<strong>工具</strong>來執行任務。

![Agent Model](../../../translated_images/zh-HK/what-agent.21f2893bdfd01e6a.webp)

讓我們來定義一下這些術語：

<strong>大型語言模型</strong> - 指本課程中所提及的模型，如 GPT-3.5、GPT-4、Llama-2 等。

<strong>狀態</strong> - 指的是 LLM 所處的上下文環境。LLM 利用過去行為及當前上下文做為後續決策的依據。AI 代理框架讓開發者更容易維護這個上下文。

<strong>工具</strong> - 為了完成用戶已請求且 LLM 計劃好的任務，LLM 需要訪問工具。工具範例包括數據庫、API、外部應用程式甚至另一個 LLM！

這些定義希望會為你奠定良好的基礎，接下來我們來看看這些定義如何在不同 AI 代理框架中實現，我們探索幾個不同 AI 代理框架：

## LangChain 代理

[LangChain 代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是上述定義的實現。

為了管理<strong>狀態</strong>，它使用一個內建函數叫做 `AgentExecutor`。此函數接受定義好的 `agent` 和可用的 `tools`。

`Agent Executor` 還會儲存聊天歷史，以提供聊天上下文。

![Langchain Agents](../../../translated_images/zh-HK/langchain-agents.edcc55b5d5c43716.webp)

LangChain 提供了一個[工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，這些工具可匯入您的應用程式供 LLM 訪問。這些工具來自社群及 LangChain 團隊。

之後你可以定義這些工具並傳給 `Agent Executor`。

當提到 AI 代理時，可視性是另一個重要方面。應用程式開發者須理解 LLM 正在使用哪個工具及使用原因。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

下一個我們要討論的 AI 代理框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 的主要焦點是對話。代理同時具備 <strong>可對話性</strong> 和 <strong>可定制性</strong>。

**可對話性－** LLM 可以開始並持續與另一個 LLM 對話以完成任務。這是透過創建 `AssistantAgents` 並給予它們特定系統訊息實現的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可定制性</strong>－代理不僅可定義為 LLM，也可為用戶或工具。作為開發者，你可以定義一個 `UserProxyAgent`，負責與用戶互動以獲取完成任務的反饋。該反饋可繼續執行任務或停止它。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態和工具

為了改變和管理狀態，輔助代理會生成 Python 代碼以完成任務。

以下是該過程的範例：

![AutoGen](../../../translated_images/zh-HK/autogen.dee9a25a45fde584.webp)

#### 用系統訊息定義的 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

此系統訊息指引特定的 LLM 哪些功能與任務相關。請記住，使用 AutoGen 你可以定義多個具有不同系統訊息的 AssistantAgents。

#### 聊天由用戶發起

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

來自 user_proxy（人類）的訊息會啟動代理探索其應執行功能的過程。

#### 執行函數

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

處理初始聊天後，代理會送出建議調用的工具，這裡是名為 `get_weather` 的函數。根據配置，此函數可自動執行並讀取，也可由用戶輸入執行。

你可以在 [AutoGen 代碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) 找到更多範例學習如何快速開始。

## 微軟代理框架

[Microsoft 代理框架](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微軟針對建立 AI 代理和多代理系統，支援 **Python** 及 **.NET** 的開源 SDK。它結合了兩個早期專案的優勢 — **Semantic Kernel** 的企業功能和 **AutoGen** 的多代理協調 — 成為單一受支持框架。若你今天開始新代理專案，建議使用此框架取代 AutoGen。

這個框架能從單一<strong>聊天代理</strong>擴展到複雜的<strong>多代理工作流程</strong>，且可直接整合 Microsoft Foundry、Azure OpenAI 與 OpenAI。它還提供透過 OpenTelemetry 內建的可觀測性，讓你能精確追蹤代理行為。

### 狀態和工具

<strong>狀態</strong> - 框架透過<strong>線程</strong>幫你管理對話上下文。代理會追蹤訊息歷史（用戶請求、工具調用及結果），讓每個回合建立於前一次基礎。線程也可持久化，允許對話暫停並稍後恢復。

<strong>工具</strong> - 你可通過傳入普通 Python 函數賦予代理工具。帶類型標註的參數會自動轉成 schema，讓模型知道何時及如何調用（函數調用）。框架還支援模型上下文協議（MCP）伺服器及代碼解釋器等托管工具。

以下是一個帶自定義工具的單代理範例：

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

如需連接 Microsoft Foundry 中的 Azure OpenAI，則將端點與憑證傳給客戶端：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 多代理工作流程

框架真正強大的地方在於協調多個代理。例如，你可以讓代理一個接一個執行（每個代理將其上下文傳給下一個），或並行啟動多個代理後整合其結果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 按順序運行代理，沿鏈條傳遞對話上下文
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 並行分發到代理，然後彙總他們的回應
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安裝框架並開始使用：

```bash
pip install agent-framework-core
# 可選整合
pip install agent-framework-openai       # OpenAI 同 Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

你可以在 [Microsoft Agent Framework 儲存庫](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) 和[官方文件](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)探索更多。

## Taskweaver

下一個代理框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被稱為「以代碼為先」的代理，因為它不僅僅操作 `string`，還能處理 Python 中的 DataFrame，這對數據分析和生成任務非常有用，例如製作圖表或生成隨機數。

### 狀態和工具

為管理對話狀態，TaskWeaver 使用 `Planner` 概念。`Planner` 是 LLM，接收用戶請求並規劃完成該請求所需的任務。

為完成任務，`Planner` 能訪問稱為 `Plugins` 的工具集合，這些可能是 Python 類或通用代碼解譯器。插件以嵌入的形式存儲，以幫助 LLM 更好搜索適合的插件。

![Taskweaver](../../../translated_images/zh-HK/taskweaver.da8559999267715a.webp)

以下是一個處理異常檢測的插件示例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

執行前會先驗證代碼。Taskweaver 管理上下文的另一功能是 `experience`。Experience 允許對話的上下文長期存储於 YAML 文件中。這樣配置後，LLM 隨著接觸更多先前對話，能在某些任務上逐步改進。

## JARVIS

最後要介紹的代理框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS 的獨特之處在於它使用 LLM 管理對話的 `狀態`，而 `工具` 則是其他專門的 AI 模型。每個模型都專精某些任務，如物件檢測、語音轉錄或圖像說明。

![JARVIS](../../../translated_images/zh-HK/jarvis.762ddbadbd1a3a33.webp)

作為通用模型的 LLM 接收用戶請求，辨識具體任務及完成該任務所需的參數/資料。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 隨後將請求格式化成專用 AI 模型可理解的格式，例如 JSON。AI 模型完成預測任務後返回結果，LLM 接收該響應。

若任務需多個模型完成，LLM 會解讀多個模型回應後整合，再產生最終回答。

下方範例展示當用戶請求圖片中物件描述及計數時的流程：

## 作業

為了持續學習 AI 代理，您可以使用 Microsoft 代理框架創建：

- 一個模擬教育新創公司不同部門業務會議的應用程式。
- 建立系統訊息，引導 LLM 理解不同角色與優先事項，讓用戶能提出新產品概念。
- 然後由 LLM 根據各部門追問的疑問，優化與完善提案及產品概念。

## 學習不止於此，繼續前進

完成本課程後，可瀏覽我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->