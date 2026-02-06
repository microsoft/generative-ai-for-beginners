# Pagpili at Pag-configure ng LLM Provider 🔑

Ang mga assignments **ay maaaring** i-setup upang gumana laban sa isa o higit pang Large Language Model (LLM) deployments sa pamamagitan ng isang suportadong service provider tulad ng OpenAI, Azure o Hugging Face. Nagbibigay ang mga ito ng _hosted endpoint_ (API) na maaari nating ma-access programmatically gamit ang tamang credentials (API key o token). Sa kursong ito, tatalakayin natin ang mga provider na ito:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang modelo kabilang ang core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para sa mga OpenAI models na may pokus sa enterprise readiness
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa open-source models at inference server

**Kakailanganin mong gamitin ang sarili mong mga account para sa mga pagsasanay na ito**. Ang mga assignments ay opsyonal kaya maaari kang pumili na i-setup ang isa, lahat - o wala - sa mga provider base sa iyong interes. Narito ang ilang gabay para sa pag-signup:

| Signup | Gastos | API Key | Playground | Mga Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Modelo ang Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Nang Maaga Para sa Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Limitado ang mga modelo sa Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sundin ang mga direksyon sa ibaba upang _i-configure_ ang repository na ito para magamit sa iba't ibang provider. Ang mga assignments na nangangailangan ng partikular na provider ay magkakaroon ng isa sa mga tag na ito sa kanilang filename:

- `aoai` - nangangailangan ng Azure OpenAI endpoint, key
- `oai` - nangangailangan ng OpenAI endpoint, key
- `hf` - nangangailangan ng Hugging Face token

Maaari kang mag-configure ng isa, wala, o lahat ng provider. Ang mga kaugnay na assignments ay mag-eerror lamang kapag kulang ang credentials.

## Gumawa ng `.env` file

Ipinagpapalagay namin na nabasa mo na ang gabay sa itaas at nakapag-signup ka na sa kaukulang provider, at nakuha mo na ang kinakailangang authentication credentials (API_KEY o token). Sa kaso ng Azure OpenAI, ipinagpapalagay din namin na mayroon kang valid deployment ng Azure OpenAI Service (endpoint) na may hindi bababa sa isang GPT model na naka-deploy para sa chat completion.

Ang susunod na hakbang ay i-configure ang iyong **local environment variables** tulad ng sumusunod:

1. Hanapin sa root folder ang `.env.copy` file na dapat ay may nilalaman tulad nito:

   ```bash
   # Tagapagbigay ng OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Nakatalaga na ang default!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopyahin ang file na iyon sa `.env` gamit ang command sa ibaba. Ang file na ito ay _gitignore-d_, kaya ligtas ang mga sikreto.

   ```bash
   cp .env.copy .env
   ```

3. Punan ang mga halaga (palitan ang mga placeholder sa kanang bahagi ng `=`) tulad ng inilalarawan sa susunod na seksyon.

4. (Opsyonal) Kung gumagamit ka ng GitHub Codespaces, may opsyon kang i-save ang environment variables bilang _Codespaces secrets_ na naka-associate sa repository na ito. Sa ganitong kaso, hindi mo na kailangang mag-setup ng lokal na .env file. **Gayunpaman, tandaan na gumagana lang ang opsyong ito kung gumagamit ka ng GitHub Codespaces.** Kailangan mo pa ring i-setup ang .env file kung gumagamit ka ng Docker Desktop.

## Punan ang `.env` file

Tingnan natin nang mabilis ang mga pangalan ng variable upang maunawaan kung ano ang kanilang kinakatawan:

| Variable  | Paglalarawan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na na-setup mo sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyo para sa non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para gamitin ang serbisyong iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang deployed endpoint para sa isang Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ model deployment endpoint |
| | |

Tandaan: Ang huling dalawang Azure OpenAI variables ay tumutukoy sa default na modelo para sa chat completion (text generation) at vector search (embeddings) ayon sa pagkakasunod. Ang mga tagubilin para sa pag-set ng mga ito ay ibibigay sa mga kaugnay na assignments.

## I-configure ang Azure: Mula sa Portal

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

## I-configure ang Azure: Mula sa Studio

1. Pumunta sa [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** tulad ng inilalarawan sa itaas.
1. I-click ang **Deployments** tab (sidebar, kaliwa) upang makita ang mga kasalukuyang na-deploy na modelo.
1. Kung ang nais mong modelo ay hindi pa na-deploy, gamitin ang **Create new deployment** upang i-deploy ito.
1. Kakailanganin mo ng _text-generation_ model - inirerekomenda namin: **gpt-35-turbo**
1. Kakailanganin mo ng _text-embedding_ model - inirerekomenda namin ang **text-embedding-ada-002**

Ngayon i-update ang environment variables upang ipakita ang _Deployment name_ na ginamit. Karaniwan itong kapareho ng pangalan ng modelo maliban kung binago mo ito nang tahasan. Halimbawa, maaari kang magkaroon ng:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Huwag kalimutang i-save ang .env file kapag tapos na**. Maaari mo nang isara ang file at bumalik sa mga tagubilin para patakbuhin ang notebook.

## I-configure ang OpenAI: Mula sa Profile

Makikita ang iyong OpenAI API key sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pa nito, maaari kang mag-signup para sa isang account at gumawa ng API key. Kapag nakuha mo na ang key, maaari mo itong gamitin upang punan ang `OPENAI_API_KEY` variable sa `.env` file.

## I-configure ang Hugging Face: Mula sa Profile

Makikita ang iyong Hugging Face token sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag itong i-post o i-share nang publiko. Sa halip, gumawa ng bagong token para sa paggamit ng proyektong ito at kopyahin ito sa `.env` file sa ilalim ng `HUGGING_FACE_API_KEY` variable. _Tandaan:_ Hindi ito teknikal na API key ngunit ginagamit para sa authentication kaya pinananatili namin ang ganitong pangalan para sa pagkakapare-pareho.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->