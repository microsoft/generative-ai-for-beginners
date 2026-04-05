# 選擇與設定 LLM 供應商 🔑

作業**可能**也會設定為透過支援的服務供應商（如 OpenAI、Azure 或 Hugging Face）對一個或多個大型語言模型（LLM）部署進行操作。這些供應商提供一個 _託管端點_（API），我們可以使用正確的憑證（API 金鑰或令牌）以程式化方式存取。在本課程中，我們討論以下供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供多樣化模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，專注於企業級的 OpenAI 模型。
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供開源模型與推理伺服器。

**您需要使用自己的帳號來完成這些練習**。作業為選擇性，您可以根據興趣選擇設定其中一個、全部或不設定任何供應商。以下是註冊的部分指引：

| 註冊 | 費用 | API 金鑰 | 操作介面 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [專案基礎](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需程式碼，網頁介面](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須事先申請存取權](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

請依照以下指示來 _設定_ 本儲存庫以使用不同供應商。需要特定供應商的作業檔名會包含以下標籤：

- `aoai` - 需要 Azure OpenAI 端點與金鑰
- `oai` - 需要 OpenAI 端點與金鑰
- `hf` - 需要 Hugging Face 令牌

您可以設定一個、沒有或全部供應商。相關作業若缺少憑證將直接報錯。

## 建立 `.env` 檔案

我們假設您已閱讀上述指引並完成相關供應商的註冊，且取得所需的認證憑證（API_KEY 或令牌）。以 Azure OpenAI 為例，我們假設您也已部署有效的 Azure OpenAI 服務（端點），並至少部署一個 GPT 模型用於聊天完成。

下一步是設定您的 **本地環境變數**，步驟如下：

1. 在根目錄尋找 `.env.copy` 檔案，內容應類似：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # 預設已設定！
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下指令將該檔案複製為 `.env`。此檔案已被 _gitignore_，可確保秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節說明填入對應值（替換 `=` 右側的佔位符）。

4. （選擇性）若您使用 GitHub Codespaces，可選擇將環境變數儲存為與本儲存庫關聯的 _Codespaces 秘密_。如此一來，您不必設定本地 .env 檔案。**但請注意，此選項僅適用於 GitHub Codespaces。** 若使用 Docker Desktop，仍需設定 .env 檔案。

## 填寫 `.env` 檔案

快速了解變數名稱及其代表意義：

| 變數名稱  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 您在個人資料中設定的使用者存取令牌 |
| OPENAI_API_KEY | 非 Azure OpenAI 端點的服務授權金鑰 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型部署端點 |
| | |

注意：最後兩個 Azure OpenAI 變數分別對應聊天完成（文字生成）與向量搜尋（嵌入）預設模型。設定指示會在相關作業中說明。

## 從 Azure 入口網站設定

Azure OpenAI 端點與金鑰可在 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，以下開始說明。

1. 前往 [Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點選側邊欄（左側選單）的 **金鑰與端點** 選項。
1. 點選 **顯示金鑰**，您會看到 KEY 1、KEY 2 與端點。
1. 將 KEY 1 的值用於 AZURE_OPENAI_API_KEY
1. 將端點值用於 AZURE_OPENAI_ENDPOINT

接著，我們需要取得已部署模型的端點。

1. 點選 Azure OpenAI 資源側邊欄（左選單）的 **模型部署** 選項。
1. 在目的頁面點選 **管理部署**

這會帶您到 Azure OpenAI Studio 網站，我們會在那裡找到其他值，如下所述。

## 從 Studio 設定 Azure

1. 依上述說明，從您的資源導向 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點選左側邊欄的 **部署** 標籤，查看目前已部署的模型。
1. 若尚未部署所需模型，請使用 **建立新部署** 來部署。
1. 您需要一個 _文字生成_ 模型，我們建議：**gpt-35-turbo**
1. 您需要一個 _文字嵌入_ 模型，我們建議：**text-embedding-ada-002**

現在更新環境變數以反映所使用的 _部署名稱_。通常部署名稱與模型名稱相同，除非您有明確更改。例如，您可能會有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成後別忘了儲存 .env 檔案**。您可以關閉檔案並回到執行筆記本的指示。

## 從個人資料設定 OpenAI

您的 OpenAI API 金鑰可在您的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。若尚無帳戶，您可以註冊並建立 API 金鑰。取得金鑰後，請將其填入 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

## 從個人資料設定 Hugging Face

您的 Hugging Face 令牌可在個人資料的 [存取令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 頁面找到。請勿公開或分享這些令牌。建議為本專案用途建立新的令牌，並將其複製到 `.env` 檔案中的 `HUGGING_FACE_API_KEY` 變數。_注意：_ 這技術上不是 API 金鑰，但用於認證，因此我們保持此命名慣例以維持一致性。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->