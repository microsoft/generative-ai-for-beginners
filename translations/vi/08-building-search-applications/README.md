<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T20:31:49+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "vi"
}
-->
# Xây dựng ứng dụng tìm kiếm

[![Giới thiệu về AI tạo sinh và Mô hình ngôn ngữ lớn](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.vi.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Nhấp vào hình ảnh trên để xem video của bài học này_

Mô hình ngôn ngữ lớn (LLMs) không chỉ dành cho chatbot và tạo văn bản. Bạn cũng có thể xây dựng ứng dụng tìm kiếm sử dụng Embeddings. Embeddings là các biểu diễn số của dữ liệu, còn được gọi là vector, và có thể được sử dụng để tìm kiếm ngữ nghĩa cho dữ liệu.

Trong bài học này, bạn sẽ xây dựng một ứng dụng tìm kiếm cho startup giáo dục của chúng tôi. Startup của chúng tôi là một tổ chức phi lợi nhuận cung cấp giáo dục miễn phí cho học sinh ở các nước đang phát triển. Startup của chúng tôi có một số lượng lớn video YouTube mà học sinh có thể sử dụng để học về AI. Startup của chúng tôi muốn xây dựng một ứng dụng tìm kiếm cho phép học sinh tìm kiếm video YouTube bằng cách nhập câu hỏi.

Ví dụ, một học sinh có thể nhập 'Jupyter Notebooks là gì?' hoặc 'Azure ML là gì?' và ứng dụng tìm kiếm sẽ trả về danh sách các video YouTube liên quan đến câu hỏi, và thậm chí tốt hơn, ứng dụng tìm kiếm sẽ trả về liên kết đến phần trong video nơi có câu trả lời cho câu hỏi.

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến:

- Tìm kiếm ngữ nghĩa so với tìm kiếm từ khóa.
- Text Embeddings là gì.
- Tạo một chỉ mục Text Embeddings.
- Tìm kiếm trong chỉ mục Text Embeddings.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Phân biệt giữa tìm kiếm ngữ nghĩa và tìm kiếm từ khóa.
- Giải thích Text Embeddings là gì.
- Tạo một ứng dụng sử dụng Embeddings để tìm kiếm dữ liệu.

## Tại sao xây dựng ứng dụng tìm kiếm?

Việc tạo một ứng dụng tìm kiếm sẽ giúp bạn hiểu cách sử dụng Embeddings để tìm kiếm dữ liệu. Bạn cũng sẽ học cách xây dựng một ứng dụng tìm kiếm mà học sinh có thể sử dụng để tìm thông tin một cách nhanh chóng.

Bài học bao gồm một chỉ mục Embedding của các bản ghi YouTube cho kênh YouTube [AI Show của Microsoft](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show là một kênh YouTube dạy bạn về AI và học máy. Chỉ mục Embedding chứa các Embeddings cho mỗi bản ghi YouTube cho đến tháng 10 năm 2023. Bạn sẽ sử dụng chỉ mục Embedding để xây dựng một ứng dụng tìm kiếm cho startup của chúng tôi. Ứng dụng tìm kiếm sẽ trả về liên kết đến phần trong video nơi có câu trả lời cho câu hỏi. Đây là một cách tuyệt vời để học sinh tìm thông tin họ cần một cách nhanh chóng.

Dưới đây là một ví dụ về truy vấn ngữ nghĩa cho câu hỏi 'bạn có thể sử dụng rstudio với azure ml không?'. Hãy kiểm tra URL YouTube, bạn sẽ thấy URL chứa một timestamp dẫn bạn đến phần trong video nơi có câu trả lời cho câu hỏi.

![Truy vấn ngữ nghĩa cho câu hỏi "bạn có thể sử dụng rstudio với Azure ML không"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.vi.png)

## Tìm kiếm ngữ nghĩa là gì?

Bây giờ bạn có thể đang tự hỏi, tìm kiếm ngữ nghĩa là gì? Tìm kiếm ngữ nghĩa là một kỹ thuật tìm kiếm sử dụng ngữ nghĩa, hoặc ý nghĩa, của các từ trong truy vấn để trả về kết quả liên quan.

Dưới đây là một ví dụ về tìm kiếm ngữ nghĩa. Giả sử bạn đang muốn mua một chiếc xe, bạn có thể tìm kiếm 'chiếc xe mơ ước của tôi', tìm kiếm ngữ nghĩa hiểu rằng bạn không `mơ` về một chiếc xe, mà thay vào đó bạn đang tìm mua chiếc xe `lý tưởng` của mình. Tìm kiếm ngữ nghĩa hiểu ý định của bạn và trả về kết quả liên quan. Ngược lại là `tìm kiếm từ khóa` sẽ tìm kiếm một cách trực tiếp về những giấc mơ liên quan đến xe và thường trả về kết quả không liên quan.

## Text Embeddings là gì?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) là một kỹ thuật biểu diễn văn bản được sử dụng trong [xử lý ngôn ngữ tự nhiên](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Text embeddings là các biểu diễn số ngữ nghĩa của văn bản. Embeddings được sử dụng để biểu diễn dữ liệu theo cách dễ hiểu đối với máy móc. Có nhiều mô hình để xây dựng text embeddings, trong bài học này, chúng ta sẽ tập trung vào việc tạo embeddings sử dụng Mô hình Embedding của OpenAI.

Dưới đây là một ví dụ, hãy tưởng tượng đoạn văn bản sau nằm trong bản ghi của một tập trên kênh YouTube AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Chúng ta sẽ truyền đoạn văn bản này đến API Embedding của OpenAI và nó sẽ trả về embedding gồm 1536 số, còn gọi là vector. Mỗi số trong vector đại diện cho một khía cạnh khác nhau của văn bản. Để ngắn gọn, đây là 10 số đầu tiên trong vector.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Chỉ mục Embedding được tạo như thế nào?

Chỉ mục Embedding cho bài học này được tạo bằng một loạt các script Python. Bạn sẽ tìm thấy các script cùng với hướng dẫn trong [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) trong thư mục 'scripts' của bài học này. Bạn không cần chạy các script này để hoàn thành bài học vì chỉ mục Embedding đã được cung cấp cho bạn.

Các script thực hiện các thao tác sau:

1. Bản ghi cho mỗi video YouTube trong danh sách phát [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) được tải xuống.
2. Sử dụng [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), một nỗ lực được thực hiện để trích xuất tên người nói từ 3 phút đầu tiên của bản ghi YouTube. Tên người nói cho mỗi video được lưu trong chỉ mục Embedding có tên `embedding_index_3m.json`.
3. Văn bản bản ghi sau đó được chia thành **các đoạn văn bản 3 phút**. Đoạn văn bản bao gồm khoảng 20 từ chồng lấn từ đoạn tiếp theo để đảm bảo rằng Embedding cho đoạn không bị cắt và cung cấp ngữ cảnh tìm kiếm tốt hơn.
4. Mỗi đoạn văn bản sau đó được truyền đến API Chat của OpenAI để tóm tắt văn bản thành 60 từ. Bản tóm tắt cũng được lưu trong chỉ mục Embedding `embedding_index_3m.json`.
5. Cuối cùng, đoạn văn bản được truyền đến API Embedding của OpenAI. API Embedding trả về một vector gồm 1536 số đại diện cho ý nghĩa ngữ nghĩa của đoạn văn bản. Đoạn văn bản cùng với vector Embedding của OpenAI được lưu trong chỉ mục Embedding `embedding_index_3m.json`.

### Cơ sở dữ liệu vector

Để đơn giản hóa bài học, chỉ mục Embedding được lưu trong tệp JSON có tên `embedding_index_3m.json` và được tải vào Pandas DataFrame. Tuy nhiên, trong môi trường sản xuất, chỉ mục Embedding sẽ được lưu trong cơ sở dữ liệu vector như [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), chỉ để kể một vài.

## Hiểu về độ tương đồng cosine

Chúng ta đã học về text embeddings, bước tiếp theo là học cách sử dụng text embeddings để tìm kiếm dữ liệu và đặc biệt là tìm các embeddings tương tự nhất với một truy vấn cụ thể bằng cách sử dụng độ tương đồng cosine.

### Độ tương đồng cosine là gì?

Độ tương đồng cosine là một thước đo sự tương đồng giữa hai vector, bạn cũng sẽ nghe điều này được gọi là `tìm kiếm láng giềng gần nhất`. Để thực hiện tìm kiếm độ tương đồng cosine, bạn cần _vector hóa_ văn bản _truy vấn_ bằng cách sử dụng API Embedding của OpenAI. Sau đó tính toán _độ tương đồng cosine_ giữa vector truy vấn và mỗi vector trong chỉ mục Embedding. Hãy nhớ rằng, chỉ mục Embedding có một vector cho mỗi đoạn văn bản bản ghi YouTube. Cuối cùng, sắp xếp kết quả theo độ tương đồng cosine và các đoạn văn bản có độ tương đồng cosine cao nhất là tương tự nhất với truy vấn.

Từ góc độ toán học, độ tương đồng cosine đo lường cosine của góc giữa hai vector được chiếu trong không gian đa chiều. Phép đo này rất hữu ích, vì nếu hai tài liệu cách xa nhau theo khoảng cách Euclidean do kích thước, chúng vẫn có thể có góc nhỏ hơn giữa chúng và do đó có độ tương đồng cosine cao hơn. Để biết thêm thông tin về các phương trình độ tương đồng cosine, hãy xem [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Xây dựng ứng dụng tìm kiếm đầu tiên của bạn

Tiếp theo, chúng ta sẽ học cách xây dựng một ứng dụng tìm kiếm sử dụng Embeddings. Ứng dụng tìm kiếm sẽ cho phép học sinh tìm kiếm video bằng cách nhập câu hỏi. Ứng dụng tìm kiếm sẽ trả về danh sách các video liên quan đến câu hỏi. Ứng dụng tìm kiếm cũng sẽ trả về liên kết đến phần trong video nơi có câu trả lời cho câu hỏi.

Giải pháp này được xây dựng và kiểm tra trên Windows 11, macOS, và Ubuntu 22.04 sử dụng Python 3.10 hoặc mới hơn. Bạn có thể tải Python từ [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Bài tập - xây dựng ứng dụng tìm kiếm, để hỗ trợ học sinh

Chúng tôi đã giới thiệu startup của mình ở đầu bài học này. Bây giờ là lúc hỗ trợ học sinh xây dựng một ứng dụng tìm kiếm cho các bài tập của họ.

Trong bài tập này, bạn sẽ tạo các dịch vụ Azure OpenAI được sử dụng để xây dựng ứng dụng tìm kiếm. Bạn sẽ tạo các dịch vụ Azure OpenAI sau. Bạn sẽ cần một tài khoản Azure để hoàn thành bài tập này.

### Bắt đầu Azure Cloud Shell

1. Đăng nhập vào [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Chọn biểu tượng Cloud Shell ở góc trên bên phải của Azure portal.
3. Chọn **Bash** cho loại môi trường.

#### Tạo một nhóm tài nguyên

> Đối với các hướng dẫn này, chúng tôi sử dụng nhóm tài nguyên có tên "semantic-video-search" ở East US.
> Bạn có thể thay đổi tên nhóm tài nguyên, nhưng khi thay đổi vị trí cho các tài nguyên,
> hãy kiểm tra [bảng khả dụng mô hình](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Tạo tài nguyên dịch vụ Azure OpenAI

Từ Azure Cloud Shell, chạy lệnh sau để tạo tài nguyên dịch vụ Azure OpenAI.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Lấy endpoint và khóa để sử dụng trong ứng dụng này

Từ Azure Cloud Shell, chạy các lệnh sau để lấy endpoint và khóa cho tài nguyên dịch vụ Azure OpenAI.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Triển khai mô hình Embedding của OpenAI

Từ Azure Cloud Shell, chạy lệnh sau để triển khai mô hình Embedding của OpenAI.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Giải pháp

Mở [notebook giải pháp](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) trong GitHub Codespaces và làm theo hướng dẫn trong Jupyter Notebook.

Khi bạn chạy notebook, bạn sẽ được yêu cầu nhập một truy vấn. Hộp nhập sẽ trông như thế này:

![Hộp nhập để người dùng nhập truy vấn](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.vi.png)

## Làm tốt lắm! Tiếp tục học tập của bạn

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học về AI tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI tạo sinh!

Hãy chuyển sang Bài học 9, nơi chúng ta sẽ tìm hiểu cách [xây dựng ứng dụng tạo hình ảnh](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính xác nhất. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.