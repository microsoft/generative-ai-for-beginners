<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T20:36:49+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "vi"
}
-->
[![Mô hình mã nguồn mở](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.vi.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Tinh chỉnh LLM của bạn

Việc sử dụng các mô hình ngôn ngữ lớn để xây dựng ứng dụng AI tạo sinh đi kèm với những thách thức mới. Một vấn đề quan trọng là đảm bảo chất lượng phản hồi (độ chính xác và sự liên quan) trong nội dung được tạo bởi mô hình cho một yêu cầu cụ thể của người dùng. Trong các bài học trước, chúng ta đã thảo luận về các kỹ thuật như thiết kế gợi ý và tạo sinh tăng cường truy xuất nhằm giải quyết vấn đề bằng cách _thay đổi đầu vào gợi ý_ cho mô hình hiện có.

Trong bài học hôm nay, chúng ta sẽ thảo luận về một kỹ thuật thứ ba, **tinh chỉnh**, nhằm giải quyết thách thức bằng cách _huấn luyện lại chính mô hình_ với dữ liệu bổ sung. Hãy cùng tìm hiểu chi tiết.

## Mục tiêu học tập

Bài học này giới thiệu khái niệm tinh chỉnh cho các mô hình ngôn ngữ đã được huấn luyện trước, khám phá lợi ích và thách thức của phương pháp này, và cung cấp hướng dẫn về thời điểm và cách sử dụng tinh chỉnh để cải thiện hiệu suất của các mô hình AI tạo sinh của bạn.

Sau khi hoàn thành bài học này, bạn sẽ có thể trả lời các câu hỏi sau:

- Tinh chỉnh mô hình ngôn ngữ là gì?
- Khi nào và tại sao tinh chỉnh lại hữu ích?
- Làm thế nào để tinh chỉnh một mô hình đã được huấn luyện trước?
- Những hạn chế của việc tinh chỉnh là gì?

Sẵn sàng chưa? Hãy bắt đầu.

## Hướng dẫn minh họa

Muốn có cái nhìn tổng quan về những gì chúng ta sẽ đề cập trước khi đi sâu vào chi tiết? Hãy xem hướng dẫn minh họa mô tả hành trình học tập cho bài học này - từ việc học các khái niệm cốt lõi và động lực cho việc tinh chỉnh, đến việc hiểu quy trình và các thực hành tốt nhất để thực hiện nhiệm vụ tinh chỉnh. Đây là một chủ đề thú vị để khám phá, vì vậy đừng quên kiểm tra trang [Tài nguyên](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có thêm các liên kết hỗ trợ hành trình học tập tự định hướng của bạn!

![Hướng dẫn minh họa về tinh chỉnh mô hình ngôn ngữ](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.vi.png)

## Tinh chỉnh mô hình ngôn ngữ là gì?

Theo định nghĩa, các mô hình ngôn ngữ lớn được _huấn luyện trước_ trên một lượng lớn văn bản được lấy từ nhiều nguồn khác nhau, bao gồm cả internet. Như chúng ta đã học trong các bài học trước, chúng ta cần các kỹ thuật như _thiết kế gợi ý_ và _tạo sinh tăng cường truy xuất_ để cải thiện chất lượng phản hồi của mô hình đối với các câu hỏi của người dùng ("gợi ý").

Một kỹ thuật thiết kế gợi ý phổ biến liên quan đến việc cung cấp cho mô hình nhiều hướng dẫn hơn về những gì được mong đợi trong phản hồi, hoặc bằng cách cung cấp _hướng dẫn_ (hướng dẫn rõ ràng) hoặc _đưa ra một vài ví dụ_ (hướng dẫn ngầm). Điều này được gọi là _học ít mẫu_ nhưng nó có hai hạn chế:

- Giới hạn token của mô hình có thể hạn chế số lượng ví dụ bạn có thể cung cấp và giảm hiệu quả.
- Chi phí token của mô hình có thể làm tăng chi phí khi thêm ví dụ vào mỗi gợi ý, và giảm tính linh hoạt.

Tinh chỉnh là một thực hành phổ biến trong các hệ thống học máy, nơi chúng ta lấy một mô hình đã được huấn luyện trước và huấn luyện lại nó với dữ liệu mới để cải thiện hiệu suất của nó trên một nhiệm vụ cụ thể. Trong bối cảnh mô hình ngôn ngữ, chúng ta có thể tinh chỉnh mô hình đã được huấn luyện trước _với một tập hợp ví dụ được chọn lọc cho một nhiệm vụ hoặc lĩnh vực ứng dụng cụ thể_ để tạo ra một **mô hình tùy chỉnh** có thể chính xác và phù hợp hơn cho nhiệm vụ hoặc lĩnh vực cụ thể đó. Một lợi ích phụ của việc tinh chỉnh là nó cũng có thể giảm số lượng ví dụ cần thiết cho học ít mẫu - giảm sử dụng token và chi phí liên quan.

## Khi nào và tại sao chúng ta nên tinh chỉnh mô hình?

Trong _bối cảnh này_, khi chúng ta nói về tinh chỉnh, chúng ta đang đề cập đến tinh chỉnh **có giám sát**, nơi việc huấn luyện lại được thực hiện bằng cách **thêm dữ liệu mới** không nằm trong tập dữ liệu huấn luyện ban đầu. Điều này khác với cách tiếp cận tinh chỉnh không giám sát, nơi mô hình được huấn luyện lại trên dữ liệu ban đầu, nhưng với các siêu tham số khác nhau.

Điều quan trọng cần nhớ là tinh chỉnh là một kỹ thuật nâng cao đòi hỏi một mức độ chuyên môn nhất định để đạt được kết quả mong muốn. Nếu thực hiện không đúng cách, nó có thể không mang lại những cải tiến như mong đợi, và thậm chí có thể làm giảm hiệu suất của mô hình đối với lĩnh vực mục tiêu của bạn.

Vì vậy, trước khi bạn học "cách" tinh chỉnh mô hình ngôn ngữ, bạn cần biết "tại sao" bạn nên chọn con đường này, và "khi nào" bắt đầu quá trình tinh chỉnh. Hãy bắt đầu bằng cách tự hỏi mình những câu hỏi sau:

- **Trường hợp sử dụng**: Trường hợp sử dụng _của bạn_ cho việc tinh chỉnh là gì? Bạn muốn cải thiện khía cạnh nào của mô hình đã được huấn luyện trước hiện tại?
- **Các lựa chọn thay thế**: Bạn đã thử _các kỹ thuật khác_ để đạt được kết quả mong muốn chưa? Sử dụng chúng để tạo một cơ sở so sánh.
  - Thiết kế gợi ý: Thử các kỹ thuật như gợi ý ít mẫu với các ví dụ về phản hồi gợi ý liên quan. Đánh giá chất lượng phản hồi.
  - Tạo sinh tăng cường truy xuất: Thử tăng cường gợi ý với kết quả truy vấn được tìm kiếm từ dữ liệu của bạn. Đánh giá chất lượng phản hồi.
- **Chi phí**: Bạn đã xác định chi phí cho việc tinh chỉnh chưa?
  - Khả năng tinh chỉnh - mô hình đã được huấn luyện trước có sẵn để tinh chỉnh không?
  - Nỗ lực - chuẩn bị dữ liệu huấn luyện, đánh giá & tinh chỉnh mô hình.
  - Tính toán - chạy các công việc tinh chỉnh, và triển khai mô hình đã tinh chỉnh.
  - Dữ liệu - có đủ ví dụ chất lượng để tạo tác động tinh chỉnh không?
- **Lợi ích**: Bạn đã xác nhận lợi ích của việc tinh chỉnh chưa?
  - Chất lượng - mô hình đã tinh chỉnh có vượt qua cơ sở không?
  - Chi phí - nó có giảm sử dụng token bằng cách đơn giản hóa gợi ý không?
  - Khả năng mở rộng - bạn có thể tái sử dụng mô hình cơ bản cho các lĩnh vực mới không?

Bằng cách trả lời những câu hỏi này, bạn sẽ có thể quyết định liệu tinh chỉnh có phải là cách tiếp cận phù hợp cho trường hợp sử dụng của bạn hay không. Lý tưởng nhất, cách tiếp cận này chỉ hợp lệ nếu lợi ích vượt trội hơn chi phí. Khi bạn quyết định tiến hành, đã đến lúc nghĩ về _cách_ bạn có thể tinh chỉnh mô hình đã được huấn luyện trước.

Muốn có thêm thông tin chi tiết về quá trình ra quyết định? Xem [Có nên tinh chỉnh hay không](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Làm thế nào chúng ta có thể tinh chỉnh một mô hình đã được huấn luyện trước?

Để tinh chỉnh một mô hình đã được huấn luyện trước, bạn cần có:

- một mô hình đã được huấn luyện trước để tinh chỉnh
- một tập dữ liệu để sử dụng cho việc tinh chỉnh
- một môi trường huấn luyện để chạy công việc tinh chỉnh
- một môi trường lưu trữ để triển khai mô hình đã tinh chỉnh

## Tinh chỉnh trong thực tế

Các tài nguyên sau đây cung cấp các hướng dẫn từng bước để hướng dẫn bạn qua một ví dụ thực tế sử dụng một mô hình được chọn với một tập dữ liệu được chọn lọc. Để làm việc qua các hướng dẫn này, bạn cần một tài khoản trên nhà cung cấp cụ thể, cùng với quyền truy cập vào mô hình và tập dữ liệu liên quan.

| Nhà cung cấp | Hướng dẫn                                                                                                                                                                       | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cách tinh chỉnh mô hình chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Học cách tinh chỉnh `gpt-35-turbo` cho một lĩnh vực cụ thể ("trợ lý công thức nấu ăn") bằng cách chuẩn bị dữ liệu huấn luyện, chạy công việc tinh chỉnh, và sử dụng mô hình đã tinh chỉnh để suy luận.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Hướng dẫn tinh chỉnh GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Học cách tinh chỉnh mô hình `gpt-35-turbo-0613` **trên Azure** bằng cách thực hiện các bước tạo & tải lên dữ liệu huấn luyện, chạy công việc tinh chỉnh. Triển khai & sử dụng mô hình mới.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Tinh chỉnh LLM với Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bài viết này hướng dẫn bạn tinh chỉnh một _LLM mở_ (ví dụ: `CodeLlama 7B`) sử dụng thư viện [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) với các [tập dữ liệu mở](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) trên Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Tinh chỉnh LLM với AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (hoặc AutoTrain Advanced) là một thư viện python được phát triển bởi Hugging Face cho phép tinh chỉnh cho nhiều nhiệm vụ khác nhau bao gồm tinh chỉnh LLM. AutoTrain là một giải pháp không cần mã và việc tinh chỉnh có thể được thực hiện trên đám mây của bạn, trên Hugging Face Spaces hoặc cục bộ. Nó hỗ trợ cả giao diện GUI dựa trên web, CLI và huấn luyện thông qua các tệp cấu hình yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Bài tập

Chọn một trong các hướng dẫn trên và thực hiện theo. _Chúng tôi có thể tái tạo một phiên bản của các hướng dẫn này trong Jupyter Notebooks trong repo này chỉ để tham khảo. Vui lòng sử dụng các nguồn gốc để có phiên bản mới nhất_.

## Làm tốt lắm! Tiếp tục học tập của bạn.

Sau khi hoàn thành bài học này, hãy kiểm tra [Bộ sưu tập học tập AI tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI tạo sinh!

Chúc mừng bạn!! Bạn đã hoàn thành bài học cuối cùng từ loạt bài v2 của khóa học này! Đừng ngừng học tập và xây dựng. \*\*Kiểm tra trang [TÀI NGUYÊN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có danh sách các gợi ý bổ sung chỉ cho chủ đề này.

Loạt bài v1 của chúng tôi cũng đã được cập nhật với nhiều bài tập và khái niệm hơn. Vì vậy, hãy dành một chút thời gian để làm mới kiến thức của bạn - và vui lòng [chia sẻ câu hỏi và phản hồi của bạn](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) để giúp chúng tôi cải thiện các bài học này cho cộng đồng.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.