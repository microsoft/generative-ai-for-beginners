# 選擇與設定 LLM 供應商 🔑

作業<strong>可能</strong>也會設定為透過像 OpenAI、Azure 或 Hugging Face 等支援的服務供應商，對一個或多個大型語言模型（LLM）部署進行操作。這些供應商提供一個 _託管端點_（API），只要有正確的憑證（API 金鑰或 token）我們就能以程式化方式存取。在本課程中，我們討論這些供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 擁有多樣化模型，包含核心的 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)，專注企業級的 OpenAI 模型
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)，僅需單一端點與 API 金鑰即可存取來自 OpenAI、Meta、Mistral、Cohere、Microsoft 等數百個模型（取代將於 2026 年 7 月底退役的 GitHub Models）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供開源模型及推論伺服器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)，如果您想在自有裝置完全離線執行模型，且不需雲端訂閱

<strong>這些練習您需要使用自己的帳號</strong>。作業是選用性的，您可依興趣選擇設定其中一個、全部或不設定任何供應商。以下是註冊指引：

| 註冊 | 費用 | API 金鑰 | 遊樂場 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [專案基礎](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需程式碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [需提前申請存取](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [專案總覽頁面](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 遊樂場](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 有免費層；同一端點 + 金鑰可用於多個模型供應商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 有限模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免費（執行於您的裝置） | 無需 | [本地 CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全離線，OpenAI 相容端點 |
| | | | | |

請依下方指示 _配置_ 本專案以搭配不同供應商。需特定供應商的作業，其檔名將帶有以下標籤：

- `aoai` - 需 Azure OpenAI 端點與金鑰
- `oai` - 需 OpenAI 端點與金鑰
- `hf` - 需 Hugging Face token
- `githubmodels` - 需 Microsoft Foundry Models 端點與金鑰（GitHub Models 將於 2026 年 7 月底退役）

你可設定其中一個、全部或都不設定。相關作業若缺少憑證會直接報錯。

## 建立 `.env` 檔案

我們假定你已閱讀上方指引並於相應供應商註冊，取得所需的驗證憑證（API_KEY 或 token）。針對 Azure OpenAI，我們假定你已有有效 Azure OpenAI 服務部署（端點），且至少部署了一個 GPT 模型用於聊天完成。

下一步是依下列方式設定你的 <strong>本地環境變數</strong>：

1. 在根目錄尋找 `.env.copy` 檔案，其內容應類似下方：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 中的 Azure OpenAI
   ## （Azure OpenAI 服務現在是 Microsoft Foundry 的一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 預設已設定！（目前穩定 GA API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多供應商模型目錄，取代將於 2026 年 7 月底退役的 GitHub 模型）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 執行下面指令將此檔案複製為 `.env`。此檔案被 _gitignore_，以保護機密資料安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節說明填入各變數數值（替換等號右側的佔位字串）。

4. (選項) 若使用 GitHub Codespaces，可將環境變數存為與本專案關聯的 _Codespaces secrets_。這樣就不必在本地設定 .env 檔案。**不過，請注意此方式僅限使用 GitHub Codespaces 時可用。** 若透過 Docker Desktop 使用，仍需設定 .env 檔案。

## 填寫 `.env` 檔案

快速了解變數名稱代表什麼：

| 變數名稱  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在個人資料中設定的使用者訪問令牌 |
| OPENAI_API_KEY | 非 Azure OpenAI 端點的服務授權金鑰 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型的部署端點名稱 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型的部署端點名稱 |
| AZURE_INFERENCE_ENDPOINT | 你的 Microsoft Foundry 專案端點，用於 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 你的 Microsoft Foundry 專案 API 金鑰 |
| | |

注意：最後兩個 Azure OpenAI 變數分別代表用於聊天完成（文字生成）與向量搜尋（嵌入）的預設模型。在相關作業中會有設定說明。

## 設定 Azure OpenAI：從 Azure 入口網站

> **注意：** Azure OpenAI 服務現在是 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 的一部分。資源與部署仍在 Azure 入口網站顯示，但日常模型管理（部署、遊樂場、監控）已轉移至 Foundry 入口網站，而非舊有的獨立 "Azure OpenAI Studio"。

Azure OpenAI 的端點與金鑰會在 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，我們從此開始。

1. 造訪 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 在側邊欄（左側選單）點選 <strong>金鑰與端點</strong>。
1. 點擊 <strong>顯示金鑰</strong>，你應能看到類似以下資訊：KEY 1、KEY 2 與端點。
1. 使用 KEY 1 的值作為 AZURE_OPENAI_API_KEY
1. 使用端點值作為 AZURE_OPENAI_ENDPOINT

接著，我們需要取得所部署特定模型的端點。

1. 在 Azure OpenAI 資源的側邊欄點選 <strong>模型部署</strong>。
1. 於目標頁面點擊 **前往 Microsoft Foundry 入口網站**（或依資源類型點選 <strong>管理部署</strong>）。

這將帶你至 Microsoft Foundry 入口網站，下方將說明你如何找到其他必要數值。

## 設定 Azure OpenAI：從 Microsoft Foundry 入口網站

1. 依上述方法，從你的資源進入 [Microsoft Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊左側側邊欄的 <strong>部署</strong> 標籤，查看當前已部署模型。
1. 若想要的模型尚未部署，請使用 <strong>部署模型</strong>，從 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 部署。
1. 你會需要一個 _文字生成_ 模型，我們推薦：**gpt-5-mini**
1. 你會需要一個 _文字嵌入_ 模型，我們推薦：**text-embedding-3-small**

現在更新環境變數，將 _部署名稱_ 填入。一般來說除非特別修改，部署名稱與模型名稱相同。舉例來說，你會有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**完成後別忘記儲存 .env 檔案**，接著即可關閉，回到執行筆記本的指示。

## 設定 OpenAI：從個人資料

你的 OpenAI API 金鑰可在你的 [OpenAI 帳號](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。若你尚未擁有，可註冊帳號並建立 API 金鑰。取得金鑰後，可於 `.env` 檔案填入 `OPENAI_API_KEY` 變數。

## 設定 Hugging Face：從個人資料

你的 Hugging Face token 可在個人資料中的 [存取令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 找到。請勿公開分享，建議專案使用時新建一組 token 並複製到 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數中。_注意：_ 這技術上不是 API 金鑰，但用於認證，我們為一致性保留這個命名規則。

## 設定 Microsoft Foundry Models：從入口網站

> **注意：** GitHub Models 將於 2026 年 7 月底退役。Microsoft Foundry Models 是直接接替方案，提供相同的免費試用模型目錄及 Azure AI 推論 SDK / OpenAI SDK 體驗。

1. 造訪 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 並建立（或開啟）Foundry 專案。
1. 瀏覽 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 並部署模型，例如 `gpt-5-mini`。
1. 在專案的 <strong>總覽</strong> 頁面，複製 <strong>端點</strong> 與 **API 金鑰**。
1. 於 `.env` 檔中分別將端點值填入 `AZURE_INFERENCE_ENDPOINT`，金鑰值填入 `AZURE_INFERENCE_CREDENTIAL`。

## 離線 / 本地端供應商

若你完全不想使用雲端訂閱，可直接在自己裝置上執行相容開源模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微軟的裝置端執行環境，會自動選擇最佳執行提供者（NPU、GPU 或 CPU），且開放一個 OpenAI 相容端點，讓你幾乎不用修改即可重用本課程範例程式碼。請參閱 [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 開始，或使用指令 `winget install Microsoft.FoundryLocal`（Windows）/ `brew install microsoft/foundrylocal/foundrylocal`（macOS）安裝。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 一個熱門的本地運行開源模型（如 Llama、Phi、Mistral、Gemma）的替代方案。


請參閱 [第19課：使用 SLM 建構](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)，其中包含使用這兩種選項的實作範例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->