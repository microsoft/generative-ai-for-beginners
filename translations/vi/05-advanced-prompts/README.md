<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2651fb16bcfbc62b8e518751ed90fdb",
  "translation_date": "2025-10-17T20:30:19+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "vi"
}
-->
# Tạo các lời nhắc nâng cao

[![Tạo các lời nhắc nâng cao](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.vi.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Hãy cùng ôn lại một số kiến thức từ chương trước:

> Kỹ thuật _lời nhắc_ là quá trình mà chúng ta **hướng dẫn mô hình tạo ra các phản hồi phù hợp hơn** bằng cách cung cấp các hướng dẫn hoặc ngữ cảnh hữu ích hơn.

Có hai bước để viết lời nhắc: xây dựng lời nhắc bằng cách cung cấp ngữ cảnh phù hợp và _tối ưu hóa_, tức là cách cải thiện lời nhắc dần dần.

Đến thời điểm này, chúng ta đã có một số hiểu biết cơ bản về cách viết lời nhắc, nhưng cần đi sâu hơn. Trong chương này, bạn sẽ chuyển từ việc thử nghiệm các lời nhắc khác nhau sang việc hiểu tại sao một lời nhắc lại tốt hơn lời nhắc khác. Bạn sẽ học cách xây dựng lời nhắc theo một số kỹ thuật cơ bản có thể áp dụng cho bất kỳ LLM nào.

## Giới thiệu

Trong chương này, chúng ta sẽ đề cập đến các chủ đề sau:

- Mở rộng kiến thức về kỹ thuật lời nhắc bằng cách áp dụng các kỹ thuật khác nhau vào lời nhắc của bạn.
- Cấu hình lời nhắc để thay đổi đầu ra.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Áp dụng các kỹ thuật lời nhắc để cải thiện kết quả của lời nhắc.
- Thực hiện lời nhắc có thể thay đổi hoặc mang tính xác định.

## Kỹ thuật lời nhắc

Kỹ thuật lời nhắc là quá trình tạo ra các lời nhắc để tạo ra kết quả mong muốn. Kỹ thuật lời nhắc không chỉ đơn thuần là viết một đoạn văn bản. Nó không phải là một ngành kỹ thuật, mà là một tập hợp các kỹ thuật bạn có thể áp dụng để đạt được kết quả mong muốn.

### Một ví dụ về lời nhắc

Hãy xem một lời nhắc cơ bản như sau:

> Tạo 10 câu hỏi về địa lý.

Trong lời nhắc này, bạn thực sự đang áp dụng một tập hợp các kỹ thuật lời nhắc khác nhau.

Hãy phân tích lời nhắc này.

- **Ngữ cảnh**, bạn chỉ định rằng nó nên liên quan đến "địa lý".
- **Giới hạn đầu ra**, bạn muốn không quá 10 câu hỏi.

### Hạn chế của lời nhắc đơn giản

Bạn có thể hoặc không thể đạt được kết quả mong muốn. Bạn sẽ nhận được các câu hỏi được tạo ra, nhưng địa lý là một chủ đề rộng lớn và bạn có thể không nhận được những gì bạn muốn vì các lý do sau:

- **Chủ đề rộng**, bạn không biết liệu nó sẽ nói về các quốc gia, thủ đô, sông ngòi, v.v.
- **Định dạng**, nếu bạn muốn các câu hỏi được định dạng theo một cách nhất định thì sao?

Như bạn thấy, có rất nhiều điều cần cân nhắc khi tạo lời nhắc.

Cho đến nay, chúng ta đã thấy một ví dụ về lời nhắc đơn giản, nhưng AI tạo sinh có khả năng làm được nhiều hơn để giúp mọi người trong nhiều vai trò và ngành nghề khác nhau. Hãy khám phá một số kỹ thuật cơ bản tiếp theo.

### Các kỹ thuật tạo lời nhắc

Trước tiên, chúng ta cần hiểu rằng việc tạo lời nhắc là một thuộc tính _phát sinh_ của LLM, nghĩa là đây không phải là một tính năng được tích hợp sẵn trong mô hình mà là điều chúng ta khám phá khi sử dụng mô hình.

Có một số kỹ thuật cơ bản mà chúng ta có thể sử dụng để tạo lời nhắc cho LLM. Hãy cùng khám phá chúng.

- **Lời nhắc không mẫu**, đây là hình thức tạo lời nhắc cơ bản nhất. Nó là một lời nhắc đơn yêu cầu phản hồi từ LLM chỉ dựa trên dữ liệu huấn luyện của nó.
- **Lời nhắc ít mẫu**, loại lời nhắc này hướng dẫn LLM bằng cách cung cấp 1 hoặc nhiều ví dụ mà nó có thể dựa vào để tạo ra phản hồi.
- **Chuỗi suy nghĩ**, loại lời nhắc này hướng dẫn LLM cách phân tích một vấn đề thành các bước.
- **Kiến thức được tạo ra**, để cải thiện phản hồi của lời nhắc, bạn có thể cung cấp các sự kiện hoặc kiến thức được tạo ra bổ sung vào lời nhắc của mình.
- **Từ ít đến nhiều**, giống như chuỗi suy nghĩ, kỹ thuật này liên quan đến việc phân tích một vấn đề thành một loạt các bước và sau đó yêu cầu thực hiện các bước này theo thứ tự.
- **Tự cải thiện**, kỹ thuật này liên quan đến việc phê bình đầu ra của LLM và sau đó yêu cầu nó cải thiện.
- **Lời nhắc maieutic**, mục tiêu ở đây là đảm bảo câu trả lời của LLM là chính xác và bạn yêu cầu nó giải thích các phần khác nhau của câu trả lời. Đây là một dạng tự cải thiện.

### Lời nhắc không mẫu

Phong cách tạo lời nhắc này rất đơn giản, nó bao gồm một lời nhắc duy nhất. Đây có lẽ là kỹ thuật mà bạn đang sử dụng khi bắt đầu tìm hiểu về LLM. Đây là một ví dụ:

- Lời nhắc: "Algebra là gì?"
- Trả lời: "Algebra là một nhánh của toán học nghiên cứu các ký hiệu toán học và các quy tắc để thao tác các ký hiệu này."

### Lời nhắc ít mẫu

Phong cách tạo lời nhắc này giúp mô hình bằng cách cung cấp một vài ví dụ cùng với yêu cầu. Nó bao gồm một lời nhắc duy nhất với dữ liệu cụ thể về nhiệm vụ. Đây là một ví dụ:

- Lời nhắc: "Viết một bài thơ theo phong cách của Shakespeare. Đây là một vài ví dụ về sonnet của Shakespeare:
  Sonnet 18: 'Shall I compare thee to a summer's day? Thou art more lovely and more temperate...'
  Sonnet 116: 'Let me not to the marriage of true minds Admit impediments. Love is not
Như bạn có thể thấy, kết quả không thể đa dạng hơn.

> Lưu ý rằng có nhiều tham số bạn có thể thay đổi để làm đa dạng đầu ra, như top-k, top-p, hình phạt lặp lại, hình phạt độ dài và hình phạt đa dạng, nhưng những điều này nằm ngoài phạm vi của chương trình học này.

## Thực hành tốt

Có nhiều cách thực hành bạn có thể áp dụng để đạt được kết quả mong muốn. Bạn sẽ tìm ra phong cách riêng của mình khi sử dụng kỹ thuật gợi ý ngày càng nhiều.

Ngoài các kỹ thuật chúng ta đã đề cập, có một số thực hành tốt cần cân nhắc khi gợi ý cho LLM.

Dưới đây là một số thực hành tốt cần cân nhắc:

- **Xác định ngữ cảnh**. Ngữ cảnh rất quan trọng, càng xác định rõ như lĩnh vực, chủ đề, v.v. thì càng tốt.
- Giới hạn đầu ra. Nếu bạn muốn một số lượng mục cụ thể hoặc độ dài cụ thể, hãy chỉ định nó.
- **Xác định cả cái gì và cách làm**. Hãy nhớ đề cập cả cái bạn muốn và cách bạn muốn nó, ví dụ "Tạo một Python Web API với các route products và customers, chia thành 3 file".
- **Sử dụng mẫu**. Thường thì bạn sẽ muốn làm phong phú gợi ý của mình bằng dữ liệu từ công ty của bạn. Sử dụng mẫu để làm điều này. Mẫu có thể có các biến mà bạn thay thế bằng dữ liệu thực tế.
- **Viết đúng chính tả**. LLM có thể cung cấp cho bạn một câu trả lời đúng, nhưng nếu bạn viết đúng chính tả, bạn sẽ nhận được câu trả lời tốt hơn.

## Bài tập

Dưới đây là đoạn mã Python minh họa cách xây dựng một API đơn giản bằng Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Sử dụng một trợ lý AI như GitHub Copilot hoặc ChatGPT và áp dụng kỹ thuật "tự cải thiện" để nâng cao đoạn mã.

## Giải pháp

Hãy thử giải bài tập bằng cách thêm các gợi ý phù hợp vào đoạn mã.

> [!TIP]
> Đưa ra một gợi ý để yêu cầu cải thiện, tốt nhất là giới hạn số lượng cải tiến. Bạn cũng có thể yêu cầu cải thiện theo một cách cụ thể, ví dụ như kiến trúc, hiệu suất, bảo mật, v.v.

[Giải pháp](../../../05-advanced-prompts/python/aoai-solution.py)

## Kiểm tra kiến thức

Tại sao tôi nên sử dụng kỹ thuật gợi ý chuỗi tư duy? Hãy cho tôi 1 câu trả lời đúng và 2 câu trả lời sai.

1. Để dạy LLM cách giải quyết một vấn đề.
1. B, Để dạy LLM tìm lỗi trong mã.
1. C, Để hướng dẫn LLM đưa ra các giải pháp khác nhau.

A: 1, bởi vì gợi ý chuỗi tư duy là về việc chỉ cho LLM cách giải quyết một vấn đề bằng cách cung cấp cho nó một loạt các bước, và các vấn đề tương tự cùng cách chúng đã được giải quyết.

## 🚀 Thử thách

Bạn vừa sử dụng kỹ thuật tự cải thiện trong bài tập. Hãy lấy bất kỳ chương trình nào bạn đã xây dựng và cân nhắc những cải tiến bạn muốn áp dụng cho nó. Bây giờ hãy sử dụng kỹ thuật tự cải thiện để áp dụng các thay đổi được đề xuất. Bạn nghĩ kết quả thế nào, tốt hơn hay tệ hơn?

## Làm tốt lắm! Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học về AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh!

Hãy chuyển sang Bài học 6, nơi chúng ta sẽ áp dụng kiến thức về Kỹ thuật Gợi ý bằng cách [xây dựng ứng dụng tạo văn bản](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.