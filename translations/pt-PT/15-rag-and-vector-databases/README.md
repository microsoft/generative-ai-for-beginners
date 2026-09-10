# Geração Aumentada por Recuperação (RAG) e Bases de Dados Vetoriais

[![Geração Aumentada por Recuperação (RAG) e Bases de Dados Vetoriais](../../../translated_images/pt-PT/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Na lição de aplicações de pesquisa, aprendemos brevemente como integrar os seus próprios dados nos Grandes Modelos de Linguagem (LLMs). Nesta lição, aprofundaremos os conceitos de fundamentar os seus dados na sua aplicação LLM, a mecânica do processo e os métodos para armazenar dados, incluindo tanto embeddings como texto.

> **Vídeo em Breve**

## Introdução

Nesta lição vamos cobrir o seguinte:

- Uma introdução a RAG, o que é e por que é usada em IA (inteligência artificial).

- Compreender o que são bases de dados vetoriais e criar uma para a nossa aplicação.

- Um exemplo prático de como integrar RAG numa aplicação.

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

- Explicar a importância da RAG na recuperação e processamento de dados.

- Configurar uma aplicação RAG e fundamentar os seus dados num LLM

- Integração eficaz de RAG e Bases de Dados Vetoriais em Aplicações LLM.

## O Nosso Cenário: melhorar os nossos LLMs com os nossos próprios dados

Para esta lição, queremos adicionar as nossas próprias notas na startup de educação, que permite ao chatbot obter mais informações sobre os diferentes assuntos. Usando as notas que temos, os aprendizes poderão estudar melhor e entender os diversos tópicos, facilitando a revisão para os seus exames. Para criar o nosso cenário, iremos usar:

- `Azure OpenAI:` o LLM que usaremos para criar o nosso chatbot

- `Lição 'IA para Iniciantes' sobre Redes Neurais`: esses serão os dados em que fundamentamos o nosso LLM

- `Azure AI Search` e `Azure Cosmos DB:` base de dados vetorial para armazenar os nossos dados e criar um índice de pesquisa

Os usuários poderão criar quizzes práticos a partir das suas notas, cartões de revisão resumidos e sumarizá-los em visões concisas. Para começar, vejamos o que é RAG e como funciona:

## Geração Aumentada por Recuperação (RAG)

Um chatbot alimentado por um LLM processa prompts do usuário para gerar respostas. É projetado para ser interativo e envolver-se com os usuários numa ampla variedade de tópicos. Contudo, as suas respostas são limitadas ao contexto fornecido e aos seus dados base de treino. Por exemplo, o corte de conhecimento do GPT-4 é setembro de 2021, significando que não tem conhecimento de eventos ocorridos após esse período. Além disso, os dados usados para treinar LLMs excluem informações confidenciais, como notas pessoais ou manuais de produtos de uma empresa.

### Como funcionam os RAG (Geração Aumentada por Recuperação)

![desenho mostrando como funcionam os RAGs](../../../translated_images/pt-PT/how-rag-works.f5d0ff63942bd3a6.webp)

Suponha que pretende lançar um chatbot que cria quizzes a partir das suas notas, vai necessitar de uma conexão à base de conhecimento. É aqui que o RAG entra em ação. Os RAGs operam da seguinte forma:

- **Base de conhecimento:** Antes da recuperação, estes documentos precisam ser ingeridos e pré-processados, tipicamente dividindo documentos grandes em partes menores, transformando-os em embeddings de texto e armazenando-os numa base de dados.

- **Consulta do usuário:** o usuário faz uma pergunta

- **Recuperação:** Quando um usuário faz uma pergunta, o modelo de embedding recupera informações relevantes da nossa base de conhecimento para fornecer mais contexto que será incorporado no prompt.

- **Geração Aumentada:** o LLM aprimora a sua resposta com base nos dados recuperados. Isso permite que a resposta gerada não seja apenas baseada em dados pré-treinados, mas também em informação relevante do contexto adicional. Os dados recuperados são usados para aumentar as respostas do LLM. O LLM então retorna uma resposta à pergunta do usuário.

![desenho mostrando a arquitetura dos RAGs](../../../translated_images/pt-PT/encoder-decode.f2658c25d0eadee2.webp)

A arquitetura dos RAGs é implementada usando transformers consistindo em duas partes: um codificador e um decodificador. Por exemplo, quando um usuário faz uma pergunta, o texto de entrada é 'codificado' em vetores que capturam o significado das palavras e os vetores são 'decodificados' no nosso índice de documentos e geram novo texto baseado na consulta do usuário. O LLM usa um modelo encoder-decoder para gerar a saída.

Duas abordagens para implementar RAG segundo o paper proposto: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) são:

- **_RAG-Sequence_** usando documentos recuperados para prever a melhor resposta possível a uma consulta do usuário

- **RAG-Token** usando documentos para gerar o próximo token, depois recuperando-os para responder à consulta do usuário

### Por que usar RAGs?

- **Riqueza de informação:** assegura que as respostas textuais estão atualizadas e são atuais. Isso, portanto, melhora o desempenho em tarefas específicas de domínio ao aceder à base de conhecimento interna.

- Reduz a fabricação ao utilizar **dados verificáveis** na base de conhecimento para fornecer contexto às perguntas dos usuários.

- É **económico** pois são mais baratos comparados com o ajuste fino de um LLM

## Criar uma base de conhecimento

A nossa aplicação baseia-se nos nossos dados pessoais, ou seja, a lição de Redes Neurais no currículo IA para Iniciantes.

### Bases de Dados Vetoriais

Uma base de dados vetorial, ao contrário das bases tradicionais, é uma base especializada projetada para armazenar, gerir e pesquisar vetores embutidos. Armazena representações numéricas de documentos. Dividir dados em embeddings numéricos facilita a compreensão e processamento dos dados pelo nosso sistema de IA.

Armazenamos os nossos embeddings em bases de dados vetoriais pois os LLMs têm um limite no número de tokens que aceitam como entrada. Como não pode passar o embedding completo para um LLM, será necessário dividi-los em partes e, quando o usuário fazer uma pergunta, os embeddings mais semelhantes são retornados juntamente com o prompt. A segmentação também reduz custos no número de tokens passados por um LLM.

Algumas bases de dados vetoriais populares incluem Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Pode criar um modelo Azure Cosmos DB usando o Azure CLI com o seguinte comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto para embeddings

Antes de armazenar os dados, é necessário convertê-los em embeddings vetoriais antes de os guardar na base de dados. Se estiver a trabalhar com documentos grandes ou textos longos, pode dividi-los com base nas consultas que espera. A segmentação pode ser feita a nível de frase ou a nível de parágrafo. Como a segmentação deriva significado das palavras ao redor, pode adicionar outro contexto a um segmento, por exemplo, adicionando o título do documento ou incluindo algum texto antes ou depois do segmento. Pode segmentar os dados da seguinte forma:

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

    # Se o último pedaço não atingiu o comprimento mínimo, adicione-o na mesma
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Depois de segmentados, podemos embutir o nosso texto usando diferentes modelos de embedding. Alguns modelos que pode usar incluem: word2vec, ada-002 da OpenAI, Azure Computer Vision e muitos mais. A escolha do modelo dependerá das línguas que usa, do tipo de conteúdo codificado (texto/imagens/áudio), do tamanho da entrada que pode codificar e do comprimento da saída do embedding.

Um exemplo de texto embutido usando o modelo `text-embedding-ada-002` da OpenAI é:
![um embedding da palavra "cat"](../../../translated_images/pt-PT/cat.74cbd7946bc9ca38.webp)

## Recuperação e Pesquisa Vetorial

Quando um usuário faz uma pergunta, o retriever transforma-a num vetor usando o codificador de consulta, depois pesquisa no nosso índice de documentos por vetores relevantes relacionados com a entrada. Depois, converte tanto o vetor de entrada como os vetores do documento em texto e passa-os para o LLM.

### Recuperação

A recuperação acontece quando o sistema tenta encontrar rapidamente os documentos no índice que satisfazem os critérios de pesquisa. O objetivo do retriever é obter documentos que serão usados para fornecer contexto e fundamentar o LLM nos seus dados.

Existem várias formas de realizar a pesquisa dentro da nossa base de dados, tais como:

- **Pesquisa por palavra-chave** - usada para pesquisas textuais

- **Pesquisa vetorial** - converte documentos de texto para representações vetoriais usando modelos de embedding, permitindo uma **pesquisa semântica** usando o significado das palavras. A recuperação é feita consultando os documentos cujas representações vetoriais estão mais próximas da questão do usuário.

- **Híbrida** - uma combinação de pesquisa por palavra-chave e vetor.

Um desafio na recuperação ocorre quando não há uma resposta similar à consulta na base de dados, o sistema retorna então a melhor informação que conseguir, contudo, pode usar táticas como definir a distância máxima para relevância ou usar pesquisa híbrida que combina palavras-chave e pesquisa vetorial. Nesta lição, iremos usar pesquisa híbrida, uma combinação de pesquisa vetorial e por palavra-chave. Armazenaremos os nossos dados num dataframe com colunas contendo os segmentos assim como embeddings.

### Similaridade Vetorial

O retriever pesquisa na base de conhecimento por embeddings próximos uns dos outros, o vizinho mais próximo, pois são textos semelhantes. No cenário, quando um usuário faz uma consulta, ela é primeiro embutida e depois comparada com embeddings semelhantes. A medida comum usada para encontrar quão semelhantes são diferentes vetores é a similaridade do cosseno, que é baseada no ângulo entre dois vetores.

Podemos medir a similaridade usando outras alternativas, como a distância euclidiana, que é a linha reta entre os extremos dos vetores, e o produto escalar, que mede a soma dos produtos de elementos correspondentes de dois vetores.

### Índice de pesquisa

Ao fazer a recuperação, será necessário construir um índice de pesquisa para a nossa base de conhecimento antes de realizar a pesquisa. Um índice armazenará nossos embeddings e poderá recuperar rapidamente os segmentos mais semelhantes, mesmo numa base de dados grande. Podemos criar o nosso índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Criar o índice de pesquisa
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Para consultar o índice, pode usar o método kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Reclassificação

Depois de consultar a base de dados, poderá necessitar de ordenar os resultados do mais relevante. Um LLM de reclassificação utiliza Machine Learning para melhorar a relevância dos resultados da pesquisa ordenando-os do mais relevante. Usando Azure AI Search, a reclassificação é feita automaticamente para si usando um reclassificador semântico. Um exemplo de como a reclassificação funciona usando vizinhos mais próximos:

```python
# Encontrar os documentos mais semelhantes
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Imprimir os documentos mais semelhantes
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

O último passo é adicionar o nosso LLM à mistura para poder obter respostas fundamentadas nos nossos dados. Podemos implementar da seguinte forma:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Converter a pergunta num vetor de consulta
    query_vector = create_embeddings(user_input)

    # Encontrar os documentos mais semelhantes
    distances, indices = nbrs.kneighbors([query_vector])

    # adicionar documentos à consulta para fornecer contexto
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combinar o histórico e a entrada do utilizador
    history.append(user_input)

    # criar um objeto de mensagem
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # usar a API de Respostas para gerar uma resposta
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Avaliar a nossa aplicação

### Métricas de Avaliação

- Qualidade das respostas fornecidas garantindo que soam naturais, fluentes e parecidas com humanos

- Fundamentação dos dados: avaliar se a resposta veio dos documentos fornecidos

- Relevância: avaliar se a resposta corresponde e está relacionada à pergunta feita

- Fluência - avaliar se a resposta faz sentido gramaticalmente

## Casos de Uso para usar RAG (Geração Aumentada por Recuperação) e bases de dados vetoriais

Existem muitos casos de uso onde as funções podem melhorar a sua aplicação, tais como:

- Perguntas e Respostas: fundamentar os dados da sua empresa num chat que pode ser usado pelos funcionários para fazer perguntas.

- Sistemas de Recomendação: onde pode criar um sistema que corresponde aos valores mais semelhantes, por exemplo, filmes, restaurantes e muito mais.

- Serviços de chatbot: pode armazenar o histórico de conversas e personalizar a conversa com base nos dados do usuário.

- Pesquisa de imagens baseada em embeddings vetoriais, útil para reconhecimento de imagem e deteção de anomalias.

## Resumo

Abordámos as áreas fundamentais do RAG desde adicionar os nossos dados à aplicação, a consulta do usuário e a saída. Para simplificar a criação de RAG, pode usar frameworks como Semanti Kernel, Langchain ou Autogen.

## Tarefa

Para continuar a sua aprendizagem sobre Geração Aumentada por Recuperação (RAG) pode construir:

- Construir um front-end para a aplicação usando o framework da sua preferência

- Utilizar um framework, quer LangChain ou Semantic Kernel, e recriar a sua aplicação.

Parabéns por completar a lição 👏.

## A aprendizagem não termina aqui, continue a Jornada

Após completar esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aumentar os seus conhecimentos em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->