[![Open Source Models](../../../translated_images/vi/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Tinh Chỉnh Lại Mô Hình Ngôn Ngữ Lớn của Bạn

Việc sử dụng các mô hình ngôn ngữ lớn để xây dựng các ứng dụng AI tạo sinh đi kèm với các thách thức mới. Một vấn đề then chốt là đảm bảo chất lượng phản hồi (độ chính xác và sự phù hợp) trong nội dung được mô hình tạo ra cho một yêu cầu người dùng cụ thể. Trong các bài học trước, chúng ta đã thảo luận về các kỹ thuật như kỹ thuật nhắc lệnh và sinh dựa trên truy xuất thông tin để cố gắng giải quyết vấn đề bằng cách _chỉnh sửa đầu vào nhắc lệnh_ cho mô hình hiện có.

Trong bài học hôm nay, chúng ta sẽ thảo luận về một kỹ thuật thứ ba, **tinh chỉnh (fine-tuning)**, cố gắng giải quyết thách thức bằng cách _đào tạo lại mô hình_ với dữ liệu bổ sung. Hãy cùng đi sâu vào chi tiết.

## Mục Tiêu Học Tập

Bài học này giới thiệu khái niệm tinh chỉnh cho các mô hình ngôn ngữ được đào tạo trước, khám phá lợi ích và thách thức của phương pháp này, đồng thời cung cấp hướng dẫn về khi nào và cách sử dụng tinh chỉnh để cải thiện hiệu suất của các mô hình AI tạo sinh của bạn.

Sau khi kết thúc bài học, bạn sẽ có thể trả lời các câu hỏi sau:

- Tinh chỉnh mô hình ngôn ngữ là gì?
- Khi nào và tại sao tinh chỉnh lại hữu ích?
- Làm thế nào tôi có thể tinh chỉnh một mô hình đã được đào tạo trước?
- Những hạn chế của việc tinh chỉnh là gì?

Sẵn sàng chưa? Chúng ta bắt đầu thôi.

## Hướng Dẫn Minh Họa

Muốn có cái nhìn tổng quan về những gì sẽ học trước khi đi sâu hơn? Hãy xem hướng dẫn minh họa này mô tả hành trình học tập cho bài học này - từ việc học các khái niệm cốt lõi và động lực cho việc tinh chỉnh, đến hiểu quy trình và các thực hành tốt nhất để thực hiện nhiệm vụ tinh chỉnh. Đây là một chủ đề hấp dẫn để khám phá, vì vậy đừng quên xem trang [Tài Nguyên](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có thêm các liên kết hỗ trợ hành trình học tập tự hướng dẫn!

![Hướng Dẫn Minh Họa Tinh Chỉnh Mô Hình Ngôn Ngữ](../../../translated_images/vi/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Tinh Chỉnh Mô Hình Ngôn Ngữ Là Gì?

Theo định nghĩa, các mô hình ngôn ngữ lớn được _đào tạo trước_ trên lượng lớn văn bản lấy từ nhiều nguồn đa dạng bao gồm cả internet. Như chúng ta đã học trong các bài học trước, chúng ta cần các kỹ thuật như _kỹ thuật nhắc lệnh_ và _tăng cường sinh dựa trên truy xuất thông tin_ để cải thiện chất lượng câu trả lời của mô hình cho các câu hỏi của người dùng ("nhắc lệnh").

Một kỹ thuật kỹ thuật nhắc lệnh phổ biến là cung cấp cho mô hình nhiều hướng dẫn hơn về những gì mong đợi ở phản hồi, bằng cách cung cấp _hướng dẫn_ (hướng dẫn rõ ràng) hoặc _cho nó một vài ví dụ_ (hướng dẫn ngầm). Kỹ thuật này gọi là _học với vài ví dụ (few-shot learning)_ nhưng nó có hai hạn chế:

- Giới hạn số token mô hình có thể xử lý làm hạn chế số lượng ví dụ bạn có thể cung cấp và hiệu quả đạt được.
- Chi phí token của mô hình có thể khiến việc thêm ví dụ vào mỗi nhắc lệnh trở nên tốn kém và làm giảm tính linh hoạt.

Tinh chỉnh là một thực hành phổ biến trong các hệ thống học máy, nơi chúng ta lấy một mô hình đã đào tạo trước và đào tạo lại nó với dữ liệu mới để cải thiện hiệu suất trên một nhiệm vụ cụ thể. Trong bối cảnh các mô hình ngôn ngữ, chúng ta có thể tinh chỉnh mô hình đã đào tạo trước _với một bộ ví dụ được tuyển chọn cho một nhiệm vụ hoặc lĩnh vực ứng dụng cụ thể_ để tạo ra một **mô hình tùy chỉnh** có thể chính xác và phù hợp hơn cho nhiệm vụ hoặc lĩnh vực đó. Một lợi ích phụ của việc tinh chỉnh là nó có thể giảm số lượng ví dụ cần thiết cho học với vài ví dụ - giảm việc sử dụng token và các chi phí liên quan.

## Khi nào và tại sao chúng ta nên tinh chỉnh mô hình?

Trong _bối cảnh này_, khi nói về tinh chỉnh, chúng ta đang ám chỉ tới **tinh chỉnh có giám sát** trong đó việc đào tạo lại được thực hiện bằng cách **thêm dữ liệu mới** mà không có trong tập dữ liệu đào tạo ban đầu. Điều này khác với phương pháp tinh chỉnh không giám sát, nơi mô hình được đào tạo lại trên dữ liệu gốc nhưng với các siêu tham số khác nhau.

Điều quan trọng cần nhớ là tinh chỉnh là một kỹ thuật nâng cao đòi hỏi trình độ chuyên môn nhất định để đạt được kết quả mong muốn. Nếu làm không đúng, nó có thể không mang lại cải thiện như mong đợi, thậm chí làm giảm hiệu suất của mô hình trên lĩnh vực mục tiêu của bạn.

Vì vậy, trước khi học "cách" tinh chỉnh mô hình ngôn ngữ, bạn cần biết "tại sao" bạn nên chọn con đường này, và "khi nào" nên bắt đầu quá trình tinh chỉnh. Hãy bắt đầu bằng cách tự hỏi những câu hỏi sau:

- **Trường Hợp Sử Dụng**: Bạn có _trường hợp sử dụng_ gì cho việc tinh chỉnh? Khía cạnh nào của mô hình đã đào tạo trước hiện tại bạn muốn cải thiện?
- **Các Phương án Thay Thế**: Bạn đã thử _các kỹ thuật khác_ để đạt được kết quả mong muốn chưa? Hãy dùng chúng để tạo một chuẩn so sánh.
  - Kỹ thuật nhắc lệnh: Thử các kỹ thuật như cung cấp vài ví dụ làm nhắc lệnh phù hợp. Đánh giá chất lượng câu trả lời.
  - Tăng cường sinh dựa trên truy xuất: Thử bổ sung các nhắc lệnh với kết quả truy vấn tìm kiếm dữ liệu của bạn. Đánh giá chất lượng câu trả lời.
- **Chi phí**: Bạn đã xác định được chi phí cho việc tinh chỉnh chưa?
  - Khả năng tinh chỉnh - mô hình đã đào tạo trước có được phép tinh chỉnh không?
  - Nỗ lực - để chuẩn bị dữ liệu đào tạo, đánh giá & tinh chỉnh mô hình.
  - Tính toán - để chạy các công việc tinh chỉnh và triển khai mô hình đã tinh chỉnh
  - Dữ liệu - có quyền truy cập vào đủ ví dụ chất lượng để tinh chỉnh không
- **Lợi ích**: Bạn đã xác nhận lợi ích của việc tinh chỉnh chưa?
  - Chất lượng - mô hình tinh chỉnh có vượt trội so với chuẩn không?
  - Chi phí - việc này có giảm sử dụng token bằng cách đơn giản hóa nhắc lệnh không?
  - Khả năng mở rộng - bạn có thể tái sử dụng mô hình gốc cho các lĩnh vực mới không?

Bằng cách trả lời những câu hỏi này, bạn sẽ có thể quyết định liệu tinh chỉnh có phải là phương pháp phù hợp cho trường hợp sử dụng của bạn hay không. Lý tưởng nhất, phương pháp này chỉ có giá trị khi lợi ích vượt trội hơn chi phí. Khi đã quyết định tiến hành, đã đến lúc nghĩ về _cách_ bạn có thể tinh chỉnh mô hình đã đào tạo trước.

Muốn có thêm hiểu biết về quy trình ra quyết định? Xem [Tinh chỉnh hay không tinh chỉnh](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Làm thế nào để tinh chỉnh một mô hình đã được đào tạo trước?

Để tinh chỉnh một mô hình đã đào tạo trước, bạn cần có:

- một mô hình đã đào tạo trước để tinh chỉnh
- một tập dữ liệu dùng cho việc tinh chỉnh
- một môi trường đào tạo để chạy công việc tinh chỉnh
- một môi trường lưu trữ để triển khai mô hình đã tinh chỉnh

## Tinh Chỉnh Trong Thực Tế

> **Lưu ý:** `gpt-35-turbo` / `gpt-3.5-turbo`, được nhắc đến trong một số hướng dẫn dưới đây, đã ngừng sử dụng cho cả suy luận và tinh chỉnh. Nếu bạn bắt đầu một công việc tinh chỉnh mới hôm nay, hãy chọn mô hình hiện đang được hỗ trợ - ví dụ `gpt-4o-mini` hoặc `gpt-4.1-mini`. Xem [Danh sách các mô hình có thể tinh chỉnh](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) để biết các mô hình có thể tinh chỉnh hiện tại. Các khái niệm và bước thực hiện trong các hướng dẫn này vẫn áp dụng.

Các tài nguyên sau đây cung cấp các hướng dẫn từng bước giúp bạn làm quen với một ví dụ thực tế bằng cách sử dụng một mô hình được chọn cùng với tập dữ liệu được tuyển chọn. Để làm theo các hướng dẫn này, bạn cần tài khoản trên nhà cung cấp cụ thể, cùng quyền truy cập vào mô hình và tập dữ liệu liên quan.

| Nhà Cung Cấp     | Hướng Dẫn                                                                                                                                                                       | Mô Tả                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cách tinh chỉnh mô hình chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Học cách tinh chỉnh `gpt-35-turbo` cho một lĩnh vực cụ thể ("trợ lý công thức") bằng cách chuẩn bị dữ liệu đào tạo, chạy công việc tinh chỉnh và dùng mô hình tinh chỉnh cho suy luận.                                                                                                                                                                                                                                       |
| Azure OpenAI | [Hướng dẫn tinh chỉnh GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Học cách tinh chỉnh mô hình `gpt-35-turbo-0613` **trên Azure** bằng cách thực hiện các bước tạo & tải lên dữ liệu đào tạo, chạy công việc tinh chỉnh. Triển khai & sử dụng mô hình mới.                                                                                                                                                                                                                                        |
| Hugging Face | [Tinh chỉnh LLMs với Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bài viết blog này hướng dẫn bạn tinh chỉnh một _mô hình LLM mở_ (ví dụ `CodeLlama 7B`) sử dụng thư viện [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) với các [tập dữ liệu](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) mở trên Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Tinh chỉnh LLMs với AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (hoặc AutoTrain Advanced) là thư viện python do Hugging Face phát triển cho phép tinh chỉnh nhiều nhiệm vụ khác nhau bao gồm tinh chỉnh LLMs. AutoTrain là giải pháp không-code và có thể chạy tinh chỉnh trên đám mây riêng, trên Hugging Face Spaces hoặc cục bộ. Nó hỗ trợ giao diện GUI trên web, CLI và đào tạo qua các file cấu hình yaml.                                                                         |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Tinh chỉnh LLMs với Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth là một khuôn khổ mã nguồn mở hỗ trợ tinh chỉnh LLM và học tăng cường (RL). Unsloth đơn giản hóa việc đào tạo cục bộ, đánh giá và triển khai với các [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) sẵn sàng sử dụng. Nó cũng hỗ trợ chuyển văn bản thành giọng nói (TTS), BERT và mô hình đa phương tiện. Để bắt đầu, đọc hướng dẫn từng bước của họ về [Tinh Chỉnh LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Bài Tập

Chọn một trong các hướng dẫn trên và làm theo. _Chúng tôi có thể sao chép phiên bản các hướng dẫn này vào Jupyter Notebooks trong repo này chỉ để tham khảo. Vui lòng sử dụng nguồn gốc chính thức để có các phiên bản mới nhất_.

## Làm Tốt Lắm! Tiếp Tục Học Tập.

Sau khi hoàn thành bài học này, hãy khám phá bộ sưu tập [Học Tập AI Tạo Sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo Sinh của bạn!

Chúc mừng!! Bạn đã hoàn thành bài học cuối cùng trong chuỗi v2 của khóa học này! Đừng ngừng học và xây dựng. \*\*Hãy xem trang [TÀI NGUYÊN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có danh sách các đề xuất bổ sung chỉ về chủ đề này.

Chuỗi bài học v1 của chúng tôi cũng đã được cập nhật với thêm bài tập và khái niệm. Vậy nên hãy dành một chút thời gian để làm mới kiến thức - và vui lòng [chia sẻ câu hỏi và phản hồi của bạn](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) để giúp chúng tôi cải thiện các bài học này cho cộng đồng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->