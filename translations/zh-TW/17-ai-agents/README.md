[![開源模型](../../../translated_images/zh-TW/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介紹

AI 代理代表了生成式 AI 領域中一項令人振奮的發展，使大型語言模型（LLM）從助理進化成能夠採取行動的代理。AI 代理框架讓開發者能夠創建應用程式，使 LLM 能夠存取工具與狀態管理。這些框架還增強了可見性，讓使用者和開發者能監控 LLM 計畫採取的行動，從而改進體驗管理。

本課程將涵蓋以下主題：

- 了解什麼是 AI 代理——AI 代理究竟是什麼？
- 探索五款不同的 AI 代理框架——它們有何獨特之處？
- 將這些 AI 代理應用於不同案例——何時應該使用 AI 代理？

## 學習目標

完成本課程後，您將能夠：

- 解釋 AI 代理是什麼以及它們如何被使用。
- 了解一些熱門 AI 代理框架的差異以及它們的不同之處。
- 了解 AI 代理如何運作，以便構建應用程式。

## 什麼是 AI 代理？

AI 代理是生成式 AI 世界中一個非常令人興奮的領域。隨著這股熱潮，有時也會產生一些術語及其應用的混淆。為了保持簡單並包容大部分被稱為 AI 代理的工具，我們將採用以下定義：

AI 代理允許大型語言模型（LLM）通過給予它們<strong>狀態</strong>和<strong>工具</strong>的存取權來執行任務。

![代理模型](../../../translated_images/zh-TW/what-agent.21f2893bdfd01e6a.webp)

讓我們定義這些術語：

<strong>大型語言模型</strong>——指本課程中提及的模型，如 GPT-3.5、GPT-4、Llama-2 等。

<strong>狀態</strong>——指的是 LLM 運作時所處的上下文。LLM 利用過去的行動及當前的背景上下文，引導其接下來的決策。AI 代理框架讓開發者更容易維護這些上下文。

<strong>工具</strong>——為了完成用戶要求且由 LLM 計畫的任務，LLM 需要存取各種工具。工具例子包括資料庫、API、外部應用程式甚至是另一個 LLM！

這些定義希望能為您打下良好的基礎，讓我們接著來看看它們如何被實現。讓我們探索幾個不同的 AI 代理框架：

## LangChain 代理

[LangChain 代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是上述定義的實作。

它使用內建函式 `AgentExecutor` 來管理<strong>狀態</strong>。此函式接受已定義的 `agent` 和可用的 `tools`。

`AgentExecutor` 也會儲存聊天歷史，以提供聊天的上下文。

![Langchain 代理](../../../translated_images/zh-TW/langchain-agents.edcc55b5d5c43716.webp)

LangChain 提供一個[工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可以進口到您的應用程式中供 LLM 使用。這些工具由社群和 LangChain 團隊製作。

您可以定義這些工具並傳遞給 `AgentExecutor`。

在談論 AI 代理時，可見性也是另一個重要面向。應用程式開發者需了解 LLM 正在使用哪個工具及原因。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

下一個我們要介紹的 AI 代理框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 主要聚焦於對話。代理既是<strong>會話式</strong>，也是<strong>可自訂的</strong>。

**會話式——**LLM 可以與其他 LLM 開始並持續對話以完成任務。這是透過建立 `AssistantAgents` 並給予它們特定的系統訊息來實現的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可自訂</strong>——代理不僅能定義為 LLM，也能是使用者或工具。作為開發者，您可以定義一個 `UserProxyAgent`，負責與使用者互動以取得反饋，協助任務完成。反饋可用於繼續或終止任務執行。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態和工具

為了變更和管理狀態，一個助理代理會產生 Python 程式碼來完成任務。

以下是此過程的範例：

![AutoGen](../../../translated_images/zh-TW/autogen.dee9a25a45fde584.webp)

#### 由系統訊息定義的 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

這個系統訊息指示特定 LLM 哪些功能與任務相關。記住，在 AutoGen 中，您可以定義多個具有不同系統訊息的 AssistantAgents。

#### 使用者發起聊天

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

來自 user_proxy（人類）的訊息會啟動代理探索應該執行哪些函數的過程。

#### 執行函數

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

初始聊天處理完成後，代理會發出建議工具調用。在此案例中是一個名為 `get_weather` 的函數。根據設定，此函數可由代理自動執行和讀取，或依照使用者輸入執行。

您可以在這裡找到更多 [AutoGen 程式碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)，深入探索如何開始建置。

## 微軟代理框架

[微軟代理框架](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微軟開源的 SDK，適用於構建 AI 代理及多代理系統，支援 **Python** 與 **.NET**。它結合了兩個先前微軟專案的優勢——企業功能的 **Semantic Kernel** 與多代理協調的 **AutoGen**——整合成一個單一且有支援的框架。如果您今天開始新代理專案，建議採用此框架替代 AutoGen。

該框架可從單一 <strong>聊天代理</strong> 擴展到複雜的 <strong>多代理工作流</strong>，並且能直接整合 Microsoft Foundry、Azure OpenAI 與 OpenAI。它也提供透過 OpenTelemetry 內建的可觀察性功能，可精確追蹤代理的行動。

### 狀態和工具

<strong>狀態</strong>——框架透過 **執行緒 (threads)** 管理對話上下文。代理會追蹤訊息歷史（使用者請求、工具呼叫及其結果），使每輪對話建立於之前基礎上。執行緒也可被持久化，使對話能暫停且稍後繼續。

<strong>工具</strong>——您可透過傳遞普通 Python 函式給代理。型別註解參數會自動轉換成架構(schema)，讓模型知道如何及何時呼叫（函式調用）。該框架也支援模型上下文協定（Model Context Protocol, MCP）伺服器與代碼解釋器等託管工具。

以下是一個帶有自訂工具的單一代理範例：

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

若要改為在 Microsoft Foundry 連接 Azure OpenAI，請將端點與憑證傳遞給用戶端：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 多代理工作流

此框架真正出色的地方在於協調多個代理一起工作。例如，您可以依序執行代理（各自將狀態傳遞給下一個）或平行將任務分派給多個代理，然後整合他們的結果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 按順序運行代理，將對話上下文沿鏈傳遞
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 並行分發給代理，然後聚合他們的回應
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安裝框架並開始使用：

```bash
pip install agent-framework-core
# 選用整合方案
pip install agent-framework-openai       # OpenAI 與 Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

您可以在 [微軟代理框架儲存庫](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) 和[官方文件](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)中探索更多內容。

## Taskweaver

下一個我們要探索的代理框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被稱為「以程式碼為主」的代理，因為它不只用處理 `string` 而是可操作 Python 中的 DataFrames。這對資料分析和生成任務非常有用，比如建立圖表和生成隨機數字。

### 狀態和工具

TaskWeaver 透過 `Planner` 概念管理對話狀態。`Planner` 是一個 LLM，負責接收用戶請求並規劃需完成的任務。

為了完成任務，`Planner` 可存取稱為 `Plugins` 的工具集合，這些工具可為 Python 類別或一般代碼解釋器。這些插件以嵌入向量儲存，好讓 LLM 更好地搜尋正確插件。

![Taskweaver](../../../translated_images/zh-TW/taskweaver.da8559999267715a.webp)

以下是處理異常檢測的插件範例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

代碼在執行前會經過驗證。Taskweaver 另一個管理上下文的特性是 `experience`。Experience 允許對話上下文長期存儲在 YAML 文件中。這可以設定，使 LLM 隨時間在接觸到以往對話的情況下持續進步特定任務。

## JARVIS

最後一個我們要探索的代理框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS 獨特之處在於它使用 LLM 管理對話的 `state`，而 `tools` 是其他 AI 模型。每個 AI 模型都是專門完成特定任務的模型，如物體偵測、語音轉錄或圖像標註。

![JARVIS](../../../translated_images/zh-TW/jarvis.762ddbadbd1a3a33.webp)

作為通用模型的 LLM 接收使用者請求，識別特定任務及完成任務所需的任何參數/資料。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 接著將請求格式化成專門 AI 模型能解讀的格式，如 JSON。AI 模型根據任務返還預測結果後，LLM 會收到回應。

若一個任務需多個模型共同完成，LLM 也會解析這些模型回應，然後整合生成回覆給使用者。

下例展示了當用戶請求圖片中的物體描述和數量時，這個流程如何運作：

## 作業

為了持續學習 AI 代理，您可以使用微軟代理框架打造：

- 一款模擬教育新創公司不同部門商務會議的應用程式。
- 創建系統訊息，引導 LLM 理解不同角色與優先事項，並讓使用者能推銷新的產品想法。
- 讓 LLM 產生各部門的後續問題，以細化和改進推銷與產品構想。

## 學習不止於此，繼續前行

完成本課程後，歡迎瀏覽我們的[生成式 AI 學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->