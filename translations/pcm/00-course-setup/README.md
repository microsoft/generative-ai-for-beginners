# How to start dis course

We very happy say you wan start dis course and see wetin you go fit build with Generative AI weh go inspire you!

To make sure say you succeed, dis page go show you how to set up, technical tins wey you go need, and where you fit get help if you need am.

## Setup Steps

To start to take dis course, you go need do dis kain steps.

### 1. Fork dis Repo

[Fork dis whole repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) go your own GitHub account so you fit change any code and finish all the challenges dem. You fit also [star (🌟) dis repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) so e go easy for you to find dis and other related repos.

### 2. Create a codespace

To avoid wahala with dependencies when you dey run code, we dey recommend make you run dis course inside [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

For your fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pcm/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Add a secret

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name OPENAI_API_KEY, paste your key, Save.

### 3. Wetin next?

| I want to…          | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Work offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Setup an LLM Provider | [`providers.md`](03-providers.md)                                        |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Troubleshooting


| Symptom                                   | Fix                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build stuck > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal no connect; click **+** ➜ *bash*                       |
| `401 Unauthorized` from OpenAI            | Wrong/no good `OPENAI_API_KEY`                                  |
| VS Code shows “Dev container mounting…”   | Refresh the browser tab—Codespaces fit lose connection          |
| Notebook kernel missing                   | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit the `.env` File**: Open the `.env` file for text editor (for example, VS Code, Notepad++, or any editor wey you like). Add this lines for the file, change the placeholders to your real Microsoft Foundry Models endpoint and key (check [`providers.md`](03-providers.md) to see how to get dem):

   > **Note:** GitHub Models (and e `GITHUB_TOKEN` variable) go stop work by the end of July 2026. Use [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) instead.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Save the File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you never install am yet, you need to install `python-dotenv` package so your Python app fit load environment variables from the `.env` file. You fit install am with `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables for Your Python Script**: For your Python script, use `python-dotenv` package make e load environment variables from the `.env` file:

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

Na so e be! You don successfully create `.env` file, add your Microsoft Foundry Models credentials, and load dem inside your Python app.

## How to Run locally for your computer

To run code locally for your computer, you go need to get one version of [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Then, to use the repository, you need to clone am:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

After you don check everything, you fit start dey work!

## Optional Steps

### Installing Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na small installer to install [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, and some packages.
Conda na package manager wey e easy to set up and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E still help install packages wey you no fit get with `pip`.

You fit follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set am up.

After you don install Miniconda, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you never do am before)

Next, you need create virtual environment. To do am with Conda, make new environment file (_environment.yml_). If you dey use Codespaces, create am inside `.devcontainer` directory, so `.devcontainer/environment.yml`.

Put dis snippet for your environment file:

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

If conda dey give you wahala, you fit manually install Microsoft AI Libraries with this command for terminal.

```
conda install -c microsoft azure-ai-ml
```

The environment file dey tell all the dependencies wey we need. `<environment-name>` na the name you want give your Conda environment, and `<python-version>` na the Python version you wan use, for example, `3` na the latest Python version.

After dat, create your Conda environment by running dis commands for your command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path dey apply only for Codespace setups
conda activate ai4beg
```

If you get any problem, check the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Using Visual Studio Code with Python support extension

We recommend make you use [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor with the [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installed for dis course. But na just recommendation, no be like say na must.

> **Note**: If you open course repo for VS Code, you fit set the project to run inside container. Dis na because of [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory inside course repo. We go talk more about dis later.

> **Note**: Once you clone and open the directory for VS Code, e go automatically suggest make you install Python support extension.

> **Note**: If VS Code tell you make you open the repo again inside container, reject am if you want use local Python version.

### Using Jupyter for the Browser

You fit also work for the project using [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) inside browser. Both classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) give better development environment with features like auto-completion, code highlighting, etc.

To start Jupyter locally, go terminal/command line, enter course directory, then run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Dis go start Jupyter and the URL to open am go show for the command line window.

Once you open the URL, you go see course outline and fit waka go any `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running inside container

The other way to set everything up for computer or Codespace na to use [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Special `.devcontainer` folder inside course repo fit make VS Code fit set the project inside container. Outside Codespaces, you go need install Docker, and to be honest, e get how e hard small, so we recommend am only for people wey sabi work with containers.

One best way to keep your API keys safe when you dey use GitHub Codespaces na to use Codespace Secrets. Abeg follow [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more.


## Lessons and Technical Requirements

Dis course get "Learn" lessons wey dey explain Generative AI concepts plus "Build" lessons wey get hands-on code examples for both **Python** and **TypeScript** where e possible.

For coding lessons, we dey use Azure OpenAI for Microsoft Foundry. You go need Azure subscription and API key. Access open - no need apply - so you fit [create Microsoft Foundry resource and deploy model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) to collect your endpoint and key.

Every coding lesson get `README.md` file wey you fit use see code and outputs without running anything.

## How to Use Azure OpenAI Service for di first time

If na your first time you dey use Azure OpenAI service, abeg follow dis guide on how to [create and deploy Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## How to Use OpenAI API for di first time

If na your first time you dey use OpenAI API, abeg follow dis guide on how to [create and use Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We don create channels for our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) make people fit meet other learners. Dis na good way to network with other people wey dey try, builders, students, and anybody wey wan improve for Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Project team go also dey for dis Discord server to help learners.

## Contribute

Dis course na open-source project. If you see any place wey you fit improve or get wahala, abeg create [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or report as [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Project team dey track all contributions. To contribute to open source na better way to push your career for Generative AI.

Most contributions go need say you agree to Contributor License Agreement (CLA) where you go say you get the right and you really give us the rights to use your contribution. For details, visit [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: When you dey translate text for this repo, abeg make sure say you no use machine translation. We go check translations through community, so abeg only volunteer for translations for languages wey you sabi well.


Wen yu submit pull request, CLA-bot go automatically sabi whether yu need provide CLA and put correct label or comment for the PR. Just follow wetin di bot tok. Yu go do am only one time for all di reposwey dem wey dey use our CLA.

Dis project don use [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more gist read di Code of Conduct FAQ or hala [Email opencode](opencode@microsoft.com) if you get any question or comment.

## Make we Start

Now wey you don finish all di steps wey you gats do to complete dis course, make we start by getting [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->