[![開源模型](../../../translated_images/zh-MO/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介紹

AI 代理是生成式 AI 中一個令人振奮的發展，讓大型語言模型（LLM）能夠從助理演變成可以採取行動的代理。AI 代理框架讓開發者能夠創建應用，使 LLM 能夠使用工具和狀態管理。這些框架也提升了可視化，使用者和開發者可以監控 LLM 計劃的行動，從而改善體驗管理。

本課程將涵蓋以下主題：

- 理解什麼是 AI 代理 - AI 代理到底是什麼？
- 探討五種不同的 AI 代理框架 - 它們有何獨特之處？
- 將這些 AI 代理應用於不同的用例 - 何時應該使用 AI 代理？

## 學習目標

完成本課程後，你將能夠：

- 解釋 AI 代理是什麼以及如何使用。
- 了解一些流行 AI 代理框架的差異及其不同之處。
- 理解 AI 代理的運作，以構建相關應用。

## 什麼是 AI 代理？

AI 代理是生成式 AI 領域中非常令人興奮的領域。隨著這份興奮而來的，有時會造成對術語及其應用的混淆。為了簡化且涵蓋大部分自稱 AI 代理的工具，我們將採用以下定義：

AI 代理讓大型語言模型（LLM）能透過獲取<strong>狀態</strong>和<strong>工具</strong>來執行任務。

![代理模型](../../../translated_images/zh-MO/what-agent.21f2893bdfd01e6a.webp)

讓我們定義這些詞彙：

<strong>大型語言模型</strong> - 指本課程中提及的模型，例如 GPT-5、GPT-4o 和 Llama 3.3 等。

<strong>狀態</strong> - 指 LLM 所處的上下文。LLM 使用過去行為和目前上下文的背景，引導其對後續行動的決策。AI 代理框架讓開發者更容易維護這樣的上下文。

<strong>工具</strong> - 為完成用戶請求且 LLM 已規劃的任務，LLM 需要存取工具。工具的例子可以是資料庫、API、外部應用甚至是另一個 LLM！

這些定義希望能為後續了解它們如何實作打下良好基礎。讓我們來探索幾個不同的 AI 代理框架：

## LangChain 代理

[LangChain 代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是上述定義的實作。

為管理<strong>狀態</strong>，它使用一個內建函數稱為 `AgentExecutor`。它接受已定義的 `agent` 和可用的 `工具`。

`Agent Executor` 也會儲存聊天歷史以提供聊天上下文。

![Langchain Agents](../../../translated_images/zh-MO/langchain-agents.edcc55b5d5c43716.webp)

LangChain 提供一個[工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可匯入您的應用程式，供 LLM 存取。這些工具由社群和 LangChain 團隊製作。

你可以定義這些工具並傳遞給 `Agent Executor`。

在談論 AI 代理時，可視化也是一項重要的方面。應用開發者需了解 LLM 正在使用哪個工具及原因。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

接下來要討論的 AI 代理框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 的主要焦點是對話。代理既是<strong>可對話的</strong>，也是<strong>可定制的</strong>。

<strong>可對話的</strong> - LLM 可以啟動以及繼續與另一個 LLM 的對話，以完成任務。這是透過創建 `AssistantAgents` 並給予特定系統消息來完成的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可定制的</strong> - 代理不僅可定義為 LLM，也可以是使用者或工具。作為開發者，你可以定義一個 `UserProxyAgent` 負責與使用者互動以取得任務完成的回饋。該回饋可用以繼續或停止任務執行。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態與工具

要變更和管理狀態，助手代理會生成 Python 代碼來完成任務。

以下是一個過程範例：

![AutoGen](../../../translated_images/zh-MO/autogen.dee9a25a45fde584.webp)

#### 使用系統消息定義的 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

此系統消息指示該特定 LLM 哪些函數與其任務相關。請記住，AutoGen 允許多個具有不同系統消息的 AssistantAgents 同時定義。

#### 聊天由使用者啟動

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

來自 user_proxy（人類）的此訊息會啟動代理探索應執行的可能函數過程。

#### 執行函數

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

初始聊天處理後，代理會發送建議調用的工具，此例中為名為 `get_weather` 的函數。根據你的配置，此函數可自動執行並被代理讀取，或根據使用者輸入執行。

你可以在此找到更多 [AutoGen 程式碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)，以進一步探索如何開始建構。

## 微軟代理框架

[微軟代理框架](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微軟的開源 SDK，用於在 **Python** 和 **.NET** 中構建 AI 代理和多代理系統。它結合了兩個早期微軟專案的優勢——具企業特色的 **Semantic Kernel** 以及多代理編排的 **AutoGen** ——整合成一個支援框架。如果你今天要開始一個新的代理專案，這是 AutoGen 的推薦繼任者。

該框架可從單一 <strong>聊天代理</strong> 擴展到複雜的 <strong>多代理工作流程</strong>，並且直接整合 Microsoft Foundry、Azure OpenAI 和 OpenAI。它還透過 OpenTelemetry 提供內建的可觀察性，讓你能精確追蹤代理的行為。

### 狀態與工具

<strong>狀態</strong> - 此框架透過 **threads** 管理會話上下文。代理追蹤訊息歷史（使用者請求、工具調用及其結果），使每輪對話根據之前內容進行。线程可以持久化，允許會話暫停後續續。

<strong>工具</strong> - 你可以透過傳遞普通 Python 函數給代理。帶有類型註解的參數會自動轉成結構化 schema，讓模型明白何時以及如何呼叫它們（函數調用）。框架也支持 Model Context Protocol（MCP）伺服器與代碼解釋器等託管工具。

這裡示範一個含自訂工具的單一代理範例：

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

若要連接 Microsoft Foundry 的 Azure OpenAI，請將你的端點和認證傳給客戶端：

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

該框架真正出色之處在於協調多個代理。例如，你可以依序運行多個代理（由前一個代理傳遞上下文給下一個）或多工平行運作多個代理並集成它們的結果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 按順序執行代理，沿鏈傳遞對話上下文
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 並行分派給代理，然後彙總他們的回應
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

若要安裝框架並開始使用：

```bash
pip install agent-framework-core
# 可選整合
pip install agent-framework-openai       # OpenAI 與 Azure OpenAI
pip install agent-framework-foundry      # 微軟 Foundry
```

你可以在 [微軟代理框架儲存庫](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) 和 [官方文件](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)深入探索更多。

## Taskweaver

接著我們來探索 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst) 代理框架。它被稱為「程式碼優先」代理，因為它不僅僅只處理 `strings`，還可以操作 Python 中的資料框 (DataFrames)。這對於資料分析和生成任務非常有用，比如繪製圖表或產生隨機數字。

### 狀態與工具

TaskWeaver 透過 `Planner` 概念管理對話狀態。`Planner` 是一個 LLM，負責接收使用者請求並規劃完成此請求所需的任務。

為了完成任務，`Planner` 可存取稱為 `Plugins` 的工具集合。這些可以是 Python 類別或一般代碼解釋器。這些插件會以向量嵌入的方式儲存，便於 LLM 搜索正確的插件。

![Taskweaver](../../../translated_images/zh-MO/taskweaver.da8559999267715a.webp)

以下是一個處理異常檢測的插件範例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

執行前會對代碼進行驗證。Taskweaver 中管理上下文的另一項功能是 `experience`。Experience 允許長期將對話上下文存成 YAML 檔。這可以被配置，使 LLM 在接觸到以前的對話時，能在某些任務上隨時間改善。

## JARVIS

最後我們將探索的代理框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS 的獨特之處在於它使用 LLM 來管理對話的 `狀態`，而 `工具` 則是其他 AI 模型。這些 AI 模型都是專門用於執行特定任務，如物件偵測、轉錄或影像說明等。

![JARVIS](../../../translated_images/zh-MO/jarvis.762ddbadbd1a3a33.webp)

作為通用模型的 LLM，接收來自使用者的請求，並識別特定任務及完成任務所需的參數/資料。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 接著將請求格式化成專門 AI 模型能理解的格式，像是 JSON。當 AI 模型根據任務回傳其預測後，LLM 接收該回應。

若任務需要多個模型協同完成，LLM 也會解讀這些模型的回應，然後將它們整合產生對使用者的回答。

下面的範例展示當使用者在圖片中請求物件的描述和數量時，這個流程如何運作：

## 作業

若要繼續學習 AI 代理，你可以使用微軟代理框架構建：

- 一個模擬教育新創公司不同部門商業會議的應用。
- 創建系統消息，引導 LLM 理解不同角色和優先事項，並讓使用者提案新產品構想。
- LLM 應從每個部門生成後續問題，以細化並改進提案和產品構想。

## 學習不止於此，繼續探索旅程

完成本課程後，請查看我們的[生成式 AI 學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->