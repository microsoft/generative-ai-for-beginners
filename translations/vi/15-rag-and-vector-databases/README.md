# Tạo Sinh Được Tăng Cường Truy Xuất (RAG) và Cơ Sở Dữ Liệu Vector

[![Tạo Sinh Được Tăng Cường Truy Xuất (RAG) và Cơ Sở Dữ Liệu Vector](../../../translated_images/vi/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Trong bài học ứng dụng tìm kiếm, chúng ta đã học sơ lược cách tích hợp dữ liệu riêng của bạn vào Mô Hình Ngôn Ngữ Lớn (LLMs). Trong bài học này, chúng ta sẽ đi sâu hơn vào các khái niệm về việc tiếp đất dữ liệu của bạn trong ứng dụng LLM, cơ chế của quá trình và các phương pháp lưu trữ dữ liệu, bao gồm cả embeddings và văn bản.

> **Video Sẽ Sớm Có**

## Giới Thiệu

Trong bài học này, chúng ta sẽ đề cập đến những nội dung sau:

- Giới thiệu về RAG, nó là gì và tại sao nó được sử dụng trong trí tuệ nhân tạo (AI).

- Hiểu về cơ sở dữ liệu vector là gì và cách tạo một cơ sở dữ liệu cho ứng dụng của chúng ta.

- Một ví dụ thực tế về cách tích hợp RAG vào ứng dụng.

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ có khả năng:

- Giải thích tầm quan trọng của RAG trong truy xuất và xử lý dữ liệu.

- Thiết lập một ứng dụng RAG và tiếp đất một LLM với dữ liệu của bạn

- Tích hợp hiệu quả RAG và cơ sở dữ liệu vector trong các ứng dụng LLM.

## Tình Huống Của Chúng Ta: nâng cao các LLM với dữ liệu riêng

Trong bài học này, chúng ta muốn thêm các ghi chú riêng của mình vào startup giáo dục, cho phép chatbot có thêm thông tin về các chủ đề khác nhau. Sử dụng các ghi chú mà chúng ta có, người học sẽ có thể học tốt hơn và hiểu sâu các chủ đề, giúp việc ôn tập cho kỳ thi dễ dàng hơn. Để tạo tình huống này, chúng ta sẽ sử dụng:

- `Azure OpenAI:` LLM mà chúng ta sẽ dùng để tạo chatbot

- `AI for beginners' lesson on Neural Networks`: đây sẽ là dữ liệu mà chúng ta tiếp đất LLM trên đó

- `Azure AI Search` và `Azure Cosmos DB:` cơ sở dữ liệu vector để lưu trữ dữ liệu và tạo chỉ mục tìm kiếm

Người dùng sẽ có thể tạo các bài kiểm tra luyện tập và thẻ ghi nhớ ôn tập từ các ghi chú của họ và tóm tắt những ghi chú đó thành các tổng quan ngắn gọn. Để bắt đầu, hãy cùng xem RAG là gì và nó hoạt động như thế nào:

## Tạo Sinh Được Tăng Cường Truy Xuất (RAG)

Một chatbot chạy trên LLM xử lý các lời nhắc từ người dùng để tạo ra các phản hồi. Nó được thiết kế để tương tác và thu hút người dùng trên nhiều chủ đề khác nhau. Tuy nhiên, phản hồi của nó bị giới hạn trong bối cảnh được cung cấp và dữ liệu đào tạo nền tảng của nó. Ví dụ, GPT-4 có giới hạn kiến thức đến tháng 9 năm 2021, có nghĩa là nó không biết các sự kiện xảy ra sau thời điểm này. Thêm vào đó, dữ liệu dùng để đào tạo LLM loại trừ thông tin bí mật như ghi chú cá nhân hoặc hướng dẫn sản phẩm của công ty.

### Cách thức hoạt động của RAG (Tạo Sinh Được Tăng Cường Truy Xuất)

![drawing showing how RAGs work](../../../translated_images/vi/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Giả sử bạn muốn triển khai một chatbot tạo câu hỏi kiểm tra từ các ghi chú của bạn, bạn sẽ cần một kết nối đến cơ sở tri thức. Đây là lúc RAG giúp đỡ. RAG hoạt động như sau:

- **Cơ sở tri thức:** Trước khi truy xuất, các tài liệu này cần được tiếp nhận và xử lý trước, thường là chia nhỏ các tài liệu lớn thành các phần nhỏ hơn, chuyển đổi chúng thành embeddings văn bản và lưu trữ trong cơ sở dữ liệu.

- **Truy vấn người dùng:** người dùng đặt câu hỏi

- **Truy xuất:** Khi người dùng hỏi, mô hình embedding truy xuất thông tin liên quan từ cơ sở tri thức để cung cấp bối cảnh bổ sung sẽ được đưa vào lời nhắc.

- **Tạo Sinh Được Tăng Cường:** LLM nâng cao phản hồi dựa trên dữ liệu truy xuất. Nó cho phép phản hồi được tạo ra không chỉ dựa trên dữ liệu tiền huấn luyện mà còn dựa trên thông tin liên quan từ bối cảnh được thêm vào. Dữ liệu truy xuất được dùng để tăng cường các câu trả lời của LLM. Sau đó LLM trả lời câu hỏi của người dùng.

![Diagram showing RAG architecture](../../../translated_images/vi/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG kết hợp một bộ truy xuất với một bộ tạo: truy vấn được chuyển thành vectơ, so khớp với chỉ mục tài liệu để tìm các phần văn bản liên quan, và các phần này được cung cấp như bối cảnh cho LLM, nó sẽ tạo phản hồi. Bộ truy xuất và bộ tạo có thể dùng các mô hình khác nhau; RAG không yêu cầu transformer kiểu encoder-decoder.

Có hai phương pháp khi triển khai RAG theo bài báo đề xuất: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) là:

- **_RAG-Sequence_** sử dụng các tài liệu truy xuất để dự đoán câu trả lời tốt nhất cho truy vấn người dùng

- **RAG-Token** sử dụng tài liệu để tạo token kế tiếp, sau đó truy xuất chúng để trả lời truy vấn của người dùng

### Tại sao bạn nên dùng RAG?

- **Đầy đủ thông tin:** đảm bảo phản hồi văn bản được cập nhật và hiện tại. Do đó, nó cải thiện hiệu suất trên các tác vụ đặc thù bằng cách truy cập cơ sở tri thức nội bộ.

- Giảm việc bịa đặt bằng cách sử dụng **dữ liệu có thể kiểm chứng** trong cơ sở tri thức để cung cấp bối cảnh cho truy vấn người dùng.

- Nó **tiết kiệm chi phí** vì rẻ hơn nhiều so với việc tinh chỉnh LLM

## Tạo cơ sở tri thức

Ứng dụng của chúng ta dựa trên dữ liệu cá nhân của mình, tức là bài học Mạng Nơ-ron từ giáo trình AI cho Người Mới Bắt Đầu.

### Cơ sở dữ liệu Vector

Cơ sở dữ liệu vector, khác với cơ sở dữ liệu truyền thống, là cơ sở dữ liệu chuyên biệt được thiết kế để lưu trữ, quản lý và tìm kiếm các vectơ nhúng. Nó lưu trữ các biểu diễn số của tài liệu. Việc phá dữ liệu thành embeddings số giúp hệ thống AI của chúng ta dễ dàng hiểu và xử lý dữ liệu hơn.

Vì LLM có giới hạn số lượng token đầu vào, chúng ta chia nhỏ tài liệu trước khi nhúng. Khi người dùng hỏi, các embeddings tương tự truy vấn nhất xác định các phần văn bản liên quan được trả lại kèm theo lời nhắc. Việc chia nhỏ cũng giảm số lượng token gửi vào LLM và từ đó giảm chi phí.

Một số cơ sở dữ liệu vector phổ biến bao gồm Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant và DeepLake. Bạn có thể tạo mô hình Azure Cosmos DB bằng Azure CLI với lệnh sau:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Từ văn bản đến embeddings

Trước khi lưu dữ liệu, chúng ta cần chuyển đổi nó thành vector embeddings trước khi lưu vào cơ sở dữ liệu. Nếu bạn làm việc với các tài liệu lớn hoặc văn bản dài, bạn có thể chia nhỏ dựa trên các truy vấn bạn dự đoán. Việc chia nhỏ có thể làm ở cấp câu hoặc đoạn. Vì việc chia nhỏ dựa trên nghĩa của các từ xung quanh, bạn có thể thêm bối cảnh khác vào một phần, ví dụ như thêm tiêu đề tài liệu hoặc bao gồm một số văn bản trước hoặc sau phần đó. Bạn có thể chia nhỏ dữ liệu như sau:

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

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Khi đã chia nhỏ, chúng ta có thể nhúng văn bản bằng các mô hình embedding khác nhau. Một số mô hình bạn có thể dùng bao gồm: word2vec, ada-002 của OpenAI, Azure Computer Vision và nhiều hơn nữa. Việc chọn mô hình phụ thuộc vào ngôn ngữ bạn dùng, loại nội dung mã hóa (văn bản/hình ảnh/âm thanh), kích thước đầu vào và độ dài đầu ra embedding.

Một ví dụ về văn bản được nhúng sử dụng mô hình `text-embedding-ada-002` của OpenAI là:
![an embedding of the word cat](../../../translated_images/vi/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Truy Xuất và Tìm Kiếm Vector

Khi người dùng hỏi, bộ truy xuất chuyển câu hỏi thành vectơ bằng bộ mã hóa truy vấn, sau đó tìm kiếm chỉ mục tài liệu cho các vectơ liên quan trong tài liệu có liên quan đến đầu vào. Sau khi xong, nó chuyển cả vectơ đầu vào và các vectơ tài liệu thành văn bản và đưa qua LLM.

### Truy Xuất

Truy xuất xảy ra khi hệ thống cố gắng nhanh chóng tìm tài liệu từ chỉ mục thoả tiêu chí tìm kiếm. Mục đích của bộ truy xuất là lấy tài liệu cung cấp bối cảnh và tiếp đất LLM trên dữ liệu của bạn.

Có nhiều cách để tìm kiếm trong cơ sở dữ liệu của chúng ta như:

- **Tìm kiếm bằng từ khóa** - dùng cho tìm kiếm văn bản

- **Tìm kiếm vector** - chuyển đổi tài liệu từ văn bản sang biểu diễn vectơ bằng các mô hình embedding, cho phép **tìm kiếm ngữ nghĩa** dựa trên nghĩa của từ. Việc truy xuất sẽ tìm các tài liệu có vector gần nhất với câu hỏi người dùng.

- **Kết hợp** - sự kết hợp cả tìm kiếm từ khóa và tìm kiếm vector.

Thách thức với truy xuất khi không có phản hồi tương tự trong cơ sở dữ liệu, hệ thống sẽ trả lại thông tin tốt nhất có thể, tuy nhiên bạn có thể dùng các chiến thuật như thiết lập khoảng cách tối đa cho tính liên quan hoặc dùng tìm kiếm kết hợp từ khóa và vector. Trong bài học này, chúng ta sẽ dùng tìm kiếm kết hợp, sự kết hợp của cả tìm kiếm vector và từ khóa. Chúng ta sẽ lưu dữ liệu vào dataframe với các cột chứa các phần nhỏ và embeddings.

### Tương đồng Vector

Bộ truy xuất sẽ tìm trong cơ sở tri thức các embeddings gần nhau nhất—các láng giềng gần nhất—vì chúng đại diện cho các văn bản tương tự nhau. Trong trường hợp này, khi người dùng gửi truy vấn, nó được nhúng và so khớp với các embeddings tương tự. Thước đo phổ biến nhất để so sánh tương đồng vector là cosine similarity, dựa trên góc giữa hai vectơ.

Các chỉ số khác để đo tương đồng gồm khoảng cách Euclidean, là đường thẳng giữa các điểm cuối vectơ, và tích vô hướng, đo tổng các tích các thành phần tương ứng trong hai vectơ.

### Chỉ mục tìm kiếm

Khi thực hiện truy xuất, chúng ta cần xây dựng một chỉ mục tìm kiếm cho cơ sở tri thức trước khi tìm kiếm. Chỉ mục sẽ lưu embeddings và có thể nhanh chóng truy xuất các phần tương tự nhất ngay cả trong cơ sở dữ liệu lớn. Chúng ta có thể tạo chỉ mục cục bộ bằng:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Sắp xếp lại kết quả

Khi bạn đã truy vấn cơ sở dữ liệu, bạn có thể cần sắp xếp kết quả theo thứ tự liên quan nhất. LLM tái xếp hạng dùng Machine Learning để nâng cao tính liên quan của kết quả tìm kiếm bằng cách sắp xếp chúng từ liên quan nhất. Sử dụng Azure AI Search, tái xếp hạng được thực hiện tự động bằng bộ tái xếp hạng ngữ nghĩa. Ví dụ về cách tái xếp hạng sử dụng các láng giềng gần nhất:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Tổng hợp lại

Bước cuối cùng là thêm LLM vào để có thể nhận phản hồi dựa trên dữ liệu của chúng ta. Chúng ta có thể triển khai như sau:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use the Responses API to generate a response
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Đánh giá ứng dụng của chúng ta

### Các chỉ số đánh giá

- Chất lượng câu trả lời đảm bảo nghe tự nhiên, trôi chảy và giống con người

- Tính gắn kết của dữ liệu: đánh giá liệu phản hồi có đến từ các tài liệu được cung cấp

- Độ phù hợp: đánh giá phản hồi khớp và liên quan đến câu hỏi được đặt ra

- Sự trôi chảy - liệu phản hồi có hợp lý về mặt ngữ pháp

## Các trường hợp sử dụng cho việc dùng RAG (Tạo Sinh Được Tăng Cường Truy Xuất) và cơ sở dữ liệu vector

Có nhiều trường hợp sử dụng khác nhau nơi RAG có thể cải thiện ứng dụng của bạn, ví dụ:

- Hỏi và Đáp: tiếp đất dữ liệu công ty bạn vào một chatbot để nhân viên hỏi đáp.

- Hệ thống đề xuất: nơi bạn có thể tạo hệ thống khớp các giá trị tương tự nhất ví dụ phim ảnh, nhà hàng và nhiều hơn nữa.

- Dịch vụ chatbot: bạn có thể lưu trữ lịch sử trò chuyện và cá nhân hóa cuộc trò chuyện dựa trên dữ liệu người dùng.

- Tìm kiếm hình ảnh dựa trên embeddings vector, hữu ích khi nhận dạng hình ảnh và phát hiện dị thường.

## Tóm tắt

Chúng ta đã bao quát các lĩnh vực cơ bản của RAG từ việc thêm dữ liệu vào ứng dụng, truy vấn người dùng và đầu ra. Để đơn giản hóa việc tạo RAG, bạn có thể dùng các framework như Semantic Kernel, LangChain hoặc AutoGen.

## Bài tập

Để tiếp tục học về Tạo Sinh Được Tăng Cường Truy Xuất (RAG) bạn có thể xây dựng:

- Xây dựng giao diện front-end cho ứng dụng sử dụng framework bạn chọn

- Sử dụng một framework, hoặc LangChain hoặc Semantic Kernel, và tái tạo ứng dụng của bạn.

Chúc mừng bạn đã hoàn thành bài học 👏.

## Việc học không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về Generative AI của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->