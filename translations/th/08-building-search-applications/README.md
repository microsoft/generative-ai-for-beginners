<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T18:34:27+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "th"
}
-->
# การสร้างแอปพลิเคชันค้นหา

[![แนะนำ AI เชิงสร้างสรรค์และโมเดลภาษาขนาดใหญ่](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.th.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้_

LLMs ไม่ได้มีแค่แชทบอทและการสร้างข้อความเท่านั้น แต่ยังสามารถสร้างแอปพลิเคชันค้นหาโดยใช้ Embeddings ได้อีกด้วย Embeddings คือการแสดงข้อมูลในรูปแบบตัวเลขที่เรียกว่าวิทยุเวกเตอร์ และสามารถใช้สำหรับการค้นหาเชิงความหมายของข้อมูลได้

ในบทเรียนนี้ คุณจะได้สร้างแอปพลิเคชันค้นหาสำหรับสตาร์ทอัพด้านการศึกษาของเรา สตาร์ทอัพของเราเป็นองค์กรไม่แสวงหาผลกำไรที่ให้การศึกษาฟรีแก่เด็กนักเรียนในประเทศกำลังพัฒนา สตาร์ทอัพของเรามีวิดีโอ YouTube จำนวนมากที่นักเรียนสามารถใช้เรียนรู้เกี่ยวกับ AI สตาร์ทอัพของเราต้องการสร้างแอปพลิเคชันค้นหาที่ช่วยให้นักเรียนสามารถค้นหาวิดีโอ YouTube ได้โดยการพิมพ์คำถาม

ตัวอย่างเช่น นักเรียนอาจพิมพ์ว่า 'Jupyter Notebooks คืออะไร?' หรือ 'Azure ML คืออะไร?' และแอปพลิเคชันค้นหาจะคืนรายการวิดีโอ YouTube ที่เกี่ยวข้องกับคำถามนั้น และที่ดียิ่งกว่านั้น แอปพลิเคชันค้นหาจะคืนลิงก์ไปยังจุดในวิดีโอที่มีคำตอบสำหรับคำถามนั้น

## บทนำ

ในบทเรียนนี้ เราจะครอบคลุม:

- การค้นหาเชิงความหมาย vs การค้นหาด้วยคำสำคัญ
- Text Embeddings คืออะไร
- การสร้างดัชนี Text Embeddings
- การค้นหาดัชนี Text Embeddings

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะสามารถ:

- แยกแยะความแตกต่างระหว่างการค้นหาเชิงความหมายและการค้นหาด้วยคำสำคัญ
- อธิบายว่า Text Embeddings คืออะไร
- สร้างแอปพลิเคชันโดยใช้ Embeddings เพื่อค้นหาข้อมูล

## ทำไมต้องสร้างแอปพลิเคชันค้นหา?

การสร้างแอปพลิเคชันค้นหาจะช่วยให้คุณเข้าใจวิธีการใช้ Embeddings ในการค้นหาข้อมูล คุณยังจะได้เรียนรู้วิธีการสร้างแอปพลิเคชันค้นหาที่นักเรียนสามารถใช้เพื่อค้นหาข้อมูลได้อย่างรวดเร็ว

บทเรียนนี้รวมถึง Embedding Index ของการถอดเสียงวิดีโอ YouTube จากช่อง [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) ของ Microsoft ช่อง AI Show เป็นช่อง YouTube ที่สอนเกี่ยวกับ AI และการเรียนรู้ของเครื่อง Embedding Index มี Embeddings สำหรับการถอดเสียงวิดีโอ YouTube จนถึงเดือนตุลาคม 2023 คุณจะใช้ Embedding Index เพื่อสร้างแอปพลิเคชันค้นหาสำหรับสตาร์ทอัพของเรา แอปพลิเคชันค้นหาจะคืนลิงก์ไปยังจุดในวิดีโอที่มีคำตอบสำหรับคำถาม นี่เป็นวิธีที่ยอดเยี่ยมสำหรับนักเรียนในการค้นหาข้อมูลที่ต้องการได้อย่างรวดเร็ว

ตัวอย่างต่อไปนี้เป็นการค้นหาเชิงความหมายสำหรับคำถาม 'สามารถใช้ rstudio กับ azure ml ได้หรือไม่?' ลองดูที่ URL ของ YouTube คุณจะเห็นว่า URL มี timestamp ที่นำคุณไปยังจุดในวิดีโอที่มีคำตอบสำหรับคำถามนั้น

![การค้นหาเชิงความหมายสำหรับคำถาม "สามารถใช้ rstudio กับ Azure ML ได้หรือไม่"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.th.png)

## การค้นหาเชิงความหมายคืออะไร?

คุณอาจสงสัยว่า การค้นหาเชิงความหมายคืออะไร? การค้นหาเชิงความหมายเป็นเทคนิคการค้นหาที่ใช้ความหมายของคำในคำค้นหาเพื่อคืนผลลัพธ์ที่เกี่ยวข้อง

นี่คือตัวอย่างของการค้นหาเชิงความหมาย สมมติว่าคุณกำลังมองหาซื้อรถ คุณอาจค้นหาว่า 'รถในฝันของฉัน' การค้นหาเชิงความหมายเข้าใจว่าคุณไม่ได้ `ฝัน` เกี่ยวกับรถ แต่คุณกำลังมองหาซื้อรถที่ `เหมาะสมที่สุด` การค้นหาเชิงความหมายเข้าใจเจตนาของคุณและคืนผลลัพธ์ที่เกี่ยวข้อง ทางเลือกคือ `การค้นหาด้วยคำสำคัญ` ซึ่งจะค้นหาความฝันเกี่ยวกับรถและมักจะคืนผลลัพธ์ที่ไม่เกี่ยวข้อง

## Text Embeddings คืออะไร?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) เป็นเทคนิคการแสดงข้อความที่ใช้ใน [การประมวลผลภาษาธรรมชาติ](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst) Text embeddings เป็นการแสดงข้อความในรูปแบบตัวเลขเชิงความหมาย Embeddings ใช้เพื่อแสดงข้อมูลในรูปแบบที่เครื่องสามารถเข้าใจได้ง่าย มีโมเดลมากมายสำหรับการสร้าง text embeddings ในบทเรียนนี้ เราจะเน้นการสร้าง embeddings โดยใช้ OpenAI Embedding Model

นี่คือตัวอย่าง ลองจินตนาการว่าข้อความต่อไปนี้อยู่ในการถอดเสียงจากหนึ่งในตอนของช่อง AI Show บน YouTube:

```text
Today we are going to learn about Azure Machine Learning.
```

เราจะส่งข้อความไปยัง OpenAI Embedding API และมันจะคืน embedding ที่ประกอบด้วยตัวเลข 1536 ตัว หรือที่เรียกว่าเวกเตอร์ แต่ละตัวเลขในเวกเตอร์แสดงถึงแง่มุมต่างๆ ของข้อความ เพื่อความกระชับ นี่คือตัวเลข 10 ตัวแรกในเวกเตอร์

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Embedding Index ถูกสร้างขึ้นอย่างไร?

Embedding Index สำหรับบทเรียนนี้ถูกสร้างขึ้นด้วยชุดของสคริปต์ Python คุณจะพบสคริปต์พร้อมคำแนะนำใน [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) ในโฟลเดอร์ 'scripts' สำหรับบทเรียนนี้ คุณไม่จำเป็นต้องรันสคริปต์เหล่านี้เพื่อจบบทเรียนนี้ เนื่องจาก Embedding Index ถูกเตรียมไว้ให้คุณแล้ว

สคริปต์ทำงานดังนี้:

1. การดาวน์โหลดการถอดเสียงสำหรับวิดีโอ YouTube แต่ละรายการในเพลย์ลิสต์ [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1)
2. ใช้ [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) เพื่อพยายามดึงชื่อผู้พูดจาก 3 นาทีแรกของการถอดเสียงวิดีโอ YouTube ชื่อผู้พูดสำหรับแต่ละวิดีโอจะถูกเก็บไว้ใน Embedding Index ชื่อ `embedding_index_3m.json`
3. ข้อความการถอดเสียงจะถูกแบ่งเป็น **ส่วนข้อความ 3 นาที** แต่ละส่วนมีคำประมาณ 20 คำที่ซ้อนทับจากส่วนถัดไปเพื่อให้แน่ใจว่า Embedding สำหรับส่วนข้อความจะไม่ถูกตัดออกและเพื่อให้บริบทการค้นหาดีขึ้น
4. ข้อความในแต่ละส่วนจะถูกส่งไปยัง OpenAI Chat API เพื่อสรุปข้อความให้เหลือ 60 คำ สรุปนี้จะถูกเก็บไว้ใน Embedding Index `embedding_index_3m.json`
5. สุดท้าย ข้อความในแต่ละส่วนจะถูกส่งไปยัง OpenAI Embedding API Embedding API จะคืนเวกเตอร์ที่มีตัวเลข 1536 ตัวที่แสดงถึงความหมายเชิงความหมายของส่วนข้อความนั้น ส่วนข้อความพร้อมกับเวกเตอร์ OpenAI Embedding จะถูกเก็บไว้ใน Embedding Index `embedding_index_3m.json`

### ฐานข้อมูลเวกเตอร์

เพื่อความง่ายในบทเรียนนี้ Embedding Index จะถูกเก็บไว้ในไฟล์ JSON ชื่อ `embedding_index_3m.json` และโหลดเข้าสู่ Pandas DataFrame อย่างไรก็ตาม ในการใช้งานจริง Embedding Index จะถูกเก็บไว้ในฐานข้อมูลเวกเตอร์ เช่น [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst) เป็นต้น

## การทำความเข้าใจความคล้ายคลึงกันของโคไซน์

เราได้เรียนรู้เกี่ยวกับ text embeddings ขั้นตอนต่อไปคือการเรียนรู้วิธีการใช้ text embeddings เพื่อค้นหาข้อมูล และโดยเฉพาะอย่างยิ่งการค้นหา embeddings ที่คล้ายกันที่สุดกับคำค้นหาที่กำหนดโดยใช้ความคล้ายคลึงกันของโคไซน์

### ความคล้ายคลึงกันของโคไซน์คืออะไร?

ความคล้ายคลึงกันของโคไซน์เป็นการวัดความคล้ายคลึงกันระหว่างเวกเตอร์สองตัว คุณอาจเคยได้ยินคำนี้ในชื่อ `การค้นหาเพื่อนบ้านที่ใกล้ที่สุด` เพื่อทำการค้นหาความคล้ายคลึงกันของโคไซน์ คุณต้อง _แปลงเป็นเวกเตอร์_ สำหรับข้อความ _query_ โดยใช้ OpenAI Embedding API จากนั้นคำนวณ _cosine similarity_ ระหว่างเวกเตอร์ query และแต่ละเวกเตอร์ใน Embedding Index จำไว้ว่า Embedding Index มีเวกเตอร์สำหรับแต่ละส่วนข้อความการถอดเสียงวิดีโอ YouTube สุดท้าย จัดเรียงผลลัพธ์ตามความคล้ายคลึงกันของโคไซน์ และส่วนข้อความที่มีความคล้ายคลึงกันของโคไซน์สูงสุดจะเป็นข้อความที่คล้ายกับ query มากที่สุด

จากมุมมองทางคณิตศาสตร์ ความคล้ายคลึงกันของโคไซน์วัดมุมโคไซน์ระหว่างเวกเตอร์สองตัวที่ฉายในพื้นที่หลายมิติ การวัดนี้มีประโยชน์เพราะหากเอกสารสองฉบับอยู่ห่างกันมากในระยะทางยูคลิดเนื่องจากขนาด พวกมันยังสามารถมีมุมที่เล็กกว่าระหว่างกันและดังนั้นจึงมีความคล้ายคลึงกันของโคไซน์สูงขึ้น สำหรับข้อมูลเพิ่มเติมเกี่ยวกับสมการความคล้ายคลึงกันของโคไซน์ ดูที่ [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst)

## การสร้างแอปพลิเคชันค้นหาแรกของคุณ

ต่อไป เราจะเรียนรู้วิธีการสร้างแอปพลิเคชันค้นหาโดยใช้ Embeddings แอปพลิเคชันค้นหาจะช่วยให้นักเรียนสามารถค้นหาวิดีโอได้โดยการพิมพ์คำถาม แอปพลิเคชันค้นหาจะคืนรายการวิดีโอที่เกี่ยวข้องกับคำถาม แอปพลิเคชันค้นหายังจะคืนลิงก์ไปยังจุดในวิดีโอที่มีคำตอบสำหรับคำถามนั้น

โซลูชันนี้ถูกสร้างและทดสอบบน Windows 11, macOS และ Ubuntu 22.04 โดยใช้ Python 3.10 หรือใหม่กว่า คุณสามารถดาวน์โหลด Python ได้จาก [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)

## งาน - การสร้างแอปพลิเคชันค้นหา เพื่อช่วยนักเรียน

เราได้แนะนำสตาร์ทอัพของเราตั้งแต่ต้นบทเรียน ตอนนี้ถึงเวลาที่จะช่วยนักเรียนสร้างแอปพลิเคชันค้นหาสำหรับการประเมินผลของพวกเขา

ในงานนี้ คุณจะสร้าง Azure OpenAI Services ที่จะใช้ในการสร้างแอปพลิเคชันค้นหา คุณจะสร้าง Azure OpenAI Services ต่อไปนี้ คุณจะต้องมีการสมัครสมาชิก Azure เพื่อทำงานนี้ให้เสร็จสมบูรณ์

### เริ่มต้น Azure Cloud Shell

1. ลงชื่อเข้าใช้ [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)
2. เลือกไอคอน Cloud Shell ที่มุมขวาบนของ Azure portal
3. เลือก **Bash** สำหรับประเภทของสภาพแวดล้อม

#### สร้างกลุ่มทรัพยากร

> สำหรับคำแนะนำเหล่านี้ เราใช้กลุ่มทรัพยากรชื่อ "semantic-video-search" ใน East US
> คุณสามารถเปลี่ยนชื่อกลุ่มทรัพยากรได้ แต่เมื่อเปลี่ยนตำแหน่งสำหรับทรัพยากร
> ตรวจสอบ [ตารางความพร้อมใช้งานของโมเดล](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)

```shell
az group create --name semantic-video-search --location eastus
```

#### สร้างทรัพยากร Azure OpenAI Service

จาก Azure Cloud Shell ให้รันคำสั่งต่อไปนี้เพื่อสร้างทรัพยากร Azure OpenAI Service

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### รับ endpoint และ keys สำหรับการใช้งานในแอปพลิเคชันนี้

จาก Azure Cloud Shell ให้รันคำสั่งต่อไปนี้เพื่อรับ endpoint และ keys สำหรับทรัพยากร Azure OpenAI Service

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### ติดตั้งโมเดล OpenAI Embedding

จาก Azure Cloud Shell ให้รันคำสั่งต่อไปนี้เพื่อติดตั้งโมเดล OpenAI Embedding

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## โซลูชัน

เปิด [solution notebook](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) ใน GitHub Codespaces และทำตามคำแนะนำใน Jupyter Notebook

เมื่อคุณรัน notebook คุณจะได้รับการแจ้งให้ป้อน query กล่องป้อนข้อมูลจะมีลักษณะดังนี้:

![กล่องป้อนข้อมูลสำหรับผู้ใช้เพื่อป้อน query](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.th.png)

## ยอดเยี่ยม! เรียนรู้ต่อไป

หลังจากจบบทเรียนนี้ ลองดู [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อเพิ่มพูนความรู้เกี่ยวกับ Generative AI!

ไปที่บทเรียนที่ 9 ซึ่งเราจะดูวิธีการ [สร้างแอปพลิเคชันการสร้างภาพ](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้