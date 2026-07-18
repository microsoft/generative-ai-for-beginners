[![Modelos Open Source](../../../translated_images/pt-BR/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introdução

Agentes de IA representam um desenvolvimento empolgante em IA Generativa, permitindo que Grandes Modelos de Linguagem (LLMs) evoluam de assistentes para agentes capazes de tomar ações. Frameworks de Agentes de IA permitem que desenvolvedores criem aplicações que dão aos LLMs acesso a ferramentas e gerenciamento de estado. Esses frameworks também aumentam a visibilidade, permitindo que usuários e desenvolvedores monitorem as ações planejadas pelos LLMs, melhorando assim o gerenciamento da experiência.

A lição abordará as seguintes áreas:

- Compreender o que é um Agente de IA - O que exatamente é um Agente de IA?
- Explorar cinco diferentes Frameworks de Agentes de IA - O que os torna únicos?
- Aplicar esses Agentes de IA a diferentes casos de uso - Quando devemos usar Agentes de IA?

## Objetivos de aprendizado

Após esta lição, você será capaz de:

- Explicar o que são Agentes de IA e como eles podem ser usados.
- Compreender as diferenças entre alguns dos frameworks populares de Agentes de IA, e como eles se diferenciam.
- Entender como Agentes de IA funcionam para construir aplicações com eles.

## O que são Agentes de IA?

Agentes de IA são um campo muito empolgante no mundo da IA Generativa. Com essa empolgação, às vezes surge confusão em relação aos termos e sua aplicação. Para manter as coisas simples e inclusivas à maioria das ferramentas que se referem a Agentes de IA, vamos usar esta definição:

Agentes de IA permitem que Grandes Modelos de Linguagem (LLMs) executem tarefas dando-lhes acesso a um **estado** e **ferramentas**.

![Modelo do Agente](../../../translated_images/pt-BR/what-agent.21f2893bdfd01e6a.webp)

Vamos definir esses termos:

**Grandes Modelos de Linguagem** - São os modelos referidos ao longo deste curso como GPT-5, GPT-4o, e Llama 3.3, etc.

**Estado** - Refere-se ao contexto em que o LLM está operando. O LLM usa o contexto de suas ações passadas e o contexto atual para orientar sua tomada de decisões para as ações subsequentes. Frameworks de Agentes de IA permitem que desenvolvedores mantenham esse contexto com mais facilidade.

**Ferramentas** - Para completar a tarefa solicitada pelo usuário e que o LLM planejou, o LLM precisa de acesso a ferramentas. Alguns exemplos de ferramentas podem ser um banco de dados, uma API, um aplicativo externo ou até outro LLM!

Essas definições devem fornecer uma boa base para seguirmos adiante enquanto olhamos como elas são implementadas. Vamos explorar alguns frameworks diferentes de Agentes de IA:

## Agentes LangChain

[Agentes LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) é uma implementação das definições que fornecemos acima.

Para gerenciar o **estado**, ele usa uma função embutida chamada `AgentExecutor`. Essa aceita o `agent` definido e as `tools` disponíveis para ele.

O `AgentExecutor` também armazena o histórico do chat para fornecer o contexto da conversa.

![Agentes LangChain](../../../translated_images/pt-BR/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferece um [catálogo de ferramentas](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) que podem ser importadas para sua aplicação e às quais o LLM pode obter acesso. Essas ferramentas são feitas pela comunidade e pela equipe LangChain.

Você pode então definir essas ferramentas e passá-las para o `AgentExecutor`.

Visibilidade é outro aspecto importante ao falar de Agentes de IA. É importante para desenvolvedores de aplicações entender qual ferramenta o LLM está utilizando e por quê. Para isso, a equipe do LangChain desenvolveu o LangSmith.

## AutoGen

O próximo framework de Agente de IA que discutiremos é o [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). O foco principal do AutoGen são conversas. Agentes são tanto **conversáveis** quanto **personalizáveis**.

**Conversável -** LLMs podem iniciar e continuar uma conversa com outro LLM para completar uma tarefa. Isso é feito criando `AssistantAgents` e dando a eles uma mensagem de sistema específica.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizável** - Agentes podem ser definidos não só como LLMs, mas também como um usuário ou uma ferramenta. Como desenvolvedor, você pode definir um `UserProxyAgent` responsável por interagir com o usuário para feedback na conclusão de uma tarefa. Esse feedback pode continuar a execução da tarefa ou paralisá-la.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado e Ferramentas

Para alterar e gerenciar estado, um Agente assistente gera código Python para completar a tarefa.

Aqui está um exemplo do processo:

![AutoGen](../../../translated_images/pt-BR/autogen.dee9a25a45fde584.webp)

#### LLM definido com uma mensagem de sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Essa mensagem de sistema direciona esse LLM específico para quais funções são relevantes para sua tarefa. Lembre-se, com AutoGen você pode ter múltiplos AssistantAgents definidos com mensagens de sistema diferentes.

#### Chat iniciado pelo usuário

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Essa mensagem do user_proxy (Humano) é o que iniciará o processo do Agente para explorar as funções possíveis que ele deve executar.

#### Função executada

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Após o processamento inicial do chat, o Agente vai enviar a ferramenta sugerida para chamada. Neste caso, é uma função chamada `get_weather`. Dependendo da sua configuração, essa função pode ser executada automaticamente e lida pelo Agente, ou pode ser executada com base na entrada do usuário.

Você pode encontrar uma lista de [amostras de código AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) para explorar melhor como começar a construir.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) é o SDK open source da Microsoft para construir Agentes de IA e sistemas multi-agentes tanto em **Python** quanto em **.NET**. Ele reúne as forças de dois projetos anteriores da Microsoft — os recursos empresariais do **Semantic Kernel** e a orquestração multi-agente do **AutoGen** — em um único framework suportado. Se você está começando um novo projeto de agente hoje, esta é a sucessora recomendada do AutoGen.

O framework escala desde um único **agente de chat** até fluxos de trabalho **multi-agente** complexos, e integra-se diretamente com Microsoft Foundry, Azure OpenAI e OpenAI. Ele também fornece observabilidade incorporada via OpenTelemetry para que você possa rastrear exatamente o que seus agentes estão fazendo.

### Estado e Ferramentas

**Estado** - O framework gerencia o contexto da conversa para você através de **threads**. Um agente mantém o histórico da mensagem (requisições do usuário, chamadas de ferramenta, e seus resultados), assim cada rodada se baseia nas anteriores. Threads também podem ser persistidos, permitindo que uma conversa seja pausada e retomada depois.

**Ferramentas** - Você fornece ferramentas a um agente passando funções Python simples. Parâmetros com anotações de tipo são automaticamente convertidos em um esquema, para que o modelo saiba como e quando chamá-las (chamada de função). O framework também suporta servidores do Model Context Protocol (MCP) e ferramentas hospedadas como um interpretador de código.

Aqui está um exemplo de um agente único com uma ferramenta personalizada:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Para conectar-se ao Azure OpenAI no Microsoft Foundry em vez disso, passe seu endpoint e credenciais para o cliente:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Fluxos de trabalho multi-agente

Onde o framework realmente se destaca é ao orquestrar vários agentes juntos. Por exemplo, você pode executar agentes um após o outro (cada um passando seu contexto para o próximo) ou disparar vários agentes em paralelo e agregar seus resultados:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Execute agentes em sequência, passando o contexto da conversa ao longo da cadeia
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribua para agentes em paralelo, então agregue suas respostas
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Para instalar o framework e começar:

```bash
pip install agent-framework-core
# Integrações opcionais
pip install agent-framework-openai       # OpenAI e Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Você pode explorar mais no [repositório Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) e na [documentação oficial](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

O próximo framework de agente que vamos explorar é o [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ele é conhecido como um agente "code-first" porque, em vez de trabalhar estritamente com `strings`, pode trabalhar com DataFrames em Python. Isso se torna extremamente útil para tarefas de análise e geração de dados. Isso pode ser coisas como criar gráficos e diagramas ou gerar números aleatórios.

### Estado e Ferramentas

Para gerenciar o estado da conversa, o TaskWeaver usa o conceito de um `Planner`. O `Planner` é um LLM que recebe a solicitação dos usuários e mapeia as tarefas que precisam ser concluídas para atender essa solicitação.

Para completar as tarefas, o `Planner` tem acesso à coleção de ferramentas chamadas `Plugins`. Estes podem ser classes Python ou um interpretador geral de código. Esses plugins são armazenados como embeddings para que o LLM possa buscar melhor o plugin correto.

![Taskweaver](../../../translated_images/pt-BR/taskweaver.da8559999267715a.webp)

Aqui está um exemplo de um plugin para lidar com detecção de anomalias:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

O código é verificado antes de ser executado. Outra funcionalidade para gerenciar contexto no Taskweaver é a `experience`. Experience permite que o contexto de uma conversa seja armazenado a longo prazo em um arquivo YAML. Isso pode ser configurado para que o LLM melhore com o tempo em certas tarefas, desde que seja exposto a conversas anteriores.

## JARVIS

O último framework de agente que vamos explorar é o [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). O que torna o JARVIS único é que ele usa um LLM para gerenciar o `estado` da conversa e as `ferramentas` são outros modelos de IA. Cada um dos modelos de IA são modelos especializados que realizam tarefas específicas, como detecção de objetos, transcrição ou legenda de imagens.

![JARVIS](../../../translated_images/pt-BR/jarvis.762ddbadbd1a3a33.webp)

O LLM, sendo um modelo de propósito geral, recebe a solicitação do usuário e identifica a tarefa específica e quaisquer argumentos/dados necessários para completar a tarefa.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

O LLM então formata a solicitação de maneira que o modelo de IA especializado possa interpretar, como JSON. Uma vez que o modelo de IA retorna sua predição baseada na tarefa, o LLM recebe a resposta.

Se múltiplos modelos forem necessários para completar a tarefa, ele também interpretará as respostas desses modelos antes de juntá-las para gerar a resposta para o usuário.

O exemplo abaixo mostra como isso funcionaria quando um usuário está solicitando uma descrição e contagem dos objetos em uma imagem:

## Tarefa

Para continuar seu aprendizado sobre Agentes de IA, você pode construir com o Microsoft Agent Framework:

- Uma aplicação que simule uma reunião de negócios com diferentes departamentos de uma startup de educação.
- Criar mensagens de sistema que guiem os LLMs a entender diferentes personas e prioridades, e permitam que o usuário apresente uma nova ideia de produto.
- O LLM deve então gerar perguntas de seguimento de cada departamento para refinar e melhorar a apresentação e a ideia de produto.

## O aprendizado não para aqui, continue a jornada

Após completar esta lição, confira nossa [coleção de aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->