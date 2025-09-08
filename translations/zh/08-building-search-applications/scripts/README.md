<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:07:23+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "zh"
}
-->
# 转录数据准备

转录数据准备脚本会下载 YouTube 视频的字幕，并将其整理为可用于“使用 OpenAI 嵌入和函数的语义搜索”示例的格式。

转录数据准备脚本已在最新版本的 Windows 11、macOS Ventura 和 Ubuntu 22.04（及以上版本）上进行了测试。

## 创建所需的 Azure OpenAI 服务资源

> [!IMPORTANT]
> 建议您将 Azure CLI 更新到最新版本，以确保与 OpenAI 的兼容性
> 详情请参见 [文档](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 创建资源组

> [!NOTE]
> 本说明中使用的资源组名称为“semantic-video-search”，位于 East US。
> 您可以更改资源组名称，但如果更改资源位置，
> 请查看[模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 创建 Azure OpenAI 服务资源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 获取用于本应用的端点和密钥

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - 版本为 `2` 或更高的 `text-embedding-ada-002`，命名为 `text-embedding-ada-002`
   - 版本为 `0613` 或更高的 `gpt-35-turbo`，命名为 `gpt-35-turbo`

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

运行 YouTube 转录数据准备脚本需要设置以下环境变量。

### Windows 系统

建议将变量添加到您的“用户”环境变量中。
`Windows 开始` > `编辑系统环境变量` > `环境变量` > 选择 [USER] 的“用户变量” > `新建`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux 和 macOS 系统

建议将以下导出命令添加到您的 `~/.bashrc` 或 `~/.zshrc` 文件中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安装所需的 Python 库

1. 如果尚未安装，请先安装 [git 客户端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 在 `终端` 窗口中，将示例克隆到您喜欢的仓库文件夹。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 进入 `data_prep` 文件夹。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 创建 Python 虚拟环境。

    Windows 系统：

    ```powershell
    python -m venv .venv
    ```

    macOS 和 Linux 系统：

    ```bash
    python3 -m venv .venv
    ```

1. 激活 Python 虚拟环境。

   Windows 系统：

   ```powershell
   .venv\Scripts\activate
   ```

   macOS 和 Linux 系统：

   ```bash
   source .venv/bin/activate
   ```

1. 安装所需库。

   Windows 系统：

   ```powershell
   pip install -r requirements.txt
   ```

   macOS 和 Linux 系统：

   ```bash
   pip3 install -r requirements.txt
   ```

## 运行 YouTube 转录数据准备脚本

### Windows 系统

```powershell
.\transcripts_prepare.ps1
```

### macOS 和 Linux 系统

```bash
./transcripts_prepare.sh
```

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。