<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:21:48+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ru"
}
-->
# Настройка вашей среды разработки

В этом репозитории и курсе используется [контейнер для разработки](https://containers.dev?WT.mc_id=academic-105485-koreyst) с универсальной средой выполнения, поддерживающей Python3, .NET, Node.js и Java. Соответствующая конфигурация описана в файле `devcontainer.json`, который находится в папке `.devcontainer/` в корне репозитория.

Чтобы запустить контейнер для разработки, откройте его в [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (облачная среда) или в [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (локальная среда). Подробнее о работе с контейнерами для разработки в VS Code читайте в [этой документации](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).  

> [!TIP]  
> Рекомендуем использовать GitHub Codespaces для быстрого старта с минимальными усилиями. Для личных аккаунтов предоставляется щедрая [бесплатная квота](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst). Настройте [тайм-ауты](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), чтобы останавливать или удалять неактивные codespaces и максимально эффективно использовать квоту.

## 1. Выполнение заданий

В каждом уроке могут быть _необязательные_ задания, которые предоставляются на одном или нескольких языках программирования: Python, .NET/C#, Java и JavaScript/TypeScript. В этом разделе приведены общие рекомендации по выполнению таких заданий.

### 1.1 Задания на Python

Задания на Python представлены либо в виде приложений (`.py` файлы), либо Jupyter ноутбуков (`.ipynb` файлы).  
- Чтобы запустить ноутбук, откройте его в Visual Studio Code, затем нажмите _Select Kernel_ (в правом верхнем углу) и выберите стандартный вариант Python 3. После этого можно использовать команду _Run All_ для выполнения всего ноутбука.  
- Для запуска Python-приложений из командной строки следуйте инструкциям, указанным в конкретном задании, чтобы выбрать правильные файлы и передать необходимые аргументы.

## 2. Настройка провайдеров

Задания **могут** быть настроены для работы с одним или несколькими развертываниями больших языковых моделей (LLM) через поддерживаемых провайдеров, таких как OpenAI, Azure или Hugging Face. Они предоставляют _хостинг-эндпоинт_ (API), к которому можно обращаться программно с помощью правильных учетных данных (API ключ или токен). В этом курсе рассматриваются следующие провайдеры:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразными моделями, включая основную серию GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) — OpenAI модели с акцентом на корпоративное использование.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) — открытые модели и серверы инференса.

**Для выполнения этих упражнений вам понадобятся собственные аккаунты**. Задания необязательны, поэтому вы можете настроить одного, всех или ни одного из провайдеров в зависимости от интересов. Вот краткая информация по регистрации:

| Регистрация | Стоимость | API ключ | Песочница | Комментарии |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Цены](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Проектные ключи](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Веб-песочница без кода](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно множество моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Цены](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [Быстрый старт SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Быстрый старт Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Необходимо предварительно подать заявку на доступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цены](https://huggingface.co/pricing) | [Токены доступа](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat поддерживает ограниченный набор моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Следуйте инструкциям ниже, чтобы _настроить_ этот репозиторий для работы с разными провайдерами. Задания, требующие конкретного провайдера, будут содержать один из следующих тегов в имени файла:
 - `aoai` — требует Azure OpenAI endpoint и ключ
 - `oai` — требует OpenAI endpoint и ключ
 - `hf` — требует токен Hugging Face

Вы можете настроить одного, нескольких или ни одного провайдера. Если учетные данные отсутствуют, соответствующие задания просто выдадут ошибку.

### 2.1. Создание файла `.env`

Предполагается, что вы уже ознакомились с инструкциями выше, зарегистрировались у нужного провайдера и получили необходимые учетные данные (API_KEY или токен). В случае Azure OpenAI предполагается, что у вас есть действующее развертывание Azure OpenAI Service (endpoint) с хотя бы одной моделью GPT, развернутой для чат-комплешена.

Следующий шаг — настроить **локальные переменные окружения** следующим образом:

1. Найдите в корневой папке файл `.env.copy`, который должен содержать примерно следующее:

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

2. Скопируйте этот файл в `.env` с помощью команды ниже. Этот файл добавлен в .gitignore, чтобы сохранить секреты в безопасности.

   ```bash
   cp .env.copy .env
   ```

3. Заполните значения (замените плейсхолдеры справа от `=`) согласно описанию в следующем разделе.

3. (Опционально) Если вы используете GitHub Codespaces, можно сохранить переменные окружения как _секреты Codespaces_, связанные с этим репозиторием. В этом случае локальный файл .env создавать не нужно. **Однако учтите, что этот способ работает только с GitHub Codespaces.** Если вы используете Docker Desktop, файл .env нужно настроить обязательно.

### 2.2. Заполнение файла `.env`

Давайте кратко рассмотрим имена переменных и их назначение:

| Переменная  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Токен доступа пользователя, который вы создаете в своем профиле |
| OPENAI_API_KEY | Ключ авторизации для использования сервиса OpenAI (не Azure) |
| AZURE_OPENAI_API_KEY | Ключ авторизации для Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | URL развернутого эндпоинта Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Имя развертывания модели для _генерации текста_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Имя развертывания модели для _векторных эмбеддингов_ |
| | |

Примечание: последние две переменные Azure OpenAI соответствуют моделям по умолчанию для чат-комплешена (генерация текста) и поиска по векторным представлениям (эмбеддинги). Инструкции по их настройке будут указаны в соответствующих заданиях.

### 2.3 Настройка Azure: через портал

Значения для Azure OpenAI endpoint и ключа можно найти в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), начнем с него.

1. Перейдите в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. В боковом меню выберите пункт **Keys and Endpoint**  
3. Нажмите **Show Keys** — вы увидите KEY 1, KEY 2 и Endpoint  
4. Используйте значение KEY 1 для AZURE_OPENAI_API_KEY  
5. Используйте значение Endpoint для AZURE_OPENAI_ENDPOINT  

Далее нам нужны эндпоинты для конкретных развернутых моделей.

1. В боковом меню выберите **Model deployments** для ресурса Azure OpenAI  
2. На открывшейся странице нажмите **Manage Deployments**

Это перенаправит вас на сайт Azure OpenAI Studio, где можно найти остальные значения, как описано ниже.

### 2.4 Настройка Azure: через Studio

1. Перейдите в [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **через ваш ресурс**, как описано выше.  
2. Выберите вкладку **Deployments** (в боковом меню слева), чтобы увидеть текущие развернутые модели.  
3. Если нужная модель не развернута, используйте **Create new deployment** для ее создания.  
4. Вам понадобится модель для _генерации текста_ — рекомендуем: **gpt-35-turbo**  
5. Вам понадобится модель для _векторных эмбеддингов_ — рекомендуем: **text-embedding-ada-002**

Теперь обновите переменные окружения, указав имя _Deployment name_, которое вы использовали. Обычно оно совпадает с именем модели, если вы не меняли его явно. Например, у вас может быть:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забудьте сохранить файл .env после изменений**. Теперь можно закрыть файл и вернуться к инструкциям по запуску ноутбука.

### 2.5 Настройка OpenAI: через профиль

Ваш OpenAI API ключ можно найти в вашем [аккаунте OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Если у вас его нет, зарегистрируйтесь и создайте ключ API. После этого заполните переменную `OPENAI_API_KEY` в файле `.env`.

### 2.6 Настройка Hugging Face: через профиль

Ваш токен Hugging Face можно найти в профиле в разделе [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикуйте и не делитесь им публично. Лучше создайте новый токен специально для этого проекта и вставьте его в файл `.env` в переменную `HUGGING_FACE_API_KEY`. _Примечание:_ технически это не API ключ, но используется для аутентификации, поэтому для удобства мы сохраняем такое название.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.