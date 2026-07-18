# AGENTS.md

## ภาพรวมโครงการ

ที่เก็บนี้มีหลักสูตรครบ 21 บทเรียน ที่สอนพื้นฐาน Generative AI และการพัฒนาแอปพลิเคชัน หลักสูตรออกแบบสำหรับผู้เริ่มต้นและครอบคลุมทุกอย่างตั้งแต่แนวคิดพื้นฐานจนถึงการสร้างแอปที่พร้อมใช้งานจริง

**เทคโนโลยีสำคัญ:**
- Python 3.9+ พร้อมไลบรารี: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript กับ Node.js และไลบรารี: `openai` (Azure OpenAI ผ่าน endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API และ Microsoft Foundry Models (GitHub Models จะหยุดให้บริการปลายเดือนกรกฎาคม 2026)
- Jupyter Notebooks สำหรับการเรียนรู้อินเทอร์แอคทีฟ
- Dev Containers สำหรับสภาพแวดล้อมการพัฒนาที่สม่ำเสมอ

**โครงสร้างที่เก็บ:**
- โฟลเดอร์บทเรียนจำนวน 21 โฟลเดอร์ (00-21) มี README, ตัวอย่างโค้ด และงานที่ต้องทำ
- การนำไปใช้หลากหลาย: ตัวอย่าง Python, TypeScript และบางครั้ง .NET
- โฟลเดอร์แปลภาษาที่มีเวอร์ชันกว่า 40 ภาษา
- การตั้งค่ากลางผ่านไฟล์ `.env` (ใช้ `.env.copy` เป็นแม่แบบ)

## คำสั่งตั้งค่า

### การตั้งค่าเริ่มต้นที่เก็บ

```bash
# โคลนที่เก็บโค้ด
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# คัดลอกเทมเพลตสภาพแวดล้อม
cp .env.copy .env
# แก้ไขไฟล์ .env ด้วยคีย์ API และจุดสิ้นสุดของคุณ
```

### การตั้งค่าสภาพแวดล้อม Python

```bash
# สร้างสภาพแวดล้อมเสมือน
python3 -m venv venv

# เปิดใช้งานสภาพแวดล้อมเสมือน
# บน macOS/Linux:
source venv/bin/activate
# บน Windows:
venv\Scripts\activate

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### การตั้งค่า Node.js/TypeScript

```bash
# ติดตั้งไลบรารีระดับราก (สำหรับเครื่องมือเอกสาร)
npm install

# สำหรับตัวอย่าง TypeScript ของแต่ละบทเรียน ให้ไปที่บทเรียนที่เจาะจง:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### การตั้งค่า Dev Container (แนะนำ)

ที่เก็บนี้รวมไฟล์กำหนดค่า `.devcontainer` สำหรับ GitHub Codespaces หรือ VS Code Dev Containers:

1. เปิดที่เก็บใน GitHub Codespaces หรือ VS Code ที่ติดตั้งส่วนขยาย Dev Containers
2. Dev Container จะทำงานอัตโนมัติ:
   - ติดตั้ง dependencies ของ Python จาก `requirements.txt`
   - รันสคริปต์ post-create (`.devcontainer/post-create.sh`)
   - ตั้งค่าเคอร์เนล Jupyter

## กระบวนการพัฒนา

### ตัวแปรสภาพแวดล้อม

บทเรียนทั้งหมดที่ต้องเข้าถึง API ใช้ตัวแปรสภาพแวดล้อมที่กำหนดใน `.env`:

- `OPENAI_API_KEY` - สำหรับ OpenAI API
- `AZURE_OPENAI_API_KEY` - สำหรับ Azure OpenAI ใน Microsoft Foundry (Azure OpenAI Service เป็นส่วนหนึ่งของ Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint ของ Azure OpenAI (endpoint ของแหล่งข้อมูล Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - ชื่อ deployment ของโมเดล chat completion (ค่าเริ่มต้นของหลักสูตร: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - ชื่อ deployment ของโมเดล embeddings (ค่าเริ่มต้นของหลักสูตร: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - เวอร์ชัน API (ค่าเริ่มต้น: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - สำหรับโมเดล Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - endpoint โมเดล Microsoft Foundry (แคตตาล็อกโมเดลจากหลายผู้ให้บริการ)
- `AZURE_INFERENCE_CREDENTIAL` - คีย์ API Microsoft Foundry Models (แทนที่ `GITHUB_TOKEN` ที่จะเลิกใช้)
- `AZURE_INFERENCE_CHAT_MODEL` - โมเดลที่ไม่ใช้เหตุผล (เช่น `Llama-3.3-70B-Instruct`) ใช้ในตัวอย่าง `temperature` เนื่องจากโมเดล reasoning ไม่รองรับการควบคุมการสุ่ม

### ข้อตกลงเกี่ยวกับโมเดล (สำคัญ)

- **โมเดล chat ดีฟอลต์คือ `gpt-5-mini`** - โมเดล **reasoning** ปัจจุบันที่ไม่เลิกใช้ ในปี 2026 โมเดล "mini" ที่ใช้ temperature ได้รุ่นเก่า (`gpt-4o-mini`, `gpt-4.1-mini`) จะ *เลิกใช้* ดังนั้นหลักสูตรจึงใช้ตระกูล GPT-5 เป็นมาตรฐาน
- **โมเดล reasoning ปฏิเสธ `temperature` และ `top_p`** และใช้ `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) แทน `max_tokens` ห้ามเพิ่ม `temperature`/`top_p`/`max_tokens` ในตัวอย่างที่เรียก `gpt-5-mini`
- **เพื่อสาธิต `temperature`** ตัวอย่างใช้โมเดล **Llama** (`Llama-3.3-70B-Instruct`) ผ่าน Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`) ควบคุมโมเดล reasoning ด้วยวิศวกรรม prompt + การควบคุม reasoning แทนปุ่มการสุ่ม
- **Fine-tuning (บทเรียน 18)** ยังคงใช้ `gpt-4.1-mini`: GPT-5 รองรับแค่ reinforcement fine-tuning (RFT) ไม่รองรับ supervised fine-tuning (SFT) ที่แสดงในบทเรียนนั้น
- บทเรียน 20 (Mistral) และ 21 (Meta) ยังคงใช้ `temperature`/`max_tokens` เพราะเน้นโมเดล Mistral/Llama ที่รองรับคุณสมบัตินี้

### การรันตัวอย่าง Python

```bash
# ไปที่ไดเรกทอรีบทเรียน
cd 06-text-generation-apps/python

# รันสคริปต์ Python
python aoai-app.py
```

### การรันตัวอย่าง TypeScript

```bash
# ไปที่ไดเรกทอรีแอป TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# สร้างโค้ด TypeScript
npm run build

# รันแอปพลิเคชัน
npm start
```

### การรัน Jupyter Notebooks

```bash
# เริ่ม Jupyter ที่โฟลเดอร์รากของที่เก็บข้อมูล
jupyter notebook

# หรือใช้ VS Code พร้อมส่วนขยาย Jupyter
```

### การทำงานกับประเภทบทเรียนต่างๆ

- **บทเรียน "Learn"**: เน้นเอกสาร README.md และแนวคิด
- **บทเรียน "Build"**: รวมตัวอย่างโค้ดที่ใช้งานได้ใน Python และ TypeScript
- บทเรียนแต่ละบทมี README.md ที่อธิบายทฤษฎี การสาธิตโค้ด และลิงก์ไปยังเนื้อหาวิดีโอ

## แนวทางการเขียนโค้ด

### Python

- ใช้ `python-dotenv` เพื่อจัดการตัวแปรสภาพแวดล้อม
- นำเข้าไลบรารี `openai` สำหรับโต้ตอบ API
- ใช้ `pylint` สำหรับตรวจสอบ (บางตัวอย่างมี `# pylint: disable=all` เพื่อความง่าย)
- ปฏิบัติตามมาตรฐานการตั้งชื่อ PEP 8
- เก็บข้อมูลล็อกอิน API ในไฟล์ `.env` ห้ามใส่ในโค้ด

### TypeScript

- ใช้แพ็กเกจ `dotenv` สำหรับตัวแปรสภาพแวดล้อม
- การตั้งค่า TypeScript ในไฟล์ `tsconfig.json` ของแต่ละแอป
- ใช้แพ็กเกจ `openai` สำหรับ Azure OpenAI (ตั้งค่าลูกค้าเรียกที่ endpoint `/openai/v1/` และเรียก `client.responses.create`); ใช้ `@azure-rest/ai-inference` สำหรับ Microsoft Foundry Models
- ใช้ `nodemon` สำหรับพัฒนาแบบรีโหลดอัตโนมัติ
- สร้างก่อนรัน: `npm run build` แล้ว `npm start`

### แนวทางปฏิบัติทั่วไป

- ทำตัวอย่างโค้ดให้เรียบง่ายและเพื่อการศึกษา
- ใส่คำอธิบายอธิบายแนวคิดหลัก
- โค้ดของแต่ละบทเรียนควรเป็นแบบแยกตัวและรันได้
- ใช้การตั้งชื่อที่สม่ำเสมอ: คำนำหน้า `aoai-` สำหรับ Azure OpenAI, `oai-` สำหรับ OpenAI API, `githubmodels-` สำหรับ Microsoft Foundry Models (คำนำหน้าเก่ายังคงใช้จากยุค GitHub Models)

## แนวทางการเขียนเอกสาร

### สไตล์ Markdown

- URL ทุกตัวต้องอยู่ในรูปแบบ `[text](../../url)` ไม่มีช่องว่างเพิ่ม
- ลิงก์สัมพันธ์ต้องเริ่มต้นด้วย `./` หรือ `../`
- ลิงก์ไปยังโดเมน Microsoft ต้องใส่ tracking ID: `?WT.mc_id=academic-105485-koreyst`
- หลีกเลี่ยงลิงก์ที่มี locale เฉพาะประเทศ เช่น `/en-us/`
- ภาพเก็บในโฟลเดอร์ `./images` พร้อมชื่อที่อธิบาย
- ใช้ตัวอักษรภาษาอังกฤษ ตัวเลข และขีดกลางในชื่อไฟล์

### การสนับสนุนการแปลภาษา

- ที่เก็บสนับสนุนกว่า 40 ภาษา ผ่าน GitHub Actions อัตโนมัติ
- การแปลเก็บในโฟลเดอร์ `translations/`
- ห้ามส่งแปลแบบบางส่วน
- ไม่รับแปลโดยเครื่อง
- ภาพที่แปลแล้วเก็บในโฟลเดอร์ `translated_images/`

## การทดสอบและการตรวจสอบ

### การตรวจสอบก่อนส่ง

ที่เก็บใช้ GitHub Actions สำหรับการตรวจสอบ ก่อนส่ง PR:

1. **ตรวจสอบลิงก์ Markdown**:
   ```bash
   # กระบวนการ validate-markdown.yml ตรวจสอบ:
   # - เส้นทางสัมพัทธ์ที่เสียหาย
   # - ขาด ID การติดตามบนเส้นทาง
   # - ขาด ID การติดตามบน URL
   # - URL ที่มีประเทศภาษาถิ่น
   # - URL ภายนอกที่เสียหาย
   ```

2. **ทดสอบด้วยตนเอง**:
   - ทดสอบตัวอย่าง Python: เปิด venv และรันสคริปต์
   - ทดสอบตัวอย่าง TypeScript: `npm install`, `npm run build`, `npm start`
   - ตรวจสอบตัวแปรสภาพแวดล้อมตั้งค่าสมบูรณ์
   - ตรวจสอบว่า API key ใช้งานได้กับตัวอย่างโค้ด

3. **ตัวอย่างโค้ด**:
   - ตรวจสอบว่าโค้ดทั้งหมดรันได้โดยไม่มีข้อผิดพลาด
   - ทดสอบกับทั้ง Azure OpenAI และ OpenAI API เมื่อใช้ได้
   - ตรวจสอบตัวอย่างที่ใช้ Microsoft Foundry Models ในกรณีที่รองรับ

### ไม่มีการทดสอบอัตโนมัติ

ที่เก็บนี้เน้นการสอนและตัวอย่าง ไม่มีการทดสอบ unit หรือ integration สิ่งที่ตรวจสอบหลักคือ:
- การทดสอบตัวอย่างโค้ดด้วยตนเอง
- GitHub Actions สำหรับตรวจสอบ Markdown
- การตรวจสอบเนื้อหาการศึกษาโดยชุมชน

## แนวทางการส่ง Pull Request

### ก่อนส่ง

1. ทดสอบการเปลี่ยนแปลงโค้ดใน Python และ TypeScript เมื่อใช้ได้
2. รันการตรวจสอบ Markdown (จะทำโดยอัตโนมัติเมื่อส่ง PR)
3. ตรวจสอบว่าลิงก์ Microsoft ทุกอันมี tracking ID
4. ตรวจสอบว่าลิงก์สัมพันธ์ถูกต้อง
5. ตรวจสอบว่าภาพถูกอ้างอิงอย่างถูกต้อง

### รูปแบบหัวข้อ PR

- ใช้หัวข้อที่อธิบายชัดเจน: `[Lesson 06] แก้ไขตัวอย่าง Python ผิดพลาด` หรือ `อัปเดต README สำหรับบทเรียน 08`
- อ้างถึงหมายเลข issue เมื่อใช้ได้: `Fixes #123`

### คำอธิบาย PR

- อธิบายการเปลี่ยนแปลงและเหตุผล
- ลิงก์ไปยัง issue ที่เกี่ยวข้อง
- สำหรับการเปลี่ยนแปลงโค้ด ระบุว่าทดสอบตัวอย่างใดบ้าง
- สำหรับ PR แปลภาษา ระบุไฟล์ทั้งหมดสำหรับการแปลครบถ้วน

### ข้อกำหนดการร่วมมือ

- ลงนามใน Microsoft CLA (อัตโนมัติเมื่อส่ง PR ครั้งแรก)
- Fork ที่เก็บไปยังบัญชีของคุณก่อนทำการเปลี่ยนแปลง
- หนึ่ง PR ต่อการเปลี่ยนแปลงเชิงตรรกะ (อย่ารวมหลายแก้ไขไม่เกี่ยวข้องกัน)
- ทำ PR ให้เน้นและเล็กที่สุดเท่าที่จะทำได้

## กระบวนการทำงานทั่วไป

### การเพิ่มตัวอย่างโค้ดใหม่

1. ไปที่โฟลเดอร์บทเรียนที่เกี่ยวข้อง
2. สร้างตัวอย่างในโฟลเดอร์ย่อย `python/` หรือ `typescript/`
3. ปฏิบัติตามข้อตกลงการตั้งชื่อ: `{provider}-{example-name}.{py|ts|js}`
4. ทดสอบด้วย credential API จริง
5. บันทึกตัวแปรสภาพแวดล้อมใหม่ใน README ของบทเรียน

### การอัปเดตเอกสาร

1. แก้ไข README.md ในโฟลเดอร์บทเรียน
2. ปฏิบัติตามแนวทาง Markdown (tracking ID, ลิงก์สัมพันธ์)
3. การอัปเดตการแปลดูแลโดย GitHub Actions (ห้ามแก้ไขเอง)
4. ทดสอบว่าลิงก์ทั้งหมดถูกต้อง

### การทำงานกับ Dev Containers

1. ที่เก็บมีไฟล์ `.devcontainer/devcontainer.json`
2. สคริปต์ post-create ติดตั้ง dependencies ของ Python อัตโนมัติ
3. ส่วนขยาย Python และ Jupyter ถูกตั้งค่าล่วงหน้า
4. สภาพแวดล้อมฐานอยู่บน `mcr.microsoft.com/devcontainers/universal:2.11.2`

## การปรับใช้และเผยแพร่

นี่คือที่เก็บสำหรับการเรียนรู้ - ไม่มีขั้นตอนการปรับใช้ หลักสูตรถูกบริโภคโดย:

1. **ที่เก็บ GitHub**: เข้าถึงโค้ดและเอกสารโดยตรง
2. **GitHub Codespaces**: สภาพแวดล้อมพัฒนาแบบทันทีที่ตั้งค่าล่วงหน้าแล้ว
3. **Microsoft Learn**: เนื้อหาอาจถูกเผยแพร่ในแพลตฟอร์มการเรียนรู้ทางการ
4. **docsify**: เว็บไซต์เอกสารสร้างจาก Markdown (ดู `docsifytopdf.js` และ `package.json`)

### การสร้างเว็บไซต์เอกสาร

```bash
# สร้าง PDF จากเอกสารประกอบ (ถ้าจำเป็น)
npm run convert
```

## การแก้ไขปัญหา

### ปัญหาทั่วไป

**ข้อผิดพลาดการนำเข้า Python**:
- ตรวจสอบให้แน่ใจว่าได้เปิดใช้งาน virtual environment แล้ว
- รัน `pip install -r requirements.txt`
- ตรวจสอบเวอร์ชัน Python ให้เป็น 3.9 ขึ้นไป

**ข้อผิดพลาดการคอมไพล์ TypeScript**:
- รัน `npm install` ในโฟลเดอร์แอปนั้น ๆ
- ตรวจสอบว่าเวอร์ชัน Node.js รองรับ
- ลบโฟลเดอร์ `node_modules` และติดตั้งใหม่หากจำเป็น

**ข้อผิดพลาดการตรวจสอบสิทธิ์ API**:
- ตรวจสอบว่าไฟล์ `.env` มีอยู่และค่าถูกต้อง
- ตรวจสอบว่า API key ถูกต้องและไม่หมดอายุ
- ตรวจสอบ URL endpoint ให้ถูกต้องกับภูมิภาคของคุณ

**ตัวแปรสภาพแวดล้อมหายไป**:
- คัดลอก `.env.copy` ไป `.env`
- เติมค่าที่จำเป็นทั้งหมดสำหรับบทเรียนที่คุณกำลังทำงาน
- รีสตาร์ทแอปหลังอัปเดต `.env`

## แหล่งข้อมูลเพิ่มเติม

- [คู่มือการตั้งค่าหลักสูตร](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [แนวทางการร่วมมือ](./CONTRIBUTING.md)
- [จรรยาบรรณการเขียนโค้ด](./CODE_OF_CONDUCT.md)
- [นโยบายความปลอดภัย](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [ชุดตัวอย่างโค้ดขั้นสูง](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## หมายเหตุเฉพาะโครงการ

- นี่คือ **ที่เก็บเพื่อการศึกษา** เน้นการเรียนรู้ ไม่ใช่โค้ดสำหรับผลิต
- ตัวอย่างจงใจทำให้เรียบง่ายและเน้นสอนแนวคิด
- คุณภาพโค้ดผสมผสานกับความชัดเจนเพื่อการศึกษา
- บทเรียนแต่ละบทเรียนเป็นอิสระและสามารถทำได้โดยแยกจากกัน
- ที่เก็บสนับสนุนผู้ให้บริการ API หลายเจ้า: Azure OpenAI, OpenAI, Microsoft Foundry Models และผู้ให้บริการออฟไลน์เช่น Foundry Local และ Ollama
- เนื้อหาเป็นหลายภาษา พร้อมเวิร์กโฟลว์แปลอัตโนมัติ
- มีชุมชนที่ใช้งานบน Discord สำหรับคำถามและการสนับสนุน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->