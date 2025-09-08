<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T14:55:23+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "tw"
}
-->
# 選擇與設定 LLM 供應商 🔑

作業**也可以**設定為透過支援的服務供應商（如 OpenAI、Azure 或 Hugging Face）來使用一個或多個大型語言模型（LLM）部署。這些供應商會提供一個_託管端點_（API），只要有正確的憑證（API 金鑰或權杖），我們就能以程式方式存取。在本課程中，我們會討論以下供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)：提供多種模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)：專注於企業級的 OpenAI 模型
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)：開源模型與推論伺服器

**這些練習需要你自行申請帳號。** 作業是選修的，你可以依照自己的興趣選擇設定其中一個、全部或都不設定。以下是註冊的相關說明：

| 註冊 | 費用 | API 金鑰 | Playground | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [專案型](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [免程式碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可選 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [需事先申請存取權](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取權杖](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 支援的模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

請依照下方指示，_設定_本儲存庫以搭配不同供應商使用。需要特定供應商的作業，檔名會包含以下其中一個標籤：

- `aoai` - 需要 Azure OpenAI 端點與金鑰
- `oai` - 需要 OpenAI 端點與金鑰
- `hf` - 需要 Hugging Face 權杖

你可以設定其中一個、全部或都不設定。相關作業如果缺少憑證，執行時會直接出錯。

## 建立 `.env` 檔案

我們假設你已經閱讀上方說明，並完成相關供應商的註冊，取得所需的認證憑證（API_KEY 或權杖）。如果是 Azure OpenAI，還需要有一個有效的 Azure OpenAI 服務部署（端點），且至少有一個 GPT 模型用於聊天補全。

下一步是依照下列方式設定你的**本地環境變數**：

1. 在根目錄找到 `.env.copy` 檔案，內容大致如下：

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 用下方指令將該檔案複製成 `.env`。此檔案已被 _gitignore_，可確保機密安全。

   ```bash
   cp .env.copy .env
   ```

3. 依照下一節說明，填入各項值（將 `=` 右側的佔位符替換成你的資料）。

4. （選用）如果你使用 GitHub Codespaces，可以選擇將環境變數儲存為 _Codespaces secrets_，與此儲存庫綁定。這樣就不需要本地 .env 檔案。**但請注意，這個選項僅適用於 GitHub Codespaces。** 如果你改用 Docker Desktop，仍需自行設定 .env 檔案。

## 填入 `.env` 檔案

我們來快速看一下各個變數名稱，了解它們的用途：

| 變數  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在個人檔案設定的存取權杖 |
| OPENAI_API_KEY | 用於非 Azure OpenAI 端點的授權金鑰 |
| AZURE_OPENAI_API_KEY | 用於該服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_模型的部署端點 |
| | |

注意：最後兩個 Azure OpenAI 變數分別代表預設的聊天補全（文字生成）與向量搜尋（嵌入）模型。設定方式會在相關作業中說明。

## 設定 Azure：從 Portal 取得

Azure OpenAI 的端點與金鑰可以在 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，請依下列步驟操作。

1. 前往 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點選側邊欄（左側選單）的 **Keys and Endpoint** 選項。
1. 點選 **Show Keys**，你會看到：KEY 1、KEY 2 和 Endpoint。
1. 將 KEY 1 的值填入 AZURE_OPENAI_API_KEY
1. 將 Endpoint 的值填入 AZURE_OPENAI_ENDPOINT

接下來，我們需要取得已部署模型的端點。

1. 在 Azure OpenAI 資源的側邊欄（左側選單）點選 **Model deployments**。
1. 在目的頁面點選 **Manage Deployments**

這會帶你進入 Azure OpenAI Studio 網站，接下來依照下方說明取得其他值。

## 設定 Azure：從 Studio 取得

1. 依上述方式，從你的資源前往 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點選側邊欄（左側）的 **Deployments** 分頁，查看目前已部署的模型。
1. 如果你想要的模型尚未部署，請用 **Create new deployment** 來部署。
1. 你需要一個 _文字生成_ 模型，建議選用：**gpt-35-turbo**
1. 你需要一個 _文字嵌入_ 模型，建議選用 **text-embedding-ada-002**

現在請將環境變數更新為你設定的 _Deployment name_。通常會與模型名稱相同，除非你有特別修改。例如：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**記得儲存 .env 檔案**。完成後即可離開此檔案，回到執行 notebook 的指示。

## 設定 OpenAI：從個人檔案取得

你的 OpenAI API 金鑰可以在 [OpenAI 帳號](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 找到。如果還沒有，可以註冊帳號並建立 API 金鑰。取得金鑰後，將其填入 `.env` 檔案的 `OPENAI_API_KEY` 變數。

## 設定 Hugging Face：從個人檔案取得

你的 Hugging Face 權杖可以在個人檔案的 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 頁面找到。請勿公開或分享這些權杖。建議為本專案建立一個新權杖，並將其填入 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數。_注意：_ 嚴格來說這不是 API 金鑰，但因為用於認證，所以我們沿用這個命名方式以保持一致。

---

**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。