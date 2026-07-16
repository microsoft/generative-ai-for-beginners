[![Open Source Models](../../../translated_images/th/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## บทนำ

AI Agents เป็นการพัฒนาที่น่าตื่นเต้นใน Generative AI ซึ่งช่วยให้ Large Language Models (LLMs) พัฒนาจากผู้ช่วยเป็นผู้แทนที่สามารถดำเนินการต่างๆ ได้ กรอบงาน AI Agent ช่วยให้นักพัฒนาสร้างแอปพลิเคชันที่ให้ LLMs เข้าถึงเครื่องมือและการจัดการสถานะ กรอบงานเหล่านี้ยังช่วยเพิ่มความโปร่งใส ทำให้ผู้ใช้และนักพัฒนาสามารถติดตามการดำเนินการที่ LLMs วางแผนไว้ จึงช่วยปรับปรุงการจัดการประสบการณ์

บทเรียนนี้จะครอบคลุมหัวข้อต่อไปนี้:

- ทำความเข้าใจว่า AI Agent คืออะไร - AI Agent คืออะไรอย่างแท้จริง?
- สำรวจกรอบงาน AI Agent ห้ารูปแบบ - อะไรที่ทำให้พวกเขาโดดเด่น?
- การประยุกต์ใช้ AI Agents ในกรณีใช้งานที่แตกต่างกัน - ควรใช้ AI Agents เมื่อใด?

## เป้าหมายการเรียนรู้

หลังจากเรียนบทนี้แล้ว คุณจะสามารถ:

- อธิบายว่า AI Agents คืออะไรและวิธีการใช้งาน
- เข้าใจความแตกต่างระหว่างกรอบงาน AI Agent ยอดนิยมบางอย่าง และวิธีที่พวกเขาแตกต่างกัน
- เข้าใจการทำงานของ AI Agents เพื่อนำไปใช้สร้างแอปพลิเคชัน

## AI Agents คืออะไร?

AI Agents เป็นสาขาที่น่าตื่นเต้นมากในโลกของ Generative AI ด้วยความตื่นเต้นนี้บางครั้งทำให้เกิดความสับสนเกี่ยวกับคำศัพท์และการประยุกต์ใช้ เพื่อให้ง่ายและครอบคลุมเครื่องมือส่วนใหญ่ที่เรียกว่า AI Agents เราจะใช้คำนิยามนี้:

AI Agents ช่วยให้ Large Language Models (LLMs) สามารถทำงานต่างๆ ได้โดยให้พวกเขาเข้าถึง **สถานะ** และ **เครื่องมือ**

![Agent Model](../../../translated_images/th/what-agent.21f2893bdfd01e6a.webp)

ให้เรานิยามคำเหล่านี้:

**Large Language Models** - คือโมเดลที่กล่าวถึงตลอดหลักสูตรนี้ เช่น GPT-3.5, GPT-4, Llama-2 เป็นต้น

**สถานะ (State)** - คือบริบทที่ LLM กำลังทำงานอยู่ LLM ใช้บริบทของการกระทำที่ผ่านมาและบริบทปัจจุบันเพื่อชี้นำการตัดสินใจในการดำเนินการต่อไป กรอบงาน AI Agent ช่วยให้นักพัฒนาจัดการบริบทนี้ได้ง่ายขึ้น

**เครื่องมือ (Tools)** - เพื่อทำงานที่ผู้ใช้ร้องขอและ LLM วางแผนไว้ให้เสร็จ LLM จำเป็นต้องเข้าถึงเครื่องมือ เช่น ฐานข้อมูล, API, แอปพลิเคชันภายนอก หรือแม้แต่ LLM ตัวอื่น!

คำนิยามเหล่านี้หวังว่าจะช่วยให้คุณมีความเข้าใจที่ดีเมื่อเราดูวิธีการใช้งานจริง มาสำรวจกรอบงาน AI Agent ต่างๆ กัน:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) เป็นการนำคำนิยามที่เรากล่าวมาข้างต้นไปใช้งาน

เพื่อจัดการ **สถานะ** ใช้ฟังก์ชันในตัวชื่อว่า `AgentExecutor` ซึ่งรับ `agent` ที่กำหนดไว้และ `tools` ที่มีให้ใช้งาน

`Agent Executor` ยังบันทึกประวัติการสนทนาเพื่อจัดบริบทของการแชท

![Langchain Agents](../../../translated_images/th/langchain-agents.edcc55b5d5c43716.webp)

LangChain มี [แคตตาล็อกเครื่องมือ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) ที่สามารถนำเข้าไปในแอปพลิเคชันเพื่อให้ LLM เข้าถึงได้ สร้างขึ้นโดยชุมชนและทีม LangChain

จากนั้นคุณสามารถกำหนดเครื่องมือเหล่านี้และส่งผ่านไปยัง `Agent Executor`

ความโปร่งใสเป็นอีกประเด็นสำคัญเมื่อพูดถึง AI Agents นักพัฒนาแอปพลิเคชันจำเป็นต้องเข้าใจว่า LLM กำลังใช้เครื่องมือใดและทำไม ทีมงาน LangChain จึงได้พัฒนา LangSmith เพื่อช่วยในเรื่องนี้

## AutoGen

กรอบงาน AI Agent ถัดไปที่เราจะพูดถึงคือ [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst) จุดเน้นหลักของ AutoGen คือบทสนทนา Agents เป็นทั้ง **สามารถสนทนาได้** และ **ปรับแต่งได้**

**สามารถสนทนาได้ -** LLMs สามารถเริ่มและดำเนินการสนทนากับ LLM ตัวอื่นเพื่อทำงานให้เสร็จ โดยสร้าง `AssistantAgents` และมอบข้อความระบบเฉพาะให้

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**ปรับแต่งได้** - Agents สามารถถูกกำหนดไม่ใช่แค่เป็น LLM แต่เป็นผู้ใช้หรือเครื่องมือได้ ในฐานะนักพัฒนา คุณสามารถกำหนด `UserProxyAgent` ซึ่งรับผิดชอบการโต้ตอบกับผู้ใช้เพื่อรับผลตอบรับเกี่ยวกับการทำงานให้เสร็จ ผลตอบรับนี้สามารถทำให้การทำงานดำเนินต่อหรือหยุดได้

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### สถานะและเครื่องมือ

เพื่อเปลี่ยนแปลงและจัดการสถานะ ตัวช่วย Agent จะสร้างโค้ด Python เพื่อทำงานให้เสร็จ

นี่คือตัวอย่างของกระบวนการ:

![AutoGen](../../../translated_images/th/autogen.dee9a25a45fde584.webp)

#### LLM ถูกกำหนดด้วยข้อความระบบ

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

ข้อความระบบนี้ชี้นำ LLM เฉพาะเจาะจงไปยังฟังก์ชันที่เกี่ยวข้องกับงาน จำไว้ว่ากับ AutoGen คุณสามารถมี AssistantAgents หลายตัวที่มาพร้อมข้อความระบบต่างกัน

#### การสนทนาถูกเริ่มโดยผู้ใช้

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

ข้อความนี้จาก user_proxy (มนุษย์) จะเริ่มกระบวนการที่ Agent จะสำรวจฟังก์ชันที่ควรจะดำเนินการ

#### ฟังก์ชันถูกดำเนินการ

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

เมื่อประมวลผลการสนทนาเริ่มต้น Agent จะส่งเครื่องมือที่แนะนำให้เรียกใช้ ในกรณีนี้คือฟังก์ชันชื่อ `get_weather` ขึ้นอยู่กับการตั้งค่าของคุณ ฟังก์ชันนี้สามารถถูกดำเนินการโดยอัตโนมัติและอ่านโดย Agent หรือดำเนินการตามป้อนข้อมูลจากผู้ใช้

คุณสามารถดูตัวอย่างโค้ด [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) เพื่อเรียนรู้วิธีเริ่มต้นสร้างงาน

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) เป็น SDK โอเพ่นซอร์สของ Microsoft สำหรับสร้าง AI Agents และระบบหลายตัวแทนใน **Python** และ **.NET** มันรวบรวมจุดแข็งของสองโปรเจกต์ก่อนหน้าของ Microsoft — คุณสมบัติองค์กรของ **Semantic Kernel** และการจัดการหลายตัวแทนของ **AutoGen** — เข้าไว้ในกรอบงานเดียวที่ได้รับการสนับสนุน หากคุณจะเริ่มโปรเจกต์ตัวแทนใหม่วันนี้ นี่คือทางเลือกที่แนะนำต่อจาก AutoGen

กรอบงานนี้สามารถขยายได้ตั้งแต่ **chat agent** ตัวเดียวไปจนถึง **เวิร์กโฟลว์หลายตัวแทนที่ซับซ้อน** และสามารถเชื่อมต่อโดยตรงกับ Microsoft Foundry, Azure OpenAI และ OpenAI นอกจากนี้ยังมีการสังเกตการณ์ในตัวผ่าน OpenTelemetry เพื่อให้คุณสามารถติดตามได้ว่าเอเย่นต์ของคุณกำลังทำอะไรอยู่

### สถานะและเครื่องมือ

**สถานะ** - กรอบงานจัดการบริบทการสนทนาให้คุณผ่าน **threads** ตัวแทนจะติดตามประวัติข้อความ (คำร้องขอของผู้ใช้ การเรียกใช้เครื่องมือ และผลลัพธ์) ดังนั้นแต่ละรอบจะต่อยอดจากรอบก่อน Threads ยังสามารถเก็บรักษาไว้ได้ ทำให้สามารถหยุดและกลับมาสนทนาใหม่ในภายหลัง

**เครื่องมือ** - คุณมอบเครื่องมือให้ตัวแทนโดยส่งฟังก์ชัน Python ธรรมดา พารามิเตอร์ที่มีการใส่ชนิดจะถูกแปลงเป็นสคีมาโดยอัตโนมัติ เพื่อให้โมเดลรู้วิธีและเวลาที่จะเรียกใช้ ฟรมเวิร์กยังรองรับเซิร์ฟเวอร์ Model Context Protocol (MCP) และเครื่องมือที่โฮสต์ เช่น ตัวแปลโค้ด

นี่คือตัวอย่างของตัวแทนเดียวที่มีเครื่องมือที่กำหนดเอง:

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

หากต้องการเชื่อมต่อกับ Azure OpenAI ใน Microsoft Foundry ให้ส่ง endpoint และข้อมูลรับรองของคุณไปยังไคลเอนต์:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### เวิร์กโฟลว์หลายตัวแทน

จุดที่กรอบงานโดดเด่นคือการจัดการตัวแทนหลายตัวร่วมกัน เช่น คุณสามารถรันตัวแทนทีละตัว (แต่ละตัวส่งต่อบริบทไปยังตัวถัดไป) หรือกระจายไปยังหลายตัวแทนพร้อมกันและรวบรวมผลลัพธ์:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# รันเอเจนต์ตามลำดับ โดยส่งต่อบริบทของการสนทนาไปตามสายโซ่
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# แยกไปยังเอเจนต์พร้อมกัน จากนั้นรวบรวมคำตอบของพวกเขา
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

ในการติดตั้งกรอบงานและเริ่มต้นใช้งาน:

```bash
pip install agent-framework-core
# การผสานรวมที่ไม่บังคับ
pip install agent-framework-openai       # OpenAI และ Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

คุณสามารถสำรวจเพิ่มเติมได้ที่ [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) และ [เอกสารอย่างเป็นทางการ](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)

## Taskweaver

กรอบงานเอเย่นต์ถัดไปที่เราจะสำรวจคือ [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst) ซึ่งเป็นที่รู้จักว่าเป็นเอเย่นต์แบบ "code-first" เพราะแทนที่จะทำงานกับ `strings` อย่างเคร่งครัด มันสามารถทำงานกับ DataFrames ใน Python ซึ่งมีประโยชน์มากสำหรับงานวิเคราะห์ข้อมูลและการสร้างข้อมูล เช่น การสร้างกราฟและแผนภูมิ หรือการสร้างตัวเลขสุ่ม

### สถานะและเครื่องมือ

เพื่อจัดการสถานะของการสนทนา TaskWeaver ใช้แนวคิดของ `Planner` ซึ่งเป็น LLM ที่รับคำขอจากผู้ใช้และวางแผนงานที่ต้องดำเนินการให้สำเร็จ

เพื่อทำงานให้สำเร็จ `Planner` จะได้รับอนุญาตให้เข้าถึงเครื่องมือที่เรียกว่า `Plugins` ซึ่งอาจเป็นคลาส Python หรือโค้ดอินเตอร์พรีเตอร์ทั่วไป ปลั๊กอินเหล่านี้ถูกเก็บเป็น embeddings เพื่อช่วยให้ LLM ค้นหาปลั๊กอินที่ถูกต้องได้ดีขึ้น

![Taskweaver](../../../translated_images/th/taskweaver.da8559999267715a.webp)

นี่คือตัวอย่างปลั๊กอินสำหรับจัดการการตรวจจับความผิดปกติ:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

โค้ดจะถูกตรวจสอบก่อนดำเนินการ อีกฟีเจอร์ที่ช่วยจัดการบริบทใน Taskweaver คือ `experience` ซึ่งอนุญาตให้จัดเก็บบริบทของการสนทนาในระยะยาวในไฟล์ YAML สามารถตั้งค่าให้ LLM ปรับปรุงการทำงานในงานบางอย่างเมื่อได้รับการเปิดเผยต่อการสนทนาเก่า

## JARVIS

กรอบงานเอเย่นต์สุดท้ายที่เราจะสำรวจคือ [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst) สิ่งที่ทำให้ JARVIS โดดเด่นคือมันใช้ LLM เพื่อจัดการ `state` ของการสนทนา และ `tools` เป็นโมเดล AI อื่นๆ ซึ่งแต่ละโมเดลเฉพาะทางทำงานบางอย่าง เช่น ตรวจจับวัตถุ, ถอดเสียง หรือใส่คำบรรยายภาพ

![JARVIS](../../../translated_images/th/jarvis.762ddbadbd1a3a33.webp)

LLM ซึ่งเป็นโมเดลทั่วไป จะรับคำขอจากผู้ใช้และระบุงานเฉพาะและข้อมูล/อาร์กิวเมนต์ใดที่จำเป็นต้องใช้ในการทำงานให้เสร็จ

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

จากนั้น LLM จะจัดรูปแบบคำขอให้อยู่ในรูปแบบที่โมเดล AI เฉพาะทางสามารถตีความได้ เช่น JSON เมื่อโมเดล AI ส่งผลลัพธ์ทำนายตามงานมาแล้ว LLM จะรับคำตอบนั้น

หากต้องใช้โมเดลหลายตัวในการทำงาน LLM จะตีความคำตอบจากโมเดลเหล่านั้นก่อนนำมารวมกันเพื่อสร้างคำตอบให้ผู้ใช้

ตัวอย่างด้านล่างแสดงการทำงานเมื่อผู้ใช้ขอคำอธิบายและนับวัตถุในภาพ:

## การบ้าน

เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับ AI Agents คุณสามารถสร้างด้วย Microsoft Agent Framework:

- แอปพลิเคชันจำลองการประชุมธุรกิจระหว่างแผนกต่างๆ ของสตาร์ทอัพการศึกษา
- สร้างข้อความระบบที่ชี้นำ LLM ในการเข้าใจบุคลิกและลำดับความสำคัญต่างๆ และให้ผู้ใช้เสนอไอเดียผลิตภัณฑ์ใหม่
- จากนั้น LLM ควรสร้างคำถามติดตามผลจากแต่ละแผนกเพื่อปรับปรุงและพัฒนาไอเดียผลิตภัณฑ์

## การเรียนรู้ไม่ได้หยุดเพียงแค่นี้ ต่อเนื่องเส้นทางของคุณ

หลังจากทำบทเรียนนี้เสร็จแล้ว เข้าไปดู [คอลเลกชันการเรียนรู้ Generative AI ของเรา](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ Generative AI ของคุณ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->