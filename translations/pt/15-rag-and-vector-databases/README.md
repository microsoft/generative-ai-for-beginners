<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-18T00:39:50+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "pt"
}
-->
# Geração Aumentada por Recuperação (RAG) e Bases de Dados Vetoriais

[![Geração Aumentada por Recuperação (RAG) e Bases de Dados Vetoriais](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.pt.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Na lição sobre aplicações de pesquisa, aprendemos brevemente como integrar os seus próprios dados em Modelos de Linguagem de Grande Escala (LLMs). Nesta lição, vamos explorar mais profundamente os conceitos de fundamentar os seus dados na aplicação de LLM, os mecanismos do processo e os métodos para armazenar dados, incluindo embeddings e texto.

> **Vídeo em breve**

## Introdução

Nesta lição, abordaremos os seguintes tópicos:

- Uma introdução ao RAG, o que é e por que é usado em IA (inteligência artificial).

- Compreender o que são bases de dados vetoriais e criar uma para a nossa aplicação.

- Um exemplo prático de como integrar o RAG numa aplicação.

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

- Explicar a importância do RAG na recuperação e processamento de dados.

- Configurar uma aplicação RAG e fundamentar os seus dados num LLM.

- Integrar eficazmente RAG e Bases de Dados Vetoriais em aplicações de LLM.

## O Nosso Cenário: melhorar os nossos LLMs com os nossos próprios dados

Para esta lição, queremos adicionar as nossas próprias notas à startup de educação, permitindo que o chatbot obtenha mais informações sobre os diferentes assuntos. Usando as notas que temos, os alunos poderão estudar melhor e compreender os diferentes tópicos, facilitando a revisão para os seus exames. Para criar o nosso cenário, utilizaremos:

- `Azure OpenAI:` o LLM que usaremos para criar o nosso chatbot.

- `Lição de IA para iniciantes sobre Redes Neurais:` este será o dado que fundamentaremos no nosso LLM.

- `Azure AI Search` e `Azure Cosmos DB:` base de dados vetorial para armazenar os nossos dados e criar um índice de pesquisa.

Os utilizadores poderão criar questionários de prática a partir das suas notas, cartões de revisão e resumi-los em visões gerais concisas. Para começar, vejamos o que é o RAG e como funciona:

## Geração Aumentada por Recuperação (RAG)

Um chatbot alimentado por LLM processa os prompts dos utilizadores para gerar respostas. Ele é projetado para ser interativo e engajar-se com os utilizadores em uma ampla gama de tópicos. No entanto, as suas respostas são limitadas ao contexto fornecido e aos dados de treino fundamentais. Por exemplo, o conhecimento do GPT-4 tem um limite até setembro de 2021, o que significa que não possui informações sobre eventos que ocorreram após esse período. Além disso, os dados usados para treinar os LLMs excluem informações confidenciais, como notas pessoais ou manuais de produtos de uma empresa.

### Como funcionam os RAGs (Geração Aumentada por Recuperação)

![desenho mostrando como funcionam os RAGs](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.pt.png)

Suponha que deseja implementar um chatbot que cria questionários a partir das suas notas; será necessário uma conexão com a base de conhecimento. É aqui que o RAG entra em ação. Os RAGs operam da seguinte forma:

- **Base de conhecimento:** Antes da recuperação, esses documentos precisam ser ingeridos e pré-processados, normalmente dividindo documentos grandes em pedaços menores, transformando-os em embeddings de texto e armazenando-os numa base de dados.

- **Consulta do utilizador:** o utilizador faz uma pergunta.

- **Recuperação:** Quando o utilizador faz uma pergunta, o modelo de embedding recupera informações relevantes da nossa base de conhecimento para fornecer mais contexto que será incorporado ao prompt.

- **Geração Aumentada:** o LLM melhora a sua resposta com base nos dados recuperados. Isso permite que a resposta gerada não seja apenas baseada nos dados pré-treinados, mas também em informações relevantes do contexto adicionado. Os dados recuperados são usados para aumentar as respostas do LLM. O LLM então retorna uma resposta à pergunta do utilizador.

![desenho mostrando a arquitetura dos RAGs](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.pt.png)

A arquitetura dos RAGs é implementada usando transformadores que consistem em duas partes: um codificador e um decodificador. Por exemplo, quando um utilizador faz uma pergunta, o texto de entrada é 'codificado' em vetores que capturam o significado das palavras, e os vetores são 'decodificados' no nosso índice de documentos, gerando um novo texto com base na consulta do utilizador. O LLM utiliza tanto o modelo codificador-decodificador para gerar a saída.

Duas abordagens ao implementar RAG, de acordo com o artigo proposto: [Geração Aumentada por Recuperação para Tarefas de NLP (Processamento de Linguagem Natural) Intensivas em Conhecimento](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst), são:

- **_RAG-Sequence_** usando documentos recuperados para prever a melhor resposta possível a uma consulta do utilizador.

- **RAG-Token** usando documentos para gerar o próximo token e, em seguida, recuperá-los para responder à consulta do utilizador.

### Por que usar RAGs?

- **Riqueza de informações:** garante que as respostas textuais estejam atualizadas e sejam atuais. Portanto, melhora o desempenho em tarefas específicas de domínio ao acessar a base de conhecimento interna.

- Reduz a fabricação utilizando **dados verificáveis** na base de conhecimento para fornecer contexto às consultas dos utilizadores.

- É **custo-efetivo**, pois é mais econômico em comparação com o ajuste fino de um LLM.

## Criando uma base de conhecimento

A nossa aplicação é baseada nos nossos dados pessoais, ou seja, a lição sobre Redes Neurais do currículo de IA para Iniciantes.

### Bases de Dados Vetoriais

Uma base de dados vetorial, ao contrário das bases de dados tradicionais, é uma base de dados especializada projetada para armazenar, gerir e pesquisar vetores incorporados. Ela armazena representações numéricas de documentos. Dividir os dados em embeddings numéricos facilita a compreensão e o processamento dos dados pelo nosso sistema de IA.

Armazenamos os nossos embeddings em bases de dados vetoriais, pois os LLMs têm um limite no número de tokens que aceitam como entrada. Como não é possível passar todos os embeddings para um LLM, será necessário dividi-los em pedaços e, quando um utilizador fizer uma pergunta, os embeddings mais semelhantes à pergunta serão retornados juntamente com o prompt. Dividir em pedaços também reduz os custos com o número de tokens processados por um LLM.

Algumas bases de dados vetoriais populares incluem Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Pode criar um modelo Azure Cosmos DB usando o Azure CLI com o seguinte comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto para embeddings

Antes de armazenar os nossos dados, será necessário convertê-los em embeddings vetoriais antes de serem armazenados na base de dados. Se estiver a trabalhar com documentos grandes ou textos longos, pode dividi-los com base nas consultas que espera. A divisão pode ser feita ao nível da frase ou do parágrafo. Como a divisão deriva significados das palavras ao seu redor, pode adicionar algum outro contexto a um pedaço, por exemplo, adicionando o título do documento ou incluindo algum texto antes ou depois do pedaço. Pode dividir os dados da seguinte forma:

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

Uma vez divididos, podemos então incorporar o nosso texto usando diferentes modelos de embedding. Alguns modelos que pode usar incluem: word2vec, ada-002 da OpenAI, Azure Computer Vision e muitos mais. A seleção de um modelo dependerá dos idiomas que está a usar, do tipo de conteúdo codificado (texto/imagens/áudio), do tamanho da entrada que pode codificar e da extensão da saída de embedding.

Um exemplo de texto incorporado usando o modelo `text-embedding-ada-002` da OpenAI é:
![um embedding da palavra gato](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.pt.png)

## Recuperação e Pesquisa Vetorial

Quando um utilizador faz uma pergunta, o recuperador transforma-a num vetor usando o codificador de consulta, depois pesquisa no nosso índice de pesquisa de documentos por vetores relevantes no documento que estão relacionados à entrada. Uma vez concluído, converte tanto o vetor de entrada quanto os vetores do documento em texto e passa-os pelo LLM.

### Recuperação

A recuperação ocorre quando o sistema tenta encontrar rapidamente os documentos do índice que satisfazem os critérios de pesquisa. O objetivo do recuperador é obter documentos que serão usados para fornecer contexto e fundamentar o LLM nos seus dados.

Existem várias maneiras de realizar pesquisas na nossa base de dados, como:

- **Pesquisa por palavras-chave** - usada para pesquisas de texto.

- **Pesquisa semântica** - utiliza o significado semântico das palavras.

- **Pesquisa vetorial** - converte documentos de texto para representações vetoriais usando modelos de embedding. A recuperação será feita consultando os documentos cujas representações vetoriais sejam mais próximas da pergunta do utilizador.

- **Híbrida** - uma combinação de pesquisa por palavras-chave e pesquisa vetorial.

Um desafio com a recuperação surge quando não há uma resposta semelhante à consulta na base de dados; o sistema então retorna as melhores informações que consegue encontrar. No entanto, pode usar táticas como definir a distância máxima para relevância ou usar pesquisa híbrida que combina palavras-chave e pesquisa vetorial. Nesta lição, usaremos pesquisa híbrida, uma combinação de pesquisa vetorial e por palavras-chave. Armazenaremos os nossos dados num dataframe com colunas contendo os pedaços, bem como os embeddings.

### Similaridade Vetorial

O recuperador pesquisará na base de dados de conhecimento por embeddings que estejam próximos uns dos outros, os vizinhos mais próximos, pois são textos semelhantes. No cenário em que um utilizador faz uma consulta, ela é primeiro incorporada e depois combinada com embeddings semelhantes. A medida comum usada para encontrar a semelhança entre diferentes vetores é a similaridade cosseno, que se baseia no ângulo entre dois vetores.

Podemos medir a similaridade usando outras alternativas, como a distância euclidiana, que é a linha reta entre os pontos finais dos vetores, e o produto escalar, que mede a soma dos produtos dos elementos correspondentes de dois vetores.

### Índice de Pesquisa

Ao realizar a recuperação, será necessário construir um índice de pesquisa para a nossa base de conhecimento antes de realizar a pesquisa. Um índice armazenará os nossos embeddings e poderá recuperar rapidamente os pedaços mais semelhantes, mesmo numa base de dados grande. Podemos criar o nosso índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Reclassificação

Depois de consultar a base de dados, pode ser necessário ordenar os resultados dos mais relevantes. Um LLM de reclassificação utiliza Machine Learning para melhorar a relevância dos resultados de pesquisa, ordenando-os dos mais relevantes. Usando o Azure AI Search, a reclassificação é feita automaticamente para si usando um reclassificador semântico. Um exemplo de como a reclassificação funciona usando vizinhos mais próximos:

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

O último passo é adicionar o nosso LLM à mistura para conseguir obter respostas fundamentadas nos nossos dados. Podemos implementá-lo da seguinte forma:

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

## Avaliando a nossa aplicação

### Métricas de Avaliação

- Qualidade das respostas fornecidas, garantindo que soem naturais, fluentes e humanas.

- Fundamentação dos dados: avaliar se a resposta veio dos documentos fornecidos.

- Relevância: avaliar se a resposta corresponde e está relacionada à pergunta feita.

- Fluência - verificar se a resposta faz sentido gramaticalmente.

## Casos de Uso para RAG (Geração Aumentada por Recuperação) e bases de dados vetoriais

Existem muitos casos de uso diferentes onde chamadas de função podem melhorar a sua aplicação, como:

- Perguntas e Respostas: fundamentar os dados da sua empresa num chat que pode ser usado pelos funcionários para fazer perguntas.

- Sistemas de Recomendação: onde pode criar um sistema que combine os valores mais semelhantes, como filmes, restaurantes e muitos mais.

- Serviços de Chatbot: pode armazenar o histórico de chat e personalizar a conversa com base nos dados do utilizador.

- Pesquisa de imagens baseada em embeddings vetoriais, útil ao realizar reconhecimento de imagens e deteção de anomalias.

## Resumo

Cobrimos as áreas fundamentais do RAG, desde adicionar os nossos dados à aplicação, a consulta do utilizador e a saída. Para simplificar a criação de RAG, pode usar frameworks como Semantic Kernel, Langchain ou Autogen.

## Tarefa

Para continuar a sua aprendizagem sobre Geração Aumentada por Recuperação (RAG), pode construir:

- Criar um front-end para a aplicação usando o framework da sua escolha.

- Utilizar um framework, seja LangChain ou Semantic Kernel, e recriar a sua aplicação.

Parabéns por completar a lição 👏.

## A aprendizagem não termina aqui, continue a jornada

Após completar esta lição, confira a nossa [coleção de aprendizagem de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprofundar os seus conhecimentos sobre IA generativa!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.