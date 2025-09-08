<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:26:30+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "hk"
}
-->

重要規則：
1. 不要在翻譯內容周圍加上'''markdown或其他標籤
2. 確保翻譯不會過於直譯
3. 註解也要翻譯
4. 此檔案為Markdown格式 - 不要當作XML或HTML處理
5. 不要翻譯：
   - [!NOTE], [!WARNING], [!TIP], [!IMPORTANT], [!CAUTION]
   - 變數名稱、函式名稱、類別名稱
   - 像 @@INLINE_CODE_x@@ 或 @@CODE_BLOCK_x@@ 這類的佔位符
   - URL或路徑
6. 保持所有原始的Markdown格式不變
7. 僅回傳翻譯後的內容，不要加任何額外標籤或標記
請從左至右書寫輸出內容。

> 「為Python Web API產生程式碼」
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

再次執行提示後，我們得到以下結果：

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

這兩個輸出之間只有一點點差異。這次我們反過來，將 temperature 設為 0.9：

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

第二次嘗試，temperature 同樣設為 0.9：

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

如你所見，結果變化非常大。

> 注意，還有更多參數可以調整以改變輸出，例如 top-k、top-p、重複懲罰、長度懲罰和多樣性懲罰，但這些超出本課程範圍。

## 好習慣

有很多方法可以嘗試達到你想要的結果。隨著你越來越多地使用提示，你會找到自己的風格。

除了我們已經介紹的技巧外，還有一些在提示大型語言模型時值得注意的好習慣。

以下是一些值得考慮的好習慣：

- **明確指定上下文**。上下文很重要，越能明確指定領域、主題等，結果越好。
- 限制輸出。如果你想要特定數量的項目或特定長度，請明確說明。
- **同時指定內容和方式**。記得說明你想要什麼以及怎麼做，例如「建立一個 Python Web API，包含 products 和 customers 路由，分成三個檔案」。
- **使用範本**。通常你會想用公司資料來豐富提示，這時候可以用範本。範本可以包含變數，替換成實際資料。
- **拼寫正確**。大型語言模型可能會給出正確答案，但拼寫正確會讓回應更好。

## 作業

以下是用 Python 示範如何用 Flask 建立簡單 API 的程式碼：

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

使用像 GitHub Copilot 或 ChatGPT 這類 AI 助手，並運用「自我優化」技巧來改進程式碼。

## 解答

請嘗試透過加入合適的提示來完成作業。

> [!TIP]
> 請用提示語句要求改進，最好限制改進的次數。你也可以指定改進方向，例如架構、效能、安全性等。

[解答](../../../05-advanced-prompts/python/aoai-solution.py)

## 知識檢核

為什麼我要使用 chain-of-thought 提示？請給我 1 個正確回答和 2 個錯誤回答。

1. 教大型語言模型如何解決問題。
1. B，教大型語言模型找出程式碼錯誤。
1. C，指示大型語言模型提出不同解決方案。

答：1，因為 chain-of-thought 是透過提供一連串步驟，以及類似問題和解決方式，來教大型語言模型如何解決問題。

## 🚀 挑戰

你剛剛在作業中使用了自我優化技巧。拿你寫過的任何程式，思考你想對它做哪些改進。然後用自我優化技巧來實施這些改變。你覺得結果如何？是變好還是變差？

## 做得好！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

接著前往第 6 課，我們將運用提示工程的知識，透過[建立文字生成應用程式](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)來實作。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。