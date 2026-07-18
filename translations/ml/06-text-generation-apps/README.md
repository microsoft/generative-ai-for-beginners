# ടെക്സ്റ്റ് ജനറേഷൻ ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ

[![Building Text Generation Applications](../../../translated_images/ml/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിലുള്ള ചിത്രം ക്ലിക്ക് ചെയ്യുക)_

ഇതുവരെ നിങ്ങൾ ഈ کور്സിലൂടെയാണ് കാണുന്നത്, പ്രോമ്പ്റ്റുകൾ പോലുള്ള അടിസ്ഥാന ആശയങ്ങളുണ്ട്, "prompt engineering" എന്ന മുഴുവൻ ശാഖയും ഉണ്ട്. ChatGPT, Office 365, Microsoft Power Platform എന്നിവ പോലെയുള്ള പല ഉപകരണങ്ങളും, നിങ്ങൾ എന്തെങ്കിലും നേടാൻ പ്രോമ്പ്റ്റുകൾ ഉപയോഗിക്കാൻ പിന്തുണയും നൽകുന്നു.

ആപ്ലിക്കേഷനിലേക്ക് ഇത്തരമുള്ള അനുഭവം ചേർക്കാൻ, പ്രോമ്പ്റ്റുകൾ, പൂർണ്ണീകരണങ്ങൾ എന്നിവ പോലുള്ള ആശയങ്ങൾ മനസ്സിലാക്കുകയും പ്രവർത്തിക്കാൻ ഒരു ലൈബ്രറി തിരഞ്ഞെടുക്കുകയും വേണം. ഇതാണ് നിങ്ങൾ ഈ അധ്യായത്തിൽ പഠിക്കാൻ പോകുന്നത്.

## പരിചയം

ഈ അധ്യായത്തിൽ, നിങ്ങൾ:

- openai ലൈബ്രറിയും അതിന്റെ പ്രധാന ആശയങ്ങളുമെന്തെന്നു പഠിക്കുക.
- openai ഉപയോഗിച്ച് ഒരു ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് നിർമ്മിക്കുക.
- ഒരു ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് നിർമ്മിക്കാൻ പ്രോമ്പ്റ്റ്, ടെമ്പറേച്ചർ, ടോക്കൻസ് തുടങ്ങിയ ആശയങ്ങൾ എങ്ങനെ ഉപയോഗിക്കും എന്ന് മനസ്സിലാക്കുക.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠത്തിന്റെ അവസാനത്തില്‍, നിങ്ങൾക്ക് സാധിക്കും:

- ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് എന്താണെന്ന് വിശദീകരിക്കുക.
- openai ഉപയോഗിച്ച് ഒരു ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് നിർമ്മിക്കുക.
- കൂടുതൽ അല്ലെങ്കിൽ കുറച്ച് ടോക്കൻസുകൾ ഉപയോഗിക്കാൻ നിങ്ങളുടെ ആപ്പ് ക്രമീകരിക്കുക; കൂടാതെ വ്യത്യസ്ത ഔട്ട്പുട്ടിനായി ടെമ്പറേച്ചർ മാറുക.

## ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് എന്താണ്?

സാധാരണയായി നിങ്ങൾ ഒരു ആപ്പ് നിർമ്മിക്കുമ്പോൾ, ഇതിനടുത്തതായി ഇത്തരമൊരു ഇന്റർഫേസ് ഉണ്ടായിരിക്കും:

- കമാൻഡ് അടിസ്ഥാനമാക്കിയുള്ളത്. കൺസോൾ ആപ്പുകൾ ഒരു കമാൻഡ് ടൈപ്പ് ചെയ്ത് ഒരു ടാസ്‌ക്ക്സ് നടത്തുന്നു. ഉദാഹരണത്തിന്, `git` ഒരു കമാൻഡ് അടിസ്ഥാനമാക്കിയുള്ള ആപ്പ് ആണ്.
- ഉപയോക്തൃ ഇന്റർഫേസ് (UI). ചില ആപ്പുകൾ ഗ്രാഫിക്കൽ യൂസർ ഇന്റർഫേസുകൾ (GUIs) ഉള്ളതാണ്, ഇവിടെ നിങ്ങൾ ബട്ടണുകൾ ക്ലിക്ക് ചെയ്യുകയും, ടെക്സ്റ്റ് ഇൻപുട്ട് നൽകുകയും, ഓപ്ഷനുകൾ തിരഞ്ഞെടുക്കുകയും ചെയ്യുന്നു.

### കൺസോൾ, UI ആപ്പുകൾക്ക് പരിധി ഉണ്ട്

നിങ്ങൾ ടൈപ്പ് ചെയ്യുന്ന കമാൻഡ് അടിസ്ഥാനമാക്കിയുള്ള ആപ്പ് ഒപ്പം താരതമ്യം ചെയ്യുക:

- **ഇത് പരിധിയാണ്**. നിങ്ങൾക്ക് യാതൊരു കമാൻഡും ടൈപ്പ് ചെയ്യാൻ കഴിയില്ല, ആപ്പ് പിന്തുണയ്ക്കുന്ന ചില കമാൻഡുകൾ മാത്രമേ സാധൂകരിക്കൂ.
- **ഭാഷാപരമായി പ്രത്യേകമായി**. ചില ആപ്പുകൾ പല ഭാഷകളും പിന്തുണയ്ക്കുന്നു, പക്ഷേ ഡീഫോൾട്ട് ആപ്പ് ഒരു പ്രത്യേക ഭാഷയ്ക്ക് മാത്രം നിർമ്മിച്ചിരിക്കുന്നു, നിങ്ങൾക്ക് കൂടുതൽ ഭാഷാ പിന്തുണ ചേർക്കാൻ കഴിയുന്നുണ്ടെങ്കിലും.

### ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പുകളുടെ ഗുണങ്ങൾ

ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് എങ്ങനെ വ്യത്യസ്തമാണ്?

ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പിൽ നിങ്ങൾക്ക് കൂടുതൽ സ്വാതന്ത്ര്യം ഉണ്ട്, നിങ്ങൾ നിർദ്ദിഷ്ട കമാൻഡുകൾക്കോ പ്രത്യേക ഇൻപുട്ട് ഭാഷയിലോ പരിധിമിതരാക്കപ്പെട്ടിട്ടില്ല. പകരം, നിങ്ങൾ ആപ്പുമായി സമ്പർക്കം സ്ഥാപിക്കാൻ സ്വാഭാവിക ഭാഷ ഉപയോഗിക്കാം. മറ്റൊരു ഗുണം, നിങ്ങൾ ഇതിനകം വലിയ വിവരങ്ങൾ മുൻകൂട്ടി പരിശീലിപ്പിച്ച ഡാറ്റ സ്രോതസുമായി സംവദിക്കുന്നു, പരമ്പരാഗത ആപ്പ് ഒരു ഡാറ്റാബേസിലുള്ള വിവരങ്ങൾ പരിധിമിതമായിരിക്കാം.

### ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പിൽ എന്തൊക്കെ നിർമ്മിക്കാം?

നിങ്ങൾ നിർമ്മിക്കാനാകുന്ന പല കാര്യങ്ങളുണ്ട്. ഉദാഹരണത്തിന്:

- **ഒരു ചാറ്റ്ബോട്ട്**. നിങ്ങളുടെ കമ്പനി, അതിന്റെയും ഉൽപ്പന്നങ്ങളുടെയും വിഷയങ്ങളെക്കുറിച്ചുള്ള ചോദ്യങ്ങൾക്കുള്ള ചാറ്റ്ബോട്ട് നല്ലൊരു അനുയോജ്യമായിരിക്കാം.
- **സഹായി**. LLM-കൾ ടെക്സ്റ്റ് സംഗ്രഹിക്കുക, വിവരങ്ങൾ നേടുക, റിസൂമേ പോലുള്ള ടെക്സ്റ്റ് നിർമ്മിക്കുക മുതലായവയിൽ മികച്ചവയാണ്.
- **കോഡ് അസിസ്റ്റന്റ്**. നിങ്ങൾ ഉപയോഗിക്കുന്ന ഭാഷാ മോഡലുമായി തീരുമാനം ചെയ്ത്, കോഡ് എഴുതാൻ സഹായിക്കുന്ന ഒരു കോഡ് സഹായി നിർമ്മിക്കാം. ഉദാഹരണത്തിന്, GitHub Copilot പോലെയാണ് ChatGPTയും കോഡ് എഴുതാൻ സഹായിക്കുന്നത്.

## എങ്ങനെ തുടങ്ങാം?

സാധാരണയായി LLM-യ്‌ക്കൊപ്പം സംയോജിപ്പിക്കാൻ നിങ്ങൾക്ക് രണ്ട് പ്രധാന സമീപനങ്ങൾ ഉണ്ട്:

- APIs ഉപയോഗിക്കുക. ഇവിടെ നിങ്ങളുടെ പ്രോമ്പ്റ്റുമായി വെബ് അഭ്യർത്ഥനകൾ നിർമ്മിച്ച് ടകസ്റ്റു ലഭിക്കും.
- ലൈബ്രറികൾ ഉപയോഗിക്കുക. ലൈബ്രറികൾ API കാൾസ് ഉൾപ്പെടുത്തും, ഉപയോഗിക്കാൻ എളുപ്പമാക്കും.

## ലൈബ്രറികൾ / SDK-കൾ

LLM പ്രവർത്തനത്തിനായി അറിയപ്പെടുന്ന ചില ലൈബ്രറികളുണ്ട്, ഉദാഹരണത്തിന്:

- **openai**: നിങ്ങളുടെ മോഡലുമായി ബന്ധപ്പെടാനും പ്രോമ്പ്റ്റുകൾ അയയ്ക്കാനും ഈ ലൈബ്രറി എളുപ്പമാക്കുന്നു.

തുടർന്ന് ഉയർന്ന നിരക്കിലുള്ള ചില ലൈബ്രറികൾ ഉണ്ട്:

- **Langchain**: Langchain അറിയപ്പെടുന്ന, Python പിന്തുണയ്ക്കുന്ന ലൈബ്രറി.
- **Semantic Kernel**: C#, Python, Java തുടങ്ങിയ ഭാഷകൾക്ക് പിന്തുണ നൽകുന്ന Microsoft-ന്റെ Semantic Kernel ലൈബ്രറി.

## openai ഉപയോഗിച്ച് ആദ്യ ആപ്പ്

നിങ്ങളുടെ ആദ്യ ആപ്പ് എങ്ങനെ നിർമ്മിക്കാമെന്ന് നോക്കാം, ഏതു ലൈബ്രറികൾ ആവശ്യമാണെന്ന്, എത്രത്തോളം വേണമെന്നു.

### openai ഇൻസ്റ്റാൾ ചെയ്യുക

OpenAI അല്ലെങ്കിൽ Azure OpenAI-വുമായുണ്ടാകുന്ന സംവേദനത്തിന് അവിടെ ഉള്ള പല ലൈബ്രറികളും ഉണ്ട്. C#, Python, JavaScript, Java മുതലായ നിരവധി പ്രോഗ്രാമിംഗ് ഭാഷകളും ഉപയോഗിക്കാൻ സാധിക്കും. ഞങ്ങൾ `openai` Python ലൈബ്രറി തിരഞ്ഞെടുക്കുകയും `pip` വഴി ഇൻസ്റ്റാൾ ചെയ്യുകയും ചെയ്യുന്നു.

```bash
pip install openai
```

### ഒരു റിസോർസ് സൃഷ്ടിക്കുക

നിങ്ങൾ താഴെ പറയുന്ന ഘട്ടങ്ങൾ നടത്തണം:

- Azure-ൽ ഒരു അക്കൗണ്ട് സൃഷ്ടിക്കുക [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI ആക്സസ് നേടുക. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) എന്ന വെബ്സൈറ്റ് സന്ദർശിച്ച് ആക്സസ് അഭ്യർത്ഥിക്കുക.

  > [!NOTE]
  > ഈ ലേഖനം എഴുതുമ്പോൾ, Azure OpenAI ഉപയോഗിക്കാൻ ആക്സസ് അപേക്ഷിക്കേണ്ടതുണ്ട്.

- Python ഇൻസ്റ്റാൾ ചെയ്യുക <https://www.python.org/>
- Azure OpenAI സേവന റിസോഴ്‌സ് സൃഷ്ടിച്ചിരിക്കണം. ഇതെങ്ങനെ ചെയ്യാമെന്ന് ഈ ഗൈഡിൽ കാണുക: [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API കീയും എന്റ്പോയിന്റും കണ്ടെത്തുക

ഇപ്പോള്‍, നിങ്ങളുടെ `openai` ലൈബ്രറിയ്ക്ക് ഏത് API കീ ഉപയോഗിക്കണമെന്ന് അറിയിക്കേണ്ടതാണ്. API കീ കണ്ടെത്താൻ, നിങ്ങളുടെ Azure OpenAI റിസോഴ്‌സിലെ "Keys and Endpoint" സെക്ഷനിലെ "Key 1" മൂല്യം കോപ്പി ചെയ്യുക.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ഇനി ഇതു കോപ്പി ചെയ്തതിനുശേഷം, ലൈബ്രറികൾ അതിനനുസരിച്ച് ഉപയോഗിക്കാൻ നാം നിർദ്ദേശിക്കാം.

> [!NOTE]
> നിങ്ങളുടെ API കീ നിങ്ങളുടെ കോഡിൽ നിന്ന് വേർതിരിക്കുക നല്ലതാണ്. ഇത് എന്വയോൺമെന്റ് വേരിയബിളുകൾ ഉപയോഗിച്ച് സാധ്യമാണ്.
>
> - എന്വയോൺമെന്റ് വേരിയബിൾ `OPENAI_API_KEY` നിങ്ങളുടെ API കീയിലേക്ക് സജ്ജീകരിക്കൂ.
>   `export OPENAI_API_KEY='sk-...'`

### Azure കോൺഫിഗറേഷൻ സജ്ജമാക്കൽ

നിങ്ങൾ Azure OpenAI (ഇപ്പോൾ Microsoft Foundryയുടെ ഭാഗം) ഉപയോഗിക്കുന്നുവെങ്കിൽ, കോൺഫിഗറേഷൻ ഇതുപോലെ സജ്ജീകരിക്കുന്നു. സ്റ്റാൻഡേർഡ് `OpenAI` ക്ലൈന്റ് ഉപയോഗിച്ച് Azure OpenAI `/openai/v1/` എന്റ്പോയിന്റിലേക്ക് പോയിന്റ് ചെയ്യുന്നു, ഇത് Responses API-വുമായാണ് പ്രവർത്തിക്കുന്നത്, അധിക `api_version` ആവശ്യമില്ല:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

മുകളിൽ താഴെ പറയുന്ന കാര്യങ്ങൾ നാം സജ്ജീകരിക്കുന്നു:

- `api_key`: Azure പോർട്ടലിൽ നിന്നോ മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രി പോർട്ടലിൽ നിന്നോ ലഭിക്കുന്ന നിങ്ങളുടെ API കീ.
- `base_url`: നിങ്ങളുടെ ഫൗണ്ട്രി റിസോഴ്‌സ് എന്റ്പോയിന്റ് `/openai/v1/` ചേർത്തു. സ്റ്റേബിൾ v1 എന്റ്പോയിന്റ് OpenAIയും Azure OpenAIയും പ്രവർത്തിക്കുന്നതു കൊണ്ട് `api_version` ഇല്ലാതെ പ്രവർത്തിക്കുന്നു.

> [!NOTE] > `os.environ` എന്വയോൺമെന്റ് വേരിയബിളുകൾ വായിക്കുന്നു. നിങ്ങൾക്ക് ഇത് `AZURE_OPENAI_API_KEY` , `AZURE_OPENAI_ENDPOINT` പോലുള്ള വേരിയബിളുകൾ വായിക്കാനും ഉണ്ടാകും. ഈ വേരിയബിളുകൾ ടെർമിനലിൽ സജ്ജീകരിക്കൂ അല്ലെങ്കിൽ `dotenv` പോലുള്ള ലൈബ്രറി ഉപയോഗിക്കുക.

## ടെക്സ്റ്റ് ജനറേറ്റ് ചെയ്യുക

ടെക്സ്റ്റ് ജനറേറ്റർ ചെയ്യാനുള്ള മാർഗം Responses API ഉപയോഗിച്ച് `responses.create` മെഥഡാണ്. ഉദാഹരണമായി ഇവിടെ കാണാം:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ഇത് നിങ്ങളുടെ മാതൃക വിന്യാസത്തിന്റെ പേര് ആണ്
    input=prompt,
    store=False,
)
print(response.output_text)
```

മുകളിൽ കൊടുത്ത കോഡിൽ, നാം ഒരു റിസ്പോണ്‍സ് സൃഷ്ടിച്ചു, മാതൃകയും പ്രോമ്പ്റ്റും നൽകി. ശേഷം `response.output_text` വഴി ജനറേറ്റുചെയ്ത ടെക്സ്റ്റ് പ്രിന്റ് ചെയ്യുന്നു.

### മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ

Responses API സിംഗിൾ-ടേൺ ടെക്സ്റ്റ് ജനറേഷൻക്കും മൾട്ടി-ടേൺ ചാറ്റ്ബോട്ടുകൾക്കും ഉത്തമം - നിങ്ങൾ `input` ലിസ്റ്റിൽ മസേജുകൾ നൽകിയാൽ സംഭാഷണം നിർമ്മിച്ചേക്കാം:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ഈ ഫംഗ്ഷണാലിറ്റിയെ കുറിച്ച് കൂടുതൽ വിവരങ്ങൾ അടുത്ത അധ്യായത്തിൽ.

## അഭ്യാസം - നിങ്ങളുടെ ആദ്യ ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ്

openai ഇൻസ്റ്റാൾ ചെയ്ത് കോൺഫിഗർ ചെയ്യാനായി പഠിച്ചതിനുശേഷം, നിങ്ങളുടെ ആദ്യ ടെക്സ്റ്റ് ജനറേഷൻ ആപ്പ് നിർമ്മിക്കാം. നിർമ്മിക്കാൻ, താഴെ പറയുന്ന ഘട്ടങ്ങൾ പിന്തുടരുക:

1. ഒരു വ്യർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുകയും openai ഇൻസ്റ്റാൾ ചെയ്യുകയും ചെയ്യുക:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows ഉപയോഗിക്കുന്നുവെങ്കിൽ `source venv/bin/activate` എന്നതിന് പകരം `venv\Scripts\activate` ഉപയോഗിക്കുക.

   > [!NOTE]
   > Azure OpenAI കീ കണ്ടെത്താൻ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) സന്ദർശിച്ച് `Open AI` തിരയുക, `Open AI resource` തിരഞ്ഞെടുക്കുക, ഉപ്പം `Keys and Endpoint` ഭാഗത്ത് നോക്കി `Key 1` കോപ്പി ചെയ്യുക.

1. ഒരു _app.py_ ഫയൽ സൃഷ്ടിച്ച് താഴെ പറയുന്ന കോഡ് നൽകുക:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # നിങ്ങളുടെ പൂർത്തീകരണ കോഡ് ചേർക്കുക
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ഉപയോഗിച്ച് അഭ്യർത്ഥന നടത്തുക
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # പ്രതികരണം അച്ചടിക്കുക
   print(response.output_text)
   ```

   > [!NOTE]
   > സാധാരണ OpenAI (Azure അല്ല) ഉപയോഗിക്കുന്നവർക്കായി, `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (base_url ഇല്ലാതെ) ഉപയോഗിക്കുക, deployment പേരിനുപകരം `gpt-5-mini` പോലെയുള്ള മോഡൽ പേര് നൽകുക.

   നിങ്ങൾക്ക് താഴെപോലൊരു ഔട്ട്‌പുട്ട് കാണാം:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## വ്യത്യസ്ത ആവശ്യങ്ങൾക്ക് വ്യത്യസ്ത പ്രോമ്പ്റ്റുകൾ

ഇപ്പോൾ നിങ്ങൾക്ക് പ്രോമ്പ്റ്റ് ഉപയോഗിച്ച് ടെക്സ്റ്റ് എങ്ങനെ ജനറേറ്റ് ചെയ്യാമെന്നും, ഒരു പ്രോഗ്രാം പ്രവർത്തിപ്പിച്ച് അതിൽ മാറ്റം വരുത്തി വ്യത്യസ്ത തരത്തിലുള്ള ടെക്സ്റ്റ് എങ്ങനെ നിർമ്മിക്കാമെന്നുമറിയാം.

പ്രോമ്പ്റ്റുകൾ പല ഫംഗ്ഷനുകളും നടത്താൻ ഉപയോഗിക്കാം. ഉദാഹരണങ്ങൾ:

- **ഒരു പ്രത്യേക തരത്തിലുള്ള ടെക്സ്റ്റ് നിർമ്മിക്കുക**. ഉദാഹരണത്തിന്, കഥ, കവിത, ക്വിസ് ചോദ്യങ്ങൾ തുടങ്ങിയവ നിർമ്മിക്കാം.
- **വിവരം അന്വേഷിക്കുക**. പ്രോമ്പ്റ്റുകൾ ഉപയോഗിച്ച് വിവരങ്ങൾ അന്വേഷിക്കാം, ഉദാഹരണത്തിന് 'web developmentൽ CORS എന്തിന്?'.
- **കോഡ് ജനറേറ്റ് ചെയ്യുക**. പ്രോമ്പ്റ്റുകൾ ഉപയോഗിച്ച് കോഡ് നിർമ്മിക്കാം, ഉദാഹരണത്തിന് ഇമെയിൽ വാലിഡേറ്റ് ചെയ്യാനുള്ള റെഗുലർ എക്‌സ്പ്രഷൻ നിർമ്മിക്കുക അല്ലെങ്കിൽ വെബ് ആപ്പ് പോലുള്ള ഒരു മുഴുവൻ പ്രോഗ്രാം നിർമ്മിക്കുക.

## കൂടുതൽ പ്രായോഗിക ഉപയോഗം: ഒരു റസിപ്പി ജനറേറ്റർ

നിങ്ങൾ വീട്ടിൽ ഉള്ള സാധനങ്ങൾ ഉപയോഗിച്ച് എന്തെങ്കിലും പാചകം ചെയ്യാൻ ആഗ്രഹിക്കുന്നു എന്ന് കരുതുക. അതിനു വേണ്ടി നിങ്ങള്ക്ക് ഒരു പാചകവിധി керек. പാചകവിധി കണ്ടെത്താൻ സാധനസൂചക യന്ത്രം ഉപയോഗിക്കാം അല്ലെങ്കിൽ LLM ഉപയോഗിക്കാം.

നിങ്ങൾ ഇങ്ങനെ ഒരു പ്രോമ്പ്റ്റ് എഴുതാം:

> "ഇടമുണ്ട് ചിക്കൺ, ഉരുളകിഴങ്ങ്, കാരറ്റ് ഉള്ള ഒരു വിഭവത്തിന് 5 റസിപ്പികൾ കാണിക്കൂ. ഓരോ റസിപ്പിക്കും ഉപയോഗിച്ച എല്ലാ സാധനങ്ങളും പട്ടിക ആക്കുക"

മുകളിൽ കൊടുത്ത പ്രോമ്പ്റ്റ് പ്രകാരം നിങ്ങൾക്ക് സമാനമായ ഒരു റിസ്പോൺസ് വരാം:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

ഈ ഫലം നല്ലതാണ്, എന്ത് പാചകം ചെയ്യാമെന്നു ഞാൻ അറിഞ്ഞു. ഇപ്പോൾ, എന്തൊക്കെ ഏറ്റവും ഉപകാരപ്രദമായുള്ള മെച്ചപ്പെടുത്തലുകൾ ആകാമെന്നു നോക്കാം:

- ഞാൻ ഇഷ്ടപ്പെടാത്ത അല്ലെങ്കിൽ അലർജി ഉള്ള സാധനങ്ങൾ ഒഴിവാക്കൽ.
- വീട്ടിൽ എവിടെ സാധനങ്ങൾ ഇല്ലെങ്കിൽ ഷോപ്പിംഗ് ലിസ്റ്റ് ഉണ്ടാക്കുക.

മുകളിൽ പറഞ്ഞ കാരണങ്ങൾക്കായി ഇതൊരു അധിക പ്രോമ്പ്റ്റ് ചേർക്കാം:

> " എനിക്ക് അല്ലർജി ഉണ്ടാ കാരണത്താൽ വെളുത്തുള്ളി ഉള്ള റസിപ്പികൾ നീക്കം ചെയ്യുക, അതിന് പകരം മറ്റൊന്ന് ഇടുക. കൂടാതെ, ഞാൻ വീട്ടിൽ ചിക്കൺ, ഉരുളകിഴങ്ങ്, കാരറ്റ് ഉണ്ടെന്ന് ശ്രദ്ധയിൽ വെച്ച് രസിപ്പിക്കുള്ള സാധനങ്ങളുടെ ഷോപ്പിംഗ് ലിസ്റ്റ് ഉണ്ടാക്കുക."

ഇപ്പോൾ നിങ്ങൾക്ക് പുതിയ ഫലം ലഭിക്കും, അതായത്:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

ആണു നിങ്ങളുടെ അഞ്ച് റസിപ്പികൾ, വെളുത്തുള്ളി ഇല്ലാതെ, കൂടാതെ നിങ്ങൾക്ക് വീട്ടിൽ ഉള്ള സാധനങ്ങൾ കരുതിയാണ് ഷോപ്പിംഗ് ലിസ്റ്റും.

## അഭ്യാസം - ഒരു റസിപ്പി ജനറേറ്റർ നിർമ്മിക്കുക

ഇപ്പോൾ ഒരു സിനാരിയോ കളിച്ചതിനുശേഷം, അത് അനുസരിച്ച് കോഡ് എഴുതാം. ഇതിനായി, താഴെ പറയുന്ന ഘട്ടങ്ങൾ പിന്തുടരുക:

1. നിലവിലുള്ള _app.py_ ഫയൽ ആരംഭ ബിന്ദുവായി ഉപയോഗിക്കുക
1. `prompt` വേരിയബിൾ കണ്ടെത്തി അതിലെ കോഡ് താഴെ കൊടുത്തതായി മാറ്റുക:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ഇപ്പോൾ നിങ്ങൾ കോഡ് റൺ ചെയ്താൽ സമാനമായ ഔട്ട്‌പുട്ട് കാണാം:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ശ്രദ്ധിക്കുക, നിങ്ങളുടെ LLM nondeterministic ആണ്, അതിനാൽ പ്രോഗ്രാം ഓരോ തവണയും റൺ ചെയ്‌തപ്പോൾ വ്യത്യസ്ത ഫലങ്ങൾ കിട്ടാം.

   വളരെ നന്നെയാണ്, മെച്ചപ്പെടുത്താനുള്ള മാർഗങ്ങൾ നോക്കാം. മെച്ചപ്പെടുത്താൻ, കോഡ് സൌകര്യപ്രദമായിരിക്കണം, അതായത് സാധനങ്ങളും റെസിപ്പികളുടെ എണ്ണവും സ്വതന്ത്രമായി മാറ്റാവുന്നതായിരിക്കണം.

1. കോഡ് താഴെ പറയുന്ന വിധം മാറ്റാം:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # റെസിപ്പികളുടെ എണ്ണം പ്രാമ്പ്റ്റിലും സസ്യാഹാരം പദാർത്ഥങ്ങളിലും ഇന്റർപ്പോളേറ്റ് ചെയ്യുക
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ടെസ്റ്റ് റൺ കൊടുക്കുമ്പോൾ കോഡ് ഇതുപോലെ തോന്നിയേക്കാം:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ഫിൽറ്റർയും ഷോപ്പിംഗ് ലിസ്റ്റും ചേർത്തു മെച്ചപ്പെടുത്തുക

ഇപ്പോൾ ഞങ്ങളുടെ ആപ്പിന് റെസിപ്പി നിർമ്മിക്കാൻ കഴിവുണ്ട്, അത് ഉപയോക്താവ് നൽകുന്ന ഇൻപുട്ടുകൾ (റെസിപ്പുകളുടെ എണ്ണം, ഉപയോഗിക്കുന്ന സാധനങ്ങൾ) അടിസ്ഥാനമാക്കി സൌകര്യമുള്ളതും.

മെച്ചപ്പെടുത്താനുള്ള മാർഗം താഴെപ്പറയുന്നവയുണ്ട്:

- **സാധനങ്ങൾ ഫിൽറ്റർ ചെയ്യുക**. നമ്മൾ ഇഷ്ടപ്പെടാത്ത അല്ലെങ്കിൽ അലർജിയുള്ള സാധനങ്ങൾ ഒഴിവാക്കാൻ സാധിക്കണം. ഇത് ചെയ്യാൻ, നിലവിലുള്ള പ്രോമ്പ്റ്റിൽ ഒരു ഫിൽറ്റർ കൊണ്ട് അവൻഡ് ചേർക്കാം:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  മുകളിൽ, പ്രോമ്പ്റ്റിന് `{filter}` ചേർത്തിരിക്കുന്നു; ഉപയോക്താവിൽ നിന്ന് ഫിൽറ്റർ മൂല്യം പ്രാപ്തമാക്കുകയും ചെയ്തു.

  പ്രോഗ്രാം ഒറ്റത്തവണ റൺ ചെയ്യുമ്പോൾ ഉൾപ്പെടുത്തലുകളുടെ ഉദാഹരണം ഇപ്രകാരം ആയിരിക്കാം:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  ഒന്ന് ശ്രദ്ധിക്കുക: പാൽ ഉള്ള任何 റെസിപ്പികളും ഫിൽറ്റർ ചെയ്തിട്ടുണ്ട്. എന്നാൽ നിങ്ങൾ ലാക്ടോസ് ഇൻറൊളറന്റ് ആണെങ്കിൽ ചീസ് ഉൾപ്പെട്ട റെസിപ്പികളും ഒഴിവാക്കേണ്ടതാണ്, അതിനാൽ വ്യക്തമാക്കേണ്ടതുണ്ട്.


- **ഒരു ഷോപ്പിംഗ് ലിസ്റ്റ് സൃഷ്ടിക്കുക**. നമുക്ക് വീട്ടില അടുത്തിടപഴകിയിരിക്കുന്നതെന്താണെന്ന് കാരണമായി കരുതിക്കൊണ്ട് ഒരു ഷോപ്പിംഗ് ലിസ്റ്റ് സൃഷ്ടിക്കണം.

  ഈ ഫങ്ഷണാലിറ്റിക്കായി, നാം എല്ലാം ഒരു പ്രംപ്റ്റിൽ പരിഹരിക്കാമെന്നും അല്ലെങ്കിൽ രണ്ടു പ്രംപ്റ്റുകളായി വിഭജിക്കാമെന്നും ശ്രമിക്കാം. രണ്ടാമത്തെ മാർഗം പരീക്ഷിക്കാം. ഇവിടെ ഞങ്ങൾ ഒരു കൂട്ടിച്ചേർക്കലുള്ള മറ്റൊരു പ്രംപ്റ്റ് ചേർക്കാൻ നിർദ്ദേശിക്കുന്നു, പക്ഷേ അത് പ്രവർത്തിക്കാൻ, ഞങ്ങൾക്ക് മുൻപ്രംപ്റ്റിലെ ഫലം പിന്നീട് പ്രംപ്റ്റിന്റെ കോൺടെക്സ്റ്റ് ആയി ചേർക്കേണ്ടത് ആവശ്യമാണ്.

  ആദ്യ പ്രംപ്റ്റിൽ നിന്നുള്ള ഫലം പ്രിന്റ് ചെയ്യുന്നതിനു വേണ്ടി ഉള്ള ഭാഗം കണ്ടെത്തി താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ചേർക്കുക:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # മറുപടി പ്രിന്റ് ചെയ്യുക
  print("Shopping list:")
  print(response.output_text)
  ```

  സുപ്രധാനമായ കുറിപ്പുകൾ:

  1. നാം പുതിയ പ്രംപ്റ്റ് നിർമ്മിക്കുന്നു, മുൻപ്രംപ്റ്റിൽ നിന്നുള്ള ഫലം പുതിയ പ്രംപ്റ്റിനോട് ചേർക്കുന്നു:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. നാം പുതിയ അപേക്ഷ നടത്തുന്നു, കൂടാതെ മുൻപ്രംപ്റ്റിൽ ആവശ്യപ്പെട്ട ടോക്കണുകളുടെ എണ്ണം പരിഗണിച്ച്, ഇത്തവണ `max_output_tokens` 1200 ആക്കുന്നു.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ഈ കോഡ് പരീക്ഷിച്ചപ്പൊഴുണ്ടാകുന്ന ഫലം ഇതാണ്:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## നിങ്ങളുടെ സജ്ജീകരണം മെച്ചപ്പെടുത്തുക

ഇതുവരെ നമുക്ക് ലഭിച്ചത് പ്രവർത്തിക്കുന്ന കോഡാണ്, പക്ഷേ കാര്യങ്ങൾ കൂടുതൽ മെച്ചപ്പെടുത്താൻ ചില മാറ്റങ്ങൾ ചെയ്യേണ്ടതാണ്. ചില കാര്യം ചെയ്യേണ്ടത്:

- **സീക്രറ്റുകൾ കോഡിൽ നിന്നും വേർതിരിക്കുക**, ഉദാഹരണത്തിന് API കി പോലുള്ളവ. സീക്രറ്റുകൾ കോഡിൽ ഇടുക ശരിയല്ല, അവ സുരക്ഷിത ഇടത്തെയും സൂക്ഷിക്കണം. സീക്രറ്റുകൾ കോഡിൽ നിന്ന് വേർതിരിക്കാൻ നാം environment variables ഉം `python-dotenv` പോലുള്ള ലൈബ്രറികളും ഉപയോഗിച്ച് ഫയലിൽ നിന്ന് ലോഡ് ചെയ്യാം. ഇതുപോലെ കോഡിൽ കാണാം:

  1. ഇനി ഒരു `.env` ഫയൽ ഇങ്ങനെയാണ് ഉണ്ടാക്കുക:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Microsoft Foundry-ൽ Azure OpenAI-ക്കായി പകരം താഴെ പറയുന്ന environment variables സജ്ജമാക്കണം:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     കോഡിൽ environment variables ഇങ്ങനെ ലോഡ് ചെയ്യും:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ടോക്കൻ ദൈർഘ്യത്തെക്കുറിച്ച് ഒരു കുറിപ്പ്**. ആവശ്യമായ വാചകങ്ങൾ സൃഷ്ടിക്കാൻ എത്ര ടോക്കണുകൾ വേണ്ടിവരും എന്ന് പരിഗണിക്കണം. ടോക്കണുകൾ ചെലവ് വരുത്തുന്നു, അതുകൊണ്ട് കഴിയുന്നിടത്ത് കുറഞ്ഞ ടോക്കണുകൾ ഉപയോഗിക്കാൻ ശ്രമിക്കണം. ഉദാഹരണത്തിന്, പ്രംപ്റ്റ് phrasing കുറച്ച് ടോക്കണുകൾ ഉപയോഗിക്കാൻ സഹായിക്കുന്നുമോ?

  ടോക്കണുകൾ മാറ്റാൻ `max_output_tokens` പാരാമീറ്റർ ഉപയോഗിക്കാം. ഉദാഹരണത്തിന്, 100 ടോക്കണുകൾക്ക് വേണ്ടി ഇത് ചെയ്യും:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **താപനില പരീക്ഷണം**. ഇതുവരെ പറഞ്ഞിട്ടില്ലെങ്കിലും താപനില നമ്മുടെ പ്രോഗ്രാം എങ്ങനെ പ്രവർത്തിക്കും എന്നതിൽ പ്രധാന ഘടകമാണ്. താപനില വലുത് ആണെങ്കിൽ ഔട്ട്പുട്ട് കൂടുതൽ റാൻഡം ആയിരിക്കും. കിഴിവുള്ള താപനിലയ്ക്ക് ഔട്ട്പുട്ട് കൂടുതൽ പ്രവചനശേഷിയുള്ളതാകും. നിങ്ങൾക്കു് ഔട്ട്പുട്ടിൽ വ്യത്യാസം വേണോ എന്ന് പരിശോധിക്കുക.

  താപനില മാറ്റാൻ `temperature` പാരാമീറ്റർ ഉപയോഗിക്കാം. ഉദാഹരണത്തിന്, താപനില 0.5 ആക്കാൻ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ശ്രദ്ധിക്കുക, 1.0-യ്ക്ക് അടുത്ത് ആയിരിക്കും ഔട്ട്പുട്ട് കൂടുതൽ വിവിധത്വം കാണിക്കുക.

- **റീഴണിംഗ് മോഡലുകൾ `temperature` ഉപയോഗിക്കുന്നില്ല**. 2026-ലെ ഒരു പ്രധാന മാറല്‍. Microsoft Foundry-യിലെ നിലവിലുള്ള, പരിഷ്‌കരിക്കപ്പെടാത്ത മോഡലുകൾ **റീഴണിംഗ് മോഡലുകൾ** ആണ് (GPT-5 കുടുംബം, o-സീരിസ്) - അവ **`temperature` അല്ലാതെ `top_p`യും പിന്തുണയ്‌ക്കുന്നില്ല** (`max_tokens` ഇല്ല, `max_output_tokens` ഉപയോഗിക്കണം). `gpt-5-mini`-ക്ക് `temperature` അയച്ചാൽ "parameter not supported" എന്ന് പിശക് വരും. അതുകൊണ്ട് താപനില ഉദാഹരണം പരീക്ഷിക്കാൻ, സ്മാപ്ലിംഗ് നിയന്ത്രണങ്ങൾ പിന്തുണയ്ക്കുന്ന മറ്റൊരു മോഡലിലേക്ക് പോയി - ഉദാഹരണത്തിന് [Microsoft Foundry മോഡൽ കാറ്റലോഗിൽ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ഉള്ള ഒരു ഓപ്പൺ **Llama** മോഡൽ, `Llama-3.3-70B-Instruct` പോലതും, Foundry Models / Azure AI Inference എൻഡ്‌പോയിന്റ് വഴിയോ (githubmodels-* സാമ്പിളുകൾ പോലെ). GPT-5 പോലുള്ള റീഴണിംഗ് മോഡലുകൾക്ക് ഔട്ട്പുട്ട് steering ഈ രീതിയിലാണ്:
  - **പ്രംപ്റ്റ് എഞ്ചിനീയറിംഗ്** - വ്യക്തമായ നിര്‍ദേശങ്ങള്‍, ഉദാഹരണങ്ങള്‍, ഘടിത ഔട്ട്പുട്ട് (പാഠം [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) കാണുക) sampling knob കളുടെ ജോലി ചെയ്യുന്നുവെന്ന് കരുതുന്നു.
  - **റീഴണിംഗ് നിയന്ത്രണങ്ങൾ** - reasoning effort/verbosity പോലുള്ള പാരാമീറ്ററുകൾ, reasoning ൽ ഉള്ള ആഴം latency ഉം ചിലവുകളും തമ്മിൽ സംതുലനം ചെയ്യും.

  ചുരുക്കത്തിൽ: `temperature`/`top_p` പല മോഡലുകളിലും (Llama, Mistral, Phi, GPT-4.x കുടുംബം - എങ്കിൽ GPT-4.x ഡിപ്രിക്കേറ്റ് ആകുന്നു) ഇപ്പോഴും സാധൂകരിക്കപ്പെടുന്നു, പക്ഷെ വഴിതിരിവ് prompt engineering + reasoning controls ആയി മുന്നോട്ട് പോവുകയാണ് GPT-5 പോലുള്ള reasoning മോഡലുകളിൽ.

## അസൈൻമെന്റ്

ഈ അസൈൻമെന്റിനായി, നിങ്ങൾക്ക് എന്ത് നിർമ്മിക്കണമെന്നത് തിരഞ്ഞെടുക്കാം.

ഇവിടെ ചില നിർദേശങ്ങൾ:

- റെസിപ്പി ജനറേറ്റർ ആപ്പ് കൂടുതൽ മെച്ചപ്പെടുത്താൻ temperature മൂല്യങ്ങൾക്കായും പ്രംപ്റ്റുകൾക്കായും കളിച്ച് നോക്കുക.
- ഒരു "സ്റ്റഡി ബഡി" നിർമ്മിക്കുക. ഈ ആപ്പ് ഒരു വിഷയം, ഉദാഹരണത്തിന് Python, സംബന്ധിച്ചും ചോദ്യങ്ങൾ മറുപടി പറയാൻ കഴിയും. നിങ്ങൾക്ക് "Python-ൽ ഒരു പ്രത്യേക വിഷയം എന്ത്?" പോലുള്ള പ്രംപ്റ്റുകൾ ഉണ്ടായിരിക്കാം, അല്ലെങ്കിൽ ഒരു പ്രത്യേക വിഷയം കോഡായി കാണിക്കുക തുടങ്ങിയ പ്രംപ്റ്റ്.
- ചരിത്ര ബോട്ട്, ചരിത്രം ജീവിതമായി മാറ്റുക, ബോട്ടിനെ ഒരു പ്രത്യേക ചരിത്ര കഥാപാത്രമായി കൃത്യമായി നിർദ്ദേശിച്ച് അതിന്റെ ജീവിതം, കാലഘട്ടം സംബന്ധിച്ച ചോദ്യങ്ങൾ ചോദിക്കുക.

## പരിഹാരം

### സ്റ്റഡി ബഡി

താഴെ ഒരു ആരംഭ പ്രംപ്റ്റ് നൽകിയിരിക്കുന്നു, നിങ്ങൾ അത് എങ്ങനെ ഉപയോഗിക്കുകയും ഇഷ്ടാനുസൃതമാക്കുകയും ചെയ്യാമെന്ന് നോക്കുക.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ചരിത്ര ബോട്ട്

ഇതിനായി ഉപയോഗിക്കാവുന്ന ചില പ്രംപ്റ്റുകൾ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## അറിവ് പരിശോധന

താപനില എന്ന ആശയം എന്ത് ചെയ്യുന്നു?

1. ഔട്ട്‌പുട്ട് എത്രമാത്രം റാൻഡം ആകണം എന്ന് നിയന്ത്രിക്കുന്നു.
1. മറുപടി എത്ര വലുത് ആകണം എന്ന് നിയന്ത്രിക്കുന്നു.
1. എത്ര ടോക്കണുകൾ ഉപയോഗിക്കണം എന്ന് നിയന്ത്രിക്കുന്നു.

## 🚀 ചലഞ്ച്

അസൈൻമെന്റ് ചെയ്തപ്പോൾ താപനില മാറ്റി പരീക്ഷിക്കൂ, 0, 0.5, 1 ആക്കി നോക്കൂ. ഓർക്കുക, 0 ഏറ്റവും കുറവ് വ്യത്യാസമുള്ളതും 1 ഏറ്റവും വ്യത്യാസമുള്ളതും ആണ്. നിങ്ങളുടെ ആപ്പിന് ഏത് മൂല്യം ഏറ്റവും നല്ലത്?

## മികച്ച ജോലി! നിങ്ങളുടെ പഠനം തുടരുക

ഈ പാഠം പൂർത്തിയായ ശേഷം, നമ്മുടെ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) കാണുക, നിങ്ങളുടെ Generative AI അറിവ് കൂടുതൽ ഉയർത്താൻ!

പാഠം 7 ലേക്ക് പോയി, നമ്മൾ എങ്ങനെ [ചാറ്റ് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാമെന്ന്](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) കാണും!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->