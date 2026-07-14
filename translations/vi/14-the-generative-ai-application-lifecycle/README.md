[![Tích hợp với gọi hàm](../../../translated_images/vi/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Vòng đời Ứng dụng AI Sinh Tạo

Một câu hỏi quan trọng đối với tất cả các ứng dụng AI là tính phù hợp của các tính năng AI, vì AI là một lĩnh vực phát triển nhanh chóng, để đảm bảo rằng ứng dụng của bạn luôn phù hợp, đáng tin cậy và mạnh mẽ, bạn cần giám sát, đánh giá và cải thiện nó liên tục. Đây là lúc vòng đời AI sinh tạo phát huy tác dụng.

Vòng đời AI sinh tạo là một khung hướng dẫn bạn qua các giai đoạn phát triển, triển khai và duy trì một ứng dụng AI sinh tạo. Nó giúp bạn xác định mục tiêu, đo lường hiệu suất, nhận diện các thách thức và triển khai các giải pháp. Nó cũng giúp bạn điều chỉnh ứng dụng với các tiêu chuẩn đạo đức và pháp lý của lĩnh vực và các bên liên quan. Bằng cách tuân theo vòng đời AI sinh tạo, bạn có thể đảm bảo ứng dụng của mình luôn mang lại giá trị và làm hài lòng người dùng.

## Giới thiệu

Trong chương này, bạn sẽ:

- Hiểu về sự chuyển dịch mô hình từ MLOps sang LLMOps
- Vòng đời LLM
- Công cụ vòng đời
- Đo lường và đánh giá vòng đời

## Hiểu về sự chuyển dịch mô hình từ MLOps sang LLMOps

LLMs là một công cụ mới trong kho vũ khí Trí tuệ Nhân tạo, chúng cực kỳ mạnh mẽ trong các nhiệm vụ phân tích và sinh tạo cho các ứng dụng, tuy nhiên sức mạnh này có những hệ quả trong cách chúng ta tối ưu hóa các nhiệm vụ AI và Học Máy cổ điển.

Với điều này, chúng ta cần một mô hình mới để thích ứng công cụ này một cách năng động, với các động lực phù hợp. Chúng ta có thể phân loại các ứng dụng AI cũ là "Ứng dụng ML" và các ứng dụng AI mới là "Ứng dụng GenAI" hoặc chỉ đơn giản là "Ứng dụng AI", phản ánh công nghệ và kỹ thuật chủ đạo được sử dụng trong thời điểm đó. Điều này thay đổi câu chuyện của chúng ta theo nhiều cách, hãy xem so sánh dưới đây.

![So sánh LLMOps và MLOps](../../../translated_images/vi/01-llmops-shift.29bc933cb3bb0080.webp)

Lưu ý rằng trong LLMOps, chúng ta tập trung nhiều hơn vào Nhà phát triển Ứng dụng, sử dụng tích hợp như một điểm then chốt, sử dụng "Models-as-a-Service" và suy nghĩ về các điểm sau cho các chỉ số.

- Chất lượng: Chất lượng phản hồi
- Tác hại: AI có trách nhiệm
- Trung thực: Tính cơ sở phản hồi (Phản hồi có hợp lý? Có chính xác không?)
- Chi phí: Ngân sách giải pháp
- Độ trễ: Thời gian trung bình phản hồi cho từng token

## Vòng đời LLM

Trước tiên, để hiểu vòng đời và các điều chỉnh, hãy lưu ý infographic sau.

![Infographic LLMOps](../../../translated_images/vi/02-llmops.70a942ead05a7645.webp)

Như bạn có thể nhận thấy, điều này khác với các Vòng đời thông thường của MLOps. LLMs có nhiều yêu cầu mới, như Prompting, các kỹ thuật khác nhau để cải thiện chất lượng (Fine-Tuning, RAG, Meta-Prompts), đánh giá và trách nhiệm với AI có trách nhiệm, cuối cùng là các chỉ số đánh giá mới (Chất lượng, Tác hại, Trung thực, Chi phí và Độ trễ).

Ví dụ, hãy xem cách chúng ta tưởng tượng ý tưởng. Sử dụng kỹ thuật prompt engineering để thử nghiệm với nhiều LLM khác nhau nhằm khám phá khả năng để kiểm tra xem Giả thuyết của họ có thể đúng không.

Lưu ý đây không phải là tuyến tính, mà là vòng lặp tích hợp, lặp đi lặp lại và có một chu kỳ tổng thể bao quát.

Chúng ta có thể khám phá các bước đó như thế nào? Hãy đi sâu vào chi tiết xem chúng ta xây dựng vòng đời ra sao.

![Luồng công việc LLMOps](../../../translated_images/vi/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Điều này có vẻ hơi phức tạp, hãy tập trung vào ba bước lớn trước.

1. Tưởng tượng/Khai phá: Khám phá, ở đây chúng ta có thể khám phá theo nhu cầu kinh doanh của mình. Tạo mẫu thử, xây dựng một [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) và kiểm tra xem nó có đủ hiệu quả cho Giả thuyết của chúng ta không.
1. Xây dựng/Bổ sung: Triển khai, bây giờ chúng ta bắt đầu đánh giá với bộ dữ liệu lớn hơn, triển khai các kỹ thuật như Fine-tuning và RAG, để kiểm tra độ bền của giải pháp. Nếu không ổn, tái triển khai, thêm các bước mới vào luồng hoặc tái cấu trúc dữ liệu, có thể giúp cải thiện. Sau khi thử nghiệm luồng và quy mô, nếu hoạt động tốt và kiểm tra các chỉ số, bước tiếp theo đã sẵn sàng.
1. Vận hành: Tích hợp, hiện thêm các hệ thống Giám sát và Cảnh báo cho hệ thống của chúng ta, triển khai và tích hợp ứng dụng vào Ứng dụng của chúng ta.

Sau đó, chúng ta có chu kỳ tổng thể của Quản lý, tập trung vào bảo mật, tuân thủ và quản trị.

Chúc mừng, giờ bạn đã có Ứng dụng AI sẵn sàng hoạt động. Để trải nghiệm thực tế, hãy xem [Demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Bây giờ, chúng ta có thể sử dụng những công cụ nào?

## Công cụ vòng đời

Về Công cụ, Microsoft cung cấp [Nền tảng Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) và [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) để hỗ trợ và làm cho chu trình của bạn dễ áp dụng và sẵn sàng.

[Nền tảng Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) cho phép bạn sử dụng [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (trước đây là Azure AI Studio) là một cổng web cho phép bạn khám phá các mô hình, mẫu và công cụ, quản lý tài nguyên, và sử dụng các luồng phát triển UI cũng như tùy chọn SDK/CLI cho phát triển hướng mã.

![Khả năng của Azure AI](../../../translated_images/vi/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI cho phép bạn sử dụng nhiều tài nguyên để quản lý các hoạt động, dịch vụ, dự án, tìm kiếm vector và nhu cầu cơ sở dữ liệu.

![LLMOps với Azure AI](../../../translated_images/vi/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Xây dựng, từ bằng chứng khái niệm (POC) đến các ứng dụng quy mô lớn với PromptFlow:

- Thiết kế và xây dựng ứng dụng từ VS Code, với các công cụ trực quan và chức năng
- Kiểm tra và tinh chỉnh ứng dụng của bạn để có AI chất lượng, dễ dàng.
- Sử dụng Microsoft Foundry để tích hợp và lặp lại trên cloud, đẩy và triển khai để tích hợp nhanh.

![LLMOps với PromptFlow](../../../translated_images/vi/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Tuyệt vời! Tiếp tục học hỏi!

Tuyệt vời, giờ hãy tìm hiểu thêm về cách chúng ta cấu trúc một ứng dụng để sử dụng các khái niệm với [Ứng dụng Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), để xem cách Cloud Advocacy thêm các khái niệm đó trong các buổi trình diễn. Để có thêm nội dung, xem buổi [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Bây giờ, xem Bài học 15, để hiểu cách [Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ảnh hưởng đến AI Sinh Tạo và để tạo các Ứng dụng hấp dẫn hơn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->