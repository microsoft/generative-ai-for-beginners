# Kuanzia na kozi hii

Tuna furaha kubwa kwa wewe kuanza kozi hii na kuona kile unachohamasishwa kujijengea kwa kutumia AI ya Uumbaji!

Ili kuhakikisha mafanikio yako, ukurasa huu unaelezea hatua za usanidi, mahitaji ya kiufundi, na mahali pa kupata msaada ikiwa unahitaji.

## Hatua za Usanidi

Ili kuanza kuchukua kozi hii, utahitaji kukamilisha hatua zifuatazo.

### 1. Fokea Repo hii

[Fokea repo yote hapa](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kwenye akaunti yako ya GitHub ili uweze kubadilisha msimbo wowote na kukamilisha changamoto. Unaweza pia [kuipa nyota (🌟) repo hii](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ili kuipata na repos zinazohusiana kwa urahisi zaidi.

### 2. Unda codespace

Kuepuka matatizo yoyote ya utegemezi unapotekeleza msimbo, tunapendekeza kuendesha kozi hii katika [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Katika fork yako: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sw/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Ongeza siri

1. ⚙️ Ikoni ya gia -> Command Pallete-> Codespaces : Manage user secret -> Ongeza siri mpya.
2. Jina OPENAI_API_KEY, weka funguo yako, Hifadhi.

### 3. Nini kinachofuata?

| Nataka…             | Nenda kwa…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Anza Somo la 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Fanya kazi bila mtandao | [`setup-local.md`](02-setup-local.md)                                   |
| Sanidi Mtoa huduma wa LLM | [`providers.md`](03-providers.md)                                        |
| Kutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Matatizo Yanayotokea


| Dalili                                    | Suluhisho                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Ujenzi wa kontena umefungwa kwa zaidi ya dakika 10 | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal haikujumuishwa; bonyeza **+** ➜ *bash*                 |
| `401 Unauthorized` kutoka OpenAI          | `OPENAI_API_KEY` si sahihi / imesitishwa                        |
| VS Code inaonyesha “Dev container mounting…” | Futa ukurasa wa kivinjari—Codespaces mara nyingine hupoteza muunganisho  |
| Kernel ya daftari la kumbukumbu haipo    | Menyu ya daftari ➜ **Kernel ▸ Chagua Kernel ▸ Python 3**         |

   Mfumo wa Unix:

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

5. **Sakinisha `python-dotenv`**: Ikiwa hujayasakinisha tayari, utahitaji kusakinisha kifurushi cha `python-dotenv` ili kupakia vigezo vya mazingira kutoka kwenye faili `.env` ndani ya programu yako ya Python. Unaweza kukisakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira katika Skripti Yako ya Python**: Katika skripti yako ya Python, tumia kifurushi cha `python-dotenv` kupakia vigezo vya mazingira kutoka faili `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Pakia mabadiliko ya mazingira kutoka kwenye faili la .env
   load_dotenv()

   # Pata thamani ya kigezo cha GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hilo nalo! Umeunda faili la `.env` vizuri, kuongeza tokeni yako ya GitHub, na kuipakia kwenye programu yako ya Python.

## Jinsi ya Kuendesha Kwenye Kompyuta Yako

Ili kuendesha msimbo kwenye kompyuta yako, utahitaji kuwa na toleo fulani la [Python lililosakinishwa](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kisha ili kutumia maktaba, unahitaji kuikokotoa:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ukishamaliza kuangalia yote, unaweza kuanza!

## Hatua za Hiari

### Kusakinisha Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kisakinishaji kidogo kwa kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na vifurushi vingine.  
Conda yenyewe ni msimamizi wa vifurushi, inayorahisisha kusanidi na kubadilisha kati ya [mazingira pepe ya Python](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na vifurushi tofauti. Pia ni msaada kwa kusakinisha vifurushi ambavyo havipatikani kupitia `pip`.

Unaweza kufuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kuweka.

Ukisakinisha Miniconda, unahitaji kukokotoa [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ikiwa bado hujafanya hivyo)

Inayofuata, lazima uunde mazingira pepe. Ili kufanya hivyo na Conda, endelea uunde faili jipya la mazingira (_environment.yml_). Ikiwa unafuata kupitia Codespaces, tengeneza hili ndani ya saraka `.devcontainer`, hivyo `.devcontainer/environment.yml`.

Endelea na ujaze faili lako la mazingira na kipande hapo chini:

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

Ikiwa unakumbana na makosa unapotumia conda unaweza kusakinisha maktaba za Microsoft AI kwa mkono kwa kutumia amri ifuatayo katika terminal.

```
conda install -c microsoft azure-ai-ml
```

Faili la mazingira linaeleza utegemezi tunazohitaji. `<environment-name>` linarejelea jina unalotaka kutumia kwa mazingira yako ya Conda, na `<python-version>` ni toleo la Python unalotaka kutumia, kwa mfano, `3` ni toleo kubwa zaidi la Python.

Baada ya hapo, unaweza endelea kuunda mazingira yako ya Conda kwa kuendesha amri zifuatazo kwenye mstari wa amri/terminal yako

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Njia ndogo ya .devcontainer inahusu usanidi wa Codespace pekee
conda activate ai4beg
```

Rejelea [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa utakutana na matatizo.

### Kutumia Visual Studio Code na kiendelezi cha msaada wa Python

Tunapendekeza kutumia mhariri wa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) na [kiendelezi cha msaada wa Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kilichosakinishwa kwa kozi hii. Hata hivyo, hili ni pendekezo zaidi na si sharti la lazima.

> **Kumbuka**: Kwa kufungua maktaba ya kozi katika VS Code, una chaguo la kuanzisha mradi ndani ya kontena. Hii ni kwa sababu ya saraka maalum ya [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) iliyopo ndani ya maktaba ya kozi. Zaidi kuhusu hili baadaye.

> **Kumbuka**: Mara tu unapochukua na kufungua saraka katika VS Code, itapendekeza moja kwa moja usakinishe kiendelezi cha msaada wa Python.

> **Kumbuka**: Ikiwa VS Code itapendekeza ufungue tena maktaba ndani ya kontena, jiruhusu ukanue ombi hili ili utumie toleo la Python lililosakinishwa eneo lako.

### Kutumia Jupyter katika Kivinjari

Unaweza pia kufanya kazi kwenye mradi kwa kutumia [mazingira ya Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) moja kwa moja kupitia kivinjari chako. Hata Jupyter klasik na [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) hutoa mazingira mazuri ya maendeleo yenye vipengele kama kukamilisha kiotomatiki, kuangazia msimbo, n.k.

Ili kuanzisha Jupyter kwa ndani, nenda kwenye terminal/mstari wa amri, elekea kwenye saraka ya kozi, na tekeleza:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha mfano wa Jupyter na URL ya kufikia itatambulika ndani ya dirisha la mstari wa amri.

Ukifikia URL, unapaswa kuona muhtasari wa kozi na uweze kuvinjari kwenye faili yoyote `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

### Kuendesha ndani ya kontena

Njia mbadala ya kusanidi kila kitu kwenye kompyuta yako au Codespace ni kutumia [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Saraka maalum ya `.devcontainer` ndani ya maktaba ya kozi inaimarisha VS Code kuweka mradi ndani ya kontena. Nje ya Codespaces, hii itahitaji usakinishaji wa Docker, na kwa ukweli, inahusisha kazi kidogo, hivyo tunapendekeza hii kwa wale tu wenye uzoefu wa kazi na kontena.

Njia moja bora ya kulinda funguo zako za API unapotumia GitHub Codespaces ni kwa kutumia Siri za Codespace. Tafadhali fuata mwongozo wa [kusimamia siri za Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ili kujifunza zaidi kuhusu hili.


## Masomo na Mahitaji ya Kiufundi

Kozi hii ina masomo 6 ya dhana na masomo 6 ya usimbaji wa msimbo.

Kwa masomo ya usimbaji wa msimbo, tunatumia Huduma ya Azure OpenAI. Utahitaji kupata huduma ya Azure OpenAI na funguo ya API kuendesha msimbo huu. Unaweza kuomba kupata huduma kwa [kukamilisha maombi haya](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Wakati unasubiri maombi yako yachakatwe, kila somo la usimbaji lina pia faili ya `README.md` ambapo unaweza kuona mstari wa msimbo na matokeo.

## Kutumia Huduma ya Azure OpenAI kwa mara ya kwanza

Ikiwa huu ni mara yako ya kwanza kufanya kazi na huduma ya Azure OpenAI, tafadhali fuata mwongozo huu juu ya jinsi ya [kuunda na kuweka rasilimali ya Huduma ya Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Kutumia API ya OpenAI kwa mara ya kwanza

Ikiwa huu ni mara yako ya kwanza kutumia API ya OpenAI, tafadhali fuata mwongozo wa jinsi ya [kuunda na kutumia Kiwango.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kutana na Wanafunzi Wengine

Tumeunda njia maalum katika seva rasmi yetu ya [Jamii ya AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kwa ajili ya kutana na wanafunzi wengine. Hii ni njia nzuri ya kutengeneza mtandao na wajasiriamali, wajenzi, wanafunzi, na yeyote anayetaka kupiga hatua katika AI ya Uumbaji.

[![Jiunge na chaneli ya discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Timu ya mradi pia itakuwa kwenye seva ya Discord kusaidia wanafunzi wote.

## Changia

Kozi hii ni jitihada ya chanzo huria. Ikiwa unaona sehemu za kuboresha au matatizo, tafadhali tengeneza [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) au andika [tatizo la GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Timu ya mradi itafuata michango yote. Kuchangia chanzo huria ni njia nzuri ya kujenga taaluma yako katika AI ya Uumbaji.

Mchango mwingi unahitaji kukubali Mkataba wa Leseni wa Mchango (CLA) unaosema kuwa una haki ya na kweli unatuwezesha kutumia mchango wako. Kwa maelezo zaidi, tembelea [Tovuti ya Mkataba wa Leseni wa Mchango, CLA](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Muhimu: unapokamilisha tafsiri ya maandishi katika repo hii, tafadhali hakikisha hutatumia tafsiri ya mashine. Tutathibitisha tafsiri kupitia jamii, hivyo tafadhali jitolee tu kwa tafsiri katika lugha unazozifahamu vizuri.

Unapowasilisha pull request, bot ya CLA itagundua moja kwa moja ikiwa unahitaji kutoa CLA na itapamba PR ipasavyo (mfano, lebo, maoni). Fuata tu maagizo yanayotolewa na bot. Hii utahitaji kufanya mara moja tu katika mabuku yote yanayotumia CLA yetu.

Mradi huu umetumia [Kanuni ya Maadili ya Chanzo Huria ya Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Kwa maelezo zaidi soma Maswali Yanayoulizwa Mara kwa Mara kuhusu Kanuni ya Maadili au wasiliana kwa [Barua pepe opencode](opencode@microsoft.com) kwa maswali au maoni zaidi.

## Tuanzie Hapa
Sasa baada ya kukamilisha hatua zinazohitajika kukamilisha kozi hii, tuanze kwa kupata [utangulizi wa AI ya Kizazi na LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kituo cha Maelezo**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au kasoro. Nyaraka asli katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba dhima yoyote kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->