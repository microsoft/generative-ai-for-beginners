<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:55:57+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "br"
}
-->
# Construindo com Modelos Mistral

## Introdução

Esta lição abordará:
- Explorar os diferentes Modelos Mistral
- Compreender os casos de uso e cenários para cada modelo
- Exemplos de código mostram as características únicas de cada modelo.

## Os Modelos Mistral

Nesta lição, exploraremos 3 modelos Mistral diferentes:
**Mistral Large**, **Mistral Small** e **Mistral Nemo**.

Cada um desses modelos está disponível gratuitamente no mercado de Modelos do Github. O código neste notebook usará esses modelos para executar o código. Aqui estão mais detalhes sobre como usar os Modelos do Github para [prototipar com modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 é atualmente o modelo principal da Mistral e é projetado para uso empresarial.

O modelo é uma atualização do Mistral Large original, oferecendo
- Janela de Contexto Maior - 128k vs 32k
- Melhor desempenho em Tarefas de Matemática e Codificação - 76,9% de precisão média vs 60,4%
- Aumento do desempenho multilíngue - idiomas incluem: Inglês, Francês, Alemão, Espanhol, Italiano, Português, Holandês, Russo, Chinês, Japonês, Coreano, Árabe e Hindi.

Com esses recursos, o Mistral Large se destaca em
- *Geração Aumentada por Recuperação (RAG)* - devido à janela de contexto maior
- *Chamada de Função* - este modelo possui chamada de função nativa que permite integração com ferramentas e APIs externas. Essas chamadas podem ser feitas tanto em paralelo quanto em sequência.
- *Geração de Código* - este modelo se destaca na geração de Python, Java, TypeScript e C++.

### Exemplo de RAG usando Mistral Large 2

Neste exemplo, estamos usando o Mistral Large 2 para executar um padrão RAG sobre um documento de texto. A pergunta é escrita em coreano e pergunta sobre as atividades do autor antes da faculdade.

Ele usa o Modelo de Embeddings Cohere para criar embeddings do documento de texto, bem como da pergunta. Para este exemplo, ele usa o pacote Python faiss como um armazenamento de vetores.

O prompt enviado ao modelo Mistral inclui tanto as perguntas quanto os trechos recuperados que são semelhantes à pergunta. O Modelo então fornece uma resposta em linguagem natural.

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

Mistral Small é outro modelo da família de modelos Mistral na categoria premier/enterprise. Como o nome sugere, este modelo é um Modelo de Linguagem Pequeno (SLM). As vantagens de usar o Mistral Small são que ele é:
- Econômico em comparação com os LLMs da Mistral, como o Mistral Large e o NeMo - redução de preço de 80%
- Baixa latência - resposta mais rápida em comparação com os LLMs da Mistral
- Flexível - pode ser implantado em diferentes ambientes com menos restrições de recursos necessários.

Mistral Small é ótimo para:
- Tarefas baseadas em texto, como sumarização, análise de sentimento e tradução.
- Aplicações onde são feitas solicitações frequentes devido à sua eficácia em custos
- Tarefas de código de baixa latência, como revisão e sugestões de código

## Comparando Mistral Small e Mistral Large

Para mostrar as diferenças de latência entre o Mistral Small e o Large, execute as células abaixo.

Você deve ver uma diferença nos tempos de resposta entre 3-5 segundos. Observe também os comprimentos e o estilo das respostas para o mesmo prompt.

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

Comparado aos outros dois modelos discutidos nesta lição, o Mistral NeMo é o único modelo gratuito com uma Licença Apache2.

Ele é visto como uma atualização do LLM de código aberto anterior da Mistral, o Mistral 7B.

Outros recursos do modelo NeMo são:

- *Tokenização mais eficiente:* Este modelo usa o tokenizador Tekken em vez do mais comumente usado tiktoken. Isso permite um melhor desempenho em mais idiomas e códigos.

- *Ajuste fino:* O modelo base está disponível para ajuste fino. Isso permite mais flexibilidade para casos de uso onde o ajuste fino pode ser necessário.

- *Chamada de Função Nativa* - Assim como o Mistral Large, este modelo foi treinado em chamada de função. Isso o torna único como um dos primeiros modelos de código aberto a fazer isso.

### Comparando Tokenizadores

Neste exemplo, veremos como o Mistral NeMo lida com a tokenização em comparação com o Mistral Large.

Ambos os exemplos usam o mesmo prompt, mas você deve ver que o NeMo retorna menos tokens em comparação com o Mistral Large.

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

## O aprendizado não para aqui, continue a Jornada

Após concluir esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.