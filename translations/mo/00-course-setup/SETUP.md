<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:23:51+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "mo"
}
-->
# 設定您的開發環境

我們使用一個包含通用執行環境的[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)來設置此儲存庫和課程，支援 Python3、.NET、Node.js 及 Java 開發。相關設定定義在位於此儲存庫根目錄 `.devcontainer/` 資料夾中的 `devcontainer.json` 檔案。

要啟動開發容器，請在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（雲端執行環境）或[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（本地裝置執行環境）中啟動。詳細了解 VS Code 中開發容器的運作方式，請參閱[此文件](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)。

> [!TIP]  
> 我們建議使用 GitHub Codespaces 以快速且輕鬆地開始。它為個人帳戶提供慷慨的[免費使用額度](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。您可以設定[逾時](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)來停止或刪除非活動的 codespaces，以最大化使用額度。

## 1. 執行作業

每堂課都會有 _可選_ 的作業，可能會以一種或多種程式語言提供，包括：Python、.NET/C#、Java 和 JavaScript/TypeScript。本節提供執行這些作業的一般指引。

### 1.1 Python 作業

Python 作業會以應用程式（`.py` 檔案）或 Jupyter 筆記本（`.ipynb` 檔案）形式提供。  
- 若要執行筆記本，請在 Visual Studio Code 中開啟，然後點選右上角的 _選擇核心_，選擇預設的 Python 3 選項。接著即可使用 _全部執行_ 來執行筆記本。  
- 若要從命令列執行 Python 應用程式，請依照作業特定指示，確保選擇正確的檔案並提供所需參數。

## 2. 設定服務提供者

作業**可能**會設定為透過支援的服務提供者（如 OpenAI、Azure 或 Hugging Face）連接一個或多個大型語言模型（LLM）部署。這些提供一個可程式化存取的 _託管端點_（API），需使用正確的認證（API 金鑰或令牌）。本課程中，我們會討論以下提供者：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，包含多種模型，包括核心 GPT 系列。  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，專注於企業級的 OpenAI 模型。  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供開源模型與推理伺服器。

**您需要使用自己的帳戶來完成這些練習**。作業為可選，您可以根據興趣選擇設定其中一個、全部或不設定任何提供者。以下是註冊的相關說明：

| 註冊 | 費用 | API 金鑰 | Playground | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [專案金鑰](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需程式碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [需事先申請存取權](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

請依照以下指示，為此儲存庫設定不同的提供者。需要特定提供者的作業，其檔名會包含以下標籤之一：  
 - `aoai` - 需要 Azure OpenAI 端點與金鑰  
 - `oai` - 需要 OpenAI 端點與金鑰  
 - `hf` - 需要 Hugging Face 令牌  

您可以設定一個、全部或不設定任何提供者。缺少認證的相關作業將會出錯。

### 2.1. 建立 `.env` 檔案

假設您已閱讀上述指引，並已在相關提供者註冊，取得所需的認證（API_KEY 或令牌）。若是 Azure OpenAI，則假設您也已部署有效的 Azure OpenAI 服務（端點），並至少部署一個用於聊天完成的 GPT 模型。

接下來請設定您的**本地環境變數**，步驟如下：

1. 在根目錄尋找 `.env.copy` 檔案，內容應類似以下：

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

2. 使用以下指令將該檔案複製為 `.env`。此檔案已被加入 `.gitignore`，可確保秘密資訊安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一節說明，填入對應的值（替換 `=` 右側的佔位符）。

3. （選擇性）若您使用 GitHub Codespaces，可選擇將環境變數儲存為與此儲存庫關聯的 _Codespaces secrets_。如此一來，您就不必設定本地 `.env` 檔案。**但請注意，此選項僅適用於 GitHub Codespaces。** 若使用 Docker Desktop，仍需設定 `.env` 檔案。

### 2.2. 填寫 `.env` 檔案

快速了解變數名稱及其代表意義：

| 變數名稱 | 說明 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 您在個人資料中設定的使用者存取令牌 |
| OPENAI_API_KEY | 用於非 Azure OpenAI 端點的授權金鑰 |
| AZURE_OPENAI_API_KEY | 用於 Azure OpenAI 服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | _文字生成_ 模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文字嵌入_ 模型的部署端點 |
| | |

注意：最後兩個 Azure OpenAI 變數分別對應聊天完成（文字生成）和向量搜尋（嵌入）的預設模型。設定說明會在相關作業中提供。

### 2.3 從 Azure 入口網站設定

Azure OpenAI 的端點與金鑰可在[Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)找到，請從這裡開始。

1. 前往[Azure 入口網站](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. 點選側邊欄（左側選單）中的 **Keys and Endpoint** 選項。  
3. 點選 **Show Keys**，您會看到 KEY 1、KEY 2 和 Endpoint。  
4. 將 KEY 1 的值用於 `AZURE_OPENAI_API_KEY`。  
5. 將 Endpoint 的值用於 `AZURE_OPENAI_ENDPOINT`。

接著，我們需要取得已部署模型的端點。

1. 點選 Azure OpenAI 資源側邊欄的 **Model deployments** 選項。  
2. 在目的頁面點選 **Manage Deployments**。

這會帶您到 Azure OpenAI Studio 網站，接下來會找到其他所需的值。

### 2.4 從 Studio 設定 Azure

1. 依上述說明，從您的資源進入 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。  
2. 點選左側邊欄的 **Deployments** 標籤，查看目前已部署的模型。  
3. 若尚未部署所需模型，請使用 **Create new deployment** 來部署。  
4. 您需要一個 _文字生成_ 模型，我們推薦：**gpt-35-turbo**。  
5. 您需要一個 _文字嵌入_ 模型，我們推薦：**text-embedding-ada-002**。

接著更新環境變數，反映所使用的 _部署名稱_。通常部署名稱與模型名稱相同，除非您有特別更改。例如，您可能會有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成後別忘了儲存 `.env` 檔案**。儲存後即可關閉檔案，回到執行筆記本的指示。

### 2.5 從個人資料設定 OpenAI

您的 OpenAI API 金鑰可在您的[OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。若尚未擁有帳戶，請註冊並建立 API 金鑰。取得金鑰後，請將其填入 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

### 2.6 從個人資料設定 Hugging Face

您的 Hugging Face 令牌可在個人資料的[存取令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)中找到。請勿公開或分享這些令牌。建議為此專案建立新的令牌，並將其複製到 `.env` 檔案中的 `HUGGING_FACE_API_KEY` 變數。_注意：_ 這技術上不是 API 金鑰，但用於認證，因此為保持一致性，我們仍使用此命名慣例。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。