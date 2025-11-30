<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T20:34:40+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "vi"
}
-->
# Khám phá và so sánh các mô hình ngôn ngữ lớn (LLMs)

[![Khám phá và so sánh các mô hình ngôn ngữ lớn (LLMs)](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.vi.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Nhấn vào hình ảnh trên để xem video bài học này_

Trong bài học trước, chúng ta đã thấy cách AI tạo sinh đang thay đổi bối cảnh công nghệ, cách các mô hình ngôn ngữ lớn (LLMs) hoạt động và cách một doanh nghiệp - như startup của chúng ta - có thể áp dụng chúng vào các trường hợp sử dụng và phát triển! Trong chương này, chúng ta sẽ so sánh và đối chiếu các loại mô hình ngôn ngữ lớn khác nhau để hiểu rõ ưu và nhược điểm của chúng.

Bước tiếp theo trong hành trình của startup chúng ta là khám phá bối cảnh hiện tại của LLMs và hiểu mô hình nào phù hợp với trường hợp sử dụng của chúng ta.

## Giới thiệu

Bài học này sẽ bao gồm:

- Các loại LLMs khác nhau trong bối cảnh hiện tại.
- Kiểm tra, lặp lại và so sánh các mô hình khác nhau cho trường hợp sử dụng của bạn trên Azure.
- Cách triển khai một LLM.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Chọn mô hình phù hợp cho trường hợp sử dụng của bạn.
- Hiểu cách kiểm tra, lặp lại và cải thiện hiệu suất của mô hình.
- Biết cách các doanh nghiệp triển khai mô hình.

## Hiểu các loại LLMs khác nhau

LLMs có thể được phân loại dựa trên kiến trúc, dữ liệu huấn luyện và trường hợp sử dụng. Hiểu những khác biệt này sẽ giúp startup của chúng ta chọn mô hình phù hợp cho tình huống và hiểu cách kiểm tra, lặp lại và cải thiện hiệu suất.

Có rất nhiều loại mô hình LLM khác nhau, lựa chọn mô hình của bạn phụ thuộc vào mục đích sử dụng, dữ liệu của bạn, ngân sách và nhiều yếu tố khác.

Tùy thuộc vào việc bạn muốn sử dụng các mô hình cho văn bản, âm thanh, video, tạo hình ảnh và các mục đích khác, bạn có thể chọn một loại mô hình khác nhau.

- **Nhận dạng âm thanh và giọng nói**. Đối với mục đích này, các mô hình loại Whisper là một lựa chọn tuyệt vời vì chúng là mô hình đa năng và hướng đến nhận dạng giọng nói. Nó được huấn luyện trên dữ liệu âm thanh đa dạng và có thể thực hiện nhận dạng giọng nói đa ngôn ngữ. Tìm hiểu thêm về [các mô hình loại Whisper tại đây](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Tạo hình ảnh**. Đối với tạo hình ảnh, DALL-E và Midjourney là hai lựa chọn rất nổi tiếng. DALL-E được cung cấp bởi Azure OpenAI. [Đọc thêm về DALL-E tại đây](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) và cũng trong Chương 9 của chương trình học này.

- **Tạo văn bản**. Hầu hết các mô hình đều được huấn luyện để tạo văn bản và bạn có nhiều lựa chọn từ GPT-3.5 đến GPT-4. Chúng có mức giá khác nhau, với GPT-4 là đắt nhất. Đáng để xem xét [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) để đánh giá mô hình nào phù hợp nhất với nhu cầu của bạn về khả năng và chi phí.

- **Đa phương thức**. Nếu bạn muốn xử lý nhiều loại dữ liệu trong đầu vào và đầu ra, bạn có thể muốn tìm hiểu các mô hình như [gpt-4 turbo với vision hoặc gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - các phiên bản mới nhất của mô hình OpenAI - có khả năng kết hợp xử lý ngôn ngữ tự nhiên với hiểu biết hình ảnh, cho phép tương tác thông qua giao diện đa phương thức.

Việc chọn một mô hình có nghĩa là bạn sẽ nhận được một số khả năng cơ bản, tuy nhiên điều đó có thể không đủ. Thường thì bạn có dữ liệu cụ thể của công ty mà bạn cần truyền đạt cho LLM. Có một số cách tiếp cận khác nhau để thực hiện điều đó, sẽ được đề cập trong các phần tiếp theo.

### Mô hình nền tảng so với LLMs

Thuật ngữ Mô hình nền tảng được [đặt ra bởi các nhà nghiên cứu Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) và được định nghĩa là một mô hình AI tuân theo một số tiêu chí, chẳng hạn như:

- **Chúng được huấn luyện bằng học không giám sát hoặc học tự giám sát**, nghĩa là chúng được huấn luyện trên dữ liệu đa phương thức không được gắn nhãn và không yêu cầu chú thích hoặc gắn nhãn dữ liệu của con người trong quá trình huấn luyện.
- **Chúng là các mô hình rất lớn**, dựa trên các mạng nơ-ron rất sâu được huấn luyện trên hàng tỷ tham số.
- **Chúng thường được thiết kế để làm nền tảng cho các mô hình khác**, nghĩa là chúng có thể được sử dụng làm điểm khởi đầu để xây dựng các mô hình khác, điều này có thể được thực hiện bằng cách tinh chỉnh.

![Mô hình nền tảng so với LLMs](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.vi.png)

Nguồn hình ảnh: [Hướng dẫn cơ bản về Mô hình nền tảng và Mô hình ngôn ngữ lớn | bởi Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Để làm rõ hơn sự khác biệt này, hãy lấy ChatGPT làm ví dụ. Để xây dựng phiên bản đầu tiên của ChatGPT, một mô hình gọi là GPT-3.5 đã được sử dụng làm mô hình nền tảng. Điều này có nghĩa là OpenAI đã sử dụng một số dữ liệu cụ thể về trò chuyện để tạo ra một phiên bản tinh chỉnh của GPT-3.5, được chuyên biệt hóa để hoạt động tốt trong các tình huống hội thoại, chẳng hạn như chatbot.

![Mô hình nền tảng](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.vi.png)

Nguồn hình ảnh: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Mô hình mã nguồn mở so với Mô hình độc quyền

Một cách khác để phân loại LLMs là liệu chúng có phải mã nguồn mở hay độc quyền.

Mô hình mã nguồn mở là các mô hình được công khai và có thể được sử dụng bởi bất kỳ ai. Chúng thường được cung cấp bởi công ty tạo ra chúng hoặc cộng đồng nghiên cứu. Các mô hình này cho phép được kiểm tra, sửa đổi và tùy chỉnh cho các trường hợp sử dụng khác nhau trong LLMs. Tuy nhiên, chúng không phải lúc nào cũng được tối ưu hóa cho việc sử dụng trong sản xuất và có thể không hiệu quả như các mô hình độc quyền. Thêm vào đó, nguồn tài trợ cho các mô hình mã nguồn mở có thể bị hạn chế, và chúng có thể không được duy trì lâu dài hoặc không được cập nhật với nghiên cứu mới nhất. Các ví dụ về mô hình mã nguồn mở phổ biến bao gồm [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) và [LLaMA](https://llama.meta.com).

Mô hình độc quyền là các mô hình thuộc sở hữu của một công ty và không được công khai. Các mô hình này thường được tối ưu hóa cho việc sử dụng trong sản xuất. Tuy nhiên, chúng không cho phép được kiểm tra, sửa đổi hoặc tùy chỉnh cho các trường hợp sử dụng khác nhau. Thêm vào đó, chúng không phải lúc nào cũng miễn phí và có thể yêu cầu đăng ký hoặc thanh toán để sử dụng. Ngoài ra, người dùng không có quyền kiểm soát dữ liệu được sử dụng để huấn luyện mô hình, điều này có nghĩa là họ phải tin tưởng vào cam kết của chủ sở hữu mô hình về bảo mật dữ liệu và sử dụng AI một cách có trách nhiệm. Các ví dụ về mô hình độc quyền phổ biến bao gồm [OpenAI models](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) hoặc [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Nhúng so với Tạo hình ảnh so với Tạo văn bản và mã

LLMs cũng có thể được phân loại theo đầu ra mà chúng tạo ra.

Nhúng là một tập hợp các mô hình có thể chuyển đổi văn bản thành dạng số, gọi là nhúng, là một biểu diễn số của văn bản đầu vào. Nhúng giúp máy móc dễ dàng hiểu mối quan hệ giữa các từ hoặc câu và có thể được sử dụng làm đầu vào cho các mô hình khác, chẳng hạn như mô hình phân loại hoặc mô hình phân cụm có hiệu suất tốt hơn trên dữ liệu số. Các mô hình nhúng thường được sử dụng cho học chuyển giao, nơi một mô hình được xây dựng cho một nhiệm vụ thay thế mà có nhiều dữ liệu, sau đó trọng số của mô hình (nhúng) được tái sử dụng cho các nhiệm vụ tiếp theo. Một ví dụ về danh mục này là [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Nhúng](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.vi.png)

Các mô hình tạo hình ảnh là các mô hình tạo ra hình ảnh. Các mô hình này thường được sử dụng cho chỉnh sửa hình ảnh, tổng hợp hình ảnh và dịch hình ảnh. Các mô hình tạo hình ảnh thường được huấn luyện trên các tập dữ liệu lớn về hình ảnh, chẳng hạn như [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), và có thể được sử dụng để tạo hình ảnh mới hoặc chỉnh sửa hình ảnh hiện có với các kỹ thuật như inpainting, siêu phân giải và tô màu. Các ví dụ bao gồm [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) và [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Tạo hình ảnh](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.vi.png)

Các mô hình tạo văn bản và mã là các mô hình tạo ra văn bản hoặc mã. Các mô hình này thường được sử dụng cho tóm tắt văn bản, dịch thuật và trả lời câu hỏi. Các mô hình tạo văn bản thường được huấn luyện trên các tập dữ liệu lớn về văn bản, chẳng hạn như [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), và có thể được sử dụng để tạo văn bản mới hoặc trả lời câu hỏi. Các mô hình tạo mã, như [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), thường được huấn luyện trên các tập dữ liệu lớn về mã, chẳng hạn như GitHub, và có thể được sử dụng để tạo mã mới hoặc sửa lỗi trong mã hiện có.

![Tạo văn bản và mã](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.vi.png)

### Mã hóa-Giải mã so với Chỉ giải mã

Để nói về các loại kiến trúc khác nhau của LLMs, hãy sử dụng một phép so sánh.

Hãy tưởng tượng quản lý của bạn giao cho bạn nhiệm vụ viết một bài kiểm tra cho học sinh. Bạn có hai đồng nghiệp; một người chịu trách nhiệm tạo nội dung và người kia chịu trách nhiệm xem xét chúng.

Người tạo nội dung giống như mô hình Chỉ giải mã, họ có thể nhìn vào chủ đề và những gì bạn đã viết, sau đó viết một khóa học dựa trên đó. Họ rất giỏi trong việc viết nội dung hấp dẫn và thông tin, nhưng họ không giỏi trong việc hiểu chủ đề và mục tiêu học tập. Một số ví dụ về mô hình Chỉ giải mã là các mô hình thuộc họ GPT, chẳng hạn như GPT-3.

Người xem xét giống như mô hình Chỉ mã hóa, họ nhìn vào khóa học đã viết và các câu trả lời, nhận thấy mối quan hệ giữa chúng và hiểu ngữ cảnh, nhưng họ không giỏi trong việc tạo nội dung. Một ví dụ về mô hình Chỉ mã hóa là BERT.

Hãy tưởng tượng rằng chúng ta cũng có thể có một người vừa tạo vừa xem xét bài kiểm tra, đây là mô hình Mã hóa-Giải mã. Một số ví dụ là BART và T5.

### Dịch vụ so với Mô hình

Bây giờ, hãy nói về sự khác biệt giữa một dịch vụ và một mô hình. Một dịch vụ là một sản phẩm được cung cấp bởi Nhà cung cấp Dịch vụ Đám mây, và thường là sự kết hợp của các mô hình, dữ liệu và các thành phần khác. Một mô hình là thành phần cốt lõi của một dịch vụ, và thường là một mô hình nền tảng, chẳng hạn như một LLM.

Các dịch vụ thường được tối ưu hóa cho việc sử dụng trong sản xuất và thường dễ sử dụng hơn các mô hình, thông qua giao diện người dùng đồ họa. Tuy nhiên, các dịch vụ không phải lúc nào cũng miễn phí và có thể yêu cầu đăng ký hoặc thanh toán để sử dụng, đổi lại việc tận dụng thiết bị và tài nguyên của chủ sở hữu dịch vụ, tối ưu hóa chi phí và dễ dàng mở rộng. Một ví dụ về dịch vụ là [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), cung cấp kế hoạch giá theo mức sử dụng, nghĩa là người dùng được tính phí tỷ lệ thuận với mức độ sử dụng dịch vụ. Ngoài ra, Azure OpenAI Service cung cấp bảo mật cấp doanh nghiệp và khung AI có trách nhiệm trên các khả năng của mô hình.

Các mô hình chỉ là Mạng Nơ-ron, với các tham số, trọng số và các yếu tố khác. Cho phép các công ty chạy cục bộ, tuy nhiên, sẽ cần mua thiết bị, xây dựng cấu trúc để mở rộng và mua giấy phép hoặc sử dụng mô hình mã nguồn mở. Một mô hình như LLaMA có sẵn để sử dụng, yêu cầu sức mạnh tính toán để chạy mô hình.

## Cách kiểm tra và lặp lại với các mô hình khác nhau để hiểu hiệu suất trên Azure

Khi nhóm của chúng ta đã khám phá bối cảnh LLMs hiện tại và xác định một số ứng viên tốt cho các tình huống của họ, bước tiếp theo là kiểm tra chúng trên dữ liệu và khối lượng công việc của họ. Đây là một quá trình lặp lại, được thực hiện thông qua các thí nghiệm và đo lường.
Hầu hết các mô hình mà chúng tôi đã đề cập trong các đoạn trước (mô hình OpenAI, mô hình mã nguồn mở như Llama2 và Hugging Face transformers) đều có sẵn trong [Danh mục Mô hình](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) tại [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) là một nền tảng đám mây được thiết kế dành cho các nhà phát triển để xây dựng ứng dụng AI tạo sinh và quản lý toàn bộ vòng đời phát triển - từ thử nghiệm đến đánh giá - bằng cách kết hợp tất cả các dịch vụ AI của Azure vào một trung tâm duy nhất với giao diện người dùng tiện lợi. Danh mục Mô hình trong Azure AI Studio cho phép người dùng:

- Tìm kiếm Mô hình Nền tảng mà bạn quan tâm trong danh mục - có thể là mô hình độc quyền hoặc mã nguồn mở, lọc theo nhiệm vụ, giấy phép hoặc tên. Để cải thiện khả năng tìm kiếm, các mô hình được tổ chức thành các bộ sưu tập, như bộ sưu tập Azure OpenAI, bộ sưu tập Hugging Face, và nhiều hơn nữa.

![Danh mục mô hình](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.vi.png)

- Xem xét thẻ mô hình, bao gồm mô tả chi tiết về mục đích sử dụng và dữ liệu huấn luyện, mẫu mã và kết quả đánh giá trong thư viện đánh giá nội bộ.

![Thẻ mô hình](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.vi.png)

- So sánh các tiêu chuẩn giữa các mô hình và tập dữ liệu có sẵn trong ngành để đánh giá mô hình nào phù hợp với kịch bản kinh doanh, thông qua bảng [Tiêu chuẩn Mô hình](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Tiêu chuẩn mô hình](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.vi.png)

- Tinh chỉnh mô hình trên dữ liệu huấn luyện tùy chỉnh để cải thiện hiệu suất mô hình trong một khối lượng công việc cụ thể, tận dụng khả năng thử nghiệm và theo dõi của Azure AI Studio.

![Tinh chỉnh mô hình](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.vi.png)

- Triển khai mô hình đã được huấn luyện trước hoặc phiên bản đã được tinh chỉnh để suy luận thời gian thực từ xa - tính toán được quản lý - hoặc điểm cuối API không máy chủ - [trả phí theo mức sử dụng](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - để cho phép các ứng dụng sử dụng nó.

![Triển khai mô hình](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.vi.png)

> [!NOTE]
> Không phải tất cả các mô hình trong danh mục hiện đều có sẵn để tinh chỉnh và/hoặc triển khai trả phí theo mức sử dụng. Kiểm tra thẻ mô hình để biết chi tiết về khả năng và hạn chế của mô hình.

## Cải thiện kết quả LLM

Chúng tôi đã cùng đội ngũ startup của mình khám phá các loại LLM khác nhau và một nền tảng đám mây (Azure Machine Learning) cho phép chúng tôi so sánh các mô hình khác nhau, đánh giá chúng trên dữ liệu kiểm tra, cải thiện hiệu suất và triển khai chúng trên các điểm cuối suy luận.

Nhưng khi nào họ nên cân nhắc việc tinh chỉnh một mô hình thay vì sử dụng mô hình đã được huấn luyện trước? Có những cách tiếp cận nào khác để cải thiện hiệu suất mô hình trên các khối lượng công việc cụ thể?

Có một số cách tiếp cận mà doanh nghiệp có thể sử dụng để đạt được kết quả mong muốn từ LLM. Bạn có thể chọn các loại mô hình khác nhau với các mức độ huấn luyện khác nhau khi triển khai LLM trong sản xuất, với các mức độ phức tạp, chi phí và chất lượng khác nhau. Dưới đây là một số cách tiếp cận khác nhau:

- **Kỹ thuật gợi ý với ngữ cảnh**. Ý tưởng là cung cấp đủ ngữ cảnh khi bạn đưa ra gợi ý để đảm bảo bạn nhận được câu trả lời như mong muốn.

- **Tạo nội dung tăng cường truy xuất, RAG**. Dữ liệu của bạn có thể tồn tại trong cơ sở dữ liệu hoặc điểm cuối web chẳng hạn, để đảm bảo dữ liệu này, hoặc một phần của nó, được bao gồm khi đưa ra gợi ý, bạn có thể truy xuất dữ liệu liên quan và thêm nó vào gợi ý của người dùng.

- **Mô hình đã được tinh chỉnh**. Ở đây, bạn huấn luyện mô hình thêm trên dữ liệu của riêng mình, điều này dẫn đến mô hình trở nên chính xác hơn và đáp ứng nhu cầu của bạn nhưng có thể tốn kém.

![Triển khai LLMs](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.vi.png)

Nguồn hình ảnh: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Kỹ thuật gợi ý với ngữ cảnh

Các LLM đã được huấn luyện trước hoạt động rất tốt trên các nhiệm vụ ngôn ngữ tự nhiên tổng quát, ngay cả khi chỉ gọi chúng với một gợi ý ngắn, như một câu cần hoàn thành hoặc một câu hỏi – cái gọi là học "zero-shot".

Tuy nhiên, càng nhiều thông tin chi tiết mà người dùng có thể cung cấp trong yêu cầu của họ, với một yêu cầu chi tiết và các ví dụ – Ngữ cảnh – thì câu trả lời càng chính xác và gần với mong đợi của người dùng. Trong trường hợp này, chúng ta nói về học "one-shot" nếu gợi ý chỉ bao gồm một ví dụ và "few-shot learning" nếu nó bao gồm nhiều ví dụ. Kỹ thuật gợi ý với ngữ cảnh là cách tiếp cận tiết kiệm chi phí nhất để bắt đầu.

### Tạo nội dung tăng cường truy xuất (RAG)

Các LLM có hạn chế là chúng chỉ có thể sử dụng dữ liệu đã được sử dụng trong quá trình huấn luyện để tạo ra câu trả lời. Điều này có nghĩa là chúng không biết gì về các sự kiện xảy ra sau quá trình huấn luyện của chúng, và chúng không thể truy cập thông tin không công khai (như dữ liệu công ty). 

Điều này có thể được khắc phục thông qua RAG, một kỹ thuật tăng cường gợi ý với dữ liệu bên ngoài dưới dạng các đoạn tài liệu, xem xét giới hạn độ dài gợi ý. Điều này được hỗ trợ bởi các công cụ cơ sở dữ liệu Vector (như [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) truy xuất các đoạn hữu ích từ các nguồn dữ liệu được xác định trước và thêm chúng vào Ngữ cảnh gợi ý.

Kỹ thuật này rất hữu ích khi một doanh nghiệp không có đủ dữ liệu, đủ thời gian hoặc nguồn lực để tinh chỉnh một LLM, nhưng vẫn muốn cải thiện hiệu suất trên một khối lượng công việc cụ thể và giảm rủi ro sai lệch, tức là sự bóp méo thực tế hoặc nội dung có hại.

### Mô hình đã được tinh chỉnh

Tinh chỉnh là một quá trình tận dụng học chuyển giao để 'tùy chỉnh' mô hình cho một nhiệm vụ cụ thể hoặc để giải quyết một vấn đề cụ thể. Khác với học few-shot và RAG, nó tạo ra một mô hình mới, với các trọng số và độ lệch được cập nhật. Nó yêu cầu một tập hợp các ví dụ huấn luyện bao gồm một đầu vào duy nhất (gợi ý) và đầu ra liên quan của nó (hoàn thành). 

Đây sẽ là cách tiếp cận ưu tiên nếu:

- **Sử dụng mô hình đã được tinh chỉnh**. Một doanh nghiệp muốn sử dụng các mô hình đã được tinh chỉnh nhưng ít khả năng hơn (như các mô hình nhúng) thay vì các mô hình hiệu suất cao, dẫn đến giải pháp tiết kiệm chi phí và nhanh chóng hơn.

- **Xem xét độ trễ**. Độ trễ là yếu tố quan trọng đối với một trường hợp sử dụng cụ thể, vì vậy không thể sử dụng các gợi ý quá dài hoặc số lượng ví dụ cần học từ mô hình không phù hợp với giới hạn độ dài gợi ý.

- **Luôn cập nhật**. Một doanh nghiệp có rất nhiều dữ liệu chất lượng cao và nhãn sự thật cơ bản cùng với các nguồn lực cần thiết để duy trì dữ liệu này luôn cập nhật theo thời gian.

### Mô hình được huấn luyện

Huấn luyện một LLM từ đầu chắc chắn là cách tiếp cận khó khăn và phức tạp nhất, yêu cầu lượng dữ liệu khổng lồ, nguồn lực có kỹ năng và sức mạnh tính toán phù hợp. Tùy chọn này chỉ nên được xem xét trong trường hợp một doanh nghiệp có một trường hợp sử dụng cụ thể theo lĩnh vực và một lượng lớn dữ liệu tập trung vào lĩnh vực đó.

## Kiểm tra kiến thức

Cách tiếp cận nào có thể là tốt để cải thiện kết quả hoàn thành của LLM?

1. Kỹ thuật gợi ý với ngữ cảnh
1. RAG
1. Mô hình đã được tinh chỉnh

A:3, nếu bạn có thời gian và nguồn lực cùng dữ liệu chất lượng cao, tinh chỉnh là lựa chọn tốt hơn để luôn cập nhật. Tuy nhiên, nếu bạn muốn cải thiện và thiếu thời gian, đáng cân nhắc RAG trước.

## 🚀 Thử thách

Tìm hiểu thêm về cách bạn có thể [sử dụng RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) cho doanh nghiệp của mình.

## Làm tốt lắm, tiếp tục học tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học về AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh!

Hãy chuyển sang Bài học 3, nơi chúng ta sẽ tìm hiểu cách [xây dựng với AI Tạo sinh một cách có trách nhiệm](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.