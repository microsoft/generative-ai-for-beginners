<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11f03c81f190d9cbafd0f977dcbede6c",
  "translation_date": "2025-05-20T07:07:57+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "ru"
}
-->
[![Open Source Models](../../../translated_images/17-lesson-banner.85938ffe06e157e1dfc9ae2fcf0de326892e71c463f62b397291ad54bd8e9602.ru.png)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Введение

AI-агенты представляют собой захватывающее развитие в области генеративного ИИ, позволяя большим языковым моделям (LLM) эволюционировать от помощников до агентов, способных принимать действия. Фреймворки AI-агентов позволяют разработчикам создавать приложения, которые дают LLM доступ к инструментам и управлению состоянием. Эти фреймворки также повышают видимость, позволяя пользователям и разработчикам отслеживать действия, запланированные LLM, тем самым улучшая управление опытом.

В уроке будут рассмотрены следующие области:

- Понимание того, что такое AI-агент - Что именно такое AI-агент?
- Изучение четырех различных фреймворков AI-агентов - Чем они уникальны?
- Применение этих AI-агентов к различным случаям использования - Когда следует использовать AI-агентов?

## Цели обучения

После прохождения этого урока вы сможете:

- Объяснить, что такое AI-агенты и как их можно использовать.
- Понять различия между некоторыми популярными фреймворками AI-агентов и чем они отличаются.
- Понять, как функционируют AI-агенты для создания приложений с их использованием.

## Что такое AI-агенты?

AI-агенты - это очень захватывающее направление в мире генеративного ИИ. Вместе с этим волнением иногда возникает путаница в терминах и их применении. Чтобы сделать все просто и охватить большинство инструментов, которые относятся к AI-агентам, мы будем использовать следующее определение:

AI-агенты позволяют большим языковым моделям (LLM) выполнять задачи, предоставляя им доступ к **состоянию** и **инструментам**.

![Agent Model](../../../translated_images/what-agent.61a7315e4b722e06561f6c93e682a51357308b53884f00af289b5a81e3e65242.ru.png)

Давайте определим эти термины:

**Большие языковые модели** - Это модели, упоминаемые на протяжении всего курса, такие как GPT-3.5, GPT-4, Llama-2 и др.

**Состояние** - Это относится к контексту, в котором работает LLM. LLM использует контекст своих прошлых действий и текущий контекст, направляя свое принятие решений для последующих действий. Фреймворки AI-агентов позволяют разработчикам легче поддерживать этот контекст.

**Инструменты** - Для выполнения задачи, которую запросил пользователь и которую спланировал LLM, LLM необходим доступ к инструментам. Примеры инструментов могут включать базу данных, API, внешнее приложение или даже другой LLM!

Эти определения, надеюсь, дадут вам хорошую основу для дальнейшего изучения, как они реализованы. Давайте рассмотрим несколько различных фреймворков AI-агентов:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) - это реализация определений, которые мы привели выше.

Для управления **состоянием** он использует встроенную функцию, называемую `AgentExecutor`. Эта функция принимает определенные `agent` и `tools`, которые доступны.

`Agent Executor` также хранит историю чата, чтобы обеспечить контекст чата.

![Langchain Agents](../../../translated_images/langchain-agents.4709b559c14be8903a59abf4ebef43916a23fac43924b133a7552121ff5e6730.ru.png)

LangChain предлагает [каталог инструментов](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), которые могут быть импортированы в ваше приложение, к которому LLM может получить доступ. Они созданы сообществом и командой LangChain.

Вы можете определить эти инструменты и передать их `Agent Executor`.

Видимость - еще один важный аспект при обсуждении AI-агентов. Важно, чтобы разработчики приложений понимали, какой инструмент использует LLM и почему. Для этого команда LangChain разработала LangSmith.

## AutoGen

Следующий фреймворк AI-агентов, который мы обсудим, - это [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Основное внимание AutoGen уделяется разговорам. Агенты являются как **разговорными**, так и **настраиваемыми**.

**Разговорные -** LLM могут начать и продолжить разговор с другим LLM для выполнения задачи. Это достигается созданием `AssistantAgents` и предоставлением им определенного системного сообщения.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Настраиваемые** - Агенты могут быть определены не только как LLM, но и как пользователь или инструмент. Как разработчик, вы можете определить `UserProxyAgent`, который отвечает за взаимодействие с пользователем для получения обратной связи при выполнении задачи. Эта обратная связь может либо продолжить выполнение задачи, либо остановить его.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Состояние и инструменты

Чтобы изменить и управлять состоянием, помощник-агент генерирует код на Python для выполнения задачи.

Вот пример процесса:

![AutoGen](../../../translated_images/autogen.8ac57409019150ec5a17c6381a92863116b19acce02604b4bf5681225dee62eb.ru.png)

#### LLM, определенный системным сообщением

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Это системное сообщение направляет конкретный LLM на функции, которые относятся к его задаче. Помните, с AutoGen вы можете иметь несколько определенных AssistantAgents с различными системными сообщениями.

#### Чат инициируется пользователем

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Это сообщение от user_proxy (человека) запускает процесс агента для исследования возможных функций, которые он должен выполнить.

#### Функция выполняется

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

После обработки начального чата агент отправит предложенный инструмент для вызова. В данном случае это функция `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`. Это могут быть классы на Python или общий интерпретатор кода. Эти плагины хранятся как эмбеддинги, чтобы LLM мог лучше искать правильный плагин.

![Taskweaver](../../../translated_images/taskweaver.c0997002a3df51572f6cad019c41202b7c2110cbfcccc4af2e5d6a0ace4b4545.ru.png)

Вот пример плагина для обработки обнаружения аномалий:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Код проверяется перед выполнением. Еще одной функцией для управления контекстом в Taskweaver является `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` разговора, и `tools` являются другими моделями ИИ. Каждая из моделей ИИ - это специализированные модели, выполняющие определенные задачи, такие как обнаружение объектов, транскрипция или описание изображений.

![JARVIS](../../../translated_images/jarvis.d41d7c4c81bf015bd7ced7f1108abdec56b312472aaf3f63b5b0e82a5f4fb395.ru.png)

LLM, будучи моделью общего назначения, получает запрос от пользователя и идентифицирует конкретную задачу и любые аргументы/данные, необходимые для выполнения задачи.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Затем LLM форматирует запрос таким образом, чтобы специализированная модель ИИ могла его интерпретировать, например, в формате JSON. После того, как модель ИИ вернула свой прогноз на основе задачи, LLM получает ответ.

Если для выполнения задачи требуется несколько моделей, он также интерпретирует ответ от этих моделей, прежде чем объединить их для генерации ответа пользователю.

Пример ниже показывает, как это будет работать, когда пользователь запрашивает описание и количество объектов на картинке:

## Задание

Чтобы продолжить изучение AI-агентов, вы можете создать приложение с AutoGen:

- Приложение, имитирующее деловую встречу с различными отделами стартапа в сфере образования.
- Создайте системные сообщения, которые направляют LLM в понимании различных персон и приоритетов и позволяют пользователю предложить новую идею продукта.
- LLM должен затем генерировать дополнительные вопросы от каждого отдела для уточнения и улучшения предложения и идеи продукта.

## Обучение не заканчивается здесь, продолжайте путешествие

После завершения этого урока ознакомьтесь с нашей [коллекцией обучения генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышение уровня ваших знаний о генеративном ИИ!

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Мы стремимся к точности, однако, пожалуйста, имейте в виду, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие в результате использования этого перевода.