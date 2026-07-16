[![Open Source Models](../../../translated_images/th/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## บทนำ

AI Agents เป็นการพัฒนาที่น่าตื่นเต้นใน Generative AI ช่วยให้ Large Language Models (LLMs) พัฒนาจากผู้ช่วยไปสู่เอเย่นต์ที่สามารถดำเนินการได้ กรอบงาน AI Agent ช่วยให้นักพัฒนาสามารถสร้างแอปพลิเคชันที่ให้ LLMs เข้าถึงเครื่องมือและการจัดการสถานะ กรอบงานเหล่านี้ยังเพิ่มความโปร่งใส ทำให้ผู้ใช้และนักพัฒนาติดตามการดำเนินการที่วางแผนโดย LLMs ได้ จึงช่วยปรับปรุงการจัดการประสบการณ์

บทเรียนนี้จะครอบคลุมหัวข้อดังต่อไปนี้:

- ทำความเข้าใจว่า AI Agent คืออะไร - AI Agent คืออะไร?
- สำรวจห้ากรอบงาน AI Agent ที่แตกต่างกัน - อะไรทำให้พวกเขาโดดเด่น?
- ประยุกต์ใช้ AI Agents กับกรณีใช้งานต่างๆ - ควรใช้ AI Agents เมื่อใด?

## เป้าหมายการเรียนรู้

หลังจากเรียนบทเรียนนี้แล้ว คุณจะสามารถ:

- อธิบายว่า AI Agents คืออะไรและใช้งานอย่างไร
- เข้าใจความแตกต่างระหว่างกรอบงาน AI Agent ที่เป็นที่นิยมและความแตกต่างของพวกเขา
- เข้าใจวิธีการทำงานของ AI Agents เพื่อสร้างแอปพลิเคชันด้วยพวกเขา

## AI Agents คืออะไร?

AI Agents เป็นสาขาที่น่าตื่นเต้นมากในโลกของ Generative AI ความตื่นเต้นนี้บางครั้งทำให้เกิดความสับสนในคำศัพท์และการใช้งาน เพื่อให้ง่ายและครอบคลุมเครื่องมือส่วนใหญ่ที่เรียกว่า AI Agents เราจะใช้คำนิยามนี้:

AI Agents ช่วยให้ Large Language Models (LLMs) ทำงานโดยให้เข้าถึง **สภาพ** และ **เครื่องมือ**

![Agent Model](../../../translated_images/th/what-agent.21f2893bdfd01e6a.webp)

มาอธิบายคำเหล่านี้กัน:

**Large Language Models** - คือโมเดลที่ถูกกล่าวถึงในหลักสูตรนี้ เช่น GPT-5, GPT-4o และ Llama 3.3 เป็นต้น

**สภาพ (State)** - หมายถึงบริบทที่ LLM กำลังทำงานอยู่ LLM ใช้บริบทจากการดำเนินการในอดีตและบริบทปัจจุบัน เพื่อชี้นำการตัดสินใจสำหรับการดำเนินการถัดไป กรอบงาน AI Agent ช่วยให้นักพัฒนาจัดการบริบทนี้ได้ง่ายขึ้น

**เครื่องมือ (Tools)** - เพื่อทำงานที่ผู้ใช้ร้องขอและ LLM วางแผนไว้ LLM ต้องเข้าถึงเครื่องมือ ตัวอย่างเครื่องมือเช่น ฐานข้อมูล API แอปพลิเคชันภายนอก หรือแม้แต่ LLM ตัวอื่น!

คำนิยามเหล่านี้หวังว่าจะช่วยให้คุณเข้าใจพื้นฐานไปข้างหน้าเมื่อเราดูการนำไปใช้ มาเรียนรู้กรอบงาน AI Agent ต่างๆ กัน:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) คือการนำคำนิยามที่เรากล่าวไว้ข้างต้นไปใช้งาน

ในการจัดการ **สภาพ** ใช้ฟังก์ชันในตัวชื่อ `AgentExecutor` ซึ่งรับพารามิเตอร์ `agent` ที่กำหนดและ `tools` ที่มีให้ใช้งาน

`Agent Executor` ยังจัดเก็บประวัติการแชทเพื่อให้บริบทของการสนทนา

![Langchain Agents](../../../translated_images/th/langchain-agents.edcc55b5d5c43716.webp)

LangChain มี [แคตตาล็อกเครื่องมือ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) ที่สามารถนำเข้าไปในแอปของคุณให้ LLM เข้าถึงได้ เครื่องมือเหล่านี้สร้างโดยชุมชนและทีม LangChain

คุณสามารถกำหนดเครื่องมือเหล่านี้และส่งต่อไปยัง `Agent Executor` ได้

ความโปร่งใสเป็นเรื่องสำคัญเมื่อพูดถึง AI Agents นักพัฒนาควรเข้าใจว่า LLM ใช้เครื่องมือใดและทำไม เพื่อจุดนี้ทีม LangChain ได้พัฒนา LangSmith ขึ้นมา

## AutoGen

กรอบงาน AI Agent ถัดไปที่เราจะพูดถึงคือ [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst) จุดเน้นหลักของ AutoGen คือการสนทนา Agents มีทั้งความสามารถในการ **สนทนา** และ **ปรับแต่งได้**

**สนทนาได้ -** LLMs สามารถเริ่มและดำเนินการสนทนากับ LLM ตัวอื่นเพื่อทำงานให้สำเร็จ โดยสร้าง `AssistantAgents` และให้ข้อความระบบเฉพาะเจาะจงแต่ละตัว

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**ปรับแต่งได้** - Agents สามารถนิยามไม่เพียงแต่เป็น LLM แต่ยังเป็นผู้ใช้หรือเครื่องมือได้ ในฐานะนักพัฒนา คุณสามารถกำหนด `UserProxyAgent` ซึ่งรับผิดชอบการโต้ตอบกับผู้ใช้เพื่อรับความคิดเห็นในการทำงานเสร็จ ความคิดเห็นนี้อาจดำเนินการต่อหรือตัดสินใจหยุดงานได้

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### สภาพและเครื่องมือ

เพื่อเปลี่ยนและจัดการสภาพ ตัวช่วย Agent จะสร้างโค้ด Python เพื่อทำงานให้เสร็จ

นี่คือตัวอย่างของกระบวนการ:

![AutoGen](../../../translated_images/th/autogen.dee9a25a45fde584.webp)

#### กำหนด LLM ด้วยข้อความระบบ

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

ข้อความระบบนี้ชี้นำ LLM เฉพาะนี้ว่าฟังก์ชันใดเกี่ยวข้องกับงานของมัน โปรดจำไว้ว่า ด้วย AutoGen คุณสามารถมี AssistantAgents หลายตัวที่กำหนดด้วยข้อความระบบที่แตกต่างกัน

#### การสนทนาเริ่มจากผู้ใช้

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

ข้อความนี้จาก user_proxy (มนุษย์) จะเริ่มกระบวนการให้ Agent สำรวจฟังก์ชันที่ควรดำเนินการ

#### ฟังก์ชันถูกดำเนินการ

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

เมื่อตรวจสอบการสนทนาเริ่มแรกแล้ว Agent จะส่งเครื่องมือที่แนะนำให้เรียกใช้งาน ในกรณีนี้คือฟังก์ชันชื่อ `get_weather` ตามการตั้งค่าของคุณ ฟังก์ชันนี้อาจถูกดำเนินการโดยอัตโนมัติและอ่านผลลัพธ์โดย Agent หรือดำเนินการตามคำสั่งผู้ใช้

คุณสามารถดูตัวอย่างโค้ด [AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับการเริ่มต้นสร้าง

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) คือ SDK แบบโอเพนซอร์ซของ Microsoft สำหรับสร้าง AI Agents และระบบมัลติเอเย่นต์ในทั้ง **Python** และ **.NET** รวมจุดแข็งของโครงการ Microsoft สองตัวก่อนหน้า — คุณสมบัติองค์กรของ **Semantic Kernel** และการประสานงานมัลติเอเย่นต์ของ **AutoGen** — เป็นกรอบงานเดียวที่ได้รับการสนับสนุน หากคุณเริ่มโครงการเอเย่นต์ใหม่วันนี้ นี่คือทางเลือกที่แนะนำแทน AutoGen

กรอบงานนี้รองรับตั้งแต่ **เอเย่นต์แชท** ตัวเดียวจนถึง **เวิร์กโฟลว์มัลติเอเย่นต์** ที่ซับซ้อน และผสานรวมโดยตรงกับ Microsoft Foundry, Azure OpenAI และ OpenAI นอกจากนี้ยังมีการสังเกตการณ์ในตัวผ่าน OpenTelemetry เพื่อให้คุณติดตามได้ว่าเอเย่นต์ของคุณทำงานอย่างไรบ้าง

### สภาพและเครื่องมือ

**สภาพ** - กรอบงานจัดการบริบทการสนทนาให้โดยใช้ **เธรด (threads)** เอเย่นต์จะเก็บประวัติข้อความ (คำร้องของผู้ใช้ การเรียกใช้เครื่องมือ และผลลัพธ์) เพื่อให้แต่ละรอบทำงานต่อจากรอบก่อนหน้า เธรดยังสามารถบันทึกไว้เพื่อพักและดำเนินการต่อภายหลังได้

**เครื่องมือ** - คุณให้เครื่องมือกับเอเย่นต์โดยส่งฟังก์ชัน Python ธรรมดา พารามิเตอร์ที่มีการระบุชนิดจะถูกแปลงเป็นสคีมาโดยอัตโนมัติ เพื่อให้โมเดลรู้วิธีและเวลาที่จะเรียกใช้ (function calling) กรอบงานนี้ยังรองรับเซิร์ฟเวอร์ Model Context Protocol (MCP) และเครื่องมือโฮสต์ เช่น ตัวแปลโค้ด

นี่คือตัวอย่างของเอเย่นต์ตัวเดียวที่มีเครื่องมือที่กำหนดเอง:

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

หากต้องการเชื่อมต่อกับ Azure OpenAI ใน Microsoft Foundry ให้ส่งปลายทางและข้อมูลการรับรองความถูกต้องไปยังลูกค้า:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### เวิร์กโฟลว์มัลติเอเย่นต์

จุดเด่นของกรอบงานอยู่ที่การประสานงานเอเย่นต์หลายตัวร่วมกัน เช่น การเรียกใช้งานเอเย่นต์ทีละตัว (โดยส่งบริบทต่อกัน) หรือแยกออกไปหลายเอเย่นต์พร้อมกันแล้วรวบรวมผลลัพธ์:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# เรียกใช้งานเอเจนต์ทีละตัว ส่งต่อบริบทการสนทนาตามลำดับ
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# กระจายไปยังเอเจนต์พร้อมกัน แล้วรวบรวมการตอบกลับของพวกเขา
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

ในการติดตั้งกรอบงานและเริ่มใช้งาน:

```bash
pip install agent-framework-core
# การรวมระบบทางเลือก
pip install agent-framework-openai       # OpenAI และ Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

คุณสามารถศึกษาเพิ่มเติมได้ที่ [ที่เก็บ Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) และ [เอกสารทางการ](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)

## Taskweaver

กรอบงานเอเย่นต์ถัดไปที่เราจะสำรวจคือ [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst) ซึ่งเป็นที่รู้จักว่าเป็นเอเย่นต์แบบ "เน้นโค้ดก่อน" เพราะแทนที่จะทำงานกับสตริง (`strings`) เฉพาะ มันสามารถทำงานกับ DataFrames ใน Python ได้ ซึ่งมีประโยชน์มากในการวิเคราะห์และสร้างข้อมูล เช่น การสร้างกราฟและแผนภูมิ หรือการสร้างจำนวนสุ่ม

### สภาพและเครื่องมือ

เพื่อจัดการสภาพของการสนทนา TaskWeaver ใช้แนวคิดของ `Planner` ซึ่งเป็น LLM ที่รับคำขอจากผู้ใช้และแผนผังงานที่ต้องทำเพื่อให้สำเร็จตามคำขอนั้น

เพื่อทำงานนั้นๆ `Planner` จะเข้าถึงเครื่องมือที่เรียกว่า `Plugins` ซึ่งสามารถเป็นคลาส Python หรือโปรแกรมแปลโค้ดทั่วไป ซึ่งปลั๊กอินเหล่านี้ถูกเก็บเป็น embeddings เพื่อช่วยให้ LLM ค้นหาปลั๊กอินที่ถูกต้องได้ดีขึ้น

![Taskweaver](../../../translated_images/th/taskweaver.da8559999267715a.webp)

นี่คือตัวอย่างปลั๊กอินสำหรับการตรวจจับความผิดปกติ:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

โค้ดจะได้รับการตรวจสอบก่อนทำงาน คุณสมบัติอีกอย่างหนึ่งในการจัดการบริบทใน Taskweaver คือ `experience` ที่อนุญาตให้เก็บบริบทการสนทนาในระยะยาวในไฟล์ YAML ซึ่งสามารถตั้งค่าให้ LLM ปรับปรุงงานระยะยาวได้เมื่อได้รับสัมผัสกับการสนทนาเก่า ๆ

## JARVIS

กรอบงานเอเย่นต์สุดท้ายที่เราจะสำรวจคือ [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst) สิ่งที่ทำให้ JARVIS โดดเด่นคือมันใช้ LLM เพื่อจัดการกับ `state` ของการสนทนา และ `tools` เป็นโมเดล AI อื่นๆ แต่ละโมเดลเป็นโมเดลเฉพาะทางที่ทำงานบางอย่าง เช่น การตรวจจับวัตถุ การถอดเสียง หรือการบรรยายภาพ

![JARVIS](../../../translated_images/th/jarvis.762ddbadbd1a3a33.webp)

LLM ซึ่งเป็นโมเดลอเนกประสงค์ จะรับคำร้องจากผู้ใช้และระบุงานเฉพาะและข้อมูล/อาร์กิวเมนต์ที่จำเป็นสำหรับงานนั้น

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

จากนั้น LLM จะจัดรูปแบบคำร้องในลักษณะที่โมเดล AI เฉพาะทางสามารถตีความได้ เช่น JSON เมื่อโมเดล AI ส่งผลลัพธ์ตามงาน LLM จะได้รับคำตอบนั้น

หากต้องใช้โมเดลหลายตัวเพื่อทำงานให้เสร็จ LLM จะตีความคำตอบจากโมเดลเหล่านั้นก่อนรวมกันเพื่อสร้างคำตอบให้ผู้ใช้

ตัวอย่างด้านล่างแสดงวิธีทำงานเมื่อผู้ใช้ขอคำบรรยายและนับวัตถุในภาพ

## งานที่ได้รับมอบหมาย

เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับ AI Agents คุณสามารถสร้างด้วย Microsoft Agent Framework:

- แอปพลิเคชันที่จำลองการประชุมธุรกิจกับแผนกต่างๆ ของสตาร์ทอัพทางการศึกษา
- สร้างข้อความระบบเพื่อชี้นำ LLM ในการเข้าใจบุคลิกและลำดับความสำคัญต่างๆ และให้นักใช้เสนอไอเดียผลิตภัณฑ์ใหม่
- LLM ควรสร้างคำถามติดตามผลจากแต่ละแผนกเพื่อปรับปรุงและพัฒนาไอเดียผลิตภัณฑ์

## การเรียนรู้ไม่หยุดที่นี่ ดำเนินต่อไป

หลังจากเสร็จสิ้นบทเรียนนี้แล้ว ลองดู [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อพัฒนาความรู้ Generative AI ของคุณต่อไป!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->