# Xây dựng Ứng dụng AI với Mã Thấp

[![Xây dựng Ứng dụng AI với Mã Thấp](../../../translated_images/vi/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Nhấp vào hình ảnh bên trên để xem video bài học này)_

## Giới thiệu

Giờ đây khi chúng ta đã học cách xây dựng các ứng dụng tạo hình ảnh, hãy nói về mã thấp. AI tạo sinh có thể được sử dụng cho nhiều lĩnh vực khác nhau bao gồm mã thấp, nhưng mã thấp là gì và làm thế nào chúng ta có thể thêm AI vào nó?

Việc xây dựng ứng dụng và giải pháp trở nên dễ dàng hơn cho lập trình viên truyền thống và cả những người không phải lập trình viên thông qua việc sử dụng Các Nền Tảng Phát Triển Mã Thấp. Các Nền Tảng Phát Triển Mã Thấp cho phép bạn xây dựng ứng dụng và giải pháp với ít hoặc không cần mã. Điều này đạt được bằng cách cung cấp môi trường phát triển trực quan cho phép bạn kéo và thả các thành phần để xây dựng ứng dụng và giải pháp. Điều này giúp bạn xây dựng ứng dụng và giải pháp nhanh hơn và ít tốn tài nguyên hơn. Trong bài học này, chúng ta sẽ đi sâu vào cách sử dụng Mã Thấp và cách nâng cao phát triển mã thấp với AI bằng cách sử dụng Power Platform.

Power Platform cung cấp cho các tổ chức cơ hội để trao quyền cho đội ngũ của họ xây dựng các giải pháp riêng thông qua môi trường mã thấp hoặc không cần mã trực quan. Môi trường này giúp đơn giản hóa quá trình xây dựng giải pháp. Với Power Platform, giải pháp có thể được xây dựng trong vài ngày hoặc tuần thay vì tháng hoặc năm. Power Platform bao gồm năm sản phẩm chính: Power Apps, Power Automate, Power BI, Power Pages và Copilot Studio.

Bài học này bao gồm:

- Giới thiệu về AI tạo sinh trong Power Platform
- Giới thiệu về Copilot và cách sử dụng nó
- Sử dụng AI tạo sinh để xây dựng ứng dụng và luồng trong Power Platform
- Hiểu các Mô hình AI trong Power Platform với AI Builder
- Xây dựng đại lý thông minh với Microsoft Copilot Studio

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Hiểu cách Copilot hoạt động trong Power Platform.

- Xây dựng Ứng dụng Theo dõi Bài tập Sinh viên cho khởi nghiệp giáo dục của chúng ta.

- Xây dựng Quy trình Xử lý Hóa đơn sử dụng AI để trích xuất thông tin từ hóa đơn.

- Áp dụng các thực hành tốt nhất khi sử dụng Mô hình AI Tạo văn bản với GPT.

- Hiểu Microsoft Copilot Studio là gì và cách xây dựng các đại lý thông minh với nó.

Các công cụ và công nghệ bạn sẽ sử dụng trong bài học này là:

- **Power Apps**, cho ứng dụng Theo dõi Bài tập Sinh viên, cung cấp môi trường phát triển mã thấp để xây dựng ứng dụng theo dõi, quản lý và tương tác với dữ liệu.

- **Dataverse**, để lưu trữ dữ liệu cho ứng dụng Theo dõi Bài tập Sinh viên, nơi Dataverse sẽ cung cấp nền tảng dữ liệu mã thấp để lưu trữ dữ liệu của ứng dụng.

- **Power Automate**, cho luồng Xử lý Hóa đơn, nơi bạn sẽ có môi trường phát triển mã thấp để xây dựng các luồng công việc tự động hóa quy trình Xử lý Hóa đơn.

- **AI Builder**, cho Mô hình AI Xử lý Hóa đơn, nơi bạn sẽ sử dụng các Mô hình AI được xây dựng sẵn để xử lý các hóa đơn cho khởi nghiệp của chúng ta.

## AI tạo sinh trong Power Platform

Nâng cao phát triển và ứng dụng mã thấp với AI tạo sinh là trọng tâm quan trọng của Power Platform. Mục tiêu là cho phép mọi người xây dựng ứng dụng, trang web, bảng điều khiển được hỗ trợ bởi AI và tự động hóa quy trình với AI, _mà không cần kỹ năng khoa học dữ liệu_. Mục tiêu này đạt được bằng cách tích hợp AI tạo sinh vào trải nghiệm phát triển mã thấp trong Power Platform dưới dạng Copilot và AI Builder.

### Cách hoạt động như thế nào?

Copilot là trợ lý AI cho phép bạn xây dựng các giải pháp Power Platform bằng cách mô tả yêu cầu của bạn qua một loạt các bước hội thoại sử dụng ngôn ngữ tự nhiên. Ví dụ, bạn có thể chỉ dẫn trợ lý AI của mình nói những trường nào ứng dụng sẽ sử dụng và nó sẽ tạo cả ứng dụng và mô hình dữ liệu nền tảng, hoặc bạn có thể chỉ định cách thiết lập một luồng trong Power Automate.

Bạn có thể sử dụng các chức năng do Copilot điều khiển như một tính năng trong màn hình ứng dụng để người dùng khám phá thông tin qua các tương tác hội thoại.

AI Builder là một khả năng AI mã thấp có trong Power Platform giúp bạn sử dụng các Mô hình AI để tự động hóa quy trình và dự đoán kết quả. Với AI Builder bạn có thể mang AI vào các ứng dụng và luồng của bạn kết nối với dữ liệu trong Dataverse hoặc các nguồn dữ liệu đám mây khác nhau, như SharePoint, OneDrive hoặc Azure.

Copilot có sẵn trong tất cả các sản phẩm Power Platform: Power Apps, Power Automate, Power BI, Power Pages và Copilot Studio (trước đây là Power Virtual Agents). AI Builder có trong Power Apps và Power Automate. Trong bài học này, chúng ta sẽ tập trung vào cách sử dụng Copilot và AI Builder trong Power Apps và Power Automate để xây dựng một giải pháp cho khởi nghiệp giáo dục của chúng ta.

### Copilot trong Power Apps

Là một phần của Power Platform, Power Apps cung cấp môi trường phát triển mã thấp để xây dựng ứng dụng theo dõi, quản lý và tương tác với dữ liệu. Đây là bộ dịch vụ phát triển ứng dụng với nền tảng dữ liệu có thể mở rộng và khả năng kết nối với dịch vụ đám mây cũng như dữ liệu tại chỗ. Power Apps cho phép bạn xây dựng ứng dụng chạy trên trình duyệt, máy tính bảng và điện thoại, và có thể chia sẻ với đồng nghiệp. Power Apps giúp người dùng tiếp cận phát triển ứng dụng với giao diện đơn giản, để mỗi người dùng doanh nghiệp hoặc lập trình viên chuyên nghiệp có thể xây dựng ứng dụng tùy chỉnh. Trải nghiệm phát triển ứng dụng cũng được nâng cao với AI tạo sinh qua Copilot.

Tính năng trợ lý AI copilot trong Power Apps cho phép bạn mô tả loại ứng dụng bạn cần và thông tin bạn muốn ứng dụng của mình theo dõi, thu thập hoặc hiển thị. Copilot sau đó sẽ tạo ra một ứng dụng Canvas phản hồi dựa trên mô tả của bạn. Bạn có thể tùy chỉnh ứng dụng để đáp ứng nhu cầu của mình. AI Copilot cũng tạo và gợi ý một Bảng Dataverse với các trường bạn cần để lưu trữ dữ liệu bạn muốn theo dõi cùng một số dữ liệu mẫu. Chúng ta sẽ tìm hiểu về Dataverse và cách bạn có thể sử dụng nó trong Power Apps trong bài học này sau. Bạn có thể tùy chỉnh bảng để đáp ứng yêu cầu của bạn bằng tính năng trợ lý AI Copilot qua các bước hội thoại. Tính năng này có sẵn ngay từ màn hình chính Power Apps.

### Copilot trong Power Automate

Là một phần của Power Platform, Power Automate cho phép người dùng tạo các luồng công việc tự động giữa các ứng dụng và dịch vụ. Nó giúp tự động hóa các quy trình công việc lặp đi lặp lại như giao tiếp, thu thập dữ liệu và phê duyệt quyết định. Giao diện đơn giản của nó cho phép người dùng ở mọi trình độ kỹ thuật (từ người mới đến lập trình viên dày dạn) tự động hóa công việc. Trải nghiệm phát triển quy trình cũng được nâng cao với AI tạo sinh qua Copilot.

Tính năng trợ lý AI copilot trong Power Automate cho phép bạn mô tả loại luồng bạn cần và những hành động mà luồng của bạn phải thực hiện. Copilot sau đó tạo ra một luồng dựa trên mô tả của bạn. Bạn có thể tùy chỉnh luồng để đáp ứng nhu cầu của mình. AI Copilot cũng tạo và gợi ý các hành động bạn cần thực hiện để hoàn thành tác vụ bạn muốn tự động hóa. Chúng ta sẽ tìm hiểu về luồng là gì và cách sử dụng chúng trong Power Automate trong bài học này sau. Bạn có thể tùy chỉnh hành động để đáp ứng nhu cầu của bạn bằng tính năng trợ lý AI Copilot qua các bước hội thoại. Tính năng này có sẵn ngay từ màn hình chính Power Automate.

## Xây dựng Đại lý Thông minh với Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (trước đây là Power Virtual Agents) là thành viên mã thấp của Power Platform để xây dựng **đại lý AI** — các trợ lý hội thoại có thể trả lời câu hỏi, thực hiện hành động và tự động hóa các tác vụ thay mặt người dùng. Giống như phần còn lại của Power Platform, bạn xây dựng các đại lý này trong môi trường trực quan, ưu tiên ngôn ngữ tự nhiên: bạn mô tả những gì bạn muốn đại lý làm, và Copilot Studio giúp xây dựng các hướng dẫn, kiến thức và hành động.

Đối với khởi nghiệp giáo dục của chúng ta, bạn có thể xây dựng một đại lý trả lời các câu hỏi của sinh viên về khóa học, kiểm tra thời hạn bài tập, và thậm chí gửi email cho giảng viên — tất cả đều không cần viết mã.

Dưới đây là một số khả năng mới nhất làm cho Copilot Studio trở nên mạnh mẽ:

- **Câu trả lời tạo sinh từ kiến thức của bạn**. Thay vì viết thủ công mọi cuộc hội thoại, bạn có thể kết nối **nguồn kiến thức** — các trang web công khai, SharePoint, OneDrive, Dataverse, tập tin tải lên hoặc dữ liệu doanh nghiệp qua các bộ kết nối — và đại lý sẽ tạo ra câu trả lời dựa trên các nguồn ấy.

- **Điều phối tạo sinh**. Thay vì dựa vào các câu kích hoạt cứng nhắc, đại lý sử dụng AI để hiểu yêu cầu và quyết định linh hoạt kiến thức, chủ đề và hành động nào cần kết hợp để hoàn thành yêu cầu, kể cả việc kết nối nhiều bước với nhau.

- **Hành động và bộ kết nối**. Các đại lý có thể *thực hiện* các tác vụ, không chỉ trò chuyện. Bạn có thể cung cấp các hành động dựa trên hơn 1,500 bộ kết nối sẵn có của Power Platform, các luồng Power Automate, REST API tùy chỉnh, yêu cầu hoặc máy chủ **Model Context Protocol (MCP)**.

- **Đại lý tự động**. Các đại lý không chỉ phản hồi trong cửa sổ trò chuyện. Bạn có thể xây dựng **đại lý tự động** được kích hoạt bởi sự kiện — chẳng hạn như email mới, bản ghi mới trong Dataverse hoặc tập tin được tải lên — rồi hành động nền để hoàn thành tác vụ.

- **Điều phối đa đại lý**. Các đại lý có thể gọi nhau. Đại lý trong Copilot Studio có thể chuyển tiếp hoặc được mở rộng bởi các đại lý khác, bao gồm đại lý phổ biến trong Microsoft 365 Copilot và đại lý xây dựng trong Microsoft Foundry.

- **Lựa chọn mô hình**. Ngoài các mô hình tích hợp, bạn có thể mang các mô hình từ danh mục mô hình Microsoft Foundry để tùy chỉnh cách đại lý suy luận và phản hồi.

- **Phát hành ở mọi nơi**. Khi xây dựng xong, đại lý có thể được xuất bản trên nhiều kênh — Microsoft Teams, Microsoft 365 Copilot, trang web hoặc ứng dụng tùy chỉnh, và hơn thế nữa — với bảo mật, xác thực và phân tích quản lý qua trải nghiệm quản trị Power Platform.

Bạn có thể bắt đầu xây dựng đại lý đầu tiên tại [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) và tìm hiểu thêm trong [tài liệu Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Bài tập: Quản lý bài tập sinh viên và hóa đơn cho khởi nghiệp của chúng ta, sử dụng Copilot

Khởi nghiệp của chúng ta cung cấp các khóa học trực tuyến cho sinh viên. Khởi nghiệp đã phát triển nhanh và giờ đang gặp khó khăn để đáp ứng nhu cầu về các khóa học của mình. Khởi nghiệp đã thuê bạn làm lập trình viên Power Platform để giúp họ xây dựng giải pháp mã thấp giúp quản lý bài tập sinh viên và hóa đơn. Giải pháp của họ phải có khả năng giúp theo dõi và quản lý bài tập sinh viên qua một ứng dụng và tự động hóa quy trình xử lý hóa đơn qua một luồng công việc. Bạn được yêu cầu sử dụng AI tạo sinh để phát triển giải pháp.

Khi bạn bắt đầu sử dụng Copilot, bạn có thể sử dụng [Thư viện Prompt Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) để bắt đầu với các prompt. Thư viện này chứa danh sách các prompt bạn có thể dùng để xây dựng ứng dụng và luồng với Copilot. Bạn cũng có thể dùng các prompt trong thư viện để có ý tưởng về cách mô tả yêu cầu của bạn cho Copilot.

### Xây dựng Ứng dụng Theo dõi Bài tập Sinh viên cho Khởi nghiệp của Chúng ta

Các nhà giáo dục tại khởi nghiệp của chúng ta đang gặp khó khăn trong việc theo dõi bài tập sinh viên. Họ đã sử dụng bảng tính để theo dõi bài tập nhưng điều này trở nên khó quản lý khi số lượng sinh viên tăng lên. Họ đã yêu cầu bạn xây dựng một ứng dụng giúp họ theo dõi và quản lý bài tập sinh viên. Ứng dụng nên cho phép họ thêm bài tập mới, xem bài tập, cập nhật bài tập và xóa bài tập. Ứng dụng cũng nên cho phép các nhà giáo dục và sinh viên xem các bài tập đã được chấm điểm và những bài chưa được chấm.

Bạn sẽ xây dựng ứng dụng sử dụng Copilot trong Power Apps theo các bước sau:

1. Truy cập màn hình chính của [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Sử dụng ô văn bản trên màn hình chính để mô tả ứng dụng bạn muốn xây dựng. Ví dụ, **_Tôi muốn xây dựng ứng dụng để theo dõi và quản lý bài tập sinh viên_**. Bấm nút **Gửi** để gửi prompt cho AI Copilot.

![Mô tả ứng dụng bạn muốn xây dựng](../../../translated_images/vi/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot sẽ gợi ý một Bảng Dataverse với các trường bạn cần lưu trữ dữ liệu bạn muốn theo dõi và một số dữ liệu mẫu. Bạn có thể tùy chỉnh bảng để đáp ứng yêu cầu của bạn bằng tính năng trợ lý AI Copilot qua các bước hội thoại.

   > **Quan trọng**: Dataverse là nền tảng dữ liệu nền tảng cho Power Platform. Nó là nền tảng dữ liệu mã thấp để lưu trữ dữ liệu của ứng dụng. Đây là dịch vụ được quản lý toàn diện lưu trữ dữ liệu an toàn trên Microsoft Cloud và được cung cấp trong môi trường Power Platform của bạn. Nó đi kèm với các khả năng quản trị dữ liệu tích hợp sẵn, như phân loại dữ liệu, nguồn gốc dữ liệu, kiểm soát truy cập chi tiết và nhiều hơn nữa. Bạn có thể tìm hiểu thêm về Dataverse [tại đây](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Các trường được gợi ý trong bảng mới của bạn](../../../translated_images/vi/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Các nhà giáo dục muốn gửi email cho sinh viên đã nộp bài tập để cập nhật tiến độ bài tập. Bạn có thể dùng Copilot để thêm trường mới vào bảng để lưu trữ email sinh viên. Ví dụ, bạn có thể dùng prompt sau để thêm trường mới vào bảng: **_Tôi muốn thêm một cột để lưu email sinh viên_**. Bấm nút **Gửi** để gửi prompt cho AI Copilot.

![Thêm trường mới](../../../translated_images/vi/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot sẽ tạo trường mới và bạn có thể tùy chỉnh trường này để đáp ứng nhu cầu của bạn.


1. Khi bạn đã hoàn thành với bảng, nhấp vào nút **Create app** để tạo ứng dụng.

1. AI Copilot sẽ tạo ra một ứng dụng Canvas đáp ứng dựa trên mô tả của bạn. Sau đó bạn có thể tùy chỉnh ứng dụng để đáp ứng nhu cầu của mình.

1. Đối với giáo viên gửi email cho học sinh, bạn có thể sử dụng Copilot để thêm một màn hình mới vào ứng dụng. Ví dụ, bạn có thể sử dụng lời nhắc sau để thêm một màn hình mới vào ứng dụng: **_Tôi muốn thêm một màn hình để gửi email cho học sinh_**. Nhấp vào nút **Send** để gửi lời nhắc đến AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/vi/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot sẽ tạo ra một màn hình mới và bạn sau đó có thể tùy chỉnh màn hình để đáp ứng nhu cầu của mình.

1. Khi bạn đã hoàn thành với ứng dụng, nhấp vào nút **Save** để lưu ứng dụng.

1. Để chia sẻ ứng dụng với các giáo viên, nhấp vào nút **Share** và sau đó nhấp lại vào nút **Share**. Bạn có thể chia sẻ ứng dụng với các giáo viên bằng cách nhập địa chỉ email của họ.

> **Bài tập về nhà của bạn**: Ứng dụng bạn vừa xây dựng là một khởi đầu tốt nhưng có thể cải tiến hơn. Với tính năng email, giáo viên chỉ có thể gửi email cho học sinh bằng cách gõ thủ công địa chỉ email của họ. Bạn có thể sử dụng Copilot để xây dựng một tự động hóa cho phép giáo viên gửi email cho học sinh một cách tự động khi họ nộp bài tập không? Gợi ý của bạn là với lời nhắc đúng, bạn có thể sử dụng Copilot trong Power Automate để xây dựng điều này.

### Xây dựng Bảng Thông tin Hóa đơn cho Startup của chúng ta

Nhóm tài chính của startup chúng ta đã gặp khó khăn trong việc theo dõi hóa đơn. Họ đã sử dụng bảng tính để theo dõi các hóa đơn nhưng điều này trở nên khó quản lý khi số lượng hóa đơn tăng lên. Họ đã yêu cầu bạn xây dựng một bảng giúp họ lưu trữ, theo dõi và quản lý thông tin của các hóa đơn họ nhận được. Bảng sẽ được sử dụng để xây dựng một tự động hóa trích xuất tất cả thông tin hóa đơn và lưu trữ vào bảng. Bảng cũng phải cho phép nhóm tài chính xem các hóa đơn đã được thanh toán và những hóa đơn chưa được thanh toán.

Power Platform có một nền tảng dữ liệu cơ bản gọi là Dataverse cho phép bạn lưu trữ dữ liệu cho các ứng dụng và giải pháp của mình. Dataverse cung cấp một nền tảng dữ liệu low-code để lưu trữ dữ liệu của ứng dụng. Đây là một dịch vụ được quản lý toàn diện lưu trữ dữ liệu an toàn trên Microsoft Cloud và được cung cấp trong môi trường Power Platform của bạn. Nó đi kèm với các khả năng quản trị dữ liệu tích hợp sẵn như phân loại dữ liệu, nguồn gốc dữ liệu, kiểm soát truy cập tinh vi và nhiều hơn nữa. Bạn có thể tìm hiểu thêm [về Dataverse tại đây](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Tại sao chúng ta nên sử dụng Dataverse cho startup của mình? Các bảng chuẩn và bảng tùy chỉnh trong Dataverse cung cấp một lựa chọn lưu trữ an toàn và dựa trên đám mây cho dữ liệu của bạn. Các bảng cho phép bạn lưu trữ các loại dữ liệu khác nhau, tương tự như cách bạn có thể sử dụng nhiều trang tính trong một sổ làm việc Excel. Bạn có thể sử dụng bảng để lưu trữ dữ liệu cụ thể cho tổ chức hoặc nhu cầu kinh doanh của mình. Một số lợi ích startup chúng ta sẽ có khi sử dụng Dataverse bao gồm nhưng không giới hạn:

- **Dễ quản lý**: Cả metadata và dữ liệu đều được lưu trữ trên đám mây, nên bạn không phải lo lắng về các chi tiết cách chúng được lưu trữ hay quản lý. Bạn có thể tập trung xây dựng ứng dụng và giải pháp của mình.

- **An toàn**: Dataverse cung cấp một lựa chọn lưu trữ an toàn và dựa trên đám mây cho dữ liệu của bạn. Bạn có thể kiểm soát ai có quyền truy cập vào dữ liệu trong bảng của bạn và cách họ truy cập bằng bảo mật dựa trên vai trò.

- **Metadata phong phú**: Các kiểu dữ liệu và các mối quan hệ được sử dụng trực tiếp trong Power Apps

- **Logic và xác nhận**: Bạn có thể sử dụng các quy tắc nghiệp vụ, các trường tính toán và quy tắc xác nhận để áp dụng logic nghiệp vụ và duy trì độ chính xác dữ liệu.

Bây giờ bạn đã biết Dataverse là gì và tại sao nên sử dụng nó, hãy cùng xem cách bạn có thể dùng Copilot để tạo một bảng trong Dataverse đáp ứng yêu cầu của nhóm tài chính chúng ta.

> **Lưu ý** : Bạn sẽ sử dụng bảng này trong phần tiếp theo để xây dựng một tự động hóa trích xuất tất cả thông tin hóa đơn và lưu trữ vào bảng.

Để tạo một bảng trong Dataverse bằng Copilot, làm theo các bước sau:

1. Chuyển đến màn hình chính của [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Trên thanh điều hướng bên trái, chọn **Tables** và sau đó nhấp vào **Describe the new Table**.

![Select new table](../../../translated_images/vi/describe-new-table.0792373eb757281e.webp)

1. Trên màn hình **Describe the new Table**, sử dụng vùng văn bản để mô tả bảng bạn muốn tạo. Ví dụ, **_Tôi muốn tạo một bảng để lưu thông tin hóa đơn_**. Nhấp nút **Send** để gửi lời nhắc đến AI Copilot.

![Describe the table](../../../translated_images/vi/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot sẽ đề xuất một Bảng Dataverse với các trường bạn cần để lưu dữ liệu bạn muốn theo dõi và một số dữ liệu mẫu. Bạn có thể tùy chỉnh bảng để đáp ứng nhu cầu của mình bằng tính năng trợ lý AI Copilot thông qua các bước đối thoại.

![Suggested Dataverse table](../../../translated_images/vi/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Nhóm tài chính muốn gửi email cho nhà cung cấp để cập nhật trạng thái hiện tại của hóa đơn. Bạn có thể dùng Copilot để thêm một trường mới vào bảng để lưu email nhà cung cấp. Ví dụ, bạn có thể sử dụng lời nhắc sau để thêm một trường mới vào bảng: **_Tôi muốn thêm một cột để lưu email nhà cung cấp_**. Nhấp nút **Send** để gửi lời nhắc đến AI Copilot.

1. AI Copilot sẽ tạo một trường mới và bạn có thể tùy chỉnh trường để đáp ứng nhu cầu của mình.

1. Khi bạn đã hoàn thành với bảng, nhấp vào nút **Create** để tạo bảng.

## Các Mô hình AI trong Power Platform với AI Builder

AI Builder là một khả năng AI low-code có trong Power Platform giúp bạn sử dụng các Mô hình AI để tự động hóa quy trình và dự đoán kết quả. Với AI Builder, bạn có thể mang AI vào ứng dụng và luồng công việc của mình kết nối với dữ liệu trong Dataverse hoặc các nguồn dữ liệu đám mây khác nhau như SharePoint, OneDrive hoặc Azure.

## Mô hình AI đã xây dựng sẵn và Mô hình AI tùy chỉnh

AI Builder cung cấp hai loại Mô hình AI: Mô hình AI đã xây dựng sẵn và Mô hình AI tùy chỉnh. Mô hình AI đã xây dựng sẵn là các mô hình AI sẵn sàng sử dụng được Microsoft đào tạo và có trong Power Platform. Những mô hình này giúp bạn thêm trí tuệ vào ứng dụng và luồng của bạn mà không cần thu thập dữ liệu rồi xây dựng, đào tạo và xuất bản mô hình của riêng bạn. Bạn có thể sử dụng các mô hình này để tự động hóa quy trình và dự đoán kết quả.

Một số Mô hình AI đã xây dựng sẵn có trong Power Platform bao gồm:

- **Trích xuất cụm từ chính**: Mô hình này trích xuất cụm từ chính từ văn bản.
- **Phát hiện ngôn ngữ**: Mô hình này phát hiện ngôn ngữ của một đoạn văn bản.
- **Phân tích cảm xúc**: Mô hình này phát hiện cảm xúc tích cực, tiêu cực, trung tính hoặc hỗn hợp trong văn bản.
- **Đọc danh thiếp**: Mô hình này trích xuất thông tin từ danh thiếp.
- **Nhận dạng văn bản**: Mô hình này trích xuất văn bản từ hình ảnh.
- **Phát hiện đối tượng**: Mô hình này phát hiện và trích xuất các đối tượng từ hình ảnh.
- **Xử lý tài liệu**: Mô hình này trích xuất thông tin từ các biểu mẫu.
- **Xử lý hóa đơn**: Mô hình này trích xuất thông tin từ các hóa đơn.

Với Mô hình AI tùy chỉnh, bạn có thể mang mô hình của riêng mình vào AI Builder để nó hoạt động như bất kỳ mô hình tùy chỉnh AI Builder nào khác, cho phép bạn đào tạo mô hình bằng dữ liệu của riêng bạn. Bạn có thể sử dụng các mô hình này để tự động hóa quy trình và dự đoán kết quả trong cả Power Apps và Power Automate. Khi sử dụng mô hình riêng, có những giới hạn áp dụng. Xem thêm về [các giới hạn này](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/vi/ai-builder-models.8069423b84cfc47f.webp)

## Bài tập #2 - Xây dựng luồng xử lý hóa đơn cho Startup của chúng ta

Nhóm tài chính gặp khó khăn trong việc xử lý hóa đơn. Họ đã sử dụng bảng tính để theo dõi hóa đơn nhưng điều này trở nên khó quản lý khi số lượng hóa đơn tăng. Họ đã yêu cầu bạn xây dựng một quy trình làm việc giúp họ xử lý hóa đơn bằng AI. Quy trình làm việc này phải cho phép họ trích xuất thông tin từ hóa đơn và lưu thông tin vào bảng Dataverse. Quy trình cũng phải cho phép họ gửi email đến nhóm tài chính với thông tin đã trích xuất.

Bây giờ bạn đã biết AI Builder là gì và tại sao nên sử dụng nó, hãy cùng xem cách bạn có thể dùng Mô hình AI xử lý hóa đơn trong AI Builder, mà chúng ta đã đề cập trước đó, để xây dựng một quy trình làm việc giúp nhóm tài chính xử lý hóa đơn.

Để xây dựng quy trình làm việc giúp nhóm tài chính xử lý hóa đơn sử dụng Mô hình AI xử lý hóa đơn trong AI Builder, làm theo các bước sau:

1. Chuyển đến màn hình chính của [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Sử dụng vùng văn bản trên màn hình chính để mô tả quy trình làm việc bạn muốn xây dựng. Ví dụ, **_Xử lý hóa đơn khi nó đến hộp thư của tôi_**. Nhấp vào nút **Send** để gửi lời nhắc đến AI Copilot.

   ![Copilot power automate](../../../translated_images/vi/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot sẽ đề xuất các hành động bạn cần thực hiện để tự động hóa công việc bạn muốn. Bạn có thể nhấp nút **Next** để qua các bước tiếp theo.

4. Ở bước tiếp theo, Power Automate sẽ yêu cầu bạn thiết lập kết nối cần thiết cho luồng. Khi hoàn tất, nhấp nút **Create flow** để tạo luồng.

5. AI Copilot sẽ tạo ra một luồng và bạn có thể tùy chỉnh luồng để đáp ứng nhu cầu của mình.

6. Cập nhật trigger của luồng và đặt **Folder** là thư mục chứa các hóa đơn. Ví dụ, bạn có thể đặt thư mục là **Inbox**. Nhấp vào **Show advanced options** và đặt **Only with Attachments** thành **Yes**. Điều này đảm bảo luồng chỉ chạy khi nhận được email có đính kèm trong thư mục.

7. Xóa các hành động sau khỏi luồng: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** và **Compose 4** vì bạn sẽ không sử dụng chúng.

8. Xóa hành động **Condition** khỏi luồng vì bạn sẽ không dùng nó. Luồng sẽ trông như ảnh chụp màn hình sau:

   ![power automate, remove actions](../../../translated_images/vi/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Nhấp nút **Add an action** và tìm kiếm **Dataverse**. Chọn hành động **Add a new row**.

10. Trong hành động **Extract Information from invoices**, cập nhật **Invoice File** trỏ đến **Attachment Content** từ email. Điều này đảm bảo luồng sẽ trích xuất thông tin từ tệp hóa đơn đính kèm.

11. Chọn **Table** bạn đã tạo trước đó. Ví dụ, bạn có thể chọn bảng **Invoice Information**. Chọn nội dung động từ hành động trước để điền vào các trường sau:

    - ID
    - Amount
    - Date
    - Name
    - Status - Đặt **Status** thành **Pending**.
    - Supplier Email - Dùng nội dung động **From** từ trigger **When a new email arrives**.

    ![power automate add row](../../../translated_images/vi/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Khi bạn đã hoàn thành với luồng, nhấp vào nút **Save** để lưu luồng. Bạn có thể kiểm tra luồng bằng cách gửi một email chứa hóa đơn tới thư mục bạn đã chỉ định trong trigger.

> **Bài tập về nhà của bạn**: Luồng bạn vừa xây dựng là một khởi đầu tốt, giờ bạn cần nghĩ cách xây dựng một tự động hóa cho phép nhóm tài chính gửi email cho nhà cung cấp để cập nhật trạng thái hiện tại của hóa đơn họ. Gợi ý: luồng phải chạy khi trạng thái hóa đơn thay đổi.

## Sử dụng mô hình AI tạo văn bản trong Power Automate

Mô hình Create Text với GPT trong AI Builder cho phép bạn tạo văn bản dựa trên một lời nhắc và được cung cấp sức mạnh bởi Microsoft Azure OpenAI Service. Với khả năng này, bạn có thể tích hợp công nghệ GPT (Generative Pre-Trained Transformer) vào ứng dụng và luồng của mình để xây dựng nhiều luồng tự động và ứng dụng mang lại nhiều thông tin hữu ích.

Các mô hình GPT được đào tạo kỹ lưỡng trên lượng dữ liệu lớn, giúp chúng tạo ra văn bản gần giống ngôn ngữ con người khi được cung cấp lời nhắc. Khi tích hợp với tự động hóa quy trình làm việc, các mô hình AI như GPT có thể được sử dụng để tinh giản và tự động hóa nhiều loại nhiệm vụ.

Ví dụ, bạn có thể xây dựng các luồng tự động tạo văn bản cho nhiều trường hợp sử dụng như: soạn thảo email, mô tả sản phẩm, và nhiều hơn nữa. Bạn cũng có thể dùng mô hình để tạo văn bản cho nhiều ứng dụng khác nhau, như chatbot và ứng dụng dịch vụ khách hàng giúp đại diện chăm sóc khách hàng trả lời nhanh chóng và hiệu quả các câu hỏi của khách hàng.

![create a prompt](../../../translated_images/vi/create-prompt-gpt.69d429300c2e870a.webp)


Để tìm hiểu cách sử dụng Mô Hình AI này trong Power Automate, hãy xem qua module [Thêm trí tuệ với AI Builder và GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Làm tốt lắm! Tiếp tục học tập của bạn

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học về AI Sinh tạo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Sinh tạo!

Muốn tùy chỉnh và khai thác nhiều hơn từ Copilot? Khám phá [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — một bộ sưu tập do cộng đồng đóng góp các chỉ dẫn, tác nhân, kỹ năng và cấu hình giúp bạn tận dụng tối đa GitHub Copilot.

Hãy đến Bài học 11, nơi chúng ta sẽ xem cách [tích hợp AI Sinh tạo với Gọi Hàm](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->