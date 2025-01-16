# 画像生成アプリケーションの構築

[![画像生成アプリケーションの構築](../../../translated_images/09-lesson-banner.png?WT.d9f0561bfac2f22fe149efecb3524eaf381a4aa260ba334f49b1fd215bd59d75.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMにはテキスト生成以外にも多くの可能性があります。テキストの説明から画像を生成することも可能です。画像をモダリティとして使用することは、MedTech、建築、観光、ゲーム開発など、さまざまな分野で非常に役立ちます。この章では、最も人気のある画像生成モデルであるDALL-EとMidjourneyについて見ていきます。

## はじめに

このレッスンでは以下を学びます：

- 画像生成とその有用性について。
- DALL-EとMidjourney、それが何であるか、どのように機能するか。
- 画像生成アプリをどのように構築するか。

## 学習目標

このレッスンを完了すると、以下ができるようになります：

- 画像生成アプリケーションを構築する。
- メタプロンプトでアプリケーションの境界を定義する。
- DALL-EとMidjourneyを使いこなす。

## なぜ画像生成アプリケーションを構築するのか？

画像生成アプリケーションは、生成AIの能力を探求する素晴らしい方法です。例えば、以下のような用途に利用できます：

- **画像編集と合成**。画像編集や画像合成など、さまざまなユースケースに画像を生成できます。

- **さまざまな業界に適用可能**。MedTech、観光、ゲーム開発など、さまざまな業界で画像を生成するために使用できます。

## シナリオ: Edu4All

このレッスンの一環として、私たちのスタートアップEdu4Allと一緒に作業を続けます。学生たちは評価のための画像を作成します。どんな画像を作成するかは学生次第ですが、自分の童話のイラストを作成したり、新しいキャラクターを作成したり、自分のアイデアや概念を視覚化するのに役立てることができます。

例えば、Edu4Allの学生がクラスでモニュメントについて学んでいる場合、次のような画像を生成できます：

![Edu4Allスタートアップ、モニュメントのクラス、エッフェル塔](../../../translated_images/startup.png?WT.da6453984b26f46f3e26925e20877c740be4f328afdfce9fe36b23e7b434c7b5.ja.mc_id=academic-105485-koreyst)

次のようなプロンプトを使用して

> "早朝の陽光の中でエッフェル塔の隣にいる犬"

## DALL-EとMidjourneyとは？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)と[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)は、最も人気のある画像生成モデルの2つで、プロンプトを使用して画像を生成できます。

### DALL-E

まずDALL-Eから始めましょう。これはテキストの説明から画像を生成する生成AIモデルです。

> [DALL-Eは、CLIPと拡散注意の2つのモデルの組み合わせです](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**は、画像やテキストからデータの数値表現である埋め込みを生成するモデルです。

- **拡散注意**は、埋め込みから画像を生成するモデルです。DALL-Eは画像とテキストのデータセットでトレーニングされており、テキストの説明から画像を生成するために使用できます。例えば、DALL-Eを使用して帽子をかぶった猫やモヒカンの犬の画像を生成することができます。

### Midjourney

MidjourneyもDALL-Eと同様に、テキストプロンプトから画像を生成します。Midjourneyを使用して、「帽子をかぶった猫」や「モヒカンの犬」などのプロンプトで画像を生成することができます。

![Midjourneyによって生成された画像、メカニカルハト](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_画像クレジット: Wikipedia、Midjourneyによって生成された画像_

## DALL-EとMidjourneyはどのように機能するのか

まず、[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)です。DALL-Eはトランスフォーマーアーキテクチャに基づいた生成AIモデルで、_自己回帰トランスフォーマー_を使用しています。

_自己回帰トランスフォーマー_は、テキストの説明から画像を生成する方法を定義します。1ピクセルずつ生成し、生成されたピクセルを使用して次のピクセルを生成します。ニューラルネットワークの複数の層を通過し、画像が完成します。

このプロセスを通じて、DALL-Eは生成された画像内の属性、オブジェクト、特徴などを制御します。しかし、DALL-E 2と3は生成された画像に対してより多くの制御を持っています。

## 初めての画像生成アプリケーションを構築する

では、画像生成アプリケーションを構築するには何が必要でしょうか？以下のライブラリが必要です：

- **python-dotenv**、このライブラリを使用して、秘密情報をコードから離れた_.env_ファイルに保持することを強くお勧めします。
- **openai**、このライブラリはOpenAI APIと対話するために使用します。
- **pillow**、Pythonで画像を操作するために使用します。
- **requests**、HTTPリクエストを行うのを助けます。

1. 以下の内容で_.env_ファイルを作成します：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portalでリソースの「Keys and Endpoint」セクションからこの情報を見つけます。

1. 上記のライブラリを_requirements.txt_というファイルに以下のように集めます：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 次に、仮想環境を作成し、ライブラリをインストールします：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windowsの場合、仮想環境を作成し、アクティブ化するために以下のコマンドを使用します：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_というファイルに以下のコードを追加します：

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

このコードを説明します：

- まず、必要なライブラリをインポートします。OpenAIライブラリ、dotenvライブラリ、requestsライブラリ、Pillowライブラリを含みます。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 次に、_.env_ファイルから環境変数をロードします。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- その後、OpenAI APIのエンドポイント、キー、バージョン、タイプを設定します。

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- 次に、画像を生成します：

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  上記のコードは、生成された画像のURLを含むJSONオブジェクトを返します。このURLを使用して画像をダウンロードし、ファイルに保存できます。

- 最後に、画像を開き、標準の画像ビューアで表示します：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 画像生成の詳細

画像を生成するコードを詳しく見てみましょう：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**は、画像を生成するために使用されるテキストプロンプトです。この場合、"Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"というプロンプトを使用しています。
- **size**は、生成される画像のサイズです。この場合、1024x1024ピクセルの画像を生成しています。
- **n**は、生成される画像の数です。この場合、2つの画像を生成しています。
- **temperature**は、生成AIモデルの出力のランダム性を制御するパラメータです。温度は0から1の間の値で、0は出力が決定的であり、1は出力がランダムであることを意味します。デフォルト値は0.7です。

次のセクションでは、画像に関してできることをさらにカバーします。

## 画像生成の追加機能

これまでに、Pythonの数行で画像を生成できることを見てきました。しかし、画像に関してできることはもっとあります。

以下のこともできます：

- **編集を行う**。既存の画像にマスクとプロンプトを提供することで、画像を変更できます。例えば、画像の一部に何かを追加できます。私たちのバニー画像を想像してみてください。バニーに帽子を追加できます。これを行う方法は、画像、マスク（変更のための領域を識別するもの）、そして何を行うべきかを示すテキストプロンプトを提供することです。

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

  基本画像にはうさぎだけが含まれますが、最終画像にはうさぎに帽子が追加されます。

- **バリエーションを作成する**。既存の画像を取り、バリエーションを作成することを依頼します。バリエーションを作成するには、画像とテキストプロンプトを提供し、次のようにコードを書きます：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注記、これはOpenAIでのみサポートされています

## 温度

温度は、生成AIモデルの出力のランダム性を制御するパラメータです。温度は0から1の間の値で、0は出力が決定的であり、1は出力がランダムであることを意味します。デフォルト値は0.7です。

温度がどのように機能するかを例で見てみましょう。このプロンプトを2回実行してみます：

> プロンプト : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.png?WT.e88fb2d10c6d1ae1c198e2959629a4737a139b457fed4b2f325b2ea8d2c7bca6.ja.mc_id=academic-105485-koreyst)

同じプロンプトをもう一度実行して、同じ画像が2回生成されないことを確認してみましょう：

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.png?WT.10df7dd739ff1f669b915523632a51ade0346b30603d8bf996872ac629f3dcd7.ja.mc_id=academic-105485-koreyst)

ご覧のとおり、画像は似ていますが、同じではありません。温度値を0.1に変更してみましょう：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 温度の変更

応答をより決定的にするために試してみましょう。生成された2つの画像から、最初の画像にはうさぎがいて、2番目の画像には馬がいることが観察できるので、画像は大きく異なります。

したがって、コードを変更し、温度を0に設定してみましょう：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

このコードを実行すると、次の2つの画像が得られます：

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.png?WT.27c4ce8ff113ce11a5a45b5c74e319c5115b0b832a3697bc91fc653d0a5f7609.ja.mc_id=academic-105485-koreyst)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.png?WT.04d52c2aa6ef41f4d67040329ca204ef927512f46bb9dfef035e02098f45d0f7.ja.mc_id=academic-105485-koreyst)

ここで、画像がより似ていることが明らかにわかります。

## メタプロンプトでアプリケーションの境界を定義する方法

デモを使って、すでにクライアントのために画像を生成できます。しかし、アプリケーションのためにいくつかの境界を作成する必要があります。

たとえば、仕事に不適切な画像や、子供に適さない画像を生成したくありません。

これを_metaprompts_で行うことができます。メタプロンプトは、生成AIモデルの出力を制御するために使用されるテキストプロンプトです。たとえば、メタプロンプトを使用して、生成された画像が仕事に適しているか、子供に適していることを確認できます。

### それはどのように機能するのか？

では、メタプロンプトはどのように機能するのでしょうか？

メタプロンプトは、生成AIモデルの出力を制御するために使用されるテキストプロンプトであり、テキストプロンプトの前に配置され、モデルの出力を制御するために使用され、アプリケーションに埋め込まれてモデルの出力を制御します。プロンプト入力とメタプロンプト入力を単一のテキストプロンプトにカプセル化します。

メタプロンプトの一例は次のようになります：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

では、デモでメタプロンプトをどのように使用できるかを見てみましょう。

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

上記のプロンプトから、すべての生成される画像がメタプロンプトを考慮していることがわかります。

## 課題 - 学生を支援しよう

このレッスンの最初にEdu4Allを紹介しました。今度は、学生が評価のために画像を生成できるようにしましょう。

学生たちは、モニュメントを含む評価のための画像を作成します。どのモニュメントを選ぶかは学生次第です。学生はこのタスクで創造性を発揮し、これらのモニュメントを異なる文脈で配置するよう求められています。

## 解決策

以下は一つの解決策です：

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

## 素晴らしい仕事！学習を続けましょう

このレッスンを完了した後は、[Generative AI Learningコレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、Generative AIの知識をさらに深めてください！

レッスン10に進み、[ローコードでAIアプリケーションを構築する方法](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)を見てみましょう。

**免責事項**:  
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。元の言語で書かれた原文が権威ある情報源と見なされるべきです。重要な情報については、プロの人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。