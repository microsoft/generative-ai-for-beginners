# Pagsisimula sa kursong ito

Lubos kaming nasasabik na masimulan mo ang kursong ito at makita kung ano ang mga bagay na mahihikayat kang gawin gamit ang Generative AI!

Upang matiyak ang iyong tagumpay, inilalatag ng pahinang ito ang mga hakbang sa pagsasaayos, mga teknikal na kinakailangan, at kung saan maaaring humingi ng tulong kung kinakailangan.

## Mga Hakbang sa Pagsasaayos

Upang masimulan mo ang kursong ito, kailangan mong kumpletuhin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo na ito](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) papunta sa iyong sariling GitHub account upang makapagbago ka ng anumang code at makumpleto ang mga hamon. Maaari mo ring [i-star (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) upang madali mo itong mahanap pati na rin ang mga kaugnay na repo.

### 2. Gumawa ng codespace

Upang maiwasan ang mga isyu sa dependency kapag nagpapatakbo ng code, inirerekomenda naming patakbuhin mo ang kursong ito sa isang [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Sa iyong fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/tl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Magdagdag ng isang lihim

1. ⚙️ Icon ng gear -> Command Pallete-> Codespaces : Manage user secret -> Magdagdag ng bagong lihim.
2. Pangalanan itong OPENAI_API_KEY, i-paste ang iyong key, I-save.

### 3. Ano ang susunod?

| Gusto kong…          | Pupuntahan…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Simulan ang Aralin 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Magtrabaho offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Mag-setup ng Provider ng LLM | [`providers.md`](03-providers.md)                                        |
| Makipagkita sa ibang mga mag-aaral | [Sumali sa aming Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pag-aayos ng Problema


| Sintomas                                   | Ayusin                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Naipit ang pagbuo ng Container > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Hindi na-attach ang Terminal; i-click ang **+** ➜ *bash*                    |
| `401 Unauthorized` mula sa OpenAI            | Mali / expired na `OPENAI_API_KEY`                                |
| Ipinapakita ng VS Code ang “Dev container mounting…”   | I-refresh ang browser tab—minsan nawawala ang koneksyon ng Codespaces   |
| Nawawala ang Notebook kernel                   | Menu ng Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Para sa mga Unix-based na sistema:

   ```bash
   touch .env
   ```

   Para sa Windows:

   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` na File**: Buksan ang `.env` na file sa isang text editor (hal., VS Code, Notepad++, o anumang editor). Idagdag ang mga sumusunod na linya sa file, palitan ang mga placeholder ng iyong aktwal na Microsoft Foundry Models endpoint at key (tingnan ang [`providers.md`](03-providers.md) para sa kung paano makuha ito):

   > **Tandaan:** Ang GitHub Models (at ang `GITHUB_TOKEN` variable nito) ay magreretiro sa katapusan ng Hulyo 2026. Gumamit na sa halip ng [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: Kung hindi mo pa nagagawa, kailangan mong i-install ang `python-dotenv` package upang ma-load ang mga environment variables mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa iyong Python Script**: Sa iyong Python script, gamitin ang `python-dotenv` package upang i-load ang environment variables mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # I-load ang mga variable ng kapaligiran mula sa .env na file
   load_dotenv()

   # I-access ang mga variable ng Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Iyan na! Matagumpay mong nagawa ang `.env` file, naidagdag ang iyong mga kredensyal ng Microsoft Foundry Models, at na-load ang mga ito sa iyong Python application.

## Paano patakbuhin nang lokal sa iyong kompyuter

Upang patakbuhin ang code nang lokal sa iyong kompyuter, kailangan mong magkaroon ng ilang bersyon ng [Python na naka-install](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para magamit ang repository, kailangan mo itong i-clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag na-check out mo na ang lahat, maaari ka nang magsimula!

## Opsyonal na mga Hakbang

### Pag-install ng Miniconda

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ng ilang mga pakete.
Ang Conda mismo ay isang package manager, na nagpapadali sa pagsasaayos at pagbabago-bago sa pagitan ng iba't ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga pakete. Kapaki-pakinabang din ito para sa pag-install ng mga pakete na hindi available sa pamamagitan ng `pip`.

Maaari mong sundan ang [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para sa pagsasaayos nito.

Kapag naka-install na ang Miniconda, kailangan mong i-clone ang [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kung hindi mo pa nagagawa)

Susunod, kailangan mong gumawa ng virtual environment. Para gawin ito gamit ang Conda, gumawa ng bagong environment file (_environment.yml_). Kung sumusunod ka sa Codespaces, gawin ito sa loob ng `.devcontainer` directory, kaya magiging `.devcontainer/environment.yml`.

Go ahead at punuin mo ang environment file gamit ang snippet sa ibaba:

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

Kung nakakaranas ka ng mga error sa paggamit ng conda, maaari mong manu-manong i-install ang Microsoft AI Libraries gamit ang sumusunod na command sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Itinakda ng environment file ang mga dependencies na kailangan natin. Ang `<environment-name>` ay tumutukoy sa pangalan na nais mong gamitin para sa iyong Conda environment, at ang `<python-version>` ay ang bersyon ng Python na gusto mong gamitin, halimbawa, ang `3` ay ang pinakabagong major version ng Python.

Kapag nagawa na ito, maaari mo nang likhain ang iyong Conda environment sa pamamagitan ng pagpapatakbo ng mga utos sa ibaba sa iyong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path ay naaangkop lamang sa mga setup ng Codespace
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung sakaling may mga isyu kang maranasan.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekomenda naming gamitin ang [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may naka-install na [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) para sa kursong ito. Ito ay isang rekomendasyon at hindi isang tiyak na kinakailangan

> **Tandaan**: Sa pagbubukas ng course repository sa VS Code, mayroon kang opsyon na i-setup ang proyekto sa loob ng container. Ito ay dahil sa [espesyal na `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) na direktoryo na matatagpuan sa loob ng course repository. Ipaliwanag pa ito sa susunod.

> **Tandaan**: Kapag ni-clone at binuksan mo ang direktoryo sa VS Code, awtomatiko nitong irerekomenda na mag-install ka ng Python support extension.

> **Tandaan**: Kung ang VS Code ay magmumungkahi na i-reopen ang repository sa isang container, tanggihan ito upang magamit ang locally installed version ng Python.

### Paggamit ng Jupyter sa Browser

Maaari ka ring magtrabaho sa proyekto gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkta sa iyong browser. Ang parehong klasikong Jupyter at ang [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng maginhawang kapaligiran sa pag-develop na may mga tampok tulad ng auto-completion, pag-highlight ng code, at iba pa.

Upang simulan ang Jupyter lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at patakbuhin ang:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Ito ay magsisimula ng isang Jupyter instance at ipapakita sa loob ng command line window ang URL para ma-access ito.

Kapag na-access mo ang URL, makikita mo ang outline ng kurso at maaari kang mag-navigate sa anumang `*.ipynb` file. Halimbawa, `08-building-search-applications/python/oai-solution.ipynb`.

### Pagpapatakbo sa loob ng isang container

Isang alternatibo sa pagsasaayos ng lahat sa iyong kompyuter o Codespace ay ang paggamit ng isang [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ang espesyal na `.devcontainer` folder sa loob ng course repository ay nagpapahintulot sa VS Code na isaayos ang proyekto sa loob ng container. Sa labas ng Codespaces, kakailanganin ang pag-install ng Docker, at, sa totoo lang, medyo masalimuot ito kaya inirerekomenda namin ito lamang sa mga may karanasan gamit ang mga container.

Isa sa mga pinakamahusay na paraan upang mapanatili ang seguridad ng iyong mga API key kapag gumagamit ng GitHub Codespaces ay gamit ang Codespace Secrets. Pakiusap sundin ang [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) na gabay upang matuto nang higit pa tungkol dito.


## Mga Aralin at Teknikal na Kinakailangan

Ang kurso ay may 6 na konseptwal na aralin at 6 na aralin sa coding.

Para sa mga aralin sa coding, ginagamit namin ang Azure OpenAI Service. Kailangan mo ng access sa Azure OpenAI service at API key upang maipatakbo ang code. Maaari kang mag-apply para makakuha ng access sa pamamagitan ng [pagkumpleto sa application na ito](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Habang hinihintay mo ang pagproseso ng iyong aplikasyon, ang bawat aralin sa coding ay mayroon ding `README.md` file kung saan maaari mong makita ang code at outputs.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung ito ang iyong unang pagkakataon na gumamit ng Azure OpenAI service, pakisunod ang gabay kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung ito ang iyong unang pagkakataon na gumamit ng OpenAI API, pakisunod ang gabay kung paano [gumawa at gumamit ng Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makipagkita sa Ibang mga Mag-aaral

Nilikha namin ang mga channel sa aming opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para sa pakikipagkita sa ibang mga mag-aaral. Ito ay isang mahusay na paraan upang makipag-network sa ibang mga kagaya mong entrepreneur, mga tagapagtayo, mag-aaral, at sinumang naghahangad na umunlad sa Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ang team ng proyekto ay narito rin sa Discord server upang makatulong sa anumang mga mag-aaral.

## Mag-ambag

Ang kursong ito ay isang open-source na inisyatibo. Kung may makita kang mga pwedeng pagbutihin o mga isyu, mangyaring gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Ang team ng proyekto ay susubaybay sa lahat ng mga kontribusyon. Ang pag-aambag sa open source ay isang kamangha-manghang paraan upang buuin ang iyong karera sa Generative AI.

Karamihan sa mga kontribusyon ay nangangailangan na pumayag ka sa isang Contributor License Agreement (CLA) na nagsasaad na ikaw ay may karapatan at legal na nagbibigay ng pahintulot na gamitin namin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalagang tandaan: kapag nagsasalin ng teksto sa repo na ito, siguraduhing HINDI gumamit ng machine translation. Vevtificatinarin namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring magboluntaryo lang sa mga pagsasalin sa mga wikang mahusay ka.

Kapag nagsumite ka ng pull request, awtomatikong tutukuyin ng CLA-bot kung kailangan mong magbigay ng CLA at lalagyan ng angkop na dekorasyon ang PR (hal., label, comment). Sundin lamang ang mga tagubiling ibibigay ng bot. Gagawin mo lang ito minsan sa lahat ng mga repository na gumagamit ng aming CLA.


Ang proyektong ito ay nagpatibay ng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon, basahin ang Code of Conduct FAQ o makipag-ugnayan sa [Email opencode](opencode@microsoft.com) para sa anumang karagdagang tanong o komentaryo.

## Magsimula Na Tayo

Ngayon na natapos mo na ang mga kailangang hakbang para tapusin ang kursong ito, magsimula tayo sa pamamagitan ng pagkuha ng [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->