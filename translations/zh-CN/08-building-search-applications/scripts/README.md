# 转录数据准备

转录数据准备脚本下载YouTube视频转录内容，并为使用OpenAI嵌入和函数的语义搜索示例做好准备。

转录数据准备脚本已在最新发布的Windows 11、macOS Ventura和Ubuntu 22.04（及以上版本）上进行了测试。

## 创建所需的Azure OpenAI服务资源

> [!IMPORTANT]
> 我们建议您将Azure CLI更新到最新版本，以确保与OpenAI的兼容性
> 参见[文档](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 创建资源组

> [!NOTE]
> 本指南中我们使用名为 "semantic-video-search" 的资源组，位于东部美国。
> 您可以更改资源组名称，但更改资源位置时，
> 请检查[模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 创建Azure OpenAI服务资源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 获取端点和密钥以供本应用使用

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - 版本为 `2` 或更高的 `text-embedding-ada-002`，命名为 `text-embedding-ada-002`
   - 命名为 `gpt-5-mini` 的 `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## 所需软件

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或更高版本

## 环境变量

运行YouTube转录数据准备脚本需要以下环境变量。

### 在Windows上

建议将变量添加到您的 `用户` 环境变量中。
`Windows开始` > `编辑系统环境变量` > `环境变量` > [用户] 的 `用户变量` > `新建`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- 您也可以将环境变量添加到您的PowerShell配置文件。

```powershell
$env:AZURE_OPENAI_API_KEY = "<您的Azure OpenAI服务API密钥>"
$env:AZURE_OPENAI_ENDPOINT = "<您的Azure OpenAI服务端点>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<您的Azure OpenAI服务模型部署名称>"
$env:GOOGLE_DEVELOPER_API_KEY = "<您的Google开发者API密钥>"
``` -->

### 在Linux和macOS上

建议将以下导出添加到您的 `~/.bashrc` 或 `~/.zshrc` 文件中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安装所需的Python库

1. 如果尚未安装，先安装[git客户端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 在 `终端` 窗口中，将示例克隆到您首选的仓库文件夹中。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 切换到 `data_prep` 文件夹。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 创建Python虚拟环境。

    在Windows上：

    ```powershell
    python -m venv .venv
    ```

    在macOS和Linux上：

    ```bash
    python3 -m venv .venv
    ```

1. 激活Python虚拟环境。

   在Windows上：

   ```powershell
   .venv\Scripts\activate
   ```

   在macOS和Linux上：

   ```bash
   source .venv/bin/activate
   ```

1. 安装所需的库。

   在Windows上：

   ```powershell
   pip install -r requirements.txt
   ```

   在macOS和Linux上：

   ```bash
   pip3 install -r requirements.txt
   ```

## 运行YouTube转录数据准备脚本

### 在Windows上

```powershell
.\transcripts_prepare.ps1
```

### 在macOS和Linux上

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->