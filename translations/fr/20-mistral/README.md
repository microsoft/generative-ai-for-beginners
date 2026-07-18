# Construire avec les modèles Mistral 

## Introduction 

Cette leçon couvrira : 
- Exploration des différents modèles Mistral 
- Compréhension des cas d'utilisation et des scénarios pour chaque modèle 
- Exploration d'exemples de code montrant les fonctionnalités uniques de chaque modèle. 

## Les modèles Mistral 

Dans cette leçon, nous explorerons 3 modèles Mistral différents : 
**Mistral Large**, **Mistral Small** et **Mistral Nemo**. 

Chacun de ces modèles est disponible gratuitement sur [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Le code dans ce carnet utilisera ces modèles pour exécuter le code.

> **Note :** GitHub Models sera retiré à la fin de juillet 2026. Voici plus de détails sur l'utilisation de [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pour prototyper avec les modèles d'IA. 


## Mistral Large 2 (2407)
Mistral Large 2 est actuellement le modèle phare de Mistral et est conçu pour une utilisation en entreprise. 

Le modèle est une amélioration par rapport au Mistral Large original en offrant 
-  Une fenêtre contextuelle plus grande - 128k contre 32k 
-  Une meilleure performance sur les tâches de mathématiques et de codage - 76,9 % de précision moyenne contre 60,4 % 
-  Une performance multilingue accrue - les langues incluent : anglais, français, allemand, espagnol, italien, portugais, néerlandais, russe, chinois, japonais, coréen, arabe et hindi.

Avec ces fonctionnalités, Mistral Large excelle dans 
- *Génération augmentée par récupération (RAG)* - grâce à la plus grande fenêtre contextuelle
- *Appel de fonction* - ce modèle dispose d'appels de fonction natifs permettant l'intégration avec des outils externes et des APIs. Ces appels peuvent être faits en parallèle ou séquentiellement. 
- *Génération de code* - ce modèle excelle dans la génération de Python, Java, TypeScript et C++. 

### Exemple de RAG utilisant Mistral Large 2 

Dans cet exemple, nous utilisons Mistral Large 2 pour exécuter un modèle RAG sur un document texte. La question est écrite en coréen et porte sur les activités de l'auteur avant l'université. 

Il utilise le modèle d’encodage de Cohere pour créer des embeddings du document texte ainsi que de la question. Pour cet exemple, il utilise le paquet Python faiss comme magasin vectoriel. 

L'invite envoyée au modèle Mistral inclut à la fois la question et les extraits récupérés similaires à la question. Le modèle fournit ensuite une réponse en langage naturel. 

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

# Obtenez-les à partir de la page "Vue d'ensemble" de votre projet Microsoft Foundry
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, indice
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
Mistral Small est un autre modèle de la famille Mistral dans la catégorie premier/entreprise. Comme son nom l'indique, ce modèle est un petit modèle de langage (SLM). Les avantages de Mistral Small sont : 
- Économies par rapport aux LLM Mistral comme Mistral Large et NeMo - réduction de prix de 80 %
- Faible latence - réponse plus rapide comparée aux LLM de Mistral
- Flexible - peut être déployé dans différents environnements avec moins de restrictions sur les ressources requises. 


Mistral Small est idéal pour : 
- Les tâches basées sur le texte comme la synthèse, l’analyse de sentiment et la traduction. 
- Les applications où des requêtes fréquentes sont faites en raison de son rapport coût-efficacité 
- Les tâches de code à faible latence comme la relecture et les suggestions de code 

## Comparaison entre Mistral Small et Mistral Large 

Pour montrer les différences de latence entre Mistral Small et Large, exécutez les cellules ci-dessous. 

Vous devriez voir une différence dans les temps de réponse de 3 à 5 secondes. Notez également les longueurs et le style des réponses sur la même invite.  

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

Comparé aux deux autres modèles abordés dans cette leçon, Mistral NeMo est le seul modèle gratuit avec une licence Apache2. 

Il est considéré comme une évolution du précédent LLM open source de Mistral, Mistral 7B. 

Certaines autres caractéristiques du modèle NeMo sont : 

- *Tokenisation plus efficace :* Ce modèle utilise le tokenizer Tekken au lieu du tiktoken plus communément utilisé. Cela permet de meilleures performances sur davantage de langues et de code. 

- *Affinage :* Le modèle de base est disponible pour un affinage. Cela permet plus de flexibilité pour les cas d'utilisation nécessitant un affinage. 

- *Appel de fonction natif* - Comme Mistral Large, ce modèle a été entraîné sur l'appel de fonction. Cela le rend unique en tant que l'un des premiers modèles open source à le faire. 


### Comparaison des tokenizers 

Dans cet exemple, nous verrons comment Mistral NeMo gère la tokenisation comparé à Mistral Large. 

Les deux exemples prennent la même invite mais vous devriez voir que NeMo retourne moins de tokens que Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importer les packages nécessaires :
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Charger le tokenizer Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniser une liste de messages
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
                                "description": "The temperature unit to use. Infer this from the user's location.",
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

# Compter le nombre de tokens
print(len(tokens))
```

```python
# Importer les packages nécessaires :
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Charger le tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniser une liste de messages
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
                                "description": "The temperature unit to use. Infer this from the user's location.",
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

# Compter le nombre de tokens
print(len(tokens))
```

## L'apprentissage ne s'arrête pas ici, continuez le voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage de l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à renforcer vos connaissances en IA générative !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->