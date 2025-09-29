<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:33:19+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ja"
}
-->
# 画像生成アプリケーションの構築

[![画像生成アプリケーションの構築](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ja.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMにはテキスト生成以外にも多くの可能性があります。テキストの説明から画像を生成することも可能です。画像をモダリティとして活用することで、MedTech、建築、観光、ゲーム開発など、さまざまな分野で非常に役立つことがあります。この章では、最も人気のある画像生成モデルであるDALL-EとMidjourneyについて学びます。

## はじめに

このレッスンでは以下を学びます：

- 画像生成とその有用性
- DALL-EとMidjourneyの概要と仕組み
- 画像生成アプリの構築方法

## 学習目標

このレッスンを完了すると、以下ができるようになります：

- 画像生成アプリケーションを構築する
- メタプロンプトを使用してアプリケーションの境界を定義する
- DALL-EとMidjourneyを活用する

## なぜ画像生成アプリケーションを構築するのか？

画像生成アプリケーションは、生成AIの能力を探求する素晴らしい方法です。以下のような用途で活用できます：

- **画像編集と合成**：画像編集や画像合成など、さまざまな用途に画像を生成できます。

- **多様な業界への応用**：MedTech、観光、ゲーム開発など、さまざまな業界で画像を生成するために使用できます。

## シナリオ: Edu4All

このレッスンでは、引き続きスタートアップ「Edu4All」と取り組みます。学生たちは自分たちの評価のために画像を作成します。どのような画像を作成するかは学生次第ですが、自分たちの童話のイラストを作成したり、新しいキャラクターを創造したり、アイデアや概念を視覚化するのに役立てることができます。

例えば、学生たちが授業でモニュメントについて学んでいる場合、以下のような画像を生成できます：

![Edu4Allスタートアップ、モニュメントの授業、エッフェル塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ja.png)

以下のようなプロンプトを使用して：

> 「早朝の陽光の中でエッフェル塔の隣にいる犬」

## DALL-EとMidjourneyとは？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)と[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)は、最も人気のある画像生成モデルであり、プロンプトを使用して画像を生成することができます。

### DALL-E

まずDALL-Eについて説明します。これはテキストの説明から画像を生成する生成AIモデルです。

> [DALL-EはCLIPと拡散注意の2つのモデルの組み合わせです](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**は、画像やテキストから数値表現（埋め込み）を生成するモデルです。

- **拡散注意**は、埋め込みから画像を生成するモデルです。DALL-Eは画像とテキストのデータセットで訓練されており、テキストの説明から画像を生成することができます。例えば、DALL-Eを使用して帽子をかぶった猫やモヒカンの犬の画像を生成することができます。

### Midjourney

MidjourneyはDALL-Eと似た方法で動作し、テキストプロンプトから画像を生成します。Midjourneyも「帽子をかぶった猫」や「モヒカンの犬」のようなプロンプトを使用して画像を生成することができます。

![Midjourneyによって生成された画像、機械的な鳩](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_画像提供: Wikipedia、Midjourneyによって生成された画像_

## DALL-EとMidjourneyの仕組み

まず、[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)について説明します。DALL-Eはトランスフォーマーアーキテクチャに基づく生成AIモデルで、_自己回帰型トランスフォーマー_を使用しています。

_自己回帰型トランスフォーマー_は、モデルがテキストの説明から画像を生成する方法を定義します。1ピクセルずつ生成し、生成されたピクセルを使用して次のピクセルを生成します。このプロセスはニューラルネットワークの複数の層を通過し、画像が完成するまで続きます。

このプロセスにより、DALL-Eは生成する画像の属性、オブジェクト、特徴などを制御します。ただし、DALL-E 2や3では生成画像の制御がさらに向上しています。

## 初めての画像生成アプリケーションの構築

画像生成アプリケーションを構築するには、以下のライブラリが必要です：

- **python-dotenv**：秘密情報をコードから離れた_.env_ファイルに保存するために推奨されるライブラリ。
- **openai**：OpenAI APIとやり取りするために使用するライブラリ。
- **pillow**：Pythonで画像を操作するためのライブラリ。
- **requests**：HTTPリクエストを行うためのライブラリ。

## Azure OpenAIモデルの作成とデプロイ

まだ行っていない場合は、[Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)ページの指示に従ってAzure OpenAIリソースとモデルを作成してください。モデルにはDALL-E 3を選択します。

## アプリの作成

1. 以下の内容で_.env_ファイルを作成します：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   この情報はAzure OpenAI Foundry Portalの「Deployments」セクションで確認できます。

1. 上記のライブラリを以下のように_requirements.txt_ファイルにまとめます：

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

1. _app.py_というファイルに以下のコードを追加します：

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

このコードを説明します：

- まず、OpenAIライブラリ、dotenvライブラリ、requestsライブラリ、Pillowライブラリなど必要なライブラリをインポートします。

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

- 次に、画像を生成します：

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上記のコードは生成された画像のURLを含むJSONオブジェクトを返します。このURLを使用して画像をダウンロードし、ファイルに保存できます。

- 最後に、画像を開き、標準の画像ビューアで表示します：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 画像生成の詳細

画像を生成するコードを詳しく見てみましょう：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**：画像を生成するために使用されるテキストプロンプト。この場合、「霧の立ち込める牧草地でスイセンが育つ場所で、馬に乗ったウサギがキャンディを持っている」というプロンプトを使用しています。
- **size**：生成される画像のサイズ。この場合、1024x1024ピクセルの画像を生成しています。
- **n**：生成される画像の数。この場合、2枚の画像を生成しています。
- **temperature**：生成AIモデルの出力のランダム性を制御するパラメータ。温度は0から1の値で、0は出力が決定的であることを意味し、1は出力がランダムであることを意味します。デフォルト値は0.7です。

画像に関してさらにできることについては、次のセクションで説明します。

## 画像生成の追加機能

これまでPythonで数行のコードを使用して画像を生成する方法を見てきました。しかし、画像に関してさらにできることがあります。

以下のことも可能です：

- **編集を行う**：既存の画像、マスク、プロンプトを提供することで画像を変更できます。例えば、画像の一部に何かを追加することができます。ウサギの画像を想像してみてください。ウサギに帽子を追加することができます。これを行うには、画像、マスク（変更する部分を特定するもの）、変更内容を指示するテキストプロンプトを提供します。
> 注意：これはDALL-E 3ではサポートされていません。

以下はGPT Imageを使用した例です：

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  基本画像にはプール付きのラウンジのみが含まれますが、最終画像にはフラミンゴが追加されます：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ja.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ja.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ja.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **バリエーションを作成する**：既存の画像を使用してバリエーションを作成することができます。バリエーションを作成するには、画像とテキストプロンプトを提供し、以下のようなコードを使用します：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意：これはOpenAIでのみサポートされています。

## 温度

温度は生成AIモデルの出力のランダム性を制御するパラメータです。温度は0から1の値で、0は出力が決定的であることを意味し、1は出力がランダムであることを意味します。デフォルト値は0.7です。

以下のプロンプトを2回実行して温度の動作を確認してみましょう：

> プrompt : 「霧の立ち込める牧草地でスイセンが育つ場所で、馬に乗ったウサギがキャンディを持っている」

![馬に乗ったウサギがキャンディを持っている画像、バージョン1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ja.png)

同じプロンプトを再度実行してみると、同じ画像が生成されないことがわかります：

![馬に乗ったウサギが生成された画像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ja.png)

ご覧の通り、画像は似ていますが同じではありません。次に温度値を0.1に変更してみましょう：

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 温度の変更

応答をより決定的にするために試してみましょう。生成された2つの画像から、最初の画像にはウサギがいて、2番目の画像には馬がいることがわかります。画像は大きく異なります。

そこで、コードを変更して温度を0に設定してみます：

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

このコードを実行すると、以下の2つの画像が生成されます：

- ![温度0、バージョン1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ja.png)
- ![温度0、バージョン2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ja.png)

これにより、画像がより似ていることが明確にわかります。

## メタプロンプトを使用してアプリケーションの境界を定義する方法

デモでは、すでにクライアント向けに画像を生成することができます。しかし、アプリケーションにいくつかの境界を設ける必要があります。

例えば、職場で安全でない画像や子供に適さない画像を生成したくありません。

これをメタプロンプトを使用して実現できます。メタプロンプトは生成AIモデルの出力を制御するために使用されるテキストプロンプトです。例えば、メタプロンプトを使用して出力を制御し、生成される画像が職場で安全であることや子供に適していることを保証できます。

### 仕組みは？

では、メタプロンプトはどのように機能するのでしょうか？

メタプロンプトは生成AIモデルの出力を制御するために使用されるテキストプロンプトであり、テキストプロンプトの前に配置され、モデルの出力を制御します。アプリケーションに埋め込まれ、モデルの出力を制御します。プロンプト入力とメタプロンプト入力を単一のテキストプロンプトにまとめます。

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

では、デモでメタプロンプトを使用する方法を見てみましょう。

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

上記のプロンプトから、生成されるすべての画像がメタプロンプトを考慮していることがわかります。

## 課題 - 学生を支援しよう

このレッスンの冒頭でEdu4Allを紹介しました。今度は学生が評価のために画像を生成できるようにしましょう。

学生たちはモニュメントを含む評価用の画像を作成します。どのモニュメントを選ぶかは学生次第です。学生たちはこの課題で創造性を発揮し、これらのモニュメントをさまざまな文脈に配置することが求められます。

## 解決策

以下は一つの解決策です：
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

## 素晴らしい仕事です！学習を続けましょう

このレッスンを完了した後は、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めてください！

次のレッスン10では、[ローコードでAIアプリケーションを構築する方法](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)について学びます。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。