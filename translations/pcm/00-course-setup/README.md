# Getting Started with this course

We dey very excited for you to start dis course and see wetin go fit inspire you to build wit Generative AI!

To make sure say you go succeed, dis page go outline setup steps, technical requirements, and where you fit find help if you need am.

## Setup Steps

To start to take dis course, you go need to complete dis following steps.

### 1. Fork this Repo

[Fork dis entire repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) go your own GitHub account so that you fit change any code and complete the challenges. You fit also [star (🌟) dis repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) to find am and related repos easier.

### 2. Create a codespace

To avoid any wahala with dependencies when you dey run code, we recommend say you run dis course inside [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Inside your fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pcm/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Add a secret

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name OPENAI_API_KEY, paste your key, Save.

### 3.  Wetin next?

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
| `python: command not found`               | Terminal no connect; click **+** ➜ *bash*                    |
| `401 Unauthorized` from OpenAI            | Wrong / expired `OPENAI_API_KEY`                                |
| VS Code shows “Dev container mounting…”   | Refresh the browser tab—Codespaces sometimes loses connection   |
| Notebook kernel missing                   | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit the `.env` File**: Open the `.env` file inside any text editor (example, VS Code, Notepad++, or any other editor). Add dis line inside the file, replace `your_github_token_here` with your real GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Save the File**: Save the changes and close the text editor.

5. **Install `python-dotenv`**: If you never install am before, you go need to install the `python-dotenv` package to load environment variables from the `.env` file go your Python application. You fit install am with `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables in Your Python Script**: Inside your Python script, use the `python-dotenv` package to load the environment variables from the `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Na im be that! You don successfully create a `.env` file, add your GitHub token, and load am for your Python app.

## How to Run locally on your computer

To run the code locally for your computer, you go need make sure say you get some version of [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

To use the repository, you go need to clone am:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

After you don check everything finish, you fit start!

## Optional Steps

### Installing Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) na light installer wey you fit use install [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, plus some packages.
Conda na package manager wey e make easy to setup and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. E still good for installing packages wey no dey for pip.

You fit follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set am up.

After you install Miniconda, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you never do am before)

Next, you need to create a virtual environment. To do dis with Conda, create new environment file (_environment.yml_). If you dey use Codespaces, create dis inside the `.devcontainer` folder, meaning `.devcontainer/environment.yml`.

Go ahead and put dis snippet inside your environment file:

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

If you see say you dey get errors when you use conda, you fit manually install the Microsoft AI Libraries by running the command wey dey below for terminal.

```
conda install -c microsoft azure-ai-ml
```

The environment file dey show the dependencies we need. `<environment-name>` na the name wey you want use for your Conda environment, and `<python-version>` na the Python version we want run, example, `3` na the latest major Python version.

After dis one finish, you fit run the commands below for your command line/terminal to create your Conda environment

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path dey work only for Codespace setups
conda activate ai4beg
```

If you get any wahala, check the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Using Visual Studio Code with the Python support extension

We recommend say you use the [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor with the [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installed for dis course. But na just recommendation, no be strict requirement.

> **Note**: When you open the course repository inside VS Code, you fit choose to set up the project inside a container. Na because of the [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) folder wey dey inside the course repository. More about dis later.

> **Note**: When you clone and open the folder inside VS Code, e go suggest say make you install Python support extension automatically.

> **Note**: If VS Code suggest say reopen the repository inside container, make you say no because you wan use the Python version wey dey your machine.

### Using Jupyter in the Browser

You fit also work on the project inside [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) right inside your browser. Both the classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) dey give better developer experience with features like auto-completion, code highlighting, and more.

To start Jupyter locally, open your terminal/command line, go the course folder, then run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

This one go start Jupyter plus the URL where you fit open am go show for your command line window.

Once you open the URL, you go see the course outline and you fit enter any `*.ipynb` file. Example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

Another way to set everything up for your computer or Codespace na to use [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). The special `.devcontainer` folder inside the course repo dey make VS Code fit setup the project inside container. Outside Codespaces, dis one need Docker installation and e get some work involved, so we recommend am mainly to people wey get experience with containers.

One of the best ways to keep your API keys safe when you dey use GitHub Codespaces na to use Codespace Secrets. Abeg follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to sabi more.

## Lessons and Technical Requirements

The course get 6 concept lessons and 6 coding lessons.

For the coding lessons, we dey use Azure OpenAI Service. You go need access to Azure OpenAI service and API key to run dis code. You fit apply for access by [completing dis application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you dey wait for your application to dey processed, each coding lesson get `README.md` file where you fit see the code and outputs.

## Using the Azure OpenAI Service for the first time

If dis na your first time to dey work with Azure OpenAI service, abeg follow dis guide on how to [create and deploy Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Using the OpenAI API for the first time

If dis na your first time to dey work with OpenAI API, abeg follow the guide on how to [create and use the Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We don create channels for our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) to meet other learners. E good way to connect with other entrepreneurs, builders, students, and anybody wey wan improve for Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

The project team go also dey inside this Discord server to help any learners.

## Contribute

Dis course na open-source initiative. If you see areas wey fit improve or you find any issues, abeg create a [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or log a [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

The project team go dey track all contributions. To contribute for open source na good way to build your career inside Generative AI.

Most contributions need say you agree to Contributor License Agreement (CLA) wey go talk say you get rights and you give us rights to use your contribution. For details, visit [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: When you dey translate text for dis repo, abeg make sure say you no dey use machine translation. We go verify translations through the community, so abeg only volunteer to translate for languages wey you sabi well.

When you submit pull request, CLA-bot go automatically check whether you need to provide CLA and go add correct decoration for PR (like label or comment). Just follow wetin the bot talk. You go only need do am once for all repos wey dey use our CLA.

Dis project don adopt the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more information, read Code of Conduct FAQ or contact [Email opencode](opencode@microsoft.com) if you get any questions or comments.

## Let's Get Started
Now wey you don complete all di steps wey you need to complete dis course, make we start by to get [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make am correct, abeg sabi say automated translation fit get mistakes or no too correct. Di original document wey dem write for im own language na di correct one. If na serious information, make person wey sabi translate am human way do am. We no go responsible for any wrong understanding or confusion wey come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->