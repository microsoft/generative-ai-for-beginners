# Выбор и настройка провайдера LLM 🔑

Задания **могут** быть настроены для работы с одной или несколькими развертками Больших Языковых Моделей (LLM) через поддерживаемого провайдера услуг, такого как OpenAI, Azure или Hugging Face. Они предоставляют _хостинг-эндпоинт_ (API), к которому мы можем получить программный доступ с нужными учетными данными (ключ API или токен). В этом курсе мы рассматриваем следующих провайдеров:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразными моделями, включая основную серию GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI с упором на корпоративную готовность
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) для одного эндпоинта и ключа API с доступом к сотням моделей от OpenAI, Meta, Mistral, Cohere, Microsoft и других (заменяет GitHub Models, который будет закрыт в конце июля 2026 года)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для моделей с открытым исходным кодом и сервера инференса
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) или [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), если вы предпочитаете запускать модели полностью офлайн на своем устройстве без необходимости облачной подписки

**Для этих упражнений вам понадобятся свои собственные аккаунты**. Задания необязательные, поэтому вы можете настроить одного, всех или ни одного из провайдеров по своему усмотрению. Немного советов по регистрации:

| Регистрация | Стоимость | Ключ API | Песочница | Комментарии |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цены](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Проектные ключи](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Веб без кода](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно несколько моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цены](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Быстрый старт SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Быстрый старт Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Необходимо предварительное одобрение для доступа](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Цены](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Страница обзора проекта](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Песочница Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Доступен бесплатный уровень; один эндпоинт и ключ для множества провайдеров моделей |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цены](https://huggingface.co/pricing) | [Токены доступа](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [В Hugging Chat ограниченный набор моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Бесплатно (запускается на вашем устройстве) | Не требуется | [Локальный CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Полностью офлайн, совместимый с OpenAI эндпоинт |
| | | | | |

Следуйте указаниям ниже, чтобы _настроить_ этот репозиторий для работы с разными провайдерами. Задания, требующие определенного провайдера, будут иметь один из этих тегов в имени файла:

- `aoai` - требует Azure OpenAI эндпоинт и ключ
- `oai` - требует OpenAI эндпоинт и ключ
- `hf` - требует токен Hugging Face
- `githubmodels` - требует Microsoft Foundry Models эндпоинт, ключ (GitHub Models закрывается в конце июля 2026)

Вы можете настроить одного, всех или ни одного из провайдеров. Связанные задания просто выведут ошибку при отсутствии учетных данных.

## Создайте файл `.env`

Мы предполагаем, что вы уже прочитали вышеуказанные инструкции, зарегистрировались у нужного провайдера и получили необходимые данные для аутентификации (API_KEY или токен). В случае с Azure OpenAI предполагается, что у вас есть действующая развертка Azure OpenAI Service (эндпоинт) с хотя бы одной GPT моделью, развернутой для завершения чата.

Следующий шаг — настроить ваши **локальные переменные окружения** следующим образом:

1. Найдите в корневой папке файл `.env.copy`, который должен содержать такой текст:

   ```bash
   # Поставщик OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI в Microsoft Foundry
   ## (Служба Azure OpenAI теперь является частью Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # По умолчанию установлено! (текущая стабильная версия API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Модели Microsoft Foundry (каталог моделей с несколькими поставщиками, заменяет модели GitHub, которые будут закрыты в конце июля 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Скопируйте этот файл в `.env` с помощью следующей команды. Этот файл _игнорируется git_, чтобы ваши секреты оставались в безопасности.

   ```bash
   cp .env.copy .env
   ```

3. Заполните значения (замените заполнители справа от `=`) как описано в следующем разделе.

4. (Опционально) Если вы используете GitHub Codespaces, у вас есть возможность сохранить переменные окружения как _секреты Codespaces_, связанные с этим репозиторием. В таком случае вам не нужно настраивать локальный файл .env. **Однако обратите внимание, что эта опция работает только для GitHub Codespaces.** Если вы используете Docker Desktop, файл .env все равно нужно будет настроить.

## Заполнение файла `.env`

Давайте быстро рассмотрим названия переменных, чтобы понять, что они означают:

| Переменная  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Токен доступа пользователя, который вы настраиваете в своем профиле |
| OPENAI_API_KEY | Ключ авторизации для использования сервиса вне Azure OpenAI эндпоинтов |
| AZURE_OPENAI_API_KEY | Ключ авторизации для данного сервиса |
| AZURE_OPENAI_ENDPOINT | Развернутый эндпоинт для ресурса Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Эндпоинт развертки модели _генерации текста_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Эндпоинт развертки модели _векторных эмбеддингов_ |
| AZURE_INFERENCE_ENDPOINT | Эндпоинт для вашего проекта Microsoft Foundry, используется для Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ключ API для вашего проекта Microsoft Foundry |
| | |

Примечание: Последние две переменные Azure OpenAI отражают модель по умолчанию для завершения чата (генерация текста) и векторного поиска (эмбеддинги) соответственно. Инструкции по их настройке будут даны в соответствующих заданиях.

## Настройка Azure OpenAI: через портал

> **Примечание:** Служба Azure OpenAI теперь является частью [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурсы и развертки все еще отображаются в портале Azure, но ежедневное управление моделями (развертки, песочница, мониторинг) теперь происходит в портале Foundry вместо старого отдельного "Azure OpenAI Studio".

Значения эндпоинта и ключа Azure OpenAI можно найти в [портале Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), начнем с него.

1. Перейдите в [портал Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Нажмите на опцию **Keys and Endpoint** в боковом меню (слева).
1. Нажмите **Show Keys** — вы увидите: KEY 1, KEY 2 и Endpoint.
1. Используйте значение KEY 1 для AZURE_OPENAI_API_KEY
1. Используйте значение Endpoint для AZURE_OPENAI_ENDPOINT

Далее нам нужны эндпоинты конкретных моделей, которые мы развернули.

1. В боковом меню (слева) выберите опцию **Model deployments** для ресурса Azure OpenAI.
1. На странице перейдите по ссылке **Go to Microsoft Foundry portal** (или **Manage Deployments** в зависимости от типа ресурса)

Это приведет вас в портал Microsoft Foundry, где мы найдем другие необходимые значения, как описано ниже.

## Настройка Azure OpenAI: через портал Microsoft Foundry

1. Перейдите в [портал Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **через ваш ресурс**, как описано выше.
1. Нажмите вкладку **Deployments** (боковая панель, слева), чтобы увидеть текущие развернутые модели.
1. Если нужная модель не развернута, используйте **Deploy model** для её развертывания из [каталога моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Вам понадобится модель _генерации текста_ — мы рекомендуем: **gpt-4o-mini**
1. Вам понадобится модель _векторных эмбеддингов_ — мы рекомендуем **text-embedding-3-small**

Теперь обновите переменные окружения, чтобы они отражали имя _Deployment_, которое вы использовали. Обычно это совпадает с именем модели, если вы явно не меняли его. Например, у вас может быть:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не забудьте сохранить файл .env после изменений**. Теперь вы можете закрыть файл и вернуться к инструкциям по запуску ноутбука.

## Настройка OpenAI: через профиль

Ваш ключ OpenAI API можно найти в вашем [аккаунте OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Если у вас его нет, вы можете зарегистрироваться и создать ключ API. После получения ключа используйте его для заполнения переменной `OPENAI_API_KEY` в файле `.env`.

## Настройка Hugging Face: через профиль

Ваш токен Hugging Face можно найти в вашем профиле в разделе [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикуйте и не делитесь им публично. Вместо этого создайте новый токен для использования в этом проекте и скопируйте его в файл `.env` в переменную `HUGGING_FACE_API_KEY`. _Примечание:_ технически это не ключ API, но используется для аутентификации, поэтому для удобства мы сохраняем это наименование.

## Настройка Microsoft Foundry Models: через портал

> **Примечание:** GitHub Models закрывается в конце июля 2026 года. Microsoft Foundry Models является прямой заменой с тем же каталогом моделей для бесплатного тестирования и поддержкой Azure AI Inference SDK / OpenAI SDK.

1. Перейдите на [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) и создайте (или откройте) проект Foundry.
1. Просмотрите [каталог моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) и разверните модель, например `gpt-4o-mini`.
1. На странице **Обзор** проекта скопируйте **эндпоинт** и **ключ API**.
1. Используйте значение эндпоинта для `AZURE_INFERENCE_ENDPOINT` и ключ для `AZURE_INFERENCE_CREDENTIAL` в вашем файле `.env`.

## Офлайн / Локальные провайдеры

Если вы предпочитаете совсем не использовать облачную подписку, вы можете запускать совместимые открытые модели непосредственно на своем устройстве:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - локальное среда выполнения Microsoft. Она автоматически выбирает лучший провайдер выполнения (NPU, GPU или CPU) и предоставляет совместимый с OpenAI эндпоинт, что позволяет повторно использовать большую часть кода из этого курса с минимальными изменениями. Смотрите [документацию Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) для начала или установите с помощью `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популярная альтернатива для локального запуска открытых моделей, таких как Llama, Phi, Mistral и Gemma.


Смотрите [Урок 19: Создание с помощью SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) для практических примеров использования обоих вариантов.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->