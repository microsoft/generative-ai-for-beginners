<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:03:04+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "vi"
}
-->
# Các khung mạng nơ-ron

Như chúng ta đã học, để có thể huấn luyện mạng nơ-ron một cách hiệu quả, chúng ta cần làm hai việc:

* Thao tác trên tensor, ví dụ như nhân, cộng, và tính toán một số hàm như sigmoid hoặc softmax
* Tính toán gradient của tất cả các biểu thức, để thực hiện tối ưu hóa gradient descent

Trong khi thư viện `numpy` có thể làm phần đầu tiên, chúng ta cần một cơ chế để tính toán gradient. Trong khung mà chúng ta đã phát triển ở phần trước, chúng ta phải tự lập trình tất cả các hàm đạo hàm bên trong phương thức `backward`, phương thức thực hiện lan truyền ngược. Lý tưởng nhất, một khung nên cung cấp cho chúng ta cơ hội để tính toán gradient của *bất kỳ biểu thức nào* mà chúng ta có thể định nghĩa.

Một điều quan trọng khác là có thể thực hiện các tính toán trên GPU, hoặc bất kỳ đơn vị tính toán chuyên dụng nào khác, chẳng hạn như TPU. Huấn luyện mạng nơ-ron sâu đòi hỏi *rất nhiều* tính toán, và khả năng song song hóa các tính toán đó trên GPU là rất quan trọng.

> ✅ Thuật ngữ 'song song hóa' có nghĩa là phân phối các tính toán trên nhiều thiết bị.

Hiện tại, hai khung mạng nơ-ron phổ biến nhất là: TensorFlow và PyTorch. Cả hai đều cung cấp một API cấp thấp để thao tác với tensor trên cả CPU và GPU. Trên API cấp thấp, còn có API cấp cao hơn, gọi là Keras và PyTorch Lightning tương ứng.

API Cấp Thấp | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API Cấp Cao| Keras| Pytorch

**API cấp thấp** trong cả hai khung cho phép bạn xây dựng cái gọi là **đồ thị tính toán**. Đồ thị này định nghĩa cách tính toán đầu ra (thường là hàm mất mát) với các tham số đầu vào đã cho, và có thể được đẩy lên GPU để tính toán, nếu có sẵn. Có các hàm để phân biệt đồ thị tính toán này và tính toán gradient, sau đó có thể được sử dụng để tối ưu hóa các tham số của mô hình.

**API cấp cao** hầu như xem mạng nơ-ron như một **chuỗi các lớp**, và làm cho việc xây dựng hầu hết các mạng nơ-ron dễ dàng hơn nhiều. Huấn luyện mô hình thường yêu cầu chuẩn bị dữ liệu và sau đó gọi một hàm `fit` để thực hiện công việc.

API cấp cao cho phép bạn xây dựng các mạng nơ-ron điển hình rất nhanh chóng mà không cần lo lắng về nhiều chi tiết. Đồng thời, API cấp thấp cung cấp nhiều kiểm soát hơn đối với quá trình huấn luyện, do đó chúng được sử dụng nhiều trong nghiên cứu, khi bạn đang làm việc với các kiến trúc mạng nơ-ron mới.

Cũng quan trọng để hiểu rằng bạn có thể sử dụng cả hai API cùng nhau, ví dụ: bạn có thể phát triển kiến trúc lớp mạng của riêng mình bằng API cấp thấp, và sau đó sử dụng nó bên trong mạng lớn hơn được xây dựng và huấn luyện với API cấp cao. Hoặc bạn có thể định nghĩa một mạng bằng API cấp cao như một chuỗi các lớp, và sau đó sử dụng vòng lặp huấn luyện cấp thấp của riêng bạn để thực hiện tối ưu hóa. Cả hai API đều sử dụng cùng một khái niệm cơ bản và được thiết kế để hoạt động tốt với nhau.

## Học tập

Trong khóa học này, chúng tôi cung cấp hầu hết nội dung cho cả PyTorch và TensorFlow. Bạn có thể chọn khung yêu thích của mình và chỉ đi qua các sổ tay tương ứng. Nếu bạn không chắc chắn nên chọn khung nào, hãy đọc một số thảo luận trên internet về **PyTorch vs. TensorFlow**. Bạn cũng có thể xem cả hai khung để hiểu rõ hơn.

Khi có thể, chúng tôi sẽ sử dụng API cấp cao để đơn giản hóa. Tuy nhiên, chúng tôi tin rằng việc hiểu cách mạng nơ-ron hoạt động từ cơ bản là quan trọng, do đó lúc đầu chúng tôi bắt đầu làm việc với API cấp thấp và tensor. Tuy nhiên, nếu bạn muốn bắt đầu nhanh chóng và không muốn tốn nhiều thời gian để học những chi tiết này, bạn có thể bỏ qua chúng và đi thẳng vào các sổ tay API cấp cao.

## ✍️ Bài tập: Khung

Tiếp tục học tập trong các sổ tay sau:

API Cấp Thấp | Sổ tay TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API Cấp Cao| Keras | *PyTorch Lightning*

Sau khi thành thạo các khung, hãy tóm tắt lại khái niệm về overfitting.

# Overfitting

Overfitting là một khái niệm cực kỳ quan trọng trong học máy, và rất quan trọng để hiểu đúng!

Xem xét vấn đề sau về việc xấp xỉ 5 điểm (được biểu diễn bởi `x` trên các đồ thị dưới đây):

!tuyến tính | overfit
-------------------------|--------------------------
**Mô hình tuyến tính, 2 tham số** | **Mô hình phi tuyến tính, 7 tham số**
Lỗi huấn luyện = 5.3 | Lỗi huấn luyện = 0
Lỗi xác thực = 5.1 | Lỗi xác thực = 20

* Bên trái, chúng ta thấy một sự xấp xỉ đường thẳng tốt. Vì số lượng tham số phù hợp, mô hình hiểu được ý tưởng đằng sau phân phối điểm.
* Bên phải, mô hình quá mạnh. Vì chúng ta chỉ có 5 điểm và mô hình có 7 tham số, nó có thể điều chỉnh để đi qua tất cả các điểm, làm cho lỗi huấn luyện là 0. Tuy nhiên, điều này ngăn cản mô hình hiểu đúng mẫu đằng sau dữ liệu, do đó lỗi xác thực rất cao.

Rất quan trọng để tìm ra sự cân bằng đúng giữa sự phong phú của mô hình (số lượng tham số) và số lượng mẫu huấn luyện.

## Tại sao overfitting xảy ra

  * Không đủ dữ liệu huấn luyện
  * Mô hình quá mạnh
  * Quá nhiều nhiễu trong dữ liệu đầu vào

## Cách phát hiện overfitting

Như bạn có thể thấy từ đồ thị trên, overfitting có thể được phát hiện bởi lỗi huấn luyện rất thấp và lỗi xác thực cao. Thông thường trong quá trình huấn luyện, chúng ta sẽ thấy cả lỗi huấn luyện và lỗi xác thực bắt đầu giảm, và sau đó tại một số điểm lỗi xác thực có thể ngừng giảm và bắt đầu tăng. Đây sẽ là dấu hiệu của overfitting, và là chỉ báo rằng chúng ta nên dừng huấn luyện tại thời điểm này (hoặc ít nhất là tạo một ảnh chụp nhanh của mô hình).

## Cách ngăn chặn overfitting

Nếu bạn thấy rằng overfitting xảy ra, bạn có thể làm một trong những điều sau:

 * Tăng số lượng dữ liệu huấn luyện
 * Giảm độ phức tạp của mô hình
 * Sử dụng một số kỹ thuật điều chỉnh, như Dropout, mà chúng ta sẽ xem xét sau.

## Overfitting và sự đánh đổi Bias-Variance

Overfitting thực sự là một trường hợp của vấn đề tổng quát hơn trong thống kê gọi là sự đánh đổi Bias-Variance. Nếu chúng ta xem xét các nguồn lỗi có thể có trong mô hình của mình, chúng ta có thể thấy hai loại lỗi:

* **Lỗi thiên lệch** gây ra bởi thuật toán của chúng ta không thể nắm bắt đúng mối quan hệ giữa dữ liệu huấn luyện. Nó có thể do thực tế là mô hình của chúng ta không đủ mạnh (**underfitting**).
* **Lỗi phương sai**, được gây ra bởi mô hình xấp xỉ nhiễu trong dữ liệu đầu vào thay vì mối quan hệ có ý nghĩa (**overfitting**).

Trong quá trình huấn luyện, lỗi thiên lệch giảm (khi mô hình của chúng ta học cách xấp xỉ dữ liệu), và lỗi phương sai tăng. Quan trọng là dừng huấn luyện - hoặc bằng tay (khi chúng ta phát hiện overfitting) hoặc tự động (bằng cách giới thiệu điều chỉnh) - để ngăn chặn overfitting.

## Kết luận

Trong bài học này, bạn đã học về sự khác biệt giữa các API khác nhau cho hai khung AI phổ biến nhất, TensorFlow và PyTorch. Ngoài ra, bạn đã học về một chủ đề rất quan trọng, overfitting.

## 🚀 Thử thách

Trong các sổ tay đi kèm, bạn sẽ tìm thấy 'nhiệm vụ' ở cuối; hãy làm việc qua các sổ tay và hoàn thành các nhiệm vụ.

## Ôn tập & Tự học

Hãy nghiên cứu về các chủ đề sau:

- TensorFlow
- PyTorch
- Overfitting

Tự hỏi bản thân những câu hỏi sau:

- Sự khác biệt giữa TensorFlow và PyTorch là gì?
- Sự khác biệt giữa overfitting và underfitting là gì?

## Bài tập

Trong phòng thí nghiệm này, bạn được yêu cầu giải hai vấn đề phân loại bằng cách sử dụng mạng nơ-ron đầy đủ kết nối một lớp và nhiều lớp bằng PyTorch hoặc TensorFlow.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.