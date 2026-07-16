[![Open Source Models](../../../translated_images/pt-PT/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introdução

Os Agentes de IA representam um desenvolvimento entusiasmante na IA Generativa, permitindo que os Modelos de Linguagem de Grande Escala (LLMs) evoluam de assistentes para agentes capazes de tomar ações. Os frameworks de Agentes de IA permitem aos desenvolvedores criar aplicações que oferecem aos LLMs acesso a ferramentas e gestão de estado. Estes frameworks também melhoram a visibilidade, permitindo que os utilizadores e desenvolvedores monitorem as ações planeadas pelos LLMs, melhorando assim a gestão da experiência.

A lição abordará as seguintes áreas:

- Compreender o que é um Agente de IA - O que exatamente é um Agente de IA?
- Explorar cinco diferentes frameworks de Agentes de IA - O que os torna únicos?
- Aplicar esses Agentes de IA a diferentes casos de uso - Quando devemos usar Agentes de IA?

## Objetivos de aprendizagem

Após esta lição, será capaz de:

- Explicar o que são Agentes de IA e como podem ser usados.
- Ter uma compreensão das diferenças entre alguns dos populares frameworks de Agentes de IA, e como diferem.
- Compreender como funcionam os Agentes de IA para construir aplicações com eles.

## O que são Agentes de IA?

Os Agentes de IA são um campo muito entusiasmante no mundo da IA Generativa. Com este entusiasmo surge às vezes uma confusão de termos e das suas aplicações. Para simplificar e incluir a maioria das ferramentas que se referem a Agentes de IA, vamos usar esta definição:

Os Agentes de IA permitem que os Modelos de Linguagem de Grande Escala (LLMs) executem tarefas dando-lhes acesso a um **estado** e **ferramentas**.

![Agent Model](../../../translated_images/pt-PT/what-agent.21f2893bdfd01e6a.webp)

Vamos definir estes termos:

**Modelos de Linguagem de Grande Escala** - Estes são os modelos referidos ao longo deste curso, como GPT-3.5, GPT-4, Llama-2, etc.

**Estado** - Refere-se ao contexto em que o LLM está a trabalhar. O LLM utiliza o contexto das suas ações anteriores e o contexto atual, orientando a sua tomada de decisão para ações subsequentes. Os frameworks de Agentes de IA permitem que os desenvolvedores mantenham este contexto de forma mais fácil.

**Ferramentas** - Para completar a tarefa que o utilizador solicitou e que o LLM planeou, o LLM precisa de acesso a ferramentas. Alguns exemplos de ferramentas podem ser uma base de dados, uma API, uma aplicação externa ou até mesmo outro LLM!

Estas definições irão, esperamos, fornecer uma boa base para avançarmos enquanto analisamos como são implementados. Vamos explorar alguns frameworks diferentes de Agentes de IA:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) é uma implementação das definições que fornecemos acima.

Para gerir o **estado** , utiliza uma função incorporada chamada `AgentExecutor`. Esta aceita o `agent` definido e as `tools` disponíveis.

O `Agent Executor` também armazena o histórico do chat para fornecer o contexto da conversa.

![Langchain Agents](../../../translated_images/pt-PT/langchain-agents.edcc55b5d5c43716.webp)

A LangChain oferece um [catálogo de ferramentas](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) que podem ser importadas para a sua aplicação, às quais o LLM pode ter acesso. Estas são feitas pela comunidade e pela equipa da LangChain.

Pode então definir estas ferramentas e passá-las para o `Agent Executor`.

A visibilidade é outro aspeto importante quando se fala em Agentes de IA. É importante para os desenvolvedores de aplicações compreender qual ferramenta o LLM está a usar e porquê. Para isso, a equipa da LangChain desenvolveu o LangSmith.

## AutoGen

O próximo framework de Agentes de IA que vamos discutir é o [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). O foco principal do AutoGen são as conversas. Os agentes são tanto **conversáveis** como **personalizáveis**.

**Conversável -** Os LLMs podem iniciar e continuar uma conversa com outro LLM para completar uma tarefa. Isto é feito criando `AssistantAgents` e dando-lhes uma mensagem de sistema específica.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizável** - Os agentes podem ser definidos não só como LLMs, mas também como um utilizador ou uma ferramenta. Como desenvolvedor, pode definir um `UserProxyAgent` que é responsável por interagir com o utilizador para obter feedback na execução de uma tarefa. Este feedback pode continuar a execução da tarefa ou pará-la.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado e Ferramentas

Para alterar e gerir o estado, um Agente assistente gera código Python para completar a tarefa.

Aqui está um exemplo do processo:

![AutoGen](../../../translated_images/pt-PT/autogen.dee9a25a45fde584.webp)

#### LLM Definido com uma Mensagem de Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Esta mensagem de sistema dirige este LLM específico para quais funções são relevantes para a sua tarefa. Lembre-se, com o AutoGen pode ter vários AssistantAgents definidos com mensagens de sistema diferentes.

#### Chat é Iniciado pelo Utilizador

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Esta mensagem do user_proxy (Humano) é o que iniciará o processo do Agente para explorar as possíveis funções que deverá executar.

#### Função é Executada

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Depois de processado o chat inicial, o Agente enviará a sugestão de ferramenta a chamar. Neste caso, é uma função chamada `get_weather`. Dependendo da sua configuração, esta função pode ser executada automaticamente e lida pelo Agente ou pode ser executada com base na entrada do utilizador.

Pode encontrar uma lista de [exemplos de código AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) para explorar melhor como começar a construir.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) é o SDK open-source da Microsoft para construir Agentes de IA e sistemas multi-agente em **Python** e **.NET**. Reúne as forças de dois projetos anteriores da Microsoft — as funcionalidades empresariais do **Semantic Kernel** e a orquestração multi-agente do **AutoGen** — num único framework apoiado. Se está a iniciar um novo projeto de agente hoje, este é o sucessor recomendado do AutoGen.

O framework escala desde um único **agente de chat** até workflows complexos de **multi-agentes**, e integra-se diretamente com Microsoft Foundry, Azure OpenAI e OpenAI. Também fornece observabilidade incorporada através do OpenTelemetry, para que possa rastrear exatamente o que os seus agentes estão a fazer.

### Estado e Ferramentas

**Estado** - O framework gere o contexto da conversa por si através de **threads**. Um agente mantém o histórico das mensagens (pedidos do utilizador, chamadas de ferramenta, e os seus resultados), para que cada turno construa sobre os anteriores. As threads também podem ser persistidas, permitindo que uma conversa seja pausada e retomada mais tarde.

**Ferramentas** - Dá ferramentas a um agente passando funções Python simples. Os parâmetros anotados com tipo são automaticamente convertidos num esquema, para que o modelo saiba como e quando os chamar (chamada de função). O framework também suporta servidores do Protocolo de Contexto do Modelo (MCP) e ferramentas alojadas como um interpretador de código.

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

Para se conectar ao Azure OpenAI no Microsoft Foundry, em vez disso, passe o seu endpoint e credenciais para o cliente:

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

Onde o framework realmente se destaca é na orquestração de vários agentes juntos. Por exemplo, pode executar agentes um após outro (cada um passando o seu contexto para o seguinte) ou expandir para vários agentes em paralelo e agregar os seus resultados:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Execute agentes em sequência, passando o contexto da conversa ao longo da cadeia
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribua para agentes em paralelo, depois agregue as suas respostas
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

O próximo framework de agente que vamos explorar é o [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). É conhecido como um agente "code-first" porque, em vez de trabalhar estritamente com `strings` , pode trabalhar com DataFrames em Python. Isto torna-se extremamente útil para tarefas de análise e geração de dados. Pode ser coisas como criar gráficos e tabelas ou gerar números aleatórios.

### Estado e Ferramentas

Para gerir o estado da conversa, o TaskWeaver usa o conceito de um `Planner`. O `Planner` é um LLM que recebe o pedido dos utilizadores e mapeia as tarefas que precisam de ser completadas para cumprir este pedido.

Para completar as tarefas, o `Planner` tem acesso à coleção de ferramentas chamadas `Plugins`. Isto podem ser classes Python ou um interpretador de código geral. Estes plugins são armazenados como embeddings para que o LLM possa procurar melhor o plugin correto.

![Taskweaver](../../../translated_images/pt-PT/taskweaver.da8559999267715a.webp)

Aqui está um exemplo de um plugin para lidar com deteção de anomalias:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

O código é verificado antes de ser executado. Outra funcionalidade para gerir o contexto no Taskweaver é a `experience`. A experiência permite que o contexto de uma conversa seja armazenado a longo prazo num ficheiro YAML. Isto pode ser configurado para que o LLM melhore ao longo do tempo em certas tarefas, dado que está exposto a conversas anteriores.

## JARVIS

O último framework de agentes que vamos explorar é o [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). O que torna o JARVIS único é que usa um LLM para gerir o `estado` da conversa e as `ferramentas` são outros modelos de IA. Cada um dos modelos de IA são modelos especializados que realizam certas tarefas como deteção de objetos, transcrição ou legendagem de imagens.

![JARVIS](../../../translated_images/pt-PT/jarvis.762ddbadbd1a3a33.webp)

O LLM, sendo um modelo de uso geral, recebe o pedido do utilizador e identifica a tarefa específica e quaisquer argumentos/dados necessários para completar a tarefa.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

O LLM depois formata o pedido de maneira que o modelo de IA especializado pode interpretar, como JSON. Uma vez que o modelo de IA tenha retornado a sua previsão baseada na tarefa, o LLM recebe a resposta.

Se forem necessários múltiplos modelos para completar a tarefa, ele também interpretará a resposta desses modelos antes de juntá-los para gerar a resposta para o utilizador.

O exemplo abaixo mostra como isto funcionaria quando um utilizador está a pedir uma descrição e contagem dos objetos numa imagem:

## Trabalho para casa

Para continuar o seu aprendizado de Agentes de IA, pode construir com o Microsoft Agent Framework:

- Uma aplicação que simule uma reunião de negócios com diferentes departamentos de uma startup de educação.
- Criar mensagens de sistema que guiem os LLMs na compreensão de diferentes personas e prioridades, e permitir que o utilizador apresente uma nova ideia de produto.
- O LLM deve então gerar perguntas de acompanhamento de cada departamento para refinar e melhorar a apresentação e a ideia do produto.

## O aprendizado não termina aqui, continue a jornada

Após completar esta lição, confira a nossa [coleção de aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aumentar os seus conhecimentos em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->