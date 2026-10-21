# Tạo Prompt Nâng cao

[![Tạo Prompt Nâng cao](../../../translated_images/vi/05-lesson-banner.522610fd4a2cd82d.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Chúng ta hãy tóm tắt lại một số kiến thức đã học từ chương trước:

> Kỹ thuật _prompt engineering_ là quá trình mà chúng ta **định hướng mô hình hướng tới các phản hồi phù hợp hơn** bằng cách cung cấp các hướng dẫn hoặc ngữ cảnh hữu ích hơn.

Cũng có hai bước trong việc viết prompt: xây dựng prompt bằng cách cung cấp ngữ cảnh liên quan, và _tối ưu hóa_, cách để cải thiện prompt một cách dần dần.

Đến thời điểm này, chúng ta đã có một số hiểu biết cơ bản về cách viết prompt, nhưng chúng ta cần đi sâu hơn. Trong chương này, bạn sẽ chuyển từ việc thử nghiệm nhiều prompt khác nhau sang việc hiểu vì sao một prompt lại tốt hơn prompt khác. Bạn sẽ học cách xây dựng prompt theo một số kỹ thuật cơ bản có thể áp dụng cho bất kỳ LLM nào.

## Giới thiệu

Trong chương này, chúng ta sẽ đề cập đến các chủ đề sau:

- Mở rộng kiến thức về kỹ thuật prompt bằng cách áp dụng các phương pháp khác nhau cho prompt của bạn.
- Cấu hình prompt để thay đổi kết quả đầu ra.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Áp dụng các kỹ thuật prompt engineering để cải thiện kết quả của các prompt.
- Thực hiện prompt với kết quả có thể thay đổi hoặc xác định.

## Prompt engineering

Prompt engineering là quá trình tạo ra các prompt để đem lại kết quả mong muốn. Nó không chỉ đơn giản là viết một đoạn văn bản cho prompt. Prompt engineering không phải là một ngành kỹ thuật, mà là một tập hợp các kỹ thuật bạn có thể áp dụng để đạt được kết quả mong muốn.

### Một ví dụ về prompt

Hãy xem xét một prompt cơ bản như sau:

> Tạo 10 câu hỏi về địa lý.

Trong prompt này, bạn thực ra đang áp dụng một số kỹ thuật prompt khác nhau.

Hãy cùng phân tích chi tiết.

- **Ngữ cảnh**, bạn chỉ định rằng nó nên liên quan đến "địa lý".
- **Giới hạn đầu ra**, bạn muốn không quá 10 câu hỏi.

### Hạn chế của prompt đơn giản

Bạn có thể sẽ nhận được hoặc không nhận được kết quả như mong muốn. Bạn sẽ thu được các câu hỏi, nhưng địa lý là một chủ đề rộng và bạn có thể không nhận được kết quả đúng do các lý do sau:

- **Chủ đề lớn**, bạn không biết nó sẽ là về quốc gia, thủ đô, sông ngòi và những thứ khác.
- **Định dạng**, nếu bạn muốn các câu hỏi được định dạng theo một kiểu nhất định thì sao?

Như bạn thấy, có rất nhiều điều cần cân nhắc khi tạo prompt.

Cho đến giờ, chúng ta đã thấy một ví dụ prompt đơn giản, nhưng AI tạo sinh có khả năng nhiều hơn giúp ích cho con người trong nhiều vai trò và ngành nghề khác nhau. Hãy khám phá một số kỹ thuật cơ bản tiếp theo.

### Các kỹ thuật tạo prompt

Trước tiên, chúng ta cần hiểu rằng prompt là một đặc tính _nổi lên_ của LLM, nghĩa là đây không phải là một tính năng có sẵn trong mô hình mà là thứ ta khám phá ra khi sử dụng mô hình.

Có một số kỹ thuật cơ bản mà chúng ta có thể dùng để tạo prompt cho LLM. Hãy cùng tìm hiểu chúng.

- **Zero-shot prompting** (prompt không ví dụ), đây là hình thức tạo prompt cơ bản nhất. Là một prompt đơn yêu cầu phản hồi dựa hoàn toàn vào dữ liệu huấn luyện của LLM.
- **Few-shot prompting** (prompt có ít ví dụ), loại prompt này hướng dẫn LLM bằng cách cung cấp một hoặc nhiều ví dụ để mô hình dựa vào đó tạo phản hồi.
- **Chain-of-thought**, loại prompt này dạy LLM cách phân chia vấn đề thành các bước.
- **Generated knowledge** (kiến thức tạo ra), để cải thiện phản hồi của prompt, bạn có thể cung cấp thêm các sự thật hoặc kiến thức được tạo ra bên cạnh prompt.
- **Least to most** (từ ít đến nhiều), giống như chain-of-thought, kỹ thuật này là chia nhỏ bài toán thành chuỗi bước và yêu cầu thực hiện từng bước theo thứ tự.
- **Self-refine** (tự cải tiến), kỹ thuật này là phản biện đầu ra của LLM và yêu cầu nó cải thiện.
- **Maieutic prompting**. Mục đích là đảm bảo câu trả lời của LLM là chính xác bằng cách yêu cầu mô hình giải thích các phần khác nhau trong câu trả lời. Đây là một dạng của self-refine.

### Zero-shot prompting

Phong cách prompt này rất đơn giản, nó gồm một prompt duy nhất. Đây có thể là kỹ thuật mà bạn dùng khi bắt đầu học về LLM. Dưới đây là ví dụ:

- Prompt: "Đại số là gì?"
- Câu trả lời: "Đại số là một nhánh của toán học nghiên cứu các ký hiệu toán học và luật để thao tác với các ký hiệu này."

### Few-shot prompting

Phong cách này giúp mô hình bằng cách cung cấp một vài ví dụ cùng với yêu cầu. Nó gồm một prompt duy nhất với dữ liệu nhiệm vụ cụ thể thêm vào. Ví dụ:

- Prompt: "Viết một bài thơ theo phong cách Shakespeare. Dưới đây là một vài ví dụ về sonnet của Shakespeare:
  Sonnet 18: 'Có nên so sánh em với ngày hè chăng? Em dịu dàng hơn, hòa nhã hơn...'
  Sonnet 116: 'Để ta không ngăn cấm cuộc kết đôi Thật lòng. Tình yêu không phải yêu khi đổi thay...'
  Sonnet 132: 'Đôi mắt anh yêu, thương cảm em, Biết trái tim em đang oán trách,...'
  Bây giờ, hãy viết một bài sonnet về vẻ đẹp của mặt trăng."
- Câu trả lời: "Trên bầu trời, vầng trăng rọi sáng dịu dàng, Trong ánh sáng bạc nhẹ nhàng tô điểm duyên dáng,..."

Các ví dụ cung cấp cho LLM ngữ cảnh, định dạng hoặc phong cách đầu ra mong muốn. Chúng giúp mô hình hiểu rõ nhiệm vụ và tạo ra câu trả lời chính xác, liên quan hơn.

### Chain-of-thought

Chain-of-thought là kỹ thuật rất thú vị vì nó hướng dẫn LLM qua từng bước. Ý tưởng là chỉ dẫn LLM sao cho nó hiểu cách thực hiện một việc nào đó. Xem ví dụ sau, có và không có chain-of-thought:

    - Prompt: "Alice has 5 apples, throws 3 apples, gives 2 to Bob and Bob gives one back, how many apples does Alice have?"
    - Answer: 5

LLM trả lời 5, sai. Đáp án đúng là 1 quả táo, theo phép tính (5 -3 -2 + 1 = 1).

Vậy làm sao chúng ta dạy LLM làm đúng?

Hãy thử chain-of-thought. Áp dụng chain-of-thought có nghĩa là:

1. Cho LLM một ví dụ tương tự.
1. Hiện phép tính và cách tính đúng.
1. Cung cấp prompt gốc.

Cách làm như sau:

- Prompt: "Lisa có 7 quả táo, ném đi 1 quả, cho Bart 4 quả và Bart trả lại 1 quả:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice có 5 quả táo, ném đi 3 quả, cho Bob 2 quả và Bob trả lại 1 quả, Alice còn bao nhiêu quả táo?"
  Câu trả lời: 1

Chú ý cách viết prompt dài hơn nhiều với ví dụ khác, phép tính và prompt gốc, ta đạt được câu trả lời đúng là 1.

Bạn thấy rằng chain-of-thought là kỹ thuật rất mạnh.

### Generated knowledge

Nhiều khi bạn muốn xây dựng prompt dựa trên dữ liệu công ty riêng. Một phần prompt là dữ liệu công ty, phần còn lại là yêu cầu bạn muốn.

Ví dụ, dưới đây là cách prompt có thể trông như thế nếu bạn làm trong ngành bảo hiểm:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Ở trên, bạn thấy cách prompt được xây dựng bằng một mẫu. Trong mẫu có nhiều biến, ký hiệu bởi `{{variable}}`, sẽ được thay bằng giá trị thực từ API công ty.

Đây là ví dụ về prompt sau khi các biến đã được thay bằng nội dung từ công ty bạn:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- Car, cheap, 500 USD
- Car, expensive, 1100 USD
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home, and Life insurance
```

Chạy prompt này với LLM sẽ tạo ra phản hồi như sau:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

Như bạn thấy, nó cũng đề xuất bảo hiểm nhân thọ, điều này không nên xảy ra. Kết quả này cho thấy chúng ta cần tối ưu prompt bằng cách chỉnh sửa prompt cho rõ ràng hơn về những gì có thể cho phép. Sau một số thử-sai, ta có prompt sau:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- type: Car, cheap, cost: 500 USD
- type: Car, expensive, cost: 1100 USD
- type: Home, cheap, cost: 600 USD
- type: Home, expensive, cost: 1200 USD
- type: Life, cheap, cost: 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000 restrict choice to types: Car, Home
```

Lưu ý rằng thêm trường _type_ và _cost_ cũng như từ khóa _restrict_ giúp LLM hiểu rõ hơn điều ta muốn.

Bây giờ ta nhận được phản hồi:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

Mục đích của ví dụ này là cho thấy dù dùng kỹ thuật cơ bản như _generated knowledge_, ta vẫn phải tối ưu prompt trong hầu hết các trường hợp để đạt kết quả mong muốn.

### Least-to-most

Ý tưởng của phương pháp Least-to-most là chia nhỏ một vấn đề lớn thành các vấn đề con. Bằng cách đó, bạn giúp dẫn dắt LLM cách "chinh phục" vấn đề lớn hơn. Ví dụ tốt có thể là khoa học dữ liệu, khi bạn có thể hỏi LLM chia nhỏ bài toán như sau:

> Prompt: Làm sao thực hiện khoa học dữ liệu trong 5 bước?

Với trợ lý AI trả lời:

1. Thu thập dữ liệu
1. Làm sạch dữ liệu
1. Phân tích dữ liệu
1. Vẽ biểu đồ dữ liệu
1. Trình bày dữ liệu

### Self-refine, phê bình kết quả

Với AI tạo sinh và LLM, bạn không thể hoàn toàn tin tưởng vào kết quả đầu ra. Bạn cần xác minh nó. Dù sao đi nữa, LLM chỉ cho bạn câu trả lời khả năng cao tiếp theo, chứ không phải câu trả lời chính xác. Vì thế, một ý tưởng tốt là yêu cầu LLM tự phê bình, đây là kỹ thuật self-refine.

Cách hoạt động như sau:

1. Prompt ban đầu yêu cầu LLM giải quyết vấn đề
1. LLM trả lời
1. Bạn phê bình câu trả lời và yêu cầu AI cải thiện
1. LLM trả lời lại lần nữa, lần này xem xét phê bình và đề xuất giải pháp nó đưa ra

Bạn có thể lặp lại quy trình này bao nhiêu lần tùy ý.

Ví dụ áp dụng kỹ thuật này:

> Prompt: "Tạo một Web API Python với các route products và customers"

Trả lời của AI:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Prompt: đề xuất 3 cách cải tiến code trên

Trả lời của AI:

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'This is the {request.path} page'

@app.route('/customers')
def customers():
    return f'This is the {request.path} page'

if __name__ == '__main__':
    app.run()
```

Như bạn thấy, phản hồi AI trên đang cải thiện đoạn code được đề xuất đầu tiên nhờ phê bình câu trả lời ban đầu.

### Maieutic prompting

Maieutic prompting là kỹ thuật giống self-refine nhưng tập trung hơn vào việc yêu cầu LLM giải thích bản thân nó. Mục tiêu là giảm sự không nhất quán trong đầu ra của LLM để đảm bảo nó đạt câu trả lời chính xác. Quy trình như sau:

1. Yêu cầu LLM trả lời câu hỏi
1. Với từng phần câu trả lời, yêu cầu LLM giải thích sâu hơn.
1. Nếu có phần không nhất quán, bỏ qua phần đó.

Lặp lại bước 2 và 3 cho đến khi bạn duyệt qua tất cả các phần và hài lòng với câu trả lời.

Ví dụ một prompt:

> prompt: Làm sao tôi tạo kế hoạch ứng phó khủng hoảng để giảm thiểu đại dịch trong 5 bước?
> LLM trả lời:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

Có 5 bước được xác định, nhưng chúng ta có thể xác minh nó đúng không? Hãy yêu cầu LLM giải thích từng bước:

> prompt: Giải thích chi tiết hơn bước đầu tiên, rủi ro đại dịch là gì chi tiết?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

Ở đây, chúng ta muốn chắc chắn LLM trả lời đúng nên hỏi giải thích chi tiết rủi ro đầu tiên và hy vọng nó nhất quán với câu trả lời trên:

> prompt: Trong đại dịch, rủi ro lớn nhất là gì và tại sao?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Rủi ro lớn nhất trong đại dịch là gì?

```text
The two biggest risks are loss of life and loss of business.
```

Ở bước này, LLM nhất quán và đề cập tới "sự sống" và "kinh doanh" là hai rủi ro lớn nhất. Giờ ta tiếp tục bước tiếp theo và có thể khá yên tâm. Tuy nhiên, không nên hoàn toàn tin tưởng LLM, luôn phải kiểm tra lại kết quả.

## Thay đổi kết quả đầu ra của bạn

LLM vốn phi xác định, nghĩa là bạn sẽ nhận được kết quả khác nhau mỗi lần chạy cùng một prompt. Thử prompt sau đây ví dụ:

> "Tạo mã cho Web API Python"

```python
# Import necessary modules
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result as JSON
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

Chạy lại prompt này tạo ra phản hồi hơi khác:

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

> Vậy kết quả đầu ra thay đổi có phải là vấn đề?

Tùy vào mục đích bạn làm gì. Nếu bạn muốn câu trả lời cụ thể thì đó là vấn đề. Nếu bạn chấp nhận đầu ra đa dạng như "Tạo 3 câu hỏi bất kỳ về địa lý", thì không phải vấn đề.

### Dùng nhiệt độ để thay đổi đầu ra

Được rồi, ta quyết định muốn giới hạn kết quả đầu ra để nó có thể dự đoán hơn, tức là xác định hơn. Làm sao để làm được điều đó?

Nhiệt độ là giá trị từ 0 đến 1, trong đó 0 là xác định nhất và 1 là đa dạng nhất. Giá trị mặc định là 0.7. Xem điều gì xảy ra khi chạy cùng prompt hai lần với nhiệt độ là 0.1:

> "Tạo mã cho Web API Python"

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

Chạy lại prompt cho ta kết quả:

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

Chỉ có khác biệt rất nhỏ giữa hai kết quả này. Lần này ta làm ngược lại, đặt nhiệt độ là 0.9:

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

Và lần thử thứ hai với nhiệt độ 0.9:

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

Như bạn thấy, kết quả đa dạng hơn rất nhiều.

> Lưu ý còn có các tham số khác bạn có thể thay đổi để thay đổi đầu ra như top-k, top-p, hình phạt lặp lại, hình phạt độ dài và hình phạt đa dạng nhưng những điều này nằm ngoài phạm vi khóa học này.

## Thực hành tốt

Có nhiều phương pháp bạn có thể áp dụng để cố gắng đạt được những gì bạn muốn. Bạn sẽ tìm ra phong cách riêng của mình khi sử dụng kỹ thuật tạo câu lệnh ngày càng nhiều hơn.

Ngoài những kỹ thuật chúng ta đã đề cập, còn có một số thực hành tốt nên cân nhắc khi tạo câu lệnh cho LLM.

Dưới đây là một số thực hành tốt nên cân nhắc:

- **Xác định bối cảnh**. Bối cảnh rất quan trọng, càng bạn xác định rõ như lĩnh vực, chủ đề, v.v. thì càng tốt.
- Giới hạn đầu ra. Nếu bạn muốn số lượng mục cụ thể hoặc độ dài cụ thể, hãy chỉ rõ.
- **Xác định cả cái gì và cách làm**. Hãy nhớ đề cập cả cái bạn muốn và cách bạn muốn, ví dụ "Tạo một API Web Python với các tuyến sản phẩm và khách hàng, chia thành 3 tệp".
- **Sử dụng mẫu câu lệnh**. Thường thì bạn sẽ muốn làm giàu câu lệnh bằng dữ liệu từ công ty của bạn. Hãy sử dụng mẫu câu lệnh để làm điều này. Mẫu có thể có các biến bạn thay bằng dữ liệu thực tế.
- **Chính tả đúng**. LLM có thể cung cấp cho bạn câu trả lời đúng, nhưng nếu bạn viết đúng chính tả, bạn sẽ nhận được câu trả lời tốt hơn.

## Bài tập

Dưới đây là mã Python minh họa cách xây dựng một API đơn giản với Flask:

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

Sử dụng trợ lý AI như GitHub Copilot hoặc ChatGPT và áp dụng kỹ thuật "tự cải tiến" để cải thiện mã.

## Giải pháp

Vui lòng thử giải bài tập bằng cách thêm các câu lệnh phù hợp vào mã.

> [!TIP]
> Soạn câu lệnh yêu cầu cải thiện, nên giới hạn số lượng cải tiến. Bạn cũng có thể yêu cầu cải thiện theo cách cụ thể, ví dụ kiến trúc, hiệu năng, bảo mật, v.v.

[Giải pháp](../../../05-advanced-prompts/python/aoai-solution.py?WT.mc_id=academic-105485-koreyst)

## Kiểm tra kiến thức

Tại sao tôi lại dùng kỹ thuật tạo chuỗi tư duy? Cho tôi xem 1 câu trả lời đúng và 2 câu trả lời sai.

1. Để dạy LLM cách giải quyết vấn đề.
1. B, Để dạy LLM tìm lỗi trong mã.
1. C, Để hướng dẫn LLM nghĩ ra các giải pháp khác nhau.

A: 1, vì chuỗi tư duy là về việc chỉ cho LLM cách giải quyết vấn đề bằng cách cung cấp một chuỗi các bước, và các vấn đề tương tự cùng cách giải quyết.

## 🚀 Thử thách

Bạn vừa sử dụng kỹ thuật tự cải tiến trong bài tập. Hãy lấy bất kỳ chương trình nào bạn đã xây dựng và xem xét những cải tiến bạn muốn áp dụng cho nó. Bây giờ hãy dùng kỹ thuật tự cải tiến để thực hiện những thay đổi đã đề xuất. Bạn nghĩ kết quả thế nào, tốt hơn hay tệ hơn?

## Rất tốt! Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy tham khảo [bộ sưu tập Học AI Sinh tạo của chúng tôi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI Sinh tạo!

Hãy đến Bài học 6 nơi bạn sẽ áp dụng kiến thức Kỹ thuật Tạo câu lệnh bằng cách [xây dựng ứng dụng tạo văn bản](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->