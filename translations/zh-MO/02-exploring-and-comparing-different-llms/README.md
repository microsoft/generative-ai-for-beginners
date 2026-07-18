# 探索與比較不同的 LLM

[![探索與比較不同的 LLM](../../../translated_images/zh-MO/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _點擊上方圖片觀看本課程的影片_

透過上一課程，我們已了解生成式 AI 如何改變科技格局，知曉大型語言模型（LLMs）的運作方式，以及像我們這樣的創業公司如何應用它們在實際案例中並成長！本章節將比較和對照不同類型的大型語言模型 (LLMs)，以了解它們的優缺點。

我們創業旅程的下一步是探索當前 LLM 的現況，並瞭解哪些適合我們的使用案例。

## 介紹

本課程將涵蓋：

- 目前市場中不同類型的 LLM。
- 在 Azure 上針對您的使用案例測試、迭代及比較不同模型。
- 如何部署 LLM。

## 學習目標

完成本課程後，您將能：

- 選擇適合您使用案例的模型。
- 理解如何測試、迭代並提升模型效能。
- 了解企業如何部署模型。

## 了解不同類型的 LLM

LLM 可依其架構、訓練資料與應用案例進行多種分類。理解這些差異將幫助我們創業公司選擇適合情境的模型，並了解到如何測試、迭代及提升效能。

市面上有許多不同類型的 LLM 模型，您選擇哪個模型取決於您的使用目的、資料、預算等多種因素。

依據您是計畫將模型用於文字、音訊、影片、圖片產生等不同應用，您可能會選擇不同種類的模型。

- <strong>音訊與語音辨識</strong>。Whisper 類模型仍是通用的語音辨識模型，但實務上也會用到如 `gpt-4o-transcribe`、`gpt-4o-mini-transcribe` 以及分割說話者變體等較新語音轉文字模型。請根據您的情境評估語言覆蓋度、說話者分離、即時支援、延遲及成本。詳見 [OpenAI 語音轉文字文件](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst)。

- <strong>圖片生成</strong>。DALL-E 與 Midjourney 是知名的圖片生成選項，但現有 OpenAI 影像 API 主要聚焦 GPT 影像模型如 `gpt-image-2`，而 Stable Diffusion、Imagen、Flux 及其他模型系列也是常見選擇。請比較提示遵從度、編輯支援、風格控制、安全要求及授權狀況。詳見 [OpenAI 圖片生成指南](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) 及本課程第 9 章。

- <strong>文字生成</strong>。文字模型涵蓋尖端模型、推理模型、小型低延遲模型及開放權重模型。目前例子有 OpenAI GPT-5.x 系列、Anthropic Claude 4.x 系列、Google Gemini 3.x 系列、Meta Llama 4 及 Mistral 模型。切勿只根據發佈日期或價格選擇；應比較任務品質、延遲、上下文視窗、工具使用、安全行為、區域可用性及總成本。可參考 [Microsoft Foundry 模型目錄](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) 來比較 Azure 上的模型。

- <strong>多模態</strong>。許多當前模型可處理不只文字，有的支援圖片、音訊或影片輸入，部分還能呼叫工具，專門模型則可生成圖片、音訊或影片。例如，現在的 OpenAI 模型支援文字與圖片輸入，Gemini 依版本可支持文字、程式碼、圖片、音訊與影片輸入，Llama 4 Scout 與 Maverick 是開放權重且天生的多模態模型。建立流程前，務必查閱每個模型卡的支援輸入與輸出形式。

選擇模型意味著您將取得某些基本能力，但可能不足夠。通常您有公司專屬資料須向 LLM 說明，對此有幾種方法，後續章節會詳述。

### 基礎模型與 LLM 之別

「基礎模型」（Foundation Model）一詞由斯坦福研究人員提出並定義為符合數項條件的 AI 模型，例如：

- <strong>透過無監督或自監督學習訓練</strong>，意味著模型基於未標記的多模態資料訓練，不需人為標註數據。
- <strong>是非常大規模的模型</strong>，建立於訓練數十億參數的深度神經網絡上。
- **通常用作其他模型的「基礎」**，意指可作為其他模型開發的起點，透過微調進行優化。

![基礎模型與 LLM](../../../translated_images/zh-MO/FoundationModel.e4859dbb7a825c94.webp)

圖片來源：[Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

為了進一步說明此區別，讓我們以 ChatGPT 作為歷史範例。早期版本 ChatGPT 使用 GPT-3.5 作為基礎模型，OpenAI 利用聊天特定的資料及調整手法，打造出在對話場景（如聊天機器人）表現更佳的調校版本。現代 AI 服務通常會在多種模型變體間切換，因此服務名稱與底層模型名稱並不總是一致。

![基礎模型](../../../translated_images/zh-MO/Multimodal.2c389c6439e0fc51.webp)

圖片來源：[2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 開放權重/開源與專有模型

另一種區分 LLM 的方法是是否屬於開放權重、開源或專有模型。

開源及開放權重模型的模型工件可供檢視、下載或客製，而其許可有所不同，有些為完全開源，有些為附限制使用的開放權重模型。企業需要更嚴格掌控部署、資料存放、成本及客製化時，這類模型很有用。但使用前仍需審視授權條款、服務成本、維護、安全更新及評估品質。例子有 [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst)、部分 [Mistral 模型](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst)、及許多存在於 [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst) 的模型。

專有模型由提供者擁有並主機管理，通常為管理式生產環境所優化，可提供強大的支援、安全系統、工具整合與擴展性。但用戶一般無法檢視或修改模型權重，且需審慎檢視提供者於隱私、資料保留、遵規及使用規範的約定。例子包括 [OpenAI 模型](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)、[Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) 及 [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst)。

### Embedding 與圖片生成及文字與程式碼生成

LLM 也可依輸出類型分類。

Embedding 是一種將文字轉換成數字形式的模型稱為嵌入向量，能數字化表示輸入的文字。Embedding 有助機器理解詞彙或句子之間的關係，也可作為其他模型的輸入，如分類模型、聚類模型等，在數字資料上表現更佳。嵌入模型常用於遷移學習，先建立一個有大量資料的替代任務模型，再重用模型權重（即嵌入）於下游任務。此類模型例子有 [OpenAI 嵌入](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)。

![嵌入](../../../translated_images/zh-MO/Embedding.c3708fe988ccf760.webp)

圖片生成模型是生成圖片的模型。此類模型通常用於圖片編輯、合成與轉換，基於大型圖片數據集訓練，如 [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)，能生成新圖片或利用修補、超解析與著色等技術編輯既有圖片。例子包括 [GPT 影像模型](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst)、[Stable Diffusion 模型](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) 及 Imagen 模型。

![圖片生成](../../../translated_images/zh-MO/Image.349c080266a763fd.webp)

文字與程式碼生成模型則用於生成文字或程式碼。此類模型常用於文字摘要、翻譯、問答等任務。文字生成模型訓練於大型文字資料集，如 [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst)，能生成新文字或回答問題。程式碼生成模型，如 [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)，訓練於大型程式碼資料集（如 GitHub），可用於生成新程式碼或修復現有程式碼錯誤。

![文字與程式碼生成](../../../translated_images/zh-MO/Text.a8c0cf139e5cc2a0.webp)

### 編碼器-解碼器 與 只有解碼器

談及 LLM 架構類型時，讓我們用比喻說明。

假設您的主管交給您一項任務，要為學生撰寫小測驗。您有兩位同事，一個負責製作內容，另一個負責審核內容。

內容製作人如同只有解碼器模型：他們能針對主題和已寫好的資料，繼續生成內容。他們善於撰寫具吸引力且資訊豐富的內容，但若任務僅是分類、檢索或編碼資訊時，未必是最佳選擇。例子有 GPT 與 Llama 模型系列。

審核者如同只有編碼器模型，他們會查看撰寫的課程內容與答案，理解它們之間的關係與上下文，卻不擅長生成內容。BERT 就是只有編碼器的模型。

假設我們還有一位既能創建又能審核的小測驗的同事，那便是編碼器-解碼器模型。例子有 BART 和 T5。

### 服務 與 模型

接著，聊聊服務與模型的差異。服務是一種由雲端服務商提供的產品，往往結合多個模型、資料及其他元件。模型則是服務的核心組件，通常為基礎模型，如 LLM。

服務通常針對生產用途優化，且透過圖形用戶介面比模型更易使用。但服務不一定免費，可能需訂閱或付費，讓用戶能利用服務營運者的設備及資源，達到費用最適化與彈性擴充。服務範例是 [Azure OpenAI 服務](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst)，其採用用量付費模式，意即依使用量比例收費，並提供企業級安全與負責任 AI 框架。

模型則指神經網絡工件：參數、權重、架構、分詞器與相關設定。若在本地或私有環境部署模型，需具備適當硬體、服務基建、監控，及符合的開源/開放權重許可或商業許可。開放權重模型如 Llama 4 或 Mistral 模型可自我托管，但仍需計算資源與營運專業知識。

## 如何在 Azure 測試與迭代不同模型以了解效能


當我們的團隊探索了目前的 LLM 生態並為他們的場景找出一些合適的候選模型後，下一步是用他們的數據和工作負載進行測試。這是一個通過實驗和測量進行的迭代過程。
我們在前面段落中提到的大多數模型（OpenAI 模型、開放權重模型如 Llama 4 和 Mistral 以及 Hugging Face 模型）都可在 [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) 中使用。

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst)，前稱 Azure AI Studio/Azure AI Foundry，是一個統一的 Azure 平台，用於構建 AI 應用程式和代理。它幫助開發者管理從實驗與評估到部署、監控和治理的整個生命週期。Microsoft Foundry 中的模型目錄使用戶能夠：

- 在目錄中找到感興趣的基礎模型，包括由 Azure 販售的模型以及合作夥伴和社群供應商的模型。用戶可以按任務、供應商、許可、部署選項或名稱篩選。

![Model catalog](../../../translated_images/zh-MO/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- 查看模型卡，包含對預期用途和訓練數據的詳細說明、程式碼範例以及內部評估庫的評估結果。

![Model card](../../../translated_images/zh-MO/ModelCard.598051692c6e400d.webp)

- 比較產業中可用模型和數據集的基準，以評估哪個符合業務場景，藉由 [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst) 面板實現。

![Model benchmarks](../../../translated_images/zh-MO/ModelBenchmarks.254cb20fbd06c03a.webp)

- 對支援的模型在自訂訓練數據上進行微調，以提升模型在特定工作負載的效能，利用 Microsoft Foundry 的實驗和追蹤功能。

![Model fine-tuning](../../../translated_images/zh-MO/FineTuning.aac48f07142e36fd.webp)

- 將原始預訓練模型或微調版本部署到遠端即時推論端點，使用受管運算或無伺服器部署選項，讓應用程式可以使用它。

![Model deployment](../../../translated_images/zh-MO/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> 目錄中的所有模型並非全部目前都支持微調和/或隨用隨付部署。請查閱模型卡瞭解該模型的功能和限制細節。

## 改善 LLM 結果

我們與新創團隊探索了不同類型的 LLM 以及一個雲端平台（Microsoft Foundry），它使我們能比較不同模型，評估測試數據上的效能，提升表現，並將其部署在推論端點。

但什麼時候應該考慮微調模型而非直接使用預訓練模型？還有什麼其他方法可以改善模型在特定工作負載的效能？

業務可採用多種方法從 LLM 獲取所需結果。部署 LLM 時，可以選擇不同類型的模型，訓練程度各異，具不同的複雜度、成本與質量。以下是一些不同的方法：

- <strong>帶有上下文的提示工程</strong>。概念是當你輸入提示時提供足夠的上下文，以保證獲得所需的回應。

- **檢索增強生成，RAG**。你的數據可能存在資料庫或網路端點中，為確保在提示時包含該數據或其子集，可以檢索相關數據並將其作為使用者提示的一部分。

- <strong>微調模型</strong>。此方式是在你的數據上進行進一步訓練，使模型更精確且更符合你的需求，但成本可能較高。

![LLMs deployment](../../../translated_images/zh-MO/Deploy.18b2d27412ec8c02.webp)

圖片來源: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 帶有上下文的提示工程

預訓練的 LLM 在一般自然語言任務中表現非常好，即使只是給一個簡短提示，如完成句子或提問 —— 所謂的“零樣本”（zero-shot）學習。

但用戶越能用詳細的請求和示例——上下文——來框定查詢，答案就越精確並越符合用戶預期。如果提示只包含一個示例，稱為“一樣本”學習（one-shot），包含多個示例則稱“少樣本”學習（few-shot）。
帶有上下文的提示工程是最具成本效益的起步方法。

### 檢索增強生成（RAG）

LLM 有個限制，只能用訓練期間使用過的數據來生成答案。這代表它們不知道訓練結束後發生的事實且無法存取非公開資訊（如公司資料）。
這可透過 RAG 克服，RAG 是一種在提示中附加外部數據片段的技術，同時考量提示長度限制。由向量資料庫工具（如 [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)）支援，從多個預定義資料來源檢索有用的數據片段並加入提示的上下文中。

當企業沒有足夠數據、時間或資源去微調 LLM，但仍希望提升特定工作負載的效能、降低虛構、過時或無支持答案的風險時，此技術非常實用。

### 微調模型

微調是一種利用轉移學習將模型「調整」到下游任務或解決特定問題的過程。與少樣本學習和 RAG 不同，微調會生成新的模型，具有更新的權重與偏差。它需要一組訓練範例，包括輸入（提示）和相關聯的輸出（完成）。
如果：

- <strong>使用較小且專門的任務模型</strong>。業務希望微調較小的模型來執行狹窄任務，而非反覆提示更大且最先進的模型，以達成更具成本效益且更快的方案。

- <strong>考慮延遲時間</strong>。某些用例對延遲重要，無法使用非常長的提示，或模型需學習的示例數不符合提示長度限制。

- <strong>調整穩定行為</strong>。業務有許多高品質範例，期望模型持續遵循任務模式、輸出格式、語調或領域特定風格。如果主要問題是頻繁變化的新事實或私有知識，請使用 RAG，而非僅依賴微調。

### 訓練模型

從零開始訓練 LLM 無疑是最困難且最複雜的方法，需大量數據、專業資源與適當計算能力。此選項應僅在企業擁有領域特定使用案例及大量該領域數據時考慮。

## 知識檢測

什麼方法可以有效改善 LLM 補全結果？

1. 帶上下文的提示工程
1. RAG
1. 微調模型

答：三個方法都有效。先從帶上下文的提示工程快速改善，當模型需要當前事實或私人商業資料時，使用 RAG。當你有足夠高品質範例並需要模型持續遵循任務、格式、語調或領域模式時，選擇微調。

## 🚀 挑戰

深入了解如何 [使用 RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) 為你的業務帶來效益。

## 不錯的表現，繼續學習

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

前往第三課，我們將探討如何 [負責任地構建生成式 AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->