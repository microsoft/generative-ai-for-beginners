<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T14:47:42+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "hk"
}
-->
# 選擇及設定 LLM 供應商 🔑

你可以選擇將作業設定為使用一個或多個大型語言模型（LLM）服務供應商，例如 OpenAI、Azure 或 Hugging Face。這些供應商會提供一個 _託管端點_（API），只要有正確的認證（API key 或 token），就可以用程式方式存取。在本課程中，我們會討論以下供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)：提供多款模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)：專為企業級應用而設的 OpenAI 模型
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)：提供開源模型及推理伺服器

**你需要用自己帳戶來做以下練習。** 這些作業是自選的，你可以按自己興趣選擇設定一個、全部，或者完全不設定任何供應商。以下是註冊時的一些建議：

| 註冊 | 收費 | API Key | Playground | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [收費詳情](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [以專案為單位](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需編碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 有多款模型可選 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [收費詳情](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [需預先申請存取權](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [收費詳情](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 支援的模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

請跟隨以下指示，_設定_ 這個 repository 以配合不同供應商使用。需要特定供應商的作業，會在檔案名稱中包含以下其中一個標籤：

- `aoai` - 需要 Azure OpenAI 端點及金鑰
- `oai` - 需要 OpenAI 端點及金鑰
- `hf` - 需要 Hugging Face token

你可以選擇設定一個、全部或完全不設定。相關作業如找不到認證資料，會直接出錯。

## 建立 `.env` 檔案

我們假設你已經閱讀了上面的指引，並已經在相關供應商註冊及取得所需的認證資料（API_KEY 或 token）。如果你用 Azure OpenAI，我們亦假設你已經有一個有效的 Azure OpenAI Service（端點），並已部署至少一個 GPT 模型作為 chat completion。

下一步是設定你的**本地環境變數**，方法如下：

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

2. 用以下指令將該檔案複製為 `.env`。這個檔案已被 _gitignore_，可以安全儲存機密資料。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節說明，填寫（即取代 `=` 右邊的 placeholder）。

4. （可選）如果你用 GitHub Codespaces，可以選擇將環境變數儲存為 _Codespaces secrets_，與這個 repository 綁定。這樣就不用再設定本地 .env 檔案。**但請注意，這個方法只適用於 GitHub Codespaces。** 如果你用 Docker Desktop，仍然需要設定 .env 檔案。

## 填寫 `.env` 檔案

我們簡單看看各個變數名稱，了解它們的用途：

| 變數  | 說明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在個人檔案設定的 access token |
| OPENAI_API_KEY | 用於非 Azure OpenAI 端點的授權金鑰 |
| AZURE_OPENAI_API_KEY | 用於該服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的已部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型的部署端點 |
| | |

注意：最後兩個 Azure OpenAI 變數分別對應 chat completion（文字生成）及向量搜尋（嵌入）的預設模型。設定方法會在相關作業中說明。

## 設定 Azure：從 Portal 取得

Azure OpenAI 的端點及金鑰可以在 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，步驟如下：

1. 前往 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 在側邊欄（左邊選單）點選 **Keys and Endpoint**
1. 點選 **Show Keys**，你會見到：KEY 1、KEY 2 及 Endpoint。
1. 將 KEY 1 的值填入 AZURE_OPENAI_API_KEY
1. 將 Endpoint 的值填入 AZURE_OPENAI_ENDPOINT

接下來，我們需要取得已部署模型的端點。

1. 在 Azure OpenAI 資源的側邊欄（左邊選單）點選 **Model deployments**
1. 在新頁面點選 **Manage Deployments**

這會帶你去 Azure OpenAI Studio 網站，以下會說明如何取得其他所需資料。

## 設定 Azure：從 Studio 取得

1. 按上面步驟，從你的資源進入 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點選側邊欄（左邊）**Deployments**，查看現有已部署模型
1. 如果你想用的模型未部署，可以用 **Create new deployment** 新增
1. 你需要一個 _text-generation_ 模型，建議用：**gpt-35-turbo**
1. 你需要一個 _text-embedding_ 模型，建議用 **text-embedding-ada-002**

然後，將環境變數更新為你用的 _Deployment name_。除非你有改名，否則通常跟模型名一樣。例如：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**記得儲存 .env 檔案！** 完成後可以關閉檔案，繼續跟著 notebook 的執行指引。

## 設定 OpenAI：從個人檔案取得

你的 OpenAI API key 可以在 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 找到。如果未有，可以註冊帳戶並建立 API key。取得後，將它填入 `.env` 檔案的 `OPENAI_API_KEY` 變數。

## 設定 Hugging Face：從個人檔案取得

你的 Hugging Face token 可以在個人檔案的 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 找到。請勿公開或分享這些 token。建議為這個專案新建一個 token，然後複製到 `.env` 檔案的 `HUGGING_FACE_API_KEY` 變數。_注意：_ 這 technically 不是 API key，但因為用來做認證，所以我們沿用這個命名方式以保持一致。

---

**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們力求準確，但請注意自動翻譯可能會有錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們不會對因使用本翻譯而產生的任何誤解或誤釋承擔責任。