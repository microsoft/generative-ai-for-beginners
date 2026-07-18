# Tài nguyên cho việc tự học

Bài học được xây dựng dựa trên các tài nguyên chính từ OpenAI và Microsoft Foundry làm tham khảo cho thuật ngữ và hướng dẫn. Dưới đây là danh sách không đầy đủ để bạn tự mình khám phá. Mỗi liên kết dưới đây dẫn đến tài liệu hiện tại, được hỗ trợ.

## 1. Tài nguyên chính

| Tiêu đề/Liên kết | Mô tả |
| :--- | :--- |
| [Fine-tuning with OpenAI Models](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fine-tuning cải thiện việc học ít ví dụ bằng cách huấn luyện trên nhiều ví dụ hơn so với những gì có thể đưa vào prompt - tiết kiệm chi phí, nâng cao chất lượng phản hồi và cho phép yêu cầu có độ trễ thấp hơn. **Tìm hiểu tổng quan về fine-tuning từ OpenAI.** |
| [When to use Microsoft Foundry fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Hiểu **fine-tuning là gì (khái niệm)**, tại sao bạn nên cân nhắc, dữ liệu nào để sử dụng, và cách đo lường chất lượng - cùng với khi nào SFT, DPO hoặc RFT là phù hợp. |
| [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Quy trình **từng bước (cách làm)** để fine-tuning trong Microsoft Foundry sử dụng portal, OpenAI / Foundry Python SDK, hoặc REST API - bao gồm chuẩn bị dữ liệu, huấn luyện, checkpoint, và triển khai. |
| [Continuous fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Quá trình lặp lại chọn một mô hình đã được fine-tune làm mô hình cơ sở và **tiếp tục fine-tune thêm** trên các bộ dữ liệu huấn luyện mới. |
| [Fine-tuning with tool (function) calling](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Fine-tuning mô hình của bạn **với ví dụ gọi công cụ (hàm)** giúp cải thiện đầu ra - phản hồi chính xác hơn, đồng nhất, định dạng tương tự với ít token prompt hơn. |
| [Fine-tuning models: Microsoft Foundry guidance](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Tra cứu **mô hình nào có thể fine-tune**, các phương pháp hỗ trợ (SFT / DPO / RFT) và các khu vực mà chúng có sẵn. |
| [Fine-tuning overview: techniques and modalities](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | So sánh ba kỹ thuật huấn luyện (SFT, DPO, RFT) và hai kiểu hình thức (không máy chủ vs. tính toán được quản lý), với hướng dẫn chọn mô hình cơ sở và bắt đầu. |
| **Tutorial**: [Fine-tune a model in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Tạo một bộ dữ liệu mẫu, chuẩn bị fine-tuning, chạy công việc fine-tuning trên một mô hình đang được hỗ trợ như `gpt-4.1-mini`, và triển khai mô hình đã fine-tune trên Azure. |
| **Tutorial**: [Fine-tune models with serverless API deployments](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Tùy chỉnh các mô hình mở và đối tác (Phi, Llama, Mistral, và nhiều hơn nữa) cho bộ dữ liệu của bạn _sử dụng quy trình làm việc dựa trên giao diện người dùng, ít mã_ trong Microsoft Foundry. |
| **Tutorial**: [Fine-tune Hugging Face models on Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Fine-tune mô hình Hugging Face với thư viện `transformers` trên một GPU sử dụng Azure Databricks và Hugging Face Trainer. |
| **Training**: [Fine-tune a foundation model with Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Danh mục mô hình Azure Machine Learning cung cấp nhiều mô hình mã nguồn mở bạn có thể fine-tune. Một phần của [Lộ trình Học tập Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Tutorial**: [Azure OpenAI fine-tuning with Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Theo dõi và phân tích các công việc fine-tuning trên Azure với W&B. Mở rộng hướng dẫn fine-tuning OpenAI với các bước và theo dõi thí nghiệm dành riêng cho Azure. |

## 2. Tài nguyên phụ

Phần này thu thập các tài nguyên bổ sung đáng để khám phá mà chúng tôi chưa có thời gian đề cập trong bài học. Hãy dùng chúng để xây dựng kiến thức chuyên môn của riêng bạn về chủ đề này.

| Tiêu đề/Liên kết | Mô tả |
| :--- | :--- |
| **OpenAI Cookbook**: [Chuẩn bị và phân tích dữ liệu cho fine-tuning mô hình chat](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Tiền xử lý và phân tích bộ dữ liệu chat trước khi fine-tuning: kiểm tra lỗi định dạng, lấy thống kê cơ bản, và ước tính số token (và chi phí). Kết hợp với [hướng dẫn fine-tuning của OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Fine-tuning cho Retrieval Augmented Generation (RAG) với Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Một ví dụ toàn diện về fine-tuning mô hình OpenAI cho RAG, tích hợp Qdrant và học ít ví dụ để tăng hiệu suất và giảm sai lệch nội dung. |
| **OpenAI Cookbook**: [Fine-tuning GPT với Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Sử dụng W&B để theo dõi huấn luyện và fine-tuning mô hình. Đọc hướng dẫn [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) trước, sau đó thử bài tập Cookbook. |
| **Hugging Face Tutorial**: [Cách Fine-Tune LLMs với Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Fine-tune các LLM mở sử dụng Hugging Face TRL, Transformers, và datasets: định nghĩa trường hợp sử dụng, thiết lập môi trường phát triển, chuẩn bị bộ dữ liệu, fine-tune, đánh giá, và triển khai. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Thư viện không mã/ít mã từ Hugging Face để fine-tune nhiều loại mô hình. Chạy trên đám mây của bạn, trên Hugging Face Spaces, hoặc cục bộ qua giao diện GUI, CLI, hoặc cấu hình YAML. |
| **Unsloth**: [Hướng dẫn Fine-tuning LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Một khung làm việc mã nguồn mở giúp đơn giản hóa fine-tuning LLM cục bộ và học tăng cường, với các [notebook](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) sẵn sàng sử dụng. |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->