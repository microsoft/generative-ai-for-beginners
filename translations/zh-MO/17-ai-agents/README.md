[![開放原始碼模型](../../../translated_images/zh-MO/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介紹

AI 代理人是生成式 AI 中令人興奮的發展，使大型語言模型 (LLMs) 從助理進化為能夠採取行動的代理人。AI 代理人框架使開發者能夠創建應用程式，讓 LLMs 獲得工具和狀態管理的訪問權限。這些框架還提高了可見性，使用戶和開發者能夠監控 LLMs 計劃的行動，從而提升體驗管理。

本課程將涵蓋以下範疇：

- 理解什麼是 AI 代理人 — AI 代理人究竟是什麼？
- 探索五個不同的 AI 代理人框架 — 它們有何獨特之處？
- 將這些 AI 代理人應用於不同的使用案例 — 何時應使用 AI 代理人？

## 學習目標

完成本課程後，你將能夠：

- 解釋什麼是 AI 代理人以及如何使用它們。
- 了解一些流行的 AI 代理人框架間的差異以及它們的不同之處。
- 理解 AI 代理人的運作方式，以便使用它們來構建應用程式。

## 什麼是 AI 代理人？

AI 代理人是生成式 AI 世界中非常令人興奮的領域。這種興奮有時也會帶來術語和應用方面的混淆。為了簡化並包容大多數提及 AI 代理人的工具，我們將使用以下定義：

AI 代理人允許大型語言模型 (LLMs) 通過獲取<strong>狀態</strong>和<strong>工具</strong>來執行任務。

![Agent Model](../../../translated_images/zh-MO/what-agent.21f2893bdfd01e6a.webp)

讓我們定義這些術語：

<strong>大型語言模型</strong> — 這是本課程中提及的模型，例如 GPT-3.5、GPT-4、Llama-2 等。

<strong>狀態</strong> — 指的是 LLM 工作的上下文。LLM 使用其過去行動和當前上下文，指導其對後續行動的決策。AI 代理人框架使開發者更容易維護此上下文。

<strong>工具</strong> — 為完成用戶請求且由 LLM 規劃的任務，LLM 需要訪問工具。工具的一些範例包括資料庫、API、外部應用程式或甚至其他 LLM！

這些定義希望能為你打下良好基礎，接著我們將看看它們如何被實作。讓我們探索幾個不同的 AI 代理人框架：

## LangChain 代理人

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是上述定義的實作。

為了管理<strong>狀態</strong>，它使用一個內建功能叫做 `AgentExecutor`。這個功能接受定義好的 `agent` 和可用的 `tools`。

`Agent Executor` 也會儲存對話歷史，以提供對話上下文。

![Langchain Agents](../../../translated_images/zh-MO/langchain-agents.edcc55b5d5c43716.webp)

LangChain 提供了一個[工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可以被匯入你的應用程式，供 LLM 取得。這些工具是由社區和 LangChain 團隊製作。

你可以定義這些工具並將它們傳遞給 `Agent Executor`。

在談論 AI 代理人時，可視性是另一個重要面向。應用程式開發者需要了解 LLM 正在使用哪個工具以及原因。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

下一個我們將討論的 AI 代理人框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 的主要焦點是對話。代理人既是<strong>可對話的</strong>也是<strong>可自訂的</strong>。

**可對話的 -** LLM 能開始並持續與另一個 LLM 的對話以完成任務。這是通過建立 `AssistantAgents` 並給予它們特定的系統信息來實現的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可自訂的</strong> — 代理人不僅可被定義為 LLM，也可以是使用者或工具。作為開發者，你可以定義一個 `UserProxyAgent`，負責與使用者互動以收集反饋，協助完成任務。該反饋可以是繼續執行任務或停止任務。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態與工具

為了變更和管理狀態，一個助理代理人會生成 Python 程式碼來完成任務。

以下是一個流程示例：

![AutoGen](../../../translated_images/zh-MO/autogen.dee9a25a45fde584.webp)

#### 使用系統信息定義 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

該系統信息指導此特定 LLM 哪些函數與其任務相關。記得，使用 AutoGen 你可以定義多個擁有不同系統信息的 AssistantAgents。

#### 對話由使用者發起

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

這條來自 user_proxy（人類）的訊息將啟動代理人探索應該執行的可能函數流程。

#### 函數執行

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

一旦初始對話處理完成，代理人將發送建議的工具呼叫。在此情況下，是一個叫做 `get_weather` 的函數。依據你的配置，該函數可以自動被執行並由代理人讀取，也可以根據用戶輸入執行。

你可以在這裡找到 [AutoGen 代碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)，進一步了解如何開始構建。

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微軟用於構建 AI 代理人與多代理系統的開源 SDK，支援 **Python** 與 **.NET**。它整合了先前兩個微軟專案的優勢 — 企業級功能的 **Semantic Kernel** 以及多代理協調的 **AutoGen** — 成為一個統一且有支援的框架。如果你今天開始新的代理人專案，推薦使用這個取代 AutoGen 的框架。

該框架可擴展，從單一<strong>聊天代理人</strong>到複雜的<strong>多代理工作流程</strong>，並且可直接結合 Microsoft Foundry、Azure OpenAI 及 OpenAI。它還通過 OpenTelemetry 內建可觀察性，讓你能精確追蹤代理人的執行狀況。

### 狀態與工具

<strong>狀態</strong> — 框架透過<strong>線程 (threads)</strong> 幫你管理對話上下文。代理人會追蹤消息歷史（用戶請求、工具調用及其結果），每一步建立在前一步基礎上。線程也可持久化，允許對話暫停後繼續。

<strong>工具</strong> — 你可以透過傳遞純 Python 函式給代理人。帶有類型註解的參數會自動轉為 schema，讓模型知道如何及何時呼叫（函式呼叫）。該框架同時支援模型上下文協議 (Model Context Protocol, MCP) 伺服器及托管工具，如程式碼解譯器。

以下是一個帶有自訂工具的單一代理人範例：

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

若要改為連接 Azure OpenAI 中的 Microsoft Foundry，請將端點和憑證傳遞給用戶端：

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

該框架真正出色之處在於協調多個代理人。舉例來說，你可以讓代理人依序執行（每個將上下文傳遞給下一個），或並行展開給多個代理人，並集合其結果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 依序執行代理，沿著鏈條傳遞對話上下文
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 同時分派給多個代理，然後匯總他們的回應
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安裝框架並開始：

```bash
pip install agent-framework-core
# 可選整合
pip install agent-framework-openai       # OpenAI 同 Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

你可以在 [Microsoft Agent Framework 倉庫](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) 與[官方文檔](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)中探索更多。

## Taskweaver

下一個我們將探討的代理人框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被稱為「程式碼優先」代理人，因為它不僅限於處理`字串`，還能操作 Python 中的 DataFrame。這在資料分析與生成任務中特別有用，例如製作圖表或產生隨機數字。

### 狀態與工具

TaskWeaver 通過 `Planner` 概念管理對話狀態。`Planner` 是一個 LLM，它接收用戶的請求並規劃完成該請求所需的任務。

為了完成任務，`Planner` 可使用一組稱為 `Plugins` 的工具。這可以是 Python 類別或通用程式碼解譯器。這些插件會以嵌入向量形式儲存，使 LLM 能更好地搜尋合適的插件。

![Taskweaver](../../../translated_images/zh-MO/taskweaver.da8559999267715a.webp)

這是一個處理異常檢測的插件範例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

程式碼執行前會先被驗證。Taskweaver 管理上下文的另一個功能是 `experience`。Experience 允許將對話上下文長期存儲於 YAML 檔案中。配置後，LLM 可隨時間累積過往對話經驗，提升特定任務的表現。

## JARVIS

最後一個我們將探索的代理人框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS 的獨特之處在於它使用 LLM 來管理對話`狀態`，而`工具`則是其他 AI 模型。這些 AI 模型皆是專門執行特定任務的專用模型，如物體檢測、轉錄或圖像說明。

![JARVIS](../../../translated_images/zh-MO/jarvis.762ddbadbd1a3a33.webp)

作為通用模型的 LLM 接收使用者請求，識別具體任務及完成任務所需的參數/資料。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 將請求格式化成專用 AI 模型可解讀的格式，例如 JSON。AI 模型根據任務返回預測結果後，LLM 接收回應。

若任務需要多個模型，LLM 也會解析它們的回應，再整合產生給使用者的回覆。

以下範例展示使用者請求圖片中物件的描述與計數時的執行方式：

## 作業

持續學習 AI 代理人，你可以使用 Microsoft Agent Framework 構建：

- 一個模擬教育新創公司不同部門商務會議的應用程式。
- 創建系統訊息，以引導 LLM 理解不同的角色與優先事項，並讓使用者能夠推銷新產品概念。
- LLM 隨後應產生來自各部門的後續問題，以完善和改進推銷及產品概念。

## 學習不止於此，繼續旅程

完成本課程後，可查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->