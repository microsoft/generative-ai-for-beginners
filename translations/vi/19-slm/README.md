# Giới thiệu về Mô hình Ngôn ngữ Nhỏ cho AI Sinh tạo dành cho Người mới bắt đầu
AI Sinh tạo là một lĩnh vực hấp dẫn của trí tuệ nhân tạo, tập trung vào việc tạo ra các hệ thống có khả năng sinh ra nội dung mới. Nội dung này có thể bao gồm văn bản, hình ảnh, âm nhạc và thậm chí cả các môi trường ảo hoàn chỉnh. Một trong những ứng dụng thú vị nhất của AI sinh tạo là trong lĩnh vực các mô hình ngôn ngữ.

## Mô hình Ngôn ngữ Nhỏ là gì?

Mô hình Ngôn ngữ Nhỏ (SLM) là một biến thể thu nhỏ của mô hình ngôn ngữ lớn (LLM), tận dụng nhiều nguyên tắc kiến trúc và kỹ thuật của LLM, đồng thời có dấu chân tính toán giảm đáng kể.

SLM là tập hợp con của các mô hình ngôn ngữ được thiết kế để tạo ra văn bản giống con người. Khác với các mô hình lớn hơn như GPT-4, SLM nhỏ gọn và hiệu quả hơn, phù hợp với các ứng dụng có giới hạn về tài nguyên tính toán. Mặc dù kích thước nhỏ hơn, chúng vẫn có thể thực hiện nhiều tác vụ khác nhau. Thông thường, SLM được xây dựng bằng cách nén hoặc chưng cất các LLM, nhằm giữ lại phần lớn chức năng và khả năng ngôn ngữ của mô hình gốc. Việc giảm kích thước mô hình làm giảm tổng độ phức tạp, giúp SLM hiệu quả hơn về mặt sử dụng bộ nhớ và yêu cầu tính toán. Mặc dù được tối ưu hóa như vậy, SLM vẫn có thể thực hiện nhiều tác vụ xử lý ngôn ngữ tự nhiên (NLP):

- Sinh văn bản: Tạo ra các câu hoặc đoạn văn có tính mạch lạc và phù hợp với ngữ cảnh.
- Hoàn thành văn bản: Dự đoán và hoàn thành câu dựa trên gợi ý được cung cấp.
- Dịch thuật: Chuyển đổi văn bản từ ngôn ngữ này sang ngôn ngữ khác.
- Tóm tắt: Rút ngắn các đoạn văn dài thành các tóm tắt ngắn gọn và dễ tiếp nhận.

Với một số đánh đổi về hiệu năng hoặc độ sâu hiểu biết so với các mô hình lớn hơn.

## Mô hình Ngôn ngữ Nhỏ hoạt động như thế nào?
SLM được huấn luyện trên lượng lớn dữ liệu văn bản. Trong quá trình huấn luyện, chúng học các mẫu và cấu trúc của ngôn ngữ, cho phép tạo ra văn bản vừa hợp ngữ pháp vừa phù hợp với ngữ cảnh. Quá trình huấn luyện gồm:

- Thu thập dữ liệu: Tập hợp các bộ dữ liệu văn bản lớn từ nhiều nguồn khác nhau.
- Tiền xử lý: Làm sạch và sắp xếp dữ liệu để phù hợp với mục đích huấn luyện.
- Huấn luyện: Sử dụng các thuật toán học máy để dạy mô hình cách hiểu và sinh văn bản.
- Tinh chỉnh: Điều chỉnh mô hình để cải thiện hiệu năng trên các nhiệm vụ cụ thể.

Sự phát triển của SLM phù hợp với nhu cầu ngày càng tăng về các mô hình có thể triển khai trong môi trường giới hạn tài nguyên, như thiết bị di động hoặc nền tảng điện toán biên, nơi các LLM toàn diện có thể không thực tế do yêu cầu tài nguyên lớn. Bằng cách tập trung vào hiệu quả, SLM cân bằng giữa hiệu năng và khả năng tiếp cận, giúp áp dụng rộng rãi hơn trên nhiều lĩnh vực.

![slm](../../../translated_images/vi/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mục tiêu học tập

Trong bài học này, chúng tôi hy vọng giới thiệu kiến thức về SLM và kết hợp với Microsoft Phi-3 để học các kịch bản khác nhau trong nội dung văn bản, thị giác và MoE.

Cuối bài học này, bạn sẽ có thể trả lời các câu hỏi sau:

- SLM là gì?
- Sự khác biệt giữa SLM và LLM là gì?
- Gia đình Microsoft Phi-3/3.5 là gì?
- Làm thế nào để chạy suy luận với Gia đình Microsoft Phi-3/3.5?

Sẵn sàng chưa? Bắt đầu thôi.

## Sự khác biệt giữa Mô hình Ngôn ngữ Lớn (LLM) và Mô hình Ngôn ngữ Nhỏ (SLM)

Cả LLM và SLM đều dựa trên các nguyên tắc cơ bản của học máy xác suất, theo các cách tiếp cận tương tự về thiết kế kiến trúc, phương pháp huấn luyện, quy trình tạo dữ liệu và kỹ thuật đánh giá mô hình. Tuy nhiên, có một số yếu tố then chốt phân biệt hai loại mô hình này.

## Ứng dụng của Mô hình Ngôn ngữ Nhỏ

SLM có nhiều ứng dụng, bao gồm:

- Chatbots: Cung cấp hỗ trợ khách hàng và tương tác với người dùng theo cách hội thoại.
- Tạo nội dung: Hỗ trợ người viết bằng cách tạo ý tưởng hoặc thậm chí soạn thảo toàn bộ bài viết.
- Giáo dục: Giúp học sinh làm bài tập viết hoặc học ngôn ngữ mới.
- Khả năng tiếp cận: Tạo công cụ cho người khuyết tật, như hệ thống chuyển văn bản thành giọng nói.

**Kích thước**
  
Sự khác biệt chính giữa LLM và SLM nằm ở quy mô mô hình. LLM, như ChatGPT (GPT-4), có thể chứa khoảng 1.76 nghìn tỷ tham số, trong khi các SLM mã nguồn mở như Mistral 7B được thiết kế với số lượng tham số ít hơn nhiều—khoảng 7 tỷ. Sự chênh lệch này chủ yếu do khác biệt về kiến trúc mô hình và quy trình huấn luyện. Ví dụ, ChatGPT sử dụng cơ chế tự chú ý trong khuôn khổ bộ mã hóa - giải mã, trong khi Mistral 7B dùng cơ chế chú ý cửa sổ trượt, cho phép huấn luyện hiệu quả hơn trong mô hình chỉ giải mã. Sự khác biệt kiến trúc này ảnh hưởng sâu sắc đến độ phức tạp và hiệu năng của các mô hình.

**Khả năng hiểu**

SLM thường được tối ưu hóa để hoạt động tốt trong các lĩnh vực cụ thể, làm chúng trở nên chuyên biệt cao nhưng có thể hạn chế khả năng cung cấp hiểu biết rộng về nhiều lĩnh vực kiến thức khác nhau. Ngược lại, LLM hướng đến mô phỏng trí tuệ giống con người trên phạm vi toàn diện hơn. Được huấn luyện trên các bộ dữ liệu đa dạng và khổng lồ, LLM được thiết kế để thực hiện tốt trên nhiều lĩnh vực, đem lại tính linh hoạt và thích ứng cao hơn. Vì vậy, LLM phù hợp hơn với nhiều nhiệm vụ hạ nguồn khác nhau, như xử lý ngôn ngữ tự nhiên và lập trình.

**Tính toán**

Quá trình huấn luyện và triển khai LLM rất tốn kém tài nguyên, thường yêu cầu hạ tầng tính toán lớn bao gồm các cụm GPU quy mô lớn. Ví dụ, việc huấn luyện từ đầu một mô hình như ChatGPT có thể cần hàng nghìn GPU trong thời gian dài. Ngược lại, SLM với số lượng tham số nhỏ hơn dễ tiếp cận hơn về mặt tài nguyên tính toán. Các mô hình như Mistral 7B có thể được huấn luyện và chạy trên máy cá nhân có GPU vừa phải, mặc dù việc huấn luyện vẫn đòi hỏi hàng giờ trên nhiều GPU.

**Thiên kiến**

Thiên kiến là một vấn đề đã được biết đến ở LLM, chủ yếu do bản chất dữ liệu huấn luyện. Những mô hình này thường dựa vào dữ liệu thô, công khai trên internet, có thể thiếu đại diện hoặc thể hiện sai về một số nhóm, gây ra gán nhãn sai hoặc phản ánh các thiên kiến ngôn ngữ do phương ngữ, biến thể địa lý và quy tắc ngữ pháp ảnh hưởng. Thêm vào đó, kiến trúc phức tạp của LLM có thể vô tình làm trầm trọng thêm thiên kiến, điều mà có thể không được phát hiện nếu không có tinh chỉnh kỹ lưỡng. Ngược lại, SLM, được huấn luyện trên các bộ dữ liệu giới hạn, chuyên môn theo lĩnh vực, bản chất ít bị ảnh hưởng bởi những thiên kiến như vậy hơn, mặc dù không hoàn toàn miễn nhiễm.

**Suy luận**

Kích thước giảm của SLM mang lại lợi thế lớn về tốc độ suy luận, cho phép tạo kết quả một cách hiệu quả trên phần cứng cục bộ mà không cần xử lý song song rộng rãi. Ngược lại, LLM, do kích thước và độ phức tạp, thường đòi hỏi tài nguyên tính toán song song lớn để đạt được thời gian suy luận chấp nhận được. Sự hiện diện của nhiều người dùng đồng thời càng làm chậm thời gian phản hồi của LLM, đặc biệt khi triển khai ở quy mô lớn.

Tóm lại, mặc dù cả LLM và SLM đều dựa trên nền tảng học máy, nhưng chúng khác biệt đáng kể về kích thước mô hình, yêu cầu tài nguyên, hiểu biết ngữ cảnh, mức độ thiên kiến và tốc độ suy luận. Những khác biệt này phản ánh sự phù hợp của chúng với các trường hợp sử dụng khác nhau, với LLM đa năng hơn nhưng tốn tài nguyên, còn SLM mang lại hiệu quả chuyên môn với nhu cầu tính toán thấp hơn.

***Lưu ý: Trong bài học này, chúng ta sẽ giới thiệu SLM sử dụng Microsoft Phi-3 / 3.5 làm ví dụ.***

## Giới thiệu Gia đình Phi-3 / Phi-3.5

Gia đình Phi-3 / 3.5 chủ yếu hướng đến các kịch bản ứng dụng văn bản, thị giác và Tác nhân (MoE):

### Phi-3 / 3.5 Instruct

Chủ yếu cho việc tạo văn bản, hoàn thành hội thoại, và trích xuất thông tin nội dung, v.v.

**Phi-3-mini**

Mô hình ngôn ngữ 3.8B có sẵn trên Microsoft Foundry, Hugging Face và Ollama. Các mô hình Phi-3 vượt trội đáng kể so với các mô hình ngôn ngữ có kích thước bằng hoặc lớn hơn trên các tiêu chuẩn chính (xem số liệu benchmark dưới đây, số cao hơn là tốt hơn). Phi-3-mini vượt trội so với các mô hình có kích thước gấp đôi, trong khi Phi-3-small và Phi-3-medium vượt trội hơn các mô hình lớn hơn, bao gồm cả GPT-3.5.

**Phi-3-small & medium**

Với chỉ 7 tỷ tham số, Phi-3-small vượt qua GPT-3.5T trên nhiều bài kiểm tra về ngôn ngữ, suy luận, lập trình và toán học.

Phi-3-medium với 14 tỷ tham số tiếp tục xu hướng này và vượt trội hơn Gemini 1.0 Pro.

**Phi-3.5-mini**

Có thể coi đây là nâng cấp của Phi-3-mini. Mặc dù số lượng tham số không thay đổi, nó cải thiện khả năng hỗ trợ đa ngôn ngữ (hỗ trợ hơn 20 ngôn ngữ: Ả Rập, Trung Quốc, Séc, Đan Mạch, Hà Lan, Anh, Phần Lan, Pháp, Đức, Hebrew, Hungary, Ý, Nhật Bản, Hàn Quốc, Na Uy, Ba Lan, Bồ Đào Nha, Nga, Tây Ban Nha, Thụy Điển, Thái Lan, Thổ Nhĩ Kỳ, Ukraina) và tăng cường hỗ trợ ngữ cảnh dài hơn.

Phi-3.5-mini với 3.8 tỷ tham số vượt trội so với các mô hình cùng kích cỡ và tương đương với mô hình có kích thước gấp đôi.

### Phi-3 / 3.5 Vision

Có thể coi mô hình Instruct của Phi-3/3.5 như khả năng hiểu của Phi, còn Vision là đôi mắt để Phi hiểu thế giới.


**Phi-3-Vision**

Phi-3-vision, với chỉ 4.2 tỷ tham số, tiếp tục xu hướng này và vượt trội so với các mô hình lớn hơn như Claude-3 Haiku và Gemini 1.0 Pro V trong các nhiệm vụ suy luận hình ảnh chung, OCR, và hiểu bảng biểu, sơ đồ.


**Phi-3.5-Vision**

Phi-3.5-Vision cũng là một bản nâng cấp của Phi-3-Vision, bổ sung hỗ trợ đa ảnh. Bạn có thể coi đây là cải tiến về thị giác, không chỉ nhìn thấy hình ảnh mà còn cả video.

Phi-3.5-vision vượt trội so với các mô hình lớn hơn như Claude-3.5 Sonnet và Gemini 1.5 Flash trong các nhiệm vụ OCR, hiểu bảng biểu và biểu đồ, và tương đương trong các nhiệm vụ suy luận kiến thức thị giác tổng quát. Hỗ trợ đầu vào đa khung hình, tức là thực hiện suy luận trên nhiều hình ảnh đầu vào.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** cho phép mô hình được huấn luyện trước với ít tài nguyên tính toán hơn nhiều, nghĩa là bạn có thể mở rộng quy mô mô hình hoặc bộ dữ liệu một cách đáng kể với ngân sách tính toán tương đương mô hình đặc (dense). Cụ thể, một mô hình MoE nên đạt chất lượng tương đương với mô hình đặc của nó nhanh hơn nhiều trong quá trình huấn luyện trước.

Phi-3.5-MoE bao gồm 16 mô-đun chuyên gia 3.8B. Phi-3.5-MoE với chỉ 6.6 tỷ tham số hoạt động đạt mức suy luận, hiểu ngôn ngữ và toán học tương tự các mô hình lớn hơn nhiều.

Chúng ta có thể sử dụng mô hình Gia đình Phi-3/3.5 dựa trên các kịch bản khác nhau. Không giống LLM, bạn có thể triển khai Phi-3/3.5-mini hoặc Phi-3/3.5-Vision trên các thiết bị biên.


## Cách sử dụng các mô hình Gia đình Phi-3/3.5

Chúng tôi hy vọng sử dụng Phi-3/3.5 trong các kịch bản khác nhau. Tiếp theo, chúng ta sẽ sử dụng Phi-3/3.5 dựa trên các kịch bản khác nhau.

![phi3](../../../translated_images/vi/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Suy luận qua API Đám mây

**Microsoft Foundry Models**

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) là bản thay thế trực tiếp.

> **Lưu ý:** Toàn bộ gia đình Phi-3/3.5 (các biến thể Instruct, Vision và MoE) đã được rút khỏi danh mục Microsoft Foundry Models vào ngày 2025-08-30. Thay vào đó, sử dụng `Phi-4` (Instruct) hoặc `Phi-4-mini-instruct` — các ví dụ Phi-3/3.5 dưới đây vẫn hoạt động qua Hugging Face, Ollama, ONNX Runtime và NVIDIA NIM.

Microsoft Foundry Models hiện cung cấp các phiên bản kế nhiệm Phi-4. Sử dụng `Phi-4` hoặc `Phi-4-mini-instruct` thay cho các mô hình Phi-3/3.5 đã ngừng hoạt động khi theo các ví dụ API đám mây.

- Demo: So sánh hiệu quả của Phi-3-mini và Phi-3.5-mini trong các kịch bản tiếng Trung

![phi3](../../../translated_images/vi/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/vi/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Nếu bạn muốn sử dụng các mô hình thị giác (đa phương thức) trên đám mây, hãy dùng `Phi-4-multimodal-instruct` hiện có qua Microsoft Foundry thay vì các mô hình Phi-3/3.5 Vision đã ngừng hoạt động; đối với các tác vụ văn bản dùng `Phi-4` hoặc `Phi-4-mini-instruct`. Mô hình Phi-3.5 MoE đã được rút khỏi Microsoft Foundry, nên dùng các lựa chọn khác mô tả trong bài học này (ví dụ Hugging Face) nếu bạn muốn thử nghiệm. Nếu quan tâm, bạn có thể đọc Phi Cookbook để học cách gọi các mô hình Phi qua Microsoft Foundry [Nhấp vào liên kết này](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bên cạnh danh mục Microsoft Foundry Models trên đám mây, bạn cũng có thể sử dụng [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) để hoàn tất các cuộc gọi liên quan. Bạn có thể truy cập NVIDIA NIM để hoàn thành các cuộc gọi API cho Gia đình Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) là tập hợp các dịch vụ suy luận tăng tốc được thiết kế giúp các nhà phát triển triển khai mô hình AI hiệu quả trên nhiều môi trường khác nhau, bao gồm đám mây, trung tâm dữ liệu và máy trạm.

Dưới đây là một số tính năng chính của NVIDIA NIM:

- **Dễ Dàng Triển Khai:** NIM cho phép triển khai các mô hình AI chỉ với một lệnh duy nhất, giúp tích hợp dễ dàng vào quy trình làm việc hiện có.
- **Hiệu Suất Tối Ưu:** Nó tận dụng các engine suy luận được tối ưu sẵn của NVIDIA, như TensorRT và TensorRT-LLM, để đảm bảo độ trễ thấp và thông lượng cao.
- **Khả Năng Mở Rộng:** NIM hỗ trợ tự động mở rộng trên Kubernetes, cho phép xử lý hiệu quả các tải công việc thay đổi.
- **Bảo Mật và Kiểm Soát:** Các tổ chức có thể duy trì kiểm soát dữ liệu và ứng dụng của mình bằng cách tự lưu trữ các dịch vụ micro của NIM trên cơ sở hạ tầng quản lý riêng.
- **API Chuẩn:** NIM cung cấp các API theo tiêu chuẩn ngành, giúp dễ dàng xây dựng và tích hợp ứng dụng AI như chatbot, trợ lý AI, và nhiều hơn nữa.

NIM là một phần của NVIDIA AI Enterprise, nhằm đơn giản hóa việc triển khai và vận hành các mô hình AI, đảm bảo chúng chạy hiệu quả trên GPU NVIDIA.

- Bản demo: Sử dụng NVIDIA NIM để gọi Phi-3.5-Vision-API  [[Nhấn vào liên kết này](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Chạy Phi-3/3.5 Cục Bộ
Suy luận liên quan đến Phi-3, hoặc bất kỳ mô hình ngôn ngữ nào như GPT-3, đề cập đến quá trình tạo ra các phản hồi hoặc dự đoán dựa trên đầu vào nó nhận được. Khi bạn cung cấp một câu hỏi hoặc yêu cầu cho Phi-3, nó sử dụng mạng nơ-ron đã được huấn luyện để suy ra phản hồi có khả năng và phù hợp nhất bằng cách phân tích các mẫu và mối quan hệ trong dữ liệu đã được huấn luyện.

**Hugging Face Transformer**
Hugging Face Transformers là một thư viện mạnh mẽ được thiết kế cho xử lý ngôn ngữ tự nhiên (NLP) và các tác vụ học máy khác. Dưới đây là một số điểm chính về nó:

1. **Mô Hình Đã Huấn Luyện Sẵn**: Nó cung cấp hàng nghìn mô hình đã được huấn luyện sẵn có thể sử dụng cho nhiều tác vụ như phân loại văn bản, nhận diện thực thể có tên, trả lời câu hỏi, tóm tắt, dịch thuật và tạo văn bản.

2. **Tương Thích Khung Làm Việc:** Thư viện hỗ trợ nhiều khung học sâu khác nhau, bao gồm PyTorch, TensorFlow, và JAX. Điều này cho phép bạn huấn luyện mô hình trên một khung và sử dụng nó trên khung khác.

3. **Khả Năng Đa Phương Tiện:** Bên cạnh NLP, Hugging Face Transformers còn hỗ trợ các tác vụ trong thị giác máy tính (ví dụ, phân loại ảnh, phát hiện vật thể) và xử lý âm thanh (ví dụ nhận dạng giọng nói, phân loại âm thanh).

4. **Dễ Sử Dụng:** Thư viện cung cấp API và công cụ để dễ dàng tải xuống và tinh chỉnh mô hình, giúp tiếp cận được cho cả người mới và chuyên gia.

5. **Cộng Đồng và Tài Nguyên:** Hugging Face có một cộng đồng sôi nổi cùng tài liệu phong phú, các bài hướng dẫn và chỉ dẫn giúp người dùng bắt đầu và tận dụng tối đa thư viện.
[tài liệu chính thức](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) hoặc kho lưu trữ [GitHub của họ](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Đây là phương pháp phổ biến nhất, nhưng cũng đòi hỏi tăng tốc GPU. Sau cùng, các tình huống như Vision và MoE yêu cầu nhiều phép tính, sẽ rất chậm trên CPU nếu không được định lượng hóa.


- Bản demo: Sử dụng Transformer để gọi Phi-3.5-Instruct [Nhấn vào liên kết này](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Bản demo: Sử dụng Transformer để gọi Phi-3.5-Vision [Nhấn vào liên kết này](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Bản demo: Sử dụng Transformer để gọi Phi-3.5-MoE [Nhấn vào liên kết này](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) là một nền tảng được thiết kế để giúp chạy các mô hình ngôn ngữ lớn (LLM) dễ dàng hơn tại máy cục bộ của bạn. Nó hỗ trợ nhiều mô hình như Llama 3.1, Phi 3, Mistral, và Gemma 2, cùng nhiều mô hình khác. Nền tảng đơn giản hóa quá trình bằng cách đóng gói trọng số mô hình, cấu hình và dữ liệu thành một gói duy nhất, giúp người dùng dễ dàng tùy chỉnh và tạo mô hình của riêng họ. Ollama có sẵn cho macOS, Linux và Windows. Đây là công cụ tuyệt vời nếu bạn muốn thử nghiệm hoặc triển khai LLM mà không phụ thuộc vào dịch vụ đám mây. Ollama là cách trực tiếp nhất, bạn chỉ cần thực thi lệnh sau.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) là thời gian chạy ngoại tuyến trên thiết bị của Microsoft để chạy các mô hình như Phi hoàn toàn trên phần cứng của bạn – không cần đăng ký Azure, khóa API hoặc kết nối mạng. Nó tự động chọn nhà cung cấp thực hiện tốt nhất có sẵn (NPU, GPU hoặc CPU) và cung cấp một điểm cuối tương thích với OpenAI, do đó mã `openai`/Azure AI Inference SDK hiện tại có thể trỏ tới nó với ít thay đổi nhất. Xem [tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) để bắt đầu.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Hoặc sử dụng SDK trực tiếp trong Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime cho GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) là trình tăng tốc huấn luyện và suy luận học máy đa nền tảng. ONNX Runtime cho Generative AI (GENAI) là công cụ mạnh giúp bạn chạy các mô hình AI tạo nội dung hiệu quả trên nhiều nền tảng.

## ONNX Runtime là gì?
ONNX Runtime là dự án mã nguồn mở cho phép suy luận hiệu suất cao các mô hình học máy. Nó hỗ trợ các mô hình ở định dạng Open Neural Network Exchange (ONNX), một tiêu chuẩn để biểu diễn mô hình học máy. Suy luận với ONNX Runtime có thể mang lại trải nghiệm khách hàng nhanh hơn và giảm chi phí, hỗ trợ các mô hình từ các khung học sâu như PyTorch và TensorFlow/Keras cũng như các thư viện học máy cổ điển như scikit-learn, LightGBM, XGBoost, v.v. ONNX Runtime tương thích với nhiều phần cứng, trình điều khiển và hệ điều hành khác nhau, đồng thời cung cấp hiệu suất tối ưu bằng cách tận dụng các bộ tăng tốc phần cứng kèm theo tối ưu và biến đổi đồ thị.

## AI Tạo Sinh là gì?
AI tạo sinh đề cập đến các hệ thống AI có khả năng tạo ra nội dung mới, như văn bản, hình ảnh hoặc âm nhạc, dựa trên dữ liệu chúng được đào tạo. Ví dụ bao gồm các mô hình ngôn ngữ như GPT-3 và mô hình tạo hình ảnh như Stable Diffusion. Thư viện ONNX Runtime cho GenAI cung cấp vòng lặp AI tạo sinh cho các mô hình ONNX, bao gồm suy luận với ONNX Runtime, xử lý logits, tìm kiếm và mẫu lấy mẫu, cùng quản lý bộ nhớ cache KV.

## ONNX Runtime cho GENAI
ONNX Runtime cho GENAI mở rộng khả năng của ONNX Runtime để hỗ trợ các mô hình AI tạo sinh. Dưới đây là một số tính năng chính:

- **Hỗ Trợ Nhiều Nền Tảng:** Nó hoạt động trên nhiều nền tảng, bao gồm Windows, Linux, macOS, Android, và iOS.
- **Hỗ Trợ Mô Hình:** Nó hỗ trợ nhiều mô hình AI tạo sinh phổ biến, như LLaMA, GPT-Neo, BLOOM, và nhiều mô hình khác.
- **Tối Ưu Hiệu Suất:** Nó bao gồm các tối ưu cho các bộ tăng tốc phần cứng như GPU của NVIDIA, AMD, và nhiều hơn nữa.
- **Dễ Sử Dụng:** Nó cung cấp API để tích hợp dễ dàng vào các ứng dụng, cho phép bạn tạo văn bản, hình ảnh và nội dung khác với mã tối thiểu.
- Người dùng có thể gọi phương thức generate() cấp cao, hoặc chạy từng vòng lặp mô hình, tạo từng token một và tùy chọn cập nhật các tham số sinh trong vòng lặp.
- ONNX runtime cũng hỗ trợ tìm kiếm greedy/beam và lấy mẫu TopP, TopK để tạo chuỗi token và xử lý logits tích hợp như phạt lặp lại. Bạn cũng có thể dễ dàng thêm điểm số tùy chỉnh.

## Bắt Đầu
Để bắt đầu với ONNX Runtime cho GENAI, bạn có thể làm theo các bước sau:

### Cài đặt ONNX Runtime:
```Python
pip install onnxruntime
```
### Cài đặt phần mở rộng Generative AI:
```Python
pip install onnxruntime-genai
```

### Chạy Mô hình: Đây là một ví dụ đơn giản bằng Python:
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
### Bản demo: Sử dụng ONNX Runtime GenAI để gọi Phi-3.5-Vision


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

Ngoài ONNX Runtime, Ollama và các phương pháp tham khảo Foundry Local, chúng ta cũng có thể hoàn thiện tham khảo các mô hình định lượng dựa trên phương pháp tham khảo mô hình do các nhà sản xuất khác nhau cung cấp. Chẳng hạn như framework Apple MLX với Apple Metal, Qualcomm QNN với NPU, Intel OpenVINO với CPU/GPU, v.v. Bạn cũng có thể tìm thêm nội dung tại [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Thêm nữa

Chúng ta đã học các kiến thức cơ bản về gia đình Phi-3/3.5, nhưng để tìm hiểu thêm về SLM chúng ta cần thêm kiến thức. Bạn có thể tìm câu trả lời trong Phi-3 Cookbook. Nếu bạn muốn tìm hiểu thêm, vui lòng truy cập [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->