<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:23:24+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pt"
}
-->
# Construir Aplicações de Geração de Imagens

[![Construir Aplicações de Geração de Imagens](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.pt.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Os LLMs não se limitam à geração de texto. Também é possível gerar imagens a partir de descrições textuais. Ter imagens como modalidade pode ser extremamente útil em várias áreas, desde MedTech, arquitetura, turismo, desenvolvimento de jogos e muito mais. Neste capítulo, vamos explorar os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, vamos abordar:

- Geração de imagens e por que é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como construir uma aplicação de geração de imagens.

## Objetivos de Aprendizagem

Após completar esta lição, serás capaz de:

- Construir uma aplicação de geração de imagens.
- Definir limites para a tua aplicação com metaprompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir uma aplicação de geração de imagens?

As aplicações de geração de imagens são uma excelente forma de explorar as capacidades da IA Generativa. Podem ser usadas, por exemplo, para:

- **Edição e síntese de imagens**. Podes gerar imagens para vários casos de uso, como edição e síntese de imagens.

- **Aplicação em diversas indústrias**. Também podem ser usadas para gerar imagens para várias indústrias, como Medtech, Turismo, Desenvolvimento de jogos e outras.

## Cenário: Edu4All

Como parte desta lição, vamos continuar a trabalhar com a nossa startup, Edu4All. Os alunos vão criar imagens para as suas avaliações; que imagens exatamente, fica ao critério dos alunos, mas podem ser ilustrações para o seu próprio conto de fadas, criar um novo personagem para a sua história ou ajudar a visualizar as suas ideias e conceitos.

Aqui está um exemplo do que os alunos da Edu4All poderiam gerar se estiverem a trabalhar em aula sobre monumentos:

![Edu4All startup, aula sobre monumentos, Torre Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.pt.png)

usando um prompt como

> "Cão ao lado da Torre Eiffel ao nascer do sol"

## O que são DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, que permitem usar prompts para gerar imagens.

### DALL-E

Vamos começar pelo DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições textuais.

> [DALL-E é uma combinação de dois modelos, CLIP e diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Diffused attention** é um modelo que gera imagens a partir dos embeddings. O DALL-E é treinado com um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com chapéu, ou um cão com moicano.

### Midjourney

O Midjourney funciona de forma semelhante ao DALL-E, gerando imagens a partir de prompts textuais. O Midjourney também pode ser usado para gerar imagens com prompts como “um gato com chapéu” ou “um cão com moicano”.

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem Wikipedia, imagem gerada pelo Midjourney_

## Como funcionam o DALL-E e o Midjourney

Comecemos pelo [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). O DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autoregressivo_.

Um _transformer autoregressivo_ define como um modelo gera imagens a partir de descrições textuais, gerando um pixel de cada vez e depois usando os pixels gerados para criar o próximo pixel. Passa por múltiplas camadas numa rede neural até a imagem estar completa.

Com este processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. No entanto, o DALL-E 2 e 3 têm um controlo ainda maior sobre a imagem gerada.

## Construir a tua primeira aplicação de geração de imagens

Então, o que é necessário para construir uma aplicação de geração de imagens? Precisarás das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendado usar esta biblioteca para manter os teus segredos num ficheiro _.env_ separado do código.
- **openai**, esta biblioteca é o que vais usar para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudar a fazer pedidos HTTP.

1. Cria um ficheiro _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Encontra esta informação no Portal Azure para o teu recurso na secção "Chaves e Endpoint".

1. Reúne as bibliotecas acima num ficheiro chamado _requirements.txt_ assim:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. De seguida, cria um ambiente virtual e instala as bibliotecas:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para Windows, usa os seguintes comandos para criar e ativar o ambiente virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Adiciona o seguinte código num ficheiro chamado _app.py_:

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

- Primeiro, importamos as bibliotecas necessárias, incluindo a biblioteca OpenAI, a dotenv, a requests e a Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Depois, carregamos as variáveis de ambiente do ficheiro _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Em seguida, definimos o endpoint, a chave para a API OpenAI, a versão e o tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

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

  O código acima responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar essa URL para descarregar a imagem e guardá-la num ficheiro.

- Por fim, abrimos a imagem e usamos o visualizador de imagens padrão para a mostrar:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mais detalhes sobre a geração da imagem

Vamos analisar o código que gera a imagem com mais detalhe:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** é o texto usado para gerar a imagem. Neste caso, estamos a usar o prompt "Coelho em cavalo, segurando um pirulito, num prado enevoado onde crescem narcisos".
- **size** é o tamanho da imagem gerada. Neste caso, estamos a gerar uma imagem de 1024x1024 pixels.
- **n** é o número de imagens geradas. Neste caso, estamos a gerar duas imagens.
- **temperature** é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura varia entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Existem mais coisas que podes fazer com imagens, que vamos abordar na próxima secção.

## Capacidades adicionais da geração de imagens

Até agora viste como conseguimos gerar uma imagem com poucas linhas em Python. No entanto, há mais possibilidades com imagens.

Podes também fazer o seguinte:

- **Realizar edições**. Ao fornecer uma imagem existente, uma máscara e um prompt, podes alterar uma imagem. Por exemplo, podes adicionar algo a uma parte da imagem. Imagina a nossa imagem do coelho, podes adicionar um chapéu ao coelho. Para isso, forneces a imagem, uma máscara (identificando a área a alterar) e um prompt textual a indicar o que deve ser feito.

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

- **Criar variações**. A ideia é pegar numa imagem existente e pedir que sejam criadas variações. Para criar uma variação, forneces uma imagem e um prompt textual e código assim:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, isto é suportado apenas na OpenAI

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura varia entre 0 e 1, onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt : "Coelho em cavalo, segurando um pirulito, num prado enevoado onde crescem narcisos"

![Coelho em cavalo segurando um pirulito, versão 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.pt.png)

Agora vamos executar o mesmo prompt só para ver que não vamos obter a mesma imagem duas vezes:

![Imagem gerada de coelho em cavalo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.pt.png)

Como podes ver, as imagens são semelhantes, mas não iguais. Vamos tentar mudar o valor da temperatura para 0.1 e ver o que acontece:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Alterar a temperatura

Vamos tentar tornar a resposta mais determinística. Podemos observar pelas duas imagens que gerámos que na primeira imagem há um coelho e na segunda há um cavalo, portanto as imagens variam bastante.

Vamos então alterar o nosso código e definir a temperatura para 0, assim:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora, quando executares este código, vais obter estas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.pt.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.pt.png)

Aqui podes ver claramente como as imagens se parecem mais entre si.

## Como definir limites para a tua aplicação com metaprompts

Com a nossa demo, já podemos gerar imagens para os nossos clientes. No entanto, precisamos de criar alguns limites para a nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam seguras para o trabalho, ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts textuais usados para controlar a saída de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar a saída e garantir que as imagens geradas são seguras para o trabalho ou apropriadas para crianças.

### Como funciona?

Então, como funcionam os metaprompts?

Metaprompts são prompts textuais usados para controlar a saída de um modelo de IA Generativa, são posicionados antes do prompt textual e usados para controlar a saída do modelo, sendo incorporados em aplicações para controlar a saída do modelo. Envolvendo o input do prompt e o input do metaprompt num único prompt textual.

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

Agora, vamos ver como podemos usar metaprompts na nossa demo.

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

A partir do prompt acima, podes ver como todas as imagens criadas consideram o metaprompt.

## Exercício - vamos capacitar os alunos

Apresentámos a Edu4All no início desta lição. Agora é altura de capacitar os alunos para gerar imagens para as suas avaliações.

Os alunos vão criar imagens para as suas avaliações contendo monumentos, exatamente quais monumentos fica ao critério dos alunos. Os alunos são convidados a usar a sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

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

## Excelente trabalho! Continua a aprender

Após completares esta lição, consulta a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuares a aprofundar os teus conhecimentos em IA Generativa!

Segue para a Lição 10 onde vamos ver como [construir aplicações de IA com low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.