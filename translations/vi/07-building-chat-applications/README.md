# Xây Dựng Ứng Dụng Trò Chuyện Dựa trên AI Sinh Tạo

[![Xây Dựng Ứng Dụng Trò Chuyện Dựa trên AI Sinh Tạo](../../../translated_images/vi/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Nhấn vào hình để xem video bài học)_

Bây giờ khi chúng ta đã xem cách xây dựng các ứng dụng tạo văn bản, hãy cùng tìm hiểu về các ứng dụng trò chuyện.

Các ứng dụng trò chuyện đã trở thành một phần không thể thiếu trong cuộc sống hàng ngày của chúng ta, không chỉ đơn thuần là phương tiện để trò chuyện bình thường. Chúng là phần thiết yếu trong dịch vụ khách hàng, hỗ trợ kỹ thuật và thậm chí các hệ thống tư vấn tinh vi. Có thể bạn đã được trợ giúp bởi một ứng dụng trò chuyện không lâu trước đây. Khi chúng ta tích hợp các công nghệ tiên tiến hơn như AI sinh tạo vào các nền tảng này, độ phức tạp tăng lên cùng với các thách thức.

Một số câu hỏi chúng ta cần giải đáp là:

- **Xây dựng ứng dụng**. Làm thế nào để chúng ta xây dựng hiệu quả và tích hợp liền mạch các ứng dụng AI này cho các trường hợp sử dụng cụ thể?
- **Giám sát**. Khi ứng dụng đã được triển khai, làm thế nào để giám sát và đảm bảo rằng các ứng dụng hoạt động với chất lượng cao nhất, cả về chức năng và tuân thủ [sáu nguyên tắc AI có trách nhiệm](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Khi chúng ta tiến sâu hơn vào thời đại được định hình bởi tự động hóa và tương tác giữa người và máy một cách liền mạch, việc hiểu cách AI sinh tạo biến đổi phạm vi, chiều sâu và khả năng thích ứng của các ứng dụng trò chuyện trở nên thiết yếu. Bài học này sẽ tìm hiểu các khía cạnh kiến trúc hỗ trợ hệ thống phức tạp này, đi sâu vào các phương pháp điều chỉnh tinh cho các nhiệm vụ chuyên môn, và đánh giá các chỉ số cùng các cân nhắc liên quan để đảm bảo triển khai AI có trách nhiệm.

## Giới Thiệu

Bài học này bao gồm:

- Kỹ thuật để xây dựng và tích hợp hiệu quả các ứng dụng trò chuyện.
- Cách áp dụng tùy chỉnh và điều chỉnh tinh cho các ứng dụng.
- Chiến lược và cân nhắc để giám sát hiệu quả các ứng dụng trò chuyện.

## Mục Tiêu Học Tập

Đến cuối bài học, bạn sẽ có thể:

- Mô tả các cân nhắc để xây dựng và tích hợp ứng dụng trò chuyện vào các hệ thống hiện có.
- Tùy chỉnh ứng dụng trò chuyện cho các trường hợp sử dụng cụ thể.
- Xác định các chỉ số chính và cân nhắc để giám sát và duy trì chất lượng các ứng dụng trò chuyện được hỗ trợ bởi AI.
- Đảm bảo các ứng dụng trò chuyện tận dụng AI một cách có trách nhiệm.

## Tích Hợp AI Sinh Tạo vào Ứng Dụng Trò Chuyện

Nâng cao các ứng dụng trò chuyện qua AI sinh tạo không chỉ là làm cho chúng thông minh hơn; mà còn là tối ưu hóa kiến trúc, hiệu suất và giao diện người dùng để mang lại trải nghiệm chất lượng. Điều này bao gồm việc điều tra các nền tảng kiến trúc, tích hợp API và các cân nhắc giao diện người dùng. Phần này nhằm cung cấp cho bạn một lộ trình chi tiết để điều hướng các lĩnh vực phức tạp này, dù bạn đang kết nối chúng vào các hệ thống hiện có hay xây dựng chúng như các nền tảng độc lập.

Đến cuối phần này, bạn sẽ được trang bị chuyên môn cần thiết để xây dựng và tích hợp các ứng dụng trò chuyện một cách hiệu quả.

### Chatbot hay Ứng dụng Trò chuyện?

Trước khi chúng ta đi sâu vào xây dựng các ứng dụng trò chuyện, hãy so sánh 'chatbots' với 'ứng dụng trò chuyện được hỗ trợ bởi AI,' vốn phục vụ các vai trò và chức năng khác biệt. Mục đích chính của chatbot là tự động hóa các tác vụ trò chuyện cụ thể, như trả lời các câu hỏi thường gặp hoặc theo dõi đơn hàng. Nó thường được điều khiển bởi logic dựa trên quy tắc hoặc các thuật toán AI phức tạp. Ngược lại, một ứng dụng trò chuyện được hỗ trợ bởi AI là một môi trường rộng lớn hơn nhiều được thiết kế để hỗ trợ nhiều hình thức giao tiếp kỹ thuật số, như trò chuyện văn bản, thoại, và video giữa người dùng. Đặc điểm nổi bật là tích hợp một mô hình AI sinh tạo mô phỏng các cuộc trò chuyện tinh tế, giống con người, tạo phản hồi dựa trên nhiều đầu vào và dấu hiệu ngữ cảnh khác nhau. Một ứng dụng trò chuyện sử dụng AI sinh tạo có thể tham gia vào các cuộc thảo luận mở, thích ứng với bối cảnh hội thoại thay đổi, và thậm chí tạo ra các đoạn đối thoại sáng tạo hay phức tạp.

Bảng dưới đây phác thảo những điểm khác biệt và tương đồng chính để giúp chúng ta hiểu vai trò đặc trưng của từng loại trong giao tiếp kỹ thuật số.

| Chatbot                               | Ứng Dụng Trò Chuyện Dựa trên AI Sinh Tạo                        |
| ------------------------------------- | --------------------------------------                           |
| Tập Trung Nhiệm Vụ và dựa trên quy tắc | Nhận Thức Ngữ Cảnh                                               |
| Thường tích hợp vào các hệ thống lớn hơn | Có thể chứa một hoặc nhiều chatbot                                |
| Giới hạn trong các chức năng được lập trình | Bao gồm các mô hình AI sinh tạo                                   |
| Tương tác chuyên biệt & có cấu trúc        | Có khả năng thảo luận mở rộng trên nhiều chủ đề                   |

### Tận dụng các chức năng dựng sẵn với SDKs và APIs

Khi xây dựng một ứng dụng trò chuyện, bước đầu tiên tuyệt vời là đánh giá những gì đã có sẵn. Sử dụng SDK và API để xây dựng các ứng dụng trò chuyện là một chiến lược có lợi vì nhiều lý do. Khi tích hợp các SDK và API được tài liệu hóa tốt, bạn đang định vị chiến lược ứng dụng để thành công lâu dài, giải quyết các vấn đề về khả năng mở rộng và bảo trì.

- **Đẩy nhanh quá trình phát triển và giảm chi phí**: Dựa vào các chức năng dựng sẵn thay vì xây dựng tốn kém cho phép bạn tập trung vào các khía cạnh khác của ứng dụng mà bạn thấy quan trọng hơn, như logic kinh doanh.
- **Hiệu suất tốt hơn**: Khi xây dựng chức năng từ đầu, bạn sẽ tự hỏi "Nó mở rộng được như thế nào? Ứng dụng này có xử lý được lượng người dùng đột ngột tăng không?" SDK và API được duy trì tốt thường có các giải pháp tích hợp cho những vấn đề này.
- **Dễ bảo trì hơn**: Việc cập nhật và cải tiến dễ quản lý hơn bởi hầu hết API và SDK chỉ cần cập nhật thư viện khi có phiên bản mới.
- **Tiếp cận công nghệ tiên tiến**: Tận dụng các mô hình đã được tối ưu và huấn luyện trên bộ dữ liệu rộng lớn mang lại khả năng xử lý ngôn ngữ tự nhiên cho ứng dụng của bạn.

Truy cập chức năng của SDK hoặc API thường liên quan đến việc lấy quyền sử dụng dịch vụ, thường thông qua việc sử dụng một khóa hoặc token xác thực độc nhất. Chúng ta sẽ sử dụng Thư viện Python của OpenAI để khám phá ví dụ này. Bạn cũng có thể thử trên chính mình trong [notebook của OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) hoặc [notebook của Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) cho bài học này.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Ví dụ trên sử dụng mô hình GPT-5 mini với API phản hồi để hoàn thành lệnh nhắc, nhưng lưu ý rằng khóa API được đặt trước khi thực hiện. Bạn sẽ nhận được lỗi nếu không đặt khóa.

## Trải Nghiệm Người Dùng (UX)

Các nguyên tắc UX chung được áp dụng cho các ứng dụng trò chuyện, nhưng dưới đây là một số cân nhắc bổ sung trở nên đặc biệt quan trọng do các thành phần máy học liên quan.

- **Cơ chế xử lý sự mơ hồ**: Các mô hình AI sinh tạo đôi khi tạo ra câu trả lời mơ hồ. Một tính năng cho phép người dùng yêu cầu làm rõ có thể hữu ích nếu họ gặp phải vấn đề này.
- **Giữ lại ngữ cảnh**: Các mô hình AI sinh tạo tiên tiến có khả năng nhớ bối cảnh trong cuộc trò chuyện, điều này có thể là tài sản cần thiết cho trải nghiệm người dùng. Cho phép người dùng kiểm soát và quản lý ngữ cảnh nâng cao trải nghiệm nhưng cũng đặt ra rủi ro giữ thông tin nhạy cảm của người dùng. Cần cân nhắc về thời gian lưu trữ thông tin, như giới thiệu chính sách lưu trữ, để cân bằng giữa nhu cầu ngữ cảnh và quyền riêng tư.
- **Cá nhân hóa**: Với khả năng học và thích ứng, các mô hình AI cung cấp trải nghiệm cá nhân hóa cho người dùng. Tùy chỉnh trải nghiệm thông qua tính năng hồ sơ người dùng không chỉ làm người dùng cảm thấy được hiểu mà còn hỗ trợ họ tìm câu trả lời cụ thể, tạo tương tác hiệu quả và hài lòng hơn.

Một ví dụ về cá nhân hóa là cài đặt "Hướng dẫn tùy chỉnh" trong ChatGPT của OpenAI. Nó cho phép bạn cung cấp thông tin về bản thân có thể là ngữ cảnh quan trọng cho lệnh nhắc của bạn. Dưới đây là một ví dụ về hướng dẫn tùy chỉnh.

![Cài đặt Hướng dẫn Tùy chỉnh trong ChatGPT](../../../translated_images/vi/custom-instructions.b96f59aa69356fcf.webp)

"Hồ sơ" này hướng ChatGPT tạo kế hoạch bài học về danh sách liên kết. Lưu ý rằng ChatGPT xem xét người dùng có thể muốn kế hoạch bài học sâu hơn dựa trên kinh nghiệm của cô ấy.

![Một lệnh nhắc trong ChatGPT về kế hoạch bài học danh sách liên kết](../../../translated_images/vi/lesson-plan-prompt.cc47c488cf1343df.webp)

### Khung Thông Báo Hệ Thống của Microsoft cho Mô hình Ngôn ngữ Lớn

[Microsoft đã cung cấp hướng dẫn](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) để viết thông báo hệ thống hiệu quả khi tạo phản hồi từ LLM chia thành 4 phần:

1. Xác định đối tượng của mô hình, cũng như khả năng và giới hạn của nó.
2. Xác định định dạng đầu ra của mô hình.
3. Cung cấp các ví dụ cụ thể minh họa hành vi mong muốn của mô hình.
4. Cung cấp các giới hạn hành vi bổ sung.

### Khả Năng Tiếp Cận

Dù người dùng có khiếm khuyết về thị giác, thính giác, vận động, hay nhận thức, một ứng dụng trò chuyện được thiết kế tốt nên có thể sử dụng được cho tất cả mọi người. Danh sách dưới đây phân tích các tính năng cụ thể nhằm nâng cao khả năng tiếp cận cho các dạng khiếm khuyết khác nhau.

- **Tính năng cho Khiếm Thị**: Chủ đề tương phản cao và chữ có thể thay đổi kích thước, tương thích với phần mềm đọc màn hình.
- **Tính năng cho Khiếm Thính**: Chức năng chuyển đổi văn bản thành giọng nói và ngược lại, cảnh báo âm thanh bằng tín hiệu hình ảnh.
- **Tính năng cho Khiếm Vận Động**: Hỗ trợ điều hướng bằng bàn phím, lệnh thoại.
- **Tính năng cho Khiếm Nhận Thức**: Các tùy chọn ngôn ngữ đơn giản hóa.

## Tùy Chỉnh và Điều Chỉnh Tinh cho Mô Hình Ngôn Ngữ Chuyên Ngành

Hãy tưởng tượng một ứng dụng trò chuyện hiểu thuật ngữ của công ty bạn và dự đoán các truy vấn cụ thể mà người dùng thường gặp. Có một vài cách tiếp cận đáng nhắc tới:

- **Tận dụng mô hình DSL**. DSL là viết tắt của domain specific language (ngôn ngữ chuyên ngành). Bạn có thể tận dụng mô hình DSL được huấn luyện trên một chuyên ngành để hiểu các khái niệm và kịch bản của nó.
- **Áp dụng điều chỉnh tinh**. Điều chỉnh tinh là quá trình đào tạo thêm mô hình của bạn với dữ liệu cụ thể.

## Tùy chỉnh: Sử dụng DSL

Tận dụng các mô hình ngôn ngữ chuyên ngành (DSL Models) có thể tăng cường sự tương tác của người dùng bằng cách cung cấp các tương tác chuyên môn, phù hợp ngữ cảnh. Đây là mô hình được huấn luyện hoặc điều chỉnh tinh để hiểu và tạo văn bản liên quan đến một lĩnh vực, ngành hay chủ đề cụ thể. Các lựa chọn sử dụng mô hình DSL có thể từ huấn luyện từ đầu, đến dùng những mô hình đã có qua SDK và API. Một lựa chọn khác là điều chỉnh tinh, tức là lấy mô hình đã được tiền huấn luyện và thích ứng nó cho một lĩnh vực cụ thể.

## Tùy chỉnh: Áp dụng điều chỉnh tinh

Điều chỉnh tinh thường được cân nhắc khi một mô hình tiền huấn luyện không đáp ứng đủ cho một lĩnh vực chuyên sâu hoặc nhiệm vụ cụ thể.

Ví dụ, các câu hỏi y tế rất phức tạp và cần nhiều ngữ cảnh. Khi một chuyên gia y tế chẩn đoán, họ dựa trên nhiều yếu tố như lối sống hay các bệnh lý tiền sử, và thậm chí dựa vào các bài báo y khoa gần đây để xác nhận chẩn đoán. Trong những tình huống tinh tế như vậy, một ứng dụng trò chuyện AI tổng quát không thể là nguồn đáng tin cậy.

### Tình huống: ứng dụng y tế

Hãy xem xét một ứng dụng trò chuyện thiết kế để hỗ trợ các chuyên gia y tế với việc cung cấp nhanh các hướng dẫn điều trị, tương tác thuốc, hoặc các kết quả nghiên cứu mới nhất.

Một mô hình tổng quát có thể đủ để trả lời các câu hỏi y tế cơ bản hoặc cung cấp lời khuyên chung, nhưng nó có thể gặp khó khăn với:

- **Các trường hợp đặc thù hoặc phức tạp cao**. Ví dụ, một bác sĩ thần kinh có thể hỏi, "Các hướng dẫn thực hành tốt nhất hiện nay về quản lý động kinh kháng thuốc ở trẻ em là gì?"
- **Thiếu những tiến bộ gần đây**. Mô hình tổng quát có thể khó cung cấp câu trả lời mới nhất tích hợp các tiến bộ gần đây trong thần kinh học và dược lý.

Trong những trường hợp như vậy, điều chỉnh tinh mô hình với bộ dữ liệu y tế chuyên ngành có thể cải thiện đáng kể khả năng xử lý các câu hỏi y tế phức tạp một cách chính xác và đáng tin cậy hơn. Điều này đòi hỏi có quyền truy cập bộ dữ liệu lớn và phù hợp phản ánh những thách thức và câu hỏi đặc trưng của lĩnh vực cần giải quyết.

## Cân Nhắc cho Trải Nghiệm Trò Chuyện AI Chất Lượng Cao

Phần này nêu ra các tiêu chí cho ứng dụng trò chuyện “chất lượng cao,” bao gồm việc thu thập các chỉ số có thể hành động và tuân thủ khung trách nhiệm trong việc sử dụng công nghệ AI.

### Các Chỉ Số Quan Trọng

Để duy trì hiệu suất chất lượng cao của ứng dụng, việc theo dõi các chỉ số và cân nhắc chính là điều cần thiết. Những phép đo này không chỉ đảm bảo chức năng của ứng dụng mà còn đánh giá chất lượng của mô hình AI và trải nghiệm người dùng. Dưới đây là danh sách các chỉ số cơ bản, AI, và trải nghiệm người dùng cần lưu ý.

| Chỉ Số                      | Định Nghĩa                                                                                                                | Cân Nhắc Dành Cho Nhà Phát Triển Trò Chuyện                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Thời gian hoạt động**       | Đo lường thời gian ứng dụng hoạt động và người dùng có thể truy cập được.                                               | Làm thế nào để bạn giảm thiểu thời gian chết?                      |
| **Thời gian phản hồi**        | Thời gian ứng dụng trả lời truy vấn của người dùng.                                                                     | Làm thế nào để tối ưu việc xử lý truy vấn nhằm cải thiện thời gian phản hồi? |
| **Độ chính xác**              | Tỷ lệ dự đoán đúng trên tổng số dự đoán đúng.                                                                            | Làm thế nào bạn xác minh độ chính xác của mô hình?                   |
| **Độ nhớ (Độ nhạy)**          | Tỷ lệ dự đoán đúng trên tổng số lượng thực sự dương tính.                                                                | Làm thế nào để bạn đo và cải thiện độ nhớ?                          |
| **Điểm F1**                  | Trung bình điều hòa của độ chính xác và độ nhớ, cân bằng giữa hai chỉ số.                                                  | Mục tiêu điểm F1 của bạn là gì? Làm sao bạn cân bằng giữa độ chính xác và độ nhớ? |
| **Mức rối rắm**               | Đo mức độ phù hợp giữa phân phối xác suất dự đoán của mô hình với phân phối dữ liệu thực tế.                               | Làm thế nào bạn giảm thiểu mức rối rắm?                             |
| **Chỉ số hài lòng người dùng** | Đo lường cảm nhận của người dùng về ứng dụng. Thường thu thập qua khảo sát.                                             | Bạn thu thập phản hồi người dùng bao lâu một lần? Bạn sẽ điều chỉnh dựa trên phản hồi thế nào? |
| **Tỷ lệ lỗi**                 | Tỷ lệ mà mô hình mắc sai lầm trong việc hiểu hoặc tạo đầu ra.                                                             | Bạn có chiến lược nào để giảm tỷ lệ lỗi?                           |
| **Chu kỳ huấn luyện lại**     | Tần suất mô hình được cập nhật để tích hợp dữ liệu và kiến thức mới.                                                    | Bạn huấn luyện lại mô hình bao lâu một lần? Điều gì kích hoạt chu kỳ huấn luyện lại? |

| **Phát Hiện Dị Thường**    | Công cụ và kỹ thuật để nhận diện các mẫu bất thường không phù hợp với hành vi mong đợi.                       | Bạn sẽ phản ứng như thế nào với các dị thường?                              |

### Triển Khai Các Thực Hành Trí Tuệ Nhân Tạo Có Trách Nhiệm Trong Ứng Dụng Chat

Cách tiếp cận của Microsoft đối với Trí Tuệ Nhân Tạo Có Trách Nhiệm đã xác định sáu nguyên tắc nên hướng dẫn việc phát triển và sử dụng AI. Dưới đây là các nguyên tắc, định nghĩa của chúng, và những điều nhà phát triển chat nên cân nhắc cùng lý do vì sao họ nên nghiêm túc thực hiện.

| Nguyên tắc             | Định nghĩa của Microsoft                             | Cân nhắc cho Nhà Phát Triển Chat                                      | Tại sao nó quan trọng                                                               |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Công bằng               | Hệ thống AI nên đối xử công bằng với tất cả mọi người.| Đảm bảo ứng dụng chat không phân biệt đối xử dựa trên dữ liệu người dùng.| Để xây dựng sự tin tưởng và bao gồm giữa người dùng; tránh các hệ quả pháp lý.    |
| Độ tin cậy và An toàn   | Hệ thống AI nên hoạt động tin cậy và an toàn.        | Triển khai kiểm thử và các biện pháp an toàn để giảm thiểu lỗi và rủi ro.| Đảm bảo sự hài lòng của người dùng và ngăn ngừa các nguy hại có thể xảy ra.       |
| Quyền riêng tư và An ninh| Hệ thống AI nên bảo mật và tôn trọng quyền riêng tư.  | Áp dụng mã hóa mạnh và các biện pháp bảo vệ dữ liệu.                   | Bảo vệ dữ liệu nhạy cảm của người dùng và tuân thủ luật bảo mật.                   |
| Tính bao gồm            | Hệ thống AI nên tạo điều kiện cho mọi người và thu hút họ.| Thiết kế giao diện người dùng thân thiện và dễ sử dụng cho nhiều đối tượng khác nhau.| Đảm bảo nhiều người có thể sử dụng ứng dụng một cách hiệu quả.                      |
| Tính minh bạch          | Hệ thống AI nên dễ hiểu.                             | Cung cấp tài liệu rõ ràng và lý do cho các câu trả lời AI.              | Người dùng có nhiều khả năng tin tưởng hệ thống hơn nếu họ hiểu cách các quyết định được đưa ra. |
| Trách nhiệm             | Con người cần chịu trách nhiệm về các hệ thống AI.   | Thiết lập quy trình rõ ràng để kiểm toán và cải thiện quyết định AI.   | Cho phép cải tiến liên tục và thực hiện các biện pháp khắc phục khi có sai sót.    |

## Bài Tập

Xem [assignment](../../../07-building-chat-applications/python). Nó sẽ hướng dẫn bạn qua một chuỗi các bài tập từ chạy các câu lệnh chat đầu tiên, đến phân loại và tóm tắt văn bản và nhiều hơn nữa. Lưu ý rằng các bài tập có sẵn bằng nhiều ngôn ngữ lập trình khác nhau!

## Làm Việc Tuyệt Vời! Tiếp Tục Hành Trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về Trí Tuệ Nhân Tạo Tạo Sinh!

Hãy chuyển sang Bài học 8 để xem cách bạn có thể bắt đầu [xây dựng các ứng dụng tìm kiếm](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->