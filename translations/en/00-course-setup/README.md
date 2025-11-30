<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T22:31:13+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "en"
}
-->
# Getting Started with this course

We are thrilled for you to begin this course and discover what you can create with Generative AI!

To help you succeed, this page provides setup instructions, technical requirements, and guidance on where to find support if needed.

## Setup Steps

To start this course, please follow these steps:

### 1. Fork this Repository

[Fork this entire repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) to your own GitHub account so you can modify the code and complete the challenges. You can also [star (🌟) this repository](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) to easily locate it and related repositories.

### 2. Create a Codespace

To avoid dependency issues when running the code, we recommend using [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) for this course.

In your fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Add a Secret

1. ⚙️ Gear icon -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.
2. Name it OPENAI_API_KEY, paste your key, and save.

### 3. What’s next?

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
| `python: command not found`               | Terminal didn’t attach; click **+** ➜ *bash*                    |
| `401 Unauthorized` from OpenAI            | Incorrect or expired `OPENAI_API_KEY`                           |
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

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

That's it! You've successfully created a `.env` file, added your GitHub token, and loaded it into your Python application.

## How to Run Locally on Your Computer

To run the code locally on your computer, you need to have a version of [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

To use the repository, clone it:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Once everything is set up, you can start working!

## Optional Steps

### Installing Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is a lightweight installer for [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, and some packages. Conda is a package manager that simplifies setting up and switching between different Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) and packages. It’s also useful for installing packages not available via `pip`.

Follow the [Miniconda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

Once Miniconda is installed, clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven’t already).

Next, create a virtual environment. Using Conda, create a new environment file (_environment.yml_). If you’re using Codespaces, create this file within the `.devcontainer` directory, so it becomes `.devcontainer/environment.yml`.

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

If you encounter errors with Conda, you can manually install the Microsoft AI Libraries using the following command in a terminal:

```
conda install -c microsoft azure-ai-ml
```

The environment file specifies the required dependencies. `<environment-name>` is the name you want for your Conda environment, and `<python-version>` is the Python version you want to use, e.g., `3` for the latest major version.

Once done, create your Conda environment by running the following commands in your terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Refer to the [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) if you encounter any issues.

### Using Visual Studio Code with the Python Support Extension

We recommend using [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) with the [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installed for this course. However, this is just a recommendation, not a strict requirement.

> **Note**: Opening the course repository in VS Code allows you to set up the project within a container, thanks to the [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory in the repository. More details on this later.

> **Note**: Once you clone and open the directory in VS Code, it will suggest installing the Python support extension.

> **Note**: If VS Code suggests reopening the repository in a container, decline this request to use the locally installed version of Python.

### Using Jupyter in the Browser

You can also work on the project using the [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directly in your browser. Both classic Jupyter and [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offer a great development experience with features like auto-completion and code highlighting.

To start Jupyter locally, open your terminal, navigate to the course directory, and run:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

This will start a Jupyter instance, and the URL to access it will be displayed in the terminal.

Once you access the URL, you’ll see the course outline and can navigate to any `*.ipynb` file, such as `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a Container

Another option for setting up the project is using a [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). The `.devcontainer` folder in the course repository allows VS Code to set up the project in a container. Outside of Codespaces, this requires installing Docker, which can be more complex, so we recommend this option for those experienced with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by utilizing Codespace Secrets. Check out the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide for more information.

## Lessons and Technical Requirements

The course includes 6 concept lessons and 6 coding lessons.

For the coding lessons, we use the Azure OpenAI Service. You’ll need access to the Azure OpenAI service and an API key to run the code. You can apply for access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While waiting for your application to be processed, each coding lesson includes a `README.md` file where you can review the code and outputs.

## Using the Azure OpenAI Service for the First Time

If you’re new to the Azure OpenAI service, follow this guide to [create and deploy an Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Using the OpenAI API for the First Time

If you’re new to the OpenAI API, follow this guide to [create and use the Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Meet Other Learners

We’ve set up channels in our official [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for connecting with other learners. It’s a great way to network with entrepreneurs, developers, students, and others interested in advancing their skills in Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

The project team will also be available on this Discord server to assist learners.

## Contribute

This course is an open-source project. If you notice areas for improvement or issues, feel free to submit a [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) or report a [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

The project team will track all contributions. Contributing to open source is a fantastic way to advance your career in Generative AI.

Most contributions require you to agree to a Contributor License Agreement (CLA), which confirms that you have the rights to grant us permission to use your contribution. For more details, visit the [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

When you submit a pull request, a CLA-bot will automatically check if you need to provide a CLA and will label the PR accordingly. Follow the bot’s instructions. You only need to do this once across all repositories using our CLA.

This project adheres to the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more information, read the Code of Conduct FAQ or contact [Email opencode](opencode@microsoft.com) with any questions or comments.

## Let's Get Started
Now that you have finished the necessary steps to complete this course, let's begin with an [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.