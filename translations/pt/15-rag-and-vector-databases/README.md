<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T17:47:04+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "pt"
}
-->
# Geração Aumentada por Recuperação (RAG) e Bases de Dados Vetoriais

[![Geração Aumentada por Recuperação (RAG) e Bases de Dados Vetoriais](../../../../../translated_images/pt/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Na lição de aplicações de pesquisa, aprendemos brevemente como integrar os seus próprios dados em Grandes Modelos de Linguagem (LLMs). Nesta lição, vamos aprofundar os conceitos de fundamentar os seus dados na sua aplicação LLM, os mecanismos do processo e os métodos para armazenar dados, incluindo tanto embeddings como texto.

> **Vídeo em Breve**

## Introdução

Nesta lição iremos abordar o seguinte:

- Uma introdução ao RAG, o que é e porque é usado em IA (inteligência artificial).

- Compreender o que são bases de dados vetoriais e criar uma para a nossa aplicação.

- Um exemplo prático de como integrar RAG numa aplicação.

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

- Explicar a importância do RAG na recuperação e processamento de dados.

- Configurar uma aplicação RAG e fundamentar os seus dados num LLM.

- Integração eficaz do RAG e Bases de Dados Vetoriais em Aplicações LLM.

## O nosso Cenário: melhorar os nossos LLMs com os nossos próprios dados

Para esta lição, queremos adicionar as nossas próprias notas à startup educativa, o que permite ao chatbot obter mais informações sobre as diferentes disciplinas. Utilizando as notas que temos, os alunos poderão estudar melhor e compreender os diferentes temas, tornando mais fácil rever para os seus exames. Para criar o nosso cenário, iremos usar:

- `Azure OpenAI:` o LLM que iremos usar para criar o nosso chatbot

- `Lição AI para iniciantes em Redes Neuronais:` estes serão os dados nos quais fundamentamos o nosso LLM

- `Azure AI Search` e `Azure Cosmos DB:` base de dados vetorial para armazenar os nossos dados e criar um índice de pesquisa

Os utilizadores poderão criar quizzes de prática a partir das suas notas, cartões de revisão e resumir para visões gerais concisas. Para começar, vejamos o que é RAG e como funciona:

## Geração Aumentada por Recuperação (RAG)

Um chatbot alimentado por um LLM processa os prompts do utilizador para gerar respostas. Foi concebido para ser interativo e envolver-se com os utilizadores numa ampla variedade de tópicos. No entanto, as suas respostas estão limitadas ao contexto fornecido e aos seus dados de treino fundamentais. Por exemplo, o corte de conhecimento do GPT-4 é setembro de 2021, o que significa que não tem conhecimento de eventos que ocorreram após esse período. Além disso, os dados usados para treinar os LLMs excluem informação confidencial como notas pessoais ou o manual do produto de uma empresa.

### Como funcionam os RAG (Geração Aumentada por Recuperação)

![desenho a mostrar como funcionam os RAGs](../../../../../translated_images/pt/how-rag-works.f5d0ff63942bd3a6.webp)

Suponha que quer implementar um chatbot que cria quizzes a partir das suas notas, irá precisar de uma ligação à base de conhecimento. É aqui que o RAG entra em ação. Os RAGs operam da seguinte forma:

- **Base de conhecimento:** Antes da recuperação, estes documentos precisam de ser ingeridos e pré-processados, normalmente dividindo documentos grandes em pedaços menores, transformando-os em embeddings de texto e armazenando-os numa base de dados.

- **Consulta do Utilizador:** o utilizador faz uma pergunta

- **Recuperação:** Quando um utilizador faz uma pergunta, o modelo de embedding recupera informação relevante da nossa base de conhecimento para fornecer mais contexto que será incorporado no prompt.

- **Geração Aumentada:** o LLM melhora a sua resposta com base nos dados recuperados. Isto permite que a resposta gerada não seja apenas baseada em dados pré-treinados, mas também em informação relevante do contexto adicionado. Os dados recuperados são usados para aumentar as respostas do LLM. O LLM retorna então uma resposta à pergunta do utilizador.

![desenho a mostrar como é a arquitetura dos RAGs](../../../../../translated_images/pt/encoder-decode.f2658c25d0eadee2.webp)

A arquitetura para os RAGs é implementada usando transformers consistindo de duas partes: um codificador (encoder) e um descodificador (decoder). Por exemplo, quando um utilizador faz uma pergunta, o texto de entrada é ‘codificado’ em vetores que capturam o significado das palavras, e os vetores são ‘descodificados’ no nosso índice de documentos e geram novo texto baseado na consulta do utilizador. O LLM usa um modelo codificador-descodificador para gerar a saída.

Duas abordagens quando se implementa RAG segundo o artigo proposto: [Retrieval-Augmented Generation for Knowledge intensive NLP (tarefas de processamento de linguagem natural)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) são:

- **_RAG-Sequence_** usando documentos recuperados para prever a melhor resposta possível a uma consulta do utilizador

- **RAG-Token** usando documentos para gerar o próximo token, depois recuperá-los para responder à consulta do utilizador

### Por que razão usar RAGs?

- **Riqueza de informação:** garante que as respostas de texto estão atualizadas e atuais. Por isso, melhora o desempenho em tarefas específicas de domínio ao aceder à base de conhecimento interna.

- Reduz fabricação ao utilizar **dados verificáveis** na base de conhecimento para fornecer contexto às questões dos utilizadores.

- É **custo-efetivo** pois são mais económicos em comparação com o ajuste fino de um LLM

## Criar uma base de conhecimento

A nossa aplicação baseia-se nos nossos dados pessoais, ou seja, a lição sobre Redes Neuronais no currículo AI para iniciantes.

### Bases de Dados Vetoriais

Uma base de dados vetorial, ao contrário das bases de dados tradicionais, é uma base especializada para armazenar, gerir e pesquisar vetores embutidos. Armazena representações numéricas de documentos. Dividir os dados em embeddings numéricos torna mais fácil para o nosso sistema de IA compreender e processar os dados.

Armazenamos os nossos embeddings em bases de dados vetoriais pois os LLMs têm um limite no número de tokens que aceitam como entrada. Como não pode passar todos os embeddings para um LLM, vamos precisar de os dividir em pedaços, e quando um utilizador faz uma pergunta, os embeddings mais semelhantes serão devolvidos juntamente com o prompt. A divisão em pedaços também reduz os custos no número de tokens passados por um LLM.

Algumas bases de dados vetoriais populares incluem Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Pode criar um modelo Azure Cosmos DB usando Azure CLI com o seguinte comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto a embeddings

Antes de armazenar os nossos dados, precisamos converter em embeddings vetoriais antes de serem armazenados na base de dados. Se estiver a trabalhar com documentos grandes ou textos longos, pode dividir em pedaços baseados nas perguntas que espera receber. A divisão pode ser feita a nível de frase ou parágrafo. Como a divisão deriva significados das palavras à sua volta, pode adicionar algum outro contexto a um pedaço, por exemplo, adicionando o título do documento ou incluindo algum texto antes ou depois do pedaço. Pode dividir os dados da seguinte forma:

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

    # Se o último pedaço não atingir o comprimento mínimo, adiciona-o na mesma
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Uma vez divididos, podemos depois incorporar o nosso texto usando diferentes modelos de embedding. Alguns modelos que pode usar incluem: word2vec, ada-002 da OpenAI, Azure Computer Vision e muitos mais. A seleção do modelo depende das línguas que está a usar, o tipo de conteúdo codificado (texto/imagens/áudio), o tamanho da entrada que pode codificar e o comprimento da saída de embedding.

Um exemplo de texto embutido usando o modelo `text-embedding-ada-002` da OpenAI é:
![um embedding da palavra gato](../../../../../translated_images/pt/cat.74cbd7946bc9ca38.webp)

## Recuperação e Pesquisa Vetorial

Quando um utilizador faz uma pergunta, o motor de recuperação transforma-a num vetor usando o codificador de consulta, depois pesquisa no nosso índice de documento os vetores relevantes relacionados com a entrada. Depois de feito, converte tanto o vetor de entrada como os vetores do documento em texto e envia para o LLM.

### Recuperação

A recuperação acontece quando o sistema tenta encontrar rapidamente os documentos do índice que satisfazem os critérios de pesquisa. O objetivo do motor de recuperação é obter documentos que serão usados para fornecer contexto e fundamentar o LLM nos seus dados.

Existem várias formas de fazer pesquisa na nossa base de dados, como:

- **Pesquisa por palavra-chave** - usada para pesquisas de texto

- **Pesquisa vetorial** - converte documentos de texto em representações vetoriais usando modelos de embedding, permitindo uma **pesquisa semântica** usando o significado das palavras. A recuperação será feita consultando os documentos cujas representações vetoriais sejam mais próximas da pergunta do utilizador.

- **Híbrido** - uma combinação de pesquisa por palavra-chave e vetorial.

Um desafio na recuperação surge quando não existe uma resposta similar à pergunta na base de dados; o sistema retorna então a melhor informação possível, contudo, pode usar táticas como definir a distância máxima para relevância ou usar pesquisa híbrida que combina palavras-chave e pesquisa vetorial. Nesta lição vamos usar pesquisa híbrida, uma combinação de ambas. Iremos armazenar os dados num dataframe com colunas que contêm os pedaços assim como os embeddings.

### Similaridade Vetorial

O motor de recuperação procura na base de conhecimento por embeddings que estão próximos, o vizinho mais próximo, pois são textos semelhantes. No cenário em que um utilizador faz uma consulta, esta é primeiro embutida e depois comparada com embeddings semelhantes. A métrica comum utilizada para medir a semelhança entre diferentes vetores é a similaridade do cosseno baseada no ângulo entre dois vetores.

Podemos medir similaridade usando outras alternativas como a distância Euclidiana, que é a linha reta entre as extremidades dos vetores, e o produto escalar que mede a soma dos produtos dos elementos correspondentes de dois vetores.

### Índice de pesquisa

Ao realizar a recuperação, precisaremos construir um índice de pesquisa para a nossa base de conhecimento antes de realizar buscas. Um índice armazenará os nossos embeddings e pode rapidamente recuperar os pedaços mais semelhantes mesmo numa base de dados grande. Podemos criar o nosso índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Criar o índice de pesquisa
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Para consultar o índice, pode usar o método kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Reordenamento

Depois de consultar a base de dados, pode ser preciso ordenar os resultados do mais relevante para o menos relevante. Um LLM de reordenamento utiliza Aprendizagem Automática para melhorar a relevância dos resultados da pesquisa, ordenando-os do mais relevante. Usando Azure AI Search, o reordenamento é feito automaticamente para si usando um reranker semântico. Um exemplo de como funciona o reordenamento com os vizinhos mais próximos:

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

## Unindo tudo

A última etapa é adicionar o nosso LLM para conseguir obter respostas que estejam fundamentadas nos nossos dados. Podemos implementá-lo da seguinte forma:

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

    # usar a conclusão de chat para gerar uma resposta
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Avaliação da nossa aplicação

### Métricas de Avaliação

- Qualidade das respostas fornecidas, garantindo que soam naturais, fluentes e semelhantes às humanas

- Fundamentação dos dados: avaliar se a resposta veio dos documentos fornecidos

- Relevância: avaliar se a resposta corresponde e está relacionada com a pergunta feita

- Fluência - se a resposta faz sentido gramaticalmente

## Casos de Uso para usar RAG (Geração Aumentada por Recuperação) e bases de dados vetoriais

Existem muitos casos de uso onde chamadas de função podem melhorar a sua app, tais como:

- Perguntas e Respostas: fundamentar os dados da sua empresa para um chat que possa ser usado por colaboradores para fazer perguntas.

- Sistemas de Recomendação: onde pode criar um sistema que corresponde aos valores mais semelhantes, ex.: filmes, restaurantes e muitos mais.

- Serviços de chatbot: pode armazenar histórico de conversa e personalizar a conversa com base nos dados do utilizador.

- Pesquisa de imagens baseada em embeddings vetoriais, útil para reconhecimento de imagem e deteção de anomalias.

## Resumo

Cobriram-se as áreas fundamentais do RAG desde adicionar os nossos dados à aplicação, a consulta do utilizador e a saída. Para simplificar a criação de RAG, pode usar frameworks como Semanti Kernel, Langchain ou Autogen.

## Tarefa

Para continuar a sua aprendizagem sobre Geração Aumentada por Recuperação (RAG) pode construir:

- Construir uma interface front-end para a aplicação usando o framework da sua escolha

- Utilizar um framework, seja LangChain ou Semantic Kernel, e recriar a sua aplicação.

Parabéns por completar a lição 👏.

## A aprendizagem não para aqui, continue a Jornada

Após completar esta lição, veja a nossa [coleção de Aprendizagem em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar os seus conhecimentos em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas que possam resultar do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->