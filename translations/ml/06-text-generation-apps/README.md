# ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ

[![Building Text Generation Applications](../../../translated_images/ml/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ഈ പാഠത്തിന്റെയും വീഡിയൊ കാണാൻ മുകളിൽ ഉള്ള ചിത്രം ക്ലിക്ക് ചെയ്യുക)_

നിങ്ങൾ ഈ оқуക്രമത്തില്‍ ഇതുവരെ കണ്ടുകൊണ്ടിരിക്കുന്നതുപോലെ പ്രോംപ്റ്റ് പോലുള്ള പ്രധാന ആശയങ്ങളും "പ്രോംപ്റ്റ് എഞ്ചിനീയറിംഗ്" എന്ന ഒരു പൂർണ്ണ വിഷയവുമുണ്ട്. ChatGPT, Office 365, Microsoft Power Platform തുടങ്ങിയ പല ഉപകരണങ്ങളും പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് എന്തെങ്കിലുമുണ്ടാക്കാൻ നിങ്ങൾക്ക് സഹായിക്കുന്നു.

ഒരു അപ്ലിക്കേഷനിൽ ഇത്തരം അനുഭവം ചേർക്കാൻ, പ്രോംപ്റ്റുകൾ, പൂരിപ്പിക്കൽ എന്നിവ പോലുള്ള ആശയങ്ങൾ മനസ്സിലാക്കേണ്ടതുണ്ട്, കൂടാതെ ഉപയോഗിക്കാൻ ഒരു ലൈബ്രറി തിരഞ്ഞെടുക്കണം. ഇതാണ് നിങ്ങൾക്ക് ഈ അധ്യായത്തിൽ പഠിക്കേണ്ടത്.

## പരിചയം

ഈ അധ്യായത്തിൽ, നിങ്ങൾ ചെയ്യും:

- openai ലൈബ്രറിയും അതിന്റെ പ്രധാന ആശയങ്ങളും പഠിക്കുക.
- openai ഉപയോഗിച്ച് ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കുക.
- ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കാൻ പ്രോംപ്റ്റ്, താപനില, ടോക്കണുകൾ തുടങ്ങിയ ആശയങ്ങൾ എങ്ങനെ ഉപയോഗിക്കാമെന്ന് മനസ്സിലാക്കുക.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം കഴിഞ്ഞാൽ, നിങ്ങൾക്ക് കഴിയും:

- ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ എന്നത് എന്താണെന്ന് വിശദീകരിക്കുക.
- openai ഉപയോഗിച്ച് ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കുക.
- കൂടുതൽ അല്ലെങ്കിൽ കുറവ് ടോക്കണുകൾ ഉപയോഗിച്ച് നിങ്ങളുടെ അപ്ലിക്കേഷൻ ക്രമീകരിക്കുകയും ഫലത്തിനായി താപനില മാറുകയും ചെയ്യുക.

## ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ എന്താണ്?

സാധാരണയായി നിങ്ങൾ ഒരു അപ്ലിക്കേഷൻ നിർമ്മിക്കുമ്പോൾ ഇതുപോലുള്ള ഏതെവിടെ ഒരു ഇന്റർഫേസ് ഉണ്ടാകും:

- കമാൻഡ് അടിസ്ഥാനത്തിൽ. കൺസോൾ അപ്ലിക്കേഷനുകൾ സാധാരണയായി ഒരു കമാൻഡ് ടൈപ്പുചെയ്യുമ്പോൾ അത് ഒരു ജോലി നിർവ്വഹിക്കുന്ന അപ്ലിക്കേഷനുകളാണ്. ഉദാഹരണത്തിന്, `git` ഒരു കമാൻഡ് അടിസ്ഥാനത്തിലുള്ള അപ്ലിക്കേഷൻ ആണ്.
- ഉപയോക്തൃ ഇന്റർഫേസ് (UI). ചില അപ്ലിക്കേഷനുകൾക്ക് ഗ്രാഫիկական ഉപയോക്തൃ ഇന്റർഫേസുകൾ (GUIs) ഉണ്ടാകാം, അവിടെ നിങ്ങൾ ബട്ടണുകൾ ക്ലിക്ക് ചെയ്യുകയും ടെക്സ്റ്റ് നൽകുകയും പതിവും തിരഞ്ഞെടുക്കുകയും ചെയ്യാം.

### കൺസോൾ & UI അപ്ലിക്കേഷനുകൾ പരിമിതമാണ്

താഴെ കാണിച്ച കമാൻഡ്-അധിഷ്ഠിത അപ്ലിക്കേഷനുമായ് താരതമ്യപ്പെടുത്തുക:

- **ഇത് പരിമിതമാണ്**. നിങ്ങൾക്ക് ഏതെങ്കിലും കമാൻഡ് ടൈപ്പ് ചെയ്യാൻ കഴിയില്ല, അപ്ലിക്കേഷൻ പിന്തുണയ്ക്കുന്നവ മാത്രമേ.
- **ഭാഷാ പ്രത്യേകമാണ്**. ചില അപ്ലിക്കേഷനുകൾ പല ഭാഷകളെ പിന്തുണയ്ക്കാം, എന്നാൽ സ്വാഭാവികമായി അത് ഒരു പ്രത്യേക ഭാഷയ്ക്കായി നിർമ്മിച്ചിരിക്കുന്നു, കൂടുതൽ ഭാഷാ പിന്തുണ ചേർക്കാനാവും.

### ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷനുകളുടെ ഗുണങ്ങൾ

അതിനാൽ, ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ എങ്ങിനെയാണ് വ്യത്യസ്തമെന്ന്?

ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷനിൽ നിങ്ങൾക്ക് കൂടുതൽ സ്വാതന്ത്ര്യമുണ്ട്, ഒരു നിശ്ചിത കമാൻഡ് സെറ്റിലോ നിർവ്വചിച്ച ഭാഷയിലോ നിങ്ങൾ പൂട്ടിപ്പെടുകയില്ല. പകരം, നിങ്ങൾ പ്രകൃതിഭാഷ ഉപയോഗിച്ച് അപ്ലിക്കേഷനുമായി ആശയവിനിമയം നടത്താം. മറ്റൊരു ഗുണം നിങ്ങൾ ഇതിനകം ഒരു വിശാലമായ കോർപ്പസ് വിവരങ്ങളിൽ പരിശീലിപ്പിച്ച ഡേറ്റാ സ്രോതസിനോടൊപ്പമാണ് ഇടപഴകുന്നത് എന്നതാണ്, ഒരു പരമ്പരാഗത അപ്ലിക്കേഷൻ ഡേറ്റാബേസിൽ ഉള്ളതിന്റെ പരിധിയിൽ വരാം.

### ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ കൊണ്ട് എന്ത് നിർമ്മിക്കാം?

നിങ്ങൾക്ക് നിരവധി കാര്യങ്ങൾ നിർമ്മിക്കാം. ഉദാഹരണത്തിന്:

- **ചാറ്റ്ബോട്ട്**. നിങ്ങളുടെ കമ്പനിയും അതിന്റെ ഉൽപ്പന്നങ്ങളും സംബന്ധിച്ച ചോദ്യങ്ങൾക്ക് ഉത്തരമ നൽകുന്ന ഒരു ചാറ്റ്ബോട്ട് നല്ല ഒരു തിരഞ്ഞെടുപ്പാകും.
- **സഹായി**. LLMകൾ ടെക്സ്റ്റ് സംഗ്രഹിക്കൽ, ഇൻസൈറ്റുകൾ നേടുക, പുനർനിർമ്മിച്ച ടെക്സ്റ്റ് (റിസ്യൂമെ പോലുള്ള) എന്നിവയിൽ മികച്ചതാണ്.
- **കോടിംഗ് സഹായി**. നിങ്ങൾ ഉപയോഗിക്കുന്ന ഭാഷാ മോഡലിന്റെ അടിസ്ഥാനത്തിൽ, നിങ്ങള്‍ക്ക് കോഡ് എഴുതാൻ സഹായിക്കുന്ന ഒരു കോഡ് അസിസ്റ്റന്റ് നിർമ്മിക്കാൻ കഴിയും. ഉദാഹരണത്തിന്, GitHub Copilot പോലുള്ള ഉൽപ്പന്നത്തിലും ChatGPTൽ നിങ്ങള്‍ക്ക് കോഡ് എഴുതാൻ സഹായം ലഭിക്കും.

## എങ്ങനെ തുടങ്ങാം?

നിങ്ങൾ സാധാരണയായി രണ്ട് രീതികളിൽ ഒരുപ്രകാരം LLM-നെ ഇന്റഗ്രേറ്റ് ചെയ്യേണ്ടതുണ്ട്:

- API ഉപയോഗിക്കുക. ഇവിടെ നിങ്ങൾ നിങ്ങളുടെ പ്രോംപ്റ്റ് ഉപയോഗിച്ച് വെബ് അഭ്യർത്ഥനകൾ നിർമ്മിക്കുന്നു, ലഭിച്ച Generated text واپس ലഭിക്കുന്നു.
- ലൈബ്രറി ഉപയോഗിക്കുക. ലൈബ്രറികൾ API കോൾസുകൾ ഉൾക്കൊള്ളിച്ച് ഉപയോഗിക്കാൻ എളുപ്പമാക്കുന്നു.

## ലൈബ്രറികൾ/SDKകൾ

LLMs-വുമായ് ജോലി ചെയ്യാൻ ചില പ്രശസ്തമായ ലൈബ്രറികൾ ഉണ്ട്:

- **openai**, ഈ ലൈബ്രറി നിങ്ങളുടെ മോഡലുമായി എളുപ്പത്തിൽ കണക്റ്റ് ചെയ്തു പ്രോംപ്റ്റുകൾ അയക്കാൻ സഹായിക്കുന്നു.

പിന്നീട് ഉയർന്ന തലത്തിലുള്ള ലൈബ്രറികളും ഉണ്ട്:

- **Langchain**. Langchain പ്രശസ്തമായ ലൈബ്രറിയാണ് Python പിന്തുണയ്ക്കുന്നു.
- **Semantic Kernel**. Semantic Kernel മൈക്രോസോഫ്റ്റ് നിർമിച്ച ഒരു ലൈബ്രറിയാണ്, C#, Python, Java ഭാഷകളിൽ പിന്തുണ ഉണ്ട്.

## openai ഉപയോഗിച്ച് ആദ്യത്തെ അപ്ലിക്കേഷൻ

ആദ്യത്തെ അപ്ലിക്കേഷൻ എങ്ങനെ നിർമ്മിക്കാം, എത്ര ലൈബ്രറികൾ ആവശ്യമുള്ളതും ഇതുവരെ നോക്കാം.

### openai ഇൻസ്റ്റാൾ ചെയ്യുക

OpenAI അല്ലെങ്കിൽ Azure OpenAI-യുമായി സംവദിക്കാൻ നിരവധി ലൈബ്രറികൾ ലഭ്യമാണ്. C#, Python, JavaScript, Java തുടങ്ങി പല പ്രോഗ്രാമിംഗ് ഭാഷകളും ഉപയോഗിക്കാം. നമ്മൾ `openai` Python ലൈബ്രറി ഉപയോഗിക്കാനാണ് തീരുമാനിച്ചിട്ടുള്ളത്, അതിനാൽ `pip` ഉപയോഗിച്ച് ഇൻസ്റ്റാൾ ചെയ്യാം.

```bash
pip install openai
```

### ഒരു റിസോഴ്സ് സൃഷ്ടിക്കുക

നിങ്ങൾ താഴെ പറയുന്ന ഘട്ടങ്ങൾ നടത്തി야 합니다:

- Azure അക്കൗണ്ട് സൃഷ്ടിക്കുക [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI-യിലേക്ക് ആക്‌സസ് നേടുക. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) സന്ദർശിച്ച് ആക്‌സസ് അഭ്യർത്ഥിക്കുക.

  > [!NOTE]
  > എഴുതുന്നതിനിടയിൽ, Azure OpenAI-ക്ക് ആക്‌സസ് അപേക്ഷിക്കേണ്ടതുണ്ട്.

- Python ഇൻസ്റ്റാൾ ചെയ്യുക <https://www.python.org/>
- Azure OpenAI സർവീസ് റിസോഴ്സ് സൃഷ്ടിച്ചിട്ടുണ്ടാകണം. ഇത് എങ്ങനെ ചെയ്യാമെന്ന് [സ്രോതസ് സൃഷ്ടിക്കൽ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) അത് കാണുക.

### API കീയും എൻഡ്പോയിന്റും കണ്ടെത്തുക

ഇവിടെ, നിങ്ങളുടെ `openai` ലൈബ്രറി ഉപയോഗിക്കുന്ന API കീ അറിയിക്കണം. നിങ്ങളുടെ API കീ കണ്ടെത്താൻ, Azure OpenAI റിസോഴ്സ് "Keys and Endpoint" വിഭാഗം കാണുക, "Key 1" മൂല്യം കോപ്പി ചെയ്യുക.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ഈ വിവരങ്ങൾ കോപ്പി ചെയ്തിട്ടുണ്ടെങ്കിൽ, ലൈബ്രറികൾക്ക് ഇത് ഉപയോഗിക്കാൻ നിർദ്ദേശിക്കാം.

> [!NOTE]
> നിങ്ങളുടെ API കീ നിങ്ങളുടെ കോഡ് മുതൽ വേർതിരിക്കുന്നത് നല്ലതാണ്. ഇത് പരിസ്ഥിതി വ്യത്യാസങ്ങൾ ഉപയോഗിച്ച് ചെയ്യാം.
>
> - പരിസ്ഥിതി വ്യത്യാസായി `OPENAI_API_KEY` നിങ്ങളുടെ API കീ ആയി സജ്ജീകരിക്കുക.
>   `export OPENAI_API_KEY='sk-...'`

### Azure കോൺഫിഗറേഷൻ ക്രമീകരിക്കൽ

നിങ്ങൾ Azure OpenAI (ഇപ്പോൾ Microsoft Foundry ഭാഗമായത്) ഉപയോഗിച്ചാൽ, നിങ്ങൾ ക്രമീകരിക്കൽ ഇങ്ങനെ ചെയ്യാം. നാം സ്റ്റാൻഡേർഡ് അഥവാ `OpenAI` ക്ലയന്റ് ഉപയോഗിക്കുന്നു, Azure OpenAI `/openai/v1/` എൻഡ്പോയിന്റിലെ, ഇത് Responses API വിന്റെ സഹായത്തോടെ പ്രവർത്തിക്കുന്നു, `api_version` ആവശ്യമില്ല:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

മുകളിൽ പറയുന്നത്:

- `api_key`, ഇത് Azure പോർട്ടലിലോ Microsoft Foundry പോർട്ടലിലോ കണ്ടു കിട്ടുന്ന നിങ്ങളുടെ API കീ ആണ്.
- `base_url`, ഇത് നിങ്ങളുടെ Foundry റിസോഴ്സ് എൻഡ്പോയിൻറ് '/openai/v1/' ചേർന്നതാണ്. ശ്രദ്ധാലുവായ v1 എൻഡ്പോയിന്റ് OpenAIയും Azure OpenAI യും ഒരുപോലെ കൈകാര്യം ചെയ്യുന്നു, പ്രത്യേക `api_version` മാനേജ്‌മെന്റ് ഇല്ലാതെ.

> [!NOTE] > `os.environ` ഉപയോഗിച്ച് പരിസ്ഥിതി വ്യത്യാസങ്ങൾ വായിക്കാൻ കഴിയും. നിങ്ങൾക്ക് `AZURE_OPENAI_API_KEY`യും `AZURE_OPENAI_ENDPOINT`വും വായിക്കാം. ഈ പരിസ്ഥിതി വ്യത്യാസങ്ങൾ നിങ്ങളുടെ ടെർമിനലിലോ `dotenv` പോലുള്ള ലൈബ്രറി ഉപയോഗിച്ചോ സജ്ജീകരിക്കാം.

## ടെക്സ്റ്റ് സൃഷ്ടിക്കുക

ടെക്സ്റ്റ് സൃഷ്ടിക്കാൻ Responses API `responses.create` രീതിയാണ് ഉപയോഗിക്കുന്നത്. ഉദാഹരണമായി:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ഇത് നിങ്ങളുടെ മോഡൽ ഡിപ്പ്ലോയ്മെന്റ് പേര് ആണ്
    input=prompt,
    store=False,
)
print(response.output_text)
```

മുകളിൽ കാണുന്ന കോഡിൽ, നാം ഒരു റസ്പോൺസ് സൃഷ്ടിക്കുന്നു, ഉപയോഗിക്കേണ്ട മോഡൽയും പ്രോംപ്റ്റും പാസായി. തുടർന്ന് `response.output_text` വഴി നിർമ്മിച്ച ടെക്സ്റ്റ് പ്രിന്റ് ചെയ്യുന്നു.

### മള്‍ട്ടി-ടേൺ സംഭാഷണങ്ങൾ

Responses API ഒരേൊരു ടെക്സ്റ്റ് ജനറേഷൻക്കും മള്‍ട്ടി-ടേൺ ചാറ്റ്ബോട്ടുകൾക്കും അനുയോജ്യമാണ് - നിങ്ങൾ `input` ലിസ്റ്റിൽ സന്ദേശങ്ങൾ നൽകിയാണ് സംഭാഷണം നിർമ്മിക്കുന്നത്:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

ഈ ഫംഗ്ഷണാലിറ്റി അടുത്ത അധ്യായത്തിൽ കൂടുതല്‍ വിശദീകരിക്കും.

## അഭ്യാസം - നിങ്ങളുടെ ആദ്യത്തെ ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ

openai ക്രമീകരണവും സെറ്റപ്പും പഠിച്ചപ്പോൾ, നിങ്ങളുടെ ആദ്യത്തെ ടെക്സ്റ്റ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കാം. ഇതിനായി താഴെ പറയുന്ന ഘട്ടങ്ങൾ പിന്തുടരുക:

1. ഒരു വെർച്ച്വൽ എൻവയേണ്മെന്റ് സൃഷ്ടിച്ച് openai ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > നിങ്ങൾ Windows ഉപയോഗിക്കുന്നെങ്കിൽ `source venv/bin/activate` പകരം `venv\Scripts\activate` എന്ന് ടൈപ്പ് ചെയ്യുക.

   > [!NOTE]
   > നിങ്ങളുടെ Azure OpenAI കീ കണ്ടെത്താൻ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) സന്ദർശിച്ച് `Open AI` എന്ന് തിരയുക, പിന്നെ `Open AI resource` തിരഞ്ഞെടുക്കുക, അപ്പോൾ `Keys and Endpoint`-ൽ നിന്ന് `Key 1` കോപ്പി ചെയ്യുക.

1. _app.py_ എന്ന ഫയൽ സൃഷ്ടിച്ച് ഇതിങ്ങനെ കോഡ് നൽകുക:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # നിങ്ങളുടെ പൂർത്തിയറിയിപ്പ് കോഡ് ചേർക്കുക
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ഉപയോഗിച്ച് ഒരു അഭ്യർത്ഥന жасаുക
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # പ്രതികരണം പ്രിന്റ് ചെയ്യുക
   print(response.output_text)
   ```

   > [!NOTE]
   > നിങ്ങൾ plain OpenAI (Azure അല്ല) ഉപയോഗിക്കുന്നുവെങ്കിൽ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ഉപയോഗിക്കുക (base_url ആവശ്യമില്ല), മോഡൽ നാമം deployment നാമത്തിന് പകരം `gpt-4o-mini` പോലുള്ളത് നൽകാം.

   നിങ്ങൾക്ക് ഇങ്ങനെ ഫലം കാണാം:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## വ്യത്യസ്ത ആവശ്യങ്ങൾക്ക് വ്യത്യസ്ത പ്രോംപ്റ്റുകൾ

ഇപ്പോൾ നിങ്ങൾ പ്രോംപ്റ്റ് ഉപയോഗിച്ച് ടെക്സ്റ്റ് സൃഷ്ടിക്കാൻ പഠിച്ചു. നിങ്ങൾക്ക് ഒരു പ്രോഗ്രാം റണ്ണിങ് ആണെന്നും ഇത് മാറ്റി വ്യത്യസ്ത തരത്തിലുള്ള ടെക്സ്റ്റ് നിർമിക്കാം.

പ്രോംപ്റ്റുകൾ എല്ലാ തരത്തിലുള്ള ജോലികൾക്കും ഉപയോഗിക്കാം. ഉദാഹരണമായി:

- **ടെക്സ്റ്റ് തരം സൃഷ്ടിക്കുക**. ഉദാഹരണത്തിന്, കവിത, ക്വിസ് ചോദ്യങ്ങൾ എന്നിവ നിർമിക്കാം.
- **വിവരം അന്വേഷിക്കുക**. 'വെബ് ഡെവലപ്പ്മെന്റിൽ CORS എന്താണ്?' പോലുള്ള വിവരങ്ങൾ അന്വേഷിക്കാൻ പ്രോംപ്റ്റുകൾ ഉപയോഗിക്കാം.
- **കോഡ് നിർമ്മിക്കുക**. പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് കോഡ് സൃഷ്ടിക്കാം, ഉദാഹരണത്തിന്, ഇമെയിൽ പരിശോധനക്കായി റെഗുലർ എക്‌സ്പ്രഷൻ നിർമ്മിക്കുക, അല്ലെങ്കിൽ ഒരു വെബ് അപ്ലിക്കേഷനു പോലെ പൂർണ്ണ പ്രോഗ്രാം സൃഷ്ടിക്കാം.

## കൂടുതൽ പ്രായോഗിക ഉദാഹരണം: ഒരു റെസിപ്പി ജനറേറ്റർ

നിങ്ങൾക്ക് വീട്ടിൽ ചില സാമഗ്രികൾ ഉണ്ടെന്നും, കൂടാതെ ഭക്ഷണം പാകം ചെയ്യണമെന്നുമാണെന്നാണ് കരുതുക. അതിനു നിങ്ങൾക്ക് ഒരു റെസിപ്പി വേണം. റെസിപ്പികൾ കണ്ടെത്താൻ വെബ് സർച്ച് എഞ്ചിൻ ഉപയോഗിക്കാം, അല്ലെങ്കിൽ LLM ഉപയോഗിക്കാം.

നിങ്ങൾ ഇങ്ങനെ ഒരു പ്രോംപ്റ്റ് എഴുതാം:

> "ഇനിപ്പറയുന്ന സാമഗ്രികൾ ഉപയോഗിച്ച ഒരു വിഭവത്തിന് 5 റെസിപ്പികൾ കാണിക്കുക: കോഴി, ഉരുളക്കിഴങ്ങ്, കാരറ്റ്. ഓരോ റെസിപ്പിക്കും ഉപയോഗിച്ച എല്ലാ സാമഗ്രികളും ലിസ്റ്റ് ചെയ്യുക."

മുകളിൽ പറഞ്ഞ പ്രോംപ്റ്റിന്റെ അടിസ്ഥാനത്തിൽ, നിങ്ങൾക്ക് ഇങ്ങനെ ഒരു മറുപടി ലഭിക്കാം:

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

ഈ ഫലം വളരെ നല്ലതാണ്, എന്നെന്ത് പാകം ചെയ്യേണ്ടതെന്ന് അറിയുന്നു. ഇപ്പോഴത്തെ മെച്ചപ്പെടുത്തലുകൾക്ക്:

- ഞാൻ ഇഷ്ടപ്പെടുന്നില്ലാത്ത അല്ലെങ്കിൽ അലർജിയുള്ള സാമഗ്രികൾ ഫിൽട്ടർ ചെയ്യുക.
- എന്റെ വീട്ടിലില്ലാത്ത സാമഗ്രികൾക്കായി ഷോപ്പിങ് ലിസ്റ്റ് പിറവിയാക്കുക.

മേൽ പറഞ്ഞ സാഹചര്യങ്ങൾക്ക്, ഞങ്ങൾ ഒരു അധിക പ്രോംപ്റ്റ് ചേർക്കാം:

> "എനിക്ക് അലർജി ഉള്ളതിനാൽ വെളുത്തുള്ളി ഉള്ള റെസിപ്പികൾ നീക്കം ചെയ്യുക, പകരം മറ്റേതെങ്കിലും ചേർക്കുക. കൂടാതെ, കോഴി, ഉരുളക്കിഴങ്ങ്, കാരറ്റ് എന്നിവAlready വീട്ടിലുണ്ടെന്നും കണക്കിലൊക്കി റെസിപ്പികൾക്കുള്ള ഷോപ്പിംഗ് ലിസ്റ്റ് ഉണ്ടാക്കുക."

ഇപ്പോൾ നിങ്ങൾക്ക് പുതിയ ഒരു ഫലം ആണ്:

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

ഇത് നിങ്ങളുടെ അഞ്ചു റെസിപ്പികൾ ആണ്, വെളുത്തുള്ളി ഇല്ലാത്തവ, കൂടാതെ നിങ്ങൾ വീട്ടിൽ ഉള്ള സാധനങ്ങൾ അടിസ്ഥാനമാക്കി ഒരു ഷോപ്പിങ് ലിസ്റ്റും ഉണ്ട്.

## അഭ്യാസം - ഒരു റെസിപ്പി ജനറേറ്റർ നിർമ്മിക്കുക

ഇപ്പോൾ നാം ഒരു സിനാരിയോ കളിച്ചതിനിടെ, നിർമിച്ചിട്ടുള്ള സിനാരിയോയുടെ പരിണാമം അനുയായിച്ച് കോഡ് എഴുതാം. കീഴ്‌വഴക്കങ്ങൾ സ്വീകരിക്കുക:

1. നിലവിലുള്ള _app.py_ ഫയൽ ആരംഭികമായി ഉപയോഗിക്കുക
1. `prompt` വേരിയബിൾ കണ്ടെത്തി അതിന്റെ കോഡ് താഴെ പറയുന്നതുപോലെ മാറ്റുക:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

ഇപ്പോൾ ഈ കോഡ് റൺ ചെയ്താൽ, ഇങ്ങനെ ഒരു ഫലം കണ്ടെത്തും:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

> ശ്രദ്ധിക്കുക, നിങ്ങളുടെ LLM nondeterministic ആണ്, അതിനാൽ പ്രോഗ്രാം റൺ ചെയ്യുമ്പോഴെല്ലാം വ്യത്യസ്ത ഫലം ലഭിക്കാം.

നന്നായി, എങ്കിൽ മെച്ചപ്പെടുത്താനാവുന്നതെങ്ങനെ എന്ന് നോക്കാം. മെച്ചപ്പെടുത്താൻ കോഡ് ഫ്ലക്സിബിൾ ആക്കണം, ഇതുവരെ ഉള്ള റെസിപ്പികളുടെ എണ്ണം കൂടാതെ സാമഗ്രികൾ മാറ്റാൻ കഴിഞ്ഞാൽ നന്നാകും.

1. കോഡിൽ താഴെ പറയുന്ന മാറ്റം ചെയ്യാം:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # റെസിപ്പികളുടെ എണ്ണം പ്രാംപ്റ്റിലും ഘടകങ്ങളിലും ഇടുക
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

പരീക്ഷണമായി ഈ കോഡ് റൺ ചെയ്യാം:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ഫിൽട്ടർ ചെയ്യൽ, ഷോപ്പിംഗ് ലിസ്റ്റ് ചേർത്തു മെച്ചപ്പെടുത്തുക

ഇനി നമ്മുടെ അപ്ലിക്കേഷൻ റെസിപ്പികൾ നിർമ്മിക്കാൻ കഴിയുന്ന ഫ്ലക്സിബിൾ ഒരു അപ്ലിക്കേഷനായി മാറി. കാരണം, റെസിപ്പികളുടെ എണ്ണം കൂടാതെ ഉപയോഗിക്കുന്ന സാമഗ്രികളും ഉപയോക്താവിൽ നിന്നെയാണ്.

കൂടുതൽ മെച്ചപ്പെടുത്താൻ, താഴെ പറയുന്നതുകൾ ചേർക്കണം:

- **സാമഗ്രികൾ ഫിൽട്ടർ ചെയ്യുക**. ഇഷ്ടമില്ലാത്ത അല്ലെങ്കിൽ അലർജി ഉള്ള സാമഗ്രികൾ ഫിൽട്ടർ ചെയ്യാൻ കഴിയണം. ഇതിന്, നിലവിലുള്ള പ്രോംപ്റ്റിൽ ഒരു ഫിൽട്ടർ കോൺഡിഷൻ ചേർക്കാം, ഇങ്ങനെ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

മുകളിൽ, പ്രോംപ്റ്റിന്റെ അവസാനം `{filter}` ചേർക്കുന്നു, ഫിൽട്ടർ മൂല്യം ഉപയോക്താവിൽ നിന്നു സ്വീകരിക്കുന്നു.

പ്രോഗ്രാം റൺ ഇന്പുട്ട് ഉദാഹരണം ഇങ്ങനെ കാണാം:

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

കാണുന്നപോലെ, പാൽ ഉള്ള ഡിഷുകൾ ഫിൽട്ടർ ചെയ്തിട്ടുണ്ട്. എന്നാൽ നിങ്ങൾക്ക് ലാക്ടോസ് മുന്‍‌ഗാമി ഉണ്ടെങ്കിൽ പനീരും ഫിൽട്ടർ ചെയ്യണം, അതിനാൽ വ്യക്തമായ വിശദീകരണം ആവശ്യമാണ്.


- **ഒരു ഷോപ്പിംഗ് ലിസ്റ്റ് ഉണ്ടാക്കുക**. ഞങ്ങൾ വീട്ടിൽ നമുക്ക് ഉണ്ടായിട്ടുള്ളതിന്റെ അടിസ്ഥാനത്തിൽ ഒരു ഷോപ്പിംഗ് ലിസ്റ്റ് ഉണ്ടാക്കണമെന്ന് ആഗ്രഹിക്കുന്നു.

  ഈ ഫംഗ്ഷനാലിറ്റിക്ക്, നാം എല്ലാം ഒരു പ്രോംപ്റ്റിൽ പരിഹരിക്കാൻ ശ്രമിക്കാമോ അല്ലെങ്കിൽ രണ്ട് പ്രോംപ്റ്റുകളിൽ വിഭജിക്കാമോ. രണ്ടാമത്തെ സമീപനം ശ്രമിക്കാം. ഇവിടെ നാം ഒരു അധിക പ്രോംപ്റ്റ് ചേർക്കുന്നത് നിർദ്ദേശിക്കുന്നു, പക്ഷേ അത് പ്രവർത്തിക്കാൻ, ആദ്യ പ്രോംപ്റ്റിലെ ഫലം പശ്ചാത്തലമായി രണ്ടാമത്തെ പ്രോംപ്റ്റിലേയ്ക്ക് ചേർക്കേണ്ടതാണ്.

  കോഡിൽ ആദ്യ പ്രോംപ്റ്റിൽ നിന്നുള്ള ഫലം പ്രിന്റ് ചെയ്യുന്ന ഭാഗം കണ്ടെത്തി താഴെ കാണിക്കുന്ന കോഡ് ചേർക്കുക:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # പ്രതികരണം മടക്കികാണിക്കുക
  print("Shopping list:")
  print(response.output_text)
  ```

  താഴെ പറയുന്ന കാര്യങ്ങൾ ശ്രദ്ധിക്കുക:

  1. നാം പുതിയ പ്രോംപ്റ്റ് തയ്യാറാക്കുന്നു, പഴയ പ്രോംപ്റ്റിന്റെ ഫലം പുതിയ പ്രോംപ്റ്റിലേക്ക് ചേർക്കുന്നു:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. നാം പുതിയ ആവശ്യം അയക്കുന്നുണ്ട്, പക്ഷേ ആദ്യ പ്രോംപ്റ്റിൽ ആവശ്യപ്പെട്ട ടോക്കൺ സംഖ്യ കൂടി പരിഗണിച്ച്, ഈ തവണ `max_output_tokens` 1200 ആക്കി പറയുന്നു.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ഈ കോഡ് പരീക്ഷിക്കുമ്പോൾ, ഇതാ നമ്മൾ ലഭിക്കുന്ന ഔട്ട്പുട്ട്:

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

ഇപ്പോൾ നമുക്ക് ഉള്ളത് പ്രവർത്തിക്കുന്ന ഒരു കോഡാണ്, എന്നാൽ കൂടുതൽ മെച്ചപ്പെടുത്താൻ ചില കുറവുകൾ ഉണ്ട്. നാം ചെയ്യേണ്ട ചില കാര്യങ്ങൾ:

- **സീക്രറ്റുകൾ കോഡിൽ നിന്നു വേർതിരിക്കുക**, API കീ പോലുള്ള. രഹസ്യങ്ങൾ കോഡിൽ ഇടുന്നതല്ല, അവ ഒരു സുരക്ഷിത സ്ഥലത്തു സൂക്ഷിക്കണം. രഹസ്യങ്ങൾ കോഡിൽ നിന്നും വേർതിരിക്കാൻ നാം പരിസ്ഥിതി വ്യത്യാസങ്ങൾ ഉപയോഗിക്കാം, കൂടാതെ `python-dotenv` പോലുള്ള ലൈബ്രറികൾ ഉപയോഗിച്ച് ഫയലിൽ നിന്ന് ലോഡ് ചെയ്യാം. കോഡിൽ ഇത് എങ്ങനെ കാണപ്പെടും:

  1. പിന് കാണുന്ന ഉള്ളടക്കത്തോടെ ഒരു `.env` ഫയൽ സൃഷ്ടിക്കുക:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ശ്രദ്ധിക്കുക, Microsoft Foundryയിലെ Azure OpenAI-യ്ക്ക്, താഴെ പറയുന്ന പരിസ്ഥിതി വ്യത്യാസങ്ങൾ സജ്ജീകരിക്കേണ്ടതുണ്ട്:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     കോഡിൽ, പരിസ്ഥിതി വ്യത്യാസങ്ങൾ ഇങ്ങനെ ലോഡ് ചെയ്യാം:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ടോക്കൺ നീളം കുറിച്ചുള്ള ഒരു കുറിപ്പ്**. നാം 얼마나 ടോക്കൺ ആവശ്യമാണെന്ന് പരിഗണിക്കണം. ടോക്കൺ ഉപയോഗിക്കുന്നത് ചിലവ് വരുത്തും, അതിനാൽ എത്രഗണമായ ടോക്കൺ ഉപയോഗിക്കുന്നുവെന്ന് സംയമനം പാലിക്കുക. ഉദാഹരണത്തിന്, പ്രോംപ്റ്റ് എളുപ്പത്തിൽ കുറച്ച് ടോക്കണുകളിൽ എഴുതാൻ പറ്റുമോ എന്ന് നോക്കുക.

  ടോക്കൺ മാറ്റാൻ, `max_output_tokens` പാരാമീറ്റർ ഉപയോഗിക്കാം. ഉദാഹരണത്തിന്, നിങ്ങൾക്ക് 100 ടോക്കൺ വേണമെങ്കിൽ, ഇങ്ങനെ ചെയ്യാം:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **താപനില (temperature) പരീക്ഷണം**. ഇതുവരെ താപനിലയെപ്പറ്റി പറയാതിരിക്കുകയുണ്ടായി, എന്നാൽ നമ്മുടെ പ്രോഗ്രാം എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്ന് അത് വളരെ പ്രധാനമാകുന്നു. താപനില മൂല്യം കൂടുതലായാൽ output കൂടുതൽ യാദൃച്ഛികമായിരിക്കും. കുറഞ്ഞാൽ output കൂടുതൽ പ്രവചിക്കാവുന്നതാകും. നിങ്ങളുടെ output-ൽ വ്യത്യാസം വേണമോ എന്ന് നിലനിര്‍ത്തുക.

  താപനില മാറ്റാൻ, `temperature` പാരാമീറ്റർ ഉപയോഗിക്കാം. ഉദാഹരണത്തിന്, താപനില 0.5 ആക്കാൻ ഇങ്ങനെ ചെയ്യാം:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ശ്രദ്ധിക്കുക, 1.0-ന് அருகിലായത് output കൂടുതൽ വ്യത്യാസമുള്ളതാക്കും.

## അസൈൻമെന്റ്

ഈ അസൈൻമെന്റിന് നിങ്ങൾക്ക് എന്ത് നിർമ്മിക്കാമെന്ന് തെരഞ്ഞെടുക്കാം.

ഇവിടെ ചില നിർദ്ദേശങ്ങൾ ആണ്:

- റെസിപി ജനറേറ്റർ ആപ്പ് മെച്ചപ്പെടുത്താൻ ശ്രമിക്കുക. താപനില മൂല്യങ്ങൾ, പ്രോംപ്റ്റുകൾ എന്നിവ പരീക്ഷിച്ച് എന്ത് നേടാമെന്ന് നോക്കുക.
- “സ്റ്റഡി ബഡി” സൃഷ്ടിക്കുക. ഈ ആപ്പ് ഒരു വിഷയം സംബന്ധിച്ച ചോദ്യം ഉത്തരം നൽകാൻ കഴിയണം. ഉദാഹരണത്തിന് Python എന്നത്; "Python-ൽ ഒരു പ്രത്യേക വിഷയം എന്ത്?" പോലുള്ള പ്രോംപ്റ്റുകൾ ഉണ്ടാക്കാം, അല്ലെങ്കിൽ "ഒരു പ്രത്യേക വിഷയത്തിന് നിർദ്ദേശിച്ച കോഡ് കാണിക്കൂ" പോലെയുള്ള പ്രോംപ്റ്റുകൾ ഉണ്ടാകാം.
- ചരിത്ര ബോട്ട്, ചരിത്രം ജീവനോടെ വരുത്തുക, ബോട്ടിന് ഒരു പ്രാചീന ചരിത്ര കഥാപാത്രം ഇരിക്കാൻ നിർദ്ദേശിക്കുക, അതിന്റെ ജീവിതത്തെയും സമയത്തെയും കുറിച്ച് ചോദ്യങ്ങൾ ചോദിക്കുക.

## പരിഹാരം

### സ്റ്റഡി بഡി

താഴെയുള്ളതൊരു തുടങ്ങിയ പ്രോംപ്റ്റാണ്, നിങ്ങൾ അതിനെ എങ്ങനെ ഉപയോഗിക്കാമെന്ന് കൂടി പരിഗണിക്കുക.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ചരിത്ര ബോട്ട്

നിങ്ങൾ ഉപയോഗിക്കാൻ കഴിയുന്ന ചില പ്രോംപ്റ്റുകൾ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## അറിവ് പരിശോധന

താപനില സങ്കല്പം എന്ത് ചെയ്യുന്നു?

1. ഇത് output എത്ര യാദൃച്ഛികമാണെന്ന് നിയന്ത്രിക്കുന്നു.
1. ഇത് പ്രതികരണത്തിന്റെ വലിപ്പം നിയന്ത്രിക്കുന്നു.
1. ഇത് ഉപയോഗിക്കുന്ന ടോക്കണുകളുടെ എണ്ണം നിയന്ത്രിക്കുന്നു.

## 🚀 ചലഞ്ച്

അസൈൻമെന്റിൽ പ്രവർത്തിക്കുമ്പോൾ, താപനില മാറ്റിയ്ക്കാൻ ശ്രമിക്കുക, 0, 0.5, 1 എന്നിവ ആക്കി സജ്ജീകരിക്കുക. മറക്കരുത് 0 ഏറ്റവും കുറവ് വ്യത്യാസമുള്ളതും 1 ഏറ്റവും വ്യത്യാസമുള്ളതുമാണ്. നിങ്ങളുടെ ആപ്പിനായി ഏത് മൂല്യം ഏറ്റവും നല്ലതാണ്?

## മികച്ച ജോലി! നിങ്ങളുടെ പഠനം തുടരുക

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, ഞങ്ങളുടെ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ Generative AI അറിവ് ഉയർത്തി തുടർച്ചയായി പഠിക്കുക!

പാഠം 7-ലേക്ക് പോയി അവിടെ [ചാറ്റ് ആപ്ലിക്കേഷനുകൾ എങ്ങനെ നിർമ്മിക്കാമെന്ന്](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) കാണാം!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->