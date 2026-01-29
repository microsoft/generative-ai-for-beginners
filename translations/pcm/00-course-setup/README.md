# How to Start Dis Course

We dey very happy say you wan start dis course and we dey look forward to wetin you go fit create wit Generative AI!

To make sure say you go succeed, dis page go show you how to setup, wetin you need technically, and where you fit find help if you need am.

## Steps to Setup

To start dis course, you go need complete dis steps.

### 1. Fork Dis Repo

[Fork dis repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) go your own GitHub account so you fit change any code and complete di challenges. You fit also [star (🌟) dis repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) so e go dey easy to find am and other related repos.

### 2. Create Codespace

To avoid wahala wit dependencies when you dey run di code, we dey recommend say make you run dis course inside [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

For your fork: **Code -> Codespaces -> New on main**

![Dialog wey show buttons to create codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Add Secret

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add new secret.
2. Name OPENAI_API_KEY, paste your key, Save.

### 3. Wetin Next?

| I wan…              | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Work offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Setup LLM Provider  | [`providers.md`](03-providers.md)                                       |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Troubleshooting

| Problem wey you see                          | Wetin you go do                                               |
|---------------------------------------------|-------------------------------------------------------------|
| Container build dey stuck > 10 min          | **Codespaces ➜ “Rebuild Container”**                        |
| `python: command not found`                 | Terminal no attach; click **+** ➜ *bash*                    |
| `401 Unauthorized` from OpenAI              | Wrong / expired `OPENAI_API_KEY`                            |
| VS Code dey show “Dev container mounting…”  | Refresh browser tab—Codespaces fit lose connection          |
| Notebook kernel no dey                       | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit `.env` File**: Open `.env` file for text editor (e.g., VS Code, Notepad++, or any other editor). Add dis line to di file, replace `your_github_token_here` wit your real GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Save File**: Save di changes and close di text editor.

5. **Install `python-dotenv`**: If you never install am before, you go need install `python-dotenv` package to load environment variables from `.env` file go your Python app. Use `pip` to install am:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables for Your Python Script**: For your Python script, use `python-dotenv` package to load di environment variables from `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Na all be dat! You don create `.env` file, add your GitHub token, and load am for your Python app.

## How to Run Locally for Your Computer

To run di code for your computer, you go need install one version of [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

To use di repo, you go need clone am:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Once you don check everything out, you fit start!

## Optional Steps

### Install Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na lightweight installer for [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, and some packages. Conda na package manager wey dey make am easy to setup and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E dey useful for installing packages wey no dey `pip`.

Follow [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to setup.

If you don install Miniconda, clone di [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you never do am before).

Next, create virtual environment. Use Conda to create new environment file (_environment.yml_). If you dey use Codespaces, create am inside `.devcontainer` directory, so `.devcontainer/environment.yml`.

Add dis snippet to your environment file:

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

If you dey get errors wit conda, you fit manually install Microsoft AI Libraries wit dis command for terminal:

```
conda install -c microsoft azure-ai-ml
```

Di environment file dey specify di dependencies wey we need. `<environment-name>` na di name wey you wan use for your Conda environment, and `<python-version>` na di Python version wey you wan use, e.g., `3` na di latest major version.

After dat, create your Conda environment wit dis commands for terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Check [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if you get any wahala.

### Use Visual Studio Code wit Python Extension

We dey recommend [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor wit [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) for dis course. But e no be must.

> **Note**: If you open di course repo for VS Code, you fit setup di project inside container because of di [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) folder wey dey di repo. More info dey later.

> **Note**: Once you clone and open di directory for VS Code, e go suggest make you install Python extension.

> **Note**: If VS Code suggest make you re-open di repo for container, no accept am so you go fit use di Python wey dey your computer.

### Use Jupyter for Browser

You fit work on di project wit [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) for browser. Both classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) dey give better development experience wit features like auto-completion, code highlighting, etc.

To start Jupyter locally, go terminal/command line, go di course directory, and run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Dis go start Jupyter instance and URL to access am go show for command line window.

Once you access di URL, you go see di course outline and fit navigate to any `*.ipynb` file. Example, `08-building-search-applications/python/oai-solution.ipynb`.

### Run Inside Container

Another way to setup everything na to use [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Di `.devcontainer` folder for di course repo dey make am possible for VS Code to setup di project inside container. If you no dey use Codespaces, you go need install Docker, but e dey involve small work, so we dey recommend am for people wey sabi containers.

One better way to keep your API keys safe for GitHub Codespaces na to use Codespace Secrets. Follow [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more.

## Lessons and Technical Requirements

Dis course get 6 concept lessons and 6 coding lessons.

For di coding lessons, we dey use Azure OpenAI Service. You go need access to Azure OpenAI service and API key to run di code. Apply for access by [completing dis application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you dey wait for your application, each coding lesson get `README.md` file wey you fit use to see di code and outputs.

## Use Azure OpenAI Service for Di First Time

If na your first time to use Azure OpenAI service, follow dis guide on how to [create and deploy Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Use OpenAI API for Di First Time

If na your first time to use OpenAI API, follow dis guide on how to [create and use di Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We don create channels for our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) to meet other learners. E good to network wit other people wey dey interested for Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Di project team go dey di Discord server to help learners.

## Contribute

Dis course na open-source project. If you see areas wey fit improve or issues, create [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or log [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Di project team go dey track all contributions. To contribute to open source na better way to build your career for Generative AI.

Most contributions go need you to agree to Contributor License Agreement (CLA) wey go show say you get di right to and actually dey give us di rights to use your contribution. For details, visit [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: when you dey translate text for dis repo, make sure say you no use machine translation. We go verify translations wit di community, so only volunteer for translations for languages wey you sabi well.

When you submit pull request, CLA-bot go automatically check if you need provide CLA and decorate di PR well (e.g., label, comment). Just follow di instructions wey di bot give. You go only need do dis once for all repos wey dey use our CLA.

Dis project don adopt [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more info, read Code of Conduct FAQ or contact [Email opencode](opencode@microsoft.com) if you get any extra questions or comments.

## Make We Start
Now wey you don finish di steps wey you need to complete dis course, make we start by getting [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->