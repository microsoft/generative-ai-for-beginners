# Criando Aplicações de Busca

[![Introduction to Generative AI and Large Language Models](../../images/08-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

Há muito mais nas LLMs do que chatbots e geração de texto. Também é possível criar aplicações de busca usando `Embeddings`. `Embeddings` são representações numéricas de dados, também conhecidas como vetores, e podem ser usados para busca semântica de dados.

Nesta lição, você vai criar uma aplicação de busca para a nossa startup de educação. Nossa startup é uma organização sem fins lucrativos que fornece educação gratuita para estudantes em países em desenvolvimento. Nossa startup possui uma grande quantidade de vídeos no YouTube que os estudantes podem usar para aprender sobre IA. Nossa startup deseja criar uma aplicação de busca que permita aos estudantes procurar por um vídeo no YouTube digitando uma pergunta.

Por exemplo, um estudante pode digitar: 'O que é Jupyter Notebooks?' ou 'O que é Azure ML' e a aplicação de busca retornará uma lista de vídeos do YouTube relevantes para a pergunta. E melhor ainda, a aplicação de busca retornará um link para o local no vídeo onde está localizada a resposta para a pergunta.

## Introdução

Nesta lição, vamos cobrir:

- Busca semântica vs busca por palavras-chave.
- O que são Embeddings de Texto.
- Criando um Índice de Embeddings de Texto.
- Buscando em um Índice de Embeddings de Texto.

## Metas de Aprendizado

Após completar esta lição, você será capaz de:

- Diferenciar entre busca semântica e busca por palavras-chave.
- Explicar o que são Embeddings de Texto.
- Criar uma aplicação usando Embeddings para buscar dados.

## Por que criar uma aplicação de busca?

Criar uma aplicação de busca ajudará você a entender como usar Embeddings para buscar dados. Você também aprenderá como construir uma aplicação de busca que pode ser usada por estudantes para encontrar informações rapidamente.

A lição inclui um Índice de Embeddings dos transcritos do YouTube para o canal [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-koreyst) da Microsoft no YouTube. O AI Show é um canal do YouTube que ensina sobre IA e aprendizado de máquina. O Índice de Embeddings contém os Embeddings para cada um dos transcritos do YouTube até outubro de 2023. Você usará o Índice de Embeddings para construir uma aplicação de busca para nossa startup. A aplicação de busca retorna um link para o local no vídeo onde está localizada a resposta para a pergunta. Esta é uma ótima maneira para os estudantes encontrarem rapidamente as informações de que precisam.

Abaixo nós temos um exemplo de uma consulta semântica para a pergunta: 'É possível usar o RStudio com o Azure ML?'. Confira a URL do YouTube, você verá que a URL contém um carimbo de data/hora que o leva para o local no vídeo onde está localizada

![Semantic query for the question "can you use rstudio with Azure ML"](../../images/query-results.png?WT.mc_id=academic-105485-koreyst)

## O que é busca semântica?

Agora você pode estar se perguntando, o que é busca semântica? A busca semântica é uma técnica de busca que utiliza a semântica, ou significado, das palavras em uma consulta para retornar resultados relevantes.

Aqui está um exemplo de busca semântica. Digamos que você esteja procurando comprar um carro, você pode buscar por 'meu carro dos sonhos', a busca semântica entende que você não está `sonhando` com um carro, mas sim procurando comprar o seu carro `ideal`. A busca semântica compreende sua intenção e retorna resultados relevantes. A alternativa é a `busca por palavras-chave`, que literalmente procuraria sonhos sobre carros e frequentemente retornaria resultados irrelevantes.

## O que são Embeddings de Texto?

[Embeddings de texto](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) são uma técnica de representação de texto usada em [processamento de linguagem natural](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Embeddings de texto são representações numéricas semânticas de texto. Embeddings são usados para representar dados de uma maneira fácil para uma máquina entender. Existem muitos modelos para construir embeddings de texto, nesta lição, vamos nos concentrar em gerar embeddings usando o Modelo de Embedding da OpenAI.

Aqui está um exemplo, imagine que o seguinte texto está em um transcrição de um dos episódios no canal do YouTube AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Nós passaríamos o texto para a API de Embedding da OpenAI e ela retornaria o seguinte embedding consistindo de 1536 números, também conhecido como um vetor. Cada número no vetor representa um aspecto diferente do texto. Para brevidade, aqui estão os primeiros 10 números do vetor.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Como o Índice de Embeddings é criado?

O Índice de Embeddings para esta lição foi criado com uma série de scripts Python. Você encontrará os scripts juntamente com as instruções no [README](../../scripts/README.md?WT.mc_id=academic-105485-koreyst) na pasta 'scripts' para esta lição. Você não precisa executar esses scripts para completar esta lição, pois o Índice de Embeddings é fornecido para você.

Os scripts executam as seguintes operações:

1. A transcrição de cada vídeo do YouTube na lista de reprodução [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-koreyst) é baixada.

2. Usando [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), uma tentativa é feita para extrair o nome do orador dos primeiros 3 minutos do transcrição do YouTube. O nome do orador para cada vídeo é armazenado no Índice de Embeddings chamado `embedding_index_3m.json`.

3. O texto da transcrição é então dividido em **segmentos de texto de 3 minutos**. O segmento inclui cerca de 20 palavras sobrepostas do próximo segmento para garantir que o Embedding para o segmento não seja cortado e para fornecer um melhor contexto de busca.

4. Cada segmento de texto é então passado para a API de Chat da OpenAI para resumir o texto em 60 palavras. O resumo também é armazenado no Índice de Embeddings `embedding_index_3m.json`.

5. Finalmente, o texto do segmento é passado para a API de Embedding da OpenAI. A API de Embedding retorna um vetor de 1536 números que representam o significado semântico do segmento. O segmento juntamente com o vetor de Embedding da OpenAI é armazenado em um Índice de Embeddings `embedding_index_3m.json`.

### Banco de Dados Vetorial

Para simplificar a lição, o Índice de Embeddings é armazenado em um arquivo JSON chamado `embedding_index_3m.json` e carregado em um DataFrame Pandas. No entanto, em produção, o Índice de Embeddings seria armazenado em um banco de dados vetorial como [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), para citar apenas alguns.

## Compreendendo a similaridade de cosseno

Aprendemos sobre embeddings de texto, o próximo passo é aprender como usar embeddings de texto para buscar dados e, em particular, encontrar os embeddings mais semelhantes a uma consulta dada usando a similaridade de cosseno.

### O que é similaridade de cosseno?

A similaridade de cosseno é uma medida de similaridade entre dois vetores, você também ouvirá isso referido como `busca por vizinho mais próximo`. Para realizar uma busca por similaridade de cosseno, é necessário _vetorizar_ o texto da _consulta_ usando a API de Embedding da OpenAI. Em seguida, calcular a _similaridade de cosseno_ entre o vetor de consulta e cada vetor no Índice de Embeddings. Lembre-se, o Índice de Embeddings tem um vetor para cada segmento de texto do transcrição do YouTube. Finalmente, ordene os resultados por similaridade de cosseno, e os segmentos de texto com a maior similaridade de cosseno são os mais semelhantes à consulta.

De uma perspectiva matemática, a similaridade de cosseno mede o cosseno do ângulo entre dois vetores projetados em um espaço multidimensional. Essa medida é benéfica, porque se dois documentos estão distantes pela distância euclidiana devido ao tamanho, eles ainda podem ter um ângulo menor entre eles e, portanto, uma maior similaridade de cosseno. Para mais informações sobre as equações de similaridade de cosseno, consulte [Similaridade de cosseno](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Criando sua primeira aplicação de busca

A seguir, vamos aprender como construir uma aplicação de busca usando Embeddings. A aplicação de busca permitirá que os estudantes procurem por um vídeo digitando uma pergunta. A aplicação de busca retornará uma lista de vídeos relevantes para a pergunta. A aplicação de busca também retornará um link para o local no vídeo onde está localizada a resposta para a pergunta.

Esta solução foi construída e testada no Windows 11, macOS e Ubuntu 22.04 usando Python 3.10 ou posterior. Você pode baixar o Python em [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Assignment - building a search application, to enable students

## Tarefa - criando uma aplicação de busca para habilitar os estudantes

Nós introduzimos nossa startup no início desta lição. Agora é hora de habilitar os estudantes para criar uma aplicação de busca para suas avaliações.

Nessa tarefa, você criará os Serviços Azure OpenAI que serão usados para construir a aplicação de busca. Você criará os seguintes Serviços Azure OpenAI. Você precisará de uma assinatura Azure para completar esta tarefa.

### Inicie o Azure Cloud Shell

1. Entre no [portal Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Selecione o ícone do Cloud Shell no canto superior direito do portal Azure.
3. Selecione **Bash** para o tipo de ambiente.

#### Crie um grupo de recursos

> Para estas instruções, estamos usando o grupo de recursos chamado "semantic-video-search" no East US.
> Você pode alterar o nome do grupo de recursos, mas ao alterar o local dos recursos,
> verifique a [tabela de disponibilidade do modelo](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Crie um recurso do Serviço do Azure OpenAI

No Azure Cloud Shell, execute o seguinte comando para criar um recurso do Serviço Azure OpenAI.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Obtenha o endpoint e as chaves para uso nesta aplicação

No Azure Cloud Shell, execute os seguintes comandos para obter o endpoint e as chaves para o recurso do Serviço Azure OpenAI.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Implemente o modelo de Embedding da OpenAI

No Azure Cloud Shell, execute o seguinte comando para implantar o modelo de Embedding da OpenAI.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
```

## Solução

Abre a [notebook de solução](../../python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) no GitHub Codespaces e siga as instruções no Jupyter Notebook.

Quando você executar o notebook, será solicitado a inserir uma consulta. A caixa de entrada será assim:

![Input box for the user to input a query](../../images/notebook-search.png?WT.mc_id=academic-105485-koreyst)

## Excelente trabalho! Continue aprendendo!

Após completar esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seu conhecimento em IA generativa!

Aqui vamos, para a Lição 9, onde veremos como [criar aplicações de geração de imagens](../../../09-building-image-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
