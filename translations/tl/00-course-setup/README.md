# Pagsisimula sa kursong ito

Nasasabik kaming simulan mo ang kursong ito at makita kung ano ang iyong malilikha gamit ang Generative AI!

Upang matiyak ang iyong tagumpay, inilalahad ng pahinang ito ang mga hakbang sa pagsasaayos, mga teknikal na kinakailangan, at kung saan ka makakakuha ng tulong kung kinakailangan.

## Mga Hakbang sa Pagsasaayos

Upang masimulan ang kursong ito, kailangan mong kumpletuhin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo na ito](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sa iyong sariling GitHub account upang maipagpalit ang anumang code at maisagawa ang mga hamon. Maaari mo ring [staran (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) upang mas madali mo itong mahanap pati na rin ang mga kaugnay na repos.

### 2. Gumawa ng codespace

Upang maiwasan ang anumang mga isyu sa dependency kapag pinapatakbo ang code, inirerekomenda naming gamitin ang kursong ito sa isang [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Sa iyong fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/tl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Magdagdag ng secret

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Pangalanan itong OPENAI_API_KEY, i-paste ang iyong key, I-save.

### 3. Ano ang susunod?

| Gusto kong…          | Pumunta sa…                                                                  |
|---------------------|----------------------------------------------------------------------------|
| Simulan ang Lesson 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| Magtrabaho offline   | [`setup-local.md`](02-setup-local.md)                                       |
| Mag-setup ng LLM Provider | [`providers.md`](03-providers.md)                                      |
| Makipagkita sa ibang mga mag-aaral | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pag-aayos ng mga problema


| Sintoma                                   | Ayusin                                                         |
|------------------------------------------|----------------------------------------------------------------|
| Nahirapan ang pagbuo ng container > 10 min | **Codespaces ➜ “Rebuild Container”**                          |
| `python: command not found`               | Hindi na-attach ang Terminal; i-click ang **+** ➜ *bash*        |
| `401 Unauthorized` mula sa OpenAI          | Mali / expired ang `OPENAI_API_KEY`                            |
| Nagpapakita ang VS Code ng “Dev container mounting…” | I-refresh ang browser tab—may mga pagkakataon na nawawala ang koneksyon ng Codespaces   |
| Nawawala ang Notebook kernel               | Menu ng Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Mga Unix-based na sistema:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file gamit ang isang text editor (hal. VS Code, Notepad++, o anumang editor). Idagdag ang mga sumusunod na linya sa file, palitan ang mga placeholder ng iyong aktwal na Microsoft Foundry Models endpoint at key (tingnan ang [`providers.md`](03-providers.md) para sa paano makuha ito):

   > **Tandaan:** Nagwawakas na ang GitHub Models (at ang `GITHUB_TOKEN` nito) sa katapusan ng Hulyo 2026. Gamitin na ang [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa ito nagagawa, kailangan mong i-install ang package na `python-dotenv` para ma-load ang mga environment variable mula sa `.env` file sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang mga Environment Variable sa Iyong Python Script**: Sa iyong Python script, gamitin ang package na `python-dotenv` upang i-load ang mga environment variable mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # I-load ang mga environment variable mula sa .env file
   load_dotenv()

   # I-access ang mga variable ng Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ayun lang! Matagumpay mong nalikha ang `.env` file, idinagdag ang iyong Microsoft Foundry Models credentials, at na-load ang mga ito sa iyong Python application.

## Paano Patakbuhin nang Lokal sa Iyong Kompyuter

Upang patakbuhin ang code nang lokal sa iyong kompyuter, kailangan mong magkaroon ng ilang bersyon ng [Python na naka-install](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Upang magamit ang repositoryo, kailangan mo itong i-clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag na-checkout mo na ang lahat, maaari ka nang magsimula!

## Mga Opsyonal na Hakbang

### Pag-install ng Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ng ilang mga pakete.
Ang Conda mismo ay isang package manager, na nagpapadali sa pagsasaayos at paglilipat-lipat sa pagitan ng iba't ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga pakete. Kapaki-pakinabang din ito sa pag-install ng mga pakete na hindi available gamit ang `pip`.

Maaari mong sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) upang mai-setup ito.

Kapag naka-install ang Miniconda, kailangan mong i-clone ang [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kung hindi mo pa nagagawa)

Susunod, kailangan mong gumawa ng virtual environment. Para gawin ito gamit ang Conda, mag-create ng bagong environment file (_environment.yml_). Kung sumusunod ka gamit ang Codespaces, ilagay ito sa loob ng `.devcontainer` directory, kaya `.devcontainer/environment.yml`.

Punuan mo ang iyong environment file gamit ang snippet sa ibaba:

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

Kung nagkakaroon ka ng errors gamit ang conda, maaari mong manu-manong i-install ang Microsoft AI Libraries gamit ang sumusunod na utos sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Ang environment file ay nagtatalaga ng mga dependencies na kailangan natin. Ang `<environment-name>` ay tumutukoy sa pangalan na gusto mong gamitin para sa iyong Conda environment, at ang `<python-version>` ay ang bersyon ng Python na nais mong gamitin, halimbawa, ang `3` ay ang pinakabagong major na bersyon ng Python.

Kapag tapos na, maaari ka nang gumawa ng iyong Conda environment sa pamamagitan ng pagpapatakbo ng mga sumusunod na utos sa iyong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Ang sub-path na .devcontainer ay naaangkop lamang sa mga setup ng Codespace
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung sakaling magkaroon ka ng anumang isyu.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekomenda namin ang paggamit ng [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may naka-install na [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) para sa kursong ito. Ito ay isang rekomendasyon lamang at hindi isang mahigpit na kinakailangan.

> **Tandaan**: Sa pagbubukas ng course repository sa VS Code, mayroon kang opsyon na i-setup ang proyekto sa loob ng isang container. Ito ay dahil sa [espesyal na `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) na folder na matatagpuan sa loob ng course repository. Pag-uusapan pa ito sa susunod.

> **Tandaan**: Kapag na-clone mo at nabuksan ang direktoryo sa VS Code, awtomatiko nitong ire-rekomenda na i-install mo ang Python support extension.

> **Tandaan**: Kung ire-rekomenda ng VS Code na i-re-open ang repository sa isang container, tanggihan ang kahilingang ito upang magamit ang lokal na naka-install na bersyon ng Python.

### Paggamit ng Jupyter sa Browser

Maaari ka ring magtrabaho sa proyekto gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) mismo sa loob ng iyong browser. Parehong ang classic Jupyter at [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng komportableng kapaligiran sa pag-develop na may mga tampok tulad ng auto-completion, code highlighting, atbp.

Upang simulan ang Jupyter nang lokal, pumunta sa terminal/command line, mag-navigate sa directory ng kurso, at patakbuhin ang:

```bash
jupyter notebook
```

o kaya

```bash
jupyterhub
```

Magsisimula ito ng isang Jupyter instance at ipapakita sa command line window ang URL para ma-access ito.

Kapag na-access mo na ang URL, makikita mo ang outline ng kurso at maaari kang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

### Pagpapatakbo sa loob ng container

Isang alternatibo sa pag-setup ng lahat sa iyong kompyuter o Codespace ay ang paggamit ng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ang espesyal na `.devcontainer` na folder sa loob ng course repository ay nagpapahintulot sa VS Code na istraktura ang proyekto sa loob ng isang container. Sa labas ng Codespaces, kakailanganin ng pag-install ng Docker, at medyo mas kumplikado ito, kaya inirerekomenda namin ito lamang sa mga may karanasan sa paggamit ng mga container.

Isa sa mga pinakamahusay na paraan upang mapanatiling ligtas ang iyong mga API key kapag gumagamit ng GitHub Codespaces ay ang paggamit ng Codespace Secrets. Sundan ang [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) na gabay upang matuto pa tungkol dito.


## Mga Aralin at Teknikal na Kinakailangan

Ang kurso ay may mga "Learn" na aralin na nagpapaliwanag ng mga konsepto ng Generative AI at mga "Build" na aralin na may mga praktikal na halimbawa ng code sa parehong **Python** at **TypeScript** kung posible.

Para sa mga coding lessons, ginagamit namin ang Azure OpenAI sa Microsoft Foundry. Kailangan mo ng Azure subscription at isang API key. Bukas ang access—hindi kailangan ng aplikasyon—kaya maaari kang [gumawa ng Microsoft Foundry resource at mag-deploy ng model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) upang makuha ang iyong endpoint at key.

Bawat coding lesson ay mayroon ding `README.md` file kung saan maaari mong makita ang code at output nang hindi pinapatakbo ang anumang bagay.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung ito ang unang beses mong gamitin ang Azure OpenAI service, sundan ang gabay na ito kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung ito ang unang beses mong gamitin ang OpenAI API, sundan ang gabay kung paano [gumawa at gamitin ang Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makipagkilala sa Ibang mga Mag-aaral

Gumawa kami ng mga channel sa aming opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para makipagkilala sa ibang mga mag-aaral. Magandang paraan ito upang makipag-network sa iba pang mga kapwa negosyante, tagapagtayo, estudyante, at sinumang nais umangat sa Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Narito rin ang project team sa Discord server para tumulong sa anumang mga mag-aaral.

## Mag-ambag

Ang kursong ito ay isang open-source na inisyatiba. Kung may nakita kang mga lugar na pwedeng pagbutihin o may mga isyu, mangyaring gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Susubaybayan ng project team ang lahat ng mga kontribusyon. Ang pag-aambag sa open source ay isang kahanga-hangang paraan upang paunlarin ang iyong karera sa Generative AI.

Karamihan sa mga kontribusyon ay nangangailangan na pumayag ka sa isang Contributor License Agreement (CLA) na nagsasaad na ikaw ay may karapatang ibigay sa amin ang mga karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalaga: kapag isinasalin ang teksto sa repo na ito, siguraduhing huwag gumamit ng makina na pagsasalin. Susuriin namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring magboluntaryo lamang para sa mga pagsasalin sa mga wikang mahusay kang magsalita.


Kapag nagsumite ka ng pull request, awtomatikong titiyakin ng CLA-bot kung kailangan mong magsumite ng CLA at lalagyan ng naaangkop na dekorasyon ang PR (hal., label, komento). Sundin lamang ang mga tagubiling ibinigay ng bot. Isang beses mo lamang ito kailangang gawin para sa lahat ng repositoryong gumagamit ng aming CLA.

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon, basahin ang Code of Conduct FAQ o makipag-ugnayan sa [Email opencode](opencode@microsoft.com) para sa iba pang mga tanong o puna.

## Magsimula Na Tayo

Ngayong natapos mo na ang mga kinakailangang hakbang upang makumpleto ang kursong ito, magsimula tayo sa pamamagitan ng pagkuha ng [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->