# LLM പ്രൊവൈഡറെ തെരഞ്ഞെടുക്കലും ക്രമീകരണവും 🔑

അസൈൻമെന്റുകൾ **കൂടാതെ** ഒപ്പൺഎഐ, അസ്യൂർ, ഹഗ്‌ഗിംഗ് ഫേസ് പോലുള്ള പിന്തുണയുള്ള സേവനദാതാക്കളിലൂടെ ഒരു അല്ലെങ്കിൽ കൂടുതൽ ലാർജ് ലാംഗ്വേജ് മോഡൽ (LLM) ഡിപ്ലോയ്മെന്റുകളുമായി പ്രവർത്തിക്കാൻ ക്രമീകരിക്കാം. ഇവ നമ്മൾ പ്രോഗ്രാമാറ്റിക് ആയി ശരിയായ ക്രെഡൻഷ്യലുകൾ കൊണ്ട് API എന്ന _ഹോസ്റ്റുചെയ്‌ത എൻഡ്‌പോയിന്റ്_ ആക്‌സസ് ചെയ്യാൻ സാധിക്കും. ഈ കോഴ്‌സിൽ, നാം ഇവയെക്കുറിച്ച് ചർച്ച ചെയ്യുന്നു:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) വിവിധ മോഡലുകൾ ഉൾപ്പെടെ കോർ GPT ശ്രേണി.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) തുറന്ന OpenAI മോഡലുകൾ എന്റർപ്രൈസ് റെഡിനസിന്
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ഒരെൻഡ്‌പോയിന്റും API കിയും ഉപയോഗിച്ച് OpenAI, മെട, മിസ്ട്രാൽ, Cohere, Microsoft എന്നിവയിൽ നിന്ന് നൂറുകണക്കിന് മോഡലുകൾ ആക്‌സസ് ചെയ്യാൻ (GitHub മോഡലുകൾ അവസാനിപ്പിക്കുന്നതിനാൽ 2026 ജൂളി അവസാനം മാറ്റപ്പെട്ടിരിക്കുന്നു)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ഓപ്പൺസോഴ്സ് മോഡലുകളും ഇൻഫറൻസ് സർവറും
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) നിങ്ങൾക്ക് തദ്ദേശീയമായി ഇന്റർനെറ്റ് കണക്ഷൻ ഇല്ലാതെ തന്നെ മോഡലുകൾ ഓടിക്കാൻ ആവശ്യമായ ക്ലൗഡ് സബ്‌സ്‌ക്രിപ്ഷൻ വേണ്ടാതെ

**ഈ അഭ്യാസങ്ങൾക്കായി നിങ്ങളുടെ സ്വന്തം അക്കൗണ്ടുകൾ ഉപയോഗിക്കേണ്ടതുണ്ടാകും**. അസൈൻമെന്റുകൾ ഐച്ഛികമാണ്, അതിനാൽ നിങ്ങൾക്കുള്ള താൽപ്പര്യമനുസരിച്ചു ഒന്ന്, ഒക്കെയും - അല്ലെങ്കിൽ കുറവും പ്രൊവൈഡറുകൾ ക്രമീകരിക്കാം. സൈൻഅപ്പ് ഗൈഡൻസിനായി:

| സൈൻഅപ്പ് | ചെലവ് | API കീ | പ്ലേഗ്രൗണ്ട് | കുറിപ്പുകൾ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [വിലനിർണ്ണയം](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [പ്രോജക്റ്റ് അടിസ്ഥാനമാക്കിയുള്ള](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [കോഡ് വേണ്ട, വെബ്](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | പല മോഡലുകളും ലഭ്യമാണ് |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [വിലനിർണ്ണയം](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ക്വിക്ക്‌സ്റ്റാർട്ട്](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [സ്റ്റുഡിയോ ക്വിക്ക്‌സ്റ്റാർട്ട്](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [അക്സസ്‌ക്കായി മുൻകൂട്ടി അപേക്ഷിക്കണം](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [വിലനിർണ്ണയം](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [പ്രോജക്റ്റ് അവലോകന പേജ്](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry പ്ലേഗ്രൗണ്ട്](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ഫ്രീ ടയർ ലഭ്യം; ഒരൊറ്റ എൻഡ്‌പോയിന്റും കീയും പല മോഡൽ പ്രൊവൈഡർമാർക്കും |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [വിലനിർണ്ണയം](https://huggingface.co/pricing) | [ആക്‌സസ് ടോക്കണുകൾ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat കുറച്ച് മോഡലുകളെ പിന്തുണയ്ക്കുന്നു](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | സൗജന്യം (നിങ്ങളുടെ ഉപകരണത്തിൽ പ്രവർത്തിക്കുന്നു) | ആവശ്യമില്ല | [തദ്ദേശീയ CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | പൂർണമായി ഓഫീസ്ലൈൻ, OpenAI-സമ്മതപ്രാപ്ത എൻഡ്‌പോയിന്റ് |
| | | | | |

വിവിധ പ്രൊവൈഡർമാർക്കായി ഈ റെപ്പോസിറ്ററി _ക്രമീകരിക്കാൻ_ താഴെയുള്ള നിർദ്ദേശങ്ങൾ പിന്തുടരുക. ഒരു പ്രത്യേക പ്രൊവൈഡറെ ആവശ്യപ്പെടുന്ന അസൈൻമെന്റുകള് അവരുടെ ഫയൽനാമിൽ താഴെ പറയുന്ന ടാഗുകൾ പോസിഷൻ ചെയ്യും:

- `aoai` - അസ്യൂർ OpenAI എൻഡ്‌പോയിന്റും കീയും ആവശ്യമാണ്
- `oai` - ഓപ്പൺഎഐ എൻഡ്‌പോയിന്റും കീയും ആവശ്യമാണ്
- `hf` - ഹഗ്‌ഗിംഗ് ഫേസ് ടോക്കൺ ആവശ്യമാണ്
- `githubmodels` - Microsoft Foundry Models എൻഡ്‌പോയിന്റും കീയും ആവശ്യമാണ് (GitHub മോഡലുകൾ 2026 ജൂലൈ അവസാനം അവസാനിക്കുന്നു)

നിങ്ങൾക്ക് ഓരോ പ്രൊവൈഡറും, ഒന്നും അല്ലെങ്കിൽ എല്ലാം ക്രമീകരിക്കാം. പ്രോസസ്സ് അനുസരിച്ച് ക്രെഡൻഷ്യൽസ് ഇല്ലായ്മയിൽ പിഴവ് കാണിക്കും.

## `.env` ഫയൽ സൃഷ്ടിക്കുക

മുൻപ് നൽകിയ മാർഗനിർദ്ദേശങ്ങൾ വായിച്ച് ബന്ധപ്പെട്ട പ്രൊവൈഡറിൽ സൈൻ അപ്പ് ചെയ്തു ആവശ്യമായ ഓതന്റിക്കേഷൻ ക്രെഡൻഷ്യൽസ് (API_KEY അല്ലെങ്കിൽ ടോക്കൺ) നേടിയെന്നാണ് നാം അനുമാനിക്കുന്നത്. അസ്യൂർ OpenAI ന്റെ സാഹചര്യത്തിൽ, ഒരു അസ്യൂർ OpenAI സേവനം (എൻഡ്‌പോയിന്റ്) ഡിപ്ലോയ്മെന്റ് നേടി ഒരു GPT മോഡൽ ചേർത്തിട്ടുള്ളതായിരിക്കണം.

അടുത്തത് നിങ്ങളുടെ **ജീർണ്ണമായ അന്തർദേശീയ വാരിയബിളുകൾ** നിയമാനുസൃതമായി ക്രമീകരിക്കുക:

1. റൂട്ട് ഫോൾഡറിൽ `.env.copy` ഫയൽ നോക്കുക, അതിൽ ഇങ്ങനെ ഉള്ളടക്കം ഉണ്ടാകും:

   ```bash
   # OpenAI നൽകുന്നവ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry ലെ Azure OpenAI
   ## (Azure OpenAI സർവീസ് ഇപ്പോൾ Microsoft Foundry ഭാഗമാണ്: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ഡിഫോൾട്ട് സെറ്റ് ചെയ്തിരിക്കുന്നു! (നിലവിലെ സുതാര്യമായ GA API പതിപ്പ്)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry മോഡലുകൾ (ബഹുപ്രവർത്തക മോഡൽ കാറ്റലോഗ്, GitHub മോഡലുകൾക്ക് പകരം, 2026 ജൂലൈ അവസാനം സഞ്ചയിപ്പിക്കും)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ഹഗ്ഗിങ് ഫെയ്‌സ്
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. താഴെ കൊടുത്ത കമാൻഡ് ഉപയോഗിച്ച് `.env` ആയി കോപ്പി ചെയ്യുക. ഈ ഫയൽ _gitignore_ ആക്കപ്പെട്ടതുകൊണ്ടു രഹസ്യങ്ങൾ സംരക്ഷിക്കപ്പെടുന്നു.

   ```bash
   cp .env.copy .env
   ```

3. നിലയിലേക്കുള്ള മൂല്യങ്ങൾ ഇനിപ്പറയുന്ന വിഭാഗത്തിൽ വെച്ചിരിക്കുന്നതുപോലെ പൂരിപ്പിക്കുക (=`= ` വലത്തോടെ ഉള്ള പ്ലേസ്‌ഹോൾഡറുകൾ മാറ്റുക).

4. (ഐച്ഛികം) GitHub Codespaces ഉപയോഗിച്ചാൽ, ഈ റെപ്പോസിറ്ററുമായി ബന്ധപെട്ട _Codespaces രഹസ്യങ്ങൾ_ ആയി അന്തർദേശീയ വാരിയബിളുകൾ സംരക്ഷിക്കാൻ കഴിയും. അപ്പോൾ .env ഫയൽ സജ്ജീകരിക്കേണ്ടതില്ല. **എങ്കിലും, ഈ ഓപ്ഷൻ GitHub Codespaces മാത്രം ഉപയോഗിക്കുന്നവർക്ക് പ്രযോജ്യമാണ് സ്ഥാ. Docker Desktop ഉപയോഗിക്കുന്നവർക്ക് .env ഫയൽ സജ്ജീകരിക്കേണ്ടതുണ്ടാകും.**

## `.env` ഫയൽ പൂരിപ്പിക്കുക

വാരിയബിൾ നാമങ്ങൾ എന്തിനർത്ഥമാക്കുന്നുവെന്ന് പരിചയപ്പെടാം:

| വാരിയബിൾ  | വിവരണം  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ഇത് നിങ്ങൾ പ്രൊഫൈലിൽ ക്രമീകരിച്ച യൂസർ ആക്‌സസ് ടോക്കണാണ് |
| OPENAI_API_KEY | അസ്യൂർ OpenAI അല്ലാത്ത സേവനങ്ങൾക്കുള്ള ഓതോറൈസേഷൻ കീ ആണ് |
| AZURE_OPENAI_API_KEY | അതിന്റെ സേവനത്തിനുള്ള ഓതോറൈസേഷൻ കീ ആണ് |
| AZURE_OPENAI_ENDPOINT | അസ്യൂർ OpenAI റിസോഴ്സ് ഡിപ്ലോയ്മെന്റിന്റെ എൻഡ്‌പോയിന്റ് |
| AZURE_OPENAI_DEPLOYMENT | _ടെക്സ്റ്റ് ജനറേഷൻ_ മോഡൽ ഡിപ്ലോയ്മെന്റ് എൻഡ്‌പോയിന്റ് |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _ടെക്സ്റ്റ് എംബഡ്ഡിങ്ങ്_ മോഡൽ ഡിപ്ലോയ്മെന്റ് എൻഡ്‌പോയിന്റ് |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry പ്രോജക്റ്റിന്റെ എൻഡ്‌പോയിന്റ്, Microsoft Foundry മോഡലുകൾക്കുള്ളത് |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry പ്രോജക്റ്റിന്റെ API കീ |
| | |

ശ്രദ്ധിക്കുക: അവസാന രണ്ട് അസ്യൂർ OpenAI വാരിയബിളുകൾ ചാറ്റ് പൂർത്തീകരണത്തിനുള്ള (ടെക്സ്റ്റ് ജനറേഷൻ) മോഡലും വെക്ടർ സെർച്ച് (എംബഡ്ഡിങ്ങ്) മോഡലും മുൻനിർദേശമായുള്ളവയാണ്. ഇവ ക്രമീകരിക്കുന്നതിനുള്ള നിർദേശങ്ങൾ ബന്ധപ്പെട്ട അസൈൻമെന്റുകളിൽ നൽകും.

## അസ്യൂർ OpenAI ക്രമീകരണം: പോർട്ടലിൽ നിന്ന്

> **കുറിപ്പ്:** അസ്യൂർ OpenAI സെർവീസ് ഇപ്പോൾ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)യുടെ ഭാഗമാണ്. അസ്യൂർ പോർട്ടലിൽ റിസോഴ്സുകളും ഡിപ്ലോയ്മെന്റുകളും കാണിക്കും, പക്ഷേ പ്രതിദിന മോഡൽ മാനേജ്മെന്റ് (ഡിപ്ലോയ്മെന്റുകൾ, പ്ലേഗ്രൗണ്ട്, നിരീക്ഷണം) ഇനി ഫൗണ്ട്രി പോർട്ടലിൽ ഉണ്ടാകും, പഴയ സ്റ്റാൻഡലോൺ "Azure OpenAI Studio"യ്ക്ക് പകരം.

അസ്യൂർ OpenAI എൻഡ്‌പോയിന്റും കീയും [അസ്യൂർ പോർട്ടലിൽ](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) കണ്ടെത്താം, അതുകൊണ്ട് അവിടെനിന്ന് ആരംഭിക്കാം.

1. [അസ്യൂർ പോർട്ടലിലേക്ക്](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) പോകുക
1. സൈഡ്ബാറിൽ **കീസ് ആൻഡ് എൻഡ്‌പോയിന്റ്** തിരഞ്ഞെടുക്കുക (വലത് വശത്തെ മെനു).
1. **ഷോ കീസ്** ക്ലിക്കുചെയ്‌താൽ താഴെ കാണുന്നവ കാണാം: KEY 1, KEY 2, എൻഡ്‌പോയിന്റ്.
1. AZURE_OPENAI_API_KEYക്ക് KEY 1യുടെ മൂല്യം ഉപയോഗിക്കുക
1. AZURE_OPENAI_ENDPOINTക്ക് എൻഡ്‌പോയിന്റ് മൂല്യം ഉപയോഗിക്കുക

ഇനി നാം ഡിപ്ലോയ്മെന്റ് ചെയ്ത പ്രത്യേക മോഡലുകളുടെ എൻഡ്‌പോയിന്റുകൾ വേണം.

1. അസ്യൂർ OpenAI റിസോഴ്സിൽ സൈഡ്ബാറിലെ **മോഡൽ ഡിപ്ലോയ്മെന്റുകൾ** ഓപ്ഷൻ ക്ലിക്ക് ചെയ്യുക
1. തന്റെ ഡെസ്റ്റിനേഷൻ പേജിൽ, **Microsoft Foundry പോർട്ടലിലേക്ക് പോയി** (**മാനേജ് ഡിപ്ലോയ്മെന്റ്സ്** അല്ലെങ്കിൽ നിങ്ങളുടെ റിസോഴ്സിന്റെ തടാകം അനുസരിച്ച്)

ഇതിലൂടെ Microsoft Foundry പോർട്ടലിലേക്ക് പോകും, അവിടെ കൂടുതൽ വിവരങ്ങൾ എങ്ങനെ കിട്ടും എന്നു താഴെ വിവരിക്കുന്നു.

## അസ്യൂർ OpenAI ക്രമീകരണം: Microsoft Foundry പോർട്ടലിൽ നിന്ന്

1. [Microsoft Foundry പോർട്ടലിലേക്കുയിച്ച്](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) നിങ്ങളുടെ റിസോഴ്സ് വഴി അവിടെ എത്തുക.
1. സൈഡ്ബാറിലെ **ഡിപ്ലോയ്മെന്റുകൾ** ടാബിൽ നിലവിൽ ഡിപ്ലോയ്ഡ് ചെയ്ത മോഡലുകൾ കാണുക.
1. നിങ്ങളുടെ വേണമെന്ന മോഡൽ ഡിപ്ലോയഡ് ചെയ്തിട്ടില്ലെങ്കിൽ, [മോഡൽ കാറ്റലോഗിൽ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) നിന്നു **Deploy model** ഉപയോഗിച്ച് അത് ഡിപ്ലോയ്മെന്റ് ചെയ്യുക.
1. നിങ്ങള്‍ക്ക് _ടെക്സ്റ്റ്-ജനറേഷൻ_ മോഡൽ വേണം - നാം ശുപാർശ ചെയ്യുന്നത്: **gpt-5-mini**
1. നിങ്ങള്‍ക്ക് _ടെക്‌സ്റ്റ്-എംബഡ്ഡിങ്_ മോഡൽ വേണം - ശുപാർശ: **text-embedding-3-small**

ഇനി ഉപയോഗിച്ചിട്ടുള്ള ഡിപ്ലോയ്മെന്റ് നാമം (Deployment name) അനുസരിച്ച് അന്തർദേശീയ വാരിയബിളുകൾ അപ്ഡേറ്റ് ചെയ്യുക. സാധാരണ മോദൽ നാമത്തോടൊപ്പം ഇത് സാധാരണയായിരിക്കും, നിങ്ങൾ അത് മനസ്സിലാക്കിയില്ലെങ്കിൽ. ഉദാഹരണത്തിന്:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**വേർപെടുത്തിയ ശേഷം .env ഫയൽ സേവ് ചെയ്യാൻ മറക്കരുത്**. ഇനി നോട്ട്ബുക്ക് ഓടിക്കുന്നതിനുള്ള നിർദ്ദേശങ്ങളിലേക്ക് മടങ്ങാം.

## ഓപ്പൺ എഐ ക്രമീകരണം: പ്രൊഫൈലിൽ നിന്ന്

നിങ്ങളുടെ ഓപ്പൺഎഐ API കീ [നിങ്ങളുടെ OpenAI അക്കൗണ്ടിൽ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) കാണാം. ഇല്ലെങ്കിൽ, അക്കൗണ്ട് സൈൻ അപ്പ് ചെയ്ത് API കീ സൃഷ്ടിക്കാം. കീ കിട്ടിയാൽ `.env` ഫയലിൽ `OPENAI_API_KEY` വാരിയബിളിൽ പൂർപ്പിക്കാം.

## ഹഗ്‌ഗിംഗ് ഫേസ് ക്രമീകരണം: പ്രൊഫൈലിൽ നിന്ന്

നിങ്ങളുടെ Hugging Face ടോക്കൺ പ്രൊഫൈലിൽ [ആക്‌സസ് ടോക്കണുകൾ](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ൽ കാണാം. ഇവ പൊതു വേദിയിൽ പോസ്റ്റ് ചെയ്യരുത് അല്ലെങ്കിൽ പങ്കുവെക്കരുത്. ഈ പ്രോജക്റ്റിനുള്ള പുതിയ ഒരു ടോക്കൺ സൃഷ്ടിച്ച് `.env` ഫയലിൽ `HUGGING_FACE_API_KEY` വാരിയബിളിൽ പേസ്റ്റ് ചെയ്യുക. _ശ്രദ്ധിക്കുക:_ ഇത് സാങ്കേതികമായി API കീ അല്ല, എന്നാൽ ഒത്തുചേരാനായി ഓതന്റിക്കേഷൻ ആയി ഉപയോഗിക്കുന്നു, അതുകൊണ്ട് ഇത് API കീ എന്ന് വിളിക്കുന്നു.

## Microsoft Foundry മോഡലുകൾ ക്രമീകരണം: പോർട്ടൽ വഴി

> **കുറിപ്പ്:** GitHub മോഡലുകൾ 2026 ജൂലൈ അവസാനം അവസാനിപ്പിക്കപ്പെടുന്നു. Microsoft Foundry മോഡലുകൾ നേരിട്ട് പകരം വയ്ക്കുന്നു അതുപോലെ ഫ്രീ ട്രൈ മോഡൽ കാറ്റലോഗും അസ്യൂർ AI ഇന്‍ഫെറന്‍സ് SDK / OpenAI SDK അനുഭവവും വാഗ്ദാനം ചെയ്യുന്നു.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ൽ പോയി പുതിയ ഫൗണ്ട്രി പ്രോജക്റ്റ് സൃഷ്ടിക്കുക അല്ലെങ്കിൽ തുറക്കുക.
1. [മോഡൽ കാറ്റലോഗ്](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ബ്രൗസ് ചെയ്ത്, ഉദാഹരണമായി `gpt-5-mini` മോഡൽ ഡിപ്ലോയ്മെന്റ് ചെയ്യുക.
1. പ്രോജക്റ്റിന്റെ **അവലോകന** പേജിൽ നിന്ന് **എൻഡ്‌പോയിന്റ്** കീ പൊൾ ചെയ്യുക.
1. `.env` ഫയലിൽ `AZURE_INFERENCE_ENDPOINT` ആക്കി എൻഡ്‌പോയിന്റും `AZURE_INFERENCE_CREDENTIAL` ആക്കി കീയും നൽകുക.

## ഓഫീസ്ലൈൻ / ലോക്കൽ പ്രൊവൈഡറുകൾ

ക്ലൗഡ് സബ്‌സ്‌ക്രിപ്ഷൻ ഉപയോഗിക്കാതെ തന്നെ, നിങ്ങൾക്ക് തദ്ദേശീയ ഡിവൈസിൽ ഒപ്പം പൊരുത്തപ്പെടുന്ന ഓപ്പൺ മോഡലുകൾ ഓടിക്കാൻ സാധിക്കും:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - മൈക്രോസോഫ്റ്റിൻറെ തദ്ദേശീയ റൺടൈം. ഇത് ഏറ്റവും നല്ല എക്സിക്യൂഷൻ പ്രൊവൈഡർ (NPU, GPU, CPU) ഓട്ടോമാറ്റിക്കായി തിരഞ്ഞെടുക്കുകയും OpenAI-സമ്മതപ്രാപ്ത എൻഡ്‌പോയിന്റ് കാണിക്കുകയും ചെയ്യുന്നു, ഫലം മിനിമൽ മാറ്റത്തോടെ ഈ കോഴ്‌സിലെ സാമ്പിൾ കോഡ് വീണ്ടും ഉപയോഗിക്കാം. തുടക്കം കുറിക്കാൻ [Foundry Local ഡോക്യുമെന്റേഷന്‍](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) കണ്ടോളൂ അല്ലെങ്കിൽ `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ഉപയോഗിച്ച് ഇൻസ്റ്റാൾ ചെയ്യൂ.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma പോലുള്ള ഓപ്പൺ മോഡലുകൾ നഗരത്തിൽ ഓടിക്കാൻ പ്രചാരത്തിലുള്ള ബദലാണ്.


ഇരുവിധ ഓപ്ഷനുകളും ഉപയോഗിക്കുന്ന കൈകടത്തൽ ഉദാഹരണങ്ങൾക്കായി [പാഠം 19: SLMകളോടുകൂടിയ നിർമ്മാണം](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) കാണുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->