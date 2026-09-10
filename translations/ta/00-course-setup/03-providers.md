# LLM வழங்குநரை தேர்வு செய்தல் & அமைத்தல் 🔑

பணிகள் **எனினும்** OpenAI, Azure அல்லது Hugging Face போன்ற ஆதரவு வழங்குநர்களின் மூலம் ஒரே அல்லது பல பெரும் மொழி மாதிரி (LLM) உருவாக்கங்கள் மீது வேலை செய்ய உருவாக்கப்படலாம். இவை நமக்கு சரியான प्रमाणங்கள் (API விசை அல்லது டோக்கன்) உடன் நிரல் மூலம் அணுகக்கூடிய _வழங்கப்பட்டி முனையம்_ (API) வழங்குகின்றன. இந்தப் பாடத்தில், இந்த வழங்குநர்களை விவரிக்கின்றோம்:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) பல்வேறு மாதிரிகள் உட்பட முக்கிய GPT தொடர்.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) நிறுவன தயாரார் நோக்கில் OpenAI மாதிரிகள்
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) OpenAI, Meta, Mistral, Cohere, Microsoft மற்றும் பிற நிறுவுநர்களின் நூற்றுக்கணக்கான மாதிரிகளுக்கு ஒரே முனையம் மற்றும் API விசை (GitHub Models ஐ மாற்றுகிறது, அது 2026 ஜூலை முடிவில் ஓய்வு பெறுகிறது)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) துவக்க மூல மாதிரிகள் மற்றும் அறிவுரைக் காரியத் தொகுதி
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) அல்லது [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) நீங்கள் பூரணமாக உங்கள் சொந்த சாதனத்தில் மாதிரிகளை குளவுட் சந்தா இல்லாமல் இயக்க விரும்பினால்

**இந்த பயிற்சிகளுக்கு உங்கள் சொந்த கணக்குகளைப் பயன்படுத்த வேண்டும்**. பணிகள் விருப்பமாக உள்ளதால் நீங்கள் உங்கள் விருப்பத்திற்கு ஏற்ப ஒரோ, அனைத்தோ அல்லது எதுவும் அமைக்கலாம். பதிவு செய்ய சில வழிகாட்டி:

| பதிவு | செலவு | API விசை | விளையாட்டு மேடை | குறிப்புகள் |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [விலை நிர்ணயம்](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [திட்டம் அடிப்படையில்](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [கோடு இல்லாமல், வலை](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | பல மாதிரிகள் கிடைக்கும் |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [விலை நிர்ணயம்](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ஆரம்பம்](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ஸ்டூடியோ ஆரம்பம்](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [முன்கூட்டியே அணுகலுக்கான விண்ணப்பம் அவசியம்](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [விலை நிர்ணயம்](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [திட்ட அறிமுக பக்கம்](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry விளையாட்டு மேடை](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | இலவச நிலை; பல மாதிரி வழங்குநர்களுக்கான ஒரு முனையம் + விசை |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [விலை நிர்ணயம்](https://huggingface.co/pricing) | [அணுகல் டோக்கன்கள்](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatக்கு மிதமான மாதிரிகள் உள்ளன](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | இலவசம் (உங்கள் சாதனத்தில் இயங்கும்) | தேவையில்லை | [உள்ளூர் CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | பூரணமான ஆஃப்லைன், OpenAI-உதவிய முனையம் |
| | | | | |

வெவ்வேறு வழங்குநர்களுடன் இந்த தொகுப்பகம் பயன்படுத்த _கட்டமைக்க_ கீழே உள்ள வழிமுறைகளை பின்பற்றவும். குறிப்பிட்ட வழங்குநரை தேவைப்படும் பணிகளில் அந்த பெயரில் கீழ்காணும் குறிச்சொற்களில் ஒன்று இருக்கும்:

- `aoai` - Azure OpenAI முனையம், விசை தேவை
- `oai` - OpenAI முனையம், விசை தேவை
- `hf` - Hugging Face டோக்கன் தேவை
- `githubmodels` - Microsoft Foundry Models முனையம், விசை தேவை (GitHub Models ஜூலை 2026 முடிவில் ஓய்வு பெறும்)

நீங்கள் ஒரேவொரு வழங்குநர், ஒன்றுமில்லை, அனைத்தையும் அமைக்கலாம். தொடர்புடைய பணிகள் தேவையான प्रमாணங்கள் இல்லாவிட்டால் பிழை நிகழும்.

## `.env` கோப்பை உருவாக்குக

மேலுள்ள வழிகாட்டியின்படி பொருந்தும் வழங்குநருடன் நீங்கள் பதிவு செய்யப்பட்டு தேவையான அங்கீகார प्रमாணங்கள் (API_KEY அல்லது டோக்கன்) பெற்றுள்ளதாக நாம் எண்ணுகிறோம். Azure OpenAI இல், குறைந்தது ஒரு GPT மாதிரி பளிங்கு சாத்தியத்துக்காக Azure OpenAI சேவை (முனையம்) வழங்கப்பட்டிருக்கும் என்றும் நினைக்கின்றோம்.

அடுத்த படி உங்கள் **உள்ளூர் சூழல் மாறிலிகள்** பின்வருமாறு கட்டமைக்கப்பட வேண்டும்:

1. அடிப்படை அடைவில் `.env.copy` என்ற கோப்பை தேடுங்கள், அதில் இதுபோன்ற உள்ளடக்கம் இருக்கும்:

   ```bash
   # OpenAI வழங்குநர்
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## மைக்ரோசாஃப்ட் ஃபவுண்டிரியில் Azure OpenAI
   ## (Azure OpenAI சேவை இப்போது மைக்ரோசாஃப்ட் ஃபவுண்ட்ரியின் பகுதி: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # இயல்பானது அமைக்கப்பட்டுள்ளது! (தற்போதைய நிலையான GA API பதிப்பு)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## மைக்ரோசாஃப்ட் ஃபவுண்ட்ரி மாடல்கள் (பன்முக வழங்குநர் மாடல் பட்டியல், GitHub மாடல்களை மாற்றுகிறது, 2026 ஜூலை இறுதியில் ஓய்வுபெறும்)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ஹக்கிங் பேஸ்
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. கீழ்காணும் கட்டளையை பயன்படுத்தி அந்த கோப்பை `.env` என நகலெடுக்கவும். இந்த கோப்பு _gitignore-ஆகும்_, ரகசியங்கள் பாதுகாக்கப்படுகிறது.

   ```bash
   cp .env.copy .env
   ```

3. அடுத்த பகுதியில் விவரிக்கப்பட்டபடி மதிப்புகளை நிரப்பவும் (`=`-இன் வலது பக்கத்தில் உள்ள இடமாற்றியுள்ளவற்றை மாற்றவும்).

4. (விருப்பம்) நீங்கள் GitHub Codespaces ஐ பயன்படுத்தினால், இந்த தொகுப்பகத்துடன் தொடர்புடைய _Codespaces ரகசியமாக_ சூழல் மாறிலிகளை சேமிக்க வாய்ப்பு உண்டு. அந்த நிலையில், உள்ளூர் .env கோப்பை அமைக்க தேவையில்லை. **ஆனால், இந்த விருப்பம் GitHub Codespaces பயன்படுத்தினால் மட்டுமே வேலை செய்கிறது.** Docker Desktop பயன்படுத்தினாலும் .env கோப்பை நீங்கள் அமைக்கவேண்டும்.

## `.env` கோப்பை நிரப்புக

அவைகளை என்ன உருவாக்கப்படுகிறது என்பதை புரிந்துகொள்ள நாம் மாறிலி பெயர்களைக் கவனிக்கலாம்:

| மாறிலி  | விளக்கம்  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | இது உங்கள் சுயவிவரத்தில் உங்கள் அணுகல் டோக்கன் |
| OPENAI_API_KEY | அச்சாவற்ற OpenAI முனைகளுக்கான சேவை பயன்படுத்தும் அங்கீகாரம் விசை |
| AZURE_OPENAI_API_KEY | அந்த சேவைக்கு அங்கு அங்கீகாரம் விசை |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI வளத்துக்கான முனைய முகவரி |
| AZURE_OPENAI_DEPLOYMENT | _உரை உருவாக்கும்_ மாதிரி வழங்கல் முனைய முகவரி |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _உரை இணைப்புகள்_ மாதிரி வழங்கல் முனைய முகவரி |
| AZURE_INFERENCE_ENDPOINT | உங்கள் Microsoft Foundry திட்டத்திற்கான முனைய முகவரி, Microsoft Foundry மாதிரிகளுக்காகப் பயன்படுத்தப்படுகிறது |
| AZURE_INFERENCE_CREDENTIAL | உங்கள் Microsoft Foundry திட்டத்திற்கான API விசை |
| | |

குறிப்புரை: கடைசி இரண்டு Azure OpenAI மாறிலிகள் உரை உருவாக்கும் (chat completion) மற்றும் வெக்டர் தேடல் (embeddings) க்கான இயல்புநிலை மாதிரியின் பிரதிபலிப்பாகும். அவற்றை அமைக்கும் வழிமுறைகள் தொடர்புடைய பணிகளில் வரையறுக்கப்படும்.

## Azure OpenAI அமைப்பு: போர்டல் மூலம்

> **குறிப்பு:** Azure OpenAI சேவை இப்பொழுது [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) இன் பகுதியாக உள்ளது. வளங்கள் மற்றும் நிறுவல்கள் Azure போர்டலில் தோன்றினாலும், தினசரி மாதிரி மேலாண்மை (நிறுவல்கள், விளையாட்டு மேடை, கண்காணிப்பு) பழைய தனித்த Azure OpenAI ஸ்டூடியோவுக்கு பதிலாக Foundry போர்டலில் நடைபெறும்.

Azure OpenAI முனையம் மற்றும் விசைப் மதிப்பைக் [Azure போர்டல்](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)ல் காணலாம்; அதுவைக் கொண்டு தொடங்குவோம்.

1. [Azure போர்டல்](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) செல்லவும்
1. இடது பக்க மெனுவில் **Keys and Endpoint** விருப்பத்தை கிளிக் செய்யவும்.
1. **Show Keys** என்பதனை கிளிக் செய்யவும் - KEY 1, KEY 2 மற்றும் முனைய முகவரி காண்பிக்கப்படும்.
1. AZURE_OPENAI_API_KEYக்கு KEY 1 மதிப்பைக் கொண்டு பயன்படுத்துங்கள்
1. AZURE_OPENAI_ENDPOINTக்கு முனைய முகவரியைப் பயன்படுத்துங்கள்

அடுத்ததாக, நாம் நிறுவியுள்ள குறிப்பிட்ட மாதிரிகளுக்கான முனைய முகவரிகள் தேவை.

1. Azure OpenAI வளத்தின் இடது பக்க மெனுவில் **Model deployments** விருப்பத்தை கிளிக் செய்யவும்.
1. இலக்கப் பக்கத்தில், **Go to Microsoft Foundry portal** (அல்லது உங்கள் வளத்துக்கு ஏற்ப **Manage Deployments**) கிளிக் செய்யவும்

இது Microsoft Foundry போர்டலைத் திறக்கும், அங்கே நாம் பிற மதிப்புகளை பெறுவோம்.

## Azure OpenAI அமைப்பு: Microsoft Foundry போர்டல் மூலம்

1. மேலே கூறியுள்ளீர்கள் போல் உங்கள் வளத்திலிருந்து [Microsoft Foundry போர்டல்](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) செல்.
1. தற்போது நிறுவியுள்ள மாதிரிகளை காண **Deployments** தாவலை (இடது பக்கம்) கிளிக் செய்யவும்.
1. உங்கள் விருப்பமான மாதிரி நிறுவப்படவில்லை என்றால், [மாதிரி இன்வென்டரி](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) இலிருந்து அதை நிறுவ **Deploy model** ஐ பயன்படுத்தவும்.
1. நீங்கள் _உரை உருவாக்கும்_ மாதிரி தேவை - நாங்கள் பரிந்துரைக்கிறோம்: **gpt-5-mini**
1. நீங்கள் _உரை இணைப்புகள்_ மாதிரி தேவை - பரிந்துரை: **text-embedding-3-small**

இப்போது சூழல் மாறிலிகளை நிறுவலில் பயன்படுத்திய _Deployment name_ இன்படி புதுப்பிக்கவும். பொதுவாக இது மாதிரி பெயருடன் ஒத்திருக்கும், நீங்கள் எடுத்து மாற்றவில்லை என்றால். உதாரணமாக:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**செயலை முடித்த பின் .env கோப்பை சேமிப்பதை மறவாதீர்கள்**. இப்போது கோப்பை மூடி நோட்ட்புக் ஓட படி நடைமுறைகளுக்கு திரும்பலாம்.

## OpenAI அமைப்பு: சுயவிவரத்திலிருந்து

உங்கள் OpenAI API விசை உங்கள் [OpenAI கணக்கில்](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) காணலாம். இல்லையெனில், கணக்கு திறக்கும் மற்றும் API விசை உருவாக்கலாம். விசையை பெற்ற பிறகு `.env` கோப்பில் `OPENAI_API_KEY` மாறிலிக்குள் பதிக்கலாம்.

## Hugging Face அமைப்பு: சுயவிவரத்திலிருந்து

உங்கள் Hugging Face டோக்கன் உங்கள் சுயவிவரத்தில் [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) பகுதியில் காணலாம். இவை பொதுவாக பகிர வேண்டாம். இதற்கான பரிந்துரையாக, இந்தத் திட்டம் பயன்பாட்டிற்கு புதிதாக ஒரு டோக்கன் உருவாக்கி அதை `.env` கோப்பில் `HUGGING_FACE_API_KEY` என்ற மாறிலியில் சேர்க்கவும். _குறிப்பு:_ இது API விசை அல்ல, ஆனாலும் அங்கீகாரம் கொள்ள பயன்படும் என்பதால் ஒரே பெயரிடல் வழக்கம் பின்பற்றப்படுகிறது.

## Microsoft Foundry மாதிரிகள் அமைப்பு: போர்டல் மூலம்

> **குறிப்பு:** GitHub Models ஜூலை 2026 முடிவில் ஓய்வு பெறுகிறது. Microsoft Foundry Models நேரடி மாற்று, அதே இலவச முயற்சி மாதிரி இன்வென்டரி மற்றும் Azure AI Inference SDK / OpenAI SDK அனுபவத்தை வழங்குகிறது.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) சென்று Foundry திட்டம் உருவாக்கவும் (அல்லது திறக்கவும்).
1. [மாதிரி இன்வென்டரி](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) பார்வையிட்டு மாதிரியை (உதாரணம் `gpt-5-mini`) நிறுவவும்.
1. திட்டத்தின் **Overview** பக்கத்தில் இருந்து **முனைய முகவரி** மற்றும் **API விசை** ஐ நகலெடுக்கவும்.
1. இந்த முகவரி `AZURE_INFERENCE_ENDPOINT` மற்றும் விசை `AZURE_INFERENCE_CREDENTIAL` என்ற மாறிலிகளுக்கு `.env` கோப்பில் சேர்க்கவும்.

## ஆஃப்லைன் / உள்ளூர் வழங்குநர்கள்

நீங்கள் குளவுட் சந்தாவைப் பயன்படுத்த விரும்பாவிட்டால், ஒத்த மாதிரிகளை நேரடியாக உங்கள் சொந்த சாதனத்தில் இயக்கலாம்:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft க்கான சாதனத்தில் இயங்கும் மாதிரி. இது சிறந்த செயல்பாட்டு வழங்குநரை தானாகத் தேர்ந்தெடுத்து OpenAI-உருப்படியான முனையத்தை வெளிப்படுத்துகிறது. இந்த பாடத்திற்கான பெரும்பாலான மாதிரி குறியீடுகளை குறைந்த மாற்றத்துடன் பயன்படுத்தலாம். துவங்க [Foundry Local ஆவணத்தை](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) பாருங்கள், அல்லது `winget install Microsoft.FoundryLocal` (விண்டோஸ்) / `brew install microsoft/foundrylocal/foundrylocal` (மெக்) கட்டளையை பயன்படுத்தி நிறுவவும்.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral மற்றும் Gemma போன்ற திறந்த மாதிரிகளை உள்ளூரிலேயே இயக்க விமான பிரபல மாற்று.


இரு விருப்பங்களையும் பயன்படுத்தி கைமுறை எடுத்துக்காட்டுகளுக்கு [பாடம் 19: SLMகளுடன் கட்டமைத்தல்](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ஐப் பார்க்கவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->