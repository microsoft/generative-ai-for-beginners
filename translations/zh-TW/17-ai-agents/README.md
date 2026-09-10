[![開源模型](../../../translated_images/zh-TW/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介紹

AI 智能代理是生成式 AI 的一個令人興奮的發展，使大型語言模型（LLM）從助手進化為能夠採取行動的代理。AI 代理框架讓開發人員能夠創建應用程式，使 LLM 可存取工具和狀態管理。這些框架還增強了可視性，讓用戶和開發人員能監控 LLM 計劃的行動，從而提升體驗管理。

本課程將涵蓋以下主題：

- 了解什麼是 AI 代理 - AI 代理究竟是什麼？
- 探索五種不同的 AI 代理框架 - 它們有何獨特之處？
- 將這些 AI 代理應用於不同案例 - 什麼時候應該使用 AI 代理？

## 學習目標

修習本課程後，你將能夠：

- 解釋 AI 代理是什麼以及其應用方式。
- 了解幾個熱門 AI 代理框架之間的差異及其不同點。
- 理解 AI 代理的運作方式，以便使用它們構建應用程式。

## 什麼是 AI 代理？

AI 代理是生成式 AI 領域中非常令人興奮的部分。但這份興奮有時也會帶來術語和應用上的混淆。為了簡化且包含大多數被稱為 AI 代理的工具，我們將採用以下定義：

AI 代理讓大型語言模型（LLM）能透過存取<strong>狀態</strong>和<strong>工具</strong>來執行任務。

![代理模型](../../../translated_images/zh-TW/what-agent.21f2893bdfd01e6a.webp)

讓我們定義這些術語：

<strong>大型語言模型</strong> - 指本課程中提到的模型，例如 GPT-5、GPT-4o 和 Llama 3.3 等。

<strong>狀態</strong> - 指 LLM 所處理的上下文。LLM 利用過往行為和當前上下文來指導後續行動的決策。AI 代理框架讓開發人員更容易維護此上下文。

<strong>工具</strong> - 為完成用戶請求且 LLM 計劃的任務，LLM 需要存取工具。工具的範例包括資料庫、API、外部應用程式甚至另一個 LLM！

這些定義將為你後續了解它們的實作方式打下良好基礎。接下來我們來探索幾種不同的 AI 代理框架：

## LangChain 代理

[LangChain 代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是上述定義的實作。

為管理<strong>狀態</strong>，它使用一個內建函式 `AgentExecutor`，接受已定義的 `agent` 及可用的 `tools`。

此 `Agent Executor` 也會儲存聊天歷史，提供聊天的上下文。

![Langchain 代理](../../../translated_images/zh-TW/langchain-agents.edcc55b5d5c43716.webp)

LangChain 提供一份可供應用程式導入的[工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，讓 LLM 可以存取。這些工具由社群與 LangChain 團隊共同製作。

你可以定義這些工具並傳遞給 `Agent Executor`。

可視性是談論 AI 代理時另一個重要面向。應用開發者需了解 LLM 使用了哪個工具及原因。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

下一個要討論的 AI 代理框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 主要聚焦於對話。代理既是<strong>可對話</strong>也是<strong>可客製化</strong>的。

**可對話 -** LLM 可與其他 LLM 啟動並持續對話以完成任務。這透過建立 `AssistantAgents` 並賦予其特定系統訊息來實現。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可客製化</strong> - 代理不僅定義為 LLM，也可以是使用者或工具。作為開發者，你可以定義一個 `UserProxyAgent`，負責與使用者互動以獲得任務完成的回饋。該回饋可繼續執行任務或停止任務。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態與工具

為變更及管理狀態，助理代理會生成 Python 程式碼以完成任務。

以下是此流程的範例：

![AutoGen](../../../translated_images/zh-TW/autogen.dee9a25a45fde584.webp)

#### 用系統訊息定義 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

此系統訊息指示此特定 LLM 相關的功能。請記得，使用 AutoGen，你可以定義多個帶有不同系統訊息的 AssistantAgents。

#### 聊天由使用者發起

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

來自 user_proxy（使用者）的訊息將開始代理探索應執行功能的流程。

#### 執行功能

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

初始聊天處理完後，代理會建議要調用的工具，此例中是名為 `get_weather` 的函式。依配置，可讓該函式自動執行並被代理讀取，或根據用戶指令執行。

你可參考 [AutoGen 程式碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) 以深入探索開始建構的方法。

## Microsoft 代理框架

[Microsoft 代理框架](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微軟的開源 SDK，用於在 **Python** 和 **.NET** 中構建 AI 代理和多代理系統。它集合了兩個早期微軟專案的優勢——企業級的 **Semantic Kernel** 與多代理協作的 **AutoGen**——成為單一支援框架。若你今天開始新代理項目，這是推薦的 AutoGen 接班人。

該框架可擴展從單一<strong>聊天代理</strong>到複雜的<strong>多代理工作流程</strong>，並且直接整合 Microsoft Foundry、Azure OpenAI 及 OpenAI。它也透過 OpenTelemetry 提供內建的可觀察性，讓你追蹤代理的確切行動。

### 狀態與工具

<strong>狀態</strong> - 框架透過 <strong>線程</strong> 為你管理對話上下文。代理會記錄訊息歷史（用戶請求、工具呼叫及其結果），每一輪對話都建立在前一輪之上。線程也可持久保存，允許對話暫停後繼續。

<strong>工具</strong> - 你可以傳入純 Python 函式為代理提供工具。帶型別註解的參數會自動轉為 schema，使模型知道如何及何時調用它們（函式呼叫）。框架也支援模型上下文協議 (MCP) 伺服器和託管工具，如程式碼解譯器。

以下是帶有自定義工具的單一代理範例：

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

若要改為連接到 Microsoft Foundry 中的 Azure OpenAI，可將端點和憑證傳給客戶端：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 多代理工作流程

框架真正出色之處在於能編排多個代理協作。例如，你可以一個接一個順序執行代理（每個代理將上下文傳給下一個代理），或並行展開多個代理並匯總結果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 依序執行代理，將對話上下文沿著串列傳遞
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 並行分派給多個代理，然後彙整他們的回應
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安裝框架並開始使用：

```bash
pip install agent-framework-core
# 選用的整合功能
pip install agent-framework-openai       # OpenAI 及 Azure OpenAI
pip install agent-framework-foundry      # 微軟 Foundry
```

你可以在 [Microsoft 代理框架倉庫](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) 與[官方文件](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)中深入探索。

## Taskweaver

下一個要探索的代理框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被稱為「以程式碼為先」的代理，因為它不僅限於操作字串，還能處理 Python 中的 DataFrame 對象。此特性在數據分析與生成任務中非常有用，比如創建圖表或生成隨機數。

### 狀態與工具

TaskWeaver 以 `Planner` 概念管理會話狀態。`Planner` 是一個 LLM，負責接收用戶請求並規劃為完成請求所需的任務。

為完成任務，`Planner` 可存取稱為 `Plugins` 的工具集合。這些可為 Python 類別或一般程式碼解譯器。這些插件以嵌入向量形式儲存，讓 LLM 更容易搜尋正確的插件。

![Taskweaver](../../../translated_images/zh-TW/taskweaver.da8559999267715a.webp)

以下是一個處理異常檢測的插件範例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

程式碼在執行前會被驗證。Taskweaver 管理上下文的另一功能是 `experience`。Experience 允許將會話上下文長期儲存在 YAML 文件中。這可設定為讓 LLM 在暴露於先前對話後，隨時間改進特定任務的表現。

## JARVIS

最後我們來看 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst) 代理框架。JARVIS 的獨特之處在於它使用 LLM 來管理會話的 `state`，而 `tools` 則是其他 AI 模型。這些 AI 模型是專門執行特定任務的模型，例如物體偵測、語音轉錄或影像標註等。

![JARVIS](../../../translated_images/zh-TW/jarvis.762ddbadbd1a3a33.webp)

作為通用模型的 LLM 接收用戶請求，識別特定任務及完成該任務所需的參數/資料。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 將請求格式化成專門 AI 模型可理解的形式，如 JSON。當 AI 模型基於任務返回預測結果後，LLM 接收該回應。

若需多個模型協同完成任務，LLM 也會先解析這些模型的回應，再綜合生成給用戶的最終回應。

下例顯示當用戶請求對一張照片中的物體進行描述和計數時的運作流程：

## 作業

繼續學習 AI 代理，嘗試用 Microsoft 代理框架構建：

- 一個模擬教育新創企業不同部門商務會議的應用程式。
- 創建系統訊息以指導 LLM 理解不同角色和優先事項，並讓用戶能提出新產品構想。
- 然後 LLM 應從各部門產生後續問題，以精煉及改善簡報和產品構想。

## 學習不止於此，繼續探索之旅

完成本課後，請參考我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->