<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:39:28+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "vi"
}
-->
# Tạo Thế Hệ Tăng Cường Truy Xuất (RAG) và Cơ Sở Dữ Liệu Vector

[![Tạo Thế Hệ Tăng Cường Truy Xuất (RAG) và Cơ Sở Dữ Liệu Vector](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.vi.png)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

Trong bài học về ứng dụng tìm kiếm, chúng ta đã tìm hiểu sơ qua cách tích hợp dữ liệu của bạn vào các Mô Hình Ngôn Ngữ Lớn (LLMs). Trong bài học này, chúng ta sẽ đi sâu hơn vào các khái niệm về việc gắn kết dữ liệu của bạn trong ứng dụng LLM, cơ chế của quá trình và các phương pháp lưu trữ dữ liệu, bao gồm cả embeddings và văn bản.

> **Video sẽ sớm ra mắt**

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến các nội dung sau:

- Giới thiệu về RAG, nó là gì và tại sao nó được sử dụng trong AI (trí tuệ nhân tạo).

- Hiểu về cơ sở dữ liệu vector và tạo một cái cho ứng dụng của chúng ta.

- Một ví dụ thực tế về cách tích hợp RAG vào một ứng dụng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Giải thích ý nghĩa của RAG trong việc truy xuất và xử lý dữ liệu.

- Thiết lập ứng dụng RAG và gắn kết dữ liệu của bạn với một LLM

- Tích hợp hiệu quả RAG và Cơ Sở Dữ Liệu Vector trong các Ứng Dụng LLM.

## Tình huống của chúng ta: nâng cao LLMs với dữ liệu của riêng chúng ta

Trong bài học này, chúng ta muốn thêm ghi chú của mình vào công ty khởi nghiệp giáo dục, điều này cho phép chatbot lấy thêm thông tin về các chủ đề khác nhau. Sử dụng các ghi chú mà chúng ta có, người học sẽ có thể học tốt hơn và hiểu các chủ đề khác nhau, giúp dễ dàng ôn tập cho các kỳ thi của họ. Để tạo tình huống của chúng ta, chúng ta sẽ sử dụng:

- `Azure OpenAI:` LLM mà chúng ta sẽ sử dụng để tạo chatbot của mình

- `AI for beginners' lesson on Neural Networks`: đây sẽ là dữ liệu mà chúng ta gắn kết LLM của mình vào

- `Azure AI Search` và `Azure Cosmos DB:` cơ sở dữ liệu vector để lưu trữ dữ liệu của chúng ta và tạo một chỉ mục tìm kiếm

Người dùng sẽ có thể tạo các bài kiểm tra thực hành từ ghi chú của họ, thẻ flash ôn tập và tóm tắt nó thành các tổng quan ngắn gọn. Để bắt đầu, hãy cùng tìm hiểu RAG là gì và cách hoạt động:

## Tạo Thế Hệ Tăng Cường Truy Xuất (RAG)

Một chatbot được hỗ trợ bởi LLM xử lý các yêu cầu của người dùng để tạo ra phản hồi. Nó được thiết kế để tương tác và giao tiếp với người dùng về một loạt các chủ đề. Tuy nhiên, các phản hồi của nó bị giới hạn trong ngữ cảnh được cung cấp và dữ liệu đào tạo nền tảng của nó. Ví dụ, GPT-4 có giới hạn kiến thức đến tháng 9 năm 2021, có nghĩa là nó thiếu kiến thức về các sự kiện đã xảy ra sau thời điểm này. Ngoài ra, dữ liệu được sử dụng để đào tạo LLMs loại trừ thông tin bảo mật như ghi chú cá nhân hoặc hướng dẫn sản phẩm của một công ty.

### Cách RAGs (Tạo Thế Hệ Tăng Cường Truy Xuất) hoạt động

![hình vẽ minh họa cách RAGs hoạt động](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.vi.png)

Giả sử bạn muốn triển khai một chatbot tạo các bài kiểm tra từ ghi chú của bạn, bạn sẽ cần một kết nối đến cơ sở kiến thức. Đây là lúc RAG phát huy tác dụng. RAGs hoạt động như sau:

- **Cơ sở kiến thức:** Trước khi truy xuất, các tài liệu này cần được nhập và tiền xử lý, thường là chia nhỏ các tài liệu lớn thành các phần nhỏ hơn, chuyển đổi chúng thành text embedding và lưu trữ chúng trong cơ sở dữ liệu.

- **Truy vấn của người dùng:** người dùng đặt câu hỏi

- **Truy xuất:** Khi người dùng đặt câu hỏi, mô hình embedding truy xuất thông tin liên quan từ cơ sở kiến thức của chúng ta để cung cấp thêm ngữ cảnh sẽ được tích hợp vào yêu cầu.

- **Tạo Thế Hệ Tăng Cường:** LLM cải thiện phản hồi của nó dựa trên dữ liệu đã truy xuất. Nó cho phép phản hồi được tạo ra không chỉ dựa trên dữ liệu đã được đào tạo trước mà còn thông tin liên quan từ ngữ cảnh được thêm vào. Dữ liệu truy xuất được sử dụng để tăng cường các phản hồi của LLM. Sau đó, LLM trả lời câu hỏi của người dùng.

![hình vẽ minh họa kiến trúc của RAGs](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.vi.png)

Kiến trúc cho RAGs được triển khai sử dụng transformers gồm hai phần: một encoder và một decoder. Ví dụ, khi một người dùng đặt câu hỏi, văn bản đầu vào 'được mã hóa' thành các vector nắm bắt ý nghĩa của các từ và các vector được 'giải mã' vào chỉ mục tài liệu của chúng ta và tạo ra văn bản mới dựa trên truy vấn của người dùng. LLM sử dụng cả mô hình encoder-decoder để tạo ra đầu ra.

Hai phương pháp khi triển khai RAG theo bài báo đề xuất: [Tạo Thế Hệ Tăng Cường Truy Xuất cho các Nhiệm Vụ NLP (phần mềm xử lý ngôn ngữ tự nhiên) cần kiến thức](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) là:

- **_RAG-Sequence_** sử dụng các tài liệu đã truy xuất để dự đoán câu trả lời tốt nhất có thể cho một truy vấn của người dùng

- **RAG-Token** sử dụng tài liệu để tạo token tiếp theo, sau đó truy xuất chúng để trả lời truy vấn của người dùng

### Tại sao bạn nên sử dụng RAGs?

- **Sự phong phú thông tin:** đảm bảo các phản hồi văn bản là cập nhật và hiện tại. Do đó, nó nâng cao hiệu suất trong các nhiệm vụ cụ thể của lĩnh vực bằng cách truy cập cơ sở kiến thức nội bộ.

- Giảm sự bịa đặt bằng cách sử dụng **dữ liệu có thể xác minh** trong cơ sở kiến thức để cung cấp ngữ cảnh cho các truy vấn của người dùng.

- Nó **hiệu quả về chi phí** vì chúng tiết kiệm hơn so với việc tinh chỉnh một LLM

## Tạo cơ sở kiến thức

Ứng dụng của chúng ta dựa trên dữ liệu cá nhân của chúng ta, tức là bài học về Mạng Nơ-ron trong chương trình AI Dành Cho Người Mới Bắt Đầu.

### Cơ Sở Dữ Liệu Vector

Một cơ sở dữ liệu vector, không giống như các cơ sở dữ liệu truyền thống, là một cơ sở dữ liệu chuyên dụng được thiết kế để lưu trữ, quản lý và tìm kiếm các vector nhúng. Nó lưu trữ các biểu diễn số của tài liệu. Phân tích dữ liệu thành các embedding số làm cho hệ thống AI của chúng ta dễ hiểu và xử lý dữ liệu hơn.

Chúng ta lưu trữ các embedding của mình trong các cơ sở dữ liệu vector vì LLMs có giới hạn về số lượng token mà chúng chấp nhận làm đầu vào. Vì bạn không thể chuyển toàn bộ embedding vào một LLM, chúng ta sẽ cần chia chúng thành các phần và khi người dùng đặt câu hỏi, các embedding giống nhất với câu hỏi sẽ được trả lại cùng với yêu cầu. Việc chia nhỏ cũng giảm chi phí trên số lượng token được chuyển qua một LLM.

Một số cơ sở dữ liệu vector phổ biến bao gồm Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant và DeepLake. Bạn có thể tạo một mô hình Azure Cosmos DB bằng cách sử dụng Azure CLI với lệnh sau:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Từ văn bản đến embedding

Trước khi lưu trữ dữ liệu của chúng ta, chúng ta sẽ cần chuyển đổi nó thành các embedding vector trước khi lưu trữ trong cơ sở dữ liệu. Nếu bạn đang làm việc với các tài liệu lớn hoặc văn bản dài, bạn có thể chia nhỏ chúng dựa trên các truy vấn bạn dự kiến. Việc chia nhỏ có thể được thực hiện ở cấp độ câu, hoặc ở cấp độ đoạn văn. Vì việc chia nhỏ lấy ý nghĩa từ các từ xung quanh, bạn có thể thêm một số ngữ cảnh khác vào một phần, ví dụ, bằng cách thêm tiêu đề tài liệu hoặc bao gồm một số văn bản trước hoặc sau phần đó. Bạn có thể chia nhỏ dữ liệu như sau:

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

Khi đã chia nhỏ, chúng ta có thể nhúng văn bản của mình bằng các mô hình nhúng khác nhau. Một số mô hình bạn có thể sử dụng bao gồm: word2vec, ada-002 của OpenAI, Azure Computer Vision và nhiều hơn nữa. Việc chọn mô hình để sử dụng sẽ phụ thuộc vào ngôn ngữ bạn đang sử dụng, loại nội dung được mã hóa (văn bản/hình ảnh/âm thanh), kích thước đầu vào mà nó có thể mã hóa và độ dài của đầu ra nhúng.

Một ví dụ về văn bản nhúng sử dụng mô hình `text-embedding-ada-002` của OpenAI là:
![một embedding của từ cat](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.vi.png)

## Truy xuất và Tìm kiếm Vector

Khi người dùng đặt câu hỏi, công cụ truy xuất sẽ chuyển đổi nó thành một vector sử dụng mã hóa truy vấn, sau đó tìm kiếm qua chỉ mục tìm kiếm tài liệu của chúng ta để tìm các vector liên quan trong tài liệu có liên quan đến đầu vào. Khi hoàn tất, nó chuyển đổi cả vector đầu vào và vector tài liệu thành văn bản và chuyển qua LLM.

### Truy xuất

Truy xuất xảy ra khi hệ thống cố gắng nhanh chóng tìm các tài liệu từ chỉ mục đáp ứng tiêu chí tìm kiếm. Mục tiêu của công cụ truy xuất là lấy các tài liệu sẽ được sử dụng để cung cấp ngữ cảnh và gắn kết LLM vào dữ liệu của bạn.

Có nhiều cách để thực hiện tìm kiếm trong cơ sở dữ liệu của chúng ta như:

- **Tìm kiếm từ khóa** - được sử dụng cho các tìm kiếm văn bản

- **Tìm kiếm ngữ nghĩa** - sử dụng ý nghĩa ngữ nghĩa của từ

- **Tìm kiếm vector** - chuyển đổi tài liệu từ văn bản thành biểu diễn vector sử dụng các mô hình nhúng. Truy xuất sẽ được thực hiện bằng cách truy vấn các tài liệu có biểu diễn vector gần nhất với câu hỏi của người dùng.

- **Kết hợp** - kết hợp cả tìm kiếm từ khóa và tìm kiếm vector.

Một thách thức với truy xuất xảy ra khi không có phản hồi tương tự với truy vấn trong cơ sở dữ liệu, hệ thống sẽ trả lại thông tin tốt nhất mà nó có thể tìm được, tuy nhiên, bạn có thể sử dụng các chiến thuật như thiết lập khoảng cách tối đa cho sự liên quan hoặc sử dụng tìm kiếm kết hợp kết hợp cả từ khóa và tìm kiếm vector. Trong bài học này, chúng ta sẽ sử dụng tìm kiếm kết hợp, kết hợp cả tìm kiếm vector và từ khóa. Chúng ta sẽ lưu trữ dữ liệu của mình vào một dataframe với các cột chứa các phần cũng như các embedding.

### Tương đồng Vector

Công cụ truy xuất sẽ tìm kiếm qua cơ sở dữ liệu kiến thức để tìm các embedding gần nhau nhất, gần nhất là hàng xóm gần nhất, vì chúng là các văn bản tương tự. Trong trường hợp người dùng đặt một truy vấn, nó được nhúng trước tiên sau đó được so khớp với các embedding tương tự. Thước đo phổ biến được sử dụng để tìm xem các vector khác nhau tương tự nhau như thế nào là độ tương đồng cosine dựa trên góc giữa hai vector.

Chúng ta có thể đo lường sự tương đồng sử dụng các lựa chọn thay thế khác như khoảng cách Euclid, là đường thẳng giữa các điểm cuối vector và tích vô hướng, đo lường tổng của các sản phẩm của các phần tử tương ứng của hai vector.

### Chỉ mục tìm kiếm

Khi thực hiện truy xuất, chúng ta sẽ cần xây dựng một chỉ mục tìm kiếm cho cơ sở kiến thức của chúng ta trước khi thực hiện tìm kiếm. Một chỉ mục sẽ lưu trữ các embedding của chúng ta và có thể nhanh chóng truy xuất các phần tương tự nhất ngay cả trong một cơ sở dữ liệu lớn. Chúng ta có thể tạo chỉ mục của mình cục bộ bằng cách sử dụng:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Xếp hạng lại

Khi bạn đã truy vấn cơ sở dữ liệu, bạn có thể cần sắp xếp kết quả từ cái có liên quan nhất. Một LLM xếp hạng lại sử dụng Máy Học để cải thiện sự liên quan của kết quả tìm kiếm bằng cách sắp xếp chúng từ cái có liên quan nhất. Sử dụng Azure AI Search, việc xếp hạng lại được thực hiện tự động cho bạn sử dụng một bộ xếp hạng ngữ nghĩa. Một ví dụ về cách xếp hạng lại hoạt động sử dụng hàng xóm gần nhất:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Kết hợp tất cả lại với nhau

Bước cuối cùng là thêm LLM của chúng ta vào để có thể nhận được các phản hồi được gắn kết trên dữ liệu của chúng ta. Chúng ta có thể triển khai nó như sau:

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
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
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

### Chỉ số đánh giá

- Chất lượng của các phản hồi cung cấp đảm bảo nó nghe tự nhiên, trôi chảy và giống con người

- Sự gắn kết của dữ liệu: đánh giá xem phản hồi có đến từ các tài liệu được cung cấp không

- Sự liên quan: đánh giá xem phản hồi có phù hợp và liên quan đến câu hỏi được đặt ra không

- Độ trôi chảy - liệu phản hồi có hợp lý về ngữ pháp không

## Các trường hợp sử dụng RAG (Tạo Thế Hệ Tăng Cường Truy Xuất) và cơ sở dữ liệu vector

Có nhiều trường hợp sử dụng khác nhau mà các cuộc gọi chức năng có thể cải thiện ứng dụng của bạn như:

- Hỏi đáp: gắn kết dữ liệu công ty của bạn vào một cuộc trò chuyện mà nhân viên có thể sử dụng để đặt câu hỏi.

- Hệ thống gợi ý: nơi bạn có thể tạo một hệ thống khớp với các giá trị tương tự nhất, ví dụ: phim, nhà hàng và nhiều hơn nữa.

- Dịch vụ chatbot: bạn có thể lưu trữ lịch sử trò chuyện và cá nhân hóa cuộc trò chuyện dựa trên dữ liệu người dùng.

- Tìm kiếm hình ảnh dựa trên embedding vector, hữu ích khi thực hiện nhận dạng hình ảnh và phát hiện bất thường.

## Tóm tắt

Chúng ta đã đề cập đến các lĩnh vực cơ bản của RAG từ việc thêm dữ liệu của chúng ta vào ứng dụng, truy vấn của người dùng và đầu ra. Để đơn giản hóa việc tạo RAG, bạn có thể sử dụng các khung như Semanti Kernel, Langchain hoặc Autogen.

## Bài tập

Để tiếp tục học về Tạo Thế Hệ Tăng Cường Truy Xuất (RAG) bạn có thể xây dựng:

- Xây dựng một giao diện người dùng cho ứng dụng sử dụng khung mà bạn chọn

- Sử dụng một khung, LangChain hoặc Semantic Kernel, và tái tạo ứng dụng của bạn.

Chúc mừng bạn đã hoàn thành bài học 👏.

## Học tập không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học Tập AI Sinh Tạo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức AI Sinh Tạo của bạn!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thống. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.