<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:02:42+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "mo"
}
-->
# 構建文本生成應用程式

[![構建文本生成應用程式](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.mo.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(點擊上方圖片觀看本課程的影片)_

到目前為止，您已經通過這門課程看到一些核心概念，例如提示（prompts），甚至有一整個學科稱為「提示工程」。許多工具，例如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持您使用提示來完成某些事情。

要將這種體驗添加到應用程式中，您需要了解提示、完成（completions）等概念並選擇一個工作庫。這正是您將在本章中學習的內容。

## 介紹

在本章中，您將：

- 學習 openai 庫及其核心概念。
- 使用 openai 構建一個文本生成應用程式。
- 理解如何使用提示、溫度（temperature）和代幣（tokens）等概念來構建文本生成應用程式。

## 學習目標

在本課結束時，您將能夠：

- 解釋什麼是文本生成應用程式。
- 使用 openai 構建文本生成應用程式。
- 配置您的應用程式以使用更多或更少的代幣，並更改溫度以獲得多樣化的輸出。

## 什麼是文本生成應用程式？

通常，當您構建一個應用程式時，它會有某種類型的介面，如下所示：

- 基於命令的。控制台應用程式是典型的應用程式，您輸入一個命令，它就執行一個任務。例如，`git` 是一個基於命令的應用程式。
- 用戶介面（UI）。有些應用程式有圖形用戶介面（GUIs），您可以點擊按鈕、輸入文本、選擇選項等。

### 控制台和 UI 應用程式的限制

與基於命令的應用程式相比，您輸入一個命令：

- **有限制**。您不能隨便輸入任何命令，只能輸入應用程式支持的命令。
- **語言特定**。有些應用程式支持多種語言，但默認情況下，應用程式是為特定語言構建的，即使您可以添加更多語言支持。

### 文本生成應用程式的好處

那麼文本生成應用程式有什麼不同呢？

在文本生成應用程式中，您有更多的靈活性，您不受限於一組命令或特定的輸入語言。相反，您可以使用自然語言與應用程式互動。另一個好處是，由於您已經在與一個基於龐大信息語料庫訓練的數據源互動，而傳統應用程式可能僅限於數據庫中的內容。

### 我可以用文本生成應用程式構建什麼？

您可以構建許多東西。例如：

- **聊天機器人**。一個回答有關主題問題的聊天機器人，例如您的公司及其產品，可能是一個很好的選擇。
- **助手**。LLMs 在總結文本、從文本中獲得洞察力、生成簡歷等文本生成方面非常出色。
- **代碼助手**。根據您使用的語言模型，您可以構建一個幫助您編寫代碼的代碼助手。例如，您可以使用 GitHub Copilot 或 ChatGPT 等產品來幫助您編寫代碼。

## 我該如何開始？

好吧，您需要找到一種方法來與 LLM 集成，通常包括以下兩種方法：

- 使用 API。在這裡，您正在構建包含提示的網絡請求，並獲得生成的文本回應。
- 使用庫。庫幫助封裝 API 調用，使其更易於使用。

## 庫/SDK

有一些著名的庫可以與 LLM 一起使用，例如：

- **openai**，這個庫使您可以輕鬆連接到模型並發送提示。

然後還有一些在更高層次上運行的庫，例如：

- **Langchain**。Langchain 以支持 Python 而聞名。
- **Semantic Kernel**。Semantic Kernel 是由 Microsoft 提供的支持 C#、Python 和 Java 語言的庫。

## 使用 openai 的第一個應用程式

讓我們看看如何構建我們的第一個應用程式，需要哪些庫，要求多少等等。

### 安裝 openai

有許多庫可以與 OpenAI 或 Azure OpenAI 互動。可以使用多種編程語言，例如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` Python 庫，因此我們將使用 `pip` 來安裝它。

```bash
pip install openai
```

### 創建資源

您需要執行以下步驟：

- 在 Azure 上創建一個帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 獲得 Azure OpenAI 的訪問權限。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 並申請訪問。

  > [!NOTE]
  > 在撰寫本文時，您需要申請 Azure OpenAI 的訪問權限。

- 安裝 Python <https://www.python.org/>
- 已創建一個 Azure OpenAI 服務資源。請參閱此指南了解如何 [創建資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 密鑰和端點

此時，您需要告訴您的 `openai` 庫使用哪個 API 密鑰。要查找您的 API 密鑰，請轉到 Azure OpenAI 資源的「密鑰和端點」部分並複製「密鑰 1」的值。

![Azure 入口網站中的密鑰和端點資源刀鋒](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在您已經複製了這些信息，讓我們指示庫使用它。

> [!NOTE]
> 值得將您的 API 密鑰與代碼分開。您可以通過使用環境變量來實現。
>
> - 設置環境變量 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### 設置 Azure 配置

如果您使用的是 Azure OpenAI，以下是設置配置的方法：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

在上面，我們設置了以下內容：

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` 類。以下是一個示例：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上述代碼中，我們創建了一個完成對象並傳入我們想要使用的模型和提示。然後我們打印生成的文本。

### 聊天完成

到目前為止，您已經看到我們如何使用 `Completion` to generate text. But there's another class called `ChatCompletion`，這更適合聊天機器人。以下是使用它的示例：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

更多有關此功能的內容將在即將到來的章節中介紹。

## 練習 - 您的第一個文本生成應用程式

現在我們已經學會了如何設置和配置 openai，是時候構建您的第一個文本生成應用程式了。要構建您的應用程式，請按照以下步驟：

1. 創建一個虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果您使用的是 Windows，請輸入 `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` 值。

1. 創建一個 _app.py_ 文件並給它以下代碼：

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
   > 如果您使用的是 Azure OpenAI，您需要將 `api_type` to `azure` and set the `api_key` 設置為您的 Azure OpenAI 密鑰。

   您應該會看到類似以下的輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示，適用於不同的事情

現在您已經看到如何使用提示生成文本。您甚至有一個可以運行的程序，您可以修改和更改它以生成不同類型的文本。

提示可以用於各種任務。例如：

- **生成一種類型的文本**。例如，您可以生成詩歌、測驗問題等。
- **查詢信息**。您可以使用提示來查找信息，例如以下示例「在網頁開發中，CORS 是什麼意思？」。
- **生成代碼**。您可以使用提示生成代碼，例如開發用於驗證電子郵件的正則表達式，或者為什麼不生成整個程序，例如網頁應用程式？

## 更實際的用例：食譜生成器

想像一下，您家裡有一些食材，您想做點什麼吃。為此，您需要一個食譜。找到食譜的方法是使用搜索引擎，或者您可以使用 LLM 來做到這一點。

您可以這樣寫一個提示：

> 「給我 5 個包含以下食材的菜餚食譜：雞肉、馬鈴薯和胡蘿蔔。每個食譜列出所有使用的食材。」

給定上述提示，您可能會得到類似以下的回應：

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

這個結果很棒，我知道該做什麼菜了。此時，可能有用的改進是：

- 過濾掉我不喜歡或過敏的食材。
- 生成購物清單，以防我家裡沒有所有食材。

對於上述情況，讓我們添加一個額外的提示：

> 「請移除含有大蒜的食譜，因為我過敏，並用其他東西替換。此外，請為食譜生成購物清單，考慮到我已經有雞肉、馬鈴薯和胡蘿蔔在家。」

現在您有了一個新結果，即：

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

這就是您的五個食譜，沒有提到大蒜，您還有一個考慮到您已經在家擁有的食材的購物清單。

## 練習 - 構建一個食譜生成器

現在我們已經演示了一個場景，讓我們編寫代碼來匹配演示的場景。要做到這一點，請按照以下步驟：

1. 使用現有的 _app.py_ 文件作為起點
1. 找到 `prompt` 變量並將其代碼更改為以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果您現在運行代碼，您應該會看到類似以下的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，您的 LLM 是非確定性的，因此每次運行程序時，您可能會得到不同的結果。

   很好，讓我們看看如何改進。為了改進，我們希望確保代碼是靈活的，因此食材和食譜數量可以改進和更改。

1. 讓我們以下列方式更改代碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   進行測試運行的代碼，可能看起來像這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通過添加過濾器和購物清單來改進

我們現在有一個能夠生成食譜的工作應用程式，並且它是靈活的，因為它依賴於用戶的輸入，不僅在食譜數量上，而且在使用的食材上。

為了進一步改進，我們希望添加以下內容：

- **過濾掉食材**。我們希望能夠過濾掉我們不喜歡或過敏的食材。要完成此更改，我們可以編輯現有的提示並在其末尾添加過濾條件，如下所示：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  在上面，我們在提示的末尾添加了 `{filter}`，我們還從用戶那裡獲取了過濾器的值。

  運行程序的示例輸入現在可能看起來像這樣：

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

  如您所見，任何含有牛奶的食譜都被過濾掉了。但是，如果您對乳糖不耐受，您可能還想過濾掉含有奶酪的食譜，因此需要明確說明。

- **生成購物清單**。我們希望生成一個購物清單，考慮到我們已經在家擁有的食材。

  對於此功能，我們可以嘗試在一個提示中解決所有問題，也可以將其分成兩個提示。讓我們嘗試後者的方法。在這裡，我們建議添加一個額外的提示，但為了使其工作，我們需要將前一個提示的結果作為上下文添加到後一個提示中。

  找到代碼中打印出第一個提示結果的部分，並在其下方添加以下代碼：

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

  注意以下幾點：

  1. 我們正在構建一個新提示，將第一個提示的結果添加到新提示中：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們發出一個新的請求，但也考慮到我們在第一個提示中要求的代幣數，因此這次我們說 `max_tokens` 是 1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     進行這段代碼的測試運行，我們現在得到以下輸出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改善您的設置

到目前為止，我們擁有的是有效的代碼，但我們應該進行一些調整以進一步改進。一些應該做的事情是：

- **將密鑰與代碼分開**，例如 API 密鑰。密鑰不應該在代碼中，應該存儲在安全的位置。要將密鑰與代碼分開，我們可以使用環境變量和像 `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` 文件這樣的庫，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Azure，您需要設置以下環境變量：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在代碼中，您可以像這樣加載環境變量：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **關於代幣長度的說明**。我們應該考慮我們需要多少代幣來生成我們想要的文本。代幣是有成本的，所以在可能的情況下，我們應該嘗試節省代幣的使用量。例如，我們能否重新措辭提示，以便可以使用更少的代幣？

  要更改使用的代幣，您可以使用 `max_tokens` 參數。例如，如果您想使用 100 個代幣，您可以這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **實驗溫度**。溫度是我們尚未提到的內容，但它對我們程序的性能具有重要影響。溫度值越高，輸出越隨機。相反，溫度值越低，輸出越可預測。考慮一下您是否希望輸出有變化。

  要更改溫度，您可以使用 `temperature` 參數。例如，如果您想使用 0.5 的溫度，您可以這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，接近 1.0 的值，輸出越多樣化。

## 作業

對於這個作業，您可以選擇構建什麼。

以下是一些建議：

- 調整食譜生成應用程式以進一步改進。試驗不同的溫度值和提示，看看您能得到什麼結果。
- 構建一個「學習夥伴」。這個應用程式應該能夠回答有關某個主題的問題，例如 Python，您可以有像「Python 中某個主題是什麼？」這樣的提示，或者您可以有一個提示說，顯示某個主題的

**免責聲明**：
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的本地語言版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。