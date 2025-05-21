<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:33:26+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tl"
}
-->
# Pagsisimula sa kursong ito

Kami ay nasasabik na magsimula ka sa kursong ito at makita kung ano ang iyong maiinspire na likhain gamit ang Generative AI!

Para matiyak ang iyong tagumpay, ang pahinang ito ay naglalarawan ng mga hakbang sa pag-setup, mga teknikal na kinakailangan, at kung saan makakakuha ng tulong kung kinakailangan.

## Mga Hakbang sa Pag-setup

Para makapagsimula sa kursong ito, kailangan mong kumpletuhin ang mga sumusunod na hakbang.

### 1. I-fork ang Repo na ito

[I-fork ang buong repo na ito](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sa iyong sariling GitHub account upang magawa mong baguhin ang anumang code at kumpletuhin ang mga hamon. Maaari mo ring [i-star (🌟) ang repo na ito](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) upang mas madali itong mahanap at ang mga kaugnay na repos.

### 2. Gumawa ng codespace

Upang maiwasan ang anumang isyu sa dependency kapag pinapatakbo ang code, inirerekumenda naming patakbuhin ang kursong ito sa isang [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ito ay maaaring gawin sa pamamagitan ng pagpili ng opsyon na `Code` sa iyong forked na bersyon ng repo na ito at pagpili ng opsyon na **Codespaces**.

![Dialog na nagpapakita ng mga button para gumawa ng codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Pag-iimbak ng Iyong mga API Key

Mahalaga ang pagpapanatiling ligtas at secure ng iyong mga API key kapag gumagawa ng anumang uri ng application. Inirerekumenda naming huwag iimbak ang anumang API key nang direkta sa iyong code. Ang pag-commit ng mga detalyeng iyon sa isang pampublikong repository ay maaaring magresulta sa mga isyu sa seguridad at kahit sa hindi kanais-nais na mga gastos kung gagamitin ng isang masamang aktor.
Narito ang isang sunud-sunod na gabay kung paano gumawa ng `.env` file para sa Python at idagdag ang `GITHUB_TOKEN`:

1. **Mag-navigate sa Iyong Project Directory**: Buksan ang iyong terminal o command prompt at mag-navigate sa root directory ng iyong proyekto kung saan mo gustong gawin ang `.env` file.

   ```bash
   cd path/to/your/project
   ```

2. **Gumawa ng `.env` File**: Gamitin ang iyong paboritong text editor para gumawa ng bagong file na pinangalanang `.env`. Kung gumagamit ka ng command line, maaari mong gamitin ang `touch` (on Unix-based systems) or `echo` (sa Windows):

   Unix-based systems:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **I-edit ang `.env` File**: Buksan ang `.env` file sa isang text editor (hal., VS Code, Notepad++, o anumang ibang editor). Idagdag ang sumusunod na linya sa file, pinapalitan ang `your_github_token_here` ng iyong aktwal na GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **I-save ang File**: I-save ang mga pagbabago at isara ang text editor.

5. **I-install ang `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` package para i-load ang mga environment variable mula sa `.env` file papunta sa iyong Python application. Maaari mo itong i-install gamit ang `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **I-load ang Environment Variables sa Iyong Python Script**: Sa iyong Python script, gamitin ang `python-dotenv` package para i-load ang mga environment variable mula sa `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Tapos na! Matagumpay mong nagawa ang isang `.env` file, idinagdag ang iyong GitHub token, at na-load ito sa iyong Python application.

## Paano Patakbuhin Lokal sa iyong computer

Para patakbuhin ang code lokal sa iyong computer, kailangan mong magkaroon ng ilang bersyon ng [Python na naka-install](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para magamit ang repository, kailangan mong i-clone ito:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kapag na-check out mo na ang lahat, maaari ka nang magsimula!

## Mga Opsyonal na Hakbang 

### Pag-install ng Miniconda 

Ang [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ay isang magaan na installer para sa pag-install ng [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pati na rin ilang mga package.
Ang Conda mismo ay isang package manager, na nagpapadali sa pag-setup at paglipat sa pagitan ng iba't ibang Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) at mga package. Nakatutulong din ito sa pag-install ng mga package na hindi available sa `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

I-populate ang iyong environment file gamit ang snippet sa ibaba:

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

Kung nakakaranas ka ng mga error sa paggamit ng conda, maaari mong mano-manong i-install ang Microsoft AI Libraries gamit ang sumusunod na command sa terminal.

```
conda install -c microsoft azure-ai-ml
```

Ang environment file ay nagsasaad ng mga dependency na kailangan natin. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` ay ang pinakabagong major na bersyon ng Python.

Kapag nagawa na iyon, maaari mong gawin ang iyong Conda environment sa pamamagitan ng pagpapatakbo ng mga command sa ibaba sa iyong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tingnan ang [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kung nakakaranas ng anumang isyu.

### Paggamit ng Visual Studio Code na may Python support extension

Inirerekumenda namin ang paggamit ng [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor na may [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) na naka-install para sa kursong ito. Gayunpaman, ito ay rekomendasyon lamang at hindi isang tiyak na kinakailangan.

> **Tandaan**: Sa pamamagitan ng pagbukas ng course repository sa VS Code, mayroon kang opsyon na i-setup ang proyekto sa loob ng isang container. Ito ay dahil sa [espesyal na `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) na direktoryo na matatagpuan sa loob ng course repository. Marami pa tungkol dito mamaya.

> **Tandaan**: Kapag na-clone mo at binuksan ang direktoryo sa VS Code, awtomatiko itong magmumungkahi na mag-install ka ng Python support extension.

> **Tandaan**: Kung iminumungkahi ng VS Code na i-reopen mo ang repository sa isang container, tanggihan ang kahilingang ito upang magamit ang lokal na naka-install na bersyon ng Python.

### Paggamit ng Jupyter sa Browser

Maaari mo ring trabahuhin ang proyekto gamit ang [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkta sa loob ng iyong browser. Parehong classic Jupyter at [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ay nagbibigay ng kaaya-ayang development environment na may mga tampok tulad ng auto-completion, code highlighting, atbp.

Para simulan ang Jupyter lokal, pumunta sa terminal/command line, mag-navigate sa course directory, at i-execute:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Ito ay magsisimula ng Jupyter instance at ang URL para ma-access ito ay ipapakita sa loob ng command line window.

Kapag na-access mo ang URL, makikita mo ang course outline at makakapag-navigate sa anumang `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` file kung saan maaari mong tingnan ang code at outputs.

## Paggamit ng Azure OpenAI Service sa unang pagkakataon

Kung ito ang iyong unang pagkakataon na gumamit ng Azure OpenAI service, mangyaring sundin ang gabay kung paano [gumawa at mag-deploy ng Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Paggamit ng OpenAI API sa unang pagkakataon

Kung ito ang iyong unang pagkakataon na gumamit ng OpenAI API, mangyaring sundin ang gabay kung paano [gumawa at gamitin ang Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Makipagtagpo sa Ibang mga Nag-aaral

Gumawa kami ng mga channel sa aming opisyal na [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para makipagtagpo sa ibang mga nag-aaral. Ito ay isang mahusay na paraan upang makipag-network sa iba pang mga negosyante, tagabuo, estudyante, at sinumang nais mag-level up sa Generative AI.

[![Sumali sa discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ang team ng proyekto ay naroroon din sa Discord server na ito upang tumulong sa mga nag-aaral.

## Mag-ambag

Ang kursong ito ay isang open-source na inisyatiba. Kung makakita ka ng mga lugar na kailangan ng pagpapabuti o mga isyu, mangyaring gumawa ng [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o mag-log ng [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Ang team ng proyekto ay susubaybayan ang lahat ng kontribusyon. Ang pag-aambag sa open source ay isang kamangha-manghang paraan upang buuin ang iyong karera sa Generative AI.

Karamihan sa mga kontribusyon ay nangangailangan sa iyo na sumang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na mayroon kang karapatan at aktwal na ibinibigay sa amin ang mga karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Mahalaga: kapag nagsasalin ng teksto sa repo na ito, mangyaring tiyakin na hindi ka gumagamit ng machine translation. Suriin namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring mag-volunteer lamang para sa mga pagsasalin sa mga wika kung saan ikaw ay bihasa.

Kapag nagsumite ka ng pull request, awtomatikong matutukoy ng CLA-bot kung kailangan mong magbigay ng CLA at i-decorate ang PR nang naaangkop (hal., label, comment). Sundin lamang ang mga tagubilin na ibinigay ng bot. Kailangan mo lamang gawin ito nang isang beses sa lahat ng repositories na gumagamit ng aming CLA.

Ang proyektong ito ay nag-ampon ng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para sa karagdagang impormasyon basahin ang Code of Conduct FAQ o makipag-ugnayan sa [Email opencode](opencode@microsoft.com) para sa anumang karagdagang katanungan o komento.

## Magsimula Na Tayo

Ngayon na natapos mo na ang mga kinakailangang hakbang para kumpletuhin ang kursong ito, magsimula tayo sa pamamagitan ng pagkuha ng [panimula sa Generative AI at LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Habang sinisikap namin ang pagiging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.