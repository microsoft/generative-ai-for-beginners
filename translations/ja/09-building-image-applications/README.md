<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:12:07+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ja"
}
-->
# 画像生成アプリケーションの構築

[![画像生成アプリケーションの構築](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ja.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMはテキスト生成だけではありません。テキストの説明から画像を生成することも可能です。画像というモダリティを活用することで、医療技術、建築、観光、ゲーム開発など、さまざまな分野で非常に役立ちます。この章では、最も人気のある画像生成モデルであるDALL-EとMidjourneyについて見ていきます。

## はじめに

このレッスンでは、以下の内容を扱います。

- 画像生成とは何か、なぜ役立つのか
- DALL-EとMidjourneyとは何か、それらがどのように動作するのか
- 画像生成アプリをどのように作るか

## 学習目標

このレッスンを終えた後、あなたは以下のことができるようになります。

- 画像生成アプリケーションを構築できる
- メタプロンプトでアプリケーションの境界を定義できる
- DALL-EとMidjourneyを使いこなせる

## なぜ画像生成アプリケーションを作るのか？

画像生成アプリケーションは、生成AIの可能性を探る素晴らしい方法です。例えば、以下のような用途があります。

- **画像編集や合成**：さまざまな用途のために画像を生成できます。例えば画像編集や画像合成などです。

- **多様な業界での応用**：医療技術、観光、ゲーム開発など、さまざまな業界向けの画像生成にも活用できます。

## シナリオ：Edu4All

このレッスンでは、引き続き私たちのスタートアップ「Edu4All」を題材に進めます。生徒たちは自分たちの課題のために画像を作成します。どんな画像を作るかは生徒次第ですが、自分の童話のイラストを描いたり、新しいキャラクターを作ったり、アイデアやコンセプトを視覚化するのに役立てたりできます。

例えば、クラスで記念碑について学んでいる場合、Edu4Allの生徒たちは次のような画像を生成できます。

![Edu4Allスタートアップ、記念碑の授業、エッフェル塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ja.png)

このようなプロンプトを使って

> 「朝日が差し込むエッフェル塔のそばにいる犬」

## DALL-EとMidjourneyとは？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)と[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)は、最も人気のある画像生成モデルの2つで、プロンプトを使って画像を生成できます。

### DALL-E

まずはDALL-Eから見ていきましょう。DALL-Eはテキストの説明から画像を生成する生成AIモデルです。

> [DALL-Eは、CLIPとdiffused attentionという2つのモデルを組み合わせたものです](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**は、画像やテキストから数値表現（埋め込み）を生成するモデルです。

- **Diffused attention**は、埋め込みから画像を生成するモデルです。DALL-Eは画像とテキストのデータセットで学習されており、テキストの説明から画像を生成できます。例えば、帽子をかぶった猫や、モヒカンの犬の画像を生成することができます。

### Midjourney

MidjourneyもDALL-Eと同様に、テキストプロンプトから画像を生成します。Midjourneyでも「帽子をかぶった猫」や「モヒカンの犬」といったプロンプトで画像を作成できます。

![Midjourneyで生成された画像、機械仕掛けのハト](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_画像提供: Wikipedia、Midjourneyで生成_

## DALL-EとMidjourneyはどう動くのか

まず[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)について。DALL-Eはトランスフォーマーアーキテクチャに基づく生成AIモデルで、_オートレグレッシブトランスフォーマー_を採用しています。

_オートレグレッシブトランスフォーマー_は、テキストの説明から画像を生成する際に、一度に1ピクセルずつ生成し、生成したピクセルを使って次のピクセルを作り出します。ニューラルネットワークの複数の層を通して、画像が完成するまでこのプロセスを繰り返します。

この仕組みにより、DALL-Eは生成する画像の属性やオブジェクト、特徴などをコントロールできます。ただし、DALL-E 2や3では、より細かく画像を制御できるようになっています。

## 初めての画像生成アプリケーションを作る

画像生成アプリケーションを作るには何が必要でしょうか？以下のライブラリが必要です。

- **python-dotenv**：このライブラリを使うことで、秘密情報を_.env_ファイルに保存し、コードから分離できます。
- **openai**：OpenAI APIとやり取りするためのライブラリです。
- **pillow**：Pythonで画像を扱うためのライブラリです。
- **requests**：HTTPリクエストを送るためのライブラリです。

## Azure OpenAIモデルの作成とデプロイ

まだ作成していない場合は、[Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)の手順に従って
Azure OpenAIリソースとモデルを作成してください。モデルにはDALL-E 3を選択します。

## アプリの作成

1. _.env_ファイルを作成し、以下の内容を記載します。

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   この情報はAzure OpenAI Foundry Portalの「Deployments」セクションで確認できます。

1. 上記のライブラリを_requirements.txt_ファイルにまとめて記載します。

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 次に、仮想環境を作成し、ライブラリをインストールします。

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windowsの場合は、以下のコマンドで仮想環境を作成・有効化します。

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_というファイルに以下のコードを追加します。

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

このコードについて説明します。

- まず、必要なライブラリ（OpenAI、dotenv、requests、Pillow）をインポートします。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 次に、_.env_ファイルから環境変数を読み込みます。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- その後、Azure OpenAIサービスクライアントを設定します。

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- 次に、画像を生成します。

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上記のコードは、生成された画像のURLを含むJSONオブジェクトを返します。このURLを使って画像をダウンロードし、ファイルとして保存できます。

- 最後に、画像を開いて標準の画像ビューアで表示します。

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 画像生成コードの詳細

画像を生成するコードをもう少し詳しく見てみましょう。

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**は、画像生成に使うテキストプロンプトです。ここでは「馬に乗ったウサギが、霧のかかった水仙の咲く草原でペロペロキャンディを持っている」というプロンプトを使っています。
- **size**は生成する画像のサイズです。ここでは1024x1024ピクセルの画像を生成しています。
- **n**は生成する画像の枚数です。ここでは2枚生成しています。
- **temperature**は、生成AIモデルの出力のランダム性を制御するパラメータです。0から1の値で、0は決定的、1はランダムな出力になります。デフォルト値は0.7です。

画像に関しては、他にもできることがあり、次のセクションで紹介します。

## 画像生成の追加機能

ここまで、Pythonの数行で画像を生成できることを見てきました。しかし、画像に対してできることは他にもあります。

例えば、以下のことも可能です。

- **編集を行う**：既存の画像、マスク、プロンプトを指定することで画像を変更できます。例えば、画像の一部に何かを追加することができます。ウサギの画像に帽子を追加する場合、画像とマスク（変更したい部分を指定）と、何をするかを記述したテキストプロンプトを用意します。
> 注意：これはDALL-E 3ではサポートされていません。

以下はGPT Imageを使った例です。

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  元の画像はプール付きラウンジだけですが、最終的な画像にはフラミンゴが追加されています。

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **バリエーションを作成する**：既存の画像をもとにバリエーションを作成することもできます。画像とテキストプロンプトを指定し、以下のようなコードでバリエーションを生成します。

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意：これはOpenAIのみでサポートされています

## Temperature（温度）について

Temperatureは、生成AIモデルの出力のランダム性を制御するパラメータです。0から1の値で、0は決定的、1はランダムな出力になります。デフォルト値は0.7です。

Temperatureの働きを例で見てみましょう。同じプロンプトを2回実行します。

> プロンプト：「馬に乗ったウサギが、霧のかかった水仙の咲く草原でペロペロキャンディを持っている」

![馬に乗ったウサギがペロペロキャンディを持っている画像、バージョン1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ja.png)

同じプロンプトをもう一度実行してみると、同じ画像にはなりません。

![馬に乗ったウサギが生成された画像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ja.png)

ご覧の通り、画像は似ていますが全く同じではありません。今度はtemperatureの値を0.1にしてみましょう。

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### temperatureを変更する

より決定的な応答にしたい場合はどうすればよいでしょうか。先ほど生成した2枚の画像を見ると、1枚目はウサギ、2枚目は馬が目立っており、かなり違いがあります。

そこで、コードを変更してtemperatureを0に設定してみます。

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

このコードを実行すると、次の2枚の画像が得られます。

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ja.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ja.png)

このように、画像同士がより似ていることが分かります。

## メタプロンプトでアプリケーションの境界を定義する方法

このデモでは、すでにクライアント向けに画像を生成できます。しかし、アプリケーションには一定の境界を設ける必要があります。

例えば、不適切な画像や子どもにふさわしくない画像は生成したくありません。

これには_メタプロンプト_を使います。メタプロンプトは、生成AIモデルの出力をコントロールするためのテキストプロンプトです。例えば、メタプロンプトを使って、生成される画像が安全であることや、子ども向けであることを保証できます。

### どのように機能するのか？

では、メタプロンプトはどのように機能するのでしょうか。

メタプロンプトは、生成AIモデルの出力をコントロールするためのテキストプロンプトで、通常のプロンプトの前に配置されます。アプリケーション内でプロンプト入力とメタプロンプト入力を1つのテキストプロンプトにまとめて使います。

メタプロンプトの一例は以下の通りです。

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

では、デモでメタプロンプトをどのように使うか見てみましょう。

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

上記のプロンプトから、すべての生成画像がメタプロンプトを考慮していることが分かります。

## 課題 - 生徒たちに画像生成を体験させよう

このレッスンの冒頭でEdu4Allを紹介しました。今度は、生徒たちが自分の課題のために画像を生成できるようにしましょう。

生徒たちは記念碑を含む画像を作成します。どの記念碑にするかは生徒次第です。生徒たちには、これらの記念碑をさまざまな文脈で表現する創造力を発揮してもらいます。

## 解答例

一つの解答例を紹介します。

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

## お疲れさまでした！さらに学びを深めましょう
このレッスンを終えたら、[ジェネレーティブAI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)で、ジェネレーティブAIの知識をさらに深めましょう！

次はレッスン10へ進み、[ローコードでAIアプリケーションを構築する方法](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)を学びます。

---

**免責事項**：  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。原文（元の言語の文書）が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。