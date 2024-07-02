# 建構文本生成應用程式

[![建構文本生成應用程式](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(點擊上方圖片以觀看本課的影片)_

你已經透過這個課程看到了核心概念，如提示，甚至還有一個叫做「提示工程」的整個學科。許多工具如ChatGPT、Office 365、Microsoft Power Platform等，都支持你使用提示來完成某些事情。

為了讓你將這樣的體驗添加到應用程式中，你需要了解提示、完成等概念，並選擇一個函式庫來使用。這正是你在本章中將學到的內容。

## 簡介

在本章中，你將：

- 了解 openai 函式庫及其核心概念。
- 使用 openai 建構一個文字產生應用程式。
- 了解如何使用提示、溫度和代幣等概念來建構一個文字產生應用程式。

## 學習目標

在本課程結束時，你將能夠：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立一個文字生成應用程式。
- 配置你的應用程式以使用更多或更少的 tokens，並且改變溫度，以獲得多樣化的輸出。

## 什麼是文字生成應用程式?

通常當你建構一個應用程式時，它會有某種介面，如下所示:

- 基於命令。控制台應用程式是典型的應用程式，你輸入一個命令，它就會執行一個任務。例如，`git` 是一個基於命令的應用程式。
- 使用者介面 (UI)。有些應用程式有圖形使用者介面 (GUI)，你可以點擊按鈕、輸入文字、選擇選項等。

### 控制台和 UI 應用程式是有限的

將其與基於命令的應用程式進行比較，在那裡你輸入一個命令:

- **它有限制**。你不能隨便輸入任何命令，只能輸入應用程式支援的命令。
- **特定語言**。有些應用程式支援多種語言，但預設情況下應用程式是為特定語言建構的，即使你可以添加更多語言支援。

### 文字生成應用程式的好處

那麼文本生成應用程式有什麼不同呢?

在一個文本生成應用中，你有更多的靈活性，你不會被限制於一組命令或特定的輸入語言。相反，你可以使用自然語言與應用互動。另一個好處是，因為你已經在與一個經過大量資訊訓練的數據源互動，而傳統應用可能會被限制於資料庫中的內容。

### 我可以用文字生成應用程式建構什麼？

有許多事情你可以建構。例如:

- **聊天機器人**。一個回答有關主題問題的聊天機器人，比如你的公司及其產品，可能是一個很好的匹配。
- **助手**。LLM 在總結文本、從文本中獲取見解、生成像簡歷這樣的文本等方面非常出色。
- **程式碼助手**。根據你使用的語言模型，你可以建構一個幫助你編寫程式碼的程式碼助手。例如，你可以使用像 GitHub Copilot 以及 ChatGPT 這樣的產品來幫助你編寫程式碼。

## 我該如何開始？

嗯，你需要找到一種方式來整合 LLM，這通常涉及以下兩種方法：

- 使用 API。在這裡，你正在使用提示來構建網路請求並獲取生成的文本。
- 使用函式庫。函式庫有助於封裝 API 呼叫並使其更易於使用。

## 函式庫/SDKs

有一些知名的函式庫可用於處理 LLM，例如:

- **openai**，此函式庫讓連接到您的模型並發送提示變得容易。

然後有一些函式庫在更高層次上運作，例如:

- **Langchain**。Langchain 眾所周知並且支援 Python。
- **Semantic Kernel**。Semantic Kernel 是 Microsoft 的一個函式庫，支援 C#、Python 和 Java 語言。

## 第一個使用 openai 的應用程式

讓我們看看如何建構我們的第一個應用程式，需要哪些函式庫，需要多少等等。

### 安裝 openai

有許多函式庫可以與 OpenAI 或 Azure OpenAI 互動。也可以使用多種程式語言，如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` Python 函式庫，因此我們將使用 `pip` 來安裝它。

```bash
pip install openai
```

### 建立資源

你需要執行以下步驟:

- 在 Azure 上建立帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 獲取 Azure OpenAI 的存取權。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 並請求存取權。

  > [!NOTE]
  > 在撰寫本文時，您需要申請存取 Azure OpenAI。

- 安裝 Python <https://www.python.org/>
- 已建立 Azure OpenAI 服務資源。請參閱此指南了解如何[建立資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰和端點

此時，你需要告訴你的 `openai` 函式庫要使用哪個 API 金鑰。要找到你的 API 金鑰，請前往 Azure OpenAI 資源的 "Keys and Endpoint" 部分並複製 "Key 1" 值。

![金鑰和端點資源頁面在 Azure Portal 中](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已經複製了這些資訊，讓我們指示函式庫使用它。

> [!NOTE]
> 值得將您的 API 金鑰與程式碼分開。您可以使用環境變數來做到這一點。
>
> - 將環境變數 `OPENAI_API_KEY` 設定為您的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 設定配置 Azure

如果你正在使用 Azure OpenAI，以下是設定配置的方法:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

以上我們設定以下內容:

- `api_type` 設為 `azure`。這告訴函式庫使用 Azure OpenAI 而非 OpenAI。
- `api_key`，這是你在 Azure Portal 中找到的 API 金鑰。
- `api_version`，這是你想使用的 API 版本。在撰寫本文時，最新的版本是 `2023-05-15`。
- `api_base`，這是 API 的端點。你可以在 Azure Portal 中的 API 金鑰旁找到。

> [!NOTE] > `os.getenv` 是一個讀取環境變數的函式。你可以使用它來讀取像是 `OPENAI_API_KEY` 和 `API_BASE` 的環境變數。在你的終端機中設定這些環境變數或使用像 `dotenv` 這樣的函式庫。

## 產生文字

生成文本的方法是使用 `Completion` 類別。以下是一個範例:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上述程式碼中，我們建立一個完成物件並傳入我們想要使用的模型和提示。然後我們列印產生的文字。

### 聊天完成

到目前為止，你已經看到我們如何使用 `Completion` 來產生文本。但還有另一個更適合聊天機器人的類別，稱為 `ChatCompletion`。以下是使用它的範例：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

更多關於此功能的資訊在即將到來的章節中。

## 練習 - 您的第一個文本生成應用程序

現在我們已經學會如何設定和配置 openai，是時候建構你的第一個文字產生應用了。要建構你的應用，請按照以下步驟操作:

1. 建立虛擬環境並安裝 openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用的是 Windows，請輸入 `venv\Scripts\activate` 而不是 `source venv/bin/activate`。

   > [!NOTE]
   > 前往 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 並搜尋 `Open AI`，選擇 `Open AI resource`，然後選擇 `Keys and Endpoint` 並複製 `Key 1` 的值來找到你的 Azure OpenAI 金鑰。

1. 建立一個 _app.py_ 文件並給它以下程式碼:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # 添加你的完成程式碼
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # 進行完成
   completion = client.chat.completions.create(model=deployment, messages=messages)

   # 打印回應
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > 如果你使用的是 Azure OpenAI，你需要將 `api_type` 設置為 `azure` 並將 `api_key` 設置為你的 Azure OpenAI 金鑰。

   你應該會看到如下輸出:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示，用於不同的事情

現在你已經看到了如何使用提示生成文本。你甚至有一個正在執行的程式碼，可以修改和更改以生成不同類型的文本。

提示可以用於各種任務。例如:

- **生成一種類型的文本**。例如，你可以生成一首詩、測驗的問題等。
- **查找資訊**。你可以使用提示來查找資訊，例如以下範例'在網頁開發中，CORS 是什麼意思？'。
- **生成程式碼**。你可以使用提示來生成程式碼，例如開發用於驗證電子郵件的正則表達式，或者為什麼不生成整個程式，例如一個網頁應用程式？

## 更實用的使用案例: 秘訣產生器

想像一下你在家裡有食材，並且你想做些料理。為此，你需要一個秘訣。一種找到秘訣的方法是使用搜尋引擎，或者你可以使用 LLM 來完成。

你可以這樣寫一個提示：

> "給我 5 個使用以下食材的菜餚秘訣: 雞肉、馬鈴薯和胡蘿蔔。每個秘訣列出所有使用的食材"

根據上述提示，你可能會得到類似的回應:

```output
1. 烤雞和蔬菜:
材料:
- 4 塊雞腿
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 2 湯匙橄欖油
- 2 瓣大蒜，切碎
- 1 茶匙乾百里香
- 1 茶匙乾牛至
- 鹽和胡椒，適量

2. 雞肉和馬鈴薯燉菜:
材料:
- 2 湯匙橄欖油
- 1 個洋蔥，切丁
- 2 瓣大蒜，切碎
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 茶匙乾牛至
- 1 茶匙乾百里香
- 1 杯雞湯
- 鹽和胡椒，適量

3. 雞肉和馬鈴薯烤盤:
材料:
- 2 湯匙橄欖油
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 個洋蔥，切丁
- 2 瓣大蒜，切碎
- 1 茶匙乾牛至
- 1 茶匙乾百里香
- 1 杯雞湯
- 鹽和胡椒，適量

4. 雞肉和馬鈴薯湯:
材料:
- 2 湯匙橄欖油
- 1 個洋蔥，切丁
- 2 瓣大蒜，切碎
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 茶匙乾牛至
- 1 茶匙乾百里香
- 4 杯雞湯
- 鹽和胡椒，適量

5. 雞肉和馬鈴薯雜燴:
材料:
- 2 湯匙橄欖油
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 個洋蔥，切丁
- 2 瓣大蒜，切碎
- 1 茶匙乾牛至
```

這個結果很棒，我知道要煮什麼。此時，可能有用的改進是:

- 過濾掉我不喜歡或過敏的食材。
- 產生購物清單，以防我家裡沒有所有食材。

對於上述情況，讓我們添加一個額外的提示:

> "請移除含有大蒜的秘訣，因為我對大蒜過敏，並用其他東西替代。另外，請為這些秘訣製作一個購物清單，考慮到我家裡已經有雞肉、馬鈴薯和胡蘿蔔。"

現在你有一個新結果，即：

```output
1. 烤雞和蔬菜:
食材:
- 4 隻雞腿
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 2 湯匙橄欖油
- 1 茶匙乾百里香
- 1 茶匙乾牛至
- 鹽和胡椒，適量

2. 雞肉和馬鈴薯燉菜:
食材:
- 2 湯匙橄欖油
- 1 個洋蔥，切丁
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 茶匙乾牛至
- 1 茶匙乾百里香
- 1 杯雞湯
- 鹽和胡椒，適量

3. 雞肉和馬鈴薯烤盤:
食材:
- 2 湯匙橄欖油
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 個洋蔥，切丁
- 1 茶匙乾牛至
- 1 茶匙乾百里香
- 1 杯雞湯
- 鹽和胡椒，適量

4. 雞肉和馬鈴薯湯:
食材:
- 2 湯匙橄欖油
- 1 個洋蔥，切丁
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 茶匙乾牛至
- 1 茶匙乾百里香
- 4 杯雞湯
- 鹽和胡椒，適量

5. 雞肉和馬鈴薯雜燴:
食材:
- 2 湯匙橄欖油
- 2 塊雞胸肉，切成塊
- 2 個馬鈴薯，切成塊
- 2 根胡蘿蔔，切成塊
- 1 個洋蔥，切丁
- 1 茶匙乾牛至

購物清單:
- 橄欖油
- 洋蔥
- 百里香
- 牛至
- 鹽
- 胡椒
```

這就是你的五個秘訣，沒有提到大蒜，並且你還有一個購物清單，考慮到你家裡已經有的東西。

## 練習 - 建構一個秘訣產生器

現在我們已經演示了一個場景，讓我們寫程式碼來匹配演示的場景。要做到這一點，請按照以下步驟操作:

1. 使用現有的 _app.py_ 文件作為起點
1. 找到 `prompt` 變數並將其程式碼更改為以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果你現在執行程式碼，你應該會看到類似以下的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 是非確定性的，所以每次執行程式時可能會得到不同的結果。

   很好，讓我們看看如何改進。為了改進，我們希望確保程式碼是靈活的，以便可以改進和更改食材和食譜數量。

1. 讓我們以以下方式更改程式碼：

   ```python
   no_recipes = input("No of recipes (for example, 5: ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試執行程式碼，可能看起來像這樣：

   ```output
   No of recipes (for example, 5: 3
   List of ingredients (for example, chicken, potatoes, and carrots: milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 改進：新增篩選和購物清單

我們現在有一個可運作的應用程式，能夠產生秘訣，並且它很靈活，因為它依賴於使用者的輸入，不僅是秘訣的數量，還有使用的成分。

為了進一步改進它，我們想添加以下內容:

- **篩選食材**。我們希望能夠篩選出我們不喜歡或過敏的食材。為了完成這個變更，我們可以編輯現有的提示，並在其末尾添加一個篩選條件，如下所示：

  ```python
  filter = input("篩選（例如，素食，純素，或無麩質: ")

  prompt = f"給我{no_recipes}道菜的食譜，包含以下食材: {ingredients}。每個食譜列出所有使用的食材，不包含{filter}"
  ```

  上述程式碼中，我們在提示的末尾添加了`{filter}`，並且從用戶那裡獲取篩選值。

  現在，執行程式的範例輸入可以如下所示：

  ```output
  食譜數量（例如，5: 3
  食材列表（例如，雞肉，馬鈴薯和胡蘿蔔: 洋蔥,牛奶
  篩選（例如，素食，純素，或無麩質: 不含牛奶

  1. 法式洋蔥湯

  食材:

  -1個大洋蔥，切片
  -3杯牛肉湯
  -1杯牛奶
  -6片法國麵包
  -1/4杯磨碎的帕瑪森起司
  -1湯匙黃油
  -1茶匙乾百里香
  -1/4茶匙鹽
  -1/4茶匙黑胡椒

  做法:

  1. 在大鍋中，用黃油將洋蔥炒至金黃色。
  2. 加入牛肉湯、牛奶、百里香、鹽和胡椒。煮沸。
  3. 降低火候，煮10分鐘。
  4. 將法國麵包片放在湯碗中。
  5. 將湯舀在麵包上。
  6. 撒上帕瑪森起司。

  2. 洋蔥和馬鈴薯湯

  食材:

  -1個大洋蔥，切碎
  -2杯馬鈴薯，切丁
  -3杯蔬菜湯
  -1杯牛奶
  -1/4茶匙黑胡椒

  做法:

  1. 在大鍋中，用黃油將洋蔥炒至金黃色。
  2. 加入馬鈴薯、蔬菜湯、牛奶和胡椒。煮沸。
  3. 降低火候，煮10分鐘。
  4. 熱食。

  3. 奶油洋蔥湯

  食材:

  -1個大洋蔥，切碎
  -3杯蔬菜湯
  -1杯牛奶
  -1/4茶匙黑胡椒
  -1/4杯通用麵粉
  -1/2杯磨碎的帕瑪森起司

  做法:

  1. 在大鍋中，用黃油將洋蔥炒至金黃色。
  2. 加入蔬菜湯、牛奶和胡椒。煮沸。
  3. 降低火候，煮10分鐘。
  4. 在小碗中，將麵粉和帕瑪森起司攪拌均勻，直到光滑。
  5. 加入湯中，繼續煮5分鐘，或直到湯變稠。
  ```

  如你所見，任何含有牛奶的食譜都被篩選掉了。但是，如果你對乳糖不耐，你可能還想篩選掉含有起司的食譜，因此需要明確說明。

- **生成購物清單**。我們希望生成購物清單，考慮到我們家裡已經有的食材。

  對於這個功能，我們可以嘗試在一個提示中解決所有問題，或者我們可以將其分成兩個提示。讓我們嘗試後者的方法。這裡我們建議添加一個額外的提示，但為了使其工作，我們需要將前一個提示的結果作為上下文添加到後一個提示中。

  找到程式碼中打印出第一個提示結果的部分，並在其下方添加以下程式碼：

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "為生成的食譜生成購物清單，請不要包括我已經有的食材。"

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # 打印回應
  print("購物清單:")
  print(completion.choices[0].message.content)
  ```

  注意以下幾點：

  1. 我們通過將第一個提示的結果添加到新提示中來構建一個新提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們發出一個新請求，但也考慮到我們在第一個提示中請求的 token 數量，所以這次我們說 `max_tokens` 是1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     試用這段程式碼，我們現在得到以下輸出：

     ```output
     食譜數量（例如，5: 2
     食材列表（例如，雞肉，馬鈴薯和胡蘿蔔: 蘋果,麵粉
     篩選（例如，素食，純素，或無麩質: 糖


     -蘋果和麵粉煎餅: 1杯麵粉，1/2茶匙泡打粉，1/2茶匙小蘇打，1/4茶匙鹽，1湯匙糖，1個雞蛋，1杯酪乳或酸奶，1/4杯融化的黃油，1個格蘭尼史密斯蘋果，去皮並磨碎
     -蘋果油炸圈餅: 1-1/2杯麵粉，1茶匙泡打粉，1/4茶匙鹽，1/4茶匙小蘇打，1/4茶匙肉豆蔻，1/4茶匙肉桂，1/4茶匙五香粉，1/4杯糖，1/4杯植物油，1/4杯牛奶，1個雞蛋，2杯磨碎的去皮蘋果
     購物清單:
     -麵粉，泡打粉，小蘇打，鹽，糖，雞蛋，酪乳，黃油，蘋果，肉豆蔻，肉桂，五香粉
     ```

## 改善你的設定

我們目前擁有的是可以運作的程式碼, 但我們應該做一些調整來進一步改進。一些我們應該做的事情是:

- **將秘密從程式碼中分離**，例如 API 金鑰。秘密不應該存在於程式碼中，應該儲存在安全的位置。要將秘密從程式碼中分離，我們可以使用環境變數和像 `python-dotenv` 這樣的函式庫從文件中載入它們。以下是程式碼中的做法：

  1. 建立一個 `.env` 文件，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Azure，你需要設定以下環境變數：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在程式碼中，你可以這樣載入環境變數：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **關於 token 長度的一句話**。我們應該考慮需要多少 token 來生成我們想要的文本。token 是要花錢的，所以在可能的情況下，我們應該嘗試節省使用的 token 數量。例如，我們能否調整提示語句以使用更少的 token？

  要更改使用的 token 數量，你可以使用 `max_tokens` 參數。例如，如果你想使用 100 個 token，你可以這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **嘗試調整 temperature**。temperature 是我們到目前為止還沒有提到的，但它對我們程式的表現有重要影響。temperature 值越高，輸出就越隨機。相反，temperature 值越低，輸出就越可預測。考慮你是否希望輸出有變化。

  要改變 temperature，你可以使用 `temperature` 參數。例如，如果你想使用 0.5 的 temperature，你可以這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，越接近 1.0，輸出越多樣化。

## 作業

在這個作業中，你可以選擇要建構什麼。

以下是一些建議：

- 調整秘訣產生器應用程式以進一步改進。嘗試不同的溫度值和提示，看看你能想出什麼。
- 建立一個「學習夥伴」。這個應用程式應該能夠回答關於某個主題的問題，例如 Python，你可以有類似「Python 中的某個主題是什麼？」的提示，或者你可以有一個提示說，顯示某個主題的程式碼等。
- 歷史機器人，讓歷史重現，指示機器人扮演某個歷史人物，並詢問它關於其生活和時代的問題。

## 解決方案

### 學習夥伴

以下是一個入門提示，看看你如何使用它並根據自己的喜好進行調整。

```text
- "你是 Python 語言的專家

    建議一個適合初學者的 Python 課程，格式如下:

    格式:
    - 概念:
    - 課程簡要說明:
    - 帶解答的程式碼練習"
```

### 歷史機器人

以下是一些你可以使用的提示:

```text
- "你是 Abe Lincoln，用三句話告訴我你自己，並使用 Abe 會使用的語法和詞彙來回答"
- "你是 Abe Lincoln，使用 Abe 會使用的語法和詞彙來回答：

   用 300 字告訴我你最大的成就"
```

## 知識檢查

概念溫度是做什麼的？

1. 它控制輸出的隨機程度。
1. 它控制回應的大小。
1. 它控制使用的標記數量。

## 🚀 挑戰

在完成作業時，嘗試變更溫度，嘗試將其設為 0、0.5 和 1。記住，0 是變化最小的，1 是變化最大的，哪個值最適合你的應用程式？

## 很棒的工作！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

前往第7課，我們將探討如何[建構聊天應用程式](../../../07-building-chat-applications/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)！

