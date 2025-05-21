<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:44:42+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fr"
}
-->
# Construire avec les modèles Mistral

## Introduction

Cette leçon couvrira :
- Exploration des différents modèles Mistral
- Compréhension des cas d'utilisation et des scénarios pour chaque modèle
- Des exemples de code montrent les caractéristiques uniques de chaque modèle.

## Les modèles Mistral

Dans cette leçon, nous explorerons 3 modèles Mistral différents : **Mistral Large**, **Mistral Small** et **Mistral Nemo**.

Chacun de ces modèles est disponible gratuitement sur le marché des modèles Github. Le code dans ce carnet utilisera ces modèles pour exécuter le code. Voici plus de détails sur l'utilisation des modèles Github pour [prototyper avec des modèles d'IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 est actuellement le modèle phare de Mistral et est conçu pour une utilisation en entreprise.

Le modèle est une mise à niveau du Mistral Large original en offrant :
- Fenêtre de contexte plus grande - 128k contre 32k
- Meilleure performance sur les tâches de mathématiques et de codage - 76,9 % de précision moyenne contre 60,4 %
- Augmentation des performances multilingues - les langues incluent : anglais, français, allemand, espagnol, italien, portugais, néerlandais, russe, chinois, japonais, coréen, arabe et hindi.

Avec ces caractéristiques, Mistral Large excelle dans :
- *Génération augmentée par récupération (RAG)* - grâce à la fenêtre de contexte plus grande
- *Appels de fonction* - ce modèle a des appels de fonction natifs qui permettent une intégration avec des outils externes et des API. Ces appels peuvent être effectués à la fois en parallèle ou successivement dans un ordre séquentiel.
- *Génération de code* - ce modèle excelle dans la génération Python, Java, TypeScript et C++.

### Exemple RAG utilisant Mistral Large 2

Dans cet exemple, nous utilisons Mistral Large 2 pour exécuter un modèle RAG sur un document texte. La question est écrite en coréen et demande les activités de l'auteur avant l'université.

Il utilise le modèle d'embeddings Cohere pour créer des embeddings du document texte ainsi que de la question. Pour cet exemple, il utilise le package Python faiss comme magasin de vecteurs.

L'invite envoyée au modèle Mistral inclut à la fois les questions et les morceaux récupérés similaires à la question. Le modèle fournit ensuite une réponse en langage naturel.

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small

Mistral Small est un autre modèle de la famille des modèles Mistral sous la catégorie premier/entreprise. Comme son nom l'indique, ce modèle est un Small Language Model (SLM). Les avantages de l'utilisation de Mistral Small sont qu'il est :
- Économique par rapport aux LLM de Mistral comme Mistral Large et NeMo - baisse de prix de 80 %
- Faible latence - réponse plus rapide par rapport aux LLM de Mistral
- Flexible - peut être déployé dans différents environnements avec moins de restrictions sur les ressources requises.

Mistral Small est idéal pour :
- Tâches basées sur le texte telles que la synthèse, l'analyse de sentiment et la traduction.
- Applications où des demandes fréquentes sont faites en raison de son efficacité économique
- Tâches de code à faible latence comme la révision et les suggestions de code

## Comparaison entre Mistral Small et Mistral Large

Pour montrer les différences de latence entre Mistral Small et Large, exécutez les cellules ci-dessous.

Vous devriez voir une différence dans les temps de réponse entre 3-5 secondes. Notez également les longueurs et le style de réponse sur la même invite.

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

Comparé aux deux autres modèles discutés dans cette leçon, Mistral NeMo est le seul modèle gratuit avec une licence Apache2.

Il est considéré comme une mise à niveau par rapport au précédent LLM open source de Mistral, Mistral 7B.

Quelques autres caractéristiques du modèle NeMo sont :

- *Tokenisation plus efficace :* Ce modèle utilise le tokenizer Tekken par rapport au tiktoken plus couramment utilisé. Cela permet une meilleure performance sur plus de langues et de code.

- *Affinage :* Le modèle de base est disponible pour l'affinage. Cela permet plus de flexibilité pour les cas d'utilisation où l'affinage peut être nécessaire.

- *Appels de fonction natifs* - Comme Mistral Large, ce modèle a été entraîné sur les appels de fonction. Cela le rend unique en étant l'un des premiers modèles open source à le faire.

### Comparaison des tokenizers

Dans cet exemple, nous allons voir comment Mistral NeMo gère la tokenisation par rapport à Mistral Large.

Les deux exemples prennent la même invite mais vous devriez voir que NeMo renvoie moins de tokens par rapport à Mistral Large.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Count the number of tokens
print(len(tokens))
```

## L'apprentissage ne s'arrête pas ici, continuez le voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage de l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à développer vos connaissances en IA générative !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.