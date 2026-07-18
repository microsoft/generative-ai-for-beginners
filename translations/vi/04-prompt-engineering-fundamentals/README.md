# Những Nguyên Lý Cơ Bản về Kỹ Thuật Viết Prompt

[![Những Nguyên Lý Cơ Bản về Kỹ Thuật Viết Prompt](../../../translated_images/vi/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Giới Thiệu
Mô-đun này trình bày các khái niệm và kỹ thuật thiết yếu để tạo ra các prompt hiệu quả trong các mô hình AI tạo sinh. Cách bạn viết prompt cho một LLM cũng rất quan trọng. Một prompt được soạn thảo cẩn thận có thể đạt được chất lượng phản hồi tốt hơn. Nhưng chính xác thì các thuật ngữ như _prompt_ và _kỹ thuật viết prompt_ có ý nghĩa gì? Và làm sao để tôi cải thiện đầu vào prompt mà tôi gửi đến LLM? Đây là những câu hỏi chúng ta sẽ cố gắng trả lời trong chương này và chương tiếp theo.

_AI tạo sinh_ có khả năng tạo ra nội dung mới (ví dụ: văn bản, hình ảnh, âm thanh, mã code, v.v.) đáp ứng các yêu cầu của người dùng. Nó đạt được điều này bằng cách sử dụng _Mô Hình Ngôn Ngữ Lớn_ như loạt GPT của OpenAI ("Generative Pre-trained Transformer") được huấn luyện để sử dụng ngôn ngữ tự nhiên và mã code.

Người dùng hiện có thể tương tác với những mô hình này bằng các phương pháp quen thuộc như chat, mà không cần vốn hiểu biết kỹ thuật hay đào tạo chuyên sâu. Các mô hình dựa trên _prompt_ - người dùng gửi đầu vào dạng văn bản (prompt) và nhận lại phản hồi từ AI (completion). Họ có thể "trò chuyện với AI" theo kiểu tuần tự nhiều lượt, tinh chỉnh prompt cho đến khi phản hồi phù hợp với kỳ vọng.

"Prompt" giờ đây trở thành _giao diện lập trình_ chính cho các ứng dụng AI tạo sinh, chỉ dẫn cho mô hình phải làm gì và ảnh hưởng đến chất lượng phản hồi trả về. "Kỹ thuật viết prompt" là một lĩnh vực nghiên cứu phát triển nhanh, tập trung vào _thiết kế và tối ưu_ các prompt để cung cấp phản hồi nhất quán và chất lượng ở quy mô lớn.

## Mục Tiêu Học Tập

Trong bài học này, chúng ta sẽ hiểu thế nào là Kỹ Thuật Viết Prompt, tại sao nó quan trọng, và cách tạo ra các prompt hiệu quả hơn cho một mô hình và mục tiêu ứng dụng cụ thể. Chúng ta sẽ hiểu các khái niệm cốt lõi và thực hành tốt nhất về kỹ thuật viết prompt - và làm quen với môi trường "sandbox" tương tác trong Jupyter Notebooks để thấy các khái niệm được áp dụng trên các ví dụ thực tế.

Cuối bài học, bạn sẽ có khả năng:

1. Giải thích thế nào là kỹ thuật viết prompt và tại sao nó quan trọng.
2. Mô tả các thành phần của một prompt và cách sử dụng chúng.
3. Học các thực hành tốt nhất và kỹ thuật cho việc viết prompt.
4. Áp dụng các kỹ thuật học được vào các ví dụ thực tế, sử dụng điểm cuối OpenAI.

## Thuật Ngữ Chính

Kỹ thuật viết Prompt: Thực hành thiết kế và tinh chỉnh đầu vào để hướng các mô hình AI tạo ra kết quả mong muốn.
Quá trình phân tách từ (Tokenization): Quá trình chuyển đổi văn bản thành các đơn vị nhỏ hơn, gọi là token, mà mô hình có thể hiểu và xử lý.
LLMs được tinh chỉnh theo hướng chỉ dẫn: Các Mô Hình Ngôn Ngữ Lớn đã được tinh chỉnh thêm với các chỉ dẫn cụ thể nhằm cải thiện độ chính xác và sự liên quan của phản hồi.

## Môi Trường Học Tập Sandbox

Kỹ thuật viết prompt hiện đang mang tính nghệ thuật nhiều hơn khoa học. Cách tốt nhất để cải thiện trực giác là _thực hành nhiều_ và áp dụng phương pháp thử và sai kết hợp chuyên môn lĩnh vực với các kỹ thuật đề xuất và tối ưu theo đặc thù mô hình.

Jupyter Notebook kèm theo bài học này cung cấp môi trường _sandbox_ nơi bạn có thể thử nghiệm những gì học được - trong quá trình hoặc như phần thử thách mã cuối bài. Để thực thi các bài tập, bạn cần:

1. **Khóa API Azure OpenAI** - điểm cuối dịch vụ cho một LLM đã triển khai.
2. **Môi trường thực thi Python** - nơi có thể chạy Notebook.
3. **Biến môi trường cục bộ** - _hoàn thành các bước [CÀI ĐẶT](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ngay bây giờ để sẵn sàng_.

Notebook cung cấp các bài tập _khởi đầu_ - nhưng bạn được khuyến khích thêm các phần _Markdown_ (mô tả) và _Code_ (yêu cầu prompt) riêng để thử thêm ví dụ hay ý tưởng - và phát triển trực giác thiết kế prompt.

## Hướng Dẫn Minh Họa

Muốn nắm tổng quan những gì bài học này đề cập trước khi bắt đầu? Hãy xem hướng dẫn minh họa này, giúp bạn hình dung các chủ đề chính và điểm cần lưu ý trong từng phần. Lộ trình bài học giúp bạn từ khởi đầu hiểu các khái niệm và thách thức cốt lõi đến cách giải quyết bằng kỹ thuật viết prompt và thực hành tốt nhất. Lưu ý phần "Kỹ Thuật Nâng Cao" trong hướng dẫn này tham chiếu đến nội dung chương _tiếp theo_ trong chương trình.

![Hướng Dẫn Minh Họa về Kỹ Thuật Viết Prompt](../../../translated_images/vi/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Khởi Nghiệp Của Chúng Ta

Giờ hãy nói về cách _chủ đề này_ liên quan đến sứ mệnh khởi nghiệp của chúng ta để [đem đổi mới AI vào giáo dục](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chúng ta muốn xây dựng các ứng dụng AI hỗ trợ _học tập cá nhân hóa_ - vậy hãy suy nghĩ cách các người dùng khác nhau của ứng dụng có thể "thiết kế" prompt:

- **Quản trị viên** có thể yêu cầu AI _phân tích dữ liệu chương trình học để xác định các khoảng trống trong nội dung_. AI có thể tóm tắt kết quả hoặc trực quan hóa bằng mã code.
- **Giáo viên** có thể yêu cầu AI _tạo kế hoạch bài học cho đối tượng và chủ đề cụ thể_. AI có thể xây dựng kế hoạch cá nhân hóa theo định dạng đã chỉ định.
- **Học sinh** có thể yêu cầu AI _dạy kèm khi gặp khó khăn trong môn học_. AI có thể hướng dẫn học sinh qua bài giảng, gợi ý và ví dụ tùy theo trình độ.

Đó chỉ là phần nổi của tảng băng chìm. Hãy xem [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - thư viện prompt mã nguồn mở được các chuyên gia giáo dục tuyển chọn - để có cái nhìn rộng hơn về tiềm năng! _Hãy thử chạy vài prompt đó trong sandbox hoặc sử dụng OpenAI Playground để xem kết quả!_

<!--
MẪU BÀI HỌC:
Đơn vị này nên đề cập khái niệm cốt lõi #1.
Củng cố khái niệm bằng ví dụ và tài liệu tham khảo.

KHÁI NIỆM #1:
Kỹ thuật viết prompt.
Định nghĩa và giải thích lý do cần thiết.
-->

## Kỹ Thuật Viết Prompt là gì?

Chúng ta bắt đầu bài học này bằng cách định nghĩa **Kỹ Thuật Viết Prompt** là quá trình _thiết kế và tối ưu hóa_ đầu vào văn bản (prompt) để cung cấp phản hồi (completion) chất lượng và nhất quán cho mục tiêu ứng dụng và mô hình cụ thể. Có thể coi đây là quá trình 2 bước:

- _thiết kế_ prompt ban đầu cho mô hình và mục tiêu nhất định
- _tinh chỉnh_ prompt liên tục để cải thiện chất lượng phản hồi

Đây là quá trình thử và sai đòi hỏi trực giác và nỗ lực của người dùng để đạt kết quả tối ưu. Vậy tại sao việc này lại quan trọng? Để trả lời, trước tiên cần hiểu ba khái niệm:

- _Phân tách từ (Tokenization)_ = cách mô hình "nhìn thấy" prompt
- _LLMs cơ bản_ = cách mô hình nền tảng "xử lý" prompt
- _LLMs được tinh chỉnh theo hướng chỉ dẫn_ = cách mô hình có thể "nhận biết nhiệm vụ"

### Phân tách từ (Tokenization)

Một LLM xem prompt như một _chuỗi các token_ trong đó các mô hình khác nhau (hoặc phiên bản khác nhau của một mô hình) có thể phân tách cùng một prompt theo cách khác nhau. Vì LLM được huấn luyện trên token (không phải văn bản thô), cách prompt được phân tách token ảnh hưởng trực tiếp đến chất lượng phản hồi sinh ra.

Để hiểu cơ chế tokenization, thử dùng các công cụ như [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) được minh họa dưới đây. Sao chép prompt của bạn - và xem nó được chuyển đổi thành token thế nào, chú ý cách xử lý ký tự khoảng trắng và dấu câu. Lưu ý ví dụ này dùng LLM cũ hơn (GPT-3) - nên thử với mô hình mới hơn có thể cho kết quả khác.

![Phân tách từ (Tokenization)](../../../translated_images/vi/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Khái niệm: Mô Hình Nền Tảng (Foundation Models)

Khi một prompt được phân tách thành token, chức năng chính của ["LLM cơ bản"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (hay mô hình nền tảng) là dự đoán token tiếp theo trong chuỗi. Vì LLM được huấn luyện trên bộ dữ liệu văn bản khổng lồ, mô hình có khả năng nắm bắt quan hệ thống kê giữa các token và dự đoán token với độ tin cậy nhất định. Lưu ý chúng không hiểu _ý nghĩa_ của từ trong prompt hay token; chúng chỉ nhìn thấy mẫu có thể "hoàn thành" bằng dự đoán tiếp theo. Mô hình có thể tiếp tục dự đoán chuỗi đến khi bị ngắt bởi người dùng hoặc điều kiện đã định.

Muốn xem cách hoàn thành dựa trên prompt hoạt động ra sao? Nhập prompt trên vào [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) với các thiết lập mặc định. Hệ thống được cấu hình xử lý prompt như yêu cầu thông tin - bạn sẽ thấy một phản hồi phù hợp với bối cảnh này.

Nhưng nếu người dùng muốn thấy điều gì đó cụ thể, đáp ứng tiêu chí hoặc mục tiêu nhiệm vụ? Lúc này các LLM _được tinh chỉnh theo chỉ dẫn_ sẽ vào cuộc.

![Hoàn thành Chat của LLM cơ bản](../../../translated_images/vi/04-playground-chat-base.65b76fcfde0caa67.webp)

### Khái niệm: LLM được Tinh Chỉnh Theo Hướng Chỉ Dẫn (Instruction Tuned LLMs)

Một [LLM được tinh chỉnh theo hướng chỉ dẫn](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bắt đầu từ mô hình nền tảng và được tinh chỉnh thêm với các ví dụ hoặc cặp đầu vào/đầu ra (ví dụ: "tin nhắn" đa lượt) có thể chứa các chỉ dẫn rõ ràng - và phản hồi AI cố gắng tuân theo chỉ dẫn đó.

Điều này sử dụng các kỹ thuật như Học Tăng Cường với Phản Hồi Con Người (RLHF) để đào tạo mô hình _tuân theo chỉ dẫn_ và _học từ phản hồi_ nhằm tạo phản hồi phù hợp hơn với ứng dụng thực tiễn và liên quan hơn đến mục tiêu người dùng.

Hãy thử lại - quay lại prompt trên, nhưng bây giờ đổi _tin nhắn hệ thống_ để cung cấp chỉ dẫn sau làm bối cảnh:

> _Tóm tắt nội dung bạn được cung cấp cho học sinh lớp hai. Giữ kết quả trong một đoạn văn có 3-5 ý chính._

Thấy kết quả bây giờ được điều chỉnh để phản ánh mục tiêu và định dạng mong muốn chưa? Giáo viên có thể dùng trực tiếp phản hồi này trong slide bài giảng.

![Hoàn thành Chat của LLM được tinh chỉnh theo chỉ dẫn](../../../translated_images/vi/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Tại sao chúng ta cần Kỹ Thuật Viết Prompt?

Giờ khi đã hiểu cách LLM xử lý prompt, hãy nói về _tại sao_ cần kỹ thuật viết prompt. Câu trả lời nằm ở chỗ các LLM hiện nay có một số thách thức làm cho việc tạo ra các phản hồi _đáng tin cậy và nhất quán_ trở nên khó khăn hơn nếu không đầu tư nỗ lực trong thiết kế và tối ưu prompt. Ví dụ:

1. **Phản hồi mô hình mang tính ngẫu nhiên.** _Cùng một prompt_ có thể tạo ra các phản hồi khác nhau với các mô hình hay phiên bản khác nhau. Và cũng có thể gửi cùng một prompt đến _cùng một mô hình_ vào các thời điểm khác nhau mà ra kết quả khác nhau. _Kỹ thuật viết prompt có thể giúp ta giảm thiểu sự biến đổi này bằng cách đưa ra các rào chắn tốt hơn_.

1. **Mô hình có thể "bịa đặt" phản hồi.** Mô hình được huấn luyện trên bộ dữ liệu _rộng nhưng hữu hạn_, nghĩa là chúng thiếu kiến thức về các khái niệm nằm ngoài phạm vi huấn luyện. Do đó, chúng có thể tạo ra các phản hồi sai lệch, tưởng tượng, hay thậm chí mâu thuẫn trực tiếp với thực tế. _Kỹ thuật viết prompt giúp người dùng nhận biết và giảm thiểu điều này, ví dụ bằng cách yêu cầu AI trích dẫn nguồn hoặc giải thích lý do_.

1. **Năng lực mô hình sẽ khác nhau.** Các mô hình thế hệ mới hơn hay các phiên bản sẽ có năng lực phong phú hơn nhưng cũng đem đến các đặc điểm riêng biệt và sự đánh đổi về chi phí & độ phức tạp. _Kỹ thuật viết prompt giúp phát triển thực hành tốt và quy trình làm việc để trừu tượng hóa sự khác biệt, thích ứng với yêu cầu riêng của từng mô hình một cách mở rộng và liền mạch_.

Hãy xem minh họa trong OpenAI hoặc Azure OpenAI Playground:

- Dùng cùng prompt với các triển khai LLM khác nhau (ví dụ OpenAI, Azure OpenAI, Hugging Face) - bạn thấy sự khác biệt không?
- Dùng lặp lại prompt với cùng một triển khai LLM (ví dụ Azure OpenAI playground) - các lần khác biệt như thế nào?

### Ví dụ về Bịa đặt

Trong khóa học này, ta dùng thuật ngữ **"bịa đặt"** để chỉ hiện tượng LLM đôi khi tạo ra thông tin sai sự thật do giới hạn trong tập huấn luyện hoặc những ràng buộc khác. Bạn có thể đã nghe gọi là _"ảo tưởng"_ trong bài viết hay nghiên cứu phổ biến. Tuy nhiên, chúng tôi khuyên dùng từ _"bịa đặt"_ để tránh vô tình nhân cách hóa hành vi này bằng cách gán các đặc tính con người cho kết quả do máy sinh ra. Điều này cũng củng cố các [hướng dẫn AI có trách nhiệm](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) về mặt thuật ngữ, loại bỏ các từ có thể bị coi là xúc phạm hoặc không bao gồm trong một số bối cảnh.

Muốn hình dung cách bịa đặt hoạt động? Hãy nghĩ đến prompt yêu cầu AI tạo nội dung cho chủ đề không tồn tại (để đảm bảo không có trong dữ liệu huấn luyện). Ví dụ - tôi thử prompt này:

> **Prompt:** tạo kế hoạch bài học về Cuộc Chiến trên Sao Hỏa năm 2076.

Tìm kiếm trên web cho thấy có các chuyện hư cấu (ví dụ: phim truyền hình hay sách) về chiến tranh Sao Hỏa - nhưng không có vào năm 2076. Hiểu biết phổ thông cũng cho biết năm 2076 là _tương lai_ nên không thể liên quan tới sự kiện có thật.


Vậy điều gì sẽ xảy ra khi chúng ta chạy lời nhắc này với các nhà cung cấp LLM khác nhau?

> **Phản hồi 1**: OpenAI Playground (GPT-35)

![Phản hồi 1](../../../translated_images/vi/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Phản hồi 2**: Azure OpenAI Playground (GPT-35)

![Phản hồi 2](../../../translated_images/vi/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Phản hồi 3**: : Hugging Face Chat Playground (LLama-2)

![Phản hồi 3](../../../translated_images/vi/04-fabrication-huggingchat.faf82a0a51278956.webp)

Như mong đợi, mỗi mô hình (hoặc phiên bản mô hình) tạo ra các phản hồi hơi khác nhau nhờ vào hành vi ngẫu nhiên và sự khác biệt về khả năng mô hình. Ví dụ, một mô hình hướng tới đối tượng học sinh lớp 8 trong khi mô hình khác giả định học sinh trung học. Nhưng cả ba mô hình đều tạo ra các phản hồi có thể thuyết phục người dùng chưa được thông tin rằng sự kiện đó là có thật.

Các kỹ thuật kỹ thuật lời nhắc như _metaprompting_ và _cấu hình nhiệt độ_ có thể giảm bớt việc bịa đặt của mô hình đến một mức độ nhất định. Các _kiến trúc_ kỹ thuật lời nhắc mới cũng tích hợp liền mạch các công cụ và kỹ thuật mới vào luồng lời nhắc, để giảm thiểu hoặc hạn chế một số hiệu ứng này.

## Nghiên cứu tình huống: GitHub Copilot

Hãy kết thúc phần này bằng cách tìm hiểu cách kỹ thuật lời nhắc được ứng dụng trong các giải pháp thực tế thông qua một nghiên cứu tình huống: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot là "Trợ lý Lập trình AI" của bạn - nó chuyển đổi lời nhắc văn bản thành các gợi ý mã và được tích hợp vào môi trường phát triển của bạn (ví dụ: Visual Studio Code) để mang lại trải nghiệm người dùng mượt mà. Như được ghi lại trong loạt bài blog dưới đây, phiên bản đầu tiên dựa trên mô hình OpenAI Codex - với các kỹ sư nhanh chóng nhận ra cần phải tinh chỉnh mô hình và phát triển các kỹ thuật kỹ thuật lời nhắc tốt hơn để cải thiện chất lượng mã. Vào tháng 7, họ đã [ra mắt một mô hình AI cải tiến vượt qua Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) nhằm cung cấp gợi ý nhanh hơn.

Đọc các bài đăng theo thứ tự để theo dõi hành trình học hỏi của họ.

- **Tháng 5 2023** | [GitHub Copilot ngày càng hiểu mã của bạn tốt hơn](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Tháng 5 2023** | [Bên trong GitHub: Làm việc với các LLM phía sau GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Tháng 6 2023** | [Cách viết lời nhắc tốt hơn cho GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Tháng 7 2023** | [.. GitHub Copilot vượt qua Codex với mô hình AI được cải thiện](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Tháng 7 2023** | [Hướng dẫn Phát triển về Kỹ thuật Lời nhắc và LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Tháng 9 2023** | [Cách xây dựng ứng dụng LLM doanh nghiệp: Bài học từ GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Bạn cũng có thể duyệt [blog Kỹ thuật](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) của họ để xem thêm các bài viết như [bài này](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) cho thấy cách các mô hình và kỹ thuật này được _ứng dụng_ để phát triển các ứng dụng thực tế.

---

<!--
MẪU BÀI HỌC:
Đơn vị này nên bao gồm khái niệm cốt lõi #2.
Củng cố khái niệm với ví dụ và tài liệu tham khảo.

KHÁI NIỆM #2:
Thiết kế Lời nhắc.
Minh họa với các ví dụ.
-->

## Cấu trúc Lời nhắc

Chúng ta đã thấy tại sao kỹ thuật lời nhắc lại quan trọng - bây giờ hãy cùng hiểu cách lời nhắc được _xây dựng_ để chúng ta có thể đánh giá các kỹ thuật khác nhau nhằm thiết kế lời nhắc hiệu quả hơn.

### Lời nhắc cơ bản

Hãy bắt đầu với lời nhắc cơ bản: một đầu vào văn bản gửi đến mô hình mà không có bối cảnh nào khác. Đây là một ví dụ - khi chúng ta gửi vài từ đầu của quốc ca Mỹ đến OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) thì ngay lập tức nó _hoàn thành_ phản hồi bằng những dòng tiếp theo, minh họa hành vi dự đoán cơ bản.

| Lời nhắc (Đầu vào) | Hoàn thành (Đầu ra)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Nghe có vẻ bạn đang bắt đầu lời bài hát "The Star-Spangled Banner," quốc ca của Hoa Kỳ. Toàn bộ lời bài hát là ...                          |

### Lời nhắc phức tạp

Bây giờ hãy thêm bối cảnh và hướng dẫn vào lời nhắc cơ bản đó. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) cho phép chúng ta xây dựng lời nhắc phức tạp dưới dạng tập hợp các _tin nhắn_ với:

- Các cặp đầu vào/đầu ra phản ánh đầu vào của _người dùng_ và phản hồi của _trợ lý_.
- Tin nhắn hệ thống đặt bối cảnh cho hành vi hoặc cá tính của trợ lý.

Yêu cầu hiện nay có dạng dưới đây, trong đó _phân đoạn token_ hiệu quả nắm bắt thông tin liên quan từ bối cảnh và cuộc trò chuyện. Bây giờ, việc thay đổi bối cảnh hệ thống có thể ảnh hưởng lớn đến chất lượng các câu trả lời, tương đương với các đầu vào của người dùng được cung cấp.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Lời nhắc hướng dẫn

Trong các ví dụ trên, lời nhắc của người dùng là câu truy vấn văn bản đơn giản có thể được hiểu là yêu cầu thông tin. Với lời nhắc _hướng dẫn_, chúng ta có thể dùng văn bản đó để chỉ định nhiệm vụ chi tiết hơn, cung cấp hướng dẫn tốt hơn cho AI. Đây là một ví dụ:

| Lời nhắc (Đầu vào)                                                                                                                                                                                                                         | Hoàn thành (Đầu ra)                                                                                                        | Loại hướng dẫn      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Viết mô tả về Nội chiến                                                                                                                                                                                                                   | _trả về một đoạn văn đơn giản_                                                                                            | Đơn giản            |
| Viết mô tả về Nội chiến. Cung cấp các ngày tháng và sự kiện chính cùng với mô tả ý nghĩa của chúng                                                                                                                                        | _trả về đoạn văn kèm danh sách ngày sự kiện chính với mô tả_                                                             | Phức tạp            |
| Viết mô tả về Nội chiến trong 1 đoạn văn. Cung cấp 3 điểm chính với ngày tháng quan trọng và ý nghĩa của chúng. Cung cấp thêm 3 điểm chính với các nhân vật lịch sử quan trọng và đóng góp của họ. Trả kết quả dưới dạng tập tin JSON                     | _trả về chi tiết nhiều hơn trong hộp thoại, định dạng dưới dạng JSON bạn có thể sao chép-dán vào tập tin và kiểm tra khi cần_ | Phức tạp. Định dạng. |

## Nội dung chính

Trong các ví dụ trên, lời nhắc vẫn khá mở, cho phép LLM tự quyết định phần dữ liệu tiền huấn luyện nào là liên quan. Với mẫu thiết kế _nội dung chính_, văn bản đầu vào được chia thành hai phần:

- một hướng dẫn (hành động)
- nội dung liên quan (ảnh hưởng đến hành động)

Đây là ví dụ trong đó lệnh là "tóm tắt nội dung này trong 2 câu".

| Lời nhắc (Đầu vào)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Hoàn thành (Đầu ra)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sao Mộc là hành tinh thứ năm từ Mặt Trời và là lớn nhất trong Hệ Mặt Trời. Nó là một hành tinh khí với khối lượng bằng một phần nghìn so với Mặt Trời, nhưng lại lớn gấp hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn thấy bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi có lịch sử ghi chép. Nó được đặt theo tên thần Jupiter của La Mã.[19] Khi quan sát từ Trái Đất, Sao Mộc có thể đủ sáng để ánh sáng phản chiếu của nó tạo thành bóng nhìn thấy được,[20] và nó trung bình là vật thể sáng thứ ba trên bầu trời đêm sau Mặt Trăng và Sao Kim. <br/> **Tóm tắt trong 2 câu ngắn gọn** | Sao Mộc, hành tinh thứ năm từ Mặt Trời, là lớn nhất trong Hệ Mặt Trời và nổi tiếng là một trong những vật thể sáng nhất trên bầu trời đêm. Được đặt theo tên thần Jupiter của La Mã, đó là hành tinh khí có khối lượng gấp hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác trong Hệ Mặt Trời cộng lại. |

Phần nội dung chính có thể được sử dụng theo nhiều cách khác nhau để tạo ra các hướng dẫn hiệu quả hơn:

- **Ví dụ** - thay vì nói cho mô hình biết phải làm gì qua lệnh rõ ràng, hãy đưa ví dụ cho nó về những gì cần làm và để nó suy luận mẫu.
- **Dấu hiệu** - theo sau hướng dẫn bằng một "dấu hiệu" để khởi động hoàn thành, hướng dẫn mô hình tới các phản hồi liên quan hơn.
- **Mẫu** - đây là những 'công thức' lặp lại cho lời nhắc với các chỗ giữ chỗ (biến) có thể tùy chỉnh với dữ liệu cho các trường hợp cụ thể.

Hãy khám phá chúng trong thực tế.

### Sử dụng Ví dụ

Đây là cách tiếp cận trong đó bạn dùng phần nội dung chính để "cung cấp cho mô hình" một số ví dụ về đầu ra mong muốn đối với một hướng dẫn nhất định, và để mô hình suy luận ra mẫu đầu ra mong muốn. Dựa trên số lượng ví dụ được cung cấp, chúng ta có thể có lời nhắc zero-shot, one-shot, few-shot, v.v.

Lời nhắc bây giờ bao gồm ba thành phần:

- Mô tả nhiệm vụ
- Một vài ví dụ về đầu ra mong muốn
- Phần bắt đầu một ví dụ mới (trở thành mô tả nhiệm vụ ngầm định)

| Loại học | Lời nhắc (Đầu vào)                                                                                                                                        | Hoàn thành (Đầu ra)         |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot | "Mặt Trời đang tỏa sáng". Dịch sang tiếng Tây Ban Nha                                                                                                 | "El Sol está brillando".    |
| One-shot  | "Mặt Trời đang tỏa sáng" => ""El Sol está brillando". <br> "Ngày hôm nay trời lạnh và gió" =>                                                        | "Es un día frío y ventoso". |
| Few-shot  | Người chơi chạy quanh các căn cứ => Bóng chày <br/> Người chơi đánh ace => Quần vợt <br/> Người chơi ghi sáu điểm => Cricket <br/> Người chơi úp rổ =>       | Bóng rổ                      |
|           |                                                                                                                                                       |                             |

Lưu ý cách chúng ta phải cung cấp hướng dẫn rõ ràng ("Dịch sang tiếng Tây Ban Nha") trong lời nhắc zero-shot, nhưng nó được suy luận trong ví dụ one-shot. Ví dụ few-shot cho thấy cách thêm nhiều ví dụ hơn giúp mô hình suy luận chính xác hơn mà không cần hướng dẫn bổ sung.

### Dấu hiệu Lời nhắc

Một kỹ thuật khác để dùng nội dung chính là cung cấp _dấu hiệu_ thay vì ví dụ. Trong trường hợp này, chúng ta đưa cho mô hình một sự khởi đầu đúng hướng bằng một đoạn văn bản phản ánh định dạng phản hồi mong muốn. Mô hình sau đó "nhận tín hiệu" để tiếp tục theo hướng đó.

| Số dấu hiệu | Lời nhắc (Đầu vào)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Hoàn thành (Đầu ra)                                                                                                                                                                                                                                                                                       |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0           | Sao Mộc là hành tinh thứ năm từ Mặt Trời và là lớn nhất trong Hệ Mặt Trời. Nó là hành tinh khí với khối lượng bằng một phần nghìn so với Mặt Trời, nhưng gấp hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn thấy bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi có lịch sử ghi chép. <br/>**Tóm tắt nội dung này**                                       | Sao Mộc là hành tinh lớn nhất trong Hệ Mặt Trời và là hành tinh thứ năm tính từ Mặt Trời. Nó là hành tinh khí với khối lượng bằng 1/1000 khối lượng Mặt Trời, nhưng nặng hơn tất cả các hành tinh khác cộng lại. Các nền văn minh cổ đại đã biết đến Sao Mộc từ lâu, và nó dễ dàng nhìn thấy trên bầu trời đêm. |
| 1           | Sao Mộc là hành tinh thứ năm từ Mặt Trời và là lớn nhất trong Hệ Mặt Trời. Nó là hành tinh khí với khối lượng bằng một phần nghìn so với Mặt Trời, nhưng gấp hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn thấy bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi có lịch sử ghi chép. <br/>**Tóm tắt nội dung này** <br/> Điều chúng ta học được là Sao Mộc | là hành tinh thứ năm từ Mặt Trời và là lớn nhất trong Hệ Mặt Trời. Nó là hành tinh khí với khối lượng bằng một phần nghìn so với Mặt Trời, nhưng gấp hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác cộng lại. Nó dễ dàng nhìn thấy bằng mắt thường và đã được biết từ thời cổ đại.                        |

| 2              | Sao Mộc là hành tinh thứ năm tính từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. Nó là một hành tinh khí khổng lồ với khối lượng bằng một phần nghìn khối lượng của Mặt Trời, nhưng lớn hơn hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn thấy bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi có lịch sử được ghi chép. <br/>**Tóm tắt này** <br/> Top 3 Sự Thật Chúng Ta Học Được:         | 1. Sao Mộc là hành tinh thứ năm tính từ Mặt Trời và lớn nhất trong Hệ Mặt Trời. <br/> 2. Nó là một hành tinh khí khổng lồ với khối lượng bằng một phần nghìn khối lượng của Mặt Trời...<br/> 3. Sao Mộc đã có thể nhìn thấy bằng mắt thường từ thời cổ đại ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Mẫu Lời Nhắc

Mẫu lời nhắc là một _công thức định nghĩa trước cho một lời nhắc_ mà có thể được lưu trữ và tái sử dụng khi cần, nhằm tạo ra trải nghiệm người dùng nhất quán hơn ở quy mô lớn. Ở dạng đơn giản nhất, nó chỉ là một tập hợp các ví dụ lời nhắc như [ví dụ này từ OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) cung cấp cả thành phần lời nhắc tương tác (tin nhắn người dùng và hệ thống) cũng như định dạng yêu cầu dựa trên API - để hỗ trợ tái sử dụng.

Ở dạng phức tạp hơn như [ví dụ này từ LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), nó chứa các _chỗ giữ chỗ_ có thể được thay thế bằng dữ liệu từ nhiều nguồn khác nhau (đầu vào người dùng, ngữ cảnh hệ thống, nguồn dữ liệu bên ngoài, v.v.) để tạo lời nhắc một cách động. Điều này cho phép chúng ta tạo thư viện lời nhắc có thể tái sử dụng để tạo ra trải nghiệm người dùng nhất quán **một cách lập trình** ở quy mô lớn.

Cuối cùng, giá trị thực sự của các mẫu nằm ở khả năng tạo và xuất bản _thư viện lời nhắc_ cho các lĩnh vực ứng dụng theo ngành - nơi mẫu lời nhắc được _tối ưu hóa_ để phản ánh bối cảnh hoặc ví dụ cụ thể của ứng dụng nhằm làm cho phản hồi phù hợp và chính xác hơn với đối tượng người dùng mục tiêu. Kho [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) là một ví dụ rất tốt về cách tiếp cận này, biên soạn một thư viện lời nhắc dành cho lĩnh vực giáo dục với trọng tâm vào các mục tiêu chính như lập kế hoạch bài học, thiết kế chương trình học, hướng dẫn học sinh, v.v.

## Nội dung hỗ trợ

Nếu chúng ta nghĩ về việc xây dựng lời nhắc như có một chỉ dẫn (nhiệm vụ) và một mục tiêu (nội dung chính), thì _nội dung phụ_ giống như bối cảnh bổ sung mà chúng ta cung cấp để **ảnh hưởng đến đầu ra theo một cách nào đó**. Nó có thể là các tham số điều chỉnh, hướng dẫn định dạng, hệ thống phân loại chủ đề, v.v. giúp mô hình _điều chỉnh_ phản hồi sao cho phù hợp với các mục tiêu hoặc kỳ vọng mong muốn của người dùng.

Ví dụ: Cho một danh mục khóa học với nhiều siêu dữ liệu chi tiết (tên, mô tả, cấp độ, thẻ siêu dữ liệu, giảng viên, v.v.) trên tất cả các khóa học có trong chương trình giảng dạy:

- chúng ta có thể định nghĩa một chỉ dẫn là "tóm tắt danh mục khóa học cho học kỳ Thu 2023"
- chúng ta có thể dùng nội dung chính để cung cấp vài ví dụ về đầu ra mong muốn
- chúng ta có thể dùng nội dung phụ để xác định 5 "thẻ" hàng đầu quan tâm.

Bây giờ, mô hình có thể cung cấp bản tóm tắt theo định dạng được trình bày qua vài ví dụ - nhưng nếu một kết quả gắn nhiều thẻ, nó có thể ưu tiên 5 thẻ được xác định trong nội dung phụ.

---

<!--
MẪU BÀI HỌC:
Đơn vị này nên bao gồm khái niệm cốt lõi #1.
Củng cố khái niệm với các ví dụ và tài liệu tham khảo.

KHÁI NIỆM #3:
Kỹ thuật Kỹ Thuật Lời Nhắc.
Một số kỹ thuật cơ bản cho kỹ thuật lời nhắc là gì?
Minh họa bằng vài bài tập.
-->

## Thực hành tốt nhất về Lời Nhắc

Bây giờ chúng ta đã biết lời nhắc có thể được _xây dựng_ như thế nào, chúng ta có thể bắt đầu suy nghĩ về cách _thiết kế_ chúng để phản ánh các thực hành tốt nhất. Chúng ta có thể nghĩ về điều này thành hai phần - có được _tư duy_ đúng và áp dụng _kỹ thuật_ phù hợp.

### Tư duy Kỹ thuật Lời Nhắc

Kỹ thuật Lời Nhắc là một quá trình thử và sai nên hãy nhớ ba yếu tố hướng dẫn rộng:

1. **Hiểu biết về lĩnh vực là quan trọng.** Độ chính xác và phù hợp của phản hồi phụ thuộc vào _lĩnh vực_ mà ứng dụng hoặc người dùng hoạt động. Áp dụng trực giác và chuyên môn lĩnh vực của bạn để **tùy chỉnh kỹ thuật** hơn nữa. Ví dụ, định nghĩa _tính cách cụ thể theo lĩnh vực_ trong lời nhắc hệ thống của bạn, hoặc sử dụng _mẫu lời nhắc riêng cho lĩnh vực_ trong lời nhắc người dùng. Cung cấp nội dung phụ phản ánh bối cảnh cụ thể lĩnh vực, hoặc dùng _dấu hiệu và ví dụ đặc thù theo lĩnh vực_ để hướng mô hình theo các mẫu sử dụng quen thuộc.

2. **Hiểu biết về mô hình là quan trọng.** Chúng ta biết mô hình bản chất là ngẫu nhiên. Nhưng các triển khai mô hình cũng có thể khác nhau về tập dữ liệu đào tạo mà chúng sử dụng (kiến thức được huấn luyện trước), các khả năng mà chúng cung cấp (ví dụ: qua API hoặc SDK) và loại nội dung mà chúng được tối ưu hóa (ví dụ: mã nguồn so với hình ảnh so với văn bản). Hiểu điểm mạnh và hạn chế của mô hình bạn đang sử dụng, và dùng kiến thức đó để _ưu tiên nhiệm vụ_ hoặc xây dựng _mẫu tùy chỉnh_ được tối ưu cho khả năng của mô hình.

3. **Lặp lại & Xác thực là quan trọng.** Mô hình phát triển nhanh chóng, cũng như kỹ thuật kỹ thuật lời nhắc. Là chuyên gia lĩnh vực, bạn có thể có bối cảnh hoặc tiêu chí riêng cho _ứng dụng_ cụ thể của bạn, mà có thể không áp dụng cho cộng đồng rộng lớn hơn. Dùng công cụ & kỹ thuật kỹ thuật lời nhắc để "khởi động nhanh" việc xây dựng lời nhắc, rồi lặp lại và xác thực kết quả bằng trực giác và chuyên môn lĩnh vực của bạn. Ghi chép lại những hiểu biết và tạo **cơ sở tri thức** (ví dụ, thư viện lời nhắc) có thể được người khác sử dụng làm nền tảng mới, giúp lặp lại nhanh hơn trong tương lai.

## Thực hành Tốt nhất

Bây giờ hãy xem các thực hành tốt nhất phổ biến được các chuyên gia [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) và [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) khuyến nghị.

| Điều gì                           | Tại sao                                                                                                                                                                                                                                           |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đánh giá các mô hình mới nhất.    | Thế hệ mô hình mới có thể có các tính năng và chất lượng cải tiến - nhưng cũng có thể phát sinh chi phí cao hơn. Đánh giá chúng về tác động, sau đó đưa ra quyết định di cư.                                                                  |
| Tách biệt chỉ dẫn & bối cảnh      | Kiểm tra xem mô hình/nhà cung cấp của bạn có xác định _dấu phân cách_ để phân biệt rõ chỉ dẫn, nội dung chính và phụ không. Điều này có thể giúp mô hình phân bổ trọng số chính xác hơn cho các token.                                         |
| Rõ ràng và cụ thể                 | Cung cấp nhiều chi tiết hơn về bối cảnh, kết quả, độ dài, định dạng, phong cách mong muốn, v.v. Điều này sẽ cải thiện cả chất lượng và tính nhất quán của phản hồi. Ghi lại công thức thành các mẫu có thể tái sử dụng.                             |
| Mô tả chi tiết, sử dụng ví dụ      | Mô hình có thể phản hồi tốt hơn với cách tiếp cận "trình bày và chỉ dẫn". Bắt đầu với cách tiếp cận `zero-shot` (không ví dụ) rồi thử `few-shot` để tinh chỉnh, cung cấp một vài ví dụ về đầu ra mong muốn. Dùng các phép ẩn dụ.                  |
| Dùng dấu hiệu để khởi động phản hồi | Hướng mô hình đến kết quả mong muốn bằng cách cung cấp vài từ hoặc cụm từ đầu để nó dùng làm điểm khởi đầu cho phản hồi.                                                                                                                     |
| Lặp lại                          | Đôi khi bạn cần nhắc lại với mô hình. Đưa chỉ dẫn trước và sau nội dung chính, dùng kết hợp chỉ dẫn và dấu hiệu, v.v. Lặp lại và xác thực để xem cái nào hiệu quả.                                                                           |
| Thứ tự quan trọng                | Thứ tự bạn trình bày thông tin cho mô hình có thể ảnh hưởng đến đầu ra, ngay cả trong các ví dụ học, nhờ thiên vị mới nhất. Thử các tùy chọn khác nhau để xem cái nào tốt nhất.                                                               |
| Cung cấp "lối thoát" cho mô hình | Đưa cho mô hình một phản hồi _dự phòng_ để nó cung cấp nếu không thể hoàn thành nhiệm vụ vì lý do gì đó. Điều này giúp giảm khả năng mô hình tạo ra phản hồi sai hoặc bịa đặt.                                                                 |
|                                   |                                                                                                                                                                                                                                                 |

Như bất kỳ thực hành tốt nhất nào, hãy nhớ rằng _kết quả có thể khác nhau_ dựa trên mô hình, nhiệm vụ và lĩnh vực. Dùng đây làm điểm bắt đầu, rồi lặp lại để tìm ra cách phù hợp nhất với bạn. Liên tục đánh giá lại quy trình kỹ thuật lời nhắc khi có mô hình và công cụ mới, với trọng tâm vào tính mở rộng quy trình và chất lượng phản hồi.

<!--
MẪU BÀI HỌC:
Đơn vị này nên cung cấp một thử thách lập trình nếu có thể

THỬ THÁCH:
Liên kết tới một Jupyter Notebook chỉ có các chú thích mã trong phần hướng dẫn (các phần mã trống).

GIẢI PHÁP:
Liên kết tới bản sao notebook đó với các lời nhắc đã điền và chạy, cho thấy một ví dụ có thể.
-->

## Bài Tập

Chúc mừng! Bạn đã hoàn thành bài học! Đã đến lúc thử một vài khái niệm và kỹ thuật đó với các ví dụ thực tế!

Đối với bài tập của chúng ta, chúng ta sẽ sử dụng một Jupyter Notebook với các bài tập bạn có thể thực hiện tương tác. Bạn cũng có thể mở rộng Notebook với các ô Markdown và Mã của riêng bạn để khám phá ý tưởng và kỹ thuật theo cách riêng.

### Để bắt đầu, phân nhánh repo, sau đó

- (Khuyến nghị) Khởi chạy GitHub Codespaces
- (Thay thế) Sao chép repo về thiết bị cục bộ của bạn và sử dụng cùng Docker Desktop
- (Thay thế) Mở Notebook bằng môi trường runtime Notebook bạn thích.

### Tiếp theo, cấu hình biến môi trường

- Sao chép tập tin `.env.copy` trong thư mục gốc repo thành `.env` và điền các giá trị `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` và `AZURE_OPENAI_DEPLOYMENT`. Quay lại [phần Sandbox Học tập](#môi-trường-học-tập-sandbox) để tìm hiểu cách thực hiện.

### Tiếp theo, mở Jupyter Notebook

- Chọn kernel runtime. Nếu dùng lựa chọn 1 hoặc 2, đơn giản chọn kernel Python 3.10.x mặc định được cung cấp bởi container phát triển.

Bạn đã sẵn sàng chạy các bài tập. Lưu ý rằng không có câu trả lời _đúng hay sai_ ở đây - chỉ là khám phá các tùy chọn thông qua thử và sai và xây dựng trực giác về cái gì hoạt động cho mô hình và lĩnh vực ứng dụng nhất định.

_Vì lý do này, bài học không có phần Giải pháp Mã. Thay vào đó, Notebook sẽ có các ô Markdown tiêu đề "Giải pháp của tôi:" cho thấy một ví dụ kết quả để tham khảo._

 <!--
MẪU BÀI HỌC:
Tổng kết phần này với tóm tắt và tài nguyên để tự học.
-->

## Kiểm tra kiến thức

Câu nào sau đây là một lời nhắc tốt theo một số thực hành hợp lý?

1. Cho tôi xem hình một chiếc xe màu đỏ
2. Cho tôi xem hình một chiếc xe màu đỏ hiệu Volvo và mẫu XC90 đậu bên vách đá với mặt trời đang lặn
3. Cho tôi xem hình một chiếc xe màu đỏ hiệu Volvo và mẫu XC90

A: 2, là lời nhắc tốt nhất vì nó cung cấp chi tiết về "cái gì" và đi vào cụ thể (không chỉ bất kỳ xe nào mà là hiệu và mẫu cụ thể) và cũng mô tả bối cảnh tổng thể. 3 là lựa chọn kế tiếp vì cũng chứa nhiều mô tả.

## 🚀 Thử thách

Thử xem bạn có thể tận dụng kỹ thuật "dấu hiệu" với lời nhắc: Hoàn thành câu "Cho tôi xem hình một chiếc xe màu đỏ hiệu Volvo và ". Phản hồi thế nào, và bạn sẽ cải thiện nó ra sao?

## Làm tốt lắm! Tiếp tục học hỏi

Muốn tìm hiểu thêm về các khái niệm Kỹ thuật Lời Nhắc khác? Vào [trang học tiếp](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tìm các tài nguyên tuyệt vời khác về chủ đề này.

Hãy đến Bài học 5 nơi chúng ta sẽ xem xét [kỹ thuật lời nhắc nâng cao](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->