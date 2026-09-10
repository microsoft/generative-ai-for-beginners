# テキスト生成アプリケーションの構築

[![テキスト生成アプリケーションの構築](../../../translated_images/ja/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(このレッスンのビデオを見るには上の画像をクリックしてください)_

これまでのカリキュラムで、プロンプトのようなコアコンセプトや「プロンプトエンジニアリング」という分野があることを見てきました。ChatGPT、Office 365、Microsoft Power Platform など、多くのツールは、何かを達成するためにプロンプトを使うことをサポートしています。

そのような体験をアプリに追加するには、プロンプトやコンプリーションの概念を理解し、使うライブラリを選ぶ必要があります。本章でまさにそれを学びます。

## はじめに

この章では、以下を学びます：

- openai ライブラリとそのコアコンセプトについて学ぶ。
- openai を使ってテキスト生成アプリを構築する。
- プロンプト、温度、トークンなどの概念を使用してテキスト生成アプリを作成する方法を理解する。

## 学習目標

このレッスンの終わりには、以下ができるようになります：

- テキスト生成アプリとは何か説明できる。
- openai を使ってテキスト生成アプリを構築できる。
- より多くまたは少ないトークンを使用するようアプリを構成し、出力のバリエーションのために温度も変更できる。

## テキスト生成アプリとは？

通常、アプリを作るときは以下のようなインターフェイスがあります：

- コマンドベース。コンソールアプリは典型的なアプリで、コマンドを入力してタスクを実行します。例として `git` はコマンドベースのアプリです。
- ユーザーインターフェース（UI）。ボタンをクリックしたり、テキストを入力したり、オプションを選択したりするグラフィカルユーザーインターフェース (GUI) を持つアプリもあります。

### コンソールおよびUIアプリの制限

コマンドベースのアプリでコマンドを入力する場合と比較すると：

- <strong>制限がある</strong>。サポートされているコマンドのみ入力可能で、どんなコマンドでも入力できるわけではありません。
- <strong>言語特化型</strong>。多言語対応のアプリもありますが、通常は特定の言語向けに作られており、追加できてもデフォルトの言語は決まっています。

### テキスト生成アプリの利点

では、テキスト生成アプリはどう違うのでしょうか？

テキスト生成アプリでは柔軟性が高く、決まったコマンドや特定の入力言語に制限されません。代わりに自然言語を使ってアプリとやり取りできます。さらに、既に膨大な情報コーパスで訓練されたデータソースとやり取りしているため、従来のアプリのようにデータベースの内容に制限されません。

### テキスト生成アプリで何が作れる？

様々なものが作れます。例えば：

- <strong>チャットボット</strong>。会社や製品について質問に答えるチャットボットなどに適しています。
- <strong>ヘルパー</strong>。LLM はテキストの要約、テキストからの洞察取得、履歴書などの文章生成が得意です。
- <strong>コードアシスタント</strong>。使用する言語モデルによっては、コードを書くのを支援するコードアシスタントを作れます。例として GitHub Copilot や ChatGPTがコード作成を支援します。

## どうやって始める？

通常は LLM と統合する方法を見つける必要があり、通常以下の二つのアプローチがあります：

- API を使う。ここではプロンプトを含むウェブリクエストを作成し、生成されたテキストを受け取ります。
- ライブラリを使う。ライブラリは API 呼び出しをカプセル化して使いやすくします。

## ライブラリ/SDK

LLM によく使われる有名なライブラリには以下があります：

- **openai**。モデルとの接続やプロンプト送信を簡単に行えます。

より高レベルで動作するライブラリもあります：

- **Langchain**。Langchain は有名で Python をサポートしています。
- **Semantic Kernel**。Semantic Kernel は Microsoft のライブラリで C#, Python, Java をサポートしています。

## openai を使った最初のアプリ

最初のアプリの作り方、必要なライブラリ、どのくらい必要かなど見ていきましょう。

### openai のインストール

OpenAI または Azure OpenAI とやり取りするためのライブラリは数多くあります。使用可能な言語も C#, Python, JavaScript, Java など多数あります。ここでは `openai` Python ライブラリを使い、`pip`でインストールします。

```bash
pip install openai
```

### リソースの作成

以下の手順を実行してください：

- Azure でアカウントを作成する [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- Azure OpenAI へのアクセス許可を得る。[https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) にアクセスし、アクセス申請を行う。

  > [!NOTE]
  > 執筆時点では、Azure OpenAI へのアクセス申請が必要です。

- Python をインストールする <https://www.python.org/>
- Azure OpenAI サービスリソースを作成済みであること。[リソースの作成方法](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)を参照してください。

### API キーとエンドポイントの確認

ここで、`openai` ライブラリに使う API キーを設定する必要があります。API キーは Azure OpenAI リソースの「キーとエンドポイント」セクションの「キー1」の値をコピーしてください。

![Azure ポータルのキーとエンドポイントリソースブレード](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

この情報をコピーしたら、ライブラリに使用させましょう。

> [!NOTE]
> API キーはコードから分離することをお勧めします。環境変数を使うと良いです。
>
> - 環境変数 `OPENAI_API_KEY` に API キーを設定する。
>   `export OPENAI_API_KEY='sk-...'`

### Azure の設定方法

Azure OpenAI（Microsoft Foundry の一部）を使う場合の設定方法です。標準の `OpenAI` クライアントを使い、Azure OpenAI の `/openai/v1/` エンドポイントを指します。これは Responses API と連携し、`api_version` は不要です：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上記で設定しているのは：

- `api_key` は Azure ポータルまたは Microsoft Foundry ポータルで見つかる API キーです。
- `base_url` は Foundry リソースのエンドポイントで、末尾に `/openai/v1/` を付けたものです。安定した v1 エンドポイントは OpenAI と Azure OpenAI の両方で `api_version` 管理不要で動作します。

> [!NOTE] > `os.environ` は環境変数を読み込みます。`AZURE_OPENAI_API_KEY` や `AZURE_OPENAI_ENDPOINT` のような環境変数を読むのに使えます。環境変数はターミナルで設定するか、`dotenv` のようなライブラリで設定してください。

## テキスト生成

テキスト生成は Responses API の `responses.create` メソッド経由で行います。例を示します：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # これはあなたのモデル展開名です
    input=prompt,
    store=False,
)
print(response.output_text)
```

上のコードでは、応答を作成し、使用モデルとプロンプトを渡します。そして `response.output_text` で生成されたテキストを表示します。

### 複数ターン会話

Responses API は単一ターンのテキスト生成にも複数ターンのチャットボットにも適しています。会話を積み上げるために `input` にメッセージのリストを渡します：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

この機能については次章で詳しく扱います。

## 演習 - あなたの最初のテキスト生成アプリ

openai の設定方法を学んだので、最初のテキスト生成アプリを構築しましょう。以下の手順に従ってください：

1. 仮想環境を作成し openai をインストールする：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows 環境の場合は `source venv/bin/activate` の代わりに `venv\Scripts\activate` を入力してください。

   > [!NOTE]
   > Azure OpenAI のキーは [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) で「Open AI」を検索し、「Open AI リソース」を選択、次に「キーとエンドポイント」から「キー1」をコピーしてください。

1. _app.py_ ファイルを作成し、以下のコードを記述する：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 完了コードを追加してください
   prompt = "Complete the following: Once upon a time there was a"

   # Responses APIを使用してリクエストを作成します
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 応答を出力します
   print(response.output_text)
   ```

   > [!NOTE]
   > 純粋な OpenAI（Azure ではなく）を使う場合は `client = OpenAI(api_key="<replace this value with your OpenAI key>")`（`base_url` は使わない）を使い、モデル名には `gpt-5-mini` のようなモデル名を渡してください（デプロイ名ではなく）。

   以下のような出力が表示されるはずです：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 用途に応じた異なるタイプのプロンプト

今、プロンプトを使ったテキスト生成の方法がわかりました。プログラムも動いており、変更してさまざまなテキストを生成できます。

プロンプトはさまざまなタスクに使えます。例えば：

- <strong>特定のタイプのテキスト生成</strong>。例えば、詩やクイズの問題を生成など。
- <strong>情報検索</strong>。プロンプトを使って「Web開発における CORS とは？」のような情報を探せます。
- <strong>コード生成</strong>。プロンプトでコードを生成でき、例としてメール検証用の正規表現を作ったり、ウェブアプリのようなプログラム全体を生成したりもできます。

## 実用的な例：レシピジェネレーター

家にある材料を使って料理をしたいとします。そのためにレシピが必要です。レシピを探すには検索エンジンを使うか、LLM を使うこともできます。

以下のようなプロンプトを書けます：

> "鶏肉、ジャガイモ、ニンジンを材料にした料理のレシピを5つ見せてください。各レシピごとに使われている材料を一覧にしてください"

このプロンプトで、次のような回答が得られるかもしれません：

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

この結果は素晴らしいです。何を作るか分かりました。この時点で役立つ改善案は：

- 嫌いな材料やアレルギーの材料を除外すること。
- 家にない材料があれば買い物リストを生成すること。

これらの場合、追加のプロンプトを加えましょう：

> "ニンニクはアレルギーなので含まれるレシピは除外し、代わりの材料を入れてください。また、鶏肉、ジャガイモ、ニンジンは家にあるので、この材料を考慮した買い物リストも作成してください。"

新しい結果は以下の通りです：

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

これが5つのレシピで、ニンニクを含まず、家にある材料を考慮した買い物リストも含まれています。

## 演習 - レシピジェネレーターの作成

シナリオを体験したので、それに合うコードを書いてみましょう。以下の手順に従ってください：

1. 既存の _app.py_ ファイルを出発点として使います
1. `prompt` 変数を見つけて、次のコードに書き換えます：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   今コードを実行すると以下のような出力が見られます：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意、LLM は非決定的なので、実行するたびに異なる結果になる場合があります。

   よし、改善方法を見ていきましょう。改善のためにコードの柔軟性を持たせ、材料やレシピ数を変更できるようにしたいです。

1. 次のようにコードを変更しましょう：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # プロンプトと材料にレシピの数を補間する
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   テスト実行用コードは次のようになります：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### フィルターと買い物リストを追加して改善

これでレシピを作れる実用的なアプリになりました。ユーザーの入力でレシピ数や材料を柔軟に変えられます。

さらに改善するためには、以下を加えたいです：

- <strong>材料のフィルタリング</strong>。嫌いな材料やアレルギーの材料を除外できるようにしたいです。そのためには、既存のプロンプトにフィルター条件を加えます：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上のコードでは、プロンプトの末尾に `{filter}` を追加し、ユーザーからのフィルター値も受け取ります。

  プログラムの実行時の入力例は以下のようになります：

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  ご覧の通り、牛乳を含むレシピはフィルタリングされています。ただし乳糖不耐症の場合はチーズも除去したいかもしれませんので、詳細な指定が必要です。


- <strong>買い物リストを作成する</strong>。家にすでにあるものを考慮しながら、買い物リストを作成したいと思います。

  この機能を実現するために、すべてを1つのプロンプトで解決する方法と、2つのプロンプトに分ける方法があります。後者の方法を試してみましょう。ここでは追加のプロンプトを加えることを提案していますが、それを実現するには前のプロンプトの結果を後のプロンプトのコンテキストとして追加する必要があります。

  最初のプロンプトの結果を表示しているコードの部分を見つけ、以下のコードをその下に追加してください：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # レスポンスを出力する
  print("Shopping list:")
  print(response.output_text)
  ```

  次の点に注意してください：

  1. 最初のプロンプトの結果を新しいプロンプトに追加して新しいプロンプトを作成しています：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 新しいリクエストを作成しますが、最初のプロンプトで指定したトークン数も考慮して、今回は`max_output_tokens`を1200に設定しています。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     このコードを実行すると、次のような出力が得られます：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## セットアップの改善

これまでのコードは動作しますが、さらに改善すべきいくつかの調整があります。やるべきことは以下の通りです：

- <strong>コードからシークレットを分離する</strong>。APIキーなどのシークレットはコードに含めるべきではなく、安全な場所に保管する必要があります。コードからシークレットを分離するには、環境変数を使用し、`python-dotenv`のようなライブラリでファイルから読み込む方法があります。コード上での例は以下の通りです：

  1. 以下の内容で `.env` ファイルを作成します：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意：Microsoft Foundry の Azure OpenAI を使用する場合は、代わりに以下の環境変数を設定する必要があります：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     コード内で環境変数を読み込むには、次のようにします：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>トークン長についての注意</strong>。生成するテキストに必要なトークン数を考慮する必要があります。トークンはコストがかかるため、可能な限りトークン数を節約するようにしましょう。例えば、プロンプトの表現を工夫してトークンを減らせるか検討してください。

  トークンの使用量を変更するには、`max_output_tokens` パラメーターを使います。例えば、100トークンを使いたい場合は次のようにします：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **温度（temperature）の実験**。温度はこれまで触れていませんでしたが、プログラムの振る舞いに重要な影響を与えます。温度の値が高いほど出力がランダムになり、低いほど予測可能になります。出力にバリエーションを持たせたいかどうかで設定を考えてください。

  温度を変更するには、`temperature` パラメーターを使います。例えば、0.5の温度にしたい場合は以下のようにします：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意：1.0に近いほど出力が多様になります。

- **推論モデルは`temperature`を使いません<strong>。これは2026年の重要な変化です。現在Microsoft Foundryの非非推奨モデルは</strong>推論モデル**（GPT-5ファミリー、o-series）であり、`temperature`や`top_p`（および`max_tokens`；代わりに`max_output_tokens`を使用）は<strong>サポートしていません</strong>。`gpt-5-mini`に`temperature`を送ると「パラメーターがサポートされていない」エラーになります。上記の温度の例を試すには、サンプリング制御をまだサポートするモデル（例えば[Microsoft Foundryモデルカタログ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)の`Llama-3.3-70B-Instruct`のようなオープンなLlamaモデル）を使い、Foundry Models / Azure AI Inferenceエンドポイント経由で呼び出してください（`githubmodels-*`サンプルと同様の方法）。GPT-5のような推論モデルの制御方法は異なります：
  - <strong>プロンプトエンジニアリング</strong> - 明確な指示、例、構造化された出力（レッスン[04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)参照）がサンプリングパラメーターの役割を担います。
  - <strong>推論コントロール</strong> - 推論努力量や冗長度などのパラメーターが、推論の深さとレイテンシおよびコストを調節します。

  要約すると：`temperature`/`top_p`は多くのモデル（Llama、Mistral、Phi、GPT-4.xファミリー- GPT-4.xは廃止傾向）でまだ有効ですが、推論モデルの方向性はプロンプトエンジニアリングと推論コントロールに移っています。

## 課題

この課題では、作成するものを自由に選択してください。

以下はいくつかの提案です：

- レシピジェネレーターアプリをさらに改善するために温度値やプロンプトをいじってみましょう。
- 「スタディバディ」を作成しましょう。例えばPythonに関するトピックについて質問に答えられるアプリで、「Pythonのあるトピックとは？」や「あるトピックのコードを見せて」といったプロンプトが考えられます。
- 歴史ボットを作り、歴史上の人物を演じさせ、その人物の人生や時代について質問できるようにしましょう。

## 解決例

### スタディバディ

以下はスタータープロンプトです。使い方を試して好みに合わせて調整してください。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歴史ボット

使えるプロンプト例は以下の通りです：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識チェック

温度の概念は何をするものですか？

1. 出力のランダムさを制御する。
1. 応答の大きさを制御する。
1. 使われるトークン数を制御する。

## 🚀 チャレンジ

課題に取り組む際は、温度を変えてみてください。0、0.5、1に設定してみましょう。0は最も変動が少なく、1は最も多様です。どの値があなたのアプリに最適か試してみてください。

## よくできました！ 続けて学びましょう

このレッスンを終えた後は、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、ジェネレーティブAIの知識をさらにレベルアップしましょう！

レッスン7に進んで、[チャットアプリケーションの作り方](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)を学びましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->