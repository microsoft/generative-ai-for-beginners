# Các nguyên lý cơ bản về Kỹ thuật Đề bài

[![Các nguyên lý cơ bản về Kỹ thuật Đề bài](../../../translated_images/vi/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Giới thiệu
Mô-đun này bao gồm các khái niệm và kỹ thuật thiết yếu để tạo ra các đề bài hiệu quả trong các mô hình AI sinh tạo. Cách bạn viết đề bài cho một LLM cũng rất quan trọng. Một đề bài được thiết kế cẩn thận có thể đạt được chất lượng phản hồi tốt hơn. Nhưng chính xác các thuật ngữ như _đề bài_ và _kỹ thuật đề bài_ có nghĩa là gì? Và làm thế nào để tôi cải thiện đề bài _đầu vào_ mà tôi gửi đến LLM? Đây là những câu hỏi chúng ta sẽ cố gắng trả lời trong chương này và chương tiếp theo.

_AI sinh tạo_ có khả năng tạo ra nội dung mới (ví dụ: văn bản, hình ảnh, âm thanh, mã v.v.) dựa trên yêu cầu của người dùng. Nó đạt được điều này bằng cách sử dụng _Mô hình Ngôn ngữ Lớn_ như loạt GPT của OpenAI ("Generative Pre-trained Transformer") được huấn luyện sử dụng ngôn ngữ tự nhiên và mã.

Người dùng hiện có thể tương tác với các mô hình này bằng các phương thức quen thuộc như chat, mà không cần chuyên môn kỹ thuật hay đào tạo. Các mô hình dựa trên _đề bài_ - người dùng gửi đầu vào văn bản (đề bài) và nhận lại phản hồi AI (hoàn thành). Họ có thể "trò chuyện với AI" theo cách lặp đi lặp lại trong các cuộc hội thoại nhiều lượt, tinh chỉnh đề bài cho đến khi phản hồi phù hợp với mong đợi.

"Đề bài" giờ đây trở thành _giao diện lập trình_ chính cho các ứng dụng AI sinh tạo, chỉ dẫn cho các mô hình những gì cần làm và ảnh hưởng đến chất lượng phản hồi được trả về. "Kỹ thuật Đề bài" là một lĩnh vực nghiên cứu phát triển nhanh tập trung vào _thiết kế và tối ưu hóa_ đề bài để cung cấp các phản hồi nhất quán và chất lượng ở quy mô lớn.

## Mục tiêu học tập

Trong bài học này, chúng ta sẽ tìm hiểu kỹ thuật đề bài là gì, tại sao nó quan trọng và làm thế nào để tạo ra những đề bài hiệu quả hơn cho một mô hình và mục tiêu ứng dụng cụ thể. Chúng ta sẽ hiểu các khái niệm cốt lõi và các thực hành tốt nhất cho kỹ thuật đề bài - và khám phá một môi trường tương tác Jupyter Notebook "sandbox" nơi chúng ta có thể thấy các khái niệm này được áp dụng vào các ví dụ thực tế.

Vào cuối bài học này, chúng ta sẽ có khả năng:

1. Giải thích kỹ thuật đề bài là gì và tại sao nó quan trọng.
2. Mô tả các thành phần của một đề bài và cách chúng được sử dụng.
3. Học các thực hành tốt nhất và kỹ thuật cho kỹ thuật đề bài.
4. Áp dụng các kỹ thuật đã học vào các ví dụ thực tế, sử dụng một điểm cuối OpenAI.

## Thuật ngữ quan trọng

Kỹ thuật Đề bài: Thực hành thiết kế và tinh chỉnh đầu vào để hướng dẫn các mô hình AI tạo ra kết quả mong muốn.
Phân tách token: Quá trình chuyển đổi văn bản thành các đơn vị nhỏ hơn, gọi là token, mà mô hình có thể hiểu và xử lý.
LLM được tinh chỉnh theo chỉ dẫn: Các Mô hình Ngôn ngữ Lớn (LLM) được tinh chỉnh thêm với các chỉ dẫn cụ thể nhằm cải thiện độ chính xác và sự phù hợp trong phản hồi.

## Môi trường học tập sandbox

Kỹ thuật đề bài hiện nay là nghệ thuật nhiều hơn khoa học. Cách tốt nhất để cải thiện trực giác cho nó là _luyện tập nhiều hơn_ và áp dụng phương pháp thử - sai kết hợp chuyên môn lĩnh vực ứng dụng với các kỹ thuật được khuyến nghị và tối ưu hóa đặc thù cho từng mô hình.

Jupyter Notebook đi cùng bài học này cung cấp một môi trường _sandbox_ nơi bạn có thể thử nghiệm những gì học được - khi đi hoặc như một phần của thử thách mã ở cuối. Để thực hiện các bài tập, bạn sẽ cần:

1. **Khóa API Azure OpenAI** - điểm cuối dịch vụ cho một LLM được triển khai.
2. **Môi trường chạy Python** - trong đó Notebook có thể được thực thi.
3. **Biến môi trường cục bộ** - _hoàn thành các bước [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ngay bây giờ để chuẩn bị_.

Notebook kèm theo các bài tập _khởi động_ - nhưng bạn được khuyến khích thêm các phần _Markdown_ (mô tả) và _Code_ (yêu cầu đề bài) của riêng bạn để thử nhiều ví dụ hoặc ý tưởng hơn - và xây dựng trực giác thiết kế đề bài.

## Hướng dẫn có minh họa

Muốn có cái nhìn tổng quát về những gì bài học này đề cập trước khi bắt đầu? Hãy xem hướng dẫn minh họa này, nó giúp bạn nhận thức về các chủ đề chính và các điểm quan trọng để suy nghĩ trong mỗi phần. Lộ trình bài học dẫn bạn từ việc hiểu các khái niệm cốt lõi và thách thức đến cách giải quyết chúng với kỹ thuật và thực hành đề bài phù hợp. Lưu ý phần "Kỹ thuật nâng cao" trong hướng dẫn này tham khảo nội dung trong chương _tiếp theo_ của chương trình.

![Hướng dẫn có minh họa về Kỹ thuật Đề bài](../../../translated_images/vi/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Khởi nghiệp của chúng ta

Bây giờ, hãy nói về cách _chủ đề này_ liên quan đến sứ mệnh khởi nghiệp của chúng ta nhằm [đem đổi mới AI đến giáo dục](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chúng ta muốn xây dựng các ứng dụng AI hỗ trợ _học tập cá nhân hóa_ - vậy hãy nghĩ về cách các người dùng khác nhau của ứng dụng của chúng ta có thể "thiết kế" đề bài:

- **Nhà quản trị** có thể yêu cầu AI _phân tích dữ liệu giáo trình để xác định các khoảng trống trong bao phủ_. AI có thể tóm tắt kết quả hoặc trực quan hóa chúng bằng mã.
- **Giáo viên** có thể yêu cầu AI _tạo kế hoạch bài học cho nhóm đối tượng và chủ đề mục tiêu_. AI có thể xây dựng kế hoạch cá nhân hóa theo định dạng được chỉ định.
- **Học sinh** có thể yêu cầu AI _dạy kèm họ trong một môn học khó khăn_. AI giờ đây có thể hướng dẫn học sinh bằng các bài học, gợi ý & ví dụ phù hợp với trình độ của họ.

Đó chỉ là phần nổi của tảng băng trôi. Hãy xem [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - thư viện đề bài mã nguồn mở được các chuyên gia giáo dục tuyển chọn - để có cảm nhận rộng hơn về các khả năng! _Hãy thử chạy một số đề bài đó trong sandbox hoặc dùng OpenAI Playground xem điều gì xảy ra!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Kỹ thuật Đề bài là gì?

Chúng ta đã bắt đầu bài học này bằng cách định nghĩa **Kỹ thuật Đề bài** là quá trình _thiết kế và tối ưu hóa_ đầu vào văn bản (đề bài) để cung cấp các phản hồi (hoàn thành) nhất quán và chất lượng cho một mục tiêu ứng dụng và mô hình cụ thể. Có thể coi đây là một quá trình hai bước:

- _thiết kế_ đề bài ban đầu cho mô hình và mục tiêu cho trước
- _tinh chỉnh_ đề bài lặp đi lặp lại để cải thiện chất lượng phản hồi

Đây nhất thiết là một quy trình thử - sai đòi hỏi trực giác và nỗ lực của người dùng để có kết quả tối ưu. Vậy tại sao nó quan trọng? Để trả lời câu hỏi đó, đầu tiên chúng ta cần hiểu ba khái niệm:

- _Phân tách token_ = cách mô hình "nhìn thấy" đề bài
- _Base LLM_ = cách mô hình nền tảng "xử lý" đề bài
- _Instruction-Tuned LLM_ = cách mô hình hiện nay có thể nhận biết "nhiệm vụ"

### Phân tách token

Một LLM xem các đề bài như _chuỗi các token_ trong đó các mô hình khác nhau (hoặc các phiên bản của cùng một mô hình) có thể phân tách cùng một đề bài theo những cách khác nhau. Vì LLM được huấn luyện trên các token (không phải trên văn bản thô), cách đề bài được phân tách token ảnh hưởng trực tiếp đến chất lượng của phản hồi sinh ra.

Để có trực giác về cách phân tách token hoạt động, hãy thử các công cụ như [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) minh họa bên dưới. Dán đề bài của bạn vào - và xem nó được chuyển đổi thành token thế nào, chú ý cách xử lý các ký tự khoảng trắng và dấu câu. Lưu ý ví dụ này hiển thị một LLM cũ hơn (GPT-3) - nên thử với mô hình mới hơn có thể cho kết quả khác.

![Phân tách token](../../../translated_images/vi/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Khái niệm: Mô hình nền tảng

Sau khi đề bài được phân tách token, chức năng chính của ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (hoặc mô hình nền tảng) là dự đoán token tiếp theo trong chuỗi đó. Vì LLM được huấn luyện trên dữ liệu văn bản khổng lồ, chúng có đánh giá khá tốt về các mối quan hệ thống kê giữa các token và có thể dự đoán đó với một mức độ chắc chắn. Lưu ý chúng không hiểu _ý nghĩa_ của các từ trong đề bài hay token; chúng chỉ nhìn thấy mẫu mà có thể "hoàn thành" bằng dự đoán tiếp theo. Chúng có thể tiếp tục dự đoán chuỗi cho đến khi bị người dùng hoặc điều kiện đã đặt trước dừng lại.

Muốn xem cách hoàn thành dựa trên đề bài hoạt động thế nào? Hãy nhập đề bài ở trên vào [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) với cài đặt mặc định. Hệ thống được cấu hình để coi đề bài là yêu cầu thông tin - nên bạn sẽ thấy phản hồi phù hợp với ngữ cảnh này.

Nhưng nếu người dùng muốn thấy điều gì đó cụ thể đáp ứng một số tiêu chí hay mục tiêu nhiệm vụ? Đây là lúc các LLM _được tinh chỉnh theo chỉ dẫn_ xuất hiện.

![Hoàn thành chat LLM nền tảng](../../../translated_images/vi/04-playground-chat-base.65b76fcfde0caa67.webp)

### Khái niệm: LLM được tinh chỉnh theo chỉ dẫn

Một [LLM được tinh chỉnh theo chỉ dẫn](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bắt đầu với mô hình nền tảng rồi tinh chỉnh thêm với các ví dụ hoặc các cặp đầu vào/đầu ra (ví dụ: các "tin nhắn" nhiều lượt) có thể chứa các chỉ dẫn rõ ràng - và phản hồi từ AI cố gắng tuân theo chỉ dẫn đó.

Điều này sử dụng kỹ thuật như Học củng cố với Phản hồi của Con người (RLHF) giúp mô hình _theo chỉ dẫn_ và _học từ phản hồi_ để tạo ra phản hồi phù hợp hơn với ứng dụng thực tế và sát với mục tiêu người dùng hơn.

Hãy thử - quay lại đề bài bên trên, nhưng giờ thay đổi _tin nhắn hệ thống_ để cung cấp chỉ dẫn sau làm ngữ cảnh:

> _Tóm tắt nội dung bạn được cung cấp cho học sinh lớp hai. Giữ kết quả trong một đoạn văn với 3-5 gạch đầu dòng._

Thấy không, kết quả giờ được tinh chỉnh để phản ánh mục tiêu và định dạng mong muốn? Một giáo viên có thể trực tiếp dùng phản hồi này trong bài giảng của họ cho lớp đó.

![Hoàn thành chat LLM tinh chỉnh chỉ dẫn](../../../translated_images/vi/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Tại sao chúng ta cần Kỹ thuật Đề bài?

Giờ chúng ta đã biết đề bài được LLM xử lý thế nào, hãy nói về _tại sao_ chúng ta cần kỹ thuật đề bài. Câu trả lời nằm ở chỗ các LLM hiện tại đặt ra nhiều thử thách khiến việc đạt được các phản hồi _đáng tin cậy và nhất quán_ trở nên khó hơn nếu không đầu tư công sức xây dựng và tối ưu đề bài. Ví dụ:

1. **Phản hồi của mô hình mang tính ngẫu nhiên.** _Đề bài giống nhau_ có thể cho ra những phản hồi khác nhau với các mô hình hoặc phiên bản mô hình khác nhau. Và nó có thể cho ra kết quả khác ngay cả với _cùng một mô hình_ vào các thời điểm khác nhau. _Kỹ thuật đề bài có thể giúp giảm thiểu các biến động này bằng cách cung cấp các hướng dẫn tốt hơn_.

1. **Mô hình có thể sáng tạo ra phản hồi.** Mô hình được huấn luyện trên bộ dữ liệu _lớn nhưng hữu hạn_, nghĩa là chúng thiếu kiến thức về các khái niệm ngoài phạm vi huấn luyện đó. Kết quả là chúng có thể tạo ra các phản hồi không chính xác, tưởng tượng hoặc thậm chí trái ngược trực tiếp với các sự thật đã biết. _Kỹ thuật đề bài giúp người dùng phát hiện và giảm thiểu các sáng tạo như vậy ví dụ: bằng cách yêu cầu AI dẫn nguồn hoặc luận lý_.

1. **Khả năng mô hình sẽ thay đổi.** Các mô hình mới hơn hay thế hệ mô hình tiếp theo sẽ có khả năng phong phú hơn nhưng cũng mang theo những đặc điểm riêng biệt và đánh đổi về chi phí & độ phức tạp. _Kỹ thuật đề bài có thể giúp phát triển các thực hành và quy trình làm việc tốt nhất để trừu tượng hóa các khác biệt và thích ứng với yêu cầu đặc thù từng mô hình một cách mở rộng và liền mạch_.

Hãy xem điều này hoạt động trong OpenAI hoặc Azure OpenAI Playground:

- Dùng cùng một đề bài với các triển khai LLM khác nhau (ví dụ OpenAI, Azure OpenAI, Hugging Face) - bạn có thấy sự biến đổi không?
- Dùng cùng một đề bài lặp đi lặp lại với _cùng_ một triển khai LLM (ví dụ Azure OpenAI playground) - các khác biệt đó khác thế nào?

### Ví dụ về sáng tạo sai sự thật

Trong khóa học này, chúng tôi dùng thuật ngữ **"sáng tạo sai sự thật"** để chỉ hiện tượng LLM đôi khi tạo ra thông tin sai sự thật do giới hạn trong huấn luyện hoặc các ràng buộc khác. Bạn có thể đã nghe gọi nó là _"ảo giác"_ trong các bài báo phổ biến hoặc nghiên cứu. Tuy nhiên, chúng tôi khuyến nghị dùng _"sáng tạo sai sự thật"_ làm thuật ngữ để tránh nhân hóa hành vi bằng cách gán đặc tính con người cho kết quả do máy tạo ra. Điều này cũng củng cố các [hướng dẫn AI có trách nhiệm](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) về mặt thuật ngữ, loại bỏ các từ có thể bị coi là xúc phạm hay không bao quát trong một số bối cảnh.

Muốn hiểu cách sáng tạo sai sự thật hoạt động? Hãy nghĩ về đề bài yêu cầu AI tạo nội dung cho một chủ đề không tồn tại (để chắc chắn nó không có trong bộ dữ liệu huấn luyện). Ví dụ - tôi thử đề bài:

> **Đề bài:** tạo kế hoạch bài học về Chiến tranh Sao Hỏa năm 2076.

Tìm kiếm trên web cho thấy có các tác phẩm hư cấu (ví dụ: phim truyền hình hoặc sách) về các cuộc chiến trên Sao Hỏa - nhưng không có cuộc chiến nào năm 2076. Lẽ thường cũng chỉ ra rằng 2076 là _tương lai_ nên không thể liên quan đến một sự kiện có thật.


Vậy chuyện gì sẽ xảy ra khi chúng ta chạy prompt này với các nhà cung cấp LLM khác nhau?

> **Phản hồi 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/vi/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Phản hồi 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/vi/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Phản hồi 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/vi/04-fabrication-huggingchat.faf82a0a51278956.webp)

Như dự đoán, mỗi mô hình (hoặc phiên bản mô hình) tạo ra phản hồi hơi khác nhau nhờ vào hành vi ngẫu nhiên và sự khác biệt về khả năng mô hình. Ví dụ, một mô hình hướng đến đối tượng học sinh lớp 8 trong khi mô hình khác giả định người dùng là học sinh trung học phổ thông. Nhưng cả ba mô hình đều tạo ra phản hồi có thể thuyết phục người dùng không biết gì rằng sự kiện là thật.

Các kỹ thuật kỹ thuật prompt như _metaprompting_ và _cấu hình nhiệt độ_ có thể giảm bớt sự bịa đặt của mô hình đến một mức độ nhất định. Các _kiến trúc_ kỹ thuật prompt mới cũng tích hợp liền mạch các công cụ và kỹ thuật mới vào luồng prompt, nhằm giảm thiểu hoặc hạn chế một số hiệu ứng này.

## Nghiên cứu trường hợp: GitHub Copilot

Hãy kết thúc phần này bằng cách cảm nhận cách kỹ thuật prompt được sử dụng trong các giải pháp thực tế bằng cách xem một nghiên cứu trường hợp: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot là "bạn đồng hành lập trình AI" của bạn - nó chuyển các prompt văn bản thành các đoạn mã hoàn chỉnh và được tích hợp trong môi trường phát triển của bạn (ví dụ, Visual Studio Code) để có trải nghiệm người dùng liền mạch. Như được ghi lại trong chuỗi blog dưới đây, phiên bản đầu tiên dựa trên mô hình OpenAI Codex - với các kỹ sư nhanh chóng nhận thấy cần tinh chỉnh mô hình và phát triển các kỹ thuật kỹ thuật prompt tốt hơn, để nâng cao chất lượng mã. Vào tháng 7, họ [giới thiệu mô hình AI cải tiến vượt ra ngoài Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) để đưa ra đề xuất nhanh hơn.

Đọc các bài viết theo thứ tự, để theo dõi hành trình học hỏi của họ.

- **Tháng 5 năm 2023** | [GitHub Copilot ngày càng hiểu mã của bạn tốt hơn](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Tháng 5 năm 2023** | [Bên trong GitHub: Làm việc với các LLM phía sau GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Tháng 6 năm 2023** | [Cách viết prompt tốt hơn cho GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Tháng 7 năm 2023** | [.. GitHub Copilot vượt ra ngoài Codex với mô hình AI cải tiến](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Tháng 7 năm 2023** | [Hướng dẫn dành cho nhà phát triển về prompt engineering và LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Tháng 9 năm 2023** | [Cách xây dựng ứng dụng LLM doanh nghiệp: Bài học từ GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Bạn cũng có thể duyệt [blog Kỹ thuật](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) của họ để xem thêm các bài viết như [bài này](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) thể hiện cách các mô hình và kỹ thuật này được _áp dụng_ để thúc đẩy các ứng dụng thực tế.

---

<!--
MẪU BÀI HỌC:
Đơn vị này nên bao gồm khái niệm cốt lõi #2.
Củng cố khái niệm bằng các ví dụ và tham khảo.

KHÁI NIỆM #2:
Thiết kế Prompt.
Minh họa bằng ví dụ.
-->

## Cấu trúc Prompt

Chúng ta đã thấy tại sao kỹ thuật prompt quan trọng - giờ hãy hiểu cách các prompt được _xây dựng_ để chúng ta có thể đánh giá các kỹ thuật khác nhau nhằm thiết kế prompt hiệu quả hơn.

### Prompt cơ bản

Hãy bắt đầu với prompt cơ bản: một đầu vào văn bản gửi tới mô hình mà không kèm bất kỳ bối cảnh nào khác. Đây là một ví dụ - khi chúng ta gửi vài từ đầu tiên của quốc ca Hoa Kỳ đến OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), nó ngay lập tức _hoàn thành_ phản hồi với vài câu tiếp theo, minh họa hành vi dự đoán cơ bản.

| Prompt (Đầu vào)     | Hoàn thành (Đầu ra)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Nó nghe như bạn đang bắt đầu lời bài hát "The Star-Spangled Banner," quốc ca của Hoa Kỳ. Lời bài hát đầy đủ là ...                       |

### Prompt phức tạp

Bây giờ hãy thêm bối cảnh và hướng dẫn vào prompt cơ bản đó. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) cho phép chúng ta xây dựng prompt phức tạp như một tập hợp các _tin nhắn_ với:

- Các cặp đầu vào/đầu ra phản ánh đầu vào của _người dùng_ và phản hồi của _trợ lý_.
- Tin nhắn hệ thống thiết lập bối cảnh cho hành vi hoặc cá tính của trợ lý.

Yêu cầu giờ ở dạng dưới đây, trong đó _tokenization_ nắm bắt hiệu quả thông tin liên quan từ bối cảnh và cuộc trò chuyện. Bây giờ, thay đổi bối cảnh hệ thống có thể tác động mạnh đến chất lượng kết quả hoàn thành như chính các đầu vào người dùng cung cấp.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt chỉ dẫn

Trong các ví dụ trên, prompt người dùng là một truy vấn văn bản đơn giản có thể được hiểu là yêu cầu thông tin. Với prompt _chỉ dẫn_, chúng ta có thể dùng văn bản đó để chỉ định một nhiệm vụ chi tiết hơn, cung cấp hướng dẫn tốt hơn cho AI. Đây là ví dụ:

| Prompt (Đầu vào)                                                                                                                                                                                                                         | Hoàn thành (Đầu ra)                                                                                                        | Loại chỉ dẫn      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Viết mô tả về Nội chiến Hoa Kỳ                                                                                                                                                                                                        | _trả về một đoạn văn đơn giản_                                                                                            | Đơn giản            |
| Viết mô tả về Nội chiến Hoa Kỳ. Cung cấp các ngày tháng và sự kiện chính và mô tả tầm quan trọng của chúng                                                                                                                            | _trả về đoạn văn theo sau là danh sách các ngày quan trọng có mô tả_                                                       | Phức tạp            |
| Viết mô tả về Nội chiến Hoa Kỳ trong 1 đoạn văn. Cung cấp 3 gạch đầu dòng với các ngày quan trọng và ý nghĩa của chúng. Cung cấp 3 gạch đầu dòng nữa với các nhân vật lịch sử cùng đóng góp của họ. Trả đầu ra dưới dạng file JSON | _trả về chi tiết mở rộng hơn trong khung văn bản, định dạng JSON để bạn có thể sao chép dán vào file và kiểm tra khi cần_ | Phức tạp. Có định dạng. |

## Nội dung chính

Trong các ví dụ trên, prompt vẫn khá mở, cho phép LLM quyết định phần nào của tập dữ liệu được huấn luyện sẵn là liên quan. Với mẫu thiết kế _nội dung chính_, văn bản đầu vào được chia thành hai phần:

- một chỉ dẫn (hành động)
- nội dung liên quan (ảnh hưởng tới hành động)

Đây là ví dụ trong đó chỉ dẫn là "tóm tắt điều này trong 2 câu".

| Prompt (Đầu vào)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Hoàn thành (Đầu ra)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sao Mộc là hành tinh thứ năm tính từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. Nó là một hành tinh khí khổng lồ có khối lượng bằng một phần nghìn Mặt Trời, nhưng gấp hai lần rưỡi tổng khối lượng các hành tinh khác trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn thấy bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi có ghi chép lịch sử. Nó được đặt theo tên vị thần Sao Mộc của La Mã.[19] Khi nhìn từ Trái Đất, Sao Mộc có thể đủ sáng để ánh sáng phản chiếu của nó tạo ra bóng nhìn thấy được,[20] và trung bình là vật thể tự nhiên sáng thứ ba trên bầu trời đêm sau Mặt Trăng và Sao Kim. <br/> **Tóm tắt điều này trong 2 câu ngắn** | Sao Mộc, hành tinh thứ năm tính từ Mặt Trời, là hành tinh lớn nhất trong Hệ Mặt Trời và được biết đến là một trong những vật thể sáng nhất trên bầu trời đêm. Được đặt theo tên vị thần La Mã Sao Mộc, đây là hành tinh khí có khối lượng gấp hai lần rưỡi tổng khối lượng tất cả các hành tinh khác cộng lại trong Hệ Mặt Trời. |

Đoạn nội dung chính có thể được sử dụng theo nhiều cách để thúc đẩy các chỉ dẫn hiệu quả hơn:

- **Ví dụ** - thay vì chỉ bảo mô hình làm gì bằng một chỉ dẫn rõ ràng, hãy đưa ví dụ về việc cần làm và để mô hình suy luận mẫu.
- **Gợi ý** - theo sau chỉ dẫn bằng một "gợi ý" nhằm kích thích kết quả, hướng mô hình tới các phản hồi liên quan hơn.
- **Mẫu** - đây là 'công thức' lặp lại cho các prompt với chỗ trống (biến) có thể tùy chỉnh với dữ liệu cho các trường hợp sử dụng cụ thể.

Hãy khám phá các cách này trong thực hành.

### Sử dụng ví dụ

Đây là cách tiếp cận bạn dùng nội dung chính để "cung cấp cho mô hình" vài ví dụ về kết quả mong muốn cho chỉ dẫn cho trước, và để mô hình suy luận mẫu kết quả mong muốn. Dựa vào số lượng ví dụ đưa ra, chúng ta có thể có prompting không ví dụ, prompting một ví dụ, prompting vài ví dụ, v.v.

Prompt giờ gồm ba thành phần:

- Mô tả nhiệm vụ
- Một vài ví dụ về kết quả mong muốn
- Bắt đầu ví dụ mới (trở thành mô tả nhiệm vụ ngầm định)

| Loại học | Prompt (Đầu vào)                                                                                                                                        | Hoàn thành (Đầu ra)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Không ví dụ   | "Mặt Trời đang chiếu sáng". Dịch sang tiếng Tây Ban Nha                                                                                              | "El Sol está brillando".    |
| Một ví dụ    | "Mặt Trời đang chiếu sáng" => ""El Sol está brillando". <br> "Ngày trời lạnh và nhiều gió" =>                                                         | "Es un día frío y ventoso". |
| Vài ví dụ    | Người chơi chạy các căn cứ => Bóng chày <br/> Người chơi đánh ace => Quần vợt <br/> Người chơi đánh six => Cricket <br/> Người chơi ghi slam-dunk =>       | Bóng rổ                     |
|               |                                                                                                                                                       |                             |

Lưu ý cách chúng ta phải cung cấp chỉ dẫn rõ ràng ("Dịch sang tiếng Tây Ban Nha") trong prompting không ví dụ, nhưng nó được suy ra trong ví dụ một shot. Ví dụ vài shot cho thấy cách thêm ví dụ giúp mô hình suy luận chính xác hơn mà không cần chỉ dẫn thêm.

### Gợi ý prompt

Một kỹ thuật khác để sử dụng nội dung chính là cung cấp _gợi ý_ thay vì ví dụ. Trong trường hợp này, chúng ta cho mô hình một lời nhắc theo hướng đúng bằng cách _bắt đầu nó_ với một đoạn mẫu phản ánh định dạng kết quả mong muốn. Sau đó mô hình "nhận gợi ý" và tiếp tục theo hướng đó.

| Số gợi ý | Prompt (Đầu vào)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Hoàn thành (Đầu ra)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Sao Mộc là hành tinh thứ năm tính từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. Nó là hành tinh khí khổng lồ có khối lượng bằng một phần nghìn Mặt Trời, nhưng nặng gấp hai lần rưỡi tổng khối lượng các hành tinh còn lại trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi lịch sử ghi chép.<br/>**Tóm tắt điều này**                                       | Sao Mộc là hành tinh lớn nhất trong Hệ Mặt Trời của chúng ta và là hành tinh thứ năm tính từ Mặt Trời. Nó là hành tinh khí có khối lượng bằng 1/1000 Mặt Trời, nhưng nặng hơn tổng khối lượng các hành tinh còn lại cộng lại. Các nền văn minh cổ đại biết đến Sao Mộc từ lâu, và nó dễ dàng nhìn thấy trên bầu trời đêm. |
| 1              | Sao Mộc là hành tinh thứ năm tính từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. Nó là hành tinh khí khổng lồ có khối lượng bằng một phần nghìn Mặt Trời, nhưng nặng gấp hai lần rưỡi tổng khối lượng các hành tinh còn lại trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi lịch sử ghi chép.<br/>**Tóm tắt điều này** <br/> Điều chúng ta học được là Sao Mộc | là hành tinh thứ năm tính từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. Nó là hành tinh khí có khối lượng bằng một phần nghìn Mặt Trời, nhưng nặng gấp hai lần rưỡi tổng khối lượng các hành tinh còn lại cộng lại. Nó dễ dàng nhìn thấy bằng mắt thường và đã được biết đến từ thời cổ đại.                        |

| 2              | Sao Mộc là hành tinh thứ năm từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. Nó là một hành tinh khí khổng lồ với khối lượng chỉ bằng một phần nghìn của Mặt Trời, nhưng lớn gấp hai lần rưỡi tổng khối lượng của tất cả các hành tinh khác trong Hệ Mặt Trời cộng lại. Sao Mộc là một trong những vật thể sáng nhất có thể nhìn thấy bằng mắt thường trên bầu trời đêm, và đã được các nền văn minh cổ đại biết đến từ trước khi có ghi chép lịch sử. <br/>**Tóm tắt nội dung** <br/> 3 sự thật hàng đầu chúng ta đã học:         | 1. Sao Mộc là hành tinh thứ năm từ Mặt Trời và là hành tinh lớn nhất trong Hệ Mặt Trời. <br/> 2. Nó là một hành tinh khí khổng lồ với khối lượng chỉ bằng một phần nghìn của Mặt Trời...<br/> 3. Sao Mộc có thể nhìn thấy bằng mắt thường từ thời cổ đại ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Mẫu nhắc

Mẫu nhắc là một _công thức được định nghĩa trước cho một lời nhắc_ có thể lưu trữ và tái sử dụng khi cần, nhằm tạo ra trải nghiệm người dùng nhất quán hơn ở quy mô lớn. Ở dạng đơn giản nhất, nó chỉ là một tập hợp các ví dụ nhắc như [ví dụ này từ OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) cung cấp cả các thành phần lời nhắc tương tác (tin nhắn người dùng và hệ thống) và định dạng yêu cầu qua API - hỗ trợ tái sử dụng.

Ở dạng phức tạp hơn như [ví dụ này từ LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) nó chứa các _chỗ giữ chỗ_ có thể được thay thế bằng dữ liệu từ nhiều nguồn khác nhau (đầu vào người dùng, ngữ cảnh hệ thống, nguồn dữ liệu bên ngoài, v.v.) để tạo ra lời nhắc một cách động. Điều này cho phép chúng ta tạo thư viện các lời nhắc có thể tái sử dụng để vận hành trải nghiệm người dùng một cách **chương trình hóa** ở quy mô lớn.

Cuối cùng, giá trị thực sự của các mẫu nằm ở khả năng tạo và xuất bản _thư viện lời nhắc_ cho các lĩnh vực ứng dụng chuyên biệt - trong đó mẫu lời nhắc được _tối ưu hóa_ để phản ánh bối cảnh hoặc ví dụ cụ thể của ứng dụng giúp các phản hồi trở nên phù hợp và chính xác hơn với đối tượng người dùng mục tiêu. Kho [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) là một ví dụ tuyệt vời về cách tiếp cận này, tập hợp thư viện lời nhắc cho lĩnh vực giáo dục với trọng tâm vào các mục tiêu chính như lập kế hoạch bài học, thiết kế chương trình giảng dạy, hướng dẫn học sinh, v.v.

## Nội dung hỗ trợ

Nếu ta nghĩ về việc xây dựng lời nhắc gồm một hướng dẫn (nhiệm vụ) và một mục tiêu (nội dung chính), thì _nội dung phụ_ giống như thông tin bổ sung giúp ta **ảnh hưởng đến đầu ra theo một cách nào đó**. Nó có thể là các tham số điều chỉnh, hướng dẫn định dạng, phân loại chủ đề, v.v. giúp mô hình _điều chỉnh_ phản hồi sao cho phù hợp với mục tiêu hoặc kỳ vọng người dùng.

Ví dụ: Với một danh mục khóa học có siêu dữ liệu chi tiết (tên, mô tả, cấp độ, thẻ meta, giảng viên, v.v.) của tất cả các khóa học có trong chương trình:

- chúng ta có thể đặt ra hướng dẫn là "tóm tắt danh mục khóa học cho Kỳ Thu 2023"
- chúng ta có thể dùng nội dung chính để cung cấp một vài ví dụ về đầu ra mong muốn
- chúng ta có thể dùng nội dung phụ để xác định 5 "thẻ" quan tâm hàng đầu.

Bây giờ, mô hình có thể cung cấp tóm tắt theo định dạng các ví dụ đã cho - nhưng nếu một kết quả có nhiều thẻ, nó có thể ưu tiên 5 thẻ đã được xác định trong nội dung phụ.

---

<!--
KHUÔN BÀI HỌC:
Đơn vị này nên bao gồm khái niệm cốt lõi #1.
Củng cố khái niệm bằng ví dụ và tham chiếu.

KHÁI NIỆM #3:
Kỹ thuật tạo lời nhắc.
Một số kỹ thuật cơ bản tạo lời nhắc là gì?
Minh họa bằng vài bài tập.
-->

## Thực hành tốt nhất khi tạo lời nhắc

Giờ chúng ta đã biết cách _xây dựng_ lời nhắc, ta có thể bắt đầu suy nghĩ về cách _thiết kế_ chúng theo các thực hành tốt nhất. Ta có thể chia làm hai phần - có _tư duy_ đúng và áp dụng _kỹ thuật_ phù hợp.

### Tư duy kỹ thuật tạo lời nhắc

Tạo lời nhắc là quá trình thử và sai, nên hãy nhớ ba yếu tố hướng dẫn rộng sau:

1. **Hiểu lĩnh vực quan trọng.** Độ chính xác và phù hợp của phản hồi là hàm số của _lĩnh vực_ mà ứng dụng hoặc người dùng hoạt động. Áp dụng trực giác và chuyên môn lĩnh vực để **tùy chỉnh kỹ thuật** thêm. Ví dụ, định nghĩa _tính cách đặc thù lĩnh vực_ trong lời nhắc hệ thống, hoặc dùng _mẫu đặc thù lĩnh vực_ trong lời nhắc người dùng. Cung cấp nội dung phụ phản ánh bối cảnh đặc thù lĩnh vực, hoặc dùng _dấu hiệu và ví dụ đặc thù lĩnh vực_ để hướng dẫn mô hình theo các mô hình sử dụng quen thuộc.

2. **Hiểu mô hình quan trọng.** Ta biết mô hình vốn dĩ có tính ngẫu nhiên. Nhưng các triển khai mô hình cũng khác nhau về bộ dữ liệu huấn luyện họ dùng (kiến thức tiền huấn luyện), khả năng họ cung cấp (ví dụ: qua API hoặc SDK) và loại nội dung họ tối ưu (ví dụ: mã lệnh so với hình ảnh so với văn bản). Hiểu điểm mạnh và hạn chế của mô hình bạn sử dụng, và dùng kiến thức đó để _ưu tiên nhiệm vụ_ hoặc xây dựng _mẫu tùy chỉnh_ tối ưu cho khả năng của mô hình.

3. **Lặp lại & xác thực quan trọng.** Mô hình phát triển nhanh, kỹ thuật tạo lời nhắc cũng vậy. Là chuyên gia lĩnh vực, bạn có thể có bối cảnh hoặc tiêu chí khác cho _ứng dụng_ cụ thể của bạn, mà có thể không áp dụng cho cộng đồng rộng hơn. Dùng công cụ và kỹ thuật tạo lời nhắc để "khởi động nhanh" việc xây dựng lời nhắc, rồi lặp lại và xác thực kết quả dựa trên trực giác và chuyên môn lĩnh vực của bạn. Ghi lại hiểu biết và tạo **cơ sở tri thức** (ví dụ, thư viện lời nhắc) để dùng làm nền tảng mới cho người khác, giúp các vòng lặp trong tương lai nhanh hơn.

## Thực hành tốt nhất

Bây giờ hãy xem các thực hành tốt nhất thông thường được các chuyên gia [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) và [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) đề xuất.

| Việc làm                         | Lý do                                                                                                                                                                                                                                           |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đánh giá các mô hình mới nhất    | Các thế hệ mô hình mới có thể có tính năng và chất lượng cải tiến - nhưng cũng có thể phát sinh chi phí cao hơn. Đánh giá tác động, sau đó quyết định liệu có nên chuyển đổi hay không.                                                         |
| Tách biệt hướng dẫn & ngữ cảnh   | Kiểm tra xem mô hình/nhà cung cấp của bạn có định nghĩa _dấu phân cách_ để phân biệt rõ hướng dẫn, nội dung chính và nội dung phụ không. Điều này giúp mô hình gán trọng số chính xác hơn cho các token.                                       |
| Cụ thể và rõ ràng                | Cung cấp chi tiết về ngữ cảnh mong muốn, kết quả, độ dài, định dạng, phong cách, v.v. Điều này cải thiện chất lượng và sự nhất quán của phản hồi. Ghi lại công thức trong các mẫu có thể tái sử dụng.                                            |
| Miêu tả kỹ, dùng ví dụ           | Mô hình có thể phản hồi tốt hơn với cách "trình bày và giải thích". Bắt đầu với phương pháp `zero-shot` nơi bạn chỉ cho nó hướng dẫn (không có ví dụ), sau đó thử `few-shot` để tinh chỉnh, cung cấp một vài ví dụ về đầu ra mong muốn. Dùng phép so sánh. |
| Dùng dấu hiệu để khởi động câu hoàn thành | Đẩy nó về phía kết quả mong muốn bằng cách cung cấp từ hoặc cụm từ dẫn đầu để nó có thể sử dụng làm điểm bắt đầu cho phản hồi.                                                                                                             |
| Lặp lại                          | Đôi khi bạn cần nhắc lại với mô hình. Cho chỉ dẫn trước và sau nội dung chính, dùng hướng dẫn và dấu hiệu, v.v. Lặp lại và kiểm tra xem cách nào hiệu quả.                                                                                     |
| Trình tự quan trọng               | Thứ tự bạn trình bày thông tin cho mô hình có thể ảnh hưởng đến kết quả, ngay cả trong các ví dụ học, nhờ sự ưu tiên gần nhất. Thử các tùy chọn khác nhau để xem cách nào hiệu quả nhất.                                                      |
| Cho mô hình “lối thoát”           | Cung cấp cho mô hình phản hồi _dự phòng_ để nó có thể sử dụng nếu không thể hoàn thành nhiệm vụ vì lý do nào đó. Điều này giảm khả năng mô hình tạo ra phản hồi sai hoặc giả mạo.                                                             |
|                                   |                                                                                                                                                                                                                                                 |

Như với mọi thực hành tốt nhất, hãy nhớ rằng _kết quả của bạn có thể khác_ tùy thuộc mô hình, nhiệm vụ và lĩnh vực. Dùng đây làm điểm khởi đầu, và lặp lại để tìm ra cách phù hợp nhất cho bạn. Luôn đánh giá lại quy trình tạo lời nhắc khi có mô hình và công cụ mới, tập trung vào khả năng mở rộng quy trình và chất lượng phản hồi.

<!--
KHUÔN BÀI HỌC:
Đơn vị này nên cung cấp một thử thách mã nếu có thể

THỬ THÁCH:
Liên kết tới một Jupyter Notebook chỉ có các bình luận mã trong phần hướng dẫn (phần mã trống).

GIẢI PHÁP:
Liên kết tới một bản sao của Notebook đó với các lời nhắc đã được điền và chạy, cho thấy một ví dụ có thể.
-->

## Bài tập

Chúc mừng! Bạn đã đến cuối bài học! Đã đến lúc thử nghiệm một số khái niệm và kỹ thuật với các ví dụ thực tế!

Với bài tập của chúng ta, ta sẽ dùng một Jupyter Notebook với các bài tập bạn có thể hoàn thành tương tác. Bạn cũng có thể mở rộng Notebook với các ô Markdown và Mã của riêng bạn để khám phá ý tưởng và kỹ thuật.

### Để bắt đầu, fork repo, sau đó

- (Khuyên dùng) Khởi chạy GitHub Codespaces
- (Ngoài ra) Sao chép repo về thiết bị của bạn và dùng với Docker Desktop
- (Ngoài ra) Mở Notebook với môi trường chạy Notebook theo lựa chọn.

### Tiếp theo, cấu hình biến môi trường

- Sao chép file `.env.copy` trong thư mục gốc repo thành `.env` và điền các giá trị `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` và `AZURE_OPENAI_DEPLOYMENT`. Quay lại phần [Learning Sandbox](#môi-trường-học-tập-sandbox) để học cách làm.

### Tiếp theo, mở Jupyter Notebook

- Chọn kernel thực thi. Nếu dùng tùy chọn 1 hoặc 2, chỉ cần chọn kernel Python 3.10.x mặc định được cung cấp trong container phát triển.

Bạn đã sẵn sàng chạy các bài tập. Lưu ý không có câu trả lời _đúng hay sai_ ở đây - chỉ là khám phá các lựa chọn bằng phương pháp thử và sai, và xây dựng trực giác về điều gì hiệu quả với mô hình và lĩnh vực ứng dụng.

_Vì lý do này nên bài học không có phần Giải pháp Mã. Thay vào đó, Notebook sẽ có các ô Markdown đề tên "Giải pháp của tôi:" trình bày một ví dụ đầu ra tham khảo._

 <!--
KHUÔN BÀI HỌC:
Bao quanh phần này bằng tóm tắt và tài nguyên học tập tự hướng dẫn.
-->

## Kiểm tra kiến thức

Câu hỏi nào sau đây là lời nhắc tốt theo một số thực hành tốt hợp lý?

1. Cho tôi xem hình ảnh một chiếc xe hơi màu đỏ
2. Cho tôi xem hình ảnh một chiếc xe hơi màu đỏ hiệu Volvo và mẫu XC90 đậu gần vách đá với mặt trời lặn
3. Cho tôi xem hình ảnh một chiếc xe hơi màu đỏ hiệu Volvo và mẫu XC90

A: 2, là lời nhắc tốt nhất vì nó cung cấp chi tiết về "cái gì" và đi vào cụ thể (không chỉ là chiếc xe nào mà là hiệu và mẫu cụ thể) và cũng mô tả bối cảnh chung. 3 xếp thứ hai vì cũng chứa nhiều mô tả.

## 🚀 Thử thách

Thử dùng kỹ thuật "dấu hiệu" với lời nhắc: Hoàn thành câu "Cho tôi xem hình ảnh một chiếc xe hơi màu đỏ hiệu Volvo và ". Nó trả lời như thế nào, và bạn sẽ cải thiện sao?

## Chúc mừng! Tiếp tục học

Muốn học thêm về các khái niệm Kỹ thuật tạo lời nhắc? Đến trang [học tiếp](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tìm các tài nguyên tuyệt vời khác về chủ đề này.

Hãy đến Bài học 5 nơi chúng ta sẽ tìm hiểu [kỹ thuật tạo lời nhắc nâng cao](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->