# 探索與比較不同的大型語言模型

[![探索與比較不同的大型語言模型](../../../translated_images/zh-TW/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _點擊上方圖片觀看本課程影片_

在上一課中，我們已經了解生成式 AI 如何改變技術環境，大型語言模型 (LLM) 的工作原理，以及像我們的創業公司這樣的企業如何將其應用於使用案例並成長！本章將比較與對照不同類型的大型語言模型，了解它們的優缺點。

我們創業之旅的下一步是探索現有的 LLM 生態並了解哪些適合我們的使用案例。

## 介紹

本課程將涵蓋：

- 目前生態中不同類型的 LLM。
- 如何在 Azure 中測試、迭代並比較不同模型以符合您的使用案例。
- 如何部署 LLM。

## 學習目標

完成本課程後，您將能夠：

- 為您的使用案例選擇合適的模型。
- 了解如何測試、迭代並提升模型性能。
- 了解企業如何部署模型。

## 理解不同類型的 LLM

LLM 可依據其架構、訓練資料和使用案例進行多重分類。瞭解這些差異將幫助我們的創業公司選擇適合情境的模型，並了解如何測試、迭代與提升表現。

LLM 有許多不同種類，您選擇的模型取決於您想用它們做什麼、您的資料、您願意支付多少費用等等。

根據您想利用模型產生文字、音訊、影片、圖像等，您可能會選擇不同類型的模型。

- <strong>音訊及語音辨識</strong>。Whisper 風格模型仍是實用的通用語音辨識模型，但業界選項也包括更新的語音轉文字模型，如 `gpt-4o-transcribe`、`gpt-4o-mini-transcribe`，以及說話人分離變體。請依您的情境評估語言覆蓋度、說話人分離、即時支援、延遲及成本。詳見 [OpenAI 語音轉文字文件](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst)。

- <strong>圖像生成</strong>。DALL-E 與 Midjourney 是知名的圖像生成選項，但目前 OpenAI 圖像 API 以 `gpt-image-2` 等 GPT 影像模型為中心，而 Stable Diffusion、Imagen、Flux 及其他模型家族也常見。您可比較提示遵循度、編輯支援、風格控制、安全要求及授權。詳情見 [OpenAI 圖像生成指南](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) 及本課程第 9 章。

- <strong>文字生成</strong>。文字模型涵蓋尖端模型、推理模型、小型低延遲模型及開放權重模型。目前範例有 OpenAI GPT-5.x、Anthropic Claude 4.x、Google Gemini 3.x、Meta Llama 4 及 Mistral 模型。不要僅以發布日期或價格選擇；請比較任務品質、延遲、上下文視窗、工具使用、安全行為、區域可用性及總成本。可於 [Microsoft Foundry 模型目錄](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) 比較可在 Azure 使用的模型。

- <strong>多模態</strong>。許多現有模型能處理不只是文字，有的接受圖像、音訊或影片輸入，有的能調用工具，專用模型能生成圖像、音訊或影片。例如，目前 OpenAI 模型支援文字與圖像輸入，Gemini 模型視變體不同可支援文字、程式碼、圖像、音訊、影片輸入，Llama 4 Scout 與 Maverick 是開放權重的原生多模態模型。建構工作流程前，請查看各模型卡以確認支援的輸入與輸出模式。

選擇模型代表您將獲得基本功能，但可能不夠用。通常，您還有公司特定資料必須以某種方式讓 LLM 知道。採取這類做法有幾種選項，將於接下來章節介紹。

### 基礎模型與 LLM

基礎模型一詞由 [史丹佛研究人員創造](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)，定義為符合某些標準的 AI 模型，例如：

- <strong>它們透過無監督學習或自我監督學習訓練</strong>，意即訓練時使用未標記多模態資料，且不需人工標註。
- <strong>它們是非常大型的模型</strong>，根據具有數十億參數的深度神經網絡訓練。
- **通常用作其他模型的“基礎”**，可作為其他模型訓練的起點，透過微調打造更專精的模型。

![基礎模型與 LLM](../../../translated_images/zh-TW/FoundationModel.e4859dbb7a825c94.webp)

圖片來源：[Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

為進一步說明這區別，以 ChatGPT 為歷史案例。ChatGPT 早期版本以 GPT-3.5 作為基礎模型，OpenAI 透過對話特定資料與對齊技術創建調整版本，使在對話場景（如聊天機器人）表現更佳。現代 AI 服務常在多個模型變體間路由，因此服務名稱與底層模型名稱未必相同。

![基礎模型](../../../translated_images/zh-TW/Multimodal.2c389c6439e0fc51.webp)

圖片來源：[2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 開放權重／開源模型與專有模型

另一種分法是模型是否開放權重、開源或專有。

開源與開放權重模型會提供模型資源以供檢視、下載或客製化，但授權有所不同。有些是完全開源，有些則是有限使用的開放權重模型。當企業需要更高的部署、資料位置、成本控管或個性化掌控時非常有用。但團隊仍須審查授權條款、服務成本、維護、安全更新及評估品質後才能用於生產環境。範例包括 [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst)、部分 [Mistral 模型](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst)、以及許多托管於 [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst) 的模型。

專有模型由提供者持有並托管。這些模型通常為生產用優化，可提供強有力的支援、安全機制、工具整合及擴展性。但客戶通常無法檢查或修改模型權重，且須審查服務提供者的隱私、資料保存、合規性及合理使用條款。範例包括 [OpenAI 模型](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)、[Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) 及 [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst)。

### 嵌入式模型、圖像生成與文字及程式碼生成

依輸出形式，LLM 還可分類。

嵌入式模型是一組可以將文字轉成數值型態（稱為嵌入向量）的模型，這是輸入文字的數值表示。嵌入式讓機器更容易理解字詞或句子間的關係，可作為其他模型的輸入，如分類模型或在數值資料上效能更佳的聚類模型。嵌入式模型常用於遷移學習，先為資料豐富的代理任務訓練模型，然後重用模型權重（嵌入向量）於其他下游任務。此類範例為 [OpenAI 嵌入模型](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)。

![嵌入式](../../../translated_images/zh-TW/Embedding.c3708fe988ccf760.webp)

圖像生成模型能創造圖片，應用於圖片編輯、合成及翻譯。這些模型通常於大型圖片資料集訓練，如 [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)，可用於生成新圖像或使用修補、超解析度、著色技術編輯現有圖像。範例包含 [GPT 影像模型](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst)、[Stable Diffusion 模型](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) 及 Imagen 模型。

![圖像生成](../../../translated_images/zh-TW/Image.349c080266a763fd.webp)

文字及程式碼生成模型能產生文字或程式碼，應用於文字摘要、翻譯及問答。文字生成模型通常於大量文字資料集訓練，如 [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst)，可用於產生新文字或回答問題。程式碼生成模型，如 [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)，通常於大量程式碼資料集（如 GitHub）訓練，用於生成新程式碼或修正既有程式碼錯誤。

![文字及程式碼生成](../../../translated_images/zh-TW/Text.a8c0cf139e5cc2a0.webp)

### 編碼器-解碼器模型與僅解碼器模型

談論 LLM 架構類型時，讓我們用比喻說明。

假設您的主管派您一個任務，為學生設計一份小測驗。您有兩位同事，一位負責創作題目內容，另一位負責審核。

創作者就像僅解碼器模型：能看到主題及您已寫的內容，然後依此上下文繼續生成文本。他們非常擅長撰寫引人入勝且有資訊性的內容，但若任務只是分類、檢索或編碼資料，他們不一定是最佳選擇。僅解碼器模型的範例有 GPT 和 Llama 模型。

審核者則像僅編碼器模型，他們審視已寫課程及答案，察覺其關聯並理解上下文，但不擅長產出內容。BERT 是僅編碼器模型範例。

想像有一人既能創作又能審核小測驗，這就是編碼器-解碼器模型。範例包括 BART 與 T5。

### 服務與模型的差異

現在來談談服務與模型的不同。服務是雲端服務提供者提供的產品，通常是模型、資料與其他元件的組合。模型是服務的核心元件，通常是基礎模型，例如 LLM。

服務通常優化為生產使用，且比模型更容易使用，常由圖形操作介面提供。不過服務不一定免費，可能需訂閱或付費，換取使用服務擁有者的設備與資源，優化支出並輕鬆擴展。服務範例有 [Azure OpenAI 服務](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst)，提供隨用隨付的收費方案，依使用量收費。Azure OpenAI 服務還在模型功能上層提供企業級安全與負責任 AI 框架。

模型是神經網絡的構件：參數、權重、架構、分詞器和支援配置。要在本地或私有環境執行模型，需要合適硬體、服務基礎設施、監控，且需相容的開源／開權授權或商業授權。開權模型如 Llama 4 或 Mistral 模型可自托管，但仍需計算資源及運營專業知識。

## 如何在 Azure 上測試並迭代不同模型以瞭解性能


一旦我們的團隊探索了當前的 LLMs 生態並為他們的場景識別出一些不錯的候選模型，下一步就是在他們的數據和工作負載上測試這些模型。這是一個透過實驗和測量反覆進行的過程。 
我們在前面的段落中提到的大多數模型（OpenAI 模型、開放權重模型如 Llama 4 和 Mistral，以及 Hugging Face 模型）都可以在 [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) 中找到。

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst)（前身為 Azure AI Studio/Azure AI Foundry）是一個統一的 Azure 平台，用於構建 AI 應用程式和代理。它幫助開發人員管理從實驗、評估到部署、監控和治理的生命週期。Microsoft Foundry 中的模型目錄使用戶能夠：

- 在目錄中找到感興趣的基礎模型，包括 Azure 銷售的模型以及合作夥伴和社區提供的模型。用戶可以按任務、提供者、授權、部署選項或名稱過濾。

![Model catalog](../../../translated_images/zh-TW/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- 查看模型卡，包括對預期用途和訓練數據的詳細描述、程式碼範例以及內部評估庫中的評估結果。

![Model card](../../../translated_images/zh-TW/ModelCard.598051692c6e400d.webp)

- 通過[模型基準](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst)面板，比較行業中可用的模型和數據集的基準，評估哪個模型符合業務場景需求。

![Model benchmarks](../../../translated_images/zh-TW/ModelBenchmarks.254cb20fbd06c03a.webp)

- 利用 Microsoft Foundry 的實驗和追蹤功能，在自訂訓練數據上微調支持的模型，以提升模型在特定工作負載上的性能。

![Model fine-tuning](../../../translated_images/zh-TW/FineTuning.aac48f07142e36fd.webp)

- 將原版預訓練模型或微調版本部署到遠端的即時推論端點，使用受管計算或無伺服器部署選項，讓應用程式能夠使用它。

![Model deployment](../../../translated_images/zh-TW/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> 目前目錄中的所有模型並非全部均可進行微調和/或按需付費部署。請查看模型卡以了解模型功能和限制的詳細資訊。

## 改善 LLM 結果

我們與創業團隊一起探索了各種 LLMs 以及一個雲平台（Microsoft Foundry），該平台使我們能比較不同模型、在測試數據上評估它們、提升性能並部署到推論端點。

但他們什麼時候應該考慮微調模型，而不是使用預訓練模型？是否還有其他方法可以提升模型在特定工作負載上的性能？

企業可以使用多種方法從 LLMs 獲得所需結果。部署 LLM 時可選擇不同類型的模型，訓練階段程度不同，具不同複雜度、成本和品質。這裡有一些不同的做法：

- <strong>帶有上下文的提示工程</strong>。其想法是，在提示時提供足夠上下文以確保能獲得所需回答。

- **檢索增強生成 (Retrieval Augmented Generation, RAG)**。例如您的數據可能存於資料庫或網頁端點，為確保在提示時包含這些或其中部分數據，可以檢索相關數據並將其作為用戶提示的一部分。

- <strong>微調模型</strong>。這裡您在自己的數據上進一步訓練模型，使模型更精確、更能回應需求，但可能成本較高。

![LLMs deployment](../../../translated_images/zh-TW/Deploy.18b2d27412ec8c02.webp)

圖片來源: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 帶有上下文的提示工程

預訓練的 LLMs 在廣義的自然語言任務上表現良好，即使僅用一個簡短的提示，如一個句子補全或一個問題，也就是所謂的“零次學習”。

然而，用戶越能詳細構造查詢，包括詳細請求和範例——即上下文——答案就越準確且符合用戶期望。如果提示中只包含一個範例，稱為「一步學習」，若包含多個範例，稱為「少步學習」。
帶有上下文的提示工程是最具成本效益的起步方法。

### 檢索增強生成（RAG）

LLMs 有其限制，即只能使用訓練期間使用的數據來生成答案。這意味著它們不知道訓練後發生的事實，也無法訪問非公開資訊（如公司數據）。
這可透過 RAG 技術克服，該技術以文件切片形式用外部數據增強提示，考慮提示長度限制。向量資料庫工具（如 [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)）支援此技術，可從多種預定義數據源檢索有用片段並加入提示上下文。

當企業缺乏足夠數據、時間或資源微調 LLM，但仍希望在特定工作負載上改善性能並降低幻覺、過時或不支持答案的風險時，此技術非常有用。

### 微調模型

微調利用遷移學習來‘調整’模型以適用下游任務或解決特定問題。不同於少步學習和 RAG，微調會產生一個新的模型，包含更新的權重和偏差。需要一組訓練範例，每個範例包含一個輸入（提示）及其對應輸出（補全）。
下列情況偏好此方法：

- <strong>使用較小的任務專用模型</strong>。企業希望微調較小模型以應對特定狹義任務，而非反覆調用較大邊界模型，這樣更具成本效益且更快速。

- <strong>考慮延遲</strong>。在特定用例中延遲很重要，因此無法使用過長提示，或者學習範例數量不符合提示長度限制。

- <strong>適應穩定行為</strong>。企業擁有大量高品質範例，期望模型始終遵循任務模式、輸出格式、語氣或特定領域風格。如果主要問題是經常變動的新事實或私有知識，應使用 RAG，而非僅依賴微調。

### 訓練模型

從頭訓練 LLM 無疑是最困難且最複雜的方法，需要大量數據、專業資源和合適的計算能力。此選項應僅在企業有領域專用用例和大量領域中心數據情況下考慮。

## 知識檢查

改善 LLM 補全結果的一個好方法是什麼？

1. 帶有上下文的提示工程
1. 檢索增強生成 (RAG)
1. 微調模型

答：這三種方法都有效。可從提示工程和上下文著手快速改善，當模型需要最新事實或私有業務數據時使用 RAG。若有足夠高品質範例且需要模型持續遵循任務、格式、語氣或領域模式，則選擇微調。

## 🚀 挑戰

深入閱讀如何為您的業務[使用 RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)。

## 很棒的工作，繼續學習吧

完成本課程後，查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

前往第三課，我們將探討如何[負責任地構建生成式 AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->