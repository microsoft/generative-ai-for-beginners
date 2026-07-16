# テキスト生成アプリケーションの構築

[![テキスト生成アプリケーションの構築](../../../translated_images/ja/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(上の画像をクリックすると、このレッスンのビデオを視聴できます)_

これまでのカリキュラムで、プロンプトのようなコアコンセプトや、「プロンプトエンジニアリング」と呼ばれる分野があることを見てきました。ChatGPT、Office 365、Microsoft Power Platform など、多くのツールは、何かを達成するためにプロンプトを利用することをサポートしています。

そのような体験をアプリに追加するには、プロンプトやコンプリーションの概念を理解し、使うライブラリを選ぶ必要があります。まさにこの章で学ぶことです。

## はじめに

この章では以下を行います：

- openaiライブラリとそのコアコンセプトを学習します。
- openaiを使ってテキスト生成アプリを構築します。
- プロンプト、temperature、tokensなどの概念を使ったテキスト生成アプリの構築方法を理解します。

## 学習目標

このレッスンの最後には、以下ができるようになります：

- テキスト生成アプリとは何か説明できる。
- openaiを使ってテキスト生成アプリを構築できる。
- トークン数を多くしたり少なくしたり、temperatureを変更して出力を変える設定ができる。

## テキスト生成アプリとは？

通常、アプリを構築するときは次のようなインターフェイスを持っていることが多いです：

- コマンドベース。コンソールアプリはコマンドを入力してタスクを実行します。例えば、`git`はコマンドベースのアプリです。
- ユーザーインターフェイス（UI）。GUIを持つアプリではボタンをクリックしたり、テキストを入力したり、オプションを選択したりします。

### コンソールとUIアプリの制限

コマンドベースのアプリと比べてみましょう：

- <strong>制限がある</strong>。サポートされていないコマンドは使えません。
- <strong>言語依存</strong>。多言語対応するアプリもありますが、デフォルトは特定の言語向けに作られています。

### テキスト生成アプリの利点

では、テキスト生成アプリはどう違うのでしょうか？

テキスト生成アプリでは柔軟性が高く、コマンドセットや特定の入力言語に制限されません。代わりに自然言語でアプリと対話できます。さらに、大量の情報コーパスで訓練されたデータソースと既に対話しているため、従来のアプリがデータベース内の情報に限られるのとは違います。

### テキスト生成アプリで何が作れる？

いろいろ作れます。例えば：

- <strong>チャットボット</strong>。会社や製品に関する質問に答えるチャットボットは良い例です。
- <strong>ヘルパー</strong>。大規模言語モデル（LLM）は文章の要約や洞察抽出、履歴書の作成などに優れています。
- <strong>コードアシスタント</strong>。使うモデルによってはコード作成を助けるアシスタントも作れます。例えばGitHub CopilotやChatGPTを使いコードを書けます。

## どうやって始める？

まず、大規模言語モデル（LLM）と連携する方法を見つける必要があります。通常は次の2つのアプローチです：

- APIを使う。プロンプトを含むウェブリクエストを構築し、生成されたテキストを受け取る方法。
- ライブラリを使う。API呼び出しをラップして使いやすくしたもの。

## ライブラリ/SDK

LLMを扱う有名なライブラリには以下があります：

- **openai**。モデル接続やプロンプト送信が簡単にできます。

さらに高レベルなライブラリもあります：

- **Langchain**。Pythonをサポートし、よく使われています。
- **Semantic Kernel**。Microsoft製ライブラリで、C#、Python、Javaをサポートします。

## openaiを使った最初のアプリ

ここでは、最初のアプリの作り方、必要なライブラリ、準備の量などを見ていきます。

### openaiのインストール

OpenAIやAzure OpenAIと対話するためのライブラリは多くあります。C#、Python、JavaScript、Javaなど多くのプログラミング言語も利用可能です。ここではPythonの`openai`ライブラリを使うため、`pip`でインストールします。

```bash
pip install openai
```

### リソースの作成

以下のステップを行います：

- Azureのアカウントを作成する：[https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
- Azure OpenAIへのアクセス権を取得する。[https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) でアクセス申請。

  > [!NOTE]
  > 執筆時点では、Azure OpenAIアクセスには申請が必要です。

- Pythonをインストールする <https://www.python.org/>
- Azure OpenAIサービスリソースを作成する。詳しくは[リソースの作成](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)を参照。

### APIキーとエンドポイントの取得

ここで、`openai`ライブラリに使うAPIキーを設定します。Azure OpenAIリソースの「キーとエンドポイント」セクションから「キー 1」の値をコピーします。

![Azureポータルのキーとエンドポイントリソースブレード](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

情報をコピーしたら、ライブラリに使わせる設定に進みましょう。

> [!NOTE]
> APIキーはコードと分離することを推奨します。環境変数を利用してください。
>
> - 環境変数 `OPENAI_API_KEY` にAPIキーを設定します。
>   `export OPENAI_API_KEY='sk-...'`

### Azureの設定

Azure OpenAI（Microsoft Foundryの一部）を使う場合の設定例です。標準の`OpenAI`クライアントにAzure OpenAIの`/openai/v1/`エンドポイントを指定し、Responses APIを使います。`api_version`は不要です。

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上記で次の設定をしています：

- `api_key`：AzureポータルまたはMicrosoft Foundryポータルで見つけたAPIキー。
- `base_url`：Foundryリソースのエンドポイントに`/openai/v1/`を追加したもの。安定版v1エンドポイントでOpenAIとAzure OpenAIの両対応。

> [!NOTE] > `os.environ`で環境変数を読み取ります。`AZURE_OPENAI_API_KEY`や`AZURE_OPENAI_ENDPOINT`をターミナルや`dotenv`のようなライブラリで設定してください。

## テキスト生成

Responses APIの`responses.create`メソッドを使ってテキストを生成します。例：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # これはあなたのモデル展開名です
    input=prompt,
    store=False,
)
print(response.output_text)
```

上記コードでは、レスポンスを作成し、使いたいモデルとプロンプトを渡します。そして`response.output_text`から生成テキストを出力します。

### マルチターン会話

Responses APIはシングルターンのテキスト生成だけでなく、マルチターンのチャットボットにも適しています。`input`にメッセージリストを渡して会話を構築します：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

この機能については次章で詳しく解説します。

## 演習 - 初めてのテキスト生成アプリ

openaiの設定方法と構成がわかったので、最初のテキスト生成アプリを作りましょう。手順は次の通りです：

1. 仮想環境を作りopenaiをインストールします：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windowsの場合は`source venv/bin/activate`ではなく`venv\Scripts\activate`を使います。

   > [!NOTE]
   > Azure OpenAIキーは[https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)で`Open AI`を検索し、`Open AI resource`を選んで「キーとエンドポイント」から`キー 1`をコピーしてください。

1. _app.py_ ファイルを作り以下のコードを記述します：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 完了コードを追加する
   prompt = "Complete the following: Once upon a time there was a"

   # Responses APIを使ってリクエストを行う
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # レスポンスを表示する
   print(response.output_text)
   ```

   > [!NOTE]
   > Azure版でない通常のOpenAIを使う場合は、`client = OpenAI(api_key="<replace this value with your OpenAI key>")`（`base_url`なし）を使い、デプロイメント名ではなく`gpt-4o-mini`のようなモデル名を渡してください。

   以下のような出力が得られるはずです：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## さまざまなタイプのプロンプト、さまざまな目的

プロンプトを使ったテキスト生成方法がわかりました。プログラムも動いていますので、さまざまなテキストを生成するために修正できます。

プロンプトは多様なタスクに利用できます。例えば：

- <strong>特定タイプのテキストを作る</strong>。詩やクイズの問題などを生成可能です。
- <strong>情報を調べる</strong>。例えば「Web開発におけるCORSとは？」のような質問に使えます。
- <strong>コードを生成する</strong>。正規表現の作成やWebアプリのようなプログラム全体を生成するのにも使えます。

## より実用的な例：レシピジェネレーター

家にある材料で料理したいとします。そのためにレシピが必要です。レシピを見つけるには検索エンジンを使うか、大規模言語モデル（LLM）を使う方法があります。

次のようなプロンプトを書くことができます：

> 「鶏肉、じゃがいも、人参を使った料理のレシピを5つ見せてください。各レシピで使用する材料をすべてリストしてください」

上のプロンプトに対して、次のような回答が得られるかもしれません：

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

この結果は素晴らしいです。次に何を作るかが分かりました。ここで改善できる点は：

- 苦手な材料やアレルギーのある材料をフィルタリングすること。
- 材料が足りない場合の買い物リストを作成すること。

そこで次の追加プロンプトを加えます：

> 「ニンニクはアレルギーがあるので除外し、代わりに他のものを使ってください。また、鶏肉、じゃがいも、人参は家にあるので、それを考慮した買い物リストも作成してください。」

すると新しい結果が得られます：

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

ニンニクを使わない5つのレシピが出てきて、家にある材料も考慮した買い物リストも一緒になっています。

## 演習 - レシピジェネレーターを作ろう

シナリオがわかったので、それに合わせたコードを書きましょう。手順は次の通りです：

1. 既存の_app.py_ファイルをベースにします。
1. `prompt`変数を探し、コードを以下のように変更します：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   もしこのコードを実行すれば、概ね次のような出力が得られます：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 補足：LLMは非決定論的（ノンデターミニスティック）なので、実行のたびに結果が異なる場合があります。

   素晴らしいです。次に改善するには、コードを柔軟にして材料やレシピ数を変えられるようにしましょう。

1. 次のようにコードを変更します：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # プロンプトと材料にレシピの数を補間する
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   テスト実行コードは以下のようになります：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### フィルターと買い物リストを追加して改善

これでユーザーが入力した材料やレシピ数に応じてレシピを作れる柔軟なアプリができました。

さらに改善するために、以下を加えたいです：

- <strong>材料のフィルタリング</strong>。嫌いな材料やアレルギーのある材料を取り除けるようにします。既存のプロンプトにフィルター条件を追加してこう書きます：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上記ではプロンプトの最後に`{filter}`を追加し、ユーザーからフィルター条件も受け取っています。

  プログラムを実行すると、入力例は次のようになります：

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

  このように、牛乳を使ったレシピは除外されました。ただし乳糖不耐症の方はチーズを使ったレシピも除外したいかもしれませんので、明確に指定する必要があります。


- <strong>買い物リストを作成する</strong>。家に既にあるものを考慮して買い物リストを作成したいと思います。

  この機能のために、すべてを1つのプロンプトで解決するか、2つのプロンプトに分割するかのどちらかを試すことができます。後者のアプローチを試してみましょう。ここでは追加のプロンプトを追加することを提案していますが、それが機能するためには、前のプロンプトの結果を後のプロンプトのコンテキストとして追加する必要があります。

  最初のプロンプトの結果を出力しているコード部分を見つけて、以下のコードをその下に追加してください。

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

  1. 最初のプロンプトの結果を新しいプロンプトに追加して、新しいプロンプトを構築しています：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 新しいリクエストを作成しますが、最初のプロンプトで要求したトークン数も考慮し、今回は `max_output_tokens` を1200に設定しています。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     このコードを実行すると、次の出力が得られます：

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

今のところ動作するコードはありますが、改善のためにいくつかの調整を行うべきです。行うべきことは次の通りです：

- <strong>秘密情報をコードから分離する</strong>。APIキーのような秘密情報はコードに含めるべきではなく、安全な場所に保管するべきです。秘密情報をコードから分離するには、環境変数を使い、`python-dotenv` のようなライブラリを使用してファイルから読み込む方法があります。コード例は以下の通りです：

  1. 以下の内容で `.env` ファイルを作成します：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意：Microsoft Foundry の Azure OpenAI では、代わりに次の環境変数を設定する必要があります：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     コード内で環境変数を次のように読み込みます：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>トークンの長さについて</strong>。生成したいテキストに必要なトークン数を考慮すべきです。トークンはコストがかかるため、可能な限り使用トークン数を節約することが望ましいです。例えば、プロンプトはより少ないトークンで済むように工夫できますか？

  使用するトークン数を変えるには、`max_output_tokens` パラメーターを使います。例えば、100トークン使用したい場合は、次のようにします：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- <strong>温度パラメータの実験</strong>。温度はこれまで触れていませんでしたが、プログラムの動作において重要なコンテキストです。温度の値が高いほど出力はよりランダムになり、逆に低いほど予測可能になります。出力のバリエーションが欲しいかどうかを考慮してください。

  温度を変更するには、`temperature` パラメーターを使います。例えば、温度0.5を使用したい場合は次のようにします：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意：1.0に近いほど、出力が多様になります。

## 課題

この課題では、何を作るか自由に選べます。

次のような提案があります：

- レシピ生成アプリをさらに改良しましょう。温度値やプロンプトを試して、どんな結果が出るか試してみてください。
- 「勉強仲間」アプリを作成しましょう。このアプリは Python のようなトピックについて質問に答えられるもので、例えば「Pythonのあるトピックって何？」や「あるトピックのコードを見せて」などのプロンプトを使えます。
- 歴史ボット、特定の歴史上の人物を演じさせ、その人の人生や時代について質問することができます。

## 解答例

### 勉強仲間

以下はスタータープロンプトです。どう使い、調整するか考えてみてください。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歴史ボット

使えるプロンプトの例はこちらです：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識チェック

温度の概念は何を制御しますか？

1. 出力がどれだけランダムかを制御する。
1. 応答の大きさを制御する。
1. 使用するトークン数を制御する。

## 🚀 チャレンジ

課題に取り組む際には、温度を変えて試してみてください。0、0.5、1 などに設定してみましょう。0は最も幅が狭く、1が最も多様な出力になります。あなたのアプリに最適な値は何でしょうか？

## お疲れ様でした！学習を続けましょう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をチェックして、生成AIの知識をさらにレベルアップさせましょう！

次はレッスン7で、[チャットアプリケーションの作り方](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) を学びます！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->