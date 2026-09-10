# 選擇及配置大型語言模型提供商 🔑

作業<strong>可能</strong>設定為通過支援的服務提供商（如 OpenAI、Azure 或 Hugging Face）對一個或多個大型語言模型 (LLM) 部署進行操作。這些提供了一個 _託管端點_（API），只要有合適的憑證（API 金鑰或令牌）就可以程式化存取。本課程中，我們會討論以下提供商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 提供多樣模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) 專注企業級的 OpenAI 模型。
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 用單一端點和 API 金鑰存取數百個來自 OpenAI、Meta、Mistral、Cohere、Microsoft 等模型（取代將於 2026 年 7 月底退休的 GitHub Models）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 提供開源模型及推論伺服器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 如果你想在自己的裝置上完全離線運行模型，無需雲端訂閱

<strong>你將需要使用自己的帳戶進行這些練習</strong>。作業是選擇性的，你可以根據興趣選擇設定一個、全部，或不設定任何提供商。以下是註冊的部分指南：

| 註冊 | 費用 | API 金鑰 | 操作環境 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [專案金鑰](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無碼、網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須事先申請存取權](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [專案概覽頁](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 操作環境](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 提供免費階層；一組端點與金鑰可存取多個模型提供商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免費（運行於你的裝置） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全離線，兼容 OpenAI 端點 |
| | | | | |

按照以下指示為不同提供商_配置_此代碼庫。需要特定提供商的作業，文件名通常會帶有以下標籤：

- `aoai` - 需要 Azure OpenAI 端點、金鑰
- `oai` - 需要 OpenAI 端點、金鑰
- `hf` - 需要 Hugging Face 令牌
- `githubmodels` - 需要 Microsoft Foundry Models 端點、金鑰（GitHub Models 將於 2026 年 7 月底退休）

你可以配置其中一個、全部或不配置。相關作業在憑證缺失時會報錯。

## 建立 `.env` 檔案

我們假設你已閱讀上述指導並在相關提供商完成註冊，並取得所需的身份驗證憑證（API_KEY 或令牌）。以 Azure OpenAI 為例，你也應該有一個有效部署的 Azure OpenAI 服務（端點），且至少部署一個 GPT 模型用於聊天補全。

接下來的步驟是設定你的<strong>本地環境變數</strong>如下：

1. 查看根目錄下的 `.env.copy` 檔，內容應類似：

   ```bash
   # OpenAI 供應商
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 內的 Azure OpenAI
   ## （Azure OpenAI 服務現已成為 Microsoft Foundry 一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 預設已設定！ （當前穩定 GA API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多供應商模型目錄，取代將於2026年7月底退休的 GitHub 模型）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下命令將該檔複製到 `.env`。此檔案已在 _gitignore_ 中，以保護秘密。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節所述填寫變數值（將 `=` 右側的佔位符替換）。

4. (選擇) 如果你使用 GitHub Codespaces，可選擇將環境變數保存為與本代碼庫相關聯的 _Codespaces secrets_。如此一來，你就不用建立本地 `.env` 檔。但請注意，**此方案僅適用於使用 GitHub Codespaces 情況**。若改用 Docker Desktop，仍須設定 `.env` 檔。

## 填寫 `.env` 檔案

快速查看變數名稱及其代表的意義：

| 變數  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在個人檔案中設定的使用者存取令牌 |
| OPENAI_API_KEY | 非 Azure OpenAI 端點使用的授權金鑰 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型部署端點 |
| AZURE_INFERENCE_ENDPOINT | 你的 Microsoft Foundry 專案端點，用於 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 你的 Microsoft Foundry 專案 API 金鑰 |
| | |

注意：最後兩個 Azure OpenAI 變數分別對應默認模型的聊天補全（文字生成）及向量搜尋（嵌入）。設定指示將在相關作業中定義。

## 配置 Azure OpenAI：從入口網站

> **注意：** Azure OpenAI 服務現已納入 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。資源和部署仍會顯示於 Azure 入口網站，但日常模型管理（部署、操作環境、監控）現於 Foundry 入口網站進行，而非舊的獨立 "Azure OpenAI Studio"。

Azure OpenAI 端點與金鑰可在 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，從此開始。

1. 進入 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點選側邊欄的 <strong>金鑰和端點</strong> 選項（左側選單）。
1. 點擊 <strong>顯示金鑰</strong> - 你會看到以下資訊：KEY 1、KEY 2 和端點。
1. 將 KEY 1 值用作 AZURE_OPENAI_API_KEY
1. 將端點值用作 AZURE_OPENAI_ENDPOINT

接著，我們需要取得已部署模型的端點。

1. 在 Azure OpenAI 資源頁面，點擊側邊欄的 <strong>模型部署</strong> 選項（左側選單）。
1. 在目標頁面中，點擊 **前往 Microsoft Foundry 入口網站**（或 <strong>管理部署</strong>，視資源類型而定）

這會導向 Microsoft Foundry 入口網站，我們將在此找到以下說明所述的其他值。

## 配置 Azure OpenAI：從 Microsoft Foundry 入口網站

1. 按上述方法從你的資源進入 [Microsoft Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊側邊欄（左側）中的 <strong>部署</strong> 分頁，查看目前已部署的模型。
1. 若目標模型尚未部署，使用 <strong>部署模型</strong> 從 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 部署。
1. 你將需要一個 _文字生成_ 模型—我們推薦：**gpt-5-mini**
1. 你將需要一個 _文字嵌入_ 模型—我們推薦 **text-embedding-3-small**

現在更新環境變數，以反映使用的 _部署名稱_。通常這與模型名稱相同，除非你有明確更改。例如，你可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**完成後別忘了存檔 .env 檔**。現在可以關閉檔案，並回到操作筆記本的指示。

## 配置 OpenAI：從個人檔案

你的 OpenAI API 金鑰可以在你的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 找到。若尚無帳戶，可以註冊並建立 API 金鑰。獲得金鑰後，用其填寫 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

## 配置 Hugging Face：從個人檔案

你的 Hugging Face 令牌可在個人資料的 [存取令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 頁面找到。請勿公開或分享；請為本專案產生新的令牌，並複製到 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數中。_注意:_ 技術上這不是 API 金鑰，但用於身份驗證，因此保持此命名風格以維持一致性。

## 配置 Microsoft Foundry Models：從入口網站

> **注意：** GitHub Models 將於 2026 年 7 月底退休。Microsoft Foundry Models 為其直接替代方案，提供相同的免費試用模型目錄及 Azure AI Inference SDK / OpenAI SDK 體驗。

1. 造訪 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 並建立（或開啟）Foundry 專案。
1. 瀏覽 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 並部署模型，例如 `gpt-5-mini`。
1. 在專案的 <strong>概覽</strong> 頁面，複製 <strong>端點</strong> 和 **API 金鑰**。
1. 使用端點值填寫 `.env` 的 `AZURE_INFERENCE_ENDPOINT`，使用金鑰值填寫 `AZURE_INFERENCE_CREDENTIAL`。

## 離線 / 本地提供商

如果你完全不想使用雲端訂閱，可以直接在自己的裝置上運行相容的開放模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微軟的本地運行時。它會自動選擇最佳執行提供商（NPU、GPU 或 CPU），並暴露兼容 OpenAI 的端點，讓你可幾乎不改動地重用本課程大部分範例程式碼。詳見 [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)，或使用 `winget install Microsoft.FoundryLocal`（Windows）／`brew install microsoft/foundrylocal/foundrylocal`（macOS）安裝。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 在本地執行開放模型如 Llama、Phi、Mistral、Gemma 的熱門替代方案。


請參閱 [第19課：使用SLM建構](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) 了解使用兩種選項的實作範例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->