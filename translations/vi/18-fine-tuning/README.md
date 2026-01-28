<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:34:31+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "vi"
}
-->
[![Open Source Models](../../../../../translated_images/vi/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Tinh Chỉnh Lại Mô Hình Ngôn Ngữ Lớn Của Bạn

Sử dụng các mô hình ngôn ngữ lớn để xây dựng các ứng dụng AI sinh tạo đi kèm với những thách thức mới. Một vấn đề then chốt là đảm bảo chất lượng phản hồi (độ chính xác và sự phù hợp) trong nội dung được mô hình tạo ra cho yêu cầu của người dùng. Trong các bài học trước, chúng ta đã thảo luận về các kỹ thuật như kỹ thuật prompt và sinh tạo tăng cường truy xuất, những kỹ thuật này cố gắng giải quyết vấn đề bằng cách _chỉnh sửa đầu vào prompt_ cho mô hình hiện có.

Trong bài học hôm nay, chúng ta sẽ thảo luận về kỹ thuật thứ ba, **tinh chỉnh lại (fine-tuning)**, kỹ thuật này cố gắng giải quyết thách thức bằng cách _huấn luyện lại chính mô hình_ với dữ liệu bổ sung. Hãy cùng tìm hiểu chi tiết.

## Mục Tiêu Học Tập

Bài học này giới thiệu khái niệm về tinh chỉnh lại đối với các mô hình ngôn ngữ đã được huấn luyện trước, khám phá lợi ích và thách thức của phương pháp này, và cung cấp hướng dẫn về thời điểm và cách sử dụng tinh chỉnh lại để cải thiện hiệu suất của các mô hình AI sinh tạo của bạn.

Kết thúc bài học này, bạn sẽ có thể trả lời các câu hỏi sau:

- Tinh chỉnh lại mô hình ngôn ngữ là gì?
- Khi nào và tại sao nên sử dụng tinh chỉnh lại?
- Làm thế nào để tinh chỉnh lại một mô hình đã được huấn luyện trước?
- Những hạn chế của việc tinh chỉnh lại là gì?

Sẵn sàng chưa? Bắt đầu thôi.

## Hướng Dẫn Minh Họa

Muốn có cái nhìn tổng quan về những gì chúng ta sẽ học trước khi đi vào chi tiết? Hãy xem hướng dẫn minh họa này mô tả hành trình học tập của bài học - từ việc tìm hiểu các khái niệm cốt lõi và động lực cho việc tinh chỉnh lại, đến hiểu quy trình và các thực hành tốt nhất để thực hiện tác vụ tinh chỉnh lại. Đây là chủ đề hấp dẫn để khám phá, đừng quên truy cập trang [Tài nguyên](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có thêm các liên kết hỗ trợ hành trình tự học của bạn!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/vi/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Tinh chỉnh lại mô hình ngôn ngữ là gì?

Theo định nghĩa, các mô hình ngôn ngữ lớn được _huấn luyện trước_ trên số lượng lớn văn bản lấy từ nhiều nguồn đa dạng bao gồm cả internet. Như chúng ta đã học trong các bài học trước, ta cần các kỹ thuật như _kỹ thuật prompt_ và _sinh tạo tăng cường truy xuất_ để cải thiện chất lượng phản hồi của mô hình đối với các câu hỏi ("prompt") của người dùng.

Một kỹ thuật phổ biến trong kỹ thuật prompt là cung cấp cho mô hình nhiều hướng dẫn hơn về những gì mong đợi trong phản hồi, bằng cách cung cấp _hướng dẫn_ (hướng dẫn rõ ràng) hoặc _cho vài ví dụ_ (hướng dẫn ngầm). Điều này gọi là _học ít ví dụ (few-shot learning)_ nhưng có hai hạn chế:

- Giới hạn token của mô hình có thể hạn chế số lượng ví dụ bạn có thể cung cấp, làm giảm hiệu quả.
- Chi phí token của mô hình có thể khiến việc thêm ví dụ vào mỗi prompt trở nên tốn kém, hạn chế tính linh hoạt.

Tinh chỉnh lại là một thực tiễn phổ biến trong các hệ thống máy học, nơi ta lấy một mô hình đã được huấn luyện trước và huấn luyện lại nó với dữ liệu mới để cải thiện hiệu suất trên nhiệm vụ cụ thể. Trong bối cảnh mô hình ngôn ngữ, ta có thể tinh chỉnh mô hình đã huấn luyện trước _với bộ dữ liệu được lựa chọn kỹ cho một nhiệm vụ hoặc lĩnh vực ứng dụng cụ thể_ để tạo ra một **mô hình tùy chỉnh** có thể chính xác và phù hợp hơn cho nhiệm vụ hoặc lĩnh vực đó. Một lợi ích phụ của tinh chỉnh lại là nó cũng có thể giảm số lượng ví dụ cần thiết cho học ít ví dụ — giúp tiết kiệm token và chi phí liên quan.

## Khi nào và tại sao nên tinh chỉnh lại mô hình?

Trong _bối cảnh này_, khi chúng ta nói về tinh chỉnh lại, ta đang nói đến **tinh chỉnh có giám sát**, nơi việc huấn luyện lại được thực hiện bằng cách **thêm dữ liệu mới** mà không có trong bộ dữ liệu huấn luyện gốc. Điều này khác với phương pháp tinh chỉnh không giám sát, nơi mô hình được huấn luyện lại trên dữ liệu gốc nhưng với siêu tham số (hyperparameters) khác nhau.

Điều quan trọng cần nhớ là tinh chỉnh lại là kỹ thuật nâng cao đòi hỏi trình độ chuyên môn nhất định để đạt được kết quả mong muốn. Nếu làm không đúng cách, nó có thể không mang lại cải thiện như kỳ vọng, thậm chí có thể làm giảm hiệu suất của mô hình đối với lĩnh vực mục tiêu của bạn.

Vì vậy, trước khi học "cách" tinh chỉnh lại mô hình ngôn ngữ, bạn cần biết "tại sao" bạn nên lựa chọn con đường này, và "khi nào" bắt đầu quá trình tinh chỉnh lại. Bắt đầu bằng cách tự hỏi bản thân các câu hỏi sau:

- **Trường hợp sử dụng**: Trường hợp sử dụng _tinh chỉnh lại_ của bạn là gì? Bạn muốn cải thiện khía cạnh nào của mô hình đã được huấn luyện trước hiện tại?
- **Các lựa chọn thay thế**: Bạn đã thử _các kỹ thuật khác_ để đạt được kết quả mong muốn chưa? Dùng chúng để tạo cơ sở so sánh.
  - Kỹ thuật prompt: Thử kỹ thuật học ít ví dụ với các ví dụ về các phản hồi prompt phù hợp. Đánh giá chất lượng phản hồi.
  - Sinh tạo tăng cường truy xuất: Thử bổ sung prompt với các kết quả truy vấn được lấy từ dữ liệu của bạn. Đánh giá chất lượng phản hồi.
- **Chi phí**: Bạn đã xác định chi phí cho việc tinh chỉnh lại chưa?
  - Khả năng tinh chỉnh - mô hình đã huấn luyện trước có sẵn để tinh chỉnh không?
  - Nỗ lực - chuẩn bị dữ liệu huấn luyện, đánh giá & tinh chỉnh mô hình.
  - Tính toán - chạy các tác vụ tinh chỉnh lại và triển khai mô hình đã tinh chỉnh.
  - Dữ liệu - có đủ các ví dụ chất lượng cao cho tác động tinh chỉnh không?
- **Lợi ích**: Bạn đã xác nhận lợi ích của việc tinh chỉnh lại chưa?
  - Chất lượng - mô hình đã tinh chỉnh có vượt trội hơn so với cơ sở không?
  - Chi phí - có giảm sử dụng token bằng cách đơn giản hóa prompt không?
  - Khả năng mở rộng - bạn có thể tái sử dụng mô hình cơ sở cho các lĩnh vực mới không?

Bằng cách trả lời các câu hỏi này, bạn sẽ có thể quyết định liệu tinh chỉnh lại có phải là phương pháp phù hợp cho trường hợp sử dụng của bạn không. Lý tưởng nhất, phương pháp này chỉ hợp lý nếu lợi ích vượt quá chi phí. Khi bạn quyết định tiến hành, đã đến lúc suy nghĩ về _cách_ bạn có thể tinh chỉnh lại mô hình đã huấn luyện trước.

Muốn có thêm cái nhìn về quá trình ra quyết định? Xem video [Tinh chỉnh hay không tinh chỉnh](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Làm thế nào để tinh chỉnh một mô hình đã được huấn luyện trước?

Để tinh chỉnh lại một mô hình đã được huấn luyện trước, bạn cần có:

- một mô hình đã được huấn luyện trước để tinh chỉnh
- một bộ dữ liệu để dùng cho việc tinh chỉnh
- một môi trường huấn luyện để chạy tác vụ tinh chỉnh
- một môi trường lưu trữ để triển khai mô hình đã tinh chỉnh

## Tinh chỉnh lại trong thực tế

Các tài nguyên dưới đây cung cấp các hướng dẫn từng bước để bạn thực hành với ví dụ thực tế sử dụng một mô hình được chọn với bộ dữ liệu được tuyển chọn. Để thực hành theo các hướng dẫn này, bạn cần có tài khoản trên nhà cung cấp tương ứng, cùng quyền truy cập tới mô hình và bộ dữ liệu liên quan.

| Nhà cung cấp | Hướng dẫn                                                                                                                                                                      | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cách tinh chỉnh các mô hình chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)            | Học cách tinh chỉnh mô hình `gpt-35-turbo` cho một lĩnh vực cụ thể ("trợ lý công thức nấu ăn") bằng cách chuẩn bị dữ liệu huấn luyện, chạy tác vụ tinh chỉnh, và dùng mô hình đã tinh chỉnh để suy luận.                                                                                                                                                                                                                      |
| Azure OpenAI | [Hướng dẫn tinh chỉnh GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Học cách tinh chỉnh mô hình `gpt-35-turbo-0613` **trên Azure** bằng cách tạo & tải lên dữ liệu huấn luyện, chạy tác vụ tinh chỉnh. Triển khai & sử dụng mô hình mới.                                                                                                                                                                                                                                                        |
| Hugging Face | [Tinh chỉnh LLM với Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                              | Bài đăng blog này hướng dẫn bạn tinh chỉnh một _mô hình LLM mở_ (ví dụ: `CodeLlama 7B`) sử dụng thư viện [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) cùng với các [bộ dữ liệu](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) trên Hugging Face. |
|              |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🤗 AutoTrain | [Tinh chỉnh LLM với AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                          | AutoTrain (hoặc AutoTrain Advanced) là thư viện python do Hugging Face phát triển cho phép tinh chỉnh nhiều tác vụ khác nhau trong đó có tinh chỉnh LLM. AutoTrain là giải pháp không cần mã, và bạn có thể tinh chỉnh trên đám mây của bạn, trên Hugging Face Spaces hoặc tại máy. Nó hỗ trợ giao diện web GUI, CLI và huấn luyện bằng file cấu hình yaml.                                                                                 |
|              |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🦥 Unsloth | [Tinh chỉnh LLM với Unsloth](https://github.com/unslothai/unsloth)                                                         | Unsloth là framework mã nguồn mở hỗ trợ tinh chỉnh LLM và học tăng cường (RL). Unsloth giúp đơn giản hóa việc huấn luyện, đánh giá và triển khai cục bộ với các [notebook](https://github.com/unslothai/notebooks) sẵn có. Nó còn hỗ trợ mô hình chuyển văn bản thành giọng nói (TTS), BERT và mô hình đa phương tiện. Để bắt đầu, đọc hướng dẫn [Tinh chỉnh LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) từng bước của họ.                                                                         |
|              |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
## Bài Tập

Chọn một trong những hướng dẫn trên và thực hành theo. _Chúng tôi có thể lặp lại phiên bản của các hướng dẫn này trong Jupyter Notebook trong repo này cho mục đích tham khảo. Vui lòng sử dụng nguồn gốc gốc trực tiếp để có phiên bản mới nhất_.

## Tuyệt vời! Tiếp tục Học Tập

Sau khi hoàn thành bài học này, hãy truy cập bộ sưu tập [Học Tập AI Sinh Tạo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI sinh tạo!

Chúc mừng!! Bạn đã hoàn thành bài học cuối cùng trong loạt bài v2 của khóa học này! Đừng ngừng học hỏi và phát triển. \*\*Hãy xem trang [TÀI NGUYÊN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có danh sách các gợi ý bổ sung chỉ cho chủ đề này.

Loạt bài v1 của chúng tôi cũng đã được cập nhật với nhiều bài tập và khái niệm hơn. Vậy nên hãy dành chút thời gian làm mới kiến thức — và vui lòng [chia sẻ câu hỏi và phản hồi của bạn](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) để giúp chúng tôi cải thiện các bài học này cho cộng đồng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo tính chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính thức. Đối với những thông tin quan trọng, khuyến nghị nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->