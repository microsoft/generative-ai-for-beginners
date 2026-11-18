# Construire avec les modèles de la famille Meta

## Introduction

Cette leçon couvrira :

- Explorer les deux principaux modèles de la famille Meta - Llama 3.1 et Llama 3.2, ainsi que les alternatives actuellement disponibles utilisées dans les exemples de code (Llama 3.3 et Llama 4) 
- Comprendre les cas d'utilisation et les scénarios pour chaque modèle 
- Exemple de code pour montrer les caractéristiques uniques de chaque modèle 


## La famille de modèles Meta

Dans cette leçon, nous allons explorer 2 modèles de la famille Meta ou "Llama Herd" - Llama 3.1 et Llama 3.2. Les exemples de code exécutables utilisent Llama 3.3 et Llama 4, qui sont actuellement des alternatives disponibles dans le catalogue Microsoft Foundry Models.

Ces modèles existent en différentes variantes et sont disponibles dans le [catalogue Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Note :** GitHub Models sera retiré à la fin de juillet 2026. Voici plus de détails sur l'utilisation de [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pour prototyper avec des modèles IA.

> **Remarque :** Les versions spécifiques des modèles sur lesquelles cette leçon a été initialement écrite (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) ont depuis été retirées du catalogue Microsoft Foundry Models. Les exemples de code ci-dessous utilisent `Llama-3.3-70B-Instruct` et `Llama-4-Scout-17B-16E-Instruct` comme alternatives actuellement disponibles dans le catalogue Microsoft Foundry Models, ils fonctionnent donc encore aujourd'hui.

Variantes de modèle (comme couvert initialement dans cette leçon) : 
- Llama 3.1 - 70B Instruct (retraité) 
- Llama 3.1 - 405B Instruct (retraité) 
- Llama 3.2 - 11B Vision Instruct (retraité) 
- Llama 3.2 - 90B Vision Instruct (retraité) 

Alternatives actuellement disponibles utilisées dans les exemples de code : 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Note : Les variantes de Llama 3 évoquées ci-dessus sont conservées pour le contexte historique et ne sont plus disponibles dans les modèles Microsoft Foundry.*

## Llama 3.1

Avec 405 milliards de paramètres, Llama 3.1 s'inscrit dans la catégorie des LLM open source.

Ce modèle est une mise à jour de la version précédente Llama 3 en offrant :

- Fenêtre de contexte plus grande - 128k tokens contre 8k tokens
- Nombre maximal de tokens en sortie plus élevé - 4096 contre 2048
- Meilleur support multilingue - grâce à une augmentation des tokens d'entraînement

Cela permet à Llama 3.1 de gérer des cas d'utilisation plus complexes lors de la création d'applications GenAI, notamment :
- Appels de fonctions natifs - la capacité d'appeler des outils et fonctions externes hors du flux de travail LLM
- Meilleure performance RAG - grâce à la fenêtre de contexte plus large
- Génération de données synthétiques - capacité à créer des données efficaces pour des tâches comme l'affinage

### Appels de fonctions natifs

Llama 3.1 a été affiné pour être plus efficace dans la réalisation d'appels de fonctions ou d'outils. Il dispose également de deux outils intégrés que le modèle peut identifier comme nécessaires à utiliser en fonction de l'invite de l'utilisateur. Ces outils sont :

- **Brave Search** - Peut être utilisé pour obtenir des informations à jour comme la météo en effectuant une recherche web
- **Wolfram Alpha** - Peut être utilisé pour des calculs mathématiques complexes, ce qui évite d'écrire vos propres fonctions.

Vous pouvez également créer vos propres outils personnalisés que le LLM peut appeler.

Dans l'exemple de code ci-dessous :

- Nous définissons les outils disponibles (brave_search, wolfram_alpha) dans l'invite système.
- Envoyons une invite utilisateur qui demande la météo dans une certaine ville.
- Le LLM répondra avec un appel à l'outil Brave Search qui ressemblera à ceci `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Note : Cet exemple réalise uniquement l'appel à l'outil, si vous souhaitez obtenir les résultats, vous devrez créer un compte gratuit sur la page Brave API et définir la fonction elle-même.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Bien qu'étant un LLM, une limitation de Llama 3.1 est son absence de multimodalité. C’est-à-dire son incapacité à utiliser différents types d'entrée comme les images en tant qu'invite et à fournir des réponses. Cette capacité est l'une des principales caractéristiques de Llama 3.2. Ces fonctionnalités incluent également :

- Multimodalité - capacité à évaluer à la fois des invites textuelles et d'image
- Variations de petite à moyenne taille (11B et 90B) - offrant des options flexibles de déploiement,
- Variations uniquement textuelles (1B et 3B) - permettant le déploiement sur des appareils edge / mobiles et fournissant une faible latence

La prise en charge multimodale représente un grand pas dans le monde des modèles open source. L'exemple de code ci-dessous prend à la fois une image et une invite de texte pour obtenir une analyse de l'image. Comme Llama 3.2 90B Vision Instruct a été retiré, l'exemple utilise `Llama-4-Scout-17B-16E-Instruct`, une alternative multimodale native actuellement disponible. 


### Support multimodal avec Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## L'apprentissage ne s'arrête pas ici, continuez le voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage en IA Générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à augmenter vos connaissances en IA Générative !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->