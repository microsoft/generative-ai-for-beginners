<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:01:06+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "mo"
}
-->
# 提示工程基礎

## 介紹
本模組涵蓋了在生成式 AI 模型中創建有效提示的基本概念和技巧。撰寫提示的方式對於大型語言模型（LLM）來說也很重要。精心設計的提示可以獲得更高質量的回應。但像 _提示_ 和 _提示工程_ 這些術語究竟意味著什麼？我如何改善發送給 LLM 的提示 _輸入_？這些是我們將在本章和下一章中嘗試回答的問題。

生成式 AI 能夠根據用戶的要求創建新的內容（例如文本、圖像、音頻、代碼等）。它使用像 OpenAI 的 GPT 系列這樣的 _大型語言模型_ 來實現，這些模型經過自然語言和代碼的訓練。

現在，使用者可以使用像聊天這樣熟悉的方式與這些模型互動，無需任何技術專業知識或訓練。這些模型是基於提示的——使用者發送文本輸入（提示）並獲得 AI 回應（完成）。他們可以在多輪對話中迭代地與 AI 聊天，直到回應符合他們的期望。

“提示”現在成為生成式 AI 應用的主要 _編程介面_，告訴模型做什麼並影響返回回應的質量。“提示工程”是一個快速增長的研究領域，專注於提示的 _設計和優化_，以在大規模上提供一致和高質量的回應。

## 學習目標

在這節課中，我們學習什麼是提示工程，為什麼它重要，以及如何為給定的模型和應用目標設計更有效的提示。我們將了解提示工程的核心概念和最佳實踐——並了解一個互動式 Jupyter Notebooks “沙盒”環境，我們可以看到這些概念應用於真實例子。

到這節課結束時，我們將能夠：

1. 解釋什麼是提示工程及其重要性。
2. 描述提示的組成部分及其用途。
3. 學習提示工程的最佳實踐和技巧。
4. 使用 OpenAI 端點將所學技巧應用於真實例子。

## 關鍵術語

提示工程：設計和完善輸入以引導 AI 模型生成所需輸出的實踐。
分詞化：將文本轉換為模型可以理解和處理的較小單位（稱為 token）的過程。
指令調整的 LLM：經過特定指令微調以提高回應準確性和相關性的大型語言模型（LLM）。

## 學習沙盒

提示工程目前更多是一門藝術而非科學。提高我們對其的直覺的最佳方式是 _多加練習_，採用結合應用領域專業知識、推薦技術和模型特定優化的試錯法。

本課程附帶的 Jupyter Notebook 提供了一個 _沙盒_ 環境，您可以嘗試所學內容——在學習過程中或作為結尾代碼挑戰的一部分。要執行練習，您需要：

1. **Azure OpenAI API 密鑰** - 部署的 LLM 的服務端點。
2. **Python 運行環境** - Notebook 可以在其中執行。
3. **本地環境變量** - _現在完成 [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) 步驟以準備_。

Notebook 附帶 _入門_ 練習——但我們鼓勵您添加自己的 _Markdown_（描述）和 _Code_（提示請求）部分，嘗試更多例子或想法——並建立您的提示設計直覺。

## 圖解指南

想在深入了解之前了解本課程涵蓋的主要內容嗎？查看這份圖解指南，它讓您了解涵蓋的主要主題和每個主題需要考慮的關鍵要點。課程路線圖將帶您從理解核心概念和挑戰到使用相關提示工程技術和最佳實踐來解決它們。請注意，本指南中的“高級技術”部分指的是本課程的 _下一章_ 中涵蓋的內容。

## 我們的初創公司

現在，讓我們談談 _這個主題_ 與我們的初創公司使命 [將 AI 創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) 的關係。我們希望建立 AI 驅動的個性化學習應用——那麼讓我們思考一下我們應用的不同使用者如何“設計”提示：

- **管理員**可能會要求 AI _分析課程數據以識別覆蓋範圍中的缺口_。AI 可以總結結果或用代碼可視化它們。
- **教育工作者**可能會要求 AI _為目標受眾和主題生成課程計劃_。AI 可以按指定格式構建個性化計劃。
- **學生**可能會要求 AI _在困難的學科上輔導他們_。AI 現在可以根據學生的水平為他們提供課程、提示和示例。

這僅僅是冰山一角。查看 [教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - 由教育專家策劃的開源提示庫 - 以獲得更廣泛的可能性！_嘗試在沙盒中運行其中一些提示或使用 OpenAI Playground 看看會發生什麼！_

## 什麼是提示工程？

我們開始這節課時將 **提示工程** 定義為 _設計和優化_ 文本輸入（提示）以為給定的應用目標和模型提供一致和高質量回應（完成）的過程。我們可以將其視為兩步驟過程：

- 為給定模型和目標設計初始提示
- 迭代地完善提示以提高回應質量

這必然是一個需要用戶直覺和努力才能獲得最佳結果的試錯過程。那麼為什麼它重要？要回答這個問題，我們首先需要了解三個概念：

- _分詞化_ = 模型如何“看到”提示
- _基礎 LLMs_ = 基礎模型如何“處理”提示
- _指令調整的 LLMs_ = 模型現在如何看到“任務”

### 分詞化

LLM 將提示視為 _token 序列_，不同模型（或模型版本）可以以不同方式分詞同一提示。由於 LLMs 是基於 token 而不是原始文本進行訓練的，提示的分詞方式直接影響生成回應的質量。

要了解分詞如何運作，可以嘗試像 [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) 這樣的工具。將您的提示複製進去 - 看看如何將其轉換為 token，注意如何處理空白字符和標點符號。請注意，這個例子顯示的是舊版 LLM（GPT-3） - 所以用新版本模型可能會產生不同結果。

### 概念：基礎模型

一旦提示被分詞化，“基礎 LLM”（或基礎模型）的主要功能就是預測序列中的 token。由於 LLMs 是基於大量文本數據集進行訓練的，它們對 token 之間的統計關係有良好的感知，並能有信心地進行預測。請注意，它們並不理解提示或 token 中單詞的 _含義_；它們只是看到一個可以用下一次預測“完成”的模式。它們可以繼續預測序列，直到用戶干預或某些預先設置的條件終止。

想看看基於提示的完成如何運作？在 Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) 中輸入上述提示，使用默認設置。系統配置為將提示視為信息請求 - 所以您應該看到滿足此上下文的完成。

但如果用戶想看到滿足某些標準或任務目標的特定內容呢？這就是 _指令調整的_ LLMs 發揮作用的地方。

### 概念：指令調整的 LLMs

[指令調整的 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) 從基礎模型開始，並通過包含明確指令的例子或輸入/輸出對（例如多輪“消息”）進行微調 - AI 的回應試圖遵循該指令。

這使用了像人類反饋的強化學習（RLHF）這樣的技術，能夠訓練模型 _遵循指令_ 並 _從反饋中學習_，以便生成更適合實際應用並更符合用戶目標的回應。

讓我們試試看 - 重訪上述提示，但現在將 _系統消息_ 更改為提供以下指令作為上下文：

> _將提供的內容總結為二年級學生。將結果保持在一段中，並包含3-5個要點。_

看看結果現在是否反映了所需的目標和格式？教育工作者現在可以直接在他們的課堂幻燈片中使用這個回應。

## 為什麼我們需要提示工程？

現在我們知道提示如何被 LLMs 處理，讓我們來談談 _為什麼_ 我們需要提示工程。答案在於當前的 LLMs 提出了一些挑戰，使得不經努力的提示構建和優化更難以實現 _可靠和一致的完成_。例如：

1. **模型回應是隨機的。** 相同的提示在不同的模型或模型版本中可能會產生不同的回應。甚至可能在同一模型中不斷產生不同結果。_提示工程技術可以幫助我們通過提供更好的防護措施來減少這些變化_。

1. **模型可能會捏造回應。** 模型是基於 _大但有限_ 的數據集進行預訓練的，這意味著它們缺乏對訓練範圍外概念的知識。因此，它們可能會產生不準確、虛構或直接與已知事實相矛盾的完成。_提示工程技術幫助用戶識別並減少這些捏造，例如要求 AI 提供引文或推理_。

1. **模型能力會有所不同。** 新版本模型或模型代可能會擁有更豐富的能力，但也帶來獨特的妥協和成本及複雜性。_提示工程可以幫助我們開發最佳實踐和工作流程，以可擴展、無縫的方式抽象出差異並適應模型特定需求_。

讓我們在 OpenAI 或 Azure OpenAI Playground 中看看這些在實際中如何運作：

- 使用不同的 LLM 部署（例如，OpenAI、Azure OpenAI、Hugging Face）使用相同的提示 - 您是否看到了變化？
- 使用相同的 LLM 部署（例如，Azure OpenAI Playground）重複使用相同的提示 - 這些變化有何不同？

### 捏造例子

在本課程中，我們使用術語 **“捏造”** 來指代 LLMs 有時因訓練或其他限制而生成事實不正確的信息的現象。您可能也在流行文章或研究論文中聽到過這被稱為 _“幻覺”_。然而，我們強烈建議使用 _“捏造”_ 作為術語，以免無意中將人類特徵賦予機器驅動的結果。這也從術語角度加強了 [負責任的 AI 準則](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去除在某些上下文中可能被視為冒犯或不包容的術語。

想了解捏造如何運作？想一個提示，指示 AI 為不存在的主題生成內容（以確保它不在訓練數據集中）。例如 - 我嘗試了這個提示：

> **提示：** 生成2076年火星戰爭的課程計劃。

網絡搜索顯示有關火星戰爭的虛構敘述（例如電視劇或書籍） - 但沒有2076年。常識也告訴我們2076年是 _未來_，因此不能與真實事件相關聯。

那麼當我們使用不同的 LLM 提供商運行這個提示時會發生什麼？

如預期，每個模型（或模型版本）都產生了稍微不同的回應，這要歸因於隨機行為和模型能力的變化。例如，一個模型針對8年級觀眾，而另一個則假設高中生。但所有三個模型都生成了可能使不知情的用戶相信事件是真實的回應。

提示工程技術如 _元提示_ 和 _溫度配置_ 可能在某種程度上減少模型捏造。新的提示工程 _架構_ 也將新的工具和技術無縫整合到提示流中，以減輕或減少一些這些效果。

## 案例研究：GitHub Copilot

讓我們通過查看一個案例研究： [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)，了解提示工程在現實解決方案中如何使用。

GitHub Copilot 是您的“AI 配對程序員” - 它將文本提示轉換為代碼完成，並集成到您的開發環境中（例如 Visual Studio Code）以提供無縫的用戶體驗。如以下博客系列所述，最早版本基於 OpenAI Codex 模型 - 工程師迅速意識到需要微調模型並開發更好的提示工程技術，以提高代碼質量。在七月，他們 [推出了一個超越 Codex 的改進 AI 模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，以更快地提供建議。

按順序閱讀帖子，以跟隨他們的學習旅程。

- **2023年5月** | [GitHub Copilot 在理解您的代碼方面變得更好](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [GitHub內部：與 GitHub Copilot 背後的 LLMs 合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023年6月** | [如何為 GitHub Copilot 編寫更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [GitHub Copilot 超越 Codex 的改進 AI 模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [開發者的提示工程和 LLMs 指南](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何建立企業 LLM 應用：GitHub Copilot 的教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

您也可以瀏覽他們的 [工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) 以獲得更多像 [這篇](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) 的文章，展示這些模型和技術如何應用於推動現實世界應用。

## 提示構建

我們已經了解了提示工程的重要性 - 現在讓我們了解提示是如何 _構建_ 的，以便我們可以評估不同的技術以設計更有效的提示。

###
最後，模板的真正價值在於能夠為垂直應用領域創建和發布_提示庫_——在這些領域中，提示模板現在已被_優化_以反映應用程序特定的上下文或示例，使得回應對目標用戶群體更加相關和準確。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)庫就是這種方法的極佳例子，它精選了一個針對教育領域的提示庫，重點在於如課程規劃、課程設計、學生輔導等關鍵目標。

## 支持內容

如果我們將提示構建視為包含指令（任務）和目標（主要內容），那麼_次要內容_就像是我們提供的額外上下文以**某種方式影響輸出**。它可能是調整參數、格式指令、主題分類等，可以幫助模型_定制_其回應以符合所需的用戶目標或期望。

例如：給定一個課程目錄，其中包含所有課程的廣泛元數據（名稱、描述、級別、元數據標籤、講師等）：

- 我們可以定義一個指令來「總結2023年秋季的課程目錄」
- 我們可以使用主要內容提供一些所需輸出的示例
- 我們可以使用次要內容來識別最感興趣的5個「標籤」。

現在，模型可以按照示例所示的格式提供摘要，但如果結果有多個標籤，它可以優先考慮次要內容中識別的5個標籤。

---

## 提示最佳實踐

現在我們知道如何_構建_提示，我們可以開始思考如何_設計_它們以反映最佳實踐。我們可以從兩個部分來考慮——擁有正確的_心態_和應用正確的_技術_。

### 提示工程心態

提示工程是一個反覆試驗的過程，因此要記住三個廣泛的指導因素：

1. **領域理解很重要。** 回應的準確性和相關性是該應用程序或用戶操作的_領域_的函數。運用你的直覺和領域專業知識來進一步**定制技術**。例如，在系統提示中定義_領域特定的人格_，或在用戶提示中使用_領域特定的模板_。提供反映領域特定上下文的次要內容，或使用_領域特定的提示和示例_來引導模型朝向熟悉的使用模式。

2. **模型理解很重要。** 我們知道模型本質上是隨機的。但模型的實現也可能因其使用的訓練數據集（預訓練知識）、提供的能力（例如，通過API或SDK）以及其優化的內容類型（例如，代碼、圖像、文本）而有所不同。了解你正在使用的模型的優勢和限制，並利用這些知識來_優先排序任務_或構建_定制模板_以優化模型的能力。

3. **迭代和驗證很重要。** 模型正在快速演變，提示工程的技術也是如此。作為領域專家，你可能擁有其他上下文或標準_你的_特定應用程序，這可能不適用於更廣泛的社區。使用提示工程工具和技術來「快速啟動」提示構建，然後使用自己的直覺和領域專業知識迭代和驗證結果。記錄你的見解並創建一個**知識庫**（例如，提示庫），其他人可以用作新的基準，未來更快的迭代。

## 最佳實踐

現在讓我們看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)和[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)從業者推薦的常見最佳實踐。

| 內容                             | 原因                                                                                                                                                                                                                                               |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 評估最新模型。                   | 新模型世代可能具有改進的功能和質量，但也可能導致更高的成本。評估其影響，然後做出遷移決策。                                                                                                                 |
| 分離指令和上下文                 | 檢查你的模型/提供者是否定義了_分隔符_以更清楚地區分指令、主要和次要內容。這可以幫助模型更準確地分配權重給標記。                                                                                          |
| 具體而清晰                       | 提供更多關於所需上下文、結果、長度、格式、風格等的細節。這將提高回應的質量和一致性。將配方捕捉在可重用的模板中。                                                                                         |
| 描述性，使用示例                 | 模型可能對「展示和講解」方法反應更好。開始使用`zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT`值。回到[學習沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)學習如何。

### 接下來，打開Jupyter Notebook

- 選擇運行時核心。如果使用選項1或2，只需選擇開發容器提供的默認Python 3.10.x核心。

你已準備好運行練習。注意這裡沒有_正確和錯誤_的答案——只是通過反覆試驗探索選項並建立直覺，看看對給定模型和應用領域有效的內容。

_因此，本課程中沒有代碼解決方案部分。相反，Notebook將有標題為「我的解決方案：」的Markdown單元，顯示一個示例輸出供參考。_

## 知識檢查

以下哪一項是符合合理最佳實踐的良好提示？

1. 給我看一輛紅色汽車的圖片
2. 給我看一輛紅色汽車的圖片，品牌為Volvo，型號為XC90，停在懸崖邊，夕陽西下
3. 給我看一輛紅色汽車的圖片，品牌為Volvo，型號為XC90

A: 2，這是最好的提示，因為它提供了「什麼」的細節並深入到具體內容（不僅僅是任何汽車，而是特定的品牌和型號），它還描述了整體背景。3是次佳，因為它也包含了很多描述。

## 🚀 挑戰

看看你能否利用「提示」技術完成提示：「給我看一輛紅色汽車的圖片，品牌為Volvo和」。它會回應什麼，你會如何改進？

## 出色的工作！繼續你的學習

想了解更多不同的提示工程概念？前往[持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)尋找其他關於此主題的精彩資源。

前往第5課，我們將研究[高級提示技術](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯而產生的任何誤解或誤釋不承擔責任。