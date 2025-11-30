<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:29:53+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "tl"
}
-->
# Pagpili at Pag-configure ng LLM Provider 🔑

Maaaring i-setup ang mga assignment para gumana gamit ang isa o higit pang Large Language Model (LLM) deployments sa pamamagitan ng mga suportadong service provider tulad ng OpenAI, Azure, o Hugging Face. Nagbibigay ang mga ito ng _hosted endpoint_ (API) na maaari nating ma-access gamit ang tamang credentials (API key o token). Sa kursong ito, tatalakayin natin ang mga sumusunod na provider:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na may iba't ibang modelo kabilang ang core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para sa mga OpenAI model na nakatuon sa enterprise readiness
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para sa open-source na mga modelo at inference server

**Kailangan mong gumamit ng sarili mong account para sa mga exercise na ito**. Opsyonal ang mga assignment kaya maaari kang pumili kung alin sa mga provider ang gusto mong i-setup—isa, lahat, o wala depende sa iyong interes. Narito ang ilang gabay para sa pag-signup:

| Signup | Gastos | API Key | Playground | Komento |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Presyo](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Maraming Modelong Pwedeng Pagpilian |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Presyo](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Kailangang Mag-apply Muna Para sa Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Presyo](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Limitado ang mga model sa Hugging Chat](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sundin ang mga tagubilin sa ibaba para _i-configure_ ang repository na ito para magamit sa iba't ibang provider. Ang mga assignment na nangangailangan ng partikular na provider ay magkakaroon ng isa sa mga tag na ito sa kanilang filename:

- `aoai` - nangangailangan ng Azure OpenAI endpoint at key
- `oai` - nangangailangan ng OpenAI endpoint at key
- `hf` - nangangailangan ng Hugging Face token

Maaari kang mag-configure ng isa, wala, o lahat ng provider. Ang mga kaugnay na assignment ay mag-e-error lang kung kulang ang credentials.

## Gumawa ng `.env` file

Ina-assume namin na nabasa mo na ang gabay sa itaas at nakapag-sign up ka na sa napiling provider, at nakuha mo na ang kinakailangang authentication credentials (API_KEY o token). Para sa Azure OpenAI, ina-assume din namin na may valid kang deployment ng Azure OpenAI Service (endpoint) na may kahit isang GPT model na naka-deploy para sa chat completion.

Ang susunod na hakbang ay i-configure ang iyong **local environment variables** tulad ng sumusunod:

1. Hanapin sa root folder ang `.env.copy` file na may laman na ganito:

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

2. Kopyahin ang file na iyon bilang `.env` gamit ang command sa ibaba. Ang file na ito ay _gitignore-d_, kaya ligtas ang iyong mga sikreto.

   ```bash
   cp .env.copy .env
   ```

3. Punan ang mga value (palitan ang mga placeholder sa kanan ng `=`) ayon sa susunod na seksyon.

4. (Opsyonal) Kung gumagamit ka ng GitHub Codespaces, maaari mong i-save ang environment variables bilang _Codespaces secrets_ na naka-link sa repository na ito. Sa ganitong kaso, hindi mo na kailangang mag-setup ng local .env file. **Tandaan: Gagana lang ito kung GitHub Codespaces ang gamit mo.** Kailangan mo pa ring mag-setup ng .env file kung Docker Desktop ang gamit mo.

## Punan ang `.env` file

Tingnan natin saglit ang mga pangalan ng variable para maintindihan kung ano ang ibig sabihin ng mga ito:

| Variable  | Deskripsyon  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ito ang user access token na sine-setup mo sa iyong profile |
| OPENAI_API_KEY | Ito ang authorization key para magamit ang serbisyo para sa non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Ito ang authorization key para magamit ang serbisyo na iyon |
| AZURE_OPENAI_ENDPOINT | Ito ang deployed endpoint para sa Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Ito ang _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ito ang _text embeddings_ model deployment endpoint |
| | |

Tandaan: Ang huling dalawang Azure OpenAI variable ay tumutukoy sa default na model para sa chat completion (text generation) at vector search (embeddings). Ang mga tagubilin para i-set up ang mga ito ay ilalagay sa mga kaugnay na assignment.

## I-configure ang Azure: Mula sa Portal

Makikita ang Azure OpenAI endpoint at key values sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kaya doon tayo magsisimula.

1. Pumunta sa [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. I-click ang **Keys and Endpoint** sa sidebar (menu sa kaliwa).
1. I-click ang **Show Keys** – makikita mo ang: KEY 1, KEY 2 at Endpoint.
1. Gamitin ang KEY 1 value para sa AZURE_OPENAI_API_KEY
1. Gamitin ang Endpoint value para sa AZURE_OPENAI_ENDPOINT

Susunod, kailangan natin ang endpoints para sa mga partikular na model na na-deploy natin.

1. I-click ang **Model deployments** sa sidebar (kaliwang menu) para sa Azure OpenAI resource.
1. Sa page na iyon, i-click ang **Manage Deployments**

Dadalin ka nito sa Azure OpenAI Studio website, kung saan makikita natin ang iba pang values gaya ng nakasaad sa ibaba.

## I-configure ang Azure: Mula sa Studio

1. Pumunta sa [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **mula sa iyong resource** gaya ng nabanggit sa itaas.
1. I-click ang **Deployments** tab (sidebar, kaliwa) para makita ang mga kasalukuyang naka-deploy na model.
1. Kung hindi pa naka-deploy ang gusto mong model, gamitin ang **Create new deployment** para i-deploy ito.
1. Kailangan mo ng _text-generation_ model – inirerekomenda namin ang: **gpt-35-turbo**
1. Kailangan mo ng _text-embedding_ model – inirerekomenda namin ang **text-embedding-ada-002**

Ngayon, i-update ang environment variables para tumugma sa _Deployment name_ na ginamit. Karaniwan, ito ay kapareho ng model name maliban na lang kung binago mo ito. Halimbawa, maaaring ganito ang laman:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Huwag kalimutang i-save ang .env file kapag tapos ka na**. Maaari mo nang isara ang file at bumalik sa mga tagubilin para patakbuhin ang notebook.

## I-configure ang OpenAI: Mula sa Profile

Makikita mo ang iyong OpenAI API key sa iyong [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kung wala ka pa nito, mag-sign up para sa account at gumawa ng API key. Kapag nakuha mo na ang key, gamitin ito para punan ang `OPENAI_API_KEY` variable sa `.env` file.

## I-configure ang Hugging Face: Mula sa Profile

Makikita mo ang iyong Hugging Face token sa iyong profile sa ilalim ng [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Huwag itong ipost o ibahagi sa publiko. Sa halip, gumawa ng bagong token para sa proyektong ito at kopyahin iyon sa `.env` file sa ilalim ng `HUGGING_FACE_API_KEY` variable. _Tandaan:_ Hindi talaga ito API key pero ginagamit ito para sa authentication kaya pinanatili natin ang pangalan para sa consistency.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.