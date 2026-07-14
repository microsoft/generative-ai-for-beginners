[![Open Source Models](../../../translated_images/vi/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Giới thiệu

AI Agents đại diện cho một bước phát triển thú vị trong Generative AI, cho phép Các Mô Hình Ngôn Ngữ Lớn (LLMs) tiến hóa từ trợ lý thành các đại lý có khả năng thực hiện các hành động. Các khung AI Agent cho phép các nhà phát triển tạo ra ứng dụng mà LLMs có thể truy cập các công cụ và quản lý trạng thái. Các khung này cũng nâng cao khả năng hiển thị, cho phép người dùng và nhà phát triển giám sát các hành động được LLMs lên kế hoạch, từ đó cải thiện quản lý trải nghiệm.

Bài học sẽ bao gồm các lĩnh vực sau:

- Hiểu AI Agent là gì - AI Agent thực sự là gì?
- Khám phá năm khung AI Agent khác nhau - Điều gì làm chúng trở nên độc đáo?
- Áp dụng các AI Agent này vào các trường hợp sử dụng khác nhau - Khi nào chúng ta nên dùng AI Agents?

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Giải thích AI Agents là gì và cách chúng có thể được sử dụng.
- Hiểu được sự khác biệt giữa một số Khung AI Agent phổ biến và cách chúng khác nhau.
- Hiểu cách AI Agents hoạt động để xây dựng ứng dụng với chúng.

## AI Agents là gì?

AI Agents là một lĩnh vực rất thú vị trong thế giới Generative AI. Cùng với sự hứng khởi này đôi khi cũng có sự nhầm lẫn về thuật ngữ và ứng dụng của chúng. Để giữ mọi thứ đơn giản và bao quát các công cụ thường gọi là AI Agents, chúng ta sẽ sử dụng định nghĩa sau:

AI Agents cho phép Các Mô Hình Ngôn Ngữ Lớn (LLMs) thực hiện nhiệm vụ bằng cách cung cấp cho chúng truy cập tới **trạng thái** và **công cụ**.

![Agent Model](../../../translated_images/vi/what-agent.21f2893bdfd01e6a.webp)

Hãy định nghĩa các thuật ngữ này:

**Large Language Models** - Đây là các mô hình được nhắc đến trong suốt khóa học này như GPT-3.5, GPT-4, Llama-2, v.v.

**Trạng thái** - Đây là ngữ cảnh mà LLM đang hoạt động. LLM sử dụng ngữ cảnh của các hành động trước đó và ngữ cảnh hiện tại để định hướng quyết định cho các hành động tiếp theo. Các khung AI Agent giúp nhà phát triển duy trì ngữ cảnh này dễ dàng hơn.

**Công cụ** - Để hoàn thành nhiệm vụ người dùng yêu cầu và LLM đã lên kế hoạch, LLM cần truy cập vào các công cụ. Một số ví dụ về công cụ có thể là cơ sở dữ liệu, API, ứng dụng bên ngoài hoặc thậm chí một LLM khác!

Những định nghĩa này hy vọng sẽ giúp bạn hiểu rõ hơn khi chúng ta xem cách các thuật ngữ đó được triển khai. Hãy khám phá một vài khung AI Agent khác nhau:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) là một hiện thực của các định nghĩa mà chúng ta đã đưa ra ở trên.

Để quản lý **trạng thái**, nó sử dụng một chức năng tích hợp gọi là `AgentExecutor`. Chức năng này nhận vào `agent` đã được định nghĩa cùng với các `tools` có sẵn cho nó.

`AgentExecutor` cũng lưu trữ lịch sử cuộc trò chuyện để cung cấp ngữ cảnh cho cuộc hội thoại.

![Langchain Agents](../../../translated_images/vi/langchain-agents.edcc55b5d5c43716.webp)

LangChain cung cấp một [danh mục công cụ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) có thể được nhập vào ứng dụng của bạn mà LLM có thể truy cập. Những công cụ này được tạo ra bởi cộng đồng và đội ngũ LangChain.

Bạn có thể định nghĩa các công cụ này và truyền chúng vào `AgentExecutor`.

Khả năng hiển thị là một khía cạnh quan trọng khác khi nói về AI Agents. Điều quan trọng là các nhà phát triển ứng dụng hiểu công cụ nào LLM đang sử dụng và lý do vì sao. Vì vậy, nhóm LangChain đã phát triển LangSmith.

## AutoGen

Khung AI Agent tiếp theo mà chúng ta sẽ thảo luận là [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Trọng tâm chính của AutoGen là các cuộc hội thoại. Các Agent vừa **có thể trò chuyện** vừa **tuỳ chỉnh được**.

**Có thể trò chuyện -** LLMs có thể bắt đầu và tiếp tục cuộc trò chuyện với một LLM khác để hoàn thành nhiệm vụ. Điều này được thực hiện bằng cách tạo các `AssistantAgents` và cung cấp cho chúng một tin nhắn hệ thống cụ thể.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Tuỳ chỉnh** - Các agent không chỉ có thể được định nghĩa là LLM mà còn có thể là người dùng hoặc công cụ. Là nhà phát triển, bạn có thể định nghĩa `UserProxyAgent` chịu trách nhiệm tương tác với người dùng để nhận phản hồi trong việc hoàn thành nhiệm vụ. Phản hồi này có thể tiếp tục thực hiện nhiệm vụ hoặc dừng lại.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Trạng thái và Công cụ

Để thay đổi và quản lý trạng thái, một trợ lý Agent tạo ra mã Python để hoàn thành nhiệm vụ.

Đây là một ví dụ của quá trình:

![AutoGen](../../../translated_images/vi/autogen.dee9a25a45fde584.webp)

#### LLM được định nghĩa với tin nhắn hệ thống

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Tin nhắn hệ thống này hướng dẫn LLM cụ thể này về các chức năng liên quan đến nhiệm vụ của nó. Hãy nhớ rằng, với AutoGen bạn có thể có nhiều AssistantAgents được định nghĩa với các tin nhắn hệ thống khác nhau.

#### Cuộc trò chuyện được bắt đầu bởi người dùng

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Tin nhắn này từ user_proxy (con người) chính là thứ sẽ khởi đầu quá trình của Agent để khám phá các chức năng có thể cần thực thi.

#### Chức năng được thực thi

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Sau khi cuộc trò chuyện ban đầu được xử lý, Agent sẽ gửi công cụ được đề xuất để gọi. Trong trường hợp này là một chức năng gọi là `get_weather`. Tùy thuộc vào cấu hình của bạn, chức năng này có thể được tự động thực thi và đọc bởi Agent hoặc được thực thi dựa trên đầu vào của người dùng.

Bạn có thể tìm danh sách [mẫu mã AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) để khám phá thêm cách bắt đầu xây dựng.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) là SDK mã nguồn mở của Microsoft để xây dựng AI Agents và các hệ thống đa agent trong cả **Python** và **.NET**. Nó kết hợp sức mạnh của hai dự án trước đó của Microsoft — các tính năng doanh nghiệp của **Semantic Kernel** và sự điều phối đa agent của **AutoGen** — vào một khung hỗ trợ duy nhất. Nếu bạn bắt đầu một dự án agent mới ngày hôm nay, đây là sự kế thừa được khuyên dùng của AutoGen.

Khung này mở rộng từ một **chat agent** đơn lẻ cho đến các **quy trình làm việc đa agent** phức tạp, và tích hợp trực tiếp với Microsoft Foundry, Azure OpenAI, và OpenAI. Nó cũng cung cấp khả năng quan sát tích hợp qua OpenTelemetry để bạn có thể theo dõi chính xác những gì các agent của bạn đang làm.

### Trạng thái và Công cụ

**Trạng thái** - Khung làm việc quản lý ngữ cảnh cuộc trò chuyện cho bạn thông qua **luồng**. Một agent giữ lịch sử tin nhắn (yêu cầu người dùng, các cuộc gọi công cụ, và kết quả của chúng), vì vậy mỗi lượt tiếp theo được xây dựng dựa trên những lượt trước đó. Các luồng cũng có thể được lưu trữ, cho phép cuộc trò chuyện được tạm dừng và tiếp tục sau.

**Công cụ** - Bạn cung cấp cho agent các công cụ bằng cách truyền các hàm Python đơn giản. Các tham số được đánh dấu kiểu tự động được chuyển thành một schema, vì thế mô hình biết cách và khi nào gọi chúng (gọi hàm). Khung làm việc cũng hỗ trợ máy chủ Model Context Protocol (MCP) và các công cụ lưu trữ như trình thông dịch mã.

Dưới đây là một ví dụ về một agent đơn với một công cụ tùy chỉnh:

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

Để kết nối với Azure OpenAI trong Microsoft Foundry thay vào đó, bạn truyền endpoint và thông tin đăng nhập cho client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Quy trình làm việc đa agent

Điểm nổi bật của khung này là khả năng điều phối nhiều agent cùng lúc. Ví dụ, bạn có thể chạy các agent lần lượt (mỗi agent truyền ngữ cảnh của nó sang agent tiếp theo) hoặc phân tán ra nhiều agent song song và tổng hợp kết quả của chúng:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Chạy các tác nhân theo tuần tự, truyền ngữ cảnh cuộc trò chuyện dọc theo chuỗi
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Phân phối đến các tác nhân song song, sau đó tổng hợp các phản hồi của họ
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Để cài đặt khung và bắt đầu:

```bash
pip install agent-framework-core
# Tích hợp tùy chọn
pip install agent-framework-openai       # OpenAI và Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Bạn có thể khám phá thêm trong [kho Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) và [tài liệu chính thức](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Khung agent tiếp theo chúng ta sẽ khám phá là [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Nó được biết đến như một agent "code-first" bởi vì thay vì làm việc chỉ với `strings` , nó có thể làm việc với DataFrames trong Python. Điều này trở nên cực kỳ hữu ích cho các nhiệm vụ phân tích và tạo dữ liệu. Chẳng hạn như tạo biểu đồ hoặc tạo số ngẫu nhiên.

### Trạng thái và Công cụ

Để quản lý trạng thái của cuộc trò chuyện, TaskWeaver sử dụng khái niệm `Planner`. `Planner` là một LLM nhận yêu cầu từ người dùng và lập sơ đồ các nhiệm vụ cần hoàn thành để đáp ứng yêu cầu này.

Để hoàn thành nhiệm vụ, `Planner` được truy cập bộ công cụ gọi là `Plugins`. Đây có thể là các lớp Python hoặc một trình thông dịch mã chung. Các plugin này được lưu trữ dưới dạng embeddings để LLM có thể tìm kiếm chính xác plugin phù hợp.

![Taskweaver](../../../translated_images/vi/taskweaver.da8559999267715a.webp)

Đây là ví dụ một plugin để xử lý phát hiện dị thường:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Mã được kiểm tra trước khi thực thi. Một tính năng khác để quản lý ngữ cảnh trong Taskweaver là `experience`. Experience cho phép ngữ cảnh của cuộc trò chuyện được lưu trữ lâu dài trong một tệp YAML. Điều này có thể được cấu hình để LLM cải thiện theo thời gian trong một số nhiệm vụ khi được tiếp xúc với các cuộc hội thoại trước đó.

## JARVIS

Khung agent cuối cùng chúng ta sẽ khám phá là [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Điều làm JARVIS độc đáo là nó sử dụng một LLM để quản lý `trạng thái` của cuộc hội thoại và các `công cụ` là các mô hình AI khác. Mỗi mô hình AI là một mô hình chuyên biệt thực hiện các nhiệm vụ như phát hiện đối tượng, phiên âm, hoặc chú thích ảnh.

![JARVIS](../../../translated_images/vi/jarvis.762ddbadbd1a3a33.webp)

LLM, là một mô hình đa năng, nhận yêu cầu từ người dùng và xác định nhiệm vụ cụ thể cùng các đối số/dữ liệu cần thiết để hoàn thành nhiệm vụ.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM sau đó định dạng yêu cầu theo cách mà mô hình AI chuyên biệt có thể hiểu, như JSON. Khi mô hình AI trả về dự đoán dựa trên nhiệm vụ, LLM nhận kết quả phản hồi.

Nếu cần nhiều mô hình để hoàn thành nhiệm vụ, nó cũng sẽ giải thích các phản hồi từ các mô hình đó trước khi kết hợp lại để tạo ra câu trả lời cho người dùng.

Ví dụ dưới đây minh họa cách làm việc khi người dùng yêu cầu mô tả và đếm các đối tượng trong một bức ảnh:

## Bài tập

Để tiếp tục học tập về AI Agents bạn có thể xây dựng với Microsoft Agent Framework:

- Một ứng dụng mô phỏng cuộc họp kinh doanh với các phòng ban khác nhau của một startup giáo dục.
- Tạo các tin nhắn hệ thống hướng dẫn LLM hiểu các nhân vật và ưu tiên khác nhau, và cho phép người dùng thuyết trình ý tưởng sản phẩm mới.
- LLM sau đó nên tạo các câu hỏi tiếp theo từ mỗi phòng ban để cải thiện và hoàn thiện ý tưởng thuyết trình và sản phẩm.

## Học tập không kết thúc tại đây, hãy tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về Generative AI của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->