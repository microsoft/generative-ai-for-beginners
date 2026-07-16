[![Modelos Open Source](../../../translated_images/pt-BR/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introdução

Agentes de IA representam um desenvolvimento empolgante em IA Generativa, permitindo que Modelos de Linguagem de Grande Porte (LLMs) evoluam de assistentes para agentes capazes de tomar ações. Frameworks de agentes de IA permitem que desenvolvedores criem aplicações que dão aos LLMs acesso a ferramentas e gerenciamento de estado. Esses frameworks também melhoram a visibilidade, permitindo que usuários e desenvolvedores monitorem as ações planejadas pelos LLMs, aprimorando assim a gestão da experiência.

A lição cobrirá as seguintes áreas:

- Compreendendo o que é um Agente de IA - O que exatamente é um Agente de IA?
- Explorando cinco diferentes Frameworks de Agente de IA - O que os torna únicos?
- Aplicando esses Agentes de IA a diferentes casos de uso - Quando devemos usar Agentes de IA?

## Objetivos de aprendizagem

Após esta lição, você será capaz de:

- Explicar o que são Agentes de IA e como podem ser usados.
- Ter uma compreensão das diferenças entre alguns dos frameworks populares de Agentes de IA, e como eles diferem.
- Entender como Agentes de IA funcionam para construir aplicações com eles.

## O que são Agentes de IA?

Agentes de IA são um campo muito empolgante no mundo da IA Generativa. Com essa empolgação, por vezes surge confusão sobre os termos e suas aplicações. Para manter as coisas simples e inclusivas da maioria das ferramentas que se referem a Agentes de IA, usaremos esta definição:

Agentes de IA permitem que Modelos de Linguagem de Grande Porte (LLMs) realizem tarefas dando-lhes acesso a um **estado** e **ferramentas**.

![Modelo de Agente](../../../translated_images/pt-BR/what-agent.21f2893bdfd01e6a.webp)

Vamos definir esses termos:

**Modelos de Linguagem de Grande Porte** - São os modelos referidos ao longo deste curso, como GPT-3.5, GPT-4, Llama-2, etc.

**Estado** - Refere-se ao contexto no qual o LLM está trabalhando. O LLM usa o contexto de suas ações passadas e o contexto atual para guiar sua tomada de decisão nas ações subsequentes. Frameworks de Agentes de IA permitem que desenvolvedores mantenham esse contexto de forma mais fácil.

**Ferramentas** - Para completar a tarefa que o usuário solicitou e que o LLM planejou, o LLM precisa de acesso a ferramentas. Alguns exemplos de ferramentas são um banco de dados, uma API, um aplicativo externo ou até mesmo outro LLM!

Esperamos que essas definições lhe deem uma boa base para avançarmos enquanto exploramos como eles são implementados. Vamos explorar alguns frameworks diferentes de Agentes de IA:

## Agentes LangChain

[Agentes LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) é uma implementação das definições que fornecemos acima.

Para gerenciar o **estado** , ele usa uma função interna chamada `AgentExecutor`. Esta aceita o `agent` definido e as `tools` que estão disponíveis.

O `Agent Executor` também armazena o histórico de chat para fornecer o contexto da conversa.

![Langchain Agents](../../../translated_images/pt-BR/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferece um [catálogo de ferramentas](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) que podem ser importadas para sua aplicação e às quais o LLM pode acessar. Elas são feitas pela comunidade e pela equipe LangChain.

Você pode então definir essas ferramentas e passá-las para o `Agent Executor`.

A visibilidade é outro aspecto importante ao falar de Agentes de IA. É importante para os desenvolvedores de aplicações entenderem qual ferramenta o LLM está usando e por quê. Para isso, a equipe LangChain desenvolveu o LangSmith.

## AutoGen

O próximo framework de agente de IA que discutiremos é o [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). O foco principal do AutoGen são conversas. Agentes são tanto **conversáveis** quanto **personalizáveis**.

**Conversável -** LLMs podem iniciar e continuar uma conversa com outro LLM para completar uma tarefa. Isso é feito criando `AssistantAgents` e dando-lhes uma mensagem de sistema específica.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizável** - Agentes podem ser definidos não apenas como LLMs, mas também como usuário ou ferramenta. Como desenvolvedor, você pode definir um `UserProxyAgent` que é responsável por interagir com o usuário para obter feedback na execução de uma tarefa. Esse feedback pode continuar a execução da tarefa ou pará-la.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado e Ferramentas

Para mudar e gerenciar o estado, um Agente assistente gera código Python para completar a tarefa.

Aqui está um exemplo do processo:

![AutoGen](../../../translated_images/pt-BR/autogen.dee9a25a45fde584.webp)

#### LLM definido com uma Mensagem de Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Essa mensagem de sistema direciona esse LLM específico para as funções relevantes para sua tarefa. Lembre-se, com AutoGen você pode ter múltiplos AssistantAgents definidos com diferentes mensagens de sistema.

#### Chat iniciado pelo Usuário

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Essa mensagem do user_proxy (Humano) é o que iniciará o processo do Agente para explorar as possíveis funções que ele deve executar.

#### Função é executada

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Uma vez que o chat inicial é processado, o Agente enviará a ferramenta sugerida para chamada. Neste caso, é uma função chamada `get_weather`. Dependendo da sua configuração, essa função pode ser executada automaticamente e lida pelo Agente ou ser executada baseado na entrada do usuário.

Você pode encontrar uma lista de [exemplos de código AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) para explorar mais como começar a construir.

## Framework Microsoft Agent

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) é o SDK open-source da Microsoft para construir Agentes de IA e sistemas multi-agentes em **Python** e **.NET**. Ele reúne as forças de dois projetos anteriores da Microsoft — as funcionalidades corporativas do **Semantic Kernel** e a orquestração multi-agente do **AutoGen** — em um framework único e suportado. Se você está começando um novo projeto de agente hoje, este é o sucessor recomendado do AutoGen.

O framework escala desde um único **agente de chat** até workflows complexos de **multi-agente**, e se integra diretamente com Microsoft Foundry, Azure OpenAI e OpenAI. Ele também oferece observabilidade embutida via OpenTelemetry para que você possa rastrear exatamente o que seus agentes estão fazendo.

### Estado e Ferramentas

**Estado** - O framework gerencia o contexto da conversa para você através de **threads**. Um agente acompanha o histórico da mensagem (requisições do usuário, chamadas de ferramenta e seus resultados), para que cada passo construa sobre os anteriores. Threads também podem ser persistidas, permitindo que uma conversa seja pausada e retomada depois.

**Ferramentas** - Você dá ferramentas ao agente passando funções Python simples. Parâmetros anotados são automaticamente transformados em um esquema, para que o modelo saiba como e quando chamá-los (function calling). O framework também suporta servidores Model Context Protocol (MCP) e ferramentas hospedadas como um interpretador de código.

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

Para conectar ao Azure OpenAI no Microsoft Foundry em vez disso, passe seu endpoint e credenciais para o cliente:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Workflows multi-agente

Onde o framework realmente se destaca é na orquestração de vários agentes juntos. Por exemplo, você pode executar agentes em sequência (cada um passando seu contexto para o próximo) ou dispersar para vários agentes em paralelo e agregar seus resultados:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Execute agentes em sequência, passando o contexto da conversa ao longo da cadeia
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribua para agentes em paralelo e depois agregue suas respostas
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

O próximo framework de agente que vamos explorar é o [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ele é conhecido como um agente "code-first" porque em vez de trabalhar estritamente com `strings`, pode trabalhar com DataFrames em Python. Isso se torna extremamente útil para tarefas de análise e geração de dados. Podem ser coisas como criar gráficos e tabelas ou gerar números aleatórios.

### Estado e Ferramentas

Para gerenciar o estado da conversa, TaskWeaver usa o conceito de um `Planner`. O `Planner` é um LLM que recebe a requisição dos usuários e mapeia as tarefas que precisam ser completadas para cumprir essa solicitação.

Para completar as tarefas, o `Planner` é exposto a uma coleção de ferramentas chamadas `Plugins`. Estes podem ser classes Python ou um interpretador de código geral. Esses plugins são armazenados como embeddings para que o LLM possa buscar melhor o plugin correto.

![Taskweaver](../../../translated_images/pt-BR/taskweaver.da8559999267715a.webp)

Aqui está um exemplo de um plugin para lidar com detecção de anomalias:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

O código é verificado antes da execução. Outra funcionalidade para gerenciar o contexto no Taskweaver é a `experience`. Experiência permite que o contexto de uma conversa seja armazenado a longo prazo em um arquivo YAML. Isso pode ser configurado para que o LLM melhore ao longo do tempo em certas tarefas, dado que seja exposto a conversas anteriores.

## JARVIS

O último framework de agente que vamos explorar é o [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). O que torna o JARVIS único é que ele usa um LLM para gerenciar o `estado` da conversa e as `ferramentas` são outros modelos de IA. Cada um desses modelos de IA é especializado em certas tarefas como detecção de objetos, transcrição ou descrição de imagens.

![JARVIS](../../../translated_images/pt-BR/jarvis.762ddbadbd1a3a33.webp)

O LLM, sendo um modelo de propósito geral, recebe a solicitação do usuário e identifica a tarefa específica e quaisquer argumentos/dados que são necessários para completá-la.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

O LLM então formata a solicitação de uma forma que o modelo especializado de IA possa interpretar, como JSON. Depois que o modelo de IA retorna sua predição baseada na tarefa, o LLM recebe a resposta.

Se múltiplos modelos forem necessários para completar a tarefa, ele também interpretará as respostas desses modelos antes de juntá-las para gerar a resposta para o usuário.

O exemplo abaixo mostra como isso funcionaria quando um usuário solicita uma descrição e contagem dos objetos em uma imagem:

## Tarefa

Para continuar seu aprendizado sobre Agentes de IA, você pode construir com o Microsoft Agent Framework:

- Uma aplicação que simule uma reunião de negócios com diferentes departamentos de uma startup educacional.
- Criar mensagens de sistema que guiem os LLMs a entender diferentes personas e prioridades, e permita que o usuário apresente uma nova ideia de produto.
- O LLM deve então gerar perguntas de acompanhamento de cada departamento para refinar e melhorar a apresentação e a ideia do produto.

## O aprendizado não para aqui, continue a jornada

Após completar esta lição, confira nossa [coleção de Aprendizagem em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar elevando seu conhecimento em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->