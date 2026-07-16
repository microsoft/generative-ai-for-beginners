# ഒരു LLM പ്രൊവൈഡറെ തിരഞ്ഞെടുക്കൽ & കോൺഫിഗർ ചെയ്യൽ 🔑

അസൈൻമെന്റുകൾ **ശേഷിക്കുന്നോ** ഒരോ-അധികം വലിയ ഭാഷാ മോഡൽ (LLM) വിന്യാസങ്ങളോടൊപ്പം പ്രവർത്തിക്കാൻ ഒരു പിന്തുണയുള്ള സേവന പ്രൊവൈഡർ പോലെ OpenAI, Azure അല്ലെങ്കിൽ Hugging Face വഴി സജ്ജീകരിക്കാം. ഇവ ഒരു _ഹോസ്റ്റുചെയ്ത ഹെൻഡ്‌പോയിന്റ്_ (API) ഒരുക്കുന്നു, അതിൽനിന്ന് നാം ശരിയായ ക്രെഡൻഷ്യലുകൾ (API കീ അല്ലെങ്കിൽ ടോക്കൺ) ഉപയോഗിച്ച് പ്രോഗ്രാമാറ്റിക്കായി ആക്‌സസ് ചെയ്യാം. ഈ കോഴ്സിൽ, നാം ഈ പ്രൊവൈഡർമാരെ ചർച്ച ചെയ്യും:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) വിവിധ മോഡലുകൾ ഉൾപ്പെടെ കോർ GPT പരമ്പര.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI മോഡലുകൾ എന്റർപ്രൈസ് റെഡീനസ് മുൻനിർത്തി
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ഒറ്റ ഹെൻഡ്‌പോയിന്റും API കീയും ഉപയോഗിച്ച് OpenAI, Meta, Mistral, Cohere, Microsoft തുടങ്ങിയവയിൽ നിന്ന് നൂറിലവരെ മോഡലുകൾ ആക്‌സസ് ചെയ്യാം (GitHub മോഡലുകൾ മാറ്റം വരുത്തുന്നു, ജൂളി 2026 അവസാനം റിട്ടയർ ചെയ്യുന്നു)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) open-source മോഡലുകൾക്കും ഇൻഫറൻസ് സെർവർക്കും
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) നിങ്ങൾക്ക് മോഡലുകൾ പൂർണമായും ഓഫ്‌ലൈൻ നിങ്ങളുടെ സ്വന്തം ഉപകരണത്തിൽ നടത്തണമെങ്കിൽ, ക്ലൗഡുകൾ സബ്സ്ക്രിപ്ഷൻ ആവശ്യമില്ല

**ഈ അഭ്യാസങ്ങൾക്കായി നിങ്ങൾക്ക് നിങ്ങളുടെ സ്വന്തം അക്കൗണ്ടുകൾ ഉപയോഗിക്കേണ്ടതുണ്ട്**. അസൈൻമെന്റുകൾ ഓപ്ഷണൽ ആണ്, അതിനാൽ നിങ്ങൾക്ക് ഒരു പ്രൊവൈഡർ, എല്ലാ പ്രൊവൈഡർമാരോ - അല്ലെങ്കിൽ ഒന്നും - സജ്ജീകരിക്കാം നിങ്ങളുടെ താല്പര്യങ്ങൾ അനുസരിച്ച്. സൈൻ അപ്പ് ചെയ്യുന്നതിനുള്ള ചില മാർഗനിർദ്ദേശങ്ങൾ:

| സൈൻ അപ്പ് | ചെലവ് | API കീ | പ്ലേഗ്രൌണ്ട് | അഭിപ്രായങ്ങൾ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [മൂല്യനിർണയം](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [പ്രോജക്ട് അധിഷ്ഠിതം](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [നോ-കോഡ്, വെബ്](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | പല മോഡലുകളും ലഭ്യമാണ് |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [മൂല്യനിർണയം](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ക്വിക്ക്‌സ്റ്റാർട്ട്](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [സ്റ്റുഡിയോ ക്വിക്ക്‌സ്റ്റാർട്ട്](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ആക്‌സസ് ലഭിക്കാൻ മുൻകൂർ അപേക്ഷ ആവശ്യമാണ്](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [മൂല്യനിർണയം](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [പ്രോജക്റ്റ് അവലോകന പേജ്](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry പ്ലേഗ്രൗണ്ട്](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ഫ്രീ ടിയർ ലഭ്യമാണ്; പല മോഡൽ പ്രൊവൈഡർമാർക്കും ഒറ്റ ഹെൻഡ്‌പോയിന്റും കീയും |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ചെലവ്](https://huggingface.co/pricing) | [ആക്‌സസ് ടോക്കൺസ്](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat-ക്ക് പരിമിതമായ മോഡലുകൾ ഉണ്ട്](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ഫ്രീ (നിങ്ങളുടെ ഉപകരണത്തിൽ പ്രവർത്തിക്കുന്നു) | ആവശ്യമില്ല | [ലോകൽ CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | പൂർണമായും ഓഫ്‌ലൈൻ, OpenAI-സഹജമായ ഹെൻഡ്‌പോയിന്റ് |
| | | | | |

വിവിധ പ്രൊവൈഡർമാരുമായി ഈ റെപ്പോസിറ്ററി _കോൺഫിഗർ_ ചെയ്യാൻ താഴെ നൽകിയിരിക്കുന്ന മാർഗ്ഗനിർദ്ദേശങ്ങൾ അനുസരിക്കുക. ഒരു പ്രത്യേക പ്രൊവൈഡർ ആവശ്യമായ അസൈൻമെന്റുകൾ ഫയലിന്റെ പേരിൽ ഈ ടാഗുകളിൽ ഒന്നോ കൂടുതലോ ഉണ്ടായിരിക്കും:

- `aoai` - Azure OpenAI ഹെൻഡ്‌പോയിന്റും കീയും ആവശ്യമാണ്
- `oai` - OpenAI ഹെൻഡ്‌പോയിന്റും കീയും ആവശ്യമാണ്
- `hf` - Hugging Face ടോക്കൺ ആവശ്യമാണ്
- `githubmodels` - Microsoft Foundry Models ഹെൻഡ്‌പോയിന്റും കീയും ആവശ്യമാണ് (GitHub മോഡലുകൾ 2026 ജൂലൈ അവസാനം റിട്ടയർ ചെയ്യുന്നു)

നിങ്ങൾക്ക് ഒരു പ്രൊവൈഡർ, ഒന്നും അല്ലെങ്കിൽ എല്ലാം കോൺഫിഗർ ചെയ്യാം. അനുബന്ധ അസൈൻമെന്റുകൾ ക്രെഡൻഷ്യലുകൾക്കില്ലാത്ത പക്ഷം എറർ കാണിക്കും.

## `.env` ഫയൽ സൃഷ്ടിക്കുക

നിങ്ങൾക്ക് മേൽ പറഞ്ഞ മാർഗ്ഗനിർദ്ദേശം വായിച്ച് ബന്ധപ്പെട്ട പ്രൊവൈഡറിൽ സൈൻ അപ്പ് ചെയ്ത് ആവശ്യമായ അതെന്റിക്കേഷൻ ക്രെഡൻഷ്യലുകൾ (API_KEY അല്ലെങ്കിൽ ടോക്കൺ) ലഭിച്ചു എന്ന് നമുക്ക് ഊഹിക്കാം. Azure OpenAI യുടെ കാര്യത്തിൽ, ഒരു Azure OpenAI സേവന (ഹെൻഡ്‌പോയിന്റ്) വാലിഡായി വിന്യസിച്ചിരിക്കുന്നു, ചാറ്റ് പൂര്‍ത്തീകരണത്തിനായി കുറഞ്ഞത് ഒരു GPT മോഡൽ വിന്യസിച്ചിരിക്കണം.

അടുത്ത് പോകേണ്ടത് നിങ്ങളുടെ **ലോകൽ എൻവയിറൺമെന്റ് വേരിയബിളുകൾ** ഇപ്രകാരം കോൺഫിഗർ ചെയ്യുക:

1. റൂട്ടു ഫോൾഡറിൽ `.env.copy` ഫയൽ കാണുക, ഇതിൽ ഉള്ളടക്കം ഇപ്രകാരം കാണാം:

   ```bash
   # OpenAI പ്രൊവൈഡർ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയിലേയ്ക്ക് Azure OpenAI
   ## (Azure OpenAI സേവനം ഇപ്പോൾ മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയുടെ ഭാഗമാണ്: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ഡിഫോൾട്ട് സെറ്റ് ചെയ്തിട്ടുണ്ട്! (നിലവിലെ സ്ഥിരമായ GA API പതിപ്പ്)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറി മോഡലുകൾ (മൾട്ടി-പ്രൊവൈഡർ മോഡൽ കാറ്റലോഗ്, GitHub മോഡലുകൾ മാറുന്നു, 2026 ജൂലൈ അവസാനത്തോടെ വിരമിക്കും)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. താഴെ നൽകിയ കമാൻഡ് ഉപയോഗിച്ച് ആ ഫയൽ `.env` ആയി കോപ്പി ചെയ്യുക. ഇത് _gitignore_-ൽ ഉൾപ്പെടുത്തിയതാണ്, രഹസ്യങ്ങൾ സുരക്ഷിതമായി സൂക്ഷിക്കുന്നതിന്.

   ```bash
   cp .env.copy .env
   ```

3. അതിനുള്ള ഡാറ്റ റൈറ്റ് സൈഡിലെ പ്ലേസ്ഹോൾഡറുകൾ മാറ്റി പൂരിപ്പിക്കുക, അടുത്ത സെക്ഷനിൽ വിശദീകരിച്ചിരിക്കുന്ന പ്രകാരം.

4. (ഓപ്ഷണൽ) നിങ്ങൾ GitHub Codespaces ഉപയോഗിച്ചാൽ, ഈ റെപ്പോസിറ്ററിക്ക് ബന്ധപ്പെടുന്ന _Codespaces രഹസ്യങ്ങൾ_ ആയി എൻവയിറൺമെന്റ് വേരിയബിളുകൾ സംഭരിക്കാൻ കഴിയും. അപ്പോൾ നിങ്ങൾക്ക് ലോകൽ .env ഫയൽ സജ്ജീകരിക്കേണ്ടതില്ല. **എന്നിരുന്നാലും, ഈ ഓപ്ഷൻ GitHub Codespaces മാത്രം പ്രയോഗിക്കുന്നവർക്കാണ്.** Docker Desktop ഉപയോഗിച്ചാൽ .env ഫയൽ എപ്പോഴും സജ്ജീകരിക്കേണ്ടതാണ്.

## `.env` ഫയൽ പൂരിപ്പിക്കുക

വ്യാരിയബിൾ നാമങ്ങൾ എന്തിനെ പ്രമാണിക്കുന്നുവെന്ന് പരിചയപ്പെടാം:

| വ്യാരിയബിൾ  | വിവരണം  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | നിങ്ങൾ നിങ്ങളുടെ പ്രൊഫൈൽ ഇൽ സജ്ജമാക്കിയ istifadə erişim ടോക്കൺ |
| OPENAI_API_KEY | നോൺ Azure OpenAI ഹെൻഡ്‌പോയിന്റുകൾ ഉപയോഗിക്കാൻ സർവീസിന്റെ ഓണുമതി കീ |
| AZURE_OPENAI_API_KEY | ആ സർവീസിന്റെ ഓണുമതി കീ |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI റിസോർസിന് വിന്യസിച്ച ഹെൻഡ്‌പോയിന്റ് |
| AZURE_OPENAI_DEPLOYMENT | _ടെക്സ്റ്റ് ജനറേഷൻ_ മോഡൽ വിന്യാസ ഹെൻഡ്‌പോയിന്റ് |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _ടെക്സ്റ്റ് എംബെഡിംഗ്സ്_ മോഡൽ വിന്യാസ ഹെൻഡ്‌പോയിന്റ് |
| AZURE_INFERENCE_ENDPOINT | നിങ്ങളുടെ Microsoft Foundry പ്രോജക്റ്റിനു വേണ്ടി, Microsoft Foundry മോഡലുകൾക്കുള്ള ഹെൻഡ്‌പോയിന്റ് |
| AZURE_INFERENCE_CREDENTIAL | നിങ്ങളുടെ Microsoft Foundry പ്രോജക്റ്റിനുള്ള API കീ |
| | |

ശ്രദ്ധിക്കുക: അവസാന രണ്ട് Azure OpenAI വ്യാരിയബിൾസ് ചാറ്റ് പൂർത്തീകരണത്തിനുള്ള (ടെക്സ്റ്റ് ജനറേഷൻ) ഡിഫോൾട്ട് മോഡൽചെയ്യലും വെക്‌ടർ തിരയലിന്റെ (എംബെഡിംഗ്സ്) വിവരങ്ങളും പ്രതിഫലിപ്പിക്കുന്നു. അവയെ സജ്ജമാക്കാനുള്ള നിർദ്ദേശങ്ങൾ ബന്ധപ്പെട്ട അസൈൻമെന്റുകളിൽ നൽകും.

## Azure OpenAI കോൺഫിഗർ ചെയ്യൽ: പോർട്ടലിൽ നിന്നും

> **ശ്രദ്ധിക്കുക:** Azure OpenAI സേവനം ഇപ്പോൾ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)യുടെ ഭാഗമായി മാറിയിരിക്കുന്നു. റിസോഴ്‌സുകളും വിന്യാസങ്ങളും Azure പോർട്ടലിൽ കാണിക്കും, എന്നാൽ ദിവസേന മോഡൽ മാനേജ്മെന്റ് (വിന്യാസങ്ങൾ, പ്ലേഗ്രൗണ്ട്, മോണിറ്ററിംഗ്) ഇപ്പോൾ പഴയ സ്റ്റാൻഡ്അലോൺ "Azure OpenAI Studio"ക്ക് പകരം Foundry പോർട്ടലിൽ നടക്കുന്നു.

Azure OpenAI ഹെൻഡ്‌പോയിന്റും കീസും [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)ൽ ലഭിക്കും, അതിനാൽ അവിടെനിന്ന് തുടക്കമിടാം.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) സന്ദർശിക്കുക
1. സൈഡ്ബാറിൽ (ഇടത്തെ മെനു) **കീസ് ആൻഡ് ഹെൻഡ്‌പോയിന്റ്** ഓപ്ഷൻ ക്ലിക്ക് ചെയ്യുക.
1. **കീസ് കാണിക്കുക** ക്ലിക്ക് ചെയ്യുക - KEY 1, KEY 2, Endpoint എന്നിവ കാണണം.
1. KEY 1 മൂല്യം AZURE_OPENAI_API_KEY ആയി ഉപയോഗിക്കുക
1. Endpoint മൂല്യം AZURE_OPENAI_ENDPOINT ആയി ഉപയോഗിക്കുക

തുടർന്ന്, നാം വിന്യസിച്ച مخصوص മോഡലുകൾക്കുള്ള ഹെൻഡ്‌പോയിന്റുകൾ ആവശ്യമുണ്ട്.

1. Azure OpenAI റിസോഴ്‌സിന് സൈഡ്ബാറിൽ (ഇടത്തെ മെനു) **Model deployments** ഓപ്ഷൻ ക്ലിക്കുക.
1. ഡെസ്റ്റിനേഷൻ പേജിൽ **Go to Microsoft Foundry portal** ( അല്ലെങ്കിൽ **Manage Deployments**, നിങ്ങളുടെ റിസോഴ്‌സ് ടൈപ്പിന്റെ അവസ്ഥപ്രകാരം) ക്ലിക്ക് ചെയ്യുക

ഇത് നിങ്ങളെ Microsoft Foundry പോർട്ടലിലേക്ക് കൊണ്ടുപോകും, അവിടെ നാം താഴെ വിവരിക്കുന്ന മറ്റു മൂല്യങ്ങൾ കാണാം.

## Azure OpenAI കോൺഫിഗർ ചെയ്യൽ: Microsoft Foundry പോർട്ടലിൽ നിന്നും

1. മുകളിൽ പറഞ്ഞതുപോലെ നിങ്ങളുടെ റിസോഴ്‌സിൽ നിന്നും [Microsoft Foundry പോർട്ടൽ](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) വഴി പ്രവേശിക്കുക.
1. നിലവിൽ വിന്യസിച്ച മോഡലുകൾ കാണാൻ സൈഡ്ബാറിൽ (ഇടത്ത്) **Deployments** ടാബ് ക്ലിക്ക് ചെയ്യുക.
1. നിങ്ങളുടെ അഭിലഷിത മോഡൽ വിന്യസിച്ചിട്ടില്ലെങ്കിൽ, [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) മുതലെടുക്കാൻ **Deploy model** ഉപയോഗിക്കുക.
1. നിങ്ങൾക്ക് _ടെക്സ്റ്റ് ജനറേഷൻ_ മോഡൽ ആവശ്യമുണ്ട് - നാം ശുപാർശ ചെയ്യുന്നത്: **gpt-4o-mini**
1. നിങ്ങൾക്ക് _ടെക്സ്റ്റ് എംബെഡിംഗ്_ മോഡൽ ആവശ്യമുണ്ട് - നാം ശുപാർശ ചെയ്യുന്നത് **text-embedding-3-small**

ഇപ്പോൾ എൻവയിറൺമെന്റ് വേരിയബിളുകൾ _Deployment name_ അനുസരിച്ച് അപ്ഡേറ്റ് ചെയ്യുക. സാധാരണയായി മോഡൽ നാമം തന്നെയായിരിക്കും, നിങ്ങൾexplicit ആയി മാറ്റിയിട്ടില്ലെങ്കിൽ. ഉദാഹരണമായി, ഇതിനു ശേഷം നിങ്ങൾക്ക് ഇങ്ങനെ ഉണ്ടായിരിക്കാം:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**ശേഷം .env ഫയൽ സംഭരിക്കാൻ മടങ്ങാതെ മറക്കേണ്ടതാണ്**. നിങ്ങൾക്ക് ഇപ്പോൾ ഫയൽ വിടുക, നോട്ട്‌ബുക്ക് പ്രവർത്തിപ്പിക്കുന്നതിനുള്ള നിർദ്ദേശങ്ങളിലേയ്ക്ക് മടങ്ങുക.

## OpenAI കോൺഫിഗർ ചെയ്യൽ: പ്രൊഫൈൽ വഴിയുള്ള

നിങ്ങളുടെ OpenAI API കീ നിങ്ങളുടെ [OpenAI അക്കൗണ്ടിൽ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) കാണാം. എല്ലാ കാരണമുള്ളവർക്കും അക്കൗണ്ട് സൈൻ അപ്പ് ചെയ്ത് API കീ സൃഷ്ടിക്കാം. കീ ലഭിച്ചതിന് ശേഷം, `.env` ഫയലിലെ `OPENAI_API_KEY` വ്യാരിയബിൾ പൂരിപ്പിക്കാൻ ഉപയോഗിക്കാം.

## Hugging Face കോൺഫിഗർ ചെയ്യൽ: പ്രൊഫൈൽ വഴിയുള്ള

നിങ്ങളുടെ Hugging Face ടോക്കൺ നിങ്ങളുടെ പ്രൊഫൈലിൽ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) കീഴിൽ കാണാം. ജനപ്രിയമായി പോസ്റ്റ് ചെയ്യുകയോ പങ്കിടുകയോ ചെയ്യരുത്. പകരം, ഈ പ്രോജക്റ്റ് ഉപയോഗത്തിനായി പുതിയ ടോക്കൺ ഉണ്ടാക്കി അത് `.env` ഫയലിലെ `HUGGING_FACE_API_KEY` വ്യാരിയബിളിൽ പകർത്തുക. _ശ്രദ്ധിക്കുക:_ ഇത് സാങ്കേതികമായും API കീ അല്ല, എന്നാൽ അവതാരണം authentication ന് ഉപയോഗിക്കുന്നതിനാൽ നാമകരണ സദൃശതയ്ക്കായി ഇതായിരിക്കും.

## Microsoft Foundry മോഡലുകൾ കോൺഫിഗർ ചെയ്യൽ: പോർട്ടൽ വഴി

> **ശ്രദ്ധിക്കുക:** GitHub മോഡലുകൾ 2026 ജൂലൈ അവസാനം റിട്ടയർ ചെയ്യുന്നു. Microsoft Foundry മോഡലുകൾ അതിന്റെ നേരിട്ടുള്ള പ്രതിപകരാണ്, അതേ ഫ്രീ-ടു-ട്രൈ മോഡൽ കാറ്റലോഗും Azure AI ഇൻഫറൻസ് SDK / OpenAI SDK അനുഭവവും നൽകുന്നു.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) സന്ദർശിച്ച് ഒരു Foundry പ്രോജക്റ്റ് സൃഷ്ടിക്കുക (അല്ലെങ്കിൽ തുറക്കുക).
1. [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ബ്രൗസ് ചെയ്ത് ഒരു മോഡൽ വിന്യസിക്കുക, ഉദാഹരണം `gpt-4o-mini`.
1. പ്രോജക്റ്റിന്റെ **Overview** പേജിൽ നിന്നു **endpoint**യും **API കീയും** പകർക്കുക.
1. `.env` ഫയലിൽ `AZURE_INFERENCE_ENDPOINT` ആയി endpoint മൂല്യവും, `AZURE_INFERENCE_CREDENTIAL` ആയിkii ഏഴിരിക്കും കീയുമായി ഉപയോഗിക്കുക.

## ഓഫ്‌ലൈൻ / ലോക്കൽ പ്രൊവൈഡർമാർ

നിങ്ങൾക്ക് ക്ളൗഡ് സബ്സ്ക്രിപ്ഷൻ ഉപയോഗിക്കേണ്ട അവസ്ഥ ഇല്ലെങ്കിൽ, അനുയോജ്യമായ open മോഡലുകൾ നിങ്ങളുടെ സ്വന്തം ഉപകരണത്തിൽ നേരിട്ടു പ്രവർത്തിക്കാം:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftന്റെ ഉപകരണത്തിൽ പ്രവർത്തിക്കുന്ന റൺടൈം. അത് യഥാർത്ഥത്തിൽ ഉത്തമ എക്സിക്യൂഷൻ പ്രൊവൈഡർ (NPU, GPU അല്ലെങ്കിൽ CPU) തിരഞ്ഞെടുക്കും, കൂടാതെ OpenAI-സഹജമായ ഹെൻഡ്‌പോയിന്റും തുറക്കും, അവിടെ നിങ്ങൾക്ക് ഈ കോഴ്സിലെ സാമ്പിൾ കോഡ് വിചാരിച്ച് വളരെ ചെറിയ മാറ്റത്തോടെ വീണ്ടും ഉപയോഗിക്കാം. ആരംഭിക്കാൻ [Foundry Local ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) കാണുക, അല്ലെങ്കിൽ `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) എന്ന കമാൻഡ് ഉപയോഗിച്ച് ഇൻസ്റ്റാൾ ചെയ്യുക.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma പോലുള്ള open മോഡലുകൾ ലോക്കലായി പ്രവർത്തിപ്പിക്കാന്‍ ജനപ്രിയമായ മറ്റൊരു ഓപ്ഷൻ.


രണ്ട് ഓപ്ഷനുകളും ഉപയോഗിച്ച് ഹാൻഡ്‌സോൺ ഉദാഹരണങ്ങൾക്ക് വേണ്ടി [പാഠം 19: SLM-കൾ ഉപയോഗിച്ച് നിർമ്മാണം](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) കാണുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->