<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:05:32+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fr"
}
-->
# Construire avec les modèles de la famille Meta

## Introduction

Cette leçon couvrira :

- Exploration des deux principaux modèles de la famille Meta - Llama 3.1 et Llama 3.2  
- Compréhension des cas d’usage et des scénarios pour chaque modèle  
- Exemple de code pour montrer les fonctionnalités uniques de chaque modèle  

## La famille de modèles Meta

Dans cette leçon, nous allons explorer 2 modèles de la famille Meta ou "Llama Herd" - Llama 3.1 et Llama 3.2

Ces modèles existent en différentes variantes et sont disponibles sur le GitHub Model marketplace. Voici plus de détails sur l’utilisation des GitHub Models pour [prototyper avec des modèles d’IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variantes des modèles :  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Note : Llama 3 est également disponible sur GitHub Models mais ne sera pas abordé dans cette leçon*

## Llama 3.1

Avec ses 405 milliards de paramètres, Llama 3.1 fait partie de la catégorie des LLM open source.

Ce modèle est une amélioration par rapport à la version précédente Llama 3 en offrant :

- Une fenêtre de contexte plus grande - 128k tokens contre 8k tokens  
- Un nombre maximal de tokens en sortie plus élevé - 4096 contre 2048  
- Un meilleur support multilingue - grâce à l’augmentation des tokens d’entraînement  

Cela permet à Llama 3.1 de gérer des cas d’usage plus complexes lors de la création d’applications GenAI, notamment :  
- Appels de fonctions natives - la capacité d’appeler des outils et fonctions externes en dehors du flux de travail LLM  
- Meilleure performance RAG - grâce à la fenêtre de contexte plus large  
- Génération de données synthétiques - la capacité de créer des données efficaces pour des tâches comme le fine-tuning  

### Appels de fonctions natives

Llama 3.1 a été affiné pour être plus efficace dans les appels de fonctions ou d’outils. Il dispose également de deux outils intégrés que le modèle peut identifier comme nécessaires à utiliser selon la requête de l’utilisateur. Ces outils sont :

- **Brave Search** - Peut être utilisé pour obtenir des informations à jour comme la météo en effectuant une recherche web  
- **Wolfram Alpha** - Peut être utilisé pour des calculs mathématiques plus complexes, évitant ainsi d’écrire vos propres fonctions  

Vous pouvez aussi créer vos propres outils personnalisés que le LLM pourra appeler.

Dans l’exemple de code ci-dessous :

- Nous définissons les outils disponibles (brave_search, wolfram_alpha) dans le prompt système.  
- Nous envoyons une requête utilisateur qui demande la météo dans une certaine ville.  
- Le LLM répondra par un appel à l’outil Brave Search qui ressemblera à ceci `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Note : Cet exemple ne fait que l’appel à l’outil, si vous souhaitez obtenir les résultats, vous devrez créer un compte gratuit sur la page Brave API et définir la fonction elle-même*

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

Bien qu’étant un LLM, une limitation de Llama 3.1 est la multimodalité. C’est-à-dire la capacité à utiliser différents types d’entrées comme des images en tant que prompts et à fournir des réponses. Cette capacité est l’une des principales fonctionnalités de Llama 3.2. Ces fonctionnalités incluent également :

- Multimodalité - capacité à évaluer à la fois des prompts texte et image  
- Variantes de petite à moyenne taille (11B et 90B) - offrant des options de déploiement flexibles  
- Variantes uniquement texte (1B et 3B) - permettant le déploiement sur des appareils edge / mobiles avec une faible latence  

Le support multimodal représente un grand pas dans le monde des modèles open source. L’exemple de code ci-dessous prend à la fois une image et un prompt texte pour obtenir une analyse de l’image par Llama 3.2 90B.

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

## L’apprentissage ne s’arrête pas là, continuez l’aventure

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.