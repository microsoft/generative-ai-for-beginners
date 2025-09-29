<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:40:11+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pt"
}
-->
# Construção de Aplicações de Geração de Imagens

[![Construção de Aplicações de Geração de Imagens](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.pt.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Os LLMs vão além da geração de texto. Também é possível gerar imagens a partir de descrições textuais. Ter imagens como uma modalidade pode ser extremamente útil em várias áreas, como MedTech, arquitetura, turismo, desenvolvimento de jogos e muito mais. Neste capítulo, vamos explorar os dois modelos de geração de imagens mais populares: DALL-E e Midjourney.

## Introdução

Nesta lição, iremos abordar:

- Geração de imagens e por que é útil.
- DALL-E e Midjourney: o que são e como funcionam.
- Como construir uma aplicação de geração de imagens.

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

- Construir uma aplicação de geração de imagens.
- Definir limites para a sua aplicação com meta prompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir uma aplicação de geração de imagens?

As aplicações de geração de imagens são uma excelente forma de explorar as capacidades da IA Generativa. Elas podem ser usadas, por exemplo:

- **Edição e síntese de imagens**. Pode gerar imagens para diversos casos de uso, como edição e síntese de imagens.

- **Aplicação em várias indústrias**. Também podem ser usadas para gerar imagens para diversas indústrias, como MedTech, Turismo, Desenvolvimento de Jogos e mais.

## Cenário: Edu4All

Como parte desta lição, continuaremos a trabalhar com a nossa startup, Edu4All. Os alunos irão criar imagens para os seus trabalhos, sendo que o tipo de imagens fica ao critério deles. Podem ser ilustrações para o seu próprio conto de fadas, criar um novo personagem para a sua história ou ajudá-los a visualizar as suas ideias e conceitos.

Aqui está um exemplo do que os alunos da Edu4All poderiam gerar se estivessem a trabalhar em aula sobre monumentos:

![Startup Edu4All, aula sobre monumentos, Torre Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.pt.png)

usando um prompt como:

> "Cão ao lado da Torre Eiffel ao amanhecer"

## O que são DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, permitindo usar prompts para gerar imagens.

### DALL-E

Comecemos pelo DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições textuais.

> [DALL-E é uma combinação de dois modelos, CLIP e atenção difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Atenção difusa**, é um modelo que gera imagens a partir de embeddings. O DALL-E é treinado num conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com um chapéu ou de um cão com um moicano.

### Midjourney

O Midjourney funciona de forma semelhante ao DALL-E, gerando imagens a partir de prompts textuais. O Midjourney também pode ser usado para gerar imagens com prompts como "um gato com um chapéu" ou "um cão com um moicano".

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem: Wikipedia, imagem gerada pelo Midjourney_

## Como funcionam o DALL-E e o Midjourney

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). O DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autoregressivo_.

Um _transformer autoregressivo_ define como um modelo gera imagens a partir de descrições textuais, gerando um pixel de cada vez e usando os pixels gerados para gerar o próximo pixel. Passa por várias camadas numa rede neural até que a imagem esteja completa.

Com este processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. No entanto, o DALL-E 2 e 3 têm mais controlo sobre a imagem gerada.

## Construção da sua primeira aplicação de geração de imagens

Então, o que é necessário para construir uma aplicação de geração de imagens? Precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendado usar esta biblioteca para manter os seus segredos num ficheiro _.env_ separado do código.
- **openai**, esta biblioteca será usada para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudar a fazer pedidos HTTP.

## Criar e implementar um modelo Azure OpenAI

Se ainda não o fez, siga as instruções na página [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) para criar um recurso e modelo Azure OpenAI. Selecione o modelo DALL-E 3.

## Criar a aplicação

1. Crie um ficheiro _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Localize esta informação no Portal Azure OpenAI Foundry para o seu recurso na secção "Deployments".

1. Reúna as bibliotecas acima num ficheiro chamado _requirements.txt_ da seguinte forma:

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

   Para Windows, use os seguintes comandos para criar e ativar o seu ambiente virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Adicione o seguinte código num ficheiro chamado _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- Em seguida, carregamos as variáveis de ambiente do ficheiro _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Depois disso, configuramos o cliente do serviço Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- A seguir, geramos a imagem:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  O código acima responde com um objeto JSON que contém o URL da imagem gerada. Podemos usar o URL para descarregar a imagem e guardá-la num ficheiro.

- Por fim, abrimos a imagem e usamos o visualizador de imagens padrão para exibi-la:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mais detalhes sobre a geração da imagem

Vamos analisar o código que gera a imagem com mais detalhe:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, é o prompt textual usado para gerar a imagem. Neste caso, estamos a usar o prompt "Coelho a cavalo, segurando um chupa-chupa, num prado enevoado onde crescem narcisos".
- **size**, é o tamanho da imagem gerada. Neste caso, estamos a gerar uma imagem de 1024x1024 pixels.
- **n**, é o número de imagens geradas. Neste caso, estamos a gerar duas imagens.
- **temperature**, é um parâmetro que controla a aleatoriedade do resultado de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que o resultado é determinístico e 1 significa que o resultado é aleatório. O valor padrão é 0.7.

Há mais coisas que pode fazer com imagens, que iremos abordar na próxima secção.

## Capacidades adicionais de geração de imagens

Até agora, vimos como conseguimos gerar uma imagem com algumas linhas de código em Python. No entanto, há mais coisas que pode fazer com imagens.

Também pode fazer o seguinte:

- **Realizar edições**. Ao fornecer uma imagem existente, uma máscara e um prompt, pode alterar uma imagem. Por exemplo, pode adicionar algo a uma parte de uma imagem. Imagine a nossa imagem do coelho, pode adicionar um chapéu ao coelho. Para isso, deve fornecer a imagem, uma máscara (identificando a parte da área para a alteração) e um prompt textual para indicar o que deve ser feito.  
> Nota: isto não é suportado no DALL-E 3. 

Aqui está um exemplo usando GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  A imagem base conteria apenas o lounge com piscina, mas a imagem final teria um flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.pt.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.pt.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.pt.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Criar variações**. A ideia é pegar numa imagem existente e pedir que sejam criadas variações. Para criar uma variação, deve fornecer uma imagem e um prompt textual e usar código como este:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota: isto só é suportado na OpenAI.

## Temperatura

A temperatura é um parâmetro que controla a aleatoriedade do resultado de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1, onde 0 significa que o resultado é determinístico e 1 significa que o resultado é aleatório. O valor padrão é 0.7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt: "Coelho a cavalo, segurando um chupa-chupa, num prado enevoado onde crescem narcisos"

![Coelho a cavalo segurando um chupa-chupa, versão 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.pt.png)

Agora vamos executar o mesmo prompt novamente para ver que não obtemos a mesma imagem duas vezes:

![Imagem gerada de coelho a cavalo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.pt.png)

Como pode ver, as imagens são semelhantes, mas não idênticas. Vamos tentar alterar o valor da temperatura para 0.1 e ver o que acontece:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Alterar a temperatura

Vamos tentar tornar a resposta mais determinística. Podemos observar nas duas imagens que gerámos que na primeira imagem há um coelho e na segunda imagem há um cavalo, então as imagens variam bastante.

Vamos, portanto, alterar o nosso código e definir a temperatura para 0, como segue:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora, ao executar este código, obtém estas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.pt.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.pt.png)

Aqui pode ver claramente como as imagens se assemelham mais.

## Como definir limites para a sua aplicação com metaprompts

Com o nosso exemplo, já conseguimos gerar imagens para os nossos clientes. No entanto, precisamos de criar alguns limites para a nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam apropriadas para o trabalho ou que não sejam adequadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts textuais usados para controlar o resultado de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar o resultado e garantir que as imagens geradas sejam apropriadas para o trabalho ou adequadas para crianças.

### Como funciona?

Então, como funcionam os metaprompts?

Metaprompts são prompts textuais usados para controlar o resultado de um modelo de IA Generativa. Eles são posicionados antes do prompt textual e são usados para controlar o resultado do modelo, sendo incorporados em aplicações para controlar o resultado do modelo. Encapsulam o input do prompt e o input do metaprompt num único prompt textual.

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

Agora, vamos ver como podemos usar metaprompts no nosso exemplo.

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

A partir do prompt acima, pode ver como todas as imagens criadas consideram o metaprompt.

## Tarefa - vamos capacitar os alunos

Introduzimos a Edu4All no início desta lição. Agora é hora de capacitar os alunos para gerar imagens para os seus trabalhos.

Os alunos irão criar imagens para os seus trabalhos contendo monumentos, sendo que os monumentos específicos ficam ao critério dos alunos. Os alunos são incentivados a usar a sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

## Solução

Aqui está uma possível solução:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Excelente Trabalho! Continue a Aprender

Depois de concluir esta lição, explore a nossa [coleção de aprendizagem sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprofundar os seus conhecimentos sobre IA generativa!

Avance para a Lição 10, onde iremos explorar como [criar aplicações de IA com low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.