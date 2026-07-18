# Выбор и настройка поставщика LLM 🔑

Задания **могут** также быть настроены для работы с одним или несколькими развертываниями Больших Языковых Моделей (LLM) через поддерживаемого поставщика услуг, такого как OpenAI, Azure или Hugging Face. Они предоставляют _хостинг-эндпоинт_ (API), к которому мы можем программно обращаться, имея правильные учетные данные (API-ключ или токен). В этом курсе мы рассматриваем следующих поставщиков:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразными моделями, включая основную серию GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI с упором на корпоративную готовность
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) с единым эндпоинтом и API-ключом для доступа к сотням моделей от OpenAI, Meta, Mistral, Cohere, Microsoft и других (заменяет GitHub Models, который будет закрыт в конце июля 2026 года)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для моделей с открытым исходным кодом и сервера инференса
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) или [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), если вы предпочитаете запускать модели полностью офлайн на своем устройстве, без необходимости облачной подписки

**Вам потребуется использовать свои собственные аккаунты для этих упражнений**. Задания являются необязательными, поэтому вы можете настроить одного, всех или ни одного из поставщиков в зависимости от ваших интересов. Некоторые рекомендации по регистрации:

| Регистрация | Стоимость | API-ключ | Песочница | Комментарии |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Цены](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [На уровне проекта](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Веб, без кода](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно множество моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Цены](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Быстрый старт](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Быстрый старт в Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Необходимо предварительное одобрение для доступа](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) |
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Цены](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Страница обзора проекта](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Песочница Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Бесплатный уровень доступен; один эндпоинт + ключ для многих поставщиков моделей |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цены](https://huggingface.co/pricing) | [Токены доступа](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [В Hugging Chat ограниченное количество моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Бесплатно (запускается на вашем устройстве) | Не требуется | [Локальный CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Полностью офлайн, совместимый с OpenAI эндпоинт |
| | | | | |

Следуйте инструкциям ниже, чтобы _настроить_ этот репозиторий для использования с разными поставщиками. Задания, требующие конкретного поставщика, будут содержать один из этих тегов в имени файла:

- `aoai` - требует Azure OpenAI эндпоинт и ключ
- `oai` - требует OpenAI эндпоинт и ключ
- `hf` - требует токен Hugging Face
- `githubmodels` - требует Microsoft Foundry Models эндпоинт и ключ (GitHub Models будет закрыт в конце июля 2026)

Вы можете настроить одного, никого или всех поставщиков. Соответствующие задания просто выдадут ошибку при отсутствии учетных данных.

## Создание файла `.env`

Предполагается, что вы уже прочитали приведенные выше инструкции, зарегистрировались у нужного поставщика и получили необходимые аутентификационные данные (API_KEY или токен). В случае Azure OpenAI предполагается, что у вас также есть действующее развертывание Azure OpenAI Service (эндпоинт) с по крайней мере одной GPT-моделью, развернутой для чат-комплитов.

Следующий шаг — настроить ваши **локальные переменные окружения** следующим образом:

1. Найдите в корневой папке файл `.env.copy` с содержимым примерно такого вида:

   ```bash
   # Поставщик OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI в Microsoft Foundry
   ## (Сервис Azure OpenAI теперь часть Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Установлено по умолчанию! (текущая стабильная версия GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Модели Microsoft Foundry (каталог моделей с несколькими поставщиками, заменяет GitHub Models, который будет закрыт в конце июля 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Скопируйте этот файл в `.env` с помощью приведенной команды. Этот файл указан в .gitignore, что обеспечивает безопасность секретов.

   ```bash
   cp .env.copy .env
   ```

3. Заполните значения (замените заполнители справа от `=`) как описано в следующем разделе.

4. (Опционально) Если вы используете GitHub Codespaces, у вас есть возможность сохранить переменные окружения как _секреты Codespaces_, связанные с этим репозиторием. В этом случае создавать локальный файл .env не потребуется. **Однако обратите внимание, что этот вариант работает только при использовании GitHub Codespaces.** Если вы используете Docker Desktop, все равно нужно настроить файл .env.

## Заполнение файла `.env`

Давайте быстро рассмотрим названия переменных, чтобы понять, что они означают:

| Переменная  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Это токен доступа пользователя, который вы настроили в своем профиле |
| OPENAI_API_KEY | Ключ авторизации для использования сервиса вне Azure OpenAI |
| AZURE_OPENAI_API_KEY | Ключ авторизации для использования Azure OpenAI сервисов |
| AZURE_OPENAI_ENDPOINT | Развернутый эндпоинт для ресурса Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Эндпоинт развертывания модели _генерации текста_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Эндпоинт развертывания модели _векторных представлений_ (эмбеддингов) |
| AZURE_INFERENCE_ENDPOINT | Эндпоинт вашего проекта Microsoft Foundry, используемый для Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | API ключ вашего проекта Microsoft Foundry |
| | |

Примечание: Последние две переменные Azure OpenAI соответствуют модели по умолчанию для чат-комплита (генерации текста) и векторного поиска (эмбеддингов) соответственно. Инструкции по их настройке будут приведены в соответствующих заданиях.

## Настройка Azure OpenAI: через портал

> **Примечание:** Azure OpenAI Service теперь входит в состав [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурсы и развертывания по-прежнему отображаются в Azure Portal, но повседневное управление моделями (развертывания, песочница, мониторинг) теперь осуществляется через портал Foundry вместо прежней отдельной "Azure OpenAI Studio".

Значения эндпоинта и ключа Azure OpenAI вы найдете в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), поэтому начнем оттуда.

1. Перейдите в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst).
1. Нажмите опцию **Ключи и эндпоинт** в боковой панели (меню слева).
1. Нажмите **Показать ключи** — вы увидите: КЛЮЧ 1, КЛЮЧ 2 и Эндпоинт.
1. Используйте значение КЛЮЧ 1 для AZURE_OPENAI_API_KEY.
1. Используйте значение Эндпоинт для AZURE_OPENAI_ENDPOINT.

Далее нам понадобятся эндпоинты для конкретных развернутых моделей.

1. Нажмите опцию **Развертывания моделей** в боковой панели (левое меню) для ресурса Azure OpenAI.
1. На открывшейся странице нажмите **Перейти в портал Microsoft Foundry** (или **Управление развертываниями**, в зависимости от типа ресурса).

Вы попадете в портал Microsoft Foundry, где можно будет найти остальные значения, как описано ниже.

## Настройка Azure OpenAI: через портал Microsoft Foundry

1. Перейдите в [портал Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **через ваш ресурс**, как описано выше.
1. Нажмите вкладку **Развертывания** (боковая панель слева), чтобы увидеть текущие развернутые модели.
1. Если нужная модель не развернута, используйте **Развернуть модель** для ее развертывания из [каталога моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Вам потребуется модель _генерации текста_ — мы рекомендуем: **gpt-5-mini**.
1. Вам потребуется модель _векторных представлений текста_ — мы рекомендуем **text-embedding-3-small**.

Теперь обновите переменные окружения, чтобы отражать используемое имя _развертывания_. Обычно оно совпадает с названием модели, если вы не меняли его явно. Например, у вас может быть:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не забудьте сохранить файл .env после заполнения**. Теперь вы можете закрыть файл и вернуться к инструкциям для запуска ноутбука.

## Настройка OpenAI: Из профиля

Ваш API-ключ OpenAI можно найти в вашем [аккаунте OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Если у вас его нет, зарегистрируйтесь и создайте API-ключ. После получения ключа используйте его для заполнения переменной `OPENAI_API_KEY` в файле `.env`.

## Настройка Hugging Face: Из профиля

Ваш токен Hugging Face можно найти в настройках профиля на странице [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикуйте и не делитесь токенами публично. Вместо этого создайте новый токен для использования в этом проекте и скопируйте его в файл `.env` под переменную `HUGGING_FACE_API_KEY`. _Примечание:_ технически это не API-ключ, но используется для аутентификации, поэтому мы сохраняем данное имя переменной для согласованности.

## Настройка Microsoft Foundry Models: Через портал

> **Примечание:** GitHub Models будет закрыт в конце июля 2026 года. Microsoft Foundry Models является его прямой заменой, предлагая тот же каталог моделей с бесплатным пробным периодом и опыт использования Azure AI Inference SDK / OpenAI SDK.

1. Перейдите на [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) и создайте (или откройте) проект Foundry.
1. Просмотрите [каталог моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) и разверните нужную модель, например `gpt-5-mini`.
1. На странице **Обзор** проекта скопируйте **эндпоинт** и **API-ключ**.
1. Используйте значение эндпоинта для `AZURE_INFERENCE_ENDPOINT` и ключ для `AZURE_INFERENCE_CREDENTIAL` в вашем файле `.env`.

## Оффлайн / локальные провайдеры

Если вы вовсе не хотите использовать облачную подписку, вы можете запускать совместимые открытые модели напрямую на своем устройстве:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - локальное решение от Microsoft. Оно автоматически выбирает лучший доступный провайдер исполнения (NPU, GPU или CPU) и предоставляет совместимый с OpenAI эндпоинт, так что вы можете использовать большую часть примеров из этого курса с минимальными изменениями. См. [документацию Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) для начала или установите с помощью `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популярная альтернатива для запуска открытых моделей, таких как Llama, Phi, Mistral и Gemma локально.


См. [Урок 19: Создание с помощью SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) для практических примеров с использованием обоих вариантов.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->