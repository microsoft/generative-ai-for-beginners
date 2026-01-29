# Local Setup 🖥️

**Gamitin ang gabay na ito kung mas gusto mong patakbuhin ang lahat sa iyong sariling laptop.**  
Mayroon kang dalawang paraan: **(A) native Python + virtual-env** o **(B) VS Code Dev Container gamit ang Docker**.  
Pumili ng alin man ang mas madali—pareho silang magdadala sa parehong mga aralin.

## 1.  Mga Kinakailangan

| Tool               | Bersyon / Tala                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (kunin ito mula sa <https://python.org>)                                      |
| **Git**            | Pinakabago (kasama sa Xcode / Git para sa Windows / Linux package manager)           |
| **VS Code**        | Opsyonal ngunit inirerekomenda <https://code.visualstudio.com>                       |
| **Docker Desktop** | *Para lamang* sa Opsyon B. Libreng install: <https://docs.docker.com/desktop/>       |

> 💡 **Tip** – Suriin ang mga tool sa terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opsyon A – Native Python (pinakamabilis)

### Hakbang 1  I-clone ang repo na ito

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Hakbang 2 Gumawa at i-activate ang virtual environment

```bash
python -m venv .venv          # gumawa ng isa
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Dapat magsimula na ang prompt sa (.venv)—ibig sabihin ay nasa loob ka na ng env.

### Hakbang 3 I-install ang mga dependencies

```bash
pip install -r requirements.txt
```

Laktawan ang Seksyon 3 tungkol sa [API keys](../../../00-course-setup)

## 2. Opsyon B – VS Code Dev Container (Docker)

Inayos namin ang repository na ito at kurso gamit ang isang [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) na may Universal runtime na sumusuporta sa Python3, .NET, Node.js at Java development. Ang kaugnay na configuration ay nakasaad sa `devcontainer.json` file na matatagpuan sa `.devcontainer/` folder sa root ng repository na ito.

>**Bakit pipiliin ito?**
>Kaparehong environment sa Codespaces; walang dependency drift.

### Hakbang 0 I-install ang mga dagdag

Docker Desktop – tiyaking gumagana ang ```docker --version```.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Hakbang 1 Buksan ang repo sa VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

Makikita ng VS Code ang .devcontainer/ at lalabas ang prompt.

### Hakbang 2 Muling buksan sa container

I-click ang “Reopen in Container”. Iba-build ng Docker ang image (≈ 3 min sa unang pagkakataon).
Kapag lumabas na ang terminal prompt, nasa loob ka na ng container.

## 2.  Opsyon C – Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ng ilang mga package.  
Ang Conda mismo ay isang package manager, na nagpapadali sa pag-setup at paglipat-lipat sa iba't ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga package. Kapaki-pakinabang din ito para sa pag-install ng mga package na hindi available sa `pip`.

### Hakbang 0  I-install ang Miniconda

Sundin ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para i-setup ito.

```bash
conda --version
```

### Hakbang 1 Gumawa ng virtual environment

Gumawa ng bagong environment file (*environment.yml*). Kung sumusunod ka gamit ang Codespaces, gawin ito sa loob ng `.devcontainer` directory, kaya `.devcontainer/environment.yml`.

### Hakbang 2  Punan ang iyong environment file

Idagdag ang sumusunod na snippet sa iyong `environment.yml`

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

### Hakbang 3 Gumawa ng Conda environment

Patakbuhin ang mga utos sa ibaba sa iyong command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Ang sub path ng .devcontainer ay nalalapat lamang sa mga setup ng Codespace
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung may mga problema.

## 2  Opsyon D – Classic Jupyter / Jupyter Lab (sa iyong browser)

> **Para kanino ito?**  
> Para sa sinumang gustong gamitin ang klasikong Jupyter interface o gustong magpatakbo ng mga notebook nang hindi gumagamit ng VS Code.  

### Hakbang 1  Siguraduhing naka-install ang Jupyter

Para simulan ang Jupyter nang lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at patakbuhin:

```bash
jupyter notebook
```

o kaya

```bash
jupyterhub
```

Magsisimula ito ng Jupyter instance at ipapakita ang URL para ma-access ito sa loob ng command line window.

Kapag na-access mo ang URL, makikita mo ang course outline at makakapag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Idagdag ang Iyong API Keys

Mahalaga ang panatilihing ligtas at secure ang iyong mga API key kapag gumagawa ng anumang uri ng aplikasyon. Inirerekomenda naming huwag itago ang mga API key nang direkta sa iyong code. Ang pag-commit ng mga detalye sa isang pampublikong repositoryo ay maaaring magdulot ng mga isyu sa seguridad at kahit hindi inaasahang gastos kung magagamit ito ng masamang loob.  
Narito ang step-by-step na gabay kung paano gumawa ng `.env` file para sa Python at idagdag ang `GITHUB_TOKEN`:

1. **Pumunta sa Iyong Project Directory**: Buksan ang iyong terminal o command prompt at pumunta sa root directory ng iyong proyekto kung saan mo gustong gumawa ng `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Gumawa ng `.env` File**: Gamitin ang iyong paboritong text editor para gumawa ng bagong file na pinangalanang `.env`. Kung gumagamit ka ng command line, maaari mong gamitin ang `touch` (sa mga Unix-based system) o `echo` (sa Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file sa isang text editor (hal., VS Code, Notepad++, o iba pang editor). Idagdag ang sumusunod na linya sa file, palitan ang `your_github_token_here` ng iyong aktwal na GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa nagagawa, kailangan mong i-install ang `python-dotenv` package para i-load ang mga environment variable mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa Iyong Python Script**: Sa iyong Python script, gamitin ang `python-dotenv` package para i-load ang mga environment variable mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # I-load ang mga environment variable mula sa .env na file
   load_dotenv()

   # I-access ang variable na GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Tapos na! Matagumpay mong nagawa ang `.env` file, naidagdag ang iyong GitHub token, at na-load ito sa iyong Python application.

🔐 Huwag kailanman i-commit ang .env—nasa .gitignore na ito.  
Ang buong mga tagubilin mula sa provider ay nasa [`providers.md`](03-providers.md).

## 4. Ano ang susunod?

| Gusto kong…          | Pumunta sa…                                                             |
|---------------------|-------------------------------------------------------------------------|
| Simulan ang Lesson 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Mag-setup ng LLM Provider | [`providers.md`](03-providers.md)                                   |
| Makilala ang ibang mga mag-aaral | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Pag-aayos ng Problema

| Sintomas                                   | Ayusin                                                             |
|-------------------------------------------|-------------------------------------------------------------------|
| `python not found`                        | Idagdag ang Python sa PATH o muling buksan ang terminal pagkatapos ng install            |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` pagkatapos subukan muli.        |
| `ModuleNotFoundError: dotenv`             | Patakbuhin ang `pip install -r requirements.txt` (hindi na-install ang env).   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → dagdagan ang disk size. |
| Patuloy na hinihikayat ng VS Code na muling buksan | Maaaring parehong aktibo ang Options; pumili ng isa (venv **o** container)|
| OpenAI 401 / 429 errors                   | Suriin ang halaga ng `OPENAI_API_KEY` / mga limitasyon sa request.             |
| Mga error sa paggamit ng Conda            | I-install ang Microsoft AI libraries gamit ang `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->