[![Modèles Open Source](../../../translated_images/fr/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduction

Les agents IA représentent une avancée passionnante dans l'IA générative, permettant aux grands modèles de langage (LLM) d'évoluer d'assistants à des agents capables d'agir. Les frameworks d'agents IA permettent aux développeurs de créer des applications qui donnent aux LLM un accès aux outils et à la gestion d'état. Ces frameworks améliorent également la visibilité, permettant aux utilisateurs et développeurs de suivre les actions planifiées par les LLM, améliorant ainsi la gestion de l'expérience.

La leçon couvrira les domaines suivants :

- Comprendre ce qu'est un agent IA - Qu'est-ce qu'un agent IA exactement ?
- Explorer cinq frameworks d'agents IA différents - Qu'est-ce qui les rend uniques ?
- Appliquer ces agents IA à différents cas d'utilisation - Quand doit-on utiliser des agents IA ?

## Objectifs d'apprentissage

Après avoir suivi cette leçon, vous serez capable de :

- Expliquer ce que sont les agents IA et comment ils peuvent être utilisés.
- Comprendre les différences entre certains frameworks d'agents IA populaires et leurs spécificités.
- Comprendre le fonctionnement des agents IA afin de construire des applications avec eux.

## Qu'est-ce qu'un agent IA ?

Les agents IA représentent un domaine très enthousiasmant dans le monde de l'IA générative. Cette excitation s'accompagne parfois d'une confusion sur les termes et leur application. Pour garder les choses simples et inclure la plupart des outils faisant référence aux agents IA, nous allons utiliser cette définition :

Les agents IA permettent aux grands modèles de langage (LLM) d'exécuter des tâches en leur donnant accès à un **état** et à des **outils**.

![Modèle d'Agent](../../../translated_images/fr/what-agent.21f2893bdfd01e6a.webp)

Définissons ces termes :

**Grands modèles de langage** - Ce sont les modèles mentionnés tout au long de ce cours tels que GPT-5, GPT-4o, et Llama 3.3, etc.

**État** - Cela fait référence au contexte dans lequel le LLM travaille. Le LLM utilise le contexte de ses actions passées et le contexte actuel pour guider sa prise de décision pour les actions suivantes. Les frameworks d'agents IA facilitent la gestion de ce contexte pour les développeurs.

**Outils** - Pour accomplir la tâche que l'utilisateur a demandée et que le LLM a planifiée, le LLM doit avoir accès à des outils. Quelques exemples d'outils peuvent être une base de données, une API, une application externe ou même un autre LLM !

Ces définitions devraient vous donner une bonne base pour avancer alors que nous explorons leur mise en œuvre. Explorons quelques frameworks d'agents IA différents :

## Agents LangChain

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) est une implémentation des définitions fournies ci-dessus.

Pour gérer l'**état**, il utilise une fonction intégrée appelée `AgentExecutor`. Celle-ci accepte l'`agent` défini et les `outils` qui lui sont disponibles.

Le `AgentExecutor` stocke également l'historique de la conversation pour fournir le contexte de la discussion.

![Agents LangChain](../../../translated_images/fr/langchain-agents.edcc55b5d5c43716.webp)

LangChain propose un [catalogue d'outils](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) pouvant être importés dans votre application auxquels le LLM peut accéder. Ceux-ci sont créés par la communauté et l’équipe LangChain.

Vous pouvez ensuite définir ces outils et les passer au `AgentExecutor`.

La visibilité est un autre aspect important lorsqu'on parle d'agents IA. Il est important que les développeurs d’applications comprennent quel outil le LLM utilise et pourquoi. Pour cela, l'équipe de LangChain a développé LangSmith.

## AutoGen

Le prochain framework d'agent IA que nous allons discuter est [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). L'objectif principal d'AutoGen est les conversations. Les agents sont à la fois **conversationnels** et **personnalisables**.

**Conversationnels -** Les LLM peuvent démarrer et poursuivre une conversation avec un autre LLM afin de compléter une tâche. Cela se fait en créant des `AssistantAgents` et en leur donnant un message système spécifique.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personnalisables** - Les agents peuvent être définis non seulement comme des LLM mais aussi comme un utilisateur ou un outil. En tant que développeur, vous pouvez définir un `UserProxyAgent` qui est responsable d'interagir avec l'utilisateur pour obtenir des retours dans la réalisation d'une tâche. Ce retour peut soit continuer l'exécution de la tâche, soit l'arrêter.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### État et Outils

Pour changer et gérer l'état, un agent assistant génère du code Python pour accomplir la tâche.

Voici un exemple du processus :

![AutoGen](../../../translated_images/fr/autogen.dee9a25a45fde584.webp)

#### LLM défini avec un message système

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ce message système dirige ce LLM spécifique vers les fonctions pertinentes pour sa tâche. N'oubliez pas qu'avec AutoGen, vous pouvez avoir plusieurs AssistantAgents définis avec différents messages système.

#### La conversation est initiée par l'utilisateur

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ce message de user_proxy (Humain) est ce qui va démarrer le processus de l'agent pour explorer les fonctions possibles qu'il doit exécuter.

#### Fonction exécutée

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Une fois la conversation initiale traitée, l'agent enverra l'outil suggéré à appeler. Dans ce cas, il s'agit d'une fonction appelée `get_weather`. Selon votre configuration, cette fonction peut être automatiquement exécutée et lue par l'agent ou peut être exécutée en fonction de la saisie utilisateur.

Vous pouvez trouver une liste d’[exemples de code AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) pour explorer davantage comment commencer à construire.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) est le SDK open source de Microsoft pour construire des agents IA et des systèmes multi-agents en **Python** et en **.NET**. Il rassemble les forces de deux projets Microsoft antérieurs — les fonctionnalités d'entreprise de **Semantic Kernel** et l'orchestration multi-agent de **AutoGen** — en un seul framework supporté. Si vous commencez un nouveau projet d'agent aujourd'hui, c'est le successeur recommandé à AutoGen.

Le framework s'adapte depuis un **agent de chat** unique jusqu'à des **flux de travail multi-agents** complexes, et il s'intègre directement avec Microsoft Foundry, Azure OpenAI et OpenAI. Il offre aussi une observabilité intégrée via OpenTelemetry pour que vous puissiez tracer précisément ce que font vos agents.

### État et Outils

**État** - Le framework gère le contexte de la conversation pour vous grâce aux **threads**. Un agent garde la trace de l’historique des messages (demandes de l'utilisateur, appels d’outils, et leurs résultats), de sorte que chaque tour s’appuie sur les précédents. Les threads peuvent aussi être sauvegardés, permettant de mettre une conversation en pause et de la reprendre plus tard.

**Outils** - Vous donnez à un agent des outils en lui passant des fonctions Python simples. Les paramètres annotés avec leur type sont automatiquement transformés en schéma, afin que le modèle sache comment et quand les appeler (appel de fonction). Le framework supporte aussi les serveurs Model Context Protocol (MCP) et les outils hébergés comme un interpréteur de code.

Voici un exemple d'un agent unique avec un outil personnalisé :

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

Pour vous connecter à Azure OpenAI dans Microsoft Foundry à la place, transmettez votre point de terminaison et vos identifiants au client :

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Flux de travail multi-agents

Là où le framework se distingue vraiment, c’est dans l’orchestration de plusieurs agents ensemble. Par exemple, vous pouvez exécuter les agents l’un après l’autre (chacun passant son contexte au suivant) ou les lancer en parallèle et agréger leurs résultats :

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Exécuter les agents en séquence, en transmettant le contexte de la conversation le long de la chaîne
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Répartir les agents en parallèle, puis agréger leurs réponses
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Pour installer le framework et commencer :

```bash
pip install agent-framework-core
# Intégrations optionnelles
pip install agent-framework-openai       # OpenAI et Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Vous pouvez en découvrir davantage dans le [dépôt Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) et la [documentation officielle](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Le prochain framework d'agent que nous allons explorer est [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Il est connu comme un agent "code-first" parce qu’au lieu de travailler strictement avec des `strings`, il peut travailler avec des DataFrames en Python. Cela devient extrêmement utile pour les tâches d'analyse et de génération de données. Cela peut être, par exemple, créer des graphiques et diagrammes ou générer des nombres aléatoires.

### État et Outils

Pour gérer l'état de la conversation, TaskWeaver utilise le concept de `Planner`. Le `Planner` est un LLM qui prend la requête des utilisateurs et établit les tâches à accomplir pour satisfaire cette requête.

Pour accomplir les tâches, le `Planner` a accès à une collection d’outils appelée `Plugins`. Ceux-ci peuvent être des classes Python ou un interpréteur de code général. Ces plugins sont stockés sous forme d’embeddings afin que le LLM puisse mieux rechercher le plugin adéquat.

![Taskweaver](../../../translated_images/fr/taskweaver.da8559999267715a.webp)

Voici un exemple d’un plugin pour gérer la détection d'anomalies :

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Le code est vérifié avant exécution. Une autre fonction pour gérer le contexte dans Taskweaver est l'`experience`. L’expérience permet d’enregistrer le contexte d’une conversation sur le long terme dans un fichier YAML. Cela peut être configuré de manière à ce que le LLM s’améliore au fil du temps sur certaines tâches, à condition qu’il soit exposé à des conversations précédentes.

## JARVIS

Le dernier framework d'agent que nous allons explorer est [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ce qui rend JARVIS unique est qu’il utilise un LLM pour gérer l'`état` de la conversation et les `outils` sont d’autres modèles d’IA. Chacun de ces modèles IA est spécialisé pour réaliser certaines tâches comme la détection d'objets, la transcription ou la légende d’image.

![JARVIS](../../../translated_images/fr/jarvis.762ddbadbd1a3a33.webp)

Le LLM, étant un modèle polyvalent, reçoit la demande de l'utilisateur et identifie la tâche spécifique ainsi que les arguments/données nécessaires pour accomplir la tâche.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Le LLM formate alors la requête d’une manière que le modèle IA spécialisé peut interpréter, comme du JSON. Une fois que le modèle IA a retourné sa prédiction basée sur la tâche, le LLM reçoit la réponse.

Si plusieurs modèles sont nécessaires pour accomplir la tâche, il interprétera aussi les réponses de ces modèles avant de les fusionner pour générer la réponse à l'utilisateur.

L'exemple ci-dessous montre comment cela fonctionnerait lorsqu’un utilisateur demande une description et un comptage des objets dans une image :

## Devoir

Pour poursuivre votre apprentissage des agents IA, vous pouvez construire avec Microsoft Agent Framework :

- Une application qui simule une réunion d’affaires avec différents départements d’une start-up éducative.
- Créez des messages système qui guident les LLM à comprendre différentes personas et priorités, et permettent à l’utilisateur de présenter une nouvelle idée de produit.
- Le LLM devrait ensuite générer des questions de suivi de chaque département pour affiner et améliorer la présentation et l'idée de produit.

## L'apprentissage ne s'arrête pas ici, continuez l'aventure

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à monter en compétence sur l’IA générative !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->