# Construindo Aplicações de Geração de Imagens

[![Construindo Aplicações de Geração de Imagens](../../../translated_images/pt-BR/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Há mais nos LLMs do que geração de texto. Também é possível gerar imagens a partir de descrições de texto. Ter imagens como uma modalidade pode ser muito útil em várias áreas, desde MedTech, arquitetura, turismo, desenvolvimento de jogos e mais. Neste capítulo, vamos explorar os dois modelos de geração de imagem mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, vamos cobrir:

- Geração de imagem e por que isso é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como construir uma aplicação de geração de imagem.

## Objetivos de Aprendizado

Após completar esta lição, você será capaz de:

- Construir uma aplicação de geração de imagem.
- Definir limites para sua aplicação com metaprompts.
- Trabalhar com DALL-E e Midjourney.

## Por que construir uma aplicação de geração de imagem?

Aplicações de geração de imagem são uma ótima forma de explorar as capacidades da IA Generativa. Elas podem ser usadas, por exemplo, para:

- **Edição e síntese de imagens**. Você pode gerar imagens para diversos casos de uso, como edição de imagem e síntese de imagem.

- **Aplicadas a diversas indústrias**. Também podem ser usadas para gerar imagens para vários setores, como Medtech, Turismo, Desenvolvimento de jogos e mais.

## Cenário: Edu4All

Como parte desta lição, continuaremos trabalhando com nossa startup, Edu4All. Os alunos criarão imagens para suas avaliações, exatamente quais imagens fica a critério dos alunos, mas elas podem ser ilustrações para seu próprio conto de fadas, ou criar um novo personagem para sua história ou ajudá-los a visualizar suas ideias e conceitos.

Veja o que os alunos da Edu4All poderiam gerar, por exemplo, se estiverem trabalhando em classe com monumentos:

![Edu4All startup, aula sobre monumentos, Torre Eiffel](../../../translated_images/pt-BR/startup.94d6b79cc4bb3f5a.webp)

usando um prompt como

> "Cachorro ao lado da Torre Eiffel na luz da manhã cedo"

## O que é DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos mais populares de geração de imagem, eles permitem o uso de prompts para gerar imagens.

### DALL-E

Vamos começar com DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições de texto.

> [DALL-E é uma combinação de dois modelos, CLIP e atenção difundida](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, é um modelo que gera embeddings, que são representações numéricas dos dados, a partir de imagens e texto.

- **Atenção difundida**, é um modelo que gera imagens a partir de embeddings. DALL-E é treinado em um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, DALL-E pode ser usado para gerar imagens de um gato com chapéu, ou um cachorro com moicano.

### Midjourney

Midjourney funciona de forma semelhante ao DALL-E, gera imagens a partir de prompts de texto. Midjourney também pode ser usado para gerar imagens usando prompts como “um gato com chapéu”, ou um “cachorro com moicano”.

![Imagem gerada pelo Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem Wikipedia, imagem gerada pelo Midjourney_

## Como DALL-E e Midjourney Funcionam

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autorregressivo_.

Um _transformer autorregressivo_ define como um modelo gera imagens a partir de descrições de texto, ele gera um pixel de cada vez, e então usa os pixels gerados para gerar o próximo pixel. Passando por várias camadas em uma rede neural, até que a imagem esteja completa.

Com esse processo, o DALL-E controla atributos, objetos, características e mais na imagem que gera. Porém, DALL-E 2 e 3 têm mais controle sobre a imagem gerada.

## Construindo sua primeira aplicação de geração de imagem

O que é necessário para construir uma aplicação de geração de imagens? Você precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendado usar essa biblioteca para manter seus segredos em um arquivo _.env_ separado do código.
- **openai**, essa biblioteca é o que você usará para interagir com a API da OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudar a fazer requisições HTTP.

## Criar e implantar um modelo Azure OpenAI

Se ainda não fez, siga as instruções na página [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
para criar um recurso e modelo Azure OpenAI. Selecione **gpt-image-1** como modelo (o modelo atual de geração de imagem Azure OpenAI; DALL-E 3 é legado e não está mais disponível para novas implantações).

## Criar o aplicativo

1. Crie um arquivo _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Localize essas informações no portal Azure OpenAI Foundry para seu recurso na seção "Implantações".

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

   Para Windows, use os comandos a seguir para criar e ativar o seu ambiente virtual:

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configurar cliente do serviço Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Criar uma imagem usando a API de geração de imagens
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Definir o diretório para a imagem armazenada
        image_dir = os.path.join(os.curdir, 'images')

        # Se o diretório não existir, criá-lo
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Inicializar o caminho da imagem (note que o tipo de arquivo deve ser png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Recuperar a imagem gerada
        image_url = generation_response.data[0].url  # extrair URL da imagem da resposta
        generated_image = requests.get(image_url).content  # baixar a imagem
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Exibir a imagem no visualizador de imagens padrão
        image = Image.open(image_path)
        image.show()

    # capturar exceções
    except openai.BadRequestError as err:
        print(err)
   ```

Vamos explicar este código:

- Primeiro, importamos as bibliotecas que precisamos, incluindo a biblioteca OpenAI, a biblioteca dotenv, a biblioteca requests, e a biblioteca Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Em seguida, carregamos as variáveis de ambiente do arquivo _.env_.

  ```python
  # importar dotenv
  dotenv.load_dotenv()
  ```

- Depois disso, configuramos o cliente do serviço Azure OpenAI 

  ```python
  # Obtenha o endpoint e a chave das variáveis de ambiente
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- A seguir, geramos a imagem:

  ```python
  # Crie uma imagem usando a API de geração de imagens
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  O código acima responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar a URL para baixar a imagem e salvar em um arquivo.

- Por fim, abrimos a imagem e usamos o visualizador padrão para exibi-la:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mais detalhes sobre a geração da imagem

Vamos examinar o código que gera a imagem com mais detalhes:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, é o texto do prompt usado para gerar a imagem. Neste caso, estamos usando o prompt "Coelho em cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos".
- **size**, é o tamanho da imagem que é gerada. Neste caso, estamos gerando uma imagem de 1024x1024 pixels.
- **n**, é o número de imagens que são geradas. Neste caso, estamos gerando duas imagens.
- **temperature**, é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1 onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Existem mais coisas que você pode fazer com imagens que abordaremos na próxima seção.

## Capacidades adicionais de geração de imagem

Você viu até agora como conseguimos gerar uma imagem usando poucas linhas em Python. Porém, existem mais coisas que você pode fazer com imagens.

Você também pode fazer o seguinte:

- **Realizar edições**. Fornecendo uma imagem existente, uma máscara e um prompt, você pode alterar uma imagem. Por exemplo, pode adicionar algo em uma parte da imagem. Imagine nossa imagem do coelho, você pode adicionar um chapéu ao coelho. Como fazer isso? Fornecendo a imagem, uma máscara (identificando a parte da área para alteração) e um prompt de texto para indicar o que deve ser feito.
> Nota: isso não é suportado no DALL-E 3. 
 
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
  <img src="../../../translated_images/pt-BR/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pt-BR/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pt-BR/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Criar variações**. A ideia é pegar uma imagem existente e pedir que variações sejam criadas. Para criar uma variação, você fornece uma imagem e um prompt de texto e código assim:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Nota: isso é suportado somente no modelo DALL-E 2 da OpenAI, não no gpt-image-1

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade da saída de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1 onde 0 significa que a saída é determinística e 1 significa que a saída é aleatória. O valor padrão é 0.7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt: "Coelho em cavalo, segurando um pirulito, em um prado enevoado onde crescem narcisos"

![Coelho em um cavalo segurando um pirulito, versão 1](../../../translated_images/pt-BR/v1-generated-image.a295cfcffa3c13c2.webp)

Agora vamos executar o mesmo prompt só para ver que não obteremos a mesma imagem duas vezes:

![Imagem gerada do coelho em cavalo](../../../translated_images/pt-BR/v2-generated-image.33f55a3714efe61d.webp)

Como pode ver, as imagens são semelhantes, mas não iguais. Vamos tentar mudar o valor da temperatura para 0.1 e ver o que acontece:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Digite seu texto de prompt aqui
        size='1024x1024',
        n=2
    )
```

### Mudando a temperatura

Então vamos tentar tornar a resposta mais determinística. Podemos observar pelas duas imagens que geramos que na primeira imagem há um coelho e na segunda imagem há um cavalo, então as imagens variam bastante.

Portanto, vamos mudar nosso código e definir a temperatura para 0, assim:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Digite seu texto de prompt aqui
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora, ao executar este código, você obtém essas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/pt-BR/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatura 0 , v2](../../../translated_images/pt-BR/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Aqui você pode claramente ver como as imagens se assemelham mais.

## Como definir limites para sua aplicação com metaprompts

Com o nosso demo, já podemos gerar imagens para nossos clientes. Contudo, precisamos criar alguns limites para nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam apropriadas para o ambiente de trabalho, ou que não sejam apropriadas para crianças.

Podemos fazer isso com _metaprompts_. Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar a saída e garantir que as imagens geradas sejam seguras para o trabalho, ou adequadas para crianças.

### Como funciona?

Agora, como funcionam os metaprompts?

Metaprompts são prompts de texto usados para controlar a saída de um modelo de IA Generativa, eles são posicionados antes do prompt de texto e usados para controlar a saída do modelo, e embutidos em aplicações para controlar a saída do modelo. Encapsulando a entrada do prompt e a entrada do metaprompt em um único prompt de texto.

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

# TODO adicionar solicitação para gerar imagem
```

Pelo prompt acima, você pode ver como todas as imagens criadas consideram o metaprompt.

## Exercício - Vamos capacitar os alunos

Apresentamos a Edu4All no início desta lição. Agora é hora de capacitar os alunos a gerar imagens para suas avaliações.


Os estudantes criarão imagens para suas avaliações contendo monumentos, exatamente quais monumentos fica a critério dos estudantes. Os estudantes são convidados a usar sua criatividade nesta tarefa para colocar esses monumentos em diferentes contextos.

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

# Obtenha o endpoint e a chave das variáveis de ambiente
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # Crie uma imagem usando a API de geração de imagens
    generation_response = client.images.generate(
        prompt=prompt,    # Insira o texto do seu prompt aqui
        size='1024x1024',
        n=1,
    )
    # Defina o diretório para a imagem armazenada
    image_dir = os.path.join(os.curdir, 'images')

    # Se o diretório não existir, crie-o
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Inicialize o caminho da imagem (observe que o tipo de arquivo deve ser png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Recupere a imagem gerada
    image_url = generation_response.data[0].url  # extraia a URL da imagem da resposta
    generated_image = requests.get(image_url).content  # faça o download da imagem
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Exiba a imagem no visualizador de imagens padrão
    image = Image.open(image_path)
    image.show()

# capture exceções
except openai.BadRequestError as err:
    print(err)
```

## Excelente Trabalho! Continue Seu Aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 10 onde vamos ver como [construir aplicações de IA com low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->