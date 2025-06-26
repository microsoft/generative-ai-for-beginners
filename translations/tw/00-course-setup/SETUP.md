<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:10:27+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tw"
}
-->
# 設置開發環境

我們使用[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)設置了這個存儲庫和課程，該容器擁有一個通用運行時，可以支持Python3、.NET、Node.js和Java的開發。相關配置在此存儲庫根目錄的`.devcontainer/`文件夾中的`devcontainer.json`文件中定義。

要啟動開發容器，可以在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（用於雲端託管運行時）或[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（用於本地設備託管運行時）中啟動它。閱讀[這份文檔](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)以了解更多有關開發容器如何在VS Code中工作的詳細信息。

> [!TIP]  
> 我們建議使用GitHub Codespaces以便快速啟動，並且所需努力最小。它為個人賬戶提供了豐厚的[免費使用配額](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超時](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或刪除不活動的codespaces，以最大化您的配額使用。

## 1. 執行作業

每個課程都會有_可選_作業，這些作業可能會以一種或多種編程語言提供，包括：Python、.NET/C#、Java和JavaScript/TypeScript。本節提供了執行這些作業的通用指導。

### 1.1 Python 作業

Python作業以應用程序形式（`.py`文件）或Jupyter筆記本（`.ipynb`文件）提供。
- 要運行筆記本，在Visual Studio Code中打開它，然後點擊_選擇內核_（右上角）並選擇顯示的默認Python 3選項。現在可以選擇_全部運行_來執行筆記本。
- 要從命令行運行Python應用程序，請遵循作業特定的指導，以確保選擇正確的文件並提供所需的參數。

## 2. 配置提供者

作業**可能**也會設置為通過支持的服務提供者（如OpenAI、Azure或Hugging Face）來處理一個或多個大型語言模型（LLM）部署。這些提供了一個_託管端點_（API），我們可以通過正確的憑據（API密鑰或令牌）以編程方式訪問。在本課程中，我們討論這些提供者：

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 擁有多樣化的模型，包括核心的GPT系列。
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) 專注於企業準備的OpenAI模型。
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 提供開源模型和推理服務器。

**您將需要使用自己的賬戶來進行這些練習**。作業是可選的，因此您可以根據興趣選擇設置一個、全部或不設置任何提供者。註冊的一些指導：

| 註冊 | 成本 | API Key | Playground | 評論 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [定價](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於項目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無需代碼，網頁版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 可用多個模型 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [定價](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [必須提前申請訪問](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [定價](https://huggingface.co/pricing) | [訪問令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 有限的模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照下面的指導來_配置_此存儲庫以與不同的提供者一起使用。需要特定提供者的作業將在其文件名中包含以下標籤之一：
- `aoai` - 需要Azure OpenAI端點，密鑰
- `oai` - 需要OpenAI端點，密鑰
- `hf` - 需要Hugging Face令牌

您可以配置一個、沒有或所有提供者。相關作業將因缺少憑據而簡單地報錯。

### 2.1. 創建`.env`文件

我們假設您已經閱讀了上述指導，並與相關提供者註冊並獲得了所需的身份驗證憑據（API_KEY或令牌）。在Azure OpenAI的情況下，我們假設您還擁有一個有效的Azure OpenAI服務部署（端點），其中至少有一個GPT模型已部署用於聊天完成。

下一步是配置您的**本地環境變量**，如下所示：

1. 在根目錄中查找一個`.env.copy`文件，該文件的內容應如下所示：

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

2. 使用下面的命令將該文件複製到`.env`。此文件已被_gitignore_，以保護秘密。

   ```bash
   cp .env.copy .env
   ```

3. 按照下一節所述填寫值（替換`=`右側的佔位符）。

4. （可選）如果您使用GitHub Codespaces，您可以選擇將環境變量保存為與此存儲庫關聯的_Codespaces secrets_。在這種情況下，您不需要設置本地.env文件。**但請注意，這個選項僅在您使用GitHub Codespaces時有效。** 如果您改用Docker Desktop，您仍然需要設置.env文件。

### 2.2. 填寫`.env`文件

讓我們快速查看變量名稱，以了解它們代表什麼：

| 變量 | 描述 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是您在個人資料中設置的用戶訪問令牌 |
| OPENAI_API_KEY | 這是用於非Azure OpenAI端點的服務授權密鑰 |
| AZURE_OPENAI_API_KEY | 這是用於該服務的授權密鑰 |
| AZURE_OPENAI_ENDPOINT | 這是Azure OpenAI資源的已部署端點 |
| AZURE_OPENAI_DEPLOYMENT | 這是_文本生成_模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 這是_文本嵌入_模型的部署端點 |
| | |

注意：最後兩個Azure OpenAI變量分別反映了一個默認的聊天完成（文本生成）和向量搜索（嵌入）的模型。設置它們的指導將在相關作業中定義。

### 2.3 配置Azure：從Portal

Azure OpenAI端點和密鑰值可以在[Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)中找到，因此讓我們從這裡開始。

1. 進入[Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
2. 點擊側邊欄（左側菜單）中的**Keys and Endpoint**選項。
3. 點擊**Show Keys** - 您應該看到以下內容：KEY 1、KEY 2和Endpoint。
4. 使用KEY 1的值作為AZURE_OPENAI_API_KEY
5. 使用Endpoint的值作為AZURE_OPENAI_ENDPOINT

接下來，我們需要獲得已部署模型的端點。

1. 點擊Azure OpenAI資源的側邊欄（左側菜單）中的**Model deployments**選項。
2. 在目標頁面中，點擊**Manage Deployments**

這將帶您進入Azure OpenAI Studio網站，我們將在這裡找到其他值，如下所述。

### 2.4 配置Azure：從Studio

1. 按上述描述從您的資源導航到[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
2. 點擊**Deployments**選項卡（側邊欄，左側）以查看當前部署的模型。
3. 如果您的目標模型尚未部署，請使用**Create new deployment**來部署它。
4. 您將需要一個_文本生成_模型 - 我們推薦：**gpt-35-turbo**
5. 您將需要一個_文本嵌入_模型 - 我們推薦**text-embedding-ada-002**

現在更新環境變量以反映所用的_Deployment name_。這通常與模型名稱相同，除非您明確更改它。因此，作為示例，您可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成後別忘了保存.env文件**。您現在可以退出文件並返回運行筆記本的指導。

### 2.5 配置OpenAI：從個人資料

您的OpenAI API密鑰可以在您的[OpenAI賬戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果您還沒有，可以註冊一個賬戶並創建一個API密鑰。一旦您擁有密鑰，您可以用它來填寫`.env`文件中的`OPENAI_API_KEY`變量。

### 2.6 配置Hugging Face：從個人資料

您的Hugging Face令牌可以在您的個人資料中的[訪問令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)下找到。不要公開發布或分享這些信息。相反，為此項目創建一個新令牌，並將其複製到`.env`文件中的`HUGGING_FACE_API_KEY`變量下。_注意：_這技術上不是API密鑰，但用於身份驗證，因此我們保持這個命名約定以保持一致性。

**免責聲明**：
本文檔已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始文件的母語版本視為權威來源。對於關鍵信息，建議使用專業人工翻譯。對於使用此翻譯而引起的任何誤解或誤譯，我們不承擔責任。