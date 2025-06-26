<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "68664f7e754a892ae1d8d5e2b7bd2081",
  "translation_date": "2025-06-26T00:46:59+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "vi"
}
-->
[![Open Source Models](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.vi.png)](https://aka.ms/gen-ai-lesson18-gh?WT.mc_id=academic-105485-koreyst)

# Tinh chỉnh LLM của bạn

Sử dụng các mô hình ngôn ngữ lớn để xây dựng ứng dụng AI tạo sinh mang đến những thách thức mới. Một vấn đề chính là đảm bảo chất lượng phản hồi (độ chính xác và sự liên quan) trong nội dung do mô hình tạo ra cho một yêu cầu cụ thể của người dùng. Trong các bài học trước, chúng ta đã thảo luận về các kỹ thuật như xây dựng prompt và tạo sinh có hỗ trợ truy xuất nhằm giải quyết vấn đề bằng cách _chỉnh sửa đầu vào prompt_ cho mô hình hiện có.

Trong bài học hôm nay, chúng ta thảo luận về một kỹ thuật thứ ba, **tinh chỉnh**, nhằm giải quyết thách thức bằng cách _huấn luyện lại chính mô hình_ với dữ liệu bổ sung. Hãy đi sâu vào chi tiết.

## Mục tiêu học tập

Bài học này giới thiệu khái niệm tinh chỉnh cho các mô hình ngôn ngữ đã được huấn luyện trước, khám phá lợi ích và thách thức của cách tiếp cận này, và cung cấp hướng dẫn về thời điểm và cách sử dụng tinh chỉnh để cải thiện hiệu suất của các mô hình AI tạo sinh của bạn.

Cuối bài học này, bạn sẽ có thể trả lời các câu hỏi sau:

- Tinh chỉnh mô hình ngôn ngữ là gì?
- Khi nào và tại sao tinh chỉnh lại hữu ích?
- Làm thế nào tôi có thể tinh chỉnh một mô hình đã được huấn luyện trước?
- Những hạn chế của tinh chỉnh là gì?

Sẵn sàng chưa? Hãy bắt đầu.

## Hướng dẫn minh họa

Muốn có cái nhìn tổng quan về những gì chúng ta sẽ đề cập trước khi đi sâu vào? Hãy xem hướng dẫn minh họa này mô tả hành trình học tập cho bài học này - từ việc học các khái niệm cốt lõi và động lực cho tinh chỉnh, đến hiểu quy trình và các thực hành tốt nhất để thực hiện nhiệm vụ tinh chỉnh. Đây là một chủ đề thú vị để khám phá, vì vậy đừng quên kiểm tra trang [Tài nguyên](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có thêm các liên kết hỗ trợ hành trình tự học của bạn!

![Hướng dẫn minh họa về Tinh chỉnh Mô hình Ngôn ngữ](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.vi.png)

## Tinh chỉnh mô hình ngôn ngữ là gì?

Theo định nghĩa, các mô hình ngôn ngữ lớn được _huấn luyện trước_ trên lượng lớn văn bản được lấy từ nhiều nguồn khác nhau bao gồm internet. Như chúng ta đã học trong các bài học trước, chúng ta cần các kỹ thuật như _xây dựng prompt_ và _tạo sinh có hỗ trợ truy xuất_ để cải thiện chất lượng phản hồi của mô hình đối với các câu hỏi của người dùng ("prompt").

Một kỹ thuật phổ biến trong xây dựng prompt là cung cấp cho mô hình thêm hướng dẫn về những gì được mong đợi trong phản hồi, bằng cách cung cấp _hướng dẫn_ (hướng dẫn rõ ràng) hoặc _cho nó một vài ví dụ_ (hướng dẫn ngầm). Điều này được gọi là _học vài-shot_ nhưng nó có hai hạn chế:

- Giới hạn token của mô hình có thể hạn chế số lượng ví dụ bạn có thể đưa ra, và hạn chế hiệu quả.
- Chi phí token của mô hình có thể làm cho việc thêm ví dụ vào mỗi prompt trở nên đắt đỏ, và hạn chế tính linh hoạt.

Tinh chỉnh là một thực hành phổ biến trong các hệ thống học máy, nơi chúng ta lấy một mô hình đã được huấn luyện trước và huấn luyện lại nó với dữ liệu mới để cải thiện hiệu suất của nó trên một nhiệm vụ cụ thể. Trong bối cảnh của các mô hình ngôn ngữ, chúng ta có thể tinh chỉnh mô hình đã được huấn luyện trước _với một tập hợp ví dụ được tuyển chọn cho một nhiệm vụ hoặc miền ứng dụng cụ thể_ để tạo ra một **mô hình tùy chỉnh** có thể chính xác và liên quan hơn cho nhiệm vụ hoặc miền cụ thể đó. Một lợi ích phụ của tinh chỉnh là nó cũng có thể giảm số lượng ví dụ cần thiết cho học vài-shot - giảm sử dụng token và chi phí liên quan.

## Khi nào và tại sao chúng ta nên tinh chỉnh mô hình?

Trong _ngữ cảnh này_, khi chúng ta nói về tinh chỉnh, chúng ta đang đề cập đến tinh chỉnh **có giám sát** nơi việc huấn luyện lại được thực hiện bằng cách **thêm dữ liệu mới** không phải là một phần của tập dữ liệu huấn luyện ban đầu. Điều này khác với cách tiếp cận tinh chỉnh không có giám sát, nơi mô hình được huấn luyện lại trên dữ liệu ban đầu, nhưng với các siêu tham số khác nhau.

Điều quan trọng cần nhớ là tinh chỉnh là một kỹ thuật nâng cao đòi hỏi một mức độ chuyên môn nhất định để đạt được kết quả mong muốn. Nếu thực hiện không đúng cách, nó có thể không cung cấp các cải tiến như mong đợi, và thậm chí có thể làm suy giảm hiệu suất của mô hình cho miền mục tiêu của bạn.

Vì vậy, trước khi bạn học "cách" tinh chỉnh các mô hình ngôn ngữ, bạn cần biết "tại sao" bạn nên đi theo con đường này, và "khi nào" bắt đầu quá trình tinh chỉnh. Bắt đầu bằng cách tự hỏi bản thân những câu hỏi sau:

- **Trường hợp sử dụng**: Trường hợp sử dụng _của bạn_ cho tinh chỉnh là gì? Khía cạnh nào của mô hình đã được huấn luyện trước hiện tại mà bạn muốn cải thiện?
- **Các lựa chọn thay thế**: Bạn đã thử _các kỹ thuật khác_ để đạt được kết quả mong muốn chưa? Sử dụng chúng để tạo ra một cơ sở so sánh.
  - Kỹ thuật xây dựng prompt: Thử các kỹ thuật như nhắc nhở vài-shot với các ví dụ về phản hồi prompt liên quan. Đánh giá chất lượng phản hồi.
  - Tạo sinh có hỗ trợ truy xuất: Thử bổ sung prompt với kết quả truy vấn được tìm kiếm từ dữ liệu của bạn. Đánh giá chất lượng phản hồi.
- **Chi phí**: Bạn đã xác định được chi phí cho tinh chỉnh chưa?
  - Khả năng tinh chỉnh - mô hình đã được huấn luyện trước có sẵn để tinh chỉnh không?
  - Nỗ lực - để chuẩn bị dữ liệu huấn luyện, đánh giá & tinh chỉnh mô hình.
  - Tính toán - để chạy các công việc tinh chỉnh, và triển khai mô hình đã được tinh chỉnh
  - Dữ liệu - truy cập đủ ví dụ chất lượng để tinh chỉnh có tác động
- **Lợi ích**: Bạn đã xác nhận được lợi ích cho tinh chỉnh chưa?
  - Chất lượng - mô hình đã tinh chỉnh có vượt trội hơn cơ sở không?
  - Chi phí - nó có giảm sử dụng token bằng cách đơn giản hóa prompt không?
  - Khả năng mở rộng - bạn có thể tái sử dụng mô hình cơ bản cho các miền mới không?

Bằng cách trả lời những câu hỏi này, bạn sẽ có thể quyết định liệu tinh chỉnh có phải là cách tiếp cận phù hợp cho trường hợp sử dụng của bạn không. Lý tưởng nhất, cách tiếp cận này chỉ hợp lệ nếu lợi ích vượt trội hơn chi phí. Khi bạn quyết định tiến hành, đã đến lúc suy nghĩ về _cách_ bạn có thể tinh chỉnh mô hình đã được huấn luyện trước.

Muốn có thêm thông tin chi tiết về quá trình ra quyết định? Xem [Có nên tinh chỉnh hay không](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Làm thế nào chúng ta có thể tinh chỉnh một mô hình đã được huấn luyện trước?

Để tinh chỉnh một mô hình đã được huấn luyện trước, bạn cần có:

- một mô hình đã được huấn luyện trước để tinh chỉnh
- một tập dữ liệu để sử dụng cho tinh chỉnh
- một môi trường huấn luyện để chạy công việc tinh chỉnh
- một môi trường lưu trữ để triển khai mô hình đã tinh chỉnh

## Tinh chỉnh trong thực tế

Các tài nguyên sau đây cung cấp các hướng dẫn từng bước để hướng dẫn bạn qua một ví dụ thực tế sử dụng một mô hình được chọn với một tập dữ liệu đã được tuyển chọn. Để làm theo các hướng dẫn này, bạn cần một tài khoản trên nhà cung cấp cụ thể, cùng với quyền truy cập vào mô hình và tập dữ liệu liên quan.

| Nhà cung cấp  | Hướng dẫn                                                                                                                                                                    | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI        | [Cách tinh chỉnh các mô hình chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)          | Học cách tinh chỉnh một `gpt-35-turbo` cho một miền cụ thể ("trợ lý công thức") bằng cách chuẩn bị dữ liệu huấn luyện, chạy công việc tinh chỉnh, và sử dụng mô hình đã tinh chỉnh cho suy luận.                                                                                                                                                                                                                           |
| Azure OpenAI  | [Hướng dẫn tinh chỉnh GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Học cách tinh chỉnh một mô hình `gpt-35-turbo-0613` **trên Azure** bằng cách thực hiện các bước để tạo và tải lên dữ liệu huấn luyện, chạy công việc tinh chỉnh. Triển khai và sử dụng mô hình mới.                                                                                                                                                                                                                       |
| Hugging Face  | [Tinh chỉnh LLMs với Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bài viết blog này hướng dẫn bạn tinh chỉnh một _LLM mở_ (ví dụ: `CodeLlama 7B`) sử dụng thư viện [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) và [Học tăng cường Transformers (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) với các [tập dữ liệu](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) mở trên Hugging Face. |
|               |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 🤗 AutoTrain  | [Tinh chỉnh LLMs với AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (hoặc AutoTrain Advanced) là một thư viện python được phát triển bởi Hugging Face cho phép tinh chỉnh cho nhiều nhiệm vụ khác nhau bao gồm tinh chỉnh LLM. AutoTrain là một giải pháp không cần mã và tinh chỉnh có thể được thực hiện trên đám mây của bạn, trên Hugging Face Spaces hoặc cục bộ. Nó hỗ trợ cả GUI dựa trên web, CLI và huấn luyện qua các tập tin cấu hình yaml.                                       |
|               |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Bài tập

Chọn một trong các hướng dẫn trên và làm theo. _Chúng tôi có thể sao chép một phiên bản của các hướng dẫn này trong Jupyter Notebooks trong repo này chỉ để tham khảo. Vui lòng sử dụng các nguồn gốc để có được các phiên bản mới nhất_.

## Làm tốt lắm! Tiếp tục học tập của bạn.

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học AI Tạo Sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo Sinh của bạn!

Chúc mừng!! Bạn đã hoàn thành bài học cuối cùng từ loạt bài v2 cho khóa học này! Đừng ngừng học tập và xây dựng. \*\*Kiểm tra trang [TÀI NGUYÊN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) để biết danh sách các đề xuất bổ sung chỉ cho chủ đề này.

Loạt bài học v1 của chúng tôi cũng đã được cập nhật với nhiều bài tập và khái niệm hơn. Vì vậy, hãy dành một chút thời gian để làm mới kiến thức của bạn - và vui lòng [chia sẻ câu hỏi và phản hồi của bạn](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) để giúp chúng tôi cải thiện các bài học này cho cộng đồng.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa của nó nên được coi là nguồn đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.