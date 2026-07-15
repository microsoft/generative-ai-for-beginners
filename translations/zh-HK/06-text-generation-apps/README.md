# 建立文字生成應用程式

[![建立文字生成應用程式](../../../translated_images/zh-HK/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(點擊上方圖片觀看此課程影片)_

到目前為止，你已在這個課程中看到有一些核心概念，例如 prompts，甚至有一整個名為「prompt engineering」的學科。許多你能互動的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，皆支援你使用 prompts 來完成某些任務。

若你想在應用程式中加入這樣的體驗，需要了解 prompts、completions 等概念，並選擇一個合適的函式庫來使用。這正是你在本章節將學到的內容。

## 介紹

在本章節中，你將會：

- 了解 openai 函式庫及其核心概念。
- 使用 openai 建立一個文字生成應用程式。
- 理解如何使用 prompt、temperature、tokens 等概念來建立文字生成應用程式。

## 學習目標

在本課結束後，你將能夠：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立文字生成應用程式。
- 配置你的應用程式使用更多或更少的 tokens，並改變 temperature 以產生多樣的輸出。

## 什麼是文字生成應用程式？

通常你建立的應用程式具有某種形式的介面，例如：

- 基於命令的。Console 應用程式是典型的命令式應用，你輸入指令，它執行任務。舉例來說，`git` 就是基於命令的應用。
- 使用者介面（UI）。有些應用有圖形使用介面（GUIs），你可按按鈕、輸入文字、選擇選項等等。

### Console 與 UI 應用的限制

比較一下基於命令的應用，你需要輸入指令：

- <strong>它有限制</strong>。你不能隨便輸入任何指令，僅能使用應用支援的指令。
- <strong>語言特定</strong>。某些應用支援多語言，但預設是專為特定語言建置，即使你可以加入更多語言支援。

### 文字生成應用的好處

那麼文字生成應用有何不同呢？

文字生成應用更具彈性，你不受限於特定一組指令或輸入語言，而是可以使用自然語言與應用互動。另一項好處是你已經在使用一個經過大量資料訓練的資料來源，而傳統應用可能只限於資料庫內的內容。

### 我可以用文字生成應用做什麼？

你可以建立許多應用，舉例：

- <strong>聊天機器人</strong>。回答有關主題問題的聊天機器人，例如你的公司與產品，是個不錯的應用。
- <strong>助手</strong>。大型語言模型 (LLMs) 擅長文本摘要、資訊洞察、產生如履歷等文字內容。
- <strong>程式碼助理</strong>。依據你使用的語言模型，可建立程式碼助理幫助你編寫程式碼。例如 GitHub Copilot 以及 ChatGPT 都能協助寫程式。

## 如何開始？

你需要找到一種方式整合大型語言模型 (LLM)，通常有兩種作法：

- 使用 API。藉由構造你的 prompt 的網路請求，並取得生成的文字回應。
- 使用函式庫。函式庫包裝 API 呼叫，讓使用更容易。

## 函式庫 / SDK

有幾個知名的 LLM 函式庫，如：

- **openai**，這個函式庫方便連接你的模型並送出 prompts。

另外還有更高階的函式庫：

- **Langchain**。Langchain 很知名且支援 Python。
- **Semantic Kernel**。Semantic Kernel 是微軟的函式庫，支援 C#、Python 和 Java。

## 使用 openai 的第一個應用程式

讓我們來看看如何建立第一個應用程式，需要哪些函式庫、多少準備工作等等。

### 安裝 openai

市面上有許多函式庫可用於與 OpenAI 或 Azure OpenAI 互動。你也可以使用多種程式語言，如 C#、Python、JavaScript、Java 等。我們選擇使用 Python 的 `openai` 函式庫，並用 `pip` 安裝。

```bash
pip install openai
```

### 建立資源

你需要進行以下步驟：

- 在 Azure 上建立帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 申請 Azure OpenAI 的存取權限。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 申請。

  > [!NOTE]
  > 撰寫本文時，需要申請 Azure OpenAI 存取權。

- 安裝 Python <https://www.python.org/>
- 完成 Azure OpenAI 服務資源的建立。請參考此指引了解如何 [建立資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找出 API 金鑰與端點

這時候，你需要告訴 `openai` 函式庫要使用哪個 API 金鑰。前往你的 Azure OpenAI 資源的「Keys and Endpoint」區塊，複製「Key 1」的值作為 API 金鑰。

![Azure Portal 中 Keys and Endpoint 資源視窗](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你有這些資訊，讓我們指示函式庫使用它們。

> [!NOTE]
> 將 API 金鑰與程式碼分開管理是值得做的事。你可以透過環境變數來實現。
>
> - 設定環境變數 `OPENAI_API_KEY` 為你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 設定 Azure 配置

如果你使用 Azure OpenAI（現為 Microsoft Foundry 的一部分），以下是配置方式。我們使用標準的 `OpenAI` 用戶端指向 Azure OpenAI 的 `/openai/v1/` 端點，這適用於 Responses API 且不需指定 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上面設定了以下內容：

- `api_key`，就是在 Azure Portal 或 Microsoft Foundry 入口找到的 API 金鑰。
- `base_url`，你的 Foundry 資源端點加上 `/openai/v1/`。穩定版的 v1 端點在 OpenAI 與 Azure OpenAI 通用，不用管理 `api_version`。

> [!NOTE] > `os.environ` 會讀取環境變數。你可以用它讀取如 `AZURE_OPENAI_API_KEY` 與 `AZURE_OPENAI_ENDPOINT`。請在終端機或使用 `dotenv` 類函式庫設定這些環境變數。

## 產生文字

產生文字的方式是使用 Responses API 的 `responses.create` 方法。範例如下：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # 這是你的模型部署名稱
    input=prompt,
    store=False,
)
print(response.output_text)
```

在上述程式中，我們建立一個回應並傳入要使用的模型及 prompt。然後透過 `response.output_text` 輸出生成的文字。

### 多輪對話

Responses API 適合用來建立單輪文字生成及多輪聊天機器人——你可在 `input` 參數中傳入多則訊息清單，構建對話：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

本功能會在後續章節進一步說明。

## 練習 - 你的第一個文字生成應用程式

現在我們已了解如何設定及配置 openai，接著是建立你的第一個文字生成應用程式。請按以下步驟操作：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 若你使用 Windows，指令為 `venv\Scripts\activate`，而非 `source venv/bin/activate`。

   > [!NOTE]
   > 在 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 搜尋 `Open AI`，選擇 `Open AI resource`，再選「Keys and Endpoint」，複製 `Key 1` 的值找到你的 Azure OpenAI 金鑰。

1. 建立一個 _app.py_ 檔案，並寫入以下程式碼：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 加入你的完成代碼
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 發出請求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 列印回應
   print(response.output_text)
   ```

   > [!NOTE]
   > 若使用純 OpenAI（非 Azure），請用 `client = OpenAI(api_key="<replace this value with your OpenAI key>")`（不帶 `base_url`），並傳入像 `gpt-4o-mini` 這樣的模型名稱，而非部署名稱。

   你會看到像是以下的輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同種類的 prompt，應用不同需求

現在你已了解如何用 prompt 生成文字。你甚至已經有一個運作中的程式，能修改生成不同類型的文字。

Prompts 可以應用於各種任務，例如：

- <strong>產生特定類型文字</strong>。例如，詩歌、測驗題目等。
- <strong>查詢資訊</strong>。用 prompt 查找資訊，如「CORS 在網頁開發中是什麼意思？」。
- <strong>生成程式碼</strong>。利用 prompt 產生程式碼，例如製作用來驗證電子郵件的正則表達式，甚至整個程式，如網頁應用程式。

## 更實用的案例：食譜生成器

假設你家中有食材，想做菜，但你需要食譜。你可以用搜尋引擎找，或者用 LLM 來幫忙。

你可以寫出這樣的 prompt：

>「請給我 5 道包含以下食材的菜譜：雞肉、馬鈴薯、紅蘿蔔。每道菜請列出所有使用的食材。」

依照上述 prompt，你可能得到像是：

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

這結果不錯，我知道要做什麼了。接著可優化的點為：

- 篩除我不喜歡或過敏的食材。
- 生成購物清單，考慮我家中已有食材不足時。

對以上狀況，我們可以加個額外的 prompt：

>「請移除含有蒜的食譜，因為我過敏，並用其它食材替代。請同時針對這些食譜產生購物清單，考慮我家裡已經有雞肉、馬鈴薯與紅蘿蔔。」

現在你會得到一個新的結果：

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

這就是你想要的五道無蒜食譜，且附上購物清單，已考慮家裡現有食材。

## 練習 - 建立食譜生成器

展開場景後，讓我們著手編寫對應的程式。請按以下步驟操作：

1. 以現有的 _app.py_ 檔案作為起點
1. 找出 `prompt` 變數，將其內容改成以下程式碼：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   若你現在執行程式，應該可以看到類似的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 是非確定性的，每次執行結果可能不同。

   很好，接著我們來看看怎麼改進。為了讓程式更具彈性，我們想要讓食材與食譜數量都能被調整。

1. 接著調整程式內容如下：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 將食譜數量插入提示和材料中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   執行測試的程式碼範例如下：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 進階改良：加上過濾及購物清單功能

我們已有一個可以正常產出食譜的應用，而且它也靈活，因為使用者能輸入食譜數量與使用的食材。

為了更進一步提升，我們希望加入：

- <strong>過濾食材</strong>。我們希望能過濾不喜歡或會過敏的食材。要達成此目標，我們可以編輯既有的 prompt，在最後加入過濾條件，如下：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  如上，我們在 prompt 後附加 `{filter}`，並自使用者取得過濾條件。

  執行程式時的輸入範例如下：

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

  如你所見，任何含牛奶的食譜被過濾掉了。但如果你乳糖不耐症，也可能想過濾起司類食譜，因此需要清楚指示。


- <strong>製作購物清單</strong>。我們想製作一份購物清單，並考慮家中已有的物品。

  對於這個功能，我們可以嘗試用一個提示解決所有問題，或者將其拆分成兩個提示。讓我們嘗試後者的方法。這裡我們建議添加一個額外的提示，但要使其運作，我們需要將前一個提示的結果作為上下文添加到後一個提示中。

  找出程式碼中列印出第一個提示結果的部分，並在其下方加入以下程式碼：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 輸出回應
  print("Shopping list:")
  print(response.output_text)
  ```

  注意以下事項：

  1. 我們正在構造一個新的提示，將第一個提示的結果加入新提示中：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們發出新的請求，但也考慮到第一次提示請求的令牌數量，因此這次 `max_output_tokens` 設為 1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     運行這段程式碼後，我們得到了如下輸出：

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

到目前為止，我們有一段可運作的程式碼，但還有一些調整可做以進一步改善。以下是一些應該採取的措施：

- <strong>將機密與程式碼分離</strong>，例如 API 金鑰。機密不應該寫在程式碼中，而應該保存在安全位置。為了將機密與程式碼分離，我們可以使用環境變數及像 `python-dotenv` 這樣的庫從檔案載入它們。程式碼如下範例：

  1. 建立一個 `.env` 檔並填入以下內容：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Microsoft Foundry 裡的 Azure OpenAI，你需要設定以下環境變數：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     在程式碼中，你可以這樣載入環境變數：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>關於令牌長度</strong>。我們應該考慮生成想要文字所需的令牌數量。令牌會花費金錢，因此盡可能要節省使用的令牌數量。例如，有沒有辦法讓提示語更精簡，使用更少的令牌？

  要改變使用的令牌數量，可以使用 `max_output_tokens` 參數。例如，如果想使用 100 個令牌，可以這樣設置：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- <strong>嘗試溫度參數</strong>。溫度是我們之前未提及，但對程式表現很重要的參數。溫度值越高，輸出越隨機。反之，溫度越低，輸出越可預測。請考慮你是否希望輸出帶有變化。

  要更改溫度，可以使用 `temperature` 參數。例如，若想設置溫度為 0.5，可以這樣設定：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，越接近 1.0，輸出變化越大。

## 作業

在這個作業中，你可以自行選擇要打造的作品。

這裡有一些建議：

- 調整食譜生成器應用，讓它變得更好。嘗試修改溫度值和提示內容，看看能做出什麼。
- 建立一個「學習夥伴」。此應用應能回答有關主題的問題，例如 Python，你可能會有「Python 中某個主題是什麼？」這類提示，或者希望它展示某個主題的程式碼等。
- 歷史機器人，讓歷史變得生動，指示機器人扮演某個歷史人物，並向它提問該人物的生活與時代背景。

## 解答

### 學習夥伴

以下是一個起始提示，看看你如何使用它並根據喜好做調整。

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

## 知識檢測

溫度參數的作用是什麼？

1. 它控制輸出的隨機程度。
1. 它控制回應的長度。
1. 它控制使用的令牌數量。

## 🚀 挑戰

在完成作業時，試著調整溫度，設成 0、0.5 和 1。記得 0 是最不變化，1 是變化最多。哪個值對你的應用最有效？

## 做得好！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

前往第 7 課，我們將探討如何[建立聊天應用程式](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->