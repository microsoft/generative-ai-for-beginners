# Kuanza na kozi hii

Tuna furaha sana kwa wewe kuanza kozi hii na kuona unachovutiwa kujenga kwa kutumia AI ya Kizazi!

Ili kuhakikisha mafanikio yako, ukurasa huu unaelezea hatua za usanidi, mahitaji ya kiufundi, na wapi pa kupata msaada ikiwa utahitaji.

## Hatua za Usanidi

Ili kuanza kuchukua kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Fanya Fork ya Repo hii

[Fanya fork ya repo nzima hii](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Pia unaweza [kutoa nyota (🌟) kwenye repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na repos nyingine zinazohusiana kwa urahisi zaidi.

### 2. Unda codespace

Ili kuepuka matatizo yoyote ya utegemezi wakati wa kuendesha msimbo, tunapendekeza kuendesha kozi hii kwenye [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Kwenye fork yako: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sw/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Ongeza siri

1. ⚙️ Ikoni ya gia -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Jina OPENAI_API_KEY, weka ufunguo wako, Hifadhi.

### 3. Nini kinafuata?

| Nataka…          | Nenda kwa…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Anza Somo la 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Fanya kazi bila mtandao        | [`setup-local.md`](02-setup-local.md)                                   |
| Sanidi Mtoa Huduma wa LLM | [`providers.md`](03-providers.md)                                        |
| Kutana na washiriki wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Kutatua Shida


| Dalili                                   | Suluhisho                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Ujenzi wa kontena umezuilika > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal haikuambatanishwa; bonyeza **+** ➜ *bash*                    |
| `401 Unauthorized` kutoka OpenAI            | `OPENAI_API_KEY` si sahihi / imeharibika                                |
| VS Code inaonyesha “Dev container mounting…”   | Reload kipengee cha kivinjari—Codespaces mara nyingine hupoteza muunganisho   |
| Kernel ya daftari la maelezo haipo                   | Menyu ya daftari ➜ **Kernel ▸ Chagua Kernel ▸ Python 3**           |

   Mifumo ya Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili la `.env`**: Fungua faili la `.env` kwa mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mistari ifuatayo kwenye faili, ukibadilisha sehemu za mahali na anuani halisi na ufunguo wa Microsoft Foundry Models (tazama [`providers.md`](03-providers.md) jinsi ya kuzipata):

   > **Kumbuka:** GitHub Models (na variable yake `GITHUB_TOKEN`) itasitishwa mwishoni mwa Julai 2026. Badili kutumia [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) badala yake.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funika mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Kama bado hujaukiweka, utahitaji kusakinisha kifurushi cha `python-dotenv` ili kupakia maadili ya mazingira kutoka faili la `.env` kwenye programu yako ya Python. Unaweza kusakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Mabadiliko ya Mazingira kwenye Script yako ya Python**: Katika script yako ya Python, tumia kifurushi cha `python-dotenv` kupakia mabadiliko ya mazingira kutoka faili la `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Pakia vigezo vya mazingira kutoka kwa faili la .env
   load_dotenv()

   # Pata vigezo vya Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Hiyo ni yote! Umeunda faili la `.env` kwa mafanikio, ukaongeza huduma za Microsoft Foundry Models, na kuzipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha kwa kompyuta yako kwa ndani

Kuendesha msimbo kwa kompyuta yako binafsi, unatakiwa kuwa na toleo la [Python limewekwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha ili kutumia repozitori, unahitaji kuikokota (clone):

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Mara baada ya kuwa na kila kitu, unaweza kuanza kazi!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kifurushi nyepesi cha kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na vifurushi vingine vichache.
Conda yenyewe ni msimamizi wa vifurushi, ambayo hurahisisha usanidi na kubadilisha kati ya [mazingira ya kweli ya Python](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi. Pia inafaa katika kusakinisha vifurushi ambavyo haviwezi kupatikana kwa njia ya `pip`.

Unaweza kufuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kuiseti.

Ukishaweka Miniconda, unahitaji kukokota [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kama bado hujafanya hivyo)

Kisha unahitaji kuunda mazingira ya kidijitali. Kufanya hivi na Conda, unda faili jipya la mazingira (_environment.yml_). Ukifuata kutumia Codespaces, tengeneza hili ndani ya saraka `.devcontainer`, yaani `.devcontainer/environment.yml`.

Endelea na jaza faili la mazingira kwa kipande hiki kilicho chini:

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

Ikiwa unakumbana na makosa ukitumia conda unaweza kusakinisha maktaba za Microsoft AI kitaalam ukitumia amri ifuatayo kwenye terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili la mazingira linaelezea utegemezi tunazohitaji. `<environment-name>` inarejelea jina unalotaka kutumia kwa mazingira yako ya Conda, na `<python-version>` ni toleo la Python unalotaka kutumia, kwa mfano, `3` ni toleo kubwa la hivi karibuni la Python.

Ukimaliza hapo, unaweza kuunda mazingira yako ya Conda kwa kuendesha amri zilizo hapa chini kwenye mstari wa amri/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Njia ndogo ya .devcontainer inatumika kwa mipangilio ya Codespace pekee
conda activate ai4beg
```

Rejelea [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa unakumbana na matatizo yoyote.

### Kutumia Visual Studio Code na kiendelezi cha msaada wa Python

Tunapendekeza utumie mhariri [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) pamoja na [kiendelezi cha msaada wa Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kilichosakinishwa kwa kozi hii. Hii ni mapendekezo zaidi kuliko sharti la lazima

> **Kumbuka**: Ukiifungua repo ya kozi hii kwenye VS Code, una chaguo la kusanidi mradi ndani ya kontena. Hii ni kwa sababu ya saraka maalum ya [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) inayopatikana ndani ya repo ya kozi. Tutaenda zaidi kuhusu hili baadaye.

> **Kumbuka**: Mara tu unapokokota na kufungua saraka kwenye VS Code, moja kwa moja itapendekeza usakinishe kiendelezi cha msaada wa Python.

> **Kumbuka**: Ikiwa VS Code inapendekeza ufungue tena repo ndani ya kontena, kataa ombi hili ili utumie toleo la Python lililosakinishwa mahali hapa.

### Kutumia Jupyter katika Kivinjari

Pia unaweza kufanya kazi kwenye mradi kutumia [mazingira ya Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja ndani ya kivinjari chako. Hii ni pamoja na Jupyter ya kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ambazo hutoa mazingira mazuri ya maendeleo pamoja na sifa kama kukamilisha moja kwa moja, kuangaza msimbo, n.k.

Kuanzisha Jupyter kwa ndani, nenda kwenye terminal/mstari wa amri, elekea kwenye saraka ya kozi, kisha endesha:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha toleo la Jupyter na URL ya kuifikia itaonyeshwa kwenye dirisha la mstari wa amri.

Ukipata URL hiyo, unapaswa kuona muhtasari wa kozi na kuweza kuvinjari faili yoyote `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

### Kuendesha ndani ya kontena

Mbali na kuandaa kila kitu kwenye kompyuta yako au Codespace, unaweza pia kutumia [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Saraka maalum ya `.devcontainer` ndani ya repo ya kozi hufanya iwezekane VS Code kuandaa mradi ndani ya kontena. Nje ya Codespaces, hii itahitaji usakinishaji wa Docker, na ukweli ni kwamba, inahitaji kazi kidogo, hivyo tunapendekeza hii kwa wale tu wenye uzoefu wa kutumia makontena.

Moja ya njia bora za kuhifadhi usalama wa funguo zako za API unapotumia GitHub Codespaces ni kwa kutumia Codespace Secrets. Tafadhali fuata mwongozo wa [kusimamia siri za Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kujifunza zaidi.


## Masomo na Mahitaji ya Kiufundi

Kozi ina masomo 6 ya dhana na masomo 6 ya uandishi wa msimbo.

Kwa masomo ya uandishi wa msimbo, tunatumia Huduma ya Azure OpenAI. Utahitaji kupata huduma ya Azure OpenAI na ufunguo wa API kuendesha msimbo huu. Unaweza kuomba kupata huduma hiyo kwa [kukamilisha maombi haya](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Wakati unasubiri maombi yako kushughulikiwa, kila somo la uandishi pia lina faili la `README.md` ambapo unaweza kuona msimbo na matokeo.

## Kutumia Huduma ya Azure OpenAI kwa mara ya kwanza

Ikiwa hii ni mara yako ya kwanza kutumia huduma ya Azure OpenAI, tafadhali fuata mwongozo huu jinsi ya [kujenga na kuweka rasilimali ya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia OpenAI API kwa mara ya kwanza

Ikiwa hii ni mara yako ya kwanza kutumia OpenAI API, tafadhali fuata mwongozo wa jinsi ya [kuunda na kutumia Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kutana na Washiriki Wengine

Tumeunda njia mawasiliano katika seva yetu rasmi ya [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kukutana na washiriki wengine. Hii ni njia nzuri ya kuungana na wajasiriamali, wajenzi, wanafunzi, na mtu yeyote anayetafuta kufikia kiwango cha juu katika AI ya Kizazi.

[![Jiunge na chaneli ya discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwepo kwenye seva hii ya Discord kusaidia washiriki wote.

## Changia

Kozi hii ni juhudi ya chanzo huria. Ikiwa unaona sehemu za kuboresha au matatizo, tafadhali tengeneza [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au fungua tatizo kwenye [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itafuatilia michango yote. Kuchangia chanzo huria ni njia nzuri ya kujenga taaluma yako katika AI ya Kizazi.

Michango mingi inahitaji iweze kukubaliana na Mkataba wa Leseni ya Mchangiaji (CLA) unaosema kwamba una haki na kwa kweli unawapa haki za kutumia mchango wako. Kwa maelezo zaidi, tembelea [CLA, Tovuti ya Mkataba wa Leseni ya Mchangiaji](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: unapotafsiri maandishi kwenye repo hii, tafadhali hakikisha hautumii tafsiri ya mashine. Tutathibitisha tafsiri kupitia jumuiya, hivyo tafadhali jitolee kwa tafsiri tu katika lugha unazozifahamu vizuri.

Unapotuma ombi la pull request, bot wa CLA moja kwa moja atabaini kama unahitaji kutoa CLA na kuweka sifa sawa (mfano, lebo, maoni). Fuata tu maelekezo ya bot. Hii itabidi uifanye mara moja tu kwa repo zote zinazotumia CLA yetu.


Mradi huu umekubali [Msaada wa Maadili wa Chanzo Huria wa Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa taarifa zaidi soma Maswali Yanayoulizwa Mara kwa Mara ya Msaada wa Maadili au wasiliana na [Email opencode](opencode@microsoft.com) kwa maswali au maoni zaidi.

## Hebu Tuanze

Sasa baada ya kumaliza hatua zinazohitajika kukamilisha kozi hii, hebu tuanze kwa kupata [utambulisho wa AI Jeneratibu na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->