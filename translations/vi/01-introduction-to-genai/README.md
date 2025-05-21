<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:26:51+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "vi"
}
-->
# Giới thiệu về AI Tạo sinh và Mô hình Ngôn ngữ Lớn

_(Nhấp vào hình ảnh ở trên để xem video của bài học này)_

AI Tạo sinh là trí tuệ nhân tạo có khả năng tạo ra văn bản, hình ảnh và các loại nội dung khác. Điều làm cho nó trở thành một công nghệ tuyệt vời là nó dân chủ hóa AI, ai cũng có thể sử dụng nó chỉ với một lời nhắc văn bản, một câu viết bằng ngôn ngữ tự nhiên. Bạn không cần phải học một ngôn ngữ như Java hay SQL để làm điều gì đó có ý nghĩa, tất cả những gì bạn cần là sử dụng ngôn ngữ của mình, nêu rõ điều bạn muốn và một đề xuất từ mô hình AI sẽ xuất hiện. Các ứng dụng và tác động của điều này là rất lớn, bạn có thể viết hoặc hiểu báo cáo, viết ứng dụng và nhiều hơn nữa, chỉ trong vài giây.

Trong chương trình học này, chúng ta sẽ khám phá cách startup của chúng ta tận dụng AI tạo sinh để mở khóa các kịch bản mới trong thế giới giáo dục và cách chúng ta giải quyết những thách thức không thể tránh khỏi liên quan đến các tác động xã hội của việc ứng dụng và giới hạn công nghệ.

## Giới thiệu

Bài học này sẽ bao gồm:

- Giới thiệu về kịch bản kinh doanh: ý tưởng và sứ mệnh của startup của chúng ta.
- AI Tạo sinh và cách chúng ta đạt được cảnh quan công nghệ hiện tại.
- Hoạt động bên trong của một mô hình ngôn ngữ lớn.
- Các khả năng chính và các trường hợp sử dụng thực tế của Mô hình Ngôn ngữ Lớn.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ hiểu:

- AI tạo sinh là gì và Mô hình Ngôn ngữ Lớn hoạt động như thế nào.
- Cách bạn có thể tận dụng mô hình ngôn ngữ lớn cho các trường hợp sử dụng khác nhau, tập trung vào các kịch bản giáo dục.

## Kịch bản: startup giáo dục của chúng ta

Trí tuệ Nhân tạo Tạo sinh (AI) đại diện cho đỉnh cao của công nghệ AI, đẩy xa giới hạn của những gì từng được cho là không thể. Các mô hình AI tạo sinh có nhiều khả năng và ứng dụng, nhưng trong chương trình học này, chúng ta sẽ khám phá cách nó đang cách mạng hóa giáo dục thông qua một startup hư cấu. Chúng ta sẽ gọi startup này là _startup của chúng ta_. Startup của chúng ta hoạt động trong lĩnh vực giáo dục với tuyên bố sứ mệnh đầy tham vọng là

> _cải thiện khả năng tiếp cận trong học tập, trên quy mô toàn cầu, đảm bảo tiếp cận giáo dục công bằng và cung cấp trải nghiệm học tập cá nhân hóa cho mọi người học, theo nhu cầu của họ_.

Đội ngũ của startup chúng ta nhận thức rằng chúng ta sẽ không thể đạt được mục tiêu này nếu không tận dụng một trong những công cụ mạnh mẽ nhất của thời hiện đại – Mô hình Ngôn ngữ Lớn (LLMs).

AI Tạo sinh được kỳ vọng sẽ cách mạng hóa cách chúng ta học và dạy ngày nay, với học sinh có sẵn giáo viên ảo 24 giờ một ngày cung cấp lượng thông tin và ví dụ phong phú, và giáo viên có thể tận dụng công cụ sáng tạo để đánh giá học sinh của họ và đưa ra phản hồi.

Để bắt đầu, hãy định nghĩa một số khái niệm cơ bản và thuật ngữ mà chúng ta sẽ sử dụng trong suốt chương trình học.

## Làm thế nào chúng ta có được AI Tạo sinh?

Mặc dù sự _hype_ phi thường được tạo ra gần đây bởi việc công bố các mô hình AI tạo sinh, công nghệ này đã được phát triển trong nhiều thập kỷ, với những nỗ lực nghiên cứu đầu tiên có từ những năm 60. Hiện tại chúng ta đang ở một điểm mà AI có khả năng nhận thức của con người, như trò chuyện như được thể hiện bởi ví dụ như [OpenAI ChatGPT](https://openai.com/chatgpt) hoặc [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), cũng sử dụng mô hình GPT cho các cuộc trò chuyện tìm kiếm web Bing.

Quay lại một chút, các nguyên mẫu AI đầu tiên bao gồm các chatbot đánh máy, dựa vào một cơ sở kiến thức được trích xuất từ một nhóm chuyên gia và được biểu diễn vào máy tính. Các câu trả lời trong cơ sở kiến thức được kích hoạt bởi các từ khóa xuất hiện trong văn bản đầu vào. Tuy nhiên, nhanh chóng rõ ràng rằng cách tiếp cận này, sử dụng các chatbot đánh máy, không mở rộng tốt.

### Cách tiếp cận thống kê với AI: Machine Learning

Một bước ngoặt đã đến trong những năm 90, với việc áp dụng một cách tiếp cận thống kê để phân tích văn bản. Điều này dẫn đến sự phát triển của các thuật toán mới – được gọi là machine learning – có khả năng học các mẫu từ dữ liệu mà không cần được lập trình rõ ràng. Cách tiếp cận này cho phép máy móc mô phỏng hiểu ngôn ngữ của con người: một mô hình thống kê được đào tạo trên các cặp văn bản-nhãn, cho phép mô hình phân loại văn bản đầu vào chưa biết với một nhãn được định trước đại diện cho ý định của thông điệp.

### Mạng nơ-ron và các trợ lý ảo hiện đại

Trong những năm gần đây, sự tiến hóa công nghệ của phần cứng, có khả năng xử lý lượng dữ liệu lớn hơn và các tính toán phức tạp hơn, đã khuyến khích nghiên cứu trong AI, dẫn đến sự phát triển của các thuật toán machine learning tiên tiến được gọi là mạng nơ-ron hoặc các thuật toán học sâu.

Mạng nơ-ron (và đặc biệt là Mạng nơ-ron Hồi quy – RNNs) đã cải thiện đáng kể xử lý ngôn ngữ tự nhiên, cho phép biểu diễn ý nghĩa của văn bản một cách có ý nghĩa hơn, đánh giá ngữ cảnh của một từ trong câu.

Đây là công nghệ đã thúc đẩy các trợ lý ảo ra đời trong thập kỷ đầu tiên của thế kỷ mới, rất thành thạo trong việc diễn giải ngôn ngữ của con người, xác định một nhu cầu và thực hiện một hành động để đáp ứng nó – như trả lời bằng một kịch bản được định trước hoặc sử dụng dịch vụ của bên thứ ba.

### Ngày nay, AI Tạo sinh

Đó là cách chúng ta đã đến với AI Tạo sinh ngày nay, có thể được coi là một phần của học sâu.

Sau nhiều thập kỷ nghiên cứu trong lĩnh vực AI, một kiến trúc mô hình mới – được gọi là _Transformer_ – đã vượt qua giới hạn của RNNs, có khả năng nhận các chuỗi văn bản dài hơn nhiều làm đầu vào. Transformers dựa trên cơ chế chú ý, cho phép mô hình đưa ra các trọng số khác nhau cho các đầu vào mà nó nhận được, ‘chú ý nhiều hơn’ nơi thông tin liên quan nhất được tập trung, bất kể thứ tự của chúng trong chuỗi văn bản.

Hầu hết các mô hình AI tạo sinh gần đây – còn được gọi là Mô hình Ngôn ngữ Lớn (LLMs), vì chúng làm việc với đầu vào và đầu ra bằng văn bản – thực sự dựa trên kiến trúc này. Điều thú vị về những mô hình này – được đào tạo trên một lượng dữ liệu không có nhãn khổng lồ từ các nguồn đa dạng như sách, bài báo và trang web – là chúng có thể thích ứng với nhiều nhiệm vụ khác nhau và tạo ra văn bản ngữ pháp chính xác với vẻ ngoài của sự sáng tạo. Vì vậy, không chỉ chúng đã cải thiện đáng kể khả năng của máy móc để ‘hiểu’ văn bản đầu vào, mà chúng còn cho phép khả năng của chúng để tạo ra một phản hồi nguyên bản bằng ngôn ngữ con người.

## Mô hình ngôn ngữ lớn hoạt động như thế nào?

Trong chương tiếp theo, chúng ta sẽ khám phá các loại mô hình AI tạo sinh khác nhau, nhưng bây giờ hãy xem mô hình ngôn ngữ lớn hoạt động như thế nào, với sự tập trung vào mô hình OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, chuyển văn bản thành số**: Mô hình Ngôn ngữ Lớn nhận văn bản làm đầu vào và tạo văn bản làm đầu ra. Tuy nhiên, là các mô hình thống kê, chúng hoạt động tốt hơn nhiều với các con số hơn là các chuỗi văn bản. Đó là lý do tại sao mọi đầu vào cho mô hình được xử lý bởi một tokenizer, trước khi được sử dụng bởi mô hình lõi. Một token là một đoạn văn bản – bao gồm một số lượng ký tự thay đổi, vì vậy nhiệm vụ chính của tokenizer là chia đầu vào thành một mảng các token. Sau đó, mỗi token được ánh xạ với một chỉ số token, là mã hóa số nguyên của đoạn văn bản gốc.

- **Dự đoán các token đầu ra**: Với n token làm đầu vào (với max n thay đổi từ mô hình này sang mô hình khác), mô hình có thể dự đoán một token làm đầu ra. Token này sau đó được kết hợp vào đầu vào của lần lặp tiếp theo, theo một mẫu cửa sổ mở rộng, cho phép trải nghiệm người dùng tốt hơn khi nhận được một (hoặc nhiều) câu làm câu trả lời. Điều này giải thích tại sao, nếu bạn từng chơi với ChatGPT, bạn có thể đã nhận thấy rằng đôi khi nó dường như dừng lại giữa câu.

- **Quá trình lựa chọn, phân phối xác suất**: Token đầu ra được chọn bởi mô hình theo xác suất của nó xảy ra sau chuỗi văn bản hiện tại. Điều này là do mô hình dự đoán một phân phối xác suất trên tất cả các ‘token tiếp theo’ có thể, được tính toán dựa trên việc đào tạo của nó. Tuy nhiên, không phải lúc nào token có xác suất cao nhất cũng được chọn từ phân phối kết quả. Một mức độ ngẫu nhiên được thêm vào lựa chọn này, theo cách mà mô hình hành động theo cách không xác định - chúng ta không nhận được đầu ra giống hệt nhau cho cùng một đầu vào. Mức độ ngẫu nhiên này được thêm vào để mô phỏng quá trình suy nghĩ sáng tạo và nó có thể được điều chỉnh bằng một tham số mô hình gọi là nhiệt độ.

## Startup của chúng ta có thể tận dụng Mô hình Ngôn ngữ Lớn như thế nào?

Bây giờ chúng ta đã hiểu rõ hơn về hoạt động bên trong của một mô hình ngôn ngữ lớn, hãy xem một số ví dụ thực tế về các nhiệm vụ phổ biến nhất mà chúng có thể thực hiện khá tốt, với sự chú ý đến kịch bản kinh doanh của chúng ta. Chúng ta đã nói rằng khả năng chính của một Mô hình Ngôn ngữ Lớn là _tạo ra văn bản từ đầu, bắt đầu từ một đầu vào bằng văn bản, viết bằng ngôn ngữ tự nhiên_.

Nhưng loại đầu vào và đầu ra văn bản nào?
Đầu vào của một mô hình ngôn ngữ lớn được gọi là prompt, trong khi đầu ra được gọi là completion, thuật ngữ này đề cập đến cơ chế của mô hình tạo ra token tiếp theo để hoàn thành đầu vào hiện tại. Chúng ta sẽ đi sâu vào prompt là gì và cách thiết kế nó để tận dụng tối đa mô hình của chúng ta. Nhưng bây giờ, hãy chỉ nói rằng một prompt có thể bao gồm:

- Một **hướng dẫn** chỉ định loại đầu ra mà chúng ta mong đợi từ mô hình. Hướng dẫn này đôi khi có thể nhúng một số ví dụ hoặc một số dữ liệu bổ sung.

  1. Tóm tắt một bài báo, sách, đánh giá sản phẩm và nhiều hơn nữa, cùng với việc trích xuất thông tin từ dữ liệu không có cấu trúc.
    
  2. Tạo ý tưởng sáng tạo và thiết kế một bài báo, một bài luận, một nhiệm vụ hoặc nhiều hơn nữa.
      
- Một **câu hỏi**, được hỏi dưới dạng một cuộc trò chuyện với một tác nhân.

- Một đoạn **văn bản cần hoàn thành**, mà ngầm là một yêu cầu trợ giúp viết.

- Một đoạn **mã** cùng với yêu cầu giải thích và ghi chép nó, hoặc một bình luận yêu cầu tạo ra một đoạn mã thực hiện một nhiệm vụ cụ thể.

Các ví dụ trên khá đơn giản và không nhằm mục đích làm một minh chứng toàn diện về khả năng của Mô hình Ngôn ngữ Lớn. Chúng nhằm mục đích cho thấy tiềm năng của việc sử dụng AI tạo sinh, đặc biệt nhưng không giới hạn trong các ngữ cảnh giáo dục.

Ngoài ra, đầu ra của một mô hình AI tạo sinh không hoàn hảo và đôi khi sự sáng tạo của mô hình có thể chống lại nó, dẫn đến một đầu ra là sự kết hợp của các từ mà người dùng có thể hiểu là một sự xuyên tạc thực tế, hoặc có thể xúc phạm. AI tạo sinh không thông minh - ít nhất là trong định nghĩa toàn diện hơn về trí thông minh, bao gồm lý luận phê bình và sáng tạo hoặc trí thông minh cảm xúc; nó không phải là xác định, và nó không đáng tin cậy, vì những bịa đặt, như các tham chiếu sai, nội dung và tuyên bố, có thể được kết hợp với thông tin chính xác, và được trình bày một cách thuyết phục và tự tin. Trong các bài học tiếp theo, chúng ta sẽ đối mặt với tất cả những giới hạn này và chúng ta sẽ xem những gì chúng ta có thể làm để giảm thiểu chúng.

## Bài tập

Bài tập của bạn là đọc thêm về [AI tạo sinh](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) và cố gắng xác định một lĩnh vực mà bạn sẽ thêm AI tạo sinh vào hôm nay mà chưa có. Tác động sẽ khác biệt như thế nào so với việc làm theo cách "cũ", bạn có thể làm điều gì mà trước đây không thể, hay bạn nhanh hơn không? Viết một bản tóm tắt 300 từ về startup AI mơ ước của bạn sẽ trông như thế nào và bao gồm các tiêu đề như "Vấn đề", "Cách tôi sẽ sử dụng AI", "Tác động" và tùy chọn một kế hoạch kinh doanh.

Nếu bạn đã hoàn thành nhiệm vụ này, bạn thậm chí có thể sẵn sàng để ứng tuyển vào chương trình ươm tạo của Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) chúng tôi cung cấp tín dụng cho cả Azure, OpenAI, tư vấn và nhiều hơn nữa, hãy xem qua!

## Kiểm tra kiến thức

Điều gì đúng về mô hình ngôn ngữ lớn?

1. Bạn nhận được phản hồi giống hệt nhau mỗi lần.
1. Nó làm mọi thứ hoàn hảo, tuyệt vời trong việc cộng số, sản xuất mã hoạt động, v.v.
1. Phản hồi có thể thay đổi mặc dù sử dụng cùng một prompt. Nó cũng rất tốt trong việc cung cấp cho bạn một bản nháp đầu tiên của một thứ gì đó, dù là văn bản hay mã. Nhưng bạn cần cải thiện kết quả.

A: 3, một LLM là không xác định, phản hồi thay đổi, tuy nhiên, bạn có thể kiểm soát sự biến đổi của nó thông qua một cài đặt nhiệt độ. Bạn cũng không nên mong đợi nó làm mọi thứ hoàn hảo, nó ở đây để làm công việc nặng nhọc cho bạn, điều này thường có nghĩa là bạn nhận được một nỗ lực đầu tiên tốt về một thứ gì đó mà bạn cần cải thiện dần.

## Làm tốt lắm! Tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

Hãy đến với Bài học 2 nơi chúng ta sẽ tìm hiểu cách [khám phá và so sánh các loại LLM khác nhau](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa của nó nên được coi là nguồn tài liệu có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.