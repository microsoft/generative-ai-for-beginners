# Construire avec les modèles de la famille Meta

## Introduction

Cette leçon couvrira :

- L'exploration des deux principaux modèles de la famille Meta - Llama 3.1 et Llama 3.2
- La compréhension des cas d'utilisation et des scénarios pour chaque modèle
- Un exemple de code pour montrer les caractéristiques uniques de chaque modèle

## La famille de modèles Meta

Dans cette leçon, nous allons explorer 2 modèles de la famille Meta ou "Llama Herd" - Llama 3.1 et Llama 3.2

Ces modèles existent en différentes variantes et sont disponibles sur le marché des modèles Github. Voici plus de détails sur l'utilisation des modèles Github pour [prototyper avec des modèles d'IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variantes de modèle :
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Remarque : Llama 3 est également disponible sur les modèles Github mais ne sera pas couvert dans cette leçon*

## Llama 3.1

Avec 405 milliards de paramètres, Llama 3.1 s'inscrit dans la catégorie des LLM open source.

Le modèle est une amélioration de la version précédente Llama 3 en offrant :

- Une fenêtre contextuelle plus grande - 128k tokens contre 8k tokens
- Plus de tokens de sortie maximale - 4096 contre 2048
- Meilleur support multilingue - grâce à l'augmentation des tokens d'entraînement

Cela permet à Llama 3.1 de gérer des cas d'utilisation plus complexes lors de la création d'applications GenAI, y compris :
- Appel de fonctions natives - la capacité d'appeler des outils et fonctions externes en dehors du flux de travail LLM
- Meilleure performance RAG - grâce à la fenêtre contextuelle plus large
- Génération de données synthétiques - la capacité de créer des données efficaces pour des tâches telles que l'ajustement fin

### Appel de fonctions natives

Llama 3.1 a été affiné pour être plus efficace dans l'appel de fonctions ou d'outils. Il dispose également de deux outils intégrés que le modèle peut identifier comme nécessaires à utiliser en fonction de la demande de l'utilisateur. Ces outils sont :

- **Brave Search** - Peut être utilisé pour obtenir des informations à jour comme la météo en effectuant une recherche sur le web
- **Wolfram Alpha** - Peut être utilisé pour des calculs mathématiques plus complexes, de sorte qu'il n'est pas nécessaire d'écrire vos propres fonctions.

Vous pouvez également créer vos propres outils personnalisés que le LLM peut appeler.

Dans l'exemple de code ci-dessous :

- Nous définissons les outils disponibles (brave_search, wolfram_alpha) dans l'invite système.
- Envoyez une invite utilisateur qui demande la météo dans une certaine ville.
- Le LLM répondra par un appel d'outil à l'outil Brave Search qui ressemblera à ceci `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Remarque : Cet exemple ne fait que l'appel de l'outil, si vous souhaitez obtenir les résultats, vous devrez créer un compte gratuit sur la page API de Brave et définir la fonction elle-même*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

Malgré le fait d'être un LLM, une limitation que Llama 3.1 a est la multimodalité. C'est-à-dire la capacité d'utiliser différents types d'entrée tels que des images comme invites et de fournir des réponses. Cette capacité est l'une des principales caractéristiques de Llama 3.2. Ces caractéristiques incluent également :

- Multimodalité - a la capacité d'évaluer à la fois des invites texte et image
- Variations de taille petite à moyenne (11B et 90B) - cela offre des options de déploiement flexibles,
- Variations texte uniquement (1B et 3B) - cela permet au modèle d'être déployé sur des appareils edge / mobiles et offre une faible latence

Le support multimodal représente un grand pas en avant dans le monde des modèles open source. L'exemple de code ci-dessous prend à la fois une image et une invite texte pour obtenir une analyse de l'image de Llama 3.2 90B.

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

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

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.