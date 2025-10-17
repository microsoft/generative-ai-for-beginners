<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T21:12:21+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Kuanza na kozi hii

Tunafurahi sana kwa wewe kuanza kozi hii na kuona kile unachoweza kuhamasika kujenga kwa kutumia Generative AI!

Ili kuhakikisha mafanikio yako, ukurasa huu unaelezea hatua za kuanzisha, mahitaji ya kiufundi, na wapi pa kupata msaada ikiwa unahitaji.

## Hatua za Kuanzisha

Ili kuanza kuchukua kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Fork Repo Hii

[Fork repo hii yote](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Unaweza pia [kuweka nyota (🌟) repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na repo zinazohusiana kwa urahisi.

### 2. Unda Codespace

Ili kuepuka masuala ya utegemezi wakati wa kuendesha msimbo, tunapendekeza kuendesha kozi hii katika [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Katika fork yako: **Code -> Codespaces -> New on main**

![Dialog inayoonyesha vifungo vya kuunda codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Ongeza Siri

1. ⚙️ Ikoni ya gia -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Jina OPENAI_API_KEY, weka funguo yako, Hifadhi.

### 3. Nini Kinachofuata?

| Nataka…             | Nenda kwa…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Kuanza Somo la 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Kufanya kazi nje ya mtandao | [`setup-local.md`](02-setup-local.md)                                   |
| Kuanzisha Mtoa Huduma wa LLM | [`providers.md`](03-providers.md)                                        |
| Kukutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Kutatua Tatizo

| Dalili                                   | Suluhisho                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Ujenzi wa kontena umekwama > dakika 10   | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal haikuunganishwa; bonyeza **+** ➜ *bash*                |
| `401 Unauthorized` kutoka OpenAI          | Funguo ya `OPENAI_API_KEY` si sahihi / imeisha muda             |
| VS Code inaonyesha “Dev container mounting…” | Refresh tab ya kivinjari—Codespaces wakati mwingine hupoteza muunganisho |
| Kernel ya Notebook haipo                  | Menu ya Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Mfumo wa Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili `.env`**: Fungua faili `.env` katika mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mstari ufuatao kwenye faili, ukibadilisha `your_github_token_here` na tokeni yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funga mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Ikiwa bado hujasakinisha, utahitaji kusakinisha kifurushi cha `python-dotenv` ili kupakia vigezo vya mazingira kutoka faili `.env` kwenye programu yako ya Python. Unaweza kusakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira katika Script yako ya Python**: Katika script yako ya Python, tumia kifurushi cha `python-dotenv` kupakia vigezo vya mazingira kutoka faili `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hayo tu! Umefanikiwa kuunda faili `.env`, kuongeza tokeni yako ya GitHub, na kuipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha Lokali kwenye Kompyuta Yako

Ili kuendesha msimbo lokali kwenye kompyuta yako, utahitaji kuwa na toleo fulani la [Python iliyosakinishwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha kutumia repo, unahitaji kuiklon:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Mara baada ya kila kitu kuangaliwa, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kisakinishi chepesi cha kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na vifurushi vichache.
Conda yenyewe ni msimamizi wa vifurushi, inayofanya iwe rahisi kuanzisha na kubadilisha kati ya [**mazingira ya virtual ya Python**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi. Pia inasaidia kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

Unaweza kufuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ili kuisakinisha.

Kwa Miniconda iliyosakinishwa, unahitaji kuklon [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ikiwa bado hujaklon).

Kisha, unahitaji kuunda mazingira ya virtual. Ili kufanya hivyo na Conda, endelea na unda faili mpya ya mazingira (_environment.yml_). Ikiwa unafuata kwa kutumia Codespaces, unda hii ndani ya saraka ya `.devcontainer`, hivyo `.devcontainer/environment.yml`.

Endelea na jaza faili yako ya mazingira na kipande cha msimbo hapa chini:

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

Faili ya mazingira inaelezea utegemezi tunaohitaji. `<environment-name>` inarejelea jina unalotaka kutumia kwa mazingira yako ya Conda, na `<python-version>` ni toleo la Python unalotaka kutumia, kwa mfano, `3` ni toleo kuu la Python la hivi karibuni.

Baada ya hayo, unaweza kuendelea na kuunda mazingira yako ya Conda kwa kuendesha amri hapa chini kwenye mstari wa amri/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rejelea [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa unakutana na matatizo.

### Kutumia Visual Studio Code na kiendelezi cha Python

Tunapendekeza kutumia mhariri wa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) na [kiendelezi cha Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kilichosakinishwa kwa kozi hii. Hii, hata hivyo, ni pendekezo tu na si hitaji la lazima.

> **Kumbuka**: Kwa kufungua repo ya kozi katika VS Code, una chaguo la kuanzisha mradi ndani ya kontena. Hii ni kwa sababu ya [saraka maalum `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) inayopatikana ndani ya repo ya kozi. Zaidi kuhusu hili baadaye.

> **Kumbuka**: Mara unapoklon na kufungua saraka katika VS Code, itapendekeza moja kwa moja usakinishe kiendelezi cha Python.

> **Kumbuka**: Ikiwa VS Code inapendekeza ufungue repo katika kontena, kataa ombi hili ili kutumia toleo la Python lililosakinishwa lokali.

### Kutumia Jupyter kwenye Kivinjari

Unaweza pia kufanya kazi kwenye mradi kwa kutumia [mazingira ya Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja ndani ya kivinjari chako. Jupyter ya kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) hutoa mazingira mazuri ya maendeleo yenye vipengele kama vile kukamilisha kiotomatiki, kuonyesha msimbo, nk.

Ili kuanzisha Jupyter lokali, nenda kwenye terminal/mstari wa amri, elekea kwenye saraka ya kozi, na tekeleza:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha Jupyter na URL ya kuifikia itaonyeshwa ndani ya dirisha la mstari wa amri.

Mara unapofikia URL, unapaswa kuona muhtasari wa kozi na uweze kuvinjari faili yoyote ya `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

### Kuendesha ndani ya kontena

Njia mbadala ya kuanzisha kila kitu kwenye kompyuta yako au Codespace ni kutumia [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Saraka maalum `.devcontainer` ndani ya repo ya kozi inafanya iwezekane kwa VS Code kuanzisha mradi ndani ya kontena. Nje ya Codespaces, hii itahitaji usakinishaji wa Docker, na kwa kweli, inahusisha kazi kidogo, kwa hivyo tunapendekeza hii tu kwa wale wenye uzoefu wa kufanya kazi na kontena.

Njia bora ya kuweka funguo zako za API salama unapotumia GitHub Codespaces ni kwa kutumia Siri za Codespace. Tafadhali fuata [mwongozo wa usimamizi wa siri za Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ili kujifunza zaidi kuhusu hili.

## Masomo na Mahitaji ya Kiufundi

Kozi ina masomo 6 ya dhana na masomo 6 ya msimbo.

Kwa masomo ya msimbo, tunatumia Huduma ya Azure OpenAI. Utahitaji ufikiaji wa Huduma ya Azure OpenAI na funguo ya API ili kuendesha msimbo huu. Unaweza kuomba kupata ufikiaji kwa [kukamilisha ombi hili](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Wakati unasubiri ombi lako kushughulikiwa, kila somo la msimbo pia linajumuisha faili ya `README.md` ambapo unaweza kuona msimbo na matokeo.

## Kutumia Huduma ya Azure OpenAI kwa mara ya kwanza

Ikiwa ni mara yako ya kwanza kufanya kazi na Huduma ya Azure OpenAI, tafadhali fuata mwongozo wa jinsi ya [kuunda na kupeleka rasilimali ya Huduma ya Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia API ya OpenAI kwa mara ya kwanza

Ikiwa ni mara yako ya kwanza kufanya kazi na API ya OpenAI, tafadhali fuata mwongozo wa jinsi ya [kuunda na kutumia Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kukutana na Wanafunzi Wengine

Tumetengeneza njia katika [seva rasmi ya Discord ya Jamii ya AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kukutana na wanafunzi wengine. Hii ni njia nzuri ya kuunda mtandao na wajasiriamali wengine wenye mawazo sawa, wajenzi, wanafunzi, na yeyote anayetaka kuboresha ujuzi wake katika Generative AI.

[![Jiunge na njia ya discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwa kwenye seva hii ya Discord kusaidia wanafunzi wowote.

## Kuchangia

Kozi hii ni mpango wa chanzo huria. Ikiwa unaona maeneo ya kuboresha au masuala, tafadhali unda [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au weka [tatizo la GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itakuwa ikifuatilia michango yote. Kuchangia kwenye chanzo huria ni njia nzuri ya kujenga kazi yako katika Generative AI.

Michango mingi inahitaji ukubali Mkataba wa Leseni ya Mchangiaji (CLA) unaotangaza kuwa una haki ya na kwa kweli unatoa haki kwetu kutumia mchango wako. Kwa maelezo, tembelea [tovuti ya CLA, Mkataba wa Leseni ya Mchangiaji](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: unapotafsiri maandishi katika repo hii, tafadhali hakikisha kuwa hutumii tafsiri ya mashine. Tutathibitisha tafsiri kupitia jamii, kwa hivyo tafadhali jitolee tu kwa tafsiri katika lugha ambazo unazifahamu vizuri.

Unapowasilisha ombi la kuvuta, CLA-bot itatambua moja kwa moja ikiwa unahitaji kutoa CLA na kupamba PR ipasavyo (mfano, lebo, maoni). Fuata tu maagizo yaliyotolewa na bot. Utahitaji kufanya hili mara moja tu katika repo zote zinazotumia CLA yetu.

Mradi huu umechukua [Kanuni ya Maadili ya Chanzo Huria ya Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali Yanayoulizwa Mara kwa Mara ya Kanuni ya Maadili au wasiliana na [Barua pepe ya opencode](opencode@microsoft.com) kwa maswali au maoni ya ziada.

## Twende Tukaanze
Sasa kwa kuwa umekamilisha hatua zinazohitajika kumaliza kozi hii, hebu tuanze kwa kupata [utambulisho wa Generative AI na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.