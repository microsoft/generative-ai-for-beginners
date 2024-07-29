# 建立進階提示

[![建立進階提示](../../images/05-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson5-gh?WT.mc_id=academic-105485-koreyst?WT.mc_id=academic-105485-koreyst)

讓我們回顧一下前一章的一些學習內容:

> Prompt _工程_ 是我們通過提供更有用的指示或上下文來**引導模型朝向更相關的回應**的過程。

撰寫提示也有兩個步驟，構建提示，提供相關上下文，第二部分是_最佳化_，如何逐步改進提示。

此時，我們已經對如何編寫提示有了一些基本的了解，但我們需要更深入地探討。在本章中，你將從嘗試各種提示到理解為什麼一個提示比另一個提示更好。你將學習如何遵循一些基本技術來構建提示，這些技術可以應用於任何 LLM。

## 簡介

在本章中，我們將涵蓋以下主題:

- 通過將不同技術應用於提示來擴展您對提示工程的知識。
- 配置您的提示以改變輸出。

## 學習目標

完成此課程後，您將能夠：

- 應用提示工程技術來改善提示的結果。
- 執行變化或確定性的提示。

## 提示工程

提示工程是創建能夠產生預期結果的提示的過程。提示工程不僅僅是編寫文本提示。提示工程不是一門工程學科，它更像是一組技術，你可以應用這些技術來獲得預期的結果。

### 範例的提示

讓我們來看一個基本的提示，如下所示：

> 產生10個地理問題。

在此提示中，您實際上應用了不同提示技術的集合。

讓我們來解析這個。

- **上下文**, 你指定它應該是關於"地理"。
- **限制輸出**, 你希望不超過10個問題。

### 簡單提示的限制

你可能會或不會得到預期的結果。你的問題會被生成，但地理是一個很大的主題，你可能因以下原因而無法得到你想要的結果:

- **大主題**, 你不知道它會是關於國家、首都、河流等等。
- **格式**, 如果你希望問題以某種方式格式化怎麼辦？

如你所見，建立提示時有很多需要考慮的因素。

到目前為止，我們已經看過一個簡單的提示範例，但生成式 AI 能夠做更多事情來幫助各種角色和行業的人們。接下來讓我們探索一些基本技術。

### 提示技巧

首先，我們需要了解，提示是一個 LLM 的 _突現_ 屬性，這意味著這不是模型內建的功能，而是我們在使用模型時發現的。

有一些基本技術可以用來提示 LLM。我們來探索它們。

- **零次提示**，這是最基本的提示形式。它是一個單一的提示，僅基於其訓練數據請求LLM的回應。
- **少次提示**，這種類型的提示通過提供一個或多個範例來引導LLM生成其回應。
- **思維鏈**，這種類型的提示告訴LLM如何將問題分解成步驟。
- **生成知識**，為了改進提示的回應，你可以額外提供生成的事實或知識。
- **從少到多**，像思維鏈一樣，這種技術是將問題分解成一系列步驟，然後要求按順序執行這些步驟。
- **自我改進**，這種技術是批判LLM的輸出，然後要求其改進。
- **產婆提示**。你在這裡想要確保LLM的答案是正確的，並要求它解釋答案的各個部分。這是一種自我改進的形式。

### 零樣本提示

這種提示風格非常簡單，它由單一提示組成。這種技術可能是你在開始學習 LLMs 時所使用的。這裡有一個範例:

- 提示: "什麼是代數？"
- 答案: "代數是數學的一個分支，研究數學符號和操作這些符號的規則。"

### 少量樣本提示

這種提示風格通過提供一些範例和請求來幫助模型。它包含一個帶有額外任務特定資料的單一提示。這裡有一個範例:

- 提示: "以莎士比亞的風格寫一首詩。這裡有一些莎士比亞十四行詩的範例:
  十四行詩18: '我能否將你比作夏日？你更可愛也更溫和...'
  十四行詩116: '真心相愛的結合，我不承認任何障礙。愛不是愛，如果它在發現變故時改變...'
  十四行詩132: '我愛你的眼睛，它們憐憫我，知道你的心折磨我，帶著輕蔑，...'
  現在，寫一首關於月亮之美的十四行詩。"
- 回答: "在天空中，月亮柔和地閃爍，銀色的光芒散發著溫柔的優雅，..."

範例提供 LLM 相關的背景、格式或所需輸出的風格。它們幫助模型理解特定任務並生成更準確和相關的回應。

### Chain-of-thought

Chain-of-thought 是一個非常有趣的技術，因為它涉及讓 LLM 經歷一系列步驟。這個想法是以某種方式指導 LLM，使其理解如何做某事。考慮以下範例，有和沒有 chain-of-thought:

- 提示: "Alice 有 5 顆蘋果，扔了 3 顆蘋果，給了 Bob 2 顆，Bob 還了一顆，Alice 還有幾顆蘋果？"
- 答案: 5

LLM 回答 5，這是不正確的。正確答案是 1 個蘋果，根據計算 (5 -3 -2 + 1 = 1)。

那麼我們如何教導 LLM 正確地執行這個操作呢？

讓我們嘗試連鎖思維。應用連鎖思維意味著:

1. 給 LLM 一個類似的範例。
1. 顯示計算過程，以及如何正確計算。
1. 提供原始提示。

以下是方法：

- 提示: "Lisa 有 7 顆蘋果，丟掉 1 顆蘋果，給 Bart 4 顆蘋果，而 Bart 還給她一顆:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice 有 5 顆蘋果，丟掉 3 顆蘋果，給 Bob 2 顆，而 Bob 還給她一顆，Alice 有幾顆蘋果？"
  答案: 1

注意我們如何使用另一個範例撰寫更長的提示，一個計算，然後是原始提示，我們得出正確答案1。

如你所見，chain-of-thought 是一個非常強大的技術。

### 生成的知識

很多時候，當你想要建構提示時，你會想要使用自己公司的資料。你希望提示的一部分來自公司，另一部分則是你感興趣的實際提示。

作為範例，如果你從事保險業務，這就是你的提示可能看起來的樣子：

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
請根據以下預算和需求推薦一份保險:
預算: {{budget}}
需求: {{requirements}}
```

在上面，你可以看到如何使用模板構建提示。在模板中，有許多變數，用 `{{variable}}` 表示，這些變數將被公司 API 的實際值替換。

以下是一個範例，說明在將變數替換為您公司內容後，提示可能的樣子：

```text
保險公司: ACME Insurance
保險產品（每月費用）:
- 汽車，便宜，500 USD
- 汽車，昂貴，1100 USD
- 住宅，便宜，600 USD
- 住宅，昂貴，1200 USD
- 人壽，便宜，100 USD

請根據以下預算和需求建議一個保險:
預算: $1000
需求: 汽車、住宅和人壽保險
```

執行此提示通過 LLM 將產生如下回應:

```output
根據預算和需求，我們建議以下來自ACME保險的保險套件:
- 汽車，便宜，500美元
- 住宅，便宜，600美元
- 人壽，便宜，100美元
總成本: $1,200美元
```

如你所見，它也建議了人壽保險，這是不應該的。這個結果表明我們需要通過更改提示來使其更清晰，以便知道它可以允許什麼。經過一些_反覆試驗_，我們得出了以下提示:

```text
保險公司: ACME Insurance
保險產品（每月費用）:
- 類型: Car, 便宜, 費用: 500 USD
- 類型: Car, 昂貴, 費用: 1100 USD
- 類型: Home, 便宜, 費用: 600 USD
- 類型: Home, 昂貴, 費用: 1200 USD
- 類型: Life, 便宜, 費用: 100 USD

請根據以下預算和需求建議保險:
預算: $1000 限制選擇類型: Car, Home
```

注意，添加 _type_ 和 _cost_ 並使用關鍵字 _restrict_ 如何幫助 LLM 理解我們的需求。

現在我們得到以下回應:

```output
鑑於預算和需求，我們建議選擇每月花費500美元的汽車和便宜的保險產品。
```

這個範例的重點是要顯示，即使我們使用像_產生的知識_這樣的基本技術，我們在大多數情況下仍然需要最佳化提示以獲得所需的結果。

### 最少到最多

將最少提示到最多提示的想法是將一個更大的問題分解成子問題。這樣，你可以幫助引導LLM如何「征服」更大的問題。一個好的範例可以是資料科學，你可以要求LLM這樣劃分一個問題:

> 提示: 如何在5個步驟中進行資料科學?

使用你的 AI 助手回答：

1. 收集資料
1. 清理資料
1. 分析資料
1. 繪製資料
1. 呈現資料

### 自我改進，批評結果

隨著生成式 AI 和 LLM 的發展，你不能完全信任其輸出。你需要驗證它。畢竟，LLM 只是向你展示下一個最有可能說的話，而不是正確的內容。因此，一個好的想法是讓 LLM 自我批評，這引導我們使用自我改進技術。

它的運作方式是你按照以下步驟操作:

1. 初始提示要求 LLM 解決問題
1. LLM 回答
1. 你批評答案並要求 AI 改進
1. LLM 再次回答，這次考慮了批評並提出了解決方案

你可以根據需要多次重複此過程。

以下是使用此技術的範例:

> 提示: "建立一個具有路由產品和客戶的 Python Web API"

AI 答案:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return '產品'

@app.route('/customers')
def customers():
    return '顧客'
```

> 提示: 建議上述程式碼的3個改進之處

AI 答案:

```text
當然，這裡有三個改進程式碼的建議:

匯入正確的模組: 第一行應該匯入 Flask 而不是 flask。正確的匯入語句應該是 from flask import Flask。

添加一個主函式: 在檔案的末尾添加一個 if __name__ == '__main__': 區塊，以便在檔案執行時運行應用程式。

使用 f-strings: 使用 f-strings 來格式化路由函式中的返回語句。例如，return 'Products' 可以改為 return f'This is the {request.path} page'。
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'這是 {request.path} 頁面'

@app.route('/customers')
def customers():
    return f'這是 {request.path} 頁面'

if __name__ == '__main__':
    app.run()
```

如你所見，上述的 AI 回應正在改進第一個建議的程式碼，這要歸功於對第一個答案的批評。

### 產婆式提示

Maieutic 提示是一種類似於自我改進的技術，但它更關注於要求 LLM 解釋自己。其目標是減少 LLM 輸出中的不一致性，以確保其得出正確的答案。要遵循的工作流程是:

1. 向 LLM 提問
1. 對於答案的每個部分，要求 LLM 更深入地解釋。
1. 如果有不一致的地方，丟棄不一致的部分。

重複 2 和 3 直到你完成所有部分並對答案感到滿意為止。

這是一個範例提示:

> 提示: 我如何在5個步驟中建立一個危機計劃來減輕大流行病的影響？
> LLM 回答:

```text
1. 識別風險
1. 識別利益相關者
1. 識別資源
1. 識別行動
1. 識別通訊管道
```

已識別出5個步驟，但我們能否確定這是正確的？讓我們請 LLM 解釋每個步驟:

> 提示: 更詳細地解釋第一步，詳細說明大流行的風險是什麼？

```text
風險如下:

- 失去生命
- 失去業務
- 失去聲譽
- 失去客戶
- 失去員工
```

此時，我們想確保 LLM 是正確的，因此我們要求它更詳細地解釋第一個風險，並希望它與上述答案一致:

> 提示: 在大流行期間，最大的風險是什麼，為什麼？

```text
最大的風險是失去生命，因為這是最重要的保護。
```

> 在大流行中最大的兩個風險是什麼?

```text
兩個最大的風險是生命損失和業務損失。
```

此時，LLM 是一致的，並提到「生活」和「業務」是前兩大風險。我們現在可以繼續進行下一步，並感到相當有信心。然而，我們不應該盲目相信 LLM，我們應該始終驗證輸出。

## 變化你的輸出

LLM 本質上是非確定性的，這意味著每次執行相同的提示時，您將獲得不同的結果。例如，嘗試以下提示:

> "為 Python Web API 產生程式碼"

```python
# 匯入必要的模組
import flask
from flask import request, jsonify

# 建立一個 Flask 應用程式
app = flask.Flask(__name__)

# 為 API 建立一個路由
@app.route('/api', methods=['GET'])
def api():
    # 從請求中獲取資料
    data = request.args

    # 處理資料
    result = process_data(data)

    # 以 JSON 格式返回結果
    return jsonify(result)

# 處理資料的函式
def process_data(data):
    # 對資料進行某些操作
    result = data + 1

    # 返回結果
    return result

# 執行應用程式
if __name__ == '__main__':
    app.run()
```

再次執行相同的提示會產生略有不同的回應:

```python
#import necessary packages
import flask
from flask import request, jsonify

#create the Flask application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#create a list of books
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

#create an endpoint for the API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#create an endpoint to return all books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#create an endpoint to return a single book
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #check if an ID was provided as part of the URL
    #if ID is provided, assign it to a variable
    #if no ID is provided, display an error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #create an empty list for our results
    results = []

    #loop through the data and match results that fit the requested ID
    #IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    #use the jsonify function from Flask to convert our list of
    #Python dictionaries to the JSON format
    return jsonify(results)

app.run()
```

> 那麼多樣化的輸出是一個問題嗎?

取決於你想要做什麼。如果你想要一個具體的回應，那麼這是一個問題。如果你對於像是「生成任意3個地理問題」這樣的多樣化輸出沒有問題，那麼這不是問題。

### 使用溫度來變化您的輸出

好的，所以我們決定要限制輸出以使其更可預測，也就是更具決定性。我們該怎麼做呢？

溫度是一個介於 0 和 1 之間的值，其中 0 是最具決定性的，1 是最具變化的。預設值是 0.7。讓我們看看在溫度設為 0.1 的情況下，兩次執行相同提示會發生什麼：

> "為 Python Web API 產生程式碼"

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create an instance of the Flask class
app = flask.Flask(__name__)

#create an endpoint for the API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #get the request data
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#function to process the data
def process_data(data):
    #process the data
    result = {'result': 'success'}

    #return the result
    return result

#run the Flask app
if __name__ == '__main__':
    app.run()

```

再次執行提示會給我們這個結果:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

這兩個輸出之間只有很小的差異。這次我們來做相反的事情，將溫度設置為0.9:

```python
# 匯入必要的函式庫
import flask
from flask import request, jsonify

# 建立一個 Flask 應用程式
app = flask.Flask(__name__)

# 為 API 建立一個路由
@app.route('/api', methods=['GET'])
def api_call():
    # 從請求中獲取資料
    data = request.args

    # 處理資料
    result = process_data(data)

    # 返回結果
    return jsonify(result)

# 處理資料的函式
def process_data(data):
    # 對資料進行處理
    result = data + 1

    # 返回結果
    return result

# 執行應用程式
if __name__ == '__main__':
    app.run()

```

並且第二次嘗試將溫度值設為 0.9:

```python
import flask
from flask import request, jsonify

# 建立 Flask 應用程式
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# 建立一些測試資料
書籍 = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# 建立一個端點
@app.route('/', methods=['GET'])
def home():
    return '''<h1>歡迎來到我們的書籍 API！</h1>'''

@app.route('/api/v1/resources/books

```

正如你所見，結果可能會非常多樣化。

> 請注意，還有更多參數可以更改以改變輸出，例如 top-k、top-p、重複懲罰、長度懲罰和多樣性懲罰，但這些不在本課程範圍內。

## 良好實踐

有許多實踐方法可以嘗試獲得你想要的結果。隨著你越來越多地使用提示，你會找到自己的風格。

此外，除了我們已經涵蓋的技術外，還有一些在提示 LLM 時需要考慮的良好實踐。

以下是一些值得考慮的良好做法:

- **指定上下文**。上下文很重要，您能指定的越多（如領域、主題等），效果會越好。
- 限制輸出。如果您想要特定數量的項目或特定長度，請指定。
- **指定內容和方式**。記得要提到您想要什麼以及您想要的方式，例如"建立一個具有產品和客戶路由的 Python Web API，將其分成三個文件"。
- **使用範本**。通常，您會希望使用來自公司資料來豐富您的提示。使用範本來做到這一點。範本可以有變數，您可以用實際資料替換這些變數。
- **拼寫正確**。LLM 可能會給您正確的回應，但如果您拼寫正確，您會得到更好的回應。

## 作業

以下是使用 Flask 建構簡單 API 的 Python 程式碼:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__': 
    app.run()
```

使用像 GitHub Copilot 或 ChatGPT 的 AI 助手，並應用「自我改進」技術來改進程式碼。

## 解決方案

請嘗試通過向程式碼添加合適的提示來解決這個任務。

> [!TIP]
> 針對提示進行措辭以要求改進，限制改進的數量是個好主意。你也可以要求以某種方式改進，例如架構、效能、安全性等。

[解決方案](../../python/aoai-solution.py?WT.mc_id=academic-105485-koreyst)

## 知識檢查

為什麼我要使用 chain-of-thought 提示？給我看 1 個正確的回應和 2 個不正確的回應。

1. 教導 LLM 如何解決問題。
1. B, 教導 LLM 找出程式碼中的錯誤。
1. C, 指導 LLM 提出不同的解決方案。

A: 1，因為 chain-of-thought 是通過提供一系列步驟來向 LLM 展示如何解決問題，以及類似問題及其解決方法。

## 🚀 挑戰

你剛剛在作業中使用了自我改進技術。拿你建構的任何程式，考慮你想要應用的改進。現在使用自我改進技術來應用所提議的更改。你認為結果如何，更好還是更糟？

## 很棒的工作！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

前往第6課，我們將應用我們的提示工程知識來[建構文本生成應用程式](../../../06-text-generation-apps/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)

