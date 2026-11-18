# บันทึกการเปลี่ยนแปลง

การเปลี่ยนแปลงที่สำคัญทั้งหมดในหลักสูตร Generative AI for Beginners ได้ถูกบันทึกไว้ในไฟล์นี้

รูปแบบนี้อ้างอิงจาก [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) เนื่องจากนี่เป็นหลักสูตรการเรียนรู้แทนที่จะเป็นชุดซอฟต์แวร์ที่มีเวอร์ชัน รายการจึงถูกจัดกลุ่มตามวันที่


## [2026-07-16] — การตรวจสอบเนื้อหา + สินทรัพย์ภาพสำหรับบทเรียนที่ 09

### มีการเปลี่ยนแปลง

- **บทเรียนที่ 10 (แอป AI แบบ low-code):** อัปเดตสองลิงก์ `docs.microsoft.com/powerapps/...` Dataverse ที่เลิกใช้งานไปแล้ว
  เป็นลิงก์ `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` ปัจจุบัน
  (ตรวจสอบแล้วยังใช้งานได้จริง).
- **บทเรียนที่ 17 (ตัวแทน AI):** ปรับปรุงตัวอย่างโมเดลเก่า (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) และชื่อการปรับใช้ตัวอย่างใน Agent Framework ที่เป็นที่อยู่สำรอง
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** เพิ่ม ID การติดตาม `?WT.mc_id=academic-105485-koreyst` ที่ขาดหายไปในลิงก์
  *Microsoft for Startups*.
- **ภาพทรัพย์สินบทเรียนที่ 09** สร้างใหม่ด้วยโมเดล `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, และ
  `images/startup.png` (คู่ตัวอย่างก่อน/หลังการแก้ไขถูกสร้างขึ้นผ่านการเรียกใช้งานจริงของ
  `client.images.edit` ที่มีการสร้างหน้ากาก).

### ได้รับการตรวจสอบแล้ว

- ตรวจสอบ READMEs สำหรับบทเรียน 01, 03, 05, 12, 14 และ 16 — ทั้งหมดเป็นปัจจุบัน (การตั้งชื่อและลิงก์ Microsoft Foundry ที่ถูกต้อง);
  ไม่มีความจำเป็นต้องเปลี่ยนแปลงใด ๆ
- รันการตรวจสอบ markdown เต็มรูปแบบในไฟล์ markdown ทั้งหมด 41 ไฟล์ในที่เก็บ (ไม่รวมการแปล) สำหรับ
  เส้นทางเอกสารที่เลิกใช้, `/en-us/` ภาษา Microsoft, ชื่อผลิตภัณฑ์/รุ่นที่ล้าสมัย, ID การติดตามที่หายไป,
  และลิงก์/รูปภาพสัมพัทธ์ที่เสีย; ช่องว่าง ID การติดตาม *Microsoft for Startups* เพียงหนึ่งช่องเป็น
  ที่สามารถดำเนินการได้; ธงอื่น ๆ ทั้งหมดได้รับการยืนยันว่าเป็นผลบวกลวง (ลิงก์การแปลที่สร้างโดยอัตโนมัติ,
  ตัวแทนที่คอมเมนต์ออก และ URL โครงสร้างของ `/en/` จากภายนอก).

## [2026-07-15] — บทเรียน 09 (แอปพลิเคชันภาพ) เขียนใหม่สำหรับโมเดลภาพ GPT

### เปลี่ยนแปลง

- **เขียนใหม่บทเรียน 09 "การสร้างแอปพลิเคชันสร้างภาพ"** รอบตัวแบบ **`gpt-image`**
  ของครอบครัวโมเดลปัจจุบัน (ค่าเริ่มต้น **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` ก็ GA เช่นกัน), แทนที่
  เนื้อหา legacy DALL·E 2/3. การแก้ไขหลัก:
  - โมเดล `gpt-image` จะส่งคืนภาพในรูปแบบ **base64 (`b64_json`)** ไม่ใช่ URL อัปเดตตัวอย่างทั้งหมดเป็น
    `base64.b64decode(...)` แทนการดาวน์โหลด `url` ด้วย `requests`
  - อัปเดตเวอร์ชัน API ของภาพเป็น `2025-04-01-preview`
  - แทนที่ส่วน "temperature" ที่แต่งขึ้นมา (โมเดลภาพไม่ได้ใช้ `temperature`) และ
    เนื้อหา **ตัวแปร** รูปภาพเฉพาะของ DALL·E-2 พร้อมส่วน **แก้ไขรูปภาพ** (มาสก์/การระบายสีใหม่)
  - ปรับปรุง `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ทั้งสอง
    สมุดโน้ตงานมอบหมาย (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), และสมุดโน้ต .NET `.dib`

### ถูกลบ

- ลบตัวอย่าง `python/aoai-app-variation.py` และ `python/oai-app-variation.py` ที่ล้าสมัยแล้ว
  (`images.create_variation` เป็นเฉพาะ DALL·E-2 และไม่รองรับโดย `gpt-image`).
- ลบภาพแอสเซทที่ถูกทิ้ง 4 รายการซึ่งเกี่ยวข้องกับส่วนเปรียบเทียบอุณหภูมิที่ถูกลบออก
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- ตัดการพึ่งพา `requests` ที่ไม่จำเป็นออกจากตัวอย่าง Python และข้อกำหนดของบทเรียน

### ยืนยันแล้ว

- รัน `aoai-app.py` จากต้นทางถึงปลายทางกับโมเดล `gpt-image-1.5` ที่เผยแพร่และยืนยันว่า
  กระบวนการถอดรหัส/บันทึก base64 ผลิตเป็น PNG. โน้ตบุ๊กยืนยันว่าเป็น JSON ที่ถูกต้อง

## [2026-07-14] — การอัปเดตโมเดลเริ่มต้น + แนวทางโมเดลเหตุผล

### มีการเปลี่ยนแปลง

- **โมเดลแชทเริ่มต้น `gpt-4o-mini` → `gpt-5-mini`** ทั่วตัวอย่างที่รันได้ในหลักสูตร,
  เอกสาร และการกำหนดค่า ขับเคลื่อนโดยสถานะวงจรชีวิตโมเดล: บน Microsoft Foundry,
  `gpt-4o-mini` (เลิกใช้ 2026-10-01) และครอบครัว `gpt-4.1` ทั้งหมด (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, เลิกใช้ 2026-10-14) กำลัง **เลิกใช้งาน**, ในขณะที่ครอบครัว **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) พร้อมใช้งานทั่วไป** (เลิกใช้ 2027-02-06) ได้รับการอัปเดต:
  - `.env.copy`, `00-course-setup/03-providers.md` (คำสั่งการติดตั้งที่แนะนำและ `az cognitiveservices`
    คำสั่ง deploy), และ README สำหรับบทเรียนที่ 04, 06, 07, และ 15
  - ตัวอย่าง Python ในบทเรียน 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) และสคริปต์บทเรียน 08
  - ตัวอย่าง TypeScript / JavaScript ในบทเรียน 06, 07, และ 11, และ `.dib` .NET notebooks สำหรับ
    บทเรียน 06 และ 07
  - โน้ตบุ๊คการบ้านในบทเรียน 04, 06, 07, และ 11 (เซลล์โค้ด), รวมทั้งตัวอย่าง docstring `shared/python/api_utils.py`

- **คำแนะนำเกี่ยวกับพารามิเตอร์โมเดลการให้เหตุผล (ใหม่).** `gpt-5-mini` เป็นโมเดล *การให้เหตุผล*: ซึ่ง **ไม่**
  รองรับ `temperature`/`top_p` และใช้ `max_completion_tokens` (การสนทนาเติมเต็ม) /
  `max_output_tokens` (Responses API) แทน `max_tokens` ดังนั้น:
  - เอา `temperature`/`top_p`/`max_tokens` ออกจากตัวอย่างที่ตอนนี้ใช้ค่าเริ่มต้นเป็น `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - เพิ่มหมายเหตุ **"โมเดลการให้เหตุผลไม่ใช้ `temperature`"** ในบทเรียนที่ 06 อธิบายว่า
    โมเดลการให้เหตุผลถูกควบคุมด้วย **การออกแบบคำสั่ง + การควบคุมการให้เหตุผล** แทนที่
    ปุ่มปรับการสุ่ม ในขณะที่ `temperature`/`top_p` ยังคงใช้ได้กับโมเดลที่ไม่ใช่โมเดลการให้เหตุผล
    (GPT-4.x, Mistral, Llama, Phi, โมเดลเปิด).
- **`gpt-5-mini` ไม่ได้ถูกใช้สำหรับบทเรียนการปรับแต่งขั้นสูง (บทที่ 18).** GPT-5 รองรับเฉพาะ
  การปรับแต่งขั้นสูงแบบเสริมแรง (RFT); การสอนเดินผ่านการปรับแต่งแบบควบคุม (SFT) ในบทที่ 18 ยังคงใช้
  `gpt-4.1-mini` ซึ่งรองรับ SFT/DPO.
- **เดโม่อุณหภูมิใช้โมเดล Llama** เพื่อรักษาการสอน `temperature` (ซึ่งโมเดลเหตุผล
  ปฏิเสธ) จะใช้โมเดล `Llama-3.3-70B-Instruct` ผ่านทาง Foundry Models endpoint มีการเพิ่มตัวแปร
  `AZURE_INFERENCE_CHAT_MODEL` ใหม่ใน `.env.copy`; โน้ตบุ๊คบทเรียน 04/06 `githubmodels` และ
  ตัวอย่าง `06` `js-githubmodels` อ่านมัน (ย้อนกลับไปที่ `Llama-3.3-70B-Instruct`) และเก็บรักษา
  ตัวอย่าง`temperature`/`top_p`/`max_tokens` demos ของพวกเขาไว้
- **ตัวอย่าง JS / .NET อัปเดตสำหรับ GPT-5.** เอา `temperature`/`top_p`/`max_tokens` ออกจาก GPT-5
  ตัวอย่าง (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ซึ่งยังเพิ่ม `MaxOutputTokenCount`
  เพื่อไม่ให้ผลลัพธ์การให้เหตุผลถูกตัดทอน). ตัวอย่าง `06` `js-githubmodels` ตอนนี้ใช้ Llama เพื่อเก็บ
  การสาธิตอุณหภูมิของมัน ตัวอย่าง `.dib` ระบุว่า `Azure.AI.Inference` + โมเดล Llama คือวิธีการ
  สาธิต `Temperature` ใน .NET
- ซ้าย `gpt-4o-mini` / `gpt-5-mini` ที่อยู่ในตำแหน่งที่พวกมันยังคงถูกต้อง: `tiktoken` การเข้ารหัสโทเค็น
  รายการอ้างอิง, รายการความพร้อมในการใช้งานโมเดลแคตตาล็อก, และโมเดลเสียงบทเรียนที่ 02 (`gpt-4o-transcribe`).
- ตัวอย่างบทเรียนที่ 20 (Mistral) และ 21 (Meta) ยังคงเก็บ `temperature`/`max_tokens` ไว้เพราะว่ามุ่งเป้าไปที่
  โมเดล Mistral/Llama ซึ่งรองรับพารามิเตอร์เหล่านั้น.

## [2026-07-06] — การปรับปรุงเนื้อหาให้ทันสมัย

การปรับปรุงครั้งใหญ่เพื่อตอบสนองหลักสูตรให้ถูกต้องสำหรับปี 2026: API ที่ทันสมัย, ชื่อผลิตภัณฑ์ปัจจุบันและ
ชื่อโมเดล, คำแนะนำของผู้ให้บริการที่ปรับปรุงแล้ว, และเครื่องมือประสบการณ์นักพัฒนารูปแบบใหม่.

### เพิ่มเติม

- **Microsoft Agent Framework** ส่วนในบทเรียน `17-ai-agents` ครอบคลุมตัวแทนแชทเดี่ยว,
  เครื่องมือ/การเรียกฟังก์ชัน, การกำหนดค่า Azure OpenAI (Microsoft Foundry) และการประสานงาน
  เวิร์กโฟลว์หลายตัวแทน (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** ได้รับการบันทึกเป็นผู้ให้บริการออฟไลน์ / บนอุปกรณ์ (ควบคู่กับ Ollama) ใน
  `00-course-setup/03-providers.md` และบทเรียน `19-slm`.
- **เวิร์กโฟลว์การผสานรวมอย่างต่อเนื่อง**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (บังคับใช้กับโมดูล `shared/` ที่ดูแลรักษา,
    คำแนะนำในส่วนที่เหลือของหลักสูตร), การผ่าน ESLint ที่เป็นคำแนะนำ และงาน pytest
  - `.github/workflows/security.yml` — การวิเคราะห์ CodeQL (Python + JavaScript/TypeScript) และ
    การตรวจสอบการพึ่งพาในคำร้องขอดึงเข้า (pull requests)
- **ชุดทดสอบ** ภายใต้ `tests/` — ทดสอบ pytest 41 รายการครอบคลุมโมดูลยูทิลิตี้ที่ใช้ร่วมกัน
- **ทักษะการย้าย Azure OpenAI → Responses API** ภายใต้
  `.github/skills/azure-openai-to-responses/` ใช้เพื่อแนะนำการย้าย API

### เปลี่ยนแปลง

- **Chat Completions API → Responses API** ในตัวอย่างการแชท Python และ TypeScript ทั้งหมด
  (`client.responses.create(...)` → `response.output_text`) รวมบทเรียน 04, 06, 07, 11,
  15, และ 18 รวมถึง README ของพวกเขา
- **GitHub Models → Microsoft Foundry Models** ตลอดทั้งข้อความ, ลิงก์ และตัวอย่าง GitHub Models
  จะเลิกใช้งานในปลายเดือนกรกฎาคม 2026; ตัวอย่างตอนนี้ชี้ไปที่แคตตาล็อกโมเดล Microsoft Foundry และใช้
  ตัวแปรสภาพแวดล้อม `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`
- **เอกสารของ `.env.copy`, `AGENTS.md`, และผู้ให้บริการ** ได้รับการอัปเดตเพื่อสะท้อนว่า Azure OpenAI ตอนนี้เป็นส่วนหนึ่ง
  ของ Microsoft Foundry และเวอร์ชัน API เริ่มต้นถูกเลื่อนขึ้นเป็น `2024-10-21`
- **ตัวอย่าง TypeScript** (บทเรียนที่ 06, 07, 08, 11) ที่ย้ายออกจาก `@azure/openai` ซึ่งเลิกใช้แล้ว
  SDK รุ่นเบต้าไปยังแพ็กเกจ `openai` (แอปแชทใช้ Responses API; แอปค้นหาใช้
  ลูกค้า embeddings).
- **.NET notebooks** (`dotnet/*.dib`) มาตรฐานบน `Azure.AI.OpenAI` **2.1.0**: บทเรียน 06 และ 07
  ใช้ `ChatClient` API, บทเรียน 08 ใช้ `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), และ
  บทเรียน 09 ใช้ `ImageClient` (`GenerateImage`) กับ `gpt-image-1` แทนที่
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` รุ่นเก่าจาก `1.0.0-beta.9`.
- **การปรับปรุงชื่อผลิตภัณฑ์**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (บทเรียน 14, 16, 17) และ "Bing" → **Microsoft Copilot** (บทเรียน 12) ซึ่งอ้างถึงผลิตภัณฑ์ปัจจุบัน
  ในปัจจุบัน
- **DevContainer** (`.devcontainer/`) ปัจจุบันมาพร้อมกับส่วนขยาย Pylance, Black, Ruff, ESLint, Prettier และ Copilot
  เปิดใช้งานการจัดรูปแบบเมื่อบันทึก และติดตั้ง `ruff`, `black`, `mypy` และ `pytest` เพื่อให้การตรวจสอบ CI
  สามารถทำซ้ำได้ในเครื่องท้องถิ่น
- **การสร้างภาพ** (บทเรียน 09) แนะนำ `gpt-image-1` สำหรับ Azure (แค็ตตาล็อก Azure ได้ถูกยกเลิก
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ได้รับการอัปเดตเพื่อสะท้อนงานที่เสร็จสมบูรณ์ (การย้าย API, CI,
  DevContainer, การทดสอบ) และข้อเท็จจริงปัจจุบัน (การแปลถูกสร้างขึ้นโดยอัตโนมัติโดย
  Azure Co-op Translator; API ผู้ช่วยถูกแทนที่ด้วย API การตอบสนอง)

### แก้ไขแล้ว

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ตอนนี้ส่งคืน
  สตริงว่างสำหรับอินพุตที่มีเฉพาะช่องว่างแทนที่จะเกิดข้อผิดพลาด "สั้นเกินไป" (สอดคล้องกับ
  กรณี `None`). พบและครอบคลุมโดยชุดทดสอบใหม่แล้ว
- **ตัวอย่างรูปภาพบทเรียน 09** — แก้ไขข้อผิดพลาดจริง: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  และตัวแปรที่ซ้อนทับโมดูล `openai`
- **สมุดบันทึก RAG บทเรียน 15** — ซ่อมแซมการตั้งค่าลูกค้า, แทนที่ `DataFrame.append` ที่ถูกลบด้วย
  `pd.concat` และปรับปรุงการใช้งาน SDK รุ่นเก่าให้ทันสมัย
- ชื่อโมเดลที่เลิกใช้ / เลิกใช้งานแล้ว (`gpt-3.5-turbo`, `gpt-35-turbo`) ถูกแทนที่ด้วย `gpt-4o-mini`
  ในตัวอย่างที่ใช้งานอยู่; ผลลัพธ์การปรับแต่งเฉพาะตัวในประวัติศาสตร์ของบทเรียน 18 ถูกเก็บไว้และทำหมายเหตุ
  แทนการเขียนใหม่

### เลิกใช้ / หมายเหตุ

- ตัวอย่าง **โมเดล Microsoft Foundry** ที่ใช้ `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ตัวอย่างและบทเรียน `githubmodels-*` และ `js-githubmodels` และบทเรียน 19, 20,
  และ 21 — ยังคงอยู่บน Model Inference API ซึ่ง **ไม่สนับสนุน** Responses API เหล่านี้
  ถูกทิ้งไว้ใน SDK นั้นโดยเจตนา
- `AzureOpenAI()` ยังคงถูกเก็บไว้หากยังเหมาะสม (embeddings และการสร้างภาพ),
  เพราะเวิร์กโฟลว์เหล่านั้นไม่ใช่ส่วนหนึ่งของการย้าย Responses API
- การอ้างอิง `text-embedding-ada-002` ยังคงเก็บไว้เมื่อมีการใช้ดรรชนี embedding ที่คำนวณไว้ล่วงหน้าอิงตามมัน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->