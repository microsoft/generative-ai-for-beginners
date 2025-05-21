<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:32:18+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ja"
}
-->
# 画像生成アプリケーションの構築

LLMsはテキスト生成だけではありません。テキストの説明から画像を生成することも可能です。画像をモダリティとして持つことは、MedTech、建築、観光、ゲーム開発など多くの分野で非常に有用です。この章では、最も人気のある画像生成モデルであるDALL-EとMidjourneyについて見ていきます。

## はじめに

このレッスンでは以下をカバーします：

- 画像生成とその有用性
- DALL-EとMidjourney、それらが何であり、どのように動作するか
- 画像生成アプリをどのように構築するか

## 学習目標

このレッスンを終えた後、あなたは以下ができるようになります：

- 画像生成アプリケーションを構築する
- メタプロンプトでアプリケーションの境界を定義する
- DALL-EとMidjourneyを使う

## なぜ画像生成アプリケーションを構築するのか？

画像生成アプリケーションは、生成AIの能力を探求するための素晴らしい方法です。以下のように利用できます：

- **画像編集と合成**。画像編集や画像合成など、さまざまなユースケースに対応する画像を生成できます。

- **さまざまな産業に応用可能**。Medtech、観光、ゲーム開発など、さまざまな産業向けの画像を生成することも可能です。

## シナリオ: Edu4All

このレッスンの一環として、私たちのスタートアップであるEdu4Allと一緒に作業を続けます。学生たちは自分たちの評価のために画像を作成しますが、どのような画像を作成するかは学生たちに任されています。例えば、自分の童話のイラストを作成したり、新しいキャラクターを作成したり、アイデアや概念を視覚化するのを助けたりすることができます。

例えば、クラスでモニュメントについて学んでいる場合、学生たちは次のような画像を生成できます：

> "朝の早い時間のエッフェル塔の隣にいる犬"

## DALL-EとMidjourneyとは何か？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)と[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)は、最も人気のある画像生成モデルの2つで、プロンプトを使って画像を生成することができます。

### DALL-E

まずDALL-Eについて見てみましょう。これは、テキストの説明から画像を生成する生成AIモデルです。

> [DALL-Eは、CLIPと拡散注意の2つのモデルの組み合わせです](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**は、画像とテキストからデータの数値表現である埋め込みを生成するモデルです。

- **拡散注意**は、埋め込みから画像を生成するモデルです。DALL-Eは画像とテキストのデータセットで訓練されており、テキストの説明から画像を生成することができます。例えば、DALL-Eを使って、帽子をかぶった猫やモヒカンの犬の画像を生成することができます。

### Midjourney

MidjourneyはDALL-Eと同様に、テキストプロンプトから画像を生成します。Midjourneyもまた、「帽子をかぶった猫」や「モヒカンの犬」といったプロンプトを使って画像を生成することができます。

## DALL-EとMidjourneyの動作原理

まず、[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)について。DALL-Eは、トランスフォーマーアーキテクチャに基づく生成AIモデルで、_自己回帰型トランスフォーマー_を使用しています。

自己回帰型トランスフォーマーは、モデルがテキストの説明から画像を生成する方法を定義します。一度に1ピクセルを生成し、その生成されたピクセルを使用して次のピクセルを生成します。ニューラルネットワークの複数の層を通過し、画像が完成するまでこのプロセスを繰り返します。

このプロセスを通じて、DALL-Eは生成された画像の属性、オブジェクト、特性などを制御します。しかし、DALL-E 2と3は生成された画像に対してより多くの制御を持っています。

## 最初の画像生成アプリケーションの構築

画像生成アプリケーションを構築するには何が必要ですか？以下のライブラリが必要です：

- **python-dotenv**、コードから離れた_.env_ファイルに秘密を保持するためにこのライブラリを使用することを強くお勧めします。
- **openai**、OpenAI APIと対話するために使用するライブラリです。
- **pillow**、Pythonで画像を操作するためのライブラリです。
- **requests**、HTTPリクエストを行うのに役立ちます。

1. 次の内容で_.env_ファイルを作成します：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azureポータルでリソースの「キーとエンドポイント」セクションにこの情報を見つけます。

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

このコードを説明します：

- まず、必要なライブラリをインポートします。OpenAIライブラリ、dotenvライブラリ、requestsライブラリ、Pillowライブラリです。

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

- 最後に、画像を開き、標準の画像ビューアを使用して表示します：

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

- **prompt**は、画像を生成するために使用されるテキストプロンプトです。この場合、「霧の立ち込める草原で馬に乗っているウサギがキャンディーを持っている」というプロンプトを使用しています。
- **size**は、生成される画像のサイズです。この場合、1024x1024ピクセルの画像を生成しています。
- **n**は、生成される画像の数です。この場合、2枚の画像を生成しています。
- **temperature**は、生成AIモデルの出力のランダム性を制御するパラメータです。temperatureは0から1の間の値で、0は出力が決定的であることを意味し、1は出力がランダムであることを意味します。デフォルト値は0.7です。

画像を使ってさらにできることについては、次のセクションで説明します。

## 画像生成の追加機能

これまでに、Pythonで数行のコードを使って画像を生成する方法を見てきましたが、画像でさらにできることがあります。

次のこともできます：

- **編集を行う**。既存の画像にマスクとプロンプトを提供することで、画像を変更することができます。例えば、画像の一部に何かを追加することができます。ウサギの画像を想像してみてください。ウサギに帽子を追加することができます。それを行う方法は、画像、マスク（変更する部分を特定するもの）、そして何をすべきかを示すテキストプロンプトを提供することです。

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

  ベース画像にはウサギだけが含まれますが、最終的な画像にはウサギに帽子が追加されます。

- **バリエーションを作成する**。既存の画像を取り、それに基づいてバリエーションを作成するよう依頼するという考え方です。バリエーションを作成するには、画像とテキストプロンプトを提供し、次のようなコードを使用します：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注：これはOpenAIでのみサポートされています

## Temperature

temperatureは、生成AIモデルの出力のランダム性を制御するパラメータです。temperatureは0から1の間の値で、0は出力が決定的であることを意味し、1は出力がランダムであることを意味します。デフォルト値は0.7です。

temperatureがどのように機能するかを例を見てみましょう。このプロンプトを2回実行します：

> プロンプト: "霧の立ち込める草原で馬に乗っているウサギがキャンディーを持っている"

同じプロンプトを実行しても、同じ画像が2回生成されないことを確認してみましょう。

このように、画像は似ていますが、同じではありません。temperature値を0.1に変更して何が起こるか見てみましょう：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperatureの変更

応答をより決定的にしようとしてみましょう。生成した2つの画像から、最初の画像にはウサギがいて、2番目の画像には馬がいることが観察でき、画像は大きく異なります。

したがって、コードを変更してtemperatureを0に設定してみましょう：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

このコードを実行すると、次の2つの画像が得られます：

ここで、画像がより似ていることが明確にわかります。

## メタプロンプトでアプリケーションの境界を定義する方法

デモを使用すると、すでにクライアントのために画像を生成できます。しかし、アプリケーションの境界を作成する必要があります。

たとえば、仕事に不適切な画像や子供に不適切な画像を生成したくありません。

これをメタプロンプトで行うことができます。メタプロンプトは、生成AIモデルの出力を制御するために使用されるテキストプロンプトです。たとえば、メタプロンプトを使用して出力を制御し、生成される画像が仕事に適したものであるか、子供に適したものであることを確認できます。

### それはどのように機能するのか？

では、メタプロンプトはどのように機能するのでしょうか？

メタプロンプトは、生成AIモデルの出力を制御するために使用されるテキストプロンプトであり、テキストプロンプトの前に配置され、モデルの出力を制御するために使用され、モデルの出力を制御するためにアプリケーションに埋め込まれます。プロンプト入力とメタプロンプト入力を単一のテキストプロンプトにカプセル化します。

メタプロンプトの一例として、以下のようなものがあります：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

さて、デモでメタプロンプトをどのように使用できるか見てみましょう。

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

上記のプロンプトから、すべての画像がメタプロンプトを考慮して作成される様子がわかります。

## 課題 - 学生を支援しましょう

このレッスンの冒頭でEdu4Allを紹介しました。今度は、学生が評価のための画像を生成できるようにします。

学生たちは、評価のためにモニュメントを含む画像を作成します。どのモニュメントを選ぶかは学生に任されています。学生たちはこの課題で創造性を発揮し、これらのモニュメントを異なるコンテキストで配置するよう求められています。

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

## よくできました！学習を続けましょう

このレッスンを終えた後は、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めてください！

レッスン10では、[ローコードでAIアプリケーションを構築する方法](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)について学びます。

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の言語での文書が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。