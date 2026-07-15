# แผนงานคุณสมบัติและการปรับปรุงขั้นสูง

เอกสารนี้สรุปข้อแนะนำสำหรับการปรับปรุงและการเสริมคุณสมบัติสำหรับหลักสูตร Generative AI for Beginners โดยอิงตามการตรวจสอบโค้ดอย่างละเอียดและการวิเคราะห์แนวปฏิบัติที่ดีที่สุดในวงการ

## บทสรุปผู้บริหาร

โค้ดเบสได้รับการวิเคราะห์ด้านความปลอดภัย คุณภาพโค้ด และประสิทธิผลทางการศึกษา เอกสารนี้นำเสนอคำแนะนำสำหรับการแก้ไขโดยทันที การปรับปรุงในระยะสั้น และการพัฒนาในอนาคต

---

## 1. การเสริมความปลอดภัย (ลำดับความสำคัญ: สำคัญมาก)

### 1.1 การแก้ไขโดยทันที (เสร็จสมบูรณ์)

| ปัญหา | ไฟล์ที่ได้รับผลกระทบ | สถานะ |
|-------|----------------|--------|
| SECRET_KEY ที่ฝังอยู่ในโค้ด | `05-advanced-prompts/python/aoai-solution.py` | แก้ไขแล้ว |
| ขาดการตรวจสอบ env | หลายไฟล์ JS/TS | แก้ไขแล้ว |
| การเรียกฟังก์ชันที่ไม่ปลอดภัย | `11-integrating-with-function-calling/js-githubmodels/app.js` | แก้ไขแล้ว |
| รั่วไหลของตัวจัดการไฟล์ | `08-building-search-applications/scripts/` | แก้ไขแล้ว |
| ขาดการตั้งเวลาหมดเวลาในการร้องขอ | `09-building-image-applications/python/` | แก้ไขแล้ว |

### 1.2 คุณสมบัติด้านความปลอดภัยเพิ่มเติมที่แนะนำ

1. **ตัวอย่างการจำกัดอัตรา (Rate Limiting)**
   - เพิ่มโค้ดตัวอย่างแสดงวิธีการใช้งานจำกัดอัตราสำหรับการเรียก API
   - แสดงรูปแบบ exponential backoff

2. **การหมุนเวียนคีย์ API**
   - เพิ่มเอกสารแนวปฏิบัติที่ดีที่สุดสำหรับการหมุนเวียนคีย์ API
   - รวมตัวอย่างการใช้ Azure Key Vault หรือบริการที่คล้ายกัน

3. **การบูรณาการความปลอดภัยเนื้อหา**
   - เพิ่มตัวอย่างการใช้ Azure Content Safety API
   - แสดงรูปแบบการควบคุมเนื้อหาขาเข้าและขาออก

---

## 2. การปรับปรุงคุณภาพโค้ด

### 2.1 เพิ่มไฟล์การกำหนดค่า

| ไฟล์ | จุดประสงค์ |
|------|---------|
| `.eslintrc.json` | กฎการ lint สำหรับ JavaScript/TypeScript |
| `.prettierrc` | มาตรฐานการจัดรูปแบบโค้ด |
| `pyproject.toml` | การตั้งค่าเครื่องมือ Python (Black, Ruff, mypy) |

### 2.2 สร้างยูทิลิตี้แชร์

โมดูลใหม่ `shared/python/` พร้อม:
- `env_utils.py` - การจัดการตัวแปรแวดล้อม
- `input_validation.py` - การตรวจสอบและทำความสะอาดข้อมูลนำเข้า
- `api_utils.py` - ตัว wrapper การร้องขอ API อย่างปลอดภัย

### 2.3 การปรับปรุงโค้ดที่แนะนำ

1. **ครอบคลุม type hints**
   - เพิ่ม type hints ให้กับไฟล์ Python ทุกไฟล์
   - เปิดใช้ strict mode ใน TypeScript ทุกโปรเจกต์

2. **มาตรฐานเอกสารอธิบาย**
   - เพิ่ม docstrings ให้กับฟังก์ชัน Python ทุกฟังก์ชัน
   - เพิ่มคอมเมนต์ JSDoc ให้กับฟังก์ชัน JavaScript/TypeScript ทุกฟังก์ชัน

3. **กรอบการทดสอบ**
   - เพิ่มการตั้งค่า pytest และตัวอย่างการทดสอบ _(เสร็จแล้ว: การตั้งค่า pytest ใน `pyproject.toml`; ตัวอย่างทดสอบสำหรับยูทิลิตี้แชร์ใน [`tests/`](../../../tests) ที่รันใน CI)_
   - เพิ่มการตั้งค่า Jest สำหรับ JavaScript/TypeScript

---

## 3. การปรับปรุงด้านการศึกษา

### 3.1 หัวข้อบทเรียนใหม่

1. **ความปลอดภัยในแอปพลิเคชัน AI** (บทเรียนที่เสนอ 22)
   - การโจมตีและการป้องกัน prompt injection
   - การจัดการคีย์ API
   - การควบคุมเนื้อหา
   - การจำกัดอัตราและการป้องกันการละเมิด

2. **การปรับใช้งานระดับโปรดักชัน** (บทเรียนที่เสนอ 23)
   - Containerization ด้วย Docker
   - pipeline CI/CD
   - การติดตามและบันทึกข้อมูล
   - การจัดการต้นทุน

3. **เทคนิค RAG ขั้นสูง** (บทเรียนที่เสนอ 24)
   - การค้นหาแบบไฮบริด (คำค้น + ความหมาย)
   - กลยุทธ์การจัดอันดับใหม่
   - Multi-modal RAG
   - เกณฑ์การประเมิน

### 3.2 การปรับปรุงบทเรียนที่มีอยู่

| บทเรียน | การปรับปรุงที่แนะนำ |
|--------|------------------------|
| 06 - การสร้างข้อความ | เพิ่มตัวอย่างการตอบสนองแบบสตรีมมิ่ง |
| 07 - แอปพลิเคชันแชท | เพิ่มรูปแบบความจำบทสนทนา |
| 08 - แอปพลิเคชันค้นหา | เพิ่มการเปรียบเทียบฐานข้อมูลเวกเตอร์ |
| 09 - การสร้างภาพ | เพิ่มตัวอย่างการแก้ไข/เปลี่ยนแปลงภาพ |
| 11 - การเรียกฟังก์ชัน | เพิ่มการเรียกฟังก์ชันแบบขนาน |
| 15 - RAG | เพิ่มการเปรียบเทียบกลยุทธ์ chunking |
| 17 - AI Agents | เพิ่มการประสานงานของหลายเอเย่นต์ |

---

## 4. การทำให้ API ทันสมัย

### 4.1 รูปแบบ API ที่เลิกใช้ (การย้ายเสร็จสมบูรณ์)

ตัวอย่าง chat ทั้งหมดสำหรับ Python และ TypeScript ได้ย้ายจาก Chat Completions API ไปยัง Responses API (`client.responses.create(...)` → `response.output_text`)

| รูปแบบเก่า | รูปแบบใหม่ | สถานะ |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | เสร็จสมบูรณ์ |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | เสร็จสมบูรณ์ |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | แพ็กเกจ `openai` `client.responses.create()` → `response.output_text` | เสร็จสมบูรณ์ |
| `df.append()` (pandas) | `pd.concat()` | เสร็จสมบูรณ์ |

> **หมายเหตุ:** ตัวอย่าง Microsoft Foundry Models ที่ใช้ `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) ยังคงใช้ Model Inference API ซึ่งไม่รองรับ Responses API `AzureOpenAI()` ยังคงถูกเก็บไว้ในที่ที่ยังใช้ได้ (embeddings และการสร้างภาพ)

### 4.2 คุณสมบัติ API ใหม่ที่จะแสดง

1. **ผลลัพธ์แบบมีโครงสร้าง** (OpenAI)
   - โหมด JSON
   - การเรียกฟังก์ชันพร้อม schema เคร่งครัด

2. **ความสามารถทางการมองเห็น**
   - การวิเคราะห์ภาพด้วย GPT-4o (vision)
   - prompt แบบ multi-modal

3. **เครื่องมือในตัวของ Responses API** (แทนที่ Assistants API แบบเก่า)
   - ตัวแปลโค้ด
   - การค้นหาไฟล์
   - การค้นหาเว็บและเครื่องมือกำหนดเอง

---

## 5. การปรับปรุงโครงสร้างพื้นฐาน

### 5.1 การเสริม CI/CD

ดำเนินการใน [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): การ lint/format Python (Ruff + Black) ถูก **บังคับใช้** กับโมดูลยูทิลิตี้ `shared/` ที่ดูแล และทำงานแบบ **แนะนำ** ในหลักสูตรส่วนที่เหลือ พร้อมกับผ่าน ESLint แบบแนะนำสำหรับ JavaScript/TypeScript ตัวอย่างฐานที่นำเสนอคือ:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 การสแกนความปลอดภัย

ดำเนินการใน [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): วิเคราะห์ CodeQL สำหรับ Python และ JavaScript/TypeScript (เมื่อ push, pull request และกำหนดการรายสัปดาห์) รวมถึงการตรวจสอบ dependencies ใน pull requests ตัวอย่างฐานที่นำเสนอคือ:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. การปรับปรุงประสบการณ์นักพัฒนา

### 6.1 การเสริม DevContainer

ดำเนินการใน [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) และ [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): container ปัจจุบันมาพร้อมกับ Pylance, formatter Black, Ruff, ESLint, Prettier และส่วนขยาย Copilot พร้อมเปิดใช้ format-on-save ที่เชื่อมโยงกับการตั้งค่า Black/Prettier ของรีโป และติดตั้งเครื่องมือพัฒนา (`ruff`, `black`, `mypy`, `pytest`) เพื่อให้การรัน [workflow คุณภาพโค้ด](../../../.github/workflows/code-quality.yml) ทำซ้ำได้ในเครื่องฐานภาพ `mcr.microsoft.com/devcontainers/universal` มี Python และ Node ในตัวอยู่แล้วจึงไม่ต้องการคุณสมบัติเพิ่มเติม ตัวอย่างฐานที่นำเสนอคือ:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 สนามเล่นแบบโต้ตอบ

พิจารณาเพิ่ม:
- สมุดโน้ต Jupyter ที่กำหนดค่า API keys ไว้ล่วงหน้า (ผ่าน environment)
- การสาธิต Gradio/Streamlit สำหรับผู้เรียนแบบภาพ
- แบบทดสอบเชิงโต้ตอบสำหรับการประเมินความรู้

---

## 7. การสนับสนุนหลายภาษา

### 7.1 ภาษาปัจจุบันที่ครอบคลุม

| เทคโนโลยี | บทเรียนที่ครอบคลุม | สถานะ |
|------------|-----------------|--------|
| Python | ทั้งหมด | เสร็จสมบูรณ์ |
| TypeScript | 06-09, 11 | ส่วนหนึ่ง |
| JavaScript | 06-08, 11 | ส่วนหนึ่ง |
| .NET/C# | บางส่วน | ส่วนหนึ่ง |

### 7.2 การเพิ่มภาษาแนะนำ

1. **Go** - กำลังเติบโตในเครื่องมือ AI/ML
2. **Rust** - แอปพลิเคชันที่ต้องการประสิทธิภาพสูง
3. **Java/Kotlin** - แอปพลิเคชันสำหรับองค์กร

---

## 8. การเพิ่มประสิทธิภาพประสิทธิผล

### 8.1 การเพิ่มประสิทธิภาพระดับโค้ด

1. **รูปแบบ Async/Await**
   - เพิ่มตัวอย่าง async สำหรับการประมวลผลแบบเป็นชุด
   - แสดงการเรียก API แบบพร้อมกัน

2. **กลยุทธ์แคช**
   - เพิ่มตัวอย่างการแคช embeddings
   - แสดงรูปแบบการแคชผลลัพธ์

3. **การเพิ่มประสิทธิภาพ token**
   - เพิ่มตัวอย่างการใช้ tiktoken
   - แสดงเทคนิคการบีบอัด prompt

### 8.2 ตัวอย่างการเพิ่มประสิทธิภาพต้นทุน

เพิ่มตัวอย่างสาธิต:
- การเลือกโมเดลตามความซับซ้อนของงาน
- การออกแบบ prompt เพื่อประหยัด token
- การประมวลผลเป็นชุดสำหรับงานจำนวนมาก

---

## 9. การเข้าถึงและนานาชาติ

### 9.1 สถานะการแปลปัจจุบัน

การแปลทั้งหมด **สมบูรณ์** และสร้างโดยอัตโนมัติผ่าน [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) ซึ่งสร้างและคงไว้ซึ่งเวอร์ชันภาษา 50+ ของหลักสูตรให้สอดคล้องกับต้นฉบับภาษาอังกฤษ เนื้อหาที่แปลจัดเก็บไว้ใน `translations/` และภาพแปลใน `translated_images/`; รายชื่อภาษาทั้งหมดที่มีเผยแพร่ที่ส่วนหัวของ README ในรีโพ

| ด้าน | สถานะ |
|--------|--------|
| ความครอบคลุมการแปล | สมบูรณ์ — 50+ ภาษา, ทุกบทเรียน |
| วิธีการแปล | อัตโนมัติผ่าน [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| คงความสอดคล้องกับต้นฉบับภาษาอังกฤษ | ใช่ — สร้างใหม่อัตโนมัติ |

### 9.2 การปรับปรุงการเข้าถึง

1. เพิ่มข้อความ alt ให้กับภาพทั้งหมด
2. ตรวจสอบให้แน่ใจว่าตัวอย่างโค้ดมีการเน้นไวยากรณ์ที่เหมาะสม
3. เพิ่มคำบรรยายวิดีโอสำหรับเนื้อหาวิดีโอทั้งหมด
4. ตรวจสอบให้แน่ใจว่าคอนทราสต์สีเป็นไปตามแนวทาง WCAG

---

## 10. ลำดับความสำคัญในการดำเนินการ

### ระยะที่ 1: ทันที (สัปดาห์ 1-2)
- [x] แก้ไขปัญหาความปลอดภัยที่สำคัญ
- [x] เพิ่มการตั้งค่าคุณภาพโค้ด
- [x] สร้างยูทิลิตี้แชร์
- [x] จัดทำเอกสารคำแนะนำความปลอดภัย

### ระยะที่ 2: ระยะสั้น (สัปดาห์ 3-4)
- [x] อัปเดตรูปแบบ API ที่เลิกใช้ (Chat Completions → Responses API, Python + TypeScript)
- [ ] เพิ่ม type hints ให้ไฟล์ Python ทุกไฟล์ (เสร็จสำหรับโมดูล `shared/` ที่ดูแล; ตัวอย่างในบทเรียนใช้แบบง่าย)
- [x] เพิ่ม workflow CI/CD สำหรับคุณภาพโค้ด
- [x] สร้าง workflow การสแกนความปลอดภัย

### ระยะที่ 3: ระยะกลาง (เดือน 2-3)
- [ ] เพิ่มบทเรียนความปลอดภัยใหม่
- [ ] เพิ่มบทเรียนการปรับใช้งานระดับโปรดักชัน
- [x] ปรับปรุงการตั้งค่า DevContainer
- [ ] เพิ่มตัวสาธิตแบบโต้ตอบ

### ระยะที่ 4: ระยะยาว (เดือน 4 ขึ้นไป)
- [ ] เพิ่มบทเรียน RAG ขั้นสูง
- [ ] ขยายการรองรับภาษา
- [ ] เพิ่มชุดทดสอบครบวงจร
- [ ] สร้างโปรแกรมรับรอง

---

## บทสรุป

แผนงานนี้นำเสนอแนวทางที่มีโครงสร้างสำหรับการปรับปรุงหลักสูตร Generative AI for Beginners โดยการจัดการประเด็นด้านความปลอดภัย ทำให้ API ทันสมัย และเพิ่มเนื้อหาทางการศึกษา หลักสูตรจะเตรียมความพร้อมนักเรียนให้ดียิ่งขึ้นสำหรับการพัฒนาแอปพลิเคชัน AI ในโลกจริง

สำหรับคำถามหรือการมีส่วนร่วม กรุณาเปิด issue ในรีโพ GitHub

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->