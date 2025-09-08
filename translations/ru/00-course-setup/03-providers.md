<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T13:51:00+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ru"
}
-->
# Выбор и настройка провайдера LLM 🔑

Задания **могут** быть настроены для работы с одним или несколькими развёрнутыми крупными языковыми моделями (LLM) через поддерживаемого провайдера, такого как OpenAI, Azure или Hugging Face. Эти сервисы предоставляют _хостинг-эндпоинт_ (API), к которому можно получить программный доступ при наличии правильных учётных данных (API-ключ или токен). В этом курсе мы рассматриваем следующие сервисы:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразными моделями, включая основную серию GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) — OpenAI-модели с акцентом на корпоративное использование
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) — открытые модели и серверы для инференса

**Для выполнения упражнений вам понадобятся собственные аккаунты в этих сервисах**. Задания необязательные, поэтому вы можете выбрать настройку одного, всех или ни одного из провайдеров — по своему желанию. Несколько советов по регистрации:

| Регистрация | Стоимость | API-ключ | Playground | Комментарии |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Тарифы](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [На основе проекта](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно несколько моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Тарифы](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Необходима предварительная заявка на доступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Тарифы](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [В Hugging Chat ограниченное количество моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Следуйте инструкциям ниже, чтобы _настроить_ этот репозиторий для работы с разными провайдерами. Задания, требующие определённого провайдера, будут содержать один из следующих тегов в названии файла:

- `aoai` — требуется Azure OpenAI endpoint и ключ
- `oai` — требуется OpenAI endpoint и ключ
- `hf` — требуется токен Hugging Face

Вы можете настроить один, ни один или все провайдеры. Соответствующие задания просто выдадут ошибку при отсутствии нужных учётных данных.

## Создание файла `.env`

Мы предполагаем, что вы уже ознакомились с инструкциями выше, зарегистрировались у нужного провайдера и получили необходимые данные для аутентификации (API_KEY или токен). В случае Azure OpenAI также предполагается, что у вас есть рабочий экземпляр Azure OpenAI Service (endpoint) с хотя бы одной развёрнутой GPT-моделью для генерации чата.

Далее нужно настроить **локальные переменные окружения** следующим образом:

1. В корневой папке найдите файл `.env.copy`, который должен содержать примерно следующее:

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

2. Скопируйте этот файл в `.env` с помощью команды ниже. Этот файл добавлен в _gitignore_, чтобы ваши секреты были в безопасности.

   ```bash
   cp .env.copy .env
   ```

3. Заполните значения (замените плейсхолдеры справа от `=`) как описано в следующем разделе.

4. (Опционально) Если вы используете GitHub Codespaces, можно сохранить переменные окружения как _секреты Codespaces_, связанные с этим репозиторием. В этом случае локальный файл .env создавать не нужно. **Однако обратите внимание, что этот вариант работает только при использовании GitHub Codespaces.** Если вы используете Docker Desktop, файл .env всё равно потребуется.

## Заполнение файла `.env`

Давайте быстро рассмотрим имена переменных, чтобы понять, что они означают:

| Переменная  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Токен доступа пользователя, который вы создаёте в своём профиле |
| OPENAI_API_KEY | Ключ авторизации для использования сервиса (не для Azure OpenAI) |
| AZURE_OPENAI_API_KEY | Ключ авторизации для использования этого сервиса |
| AZURE_OPENAI_ENDPOINT | Развёрнутый endpoint для ресурса Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Endpoint развёртывания модели _генерации текста_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Endpoint развёртывания модели _эмбеддингов текста_ |
| | |

Примечание: последние две переменные Azure OpenAI отражают модель по умолчанию для генерации чата (генерация текста) и поиска по векторам (эмбеддинги) соответственно. Инструкции по их настройке будут даны в соответствующих заданиях.

## Настройка Azure: через портал

Значения endpoint и ключа Azure OpenAI можно найти в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), поэтому начнём с этого.

1. Перейдите в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. В боковом меню выберите **Keys and Endpoint**.
1. Нажмите **Show Keys** — вы увидите: KEY 1, KEY 2 и Endpoint.
1. Для AZURE_OPENAI_API_KEY используйте значение KEY 1
1. Для AZURE_OPENAI_ENDPOINT используйте значение Endpoint

Далее нам понадобятся endpoints для конкретных моделей, которые вы развернули.

1. В боковом меню (слева) для ресурса Azure OpenAI выберите **Model deployments**.
1. На открывшейся странице нажмите **Manage Deployments**

Это приведёт вас на сайт Azure OpenAI Studio, где мы найдём остальные значения, как описано ниже.

## Настройка Azure: через Studio

1. Перейдите в [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **из вашего ресурса**, как описано выше.
1. В левой панели выберите вкладку **Deployments**, чтобы увидеть развернутые модели.
1. Если нужная модель не развернута, используйте **Create new deployment** для её развертывания.
1. Вам понадобится модель _генерации текста_ — рекомендуем: **gpt-35-turbo**
1. Вам понадобится модель _эмбеддингов текста_ — рекомендуем **text-embedding-ada-002**

Теперь обновите переменные окружения, указав _Deployment name_, который вы использовали. Обычно он совпадает с названием модели, если вы его явно не меняли. Например, у вас может быть:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забудьте сохранить файл .env после изменений**. Теперь вы можете закрыть файл и вернуться к инструкциям по запуску ноутбука.

## Настройка OpenAI: через профиль

Ваш OpenAI API-ключ можно найти в [аккаунте OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Если у вас его нет, зарегистрируйтесь и создайте API-ключ. После этого используйте его для заполнения переменной `OPENAI_API_KEY` в файле `.env`.

## Настройка Hugging Face: через профиль

Ваш токен Hugging Face находится в профиле в разделе [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикуйте и не делитесь этими токенами. Лучше создайте отдельный токен для этого проекта и скопируйте его в файл `.env` в переменную `HUGGING_FACE_API_KEY`. _Примечание:_ Технически это не API-ключ, но он используется для аутентификации, поэтому мы сохраняем такое название для единообразия.

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.