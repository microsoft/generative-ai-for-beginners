<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:59:11+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "br"
}
-->
# Construindo com Modelos Mistral

## Introdução

Esta lição abordará:  
- Exploração dos diferentes Modelos Mistral  
- Compreensão dos casos de uso e cenários para cada modelo  
- Exemplos de código que mostram as características únicas de cada modelo.

## Os Modelos Mistral

Nesta lição, exploraremos 3 modelos diferentes da Mistral:  
**Mistral Large**, **Mistral Small** e **Mistral Nemo**.

Cada um desses modelos está disponível gratuitamente no marketplace de Modelos do Github. O código deste notebook usará esses modelos para executar os exemplos. Aqui estão mais detalhes sobre como usar os Modelos do Github para [prototipar com modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
O Mistral Large 2 é atualmente o modelo principal da Mistral e foi projetado para uso empresarial.

O modelo é uma evolução do Mistral Large original, oferecendo:  
- Janela de contexto maior - 128k contra 32k  
- Melhor desempenho em tarefas de Matemática e Programação - 76,9% de precisão média contra 60,4%  
- Maior desempenho multilíngue - idiomas incluem: inglês, francês, alemão, espanhol, italiano, português, holandês, russo, chinês, japonês, coreano, árabe e hindi.

Com essas características, o Mistral Large se destaca em:  
- *Retrieval Augmented Generation (RAG)* - devido à janela de contexto maior  
- *Function Calling* - este modelo possui chamadas de função nativas que permitem integração com ferramentas e APIs externas. Essas chamadas podem ser feitas em paralelo ou sequencialmente.  
- *Geração de Código* - este modelo se destaca na geração de código em Python, Java, TypeScript e C++.

### Exemplo de RAG usando Mistral Large 2

Neste exemplo, usamos o Mistral Large 2 para executar um padrão RAG sobre um documento de texto. A pergunta está escrita em coreano e questiona sobre as atividades do autor antes da faculdade.

Ele utiliza o Modelo de Embeddings Cohere para criar embeddings do documento de texto e da pergunta. Para este exemplo, é usado o pacote Python faiss como armazenamento vetorial.

O prompt enviado ao modelo Mistral inclui tanto as perguntas quanto os trechos recuperados que são semelhantes à pergunta. O modelo então fornece uma resposta em linguagem natural.

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
O Mistral Small é outro modelo da família Mistral, dentro da categoria premier/enterprise. Como o nome sugere, este é um Modelo de Linguagem Pequeno (SLM). As vantagens de usar o Mistral Small são:  
- Economia de custo em comparação com LLMs Mistral como Mistral Large e NeMo - redução de preço de 80%  
- Baixa latência - resposta mais rápida em comparação com os LLMs da Mistral  
- Flexível - pode ser implantado em diferentes ambientes com menos restrições quanto aos recursos necessários.

O Mistral Small é ideal para:  
- Tarefas baseadas em texto, como sumarização, análise de sentimento e tradução.  
- Aplicações que fazem requisições frequentes devido à sua relação custo-benefício  
- Tarefas de código com baixa latência, como revisão e sugestões de código

## Comparando Mistral Small e Mistral Large

Para mostrar as diferenças de latência entre Mistral Small e Large, execute as células abaixo.

Você deverá notar uma diferença no tempo de resposta entre 3 a 5 segundos. Também observe os comprimentos e o estilo das respostas para o mesmo prompt.

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

Comparado aos outros dois modelos discutidos nesta lição, o Mistral NeMo é o único modelo gratuito com licença Apache2.

Ele é visto como uma evolução do LLM open source anterior da Mistral, o Mistral 7B.

Algumas outras características do modelo NeMo são:

- *Tokenização mais eficiente:* Este modelo usa o tokenizador Tekken em vez do mais comum tiktoken. Isso permite melhor desempenho em mais idiomas e códigos.

- *Finetuning:* O modelo base está disponível para ajuste fino. Isso oferece mais flexibilidade para casos de uso que necessitam de finetuning.

- *Function Calling nativo* - Assim como o Mistral Large, este modelo foi treinado para chamadas de função. Isso o torna único como um dos primeiros modelos open source a oferecer essa funcionalidade.

### Comparando Tokenizadores

Neste exemplo, veremos como o Mistral NeMo lida com a tokenização em comparação com o Mistral Large.

Ambos os exemplos usam o mesmo prompt, mas você deverá perceber que o NeMo retorna menos tokens em relação ao Mistral Large.

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

## O aprendizado não para aqui, continue a jornada

Após concluir esta lição, confira nossa [coleção de Aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seus conhecimentos em IA Generativa!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.