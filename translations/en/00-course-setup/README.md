<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T13:17:18+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "en"
}
-->
# Getting Started with this course

We’re excited for you to begin this course and see what you’ll be inspired to build with Generative AI!

To help you succeed, this page covers setup steps, technical requirements, and where to get help if you need it.

## Setup Steps

To start this course, you’ll need to complete the following steps.

### 1. Fork this Repo

[Fork this entire repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) to your own GitHub account so you can modify code and complete the challenges. You can also [star (🌟) this repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) to make it and related repos easier to find.

### 2. Create a codespace

To avoid dependency issues when running the code, we recommend using [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) for this course.

In your fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Add a secret

1. ⚙️ Gear icon -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Name it OPENAI_API_KEY, paste your key, and Save.

### 3.  What’s next?

| I want to…          | Go to…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Work offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Setup an LLM Provider | [`providers.md`](providers.md)                                        |
| Meet other learners | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Troubleshooting

| Symptom                                   | Fix                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build stuck > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal didn’t attach; click **+** ➜ *bash*                    |
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

3. **Edit the `.env` File**: Open the `.env` file in a text editor (e.g., VS Code, Notepad++, or any other editor). Add the following line to the file, replacing `your_github_token_here` with your actual GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Save the File**: Save your changes and close the text editor.

5. **Install `python-dotenv`**: If you haven’t already, you’ll need to install the `python-dotenv` package to load environment variables from the `.env` file into your Python application. You can install it using `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables in Your Python Script**: In your Python script, use the `python-dotenv` package to load the environment variables from the `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

That’s it! You’ve successfully created a `.env` file, added your GitHub token, and loaded it into your Python application.

## How to Run locally on your computer

To run the code locally, you’ll need to have [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

To use the repository, you need to clone it:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Once you have everything checked out, you’re ready to get started!

## Optional Steps

### Installing Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is a lightweight installer for [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, and a few packages.
Conda is a package manager that makes it easy to set up and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. It’s also useful for installing packages not available via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven’t already).

Next, create a virtual environment. To do this with Conda, create a new environment file (_environment.yml_). If you’re following along in Codespaces, create this within the `.devcontainer` directory, so `.devcontainer/environment.yml`.

Fill your environment file with the snippet below:

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

If you run into errors using conda, you can manually install the Microsoft AI Libraries using the following command in a terminal.

```
conda install -c microsoft azure-ai-ml
```

The environment file lists the dependencies you need. `<environment-name>` is the name you want for your Conda environment, and `<python-version>` is the Python version you want to use, for example, `3` is the latest major version.

Once that’s done, you can create your Conda environment by running the commands below in your command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Check the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if you have any issues.

### Using Visual Studio Code with the Python support extension

We recommend using [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) with the [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) for this course. This is just a recommendation, not a strict requirement.

> **Note**: By opening the course repository in VS Code, you can set up the project in a container. This is possible because of the [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory in the course repository. More on this later.

> **Note**: Once you clone and open the directory in VS Code, it will automatically suggest installing a Python support extension.

> **Note**: If VS Code suggests reopening the repository in a container, decline to use your locally installed Python.

### Using Jupyter in the Browser

You can also work on the project using the [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) right in your browser. Both classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offer a great development environment with features like auto-completion, code highlighting, and more.

To start Jupyter locally, open your terminal/command line, navigate to the course directory, and run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

This will start a Jupyter instance and display the URL to access it in the command line window.

Once you access the URL, you should see the course outline and be able to open any `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

Another way to set everything up, besides on your computer or Codespace, is to use a [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). The special `.devcontainer` folder in the course repository lets VS Code set up the project in a container. Outside of Codespaces, this requires installing Docker, and it’s a bit more involved, so we recommend it only for those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we use the Azure OpenAI Service. You’ll need access to the Azure OpenAI service and an API key to run this code. You can apply for access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` file where you can view the code and outputs.

## Using the Azure OpenAI Service for the first time

If this is your first time using the Azure OpenAI service, please follow this guide on how to [create and deploy an Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Using the OpenAI API for the first time

If this is your first time using the OpenAI API, please follow the guide on how to [create and use the Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We’ve set up channels in our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for meeting other learners. It’s a great way to connect with other entrepreneurs, builders, students, and anyone looking to grow in Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

The project team will also be on this Discord server to help learners.

## Contribute

This course is an open-source project. If you see areas for improvement or issues, please create a [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or log a [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

The project team will track all contributions. Contributing to open source is a great way to build your career in Generative AI.

Most contributions require you to agree to a Contributor License Agreement (CLA) stating that you have the right to, and do, grant us the rights to use your contribution. For details, visit the [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: when translating text in this repo, please make sure not to use machine translation. We will verify translations through the community, so only volunteer for languages you are proficient in.

When you submit a pull request, a CLA-bot will automatically check if you need to provide a CLA and will update the PR accordingly (e.g., label, comment). Just follow the instructions from the bot. You only need to do this once across all repositories using our CLA.

This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more information, read the Code of Conduct FAQ or contact [Email opencode](opencode@microsoft.com) with any additional questions or comments.

## Let's Get Started
Now that you have finished the necessary steps to complete this course, let's begin with an [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.