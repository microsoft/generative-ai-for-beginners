# テキスト生成アプリケーションの構築

[![テキスト生成アプリケーションの構築](../../../translated_images/06-lesson-banner.png?WT.2cbccad4fdd538d4f7d47c475b058629b7b7fb1a010acde6e323370d82005b16.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(このレッスンのビデオを見るには、上の画像をクリックしてください)_

このカリキュラムを通じて、プロンプトなどの基本概念や「プロンプトエンジニアリング」と呼ばれる専門分野があることを見てきました。ChatGPT、Office 365、Microsoft Power Platformなど、多くのツールはプロンプトを使用して何かを達成することをサポートしています。

このような体験をアプリに追加するためには、プロンプトや完了の概念を理解し、使用するライブラリを選ぶ必要があります。これがこの章で学ぶことです。

## はじめに

この章では、以下を学びます：

- openaiライブラリとその基本概念について学ぶ。
- openaiを使用してテキスト生成アプリを構築する。
- プロンプト、温度、トークンなどの概念を使用してテキスト生成アプリを構築する方法を理解する。

## 学習目標

このレッスンの終わりには、以下ができるようになります：

- テキスト生成アプリが何かを説明する。
- openaiを使用してテキスト生成アプリを構築する。
- アプリを設定してトークンの使用量を増減させ、温度を変えて多様な出力を得る。

## テキスト生成アプリとは？

通常、アプリを構築すると、次のようなインターフェースがあります：

- コマンドベース。コンソールアプリは、コマンドを入力してタスクを実行する典型的なアプリです。例えば、`git`はコマンドベースのアプリです。
- ユーザーインターフェース（UI）。一部のアプリは、ボタンをクリックしたり、テキストを入力したり、オプションを選択したりするグラフィカルユーザーインターフェース（GUI）を持っています。

### コンソールとUIアプリの制限

コマンドを入力するコマンドベースのアプリと比較してみましょう：

- **制限されている**。アプリがサポートするコマンドだけを入力でき、任意のコマンドを入力することはできません。
- **言語特化**。一部のアプリは多くの言語をサポートしていますが、デフォルトでは特定の言語向けに構築されています。

### テキスト生成アプリの利点

では、テキスト生成アプリはどのように異なるのでしょうか？

テキスト生成アプリでは、コマンドや特定の入力言語に制限されることなく、自然言語を使用してアプリと対話することができます。さらに、膨大な情報のコーパスで訓練されたデータソースとすでに対話しているため、伝統的なアプリがデータベースに限定されるのに対し、より多様な情報にアクセスできます。

### テキスト生成アプリで何が作れる？

以下のようなものを構築できます：

- **チャットボット**。会社や製品についての質問に答えるチャットボット。
- **ヘルパー**。テキストの要約、テキストからの洞察の取得、履歴書の作成など、LLMは得意です。
- **コードアシスタント**。使用する言語モデルに応じて、コードを書くのを助けるコードアシスタントを構築できます。例えば、GitHub CopilotやChatGPTを使用してコードを書くのを助けることができます。

## どのように始めればいいの？

通常、LLMと統合する方法を見つける必要があり、以下の2つのアプローチが一般的です：

- APIを使用する。プロンプトを含むウェブリクエストを作成し、生成されたテキストを取得します。
- ライブラリを使用する。ライブラリはAPIコールをカプセル化し、使いやすくします。

## ライブラリ/SDK

LLMと連携するためのよく知られたライブラリがいくつかあります：

- **openai**。このライブラリは、モデルに接続してプロンプトを送信するのを簡単にします。

次に、高レベルで動作するライブラリがあります：

- **Langchain**。Pythonをサポートしていることで知られています。
- **Semantic Kernel**。Microsoftによるライブラリで、C#、Python、Javaをサポートしています。

## openaiを使った最初のアプリ

最初のアプリをどのように構築するか、必要なライブラリ、必要なものなどを見てみましょう。

### openaiのインストール

OpenAIまたはAzure OpenAIと対話するためのライブラリは多数あります。C#、Python、JavaScript、Javaなどの多くのプログラミング言語を使用することが可能です。`openai` Pythonライブラリを使用することを選択したので、`pip`を使用してインストールします。

```bash
pip install openai
```

### リソースの作成

次のステップを実行する必要があります：

- Azureでアカウントを作成します [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- Azure OpenAIへのアクセスを取得します。 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) にアクセスして、アクセスをリクエストします。

  > [!NOTE]
  > 執筆時点では、Azure OpenAIへのアクセスを申請する必要があります。

- Pythonをインストールします <https://www.python.org/>
- Azure OpenAI Serviceリソースを作成します。リソースの作成方法については、こちらのガイドを参照してください [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### APIキーとエンドポイントの特定

この時点で、`openai`ライブラリに使用するAPIキーを指定する必要があります。APIキーを見つけるには、Azure OpenAIリソースの「Keys and Endpoint」セクションに移動し、「Key 1」値をコピーします。

![AzureポータルのKeys and Endpointリソースブレード](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

この情報をコピーしたので、ライブラリに使用するよう指示しましょう。

> [!NOTE]
> APIキーをコードから分離することは価値があります。環境変数を使用してこれを行うことができます。
>
> - 環境変数を設定します `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Azureの設定

Azure OpenAIを使用している場合、設定方法は次のとおりです：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上記では、次の設定を行っています：

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` クラス。以下はその例です：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

上記のコードでは、使用したいモデルとプロンプトを渡して完了オブジェクトを作成し、生成されたテキストを出力します。

### チャット完了

これまでに見たように、`Completion` to generate text. But there's another class called `ChatCompletion` を使用しており、これはチャットボットに適しています。これを使用する例は以下の通りです：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

この機能については、今後の章で詳しく説明します。

## 演習 - 最初のテキスト生成アプリ

openaiのセットアップと設定方法を学んだので、最初のテキスト生成アプリを構築する時が来ました。アプリを構築するには、次の手順に従ってください：

1. 仮想環境を作成し、openaiをインストールします：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windowsを使用している場合は `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` 値を入力します。

1. _app.py_ ファイルを作成し、次のコードを入力します：

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
   completion = client.chat.completions.create(model=deployment, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Azure OpenAIを使用している場合、`api_type` to `azure` and set the `api_key` をAzure OpenAIキーに設定する必要があります。

   次のような出力が表示されます：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 異なる目的のための異なるタイプのプロンプト

プロンプトを使用してテキストを生成する方法を見ました。実行しているプログラムを変更して、異なるタイプのテキストを生成することができます。

プロンプトはさまざまなタスクに使用できます。例えば：

- **特定のタイプのテキストを生成**。例えば、詩やクイズの質問などを生成できます。
- **情報の検索**。以下の例のように、情報を検索するためにプロンプトを使用できます。「ウェブ開発におけるCORSとは何か？」。
- **コードの生成**。プロンプトを使用してコードを生成できます。例えば、メールを検証するための正規表現を開発する、またはウェブアプリのようなプログラム全体を生成することができます。

## より実践的なユースケース：レシピジェネレーター

家にある材料を使って料理をしたいとしましょう。そのためにはレシピが必要です。レシピを見つける方法としては、検索エンジンを使用するか、LLMを使用することができます。

次のようなプロンプトを書くことができます：

> "以下の材料を使用した料理のレシピを5つ見せてください：鶏肉、じゃがいも、にんじん。各レシピには使用するすべての材料をリストしてください"

上記のプロンプトを与えると、次のような応答を得るかもしれません：

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

この結果は素晴らしいです、何を料理するかが分かります。この時点で、役立つ改善点としては：

- 嫌いな材料やアレルギーのある材料を除外する。
- 家にない材料を考慮した買い物リストを作成する。

上記のケースに対して、追加のプロンプトを追加しましょう：

> "アレルギーがあるのでにんにくを含むレシピを削除し、別のものに置き換えてください。また、家に鶏肉、じゃがいも、にんじんがあることを考慮した買い物リストを作成してください。"

これで新しい結果が得られます：

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

これがあなたの5つのレシピで、にんにくは言及されておらず、家にあるものを考慮した買い物リストもあります。

## 演習 - レシピジェネレーターを構築

シナリオを演じたので、デモンストレーションされたシナリオに一致するコードを書きましょう。以下の手順に従ってください：

1. 既存の _app.py_ ファイルを開始点として使用
1. `prompt` 変数を特定し、そのコードを次のように変更：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   コードを実行すると、次のような出力が表示されるはずです：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE、LLMは非決定論的なので、プログラムを実行するたびに異なる結果が得られるかもしれません。

   素晴らしいですね、改善方法を見てみましょう。改善するために、コードを柔軟にし、材料やレシピの数を改善し変更できるようにしたいです。

1. コードを次のように変更します：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   コードをテスト実行すると、次のようになります：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### フィルターと買い物リストの追加による改善

レシピを生成する能力を持つ動作するアプリがあり、ユーザーからの入力に依存しているため柔軟性があります。レシピの数だけでなく使用する材料も考慮します。

これをさらに改善するために、次のことを追加したいです：

- **材料をフィルターアウトする**。嫌いな材料やアレルギーのある材料をフィルターアウトできるようにしたいです。この変更を達成するために、既存のプロンプトを編集し、次のように末尾にフィルター条件を追加できます：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上記では、プロンプトの末尾に `{filter}` を追加し、ユーザーからフィルター値を取得します。

  プログラムを実行したときの入力例は次のようになります：

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

  ご覧の通り、牛乳を含むレシピはすべてフィルターアウトされています。しかし、乳糖不耐症の場合は、チーズを含むレシピもフィルターアウトしたいかもしれませんので、明確にする必要があります。

- **買い物リストを作成する**。家にあるものを考慮した買い物リストを作成したいです。

  この機能のために、すべてを1つのプロンプトで解決しようとすることもできますが、2つのプロンプトに分けることもできます。後者のアプローチを試してみましょう。ここでは追加のプロンプトを提案していますが、これが機能するためには、最初のプロンプトの結果を2番目のプロンプトへのコンテキストとして追加する必要があります。

  最初のプロンプトからの結果を出力するコードの部分を特定し、その下に次のコードを追加します：

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

  次の点に注意してください：

  1. 最初のプロンプトの結果を新しいプロンプトに追加して、新しいプロンプトを構築しています：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 最初のプロンプトで要求したトークンの数を考慮して、新しいリクエストを行います。このため、今回は `max_tokens` を1200とします。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     このコードを試してみると、次のような出力が得られます：

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

これまでにあるのは機能するコードですが、さらに改善するために調整するべき点がいくつかあります。すべきことの一部は：

- **コードから秘密を分離する**、APIキーのように。秘密はコードに含めるべきではなく、安全な場所に保存されるべきです。コードから秘密を分離するために、環境変数や `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` ファイルのようなライブラリを使用できます。以下の内容を含む：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意：Azureの場合、次の環境変数を設定する必要があります：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     コードでは、次のように環境変数を読み込みます：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **トークンの長さに関する一言**。生成したいテキストにどれだけのトークンが必要かを考慮すべきです。トークンには費用がかかるため、可能な限り、使用するトークンの数を経済的にするようにすべきです。例えば、プロンプトをどのように表現すればトークンを減らせるか？

  使用するトークンを変更するには、`max_tokens` パラメータを使用できます。例えば、100トークンを使用したい場合は、次のようにします：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **温度の実験**。これまで温度については触れていません

**免責事項**:
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確さを追求しておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。原文が書かれた言語の文書を正式な情報源と見なしてください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用によって生じた誤解や誤解釈について、当社は責任を負いません。