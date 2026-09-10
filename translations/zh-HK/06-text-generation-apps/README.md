# 建立文字生成應用程式

[![建立文字生成應用程式](../../../translated_images/zh-HK/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(點擊上方圖片觀看本課程影片)_

到目前為止，你已經看到課程中有核心概念像是提示詞（prompts），甚至有整個領域稱為「提示工程」。許多你可以互動的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持你用提示詞來完成任務。

若你想在應用程式中加入這樣的體驗，你需要理解提示詞、完成結果等概念，並選擇一個合適的函式庫來使用。這正是你將在本章學到的內容。

## 介紹

在本章節中，你將會：

- 認識 openai 函式庫及其核心概念。
- 使用 openai 建立一個文字生成應用程式。
- 了解如何使用提示詞、溫度（temperature）和代幣（tokens）等概念來建立文字生成應用程式。

## 學習目標

本課結束時，你將能夠：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立文字生成應用程式。
- 設定你的應用程式以控制使用較多或較少代幣，並更改溫度以產生多樣化輸出。

## 什麼是文字生成應用程式？

通常當你建立一個應用程式時，它會有某種介面像以下這些：

- 指令式。命令列應用程式是典型的應用程式，你輸入一個命令，它便執行任務。例如，`git` 是一個指令式應用程式。
- 使用者介面（UI）。有些應用程式有圖形使用者介面（GUI），你可以點擊按鈕、輸入文字、選擇選項等。

### 命令列和 UI 應用程式的限制

與指令式應用程式比擬，你輸入命令：

- <strong>受限的</strong>。你不能隨意輸入任意命令，只有應用程式支持的命令才能使用。
- <strong>語言限制</strong>。某些應用程式支持多語言，但預設是針對特定語言建置，即使可以添加更多語言支援。

### 文字生成應用程式的優點

那麼文字生成應用程式有何不同？

在文字生成應用程式中，你擁有更多彈性，不受限於既定指令集合或特定輸入語言。你可以用自然語言與應用互動。另一個好處是你已經在使用一個基於龐大語料庫訓練的資料來源，而傳統應用程式往往受限於數據庫中的內容。

### 我可以用文字生成應用程式做什麼？

你可以建立很多東西，例如：

- <strong>聊天機器人</strong>。一個針對公司和產品主題回答問題的聊天機器人將會非常合適。
- <strong>助手</strong>。大型語言模型（LLM）非常擅長總結文本、從文字中萃取見解、生成文字如履歷等。
- <strong>程式輔助</strong>。根據使用的語言模型，你可以構建程式碼助手來幫你寫程式碼。例如，你可以使用 GitHub Copilot 或 ChatGPT 來協助編寫程式碼。

## 如何開始？

你需要找到整合大型語言模型的方式，通常有以下兩種方法：

- 使用 API。你構造帶有提示詞的網路請求並取得生成的文字。
- 使用函式庫。函式庫封裝了 API 呼叫，使它們更容易使用。

## 函式庫/SDK

有幾個知名函式庫用於操作大型語言模型，例如：

- **openai**，這個函式庫讓你輕鬆連接模型並發送提示詞。

還有一些更高階的函式庫：

- **Langchain**。Langchain 知名且支援 Python。
- **Semantic Kernel**。Semantic Kernel 是微軟的函式庫，支援 C#、Python 與 Java。

## 使用 openai 建立第一個應用程式

讓我們看看如何建立第一個應用程式，需要什麼函式庫和配置需求。

### 安裝 openai

市面上有許多函式庫可以用於互動 OpenAI 或 Azure OpenAI，也可用多種程式語言如 C#、Python、JavaScript、Java 等。我們選擇使用 Python 的 `openai` 函式庫，並用 `pip` 安裝它。

```bash
pip install openai
```

### 建立資源

你需要完成以下步驟：

- 在 Azure 上建立一個帳號 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 取得 Azure OpenAI 訪問權限。進入 [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 申請訪問權限。

  > [!NOTE]
  > 編寫時，使用者需申請 Azure OpenAI 訪問權限。

- 安裝 Python <https://www.python.org/>
- 建立 Azure OpenAI 服務資源。請參考此指南了解如何[建立資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰和端點

現在你需要讓 `openai` 函式庫知道使用哪個 API 金鑰。進入 Azure OpenAI 資源的「金鑰與端點」區，複製「金鑰 1」的值。

![Azure Portal 中的金鑰與端點資源視窗](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已複製這些資訊，讓我們教函式庫如何使用它們。

> [!NOTE]
> 將 API 金鑰與程式碼分離是值得的。可以透過環境變數來實現。
>
> - 設定環境變數 `OPENAI_API_KEY` 為你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### Azure 設定配置

如果你使用 Azure OpenAI（現為 Microsoft Foundry 的一部分），設定配置方法如下。我們使用標準 `OpenAI` 用戶端，指向 Azure OpenAI 的 `/openai/v1/` 端點，該端點使用回應 API 不需指定 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

以上我們設定了：

- `api_key`，你在 Azure 入口網站或 Microsoft Foundry 入口網站找到的 API 金鑰。
- `base_url`，你的 Foundry 資源端點，後面加上 `/openai/v1/`。穩定的 v1 端點可同時用於 OpenAI 和 Azure OpenAI，不用管理 `api_version`。

> [!NOTE] > `os.environ` 用來讀取環境變數。你可以用它讀取如 `AZURE_OPENAI_API_KEY` 及 `AZURE_OPENAI_ENDPOINT` 等環境變數，設定這些變數可在終端機或用 `dotenv` 之類的函式庫完成。

## 生成文字

生成文字的方法是使用回應 API 的 `responses.create` 方法。範例如下：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # 這是你的模型部署名稱
    input=prompt,
    store=False,
)
print(response.output_text)
```

以上程式中，我們建立了一個回應並指定要使用的模型及提示詞，然後通過 `response.output_text` 輸出生成文字。

### 多輪對話

回應 API 適合單輪文字生成和多輪聊天機器人 — 你在 `input` 中提供訊息列表來建立對話：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

更多此功能細節將於後續章節介紹。

## 練習 - 你的第一個文字生成應用程式

熟悉如何設定和配置 openai 後，現在是時候建立你的第一個文字生成應用程式。請執行以下步驟：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows 使用者請輸入 `venv\Scripts\activate`，而非 `source venv/bin/activate`。

   > [!NOTE]
   > 透過 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 找到你的 Azure OpenAI 金鑰，搜尋 `Open AI`，選擇 `Open AI 資源`，再點選 `金鑰及端點`，複製 `金鑰 1`。

1. 新增一個 _app.py_ 檔案，並寫入以下程式碼：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 新增你的完成代碼
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 發出請求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 輸出回應
   print(response.output_text)
   ```

   > [!NOTE]
   > 若使用純 OpenAI（非 Azure 版本），請用 `client = OpenAI(api_key="<替換為你的 OpenAI 金鑰>")`（無需 `base_url`），並傳入模型名稱如 `gpt-5-mini` 來取代部署名。

   你應該會看到類似以下輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型提示詞，搭配不同任務

現在你已了解如何透過提示詞生成文字。你甚至有一個正在運行的程式，可修改以生成不同類型的文字。

提示詞可用於各種任務，例如：

- <strong>生成特定類型的文字</strong>。例如，可以生成詩歌、測驗問題等。
- <strong>查詢資訊</strong>。你可以用提示詞查詢資訊，如例子「在網頁開發中 CORS 是什麼意思？」。
- <strong>生成程式碼</strong>。你可以用提示詞生成程式碼，例如開發用於驗證電子郵件的正則表達式，或者生成一個完整程式如網頁應用程式。

## 更實用的用例：食譜生成器

想像你家裡有一些材料，想做料理。此時你需要食譜。你可以用搜尋引擎找，也可以用大型語言模型來做這件事。

你可以寫以下提示詞：

> 「告訴我用以下食材做菜的 5 個食譜：雞肉、馬鈴薯和胡蘿蔔。並列出每個食譜所用的全部材料」

根據以上提示詞，你可能會得到類似以下的回答：

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

這個結果很棒，我知道該煮什麼了。接下來有用的改進是：

- 過濾我不喜歡或過敏的食材。
- 製作購物清單，以防家裡沒有的食材。

針對上述情況，我們加入額外的提示詞：

> 「請移除包含蒜頭的食譜，因為我會過敏，並替換成其他食材。還請根據這些食譜產生購物清單，並考慮我家已有的雞肉、馬鈴薯和胡蘿蔔。」

現在你會看到新的結果，像是：

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

這是你的五個食譜，沒有蒜頭，還有針對你現有食材的購物清單。

## 練習 - 建立食譜生成器

既然模擬了情境，我們動手寫程式碼實現剛才的示範。請依下列步驟操作：

1. 使用現有的 _app.py_ 檔做為起點
1. 找到變數 `prompt`，將其程式碼變更為以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   執行程式後，你應該可以看到類似以下的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 非確定性，因此同一程式多次執行可能有不同結果。

   很好，我們來看看如何改進。為了改進，希望讓程式更有彈性，可以更改食材和食譜數量。

1. 請如以下方式修改程式碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 將食譜數量和材料插入提示中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試執行的程式碼範例如下：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 加入過濾器和購物清單的改進

現在我們有一個可用的應用程式，能根據使用者輸入的配料和食譜數量來生成食譜，具備彈性。

再進一步改進，我們想要加入：

- <strong>過濾食材</strong>。我們希望能過濾掉不喜歡或過敏的食材。實現方法是修改提示詞，在結尾加入過濾條件，如下：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  以上在提示詞末尾加了 `{filter}`，並且從使用者獲取過濾條件的值。

  執行程式時的輸入示例如下：

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

  如你所見，含有牛奶的食譜被過濾掉了。不過若你是乳糖不耐症，可能還想把含乳酪的食譜也過濾掉，因此要明確表達過濾條件。


- <strong>製作購物清單</strong>。我們想要製作一個購物清單，考慮我們家中已經擁有的物品。

  對於這個功能，我們可以嘗試在一個提示中解決所有問題，或者將其拆分成兩個提示。讓我們嘗試後者。在這裡，我們建議添加一個額外的提示，但要達成這個目的，我們需要將前一個提示的結果作為上下文加入到後一個提示中。

  找到在代碼中打印第一個提示結果的部分，並在其下方添加以下代碼：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 列印回應
  print("Shopping list:")
  print(response.output_text)
  ```

  請注意以下事項：

  1. 我們通過將第一個提示的結果加入到新提示中來構建新的提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們再次發出請求，但也考慮到我們在第一個提示中要求的令牌數，因此這次將 `max_output_tokens` 設置為1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     運行這段代碼，我們現在得到以下輸出：

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

到目前為止，我們已有的代碼是可行的，但仍有一些調整可以進一步完善。下面是一些建議的改進項目：

- <strong>將機密與代碼分離</strong>，例如 API 密鑰。機密不應該出現在代碼中，應儲存在安全的位置。為了將機密與代碼分離，我們可以使用環境變量和類似 `python-dotenv` 的庫，從文件中載入它們。代碼如下所示：

  1. 建立一個 `.env` 文件，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Microsoft Foundry 中的 Azure OpenAI，您需要設置以下環境變量：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     在代碼中，您可以這樣載入環境變量：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>關於令牌長度的一句話</strong>。我們應該考慮生成所需文字的令牌數。令牌會產生費用，因此盡可能地節省使用的令牌數。例如，我們是否可以重新表述提示，使令牌消耗更少？

  要更改使用的令牌數，可以使用 `max_output_tokens` 參數。例如，想用100個令牌時，您可以這樣做：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **試驗溫度 (temperature)**。溫度是目前還未提及但對程序表現很重要的參數。溫度值越高，輸出越隨機；溫度值越低，輸出越可預測。請考慮您想要輸出有多少變化量。

  要調整溫度，您可以使用 `temperature` 參數。例如，想用 0.5 的溫度值時，可以這樣做：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，越接近 1.0 輸出越多樣化。

- **推理模型不使用 `temperature`<strong>。這是2026年的一項重要變革。Microsoft Foundry 上目前的非棄用模型是 </strong>推理模型<strong>（GPT-5 家族、o 系列）——它們 </strong>不支援 `temperature` 或 `top_p`**（也不支援 `max_tokens`，請使用 `max_output_tokens`）。如果向 `gpt-5-mini` 傳送 `temperature`，您會收到「不支援此參數」的錯誤。要嘗試溫度範例，請選擇仍支持抽樣控制的模型——例如來自 [Microsoft Foundry 模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 的開源 **Llama** 模型，如 `Llama-3.3-70B-Instruct`，可通過 Foundry Models / Azure AI 推理端點調用（與 `githubmodels-*` 範例相同）。對於如 GPT-5 的推理模型，您需要用其他方式引導輸出：
  - <strong>提示工程</strong> - 明確指示、範例及結構化輸出（參見課程[04 - 提示工程基礎](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)）可替代過去抽樣控制的工作。
  - <strong>推理控制</strong> - 參數如推理努力/詳盡度在推理深度與延遲和成本間取捨。

  簡言之：`temperature`/`top_p` 在許多模型（Llama、Mistral、Phi 和 GPT-4.x 家族，儘管 GPT-4.x 正在棄用）仍然有效，但未來趨勢是推理模型如 GPT-5 上以提示工程和推理控制為主導。

## 作業

本次作業您可以選擇要構建的項目。

以下是一些建議：

- 優化食譜生成器應用，嘗試調整溫度參數和提示，看看能創造什麼新效果。
- 製作一個「學習夥伴」。該應用能回答特定主題的問題，例如 Python，您可以使用類似「Python的某個主題是什麼？」的提示，或請它顯示某個主題的範例代碼。
- 歷史機器人，讓歷史活現眼前，指示機器人扮演某個歷史人物，並向它提問此人物的生平與時代。

## 解決方案

### 學習夥伴

以下是一個起始提示，看看如何使用及調整它以符合您的喜好。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

以下是一些您可以使用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢測

溫度參數 (temperature) 有什麼作用？

1. 它控制輸出的隨機程度。
1. 它控制回應的長度。
1. 它控制使用的令牌數。

## 🚀 挑戰

在完成作業時，嘗試變化溫度，設定為 0、0.5 和 1。記得 0 表示最不變化，1 表示變化最多。哪個值對您的應用最合適？

## 做得好！繼續學習

完成本課後，請查看我們的[生成式 AI 學習集錦](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

前往第七課，我們將探討如何[構建聊天應用](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->