<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T09:49:47+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "tw"
}
-->
# 提示工程基礎

## 介紹
這個模組涵蓋了在生成式AI模型中創建有效提示的基本概念和技術。你撰寫提示給LLM的方式也很重要。精心設計的提示可以獲得更好的回應質量。但究竟什麼是「提示」和「提示工程」？如何改善我發送給LLM的提示輸入？這些是我們在本章和下一章中試圖回答的問題。

生成式AI能夠根據用戶請求創造新的內容（例如文本、圖像、音頻、代碼等）。它使用像OpenAI的GPT（「生成預訓練轉換器」）系列等大型語言模型進行訓練，使用自然語言和代碼。

用戶現在可以使用熟悉的聊天模式與這些模型互動，無需任何技術專業知識或訓練。這些模型是基於提示的——用戶發送文本輸入（提示），並獲得AI的回應（完成）。然後，他們可以在多回合對話中「與AI聊天」，迭代地完善提示，直到回應符合他們的期望。

「提示」現在成為生成式AI應用的主要編程介面，告訴模型該做什麼並影響回應的質量。「提示工程」是一個快速增長的研究領域，專注於提示的設計和優化，以在規模上提供一致和高質量的回應。

## 學習目標

在本課中，我們將了解什麼是提示工程、為什麼它很重要，以及如何為給定的模型和應用目標設計更有效的提示。我們將理解提示工程的核心概念和最佳實踐，並了解一個互動式Jupyter Notebook「沙盒」環境，在那裡我們可以看到這些概念應用於真實例子。

到本課結束時，我們將能夠：

1. 解釋什麼是提示工程以及它的重要性。
2. 描述提示的組成部分及其使用方式。
3. 學習提示工程的最佳實踐和技術。
4. 使用OpenAI端點將所學技術應用於真實例子。

## 關鍵術語

提示工程：設計和完善輸入以引導AI模型生成所需輸出的實踐。
分詞：將文本轉換為模型能理解和處理的小單位（稱為詞元）的過程。
指令調整LLM：經過特定指令微調以提高回應準確性和相關性的LLM。

## 學習沙盒

提示工程目前更像是一門藝術而非科學。提高直覺的最佳方法是多加練習，採用結合應用領域專業知識與推薦技術和模型特定優化的試錯法。

隨附本課的Jupyter Notebook提供了一個沙盒環境，讓你可以在學習過程中或作為最後的代碼挑戰的一部分嘗試所學內容。要執行練習，你需要：

1. **Azure OpenAI API密鑰**——已部署LLM的服務端點。
2. **Python運行時**——Notebook可在其中執行。
3. **本地環境變數**——立即完成[SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst)步驟以做好準備。

Notebook附有入門練習——但鼓勵你添加自己的Markdown（描述）和代碼（提示請求）部分，以嘗試更多例子或想法——並建立提示設計的直覺。

## 圖解指南

想在深入學習之前了解本課涵蓋的內容全貌嗎？查看這份圖解指南，讓你了解涵蓋的主要主題以及每個主題中的關鍵要點。課程路線圖從理解核心概念和挑戰開始，通過相關的提示工程技術和最佳實踐來解決它們。注意，指南中的「高級技術」部分指的是本課程下一章中涵蓋的內容。

## 我們的創業項目

現在，讓我們談談這個主題如何與我們的創業使命——[將AI創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)相關。我們希望建立AI驅動的個性化學習應用——所以讓我們思考一下我們應用的不同用戶如何「設計」提示：

- **管理者**可能要求AI分析課程數據以識別覆蓋範圍的差距。AI可以總結結果或使用代碼進行可視化。
- **教育者**可能要求AI為特定受眾和主題生成課程計劃。AI可以以指定格式構建個性化計劃。
- **學生**可能要求AI在困難的學科上輔導他們。AI現在可以根據他們的水平提供量身定制的課程、提示和例子。

這只是冰山一角。查看[教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)——由教育專家策劃的開源提示庫——以獲得更廣泛的可能性！嘗試在沙盒中運行其中一些提示或使用OpenAI Playground看看會發生什麼！

## 什麼是提示工程？

我們開始這課時定義了**提示工程**為設計和優化文本輸入（提示）以提供一致和高質量回應（完成）的過程，以滿足給定的應用目標和模型。我們可以將其視為兩步過程：

- 為給定的模型和目標設計初始提示
- 迭代地完善提示以提高回應質量

這必然是一個需要用戶直覺和努力的試錯過程，以獲得最佳結果。那麼為什麼它很重要呢？要回答這個問題，我們首先需要了解三個概念：

- **分詞** = 模型如何「看」提示
- **基礎LLM** = 基礎模型如何「處理」提示
- **指令調整LLM** = 模型如何現在能看到「任務」

### 分詞

LLM將提示視為詞元序列，其中不同的模型（或模型版本）可以以不同的方式對同一提示進行分詞。由於LLM是基於詞元（而不是原始文本）進行訓練的，提示被分詞的方式直接影響生成回應的質量。

要了解分詞如何運作，試試[OpenAI分詞器](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst)等工具。將你的提示複製進去——看看如何轉換為詞元，注意如何處理空白字符和標點符號。注意這個例子顯示的是較舊的LLM（GPT-3）——因此用較新的模型嘗試可能會產生不同的結果。

### 概念：基礎模型

一旦提示被分詞，「基礎LLM」的主要功能是預測序列中的詞元。由於LLM是基於大量文本數據集進行訓練的，它們對詞元之間的統計關係有良好的感知，並能以一定的信心進行預測。注意，它們不理解提示或詞元中的單詞的「含義」；它們只是看到可以用下一個預測「完成」的模式。它們可以繼續預測序列，直到被用戶干預或某個預設條件終止。

想看看基於提示的完成如何運作嗎？將上述提示輸入Azure OpenAI Studio的[聊天遊樂場](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)並使用默認設置。系統配置為將提示視為信息請求——所以你應該看到滿足這個上下文的完成。

但如果用戶希望看到滿足某些標準或任務目標的具體內容呢？這就是指令調整LLM派上用場的地方。

### 概念：指令調整LLM

指令調整LLM從基礎模型開始，並使用例子或輸入/輸出對（例如多回合「消息」）進行微調，這些對可以包含明確的指令——AI嘗試遵循該指令的回應。

這使用像人類反饋的強化學習（RLHF）等技術，可以訓練模型遵循指令並從反饋中學習，以生成更適合實際應用且更符合用戶目標的回應。

讓我們試試——重溫上述提示，但現在將系統消息更改為提供以下指令作為上下文：

> 將提供的內容總結為二年級學生。將結果保持在一段中，包含3-5個要點。

看看結果如何調整以反映所需的目標和格式？教育者現在可以直接在他們的課堂幻燈片中使用這個回應。

## 為什麼我們需要提示工程？

現在我們知道提示是如何被LLM處理的，讓我們談談為什麼我們需要提示工程。答案在於當前的LLM提出了一些挑戰，使得在不投入提示構建和優化的情況下更難實現可靠和一致的完成。例如：

1. **模型回應是隨機的。** 相同的提示可能會在不同的模型或模型版本中產生不同的回應。即使是在不同時間使用相同模型也可能產生不同結果。提示工程技術可以幫助我們通過提供更好的護欄來減少這些變化。

1. **模型可能會編造回應。** 模型是用大型但有限的數據集預訓練的，這意味著它們缺乏對訓練範圍外概念的知識。因此，它們可能會生成不準確、虛構或直接與已知事實相矛盾的完成。提示工程技術幫助用戶識別和減少這些編造，例如通過要求AI提供引文或推理。

1. **模型能力會有所不同。** 較新的模型或模型世代將具有更豐富的能力，但也帶來了成本和複雜性方面的獨特怪癖和權衡。提示工程可以幫助我們開發最佳實踐和工作流程，抽象化差異並以可擴展、無縫的方式適應模型特定要求。

讓我們在OpenAI或Azure OpenAI Playground中看看這些如何運作：

- 使用不同的LLM部署（例如OpenAI、Azure OpenAI、Hugging Face）使用相同的提示——你看到變化了嗎？
- 使用相同的LLM部署（例如Azure OpenAI Playground）重複使用相同的提示——這些變化有何不同？

### 編造例子

在本課程中，我們使用術語**「編造」**來描述LLM有時由於訓練限制或其他約束生成事實不正確信息的現象。你可能在流行文章或研究論文中聽過這被稱為「幻覺」。然而，我們強烈建議使用「編造」這個術語，以避免不小心將行為擬人化，將人類特徵歸因於機器驅動的結果。這也從術語角度加強了[負責任AI指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去除在某些情境中可能被認為冒犯或不包容的術語。

想了解編造如何運作嗎？想一個指示AI生成不存在主題內容的提示（以確保它不在訓練數據集中）。例如——我試過這個提示：

> **提示：**生成2076年火星戰爭的課程計劃。

網絡搜索顯示有關火星戰爭的虛構賬戶（例如電視劇或書籍）——但沒有2076年的。常識也告訴我們2076年是未來，因此不能與真實事件相關聯。

那麼當我們使用不同的LLM提供商運行這個提示時會發生什麼？

如預期，每個模型（或模型版本）都因隨機行為和模型能力變化而產生稍微不同的回應。例如，一個模型針對八年級受眾，而另一個假設高中生。但所有三個模型都生成了可能讓不知情用戶相信事件是真實的回應。

提示工程技術如元提示和溫度配置可能在某種程度上減少模型編造。一些新的提示工程架構還將新工具和技術無縫地納入提示流程，以減少或減輕其中一些影響。

## 案例研究：GitHub Copilot

讓我們通過查看一個案例研究來了解提示工程在現實解決方案中的應用：[GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot是你的「AI配對程序員」——它將文本提示轉換為代碼完成，並集成到你的開發環境（例如Visual Studio Code）中，提供無縫的用戶體驗。如下面一系列博客所述，最早版本基於OpenAI Codex模型——工程師很快意識到需要微調模型並開發更好的提示工程技術，以提高代碼質量。在七月，他們[推出了一個改進的AI模型，超越了Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，以提供更快的建議。

按順序閱讀帖子，跟隨他們的學習旅程。

- **2023年5月** | [GitHub Copilot正在更好地理解你的代碼](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [GitHub內部：與GitHub Copilot背後的LLM合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023年6月** | [如何為GitHub Copilot撰寫更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023年7月** | [.. GitHub Copilot超越Codex，推出改進的AI模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [開發者的提示工程和LLM指南](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何建立企業LLM應用：GitHub Copilot的經驗教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

你也可以瀏覽他們的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)以獲得更多像[這篇](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)的帖子，展示如何應用這些模型和技術來推動現實世界應用。

## 提示構建

我們已經了解了提示工程的重要性，現在讓我們理解提示是如何構建的，以便評估不同的技術來設計更有效的提示。

### 基本提示

讓我們從基本提示開始：一個發送給模型的文本輸入，沒有其他上下文。這裡有個例子——當我們將美國國歌的前幾個詞發送到OpenAI完成API時，它立即以下一行完成回應，展示了基本的預測行為。

### 複雜提示

現在讓我們為基本提示添加上下文和指令。聊天完成API讓我們可以將複雜提示構建為一組消息，包括：

- 反映用戶輸入和助手回應的輸入/輸出對。
- 設置助手行為或個性的系統消息。

請求現在以如下形式存在，其中分詞有效地捕捉了上下文和對話中的相關信息。現在，改變系統上下文可以像提供的用戶輸入一樣影響完成的質量。

### 指令提示

在上述例子中，用戶提示是一個簡單的文本查詢，可以被解釋為信息請求
最終，範本的真正價值在於能夠為垂直應用領域創建和發布_提示庫_——這些提示範本經過_優化_，能夠反映特定應用的上下文或例子，使回應對目標用戶群體更具相關性和準確性。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 資源庫就是這種方法的絕佳例子，它精心編輯了一個針對教育領域的提示庫，重點在於課程規劃、課程設計、學生輔導等關鍵目標。

## 支持內容

如果我們將提示構建視為擁有一個指令（任務）和一個目標（主要內容），那麼_次要內容_就像是我們提供的額外上下文，以某種方式**影響輸出**。它可以是調整參數、格式指令、主題分類等，這些都可以幫助模型_定制_其回應，以符合所需的用戶目標或期望。

例如：給定一個包含所有課程的課程目錄，並附有豐富的元數據（名稱、描述、級別、元數據標籤、講師等）：

- 我們可以定義一個指令來「總結2023年秋季的課程目錄」
- 我們可以使用主要內容來提供幾個所需輸出的例子
- 我們可以使用次要內容來識別5個感興趣的「標籤」

現在，模型可以按照所提供的例子格式來提供總結——但如果結果有多個標籤，它可以優先考慮次要內容中識別出的5個標籤。

---

<!--
課程範本：
這單元應涵蓋核心概念#1。
用例子和參考資料加強這個概念。

概念#3：
提示工程技術。
有哪些基本的提示工程技術？
用一些練習來說明。
-->

## 提示最佳實踐

現在我們知道如何_構建_提示，我們可以開始思考如何_設計_它們以反映最佳實踐。我們可以將這分為兩部分——擁有正確的_心態_和應用正確的_技術_。

### 提示工程心態

提示工程是一個反覆試驗的過程，所以要記住三個廣泛的指導因素：

1. **領域理解很重要。** 回應的準確性和相關性取決於應用或用戶所處的_領域_。運用你的直覺和領域專業知識進一步**定制技術**。例如，在系統提示中定義_特定領域的人格_，或在用戶提示中使用_特定領域的範本_。提供反映特定領域上下文的次要內容，或使用_特定領域的提示和例子_來引導模型朝著熟悉的使用模式。

2. **模型理解很重要。** 我們知道模型本質上是隨機的。但模型實現也可能因其使用的訓練數據集（預訓練知識）、提供的能力（例如，通過API或SDK）以及它們優化的內容類型（例如，代碼、圖像或文本）而異。了解你所使用模型的優勢和限制，並利用這些知識來_優先處理任務_或構建_定制範本_，使其針對模型的能力進行優化。

3. **迭代和驗證很重要。** 模型在迅速演變，提示工程技術也是如此。作為領域專家，你可能有其他上下文或標準適用於_你的_特定應用，而不適用於更廣泛的社群。使用提示工程工具和技術來「快速啟動」提示構建，然後使用自己的直覺和領域專業知識進行迭代和驗證結果。記錄你的見解並創建一個**知識庫**（例如，提示庫），以便其他人可以用作新的基準，從而在未來更快地進行迭代。

## 最佳實踐

現在讓我們來看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)和[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)從業者推薦的一些常見最佳實踐。

| 內容                              | 原因                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 評估最新模型。                     | 新一代模型可能具有改進的功能和質量——但也可能帶來更高的成本。評估它們的影響，然後做出遷移決策。                                                                                                            |
| 分開指令和上下文                  | 檢查你的模型/提供者是否定義了_分隔符_，以更清晰地區分指令、主要和次要內容。這可以幫助模型更準確地分配權重給標記。                                                                                     |
| 具體和清晰                        | 提供更多有關所需上下文、結果、長度、格式、風格等的細節。這將提高回應的質量和一致性。將這些方案記錄在可重用的範本中。                                                                                      |
| 詳細描述，使用例子                | 模型可能更好地響應「展示和講解」的方法。從`zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT`值開始。返回到[學習沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)學習如何。

### 接下來，打開 Jupyter Notebook

- 選擇運行時核心。如果使用選項1或2，只需選擇開發容器提供的默認 Python 3.10.x 核心。

你已準備好運行練習。注意這裡沒有_對錯_的答案——只是通過反覆試驗來探索選項，並為特定模型和應用領域建立直覺。

_因此，本課中沒有代碼解決方案部分。相反，Notebook 將有名為「我的解決方案：」的 Markdown 單元格，顯示一個示例輸出供參考。_

 <!--
課程範本：
用總結和自學資源來結束本節。
-->

## 知識檢查

以下哪一個是符合某些合理最佳實踐的良好提示？

1. 給我看一張紅色車的圖片
2. 給我看一張紅色車的圖片，品牌為 Volvo，型號為 XC90，停在懸崖邊，夕陽西下
3. 給我看一張紅色車的圖片，品牌為 Volvo，型號為 XC90

A: 2，這是最佳提示，因為它提供了「什麼」的詳細信息，並進入具體細節（不僅僅是任何車，而是特定的品牌和型號），還描述了整體場景。3是次佳，因為它也包含了很多描述。

## 🚀 挑戰

看看你能否利用「提示」技術來完成這個提示：「給我看一張紅色車的圖片，品牌為 Volvo 和」。它的回應是什麼，你會如何改進？

## 很棒的工作！繼續學習

想了解更多不同的提示工程概念嗎？前往[持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，尋找其他關於此主題的優秀資源。

前往第5課，我們將探討[高級提示技術](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免責聲明**：
本文檔已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議使用專業人工翻譯。對於因使用此翻譯而產生的任何誤解或誤釋，我們不承擔責任。