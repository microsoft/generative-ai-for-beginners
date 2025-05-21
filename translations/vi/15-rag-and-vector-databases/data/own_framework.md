<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:23:24+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Mạng Nơ-ron. Perceptron Đa Tầng

Trong phần trước, bạn đã tìm hiểu về mô hình mạng nơ-ron đơn giản nhất - perceptron một tầng, một mô hình phân loại tuyến tính hai lớp.

Trong phần này, chúng ta sẽ mở rộng mô hình này thành một khung linh hoạt hơn, cho phép chúng ta:

* thực hiện **phân loại đa lớp** ngoài phân loại hai lớp
* giải quyết **các vấn đề hồi quy** ngoài phân loại
* phân tách các lớp không thể phân tách tuyến tính

Chúng ta cũng sẽ phát triển khung mô-đun của riêng mình trong Python để cho phép xây dựng các kiến trúc mạng nơ-ron khác nhau.

## Định hình Học Máy

Hãy bắt đầu với việc định hình vấn đề Học Máy. Giả sử chúng ta có một tập dữ liệu huấn luyện **X** với nhãn **Y**, và chúng ta cần xây dựng một mô hình *f* để đưa ra dự đoán chính xác nhất. Chất lượng dự đoán được đo bằng **hàm mất mát** ℒ. Các hàm mất mát sau đây thường được sử dụng:

* Đối với vấn đề hồi quy, khi cần dự đoán một số, chúng ta có thể sử dụng **lỗi tuyệt đối** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, hoặc **lỗi bình phương** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Đối với phân loại, chúng ta sử dụng **mất mát 0-1** (về cơ bản là giống như **độ chính xác** của mô hình), hoặc **mất mát logistic**.

Đối với perceptron một tầng, hàm *f* được định nghĩa là một hàm tuyến tính *f(x)=wx+b* (ở đây *w* là ma trận trọng số, *x* là vector của các đặc trưng đầu vào, và *b* là vector độ lệch). Đối với các kiến trúc mạng nơ-ron khác nhau, hàm này có thể có dạng phức tạp hơn.

> Trong trường hợp phân loại, thường mong muốn có được xác suất của các lớp tương ứng như đầu ra của mạng. Để chuyển đổi các số bất kỳ thành xác suất (ví dụ để chuẩn hóa đầu ra), chúng ta thường sử dụng hàm **softmax** σ, và hàm *f* trở thành *f(x)=σ(wx+b)*

Trong định nghĩa của *f* ở trên, *w* và *b* được gọi là **tham số** θ=⟨*w,b*⟩. Cho tập dữ liệu ⟨**X**,**Y**⟩, chúng ta có thể tính toán lỗi tổng thể trên toàn bộ tập dữ liệu như một hàm của các tham số θ.

> ✅ **Mục tiêu của việc huấn luyện mạng nơ-ron là giảm thiểu lỗi bằng cách thay đổi các tham số θ**

## Tối ưu hóa Gradient Descent

Có một phương pháp tối ưu hóa hàm được biết đến rộng rãi gọi là **gradient descent**. Ý tưởng là chúng ta có thể tính toán đạo hàm (trong trường hợp đa chiều gọi là **gradient**) của hàm mất mát đối với các tham số, và thay đổi các tham số theo cách mà lỗi sẽ giảm. Điều này có thể được định hình như sau:

* Khởi tạo các tham số bằng một số giá trị ngẫu nhiên w<sup>(0)</sup>, b<sup>(0)</sup>
* Lặp lại bước sau nhiều lần:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Trong quá trình huấn luyện, các bước tối ưu hóa được tính toán dựa trên toàn bộ tập dữ liệu (nhớ rằng mất mát được tính như tổng qua tất cả các mẫu huấn luyện). Tuy nhiên, trong thực tế, chúng ta lấy các phần nhỏ của tập dữ liệu gọi là **minibatches**, và tính toán gradient dựa trên một phần dữ liệu. Vì phần dữ liệu được lấy ngẫu nhiên mỗi lần, phương pháp này được gọi là **stochastic gradient descent** (SGD).

## Perceptron Đa Tầng và Backpropagation

Mạng một tầng, như chúng ta đã thấy ở trên, có khả năng phân loại các lớp có thể phân tách tuyến tính. Để xây dựng một mô hình phong phú hơn, chúng ta có thể kết hợp nhiều tầng của mạng. Về mặt toán học, điều này có nghĩa là hàm *f* sẽ có dạng phức tạp hơn, và sẽ được tính toán trong nhiều bước:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ở đây, α là một **hàm kích hoạt phi tuyến**, σ là hàm softmax, và các tham số θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Thuật toán gradient descent sẽ vẫn giữ nguyên, nhưng sẽ khó khăn hơn để tính toán gradient. Theo quy tắc chuỗi đạo hàm, chúng ta có thể tính toán đạo hàm như sau:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Quy tắc chuỗi đạo hàm được sử dụng để tính toán đạo hàm của hàm mất mát đối với các tham số.

Lưu ý rằng phần bên trái của tất cả các biểu thức này là giống nhau, và do đó chúng ta có thể tính toán hiệu quả các đạo hàm bắt đầu từ hàm mất mát và đi "ngược lại" qua biểu đồ tính toán. Do đó, phương pháp huấn luyện perceptron đa tầng được gọi là **backpropagation**, hoặc 'backprop'.

> TODO: trích dẫn hình ảnh

> ✅ Chúng ta sẽ nghiên cứu backprop chi tiết hơn trong ví dụ notebook của mình.

## Kết luận

Trong bài học này, chúng ta đã xây dựng thư viện mạng nơ-ron của riêng mình, và chúng ta đã sử dụng nó cho một nhiệm vụ phân loại hai chiều đơn giản.

## 🚀 Thử thách

Trong notebook đi kèm, bạn sẽ triển khai khung của riêng mình để xây dựng và huấn luyện perceptron đa tầng. Bạn sẽ có thể thấy chi tiết cách các mạng nơ-ron hiện đại hoạt động.

Tiến hành đến notebook OwnFramework và thực hiện nó.

## Đánh giá & Tự học

Backpropagation là một thuật toán phổ biến được sử dụng trong AI và ML, đáng để nghiên cứu chi tiết hơn.

## Bài tập

Trong phòng thí nghiệm này, bạn được yêu cầu sử dụng khung mà bạn đã xây dựng trong bài học này để giải quyết phân loại chữ số viết tay MNIST.

* Hướng dẫn
* Notebook

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.