# 建立文字生成應用程式

[![建立文字生成應用程式](../../../translated_images/zh-TW/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(點擊上圖觀看本課程影片)_

你到目前為止已經在這個課程中看到，有一些核心概念像是提示詞，甚至有整個領域稱為「提示工程」。許多你可以使用的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持你透過提示詞來完成任務。

若你想在應用程式中新增這種體驗，你需要理解提示詞、完成等概念，並選擇一個工作所需的函式庫。這正是你會在本章學習的內容。

## 介紹

在本章中，你將會：

- 了解 openai 函式庫及其核心概念。
- 使用 openai 建立文字生成應用程式。
- 理解如何使用提示詞、溫度和代幣等概念來建立文字生成應用程式。

## 學習目標

在本課程結束時，你將能：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立文字生成應用程式。
- 設定應用程式使用更多或更少的代幣，並可調整溫度，以產生多樣化的輸出。

## 什麼是文字生成應用程式？

通常當你建立一個應用程式時，它會有某種類型的介面，如以下例子：

- 指令式。主控台應用程式是典型的應用程式，你輸入指令後執行任務。例如，`git` 就是一個指令式應用程式。
- 使用者介面 (UI)。一些應用程式有圖形使用者介面 (GUI)，你可以點擊按鈕、輸入文字、選取選項等。

### 主控台和使用者介面應用程式的限制

相較於指令式應用程式，當你輸入指令時：

- <strong>有局限</strong>。你不能隨意輸入任何指令，只能使用應用程式支持的指令。
- <strong>語言特定</strong>。有些應用程式支持多種語言，但預設都是為某種語言建置，即使你可以加上其他語言支持。

### 文字生成應用程式的優點

那麼文字生成應用程式有何不同？

在文字生成應用程式中，你有更多彈性，不受限於固定指令集合或特定輸入語言。你可以用自然語言與應用程式互動。另一個好處是，你已經在與一個基於龐大語料庫訓練的資料來源互動，而傳統應用程式可能受限於資料庫內容。

### 文字生成應用程式可以做什麼？

你可以做很多事情。例如：

- <strong>聊天機器人</strong>。像是回答關於公司及產品主題問題的聊天機器人會非常適合。
- <strong>助手</strong>。大型語言模型擅長文字摘要、從文字提煉洞見、產生如履歷等文本。
- <strong>程式碼助手</strong>。根據使用的語言模型，你可以建立協助撰寫程式碼的助手。例如，你可以使用產品如 GitHub Copilot 以及 ChatGPT 協助寫程式。

## 如何開始？

你需要找到一種方法整合大型語言模型（LLM），通常有以下兩種方式：

- 使用 API。這裡你是建構網路請求，帶入提示詞並取得生成文字。
- 使用函式庫。函式庫幫助封裝 API 呼叫，讓使用更方便。

## 函式庫/開發套件（SDK）

有幾個知名的函式庫可用於操作大型語言模型，例如：

- **openai**，這個函式庫讓你輕鬆連線到模型並送出提示詞。

另外還有一些運作層次較高的函式庫：

- **Langchain**。Langchain 知名且支持 Python。
- **Semantic Kernel**。Semantic Kernel 是微軟的函式庫，支持 C#、Python 及 Java。

## 使用 openai 建立第一個應用程式

讓我們來看看如何建立第一個應用程式，需要哪些函式庫，需求多少等。

### 安裝 openai

有很多函式庫可用於與 OpenAI 或 Azure OpenAI 互動。你也可以使用多種程式語言，例如 C#、Python、JavaScript、Java 等。我們這裡選擇使用 `openai` Python 函式庫，透過 `pip` 安裝它。

```bash
pip install openai
```

### 創建資源

你需要執行以下步驟：

- 在 Azure 上創建帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 取得 Azure OpenAI 存取權限。前往 [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 並申請。

  > [!NOTE]
  > 撰寫本文時，你需要申請 Azure OpenAI 存取權限。

- 安裝 Python <https://www.python.org/>
- 已創建 Azure OpenAI 服務資源。請參閱本指南的[如何創建資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰和端點

此時，你需要告訴 `openai` 函式庫使用哪個 API 金鑰。請前往 Azure OpenAI 資源的「Keys and Endpoint」部分，複製「Key 1」值。

![Azure 入口網站中的 Keys and Endpoint 資源視窗](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已複製好資訊，讓我們指示函式庫使用它。

> [!NOTE]
> 將 API 金鑰與程式碼分離是值得的做法。你可以使用環境變數來達成。
>
> - 設定環境變數 `OPENAI_API_KEY` 為你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 設定 Azure 配置

如果你使用的是 Azure OpenAI（現為 Microsoft Foundry 的一部分），設定方式如下。我們使用標準的 `OpenAI` 用戶端，指向 Azure OpenAI 的 `/openai/v1/` 端點，這可搭配 Responses API 使用，不需 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上方設定了以下內容：

- `api_key`，即你在 Azure 入口網站或 Microsoft Foundry 入口網站找到的 API 金鑰。
- `base_url`，指向你的 Foundry 資源端點，並在後面加上 `/openai/v1/`。穩定的 v1 端點在 OpenAI 和 Azure OpenAI 之間通用，不需管理 `api_version`。

> [!NOTE] > `os.environ` 用於讀取環境變數。你可以用它讀取類似 `AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT` 的環境變數。在終端機或使用類似 `dotenv` 的函式庫設定這些環境變數。

## 生成文字

產生文字的方式是使用 Responses API，透過 `responses.create` 方法。範例如下：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # 這是您的模型部署名稱
    input=prompt,
    store=False,
)
print(response.output_text)
```

在上述程式碼中，我們建立了一個回應並傳入想使用的模型和提示詞。之後，我們透過 `response.output_text` 印出生成的文字。

### 多輪對話

Responses API 非常適合單輪文字生成和多輪聊天機器人——你在 `input` 裡提供訊息列表以建立對話：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

這部分功能會在後續章節做更深入介紹。

## 練習 — 你的第一個文字生成應用程式

既然我們已學到如何設定並配置 openai，現在是時候建立你的第一個文字生成應用程式。請依照以下步驟進行：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 若你使用 Windows，請輸入 `venv\Scripts\activate` 取代 `source venv/bin/activate`。

   > [!NOTE]
   > 在 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 找到你的 Azure OpenAI 金鑰，搜尋「Open AI」，選擇「Open AI 資源」，再選「Keys and Endpoint」，複製「Key 1」的值。

1. 建立 _app.py_ 檔案，並加入以下程式碼：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 新增您的完成程式碼
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 發出請求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 輸出回應內容
   print(response.output_text)
   ```

   > [!NOTE]
   > 若你使用純 OpenAI（非 Azure），請使用 `client = OpenAI(api_key="<請替換為你的 OpenAI 金鑰>")`（不設定 `base_url`），並傳入模型名稱如 `gpt-5-mini`，取代部署名稱。

   你應該會看到類似以下的輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示詞，應用於不同目的

現在你已經知道如何用提示詞生成文字。你甚至已有一個可運作並可修改、調整以產生不同類型文字的程式。

提示詞可用於各種任務。例如：

- <strong>生成特定類型文字</strong>。例如，你可以生成詩歌、測驗的問題等。
- <strong>查詢資訊</strong>。你可以用提示詞查找資訊，例如「CORS 在網頁開發中是什麼意思？」。
- <strong>生成程式碼</strong>。你可以用提示詞生成程式碼，例如開發用於驗證電子郵件的正則表達式，甚至生成整個程式如網站應用。

## 更實用的應用：食譜產生器

假設你有些食材在家，想做菜。你需要食譜。找到食譜的方式有用搜尋引擎，也可以用大型語言模型。

你可以寫出這樣的提示詞：

> 「請給我包含以下食材的五道菜食譜：雞肉、馬鈴薯和紅蘿蔔。每道菜請列出所用食材。」

根據上述提示詞，你可能會得到如下回應：

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

這樣的結果很棒，我知道要煮什麼了。此時，可能的改進包括：

- 篩選掉我不喜歡或過敏的食材。
- 產生購物清單，以防我家裡沒有所有食材。

針對上述需求，我們來加個進一步的提示詞：

> 「請移除含有大蒜的食譜，因為我過敏，並用其他食材替代。同時，製作這些食譜的購物清單，考慮我已有雞肉、馬鈴薯和紅蘿蔔。」

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

這就是不含大蒜的五道食譜，並且有依據你家中已有食材的購物清單。

## 練習 — 建立食譜產生器

現在我們模擬了一個情境，開始撰寫符合示範情景的程式碼。照以下步驟操作：

1. 以現有的 _app.py_ 檔為起點
1. 找到 `prompt` 變數，並將程式碼改成以下：

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

   > 注意，你的 LLM 不是確定性模型，因此每次運行程式可能得到不同結果。

   很好，接下來我們看看如何改進。為了讓程式更彈性，我們希望讓食材和食譜數量可調整和變更。

1. 我們改寫程式碼如下：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 將食譜數量插入提示和食材中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   進行測試執行的程式可能長這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 加入篩選和購物清單以改進

我們現在有一個可用的程式，能夠產生食譜，且相當彈性，因為它依賴使用者輸入的食譜數量及使用的食材。

想要進一步改進，我們可以加入：

- <strong>篩選食材</strong>。我們希望能篩選不喜歡或過敏的食材。為達成此變更，我們可以編輯現有的提示詞，在最後加入篩選條件：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面我們在提示詞尾端加上 `{filter}`，同時從使用者捕捉篩選條件的值。

  執行程式時的一個範例輸入可能看起來像這樣：

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

  如你所見，任何含牛奶的食譜被篩除。但如果你乳糖不耐，也可能想篩除含乳酪的食譜，所以務必清楚說明。


- <strong>產生購物清單</strong>。我們想要產生一個購物清單，並考慮我們家中已有的物品。

  對於此功能，我們可以嘗試用一個提示完成所有任務，或者將它拆分成兩個提示。我們嘗試後者。在這裡，我們建議增加一個額外的提示，但要做到這點，我們需要把前一個提示的結果作為上下文加入到後一個提示中。

  找到程式碼中印出第一個提示結果的部分，並在其下新增以下程式碼：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 印出回應
  print("Shopping list:")
  print(response.output_text)
  ```

  注意以下事項：

  1. 我們透過將第一個提示的結果加入新的提示中來構造一個新的提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們做了一個新的請求，同時考慮第一個提示要求的代幣數量，因此這次 `max_output_tokens` 設為 1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     執行這段程式碼後，我們得到以下輸出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改善你的設定

目前的程式碼能運作，但有一些調整能進一步改進。一些我們應該做的事情包括：

- <strong>將機密資訊與程式碼分離</strong>，例如 API 金鑰。機密資訊不應該寫在程式碼中，而應該妥善儲存在安全的位置。要將機密與程式碼分離，我們可以使用環境變數，並用像 `python-dotenv` 之類的套件從檔案載入。程式碼中大致長這樣：

  1. 建立一個 `.env` 檔案，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，針對 Microsoft Foundry 的 Azure OpenAI，您需要設定以下環境變數：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     在程式碼中，可這樣載入環境變數：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>關於代幣長度</strong>。我們應考慮產生所需文字時代幣的數量。代幣會產生成本，所以越能節省代幣使用越好。例如，我們是否可以調整提示語，使使用的代幣更少？

  想改變使用的代幣量，可以設定 `max_output_tokens` 參數。例如，若想使用 100 代幣，可以這樣寫：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **嘗試調整 temperature**。temperature（溫度）目前還沒提及，但對程式表現很重要。溫度越高，輸出越隨機；溫度越低，輸出越可預測。請思考你是否希望輸出有較大變化。

  要調整溫度，可以使用 `temperature` 參數。例如，想設定溫度為 0.5，可這樣做：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，溫度越接近 1.0，輸出變化越大。

- **推理模型不使用 `temperature`<strong>。這是 2026 年的重要變革。微軟 Foundry 上目前非棄用的模型都是 </strong>推理模型<strong>（GPT-5 家族、o 系列），他們 </strong>不支援 `temperature` 也不支援 `top_p`**（也不支援 `max_tokens`，請用 `max_output_tokens`）。如果你對 `gpt-5-mini` 傳送 `temperature` 參數，會收到「參數不支援」錯誤。所以如果想試上面溫度示例，要用仍支援抽樣控制的模型——例如開放的 **Llama** 模型，如來自 [Microsoft Foundry 模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 的 `Llama-3.3-70B-Instruct`，透過 Foundry Models / Azure AI 推理端點呼叫（與 `githubmodels-*` 範例相同方式）。像 GPT-5 這類推理模型的輸出控制，改用其他方式：
  - <strong>提示工程</strong> - 清楚的指示、範例和結構化輸出（請參考課程 [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)）取代了過去的抽樣調整功能。
  - <strong>推理控制</strong> - 使用諸如推理努力或冗長度等參數，在推理深度與延遲和成本之間做取捨。

  簡言之：`temperature`/`top_p` 在許多模型（如 Llama、Mistral、Phi 以及 GPT-4.x 家族，儘管 GPT-4.x 正在逐步棄用）仍有效，但趨勢是推理模型如 GPT-5 採用提示工程加推理控制。

## 作業

在本次作業中，你可以自由選擇要製作什麼。

以下是一些建議：

- 調整食譜產生器應用程式以進一步改進。試試溫度值和提示，看看你會創造出什麼。
- 製作一個「學習夥伴」。這個應用程式應該能回答關於某主題的問題，例如 Python，你可以設定提示像是「Python 的某某主題是什麼？」或是「示範某個主題的程式碼」等。
- 歷史機器人，讓歷史活起來，指示機器人扮演某位歷史人物，並問關於他的生平與時代的問題。

## 解答

### 學習夥伴

以下是入門提示，看看你如何使用並調整它以符合你的需求。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

這裡有一些你可以用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢核

溫度（temperature）概念是什麼？

1. 它控制輸出的隨機程度。
1. 它控制回應的字數大小。
1. 它控制使用的代幣數量。

## 🚀 挑戰

在作業中，嘗試變化溫度設定，分別設為 0、0.5 和 1。記住，0 表示變化最小，1 表示變化最大。哪個值最適合你的應用程式？

## 太棒了！繼續學習

完成本課程後，請瀏覽我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

接著前往第 7 課，我們將探討如何[打造聊天應用程式](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->