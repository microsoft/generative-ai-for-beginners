# Geração Aumentada por Recuperação (RAG) e Bancos de Dados Vetoriais

[![Geração Aumentada por Recuperação (RAG) e Bancos de Dados Vetoriais](../../../translated_images/pt-BR/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Na lição de aplicações de busca, aprendemos brevemente como integrar seus próprios dados em Modelos de Linguagem de Grande Escala (LLMs). Nesta lição, vamos aprofundar os conceitos de incorporar seus dados na aplicação LLM, os mecanismos do processo e os métodos para armazenar dados, incluindo embeddings e texto.

> **Vídeo em Breve**

## Introdução

Nesta lição, cobriremos o seguinte:

- Uma introdução ao RAG, o que é e por que é usado em IA (inteligência artificial).

- Entender o que são bancos de dados vetoriais e criar um para nossa aplicação.

- Um exemplo prático de como integrar RAG em uma aplicação.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

- Explicar a importância do RAG na recuperação e processamento de dados.

- Configurar uma aplicação RAG e incorporar seus dados em um LLM

- Integração eficaz do RAG e Bancos de Dados Vetoriais em Aplicações LLM.

## Nosso Cenário: aprimorando nossos LLMs com nossos próprios dados

Para esta lição, queremos adicionar nossas próprias notas na startup educacional, o que permite que o chatbot obtenha mais informações sobre os diferentes assuntos. Usando as notas que temos, os alunos poderão estudar melhor e entender os diferentes tópicos, facilitando a revisão para seus exames. Para criar nosso cenário, usaremos:

- `Azure OpenAI:` o LLM que usaremos para criar nosso chatbot

- `Lição AI para iniciantes sobre Redes Neurais`: estes serão os dados nos quais fundamentaremos nosso LLM

- `Azure AI Search` e `Azure Cosmos DB:` banco de dados vetorial para armazenar nossos dados e criar um índice de busca

Os usuários poderão criar quizzes de prática a partir das suas notas, cartões de revisão e resumi-los em visões gerais concisas. Para começar, vamos ver o que é RAG e como funciona:

## Geração Aumentada por Recuperação (RAG)

Um chatbot alimentado por LLM processa as solicitações dos usuários para gerar respostas. Ele é projetado para ser interativo e engaja os usuários em uma ampla variedade de tópicos. Porém, suas respostas são limitadas ao contexto fornecido e seus dados de treinamento fundamentais. Por exemplo, o corte de conhecimento do GPT-4 é de setembro de 2021, o que significa que ele não possui conhecimento de eventos ocorridos após esse período. Além disso, os dados usados para treinar LLMs excluem informações confidenciais como notas pessoais ou manuais de produtos de uma empresa.

### Como os RAGs (Geração Aumentada por Recuperação) funcionam

![desenho mostrando como os RAGs funcionam](../../../translated_images/pt-BR/how-rag-works.f5d0ff63942bd3a6.webp)

Suponha que você queira implantar um chatbot que cria quizzes a partir de suas notas, você precisará de uma conexão com a base de conhecimento. É aí que o RAG entra em ação. Os RAGs operam da seguinte forma:

- **Base de conhecimento:** Antes da recuperação, esses documentos precisam ser ingeridos e pré-processados, normalmente dividindo grandes documentos em partes menores, transformando-os em embeddings de texto e armazenando-os em um banco de dados.

- **Consulta do usuário:** o usuário faz uma pergunta

- **Recuperação:** Quando um usuário faz uma pergunta, o modelo de embedding recupera informações relevantes da nossa base de conhecimento para fornecer mais contexto que será incorporado ao prompt.

- **Geração Aumentada:** o LLM aprimora sua resposta com base nos dados recuperados. Isso permite que a resposta gerada não seja apenas baseada em dados pré-treinados, mas também em informações relevantes do contexto adicionado. Os dados recuperados são usados para aumentar as respostas do LLM. O LLM então retorna uma resposta à pergunta do usuário.

![desenho mostrando como é a arquitetura dos RAGs](../../../translated_images/pt-BR/encoder-decode.f2658c25d0eadee2.webp)

A arquitetura para RAGs é implementada usando transformers que consistem em duas partes: um codificador (encoder) e um decodificador (decoder). Por exemplo, quando um usuário faz uma pergunta, o texto de entrada é 'codificado' em vetores que capturam o significado das palavras e os vetores são 'decodificados' em nosso índice de documentos e geram novo texto com base na consulta do usuário. O LLM usa um modelo encoder-decoder para gerar a saída.

Duas abordagens ao implementar RAG conforme o artigo proposto: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) são:

- **_RAG-Sequence_** usando documentos recuperados para prever a melhor resposta possível para a consulta do usuário

- **RAG-Token** usando documentos para gerar o próximo token, então recuperá-los para responder à consulta do usuário

### Por que usar RAGs?

- **Riqueza de informação:** garante que as respostas textuais estejam atualizadas e atuais. Portanto, melhora o desempenho em tarefas específicas de domínio acessando a base de conhecimento interna.

- Reduz a fabricação ao utilizar **dados verificáveis** na base de conhecimento para fornecer contexto às consultas dos usuários.

- É **econômico**, pois é mais barato comparado a fazer fine-tuning em um LLM.

## Criando uma base de conhecimento

Nossa aplicação baseia-se em nossos dados pessoais, isto é, a lição sobre Redes Neurais do currículo AI Para Iniciantes.

### Bancos de dados vetoriais

Um banco de dados vetorial, diferente dos bancos de dados tradicionais, é um banco especializado projetado para armazenar, gerenciar e buscar vetores incorporados. Ele armazena representações numéricas de documentos. Quebrar dados em embeddings numéricos facilita para nosso sistema de IA entender e processar os dados.

Armazenamos nossos embeddings em bancos de dados vetoriais, pois os LLMs têm um limite de tokens que aceitam como entrada. Como não é possível passar o embedding inteiro para o LLM, precisamos dividir em partes e, quando um usuário faz uma pergunta, os embeddings mais similares à pergunta serão retornados junto com o prompt. Dividir em partes também reduz custos no número de tokens enviados para o LLM.

Alguns bancos de dados vetoriais populares incluem Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Você pode criar um modelo Azure Cosmos DB usando Azure CLI com o seguinte comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto para embeddings

Antes de armazenar nossos dados, precisamos converter para embeddings vetoriais antes de armazená-los no banco de dados. Se você estiver trabalhando com documentos grandes ou textos longos, pode dividi-los com base nas consultas esperadas. A divisão pode ser feita no nível da sentença ou do parágrafo. Como a divisão deriva significados das palavras próximas, você pode adicionar outro contexto a um pedaço, por exemplo, incluindo o título do documento ou algum texto antes ou depois do trecho. Você pode dividir os dados assim:

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

    # Se o último fragmento não atingiu o comprimento mínimo, adicione-o de qualquer forma
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Depois de dividir, podemos transformar nosso texto em embeddings usando diferentes modelos de embedding. Alguns modelos que você pode usar incluem: word2vec, ada-002 da OpenAI, Azure Computer Vision e muitos mais. A escolha do modelo depende das línguas usadas, tipo de conteúdo codificado (texto/imagem/áudio), tamanho da entrada que pode codificar e comprimento da saída do embedding.

Um exemplo de texto embutido usando o modelo `text-embedding-ada-002` da OpenAI é:
![uma embedding da palavra gato](../../../translated_images/pt-BR/cat.74cbd7946bc9ca38.webp)

## Recuperação e Busca Vetorial

Quando um usuário faz uma pergunta, o recuperador transforma essa pergunta em um vetor usando o codificador de consulta, e então busca pelo nosso índice de pesquisa de documentos os vetores relevantes no documento relacionados à entrada. Uma vez feito isso, converte tanto o vetor de entrada quanto os vetores dos documentos em texto e passa para o LLM.

### Recuperação

A recuperação acontece quando o sistema tenta rapidamente encontrar os documentos do índice que satisfazem os critérios de busca. O objetivo do recuperador é obter documentos que serão usados para fornecer contexto e fundamentar o LLM em seus dados.

Existem várias formas de realizar busca no nosso banco de dados, como:

- **Busca por palavra-chave** - usada para buscas textuais

- **Busca vetorial** - converte documentos de texto para representações vetoriais usando modelos de embedding, permitindo uma **busca semântica** usando o significado das palavras. A recuperação será feita consultando os documentos cujas representações vetoriais são as mais próximas da pergunta do usuário.

- **Híbrido** - combinação de busca por palavra-chave e busca vetorial.

Um desafio na recuperação ocorre quando não há resposta similar para a consulta na base de dados, o sistema então retorna a melhor informação possível, contudo, você pode usar estratégias como definir a distância máxima para relevância ou usar busca híbrida que combina palavra-chave e busca vetorial. Nesta lição, usaremos busca híbrida, combinação de busca vetorial e por palavra-chave. Armazenaremos nossos dados em um dataframe com colunas contendo os trechos e os embeddings.

### Similaridade Vetorial

O recuperador vai buscar a base de conhecimento os embeddings que estejam próximos, os vizinhos mais próximos, pois são textos similares. No cenário, quando o usuário faz uma consulta, esta é primeiro embutida e então combinada com embeddings similares. A medição comum usada para descobrir similaridade de vetores é a similaridade do cosseno, que é baseada no ângulo entre dois vetores.

Podemos medir a similaridade usando outras alternativas como distância euclidiana que é a linha reta entre os pontos finais dos vetores e produto escalar que mede a soma dos produtos dos elementos correspondentes dos dois vetores.

### Índice de busca

Ao fazer a recuperação, precisaremos construir um índice de busca para nossa base de conhecimento antes de realizar a pesquisa. Um índice armazenará nossos embeddings e pode recuperar rapidamente os trechos mais similares mesmo em uma base de dados grande. Podemos criar nosso índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Criar o índice de busca
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Para consultar o índice, você pode usar o método kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Reordenação

Depois de consultar o banco de dados, pode ser necessário ordenar os resultados do mais relevante para o menos relevante. Um LLM de reordenação utiliza Machine Learning para melhorar a relevância dos resultados da busca ordenando-os do mais relevante. Usando Azure AI Search, a reordenação é feita automaticamente para você usando um reordenador semântico. Exemplo de como funciona a reordenação usando vizinhos mais próximos:

```python
# Encontre os documentos mais semelhantes
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Imprima os documentos mais semelhantes
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Combinando tudo

A última etapa é adicionar nosso LLM à mistura para ser capaz de obter respostas fundamentadas em nossos dados. Podemos implementar da seguinte forma:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Converter a pergunta em um vetor de consulta
    query_vector = create_embeddings(user_input)

    # Encontrar os documentos mais similares
    distances, indices = nbrs.kneighbors([query_vector])

    # adicionar documentos à consulta para fornecer contexto
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combinar o histórico e a entrada do usuário
    history.append(user_input)

    # criar um objeto de mensagem
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # usar a API Responses para gerar uma resposta
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Avaliando nossa aplicação

### Métricas de Avaliação

- Qualidade das respostas fornecidas, garantindo que soe natural, fluente e parecida com humana

- Fundamentação dos dados: avaliar se a resposta veio dos documentos fornecidos

- Relevância: avaliar se a resposta coincide e está relacionada com a pergunta feita

- Fluência - se a resposta faz sentido gramaticalmente

## Casos de Uso para usar RAG (Geração Aumentada por Recuperação) e bancos de dados vetoriais

Existem muitos casos de uso diferentes onde chamadas de função podem melhorar seu app, como:

- Perguntas e Respostas: fundamentar os dados da empresa em um chat que pode ser usado por colaboradores para fazer perguntas.

- Sistemas de Recomendação: onde você pode criar um sistema que combine os valores mais similares, por exemplo, filmes, restaurantes e muitos mais.

- Serviços de chatbot: você pode armazenar histórico do chat e personalizar a conversa com base nos dados do usuário.

- Busca por imagens baseada em embeddings vetoriais, útil ao fazer reconhecimento de imagens e detecção de anomalias.

## Resumo

Cobrimos as áreas fundamentais do RAG, desde adicionar nossos dados na aplicação, a consulta do usuário e a saída. Para simplificar a criação do RAG, você pode usar frameworks como Semantic Kernel, Langchain ou Autogen.

## Tarefa

Para continuar seu aprendizado sobre Geração Aumentada por Recuperação (RAG), você pode construir:

- Construir uma interface front-end para a aplicação usando o framework de sua escolha

- Utilizar um framework, seja LangChain ou Semantic Kernel, e recriar sua aplicação.

Parabéns por completar a lição 👏.

## O aprendizado não para aqui, continue a Jornada

Após terminar esta lição, confira nossa [coleção de aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar evoluindo seu conhecimento de IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->