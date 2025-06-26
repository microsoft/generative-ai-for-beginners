<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:06:00+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "tw"
}
-->
# 提示工程基礎

## 介紹
本模組涵蓋了在生成式AI模型中創建有效提示的基本概念和技術。您撰寫提示給大型語言模型（LLM）的方式也很重要。精心設計的提示可以獲得更高質量的回應。但究竟什麼是「提示」和「提示工程」？我應該如何改善發送給LLM的提示「輸入」？這些是我們在本章和下一章中將嘗試回答的問題。

生成式AI能夠根據用戶的要求創造新內容（例如，文本、圖像、音頻、代碼等）。它使用像OpenAI的GPT（「生成預訓練變換器」）系列這樣的_大型語言模型_來實現，這些模型是用自然語言和代碼訓練的。

用戶現在可以使用熟悉的範式與這些模型互動，比如聊天，而無需任何技術專業知識或訓練。這些模型是基於提示的——用戶發送一個文本輸入（提示），並獲得AI的回應（完成）。然後，他們可以在多輪對話中反覆「與AI聊天」，優化他們的提示，直到回應符合他們的期望。

「提示」現在成為生成式AI應用程序的主要_編程接口_，告訴模型該做什麼並影響回應質量。「提示工程」是一個快速增長的研究領域，專注於提示的_設計和優化_，以大規模提供一致和高質量的回應。

## 學習目標

在這一課中，我們將學習什麼是提示工程，為什麼它很重要，以及如何為給定的模型和應用目標設計更有效的提示。我們將了解提示工程的核心概念和最佳實踐——並了解一個互動式Jupyter Notebook「沙盒」環境，在那裡我們可以看到這些概念應用於真實的例子。

在本課結束時，我們將能夠：

1. 解釋什麼是提示工程以及它為什麼重要。
2. 描述提示的組成部分及其用途。
3. 學習提示工程的最佳實踐和技術。
4. 使用OpenAI端點將學到的技術應用於真實例子。

## 關鍵術語

提示工程：設計和完善輸入以引導AI模型生成所需輸出的實踐。
分詞：將文本轉換為模型可以理解和處理的小單位，稱為token的過程。
指令調整的LLM：經過特定指令微調的大型語言模型，以提高其回應的準確性和相關性。

## 學習沙盒

提示工程目前更多是一門藝術而非科學。提高我們直覺的最佳方法是_多加練習_，並採用結合應用領域專業知識與推薦技術和特定模型優化的試錯法。

本課程附帶的Jupyter Notebook提供了一個_沙盒_環境，您可以在那裡嘗試學到的知識——無論是在進行中還是在最後的代碼挑戰中。要執行這些練習，您將需要：

1. **Azure OpenAI API密鑰**——已部署的LLM的服務端點。
2. **Python運行環境**——在其中可以執行Notebook。
3. **本地環境變數**——_完成[設置](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst)步驟以準備就緒_。

該Notebook附帶_入門_練習——但我們鼓勵您添加自己的_Markdown_（描述）和_代碼_（提示請求）部分，以嘗試更多的例子或想法——並建立您對提示設計的直覺。

## 圖解指南

想在深入學習之前了解本課程涵蓋的主要內容嗎？查看這個圖解指南，它會給您一個關於涵蓋的主要主題和每個主題需要思考的關鍵要點的概念。課程路線圖將帶您從理解核心概念和挑戰開始，通過相關的提示工程技術和最佳實踐來解決它們。請注意，該指南中的「高級技術」部分指的是本課程的_下一章_中涵蓋的內容。

## 我們的創業公司

現在，讓我們來談談_這個主題_如何與我們的創業公司使命相關，即[將AI創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)。我們希望構建AI驅動的_個性化學習_應用程序——所以讓我們想想我們的應用程序的不同用戶可能如何「設計」提示：

- **管理員**可能會要求AI_分析課程數據以識別覆蓋範圍中的差距_。AI可以總結結果或用代碼將其可視化。
- **教育者**可能會要求AI_為目標受眾和主題生成一個教學計劃_。AI可以以指定的格式構建個性化計劃。
- **學生**可能會要求AI_在困難的科目上輔導他們_。AI現在可以根據他們的水平為學生提供課程、提示和示例。

這只是冰山一角。查看[教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)——一個由教育專家策劃的開源提示庫——以獲得更廣泛的可能性！_嘗試在沙盒中運行其中一些提示或使用OpenAI Playground來看看會發生什麼！_

## 什麼是提示工程？

我們開始這一課時，將**提示工程**定義為_設計和優化_文本輸入（提示）的過程，以便為給定的應用目標和模型提供一致和高質量的回應（完成）。我們可以將其視為一個兩步驟的過程：

- 為給定模型和目標_設計_初始提示
- 迭代地_優化_提示以提高回應質量

這必然是一個需要用戶直覺和努力的試錯過程，以獲得最佳結果。那麼為什麼這很重要呢？要回答這個問題，我們首先需要了解三個概念：

- _分詞_ = 模型如何「看到」提示
- _基礎LLM_ = 基礎模型如何「處理」提示
- _指令調整的LLM_ = 模型如何現在可以看到「任務」

### 分詞

LLM將提示視為_token序列_，不同的模型（或模型版本）可以以不同的方式對同一提示進行分詞。由於LLM是基於token訓練的（而不是原始文本），提示的分詞方式直接影響生成回應的質量。

要了解分詞如何工作，請嘗試像下面展示的[OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst)這樣的工具。複製您的提示——並查看它如何轉換為token，注意空白字符和標點符號的處理方式。請注意，此示例顯示的是較舊的LLM（GPT-3）——因此使用較新模型嘗試此操作可能會產生不同的結果。

### 概念：基礎模型

一旦提示被分詞，「基礎LLM」（或基礎模型）的主要功能就是預測該序列中的token。由於LLM是基於大量文本數據集訓練的，它們對token之間的統計關係有很好的理解，並且可以相當有信心地進行預測。請注意，它們並不理解提示或token中的單詞的_意義_；它們只是看到一個可以用下一次預測「完成」的模式。它們可以繼續預測序列，直到被用戶干預或某些預設條件終止。

想看看基於提示的完成如何工作？在Azure OpenAI Studio的[_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)中輸入上述提示，使用默認設置。系統被配置為將提示視為信息請求——因此您應該看到一個滿足此上下文的完成。

但如果用戶想看到符合某些標準或任務目標的具體內容呢？這就是_指令調整_的LLM的作用。

### 概念：指令調整的LLM

[指令調整的LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)從基礎模型開始，並用示例或輸入/輸出對（例如，多輪「消息」）進行微調，這些對可以包含明確的指令——AI的回應嘗試遵循這些指令。

這使用了像人類反饋的強化學習（RLHF）這樣的技術，可以訓練模型_遵循指令_和_從反饋中學習_，以便生成更適合實際應用和更符合用戶目標的回應。

讓我們來試試——重訪上面的提示，但現在將_系統消息_更改為提供以下指令作為上下文：

> _將提供的內容總結為二年級學生。將結果保持在一段中，並包含3-5個要點。_

看看結果現在如何調整以反映所需的目標和格式？教育者現在可以直接在該班級的幻燈片中使用此回應。

## 為什麼我們需要提示工程？

現在我們知道提示是如何被LLM處理的，讓我們來談談為什麼我們需要提示工程。答案在於當前的LLM存在許多挑戰，使得在不投入精力於提示構建和優化的情況下_實現可靠和一致的完成_更具挑戰性。例如：

1. **模型回應是隨機的。** _相同的提示_可能會在不同的模型或模型版本中產生不同的回應。甚至可能在_相同的模型_上在不同時間產生不同的結果。_提示工程技術可以通過提供更好的保障措施來幫助我們減少這些變化_。

2. **模型可以捏造回應。** 模型是基於_大但有限_的數據集預訓練的，這意味著它們缺乏關於訓練範圍之外概念的知識。因此，它們可能會生成不準確、虛構或直接與已知事實相矛盾的完成。_提示工程技術幫助用戶識別和減少此類捏造，例如，通過要求AI提供引文或推理_。

3. **模型能力會有所不同。** 更新的模型或模型代會有更豐富的能力，但也會帶來成本和複雜性方面的獨特問題和權衡。_提示工程可以幫助我們開發最佳實踐和工作流程，以抽象掉差異並以可擴展、無縫的方式適應特定模型的要求_。

讓我們在OpenAI或Azure OpenAI Playground中看看這些問題的實際操作：

- 使用不同的LLM部署（例如，OpenAI、Azure OpenAI、Hugging Face）使用相同的提示——您是否看到了變化？
- 在_相同_的LLM部署中重複使用相同的提示（例如，Azure OpenAI playground）——這些變化有何不同？

### 捏造示例

在本課程中，我們使用術語**「捏造」**來描述LLM有時會由於訓練或其他限制而生成事實不正確的信息的現象。您可能在流行文章或研究論文中聽過這被稱為_「幻覺」_。然而，我們強烈建議使用_「捏造」_這個術語，以免在描述機器驅動的結果時無意中賦予其人類特徵。這也從術語角度強化了[負責任AI指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去除可能在某些上下文中被認為是冒犯或不包容的術語。

想了解捏造是如何工作的嗎？想一個提示，指示AI為一個不存在的主題生成內容（以確保它不在訓練數據集中）。例如，我嘗試了這個提示：

> **提示：**為2076年的火星戰爭生成一個教學計劃。

網絡搜索顯示，存在關於火星戰爭的虛構賬目（例如，電視劇或書籍）——但沒有在2076年。常識也告訴我們，2076年是_未來_，因此，無法與真實事件相關聯。

那麼，當我們在不同的LLM提供商中運行此提示時會發生什麼？

> **回應1：** OpenAI Playground（GPT-35）

> **回應2：** Azure OpenAI Playground（GPT-35）

> **回應3：** : Hugging Face Chat Playground（LLama-2）

如預期的那樣，由於隨機行為和模型能力的變化，每個模型（或模型版本）產生略有不同的回應。例如，一個模型針對8年級受眾，而另一個假設高中生。但所有三個模型都生成了可能讓不知情的用戶相信事件是真實的回應。

提示工程技術如_元提示_和_溫度配置_可能在某種程度上減少模型捏造。新的提示工程_架構_也將新工具和技術無縫集成到提示流中，以減少或減輕這些影響。

## 案例研究：GitHub Copilot

讓我們通過查看一個案例研究來結束這一部分，以了解提示工程在現實世界解決方案中的應用：[GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot是您的「AI配對程序員」——它將文本提示轉換為代碼完成，並集成到您的開發環境（例如，Visual Studio Code）中，以提供無縫的用戶體驗。如以下一系列博客所述，最早的版本是基於OpenAI Codex模型的——工程師很快意識到需要微調模型並開發更好的提示工程技術，以提高代碼質量。在七月，他們[推出了一個超越Codex的改進AI模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，以提供更快的建議。

按順序閱讀這些文章，以跟隨他們的學習旅程。

- **2023年5月** | [GitHub Copilot在理解您的代碼方面變得更好](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [GitHub內部：與GitHub Copilot背後的LLM合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年6月** | [如何為GitHub Copilot編寫更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年7月** | [.. GitHub Copilot超越Codex，具有改進的AI模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [開發者指南：提示工程和LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何構建企業LLM應用程序：GitHub Copilot的經驗教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

您還可以瀏覽他們的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)，以獲得更多類似[這篇](https://github.blog/2023-09-27-how-i-used-g
最後，範本的真正價值在於能夠為垂直應用領域創建和發布_提示庫_，其中提示範本現在已被_優化_以反映應用特定的背景或示例，使回應對目標用戶群體更具相關性和準確性。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)存儲庫是這種方法的一個很好例子，策劃了一個教育領域的提示庫，強調如課程計劃、課程設計、學生輔導等關鍵目標。

## 支援內容

如果我們認為提示構建包括指令（任務）和目標（主要內容），那麼_次要內容_就像是我們提供的額外背景，以某種方式**影響輸出**。這可能是調整參數、格式指令、主題分類等，可以幫助模型_定制_其回應以符合期望的用戶目標或期望。

例如：給定一個課程目錄，包含所有課程的詳細元數據（名稱、描述、等級、元數據標籤、講師等）：

- 我們可以定義一個指令來「總結2023年秋季課程目錄」
- 我們可以使用主要內容提供一些期望輸出的示例
- 我們可以使用次要內容識別最感興趣的前5個「標籤」。

現在，模型可以以示例所示的格式提供摘要 - 但如果結果有多個標籤，它可以優先考慮次要內容中識別的5個標籤。

---

<!--
課程範本：
這個單元應涵蓋核心概念#1。
用例子和參考來加強這個概念。

概念#3：
提示工程技術。
有哪些基本的提示工程技術？
用一些練習來說明。
-->

## 提示最佳實踐

現在我們知道如何構建提示，我們可以開始思考如何設計它們以反映最佳實踐。我們可以將這分為兩部分 - 擁有正確的_心態_和應用正確的_技術_。

### 提示工程心態

提示工程是一個試錯過程，因此請記住三個廣泛的指導因素：

1. **領域理解很重要。** 回應的準確性和相關性取決於應用或用戶運行的_領域_。運用你的直覺和領域專業知識進一步**定制技術**。例如，在系統提示中定義_領域特定個性_，或在用戶提示中使用_領域特定範本_。提供反映領域特定背景的次要內容，或使用_領域特定提示和示例_引導模型朝向熟悉的使用模式。

2. **模型理解很重要。** 我們知道模型本質上是隨機的。但模型實現也可能因其使用的訓練數據集（預訓練知識）、提供的功能（例如通過API或SDK）以及優化的內容類型（例如，代碼與圖像與文本）而有所不同。了解你使用的模型的優勢和限制，並利用這些知識來_優先考慮任務_或構建_定制範本_，以優化模型的能力。

3. **迭代和驗證很重要。** 模型正在快速演變，提示工程的技術也是如此。作為領域專家，你可能有其他上下文或標準_你的_特定應用，可能不適用於更廣泛的社群。使用提示工程工具和技術「快速啟動」提示構建，然後使用你的直覺和領域專業知識迭代並驗證結果。記錄你的見解並創建一個**知識庫**（例如，提示庫），可供他人用作新基準，為未來的更快迭代提供支持。

## 最佳實踐

現在讓我們看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)和[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)從業者推薦的常見最佳實踐。

| 什麼                              | 為什麼                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 評估最新模型。       | 新一代模型可能具有改進的功能和質量 - 但也可能會產生更高的成本。評估它們的影響，然後做出遷移決策。                                                                                |
| 分離指令和上下文   | 檢查你的模型/提供者是否定義_分隔符_以更清楚地區分指令、主要和次要內容。這可以幫助模型更準確地分配權重給標記。                                                         |
| 具體和清晰             | 提供更多有關期望的背景、結果、長度、格式、風格等的詳細信息。這將改善回應的質量和一致性。將配方捕獲在可重用範本中。                                                          |
| 描述性，使用例子      | 模型可能對「展示和講解」方法反應更好。從`zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- 選擇運行時核心。如果使用選項1或2，只需選擇開發容器提供的默認Python 3.10.x核心。

你已準備好運行練習。注意，這裡沒有_對錯_答案 - 只是通過試錯探索選項，並為給定模型和應用領域建立直覺。

_因此，本課程中沒有代碼解決方案段落。相反，Notebook將有標題為「我的解決方案：」的Markdown單元格，顯示一個示例輸出供參考。_

 <!--
課程範本：
用總結和自我導向學習資源包裹這一部分。
-->

## 知識檢查

以下哪一個是遵循合理最佳實踐的良好提示？

1. 給我看一張紅色車的圖片
2. 給我看一張紅色車的圖片，車型為沃爾沃XC90，停在懸崖邊，夕陽西下
3. 給我看一張紅色車的圖片，車型為沃爾沃XC90

A: 2，這是最好的提示，因為它提供了「什麼」的細節並深入具體（不僅僅是任何車，而是特定的品牌和型號），並且描述了整體環境。3是次佳，因為它也包含了很多描述。

## 🚀 挑戰

看看你能否利用「提示」技術，提示：「完成句子『給我看一張紅色車的圖片，車型為沃爾沃和』。」它的回應是什麼，你會如何改善它？

## 很棒的工作！繼續你的學習

想要了解更多不同的提示工程概念嗎？前往[持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以找到其他有關此主題的精彩資源。

前往第5課，我們將探討[高級提示技術](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免責聲明**：
本文檔是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始文件的母語版本視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對於使用此翻譯而引起的任何誤解或誤讀不承擔責任。