<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:56:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Kuanza na kozi hii

Tuna furaha sana kwa wewe kuanza kozi hii na kuona kile utakachopata msukumo wa kujenga na AI Inayotengeneza!

Ili kuhakikisha mafanikio yako, ukurasa huu unaeleza hatua za kuanzisha, mahitaji ya kiufundi, na wapi pa kupata msaada ikiwa unahitajika.

## Hatua za Kuanzisha

Ili kuanza kuchukua kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Nakili Hifadhi Hii

[Nakili hifadhi hii yote](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako mwenyewe ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Unaweza pia [kuweka alama (🌟) kwenye hifadhi hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na hifadhi zinazohusiana kwa urahisi.

### 2. Tengeneza nafasi ya msimbo

Ili kuepuka masuala yoyote ya utegemezi wakati wa kuendesha msimbo, tunapendekeza kuendesha kozi hii katika [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Hii inaweza kuundwa kwa kuchagua chaguo la `Code` kwenye toleo lako la hifadhi hii na kuchagua chaguo la **Codespaces**.

![Dialog inayoonyesha vitufe vya kuunda nafasi ya msimbo](../../../00-course-setup/images/who-will-pay.webp)

### 3. Kuhifadhi Funguo Zako za API

Kuhifadhi funguo zako za API kwa usalama ni muhimu wakati wa kujenga aina yoyote ya programu. Tunapendekeza usihifadhi funguo za API moja kwa moja kwenye msimbo wako. Kujumuisha maelezo hayo kwenye hifadhi ya umma kunaweza kusababisha masuala ya usalama na hata gharama zisizohitajika ikiwa zitatumiwa na mtu mbaya.
Hapa kuna mwongozo wa hatua kwa hatua jinsi ya kuunda faili ya `.env` kwa Python na kuongeza `GITHUB_TOKEN`:

1. **Nenda kwenye Saraka ya Mradi Wako**: Fungua terminal yako au command prompt na nenda kwenye saraka kuu ya mradi wako ambapo unataka kuunda faili ya `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Unda Faili ya `.env`**: Tumia mhariri wa maandishi unaoupenda kuunda faili mpya inayoitwa `.env`. Ikiwa unatumia command line, unaweza kutumia `touch` (on Unix-based systems) or `echo` (kwenye Windows):

   Mfumo wa Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Hariri Faili ya `.env`**: Fungua faili ya `.env` katika mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mstari ufuatao kwenye faili, ukibadilisha `your_github_token_here` na token yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funga mhariri wa maandishi.

5. **Sakinisha kifurushi cha `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` ili kupakia vigezo vya mazingira kutoka kwenye faili ya `.env` kwenye programu yako ya Python. Unaweza kukisakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira kwenye Script Yako ya Python**: Katika script yako ya Python, tumia kifurushi cha `python-dotenv` kupakia vigezo vya mazingira kutoka kwenye faili ya `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hiyo ndiyo yote! Umefanikiwa kuunda faili ya `.env`, kuongeza token yako ya GitHub, na kuipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha kwenye Kompyuta Yako

Ili kuendesha msimbo kwenye kompyuta yako, utahitaji kuwa na toleo fulani la [Python iliyosakinishwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha kutumia hifadhi, unahitaji kuikopi:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Baada ya kuwa na kila kitu, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kisakinishi chepesi kwa kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na vifurushi vichache.
Conda yenyewe ni msimamizi wa kifurushi, ambayo inafanya iwe rahisi kuanzisha na kubadilisha kati ya [**mazingira ya kawaida ya Python**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi. Pia ni muhimu kwa kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Endelea na kujaza faili yako ya mazingira kwa kipande kilicho hapa chini:

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

Ikiwa unakutana na makosa ukitumia conda unaweza kusakinisha maktaba za Microsoft AI kwa kutumia amri ifuatayo kwenye terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili ya mazingira inaelezea utegemezi tunazohitaji. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` ni toleo kuu la Python la hivi karibuni.

Baada ya hayo, unaweza kuendelea na kuunda mazingira yako ya Conda kwa kuendesha amri zilizo hapa chini kwenye mstari wa amri/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rejelea mwongozo wa [mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa utakutana na masuala yoyote.

### Kutumia Visual Studio Code na kiendelezi cha msaada wa Python

Tunapendekeza kutumia mhariri wa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) na kiendelezi cha msaada wa Python kilichosakinishwa kwa kozi hii. Hii, hata hivyo, ni pendekezo zaidi na si hitaji la lazima.

> **Kumbuka**: Kwa kufungua hifadhi ya kozi katika VS Code, una chaguo la kuanzisha mradi ndani ya kontena. Hii ni kwa sababu ya saraka ya [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) maalum inayopatikana ndani ya hifadhi ya kozi. Zaidi kuhusu hili baadaye.

> **Kumbuka**: Mara unapo kopi na kufungua saraka katika VS Code, itapendekeza moja kwa moja usakinishe kiendelezi cha msaada wa Python.

> **Kumbuka**: Ikiwa VS Code inapendekeza ufungue tena hifadhi katika kontena, kataa ombi hili ili kutumia toleo la Python lililosakinishwa kwenye kompyuta yako.

### Kutumia Jupyter kwenye Kivinjari

Unaweza pia kufanya kazi kwenye mradi ukitumia mazingira ya [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja ndani ya kivinjari chako. Jupyter ya kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) hutoa mazingira mazuri ya maendeleo yenye vipengele kama vile kukamilisha kiotomatiki, kuangazia msimbo, n.k.

Kuanzisha Jupyter kwenye kompyuta yako, nenda kwenye terminal/mstari wa amri, elekea kwenye saraka ya kozi, na utekeleze:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha mfano wa Jupyter na URL ya kuifikia itaonyeshwa ndani ya dirisha la mstari wa amri.

Mara unapoifikia URL, unapaswa kuona muhtasari wa kozi na uweze kwenda kwenye faili yoyote ya `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` ambapo unaweza kuona msimbo na matokeo.

## Kutumia Huduma ya Azure OpenAI kwa mara ya kwanza

Ikiwa hii ni mara yako ya kwanza kufanya kazi na huduma ya Azure OpenAI, tafadhali fuata mwongozo huu jinsi ya [kuunda na kupeleka rasilimali ya Huduma ya Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia API ya OpenAI kwa mara ya kwanza

Ikiwa hii ni mara yako ya kwanza kufanya kazi na API ya OpenAI, tafadhali fuata mwongozo juu ya jinsi ya [kuunda na kutumia Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kukutana na Wanafunzi Wengine

Tumetengeneza njia katika seva yetu rasmi ya [Discord ya Jamii ya AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kukutana na wanafunzi wengine. Hii ni njia nzuri ya kujenga mtandao na wajasiriamali wengine wenye mawazo sawa, wajenzi, wanafunzi, na yeyote anayetaka kuboresha uwezo wake katika AI Inayotengeneza.

[![Jiunge na njia ya discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwa kwenye seva hii ya Discord kusaidia wanafunzi wowote.

## Kuchangia

Kozi hii ni mpango wa chanzo huria. Ikiwa unaona maeneo ya kuboresha au masuala, tafadhali unda [Ombi la Kuvuta](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au logi suala la [GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itakuwa ikifuatilia michango yote. Kuchangia kwa chanzo huria ni njia ya ajabu ya kujenga kazi yako katika AI Inayotengeneza.

Michango mingi inahitaji ukubali Mkataba wa Leseni ya Mchangiaji (CLA) unaotangaza kuwa una haki ya na kwa kweli unatoa, kutupa haki za kutumia mchango wako. Kwa maelezo, tembelea [tovuti ya CLA, Mkataba wa Leseni ya Mchangiaji](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: wakati wa kutafsiri maandishi katika hifadhi hii, tafadhali hakikisha kuwa hutumii tafsiri ya mashine. Tutathibitisha tafsiri kupitia jamii, hivyo tafadhali jitoe tu kwa tafsiri katika lugha ambazo unazifahamu.

Unapowasilisha ombi la kuvuta, CLA-bot itaamua moja kwa moja ikiwa unahitaji kutoa CLA na kuipamba PR ipasavyo (mfano, lebo, maoni). Fuata tu maelekezo yaliyotolewa na roboti. Utahitaji kufanya hivi mara moja tu katika hifadhi zote zinazotumia CLA yetu.

Mradi huu umekubali [Kanuni za Maadili ya Chanzo Huria ya Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali Yanayoulizwa Mara kwa Mara ya Kanuni za Maadili au wasiliana na [Barua pepe ya opencode](opencode@microsoft.com) kwa maswali au maoni yoyote ya ziada.

## Twende Tukaanze

Sasa kwa kuwa umekamilisha hatua zinazohitajika kumaliza kozi hii, twende tukaanze kwa kupata [utambulisho wa AI Inayotengeneza na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.