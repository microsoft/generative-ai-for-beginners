# 提示工程基礎

[![提示工程基礎](../../../translated_images/zh-TW/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## 介紹
本單元涵蓋了在生成式 AI 模型中創建有效提示的基本概念和技術。你對大型語言模型（LLM）撰寫提示的方式同樣重要。精心設計的提示可以實現更高品質的回應。但究竟什麼是「提示」和「提示工程」？我們該如何改善發送給 LLM 的提示輸入？這些問題將在本章節及下一章節中嘗試回答。

_生成式 AI_ 能夠回應使用者請求，創造出新內容（例如：文字、圖像、音訊、程式碼等）。它透過像 OpenAI 的 GPT（「生成式預訓練轉換器」）系列這樣的_大型語言模型_來達成，這些模型受過使用自然語言和程式碼的訓練。

使用者現在可以使用熟悉的聊天模式與這些模型互動，無需任何技術專業知識或培訓。這些模型是_基於提示_的——使用者送出文字輸入（提示），然後取得 AI 回應（完成結果）。他們可以反覆「與 AI 聊天」，在多回合對話中不斷調整提示，直到回應符合期望。

「提示」現在成為生成式 AI 應用的主要_程式設計介面_，指示模型該做什麼，並影響回傳結果的品質。「提示工程」是一個快速成長的研究領域，專注於_設計和優化_提示，以大規模傳遞一致且高品質的回應。

## 學習目標

本課程將學習什麼是提示工程、為何重要，以及如何為給定的模型和應用目標設計更有效的提示。我們將了解提示工程的核心概念和最佳實踐，並學習使用一個互動式 Jupyter 筆記本「沙盒」環境，在其中將這些概念應用於實際範例。

完成本課程後，我們將能夠：

1. 解釋提示工程是什麼以及它的重要性。
2. 描述提示的組成部分及其使用方式。
3. 學習提示工程的最佳實務和技術。
4. 利用 OpenAI 端點將學到的技術應用於實例。

## 關鍵術語

提示工程：設計和改良輸入，以引導 AI 模型產生期望輸出的做法。  
分詞(tokenization)：將文字轉換成模型可理解和處理的更小單位（稱為標記）的過程。  
指令微調的大型語言模型(Instruction-Tuned LLMs)：經由特定指令微調，以提升回應精確度和相關性的 LLM。

## 學習沙盒

提示工程目前更多是藝術而非科學。提升直覺的最好方法是_多加練習_，採用結合領域專業知識、推薦技術及模型特有最佳化的嘗試錯誤方法。

搭配本課的 Jupyter 筆記本提供一個_沙盒_環境，可讓你在學習過程中或課末的程式挑戰中嘗試所學。執行練習需要：

1. **Azure OpenAI API 金鑰**——已部署 LLM 的服務端點。  
2. **Python 執行環境**——可執行筆記本的環境。  
3. <strong>本機環境變數</strong>——_請立即完成 [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) 步驟以準備_。

筆記本附有_入門_練習——但鼓勵你新增自己的_Markdown_（說明）和_程式碼_（提示請求）區段，嘗試更多範例或想法，並建立提示設計的直覺。

## 圖解指南

想在深入學習前對本課概覽全貌嗎？看看這份圖解指南，它帶你了解主要涵蓋主題及每個主題的關鍵面向。課程地圖將帶領你從理解核心概念與挑戰，到採用相關的提示工程技術和最佳實務應對它們。請注意，此指南中的「進階技術」章節指的是本課程_下一章節_涵蓋的內容。

![提示工程圖解指南](../../../translated_images/zh-TW/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## 我們的新創公司

現在，讓我們談談_此主題_如何與我們推動[將 AI 創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)的新創使命相關。我們希望建立基於 AI 的_個人化學習_應用——來想想不同使用者如何「設計」他們使用的提示：

- <strong>管理員</strong>可能請 AI_分析課程資料以找出內容涵蓋的缺口_。AI 可以摘要結果，或用程式碼視覺化。  
- <strong>教師</strong>可能請 AI_生成針對特定對象和主題的教案_。AI 可以以指定格式建構個人化計畫。  
- <strong>學生</strong>可能請 AI_在難題上輔導他們_。AI 現在能用符合他們水準的課程、提示與範例引導學生。

這還只是冰山一角。看看 [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)——這是由教育專家精心策劃的開源提示庫——幫你更全面了解可能性！_試著在沙盒或使用 OpenAI Playground 執行這些提示，看看會發生什麼！_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## 什麼是提示工程？

我們從定義<strong>提示工程</strong>開始，它是設計和優化文字輸入（提示），以針對特定應用目標和模型產生一致、高品質回應（完成結果）的過程。我們可以將其視為兩步驟：

- _為特定模型和目標設計_初始提示  
- _反覆調整_提示以提升回應品質

這必然是一個需依靠用戶直覺和努力的嘗試錯誤過程，以取得最佳結果。那為什麼重要？為了回答這個問題，我們先了解三個概念：

- _分詞_＝模型如何「看」提示  
- _基礎 LLM_＝基礎模型如何「處理」提示  
- _指令微調 LLM_＝模型如何能「理解任務」

### 分詞(Tokenization)

LLM 將提示視為_標記的序列_，不同模型（或同一模型的不同版本）對同一提示的分詞方式可能不同。由於 LLM 是以標記而非純文本進行訓練，提示如何被分詞直接影響生成回應的品質。

想直覺感受分詞如何運作，可嘗試 [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) 工具（如下圖所示）。貼上你的提示，看它如何被轉換成標記，注意空白字元和標點符號的處理方式。此範例使用較舊的 LLM（GPT-3），換用較新模型結果可能不同。

![分詞示意](../../../translated_images/zh-TW/04-tokenizer-example.e71f0a0f70356c5c.webp)

### 概念：基礎模型(Foundation Models)

提示經分詞後，_「基礎 LLM」_（或基礎模型）的主要功能就是預測序列中的下一個標記。因為 LLM 是在龐大文字資料集上訓練，能掌握標記間統計關係，並有信心進行預測。請注意它們不理解提示中詞語的_意義_；只是看到可「補完」的模式。模型會不斷預測序列，直到使用者停止或達到預設條件。

想看提示生成運作嗎？將上述提示輸入 Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)，使用預設設定。系統會將提示視為資訊請求，你應會看到符合該情境的完成結果。

若使用者想要看到符合特定條件或任務目標的內容呢？這時，_指令微調_的 LLM 就派上用場了。

![基礎 LLM 聊天完成示意](../../../translated_images/zh-TW/04-playground-chat-base.65b76fcfde0caa67.webp)

### 概念：指令微調 LLM

[指令微調 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) 在基礎模型基礎上，利用帶有明確指令的範例或輸入/輸出對（例如多回合「訊息」）微調模型，讓 AI 致力於遵循這些指令。

此過程使用類似以人力回饋強化學習（RLHF）的技術，訓練模型_遵守指令_並從反饋中學習，使回應更切合實際應用且符合使用者目標。

試試看：回到上述提示，但將 _系統訊息_ 改成以下情境指令：

> _幫助二年級學生摘要你所收到的內容。結果保持一段落，並包含3-5個重點條列。_

看看結果如何調整成符合目標與格式？教育者現在能直接用此回應做該堂課的簡報。

![指令微調 LLM 聊天完成示意](../../../translated_images/zh-TW/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## 為什麼我們需要提示工程？

了解提示如何被 LLM 處理後，讓我們談談為什麼需要提示工程。原因是目前 LLM 存在多項挑戰，若不花心思設計和優化提示，很難達成_可靠且一致的完成結果_。例如：

1. **模型回應具有隨機性。**_相同的提示_在不同模型或不同版本間往往產生差異，甚至在_相同模型_的不同時間也可能有不同結果。_提示工程技術有助我們用更好的界限降低這些變異_。

1. <strong>模型可能虛構回應。</strong>模型是以_龐大但有限_的資料集預訓練，缺乏訓練外之知識，因此可能產生不正確、空想或與已知事實直接矛盾的內容。_提示工程技巧幫助使用者辨識並減輕此類虛構，例如要求 AI 引用來源或推理_。

1. <strong>模型能力會有所差異。</strong>較新的模型世代具備更豐富功能，但也帶來成本與複雜性的特有限制。_提示工程能協助我們發展最佳實務和工作流程，以抽象化差異，並以可擴展且無縫方式調適特定模型需求_。

我們可以在 OpenAI 或 Azure OpenAI Playground 實際測試：

- 用相同提示嘗試不同 LLM 部署（如 OpenAI、Azure OpenAI、Hugging Face）——是否見到差異？  
- 在_同一_ LLM 部署（例如 Azure OpenAI Playground）中反覆使用相同提示——這些差異如何？

### 虛構回應範例

在本課程，我們以<strong>「虛構（fabrication）」</strong>一詞指代 LLM 有時因訓練限制或其他因素產生事實錯誤訊息的現象。你或許在通俗文章或研究論文中聽過這稱為_「幻覺（hallucinations）」_。不過我們強烈建議使用_「虛構」_，避免不小心以人性化詞彙描述機器行為，並符合[負責任的 AI 指導原則](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，移除可能冒犯或不包容的用詞。

想體會虛構如何發生？想像一個提示指示 AI 生成不存在主題的內容（確保訓練資料中不曾出現）。例如，我嘗試了這個提示：

> **提示：** 生成 2076 年火星戰爭的教案。
一次網路搜尋顯示，有關火星戰爭的虛構敘述（例如電視劇或書籍）——但沒有在2076年的虛構作品。常識也告訴我們，2076年是_未來_，因此不可能與真實事件有關。

那麼，當我們用不同的大型語言模型供應商執行這個提示時會發生什麼？

> **回應 1**：OpenAI Playground（GPT-35）

![Response 1](../../../translated_images/zh-TW/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **回應 2**：Azure OpenAI Playground（GPT-35）

![Response 2](../../../translated_images/zh-TW/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **回應 3**：Hugging Face 聊天 Playground（LLama-2）

![Response 3](../../../translated_images/zh-TW/04-fabrication-huggingchat.faf82a0a51278956.webp)

如預期，每個模型（或模型版本）基於隨機行為和模型能力差異，產生略有不同的回答。例如，一個模型的目標聽眾是8年級學生，而另一個則假設是高中生。但這三個模型都產生了能讓不知情使用者相信該事件是真實的回應。

彈性提示工程技術如_元提示_和_溫度參數設定_，可能在某種程度上降低模型捏造的情況。新的提示工程_架構_也將新工具和技術無縫整合進提示流程中，以減輕或降低這些影響。

## 個案研究：GitHub Copilot

讓我們透過一個個案研究來瞭解提示工程如何在現實世界的解決方案中發揮作用：[GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot 是你的「AI 結對程式設計師」——它將文字提示轉換成程式碼補全，並整合於你的開發環境中（例如 Visual Studio Code），提供無縫的使用體驗。依據下面一系列的部落格紀錄，最初版本是基於 OpenAI Codex 模型，工程師很快意識到需要微調模型並開發更好的提示工程技術，以提升程式碼品質。今年七月，他們[發表了比 Codex 更先進的 AI 模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，提供更快速的建議。

請依序閱讀這些文章，以跟隨他們的學習歷程：

- **2023年5月**｜[GitHub Copilot 正在更好地理解你的程式碼](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月**｜[GitHub 內部揭秘：與 GitHub Copilot 背後的 LLMs 合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023年6月**｜[如何為 GitHub Copilot 撰寫更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023年7月**｜[.. GitHub Copilot 以改良的 AI 模型超越 Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月**｜[開發者指南：提示工程與大型語言模型](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月**｜[如何打造企業級 LLM 應用：來自 GitHub Copilot 的經驗教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

你也可以瀏覽他們的[工程部落格](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)來了解更多像[這篇](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)展示了這些模型和技術如何_應用_於驅動現實世界應用的文章。

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## 提示構建

我們已經了解到為何提示工程至關重要——現在讓我們了解提示如何被_構建_，以評估不同技術來設計更有效的提示。

### 基本提示

先從基本提示開始：一個純文字輸入送入模型，沒有其他上下文。以下是一個範例——當我們將美國國歌前幾個字送至 OpenAI 的[Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)時，模型會立即_補全_接下來的幾行歌詞，說明基本的預測行為。

| 提示（輸入）         | 補全（輸出）                                                                                                                          |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | 聽起來你在開始唱「星條旗永不落」的歌詞，即美國的國歌。完整歌詞是…                                                                                   |

### 複雜提示

現在在那個基本提示上加入上下文和指示。[Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst)讓我們將複雜的提示建構成一組_訊息_，包含：

- 輸入/輸出對，反映_使用者_輸入和_助理_回答
- 系統訊息，設定助理的行為或個性上下文

請求格式如下，其中的_tokenization_有效擷取上下文和對話中的相關資訊。改變系統上下文對完成品質的影響可與使用者輸入同等重要。

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### 指令提示

上述範例中，用戶提示是簡單的文字查詢，可解讀為資訊請求。使用_指令_提示時，我們能用該文字更詳細地指定任務，為 AI 提供更佳指導。範例如下：

| 提示（輸入）                                                                                                                                                                                                                         | 補全（輸出）                                                                                                             | 指令類型          |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :---------------- |
| Write a description of the Civil War                                                                                                                                                                                                 | _回傳一段簡單文字_                                                                                                       | 簡單              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                 | _回傳一段文字，接著列出重要事件日期及其描述_                                                                            | 複雜              |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _回傳內容更詳盡，以 JSON 格式呈現於文字框中，你可以複製貼上到檔案並視需求驗證_                                      | 複雜。格式化。    |

## 主要內容

上述範例中，提示仍然相當開放，讓大型語言模型決定它的預訓練資料中哪些部分是相關的。利用_主要內容_設計模式，輸入文字分為兩部分：

- 指令（動作）
- 相關內容（影響動作）

以下範例中，指令為「用兩句話總結」。

| 提示（輸入）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 補全（輸出）                                                                                                                                                                                                                                                                                |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 木星是距離太陽第五顆行星，也是太陽系最大的行星。它是一個氣態巨星，質量是太陽的千分之一，但比太陽系中所有其他行星的質量總和還大兩倍半。肉眼可見的夜空中，木星是最亮的天體之一，自有歷史記錄以來，古文明就認識它。它以羅馬神祇朱庇特命名。[19] 從地球觀察，木星反射的光足夠投下可見陰影，[20] 並且平均是夜空中繼月亮和金星之後第三亮的自然天體。 <br/> <strong>請用兩句短話總結</strong> | 木星是距離太陽第五顆行星，也是太陽系最大的行星之一，並且是夜空中最亮的天體之一。它以羅馬神祇朱庇特命名，是一顆氣態巨星，其質量是太陽系其他行星總和的兩倍半。                                                                                                                      |

主要內容的區塊可用多種方式來驅動更有效的指令：

- <strong>範例</strong>——與其明確告訴模型要做什麼，不如給它想要的輸出範例，讓它自行推斷模式。
- <strong>提示語</strong>——緊接著指令給模型一個「提示語」，引導模型往更相關的回答方向發展。
- <strong>模板</strong>——可重複使用的提示「配方」，其中含有可用於特定用例的資料自訂的占位符（變數）。

讓我們來看看具體做法。

### 使用範例

這種方法利用主要內容「提供模型」一些想要輸出的範例，讓它推斷想要輸出的模式。根據提供範例數量，我們有零次學習提示（一擊）、單次學習提示（單擊）、少量學習提示等。

提示現由三個部份組成：

- 任務描述
- 幾個想要的輸出範例
- 新範例的開頭（變成隱含任務描述）

| 學習類型       | 提示（輸入）                                                                                                                                                             | 補全（輸出）              |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| 零次學習       | "The Sun is Shining". 翻譯成西班牙語                                                                                                                                | "El Sol está brillando".  |
| 一次學習       | "The Sun is Shining" => "El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                                   | "Es un día frío y ventoso". |
| 少量學習       | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => Basketball          | 範例                      |
|                |                                                                                                                                                                     |                           |

注意在零次學習時，我們必須提供明確指令（「翻譯成西班牙語」），但在一次學習範例中，模型就能推斷指令。少量學習的例子展示了增加更多範例，讓模型在沒有額外指令的情況下做出更準確推斷。

### 提示語

另一種使用主要內容的方法是提供_提示語_而非範例。在此，我們藉由_用一段片段_「開始」想要的回應格式，讓模型「接受提示」，繼續以該格式回應。

| 提示語數量   | 提示（輸入）                                                                                                                                                                                                                                                                                                                                                                                                                                            | 補全（輸出）                                                                                                                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0             | 木星是距離太陽第五顆行星，也是太陽系最大的行星。它是一個氣態巨星，質量是太陽的千分之一，但比太陽系中所有其他行星的質量總和還大兩倍半。肉眼可見的夜空中，木星是最亮的天體之一，自有歷史記錄以來，古文明就認識它。 <br/><strong>請總結此段</strong>                                                                                          | 木星是太陽系中最大的行星，也是第五顆離太陽最近的行星。它是一顆氣態巨星，質量為太陽的千分之一，但比其他所有行星加起來還重。古代文明長久以來就認識木星，且它在夜空中十分明亮。                                                                                                                                                  |
| 1              | 木星是距太陽第五顆行星，也是太陽系中最大的行星。它是一顆氣體巨行星，質量約為太陽的千分之一，但卻是太陽系中所有其他行星質量總和的兩倍半。木星是夜空肉眼可見的最明亮天體之一，並且自有文字記錄前的古代文明以來就為人所知。<br/><strong>總結</strong><br/>我們學到的是，木星 | 是距太陽第五顆行星，也是太陽系中最大的行星。它是一顆氣體巨行星，質量約為太陽的千分之一，但卻是所有其他行星總和的兩倍半。肉眼可輕易看到，並且自古代以來就為人所知。                         |
| 2              | 木星是距太陽第五顆行星，也是太陽系中最大的行星。它是一顆氣體巨行星，質量約為太陽的千分之一，但卻是太陽系中所有其他行星質量總和的兩倍半。木星是夜空中肉眼可見的最明亮天體之一，自有文字記錄前的古代文明以來就為人所知。<br/><strong>總結</strong><br/>我們學到的三大事實：         | 1. 木星是距太陽第五顆行星，也是太陽系中最大的行星。<br/> 2. 它是一顆氣體巨行星，質量約為太陽的千分之一...<br/> 3. 木星自古代以來就肉眼可見...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

提示模板是一種 _預先定義好的提示配方_，可以按需儲存和重複使用，以推動更一致的使用者經驗。在最簡單的形式中，它只是一組提示範例，就像 [這個來自 OpenAI 的範例](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst)，其中同時提供了互動式提示元件（用戶和系統訊息）以及 API 請求格式——方便重用。

在更複雜的形式中，如 [LangChain 的範例](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst)，它包含可用各種來源資料（用戶輸入、系統上下文、外部資料來源等）替換的 _佔位符_，能動態生成提示。這讓我們可以創建可重用的提示庫，<strong>程式化地</strong>推動一致的使用者體驗。

最終，這些模板的真正價值在於能針對垂直應用領域製作和發布 _提示庫_，該提示模板經過 _優化_，反映特定應用的上下文或範例，使回應更加相關且準確地符合目標使用者群。像是 [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 倉庫就是這種方法的極佳範例，策劃了關注課程規劃、課程設計、學生輔導等教育領域重點目標的提示庫。

## Supporting Content

如果把提示構成看作包含指令（任務）和目標（主要內容），那麼 _次要內容_ 就像是我們額外提供的背景資訊，用來 <strong>影響輸出內容</strong>。次要內容可能是調整參數、格式化指令、主題分類法等，可以幫助模型 _客製化_ 回應，使其更符合期望的使用者目標。

舉例來說：在課程目錄中有廣泛的元資料（名稱、描述、等級、元資料標籤、講師等等）：

- 我們可以定義指令為「總結 2023 年秋季的課程目錄」
- 用主要內容提供一些期望輸出的範例
- 用次要內容標示最受關注的五個「標籤」

這樣模型可以依照範例格式提供摘要，如果一個結果含有多個標籤，則會優先處理次要內容中指出的五個標籤。

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Prompting Best Practices

既然我們已經了解如何 _構造_ 提示，就可以開始思考如何 _設計_ 提示以符合最佳實務。我們可以從兩方面來思考——擁有正確的 _心態_ 和應用正確的 _技巧_。

### Prompt Engineering Mindset

提示工程是一種試錯過程，請記住以下三個廣泛的指導因素：

1. **領域知識很重要。** 回應的準確度和相關性取決於應用或用戶所屬的 _領域_。請運用直覺和領域專長來 <strong>進一步客製化技巧</strong>。例如，在系統提示中定義 _領域特定的人格_，或在用戶提示中使用 _領域專用模板_。提供反映特定領域上下文的次要內容，或用 _領域相關的暗示與範例_ 引導模型符合熟悉的使用模式。

2. **了解模型性質很重要。** 我們知道模型本質上是隨機生成的。但模型的實作也會因訓練資料（預訓練知識）、提供的能力（例如透過 API 或 SDK）、以及優化的內容型別（代碼、圖片、文字等）而異。了解你使用的模型的優勢與限制，並用這些知識去 _優先排序任務_、或建立 _客製化模板_，讓其符合模型的特長。

3. **反覆迭代與驗證很重要。** 模型與提示工程技術都在快速演進。作為領域專家，你可能有其他背景或標準只適用於 _你_ 具體的應用，而非普遍社群。使用提示工程工具和技巧來「快速啟動」提示構造，再用你的直覺與領域經驗反覆迭代與驗證結果。將你的見解記錄下來並建立 <strong>知識庫</strong>（例如提示庫），成為其他人未來能快速迭代的基礎。

## Best Practices

以下是由 [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) 和 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) 實務者們建議的常見最佳做法。

| 項目                              | 原因                                                                                                                                                                                                                                              |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 評估最新模型                      | 新一代模型往往具備改進的特性與品質，但成本可能更高。要先評估影響再決定是否遷移。                                                                                                                        |
| 區分指令與上下文                  | 檢查你的模型或供應商是否定義了 _界定符_ 以更明確區分指令、主要與次要內容。這有助模型更準確地為詞元分配權重。                                                                                              |
| 明確並具體說明                   | 詳細說明期望的上下文、結果、長度、格式、風格等，有助提升回應的品質與一致性。將這些規則整合成可重用的模板。                                                                                                 |
| 多用描述與範例                   | 模型對於「展示並說明」的方式通常反應更好。可以先試試「零 shot」方式（只給指令，無範例），然後再用「少數 shot」提供幾個期望輸出的範例做優化。用比喻也很有效。                                                    |
| 利用暗示啟動生成                 | 透過提供引導詞或片語，讓模型有個明確起點，有助引導它生成理想的結果。                                                                                                                           |
| 重複強調                         | 有時候需要重複說明，像是在主要內容前後都給指令，用指令配合暗示等等。持續迭代並驗證有效性。                                                                                                             |
| 呈現順序很重要                   | 提供給模型資訊的順序可能影響輸出結果，包括學習範例的順序，因為有近因偏差。試試不同組合找出最佳解。                                                                                                      |
| 給模型「退路」                   | 給模型一個 _後備_ 的預設回應，以免因無法完成任務而產生錯誤或捏造內容。                                                                                                                           |
|                                  |                                                                                                                                                                                                                                                   |

和任何最佳實務一樣，請記住根據模型、任務和領域，_你的狀況可能會不同_。將這些作為起點，持續反覆，找出最適合你的做法。當有新模型與工具推出時，要持續重新評估你的提示工程流程，著重流程的可擴展性及回應品質。

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

恭喜！你已經到了課程的最後！現在該將所學的概念和技巧用真實範例來檢驗了！

本次作業將使用 Jupyter Notebook，讓你可互動式完成練習。你也可以透過添加自己的 Markdown 和程式碼儲存格，探索與實驗更多想法與技巧。

### 開始前，先 Fork 倉庫，然後

- （推薦）啟動 GitHub Codespaces
- （或者）將倉庫克隆到本地設備，並在 Docker Desktop 環境使用
- （或者）使用你偏好的 Notebook 執行環境打開 Notebook

### 接著，設定環境變數

- 將倉庫根目錄中的 `.env.copy` 複製為 `.env`，並填入 `AZURE_OPENAI_API_KEY`、`AZURE_OPENAI_ENDPOINT` 和 `AZURE_OPENAI_DEPLOYMENT`。之後可回到 [Learning Sandbox 部分](#學習沙盒) 學習設定細節。

### 然後，打開 Jupyter Notebook

- 選擇運行核心。如果使用前兩種方案，直接選擇 dev 容器裡提供的預設 Python 3.10.x 核心即可。

你已準備好開始執行練習。請注意，這裡沒有絕對的「對錯」答案——而是透過試錯探索，培養你對特定模型與應用領域的直覺。

_基於此，課程中不會有完整程式碼解答段落，取而代之的是 Notebook 中「My Solution:」的 Markdown 儲存格，示範一個參考輸出。_

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Knowledge check

下列哪一個是合理且符合一些常見最佳實務的良好提示？

1. 給我一張紅色汽車的圖片
2. 給我一張紅色沃爾沃（Volvo）XC90，停在懸崖邊夕陽下的汽車圖片
3. 給我一張紅色沃爾沃（Volvo）XC90的汽車圖片

答案：2，因為它包含了「什麼」的詳細描述，並進一步具體說明（不只是任一輛車，而是特定品牌和車型）且還描述了整體場景。3 屬次之，因為也包含不少描述。

## 🚀 Challenge

試著用「暗示」技巧，搭配提示句：Complete the sentence "Show me an image of red car of make Volvo and "。它會回應什麼？你會如何改進它？

## Great Work! Continue Your Learning

想知道更多關於不同提示工程概念嗎？請造訪 [持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ，找到更多優質資源。

接著前往第五課，我們會探討[進階提示技巧](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->