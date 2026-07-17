# Pagtatayo ng Mga Aplikasyon sa Paglikha ng Imahe

[![Pagtatayo ng Mga Aplikasyon sa Paglikha ng Imahe](../../../translated_images/tl/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Hindi lamang sa paglikha ng teksto umiikot ang LLMs. Maaari ka ring gumawa ng mga imahe mula sa mga paglalarawan ng teksto. Ang mga imahe bilang isang modality ay kapaki-pakinabang sa MedTech, arkitektura, turismo, pag-develop ng laro, marketing, at iba pa. Sa araling ito titingnan natin ang mga kasalukuyang **GPT Image** na modelo at gagawa tayo ng isang app para sa paglikha ng imahe.

## Panimula

Pinapayagan ka ng paglikha ng imahe na gawing larawan ang isang natural-language prompt. Sa araling ito gagamit tayo ng pamilya ng mga modelo na **`gpt-image`** mula sa OpenAI - ang kasalukuyang henerasyon ng mga modelo ng imahe na available sa **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** at sa plataporma ng OpenAI. Pinalitan ng mga modelong ito ang mga lumang DALL·E na modelo (DALL·E 2/3 ay mga legacy).

Sa buong aralin gagamit tayo ng isang kathang-isip na startup, **Edu4All**, na gumagawa ng mga learning tool. Nais ng koponan na gumawa ng mga ilustrasyon para sa mga takdang-aralin at materyales sa pag-aaral.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito ay magagawa mong:

- Ipaliwanag kung ano ang paglikha ng imahe at saan ito kapaki-pakinabang.
- Maunawaan ang pamilya ng `gpt-image` na modelo at kung paano ito naiiba sa mga legacy na DALL·E na modelo.
- Gumawa ng isang app sa paglikha ng imahe gamit ang Python (at TypeScript / .NET).
- I-edit ang mga imahe at maglagay ng safety guardrails gamit ang metaprompts.

## Ano ang paglikha ng imahe?

Lumilikha ang mga modelo ng paglikha ng imahe ng mga larawan mula sa isang text prompt. Ang mga modernong modelo tulad ng `gpt-image` ay ginawa gamit ang transformer + diffusion techniques: natututuhan ng modelo ang relasyon ng teksto at mga imahe sa panahon ng pagsasanay, pagkatapos, kapag may prompt, unti-unting "dinidenoise" ang random na ingay upang maging isang imahe na tumutugma sa paglalarawan.

Dalawang kilalang pamilya ng mga modelo ng imahe ay:

- **`gpt-image` (OpenAI)** - ang kasalukuyang henerasyon, na ginagamit sa araling ito. Sinusuportahan ang text-to-image generation at image editing (inpainting gamit ang mask).
- **Midjourney** - isang tanyag na third-party na modelo na may sariling serbisyo at Discord-based workflow.

> Ang mga lumang OpenAI na modelo ng imahe - **DALL·E 2** at **DALL·E 3** - ay mga legacy. Hindi na available ang DALL·E 3 para sa mga bagong deployment, at ang mga feature tulad ng `create_variation` ay nasa DALL·E 2 lamang. Gamitin ang mga `gpt-image` na modelo para sa mga bagong aplikasyon.

### Alin sa `gpt-image` na modelo ang dapat kong gamitin?

Sa Microsoft Foundry ang mga sumusunod ay **Generally Available**:

| Modelo | Mga Tala |
| --- | --- |
| **`gpt-image-2`** | Pinakabago at pinakamakapangyarihang modelo ng imahe - inirerekomendang default. |
| `gpt-image-1.5` | Generally available; mataas ang kalidad sa mas mababang gastos. |
| `gpt-image-1-mini` | Generally available; pinakamabilis / pinakamababang gastos. |
| `gpt-image-1` | Preview lamang. |

Palaging tingnan ang kasalukuyang [Foundry image models list](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) para sa availability at mga rehiyon.

> **Mahalaga:** Nagbabalik ang mga `gpt-image` na modelo ng nilikhang imahe bilang **base64** (`b64_json`), hindi bilang URL. Dina-decode ng iyong code ang base64 string patungo sa mga byte at sine-save ito - walang image URL na kailangang i-download.

## Setup

Maaari mong patakbuhin ang mga sample laban sa **Azure OpenAI sa Microsoft Foundry** (ang `aoai-*` na mga sample) o sa **OpenAI platform** (ang `oai-*` na mga sample).

### 1. Gumawa at i-deploy ang isang modelo

Sundan ang gabay na [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) upang gumawa ng Microsoft Foundry resource, pagkatapos i-deploy ang isang image model - inirerekomenda ang **`gpt-image-2`**.

### 2. I-configure ang iyong `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Hanapin ang mga halagang ito sa pahina ng **Deployments** ng iyong resource sa [Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. I-install ang mga library

Gumawa ng `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Pagkatapos ay gumawa at i-activate ang isang virtual environment at i-install:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Bumuo ng app

Gumawa ng `app.py` gamit ang sumusunod na code. Lumilikha ito ng imahe at sine-save bilang PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Ituro ang kliyente sa iyong Azure OpenAI (Microsoft Foundry) na resource.
# Kailangan ng mga image model ng bagong bersyon ng API - tingnan ang Foundry docs para sa kinakailangan ng iyong modelo.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # hal. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # pati na rin 1536x1024 (landscape), 1024x1536 (portrait), o "auto"
    n=1,
)

# Ang mga gpt-image model ay nagbabalik ng base64 (b64_json), hindi URL - i-decode ito sa bytes.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Patakbuhin ito gamit ang `python app.py`. Makakakuha ka ng PNG na na-save sa ilalim ng `images/`.

> Bawat tawag sa `images.generate` ay naglalabas ng ibang imahe para sa parehong prompt - hindi gumagamit ang mga image model ng `temperature` parameter (iyon ay para sa text generation control). Para magkaroon ng iba't ibang resulta, tawagin muli ang API; para mabawasan ang pagkakaiba-iba, gawing mas espesipiko ang iyong prompt.

## Pag-edit ng mga imahe

Kayang **i-edit** ng mga `gpt-image` na modelo ang umiiral na imahe: ibigay ang imahe, isang opsyonal na **mask** (na nagtatalaga ng lugar na babaguhin), at isang prompt na naglalarawan ng pagbabago. Tulad ng paglikha, ang mga edits ay ibinabalik bilang base64.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/tl/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/tl/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/tl/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Pagtatakda ng mga hangganan gamit ang metaprompts

Kapag kaya mo nang gumawa ng mga imahe, kailangan mo ng guardrails upang maiwasan ng iyong app na makabuo ng hindi ligtas o off-brand na nilalaman. Ang **metaprompt** ay teksto na dina-append mo sa prompt ng user upang limitahan ang output ng modelo.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# ipasa ang `prompt` sa client.images.generate(...)
```

Bawat imahe ay nililikha na ngayon sa loob ng mga hangganang itinakda ng metaprompt. Pagsamahin ito sa mga content filter na naka-built sa Microsoft Foundry para sa defense in depth.

## Takdang-aralin - tulungan nating ang mga estudyante

Kailangan ng mga estudyante ng Edu4All ng mga imahe para sa kanilang mga pagsusulit. Gumawa ng app na lumilikha ng mga imahe ng **monumento** (alin mang monumento ay nasa iyong desisyon) na inilalagay sa iba't ibang, malikhaing konteksto - halimbawa, isang tanyag na landmark sa paglubog ng araw na may batang nakamasid.

Subukan mo ito mismo, pagkatapos ay ikumpara sa mga reference na solusyon:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) buong generation app: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Gawin mo rin ang mga notebook sa [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` para sa Azure, `oai-assignment.ipynb` para sa OpenAI).

## Magaling! Ipagpatuloy ang iyong pag-aaral

Pagkatapos makumpleto ang araling ito, silipin ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na mapalago ang iyong kaalaman sa Generative AI!

Pumunta sa lesson 10 upang ipagpatuloy ang pag-aaral.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->