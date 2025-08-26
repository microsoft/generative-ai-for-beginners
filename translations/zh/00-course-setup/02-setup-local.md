<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T14:30:22+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "zh"
}
-->
# 本地环境搭建 🖥️

**如果你更喜欢在自己的电脑上运行所有内容，请参考本指南。**  
你有两种选择：**(A) 原生 Python + 虚拟环境** 或 **(B) VS Code Dev Container 配合 Docker**。  
任选一种你觉得更简单的方式——两种方法都能学到同样的内容。

## 1.  前置条件

| 工具                | 版本 / 说明                                                                       |
|---------------------|-----------------------------------------------------------------------------------|
| **Python**          | 3.10 及以上（可在 <https://python.org> 下载）                                     |
| **Git**             | 最新版（Xcode / Git for Windows / Linux 包管理器自带）                            |
| **VS Code**         | 可选但推荐 <https://code.visualstudio.com>                                        |
| **Docker Desktop**  | *仅* 适用于选项 B。免费安装：<https://docs.docker.com/desktop/>                   |

> 💡 **提示** – 在终端验证工具是否安装：  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  选项 A – 原生 Python（最快）

### 步骤 1  克隆本仓库

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 步骤 2 创建并激活虚拟环境

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 现在命令行前面应该有 (.venv)——这表示你已经进入了虚拟环境。

### 步骤 3 安装依赖

```bash
pip install -r requirements.txt
```

跳转到第 3 节 [API 密钥](../../../00-course-setup)

## 2. 选项 B – VS Code Dev Container（Docker）

我们为本仓库和课程配置了一个 [开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，它内置了通用运行环境，支持 Python3、.NET、Node.js 和 Java 开发。相关配置在仓库根目录的 `.devcontainer/` 文件夹下的 `devcontainer.json` 文件中。

>**为什么选择这个？**
>环境和 Codespaces 完全一致；不会有依赖漂移问题。

### 步骤 0 安装额外工具

Docker Desktop – 确认 ```docker --version``` 能正常运行。  
VS Code Remote – Containers 扩展（ID: ms-vscode-remote.remote-containers）。

### 步骤 1 用 VS Code 打开仓库

文件 ▸ 打开文件夹…  → generative-ai-for-beginners

VS Code 会检测到 .devcontainer/ 并弹出提示。

### 步骤 2 在容器中重新打开

点击“Reopen in Container”。Docker 会构建镜像（首次大约 3 分钟）。
当终端出现提示符时，说明你已经在容器内部了。

## 2.  选项 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级的 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及部分包的安装器。
Conda 本身是一个包管理器，可以方便地创建和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和包。对于一些 `pip` 无法安装的包也很有用。

### 步骤 0  安装 Miniconda

按照 [MiniConda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 进行安装。

```bash
conda --version
```

### 步骤 1 创建虚拟环境

新建一个环境文件（*environment.yml*）。如果你在 Codespaces 上操作，请在 `.devcontainer` 目录下创建，即 `.devcontainer/environment.yml`。

### 步骤 2  填写环境文件

将以下内容添加到你的 `environment.yml` 文件中

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

### 步骤 3 创建 Conda 环境

在命令行/终端中运行以下命令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如遇问题可参考 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2  选项 D – 经典 Jupyter / Jupyter Lab（浏览器中运行）

> **适合谁？**  
> 喜欢经典 Jupyter 界面或希望不用 VS Code 直接运行 notebook 的同学。  

### 步骤 1  确保已安装 Jupyter

要在本地启动 Jupyter，请在终端/命令行进入课程目录，并执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这会启动一个 Jupyter 实例，命令行窗口会显示访问用的 URL。

访问该 URL 后，你应该能看到课程大纲，并可以浏览任意 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

## 3. 添加你的 API 密钥

在开发任何应用时，保护好你的 API 密钥非常重要。我们建议不要将 API 密钥直接写在代码里。如果把密钥提交到公开仓库，可能会带来安全风险，甚至被恶意使用导致不必要的费用。
下面是为 Python 创建 `.env` 文件并添加 `GITHUB_TOKEN` 的详细步骤：

1. **进入你的项目目录**：打开终端或命令提示符，进入你想创建 `.env` 文件的项目根目录。

   ```bash
   cd path/to/your/project
   ```

2. **创建 `.env` 文件**：用你喜欢的文本编辑器新建一个名为 `.env` 的文件。如果用命令行，可以用 `touch`（类 Unix 系统）或 `echo`（Windows）：

   类 Unix 系统：

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器（如 VS Code、Notepad++ 或其他）打开 `.env` 文件。添加如下内容，并将 `your_github_token_here` 替换为你自己的 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存修改并关闭编辑器。

5. **安装 `python-dotenv`**：如果还没安装，需要用 `pip` 安装 `python-dotenv` 包，以便从 `.env` 文件加载环境变量到 Python 应用中：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在你的 Python 脚本中，使用 `python-dotenv` 包从 `.env` 文件加载环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就这样！你已经成功创建了 `.env` 文件，添加了 GitHub token，并将其加载到 Python 应用中。

🔐 千万不要提交 .env 文件——它已经被加入 .gitignore。
完整的服务商说明见 [`providers.md`](03-providers.md)。

## 4. 接下来做什么？

| 我想要…             | 前往…                                                                       |
|---------------------|----------------------------------------------------------------------------|
| 开始第一课          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| 配置 LLM 服务商     | [`providers.md`](03-providers.md)                                          |
| 结识其他学习者      | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 常见问题排查

| 症状                                      | 解决方法                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | 将 Python 加入 PATH 或安装后重启终端                            |
| `pip` 无法构建 wheels（Windows）          | 先运行 `pip install --upgrade pip setuptools wheel` 再重试      |
| `ModuleNotFoundError: dotenv`             | 运行 `pip install -r requirements.txt`（环境未安装）            |
| Docker 构建失败 *No space left*           | Docker Desktop ▸ *设置* ▸ *资源* → 增加磁盘空间                 |
| VS Code 一直提示重新打开                  | 可能同时激活了两种方式；请选择一种（venv **或** container）     |
| OpenAI 401 / 429 错误                     | 检查 `OPENAI_API_KEY` 的值 / 请求频率限制                       |
| 使用 Conda 报错                           | 用 `conda install -c microsoft azure-ai-ml` 安装微软 AI 库      |

---

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。