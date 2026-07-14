# Giới thiệu về Mô hình Ngôn ngữ Nhỏ cho AI Tạo Sinh dành cho Người mới bắt đầu
AI Tạo Sinh là một lĩnh vực hấp dẫn của trí tuệ nhân tạo tập trung vào việc tạo ra các hệ thống có khả năng sinh nội dung mới. Nội dung này có thể là văn bản, hình ảnh, âm nhạc và thậm chí cả môi trường ảo toàn diện. Một trong những ứng dụng thú vị nhất của AI tạo sinh là trong lĩnh vực các mô hình ngôn ngữ.

## Mô hình Ngôn ngữ Nhỏ là gì?

Mô hình Ngôn ngữ Nhỏ (SLM) là một phiên bản thu nhỏ của mô hình ngôn ngữ lớn (LLM), tận dụng nhiều nguyên tắc kiến trúc và kỹ thuật của LLM, trong khi thể hiện dấu chân tính toán giảm đáng kể.

SLM là một tập hợp con của các mô hình ngôn ngữ được thiết kế để tạo ra văn bản giống con người. Khác với các mô hình lớn hơn như GPT-4, SLM nhỏ gọn và hiệu quả hơn, làm cho chúng trở nên lý tưởng cho các ứng dụng có tài nguyên tính toán hạn chế. Mặc dù kích thước nhỏ hơn, chúng vẫn có thể thực hiện nhiều nhiệm vụ khác nhau. Thông thường, SLM được xây dựng bằng cách nén hoặc chưng cất các LLM nhằm giữ lại phần lớn chức năng và khả năng ngôn ngữ của mô hình gốc. Việc giảm kích thước mô hình giúp giảm độ phức tạp tổng thể, làm cho SLM hiệu quả hơn cả về sử dụng bộ nhớ lẫn yêu cầu tính toán. Mặc dù có những tối ưu này, SLM vẫn có thể thực hiện nhiều nhiệm vụ xử lý ngôn ngữ tự nhiên (NLP):

- Sinh văn bản: Tạo câu hoặc đoạn văn mạch lạc và phù hợp ngữ cảnh.
- Hoàn thành văn bản: Dự đoán và hoàn thành câu dựa trên đoạn gợi ý.
- Dịch thuật: Chuyển đổi văn bản từ ngôn ngữ này sang ngôn ngữ khác.
- Tóm tắt: Cô đọng các đoạn văn dài thành bản tóm tắt ngắn gọn và dễ hiểu hơn.

Tuy nhiên, có một số đánh đổi về hiệu suất hoặc mức độ hiểu biết sâu so với các mô hình lớn hơn.

## Mô hình Ngôn ngữ Nhỏ hoạt động như thế nào?
SLM được huấn luyện trên lượng lớn dữ liệu văn bản. Trong quá trình huấn luyện, chúng học các mẫu và cấu trúc của ngôn ngữ, cho phép tạo ra văn bản vừa chính xác ngữ pháp vừa phù hợp ngữ cảnh. Quá trình huấn luyện bao gồm:

- Thu thập dữ liệu: Thu thập các bộ dữ liệu lớn từ nhiều nguồn khác nhau.
- Tiền xử lý: Làm sạch và tổ chức dữ liệu để phù hợp cho việc huấn luyện.
- Huấn luyện: Sử dụng các thuật toán học máy để dạy mô hình hiểu và tạo văn bản.
- Tinh chỉnh: Điều chỉnh mô hình để cải thiện hiệu suất trong các tác vụ cụ thể.

Việc phát triển SLM phù hợp với nhu cầu gia tăng về các mô hình có thể triển khai trong môi trường tài nguyên hạn chế, chẳng hạn như thiết bị di động hoặc nền tảng tính toán biên, nơi các LLM quy mô lớn có thể không khả thi do yêu cầu tài nguyên nặng. Bằng cách tập trung vào hiệu quả, SLM cân bằng giữa hiệu suất và khả năng tiếp cận, cho phép ứng dụng rộng rãi hơn trong nhiều lĩnh vực.

![slm](../../../translated_images/vi/slm.4058842744d0444a.webp)

## Mục tiêu học tập

Trong bài học này, chúng ta hy vọng giới thiệu kiến thức về SLM và kết hợp nó với Microsoft Phi-3 để học các kịch bản khác nhau về nội dung văn bản, thị giác và MoE.

Cuối bài học, bạn sẽ có thể trả lời các câu hỏi sau:

- SLM là gì?
- Sự khác biệt giữa SLM và LLM là gì?
- Microsoft Phi-3/3.5 Family là gì?
- Cách thực hiện suy luận với Microsoft Phi-3/3.5 Family như thế nào?

Sẵn sàng chưa? Hãy bắt đầu nào.

## Sự khác biệt giữa Mô hình Ngôn ngữ Lớn (LLM) và Mô hình Ngôn ngữ Nhỏ (SLM)

Cả LLM và SLM đều được xây dựng trên các nguyên tắc cơ bản của học máy xác suất, theo các phương pháp tương tự trong thiết kế kiến trúc, phương pháp huấn luyện, quy trình tạo dữ liệu và kỹ thuật đánh giá mô hình. Tuy nhiên, có một số yếu tố chính phân biệt hai loại mô hình này.

## Các ứng dụng của Mô hình Ngôn ngữ Nhỏ

SLM có nhiều ứng dụng, bao gồm:

- Chatbot: Cung cấp hỗ trợ khách hàng và tương tác với người dùng theo cách hội thoại.
- Tạo nội dung: Hỗ trợ người viết tạo ý tưởng hoặc thậm chí soạn thảo toàn bộ bài viết.
- Giáo dục: Giúp học sinh làm bài tập viết hoặc học ngôn ngữ mới.
- Khả năng tiếp cận: Tạo công cụ cho người khuyết tật, ví dụ như hệ thống chuyển văn bản thành giọng nói.

**Kích thước**
  
Một phân biệt cơ bản giữa LLM và SLM nằm ở quy mô mô hình. LLM như ChatGPT (GPT-4) có thể gồm khoảng 1,76 nghìn tỷ tham số, trong khi các SLM mã nguồn mở như Mistral 7B được thiết kế với số tham số ít hơn nhiều - khoảng 7 tỷ. Sự khác biệt này chủ yếu đến từ khác biệt trong kiến trúc mô hình và quy trình huấn luyện. Ví dụ, ChatGPT sử dụng cơ chế tự chú ý trong khung mã hóa - giải mã, trong khi Mistral 7B sử dụng cơ chế chú ý cửa sổ trượt giúp huấn luyện hiệu quả hơn trong mô hình chỉ giải mã. Sự khác biệt kiến trúc này có ảnh hưởng sâu sắc đến độ phức tạp và hiệu suất của các mô hình.

**Khả năng Hiểu**

SLM thường được tối ưu về hiệu suất trong các lĩnh vực cụ thể, làm chúng rất chuyên môn hóa nhưng có thể hạn chế khả năng cung cấp hiểu biết bối cảnh rộng lớn trên nhiều lĩnh vực kiến thức khác nhau. Ngược lại, LLM hướng đến mô phỏng trí tuệ giống con người ở phạm vi rộng hơn. Được huấn luyện trên các bộ dữ liệu đa dạng và rất lớn, LLM được thiết kế để hoạt động tốt trong nhiều lĩnh vực, mang lại sự đa dụng và thích nghi cao hơn. Do đó, LLM phù hợp hơn cho nhiều loại tác vụ hạ nguồn, như xử lý ngôn ngữ tự nhiên và lập trình.

**Tính toán**

Quá trình huấn luyện và triển khai LLM là tốn kém về tài nguyên, thường đòi hỏi hạ tầng tính toán lớn, bao gồm các cụm GPU quy mô lớn. Ví dụ, huấn luyện một mô hình như ChatGPT từ đầu có thể cần hàng ngàn GPU trong thời gian dài. Ngược lại, SLM với số tham số nhỏ hơn, dễ tiếp cận hơn về mặt tài nguyên tính toán. Các mô hình như Mistral 7B có thể được huấn luyện và chạy trên các máy cá nhân có GPU vừa phải, mặc dù huấn luyện vẫn yêu cầu vài giờ trên nhiều GPU.

**Định kiến**

Định kiến là vấn đề đã biết ở LLM, chủ yếu do bản chất dữ liệu huấn luyện. Các mô hình này thường dựa vào dữ liệu thô, công khai trên internet, có thể không phản ánh đầy đủ hoặc bị sai lệch về một số nhóm, gây ra nhãn sai hoặc phản ánh định kiến ngôn ngữ bị ảnh hưởng bởi phương ngữ, biến thể địa lý và quy tắc ngữ pháp. Thêm vào đó, sự phức tạp của kiến trúc LLM có thể vô tình làm trầm trọng thêm định kiến, điều này có thể không được phát hiện nếu không được tinh chỉnh cẩn thận. Trong khi đó, SLM, được huấn luyện trên các bộ dữ liệu giới hạn hơn, chuyên biệt theo lĩnh vực, vốn dĩ ít bị ảnh hưởng hơn bởi các định kiến như vậy, mặc dù không hoàn toàn miễn nhiễm.

**Suy luận**

Kích thước nhỏ hơn của SLM mang lại lợi thế đáng kể về tốc độ suy luận, cho phép chúng tạo ra đầu ra một cách hiệu quả trên phần cứng cục bộ mà không cần xử lý song song phức tạp. Ngược lại, LLM do kích thước và độ phức tạp của chúng thường đòi hỏi nhiều tài nguyên tính toán song song lớn để đạt thời gian suy luận chấp nhận được. Sự hiện diện của nhiều người dùng đồng thời còn làm chậm thời gian phản hồi của LLM, đặc biệt khi triển khai ở quy mô lớn.

Tóm lại, trong khi cả LLM và SLM đều có nền tảng học máy chung, chúng khác biệt đáng kể về kích thước mô hình, yêu cầu tài nguyên, khả năng hiểu bối cảnh, mức độ định kiến và tốc độ suy luận. Những điểm khác biệt này phản ánh sự phù hợp của chúng với các trường hợp sử dụng khác nhau, với LLM đa năng hơn nhưng chiếm nhiều tài nguyên, còn SLM mang lại hiệu quả theo lĩnh vực với yêu cầu tính toán giảm.

***Lưu ý: Trong bài học này, chúng ta sẽ giới thiệu SLM sử dụng Microsoft Phi-3 / 3.5 làm ví dụ.***

## Giới thiệu về dòng Phi-3 / Phi-3.5

Dòng Phi-3 / 3.5 chủ yếu nhắm đến các kịch bản ứng dụng về văn bản, thị giác và tác nhân (MoE):

### Phi-3 / 3.5 Instruct

Chủ yếu cho việc tạo văn bản, hoàn thành hội thoại và trích xuất thông tin nội dung, v.v.

**Phi-3-mini**

Mô hình ngôn ngữ 3.8 tỷ tham số có sẵn trên Microsoft Foundry, Hugging Face và Ollama. Các mô hình Phi-3 vượt trội đáng kể so với các mô hình ngôn ngữ cùng kích thước hoặc lớn hơn trên các bài kiểm tra chuẩn (xem số liệu benchmark dưới đây, số cao hơn là tốt hơn). Phi-3-mini vượt trội hơn các mô hình gấp đôi kích cỡ nó, trong khi Phi-3-small và Phi-3-medium vượt trội hơn các mô hình lớn hơn, bao gồm cả GPT-3.5.

**Phi-3-small & medium**

Với chỉ 7 tỷ tham số, Phi-3-small đánh bại GPT-3.5T trên nhiều bài kiểm tra về ngôn ngữ, lý luận, lập trình và toán học.

Phi-3-medium với 14 tỷ tham số tiếp tục xu hướng này và vượt trội hơn Gemini 1.0 Pro.

**Phi-3.5-mini**

Có thể coi đây là bản nâng cấp của Phi-3-mini. Mặc dù số tham số không đổi, nó cải thiện khả năng hỗ trợ đa ngôn ngữ (hỗ trợ hơn 20 ngôn ngữ: Ả Rập, Trung, Séc, Đan Mạch, Hà Lan, Anh, Phần Lan, Pháp, Đức, Do Thái, Hungary, Ý, Nhật, Hàn, Na Uy, Ba Lan, Bồ Đào Nha, Nga, Tây Ban Nha, Thụy Điển, Thái, Thổ Nhĩ Kỳ, Ukraina) và tăng cường hỗ trợ bối cảnh dài.

Phi-3.5-mini với 3.8 tỷ tham số vượt trội hơn các mô hình cùng kích cỡ và ngang bằng với các mô hình gấp đôi kích cỡ nó.

### Phi-3 / 3.5 Vision

Có thể coi mô hình Instruct của Phi-3/3.5 như khả năng hiểu của Phi, còn Vision chính là cặp mắt để Phi hiểu thế giới.


**Phi-3-Vision**

Phi-3-vision với chỉ 4.2 tỷ tham số tiếp tục xu hướng này và vượt trội hơn các mô hình lớn hơn như Claude-3 Haiku và Gemini 1.0 Pro V trong các nhiệm vụ lý luận thị giác tổng quát, OCR và hiểu bảng biểu, sơ đồ.


**Phi-3.5-Vision**

Phi-3.5-Vision cũng là bản nâng cấp của Phi-3-Vision, bổ sung hỗ trợ đa hình ảnh. Bạn có thể hiểu đây là cải thiện về thị giác, không chỉ nhìn thấy hình ảnh mà còn cả video.

Phi-3.5-vision vượt trội hơn các mô hình lớn hơn như Claude-3.5 Sonnet và Gemini 1.5 Flash trong các nhiệm vụ OCR, hiểu bảng biểu và biểu đồ, và ngang hàng trong các nhiệm vụ lý luận kiến thức thị giác tổng quát. Hỗ trợ đầu vào đa khung hình, tức là thực hiện lý luận trên nhiều hình ảnh đầu vào.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** cho phép mô hình được huấn luyện trước với lượng tính toán ít hơn nhiều, có nghĩa là bạn có thể dễ dàng mở rộng kích thước mô hình hoặc bộ dữ liệu với cùng ngân sách tính toán như mô hình dày đặc. Đặc biệt, mô hình MoE đạt chất lượng tương đương với mô hình dày đặc nhanh hơn đáng kể trong giai đoạn huấn luyện trước.

Phi-3.5-MoE bao gồm 16 module chuyên gia 3.8 tỷ tham số. Phi-3.5-MoE với chỉ 6.6 tỷ tham số kích hoạt đạt mức lý luận, hiểu ngôn ngữ và toán học tương tự các mô hình lớn hơn nhiều.

Chúng ta có thể sử dụng mô hình Phi-3/3.5 dựa trên các kịch bản khác nhau. Khác với LLM, bạn có thể triển khai Phi-3/3.5-mini hoặc Phi-3/3.5-Vision trên các thiết bị biên.


## Cách sử dụng các mô hình dòng Phi-3/3.5

Chúng ta hi vọng dùng Phi-3/3.5 trong các kịch bản khác nhau. Tiếp theo, ta sẽ sử dụng Phi-3/3.5 dựa trên các kịch bản khác nhau.

![phi3](../../../translated_images/vi/phi3.655208c3186ae381.webp)

### Suy luận qua API đám mây

**Mô hình Microsoft Foundry**

> **Lưu ý:** GitHub Models sẽ nghỉ hưu vào cuối tháng 7 năm 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) là sự thay thế trực tiếp.

Microsoft Foundry Models là cách thức trực tiếp nhất. Bạn có thể nhanh chóng truy cập mô hình Phi-3/3.5-Instruct qua danh mục mô hình Foundry. Kết hợp với Azure AI Inference SDK / OpenAI SDK, bạn có thể truy cập API qua code để hoàn thành cuộc gọi Phi-3/3.5-Instruct. Bạn cũng có thể thử nghiệm các hiệu ứng khác nhau qua Playground.

- Demo: So sánh hiệu quả của Phi-3-mini và Phi-3.5-mini trong các kịch bản tiếng Trung

![phi3](../../../translated_images/vi/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/vi/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Hoặc nếu bạn muốn sử dụng các mô hình thị giác và MoE, bạn có thể dùng Microsoft Foundry để thực hiện cuộc gọi. Nếu quan tâm, bạn có thể đọc cuốn sách nấu ăn Phi-3 để học cách gọi Phi-3/3.5 Instruct, Vision, MoE qua Microsoft Foundry [Nhấn vào đây](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ngoài danh mục Microsoft Foundry Models dựa trên đám mây, bạn cũng có thể sử dụng [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) để thực hiện các cuộc gọi liên quan. Bạn có thể truy cập NVIDIA NIM để hoàn thành các cuộc gọi API cho dòng Phi-3/3.5 Family. NVIDIA NIM (NVIDIA Inference Microservices) là một bộ các microservice suy luận tăng tốc thiết kế để giúp các nhà phát triển triển khai mô hình AI hiệu quả qua nhiều môi trường, bao gồm đám mây, trung tâm dữ liệu và trạm làm việc.

Dưới đây là một số tính năng chính của NVIDIA NIM:

- **Dễ dàng Triển khai:** NIM cho phép triển khai các mô hình AI chỉ với một lệnh, giúp tích hợp dễ dàng vào quy trình hiện có.

- **Hiệu suất tối ưu:** Nó tận dụng các công cụ suy luận được tối ưu hóa sẵn của NVIDIA, như TensorRT và TensorRT-LLM, để đảm bảo độ trễ thấp và thông lượng cao.
- **Khả năng mở rộng:** NIM hỗ trợ tự động mở rộng trên Kubernetes, giúp xử lý hiệu quả các khối lượng công việc khác nhau.
- **Bảo mật và kiểm soát:** Các tổ chức có thể duy trì kiểm soát dữ liệu và ứng dụng của mình bằng cách tự lưu trữ các dịch vụ vi mô NIM trên hạ tầng quản lý riêng.
- **API tiêu chuẩn:** NIM cung cấp các API chuẩn công nghiệp, giúp dễ dàng xây dựng và tích hợp các ứng dụng AI như chatbot, trợ lý AI và nhiều ứng dụng khác.

NIM là một phần của NVIDIA AI Enterprise, nhằm đơn giản hóa việc triển khai và vận hành các mô hình AI, đảm bảo chúng chạy hiệu quả trên GPU của NVIDIA.

- Demo: Sử dụng NVIDIA NIM để gọi Phi-3.5-Vision-API  [[Nhấn vào đây](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Chạy Phi-3/3.5 tại chỗ
Suy luận liên quan đến Phi-3, hoặc bất kỳ mô hình ngôn ngữ nào như GPT-3, đề cập đến quá trình tạo ra câu trả lời hoặc dự đoán dựa trên đầu vào nhận được. Khi bạn cung cấp một lời nhắc hoặc câu hỏi cho Phi-3, nó sử dụng mạng nơ-ron đã được huấn luyện để suy luận câu trả lời có khả năng và liên quan nhất bằng cách phân tích các mẫu và mối quan hệ trong dữ liệu đã được huấn luyện.

**Hugging Face Transformer**
Hugging Face Transformers là một thư viện mạnh mẽ thiết kế cho xử lý ngôn ngữ tự nhiên (NLP) và các tác vụ học máy khác. Dưới đây là một số điểm chính về nó:

1. **Mô hình đã được huấn luyện sẵn**: Nó cung cấp hàng ngàn mô hình được huấn luyện sẵn có thể sử dụng cho nhiều tác vụ như phân loại văn bản, nhận dạng thực thể có tên, trả lời câu hỏi, tóm tắt, dịch thuật và tạo văn bản.

2. **Tương thích đa khung làm việc:** Thư viện hỗ trợ nhiều khung học sâu khác nhau, bao gồm PyTorch, TensorFlow và JAX. Điều này cho phép bạn huấn luyện một mô hình trong một khung và sử dụng nó trong khung khác.

3. **Khả năng đa phương tiện:** Ngoài NLP, Hugging Face Transformers còn hỗ trợ các tác vụ trong thị giác máy tính (ví dụ: phân loại hình ảnh, phát hiện đối tượng) và xử lý âm thanh (ví dụ: nhận diện giọng nói, phân loại âm thanh).

4. **Dễ sử dụng:** Thư viện cung cấp các API và công cụ để dễ dàng tải xuống và tinh chỉnh mô hình, giúp người mới và chuyên gia đều có thể tiếp cận.

5. **Cộng đồng và tài nguyên:** Hugging Face có một cộng đồng sôi động và tài liệu, bài hướng dẫn, hướng dẫn phong phú để hỗ trợ người dùng bắt đầu và tận dụng tối đa thư viện.
[tài liệu chính thức](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) hoặc kho lưu trữ [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Đây là phương pháp được sử dụng phổ biến nhất, nhưng cũng cần tăng tốc bằng GPU. Đến cuối cùng, các kịch bản như Vision và MoE đòi hỏi rất nhiều phép tính, nếu không được lượng tử hóa thì sẽ rất chậm trên CPU.


- Demo: Sử dụng Transformer để gọi Phi-3.5-Instruct [Nhấn vào đây](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Sử dụng Transformer để gọi Phi-3.5-Vision [Nhấn vào đây](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Sử dụng Transformer để gọi Phi-3.5-MoE [Nhấn vào đây](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) là một nền tảng được thiết kế để giúp bạn dễ dàng chạy các mô hình ngôn ngữ lớn (LLM) tại chỗ trên máy của bạn. Nó hỗ trợ các mô hình khác nhau như Llama 3.1, Phi 3, Mistral, và Gemma 2, v.v. Nền tảng đơn giản hóa quá trình bằng cách đóng gói trọng số mô hình, cấu hình và dữ liệu thành một gói duy nhất, giúp người dùng dễ dàng tùy chỉnh và tạo ra mô hình riêng của mình. Ollama có sẵn cho macOS, Linux và Windows. Đây là công cụ tuyệt vời nếu bạn muốn thử nghiệm hoặc triển khai LLM mà không cần dựa vào dịch vụ đám mây. Ollama là cách trực tiếp nhất, bạn chỉ cần chạy lệnh sau.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) là môi trường chạy offline, ngay trên thiết bị của Microsoft để chạy các mô hình như Phi hoàn toàn trên phần cứng của bạn — không cần đăng ký Azure, khóa API, hay kết nối mạng. Nó tự động chọn nhà cung cấp thực thi tốt nhất hiện có (NPU, GPU, hoặc CPU) và cung cấp một điểm cuối tương thích OpenAI, giúp mã `openai`/Azure AI Inference SDK hiện có có thể kết nối với nó với ít thay đổi nhất. Xem [tài liệu Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) để bắt đầu.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Hoặc dùng trực tiếp SDK trong Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime cho GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) là trình tăng tốc suy luận và huấn luyện máy học đa nền tảng. ONNX Runtime cho Trí tuệ nhân tạo sinh tạo (GENAI) là công cụ mạnh mẽ giúp bạn chạy hiệu quả các mô hình AI sinh tạo trên nhiều nền tảng khác nhau. 

## ONNX Runtime là gì?
ONNX Runtime là một dự án mã nguồn mở giúp suy luận hiệu năng cao các mô hình máy học. Nó hỗ trợ các mô hình theo định dạng Open Neural Network Exchange (ONNX), một chuẩn để biểu diễn các mô hình máy học. Suy luận ONNX Runtime có thể giúp cải thiện trải nghiệm khách hàng nhanh hơn và giảm chi phí, hỗ trợ các mô hình từ các khung học sâu như PyTorch và TensorFlow/Keras cũng như các thư viện máy học truyền thống như scikit-learn, LightGBM, XGBoost, v.v. ONNX Runtime tương thích với nhiều phần cứng, trình điều khiển và hệ điều hành khác nhau, đồng thời cung cấp hiệu suất tối ưu bằng cách tận dụng các bộ tăng tốc phần cứng nơi phù hợp kèm theo tối ưu và chuyển đổi đồ thị.

## Trí tuệ nhân tạo sinh tạo là gì?
Trí tuệ nhân tạo sinh tạo đề cập đến các hệ thống AI có thể tạo ra nội dung mới, như văn bản, hình ảnh hoặc âm nhạc, dựa trên dữ liệu mà chúng đã được huấn luyện. Ví dụ bao gồm các mô hình ngôn ngữ như GPT-3 và các mô hình tạo hình ảnh như Stable Diffusion. Thư viện ONNX Runtime cho GenAI cung cấp vòng lặp AI sinh tạo cho các mô hình ONNX, bao gồm suy luận với ONNX Runtime, xử lý logits, tìm kiếm và lấy mẫu, và quản lý bộ nhớ đệm KV.

## ONNX Runtime cho GENAI
ONNX Runtime cho GENAI mở rộng khả năng của ONNX Runtime để hỗ trợ các mô hình AI sinh tạo. Dưới đây là một số tính năng chính:

- **Hỗ trợ nền tảng rộng rãi:** Nó hoạt động trên nhiều nền tảng khác nhau, bao gồm Windows, Linux, macOS, Android, và iOS.
- **Hỗ trợ mô hình:** Nó hỗ trợ nhiều mô hình AI sinh tạo phổ biến như LLaMA, GPT-Neo, BLOOM, và nhiều hơn nữa.
- **Tối ưu hóa hiệu suất:** Bao gồm các tối ưu hóa cho các bộ tăng tốc phần cứng khác nhau như GPU NVIDIA, GPU AMD, và nhiều hơn nữa2.
- **Dễ sử dụng:** Cung cấp API để tích hợp dễ dàng vào các ứng dụng, cho phép bạn tạo văn bản, hình ảnh và các nội dung khác chỉ với ít mã lệnh.
- Người dùng có thể gọi phương thức generate() cấp cao, hoặc chạy từng vòng lặp của mô hình, tạo từng token một, và tùy chọn cập nhật các tham số tạo trong vòng lặp.
- ONNX runtime cũng hỗ trợ tìm kiếm greedy/beam và lấy mẫu TopP, TopK để tạo chuỗi token và xử lý logits tích hợp như phạt lặp lại. Bạn cũng có thể dễ dàng thêm điểm số tùy chỉnh.

## Bắt đầu
Để bắt đầu với ONNX Runtime cho GENAI, bạn có thể làm theo các bước sau:

### Cài đặt ONNX Runtime:
```Python
pip install onnxruntime
```
### Cài đặt phần mở rộng AI sinh tạo:
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
### Demo:Sử dụng ONNX Runtime GenAI để gọi Phi-3.5-Vision


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

Bên cạnh các phương pháp tham khảo ONNX Runtime, Ollama và Foundry Local, chúng ta cũng có thể hoàn thành tham chiếu các mô hình định lượng dựa trên phương pháp tham khảo mô hình do các nhà sản xuất khác nhau cung cấp. Chẳng hạn như framework Apple MLX với Apple Metal, Qualcomm QNN với NPU, Intel OpenVINO với CPU/GPU, v.v. Bạn cũng có thể tham khảo thêm nội dung từ [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Thêm nữa

Chúng ta đã học những kiến thức cơ bản về gia đình Phi-3/3.5, nhưng để hiểu thêm về SLM chúng ta cần nhiều kiến thức hơn. Bạn có thể tìm câu trả lời trong Phi-3 Cookbook. Nếu muốn tìm hiểu thêm, vui lòng truy cập [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->