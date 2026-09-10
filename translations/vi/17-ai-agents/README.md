[![Mô hình Mã nguồn mở](../../../translated_images/vi/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Giới thiệu

Các Đại lý AI đại diện cho một bước phát triển thú vị trong AI Phát sinh, cho phép Các Mô hình Ngôn ngữ Lớn (LLM) tiến hóa từ trợ lý thành các đại lý có khả năng thực hiện hành động. Các khung đại lý AI cho phép nhà phát triển tạo các ứng dụng cung cấp cho LLM quyền truy cập vào công cụ và quản lý trạng thái. Các khung này cũng nâng cao khả năng quan sát, cho phép người dùng và nhà phát triển theo dõi các hành động do LLM lập kế hoạch, từ đó cải thiện quản lý trải nghiệm.

Bài học sẽ bao gồm các lĩnh vực sau:

- Hiểu đại lý AI là gì - Đại lý AI chính xác là gì?
- Khám phá năm khung đại lý AI khác nhau - Điều gì làm cho chúng độc đáo?
- Áp dụng các Đại lý AI này vào các trường hợp sử dụng khác nhau - Khi nào nên sử dụng Đại lý AI?

## Mục tiêu học tập

Sau khi học xong bài học này, bạn sẽ có thể:

- Giải thích đại lý AI là gì và cách sử dụng chúng.
- Hiểu sự khác biệt giữa một số Khung đại lý AI phổ biến và cách chúng khác nhau.
- Hiểu cách hoạt động của Đại lý AI để xây dựng ứng dụng với chúng.

## Đại lý AI là gì?

Đại lý AI là một lĩnh vực rất thú vị trong thế giới AI Phát sinh. Cùng với sự phấn khích này đôi khi có sự nhầm lẫn về thuật ngữ và cách áp dụng. Để đơn giản và bao gồm hầu hết các công cụ được gọi là Đại lý AI, chúng ta sẽ sử dụng định nghĩa sau:

Đại lý AI cho phép Các Mô hình Ngôn ngữ Lớn (LLM) thực hiện các nhiệm vụ bằng cách cung cấp cho chúng quyền truy cập vào **trạng thái** và **công cụ**.

![Mô hình Đại lý](../../../translated_images/vi/what-agent.21f2893bdfd01e6a.webp)

Hãy định nghĩa các thuật ngữ này:

**Các Mô hình Ngôn ngữ Lớn** - Đây là các mô hình được nhắc đến trong suốt khóa học như GPT-5, GPT-4o, và Llama 3.3, vv.

**Trạng thái** - Đây là ngữ cảnh mà LLM đang làm việc trong đó. LLM sử dụng ngữ cảnh của các hành động trước đây và ngữ cảnh hiện tại để hướng dẫn quyết định cho các hành động tiếp theo. Các Khung Đại lý AI cho phép nhà phát triển duy trì ngữ cảnh này dễ dàng hơn.

**Công cụ** - Để hoàn thành nhiệm vụ người dùng yêu cầu và do LLM lên kế hoạch, LLM cần quyền truy cập vào các công cụ. Một số ví dụ về công cụ có thể là cơ sở dữ liệu, API, ứng dụng bên ngoài hoặc thậm chí một LLM khác!

Những định nghĩa này hy vọng sẽ cung cấp cho bạn nền tảng tốt khi chúng ta xem cách chúng được triển khai. Hãy khám phá một vài khung đại lý AI khác nhau:

## Đại lý LangChain

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) là một triển khai của các định nghĩa mà chúng tôi đã cung cấp ở trên.

Để quản lý **trạng thái**, nó sử dụng một hàm tích hợp gọi là `AgentExecutor`. Hàm này nhận vào `agent` đã định nghĩa và các `tools` sẵn có cho nó.

`Agent Executor` cũng lưu giữ lịch sử trò chuyện để cung cấp ngữ cảnh cho cuộc trò chuyện.

![Đại lý Langchain](../../../translated_images/vi/langchain-agents.edcc55b5d5c43716.webp)

LangChain cung cấp một [danh mục công cụ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) có thể được nhập vào ứng dụng của bạn để LLM có thể truy cập. Đây là những công cụ do cộng đồng và đội ngũ LangChain tạo ra.

Bạn có thể định nghĩa các công cụ này và truyền chúng cho `Agent Executor`.

Khả năng quan sát là một khía cạnh quan trọng khác khi nói về Đại lý AI. Việc hiểu công cụ nào LLM đang sử dụng và lý do là rất quan trọng đối với nhà phát triển ứng dụng. Vì điều đó, đội ngũ LangChain đã phát triển LangSmith.

## AutoGen

Khung đại lý AI tiếp theo chúng ta sẽ thảo luận là [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Trọng tâm chính của AutoGen là các cuộc hội thoại. Các đại lý vừa **có khả năng đàm thoại** vừa **có thể tùy chỉnh**.

**Có khả năng đàm thoại -** Các LLM có thể bắt đầu và tiếp tục cuộc trò chuyện với LLM khác để hoàn thành nhiệm vụ. Điều này được thực hiện bằng cách tạo ra các `AssistantAgents` và cung cấp cho chúng một thông điệp hệ thống cụ thể.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Có thể tùy chỉnh** - Đại lý không chỉ được định nghĩa như LLM mà còn có thể là người dùng hoặc công cụ. Là nhà phát triển, bạn có thể định nghĩa `UserProxyAgent` chịu trách nhiệm tương tác với người dùng để lấy phản hồi trong việc hoàn thành nhiệm vụ. Phản hồi này có thể tiếp tục thực hiện nhiệm vụ hoặc dừng lại.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Trạng thái và Công cụ

Để thay đổi và quản lý trạng thái, một đại lý trợ lý tạo mã Python để hoàn thành nhiệm vụ.

Đây là ví dụ về quy trình:

![AutoGen](../../../translated_images/vi/autogen.dee9a25a45fde584.webp)

#### LLM được định nghĩa với thông điệp hệ thống

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Thông điệp hệ thống này hướng dẫn LLM cụ thể này về các chức năng liên quan đến nhiệm vụ của nó. Hãy nhớ, với AutoGen bạn có thể định nghĩa nhiều AssistantAgents với các thông điệp hệ thống khác nhau.

#### Trò chuyện được khởi tạo bởi người dùng

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Tin nhắn này từ user_proxy (Con người) là thứ sẽ bắt đầu quá trình đại lý khám phá các chức năng có thể nó nên thực hiện.

#### Hàm được thực thi

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Khi trò chuyện ban đầu được xử lý, đại lý sẽ gửi công cụ đề xuất để gọi. Trong trường hợp này, đó là một hàm gọi là `get_weather`. Tùy thuộc vào cấu hình của bạn, hàm này có thể được tự động thực thi và đọc bởi đại lý hoặc có thể được thực thi dựa trên đầu vào của người dùng.

Bạn có thể tìm thấy danh sách [mẫu mã AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) để khám phá thêm cách bắt đầu xây dựng.

## Khung đại lý Microsoft

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) là SDK mã nguồn mở của Microsoft để xây dựng Đại lý AI và hệ thống đa đại lý trong cả **Python** và **.NET**. Nó kết hợp sức mạnh của hai dự án Microsoft trước đây — các tính năng doanh nghiệp của **Semantic Kernel** và điều phối đa đại lý của **AutoGen** — thành một khung duy nhất được hỗ trợ. Nếu bạn đang bắt đầu một dự án đại lý mới hôm nay, đây là người kế nhiệm được khuyến nghị của AutoGen.

Khung này mở rộng từ một **đại lý trò chuyện** đơn đến các **quy trình làm việc đa đại lý** phức tạp, và tích hợp trực tiếp với Microsoft Foundry, Azure OpenAI, và OpenAI. Nó cũng cung cấp khả năng quan sát tích hợp thông qua OpenTelemetry để bạn có thể theo dõi chính xác những gì đại lý của bạn đang làm.

### Trạng thái và Công cụ

**Trạng thái** - Khung này quản lý ngữ cảnh cuộc hội thoại cho bạn thông qua **thread**. Một đại lý theo dõi lịch sử tin nhắn (yêu cầu người dùng, gọi công cụ và kết quả của chúng), do đó mỗi lượt là xây dựng dựa trên những lượt trước đó. Thread cũng có thể được lưu trữ lâu dài, cho phép cuộc trò chuyện bị tạm dừng và tiếp tục sau.

**Công cụ** - Bạn cung cấp công cụ cho đại lý bằng cách truyền các hàm Python thuần túy. Các tham số được chú thích kiểu tự động chuyển thành một lược đồ, để mô hình biết cách và khi nào gọi chúng (gọi hàm). Khung này cũng hỗ trợ các máy chủ Giao thức Ngữ cảnh Mô hình (MCP) và các công cụ được lưu trữ như trình thông dịch mã.

Đây là ví dụ về một đại lý đơn với một công cụ tùy chỉnh:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Để kết nối với Azure OpenAI trong Microsoft Foundry, thay vào đó truyền điểm cuối và thông tin xác thực của bạn cho client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Quy trình làm việc đa đại lý

Nơi khung này thật sự nổi bật là điều phối nhiều đại lý cùng nhau. Ví dụ, bạn có thể chạy các đại lý lần lượt (mỗi đại lý truyền ngữ cảnh của mình cho đại lý tiếp theo) hoặc phân tán đến nhiều đại lý đồng thời và tổng hợp kết quả của chúng:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Chạy các tác nhân theo trình tự, truyền ngữ cảnh hội thoại dọc theo chuỗi
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Phân tán đến các tác nhân cùng lúc, sau đó tổng hợp phản hồi của họ
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Để cài đặt khung và bắt đầu:

```bash
pip install agent-framework-core
# Tích hợp tùy chọn
pip install agent-framework-openai       # OpenAI và Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Bạn có thể khám phá thêm ở [kho lưu trữ Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) và [tài liệu chính thức](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Khung đại lý tiếp theo chúng ta sẽ khám phá là [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Nó được biết đến là đại lý "ưu tiên mã" vì thay vì làm việc chặt chẽ với `strings`, nó có thể làm việc với DataFrame trong Python. Điều này trở nên cực kỳ hữu ích cho các nhiệm vụ phân tích và tạo dữ liệu. Những việc này có thể là tạo đồ thị và biểu đồ hoặc tạo số ngẫu nhiên.

### Trạng thái và Công cụ

Để quản lý trạng thái cuộc trò chuyện, TaskWeaver sử dụng khái niệm `Planner`. `Planner` là một LLM nhận yêu cầu từ người dùng và lập bản đồ các nhiệm vụ cần hoàn thành để đáp ứng yêu cầu này.

Để hoàn thành các nhiệm vụ, `Planner` được cung cấp bộ sưu tập các công cụ gọi là `Plugins`. Đây có thể là các lớp Python hoặc một trình thông dịch mã chung. Các plugin này được lưu trữ dưới dạng embedding để LLM có thể tìm kiếm plugin chính xác hơn.

![Taskweaver](../../../translated_images/vi/taskweaver.da8559999267715a.webp)

Đây là ví dụ về một plugin để xử lý phát hiện dị thường:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Mã được xác minh trước khi thực thi. Một tính năng khác để quản lý ngữ cảnh trong Taskweaver là `experience`. Experience cho phép lưu trữ ngữ cảnh của một cuộc trò chuyện lâu dài trong một tập tin YAML. Điều này có thể được cấu hình để LLM cải thiện theo thời gian trên một số nhiệm vụ nhất định nếu nó được tiếp xúc với các cuộc trò chuyện trước.

## JARVIS

Khung đại lý cuối cùng chúng ta sẽ khám phá là [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Điều làm cho JARVIS độc đáo là nó sử dụng một LLM để quản lý `trạng thái` cuộc trò chuyện trong khi `công cụ` là các mô hình AI khác. Mỗi mô hình AI là mô hình chuyên biệt thực hiện các nhiệm vụ cụ thể như phát hiện đối tượng, chuyển ngữ hoặc chú thích hình ảnh.

![JARVIS](../../../translated_images/vi/jarvis.762ddbadbd1a3a33.webp)

LLM, là mô hình đa năng, nhận yêu cầu từ người dùng và xác định nhiệm vụ cụ thể cùng bất kỳ đối số/dữ liệu cần thiết để hoàn thành nhiệm vụ.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM sau đó định dạng yêu cầu theo cách mà mô hình AI chuyên biệt có thể hiểu, ví dụ như JSON. Khi mô hình AI trả về dự đoán dựa trên nhiệm vụ, LLM sẽ nhận được phản hồi.

Nếu cần nhiều mô hình để hoàn thành nhiệm vụ, LLM cũng sẽ giải thích phản hồi từ các mô hình đó trước khi kết hợp chúng để tạo phản hồi cho người dùng.

Ví dụ dưới đây cho thấy cách hoạt động khi người dùng yêu cầu mô tả và đếm các vật thể trong một bức ảnh:

## Bài tập

Để tiếp tục học về Đại lý AI, bạn có thể xây dựng với Microsoft Agent Framework:

- Một ứng dụng mô phỏng cuộc họp kinh doanh với các phòng ban khác nhau của một startup giáo dục.
- Tạo các thông điệp hệ thống hướng dẫn LLM hiểu các nhân vật và ưu tiên khác nhau, và cho phép người dùng trình bày ý tưởng sản phẩm mới.
- LLM sau đó nên tạo câu hỏi tiếp theo từ mỗi phòng ban để tinh chỉnh và cải thiện bài trình bày và ý tưởng sản phẩm.

## Học tập không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học tập AI Phát sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức AI Phát sinh của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->