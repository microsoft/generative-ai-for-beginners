<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T20:32:43+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "vi"
}
-->
# Bảo mật ứng dụng AI tạo sinh của bạn

[![Bảo mật ứng dụng AI tạo sinh của bạn](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.vi.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Giới thiệu

Bài học này sẽ đề cập đến:

- Bảo mật trong bối cảnh hệ thống AI.
- Các rủi ro và mối đe dọa phổ biến đối với hệ thống AI.
- Phương pháp và cân nhắc để bảo vệ hệ thống AI.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ hiểu được:

- Các mối đe dọa và rủi ro đối với hệ thống AI.
- Các phương pháp và thực hành phổ biến để bảo vệ hệ thống AI.
- Cách triển khai kiểm tra bảo mật có thể ngăn chặn kết quả không mong muốn và làm giảm lòng tin của người dùng.

## Bảo mật có ý nghĩa gì trong bối cảnh AI tạo sinh?

Khi công nghệ Trí tuệ Nhân tạo (AI) và Học máy (ML) ngày càng ảnh hưởng đến cuộc sống của chúng ta, việc bảo vệ không chỉ dữ liệu khách hàng mà còn cả chính các hệ thống AI trở nên vô cùng quan trọng. AI/ML ngày càng được sử dụng để hỗ trợ các quy trình ra quyết định có giá trị cao trong các ngành công nghiệp, nơi quyết định sai có thể dẫn đến hậu quả nghiêm trọng.

Dưới đây là những điểm chính cần xem xét:

- **Tác động của AI/ML**: AI/ML có ảnh hưởng lớn đến cuộc sống hàng ngày và do đó việc bảo vệ chúng trở nên thiết yếu.
- **Thách thức bảo mật**: Tác động mà AI/ML mang lại cần được chú ý đúng mức để giải quyết nhu cầu bảo vệ các sản phẩm dựa trên AI khỏi các cuộc tấn công tinh vi, dù là từ các nhóm troll hay tổ chức.
- **Vấn đề chiến lược**: Ngành công nghệ phải chủ động giải quyết các thách thức chiến lược để đảm bảo an toàn lâu dài cho khách hàng và bảo mật dữ liệu.

Ngoài ra, các mô hình Học máy phần lớn không thể phân biệt giữa đầu vào độc hại và dữ liệu bất thường vô hại. Một nguồn dữ liệu đào tạo đáng kể được lấy từ các tập dữ liệu công khai không được kiểm duyệt, không được quản lý, và mở cho sự đóng góp của bên thứ ba. Kẻ tấn công không cần phải xâm phạm các tập dữ liệu khi chúng có thể tự do đóng góp vào đó. Theo thời gian, dữ liệu độc hại có độ tin cậy thấp có thể trở thành dữ liệu đáng tin cậy có độ tin cậy cao, nếu cấu trúc/định dạng dữ liệu vẫn đúng.

Đây là lý do tại sao việc đảm bảo tính toàn vẹn và bảo vệ các kho dữ liệu mà mô hình của bạn sử dụng để đưa ra quyết định là rất quan trọng.

## Hiểu các mối đe dọa và rủi ro của AI

Trong bối cảnh AI và các hệ thống liên quan, nhiễm độc dữ liệu nổi bật như một mối đe dọa bảo mật đáng kể nhất hiện nay. Nhiễm độc dữ liệu xảy ra khi ai đó cố tình thay đổi thông tin được sử dụng để đào tạo AI, khiến nó đưa ra các quyết định sai lầm. Điều này xảy ra do thiếu các phương pháp phát hiện và giảm thiểu tiêu chuẩn, cùng với sự phụ thuộc của chúng ta vào các tập dữ liệu công khai không được tin cậy hoặc không được kiểm duyệt để đào tạo. Để duy trì tính toàn vẹn của dữ liệu và ngăn chặn quá trình đào tạo bị sai lệch, điều quan trọng là phải theo dõi nguồn gốc và dòng chảy của dữ liệu. Nếu không, câu nói cũ “rác vào, rác ra” sẽ trở thành sự thật, dẫn đến hiệu suất mô hình bị tổn hại.

Dưới đây là các ví dụ về cách nhiễm độc dữ liệu có thể ảnh hưởng đến mô hình của bạn:

1. **Đảo ngược nhãn**: Trong một nhiệm vụ phân loại nhị phân, kẻ tấn công cố tình đảo ngược nhãn của một phần nhỏ dữ liệu đào tạo. Ví dụ, các mẫu vô hại bị gán nhãn là độc hại, khiến mô hình học các liên kết sai.\
   **Ví dụ**: Bộ lọc thư rác phân loại sai email hợp lệ thành thư rác do nhãn bị thao túng.
2. **Nhiễm độc đặc trưng**: Kẻ tấn công tinh chỉnh các đặc trưng trong dữ liệu đào tạo để tạo ra sự thiên vị hoặc gây nhầm lẫn cho mô hình.\
   **Ví dụ**: Thêm các từ khóa không liên quan vào mô tả sản phẩm để thao túng hệ thống gợi ý.
3. **Tiêm dữ liệu**: Tiêm dữ liệu độc hại vào tập dữ liệu đào tạo để ảnh hưởng đến hành vi của mô hình.\
   **Ví dụ**: Thêm các đánh giá giả mạo của người dùng để làm sai lệch kết quả phân tích cảm xúc.
4. **Tấn công cửa sau**: Kẻ tấn công chèn một mẫu ẩn (cửa sau) vào dữ liệu đào tạo. Mô hình học cách nhận diện mẫu này và hành xử một cách độc hại khi bị kích hoạt.\
   **Ví dụ**: Hệ thống nhận diện khuôn mặt được đào tạo với hình ảnh có cửa sau, dẫn đến việc nhận diện sai một người cụ thể.

Tổ chức MITRE đã tạo ra [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), một cơ sở dữ liệu về các chiến thuật và kỹ thuật mà kẻ tấn công sử dụng trong các cuộc tấn công thực tế vào hệ thống AI.

> Ngày càng có nhiều lỗ hổng trong các hệ thống hỗ trợ AI, vì việc tích hợp AI làm tăng diện tấn công của các hệ thống hiện có vượt xa các cuộc tấn công mạng truyền thống. Chúng tôi đã phát triển ATLAS để nâng cao nhận thức về những lỗ hổng độc đáo và đang phát triển này, khi cộng đồng toàn cầu ngày càng tích hợp AI vào các hệ thống khác nhau. ATLAS được mô hình hóa theo khung MITRE ATT&CK® và các chiến thuật, kỹ thuật, và quy trình (TTPs) của nó bổ sung cho những gì trong ATT&CK.

Tương tự như khung MITRE ATT&CK®, được sử dụng rộng rãi trong an ninh mạng truyền thống để lập kế hoạch các kịch bản mô phỏng mối đe dọa tiên tiến, ATLAS cung cấp một tập hợp TTPs dễ dàng tìm kiếm, giúp hiểu rõ hơn và chuẩn bị cho việc phòng thủ trước các cuộc tấn công mới nổi.

Ngoài ra, Dự án Bảo mật Ứng dụng Web Mở (OWASP) đã tạo ra "[Danh sách Top 10](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" về các lỗ hổng nghiêm trọng nhất được tìm thấy trong các ứng dụng sử dụng LLMs. Danh sách này nêu bật các rủi ro từ các mối đe dọa như nhiễm độc dữ liệu đã đề cập ở trên cùng với các mối đe dọa khác như:

- **Tiêm lệnh nhắc**: một kỹ thuật mà kẻ tấn công thao túng Mô hình Ngôn ngữ Lớn (LLM) thông qua các đầu vào được tạo cẩn thận, khiến nó hành xử ngoài ý định ban đầu.
- **Lỗ hổng chuỗi cung ứng**: Các thành phần và phần mềm tạo nên các ứng dụng được sử dụng bởi LLM, chẳng hạn như các module Python hoặc tập dữ liệu bên ngoài, có thể bị xâm phạm dẫn đến kết quả không mong muốn, thiên vị được giới thiệu và thậm chí là các lỗ hổng trong cơ sở hạ tầng nền tảng.
- **Phụ thuộc quá mức**: LLMs có thể mắc lỗi và đã từng cung cấp kết quả không chính xác hoặc không an toàn. Trong một số trường hợp được ghi nhận, người dùng đã tin tưởng vào kết quả mà không kiểm tra, dẫn đến những hậu quả tiêu cực trong thực tế.

Rod Trent, Nhà truyền bá đám mây của Microsoft, đã viết một ebook miễn phí, [Phải học về bảo mật AI](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), đi sâu vào các mối đe dọa AI mới nổi này và cung cấp hướng dẫn chi tiết về cách tốt nhất để giải quyết các tình huống này.

## Kiểm tra bảo mật cho hệ thống AI và LLMs

Trí tuệ nhân tạo (AI) đang thay đổi nhiều lĩnh vực và ngành công nghiệp, mang lại những khả năng và lợi ích mới cho xã hội. Tuy nhiên, AI cũng đặt ra những thách thức và rủi ro đáng kể, chẳng hạn như quyền riêng tư dữ liệu, thiên vị, thiếu khả năng giải thích và khả năng bị lạm dụng. Do đó, điều quan trọng là phải đảm bảo rằng các hệ thống AI an toàn và có trách nhiệm, nghĩa là chúng tuân thủ các tiêu chuẩn đạo đức và pháp lý và có thể được người dùng và các bên liên quan tin tưởng.

Kiểm tra bảo mật là quá trình đánh giá bảo mật của một hệ thống AI hoặc LLM, bằng cách xác định và khai thác các lỗ hổng của chúng. Điều này có thể được thực hiện bởi các nhà phát triển, người dùng hoặc kiểm toán viên bên thứ ba, tùy thuộc vào mục đích và phạm vi của việc kiểm tra. Một số phương pháp kiểm tra bảo mật phổ biến nhất cho hệ thống AI và LLMs là:

- **Làm sạch dữ liệu**: Đây là quá trình loại bỏ hoặc ẩn danh thông tin nhạy cảm hoặc riêng tư khỏi dữ liệu đào tạo hoặc đầu vào của một hệ thống AI hoặc LLM. Làm sạch dữ liệu có thể giúp ngăn chặn rò rỉ dữ liệu và thao túng độc hại bằng cách giảm thiểu sự tiếp xúc của dữ liệu bí mật hoặc cá nhân.
- **Kiểm tra đối kháng**: Đây là quá trình tạo và áp dụng các ví dụ đối kháng vào đầu vào hoặc đầu ra của một hệ thống AI hoặc LLM để đánh giá độ bền và khả năng chống lại các cuộc tấn công đối kháng. Kiểm tra đối kháng có thể giúp xác định và giảm thiểu các lỗ hổng và điểm yếu của một hệ thống AI hoặc LLM có thể bị kẻ tấn công khai thác.
- **Xác minh mô hình**: Đây là quá trình xác minh tính đúng đắn và đầy đủ của các tham số hoặc kiến trúc mô hình của một hệ thống AI hoặc LLM. Xác minh mô hình có thể giúp phát hiện và ngăn chặn việc đánh cắp mô hình bằng cách đảm bảo rằng mô hình được bảo vệ và xác thực.
- **Xác thực đầu ra**: Đây là quá trình xác thực chất lượng và độ tin cậy của đầu ra của một hệ thống AI hoặc LLM. Xác thực đầu ra có thể giúp phát hiện và sửa chữa sự thao túng độc hại bằng cách đảm bảo rằng đầu ra là nhất quán và chính xác.

OpenAI, một công ty dẫn đầu trong lĩnh vực hệ thống AI, đã thiết lập một loạt các _đánh giá an toàn_ như một phần của sáng kiến mạng lưới red teaming, nhằm kiểm tra đầu ra của các hệ thống AI với hy vọng đóng góp vào sự an toàn của AI.

> Các đánh giá có thể dao động từ các bài kiểm tra Hỏi & Đáp đơn giản đến các mô phỏng phức tạp hơn. Dưới đây là các ví dụ cụ thể về các đánh giá được OpenAI phát triển để đánh giá hành vi của AI từ nhiều góc độ:

#### Thuyết phục

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): AI có thể khiến một hệ thống AI khác nói ra một từ bí mật tốt đến mức nào?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): AI có thể thuyết phục một hệ thống AI khác quyên góp tiền tốt đến mức nào?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): AI có thể ảnh hưởng đến sự ủng hộ của một hệ thống AI khác đối với một đề xuất chính trị tốt đến mức nào?

#### Steganography (tin nhắn ẩn)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): AI có thể truyền tin nhắn bí mật mà không bị hệ thống AI khác phát hiện tốt đến mức nào?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): AI có thể nén và giải nén tin nhắn để cho phép giấu tin nhắn bí mật tốt đến mức nào?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): AI có thể phối hợp với một hệ thống AI khác mà không cần giao tiếp trực tiếp tốt đến mức nào?

### Bảo mật AI

Điều quan trọng là chúng ta phải bảo vệ các hệ thống AI khỏi các cuộc tấn công độc hại, lạm dụng hoặc hậu quả không mong muốn. Điều này bao gồm việc thực hiện các bước để đảm bảo an toàn, độ tin cậy và sự đáng tin cậy của các hệ thống AI, chẳng hạn như:

- Bảo vệ dữ liệu và thuật toán được sử dụng để đào tạo và vận hành các mô hình AI
- Ngăn chặn truy cập trái phép, thao túng hoặc phá hoại các hệ thống AI
- Phát hiện và giảm thiểu thiên vị, phân biệt đối xử hoặc các vấn đề đạo đức trong các hệ thống AI
- Đảm bảo trách nhiệm, minh bạch và khả năng giải thích của các quyết định và hành động của AI
- Điều chỉnh mục tiêu và giá trị của các hệ thống AI với con người và xã hội

Bảo mật AI rất quan trọng để đảm bảo tính toàn vẹn, khả năng sẵn sàng và tính bảo mật của các hệ thống và dữ liệu AI. Một số thách thức và cơ hội của bảo mật AI là:

- **Cơ hội**: Tích hợp AI vào các chiến lược an ninh mạng vì nó có thể đóng vai trò quan trọng trong việc xác định các mối đe dọa và cải thiện thời gian phản ứng. AI có thể giúp tự động hóa và tăng cường việc phát hiện và giảm thiểu các cuộc tấn công mạng, chẳng hạn như phishing, malware hoặc ransomware.
- **Thách thức**: AI cũng có thể được sử dụng bởi kẻ xấu để thực hiện các cuộc tấn công tinh vi, chẳng hạn như tạo nội dung giả hoặc gây hiểu lầm, giả mạo người dùng hoặc khai thác các lỗ hổng trong hệ thống AI. Do đó, các nhà phát triển AI có trách nhiệm đặc biệt trong việc thiết kế các hệ thống mạnh mẽ và bền vững trước sự lạm dụng.

### Bảo vệ dữ liệu

LLMs có thể gây rủi ro cho quyền riêng tư và bảo mật của dữ liệu mà chúng sử dụng. Ví dụ, LLMs có thể ghi nhớ và rò rỉ thông tin nhạy cảm từ dữ liệu đào tạo của chúng, chẳng hạn như tên cá nhân, địa chỉ, mật khẩu hoặc số thẻ tín dụng. Chúng cũng có thể bị thao túng hoặc tấn công bởi các tác nhân độc hại muốn khai thác các lỗ hổng hoặc thiên vị của chúng. Do đó, điều quan trọng là phải nhận thức được những rủi ro này và thực hiện các biện pháp thích hợp để bảo vệ dữ liệu được sử dụng với LLMs. Có một số bước bạn có thể thực hiện để bảo vệ dữ liệu được sử dụng với LLMs. Các bước này bao gồm:

- **Hạn chế lượng và loại dữ liệu chia sẻ với LLMs**: Chỉ chia sẻ dữ liệu cần thiết và liên quan đến mục đích dự định, và tránh chia sẻ bất kỳ dữ liệu nào nhạy cảm, bí mật hoặc cá nhân. Người dùng cũng nên ẩn danh hoặc mã hóa dữ liệu mà họ chia sẻ với LLMs, chẳng hạn như bằng cách loại bỏ hoặc che giấu bất kỳ thông tin nhận dạng nào, hoặc sử dụng các kênh giao tiếp an toàn.
- **Xác minh dữ liệu mà LLMs tạo ra**: Luôn kiểm tra độ chính xác và chất lượng của đầu ra do LLMs tạo ra để đảm bảo chúng không chứa bất kỳ thông tin không mong muốn hoặc không phù hợp nào.
- **Báo cáo và cảnh báo về bất kỳ vi phạm dữ liệu hoặc sự cố nào**: Cảnh giác với bất kỳ hoạt động hoặc hành vi đáng ngờ hoặc bất thường nào từ LLMs, chẳng hạn như tạo ra các văn bản không liên quan, không chính xác, xúc phạm hoặc có hại. Điều này có thể là dấu hiệu của một vi phạm dữ liệu hoặc sự cố bảo mật.

Bảo mật, quản trị và tuân thủ dữ liệu là rất quan trọng đối với bất kỳ tổ chức nào muốn tận dụng sức mạnh của dữ liệu và AI trong môi trường đa đám mây. Bảo vệ và quản trị tất cả dữ liệu của bạn là một nhiệm vụ phức tạp và đa chiều. Bạn cần bảo vệ và quản trị các loại dữ liệu khác nhau (có cấu trúc, không có cấu trúc và dữ liệu được tạo bởi AI) ở các vị trí khác nhau trên nhiều đám mây, và bạn cần tính đến các quy định hiện tại và tương lai về bảo mật, quản trị và AI. Để bảo vệ dữ liệu của bạn, bạn cần áp dụng một số thực hành và biện pháp phòng ngừa tốt nhất, chẳng hạn như:

- Sử dụng các dịch vụ hoặc nền tảng đám mây cung cấp các tính năng bảo vệ và bảo mật dữ liệu.
- Sử dụng các công cụ
Việc mô phỏng các mối đe dọa thực tế hiện được coi là một thực hành tiêu chuẩn trong việc xây dựng các hệ thống AI có khả năng chống chịu bằng cách sử dụng các công cụ, chiến thuật, quy trình tương tự để xác định rủi ro đối với hệ thống và kiểm tra phản ứng của người bảo vệ.

> Thực hành red teaming AI đã phát triển để mang ý nghĩa rộng hơn: nó không chỉ bao gồm việc kiểm tra các lỗ hổng bảo mật mà còn bao gồm việc kiểm tra các lỗi hệ thống khác, chẳng hạn như việc tạo ra nội dung có khả năng gây hại. Các hệ thống AI đi kèm với những rủi ro mới, và red teaming là cốt lõi để hiểu những rủi ro mới đó, chẳng hạn như tiêm lệnh (prompt injection) và tạo nội dung không có cơ sở. - [Microsoft AI Red Team xây dựng tương lai AI an toàn hơn](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Hướng dẫn và tài nguyên cho red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.vi.png)]()

Dưới đây là những thông tin chính đã định hình chương trình AI Red Team của Microsoft.

1. **Phạm vi mở rộng của Red Teaming AI:**
   Red teaming AI hiện bao gồm cả kết quả về bảo mật và AI có trách nhiệm (RAI). Truyền thống, red teaming tập trung vào các khía cạnh bảo mật, coi mô hình như một vector (ví dụ: đánh cắp mô hình cơ bản). Tuy nhiên, các hệ thống AI giới thiệu các lỗ hổng bảo mật mới (ví dụ: tiêm lệnh, nhiễm độc), đòi hỏi sự chú ý đặc biệt. Ngoài bảo mật, red teaming AI cũng kiểm tra các vấn đề về công bằng (ví dụ: định kiến) và nội dung có hại (ví dụ: tôn vinh bạo lực). Việc xác định sớm các vấn đề này cho phép ưu tiên đầu tư vào phòng thủ.

2. **Thất bại do ác ý và vô ý:**
   Red teaming AI xem xét các thất bại từ cả góc độ ác ý và vô ý. Ví dụ, khi red teaming Bing mới, chúng tôi không chỉ khám phá cách các đối thủ ác ý có thể làm suy yếu hệ thống mà còn cách người dùng thông thường có thể gặp phải nội dung có vấn đề hoặc gây hại. Không giống như red teaming bảo mật truyền thống, chủ yếu tập trung vào các tác nhân ác ý, red teaming AI tính đến một phạm vi rộng hơn về các nhân vật và các thất bại tiềm năng.

3. **Tính chất động của các hệ thống AI:**
   Các ứng dụng AI liên tục phát triển. Trong các ứng dụng mô hình ngôn ngữ lớn, các nhà phát triển thích nghi với các yêu cầu thay đổi. Red teaming liên tục đảm bảo sự cảnh giác và thích nghi với các rủi ro đang phát triển.

Red teaming AI không phải là toàn diện và nên được coi là một động thái bổ sung cho các biện pháp kiểm soát khác như [kiểm soát truy cập dựa trên vai trò (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) và các giải pháp quản lý dữ liệu toàn diện. Nó được thiết kế để bổ sung chiến lược bảo mật tập trung vào việc sử dụng các giải pháp AI an toàn và có trách nhiệm, đồng thời tính đến quyền riêng tư và bảo mật, trong khi cố gắng giảm thiểu định kiến, nội dung có hại và thông tin sai lệch có thể làm giảm niềm tin của người dùng.

Dưới đây là danh sách các tài liệu đọc thêm có thể giúp bạn hiểu rõ hơn cách red teaming có thể giúp xác định và giảm thiểu rủi ro trong các hệ thống AI của bạn:

- [Lập kế hoạch red teaming cho các mô hình ngôn ngữ lớn (LLMs) và các ứng dụng của chúng](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Mạng lưới Red Teaming của OpenAI là gì?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [Red Teaming AI - Một thực hành quan trọng để xây dựng các giải pháp AI an toàn và có trách nhiệm hơn](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Cảnh quan mối đe dọa đối với các hệ thống trí tuệ nhân tạo)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), một cơ sở kiến thức về các chiến thuật và kỹ thuật được các đối thủ sử dụng trong các cuộc tấn công thực tế vào các hệ thống AI.

## Kiểm tra kiến thức

Phương pháp nào có thể tốt để duy trì tính toàn vẹn của dữ liệu và ngăn chặn việc sử dụng sai?

1. Có các kiểm soát mạnh mẽ dựa trên vai trò đối với quyền truy cập dữ liệu và quản lý dữ liệu  
1. Thực hiện và kiểm tra việc gán nhãn dữ liệu để ngăn chặn việc trình bày sai hoặc sử dụng sai dữ liệu  
1. Đảm bảo cơ sở hạ tầng AI của bạn hỗ trợ lọc nội dung  

A:1, Mặc dù cả ba đều là những khuyến nghị tuyệt vời, việc đảm bảo rằng bạn đang cấp quyền truy cập dữ liệu phù hợp cho người dùng sẽ giúp ngăn chặn việc thao túng và trình bày sai dữ liệu được sử dụng bởi LLMs.

## 🚀 Thử thách

Tìm hiểu thêm về cách bạn có thể [quản lý và bảo vệ thông tin nhạy cảm](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) trong thời đại AI.

## Hoàn thành tốt, Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học về AI tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI tạo sinh!

Hãy chuyển sang Bài học 14, nơi chúng ta sẽ tìm hiểu về [Vòng đời ứng dụng AI tạo sinh](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.