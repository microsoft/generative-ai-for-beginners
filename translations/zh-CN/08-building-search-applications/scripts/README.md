# 转录数据准备

转录数据准备脚本下载 YouTube 视频转录文本，并为使用 OpenAI Embeddings 和 Functions 的语义搜索示例做准备。

转录数据准备脚本已在最新版本的 Windows 11、macOS Ventura 和 Ubuntu 22.04（及更高版本）上进行了测试。

## 创建所需的 Azure OpenAI 服务资源

> [!IMPORTANT]
> 我们建议您将 Azure CLI 更新到最新版本，以确保与 OpenAI 的兼容性
> 参见 [文档](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 创建资源组

> [!NOTE]
> 在这些说明中，我们使用位于 East US 的名为“semantic-video-search”的资源组。
> 您可以更改资源组的名称，但更改资源位置时，
> 请检查 [模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 创建 Azure OpenAI 服务资源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 获取端点和密钥以供本应用程序使用

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - 版本为 `2` 或更高的 `text-embedding-ada-002`，命名为 `text-embedding-ada-002`
   - 命名为 `gpt-4o-mini` 的 `gpt-4o-mini`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## 所需软件

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或更高版本

## 环境变量

运行 YouTube 转录数据准备脚本需要以下环境变量。

### 在 Windows 上

建议将变量添加到您的 `user` 环境变量中。
`Windows Start` > `编辑系统环境变量` > `环境变量` > [USER] 用户变量 > `新建`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- 您也可以将环境变量添加到您的 PowerShell 配置文件。

```powershell
$env:AZURE_OPENAI_API_KEY = "<您的 Azure OpenAI 服务 API 密钥>"
$env:AZURE_OPENAI_ENDPOINT = "<您的 Azure OpenAI 服务端点>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<您的 Azure OpenAI 服务模型部署名称>"
$env:GOOGLE_DEVELOPER_API_KEY = "<您的 Google 开发者 API 密钥>"
``` -->

### 在 Linux 和 macOS 上

建议将以下导出添加到您的 `~/.bashrc` 或 `~/.zshrc` 文件中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安装所需的 Python 库

1. 如果尚未安装，先安装 [git 客户端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 在 `终端` 窗口中，克隆样例到您喜欢的仓库文件夹。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 进入 `data_prep` 文件夹。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 创建 Python 虚拟环境。

    在 Windows 上：

    ```powershell
    python -m venv .venv
    ```

    在 macOS 和 Linux 上：

    ```bash
    python3 -m venv .venv
    ```

1. 激活 Python 虚拟环境。

   在 Windows 上：

   ```powershell
   .venv\Scripts\activate
   ```

   在 macOS 和 Linux 上：

   ```bash
   source .venv/bin/activate
   ```

1. 安装所需库。

   在 Windows 上：

   ```powershell
   pip install -r requirements.txt
   ```

   在 macOS 和 Linux 上：

   ```bash
   pip3 install -r requirements.txt
   ```

## 运行 YouTube 转录数据准备脚本

### 在 Windows 上

```powershell
.\transcripts_prepare.ps1
```

### 在 macOS 和 Linux 上

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->