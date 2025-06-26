<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:06:50+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "vi"
}
-->
# Các Khung Mạng Nơ-ron

Như chúng ta đã học, để có thể huấn luyện mạng nơ-ron một cách hiệu quả, chúng ta cần làm hai điều:

* Thao tác trên các tensor, ví dụ như nhân, cộng, và tính một số hàm như sigmoid hoặc softmax
* Tính gradient của tất cả các biểu thức, để thực hiện tối ưu hóa gradient descent

Mặc dù thư viện `numpy` có thể thực hiện phần đầu tiên, chúng ta cần một cơ chế để tính gradient. Trong khung mà chúng ta đã phát triển ở phần trước, chúng ta phải tự lập trình tất cả các hàm đạo hàm bên trong phương thức `backward`, phương thức thực hiện backpropagation. Lý tưởng nhất, một khung nên cho phép chúng ta tính gradient của *bất kỳ biểu thức nào* mà chúng ta có thể định nghĩa.

Một điều quan trọng khác là có thể thực hiện các tính toán trên GPU, hoặc bất kỳ đơn vị tính toán chuyên biệt nào khác, như TPU. Huấn luyện mạng nơ-ron sâu đòi hỏi *rất nhiều* tính toán, và khả năng phân tán các tính toán đó trên GPU là rất quan trọng.

> ✅ Thuật ngữ 'parallelize' có nghĩa là phân phối các tính toán qua nhiều thiết bị.

Hiện tại, hai khung mạng nơ-ron phổ biến nhất là: TensorFlow và PyTorch. Cả hai đều cung cấp một API cấp thấp để thao tác với các tensor trên cả CPU và GPU. Trên nền tảng API cấp thấp, cũng có API cấp cao hơn, được gọi là Keras và PyTorch Lightning tương ứng.

API Cấp Thấp | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API Cấp Cao| Keras| Pytorch

**APIs Cấp Thấp** trong cả hai khung cho phép bạn xây dựng cái gọi là **đồ thị tính toán**. Đồ thị này định nghĩa cách tính đầu ra (thường là hàm mất mát) với các tham số đầu vào cho trước, và có thể được đẩy lên để tính toán trên GPU, nếu có sẵn. Có các hàm để phân biệt đồ thị tính toán này và tính gradient, sau đó có thể được sử dụng để tối ưu hóa các tham số mô hình.

**APIs Cấp Cao** gần như xem mạng nơ-ron như một **chuỗi các lớp**, và làm cho việc xây dựng hầu hết các mạng nơ-ron trở nên dễ dàng hơn. Việc huấn luyện mô hình thường đòi hỏi chuẩn bị dữ liệu và sau đó gọi hàm `fit` để thực hiện công việc.

API cấp cao cho phép bạn xây dựng các mạng nơ-ron điển hình rất nhanh chóng mà không cần lo lắng về nhiều chi tiết. Đồng thời, API cấp thấp cung cấp nhiều quyền kiểm soát hơn đối với quá trình huấn luyện, và do đó chúng được sử dụng nhiều trong nghiên cứu, khi bạn đang làm việc với các kiến trúc mạng nơ-ron mới.

Cũng quan trọng để hiểu rằng bạn có thể sử dụng cả hai API cùng nhau, ví dụ: bạn có thể phát triển kiến trúc lớp mạng của riêng mình bằng API cấp thấp, và sau đó sử dụng nó bên trong mạng lớn hơn được xây dựng và huấn luyện với API cấp cao. Hoặc bạn có thể định nghĩa một mạng bằng API cấp cao như một chuỗi các lớp, và sau đó sử dụng vòng lặp huấn luyện cấp thấp của riêng bạn để thực hiện tối ưu hóa. Cả hai API sử dụng cùng các khái niệm cơ bản và chúng được thiết kế để hoạt động tốt cùng nhau.

## Học tập

Trong khóa học này, chúng tôi cung cấp hầu hết nội dung cho cả PyTorch và TensorFlow. Bạn có thể chọn khung ưa thích của mình và chỉ cần đi qua các notebook tương ứng. Nếu bạn không chắc chắn nên chọn khung nào, hãy đọc một số thảo luận trên internet về **PyTorch vs. TensorFlow**. Bạn cũng có thể xem qua cả hai khung để hiểu rõ hơn.

Khi có thể, chúng tôi sẽ sử dụng APIs Cấp Cao để đơn giản hóa. Tuy nhiên, chúng tôi tin rằng việc hiểu cách mạng nơ-ron hoạt động từ đầu là quan trọng, do đó ban đầu chúng tôi bắt đầu làm việc với API cấp thấp và tensor. Tuy nhiên, nếu bạn muốn bắt đầu nhanh chóng và không muốn dành nhiều thời gian để học các chi tiết này, bạn có thể bỏ qua chúng và đi thẳng vào các notebook API cấp cao.

## ✍️ Bài tập: Khung

Tiếp tục học tập trong các notebook sau:

API Cấp Thấp | Notebook TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API Cấp Cao| Keras | *PyTorch Lightning*

Sau khi thành thạo các khung, hãy tóm tắt lại khái niệm overfitting.

# Overfitting

Overfitting là một khái niệm cực kỳ quan trọng trong học máy, và rất quan trọng để hiểu đúng!

Hãy xem xét vấn đề sau đây của việc xấp xỉ 5 điểm (được biểu diễn bởi `x` trên các đồ thị dưới đây):

!tuyến tính | overfit
-------------------------|--------------------------
**Mô hình tuyến tính, 2 tham số** | **Mô hình phi tuyến tính, 7 tham số**
Lỗi huấn luyện = 5.3 | Lỗi huấn luyện = 0
Lỗi xác thực = 5.1 | Lỗi xác thực = 20

* Ở bên trái, chúng ta thấy một xấp xỉ đường thẳng tốt. Vì số lượng tham số là phù hợp, mô hình nắm bắt được ý tưởng đằng sau phân phối điểm.
* Ở bên phải, mô hình quá mạnh. Vì chúng ta chỉ có 5 điểm và mô hình có 7 tham số, nó có thể điều chỉnh để đi qua tất cả các điểm, làm cho lỗi huấn luyện bằng 0. Tuy nhiên, điều này ngăn cản mô hình hiểu đúng mẫu đằng sau dữ liệu, do đó lỗi xác thực rất cao.

Rất quan trọng để đạt được sự cân bằng đúng giữa độ phong phú của mô hình (số lượng tham số) và số lượng mẫu huấn luyện.

## Tại sao xảy ra overfitting

  * Không đủ dữ liệu huấn luyện
  * Mô hình quá mạnh
  * Quá nhiều nhiễu trong dữ liệu đầu vào

## Cách phát hiện overfitting

Như bạn có thể thấy từ đồ thị trên, overfitting có thể được phát hiện bằng một lỗi huấn luyện rất thấp, và một lỗi xác thực cao. Thông thường trong quá trình huấn luyện, chúng ta sẽ thấy cả lỗi huấn luyện và lỗi xác thực bắt đầu giảm, và sau đó tại một thời điểm nào đó lỗi xác thực có thể ngừng giảm và bắt đầu tăng. Đây sẽ là dấu hiệu của overfitting, và chỉ báo rằng chúng ta có thể nên ngừng huấn luyện tại thời điểm này (hoặc ít nhất là tạo một bản chụp của mô hình).

overfitting

## Cách ngăn ngừa overfitting

Nếu bạn thấy rằng overfitting xảy ra, bạn có thể thực hiện một trong những điều sau:

 * Tăng số lượng dữ liệu huấn luyện
 * Giảm độ phức tạp của mô hình
 * Sử dụng một số kỹ thuật điều chỉnh, như Dropout, mà chúng ta sẽ xem xét sau.

## Overfitting và Cân Bằng Bias-Variance

Overfitting thực chất là một trường hợp của vấn đề chung hơn trong thống kê gọi là Cân Bằng Bias-Variance. Nếu chúng ta xem xét các nguồn lỗi có thể có trong mô hình của mình, chúng ta có thể thấy hai loại lỗi:

* **Lỗi bias** do thuật toán của chúng ta không thể nắm bắt mối quan hệ giữa dữ liệu huấn luyện một cách chính xác. Nó có thể do mô hình của chúng ta không đủ mạnh (**underfitting**).
* **Lỗi variance**, do mô hình xấp xỉ nhiễu trong dữ liệu đầu vào thay vì mối quan hệ có ý nghĩa (**overfitting**).

Trong quá trình huấn luyện, lỗi bias giảm (khi mô hình của chúng ta học cách xấp xỉ dữ liệu), và lỗi variance tăng. Quan trọng là ngừng huấn luyện - hoặc thủ công (khi chúng ta phát hiện overfitting) hoặc tự động (bằng cách giới thiệu điều chỉnh) - để ngăn ngừa overfitting.

## Kết luận

Trong bài học này, bạn đã học về sự khác biệt giữa các API khác nhau cho hai khung AI phổ biến nhất, TensorFlow và PyTorch. Ngoài ra, bạn đã học về một chủ đề rất quan trọng, overfitting.

## 🚀 Thử thách

Trong các notebook đi kèm, bạn sẽ tìm thấy 'nhiệm vụ' ở cuối; hãy làm việc qua các notebook và hoàn thành các nhiệm vụ.

## Ôn tập & Tự học

Nghiên cứu một số chủ đề sau:

- TensorFlow
- PyTorch
- Overfitting

Tự hỏi bản thân các câu hỏi sau:

- Sự khác biệt giữa TensorFlow và PyTorch là gì?
- Sự khác biệt giữa overfitting và underfitting là gì?

## Bài tập

Trong phòng thí nghiệm này, bạn được yêu cầu giải quyết hai vấn đề phân loại bằng cách sử dụng mạng kết nối đầy đủ đơn lớp và nhiều lớp bằng PyTorch hoặc TensorFlow.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.