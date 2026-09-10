# 画像生成アプリケーションの構築

[![画像生成アプリケーションの構築](../../../translated_images/ja/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMはテキスト生成だけではありません。テキストの説明から画像を生成することもできます。画像というモダリティはMedTech、建築、観光、ゲーム開発、マーケティングなど幅広い分野で役立ちます。このレッスンでは最新の<strong>GPT Image</strong>モデルを見て、画像生成アプリを作成します。

## はじめに

画像生成は自然言語のプロンプトを画像に変換します。このレッスンではOpenAIの**`gpt-image`**ファミリーを扱います。これは**[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)**とOpenAIプラットフォームで利用可能な最新世代の画像モデルです。これらのモデルは旧来のDALL·Eモデル（DALL·E 2/3はレガシー）に代わります。

レッスンを通じて、架空のスタートアップである<strong>Edu4All</strong>が学習ツールを作っており、課題や学習資料のイラストを生成したいという設定で進めます。

## 学習目標

このレッスンの終わりには以下ができるようになります：

- 画像生成とは何か、その活用場面の説明。
- `gpt-image`モデルファミリーの理解と、レガシーDALL·Eモデルとの違いの把握。
- Python（およびTypeScript / .NET）で画像生成アプリを構築。
- メタプロンプトを用いた画像編集と安全ガードレールの適用。

## 画像生成とは？

画像生成モデルはテキストプロンプトから画像を生成します。最新の`gpt-image`モデルはトランスフォーマーと拡散（diffusion）技術を組み合わせて構築されており、訓練時にテキストと画像の関係を学び、与えられたプロンプトに基づきランダムノイズを段階的に「ノイズ除去」して説明に合う画像を生成します。

よく知られた画像モデルファミリーには以下があります：

- **`gpt-image`（OpenAI）** - 今回のレッスンで使う最新世代モデル。テキストから画像生成やマスクを用いた編集（インペインティング）に対応。
- **Midjourney** - 独自サービスとDiscordワークフローを持つ人気のサードパーティモデル。

> 旧OpenAI画像モデルである<strong>DALL·E 2</strong>および<strong>DALL·E 3</strong>はレガシーです。DALL·E 3は新規展開に使えず、`create_variation`機能はDALL·E 2のみ存在しました。新規アプリには`gpt-image`モデルを使ってください。

### どの`gpt-image`モデルを使うべき？

Microsoft Foundryで以下が<strong>一般提供</strong>されています：

| モデル | 説明 |
| --- | --- |
| **`gpt-image-2`** | 最新で最も高性能な画像モデル - 推奨デフォルト。 |
| `gpt-image-1.5` | 一般提供されており、コストを抑えて高品質。 |
| `gpt-image-1-mini` | 一般提供されており、最速かつ最安。 |
| `gpt-image-1` | プレビュー版のみ。 |

利用可能地域や提供状況は常に最新の[Foundry画像モデル一覧](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst)を確認してください。

> **重要：** `gpt-image`モデルは生成された画像をURLではなく、**base64**（`b64_json`）で返します。コード側でbase64文字列をバイトにデコードして保存してください。画像のダウンロード用URLはありません。

## セットアップ

サンプルは<strong>Microsoft FoundryのAzure OpenAI</strong>（`aoai-*`サンプル）か<strong>OpenAIプラットフォーム</strong>（`oai-*`サンプル）で実行できます。

### 1. モデルを作成しデプロイする

[リソース作成](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)ガイドに従いMicrosoft Foundryリソースを作成し、画像モデルをデプロイしてください。**`gpt-image-2`**を推奨します。

### 2. `.env`を設定する

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

[Foundryポータル](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)のリソースの<strong>Deployments</strong>ページでこれらの値を見つけてください。

### 3. ライブラリをインストールする

`requirements.txt`を作成：

```text
python-dotenv
openai
pillow
```

そして仮想環境を作成・有効化し、インストール：

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## アプリを構築する

以下のコードで`app.py`を作成します。画像を生成しPNGとして保存します。

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# クライアントを Azure OpenAI (Microsoft Foundry) リソースに向けます。
# 画像モデルには最新の API バージョンが必要です - ご利用のモデルが必要とするバージョンは Foundry のドキュメントで確認してください。
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # 例: "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # また、1536x1024（横向き）、1024x1536（縦向き）、または「自動」もあります。
    n=1,
)

# gpt-image モデルは URL ではなく base64 (b64_json) を返します - バイトにデコードしてください。
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

`python app.py`で実行してください。`images/`にPNGファイルが保存されます。

> `images.generate`を呼ぶたびに同じプロンプトでも異なる画像が生成されます。画像モデルは`temperature`パラメーターを使いません（それはテキスト生成用の制御です）。バリエーションを増やしたいならAPIを再度呼び、減らしたいならプロンプトをより具体的にしてください。

## 画像編集

`gpt-image`モデルは既存の画像を<strong>編集</strong>できます。画像とオプションの<strong>マスク</strong>（編集する領域を示す）、編集内容を説明するプロンプトを与えます。生成された編集結果もbase64で返されます。

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ja/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ja/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ja/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## メタプロンプトで境界線を設定する

画像を生成できるようになったら、アプリで安全でない内容やブランドに合わない内容が出ないようガードレールが必要です。<strong>メタプロンプト</strong>はユーザーのプロンプトに先置きしてモデルの出力を制限するテキストです。

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# `prompt`をclient.images.generate(...)に渡す
```

すべての画像はメタプロンプトで設定された境界内で生成されます。Microsoft Foundryに組み込まれたコンテンツフィルターと組み合わせて多層防御を実現します。

## 課題 - 学生に使わせてみよう

Edu4Allの学生はアセスメントに画像が必要です。<strong>記念碑</strong>（どの記念碑かは自由）を、異なる創造的な文脈に配置した画像を生成するアプリを作ってみてください。例えば、有名なランドマークの夕暮れ時と見つめる子どもなど。

自分で試してみて、参照解答と比較してください：

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) フル生成アプリ: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

また[python/](../../../09-building-image-applications/python)のノートブックも進めてみてください（Azure用は`aoai-assignment.ipynb`、OpenAI用は`oai-assignment.ipynb`）。

## お疲れさまでした！学習を続けましょう

このレッスンを終えたら[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに高めてください！

レッスン10に進んで学習を続けましょう。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->