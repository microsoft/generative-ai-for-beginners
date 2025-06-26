<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:28:10+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "vi"
}
-->
# Sử Dụng AI Tạo Sinh Một Cách Có Trách Nhiệm

> _Nhấn vào hình trên để xem video của bài học này_

Rất dễ bị cuốn hút bởi AI và đặc biệt là AI tạo sinh, nhưng bạn cần cân nhắc cách sử dụng nó một cách có trách nhiệm. Bạn cần cân nhắc những điều như cách đảm bảo đầu ra là công bằng, không gây hại và nhiều hơn nữa. Chương này nhằm cung cấp cho bạn bối cảnh đã đề cập, những gì cần cân nhắc và cách thực hiện các bước tích cực để cải thiện việc sử dụng AI của bạn.

## Giới Thiệu

Bài học này sẽ bao gồm:

- Tại sao bạn nên ưu tiên AI Có Trách Nhiệm khi xây dựng các ứng dụng AI Tạo Sinh.
- Nguyên tắc cốt lõi của AI Có Trách Nhiệm và cách chúng liên quan đến AI Tạo Sinh.
- Cách áp dụng những nguyên tắc AI Có Trách Nhiệm này vào thực tế thông qua chiến lược và công cụ.

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết:

- Tầm quan trọng của AI Có Trách Nhiệm khi xây dựng các ứng dụng AI Tạo Sinh.
- Khi nào nên suy nghĩ và áp dụng các nguyên tắc cốt lõi của AI Có Trách Nhiệm khi xây dựng các ứng dụng AI Tạo Sinh.
- Những công cụ và chiến lược nào có sẵn cho bạn để thực hiện khái niệm AI Có Trách Nhiệm.

## Nguyên Tắc AI Có Trách Nhiệm

Sự hào hứng với AI Tạo Sinh chưa bao giờ cao hơn. Sự hào hứng này đã mang lại rất nhiều nhà phát triển mới, sự chú ý và nguồn tài trợ cho lĩnh vực này. Mặc dù điều này rất tích cực cho bất kỳ ai đang tìm cách xây dựng sản phẩm và công ty sử dụng AI Tạo Sinh, điều quan trọng là chúng ta cũng phải tiến hành một cách có trách nhiệm.

Trong suốt khóa học này, chúng ta tập trung vào việc xây dựng startup và sản phẩm giáo dục AI của mình. Chúng ta sẽ sử dụng các nguyên tắc của AI Có Trách Nhiệm: Công bằng, Bao gồm, Độ tin cậy/An toàn, Bảo mật & Riêng tư, Minh bạch và Trách nhiệm. Với những nguyên tắc này, chúng ta sẽ khám phá cách chúng liên quan đến việc sử dụng AI Tạo Sinh trong sản phẩm của chúng ta.

## Tại Sao Bạn Nên Ưu Tiên AI Có Trách Nhiệm

Khi xây dựng một sản phẩm, việc áp dụng phương pháp tiếp cận tập trung vào con người bằng cách giữ lợi ích tốt nhất của người dùng trong tâm trí dẫn đến kết quả tốt nhất.

Sự độc đáo của AI Tạo Sinh là khả năng tạo ra các câu trả lời, thông tin, hướng dẫn và nội dung hữu ích cho người dùng. Điều này có thể được thực hiện mà không cần nhiều bước thủ công, có thể dẫn đến kết quả rất ấn tượng. Tuy nhiên, nếu không có kế hoạch và chiến lược đúng đắn, điều này cũng có thể dẫn đến một số kết quả có hại cho người dùng, sản phẩm của bạn và toàn xã hội.

Hãy xem một số (nhưng không phải tất cả) các kết quả có hại tiềm ẩn này:

### Ảo Giác

Ảo giác là thuật ngữ dùng để mô tả khi một LLM tạo ra nội dung hoàn toàn vô nghĩa hoặc điều gì đó mà chúng ta biết là sai sự thật dựa trên các nguồn thông tin khác.

Hãy lấy ví dụ, chúng ta xây dựng một tính năng cho startup của mình cho phép học sinh đặt câu hỏi lịch sử cho một mô hình. Một học sinh đặt câu hỏi `Who was the sole survivor of Titanic?`

Mô hình tạo ra một phản hồi như sau:

Đây là một câu trả lời rất tự tin và chi tiết. Tuy nhiên, nó không đúng. Ngay cả với một lượng nghiên cứu tối thiểu, người ta cũng có thể phát hiện ra có nhiều hơn một người sống sót trong thảm họa Titanic. Đối với một học sinh chỉ mới bắt đầu nghiên cứu chủ đề này, câu trả lời này có thể đủ thuyết phục để không bị nghi ngờ và được coi là sự thật. Hậu quả của điều này có thể dẫn đến hệ thống AI không đáng tin cậy và ảnh hưởng tiêu cực đến danh tiếng của startup của chúng ta.

Với mỗi lần lặp lại của bất kỳ LLM nào, chúng ta đã thấy sự cải thiện hiệu suất trong việc giảm thiểu ảo giác. Ngay cả với sự cải thiện này, chúng ta với tư cách là những người xây dựng ứng dụng và người dùng vẫn cần nhận thức được những hạn chế này.

### Nội Dung Có Hại

Chúng ta đã đề cập trong phần trước khi một LLM tạo ra các phản hồi sai hoặc vô nghĩa. Một rủi ro khác mà chúng ta cần nhận thức là khi mô hình phản hồi với nội dung có hại.

Nội dung có hại có thể được định nghĩa là:

- Cung cấp hướng dẫn hoặc khuyến khích tự hại hoặc gây hại cho các nhóm nhất định.
- Nội dung thù hận hoặc hạ thấp.
- Hướng dẫn lập kế hoạch cho bất kỳ loại tấn công hoặc hành động bạo lực nào.
- Cung cấp hướng dẫn về cách tìm nội dung bất hợp pháp hoặc thực hiện hành vi phạm pháp.
- Hiển thị nội dung tình dục rõ ràng.

Đối với startup của chúng ta, chúng ta muốn đảm bảo rằng chúng ta có các công cụ và chiến lược đúng đắn để ngăn chặn loại nội dung này được nhìn thấy bởi học sinh.

### Thiếu Công Bằng

Công bằng được định nghĩa là "đảm bảo rằng một hệ thống AI không có thành kiến và phân biệt đối xử và rằng nó đối xử với mọi người một cách công bằng và bình đẳng." Trong thế giới AI Tạo Sinh, chúng ta muốn đảm bảo rằng các quan điểm thế giới loại trừ của các nhóm bị thiệt thòi không được củng cố bởi đầu ra của mô hình.

Những loại đầu ra này không chỉ phá hoại việc xây dựng trải nghiệm sản phẩm tích cực cho người dùng của chúng ta mà còn gây hại xã hội thêm. Với tư cách là những người xây dựng ứng dụng, chúng ta nên luôn giữ một cơ sở người dùng rộng lớn và đa dạng trong tâm trí khi xây dựng các giải pháp với AI Tạo Sinh.

## Cách Sử Dụng AI Tạo Sinh Một Cách Có Trách Nhiệm

Bây giờ chúng ta đã xác định được tầm quan trọng của AI Tạo Sinh Có Trách Nhiệm, hãy xem xét 4 bước chúng ta có thể thực hiện để xây dựng các giải pháp AI của mình một cách có trách nhiệm:

### Đo Lường Các Tác Hại Tiềm Ẩn

Trong thử nghiệm phần mềm, chúng ta kiểm tra các hành động dự kiến của người dùng trên ứng dụng. Tương tự, thử nghiệm một tập hợp đa dạng các lời nhắc mà người dùng có khả năng sử dụng là một cách tốt để đo lường tác hại tiềm ẩn.

Vì startup của chúng ta đang xây dựng một sản phẩm giáo dục, sẽ tốt nếu chuẩn bị một danh sách các lời nhắc liên quan đến giáo dục. Điều này có thể bao gồm một số môn học, sự kiện lịch sử và lời nhắc về cuộc sống sinh viên.

### Giảm Thiểu Các Tác Hại Tiềm Ẩn

Bây giờ là lúc tìm cách mà chúng ta có thể ngăn chặn hoặc hạn chế tác hại tiềm ẩn gây ra bởi mô hình và các phản hồi của nó. Chúng ta có thể xem xét điều này ở 4 lớp khác nhau:

- **Mô Hình**. Chọn mô hình phù hợp cho trường hợp sử dụng phù hợp. Các mô hình lớn hơn và phức tạp hơn như GPT-4 có thể gây ra nhiều rủi ro nội dung có hại hơn khi áp dụng cho các trường hợp sử dụng nhỏ hơn và cụ thể hơn. Sử dụng dữ liệu đào tạo của bạn để tinh chỉnh cũng giảm thiểu rủi ro nội dung có hại.

- **Hệ Thống An Toàn**. Một hệ thống an toàn là tập hợp các công cụ và cấu hình trên nền tảng phục vụ mô hình giúp giảm thiểu tác hại. Một ví dụ về điều này là hệ thống lọc nội dung trên dịch vụ Azure OpenAI. Các hệ thống cũng nên phát hiện các cuộc tấn công jailbreak và hoạt động không mong muốn như yêu cầu từ bot.

- **Metaprompt**. Metaprompts và grounding là cách chúng ta có thể định hướng hoặc hạn chế mô hình dựa trên các hành vi và thông tin nhất định. Điều này có thể là sử dụng đầu vào hệ thống để xác định các giới hạn nhất định của mô hình. Ngoài ra, cung cấp đầu ra phù hợp hơn với phạm vi hoặc lĩnh vực của hệ thống.

Nó cũng có thể là sử dụng các kỹ thuật như Tạo Sinh Tăng Cường Truy Xuất (RAG) để khiến mô hình chỉ kéo thông tin từ một tập hợp các nguồn đáng tin cậy. Có một bài học sau trong khóa học này về [xây dựng ứng dụng tìm kiếm](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Trải Nghiệm Người Dùng**. Lớp cuối cùng là nơi người dùng tương tác trực tiếp với mô hình thông qua giao diện ứng dụng của chúng ta theo một cách nào đó. Bằng cách này, chúng ta có thể thiết kế UI/UX để hạn chế người dùng về các loại đầu vào họ có thể gửi đến mô hình cũng như văn bản hoặc hình ảnh hiển thị cho người dùng. Khi triển khai ứng dụng AI, chúng ta cũng phải minh bạch về những gì ứng dụng AI Tạo Sinh của chúng ta có thể và không thể làm.

Chúng ta có một bài học toàn diện dành riêng cho [Thiết Kế UX cho Ứng Dụng AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Đánh Giá Mô Hình**. Làm việc với LLM có thể khó khăn vì chúng ta không phải lúc nào cũng kiểm soát được dữ liệu mà mô hình đã được đào tạo. Dù sao, chúng ta nên luôn đánh giá hiệu suất và đầu ra của mô hình. Vẫn quan trọng để đo lường độ chính xác, độ tương đồng, độ căn cứ và độ liên quan của đầu ra. Điều này giúp cung cấp sự minh bạch và tin tưởng cho các bên liên quan và người dùng.

### Vận Hành Giải Pháp AI Tạo Sinh Có Trách Nhiệm

Xây dựng một thực hành vận hành xung quanh các ứng dụng AI của bạn là giai đoạn cuối cùng. Điều này bao gồm việc hợp tác với các bộ phận khác của startup như Pháp lý và Bảo mật để đảm bảo chúng ta tuân thủ tất cả các chính sách quy định. Trước khi ra mắt, chúng ta cũng muốn xây dựng các kế hoạch xung quanh việc phân phối, xử lý sự cố và quay lại để ngăn chặn bất kỳ tác hại nào đối với người dùng của chúng ta.

## Công Cụ

Mặc dù công việc phát triển các giải pháp AI Có Trách Nhiệm có vẻ như rất nhiều, đó là công việc đáng nỗ lực. Khi lĩnh vực AI Tạo Sinh phát triển, nhiều công cụ giúp các nhà phát triển tích hợp trách nhiệm vào quy trình làm việc của họ sẽ trưởng thành. Ví dụ, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) có thể giúp phát hiện nội dung và hình ảnh có hại thông qua yêu cầu API.

## Kiểm Tra Kiến Thức

Có những điều gì bạn cần quan tâm để đảm bảo sử dụng AI một cách có trách nhiệm?

1. Rằng câu trả lời là chính xác.
2. Sử dụng có hại, rằng AI không được sử dụng cho mục đích phạm pháp.
3. Đảm bảo AI không có thành kiến và phân biệt đối xử.

A: 2 và 3 là đúng. AI Có Trách Nhiệm giúp bạn cân nhắc cách giảm thiểu các tác động có hại và thành kiến và nhiều hơn nữa.

## 🚀 Thử Thách

Tìm hiểu về [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) và xem bạn có thể áp dụng điều gì cho việc sử dụng của mình.

## Công Việc Tuyệt Vời, Tiếp Tục Học Tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học AI Tạo Sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức AI Tạo Sinh của bạn!

Hãy chuyển sang Bài học 4 nơi chúng ta sẽ xem xét [Các Nguyên Tắc Cơ Bản Về Kỹ Thuật Lời Nhắc](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tài liệu chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.