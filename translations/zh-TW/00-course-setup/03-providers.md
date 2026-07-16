# 選擇與設定大型語言模型提供者 🔑

作業<strong>可能</strong>也會設定為透過像是 OpenAI、Azure 或 Hugging Face 等支援的服務供應商，對一個或多個大型語言模型（LLM）部署工作。這些提供一個我們可以使用適當憑證（API 金鑰或令牌）以程式化方式存取的_託管端點_（API）。在本課程中，我們討論這些提供者：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 提供多元模型，包括核心的 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) 針對企業級需求的 OpenAI 模型
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 提供單一端點與 API 金鑰，可存取來自 OpenAI、Meta、Mistral、Cohere、Microsoft 等數百個模型（取代將於 2026 年七月底退休的 GitHub Models）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 提供開源模型與推理伺服器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 如果你希望完全在自己的裝置上離線運行模型，不需任何雲端訂閱

<strong>這些練習需要使用你自己的帳戶</strong>。作業是選擇性的，因此你可根據興趣選擇設定其中一個、全部或都不設定。註冊的一些指引如下：

| 註冊 | 費用 | API 金鑰 | 操作介面 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於專案](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需程式碼，網頁介面](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [須提前申請存取](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [專案總覽頁面](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 操作介面](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 提供免費層級；一個端點 + 金鑰支援多個模型供應商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 有模型限制](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免費（在你的裝置上運行） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全離線，OpenAI 相容端點 |
| | | | | |

請依照下方指示_配置_此程式庫以供不同提供者使用。需要特定提供者的作業檔名會包含以下之一的標籤：

- `aoai` - 需 Azure OpenAI 端點與金鑰
- `oai` - 需 OpenAI 端點與金鑰
- `hf` - 需 Hugging Face 令牌
- `githubmodels` - 需 Microsoft Foundry Models 端點與金鑰（GitHub Models 將於 2026 年七月底退役）

你可以設定其中一個、都不設定或全部設定。相關作業在缺少憑證時會直接報錯。

## 建立 `.env` 檔案

我們假設你已閱讀上方指引，並向相關提供者註冊取得所需的驗證憑證（API_KEY 或令牌）。以 Azure OpenAI 為例，我們假設你已成功部署 Azure OpenAI 服務（端點），且至少部署了一個用於聊天完成的 GPT 模型。

下一步是依照下列方式設定你的<strong>本地環境變數</strong>：

1. 檢視根目錄中名為 `.env.copy` 的檔案，內容大致如下：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 中的 Azure OpenAI
   ## （Azure OpenAI 服務現已成為 Microsoft Foundry 的一部分: https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 已設定預設值！(目前穩定的 GA API 版本)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多提供者模型目錄，取代將於 2026 年 7 月底退役的 GitHub 模型）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下指令將檔案複製為 `.env`。此檔案已加入 .gitignore，能確保秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 按照下一節說明，填寫各欄位值（取代等號右側的佔位符）。

4. (選項) 如果你使用 GitHub Codespaces，則可選擇把環境變數保存為與本程式庫關聯的 _Codespaces 秘密_。如此一來，就不必再設定本地 `.env` 檔案。**但請注意，這選項僅適用於 GitHub Codespaces。** 若使用 Docker Desktop 則仍需設定 `.env`。

## 填寫 `.env` 檔案

讓我們快速看一下變數名稱，以了解其代表的意義：

| 變數名稱  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是你在個人頁面設定的使用者存取令牌 |
| OPENAI_API_KEY | 使用非 Azure OpenAI 端點的服務驗證金鑰 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 服務的驗證金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文本生成_ 模型部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文本嵌入_ 模型部署端點 |
| AZURE_INFERENCE_ENDPOINT | 你的 Microsoft Foundry 專案端點，用於 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 你的 Microsoft Foundry 專案 API 金鑰 |
| | |

注意：最後兩個 Azure OpenAI 變數分別代表聊天完成（文本生成）和向量搜尋（嵌入）模型的預設部署。設定指令會在相關作業中說明。

## 配置 Azure OpenAI：從入口網站操作

> **注意：** Azure OpenAI 服務已整合入 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。資源與部署仍顯示在 Azure 入口網站，但日常模型管理（部署、遊樂場、監控）現在改在 Foundry 入口網站，而非舊有的獨立「Azure OpenAI Studio」。

Azure OpenAI 端點與金鑰可在 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，我們就從這裡開始。

1. 造訪 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點選側欄的 **Keys and Endpoint** 選項（左側選單）。
1. 點選 <strong>顯示金鑰</strong>，你應會看到 KEY 1、KEY 2 以及 Endpoint。
1. 使用 KEY 1 的值填入 AZURE_OPENAI_API_KEY
1. 使用 Endpoint 值填入 AZURE_OPENAI_ENDPOINT

接著，我們需要取得已部署模型的端點。

1. 點選 Azure OpenAI 資源的側欄 **Model deployments** 選項。
1. 在目的頁面，點選 **前往 Microsoft Foundry 入口網站**（或 <strong>管理部署</strong>，視你的資源類型而定）

這會帶你進入 Microsoft Foundry 入口網站，我們將在此找到其他所需值，如下所述。

## 配置 Azure OpenAI：從 Microsoft Foundry 入口網站

1. 按照上方說明，從你的資源導向 [Microsoft Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點選側欄（左側）**Deployments** 頁籤，查看目前部署的模型。
1. 如果想要的模型尚未部署，使用 **Deploy model** 從 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 部署它。
1. 你需要一個＿文本生成＿模型 - 建議使用：**gpt-4o-mini**
1. 你需要一個＿文本嵌入＿模型 - 建議使用 **text-embedding-3-small**

現在更新環境變數以反映所使用的_部署名稱_。通常它會與模型名稱相同，除非你有明確變更。例如，你可能會有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**完成後請記得儲存 .env 檔案**。儲存後即可退出檔案，然後返回指示繼續執行筆記本。

## 配置 OpenAI：從個人檔案

你的 OpenAI API 金鑰可在你的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。若尚未擁有，可註冊帳號並建立 API 金鑰。取得金鑰後，填入 `.env` 檔中的 `OPENAI_API_KEY` 變數。

## 配置 Hugging Face：從個人檔案

你的 Hugging Face 令牌可在個人分頁下的 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 找到。請勿公開或分享這些令牌。建議為此專案創建新的令牌，然後複製到 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數中。_備註：_技術上這不是 API 金鑰，但用於驗證，所以為保持一致性我們保留該命名慣例。

## 配置 Microsoft Foundry Models：從入口網站

> **注意：** GitHub Models 將於 2026 年七月底退役。Microsoft Foundry Models 是直接替代方案，提供同樣的免費試用模型目錄以及 Azure AI 推論 SDK / OpenAI SDK 體驗。

1. 造訪 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 並建立（或開啟）Foundry 專案。
1. 瀏覽 [模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 並部署一個模型，例如 `gpt-4o-mini`。
1. 在專案的 <strong>總覽</strong> 頁面，複製 <strong>端點</strong> 及 **API 金鑰**。
1. 將端點值填入 `.env` 檔的 `AZURE_INFERENCE_ENDPOINT`，金鑰值填入 `AZURE_INFERENCE_CREDENTIAL`。

## 離線 / 本地提供者

如果你完全不想使用雲端訂閱，可以在自己的裝置上執行相容的開放模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微軟的裝置端運行時。它會自動選擇最佳執行提供者（NPU、GPU 或 CPU），並提供 OpenAI 相容端點，因此你可以用本課程中大部分範例程式碼，只需極少更動。參考 [Foundry Local 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 開始，或使用 `winget install Microsoft.FoundryLocal`（Windows）/ `brew install microsoft/foundrylocal/foundrylocal`（macOS）安裝。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 一個熱門的離線本地執行替代方案，可用於運行 Llama、Phi、Mistral 及 Gemma 等開放模型。


請參閱 [課程 19：使用 SLMs 建構](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) 以取得使用兩個選項的實作範例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->