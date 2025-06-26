<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:45:28+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pa"
}
-->
# ਇਸ ਕੋਰਸ ਨਾਲ ਸ਼ੁਰੂਆਤ

ਅਸੀਂ ਤੁਹਾਨੂੰ ਇਸ ਕੋਰਸ ਦੀ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ ਬਹੁਤ ਉਤਸ਼ਾਹਿਤ ਹਾਂ ਅਤੇ ਵੇਖਣ ਲਈ ਉਤਸੁਕ ਹਾਂ ਕਿ ਤੁਸੀਂ Generative AI ਨਾਲ ਕੀ ਬਣਾਉਣ ਲਈ ਪ੍ਰੇਰਿਤ ਹੁੰਦੇ ਹੋ!

ਤੁਹਾਡੀ ਸਫਲਤਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ, ਇਹ ਪੰਨਾ ਸੈਟਅਪ ਕਦਮਾਂ, ਤਕਨੀਕੀ ਜ਼ਰੂਰਤਾਂ, ਅਤੇ ਜਿੱਥੇ ਮਦਦ ਮਿਲ ਸਕਦੀ ਹੈ, ਉਹ ਦਰਸਾਉਂਦਾ ਹੈ।

## ਸੈਟਅਪ ਕਦਮ

ਇਸ ਕੋਰਸ ਨੂੰ ਲੈਣ ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੇ ਕਦਮ ਪੂਰੇ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।

### 1. ਇਸ ਰਿਪੋ ਨੂੰ ਫੋਰਕ ਕਰੋ

ਆਪਣੇ GitHub ਖਾਤੇ ਵਿੱਚ ਕੋਈ ਵੀ ਕੋਡ ਬਦਲਣ ਅਤੇ ਚੁਣੌਤੀਆਂ ਪੂਰੀਆਂ ਕਰਨ ਲਈ [ਇਸ ਪੂਰੀ ਰਿਪੋ ਨੂੰ ਫੋਰਕ ਕਰੋ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)। ਤੁਸੀਂ ਇਸ ਨੂੰ ਅਤੇ ਸੰਬੰਧਿਤ ਰਿਪੋ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਲੱਭਣ ਲਈ [ਇਸ ਰਿਪੋ ਨੂੰ ਸਟਾਰ (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ਵੀ ਕਰ ਸਕਦੇ ਹੋ।

### 2. ਇੱਕ ਕੋਡਸਪੇਸ ਬਣਾਓ

ਕੋਡ ਚਲਾਉਣ ਸਮੇਂ ਕਿਸੇ ਵੀ ਨਿਰਭਰਤਾ ਸਮੱਸਿਆਵਾਂ ਤੋਂ ਬਚਣ ਲਈ, ਅਸੀਂ ਇਸ ਕੋਰਸ ਨੂੰ ਇੱਕ [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਚਲਾਉਣ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

ਇਹ ਤੁਹਾਡੇ ਫੋਰਕ ਕੀਤੇ ਗਏ ਰਿਪੋ ਦੇ `Code` ਵਿਕਲਪ ਨੂੰ ਚੁਣ ਕੇ ਅਤੇ **Codespaces** ਵਿਕਲਪ ਚੁਣ ਕੇ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

![ਕੋਡਸਪੇਸ ਬਣਾਉਣ ਲਈ ਬਟਨਾਂ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲਾ ਡਾਇਲਾਗ](../../../00-course-setup/images/who-will-pay.webp)

### 3. ਆਪਣੇ API ਕੁੰਜੀਆਂ ਸਟੋਰ ਕਰਨਾ

ਕਿਸੇ ਵੀ ਕਿਸਮ ਦੇ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਂਦੇ ਸਮੇਂ ਆਪਣੀਆਂ API ਕੁੰਜੀਆਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਅਤੇ ਸੁਰੱਖਿਅਤ ਰੱਖਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਕੋਈ ਵੀ API ਕੁੰਜੀਆਂ ਸਿੱਧੇ ਆਪਣੇ ਕੋਡ ਵਿੱਚ ਸਟੋਰ ਨਾ ਕਰੋ। ਜੇਕਰ ਕਿਸੇ ਬੁਰੇ ਕਾਰਕਰਤਾ ਦੁਆਰਾ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਇਹ ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਅਣਚਾਹੇ ਖਰਚਿਆਂ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦੀ ਹੈ।
ਇਹ ਰਿਹਾ Python ਲਈ `.env` ਫਾਈਲ ਬਣਾਉਣ ਅਤੇ `GITHUB_TOKEN` ਸ਼ਾਮਲ ਕਰਨ ਦਾ ਕਦਮ ਦਰ ਕਦਮ ਮਾਰਗਦਰਸ਼ਨ:

1. **ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ**: ਆਪਣਾ ਟਰਮੀਨਲ ਜਾਂ ਕਮਾਂਡ ਪ੍ਰੰਪਟ ਖੋਲ੍ਹੋ ਅਤੇ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ ਜਿੱਥੇ ਤੁਸੀਂ `.env` ਫਾਈਲ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ਫਾਈਲ ਬਣਾਓ**: ਆਪਣੇ ਮਨਪਸੰਦ ਟੈਕਸਟ ਐਡੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ `.env` ਨਾਮਕ ਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਓ। ਜੇਕਰ ਤੁਸੀਂ ਕਮਾਂਡ ਲਾਈਨ ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ `touch` (on Unix-based systems) or `echo` (Windows 'ਤੇ) ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ:

   ਯੂਨਿਕਸ-ਅਧਾਰਿਤ ਪ੍ਰਣਾਲੀਆਂ:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **`.env` ਫਾਈਲ ਸੰਪਾਦਿਤ ਕਰੋ**: `.env` ਫਾਈਲ ਨੂੰ ਇੱਕ ਟੈਕਸਟ ਐਡੀਟਰ (ਜਿਵੇਂ ਕਿ VS Code, Notepad++, ਜਾਂ ਕੋਈ ਹੋਰ ਐਡੀਟਰ) ਵਿੱਚ ਖੋਲ੍ਹੋ। ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਲਾਈਨ ਸ਼ਾਮਲ ਕਰੋ, `your_github_token_here` ਨੂੰ ਆਪਣੇ ਅਸਲ GitHub ਟੋਕਨ ਨਾਲ ਬਦਲੋ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ਫਾਈਲ ਸੇਵ ਕਰੋ**: ਬਦਲਾਅ ਨੂੰ ਸੇਵ ਕਰੋ ਅਤੇ ਟੈਕਸਟ ਐਡੀਟਰ ਨੂੰ ਬੰਦ ਕਰੋ।

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` ਪੈਕੇਜ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ ਤਾਂ ਜੋ `.env` ਫਾਈਲ ਤੋਂ ਆਪਣੇ Python ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਲੋਡ ਕੀਤੇ ਜਾ ਸਕਣ। ਤੁਸੀਂ ਇਸ ਨੂੰ `pip` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:

   ```bash
   pip install python-dotenv
   ```

6. **ਆਪਣੇ Python ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਲੋਡ ਕਰੋ**: ਆਪਣੇ Python ਸਕ੍ਰਿਪਟ ਵਿੱਚ, `.env` ਫਾਈਲ ਤੋਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਲੋਡ ਕਰਨ ਲਈ `python-dotenv` ਪੈਕੇਜ ਦੀ ਵਰਤੋਂ ਕਰੋ:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ਇਹ ਹੋ ਗਿਆ! ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਵਕ ਇੱਕ `.env` ਫਾਈਲ ਬਣਾਈ ਹੈ, ਆਪਣਾ GitHub ਟੋਕਨ ਸ਼ਾਮਲ ਕੀਤਾ ਹੈ, ਅਤੇ ਇਸ ਨੂੰ ਆਪਣੇ Python ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਲੋਡ ਕੀਤਾ ਹੈ।

## ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ

ਕੋਡ ਨੂੰ ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਚਲਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਕੁਝ ਸੰਸਕਰਣਾਂ ਦਾ [Python ਇੰਸਟਾਲ ਕੀਤਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

ਫਿਰ ਰਿਪੋਜਟਰੀ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਇਸਨੂੰ ਕਲੋਨ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਸਭ ਕੁਝ ਚੈੱਕ ਆਊਟ ਹੋਵੇ, ਤਾਂ ਤੁਸੀਂ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ!

## ਵਿਕਲਪਕ ਕਦਮ

### Miniconda ਇੰਸਟਾਲ ਕਰਨਾ

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ਇੱਕ ਹਲਕਾ ਇੰਸਟਾਲਰ ਹੈ ਜੋ [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ਅਤੇ ਕੁਝ ਪੈਕੇਜਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਹੈ। 
Conda ਖੁਦ ਇੱਕ ਪੈਕੇਜ ਮੈਨੇਜਰ ਹੈ, ਜੋ ਵੱਖ-ਵੱਖ Python [**ਵਰਚੁਅਲ ਵਾਤਾਵਰਣਾਂ**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ਅਤੇ ਪੈਕੇਜਾਂ ਦੇ ਵਿਚਕਾਰ ਸੈਟਅਪ ਅਤੇ ਸਵਿੱਚ ਕਰਨਾ ਆਸਾਨ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` ਰਾਹੀਂ ਉਪਲਬਧ ਨਾ ਹੋਣ ਵਾਲੇ ਪੈਕੇਜਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਵੀ ਸੁਵਿਧਾਜਨਕ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਆਪਣੇ ਵਾਤਾਵਰਣ ਫਾਈਲ ਨੂੰ ਭਰੋ:

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

ਜੇਕਰ ਤੁਹਾਨੂੰ conda ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀਆਂ ਆਉਂਦੀਆਂ ਹਨ, ਤਾਂ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟਰਮੀਨਲ ਵਿੱਚ Microsoft AI ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਮੈਨੂਅਲ ਤੌਰ 'ਤੇ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ।

```
conda install -c microsoft azure-ai-ml
```

ਵਾਤਾਵਰਣ ਫਾਈਲ ਉਹ ਨਿਰਭਰਤਾਵਾਂ ਦਰਸਾਉਂਦੀ ਹੈ ਜਿਨ੍ਹਾਂ ਦੀ ਸਾਨੂੰ ਲੋੜ ਹੈ। `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python ਦਾ ਨਵਾਂ ਪ੍ਰਮੁੱਖ ਸੰਸਕਰਣ ਹੈ।

ਇਸ ਨਾਲ, ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨੂੰ ਆਪਣੇ ਕਮਾਂਡ ਲਾਈਨ/ਟਰਮੀਨਲ ਵਿੱਚ ਚਲਾ ਕੇ ਆਪਣਾ Conda ਵਾਤਾਵਰਣ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਹੋ ਸਕਦੇ ਹੋ

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ਜੇਕਰ ਤੁਹਾਨੂੰ ਕਿਸੇ ਸਮੱਸਿਆ ਦਾ ਸਾਹਮਣਾ ਹੋਵੇ ਤਾਂ [Conda ਵਾਤਾਵਰਣ ਗਾਈਡ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ।

### Python ਸਹਾਇਕ ਵਿਸਥਾਰ ਨਾਲ Visual Studio Code ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਅਸੀਂ ਇਸ ਕੋਰਸ ਲਈ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ਐਡੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ Python ਸਹਾਇਕ ਵਿਸਥਾਰ ਇੰਸਟਾਲ ਕੀਤਾ ਹੋਇਆ ਹੈ। ਇਹ, ਹਾਲਾਂਕਿ, ਜ਼ਿਆਦਾਤਰ ਇੱਕ ਸਿਫਾਰਸ਼ ਹੈ ਅਤੇ ਕੋਈ ਨਿਸ਼ਚਿਤ ਲੋੜ ਨਹੀਂ ਹੈ

> **ਨੋਟ**: VS Code ਵਿੱਚ ਕੋਰਸ ਰਿਪੋਜਟਰੀ ਨੂੰ ਖੋਲ੍ਹ ਕੇ, ਤੁਹਾਡੇ ਕੋਲ ਇਸਨੂੰ ਇੱਕ ਕੰਟੇਨਰ ਵਿੱਚ ਸੈਟਅਪ ਕਰਨ ਦਾ ਵਿਕਲਪ ਹੁੰਦਾ ਹੈ। ਇਹ [ਖਾਸ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ਡਾਇਰੈਕਟਰੀ ਦੀ ਵਜ੍ਹਾ ਨਾਲ ਹੈ ਜੋ ਕੋਰਸ ਰਿਪੋਜਟਰੀ ਵਿੱਚ ਮਿਲਦੀ ਹੈ। ਇਸ ਬਾਰੇ ਹੋਰ ਬਾਅਦ ਵਿੱਚ।

> **ਨੋਟ**: ਜਦੋਂ ਤੁਸੀਂ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਕਲੋਨ ਅਤੇ ਖੋਲ੍ਹਦੇ ਹੋ, ਤਾਂ VS Code ਤੁਹਾਨੂੰ ਇੱਕ Python ਸਹਾਇਕ ਵਿਸਥਾਰ ਇੰਸਟਾਲ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕਰੇਗਾ।

> **ਨੋਟ**: ਜੇਕਰ VS Code ਤੁਹਾਨੂੰ ਰਿਪੋਜਟਰੀ ਨੂੰ ਇੱਕ ਕੰਟੇਨਰ ਵਿੱਚ ਦੁਬਾਰਾ ਖੋਲ੍ਹਣ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦਾ ਹੈ, ਤਾਂ ਇਸ ਬੇਨਤੀ ਨੂੰ ਅਸਵੀਕਾਰ ਕਰੋ ਤਾਂ ਜੋ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਇੰਸਟਾਲ ਕੀਤੇ ਗਏ Python ਸੰਸਕਰਣ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕੇ।

### ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ Jupyter ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਤੁਸੀਂ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਹੀ [Jupyter ਵਾਤਾਵਰਣ](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ 'ਤੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ। ਦੋਵੇਂ ਕਲਾਸਿਕ Jupyter ਅਤੇ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ਆਟੋ-ਕੰਪਲੀਸ਼ਨ, ਕੋਡ ਹਾਈਲਾਈਟਿੰਗ ਆਦਿ ਵਰਗੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ ਇੱਕ ਸੁਖਦਾਈ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

ਸਥਾਨਕ ਤੌਰ 'ਤੇ Jupyter ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਟਰਮੀਨਲ/ਕਮਾਂਡ ਲਾਈਨ ਵੱਲ ਜਾਓ, ਕੋਰਸ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ, ਅਤੇ ਇਹ ਚਲਾਓ:

```bash
jupyter notebook
```

ਜਾਂ

```bash
jupyterhub
```

ਇਸ ਨਾਲ ਇੱਕ Jupyter ਇੰਸਟੈਂਸ ਸ਼ੁਰੂ ਹੋਵੇਗਾ ਅਤੇ ਇਸਨੂੰ ਐਕਸੈਸ ਕਰਨ ਲਈ URL ਕਮਾਂਡ ਲਾਈਨ ਵਿੰਡੋ ਵਿੱਚ ਦਿਖਾਇਆ ਜਾਵੇਗਾ।

ਜਦੋਂ ਤੁਸੀਂ URL ਤੱਕ ਪਹੁੰਚ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਕੋਰਸ ਦਾ ਖਾਕਾ ਵੇਖਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਕਿਸੇ ਵੀ `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` ਫਾਈਲ ਵਿੱਚ ਜਾ ਸਕਦੇ ਹੋ ਜਿੱਥੇ ਤੁਸੀਂ ਕੋਡ ਅਤੇ ਨਤੀਜੇ ਵੇਖ ਸਕਦੇ ਹੋ।

## ਪਹਿਲੀ ਵਾਰ ਲਈ Azure OpenAI ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਜੇਕਰ ਤੁਸੀਂ ਪਹਿਲੀ ਵਾਰ Azure OpenAI ਸੇਵਾ ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI ਸੇਵਾ ਸਰੋਤ ਬਣਾਉਣ ਅਤੇ ਤਾਇਨਾਤ ਕਰਨ ਬਾਰੇ ਇਸ ਮਾਰਗਦਰਸ਼ਨ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ਨੂੰ ਪਾਲਣਾ ਕਰੋ।

## ਪਹਿਲੀ ਵਾਰ ਲਈ OpenAI API ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਜੇਕਰ ਤੁਸੀਂ ਪਹਿਲੀ ਵਾਰ OpenAI API ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ [ਇੰਟਰਫੇਸ ਬਣਾਉਣ ਅਤੇ ਵਰਤਣ ਬਾਰੇ ਮਾਰਗਦਰਸ਼ਨ](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲੋ

ਅਸੀਂ ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ ਲਈ ਆਪਣੇ ਸਰਕਾਰੀ [AI ਕਮਿਊਨਿਟੀ Discord ਸਰਵਰ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਚੈਨਲ ਬਣਾਏ ਹਨ। ਇਹ ਹੋਰ ਸਮਾਨ ਵਿਚਾਰਧਾਰਾ ਵਾਲੇ ਉੱਦਮੀ, ਬਿਲਡਰ, ਵਿਦਿਆਰਥੀ, ਅਤੇ ਕੋਈ ਵੀ ਜੋ Generative AI ਵਿੱਚ ਸਿਖਰ ਤੇ ਜਾਣ ਦੀ ਖੋਜ ਕਰ ਰਿਹਾ ਹੈ, ਨਾਲ ਨੈਟਵਰਕਿੰਗ ਕਰਨ ਦਾ ਇੱਕ ਸ਼ਾਨਦਾਰ ਤਰੀਕਾ ਹੈ।

[![Discord ਚੈਨਲ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ਪਰਿਯੋਜਨਾ ਦੀ ਟੀਮ ਵੀ ਕਿਸੇ ਵੀ ਸਿੱਖਣ ਵਾਲੇ ਦੀ ਮਦਦ ਕਰਨ ਲਈ ਇਸ Discord ਸਰਵਰ 'ਤੇ ਹੋਵੇਗੀ।

## ਯੋਗਦਾਨ

ਇਹ ਕੋਰਸ ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਪਹਲ ਹੈ। ਜੇਕਰ ਤੁਸੀਂ ਸੁਧਾਰ ਜਾਂ ਸਮੱਸਿਆ ਦੇ ਖੇਤਰ ਵੇਖਦੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ [ਪੁਲ ਰਿਕਵੈਸਟ ਬਣਾਓ](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ਜਾਂ ਇੱਕ [GitHub ਸਮੱਸਿਆ ਲਾਗ ਕਰੋ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)।

ਪਰਿਯੋਜਨਾ ਦੀ ਟੀਮ ਸਾਰੇ ਯੋਗਦਾਨਾਂ ਨੂੰ ਟ੍ਰੈਕ ਕਰੇਗੀ। ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਵਿੱਚ ਯੋਗਦਾਨ ਦੇਣਾ Generative AI ਵਿੱਚ ਆਪਣਾ ਕਰੀਅਰ ਬਣਾਉਣ ਦਾ ਇੱਕ ਸ਼ਾਨਦਾਰ ਤਰੀਕਾ ਹੈ।

ਜ਼ਿਆਦਾਤਰ ਯੋਗਦਾਨਾਂ ਲਈ ਤੁਹਾਨੂੰ ਇੱਕ Contributor License Agreement (CLA) ਨਾਲ ਸਹਿਮਤ ਹੋਣਾ ਲੋੜੀਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇਹ ਘੋਸ਼ਣਾ ਕੀਤੀ ਗਈ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਹੀ ਹੈ ਅਤੇ ਅਸਲ ਵਿੱਚ, ਸਾਨੂੰ ਤੁਹਾਡੇ ਯੋਗਦਾਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦਾ ਅਧਿਕਾਰ ਦਿੰਦਾ ਹੈ। ਵਿਸਥਾਰ ਲਈ, [CLA, Contributor License Agreement ਵੈਬਸਾਈਟ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ।

ਮਹੱਤਵਪੂਰਨ: ਇਸ ਰਿਪੋ ਵਿੱਚ ਪਾਠ ਦਾ ਅਨੁਵਾਦ ਕਰਦੇ ਸਮੇਂ, ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਮਸ਼ੀਨ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰਦੇ। ਅਸੀਂ ਕਮਿਊਨਿਟੀ ਦੁਆਰਾ ਅਨੁਵਾਦਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਾਂਗੇ, ਇਸ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਕੇਵਲ ਉਹਨਾਂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਲਈ ਸਵੈਛਿਕ ਬਣੋ ਜਿੱਥੇ ਤੁਸੀਂ ਨਿਪੁੰਨ ਹੋ।

ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਪੁਲ ਰਿਕਵੈਸਟ ਜਮ੍ਹਾਂ ਕਰਵਾਉਂਦੇ ਹੋ, ਇੱਕ CLA-ਬੋਟ ਆਪਣੇ ਆਪ ਇਹ ਨਿਰਧਾਰਿਤ ਕਰੇਗਾ ਕਿ ਤੁਹਾਨੂੰ CLA ਪ੍ਰਦਾਨ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਜਾਂ ਨਹੀਂ ਅਤੇ PR ਨੂੰ ਸਹੀ ਤੌਰ 'ਤੇ ਸਜਾਏਗਾ (ਜਿਵੇਂ ਕਿ ਲੇਬਲ, ਟਿੱਪਣੀ)। ਬੋਟ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ ਗਏ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਤੁਹਾਨੂੰ ਸਿਰਫ਼ ਇੱਕ ਵਾਰ ਸਾਡੇ CLA ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਸਾਰੇ ਰਿਪੋਜ਼ਟਰੀਆਂ ਵਿੱਚ ਇਹ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।

ਇਸ ਪ੍ਰੋਜੈਕਟ ਨੇ [Microsoft ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਆਚਰਣ ਸੰਹਿਤਾ](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਅਪਣਾਇਆ ਹੈ। ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਆਚਰਣ ਸੰਹਿਤਾ FAQ ਪੜ੍ਹੋ ਜਾਂ [Email opencode](opencode@microsoft.com) ਨਾਲ ਕਿਸੇ ਵੀ ਵਾਧੂ ਸਵਾਲਾਂ ਜਾਂ ਟਿੱਪਣੀਆਂ ਲਈ

**ਅਸਵੀਕਾਰਣੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣੀਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।