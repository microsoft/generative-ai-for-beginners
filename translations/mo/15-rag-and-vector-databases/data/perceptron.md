<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:31:35+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "mo"
}
-->
# Introduction to Neural Networks: Perceptron

Một trong những nỗ lực đầu tiên để triển khai thứ gì đó tương tự như mạng nơ-ron hiện đại đã được thực hiện bởi Frank Rosenblatt từ Cornell Aeronautical Laboratory vào năm 1957. Đó là một thiết bị phần cứng gọi là "Mark-1", được thiết kế để nhận diện các hình học cơ bản như tam giác, vuông và tròn.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Hình ảnh từ Wikipedia

Một hình ảnh đầu vào được đại diện bởi mảng tế bào quang 20x20, vì vậy mạng nơ-ron có 400 đầu vào và một đầu ra nhị phân. Một mạng đơn giản chứa một nơ-ron, cũng gọi là **đơn vị logic ngưỡng**. Các trọng số của mạng nơ-ron hoạt động như các biến trở cần điều chỉnh thủ công trong giai đoạn huấn luyện.

> ✅ Biến trở là một thiết bị cho phép người dùng điều chỉnh điện trở của một mạch.

> Thời báo New York đã viết về perceptron vào thời điểm đó: *phôi của một máy tính điện tử mà [Hải quân] mong đợi sẽ có khả năng đi lại, nói chuyện, nhìn thấy, viết, tự tái tạo và nhận thức được sự tồn tại của nó.*

## Mô hình Perceptron

Giả sử chúng ta có N đặc trưng trong mô hình của mình, trong trường hợp đó vector đầu vào sẽ là một vector có kích thước N. Perceptron là một mô hình **phân loại nhị phân**, tức là nó có thể phân biệt giữa hai lớp dữ liệu đầu vào. Chúng ta sẽ giả định rằng đối với mỗi vector đầu vào x, đầu ra của perceptron sẽ là +1 hoặc -1, tùy thuộc vào lớp. Đầu ra sẽ được tính bằng công thức:

y(x) = f(w<sup>T</sup>x)

trong đó f là hàm kích hoạt bước

## Huấn luyện Perceptron

Để huấn luyện perceptron, chúng ta cần tìm một vector trọng số w phân loại hầu hết các giá trị đúng, tức là dẫn đến lỗi nhỏ nhất. Lỗi này được định nghĩa bởi **tiêu chí perceptron** theo cách sau:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

trong đó:

* tổng được lấy trên những điểm dữ liệu huấn luyện i dẫn đến phân loại sai
* x<sub>i</sub> là dữ liệu đầu vào, và t<sub>i</sub> là -1 hoặc +1 cho các ví dụ tiêu cực và tích cực tương ứng.

Tiêu chí này được xem như một hàm của trọng số w, và chúng ta cần tối thiểu hóa nó. Thường thì một phương pháp gọi là **gradient descent** được sử dụng, trong đó chúng ta bắt đầu với một số trọng số ban đầu w<sup>(0)</sup>, và sau đó ở mỗi bước cập nhật trọng số theo công thức:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ở đây η là cái gọi là **tốc độ học**, và ∇E(w) biểu thị **gradient** của E. Sau khi chúng ta tính toán gradient, chúng ta có

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Thuật toán trong Python trông như thế này:

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

Trong bài học này, bạn đã học về perceptron, một mô hình phân loại nhị phân, và cách huấn luyện nó bằng cách sử dụng vector trọng số.

## 🚀 Thử thách

Nếu bạn muốn thử xây dựng perceptron của riêng mình, hãy thử bài thực hành này trên Microsoft Learn sử dụng Azure ML designer

## Ôn tập & Tự học

Để xem cách chúng ta có thể sử dụng perceptron để giải quyết một vấn đề đồ chơi cũng như các vấn đề thực tế, và để tiếp tục học - hãy đến với notebook Perceptron.

Đây là một bài viết thú vị về perceptrons.

## Bài tập

Trong bài học này, chúng ta đã triển khai một perceptron cho nhiệm vụ phân loại nhị phân, và chúng ta đã sử dụng nó để phân loại giữa hai chữ số viết tay. Trong bài thực hành này, bạn được yêu cầu giải quyết vấn đề phân loại chữ số hoàn toàn, tức là xác định chữ số nào có khả năng tương ứng với một hình ảnh đã cho.

* Hướng dẫn
* Notebook

I'm sorry, but I'm not familiar with a language called "mo." Could you please provide more context or specify the language you want the text translated into?