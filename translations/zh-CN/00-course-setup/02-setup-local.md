# 本地设置 🖥️

**如果你更喜欢在自己的笔记本电脑上运行所有内容，请使用本指南。**  
你有两条路径：**(A) 原生 Python + 虚拟环境** 或 **(B) 带有 Docker 的 VS Code 开发容器**。  
选择你觉得更简单的方式——两者都能完成相同的课程内容。

## 1.  先决条件

| 工具               | 版本 / 备注                                                                        |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10+（可从 <https://python.org> 获取）                                            |
| **Git**            | 最新版本（随 Xcode / Git for Windows / Linux 包管理器一起提供）                    |
| **VS Code**        | 可选但推荐 <https://code.visualstudio.com>                                        |
| **Docker Desktop** | *仅用于选项 B*。免费下载：<https://docs.docker.com/desktop/>                      |

> 💡 <strong>小贴士</strong> – 在终端验证工具：  
> `python --version`，`git --version`，`docker --version`，`code --version`  

## 2.  选项 A – 原生 Python（最快速）

### 第一步 克隆此仓库

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 第二步 创建并激活虚拟环境

```bash
python -m venv .venv          # 创建一个
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 提示符现在应该以 (.venv) 开头——这意味着你已经进入该环境。

### 第三步 安装依赖

```bash
pip install -r requirements.txt
```

跳到第3节查看[API 密钥](#3-添加你的-api-密钥)

## 2. 选项 B – VS Code 开发容器 (Docker)

我们配备了一个[开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，里面有一个通用运行时，可以支持 Python3、.NET、Node.js 和 Java 开发。相关配置定义在此仓库根目录下 `.devcontainer/` 文件夹内的 `devcontainer.json` 文件中。

>**为什么选择此项？**
>环境与 Codespaces 完全相同；避免依赖漂移。

### 第零步 安装额外组件

Docker Desktop – 确认运行 `docker --version` 命令有效。
VS Code 远程 – 容器扩展（ID：ms-vscode-remote.remote-containers）。

### 第一步 在 VS Code 中打开仓库

文件 ▸ 打开文件夹… → generative-ai-for-beginners

VS Code 会检测到 .devcontainer/ 目录并弹出提示。

### 第二步 在容器中重新打开

点击“在容器中重新打开”。Docker 首次构建镜像大约需 3 分钟。
当终端提示符出现时，说明你已进入容器内。

## 2. 选项 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级安装器，用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些软件包。
Conda 本身是一个包管理工具，它能轻松设置和切换不同的 Python [<strong>虚拟环境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和软件包。它还方便安装那些无法通过 `pip` 安装的软件包。

### 第零步 安装 Miniconda

按照[Miniconda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)完成安装。

```bash
conda --version
```

### 第一步 创建虚拟环境

创建一个新环境文件 (*environment.yml*)。如果你使用 Codespaces 跟进，请在 `.devcontainer` 目录内创建，即 `.devcontainer/environment.yml`。

### 第二步 填充你的环境文件

将下面的内容添加到你的 `environment.yml` 中

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### 第三步 创建 Conda 环境

在命令行/终端运行以下命令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路径仅适用于 Codespace 设置
conda activate ai4beg
```

遇到问题请参考 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2 选项 D – 经典 Jupyter / Jupyter Lab（浏览器中）

> **适用人群？**  
> 喜欢经典 Jupyter 界面或想在不使用 VS Code 的情况下运行笔记本的人。  

### 第一步 确保已安装 Jupyter

本地启动 Jupyter，请打开终端/命令行，进入课程目录，执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这将启动一个 Jupyter 实例，访问 URL 会显示在命令行窗口中。

一旦访问该 URL，即可看到课程目录并浏览任一 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

## 3. 添加你的 API 密钥

构建任何应用时确保 API 密钥安全非常重要。建议不要直接将 API 密钥存储在代码中。将这些信息提交到公共仓库可能导致安全问题，甚至在被不良行为者使用时产生不必要的费用。
以下是如何为 Python 创建 `.env` 文件并添加 Microsoft Foundry Models 凭据的分步骤指南：

> **注意：** GitHub Models（及其 `GITHUB_TOKEN` 变量）将于2026年7月底下线。本指南改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。想要完全离线工作？请参见 [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)。

1. <strong>进入你的项目目录</strong>：打开终端或命令提示符，进入你希望创建 `.env` 文件的项目根目录。

   ```bash
   cd path/to/your/project
   ```

2. **创建 `.env` 文件**：使用你喜欢的文本编辑器创建名为 `.env` 的新文件。如果使用命令行，可用 `touch`（Unix 系统）或 `echo`（Windows）命令：

   Unix 系统：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器（如 VS Code、Notepad++ 或其他编辑器）打开 `.env` 文件。添加以下内容，替换为你的 Microsoft Foundry 项目端点和 API 密钥：

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>保存文件</strong>：保存更改并关闭编辑器。

5. **安装 `python-dotenv`**：如果尚未安装，需要安装 `python-dotenv` 包以将 `.env` 文件中的环境变量加载到 Python 应用中。可以通过 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在你的 Python 脚本中，使用 `python-dotenv` 包加载 `.env` 文件的环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # 从.env文件加载环境变量
   load_dotenv()

   # 访问Microsoft Foundry模型变量
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

就这样！你已经成功创建了 `.env` 文件，添加了 Microsoft Foundry Models 凭据，并在 Python 应用中加载了它们。

🔐 千万不要提交 .env 文件——它已经被加入 .gitignore。
完整的提供者说明见 [`providers.md`](03-providers.md)。

## 4. 接下来做什么？

| 我想…             | 跳转至…                                                                |
|---------------------|------------------------------------------------------------------------|
| 开始第1课          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 配置 LLM 提供者     | [`providers.md`](03-providers.md)                                       |
| 认识其他学习者     | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 故障排除

| 问题表现                              | 解决办法                                                   |
|-------------------------------------|------------------------------------------------------------|
| `python not found`                 | 将 Python 添加到 PATH，或安装后重新打开终端                  |
| Windows 上 `pip` 无法构建 wheel       | 运行 `pip install --upgrade pip setuptools wheel`，然后重试。 |
| `ModuleNotFoundError: dotenv`      | 运行 `pip install -r requirements.txt`（环境未安装）         |
| Docker 构建失败 *No space left*    | Docker Desktop ▸ <em>设置</em> ▸ <em>资源</em> → 增加磁盘大小。            |
| VS Code 不断提示重新打开             | 可能两个选项都启用了；选择一个（venv <strong>或</strong> 容器）          |
| OpenAI 401 / 429 错误              | 检查 `OPENAI_API_KEY` 值 / 请求速率限制                       |
| 使用 Conda 出错                    | 使用 `conda install -c microsoft azure-ai-ml` 安装 Microsoft AI 库 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->