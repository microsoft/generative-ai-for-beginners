<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T15:58:52+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "br"
}
-->
# Recuperação Aumentada por Geração (RAG) e Bancos de Dados Vetoriais

[![Recuperação Aumentada por Geração (RAG) e Bancos de Dados Vetoriais](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.br.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Na aula sobre aplicativos de busca, aprendemos brevemente como integrar seus próprios dados em Modelos de Linguagem Grande (LLMs). Nesta aula, vamos nos aprofundar nos conceitos de fundamentar seus dados em seu aplicativo LLM, na mecânica do processo e nos métodos para armazenar dados, incluindo embeddings e texto.

> **Vídeo em breve**

## Introdução

Nesta aula, abordaremos os seguintes tópicos:

- Uma introdução ao RAG, o que é e por que é usado em IA (inteligência artificial).

- Compreender o que são bancos de dados vetoriais e criar um para nosso aplicativo.

- Um exemplo prático de como integrar o RAG em um aplicativo.

## Objetivos de Aprendizagem

Após concluir esta aula, você será capaz de:

- Explicar a importância do RAG na recuperação e processamento de dados.

- Configurar um aplicativo RAG e fundamentar seus dados em um LLM.

- Integrar de forma eficaz o RAG e Bancos de Dados Vetoriais em aplicativos LLM.

## Nosso Cenário: aprimorando nossos LLMs com nossos próprios dados

Para esta aula, queremos adicionar nossas próprias anotações à startup de educação, permitindo que o chatbot obtenha mais informações sobre os diferentes assuntos. Usando as anotações que temos, os alunos poderão estudar melhor e entender os diferentes tópicos, facilitando a revisão para seus exames. Para criar nosso cenário, usaremos:

- `Azure OpenAI:` o LLM que usaremos para criar nosso chatbot.

- `Aula de IA para iniciantes sobre Redes Neurais:` este será o dado que fundamentaremos nosso LLM.

- `Azure AI Search` e `Azure Cosmos DB:` banco de dados vetorial para armazenar nossos dados e criar um índice de busca.

Os usuários poderão criar questionários práticos a partir de suas anotações, cartões de revisão e resumi-los em visões gerais concisas. Para começar, vamos entender o que é RAG e como funciona:

## Recuperação Aumentada por Geração (RAG)

Um chatbot alimentado por LLM processa os prompts dos usuários para gerar respostas. Ele é projetado para ser interativo e engajar os usuários em uma ampla gama de tópicos. No entanto, suas respostas são limitadas ao contexto fornecido e aos dados de treinamento fundamentais. Por exemplo, o conhecimento do GPT-4 tem um limite até setembro de 2021, o que significa que ele não possui informações sobre eventos que ocorreram após esse período. Além disso, os dados usados para treinar LLMs excluem informações confidenciais, como anotações pessoais ou o manual de produtos de uma empresa.

### Como funcionam os RAGs (Recuperação Aumentada por Geração)

![desenho mostrando como os RAGs funcionam](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.br.png)

Suponha que você queira implantar um chatbot que crie questionários a partir de suas anotações; será necessário uma conexão com a base de conhecimento. É aqui que o RAG entra em ação. Os RAGs operam da seguinte forma:

- **Base de conhecimento:** Antes da recuperação, esses documentos precisam ser ingeridos e pré-processados, geralmente dividindo grandes documentos em partes menores, transformando-os em embeddings de texto e armazenando-os em um banco de dados.

- **Consulta do usuário:** o usuário faz uma pergunta.

- **Recuperação:** Quando o usuário faz uma pergunta, o modelo de embedding recupera informações relevantes de nossa base de conhecimento para fornecer mais contexto que será incorporado ao prompt.

- **Geração Aumentada:** o LLM aprimora sua resposta com base nos dados recuperados. Isso permite que a resposta gerada seja baseada não apenas nos dados pré-treinados, mas também em informações relevantes do contexto adicionado. Os dados recuperados são usados para aumentar as respostas do LLM. O LLM então retorna uma resposta à pergunta do usuário.

![desenho mostrando a arquitetura dos RAGs](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.br.png)

A arquitetura dos RAGs é implementada usando transformers que consistem em duas partes: um codificador e um decodificador. Por exemplo, quando um usuário faz uma pergunta, o texto de entrada é 'codificado' em vetores que capturam o significado das palavras, e os vetores são 'decodificados' em nosso índice de documentos, gerando um novo texto com base na consulta do usuário. O LLM usa um modelo codificador-decodificador para gerar a saída.

Duas abordagens ao implementar RAG, de acordo com o artigo proposto: [Recuperação-Aumentada por Geração para Tarefas de NLP (Processamento de Linguagem Natural) Intensivas em Conhecimento](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst), são:

- **_RAG-Sequence_** usando documentos recuperados para prever a melhor resposta possível a uma consulta do usuário.

- **RAG-Token** usando documentos para gerar o próximo token e, em seguida, recuperá-los para responder à consulta do usuário.

### Por que usar RAGs?

- **Riqueza de informações:** garante que as respostas de texto estejam atualizadas e sejam atuais. Portanto, melhora o desempenho em tarefas específicas de domínio ao acessar a base de conhecimento interna.

- Reduz a fabricação utilizando **dados verificáveis** na base de conhecimento para fornecer contexto às consultas dos usuários.

- É **custo-efetivo**, pois é mais econômico em comparação com o ajuste fino de um LLM.

## Criando uma base de conhecimento

Nosso aplicativo é baseado em nossos dados pessoais, ou seja, a aula sobre Redes Neurais do currículo de IA para Iniciantes.

### Bancos de Dados Vetoriais

Um banco de dados vetorial, diferente dos bancos de dados tradicionais, é um banco de dados especializado projetado para armazenar, gerenciar e buscar vetores incorporados. Ele armazena representações numéricas de documentos. Dividir os dados em embeddings numéricos facilita para nosso sistema de IA entender e processar os dados.

Armazenamos nossos embeddings em bancos de dados vetoriais, pois os LLMs têm um limite no número de tokens que aceitam como entrada. Como você não pode passar todos os embeddings para um LLM, será necessário dividi-los em partes e, quando um usuário fizer uma pergunta, os embeddings mais semelhantes à pergunta serão retornados junto com o prompt. Dividir em partes também reduz os custos com o número de tokens passados por um LLM.

Alguns bancos de dados vetoriais populares incluem Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Você pode criar um modelo Azure Cosmos DB usando Azure CLI com o seguinte comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto para embeddings

Antes de armazenar nossos dados, precisaremos convertê-los em embeddings vetoriais antes de armazená-los no banco de dados. Se você estiver trabalhando com documentos grandes ou textos longos, pode dividi-los com base nas consultas que espera. A divisão pode ser feita no nível da frase ou no nível do parágrafo. Como a divisão deriva significados das palavras ao seu redor, você pode adicionar algum outro contexto a uma parte, por exemplo, adicionando o título do documento ou incluindo algum texto antes ou depois da parte. Você pode dividir os dados da seguinte forma:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Uma vez divididos, podemos então incorporar nosso texto usando diferentes modelos de embedding. Alguns modelos que você pode usar incluem: word2vec, ada-002 da OpenAI, Azure Computer Vision e muitos outros. A escolha do modelo dependerá dos idiomas que você está usando, do tipo de conteúdo codificado (texto/imagens/áudio), do tamanho da entrada que ele pode codificar e do comprimento da saída de embedding.

Um exemplo de texto incorporado usando o modelo `text-embedding-ada-002` da OpenAI é:
![um embedding da palavra gato](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.br.png)

## Recuperação e Busca Vetorial

Quando um usuário faz uma pergunta, o recuperador a transforma em um vetor usando o codificador de consulta, e então busca em nosso índice de busca de documentos por vetores relevantes no documento que estão relacionados à entrada. Uma vez feito, ele converte tanto o vetor de entrada quanto os vetores do documento em texto e os passa pelo LLM.

### Recuperação

A recuperação ocorre quando o sistema tenta encontrar rapidamente os documentos do índice que atendem aos critérios de busca. O objetivo do recuperador é obter documentos que serão usados para fornecer contexto e fundamentar o LLM em seus dados.

Existem várias maneiras de realizar buscas dentro de nosso banco de dados, como:

- **Busca por palavras-chave** - usada para buscas de texto.

- **Busca semântica** - usa o significado semântico das palavras.

- **Busca vetorial** - converte documentos de texto para representações vetoriais usando modelos de embedding. A recuperação será feita consultando os documentos cujas representações vetoriais estão mais próximas da pergunta do usuário.

- **Híbrido** - uma combinação de busca por palavras-chave e busca vetorial.

Um desafio com a recuperação surge quando não há resposta semelhante à consulta no banco de dados; o sistema então retorna as melhores informações que pode obter. No entanto, você pode usar táticas como configurar a distância máxima para relevância ou usar busca híbrida que combina palavras-chave e busca vetorial. Nesta aula, usaremos busca híbrida, uma combinação de busca vetorial e por palavras-chave. Armazenaremos nossos dados em um dataframe com colunas contendo as partes e os embeddings.

### Similaridade Vetorial

O recuperador buscará na base de conhecimento por embeddings que estão próximos, os vizinhos mais próximos, pois são textos semelhantes. No cenário em que um usuário faz uma consulta, ela é primeiro incorporada e depois combinada com embeddings semelhantes. A medida comum usada para encontrar a similaridade entre diferentes vetores é a similaridade cosseno, que é baseada no ângulo entre dois vetores.

Podemos medir a similaridade usando outras alternativas, como distância Euclidiana, que é a linha reta entre os pontos finais dos vetores, e produto escalar, que mede a soma dos produtos dos elementos correspondentes de dois vetores.

### Índice de Busca

Ao realizar a recuperação, precisaremos construir um índice de busca para nossa base de conhecimento antes de realizar a busca. Um índice armazenará nossos embeddings e poderá recuperar rapidamente as partes mais semelhantes, mesmo em um banco de dados grande. Podemos criar nosso índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Reclassificação

Depois de consultar o banco de dados, pode ser necessário classificar os resultados do mais relevante. Um LLM de reclassificação utiliza aprendizado de máquina para melhorar a relevância dos resultados de busca, ordenando-os do mais relevante. Usando Azure AI Search, a reclassificação é feita automaticamente para você usando um reclassificador semântico. Um exemplo de como a reclassificação funciona usando vizinhos mais próximos:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Juntando tudo

O último passo é adicionar nosso LLM à mistura para obter respostas fundamentadas em nossos dados. Podemos implementá-lo da seguinte forma:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Avaliando nosso aplicativo

### Métricas de Avaliação

- Qualidade das respostas fornecidas, garantindo que soem naturais, fluentes e humanas.

- Fundamentação dos dados: avaliando se a resposta veio dos documentos fornecidos.

- Relevância: avaliando se a resposta corresponde e está relacionada à pergunta feita.

- Fluência: verificando se a resposta faz sentido gramaticalmente.

## Casos de Uso para RAG (Recuperação Aumentada por Geração) e Bancos de Dados Vetoriais

Existem muitos casos de uso diferentes onde chamadas de função podem melhorar seu aplicativo, como:

- Perguntas e Respostas: fundamentando os dados da sua empresa em um chat que pode ser usado por funcionários para fazer perguntas.

- Sistemas de Recomendação: onde você pode criar um sistema que combina os valores mais semelhantes, como filmes, restaurantes e muitos outros.

- Serviços de Chatbot: você pode armazenar o histórico de chat e personalizar a conversa com base nos dados do usuário.

- Busca de imagens baseada em embeddings vetoriais, útil ao realizar reconhecimento de imagens e detecção de anomalias.

## Resumo

Cobrimos as áreas fundamentais do RAG, desde adicionar nossos dados ao aplicativo, a consulta do usuário e a saída. Para simplificar a criação de RAG, você pode usar frameworks como Semantic Kernel, Langchain ou Autogen.

## Tarefa

Para continuar seu aprendizado sobre Recuperação Aumentada por Geração (RAG), você pode construir:

- Um front-end para o aplicativo usando o framework de sua escolha.

- Utilizar um framework, seja LangChain ou Semantic Kernel, e recriar seu aplicativo.

Parabéns por concluir a aula 👏.

## O aprendizado não para por aqui, continue a jornada

Após concluir esta aula, confira nossa [coleção de aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.