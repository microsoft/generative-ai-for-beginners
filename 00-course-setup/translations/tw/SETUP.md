# 設定 Your Dev Environment

我們設定了這個資料庫和課程，並使用[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，該容器具有通用執行環境，可以支援 Python3、.NET、Node.js 和 Java 開發。相關配置定義在此資料庫根目錄的 `.devcontainer/` 資料夾中的 `devcontainer.json` 文件中。

要啟動開發容器，請在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（用於雲端託管的執行環境）或[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（用於本地設備託管的執行環境）中啟動它。閱讀[此文件](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)以獲取有關開發容器在 VS Code 中如何工作的更多詳細資訊。

> [!TIP]  
> 我們建議使用 GitHub Codespaces 來快速開始並減少努力。它為個人帳戶提供慷慨的[免費使用配額](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超時](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或刪除不活動的 codespaces 以最大化您的配額使用。

## 1. 執行指派任務

每節課將有_可選的_作業，可能會以一種或多種程式語言提供，包括: Python、.NET/C#、Java 和 JavaScript/TypeScript。本節提供與執行這些作業相關的一般指導。

### 1.1 Python 指派

Python 指派是以應用程式（`.py` 檔案）或 Jupyter 筆記本（`.ipynb` 檔案）提供。

- 要執行筆記本，請在 Visual Studio Code 中打開它，然後點擊 _Select Kernel_ (在右上角)，並選擇顯示的預設 Python 3 選項。現在你可以 _Run All_ 來執行筆記本。
- 要從命令列執行 Python 應用程式，請遵循特定作業的指示，以確保選擇正確的檔案並提供所需的參數。

## 2. 設定提供者

作業**可能**也會被設定為通過像 OpenAI、Azure 或 Hugging Face 這樣的支援服務提供者來對抗一個或多個大型語言模型（LLM）部署。這些提供一個_託管端點_（API），我們可以使用正確的憑證（API 金鑰或令牌）以程式化方式訪問。在本課程中，我們討論這些提供者:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 包含多樣化模型，包括核心的 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) 提供專注於企業準備的 OpenAI 模型
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 提供開放原始碼模型和推論伺服器

**你將需要使用你自己的帳戶來完成這些練習**。作業是可選的，所以你可以根據自己的興趣選擇設定一個、全部或不設定任何提供者。以下是一些註冊的指導：

| 註冊 | 費用 | API 金鑰 | 操作平台 | 評論 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [價格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基於專案](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [無程式碼, 網頁](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多種模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [價格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入門](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必須提前申請訪問](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [價格](https://huggingface.co/pricing) | [存取權杖](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 有限的模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照以下指示來_配置_此儲存庫以供不同提供者使用。需要特定提供者的作業將在其檔案名中包含以下標籤之一:

- `aoai` - 需要 Azure OpenAI 端點, 金鑰
 - `oai` - 需要 OpenAI 端點, 金鑰
 - `hf` - 需要 Hugging Face token

您可以設定一個、沒有或所有提供者。相關的分配將在缺少憑證時簡單地出錯。

###  2.1. 建立 `.env` 文件

我們假設您已經閱讀了上述指南並註冊了相關提供者，並獲得了所需的身份驗證憑證(API_KEY 或 token)。在 Azure OpenAI 的情況下，我們假設您還擁有一個有效的 Azure OpenAI 服務部署(endpoint)，並至少部署了一個 GPT 模型以完成聊天。

下一步是按如下方式配置你的**本地環境變數**:

1. 在根目錄中查找 `.env.copy` 文件，內容應如下所示:

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

2. 使用以下命令將該文件複製到 `.env`。此文件已被 _gitignore-d_，以保護秘密資訊。

   ```bash
   cp .env.copy .env
   ```

3. 按照下一節中的描述填寫值（替換 `=` 右側的佔位符）。

3. (選項) 如果您使用 GitHub Codespaces，您可以選擇將環境變數保存為與此存儲庫關聯的 _Codespaces secrets_。在這種情況下，您不需要設置本地 .env 文件。**但是，請注意，此選項僅在您使用 GitHub Codespaces 時有效。**如果您使用 Docker Desktop，仍然需要設置 .env 文件。

### 2.2. 填寫 `.env` 檔案

讓我們快速看一下變數名稱，以了解它們代表什麼:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 這是您在個人資料中設定的使用者存取權杖 |
| OPENAI_API_KEY | 這是用於非 Azure OpenAI 端點服務的授權金鑰 |
| AZURE_OPENAI_KEY | 這是用於該服務的授權金鑰 |
| AZURE_OPENAI_ENDPOINT | 這是 Azure OpenAI 資源的部署端點 |
| AZURE_OPENAI_DEPLOYMENT | 這是 _文本生成_ 模型的部署端點 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 這是 _文本嵌入_ 模型的部署端點 |
| | |

注意: 最後兩個 Azure OpenAI 變數分別反映了聊天完成（文字產生）和向量搜尋（嵌入）的預設模型。設定它們的說明將在相關作業中定義。

### 2.3 設定 Azure: 從 Portal

Azure OpenAI 端點和金鑰值可以在 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，所以讓我們從那裡開始。

1. 前往 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 點擊側邊欄中的 **Keys and Endpoint** 選項（左側選單）。
1. 點擊 **Show Keys** - 你應該會看到以下內容: KEY 1, KEY 2 和 Endpoint。
1. 使用 KEY 1 的值作為 AZURE_OPENAI_KEY
1. 使用 Endpoint 的值作為 AZURE_OPENAI_ENDPOINT

接下來，我們需要已部署的特定模型的端點。

1. 在側邊欄（左側選單）中點擊 **Model deployments** 選項以獲取 Azure OpenAI 資源。
1. 在目標頁面中，點擊 **Manage Deployments**

這將帶你到 Azure OpenAI Studio 網站，我們會在那裡找到如下所述的其他值。

### 2.4 設定 Azure: 從 Studio

1. 按照上述說明從你的資源導航到 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 點擊 **Deployments** 標籤（側邊欄，左側）以查看當前部署的模型。
1. 如果你想要的模型尚未部署，使用 **Create new deployment** 來部署它。
1. 你將需要一個 _text-generation_ 模型 - 我們推薦: **gpt-35-turbo**
1. 你將需要一個 _text-embedding_ 模型 - 我們推薦 **text-embedding-ada-002**

現在更新環境變數以反映所使用的_部署名稱_。這通常與模型名稱相同，除非你明確更改了它。因此，作為範例，你可能會有:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**不要忘記在完成後保存.env文件**。你現在可以退出文件並返回執行筆記本的說明。

### 2.5 設定 OpenAI: 從 Profile

你的 OpenAI API 金鑰可以在你的 [OpenAI 帳戶](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果你沒有，你可以註冊一個帳戶並建立一個 API 金鑰。一旦你有了金鑰，你可以用它來填充 `.env` 檔案中的 `OPENAI_API_KEY` 變數。

### 2.6 設定 Hugging Face: 從個人資料

您的 Hugging Face token 可以在您的個人資料中的[Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)找到。不要公開張貼或分享這些資訊。相反地，為此專案使用建立一個新的 token，並將其複製到 `.env` 檔案中的 `HUGGING_FACE_API_KEY` 變數下。_注意:_ 這在技術上不是 API key，但用於身份驗證，因此我們保持這個命名慣例以保持一致性。

