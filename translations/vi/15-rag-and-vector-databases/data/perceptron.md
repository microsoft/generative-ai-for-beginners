<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:59:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Mạng Nơ-ron: Perceptron

Một trong những nỗ lực đầu tiên để triển khai một thứ gì đó tương tự như mạng nơ-ron hiện đại được thực hiện bởi Frank Rosenblatt từ Phòng thí nghiệm Hàng không Cornell vào năm 1957. Đó là một thiết bị phần cứng gọi là "Mark-1", được thiết kế để nhận dạng các hình học sơ khai, như tam giác, hình vuông và hình tròn.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Hình ảnh từ Wikipedia

Một hình ảnh đầu vào được biểu diễn bằng mảng 20x20 tế bào quang điện, vì vậy mạng nơ-ron có 400 đầu vào và một đầu ra nhị phân. Mạng đơn giản chỉ chứa một neuron, còn gọi là **đơn vị logic ngưỡng**. Trọng số của mạng nơ-ron hoạt động giống như các biến trở cần được điều chỉnh thủ công trong giai đoạn huấn luyện.

> ✅ Biến trở là một thiết bị cho phép người dùng điều chỉnh điện trở của mạch.

> The New York Times đã viết về perceptron vào thời điểm đó: *phôi thai của một máy tính điện tử mà [Hải quân] kỳ vọng có thể đi, nói, nhìn, viết, tự nhân bản và nhận thức được sự tồn tại của nó.*

## Mô hình Perceptron

Giả sử chúng ta có N đặc trưng trong mô hình, trong trường hợp này vector đầu vào sẽ là một vector kích thước N. Perceptron là một mô hình **phân loại nhị phân**, tức là nó có thể phân biệt giữa hai lớp dữ liệu đầu vào. Chúng ta sẽ giả định rằng với mỗi vector đầu vào x, đầu ra của perceptron sẽ là +1 hoặc -1, tùy thuộc vào lớp. Đầu ra được tính theo công thức:

y(x) = f(w<sup>T</sup>x)

trong đó f là hàm kích hoạt bước

## Huấn luyện Perceptron

Để huấn luyện perceptron, chúng ta cần tìm vector trọng số w sao cho phân loại đúng phần lớn các giá trị, tức là tạo ra **lỗi** nhỏ nhất. Lỗi này được định nghĩa bởi **tiêu chí perceptron** như sau:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

trong đó:

* tổng được lấy trên các điểm dữ liệu huấn luyện i mà bị phân loại sai
* x<sub>i</sub> là dữ liệu đầu vào, và t<sub>i</sub> là -1 hoặc +1 tương ứng với các ví dụ âm và dương.

Tiêu chí này được xem như một hàm của trọng số w, và chúng ta cần tối thiểu hóa nó. Thường thì một phương pháp gọi là **gradient descent** được sử dụng, trong đó ta bắt đầu với một vector trọng số khởi tạo w<sup>(0)</sup>, rồi tại mỗi bước cập nhật trọng số theo công thức:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ở đây η là cái gọi là **tốc độ học**, và ∇E(w) là **đạo hàm** của E. Sau khi tính đạo hàm, ta có:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Thuật toán trong Python trông như sau:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Kết luận

Trong bài học này, bạn đã tìm hiểu về perceptron, một mô hình phân loại nhị phân, và cách huấn luyện nó bằng cách sử dụng vector trọng số.

## 🚀 Thử thách

Nếu bạn muốn thử xây dựng perceptron của riêng mình, hãy thử làm bài lab này trên Microsoft Learn sử dụng Azure ML designer


## Ôn tập & Tự học

Để xem cách chúng ta có thể sử dụng perceptron để giải quyết một bài toán đơn giản cũng như các bài toán thực tế, và để tiếp tục học tập - hãy truy cập vào sổ tay Perceptron.

Dưới đây là một bài viết thú vị về perceptron.

## Bài tập

Trong bài học này, chúng ta đã triển khai perceptron cho bài toán phân loại nhị phân, và đã sử dụng nó để phân loại giữa hai chữ số viết tay. Trong bài lab này, bạn được yêu cầu giải quyết hoàn toàn bài toán phân loại chữ số, tức là xác định chữ số nào có khả năng tương ứng nhất với một hình ảnh cho trước.

* Hướng dẫn
* Sổ tay

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.