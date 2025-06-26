<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:03:25+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hk"
}
-->
# 提示工程基礎

## 介紹
此模組涵蓋了在生成式 AI 模型中創建有效提示的基本概念和技術。你撰寫提示給大型語言模型（LLM）的方式也很重要。精心設計的提示可以獲得更高質量的回應。但究竟什麼是「提示」和「提示工程」？我如何改善發送給 LLM 的提示輸入？這些是我們在本章和下一章中試圖回答的問題。

生成式 AI 能夠根據用戶請求創建新的內容（例如文本、圖像、音頻、代碼等）。它使用大型語言模型（如 OpenAI 的 GPT 系列）進行訓練，以自然語言和代碼為基礎。

用戶現在可以使用像聊天這樣熟悉的方式與這些模型互動，而不需要任何技術專業知識或訓練。這些模型是基於提示的——用戶發送文本輸入（提示），然後獲得 AI 的回應（完成）。他們可以在多輪對話中反覆與 AI 交流，調整提示直到回應符合他們的期望。

「提示」現在成為生成式 AI 應用的主要編程界面，告訴模型該做什麼並影響返回回應的質量。「提示工程」是一個快速增長的研究領域，專注於設計和優化提示，以大規模地提供一致和高質量的回應。

## 學習目標

在這節課中，我們將學習什麼是提示工程，為什麼它很重要，以及如何為給定的模型和應用目標創建更有效的提示。我們將了解提示工程的核心概念和最佳實踐——並了解一個互動的 Jupyter Notebooks「沙盒」環境，在那裡我們可以看到這些概念應用於真實例子。

在這節課結束時，我們將能夠：

1. 解釋什麼是提示工程及其重要性。
2. 描述提示的組成部分及其用法。
3. 學習提示工程的最佳實踐和技術。
4. 使用 OpenAI 端點將學到的技術應用於真實例子。

## 關鍵術語

提示工程：設計和改進輸入以引導 AI 模型產生所需輸出的實踐。
分詞：將文本轉換為模型可以理解和處理的較小單位（稱為標記）的過程。
指令調整 LLMs：經過特定指令微調以提高回應準確性和相關性的 LLMs。

## 學習沙盒

提示工程目前更像是一門藝術而非科學。改進我們的直覺的最佳方法是多加練習，並採用一種試錯法，將應用領域專業知識與推薦技術和模型特定優化相結合。

隨堂附帶的 Jupyter Notebook 提供了一個「沙盒」環境，你可以在其中嘗試所學內容——隨著進度或作為最後代碼挑戰的一部分進行。要執行練習，你需要：

1. **Azure OpenAI API 金鑰** - 部署的 LLM 的服務端點。
2. **Python 執行環境** - 可執行 Notebook 的環境。
3. **本地環境變數** - 現在完成 [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) 步驟以做好準備。

該 Notebook 附帶入門練習，但鼓勵你添加自己的 Markdown（描述）和代碼（提示請求）部分，以嘗試更多例子或想法——並建立你的提示設計直覺。

## 圖解指南

想在深入學習之前了解這節課的全貌嗎？查看這個圖解指南，它讓你了解所涵蓋的主要主題和每個主題的關鍵要點。課程路線圖將帶你從理解核心概念和挑戰到使用相關的提示工程技術和最佳實踐來解決它們。請注意，指南中的「進階技術」部分指的是本課程下一章中涵蓋的內容。

## 我們的初創公司

現在，讓我們談談這個主題如何與我們的初創公司使命相關，即[將 AI 創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)。我們希望構建 AI 驅動的個性化學習應用程序——因此讓我們思考我們的應用程序的不同用戶如何「設計」提示：

- **管理員**可能要求 AI 分析課程數據以識別覆蓋範圍的差距。AI 可以總結結果或用代碼將其可視化。
- **教育者**可能要求 AI 為目標受眾和主題生成課程計劃。AI 可以以指定格式構建個性化計劃。
- **學生**可能要求 AI 在困難的學科中輔導他們。AI 現在可以根據他們的水平提供量身定制的課程、提示和例子。

這僅僅是冰山一角。查看 [教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)——由教育專家策劃的開源提示庫——以獲得更廣泛的可能性！在沙盒中或使用 OpenAI Playground 嘗試運行其中一些提示，看看會發生什麼！

## 什麼是提示工程？

我們開始這節課時將**提示工程**定義為設計和優化文本輸入（提示）的過程，以便為給定的應用目標和模型提供一致和高質量的回應（完成）。我們可以將其視為一個兩步驟的過程：

- 為給定模型和目標設計初始提示
- 反覆優化提示以提高回應質量

這必然是一個需要用戶直覺和努力的試錯過程，以獲得最佳結果。那麼為什麼這很重要呢？要回答這個問題，我們首先需要了解三個概念：

- 分詞 = 模型如何「看到」提示
- 基礎 LLMs = 基礎模型如何「處理」提示
- 指令調整 LLMs = 模型現在如何看到「任務」

### 分詞

LLM 將提示視為一個標記序列，其中不同的模型（或模型版本）可以以不同方式對同一提示進行分詞。由於 LLMs 是基於標記而非原始文本進行訓練的，因此提示的分詞方式直接影響生成回應的質量。

要了解分詞的工作原理，可以嘗試像 [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) 這樣的工具。將你的提示複製進去，看看它如何轉換為標記，注意空白字符和標點符號的處理方式。請注意，這個例子顯示了一個較舊的 LLM（GPT-3），因此用較新的模型嘗試可能會產生不同的結果。

### 概念：基礎模型

一旦提示被分詞，「基礎 LLM」（或基礎模型）的主要功能是預測該序列中的標記。由於 LLMs 是基於大量文本數據集進行訓練的，它們對標記之間的統計關係有很好的理解，並能夠自信地做出預測。請注意，它們並不理解提示或標記中的詞語「意義」；它們只是看到一個可以通過下一次預測來「完成」的模式。它們可以繼續預測序列，直到用戶干預或某個預先建立的條件終止。

想看看基於提示的完成是如何工作的嗎？將上述提示輸入 Azure OpenAI Studio 的[聊天沙盒](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)，使用默認設置。系統配置為將提示視為信息請求，因此你應該看到一個滿足此上下文的完成。

但如果用戶想看到符合某些標準或任務目標的具體內容呢？這就是指令調整 LLMs 出現的地方。

### 概念：指令調整 LLMs

[指令調整 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) 以基礎模型為起點，並通過示例或輸入/輸出對（例如多輪「消息」）進行微調，這些對可以包含明確的指令，AI 嘗試遵循該指令進行回應。

這使用了像人類反饋強化學習（RLHF）這樣的技術，能夠訓練模型「遵循指令」和「從反饋中學習」，以便它生成的回應更適合實際應用，更符合用戶目標。

讓我們試試看——重訪上述提示，但現在更改系統消息以提供以下指令作為上下文：

> 將提供的內容總結為二年級學生。將結果限制在一段中，並包含 3-5 個要點。

看看結果現在如何調整以反映所需的目標和格式？教育者現在可以直接在他們的課程幻燈片中使用此回應。

## 為什麼我們需要提示工程？

現在我們知道 LLMs 如何處理提示，讓我們談談為什麼我們需要提示工程。答案在於當前的 LLMs 存在一些挑戰，使得在不努力構建和優化提示的情況下實現可靠和一致的完成更加困難。例如：

1. **模型回應是隨機的。** 相同的提示可能會在不同的模型或模型版本中產生不同的回應。即使是相同的模型在不同時間也可能產生不同的結果。_提示工程技術可以幫助我們通過提供更好的防護措施來最大限度地減少這些變化_。

2. **模型可能會捏造回應。** 模型是基於大型但有限的數據集進行預訓練的，這意味著它們缺乏關於訓練範圍外概念的知識。因此，它們可能會產生不準確、虛構或直接與已知事實相矛盾的完成。_提示工程技術可以幫助用戶識別和減輕這些捏造，例如，要求 AI 提供引用或推理_。

3. **模型能力會有所不同。** 更新的模型或模型世代將具有更豐富的功能，但也會帶來成本和複雜性方面的獨特怪癖和權衡。_提示工程可以幫助我們開發最佳實踐和工作流程，以抽象掉差異並以可擴展、無縫的方式適應模型特定的需求_。

讓我們在 OpenAI 或 Azure OpenAI Playground 中看看這些挑戰：

- 使用不同的 LLM 部署（例如，OpenAI、Azure OpenAI、Hugging Face）使用相同的提示——你看到變化了嗎？
- 使用相同的 LLM 部署（例如，Azure OpenAI Playground）重複使用相同的提示——這些變化有什麼不同？

### 捏造示例

在本課程中，我們使用「捏造」一詞來指代 LLMs 有時會因其訓練或其他限制而生成事實上不正確的信息的現象。你可能在流行文章或研究論文中也聽過這被稱為「幻覺」。然而，我們強烈建議使用「捏造」這個術語，以免不小心將人類特徵賦予機器驅動的結果。這也從術語角度加強了[負責任的 AI 指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去除在某些上下文中可能被認為具有攻擊性或不包容的術語。

想了解捏造是如何工作的嗎？想一個指示 AI 為不存在的主題生成內容的提示（以確保它不在訓練數據集中）。例如——我嘗試了這個提示：

> **提示：** 為 2076 年的火星戰爭生成一個課程計劃。

網絡搜索顯示有關火星戰爭的虛構故事（例如，電視劇或書籍）——但 2076 年的沒有。常識也告訴我們，2076 年是未來，因此不能與真實事件相關聯。

那麼當我們與不同的 LLM 提供商一起運行此提示時會發生什麼？

> **回應 1**：OpenAI Playground (GPT-35)

> **回應 2**：Azure OpenAI Playground (GPT-35)

> **回應 3**：Hugging Face Chat Playground (LLama-2)

如預期，每個模型（或模型版本）都因隨機行為和模型能力差異而產生略有不同的回應。例如，一個模型針對八年級受眾，而另一個則假設高中生。但所有三個模型都生成了可能讓不知情的用戶相信事件是真實的回應

提示工程技術如_元提示_和_溫度配置_可以在某種程度上減少模型捏造。新的提示工程_架構_還將新工具和技術無縫整合到提示流中，以緩解或減少其中的一些影響。

## 案例研究：GitHub Copilot

讓我們通過查看一個案例研究來了解提示工程在真實世界解決方案中的使用： [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot 是你的「AI 配對程序員」——它將文本提示轉換為代碼完成，並集成到你的開發環境（例如，Visual Studio Code）中，提供無縫的用戶體驗。正如下面一系列博客中所記錄的，最早的版本基於 OpenAI Codex 模型——工程師很快意識到需要對模型進行微調並開發更好的提示工程技術，以提高代碼質量。在 7 月，他們[推出了一個改進的 AI 模型，超越 Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，提供更快的建議。

按順序閱讀這些帖子，以了解他們的學習過程。

- **2023 年 5 月** | [GitHub Copilot 在更好地理解你的代碼](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 年 5 月** | [GitHub 內部：與 GitHub Copilot 背後的 LLMs 合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023 年 6 月** | [如何為 GitHub Copilot 撰寫更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023 年 7 月** | [GitHub Copilot 超越 Codex 的改進 AI 模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 年 7 月** | [開發者指南：提示工程和 LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 年 9 月** | [如何構建企業 LLM 應用程序：GitHub Copilot 的經驗教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

你還可以瀏覽他們的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)，了解更多像[這篇](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)那樣的帖子，展示這些模型和技術如何應用於驅動現實世界的應用程序。

## 提示構建

我們已經看到了提示工程的重要性，現在讓我們了解提示
最終，範本的真正價值在於能夠為垂直應用領域創建和發布_提示庫_——在這裡，提示範本已經_優化_以反映特定應用的背景或範例，使得回應對目標用戶群體更具相關性和準確性。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 資源庫是這種方法的一個很好的例子，精選了一個針對教育領域的提示庫，重點在於課程規劃、課程設計、學生輔導等關鍵目標。

## 支援內容

如果我們將提示構建視為包含指令（任務）和目標（主要內容），那麼_次要內容_就像我們提供的額外背景，以某種方式**影響輸出**。這可能是調整參數、格式化指令、主題分類等，這些可以幫助模型_定制_其回應以符合所需的用戶目標或期望。

例如：給定一個課程目錄，其中包含所有課程的廣泛元數據（名稱、描述、等級、元數據標籤、講師等）：

- 我們可以定義一個指令來“總結 2023 年秋季的課程目錄”
- 我們可以使用主要內容來提供一些期望輸出的範例
- 我們可以使用次要內容來識別前五個感興趣的“標籤”。

現在，模型可以提供格式與範例顯示一致的摘要——但如果結果有多個標籤，它可以優先考慮次要內容中識別的五個標籤。

---

<!--
課程範本：
這個單元應該涵蓋核心概念#1。
用例子和參考來強化這個概念。

概念#3：
提示工程技術。
有哪些基本的提示工程技術？
用一些練習來說明。
-->

## 提示最佳實踐

現在我們知道如何_構建_提示，我們可以開始思考如何_設計_它們以反映最佳實踐。我們可以將其分為兩部分——擁有正確的_心態_和應用正確的_技術_。

### 提示工程心態

提示工程是一個試錯過程，因此請記住三個廣泛的指導因素：

1. **領域理解很重要。** 回應的準確性和相關性取決於應用或用戶運作的_領域_。運用你的直覺和領域專業知識進一步**定制技術**。例如，在系統提示中定義_領域特定的個性_，或在用戶提示中使用_領域特定的範本_。提供反映領域特定背景的次要內容，或使用_領域特定的提示和範例_來引導模型朝著熟悉的使用模式。

2. **模型理解很重要。** 我們知道模型本質上是隨機的。但模型的實施也可能因所使用的訓練數據集（預訓練知識）、它們提供的能力（例如，通過 API 或 SDK）和它們優化的內容類型（例如，代碼 vs. 圖像 vs. 文本）而有所不同。了解你所使用的模型的優勢和局限性，並利用這些知識來_優先安排任務_或構建_定制範本_，以優化模型的能力。

3. **迭代與驗證很重要。** 模型正在迅速演變，提示工程的技術也是如此。作為領域專家，你可能對_你_的特定應用有其他背景或標準，這可能不適用於更廣泛的社區。使用提示工程工具和技術來“快速啟動”提示構建，然後使用你的直覺和領域專業知識進行迭代和驗證結果。記錄你的見解並創建一個**知識庫**（例如，提示庫），可供他人用作新的基準，以便未來更快的迭代。

## 最佳實踐

現在讓我們看看 [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) 和 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) 實踐者推薦的常見最佳實踐。

| 內容                              | 原因                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 評估最新模型。                    | 新一代模型可能具有改進的功能和質量——但也可能會產生更高的成本。評估它們的影響，然後做出遷移決策。                                                                                                                                                |
| 分開指令與背景                     | 檢查你的模型/提供者是否定義了_分隔符_以更清楚地區分指令、主要和次要內容。這可以幫助模型更準確地分配權重給標記。                                                                                                                         |
| 具體且清晰                         | 提供更多關於期望的背景、結果、長度、格式、風格等的細節。這將改善回應的質量和一致性。將配方捕捉到可重用的範本中。                                                                                                                          |
| 描述性，使用範例                   | 模型可能對“展示和講述”方法反應更好。從 `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` 值開始。回到[學習沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)學習如何做。

### 接下來，打開 Jupyter Notebook

- 選擇運行時內核。如果使用選項 1 或 2，只需選擇開發容器提供的默認 Python 3.10.x 內核。

你已準備好運行練習。請注意，這裡沒有_正確和錯誤_的答案——只是通過試錯探索選項，並建立對於給定模型和應用領域有效的直覺。

_因此，本課程中沒有代碼解決方案部分。相反，Notebook 會有標題為“我的解決方案：”的 Markdown 單元格，顯示一個參考的範例輸出。_

 <!--
課程範本：
用總結和自學資源來結束這一部分。
-->

## 知識檢查

以下哪一個是符合一些合理最佳實踐的好提示？

1. 給我看一張紅色汽車的圖片
2. 給我看一張紅色汽車的圖片，品牌是沃爾沃，型號是 XC90，停在懸崖邊，夕陽西下
3. 給我看一張紅色汽車的圖片，品牌是沃爾沃，型號是 XC90

A: 2，這是最好的提示，因為它提供了“什麼”的細節，並深入到具體細節（不僅僅是任何汽車，而是特定的品牌和型號），並且還描述了整體設置。3 是次佳選擇，因為它也包含了很多描述。

## 🚀 挑戰

看看你能否利用“提示”技術來完成這個句子：“給我看一張紅色汽車的圖片，品牌是沃爾沃和”。它會回應什麼，你會如何改進它？

## 優秀的工作！繼續你的學習

想了解更多不同的提示工程概念嗎？請訪問[持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以找到關於此主題的其他優秀資源。

前往第 5 課，我們將探討[高級提示技術](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的本地語言版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤譯承擔責任。