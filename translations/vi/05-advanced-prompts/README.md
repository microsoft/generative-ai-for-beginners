<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:36:08+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "vi"
}
-->

> "Tạo mã cho một API Web Python"
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

Chạy lại prompt sẽ cho ra kết quả như sau:

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

Chỉ có một sự khác biệt rất nhỏ giữa hai kết quả này. Lần này, hãy làm ngược lại, đặt nhiệt độ thành 0.9:

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

và lần thử thứ hai với giá trị nhiệt độ 0.9:

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

Như bạn thấy, kết quả có thể rất đa dạng.

> Note, rằng còn nhiều tham số khác bạn có thể thay đổi để đa dạng hóa kết quả, như top-k, top-p, repetition penalty, length penalty và diversity penalty nhưng những điều này nằm ngoài phạm vi của khóa học này.

## Thực hành tốt

Có nhiều cách bạn có thể áp dụng để cố gắng đạt được kết quả mong muốn. Bạn sẽ tìm ra phong cách riêng của mình khi sử dụng prompt ngày càng nhiều.

Ngoài các kỹ thuật đã đề cập, còn có một số thực hành tốt cần cân nhắc khi tạo prompt cho LLM.

Dưới đây là một số thực hành tốt nên xem xét:

- **Xác định ngữ cảnh**. Ngữ cảnh rất quan trọng, càng xác định rõ như lĩnh vực, chủ đề, v.v. thì kết quả càng tốt.
- Giới hạn đầu ra. Nếu bạn muốn số lượng mục cụ thể hoặc độ dài nhất định, hãy chỉ rõ.
- **Xác định cả nội dung và cách thức**. Hãy nhớ đề cập cả những gì bạn muốn và cách bạn muốn, ví dụ "Tạo một API Web Python với các route products và customers, chia thành 3 file".
- **Sử dụng mẫu (templates)**. Thường thì bạn sẽ muốn làm phong phú prompt với dữ liệu từ công ty bạn. Hãy dùng templates để làm điều này. Templates có thể có các biến mà bạn thay thế bằng dữ liệu thực tế.
- **Chính tả đúng**. LLM có thể trả lời đúng, nhưng nếu bạn viết đúng chính tả, câu trả lời sẽ tốt hơn.

## Bài tập

Dưới đây là đoạn code Python minh họa cách xây dựng một API đơn giản bằng Flask:

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

Sử dụng trợ lý AI như GitHub Copilot hoặc ChatGPT và áp dụng kỹ thuật "tự cải tiến" để nâng cao đoạn code.

## Giải pháp

Hãy thử giải bài tập bằng cách thêm các prompt phù hợp vào đoạn code.

> [!TIP]
> Hãy đặt câu hỏi để yêu cầu cải tiến, tốt nhất là giới hạn số lần cải tiến. Bạn cũng có thể yêu cầu cải tiến theo một cách cụ thể, ví dụ kiến trúc, hiệu năng, bảo mật, v.v.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Kiểm tra kiến thức

Tại sao tôi lại sử dụng chain-of-thought prompting? Cho tôi xem 1 câu trả lời đúng và 2 câu trả lời sai.

1. Để dạy LLM cách giải quyết một vấn đề.
1. B, Để dạy LLM tìm lỗi trong code.
1. C, Để hướng dẫn LLM đưa ra các giải pháp khác nhau.

A: 1, vì chain-of-thought là cách chỉ cho LLM cách giải quyết vấn đề bằng cách cung cấp cho nó một chuỗi các bước, cùng với các vấn đề tương tự và cách chúng được giải quyết.

## 🚀 Thử thách

Bạn vừa sử dụng kỹ thuật tự cải tiến trong bài tập. Hãy lấy bất kỳ chương trình nào bạn đã xây dựng và xem xét những cải tiến bạn muốn áp dụng cho nó. Bây giờ hãy dùng kỹ thuật tự cải tiến để thực hiện các thay đổi đó. Bạn nghĩ kết quả sẽ tốt hơn hay tệ hơn?

## Làm tốt lắm! Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về Generative AI!

Hãy đến bài học 6, nơi chúng ta sẽ áp dụng kiến thức về Prompt Engineering bằng cách [xây dựng các ứng dụng tạo văn bản](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.