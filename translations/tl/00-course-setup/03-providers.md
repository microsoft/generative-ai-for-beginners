# Pagpili at Pag-configure ng Tagapagbigay ng LLM 🔑

Maaaring i-setup din ang mga takdang-aralin para gumana laban sa isa o higit pang Malalaking Modelo ng Wika (Large Language Model o LLM) sa pamamagitan ng suportadong tagapagbigay ng serbisyo tulad ng OpenAI, Azure, o Hugging Face. Nagbibigay ang mga ito ng _hosted endpoint_ (API) na maaaring ma-access programmatically gamit ang tamang mga kredensyal (API key o token). Sa kurso na ito, tatalakayin natin ang mga tagapagbigay na ito:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang modelo kabilang ang pangunahing serye ng GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para sa mga modelo ng OpenAI na nakatuon sa kahandaan para sa enterprise
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para sa isang solong endpoint at API key upang ma-access ang daan-daang mga modelo mula sa OpenAI, Meta, Mistral, Cohere, Microsoft at iba pa (papalitan nito ang GitHub Models na magwawakas sa katapusan ng Hulyo 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa mga open-source na modelo at inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) o [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) kung nais mong patakbuhin ang mga modelo nang ganap offline sa iyong sariling device, nang walang kailangang cloud subscription

**Kailangan mong gamitin ang sarili mong mga account para sa mga pagsasanay na ito**. Opsyonal ang mga takdang-aralin kaya maaari kang pumili na i-setup ang isa, lahat, o wala sa mga tagapagbigay base sa iyong interes. Narito ang ilang gabay para sa pag-signup:

| Signup | Gastos | API Key | Playground | Mga Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Modelong Magagamit |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Nang Maaga Para sa Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Pricing](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project Overview page](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | May libreng tier; isang endpoint + key para sa maraming tagapagbigay ng modelo |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [May limitadong mga modelo ang Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Libre (tumakbo sa iyong device) | Hindi kailangan | [Local CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Ganap na offline, OpenAI-compatible endpoint |
| | | | | |

Sundin ang mga direksyon sa ibaba para _i-configure_ ang repository na ito upang magamit sa iba't ibang mga tagapagbigay. Ang mga takdang-aralin na nangangailangan ng partikular na tagapagbigay ay maglalaman ng isa sa mga tag na ito sa kanilang filename:

- `aoai` - nangangailangan ng Azure OpenAI endpoint, key
- `oai` - nangangailangan ng OpenAI endpoint, key
- `hf` - nangangailangan ng Hugging Face token
- `githubmodels` - nangangailangan ng Microsoft Foundry Models endpoint, key (Magwawakas ang GitHub Models sa katapusan ng Hulyo 2026)

Maaari kang mag-configure ng isa, wala, o lahat ng tagapagbigay. Magkakaroon ng error ang mga kaugnay na takdang-aralin kung wala ang mga kredensyal.

## Gumawa ng `.env` na file

Inaakalang nabasa mo na ang gabay sa itaas at nakapag-signup ka na sa kaukulang tagapagbigay, at nakuha mo na ang kinakailangang mga kredensyal sa pagpapatotoo (API_KEY o token). Sa kaso ng Azure OpenAI, inaasahan ding mayroon kang valid na deployment ng Azure OpenAI Service (endpoint) na may hindi bababa sa isang GPT model na naka-deploy para sa chat completion.

Ang susunod na hakbang ay para i-configure ang iyong **lokal na mga environment variable** tulad ng sumusunod:

1. Hanapin sa root folder ang `.env.copy` na file na may laman na katulad nito:

   ```bash
   # Tagapagbigay ng OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI sa Microsoft Foundry
   ## (Ang Azure OpenAI Service ay bahagi na ng Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default na nakaset! (kasalukuyang matatag na bersyon ng GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Mga Modelo ng Microsoft Foundry (multi-provider na katalogo ng modelo, pumapalit sa GitHub Models, na tatapusin sa katapusan ng Hulyo 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopyahin ang file na iyon sa `.env` gamit ang utos sa ibaba. Ang file na ito ay _ginitignore_, kaya ligtas ang mga lihim.

   ```bash
   cp .env.copy .env
   ```

3. Punan ang mga halaga (palitan ang mga placeholder sa kanang bahagi ng `=`) tulad ng inilalarawan sa susunod na seksyon.

4. (Opsyonal) Kung gumagamit ka ng GitHub Codespaces, may opsyon kang i-save ang environment variables bilang _Codespaces secrets_ na kaugnay ng repository na ito. Sa ganitong kaso, hindi mo na kailangang mag-setup ng lokal na .env file. **Gayunpaman, tandaan na ang opsyong ito ay gumagana lamang kung gumagamit ka ng GitHub Codespaces.** Kailangan mo pa ring i-setup ang .env file kung gumagamit ka ng Docker Desktop.

## Punan ang `.env` na file

Tingnan natin nang mabilis ang mga pangalan ng variable para maintindihan kung ano ang kanilang kinakatawan:

| Variable  | Paglalarawan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na na-setup mo sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyo para sa mga non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyong iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang deployed endpoint para sa isang Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ na modelo deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ na modelo deployment endpoint |
| AZURE_INFERENCE_ENDPOINT | Ito ang endpoint para sa iyong Microsoft Foundry project, na ginagamit para sa Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ito ang API key para sa iyong Microsoft Foundry project |
| | |

Tandaan: Ang huling dalawang Azure OpenAI variable ay nagpapakita ng default na modelo para sa chat completion (text generation) at vector search (embeddings) ayon sa pagkakabanggit. Ang mga tagubilin para sa pagsesetup ng mga ito ay ibibigay sa mga kaugnay na takdang-aralin.

## I-configure ang Azure OpenAI: Mula sa Portal

> **Tandaan:** Ang Azure OpenAI Service ay bahagi na ngayon ng [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ipinapakita pa rin ang mga resources at deployment sa Azure Portal, ngunit ang araw-araw na pamamahala ng modelo (deployments, playground, monitoring) ay ginagawa na ngayon sa Foundry portal sa halip na sa lumang standalone na "Azure OpenAI Studio".

Makikita ang Azure OpenAI endpoint at key values sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kaya magsimula tayo doon.

1. Pumunta sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. I-click ang **Keys and Endpoint** na opsyon sa sidebar (menu sa kaliwa).
1. I-click ang **Show Keys** - makikita mo dapat ang mga sumusunod: KEY 1, KEY 2 at Endpoint.
1. Gamitin ang halaga ng KEY 1 para sa AZURE_OPENAI_API_KEY
1. Gamitin ang halaga ng Endpoint para sa AZURE_OPENAI_ENDPOINT

Sunod, kailangan natin ang mga endpoint para sa mga partikular na modelong na-deploy natin.

1. I-click ang **Model deployments** na opsyon sa sidebar (menu sa kaliwa) para sa Azure OpenAI resource.
1. Sa destination page, i-click ang **Go to Microsoft Foundry portal** (o **Manage Deployments**, depende sa uri ng resource mo)

Dadalhin ka nito sa Microsoft Foundry portal, kung saan makikita natin ang mga iba pang halaga tulad ng inilalarawan sa ibaba.

## I-configure ang Azure OpenAI: Mula sa Microsoft Foundry portal

1. Pumunta sa [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** tulad ng inilarawan sa itaas.
1. I-click ang tab na **Deployments** (sidebar, kaliwa) upang makita ang mga kasalukuyang nadeploy na modelo.
1. Kung hindi nadeploy ang nais mong modelo, gamitin ang **Deploy model** upang ideploy ito mula sa [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Kakailanganin mo ng _text-generation_ na modelo - nirekomenda namin: **gpt-4o-mini**
1. Kakailanganin mo ng _text-embedding_ na modelo - nirekomenda namin ang **text-embedding-3-small**

Ngayon, i-update ang mga environment variable para ipakita ang _Deployment name_ na ginamit. Karaniwan itong kapareho ng pangalan ng modelo maliban kung pinalitan mo ito nang tahasan. Halimbawa, maaari kang magkaroon ng:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Huwag kalimutang i-save ang .env file kapag tapos na**. Maaari mo nang isara ang file at bumalik sa mga tagubilin para sa pagpapatakbo ng notebook.

## I-configure ang OpenAI: Mula sa Profile

Makikita ang iyong OpenAI API key sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pa nito, maaari kang mag-sign up para sa isang account at gumawa ng API key. Kapag nakuha mo na ang key, maaari mo itong gamitin para punan ang variable na `OPENAI_API_KEY` sa `.env` file.

## I-configure ang Hugging Face: Mula sa Profile

Makikita ang iyong Hugging Face token sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag itong i-post o i-share nang publiko. Sa halip, gumawa ng bagong token para sa paggamit ng proyektong ito at kopyahin iyon sa `.env` file sa ilalim ng variable na `HUGGING_FACE_API_KEY`. _Tandaan:_ Hindi ito teknikal na API key ngunit ginagamit para sa pagpapatotoo kaya pinapanatili namin ang ganitong pangalan para sa pagkakapare-pareho.

## I-configure ang Microsoft Foundry Models: Mula sa Portal

> **Tandaan:** Magwawakas ang GitHub Models sa katapusan ng Hulyo 2026. Ang Microsoft Foundry Models ang direktang kapalit nito, na nag-aalok ng parehong libreng subukan na model catalog at Azure AI Inference SDK / OpenAI SDK na karanasan.

1. Pumunta sa [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) at gumawa (o buksan) ng Foundry project.
1. I-browse ang [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) at ideploy ang isang modelo, halimbawa `gpt-4o-mini`.
1. Sa pahina ng **Overview** ng proyekto, kopyahin ang **endpoint** at **API key**.
1. Gamitin ang endpoint value para sa `AZURE_INFERENCE_ENDPOINT` at ang key value para sa `AZURE_INFERENCE_CREDENTIAL` sa iyong `.env` file.

## Offline / Lokal na mga Tagapagbigay

Kung ayaw mong gumamit ng cloud subscription, maaari mong patakbuhin ang mga compatible na open model nang direkta sa iyong sariling device:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - On-device runtime ng Microsoft. Awtomatikong pinipili nito ang pinakamahusay na execution provider (NPU, GPU, o CPU) at naglalabas ng OpenAI-compatible endpoint, kaya maaari mong gamitin ang karamihan sa sample code sa kurso na ito nang minimal lang ang pagbabago. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para makapagsimula, o i-install gamit ang `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - isang sikat na alternatibo para patakbuhin ang mga open model tulad ng Llama, Phi, Mistral, at Gemma nang lokal.


Tingnan ang [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para sa mga praktikal na halimbawa gamit ang dalawang opsyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->