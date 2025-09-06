<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:20:55+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "vi"
}
-->
[![Mô hình Mã nguồn Mở](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.vi.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Giới thiệu

Thế giới của các LLM mã nguồn mở rất thú vị và không ngừng phát triển. Bài học này nhằm cung cấp cái nhìn sâu sắc về các mô hình mã nguồn mở. Nếu bạn đang tìm kiếm thông tin về cách so sánh giữa các mô hình độc quyền và mô hình mã nguồn mở, hãy truy cập bài học ["Khám phá và So sánh Các LLM Khác Nhau"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Bài học này cũng sẽ đề cập đến chủ đề tinh chỉnh mô hình, nhưng bạn có thể tìm thấy giải thích chi tiết hơn trong bài học ["Tinh chỉnh LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Mục tiêu học tập

- Hiểu rõ về các mô hình mã nguồn mở  
- Hiểu được lợi ích của việc làm việc với các mô hình mã nguồn mở  
- Khám phá các mô hình mã nguồn mở có sẵn trên Hugging Face và Azure AI Studio  

## Mô hình Mã nguồn Mở là gì?

Phần mềm mã nguồn mở đã đóng vai trò quan trọng trong sự phát triển của công nghệ trên nhiều lĩnh vực. Sáng kiến Mã nguồn Mở (OSI) đã định nghĩa [10 tiêu chí cho phần mềm](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) để được phân loại là mã nguồn mở. Mã nguồn phải được chia sẻ công khai dưới một giấy phép được OSI phê duyệt.

Mặc dù việc phát triển LLM có những yếu tố tương tự như phát triển phần mềm, nhưng quy trình này không hoàn toàn giống nhau. Điều này đã dẫn đến nhiều cuộc thảo luận trong cộng đồng về định nghĩa mã nguồn mở trong bối cảnh của LLM. Để một mô hình phù hợp với định nghĩa truyền thống của mã nguồn mở, các thông tin sau đây cần được công khai:

- Bộ dữ liệu được sử dụng để huấn luyện mô hình.  
- Toàn bộ trọng số mô hình như một phần của quá trình huấn luyện.  
- Mã đánh giá.  
- Mã tinh chỉnh.  
- Toàn bộ trọng số mô hình và các chỉ số huấn luyện.  

Hiện tại chỉ có một số ít mô hình đáp ứng các tiêu chí này. [Mô hình OLMo được tạo bởi Viện Allen về Trí tuệ Nhân tạo (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) là một ví dụ phù hợp với danh mục này.

Trong bài học này, chúng ta sẽ gọi các mô hình này là "mô hình mở" vì chúng có thể không đáp ứng đầy đủ các tiêu chí trên tại thời điểm viết bài.

## Lợi ích của Mô hình Mở

**Tùy chỉnh cao** - Vì các mô hình mở được phát hành với thông tin huấn luyện chi tiết, các nhà nghiên cứu và nhà phát triển có thể chỉnh sửa nội bộ của mô hình. Điều này cho phép tạo ra các mô hình chuyên biệt cao được tinh chỉnh cho một nhiệm vụ hoặc lĩnh vực nghiên cứu cụ thể. Một số ví dụ bao gồm tạo mã, các phép toán toán học và sinh học.

**Chi phí** - Chi phí trên mỗi token khi sử dụng và triển khai các mô hình này thấp hơn so với các mô hình độc quyền. Khi xây dựng các ứng dụng AI tạo sinh, cần xem xét hiệu suất so với giá cả khi làm việc với các mô hình này cho trường hợp sử dụng của bạn.

![Chi phí Mô hình](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.vi.png)  
Nguồn: Artificial Analysis  

**Linh hoạt** - Làm việc với các mô hình mở cho phép bạn linh hoạt trong việc sử dụng các mô hình khác nhau hoặc kết hợp chúng. Một ví dụ là [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), nơi người dùng có thể chọn mô hình được sử dụng trực tiếp trong giao diện người dùng:

![Chọn Mô hình](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.vi.png)

## Khám phá Các Mô hình Mở Khác Nhau

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), được phát triển bởi Meta, là một mô hình mở được tối ưu hóa cho các ứng dụng dựa trên hội thoại. Điều này là nhờ vào phương pháp tinh chỉnh của nó, bao gồm một lượng lớn dữ liệu hội thoại và phản hồi từ con người. Với phương pháp này, mô hình tạo ra các kết quả phù hợp hơn với kỳ vọng của con người, mang lại trải nghiệm người dùng tốt hơn.

Một số ví dụ về các phiên bản tinh chỉnh của Llama bao gồm [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), chuyên về tiếng Nhật và [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), là một phiên bản nâng cao của mô hình gốc.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) là một mô hình mở tập trung mạnh vào hiệu suất cao và hiệu quả. Nó sử dụng phương pháp Mixture-of-Experts, kết hợp một nhóm các mô hình chuyên gia chuyên biệt thành một hệ thống, trong đó tùy thuộc vào đầu vào, các mô hình nhất định sẽ được chọn để sử dụng. Điều này làm cho việc tính toán hiệu quả hơn vì các mô hình chỉ xử lý các đầu vào mà chúng chuyên về.

Một số ví dụ về các phiên bản tinh chỉnh của Mistral bao gồm [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), tập trung vào lĩnh vực y tế và [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), thực hiện các phép tính toán học.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) là một LLM được tạo bởi Viện Đổi mới Công nghệ (**TII**). Falcon-40B được huấn luyện trên 40 tỷ tham số, đã được chứng minh là hoạt động tốt hơn GPT-3 với ngân sách tính toán thấp hơn. Điều này là nhờ vào việc sử dụng thuật toán FlashAttention và multiquery attention, giúp giảm yêu cầu bộ nhớ trong thời gian suy luận. Với thời gian suy luận giảm, Falcon-40B phù hợp cho các ứng dụng hội thoại.

Một số ví dụ về các phiên bản tinh chỉnh của Falcon là [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), một trợ lý được xây dựng trên các mô hình mở và [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), mang lại hiệu suất cao hơn so với mô hình gốc.

## Cách Lựa Chọn

Không có câu trả lời duy nhất cho việc chọn một mô hình mở. Một nơi tốt để bắt đầu là sử dụng tính năng lọc theo nhiệm vụ của Azure AI Studio. Điều này sẽ giúp bạn hiểu các loại nhiệm vụ mà mô hình đã được huấn luyện. Hugging Face cũng duy trì một bảng xếp hạng LLM, hiển thị các mô hình hoạt động tốt nhất dựa trên các chỉ số nhất định.

Khi muốn so sánh các LLM trên các loại khác nhau, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) là một nguồn tài nguyên tuyệt vời khác:

![Chất lượng Mô hình](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.vi.png)  
Nguồn: Artificial Analysis  

Nếu làm việc trên một trường hợp sử dụng cụ thể, việc tìm kiếm các phiên bản tinh chỉnh tập trung vào cùng lĩnh vực có thể hiệu quả. Thử nghiệm với nhiều mô hình mở để xem chúng hoạt động như thế nào theo kỳ vọng của bạn và người dùng cũng là một thực hành tốt.

## Bước Tiếp Theo

Điều tuyệt vời nhất về các mô hình mở là bạn có thể bắt đầu làm việc với chúng khá nhanh chóng. Hãy xem [Danh mục Mô hình Azure AI Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), nơi có một bộ sưu tập Hugging Face cụ thể với các mô hình mà chúng ta đã thảo luận ở đây.

## Học không dừng lại ở đây, tiếp tục Hành trình

Sau khi hoàn thành bài học này, hãy xem [Bộ sưu tập Học AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.