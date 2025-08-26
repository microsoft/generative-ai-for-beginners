<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:30:28+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tl"
}
-->
# Pagsisimula sa kursong ito

Excited kaming makita kang magsimula sa kursong ito at malaman kung ano ang mga ideya mong mabubuo gamit ang Generative AI!

Para matiyak ang iyong tagumpay, inilista sa pahinang ito ang mga hakbang sa setup, teknikal na mga kinakailangan, at kung saan ka pwedeng humingi ng tulong kung kinakailangan.

## Mga Hakbang sa Setup

Para makapagsimula sa kursong ito, kailangan mong tapusin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo na ito](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sa sarili mong GitHub account para magawa mong baguhin ang code at tapusin ang mga hamon. Pwede mo ring [i-star (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para mas madali mong mahanap ito at ang mga kaugnay na repo.

### 2. Gumawa ng codespace

Para maiwasan ang mga dependency issue sa pagpapatakbo ng code, inirerekomenda naming gamitin ang [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) para sa kursong ito.

Sa iyong fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Magdagdag ng secret

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Pangalanan na OPENAI_API_KEY, i-paste ang iyong key, i-Save.

### 3.  Ano ang susunod?

| Gusto kong…          | Pumunta sa…                                                                  |
|---------------------|-------------------------------------------------------------------------------|
| Simulan ang Lesson 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Magtrabaho offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Mag-setup ng LLM Provider | [`providers.md`](providers.md)                                          |
| Makipagkilala sa ibang learners | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pagsasaayos ng mga problema

| Sintomas                                   | Solusyon                                                             |
|-------------------------------------------|---------------------------------------------------------------------|
| Container build stuck > 10 min            | **Codespaces ➜ “Rebuild Container”**                                |
| `python: command not found`               | Hindi naka-attach ang terminal; i-click ang **+** ➜ *bash*          |
| `401 Unauthorized` mula sa OpenAI         | Mali o expired na `OPENAI_API_KEY`                                  |
| VS Code shows “Dev container mounting…”   | I-refresh ang browser tab—minsan nawawala ang koneksyon ng Codespaces |
| Notebook kernel missing                   | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   Para sa Unix-based systems:

   ```bash
   touch .env
   ```

   Para sa Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file gamit ang text editor (hal. VS Code, Notepad++, o iba pa). Idagdag ang linyang ito sa file, palitan ang `your_github_token_here` ng iyong aktwal na GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa nagagawa, kailangan mong i-install ang `python-dotenv` package para ma-load ang environment variables mula sa `.env` file papunta sa iyong Python application. Pwede mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa iyong Python Script**: Sa iyong Python script, gamitin ang `python-dotenv` package para ma-load ang environment variables mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ayos! Nagawa mo nang gumawa ng `.env` file, idagdag ang iyong GitHub token, at i-load ito sa iyong Python application.

## Paano Patakbuhin sa Lokal na Computer

Para patakbuhin ang code sa iyong sariling computer, kailangan mong may naka-install na [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para magamit ang repository, kailangan mo itong i-clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag nakuha mo na ang lahat, pwede ka nang magsimula!

## Mga Opsyonal na Hakbang

### Pag-install ng Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay magaan na installer para sa [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, at ilang packages.
Ang Conda ay package manager na nagpapadali sa pag-setup at pag-switch sa iba’t ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at packages. Magagamit din ito para mag-install ng mga package na hindi available sa `pip`.

Sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para ma-setup ito.

Kapag naka-install na ang Miniconda, kailangan mong i-clone ang [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kung hindi mo pa nagagawa).

Susunod, kailangan mong gumawa ng virtual environment. Para magawa ito gamit ang Conda, gumawa ng bagong environment file (_environment.yml_). Kung sumusunod ka gamit ang Codespaces, gawin ito sa loob ng `.devcontainer` directory, kaya `.devcontainer/environment.yml`.

Ilagay ang snippet sa ibaba sa iyong environment file:

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

Kung makaranas ka ng error sa paggamit ng conda, pwede mong mano-manong i-install ang Microsoft AI Libraries gamit ang command na ito sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Ang environment file ay naglalaman ng mga dependencies na kailangan natin. Ang `<environment-name>` ay pangalan na gusto mong gamitin para sa iyong Conda environment, at ang `<python-version>` ay version ng Python na gusto mong gamitin, halimbawa, `3` para sa pinakabagong major version.

Kapag tapos na, pwede ka nang gumawa ng Conda environment sa pamamagitan ng pagtakbo ng mga command na ito sa iyong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Sundan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung may problema ka.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekomenda naming gamitin ang [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) para sa kursong ito. Pero ito ay rekomendasyon lamang at hindi kinakailangan.

> **Note**: Kapag binuksan mo ang course repository sa VS Code, may opsyon kang i-setup ang project sa loob ng container. Ito ay dahil sa [special na `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory na nasa course repository. Malalaman mo pa ito mamaya.

> **Note**: Kapag na-clone at nabuksan mo ang directory sa VS Code, awtomatikong mag-susuggest ito na mag-install ka ng Python support extension.

> **Note**: Kung mag-suggest ang VS Code na buksan ang repository sa container, tanggihan ito para magamit ang locally installed na Python.

### Paggamit ng Jupyter sa Browser

Pwede mo ring gawin ang project gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkta sa iyong browser. Parehong classic Jupyter at [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng magandang development environment na may features tulad ng auto-completion, code highlighting, at iba pa.

Para magsimula ng Jupyter sa lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at i-execute:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Magsisimula ito ng Jupyter instance at ipapakita ang URL para ma-access ito sa command line window.

Kapag na-access mo na ang URL, makikita mo ang course outline at pwede kang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

### Pagpapatakbo sa container

Isa pang paraan bukod sa pag-setup sa computer o Codespace ay ang paggamit ng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ang espesyal na `.devcontainer` folder sa course repository ay nagpapahintulot sa VS Code na i-setup ang project sa loob ng container. Kung hindi Codespaces, kailangan mong mag-install ng Docker, at medyo matrabaho ito, kaya inirerekomenda lang ito sa may karanasan sa containers.

Isa sa pinakamagandang paraan para mapanatiling ligtas ang iyong API keys kapag gumagamit ng GitHub Codespaces ay ang paggamit ng Codespace Secrets. Sundan ang [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide para matutunan pa ito.

## Mga Aralin at Teknikal na Kinakailangan

Ang kurso ay may 6 na concept lessons at 6 na coding lessons.

Para sa coding lessons, ginagamit natin ang Azure OpenAI Service. Kailangan mo ng access sa Azure OpenAI service at API key para mapatakbo ang code. Pwede kang mag-apply para sa access sa pamamagitan ng [pagkumpleto ng application na ito](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Habang hinihintay mo ang approval ng application mo, bawat coding lesson ay may `README.md` file kung saan pwede mong makita ang code at outputs.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung unang beses mong gagamitin ang Azure OpenAI service, sundan ang guide kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung unang beses mong gagamitin ang OpenAI API, sundan ang guide kung paano [gumawa at gumamit ng Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makipagkilala sa Ibang Learners

May mga channel kami sa opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para makipagkilala sa ibang learners. Magandang paraan ito para makipag-network sa mga kapwa entrepreneur, builder, estudyante, at sinumang gustong matuto pa tungkol sa Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ang project team ay nandito rin sa Discord server para tumulong sa mga learners.

## Mag-ambag

Ang kursong ito ay open-source initiative. Kung may nakikita kang pwedeng i-improve o may issue, gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Ang project team ay nagmo-monitor ng lahat ng ambag. Ang pag-aambag sa open source ay magandang paraan para palaguin ang iyong career sa Generative AI.

Karamihan sa mga ambag ay nangangailangan ng pagsang-ayon sa Contributor License Agreement (CLA) na nagsasabing may karapatan ka at binibigyan mo kami ng karapatang gamitin ang iyong ambag. Para sa detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalaga: kapag nagta-translate ng text sa repo na ito, siguraduhing hindi ka gagamit ng machine translation. Ibe-verify ng komunidad ang mga translation, kaya mag-volunteer lang kung proficient ka sa wika.

Kapag nag-submit ka ng pull request, awtomatikong malalaman ng CLA-bot kung kailangan mong magbigay ng CLA at lalagyan ng tamang label o comment ang PR. Sundan lang ang instructions ng bot. Isang beses mo lang ito kailangang gawin sa lahat ng repo na gumagamit ng CLA namin.

Ang project na ito ay sumusunod sa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon, basahin ang Code of Conduct FAQ o mag-email sa [Email opencode](opencode@microsoft.com) para sa mga tanong o komento.

## Tara, Simulan na!
Ngayon na natapos mo na ang mga kinakailangang hakbang para matapos ang kursong ito, magsimula tayo sa pamamagitan ng pagkuha ng [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.