[![開源模型](../../../translated_images/zh-HK/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介紹

AI 代理是生成式 AI 中一個令人興奮的發展，讓大型語言模型（LLM）從助手進化為能夠採取行動的代理。AI 代理框架讓開發者能夠創建應用程式，賦予 LLM 使用工具和狀態管理的能力。這些框架還增強了可視性，使用戶和開發者能夠監控 LLM 計劃的行動，從而提升體驗管理。

本課程將涵蓋以下領域：

- 了解什麼是 AI 代理 - AI 代理到底是什麼？
- 探索五種不同的 AI 代理框架 - 它們的獨特之處是什麼？
- 將這些 AI 代理應用於不同的用例 - 何時應該使用 AI 代理？

## 學習目標

完成本課程後，您將能夠：

- 解釋什麼是 AI 代理以及它們如何被使用。
- 了解一些流行的 AI 代理框架之間的差異，以及它們如何不同。
- 理解 AI 代理的運作方式，從而建立相關應用程式。

## 什麼是 AI 代理？

AI 代理是生成式 AI 領域中非常令人興奮的一環。隨著興奮而來的，有時也會對術語及其應用產生混淆。為了簡化並涵蓋大部分稱為 AI 代理的工具，我們將採用以下定義：

AI 代理讓大型語言模型（LLM）能透過獲得<strong>狀態</strong>和<strong>工具</strong>來執行任務。

![代理模型](../../../translated_images/zh-HK/what-agent.21f2893bdfd01e6a.webp)

我們來定義這些術語：

<strong>大型語言模型</strong> - 指本課程中提及的模型，如 GPT-5、GPT-4o 及 Llama 3.3 等。

<strong>狀態</strong> - 指 LLM 正在運作的上下文情境。LLM 利用過往行動和當前情境指導其後續決策。AI 代理框架讓開發者更容易維護這些上下文。

<strong>工具</strong> - 為完成用戶要求且 LLM 已計劃的任務，LLM 需要使用工具。一些工具範例如資料庫、API、外部應用程式甚至其他 LLM！

這些定義希望能為你奠定良好基礎，接下來我們將探討它們如何被實作。讓我們探索幾種不同的 AI 代理框架：

## LangChain 代理

[LangChain 代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是我們上述定義的實作。

為管理<strong>狀態</strong>，它使用一個內建函式稱為 `AgentExecutor`。此函式接受已定義的 `agent` 和可用的 `tools`。

`AgentExecutor` 同時儲存聊天歷史以提供聊天上下文。

![Langchain 代理](../../../translated_images/zh-HK/langchain-agents.edcc55b5d5c43716.webp)

LangChain 提供一個可以匯入您的應用程式並供 LLM 使用的 [工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)。這些工具由社群及 LangChain 團隊製作。

您可以定義這些工具並傳入 `AgentExecutor`。

可視化是討論 AI 代理時另一重要方面。應用開發者需了解 LLM 使用的是哪個工具及使用原因。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

下一個我們將討論的 AI 代理框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 主要聚焦於對話。代理既是 <strong>可對話的</strong>，又是 <strong>可自定義的</strong>。

**可對話的 -** LLMs 能與另一個 LLM 開始並持續對話來完成任務。這是透過創建 `AssistantAgents` 並給予其特定的系統訊息來實現。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可自定義</strong> - 代理不僅可定義為 LLM，也可是使用者或工具。作為開發者，您可以定義一個 `UserProxyAgent`，負責與使用者互動，收集完成任務的回饋。此回饋可用於繼續執行或停止任務。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態與工具

要修改和管理狀態，助理代理會生成 Python 代碼來完成任務。

以下是流程示例：

![AutoGen](../../../translated_images/zh-HK/autogen.dee9a25a45fde584.webp)

#### 用系統訊息定義 LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

此系統訊息指示該 LLM 哪些函數與其任務相關。請記住，在 AutoGen 中您可以定義多個擁有不同系統訊息的 AssistantAgents。

#### 聊天由用戶發起

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

這條來自 user_proxy（人類）的訊息將啟動代理探索應執行函數的過程。

#### 執行函數

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

在初始聊天處理後，代理會發送建議調用的工具函數，此例中是 `get_weather`。根據您的配置，該函數可自動由代理執行並讀取結果，或依用戶輸入觸發執行。

您可參考一系列 [AutoGen 代碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)，進一步探索如何開始構建。

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微軟開源的 SDK，用於用 **Python** 和 **.NET** 構建 AI 代理及多代理系統。它整合了微軟兩個早期專案的優勢——企業特性的 **Semantic Kernel** 和多代理協調的 **AutoGen** ——成為一個獲得支援的框架。如果您今天開始一個新的代理專案，這是推薦的 AutoGen 後繼方案。

該框架支持從單一<strong>聊天代理</strong>到複雜的<strong>多代理工作流程</strong>擴展，且可直接集成微軟 Foundry、Azure OpenAI、OpenAI。它還透過 OpenTelemetry 提供內建可觀察性，可精確追蹤代理的行為。

### 狀態與工具

<strong>狀態</strong> - 框架透過 **threads** 管理會話上下文。代理追蹤消息歷史（用戶請求、工具調用及其結果），讓每輪對話建立在前次基礎。Threads 可持久保存，允許對話中斷後繼續。

<strong>工具</strong> - 您可通過傳入普通 Python 函數賦予代理工具。帶有類型註解的參數會自動生成結構化模式，讓模型知道如何及何時調用（函數調用）。框架同時支持模型上下文協議（MCP）服務器及代碼解釋器等託管工具。

以下是一個帶有自定義工具的單一代理範例：

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

若要連接微軟 Foundry 中的 Azure OpenAI，請將端點和憑證傳入客戶端：

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

框架的亮點在於協調多個代理。例如，您可以依序執行代理（將上下文傳遞給下一個），或同時發散給多個代理並整合其結果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 按順序運行代理，沿鏈傳遞對話上下文
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 並行展開至多個代理，然後彙總它們的回應
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安裝框架並開始使用：

```bash
pip install agent-framework-core
# 可選整合
pip install agent-framework-openai       # OpenAI 及 Azure OpenAI
pip install agent-framework-foundry      # 微軟 Foundry
```

您可以在 [Microsoft Agent Framework 倉庫](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) 及其 [官方文件](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 中探索更多。

## Taskweaver

下一個我們將探索的代理框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被稱為「以代碼為先」的代理，因為它不僅處理 `strings`，還能處理 Python 中的 DataFrames，這對資料分析和生成任務非常有用，例如繪製圖表或產生隨機數。

### 狀態與工具

為管理對話狀態，TaskWeaver 採用了 `Planner` 的概念。`Planner` 是一個 LLM，接收用戶請求並規劃需完成的任務。

為完成任務，`Planner` 可使用稱為 `Plugins` 的工具集，這些工具可為 Python 類或通用代碼解釋器。這些插件以 embedding 形式存儲，方便 LLM 精準搜尋對應插件。

![Taskweaver](../../../translated_images/zh-HK/taskweaver.da8559999267715a.webp)

以下是一個用於處理異常檢測的插件範例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

代碼在執行前會被驗證。Taskweaver 中管理上下文的另一功能是 `experience`，它能將對話上下文長期存於 YAML 檔案，配置後讓 LLM 隨時間累積對特定任務的表現提升。

## JARVIS

最後一個我們探索的代理框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS 的獨特之處在於它使用 LLM 管理對話的 `state`，而 `tools` 則是其他 AI 模型。每個 AI 模型都是專門用於特定任務，如物體偵測、轉錄或圖片說明的專業模型。

![JARVIS](../../../translated_images/zh-HK/jarvis.762ddbadbd1a3a33.webp)

作為通用模型的 LLM 從用戶接收請求，識別具體任務和完成任務所需的參數或資料。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 將請求格式化成專用 AI 模型能理解的格式，如 JSON。專用 AI 模型完成預測後，LLM 接收該回應。

如果完成任務需多個模型，LLM 還會解讀這些模型的回應，然後整合生成回覆給用戶。

下述範例展示當用戶要求描述圖片中物件及計數時，該流程如何運作：

## 作業

為持續學習 AI 代理，您可以使用 Microsoft Agent Framework 建立：

- 一個模擬教育新創公司不同部門的商業會議應用程式。
- 創建系統訊息，引導 LLM 理解不同角色及優先事項，並讓用戶能推銷新產品構想。
- LLM 需從各部門產生後續問題以改進推銷與產品構想。

## 學習不止於此，繼續您的旅程

完成本課程後，請瀏覽我們的 [生成式 AI 學習專輯](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->