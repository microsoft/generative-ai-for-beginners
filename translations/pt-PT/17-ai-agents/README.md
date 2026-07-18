[![Modelos Open Source](../../../translated_images/pt-PT/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introdução

Agentes de IA representam um desenvolvimento entusiasmante na IA Generativa, permitindo que os Grandes Modelos de Linguagem (LLMs) evoluam de assistentes para agentes capazes de tomar ações. Os frameworks de agentes de IA permitem aos programadores criar aplicações que dão aos LLMs acesso a ferramentas e gestão de estado. Estes frameworks também aumentam a visibilidade, permitindo aos utilizadores e programadores monitorizar as ações planeadas pelos LLMs, melhorando assim a gestão da experiência.

A lição irá abranger as seguintes áreas:

- Compreender o que é um Agente de IA - O que é exatamente um Agente de IA?
- Explorar cinco diferentes frameworks de Agentes de IA - O que os torna únicos?
- Aplicar estes Agentes de IA a diferentes casos de uso - Quando devemos usar Agentes de IA?

## Objetivos de aprendizagem

Após esta lição, será capaz de:

- Explicar o que são Agentes de IA e como podem ser usados.
- Ter uma compreensão das diferenças entre alguns dos frameworks populares de Agentes de IA e como se distinguem.
- Entender como funcionam os Agentes de IA para construir aplicações com eles.

## O Que São Agentes de IA?

Agentes de IA são um campo muito entusiasmante no mundo da IA Generativa. Com esta excitação surge às vezes uma confusão de termos e suas aplicações. Para manter as coisas simples e inclusivas para a maioria das ferramentas que se referem a Agentes de IA, vamos usar esta definição:

Agentes de IA permitem que os Grandes Modelos de Linguagem (LLMs) realizem tarefas dando-lhes acesso a um **estado** e a **ferramentas**.

![Modelo de Agente](../../../translated_images/pt-PT/what-agent.21f2893bdfd01e6a.webp)

Vamos definir estes termos:

**Grandes Modelos de Linguagem** - Estes são os modelos referidos ao longo deste curso como GPT-5, GPT-4o, Llama 3.3, etc.

**Estado** - Refere-se ao contexto em que o LLM está a trabalhar. O LLM usa o contexto das suas ações passadas e o contexto atual, guiando a sua tomada de decisões para ações subsequentes. Frameworks de Agentes de IA permitem aos programadores manter este contexto mais facilmente.

**Ferramentas** - Para completar a tarefa que o utilizador solicitou e que o LLM planeou, o LLM precisa ter acesso a ferramentas. Alguns exemplos de ferramentas podem ser uma base de dados, uma API, uma aplicação externa ou até outro LLM!

Estas definições, esperamos, dar-lhe-ão uma boa base para avançar enquanto exploramos como são implementados. Vamos explorar alguns diferentes frameworks de Agentes de IA:

## Agentes LangChain

[Agentes LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) é uma implementação das definições fornecidas acima.

Para gerir o **estado**, usa uma função incorporada chamada `AgentExecutor`. Esta aceita o `agent` definido e as `tools` disponíveis para ele.

O `Agent Executor` também armazena o histórico do chat para fornecer o contexto da conversa.

![Agentes Langchain](../../../translated_images/pt-PT/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferece um [catálogo de ferramentas](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) que podem ser importadas para a sua aplicação e às quais o LLM pode aceder. Estas são feitas pela comunidade e pela equipa LangChain.

Pode depois definir estas ferramentas e passá-las ao `Agent Executor`.

A visibilidade é outro aspeto importante ao falar de Agentes de IA. É importante para os programadores entenderem qual ferramenta o LLM está a usar e porquê. Para isso, a equipa da LangChain desenvolveu o LangSmith.

## AutoGen

O próximo framework de Agente de IA que vamos discutir é [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). O foco principal do AutoGen são as conversas. Os agentes são tanto **conversáveis** como **personalizáveis**.

**Conversável -** LLMs podem iniciar e continuar uma conversa com outro LLM para completar uma tarefa. Isto é feito criando `AssistantAgents` e dando-lhes uma mensagem de sistema específica.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizável** - Os agentes podem ser definidos não só como LLMs, mas também como um utilizador ou uma ferramenta. Como programador, pode definir um `UserProxyAgent` que é responsável por interagir com o utilizador para obter feedback na realização de uma tarefa. Este feedback pode continuar ou parar a execução da tarefa.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado e Ferramentas

Para alterar e gerir o estado, um agente assistente gera código Python para completar a tarefa.

Aqui está um exemplo do processo:

![AutoGen](../../../translated_images/pt-PT/autogen.dee9a25a45fde584.webp)

#### LLM Definido com uma Mensagem de Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Esta mensagem do sistema direciona este LLM específico para quais funções são relevantes para a sua tarefa. Lembre-se, com o AutoGen pode ter vários AssistantAgents definidos com diferentes mensagens de sistema.

#### Chat Iniciado pelo Utilizador

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Esta mensagem do user_proxy (Humano) é o que inicia o processo para o agente explorar as possíveis funções que deve executar.

#### Função é Executada

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Uma vez processada a conversa inicial, o agente vai enviar a ferramenta sugerida para chamada. Neste caso, é uma função chamada `get_weather`. Dependendo da sua configuração, esta função pode ser executada automaticamente e lida pelo agente ou executada com base na entrada do utilizador.

Pode encontrar uma lista de [exemplos de código AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) para explorar melhor como começar a construir.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) é o SDK open-source da Microsoft para construir agentes de IA e sistemas multi-agentes em **Python** e **.NET**. Reúne as forças de dois projetos anteriores da Microsoft — as funcionalidades empresariais do **Semantic Kernel** e a orquestração multi-agente do **AutoGen** — num único framework suportado. Se está a iniciar hoje um novo projeto de agente, este é o sucessor recomendado do AutoGen.

O framework escala desde um único **agente de chat** até fluxos de trabalho complexos de **multi-agentes**, integrando-se diretamente com Microsoft Foundry, Azure OpenAI, e OpenAI. Também fornece observabilidade incorporada via OpenTelemetry para poder rastrear exatamente o que os seus agentes estão a fazer.

### Estado e Ferramentas

**Estado** - O framework gere o contexto da conversa por si através de **threads**. Um agente mantém o histórico de mensagens (pedidos de utilizadores, chamadas de ferramentas e seus resultados), para que cada turno se baseie nos anteriores. As threads podem também ser persistidas, permitindo que uma conversa seja pausada e retomada mais tarde.

**Ferramentas** - Dá ferramentas a um agente passando funções Python simples. Parâmetros anotados com tipo são automaticamente convertidos num esquema, para que o modelo saiba como e quando as chamar (function calling). O framework também suporta servidores do Modelo Context Protocol (MCP) e ferramentas hospedadas como um interpretador de código.

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

Para conectar ao Azure OpenAI no Microsoft Foundry, em vez disso, passe o seu endpoint e credenciais ao cliente:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Fluxos de trabalho multi-agentes

Onde o framework realmente se destaca é orquestrar vários agentes juntos. Por exemplo, pode executar agentes um após outro (cada um passando o seu contexto para o seguinte) ou dividir vários agentes em paralelo e agregar os seus resultados:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Executar agentes em sequência, passando o contexto da conversa ao longo da cadeia
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribuir para agentes em paralelo, depois agregar as suas respostas
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Para instalar o framework e começar:

```bash
pip install agent-framework-core
# Integrações opcionais
pip install agent-framework-openai       # OpenAI e Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Pode explorar mais no [repositório Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) e na [documentação oficial](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

O próximo framework de agente que vamos explorar é o [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). É conhecido como um agente "code-first" porque, em vez de trabalhar estritamente com `strings`, pode trabalhar com DataFrames em Python. Isto torna-se extremamente útil para tarefas de análise e geração de dados. Podem ser coisas como criar gráficos e diagramas ou gerar números aleatórios.

### Estado e Ferramentas

Para gerir o estado da conversa, o TaskWeaver usa o conceito de um `Planner`. O `Planner` é um LLM que recebe o pedido dos utilizadores e traça as tarefas que precisam ser completadas para satisfazer esse pedido.

Para completar as tarefas, o `Planner` está exposto a uma coleção de ferramentas chamadas `Plugins`. Podem ser classes Python ou um interpretador de código geral. Estes plugins são armazenados como embeddings para que o LLM possa melhor procurar o plugin correto.

![Taskweaver](../../../translated_images/pt-PT/taskweaver.da8559999267715a.webp)

Aqui está um exemplo de um plugin para lidar com deteção de anomalias:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

O código é verificado antes de ser executado. Outra funcionalidade para gerir contexto no Taskweaver é a `experience`. A experiência permite que o contexto de uma conversa seja armazenado a longo prazo num ficheiro YAML. Isto pode ser configurado para que o LLM melhore ao longo do tempo em certas tarefas, dado que é exposto a conversas anteriores.

## JARVIS

O último framework de agente que vamos explorar é o [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). O que torna o JARVIS único é que ele usa um LLM para gerir o `estado` da conversa e as `ferramentas` são outros modelos de IA. Cada um dos modelos de IA é especializado para realizar determinadas tarefas, como deteção de objetos, transcrição ou legendagem de imagens.

![JARVIS](../../../translated_images/pt-PT/jarvis.762ddbadbd1a3a33.webp)

O LLM, sendo um modelo de uso geral, recebe o pedido do utilizador e identifica a tarefa específica e quaisquer argumentos/dados necessários para completar a tarefa.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

O LLM então formata o pedido de uma forma que o modelo de IA especializado possa interpretar, como JSON. Depois de o modelo de IA retornar a sua predição baseada na tarefa, o LLM recebe a resposta.

Se forem necessários múltiplos modelos para completar a tarefa, também irá interpretar a resposta desses modelos antes de os juntar para gerar a resposta ao utilizador.

O exemplo abaixo mostra como isto funcionaria quando um utilizador pede uma descrição e contagem de objetos numa imagem:

## Exercício

Para continuar a sua aprendizagem sobre Agentes de IA pode construir com o Microsoft Agent Framework:

- Uma aplicação que simule uma reunião de negócios com diferentes departamentos de uma startup de educação.
- Criar mensagens de sistema que orientem os LLMs na compreensão de diferentes personas e prioridades, e permitam ao utilizador apresentar uma nova ideia de produto.
- O LLM deve então gerar perguntas de seguimento de cada departamento para refinar e melhorar a apresentação e a ideia do produto.

## A aprendizagem não termina aqui, continue a sua jornada

Após completar esta lição, descubra a nossa [coleção de aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar o seu conhecimento em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->