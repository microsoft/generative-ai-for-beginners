<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:25:42+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tl"
}
-->
# I-setup ang Iyong Dev Environment

Inisetup namin ang repositoryong ito at kurso gamit ang isang [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) na may Universal runtime na maaaring sumuporta sa Python3, .NET, Node.js at Java development. Ang kaugnay na configuration ay nakadefine sa file na `devcontainer.json` na matatagpuan sa folder na `.devcontainer/` sa ugat ng repositoryong ito.

Upang i-activate ang dev container, ilunsad ito sa [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para sa cloud-hosted runtime) o sa [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para sa local device-hosted runtime). Basahin ang [dokumentasyong ito](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para sa karagdagang detalye kung paano gumagana ang dev containers sa loob ng VS Code.  

> [!TIP]  
> Inirerekomenda namin ang paggamit ng GitHub Codespaces para sa mabilis na pagsisimula na may kaunting pagsisikap. Nagbibigay ito ng mapagbigay na [libre na paggamit ng quota](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para sa personal na mga account. I-configure ang [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) upang ihinto o tanggalin ang mga hindi aktibong codespaces upang mapakinabangan ang iyong quota na paggamit.

## 1. Pagpapatupad ng mga Takdang-Aralin

Ang bawat aralin ay magkakaroon ng _opsyonal_ na mga takdang-aralin na maaaring ibigay sa isa o higit pang mga programming languages kabilang ang: Python, .NET/C#, Java at JavaScript/TypeScript. Ang seksyong ito ay nagbibigay ng pangkalahatang gabay na may kaugnayan sa pagpapatupad ng mga takdang-aralin na iyon.

### 1.1 Mga Takdang-Aralin sa Python

Ang mga takdang-aralin sa Python ay ibinibigay alinman bilang mga aplikasyon (`.py` files) o Jupyter notebooks (`.ipynb` files). 
- Upang patakbuhin ang notebook, buksan ito sa Visual Studio Code pagkatapos ay i-click ang _Select Kernel_ (sa itaas na kanan) at piliin ang default na opsyon na Python 3 na ipinapakita. Maaari mo nang i-_Run All_ upang patakbuhin ang notebook.
- Upang patakbuhin ang mga aplikasyon ng Python mula sa command-line, sundin ang mga tagubilin na partikular sa takdang-aralin upang matiyak na pipiliin mo ang tamang mga file at ibigay ang mga kinakailangang argumento.

## 2. Pag-configure ng mga Provider

Ang mga takdang-aralin **maaaring** isetup upang gumana laban sa isa o higit pang mga Large Language Model (LLM) deployments sa pamamagitan ng isang suportadong service provider tulad ng OpenAI, Azure o Hugging Face. Ang mga ito ay nagbibigay ng isang _hosted endpoint_ (API) na maaari naming ma-access programmatically gamit ang tamang credentials (API key o token). Sa kursong ito, tinatalakay namin ang mga provider na ito:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang mga modelo kabilang ang core na serye ng GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para sa mga modelo ng OpenAI na may pokus sa kahandaan ng enterprise.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa mga open-source na modelo at inference server.

**Kailangan mong gumamit ng sarili mong mga account para sa mga pagsasanay na ito**. Ang mga takdang-aralin ay opsyonal kaya maaari mong piliing isetup ang isa, lahat - o wala - ng mga provider batay sa iyong interes. Ilang gabay para sa signup:

| Signup | Gastos | API Key | Playground | Mga Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pagpepresyo](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Modelong Magagamit |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pagpepresyo](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Muna Para sa Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pagpepresyo](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Limitado ang mga modelo ng Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sundin ang mga direksyon sa ibaba upang _i-configure_ ang repositoryong ito para magamit sa iba't ibang provider. Ang mga takdang-aralin na nangangailangan ng isang tiyak na provider ay maglalaman ng isa sa mga tag na ito sa kanilang filename:
 - `aoai` - nangangailangan ng Azure OpenAI endpoint, key
 - `oai` - nangangailangan ng OpenAI endpoint, key
 - `hf` - nangangailangan ng Hugging Face token

Maaari mong i-configure ang isa, wala, o lahat ng provider. Ang mga kaugnay na takdang-aralin ay simpleng mag-e-error kung kulang ang mga kredensyal.

### 2.1. Gumawa ng `.env` file

Inaakala naming nabasa mo na ang gabay sa itaas at nag-sign up sa kaugnay na provider, at nakuha ang kinakailangang mga kredensyal sa pagpapatunay (API_KEY o token). Sa kaso ng Azure OpenAI, inaakala naming mayroon ka ring wastong deployment ng isang Azure OpenAI Service (endpoint) na may hindi bababa sa isang GPT model na na-deploy para sa chat completion.

Ang susunod na hakbang ay i-configure ang iyong **mga lokal na environment variables** gaya ng sumusunod:

1. Tumingin sa root folder para sa isang `.env.copy` file na dapat may mga nilalaman na ganito:

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

3. Punan ang mga halaga (palitan ang mga placeholder sa kanang bahagi ng `=`) ayon sa inilarawan sa susunod na seksyon.

3. (Opsyon) Kung gumagamit ka ng GitHub Codespaces, mayroon kang opsyon na i-save ang mga environment variable bilang _Codespaces secrets_ na nauugnay sa repositoryong ito. Sa kasong iyon, hindi mo na kailangang mag-setup ng lokal na .env file. **Gayunpaman, tandaan na ang opsyong ito ay gumagana lamang kung gumagamit ka ng GitHub Codespaces.** Kakailanganin mo pa ring i-setup ang .env file kung gumagamit ka ng Docker Desktop sa halip.

### 2.2. Punan ang `.env` file

Tingnan natin nang mabilis ang mga pangalan ng variable upang maunawaan kung ano ang kanilang kinakatawan:

| Variable  | Paglalarawan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na na-setup mo sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para sa paggamit ng serbisyo para sa mga non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para sa paggamit ng serbisyong iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang na-deploy na endpoint para sa isang Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ model deployment endpoint |
| | |

Tandaan: Ang huling dalawang Azure OpenAI variable ay nagpapakita ng default na model para sa chat completion (text generation) at vector search (embeddings) ayon sa pagkakabanggit. Ang mga tagubilin para sa kanilang pag-set ay ipapaliwanag sa mga kaugnay na takdang-aralin.

### 2.3 I-configure ang Azure: Mula sa Portal

Ang mga halaga ng Azure OpenAI endpoint at key ay matatagpuan sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kaya't magsimula tayo doon.

1. Pumunta sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. I-click ang opsyon na **Keys and Endpoint** sa sidebar (menu sa kaliwa).
1. I-click ang **Show Keys** - dapat mong makita ang sumusunod: KEY 1, KEY 2 at Endpoint.
1. Gamitin ang KEY 1 na halaga para sa AZURE_OPENAI_API_KEY
1. Gamitin ang Endpoint na halaga para sa AZURE_OPENAI_ENDPOINT

Susunod, kailangan natin ang mga endpoints para sa mga partikular na model na na-deploy natin.

1. I-click ang opsyon na **Model deployments** sa sidebar (left menu) para sa Azure OpenAI resource.
1. Sa destination page, i-click ang **Manage Deployments**

Ito ay magdadala sa iyo sa Azure OpenAI Studio website, kung saan makikita natin ang iba pang mga halaga gaya ng inilarawan sa ibaba.

### 2.4 I-configure ang Azure: Mula sa Studio

1. Mag-navigate sa [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** gaya ng inilarawan sa itaas.
1. I-click ang tab na **Deployments** (sidebar, kaliwa) upang makita ang kasalukuyang mga na-deploy na modelo.
1. Kung ang iyong nais na modelo ay hindi pa na-deploy, gamitin ang **Create new deployment** upang i-deploy ito.
1. Kakailanganin mo ng isang _text-generation_ na modelo - inirerekomenda namin: **gpt-35-turbo**
1. Kakailanganin mo ng isang _text-embedding_ na modelo - inirerekomenda namin **text-embedding-ada-002**

Ngayon i-update ang mga environment variable upang ipakita ang _Deployment name_ na ginamit. Ito ay karaniwang magiging pareho sa pangalan ng modelo maliban kung binago mo ito nang tahasan. Kaya, bilang isang halimbawa, maaaring mayroon ka:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Huwag kalimutang i-save ang .env file kapag tapos na**. Maaari mo nang isara ang file at bumalik sa mga tagubilin para sa pagpapatakbo ng notebook.

### 2.5 I-configure ang OpenAI: Mula sa Profile

Ang iyong OpenAI API key ay makikita sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pa nito, maaari kang mag-sign up para sa isang account at lumikha ng isang API key. Kapag mayroon ka na ng key, maaari mo itong gamitin upang punan ang `OPENAI_API_KEY` variable sa `.env` file.

### 2.6 I-configure ang Hugging Face: Mula sa Profile

Ang iyong Hugging Face token ay makikita sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag itong ipost o ibahagi sa publiko. Sa halip, lumikha ng bagong token para sa paggamit ng proyektong ito at kopyahin iyon sa `.env` file sa ilalim ng `HUGGING_FACE_API_KEY` variable. _Tandaan:_ Ito ay teknikal na hindi isang API key ngunit ginagamit para sa pagpapatunay kaya't pinapanatili namin ang naming convention na iyon para sa pagkakapare-pareho.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpakan. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.