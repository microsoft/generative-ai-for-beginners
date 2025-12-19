<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T18:15:38+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pcm"
}
-->
# Local Setup 🖥️

**Use dis guide if you prefer to run everything for your own laptop.**   
You get two ways: **(A) native Python + virtual-env** or **(B) VS Code Dev Container with Docker**.  
Choose whichever e easy for you—both go lead to the same lessons.

## 1.  Prerequisites

| Tool               | Version / Notes                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (collect am from <https://python.org>)                                        |
| **Git**            | Latest (e dey come with Xcode / Git for Windows / Linux package manager)             |
| **VS Code**        | Optional but e good make you get am <https://code.visualstudio.com>                   |
| **Docker Desktop** | *Only* for Option B. Free install: <https://docs.docker.com/desktop/>                |

> 💡 **Tip** – Check tools for terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (fastest)

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

✅ Prompt go start with (.venv) now—that mean you dey inside the env.

### Step 3 Install dependencies

```bash
pip install -r requirements.txt
```

Skip go Section 3 for [API keys](../../../00-course-setup)

## 2. Option B – VS Code Dev Container (Docker)

We set up dis repository and course with one [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) wey get Universal runtime wey fit support Python3, .NET, Node.js and Java development. The configuration dey inside `devcontainer.json` file wey dey `.devcontainer/` folder for root of dis repository.

>**Why you go choose dis?**
>Environment na the same as Codespaces; no wahala with dependency drift.

### Step 0 Install the extras

Docker Desktop – confirm say ```docker --version``` dey work.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Step 1 Open the repo for VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code go detect .devcontainer/ and go show prompt.

### Step 2 Reopen inside container

Click “Reopen in Container”. Docker go build the image (≈ 3 min first time).
When terminal prompt show, you dey inside the container.

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na small installer for installing [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, plus some packages.
Conda na package manager wey make am easy to set up and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E still good for installing packages wey no dey available via `pip`.

### Step 0  Install Miniconda

Follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set am up.

```bash
conda --version
```

### Step 1 Create virtual environment

Create new environment file (*environment.yml*). If you dey follow for Codespaces, create am inside `.devcontainer` directory, so `.devcontainer/environment.yml`.

### Step 2  Add to your environment file

Put dis snippet inside your  `environment.yml`

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

Run the commands below for your command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path na only for Codespace setups e dey apply
conda activate ai4beg
```

If you get any problem, check the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Option D – Classic Jupyter / Jupyter Lab (for your browser)

> **Who dis one dey for?**  
> Anybody wey like the classic Jupyter interface or want run notebooks without VS Code.  

### Step 1  Make sure Jupyter dey installed

To start Jupyter locally, go terminal/command line, waka go the course directory, then run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Dis one go start Jupyter instance and the URL to access am go show for command line window.

When you open the URL, you go see the course outline and fit waka go any `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Add Your API Keys

To keep your API keys safe and secure na important thing when you dey build any kind application. We recommend say no store any API keys directly for your code. If you put those details for public repository, e fit cause security wahala and even unwanted cost if bad person use am.
Here na step-by-step guide on how to create `.env` file for Python and add `GITHUB_TOKEN`:

1. **Waka go Your Project Directory**: Open your terminal or command prompt and waka go your project's root directory wey you want create `.env` file.

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

3. **Edit `.env` File**: Open `.env` file for text editor (e.g., VS Code, Notepad++, or any other editor). Add dis line inside the file, change `your_github_token_here` to your real GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Save the File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you never install am before, you go need install `python-dotenv` package to load environment variables from `.env` file into your Python app. You fit install am with `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables for Your Python Script**: For your Python script, use `python-dotenv` package to load environment variables from `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Na so e be! You don create `.env` file, add your GitHub token, and load am inside your Python app.

🔐 No ever commit .env—e don dey inside .gitignore.
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
| `python not found`                        | Add Python to PATH or open terminal again after install         |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` then try again.    |
| `ModuleNotFoundError: dotenv`             | Run `pip install -r requirements.txt` (env no install).         |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → increase disk size. |
| VS Code dey always ask to reopen           | You fit get both Options active; choose one (venv **or** container)|
| OpenAI 401 / 429 errors                   | Check `OPENAI_API_KEY` value / request rate limits.             |
| Errors with Conda                        | Install Microsoft AI libraries with `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or no too correct. Di original document wey e dey for im own language na di correct one. If na serious matter, e better make human professional translate am. We no go responsible for any wahala or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->