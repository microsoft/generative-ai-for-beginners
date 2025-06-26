<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:09:50+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hk"
}
-->
# 設置開發環境

我們設置了這個資料庫和課程，使用一個[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，這個容器擁有一個通用運行時，可以支援 Python3、.NET、Node.js 和 Java 的開發。相關的配置定義在這個資料庫根目錄下的 `devcontainer.json` 文件中，位於 `.devcontainer/` 資料夾內。

要激活開發容器，可以在 [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（用於雲端運行時）或 [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（用於本地設備運行時）中啟動它。閱讀[這份文件](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)了解有關開發容器在 VS Code 中如何運作的更多細節。

> [!TIP]  
> 我們建議使用 GitHub Codespaces 來快速開始並減少麻煩。它為個人帳戶提供了慷慨的[免費使用額度](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超時](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或刪除不活躍的 codespaces，以最大化配額使用。

## 1. 執行作業

每個課程都會有_可選的_作業，這些作業可能會以一種或多種程式語言提供，包括：Python、.NET/C#、Java 和 JavaScript/TypeScript。本節提供了有關執行這些作業的一般指導。

### 1.1 Python 作業

Python 作業可以作為應用程序 (`.py` 文件) 或 Jupyter 筆記本 (`.ipynb` 文件) 提供。
- 要運行筆記本，在 Visual Studio Code 中打開它，然後點擊_選擇內核_（在右上角），選擇顯示的默認 Python 3 選項。現在可以選擇_全部運行_來執行筆記本。
- 要從命令行運行 Python 應用程序，請遵循作業特定的指導，以確保選擇正確的文件並提供所需的參數。

## 2. 配置提供者

作業**可能**還設置為通過支援的服務提供者（如 OpenAI、Azure 或 Hugging Face）對一個或多個大型語言模型（LLM）部署進行操作。這些提供了一個_託管端點_（API），我們可以使用正確的憑證（API 密鑰或令牌）以程式化方式訪問。在這個課程中，我們討論這些提供者：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供多種模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，專注於企業準備的 OpenAI 模型。
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供開源模型和推理服務器。

**您將需要使用自己的帳戶來進行這些練習**。作業是可選的，因此您可以根據自己的興趣選擇設置一個、全部或不設置任何提供者。以下是註冊的一些指導：

| 註冊 | 成本 | API 密鑰 | 操作界面 | 備註 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於項目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需編碼，網頁](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 提供多種模型 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須提前申請訪問權限](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [訪問令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 提供有限的模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照下面的指示來_配置_這個資料庫，以便與不同的提供者一起使用。需要特定提供者的作業將在其文件名中包含以下標籤之一：
 - `aoai` - 需要 Azure OpenAI 端點和密鑰
 - `oai` - 需要 OpenAI 端點和密鑰
 - `hf` - 需要 Hugging Face 令牌

您可以配置一個、沒有或全部提供者。相關作業將因缺少憑證而報錯。

### 2.1. 創建 `.env` 文件

我們假設您已經閱讀了上面的指導，並註冊了相關的提供者，獲得了所需的身份驗證憑證（API_KEY 或令牌）。在 Azure OpenAI 的情況下，我們假設您還擁有一個有效的 Azure OpenAI 服務部署（端點），並部署了至少一個 GPT 模型以進行聊天完成。

下一步是配置您的**本地環境變數**如下：

1. 在根目錄中查找一個 `.env.copy` 文件，內容應如下所示：

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

2. 使用下面的命令將該文件複製到 `.env`。此文件是 _gitignore-d_ 的，確保秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 填寫值（替換 `=` 右側的佔位符），如下一節所述。

3. （選項）如果您使用 GitHub Codespaces，您可以選擇將環境變數保存為與此資料庫關聯的 _Codespaces 秘密_。在這種情況下，您不需要設置本地 .env 文件。**但請注意，此選項僅在您使用 GitHub Codespaces 時有效。** 如果您使用 Docker Desktop，仍需設置 .env 文件。

### 2.2. 填寫 `.env` 文件

讓我們快速了解變數名稱，以理解它們代表什麼：

| 變數  | 描述  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是您在個人資料中設置的用戶訪問令牌 |
| OPENAI_API_KEY | 這是用於非 Azure OpenAI 端點的服務授權密鑰 |
| AZURE_OPENAI_API_KEY | 這是使用該服務的授權密鑰 |
| AZURE_OPENAI_ENDPOINT | 這是 Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | 這是_文本生成_模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 這是_文本嵌入_模型的部署端點 |
| | |

注意：最後兩個 Azure OpenAI 變數分別反映了默認的聊天完成（文本生成）和向量搜索（嵌入）模型。設置它們的指導將在相關作業中定義。

### 2.3 配置 Azure：從門戶

Azure OpenAI 端點和密鑰值可以在 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 中找到，讓我們從這裡開始。

1. 進入 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點擊側邊欄（左側菜單）中的 **密鑰和端點** 選項。
1. 點擊 **顯示密鑰** - 您應該看到以下內容：密鑰 1、密鑰 2 和端點。
1. 使用密鑰 1 的值作為 AZURE_OPENAI_API_KEY
1. 使用端點的值作為 AZURE_OPENAI_ENDPOINT

接下來，我們需要特定模型的端點。

1. 點擊 Azure OpenAI 資源的側邊欄（左側菜單）中的 **模型部署** 選項。
1. 在目標頁面中，點擊 **管理部署**

這將帶您到 Azure OpenAI Studio 網站，我們將在這裡找到其他值，如下所述。

### 2.4 配置 Azure：從 Studio

1. 從您的資源導航到 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) ，如上所述。
1. 點擊 **部署** 標籤（側邊欄，左側）以查看當前部署的模型。
1. 如果您需要的模型未部署，使用 **創建新部署** 來部署它。
1. 您將需要一個_文本生成_模型 - 我們推薦：**gpt-35-turbo**
1. 您將需要一個_文本嵌入_模型 - 我們推薦 **text-embedding-ada-002**

現在更新環境變數以反映所使用的_部署名稱_。這通常與模型名稱相同，除非您顯式更改它。因此，作為示例，您可能會有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成後不要忘記保存 .env 文件**。現在您可以退出該文件，返回到運行筆記本的指導。

### 2.5 配置 OpenAI：從個人資料

您的 OpenAI API 密鑰可以在您的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。如果您沒有，可以註冊一個帳戶並創建一個 API 密鑰。一旦您擁有密鑰，可以用它來填寫 `.env` 文件中的 `OPENAI_API_KEY` 變數。

### 2.6 配置 Hugging Face：從個人資料

您的 Hugging Face 令牌可以在個人資料的[訪問令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)下找到。不要公開發佈或分享這些。相反，為此項目創建一個新令牌，並將其複製到 `.env` 文件中的 `HUGGING_FACE_API_KEY` 變數下。_注意：_這技術上不是 API 密鑰，但用於身份驗證，因此我們保持這種命名約定以保持一致性。

**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤釋承擔責任。