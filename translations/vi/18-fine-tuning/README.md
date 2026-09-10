[![Các Mô Hình Mã Nguồn Mở](../../../translated_images/vi/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Tinh Chỉnh Mô Hình Ngôn Ngữ Lớn Của Bạn

Việc sử dụng các mô hình ngôn ngữ lớn để xây dựng các ứng dụng AI sinh tạo gặp phải những thách thức mới. Một vấn đề then chốt là đảm bảo chất lượng phản hồi (độ chính xác và sự phù hợp) trong nội dung do mô hình tạo ra cho một yêu cầu người dùng nhất định. Trong các bài học trước, chúng ta đã thảo luận về các kỹ thuật như kỹ thuật tạo prompt và tạo sinh hỗ trợ truy xuất dữ liệu nhằm giải quyết vấn đề bằng cách _chỉnh sửa đầu vào prompt_ cho mô hình hiện có.

Trong bài học hôm nay, chúng ta sẽ bàn về kỹ thuật thứ ba, **tinh chỉnh**, nhằm giải quyết thách thức bằng cách _đào tạo lại mô hình_ với dữ liệu bổ sung. Hãy cùng tìm hiểu chi tiết.

## Mục Tiêu Học Tập

Bài học này giới thiệu khái niệm tinh chỉnh cho các mô hình ngôn ngữ đã được huấn luyện trước, khám phá lợi ích và thách thức của phương pháp này, và cung cấp hướng dẫn về khi nào và cách sử dụng tinh chỉnh để nâng cao hiệu suất các mô hình AI sinh tạo của bạn.

Kết thúc bài học này, bạn sẽ có thể trả lời các câu hỏi sau:

- Tinh chỉnh mô hình ngôn ngữ là gì?
- Khi nào và tại sao việc tinh chỉnh lại hữu ích?
- Làm thế nào để tôi tinh chỉnh một mô hình đã được huấn luyện trước?
- Những hạn chế của việc tinh chỉnh là gì?

Sẵn sàng chưa? Bắt đầu thôi.

## Hướng Dẫn Minh Họa

Muốn có cái nhìn tổng quan về những gì sẽ học trước khi đi sâu? Hãy xem hướng dẫn minh họa này mô tả hành trình học tập cho bài học này - từ việc học các khái niệm cốt lõi và động lực tinh chỉnh, đến hiểu quy trình và các thực hành tốt nhất để thực hiện nhiệm vụ tinh chỉnh. Đây là chủ đề hấp dẫn để khám phá, đừng quên xem trang [Tài nguyên](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có thêm các liên kết hỗ trợ cho hành trình học tự hướng dẫn của bạn!

![Hướng Dẫn Minh Họa Tinh Chỉnh Mô Hình Ngôn Ngữ](../../../translated_images/vi/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Tinh Chỉnh Mô Hình Ngôn Ngữ Là Gì?

Theo định nghĩa, các mô hình ngôn ngữ lớn được _huấn luyện trước_ trên một lượng lớn văn bản đa dạng có nguồn từ internet và các nguồn khác. Như chúng ta đã học trong các bài trước, cần các kỹ thuật như _kỹ thuật tạo prompt_ và _tạo sinh hỗ trợ truy xuất dữ liệu_ để cải thiện chất lượng phản hồi của mô hình cho các câu hỏi ("prompt") của người dùng.

Một kỹ thuật tạo prompt phổ biến là cung cấp cho mô hình thêm hướng dẫn về những gì mong đợi trong phản hồi, thông qua _hướng dẫn_ (chỉ dẫn rõ ràng) hoặc _cung cấp một vài ví dụ_ (hướng dẫn ngụ ý). Đây gọi là _học theo mẫu ít_ nhưng có hai hạn chế:

- Giới hạn số token của mô hình có thể hạn chế số lượng ví dụ bạn có thể cung cấp và hiệu quả.
- Chi phí token của mô hình làm cho việc thêm ví dụ vào mỗi prompt trở nên đắt đỏ và hạn chế tính linh hoạt.

Tinh chỉnh là thực hành phổ biến trong hệ thống học máy, nơi chúng ta lấy mô hình đã được huấn luyện trước và đào tạo lại với dữ liệu mới để cải thiện hiệu suất trên một nhiệm vụ cụ thể. Trong bối cảnh mô hình ngôn ngữ, ta có thể tinh chỉnh mô hình huấn luyện trước _với một bộ ví dụ được chọn lọc cho một tác vụ hoặc miền ứng dụng_ để tạo ra một **mô hình tùy chỉnh** chính xác và phù hợp hơn với tác vụ hay miền đó. Một lợi ích phụ của tinh chỉnh là nó có thể giảm số lượng ví dụ cần thiết cho học theo mẫu ít - giảm sử dụng token và chi phí liên quan.

## Khi nào và tại sao nên tinh chỉnh mô hình?

Trong _trường hợp này_, nói về tinh chỉnh là ám chỉ **tinh chỉnh có giám sát**, tức đào tạo lại bằng cách **thêm dữ liệu mới** không có trong tập dữ liệu huấn luyện gốc. Điều này khác với tinh chỉnh không giám sát, khi mô hình được đào tạo lại trên dữ liệu gốc nhưng với các siêu tham số khác nhau.

Điều quan trọng cần nhớ là tinh chỉnh là một kỹ thuật nâng cao đòi hỏi một mức độ chuyên môn nhất định để đạt kết quả mong muốn. Nếu làm sai, nó có thể không mang lại cải tiến như mong đợi và thậm chí làm giảm hiệu suất mô hình cho miền bạn nhắm đến.

Vì vậy, trước khi học "cách" tinh chỉnh mô hình ngôn ngữ, bạn cần biết "tại sao" nên đi theo con đường này, và "khi nào" bắt đầu quy trình tinh chỉnh. Hãy bắt đầu bằng việc tự hỏi các câu hỏi sau:

- **Trường hợp sử dụng**: Trường hợp _sử dụng_ của bạn cho tinh chỉnh là gì? Bạn muốn cải thiện khía cạnh nào của mô hình huấn luyện trước hiện tại?
- **Các lựa chọn thay thế**: Bạn đã thử _các kỹ thuật khác_ để đạt kết quả mong muốn chưa? Sử dụng chúng để tạo nền so sánh.
  - Kỹ thuật tạo prompt: Thử các phương pháp như few-shot với các ví dụ prompt phù hợp. Đánh giá chất lượng phản hồi.
  - Tạo sinh hỗ trợ truy xuất: Thử bổ sung prompt với kết quả truy vấn dựa trên dữ liệu của bạn. Đánh giá chất lượng phản hồi.
- **Chi phí**: Bạn đã xác định được chi phí của việc tinh chỉnh chưa?
  - Tính khả thi - mô hình huấn luyện trước có cho phép tinh chỉnh không?
  - Công sức - chuẩn bị dữ liệu huấn luyện, đánh giá & tinh chỉnh mô hình.
  - Tính toán - cho việc chạy các job tinh chỉnh và triển khai mô hình tinh chỉnh.
  - Dữ liệu - truy cập đủ ví dụ chất lượng cho tác động tinh chỉnh.
- **Lợi ích**: Bạn đã xác nhận lợi ích của tinh chỉnh chưa?
  - Chất lượng - mô hình tinh chỉnh có vượt trội so với nền tảng không?
  - Chi phí - có giúp giảm sử dụng token bằng cách đơn giản hóa prompt không?
  - Khả năng mở rộng - có thể tái sử dụng mô hình cơ sở cho các lĩnh vực mới không?

Bằng cách trả lời các câu hỏi này, bạn sẽ quyết định được tinh chỉnh có phải là phương án phù hợp cho trường hợp của bạn không. Tốt nhất, phương án chỉ hợp lý nếu lợi ích vượt chi phí. Khi bạn quyết định tiến hành, hãy suy nghĩ về _cách_ để tinh chỉnh mô hình đã huấn luyện trước.

Muốn có thêm cái nhìn sâu sắc về quá trình ra quyết định? Xem [Tinh chỉnh hay không tinh chỉnh](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Làm thế nào để tinh chỉnh một mô hình huấn luyện trước?

Để tinh chỉnh một mô hình đã huấn luyện trước, bạn cần có:

- một mô hình đã huấn luyện trước để tinh chỉnh
- một bộ dữ liệu để dùng cho tinh chỉnh
- môi trường đào tạo để chạy công việc tinh chỉnh
- môi trường lưu trữ để triển khai mô hình tinh chỉnh

## Tinh Chỉnh trên Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) là nơi bạn tinh chỉnh, triển khai và quản lý các mô hình tùy chỉnh trên Azure hiện nay (nơi này kết hợp Azure OpenAI Studio và Azure AI Studio trước đây). Trước khi bắt đầu công việc, bạn nên hiểu các lựa chọn Foundry cung cấp - cùng các thực hành tốt nhất được nền tảng khuyến nghị. Foundry sử dụng **LoRA (adaptation bậc thấp)** để tinh chỉnh mô hình hiệu quả, giúp việc đào tạo nhanh và tiết kiệm hơn việc đào tạo lại toàn bộ trọng số.

### Bước 1: Chọn kỹ thuật đào tạo

Foundry hỗ trợ ba kỹ thuật tinh chỉnh. **Bắt đầu với SFT** - nó bao quát phạm vi tình huống rộng nhất.

| Kỹ thuật | Công dụng | Khi nào sử dụng |
| --- | --- | --- |
| **Tinh Chỉnh Có Giám Sát (SFT)** | Đào tạo trên cặp ví dụ đầu vào/đầu ra để mô hình học cách tạo phản hồi bạn muốn. | Mặc định cho hầu hết nhiệm vụ: chuyên môn hóa miền, hiệu suất tác vụ, phong cách và giọng điệu, tuân theo hướng dẫn, và thích ứng ngôn ngữ. |
| **Tối Ưu Ưu Tiên Trực Tiếp (DPO)** | Học từ các cặp phản hồi _ưa thích và không ưa thích_ để điều chỉnh đầu ra phù hợp với sở thích con người. | Cải thiện chất lượng phản hồi, an toàn và sự phù hợp khi bạn có phản hồi so sánh. |
| **Tinh Chỉnh Tăng Cường (RFT)** | Sử dụng tín hiệu thưởng từ _người đánh giá_ để tối ưu hành vi phức tạp với học tăng cường. | Miền mục tiêu, đòi hỏi suy luận cao (toán, hóa học, vật lý) với câu trả lời đúng/sai rõ ràng. Yêu cầu chuyên môn ML nhiều hơn. |

### Bước 2: Chọn cấp độ đào tạo

Foundry cho phép chọn cách và nơi chạy đào tạo:

- **Chuẩn** - đào tạo ở vùng tài nguyên của bạn và đảm bảo dữ liệu nằm trong vùng đó. Dùng khi dữ liệu phải ở vị trí cụ thể.
- **Toàn cầu** - rẻ hơn và nhanh hơn khi xếp hàng nhờ dùng năng lực ngoài vùng vùng của bạn (dữ liệu và trọng số được sao chép vào vùng đào tạo). Mặc định tốt khi không yêu cầu vị trí dữ liệu.
- **Phát triển** - chi phí thấp nhất, dùng năng lực nhàn rỗi không đảm bảo độ trễ/SLA (các job có thể bị tạm dừng và tiếp tục). Lý tưởng cho thử nghiệm.

### Bước 3: Chọn mô hình cơ sở

Các mô hình có thể tinh chỉnh gồm OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, và `gpt-4.1-nano` (SFT; dòng 4o/4.1 cũng hỗ trợ DPO), các mô hình suy luận `o4-mini` và `gpt-5` (RFT), cùng các mô hình mã nguồn mở như `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, và `gpt-oss-20b` (SFT trên tài nguyên Foundry). Luôn kiểm tra [Danh sách mô hình tinh chỉnh hiện tại](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) để biết các phương pháp, vùng, và khả dụng được hỗ trợ.

> Foundry cung cấp hai hình thức: **không máy chủ** (giá dựa trên mức tiêu thụ, không quản lý hạn ngạch GPU, OpenAI và các mô hình chọn lọc) và **tính toán có quản lý** (mang theo VM của bạn qua Azure Machine Learning để có dải mô hình rộng nhất). Phần lớn nên bắt đầu với không máy chủ.

### Các thực hành tốt của Foundry

- **Đầu tiên thiết lập nền tảng.** Đo mô hình cơ sở với kỹ thuật tạo prompt và RAG _trước_ khi tinh chỉnh để chứng minh sự cải tiến.
- **Bắt đầu nhỏ rồi mở rộng.** Bắt đầu với 50-100 ví dụ chất lượng để xác minh phương pháp, sau đó mở rộng lên 500+ cho sản xuất. Chất lượng hơn số lượng - loại bỏ ví dụ kém chất lượng.
- **Định dạng dữ liệu chính xác.** Tệp huấn luyện và đánh giá phải là JSONL, UTF-8 **có BOM**, dưới 512 MB, dùng định dạng tin nhắn chat-completions. Luôn bao gồm tệp đánh giá để theo dõi hiện tượng overfitting.
- **Giữ prompt hệ thống trong suy luận.** Dùng cùng tin nhắn hệ thống gọi mô hình mà bạn đã dùng trong huấn luyện.
- **Đánh giá điểm dừng - đừng chỉ triển khai điểm cuối cùng.** Foundry giữ ba epoch cuối làm điểm dừng triển khai; chọn điểm tổng quát tốt nhất bằng cách theo dõi `train_loss` / `valid_loss` và độ chính xác token.
- **Đo chi phí token cùng chất lượng** khi so sánh mô hình tinh chỉnh với nền tảng.
- **Lặp lại với tinh chỉnh liên tục.** Bạn có thể tinh chỉnh mô hình đã tinh chỉnh trên dữ liệu mới (hỗ trợ cho mô hình OpenAI).
- **Chú ý chi phí lưu trữ.** Mô hình tùy chỉnh triển khai tính phí theo giờ, và triển khai không hoạt động sẽ bị xoá sau 15 ngày - hãy dọn dẹp những gì không cần.

Làm theo hướng dẫn toàn diện trong [Tùy chỉnh mô hình với tinh chỉnh](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), và xem các hướng dẫn cho [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) và [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) khi bạn sẵn sàng với các kỹ thuật khác.

## Tinh Chỉnh Trong Thực Tế

Các tài nguyên sau cung cấp hướng dẫn từng bước cùng ví dụ thực tế trên các mô hình hiện đang được hỗ trợ với bộ dữ liệu được chọn lọc. Để thực hành theo, bạn cần có tài khoản trên nhà cung cấp cụ thể, cùng quyền truy cập mô hình và bộ dữ liệu tương ứng.

| Nhà cung cấp | Hướng dẫn                                                                                                                                                                      | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cách tinh chỉnh mô hình chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Học cách tinh chỉnh một mô hình chat OpenAI gần đây cho một miền cụ thể ("trợ lý nấu ăn") bằng cách chuẩn bị dữ liệu huấn luyện, chạy công việc tinh chỉnh, và dùng mô hình tinh chỉnh để suy luận.                                                                                                                                                                                                                                      |
| Microsoft Foundry | [Tùy chỉnh mô hình với tinh chỉnh](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Học cách tinh chỉnh một mô hình hiện được hỗ trợ như `gpt-4.1-mini` **trên Azure** với Microsoft Foundry: chuẩn bị và tải lên dữ liệu huấn luyện và đánh giá, chạy công việc tinh chỉnh, sau đó triển khai và sử dụng mô hình mới.                                                                                                                                                                                                        |

| Hugging Face | [Điều chỉnh tinh chỉnh LLMs với Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bài đăng blog này hướng dẫn bạn điều chỉnh tinh chỉnh một _LLM mở_ (ví dụ: `CodeLlama 7B`) sử dụng thư viện [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) với các [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) mở trên Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Điều chỉnh tinh chỉnh LLMs với AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (hoặc AutoTrain Advanced) là một thư viện python do Hugging Face phát triển cho phép tinh chỉnh cho nhiều tác vụ khác nhau bao gồm cả tinh chỉnh LLM. AutoTrain là giải pháp không cần mã hóa và việc tinh chỉnh có thể được thực hiện trên đám mây riêng của bạn, trên Hugging Face Spaces hoặc cục bộ. Nó hỗ trợ cả giao diện web, CLI và đào tạo thông qua các tệp cấu hình yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Điều chỉnh tinh chỉnh LLMs với Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth là một framework mã nguồn mở hỗ trợ tinh chỉnh LLM và học tăng cường (RL). Unsloth đơn giản hóa việc đào tạo cục bộ, đánh giá và triển khai với các [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) sẵn sàng sử dụng. Nó cũng hỗ trợ chuyển văn bản thành giọng nói (TTS), các mô hình BERT và mô hình đa phương tiện. Để bắt đầu, hãy đọc [Hướng dẫn Tinh chỉnh LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) từng bước của họ.                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Bài tập

Chọn một trong các hướng dẫn ở trên và làm theo. _Chúng tôi có thể sao chép một phiên bản của các hướng dẫn này trong các Jupyter Notebooks trong kho này chỉ để tham khảo. Vui lòng sử dụng nguồn gốc ban đầu trực tiếp để có phiên bản mới nhất_.

## Làm tốt lắm! Tiếp tục học tập của bạn.

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI tạo sinh!

Chúc mừng!! Bạn đã hoàn thành bài học cuối cùng trong loạt bài v2 cho khóa học này! Đừng ngừng học và xây dựng. \*\*Hãy xem trang [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) để có danh sách các đề xuất bổ sung chỉ cho chủ đề này.

Loạt bài v1 của chúng tôi cũng đã được cập nhật với nhiều bài tập và khái niệm hơn. Vì vậy, hãy dành một phút để làm mới kiến thức của bạn - và vui lòng [chia sẻ câu hỏi và phản hồi của bạn](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) để giúp chúng tôi cải thiện các bài học này cho cộng đồng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->