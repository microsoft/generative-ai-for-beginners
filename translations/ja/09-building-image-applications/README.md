<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:09:53+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ja"
}
-->
# 画像生成アプリケーションの構築

LLMsにはテキスト生成以上の機能があります。テキストの説明から画像を生成することも可能です。画像をモダリティとして持つことは、MedTech、建築、観光、ゲーム開発など多くの分野で非常に有用です。この章では、最も人気のある画像生成モデルであるDALL-EとMidjourneyについて見ていきます。

## はじめに

このレッスンでは以下をカバーします：

- 画像生成とその有用性
- DALL-EとMidjourney、それらが何であるか、そしてどのように動作するか
- 画像生成アプリの構築方法

## 学習目標

このレッスンを完了した後、あなたは以下のことができるようになります：

- 画像生成アプリケーションを構築する
- メタプロンプトを使用してアプリケーションの境界を定義する
- DALL-EとMidjourneyを使用する

## なぜ画像生成アプリケーションを構築するのか？

画像生成アプリケーションは、生成AIの能力を探求する素晴らしい方法です。例えば、以下のような用途で使用できます：

- **画像編集と合成**。画像編集や画像合成など、さまざまな用途のために画像を生成できます。

- **さまざまな業界に応用**。Medtech、観光、ゲーム開発など、さまざまな業界のために画像を生成するためにも使用できます。

## シナリオ: Edu4All

このレッスンの一環として、スタートアップEdu4Allと共に作業を続けます。学生は評価のために画像を作成します。どのような画像を作成するかは学生次第ですが、彼ら自身の童話のためのイラストを作成したり、ストーリーの新しいキャラクターを作成したり、アイデアや概念を視覚化するのを助けることができます。

例えば、クラスでモニュメントについて学んでいる場合、Edu4Allの学生が生成できるものは次の通りです：

> "早朝の陽光の中、エッフェル塔の隣にいる犬"

## DALL-EとMidjourneyとは？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)と[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)は、最も人気のある画像生成モデルの一つで、プロンプトを使用して画像を生成することができます。

### DALL-E

まずはDALL-Eから始めましょう。これはテキストの説明から画像を生成する生成AIモデルです。

- **CLIP**は、画像とテキストからデータの数値表現である埋め込みを生成するモデルです。

- **拡散注意**は、埋め込みから画像を生成するモデルです。DALL-Eは画像とテキストのデータセットで訓練されており、テキストの説明から画像を生成するために使用できます。例えば、DALL-Eは帽子をかぶった猫やモヒカンの犬の画像を生成することができます。

### Midjourney

MidjourneyはDALL-Eと似た方法で動作し、テキストプロンプトから画像を生成します。Midjourneyもまた、「帽子をかぶった猫」や「モヒカンの犬」のようなプロンプトを使用して画像を生成することができます。

## DALL-EとMidjourneyの動作原理

まず、[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)です。DALL-Eは、トランスフォーマーアーキテクチャに基づく生成AIモデルで、_自己回帰トランスフォーマー_を備えています。

_自己回帰トランスフォーマー_は、テキストの説明から画像を生成する方法を定義し、1ピクセルずつ生成し、生成されたピクセルを使用して次のピクセルを生成します。ニューラルネットワークの複数の層を通過し、画像が完成するまで続けます。

このプロセスにより、DALL-Eは生成する画像の属性、オブジェクト、特性などを制御します。ただし、DALL-E 2と3は生成された画像をより詳細に制御できます。

## 初めての画像生成アプリケーションの構築

では、画像生成アプリケーションを構築するには何が必要でしょうか？以下のライブラリが必要です：

- **python-dotenv**、コードから離れた_.env_ファイルに秘密を保存するためにこのライブラリを使用することを強くお勧めします。
- **openai**、OpenAI APIと対話するために使用するライブラリです。
- **pillow**、Pythonで画像を扱うためのライブラリです。
- **requests**、HTTPリクエストを行うのに役立つライブラリです。

1. 以下の内容で_.env_ファイルを作成します：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   この情報はAzure Portalの「Keys and Endpoint」セクションでリソースに対して見つけることができます。

1. 上記のライブラリを_requirements.txt_というファイルに収集します：

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

   Windowsの場合、以下のコマンドを使用して仮想環境を作成し、アクティブ化します：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_というファイルに次のコードを追加します：

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

このコードを説明しましょう：

- まず、必要なライブラリをインポートします。OpenAIライブラリ、dotenvライブラリ、requestsライブラリ、Pillowライブラリなどです。

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

  上記のコードは、生成された画像のURLを含むJSONオブジェクトを返します。URLを使用して画像をダウンロードし、ファイルに保存することができます。

- 最後に、画像を開いて標準の画像ビューアーで表示します：

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

- **prompt**は、画像生成に使用されるテキストプロンプトです。この場合、「霧の立ち込める草原でロリポップを持っている馬に乗ったウサギ」というプロンプトを使用しています。
- **size**は生成される画像のサイズです。この場合、1024x1024ピクセルの画像を生成しています。
- **n**は生成される画像の数です。この場合、2枚の画像を生成しています。
- **temperature**は生成AIモデルの出力のランダム性を制御するパラメータです。温度は0から1の間の値で、0は出力が決定的であることを意味し、1は出力がランダムであることを意味します。デフォルト値は0.7です。

次のセクションでは、画像でできることがさらにあります。

## 画像生成の追加機能

これまでにPythonで数行のコードを使用して画像を生成する方法を見てきました。しかし、画像でできることはさらにあります。

以下のこともできます：

- **編集を行う**。既存の画像にマスクとプロンプトを提供することで画像を変更することができます。例えば、画像の一部に何かを追加することができます。ウサギの画像を想像してみてください。ウサギに帽子を追加することができます。それを行う方法は、画像、変更の対象となる領域を特定するマスク、そして何を行うべきかを示すテキストプロンプトを提供することです。

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

  ベース画像にはウサギのみが含まれますが、最終画像にはウサギに帽子がかぶせられています。

- **バリエーションを作成する**。既存の画像を取り、バリエーションを作成するように要求します。バリエーションを作成するには、画像とテキストプロンプトを提供し、次のようにコードを書きます：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意、これはOpenAIでのみサポートされています

## 温度

温度は生成AIモデルの出力のランダム性を制御するパラメータです。温度は0から1の間の値で、0は出力が決定的であることを意味し、1は出力がランダムであることを意味します。デフォルト値は0.7です。

温度がどのように機能するかの例を見てみましょう。このプロンプトを2回実行してみます：

> プロンプト : "霧の立ち込める草原でロリポップを持っている馬に乗ったウサギ"

同じプロンプトを実行しても同じ画像が2回生成されないことを確認してみましょう：

画像は似ていますが、同じではありません。温度の値を0.1に変更して何が起こるか見てみましょう：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 温度の変更

応答をより決定的にするために試してみましょう。生成した2枚の画像から、最初の画像にはウサギがいて、2枚目の画像には馬がいることが観察できるので、画像は大きく異なります。

そこで、コードを変更して温度を0に設定しましょう：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

このコードを実行すると、次の2枚の画像が生成されます：

ここでは、画像がより似ていることがはっきりとわかります。

## メタプロンプトでアプリケーションの境界を定義する方法

デモでは、すでにクライアントのために画像を生成できます。しかし、アプリケーションにいくつかの境界を作成する必要があります。

例えば、職場で安全でない画像や子供に不適切な画像を生成したくありません。

これをメタプロンプトで行うことができます。メタプロンプトは、生成AIモデルの出力を制御するために使用されるテキストプロンプトです。例えば、メタプロンプトを使用して出力を制御し、生成された画像が職場で安全であることや子供に適していることを保証することができます。

### どのように機能するのか？

では、メタプロンプトはどのように機能するのでしょうか？

メタプロンプトは生成AIモデルの出力を制御するために使用されるテキストプロンプトであり、テキストプロンプトの前に配置され、モデルの出力を制御するために使用されます。アプリケーションに埋め込まれ、モデルの出力を制御します。プロンプト入力とメタプロンプト入力を1つのテキストプロンプトにカプセル化します。

メタプロンプトの例として以下のものがあります：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

では、デモでメタプロンプトをどのように使用するか見てみましょう。

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

このレッスンの冒頭でEdu4Allを紹介しました。今度は、学生が評価のために画像を生成できるようにしましょう。

学生は評価のためにモニュメントを含む画像を作成します。どのモニュメントを作成するかは学生次第です。学生はこのタスクで創造性を発揮し、これらのモニュメントをさまざまな文脈で配置することを求められています。

## 解決策

ここに一つの可能な解決策があります：

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

## 素晴らしい！学習を続けましょう

このレッスンを完了した後は、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに向上させてください！

次のレッスン10では、[ローコードでAIアプリケーションを構築する方法](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)について見ていきます。

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の言語での文書が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。