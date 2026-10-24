# Giới thiệu về Mô hình Ngôn ngữ Nhỏ cho AI Sinh tạo dành cho Người mới bắt đầu
AI sinh tạo là một lĩnh vực hấp dẫn của trí tuệ nhân tạo tập trung vào việc tạo ra các hệ thống có khả năng tạo nội dung mới. Nội dung này có thể bao gồm từ văn bản và hình ảnh đến âm nhạc và thậm chí toàn bộ môi trường ảo. Một trong những ứng dụng thú vị nhất của AI sinh tạo là trong lĩnh vực các mô hình ngôn ngữ.

## Mô hình Ngôn ngữ Nhỏ là gì?

Mô hình Ngôn ngữ Nhỏ (SLM) là một biến thể thu nhỏ của mô hình ngôn ngữ lớn (LLM), tận dụng nhiều nguyên tắc kiến trúc và kỹ thuật của LLM, trong khi thể hiện một dấu chân tính toán giảm đáng kể. 

SLM là một tập con của các mô hình ngôn ngữ được thiết kế để tạo ra văn bản giống như con người. Khác với các mô hình lớn hơn như GPT-4, SLM nhỏ gọn và hiệu quả hơn, làm cho chúng trở nên lý tưởng cho các ứng dụng nơi tài nguyên tính toán bị giới hạn. Mặc dù kích thước nhỏ hơn, chúng vẫn có thể thực hiện nhiều nhiệm vụ khác nhau. Thông thường, SLM được xây dựng bằng cách nén hoặc chưng cất các LLM, nhằm giữ lại một phần lớn chức năng và khả năng ngôn ngữ của mô hình gốc. Việc giảm kích thước mô hình này làm giảm độ phức tạp tổng thể, giúp SLM hiệu quả hơn về cả sử dụng bộ nhớ lẫn yêu cầu tính toán. Dù có những tối ưu này, SLM vẫn có thể thực hiện nhiều nhiệm vụ xử lý ngôn ngữ tự nhiên (NLP):

- Tạo Văn Bản: Tạo các câu hoặc đoạn văn mạch lạc và phù hợp ngữ cảnh.
- Hoàn Thành Văn Bản: Dự đoán và hoàn thành câu dựa trên một đề bài cho trước.
- Dịch Thuật: Chuyển đổi văn bản từ ngôn ngữ này sang ngôn ngữ khác.
- Tóm Tắt: Cô đọng các đoạn văn bản dài thành các bản tóm tắt ngắn gọn, dễ hiểu hơn.

Tuy có một số đánh đổi về hiệu năng hoặc chiều sâu hiểu biết so với các mô hình lớn hơn.

## Mô hình Ngôn ngữ Nhỏ hoạt động như thế nào?
SLM được huấn luyện trên lượng lớn dữ liệu văn bản. Trong quá trình huấn luyện, chúng học các mẫu và cấu trúc của ngôn ngữ, cho phép tạo ra văn bản vừa chính xác ngữ pháp vừa phù hợp với ngữ cảnh. Quá trình huấn luyện bao gồm:

- Thu thập dữ liệu: Tập hợp các bộ dữ liệu văn bản lớn từ nhiều nguồn khác nhau.
- Tiền xử lý: Làm sạch và tổ chức dữ liệu để phù hợp với việc huấn luyện.
- Huấn luyện: Sử dụng các thuật toán học máy để dạy mô hình cách hiểu và tạo văn bản.
- Tinh chỉnh: Điều chỉnh mô hình để cải thiện hiệu suất trên các nhiệm vụ cụ thể.

Việc phát triển SLM phù hợp với nhu cầu ngày càng tăng về các mô hình có thể triển khai trong các môi trường hạn chế tài nguyên, như thiết bị di động hoặc nền tảng điện toán biên, nơi mà các LLM quy mô lớn có thể không thực tế do yêu cầu tài nguyên lớn. Bằng cách tập trung vào hiệu quả, SLM cân bằng giữa hiệu suất và khả năng tiếp cận, cho phép ứng dụng rộng rãi hơn trong nhiều lĩnh vực.

![slm](../../../translated_images/vi/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mục Tiêu Học Tập

Trong bài học này, chúng ta hy vọng giới thiệu kiến thức về SLM và kết hợp với Microsoft Phi-3 để học các kịch bản khác nhau trong nội dung văn bản, thị giác và MoE.

Đến cuối bài học, bạn sẽ có thể trả lời các câu hỏi sau:

- SLM là gì?
- Sự khác biệt giữa SLM và LLM là gì?
- Microsoft Phi-3/3.5 Family là gì?
- Cách chạy suy luận với Microsoft Phi-3/3.5 Family như thế nào?

Sẵn sàng chưa? Hãy bắt đầu.

## Sự khác biệt giữa Mô hình Ngôn ngữ Lớn (LLM) và Mô hình Ngôn ngữ Nhỏ (SLM)

Cả LLM và SLM đều được xây dựng dựa trên các nguyên tắc nền tảng của học máy xác suất, theo các phương pháp tương tự trong thiết kế kiến trúc, phương pháp huấn luyện, quy trình tạo dữ liệu và kỹ thuật đánh giá mô hình. Tuy nhiên, có một số yếu tố then chốt phân biệt hai loại mô hình này.

## Ứng dụng của Mô hình Ngôn ngữ Nhỏ

SLM có phạm vi ứng dụng rộng, bao gồm:

- Chatbot: Cung cấp hỗ trợ khách hàng và tương tác với người dùng theo cách hội thoại.
- Tạo Nội dung: Hỗ trợ người viết bằng cách tạo ý tưởng hoặc thậm chí soạn thảo toàn bộ bài viết.
- Giáo dục: Giúp học sinh làm bài tập viết hoặc học ngôn ngữ mới.
- Khả năng tiếp cận: Tạo công cụ cho người khuyết tật, như hệ thống chuyển văn bản thành giọng nói.

**Kích thước**
  
Sự khác biệt chính giữa LLM và SLM nằm ở quy mô mô hình. LLM, như ChatGPT (GPT-4), có thể gồm khoảng 1.76 nghìn tỷ tham số, trong khi các SLM mã nguồn mở như Mistral 7B được thiết kế với số lượng tham số thấp hơn nhiều — khoảng 7 tỷ. Sự chênh lệch này chủ yếu do khác biệt trong kiến trúc mô hình và quy trình huấn luyện. Ví dụ, ChatGPT sử dụng cơ chế tự chú ý trong khung mã hóa - giải mã, trong khi Mistral 7B sử dụng chú ý cửa sổ trượt, giúp huấn luyện hiệu quả hơn trong mô hình chỉ giải mã. Sự khác biệt kiến trúc này ảnh hưởng sâu sắc đến độ phức tạp và hiệu suất của các mô hình.

**Khả năng Hiểu Biết**

SLM thường được tối ưu hóa cho hiệu suất trong các lĩnh vực cụ thể, làm cho chúng rất chuyên biệt nhưng có thể hạn chế trong khả năng cung cấp hiểu biết rộng trên nhiều lĩnh vực kiến thức. Ngược lại, LLM nhằm mục tiêu mô phỏng trí tuệ giống con người ở mức độ toàn diện hơn. Được huấn luyện trên các bộ dữ liệu lớn và đa dạng, LLM được thiết kế để hoạt động tốt trên nhiều lĩnh vực, cung cấp sự đa năng và thích nghi cao hơn. Do đó, LLM phù hợp hơn cho nhiều nhiệm vụ hạ nguồn như xử lý ngôn ngữ tự nhiên và lập trình.

**Tính Toán**

Quá trình huấn luyện và triển khai LLM tiêu tốn nhiều tài nguyên, thường yêu cầu hạ tầng tính toán lớn, bao gồm các cụm GPU quy mô lớn. Ví dụ, huấn luyện một mô hình như ChatGPT từ đầu có thể cần hàng nghìn GPU trong thời gian dài. Ngược lại, SLM với số lượng tham số nhỏ hơn, dễ tiếp cận hơn về mặt tài nguyên tính toán. Các mô hình như Mistral 7B có thể được huấn luyện và chạy trên các máy cục bộ trang bị GPU vừa phải, mặc dù huấn luyện vẫn cần vài giờ trên nhiều GPU.

**Định kiến**

Định kiến là một vấn đề đã biết trong LLM, chủ yếu do tính chất của dữ liệu huấn luyện. Các mô hình này thường dựa trên dữ liệu thô, công khai trên internet, có thể thiếu đại diện hoặc phản ánh sai các nhóm nhất định, gây ra gán nhãn sai hoặc phản ánh định kiến ngôn ngữ bị ảnh hưởng bởi phương ngữ, biến thể địa lý và quy tắc ngữ pháp. Thêm vào đó, kiến trúc phức tạp của LLM có thể vô tình làm tăng định kiến, điều này có thể không được phát hiện nếu không thực hiện tinh chỉnh kỹ lưỡng. Ngược lại, SLM do được huấn luyện trên các bộ dữ liệu giới hạn hơn, theo lĩnh vực cụ thể, ít bị ảnh hưởng bởi các định kiến này dù không hoàn toàn miễn nhiễm.

**Suy luận**

Kích thước giảm của SLM mang lại lợi thế lớn về tốc độ suy luận, cho phép chúng tạo ra kết quả hiệu quả trên phần cứng cục bộ mà không cần xử lý song song nhiều. Trong khi đó, LLM với kích thước và độ phức tạp cao thường yêu cầu tài nguyên tính toán song song đáng kể để đạt thời gian suy luận chấp nhận được. Số lượng người dùng đồng thời lớn càng làm chậm thời gian phản hồi của LLM, đặc biệt khi triển khai ở quy mô lớn.

Tóm lại, trong khi cả LLM và SLM đều dựa trên nền tảng học máy, chúng khác biệt rõ rệt về kích thước mô hình, yêu cầu tài nguyên, khả năng hiểu ngữ cảnh, độ nhạy với định kiến và tốc độ suy luận. Những điểm khác biệt này phản ánh sự phù hợp của chúng với các trường hợp sử dụng khác nhau, với LLM đa năng hơn nhưng tốn kém tài nguyên, còn SLM cung cấp hiệu quả theo lĩnh vực với yêu cầu tính toán giảm.

***Lưu ý: Trong bài học này, chúng ta sẽ giới thiệu SLM sử dụng Microsoft Phi-3 / 3.5 làm ví dụ.***

## Giới thiệu về Phi-3 / Phi-3.5 Family

Phi-3 / 3.5 Family chủ yếu hướng tới các kịch bản ứng dụng về văn bản, thị giác và Đại lý (MoE):

### Phi-3 / 3.5 Instruct

Chủ yếu cho tạo văn bản, hoàn thành chat, và trích xuất thông tin nội dung, v.v.

**Phi-3-mini**

Mô hình ngôn ngữ 3.8B có sẵn trên Microsoft Foundry, Hugging Face và Ollama. Các mô hình Phi-3 vượt trội đáng kể so với các mô hình ngôn ngữ cùng kích thước và lớn hơn trên các chuẩn đánh giá chính (xem số liệu chuẩn bên dưới, số càng cao càng tốt). Phi-3-mini vượt qua các mô hình có kích thước gấp đôi, trong khi Phi-3-small và Phi-3-medium vượt trội hơn các mô hình lớn hơn, bao gồm GPT-3.5.

**Phi-3-small & medium**

Với chỉ 7 tỷ tham số, Phi-3-small đánh bại GPT-3.5T trên nhiều chuẩn đánh giá về ngôn ngữ, lý luận, lập trình và toán học.

Phi-3-medium với 14 tỷ tham số tiếp tục xu hướng này và vượt trội Gemini 1.0 Pro.

**Phi-3.5-mini**

Có thể coi đây là phiên bản nâng cấp của Phi-3-mini. Mặc dù số lượng tham số không thay đổi, nó cải thiện khả năng hỗ trợ đa ngôn ngữ (hỗ trợ hơn 20 ngôn ngữ: Ả Rập, Trung, Séc, Đan Mạch, Hà Lan, Anh, Phần Lan, Pháp, Đức, Hebrew, Hungary, Ý, Nhật, Hàn, Na Uy, Ba Lan, Bồ Đào Nha, Nga, Tây Ban Nha, Thụy Điển, Thái, Thổ Nhĩ Kỳ, Ukraina) và thêm hỗ trợ mạnh hơn cho ngữ cảnh dài.

Phi-3.5-mini với 3.8 tỷ tham số vượt trội hơn các mô hình cùng kích thước và tương đương với các mô hình gấp đôi kích thước.

### Phi-3 / 3.5 Vision

Có thể xem mô hình Instruct của Phi-3/3.5 như khả năng hiểu của Phi, và Vision là đôi mắt giúp Phi hiểu thế giới.


**Phi-3-Vision**

Phi-3-vision, với chỉ 4.2 tỷ tham số, tiếp tục xu hướng này và vượt trội các mô hình lớn hơn như Claude-3 Haiku và Gemini 1.0 Pro V trên các tác vụ lý luận thị giác tổng quát, OCR, và hiểu bảng biểu và sơ đồ.


**Phi-3.5-Vision**

Phi-3.5-Vision cũng là bản nâng cấp của Phi-3-Vision, thêm khả năng hỗ trợ nhiều hình ảnh. Bạn có thể hiểu đó là cải thiện về thị giác, không chỉ nhìn thấy hình ảnh mà còn cả video.

Phi-3.5-vision vượt trội hơn các mô hình lớn như Claude-3.5 Sonnet và Gemini 1.5 Flash trên các tác vụ OCR, hiểu bảng và biểu đồ và tương đương về các tác vụ lý luận kiến thức thị giác tổng quát. Hỗ trợ đầu vào đa khung hình, tức là thực hiện suy luận trên nhiều hình ảnh đầu vào.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** cho phép các mô hình được tiền huấn luyện với lượng tính toán ít hơn nhiều, có nghĩa là bạn có thể mở rộng quy mô mô hình hoặc bộ dữ liệu đáng kể với cùng ngân sách tính toán so với mô hình đặc. Đặc biệt, mô hình MoE có thể đạt chất lượng tương đương với mô hình đặc tương ứng nhanh hơn nhiều trong quá trình tiền huấn luyện.

Phi-3.5-MoE gồm 16 mô-đun chuyên gia 3.8B. Phi-3.5-MoE với chỉ 6.6 tỷ tham số hoạt động đạt mức độ lý luận, hiểu ngôn ngữ và toán học tương tự các mô hình lớn hơn nhiều.

Chúng ta có thể sử dụng mô hình Phi-3/3.5 cho nhiều kịch bản khác nhau. Khác với LLM, bạn có thể triển khai Phi-3/3.5-mini hoặc Phi-3/3.5-Vision trên các thiết bị biên.


## Cách sử dụng các mô hình Phi-3/3.5 Family

Chúng ta hy vọng sử dụng Phi-3/3.5 trong nhiều kịch bản khác nhau. Tiếp theo, chúng ta sẽ sử dụng Phi-3/3.5 dựa trên các kịch bản khác nhau.

![phi3](../../../translated_images/vi/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Suy luận qua API Đám mây

**Mô hình Microsoft Foundry**

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) là sự thay thế trực tiếp.

Microsoft Foundry Models là cách trực tiếp nhất. Bạn có thể nhanh chóng truy cập mô hình Phi-3/3.5-Instruct qua danh mục mô hình Foundry. Kết hợp với Azure AI Inference SDK / OpenAI SDK, bạn có thể truy cập API qua mã để hoàn thành gọi Phi-3/3.5-Instruct. Bạn cũng có thể thử nghiệm các hiệu ứng khác nhau qua Playground.

- Demo: So sánh hiệu quả của Phi-3-mini và Phi-3.5-mini trong kịch bản tiếng Trung

![phi3](../../../translated_images/vi/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/vi/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Hoặc nếu bạn muốn sử dụng các mô hình thị giác và MoE, bạn có thể dùng Microsoft Foundry để hoàn thành cuộc gọi. Nếu quan tâm, bạn có thể đọc Sổ tay Phi-3 để biết cách gọi Phi-3/3.5 Instruct, Vision, MoE qua Microsoft Foundry [Nhấn vào đây](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ngoài danh mục mô hình dựa trên đám mây Microsoft Foundry, bạn cũng có thể sử dụng [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) để hoàn thành các cuộc gọi liên quan. Bạn có thể truy cập NVIDIA NIM để thực hiện các cuộc gọi API của Phi-3/3.5 Family. NVIDIA NIM (NVIDIA Inference Microservices) là tập hợp các dịch vụ vi mô suy luận tăng tốc nhằm giúp nhà phát triển triển khai các mô hình AI hiệu quả trên nhiều môi trường khác nhau, bao gồm đám mây, trung tâm dữ liệu và máy trạm.

Dưới đây là một số tính năng chính của NVIDIA NIM:

- **Dễ triển khai:** NIM cho phép triển khai mô hình AI chỉ với một lệnh, giúp dễ dàng tích hợp vào quy trình hiện có.
- **Hiệu suất tối ưu:** Tận dụng các công cụ suy luận được NVIDIA tối ưu sẵn, như TensorRT và TensorRT-LLM, để đảm bảo độ trễ thấp và thông lượng cao.
- **Khả năng mở rộng:** NIM hỗ trợ tự động mở rộng trên Kubernetes, giúp xử lý khối lượng công việc biến đổi hiệu quả.
- **Bảo mật và Kiểm soát:** Các tổ chức có thể giữ quyền kiểm soát dữ liệu và ứng dụng bằng cách tự vận hành các dịch vụ vi mô NIM trên hạ tầng quản lý của riêng họ.
- **API Chuẩn:** NIM cung cấp các API chuẩn công nghiệp, giúp dễ dàng xây dựng và tích hợp các ứng dụng AI như chatbot, trợ lý AI, và nhiều hơn nữa.

NIM là một phần của NVIDIA AI Enterprise, nhằm đơn giản hóa việc triển khai và vận hành các mô hình AI, đảm bảo chúng chạy hiệu quả trên GPU NVIDIA.

- Demo: Sử dụng NVIDIA NIM để gọi Phi-3.5-Vision-API [[Nhấn vào đây](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Chạy Phi-3/3.5 Cục bộ
Inference liên quan đến Phi-3, hoặc bất kỳ mô hình ngôn ngữ nào như GPT-3, đề cập đến quá trình tạo ra phản hồi hoặc dự đoán dựa trên đầu vào mà nó nhận được. Khi bạn cung cấp một lời nhắc hoặc câu hỏi cho Phi-3, nó sử dụng mạng nơ-ron được huấn luyện để suy luận phản hồi có khả năng cao nhất và phù hợp nhất bằng cách phân tích các mẫu và mối quan hệ trong dữ liệu mà nó đã được huấn luyện.

**Hugging Face Transformer**
Hugging Face Transformers là một thư viện mạnh mẽ được thiết kế cho xử lý ngôn ngữ tự nhiên (NLP) và các nhiệm vụ học máy khác. Dưới đây là một số điểm chính về nó:

1. **Mô hình được huấn luyện sẵn**: Nó cung cấp hàng ngàn mô hình đã được huấn luyện sẵn có thể dùng cho nhiều nhiệm vụ như phân loại văn bản, nhận dạng thực thể đặt tên, trả lời câu hỏi, tóm tắt, dịch thuật và tạo văn bản.

2. **Tương tác đa framework**: Thư viện hỗ trợ nhiều framework học sâu, bao gồm PyTorch, TensorFlow và JAX. Điều này cho phép bạn huấn luyện một mô hình trong một framework và dùng nó trong framework khác.

3. **Khả năng đa phương tiện**: Ngoài NLP, Hugging Face Transformers cũng hỗ trợ các nhiệm vụ trong thị giác máy tính (ví dụ: phân loại hình ảnh, phát hiện đối tượng) và xử lý âm thanh (ví dụ: nhận dạng giọng nói, phân loại âm thanh).

4. **Dễ sử dụng**: Thư viện cung cấp API và công cụ để dễ dàng tải xuống và tinh chỉnh mô hình, giúp người dùng cả mới và chuyên gia đều có thể tiếp cận.

5. **Cộng đồng và tài nguyên**: Hugging Face có một cộng đồng sôi động và tài liệu, hướng dẫn, bài học phong phú để hỗ trợ người dùng bắt đầu và tận dụng tối đa thư viện.
[tài liệu chính thức](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) hoặc [kho GitHub của họ](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Đây là phương pháp phổ biến nhất, nhưng nó cũng yêu cầu tăng tốc GPU. Dù sao thì, các kịch bản như Vision và MoE đòi hỏi nhiều phép tính, sẽ rất chậm trên CPU nếu không được lượng tử hóa.


- Demo: Sử dụng Transformer để gọi Phi-3.5-Instruct [Nhấn vào đây](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Sử dụng Transformer để gọi Phi-3.5-Vision [Nhấn vào đây](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Sử dụng Transformer để gọi Phi-3.5-MoE [Nhấn vào đây](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) là một nền tảng được thiết kế để giúp việc chạy các mô hình ngôn ngữ lớn (LLMs) cục bộ trên máy của bạn dễ dàng hơn. Nó hỗ trợ các mô hình khác nhau như Llama 3.1, Phi 3, Mistral và Gemma 2, cùng nhiều mô hình khác. Nền tảng này đơn giản hóa quy trình bằng cách đóng gói trọng số mô hình, cấu hình và dữ liệu thành một gói duy nhất, giúp người dùng dễ dàng tùy chỉnh và tạo mô hình riêng. Ollama có sẵn cho macOS, Linux và Windows. Đây là công cụ tuyệt vời nếu bạn muốn thử nghiệm hoặc triển khai LLM mà không phụ thuộc vào dịch vụ đám mây. Ollama là cách trực tiếp nhất, bạn chỉ cần thực thi lệnh sau.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) là môi trường runtime ngoại tuyến trực tiếp trên thiết bị của Microsoft để chạy các mô hình như Phi hoàn toàn trên phần cứng của bạn - không cần đăng ký Azure, khóa API hay kết nối mạng. Nó tự động chọn nhà cung cấp thực thi tốt nhất có sẵn (NPU, GPU hoặc CPU) và phơi bày một endpoint tương thích OpenAI, vì vậy mã SDK `openai`/Azure AI Inference hiện có có thể trỏ tới nó với ít thay đổi nhất. Xem [tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) để bắt đầu.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Hoặc dùng SDK trực tiếp trong Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime cho GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) là một công cụ tăng tốc học máy đa nền tảng dùng cho infer và huấn luyện. ONNX Runtime cho Generative AI (GENAI) là một công cụ mạnh mẽ giúp bạn chạy các mô hình AI sinh tạo hiệu quả trên nhiều nền tảng khác nhau.

## ONNX Runtime là gì?
ONNX Runtime là dự án mã nguồn mở cho phép infer các mô hình học máy hiệu suất cao. Nó hỗ trợ các mô hình ở định dạng Open Neural Network Exchange (ONNX), một tiêu chuẩn cho biểu diễn mô hình học máy. ONNX Runtime inference có thể cải thiện trải nghiệm khách hàng nhanh hơn và chi phí thấp hơn, hỗ trợ các mô hình từ các framework học sâu như PyTorch và TensorFlow/Keras cũng như các thư viện học máy truyền thống như scikit-learn, LightGBM, XGBoost, v.v. ONNX Runtime tương thích với nhiều phần cứng, driver và hệ điều hành khác nhau, và cung cấp hiệu suất tối ưu nhờ tận dụng các bộ tăng tốc phần cứng cùng các tối ưu đồ thị và biến đổi.

## Generative AI là gì?
Generative AI đề cập đến các hệ thống AI có thể tạo ra nội dung mới, như văn bản, hình ảnh hoặc âm nhạc, dựa trên dữ liệu mà chúng được huấn luyện. Ví dụ bao gồm các mô hình ngôn ngữ như GPT-3 và các mô hình tạo hình ảnh như Stable Diffusion. Thư viện ONNX Runtime cho GenAI cung cấp vòng lặp sinh tạo AI cho các mô hình ONNX, bao gồm infer với ONNX Runtime, xử lý logits, tìm kiếm và lấy mẫu, và quản lý bộ nhớ đệm KV.

## ONNX Runtime cho GENAI
ONNX Runtime cho GENAI mở rộng khả năng của ONNX Runtime để hỗ trợ các mô hình AI sinh tạo. Dưới đây là một số tính năng chính:

- **Hỗ trợ nền tảng rộng:** Nó hoạt động trên nhiều nền tảng, bao gồm Windows, Linux, macOS, Android và iOS.
- **Hỗ trợ mô hình:** Nó hỗ trợ nhiều mô hình AI sinh tạo phổ biến, như LLaMA, GPT-Neo, BLOOM và nhiều hơn nữa.
- **Tối ưu hiệu suất:** Bao gồm các tối ưu cho các bộ tăng tốc phần cứng khác nhau như GPU NVIDIA, GPU AMD, và nhiều hơn nữa.
- **Dễ sử dụng:** Cung cấp API giúp tích hợp vào ứng dụng một cách dễ dàng, cho phép bạn tạo ra văn bản, hình ảnh và nội dung khác chỉ với một lượng mã tối thiểu.
- Người dùng có thể gọi phương thức cao cấp generate(), hoặc chạy từng vòng lặp của mô hình theo từng token, và tùy chọn cập nhật tham số sinh tạo trong vòng lặp.
- ONNX runtime cũng hỗ trợ tìm kiếm greedy/beam và việc lấy mẫu TopP, TopK để tạo chuỗi token cùng xử lý logits tích hợp như phạt lặp lại. Bạn cũng có thể dễ dàng thêm điểm số tùy chỉnh.

## Bắt đầu
Để bắt đầu với ONNX Runtime cho GENAI, bạn có thể làm theo các bước sau:

### Cài đặt ONNX Runtime:
```Python
pip install onnxruntime
```
### Cài đặt tiện ích mở rộng Generative AI:
```Python
pip install onnxruntime-genai
```

### Chạy một mô hình: Đây là ví dụ đơn giản bằng Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Sử dụng ONNX Runtime GenAI để gọi Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Khác**

Ngoài ONNX Runtime, Ollama và phương pháp tham khảo Foundry Local, chúng ta cũng có thể hoàn thiện tham chiếu mô hình lượng tử dựa trên các phương pháp tham khảo mô hình do các nhà sản xuất khác nhau cung cấp. Chẳng hạn như framework Apple MLX với Apple Metal, Qualcomm QNN với NPU, Intel OpenVINO với CPU/GPU, v.v. Bạn cũng có thể xem thêm từ [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Thêm nữa

Chúng ta đã học những điều cơ bản về gia đình Phi-3/3.5, nhưng để tìm hiểu thêm về SLM, chúng ta cần kiến thức sâu hơn. Bạn có thể tìm câu trả lời trong Phi-3 Cookbook. Nếu muốn học thêm, vui lòng truy cập [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->