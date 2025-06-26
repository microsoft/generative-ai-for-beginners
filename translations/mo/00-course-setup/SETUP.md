<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:09:14+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "mo"
}
-->
# 設置您的開發環境

我們使用[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)設置了這個存儲庫和課程，該容器具有支持 Python3、.NET、Node.js 和 Java 開發的通用運行時。相關配置在存儲庫根目錄的 `devcontainer.json` 文件中定義，位於 `.devcontainer/` 文件夾中。

要激活開發容器，請在 [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（雲端托管運行時）或 [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（本地設備托管運行時）中啟動它。閱讀[這份文檔](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)了解在 VS Code 中開發容器的工作原理。

> [!TIP]  
> 我們建議使用 GitHub Codespaces 以快速啟動，並且只需最少的努力。它為個人賬戶提供慷慨的[免費使用配額](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超時](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或刪除不活躍的代碼空間，最大化配額使用。

## 1. 執行作業

每節課都有 _可選_ 作業，可能提供一種或多種編程語言，包括：Python、.NET/C#、Java 和 JavaScript/TypeScript。本節提供執行這些作業的通用指導。

### 1.1 Python 作業

Python 作業提供為應用程序 (`.py` 文件) 或 Jupyter 筆記本 (`.ipynb` 文件)。
- 要運行筆記本，請在 Visual Studio Code 中打開它，然後點擊 _選擇內核_（右上角），並選擇顯示的默認 Python 3 選項。您現在可以 _運行全部_ 來執行筆記本。
- 要從命令行運行 Python 應用程序，請遵循作業特定的指導，以確保您選擇正確的文件並提供所需的參數。

## 2. 配置提供商

作業 **可能** 還會設置為通過支持的服務提供商（如 OpenAI、Azure 或 Hugging Face）對一個或多個大型語言模型（LLM）部署進行工作。這些提供一個 _托管端點_（API），我們可以使用正確的憑證（API 密鑰或令牌）以編程方式訪問。在本課程中，我們討論這些提供商：

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 擁有多樣化的模型，包括核心 GPT 系列。
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) 專注於企業就緒性的 OpenAI 模型。
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 提供開源模型和推理服務器。

**您將需要使用自己的賬戶進行這些練習**。作業是可選的，因此您可以根據自己的興趣選擇設置一個、全部或不設置任何提供商。以下是一些註冊指南：

| 註冊 | 成本 | API 密鑰 | 操作台 | 評論 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於項目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無代碼，網頁](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 可用多個模型 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須提前申請訪問](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [訪問令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照下面的指導為不同的提供商 _配置_ 此存儲庫。需要特定提供商的作業將在其文件名中包含以下標籤之一：
- `aoai` - 需要 Azure OpenAI 端點、密鑰
- `oai` - 需要 OpenAI 端點、密鑰
- `hf` - 需要 Hugging Face 令牌

您可以配置一個、沒有或所有提供商。相關作業在缺少憑證時會出錯。

### 2.1. 創建 `.env` 文件

我們假設您已經閱讀了上面的指導，並註冊了相關提供商，並獲得了所需的身份驗證憑證（API_KEY 或令牌）。在 Azure OpenAI 的情況下，我們假設您也有一個有效的 Azure OpenAI 服務部署（端點），並至少部署了一個 GPT 模型以完成聊天。

下一步是配置您的 **本地環境變量** 如下：

1. 在根文件夾中尋找一個 `.env.copy` 文件，該文件應具有如下內容：

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

2. 使用以下命令將該文件複製到 `.env`。此文件已被 _gitignore_，以確保秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 按照下一節所述填寫值（替換 `=` 右側的占位符）。

3. （選項）如果您使用 GitHub Codespaces，您可以選擇將環境變量保存為與此存儲庫相關的 _Codespaces secrets_。在這種情況下，您不需要設置本地 .env 文件。**但是，請注意，此選項僅在您使用 GitHub Codespaces 時有效。** 如果您使用 Docker Desktop，您仍然需要設置 .env 文件。

### 2.2. 填充 `.env` 文件

讓我們快速查看變量名稱以了解它們代表什麼：

| 變量 | 描述 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是您在個人資料中設置的用戶訪問令牌 |
| OPENAI_API_KEY | 這是使用非 Azure OpenAI 端點服務的授權密鑰 |
| AZURE_OPENAI_API_KEY | 這是使用該服務的授權密鑰 |
| AZURE_OPENAI_ENDPOINT | 這是 Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | 這是 _文本生成_ 模型部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 這是 _文本嵌入_ 模型部署端點 |
| | |

注意：最後兩個 Azure OpenAI 變量分別反映了聊天完成（文本生成）和向量搜索（嵌入）的默認模型。設置它們的指導將在相關作業中定義。

### 2.3 配置 Azure：從 Portal

Azure OpenAI 端點和密鑰值將在 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 中找到，所以我們從這裡開始。

1. 進入 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點擊側邊欄（左側菜單）中的 **密鑰和端點** 選項。
1. 點擊 **顯示密鑰** - 您應該看到以下內容：KEY 1、KEY 2 和端點。
1. 使用 KEY 1 值作為 AZURE_OPENAI_API_KEY
1. 使用端點值作為 AZURE_OPENAI_ENDPOINT

接下來，我們需要為我們部署的特定模型提供端點。

1. 點擊側邊欄（左側菜單）中的 **模型部署** 選項以獲取 Azure OpenAI 資源。
1. 在目標頁面中，點擊 **管理部署**

這將帶您進入 Azure OpenAI Studio 網站，我們將在下面描述的其他值。

### 2.4 配置 Azure：從 Studio

1. 按上述描述從您的資源導航到 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊 **部署** 標籤（側邊欄，左側）查看當前部署的模型。
1. 如果您想要的模型未部署，請使用 **創建新部署** 來部署它。
1. 您將需要一個 _文本生成_ 模型 - 我們推薦：**gpt-35-turbo**
1. 您將需要一個 _文本嵌入_ 模型 - 我們推薦 **text-embedding-ada-002**

現在更新環境變量以反映使用的 _部署名稱_。這通常與模型名稱相同，除非您明確更改它。所以，作為示例，您可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成後不要忘記保存 .env 文件**。您現在可以退出文件並返回運行筆記本的指導。

### 2.5 配置 OpenAI：從個人資料

您的 OpenAI API 密鑰可以在您的 [OpenAI 賬戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果您沒有，可以註冊一個賬戶並創建一個 API 密鑰。一旦您擁有密鑰，您可以使用它來填充 `.env` 文件中的 `OPENAI_API_KEY` 變量。

### 2.6 配置 Hugging Face：從個人資料

您的 Hugging Face 令牌可以在個人資料的 [訪問令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 下找到。不要公開發佈或分享這些。相反，為此項目創建一個新令牌，並將其複製到 `.env` 文件中的 `HUGGING_FACE_API_KEY` 變量下。_注意：_ 這在技術上不是 API 密鑰，但用於身份驗證，所以我們保持這種命名慣例以保持一致性。

**免責聲明**：
本文檔已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯可能引起的任何誤解或誤釋不承擔責任。