<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:56:31+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "vi"
}
-->
# Kiến thức cơ bản về Prompt Engineering

## Giới thiệu
Module này bao gồm các khái niệm và kỹ thuật cần thiết để tạo ra các prompt hiệu quả trong mô hình AI tạo sinh. Cách bạn viết prompt cho một LLM cũng rất quan trọng. Một prompt được tạo ra cẩn thận có thể đạt được chất lượng phản hồi tốt hơn. Nhưng chính xác thì các thuật ngữ như _prompt_ và _prompt engineering_ có nghĩa là gì? Và làm thế nào để cải thiện _đầu vào_ prompt mà tôi gửi cho LLM? Đây là những câu hỏi chúng ta sẽ cố gắng trả lời trong chương này và chương tiếp theo.

AI tạo sinh có khả năng tạo nội dung mới (ví dụ: văn bản, hình ảnh, âm thanh, mã, v.v.) để đáp ứng yêu cầu của người dùng. Nó đạt được điều này bằng cách sử dụng _Các mô hình ngôn ngữ lớn_ như dòng GPT ("Generative Pre-trained Transformer") của OpenAI, được đào tạo để sử dụng ngôn ngữ tự nhiên và mã.

Người dùng hiện có thể tương tác với các mô hình này bằng các cách quen thuộc như trò chuyện, mà không cần bất kỳ chuyên môn kỹ thuật hay đào tạo nào. Các mô hình này dựa trên _prompt_ - người dùng gửi một đầu vào văn bản (prompt) và nhận lại phản hồi AI (completion). Sau đó, họ có thể "trò chuyện với AI" theo cách lặp đi lặp lại, trong các cuộc trò chuyện nhiều lượt, tinh chỉnh prompt của mình cho đến khi phản hồi khớp với mong đợi của họ.

"Prompts" hiện trở thành _giao diện lập trình_ chính cho các ứng dụng AI tạo sinh, chỉ đạo các mô hình phải làm gì và ảnh hưởng đến chất lượng của các phản hồi trả về. "Prompt Engineering" là một lĩnh vực nghiên cứu đang phát triển nhanh chóng, tập trung vào _thiết kế và tối ưu hóa_ các prompt để cung cấp phản hồi nhất quán và chất lượng ở quy mô lớn.

## Mục tiêu học tập

Trong bài học này, chúng ta sẽ tìm hiểu Prompt Engineering là gì, tại sao nó quan trọng, và cách chúng ta có thể tạo ra các prompt hiệu quả hơn cho một mô hình và mục tiêu ứng dụng cụ thể. Chúng ta sẽ hiểu các khái niệm cốt lõi và các thực hành tốt nhất cho prompt engineering - và tìm hiểu về môi trường "sandbox" Jupyter Notebooks tương tác nơi chúng ta có thể thấy các khái niệm này được áp dụng vào các ví dụ thực tế.

Cuối bài học này, chúng ta sẽ có thể:

1. Giải thích Prompt Engineering là gì và tại sao nó quan trọng.
2. Mô tả các thành phần của một prompt và cách chúng được sử dụng.
3. Học các thực hành tốt nhất và kỹ thuật cho prompt engineering.
4. Áp dụng các kỹ thuật đã học vào các ví dụ thực tế, sử dụng một điểm cuối OpenAI.

## Thuật ngữ chính

Prompt Engineering: Thực hành thiết kế và tinh chỉnh đầu vào để hướng dẫn các mô hình AI tạo ra đầu ra mong muốn.
Tokenization: Quá trình chuyển đổi văn bản thành các đơn vị nhỏ hơn, gọi là token, mà mô hình có thể hiểu và xử lý.
Instruction-Tuned LLMs: Các mô hình ngôn ngữ lớn (LLMs) đã được tinh chỉnh với các hướng dẫn cụ thể để cải thiện độ chính xác và sự liên quan của phản hồi.

## Sandbox học tập

Prompt engineering hiện nay thiên về nghệ thuật hơn là khoa học. Cách tốt nhất để cải thiện trực giác của chúng ta về nó là _thực hành nhiều hơn_ và áp dụng phương pháp thử và sai kết hợp với kiến thức chuyên môn về lĩnh vực ứng dụng cùng với các kỹ thuật được khuyến nghị và tối ưu hóa mô hình cụ thể.

Jupyter Notebook đi kèm với bài học này cung cấp một môi trường _sandbox_ nơi bạn có thể thử những gì bạn học - khi bạn đi hoặc như một phần của thử thách mã ở cuối. Để thực hiện các bài tập, bạn sẽ cần:

1. **Một khóa API Azure OpenAI** - điểm cuối dịch vụ cho một LLM đã triển khai.
2. **Một môi trường Python** - nơi Notebook có thể được thực thi.
3. **Các biến môi trường cục bộ** - _hoàn thành các bước [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) ngay bây giờ để sẵn sàng_.

Notebook đi kèm với các bài tập _khởi đầu_ - nhưng bạn được khuyến khích thêm các phần _Markdown_ (mô tả) và _Code_ (yêu cầu prompt) của riêng mình để thử thêm các ví dụ hoặc ý tưởng - và xây dựng trực giác của bạn về thiết kế prompt.

## Hướng dẫn minh họa

Muốn có cái nhìn tổng quan về những gì bài học này bao gồm trước khi bạn bắt đầu? Hãy xem hướng dẫn minh họa này, giúp bạn hiểu các chủ đề chính được đề cập và các điểm quan trọng cần bạn suy nghĩ trong từng chủ đề. Lộ trình bài học đưa bạn từ việc hiểu các khái niệm và thách thức cốt lõi đến việc giải quyết chúng bằng các kỹ thuật và thực hành tốt nhất về prompt engineering. Lưu ý rằng phần "Kỹ thuật nâng cao" trong hướng dẫn này đề cập đến nội dung được đề cập trong chương _tiếp theo_ của giáo trình này.

## Startup của chúng tôi

Bây giờ, hãy nói về cách _chủ đề này_ liên quan đến sứ mệnh startup của chúng tôi để [mang sự đổi mới AI vào giáo dục](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chúng tôi muốn xây dựng các ứng dụng học tập cá nhân hóa được hỗ trợ bởi AI - vì vậy hãy nghĩ về cách những người dùng khác nhau của ứng dụng của chúng tôi có thể "thiết kế" prompts:

- **Quản trị viên** có thể yêu cầu AI _phân tích dữ liệu chương trình giảng dạy để xác định các lỗ hổng trong phạm vi_. AI có thể tóm tắt kết quả hoặc trực quan hóa chúng bằng mã.
- **Giáo viên** có thể yêu cầu AI _tạo một kế hoạch bài học cho một đối tượng và chủ đề mục tiêu_. AI có thể xây dựng kế hoạch cá nhân hóa theo định dạng được chỉ định.
- **Sinh viên** có thể yêu cầu AI _dạy họ một môn học khó_. AI hiện có thể hướng dẫn sinh viên với các bài học, gợi ý và ví dụ phù hợp với trình độ của họ.

Đó chỉ là phần nổi của tảng băng chìm. Hãy xem [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - một thư viện prompts mã nguồn mở được tuyển chọn bởi các chuyên gia giáo dục - để có cái nhìn rộng hơn về các khả năng! _Hãy thử chạy một số trong những prompts đó trong sandbox hoặc sử dụng OpenAI Playground để xem điều gì xảy ra!_

## Prompt Engineering là gì?

Chúng tôi bắt đầu bài học này bằng cách định nghĩa **Prompt Engineering** là quá trình _thiết kế và tối ưu hóa_ đầu vào văn bản (prompts) để cung cấp phản hồi nhất quán và chất lượng (completions) cho một mục tiêu ứng dụng và mô hình cụ thể. Chúng ta có thể nghĩ về điều này như một quá trình gồm 2 bước:

- _thiết kế_ prompt ban đầu cho một mô hình và mục tiêu cụ thể
- _tinh chỉnh_ prompt theo cách lặp đi lặp lại để cải thiện chất lượng của phản hồi

Điều này nhất thiết là một quá trình thử và sai yêu cầu trực giác và nỗ lực của người dùng để đạt được kết quả tối ưu. Vậy tại sao nó lại quan trọng? Để trả lời câu hỏi đó, trước tiên chúng ta cần hiểu ba khái niệm:

- _Tokenization_ = cách mô hình "nhìn thấy" prompt
- _Base LLMs_ = cách mô hình nền "xử lý" một prompt
- _Instruction-Tuned LLMs_ = cách mô hình hiện có thể thấy "nhiệm vụ"

### Tokenization

Một LLM nhìn thấy prompts như một _chuỗi các token_ trong đó các mô hình khác nhau (hoặc các phiên bản của một mô hình) có thể tokenize cùng một prompt theo những cách khác nhau. Vì LLMs được đào tạo trên các token (chứ không phải trên văn bản thô), cách các prompts được tokenize có ảnh hưởng trực tiếp đến chất lượng của phản hồi được tạo ra.

Để có trực giác về cách tokenization hoạt động, hãy thử các công cụ như [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) được hiển thị dưới đây. Sao chép prompt của bạn vào - và xem cách đó được chuyển đổi thành các token, chú ý cách các ký tự khoảng trắng và dấu câu được xử lý. Lưu ý rằng ví dụ này hiển thị một LLM cũ (GPT-3) - vì vậy việc thử điều này với một mô hình mới hơn có thể tạo ra kết quả khác.

### Khái niệm: Foundation Models

Khi một prompt được tokenize, chức năng chính của ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (hoặc mô hình nền) là dự đoán token trong chuỗi đó. Vì LLMs được đào tạo trên các tập dữ liệu văn bản lớn, chúng có hiểu biết tốt về các mối quan hệ thống kê giữa các token và có thể thực hiện dự đoán đó với một số độ tin cậy. Lưu ý rằng chúng không hiểu _ý nghĩa_ của các từ trong prompt hoặc token; chúng chỉ thấy một mẫu mà chúng có thể "hoàn thành" với dự đoán tiếp theo của mình. Chúng có thể tiếp tục dự đoán chuỗi cho đến khi bị chấm dứt bởi sự can thiệp của người dùng hoặc một điều kiện đã được thiết lập trước.

Muốn thấy cách hoàn thành dựa trên prompt hoạt động? Nhập prompt trên vào [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) của Azure OpenAI Studio với các cài đặt mặc định. Hệ thống được cấu hình để xử lý prompts như các yêu cầu thông tin - vì vậy bạn nên thấy một completion đáp ứng ngữ cảnh này.

Nhưng nếu người dùng muốn thấy điều gì đó cụ thể đáp ứng một tiêu chí hoặc mục tiêu nhiệm vụ thì sao? Đây là nơi _instruction-tuned_ LLMs xuất hiện.

### Khái niệm: Instruction Tuned LLMs

Một [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bắt đầu với mô hình nền và tinh chỉnh nó với các ví dụ hoặc cặp đầu vào/đầu ra (ví dụ: "tin nhắn" nhiều lượt) có thể chứa các hướng dẫn rõ ràng - và phản hồi từ AI cố gắng tuân theo hướng dẫn đó.

Điều này sử dụng các kỹ thuật như Reinforcement Learning with Human Feedback (RLHF) có thể đào tạo mô hình để _tuân theo hướng dẫn_ và _học từ phản hồi_ để tạo ra các phản hồi phù hợp hơn với các ứng dụng thực tế và liên quan hơn đến mục tiêu của người dùng.

Hãy thử nghiệm - xem lại prompt ở trên, nhưng bây giờ thay đổi _tin nhắn hệ thống_ để cung cấp hướng dẫn sau đây như ngữ cảnh:

> _Tóm tắt nội dung bạn được cung cấp cho học sinh lớp hai. Giữ kết quả trong một đoạn văn với 3-5 điểm bullet._

Hãy xem kết quả hiện đã được điều chỉnh để phản ánh mục tiêu và định dạng mong muốn? Một giáo viên hiện có thể trực tiếp sử dụng phản hồi này trong các slide của họ cho lớp học đó.

## Tại sao chúng ta cần Prompt Engineering?

Bây giờ chúng ta đã biết cách prompts được xử lý bởi LLMs, hãy nói về _tại sao_ chúng ta cần prompt engineering. Câu trả lời nằm ở thực tế rằng các LLM hiện tại đặt ra một số thách thức khiến _hoàn thành đáng tin cậy và nhất quán_ trở nên khó đạt được hơn mà không đặt nỗ lực vào việc xây dựng và tối ưu hóa prompt. Ví dụ:

1. **Phản hồi mô hình là ngẫu nhiên.** _Cùng một prompt_ có khả năng tạo ra các phản hồi khác nhau với các mô hình hoặc phiên bản mô hình khác nhau. Và nó thậm chí có thể tạo ra các kết quả khác nhau với _cùng một mô hình_ vào các thời điểm khác nhau. _Các kỹ thuật prompt engineering có thể giúp chúng ta giảm thiểu những biến thể này bằng cách cung cấp các biện pháp bảo vệ tốt hơn_.

1. **Các mô hình có thể tạo ra các phản hồi tưởng tượng.** Các mô hình được đào tạo trước với _các tập dữ liệu lớn nhưng hữu hạn_, nghĩa là chúng thiếu kiến thức về các khái niệm ngoài phạm vi đào tạo đó. Do đó, chúng có thể tạo ra các completions không chính xác, tưởng tượng hoặc trực tiếp mâu thuẫn với các sự thật đã biết. _Các kỹ thuật prompt engineering giúp người dùng xác định và giảm thiểu các phản hồi tưởng tượng như vậy, ví dụ: bằng cách yêu cầu AI cung cấp trích dẫn hoặc lý luận_.

1. **Khả năng của các mô hình sẽ thay đổi.** Các mô hình mới hơn hoặc các thế hệ mô hình sẽ có khả năng phong phú hơn nhưng cũng mang lại những đặc điểm riêng và sự đánh đổi trong chi phí & độ phức tạp. _Prompt engineering có thể giúp chúng ta phát triển các thực hành và quy trình tốt nhất trừu tượng hóa sự khác biệt và thích ứng với các yêu cầu cụ thể của mô hình một cách liền mạch, có thể mở rộng_.

Hãy xem điều này hoạt động trong OpenAI hoặc Azure OpenAI Playground:

- Sử dụng cùng một prompt với các triển khai LLM khác nhau (ví dụ, OpenAI, Azure OpenAI, Hugging Face) - bạn có thấy các biến thể không?
- Sử dụng cùng một prompt lặp đi lặp lại với cùng một triển khai LLM (ví dụ, Azure OpenAI playground) - những biến thể này khác nhau như thế nào?

### Ví dụ về Phản hồi Tưởng Tượng

Trong khóa học này, chúng tôi sử dụng thuật ngữ **"phản hồi tưởng tượng"** để chỉ hiện tượng mà LLMs đôi khi tạo ra thông tin không chính xác về mặt thực tế do hạn chế trong đào tạo hoặc các ràng buộc khác. Bạn cũng có thể đã nghe điều này được gọi là _"ảo giác"_ trong các bài viết phổ biến hoặc các bài báo nghiên cứu. Tuy nhiên, chúng tôi khuyến nghị mạnh mẽ sử dụng thuật ngữ _"phản hồi tưởng tượng"_ để chúng ta không vô tình nhân hóa hành vi bằng cách gán một đặc điểm giống con người cho một kết quả do máy móc điều khiển. Điều này cũng củng cố [các hướng dẫn AI có trách nhiệm](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) từ góc độ thuật ngữ, loại bỏ các thuật ngữ có thể được coi là xúc phạm hoặc không bao gồm trong một số ngữ cảnh.

Muốn có cái nhìn về cách phản hồi tưởng tượng hoạt động? Hãy nghĩ về một prompt yêu cầu AI tạo nội dung cho một chủ đề không tồn tại (để đảm bảo nó không được tìm thấy trong tập dữ liệu đào tạo). Ví dụ - tôi đã thử prompt này:

> **Prompt:** tạo một kế hoạch bài học về Cuộc Chiến Sao Hỏa năm 2076.

Một tìm kiếm trên web cho thấy rằng có các tài khoản hư cấu (ví dụ, loạt phim truyền hình hoặc sách) về các cuộc chiến Sao Hỏa - nhưng không có nào vào năm 2076. Lẽ thường cũng cho chúng ta biết rằng năm 2076 là _trong tương lai_ và do đó, không thể liên quan đến một sự kiện thực tế.

Vậy điều gì xảy ra khi chúng ta chạy prompt này với các nhà cung cấp LLM khác nhau?

> **Phản hồi 1**: OpenAI Playground (GPT-35)

> **Phản hồi 2**: Azure OpenAI Playground (GPT-35)

> **Phản hồi 3**: Hugging Face Chat Playground (LLama-2)

Như dự đoán, mỗi mô hình (hoặc phiên bản mô hình) tạo ra các phản hồi hơi khác nhau nhờ vào hành vi ngẫu nhiên và sự thay đổi khả năng mô hình. Ví dụ, một mô hình nhắm đến đối tượng học sinh lớp 8 trong khi mô hình khác giả định học sinh trung học. Nhưng cả ba mô hình đều tạo ra các phản hồi có thể thuyết phục một người dùng không được thông tin rằng sự kiện là thực.

Các kỹ thuật prompt engineering như _metaprompting_ và _cấu hình nhiệt độ_ có thể giảm thiểu các phản hồi tưởng tượng của mô hình ở một mức độ nào đó. Các _kiến trúc_ prompt engineering mới cũng tích hợp các công cụ và kỹ thuật mới một cách liền mạch vào luồng prompt, để giảm thiểu hoặc giảm bớt một số hiệu ứng này.

## Nghiên cứu trường hợp: GitHub Copilot

Hãy kết thúc phần này bằng cách có cái nhìn về cách prompt engineering được sử dụng trong các giải pháp thực tế bằng cách xem xét một Nghiên cứu Trường hợp: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot là "Lập trình viên đôi AI" của bạn - nó chuyển đổi các prompt văn bản thành các completions mã và được tích hợp vào môi trường phát triển của bạn (ví dụ, Visual Studio Code) để có trải nghiệm người dùng liền mạch. Như đã được tài liệu hóa trong loạt bài viết dưới đây, phiên bản đầu tiên dựa trên mô hình OpenAI Codex - với các kỹ sư nhanh chóng nhận ra sự cần thiết phải tinh chỉnh mô hình và phát triển các kỹ thuật prompt engineering tốt hơn, để cải thiện chất lượng mã. Vào tháng 7, họ [ra mắt một mô hình AI cải tiến vượt qua Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-cod
Cuối cùng, giá trị thực sự của các mẫu nằm ở khả năng tạo và xuất bản _thư viện nhắc_ cho các lĩnh vực ứng dụng dọc - nơi mà mẫu nhắc hiện được _tối ưu hóa_ để phản ánh ngữ cảnh hoặc ví dụ cụ thể của ứng dụng, giúp cho các phản hồi trở nên phù hợp và chính xác hơn đối với đối tượng người dùng mục tiêu. Kho [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) là một ví dụ tuyệt vời của phương pháp này, tuyển chọn một thư viện các nhắc cho lĩnh vực giáo dục với sự nhấn mạnh vào các mục tiêu chính như lập kế hoạch bài học, thiết kế chương trình học, dạy kèm học sinh, v.v.

## Nội dung hỗ trợ

Nếu chúng ta nghĩ về việc xây dựng nhắc nhở như có một hướng dẫn (nhiệm vụ) và một mục tiêu (nội dung chính), thì _nội dung phụ_ giống như ngữ cảnh bổ sung mà chúng ta cung cấp để **ảnh hưởng đến kết quả theo một cách nào đó**. Nó có thể là điều chỉnh các tham số, hướng dẫn định dạng, phân loại chủ đề, v.v. có thể giúp mô hình _tùy chỉnh_ phản hồi của mình để phù hợp với các mục tiêu hoặc kỳ vọng của người dùng mong muốn.

Ví dụ: Cho một danh mục khóa học với siêu dữ liệu phong phú (tên, mô tả, cấp độ, thẻ siêu dữ liệu, giảng viên, v.v.) về tất cả các khóa học có sẵn trong chương trình học:

- chúng ta có thể định nghĩa một hướng dẫn để "tóm tắt danh mục khóa học cho mùa Thu 2023"
- chúng ta có thể sử dụng nội dung chính để cung cấp một vài ví dụ về kết quả mong muốn
- chúng ta có thể sử dụng nội dung phụ để xác định 5 "thẻ" quan tâm hàng đầu.

Bây giờ, mô hình có thể cung cấp một bản tóm tắt theo định dạng được hiển thị bởi một vài ví dụ - nhưng nếu một kết quả có nhiều thẻ, nó có thể ưu tiên 5 thẻ được xác định trong nội dung phụ.

---

## Thực hành tốt nhất về nhắc nhở

Bây giờ chúng ta biết cách nhắc nhở có thể được _xây dựng_, chúng ta có thể bắt đầu suy nghĩ về cách _thiết kế_ chúng để phản ánh các thực hành tốt nhất. Chúng ta có thể nghĩ về điều này theo hai phần - có được tư duy _đúng_ và áp dụng các kỹ thuật _đúng_.

### Tư duy Kỹ thuật Nhắc nhở

Kỹ thuật Nhắc nhở là một quá trình thử và sai nên hãy ghi nhớ ba yếu tố hướng dẫn rộng:

1. **Hiểu biết về lĩnh vực quan trọng.** Độ chính xác và sự liên quan của phản hồi là một hàm của _lĩnh vực_ mà ứng dụng hoặc người dùng đó hoạt động. Áp dụng trực giác và chuyên môn của bạn để **tùy chỉnh các kỹ thuật** thêm nữa. Ví dụ, định nghĩa _tính cách cụ thể của lĩnh vực_ trong các nhắc hệ thống của bạn, hoặc sử dụng _mẫu cụ thể của lĩnh vực_ trong các nhắc người dùng của bạn. Cung cấp nội dung phụ phản ánh ngữ cảnh cụ thể của lĩnh vực, hoặc sử dụng _dấu hiệu và ví dụ cụ thể của lĩnh vực_ để hướng dẫn mô hình theo các mẫu sử dụng quen thuộc.

2. **Hiểu biết về mô hình quan trọng.** Chúng ta biết các mô hình là ngẫu nhiên theo bản chất. Nhưng các triển khai mô hình cũng có thể khác nhau về bộ dữ liệu đào tạo mà chúng sử dụng (kiến thức tiền đào tạo), các khả năng mà chúng cung cấp (ví dụ, qua API hoặc SDK) và loại nội dung mà chúng được tối ưu hóa (ví dụ, mã vs. hình ảnh vs. văn bản). Hiểu rõ điểm mạnh và hạn chế của mô hình bạn đang sử dụng, và sử dụng kiến thức đó để _ưu tiên các nhiệm vụ_ hoặc xây dựng _mẫu tùy chỉnh_ được tối ưu hóa cho khả năng của mô hình.

3. **Lặp lại & Xác nhận quan trọng.** Các mô hình đang phát triển nhanh chóng, và các kỹ thuật cho kỹ thuật nhắc nhở cũng vậy. Là một chuyên gia trong lĩnh vực, bạn có thể có ngữ cảnh hoặc tiêu chí khác _cho_ ứng dụng cụ thể của bạn, điều này có thể không áp dụng cho cộng đồng rộng lớn hơn. Sử dụng các công cụ và kỹ thuật nhắc nhở để "khởi động" việc xây dựng nhắc nhở, sau đó lặp lại và xác nhận kết quả bằng trực giác và chuyên môn của bạn. Ghi lại những hiểu biết của bạn và tạo ra một **cơ sở kiến thức** (ví dụ, thư viện nhắc) có thể được sử dụng làm nền tảng mới bởi những người khác, để có các lần lặp nhanh hơn trong tương lai.

## Thực hành tốt nhất

Bây giờ hãy nhìn vào các thực hành tốt nhất phổ biến được khuyến nghị bởi [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) và các nhà thực hành [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Điều gì                              | Tại sao                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Đánh giá các mô hình mới nhất.       | Các thế hệ mô hình mới có khả năng có các tính năng và chất lượng cải tiến - nhưng cũng có thể chịu chi phí cao hơn. Đánh giá chúng để xem tác động, sau đó đưa ra quyết định di chuyển.                                                                                |
| Tách biệt hướng dẫn & ngữ cảnh   | Kiểm tra xem mô hình/nhà cung cấp của bạn có định nghĩa _dấu phân cách_ để phân biệt hướng dẫn, nội dung chính và nội dung phụ rõ ràng hơn không. Điều này có thể giúp các mô hình gán trọng số chính xác hơn cho các token.                                                         |
| Hãy cụ thể và rõ ràng             | Cung cấp thêm chi tiết về ngữ cảnh mong muốn, kết quả, độ dài, định dạng, phong cách, v.v. Điều này sẽ cải thiện cả chất lượng và sự nhất quán của các phản hồi. Ghi lại các công thức trong các mẫu có thể tái sử dụng.                                                          |
| Hãy mô tả, sử dụng ví dụ      | Các mô hình có thể phản hồi tốt hơn với cách tiếp cận "trình diễn và kể chuyện". Bắt đầu với một `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` các giá trị. Quay lại phần [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) để tìm hiểu thêm.

### Tiếp theo, mở Jupyter Notebook

- Chọn kernel runtime. Nếu sử dụng tùy chọn 1 hoặc 2, chỉ cần chọn kernel Python 3.10.x mặc định được cung cấp bởi dev container.

Bạn đã sẵn sàng để chạy các bài tập. Lưu ý rằng không có câu trả lời _đúng và sai_ ở đây - chỉ là khám phá các tùy chọn bằng cách thử và sai và xây dựng trực giác cho những gì hoạt động cho một mô hình và lĩnh vực ứng dụng nhất định.

_Vì lý do này, không có đoạn giải pháp mã trong bài học này. Thay vào đó, Notebook sẽ có các ô Markdown tiêu đề "Giải pháp của tôi:" cho thấy một ví dụ đầu ra để tham khảo._

## Kiểm tra kiến thức

Cái nào sau đây là một nhắc tốt theo một số thực hành tốt hợp lý?

1. Cho tôi xem một hình ảnh của chiếc xe màu đỏ
2. Cho tôi xem một hình ảnh của chiếc xe màu đỏ của hãng Volvo và mẫu XC90 đậu cạnh vách đá với hoàng hôn
3. Cho tôi xem một hình ảnh của chiếc xe màu đỏ của hãng Volvo và mẫu XC90

A: 2, đó là nhắc tốt nhất vì nó cung cấp chi tiết về "cái gì" và đi vào cụ thể (không chỉ bất kỳ chiếc xe nào mà là một hãng và mẫu cụ thể) và nó cũng mô tả ngữ cảnh tổng thể. 3 là tốt nhất tiếp theo vì nó cũng chứa nhiều mô tả.

## 🚀 Thử thách

Xem liệu bạn có thể tận dụng kỹ thuật "gợi ý" với nhắc nhở: Hoàn thành câu "Cho tôi xem một hình ảnh của chiếc xe màu đỏ của hãng Volvo và ". Nó phản hồi như thế nào, và bạn sẽ cải thiện nó như thế nào?

## Làm tốt lắm! Tiếp tục học tập của bạn

Muốn tìm hiểu thêm về các khái niệm Kỹ thuật Nhắc nhở khác nhau? Hãy đến trang [học tập tiếp tục](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tìm các tài nguyên tuyệt vời khác về chủ đề này.

Hãy đến Bài học 5 nơi chúng ta sẽ xem xét [các kỹ thuật nhắc nâng cao](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.