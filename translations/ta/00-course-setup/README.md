# இந்த பாடத்திட்டத்தைத் தொடங்குதல்

உங்களுக்கு இந்தப் பாடத்திட்டத்தைத் தொடங்குவதற்கும் உங்களுக்கு சிறந்த ஊக்கத்தை தரும் Generative AI உடன் என்ன செய்யப் போகிறீர்கள் என்பதைப் பார்க்க மிகவும் மகிழ்ச்சி!

உங்கள் வெற்றிக்காக, இந்தப் பக்கம் அமைப்பு படிகளை, தொழில்நுட்ப தேவைகளை, மற்றும் உதவி தேவைப்படின் எங்கே அணுகுவது என்பதைக் குறிப்பிடுகிறது.

## அமைப்பு படிகள்

இந்தக் குர்ஸ் எடுக்கத் தொடங்க, கீழ்காணும் படிகளை முடிக்க வேண்டும்.

### 1. இந்த ரெப்போவை Fork செய்க

அனைத்துக் கோடையும் மாற்றவும் சவால்கள் முடிக்கவும் உங்கள் சொந்த GitHub கணக்கிற்கு [இந்த முழு ரெப்போவை Fork செய்யவும்](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). மேலும் இதை மற்றும் தொடர்புடைய ரெப்போக்களை எளிதாக கண்டுபிடிக்க [நட்சத்திரம் (🌟) விடவும்](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst).

### 2. codespace உருவாக்கவும்

குறியீடு இயக்கும் போது எந்தவொரு சார்பு பிரச்சனையும் இருக்காமல் இருக்க [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) இல் இந்தக் குயர்ஸை இயக்க பரிந்துரைக்கப்படுகிறது.

உங்கள் fork இல்: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ta/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ஒரு ரகசியம் சேர்க்கவும்

1. ⚙️ பூட்டு ஐகான் -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. OPENAI_API_KEY என பெயரிடவும், உங்கள் விசையை ஒட்டவும், சேமிக்கவும்.

### 3. அடுத்து என்ன?

| நான் ... செய்ய விரும்புகிறேன் | செல்ல...                                                                  |
|-----------------------------|-------------------------------------------------------------------------|
| பாடம் 1 துவங்கவும்          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ஆஃப்லைனில் வேலை செய்யவும்  | [`setup-local.md`](02-setup-local.md)                                   |
| ஒரு LLM வழங்குநரை அமைக்கவும் | [`providers.md`](03-providers.md)                                        |
| மற்ற கற்றுக்கொள்ளுபவர்களை சந்திக்கவும் | [எங்கள் Discord சேரவும்](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## சிக்கல் தீர்க்கும் வழிகள்


| அறிகுறி                                   | சரி செய்யும் வழி                                                 |
|-------------------------------------------|-----------------------------------------------------------------|
| Container கட்டுமானம் 10 நிமிடங்களுக்கு மேல் தாமதம் | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | டெர்மினல் இணைக்கப்படவில்லை; **+** ஐ சொடுக்கி *bash* தேர்வு செய்க    |
| OpenAI-விலிருந்து `401 Unauthorized`       | தவறான அல்லது காலாவதியான `OPENAI_API_KEY`                        |
| VS Code “Dev container mounting…” காட்டுகிறது | இணைய உலாவி தாள் புதுப்பிக்கவும்—Codespaces நேரத்துக்கு இழப்பு ஏற்படும் நேரம் உள்ளது  |
| நோட்புக் கர்னல் காணாமலிருக்கிறது          | நோட்புக் மெனு ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix அடிப்படையிலான அமைப்புகள்:

   ```bash
   touch .env
   ```

   வின்டோஸ்:

   ```cmd
   echo . > .env
   ```

3. **`.env` கோப்பைத் திருத்தவும்**: `.env` கோப்பை ஏதேனும் உரை திருத்தியில் (எ.கா., VS Code, Notepad++, அல்லது மற்ற) திறந்துகொண்டு, கீழ்காணும் வரியை சேர்க்கவும், `your_github_token_here` எனும் பகுதியை உங்கள் நிஜ GitHub டோக்கனில் மாற்றவும்:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **கோப்பை சேமிக்கவும்**: மாற்றங்களைச் சேமித்து, உரை திருத்தியை மூடவும்.

5. **`python-dotenv` ஐ நிறுவவும்**: நீங்கள் இன்னும் நிறுவவில்லை என்றால், `.env` கோப்பிலிருந்து மாறிலி உள்ளீட்டை கொண்டுவர `python-dotenv` பேக்கேஜைப் பயன்படுத்த வேண்டும். அதை `pip` மூலம் நிறுவலாம்:

   ```bash
   pip install python-dotenv
   ```

6. **இயல்பு மாறிலிகளை உங்கள் Python ஸ்கிரிப்டில் ஏற்றவும்**: உங்கள் Python ஸ்கிரிப்டில் `.env` கோப்பிலிருந்து இயல்புகளைக் குறியிட `python-dotenv` பயன்படுத்தவும்:

   ```python
   from dotenv import load_dotenv
   import os

   # .env கோப்பில் இருந்து சுற்றுச்சூழல் மாறிகளை ஏற்றுக
   load_dotenv()

   # GITHUB_TOKEN மாறி அணுகுக
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

இது மட்டும்! நீங்கள் வெற்றிகரமாக `.env` கோப்பை உருவாக்கி, GitHub டோக்கனைச் சேர்த்து அதை Python செயலியில் ஏற்றியுள்ளீர்கள்.

## உங்கள் கணினியில் உள்ளூராக இயக்கும் முறை

கோடை உங்கள் கணினியில் உள்ளூர் இயக்க, உங்கள் கணினியில் ஏதேனும் Python பதிப்பு [நிறுவப்பட்டிருக்க வேண்டும்](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

பின்பு, ரெப்போவை பயன்படுத்த, அதை கிளோன் செய்ய தேவையானது:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

எல்லாம் சரிபார்த்த பலகையுடன், நீங்கள் துவங்கலாம்!

## விருப்ப படிகள்

### Miniconda நிறுவல்

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) என்பது [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python மற்றும் சில பேக்கேஜ்களை நிறுவ ஒரு நெகிழ்வான நிறுவி ஆகும்.
Conda என்பது பல்வேறு Python [**மெய்நிகர் சூழல்**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) மற்றும் பேக்கேஜ்களை அமைக்க மற்றும் மாறுவதற்கு எளிதாக்கும் பேக்கேஜ் மேலாளி ஆகும். `pip` மூலம் கிடைக்காத பேக்கேஜ்களை நிறுவவும் இது உதவும்.

நீங்கள் [MiniConda நிறுவல் வழிகாட்டி](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) பின்பற்றி அதை அமைக்கலாம்.

Miniconda நிறுவிய பிறகு, ரெப்போவை கிளோன் செய்ய வேண்டும் (இன்னும்வரவில்லை என்றால்).

அடுத்து, ஒரு மெய்நிகர் சூழலை உருவாக்க வேண்டும். Conda உடன் இது செய்ய, புதிய சூழல் கோப்பை (_environment.yml_) உருவாக்குங்கள். நீங்கள் Codespaces பயன்படுத்தினால், `.devcontainer` அடைவுக்குள், அதாவது `.devcontainer/environment.yml` இல் உருவாக்கவும்.

கீழ்க்காணும் கோப்பின் உள்ளடக்கத்தை உங்கள் சூழல் கோப்பில் சேர்க்கவும்:

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

conda பயன்படுத்தும் போது பிழைகள் வரும் எனில், கீழ்காணும் கட்டளை மூலம் Microsoft AI நூலகங்களை உள்ளகமாக நிறுவலாம்.

```
conda install -c microsoft azure-ai-ml
```

சூழல் கோப்பு தேவையான சார்புகளை குறிப்பிடுகிறது. `<environment-name>` என்பது நீங்கள் உங்கள் Conda சூழல் பெயராக பயன்படுத்த விரும்பும் பெயர், `<python-version>` என்பது பயன்படுத்த விரும்பும் Python பதிப்பு, உதாரணமாக, `3` என்பது Python இன் தற்போதைய பெரிய பதிப்பு.

இதற்குப் பிறகு கீழ்க்காணும் கட்டளைகளை உங்கள் கட்டளை வரி/டெர்மினலில் இயக்கு மற்றும் உங்கள் Conda சூழலை உருவாக்குங்கள்:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer உப பாதை Codespace அமைப்புகளுக்கு மட்டுமே பொருந்தும்
conda activate ai4beg
```

எந்தவொரு சிக்கலும் ஏற்பட்டால் [Conda சூழல்கள் வழிகாட்டியை](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) பார்க்கவும்.

### Python ஆதரவு விரிவாக்கத்துடன் Visual Studio Code பயன்படுத்துதல்

இந்தக் குர்ஸிற்காக [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ஆசிரியர் மற்றும் [Python ஆதரவு விரிவாக்கம்](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) நிறுவி பயன்படுத்த பரிந்துரைக்கப்படுகிறது. எனினும் இதுவே கட்டாயமல்ல, பரிந்துரை மட்டுமே.

> **குறிப்பு**: இந்தக் குர்ஸ் ரெப்போவை VS Code இல் திறக்கும் போது, இது ஒரு கன்டெய்னரில் திட்டத்தை அமைக்க வாய்ப்பு வழங்கும். காரணம், இந்தக் குர்ஸ் ரெப்போவில் இருக்கும் [சிறப்பு `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) அடைவு. இதைப் பற்றி பின்னர் மேலும் அறியலாம்.

> **குறிப்பு**: ரெப்போவை கிளோன் செய்து VS Code இல் திறந்தவுடன், Python ஆதரவு விரிவாக்கத்தை நிறுவ பரிந்துரைக்கும்.

> **குறிப்பு**: VS Code ரெப்போவை மறுபடியும் கன்டெய்னரில் திறக்கச் சொல்லின், உங்கள் உள்ளூர் Python பதிப்பை பயன்படுத்த மறுக்கவும்.

### உலாவியில் Jupyter பயன்படுத்துதல்

நீங்கள் [Jupyter சூழலை](https://jupyter.org?WT.mc_id=academic-105485-koreyst) உங்கள் உலாவியில் நேரடியாகவும் பயன்படுத்தலாம். கிளாசிக் Jupyter மற்றும் [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) இரண்டும் ஆட்டோ-கூறுதல், குறியீடு விளக்குதல் போன்ற வசதிகள் கொண்ட சந்தோஷமான மேம்பாட்டு சூழலை வழங்குகின்றன.

Jupyter ஐ உள்ளூர் துவங்க, டெர்மினல்/கட்டளை வரிக்கு சென்று, பாடத்திட்ட அடைவுக்கு செல்லவும், பின்வரும் கட்டளையை இயக்கவும்:

```bash
jupyter notebook
```

அல்லது

```bash
jupyterhub
```

இதனால் Jupyter தொடங்கும், அணுக URL கட்டளை வரியில் காட்டப்படும்.

URL-ஐ அணுகியவுடன் பாடக்குறிப்பை காணலாம், எந்த `*.ipynb` கோப்புகளையும் திறக்கலாம். உதா., `08-building-search-applications/python/oai-solution.ipynb`.

### கன்டெய்னரில் இயக்குதல்

உங்கள் கணினி அல்லது Codespace இல் அனைத்தையும் அமைக்கும் மாற்றாக [கன்டெய்னர்](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) பயன்படுத்தலாம். குர்ஸ் ரெப்போவில் உள்ள சிறப்பு `.devcontainer` அடைவால் VS Code இணைக்கப்பட்ட கணினியில் திட்டத்தை கன்டெய்னரில் அமைக்க முடியும். Codespaces வெளியிலும் இதற்கு Docker நிறுவல் தேவை, மேலும் கொஞ்சம் சிரமம் இருக்கும். எனவே கன்டெய்னர்களோடு அனுபவமுள்ளவர்களுக்கு மட்டுமே இதனை பரிந்துரைக்கிறோம்.

GitHub Codespaces பயன்படுத்தும் போது உங்கள் API விசைகளை பாதுகாப்பாக வைக்க சிறந்த வழிகளில் ஒன்று Codespace ரகசியங்கள் ஆகும். இதைப் பற்றி அறிய [Codespaces ரகசிய மேலாண்மை](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) வழிகாட்டியைப் பின்பற்றவும்.

## பாடங்கள் மற்றும் தொழில்நுட்ப தேவைகள்

இந்தக் குர்ஸ் 6 கருத்து பாடங்களையும் 6 குறியீடு பாடங்களையும் கொண்டது.

குறியீடு பாடங்களுக்கு, Azure OpenAI சேவையை பயன்படுத்துகிறோம். இந்தக் குறியீடுகளை இயக்க Azure OpenAI சேவைக்கும் API விசைகளுக்கும் அணுகல் வேண்டும். [இந்த விண்ணப்பத்தை பூர்த்தி செய்து](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) அணுகலைக் கேட்கலாம்.

உங்கள் விண்ணப்பம் பரிசீலிக்கப்படுவதை காத்திருக்கையில், ஒவ்வொரு குறியீடு பாடத்துடனும் `README.md` கோப்பில் குறியீடு மற்றும் விளைவுகளைப் பார்க்கலாம்.

## முதன்முறையாக Azure OpenAI சேவையை பயன்படுத்துதல்

Azure OpenAI சேவைக்கான முதன்முறை பயன்பாட்டிற்கு, [Azure OpenAI சேவை வளத்தை உருவாக்கி உடனடி எப்படி பயன்படுத்துவது](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) என்பதைப் படியுங்கள்.

## முதன்முறையாக OpenAI API ஐ பயன்படுத்துதல்

OpenAI API முதன் முறையாகப் பயன்படுத்தினால், [இணைப்பை உருவாக்கி பயன்படுத்துவது](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) குறித்த வழிகாட்டியைப் பின்பற்றவும்.

## மற்ற கற்றுக்கொள்ளுபவர்களை சந்திக்கவும்

நாங்கள் அதிகாரப்பூர்வ [AI Community Discord சேவையகத்தில்](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) மற்ற கற்றுக்கொள்ளுபவர்களை சந்திக்க சந்தைப்படைகள் அமைத்துள்ளோம். இது போன்ற மனப்பான்மையுடைய புதிய தொழிலதிபர்கள், கட்டுநர்கள், மாணவர்கள் மற்றும் Generative AI இல் முன்னேற விரும்புவோருடன் இணைப்பு கொள்ள சிறந்த வாய்ப்பு.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

திட்டக் குழுவும் இந்த Discord சேவையகத்தில் கற்றுக்கொள்ளுபவர்களுக்கு உதவ இருப்பார்கள்.

## பங்களிக்கவும்

இந்தக் குர்ஸ் ஒரு திறந்த மூல முயற்சி. மேம்பாடு தெரிவுகள் அல்லது பிரச்சனைகள் இருப்பின், தயவுசெய்து [Pull Request உருவாக்கவும்](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) அல்லது [GitHub பிரச்சனை பதிவுசெய்க](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

திட்டக் குழு அனைத்து பங்களிப்புக்களையும் கண்காணிக்கும். திறந்த மூலத்தில் பங்களிப்பது Generative AI இல் உங்கள் தொழிலை கட்டியெழுப்ப ஒரு அரிய வழி.

பல பங்களிப்புகள் உங்கள் உரிமையை உறுதிப்படுத்தும் Contributors License Agreement (CLA) ஒப்புதலுக்கு உட்பட்டவை. விரிவாக அறிய [CLA, Contributor License Agreement இணையதளம்](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) பார்வையிடவும்.

முக்கியம்: இந்த ரெப்போவில் உரையை மொழிமாற்றம் செய்யும் போது இயந்திர மொழிபெயர்ப்புகளை பயன்படுத்த வேண்டாம். மொழிபெயர்ப்புகள் சமூகத்துடன் சரிபார்க்கப்படும், எனவே நீங்கள் நன்கு தெரிந்த மொழிகளில் மட்டுமே மொழிபெயர்ப்பு செய்வதற்கு முன்வரவும்.

நீங்கள் ஒரு புல் ரெக்வஸ்ட் சமர்ப்பிக்கும்போது, CLA-bot தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்பதை நிர்ணயம் செய்து புல் ரெக்வஸ்ட்-ஐ சரியான வகையில் அடையாளம் காணச் சுட்டும் (எ.கா. லேபிள், கருத்து). அன்றாடப் படி bot தரும் செயற்கை நடத்தைகளை பின்பற்றவும். இது அனைத்து ரெப்போகளிலும் ஒருமுறை மட்டுமே செய்யவேண்டும்.

இந்தத் திட்டம் [Microsoft திறந்த மூல நடத்தை அட்டவணை](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ஐ ஏற்றுக்கொண்டுள்ளது. மேலதிக விவரங்களுக்கு நடத்தை அட்டவணை FAQ-ஐ படியுங்கள் அல்லது [Email opencode](opencode@microsoft.com) என்ற முகவரிக்கு தொடர்பு கொள்ளவும்.

## வாருங்கள், தொடங்குவோம்!
இந்த பாடத்தை நிறைவு செய்ய தேவையான படிகளை நீங்கள் முடித்துவிட்டீர்கள், தற்போது நாம் ஒரு [உருவாக்கும் செயற்கை நுண்ணறிவு மற்றும் LLM களின் அறிமுகத்துடன்](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) தொடங்குவோம்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற செயற்கை நுண்ணறிவு மொழிபெயர்ப்பு சேவையின் உதவியால் மொழியாக்கம் செய்யப்பட்டதாகும். நாங்கள் துல்லியத்திற்காக முயலினாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து மனதில் கொள்க. அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரபூர்வமான ஆதாரமாக கருதப்பட வேண்டும். முக்கிய தகவல்களுக்கு, நிபுணத்துவமிக்க மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த தவிர்க்கப்பட முடியாத புரிதல் நிலைகள் அல்லது தவறான புரிதல்களுக்கு நாங்கள் பொறுப்பில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->