# 選擇及配置 LLM 供應商 🔑

作業 <strong>可以</strong> 設定為透過支援的服務供應商，如 OpenAI、Azure 或 Hugging Face，對一個或多個大型語言模型（LLM）部署進行操作。這些供應商提供 _託管端點_（API），我們可利用正確的憑證（API 金鑰或令牌）以程式方式存取。本課程中，我們將討論以下供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，擁有多款模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，專注於企業級的 OpenAI 模型
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)，提供單一端點和 API 金鑰以存取來自 OpenAI、Meta、Mistral、Cohere、Microsoft 等數百個模型（取代將於 2026 年 7 月底退休的 GitHub Models）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，開源模型及推理伺服器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)，如果你希望完全離線在自己的裝置運行模型，無需雲端訂閱

<strong>你需要自行使用帳戶完成這些練習</strong>。作業是選擇性的，因此你可以根據興趣選擇設定其中一個、全部或沒有供應商。以下是註冊指引：

| 註冊 | 費用 | API 金鑰 | Playground | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [專案基礎](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無代碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多款模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [須提前申請存取](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [專案概覽頁](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 免費方案可用；一個端點及金鑰可存取多款模型供應商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 限制模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免費（在你的裝置運行） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全離線，OpenAI 相容端點 |
| | | | | |

請依下方指示，為不同供應商 _配置_ 本儲存庫。需要特定供應商的作業將於檔名中包含以下標籤：

- `aoai` - 需要 Azure OpenAI 端點與金鑰
- `oai` - 需要 OpenAI 端點與金鑰
- `hf` - 需要 Hugging Face 令牌
- `githubmodels` - 需要 Microsoft Foundry Models 端點與金鑰（GitHub Models 將於 2026 年 7 月底退休）

你可以設定一個、沒有或全部供應商。相關作業若憑證遺失則會出錯。

## 建立 `.env` 檔案

假設你已閱讀上述指引，並已在相關供應商註冊，取得必需的認證憑證（API_KEY 或令牌）。對於 Azure OpenAI，假設你已有有效的 Azure OpenAI 服務部署端點，並至少部署了一款 GPT 聊天完成模型。

接下來步驟是配置你的 <strong>本地環境變數</strong>，如下：

1. 在根資料夾中找到 `.env.copy` 檔案，內容應如以下所示：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 內的 Azure OpenAI
   ## （Azure OpenAI 服務現已成為 Microsoft Foundry 一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 預設已設定！（目前穩定 GA API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多提供者模型目錄，取代 GitHub 模型，GitHub 模型將於 2026 年 7 月底退休）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下指令將該檔案複製為 `.env`。此檔案已加入 _gitignore_，可確保憑證安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節說明填入數值（替換 `=` 右側的佔位符）。

4. （選擇性）若你使用 GitHub Codespaces，可將環境變數保存為本儲存庫關聯的 _Codespaces secrets_。此選項可免去本地 .env 檔案設置。**不過此選項只適用於 GitHub Codespaces。** 若使用 Docker Desktop 則仍需建立 .env 檔案。

## 填寫 `.env` 檔案

來快速了解各變數名稱所代表之意義：

| 變數名稱  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在個人資料中設定的用戶存取令牌 |
| OPENAI_API_KEY | 非 Azure OpenAI 端點服務使用的授權金鑰 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 服務使用的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型的部署端點 |
| AZURE_INFERENCE_ENDPOINT | 你的 Microsoft Foundry 專案端點，用於 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 你 Microsoft Foundry 專案的 API 金鑰 |
| | |

注意：最後兩個 Azure OpenAI 變數分別對應聊天完成（文字生成）和向量搜尋（嵌入）的預設模型。相關設定指示會在相應作業中說明。

## Azure OpenAI 配置：透過入口網站

> **注意：** Azure OpenAI 服務現已納入 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 旗下。資源與部署仍會出現在 Azure 入口網站，但日常模型管理（部署、playground、監控）現改在 Foundry 網站進行，取代舊獨立的「Azure OpenAI Studio」。

Azure OpenAI 端點與金鑰可在 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，讓我們從這裡開始。

1. 前往 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點選側邊欄（左側選單）中的 <strong>金鑰與端點</strong> 選項。
1. 點擊 <strong>顯示金鑰</strong> - 你應該可看到 KEY 1、KEY 2 及 Endpoint。
1. 將 KEY 1 欄位用於 AZURE_OPENAI_API_KEY
1. 將 Endpoint 欄位用於 AZURE_OPENAI_ENDPOINT

接著，我們需要所部署的特定模型端點。

1. 點選 Azure OpenAI 資源側邊欄（左選單）中的 <strong>模型部署</strong> 選項。
1. 進入目標頁面後，點擊 **前往 Microsoft Foundry 入口**（或視資源類型為 <strong>管理部署</strong>）

這將帶你至 Microsoft Foundry 入口，我們將依下述指示找到其他數值。

## Azure OpenAI 配置：透過 Microsoft Foundry 入口

1. 如上所述，從你的資源前往 [Microsoft Foundry 入口](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊左側側邊欄的 <strong>部署</strong> 標籤以檢視現有部署模型。
1. 若尚未部署目標模型，可於 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 使用 <strong>部署模型</strong> 進行布署。
1. 你將需要一款 _文字生成_ 模型 - 建議使用：**gpt-4o-mini**
1. 你將需要一款 _文字嵌入_ 模型 - 建議使用 **text-embedding-3-small**

現在更新環境變數以反映所用的 _部署名稱_，通常與模型名稱相同（除非明確更改）。舉例：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**完成後別忘記儲存 .env 檔案**。你現在可關閉此檔案並遵循筆記本指令繼續操作。

## OpenAI 配置：來自個人帳戶

你的 OpenAI API 金鑰可在你的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。若尚無帳戶，可註冊並建立 API 金鑰。取得後，填入 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

## Hugging Face 配置：來自個人資料

你的 Hugging Face 令牌可在個人資料中 [存取令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 頁面找到。請勿公開或分享。請為本專案建立新令牌，並複製到 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數中。_註：_ 技術上這不是 API 金鑰，但作為認證使用，我們保留此命名慣例以保持一致。

## Microsoft Foundry Models 配置：入口網站

> **注意：** GitHub Models 將於 2026 年 7 月底退休，Microsoft Foundry Models 是直接替代方案，提供相同免費試用模型目錄和 Azure AI 推理 SDK / OpenAI SDK 體驗。

1. 前往 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 建立（或開啟）Foundry 專案。
1. 瀏覽 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 並部署一款模型，例如 `gpt-4o-mini`。
1. 在專案 <strong>概覽</strong> 頁面複製 <strong>端點</strong> 與 **API 金鑰**。
1. 將端點填入你的 `.env` 檔案中 `AZURE_INFERENCE_ENDPOINT`，將金鑰填入 `AZURE_INFERENCE_CREDENTIAL`。

## 離線 / 本地供應商

如果你完全不想使用雲端訂閱，可以直接在自己裝置上運行相容的開源模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微軟的裝置端運行時，自動選擇最佳執行供應者（NPU、GPU 或 CPU），並提供 OpenAI 兼容端點，因此你可以用非常少的更動重用本課程的大部分示例程式碼。請參閱 [Foundry Local 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 開始使用，或使用 `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) 進行安裝。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 一個用於本地運行 Llama、Phi、Mistral、Gemma 等開源模型的熱門替代方案。


請參閱 [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) 以獲取同時使用兩個選項的實作範例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->