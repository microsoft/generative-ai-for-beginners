<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:43:31+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hk"
}
-->
# 設置你的開發環境

我們使用[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)設置了這個倉庫和課程，它具有支持Python3、.NET、Node.js和Java開發的通用運行時。相關配置在此倉庫根目錄的`.devcontainer/`文件夾中的`devcontainer.json`文件中定義。

要激活開發容器，可以在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（雲端托管運行時）或在[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（本地設備托管運行時）中啟動它。請閱讀[此文檔](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)以了解VS Code中開發容器的工作原理。

> [!TIP]  
> 我們推薦使用GitHub Codespaces以便快速開始並減少努力。它為個人賬戶提供慷慨的[免費使用配額](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超時](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或刪除不活躍的codespaces，以最大化你的配額使用。

## 1. 執行作業

每節課將有_可選_作業，可能以一種或多種編程語言提供，包括：Python、.NET/C#、Java和JavaScript/TypeScript。本節提供執行這些作業的通用指導。

### 1.1 Python作業

Python作業要么以應用程序形式提供（`.py`文件），要么以Jupyter筆記本形式提供（`.ipynb`文件）。
- 要運行筆記本，請在Visual Studio Code中打開它，然後點擊_選擇內核_（右上角），選擇顯示的默認Python 3選項。你現在可以_運行所有_來執行筆記本。
- 要從命令行運行Python應用程序，請遵循作業特定的指示，以確保選擇正確的文件並提供所需的參數。

## 2. 配置供應商

作業**可能**也被設置為通過支持的服務供應商（如OpenAI、Azure或Hugging Face）在一個或多個大型語言模型（LLM）部署上工作。這些提供一個_托管端點_（API），我們可以用正確的憑證（API密鑰或令牌）以編程方式訪問。在這門課程中，我們討論這些供應商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)提供多樣化模型，包括核心GPT系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)專注於企業準備的OpenAI模型
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)提供開源模型和推理服務器

**你將需要使用自己的賬戶進行這些練習**。作業是可選的，因此你可以根據興趣選擇設置一個、全部或不設置任何供應商。一些註冊指導：

| 註冊 | 成本 | API密鑰 | 操作平台 | 評論 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於項目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無代碼，網頁](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須提前申請獲得訪問](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [訪問令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat有有限的模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照下面的指示_配置_此倉庫以與不同供應商一起使用。需要特定供應商的作業將在其文件名中包含以下標籤之一：
 - `aoai` - 需要Azure OpenAI端點，密鑰
 - `oai` - 需要OpenAI端點，密鑰
 - `hf` - 需要Hugging Face令牌

你可以配置一個、沒有或所有供應商。相關作業將在缺少憑證時報錯。

###  2.1. 創建`.env`文件

我們假設你已經閱讀了上面的指導並註冊了相關供應商，並獲得了所需的身份驗證憑證（API_KEY或令牌）。在Azure OpenAI的情況下，我們假設你也有一個有效的Azure OpenAI服務（端點）部署，其中至少部署了一個GPT模型以完成聊天。

下一步是按如下方式配置你的**本地環境變量**：

1. 在根文件夾中查找一個`.env.copy`文件，其內容應如下所示：

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

2. 使用下面的命令將該文件複製到`.env`。此文件已被_gitignore_，保持秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 按照下一節的描述填寫值（替換`=`右側的佔位符）。

3. （選項）如果你使用GitHub Codespaces，你可以選擇將環境變量保存為與此倉庫相關聯的_Codespaces secrets_。在這種情況下，你將不需要設置本地.env文件。**但是，請注意，此選項僅在你使用GitHub Codespaces時有效。**如果你使用Docker Desktop，仍然需要設置.env文件。

### 2.2. 填寫`.env`文件

讓我們快速查看變量名稱以了解它們代表什麼：

| 變量 | 描述 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是你在個人資料中設置的用戶訪問令牌 |
| OPENAI_API_KEY | 這是用於非Azure OpenAI端點的服務授權密鑰 |
| AZURE_OPENAI_API_KEY | 這是使用該服務的授權密鑰 |
| AZURE_OPENAI_ENDPOINT | 這是Azure OpenAI資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | 這是_文本生成_模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 這是_文本嵌入_模型的部署端點 |
| | |

注意：最後兩個Azure OpenAI變量分別反映聊天完成（文本生成）和向量搜索（嵌入）的默認模型。設置它們的指示將在相關作業中定義。

### 2.3 配置Azure：從Portal

Azure OpenAI端點和密鑰值將在[Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)中找到，所以讓我們從那裡開始。

1. 前往[Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點擊側邊欄中的**密鑰和端點**選項（左側菜單）。
1. 點擊**顯示密鑰** - 你應該看到以下內容：密鑰1、密鑰2和端點。
1. 使用密鑰1的值作為AZURE_OPENAI_API_KEY
1. 使用端點值作為AZURE_OPENAI_ENDPOINT

接下來，我們需要為我們部署的特定模型獲得端點。

1. 點擊Azure OpenAI資源的側邊欄（左側菜單）中的**模型部署**選項。
1. 在目標頁面中，點擊**管理部署**

這將帶你到Azure OpenAI Studio網站，我們將在下面找到其他值。

### 2.4 配置Azure：從Studio

1. 如上所述，**從你的資源**導航到[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊側邊欄（左側）中的**部署**選項卡以查看當前部署的模型。
1. 如果你的目標模型未部署，請使用**創建新部署**來部署它。
1. 你將需要一個_文本生成_模型 - 我們推薦：**gpt-35-turbo**
1. 你將需要一個_文本嵌入_模型 - 我們推薦**text-embedding-ada-002**

現在更新環境變量以反映使用的_部署名稱_。這通常會與模型名稱相同，除非你顯式更改它。因此，作為示例，你可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成後不要忘記保存.env文件**。你現在可以退出文件並返回運行筆記本的指示。

### 2.5 配置OpenAI：從個人資料

你的OpenAI API密鑰可以在你的[OpenAI賬戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果你沒有賬戶，你可以註冊並創建API密鑰。獲得密鑰後，你可以用它來填寫`.env`文件中的`OPENAI_API_KEY`變量。

### 2.6 配置Hugging Face：從個人資料

你的Hugging Face令牌可以在你的個人資料中找到，位於[訪問令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)下。不要公開發布或分享這些令牌。相反，為此項目使用創建一個新的令牌並將其複製到`.env`文件中的`HUGGING_FACE_API_KEY`變量下。_注意：_這在技術上不是API密鑰，但用於身份驗證，因此我們保持這種命名約定以保持一致性。

**免責聲明**：
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對於使用此翻譯所引起的任何誤解或誤釋不承擔責任。