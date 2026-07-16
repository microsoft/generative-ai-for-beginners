# Lokal na Setup 🖥️

**Gamitin ang gabay na ito kung nais mong patakbuhin ang lahat sa sariling laptop mo.**  
Mayroon kang dalawang paraan: **(A) native Python + virtual-env** o **(B) VS Code Dev Container gamit ang Docker**.  
Piliin ang sa tingin mo ay mas madali—pareho ang patutunguhan ng mga ito sa mga aralin.

## 1.  Mga Kinakailangan

| Kasangkapan         | Bersyon / Tala                                                                       |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (kunin mula sa <https://python.org>)                                          |
| **Git**            | Pinakabago (kasama sa Xcode / Git para sa Windows / Linux package manager)            |
| **VS Code**        | Opsyonal pero inirerekomenda <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Para lamang sa Option B.* Libreng install: <https://docs.docker.com/desktop/>       |

> 💡 **Tip** – Suriin ang mga kasangkapan sa terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (pinakamabilis)

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

✅ Dapat magsimula ang prompt ngayon sa (.venv)—iyon ay nasa loob ka na ng env.

### Hakbang 3 Mag-install ng dependencies

```bash
pip install -r requirements.txt
```

Tumungo sa Seksyon 3 para sa [API keys](#3-idagdag-ang-iyong-mga-api-key)

## 2. Option B – VS Code Dev Container (Docker)

Inayos namin ang repository na ito at kurso gamit ang isang [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) na may Universal runtime na sumusuporta sa Python3, .NET, Node.js at Java development. Ang kaukulang configuration ay nasa `devcontainer.json` file na matatagpuan sa `.devcontainer/` folder sa root ng repository na ito.

>**Bakit ito ang piliin?**
>Kaparehong environment ng Codespaces; walang dependency drift.

### Hakbang 0 I-install ang mga dagdag na kailangan

Docker Desktop – tiyaking gumagana ang ```docker --version```.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Hakbang 1 Buksan ang repo sa VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

Awtomatikong madedetect ng VS Code ang .devcontainer/ at magpapakita ng prompt.

### Hakbang 2 I-reopen sa container

I-click ang “Reopen in Container”. Ito ay magtatayo ng Docker image (≈ 3 min sa unang pagkakataon).
Kapag lumabas ang terminal prompt, nasa loob ka na ng container.

## 2.  Option C – Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, at ilang mga packages.
Ang Conda mismo ay isang package manager, na nagpapadali sa pag-setup at pagpapalit-palit ng mga Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga packages. Kapaki-pakinabang din ito sa pag-install ng mga packages na hindi available sa pamamagitan ng `pip`.

### Hakbang 0  I-install ang Miniconda

Sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para ma-setup ito.

```bash
conda --version
```

### Hakbang 1 Gumawa ng virtual environment

Gumawa ng bagong environment file (*environment.yml*). Kung sumusunod ka gamit ang Codespaces, gawin ito sa loob ng `.devcontainer` directory, o kaya `.devcontainer/environment.yml`.

### Hakbang 2  Lagyan ng laman ang environment file mo

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

### Hakbang 3 Gumawa ng Conda environment mo

Patakbuhin ang mga sumusunod na command sa command line/terminal mo

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Ang sub path ng .devcontainer ay naaangkop lamang sa mga setup ng Codespace
conda activate ai4beg
```

Tumingin sa [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung may problema ka.

## 2  Option D – Classic Jupyter / Jupyter Lab (sa browser mo)

> **Para kanino ito?**  
> Para sa mga gustong gamitin ang klasikong Jupyter interface o gustong magpatakbo ng notebooks nang hindi gumagamit ng VS Code.  

### Hakbang 1  Siguraduhing naka-install ang Jupyter

Para simulan ang Jupyter lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at i-execute ang:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Magsisimula ito ng Jupyter instance at ipapakita ang URL para ma-access ito sa loob ng command line window.

Kapag na-access mo na ang URL, makikita mo ang outline ng kurso at maaari kang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Idagdag ang Iyong Mga API Key

Mahalaga ang pag-ingat sa kaligtasan ng iyong mga API key kapag gumagawa ng anumang uri ng aplikasyon. Inirerekomenda naming huwag iimbak nang direkta ang mga API key sa iyong code. Ang pag-commit ng mga detalye sa pampublikong repository ay maaaring magdulot ng mga isyu sa seguridad at kahit hindi inaasahang gastos kapag ginamit ng mga masasamang-loob.
Narito ang hakbang-hakbang na gabay kung paano gumawa ng `.env` file para sa Python at idagdag ang iyong Microsoft Foundry Models credentials:

> **Tandaan:** Ang GitHub Models (at ang `GITHUB_TOKEN` variable nito) ay magre-retire sa katapusan ng Hulyo 2026. Ang gabay na ito ay gumagamit ng [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) bilang kapalit. Mas gusto mo bang gumawa nang ganap sa offline? Tingnan ang [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Pumunta sa Project Directory Mo**: Buksan ang terminal o command prompt at mag-navigate sa root directory ng iyong proyekto kung saan mo gustong gumawa ng `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Gumawa ng `.env` File**: Gamitin ang paborito mong text editor para gumawa ng bagong file na may pangalang `.env`. Kung nasa command line ka, maaari mong gamitin ang `touch` (sa mga Unix-based system) o `echo` (sa Windows):

   Sa mga Unix-based system:

   ```bash
   touch .env
   ```

   Sa Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file sa isang text editor (hal., VS Code, Notepad++, o anumang iba pang editor). Idagdag ang mga sumusunod na linya sa file, palitan ang mga placeholder ng iyong tunay na Microsoft Foundry project endpoint at API key:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa ito na-install, kailangan mong i-install ang `python-dotenv` package para ma-load ang mga environment variable mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Mga Environment Variables sa Iyong Python Script**: Sa iyong Python script, gamitin ang `python-dotenv` package para i-load ang environment variables mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # I-load ang mga environment variables mula sa .env file
   load_dotenv()

   # I-access ang mga variable ng Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ayun na! Matagumpay mong nagawa ang `.env` file, naidagdag ang iyong Microsoft Foundry Models credentials, at naiload mo na ito sa iyong Python application.

🔐 Huwag kailanman i-commit ang .env—nasa .gitignore na ito.
Buong tagubilin mula sa provider ay makikita sa [`providers.md`](03-providers.md).

## 4. Ano ang susunod?

| Gusto kong…          | Pumunta sa…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Simulan ang Lesson 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Mag-setup ng LLM Provider | [`providers.md`](03-providers.md)                                   |
| Makilala ang ibang mga nag-aaral | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Pag-ayos ng Problema

| Sintomas                                   | Ayusin                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Idagdag ang Python sa PATH o muling buksan ang terminal pagkatapos ng install |
| `pip` hindi makapag-build wheels (Windows) | Patakbuhin ang `pip install --upgrade pip setuptools wheel` tapos ulitin. |
| `ModuleNotFoundError: dotenv`             | Patakbuhin ang `pip install -r requirements.txt` (hindi na-install ang env). |
| Docker build nabibigo *No space left*     | Docker Desktop ▸ *Settings* ▸ *Resources* → dagdagan ang laki ng disk. |
| Patuloy na hinihikayat ng VS Code na mag-reopen | Maaaring parehong aktibo ang mga Options; pumili ng isa (venv **o** container)|
| OpenAI 401 / 429 errors                   | Suriin ang halaga ng `OPENAI_API_KEY` / request rate limits.             |
| Mga error gamit ang Conda                  | I-install ang Microsoft AI libraries gamit ang `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->