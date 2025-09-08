<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:39:25+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Kuanza na kozi hii

Tunafurahia sana kuona unaanza kozi hii na kuona utapata msukumo wa kujenga nini kwa kutumia AI Inayozalisha!

Ili kuhakikisha unafanikiwa, ukurasa huu unaelezea hatua za maandalizi, mahitaji ya kiufundi, na mahali pa kupata msaada ukihitaji.

## Hatua za Maandalizi

Ili kuanza na kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Fork Repo hii

[Fork repo hii yote](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Unaweza pia [kuweka nyota (🌟) kwenye repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili iwe rahisi kuipata pamoja na repo zinazohusiana.

### 2. Tengeneza codespace

Ili kuepuka matatizo ya utegemezi wakati wa kuendesha msimbo, tunapendekeza uendeshe kozi hii kwenye [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Kwenye fork yako: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Ongeza siri

1. ⚙️ Alama ya gia -> Command Pallete-> Codespaces : Manage user secret -> Ongeza siri mpya.
2. Andika OPENAI_API_KEY, bandika ufunguo wako, Hifadhi.

### 3.  Nini kinafuata?

| Nataka…              | Nenda kwenye…                                                           |
|----------------------|-------------------------------------------------------------------------|
| Anza Somo la 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Fanya kazi bila mtandao | [`setup-local.md`](02-setup-local.md)                                |
| Sanidi Mtoa Huduma wa LLM | [`providers.md`](providers.md)                                     |
| Kutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Kutatua Matatizo

| Dalili                                    | Suluhisho                                                        |
|-------------------------------------------|------------------------------------------------------------------|
| Ujenzi wa kontena umekwama > dakika 10    | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Terminal haijaunganishwa; bonyeza **+** ➜ *bash*                 |
| `401 Unauthorized` kutoka OpenAI          | `OPENAI_API_KEY` si sahihi / imeisha muda                       |
| VS Code inaonyesha “Dev container mounting…” | Refresh tab ya kivinjari—Codespaces wakati mwingine hupoteza muunganisho |
| Kernel ya Notebook haipo                  | Menu ya Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Mfumo wa Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili la `.env`**: Fungua faili la `.env` kwenye mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mstari ufuatao kwenye faili, ukibadilisha `your_github_token_here` na tokeni yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funga mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Ikiwa bado hujasakinisha, utahitaji kusakinisha kifurushi cha `python-dotenv` ili kupakia vigezo vya mazingira kutoka kwenye faili la `.env` kwenye programu yako ya Python. Unaweza kusakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira kwenye Script yako ya Python**: Kwenye script yako ya Python, tumia kifurushi cha `python-dotenv` kupakia vigezo vya mazingira kutoka kwenye faili la `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Umefanikiwa! Umetengeneza faili la `.env`, umeongeza tokeni yako ya GitHub, na umeipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha kwenye Kompyuta yako

Ili kuendesha msimbo kwenye kompyuta yako, utahitaji kuwa na toleo fulani la [Python limewekwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha kutumia repo, unahitaji kuiklon:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ukishamaliza kila kitu, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kisakinishi chepesi kwa ajili ya kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na baadhi ya vifurushi.
Conda yenyewe ni msimamizi wa vifurushi, inayorahisisha kuanzisha na kubadilisha kati ya [**mazingira pepe**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ya Python na vifurushi. Pia inasaidia kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

Unaweza kufuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ili kuisakinisha.

Baada ya kusakinisha Miniconda, unahitaji kuklon [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kama bado hujafanya hivyo)

Kisha, unahitaji kuunda mazingira pepe. Ili kufanya hivi kwa kutumia Conda, tengeneza faili jipya la mazingira (_environment.yml_). Kama unafuata kwa kutumia Codespaces, tengeneza hili ndani ya folda ya `.devcontainer`, hivyo basi `.devcontainer/environment.yml`.

Jaza faili lako la mazingira na kipande hiki hapa chini:

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

Kama utapata makosa ukitumia conda unaweza kusakinisha Microsoft AI Libraries kwa mkono kwa kutumia amri hii kwenye terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili la mazingira linaorodhesha utegemezi tunaohitaji. `<environment-name>` ni jina unalotaka kutumia kwa mazingira yako ya Conda, na `<python-version>` ni toleo la Python unalotaka kutumia, kwa mfano, `3` ni toleo kuu la hivi karibuni la Python.

Baada ya hapo, unaweza kuunda mazingira yako ya Conda kwa kuendesha amri hizi kwenye command line/terminal yako

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tazama [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kama utapata matatizo yoyote.

### Kutumia Visual Studio Code na kiendelezi cha Python

Tunapendekeza utumie [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) pamoja na [kiendelezi cha Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kwa ajili ya kozi hii. Hata hivyo, hii ni pendekezo tu na si lazima.

> **Note**: Ukifungua repo ya kozi kwenye VS Code, utakuwa na chaguo la kusanidi mradi ndani ya kontena. Hii ni kwa sababu ya [folda maalum ya `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) iliyopo kwenye repo ya kozi. Zaidi kuhusu hili baadaye.

> **Note**: Mara tu ukiklon na kufungua folda kwenye VS Code, itapendekeza usakinishe kiendelezi cha Python.

> **Note**: Kama VS Code itapendekeza ufungue repo kwenye kontena, kataa ombi hili ili utumie toleo la Python ulilosakinisha kwenye kompyuta yako.

### Kutumia Jupyter kwenye Kivinjari

Unaweza pia kufanya kazi na mradi huu kwa kutumia [mazingira ya Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja kwenye kivinjari chako. Jupyter ya kawaida na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) zote zinatoa mazingira mazuri ya maendeleo yenye vipengele kama vile kukamilisha msimbo kiotomatiki, kuangazia msimbo, n.k.

Ili kuanzisha Jupyter kwenye kompyuta yako, nenda kwenye terminal/command line, elekea kwenye folda ya kozi, na endesha:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha Jupyter na URL ya kuifikia itaonyeshwa kwenye dirisha la command line.

Ukishaingia kwenye URL, utaona muhtasari wa kozi na utaweza kufungua faili lolote la `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

### Kuendesha kwenye kontena

Njia mbadala ya kusanidi kila kitu kwenye kompyuta yako au Codespace ni kutumia [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folda maalum ya `.devcontainer` ndani ya repo ya kozi inafanya iwezekane kwa VS Code kusanidi mradi ndani ya kontena. Nje ya Codespaces, hii itahitaji usakinishaji wa Docker, na kwa kweli, inahitaji uzoefu kidogo, hivyo tunapendekeza hii kwa wale tu wenye uzoefu wa kufanya kazi na makontena.

Njia mojawapo bora ya kuweka funguo zako za API salama unapotumia GitHub Codespaces ni kutumia Codespace Secrets. Tafadhali fuata [mwongozo wa usimamizi wa siri za Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kujifunza zaidi kuhusu hili.

## Masomo na Mahitaji ya Kiufundi

Kozi ina masomo 6 ya dhana na masomo 6 ya msimbo.

Kwa masomo ya msimbo, tunatumia Azure OpenAI Service. Utahitaji kupata huduma ya Azure OpenAI na API key ili kuendesha msimbo huu. Unaweza kutuma maombi ya kupata huduma kwa [kujaza fomu hii](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Wakati unasubiri ombi lako lichakatwe, kila somo la msimbo pia lina faili la `README.md` ambapo unaweza kuona msimbo na matokeo.

## Kutumia Azure OpenAI Service kwa mara ya kwanza

Kama ni mara yako ya kwanza kufanya kazi na Azure OpenAI service, tafadhali fuata mwongozo huu wa jinsi ya [kuunda na kupeleka rasilimali ya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia OpenAI API kwa mara ya kwanza

Kama ni mara yako ya kwanza kutumia OpenAI API, tafadhali fuata mwongozo wa jinsi ya [kuunda na kutumia Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kutana na Wanafunzi Wengine

Tumeunda chaneli kwenye [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) rasmi kwa ajili ya kukutana na wanafunzi wengine. Hii ni njia nzuri ya kujenga mtandao na wajasiriamali, wabunifu, wanafunzi, na yeyote anayependa kukuza ujuzi wake kwenye AI Inayozalisha.

[![Jiunge na chaneli ya discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwepo kwenye Discord hii kusaidia wanafunzi wowote.

## Changia

Kozi hii ni mradi wa wazi. Ukiona maeneo ya kuboresha au matatizo, tafadhali tengeneza [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au andika [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itafuatilia michango yote. Kuchangia kwenye chanzo huria ni njia nzuri ya kujenga taaluma yako kwenye AI Inayozalisha.

Michango mingi inahitaji ukubali Mkataba wa Leseni ya Mchangiaji (CLA) unaothibitisha kuwa una haki na kweli unaturuhusu kutumia mchango wako. Kwa maelezo zaidi, tembelea [tovuti ya CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: unapofasiri maandishi kwenye repo hii, tafadhali hakikisha hutumii tafsiri ya mashine. Tutathibitisha tafsiri kupitia jamii, hivyo tafadhali jitolee tu kwa lugha unazozimudu vizuri.

Unapotuma pull request, CLA-bot itatambua kiotomatiki kama unahitaji kutoa CLA na itaweka alama kwenye PR ipasavyo (mfano, lebo, maoni). Fuata tu maelekezo yatakayotolewa na bot. Utahitaji kufanya hivi mara moja tu kwenye repo zote zinazotumia CLA yetu.

Mradi huu umechukua [Kanuni ya Maadili ya Chanzo Huria ya Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali ya Kanuni ya Maadili au wasiliana na [Email opencode](opencode@microsoft.com) kwa maswali au maoni zaidi.

## Twende Kazi
Sasa kwa kuwa umekamilisha hatua zinazohitajika kumaliza kozi hii, hebu tuanze kwa kupata [utambulisho wa AI Inayotengeneza na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.