<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T10:03:54+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ja"
}
-->
# テキスト生成アプリケーションの構築

[![テキスト生成アプリケーションの構築](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.ja.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(上の画像をクリックして、このレッスンのビデオを視聴してください)_

これまでのカリキュラムで、プロンプトなどの基本概念や「プロンプトエンジニアリング」という分野があることを学びました。ChatGPT、Office 365、Microsoft Power Platform など、プロンプトを使用して何かを達成することをサポートするツールと対話できます。

アプリにそのような体験を追加するには、プロンプト、完了、そして使用するライブラリを選択するなどの概念を理解する必要があります。この章ではまさにそれを学びます。

## はじめに

この章では次のことを学びます:

- openai ライブラリとその基本概念について学ぶ。
- openai を使用してテキスト生成アプリを構築する。
- プロンプト、温度、トークンなどの概念を使用してテキスト生成アプリを構築する方法を理解する。

## 学習目標

このレッスンの終わりには、次のことができるようになります:

- テキスト生成アプリとは何かを説明する。
- openai を使用してテキスト生成アプリを構築する。
- トークンの使用量を調整したり、温度を変更して多様な出力を得るためにアプリを設定する。

## テキスト生成アプリとは？

通常、アプリを構築すると、次のようなインターフェースが備わっています:

- コマンドベース。コンソールアプリは典型的なもので、コマンドを入力してタスクを実行します。例えば、`git` はコマンドベースのアプリです。
- ユーザーインターフェース (UI)。いくつかのアプリはグラフィカルユーザーインターフェース (GUI) を持ち、ボタンをクリックしたり、テキストを入力したり、オプションを選択したりします。

### コンソールと UI アプリの制限

コマンドベースのアプリと比較して:

- **制限がある**。任意のコマンドを入力できるわけではなく、アプリがサポートするコマンドだけです。
- **言語特有**。一部のアプリは多くの言語をサポートしていますが、デフォルトでは特定の言語向けに構築されています。

### テキスト生成アプリの利点

では、テキスト生成アプリはどのように異なるのでしょうか？

テキスト生成アプリでは、より柔軟で、特定のコマンドや入力言語に限定されません。代わりに、自然言語を使ってアプリと対話できます。さらに、既に膨大な情報を持つデータソースと対話しているため、従来のアプリがデータベース内の情報に制限されているのに対し、より多くの情報にアクセスできます。

### テキスト生成アプリで何が作れる？

作れるものはたくさんあります。例えば:

- **チャットボット**。会社や製品についての質問に答えるチャットボットは良い選択肢かもしれません。
- **ヘルパー**。LLM はテキストの要約や洞察を得ること、履歴書のようなテキストを生成することなどに優れています。
- **コードアシスタント**。使用する言語モデルに応じて、コード作成を支援するコードアシスタントを構築できます。例えば、GitHub Copilot や ChatGPT を使用してコードを書く手助けをすることができます。

## どのように始める？

LLM と統合する方法を見つける必要があります。通常、次の2つのアプローチがあります:

- API を使用する。ここでは、プロンプトを含むウェブリクエストを構築し、生成されたテキストを取得します。
- ライブラリを使用する。ライブラリは API コールをカプセル化し、使用を容易にします。

## ライブラリ/SDK

LLM を操作するためのよく知られたライブラリがいくつかあります:

- **openai**。このライブラリは、モデルに接続してプロンプトを送信するのを容易にします。

さらに、より高レベルで操作するライブラリもあります:

- **Langchain**。Langchain はよく知られており、Python をサポートしています。
- **Semantic Kernel**。Semantic Kernel は、C#、Python、Java をサポートする Microsoft のライブラリです。

## openai を使用した最初のアプリ

最初のアプリをどのように構築するか、必要なライブラリ、必要なものなどを見てみましょう。

### openai のインストール

OpenAI や Azure OpenAI と対話するための多くのライブラリがあります。C#、Python、JavaScript、Java などのプログラミング言語を使用することが可能です。今回は `openai` Python ライブラリを選択し、`pip` を使用してインストールします。

```bash
pip install openai
```

### リソースの作成

次のステップを実行する必要があります:

- Azure でアカウントを作成します [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- Azure OpenAI へのアクセスを取得します。 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) にアクセスし、アクセスをリクエストします。

  > [!NOTE]
  > 記述時点では、Azure OpenAI へのアクセスを申請する必要があります。

- Python をインストールします <https://www.python.org/>
- Azure OpenAI サービスリソースを作成します。リソースの作成方法については、このガイドを参照してください [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### API キーとエンドポイントの場所

この時点で、`openai` ライブラリに使用する API キーを指定する必要があります。API キーを見つけるには、Azure OpenAI リソースの「キーとエンドポイント」セクションに移動し、「キー 1」の値をコピーします。

![Azure ポータルのキーとエンドポイントリソースブレード](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

この情報をコピーしたら、ライブラリに使用するように指示します。

> [!NOTE]
> API キーをコードから分離する価値があります。環境変数を使用することでこれを行うことができます。
>
> - 環境変数 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'` を設定します。

### Azure の設定

Azure OpenAI を使用している場合、設定方法は次の通りです:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上記では次のことを設定しています:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` クラス。例を示します:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

上記のコードでは、使用するモデルとプロンプトを渡して完了オブジェクトを作成し、生成されたテキストを出力します。

### チャット完了

これまで、`Completion` to generate text. But there's another class called `ChatCompletion` を使用してきたことがわかりますが、これはチャットボットにより適しています。以下にその使用例を示します:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

この機能については次の章で詳しく説明します。

## 演習 - 最初のテキスト生成アプリ

openai のセットアップと構成方法を学んだので、最初のテキスト生成アプリを構築する時が来ました。アプリを構築するには、次の手順に従います:

1. 仮想環境を作成し、openai をインストールします:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows を使用している場合は、`venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` の値を入力します。

1. _app.py_ ファイルを作成し、次のコードを入力します:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Azure OpenAI を使用している場合は、`api_type` to `azure` and set the `api_key` を Azure OpenAI キーに設定する必要があります。

   次のような出力が表示されます:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## さまざまな目的に応じた異なるタイプのプロンプト

プロンプトを使用してテキストを生成する方法を見てきました。異なる種類のテキストを生成するために変更できるプログラムも動作しています。

プロンプトはさまざまなタスクに使用できます。例えば:

- **特定の種類のテキストを生成する**。例えば、詩やクイズの質問を生成することができます。
- **情報を検索する**。プロンプトを使用して情報を検索することができます。例えば、「Web 開発における CORS とは何か？」のような例です。
- **コードを生成する**。プロンプトを使用してコードを生成することができます。例えば、メールを検証するための正規表現を開発したり、Web アプリのようなプログラム全体を生成したりすることができます。

## より実用的なユースケース: レシピジェネレーター

自宅にある材料を使って何かを料理したいと考えたとします。そのためにはレシピが必要です。レシピを見つける方法としては、検索エンジンを使うか、LLM を使うことができます。

次のようなプロンプトを書くことができます:

> 「鶏肉、ジャガイモ、ニンジンを使った料理のレシピを5つ見せてください。各レシピで使用するすべての材料をリストアップしてください」

上記のプロンプトに対して、次のような応答が得られるかもしれません:

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

この結果は素晴らしいです。何を料理するかがわかります。この時点で役立つ改善点は次の通りです:

- 嫌いな材料やアレルギーのある材料を除外する。
- 家にない材料のための買い物リストを作成する。

上記のケースでは、追加のプロンプトを追加します:

> 「ニンニクがアレルギーなので、ニンニクを使ったレシピを削除し、代わりに他のものを使ってください。また、家にすでに鶏肉、ジャガイモ、ニンジンがあることを考慮して、レシピのための買い物リストを作成してください。」

新しい結果が得られます:

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

これで5つのレシピがニンニクを含まず、家にあるものを考慮した買い物リストもあります。

## 演習 - レシピジェネレーターを構築する

シナリオを実行したので、デモンストレーションされたシナリオに一致するコードを書いてみましょう。次の手順に従います:

1. 既存の _app.py_ ファイルを開始点として使用します
1. `prompt` 変数を見つけて、そのコードを次のように変更します:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   コードを実行すると、次のような出力が表示されるはずです:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE、あなたの LLM は非決定的であるため、プログラムを実行するたびに異なる結果が得られるかもしれません。

   素晴らしい、改善方法を見てみましょう。改善するためには、コードが柔軟であることを確認し、材料やレシピの数を改善および変更できるようにしたいです。

1. コードを次のように変更します:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   コードをテスト実行すると、次のような結果になります:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### フィルタと買い物リストを追加して改善する

現在、レシピを生成できる動作するアプリがありますが、ユーザーからの入力に依存しているため、レシピの数や使用する材料も柔軟です。

さらに改善するために、次のことを追加したいです:

- **材料をフィルタリングする**。好きでない材料やアレルギーのある材料をフィルタリングできるようにしたいです。この変更を行うために、既存のプロンプトを編集し、次のようにフィルタ条件を追加します:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上記では、プロンプトの最後に `{filter}` を追加し、ユーザーからフィルタ値を取得しています。

  プログラムを実行したときの入力例は次のようになります:

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

  ご覧の通り、ミルクを含むレシピはフィルタリングされています。しかし、乳糖不耐症の方は、チーズを含むレシピもフィルタリングしたいかもしれませんので、明確にする必要があります。

- **買い物リストを作成する**。すでに家にあるものを考慮して買い物リストを作成したいです。

  この機能のために、すべてを1つのプロンプトで解決しようとすることもできますが、2つのプロンプトに分けることもできます。後者のアプローチを試してみましょう。ここでは、追加のプロンプトを提案していますが、それが機能するためには、最初のプロンプトの結果を後者のプロンプトにコンテキストとして追加する必要があります。

  最初のプロンプトの結果を出力するコード部分を見つけ、その下に次のコードを追加します:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  次の点に注意してください:

  1. 新しいプロンプトを作成し、最初のプロンプトの結果を新しいプロンプトに追加しています:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 新しいリクエストを行いますが、最初のプロンプトで要求したトークン数を考慮し、この時点で `max_tokens` を 1200 に設定します。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     このコードを実行すると、次のような出力が得られます:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## セットアップを改善する

これまでのところ、動作するコードがありますが、さらに改善するためにいくつかの調整を行うべきです。改善するべきことのいくつかは次の通りです:

- **コードから秘密情報を分離する**。API キーのような秘密情報はコードに含めるべきではなく、安全な場所に保存するべきです。コードから秘密情報を分離するために、環境変数や `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` ファイルを使用できます。次の内容を含めます:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意、Azure の場合、次の環境変数を設定する必要があります:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     コードでは、次のように環境変数をロードします:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **トークンの長さについての一言**。生成したいテキストに必要なトークン数を考慮するべきです。トークンはコストがかかるため、可能な限り、使用するトークン数を節約するようにするべきです。例えば、プロンプトをどのように表現すればトークンを少なくできるかを考えることができます。

  使用するトークンを変更するには、`max_tokens` パラメータを使用します

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文の言語での文書が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用によって生じた誤解や誤解釈について、当社は責任を負いません。