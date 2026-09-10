# Создание приложений для генерации изображений

[![Создание приложений для генерации изображений](../../../translated_images/ru/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Возможности LLM выходят за рамки генерации текста. Вы также можете генерировать изображения по текстовым описаниям. Изображения как модальность полезны в MedTech, архитектуре, туризме, разработке игр, маркетинге и других областях. В этом уроке мы рассмотрим современные модели **GPT Image** и создадим приложение для генерации изображений.

## Введение

Генерация изображений позволяет превращать естественно-языковые подсказки в картинку. В этом уроке мы работаем с семейством моделей **`gpt-image`** от OpenAI — текущим поколением моделей для изображений, доступных на **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** и платформе OpenAI. Эти модели заменяют старые модели DALL·E (DALL·E 2/3 — устаревшие).

На протяжении урока мы используем вымышленный стартап **Edu4All**, создающий обучающие инструменты. Команда хочет генерировать иллюстрации для заданий и учебных материалов.

## Цели обучения

К концу этого урока вы сможете:

- Объяснить, что такое генерация изображений и где она полезна.
- Понять семейство моделей `gpt-image` и чем оно отличается от устаревших моделей DALL·E.
- Создать приложение для генерации изображений на Python (и TypeScript / .NET).
- Редактировать изображения и применять защитные метаподсказки.

## Что такое генерация изображений?

Модели генерации изображений создают картинки по текстовой подсказке. Современные модели, такие как `gpt-image`, основаны на трансформерах и диффузионных техниках: модель изучает связь между текстом и изображениями во время обучения, затем, получив подсказку, итеративно «очищает» случайный шум, превращая его в изображение, соответствующее описанию.

Два известных семейства моделей изображений:

- **`gpt-image` (OpenAI)** — текущее поколение, используемое в этом уроке. Поддерживает генерацию изображений из текста и редактирование изображений (заполнение с маской).
- **Midjourney** — популярная сторонняя модель с собственным сервисом и рабочим процессом через Discord.

> Старые модели изображений OpenAI — **DALL·E 2** и **DALL·E 3** — устаревшие. DALL·E 3 больше не доступен для новых развёртываний, а такие функции, как `create_variation`, были только в DALL·E 2. Для новых приложений используйте модели `gpt-image`.

### Какую модель `gpt-image` выбрать?

В Microsoft Foundry следующие модели доступны **в общем доступе**:

| Модель | Примечания |
| --- | --- |
| **`gpt-image-2`** | Последняя и самая мощная модель для изображений — рекомендуется по умолчанию. |
| `gpt-image-1.5` | В общем доступе; высокое качество при меньших затратах. |
| `gpt-image-1-mini` | В общем доступе; самая быстрая и с минимальными затратами. |
| `gpt-image-1` | Только для предварительного просмотра. |

Всегда проверяйте актуальный [список моделей изображений Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) по доступности и регионам.

> **Важно:** модели `gpt-image` возвращают сгенерированное изображение в формате **base64** (`b64_json`), а не как URL. Ваш код декодирует строку base64 в байты и сохраняет — URL для загрузки изображения отсутствует.

## Настройка

Вы можете запускать примеры как с **Azure OpenAI в Microsoft Foundry** (примеры `aoai-*`), так и с **платформы OpenAI** (примеры `oai-*`).

### 1. Создайте и разверните модель

Следуйте руководству [создать ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), чтобы создать ресурс в Microsoft Foundry, затем разверните модель для изображений — рекомендуется **`gpt-image-2`**.

### 2. Настройте ваш `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Найдите эти значения на странице **Deployments** вашего ресурса в [портале Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Установите библиотеки

Создайте `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Затем создайте и активируйте виртуальное окружение и установите:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Создание приложения

Создайте `app.py` со следующим кодом. Он генерирует изображение и сохраняет его в формате PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Укажите клиенту ваш ресурс Azure OpenAI (Microsoft Foundry).
# Для моделей изображений требуется последняя версия API - проверьте документацию Foundry для модели, которую вы используете.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # например, "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # также 1536x1024 (горизонтальная ориентация), 1024x1536 (портретная ориентация) или "авто"
    n=1,
)

# модели gpt-image возвращают base64 (b64_json), а не URL - декодируйте это в байты.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Запустите командой `python app.py`. Вы получите PNG, сохранённый в папке `images/`.

> Каждый вызов `images.generate` создаёт уникальное изображение для одной и той же подсказки — модели изображений не принимают параметр `temperature` (это управление для генерации текста). Чтобы получить разнообразие, просто вызовите API снова; чтобы уменьшить разнообразие — сделайте подсказку более конкретной.

## Редактирование изображений

Модели `gpt-image` могут **редактировать** существующее изображение: предоставьте изображение, необязательную **маску** (обозначающую область для изменения) и подсказку, описывающую изменение. Результаты, как и генерация, возвращаются в base64.

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
  <img src="../../../translated_images/ru/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ru/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ru/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Установка границ с метаподсказками

После того, как вы сможете генерировать изображения, нужны защитные механизмы, чтобы приложение не создавало небезопасный или не соответствующий бренду контент. **Метаподсказка** — текст, который добавляется перед подсказкой пользователя для ограничения вывода модели.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# передать `prompt` в client.images.generate(...)
```

Теперь каждое изображение генерируется в рамках, установленных метаподсказкой. Совместите это с встроенными фильтрами контента Microsoft Foundry для многоуровневой защиты.

## Задание — поможем студентам

Студентам Edu4All нужны изображения для их заданий. Создайте приложение, которое генерирует изображения **памятников** (каких именно — решайте вы), размещённых в различных творческих контекстах — например, известный памятник на закате с ребёнком, который смотрит на него.

Попробуйте сами, затем сравните с эталонными решениями:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Полное приложение генерации на Python (Azure): [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Также поработайте с блокнотами в папке [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` для Azure, `oai-assignment.ipynb` для OpenAI).

## Отличная работа! Продолжайте обучение

По завершении этого урока изучите нашу коллекцию [Обучение генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжать развивать свои знания по генеративному ИИ!

Перейдите к уроку 10 для дальнейшего обучения.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->