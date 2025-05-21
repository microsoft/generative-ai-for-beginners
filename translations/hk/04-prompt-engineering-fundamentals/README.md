<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:11:36+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hk"
}
-->
# 提示工程基礎

## 簡介
這個模組涵蓋了在生成式 AI 模型中創建有效提示的基本概念和技術。你如何向 LLM 編寫提示也很重要。精心設計的提示可以獲得更好的回應質量。但究竟什麼是提示和提示工程？我如何改進發送給 LLM 的提示輸入？這些問題我們將在本章和下一章中尋找答案。

生成式 AI 能夠根據用戶請求創建新內容（例如文本、圖像、音頻、代碼等）。它使用大型語言模型（例如 OpenAI 的 GPT 系列）進行訓練，利用自然語言和代碼來實現。

現在用戶可以使用熟悉的方式與這些模型互動，例如聊天，無需任何技術專業知識或訓練。這些模型是基於提示的——用戶發送文本輸入（提示）並獲得 AI 回應（完成）。然後他們可以在多輪對話中反覆與 AI 交流，精細化他們的提示，直到回應符合他們的期望。

“提示”現在成為生成式 AI 應用的主要編程接口，告訴模型做什麼並影響返回回應的質量。“提示工程”是一個快速增長的研究領域，專注於提示的設計和優化，以在大規模上提供一致且高質量的回應。

## 學習目標

在本課中，我們將學習什麼是提示工程，為什麼它重要，以及如何為特定模型和應用目標設計更有效的提示。我們將了解提示工程的核心概念和最佳實踐，並學習一個互動式 Jupyter Notebook 的“沙盒”環境，在那裡我們可以看到這些概念應用於實際例子。

在本課結束時，我們將能夠：

1. 解釋什麼是提示工程及其重要性。
2. 描述提示的組成部分及其用途。
3. 學習提示工程的最佳實踐和技術。
4. 使用 OpenAI 端點將所學技術應用於實際例子。

## 關鍵術語

提示工程：設計和精細化輸入以引導 AI 模型生成所需輸出的實踐。
分詞：將文本轉換為模型可以理解和處理的較小單位（稱為 token）的過程。
指令調整的 LLM：通過特定指令進行微調以提高回應準確性和相關性的大型語言模型（LLM）。

## 學習沙盒

提示工程目前更多是藝術而不是科學。改善我們直覺的最佳方法是多加練習並採用結合應用領域專業知識的試錯方法。

本課配套的 Jupyter Notebook 提供了一個沙盒環境，你可以在學習過程中或在結尾的代碼挑戰中嘗試所學內容。執行練習需要：

1. **Azure OpenAI API 密鑰** - 部署的 LLM 的服務端點。
2. **Python 運行時環境** - Notebook 可以在其中執行。
3. **本地環境變量** - 現在完成 [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) 步驟以做好準備。

Notebook 附帶了入門練習——但鼓勵你添加自己的 Markdown（描述）和代碼（提示請求）部分以嘗試更多例子或想法，並建立對提示設計的直覺。

## 圖解指南

想在深入學習之前了解本課涵蓋的主要內容嗎？查看這份圖解指南，它可以讓你了解主要主題和每個主題的關鍵要點。課程路線圖從理解核心概念和挑戰開始，然後用相關的提示工程技術和最佳實踐來解決它們。注意，本指南中的“高級技術”部分指的是本課程下一章的內容。

## 我們的初創公司

現在，讓我們談談這個主題如何與我們的初創公司使命——[將 AI 創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)——相關。我們想建立 AI 驅動的個性化學習應用——所以讓我們思考不同的應用用戶如何“設計”提示：

- **管理者**可能會要求 AI 分析課程數據以識別覆蓋範圍的空白。AI 可以總結結果或用代碼將其可視化。
- **教育者**可能會要求 AI 為目標受眾和主題生成課程計劃。AI 可以以指定格式構建個性化計劃。
- **學生**可能會要求 AI 在困難科目上輔導他們。AI 現在可以根據他們的水平提供課程、提示和例子。

這只是冰山一角。查看 [教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - 由教育專家策劃的開源提示庫 - 以獲得更廣泛的可能性！在沙盒中運行一些這些提示或使用 OpenAI Playground 看看會發生什麼！

## 什麼是提示工程？

我們開始這課時定義了提示工程為設計和優化文本輸入（提示）的過程，以在給定應用目標和模型中提供一致且高質量的回應（完成）。我們可以將其視為兩步過程：

- 設計給定模型和目標的初始提示
- 迭代精細化提示以改善回應質量

這必然是一個需要用戶直覺和努力的試錯過程以獲得最佳結果。那麼為什麼它重要呢？要回答這個問題，我們首先需要理解三個概念：

- 分詞 = 模型如何“看到”提示
- 基礎 LLM = 基礎模型如何“處理”提示
- 指令調整的 LLM = 模型如何現在看到“任務”

### 分詞

LLM 將提示視為 token 序列，其中不同模型（或模型版本）可以以不同方式分詞相同提示。由於 LLM 是基於 token 而不是原始文本進行訓練的，提示的分詞方式直接影響生成回應的質量。

要了解分詞如何工作，可以嘗試像 [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) 這樣的工具。將你的提示複製進去，看看如何轉換成 token，注意空白字符和標點符號的處理。注意這個例子展示了一個較舊的 LLM（GPT-3） - 所以用更新模型嘗試可能會產生不同結果。

### 概念：基礎模型

一旦提示被分詞，["基礎 LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)（或基礎模型）的主要功能是預測序列中的 token。由於 LLM 是基於大量文本數據集進行訓練的，它們對 token 之間的統計關係有很好的理解，並可以有信心地進行預測。注意它們不理解提示或 token 中單詞的“含義”；它們只是看到可以用下一個預測“完成”的模式。它們可以繼續預測序列，直到被用戶干預或某些預設條件終止。

想看看基於提示的完成如何工作？將上述提示輸入 Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) 並使用默認設置。系統配置為將提示視為信息請求 - 所以你應該看到滿足此上下文的完成。

但如果用戶希望看到符合某些標準或任務目標的具體內容呢？這就是指令調整的 LLM 的作用。

### 概念：指令調整的 LLM

[指令調整的 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)從基礎模型開始，並通過示例或輸入/輸出對（例如多輪“消息”）進行微調，可以包含明確指令 - 並且 AI 的回應嘗試遵循該指令。

這使用像人類反饋的強化學習（RLHF）這樣的技術，能夠訓練模型“遵循指令”和“學習反饋”，使其生成更適合實際應用並更符合用戶目標的回應。

讓我們試試 - 重訪上述提示，但現在更改系統消息以提供以下指令作為上下文：

> _為二年級學生總結提供的內容。結果保持在一段，並有 3-5 個要點。_

看看結果如何調整以反映所需目標和格式？教育者現在可以直接在課堂的幻燈片中使用此回應。

## 為什麼我們需要提示工程？

現在我們知道提示是如何被 LLM 處理的，讓我們談談為什麼我們需要提示工程。答案在於目前的 LLM 提出了一些挑戰，使得可靠和一致的完成更難以實現，而不在提示構建和優化上投入努力。例如：

1. **模型回應是隨機的。** 相同的提示很可能會在不同模型或模型版本中產生不同回應。甚至在相同模型中不同時間也可能產生不同結果。提示工程技術可以幫助我們通過提供更好的防護措施來最大限度地減少這些變化。

2. **模型可能會編造回應。** 模型是用大但有限的數據集進行預訓練的，這意味著它們缺乏對訓練範圍之外概念的知識。因此，它們可能會生成不準確、虛構或直接與已知事實相矛盾的完成。提示工程技術幫助用戶識別和減少這些編造，例如通過要求 AI 提供引用或推理。

3. **模型能力會有所不同。** 新模型或模型世代會有更豐富的能力，但也會帶來獨特的怪癖和成本與複雜性的權衡。提示工程可以幫助我們開發最佳實踐和工作流程，以可擴展、無縫的方式抽象掉差異並適應模型特定需求。

讓我們在 OpenAI 或 Azure OpenAI Playground 中看看這些：

- 使用不同 LLM 部署（例如 OpenAI、Azure OpenAI、Hugging Face）使用相同提示 - 你是否看到了變化？
- 使用相同 LLM 部署（例如 Azure OpenAI Playground）重複使用相同提示 - 這些變化有何不同？

### 編造例子

在本課中，我們使用術語“編造”來指代 LLM 有時會生成事實錯誤信息的現象，這是由於訓練限制或其他約束造成的。你可能也聽過在流行文章或研究論文中稱其為“幻覺”。然而，我們強烈建議使用“編造”這個術語，以免不小心將人類特徵歸因於機器驅動的結果。這也從術語角度加強了[負責任的 AI 指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去掉了可能在某些情境中被視為冒犯或不包容的術語。

想了解編造如何工作嗎？想一個指導 AI 為不存在的主題生成內容的提示（確保它不在訓練數據集中）。例如 - 我嘗試了這個提示：

> **提示：**生成 2076 年火星戰爭的課程計劃。

網絡搜索顯示有關火星戰爭的虛構敘述（例如電視劇或書籍） - 但沒有 2076 年的。常識也告訴我們 2076 年是未來，不可能與真實事件相關。

所以當我們用不同 LLM 提供者運行這個提示時會發生什麼？

> **回應 1**：OpenAI Playground (GPT-35)

> **回應 2**：Azure OpenAI Playground (GPT-35)

> **回應 3**：Hugging Face Chat Playground (LLama-2)

正如預期的那樣，由於隨機行為和模型能力的變化，每個模型（或模型版本）都產生略有不同的回應。例如，一個模型針對 8 年級受眾，而另一個假設是高中生。但所有三個模型都生成了可能使不知情的用戶相信事件是真實的回應

提示工程技術如元提示和溫度配置可能在一定程度上減少模型編造。新的提示工程架構也無縫地將新工具和技術納入提示流程，以減少或減輕其中一些效果。

## 案例研究：GitHub Copilot

讓我們通過查看一個案例研究來了解提示工程在實際解決方案中的應用：[GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot 是你的“AI 配對程序員” - 它將文本提示轉換為代碼完成並集成到你的開發環境中（例如 Visual Studio Code），提供無縫的用戶體驗。正如以下系列博客中所記錄的，最早的版本是基於 OpenAI Codex 模型 - 工程師迅速意識到需要微調模型並開發更好的提示工程技術，以改善代碼質量。7 月，他們[推出了一個超越 Codex 的改進 AI 模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)以提供更快的建議。

按順序閱讀文章，以跟隨他們的學習旅程。

- **2023年5月** | [GitHub Copilot 正在更好地理解你的代碼](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [GitHub內部：與 GitHub Copilot 背後的 LLM 合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023年6月** | [如何為 GitHub Copilot 編寫更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023年7月** | [GitHub Copilot 超越 Codex 的改進 AI 模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [開發者的提示工程和 LLM 指南](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何構建企業 LLM 應用：GitHub Copilot 的教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

你還可以瀏覽他們的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)以獲得更多像[這篇文章](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)展示這些模型和技術如何應用於驅動實際應用的文章。

## 提示構建

我們已經了解了為什麼提示工程很重要 - 現在讓我們理解提示是如何構建的，以便我們可以評估更有效提示設計的不同技術。

### 基本提示

讓我們從基本提示開始：發送給模型的文本輸入，沒有其他上下文。這是一個例子 - 當我們將美國國歌的前幾個詞發送給 OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) 時，它立即用接下來的幾行“完成”回應，說明了
最後，模板的真正價值在於能夠為垂直應用領域創建和發布_提示庫_，此時提示模板已經_優化_，以反映應用程序特定的上下文或示例，從而使回應對目標用戶群體更具相關性和準確性。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)庫就是這種方法的絕佳示例，它為教育領域策劃了一個提示庫，重點放在課程計劃、課程設計、學生輔導等關鍵目標上。

## 支持內容

如果我們將提示構建視為有一個指令（任務）和一個目標（主要內容），那麼_次要內容_就像我們提供的額外上下文，用來**以某種方式影響輸出**。它可能是調整參數、格式說明、主題分類等，可以幫助模型_調整_其回應以適應所需的用戶目標或期望。

例如：給定一個課程目錄，其中包含課程名稱、描述、級別、元數據標籤、講師等的豐富元數據：

- 我們可以定義一個指令來「總結2023年秋季的課程目錄」
- 我們可以使用主要內容來提供所需輸出的幾個示例
- 我們可以使用次要內容來確定最感興趣的5個「標籤」。

現在，模型可以按照示例顯示的格式提供摘要——但如果結果有多個標籤，它可以優先考慮次要內容中確定的5個標籤。

---

## 提示最佳實踐

既然我們知道如何_構建_提示，我們就可以開始考慮如何_設計_它們以反映最佳實踐。我們可以將其分為兩部分——擁有正確的_心態_和應用正確的_技術_。

### 提示工程心態

提示工程是一個反覆試驗的過程，因此請記住三個廣泛的指導因素：

1. **領域理解很重要。** 回應的準確性和相關性是該應用或用戶運行的_領域_的函數。運用你的直覺和領域專業知識進一步**定制技術**。例如，在系統提示中定義_領域特定的個性_，或在用戶提示中使用_領域特定的模板_。提供反映領域特定上下文的次要內容，或使用_領域特定的提示和示例_來引導模型朝著熟悉的使用模式發展。

2. **模型理解很重要。** 我們知道模型本質上是隨機的。但是模型的實現可能會因使用的訓練數據集（預訓練知識）、提供的能力（例如，通過API或SDK）以及它們優化的內容類型（例如，代碼、圖像或文本）而有所不同。了解你使用的模型的優勢和局限性，並利用這些知識來_優先考慮任務_或構建_定制模板_，以優化模型的能力。

3. **迭代和驗證很重要。** 模型正在快速發展，提示工程的技術也是如此。作為領域專家，你可能擁有其他上下文或標準_你的_特定應用程序，這可能不適用於更廣泛的社區。使用提示工程工具和技術來「快速啟動」提示構建，然後使用自己的直覺和領域專業知識進行迭代和驗證結果。記錄你的見解並創建一個**知識庫**（例如，提示庫），其他人可以將其用作新的基準，以便未來更快地進行迭代。

## 最佳實踐

現在讓我們看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)和[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)從業者推薦的一些常見最佳實踐。

| 什麼                              | 為什麼                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 評估最新模型。                    | 新的模型代可能具有改進的功能和質量，但也可能帶來更高的成本。評估它們的影響，然後做出遷移決策。                                                                                                                                                |
| 分開指令和上下文                  | 檢查你的模型/提供者是否定義了_分隔符_來更清晰地區分指令、主要和次要內容。這可以幫助模型更準確地為標記分配權重。                                                                                                                         |
| 具體和清晰                        | 提供更多有關所需上下文、結果、長度、格式、風格等的詳細信息。這將提高回應的質量和一致性。將食譜捕捉到可重用的模板中。                                                                                                                          |
| 描述性，使用示例                  | 模型可能對「展示和講述」的方法反應更好。從`zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT`值開始。回到[學習沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)學習如何。

### 接下來，打開Jupyter Notebook

- 選擇運行時內核。如果使用選項1或2，只需選擇dev容器提供的默認Python 3.10.x內核。

你已準備好運行練習。請注意，這裡沒有_對錯_答案——只是通過反覆試驗探索選項，並為給定模型和應用領域建立直覺。

_出於這個原因，本課程中沒有代碼解決方案部分。相反，Notebook將有標題為「我的解決方案：」的Markdown單元格，顯示一個參考示例輸出。_

## 知識檢查

以下哪一個是遵循合理最佳實踐的好提示？

1. 給我看一輛紅色汽車的圖片
2. 給我看一輛紅色沃爾沃XC90型號汽車停在懸崖邊，夕陽西下的圖片
3. 給我看一輛紅色沃爾沃XC90型號汽車的圖片

A: 2，它是最佳提示，因為它提供了「什麼」的細節並進入具體（不僅僅是任何汽車，而是特定的品牌和型號），而且還描述了整體環境。3是次佳，因為它也包含很多描述。

## 🚀 挑戰

看看你能否利用「提示」技術來完成提示：「給我看一輛紅色沃爾沃汽車的圖片」。它會回應什麼，你會如何改進它？

## 出色的工作！繼續你的學習

想了解更多關於不同提示工程概念的信息嗎？請訪問[持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以找到關於此主題的其他優質資源。

前往第5課，我們將研究[高級提示技術](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免責聲明**：

此文件是使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)翻譯的。雖然我們努力保證準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。