<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:30:57+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "br"
}
-->
# Construindo Aplicações de Geração de Imagens

[![Construindo Aplicações de Geração de Imagens](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.br.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Os LLMs vão além da geração de texto. Também é possível gerar imagens a partir de descrições textuais. Ter imagens como uma modalidade pode ser altamente útil em várias áreas, desde MedTech, arquitetura, turismo, desenvolvimento de jogos e mais. Neste capítulo, vamos explorar os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, vamos abordar:

- Geração de imagens e por que é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como você construiria um aplicativo de geração de imagens.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

- Construir uma aplicação de geração de imagens.
- Definir limites para sua aplicação com metaprompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir uma aplicação de geração de imagens?

Aplicações de geração de imagens são uma ótima maneira de explorar as capacidades da IA Generativa. Elas podem ser usadas, por exemplo, para:

- **Edição e síntese de imagens**. Você pode gerar imagens para uma variedade de casos de uso, como edição e síntese de imagens.

- **Aplicadas a uma variedade de indústrias**. Elas também podem ser usadas para gerar imagens para várias indústrias, como MedTech, Turismo, Desenvolvimento de Jogos e mais.

## Cenário: Edu4All

Como parte desta lição, continuaremos a trabalhar com nossa startup, Edu4All. Os estudantes criarão imagens para suas avaliações, exatamente quais imagens fica a critério dos estudantes, mas podem ser ilustrações para seu próprio conto de fadas ou criar um novo personagem para sua história ou ajudá-los a visualizar suas ideias e conceitos.

Aqui está o que os estudantes da Edu4All poderiam gerar, por exemplo, se estivessem trabalhando em sala de aula sobre monumentos:

![Startup Edu4All, aula sobre monumentos, Torre Eiffel](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.br.png)

usando um prompt como

> "Cachorro ao lado da Torre Eiffel no início da manhã"

## O que é DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, permitindo que você use prompts para gerar imagens.

### DALL-E

Vamos começar com o DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições textuais.

> [DALL-E é uma combinação de dois modelos, CLIP e atenção difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Atenção difusa**, é um modelo que gera imagens a partir de embeddings. O DALL-E é treinado em um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com um chapéu, ou um cachorro com um moicano.

### Midjourney

O Midjourney funciona de forma semelhante ao DALL-E, gerando imagens a partir de prompts textuais. O Midjourney também pode ser usado para gerar imagens usando prompts como “um gato com um chapéu” ou um “cachorro com um moicano”.

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem Wikipedia, imagem gerada pelo Midjourney_

## Como o DALL-E e o Midjourney Funcionam

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). O DALL-E é um modelo de IA Generativa baseado na arquitetura de transformadores com um _transformador autorregressivo_.

Um _transformador autorregressivo_ define como um modelo gera imagens a partir de descrições textuais, gerando um pixel de cada vez e, em seguida, usando os pixels gerados para gerar o próximo pixel. Passando por várias camadas em uma rede neural, até que a imagem esteja completa.

Com este processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. No entanto, o DALL-E 2 e 3 têm mais controle sobre a imagem gerada.

## Construindo sua primeira aplicação de geração de imagens

Então, o que é necessário para construir uma aplicação de geração de imagens? Você precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendado usar esta biblioteca para manter seus segredos em um arquivo _.env_ separado do código.
- **openai**, esta biblioteca é o que você usará para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudá-lo a fazer requisições HTTP.

1. Crie um arquivo _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Localize esta informação no Portal do Azure para seu recurso na seção "Chaves e Endpoint".

1. Reúna as bibliotecas acima em um arquivo chamado _requirements.txt_ assim:

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

- Primeiro, importamos as bibliotecas necessárias, incluindo a biblioteca OpenAI, a biblioteca dotenv, a biblioteca requests e a biblioteca Pillow.

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

Vamos analisar o código que gera a imagem em mais detalhes:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, é o prompt textual usado para gerar a imagem. Neste caso, estamos usando o prompt "Coelho a cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos".
- **size**, é o tamanho da imagem gerada. Neste caso, estamos gerando uma imagem de 1024x1024 pixels.
- **n**, é o número de imagens geradas. Neste caso, estamos gerando duas imagens.
- **temperature**, é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Há mais coisas que você pode fazer com imagens que cobriremos na próxima seção.

## Capacidades adicionais da geração de imagens

Você viu até agora como conseguimos gerar uma imagem usando algumas linhas em Python. No entanto, há mais coisas que você pode fazer com imagens.

Você também pode fazer o seguinte:

- **Realizar edições**. Fornecendo uma imagem existente, uma máscara e um prompt, você pode alterar uma imagem. Por exemplo, você pode adicionar algo a uma parte de uma imagem. Imagine nossa imagem do coelho, você pode adicionar um chapéu ao coelho. Como você faria isso é fornecendo a imagem, uma máscara (identificando a parte da área para a alteração) e um prompt de texto para dizer o que deve ser feito.

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

- **Criar variações**. A ideia é que você pegue uma imagem existente e peça que sejam criadas variações. Para criar uma variação, você fornece uma imagem e um prompt de texto e um código assim:

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

A temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt: "Coelho a cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos"

![Coelho a cavalo segurando um pirulito, versão 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.br.png)

Agora vamos executar o mesmo prompt apenas para ver que não obteremos a mesma imagem duas vezes:

![Imagem gerada de coelho a cavalo](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.br.png)

Como você pode ver, as imagens são semelhantes, mas não iguais. Vamos tentar mudar o valor da temperatura para 0.1 e ver o que acontece:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mudando a temperatura

Então, vamos tentar tornar a resposta mais determinística. Podemos observar das duas imagens que geramos que na primeira imagem há um coelho e na segunda imagem há um cavalo, então as imagens variam bastante.

Vamos, portanto, mudar nosso código e definir a temperatura para 0, assim:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora, quando você executa este código, obtém estas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.br.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.br.png)

Aqui você pode ver claramente como as imagens se assemelham mais.

## Como definir limites para sua aplicação com metaprompts

Com nossa demonstração, já podemos gerar imagens para nossos clientes. No entanto, precisamos criar alguns limites para nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam seguras para o trabalho ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts textuais usados para controlar a saída de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar a saída e garantir que as imagens geradas sejam seguras para o trabalho ou apropriadas para crianças.

### Como funciona?

Agora, como os metaprompts funcionam?

Metaprompts são prompts textuais usados para controlar a saída de um modelo de IA Generativa, eles são posicionados antes do prompt textual e são usados para controlar a saída do modelo e são incorporados em aplicações para controlar a saída do modelo. Encapsulando a entrada do prompt e a entrada do metaprompt em um único prompt textual.

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

Agora, vamos ver como podemos usar metaprompts em nossa demonstração.

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

## Tarefa - vamos capacitar os estudantes

Introduzimos a Edu4All no início desta lição. Agora é hora de capacitar os estudantes para gerar imagens para suas avaliações.

Os estudantes criarão imagens para suas avaliações contendo monumentos, exatamente quais monumentos fica a critério dos estudantes. Os estudantes são convidados a usar sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

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

## Ótimo Trabalho! Continue seu Aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 10, onde vamos explorar como [construir aplicações de IA com low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, é recomendada a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.