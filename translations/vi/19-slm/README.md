# Giới thiệu về Mô hình Ngôn ngữ Nhỏ cho Trí tuệ Nhân tạo Tạo sinh dành cho Người mới bắt đầu
Trí tuệ nhân tạo tạo sinh là một lĩnh vực hấp dẫn của trí tuệ nhân tạo, tập trung vào việc tạo ra các hệ thống có khả năng tạo nội dung mới. Nội dung này có thể bao gồm văn bản, hình ảnh, âm nhạc và thậm chí cả những môi trường ảo hoàn chỉnh. Một trong những ứng dụng thú vị nhất của trí tuệ nhân tạo tạo sinh là trong lĩnh vực mô hình ngôn ngữ.

## Mô hình Ngôn ngữ Nhỏ là gì?

Mô hình Ngôn ngữ Nhỏ (SLM) là một biến thể thu nhỏ của mô hình ngôn ngữ lớn (LLM), tận dụng nhiều nguyên tắc kiến trúc và kỹ thuật của LLM, trong khi thể hiện dấu chân tính toán nhỏ hơn đáng kể.

SLM là một tập hợp con của các mô hình ngôn ngữ được thiết kế để tạo ra văn bản giống như con người. Khác với các phiên bản lớn hơn như GPT-4, SLM nhỏ gọn và hiệu quả hơn, làm cho chúng trở nên lý tưởng cho các ứng dụng có tài nguyên tính toán hạn chế. Mặc dù kích thước nhỏ hơn, chúng vẫn có thể thực hiện nhiều tác vụ khác nhau. Thông thường, SLM được xây dựng bằng cách nén hoặc chưng cất các LLM, nhằm giữ lại phần lớn chức năng và khả năng ngôn ngữ của mô hình gốc. Việc giảm kích thước mô hình làm giảm độ phức tạp tổng thể, khiến SLM hiệu quả hơn cả về sử dụng bộ nhớ lẫn yêu cầu tính toán. Mặc dù có những tối ưu này, SLM vẫn có thể thực hiện đa dạng các nhiệm vụ xử lý ngôn ngữ tự nhiên (NLP):

- Tạo văn bản: Tạo các câu hoặc đoạn văn mạch lạc và phù hợp về ngữ cảnh.
- Hoàn thành văn bản: Dự đoán và hoàn thành câu dựa trên gợi ý cho trước.
- Dịch thuật: Chuyển đổi văn bản từ ngôn ngữ này sang ngôn ngữ khác.
- Tóm tắt: Rút gọn các đoạn văn dài thành các bản tóm tắt ngắn gọn, dễ hiểu hơn.

Tuy nhiên có một số đánh đổi về hiệu suất hoặc độ sâu hiểu biết so với các mô hình lớn hơn.

## Mô hình Ngôn ngữ Nhỏ hoạt động như thế nào?
SLM được huấn luyện trên một lượng lớn dữ liệu văn bản. Trong quá trình huấn luyện, chúng học các mẫu và cấu trúc của ngôn ngữ, giúp tạo ra văn bản vừa đúng ngữ pháp vừa phù hợp với ngữ cảnh. Quá trình huấn luyện bao gồm:

- Thu thập dữ liệu: Gom các bộ dữ liệu lớn từ nhiều nguồn khác nhau.
- Tiền xử lý: Làm sạch và tổ chức dữ liệu để phù hợp cho việc huấn luyện.
- Huấn luyện: Sử dụng các thuật toán máy học để dạy mô hình cách hiểu và tạo văn bản.
- Tinh chỉnh: Điều chỉnh mô hình để cải thiện hiệu suất trên các nhiệm vụ cụ thể.

Sự phát triển của SLM phù hợp với nhu cầu ngày càng tăng về các mô hình có thể triển khai trong môi trường hạn chế tài nguyên, chẳng hạn như thiết bị di động hoặc nền tảng điện toán biên, nơi LLM quy mô lớn có thể không thực tế do yêu cầu tài nguyên cao. Bằng cách tập trung vào hiệu quả, SLM cân bằng giữa hiệu suất và khả năng truy cập, cho phép ứng dụng rộng rãi hơn trong nhiều lĩnh vực.

![slm](../../../translated_images/vi/slm.4058842744d0444a.webp)

## Mục tiêu học tập

Trong bài học này, chúng tôi hy vọng giới thiệu kiến thức về SLM và kết hợp với Microsoft Phi-3 để tìm hiểu các kịch bản khác nhau trong nội dung văn bản, thị giác và MoE.

Sau khi kết thúc bài học này, bạn sẽ có thể trả lời các câu hỏi sau:

- SLM là gì?
- Sự khác biệt giữa SLM và LLM là gì?
- Microsoft Phi-3/3.5 Family là gì?
- Làm thế nào để thực hiện suy luận với Microsoft Phi-3/3.5 Family?

Sẵn sàng chưa? Hãy bắt đầu thôi.

## Sự khác biệt giữa Mô hình Ngôn ngữ Lớn (LLMs) và Mô hình Ngôn ngữ Nhỏ (SLMs)

Cả LLM và SLM đều được xây dựng trên các nguyên tắc cơ bản của máy học xác suất, theo những phương pháp tương tự trong thiết kế kiến trúc, phương pháp huấn luyện, quá trình tạo dữ liệu và kỹ thuật đánh giá mô hình. Tuy nhiên, có một số yếu tố chính phân biệt hai loại mô hình này.

## Ứng dụng của Mô hình Ngôn ngữ Nhỏ

SLM có nhiều ứng dụng đa dạng, bao gồm:

- Chatbot: Cung cấp hỗ trợ khách hàng và tương tác với người dùng theo cách hội thoại.
- Tạo nội dung: Hỗ trợ người viết bằng cách tạo ý tưởng hoặc thậm chí soạn thảo các bài viết hoàn chỉnh.
- Giáo dục: Giúp học sinh trong các bài tập viết hoặc học ngôn ngữ mới.
- Truy cập dễ dàng: Tạo công cụ cho người khuyết tật, chẳng hạn như hệ thống chuyển văn bản thành giọng nói.

**Kích thước**
  
Một điểm phân biệt chính giữa LLM và SLM nằm ở quy mô của mô hình. LLM như ChatGPT (GPT-4) có thể bao gồm khoảng 1,76 nghìn tỷ tham số, trong khi các SLM mã nguồn mở như Mistral 7B chỉ được thiết kế với số lượng tham số ít hơn đáng kể — khoảng 7 tỷ. Sự chênh lệch này chủ yếu do khác biệt về kiến trúc mô hình và quy trình huấn luyện. Ví dụ, ChatGPT sử dụng cơ chế tự chú ý trong khuôn khổ mã hóa-giải mã, trong khi Mistral 7B sử dụng cơ chế chú ý cửa sổ trượt, cho phép huấn luyện hiệu quả hơn trong một mô hình chỉ giải mã. Sự khác biệt kiến trúc này có ảnh hưởng sâu sắc đến độ phức tạp và hiệu suất của các mô hình.

**Hiểu biết**

SLM thường được tối ưu hóa cho hiệu suất trong các lĩnh vực cụ thể, khiến chúng rất chuyên biệt nhưng có thể hạn chế khả năng cung cấp hiểu biết bối cảnh rộng rãi qua nhiều lĩnh vực kiến thức khác nhau. Ngược lại, LLM hướng tới mô phỏng trí tuệ giống như con người ở mức độ toàn diện hơn. Được huấn luyện trên các bộ dữ liệu rộng lớn, đa dạng, LLM được thiết kế để hoạt động tốt trên nhiều lĩnh vực, mang lại tính đa dụng và khả năng thích ứng cao hơn. Do đó, LLM phù hợp hơn cho nhiều nhiệm vụ hạ nguồn, như xử lý ngôn ngữ tự nhiên và lập trình.

**Tính toán**

Việc huấn luyện và triển khai LLM tiêu tốn nhiều tài nguyên, thường yêu cầu hạ tầng tính toán mạnh mẽ bao gồm các cụm GPU quy mô lớn. Ví dụ, huấn luyện một mô hình như ChatGPT từ đầu có thể cần hàng nghìn GPU trong thời gian dài. Ngược lại, SLM với số lượng tham số nhỏ hơn dễ tiếp cận hơn về mặt tài nguyên tính toán. Các mô hình như Mistral 7B có thể được huấn luyện và chạy trên các máy cục bộ có khả năng GPU vừa phải, mặc dù huấn luyện vẫn đòi hỏi nhiều giờ trên nhiều GPU.

**Thiên kiến**

Thiên kiến là một vấn đề đã biết trong LLM, chủ yếu do tính chất dữ liệu huấn luyện. Các mô hình này thường dựa vào dữ liệu thô có sẵn trên internet, có thể thiếu hoặc đánh sai thông tin một số nhóm, gây nhãn sai, hoặc phản ánh thiên kiến ngôn ngữ bị ảnh hưởng bởi phương ngữ, sự khác biệt địa lý và quy tắc ngữ pháp. Thêm vào đó, sự phức tạp trong kiến trúc LLM có thể khiến thiên kiến trở nên trầm trọng hơn mà không dễ nhận thấy nếu không tinh chỉnh kỹ lưỡng. Mặt khác, SLM được huấn luyện trên các bộ dữ liệu hạn chế hơn, chuyên ngành hơn, nên ít bị ảnh hưởng bởi các thiên kiến này mặc dù không hoàn toàn miễn nhiễm.

**Suy luận**

Kích thước nhỏ hơn của SLM mang lại lợi thế lớn về tốc độ suy luận, cho phép chúng tạo ra kết quả hiệu quả trên phần cứng cục bộ mà không cần xử lý song song phức tạp. Trong khi đó, LLM do có kích thước và độ phức tạp cao thường cần tài nguyên tính toán song song lớn để đạt tốc độ suy luận chấp nhận được. Sự tồn tại của nhiều người dùng đồng thời càng làm chậm thời gian phản hồi của LLM, đặc biệt khi triển khai ở quy mô lớn.

Tóm lại, mặc dù cả LLM và SLM đều có nền tảng chung trong máy học, chúng khác biệt đáng kể về kích thước mô hình, yêu cầu tài nguyên, khả năng hiểu ngữ cảnh, mức độ bị thiên kiến và tốc độ suy luận. Những khác biệt này phản ánh sự phù hợp của từng loại cho các trường hợp sử dụng khác nhau, với LLM đa năng nhưng tốn tài nguyên, trong khi SLM hiệu quả hơn trong các lĩnh vực chuyên biệt với yêu cầu tính toán thấp hơn.

***Lưu ý: Trong bài học này, chúng tôi sẽ giới thiệu SLM sử dụng Microsoft Phi-3 / 3.5 làm ví dụ.***

## Giới thiệu về Phi-3 / Phi-3.5 Family

Phi-3 / 3.5 Family chủ yếu hướng tới các kịch bản ứng dụng về văn bản, thị giác và Agent (MoE):

### Phi-3 / 3.5 Instruct

Chủ yếu cho việc tạo văn bản, hoàn thành hội thoại, và trích xuất thông tin nội dung, v.v.

**Phi-3-mini**

Mô hình ngôn ngữ 3.8B có sẵn trên Microsoft Foundry, Hugging Face và Ollama. Các mô hình Phi-3 vượt trội đáng kể so với các mô hình ngôn ngữ có kích thước tương đương và lớn hơn trên các chuẩn đánh giá chính (xem số liệu chuẩn bên dưới, số cao hơn là tốt hơn). Phi-3-mini vượt trội hơn các mô hình gấp đôi kích thước, trong khi Phi-3-small và Phi-3-medium vượt trội các mô hình lớn hơn, bao gồm GPT-3.5.

**Phi-3-small & medium**

Với chỉ 7 tỷ tham số, Phi-3-small đánh bại GPT-3.5T trên nhiều bộ chuẩn ngôn ngữ, lập luận, lập trình và toán học.

Phi-3-medium với 14 tỷ tham số tiếp tục xu hướng này và vượt trội Gemini 1.0 Pro.

**Phi-3.5-mini**

Có thể xem nó như là bản nâng cấp của Phi-3-mini. Trong khi số tham số không đổi, nó cải thiện khả năng hỗ trợ đa ngôn ngữ (hỗ trợ hơn 20 ngôn ngữ: tiếng Ả Rập, Trung, Séc, Đan Mạch, Hà Lan, Anh, Phần Lan, Pháp, Đức, Hebrew, Hungary, Ý, Nhật, Hàn, Na Uy, Ba Lan, Bồ Đào Nha, Nga, Tây Ban Nha, Thụy Điển, Thái Lan, Thổ Nhĩ Kỳ, Ukraina) và tăng cường hỗ trợ cho ngữ cảnh dài.

Phi-3.5-mini với 3.8 tỷ tham số vượt trội các mô hình cùng kích thước và ngang bằng với các mô hình gấp đôi kích thước.

### Phi-3 / 3.5 Vision

Có thể coi mô hình Instruct của Phi-3/3.5 như khả năng hiểu của Phi, và Vision là đôi mắt của Phi để hiểu thế giới.


**Phi-3-Vision**

Phi-3-vision, chỉ với 4.2 tỷ tham số, vẫn tiếp tục xu hướng này và vượt trội các mô hình lớn hơn như Claude-3 Haiku và Gemini 1.0 Pro V trên các nhiệm vụ lý luận hình ảnh tổng quát, OCR, và hiểu bảng biểu, sơ đồ.


**Phi-3.5-Vision**

Phi-3.5-Vision cũng là bản nâng cấp của Phi-3-Vision, thêm khả năng hỗ trợ nhiều hình ảnh. Có thể xem đây là sự cải thiện về thị giác, không chỉ nhìn thấy hình ảnh mà còn cả video.

Phi-3.5-vision vượt trội các mô hình lớn hơn như Claude-3.5 Sonnet và Gemini 1.5 Flash trên các nhiệm vụ OCR, hiểu bảng biểu và biểu đồ, và tương đương trong các nhiệm vụ lý luận kiến thức thị giác tổng quát. Hỗ trợ nhập nhiều khung hình, tức là thực hiện suy luận trên nhiều hình ảnh đầu vào.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** cho phép các mô hình được tiền huấn luyện với tài nguyên tính toán ít hơn nhiều, nghĩa là bạn có thể mở rộng đáng kể quy mô mô hình hoặc tập dữ liệu với cùng ngân sách tính toán như mô hình đặc. Cụ thể, một mô hình MoE nên đạt chất lượng tương đương mô hình đặc cùng loại nhanh hơn nhiều trong quá trình tiền huấn luyện.

Phi-3.5-MoE bao gồm 16 mô-đun chuyên gia 3.8B. Phi-3.5-MoE với chỉ 6.6 tỷ tham số hoạt động đạt mức suy luận, hiểu ngôn ngữ, và toán học tương đương các mô hình lớn hơn nhiều.

Chúng ta có thể sử dụng mô hình Phi-3/3.5 Family dựa trên các kịch bản khác nhau. Khác với LLM, bạn có thể triển khai Phi-3/3.5-mini hoặc Phi-3/3.5-Vision trên các thiết bị biên.


## Cách sử dụng các mô hình Phi-3/3.5 Family

Chúng ta muốn sử dụng Phi-3/3.5 trong các kịch bản khác nhau. Tiếp theo, chúng ta sẽ sử dụng Phi-3/3.5 dựa trên từng kịch bản.

![phi3](../../../translated_images/vi/phi3.655208c3186ae381.webp)

### Suy luận qua API Đám mây

**Mô hình Microsoft Foundry**

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) là sự thay thế trực tiếp.

Microsoft Foundry Models là cách trực tiếp nhất. Bạn có thể nhanh chóng truy cập mô hình Phi-3/3.5-Instruct thông qua danh mục mô hình Foundry. Kết hợp với Azure AI Inference SDK / OpenAI SDK, bạn có thể gọi API thông qua mã để hoàn thành lời gọi Phi-3/3.5-Instruct. Bạn cũng có thể thử nghiệm các hiệu ứng khác nhau qua Playground.

- Demo: So sánh hiệu quả của Phi-3-mini và Phi-3.5-mini trong các kịch bản tiếng Trung

![phi3](../../../translated_images/vi/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/vi/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Hoặc nếu bạn muốn sử dụng các mô hình vision và MoE, bạn có thể sử dụng Microsoft Foundry để hoàn thành lời gọi. Nếu quan tâm, bạn có thể đọc Sổ tay Phi-3 để học cách gọi Phi-3/3.5 Instruct, Vision, MoE qua Microsoft Foundry [Nhấn vào liên kết này](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ngoài danh mục Microsoft Foundry Models trên đám mây, bạn cũng có thể sử dụng [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) để hoàn thành các cuộc gọi liên quan. Bạn có thể truy cập NVIDIA NIM để thực hiện các cuộc gọi API của Phi-3/3.5 Family. NVIDIA NIM (NVIDIA Inference Microservices) là một tập hợp các dịch vụ vi mô tăng tốc suy luận được thiết kế giúp các nhà phát triển triển khai mô hình AI hiệu quả trên nhiều môi trường, bao gồm đám mây, trung tâm dữ liệu và máy trạm.

Dưới đây là một vài tính năng chính của NVIDIA NIM:

- **Dễ dàng triển khai:** NIM cho phép triển khai mô hình AI chỉ với một lệnh duy nhất, giúp tích hợp dễ dàng vào các luồng công việc hiện có.

- **Hiệu suất tối ưu:** Nó tận dụng các động cơ suy luận được NVIDIA tối ưu sẵn, chẳng hạn như TensorRT và TensorRT-LLM, để đảm bảo độ trễ thấp và thông lượng cao.
- **Khả năng mở rộng:** NIM hỗ trợ tự động mở rộng trên Kubernetes, cho phép xử lý các khối lượng công việc biến đổi một cách hiệu quả.
- **Bảo mật và kiểm soát:** Các tổ chức có thể duy trì kiểm soát dữ liệu và ứng dụng của họ bằng cách tự lưu trữ các microservice NIM trên hạ tầng do họ quản lý.
- **API tiêu chuẩn:** NIM cung cấp các API tiêu chuẩn trong ngành, giúp dễ dàng xây dựng và tích hợp các ứng dụng AI như chatbot, trợ lý AI, và nhiều hơn nữa.

NIM là một phần của NVIDIA AI Enterprise, với mục tiêu đơn giản hóa việc triển khai và vận hành các mô hình AI, đảm bảo chúng chạy hiệu quả trên GPU của NVIDIA.

- Demo: Sử dụng NVIDIA NIM để gọi Phi-3.5-Vision-API  [[Nhấn vào đây](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Chạy Phi-3/3.5 Cục bộ
Suy luận liên quan đến Phi-3, hoặc bất kỳ mô hình ngôn ngữ nào như GPT-3, đề cập đến quá trình tạo phản hồi hoặc dự đoán dựa trên đầu vào nhận được. Khi bạn cung cấp một lời nhắc hoặc câu hỏi cho Phi-3, nó sử dụng mạng nơ-ron đã được huấn luyện để suy ra phản hồi có khả năng và phù hợp nhất bằng cách phân tích các mẫu và mối quan hệ trong dữ liệu mà nó đã được huấn luyện.

**Hugging Face Transformer**
Hugging Face Transformers là một thư viện mạnh mẽ được thiết kế cho xử lý ngôn ngữ tự nhiên (NLP) và các nhiệm vụ học máy khác. Dưới đây là một số điểm chính về nó:

1. **Mô hình được huấn luyện sẵn**: Nó cung cấp hàng nghìn mô hình đã được huấn luyện trước có thể dùng cho các nhiệm vụ khác nhau như phân loại văn bản, nhận dạng thực thể, trả lời câu hỏi, tổng hợp, dịch thuật, và tạo văn bản.

2. **Tương thích đa framework:** Thư viện hỗ trợ nhiều framework học sâu khác nhau, bao gồm PyTorch, TensorFlow và JAX. Điều này cho phép bạn huấn luyện mô hình trong một framework và sử dụng nó trong framework khác.

3. **Khả năng đa phương thức:** Ngoài NLP, Hugging Face Transformers còn hỗ trợ các nhiệm vụ trong thị giác máy tính (ví dụ: phân loại ảnh, phát hiện đối tượng) và xử lý âm thanh (ví dụ: nhận diện giọng nói, phân loại âm thanh).

4. **Dễ sử dụng:** Thư viện cung cấp các API và công cụ để dễ dàng tải xuống và tinh chỉnh mô hình, làm cho nó trở nên tiếp cận được với cả người mới bắt đầu và chuyên gia.

5. **Cộng đồng và tài nguyên:** Hugging Face có một cộng đồng sôi động và tài liệu, hướng dẫn cùng bài học phong phú để giúp người dùng bắt đầu và tận dụng tối đa thư viện.
[tài liệu chính thức](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) hoặc kho lưu trữ [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst) của họ.

Đây là phương pháp được sử dụng phổ biến nhất, nhưng cũng yêu cầu tăng tốc bằng GPU. Rốt cuộc, các kịch bản như Vision và MoE đòi hỏi nhiều phép tính, sẽ rất chậm trên CPU nếu không được lượng tử hóa.


- Demo: Sử dụng Transformer để gọi Phi-3.5-Instruct [Nhấn vào đây](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Sử dụng Transformer để gọi Phi-3.5-Vision [Nhấn vào đây](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Sử dụng Transformer để gọi Phi-3.5-MoE [Nhấn vào đây](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) là một nền tảng được thiết kế để giúp chạy các mô hình ngôn ngữ lớn (LLMs) dễ dàng hơn trên máy của bạn. Nó hỗ trợ các mô hình như Llama 3.1, Phi 3, Mistral, và Gemma 2, cùng nhiều mô hình khác. Nền tảng này đơn giản hóa quá trình bằng cách đóng gói trọng số mô hình, cấu hình và dữ liệu thành một gói duy nhất, giúp người dùng dễ dàng tùy chỉnh và tạo mô hình riêng của họ. Ollama có sẵn cho macOS, Linux và Windows. Đây là công cụ tuyệt vời nếu bạn muốn thử nghiệm hoặc triển khai LLM mà không phụ thuộc vào dịch vụ đám mây. Ollama là cách trực tiếp nhất, bạn chỉ cần chạy lệnh sau.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) là môi trường chạy trên thiết bị ngoại tuyến của Microsoft để chạy các mô hình như Phi hoàn toàn trên phần cứng của bạn - không cần đăng ký Azure, khóa API, hay kết nối mạng. Nó tự động chọn nhà cung cấp thực thi tốt nhất có sẵn (NPU, GPU, hoặc CPU) và cung cấp một điểm cuối tương thích với OpenAI, do đó mã SDK `openai`/Azure AI Inference hiện có có thể kết nối với nó chỉ với một vài thay đổi nhỏ. Xem [tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) để bắt đầu.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) là trình tăng tốc máy học cho suy luận và huấn luyện đa nền tảng. ONNX Runtime cho Generative AI (GENAI) là công cụ mạnh mẽ giúp bạn chạy các mô hình AI tạo sinh hiệu quả trên nhiều nền tảng khác nhau.

## ONNX Runtime là gì?
ONNX Runtime là một dự án mã nguồn mở cho phép suy luận hiệu suất cao các mô hình máy học. Nó hỗ trợ các mô hình ở định dạng Open Neural Network Exchange (ONNX), một tiêu chuẩn đại diện mô hình máy học. ONNX Runtime cho phép trải nghiệm khách hàng nhanh hơn và giảm chi phí, hỗ trợ các mô hình từ các framework học sâu như PyTorch và TensorFlow/Keras cũng như các thư viện máy học cổ điển như scikit-learn, LightGBM, XGBoost, v.v. ONNX Runtime tương thích với nhiều phần cứng, trình điều khiển và hệ điều hành khác nhau, và cung cấp hiệu suất tối ưu bằng cách tận dụng các bộ tăng tốc phần cứng khi có thể kèm theo tối ưu và biến đổi biểu đồ.

## AI Tạo Sinh là gì?
AI Tạo Sinh đề cập đến các hệ thống AI có khả năng tạo ra nội dung mới, như văn bản, hình ảnh, hoặc âm nhạc, dựa trên dữ liệu mà chúng đã được huấn luyện. Ví dụ bao gồm các mô hình ngôn ngữ như GPT-3 và các mô hình tạo hình ảnh như Stable Diffusion. Thư viện ONNX Runtime cho GenAI cung cấp vòng lặp tạo sinh AI cho các mô hình ONNX, bao gồm suy luận với ONNX Runtime, xử lý logits, tìm kiếm và lấy mẫu, cùng quản lý bộ nhớ đệm KV.

## ONNX Runtime cho GENAI
ONNX Runtime cho GENAI mở rộng khả năng của ONNX Runtime để hỗ trợ các mô hình AI tạo sinh. Dưới đây là một số tính năng chính:

- **Hỗ trợ nền tảng rộng:** Nó hoạt động trên nhiều nền tảng, bao gồm Windows, Linux, macOS, Android và iOS.
- **Hỗ trợ mô hình:** Hỗ trợ nhiều mô hình AI tạo sinh phổ biến, như LLaMA, GPT-Neo, BLOOM, và nhiều hơn nữa.
- **Tối ưu hiệu suất:** Bao gồm các tối ưu cho các bộ tăng tốc phần cứng khác nhau như GPU của NVIDIA, GPU của AMD, và hơn nữa.
- **Dễ sử dụng:** Cung cấp API để tích hợp dễ dàng vào ứng dụng, cho phép bạn tạo văn bản, hình ảnh, và nội dung khác với mã tối thiểu.
- Người dùng có thể gọi phương thức generate() ở cấp cao, hoặc chạy từng vòng lặp mô hình, tạo từng token một, và tùy chọn cập nhật các tham số tạo sinh trong vòng lặp.
- ONNX runtime cũng hỗ trợ tìm kiếm tham lam/beam search và lấy mẫu TopP, TopK để tạo chuỗi token và xử lý logits tích hợp như hình phạt lặp lại. Bạn cũng có thể dễ dàng thêm điểm số tùy chỉnh.

## Bắt đầu
Để bắt đầu với ONNX Runtime cho GENAI, bạn có thể làm theo các bước sau:

### Cài đặt ONNX Runtime:
```Python
pip install onnxruntime
```
### Cài đặt phần mở rộng Generative AI:
```Python
pip install onnxruntime-genai
```

### Chạy mô hình: Đây là một ví dụ đơn giản trong Python:
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


**Các phương pháp khác**

Ngoài các phương pháp tham khảo ONNX Runtime, Ollama và Foundry Local, chúng ta cũng có thể hoàn thành tham khảo các mô hình lượng tử dựa trên các phương pháp tham khảo mô hình từ các nhà sản xuất khác nhau. Ví dụ như framework Apple MLX với Apple Metal, Qualcomm QNN với NPU, Intel OpenVINO với CPU/GPU, v.v. Bạn cũng có thể xem thêm nội dung tại [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Thêm nữa

Chúng ta đã tìm hiểu cơ bản về dòng Phi-3/3.5, nhưng để học thêm về SLM chúng ta cần nhiều kiến thức hơn. Bạn có thể tìm câu trả lời trong Phi-3 Cookbook. Nếu muốn học thêm, hãy truy cập [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->