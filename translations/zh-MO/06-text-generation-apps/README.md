# 建立文本生成應用程式

[![建立文本生成應用程式](../../../translated_images/zh-MO/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(點擊上方圖片觀看本課程影片)_

到目前為止，你已在此課程中看到關於提示詞等核心概念，甚至還有一門完整的學科稱為「提示工程」。許多你可以互動的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，都支援你透過提示詞來完成某些任務。

若你想要把這種體驗加入到應用程式中，就需要了解像是提示詞、補全等概念，並選擇適合的函式庫合作。這正是你會在本章學習的內容。

## 介紹

在本章，你將會：

- 瞭解 openai 函式庫及其核心概念。
- 使用 openai 建立文本生成應用程式。
- 瞭解如何使用提示詞、溫度和代幣等概念來建立文本生成應用程式。

## 學習目標

在本課結束時，你將能夠：

- 解釋什麼是文本生成應用程式。
- 使用 openai 建立文本生成應用程式。
- 設定你的應用程式使用較多或較少的代幣，也能調整溫度，以產生多樣化的輸出。

## 什麼是文本生成應用程式？

通常當你建立應用程式時，會有某種介面，像以下範例：

- 指令式。控制台應用程式是典型的指令式應用程式，你輸入指令，程式執行任務。例如，`git` 就是指令式應用程式。
- 使用者介面 (UI)。有些應用程式具備圖形使用者介面 (GUI)，你可以點按按鈕、輸入文字、選擇選項等等。

### 控制台和 UI 應用程式的限制

與你在指令式應用程式中輸入指令相比：

- <strong>有其限制</strong>。你不能隨心所欲地輸入任何指令，只能是應用程式所支援的指令。
- <strong>語言特定</strong>。有些應用支援多種語言，但預設仍是以特定語言開發，雖然你可以擴充語言支援。

### 文本生成應用程式的優點

那麼文本生成應用程式有何不同呢？

在文本生成應用程式裡，你有更多彈性，不再限於固定指令集合或特定輸入語言。你可以使用自然語言與應用程式互動。另一優點是你其實已經在與一個經過大量語料訓練的資料來源互動，而傳統應用可能只限於資料庫內的資訊。

### 我可以用文本生成應用程式做什麼？

你可以做很多事。例如：

- <strong>聊天機器人</strong>。一個回答主題問題的聊天機器人，例如關於你公司及其產品的問題，就很適合。
- <strong>助手</strong>。大型語言模型擅長摘要文本、從文本中獲得洞察、產出履歷等多種文本。
- <strong>程式碼助理</strong>。視所用模型而定，你可以建立程式碼助理幫你撰寫程式碼。例如，可以使用 GitHub Copilot 或 ChatGPT 協助寫程式。

## 如何開始？

你需要找到一個方法與大型語言模型集成，通常包含以下兩種方式：

- 使用 API。這裡你建立帶有提示詞的網路請求，取得生成的文本。
- 使用函式庫。函式庫封裝 API 呼叫，讓使用更簡便。

## 函式庫/SDK

有幾個知名的函式庫用於與大型語言模型合作，例如：

- **openai**，此函式庫讓你輕鬆連接你的模型並傳送提示詞。

還有一些運作在更高層級的函式庫，例如：

- **Langchain**。Langchain 知名且支援 Python。
- **Semantic Kernel**。Semantic Kernel 是微軟的函式庫，支援 C#、Python 和 Java。

## 使用 openai 建立第一個應用程式

讓我們看看如何建立第一個應用程式，需要哪些函式庫，以及所需資源量等。

### 安裝 openai

市面上有許多與 OpenAI 或 Azure OpenAI 互動的函式庫。你也可以使用多種程式語言，如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` Python 函式庫，因此會用 `pip` 安裝它。

```bash
pip install openai
```

### 建立資源

你需要完成以下步驟：

- 在 Azure 建立帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 取得 Azure OpenAI 權限。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 並申請權限。

  > [!NOTE]
  > 撰寫本文時，需申請 Azure OpenAI 的使用權限。

- 安裝 Python <https://www.python.org/>
- 已建立 Azure OpenAI 服務資源。請參考此指引了解如何[建立資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰與端點

現在你需要告訴 `openai` 函式庫要使用哪個 API 金鑰。請前往 Azure OpenAI 資源的「金鑰與端點」區段，複製「金鑰 1」的值。

![Azure 入口網站中的金鑰與端點資源版面](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你有了這個資訊，讓我們指示函式庫使用它。

> [!NOTE]
> 建議將你的 API 金鑰與程式碼分離。你可以透過環境變數做到這點。
>
> - 將環境變數 `OPENAI_API_KEY` 設為你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 設定 Azure 配置

如果你使用 Azure OpenAI（現為 Microsoft Foundry 一部分），設定方法如下。我們使用標準 `OpenAI` 用戶端指向 Azure OpenAI `/openai/v1/` 端點，這適用於 Responses API，且無需 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上述設定包含：

- `api_key`，你的 Azure Portal 或 Microsoft Foundry 入口網站找到的 API 金鑰。
- `base_url`，你的 Foundry 資源端點，末尾附加 `/openai/v1/`。這一穩定的 v1 端點同時支援 OpenAI 與 Azure OpenAI，無需管理 `api_version`。

> [!NOTE] > `os.environ` 用來讀取環境變數。你可用它讀取像 `AZURE_OPENAI_API_KEY` 與 `AZURE_OPENAI_ENDPOINT` 這類環境變數。可在終端機設定或使用函式庫如 `dotenv`。

## 生成文字

生成文字的方式是使用 Responses API 的 `responses.create` 方法。以下是範例：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # 這是您的模型部署名稱
    input=prompt,
    store=False,
)
print(response.output_text)
```

在上述程式中，我們建立一個回應，傳入想使用的模型與提示詞，然後透過 `response.output_text` 列印生成的文字。

### 支援多輪對話

Responses API 適合單輪文本生成和多輪聊天機器人 — 你可以在 `input` 中傳入多條訊息來構建對話：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

更多此功能內容將在接下來的章節介紹。

## 練習 - 你的第一個文本生成應用程式

現在你已學會如何設定與配置 openai，該是建立你第一個文本生成應用程式的時候。建立應用程式，請依照以下步驟：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 若使用 Windows，請輸入 `venv\Scripts\activate`，而非 `source venv/bin/activate`。

   > [!NOTE]
   > 前往 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 搜尋 `Open AI`，選擇 `Open AI 資源`，再進入「金鑰與端點」並複製 `金鑰 1` 的值。

1. 建立一個 _app.py_ 檔案並填入以下程式碼：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 添加您的完成程式碼
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 進行請求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 列印回應
   print(response.output_text)
   ```

   > [!NOTE]
   > 如果你使用純 OpenAI (非 Azure)，請改用 `client = OpenAI(api_key="<用你的OpenAI金鑰取代此值>")`（無需 `base_url`），並傳入模型名稱如 `gpt-4o-mini`，而非部署名稱。

   你應該會看到類似以下輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示詞，對不同任務

現在你已看到如何用提示詞生成文字。你甚至有一個已執行的程式，可以修改它來生成不同類型的文字。

提示詞可支援各種任務。例如：

- <strong>生成特定類型的文本</strong>。例如，詩歌、測驗問題等。
- <strong>查詢資訊</strong>。可用提示詞查詢資訊，例如「在網頁開發中 CORS 是什麼意思？」等。
- <strong>生成程式碼</strong>。可用提示詞產生程式碼，例如開發正則表達式用來驗證電子郵件，甚至直接生成整個程式，如 Web 應用程式。

## 更實用的案例：食譜生成器

想像你家裡有食材，想煮點什麼。這時候你需要食譜。尋找食譜的方法，可以用搜尋引擎，或者直接用大型語言模型。

你可以寫出如下的提示詞：

> 「列出 5 道包含以下材料的菜肴食譜：雞肉、馬鈴薯、紅蘿蔔。每道食譜列出所有食材。」

依上述提示詞，你可能會得到這樣的回應：

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

這樣的結果很好，我知道該煮什麼了。接下來有用的改進可能是：

- 過濾掉我不喜歡或過敏的食材。
- 產生購物清單，以防我家中食材不齊全。

對以上情況，我們來增加一個額外提示詞：

> 「請移除含大蒜的食譜，因為我過敏，並替換成其他材料。同時請考慮我家已有雞肉、馬鈴薯和紅蘿蔔，產生購物清單。」

現在你會得到新的結果，如下：

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

這是你的五道食譜，都不含大蒜，且你也有一張考慮現有食材的購物清單。

## 練習 - 建立食譜生成器

我們已經演示了這種情境，接著寫程式碼來實現。請依以下步驟：

1. 以現有的 _app.py_ 檔案作為起點
1. 找到 `prompt` 變數，將其程式碼改為如下：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   現在執行程式，你會看到類似輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 是非確定性的，每次執行程式結果可能不同。

   很好，讓我們看看如何改進。為了讓程式更靈活，讓食材與食譜數量都能改變與調整。

1. 我們依以下方式修改程式碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 將食譜的數量和材料插入提示中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試執行程式的程式碼，可以像這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 改進：加入過濾條件與購物清單

我們現在有一個可用應用，可產生食譜，且因為依賴使用者輸入，無論是食譜數量還是食材都相當靈活。

進一步改進，我們想加入：

- <strong>過濾食材</strong>。想能過濾掉不喜歡或過敏的食材。為了達成，我們可在現有提示詞後加上過濾條件，如下：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面我們在提示詞末尾加入 `{filter}`，並從使用者取得過濾條件值。

  執行程式的範例輸入可能如下：

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

  如你所見，任何含牛奶的食譜都被過濾掉了。但如果你乳糖不耐症，也可能想過濾掉有起司的食譜，因此需明確描述。


- <strong>製作購物清單</strong>。我哋想製作一個購物清單，考慮我哋已經喺屋企擁有嘅嘢。

  對於呢個功能，我哋可以嘗試喺一個提示入面解決所有嘢，或者將佢分拆成兩個提示。試吓後者嘅方法。呢度我哋建議加入一個額外嘅提示，但要令到呢個工作，需要將前一個提示嘅結果加到後一個提示嘅上下文入面。

  搵出代碼中打印第一個提示結果嘅部份，然後喺下面加入以下代碼：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 列印回應
  print("Shopping list:")
  print(response.output_text)
  ```

  留意以下事項：

  1. 我哋係通過將第一個提示嘅結果加入新提示，嚟構建一個新提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我哋做一個新嘅請求，同時考慮第一個提示 asked 嘅 token 數量，所以今次我哋講 `max_output_tokens` 係 1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     透過執行呢段代碼，我哋而家得到嘅輸出係：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改進你嘅設置

到目前為止，我哋寫嘅代碼係可行嘅，但有啲調整我哋應該做嚟進一步改進。可以考慮嘅嘢有：

- <strong>將機密同代碼分離</strong>，例如 API 密鑰。機密唔應該放喺代碼入面，應該儲存在安全嘅地方。為咗將機密同代碼分離，我哋可以用環境變數同埋例如 `python-dotenv` 呢啲庫去從文件加载佢哋。以下係代碼示例：

  1. 建立一個 `.env` 文件，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，喺 Microsoft Foundry 嘅 Azure OpenAI，要設定以下環境變數：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     喺代碼中，你會咁樣加载環境變數：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **關於 token 長度嘅說明**。我哋應該考慮生成文字所需嘅 token 數。Token 係要費錢嘅，所以盡量喺可能嘅情況下節省 token 使用量。例如，唔可以調整提示，使得用更少嘅 token 表達？

  要改變使用嘅 token 數，可以用 `max_output_tokens` 參數。例如你想用 100 個 token，可以咁做：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **嘗試調整 temperature**。到而家為止我哋未提及 temperature，但佢係對程序表現好重要嘅一個上下文參數。temperature 值越高，輸出結果就越隨機。相反，temperature 值越低，輸出就越可預測。考慮你想唔想令輸出有變化。

  要調整 temperature，可以用 `temperature` 參數。例如你想用 0.5 嘅 temperature，可以咁做：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，越接近 1.0，輸出越多變化。

## 任務

呢個任務，你可以自由選擇想製作乜嘢。

以下係啲建議：

- 微調食譜生成器應用，令佢變得更好。試吓調整 temperature 嘅值，亦試吓改變提示詞，睇吓可以搞出咩花樣。
- 製作一個「學習夥伴」。呢個應用要能回答關於某個主題嘅問題，例如 Python，可以用類似「Python 中乜嘢係某個話題？」嘅提示，或者有啲提示叫佢顯示某個主題嘅代碼等等。
- 歷史 Bot，令歷史活起嚟，指示 Bot 扮演某個歷史人物，問佢關於佢嘅人生同時代嘅問題。

## 解決方案

### 學習夥伴

以下係一個起步提示，睇吓你點用佢同埋按你喜好調整。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史 Bot

呢度係可以使用嘅啲提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢查

temperature 呢個概念係做咩用？

1. 控制輸出嘅隨機程度。
1. 控制回應嘅長度。
1. 控制使用嘅 token 數量。

## 🚀 挑戰

喺做任務嘅時候，試吓改變 temperature，試下設 0、0.5 同 1。記住 0 係最少變化，1 係最高變化。邊個值喺你嘅應用裡面效果最好？

## 做得好！繼續學習

完成呢課後，可以睇睇我哋嘅 [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你嘅生成式 AI 知識！

去下一課 Lesson 7，研究點樣 [製造聊天應用](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->