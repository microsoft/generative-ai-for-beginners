# Construir com os Modelos Mistral 

## Introdução 

Esta lição irá cobrir: 
- Explorar os diferentes Modelos Mistral 
- Compreender os casos de uso e cenários para cada modelo 
- Explorar exemplos de código que mostram as características únicas de cada modelo. 

## Os Modelos Mistral 

Nesta lição, vamos explorar 3 modelos diferentes da Mistral: 
**Mistral Large**, **Mistral Small** e **Mistral Nemo**. 

Cada um destes modelos está disponível gratuitamente em [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). O código neste caderno irá usar estes modelos para executar o código.

> **Nota:** Os Modelos GitHub serão descontinuados no final de julho de 2026. Aqui estão mais detalhes sobre como usar [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para prototipar com modelos de IA. 


## Mistral Large 2 (2407)
O Mistral Large 2 é atualmente o modelo principal da Mistral e é concebido para uso empresarial. 

O modelo é uma atualização do original Mistral Large, oferecendo 
- Janela de Contexto Maior - 128k vs 32k 
- Melhor desempenho em Tarefas de Matemática e Codificação - 76.9% de precisão média vs 60.4% 
- Maior desempenho multilingue - línguas incluem: Inglês, Francês, Alemão, Espanhol, Italiano, Português, Holandês, Russo, Chinês, Japonês, Coreano, Árabe e Hindi.

Com estas características, o Mistral Large destaca-se em 
- *Geração Aumentada por Recuperação (RAG)* - devido à maior janela de contexto
- *Chamada de Função* - este modelo tem chamada de função nativa que permite integração com ferramentas externas e APIs. Estas chamadas podem ser feitas em paralelo ou sequencialmente uma após outra. 
- *Geração de Código* - este modelo é excelente na geração em Python, Java, TypeScript e C++. 

### Exemplo RAG usando Mistral Large 2 

Neste exemplo, estamos a usar o Mistral Large 2 para executar um padrão RAG sobre um documento de texto. A pergunta está escrita em coreano e questiona sobre as atividades do autor antes da universidade. 

Usa o Modelo de Embeddings Cohere para criar embeddings do documento de texto bem como da pergunta. Para este exemplo, usa o pacote Python faiss como loja de vetores. 

O prompt enviado ao modelo Mistral inclui tanto as perguntas como os fragmentos recuperados que são semelhantes à pergunta. O modelo fornece então uma resposta em linguagem natural. 

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

# Obtenha estes da página "Visão geral" do seu projeto Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distância, índice
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
O Mistral Small é outro modelo da família Mistral na categoria premier/empresarial. Como o nome indica, este modelo é um Modelo de Linguagem Pequeno (SLM). As vantagens de usar o Mistral Small são que ele é: 
- De redução de custos comparado com LLMs Mistral como Mistral Large e NeMo - redução de preço de 80%
- Baixa latência - resposta mais rápida comparado com os LLMs da Mistral
- Flexível - pode ser implementado em diferentes ambientes com menos restrições nos recursos necessários. 


O Mistral Small é excelente para: 
- Tarefas baseadas em texto como sumarização, análise de sentimento e tradução. 
- Aplicações onde pedidos frequentes são feitos devido à sua eficácia em custo 
- Tarefas de código de baixa latência como revisão e sugestões de código 

## Comparando Mistral Small e Mistral Large 

Para mostrar as diferenças de latência entre o Mistral Small e o Large, execute as células abaixo. 

Deve ver uma diferença nos tempos de resposta entre 3-5 segundos. Note também os comprimentos e estilo das respostas com o mesmo prompt.  

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

Comparado com os outros dois modelos discutidos nesta lição, o Mistral NeMo é o único modelo gratuito com Licença Apache2. 

É visto como uma atualização do anterior LLM open source da Mistral, o Mistral 7B. 

Algumas outras características do modelo NeMo são: 

- *Tokenização mais eficiente:* Este modelo usa o tokenizer Tekken em vez do mais comum tiktoken. Isto permite melhor desempenho em mais línguas e código. 

- *Ajuste Fino:* O modelo base está disponível para ajuste fino. Isto permite maior flexibilidade para casos de uso onde o ajuste fino pode ser necessário. 

- *Chamada Nativa de Função* - Como o Mistral Large, este modelo foi treinado para chamada de função. Isto torna-o único como um dos primeiros modelos open source a fazê-lo. 


### Comparando Tokenizadores 

Neste exemplo, vamos ver como o Mistral NeMo trata a tokenização comparado com o Mistral Large. 

Ambos os exemplos usam o mesmo prompt, mas deve notar que o NeMo retorna menos tokens que o Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importar os pacotes necessários:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Carregar o tokenizer Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizar uma lista de mensagens
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

# Contar o número de tokens
print(len(tokens))
```

```python
# Importar pacotes necessários:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Carregar o tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizar uma lista de mensagens
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

# Contar o número de tokens
print(len(tokens))
```

## A aprendizagem não termina aqui, continue a jornada

Depois de completar esta lição, veja a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar os seus conhecimentos sobre IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->