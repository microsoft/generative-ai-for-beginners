<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:56:00+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tl"
}
-->
# I-setup ang Iyong Dev Environment

I-setup namin ang repository at kurso na ito gamit ang isang [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) na may Universal runtime na sumusuporta sa Python3, .NET, Node.js at Java development. Ang kaugnay na configuration ay nakasaad sa `devcontainer.json` file na matatagpuan sa `.devcontainer/` folder sa ugat ng repository na ito.

Upang i-activate ang dev container, ilunsad ito sa [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para sa cloud-hosted runtime) o sa [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para sa local device-hosted runtime). Basahin ang [dokumentasyong ito](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para sa karagdagang detalye kung paano gumagana ang dev containers sa loob ng VS Code.  

> [!TIP]  
> Inirerekumenda namin ang paggamit ng GitHub Codespaces para sa mabilis na pagsisimula na may kaunting pagsisikap. Nagbibigay ito ng malawak na [libreng paggamit na quota](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para sa personal na account. I-configure ang [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) upang ihinto o tanggalin ang mga hindi aktibong codespaces upang mapakinabangan ang paggamit ng iyong quota.


## 1. Pagpapatakbo ng Mga Asignatura

Bawat aralin ay magkakaroon ng _opsyonal_ na mga asignatura na maaaring ibigay sa isa o higit pang mga programming languages kabilang ang: Python, .NET/C#, Java at JavaScript/TypeScript. Ang seksyong ito ay nagbibigay ng pangkalahatang gabay kaugnay sa pagpapatakbo ng mga asignaturang iyon.

### 1.1 Mga Asignatura sa Python

Ang mga asignatura sa Python ay ibinibigay alinman bilang mga aplikasyon (`.py` files) o Jupyter notebooks (`.ipynb` files). 
- Upang patakbuhin ang notebook, buksan ito sa Visual Studio Code pagkatapos ay i-click ang _Select Kernel_ (sa itaas na kanan) at piliin ang default na Python 3 na opsyon na ipinapakita. Maaari mo nang i-_Run All_ upang patakbuhin ang notebook.
- Upang patakbuhin ang mga aplikasyon ng Python mula sa command-line, sundin ang mga partikular na tagubilin sa asignatura upang matiyak na pinili mo ang tamang mga file at magbigay ng kinakailangang mga argumento.

## 2. Pag-configure ng Mga Provider

Ang mga asignatura **maaaring** i-setup upang gumana laban sa isa o higit pang Large Language Model (LLM) deployments sa pamamagitan ng isang suportadong service provider tulad ng OpenAI, Azure o Hugging Face. Ang mga ito ay nagbibigay ng isang _hosted endpoint_ (API) na maaari nating ma-access programmatically gamit ang tamang mga kredensyal (API key o token). Sa kursong ito, tinatalakay namin ang mga provider na ito:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang mga modelo kabilang ang pangunahing serye ng GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para sa mga OpenAI models na nakatuon sa enterprise readiness
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa open-source models at inference server

**Kailangan mong gamitin ang iyong sariling mga account para sa mga ehersisyong ito**. Ang mga asignatura ay opsyonal kaya maaari mong piliin na i-setup ang isa, lahat - o wala - sa mga provider batay sa iyong interes. Ilang gabay para sa signup:

| Signup | Gastos | API Key | Playground | Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Presyo](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Batay sa Proyekto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Magagamit na Modelo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Presyo](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Nang Maaga Para sa Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Presyo](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Limitadong mga modelo ang Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sundin ang mga direksyon sa ibaba upang _i-configure_ ang repository na ito para sa paggamit sa iba't ibang mga provider. Ang mga asignaturang nangangailangan ng partikular na provider ay maglalaman ng isa sa mga tag na ito sa kanilang filename:
 - `aoai` - nangangailangan ng Azure OpenAI endpoint, key
 - `oai` - nangangailangan ng OpenAI endpoint, key
 - `hf` - nangangailangan ng Hugging Face token

Maaari mong i-configure ang isa, wala, o lahat ng provider. Ang kaugnay na mga asignatura ay mag-e-error lang sa nawawalang mga kredensyal.

###  2.1. Lumikha ng `.env` file

Ina-assume namin na nabasa mo na ang gabay sa itaas at nag-sign up sa kaugnay na provider, at nakuha ang kinakailangang authentication credentials (API_KEY o token). Sa kaso ng Azure OpenAI, ina-assume namin na mayroon ka ring valid deployment ng isang Azure OpenAI Service (endpoint) na may hindi bababa sa isang GPT model na naka-deploy para sa chat completion.

Ang susunod na hakbang ay i-configure ang iyong **local environment variables** gaya ng sumusunod:


1. Hanapin sa root folder ang isang `.env.copy` file na dapat may mga nilalaman na ganito:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopyahin ang file na iyon sa `.env` gamit ang command sa ibaba. Ang file na ito ay _gitignore-d_, pinapanatiling ligtas ang mga lihim.

   ```bash
   cp .env.copy .env
   ```

3. Punan ang mga halaga (palitan ang mga placeholder sa kanan ng `=`) gaya ng inilarawan sa susunod na seksyon.

3. (Opsyon) Kung gumagamit ka ng GitHub Codespaces, mayroon kang opsyon na i-save ang environment variables bilang _Codespaces secrets_ na nauugnay sa repository na ito. Sa kasong iyon, hindi mo na kailangang mag-setup ng lokal na .env file. **Gayunpaman, tandaan na gumagana lamang ang opsyong ito kung gumagamit ka ng GitHub Codespaces.** Kakailanganin mo pa ring i-setup ang .env file kung gumagamit ka ng Docker Desktop.

### 2.2. I-populate ang `.env` file

Tingnan natin ang mga pangalan ng variable upang maunawaan kung ano ang kanilang kinakatawan:

| Variable  | Deskripsyon  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na iyong i-setup sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para sa paggamit ng serbisyo para sa non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para sa paggamit ng serbisyong iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang na-deploy na endpoint para sa isang Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ model deployment endpoint |
| | |

Tandaan: Ang huling dalawang Azure OpenAI variables ay sumasalamin sa default na model para sa chat completion (text generation) at vector search (embeddings) ayon sa pagkakabanggit. Ang mga tagubilin para sa pag-set up ng mga ito ay ilalarawan sa mga kaugnay na asignatura.


### 2.3 I-configure ang Azure: Mula sa Portal

Ang Azure OpenAI endpoint at key values ay matatagpuan sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kaya magsimula tayo doon.

1. Pumunta sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. I-click ang opsyon na **Keys and Endpoint** sa sidebar (menu sa kaliwa).
1. I-click ang **Show Keys** - makikita mo ang mga sumusunod: KEY 1, KEY 2 at Endpoint.
1. Gamitin ang KEY 1 value para sa AZURE_OPENAI_API_KEY
1. Gamitin ang Endpoint value para sa AZURE_OPENAI_ENDPOINT

Susunod, kailangan natin ang mga endpoints para sa partikular na mga model na na-deploy natin.

1. I-click ang opsyon na **Model deployments** sa sidebar (kaliwang menu) para sa Azure OpenAI resource.
1. Sa destination page, i-click ang **Manage Deployments**

Dadalin ka nito sa Azure OpenAI Studio website, kung saan natin makikita ang iba pang mga halaga gaya ng inilarawan sa ibaba.

### 2.4 I-configure ang Azure: Mula sa Studio

1. Mag-navigate sa [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** gaya ng inilarawan sa itaas.
1. I-click ang **Deployments** tab (sidebar, kaliwa) upang makita ang kasalukuyang na-deploy na mga model.
1. Kung ang iyong nais na model ay hindi pa na-deploy, gamitin ang **Create new deployment** upang i-deploy ito.
1. Kailangan mo ng _text-generation_ model - inirerekumenda namin: **gpt-35-turbo**
1. Kailangan mo ng _text-embedding_ model - inirerekumenda namin **text-embedding-ada-002**

Ngayon ay i-update ang environment variables upang ipakita ang _Deployment name_ na ginamit. Ito ay karaniwang magiging pareho sa pangalan ng model maliban kung binago mo ito nang tahasan. Kaya, bilang halimbawa, maaaring mayroon kang:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Huwag kalimutang i-save ang .env file kapag tapos na**. Maaari mo na ngayong isara ang file at bumalik sa mga tagubilin para sa pagpapatakbo ng notebook.

### 2.5 I-configure ang OpenAI: Mula sa Profile

Ang iyong OpenAI API key ay matatagpuan sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pang isa, maaari kang mag-sign up para sa isang account at lumikha ng isang API key. Kapag mayroon ka na ng key, maaari mo itong gamitin upang punan ang `OPENAI_API_KEY` variable sa `.env` file.

### 2.6 I-configure ang Hugging Face: Mula sa Profile

Ang iyong Hugging Face token ay matatagpuan sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag i-post o ibahagi ang mga ito sa publiko. Sa halip, lumikha ng bagong token para sa paggamit ng proyektong ito at kopyahin iyon sa `.env` file sa ilalim ng `HUGGING_FACE_API_KEY` variable. _Tandaan:_ Hindi ito teknikal na API key ngunit ginagamit para sa authentication kaya pinapanatili namin ang naming convention na iyon para sa consistency.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't pinagsisikapan naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa sariling wika nito ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.