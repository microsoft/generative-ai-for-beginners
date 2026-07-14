# Tạo Sinh Tăng Cường Truy Xuất (RAG) và Cơ Sở Dữ Liệu Vector

[![Tạo Sinh Tăng Cường Truy Xuất (RAG) và Cơ Sở Dữ Liệu Vector](../../../translated_images/vi/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Trong bài học ứng dụng tìm kiếm, chúng ta đã tìm hiểu ngắn gọn cách tích hợp dữ liệu của riêng bạn vào Mô Hình Ngôn Ngữ Lớn (LLMs). Trong bài học này, chúng ta sẽ khám phá sâu hơn về các khái niệm về căn cứ dữ liệu vào ứng dụng LLM của bạn, cơ chế của quy trình và các phương pháp lưu trữ dữ liệu, bao gồm cả embeddings và văn bản.

> **Video Sẽ Ra Mắt Sớm**

## Giới thiệu

Trong bài học này chúng ta sẽ đề cập đến:

- Giới thiệu về RAG, nó là gì và tại sao được sử dụng trong AI (trí tuệ nhân tạo).

- Hiểu về cơ sở dữ liệu vector là gì và cách tạo một cơ sở cho ứng dụng của chúng ta.

- Ví dụ thực tế về cách tích hợp RAG vào một ứng dụng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Giải thích tầm quan trọng của RAG trong việc truy xuất và xử lý dữ liệu.

- Thiết lập ứng dụng RAG và liên kết dữ liệu của bạn với một LLM

- Tích hợp hiệu quả RAG và Cơ Sở Dữ Liệu Vector trong Ứng Dụng LLM.

## Kịch bản của chúng ta: nâng cao LLM của chúng ta bằng dữ liệu riêng

Trong bài học này, chúng ta sẽ thêm các ghi chú của chính mình vào startup giáo dục, cho phép chatbot lấy thêm thông tin về các chủ đề khác nhau. Sử dụng các ghi chú có sẵn, người học sẽ có thể học tốt hơn và hiểu các chủ đề khác nhau, giúp việc ôn tập cho kỳ thi dễ dàng hơn. Để tạo kịch bản, chúng ta sẽ sử dụng:

- `Azure OpenAI:` LLM chúng ta sẽ dùng để tạo chatbot

- `Bài học AI cho người mới bắt đầu về Mạng Nơ-ron`: đây sẽ là dữ liệu căn cứ cho LLM của chúng ta

- `Azure AI Search` và `Azure Cosmos DB:` cơ sở dữ liệu vector để lưu trữ dữ liệu và tạo chỉ mục tìm kiếm

Người dùng sẽ có thể tạo các bài kiểm tra thực hành từ ghi chú của họ, thẻ flash ôn tập và tóm tắt thành các phần ngắn gọn. Để bắt đầu, hãy cùng tìm hiểu RAG là gì và cách nó hoạt động:

## Tạo Sinh Tăng Cường Truy Xuất (RAG)

Chatbot dựa trên LLM xử lý các yêu cầu của người dùng để tạo phản hồi. Nó được thiết kế để tương tác và giao tiếp với người dùng về nhiều chủ đề khác nhau. Tuy nhiên, câu trả lời bị giới hạn trong ngữ cảnh được cung cấp và dữ liệu đào tạo cơ bản của nó. Ví dụ, kiến thức của GPT-4 dừng lại vào tháng 9 năm 2021, nghĩa là nó không biết về các sự kiện xảy ra sau thời điểm đó. Ngoài ra, dữ liệu sử dụng để huấn luyện LLM không bao gồm thông tin bí mật như ghi chú cá nhân hoặc hướng dẫn sản phẩm của công ty.

### Cách mà RAG (Tạo Sinh Tăng Cường Truy Xuất) hoạt động

![bản vẽ minh họa cách hoạt động của RAG](../../../translated_images/vi/how-rag-works.f5d0ff63942bd3a6.webp)

Giả sử bạn muốn triển khai một chatbot tạo bài kiểm tra từ ghi chú, bạn sẽ cần kết nối với cơ sở tri thức. Đó là lúc RAG tham gia hỗ trợ. RAG hoạt động như sau:

- **Cơ sở tri thức:** Trước khi truy xuất, các tài liệu này cần được nhập và xử lý trước, thường là chia nhỏ tài liệu lớn thành các phần nhỏ hơn, chuyển đổi thành text embedding và lưu vào cơ sở dữ liệu.

- **Truy vấn người dùng:** người dùng đặt câu hỏi

- **Truy xuất:** Khi người dùng đặt câu hỏi, mô hình embedding sẽ truy xuất thông tin liên quan trong cơ sở tri thức để cung cấp thêm ngữ cảnh được tích hợp vào prompt.

- **Tăng cường tạo sinh:** LLM cải thiện phản hồi dựa trên dữ liệu được truy xuất. Điều này cho phép câu trả lời không chỉ dựa vào dữ liệu đã huấn luyện mà còn dựa trên thông tin liên quan từ ngữ cảnh thêm vào. Dữ liệu được truy xuất dùng để tăng cường các phản hồi LLM. Sau đó LLM trả lời câu hỏi người dùng.

![bản vẽ kiến trúc RAG](../../../translated_images/vi/encoder-decode.f2658c25d0eadee2.webp)

Kiến trúc RAG được triển khai sử dụng transformers gồm hai phần: bộ mã hóa và bộ giải mã. Ví dụ, khi người dùng hỏi một câu, văn bản đầu vào được 'mã hóa' thành các vector nắm bắt ý nghĩa của từ và các vector này được 'giải mã' vào chỉ mục tài liệu và sinh ra văn bản mới dựa trên truy vấn người dùng. LLM sử dụng mô hình encoder-decoder để tạo ra đầu ra.

Có hai cách tiếp cận khi triển khai RAG theo bài báo đề xuất: [Retrieval-Augmented Generation for Knowledge intensive NLP (xử lý ngôn ngữ tự nhiên)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) là:

- **_RAG-Sequence_** sử dụng các tài liệu truy xuất được để dự đoán câu trả lời tốt nhất cho truy vấn người dùng

- **RAG-Token** sử dụng tài liệu để tạo token tiếp theo, sau đó truy xuất chúng để trả lời truy vấn người dùng

### Tại sao bạn nên sử dụng RAG? 

- **Độ phong phú thông tin:** đảm bảo các phản hồi văn bản được cập nhật và mới nhất. Do đó, nâng cao hiệu suất cho các nhiệm vụ chuyên ngành bằng cách truy cập vào cơ sở tri thức nội bộ.

- Giảm thiểu tạo dựng thông tin sai lệch bằng cách sử dụng **dữ liệu có thể xác minh** trong cơ sở tri thức để cung cấp ngữ cảnh cho truy vấn người dùng.

- Có tính **hiệu quả về chi phí** vì nó tiết kiệm hơn so với việc tinh chỉnh một LLM

## Tạo cơ sở tri thức

Ứng dụng của chúng ta dựa trên dữ liệu cá nhân, tức là bài học Mạng Nơ-ron trong chương trình AI Cho Người Mới Bắt Đầu.

### Cơ Sở Dữ Liệu Vector

Cơ sở dữ liệu vector, khác với cơ sở dữ liệu truyền thống, là một loại cơ sở dữ liệu chuyên biệt thiết kế để lưu trữ, quản lý và tìm kiếm các vector nhúng. Nó lưu trữ các biểu diễn số học của tài liệu. Việc chuyển đổi dữ liệu thành các embedding số giúp hệ thống AI của chúng ta dễ hiểu và xử lý dữ liệu hơn.

Chúng ta lưu embeddings trong cơ sở dữ liệu vector vì LLM có giới hạn số token được nhận làm đầu vào. Vì không thể truyền toàn bộ embeddings vào LLM, chúng ta sẽ phải chia chúng thành các mảnh nhỏ và khi người dùng đặt câu hỏi, embeddings gần nhất với câu hỏi sẽ được trả về cùng với prompt. Việc chia nhỏ cũng giúp giảm chi phí về số token truyền qua LLM.

Một số cơ sở dữ liệu vector phổ biến bao gồm Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant và DeepLake. Bạn có thể tạo mô hình Azure Cosmos DB bằng Azure CLI với lệnh sau:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Từ văn bản đến embedding

Trước khi lưu trữ dữ liệu, chúng ta cần chuyển đổi nó thành vector embedding trước khi lưu vào cơ sở dữ liệu. Nếu bạn làm việc với tài liệu lớn hoặc văn bản dài, bạn có thể chia nhỏ dựa trên các truy vấn dự kiến. Việc chia nhỏ có thể thực hiện ở cấp câu hoặc đoạn văn. Vì chia nhỏ dựa trên ý nghĩa các từ xung quanh, bạn có thể thêm một số ngữ cảnh khác vào mảnh nhỏ, ví dụ thêm tiêu đề tài liệu hoặc một số đoạn văn trước hoặc sau mảnh đó. Bạn có thể chia nhỏ dữ liệu như sau:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # Nếu phần cuối cùng không đạt độ dài tối thiểu, vẫn thêm nó vào
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Khi đã chia nhỏ, chúng ta có thể nhúng văn bản bằng các mô hình embedding khác nhau. Một số mô hình bạn có thể sử dụng bao gồm: word2vec, ada-002 của OpenAI, Azure Computer Vision và nhiều mô hình khác. Lựa chọn mô hình tùy thuộc vào ngôn ngữ bạn dùng, loại nội dung mã hóa (văn bản/hình ảnh/âm thanh), kích thước đầu vào có thể mã hóa và độ dài đầu ra embedding.

Ví dụ embedding văn bản dùng mô hình `text-embedding-ada-002` của OpenAI là:
![một embedding của từ cat](../../../translated_images/vi/cat.74cbd7946bc9ca38.webp)

## Truy Xuất và Tìm Kiếm Vector

Khi người dùng đặt câu hỏi, hệ thống truy xuất sẽ chuyển đổi câu hỏi thành vector bằng bộ mã hóa truy vấn, sau đó tìm kiếm trong chỉ mục tài liệu cho các vector liên quan đến câu hỏi. Khi hoàn tất, nó chuyển cả vector đầu vào và vector tài liệu thành văn bản và gửi cho LLM.

### Truy xuất

Truy xuất xảy ra khi hệ thống cố gắng nhanh chóng tìm tài liệu từ chỉ mục phù hợp với tiêu chí tìm kiếm. Mục tiêu của bộ truy xuất là lấy tài liệu dùng làm ngữ cảnh và nền tảng cho LLM trên dữ liệu của bạn.

Có nhiều cách để thực hiện tìm kiếm trong cơ sở dữ liệu như:

- **Tìm kiếm theo từ khóa** - dùng cho tìm kiếm văn bản

- **Tìm kiếm theo vector** - chuyển đổi tài liệu từ văn bản thành biểu diễn vector bằng các mô hình embedding, cho phép **tìm kiếm ngữ nghĩa** dựa trên ý nghĩa từ. Truy xuất thực hiện bằng cách truy vấn các tài liệu có biểu diễn vector gần nhất với câu hỏi người dùng.

- **Kết hợp** - kết hợp cả tìm kiếm theo từ khóa và tìm kiếm vector.

Một thách thức khi truy xuất là khi không có phản hồi tương tự trong cơ sở dữ liệu, hệ thống sẽ trả về thông tin tốt nhất họ có thể lấy. Tuy nhiên, bạn có thể sử dụng các chiến thuật như đặt khoảng cách tối đa phù hợp hoặc dùng tìm kiếm kết hợp. Bài học này chúng ta sẽ dùng tìm kiếm kết hợp, kêt hợp tìm kiếm vector và từ khóa. Chúng ta sẽ lưu dữ liệu vào dataframe với các cột chứa cả mảnh văn bản và embeddings.

### Tương đồng vector

Bộ truy xuất sẽ tìm kiếm trong cơ sở tri thức các embedding gần nhau, gọi là hàng xóm gần nhất, vì chúng là những văn bản tương tự. Trong kịch bản khi người dùng đặt câu hỏi, nó trước tiên được embedding rồi so khớp với các embedding tương tự. Phép đo phổ biến dùng để xác định độ tương đồng giữa các vector là cosine similarity dựa trên góc giữa hai vector.

Chúng ta có thể dùng các lựa chọn khác để đo sự tương đồng như khoảng cách Euclidean (đường thẳng giữa hai điểm cuối vector) và tích vô hướng (đo tổng tích các phần tử tương ứng giữa hai vector).

### Chỉ mục tìm kiếm

Khi thực hiện truy xuất, chúng ta cần xây dựng chỉ mục tìm kiếm cho cơ sở tri thức trước. Chỉ mục sẽ lưu trữ embeddings và có thể nhanh chóng truy xuất các mảnh dữ liệu tương tự nhất ngay cả trong cơ sở dữ liệu lớn. Bạn có thể tạo chỉ mục cục bộ với:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Tạo chỉ mục tìm kiếm
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Để truy vấn chỉ mục, bạn có thể sử dụng phương thức kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Tái xếp hạng

Khi đã truy vấn cơ sở dữ liệu, bạn có thể cần sắp xếp kết quả theo mức độ liên quan nhất. LLM tái xếp hạng sử dụng Học Máy để cải thiện mức độ liên quan của kết quả tìm kiếm thông qua sắp xếp. Dùng Azure AI Search, việc tái xếp hạng được tự động thực hiện bằng bộ sắp xếp ngữ nghĩa. Ví dụ về tái xếp hạng theo hàng xóm gần nhất:

```python
# Tìm các tài liệu giống nhau nhất
distances, indices = nbrs.kneighbors([query_vector])

index = []
# In ra các tài liệu giống nhau nhất
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Tổng hợp lại tất cả

Bước cuối cùng là thêm LLM vào để có thể nhận được phản hồi dựa trên dữ liệu của chúng ta. Ta thực hiện như sau:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Chuyển câu hỏi thành vector truy vấn
    query_vector = create_embeddings(user_input)

    # Tìm các tài liệu tương tự nhất
    distances, indices = nbrs.kneighbors([query_vector])

    # thêm tài liệu vào truy vấn để cung cấp ngữ cảnh
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # kết hợp lịch sử và đầu vào của người dùng
    history.append(user_input)

    # tạo một đối tượng tin nhắn
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # sử dụng API Responses để tạo phản hồi
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Đánh giá ứng dụng của chúng ta

### Các chỉ số đánh giá

- Chất lượng phản hồi đảm bảo nghe tự nhiên, lưu loát và giống con người

- Căn cứ dữ liệu: đánh giá liệu phản hồi có đến từ tài liệu cung cấp không

- Mức độ liên quan: đánh giá phản hồi có phù hợp và liên quan đến câu hỏi không

- Lưu loát - liệu phản hồi có ngữ pháp hợp lý không

## Các trường hợp sử dụng cho RAG (Tạo Sinh Tăng Cường Truy Xuất) và cơ sở dữ liệu vector

Có nhiều trường hợp sử dụng khác nhau mà các cuộc gọi hàm có thể cải thiện ứng dụng của bạn như:

- Hỏi và Trả lời: liên kết dữ liệu công ty bạn với một chatbot để nhân viên có thể đặt câu hỏi.

- Hệ thống đề xuất: bạn có thể tạo hệ thống so khớp các giá trị tương tự nhất ví dụ: phim ảnh, nhà hàng và nhiều hơn nữa.

- Dịch vụ chatbot: bạn có thể lưu lịch sử chat và cá nhân hóa cuộc trò chuyện dựa trên dữ liệu người dùng.

- Tìm kiếm hình ảnh dựa trên vector embedding, hữu ích trong nhận dạng hình ảnh và phát hiện bất thường.

## Tóm tắt

Chúng ta đã bao quát các khía cạnh cơ bản của RAG từ việc thêm dữ liệu vào ứng dụng, truy vấn người dùng và đầu ra. Để đơn giản hóa việc tạo RAG, bạn có thể dùng các framework như Semanti Kernel, Langchain hoặc Autogen.

## Bài tập

Để tiếp tục học về Tạo Sinh Tăng Cường Truy Xuất (RAG), bạn có thể xây dựng:

- Xây dựng giao diện người dùng cho ứng dụng dùng framework bạn chọn

- Sử dụng một framework, LangChain hoặc Semantic Kernel, và tái tạo lại ứng dụng của bạn.

Chúc mừng bạn đã hoàn thành bài học 👏.

## Hành trình học tập không dừng lại ở đây, hãy tiếp tục

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức AI Tạo Sinh của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->