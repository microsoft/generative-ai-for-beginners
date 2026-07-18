# Kuanzia na kozi hii

Tunafurahi sana kwa wewe kuanza kozi hii na kuona ni nini utakachovutiwa kujenga kwa kutumia AI ya Kizazi!

Ili kuhakikisha mafanikio yako, ukurasa huu unaelezea hatua za usanidi, mahitaji ya kiufundi, na wapi pa kupata msaada ikiwa utahitaji.

## Hatua za Usanidi

Ili kuanza kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Toa Nakala ya Repo hii

[Toa nakala ya repo hii yote](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Unaweza pia [kutoa nyota (🌟) kwa repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na repos zinazohusiana kwa urahisi zaidi.

### 2. Unda eneo la codespace

Ili kuepuka matatizo yoyote ya utegemezi unapotumia msimbo, tunapendekeza kuendesha kozi hii kwenye [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Katika nakala yako: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sw/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Ongeza siri

1. ⚙️ Ikoni ya gia -> Command Pallete-> Codespaces : Manage user secret -> Ongeza siri mpya.
2. Jina OPENAI_API_KEY, bandika ufunguo wako, Hifadhi.

### 3. Nini kingine?

| Nataka…           | Nenda kwa…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Anza Somo la 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Fanya kazi bila mtandao | [`setup-local.md`](02-setup-local.md)                                   |
| Sanidi Mtoa LLM      | [`providers.md`](03-providers.md)                                        |
| Kutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Utatuzi wa matatizo


| Dalili                                   | Suluhisho                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Ujenzi wa kontena unazidi dakika 10         | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal haikuwa imeshikamana; bonyeza **+** ➜ *bash*                    |
| `401 Unauthorized` kutoka OpenAI            | `OPENAI_API_KEY` si sahihi / imeisha muda wa uhalali                                |
| VS Code inaonyesha “Dev container mounting…”   | Futa ukurasa wa kivinjari—Codespaces wakati mwingine hupoteza muunganisho   |
| Kernel ya daftari la kumbukumbu haipo  | Menyu ya daftari ➜ **Kernel ▸ Chagua Kernel ▸ Python 3**           |

   Mfumo wa Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili la `.env`**: Fungua faili `.env` katika mhariri wa maandishi (kama vile VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mistari ifuatayo kwa faili, ukibadilisha vidondoo na anwani halisi na ufunguo wa Microsoft Foundry Models (angalia [`providers.md`](03-providers.md) jinsi ya kupata hizi):

   > **Kumbuka:** Microsoft Models ya GitHub (na kigezo chake cha `GITHUB_TOKEN`) kitafutwa mwisho wa Julai 2026. Tumia badala yake [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na fungua mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Ikiwa bado hujafanya hivyo, utahitaji kusakinisha kifurushi cha `python-dotenv` ili kupakia vigezo vya mazingira kutoka faili `.env` katika programu yako ya Python. Unaweza kusakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira katika Skripti Yako ya Python**: Katika skripti yako ya Python, tumia kifurushi cha `python-dotenv` kupakia vigezo vya mazingira kutoka faili `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Pakia vigezo vya mazingira kutoka kwenye faili .env
   load_dotenv()

   # Pata vigezo vya Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Hiyo ni yote! Umeunda kwa mafanikio faili `.env`, umeongeza vibali vyako vya Microsoft Foundry Models, na kuviingiza katika programu yako ya Python.

## Jinsi ya kuendesha karibu na kompyuta yako

Ili kuendesha msimbo karibu na kompyuta yako, unahitaji kuwa na toleo fulani la [Python limesanidishwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha ili kutumia hifadhidata, unahitaji kuiyakili (clone):

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Baada ya kuipata kila kitu, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni mtoaji mwepesi wa kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, na vifurushi kadhaa.
Conda yenyewe ni msimamizi wa vifurushi, ambao hufanya iwe rahisi kusanidi na kubadilisha kati ya [mazingira ya kuigwa ya Python](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi. Pia inasaidia kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

Unaweza kufuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kuziweka.

Ukiwa na Miniconda imesakinishwa, unahitaji kuandika hifadhidata (repository) (kama bado hujafanya hivyo)

Kisha, unahitaji kuunda mazingira ya kuigwa (virtual environment). Ili kufanya hivi na Conda, endelea na tengeneza faili mpya ya mazingira (_environment.yml_). Ikiwa unafuata kwa kutumia Codespaces, tengeneza hii ndani ya saraka `.devcontainer`, yaani `.devcontainer/environment.yml`.

Endelea na jaza faili ya mazingira na kipande kilichopo hapa chini:

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

Ikiwa unapata hitilafu unapotumia conda unaweza kusakinisha maktaba za Microsoft AI kwa mkono kwa kutumia amri ifuatayo kwenye terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili la mazingira linaelezea utegemezi tunaohitaji. `<environment-name>` linarejelea jina unalotaka kutumia kwa mazingira yako ya Conda, na `<python-version>` ni toleo la Python unalotaka kutumia, kwa mfano, `3` ni toleo kubwa la hivi karibuni la Python.

Baada ya hayo, unaweza kuendelea na kuunda mazingira yako ya Conda kwa kuendesha amri zifuatazo katika mstari wa amri/terminal yako

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Njia ndogo ya .devcontainer inatumika tu kwa usanidi wa Codespace
conda activate ai4beg
```

Rejea kwenye [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa utakumbana na matatizo yoyote.

### Kutumia Visual Studio Code na kiendelezi cha msaada wa Python

Tunapendekeza kutumia mhariri wa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) pamoja na [kiendelezi cha msaada wa Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kilichosakinishwa kwa kozi hii. Hii ni pendekezo zaidi kuliko sharti la lazima.

> **Kumbuka**: Kwa kufungua hifadhidata ya kozi kwenye VS Code, una chaguo la kuanzisha mradi ndani ya kontena. Hii ni kutokana na saraka maalum ya [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) iliyomo katika hifadhidata ya kozi. Tutaendelea kufafanua baadaye.

> **Kumbuka**: Mara tu unapoyakili na kufungua saraka kwenye VS Code, itapendekeza kiotomatiki usakinishe kiendelezi cha msaada wa Python.

> **Kumbuka**: Ikiwa VS Code itapendekeza ufungue tena hifadhidata ndani ya kontena, kataa ombi hili ili utumie toleo la Python lililosakinishwa karibu.

### Kutumia Jupyter kwenye Kivinjari

Pia unaweza kufanya kazi kwenye mradi kwa kutumia [mazingira ya Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja katika kivinjari chako. Haya ni pamoja na Jupyter ya kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ambayo hutoa mazingira mazuri ya maendeleo yenye vipengele kama kukamilisha kiotomatiki, kuangazia msimbo, n.k.

Kuanzia Jupyter mahali hapa karibu, nenda kwenye terminal/mstari wa amri, elekea sarakani ya kozi, na tekeleza:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha mfano wa Jupyter na URL ya kuifikia itaonyeshwa ndani ya dirisha la mstari wa amri.

Mara unapoingia kwenye URL, unapaswa kuona mpangilio wa kozi na uweze kuvinjari faili zozote za `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

### Kuendesha ndani ya kontena

Mbadala wa kusanidi kila kitu kwenye kompyuta yako au Codespace ni kutumia [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Saka la maalum la `.devcontainer` ndani ya hifadhidata ya kozi linawezesha VS Code kusanidi mradi ndani ya kontena. Nje ya Codespaces, hii itahitaji usakinishaji wa Docker, na waziwazi, huchukua kazi kidogo, hivyo tunapendekeza hii kwa wale wenye uzoefu na kontena.

Njia mojawapo bora ya kuweka funguo zako za API salama unapotumia GitHub Codespaces ni kwa kutumia Siri za Codespace. Tafadhali fuata mwongozo wa [usimamizi wa siri za Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kujifunza zaidi.


## Masomo na Mahitaji ya Kiufundi

Kozi ina masomo ya "Jifunze" yanayoelezea dhana za AI ya Kizazi na masomo ya "Jenga" yenye mifano ya msimbo wa vitendo kwa **Python** na **TypeScript** inapowezekana.

Kwa masomo ya uandishi wa msimbo, tunatumia Azure OpenAI katika Microsoft Foundry. Utahitaji usajili wa Azure na ufunguo wa API. Ufikiaji ni wa wazi - hakuna maombi yanayohitajika - hivyo unaweza [kuunda rasilimali ya Microsoft Foundry na kupeleka mfano](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) kupata anwani zako na ufunguo.

Kila somo la uandishi wa msimbo pia lina faili la `README.md` ambapo unaweza kuona msimbo na matokeo bila kuendesha chochote.

## Kutumia Huduma ya Azure OpenAI kwa mara ya kwanza

Ikiwa hii ni mara yako ya kwanza kufanya kazi na huduma ya Azure OpenAI, tafadhali fuata mwongozo huu jinsi ya [kuunda na kupeleka rasilimali ya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia API ya OpenAI kwa mara ya kwanza

Ikiwa hii ni mara yako ya kwanza kufanya kazi na API ya OpenAI, tafadhali fuata mwongozo jinsi ya [kuunda na kutumia Kiolesura.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kutana na Wanafunzi Wengine

Tumeunda vituo kwenye seva rasmi ya [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kukutana na wanafunzi wengine. Hii ni njia nzuri ya kuungana na wajasiriamali wengine wenye fikra moja, wajenzi, wanafunzi, na mtu yeyote anayetamani kujifunza zaidi AI ya Kizazi.

[![Jiunge na kituo cha discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakua kwenye server hii ya Discord kusaidia wanafunzi wote.

## Changia

Kozi hii ni juhudi ya chanzo fungani. Ikiwa unaona maeneo ya kuboresha au matatizo, tafadhali tengeneza [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au andika [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itafuatilia michango yote. Kuchangia chanzo hufungua fursa ya ajira katika AI ya Kizazi.

Michango mingi inahitaji kukubali Mkataba wa Leseni ya Mchangiaji (CLA) unaosema kuwa una haki na kwa kweli unatuwezesha kutumia mchango wako. Kwa maelezo, tembelea [CLA, tovuti ya Mkataba wa Leseni ya Mchangiaji](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: unapotafsiri maandishi katika repo hii, tafadhali hakikisha hauitumi tafsiri ya mashine. Tutathibitisha tafsiri kupitia jamii, hivyo tafadhali jitolee tu kutafsiri kwa lugha unazozifahamu vizuri.


Unapowasilisha ombi la kuvuta, CLA-bot itabaini moja kwa moja kama unahitaji kutoa CLA na kupamba PR ipasavyo (mfano, alama, maoni). Fuata tu maagizo yaliyotolewa na bot. Utahitaji kufanya hivi mara moja tu katika maktaba zote zinazo tumia CLA yetu.

Mradi huu umekubali [Kanuni za Maadili za Chanzo Huria za Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali Yanayoulizwa Mara kwa Mara juu ya Kanuni za Maadili au wasiliana na [Barua pepe opencode](opencode@microsoft.com) kwa maswali au maoni zaidi.

## Hebu Tuanze

Sasa baada ya kumaliza hatua muhimu za kukamilisha kozi hii, hebu tuanze kwa kupata [utambulisho wa AI Mwenyekiti na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->