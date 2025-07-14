<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:34:35+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tl"
}
-->
# I-setup ang Iyong Dev Environment

Inilagay namin ang repository at kurso na ito gamit ang [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) na may Universal runtime na sumusuporta sa Python3, .NET, Node.js, at Java development. Ang kaugnay na configuration ay nakasaad sa `devcontainer.json` file na matatagpuan sa `.devcontainer/` folder sa root ng repository na ito.

Para i-activate ang dev container, buksan ito sa [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para sa cloud-hosted runtime) o sa [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para sa local device-hosted runtime). Basahin ang [dokumentasyong ito](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para sa karagdagang detalye kung paano gumagana ang dev containers sa loob ng VS Code.

> [!TIP]  
> Inirerekomenda naming gamitin ang GitHub Codespaces para sa mabilisang pagsisimula na may kaunting pagsisikap. Nagbibigay ito ng maluwag na [libreng quota ng paggamit](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para sa mga personal na account. I-configure ang [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para itigil o tanggalin ang mga inactive na codespaces upang masulit ang iyong quota.

## 1. Pagsasagawa ng mga Takdang-Aralin

Bawat aralin ay magkakaroon ng _opsyonal_ na mga takdang-aralin na maaaring ibigay sa isa o higit pang mga programming language kabilang ang: Python, .NET/C#, Java, at JavaScript/TypeScript. Ang seksyong ito ay nagbibigay ng pangkalahatang gabay tungkol sa pagsasagawa ng mga takdang-aralin na iyon.

### 1.1 Mga Takdang-Aralin sa Python

Ang mga takdang-aralin sa Python ay ibinibigay bilang mga aplikasyon (`.py` files) o Jupyter notebooks (`.ipynb` files).  
- Para patakbuhin ang notebook, buksan ito sa Visual Studio Code, pagkatapos ay i-click ang _Select Kernel_ (sa itaas na kanan) at piliin ang default na Python 3 na opsyon na ipinapakita. Maaari mo nang i-_Run All_ para isagawa ang notebook.  
- Para patakbuhin ang mga Python application mula sa command-line, sundin ang mga partikular na tagubilin ng takdang-aralin upang matiyak na napili mo ang tamang mga file at naibigay ang kinakailangang mga argumento.

## 2. Pag-configure ng mga Provider

Ang mga takdang-aralin **ay maaaring** i-setup upang gumana laban sa isa o higit pang Large Language Model (LLM) deployments sa pamamagitan ng suportadong service provider tulad ng OpenAI, Azure, o Hugging Face. Nagbibigay ang mga ito ng _hosted endpoint_ (API) na maaari nating ma-access programmatically gamit ang tamang kredensyal (API key o token). Sa kursong ito, tatalakayin natin ang mga provider na ito:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang modelo kabilang ang core GPT series.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para sa OpenAI models na may pokus sa enterprise readiness  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa open-source models at inference server

**Kailangan mong gamitin ang sarili mong mga account para sa mga pagsasanay na ito**. Opsyonal ang mga takdang-aralin kaya maaari kang pumili na i-setup ang isa, lahat, o wala sa mga provider depende sa iyong interes. Narito ang ilang gabay para sa pag-signup:

| Signup | Gastos | API Key | Playground | Mga Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Presyo](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Modelo ang Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Presyo](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Nang Maaga Para sa Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Presyo](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Limitado ang mga Modelo sa Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sundin ang mga tagubilin sa ibaba para _i-configure_ ang repository na ito para magamit sa iba't ibang provider. Ang mga takdang-aralin na nangangailangan ng partikular na provider ay magkakaroon ng isa sa mga tag na ito sa kanilang filename:  
 - `aoai` - nangangailangan ng Azure OpenAI endpoint, key  
 - `oai` - nangangailangan ng OpenAI endpoint, key  
 - `hf` - nangangailangan ng Hugging Face token

Maaari kang mag-configure ng isa, wala, o lahat ng mga provider. Ang mga kaugnay na takdang-aralin ay magbibigay lang ng error kapag kulang ang kredensyal.

###  2.1. Gumawa ng `.env` file

Ipinagpapalagay namin na nabasa mo na ang gabay sa itaas at nakapag-signup ka na sa kaukulang provider, at nakuha mo na ang kinakailangang authentication credentials (API_KEY o token). Sa kaso ng Azure OpenAI, ipinagpapalagay din namin na mayroon kang valid na deployment ng Azure OpenAI Service (endpoint) na may hindi bababa sa isang GPT model na naka-deploy para sa chat completion.

Ang susunod na hakbang ay i-configure ang iyong **local environment variables** tulad ng sumusunod:

1. Hanapin sa root folder ang `.env.copy` file na dapat ay may nilalaman na ganito:

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

2. Kopyahin ang file na iyon bilang `.env` gamit ang command sa ibaba. Ang file na ito ay _gitignore-d_, kaya ligtas ang mga sikreto.

   ```bash
   cp .env.copy .env
   ```

3. Punan ang mga halaga (palitan ang mga placeholder sa kanan ng `=`) ayon sa paglalarawan sa susunod na seksyon.

3. (Opsyonal) Kung gumagamit ka ng GitHub Codespaces, may opsyon kang i-save ang environment variables bilang _Codespaces secrets_ na naka-link sa repository na ito. Sa ganitong kaso, hindi mo na kailangang gumawa ng lokal na .env file. **Ngunit tandaan na gumagana lang ang opsyong ito kung gumagamit ka ng GitHub Codespaces.** Kailangan mo pa ring i-setup ang .env file kung gagamit ka ng Docker Desktop.

### 2.2. Punan ang `.env` file

Tingnan natin nang mabilis ang mga pangalan ng variable para maintindihan kung ano ang kinakatawan nila:

| Variable  | Paglalarawan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na na-setup mo sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyo para sa non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyong iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang deployed endpoint para sa isang Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ model deployment endpoint |
| | |

Tandaan: Ang huling dalawang Azure OpenAI variables ay tumutukoy sa default na modelo para sa chat completion (text generation) at vector search (embeddings) ayon sa pagkakasunod. Ang mga tagubilin para sa pag-set ng mga ito ay ibibigay sa mga kaugnay na takdang-aralin.

### 2.3 I-configure ang Azure: Mula sa Portal

Makikita ang Azure OpenAI endpoint at key values sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kaya magsimula tayo doon.

1. Pumunta sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. I-click ang **Keys and Endpoint** na opsyon sa sidebar (menu sa kaliwa).  
1. I-click ang **Show Keys** - makikita mo ang mga sumusunod: KEY 1, KEY 2 at Endpoint.  
1. Gamitin ang KEY 1 value para sa AZURE_OPENAI_API_KEY  
1. Gamitin ang Endpoint value para sa AZURE_OPENAI_ENDPOINT

Susunod, kailangan natin ang mga endpoint para sa mga partikular na modelong na-deploy natin.

1. I-click ang **Model deployments** na opsyon sa sidebar (menu sa kaliwa) para sa Azure OpenAI resource.  
1. Sa destination page, i-click ang **Manage Deployments**

Dadala ka nito sa Azure OpenAI Studio website, kung saan makikita natin ang iba pang mga halaga tulad ng inilalarawan sa ibaba.

### 2.4 I-configure ang Azure: Mula sa Studio

1. Pumunta sa [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** tulad ng nabanggit sa itaas.  
1. I-click ang **Deployments** tab (sidebar, kaliwa) para makita ang mga kasalukuyang na-deploy na modelo.  
1. Kung ang nais mong modelo ay hindi pa na-deploy, gamitin ang **Create new deployment** para i-deploy ito.  
1. Kailangan mo ng _text-generation_ model - inirerekomenda namin ang: **gpt-35-turbo**  
1. Kailangan mo ng _text-embedding_ model - inirerekomenda namin ang **text-embedding-ada-002**

Ngayon i-update ang environment variables upang ipakita ang _Deployment name_ na ginamit. Karaniwan itong kapareho ng pangalan ng modelo maliban kung pinalitan mo ito nang tahasan. Halimbawa, maaari kang magkaroon ng:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Huwag kalimutang i-save ang .env file kapag tapos na**. Maaari mo nang isara ang file at bumalik sa mga tagubilin para patakbuhin ang notebook.

### 2.5 I-configure ang OpenAI: Mula sa Profile

Makikita ang iyong OpenAI API key sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pang account, maaari kang mag-signup at gumawa ng API key. Kapag nakuha mo na ang key, maaari mo itong gamitin para punan ang `OPENAI_API_KEY` variable sa `.env` file.

### 2.6 I-configure ang Hugging Face: Mula sa Profile

Makikita ang iyong Hugging Face token sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag itong i-post o ibahagi nang publiko. Sa halip, gumawa ng bagong token para sa paggamit ng proyektong ito at kopyahin ito sa `.env` file sa ilalim ng `HUGGING_FACE_API_KEY` variable. _Tandaan:_ Hindi ito teknikal na API key ngunit ginagamit para sa authentication kaya pinananatili namin ang ganitong pangalan para sa pagkakapare-pareho.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.