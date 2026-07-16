# 建立文字生成應用程式

[![建立文字生成應用程式](../../../translated_images/zh-TW/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(點擊上方圖片觀看本課程影片)_

截至目前為止，你已經看到課程中有一些核心概念，比如提示語，甚至還有一門專門的學科叫做「提示語工程」。許多你可以互動的工具，比如 ChatGPT、Office 365、Microsoft Power Platform 等，都支援你使用提示語來完成某些任務。

若你想將這樣的體驗加入到應用程式中，你需要理解提示語、完成項目等概念，並選擇一個相應的程式庫。這正是本章節要教你的內容。

## 介紹

在本章節中，你將會：

- 了解 openai 程式庫及其核心概念。
- 使用 openai 建立文字生成應用程式。
- 理解如何使用提示語、溫度和代幣這些概念來建立文字生成應用程式。

## 學習目標

學完本課程後，你將能：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立文字生成應用程式。
- 配置你的應用程式以使用更多或更少的代幣，並調整溫度，讓輸出結果多樣化。

## 什麼是文字生成應用程式？

通常當你建立應用程式時，它會有某種類型的介面，例如：

- 命令式介面。控制臺應用程式是你輸入指令然後它執行任務的典型應用。例如，`git` 就是命令式應用程式。
- 使用者介面 (UI)。有些應用程式有圖形使用者介面 (GUIs)，你可以點擊按鈕、輸入文字、選擇選項等等。

### 控制臺和 UI 應用程式有限制

與命令式應用程式相比，你輸入指令：

- <strong>有限制</strong>。你不能隨意輸入任何指令，只能使用應用程式支援的指令。
- <strong>語言特定</strong>。有些應用程式支援多種語言，但預設是針對特定語言建構，即使你可以額外新增語言支援。

### 文字生成應用程式的優勢

那麼文字生成應用程式有什麼不同呢？

在文字生成應用程式中，你有更多彈性，不侷限於一套指令或特定輸入語言。相反地，你可以使用自然語言與應用程式互動。另一個好處是，你已經在與一個根據大量資料集訓練的資料源互動，而傳統應用程式可能受限於資料庫中的資訊。

### 我可以用文字生成應用程式做什麼？

你可以做很多事情。例如：

- <strong>聊天機器人</strong>。能回答關於主題的問題，比如你公司的產品等，非常適合。
- <strong>助理工具</strong>。大型語言模型擅長摘要文本、獲取文本洞見，產生文本例如履歷等。
- <strong>程式碼助理</strong>。根據你使用的語言模型，你可以建立程式碼助理幫你撰寫程式碼。例如，你可以使用 GitHub Copilot 或 ChatGPT 來協助寫程式。

## 如何開始？

你需要找到一種方法與大型語言模型 (LLM) 整合，通常有以下兩種方法：

- 使用 API。你建構網路請求，送入提示語，然後取得生成的文字。
- 使用程式庫。程式庫封裝了 API 呼叫，使使用更簡單。

## 程式庫／SDK

有幾個知名的程式庫用來操作大型語言模型，比如：

- **openai**，這個程式庫讓你輕鬆連接到模型並發送提示語。

還有一些功能更高階的程式庫：

- **Langchain**。Langchain 風靡一時，支援 Python。
- **Semantic Kernel**。Semantic Kernel 是微軟的程式庫，支援 C#、Python、Java。

## 使用 openai 建立第一個應用程式

讓我們來看看如何建立第一個應用程式，哪些程式庫需要、需要多少設定等等。

### 安裝 openai

現在有很多程式庫可以跟 OpenAI 或 Azure OpenAI 互動。你可以選擇多種程式語言，例如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` Python 程式庫，所以會用 `pip` 來安裝。

```bash
pip install openai
```

### 建立資源

你需要完成以下步驟：

- 在 Azure 上建立帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 取得 Azure OpenAI 訪問權限。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 申請訪問。

  > [!NOTE]
  > 撰寫本文時，你需要申請 Azure OpenAI 訪問權限。

- 安裝 Python <https://www.python.org/>
- 建立 Azure OpenAI 服務資源。參考本指南了解如何[建立資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰及端點

此時，你需要告訴 `openai` 程式庫要使用哪個 API 金鑰。要找到你的 API 金鑰，請前往 Azure OpenAI 資源的「金鑰與端點」區段，複製「Key 1」的值。

![Azure Portal 中的金鑰與端點資源窗格](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

既然已經複製了這些資訊，讓我們指示程式庫使用它。

> [!NOTE]
> 你最好將 API 金鑰與程式碼分開管理。你可以使用環境變數來實現這件事。
>
> - 設定環境變數 `OPENAI_API_KEY` 為你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 設定 Azure 配置

如果你使用 Azure OpenAI（現在是 Microsoft Foundry 的一部分），設定方法如下。我們使用標準的 `OpenAI` 客戶端指向 Azure OpenAI 的 `/openai/v1/` 端點，這適用於 Responses API，且無需 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上面設定了：

- `api_key`，你的 API 金鑰，在 Azure Portal 或 Microsoft Foundry 入口網站找到。
- `base_url`，你的 Foundry 資源端點，加上 `/openai/v1/`。這個穩定的 v1 端點可用於 OpenAI 和 Azure OpenAI，且無需管理 `api_version`。

> [!NOTE] > `os.environ` 用來讀取環境變數。你可以用它讀取像是 `AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT`。這些環境變數可以在你的終端機設定或使用 `dotenv` 之類的程式庫設定。

## 生成文字

生成文字的方式是使用 Responses API 的 `responses.create` 方法。範例如下：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # 這是您的模型部署名稱
    input=prompt,
    store=False,
)
print(response.output_text)
```

在上面程式碼中，我們建立一個回應，並傳入我們想用的模型和提示語。然後透過 `response.output_text` 印出生成的文字。

### 多回合對話

Responses API 非常適合單回合文字生成和多回合聊天機器人 — 你提供一個訊息清單於 `input` 以建立對話：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

更多關於此功能會在後續章節說明。

## 練習 - 你的第一個文字生成應用程式

現在我們學會如何設定與配置 openai，是時候來建立你的第一個文字生成應用程式。請按照以下步驟操作：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用 Windows，請輸入 `venv\Scripts\activate`，而非 `source venv/bin/activate`。

   > [!NOTE]
   > 在 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 中，搜尋 `Open AI`，選擇 `Open AI resource`，然後點「金鑰與端點」，複製 `Key 1` 的值。

1. 建立 _app.py_ 檔案，並寫入以下程式碼：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 新增您的完成碼
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 發送請求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 列印回應
   print(response.output_text)
   ```

   > [!NOTE]
   > 如果你使用純 OpenAI（非 Azure），請用 `client = OpenAI(api_key="<將此替換成你的 OpenAI 金鑰>")`（無需 `base_url`），並傳入模型名稱，例如 `gpt-4o-mini`，取代部署名稱。

   你會看到類似以下的輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示語，用於不同任務

現在你已經知道如何使用提示語生成文字。你甚至有一個程式正在執行，你可以修改它來生成不同類型的文字。

提示語可以用來做各種任務。例如：

- <strong>生成特定類型的文字</strong>。如生成詩歌、測驗問題等。
- <strong>查找資訊</strong>。你可以使用提示語查詢資訊，例如「CORS 在網頁開發中是什麼意思？」。
- <strong>生成程式碼</strong>。你可以用提示語生成程式碼，例如開發用於驗證電子郵件的正規表示式，或甚至生成整個程式，例如網頁應用程式。

## 更實際的案例：食譜產生器

想像你家裡有一些食材，想要烹調料理。你需要食譜。找食譜的方式可以用搜尋引擎，也可以用大型語言模型來完成。

你可以寫一個提示語，像這樣：

> 「給我 5 道包含以下食材的料理：雞肉、馬鈴薯和紅蘿蔔。請列出每道料理所使用的所有食材」

根據上述提示語，你可能會得到類似的回答：

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

這樣的結果很棒，我知道該煮什麼了。此時，可能有以下有用的改進：

- 過濾我不喜歡或過敏的食材。
- 產生購物清單，以防我家裡沒有全部食材。

對於以上情形，可以加一個附加提示語：

> 「請移除含有大蒜的食譜，我對大蒜過敏，並請以其他食材替代。同時，根據我有的雞肉、馬鈴薯和紅蘿蔔，幫我產生購物清單。」

現在你會得到新的結果，像是：

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

這就是你的五道食譜，不含大蒜，且同時有考量你家已有的食材，產生了購物清單。

## 練習 - 建立食譜產生器

現在我們完成了情境演練，讓我們撰寫對應的程式碼。請依照以下步驟：

1. 以現有的 _app.py_ 檔案作為起點
1. 找到 `prompt` 變數，將其程式碼改成以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   現在執行程式，你應該會看到類似以下的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的大型語言模型結果非確定性，每次執行可能不同。

   很好，讓我們來看看如何改進。我們想讓程式碼更靈活，讓食材和食譜數量可以輕鬆調整。

1. 我們接著做以下修改：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 將食譜數量插入提示和食材中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試執行的程式碼看起來可能像這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 透過添加過濾條件與購物清單來改進

現在我們有一個可用的應用程式，能夠產生食譜，且很靈活，因為它依賴用戶輸入的食譜數量與使用的食材。

接著我們想加上以下功能：

- <strong>過濾食材</strong>。我們希望能過濾掉不喜歡或過敏的食材。為了實現這一點，我們可以修改現有的提示語，並在末尾加入過濾條件，如下：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面我們在提示語結尾添加了 `{filter}`，並且從使用者那裡捕捉過濾條件的值。

  執行程式時的範例輸入現在看起來會是這樣：

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

  如你所見，含有牛奶的任何食譜已被過濾掉。但如果你乳糖不耐，可能也想過濾起司類食譜，所以要說清楚。


- <strong>產生購物清單</strong>。我們想要產生一份購物清單，考慮到家中已經有哪些物品。

  對於這個功能，我們可以嘗試在一個提示中解決所有問題，或者將其分成兩個提示。讓我們嘗試後者。這裡我們建議新增一個提示，但為了讓這個方法工作，我們需要把前一個提示的結果作為後一個提示的上下文。

  找到程式碼中列印第一個提示結果的部分，並在該處下方加入以下程式碼：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 列印回應
  print("Shopping list:")
  print(response.output_text)
  ```

  注意以下事項：

  1. 我們透過新增第一個提示的結果到新的提示，來構造一個新的提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們發出新的請求，同時考慮到第一個提示要求的令牌數，因此這次設定 `max_output_tokens` 為 1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     嘗試這段程式碼後，我們得到以下輸出：

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

目前為止的程式碼可以運作，但還有一些調整可以進一步改進。有些事情我們應該做的是：

- <strong>將密鑰與程式碼分離</strong>，例如 API 金鑰。密鑰不應該直接寫在程式碼中，而應該儲存在安全的位置。分離密鑰與程式碼，我們可以使用環境變量以及像 `python-dotenv` 這樣的函式庫從文件載入它們。程式碼範例如下：

  1. 建立一個 `.env` 檔案，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Microsoft Foundry 中的 Azure OpenAI，您需要設定以下環境變數：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     在程式碼中，您可這樣載入環境變量：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>關於令牌長度</strong>。我們應該考慮產生想要的文字需要多少令牌。令牌是會花費金錢的，因此在可能的情況下，我們應該盡量經濟使用令牌數。例如，我們能否調整提示詞，讓它用更少令牌？

  要改變使用的令牌數，可以使用 `max_output_tokens` 參數。例如，如果您想使用 100 個令牌，可以這樣寫：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- <strong>嘗試溫度參數</strong>。溫度是我們之前尚未提及的重要參數，它會影響程式的表現。溫度值越高，輸出越隨機；溫度值越低，輸出越可預測。請考慮你是否希望輸出多樣化。

  要調整溫度，可以使用 `temperature` 參數。例如，如果你想使用 0.5 的溫度，可以這樣寫：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，越接近 1.0，輸出越多變。

## 作業

這個作業你可以選擇要做什麼。

這裡有一些建議：

- 調整食譜生成器應用程式來進一步改善它。嘗試不同溫度值和提示詞看看你能達成什麼。
- 建立一個「學習夥伴」。這個應用程式應該能回答關於某個主題的問題，例如 Python，你可以有提示詞像是「Python 中某個主題是什麼？」或者提示詞是要示範某個主題的程式碼等等。
- 歷史機器人，讓歷史變得生動。指示機器人扮演某個歷史人物，然後問它關於該人物的生平及時代的問題。

## 解答

### 學習夥伴

以下是一個起始提示，看看你如何使用並調整它使其符合你的喜好。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

這裡有一些你可以使用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識測驗

溫度參數的作用是什麼？

1. 它控制輸出結果的隨機程度。
1. 它控制回應的大小。
1. 它控制使用多少令牌。

## 🚀 挑戰

在進行作業時，嘗試變化溫度，設成 0、0.5 和 1。記住 0 是最不多變，而 1 是最多變。哪個數值最適合你的應用程式？

## 好棒！繼續您的學習

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您對生成式 AI 的認識！

接著前往第7課，我們將探討如何[建立聊天應用程式](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->