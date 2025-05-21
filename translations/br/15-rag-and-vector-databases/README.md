<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:15:09+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "br"
}
-->
# Geração Aumentada por Recuperação (RAG) e Bancos de Dados Vetoriais

Na lição de aplicativos de busca, aprendemos brevemente como integrar seus próprios dados em Modelos de Linguagem Grande (LLMs). Nesta lição, vamos nos aprofundar nos conceitos de fundamentar seus dados em sua aplicação LLM, na mecânica do processo e nos métodos para armazenar dados, incluindo embeddings e texto.

> **Vídeo Em Breve**

## Introdução

Nesta lição, abordaremos o seguinte:

- Uma introdução ao RAG, o que é e por que é usado em IA (inteligência artificial).

- Entender o que são bancos de dados vetoriais e criar um para nossa aplicação.

- Um exemplo prático de como integrar RAG em uma aplicação.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

- Explicar a importância do RAG na recuperação e processamento de dados.

- Configurar a aplicação RAG e fundamentar seus dados em um LLM

- Integração eficaz de RAG e Bancos de Dados Vetoriais em Aplicações LLM.

## Nosso Cenário: aprimorando nossos LLMs com nossos próprios dados

Para esta lição, queremos adicionar nossas próprias notas na startup de educação, o que permite que o chatbot obtenha mais informações sobre os diferentes assuntos. Usando as notas que temos, os alunos poderão estudar melhor e entender os diferentes tópicos, facilitando a revisão para seus exames. Para criar nosso cenário, usaremos:

- `Azure OpenAI:` o LLM que usaremos para criar nosso chatbot

- `AI for beginners' lesson on Neural Networks`: isso será o dado que fundamentaremos nosso LLM

- `Azure AI Search` e `Azure Cosmos DB:` banco de dados vetorial para armazenar nossos dados e criar um índice de busca

Os usuários poderão criar quizzes de prática a partir de suas notas, cartões de revisão e resumir em visões gerais concisas. Para começar, vejamos o que é RAG e como funciona:

## Geração Aumentada por Recuperação (RAG)

Um chatbot alimentado por LLM processa prompts do usuário para gerar respostas. Ele é projetado para ser interativo e engaja os usuários em uma ampla gama de tópicos. No entanto, suas respostas são limitadas ao contexto fornecido e aos dados de treinamento fundamentais. Por exemplo, o corte de conhecimento do GPT-4 é setembro de 2021, ou seja, ele não tem conhecimento de eventos que ocorreram após esse período. Além disso, os dados usados para treinar LLMs excluem informações confidenciais, como notas pessoais ou o manual de produtos de uma empresa.

### Como funcionam os RAGs (Geração Aumentada por Recuperação)

Suponha que você queira implantar um chatbot que cria quizzes a partir de suas notas, você precisará de uma conexão com a base de conhecimento. É aí que o RAG entra em cena. Os RAGs operam da seguinte forma:

- **Base de conhecimento:** Antes da recuperação, esses documentos precisam ser ingeridos e pré-processados, normalmente dividindo documentos grandes em partes menores, transformando-os em embeddings de texto e armazenando-os em um banco de dados.

- **Consulta do usuário:** o usuário faz uma pergunta

- **Recuperação:** Quando um usuário faz uma pergunta, o modelo de embedding recupera informações relevantes de nossa base de conhecimento para fornecer mais contexto que será incorporado ao prompt.

- **Geração Aumentada:** o LLM aprimora sua resposta com base nos dados recuperados. Isso permite que a resposta gerada não seja apenas baseada em dados pré-treinados, mas também em informações relevantes do contexto adicionado. Os dados recuperados são usados para aumentar as respostas do LLM. O LLM então retorna uma resposta à pergunta do usuário.

A arquitetura dos RAGs é implementada usando transformadores que consistem em duas partes: um codificador e um decodificador. Por exemplo, quando um usuário faz uma pergunta, o texto de entrada é 'codificado' em vetores capturando o significado das palavras e os vetores são 'decodificados' em nosso índice de documentos e geram novo texto com base na consulta do usuário. O LLM usa tanto um modelo codificador-decodificador para gerar a saída.

Duas abordagens ao implementar RAG de acordo com o artigo proposto: [Geração Aumentada por Recuperação para Tarefas de NLP (processamento de linguagem natural) intensivas em conhecimento](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) são:

- **_RAG-Sequence_** usando documentos recuperados para prever a melhor resposta possível para uma consulta do usuário

- **RAG-Token** usando documentos para gerar o próximo token, depois recuperá-los para responder à consulta do usuário

### Por que você usaria RAGs?

- **Riqueza de informação:** garante que as respostas de texto estejam atualizadas e atuais. Portanto, melhora o desempenho em tarefas específicas de domínio ao acessar a base de conhecimento interna.

- Reduz a fabricação utilizando **dados verificáveis** na base de conhecimento para fornecer contexto às consultas do usuário.

- É **custo-efetivo** pois são mais econômicos em comparação com o ajuste fino de um LLM

## Criando uma base de conhecimento

Nossa aplicação é baseada em nossos dados pessoais, ou seja, a lição de Redes Neurais no currículo de IA Para Iniciantes.

### Bancos de Dados Vetoriais

Um banco de dados vetorial, ao contrário dos bancos de dados tradicionais, é um banco de dados especializado projetado para armazenar, gerenciar e buscar vetores incorporados. Ele armazena representações numéricas de documentos. Dividir os dados em embeddings numéricos facilita para nosso sistema de IA entender e processar os dados.

Armazenamos nossos embeddings em bancos de dados vetoriais, pois os LLMs têm um limite do número de tokens que aceitam como entrada. Como você não pode passar todos os embeddings para um LLM, precisaremos dividi-los em partes e, quando um usuário fizer uma pergunta, os embeddings mais semelhantes à pergunta serão retornados juntamente com o prompt. A divisão também reduz os custos no número de tokens passados por um LLM.

Alguns bancos de dados vetoriais populares incluem Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Você pode criar um modelo Azure Cosmos DB usando Azure CLI com o seguinte comando:

Antes de armazenarmos nossos dados, precisaremos convertê-los em embeddings vetoriais antes de serem armazenados no banco de dados. Se você estiver trabalhando com documentos grandes ou textos longos, pode dividi-los com base nas consultas que espera. A divisão pode ser feita no nível da frase ou no nível do parágrafo. Como a divisão deriva significados das palavras ao seu redor, você pode adicionar algum outro contexto a uma parte, por exemplo, adicionando o título do documento ou incluindo algum texto antes ou depois da parte. Você pode dividir os dados da seguinte forma:

Uma vez divididos, podemos então incorporar nosso texto usando diferentes modelos de embedding. Alguns modelos que você pode usar incluem: word2vec, ada-002 da OpenAI, Azure Computer Vision e muitos mais. Selecionar um modelo para usar dependerá das linguagens que você está usando, do tipo de conteúdo codificado (texto/imagens/áudio), do tamanho da entrada que pode codificar e do comprimento da saída de embedding.

Um exemplo de texto incorporado usando o modelo `text-embedding-ada-002` da OpenAI é:

## Recuperação e Busca Vetorial

Quando um usuário faz uma pergunta, o recuperador a transforma em um vetor usando o codificador de consulta, ele então busca em nosso índice de busca de documentos por vetores relevantes no documento que estão relacionados à entrada. Uma vez feito, ele converte tanto o vetor de entrada quanto os vetores de documentos em texto e passa pelo LLM.

### Recuperação

A recuperação acontece quando o sistema tenta encontrar rapidamente os documentos do índice que satisfazem os critérios de busca. O objetivo do recuperador é obter documentos que serão usados para fornecer contexto e fundamentar o LLM em seus dados.

Existem várias maneiras de realizar buscas dentro de nosso banco de dados, como:

- **Busca por palavra-chave** - usada para buscas de texto

- **Busca semântica** - usa o significado semântico das palavras

- **Busca vetorial** - converte documentos de texto para representações vetoriais usando modelos de embedding. A recuperação será feita consultando os documentos cujas representações vetoriais estão mais próximas da pergunta do usuário.

- **Híbrida** - uma combinação de busca por palavra-chave e busca vetorial.

Um desafio com a recuperação surge quando não há resposta semelhante à consulta no banco de dados, o sistema então retornará a melhor informação que puder obter, no entanto, você pode usar táticas como definir a distância máxima para relevância ou usar busca híbrida que combina palavras-chave e busca vetorial. Nesta lição, usaremos busca híbrida, uma combinação de busca vetorial e por palavra-chave. Armazenaremos nossos dados em um dataframe com colunas contendo as partes, bem como embeddings.

### Similaridade Vetorial

O recuperador buscará na base de dados de conhecimento por embeddings que estão próximos, o vizinho mais próximo, pois são textos que são semelhantes. No cenário em que um usuário faz uma consulta, ela é primeiro incorporada e depois combinada com embeddings semelhantes. A medida comum usada para encontrar a semelhança entre diferentes vetores é a similaridade cosseno, que se baseia no ângulo entre dois vetores.

Podemos medir a similaridade usando outras alternativas que podemos usar são a distância Euclidiana, que é a linha reta entre os pontos finais do vetor, e o produto escalar, que mede a soma dos produtos dos elementos correspondentes de dois vetores.

### Índice de Busca

Ao fazer a recuperação, precisaremos construir um índice de busca para nossa base de conhecimento antes de realizarmos a busca. Um índice armazenará nossos embeddings e poderá recuperar rapidamente as partes mais semelhantes, mesmo em um banco de dados grande. Podemos criar nosso índice localmente usando:

### Re-ranqueamento

Uma vez que você consultou o banco de dados, pode precisar classificar os resultados dos mais relevantes. Um LLM de re-ranqueamento utiliza Machine Learning para melhorar a relevância dos resultados de busca, ordenando-os dos mais relevantes. Usando o Azure AI Search, o re-ranqueamento é feito automaticamente para você usando um re-ranqueador semântico. Um exemplo de como o re-ranqueamento funciona usando vizinhos mais próximos:

## Unindo tudo

O último passo é adicionar nosso LLM à mistura para poder obter respostas que são fundamentadas em nossos dados. Podemos implementá-lo da seguinte forma:

## Avaliando nossa aplicação

### Métricas de Avaliação

- Qualidade das respostas fornecidas garantindo que soem naturais, fluentes e semelhantes a humanos

- Fundamentação dos dados: avaliando se a resposta veio dos documentos fornecidos

- Relevância: avaliando se a resposta corresponde e está relacionada à pergunta feita

- Fluência - se a resposta faz sentido gramaticalmente

## Casos de Uso para usar RAG (Geração Aumentada por Recuperação) e bancos de dados vetoriais

Existem muitos casos de uso diferentes onde chamadas de função podem melhorar seu aplicativo, como:

- Perguntas e Respostas: fundamentando os dados da sua empresa para um chat que pode ser usado por funcionários para fazer perguntas.

- Sistemas de Recomendação: onde você pode criar um sistema que combina os valores mais semelhantes, por exemplo, filmes, restaurantes e muitos mais.

- Serviços de Chatbot: você pode armazenar o histórico de chat e personalizar a conversa com base nos dados do usuário.

- Busca de imagens baseada em embeddings vetoriais, útil ao fazer reconhecimento de imagens e detecção de anomalias.

## Resumo

Cobrimos as áreas fundamentais do RAG desde adicionar nossos dados à aplicação, a consulta do usuário e a saída. Para simplificar a criação do RAG, você pode usar frameworks como Semanti Kernel, Langchain ou Autogen.

## Tarefa

Para continuar seu aprendizado sobre Geração Aumentada por Recuperação (RAG), você pode construir:

- Construir um front-end para a aplicação usando o framework de sua escolha

- Utilizar um framework, seja LangChain ou Semantic Kernel, e recriar sua aplicação.

Parabéns por completar a lição 👏.

## O aprendizado não para por aqui, continue a Jornada

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.