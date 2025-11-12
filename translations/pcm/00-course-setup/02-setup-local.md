<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-11-12T09:02:43+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pcm"
}
-->
# Local Setup 🖥️

**Use dis guide if you wan run everything for your laptop.**  
You get two options: **(A) native Python + virtual-env** or **(B) VS Code Dev Container with Docker**.  
Choose the one wey easy for you—both go lead to the same lessons.

## 1. Prerequisites

| Tool               | Version / Notes                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (get am from <https://python.org>)                                            |
| **Git**            | Latest (e dey come with Xcode / Git for Windows / Linux package manager)             |
| **VS Code**        | Optional but e good make you use am <https://code.visualstudio.com>                  |
| **Docker Desktop** | *Only* for Option B. Free install: <https://docs.docker.com/desktop/>                |

> 💡 **Tip** – Check tools for terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Option A – Native Python (quickest)

### Step 1 Clone dis repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 Create & activate virtual environment

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt go dey start with (.venv)—e mean say you don enter the env.

### Step 3 Install dependencies

```bash
pip install -r requirements.txt
```

Skip go Section 3 for [API keys](../../../00-course-setup)

## 2. Option B – VS Code Dev Container (Docker)

We don set dis repository and course with [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) wey get Universal runtime wey fit support Python3, .NET, Node.js and Java development. The related configuration dey for `devcontainer.json` file wey dey inside `.devcontainer/` folder for the root of dis repository.

>**Why you go choose dis one?**
>Environment go dey same as Codespaces; no dependency wahala.

### Step 0 Install the extras

Docker Desktop – confirm ```docker --version``` dey work.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Step 1 Open the repo for VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code go detect .devcontainer/ and go show prompt.

### Step 2 Reopen for container

Click “Reopen in Container”. Docker go build the image (≈ 3 min first time).
When terminal prompt show, you don enter the container.

## 2. Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na lightweight installer for installing [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, and some packages.  
Conda na package manager wey dey make am easy to setup and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E dey also help for installing packages wey no dey available via `pip`.

### Step 0 Install Miniconda

Follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set am up.

```bash
conda --version
```

### Step 1 Create virtual environment

Create new environment file (*environment.yml*). If you dey follow along using Codespaces, create am inside `.devcontainer` directory, so `.devcontainer/environment.yml`.

### Step 2 Add to your environment file

Add dis snippet to your `environment.yml`

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

Run dis commands for your command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Check [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if you get any wahala.

## 2. Option D – Classic Jupyter / Jupyter Lab (for your browser)

> **Who dis one fit?**  
> Anybody wey like the classic Jupyter interface or wan run notebooks without VS Code.  

### Step 1 Make sure Jupyter dey installed

To start Jupyter locally, go terminal/command line, go the course directory, and run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Dis go start Jupyter instance and the URL to access am go show for the command line window.

Once you access the URL, you go see the course outline and fit navigate to any `*.ipynb` file. Example, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Add Your API Keys

To keep your API keys safe and secure dey important when you dey build any type of application. We dey recommend make you no store any API keys directly for your code. If you commit those details to public repository, e fit cause security wahala and even unwanted costs if bad person use am.  
Here na step-by-step guide on how to create `.env` file for Python and add `GITHUB_TOKEN`:

1. **Go Your Project Directory**: Open your terminal or command prompt and go your project's root directory wey you wan create `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Create `.env` File**: Use your preferred text editor to create new file wey dem call `.env`. If you dey use command line, you fit use `touch` (for Unix-based systems) or `echo` (for Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit `.env` File**: Open `.env` file for text editor (e.g., VS Code, Notepad++, or any other editor). Add dis line to the file, replace `your_github_token_here` with your actual GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Save the File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you never install am before, you go need install `python-dotenv` package to load environment variables from `.env` file into your Python application. You fit install am using `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables for Your Python Script**: For your Python script, use `python-dotenv` package to load the environment variables from `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Na so e be! You don successfully create `.env` file, add your GitHub token, and load am into your Python application.

🔐 No commit `.env`—e don already dey for `.gitignore`.  
Full provider instructions dey for [`providers.md`](03-providers.md).

## 4. Wetin next?

| I wan…              | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Setup LLM Provider  | [`providers.md`](03-providers.md)                                       |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Troubleshooting

| Symptom                                   | Fix                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Add Python to PATH or re-open terminal after install            |
| `pip` no fit build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` then try again.    |
| `ModuleNotFoundError: dotenv`             | Run `pip install -r requirements.txt` (env no dey installed).   |
| Docker build fail *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → increase disk size. |
| VS Code dey prompt to reopen              | You fit get both Options active; choose one (venv **or** container)|
| OpenAI 401 / 429 errors                   | Check `OPENAI_API_KEY` value / request rate limits.             |
| Errors using Conda                        | Install Microsoft AI libraries using `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->