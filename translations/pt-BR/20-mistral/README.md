# Construindo com Modelos Mistral

## Introdução

Esta lição abordará:
- Explorando os diferentes Modelos Mistral
- Entendendo os casos de uso e cenários para cada modelo
- Explorando exemplos de código que mostram as características únicas de cada modelo.

## Os Modelos Mistral

Nesta lição, exploraremos 3 diferentes modelos Mistral:
**Mistral Large**, **Mistral Small** e **Mistral Nemo**.

Cada um desses modelos está disponível gratuitamente em [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). O código neste notebook usará esses modelos para executar o código.

> **Nota:** o GitHub Models será desativado no final de julho de 2026. Aqui estão mais detalhes sobre o uso dos [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para prototipagem com modelos de IA.


## Mistral Large 2 (2407)
Mistral Large 2 é atualmente o modelo principal da Mistral e é projetado para uso empresarial.

O modelo é uma atualização do Mistral Large original, oferecendo
- Janela de contexto maior - 128k vs 32k
- Melhor desempenho em tarefas de matemática e programação - 76,9% de precisão média vs 60,4%
- Maior desempenho multilíngue - idiomas incluem: inglês, francês, alemão, espanhol, italiano, português, holandês, russo, chinês, japonês, coreano, árabe e hindi.

Com essas características, o Mistral Large se destaca em
- *Geração aumentada por recuperação (RAG)* - devido à janela de contexto maior
- *Chamada de Função* - este modelo possui chamada de função nativa, o que permite integração com ferramentas externas e APIs. Essas chamadas podem ser feitas tanto em paralelo quanto sequencialmente.
- *Geração de Código* - este modelo se destaca na geração de Python, Java, TypeScript e C++.

### Exemplo de RAG usando Mistral Large 2

Neste exemplo, estamos usando o Mistral Large 2 para executar um padrão RAG sobre um documento de texto. A pergunta está escrita em coreano e pergunta sobre as atividades do autor antes da faculdade.

Ele usa o Modelo de Embeddings Cohere para criar embeddings do documento de texto, bem como da pergunta. Para este exemplo, usa o pacote faiss em Python como armazenamento vetorial.

O prompt enviado para o modelo Mistral inclui tanto a pergunta quanto os fragmentos recuperados que são semelhantes à pergunta. O modelo então fornece uma resposta em linguagem natural.

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

# Obtenha estes da página "Visão Geral" do seu projeto Microsoft Foundry
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
Mistral Small é outro modelo na família Mistral dentro da categoria premier/enterprise. Como o nome sugere, este é um Modelo de Linguagem Pequeno (SLM). As vantagens de usar o Mistral Small são:
- Economia de custo em comparação com LLMs Mistral como Mistral Large e NeMo - redução de preço de 80%
- Baixa latência - resposta mais rápida em comparação com os LLMs da Mistral
- Flexível - pode ser implantado em diferentes ambientes com menos restrições quanto aos recursos necessários.


Mistral Small é ideal para:
- Tarefas baseadas em texto como sumarização, análise de sentimento e tradução.
- Aplicações onde são feitas solicitações frequentes devido à sua relação custo-benefício
- Tarefas de código com baixa latência como revisão e sugestões de código

## Comparando Mistral Small e Mistral Large

Para mostrar as diferenças de latência entre Mistral Small e Large, execute as células abaixo.

Você deverá notar uma diferença no tempo de resposta entre 3-5 segundos. Também observe os comprimentos e estilos da resposta para o mesmo prompt.

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

Em comparação com os outros dois modelos discutidos nesta lição, o Mistral NeMo é o único modelo gratuito com licença Apache2.

É considerado uma atualização do primeiro LLM open source da Mistral, o Mistral 7B.

Algumas outras características do modelo NeMo são:

- *Tokenização mais eficiente:* Este modelo usa o tokenizador Tekken em vez do mais comumente usado tiktoken. Isso permite melhor desempenho em mais idiomas e código.

- *Ajuste fino (Finetuning):* O modelo base está disponível para ajuste fino. Isso permite mais flexibilidade para casos de uso onde o ajuste fino pode ser necessário.

- *Chamada de Função Nativa* - Como o Mistral Large, este modelo foi treinado em chamada de função. Isso o torna único, sendo um dos primeiros modelos open source a fazer isso.


### Comparando Tokenizadores

Neste exemplo, veremos como o Mistral NeMo trata a tokenização em comparação com o Mistral Large.

Ambos os exemplos usam o mesmo prompt, mas você deve ver que o NeMo retorna menos tokens que o Mistral Large.

```bash
pip install mistral-common
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

# Carregar o tokenizador Mistral

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

# Carregar tokenizador Mistral

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

## O aprendizado não para aqui, continue a jornada

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seus conhecimentos em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->