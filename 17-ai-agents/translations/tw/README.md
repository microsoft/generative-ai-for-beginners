[![開放原始碼模型](../../images/17-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## 簡介

AI代理代表了生成式AI的一個令人興奮的發展，使大型語言模型（LLMs）從助手演變為能夠採取行動的代理。AI代理框架使開發者能夠建立應用程式，讓LLMs能夠訪問工具和狀態管理。這些框架還增強了可見性，使用戶和開發者能夠監控LLMs計劃的行動，從而改善體驗管理。

這節課將涵蓋以下領域:

- 理解什麼是 AI Agent - AI Agent 到底是什麼？
- 探索四種不同的 AI Agent 框架 - 它們有什麼獨特之處？
- 將這些 AI Agent 應用於不同的使用案例 - 我們應該何時使用 AI Agent？

## 學習目標

完成這節課後，你將能夠：

- 解釋什麼是 AI 代理以及它們如何使用。
- 了解一些流行的 AI 代理框架之間的差異，以及它們的不同之處。
- 了解 AI 代理如何運作，以便使用它們建構應用程式。

## 什麼是 AI 代理？

AI代理是一個在生成式AI世界中非常令人興奮的領域。隨著這種興奮，有時會出現術語和其應用的混淆。為了保持簡單並包含大多數提到AI代理的工具，我們將使用這一定義:

AI Agents 允許大型語言模型（LLMs）透過提供**狀態**和**工具**來執行任務。

![代理模型](../../images/what-agent.png?WT.mc_id=academic-105485-koreyst)

讓我們定義這些術語:

**大型語言模型** - 這些是本課程中提到的模型，例如 GPT-3.5、GPT-4、Llama-2 等。

**狀態** - 這指的是LLM正在工作的上下文。LLM使用其過去行動的上下文和當前上下文，指導其後續行動的決策。AI代理框架允許開發人員更容易地維護此上下文。

**工具** - 為了完成使用者請求的任務以及 LLM 所規劃的任務，LLM 需要訪問工具。一些工具的範例可以是資料庫、API、外部應用程式甚至是另一個 LLM！

這些定義希望能在我們了解它們如何實現時，為你打下良好的基礎。讓我們來探索幾個不同的 AI Agent 框架:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/modules/agents/?WT.mc_id=academic-105485-koreyst) 是我們上述定義的實現。

要管理**狀態**，它使用一個名為 `AgentExecutor` 的內建函式。這個函式接受定義的 `agent` 和可用的 `tools`。

`Agent Executor` 也儲存聊天記錄以提供聊天的上下文。

![Langchain Agents](../../images/langchain-agents.png?WT.mc_id=academic-105485-koreyst)

LangChain 提供一個[工具目錄](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可以匯入到您的應用程式中，LLM 可以存取這些工具。這些工具由社群和 LangChain 團隊製作。

然後你可以定義這些工具並將它們傳遞給 `Agent Executor`。

可見性是討論 AI 代理時另一個重要方面。應用程式開發人員需要了解 LLM 使用的是哪種工具以及為什麼。為此，LangChain 團隊開發了 LangSmith。

## AutoGen

下一個我們將討論的 AI Agent 框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 的主要焦點是對話。Agents 既是**可對話的**也是**可定制的**。

**Conversable -** LLMs 可以啟動並繼續與另一個 LLM 的對話以完成任務。這是通過建立 `AssistantAgents` 並給予它們特定的系統訊息來完成的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**可自訂** - Agent 不僅可以定義為 LLMs，也可以是使用者或工具。作為開發者，你可以定義一個 `UserProxyAgent`，負責與使用者互動以獲取完成任務的反饋。這些反饋可以繼續執行任務或停止它。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 狀態和工具

為了改變和管理狀態，助手代理生成Python程式碼來完成任務。

這裡是一個過程的範例:

![AutoGen](../../images/autogen.png?WT.mc_id=academic-105485-koreyst)

#### 定義 LLM 的系統訊息

```python
system_message="對於天氣相關的任務，只使用提供給你的函式。任務完成後回覆 TERMINATE。"
```

此系統訊息指導此特定 LLM 哪些函式與其任務相關。請記住，使用 AutoGen 時，您可以有多個具有不同系統訊息的 AssistantAgents。

#### 聊天由使用者發起

```python
user_proxy.initiate_chat( chatbot, message="我計劃下週去紐約旅行，你能幫我選擇穿什麼嗎？", )
```

此訊息來自 user_proxy (人類) 是啟動代理探索應執行的可能函式的過程。

#### 函式被執行

```bash
聊天機器人 (to user_proxy):

***** 建議的工具呼叫: get_weather ***** 參數: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> 執行函式 get_weather... user_proxy (to 聊天機器人): ***** 呼叫函式 "get_weather" 的回應 ***** 112.22727272727272 EUR ****************************************************************

```

一旦初始聊天處理完成，代理將發送建議的工具來呼叫。在這種情況下，它是一個名為 `get_weather` 的函式。根據您的配置，這個函式可以由代理自動執行和讀取，或者可以根據用戶輸入來執行。

你可以找到[AutoGen 程式碼範例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)來進一步探索如何開始建構。

## Taskweaver

接下來我們將探討的代理框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被稱為「程式碼優先」代理，因為它不僅僅是嚴格地與 `strings` 一起工作，它還可以與 Python 中的 DataFrames 一起工作。這對於資料分析和生成任務變得非常有用。這可以是建立圖表或生成隨機數等事情。

### 狀態和工具

為了管理對話的狀態，TaskWeaver 使用了 `Planner` 的概念。`Planner` 是一個 LLM，它接收用戶的請求並規劃出需要完成的任務，以滿足這些請求。

為了完成任務，`Planner` 會接觸到稱為 `Plugins` 的工具集合。這可以是 Python 類別或一般的程式碼解釋器。這些插件被儲存為嵌入，以便 LLM 能夠更好地搜尋正確的插件。

![Taskweaver](../../images/taskweaver.png?WT.mc_id=academic-105485-koreyst)

這裡是一個處理異常檢測的插件範例:

```python
類別 AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

程式碼在執行前會被驗證。Taskweaver 中管理上下文的另一個功能是 `experience`。Experience 允許將對話的上下文長期存儲在 YAML 檔案中。這可以配置，使得 LLM 隨著時間的推移在某些任務上有所改進，前提是它接觸到先前的對話。

## JARVIS

最後我們將探討的代理框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst)。JARVIS 的獨特之處在於它使用 LLM 來管理對話的 `state`，而 `tools` 是其他 AI 模型。每個 AI 模型都是專門的模型，執行某些任務，例如物件檢測、轉錄或圖像標註。

![JARVIS](../../images/jarvis.png?WT.mc_id=academic-105485-koreyst)

LLM 作為一個通用模型，接收來自使用者的請求並識別特定任務及完成任務所需的任何參數/資料。

```python
[{"task": "物件-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 然後以專門的 AI 模型能夠解釋的方式格式化請求，例如 JSON。一旦 AI 模型根據任務返回其預測，LLM 便會接收回應。

如果需要多個模型來完成任務，它還會解釋這些模型的回應，然後將它們整合起來生成對用戶的回應。

範例如下顯示當使用者請求描述和計算圖片中的物件時，這將如何運作:

## 作業

為了繼續學習可以使用 AutoGen 建構的 AI 代理:

- 一個模擬教育初創公司不同部門商務會議的應用程式。
- 建立系統訊息，引導LLM理解不同角色和優先事項，並使使用者能夠提出新的產品創意。
- 然後，LLM應從每個部門生成後續問題，以完善和改進提案和產品創意。

## 學習不止於此，繼續旅程

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

