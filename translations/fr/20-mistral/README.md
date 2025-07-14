<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:55:08+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fr"
}
-->
# Construire avec les modèles Mistral

## Introduction

Cette leçon couvrira :  
- L’exploration des différents modèles Mistral  
- La compréhension des cas d’usage et scénarios pour chaque modèle  
- Des exemples de code montrant les fonctionnalités uniques de chaque modèle.

## Les modèles Mistral

Dans cette leçon, nous allons explorer 3 modèles Mistral différents :  
**Mistral Large**, **Mistral Small** et **Mistral Nemo**.

Chacun de ces modèles est disponible gratuitement sur le marketplace Github Model. Le code de ce notebook utilisera ces modèles pour exécuter le code. Voici plus de détails sur l’utilisation des Github Models pour [prototyper avec des modèles d’IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 est actuellement le modèle phare de Mistral, conçu pour un usage en entreprise.

Ce modèle est une amélioration par rapport au Mistral Large original en offrant :  
- Une fenêtre de contexte plus grande - 128k contre 32k  
- De meilleures performances en mathématiques et en programmation - 76,9 % de précision moyenne contre 60,4 %  
- Une performance multilingue accrue - langues incluses : anglais, français, allemand, espagnol, italien, portugais, néerlandais, russe, chinois, japonais, coréen, arabe et hindi.

Grâce à ces caractéristiques, Mistral Large excelle dans :  
- *Retrieval Augmented Generation (RAG)* - grâce à la fenêtre de contexte plus large  
- *Function Calling* - ce modèle dispose d’un appel de fonction natif permettant l’intégration avec des outils et API externes. Ces appels peuvent être effectués en parallèle ou séquentiellement.  
- *Génération de code* - ce modèle est performant pour la génération en Python, Java, TypeScript et C++.

### Exemple RAG avec Mistral Large 2

Dans cet exemple, nous utilisons Mistral Large 2 pour appliquer un schéma RAG sur un document texte. La question est écrite en coréen et porte sur les activités de l’auteur avant l’université.

Il utilise le modèle d’Embeddings Cohere pour créer des embeddings du document texte ainsi que de la question. Pour cet exemple, il utilise le package Python faiss comme magasin vectoriel.

Le prompt envoyé au modèle Mistral inclut à la fois la question et les extraits récupérés similaires à la question. Le modèle fournit ensuite une réponse en langage naturel.

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
Mistral Small est un autre modèle de la famille Mistral, dans la catégorie premier/entreprise. Comme son nom l’indique, ce modèle est un Small Language Model (SLM). Les avantages de Mistral Small sont :  
- Économies de coûts par rapport aux LLM Mistral comme Mistral Large et NeMo - réduction de prix de 80 %  
- Faible latence - réponse plus rapide comparée aux LLM de Mistral  
- Flexibilité - peut être déployé dans différents environnements avec moins de contraintes sur les ressources requises.

Mistral Small est idéal pour :  
- Les tâches basées sur le texte comme le résumé, l’analyse de sentiment et la traduction.  
- Les applications avec des requêtes fréquentes grâce à son rapport coût-efficacité  
- Les tâches de code à faible latence comme la revue et les suggestions de code

## Comparaison entre Mistral Small et Mistral Large

Pour montrer les différences de latence entre Mistral Small et Large, exécutez les cellules ci-dessous.

Vous devriez observer une différence de temps de réponse entre 3 et 5 secondes. Notez également la longueur et le style des réponses pour le même prompt.

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

Comparé aux deux autres modèles abordés dans cette leçon, Mistral NeMo est le seul modèle gratuit sous licence Apache2.

Il est considéré comme une évolution du premier LLM open source de Mistral, Mistral 7B.

Parmi les autres caractéristiques du modèle NeMo :  

- *Tokenisation plus efficace :* Ce modèle utilise le tokenizer Tekken au lieu du plus courant tiktoken. Cela permet de meilleures performances sur un plus grand nombre de langues et de code.

- *Fine-tuning :* Le modèle de base est disponible pour le fine-tuning, offrant plus de flexibilité pour les cas d’usage nécessitant un ajustement.

- *Function Calling natif* - Comme Mistral Large, ce modèle a été entraîné à l’appel de fonction. Cela en fait l’un des premiers modèles open source à proposer cette fonctionnalité.

### Comparaison des tokenizers

Dans cet exemple, nous allons voir comment Mistral NeMo gère la tokenisation comparé à Mistral Large.

Les deux exemples utilisent le même prompt, mais vous devriez constater que NeMo retourne moins de tokens que Mistral Large.

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

## L’apprentissage ne s’arrête pas ici, continuez l’aventure

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.