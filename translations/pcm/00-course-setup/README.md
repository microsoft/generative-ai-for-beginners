# How to Start dis course

We dey very happy make you start dis course and see wetin go inspire you to build with Generative AI!

To make sure say you go succeed, dis page go show you how to set up, wetin you need for technical side, and where to find help if you need am.

## Setup Steps

To begin this course, you go need finish these steps.

### 1. Fork dis Repo

[Fork dis whole repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) go your own GitHub account so you fit change any code and finish the challenges. You fit also [star (🌟) dis repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) to fit find am and related repos easier.

### 2. Create a codespace

To avoid wahala with dependencies when you dey run code, we recommend say you run this course for [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

For your fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pcm/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Add one secret

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add one new secret.
2. Name am OPENAI_API_KEY, paste your key, then Save.

### 3. Wetin next?

| I want to…          | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Work offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Setup one LLM Provider | [`providers.md`](03-providers.md)                                        |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Troubleshooting


| Symptom                                   | How to fix am                                                  |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build dey stuck pass 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal no connect; click **+** ➜ *bash*                    |
| `401 Unauthorized` from OpenAI            | Wrong / expired `OPENAI_API_KEY`                                |
| VS Code dey show “Dev container mounting…”   | Refresh your browser tab—sometimes Codespaces lose connection   |
| Notebook kernel no dey                     | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit the `.env` File**: Open the `.env` file for text editor (like VS Code, Notepad++, or any other editor). Add these lines for the file, switch the placeholders with your real Microsoft Foundry Models endpoint and key (check [`providers.md`](03-providers.md) for how to get these):

   > **Note:** GitHub Models (and e `GITHUB_TOKEN` variable) go stop by end of July 2026. Use [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) instead.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Save the File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you never install am before, you go need install `python-dotenv` package to load environment variables from `.env` file enter your Python app. You fit install am with `pip`:

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

Na so e be! You don successfully create `.env` file, add your Microsoft Foundry Models credentials, and load dem inside your Python app.

## How to Run locally for your computer

To run code locally for your computer, you go need get some version of [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

To use the repository, you go need clone am:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Once you get everything ready, you fit start!

## Optional Steps

### Installing Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na light installer wey fit install [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, plus some packages.
Conda na package manager, wey make e easy to setup and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E still good for installing packages wey no dey available via `pip`.

You fit follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set am up.

After you install Miniconda, you go need clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you never do am before)

Next, you go need create virtual environment. To do am with Conda, create new environment file (_environment.yml_). If you dey follow with Codespaces, create dis inside the `.devcontainer` folder, so `.devcontainer/environment.yml`.

Put this snippet inside your environment file:

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

If you dey get errors with conda, you fit manually install Microsoft AI Libraries using dis command for terminal.

```
conda install -c microsoft azure-ai-ml
```

The environment file dey show the dependencies we need. `<environment-name>` na the name wey you want use for your Conda environment, and `<python-version>` na the version of Python you want use, example, `3` na the latest major Python version.

After dat, you fit create your Conda environment by running these commands for your command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path na only for Codespace setups e dey apply
conda activate ai4beg
```

Check [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if you get any wahala.

### Using Visual Studio Code with Python support extension

We recommend say you use [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor plus [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) wey dem install for dis course. But na only recommendation e be, e no mandatory.

> **Note**: If you open course repository for VS Code, you fit choose set project up for container. Na because of special [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) folder wey dey for course repository. We go talk more about dis later.

> **Note**: Once you clone and open the directory for VS Code, e go automatically suggest you install Python support extension.

> **Note**: If VS Code dey suggest you reopen the repository inside container, decline am if you want use the Python wey dey your local machine.

### Using Jupyter inside Browser

You fit also work for the project by using [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) inside your browser. Both classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) dey give correct development environment with features like auto-completion, code highlighting, and others.

To start Jupyter locally, waka go terminal/command line, enter course directory, then run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

This one go start Jupyter instance and URL wey you go use access am go show inside command line window.

Once you access the URL, you go see course outline and fit waka go any `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running inside container

Another way to set everything for your computer or Codespace na to use [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). The special `.devcontainer` folder inside course repository make VS Code fit set up project inside container. If you no dey use Codespaces, you go need install Docker, and truly, e take small work, so we recommend am only to people wey don sabi work with containers before.

Best way to keep your API keys safe when you dey use GitHub Codespaces na to use Codespace Secrets. Please follow [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to sabi more about this.


## Lessons and Technical Requirements

The course get 6 concept lessons and 6 coding lessons.

For the coding lessons, we dey use Azure OpenAI Service. You go need access to Azure OpenAI service and API key to run this code. You fit apply for access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you dey wait for your application, each coding lesson get `README.md` file wey you go fit see code and outputs.

## Using the Azure OpenAI Service for the first time

If na your first time to work with Azure OpenAI service, abeg follow how to [create and deploy Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Using the OpenAI API for the first time

If na your first time to work with OpenAI API, abeg follow guide on how to [create and use the Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We don create channels for our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) to meet other learners. Na beta way to network with other entrepreneurs, builders, students, and anybody wey want grow for Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

The project team go also dey for this Discord server to help learners.

## Contribute

Dis course na open-source work. If you see place wey fit improve or issues, abeg create [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or log [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

The project team go dey track all contributions. Contribute for open source na beta way to build your career for Generative AI.

Most contributions need say you agree to Contributor License Agreement (CLA) wey talk say you get right and actually give us right to use your contribution. For details, visit [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: when you dey translate text for dis repo, make sure say you no dey use machine translation. We go check translations through community, so abeg only volunteer for translations for languages wey you sabi well.

When you submit pull request, CLA-bot go automatically check if you need provide CLA and go put correct label or comment for PR. Just follow instructions wey the bot give. You go only need do this once for all repos wey dey use our CLA.


Dis project don adopt di [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more info, read di Code of Conduct FAQ or contact [Email opencode](opencode@microsoft.com) if you get any oda questions or comments.

## Make we begin

Now wey you don finish di steps wey you need to complete dis course, make we start by getting [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->