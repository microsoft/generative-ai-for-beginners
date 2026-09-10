# Pagpili at Pag-configure ng Tagapagbigay ng LLM 🔑

Ang mga takdang-aralin **ay maaaring** i-setup upang gumana laban sa isa o higit pang Large Language Model (LLM) deployments sa pamamagitan ng isang suportadong tagapagbigay ng serbisyo tulad ng OpenAI, Azure o Hugging Face. Nagbibigay ang mga ito ng isang _hosted endpoint_ (API) na maaari nating ma-access programmatically gamit ang tamang credentials (API key o token). Sa kursong ito, tinalakay natin ang mga tagapagbigay na ito:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang modelo kabilang ang core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) para sa mga OpenAI modelong naka-focus sa kahandaan ng enterprise
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para sa isang endpoint at API key upang ma-access ang daan-daang modelo mula sa OpenAI, Meta, Mistral, Cohere, Microsoft at iba pa (pinalitan ang GitHub Models, na magreretiro sa katapusan ng Hulyo 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa open-source models at inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) o [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) kung mas gusto mong patakbuhin ang mga modelo nang ganap na offline sa iyong sariling device, nang walang kinakailangang cloud subscription

**Kailangang gamitin mo ang iyong sariling mga account para sa mga pagsasanay na ito**. Ang mga takdang-aralin ay opsyonal kaya maaari kang pumili na i-setup ang isa, lahat, o wala sa mga tagapagbigay depende sa iyong interes. Narito ang ilang gabay para sa pag-signup:

| Signup | Gastos | API Key | Playground | Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pagpepresyo](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Batay sa Proyekto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Magagamit na Modelo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pagpepresyo](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Nang Maaga Para sa Access](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Pagpepresyo](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Pahina ng Pangkalahatang-ideya ng Proyekto](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | May libreng tier; isang endpoint + key para sa maraming tagapagbigay ng modelo |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pagpepresyo](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Limitado ang mga Modelo sa Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Libre (patakbuhin sa iyong device) | Hindi kailangan | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Ganap na offline, OpenAI-compatible endpoint |
| | | | | |

Sundin ang mga tagubilin sa ibaba upang _i-configure_ ang repositoryong ito para magamit sa iba't ibang mga tagapagbigay. Ang mga takdang-aralin na nangangailangan ng isang tiyak na tagapagbigay ay magkakaroon ng isa sa mga tag na ito sa pangalan ng file:

- `aoai` - nangangailangan ng Azure OpenAI endpoint, key
- `oai` - nangangailangan ng OpenAI endpoint, key
- `hf` - nangangailangan ng Hugging Face token
- `githubmodels` - nangangailangan ng Microsoft Foundry Models endpoint, key (Magreretiro ang GitHub Models sa katapusan ng Hulyo 2026)

Maaari kang mag-configure ng isa, wala, o lahat ng mga tagapagbigay. Ang mga kaugnay na takdang-aralin ay magbibigay lamang ng error kapag wala ang credentials.

## Gumawa ng `.env` na file

Inaakala namin na nabasa mo na ang gabay sa itaas at nakapag-signup ka na sa kaukulang tagapagbigay, at nakuha ang kinakailangang authentication credentials (API_KEY o token). Sa kaso ng Azure OpenAI, inaasahan din namin na mayroon kang valid deployment ng Azure OpenAI Service (endpoint) na may hindi bababa sa isang GPT model na na-deploy para sa chat completion.

Ang susunod na hakbang ay i-configure ang iyong **local environment variables** gaya ng sumusunod:

1. Hanapin ang `.env.copy` na file sa root folder na dapat ay may mga nilalaman na ganito:

   ```bash
   # Tagapagbigay ng OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI sa Microsoft Foundry
   ## (Azure OpenAI Service ay bahagi na ng Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default ay naka-set! (kasalukuyang stable GA API na bersyon)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Models (multi-provider model catalog, pumapalit sa GitHub Models, na magre-retire sa katapusan ng Hulyo 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopyahin ang file na iyon sa `.env` gamit ang utos sa ibaba. Ang file na ito ay _gitignore-d_, kaya ligtas ang mga lihim.

   ```bash
   cp .env.copy .env
   ```

3. Punan ang mga halaga (palitan ang mga placeholder sa kanang bahagi ng `=`) tulad ng inilalarawan sa susunod na seksyon.

4. (Opsyonal) Kung gumagamit ka ng GitHub Codespaces, mayroon kang opsyon na i-save ang mga environment variables bilang _Codespaces secrets_ na kaugnay sa repositoryong ito. Sa kasong iyon, hindi mo na kailangang mag-setup ng lokal na .env file. **Gayunpaman, tandaan na gumagana lamang ang opsyon na ito kung gumagamit ka ng GitHub Codespaces.** Kailangan mo pa ring i-setup ang .env file kung gumagamit ka ng Docker Desktop.

## Punan ang `.env` na file

Tingnan natin nang mabilis ang mga pangalan ng variable para maunawaan kung ano ang kanilang kinakatawan:

| Variable  | Paglalarawan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na na-setup mo sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyo para sa mga hindi Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyong iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang deployed endpoint para sa isang Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ model deployment endpoint |
| AZURE_INFERENCE_ENDPOINT | Ito ang endpoint para sa iyong Microsoft Foundry project, ginagamit para sa Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ito ang API key para sa iyong Microsoft Foundry project |
| | |

Tala: Ang huling dalawang Azure OpenAI variables ay sumasalamin sa default na modelo para sa chat completion (text generation) at vector search (embeddings) ayon sa pagkakasunod. Ang mga tagubilin para sa pagsesetup ng mga ito ay ilalathala sa mga kaugnay na takdang-aralin.

## I-configure ang Azure OpenAI: Mula sa Portal

> **Tala:** Ang Azure OpenAI Service ay bahagi na ngayon ng [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ang mga resource at deployment ay makikita pa rin sa Azure Portal, ngunit ang araw-araw na pamamahala ng modelo (deployments, playground, monitoring) ay ginagawa na ngayon sa Foundry portal sa halip na sa dating standalone na "Azure OpenAI Studio".

Matatagpuan ang Azure OpenAI endpoint at key values sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kaya simulan natin doon.

1. Pumunta sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. I-click ang opsyon na **Keys and Endpoint** sa sidebar (menu sa kaliwa).
1. I-click ang **Show Keys** - makikita mo ang sumusunod: KEY 1, KEY 2 at Endpoint.
1. Gamitin ang halaga ng KEY 1 para sa AZURE_OPENAI_API_KEY
1. Gamitin ang halaga ng Endpoint para sa AZURE_OPENAI_ENDPOINT

Sunod, kailangan natin ang mga endpoint para sa mga partikular na modelong na-deploy natin.

1. I-click ang opsyon na **Model deployments** sa sidebar (menu sa kaliwa) para sa Azure OpenAI resource.
1. Sa destination page, i-click ang **Go to Microsoft Foundry portal** (o **Manage Deployments**, depende sa uri ng iyong resource)

Dadalhin ka nito sa Microsoft Foundry portal, kung saan hahanapin natin ang iba pang mga halaga ayon sa nakasaad sa ibaba.

## I-configure ang Azure OpenAI: Mula sa Microsoft Foundry portal

1. Pumunta sa [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** gaya ng nakasaad sa itaas.
1. I-click ang tab na **Deployments** (sidebar, kaliwa) upang makita ang mga kasalukuyang deployed na modelo.
1. Kung ang nais mong modelo ay hindi pa na-deploy, gamitin ang **Deploy model** upang i-deploy ito mula sa [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Kailangan mo ng _text-generation_ na modelo - inirerekomenda namin ang: **gpt-5-mini**
1. Kailangan mo ng _text-embedding_ na modelo - inirerekomenda ang **text-embedding-3-small**

Ngayon ay i-update ang environment variables upang ipakita ang _Deployment name_ na ginagamit. Ito ay karaniwang katulad ng pangalan ng modelo maliban kung binago mo ito nang tahasan. Halimbawa, maaari mong magkaroon ng:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Huwag kalimutang i-save ang .env file kapag tapos na**. Maaari mo nang isara ang file at bumalik sa mga tagubilin para patakbuhin ang notebook.

## I-configure ang OpenAI: Mula sa Profile

Ang iyong OpenAI API key ay makikita sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pang isa, maaari kang mag-signup para sa account at gumawa ng API key. Kapag mayroon ka nang susi, maaari mo itong gamitin upang punan ang `OPENAI_API_KEY` variable sa `.env` file.

## I-configure ang Hugging Face: Mula sa Profile

Ang iyong Hugging Face token ay makikita sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag itong i-post o ibahagi nang publiko. Sa halip, gumawa ng bagong token para sa paggamit ng proyektong ito at kopyahin ito sa `.env` file sa ilalim ng `HUGGING_FACE_API_KEY` variable. _Tandaan:_ Hindi ito teknikal na API key pero ginagamit ito para sa authentication kaya ipinananatili namin ang ganitong pangalan para sa pagkakapareho.

## I-configure ang Microsoft Foundry Models: Mula sa Portal

> **Tala:** Magreretiro ang GitHub Models sa katapusan ng Hulyo 2026. Ang Microsoft Foundry Models ang direktang kapalit, na nag-aalok ng parehong libreng subok na model catalog at karanasan sa Azure AI Inference SDK / OpenAI SDK.

1. Pumunta sa [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) at gumawa (o buksan) ng Foundry project.
1. Suriin ang [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) at i-deploy ang modelo, halimbawa ay `gpt-5-mini`.
1. Sa pahina ng **Overview** ng proyekto, kopyahin ang **endpoint** at **API key**.
1. Gamitin ang endpoint value para sa `AZURE_INFERENCE_ENDPOINT` at ang key value para sa `AZURE_INFERENCE_CREDENTIAL` sa iyong `.env` file.

## Offline / Local Providers

Kung ayaw mong gumamit ng cloud subscription, maaari mong patakbuhin ang katugmang open models nang direkta sa iyong sariling device:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ang on-device runtime ng Microsoft. Awtomatikong pinipili nito ang pinakamahusay na execution provider (NPU, GPU, o CPU) at ipinapakita ang isang OpenAI-compatible endpoint, kaya maaari mong muling gamitin ang karamihan sa sample code sa kursong ito nang may kaunting pagbabago. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) upang makapagsimula, o i-install gamit ang `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - isang popular na alternatibo para patakbuhin ang mga open models tulad ng Llama, Phi, Mistral, at Gemma nang lokal.


Tingnan ang [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para sa mga praktikal na halimbawa gamit ang parehong mga pagpipilian.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->