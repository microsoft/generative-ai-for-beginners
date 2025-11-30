<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T01:10:20+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tl"
}
-->
# Pagsisimula sa kursong ito

Kami ay lubos na nasasabik na simulan mo ang kursong ito at makita kung ano ang maipapagawa mo gamit ang Generative AI!

Upang matiyak ang iyong tagumpay, inilalahad ng pahinang ito ang mga hakbang sa pag-setup, mga teknikal na kinakailangan, at kung saan makakakuha ng tulong kung kinakailangan.

## Mga Hakbang sa Pag-setup

Upang simulan ang kursong ito, kailangan mong kumpletuhin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo na ito](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sa iyong sariling GitHub account upang mabago ang anumang code at makumpleto ang mga hamon. Maaari mo ring [i-star (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) upang mas madali itong mahanap pati na rin ang mga kaugnay na repo.

### 2. Gumawa ng Codespace

Upang maiwasan ang anumang dependency issues kapag pinapatakbo ang code, inirerekomenda naming patakbuhin ang kursong ito sa [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Sa iyong fork: **Code -> Codespaces -> New on main**

![Dialog na nagpapakita ng mga button para gumawa ng codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Magdagdag ng secret

1. ⚙️ Icon ng Gear -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Pangalanan bilang OPENAI_API_KEY, i-paste ang iyong key, I-save.

### 3. Ano ang susunod?

| Gusto kong…         | Pumunta sa…                                                             |
|---------------------|-------------------------------------------------------------------------|
| Simulan ang Lesson 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Magtrabaho offline  | [`setup-local.md`](02-setup-local.md)                                   |
| Mag-setup ng LLM Provider | [`providers.md`](03-providers.md)                                        |
| Makipagkita sa ibang mga mag-aaral | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pag-aayos ng Problema

| Sintomas                                  | Solusyon                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build stuck > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Hindi naka-attach ang terminal; i-click ang **+** ➜ *bash*      |
| `401 Unauthorized` mula sa OpenAI         | Mali / expired `OPENAI_API_KEY`                                 |
| Ipinapakita ng VS Code ang “Dev container mounting…” | I-refresh ang tab ng browser—minsan nawawala ang koneksyon ng Codespaces |
| Nawawala ang Notebook kernel              | Menu ng Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Mga sistemang Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang File na `.env`**: Buksan ang file na `.env` sa isang text editor (hal., VS Code, Notepad++, o anumang iba pang editor). Idagdag ang sumusunod na linya sa file, palitan ang `your_github_token_here` ng iyong aktwal na GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa ito na-install, kakailanganin mong i-install ang package na `python-dotenv` upang ma-load ang mga environment variable mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa Iyong Python Script**: Sa iyong Python script, gamitin ang package na `python-dotenv` upang ma-load ang mga environment variable mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Tapos na! Matagumpay mong nagawa ang `.env` file, naidagdag ang iyong GitHub token, at na-load ito sa iyong Python application.

## Paano Patakbuhin Lokal sa Iyong Computer

Upang patakbuhin ang code lokal sa iyong computer, kailangan mong magkaroon ng ilang bersyon ng [Python na naka-install](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Upang magamit ang repository, kailangan mo itong i-clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag na-checkout mo na ang lahat, maaari ka nang magsimula!

## Mga Opsyonal na Hakbang

### Pag-install ng Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ang ilang mga package. Ang Conda mismo ay isang package manager na nagpapadali sa pag-setup at paglipat sa pagitan ng iba't ibang [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ng Python at mga package. Kapaki-pakinabang din ito para sa pag-install ng mga package na hindi available sa `pip`.

Maaari mong sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) upang mai-setup ito.

Kapag na-install na ang Miniconda, kailangan mong i-clone ang [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kung hindi mo pa nagagawa).

Susunod, kailangan mong gumawa ng virtual environment. Upang gawin ito gamit ang Conda, gumawa ng bagong environment file (_environment.yml_). Kung sumusunod ka gamit ang Codespaces, gawin ito sa loob ng `.devcontainer` directory, kaya `.devcontainer/environment.yml`.

Punan ang iyong environment file gamit ang snippet sa ibaba:

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

Kung makakaranas ka ng mga error gamit ang conda, maaari mong manu-manong i-install ang Microsoft AI Libraries gamit ang sumusunod na command sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Ang environment file ay naglalaman ng mga kinakailangang dependencies. Ang `<environment-name>` ay tumutukoy sa pangalan na nais mong gamitin para sa iyong Conda environment, at ang `<python-version>` ay ang bersyon ng Python na nais mong gamitin, halimbawa, `3` ang pinakabagong major version ng Python.

Kapag tapos na, maaari mong gawin ang iyong Conda environment sa pamamagitan ng pagpatakbo ng mga command sa ibaba sa iyong command line/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung makakaranas ka ng anumang isyu.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekomenda naming gamitin ang [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may naka-install na [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) para sa kursong ito. Gayunpaman, ito ay isang rekomendasyon lamang at hindi isang tiyak na kinakailangan.

> **Tandaan**: Sa pamamagitan ng pagbukas ng repository ng kurso sa VS Code, mayroon kang opsyon na i-setup ang proyekto sa loob ng isang container. Ito ay dahil sa [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory na matatagpuan sa loob ng repository ng kurso. Higit pa tungkol dito sa susunod.

> **Tandaan**: Kapag na-clone mo at binuksan ang direktoryo sa VS Code, awtomatiko nitong imumungkahi na i-install ang isang Python support extension.

> **Tandaan**: Kung imumungkahi ng VS Code na muling buksan ang repository sa isang container, tanggihan ang kahilingang ito upang magamit ang lokal na naka-install na bersyon ng Python.

### Paggamit ng Jupyter sa Browser

Maaari mo ring gamitin ang proyekto gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkta sa iyong browser. Ang parehong classic Jupyter at [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng kaaya-ayang development environment na may mga tampok tulad ng auto-completion, code highlighting, at iba pa.

Upang simulan ang Jupyter lokal, pumunta sa terminal/command line, mag-navigate sa direktoryo ng kurso, at i-execute:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Ito ay magsisimula ng Jupyter instance at ang URL upang ma-access ito ay ipapakita sa loob ng command line window.

Kapag na-access mo ang URL, makikita mo ang outline ng kurso at magagawang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

### Pagpapatakbo sa isang container

Isang alternatibo sa pag-setup ng lahat sa iyong computer o Codespace ay ang paggamit ng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ang espesyal na `.devcontainer` folder sa loob ng repository ng kurso ay nagbibigay-daan sa VS Code na i-setup ang proyekto sa loob ng isang container. Sa labas ng Codespaces, kakailanganin ang pag-install ng Docker, at medyo mas kumplikado ito, kaya inirerekomenda namin ito lamang sa mga may karanasan sa paggamit ng containers.

Isa sa mga pinakamahusay na paraan upang mapanatiling ligtas ang iyong mga API keys kapag gumagamit ng GitHub Codespaces ay sa pamamagitan ng paggamit ng Codespace Secrets. Mangyaring sundan ang [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide upang matuto pa tungkol dito.

## Mga Aralin at Teknikal na Kinakailangan

Ang kurso ay may 6 na concept lessons at 6 na coding lessons.

Para sa mga coding lessons, ginagamit namin ang Azure OpenAI Service. Kakailanganin mo ng access sa Azure OpenAI service at isang API key upang patakbuhin ang code na ito. Maaari kang mag-apply upang makakuha ng access sa pamamagitan ng [pagkumpleto ng application na ito](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Habang naghihintay ka na maiproseso ang iyong application, ang bawat coding lesson ay may kasamang `README.md` file kung saan maaari mong tingnan ang code at mga output.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung ito ang iyong unang beses na gagamit ng Azure OpenAI service, mangyaring sundan ang gabay kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung ito ang iyong unang beses na gagamit ng OpenAI API, mangyaring sundan ang gabay kung paano [gumawa at gamitin ang Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makipagkita sa Ibang mga Mag-aaral

Gumawa kami ng mga channel sa aming opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para makipagkita sa ibang mga mag-aaral. Ito ay isang mahusay na paraan upang makipag-network sa iba pang mga negosyante, tagabuo, mag-aaral, at sinumang nais mag-level up sa Generative AI.

[![Sumali sa discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ang project team ay naroon din sa Discord server na ito upang tumulong sa mga mag-aaral.

## Mag-ambag

Ang kursong ito ay isang open-source na inisyatibo. Kung may nakikita kang mga lugar na maaaring mapabuti o mga isyu, mangyaring gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng isang [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Ang project team ay susubaybayan ang lahat ng kontribusyon. Ang pag-aambag sa open source ay isang kamangha-manghang paraan upang buuin ang iyong karera sa Generative AI.

Karamihan sa mga kontribusyon ay nangangailangan sa iyo na sumang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na mayroon kang karapatang at aktwal na ibigay sa amin ang mga karapatan upang gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalaga: kapag nagsasalin ng teksto sa repo na ito, tiyakin na hindi ka gagamit ng machine translation. Ibe-verify namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring mag-volunteer lamang para sa mga pagsasalin sa mga wika kung saan ikaw ay bihasa.

Kapag nagsumite ka ng pull request, awtomatikong matutukoy ng CLA-bot kung kailangan mong magbigay ng CLA at lalagyan ng label ang PR nang naaayon (hal., label, komento). Sundin lamang ang mga tagubilin na ibinigay ng bot. Kailangan mo lamang gawin ito nang isang beses sa lahat ng repositories na gumagamit ng aming CLA.

Ang proyektong ito ay nagpatibay sa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon basahin ang Code of Conduct FAQ o makipag-ugnayan sa [Email opencode](opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Simulan na Natin
Ngayon na natapos mo na ang mga kinakailangang hakbang para makumpleto ang kursong ito, magsimula tayo sa pamamagitan ng pagkuha ng [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na awtoritatibong pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.