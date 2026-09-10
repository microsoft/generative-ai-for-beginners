# Local Setup 🖥️

**Use this guide if you prefer to run everything on your own laptop.**   
You have two paths: **(A) native Python + virtual-env** or **(B) VS Code Dev Container with Docker**.  
Choose whichever feels easier—both lead to the same lessons.

## 1.  Prerequisites

| Tool               | Version / Notes                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (get it from <https://python.org>)                                            |
| **Git**            | Latest (comes with Xcode / Git for Windows / Linux package manager)                   |
| **VS Code**        | Optional but recommended <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Only* for Option B. Free install: <https://docs.docker.com/desktop/>                |

> 💡 **Tip** – Verify tools in a terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (quickest)

### Step 1  Clone this repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 Create & activate a virtual environment

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt should now start with (.venv)—that means you’re inside the env.

### Step 3 Install dependencies

```bash
pip install -r requirements.txt
```

Skip to Section 3 on [API keys](#3-add-your-api-keys)

## 2. Option B – VS Code Dev Container (Docker)

We setup this repository and course with a [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) that has a Universal runtime that can support Python3, .NET, Node.js and Java development. The related configuration is defined in the `devcontainer.json` file located in the `.devcontainer/` folder at the root of this repository.

>**Why choose this?**
>Identical environment to Codespaces; no dependency drift.

### Step 0 Install the extras

Docker Desktop – confirm ```docker --version``` works.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Step 1 Open the repo in VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code detects .devcontainer/ and pops a prompt.

### Step 2 Reopen in container

Click “Reopen in Container”. Docker builds the image (≈ 3 min first time).
When the terminal prompt appears, you’re inside the container.

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is a lightweight installer for installing [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, as well as a few packages.
Conda itself is a package manager, that makes it easy to setup and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. It also comes in handy for installing packages that are not available via `pip`.

### Step 0  Install Miniconda

Follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

```bash
conda --version
```

### Step 1 Create a virtual environment

Create a new environment file (*environment.yml*). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

### Step 2  Populate your environment file

Add the following snippet to your  `environment.yml`

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

### Step 3 Create your Conda environment

Run the commands below in your command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Refer to the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if you run into any issues.

## 2  Option D – Classic Jupyter / Jupyter Lab (in your browser)

> **Who’s this for?**  
> Anyone who loves the classic Jupyter interface or wants to run notebooks without VS Code.  

### Step 1  Ensure Jupyter is installed

To start Jupyter locally, head over to the terminal/command line, navigate to the course directory, and execute:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

This will start a Jupyter instance and the URL to access it will be shown within the command line window.

Once you access the URL, you should see the course outline and be able to navigate to any `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Add Your API Keys

Keeping your API keys safe and secure is important when building any type of application. We recommend not to store any API keys directly in your code. Committing those details to a public repository could result in security issues and even unwanted costs if used by a bad actor.
Here's a step-by-step guide on how to create a `.env` file for Python and add your Microsoft Foundry Models credentials:

> **Note:** GitHub Models (and its `GITHUB_TOKEN` variable) is retiring at the end of July 2026. This guide uses [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) instead. Prefer to work fully offline? See [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navigate to Your Project Directory**: Open your terminal or command prompt and navigate to your project's root directory where you want to create the `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Create the `.env` File**: Use your preferred text editor to create a new file named `.env`. If you're using the command line, you can use `touch` (on Unix-based systems) or `echo` (on Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit the `.env` File**: Open the `.env` file in a text editor (e.g., VS Code, Notepad++, or any other editor). Add the following lines to the file, replacing the placeholders with your actual Microsoft Foundry project endpoint and API key:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Save the File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` package to load environment variables from the `.env` file into your Python application. You can install it using `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables in Your Python Script**: In your Python script, use the `python-dotenv` package to load the environment variables from the `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the Microsoft Foundry Models variables
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

That's it! You've successfully created a `.env` file, added your Microsoft Foundry Models credentials, and loaded them into your Python application.

🔐 Never commit .env—it’s already in .gitignore.
Full provider instructions live in [`providers.md`](03-providers.md).

## 4. What’s next?

| I want to…          | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Setup an LLM Provider | [`providers.md`](03-providers.md)                                       |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Troubleshooting

| Symptom                                   | Fix                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Add Python to PATH or re-open terminal after install            |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` then retry.        |
| `ModuleNotFoundError: dotenv`             | Run `pip install -r requirements.txt` (env wasn’t installed).   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → increase disk size. |
| VS Code keeps prompting to reopen         | You may have both Options active; choose one (venv **or** container)|
| OpenAI 401 / 429 errors                   | Check `OPENAI_API_KEY` value / request rate limits.             |
| Errors using Conda                        | Install Microsoft AI libraries using `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->