# Pagsisimula sa kurso na ito

Kami ay nasasabik na ikaw ay magsimulang sa kurso na ito at makita kung ano ang maipupukaw ng iyong inspirasyon na gawin gamit ang Generative AI!

Upang matiyak ang iyong tagumpay, inilalahad ng pahinang ito ang mga hakbang sa pagsasaayos, teknikal na mga kinakailangan, at kung saan kumuha ng tulong kung kinakailangan.

## Mga Hakbang sa Pagsasaayos

Upang simulang kunin ang kurso na ito, kailangan mong kumpletuhin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo na ito](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sa iyong sariling account sa GitHub upang makapagbago ng anumang code at makumpleto ang mga hamon. Maaari mo ring [i-star (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) upang mas madali mo itong mahanap pati na ang mga kaugnay na repos.

### 2. Gumawa ng codespace

Upang maiwasan ang anumang isyu sa dependency kapag pinapatakbo ang code, inirerekomenda naming patakbuhin ang kurso na ito sa isang [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Sa iyong fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/tl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Magdagdag ng secret

1. ⚙️ Icon ng gear -> Command Pallete-> Codespaces : Manage user secret -> Magdagdag ng bagong secret.
2. Pangalanan ito bilang OPENAI_API_KEY, i-paste ang iyong key, I-save.

### 3. Ano ang susunod?

| Nais kong…             | Pumunta sa…                                                            |
|------------------------|------------------------------------------------------------------------|
| Simulan ang Lesson 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Magtrabaho offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Mag-setup ng LLM Provider | [`providers.md`](03-providers.md)                                     |
| Makilala ang ibang mga nag-aaral | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## Mga Pag-aayos ng Problema


| Sintomas                                   | Solusyon                                                          |
|--------------------------------------------|------------------------------------------------------------------|
| Container build tumigil > 10 min           | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                 | Hindi nakakabit ang terminal; i-click ang **+** ➜ *bash*         |
| `401 Unauthorized` mula sa OpenAI           | Mali / nag-expire na `OPENAI_API_KEY`                            |
| Nagpapakita ng “Dev container mounting…” sa VS Code | I-refresh ang tab ng browser—minsan nawawala ang koneksyon sa Codespaces |
| Nawawala ang kernel ng Notebook             | Menu ng Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Para sa mga Unix-based systems:

   ```bash
   touch .env
   ```

   Para sa Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file sa isang text editor (hal., VS Code, Notepad++, o anumang iba pang editor). Idagdag ang sumusunod na linya sa file, palitan ang `your_github_token_here` ng iyong aktwal na GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa ito na-install, kailangan mong i-install ang `python-dotenv` package para mabasa ang mga environment variables mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa Iyong Python Script**: Sa iyong Python script, gamitin ang `python-dotenv` package para i-load ang mga environment variables mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # I-load ang mga variable ng kapaligiran mula sa .env na file
   load_dotenv()

   # I-access ang variable na GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ayun lang! Matagumpay mong nagawa ang `.env` file, naidagdag ang iyong GitHub token, at na-load ito sa iyong Python application.

## Paano Patakbuhin nang lokal sa iyong computer

Upang patakbuhin ang code nang lokal sa iyong computer, kailangan mong magkaroon ng ilang bersyon ng [Python na naka-install](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para magamit ang repository, kailangan mo itong i-clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag naayos mo na ang lahat, maaari ka nang magsimula!

## Mga Opsyonal na Hakbang

### Pag-install ng Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ilang mga pakete.
Ang Conda mismo ay isang package manager na nagpapadali sa pagsasaayos at pagpapalit-palit ng mga Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga pakete. Nakakatulong rin ito para mag-install ng mga pakete na hindi available sa pamamagitan ng `pip`.

Maaari mong sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para masetup ito.

Kapag na-install na ang Miniconda, kailangan mong i-clone ang [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kung hindi pa nagagawa)

Susunod, kailangan mong gumawa ng virtual environment. Para dito gamit ang Conda, gumawa ng bagong environment file (_environment.yml_). Kung sumusunod ka gamit ang Codespaces, ilagay ito sa loob ng `.devcontainer` direktoryo, kaya magiging `.devcontainer/environment.yml`.

Punuin ang iyong environment file gamit ang snippet sa ibaba:

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

Kung nakararanas ng error gamit ang conda, maaari mong mano-manong i-install ang Microsoft AI Libraries gamit ang sumusunod na command sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Ang environment file ang nagtatakda ng mga dependencies na kailangan natin. Ang `<environment-name>` ay tumutukoy sa pangalan na gusto mong gamitin para sa iyong Conda environment, at ang `<python-version>` ay ang bersyon ng Python na nais mong gamitin, halimbawa, ang `3` ay ang pinakabagong pangunahing bersyon ng Python.

Kapag tapos na dito, maaari mo nang likhain ang iyong Conda environment sa pamamagitan ng pagpapatakbo ng mga command na nasa ibaba sa iyong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Ang sub path ng .devcontainer ay nalalapat lamang sa Mga setup ng Codespace
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung sakaling magkaroon ka ng mga problema.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekomenda naming gamitin ang [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) para sa kursong ito. Ito ay isang rekomendasyon lamang at hindi isang mahigpit na pangangailangan.

> **Tandaan**: Sa pagbukas ng course repository sa VS Code, may opsyon kang i-setup ang proyekto sa loob ng container. Ito ay dahil sa [espesyal na `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktoriyo na matatagpuan sa loob ng course repository. Pag-uusapan ito nang mas detalyado mamaya.

> **Tandaan**: Kapag na-clone mo at nabuksan ang direktoryo sa VS Code, awtomatiko nitong irerekomenda na i-install mo ang Python support extension.

> **Tandaan**: Kung hihilingin ng VS Code na i-reopen ang repository sa isang container, tanggihan ito kung nais mong gamitin ang lokal na naka-install na bersyon ng Python.

### Paggamit ng Jupyter sa Browser

Maaari ka ring magtrabaho sa proyekto gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkta sa iyong browser. Parehong ang classic Jupyter at [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng maginhawang development environment na may mga tampok tulad ng auto-completion, code highlighting, at iba pa.

Para simulan ang Jupyter nang lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at isagawa ang:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Ito ay magsisimula ng isang Jupyter instance at ipapakita ang URL para ma-access ito sa loob ng command line window.

Kapag na-access mo ang URL, makikita mo ang outline ng kurso at maaari kang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

### Pagpapatakbo sa isang container

Isang alternatibo sa pag-set up ng lahat sa iyong computer o Codespace ay ang paggamit ng isang [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ang espesyal na `.devcontainer` folder sa loob ng course repository ay nagpapahintulot sa VS Code na i-setup ang proyekto sa loob ng isang container. Sa labas ng Codespaces, kakailanganin nitong mag-install ka ng Docker, at sa totoo lang, medyo mahirap ito kaya inirerekomenda namin ito lamang sa mga may karanasan sa paggamit ng containers.

Isa sa pinakamahusay na paraan para panatilihing ligtas ang iyong mga API key kapag gumagamit ng GitHub Codespaces ay ang paggamit ng Codespace Secrets. Mangyaring sundin ang [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) na gabay upang matuto pa tungkol dito.


## Mga Leksyon at Teknikal na Mga Kinakailangan

Ang kurso ay may 6 na konseptong leksyon at 6 na coding lesson.

Para sa coding lessons, ginagamit namin ang Azure OpenAI Service. Kailangan mong magkaroon ng access sa Azure OpenAI service at API key upang patakbuhin ang code na ito. Maaari kang mag-apply para makakuha ng access sa pamamagitan ng [pagkumpleto ng application na ito](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Habang hinihintay ang pagproseso ng iyong aplikasyon, bawat coding lesson ay may kasamang `README.md` file kung saan maaari mong makita ang code at mga resulta.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung ito ang unang pagkakataon mo na gumamit ng Azure OpenAI service, mangyaring sundin ang gabay na ito kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung ito ang unang pagkakataon mo na gumamit ng OpenAI API, mangyaring sundan ang gabay kung paano [gumawa at gumamit ng Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makilala ang Ibang Nag-aaral

Nilikha namin ang mga channel sa aming opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para sa pagkikita ng ibang mga nag-aaral. Ito ay isang magandang paraan para makipag-network sa mga kapwa negosyante, tagabuo, estudyante, at iba pa na nais umangat sa Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ang koponan ng proyekto ay nasa Discord server din upang tumulong sa mga nag-aaral.

## Mag-ambag

Ang kursong ito ay isang open-source na inisyatibo. Kung makita mong may puwang para sa pagpapabuti o may mga isyu, mangyaring gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng isang [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Susubaybayan ng koponan ng proyekto ang lahat ng kontribusyon. Ang pag-ambag sa open source ay isang kahanga-hangang paraan upang maitaguyod ang iyong karera sa Generative AI.

Karamihan sa mga kontribusyon ay nangangailangan na sumang-ayon ka sa Contributor License Agreement (CLA) na nagsasaad na may karapatan ka at talagang ibinibigay mo sa amin ang mga karapatan na gamitin ang iyong kontribusyon. Para sa detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalaga: kapag nagsasalin ng teksto sa repo na ito, tiyakin na hindi gumagamit ng machine translation. Susuriin namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring magboluntaryo lamang para sa mga pagsasalin sa mga wika kung saan ikaw ay bihasa.

Kapag nagsumite ka ng pull request, awtomatikong matutukoy ng CLA-bot kung kailangan mong magbigay ng CLA at bibigyan ang PR ng naaangkop na dekorasyon (halimbawa, label, komento). Sundin lamang ang mga tagubilin na ibibigay ng bot. Isang beses mo lamang ito kailangang gawin sa lahat ng repos na gumagamit ng aming CLA.

Ang proyektong ito ay sumusunod sa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon basahin ang Code of Conduct FAQ o kontakin ang [Email opencode](opencode@microsoft.com) para sa anumang mga tanong o komento.

## Magsimula Na Tayo!
Ngayon na natapos mo na ang mga kinakailangang hakbang upang makumpleto ang kursong ito, magsimula tayo sa pamamagitan ng pagkuha ng isang [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kaming maging tumpak, pakitandaan na maaaring may mga pagkakamali o kamalian ang mga awtomatikong pagsasalin. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahin at opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->