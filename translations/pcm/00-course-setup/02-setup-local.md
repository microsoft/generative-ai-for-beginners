# Local Setup 🖥️

**Use dis guide if you prefer make you run everything for your own laptop.**   
You get two roads: **(A) native Python + virtual-env** or **(B) VS Code Dev Container wit Docker**.  
Choose any wey feel easier—both go lead to di same lessons.

## 1.  Prerequisites

| Tool               | Version / Notes                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (get am from <https://python.org>)                                            |
| **Git**            | Latest (e dey come wit Xcode / Git for Windows / Linux package manager)              |
| **VS Code**        | Optional but recommended <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Only* for Option B. Free install: <https://docs.docker.com/desktop/>                |

> 💡 **Tip** – Verify tools for terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (fast pass)

### Step 1  Clone dis repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 Create & activate virtual environment

```bash
python -m venv .venv          # mek one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt for terminal suppose now start wit (.venv)—dat mean say you dey inside di env.

### Step 3 Install dependencies

```bash
pip install -r requirements.txt
```

Skip go Section 3 about [API keys](#3-add-your-api-keys)

## 2. Option B – VS Code Dev Container (Docker)

We setup dis repository and course wit a [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) wey get Universal runtime wey fit support Python3, .NET, Node.js and Java development. Di related configuration dey inside `devcontainer.json` file wey dey `.devcontainer/` folder for root of dis repository.

>**Why you go choose dis?**
>E get di same environment as Codespaces; no wahala with dependency drift.

### Step 0 Install di extras

Docker Desktop – confirm say ```docker --version``` dey work.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Step 1 Open di repo for VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code go see .devcontainer/ and go show prompt.

### Step 2 Reopen inside container

Click “Reopen in Container”. Docker go build di image (≈ 3 min for first time).
When terminal prompt show, you dey inside container.

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na small installer for installing [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, plus some packages.
Conda na package manager wey make am easy to setup and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E still help for installing packages wey no dey available for `pip`.

### Step 0  Install Miniconda

Follow [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set am up.

```bash
conda --version
```

### Step 1 Create virtual environment

Make new environment file (*environment.yml*). If you dey follow using Codespaces, create dis inside `.devcontainer` directory, so `.devcontainer/environment.yml`.

### Step 2  Put your environment file

Add dis snippet for your  `environment.yml`

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

Run command dem for your command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path na only for Codespace settings e dey apply
conda activate ai4beg
```

Check [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if wahala show.

## 2  Option D – Classic Jupyter / Jupyter Lab (for your browser)

> **Who e dey for?**  
> Anybody wey like classic Jupyter interface or want run notebooks without VS Code.  

### Step 1  Make sure Jupyter dey installed

To start Jupyter locally, waka go terminal/command line, enter course directory, then run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Dis one go start Jupyter instance and URL to access go show for command line window.

When you access that URL, you go see course outline plus you fit waka to any `*.ipynb` file. Like `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Add Your API Keys

To keep your API keys safe and secure na important thing when you dey build any kind application. We recommend say no make you store any API keys direct for your code. Put those details for public repository fit cause security palava and fit even cause unwanted costs if bad person use am.
Here na step-by-step guide on how to create `.env` file for Python and add your Microsoft Foundry Models credentials:

> **Note:** GitHub Models (and e `GITHUB_TOKEN` variable) go retire by end of July 2026. Dis guide dey use [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) instead. You want work fully offline? See [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Waka go Your Project Directory**: Open your terminal or command prompt and waka go your project's root directory wey you wan create `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Create di `.env` File**: Use your preferred text editor to create new file named `.env`. If you dey use command line, you fit use `touch` (for Unix-based systems) or `echo` (for Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit di `.env` File**: Open `.env` file for text editor (e.g., VS Code, Notepad++, or any other editor). Add dis lines to the file, replace placeholders with your real Microsoft Foundry project endpoint and API key:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Save di File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you never install am, you go need install `python-dotenv` package to load environment variables from `.env` file into your Python application. You fit install am with `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables for Your Python Script**: For your Python script, use `python-dotenv` package to load environment variables from `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access di Microsoft Foundry Models variables
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Na so e be! You don successfully create `.env` file, add your Microsoft Foundry Models credentials, and load dem into your Python application.

🔐 Make you no ever commit .env—it dey already inside .gitignore.
Full provider instructions dey for [`providers.md`](03-providers.md).

## 4. Wetin next?

| I want to…          | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Setup an LLM Provider | [`providers.md`](03-providers.md)                                       |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Troubleshooting

| Symptom                                   | Fix                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Add Python to PATH or open terminal again after install            |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` then try again        |
| `ModuleNotFoundError: dotenv`             | Run `pip install -r requirements.txt` (env neva install).          |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → increase disk size     |
| VS Code dey always ask to reopen            | You fit get both Options active; choose one (venv **or** container)|
| OpenAI 401 / 429 errors                   | Check `OPENAI_API_KEY` value / request rate limits                 |
| Errors using Conda                        | Install Microsoft AI libraries with `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->