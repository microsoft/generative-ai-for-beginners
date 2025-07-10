<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T06:57:36+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "en"
}
-->
# Getting Started with this course

We’re excited for you to begin this course and see what you’re inspired to create with Generative AI!

To help you succeed, this page outlines the setup steps, technical requirements, and where to find help if needed.

## Setup Steps

To start this course, you’ll need to complete the following steps.

### 1. Fork this Repo

[Fork this entire repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) to your own GitHub account so you can modify the code and complete the challenges. You can also [star (🌟) this repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) to find it and related repos more easily.

### 2. Create a codespace

To avoid dependency issues when running the code, we recommend using [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

You can create one by selecting the `Code` button on your forked repo and choosing the **Codespaces** option.

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Storing Your API Keys

Keeping your API keys safe is crucial when building any application. We recommend not storing API keys directly in your code. Committing them to a public repo can lead to security risks and unexpected costs if misused.

Here’s a step-by-step guide to creating a `.env` file for Python and adding your `GITHUB_TOKEN`:

1. **Navigate to Your Project Directory**: Open your terminal or command prompt and go to your project’s root directory where you want to create the `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Create the `.env` File**: Use your preferred text editor to create a new file named `.env`. From the command line, you can use `touch` (Unix-based systems) or `echo` (Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit the `.env` File**: Open `.env` in a text editor (e.g., VS Code, Notepad++, or any other editor). Add the following line, replacing `your_github_token_here` with your actual GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Save the File**: Save and close the editor.

5. **Install `python-dotenv`**: If you haven’t already, install the `python-dotenv` package to load environment variables from the `.env` file into your Python app. Use `pip` to install it:

   ```bash
   pip install python-dotenv
   ```

6. **Load Environment Variables in Your Python Script**: In your Python script, use `python-dotenv` to load the variables from `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

That’s it! You’ve created a `.env` file, added your GitHub token, and loaded it into your Python app.

## How to Run locally on your computer

To run the code locally, you’ll need to have [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Then, clone the repository:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Once everything is set up, you’re ready to get started!

## Optional Steps

### Installing Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is a lightweight installer for [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, and some packages.

Conda is a package manager that makes it easy to create and switch between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. It’s also useful for installing packages not available via `pip`.

Follow the [Miniconda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

After installing Miniconda, clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) if you haven’t already.

Next, create a virtual environment. With Conda, create a new environment file (_environment.yml_). If you’re using Codespaces, place this inside the `.devcontainer` directory as `.devcontainer/environment.yml`.

Add the following snippet to your environment file:

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

If you encounter errors using conda, you can manually install the Microsoft AI Libraries with this command in a terminal:

```
conda install -c microsoft azure-ai-ml
```

The environment file lists the dependencies needed. `<environment-name>` is the name you want for your Conda environment, and `<python-version>` is the Python version you want to use (e.g., `3` for the latest major version).

Once ready, create your Conda environment by running these commands in your terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

If you run into issues, see the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Using Visual Studio Code with the Python support extension

We recommend using [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) for this course. This is a recommendation, not a strict requirement.

> **Note**: Opening the course repo in VS Code lets you set up the project inside a container, thanks to the special [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) folder in the repo. More on this later.

> **Note**: After cloning and opening the repo in VS Code, it will prompt you to install the Python extension.

> **Note**: If VS Code suggests reopening the repo in a container, decline if you want to use your local Python installation.

### Using Jupyter in the Browser

You can also work on the project using [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) right in your browser. Both classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offer a smooth development experience with features like auto-completion and syntax highlighting.

To start Jupyter locally, open your terminal, navigate to the course directory, and run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

This will launch a Jupyter instance, and the URL to access it will appear in the terminal.

Once you open the URL, you’ll see the course outline and can open any `*.ipynb` file, for example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

Instead of setting everything up on your computer or Codespace, you can use a [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). The `.devcontainer` folder in the repo allows VS Code to set up the project inside a container.

Outside of Codespaces, this requires installing Docker and some setup, so we recommend this only if you have experience with containers.

One of the best ways to keep your API keys secure in GitHub Codespaces is by using Codespace Secrets. Follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more.

## Lessons and Technical Requirements

The course includes 6 concept lessons and 6 coding lessons.

For the coding lessons, we use the Azure OpenAI Service. You’ll need access to Azure OpenAI and an API key to run the code. You can apply for access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While waiting for your application, each coding lesson also includes a `README.md` file where you can view the code and outputs.

## Using the Azure OpenAI Service for the first time

If you’re new to Azure OpenAI, follow this guide on how to [create and deploy an Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Using the OpenAI API for the first time

If you’re new to the OpenAI API, follow the guide on how to [create and use the Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We’ve set up channels in our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) to connect with other learners. It’s a great way to network with entrepreneurs, builders, students, and anyone looking to advance in Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

The project team will also be active on this Discord to support learners.

## Contribute

This course is open source. If you find areas for improvement or issues, please create a [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or open a [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

The project team tracks all contributions. Contributing to open source is a great way to build your career in Generative AI.

Most contributions require agreeing to a Contributor License Agreement (CLA), confirming you have the rights to grant us permission to use your contribution. For details, visit the [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: when translating text in this repo, please avoid using machine translation. We verify translations through the community, so only volunteer for languages you’re proficient in.

When you submit a pull request, a CLA-bot will check if you need to sign a CLA and will label or comment accordingly. Just follow the bot’s instructions. You only need to do this once across all repos using our CLA.

This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more info, read the Code of Conduct FAQ or contact [Email opencode](opencode@microsoft.com) with questions or comments.

## Let's Get Started

Now that you’ve completed the setup steps, let’s begin with an [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.