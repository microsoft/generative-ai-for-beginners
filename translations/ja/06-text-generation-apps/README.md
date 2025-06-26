<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:08:07+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ja"
}
-->
# テキスト生成アプリケーションの構築

> _(このレッスンのビデオを見るには、上の画像をクリックしてください)_

これまでのカリキュラムを通じて、プロンプトなどの基本概念や「プロンプトエンジニアリング」と呼ばれる分野があることを学びました。ChatGPT、Office 365、Microsoft Power Platformなどの多くのツールでは、プロンプトを使用して何かを達成することがサポートされています。

アプリにそのような体験を追加するためには、プロンプトやコンプリートといった概念を理解し、使用するライブラリを選択する必要があります。この章ではまさにそのことを学びます。

## はじめに

この章では以下を学びます:

- openaiライブラリとその基本概念について学ぶ
- openaiを使ってテキスト生成アプリを構築する
- プロンプト、温度、トークンなどの概念を使ってテキスト生成アプリを構築する方法を理解する

## 学習目標

このレッスンの終わりには、次のことができるようになります:

- テキスト生成アプリとは何かを説明する
- openaiを使ってテキスト生成アプリを構築する
- トークンを多く使ったり少なく使ったりするようにアプリを設定し、温度を変更して多様な出力を得る

## テキスト生成アプリとは？

通常、アプリを構築する際には以下のようなインターフェースがあります:

- コマンドベース。コンソールアプリは、コマンドを入力するとタスクを実行する典型的なアプリです。例えば、`git`はコマンドベースのアプリです。
- ユーザーインターフェース（UI）。一部のアプリは、ボタンをクリックしたり、テキストを入力したり、オプションを選択したりするグラフィカルユーザーインターフェース（GUI）を持っています。

### コンソールとUIアプリの制限

コマンドベースのアプリと比較してみましょう:

- **制限されている**。アプリがサポートしているコマンドだけを入力できます。
- **言語に依存している**。一部のアプリは多くの言語をサポートしていますが、デフォルトでは特定の言語用に構築されています。

### テキスト生成アプリの利点

では、テキスト生成アプリはどのように異なるのでしょうか？

テキスト生成アプリでは、より柔軟性があり、特定のコマンドや入力言語に制限されません。代わりに、自然言語を使ってアプリと対話することができます。もう一つの利点は、膨大な情報を学習したデータソースと既に対話しているため、従来のアプリがデータベースにある情報に制限されるのに対して、より広範な情報にアクセスできることです。

### テキスト生成アプリで何が作れるの？

作れるものはたくさんあります。例えば:

- **チャットボット**。会社やその製品についての質問に答えるチャットボットは良い例です。
- **ヘルパー**。LLMはテキストの要約、テキストからの洞察の抽出、履歴書の作成などに優れています。
- **コードアシスタント**。使用する言語モデルによっては、コードを書くのを助けるコードアシスタントを構築することができます。例えば、GitHub CopilotやChatGPTを使ってコードを書くのを手伝ってもらうことができます。

## どうやって始めればいいの？

まず、LLMと統合する方法を見つける必要があります。通常、以下の2つのアプローチがあります:

- APIを使用する。ここでは、プロンプトを使ってウェブリクエストを構築し、生成されたテキストを取得します。
- ライブラリを使用する。ライブラリはAPI呼び出しをカプセル化し、使用を容易にします。

## ライブラリ/SDK

LLMと連携するための有名なライブラリはいくつかあります:

- **openai**、このライブラリはモデルに接続し、プロンプトを送信するのを容易にします。

次に、高レベルで動作するライブラリがあります:

- **Langchain**。LangchainはPythonをサポートしています。
- **Semantic Kernel**。Semantic KernelはMicrosoftによって提供されており、C#、Python、Javaをサポートしています。

## 初めてのopenaiアプリ

最初のアプリをどのように構築するか、必要なライブラリ、必要なものなどを見てみましょう。

### openaiのインストール

OpenAIまたはAzure OpenAIと対話するためのライブラリはたくさんあります。C#、Python、JavaScript、Javaなど、さまざまなプログラミング言語を使用することが可能です。ここでは`openai` Pythonライブラリを選択し、`pip`を使ってインストールします。

```bash
pip install openai
```

### リソースの作成

以下の手順を実行する必要があります:

- Azureでアカウントを作成する [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- Azure OpenAIにアクセスする。 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) にアクセスし、アクセスをリクエストします。

  > [!NOTE]
  > 記述時点では、Azure OpenAIへのアクセスには申請が必要です。

- Pythonをインストールする <https://www.python.org/>
- Azure OpenAIサービスリソースを作成する。 [リソースの作成方法](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) を参照してください。

### APIキーとエンドポイントの特定

この時点で、`openai`ライブラリに使用するAPIキーを指定する必要があります。APIキーを見つけるには、Azure OpenAIリソースの「キーとエンドポイント」セクションに移動し、「キー1」の値をコピーします。

![Azureポータルのキーとエンドポイントリソースブレード](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

この情報をコピーしたら、ライブラリに使用するよう指示します。

> [!NOTE]
> APIキーをコードから分離することは価値があります。環境変数を使用することでこれを行うことができます。
>
> - 環境変数 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'` を設定します。

### Azureの設定

Azure OpenAIを使用している場合、設定方法は以下の通りです:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上記では以下を設定しています:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` クラス。以下は例です:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

上記のコードでは、コンプリートオブジェクトを作成し、使用したいモデルとプロンプトを渡します。そして、生成されたテキストを出力します。

### チャットコンプリート

これまでに、`Completion` to generate text. But there's another class called `ChatCompletion` を使ってきたことを見てきましたが、これはチャットボットにより適しています。以下はその使用例です:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

この機能については次の章で詳しく説明します。

## 演習 - 初めてのテキスト生成アプリ

openaiの設定と構成方法を学んだので、最初のテキスト生成アプリを構築する時が来ました。アプリを構築するには、以下の手順に従います:

1. 仮想環境を作成し、openaiをインストールする:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windowsを使用している場合は、`venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` の値を入力します。

1. _app.py_ ファイルを作成し、以下のコードを入力します:

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
   > Azure OpenAIを使用している場合は、`api_type` to `azure` and set the `api_key` をAzure OpenAIキーに設定する必要があります。

   次のような出力が表示されるはずです:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 様々なプロンプトの種類

プロンプトを使用してテキストを生成する方法を見てきました。異なる種類のテキストを生成するためにプログラムを変更して実行することができます。

プロンプトは様々なタスクに使用できます。例えば:

- **特定の種類のテキストを生成する**。例えば、詩やクイズの質問を生成することができます。
- **情報を検索する**。プロンプトを使用して、ウェブ開発におけるCORSの意味などの情報を探すことができます。
- **コードを生成する**。プロンプトを使用して、メールを検証するための正規表現を開発したり、ウェブアプリのようなプログラム全体を生成したりすることができます。

## より実践的な使用例: レシピジェネレーター

家にある食材を使って何かを料理したいとします。そのためにはレシピが必要です。レシピを見つける方法としては、検索エンジンを使うか、LLMを使うことが考えられます。

以下のようなプロンプトを書くことができます:

> "以下の食材を使った料理のレシピを5つ見せてください: チキン、ジャガイモ、ニンジン。各レシピで使用するすべての食材を列挙してください"

上記のプロンプトに基づいて、次のような応答を得ることができます:

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

この結果は素晴らしいですね。何を料理するかがわかります。この時点で役立つ改善点としては:

- 嫌いな食材やアレルギーのある食材を除外する。
- 家にない食材を考慮して買い物リストを作成する。

上記のケースのために、追加のプロンプトを追加しましょう:

> "ニンニクがアレルギーなので、ニンニクを含むレシピを削除し、代わりに別のものを使用してください。また、家にチキン、ジャガイモ、ニンジンがあることを考慮して、レシピの買い物リストを作成してください。"

これで新しい結果が得られます:

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

これが5つのレシピで、ニンニクが含まれておらず、家にあるものを考慮した買い物リストもあります。

## 演習 - レシピジェネレーターを構築する

シナリオを試したので、示されたシナリオに一致するコードを書いてみましょう。以下の手順に従ってください:

1. 既存の _app.py_ ファイルを出発点として使用します
1. `prompt` 変数を見つけ、そのコードを以下のように変更します:

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

   > NOTE、LLMは非決定的なので、プログラムを実行するたびに異なる結果が得られることがあります。

   素晴らしいですね。どのように改善できるか見てみましょう。改善するためには、コードが柔軟であることを確認したいので、食材やレシピの数を改善し、変更できるようにしたいです。

1. コードを次のように変更しましょう:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   コードをテスト実行すると、次のようになります:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### フィルタと買い物リストを追加して改善する

現在、レシピを生成できるアプリが動作しており、ユーザーからの入力に依存しているため、柔軟性があります。

さらに改善するために、以下を追加したいです:

- **食材をフィルタリングする**。嫌いな食材やアレルギーのある食材を除外できるようにしたいです。この変更を実現するために、既存のプロンプトを編集し、次のようにフィルタ条件を追加します:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上記では、プロンプトの末尾に `{filter}` を追加し、ユーザーからフィルタ値を取得します。

  プログラムを実行した際の入力例は次のようになります:

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

  ご覧の通り、ミルクを含むレシピはすべてフィルタリングされました。しかし、乳糖不耐症の場合、チーズを含むレシピもフィルタリングしたいかもしれませんので、明確にする必要があります。

- **買い物リストを作成する**。家にあるものを考慮して買い物リストを作成したいです。

  この機能のために、すべてを1つのプロンプトで解決するか、2つのプロンプトに分けるかを試みることができます。後者のアプローチを試してみましょう。ここでは追加のプロンプトを提案していますが、それを機能させるためには、前のプロンプトの結果を新しいプロンプトのコンテキストとして追加する必要があります。

  最初のプロンプトの結果を出力する部分を見つけ、その下に以下のコードを追加します:

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

  以下に注意してください:

  1. 最初のプロンプトの結果を新しいプロンプトに追加することで、新しいプロンプトを構築しています:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 最初のプロンプトで要求したトークンの数を考慮し、`max_tokens` を1200に設定して新しいリクエストを行います。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     このコードを試すと、次のような出力が得られます:

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

これまでのところ、コードは動作していますが、さらに改善するための調整がいくつかあります。改善するためにすべきことは次のとおりです:

- **コードから秘密情報を分離する**、例えばAPIキー。秘密情報はコードに含めるべきではなく、安全な場所に保存する必要があります。コードから秘密情報を分離するために、環境変数や `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` ファイルなどのライブラリを使用できます。次の内容を含めます:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意、Azureの場合、以下の環境変数を設定する必要があります:

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

- **トークンの長さについての言及**。生成したいテキストに必要なトークンの数を考慮すべきです。トークンはお金がかかるので、可能な限り使用するトークンの数を節約するようにすべきです。例えば、プロンプトをどのように表現すればトークンを少なくできるかを考えます。

  使用するトークンを変更するには、`max_tokens` パラメータを使用します。例えば、100トークンを使用したい場合、次のようにします:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **温度の実験**。温度はこれまで言及していませんが、プログラムのパフォーマンスに重要な影響を与えるコンテキストです。温度値が高いほど出力はランダムになり、逆に温度値が低いほど出力は予測可能になります。出

**免責事項**:
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。元の言語での原文が権威ある情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じる誤解や誤解については責任を負いません。