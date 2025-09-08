<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:48:56+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Mạng Nơ-ron. Perceptron đa lớp

Trong phần trước, bạn đã tìm hiểu về mô hình mạng nơ-ron đơn giản nhất - perceptron một lớp, một mô hình phân loại hai lớp tuyến tính.

Trong phần này, chúng ta sẽ mở rộng mô hình này thành một khuôn khổ linh hoạt hơn, cho phép chúng ta:

* thực hiện **phân loại đa lớp** ngoài phân loại hai lớp
* giải quyết **bài toán hồi quy** ngoài phân loại
* tách các lớp không thể phân tách tuyến tính

Chúng ta cũng sẽ phát triển một khuôn khổ mô-đun riêng bằng Python, giúp xây dựng các kiến trúc mạng nơ-ron khác nhau.

## Hình thức hóa bài toán Máy học

Hãy bắt đầu với việc hình thức hóa bài toán Máy học. Giả sử chúng ta có tập dữ liệu huấn luyện **X** với nhãn **Y**, và cần xây dựng một mô hình *f* để dự đoán chính xác nhất có thể. Chất lượng dự đoán được đo bằng **hàm mất mát** ℒ. Các hàm mất mát thường dùng bao gồm:

* Với bài toán hồi quy, khi cần dự đoán một số, ta có thể dùng **lỗi tuyệt đối** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, hoặc **lỗi bình phương** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Với bài toán phân loại, ta dùng **0-1 loss** (về cơ bản tương đương với **độ chính xác** của mô hình), hoặc **logistic loss**.

Với perceptron một lớp, hàm *f* được định nghĩa là hàm tuyến tính *f(x)=wx+b* (ở đây *w* là ma trận trọng số, *x* là vector đặc trưng đầu vào, và *b* là vector bias). Với các kiến trúc mạng nơ-ron khác, hàm này có thể phức tạp hơn.

> Trong trường hợp phân loại, thường ta muốn đầu ra của mạng là xác suất của các lớp tương ứng. Để chuyển đổi các số bất kỳ thành xác suất (ví dụ để chuẩn hóa đầu ra), ta thường dùng hàm **softmax** σ, và hàm *f* trở thành *f(x)=σ(wx+b)*

Trong định nghĩa *f* ở trên, *w* và *b* được gọi là **tham số** θ=⟨*w,b*⟩. Với tập dữ liệu ⟨**X**,**Y**⟩, ta có thể tính tổng lỗi trên toàn bộ tập dữ liệu như một hàm của tham số θ.

> ✅ **Mục tiêu của việc huấn luyện mạng nơ-ron là giảm thiểu lỗi bằng cách điều chỉnh tham số θ**

## Tối ưu hóa bằng Gradient Descent

Có một phương pháp tối ưu hàm rất phổ biến gọi là **gradient descent**. Ý tưởng là ta có thể tính đạo hàm (trong trường hợp đa chiều gọi là **gradient**) của hàm mất mát theo tham số, và điều chỉnh tham số sao cho lỗi giảm xuống. Cách làm được hình thức hóa như sau:

* Khởi tạo tham số với giá trị ngẫu nhiên w<sup>(0)</sup>, b<sup>(0)</sup>
* Lặp lại nhiều lần bước sau:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Trong quá trình huấn luyện, các bước tối ưu được tính dựa trên toàn bộ tập dữ liệu (nhớ rằng lỗi được tính bằng tổng qua tất cả mẫu huấn luyện). Tuy nhiên, trong thực tế ta lấy các phần nhỏ của tập dữ liệu gọi là **minibatches**, và tính gradient dựa trên một phần dữ liệu. Vì phần dữ liệu này được lấy ngẫu nhiên mỗi lần, phương pháp này gọi là **stochastic gradient descent** (SGD).

## Perceptron đa lớp và Thuật toán lan truyền ngược

Mạng một lớp, như ta đã thấy ở trên, chỉ có thể phân loại các lớp tách biệt tuyến tính. Để xây dựng mô hình phong phú hơn, ta có thể kết hợp nhiều lớp mạng. Về mặt toán học, điều này có nghĩa hàm *f* sẽ phức tạp hơn và được tính qua nhiều bước:

* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ở đây, α là **hàm kích hoạt phi tuyến**, σ là hàm softmax, và tham số θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Thuật toán gradient descent vẫn giữ nguyên, nhưng việc tính gradient trở nên phức tạp hơn. Dựa trên quy tắc đạo hàm theo chuỗi, ta có thể tính các đạo hàm như sau:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Quy tắc đạo hàm theo chuỗi được dùng để tính đạo hàm của hàm mất mát theo tham số.

Lưu ý phần bên trái của tất cả các biểu thức trên là giống nhau, do đó ta có thể tính đạo hàm hiệu quả bắt đầu từ hàm mất mát và đi "ngược lại" qua đồ thị tính toán. Phương pháp huấn luyện perceptron đa lớp này gọi là **backpropagation**, hay 'backprop'.

> TODO: trích dẫn hình ảnh

> ✅ Chúng ta sẽ tìm hiểu chi tiết hơn về backprop trong ví dụ notebook kèm theo.

## Kết luận

Trong bài học này, chúng ta đã xây dựng thư viện mạng nơ-ron riêng, và sử dụng nó cho bài toán phân loại đơn giản hai chiều.

## 🚀 Thử thách

Trong notebook kèm theo, bạn sẽ tự triển khai khuôn khổ xây dựng và huấn luyện perceptron đa lớp. Bạn sẽ có cơ hội quan sát chi tiết cách các mạng nơ-ron hiện đại hoạt động.

Hãy chuyển sang notebook OwnFramework và làm theo hướng dẫn.

## Ôn tập & Tự học

Backpropagation là thuật toán phổ biến trong AI và ML, rất đáng để nghiên cứu kỹ hơn.

## Bài tập

Trong bài lab này, bạn được yêu cầu sử dụng khuôn khổ đã xây dựng trong bài học để giải bài toán phân loại chữ số viết tay MNIST.

* Hướng dẫn
* Notebook

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.