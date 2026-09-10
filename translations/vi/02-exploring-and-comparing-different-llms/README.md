# Khám phá và so sánh các LLM khác nhau

[![Khám phá và so sánh các LLM khác nhau](../../../translated_images/vi/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Nhấp vào hình ảnh trên để xem video của bài học này_

Với bài học trước, chúng ta đã thấy AI Tạo sinh đang thay đổi cảnh quan công nghệ như thế nào, các Mô hình Ngôn ngữ Lớn (LLMs) hoạt động ra sao và một doanh nghiệp - như startup của chúng ta - có thể áp dụng chúng vào các trường hợp sử dụng của họ và phát triển! Trong chương này, chúng ta sẽ so sánh và đối chiếu các loại mô hình ngôn ngữ lớn khác nhau để hiểu ưu nhược điểm của chúng.

Bước tiếp theo trong hành trình của startup chúng ta là khám phá cảnh quan hiện tại của các LLM và hiểu rõ loại nào phù hợp với trường hợp sử dụng của chúng ta.

## Giới thiệu

Bài học này sẽ đề cập đến:

- Các loại LLM khác nhau trong cảnh quan hiện tại.
- Thử nghiệm, lặp lại và so sánh các mô hình khác nhau cho trường hợp sử dụng của bạn trên Azure.
- Cách triển khai một LLM.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Chọn mô hình phù hợp cho trường hợp sử dụng của bạn.
- Hiểu cách thử nghiệm, lặp lại và cải thiện hiệu năng của mô hình.
- Biết cách các doanh nghiệp triển khai mô hình.

## Hiểu các loại LLM khác nhau

LLM có thể được phân loại theo kiến trúc, dữ liệu huấn luyện và trường hợp sử dụng. Hiểu những khác biệt này sẽ giúp startup của chúng ta chọn mô hình phù hợp cho từng kịch bản, cũng như biết cách thử nghiệm, lặp lại và cải thiện hiệu suất.

Có nhiều loại mô hình LLM khác nhau, lựa chọn mô hình của bạn phụ thuộc vào mục đích sử dụng, dữ liệu, khả năng chi trả và nhiều yếu tố khác.

Tùy thuộc bạn muốn sử dụng mô hình cho văn bản, âm thanh, video, tạo hình ảnh hay những loại khác, bạn sẽ chọn loại mô hình phù hợp.

- **Nhận dạng âm thanh và giọng nói**. Các mô hình kiểu Whisper vẫn hữu dụng như các mô hình nhận dạng giọng nói đa năng, nhưng các lựa chọn trong sản xuất bây giờ còn bao gồm các mô hình chuyển giọng nói thành văn bản mới như `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` và các biến thể phân tách người nói. Hãy đánh giá phạm vi ngôn ngữ, phân tách người nói, hỗ trợ thời gian thực, độ trễ và chi phí cho trường hợp của bạn. Tìm hiểu thêm tại tài liệu [OpenAI chuyển giọng nói thành văn bản](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Tạo hình ảnh**. DALL-E và Midjourney là các lựa chọn tạo hình ảnh nổi tiếng, nhưng các API hình ảnh hiện tại của OpenAI tập trung vào các mô hình GPT Image như `gpt-image-2`, trong khi các gia đình mô hình khác như Stable Diffusion, Imagen, Flux cũng phổ biến. So sánh độ chính xác đáp ứng câu lệnh, hỗ trợ chỉnh sửa, kiểm soát phong cách, yêu cầu an toàn và cấp phép. Tìm hiểu thêm trong [hướng dẫn tạo hình ảnh của OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) và Chương 9 của giáo trình này.

- **Tạo văn bản**. Mô hình văn bản hiện nay bao gồm các mô hình tiên tiến, mô hình suy luận, các mô hình nhỏ có độ trễ thấp và các mô hình mã nguồn mở. Ví dụ hiện tại gồm các mô hình OpenAI GPT-5.x, Anthropic Claude 4.x, Google Gemini 3.x, Meta Llama 4 và Mistral. Không chọn chỉ dựa trên ngày phát hành hay giá cả; hãy so sánh chất lượng nhiệm vụ, độ trễ, cửa sổ ngữ cảnh, sử dụng công cụ, hành vi an toàn, khả năng sẵn có theo vùng và tổng chi phí. Danh mục mô hình [Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) là nơi tốt để so sánh các mô hình trên Azure.

- **Đa phương thức**. Nhiều mô hình hiện nay xử lý được hơn chỉ văn bản. Một số nhận đầu vào hình ảnh, âm thanh hoặc video; số khác có thể gọi công cụ; và các mô hình chuyên biệt có thể tạo hình ảnh, âm thanh hoặc video. Ví dụ, các mô hình OpenAI hiện tại hỗ trợ đầu vào văn bản và hình ảnh, các mô hình Gemini hỗ trợ văn bản, mã nguồn, hình ảnh, âm thanh và video tùy biến thể, còn Llama 4 Scout và Maverick là các mô hình đa phương thức mã nguồn mở. Luôn kiểm tra thẻ mô hình để biết các kiểu đầu vào và đầu ra được hỗ trợ trước khi xây dựng quy trình.

Việc chọn một mô hình nghĩa là bạn sẽ có các khả năng cơ bản, tuy nhiên điều đó có thể chưa đủ. Thường khi bạn có dữ liệu theo đặc thù doanh nghiệp mà cần phải báo cho LLM biết. Có một vài cách tiếp cận khác nhau cho việc này, sẽ được trình bày ở các phần tiếp theo.

### Mô hình cơ sở (Foundation models) và LLM

Thuật ngữ Mô hình Cơ sở được [các nhà nghiên cứu Stanford đặt ra](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) và định nghĩa như một mô hình AI đáp ứng các tiêu chí như sau:

- **Chúng được huấn luyện bằng học không giám sát hoặc học tự giám sát**, nghĩa là được đào tạo trên dữ liệu đa phương thức chưa có nhãn, và không cần con người đánh dấu hay chú thích dữ liệu trong quá trình huấn luyện.
- **Chúng là các mô hình rất lớn**, dựa trên các mạng nơ-ron sâu, được huấn luyện trên hàng tỷ tham số.
- **Chúng thường nhằm phục vụ như một ‘nền tảng’ để xây dựng các mô hình khác**, tức là có thể được dùng làm điểm khởi đầu để phát triển các mô hình khác, thông qua tinh chỉnh (fine-tuning).

![Mô hình cơ sở so với LLM](../../../translated_images/vi/FoundationModel.e4859dbb7a825c94.webp)

Nguồn ảnh: [Essential Guide to Foundation Models and Large Language Models | bởi Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Để làm rõ hơn sự khác biệt này, hãy lấy ChatGPT làm ví dụ lịch sử. Các phiên bản đầu của ChatGPT dùng GPT-3.5 như một mô hình cơ sở. OpenAI sau đó dùng dữ liệu và kỹ thuật điều chỉnh hội thoại đặc thù để tạo ra một phiên bản tinh chỉnh hoạt động tốt hơn trong các kịch bản trò chuyện, như chatbot. Các dịch vụ AI hiện đại thường sử dụng nhiều biến thể mô hình, vì vậy tên dịch vụ và tên mô hình bên trong không phải lúc nào cũng giống nhau.

![Mô hình cơ sở](../../../translated_images/vi/Multimodal.2c389c6439e0fc51.webp)

Nguồn ảnh: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Mô hình mã nguồn mở/mở trọng số so với mô hình độc quyền

Một cách khác để phân loại LLM là dựa vào việc mô hình có mở trọng số, mã nguồn mở hay độc quyền.

Mô hình mã nguồn mở và mở trọng số cho phép bạn xem xét, tải xuống hoặc tùy chỉnh mô hình, tuy nhiên giấy phép có thể khác nhau. Một số hoàn toàn mã nguồn mở, trong khi số khác là mô hình mở trọng số với các hạn chế sử dụng. Chúng hữu ích khi doanh nghiệp cần kiểm soát hơn về triển khai, dữ liệu tại chỗ, chi phí hoặc tùy chỉnh. Tuy nhiên, nhóm cần xem xét kỹ các điều khoản cấp phép, chi phí phục vụ, bảo trì, cập nhật bảo mật và chất lượng đánh giá trước khi dùng trong sản xuất. Ví dụ có thể kể đến là [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), một số [mô hình Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) và nhiều mô hình trên [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Mô hình độc quyền thuộc sở hữu và được lưu trữ bởi nhà cung cấp. Các mô hình này thường được tối ưu cho sản xuất quản lý và có thể cung cấp hỗ trợ mạnh, hệ thống an toàn, tích hợp công cụ và khả năng mở rộng. Tuy nhiên, khách hàng thường không thể xem hay chỉnh sửa trọng số mô hình, và phải xem xét các điều khoản của nhà cung cấp về quyền riêng tư, lưu trữ, tuân thủ và sử dụng hợp lệ. Ví dụ gồm có [mô hình OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) và [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Mô hình Nhúng (Embedding) so với Tạo hình ảnh so với Tạo văn bản và mã nguồn

LLM cũng có thể được phân loại theo kết quả đầu ra mà chúng tạo ra.

Embedding là tập hợp các mô hình có thể chuyển đổi văn bản thành dạng số, gọi là embedding, là biểu diễn số của văn bản đầu vào. Embedding giúp máy tính dễ hiểu mối quan hệ giữa các từ hoặc câu và có thể được dùng làm đầu vào cho các mô hình khác như mô hình phân loại hoặc mô hình phân cụm, những mô hình này hoạt động tốt hơn với dữ liệu số. Mô hình embedding thường được dùng để học chuyển giao (transfer learning), tức xây dựng mô hình cho một nhiệm vụ thay thế có nhiều dữ liệu, rồi dùng lại trọng số (embedding) cho các nhiệm vụ khác. Ví dụ trong nhóm này là [embedding OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/vi/Embedding.c3708fe988ccf760.webp)

Mô hình tạo hình ảnh là các mô hình tạo ra hình ảnh. Các mô hình này thường được dùng cho chỉnh sửa hình ảnh, tổng hợp hình ảnh và chuyển đổi hình ảnh. Mô hình tạo hình ảnh thường được huấn luyện trên các bộ dữ liệu lớn về hình ảnh, như [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), và có thể dùng để tạo hình ảnh mới hoặc chỉnh sửa hình ảnh hiện có bằng kỹ thuật inpainting, siêu phân giải và tô màu. Ví dụ gồm có các [mô hình GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [mô hình Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) và mô hình Imagen.

![Tạo hình ảnh](../../../translated_images/vi/Image.349c080266a763fd.webp)

Mô hình tạo văn bản và mã nguồn là các mô hình tạo ra văn bản hoặc mã. Các mô hình này thường dùng để tóm tắt văn bản, dịch thuật và trả lời câu hỏi. Mô hình tạo văn bản thường được huấn luyện trên các bộ dữ liệu lớn về văn bản, như [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), và có thể dùng để tạo ra văn bản mới, hoặc trả lời câu hỏi. Mô hình tạo mã như [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst) được huấn luyện trên bộ dữ liệu lớn mã nguồn, như GitHub, và có thể tạo mã mới hoặc sửa lỗi trong mã hiện có.

![Tạo văn bản và mã nguồn](../../../translated_images/vi/Text.a8c0cf139e5cc2a0.webp)

### Kiến trúc Mã hóa - Giải mã so với Chỉ giải mã

Để nói về các loại kiến trúc LLM khác nhau, hãy dùng một phép tương tự.

Hãy tưởng tượng người quản lý của bạn giao nhiệm vụ viết một bài quiz cho học sinh. Bạn có hai đồng nghiệp; người này chịu trách nhiệm tạo nội dung và người kia chịu trách nhiệm xem lại.

Người tạo nội dung giống như mô hình chỉ giải mã: họ có thể nhìn vào chủ đề, xem những gì bạn đã viết, và tiếp tục tạo nội dung dựa trên ngữ cảnh đó. Họ rất giỏi viết nội dung hấp dẫn và thông tin, nhưng không phải lúc nào cũng là lựa chọn tốt nhất khi nhiệm vụ chỉ là phân loại, truy xuất hoặc mã hóa thông tin. Các ví dụ về mô hình chỉ giải mã là các mô hình GPT và Llama.

Người xem lại giống như mô hình chỉ mã hóa; họ xem bài học đã viết và câu trả lời, nhận thấy mối quan hệ giữa chúng và hiểu ngữ cảnh, nhưng họ không giỏi tạo nội dung. Ví dụ mô hình chỉ mã hóa là BERT.

Hãy tưởng tượng rằng chúng ta có người có thể tạo và xem lại bài quiz, đây chính là mô hình Mã hóa - Giải mã. Một số ví dụ là BART và T5.

### Dịch vụ so với Mô hình

Bây giờ, hãy nói về sự khác biệt giữa dịch vụ và mô hình. Dịch vụ là sản phẩm do Nhà cung cấp Dịch vụ Đám mây cung cấp, thường là sự kết hợp của mô hình, dữ liệu và các thành phần khác. Mô hình là thành phần cốt lõi của dịch vụ, thường là mô hình cơ sở như LLM.

Các dịch vụ thường được tối ưu cho sử dụng trong sản xuất và dễ dùng hơn mô hình qua giao diện đồ họa. Nhưng dịch vụ không luôn miễn phí, và có thể yêu cầu đăng ký hoặc trả phí để sử dụng, đổi lại việc tận dụng thiết bị và tài nguyên của chủ dịch vụ, tối ưu chi phí và mở rộng dễ dàng. Ví dụ về dịch vụ là [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), cung cấp gói trả tiền theo mức sử dụng, nghĩa là người dùng bị tính phí tỉ lệ thuận với mức độ sử dụng dịch vụ. Azure OpenAI Service cũng mang đến an ninh cấp doanh nghiệp và khung AI có trách nhiệm trên nền tảng khả năng của mô hình.

Mô hình là các tác phẩm mạng nơ-ron nhân tạo: tham số, trọng số, kiến trúc, bộ mã hóa token và cấu hình hỗ trợ. Chạy một mô hình cục bộ hoặc trong môi trường riêng yêu cầu phần cứng thích hợp, hạ tầng phục vụ, giám sát, và giấy phép tương thích (mở trọng số/mã nguồn mở hoặc thương mại). Các mô hình mở trọng số như Llama 4 hoặc Mistral có thể được tự lưu trữ, nhưng vẫn cần sức mạnh tính toán và chuyên môn vận hành.

## Cách thử nghiệm và lặp lại với các mô hình khác nhau để hiểu hiệu năng trên Azure


Khi nhóm của chúng tôi đã khám phá bối cảnh các LLM hiện tại và xác định được một số ứng viên tốt cho các tình huống của họ, bước tiếp theo là thử nghiệm chúng trên dữ liệu và khối lượng công việc của họ. Đây là một quá trình lặp đi lặp lại, được thực hiện bằng các thí nghiệm và đo lường.
Hầu hết các mô hình chúng tôi đã đề cập trong các đoạn trước (mô hình OpenAI, mô hình có trọng số mở như Llama 4 và Mistral, và mô hình Hugging Face) có sẵn trong [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), trước đây là Azure AI Studio/Azure AI Foundry, là nền tảng Azure thống nhất để xây dựng các ứng dụng và tác nhân AI. Nó giúp các nhà phát triển quản lý vòng đời từ thí nghiệm và đánh giá đến triển khai, giám sát và quản trị. Danh mục mô hình trong Microsoft Foundry cho phép người dùng:

- Tìm mô hình nền tảng quan tâm trong danh mục, bao gồm các mô hình được Azure bán và các mô hình từ các đối tác và nhà cung cấp cộng đồng. Người dùng có thể lọc theo nhiệm vụ, nhà cung cấp, giấy phép, tùy chọn triển khai hoặc tên.

![Model catalog](../../../translated_images/vi/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Xem xét thẻ mô hình, bao gồm mô tả chi tiết về mục đích sử dụng và dữ liệu đào tạo, ví dụ mã và kết quả đánh giá trên thư viện đánh giá nội bộ.

![Model card](../../../translated_images/vi/ModelCard.598051692c6e400d.webp)

- So sánh các điểm chuẩn giữa các mô hình và tập dữ liệu có sẵn trong ngành để đánh giá mô hình nào phù hợp với kịch bản kinh doanh, thông qua bảng [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/vi/ModelBenchmarks.254cb20fbd06c03a.webp)

- Tinh chỉnh mô hình được hỗ trợ trên dữ liệu đào tạo tùy chỉnh để cải thiện hiệu suất mô hình trong một khối lượng công việc cụ thể, tận dụng khả năng thực nghiệm và theo dõi của Microsoft Foundry.

![Model fine-tuning](../../../translated_images/vi/FineTuning.aac48f07142e36fd.webp)

- Triển khai mô hình gốc đã được đào tạo trước hoặc phiên bản đã được tinh chỉnh tới điểm cuối suy luận thời gian thực từ xa, sử dụng các tùy chọn tính toán được quản lý hoặc triển khai không máy chủ, để các ứng dụng có thể sử dụng nó.

![Model deployment](../../../translated_images/vi/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Không phải tất cả các mô hình trong danh mục hiện đều có sẵn để tinh chỉnh và/hoặc triển khai theo mô hình trả theo mức sử dụng. Kiểm tra thẻ mô hình để biết chi tiết về khả năng và giới hạn của mô hình.

## Cải thiện kết quả LLM

Chúng tôi đã khám phá cùng nhóm khởi nghiệp các loại LLM khác nhau và một nền tảng đám mây (Microsoft Foundry) cho phép chúng tôi so sánh các mô hình, đánh giá chúng trên dữ liệu thử nghiệm, cải thiện hiệu suất và triển khai chúng trên các điểm cuối suy luận.

Nhưng khi nào họ nên cân nhắc tinh chỉnh một mô hình thay vì sử dụng một mô hình đã được đào tạo trước? Có những phương pháp khác để cải thiện hiệu suất mô hình trên các khối lượng công việc cụ thể không?

Có nhiều phương pháp mà doanh nghiệp có thể sử dụng để đạt được kết quả cần thiết từ LLM. Bạn có thể chọn các loại mô hình khác nhau với mức độ đào tạo khác nhau khi triển khai một LLM vào sản xuất, với các mức độ phức tạp, chi phí, và chất lượng khác nhau. Dưới đây là một số phương pháp khác nhau:

- **Kỹ thuật gợi ý với bối cảnh**. Ý tưởng là cung cấp đủ bối cảnh khi bạn gợi ý để đảm bảo nhận được phản hồi bạn cần.

- **Tạo sinh tăng cường truy xuất, RAG**. Dữ liệu của bạn có thể tồn tại trong cơ sở dữ liệu hoặc điểm cuối web ví dụ, để đảm bảo dữ liệu này, hoặc một phần của nó, được bao gồm tại thời điểm gợi ý, bạn có thể truy xuất dữ liệu liên quan và đưa phần đó vào gợi ý của người dùng.

- **Mô hình được tinh chỉnh**. Ở đây, bạn đào tạo thêm mô hình trên dữ liệu của riêng bạn, khiến mô hình chính xác hơn và đáp ứng tốt hơn nhu cầu của bạn nhưng có thể tốn kém.

![LLMs deployment](../../../translated_images/vi/Deploy.18b2d27412ec8c02.webp)

Nguồn ảnh: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Kỹ thuật gợi ý với bối cảnh

Các LLM đã được đào tạo trước hoạt động rất tốt trên các nhiệm vụ ngôn ngữ tự nhiên tổng quát, ngay cả khi gọi chúng với một gợi ý ngắn, như một câu để hoàn thiện hoặc một câu hỏi – còn gọi là học “zero-shot”.

Tuy nhiên, người dùng càng có thể định dạng câu hỏi của họ, với một yêu cầu chi tiết và các ví dụ – tức Bối cảnh – thì câu trả lời càng chính xác và gần với kỳ vọng của người dùng hơn. Trong trường hợp này, chúng ta gọi là học “one-shot” nếu gợi ý chỉ bao gồm một ví dụ và học “few-shot” nếu bao gồm nhiều ví dụ.
Kỹ thuật gợi ý với bối cảnh là phương pháp tiết kiệm chi phí nhất để bắt đầu.

### Tạo sinh tăng cường truy xuất (RAG)

LLM có hạn chế là chỉ có thể sử dụng dữ liệu đã được dùng trong quá trình đào tạo để tạo câu trả lời. Điều này có nghĩa là chúng không biết gì về các sự kiện xảy ra sau quá trình đào tạo, và không thể truy cập thông tin không công khai (như dữ liệu công ty).
Điều này có thể được khắc phục bằng RAG, kỹ thuật tăng cường gợi ý với dữ liệu bên ngoài dưới dạng các đoạn tài liệu, cân nhắc giới hạn độ dài gợi ý. Điều này được hỗ trợ bởi các công cụ cơ sở dữ liệu vector (như [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) để truy xuất các đoạn hữu ích từ các nguồn dữ liệu đa dạng đã được định nghĩa trước và thêm chúng vào Bối cảnh gợi ý.

Kỹ thuật này rất hữu ích khi doanh nghiệp không có đủ dữ liệu, đủ thời gian hoặc nguồn lực để tinh chỉnh LLM, nhưng vẫn muốn cải thiện hiệu suất trên khối lượng công việc cụ thể và giảm rủi ro câu trả lời ảo tưởng, lỗi thời hoặc không được hỗ trợ.

### Mô hình được tinh chỉnh

Tinh chỉnh là quá trình tận dụng học chuyển giao để ‘thích ứng’ mô hình với một nhiệm vụ cụ thể hoặc để giải quyết một vấn đề cụ thể. Khác với học few-shot và RAG, nó tạo ra một mô hình mới với các trọng số và độ lệch cập nhật. Nó yêu cầu một tập các ví dụ đào tạo bao gồm một đầu vào (gợi ý) và đầu ra liên quan (hoàn thiện).
Đây sẽ là phương pháp ưu tiên nếu:

- **Sử dụng các mô hình nhỏ hơn chuyên biệt cho nhiệm vụ**. Doanh nghiệp muốn tinh chỉnh một mô hình nhỏ hơn cho một nhiệm vụ hẹp thay vì liên tục gợi ý một mô hình biên lớn hơn, dẫn đến giải pháp tiết kiệm chi phí và nhanh hơn.

- **Xem xét độ trễ**. Độ trễ quan trọng cho một trường hợp sử dụng cụ thể, nên không thể dùng các gợi ý quá dài hoặc số lượng các ví dụ mà mô hình cần học không phù hợp với giới hạn độ dài gợi ý.

- **Thích ứng hành vi ổn định**. Doanh nghiệp có nhiều ví dụ chất lượng cao và muốn mô hình nhất quán tuân theo mẫu nhiệm vụ, định dạng đầu ra, giọng điệu hoặc phong cách theo miền. Nếu vấn đề chính là thông tin mới hoặc tri thức riêng tư thay đổi thường xuyên, hãy sử dụng RAG thay vì chỉ dựa vào tinh chỉnh.

### Mô hình được đào tạo

Đào tạo một LLM từ đầu không nghi ngờ gì là phương pháp khó khăn và phức tạp nhất để áp dụng, đòi hỏi lượng dữ liệu khổng lồ, nguồn lực có kỹ năng và công suất tính toán phù hợp. Tùy chọn này chỉ nên xem xét trong trường hợp doanh nghiệp có trường hợp sử dụng chuyên ngành và lượng lớn dữ liệu tập trung theo ngành.

## Kiểm tra kiến thức

Phương pháp nào có thể là cách tốt để cải thiện kết quả hoàn thiện LLM?

1. Kỹ thuật gợi ý với bối cảnh
1. RAG
1. Mô hình được tinh chỉnh

A: Cả ba đều có thể giúp. Bắt đầu với kỹ thuật gợi ý và bối cảnh để cải thiện nhanh, và dùng RAG khi mô hình cần thông tin hiện tại hoặc dữ liệu doanh nghiệp riêng. Chọn tinh chỉnh khi bạn có đủ ví dụ chất lượng cao và cần mô hình nhất quán theo nhiệm vụ, định dạng, giọng điệu hoặc mẫu miền.

## 🚀 Thử thách

Đọc thêm về cách bạn có thể [sử dụng RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) cho doanh nghiệp của mình.

## Làm tốt lắm, Tiếp tục Học hỏi

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

Hãy đến bài học 3, nơi chúng ta sẽ xem cách [xây dựng với Generative AI một cách có trách nhiệm](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->