# 選擇和配置 LLM 供應商 🔑

作業<strong>可以</strong>設置為透過支援的服務供應商，如 OpenAI、Azure 或 Hugging Face，對一個或多個大型語言模型（LLM）部署進行操作。這些供應商提供一個 _託管端點_（API），我們可以使用正確的憑證（API 密鑰或令牌）以程式方式訪問。在本課程中，我們討論以下這些供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ，提供多元模型，包括核心的 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，專注於企業級準備的 OpenAI 模型
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)，透過單一端點和 API 密鑰訪問來自 OpenAI、Meta、Mistral、Cohere、Microsoft 等數百個模型（取代 GitHub Models，該服務將於 2026 年 7 月底停用）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，用於開源模型和推理伺服器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)，如果你想要在自己的設備上完全離線運行模型，無需雲訂閱

<strong>你需要使用自己的帳戶來完成這些練習</strong>。作業是選修的，所以你可以根據興趣選擇設置一個、全部或者都不設定。以下是一些註冊指引：

| 註冊 | 費用 | API 密鑰 | 練習台 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於專案](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需程式碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須事先申請訪問](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [專案概覽頁面](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 練習台](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 免費等級可用；一個端點+密鑰對應多個模型供應商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [訪問令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免費（在你的設備運行） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全離線，支援 OpenAI 相容端點 |
| | | | | |

請依照以下指示來 _配置_ 此程式碼庫以使用不同的供應商。需要特定供應商的作業會在其檔名中包含下列標籤之一：

- `aoai` - 需 Azure OpenAI 端點和密鑰
- `oai` - 需 OpenAI 端點和密鑰
- `hf` - 需 Hugging Face 令牌
- `githubmodels` - 需 Microsoft Foundry Models 端點和密鑰（GitHub Models 將於 2026 年 7 月底停用）

你可以選擇配置其中一個、全部或都不配置。缺少憑證時，相關作業將產生錯誤。

## 建立 `.env` 檔案

我們假設你已經閱讀上方指導並註冊了相關供應商，且已取得所需的認證憑證（API_KEY 或令牌）。以 Azure OpenAI 為例，我們假設你也已經有一個有效部署的 Azure OpenAI 服務（端點），並部署了至少一個 GPT 聊天完成模型。

接下來請依下列步驟配置你的 <strong>本地環境變數</strong>：

1. 在根目錄尋找 `.env.copy` 檔案，裡面應該包含如下所示內容：

   ```bash
   # OpenAI 供應商
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 的 Azure OpenAI
   ##（Azure OpenAI 服務現已成為 Microsoft Foundry 的一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 預設已設定！（目前穩定 GA API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多供應商模型目錄，取代 2026 年 7 月底退役的 GitHub 模型）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用下面的指令將該檔案複製為 `.env`。該檔案已設定為 _gitignore_，以保障機密安全。

   ```bash
   cp .env.copy .env
   ```

3. 依下一節的說明填入變數值（替換 `=` 右側的佔位符）。

4. （選項）如果你使用 GitHub Codespaces，可以選擇將環境變數儲存為與該程式碼庫關聯的 _Codespaces 秘密_，這樣就不必在本地建立 .env 檔案。但請注意，**此選項只適用於使用 GitHub Codespaces 時**。若改用 Docker Desktop，仍需設置 .env 檔案。

## 填寫 `.env` 檔案

讓我們快速了解變數名稱所代表的意義：

| 變數名稱 | 說明 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在個人資料中設置的使用者存取令牌 |
| OPENAI_API_KEY | 用於非 Azure OpenAI 端點服務的授權密鑰 |
| AZURE_OPENAI_API_KEY | 用於 Azure OpenAI 服務的授權密鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字向量嵌入_ 模型部署端點 |
| AZURE_INFERENCE_ENDPOINT | 你的 Microsoft Foundry 專案端點，用於 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 你的 Microsoft Foundry 專案用 API 密鑰 |
| | |

注意：最後兩個 Azure OpenAI 變數分別為聊天完成（文字生成）和向量搜尋（嵌入向量）的預設模型。設置說明將在相關作業中詳述。

## 配置 Azure OpenAI：從入口網站

> **注意：** Azure OpenAI 服務現已納入 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。資源和部署仍可在 Azure 入口網站中查看，但日常的模型管理（部署、練習台、監控）現在改在 Foundry 入口網站操作，取代舊有獨立的「Azure OpenAI Studio」。

Azure OpenAI 的端點和密鑰可在 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)找到，我們從這裡開始。

1. 前往 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 在側邊欄（左側選單）點選 **Keys and Endpoint** 選項。
1. 點擊 **Show Keys** —— 你應該會看到：KEY 1、KEY 2 及 Endpoint。
1. 將 KEY 1 的值用於 AZURE_OPENAI_API_KEY
1. 將 Endpoint 的值用於 AZURE_OPENAI_ENDPOINT

接著，我們需要所部署模型的端點。

1. 在 Azure OpenAI 資源的側邊欄（左側選單）點選 **Model deployments**。
1. 在目標頁面中，點選 **Go to Microsoft Foundry portal**（或根據資源類型點選 **Manage Deployments**）

這會帶你至 Microsoft Foundry 入口網站，我們將在此找到其他必須的設定值，如下所述。

## 配置 Azure OpenAI：從 Microsoft Foundry 入口網站

1. 按上面說明，透過你的資源進入 [Microsoft Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊 **Deployments** 標籤（側邊欄，左側）檢視已部署模型。
1. 如果你想要的模型尚未部署，使用 **Deploy model** 從 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)部署它。
1. 你會需要一個 _文字生成_ 模型 —— 我們推薦：**gpt-4o-mini**
1. 你會需要一個 _文字嵌入_ 模型 —— 我們推薦：**text-embedding-3-small**

現在更新環境變數以反映所用的 _部署名稱_。通常這會和模型名稱相同，除非你特別更改。舉例來說，你可能會這樣寫：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**更新完成後別忘了儲存 .env 檔案**。接著你可以關閉檔案並返回操作筆記本的指示。

## 配置 OpenAI：來自個人頁面

你的 OpenAI API 密鑰可在你的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果沒有，可以註冊帳號並建立 API 密鑰。取得密鑰後，可用它填寫 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

## 配置 Hugging Face：來自個人頁面

你的 Hugging Face 令牌可以在個人資料的 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 中找到。請勿公開或分享令牌，建議為本專案創建新的令牌，並複製貼到 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數下。_注意：_ 技術上這不是 API 密鑰，但用於認證，因此我們沿用此命名慣例以保持一致性。

## 配置 Microsoft Foundry Models：從入口網站

> **注意：** GitHub Models 將於 2026 年 7 月底退役。Microsoft Foundry Models 是直接替代方案，提供相同的免費試用模型目錄以及 Azure AI 推論 SDK / OpenAI SDK 體驗。

1. 前往 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 並建立（或開啟）Foundry 專案。
1. 瀏覽 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)，並部署一個模型，例如 `gpt-4o-mini`。
1. 在專案的 **Overview** 頁面，複製 <strong>端點</strong> 和 **API 密鑰**。
1. 將端點值用於 `.env` 檔案中的 `AZURE_INFERENCE_ENDPOINT`，將密鑰值用於 `AZURE_INFERENCE_CREDENTIAL`。

## 離線／本地供應商

如果你不想使用雲端訂閱，可以直接在自己的設備上運行相容的開源模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微軟的設備端執行環境。自動選擇最佳執行裝置（NPU、GPU 或 CPU），並提供 OpenAI 相容端點，讓你可以最小化修改地重用本課程的大部分示範程式碼。請參閱 [Foundry Local 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 以開始，或者使用 `winget install Microsoft.FoundryLocal`（Windows）／`brew install microsoft/foundrylocal/foundrylocal`（macOS）安裝。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 在本地運行如 Llama、Phi、Mistral 和 Gemma 等開放模型的流行替代方案。


請參閱 [Lesson 19: 使用 SLMs 建構](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) 以獲得兩種選項的實作範例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->