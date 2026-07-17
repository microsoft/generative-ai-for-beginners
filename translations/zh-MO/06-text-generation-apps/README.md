# 建立文字生成應用程式

[![建立文字生成應用程式](../../../translated_images/zh-MO/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(按上方圖片觀看本課程的影片)_

到目前為止，你已經在這個課程中看到一些核心概念，比如提示詞，甚至有一個完整的領域叫做「提示工程」。許多你可以互動的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持你使用提示詞來完成某些工作。

若你想要在應用程式中加入這類體驗，就需要理解提示詞、補全等概念並選擇合適的函式庫來使用。這正是你在本章節將學到的內容。

## 介紹

在本章中，你將會：

- 了解 openai 函式庫及其核心概念。
- 使用 openai 建立一個文字生成應用程式。
- 理解如何使用提示詞、溫度、代幣等概念來建立文字生成應用程式。

## 學習目標

在本課程結束時，你將能夠：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立文字生成應用程式。
- 配置你的應用程式使用更多或更少的代幣，並且調整溫度以產生不同的輸出。

## 什麼是文字生成應用程式？

通常當你建立一個應用程式時，它會有某種介面，例如下列：

- 基於指令。命令列應用程式是典型的應用程式，你輸入一個指令，應用程式便會執行任務。比方說，`git` 就是基於指令的應用程式。
- 使用使用者介面（UI）。有些應用程式有圖形使用者介面（GUI），你可以點擊按鈕、輸入文字、選擇選項等。

### 命令列和 GUI 應用程式的限制

與你直接輸入指令的應用程式比較：

- <strong>受限</strong>。你不能隨便打任何指令，只能用應用程式支持的指令。
- <strong>特定語言</strong>。有些應用程式支持多種語言，但預設情況下是為某一種語言設計，即使你可以加裝更多語言支持。

### 文字生成應用程式的好處

那麼文字生成應用程式有什麼不同呢？

在文字生成應用程式中，你擁有更多彈性，不受限於一組固定的指令或特定輸入語言。你可以用自然語言來與應用程式互動。另一個好處是，你已經在與一個經過大量資訊語料訓練過的資料來源互動，而傳統應用程式可能只受限於資料庫裡的內容。

### 用文字生成應用程式可以做什麼？

你可以建立很多類型的東西，例如：

- <strong>聊天機器人</strong>。一個能回答問題的聊天機器人，像是關於你的公司和產品的問題，是很好的應用。
- <strong>助手</strong>。大型語言模型（LLM）很擅長摘要文字、從文字中獲得洞見、生成文字如履歷等。
- <strong>程式碼助手</strong>。視所使用的語言模型而定，你可以建造一個幫助寫程式碼的程式碼助手。例如，你可以使用 GitHub Copilot 或 ChatGPT 來幫助你編寫程式碼。

## 怎麼開始？

好的，你需要找到一種方式與大型語言模型整合，通常有以下兩種方法：

- 使用 API。你構造帶有提示詞的網路請求，然後獲得生成的文字回應。
- 使用函式庫。函式庫幫助封裝 API 調用，使使用更加簡便。

## 函式庫/SDK

有幾個知名的函式庫用於與大型語言模型互動，例如：

- **openai**，這個函式庫讓你輕鬆連接到模型並發送提示詞。

還有一些運作在更高層次的函式庫，如：

- **Langchain**。Langchain 是知名的函式庫，並且支持 Python。
- **Semantic Kernel**。Semantic Kernel 是微軟推出的函式庫，支持 C#、Python 和 Java。

## 使用 openai 建立第一個應用程式

讓我們看看怎麼建立第一個應用程式，需要哪些函式庫，需求有多大等等。

### 安裝 openai

有很多函式庫可以用來與 OpenAI 或 Azure OpenAI 互動。你也可以使用多種程式語言，如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` Python 函式庫，因此將用 `pip` 來安裝它。

```bash
pip install openai
```

### 建立資源

你需要完成以下步驟：

- 在 Azure 上建立帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 取得 Azure OpenAI 的權限。前往 [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 申請權限。

  > [!NOTE]
  > 撰寫本文時，你需要申請 Azure OpenAI 的使用權限。

- 安裝 Python <https://www.python.org/>
- 已建立 Azure OpenAI 服務資源。請參考此指南以了解如何[建立資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找出 API 金鑰和端點

此時，你需要告訴 `openai` 函式庫使用哪個 API 金鑰。前往你的 Azure OpenAI 資源中的「Keys and Endpoint」部分，複製「Key 1」的值。

![Azure 入口網站中的 Keys and Endpoint 資源頁面](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已複製了這些資訊，讓我們來指示函式庫使用它們。

> [!NOTE]
> 將 API 金鑰與程式碼分開存放是值得的。你可以使用環境變數來達成這點。
>
> - 設定環境變數 `OPENAI_API_KEY` 給你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 設定 Azure 配置

若你使用 Azure OpenAI（現為 Microsoft Foundry 的一部分），設定方式如下。我們使用標準的 `OpenAI` 用戶端，指向 Azure OpenAI 的 `/openai/v1/` 端點，該端點適用於 Responses API 且不需要 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上述設定了以下項目：

- `api_key`，這是你在 Azure 入口網站或 Microsoft Foundry 入口網站找到的 API 金鑰。
- `base_url`，這是你的 Foundry 資源端點，後面加上 `/openai/v1/`。穩定的 v1 端點適用於 OpenAI 和 Azure OpenAI，不用管理 `api_version`。

> [!NOTE] > `os.environ` 讀取環境變數。你可以用它讀取像是 `AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT` 的環境變數。請在終端機設定這些環境變數，或使用像 `dotenv` 的函式庫。

## 產生文字

產生文字的方法是使用 Responses API 的 `responses.create` 方法。例如：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # 這是您的模型部署名稱
    input=prompt,
    store=False,
)
print(response.output_text)
```

以上程式碼示範我們建立一個回應並傳入想用的模型和提示詞。接著我們用 `response.output_text` 列印生成的文字。

### 多輪對話

Responses API 非常適合單輪文字生成和多輪聊天機器人——你可在 `input` 中提供一串訊息，建立對話：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

這項功能會在後面章節詳細介紹。

## 練習 - 你的第一個文字生成應用程式

現在我們學會如何設定並配置 openai，是時候建立你的第一個文字生成應用程式。按下列步驟操作：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你是使用 Windows，請輸入 `venv\Scripts\activate`，而非 `source venv/bin/activate`。

   > [!NOTE]
   > 到 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 搜尋 `Open AI`，點選 `Open AI resource`，再點選 `Keys and Endpoint`，複製 `Key 1` 的值。

1. 建立一個 _app.py_ 檔案，並加入以下程式碼：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 加入您的完成程式碼
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 發出請求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 印出回應
   print(response.output_text)
   ```

   > [!NOTE]
   > 如果你使用純 OpenAI（非 Azure），請使用 `client = OpenAI(api_key="<replace this value with your OpenAI key>")`（不帶 `base_url`），並且傳入模型名稱如 `gpt-5-mini` 而非部署名稱。

   你應該會看到如下輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示詞，針對不同用途

現在你已經看到如何使用提示詞生成文字。你的程式已經可以運行，你也可以修改它產生不同類型的文字。

提示詞可以用於各種任務。例如：

- <strong>生成某種類型的文字</strong>。比如你可以生成詩歌、測驗題目等。
- <strong>查找資訊</strong>。你可以用提示詞來查找資訊，例如以下問題「CORS 在網頁開發中是什麼意思？」。
- <strong>產生程式碼</strong>。你可以用提示詞生成程式碼，例如開發用於驗證電子郵件的正則表達式，或甚至產生一個完整的程式，如網頁應用程式？

## 更實用的例子：食譜生成器

想像你家裡有一些材料，想煮點什麼。你需要食譜。找食譜的方式可以是用搜尋引擎，或者使用大型語言模型來幫忙。

你可以這樣撰寫提示詞：

> "展示五個含有以下材料的菜譜：雞肉、馬鈴薯和紅蘿蔔。並列出每道菜的所有用料。"

對於上述提示詞，你可能會得到類似的回應：

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

這結果很棒，我知道該煮什麼了。此時可以做的改進包含：

- 篩選出我不喜歡或過敏的材料。
- 產生購物清單，以防我家沒有所有必需材料。

針對上述情況，我們加一個額外提示詞：

> "請去除含有大蒜的食譜，因為我過敏，並用其他材料替代。另外，請根據食譜製作購物清單，考慮我家已有雞肉、馬鈴薯和紅蘿蔔。"

現在你會有如下新結果：

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

這就是你的五道菜譜，沒有提到大蒜，且有考慮你家已有材料的購物清單。

## 練習 - 建立食譜生成器

現在我們複習過一個場景，我們來寫程式碼對應此場景。操作步驟如下：

1. 使用現有的 _app.py_ 檔案為起點
1. 找到 `prompt` 變數，並將其程式碼改為以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果現在執行程式，你應該會看到類似的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 是非決定性的，每次執行程式可能得到不同結果。

   很好，我們來看看如何改進。為了更靈活，我們希望能讓代碼能改變配料與菜譜數量。

1. 按下列方式修改程式碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 把食譜數目插入提示同原材料中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試運行程式可能會長這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 透過加入過濾器和購物清單來改進

我們現在有一個能產生食譜的運作中應用程式，而且它的彈性大，因為它依賴使用者輸入，既控制食譜數量，也控制使用的材料。

進一步改進，我們希望加上以下功能：

- <strong>過濾材料</strong>。我們想過濾掉不喜歡或會過敏的材料。實現此改動，我們可以編輯現有提示詞，並在尾端加上過濾條件，像這樣：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  在上面，我們在提示詞尾端加上 `{filter}`，同時我們也捕捉使用者輸入的過濾條件值。

  執行程式時的一個範例輸入可能如下所示：

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

  如你所見，任何含牛奶的食譜已被過濾。但如果你乳糖不耐症，可能也要過濾掉含起司的食譜，因此也祈求明確的過濾條件。


- <strong>產生購物清單</strong>。我們想要產生一個購物清單，考慮我們家裡已經有的東西。

  對於這個功能，我們可以嘗試用一個提示來解決所有問題，或者把它分成兩個提示。讓我們試試後者的方法。這裡我們建議添加一個額外的提示，但要實現這個功能，我們需要把前一個提示的結果作為後一個提示的上下文。

  找到程式碼中顯示第一個提示結果的部分，並在下面添加以下程式碼：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 列印回應
  print("Shopping list:")
  print(response.output_text)
  ```

  注意以下幾點：

  1. 我們正在構造一個新的提示，將第一個提示的結果加入到新提示中：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們發出一個新請求，但也考慮到第一次提示所要求的 token 數，因此這次設置 `max_output_tokens` 為 1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     試跑這段程式碼後，我們得到如下輸出：

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

到目前為止，我們的程式碼是可運作的，但我們還可以進行一些調整來進一步提升。有幾件事我們應該做：

- <strong>將密鑰與程式碼分離</strong>，例如 API 金鑰。密鑰不應該出現在程式碼中，應該存放在安全的位置。為了將密鑰從程式碼中分離出來，我們可以使用環境變量和像 `python-dotenv` 這樣的庫從檔案中載入。程式碼範例如下：

  1. 建立一個 `.env` 檔案，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，若使用 Microsoft Foundry 的 Azure OpenAI，需設置以下環境變量：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     在程式碼中，載入環境變量的方式如下：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **關於 token 長度的一句話**。我們需要考慮產生所需文字用的 token 數量。token 是要花費資源的，所以能節省使用 token 的地方就盡量節省。例如，我們能不能學會如何修改提示以使用較少 token？

  要改變使用的 token 數，可以使用 `max_output_tokens` 參數。例如，若要使用 100 個 tokens，可以這樣設置：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **嘗試調整 temperature**。temperature 是我們目前還沒提過，但對程式表現很重要的參數。temperature 數值越高，輸出越隨機；越低，輸出越可預測。思考一下你是否需要你的輸出多樣化。

  要改變溫度，可使用 `temperature` 參數。例如，若想設定為 0.5，可以這樣做：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，越接近 1.0，輸出越多變。

- **推理模型不使用 `temperature`<strong>。這是 2026 年一個重要的轉變。目前在 Microsoft Foundry 上的非棄用模型中，是</strong>推理模型<strong>（GPT-5 系列，o-series），而且它們</strong>不支持 `temperature` 或 `top_p`**（也不支持 `max_tokens`，請使用 `max_output_tokens`）。如果你對 `gpt-5-mini` 發送 `temperature`，會得到「不支持此參數」的錯誤。所以想嘗試上面的 temperature 範例，請用還支持抽樣控制的模型——例如來自 [Microsoft Foundry 模型目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 的開放式 **Llama** 模型 `Llama-3.3-70B-Instruct`，透過 Foundry Models / Azure AI 推論端點呼叫（用法與 `githubmodels-*` 範例相同）。對於像 GPT-5 這類的推理模型，控制輸出方式有所不同：
  - <strong>提示工程</strong>——清晰的指令、範例和結構化輸出（參見課程 [04 - 提示工程基礎](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)）完成了原本抽樣控制的工作。
  - <strong>推理控制</strong>——使用像推理努力/冗長度之類的參數來權衡推理深度、延遲和成本。

  簡言之：`temperature`/`top_p` 依然在很多模型（Llama、Mistral、Phi 和 GPT-4.x 系列——雖然 GPT-4.x 正在逐步淘汰）上有效，但趨勢是推理模型如 GPT-5 會以提示工程和推理控制為主。

## 作業

這次作業，你可以自由選擇要開發什麼。

以下是一些建議：

- 調整食譜生成器應用，進一步改進它。嘗試不同的 temperature 值和提示，看看能產出什麼結果。
- 建立一個「學習夥伴」。此應用應能回答有關某個主題的問題，例如 Python，你可以有提示像是「Python 中某個主題是什麼？」或請它顯示某個主題的程式碼等。
- 歷史機器人，讓歷史活起來，指示機器人扮演某個歷史人物，並問它有關該人物生平與時代的問題。

## 解決方案

### 學習夥伴

以下是起步提示，看看你如何使用它並調整成你喜歡的樣子。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

這是一些你可以用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢測

temperature 這個概念有什麼功能？

1. 它控制輸出的隨機程度。
1. 它控制回應的篇幅大小。
1. 它控制使用多少 tokens。

## 🚀 挑戰

在做作業時，試著變化 temperature，設為 0、0.5 和 1。記住 0 是最不變化，1 是變化最多。哪個數值對你的應用最好？

## 做得好！繼續學習

完成本課後，請參考我們的 [生成式 AI 學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

前往第七課，了解如何[建構聊天應用程式](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->