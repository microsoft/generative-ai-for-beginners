<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:23:49+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "br"
}
-->
# Construindo Aplicações de Geração de Imagens

[![Construindo Aplicações de Geração de Imagens](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.br.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs vão além da geração de texto. Também é possível gerar imagens a partir de descrições em texto. Ter imagens como uma modalidade pode ser extremamente útil em diversas áreas, como MedTech, arquitetura, turismo, desenvolvimento de jogos e muito mais. Neste capítulo, vamos explorar os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, vamos abordar:

- Geração de imagens e por que ela é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como construir uma aplicação de geração de imagens.

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

- Construir uma aplicação de geração de imagens.
- Definir limites para sua aplicação com metaprompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir uma aplicação de geração de imagens?

Aplicações de geração de imagens são uma ótima forma de explorar as capacidades da IA Generativa. Elas podem ser usadas, por exemplo, para:

- **Edição e síntese de imagens**. Você pode gerar imagens para diversos casos de uso, como edição e síntese de imagens.

- **Aplicação em várias indústrias**. Também podem ser usadas para gerar imagens para diferentes setores, como MedTech, Turismo, Desenvolvimento de jogos e outros.

## Cenário: Edu4All

Como parte desta lição, continuaremos trabalhando com nossa startup, Edu4All. Os estudantes criarão imagens para suas avaliações; quais imagens exatamente fica a critério deles, mas podem ser ilustrações para seus próprios contos de fadas, criar um novo personagem para suas histórias ou ajudar a visualizar suas ideias e conceitos.

Veja o que os estudantes da Edu4All poderiam gerar, por exemplo, se estiverem trabalhando em sala sobre monumentos:

![Edu4All startup, aula sobre monumentos, Torre Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.br.png)

usando um prompt como

> "Cachorro ao lado da Torre Eiffel na luz do sol da manhã cedo"

## O que são DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, que permitem usar prompts para gerar imagens.

### DALL-E

Vamos começar com o DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições em texto.

> [DALL-E é uma combinação de dois modelos, CLIP e diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** é um modelo que gera embeddings, que são representações numéricas dos dados, a partir de imagens e texto.

- **Diffused attention** é um modelo que gera imagens a partir dos embeddings. O DALL-E é treinado em um conjunto de dados de imagens e textos e pode ser usado para gerar imagens a partir de descrições em texto. Por exemplo, o DALL-E pode gerar imagens de um gato com chapéu ou um cachorro com moicano.

### Midjourney

O Midjourney funciona de forma semelhante ao DALL-E, gerando imagens a partir de prompts em texto. O Midjourney também pode ser usado para gerar imagens com prompts como “um gato com chapéu” ou “um cachorro com moicano”.

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem Wikipedia, imagem gerada pelo Midjourney_

## Como funcionam DALL-E e Midjourney

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). O DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autoregressivo_.

Um _transformer autoregressivo_ define como o modelo gera imagens a partir de descrições em texto, gerando um pixel por vez e usando os pixels gerados para criar o próximo pixel. Passa por múltiplas camadas em uma rede neural até que a imagem esteja completa.

Com esse processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. No entanto, o DALL-E 2 e 3 oferecem maior controle sobre a imagem gerada.

## Construindo sua primeira aplicação de geração de imagens

Então, o que é necessário para construir uma aplicação de geração de imagens? Você precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendado usar essa biblioteca para manter seus segredos em um arquivo _.env_ separado do código.
- **openai**, essa biblioteca é o que você usará para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudar a fazer requisições HTTP.

1. Crie um arquivo _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Localize essas informações no Portal do Azure para seu recurso na seção "Chaves e Endpoint".

1. Liste as bibliotecas acima em um arquivo chamado _requirements.txt_ assim:

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

Vamos explicar esse código:

- Primeiro, importamos as bibliotecas necessárias, incluindo a biblioteca OpenAI, dotenv, requests e Pillow.

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

- Depois, definimos o endpoint, a chave da API OpenAI, a versão e o tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Agora, geramos a imagem:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  O código acima responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar essa URL para baixar a imagem e salvá-la em um arquivo.

- Por fim, abrimos a imagem e usamos o visualizador padrão para exibi-la:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mais detalhes sobre a geração da imagem

Vamos analisar o código que gera a imagem com mais detalhes:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** é o texto usado para gerar a imagem. Neste caso, usamos o prompt "Coelho em cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos".
- **size** é o tamanho da imagem gerada. Aqui, estamos gerando uma imagem de 1024x1024 pixels.
- **n** é o número de imagens geradas. Neste caso, estamos gerando duas imagens.
- **temperature** é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura varia entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0,7.

Existem outras coisas que você pode fazer com imagens, que abordaremos na próxima seção.

## Capacidades adicionais da geração de imagens

Até agora, você viu como gerar uma imagem usando poucas linhas em Python. No entanto, há mais possibilidades com imagens.

Você também pode:

- **Realizar edições**. Fornecendo uma imagem existente, uma máscara e um prompt, você pode alterar uma imagem. Por exemplo, pode adicionar algo a uma parte da imagem. Imagine nossa imagem do coelho, você pode adicionar um chapéu ao coelho. Para isso, você fornece a imagem, uma máscara (identificando a área a ser alterada) e um prompt de texto dizendo o que deve ser feito.

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

- **Criar variações**. A ideia é pegar uma imagem existente e pedir que variações sejam criadas. Para criar uma variação, você fornece uma imagem e um prompt de texto, e o código fica assim:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota: isso é suportado apenas na OpenAI

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura varia entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0,7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt: "Coelho em cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos"

![Coelho em cavalo segurando um pirulito, versão 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.br.png)

Agora vamos executar o mesmo prompt novamente para ver que não obteremos a mesma imagem duas vezes:

![Imagem gerada de coelho em cavalo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.br.png)

Como você pode ver, as imagens são parecidas, mas não idênticas. Vamos tentar mudar o valor da temperatura para 0,1 e ver o que acontece:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Alterando a temperatura

Vamos tentar tornar a resposta mais determinística. Podemos observar nas duas imagens geradas que na primeira há um coelho e na segunda um cavalo, então as imagens variam bastante.

Vamos então alterar nosso código e definir a temperatura para 0, assim:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora, ao executar esse código, você obterá estas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.br.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.br.png)

Aqui você pode ver claramente como as imagens se parecem mais entre si.

## Como definir limites para sua aplicação com metaprompts

Com nossa demonstração, já podemos gerar imagens para nossos clientes. No entanto, precisamos criar alguns limites para nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam adequadas para o ambiente de trabalho ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para garantir que as imagens geradas sejam seguras para o trabalho ou apropriadas para crianças.

### Como funciona?

Agora, como funcionam os metaprompts?

Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA Generativa, eles são posicionados antes do prompt de texto e usados para controlar a saída do modelo, sendo incorporados em aplicações para esse controle. Eles encapsulam a entrada do prompt e a entrada do metaprompt em um único prompt de texto.

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

Apresentamos a Edu4All no início desta lição. Agora é hora de capacitar os estudantes a gerar imagens para suas avaliações.

Os estudantes criarão imagens para suas avaliações contendo monumentos; quais monumentos exatamente fica a critério deles. Eles são convidados a usar a criatividade para colocar esses monumentos em diferentes contextos.

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

prompt = f"""{meta_prompt}
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

## Excelente trabalho! Continue seu aprendizado

Após concluir esta lição, confira nossa [coleção de Aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seus conhecimentos em IA Generativa!

Siga para a Lição 10, onde veremos como [construir aplicações de IA com low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.