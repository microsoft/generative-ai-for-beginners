# 本地设置 🖥️

**如果你更喜欢在自己的笔记本电脑上运行所有内容，请使用本指南。**  
你有两条路径：**(A) 原生 Python + 虚拟环境** 或 **(B) 使用 Docker 的 VS Code 开发容器**。  
选择你觉得更简单的方式——两者都能完成相同的课程。

## 1. 先决条件

| 工具               | 版本 / 备注                                                                        |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 及以上（从 <https://python.org> 获取）                                        |
| **Git**            | 最新版本（随 Xcode / Windows Git / Linux 包管理器提供）                            |
| **VS Code**        | 可选但推荐 <https://code.visualstudio.com>                                        |
| **Docker Desktop** | *仅限* 选项 B。免费安装：<https://docs.docker.com/desktop/>                        |

> 💡 **提示** – 在终端验证工具：  
> `python --version`，`git --version`，`docker --version`，`code --version`  

## 2. 选项 A – 原生 Python（最快）

### 第 1 步 克隆此仓库

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 第 2 步 创建并激活虚拟环境

```bash
python -m venv .venv          # 制作一个
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 提示符现在应以 (.venv) 开头——这表示你已进入虚拟环境。

### 第 3 步 安装依赖

```bash
pip install -r requirements.txt
```

跳转到第 3 节 [添加你的 API 密钥](../../../00-course-setup)

## 2. 选项 B – VS Code 开发容器（Docker）

我们使用了一个[开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)来设置此仓库和课程，该容器具有支持 Python3、.NET、Node.js 和 Java 开发的通用运行时。相关配置定义在仓库根目录的 `.devcontainer/` 文件夹中的 `devcontainer.json` 文件里。

>**为什么选择这个？**  
>环境与 Codespaces 完全相同；无依赖漂移。

### 第 0 步 安装额外工具

Docker Desktop – 确认 ```docker --version``` 可用。  
VS Code 远程 – 容器扩展（ID: ms-vscode-remote.remote-containers）。

### 第 1 步 在 VS Code 中打开仓库

文件 ▸ 打开文件夹… → generative-ai-for-beginners

VS Code 会检测到 .devcontainer/ 并弹出提示。

### 第 2 步 在容器中重新打开

点击“在容器中重新打开”。Docker 会构建镜像（首次约 3 分钟）。  
当终端提示出现时，你已进入容器。

## 2. 选项 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级安装器，用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些包。  
Conda 本身是一个包管理器，方便设置和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和包。它也适合安装 `pip` 无法提供的包。

### 第 0 步 安装 Miniconda

按照 [MiniConda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 进行安装。

```bash
conda --version
```

### 第 1 步 创建虚拟环境

创建一个新的环境文件 (*environment.yml*)。如果你使用 Codespaces，需在 `.devcontainer` 目录下创建，即 `.devcontainer/environment.yml`。

### 第 2 步 填充环境文件

将以下内容添加到你的 `environment.yml` 中

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

### 第 3 步 创建 Conda 环境

在命令行/终端运行以下命令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路径仅适用于 Codespace 设置
conda activate ai4beg
```

如果遇到问题，请参考 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2. 选项 D – 经典 Jupyter / Jupyter Lab（浏览器中）

> **适合谁？**  
> 喜欢经典 Jupyter 界面或想在不使用 VS Code 的情况下运行笔记本的用户。

### 第 1 步 确保已安装 Jupyter

要在本地启动 Jupyter，打开终端/命令行，切换到课程目录，执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这将启动一个 Jupyter 实例，访问 URL 会显示在命令行窗口中。

访问该 URL 后，你应能看到课程大纲并导航到任何 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

## 3. 添加你的 API 密钥

在构建任何类型的应用时，保护你的 API 密钥安全非常重要。我们建议不要将任何 API 密钥直接存储在代码中。将这些信息提交到公共仓库可能导致安全问题，甚至被恶意使用产生不必要的费用。  
以下是如何为 Python 创建 `.env` 文件并添加 `GITHUB_TOKEN` 的分步指南：

1. **进入你的项目目录**：打开终端或命令提示符，切换到你想创建 `.env` 文件的项目根目录。

   ```bash
   cd path/to/your/project
   ```

2. **创建 `.env` 文件**：使用你喜欢的文本编辑器创建一个名为 `.env` 的新文件。如果使用命令行，可以用 `touch`（Unix 系统）或 `echo`（Windows）：

   Unix 系统：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器（如 VS Code、Notepad++ 或其他）打开 `.env` 文件。添加以下内容，将 `your_github_token_here` 替换为你的实际 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改并关闭编辑器。

5. **安装 `python-dotenv`**：如果尚未安装，需要安装 `python-dotenv` 包以从 `.env` 文件加载环境变量到 Python 应用。可用 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在你的 Python 脚本中，使用 `python-dotenv` 包加载 `.env` 文件中的环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # 从 .env 文件加载环境变量
   load_dotenv()

   # 访问 GITHUB_TOKEN 变量
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成！你已成功创建 `.env` 文件，添加了 GitHub 令牌，并将其加载到 Python 应用中。

🔐 切勿提交 .env 文件——它已被加入 .gitignore。  
完整的提供商说明见 [`providers.md`](03-providers.md)。

## 4. 接下来做什么？

| 我想…              | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 开始第 1 课         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 设置 LLM 提供商     | [`providers.md`](03-providers.md)                                       |
| 认识其他学习者      | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 故障排除

| 现象                                      | 解决方法                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | 将 Python 添加到 PATH，或安装后重新打开终端                      |
| Windows 下 `pip` 无法构建 wheels          | 运行 `pip install --upgrade pip setuptools wheel` 后重试         |
| `ModuleNotFoundError: dotenv`             | 运行 `pip install -r requirements.txt`（环境未安装）             |
| Docker 构建失败 *No space left*            | Docker Desktop ▸ *设置* ▸ *资源* → 增加磁盘大小                  |
| VS Code 不断提示重新打开                   | 你可能同时启用了两个选项；请选择一个（venv **或** 容器）          |
| OpenAI 401 / 429 错误                      | 检查 `OPENAI_API_KEY` 值 / 请求速率限制                          |
| 使用 Conda 出错                           | 使用 `conda install -c microsoft azure-ai-ml` 安装微软 AI 库      |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->