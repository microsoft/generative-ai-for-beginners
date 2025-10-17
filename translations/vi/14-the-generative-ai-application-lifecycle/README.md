<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T20:36:32+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "vi"
}
-->
[![Tích hợp với chức năng gọi](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.vi.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Vòng đời ứng dụng AI tạo sinh

Một câu hỏi quan trọng đối với tất cả các ứng dụng AI là mức độ phù hợp của các tính năng AI, vì đây là một lĩnh vực phát triển nhanh. Để đảm bảo ứng dụng của bạn luôn phù hợp, đáng tin cậy và mạnh mẽ, bạn cần theo dõi, đánh giá và cải thiện nó liên tục. Đây chính là lúc vòng đời AI tạo sinh phát huy tác dụng.

Vòng đời AI tạo sinh là một khung hướng dẫn bạn qua các giai đoạn phát triển, triển khai và duy trì một ứng dụng AI tạo sinh. Nó giúp bạn xác định mục tiêu, đo lường hiệu suất, nhận diện thách thức và thực hiện các giải pháp. Đồng thời, nó cũng giúp bạn điều chỉnh ứng dụng của mình theo các tiêu chuẩn đạo đức và pháp lý của lĩnh vực và các bên liên quan. Bằng cách tuân theo vòng đời AI tạo sinh, bạn có thể đảm bảo rằng ứng dụng của mình luôn mang lại giá trị và làm hài lòng người dùng.

## Giới thiệu

Trong chương này, bạn sẽ:

- Hiểu sự chuyển đổi từ MLOps sang LLMOps
- Vòng đời của LLM
- Công cụ hỗ trợ vòng đời
- Đo lường và đánh giá vòng đời

## Hiểu sự chuyển đổi từ MLOps sang LLMOps

LLM là một công cụ mới trong kho vũ khí của Trí tuệ Nhân tạo, chúng cực kỳ mạnh mẽ trong các nhiệm vụ phân tích và tạo nội dung cho ứng dụng. Tuy nhiên, sức mạnh này cũng mang lại một số hệ quả trong cách chúng ta tối ưu hóa các nhiệm vụ AI và Học máy cổ điển.

Với điều này, chúng ta cần một cách tiếp cận mới để thích nghi với công cụ này một cách linh hoạt, với các động lực phù hợp. Chúng ta có thể phân loại các ứng dụng AI cũ là "Ứng dụng ML" và các ứng dụng AI mới là "Ứng dụng GenAI" hoặc chỉ "Ứng dụng AI", phản ánh công nghệ và kỹ thuật chính thống được sử dụng tại thời điểm đó. Điều này thay đổi cách chúng ta nhìn nhận theo nhiều cách, hãy xem so sánh sau.

![So sánh LLMOps và MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.vi.png)

Lưu ý rằng trong LLMOps, chúng ta tập trung nhiều hơn vào các nhà phát triển ứng dụng, sử dụng tích hợp như một điểm chính, sử dụng "Mô hình như một dịch vụ" và xem xét các điểm sau để đo lường:

- Chất lượng: Chất lượng phản hồi
- Tác hại: AI có trách nhiệm
- Trung thực: Phản hồi có cơ sở (Có hợp lý không? Có chính xác không?)
- Chi phí: Ngân sách giải pháp
- Độ trễ: Thời gian trung bình cho phản hồi token

## Vòng đời của LLM

Đầu tiên, để hiểu vòng đời và các thay đổi, hãy xem qua infographic sau.

![Infographic LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.vi.png)

Như bạn có thể thấy, điều này khác với các vòng đời thông thường của MLOps. LLM có nhiều yêu cầu mới, như kỹ thuật Prompting, các kỹ thuật khác nhau để cải thiện chất lượng (Fine-Tuning, RAG, Meta-Prompts), đánh giá và trách nhiệm với AI có trách nhiệm, cuối cùng là các chỉ số đánh giá mới (Chất lượng, Tác hại, Trung thực, Chi phí và Độ trễ).

Ví dụ, hãy xem cách chúng ta hình thành ý tưởng. Sử dụng kỹ thuật prompt engineering để thử nghiệm với các LLM khác nhau nhằm khám phá các khả năng và kiểm tra xem giả thuyết của họ có thể đúng hay không.

Lưu ý rằng đây không phải là một quy trình tuyến tính, mà là các vòng lặp tích hợp, lặp đi lặp lại và có một chu kỳ tổng thể.

Làm thế nào để chúng ta khám phá các bước này? Hãy đi vào chi tiết cách chúng ta xây dựng một vòng đời.

![Quy trình làm việc LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.vi.png)

Điều này có vẻ hơi phức tạp, hãy tập trung vào ba bước lớn trước.

1. Hình thành ý tưởng/Khám phá: Khám phá, ở đây chúng ta có thể khám phá theo nhu cầu kinh doanh của mình. Tạo mẫu, tạo [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) và kiểm tra xem nó có đủ hiệu quả cho giả thuyết của chúng ta không.
1. Xây dựng/Tăng cường: Triển khai, bây giờ, chúng ta bắt đầu đánh giá với các tập dữ liệu lớn hơn, triển khai các kỹ thuật như Fine-tuning và RAG để kiểm tra độ mạnh mẽ của giải pháp. Nếu không đạt, việc triển khai lại, thêm các bước mới vào quy trình hoặc tái cấu trúc dữ liệu có thể giúp ích. Sau khi kiểm tra quy trình và quy mô của chúng ta, nếu hoạt động và đáp ứng các chỉ số, nó đã sẵn sàng cho bước tiếp theo.
1. Vận hành: Tích hợp, bây giờ thêm hệ thống giám sát và cảnh báo vào hệ thống của chúng ta, triển khai và tích hợp ứng dụng vào ứng dụng của chúng ta.

Sau đó, chúng ta có chu kỳ tổng thể về Quản lý, tập trung vào bảo mật, tuân thủ và quản trị.

Chúc mừng, giờ bạn đã có ứng dụng AI sẵn sàng hoạt động. Để có trải nghiệm thực hành, hãy xem [Demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Bây giờ, chúng ta có thể sử dụng những công cụ nào?

## Công cụ hỗ trợ vòng đời

Về công cụ, Microsoft cung cấp [Nền tảng Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) và [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) để giúp bạn dễ dàng triển khai và sẵn sàng sử dụng vòng đời của mình.

[Nền tảng Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) cho phép bạn sử dụng [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio là một cổng web cho phép bạn khám phá các mô hình, mẫu và công cụ. Quản lý tài nguyên của bạn, các quy trình phát triển giao diện người dùng và các tùy chọn SDK/CLI cho phát triển ưu tiên mã.

![Khả năng của Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.vi.png)

Azure AI cho phép bạn sử dụng nhiều tài nguyên để quản lý hoạt động, dịch vụ, dự án, tìm kiếm vector và nhu cầu cơ sở dữ liệu.

![LLMOps với Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.vi.png)

Xây dựng, từ Proof-of-Concept (POC) đến các ứng dụng quy mô lớn với PromptFlow:

- Thiết kế và xây dựng ứng dụng từ VS Code, với các công cụ trực quan và chức năng
- Kiểm tra và tinh chỉnh ứng dụng của bạn để có AI chất lượng cao một cách dễ dàng.
- Sử dụng Azure AI Studio để tích hợp và lặp lại với đám mây, đẩy và triển khai để tích hợp nhanh chóng.

![LLMOps với PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.vi.png)

## Tuyệt vời! Tiếp tục học tập!

Thật tuyệt vời, bây giờ hãy tìm hiểu thêm về cách chúng ta cấu trúc một ứng dụng để sử dụng các khái niệm với [Ứng dụng Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), để xem cách Cloud Advocacy áp dụng các khái niệm này trong các buổi trình diễn. Để biết thêm nội dung, hãy xem [Phiên họp tại Ignite!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Bây giờ, hãy xem Bài học 15 để hiểu cách [Tạo nội dung tăng cường và cơ sở dữ liệu vector](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ảnh hưởng đến AI tạo sinh và cách tạo ra các ứng dụng hấp dẫn hơn!

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.