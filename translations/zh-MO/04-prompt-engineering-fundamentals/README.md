# Prompt Engineering Fundamentals

[![Prompt Engineering Fundamentals](../../../translated_images/zh-MO/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduction
本章節涵蓋了在生成式 AI 模型中創建有效提示的基本概念和技術。向大型語言模型（LLM）輸入提示的方式也很重要。精心設計的提示能夠獲得更高質量的回應。但諸如 _prompt_ 和 _prompt engineering_ 這些術語究竟意味著什麼？以及我如何改進發送給 LLM 的提示 _輸入_？這些都是我們將在本章和下一章嘗試解答的問題。

_生成式 AI_ 能夠根據用戶請求創造新的內容（例如，文字、圖片、音頻、程式碼等）。它通過使用如 OpenAI 的 GPT（「生成式預訓練轉換器」）系列等 _大型語言模型_ 來實現，這些模型在自然語言和程式碼上接受訓練。

用戶現在可以使用熟悉的範例，如對話方式與這些模型互動，無需任何技術專長或培訓。這些模型是 _基於提示_ 的——用戶發送文本輸入（提示），並獲得 AI 回應（完成）。他們可以反覆「與 AI 對話」，通過多輪對話精煉提示，直到回應符合期望。

「提示」現在成為生成式 AI 應用的主要 _程式設計介面_，告訴模型該做什麼，並影響返回回應的質量。「提示工程」是一個快速發展的研究領域，專注於 _設計和優化_ 提示，以實現規模化下的穩定且高質量回應。

## Learning Goals

在本課程中，我們將了解什麼是提示工程、為什麼它重要，以及如何針對特定模型和應用目標製作更有效的提示。我們將理解提示工程的核心概念及最佳實踐，並了解一個互動式 Jupyter 筆記本的「沙盒」環境，能看到這些概念如何應用於真實範例。

課程結束後，我們將能夠：

1. 解釋什麼是提示工程及其重要性。
2. 描述提示的組成部分及其用途。
3. 學習提示工程的最佳實踐和技術。
4. 利用 OpenAI 端點將學到的技術應用於真實範例。

## Key Terms

Prompt Engineering：設計和優化輸入以引導 AI 模型產生預期輸出的實踐。
Tokenization：將文本轉換成較小單位（稱為標記 tokens）的過程，使模型能理解和處理。
Instruction-Tuned LLMs：經過特定指令微調以提升回應準確性和相關性的指令調校大型語言模型（LLMs）。

## Learning Sandbox

提示工程目前更像是藝術而非科學。提升直覺的最佳方法是 _多加練習_，並採用結合應用領域專業知識、推薦技術與模型專屬優化的反覆試驗方法。

本課程附帶的 Jupyter 筆記本提供了一個 _沙盒_ 環境，讓你可以邊學邊試，或作為最後程式挑戰的一部分執行練習。執行練習需要：

1. **Azure OpenAI API 金鑰** — 已部署大型語言模型的服務端點。
2. **Python 執行環境** — 執行筆記本所需環境。
3. <strong>本機環境變數</strong> — _請現在完成 [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) 步驟以準備好_。

此筆記本附有 _入門_ 練習，但鼓勵你添加自己的 _Markdown_（說明）和 _Code_（提示請求）區段，試驗更多範例與想法，建立提示設計的直覺。

## Illustrated Guide

想在深入學習前先了解本課程涵蓋的整體架構？參考本插圖指南，幫助你掌握主要議題以及每個議題的重要思考重點。課程路線圖帶你從理解核心概念與挑戰，進而以相關提示工程技術和最佳實踐加以解決。請注意，本指南中「進階技術」部分涵蓋了本課程 _下一章_ 的內容。

![Illustrated Guide to Prompt Engineering](../../../translated_images/zh-MO/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Our Startup

現在，讓我們談談 _本主題_ 如何與我們創業公司的使命——[將 AI 創新帶入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) 相關。我們想建立強調 _個人化學習_ 的 AI 應用——所以讓我們思考不同用戶如何在我們的應用中「設計」提示：

- <strong>管理者</strong> 可能會請 AI _分析課程數據以識別覆蓋缺口_。AI 可以用程式碼總結結果或視覺化。
- <strong>教育者</strong> 可能會請 AI _為目標對象和主題生成授課計劃_。AI 可以用指定格式建立個人化計劃。
- <strong>學生</strong> 可能會請 AI _輔導他們學習困難科目_。AI 現在可以針對學生程度提供課程、提示和範例。

這只是冰山一角。請查閱 [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) ——由教育專家策劃的開源提示庫——以獲得更廣泛的可能性概念！_試試在沙盒或 OpenAI Playground 運行其中一些提示，看看會產生什麼效果！_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## What is Prompt Engineering?

我們一開始就將 <strong>提示工程</strong> 定義為為特定應用目標和模型 _設計和優化_ 文本輸入（提示）的過程，以交付穩定且高質量的回應（完成）。我們可以將其視為兩個步驟：

- 為特定模型和目標 _設計_ 初始提示
- 迭代 _優化_ 提示以提升回應品質

這必須採用反覆試驗的方式，依賴用戶的直覺與努力以達到最佳結果。那麼，為何如此重要？解答這個問題前，我們需要先理解三個概念：

- _Tokenization_ = 模型如何「看見」提示
- _Base LLMs_ = 基礎模型如何「處理」提示
- _Instruction-Tuned LLMs_ = 模型如何現在能「理解任務」

### Tokenization

大型語言模型將提示視為 _標記序列_，不同模型（或同一模型的不同版本）可能用不同方式對相同提示進行分詞。因為 LLM 是訓練在標記（tokens）上，而非原始文本，提示的分詞方式直接影響生成回應的品質。

想要直觀理解分詞運作，可嘗試使用如下的 [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) 工具。將你的提示複製到該工具，檢查它如何轉為標記，特別留意空白字元和標點符號的處理。注意此範例使用較舊的 LLM（GPT-3），嘗試新模型可能結果會不同。

![Tokenization](../../../translated_images/zh-MO/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concept: Foundation Models

一旦提示完成分詞，["基礎 LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)（或稱基礎模型）的主要功能是預測該序列中的下一個標記。LLM 在大量文本資料上訓練，因此能掌握標記間的統計關係，並較有信心地做出預測。請注意，模型並不「理解」提示中詞語的 _意義_；它只看到能「完成」的模式。它們會持續預測序列，直到用戶干預或符合預設條件終止。

想看提示基礎的完成如何運作？將上述提示輸入 Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)，保持預設設定。系統被配置為將提示視為資訊請求——你應該會看到符合情境的完成內容。

但如果用戶想看到符合特定標準或任務目標的回應呢？這時候就需要 _指令微調_ 的大型語言模型。

![Base LLM Chat Completion](../../../translated_images/zh-MO/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concept: Instruction Tuned LLMs

[指令微調 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) 是在基礎模型基礎上，使用示例或輸入/輸出對（例如多輪「訊息」）進行微調，這些示例包含明確指令——AI 回應會嘗試遵守該指令。

此過程使用如人類反饋強化學習（RLHF）等技術，訓練模型 _遵循指令_ 並 _從反饋中學習_，讓回應更適合實際應用且更貼近用戶目標。

來試試看——回到前面的提示，這次修改 _系統訊息_，提供如下指令作為上下文：

> _將所提供內容總結給二年級學生。結果保持一段話並附上3-5個重點項目。_

看看結果如何反映目標和格式？教育者現在可以直接將此回應用於該堂課的投影片。

![Instruction Tuned LLM Chat Completion](../../../translated_images/zh-MO/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Why do we need Prompt Engineering?

既然我們了解提示是如何被 LLM 處理的，讓我們談談 _為什麼_ 需要提示工程。原因在於目前的 LLM 存在許多挑戰，使得 _可靠且一致的完成結果_ 不易達成，除非投入提示構造和優化的努力。例如：

1. **模型回應具有隨機性。** _相同的提示_ 在不同模型或不同版本可能產生不同回應。甚至在 _同一模型_ 下多次輸入也可能產生不同結果。_提示工程技術能幫助我們透過設計更嚴謹的提示來減少這些變異_。

1. **模型可能會捏造回應。** 模型經預訓練於 _大量但有限_ 的資料集，意味著它缺乏訓練範圍之外的知識。因此，它可能產生不準確、虛構或與已知事實直接衝突的回應。_提示工程可幫助用戶識別並緩解這種捏造，例如要求 AI 提供引用或推理_。

1. **模型能力會有所不同。** 較新的模型或新版代會具有更豐富的能力，但也帶來獨特特性與在成本和複雜度上的權衡。_提示工程能幫助建立最佳實踐和工作流程，抽象差異並以可擴展且無縫的方式適應模型特定需求_。

讓我們在 OpenAI 或 Azure OpenAI Playground 中實際看看：

- 用相同提示測試不同 LLM 部署（如 OpenAI、Azure OpenAI、Hugging Face）——你有看到差異嗎？
- 用相同提示多次測試 _相同_ LLM 部署（例如 Azure OpenAI Playground）——這些變異如何不同？

### Fabrications Example

在本課程中，我們用 **「捏造」** 一詞指稱 LLM 由於其訓練限制或其他約束，有時會生成事實不正確資訊的現象。你可能在大眾文章或研究論文中聽過這被稱為 _「幻覺」_。然而，我們強烈建議使用 _「捏造」_ 這一術語，避免透過賦予機器人的行為類人特質來擬人化此現象。從術語角度來說，這也符合 [負責任 AI 指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) 的精神，剔除可能在某些情境中被視為冒犯或不包容的詞彙。

想要體會捏造是如何產生的？想像一個提示指示 AI 針對並不存在的主題生成內容（確保該主題未被訓練資料涵蓋）。例如——我嘗試使用以下提示：

> **Prompt:** generate a lesson plan on the Martian War of 2076.
一個網絡搜尋告訴我，有關火星戰爭的虛構故事（例如電視劇或書籍）——但沒有在2076年的。常識也告訴我們，2076年是在 _未來_，因此不可能與真實事件有關。

那麼當我們用不同的LLM供應商運行這個提示時會發生什麼？

> **回應 1**：OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/zh-MO/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **回應 2**：Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/zh-MO/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **回應 3**：：Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/zh-MO/04-fabrication-huggingchat.faf82a0a51278956.webp)

如預期，每個模型（或模型版本）因隨機性行為和模型能力差異而產生略有不同的回應。例如，一個模型面向8年級學生，而另一個則假設是高中學生。但三個模型都生成了可能令無知用戶相信該事件真實發生的回應。

提示工程技術如 _元提示_ 和 _溫度配置_ 可能在某種程度上減少模型虛構。新的提示工程 _架構_ 也將新工具和技術無縫整合到提示流程中，以減輕或減少其中一些影響。

## 案例研究：GitHub Copilot

讓我們通過一個案例研究來了解實際解決方案中如何使用提示工程：[GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot 是你的「AI 對題程式員」— 它將文本提示轉換為程式碼補全，並整合到你的開發環境（例如 Visual Studio Code）中，提供無縫的用戶體驗。正如下列博客系列所記錄的，最早版本基於 OpenAI Codex 模型——工程師很快意識到需要微調模型並開發更好的提示工程技術，以提升程式碼品質。今年7月，他們[推出了超越Codex的改進AI模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，提供更快的建議。

請按順序閱讀這些文章，跟隨它們的學習旅程。

- **2023年5月**｜[GitHub Copilot 正在變得更好理解你的程式碼](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月**｜[GitHub內部：與GitHub Copilot背後的LLMs合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023年6月**｜[如何為GitHub Copilot寫出更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023年7月**｜[.. GitHub Copilot 透過改進AI模型超越Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月**｜[開發者的提示工程和LLMs指南](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月**｜[如何構建企業級LLM應用：GitHub Copilot 的教訓](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

你也可以瀏覽他們的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)，閱讀更多像[這篇](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)的文章，展示這些模型和技術如何 _應用_ 於推動真實世界中的應用。

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

我們已經知道為什麼提示工程很重要——現在讓我們了解提示是如何 _構建_ 的，從而評估不同技術以設計更有效的提示。

### 基本提示

讓我們從基本提示開始：一個沒有其它上下文的文本輸入傳送給模型。以下是一個例子——當我們把美國國歌的開頭幾個字送到 OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)時，它會立即 _補全_ 接下來的幾句，展示基礎的預測行為。

| 提示（輸入）       | 補全（輸出）                                                                                                                          |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | 這聽起來像是在開始唱《星條旗永不落》（美國國歌）的歌詞。完整歌詞是...                                                                |

### 複雜提示

現在讓我們在基本提示中加入上下文和指示。[Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst)允許我們將複雜提示構建為一組 _訊息_：

- 輸入/輸出對，反映 _用戶_ 的輸入和 _助理_ 的回應。
- 系統訊息設置助理行為或性格的上下文。

請求現以如下形式，_標記化_ 有效捕捉來自上下文和對話的相關資訊。更改系統上下文就像更改用戶輸入一樣，對完成質量影響甚大。

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

在以上例子中，用戶提示是一個簡單的文本查詢，可解釋為資訊請求。透過 _指令_ 提示，我們可以用該文本詳細指定任務，給AI更好的指引。舉例如下：

| 提示（輸入）                                                                                                                                                                                                                           | 補全（輸出）                                                                                              | 指令類型         |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :--------------- |
| 寫一段南北戰爭的描述                                                                                                                                                                                                                   | _返回一段簡單的段落_                                                                                        | 簡單              |
| 寫一段南北戰爭的描述。提供關鍵日期和事件並描述其重要性                                                                                                                                                                                 | _返回一段文字，隨後列出關鍵事件日期及描述_                                                                   | 複雜              |
| 用一段話描述南北戰爭，提供3點關鍵日期及其重要性，另列3點重要歷史人物和其貢獻。輸出格式為JSON文件                                                                           | _返回較詳細文字內容，格式為可供複製貼上並驗證的JSON格式_                                                    | 複雜，有格式化      |

## 主要內容

在上述案例中，提示仍相當開放，讓LLM決定預訓練數據中哪些部份相關。使用 _主要內容_ 設計模式，輸入文本被分為兩部分：

- 指令（行動）
- 相關內容（影響該行動）

下面的例子中，指令是「用兩句話總結這段文字」。

| 提示（輸入）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 補全（輸出）                                                                                                                                                                                                                                                                       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 木星是距離太陽第五顆行星，也是太陽系中最大的行星。它是一顆氣體巨行星，質量是太陽的千分之一，但卻是太陽系中其他所有行星質量總和的兩倍半。木星是肉眼可見夜空中最亮的天體之一，早在記錄歷史之前就為古文明所知。它以羅馬神木星命名。[19] 從地球觀測時，木星反射的光亮度足以投射明顯的影子，[20] 平均來看，它是繼月亮和金星後夜空中第三亮的自然天體。<br/> <strong>請用兩句話簡短說明</strong> | 木星是距離太陽第五顆也是最大的一顆行星，夜空中最明亮的天體之一。它以羅馬神木星命名，是一顆氣體巨行星，質量是其他所有行星的兩倍半。                                                                                                                          |

主要內容段可用多種方式來驅動更有效的指令：

- <strong>範例</strong> — 不是透過明確指令告訴模型做什麼，而是給它想要的輸出範例，讓它推斷模式。
- <strong>提示信號</strong> — 在指令後附上一個「提示信號」，引導補全，引領模型產生更相關的回應。
- <strong>模板</strong> — 可重複使用的提示「配方」，包含可用資料自訂的佔位符（變量），用於特定用例。

我們來看看這些技術的實際運用。

### 使用範例

這是一種方法，利用主要內容「餵給模型」你期望的輸出範例，讓它推測所需輸出格式。根據範例數目不同，可分為零鏡頭、一鏡頭、多鏡頭提示。

提示包含三部分：

- 任務描述
- 幾個期望輸出範例
- 新範例的開始（隱含任務描述）

| 學習類型 | 提示（輸入）                                                                                                                                                 | 補全（輸出）               |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| 零鏡頭   | 「The Sun is Shining」。翻譯成西班牙語                                                                                                                      | 「El Sol está brillando」。  |
| 一鏡頭   | 「The Sun is Shining」 => 「El Sol está brillando」。<br>「It's a Cold and Windy Day」 =>                                                                      | 「Es un día frío y ventoso」。|
| 多鏡頭   | 球員跑壘 => 棒球<br/>球員發出ACE球 => 網球<br/>球員擊出六分 => 板球<br/>球員灌籃得分 =>                                                                       | 籃球                       |
|          |                                                                                                                                                             |                            |

你會注意到在零鏡頭提示中必須明確指示「Translate to Spanish」，但在一鏡頭提示範例中，該指示被隱含推斷出來。多鏡頭範例顯示，增加更多範例讓模型能更準確推斷，無需額外指令。

### 提示信號

另一種使用主要內容的技術是提供 _提示信號_ 而非範例。在這種情況下，我們透過 _啟動_ 一段反映期望回應格式的片段，給模型一個指引。模型隨後「接收提示信號」並繼續以相同方式生成。

| 提示信號數量 | 提示（輸入）                                                                                                                                                                                                                                                                                                                                                                                                                                             | 補全（輸出）                                                                                                                                                                                                                                                                                         |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0             | 木星是距離太陽第五顆行星，也是太陽系中最大的行星。它是一顆氣體巨行星，質量是太陽的千分之一，但卻是太陽系中其他所有行星質量總和的兩倍半。木星是肉眼可見夜空中最亮的天體之一，早在記錄歷史之前就為古文明所知。<br/><strong>請簡短總結這段文字</strong>                                                                                                                                    | 木星是太陽系中最大且距離太陽第五的行星。它是一顆氣體巨行星，質量是太陽的千分之一，但重於其他所有行星的總和。古代文明長期以來認識木星，且在夜空中容易看到。                                                                                                                                  |
| 1              | 木星是太陽系中距離太陽第五遠的行星，也是最大的行星。它是一顆氣體巨星，質量約為太陽的千分之一，但卻是太陽系其他所有行星質量總和的兩倍半。木星是夜空中用肉眼可見的最明亮天體之一，從有記錄的歷史之前就已為古代文明所知。<br/><strong>總結</strong><br/> 我們學到的是木星 | 是距離太陽第五遠的行星，也是太陽系中最大的。它是一顆氣體巨星，質量約為太陽的千分之一，但比其他所有行星總和的質量還要大兩倍半。它用肉眼很容易看見，自古以來就已為人所知。                        |
| 2              | 木星是太陽系中距離太陽第五遠的行星，也是最大的行星。它是一顆氣體巨星，質量約為太陽的千分之一，但卻是太陽系其他所有行星質量總和的兩倍半。木星是夜空中用肉眼可見的最明亮天體之一，從有記錄的歷史之前就已為古代文明所知。<br/><strong>總結</strong><br/> 我們學到的三大要點：         | 1. 木星是距離太陽第五遠的行星，也是太陽系中最大的。<br/> 2. 它是一顆氣體巨星，質量約為太陽的千分之一...<br/> 3. 木星自古以來就能用肉眼看見...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

提示模板是一個_預先定義的提示配方_，可儲存及重用以推動更一致的用戶體驗。在最簡單的形式中，它僅僅是一組提示範例，例如[這個來自OpenAI的範例](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst)，同時提供互動式的提示組件（用戶與系統訊息）和API驅動的請求格式——以支持重用。

在更複雜的形式如[這個來自LangChain的範例](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst)中，它包含_占位符_，可用來根據來自多種來源的資料（用戶輸入、系統上下文、外部資料來源等等）動態生成提示。這讓我們可以創建可重用提示庫，用於<strong>程式化</strong>地在規模上推動一致的用戶體驗。

最後，模板的真正價值在於創建並發布垂直應用領域的_提示庫_——提示模板現已_優化_，反映特定應用背景或示例，使回答更加符合目標用戶群體需求。像[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)倉庫，就是此類方法的優秀例子，策劃了面向教育領域的提示庫，強調課程規劃、課綱設計、學生輔導等核心目標。

## Supporting Content

如果把提示建構看作包含說明（任務）和目標（主內容），那麼_次要內容_就像是我們提供的額外背景，用以<strong>某種方式影響輸出</strong>。它可能是調整參數、格式指令、主題分類等，可幫助模型_調整響應_以符合所需的用戶目標或期望。

例如：給定一份包含豐富元資料（名稱、描述、等級、元資料標籤、講師等）的課程目錄：

- 我們可定義說明「為2023秋季學期總結課程目錄」
- 我們可使用主內容提供所需輸出格式的幾個示例
- 我們可用次要內容標示關注度最高的5個「標籤」

現在，模型能夠以範例中展示的格式產生摘要，但若結果具有多個標籤，可以優先著重於次要內容中標示的5個標籤。

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

## 提示工程最佳實務

既然我們知道如何_構建_提示，我們可以開始思考如何_設計_提示來反映最佳實務。這可分為兩部分：擁有正確的_心態_以及運用適當的_技巧_。

### 提示工程心態

提示工程是一個試錯過程，請記住三個廣泛的指導因素：

1. **領域理解很重要。** 回應的準確性和相關性取決於應用或用戶操作的_領域_。運用你的直覺和領域專長來<strong>進一步定制技術</strong>。例如，在系統提示中定義_特定領域的人格_，或在用戶提示中使用_特定領域的模板_。提供反映領域特定上下文的次要內容，或使用_特定領域的提示和示例_以引導模型朝熟悉的使用模式回應。

2. **對模型的理解很重要。** 我們知道模型本質上帶有隨機性。但模型的實作也會因使用的訓練資料集（預訓知識）、所提供的能力（例如透過API或SDK）和優化的內容類型（例如程式碼、圖像或文本）而異。理解你所用模型的優劣，並利用此知識_優先排序任務_或建立為該模型能力優化的_自訂模板_。

3. **迭代與驗證很重要。** 模型快速演進，提示工程技巧亦然。作為領域專家，你可能有其它特定於你應用的背景或標準，未必適用於更廣泛社群。利用提示工程工具與技巧「起步」建構提示，接著用你的直覺和專業知識迭代與驗證結果。記錄心得並建立<strong>知識庫</strong>（例如提示庫），供他人作為更快迭代的新基線。

## 最佳實務

現在來看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)及[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)實務者推薦的通用最佳實務。

| 什麼                              | 為什麼                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 評估最新模型                    | 新一代模型多半擁有改進的功能和品質，但可能也帶來較高成本。請評估其影響後再決定是否遷移。                                                                                                                                |
| 分離指令與上下文               | 檢查你的模型/服務提供者是否定義_分隔符_用以更清晰區分指令、主內容與次要內容。這有助模型更精確地賦予權重給詞元。                                                                                              |
| 具體而清晰                     | 詳細說明期望的上下文、結果、長度、格式、風格等，提升回答的品質與一致性。將配方記錄在可重用的模板中。                                                                                           |
| 具描述性，使用示例             | 模型可能較好回應「展示與說明」的方式。可先用「零樣本」（zero-shot）給指令（無示例），再用「少樣本」（few-shot）以少數示例細化，使用類比等。                                                      |
| 使用提示引導完成               | 透過提供一些引導詞或短語，促使模型以此作為開始點，推向所需結果。                                                                                                                              |
| 重複強調                       | 有時你需要對模型重複指令。可在主內容之前及之後給指令，使用指令與引導搭配等。反覆嘗試並驗證什麼有效。                                                                                                  |
| 順序很重要                     | 向模型呈現資訊的順序可能影響輸出，甚至在示例教學中，因為有回顧偏向。嘗試不同方式看哪個效果最好。                                                                                                      |
| 給模型“出路”                   | 提供模型一個_備用_完成響應，以防它因任何原因無法完成任務。這可減少模型產生錯誤或捏造回答的機率。                                                                                                       |
|                                   |                                                                                                                                                                                                                                                   |

如同任何最佳實務，請記得根據模型、任務與領域_實際情況可能有所不同_。將這些作為起點，透過迭代找出最適合你的方法。當新模型與工具問世時，持續重新評估提示工程流程，聚焦流程可擴展性與回答品質。

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## 任務

恭喜你完成本課程！是時候用真實範例檢驗你學到的概念與技巧了！

這次的任務將使用 Jupyter Notebook，內含你可互動完成的練習。你也可以添加自己的 Markdown 與程式碼單元，以自行探索想法與技巧。

### 開始前，請先分支本倉庫，然後

- （推薦）啟動 GitHub Codespaces
- （替代）克隆本倉庫到本地並使用 Docker Desktop
- （替代）用你慣用的 Notebook 運行環境打開 Notebook

### 接著，配置環境變量

- 複製倉庫根目錄的 `.env.copy` 為 `.env`，填入 `AZURE_OPENAI_API_KEY`、`AZURE_OPENAI_ENDPOINT` 與 `AZURE_OPENAI_DEPLOYMENT`。完成後請返回[學習沙箱區](#learning-sandbox)了解詳細操作。

### 然後，打開 Jupyter Notebook

- 選擇運行核心。如果使用方案1或2，只需使用開發容器預設提供的 Python 3.10.x 內核即可。

你就可以開始執行練習。請注意，這裡不存在「對錯」答案——重點是透過試錯探索選項，並累積對特定模型與應用領域的理解。

_因此本課程不提供程式碼解答區段，Notebook 裡以標題為「我的解答：」的 Markdown 單元展示一個參考範例輸出。_

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## 知識檢核

以下哪個提示較符合合理的最佳實務？

1. 給我一張紅色汽車的圖片
2. 給我一張紅色 Volvo XC90 停在懸崖旁夕陽景色的汽車圖片
3. 給我一張紅色 Volvo XC90 汽車圖片

A: 2，是最佳提示，因為詳細描述了「什麼」且具體說明（不只是任意汽車，而是特定品牌和型號），並描述整體場景。3最差，因為描述較少。

## 🚀 挑戰

試試看用提示技巧「引導」完成句子「給我一張紅色 Volvo 汽車的…」，看看模型回應什麼？你會如何改進？

## 做得好！繼續學習

想了解更多提示工程概念？前往[持續學習頁面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)探索其他優質資源。

接著來第5課，我們將探討[進階提示技巧](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->