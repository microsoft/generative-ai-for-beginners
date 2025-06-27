<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:16:48+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pt"
}
-->
# Construindo Aplicações de Geração de Imagens

[![Construindo Aplicações de Geração de Imagens](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.pt.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Há mais nos LLMs do que apenas geração de texto. Também é possível gerar imagens a partir de descrições textuais. Ter imagens como uma modalidade pode ser extremamente útil em várias áreas, desde MedTech, arquitetura, turismo, desenvolvimento de jogos e muito mais. Neste capítulo, vamos explorar os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, vamos abordar:

- Geração de imagens e por que é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como você pode construir um aplicativo de geração de imagens.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

- Construir uma aplicação de geração de imagens.
- Definir limites para sua aplicação com meta prompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir uma aplicação de geração de imagens?

Aplicações de geração de imagens são uma ótima maneira de explorar as capacidades da IA Generativa. Elas podem ser usadas, por exemplo:

- **Edição e síntese de imagens**. Você pode gerar imagens para uma variedade de casos de uso, como edição e síntese de imagens.

- **Aplicação em diversos setores**. Elas também podem ser usadas para gerar imagens para uma variedade de setores como Medtech, Turismo, Desenvolvimento de Jogos e mais.

## Cenário: Edu4All

Como parte desta lição, continuaremos a trabalhar com nossa startup, Edu4All. Os alunos criarão imagens para suas avaliações, exatamente quais imagens fica a critério dos alunos, mas elas podem ser ilustrações para seu próprio conto de fadas ou criar um novo personagem para sua história ou ajudá-los a visualizar suas ideias e conceitos.

Aqui está o que os alunos do Edu4All poderiam gerar, por exemplo, se estivessem trabalhando em sala de aula sobre monumentos:

![Startup Edu4All, aula sobre monumentos, Torre Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.pt.png)

usando um prompt como

> "Cachorro ao lado da Torre Eiffel ao nascer do sol"

## O que é DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, eles permitem que você use prompts para gerar imagens.

### DALL-E

Vamos começar com o DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições textuais.

> [DALL-E é uma combinação de dois modelos, CLIP e atenção difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Atenção difusa**, é um modelo que gera imagens a partir de embeddings. DALL-E é treinado em um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com um chapéu, ou um cachorro com um moicano.

### Midjourney

O Midjourney funciona de maneira semelhante ao DALL-E, ele gera imagens a partir de prompts textuais. O Midjourney também pode ser usado para gerar imagens usando prompts como “um gato com um chapéu” ou “um cachorro com um moicano”.

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem Wikipedia, imagem gerada pelo Midjourney_

## Como DALL-E e Midjourney Funcionam

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autorregressivo_.

Um _transformer autorregressivo_ define como um modelo gera imagens a partir de descrições textuais, ele gera um pixel de cada vez, e depois usa os pixels gerados para gerar o próximo pixel. Passando por várias camadas em uma rede neural, até que a imagem esteja completa.

Com este processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. No entanto, o DALL-E 2 e 3 têm mais controle sobre a imagem gerada.

## Construindo sua primeira aplicação de geração de imagens

Então, o que é necessário para construir uma aplicação de geração de imagens? Você precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendado usar esta biblioteca para manter seus segredos em um arquivo _.env_ longe do código.
- **openai**, esta biblioteca é o que você usará para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudá-lo a fazer solicitações HTTP.

1. Crie um arquivo _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Localize estas informações no Portal Azure para seu recurso na seção "Chaves e Endpoint".

1. Colete as bibliotecas acima em um arquivo chamado _requirements.txt_ assim:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Em seguida, crie um ambiente virtual e instale as bibliotecas:

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
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

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
   except openai.InvalidRequestError as err:
       print(err)

   ```

Vamos explicar este código:

- Primeiro, importamos as bibliotecas que precisamos, incluindo a biblioteca OpenAI, a biblioteca dotenv, a biblioteca requests e a biblioteca Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Em seguida, carregamos as variáveis de ambiente do arquivo _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Depois disso, definimos o endpoint, chave para a API da OpenAI, versão e tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Em seguida, geramos a imagem:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  O código acima responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar a URL para baixar a imagem e salvá-la em um arquivo.

- Por último, abrimos a imagem e usamos o visualizador de imagens padrão para exibi-la:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mais detalhes sobre a geração da imagem

Vamos examinar o código que gera a imagem em mais detalhes:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, é o prompt textual usado para gerar a imagem. Neste caso, estamos usando o prompt "Coelho em um cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos".
- **size**, é o tamanho da imagem que é gerada. Neste caso, estamos gerando uma imagem de 1024x1024 pixels.
- **n**, é o número de imagens que são geradas. Neste caso, estamos gerando duas imagens.
- **temperature**, é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Há mais coisas que você pode fazer com imagens que abordaremos na próxima seção.

## Capacidades adicionais da geração de imagens

Você viu até agora como conseguimos gerar uma imagem usando algumas linhas em Python. No entanto, há mais coisas que você pode fazer com imagens.

Você também pode fazer o seguinte:

- **Realizar edições**. Ao fornecer uma imagem existente, uma máscara e um prompt, você pode alterar uma imagem. Por exemplo, você pode adicionar algo a uma parte de uma imagem. Imagine nossa imagem do coelho, você pode adicionar um chapéu ao coelho. Como você faria isso é fornecendo a imagem, uma máscara (identificando a parte da área para a mudança) e um prompt de texto para dizer o que deve ser feito.

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

  A imagem base conteria apenas o coelho, mas a imagem final teria o chapéu no coelho.

- **Criar variações**. A ideia é que você pegue uma imagem existente e peça que variações sejam criadas. Para criar uma variação, você fornece uma imagem e um prompt de texto e código assim:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, isso é suportado apenas no OpenAI

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt: "Coelho em um cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos"

![Coelho em um cavalo segurando um pirulito, versão 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.pt.png)

Agora vamos executar o mesmo prompt apenas para ver que não obteremos a mesma imagem duas vezes:

![Imagem gerada de coelho em cavalo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.pt.png)

Como você pode ver, as imagens são semelhantes, mas não idênticas. Vamos tentar mudar o valor da temperatura para 0.1 e ver o que acontece:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mudando a temperatura

Então, vamos tentar tornar a resposta mais determinística. Pudemos observar nas duas imagens que geramos que na primeira imagem, há um coelho e na segunda imagem, há um cavalo, então as imagens variam muito.

Vamos, portanto, mudar nosso código e definir a temperatura para 0, assim:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora, quando você executa este código, você obtém estas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.pt.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.pt.png)

Aqui você pode ver claramente como as imagens se assemelham mais.

## Como definir limites para sua aplicação com metaprompts

Com nosso demo, já podemos gerar imagens para nossos clientes. No entanto, precisamos criar alguns limites para nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam seguras para o trabalho, ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar a saída e garantir que as imagens geradas sejam seguras para o trabalho ou apropriadas para crianças.

### Como funciona?

Agora, como os metaprompts funcionam?

Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA Generativa, eles são posicionados antes do prompt de texto e são usados para controlar a saída do modelo e incorporados em aplicações para controlar a saída do modelo. Encapsulando a entrada do prompt e a entrada do metaprompt em um único prompt de texto.

Um exemplo de metaprompt seria o seguinte:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Agora, vamos ver como podemos usar metaprompts em nosso demo.

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
```

Pelo prompt acima, você pode ver como todas as imagens criadas consideram o metaprompt.

## Tarefa - vamos capacitar os alunos

Introduzimos o Edu4All no início desta lição. Agora é hora de capacitar os alunos a gerar imagens para suas avaliações.

Os alunos criarão imagens para suas avaliações contendo monumentos, exatamente quais monumentos fica a critério dos alunos. Os alunos são incentivados a usar sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

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

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
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
except openai.InvalidRequestError as err:
    print(err)
```

## Ótimo Trabalho! Continue Seu Aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 10, onde veremos como [construir aplicações de IA com baixo código](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se uma tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.