<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11f03c81f190d9cbafd0f977dcbede6c",
  "translation_date": "2025-05-20T07:24:13+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "th"
}
-->
[![Open Source Models](../../../translated_images/17-lesson-banner.85938ffe06e157e1dfc9ae2fcf0de326892e71c463f62b397291ad54bd8e9602.th.png)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## บทนำ

AI Agents เป็นการพัฒนาใหม่ที่น่าตื่นเต้นใน Generative AI ซึ่งทำให้ Large Language Models (LLMs) พัฒนาไปจากผู้ช่วยกลายเป็นตัวแทนที่สามารถดำเนินการได้ เฟรมเวิร์กของ AI Agent ช่วยให้นักพัฒนาสามารถสร้างแอปพลิเคชันที่ให้ LLMs เข้าถึงเครื่องมือและการจัดการสถานะ เฟรมเวิร์กเหล่านี้ยังช่วยเพิ่มการมองเห็น ทำให้ผู้ใช้และนักพัฒนาสามารถติดตามการกระทำที่ LLMs วางแผนไว้ได้ ซึ่งช่วยปรับปรุงการจัดการประสบการณ์

บทเรียนนี้จะครอบคลุมหัวข้อต่อไปนี้:

- ทำความเข้าใจว่า AI Agent คืออะไร - AI Agent คืออะไรกันแน่?
- สำรวจเฟรมเวิร์ก AI Agent สี่ประเภท - อะไรทำให้พวกเขามีเอกลักษณ์เฉพาะตัว?
- การนำ AI Agents ไปใช้ในกรณีการใช้งานต่าง ๆ - เมื่อไหร่เราควรใช้ AI Agents?

## เป้าหมายการเรียนรู้

หลังจากเรียนบทเรียนนี้ คุณจะสามารถ:

- อธิบายว่า AI Agents คืออะไรและสามารถนำไปใช้ได้อย่างไร
- มีความเข้าใจในความแตกต่างระหว่างเฟรมเวิร์ก AI Agent ยอดนิยมบางตัว และความแตกต่างระหว่างพวกเขา
- เข้าใจวิธีการทำงานของ AI Agents เพื่อสร้างแอปพลิเคชันด้วยพวกเขา

## AI Agents คืออะไร?

AI Agents เป็นสนามที่น่าตื่นเต้นมากในโลกของ Generative AI ด้วยความตื่นเต้นนี้บางครั้งทำให้เกิดความสับสนในเรื่องคำศัพท์และการใช้งาน เพื่อให้เรื่องง่ายและครอบคลุมเครื่องมือส่วนใหญ่ที่เรียกว่า AI Agents เราจะใช้คำจำกัดความนี้:

AI Agents ช่วยให้ Large Language Models (LLMs) สามารถทำงานได้โดยให้พวกเขาเข้าถึง **สถานะ** และ **เครื่องมือ**

![Agent Model](../../../translated_images/what-agent.61a7315e4b722e06561f6c93e682a51357308b53884f00af289b5a81e3e65242.th.png)

มาทำความเข้าใจคำเหล่านี้:

**Large Language Models** - นี่คือโมเดลที่ถูกกล่าวถึงตลอดหลักสูตรนี้ เช่น GPT-3.5, GPT-4, Llama-2 เป็นต้น

**สถานะ** - นี่หมายถึงบริบทที่ LLM กำลังทำงานอยู่ LLM ใช้บริบทของการกระทำที่ผ่านมาและบริบทปัจจุบันในการตัดสินใจสำหรับการกระทำถัดไป เฟรมเวิร์ก AI Agent ช่วยให้นักพัฒนาสามารถรักษาบริบทนี้ได้ง่ายขึ้น

**เครื่องมือ** - เพื่อทำงานที่ผู้ใช้ร้องขอและที่ LLM วางแผนไว้ LLM จำเป็นต้องเข้าถึงเครื่องมือ ตัวอย่างของเครื่องมืออาจเป็นฐานข้อมูล, API, แอปพลิเคชันภายนอก หรือแม้กระทั่ง LLM อื่น!

คำจำกัดความเหล่านี้หวังว่าจะให้พื้นฐานที่ดีในการก้าวไปข้างหน้าเมื่อเราดูวิธีการที่พวกเขาถูกนำไปใช้ มาสำรวจเฟรมเวิร์ก AI Agent ที่แตกต่างกัน:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) เป็นการนำคำจำกัดความที่เรากล่าวถึงมาใช้

เพื่อจัดการ **สถานะ** จะใช้ฟังก์ชันในตัวที่เรียกว่า `AgentExecutor` ซึ่งยอมรับ `agent` ที่กำหนดและ `tools` ที่มีอยู่

`Agent Executor` ยังจัดเก็บประวัติการสนทนาเพื่อให้บริบทของการสนทนา

![Langchain Agents](../../../translated_images/langchain-agents.4709b559c14be8903a59abf4ebef43916a23fac43924b133a7552121ff5e6730.th.png)

LangChain มี [แคตตาล็อกเครื่องมือ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) ที่สามารถนำเข้าไปในแอปพลิเคชันของคุณที่ LLM สามารถเข้าถึงได้ สิ่งเหล่านี้ถูกสร้างขึ้นโดยชุมชนและทีม LangChain

คุณสามารถกำหนดเครื่องมือเหล่านี้และส่งต่อไปยัง `Agent Executor`

การมองเห็นเป็นอีกหนึ่งด้านสำคัญเมื่อพูดถึง AI Agents เป็นสิ่งสำคัญสำหรับนักพัฒนาแอปพลิเคชันที่จะเข้าใจว่าเครื่องมือใดที่ LLM กำลังใช้อยู่และทำไม สำหรับสิ่งนั้น ทีมที่ LangChain ได้พัฒนา LangSmith

## AutoGen

เฟรมเวิร์ก AI Agent ถัดไปที่เราจะพูดถึงคือ [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst) จุดเน้นหลักของ AutoGen คือการสนทนา Agents สามารถ **สนทนาได้** และ **ปรับแต่งได้**

**สนทนาได้ -** LLMs สามารถเริ่มและดำเนินการสนทนากับ LLM อื่นเพื่อทำงานให้เสร็จสิ้น สิ่งนี้ทำได้โดยการสร้าง `AssistantAgents` และให้ข้อความระบบเฉพาะ

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**ปรับแต่งได้** - Agents สามารถถูกกำหนดไม่เพียงแค่เป็น LLMs แต่เป็นผู้ใช้หรือเครื่องมือ ในฐานะนักพัฒนา คุณสามารถกำหนด `UserProxyAgent` ซึ่งรับผิดชอบในการโต้ตอบกับผู้ใช้เพื่อรับข้อเสนอแนะในการทำงานให้เสร็จ ข้อเสนอแนะนี้สามารถดำเนินการต่อหรือหยุดการดำเนินการของงานได้

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### สถานะและเครื่องมือ

เพื่อเปลี่ยนและจัดการสถานะ ตัวแทนผู้ช่วยจะสร้างโค้ด Python เพื่อทำงานให้เสร็จสิ้น

นี่คือตัวอย่างของกระบวนการ:

![AutoGen](../../../translated_images/autogen.8ac57409019150ec5a17c6381a92863116b19acce02604b4bf5681225dee62eb.th.png)

#### LLM ถูกกำหนดด้วยข้อความระบบ

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

ข้อความระบบนี้บอก LLM เฉพาะว่าฟังก์ชันใดที่เกี่ยวข้องกับงานของมัน จำไว้ว่า ด้วย AutoGen คุณสามารถมี AssistantAgents ที่กำหนดหลายตัวพร้อมข้อความระบบที่แตกต่างกัน

#### การสนทนาเริ่มต้นโดยผู้ใช้

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

ข้อความนี้จาก user_proxy (มนุษย์) เป็นสิ่งที่จะเริ่มกระบวนการของ Agent เพื่อสำรวจฟังก์ชันที่ควรดำเนินการ

#### ฟังก์ชันถูกดำเนินการ

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

เมื่อการสนทนาเริ่มต้นถูกประมวลผล Agent จะส่งเครื่องมือที่แนะนำให้เรียกใช้ ในกรณีนี้คือฟังก์ชันที่เรียกว่า `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins` สิ่งนี้สามารถเป็นคลาส Python หรืออินเตอร์พรีเตอร์โค้ดทั่วไปได้ Plugins เหล่านี้ถูกเก็บเป็น embeddings เพื่อให้ LLM สามารถค้นหา plugin ที่ถูกต้องได้ดีขึ้น

![Taskweaver](../../../translated_images/taskweaver.c0997002a3df51572f6cad019c41202b7c2110cbfcccc4af2e5d6a0ace4b4545.th.png)

นี่คือตัวอย่างของ plugin ที่จัดการการตรวจจับความผิดปกติ:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

โค้ดถูกตรวจสอบก่อนดำเนินการ อีกคุณสมบัติหนึ่งในการจัดการบริบทใน Taskweaver คือ `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` ของการสนทนาและ `tools` คือโมเดล AI อื่น ๆ แต่ละโมเดล AI เป็นโมเดลเฉพาะที่ทำงานบางอย่างเช่นการตรวจจับวัตถุ การถอดเสียง หรือการบรรยายภาพ

![JARVIS](../../../translated_images/jarvis.d41d7c4c81bf015bd7ced7f1108abdec56b312472aaf3f63b5b0e82a5f4fb395.th.png)

LLM ซึ่งเป็นโมเดลทั่วไป รับคำขอจากผู้ใช้และระบุงานเฉพาะและอาร์กิวเมนต์/ข้อมูลที่จำเป็นในการทำงานให้เสร็จ

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

จากนั้น LLM จะจัดรูปแบบคำขอในลักษณะที่โมเดล AI เฉพาะสามารถตีความได้ เช่น JSON เมื่อโมเดล AI ได้ส่งคืนการทำนายตามงาน LLM จะได้รับการตอบกลับ

หากจำเป็นต้องใช้โมเดลหลายตัวเพื่อทำงานให้เสร็จสิ้น มันจะตีความการตอบกลับจากโมเดลเหล่านั้นก่อนที่จะนำมารวมกันเพื่อสร้างการตอบกลับให้ผู้ใช้

ตัวอย่างด้านล่างแสดงให้เห็นว่าสิ่งนี้จะทำงานอย่างไรเมื่อผู้ใช้ขอคำอธิบายและการนับวัตถุในภาพ:

## งานที่มอบหมาย

เพื่อดำเนินการเรียนรู้ของคุณเกี่ยวกับ AI Agents คุณสามารถสร้างด้วย AutoGen:

- แอปพลิเคชันที่จำลองการประชุมธุรกิจกับแผนกต่าง ๆ ของสตาร์ทอัพด้านการศึกษา
- สร้างข้อความระบบที่แนะนำ LLMs ในการทำความเข้าใจบุคคลและลำดับความสำคัญต่าง ๆ และให้ผู้ใช้เสนอไอเดียผลิตภัณฑ์ใหม่
- จากนั้น LLM ควรสร้างคำถามติดตามผลจากแต่ละแผนกเพื่อปรับปรุงและพัฒนาไอเดียผลิตภัณฑ์

## การเรียนรู้ไม่หยุดเพียงแค่นี้ ดำเนินการต่อไป

หลังจากเรียนจบบทเรียนนี้ ตรวจสอบ [คอลเลกชันการเรียนรู้ Generative AI ของเรา](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อเพิ่มพูนความรู้ของคุณใน Generative AI!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาที่เป็นต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้