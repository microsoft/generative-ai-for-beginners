# இந்த பாடத்திட்டத்தை தொடங்குதல்

இந்தப் பாடத்திட்டத்தை நீங்கள் தொடங்கி, ஜெனரேட்டிவ் AI உடன் நீங்கள் உருவாக்கும் அதிர்ஷ்டத்தை பார்க்க நாங்கள் மிகவும் உற்சாகமாக உள்ளோம்!

உங்கள் வெற்றியை உறுதிசெய்ய, இந்த பக்கம் அமைப்பு படிகள், தொழில்நுட்ப தேவைகள் மற்றும் உதவி எங்கே பெறுவது என்பதை விளக்குகிறது.

## அமைப்பு படிகள்

இந்தப் பாடத்தை தொடங்க, கீழ்க்காணும் படிகளை நீங்கள் முடிக்க வேண்டும்.

### 1. இந்த ரெப்போவை ஃபோர்க் செய்யவும்

[இந்த முழு ரெப்போவை ஃபோர்க் செய்யவும்](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) உங்கள் சொந்த GitHub கணக்கிற்கு, இதன்மூலம் நீங்கள் ஏதேனும் குறியீடுகளை மாற்றி சவால்களை முடிக்க முடியும். மேலும் இதையும் மற்றும் தொடர்புடைய ரெப்போக்களை எளிதில் காண [⭐ (ஸ்டார்) செய்யவும்](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst).

### 2. கோட்ஸ்பேஸ் உருவாக்கவும்

குறியீட்டை இயக்கும் போது பிற சார்புகள் பிரச்சனைகளில் எடையை தவிர்க்க, இந்த பாடத்தை [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) இல் இயக்க பரிந்துரைக்கப்படுகிறது.

உங்கள் ஃபோர்கில்: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ta/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ஒரு ரகசியத்தைச் சேர்க்கவும்

1. ⚙️ கருவி ஐகன் -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. OPENAI_API_KEY என்று பெயர் இடுங்கள், உங்கள் விசையை ஒட்டவும், சேமிக்கவும்.

### 3. அடுத்து என்ன?

| நான் விரும்புவது…       | செல்ல வேண்டியது…                                                       |
|---------------------|-------------------------------------------------------------------------|
| பாடம் 1 தொடங்கு     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ஆஃப்லைனில் பணியாற்று | [`setup-local.md`](02-setup-local.md)                                   |
| ஒரு LLM வழங்குநரை அமைக்கவும் | [`providers.md`](03-providers.md)                                        |
| மற்ற மாணவர்களை சந்திக்கவும் | [எங்கள் Discord-இல் சேரவும்](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## பிரச்சனைத் தீர்க்கும் வழிகள்


| அறிகுறி                                  | தீர்வு                                                            |
|-------------------------------------------|-----------------------------------------------------------------|
| கொண்டெயினர் கட்டுமானம் 10 நிமிடத்திற்கு மேலாக நின்று இருக்கிறது | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | டெர்மினல் இணைக்கப்படவில்லை; **+** கிளிக் செய்து *bash* தேர்வு செய்யவும்    |
| OpenAI-இல் இருந்து `401 Unauthorized`    | தவறான அல்லது காலாவதியான `OPENAI_API_KEY`                       |
| VS Code “Dev container mounting…” காட்டுகிறது | உலாவி தாவலை புதுப்பிக்கவும்—Codespaces சில நேரங்களில் இணைப்பை இழக்கிறது |
| நோட்புக்கின் கர்னல் காணவில்லை               | நோட்புக் மெனு ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   யூனிக்ஸ் அடிப்படையிலான கணினிகள்:

   ```bash
   touch .env
   ```

   விண்டோஸ்:

   ```cmd
   echo . > .env
   ```

3. **`.env` கோப்பை திருத்தவும்**: `.env` கோப்பை உரை திருத்தியில் (எ.ก., VS Code, Notepad++, அல்லது வேறு எந்த திருத்தியிலும்) திறக்கவும். கீழ்காணும் வரிகளை சேர்த்து, உங்கள் Microsoft Foundry Models முனையத்தையும் விசையையும் (விளக்கத்திற்கு [`providers.md`](03-providers.md) பார்க்கவும்) பதிலாக பயன்படுத்தவும்:

   > **குறிப்பு:** GitHub Models (மற்றும் அதனுடைய `GITHUB_TOKEN` மாறி) ஜூலை 2026 முடிவில் சேவை நிறுத்துகிறது. அதன் பதிலாக [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) பயன்படுத்தவும்.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **கோப்பை சேமிக்கவும்**: மாற்றங்களை சேமித்து உரை திருத்தியை மூடவும்.

5. **`python-dotenv` நிறுவவும்**: நீங்கள் இதுவரை நிறுவாதிருந்தால், `.env` கோப்பிலிருந்து வகை நிலை மாறிகள் போன்றவற்றை உங்கள் Python செயலியில் ஏற்க `python-dotenv` தொகுப்பை நிறுவவேண்டும். `pip` மூலம் நிறுவலாம்:

   ```bash
   pip install python-dotenv
   ```

6. **Python ஸ்க்ரிப்டில் வகை நிலை மாறிகளை ஏற்றி கொள்ளவும்**: உங்கள் Python ஸ்கிரிப்டில், `python-dotenv` தொகுப்பை பயன்படுத்தி `.env` கோப்பிலிருந்து வகை நிலை மாறிகளை ஏற்றவும்:

   ```python
   from dotenv import load_dotenv
   import os

   # .env கோப்பிலிருந்து சுற்றுச்சூழல் மாறிகள் ஏற்று
   load_dotenv()

   # Microsoft Foundry Models மாறிகள் அணுகு
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

அதுவே! நீங்கள் வெற்றிகரமாக `.env` கோப்பை உருவாக்கி, உங்கள் Microsoft Foundry Models அங்கீகாரங்களைச் சேர்த்து, உங்கள் Python செயலியில் ஏற்றிவிட்டீர்கள்.

## உங்கள் கணினியில் உள்ளூர் இயக்குவது எப்படி

குறியீட்டை உங்கள் கணினியில் உள்ளூர் இயக்க, நீங்கள் எந்தவொரு [Python பதிப்பையும் நிறுவியிருக்க வேண்டும்](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

பின்னர் ரெப்போவை பயன்படுத்த, அதை கிளோன் செய்ய வேண்டும்:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

எல்லாவற்றையும் சரிபார்த்து பெற்ற பிறகே, நீங்கள் துவங்கலாம்!

## விருப்ப படிகள்

### மினிகொண்டா நிறுவல்

[மினிகொண்டா](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) என்பது [கொண்டா](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python மற்றும் சில தொகுப்புகளை நிறுவ ஒரு மென்மையான நிறுவி ஆகும்.
கொண்டா என்பது ஒரு தொகுப்பு மேலாளர்; இது Python [**மெய்நிகர் சூழல்களை**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) மற்றும் தொகுப்புகளை அமைக்கவும் மாறிடவும் சுலபமாக்குகிறது. `pip` மூலம் கிடைக்காத தொகுப்புகளை நிறுவ உதவும்.

[மினிகொண்டா நிறுவல் வழிகாட்டியை](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) பின்பற்ற வியூகிக்கவும்.

மினிகொண்டா நிறுவிய பிறகு, [ரெப்போவை](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (இன்னும் கிளோன் செய்யவில்லை என்றால்) கிளோன் செய்யவும்.

அடுத்து, ஒரு மெய்நிகர் சூழலை உருவாக்க வேண்டும். கொண்டாவுடன், _environment.yml_ என்ற சூழல் கோப்பை உருவாக்கி, Codespaces பயன்படுத்தினால் அந்த கோப்பை `.devcontainer` கோப்பகத்தில் வைத்து `.devcontainer/environment.yml` ஆக உருவாக்கவும்.

கீழ்காணும் சான்று குறியீட்டை உங்கள் சூழல் கோப்பில் நிரப்பவும்:

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

கொண்டா பயன்படுத்தும்போது பிழைகள் வந்தால், டெர்மினலில் கீழ்க்காணும் கட்டளையைக் கொண்டு Microsoft AI நூலகங்களை கைமுறையால் நிறுவலாம்.

```
conda install -c microsoft azure-ai-ml
```

சூழல் கோப்பு நமக்கு தேவைப்படும் சார்புகளை குறிப்பிடுகிறது. `<environment-name>` என்பது நீங்கள் கொண்டா சூழலுக்கு கொடுக்க விரும்பும் பெயர், `<python-version>` என்பது நீங்கள் பயன்படுத்த விரும்பும் Python பதிப்பு, உதாரணமாக `3` என்பது Python இன் புதிய பிரதான பதிப்பாகும்.

இவற்றை முடித்த பின், கீழ்காணும் கட்டளைகளை உங்கள் கட்டளைக் கோப்பில்/டெர்மினலில் இயக்கி கொண்டா சூழலை உருவாக்கவும்

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer உபபாதை Codespace அமைப்புகளுக்கு மட்டுமே பொருந்தும்
conda activate ai4beg
```

ஏதேனும் பிரச்சனை வந்தால் [கொண்டா சூழல் வழிகாட்டி](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ஐ பார்க்கவும்.

### Python ஆதரவுடன் Visual Studio Code பயன்படுத்துதல்

இந்த பாடத்திற்கு, [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) மற்றும் அதில் உள்ள [Python ஆதரவு நீட்சியை](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) பயன்படுத்த பரிந்துரைக்கிறோம். இது ஒரு பரிந்துரையே; கட்டாயம் இல்லை.

> **குறிப்பு**: VS Code இல் பாடம் ரெப்போவைத் திறந்தவுடன், உங்கள் திட்டத்தை ஒரு கொண்டெயினர் வழியாக அமைக்க επιλογம் உள்ளது. இதற்கு காரணம் பாடம் ரெப்போவில் உள்ள [சிறப்பு `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) கோப்பகம் ஆகும். பின்னர் இதில் விளக்கம்.

> **குறிப்பு**: நீங்கள் ரெப்போவை கிளோன் செய்து VS Code இல் திறக்கும்போது, Python ஆதரவு நீடியை நிறுவ பரிந்துரை செய்யப்படும்.

> **குறிப்பு**: VS Code ரெப்போவை கொண்டெயினரில் மீண்டும் திறக்க பரிந்துரைத்தால், அதற்கான வேண்டுகோளை மறுத்து உள்ளூர் Python பதிப்பை பயன்படுத்தவும்.

### உலாவியில் Jupyter பயன்படுத்துதல்

உலாவியில் உள்ளே [Jupyter சூழலை](https://jupyter.org?WT.mc_id=academic-105485-koreyst) பயன்படுத்தி பணியாற்றலாம். இரண்டிலும், பழமையான Jupyter மற்றும் [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) தானாக நிறைவு, குறியீடு வண்ணமயமாக்கல் போன்ற வாய்ப்புகளை கொண்ட இனிமையான வளர்ச்சிச் சூழல்களை வழங்குகின்றன.

Jupyter ஐ உள்ளூரில் தொடங்க, டெர்மினல்/கட்டளைக் கோப்பிற்கு சென்று பாடம் கோப்புறைக்கு நகர்ந்து இயக்கவும்:

```bash
jupyter notebook
```

அல்லது

```bash
jupyterhub
```

இதனால் Jupyter வேலை நிழல் துவங்கி, அணுகுவதற்கான URL கட்டளைக் கோப்பு ஜன்னலில் காட்டப்படும்.

அந்த URL ஐ அணுகியவுடன், பாட திட்ட அகத்தை காண்பீர்கள் மற்றும் எந்த `*.ipynb` கோப்புக்கும் செல்ல முடியும். உதாரணமாக, `08-building-search-applications/python/oai-solution.ipynb`.

### கொண்டெயினரில் இயக்குதல்

உங்கள் கணினியில் அல்லது Codespace இல் அனைத்தையும் அமைக்கும் மாற்றாக [ஒரு கொண்டெயினர்](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) பயன்படுத்தலாம். பாடம் ரெப்போவில் உள்ள சிறப்பு `.devcontainer` கோப்பகம் VS Code இல் கொண்டெயினரில் இதை அமைக்க உதவும். Codespaces தவிர்ப்பில், Docker நிறுவ வேண்டும்; இது குறுகிய நேரம் மற்றும் அனுபவம் தேவைபடும், ஆகையால் கொண்டெயினர்களில் அனுபவமுள்ளவர்களுக்கு பரிந்துரைக்கப்படுகின்றது.

GitHub Codespaces பயன்படுத்தும் போது உங்கள் API விசைகளை பாதுகாப்பதற்கான சிறந்த வழிகளில் ஒன்று Codespace ரகசியங்களைப் பயன்படுத்தல் ஆகும். இதைப் பற்றி இங்கே பார்க்கவும்: [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)


## பாடங்கள் மற்றும் தொழில்நுட்ப தேவைகள்

பாடத்தில் "கற்றல்" பாடங்கள் ஜெனரேட்டிவ் AI கருத்துக்களை விளக்கும்; "உருவாக்குதல்" பாடங்கள் Python மற்றும் TypeScript இல் கையால் எழுதும் குறியீடு உதாரணங்களைக் கொண்டவை.

குறியீட்டுப் பாடங்களுக்கு, Microsoft Foundry இல் Azure OpenAI பயன்படுத்தப்படுகிறது. இதற்காக Azure சந்தா மற்றும் API விசை வேண்டும். விண்ணப்பம் இல்லாமல் திறந்த அணுகல் உள்ளது - அதனால் [Microsoft Foundry வளத்தை உருவாக்கி மற்றும் ஒரு மாதிரியை தளத்தில் அனுப்ப](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) உங்கள் முனையத்தையும் விசையையும் பெறலாம்.

ஒவ்வொரு குறியீட்டு பாடத்திலும் குறியீடு மற்றும் வெளியீடுகளை இயக்காமல் பார்ப்பதற்கான `README.md` கோப்பு உண்டு.

## Azure OpenAI சேவையை முதன்முறையாக பயன்படுத்துதல்

இது Azure OpenAI சேவையை முதன்முறையாக பயன்படுத்தினால், தயவுசெய்து இந்த வழிகாட்டியை பின்பற்ற [Azure OpenAI சேவை வளத்தை உருவாக்கி அனுப்புவது எப்படி](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API-ஐ முதன்முறையாக பயன்படுத்துதல்

OpenAI API-ஐ முதன்முறையாக பயன்படுத்தினால், இந்த வழிகாட்டியை பின்பற்றவும்: [இணைமுகத்தை உருவாக்கி பயன்படுத்துவது எப்படி](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## மற்ற மாணவர்களை சந்திக்க

எங்கள் அதிகாரப்பூர்வ [AI Community Discord சேவையகத்தில்](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) மற்ற மாணவர்களை சந்திக்க சேனல் அமைத்துள்ளோம். இது மற்றபடியும் சேர்க்கையோடு முனைந்த தொழில்களோடு, கட்டுமானத்தோடு, மாணவர்களோடு மற்றும் ஜெனரேட்டிவ் AI-யில் முன்னேறும் விருப்பமுள்ளவர்களோடு தொடர்பை பராமரிக்க சிறந்த வழி.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

இந்த Discord சேவையகத்தில் திட்ட குழு மாணவர்களுக்கு உதவும்.

## பங்களிக்கவும்

இந்த பாடத்திட்டம் திறந்த மூல முயற்சி ஆகும். மேம்பாட்டு பகுதிகள் அல்லது பிரச்சனைகள் இருந்தால், தயவுசெய்து [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) உருவாக்கவும் அல்லது [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) பதிவேற்றவும்.

திட்டம் அனைத்து பங்களிப்புகளையும் கண்காணிக்கும். திறந்த மூலத்திற்கு பங்களிப்பு செய்வது ஜெனரேட்டிவ் AI-யில் உங்கள் தொழிலை உருவாக்க சிறந்த வழி.

பெரும்பாலான பங்களிப்புகளுக்கு, நீங்கள் ஒரு பங்களிப்பாளர் உரிமம் ஒப்பந்தத்துக்கு (CLA) ஒப்புக்கொண்டிருப்பது அவசியம். இதில் நீங்கள் பங்களிப்பை வழங்கும் உரிமையை கொண்டுள்ளீர்கள் என்றும், நமக்கு பயன் படுத்த அனுமதி தருவீர்கள் என்றும் கூறப்படுகிறது. விரிவுகளுக்கு [CLA, Contributor License Agreement இணையத்தளம்](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) பார்க்கவும்.

முக்கியம்: இந்த ரெப்போவில் உள்ள உரைகளை மொழிமாற்றம் செய்யும்போது, தயவு செய்து மெஷின் தமிழ் மொழிமாற்றத்தைப் பயன்படுத்த வேண்டாம். மொழிபெயர்ப்புகளை சமுதாயத்தின் மூலம் சரிபார்ப்போம். எனவே, நீங்கள் நன்றாக அறிந்த மொழிகளுக்குப் பணி செய்யவும்.


நீங்கள் ஒரு pull request சமர்ப்பிக்கும் போது, CLA-bot தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்று தீர்மானித்து PR ஐ பொருத்தமான முறையில் அலங்கரிக்கும் (உதாரணமாக, லேபல், கருத்து). இந்தக் கட்டளைபடி bot வழங்கும் வழிமுறைகளை பின்பற்றுங்கள். நீங்கள் எங்கள் CLA ஐ பயன்படுத்தும் அனைத்து சேமிப்பகங்களிலும் இதை ஒருமுறை ғана செய்ய வேண்டும்.

இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ஐ ஏற்றுக்கொண்டுள்ளது. கூடுதல் தகவலுக்கு நடத்தை விதிமுறைகள் FAQ ஐ படியுங்கள் அல்லது [Email opencode](opencode@microsoft.com) என்ற முகவரிக்கு கூடுதல் கேள்விகள் அல்லது கருத்துக்களை அனுப்புங்கள்.

## தொடங்குவோம்

இப்போது நீங்கள் இந்த பாடத்திட்டத்தை முடித்துள்ளீர்கள், [இங்கு இருந்து ஜெனரட்டிவ் AI மற்றும் LLM களை அறிமுகம்](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) படியுங்கள்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->