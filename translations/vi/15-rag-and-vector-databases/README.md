<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:36:05+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "vi"
}
-->
# Retrieval Augmented Generation (RAG) và Cơ sở Dữ liệu Vector

[![Retrieval Augmented Generation (RAG) và Cơ sở Dữ liệu Vector](../../../../../translated_images/vi/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Trong bài học ứng dụng tìm kiếm, chúng ta đã học sơ lược cách tích hợp dữ liệu của riêng bạn vào các Mô hình Ngôn ngữ Lớn (LLMs). Trong bài học này, chúng ta sẽ đi sâu hơn vào các khái niệm về cách gắn dữ liệu của bạn vào ứng dụng LLM, cơ chế của quá trình và các phương pháp lưu trữ dữ liệu, bao gồm cả embeddings và văn bản.

> **Video sẽ sớm có**

## Giới thiệu

Trong bài học này, chúng ta sẽ bao gồm các nội dung sau:

- Giới thiệu về RAG, nó là gì và tại sao nó được sử dụng trong AI (trí tuệ nhân tạo).

- Hiểu về cơ sở dữ liệu vector là gì và cách tạo một cơ sở dữ liệu cho ứng dụng của chúng ta.

- Ví dụ thực tiễn về cách tích hợp RAG vào một ứng dụng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Giải thích tầm quan trọng của RAG trong truy xuất và xử lý dữ liệu.

- Thiết lập ứng dụng RAG và gắn dữ liệu của bạn với LLM

- Tích hợp hiệu quả RAG và Cơ sở Dữ liệu Vector trong các Ứng dụng LLM.

## Kịch bản của chúng ta: nâng cao LLM với dữ liệu của riêng mình

Trong bài học này, chúng ta muốn thêm ghi chú của riêng mình vào nền tảng khởi nghiệp giáo dục, điều này sẽ cho phép chatbot lấy thêm thông tin về các chủ đề khác nhau. Sử dụng các ghi chú mà chúng ta có, người học sẽ có thể học tốt hơn và hiểu các chủ đề khác nhau, giúp họ dễ dàng ôn tập cho các kỳ thi. Để tạo kịch bản này, chúng ta sẽ sử dụng:

- `Azure OpenAI:` LLM mà chúng ta sẽ sử dụng để tạo chatbot

- `Bài học AI cho người mới bắt đầu về Mạng Nơ-ron`: đây sẽ là dữ liệu chúng ta gắn LLM lên

- `Azure AI Search` và `Azure Cosmos DB:` cơ sở dữ liệu vector để lưu trữ dữ liệu và tạo chỉ mục tìm kiếm

Người dùng sẽ có thể tạo đề kiểm tra thực hành từ ghi chú của họ, flash card ôn tập và tóm tắt thành các tổng quan ngắn gọn. Để bắt đầu, hãy xem RAG là gì và nó hoạt động thế nào:

## Retrieval Augmented Generation (RAG)

Một chatbot dựa trên LLM xử lý các yêu cầu của người dùng để tạo ra các phản hồi. Nó được thiết kế để tương tác và giao tiếp với người dùng về nhiều chủ đề khác nhau. Tuy nhiên, phản hồi của nó bị giới hạn trong bối cảnh được cung cấp và dữ liệu đào tạo nền tảng của nó. Ví dụ, kiến thức của GPT-4 được cắt đứt vào tháng 9 năm 2021, nghĩa là nó không có kiến thức về các sự kiện xảy ra sau thời điểm đó. Ngoài ra, dữ liệu được sử dụng để đào tạo LLM không bao gồm thông tin bí mật như ghi chú cá nhân hoặc tài liệu hướng dẫn sản phẩm của công ty.

### Cách RAG (Retrieval Augmented Generation) hoạt động

![hình vẽ thể hiện cách RAG hoạt động](../../../../../translated_images/vi/how-rag-works.f5d0ff63942bd3a6.webp)

Giả sử bạn muốn triển khai một chatbot tạo câu đố từ ghi chú của bạn, bạn sẽ cần một kết nối tới cơ sở kiến thức. Đây là lúc RAG hỗ trợ. RAG hoạt động như sau:

- **Cơ sở kiến thức:** Trước khi truy xuất, các tài liệu này cần được đưa vào và tiền xử lý, thường là chia nhỏ các tài liệu lớn thành các phần nhỏ hơn, chuyển đổi chúng thành embeddings văn bản và lưu trữ trong cơ sở dữ liệu.

- **Truy vấn người dùng:** người dùng đặt câu hỏi

- **Truy xuất:** Khi người dùng đặt câu hỏi, mô hình embedding sẽ truy xuất thông tin liên quan từ cơ sở kiến thức để cung cấp thêm bối cảnh sẽ được hòa vào lời nhắc.

- **Tăng cường tạo dữ liệu:** LLM cải thiện phản hồi của mình dựa trên dữ liệu được truy xuất. Điều này cho phép câu trả lời được tạo ra không chỉ dựa trên dữ liệu được huấn luyện trước mà còn dựa trên thông tin liên quan từ bối cảnh thêm vào. Dữ liệu truy xuất được dùng để tăng cường các phản hồi của LLM. Sau đó, LLM trả lời câu hỏi của người dùng.

![hình vẽ thể hiện kiến trúc của RAG](../../../../../translated_images/vi/encoder-decode.f2658c25d0eadee2.webp)

Kiến trúc cho RAG được triển khai bằng cách sử dụng các transformers bao gồm hai phần: một bộ mã hóa và một bộ giải mã. Ví dụ, khi người dùng đặt câu hỏi, văn bản đầu vào được 'mã hóa' thành các vector thể hiện ý nghĩa của từ ngữ, rồi các vector này được 'giải mã' vào chỉ mục tài liệu và tạo ra văn bản mới dựa trên câu hỏi của người dùng. LLM dùng mô hình mã hóa-giải mã để tạo đầu ra.

Hai phương pháp khi triển khai RAG theo bài báo đề xuất: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) là:

- **_RAG-Sequence_** sử dụng các tài liệu truy xuất để dự đoán câu trả lời tốt nhất cho câu hỏi người dùng

- **RAG-Token** sử dụng tài liệu để tạo token tiếp theo, sau đó truy xuất chúng để trả lời câu hỏi của người dùng

### Tại sao bạn nên dùng RAG? 

- **Đầy đủ thông tin:** đảm bảo các phản hồi văn bản luôn cập nhật và chính xác. Do đó, nó nâng cao hiệu suất trên các nhiệm vụ chuyên biệt bằng cách truy cập cơ sở kiến thức nội bộ.

- Giảm thiểu tạo thông tin sai lệch bằng cách sử dụng **dữ liệu có thể kiểm chứng** trong cơ sở kiến thức để cung cấp bối cảnh cho các truy vấn của người dùng.

- **Tiết kiệm chi phí** vì chúng kinh tế hơn so với việc điều chỉnh tinh chỉnh một LLM.

## Tạo cơ sở kiến thức

Ứng dụng của chúng ta dựa trên dữ liệu cá nhân, tức là bài học Mạng Nơ-ron trong chương trình AI cho người mới bắt đầu.

### Cơ sở dữ liệu Vector

Cơ sở dữ liệu vector, khác với cơ sở dữ liệu truyền thống, là một cơ sở dữ liệu chuyên biệt được thiết kế để lưu trữ, quản lý và tìm kiếm các vector nhúng. Nó lưu trữ các biểu diễn số học của tài liệu. Việc chia nhỏ dữ liệu thành các embeddings số giúp hệ thống AI của chúng ta hiểu và xử lý dữ liệu dễ dàng hơn.

Chúng ta lưu trữ embeddings trong cơ sở dữ liệu vector vì LLM có giới hạn về số token chúng chấp nhận làm đầu vào. Vì bạn không thể truyền toàn bộ embeddings vào LLM, chúng ta cần chia chúng thành các phần nhỏ và khi người dùng đặt câu hỏi, embeddings phù hợp nhất với câu hỏi sẽ được trả về cùng với lời nhắc. Việc chia nhỏ cũng giúp giảm chi phí về số token truyền qua LLM.

Một số cơ sở dữ liệu vector phổ biến gồm có Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant và DeepLake. Bạn có thể tạo một mô hình Azure Cosmos DB bằng Azure CLI với lệnh sau:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Từ văn bản tới embeddings

Trước khi lưu trữ dữ liệu, bạn cần chuyển đổi nó thành embeddings vector trước khi lưu vào cơ sở dữ liệu. Nếu bạn làm việc với các tài liệu lớn hoặc văn bản dài, bạn có thể chia nhỏ chúng dựa trên các truy vấn bạn dự đoán sẽ nhận được. Việc chia nhỏ có thể thực hiện ở cấp độ câu, hoặc cấp độ đoạn văn. Vì việc chia nhỏ lấy ý nghĩa dựa trên các từ xung quanh, bạn có thể thêm một số ngữ cảnh khác cho mỗi phần, ví dụ như thêm tiêu đề tài liệu hoặc bao gồm một số văn bản trước hoặc sau phần đó. Bạn có thể chia nhỏ dữ liệu như sau:

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

    # Nếu phần cuối cùng không đạt đến độ dài tối thiểu, vẫn thêm nó vào
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Sau khi chia nhỏ, chúng ta có thể nhúng văn bản bằng các mô hình embedding khác nhau. Một số mô hình bạn có thể sử dụng bao gồm: word2vec, ada-002 của OpenAI, Azure Computer Vision và nhiều hơn nữa. Việc chọn mô hình sử dụng phụ thuộc vào ngôn ngữ bạn dùng, loại nội dung được mã hóa (văn bản/hình ảnh/âm thanh), kích thước đầu vào có thể mã hóa và độ dài đầu ra embedding.

Ví dụ về văn bản được nhúng bằng mô hình `text-embedding-ada-002` của OpenAI như sau:
![một embedding của từ cat](../../../../../translated_images/vi/cat.74cbd7946bc9ca38.webp)

## Truy xuất và Tìm kiếm Vector

Khi người dùng đặt câu hỏi, bộ truy xuất sẽ chuyển đổi câu hỏi thành vector bằng bộ mã hóa truy vấn, sau đó tìm kiếm trong chỉ mục tài liệu những vector liên quan đến đầu vào. Khi hoàn tất, nó chuyển đổi cả vector đầu vào và vector tài liệu sang văn bản và truyền qua LLM.

### Truy xuất

Truy xuất xảy ra khi hệ thống cố gắng tìm nhanh các tài liệu trong chỉ mục thỏa mãn điều kiện tìm kiếm. Mục tiêu của bộ truy xuất là lấy các tài liệu sẽ dùng để cung cấp bối cảnh và gắn LLM lên dữ liệu của bạn.

Có nhiều cách để thực hiện tìm kiếm trong cơ sở dữ liệu như:

- **Tìm kiếm theo từ khóa** - sử dụng cho tìm kiếm văn bản

- **Tìm kiếm vector** - chuyển đổi tài liệu từ văn bản sang biểu diễn vector bằng mô hình embedding, cho phép **tìm kiếm ngữ nghĩa** dựa trên ý nghĩa của từ. Truy xuất sẽ được thực hiện bằng cách truy vấn các tài liệu có vector biểu diễn gần nhất với câu hỏi người dùng.

- **Kết hợp** - sự kết hợp giữa tìm kiếm theo từ khóa và tìm kiếm vector.

Một thử thách khi truy xuất là khi không có phản hồi tương đồng trong cơ sở dữ liệu, hệ thống sẽ trả về thông tin tốt nhất có thể, tuy nhiên bạn có thể dùng các thủ thuật như thiết lập khoảng cách tối đa cho sự phù hợp hoặc dùng tìm kiếm kết hợp cả từ khóa và vector. Trong bài học này, chúng ta sẽ dùng tìm kiếm kết hợp. Chúng ta sẽ lưu dữ liệu vào dataframe với các cột chứa phần nhỏ cùng với embeddings.

### Độ tương đồng Vector

Bộ truy xuất sẽ tìm kiếm trong cơ sở kiến thức các embeddings có độ gần nhau nhất, tức là các láng giềng gần nhất, vì chúng là các văn bản tương tự. Trong kịch bản khi người dùng đặt câu hỏi, câu hỏi được nhúng rồi đối chiếu với các embeddings tương tự. Thước đo phổ biến để xác định độ tương đồng giữa các vector là độ tương đồng cosine, dựa trên góc giữa hai vector.

Chúng ta còn có thể đo độ tương đồng bằng các phương pháp khác như khoảng cách Euclid - là đường thẳng nối hai đầu mút vector và tích vô hướng (dot product) - đo tổng các tích của các phần tử tương ứng của hai vector.

### Chỉ mục tìm kiếm

Khi thực hiện truy xuất, chúng ta cần xây dựng chỉ mục tìm kiếm cho cơ sở kiến thức trước khi thực hiện tìm kiếm. Một chỉ mục sẽ lưu trữ embeddings và có thể truy xuất nhanh các phần nhỏ tương tự nhất ngay cả trong cơ sở dữ liệu lớn. Chúng ta có thể tạo chỉ mục cục bộ bằng:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Tạo chỉ mục tìm kiếm
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Để truy vấn chỉ mục, bạn có thể sử dụng phương thức kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Tái xếp hạng

Khi bạn đã truy vấn cơ sở dữ liệu, bạn có thể cần sắp xếp kết quả theo mức độ liên quan nhất. Một LLM tái xếp hạng sử dụng Học Máy để cải thiện mức độ liên quan của kết quả tìm kiếm bằng cách sắp xếp chúng theo độ phù hợp nhất. Khi dùng Azure AI Search, tái xếp hạng được thực hiện tự động thông qua bộ tái xếp hạng ngữ nghĩa. Ví dụ về cách tái xếp hạng hoạt động bằng cách sử dụng các láng giềng gần nhất:

```python
# Tìm các tài liệu tương tự nhất
distances, indices = nbrs.kneighbors([query_vector])

index = []
# In ra các tài liệu tương tự nhất
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Tổng hợp tất cả lại

Bước cuối cùng là thêm LLM vào để có thể nhận các phản hồi dựa trên dữ liệu của chúng ta. Chúng ta có thể triển khai như sau:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Chuyển câu hỏi thành một vectơ truy vấn
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

    # sử dụng hoàn thành trò chuyện để tạo phản hồi
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Đánh giá ứng dụng của chúng ta

### Các chỉ số đánh giá

- Chất lượng phản hồi đảm bảo nghe tự nhiên, trôi chảy và giống con người

- Tính nền tảng của dữ liệu: đánh giá xem phản hồi có xuất phát từ tài liệu cung cấp không

- Mức độ liên quan: đánh giá phản hồi phù hợp và liên quan đến câu hỏi đã đặt

- Tính lưu loát - phản hồi có hợp lý về mặt ngữ pháp hay không

## Các trường hợp sử dụng RAG (Retrieval Augmented Generation) và cơ sở dữ liệu vector

Có nhiều trường hợp sử dụng khác nhau mà các gọi hàm có thể cải thiện ứng dụng của bạn như:

- Hỏi đáp: gắn dữ liệu công ty bạn vào trò chuyện có thể dùng bởi nhân viên để đặt câu hỏi.

- Hệ thống đề xuất: nơi bạn có thể tạo hệ thống ghép các giá trị tương tự nhất ví dụ như phim, nhà hàng và nhiều hơn nữa.

- Dịch vụ chatbot: bạn có thể lưu lịch sử trò chuyện và cá nhân hóa cuộc hội thoại dựa trên dữ liệu người dùng.

- Tìm kiếm hình ảnh dựa trên embeddings vector, hữu ích khi nhận dạng hình ảnh và phát hiện bất thường.

## Tóm tắt

Chúng ta đã bao quát các lĩnh vực cơ bản của RAG từ việc thêm dữ liệu vào ứng dụng, câu hỏi của người dùng và đầu ra. Để đơn giản hóa việc tạo RAG, bạn có thể sử dụng các framework như Semanti Kernel, Langchain hoặc Autogen.

## Bài tập

Để tiếp tục học về Retrieval Augmented Generation (RAG), bạn có thể xây dựng:

- Xây dựng giao diện front-end cho ứng dụng bằng framework bạn chọn

- Sử dụng một framework, LangChain hoặc Semantic Kernel, và tái tạo lại ứng dụng của bạn.

Chúc mừng bạn đã hoàn thành bài học 👏.

## Học không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy khám phá bộ sưu tập [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức AI sinh tạo!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc thông tin không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa được coi là nguồn đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hay diễn giải sai lệch nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->