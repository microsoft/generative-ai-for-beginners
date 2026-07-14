# Construir Aplicações de Geração de Imagens

[![Construir Aplicações de Geração de Imagens](../../../translated_images/pt-PT/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Os LLMs não se resumem à geração de texto. Também é possível gerar imagens a partir de descrições textuais. Ter imagens como uma modalidade pode ser bastante útil em várias áreas, desde MedTech, arquitetura, turismo, desenvolvimento de jogos e muito mais. Neste capítulo, iremos analisar os dois modelos de geração de imagens mais populares, DALL-E e Midjourney.

## Introdução

Nesta lição, iremos abordar:

- Geração de imagens e porque é útil.
- DALL-E e Midjourney, o que são e como funcionam.
- Como construir uma aplicação de geração de imagens.

## Objetivos de Aprendizagem

Após concluir esta lição, será capaz de:

- Construir uma aplicação de geração de imagens.
- Definir limites para a sua aplicação com metaprompts.
- Trabalhar com DALL-E e Midjourney.

## Porquê construir uma aplicação de geração de imagens?

As aplicações de geração de imagens são uma ótima forma de explorar as capacidades da IA Generativa. Podem ser usadas, por exemplo, para:

- **Edição e síntese de imagens**. Pode gerar imagens para vários casos de uso, como edição e síntese de imagens.

- **Aplicadas a diversas indústrias**. Podem também ser usadas para gerar imagens para várias indústrias como Medtech, Turismo, Desenvolvimento de jogos e outras.

## Cenário: Edu4All

Como parte desta lição, continuaremos a trabalhar com a nossa startup, Edu4All. Os alunos irão criar imagens para as suas avaliações, que imagens exatamente depende dos alunos, mas podem ser ilustrações para o seu próprio conto de fadas, ou criar um novo personagem para a sua história ou ajudá-los a visualizar as suas ideias e conceitos.

Aqui está o que os alunos da Edu4All poderiam gerar, por exemplo, se estivessem a trabalhar em sala numa aula sobre monumentos:

![Startup Edu4All, aula sobre monumentos, Torre Eiffel](../../../translated_images/pt-PT/startup.94d6b79cc4bb3f5a.webp)

usando um prompt como

> "Cão junto à Torre Eiffel ao nascer do sol"

## O que são DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) são dois dos modelos de geração de imagens mais populares, que permitem usar prompts para gerar imagens.

### DALL-E

Comecemos pelo DALL-E, que é um modelo de IA Generativa que gera imagens a partir de descrições em texto.

> [DALL-E é uma combinação de dois modelos, CLIP e atenção difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, é um modelo que gera embeddings, que são representações numéricas de dados, a partir de imagens e texto.

- **Atenção difusa**, é um modelo que gera imagens a partir de embeddings. O DALL-E é treinado com um conjunto de dados de imagens e texto e pode ser usado para gerar imagens a partir de descrições textuais. Por exemplo, o DALL-E pode ser usado para gerar imagens de um gato com um chapéu, ou um cão com um moicano.

### Midjourney

O Midjourney funciona de forma semelhante ao DALL-E, gera imagens a partir de prompts textuais. O Midjourney pode também ser usado para gerar imagens usando prompts como “um gato com chapéu”, ou um “cão com moicano”.

![Imagem gerada por Midjourney, pombo mecânico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito da imagem Wikipedia, imagem gerada por Midjourney_

## Como funcionam o DALL-E e o Midjourney

Primeiro, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). O DALL-E é um modelo de IA Generativa baseado na arquitetura transformer com um _transformer autoregressivo_.

Um _transformer autoregressivo_ define como um modelo gera imagens a partir de descrições textuais, gera um pixel de cada vez, e depois usa os pixels gerados para gerar o próximo pixel. Passando por várias camadas numa rede neural, até a imagem estar completa.

Com este processo, o DALL-E controla atributos, objetos, características e muito mais na imagem que gera. No entanto, o DALL-E 2 e 3 têm maior controlo sobre a imagem gerada.

## Construir a sua primeira aplicação de geração de imagens

Então, o que é necessário para construir uma aplicação de geração de imagens? Precisa das seguintes bibliotecas:

- **python-dotenv**, é altamente recomendável usar esta biblioteca para manter os seus segredos num ficheiro _.env_ separado do código.
- **openai**, esta biblioteca é usada para interagir com a API OpenAI.
- **pillow**, para trabalhar com imagens em Python.
- **requests**, para ajudar a fazer pedidos HTTP.

## Criar e implantar um modelo Azure OpenAI

Se ainda não o fez, siga as instruções na página [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
para criar um recurso Azure OpenAI e modelo. Selecione **gpt-image-1** como modelo (o modelo de geração de imagem Azure OpenAI da geração atual; DALL-E 3 é legado e já não está disponível para novas implementações).

## Criar a aplicação

1. Crie um ficheiro _.env_ com o seguinte conteúdo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Localize esta informação no Portal Azure OpenAI Foundry para o seu recurso na secção "Deployments".

1. Reúna as bibliotecas acima num ficheiro chamado _requirements.txt_ assim:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. De seguida, crie um ambiente virtual e instale as bibliotecas:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para Windows, use os seguintes comandos para criar e ativar o ambiente virtual:

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
    
    # Configurar o cliente do serviço Azure OpenAI
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

        # Inicializar o caminho da imagem (note que o tipo de ficheiro deve ser png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Recuperar a imagem gerada
        image_url = generation_response.data[0].url  # extrair a URL da imagem da resposta
        generated_image = requests.get(image_url).content  # descarregar a imagem
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Mostrar a imagem no visualizador de imagens padrão
        image = Image.open(image_path)
        image.show()

    # capturar exceções
    except openai.BadRequestError as err:
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

- De seguida, carregamos as variáveis de ambiente do ficheiro _.env_.

  ```python
  # importar dotenv
  dotenv.load_dotenv()
  ```

- Depois disso, configuramos o cliente do serviço Azure OpenAI 

  ```python
  # Obter endpoint e chave a partir das variáveis de ambiente
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

  O código acima responde com um objeto JSON que contém a URL da imagem gerada. Podemos usar a URL para fazer o download da imagem e guardá-la num ficheiro.

- Por fim, abrimos a imagem e usamos o visualizador de imagens padrão para a exibir:

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

- **prompt**, é o prompt textual usado para gerar a imagem. Neste caso, estamos a usar o prompt "Coelho num cavalo, segurando um chupeta, num prado enevoado onde crescem narcisos".
- **size**, é o tamanho da imagem que é gerada. Neste caso, estamos a gerar uma imagem de 1024x1024 pixels.
- **n**, é o número de imagens que são geradas. Neste caso, geramos duas imagens.
- **temperature**, é um parâmetro que controla a aleatoriedade do output de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1 onde 0 significa que o output é determinístico e 1 significa que o output é aleatório. O valor padrão é 0,7.

Existem mais coisas que pode fazer com imagens que iremos cobrir na próxima secção.

## Capacidades adicionais da geração de imagens

Viu até agora como conseguimos gerar uma imagem usando poucas linhas em Python. Contudo, há mais coisas que pode fazer com imagens.

Pode também fazer o seguinte:

- **Realizar edições**. Fornecendo uma imagem existente, uma máscara e um prompt, pode alterar uma imagem. Por exemplo, pode adicionar algo a uma parte da imagem. Imagine a nossa imagem do coelho, pode adicionar-lhe um chapéu. Como faria isso é ao fornecer a imagem, uma máscara (identificando a parte da área para a mudança) e um prompt textual que indica o que deve ser feito. 
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

  A imagem base conteria apenas o lounge com piscina mas a imagem final teria um flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/pt-PT/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pt-PT/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pt-PT/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Criar variações**. A ideia é que pegue numa imagem existente e peça que sejam criadas variações. Para criar uma variação, fornece uma imagem e um prompt textual e código assim:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Nota, isto só é suportado no modelo DALL-E 2 da OpenAI, não em gpt-image-1

## Temperatura

Temperatura é um parâmetro que controla a aleatoriedade do output de um modelo de IA Generativa. A temperatura é um valor entre 0 e 1 onde 0 significa que o output é determinístico e 1 significa que o output é aleatório. O valor padrão é 0,7.

Vamos ver um exemplo de como a temperatura funciona, executando este prompt duas vezes:

> Prompt : "Coelho num cavalo, segurando um chupeta, num prado enevoado onde crescem narcisos"

![Coelho num cavalo segurando um chupeta, versão 1](../../../translated_images/pt-PT/v1-generated-image.a295cfcffa3c13c2.webp)

Agora vamos executar o mesmo prompt só para verificar que não vamos obter a mesma imagem duas vezes:

![Imagem gerada de coelho em cavalo](../../../translated_images/pt-PT/v2-generated-image.33f55a3714efe61d.webp)

Como pode ver, as imagens são parecidas, mas não iguais. Vamos tentar alterar o valor da temperatura para 0,1 e ver o que acontece:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Insira o texto do seu pedido aqui
        size='1024x1024',
        n=2
    )
```

### Alterar a temperatura

Então, vamos tentar tornar a resposta mais determinística. Podemos observar pelas duas imagens que gerámos que na primeira imagem há um coelho e na segunda um cavalo, portanto as imagens variam bastante.

Vamos então alterar o nosso código e definir a temperatura para 0, assim:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Introduza o texto do seu pedido aqui
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Agora quando executa este código, obtém estas duas imagens:

- ![Temperatura 0, v1](../../../translated_images/pt-PT/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatura 0 , v2](../../../translated_images/pt-PT/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Aqui pode ver claramente como as imagens se assemelham mais.

## Como definir limites para a sua aplicação com metaprompts

Com a nossa demo, já podemos gerar imagens para os nossos clientes. No entanto, precisamos criar alguns limites para a nossa aplicação.

Por exemplo, não queremos gerar imagens que não sejam seguras para trabalho, ou que não sejam apropriadas para crianças.

Podemos fazer isto com _metaprompts_. Metaprompts são prompts textuais usados para controlar o output de um modelo de IA Generativa. Por exemplo, podemos usar metaprompts para controlar o output e garantir que as imagens geradas são seguras para trabalho, ou apropriadas para crianças.

### Como funciona?

Agora, como funcionam os metaprompts?

Metaprompts são prompts textuais usados para controlar o output de um modelo de IA Generativa, são posicionados antes do prompt textual, e são usados para controlar o output do modelo e incorporados em aplicações para controlar o output do modelo. Envolvendo o prompt de entrada e o prompt meta numa única entrada textual.

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

Agora, vejamos como podemos usar metaprompts na nossa demo.

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

# TODO adicionar pedido para gerar imagem
```

A partir do prompt acima, pode ver como todas as imagens geradas consideram o metaprompt.

## Tarefa - vamos capacitar os estudantes

Introduzimos a Edu4All no início desta lição. Agora é tempo de permitir aos alunos gerar imagens para as suas avaliações.


Os alunos vão criar imagens para as suas avaliações contendo monumentos, exatamente quais monumentos ficam a critério dos alunos. Os alunos são convidados a usar a sua criatividade nesta tarefa para colocar estes monumentos em diferentes contextos.

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

# Obter endpoint e chave das variáveis de ambiente
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
    # Criar uma imagem usando a API de geração de imagens
    generation_response = client.images.generate(
        prompt=prompt,    # Insira o seu texto de prompt aqui
        size='1024x1024',
        n=1,
    )
    # Definir o diretório para a imagem guardada
    image_dir = os.path.join(os.curdir, 'images')

    # Se o diretório não existir, criá-lo
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Inicializar o caminho da imagem (note que o tipo de ficheiro deve ser png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Recuperar a imagem gerada
    image_url = generation_response.data[0].url  # extrair URL da imagem da resposta
    generated_image = requests.get(image_url).content  # transferir a imagem
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Mostrar a imagem no visualizador de imagens predefinido
    image = Image.open(image_path)
    image.show()

# capturar exceções
except openai.BadRequestError as err:
    print(err)
```

## Excelente trabalho! Continue a sua aprendizagem

Depois de completar esta lição, confira a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprofundar o seu conhecimento em IA Generativa!

Dirija-se à Lição 10 onde iremos ver como [construir aplicações de IA com low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->