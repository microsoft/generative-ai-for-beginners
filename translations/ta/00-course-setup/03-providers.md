# ஒரு LLM வழங்கியவரை தேர்வு செய்வதும் கட்டமைக்கும் செயல்முறையும் 🔑

பணிகள் **ஆஆக** ஒரு அல்லது அதற்கு மேற்பட்ட பெரிய மொழி மாதிரிகள் (LLM) அமர்வுகள் மூலம் ஆதரிக்கப்படும் சேவை வழங்கியவர்களால் (OpenAI, Azure அல்லது Hugging Face ஆகியவற்றைப் போன்ற) செயல்பட அமைக்கப்படலாம். இவை ஒரு _வழங்கப்பட்ட இடைமுகத்தை_ (API) வழங்குகின்றன, அதனை சரியான அங்கீகார சேர்க்கைகளுடன் (API விசை அல்லது டோக்கன்) நிரல்பூர்வமாக அணுக முடியும். இந்த பாடத்திட்டத்தில், இந்த வழங்கியவர்களைப் பற்றி பேசி வருகிறோம்:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) பல்வேறு மாதிரிகளுடன், அதில் மையமான GPT தொடரும் உள்ளது.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI மாதிரிகளுக்கு, தொழில்துறை தயாராகத்தன்மையுடன்
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) உடன் ஒரே இடைமுகம் மற்றும் API விசை மூலம் OpenAI, Meta, Mistral, Cohere, Microsoft மற்றும் இன்னத்தனுடன் நூற்றுக்கணக்கான மாதிரிகளுக்கு அணுகல் (GitHub Models ஐ மாற்றுகிறது, அது 2026 ஜூலை இறுதியில் ஓய்வு பெறுகிறது)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) திறந்த மூல மாதிரிகளுக்கும் கருத்தாய்வு சேவைக்கும்
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) அல்லது [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), உங்கள் சாதனத்தில் முழுமையாக ஆஃப்லைனில் மாதிரிகளை இயக்க விரும்பினால், எந்த கிளவுட் சந்தா தேவையுமில்லை

**இந்த பயிற்சிகளுக்கு நீங்கள் உங்கள் சொந்த கணக்குகளைப் பயன்படுத்த வேண்டும்**. பணிகள் விருப்பமானவை, எனவே நீங்கள் ஒருவேளை, எல்லாவற்றையும், அல்லது எதுவும் செய்யாமல், உங்கள் விருப்பப்படி வழங்கியவர்களை அமைக்க முடியும். பதிவு செய்வதற்கான சில வழிகாட்டல்கள்:

| பதிவு | கட்டணம் | API விசை | விளையாட்டு இடம் | கருத்துக்கள் |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [கட்டண விவரம்](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [திட்ட அடிப்படையிலான](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [கோடில்லாதது, வலை](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | பல மாதிரிகள் கிடைக்கும் |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [கட்டண விவரம்](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK துவக்கம்](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ஸ்டுடியோ துவக்கம்](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [அணுகலுக்கு முன்பாக விண்ணப்பிக்க வேண்டும்](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [கட்டண விவரம்](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [திட்ட மேற்பார்வை பக்கம்](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry விளையாட்டு இடம்](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | இலவச நிலை கிடைக்கும்; பல மாதிரி வழங்கியவர்களுக்கு ஒரு இடைமுகம் + விசை |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [கட்டண விவரம்](https://huggingface.co/pricing) | [அணுகல் டோக்கன்கள்](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatக்கு வரம்பான மாதிரிகள் உள்ளன](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | இலவசம் (உங்கள் சாதனத்தில் இயங்கும்) | தேவையில்லை | [உள்ளூர் CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | முழுமையாக ஆஃப்லைன், OpenAI-உரிய இடைமுகம் |
| | | | | |

இந்த களஞ்சியத்தை வேறு வழங்கியர்களுடன் பயன்பாட்டுக்கு _கட்டமைக்க_ கீழ்காணும் வழிமுறைகளை பின்பற்றவும். குறிப்பிட்ட வழங்கியோரை தேவைப்படுத்தும் பணிகளில் அந்த வழங்கியவரின் குறியீடு பெயரில் காணப்படும்:

- `aoai` - Azure OpenAI இடைமுகம், விசை தேவை
- `oai` - OpenAI இடைமுகம், விசை தேவை
- `hf` - Hugging Face டோக்கன் தேவை
- `githubmodels` - Microsoft Foundry Models இடைமுகம், விசை தேவை (GitHub Models 2026 ஜூலை இறுதியில் ஓய்வு பெறுகிறது)

நீங்கள் ஒருவேளை, எதுவும் இல்லாமல் அல்லது அனைத்து வழங்கியவர்களையும் அமைக்க முடியும். சம்பந்தப்பட்ட பணிகள் அங்கீகாரச் சான்றிதழ்கள் இல்லாமல் பிழை விடுத்து நிறுத்தப்படும்.

## `.env` கோப்பை உருவாக்குதல்

நீங்கள் மேலே கொடுக்கப்பட்ட வழிகாட்டலை ஏற்கனவே படித்து, சம்பந்தப்பட்ட வழங்கியவருடன் பதிவு செய்துள்ளீர்கள் என்று நம்புகிறோம். தேவையான அங்கீகாரச் சான்றுகளை (API_KEY அல்லது டோக்கன்) பெற்றிருக்க வேண்டும். Azure OpenAI வேறு, ஒரு Azure OpenAI சேவை (இடைமுகம்) ஆனது நன்கு அமர்ந்திருக்கும் மற்றும் குறைந்தது ஒரு GPT மாதிரி அரட்டை முடிப்புக்காக இயக்கப்பட வேண்டும் என்று எடுத்துக்கொள்கிறோம்.

அடுத்து உங்கள் **உள்ளூர் சூழல் மாறிலிகளை** கீழ்வருமாறு அமைக்க வேண்டும்:

1. ருட் கோப்புறையில் `.env.copy` என்ற கோப்பை தேடவும், அதில் பின்வரும் போன்ற உள்ளடக்கம் இருக்கும்:

   ```bash
   # OpenAI வழங்குநர்
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry-இல் Azure OpenAI
   ## (Azure OpenAI சேவை şimdi Microsoft Foundry இன் ஒரு பகுதியாக உள்ளது: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # முன்னமைவு அமைக்கப்பட்டுள்ளது! (தற்போதைய நிலையான GA API பதிப்பு)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry மாதிரிகள் (பல வழங்குநர் மாதிரி सूची, GitHub மாதிரிகளை மாற்றுகிறது, அது ஜூலை 2026 முடிவில் ஓய்வாகும்)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. கீழ்காணும் கட்டளை மூலம் அந்த கோப்பை `.env` ஆக நகலெடுக்கவும். இக்கோப்பு _gitignore-செய்யப்பட்ட_ ஆகும், இது ரகசியங்களை பாதுகாக்க உதவும்.

   ```bash
   cp .env.copy .env
   ```

3. மதிப்புகளை (`=` வலது பகுதி உள்ள மாறிலி பெயர்களை) அடுத்த பகுதியில் விளக்கப்பட்டதைப் போல நிரப்பவும்.

4. (விருப்பம்) GitHub Codespaces பயன்படுத்தினால், இந்தக் களஞ்சியத்துடன் தொடர்புடைய Codespaces ரகசியங்களாக சூழல் மாறிலிகளைச் சேமிக்க முடியும். அதனால் உள்ளூர் `.env` கோப்பை அமைக்க தேவையில்லை. **ஆனால், இந்த விருப்பம் GitHub Codespaces பயன்படுத்தும் போது மட்டும் வேலை செய்கிறது என்பதை கவனிக்கவும். Docker Desktop பயன்படுத்தினால் `.env` கோப்பை அமைக்கவேண்டும்.**

## `.env` கோப்பை நிரப்புதல்

மாறிலி பெயர்களை விரைவாகப் பார்ப்போம், அவை எதை குறிக்கின்றன என்பதை புரிந்துகொள்ள:

| மாறிலி  | விளக்கம்  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | உங்கள் சுயவிவரத்தில் அமைந்துள்ள பயனர் அணுகல் டோக்கன் |
| OPENAI_API_KEY | Azure OpenAI அல்லாத இடைமுகங்களுக்கு சேவையை பயன்படுத்த அங்கீகார விசை |
| AZURE_OPENAI_API_KEY | அந்த சேவையைப் பயன்படுத்த அங்கீகார விசை |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI வளத்துக்கான இடைமுகம் |
| AZURE_OPENAI_DEPLOYMENT | _எழுத்து தலைமுறை_ மாதிரி அமர்வு இடைமுகம் |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _எழுத்து உள்ளளவை_ மாதிரி அமர்வு இடைமுகம் |
| AZURE_INFERENCE_ENDPOINT | உங்கள் Microsoft Foundry திட்டத்திற்கான இடைமுகம், Microsoft Foundry Models பயன்படுத்தப்படுகிறது |
| AZURE_INFERENCE_CREDENTIAL | உங்கள் Microsoft Foundry திட்டத்திற்கான API விசை |
| | |

குறிப்பு: கடைசி இரண்டு Azure OpenAI மாறிலிகள் உரையாடல் முடிப்புக்கான இயல்பு மாதிரி (எழுத்து தலைமுறை) மற்றும் வேக்டர் தேடல் (உள்ளளவு) க்கு தொடர்புடையவை. அவற்றை அமைப்பதற்கான வழிமுறைகள் சம்பந்தப்பட்ட பணிகளில் குறிப்பிடப்படும்.

## Azure OpenAI அமைப்புகள்: போர்டல் வழியாக

> **குறிப்பு:** Azure OpenAI சேவை தற்போது [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) இற்குள் உள்ளது. வளங்கள் மற்றும் அமர்வுகள் இன்னும் Azure போர்டலில் காணப்படுகின்றன, ஆனால் மாதிரி மேலாண்மை (அமர்வுகள், விளையாட்டு இடம், கண்காணிப்பு) இப்போது புராணமான தனியாக இருக்கும் "Azure OpenAI Studio"யை தவிர, Foundry போர்டலில் நடைபெறுகிறது.

Azure OpenAI இடைமுக மற்றும் விசை மதிப்புகள் [Azure போர்டல்](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) யில் கிடைக்கும், அதில் ஆரம்பிப்போம்.

1. [Azure போர்டல்](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) செல்
1. இடது பட்டியில் உள்ள **Keys and Endpoint** தேர்வை கிளிக் செய்க
1. **Show Keys** கிளிக் செய்க - KEY 1, KEY 2 மற்றும் இடைமுகம் காணப்பட வேண்டும்
1. KEY 1 மதிப்பை AZURE_OPENAI_API_KEY க்கு பயன்படுத்தவும்
1. இடைமுக மதிப்பை AZURE_OPENAI_ENDPOINT க்கு பயன்படுத்தவும்

அடுத்து, நாங்கள் அமர்த்திய குறிப்பிட்ட மாதிரிகளுக்கான இடைமுகங்கள் தேவை.

1. Azure OpenAI வளத்தின் இடது பட்டியில் **Model deployments** தேர்வு செய்க.
1. இலக்க சென்ற பக்கத்தில் **Go to Microsoft Foundry portal** (அல்லது **Manage Deployments**, உங்கள் வளத்தின் அடிப்படையில்) கிளிக் செய்க

இது Microsoft Foundry போர்டலை திறக்கும், அங்கே நாங்கள் மற்ற மதிப்புக்களை கீழ்காணும் படி காண்போம்.

## Azure OpenAI அமைப்புகள்: Microsoft Foundry போர்டல் வழியாக

1. [Microsoft Foundry போர்டல்](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **உங்கள் வளத்திலிருந்து** சென்றடையவும்
1. இடது பட்டியில் உள்ள **Deployments** தாவலை கிளிக் செய்து தற்போதைய மாதிரிகளைப் பார்வையிடுக
1. உங்கள் விருப்பமான மாதிரி இனி அமர்த்தப்படவில்லை என்றால், [மாதிரி பட்டியல்](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) இலிருந்து அதை அமர்த்த **Deploy model** பயன்படுத்தவும்
1. நீங்கள் _எழுத்து தலைமுறை_ மாதிரியை வேண்டும் - நாம் பரிந்துரைக்கிறோம்: **gpt-4o-mini**
1. நீங்கள் _எழுத்து உள்ளளவு_ மாதிரியை வேண்டும் - பரிந்துரைக்கப்படுகிறது **text-embedding-3-small**

இப்போது, அவர்களால் பயன்படுத்தப்படும் _Deployment name_-ஐ பிரதிபலிக்கும் வகையில் சூழல் மாறிலிகளை புதுப்பிக்கவும். இது பொதுவாக மாதிரி பெயருடன் சமமாக இருக்கும், நீங்கள் மாற்றவில்லை என்றால். உதாரணமாக:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**முடிந்ததும் .env கோப்பை சேமிப்பதை மறக்கவேண்டாம்**. இப்போது கோப்பை மூடி குறிப்புகள் காணும் பக்கத்திற்கு திரும்பலாம்.

## OpenAI அமைப்புகள்: கணக்கில் இருந்து

உங்கள் OpenAI API விசை உங்கள் [OpenAI கணக்கில்](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) காணலாம். ஒன்று இல்லையெனில், நீங்கள் சொந்த கணக்கை பதிவு செய்து API விசையை உருவாக்கலாம். இதற்கு பிறகு, `.env` கோப்பில் `OPENAI_API_KEY` மாறிலி நிரப்பப்படலாம்.

## Hugging Face அமைப்புகள்: சுயவிவரத்தில் இருந்து

உங்கள் Hugging Face டோக்கன் உங்கள் சுயவிவரத்தில் உள்ள [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) பகுதியில் கிடைக்கும். இதுகளை பொது இடங்களில் பகிர வேண்டாம். பதிலுக்கு, இந்த திட்ட பயன்பாட்டிற்கு புதிய டோக்கனை உருவாக்கி `.env` கோப்பில் `HUGGING_FACE_API_KEY` என்ற மாறிலியில் நகலெடுக்கவும். _குறிப்பு:_ இது தொழில்நுட்பமாக API விசை அல்ல, ஆனால் அங்கீகாரம் பெற பயன்படுத்தப்படுகிறது எனவே ஒரே பெயரிடல் நிலையை பராமரிக்கின்றோம்.

## Microsoft Foundry Models அமைப்புகள்: போர்டல் வழியாக

> **குறிப்பு:** GitHub Models 2026 ஜூலை இறுதியில் ஓய்வு பெறுகிறது. Microsoft Foundry Models நேரடி மாற்றாக உள்ளது, அதே இலவச-சோதனை மாதிரி பட்டியலும் Azure AI Inference SDK / OpenAI SDK அனுபவமும் வழங்குகிறது.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) சென்று Foundry திட்டத்தை உருவாக்கவும் (அல்லது திறக்கவும்).
1. [மாதிரி பட்டியல்](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) பார்வையிட்டு மாதிரியை (உதாரணமாக `gpt-4o-mini`) அமர்த்தவும்.
1. திட்டத்தின் **மேற்பார்வை** பக்கத்தில் இருந்து **இடைமுகம்** மற்றும் **API விசை** நகலெடுக்கவும்.
1. `.env` கோப்பில் `AZURE_INFERENCE_ENDPOINT` க்கு இடைமுக மதிப்பை, `AZURE_INFERENCE_CREDENTIAL` க்கு விசை மதிப்பை பயன்படுத்தவும்.

## ஆஃப்லைன் / உள்ளூர் வழங்கியவர்கள்

நீங்கள் முழுமையாக கிளவுட் சந்தா பயன்படுத்த விரும்பவில்லை என்றால், நீங்கள் இணக்கமான திறந்த மாதிரிகளை நேரடியாக உங்கள் சாதனத்தில் இயக்கலாம்:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft வழங்கும் சாதனத்தில் இயங்கும் விரும்பக்கூடிய செயலி. இது சிறந்த செயல்முறையாளரை (NPU, GPU, அல்லது CPU) தானாக தேர்வு செய்து OpenAI-போன்ற இடைமுகத்தை வெளிப்படுத்துகிறது, எனவே இந்தப் பாடத்திட்டத்தில் உள்ள சிறுபிரதிகள் மிகக் குறைந்த மாற்றங்களுடன் மீண்டும் பயன்படலாம். ஆரம்பிக்க [Foundry Local ஆவணத்தைக்](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) காணவும், அல்லது `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ஆகியவற்றை நிறுவவும்.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral மற்றும் Gemma போன்ற திறந்த மாதிரிகளை உள்ளூர் இயக்குவதற்கான பிரபல மாற்று.


இரு விருப்பங்களையும் பயன்படுத்தி நடைமுறை எடுத்துக்காட்டுகளை காட்சிப்படுத்த [பாடம் 19: SLMs உடன் கட்டல்](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ஐப் பார்க்கவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->