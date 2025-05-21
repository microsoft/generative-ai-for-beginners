<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:27:02+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "zh"
}
-->
# 转录数据准备

转录数据准备脚本用于下载 YouTube 视频的转录内容，并将其准备好以用于 OpenAI 嵌入和函数示例的语义搜索。

转录数据准备脚本已经在最新版本的 Windows 11、macOS Ventura 和 Ubuntu 22.04（及以上版本）上进行了测试。

## 创建所需的 Azure OpenAI 服务资源

> [!IMPORTANT]
> 我们建议您将 Azure CLI 更新到最新版本以确保与 OpenAI 的兼容性。
> 请参阅[文档](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 创建一个资源组

> [!NOTE]
> 在这些说明中，我们使用的是位于美国东部的名为“semantic-video-search”的资源组。
> 您可以更改资源组的名称，但在更改资源位置时，请检查[模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 创建一个 Azure OpenAI 服务资源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 获取此应用程序使用的终端和密钥

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## 所需软件

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或更高版本

## 环境变量

运行 YouTube 转录数据准备脚本需要以下环境变量。

### 在 Windows 上

建议将变量添加到您的 `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### 在 Linux 和 macOS 上

建议将以下导出添加到您的 `~/.bashrc` or `~/.zshrc` 文件中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安装所需的 Python 库

1. 如果尚未安装，请安装 [git 客户端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 在 `Terminal` 窗口中，将示例克隆到您首选的存储库文件夹。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 导航到 `data_prep` 文件夹。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 创建一个 Python 虚拟环境。

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

1. 安装所需的库。

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

**免责声明**：
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档的本国语言版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误释，我们不承担责任。