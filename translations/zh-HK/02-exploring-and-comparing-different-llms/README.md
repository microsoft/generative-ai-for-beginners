# 探索及比較不同大型語言模型 (LLMs)

[![探索及比較不同大型語言模型 (LLMs)](../../../translated_images/zh-HK/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _點擊上方圖片觀看本課程影片_

透過上一課程，我們已了解生成式人工智能如何改變科技格局、大型語言模型（LLMs）的工作原理，以及企業（像我們的初創公司）如何應用它們以解決用例和成長！本章節將比較不同類型的大型語言模型，了解它們的優缺點。

我們初創公司的下一步是探索現有LLM的狀況，並了解哪些適合我們的用例。

## 簡介

本課程將涵蓋：

- 現時不同類型的LLM。
- 在Azure上測試、迭代及比較不同模型以配合你的用例。
- 如何部署LLM。

## 學習目標

完成本課程後，你將能：

- 為你的用例選擇合適的模型。
- 了解如何測試、迭代並提升模型的表現。
- 了解企業如何部署模型。

## 了解不同類型的LLM

LLM可依據架構、訓練數據及用例被分類。理解這些差異有助我們的初創公司為情境選擇合適模型，並懂得如何測試、迭代及提升性能。

LLM種類繁多，所選模型取決於你的用途、數據、支付意願等因素。

根據你打算使用模型於文字、音訊、影片、圖像生成等用途，可能會選擇不同類型的模型。

- <strong>音訊和語音識別</strong>。Whisper類模型仍是通用語音識別模型，但生產環境中亦有較新語音轉文字模型，例如 `gpt-4o-transcribe`、`gpt-4o-mini-transcribe` 及分話者識別版本。根據語言覆蓋範圍、分話者識別、實時支持、延遲及成本進行評估。詳見 [OpenAI 語音轉文字文檔](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst)。

- <strong>圖像生成</strong>。DALL-E及Midjourney是著名圖像生成選項，目前OpenAI圖像API中心是基於GPT圖像模型如 `gpt-image-2`，同時Stable Diffusion、Imagen、Flux及其他模型系列也常用。比較提示響應度、編輯支援、風格控制、安全要求及授權。詳見 [OpenAI 圖像生成指南](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) 及本課程第9章。

- <strong>文字生成</strong>。文字模型涵蓋前沿模型、推理模型、小型低延遲模型及開放權重模型。例子包括OpenAI GPT-5.x、Anthropic Claude 4.x、Google Gemini 3.x、Meta Llama 4、Mistral模型。選擇時不要只看發布日期或價格，需比較任務質量、延遲、上下文視窗、工具使用、安全行為、區域可用性及總成本。可參考 [Microsoft Foundry 模型目錄](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) 比較Azure上的模型。

- <strong>多模態</strong>。許多現有模型可處理多於文字輸入。有些接受圖像、音訊或影片輸入，有些可調用工具，專門模型可生成圖像、音訊及影片。例如，現有OpenAI模型支援文字與圖像輸入，Gemini模型視版本支援文字、程式碼、圖像、音訊及影片輸入，Llama 4 Scout與Maverick是原生多模態的開放權重模型。構建工作流程前，須檢查每個模型卡支持的輸入及輸出模態。

選擇模型意味著獲得某些基本能力，但這可能不足。通常企業有特定數據需要告知LLM。處理方法有幾種選擇，將在接下來章節詳述。

### 基礎模型與大型語言模型 (LLMs)

「基礎模型」一詞由[史丹福研究員首次提出](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)，定義為符合某些標準的AI模型，如：

- <strong>以無監督學習或自監督學習訓練</strong>，即基於無標籤的多模態數據訓練，無需人工標注。
- <strong>模型非常龐大</strong>，基於深度神經網絡訓練，涉及數十億參數。
- **通常作為其他模型的「基礎」**，可作為其他模型基礎，通過微調延伸功能。

![基礎模型與大型語言模型 (LLMs)](../../../translated_images/zh-HK/FoundationModel.e4859dbb7a825c94.webp)

圖片來源：[Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

為釐清區別，以ChatGPT為例。早期版本ChatGPT用GPT-3.5作為基礎模型，OpenAI再利用聊天專屬數據與對齊技術，打造適合對話場景（如聊天機械人）表現更佳的微調版本。現代AI服務通常在多種模型變體間切換，服務名稱與底層模型名稱未必相同。

![基礎模型](../../../translated_images/zh-HK/Multimodal.2c389c6439e0fc51.webp)

圖片來源：[2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 開放權重／開源模型與私有模型

另一種分類方式是根據模型是否開放權重、開源或私有。

開源及開放權重模型允許查看、下載或自訂模型檔案，但授權條件不同。有些完全開源，有些開放權重但有使用限制。當企業需更多部署控制、數據本地化、成本或定制化需求時很有用。然團隊仍需審查授權條款、服務成本、維護、安全更新及評估品質，才能用於生產環境。例子有[Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst)、部分[Mistral模型](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst)，及許多托管於[Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst)上的模型。

私有模型由供應商擁有及托管，常為管理式生產優化，可提供強大支援、安全系統、工具整合及擴充。客戶通常無法檢視或修改模型權重，必須審查供應商的隱私、保留、合規與可接受使用條款。例子有[OpenAI模型](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)、[Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst)及[Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst)。

### 向量嵌入 (Embedding)、圖像生成及文字與程式碼生成

LLM亦可依輸出類型分類。

向量嵌入是一類能將文字轉為數值形式的模型，稱為嵌入 (embedding)，是輸入文字的數值化表徵。嵌入讓機器更易理解字詞或句子間的關係，且可作為其他模型（如分類模型或數值表現優異的聚類模型）的輸入。嵌入模型常用於遷移學習：先建立具大量數據的代理任務模型，然後其模型權重（嵌入）可重用於其他下游任務。此類別例子為[OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)。

![向量嵌入](../../../translated_images/zh-HK/Embedding.c3708fe988ccf760.webp)

圖像生成模型用於生成圖像，常被用於圖像編輯、合成及轉換。其訓練資料集常大規模，如[LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)，能生成新圖像或用修補、超解析度、上色技巧編輯現有圖像。例子有[GPT圖像模型](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst)、[Stable Diffusion模型](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst)及Imagen模型。

![圖像生成](../../../translated_images/zh-HK/Image.349c080266a763fd.webp)

文字與程式碼生成模型用於生成文字或程式碼，常應用於文字摘要、翻譯及問答。文字生成模型訓練於大規模文字資料，例如[BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst)，能生成新文字或回答問題。程式碼生成模型如[CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)訓練於大型程式碼資料集如GitHub，能生成新程式碼或修復現有程式碼漏洞。

![文字與程式碼生成](../../../translated_images/zh-HK/Text.a8c0cf139e5cc2a0.webp)

### 編碼器-解碼器 (Encoder-Decoder) 與 僅解碼器 (Decoder-only)

談及LLM不同架構，讓我們用類比說明。

想像你的主管委派你為學生編寫小測驗，你有兩位同事：一位負責內容創作，另一位負責審核。

內容創作者就像僅有解碼器模型：他們能看主題、觀察你所寫的內容，然後根據上下文繼續生成內容。他們擅長寫吸引人且具資訊性的內容，但任務只是分類、檢索或編碼信息時，不一定是最佳選擇。例子為GPT及Llama等僅解碼器模型系列。

審核者則像僅編碼器模型，查看所寫課程與答案，理解彼此關聯與上下文，但不擅長生成內容。典型編碼器模型為BERT。

想像也有可創作及審核小測的人，這便是編碼器-解碼器模型。例子有BART及T5。

### 服務 (Service) 與 模型 (Model)

現談服務與模型差異。服務是雲端供應商提供的產品，通常結合了多個模型、數據及其他組件。模型是服務的核心組件，常為基礎模型如LLM。

服務通常為生產優化，使用介面也比模型友好，帶有圖形用戶介面。但服務未必免費，需訂閱或付費以使用，換取使用服務擁有者的設備與資源，優化開支及輕鬆擴充。例子為[Azure OpenAI 服務](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst)，採用按用量付費方案，讓用戶按照實際使用量付費。Azure OpenAI 服務亦提供企業級安全及負責任AI框架，涵蓋模型能力之上。

模型為神經網路的產物，包括參數、權重、架構、分詞器及配置。要在本地或私有環境運行模型，需合適硬件、服務基礎設施、監控，以及兼容的開源/開權授權或商用授權。開權模型如Llama 4或Mistral可自託管，惟仍需計算能力與運營專業知識。

## 如何在Azure上測試及迭代不同模型以理解性能


當我們團隊探索現有的大語言模型（LLM）現況並為其場景挑選出合適的候選模型後，下一步是用他們的數據和工作負載對模型進行測試。這是一個通過實驗和測量進行的反覆過程。
我們之前提及的大多數模型（OpenAI 模型、類似 Llama 4 和 Mistral 的開放權重模型，以及 Hugging Face 模型）都可以在 [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) 中找到。

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst)，前稱 Azure AI Studio/Azure AI Foundry，是一個統一的 Azure 平台，用於構建 AI 應用和代理。它幫助開發者管理從實驗評估到部署、監控和治理的整個生命週期。Microsoft Foundry 中的模型目錄允許用戶：

- 在目錄中尋找感興趣的基礎模型，涵蓋 Azure 銷售的模型以及合作夥伴和社群提供的模型。用戶可以根據任務、提供者、授權、部署選項或名稱進行篩選。

![Model catalog](../../../translated_images/zh-HK/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- 查看模型卡，其中包含詳細的預期用途和訓練數據描述、程式碼範例，以及內部評估庫的評估結果。

![Model card](../../../translated_images/zh-HK/ModelCard.598051692c6e400d.webp)

- 通過 [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst) 面板比較業界的模型和數據集基準，評估哪一個最符合業務場景需求。

![Model benchmarks](../../../translated_images/zh-HK/ModelBenchmarks.254cb20fbd06c03a.webp)

- 在自訂訓練數據上微調支持的模型，以提升特定工作負載的模型表現，利用 Microsoft Foundry 的實驗和追蹤功能。

![Model fine-tuning](../../../translated_images/zh-HK/FineTuning.aac48f07142e36fd.webp)

- 將原始的預訓練模型或微調版本部署到遠端的實時推理端點，使用託管計算或無伺服器部署選項，讓應用程式能夠調用。

![Model deployment](../../../translated_images/zh-HK/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> 並非目錄中所有模型目前都支持微調和/或按需付費部署。請查看模型卡以了解模型的功能和限制詳情。

## 改善 LLM 結果

我們的創業團隊嘗試過多種 LLM 以及一個雲端平台（Microsoft Foundry），該平台可讓我們比較不同模型、在測試數據上評估它們、提升效能，並部署到推理端點。

那麼，他們應該在何時考慮微調模型，而非使用預訓練模型？還有其他方法可以提升特定工作負載的模型表現嗎？

業務可採用多種方式從 LLM 獲取所需結果。部署 LLM 時，可以選擇不同類型的模型與不同程度的訓練，這些方案在複雜度、成本和質量上各有不同。以下列出幾種不同做法：

- <strong>帶上下文的提示工程</strong>。目的是在提示時提供足夠的上下文，以確保得到需要的回答。

- **檢索增強生成（Retrieval Augmented Generation，RAG）**。例如，您的數據可能存在於資料庫或網路端點中，為了確保在提示時包含這些數據或其子集，可以檢索相關數據並將其納入用戶提示中。

- <strong>微調模型</strong>。即您在自己的數據上進一步訓練模型，使其更精確並更符合您的需求，但可能成本較高。

![LLMs deployment](../../../translated_images/zh-HK/Deploy.18b2d27412ec8c02.webp)

圖片來源：[Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 帶上下文的提示工程

預訓練的 LLM 在通用自然語言任務中表現良好，即使只用簡短提示（如要完成的句子或問題）調用，也稱為「零射學習」。

然而，使用者越能建構出詳細且含有範例的查詢——即上下文，回答就會越準確且越符合使用者期望。當提示中包含一個範例時，我們稱之為「單射學習」，如果包含多個範例則稱為「少射學習」。
帶上下文的提示工程是最具成本效益的起步方法。

### 檢索增強生成（RAG）

LLM 有一個限制，就是它們只能根據訓練時所使用的數據來生成回答。這意味著它們對訓練後發生的事實一無所知，且無法訪問非公開資訊（例如公司數據）。
可以通過 RAG 技術來克服這一限制，該技術會將外部數據以文件片段形式增添到提示中，同時考慮提示長度限制。這由向量資料庫工具支援，例如 [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)，該工具從多種預定義資料源中檢索有用片段，並加入提示上下文。

當業務沒有足夠數據、時間或資源微調 LLM，但仍希望在特定工作負載上提升表現並降低產生幻覺、過時或不支持回答的風險時，這項技術非常有用。

### 微調模型

微調是利用遷移學習的方法來「適應」模型至下游任務或特定問題。與少射學習和 RAG 不同，微調會產生一個新的模型，帶有更新的權重與偏差。這需要一組訓練範例，包括單一輸入（提示）及其對應輸出（完成內容）。
若符合以下情況，這是首選方法：

- <strong>使用較小的任務專用模型</strong>。業務希望對較小模型進行微調以聚焦狹窄任務，而非反覆提示更大型前沿模型，從而達到更具成本效益和更快的解決方案。

- <strong>考慮延遲</strong>。延遲對某些用例非常重要，因此無法使用非常長的提示，或者需要模型學習的範例數量超出提示長度限制。

- <strong>調整穩定行為</strong>。業務擁有大量高品質範例，且希望模型持續遵循任務模式、輸出格式、語氣或特定領域風格。如果主要問題是新鮮事實或經常變動的私有知識，則應用 RAG 代替單靠微調。

### 從頭訓練模型

從頭訓練 LLM 無疑是最困難且複雜的方式，需要大量數據、專業人力以及充足計算能力。此選項只適用於業務有特定領域用例及大量領域相關數據的情況。

## 知識檢查

什麼方法可以有效提升 LLM 的完成結果？

1. 帶上下文的提示工程
1. RAG
1. 微調模型

答案：以上三種方法均可幫助。可先從帶上下文的提示工程開始，快速提升；當模型需要最新事實或商業私有數據時，使用 RAG；當擁有足夠高品質範例且希望模型持續遵循任務、格式、語氣或領域模式時，選擇微調。

## 🚀 挑戰

深入閱讀如何為您的業務[使用 RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)。

## 做得好，繼續學習

完成本課程後，查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

前往第 3 課，瞭解如何[負責任地使用生成式 AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->