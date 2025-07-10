<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:27:23+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ja"
}
-->

# Python Web APIのコードを生成する

このドキュメントでは、Pythonを使ってWeb APIを作成する方法について説明します。

## はじめに

Pythonはシンプルで強力なプログラミング言語であり、Web APIの開発に適しています。ここでは、Flaskフレームワークを使った基本的なAPIの作成例を紹介します。

## 必要なライブラリのインストール

まず、Flaskをインストールします。

```bash
pip install Flask
```

## 基本的なAPIの作成

以下は、簡単なAPIエンドポイントを作成するサンプルコードです。

```python
from flask import Flask, jsonify

app = Flask(__name__)

# ルートエンドポイント
@app.route('/')
def home():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
```

## 実行方法

上記のコードを`app.py`というファイルに保存し、以下のコマンドで実行します。

```bash
python app.py
```

ブラウザで`http://localhost:5000/`にアクセスすると、JSON形式のメッセージが表示されます。

## まとめ

このように、Flaskを使うことで簡単にPythonでWeb APIを作成できます。さらに複雑な機能を追加することで、実用的なAPIを構築可能です。
```python
#import necessary libraries
import flask
from flask import request, jsonify

#create an instance of the Flask class
app = flask.Flask(__name__)

#create an endpoint for the API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #get the request data
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#function to process the data
def process_data(data):
    #process the data
    result = {'result': 'success'}

    #return the result
    return result

#run the Flask app
if __name__ == '__main__':
    app.run()

```

もう一度プロンプトを実行すると、次のような結果が得られます：

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

この2つの出力にはほんのわずかな違いしかありません。今回は逆に、temperatureを0.9に設定してみましょう：

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

そして、temperature値を0.9にした2回目の試み：

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

ご覧の通り、結果は大きく異なっています。

> Note, that there are more parameters you can change to vary the output, like top-k, top-p, repetition penalty, length penalty and diversity penalty but these are outside the scope of this curriculum.

## 良いプラクティス

望む結果を得るために試せるプラクティスはたくさんあります。プロンプトを使い込むうちに、自分なりのスタイルが見つかるでしょう。

これまでに紹介したテクニックに加えて、LLMにプロンプトを投げる際に考慮すべき良いプラクティスがあります。

以下は考慮すべき良いプラクティスです：

- **コンテキストを明確にする**。コンテキストは重要です。ドメインやトピックなど、できるだけ具体的に指定しましょう。
- 出力を制限する。特定のアイテム数や長さが欲しい場合は、それを明示してください。
- **何をどうするかを明示する**。欲しいものとその方法の両方を伝えましょう。例えば「productsとcustomersのルートを持つPythonのWeb APIを作成し、3つのファイルに分割する」といった具合です。
- **テンプレートを使う**。会社のデータなどでプロンプトを充実させたい場合はテンプレートを活用しましょう。テンプレートには実際のデータに置き換える変数を含めることができます。
- **正しいスペルを使う**。LLMは正しい回答を返すこともありますが、正しいスペルで入力したほうがより良い回答が得られます。

## 課題

Flaskを使ってシンプルなAPIを作るPythonコードはこちらです：

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

GitHub CopilotやChatGPTのようなAIアシスタントを使い、「self-refine」テクニックを適用してコードを改善してみましょう。

## 解答例

適切なプロンプトをコードに追加して課題を解いてみてください。

> [!TIP]
> 改善を依頼するプロンプトを作成するときは、改善の回数を制限するのが良いでしょう。また、アーキテクチャ、パフォーマンス、セキュリティなど特定の観点で改善を求めることもできます。

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## 知識チェック

なぜchain-of-thoughtプロンプティングを使うのでしょうか？正しい回答1つと間違った回答2つを示してください。

1. 問題解決の方法をLLMに教えるため。
1. B, コードのエラーを見つけるようLLMに教えるため。
1. C, LLMに異なる解決策を考えさせるため。

A: 1が正解です。chain-of-thoughtは、LLMに一連のステップや類似問題の解決方法を示すことで、問題の解き方を教える手法だからです。

## 🚀 チャレンジ

課題でself-refineテクニックを使いましたね。あなたが作ったプログラムの中から1つ選び、どんな改善を加えたいか考えてみてください。次にself-refineテクニックを使って提案した変更を適用してみましょう。結果はどうでしたか？良くなりましたか、それとも悪くなりましたか？

## 素晴らしい！学習を続けましょう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)でさらにジェネレーティブAIの知識を深めていきましょう！

次のレッスン6では、プロンプトエンジニアリングの知識を活かして[テキスト生成アプリを作成します](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。