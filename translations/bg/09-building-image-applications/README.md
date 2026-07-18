# Създаване на приложения за генериране на изображения

[![Създаване на приложения за генериране на изображения](../../../translated_images/bg/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM моделите не са само за генериране на текст. Можете също така да генерирате изображения от текстови описания. Изображенията като модалност са полезни в МедТех, архитектура, туризъм, разработка на игри, маркетинг и други. В този урок разглеждаме днешните модели **GPT Image** и създаваме приложение за генериране на изображения.

## Въведение

Генерирането на изображения ви позволява да превърнете естествено езиково подканване в картина. В този урок работим със семейството от модели **`gpt-image`** на OpenAI - текущото поколение модели за изображения, достъпни на **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** и платформата OpenAI. Тези модели заменят по-старите модели DALL·E (DALL·E 2/3 са наследени).

През целия урок използваме измислен стартъп, **Edu4All**, който разработва учебни инструменти. Екипът иска да генерира илюстрации за задачи и учебни материали.

## Учебни цели

В края на този урок ще можете да:

- Обясните какво е генериране на изображения и къде е полезно.
- Разберете семейството от модели `gpt-image` и как се различава от наследените модели DALL·E.
- Създадете приложение за генериране на изображения с Python (и TypeScript / .NET).
- Редактирате изображения и прилагате защитни механизми с метаподканвания.

## Какво е генериране на изображения?

Моделите за генериране на изображения създават изображения от текстово подканване. Модерните модели като `gpt-image` са базирани на техники трансформър + дифузия: моделът научава връзката между текст и изображения по време на обучението, след което при подканване итеративно "почиства" случайния шум до изображение, което съответства на описанието.

Две добре познати семейства модели за изображения са:

- **`gpt-image` (OpenAI)** – текущото поколение, използвано в този урок. Поддържа генериране от текст към изображение и редактиране на изображения (inpainting с маска).
- **Midjourney** – популярен трети страничен модел със собствена услуга и workflow в Discord.

> По-старите модели на OpenAI за изображения - **DALL·E 2** и **DALL·E 3** - са наследени. DALL·E 3 вече не е достъпен за нови внедрявания, а функции като `create_variation` са съществували само в DALL·E 2. Използвайте моделите `gpt-image` за нови приложения.

### Кой модел `gpt-image` да използвам?

На Microsoft Foundry следните модели са **Общо достъпни**:

| Модел | Бележки |
| --- | --- |
| **`gpt-image-2`** | Най-новият и най-способен модел за изображения - препоръчителен по подразбиране. |
| `gpt-image-1.5` | Общо достъпен; силно качество при по-ниска цена. |
| `gpt-image-1-mini` | Общо достъпен; най-бърз / най-ниска цена. |
| `gpt-image-1` | Само за преглед. |

Винаги проверявайте текущия [списък с модели за изображения на Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) за наличност и региони.

> **Важно:** Моделите `gpt-image` връщат генерираното изображение като **base64** (`b64_json`), а не като URL. Вашият код декодира base64 стринга към байтове и го записва - няма URL за изтегляне на изображение.

## Настройка

Можете да изпълнявате примерите срещу **Azure OpenAI в Microsoft Foundry** (примерите `aoai-*`) или платформата **OpenAI** (примерите `oai-*`).

### 1. Създайте и внедрете модел

Следвайте ръководството [създаване на ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), за да създадете ресурс в Microsoft Foundry, след което внедрете модел за изображения – препоръчва се **`gpt-image-2`**.

### 2. Конфигурирайте вашия `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Намерете тези стойности на страницата **Deployments** на вашия ресурс в [портала Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Инсталирайте библиотеките

Създайте `requirements.txt`:

```text
python-dotenv
openai
pillow
```

След това създайте и активирайте виртуална среда и инсталирайте:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Създаване на приложението

Създайте `app.py` със следния код. Той генерира изображение и го запазва като PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Насочете клиента към вашия Azure OpenAI (Microsoft Foundry) ресурс.
# Моделите за изображения изискват скорошна версия на API - проверете документацията на Foundry за версията, необходима за вашия модел.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # например "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # също 1536x1024 (пейзаж), 1024x1536 (портрет), или "auto"
    n=1,
)

# моделите gpt-image връщат base64 (b64_json), а не URL - декодирайте го в байтове.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Стартирайте с `python app.py`. Ще получите PNG, запазен в `images/`.

> Всяко извикване на `images.generate` произвежда различно изображение за същото подканване – моделите за изображения не използват параметър `temperature` (това е контрол за генериране на текст). За разнообразие просто извикайте API отново; за намаляване на разнообразието направете вашето подканване по-конкретно.

## Редактиране на изображения

Моделите `gpt-image` могат да **редактират** съществуващо изображение: предоставете изображението, опционална **маска** (която маркира зоната за промяна) и подканване, описващо промяната. Подобно на генерирането, редакциите се връщат като base64.

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
  <img src="../../../translated_images/bg/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/bg/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/bg/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Поставяне на граници с метаподканвания

След като можете да генерирате изображения, трябва да има защитни граници, за да не позволите на приложението да създава небезопасно или несъвместимо съдържание. **Метаподканване** е текст, който се добавя пред подканването на потребителя, за да ограничи изхода на модела.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# предайте `prompt` на client.images.generate(...)
```

Всяко изображение сега се генерира в рамките на границите, зададени от метаподканването. Комбинирайте това с вградените филтри за съдържание в Microsoft Foundry за дълбока защита.

## Задача - да помогнем на учениците

Учениците в Edu4All се нуждаят от изображения за своите оценки. Създайте приложение, което генерира изображения на **паметници** (кои паметници избирате зависи от вас), поставени в различни, креативни контексти – например известна забележителност при залез слънце с дете, което гледа.

Опитайте сами, после сравнете с референтните решения:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) пълно приложение за генериране: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Също така работете с ноутбуките в [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` за Azure, `oai-assignment.ipynb` за OpenAI).

## Отлична работа! Продължете ученето

След завършване на този урок разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си за Генеративен AI!

Отидете към урок 10, за да продължите обучението си.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->