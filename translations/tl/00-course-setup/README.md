<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:14:35+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tl"
}
-->
# Pagsisimula sa kursong ito

Lubos kaming nasasabik na simulan mo ang kursong ito at makita kung ano ang mahihikayat kang gawin gamit ang Generative AI!

Upang matiyak ang iyong tagumpay, inilalahad sa pahinang ito ang mga hakbang sa pagsasaayos, mga teknikal na kinakailangan, at kung saan ka maaaring humingi ng tulong kung kinakailangan.

## Mga Hakbang sa Pagsasaayos

Para makapagsimula sa kursong ito, kailangan mong tapusin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sa iyong sariling GitHub account upang magkaroon ka ng kakayahang baguhin ang anumang code at tapusin ang mga hamon. Maaari mo ring [i-star (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para mas madali mo itong mahanap pati na rin ang mga kaugnay na repo.

### 2. Gumawa ng codespace

Para maiwasan ang anumang problema sa dependency kapag pinapatakbo ang code, inirerekomenda naming patakbuhin ang kursong ito sa isang [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Magagawa ito sa pamamagitan ng pagpili sa opsyong `Code` sa iyong na-fork na bersyon ng repo na ito at pagpili sa opsyong **Codespaces**.

![Dialog na nagpapakita ng mga button para gumawa ng codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Pag-iimbak ng Iyong API Keys

Mahalaga ang panatilihing ligtas at protektado ang iyong mga API key kapag gumagawa ng anumang uri ng aplikasyon. Inirerekomenda naming huwag direktang itago ang mga API key sa iyong code. Ang pag-commit ng mga detalye na ito sa isang pampublikong repositoryo ay maaaring magdulot ng mga isyu sa seguridad at posibleng hindi inaasahang gastos kung magagamit ito ng mga masasamang loob.  
Narito ang isang hakbang-hakbang na gabay kung paano gumawa ng `.env` file para sa Python at idagdag ang `GITHUB_TOKEN`:

1. **Pumunta sa Direktoryo ng Iyong Proyekto**: Buksan ang iyong terminal o command prompt at pumunta sa root directory ng iyong proyekto kung saan mo gustong gumawa ng `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Gumawa ng `.env` File**: Gamitin ang iyong paboritong text editor para gumawa ng bagong file na pinangalanang `.env`. Kung gumagamit ka ng command line, maaari mong gamitin ang `touch` (sa mga Unix-based na sistema) o `echo` (sa Windows):

   Unix-based na sistema:

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

5. **I-install ang `python-dotenv`**: Kung hindi mo pa ito na-install, kailangan mong i-install ang package na `python-dotenv` para ma-load ang mga environment variable mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa Iyong Python Script**: Sa iyong Python script, gamitin ang package na `python-dotenv` para i-load ang mga environment variable mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ayan! Matagumpay mong nagawa ang `.env` file, naidagdag ang iyong GitHub token, at na-load ito sa iyong Python application.

## Paano Patakbuhin nang Lokal sa Iyong Kompyuter

Para patakbuhin ang code nang lokal sa iyong kompyuter, kailangan mong magkaroon ng naka-install na bersyon ng [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para magamit ang repositoryo, kailangan mo itong i-clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag naayos mo na ang lahat, maaari ka nang magsimula!

## Opsyonal na Mga Hakbang

### Pag-install ng Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ng ilang mga package.  
Ang Conda mismo ay isang package manager na nagpapadali sa pag-setup at paglipat-lipat sa iba't ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga package. Kapaki-pakinabang din ito sa pag-install ng mga package na hindi available sa pamamagitan ng `pip`.

Maaari mong sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para sa pag-setup.

Kapag naka-install na ang Miniconda, kailangan mong i-clone ang [repositoryo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kung hindi mo pa nagagawa).

Susunod, kailangan mong gumawa ng virtual environment. Para gawin ito gamit ang Conda, gumawa ng bagong environment file (_environment.yml_). Kung sumusunod ka gamit ang Codespaces, gawin ito sa loob ng `.devcontainer` directory, kaya `.devcontainer/environment.yml`.

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

Kung makaranas ka ng mga error gamit ang conda, maaari mong mano-manong i-install ang Microsoft AI Libraries gamit ang sumusunod na command sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Itinatakda ng environment file ang mga dependencies na kailangan natin. Ang `<environment-name>` ay tumutukoy sa pangalan na gusto mong gamitin para sa iyong Conda environment, at ang `<python-version>` ay ang bersyon ng Python na nais mong gamitin, halimbawa, ang `3` ay ang pinakabagong major na bersyon ng Python.

Kapag tapos na, maaari mo nang likhain ang iyong Conda environment sa pamamagitan ng pagpapatakbo ng mga sumusunod na command sa iyong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung sakaling magkaroon ka ng mga problema.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekomenda naming gamitin ang [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may naka-install na [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) para sa kursong ito. Ito ay isang rekomendasyon lamang at hindi isang mahigpit na kinakailangan.

> **Note**: Sa pagbubukas ng course repository sa VS Code, may opsyon kang i-setup ang proyekto sa loob ng isang container. Ito ay dahil sa [espesyal na `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) na direktoryo na matatagpuan sa loob ng course repository. Tatalakayin pa ito mamaya.

> **Note**: Kapag na-clone mo at binuksan ang direktoryo sa VS Code, awtomatiko nitong irerekomenda na i-install mo ang Python support extension.

> **Note**: Kung hihilingin ng VS Code na muling buksan ang repository sa isang container, tanggihan ang kahilingang ito upang magamit ang lokal na naka-install na bersyon ng Python.

### Paggamit ng Jupyter sa Browser

Maaari ka ring magtrabaho sa proyekto gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkta sa iyong browser. Parehong ang classic Jupyter at [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng maginhawang development environment na may mga tampok tulad ng auto-completion, code highlighting, atbp.

Para simulan ang Jupyter nang lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at patakbuhin ang:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Ito ay magsisimula ng isang Jupyter instance at ipapakita ang URL para ma-access ito sa loob ng command line window.

Kapag na-access mo ang URL, makikita mo ang outline ng kurso at maaari kang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

### Pagpapatakbo sa loob ng container

Isang alternatibo sa pag-setup ng lahat sa iyong kompyuter o Codespace ay ang paggamit ng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ang espesyal na `.devcontainer` folder sa loob ng course repository ay nagpapahintulot sa VS Code na i-setup ang proyekto sa loob ng isang container. Sa labas ng Codespaces, kakailanganin nito ang pag-install ng Docker, at medyo mas kumplikado ito, kaya inirerekomenda namin ito lamang sa mga may karanasan sa paggamit ng containers.

Isa sa mga pinakamabisang paraan para mapanatiling ligtas ang iyong API keys kapag gumagamit ng GitHub Codespaces ay sa pamamagitan ng paggamit ng Codespace Secrets. Sundin ang [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) na gabay para matuto pa tungkol dito.

## Mga Aralin at Teknikal na Kinakailangan

Ang kurso ay may 6 na konseptwal na aralin at 6 na coding na aralin.

Para sa mga coding na aralin, ginagamit namin ang Azure OpenAI Service. Kailangan mong magkaroon ng access sa Azure OpenAI service at isang API key para mapatakbo ang code na ito. Maaari kang mag-apply para makakuha ng access sa pamamagitan ng [pagsagot sa aplikasyon na ito](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Habang hinihintay ang pagproseso ng iyong aplikasyon, bawat coding na aralin ay may kasamang `README.md` file kung saan maaari mong tingnan ang code at mga output.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung ito ang unang pagkakataon mong gumamit ng Azure OpenAI service, sundin ang gabay na ito kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung ito ang unang pagkakataon mong gumamit ng OpenAI API, sundin ang gabay kung paano [gumawa at gumamit ng Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makipagkilala sa Iba pang mga Nag-aaral

Nilikha namin ang mga channel sa aming opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para makipagkilala sa iba pang mga nag-aaral. Magandang paraan ito para makipag-network sa iba pang mga negosyante, tagabuo, estudyante, at sinumang nais umangat sa Generative AI.

[![Sumali sa discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Nandoon din ang project team sa Discord server na ito upang tumulong sa mga nag-aaral.

## Mag-ambag

Ang kursong ito ay isang open-source na inisyatiba. Kung may makita kang mga pwedeng pagbutihin o mga isyu, mangyaring gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Susubaybayan ng project team ang lahat ng kontribusyon. Ang pag-ambag sa open source ay isang mahusay na paraan para paunlarin ang iyong karera sa Generative AI.

Karamihan sa mga kontribusyon ay nangangailangan na sumang-ayon ka sa Contributor License Agreement (CLA) na nagsasaad na may karapatan ka at talagang binibigyan mo kami ng karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalaga: kapag nagsasalin ng teksto sa repo na ito, siguraduhing huwag gumamit ng machine translation. Susuriin namin ang mga salin sa pamamagitan ng komunidad, kaya mangyaring mag-volunteer lamang para sa mga pagsasalin sa mga wikang bihasa ka.

Kapag nagsumite ka ng pull request, awtomatikong malalaman ng CLA-bot kung kailangan mong magbigay ng CLA at lalagyan ng angkop na label o komento ang PR. Sundin lamang ang mga tagubiling ibibigay ng bot. Isang beses mo lang ito kailangang gawin sa lahat ng repositoryo na gumagamit ng aming CLA.

Ang proyektong ito ay sumusunod sa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon, basahin ang Code of Conduct FAQ o kontakin ang [Email opencode](opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Magsimula Na Tayo

Ngayon na natapos mo na ang mga kinakailangang hakbang para matapos ang kursong ito, simulan natin sa pamamagitan ng pagkuha ng [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.