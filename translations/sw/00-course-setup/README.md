<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:33:58+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Kuanza na Kozi Hii

Tunafurahia sana kwamba unaanza kozi hii na kuona kile utakachopata msukumo wa kujenga na AI ya Kuzalisha!

Ili kuhakikisha mafanikio yako, ukurasa huu unaelezea hatua za usakinishaji, mahitaji ya kiufundi, na wapi kupata msaada ikiwa unahitaji.

## Hatua za Usakinishaji

Ili kuanza kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Fork Repo Hii

[Fork repo hii yote](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Unaweza pia [kuweka nyota (🌟) kwenye repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na repo zinazohusiana kwa urahisi zaidi.

### 2. Unda Codespace

Ili kuepuka masuala yoyote ya utegemezi wakati wa kuendesha msimbo, tunapendekeza kuendesha kozi hii kwenye [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Hii inaweza kuundwa kwa kuchagua chaguo la `Code` kwenye toleo lako la repo hii na kuchagua chaguo la **Codespaces**.

![Dialog inayoonyesha vitufe vya kuunda codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Kuhifadhi Funguo Zako za API

Kuhifadhi funguo zako za API kwa usalama ni muhimu wakati wa kujenga aina yoyote ya programu. Tunapendekeza usihifadhi funguo zozote za API moja kwa moja kwenye msimbo wako. Kujumuisha maelezo hayo kwenye repo ya umma kunaweza kusababisha masuala ya usalama na hata gharama zisizohitajika ikiwa itatumiwa na mtu mbaya. Hapa kuna mwongozo wa hatua kwa hatua jinsi ya kuunda faili ya `.env` kwa Python na kuongeza `GITHUB_TOKEN`:

1. **Nenda kwenye Saraka ya Mradi Wako**: Fungua terminal yako au command prompt na nenda kwenye saraka kuu ya mradi wako ambapo unataka kuunda faili ya `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Unda Faili ya `.env`**: Tumia mhariri wako wa maandishi unaopendelea kuunda faili mpya yenye jina `.env`. Ikiwa unatumia mstari wa amri, unaweza kutumia `touch` (on Unix-based systems) or `echo` (kwenye Windows):

   Mifumo ya Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Hariri Faili ya `.env`**: Fungua faili ya `.env` kwenye mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mstari ufuatao kwenye faili, ukibadilisha `your_github_token_here` na tokeni yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funga mhariri wa maandishi.

5. **Sakinisha kifurushi cha `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` ili kupakia mazingira ya kutofautiana kutoka kwenye faili ya `.env` kwenye programu yako ya Python. Unaweza kukisakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira kwenye Msimbo Wako wa Python**: Kwenye msimbo wako wa Python, tumia kifurushi cha `python-dotenv` kupakia vigezo vya mazingira kutoka kwenye faili ya `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hiyo ndiyo yote! Umefanikiwa kuunda faili ya `.env`, kuongeza tokeni yako ya GitHub, na kuipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha Kimahali kwenye Kompyuta Yako

Ili kuendesha msimbo kimahali kwenye kompyuta yako, utahitaji kuwa na toleo fulani la [Python iliyosakinishwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha ili kutumia repo, unahitaji kuiklon:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Mara tu unapokuwa na kila kitu kilichopakuliwa, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kisakinishi chepesi cha kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na vifurushi vichache. Conda yenyewe ni meneja wa vifurushi, ambayo inafanya iwe rahisi kusanidi na kubadilisha kati ya [**mazingira ya kawaida ya Python**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi. Pia inasaidia kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Endelea na jaza faili yako ya mazingira kwa snippet iliyo hapa chini:

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

Ikiwa unapata makosa ukitumia conda unaweza kusakinisha kwa mkono Maktaba za AI za Microsoft kwa kutumia amri ifuatayo kwenye terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili ya mazingira inabainisha utegemezi tunazohitaji. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` ni toleo kuu la hivi karibuni la Python.

Baada ya kufanya hivyo, unaweza kuendelea na kuunda mazingira yako ya Conda kwa kuendesha amri zilizo hapa chini kwenye mstari wako wa amri/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rejelea [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa unakutana na matatizo yoyote.

### Kutumia Visual Studio Code na kiendelezi cha msaada wa Python

Tunapendekeza kutumia mhariri wa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) na kiendelezi cha msaada wa [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kilichosakinishwa kwa kozi hii. Hii, hata hivyo, ni zaidi ya pendekezo na si sharti la lazima.

> **Kumbuka**: Kwa kufungua repo ya kozi katika VS Code, unayo chaguo la kusanidi mradi ndani ya kontena. Hii ni kwa sababu ya saraka maalum ya [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) inayopatikana ndani ya repo ya kozi. Zaidi juu ya hili baadaye.

> **Kumbuka**: Mara tu unapoklon na kufungua saraka katika VS Code, itapendekeza moja kwa moja usakinishe kiendelezi cha msaada wa Python.

> **Kumbuka**: Ikiwa VS Code inapendekeza ufungue tena repo katika kontena, kataa ombi hili ili kutumia toleo la Python lililosakinishwa kimahali.

### Kutumia Jupyter kwenye Kivinjari

Unaweza pia kufanya kazi kwenye mradi kwa kutumia mazingira ya [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja ndani ya kivinjari chako. Jupyter ya kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) zote mbili zinatoa mazingira mazuri ya maendeleo yenye vipengele kama vile kukamilisha kiotomatiki, kuangazia msimbo, n.k.

Ili kuanza Jupyter kimahali, nenda kwenye terminal/command line, nenda kwenye saraka ya kozi, na utekeleze:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha mfano wa Jupyter na URL ya kuifikia itaonyeshwa ndani ya dirisha la mstari wa amri.

Mara tu unapofikia URL, unapaswa kuona muhtasari wa kozi na uweze kwenda kwenye faili yoyote ya `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` ambapo unaweza kuona msimbo na matokeo.

## Kutumia Huduma ya Azure OpenAI kwa Mara ya Kwanza

Ikiwa hii ni mara yako ya kwanza kufanya kazi na huduma ya Azure OpenAI, tafadhali fuata mwongozo huu jinsi ya [kuunda na kupeleka rasilimali ya Huduma ya Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia API ya OpenAI kwa Mara ya Kwanza

Ikiwa hii ni mara yako ya kwanza kufanya kazi na API ya OpenAI, tafadhali fuata mwongozo jinsi ya [kuunda na kutumia Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kutana na Wanafunzi Wengine

Tumetengeneza njia katika seva yetu rasmi ya [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kukutana na wanafunzi wengine. Hii ni njia nzuri ya kujenga mtandao na wajasiriamali wengine wenye mawazo sawa, wajenzi, wanafunzi, na yeyote anayelenga kujiendeleza katika AI ya Kuzalisha.

[![Jiunge na njia ya discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwa kwenye seva hii ya Discord kusaidia wanafunzi wowote.

## Changia

Kozi hii ni mpango wa chanzo wazi. Ikiwa unaona maeneo ya kuboresha au masuala, tafadhali tengeneza [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au weka [suala la GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itakuwa ikifuatilia michango yote. Kuchangia katika chanzo wazi ni njia nzuri ya kujenga kazi yako katika AI ya Kuzalisha.

Michango mingi inahitaji ukubaliane na Mkataba wa Leseni ya Mchangiaji (CLA) unaotangaza kuwa una haki ya na kwa kweli unatoa, ruhusa kwetu kutumia mchango wako. Kwa maelezo, tembelea [tovuti ya CLA, Mkataba wa Leseni ya Mchangiaji](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: unapofanya tafsiri ya maandishi katika repo hii, tafadhali hakikisha kuwa hutumii tafsiri ya mashine. Tutathibitisha tafsiri kupitia jamii, kwa hivyo tafadhali jitolee tu kwa tafsiri katika lugha ambazo unazifahamu vizuri.

Unapowasilisha ombi la kuvuta, CLA-bot itabaini moja kwa moja ikiwa unahitaji kutoa CLA na kupamba PR ipasavyo (mfano, lebo, maoni). Fuata tu maagizo yaliyotolewa na bot. Utahitaji kufanya hivyo mara moja tu katika repo zote zinazotumia CLA yetu.

Mradi huu umechukua [Kanuni za Maadili ya Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali Yanayoulizwa Mara kwa Mara ya Kanuni za Maadili au wasiliana na [Email opencode](opencode@microsoft.com) kwa maswali au maoni ya ziada.

## Twende Kuanza

Sasa kwa kuwa umekamilisha hatua zinazohitajika kukamilisha kozi hii, hebu tuanze kwa kupata [utambulisho wa AI ya Kuzalisha na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokamilika. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo rasmi. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.