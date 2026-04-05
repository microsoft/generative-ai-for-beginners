# Construire avec les modèles de la famille Meta

## Introduction

Cette leçon couvrira :

- Exploration des deux principaux modèles de la famille Meta - Llama 3.1 et Llama 3.2
- Comprendre les cas d'usage et scénarios pour chaque modèle
- Exemple de code pour montrer les fonctionnalités uniques de chaque modèle

## La famille de modèles Meta

Dans cette leçon, nous allons explorer 2 modèles de la famille Meta ou "Llama Herd" - Llama 3.1 et Llama 3.2.

Ces modèles se déclinent en différentes variantes et sont disponibles sur le marché GitHub Model. Voici plus de détails sur l'utilisation des modèles GitHub pour [prototyper avec des modèles IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variantes de modèles :  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Note : Llama 3 est également disponible sur GitHub Models mais ne sera pas couvert dans cette leçon*

## Llama 3.1

Avec 405 milliards de paramètres, Llama 3.1 s'inscrit dans la catégorie des LLM open source.

Le modèle est une amélioration de la précédente version Llama 3 en offrant :

- Fenêtre de contexte plus grande - 128k tokens contre 8k tokens
- Nombre maximum de tokens en sortie plus élevé - 4096 contre 2048
- Meilleur support multilingue - dû à l'augmentation des tokens d'entraînement

Cela permet à Llama 3.1 de gérer des cas d'usage plus complexes lors de la création d'applications GenAI incluant : 
- Appel natif de fonctions - capacité à appeler des outils externes et fonctions en dehors du workflow LLM
- Meilleure performance RAG - grâce à une fenêtre de contexte plus large
- Génération de données synthétiques - capacité à créer des données efficaces pour des tâches telles que le fine-tuning

### Appel natif de fonctions

Llama 3.1 a été affiné pour être plus efficace dans les appels de fonctions ou d’outils. Il dispose également de deux outils intégrés que le modèle peut identifier comme devant être utilisés selon l'invite de l'utilisateur. Ces outils sont :

- **Brave Search** - Peut être utilisé pour obtenir des informations à jour comme la météo en effectuant une recherche web
- **Wolfram Alpha** - Peut être utilisé pour des calculs mathématiques complexes sans nécessiter d'écrire vos propres fonctions.

Vous pouvez aussi créer vos propres outils personnalisés que le LLM peut appeler.

Dans l'exemple de code ci-dessous :

- Nous définissons les outils disponibles (brave_search, wolfram_alpha) dans l'invite système.
- Envoyons une invite utilisateur qui demande la météo d’une ville précise.
- Le LLM répondra par un appel à l’outil Brave Search qui ressemblera à ceci `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Note : Cet exemple effectue uniquement l’appel à l’outil, si vous souhaitez obtenir les résultats, vous devrez créer un compte gratuit sur la page Brave API et définir la fonction elle-même.

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

Malgré son statut de LLM, une limitation de Llama 3.1 est son absence de multimodalité. C’est-à-dire l’incapacité d’utiliser différents types d'entrées telles que des images comme prompt et de fournir des réponses. Cette capacité est l’une des caractéristiques principales de Llama 3.2. Ces caractéristiques incluent également :

- Multimodalité - capacité à évaluer à la fois du texte et des images comme prompts
- Variantes de petite à moyenne taille (11B et 90B) - offrant des options de déploiement flexibles,
- Variantes uniquement texte (1B et 3B) - permettant un déploiement sur des appareils edge / mobiles avec une faible latence

Le support multimodal représente un grand pas dans le monde des modèles open source. L’exemple de code ci-dessous prend à la fois une image et un prompt texte pour obtenir une analyse de l’image avec Llama 3.2 90B.

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
  
## L’apprentissage ne s’arrête pas ici, continuez votre parcours

Après avoir terminé cette leçon, découvrez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->