<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:15:01+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Kuanzia na kozi hii

Tunafurahia sana kwamba umeanza kozi hii na kuona unachovutiwa kujifunza kujenga kwa kutumia Generative AI!

Ili kuhakikisha unafanikiwa, ukurasa huu unaelezea hatua za kuanzisha, mahitaji ya kiufundi, na mahali pa kupata msaada ikiwa utahitaji.

## Hatua za Kuanzisha

Ili kuanza kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Fanya Fork ya Repo hii

[Fanya fork ya repo hii yote](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Pia unaweza [kutoa nyota (🌟) kwa repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na repos zinazohusiana kwa urahisi zaidi.

### 2. Tengeneza codespace

Ili kuepuka matatizo yoyote ya utegemezi wakati wa kuendesha msimbo, tunapendekeza kuendesha kozi hii katika [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Hii inaweza kuundwa kwa kuchagua chaguo la `Code` kwenye toleo lako la fork la repo hii na kisha kuchagua chaguo la **Codespaces**.

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Kuhifadhi API Keys Zako

Kuhifadhi API keys zako salama ni muhimu wakati wa kujenga aina yoyote ya programu. Tunapendekeza usihifadhi API keys moja kwa moja ndani ya msimbo wako. Kuweka maelezo hayo kwenye repo ya umma kunaweza kusababisha matatizo ya usalama na hata gharama zisizotarajiwa ikiwa zitatumika na mtu mwenye nia mbaya.  
Hapa kuna mwongozo wa hatua kwa hatua jinsi ya kuunda faili la `.env` kwa Python na kuongeza `GITHUB_TOKEN`:

1. **Nenda kwenye Kabrasha la Mradi Wako**: Fungua terminal au command prompt na nenda kwenye kabrasha kuu la mradi wako ambapo unataka kuunda faili la `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Unda Faili la `.env`**: Tumia mhariri wa maandishi unayopendelea kuunda faili mpya liitwalo `.env`. Ikiwa unatumia command line, unaweza kutumia `touch` (kwa mifumo ya Unix) au `echo` (kwa Windows):

   Mifumo ya Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili la `.env`**: Fungua faili la `.env` katika mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mstari ufuatao kwenye faili, ukibadilisha `your_github_token_here` na tokeni yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funga mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Ikiwa bado hujasakinisha, utahitaji kusakinisha kifurushi cha `python-dotenv` ili kupakia mabadiliko ya mazingira kutoka kwenye faili la `.env` kwenye programu yako ya Python. Unaweza kusakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Mabadiliko ya Mazingira katika Script yako ya Python**: Katika script yako ya Python, tumia kifurushi cha `python-dotenv` kupakia mabadiliko ya mazingira kutoka kwenye faili la `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hiyo ni yote! Umefanikiwa kuunda faili la `.env`, kuongeza tokeni yako ya GitHub, na kuipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha kwa Kompyuta Yako

Ili kuendesha msimbo kwa kompyuta yako, utahitaji kuwa na toleo fulani la [Python limewekwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha, ili kutumia repository, unahitaji kuikopa (clone):

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Mara baada ya kuwa na kila kitu tayari, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni msakinishaji mwepesi wa kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na vifurushi vingine kadhaa.  
Conda ni meneja wa vifurushi, ambayo hufanya iwe rahisi kuanzisha na kubadilisha kati ya [mazingira ya virtual ya Python](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi. Pia ni muhimu kwa kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

Unaweza kufuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kuisanikisha.

Baada ya kusakinisha Miniconda, unahitaji kuikopa [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ikiwa bado hujafanya hivyo).

Kisha, unahitaji kuunda mazingira ya virtual. Ili kufanya hivyo kwa Conda, endelea na tengeneza faili jipya la mazingira (_environment.yml_). Ikiwa unafuata kwa kutumia Codespaces, tengeneza hili ndani ya kabrasha la `.devcontainer`, yaani `.devcontainer/environment.yml`.

Endelea na jaza faili lako la mazingira na kipande kilicho hapa chini:

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

Ikiwa unakutana na makosa unapotumia conda, unaweza kusakinisha maktaba za Microsoft AI kwa mkono kwa kutumia amri ifuatayo kwenye terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili la mazingira linaelezea utegemezi tunazohitaji. `<environment-name>` linarejelea jina unalotaka kutumia kwa mazingira yako ya Conda, na `<python-version>` ni toleo la Python unalotaka kutumia, kwa mfano, `3` ni toleo kuu la hivi karibuni la Python.

Baada ya hapo, unaweza kuunda mazingira yako ya Conda kwa kuendesha amri zifuatazo kwenye command line/terminal yako

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rejea [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa utakutana na matatizo yoyote.

### Kutumia Visual Studio Code na ugani wa msaada wa Python

Tunapendekeza kutumia mhariri wa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) pamoja na [ugani wa msaada wa Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) uliosakinishwa kwa kozi hii. Hii ni pendekezo tu na si sharti la lazima.

> **Note**: Kwa kufungua repo ya kozi katika VS Code, una chaguo la kuanzisha mradi ndani ya container. Hii ni kwa sababu ya kabrasha maalum la [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) lililopo ndani ya repo ya kozi. Tutaelezea zaidi baadaye.

> **Note**: Mara tu unapokopa na kufungua kabrasha hilo katika VS Code, itapendekeza moja kwa moja usakinishe ugani wa msaada wa Python.

> **Note**: Ikiwa VS Code itapendekeza ufungue repo tena ndani ya container, kataa ombi hili ili utumie toleo la Python lililosakinishwa kwa ndani.

### Kutumia Jupyter katika Kivinjari

Unaweza pia kufanya kazi kwenye mradi kwa kutumia [mazingira ya Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja katika kivinjari chako. Jupyter wa kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) hutoa mazingira mazuri ya maendeleo yenye vipengele kama kukamilisha kiotomatiki, kuangazia msimbo, n.k.

Ili kuanzisha Jupyter kwa ndani, nenda kwenye terminal/command line, nenda kwenye kabrasha la kozi, na endesha:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha toleo la Jupyter na URL ya kuifikia itaonyeshwa ndani ya dirisha la command line.

Mara utakapoingia kwenye URL, utapata muhtasari wa kozi na utaweza kuvinjari faili yoyote ya `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

### Kuendesha ndani ya container

Mbali na kuanzisha kila kitu kwenye kompyuta yako au Codespace, unaweza kutumia [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kabrasha maalum la `.devcontainer` ndani ya repo ya kozi linawezesha VS Code kuanzisha mradi ndani ya container. Mbali na Codespaces, hii itahitaji usakinishaji wa Docker, na kwa kweli, inahusisha kazi kidogo, hivyo tunapendekeza hii kwa wale tu wenye uzoefu wa kutumia containers.

Njia mojawapo bora za kuhakikisha API keys zako zinabaki salama unapotumia GitHub Codespaces ni kwa kutumia Codespace Secrets. Tafadhali fuata mwongozo wa [usimamizi wa siri za Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ili kujifunza zaidi kuhusu hili.

## Masomo na Mahitaji ya Kiufundi

Kozi ina masomo 6 ya dhana na masomo 6 ya uandishi wa msimbo.

Kwa masomo ya uandishi wa msimbo, tunatumia Azure OpenAI Service. Utahitaji kupata huduma ya Azure OpenAI na API key ili kuendesha msimbo huu. Unaweza kuomba kupata huduma kwa [kukamilisha maombi haya](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Wakati unasubiri maombi yako kushughulikiwa, kila somo la uandishi wa msimbo pia lina faili la `README.md` ambapo unaweza kuona msimbo na matokeo.

## Kutumia Azure OpenAI Service kwa mara ya kwanza

Ikiwa ni mara yako ya kwanza kutumia huduma ya Azure OpenAI, tafadhali fuata mwongozo huu wa jinsi ya [kuunda na kupeleka rasilimali ya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia OpenAI API kwa mara ya kwanza

Ikiwa ni mara yako ya kwanza kutumia OpenAI API, tafadhali fuata mwongozo wa jinsi ya [kuunda na kutumia Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kutana na Wanafunzi Wengine

Tumeunda vituo kwenye seva rasmi ya [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kukutana na wanafunzi wengine. Hii ni njia nzuri ya kuungana na wajasiriamali, wajenzi, wanafunzi, na yeyote anayetaka kujiendeleza katika Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwa kwenye seva hii ya Discord kusaidia wanafunzi wote.

## Changia

Kozi hii ni mpango wa chanzo huria. Ikiwa unaona maeneo ya kuboresha au matatizo, tafadhali tengeneza [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au andika [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itafuatilia michango yote. Kuchangia chanzo huria ni njia nzuri ya kujenga taaluma yako katika Generative AI.

Michango mingi inahitaji kukubaliana na Mkataba wa Leseni ya Mchango (CLA) unaothibitisha kuwa una haki na kwa kweli unaturuhusu kutumia mchango wako. Kwa maelezo zaidi, tembelea [CLA, Tovuti ya Mkataba wa Leseni ya Mchango](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: wakati wa kutafsiri maandishi katika repo hii, tafadhali hakikisha hutumii tafsiri za mashine. Tutathibitisha tafsiri kupitia jamii, hivyo tafadhali jitolee tu kutafsiri lugha unazozifahamu vizuri.

Unapowasilisha pull request, CLA-bot atagundua moja kwa moja kama unahitaji kutoa CLA na kuipamba PR ipasavyo (mfano, lebo, maoni). Fuata tu maelekezo yanayotolewa na bot. Hii utahitaji kufanya mara moja tu kwa repos zote zinazotumia CLA yetu.

Mradi huu umechukua [Kanuni za Maadili za Chanzo Huria za Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali Yanayoulizwa Mara kwa Mara kuhusu Kanuni za Maadili au wasiliana na [Email opencode](opencode@microsoft.com) kwa maswali au maoni zaidi.

## Hebu Tuanze

Sasa baada ya kukamilisha hatua zinazohitajika kwa kozi hii, tuanze kwa kupata [utangulizi wa Generative AI na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.