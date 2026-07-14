# இந்த பாடத்திட்டத்தைத் தொடங்குதல்

ஜெனரேட்டிவ் ஏஐயுடன் நீங்கள் உருவாக்கத் தூண்டப்படுவது என்ன என்று இப்பாடத்திட்டத்தைத் தொடங்குவதற்கு நாங்கள் மிகவும் உற்சாகமாக இருக்கிறோம்!

உங்கள் வெற்றியை உறுதிப்படுத்த, இந்த பக்கம் அமைப்பு படிகளை, தொழில்நுட்ப தேவைகளை, மற்றும் உதவி பெறும் இடங்களை விளக்குகிறது.

## அமைப்பு படிகள்

இந்த பாடத்திட்டத்தைத் தொடங்க நீங்கள் பின்வரும் படிகளை முடிக்க வேண்டும்.

### 1. இந்த ரெப்போவை ஃபோர்க் செய்யவும்

[இந்த முழுக் ரெப்போவை ஃபோர்க் செய்யவும்](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) உங்கள் சொந்த GitHub கணக்கிற்கு, எந்த குறியீடும் மாற்றி சவால்களை நிறைவேற்ற முடியும். மேலும், [இந்த ரெப்போவை ஸ்டார் செய்யவும் (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) அதையும் சம்பந்தப்பட்ட ரெப்போக்களையும் எளிதில் கண்டுபிடிக்க.

### 2. ஒரு கோட்ஸ்பேசை உருவாக்கவும்

குறியீட்டைப் இயக்கும்போது எந்த சார்பு பிரச்சினைகளும் தவிர்க்க, இந்த பாடத்திட்டத்தை [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) இல் இயக்க பரிந்துரைக்கிறோம்.

உங்கள் ஃபோர்கில்: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ta/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ஒரு ரகசியத்தைச் சேர்க்கவும்

1. ⚙️ கருவி ஐகான் -> கமாண்ட் பிலேட் -> Codespaces : Manage user secret -> Add a new secret.
2. OPENAI_API_KEY என பெயரிடுக, உங்கள் விசையை ஒட்டு, சேமிக்கவும்.

### 3. அடுத்து என்ன?

| நான் என்ன செய்ய விரும்புகிறேன்… | செல்ல வேண்டியது…                                                           |
|-----------------------------|-------------------------------------------------------------------------|
| பாடம் 1 தொடங்கவும்           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ஆஃப்லைன் வேலை செய்தல்       | [`setup-local.md`](02-setup-local.md)                                   |
| LLM வழங்குநரை அமைத்தல்    | [`providers.md`](03-providers.md)                                        |
| மற்ற பயனர்களுடன் சந்திக்க  | [எங்கள் Discord இல் சேரவும்](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## குறைபாடுகள் தீர்க்கல்


| அறிகுறி                                 | சரி செய்வது                                                      |
|----------------------------------------|-----------------------------------------------------------------|
| கன்டெய்னர் கட்டமைப்பு 10 நிமிடங்களுக்கு மேல் தங்கல் | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`            | டெர்மினல் இணைக்கப்படவில்லை; **+** ➜ *bash* கிளிக் செய்யவும்        |
| OpenAI இல் இருந்து `401 Unauthorized`  | தவறான/காலாவதியான `OPENAI_API_KEY`                                |
| VS Code “Dev container mounting…” காட்சி | உலாவி தாளை புதுப்பிக்கவும்—Codespaces சில நேரங்களில் இணைப்பை இழக்கிறது  |
| நோட்டுபுக் கர்னல் காணவில்லை          | நோட்டுபுக் மெனு ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   யுனிக்ஸ் அடிப்படையிலான அமைப்புகள்:

   ```bash
   touch .env
   ```

   விண்டோஸ்:

   ```cmd
   echo . > .env
   ```

3. **`.env` கோப்பை தொகுக்கவும்**: `.env` கோப்பை ஒரு உரை தொகுப்பியில் (उदा., VS Code, Notepad++, அல்லது வேறு வேறு தொகுப்பு) திறந்து, உங்கள் Microsoft Foundry Models முகவரி மற்றும் விசையை உள்ளிடுங்கள் (பெறுவதற்கான வழிமுறைகள் [`providers.md`](03-providers.md) நிரலில் உள்ளன):

   > **குறிப்பு:** GitHub Models (மற்றும் அதன் `GITHUB_TOKEN` மாறிலி)  ஜூலை 2026இல் பணிபுரிந்து முடிகிறது. பதிலாக [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) பயன்படுத்தவும்.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **கோப்பை சேமிக்கவும்**: மாற்றங்களை சேமித்து உரை தொகுப்பியை மூடவும்.

5. **`python-dotenv` நிறுவுக**: நீங்கள் இதுவரை நிறுவவில்லை என்றால், .env கோப்பிலிருந்து சூழல் மாறிலிகளை உங்கள் Python பயன்பாட்டிற்கு ஏற்ற `python-dotenv` தொகுப்பை நிறுவ வேண்டும். இதை `pip` மூலம் நிறுவலாம்:

   ```bash
   pip install python-dotenv
   ```

6. **Python ஸ்கிரிப்டில் சூழல் மாறிலிகளை ஏற்றுக**: உங்கள் Python ஸ்கிரிப்டில், `.env` கோப்பிலிருந்து சூழல் மாறிலிகளை `python-dotenv` மூலம் ஏற்றுக:

   ```python
   from dotenv import load_dotenv
   import os

   # .env கோப்பிலிருந்து சூழல் மாறிலிகளை ஏற்றுக
   load_dotenv()

   # Microsoft Foundry Models மாறிலிகளை அணுகுக
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

அதுவே! நீங்கள் வெற்றிகரமாக `.env` கோப்பை உருவாக்கி, Microsoft Foundry Models அங்கீகாரங்களை சேர், அவற்றை உங்கள் Python பயன்பாட்டில் ஏற்றியுள்ளீர்கள்.

## உங்கள் கணினியில் உள்ளடக்கமாக இயக்குவது எப்படி

குறியீட்டை உங்கள் கணினியில் இயக்க, உங்கள் கணினியில் [Python இன் ஒரு பதிப்பு நிறுவப்பட்டிருக்க வேண்டும்](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

பின்னர், இந்த ரெப்போவை கிளோன் செய்ய வேண்டும்:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

அனைத்து பொருட்களையும் சரிபார்த்த பிறகு, நீங்கள் இப்போது தொடங்கலாம்!

## விருப்ப படிகள்

### Miniconda நிறுவுதல்

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) என்பது [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python மற்றும் சில தொகுப்புகளை நிறுவுவதற்கு எளிமையான நிறுவி ஆகும்.
Conda தானாகவே ஒரு தொகுப்பு மேலாளராகும், இது பல Python [**விர்ச்சுவல் சூழல்களில்**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) மற்றும் தொகுப்புகளின் இடையிலான மாற்றத்தை எளிதாக்குகிறது. இது `pip` மூலம் கிடைக்காத தொகுப்புகளை நிறுவுவதிலும் உதவுகிறது.

அதை அமைப்பதற்கான [MiniConda நிறுவல் வழிகாட்டியை](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) பின்பற்றலாம்.

Miniconda நிறுவப்பட்ட பிறகு, நீங்கள் இப்போதும் கிளோன் செய்ய வேண்டும் [ரெப்போவை](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (முந்தையதாக செய்யவில்லை என்றால்)

அடுத்ததாக, ஒரு விர்ச்சுவல் சூழலை உருவாக்கவேண்டும். இதற்கு Conda துணை கொண்டு, புதிய சூழல் கோப்பை (_environment.yml_) உருவாக்குங்கள். நீங்கள் Codespaces ஐ பயன்படுத்தினால், `.devcontainer` கோப்புறையில் இது இருக்க வேண்டும், அதாவது `.devcontainer/environment.yml`.

கீழ்க்காணும் சிற்றொட்டையை உங்கள் சூழல் கோப்பில் சேர்க்கவும்:

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

எசர்கலைப்போகும் போது, குறைபாடுகள் வந்தால் கீழ்க்காணும் கட்டளையை டெர்மினலில் இயக்கி Microsoft AI நூலகங்களை கையேடு முறையில் நிறுவலாம்.

```
conda install -c microsoft azure-ai-ml
```

சூழல் கோப்பு நாம் தேவையான சார்புகளை குறிப்பிடுகிறது. `<environment-name>` என்பது உங்கள் Conda சூழலுக்கு விரும்பும் பெயர், `<python-version>` என்பது நீங்கள் இயக்க விரும்பும் Python பதிப்பு (எ.கா., `3` என்பது Python இன் சமீபத்திய முக்கிய பதிப்பு).

இதை முடித்த பிறகு, கீழ்க்காணும் கட்டளைகளை உங்கள் கட்டளைப் பத்தியில்/டெர்மினலில் இயக்கி உங்கள் Conda சூழலை உருவாக்கலாம்

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer துணை பாதை Codespace அமைப்புகளுக்கு மட்டும் பொருந்தும்
conda activate ai4beg
```

எந்த பிரச்சனையோ ஏற்பட்டால் [Conda சூழல்கள் வழிகாட்டி](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) பார்க்கவும்.

### Python மேலாண்மையுடன் Visual Studio Code பயன்படுத்துதல்

இந்த பாடத்திட்டத்துக்கு நாம் பரிந்துரைக்கிறோம் [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) தொகுப்பாளியை [Python மேலாண்மை நீட்சியுடன்](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) பயன்படுத்த. இது பரிந்துரை மட்டுமே, கட்டாயம் அல்ல.

> **குறிப்பு**: பாடத்திட்ட ரெப்போவை VS Code இல் திறந்தால், திட்டத்தை ஒரு கன்டெய்னரில் அமைப்பதற்கான விருப்பம் உங்களுக்கு கிடைக்கும். இது பாடத்திட்டத்தில் உள்ள [சிறப்பு `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) கோப்புறையின் காரணமாகவே. இதை பின்னர் மேலும் பார்க்கலாம்.

> **குறிப்பு**: நீங்கள் ரெப்போவை கிளோன் செய்து VS Code இல் திறந்தவுடன், Python மேலாண்மை நீட்சியை நிறுவ பரிந்துரை வரும்.

> **குறிப்பு**: VS Code ரெப்போவை கன்டெய்னரில் மீண்டும் திறக்க பரிந்துரைத்தால், அதை மறுக்கவும், ஏனெனில் நீங்கள் உள்ளூர் கணினியில் நிறுவிய Python ஐ பயன்படுத்த விரும்பலாம்.

### உலாவியில் Jupyter பயன்படுத்தல்

இந்த திட்டத்தில் வேலை செய்வதற்கு நீங்கள் உங்கள் உலாவியில் உள்ள [Jupyter சூழலை](https://jupyter.org?WT.mc_id=academic-105485-koreyst) பயன்படுத்தலாம். பாரம்பரிய Jupyter மற்றும் [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) இரண்டும் தானாகக் குமிழ்நீக்கம், குறியீட்டு வெளிச்சம் போன்ற வசதிகளுடன் ஒரு இனிமையான அபிவிருத்தி சூழலை வழங்குகின்றன.

Jupyter ஐ உள்ளூர் இயக்க, டெர்மினல்/கமாண்ட் பத்தியை திறந்து, பாடத்திட்ட கோப்புறைக்கு சென்று, கீழ்க்காணும் கட்டளை இயக்கவும்:

```bash
jupyter notebook
```

அல்லது

```bash
jupyterhub
```

இது ஒரு Jupyter இடத்தைத் துவக்கி, அணுகும் URL-ஐ கட்டளை பத்தி சாளரத்தில் காட்டும்.

நீங்கள் அந்த URL-ஐ அணுகியவுடன், பாடத்திட்ட விளக்கத்தைப் பார், எந்த `*.ipynb` கோப்பிடத்திற்கும் செல்ல முடியும். உதாரணமாக, `08-building-search-applications/python/oai-solution.ipynb`.

### கன்டெய்னரில் இயக்குதல்

உங்கள் கணினியிலும் Codespace-லுமல்லாமல் ஒரு [கன்டெய்னர்](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) பயன்படுத்துவதும் வழி உள்ளது. பாடத்திட்ட ரெப்போவின் `.devcontainer` கோப்புறை இதை VS Codeலாக அமைக்க உதவுகிறது. Codespaces தவிர, இது Docker நிறுவல் தேவைப்படும், மற்றும் ஒரு கட்டாய வேலை, எனவே தயவுசெய்து கன்டெய்னர் அனுபவம் உள்ளவர்கள் மட்டுமே இதை முயற்சிக்க வேண்டும்.

GitHub Codespaces பயன்படுத்தும்போது உங்கள் API விசைகளை பாதுகாப்பாக வைப்பதற்கான சிறந்த வழிகளில் ஒன்று Codespace ரகசியங்களை பயன்படுத்துதல். இதற்கான மேலாண்மை முறையை அறிய [Codespaces ரகசிய மேலாண்மை](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) வழிகாட்டியை பின்பற்றவும்.


## பாடங்கள் மற்றும் தொழில்நுட்ப தேவைகள்

இந்த பாடத்திட்டத்தில் 6 கருத்துப் பாடங்களும் 6 குறியீட்டு பாடங்களும் உள்ளன.

குறியீட்டு பாடங்களுக்கான, நாம் Azure OpenAI சேவையைப் பயன்படுத்துகிறோம். இந்த குறியீட்டை இயக்க Azure OpenAI சேவையிலும் API விசையுமே வேண்டும். அணுகலை பெற [இந்த விண்ணப்பத்தை](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) பூர்த்தி செய்து கோரி பெறலாம்.

உங்கள் விண்ணப்பம் செயலாக்கப்படும் வரை, ஒவ்வொரு குறியீட்டு பாடத்திலும் உள்ள `README.md` கோப்பில் குறியீடு மற்றும் வெளியீடுகளை பார்க்கலாம்.

## Azure OpenAI சேவையை முதல்முறை பயன்பாடு

இது உங்கள் முதல் முறையாக Azure OpenAI சேவையைப் பயன்படுத்துவதாக இருந்தால், [Azure OpenAI சேவை வளங்களை உருவாக்கி இயக்கும் வழிகாட்டியை](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) பின்பற்றவும்.

## OpenAI API-ஐ முதல் முறையாக பயன்படுத்துதல்

இது உங்கள் முதல் முறையாக OpenAI API-ஐப் பயன்படுத்துகிறீர்களானால், [இணையமைப்பை உருவாக்கி பயன்படுத்தும் வழிகாட்டியை](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) பின்பற்றவும்.

## மற்ற பயனர்களுடன் சந்திப்பு

நாங்கள் அதிகாரப்பூர்வ [AI சமூha Discord சேவையில்](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) மற்ற பயனர்களுக்கு சந்திப்புக்கான சேனல்கள் உருவாக்கியுள்ளோம். இது இதேபோன்ற ஆசைப்படுவோரோடு, கலைஞர்களோடு, மாணவர்களோடு இணைந்து வலைபின்னல் அமைப்பதற்கான சிறந்த வழி.

[![Discord சேனலில் சேரவும்](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

திட்ட குழு இந்த Discord சேவையிலிருப்பார்கள் மற்றும் பயனர்களுக்கு உதவுவார்கள்.

## பங்களிக்கவும்

இந்த பாடத்திட்டம் ஒரு திறந்த மூல முயற்சி ஆகும். மேம்பாடுகள் அல்லது பிழைகள் இருந்தால், [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) உருவாக்கவும் அல்லது [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) பதிவு செய்யவும்.

திட்ட குழு அனைத்து பங்களிப்புகளையும் கண்காணிப்பார்கள். திறந்த மூலத்தில் பங்களிப்பது ஜெனரேட்டிவ் ஏஐ-இல் உங்கள் வாழ்க்கைமாறு அமைப்பதற்கான ஒரு அற்புதமான வழி.

பெரும்பாலான பங்களிப்புகள், நீங்கள் அந்த பங்களிப்பை பயன்படுத்துவதற்கு உரிமை உங்களுக்கு இருப்பதாகவும், உண்மையிலேயும் அப்படி செய்கிறீர்களா என்று உறுதிப்படுத்தும் பங்களிப்பாளர் உரிமம் ஒப்பந்தம் (CLA) ஒப்புதல் தேவைப்படும். விரிவாக, [CLA, Contributor License Agreement இணையதளத்தை](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) பார்க்கவும்.

முக்கியம்: இந்த ரெப்போவில் உரையை மொழிபெயர்க்கும்போது, இயந்திர மொழிபெயர்ப்பைப் பயன்படுத்த வேண்டாம். சமூகத்தினரால் மொழிபெயர்ப்புகள் சரிபார்க்கப்படும், எனவே நீங்கள் தேர்ச்சி பெற்ற மொழிகளில் மட்டும் மொழிபெயர்ப்புக்கான தன்னார்வப் பார்வையாளராக இருங்கள்.

நீங்கள் ஒரு pull request சமர்ப்பிக்கும் போது, CLA-பாட் தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்பதையும், PR-ஐ சரியானவாறு அடையாளம் காணும் (எ.கா., லேபல், கருத்து). பின் படிகள் அவனின் வழிகாட்டுதல்களைப் பின்பற்றுங்கள். இது ஒரு முறையே அனைத்து ரெப்போக்களுக்கும் செய்வது போதுமானது.


இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)-ஐ ஏற்றுக்கொண்டுள்ளது. கூடுதல் தகவலுக்கு Code of Conduct FAQஐ படிக்கவும் அல்லது [Email opencode](opencode@microsoft.com)க்கு மேலதிக கேள்விகள் அல்லது கருத்துக்கள் இருந்தால் தொடர்புகொள்ளவும்.

## ஆவனையுடன் தொடங்குவோம்

இப்போது நீங்கள் இந்த பாடங்களை முடித்துள்ளீர்கள், தொடங்கும்போது [Generative AI மற்றும் LLMகளுக்கான அறிமுகம்](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) பெறுவோம்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->