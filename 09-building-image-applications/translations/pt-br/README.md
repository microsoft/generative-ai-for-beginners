# Criando aplicativos de geração de imagens

[![Building Image Generation Applications](../../images/09-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Ainda há muito mais que os LLMs podem fazer além da geração de texto. Também é possível gerar imagens a partir de descrições de texto. Ter imagens como modalidade pode ser altamente útil em uma série de áreas, desde MedTech, arquitetura, turismo, desenvolvimento de jogos e muito mais. Neste capítulo, veremos os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introduction

In this lesson, we will cover:

- Image generation and why it's useful.
- DALL-E and Midjourney, what they are, and how they work.
- How you would build an image generation app.

## Learning Goals

After completing this lesson, you will be able to:

- Build an image generation application.
- Define boundaries for your application with meta prompts.
- Work with DALL-E and Midjourney.

## Why build an image generation application?

Image generation applications are a great way to explore the capabilities of Generative AI. They can be used for, for example:

- **Image editing and synthesis**. You can generate images for a variety of use cases, such as image editing and image synthesis.

- **Applied to a variety of industries**. They can also be used to generate images for a variety of industries like Medtech, Tourism, Game development and more.

## Scenario: Edu4All

As part of this lesson, we will continue to work with our startup, Edu4All, in this lesson. The students will create images for their assessments, exactly what images is up to the students, but they could be illustrations for their own fairytale or create a new character for their story or help them visualize their ideas and concepts.

Here's what Edu4All's students could generate for example if they're working in class on monuments:

![Edu4All startup, class on monuments, Eiffel Tower](../../images/startup.png?WT.mc_id=academic-105485-koreyst)

using a prompt like

## Introdução

Nesta lição, abordaremos:

- Geração de imagens e por que é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como criar uma aplicação de geração de imagens.

## Metas de Aprendizado

Após completar esta lição, você será capaz de:

- Criar uma aplicação de geração de imagens.
- Definir limites para o seu aplicativo com meta-prompts.
- Trabalhar com DALL-E e Midjourney.

## Por que criar um aplicativo de geração de imagens?

Aplicativos de geração de imagens são uma ótima maneira de explorar as capacidades da Inteligência Artificial Generativa. Eles podem ser usados, por exemplo:

- **Edição e síntese de imagens**: Você pode gerar imagens para uma variedade de casos de uso, como edição e síntese de imagens.

- **Aplicados a várias indústrias**: Eles também podem ser usados para gerar imagens para diversas indústrias como: Medtech, Turismo, Desenvolvimento de Jogos e muito mais.

## Cenário: Edu4All

Como parte desta lição, continuaremos a trabalhar com nossa startup, Edu4All. Os estudantes criarão imagens para suas avaliações, exatamente quais imagens ficam a critério dos estudantes, mas podem ser ilustrações para seu próprio conto de fadas, criar um novo personagem para sua história ou ajudá-los a visualizar suas ideias e conceitos.

Veja o que os estudantes da Edu4All poderiam gerar, por exemplo, se estivessem trabalhando em sala de aula sobre monumentos:

![Edu4All startup, aula sobre monumentos, Torre Eiffel](../../images/startup.png?WT.mc_id=academic-105485-koreyst)

usando um prompt como:

> "Dog next to Eiffel Tower in early morning sunlight"

## O que é DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, eles permitem que você use prompts para gerar imagens.

### DALL-E

Vamos começar com o DALL-E, que é um modelo de Inteligência Artificial Generativa que gera imagens a partir de descrições de texto.

> [DALL-E é uma combinação de dois modelos, CLIP e atenção difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Atenção difusa** é um modelo que gera imagens a partir de embeddings. O DALL-E é treinado em um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições de texto. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com chapéu ou um cachorro com um moicano.

### Midjourney

Midjourney funciona de maneira semelhante ao DALL-E, gerando imagens a partir de prompts de texto. Midjourney também pode ser usado para gerar imagens usando prompts como "um gato com chapéu" ou "um cachorro com um moicano".

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Créditos da imagem: Wikipedia, imagem gerada pelo Midjourney_

## Como DALL-E e Midjourney Funcionam

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E é um modelo de Inteligência Artificial Generativa baseado na arquitetura do transformer com um _transformer autoregressivo_.

Um _transformer autoregressivo_ define como um modelo gera imagens a partir de descrições de texto, gerando um pixel de cada vez e, em seguida, usando os pixels gerados para gerar o próximo pixel. Passando por várias camadas em uma rede neural, até que a imagem esteja completa.

Com esse processo, o DALL-E controla atributos, objetos, características e muito mais na imagem que gera. No entanto, DALL-E 2 e 3 têm mais controle sobre a imagem gerada.

## Criando seu primeiro aplicativo de geração de imagens

Então, o que é necessário para construir um aplicativo de geração de imagens? Você precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendável usar esta biblioteca para manter suas informações confidenciais em um arquivo _.env_ longe do código.
- **openai**, esta biblioteca é o que você usará para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudar você a fazer solicitações HTTP.

1. Crie um arquivo _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_KEY=<your key>
   ```

   Encontre essas informações no Portal do Azure para o seu recurso na seção "Chaves e Endpoint".

1. Cole as bibliotecas acima em um arquivo chamado _requirements.txt_ assim:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Depois, crie um ambiente virtual e instale as bibliotecas:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para Windows, use os seguintes comandos para criar e ativar seu ambiente virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Adicione o seguinte código em um arquivo chamado _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.error.InvalidRequestError as err:
       print(err)

   ```

Vamos explicar este código:

- Primeiro, importamos as bibliotecas de que precisamos, incluindo as bibliotecas OpenAI, dotenv, request e Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Depois, carregamos as variáveis de ambiente do arquivo _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Após isso, definimos o endpoint, a chave para a API OpenAI, a versão e o tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Depois, geramos a imagem:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Acima está o código que responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar a URL para baixar a imagem e salvá-la em um arquivo.

- Finalmente, abrimos a imagem e usamos o visualizador de imagens padrão para exibi-la:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mais detalhes sobre a geração da imagem

Vamos dar uma olhada no código que gera a imagem com mais detalhes:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** é o prompt de texto usado para gerar a imagem. Neste caso, estamos usando o prompt: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".

- **size** é o tamanho da imagem gerada. Neste caso, estamos gerando uma imagem de 1024x1024 pixels.

- **n** é o número de imagens geradas. Neste caso, estamos gerando duas imagens.

- **temperature** é um parâmetro que controla a aleatoriedade da saída de um modelo de Inteligência Artificial Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Há mais coisas que você pode fazer com imagens que abordaremos na próxima seção.

## Mais capacidades de geração de imagens

Você viu até agora como conseguimos gerar uma imagem usando algumas linhas em Python. No entanto, há mais coisas que você pode fazer com imagens.

Você também pode fazer o seguinte:

- **Perform edits**. By providing an existing image a mask and a prompt, you can alter an image. For example, you can add something to a portion of an image. Imagine our bunny image, you can add a hat to the bunny. How you would do that is by providing the image, a mask (identifying the part of the area for the change) and a text prompt to say what should be done.

- **Realizar edições**: Ao fornecer uma imagem existente, uma máscara e um prompt, você pode alterar uma imagem. Por exemplo, você pode adicionar algo a uma parte de uma imagem. Imagine nossa imagem de coelho, você pode adicionar um chapéu ao coelho. Como você faria isso é fornecendo a imagem, uma máscara (identificando a parte da área para a mudança) e um prompt de texto para dizer o que deve ser feito.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  A base da imagem conteria apenas o coelho, mas a imagem final teria o chapéu no coelho.

- **Criar variações**: A ideia é que você pegue uma imagem existente e peça que sejam criadas variações. Para criar uma variação, você fornece uma imagem e um prompt de texto e o código é assim:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Observação: isso é suportado apenas no OpenAI

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de Inteligência Artificial Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Vamos dar uma olhada em um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../images/v1-generated-image.png?WT.mc_id=academic-105485-koreyst)

Agora, vamos executar o mesmo prompt apenas para ver que não obteremos a mesma imagem duas vezes:

![Generated image of bunny on horse](../../images/v2-generated-image.png?WT.mc_id=academic-105485-koreyst)

Como você pode ver, as imagens são semelhantes, mas não são as mesmas. Vamos tentar mudar o valor da temperatura para 0.1 e ver o que acontece:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Alterando a temperatura

Agora, vamos tentar tornar a resposta mais determinística. Podemos observar pelas duas imagens que geramos que na primeira imagem há um coelho e na segunda imagem há um cavalo, então as imagens variam muito.

Vamos alterar nosso código e definir a temperatura para 0, assim:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora quando você executar este código, você obtém essas duas imagens:

- ![Temperature 0, v1](../../images/v1-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)
- ![Temperature 0 , v2](../../images/v2-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)

Aqui você pode ver claramente como as imagens se assemelham mais umas às outras.

## Como definir limites para seu aplicativo com metaprompts

Com a nossa demonstração, já podemos gerar imagens para nossos clientes. No entanto, precisamos estabelecer algumas limitações para nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam seguras para o trabalho ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts de texto que são usados para controlar a saída de um modelo de IA generativa. Por exemplo, podemos usar metaprompts para controlar a saída e garantir que as imagens geradas sejam seguras para o trabalho ou apropriadas para crianças.

### Como funciona?

Agora, como os metaprompts funcionam?

Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA generativa. Eles são posicionados antes do prompt de texto e são usados para controlar a saída do modelo, sendo incorporados em aplicativos para controlar a saída do modelo. Encapsulando a entrada do prompt e a entrada do metaprompt em um único prompt de texto.

Um exemplo de metaprompt seria o seguinte:

````text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```text

Now, let's see how we can use meta prompts in our demo.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
````

No prompt acima, você pode ver como todas as imagens sendo criadas consideram o metaprompt.

## Tarefa - vamos habilitar os estudantes

Nós introduzimos o Edu4All no início desta lição. Agora é hora de permitir que os estudantes gerem imagens para suas avaliações.

Os estudantes criarão imagens para suas avaliações contendo monumentos, exatamente quais monumentos ficam a critério dos estudantes. Os estudantes são convidados a usar sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

## Solução

Aqui está uma possível solução:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.error.InvalidRequestError as err:
    print(err)
```

## Excelente trabalho! Continue seu aprendizado

Após completar esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seus conhecimentos sobre IA generativa!

Vamos partir agora para a Lição 10, onde veremos como [Criando aplicativos de IA com Low Code](../../../10-building-low-code-ai-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)
