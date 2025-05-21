<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:07:37+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pt"
}
-->
# Construindo Aplicações de Geração de Imagens

Há mais nos LLMs do que apenas geração de texto. Também é possível gerar imagens a partir de descrições textuais. Ter imagens como uma modalidade pode ser altamente útil em várias áreas, como MedTech, arquitetura, turismo, desenvolvimento de jogos e mais. Neste capítulo, vamos explorar os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, vamos abordar:

- Geração de imagens e por que é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como você pode construir um aplicativo de geração de imagens.

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

- Construir um aplicativo de geração de imagens.
- Definir limites para seu aplicativo com metaprompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir um aplicativo de geração de imagens?

Aplicações de geração de imagens são uma ótima maneira de explorar as capacidades da IA Generativa. Elas podem ser usadas, por exemplo, para:

- **Edição e síntese de imagens**. Você pode gerar imagens para uma variedade de casos de uso, como edição e síntese de imagens.

- **Aplicado a uma variedade de indústrias**. Elas também podem ser usadas para gerar imagens para uma variedade de indústrias como Medtech, Turismo, Desenvolvimento de jogos e mais.

## Cenário: Edu4All

Como parte desta lição, continuaremos a trabalhar com nossa startup, Edu4All, nesta lição. Os estudantes criarão imagens para suas avaliações, exatamente quais imagens fica a critério dos estudantes, mas elas podem ser ilustrações para seu próprio conto de fadas ou criar um novo personagem para sua história ou ajudá-los a visualizar suas ideias e conceitos.

Aqui está o que os estudantes da Edu4All poderiam gerar, por exemplo, se estivessem trabalhando em aula sobre monumentos:

usando um prompt como

> "Cachorro ao lado da Torre Eiffel ao nascer do sol"

## O que é DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, eles permitem que você use prompts para gerar imagens.

### DALL-E

Vamos começar com o DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições textuais.

- **CLIP**, é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Atenção Difusa**, é um modelo que gera imagens a partir de embeddings. O DALL-E é treinado em um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com um chapéu, ou um cachorro com um moicano.

### Midjourney

O Midjourney funciona de maneira semelhante ao DALL-E, ele gera imagens a partir de prompts textuais. O Midjourney também pode ser usado para gerar imagens usando prompts como "um gato com um chapéu", ou um "cachorro com um moicano".

## Como DALL-E e Midjourney Funcionam

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autorregressivo_.

Um _transformer autorregressivo_ define como um modelo gera imagens a partir de descrições textuais, ele gera um pixel de cada vez e depois usa os pixels gerados para gerar o próximo pixel. Passando por várias camadas em uma rede neural, até que a imagem esteja completa.

Com esse processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. No entanto, o DALL-E 2 e 3 têm mais controle sobre a imagem gerada.

## Construindo seu primeiro aplicativo de geração de imagens

Então, o que é necessário para construir um aplicativo de geração de imagens? Você precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendável usar esta biblioteca para manter seus segredos em um arquivo _.env_ longe do código.
- **openai**, esta biblioteca é o que você usará para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudá-lo a fazer solicitações HTTP.

1. Crie um arquivo _.env_ com o seguinte conteúdo:

   Localize essas informações no Portal Azure para seu recurso na seção "Chaves e Endpoint".

1. Colete as bibliotecas acima em um arquivo chamado _requirements.txt_ assim:

1. Em seguida, crie um ambiente virtual e instale as bibliotecas:

   Para Windows, use os seguintes comandos para criar e ativar seu ambiente virtual:

1. Adicione o seguinte código em um arquivo chamado _app.py_:

Vamos explicar este código:

- Primeiro, importamos as bibliotecas que precisamos, incluindo a biblioteca OpenAI, a biblioteca dotenv, a biblioteca requests e a biblioteca Pillow.

- Em seguida, carregamos as variáveis de ambiente do arquivo _.env_.

- Depois disso, definimos o endpoint, chave para a API da OpenAI, versão e tipo.

- Em seguida, geramos a imagem:

  O código acima responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar a URL para baixar a imagem e salvá-la em um arquivo.

- Por fim, abrimos a imagem e usamos o visualizador de imagens padrão para exibi-la:

### Mais detalhes sobre a geração da imagem

Vamos olhar o código que gera a imagem em mais detalhes:

- **prompt**, é o prompt textual usado para gerar a imagem. Neste caso, estamos usando o prompt "Coelho a cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos".
- **size**, é o tamanho da imagem que é gerada. Neste caso, estamos gerando uma imagem que é 1024x1024 pixels.
- **n**, é o número de imagens que são geradas. Neste caso, estamos gerando duas imagens.
- **temperature**, é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1 onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Há mais coisas que você pode fazer com imagens que vamos cobrir na próxima seção.

## Capacidades adicionais de geração de imagens

Você já viu até agora como fomos capazes de gerar uma imagem usando algumas linhas em Python. No entanto, há mais coisas que você pode fazer com imagens.

Você também pode fazer o seguinte:

- **Realizar edições**. Ao fornecer uma imagem existente, uma máscara e um prompt, você pode alterar uma imagem. Por exemplo, você pode adicionar algo a uma parte de uma imagem. Imagine nossa imagem do coelho, você pode adicionar um chapéu ao coelho. Como você faria isso é fornecendo a imagem, uma máscara (identificando a parte da área para a alteração) e um prompt textual para dizer o que deve ser feito.

  A imagem base conteria apenas o coelho, mas a imagem final teria o chapéu no coelho.

- **Criar variações**. A ideia é que você pegue uma imagem existente e peça que variações sejam criadas. Para criar uma variação, você fornece uma imagem e um prompt textual e código assim:

  > Nota, isso é suportado apenas na OpenAI

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1 onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

Agora vamos executar o mesmo prompt apenas para ver que não obteremos a mesma imagem duas vezes:

Como você pode ver, as imagens são semelhantes, mas não iguais. Vamos tentar mudar o valor da temperatura para 0.1 e ver o que acontece:

### Mudando a temperatura

Então vamos tentar tornar a resposta mais determinística. Pudemos observar nas duas imagens que geramos que na primeira imagem, há um coelho e na segunda imagem, há um cavalo, então as imagens variam bastante.

Portanto, vamos mudar nosso código e definir a temperatura para 0, assim:

Agora, quando você executa este código, obtém estas duas imagens:

Aqui você pode ver claramente como as imagens se assemelham mais.

## Como definir limites para seu aplicativo com metaprompts

Com nossa demonstração, já podemos gerar imagens para nossos clientes. No entanto, precisamos criar alguns limites para nosso aplicativo.

Por exemplo, não queremos gerar imagens que não sejam seguras para o trabalho ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts textuais que são usados para controlar a saída de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar a saída e garantir que as imagens geradas sejam seguras para o trabalho ou apropriadas para crianças.

### Como funciona?

Agora, como os metaprompts funcionam?

Metaprompts são prompts textuais que são usados para controlar a saída de um modelo de IA Generativa, eles são posicionados antes do prompt textual e são usados para controlar a saída do modelo e incorporados em aplicativos para controlar a saída do modelo. Encapsulando o prompt de entrada e o metaprompt de entrada em um único prompt textual.

Um exemplo de metaprompt seria o seguinte:

Agora, vamos ver como podemos usar metaprompts em nossa demonstração.

A partir do prompt acima, você pode ver como todas as imagens sendo criadas consideram o metaprompt.

## Tarefa - vamos capacitar os alunos

Introduzimos a Edu4All no início desta lição. Agora é hora de capacitar os alunos a gerar imagens para suas avaliações.

Os alunos criarão imagens para suas avaliações contendo monumentos, exatamente quais monumentos fica a critério dos alunos. Os alunos são convidados a usar sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

## Solução

Aqui está uma possível solução:

## Bom Trabalho! Continue Seu Aprendizado

Após concluir esta lição, confira nossa [coleção de aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 10, onde veremos como [construir aplicativos de IA com baixo código](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, é recomendada a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.