# 選擇及配置 LLM 供應商 🔑

作業<strong>可能</strong>會設置為透過支援的服務供應商如 OpenAI、Azure 或 Hugging Face，對一個或多個大型語言模型（LLM）部署進行操作。這些服務提供一個 _託管端點_（API），我們可以用正確的憑證（API 金鑰或令牌）以程式方式存取。在本課程中，我們將討論以下這些供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供多款模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)，專注於企業級準備的 OpenAI 模型。
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)，提供單一端點及 API 金鑰以存取來自 OpenAI、Meta、Mistral、Cohere、Microsoft 等數百個模型（取代將於 2026 年 7 月底退休的 GitHub Models）。
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供開源模型及推斷伺服器。
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)，如果你想完全離線在自家設備上運行模型，毋須雲端訂閱。

<strong>這些練習需使用你自己的帳戶</strong>。作業為選填，你可依興趣選擇設定其中一個、全部或不設定任何供應商。以下是一些註冊指引：

| 註冊 | 費用 | API 金鑰 | 遊樂場 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於專案](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [免程式碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多款模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [需提前申請存取權](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [專案概覽頁面](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 遊樂場](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 有免費層級；一個端點+金鑰可存取多家模型供應商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限制](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免費（在你的裝置上執行） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全離線，與 OpenAI 兼容的端點 |
| | | | | |

請依照以下說明來_配置_此存放庫以用於不同的供應商。需要特定供應商的作業檔名會包含以下標籤之一：

- `aoai` - 需要 Azure OpenAI 端點與金鑰
- `oai` - 需要 OpenAI 端點與金鑰
- `hf` - 需要 Hugging Face 令牌
- `githubmodels` - 需要 Microsoft Foundry Models 端點與金鑰（GitHub Models 於 2026 年 7 月底退役）

你可以配置其中一個、沒有或全部供應商。相對應的作業若缺憑證會直接出錯。

## 建立 `.env` 檔案

我們假設你已閱讀上述指引且已於相關供應商註冊並取得所需的鑑權憑證（API_KEY 或令牌）。Azure OpenAI 部分則假設你同時已部署一個 Azure OpenAI 服務的有效端點，且至少部署了一個 GPT 模型用於對話完成。

下一步是如以下方式配置你的<strong>本地環境變數</strong>：

1. 在根目錄尋找名為 `.env.copy` 的檔案，內容應如下：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 的 Azure OpenAI
   ## （Azure OpenAI 服務現為 Microsoft Foundry 的一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 已設為預設！（目前穩定的 GA API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多供應商模型目錄，取代 GitHub 模型，後者將於 2026 年 7 月底退役）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下命令將該檔複製成 `.env`。此檔案已被 _gitignore_，可安全保存秘密資訊。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節說明的內容填入變數值（替換等號右側的佔位符）。

4. （選項）如果你使用 GitHub Codespaces，也可以選擇將環境變數保存為與此存放庫相關聯的_Codespaces 秘密_。如此一來，你便不需要設定本地 .env 檔案。<strong>但請注意，此選項只於 GitHub Codespaces 有效。</strong>若你使用 Docker Desktop 等，仍需自行設定 .env 檔案。

## 填寫 `.env` 檔案

讓我們快速看看變數名稱代表什麼：

| 變數名稱  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是你在個人資料中設定的使用者存取令牌 |
| OPENAI_API_KEY | 用於非 Azure OpenAI 端點的服務授權金鑰 |
| AZURE_OPENAI_API_KEY | 用於 Azure OpenAI 服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型的部署端點名稱 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型的部署端點名稱 |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry 專案的端點，用於 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry 專案的 API 金鑰 |
| | |

注意：最後兩個 Azure OpenAI 變數分別代表用於對話完成（文字生成）及向量搜索（嵌入）的預設模型。設定說明會在相關作業中定義。

## 從入口網站配置 Azure OpenAI

> **注意：** Azure OpenAI 服務現已整合至 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。資源和部署仍會顯示於 Azure 入口網站，但日常的模型管理（部署、遊樂場、監控）現在改在 Foundry 入口網站進行，不再使用舊有的獨立「Azure OpenAI Studio」。

Azure OpenAI 的端點與金鑰可於 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，我們先從這裏開始。

1. 前往 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點擊側邊欄（左側選單）中的 <strong>金鑰與端點</strong> 選項。
1. 點擊 <strong>顯示金鑰</strong>，你會看到 KEY 1、KEY 2 與端點。
1. 使用 KEY 1 的值作為 AZURE_OPENAI_API_KEY
1. 使用端點的值作為 AZURE_OPENAI_ENDPOINT

接著，我們需要取得所部署特定模型的端點。

1. 點擊 Azure OpenAI 資源的側邊欄（左選單）中 <strong>模型部署</strong> 選項。
1. 在目的頁面中，點擊 **前往 Microsoft Foundry 入口網站**（或依資源類型可能顯示 <strong>管理部署</strong>）

這會導你至 Microsoft Foundry 入口網站，我們將在那裏找到以下說明的其他值。

## 從 Microsoft Foundry 入口網站配置 Azure OpenAI

1. 按上面說明，從你的資源入口導航至 [Microsoft Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊側邊欄（左）中的 <strong>部署</strong> 分頁以查看已部署模型。
1. 若未部署你需的模型，利用 <strong>部署模型</strong> 從 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 新增部署。
1. 你將需要一個 _文字生成_ 模型 — 推薦使用：**gpt-5-mini**
1. 你將需要一個 _文字嵌入_ 模型 — 推薦使用：**text-embedding-3-small**

現在更新環境變數反映 _部署名稱_，通常會與模型名稱相同，除非有特別更改。例如，你可能會有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**完成後別忘了儲存 .env 檔案**。接著你可以關閉檔案，回到筆記本的執行說明。

## 從個人資料配置 OpenAI

你的 OpenAI API 金鑰可在你的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 內找到。如果還未有帳戶，可註冊一個並創建 API 金鑰。取得金鑰後可用它來填寫 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

## 從個人資料配置 Hugging Face

你的 Hugging Face 令牌位於個人資料的 [存取令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 頁面。請勿公開或分享這些令牌，而是為本專案創建新的令牌，並複製至 `.env` 檔案中的 `HUGGING_FACE_API_KEY` 變數。_注意：_ 它嚴格來說不是 API 金鑰，但用作鑑權，我們為一致起見繼續使用此命名慣例。

## 從入口網站配置 Microsoft Foundry Models

> **注意：** GitHub Models 將於 2026 年 7 月底退休。Microsoft Foundry Models 為直接替代方案，提供同樣可免費試用的模型目錄及 Azure AI 推斷 SDK / OpenAI SDK 體驗。

1. 前往 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 並建立（或開啟）Foundry 專案。
1. 瀏覽 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 並部署模型，例如 `gpt-5-mini`。
1. 在專案的 <strong>概覽</strong> 頁面，複製 <strong>端點</strong> 與 **API 金鑰**。
1. 在 `.env` 檔案中，分別將端點值填入 `AZURE_INFERENCE_ENDPOINT`，API 金鑰填入 `AZURE_INFERENCE_CREDENTIAL`。

## 離線／本地供應商

若你完全不想使用雲端訂閱，可以在自己的設備上直接運行相容的開放模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** — 微軟的本地執行時。它會自動選擇最佳執行提供者（NPU、GPU 或 CPU），並提供符合 OpenAI 端點標準，故你可用本課程的範例程式碼並做極少更改。詳見 [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)，或使用 `winget install Microsoft.FoundryLocal`（Windows）／`brew install microsoft/foundrylocal/foundrylocal`（macOS）安裝。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** — 流行的本地運行開放模型替代方案，如 Llama、Phi、Mistral 與 Gemma 等。


請參閱 [第19課：使用 SLM 建構](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) 來了解使用兩個選項的操作範例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->