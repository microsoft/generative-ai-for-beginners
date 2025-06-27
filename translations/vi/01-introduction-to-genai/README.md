<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T09:59:12+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "vi"
}
-->
# Giới thiệu về AI Tạo Sinh và Mô Hình Ngôn Ngữ Lớn

_(Nhấn vào hình ảnh trên để xem video của bài học này)_

AI Tạo Sinh là trí tuệ nhân tạo có khả năng tạo ra văn bản, hình ảnh và các loại nội dung khác. Điều làm cho nó trở thành một công nghệ tuyệt vời là nó dân chủ hóa AI, bất kỳ ai cũng có thể sử dụng nó chỉ với một đoạn văn bản, một câu viết bằng ngôn ngữ tự nhiên. Bạn không cần phải học một ngôn ngữ như Java hay SQL để làm được điều gì đó có giá trị, tất cả những gì bạn cần là sử dụng ngôn ngữ của mình, nói ra điều bạn muốn và AI sẽ đưa ra gợi ý. Ứng dụng và tác động của điều này rất lớn, bạn có thể viết hoặc hiểu báo cáo, viết ứng dụng và nhiều hơn nữa, tất cả chỉ trong vài giây.

Trong chương trình học này, chúng ta sẽ khám phá cách mà công ty khởi nghiệp của chúng tôi sử dụng AI Tạo Sinh để mở ra các kịch bản mới trong thế giới giáo dục và cách chúng tôi giải quyết những thách thức không thể tránh khỏi liên quan đến các tác động xã hội của việc ứng dụng và những hạn chế của công nghệ.

## Giới thiệu

Bài học này sẽ bao gồm:

- Giới thiệu về kịch bản kinh doanh: ý tưởng và sứ mệnh của công ty khởi nghiệp của chúng tôi.
- AI Tạo Sinh và cách chúng tôi đạt đến bối cảnh công nghệ hiện tại.
- Cách hoạt động bên trong của một mô hình ngôn ngữ lớn.
- Các khả năng chính và trường hợp sử dụng thực tế của Mô Hình Ngôn Ngữ Lớn.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ hiểu:

- AI Tạo Sinh là gì và Mô Hình Ngôn Ngữ Lớn hoạt động như thế nào.
- Cách bạn có thể tận dụng các mô hình ngôn ngữ lớn cho các trường hợp sử dụng khác nhau, với trọng tâm là các kịch bản giáo dục.

## Kịch bản: công ty khởi nghiệp giáo dục của chúng tôi

Trí tuệ Nhân tạo Tạo Sinh (AI) đại diện cho đỉnh cao của công nghệ AI, đẩy lùi giới hạn của những gì từng được cho là không thể. Các mô hình AI Tạo Sinh có nhiều khả năng và ứng dụng, nhưng trong chương trình học này, chúng ta sẽ khám phá cách nó đang cách mạng hóa giáo dục thông qua một công ty khởi nghiệp hư cấu. Chúng tôi sẽ gọi công ty khởi nghiệp này là _công ty khởi nghiệp của chúng tôi_. Công ty khởi nghiệp của chúng tôi hoạt động trong lĩnh vực giáo dục với tuyên bố sứ mệnh đầy tham vọng là

> _cải thiện khả năng tiếp cận trong học tập, trên quy mô toàn cầu, đảm bảo quyền tiếp cận giáo dục công bằng và cung cấp trải nghiệm học tập cá nhân hóa cho từng người học, theo nhu cầu của họ_.

Đội ngũ công ty khởi nghiệp của chúng tôi biết rằng chúng tôi sẽ không thể đạt được mục tiêu này nếu không tận dụng một trong những công cụ mạnh mẽ nhất của thời hiện đại – Mô Hình Ngôn Ngữ Lớn (LLMs).

AI Tạo Sinh được kỳ vọng sẽ cách mạng hóa cách chúng ta học và dạy ngày nay, với học sinh có trong tay các giáo viên ảo 24 giờ một ngày cung cấp lượng thông tin và ví dụ khổng lồ, và giáo viên có thể tận dụng các công cụ sáng tạo để đánh giá học sinh của mình và đưa ra phản hồi.

Để bắt đầu, hãy định nghĩa một số khái niệm và thuật ngữ cơ bản mà chúng ta sẽ sử dụng trong suốt chương trình học.

## Chúng ta đã có AI Tạo Sinh như thế nào?

Mặc dù _hype_ phi thường được tạo ra gần đây bởi thông báo về các mô hình AI Tạo Sinh, công nghệ này đã được phát triển hàng thập kỷ, với những nỗ lực nghiên cứu đầu tiên từ những năm 60. Chúng ta hiện đang ở một điểm mà AI có khả năng nhận thức của con người, như hội thoại được thể hiện qua [OpenAI ChatGPT](https://openai.com/chatgpt) hoặc [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), cũng sử dụng một mô hình GPT cho các cuộc hội thoại tìm kiếm trên web của Bing.

Quay lại một chút, các nguyên mẫu AI đầu tiên bao gồm các chatbot đánh máy, dựa vào một cơ sở kiến thức được trích xuất từ một nhóm chuyên gia và được biểu diễn vào một máy tính. Các câu trả lời trong cơ sở kiến thức được kích hoạt bởi các từ khóa xuất hiện trong văn bản đầu vào. Tuy nhiên, nhanh chóng nhận ra rằng phương pháp như vậy, sử dụng các chatbot đánh máy, không mở rộng tốt.

### Cách tiếp cận thống kê với AI: Học máy

Một bước ngoặt đã đến trong những năm 90, với việc áp dụng cách tiếp cận thống kê để phân tích văn bản. Điều này dẫn đến sự phát triển của các thuật toán mới – được gọi là học máy – có khả năng học các mẫu từ dữ liệu mà không cần được lập trình rõ ràng. Cách tiếp cận này cho phép máy móc mô phỏng sự hiểu biết ngôn ngữ của con người: một mô hình thống kê được huấn luyện trên các cặp văn bản-nhãn, cho phép mô hình phân loại văn bản đầu vào không xác định với một nhãn được định trước đại diện cho ý định của thông điệp.

### Mạng nơ-ron và trợ lý ảo hiện đại

Trong những năm gần đây, sự tiến hóa công nghệ của phần cứng, có khả năng xử lý lượng dữ liệu lớn hơn và tính toán phức tạp hơn, đã khuyến khích nghiên cứu trong AI, dẫn đến sự phát triển của các thuật toán học máy tiên tiến được gọi là mạng nơ-ron hoặc thuật toán học sâu.

Mạng nơ-ron (đặc biệt là Mạng nơ-ron Tái diễn – RNNs) đã tăng cường đáng kể xử lý ngôn ngữ tự nhiên, cho phép biểu diễn ý nghĩa của văn bản theo cách có ý nghĩa hơn, đánh giá cao ngữ cảnh của một từ trong một câu.

Đây là công nghệ đã cung cấp năng lượng cho các trợ lý ảo ra đời trong thập kỷ đầu tiên của thế kỷ mới, rất thành thạo trong việc diễn giải ngôn ngữ của con người, xác định nhu cầu và thực hiện một hành động để đáp ứng nó – như trả lời bằng một kịch bản được định trước hoặc tiêu thụ một dịch vụ bên thứ ba.

### Ngày nay, AI Tạo Sinh

Vậy đó là cách chúng ta đến với AI Tạo Sinh ngày nay, có thể được xem như một tập hợp con của học sâu.

Sau hàng thập kỷ nghiên cứu trong lĩnh vực AI, một kiến trúc mô hình mới – được gọi là _Transformer_ – đã vượt qua các giới hạn của RNNs, có khả năng nhận được các chuỗi văn bản dài hơn nhiều làm đầu vào. Transformers dựa trên cơ chế chú ý, cho phép mô hình đưa ra các trọng số khác nhau cho các đầu vào mà nó nhận được, ‘chú ý nhiều hơn’ nơi thông tin quan trọng nhất tập trung, bất kể thứ tự của chúng trong chuỗi văn bản.

Hầu hết các mô hình AI Tạo Sinh gần đây – còn được gọi là Mô Hình Ngôn Ngữ Lớn (LLMs), vì chúng làm việc với đầu vào và đầu ra dạng văn bản – thực sự dựa trên kiến trúc này. Điều thú vị về các mô hình này – được huấn luyện trên một lượng lớn dữ liệu chưa được gắn nhãn từ các nguồn đa dạng như sách, bài báo và trang web – là chúng có thể được điều chỉnh để thực hiện nhiều nhiệm vụ khác nhau và tạo ra văn bản đúng ngữ pháp với một chút sáng tạo. Vì vậy, không chỉ chúng đã tăng cường đáng kể khả năng của một máy móc để ‘hiểu’ một văn bản đầu vào, mà chúng còn cho phép khả năng tạo ra một phản hồi gốc bằng ngôn ngữ con người.

## Mô hình ngôn ngữ lớn hoạt động như thế nào?

Trong chương tiếp theo, chúng ta sẽ khám phá các loại mô hình AI Tạo Sinh khác nhau, nhưng bây giờ hãy cùng xem cách mà các mô hình ngôn ngữ lớn hoạt động, với trọng tâm là các mô hình OpenAI GPT (Transformer Được Huấn Luyện Trước Để Tạo Sinh).

- **Tokenizer, văn bản thành số**: Mô hình Ngôn Ngữ Lớn nhận một văn bản làm đầu vào và tạo ra một văn bản làm đầu ra. Tuy nhiên, là các mô hình thống kê, chúng hoạt động tốt hơn nhiều với số hơn là chuỗi văn bản. Đó là lý do tại sao mọi đầu vào vào mô hình được xử lý bởi một tokenizer, trước khi được sử dụng bởi mô hình cốt lõi. Một token là một đoạn văn bản – bao gồm một số lượng ký tự biến đổi, vì vậy nhiệm vụ chính của tokenizer là chia đầu vào thành một mảng các token. Sau đó, mỗi token được ánh xạ với một chỉ số token, là mã hóa số nguyên của đoạn văn bản gốc.

- **Dự đoán các token đầu ra**: Với n token làm đầu vào (với max n thay đổi từ mô hình này sang mô hình khác), mô hình có khả năng dự đoán một token làm đầu ra. Token này sau đó được đưa vào đầu vào của lần lặp tiếp theo, theo một mẫu cửa sổ mở rộng, cho phép một trải nghiệm người dùng tốt hơn khi nhận được một (hoặc nhiều) câu làm câu trả lời. Điều này giải thích tại sao, nếu bạn đã từng chơi với ChatGPT, bạn có thể nhận thấy rằng đôi khi nó có vẻ như dừng lại giữa một câu.

- **Quá trình lựa chọn, phân phối xác suất**: Token đầu ra được chọn bởi mô hình theo xác suất xuất hiện của nó sau chuỗi văn bản hiện tại. Điều này là do mô hình dự đoán một phân phối xác suất trên tất cả các ‘token tiếp theo’ có thể, được tính toán dựa trên việc huấn luyện của nó. Tuy nhiên, không phải lúc nào token có xác suất cao nhất cũng được chọn từ phân phối kết quả. Một mức độ ngẫu nhiên được thêm vào sự lựa chọn này, theo cách mà mô hình hành động không theo định trước - chúng ta không nhận được kết quả giống hệt nhau cho cùng một đầu vào. Mức độ ngẫu nhiên này được thêm vào để mô phỏng quá trình tư duy sáng tạo và nó có thể được điều chỉnh bằng một tham số mô hình gọi là nhiệt độ.

## Công ty khởi nghiệp của chúng tôi có thể tận dụng Mô Hình Ngôn Ngữ Lớn như thế nào?

Bây giờ chúng ta đã hiểu rõ hơn về cách hoạt động bên trong của một mô hình ngôn ngữ lớn, hãy xem một số ví dụ thực tế về những nhiệm vụ phổ biến nhất mà chúng có thể thực hiện khá tốt, với một cái nhìn đến kịch bản kinh doanh của chúng tôi. Chúng tôi đã nói rằng khả năng chính của một Mô Hình Ngôn Ngữ Lớn là _tạo ra văn bản từ đầu, bắt đầu từ một đầu vào văn bản, được viết bằng ngôn ngữ tự nhiên_.

Nhưng loại đầu vào và đầu ra văn bản nào?
Đầu vào của một mô hình ngôn ngữ lớn được gọi là một prompt, trong khi đầu ra được gọi là một completion, thuật ngữ chỉ cơ chế của mô hình tạo ra token tiếp theo để hoàn thành đầu vào hiện tại. Chúng ta sẽ đi sâu vào prompt là gì và cách thiết kế nó để tận dụng tối đa mô hình của chúng ta. Nhưng bây giờ, hãy chỉ nói rằng một prompt có thể bao gồm:

- Một **hướng dẫn** chỉ định loại đầu ra mà chúng ta mong đợi từ mô hình. Hướng dẫn này đôi khi có thể bao gồm một số ví dụ hoặc một số dữ liệu bổ sung.

  1. Tóm tắt một bài viết, sách, đánh giá sản phẩm và hơn thế nữa, cùng với việc trích xuất thông tin chi tiết từ dữ liệu chưa cấu trúc.
  
  2. Sáng tạo ý tưởng và thiết kế một bài viết, một bài luận, một bài tập hoặc nhiều hơn thế.

- Một **câu hỏi**, được hỏi dưới dạng một cuộc trò chuyện với một tác nhân.

- Một đoạn **văn bản để hoàn thành**, mà ngầm hiểu là một yêu cầu hỗ trợ viết.

- Một đoạn **mã** cùng với yêu cầu giải thích và tài liệu hóa nó, hoặc một bình luận yêu cầu tạo ra một đoạn mã thực hiện một nhiệm vụ cụ thể.

Các ví dụ trên khá đơn giản và không nhằm mục đích trình diễn toàn diện khả năng của Mô Hình Ngôn Ngữ Lớn. Chúng nhằm mục đích cho thấy tiềm năng của việc sử dụng AI Tạo Sinh, đặc biệt nhưng không giới hạn trong các bối cảnh giáo dục.

Ngoài ra, đầu ra của một mô hình AI Tạo Sinh không hoàn hảo và đôi khi sự sáng tạo của mô hình có thể chống lại nó, dẫn đến một đầu ra là sự kết hợp của các từ mà người dùng có thể diễn giải như một sự bóp méo thực tế, hoặc có thể là xúc phạm. AI Tạo Sinh không thông minh - ít nhất là trong định nghĩa toàn diện hơn về trí thông minh, bao gồm lý luận phê phán và sáng tạo hoặc trí thông minh cảm xúc; nó không phải là xác định, và nó không đáng tin cậy, vì những sự bịa đặt, chẳng hạn như các tham chiếu sai, nội dung và tuyên bố, có thể được kết hợp với thông tin đúng và được trình bày theo cách thuyết phục và tự tin. Trong các bài học tiếp theo, chúng ta sẽ đối phó với tất cả những hạn chế này và sẽ xem chúng ta có thể làm gì để giảm thiểu chúng.

## Bài tập

Bài tập của bạn là tìm hiểu thêm về [AI Tạo Sinh](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) và cố gắng xác định một lĩnh vực mà bạn sẽ thêm AI Tạo Sinh vào ngày hôm nay mà chưa có nó. Ảnh hưởng sẽ khác biệt như thế nào so với việc làm theo cách "cũ", bạn có thể làm điều gì đó mà trước đây bạn không thể, hoặc bạn có nhanh hơn không? Viết một tóm tắt 300 từ về công ty khởi nghiệp AI trong mơ của bạn sẽ trông như thế nào và bao gồm các tiêu đề như "Vấn đề", "Cách tôi sẽ sử dụng AI", "Ảnh hưởng" và tùy chọn một kế hoạch kinh doanh.

Nếu bạn đã làm bài tập này, bạn thậm chí có thể sẵn sàng để ứng tuyển vào vườn ươm của Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) chúng tôi cung cấp tín dụng cho cả Azure, OpenAI, tư vấn và nhiều hơn nữa, hãy kiểm tra!

## Kiểm tra kiến thức

Điều gì đúng về mô hình ngôn ngữ lớn?

1. Bạn nhận được phản hồi giống hệt nhau mỗi lần.
2. Nó làm mọi thứ hoàn hảo, giỏi trong việc cộng số, sản xuất mã hoạt động, v.v.
3. Phản hồi có thể thay đổi mặc dù sử dụng cùng một prompt. Nó cũng rất giỏi trong việc đưa ra bản nháp đầu tiên của một cái gì đó, dù là văn bản hay mã. Nhưng bạn cần cải thiện kết quả.

A: 3, một LLM không xác định, phản hồi thay đổi, tuy nhiên, bạn có thể kiểm soát độ biến thiên của nó thông qua cài đặt nhiệt độ. Bạn cũng không nên mong đợi nó làm mọi thứ hoàn hảo, nó ở đây để làm công việc nặng nhọc cho bạn mà thường có nghĩa là bạn có được một nỗ lực đầu tiên tốt về một cái gì đó mà bạn cần dần dần cải thiện.

## Làm tốt lắm! Tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học AI Tạo Sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức AI Tạo Sinh của bạn!

Hãy chuyển sang Bài học 2, nơi chúng ta sẽ xem cách [khám phá và so sánh các loại LLM khác nhau](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.