<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:29:28+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "tl"
}
-->
# Lokal na Setup 🖥️

**Gamitin ang gabay na ito kung mas gusto mong patakbuhin ang lahat sa sarili mong laptop.**  
Mayroon kang dalawang opsyon: **(A) native Python + virtual-env** o **(B) VS Code Dev Container gamit ang Docker**.  
Pumili ng alinman sa tingin mong mas madali—pareho lang ang magiging resulta ng mga aralin.

## 1.  Mga Kailangan Bago Magsimula

| Tool               | Bersyon / Tala                                                                      |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (kunin mula sa <https://python.org>)                                         |
| **Git**            | Pinakabago (kasama na sa Xcode / Git for Windows / Linux package manager)           |
| **VS Code**        | Opsyonal pero inirerekomenda <https://code.visualstudio.com>                        |
| **Docker Desktop** | *Para lang* sa Option B. Libreng install: <https://docs.docker.com/desktop/>        |

> 💡 **Tip** – I-verify ang mga tool sa terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (pinakamabilis)

### Step 1  I-clone ang repo na ito

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 Gumawa at i-activate ang virtual environment

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Dapat magsimula na ngayon ang prompt sa (.venv)—ibig sabihin nasa loob ka na ng environment.

### Step 3 I-install ang mga kinakailangang package

```bash
pip install -r requirements.txt
```

Lumaktaw na sa Seksyon 3 tungkol sa [API keys](../../../00-course-setup)

## 2. Option B – VS Code Dev Container (Docker)

Inihanda namin ang repository at kursong ito gamit ang isang [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) na may Universal runtime na sumusuporta sa Python3, .NET, Node.js at Java development. Ang kaugnay na configuration ay nasa `devcontainer.json` file na matatagpuan sa `.devcontainer/` folder sa root ng repository na ito.

>**Bakit ito ang pipiliin?**
>Parehong-pareho ang environment sa Codespaces; walang problema sa dependencies.

### Step 0 I-install ang mga dagdag na kailangan

Docker Desktop – tiyaking gumagana ang ```docker --version```.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Step 1 Buksan ang repo sa VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

Awtomatikong madedetect ng VS Code ang .devcontainer/ at magpapakita ng prompt.

### Step 2 Buksan muli sa container

I-click ang “Reopen in Container”. Gagawa ng Docker ng image (≈ 3 minuto sa unang beses).
Kapag lumitaw na ang terminal prompt, nasa loob ka na ng container.

## 2.  Option C – Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, at ilang packages.
Ang Conda mismo ay isang package manager na nagpapadali sa pag-setup at paglipat-lipat sa iba’t ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at packages. Magagamit din ito para mag-install ng mga package na wala sa `pip`.

### Step 0  I-install ang Miniconda

Sundin ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para ma-setup ito.

```bash
conda --version
```

### Step 1 Gumawa ng virtual environment

Gumawa ng bagong environment file (*environment.yml*). Kung sumusunod ka gamit ang Codespaces, gawin ito sa loob ng `.devcontainer` directory, kaya `.devcontainer/environment.yml`.

### Step 2  Lagyan ng laman ang environment file mo

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

### Step 3 Gumawa ng Conda environment

Patakbuhin ang mga command sa ibaba sa iyong command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung may naging problema.

## 2  Option D – Classic Jupyter / Jupyter Lab (sa browser mo)

> **Para kanino ito?**  
> Para sa mga mas gusto ang classic na Jupyter interface o gustong magpatakbo ng notebooks nang hindi gumagamit ng VS Code.  

### Step 1  Tiyaking naka-install ang Jupyter

Para magsimula ng Jupyter sa lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at patakbuhin:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Magsisimula ito ng Jupyter instance at ipapakita ang URL na gagamitin sa command line window.

Pag na-access mo na ang URL, makikita mo ang course outline at makakapunta ka sa kahit anong `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Idagdag ang Iyong API Keys

Mahalagang panatilihing ligtas at secure ang iyong mga API key kapag gumagawa ng kahit anong application. Huwag ilalagay ang mga API key direkta sa code mo. Kung ma-commit mo ito sa public repository, puwedeng magdulot ito ng security issues at hindi inaasahang gastos kung magamit ng iba.
Narito ang step-by-step na gabay kung paano gumawa ng `.env` file para sa Python at idagdag ang `GITHUB_TOKEN`:

1. **Pumunta sa Project Directory Mo**: Buksan ang terminal o command prompt at mag-navigate sa root directory ng project mo kung saan mo gustong gawin ang `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Gumawa ng `.env` File**: Gamitin ang paborito mong text editor para gumawa ng bagong file na pinangalanang `.env`. Kung command line ang gamit mo, puwede mong gamitin ang `touch` (sa Unix-based systems) o `echo` (sa Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file sa text editor (hal. VS Code, Notepad++, o iba pa). Idagdag ang linyang ito sa file, palitan ang `your_github_token_here` ng aktwal mong GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa nagagawa, kailangan mong i-install ang `python-dotenv` package para ma-load ang environment variables mula sa `.env` file papunta sa Python application mo. I-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa Python Script Mo**: Sa Python script mo, gamitin ang `python-dotenv` package para i-load ang environment variables mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ayan! Matagumpay kang nakagawa ng `.env` file, nadagdag ang GitHub token mo, at na-load ito sa Python application mo.

🔐 Huwag kailanman i-commit ang .env—nasa .gitignore na ito.
Kumpletong tagubilin para sa mga provider ay nasa [`providers.md`](03-providers.md).

## 4. Ano ang susunod?

| Gusto kong…         | Pumunta sa…                                                                 |
|---------------------|------------------------------------------------------------------------------|
| Simulan ang Lesson 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)          |
| Mag-setup ng LLM Provider | [`providers.md`](03-providers.md)                                      |
| Makipagkilala sa ibang learners | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Troubleshooting

| Sintomas                                   | Solusyon                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| `python not found`                         | Idagdag ang Python sa PATH o i-reopen ang terminal pagkatapos mag-install |
| `pip` cannot build wheels (Windows)        | `pip install --upgrade pip setuptools wheel` tapos subukan ulit.|
| `ModuleNotFoundError: dotenv`              | Patakbuhin ang `pip install -r requirements.txt` (hindi pa na-install ang env).|
| Docker build fails *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → dagdagan ang disk size.|
| VS Code keeps prompting to reopen          | Maaaring parehong active ang Options; pumili ng isa (venv **o** container)|
| OpenAI 401 / 429 errors                    | Suriin ang `OPENAI_API_KEY` value / request rate limits.        |
| Errors using Conda                         | I-install ang Microsoft AI libraries gamit ang `conda install -c microsoft azure-ai-ml`|

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.