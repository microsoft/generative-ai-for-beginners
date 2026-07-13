# 画像生成アプリケーションの構築

[![画像生成アプリケーションの構築](../../../translated_images/ja/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMはテキスト生成だけではありません。テキストの説明から画像を生成することも可能です。画像をモダリティとして持つことは、医療技術、建築、観光、ゲーム開発など多くの分野で非常に役立ちます。この章では、最も人気のある画像生成モデルの2つ、DALL-EとMidjourneyについて見ていきます。

## はじめに

本レッスンでは以下を扱います：

- 画像生成とその有用性について。
- DALL-EとMidjourneyの概要と仕組み。
- 画像生成アプリの構築方法。

## 学習目標

このレッスンを終えると、以下が可能になります：

- 画像生成アプリケーションを構築する。
- メタプロンプトでアプリケーションの境界を定義する。
- DALL-EとMidjourneyを使いこなす。

## なぜ画像生成アプリを作るのか？

画像生成アプリは生成AIの能力を探求する良い方法です。例えば、以下の用途があります：

- <strong>画像の編集や合成</strong>。画像編集や画像合成など、さまざまな用途で画像を生成できます。

- **様々な業界への応用**。医療技術、観光、ゲーム開発など多岐にわたる業界で画像生成に活用できます。

## シナリオ：Edu4All

このレッスンでは、引き続きスタートアップのEdu4Allと共に作業します。学生たちは評価のために画像を作成します。どんな画像かは学生次第ですが、自分の童話の挿絵にしたり、新しいキャラクターを作成したり、アイデアや概念の視覚化の助けにすることが可能です。

例えば、学生が授業で記念碑について作業している場合、Edu4Allの学生が生成できる画像例は以下のとおりです：

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/ja/startup.94d6b79cc4bb3f5a.webp)

以下のようなプロンプトを使っています：

> "朝早い日差しのエッフェル塔の横にいる犬"

## DALL-EとMidjourneyとは？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) と [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) は、最も人気のある画像生成モデルの2つです。プロンプトから画像を生成できます。

### DALL-E

まずDALL-Eから始めましょう。DALL-Eはテキストの説明から画像を生成する生成AIモデルです。

> [DALL-EはCLIPと拡散注意機構（diffused attention）という2つのモデルの組み合わせです](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** は、画像とテキストからデータの数値表現である埋め込み（embedding）を生成するモデルです。

- <strong>拡散注意機構</strong> は、埋め込みから画像を生成するモデルです。DALL-Eは画像とテキストのデータセットで学習され、テキストの説明から画像を生成できます。例えば、帽子をかぶった猫やモヒカンの犬の画像を生成できます。

### Midjourney

MidjourneyはDALL-Eと似た仕組みで、テキストプロンプトから画像を生成します。例えば「帽子をかぶった猫」や「モヒカンの犬」といったプロンプトからも画像が生成できます。

![Midjourneyで生成された画像、機械仕掛けの鳩](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_画像提供：Wikipedia、Midjourneyで生成された画像_

## DALL-EとMidjourneyの仕組み

まずは[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)です。DALL-Eはトランスフォーマーアーキテクチャに基づく生成AIモデルで、_自己回帰型トランスフォーマー_を用いています。

_自己回帰型トランスフォーマー_ は、モデルがテキストの説明から画像を一度に1ピクセルずつ生成し、生成したピクセルを用いて次のピクセルを生成する方法を定義しています。ニューラルネットワークの複数の層を通過し、画像が完成します。

このプロセスにより、DALL-Eは生成する画像の属性、オブジェクト、特徴などを制御します。ただし、DALL-E 2や3の方が生成画像の制御がより進化しています。

## 最初の画像生成アプリケーションを構築する

画像生成アプリを作るには何が必要でしょうか？以下のライブラリが必要です：

- **python-dotenv** は、シークレット情報をコードから分離して_.env_ファイルに管理するためのライブラリで、使用が強く推奨されます。
- **openai** は、OpenAI APIと連携するために使います。
- **pillow** はPythonで画像を扱うためのライブラリです。
- **requests** はHTTPリクエストを簡単に行うためのライブラリです。

## Azure OpenAIモデルを作成し展開する

まだの場合は、[Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)の手順に従い、
Azure OpenAIリソースとモデルを作成してください。モデルは **gpt-image-1** を選択します（現在のAzure OpenAI画像モデル。DALL-E 3はレガシーで新規展開はできません）。

## アプリを作成する

1. _.env_ ファイルを以下の内容で作成します：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Azure OpenAI Foundryポータルの「Deployments」セクションでこの情報を確認できます。

1. 上記のライブラリを _requirements.txt_ にまとめます：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 次に、仮想環境を作成してライブラリをインストールします：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windowsの場合は以下のコマンドで仮想環境を作成しアクティベートします：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ファイルに以下のコードを記述します：

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenvをインポートする
    dotenv.load_dotenv()
    
    # Azure OpenAIサービスクライアントを設定する
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # 画像生成APIを使用して画像を作成する
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # 保存された画像のディレクトリを設定する
        image_dir = os.path.join(os.curdir, 'images')

        # ディレクトリが存在しない場合は作成する
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # 画像パスを初期化する（ファイルタイプはpngにすること）
        image_path = os.path.join(image_dir, 'generated-image.png')

        # 生成された画像を取得する
        image_url = generation_response.data[0].url  # レスポンスから画像URLを抽出する
        generated_image = requests.get(image_url).content  # 画像をダウンロードする
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # デフォルトの画像ビューアで画像を表示する
        image = Image.open(image_path)
        image.show()

    # 例外をキャッチする
    except openai.BadRequestError as err:
        print(err)
   ```

このコードを説明します：

- まず、OpenAIライブラリ、dotenvライブラリ、requestsライブラリ、Pillowライブラリなど必要なライブラリをインポートします。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 次に、_.env_ ファイルから環境変数を読み込みます。

  ```python
  # dotenvをインポートする
  dotenv.load_dotenv()
  ```

- その後、Azure OpenAIサービスクライアントの設定を行います。

  ```python
  # エンドポイントとキーを環境変数から取得する
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- 次に、画像を生成します：

  ```python
  # 画像生成APIを使用して画像を作成する
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上記コードは生成された画像のURLを含むJSONオブジェクトで応答します。URLを使って画像をダウンロードし、ファイルに保存できます。

- 最後に、画像を開き、標準の画像ビューアで表示します：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 画像生成の詳細

画像生成のコードをもう少し詳しく見てみましょう：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** は画像生成に使うテキストプロンプトです。この例では「Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils」を使っています。
- **size** は生成する画像のサイズで、この例では1024x1024ピクセルです。
- **n** は生成する画像の枚数で、この例では2枚生成します。
- **temperature** は生成AIモデルの出力のランダム性を制御するパラメーターで、0から1の値をとります。0は決定論的で1は完全にランダムです。初期値は0.7です。

次のセクションで、画像でできる他のことも説明します。

## 画像生成の追加機能

これまでPythonの数行のコードで画像を生成できることを見てきましたが、画像でできることはもっとあります。

次のことも可能です：

- <strong>編集を行う</strong>。既存の画像にマスクとプロンプトを使うことで、画像を変更できます。例えば、ウサギの画像に帽子を追加できます。やり方は、画像と変更部分を示すマスク、そして何をするかのテキストプロンプトを用意します。
> 注意：これはDALL-E 3ではサポートされていません。
 
GPT Imageを使った例はこちらです：

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  ベース画像はプール付きラウンジのみですが、完成画像にはフラミンゴが追加されています：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ja/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ja/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ja/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- <strong>変種を作成する</strong>。既存画像を元にバリエーションを作成します。変種作成は画像とテキストプロンプトを提供して、次のようにコードを書きます：

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > 注意：これはOpenAIのDALL-E 2モデルのみサポートされており、gpt-image-1ではサポートされていません

## 温度（Temperature）

Temperatureは生成AIモデルの出力のランダム性を制御するパラメーターで、0から1の間の値をとります。0は決定論的、1はランダムな出力になります。初期値は0.7です。

Temperatureがどのように働くか、以下のプロンプトを2回実行してみて確認しましょう：

> プロンプト : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![棒付きキャンディを持つ馬の上のウサギ、バージョン1](../../../translated_images/ja/v1-generated-image.a295cfcffa3c13c2.webp)

同じプロンプトを再度実行して、同じ画像が2回生成されないことを確認します：

![馬の上のウサギの生成画像](../../../translated_images/ja/v2-generated-image.33f55a3714efe61d.webp)

画像は似ていますが同じではありません。次にtemperature値を0.1に変更して動作を見てみましょう：

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ここにプロンプトテキストを入力してください
        size='1024x1024',
        n=2
    )
```

### 温度の変更

では、応答をより決定論的にします。2つの画像を比較すると、1枚目はウサギ、2枚目は馬がいて、大きく異なることが分かります。

そこでコードを変更しtemperatureを0に設定します：

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # プロンプトテキストをここに入力してください
        size='1024x1024',
        n=2,
        temperature=0
    )
```

このコードを実行すると、次の2つの画像が得られます：

- ![Temperature 0, v1](../../../translated_images/ja/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0, v2](../../../translated_images/ja/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ここでは画像同士がより似ていることが明確に見て取れます。

## メタプロンプトでアプリの境界を定義する方法

デモではすでにクライアント向けの画像生成が可能ですが、アプリに境界を作る必要があります。

例えば、就労環境に不適切な画像や子供にふさわしくない画像は生成させたくありません。

これは_メタプロンプト_で制御できます。メタプロンプトは生成AIモデルの出力を制御するためのテキストプロンプトです。例えば、メタプロンプトを使って「仕事場で安全」「子供に適切」といった生成画像を保証できます。

### 仕組み

メタプロンプトはどう機能するのでしょうか？

メタプロンプトは生成AIモデルの出力を制御するテキストプロンプトで、テキストプロンプトの前に置かれ、モデルの出力を制御します。アプリケーションに組み込まれ、プロンプト入力とメタプロンプト入力をひとつにまとめています。

メタプロンプトの例は以下の通りです：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

では、デモでメタプロンプトをどう使うか見てみましょう。

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

# TODO 画像生成リクエストを追加する
```

上記のプロンプトから、生成される全画像がメタプロンプトに従っていることがわかります。

## 課題 - 学生に生成を促す

このレッスンの冒頭で紹介したEdu4All。いよいよ学生が評価用の画像を生成できるようにします。


学生たちは評価用に、記念碑を含む画像を作成します。どの記念碑にするかは学生に任されています。学生たちはこの課題で創造力を発揮し、これらの記念碑をさまざまな文脈に配置することが求められています。

## 解決策

こちらは一つの可能な解決策です：

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# エンドポイントとキーを環境変数から取得する
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
    # 画像生成APIを使用して画像を作成する
    generation_response = client.images.generate(
        prompt=prompt,    # プロンプトテキストをここに入力してください
        size='1024x1024',
        n=1,
    )
    # 保存された画像のディレクトリを設定する
    image_dir = os.path.join(os.curdir, 'images')

    # ディレクトリが存在しない場合は作成する
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # 画像パスを初期化する（ファイルタイプはpngにすること）
    image_path = os.path.join(image_dir, 'generated-image.png')

    # 生成された画像を取得する
    image_url = generation_response.data[0].url  # レスポンスから画像URLを抽出する
    generated_image = requests.get(image_url).content  # 画像をダウンロードする
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # デフォルトの画像ビューアで画像を表示する
    image = Image.open(image_path)
    image.show()

# 例外をキャッチする
except openai.BadRequestError as err:
    print(err)
```

## 素晴らしい仕事です！学習を続けましょう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をチェックして、ジェネレーティブAIの知識をさらに高めましょう！

レッスン10に進み、[ローコードでAIアプリケーションを作成する方法](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)について見ていきます

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->