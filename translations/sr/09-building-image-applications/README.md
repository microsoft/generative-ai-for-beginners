# Прављење апликација за генерисање слика

[![Прављење апликација за генерисање слика](../../../translated_images/sr/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

ЛЛМ модели нису само за генерисање текста. Можете такође генерисати слике из текстуалних описа. Слике као модалитет су корисне у МедТеху, архитектури, туризму, развоју игара, маркетингу и још много тога. У овој лекцији погледаћемо данашње **GPT Image** моделе и направити апликацију за генерисање слика.

## Увод

Генерисање слика вам омогућава да претворите природно језичке упите у слику. У овој лекцији користимо породицу модела **`gpt-image`** компаније OpenAI - тренутну генерацију модела за слике доступних на **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** и OpenAI платформи. Ови модели замењују старије DALL·E моделе (DALL·E 2/3 су наслеђе).

Током лекције користимо имагинарни стартап, **Edu4All**, који прави алате за учење. Тим жели да генерише илустрације за задатке и материјале за учење.

## Циљеви учења

До краја ове лекције моћи ћете да:

- Објасните шта је генерисање слика и где је корисно.
- Разумете породицу модела `gpt-image` и како се разликује од старих DALL·E модела.
- Направите апликацију за генерисање слика у Python-у (и TypeScript / .NET).
- Уређујете слике и примењујете безбедносне мере користећи метапромпте.

## Шта је генерисање слика?

Модели за генерисање слика стварају слике из текстуалног упита. Модерни модели као што је `gpt-image` базирани су на техникама трансформера + дифузије: модел учи везу између текста и слика током тренинга, а затим, дати упит, итеративно "отстрањује шум" из насумичног шума до слике која одговара опису.

Две добро познате породице модела за слике су:

- **`gpt-image` (OpenAI)** - тренутна генерација, користи се у овој лекцији. Подржава генерисање слика из текста и уређивање слика (inpainting са маском).
- **Midjourney** - популарни модел треће стране са својом услугом и Discord-базираним радним током.

> Старији OpenAI модели за слике - **DALL·E 2** и **DALL·E 3** - су наслеђе. DALL·E 3 више није доступан за нове имплементације, а функције као `create_variation` су постојале само у DALL·E 2. За нове апликације користите `gpt-image` моделе.

### Који `gpt-image` модел да користим?

На Microsoft Foundry следећи су **Опште доступни**:

| Модел | Белешке |
| --- | --- |
| **`gpt-image-2`** | Најновији и најспособнији модел за слике - препоручени подразумевани. |
| `gpt-image-1.5` | Опште доступан; јака квалитета уз мање трошкове. |
| `gpt-image-1-mini` | Опште доступан; најбржи / најјефтинији. |
| `gpt-image-1` | Само преглед. |

Увек проверите тренутни [списак модела за слике Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) за доступност и регионе.

> **Важно:** `gpt-image` модели враћају генерисану слику као **base64** (`b64_json`), а не као URL. Ваш код декодира base64 стринг у бајтове и сачува - нема URL слике за преузимање.

## Подешавање

Можете покренути примерке против **Azure OpenAI на Microsoft Foundry-у** (примерци `aoai-*`) или **OpenAI платформе** (примерци `oai-*`).

### 1. Креирање и распоређивање модела

Следите водич [како направити ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) да направите Microsoft Foundry ресурс, затим распоредите модел за слике - препоручује се **`gpt-image-2`**.

### 2. Конфигуришите ваш `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Пронађите ове вредности на страници **Deployments** вашег ресурса у [Foundry порталу](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Инсталирајте библиотеке

Направите `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Онда направите и активирајте виртуелно окружење и инсталирајте:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Направите апликацију

Направите `app.py` са следећим кодом. Генерише слику и сачува је као PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Usmerite klijenta na vaš Azure OpenAI (Microsoft Foundry) resurs.
# Modeli za slike zahtevaju noviju verziju API-ja - proverite Foundry dokumentaciju za verziju koju vaš model zahteva.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # npr. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # takođe 1536x1024 (pejzaž), 1024x1536 (portret), ili "auto"
    n=1,
)

# gpt-image modeli vraćaju base64 (b64_json), a ne URL - dekodirajte ga u bajtove.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Покрените је са `python app.py`. Добићете PNG сачуван у `images/`.

> Сваки позив `images.generate` производи различиту слику за исти упит - модели за слике не користе параметар `temperature` (то је контролa за генерисање текста). Да бисте добили варијанте, једноставно позовите API поново; да бисте смањили варијанте, учините ваш упит специфичнијим.

## Уређивање слика

`gpt-image` модели могу **уредити** постојећу слику: доставите слику, опционалну **маску** (која означава област за промену) и упит који описује промену. Као и код генерисања, уређења се враћају као base64.

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
  <img src="../../../translated_images/sr/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sr/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sr/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Постављање граница помоћу метапромптова

Када можете да генеришете слике, требате безбедносне мере да ваша апликација не би производила несигуран или ван бренд садржај. **Метапромпт** је текст који додате испред упита корисника да ограничите излаз модела.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# проследити `prompt` функцији client.images.generate(...)
```

Свака слика сада се генерише у оквиру граница постављених метапромптом. Комбинујте ово са филтерима садржаја уграђеним у Microsoft Foundry ради вишеструке заштите.

## Задатак - омогућимо студентима

Студенти Edu4All-а требају слике за своје задатке. Направите апликацију која генерише слике **споменика** (то који споменици је на вама) смештених у различите, креативне контексте - на пример, познати споменик на заласку сунца и дете које гледа.

Испробајте сами, затим упоредите са референтним решењима:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) потпуно решење за генерисање: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Такође прођите кроз свеске у [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` за Azure, `oai-assignment.ipynb` за OpenAI).

## Одличан посао! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [Колекцију за учење генеративне АИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бисте наставили да унапређујете своје знање о генеративној АИ!

Пређите на лекцију 10 да бисте наставили учење.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->