<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:34:27+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "vi"
}
-->
# Các Framework Mạng Nơ-ron

Như chúng ta đã học, để có thể huấn luyện mạng nơ-ron một cách hiệu quả, chúng ta cần làm hai việc:

* Thao tác trên tensor, ví dụ như nhân, cộng, và tính các hàm như sigmoid hoặc softmax
* Tính đạo hàm của tất cả các biểu thức, để thực hiện tối ưu hóa bằng phương pháp gradient descent

Mặc dù thư viện `numpy` có thể làm phần đầu tiên, chúng ta cần một cơ chế để tính gradient. Trong framework mà chúng ta đã phát triển ở phần trước, chúng ta phải tự lập trình tất cả các hàm đạo hàm trong phương thức `backward`, chịu trách nhiệm cho việc lan truyền ngược (backpropagation). Lý tưởng nhất, một framework nên cho phép chúng ta tính gradient của *bất kỳ biểu thức nào* mà ta định nghĩa.

Một điều quan trọng khác là khả năng thực hiện tính toán trên GPU hoặc các đơn vị tính toán chuyên biệt khác như TPU. Việc huấn luyện mạng nơ-ron sâu đòi hỏi *rất nhiều* phép tính, và khả năng phân tán các phép tính này trên GPU là rất quan trọng.

> ✅ Thuật ngữ 'parallelize' có nghĩa là phân phối các phép tính trên nhiều thiết bị.

Hiện nay, hai framework mạng nơ-ron phổ biến nhất là: TensorFlow và PyTorch. Cả hai đều cung cấp API cấp thấp để thao tác với tensor trên cả CPU và GPU. Trên API cấp thấp còn có API cấp cao hơn, tương ứng là Keras và PyTorch Lightning.

API Cấp Thấp | TensorFlow | PyTorch
--------------|-------------|---------
API Cấp Cao   | Keras       | PyTorch

**API cấp thấp** trong cả hai framework cho phép bạn xây dựng các **đồ thị tính toán**. Đồ thị này định nghĩa cách tính đầu ra (thường là hàm mất mát) với các tham số đầu vào, và có thể được đẩy lên GPU để tính toán nếu có sẵn. Có các hàm để lấy đạo hàm của đồ thị tính toán này và tính gradient, sau đó dùng để tối ưu hóa tham số mô hình.

**API cấp cao** xem mạng nơ-ron như một **chuỗi các lớp**, giúp việc xây dựng hầu hết các mạng nơ-ron trở nên dễ dàng hơn nhiều. Việc huấn luyện mô hình thường chỉ cần chuẩn bị dữ liệu rồi gọi hàm `fit` để thực hiện.

API cấp cao cho phép bạn xây dựng các mạng nơ-ron điển hình rất nhanh mà không cần lo lắng nhiều về chi tiết. Trong khi đó, API cấp thấp cung cấp nhiều quyền kiểm soát hơn trong quá trình huấn luyện, nên thường được sử dụng trong nghiên cứu khi bạn làm việc với các kiến trúc mạng mới.

Cũng cần hiểu rằng bạn có thể dùng cả hai API cùng lúc, ví dụ bạn có thể phát triển kiến trúc lớp mạng riêng bằng API cấp thấp, rồi dùng nó trong mạng lớn hơn được xây dựng và huấn luyện bằng API cấp cao. Hoặc bạn có thể định nghĩa mạng bằng API cấp cao như một chuỗi lớp, rồi dùng vòng lặp huấn luyện cấp thấp của riêng bạn để tối ưu hóa. Cả hai API đều dựa trên cùng các khái niệm cơ bản và được thiết kế để hoạt động tốt cùng nhau.

## Học tập

Trong khóa học này, chúng tôi cung cấp hầu hết nội dung cho cả PyTorch và TensorFlow. Bạn có thể chọn framework ưa thích và chỉ học các notebook tương ứng. Nếu chưa chắc chọn framework nào, bạn có thể đọc các thảo luận trên mạng về **PyTorch vs. TensorFlow**. Bạn cũng có thể xem qua cả hai để hiểu rõ hơn.

Khi có thể, chúng tôi sẽ dùng API cấp cao để đơn giản hóa. Tuy nhiên, chúng tôi tin rằng việc hiểu cách mạng nơ-ron hoạt động từ cơ bản là rất quan trọng, nên ban đầu chúng ta sẽ làm việc với API cấp thấp và tensor. Nếu bạn muốn bắt đầu nhanh và không muốn tốn nhiều thời gian học các chi tiết này, bạn có thể bỏ qua và đi thẳng vào các notebook API cấp cao.

## ✍️ Bài tập: Frameworks

Tiếp tục học trong các notebook sau:

API Cấp Thấp | Notebook TensorFlow+Keras | PyTorch
--------------|----------------------------|---------
API Cấp Cao   | Keras                      | *PyTorch Lightning*

Sau khi thành thạo các framework, chúng ta sẽ ôn lại khái niệm overfitting.

# Overfitting

Overfitting là một khái niệm cực kỳ quan trọng trong học máy, và việc hiểu đúng nó là rất cần thiết!

Xem xét bài toán xấp xỉ 5 điểm (được biểu diễn bằng `x` trên các đồ thị dưới đây):

!linear | overfit
-------------------------|--------------------------
**Mô hình tuyến tính, 2 tham số** | **Mô hình phi tuyến, 7 tham số**
Lỗi huấn luyện = 5.3 | Lỗi huấn luyện = 0
Lỗi kiểm tra = 5.1 | Lỗi kiểm tra = 20

* Ở bên trái, ta thấy một đường thẳng xấp xỉ tốt. Vì số tham số phù hợp, mô hình nắm được ý tưởng phân bố điểm đúng.
* Ở bên phải, mô hình quá mạnh. Vì chỉ có 5 điểm nhưng mô hình có 7 tham số, nó có thể điều chỉnh để đi qua tất cả các điểm, khiến lỗi huấn luyện bằng 0. Tuy nhiên, điều này ngăn mô hình hiểu đúng mẫu dữ liệu, nên lỗi kiểm tra rất cao.

Việc cân bằng đúng giữa độ phức tạp của mô hình (số tham số) và số lượng mẫu huấn luyện là rất quan trọng.

## Tại sao overfitting xảy ra

  * Dữ liệu huấn luyện không đủ
  * Mô hình quá mạnh
  * Dữ liệu đầu vào có quá nhiều nhiễu

## Cách phát hiện overfitting

Như bạn thấy trong đồ thị trên, overfitting có thể được phát hiện khi lỗi huấn luyện rất thấp nhưng lỗi kiểm tra lại cao. Thông thường trong quá trình huấn luyện, lỗi huấn luyện và lỗi kiểm tra đều giảm, nhưng đến một điểm nào đó lỗi kiểm tra có thể ngừng giảm và bắt đầu tăng lên. Đây là dấu hiệu của overfitting, và là lúc bạn nên dừng huấn luyện (hoặc ít nhất lưu lại trạng thái mô hình).

overfitting

## Cách ngăn ngừa overfitting

Nếu bạn thấy overfitting xảy ra, bạn có thể làm một trong các việc sau:

 * Tăng lượng dữ liệu huấn luyện
 * Giảm độ phức tạp của mô hình
 * Sử dụng kỹ thuật regularization, như Dropout, mà chúng ta sẽ tìm hiểu sau.

## Overfitting và sự đánh đổi Bias-Variance

Overfitting thực ra là một trường hợp của vấn đề tổng quát hơn trong thống kê gọi là Bias-Variance Tradeoff. Nếu xem xét các nguồn lỗi trong mô hình, ta có thể thấy hai loại lỗi:

* **Lỗi bias** do thuật toán không thể nắm bắt đúng mối quan hệ trong dữ liệu huấn luyện. Điều này có thể do mô hình không đủ mạnh (**underfitting**).
* **Lỗi variance** do mô hình xấp xỉ cả nhiễu trong dữ liệu đầu vào thay vì mối quan hệ có ý nghĩa (**overfitting**).

Trong quá trình huấn luyện, lỗi bias giảm (khi mô hình học được dữ liệu), còn lỗi variance tăng. Việc dừng huấn luyện đúng lúc - bằng tay (khi phát hiện overfitting) hoặc tự động (bằng regularization) - là rất quan trọng để tránh overfitting.

## Kết luận

Trong bài học này, bạn đã học về sự khác biệt giữa các API trong hai framework AI phổ biến nhất, TensorFlow và PyTorch. Ngoài ra, bạn cũng đã tìm hiểu về một chủ đề rất quan trọng là overfitting.

## 🚀 Thử thách

Trong các notebook kèm theo, bạn sẽ thấy các 'nhiệm vụ' ở cuối; hãy làm theo các notebook và hoàn thành các nhiệm vụ đó.

## Ôn tập & Tự học

Tìm hiểu thêm về các chủ đề sau:

- TensorFlow
- PyTorch
- Overfitting

Tự đặt câu hỏi cho mình:

- Sự khác biệt giữa TensorFlow và PyTorch là gì?
- Sự khác biệt giữa overfitting và underfitting là gì?

## Bài tập

Trong phòng thí nghiệm này, bạn được yêu cầu giải hai bài toán phân loại sử dụng mạng fully-connected một lớp và nhiều lớp bằng PyTorch hoặc TensorFlow.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.