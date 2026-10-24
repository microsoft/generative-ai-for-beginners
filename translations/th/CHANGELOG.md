# บันทึกการเปลี่ยนแปลง

การเปลี่ยนแปลงที่สำคัญทั้งหมดในหลักสูตรปัญญาประดิษฐ์เชิงสร้างสรรค์สำหรับผู้เริ่มต้นถูกบันทึกไว้ในไฟล์นี้

รูปแบบนี้อ้างอิงจาก [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) เนื่องจากนี่คือหลักสูตรการเรียนรู้ไม่ใช่ซอฟต์แวร์ที่มีเวอร์ชัน รายการจึงถูกจัดกลุ่มตามวันที่


## [2026-07-16] — การตรวจสอบเนื้อหา + สื่อภาพสำหรับบทที่ 09

### เปลี่ยนแปลง

- **บทที่ 10 (แอป AI แบบโค้ดต่ำ):** อัปเดตสองลิงก์ `docs.microsoft.com/powerapps/...` Dataverse ที่เลิกใช้
  ไปยัง `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` ปัจจุบัน
  (ตรวจสอบแล้วว่าทำงานได้จริง).
- **บทที่ 17 (เอเจนต์ AI):** ปรับตัวอย่างโมเดลที่ล้าสมัยให้ทันสมัย (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) และชื่อการปรับใช้แบบตัวอย่างในเฟรมเวิร์กเอเจนต์
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **ราก `README.md`:** เพิ่มรหัสติดตาม `?WT.mc_id=academic-105485-koreyst` ที่ขาดไปในลิงก์
  *Microsoft for Startups*.
- **ทรัพยากรภาพบทที่ 09** สร้างใหม่ด้วยโมเดล `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, และ
  `images/startup.png` (ตัวอย่างการแก้ไขคู่ก่อน/หลังถูกสร้างผ่านการเรียก `client.images.edit`
  จริง พร้อมหน้ากากที่สร้างขึ้น).

### ได้รับการยืนยันแล้ว

- ตรวจสอบ README สำหรับบทที่ 01, 03, 05, 12, 14, และ 16 — ทั้งหมดเป็นปัจจุบัน (ชื่อและลิงก์ Microsoft Foundry ที่ถูกต้อง); ไม่มีความจำเป็นต้องเปลี่ยนแปลง

- รันการตรวจสอบ markdown แบบเต็มบนไฟล์ markdown ทั้ง 41 ในที่เก็บ (ไม่รวมการแปล) สำหรับ
  เส้นทางเอกสารที่เลิกใช้, `/en-us/` โลเคิล Microsoft, ชื่อผลิตภัณฑ์/โมเดลที่ล้าสมัย, รหัสติดตามที่ขาดหาย,
  และลิงก์/ภาพสัมพัทธ์ที่เสีย; พบช่องว่างของรหัสติดตาม *Microsoft for Startups* เพียงรายการเดียวที่ต้องแก้ไข;
  ธงอื่นทั้งหมดยืนยันว่าเป็นผลบวกเท็จ (ลิงก์แปลที่สร้างอัตโนมัติ,
  ตัวแทนที่ถูกคอมเมนต์ และ URL โครงสร้างของ `/en/` จากบุคคลที่สาม).

## [2026-07-15] — บทที่ 09 (แอปพลิเคชันภาพ) เขียนใหม่สำหรับโมเดลภาพ GPT

### มีการเปลี่ยนแปลง

- **เขียนใหม่บทที่ 09 "การสร้างแอปพลิเคชันสร้างภาพ"** รอบครอบครัวโมเดล **`gpt-image`** ปัจจุบัน
  (ค่าเริ่มต้น **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` ก็เปิดตัวทั่วไปด้วย) แทนเนื้อหาเก่าของ DALL·E 2/3. การแก้ไขสำคัญ:
  เนื้อหา DALL·E 2/3 รุ่นเก่า การแก้ไขหลัก:
  - `gpt-image` โมเดลส่งคืนภาพเป็น **base64 (`b64_json`)** ไม่ใช่ URL อัปเดตตัวอย่างทั้งหมดให้
    `base64.b64decode(...)` แทนการดาวน์โหลด `url` ด้วย `requests`
  - ปรับเวอร์ชัน API ของภาพเป็น `2025-04-01-preview`
  - แทนที่ส่วน "temperature" ที่แต่งขึ้น (โมเดลภาพไม่รับ `temperature`) และเนื้อหา
    **variations** ของ DALL·E-2 เท่านั้น ด้วยส่วน **image editing** (mask/inpainting)
  - อัปเดต `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ทั้งสอง
    สมุดงานมอบหมาย (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) และสมุดงาน .NET `.dib`

### ถูกลบออก

- ลบตัวอย่าง `python/aoai-app-variation.py` และ `python/oai-app-variation.py` ที่ล้าสมัย
  (`images.create_variation` คือเฉพาะ DALL·E-2 และไม่ได้รับการสนับสนุนโดย `gpt-image`)
- ลบไฟล์ภาพเดี่ยว 4 รายการที่ไม่ได้ใช้งานผูกกับส่วนเปรียบเทียบอุณหภูมิที่ถูกลบออก
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`)
- ยกเลิกการพึ่งพา `requests` ที่ไม่จำเป็นจากตัวอย่าง Python และความต้องการในบทเรียน

### ได้รับการตรวจสอบ

- รัน `aoai-app.py` แบบ end-to-end กับโมเดล `gpt-image-1.5` ที่ปรับใช้และยืนยันว่า
  ขั้นตอนถอดรหัส/บันทึก base64 ผลลัพธ์เป็น PNG สมุดงานถูกยืนยันว่าเป็น JSON ที่ถูกต้อง

## [2026-07-14] — อัปเดตโมเดลเริ่มต้น + การแนะนำโมเดลเหตุผล

### การเปลี่ยนแปลง

- **โมเดลแชทเริ่มต้น `gpt-4o-mini` → `gpt-5-mini`** ทั่วตัวอย่างที่สามารถรันได้ในหลักสูตร,
  เอกสาร และการตั้งค่า ซึ่งได้รับการขับเคลื่อนโดยสถานะวงจรชีวิตของโมเดล: บน Microsoft Foundry,
  `gpt-4o-mini` (จะหยุดใช้งานวันที่ 2026-10-01) และครอบครัว `gpt-4.1` ทั้งหมด (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, จะหยุดใช้งานวันที่ 2026-10-14) กำลัง **ถูกยกเลิก**, ในขณะที่ **ครอบครัว GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) พร้อมใช้งานทั่วไป** (จะหยุดใช้งานวันที่ 2027-02-06) อัปเดต:
  - `.env.copy`, `00-course-setup/03-providers.md` (คำแนะนำการปรับใช้และคำสั่ง `az cognitiveservices`
    การปรับใช้), และไฟล์ README สำหรับบทเรียนที่ 04, 06, 07, และ 15
  - ตัวอย่าง Python ในบทเรียน 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) และสคริปต์บทเรียน 08
  - ตัวอย่าง TypeScript / JavaScript ในบทเรียน 06, 07, และ 11 และสมุดบันทึก `.dib` .NET สำหรับ
    บทเรียน 06 และ 07
  - สมุดบันทึกงานมอบหมายในบทเรียน 04, 06, 07, และ 11 (โค้ดเซลล์) รวมถึงตัวอย่าง `shared/python/api_utils.py`
    docstring
- **คำแนะนำพารามิเตอร์ของโมเดลสำหรับการให้เหตุผล (ใหม่).** `gpt-5-mini` เป็นโมเดล *การให้เหตุผล*: มัน **ไม่**
  รองรับ `temperature`/`top_p`, และใช้ `max_completion_tokens` (แชทคอมพลีชัน) /
  `max_output_tokens` (API ตอบกลับ) แทน `max_tokens` ดังนั้น:
  - ลบ `temperature`/`top_p`/`max_tokens` ออกจากตัวอย่างที่ตอนนี้ตั้งค่าเป็นค่าเริ่มต้นเป็น `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README RAG บทเรียน 15)
  - เพิ่มหมายเหตุ **"โมเดลการให้เหตุผลไม่ใช้ `temperature`"** ในบทเรียน 06 อธิบายว่า
    โมเดลการให้เหตุผลถูกควบคุมด้วย **การประดิษฐ์คำถามต่างๆ + การควบคุมการให้เหตุผล** แทน
    การปรับระดับสุ่ม (sampling knobs) ขณะที่ `temperature`/`top_p` ยังคงใช้ได้กับโมเดลที่ไม่ใช่การให้เหตุผล
    (GPT-4.x, Mistral, Llama, Phi, โมเดลเปิด)
- **`gpt-5-mini` ไม่ได้ใช้ในบทเรียนการปรับแต่งขั้นสูง (บทเรียน 18).** GPT-5 รองรับเฉพาะ
  การปรับแต่งแบบเร่งรัด (RFT); การสอนปรับแต่งแบบมีผู้สอน (SFT) ในบทเรียน 18 ยังคงใช้
  `gpt-4.1-mini` ซึ่งสนับสนุน SFT/DPO
- **เดโมอุณหภูมิใช้โมเดล Llama.** เพื่อให้สามารถสอน `temperature` (ซึ่งโมเดลการให้เหตุผล
  ปฏิเสธ), จึงใช้โมเดล `Llama-3.3-70B-Instruct` ผ่านทาง Foundry Models endpoint มีการเพิ่มตัวแปรใหม่
  `AZURE_INFERENCE_CHAT_MODEL` ใน `.env.copy`; สมุดบันทึก `githubmodels` สำหรับบทเรียน 04/06 และ
  ตัวอย่าง `06` `js-githubmodels` อ่านมัน (fallback ไปยัง `Llama-3.3-70B-Instruct`) และเก็บไว้
  ตัวอย่าง `temperature`/`top_p`/`max_tokens`
- **ตัวอย่าง JS / .NET อัปเดตสำหรับ GPT-5.** ลบ `temperature`/`top_p`/`max_tokens` ออกจากตัวอย่าง GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ซึ่งยังเพิ่ม `MaxOutputTokenCount`
  เพื่อไม่ให้ผลลัพธ์การวางเหตุผลถูกตัดทอน). ตัวอย่าง `06` `js-githubmodels` ใช้ Llama เพื่อเก็บ
  ตัวอย่างอุณหภูมิของมัน. ตัวอย่าง `.dib` ชี้ว่า `Azure.AI.Inference` + โมเดล Llama คือวิธีการ
  ในการสาธิต `Temperature` ใน .NET.
- ทิ้ง `gpt-4o-mini` / `gpt-5-mini` ไว้ในตำแหน่งที่ยังคงถูกต้อง: อ้างอิงโทเค็นเข้ารหัส `tiktoken`,
  รายการความพร้อมใช้งานโมเดลในแคตตาล็อก และโมเดลคำพูดบทเรียน 02 (`gpt-4o-transcribe`).
- ตัวอย่างบทเรียน 20 (Mistral) และ 21 (Meta) ยังคงใช้ `temperature`/`max_tokens` เพราะพวกเขากำหนดเป้าหมาย
  โมเดล Mistral/Llama ที่รองรับพารามิเตอร์เหล่านั้น.

## [2026-07-06] — การรีเฟรชปรับปรุงเนื้อหาให้ทันสมัย

การรีเฟรชอย่างกว้างเพื่อให้หลักสูตรถูกต้องสำหรับปี 2026: API สมัยใหม่, ชื่อผลิตภัณฑ์ปัจจุบันและ
ชื่อโมเดล, คำแนะนำผู้ให้บริการที่อัปเดต, และเครื่องมือประสบการณ์นักพัฒนารูปแบบใหม่.

### สิ่งที่เพิ่มเข้ามา

- ส่วน **Microsoft Agent Framework** ในบทเรียน `17-ai-agents` ครอบคลุมตัวแทนแชทเดี่ยว,
  เครื่องมือ/การเรียกใช้งานฟังก์ชัน, การตั้งค่า Azure OpenAI (Microsoft Foundry), และการจัดสรรเวิร์กโฟลว์ตัวแทนหลายคน
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** ถูกบันทึกเป็นผู้ให้บริการแบบออฟไลน์ / บนอุปกรณ์ (คู่กับ Ollama) ใน
  `00-course-setup/03-providers.md` และบทเรียน `19-slm`.
- **เวิร์กโฟลว์การบูรณาการอย่างต่อเนื่อง**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (บังคับใช้ในโมดูล `shared/` ที่ดูแลรักษา,
    คำแนะนำทั่วทั้งหลักสูตร), การผ่าน ESLint ที่แนะนำ และงาน pytest.
  - `.github/workflows/security.yml` — การวิเคราะห์ CodeQL (Python + JavaScript/TypeScript) และ
    การตรวจสอบ dependencies ในการร้องขอ pull.
- **ชุดทดสอบ** ภายใต้ `tests/` — 41 การทดสอบ pytest ที่ครอบคลุมโมดูลยูทิลิตี้ที่ใช้ร่วมกัน.
- **ทักษะการย้าย Azure OpenAI → Responses API** ภายใต้
  `.github/skills/azure-openai-to-responses/` ใช้เพื่อแนะนำการย้าย API.

### สิ่งที่เปลี่ยนแปลง

- **Chat Completions API → Responses API** ในตัวอย่างแชท Python และ TypeScript ทั้งหมด
  (`client.responses.create(...)` → `response.output_text`), รวมถึงบทเรียน 04, 06, 07, 11,
  15 และ 18 รวมถึง README ของพวกเขา
- **GitHub Models → Microsoft Foundry Models** ตลอดทั้งเนื้อหา ลิงก์ และตัวอย่าง GitHub Models
  จะเลิกใช้ในสิ้นเดือนกรกฎาคม 2026; ตัวอย่างปัจจุบันชี้ไปที่แคตตาล็อกโมเดล Microsoft Foundry และใช้
  ตัวแปรสภาพแวดล้อม `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`
- **`.env.copy`, `AGENTS.md`, และเอกสารผู้ให้บริการ** ได้รับการอัปเดตเพื่อสะท้อนว่า Azure OpenAI ตอนนี้เป็นส่วนหนึ่ง
  ของ Microsoft Foundry และเวอร์ชัน API เริ่มต้นถูกปรับเป็น `2024-10-21`.
- **ตัวอย่าง TypeScript** (บทเรียน 06, 07, 08, 11) ย้ายจาก SDK เบต้า `@azure/openai` ที่เลิกใช้
  ไปยังแพ็คเกจ `openai` (แอปแชทใช้ Responses API; แอปค้นหาใช้
  ตัวลูกค้า embeddings).
- **โน้ตบุ๊ก .NET** (`dotnet/*.dib`) มาตรฐานใน `Azure.AI.OpenAI` **2.1.0**: บทเรียน 06 และ 07
  ใช้ API `ChatClient`, บทเรียน 08 ใช้ `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), และ
  บทเรียน 09 ใช้ `ImageClient` (`GenerateImage`) กับ `gpt-image-1` แทนที่
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` แบบเก่าจาก `1.0.0-beta.9`
- **การปรับปรุงชื่อผลิตภัณฑ์**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (บทเรียน 14, 16, 17) และ "Bing" → **Microsoft Copilot** (บทเรียน 12) ซึ่งทั้งหมดนี้หมายถึง
  สินค้าปัจจุบัน
- **DevContainer** (`.devcontainer/`) ตอนนี้มีส่วนขยาย Pylance, Black, Ruff, ESLint, Prettier และ Copilot
  เปิดใช้งานการจัดรูปแบบอัตโนมัติเมื่อบันทึก และติดตั้ง `ruff`, `black`, `mypy` และ `pytest` เพื่อให้การตรวจสอบ CI
  สามารถทำซ้ำได้ในเครื่อง
- **การสร้างภาพ** (บทเรียน 09) แนะนำให้ใช้ `gpt-image-1` สำหรับ Azure (แคตตาล็อก Azure ได้ยกเลิก
  `dall-e-3` แล้ว)
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** อัปเดตเพื่อสะท้อนงานที่เสร็จสมบูรณ์แล้ว (การย้าย API, CI,
  DevContainer, การทดสอบ) และข้อเท็จจริงปัจจุบัน (คำแปลถูกสร้างขึ้นโดยอัตโนมัติโดย
  Azure Co-op Translator; API ผู้ช่วยถูกแทนที่ด้วย Responses API).

### แก้ไขแล้ว

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ตอนนี้ส่งคืน
  สตริงว่างสำหรับข้อมูลนำเข้าเฉพาะช่องว่างแทนที่จะเกิดข้อผิดพลาด "สั้นเกินไป" (สอดคล้องกับกรณี
  `None`) พบและครอบคลุมโดยชุดการทดสอบใหม่
- **ตัวอย่างภาพบทเรียน 09** — แก้ไขข้อผิดพลาดจริง: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  และตัวแปรที่บังโมดูล `openai`
- **สมุดบันทึก Lesson 15 RAG** — ซ่อมแซมการตั้งค่าลูกค้า, แทนที่ `DataFrame.append` ที่ถูกลบ
  ด้วย `pd.concat` และทันสมัยการใช้ SDK แบบเก่า
- ชื่อโมเดลที่เลิกใช้ / เลิกใช้งาน (`gpt-3.5-turbo`, `gpt-35-turbo`) ถูกแทนที่ด้วย `gpt-4o-mini`
  ในตัวอย่างใช้งานที่ใช้งานอยู่; ผลลัพธ์การปรับแต่งละเอียดในบทเรียน 18 ถูกเก็บรักษาและอธิบาย
  แทนที่จะเขียนใหม่

### เลิกใช้ / หมายเหตุ

- **ตัวอย่างโมเดล Microsoft Foundry** ที่ใช้ `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ตัวอย่างและบทเรียน `githubmodels-*` และ `js-githubmodels` และบทเรียน 19, 20,
  และ 21 — ยังคงใช้ Model Inference API ซึ่ง **ไม่** รองรับ Responses API เหล่านี้ถูก
  ทิ้งไว้อย่างจงใจบน SDK นั้น
- `AzureOpenAI()` ยังคงเก็บไว้เมื่อยังเหมาะสม (embeddings และการสร้างภาพ),
  เนื่องจากเวิร์กโฟลว์เหล่านั้นไม่ใช่ส่วนหนึ่งของการย้าย Responses API
- `text-embedding-ada-002` อ้างอิงยังคงเก็บไว้เนื่องจากดัชนี embedding ที่คำนวณล่วงหน้าขึ้นอยู่กับมัน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->