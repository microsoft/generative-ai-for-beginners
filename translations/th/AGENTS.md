<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:03:08+00:00",
  "source_file": "AGENTS.md",
  "language_code": "th"
}
-->
# AGENTS.md

## ภาพรวมของโปรเจกต์

คลังนี้ประกอบด้วยหลักสูตร 21 บทเรียนที่ครอบคลุมพื้นฐานของ Generative AI และการพัฒนาแอปพลิเคชัน หลักสูตรนี้ออกแบบมาสำหรับผู้เริ่มต้นและครอบคลุมตั้งแต่แนวคิดพื้นฐานไปจนถึงการสร้างแอปพลิเคชันที่พร้อมใช้งานในระดับการผลิต

**เทคโนโลยีสำคัญ:**
- Python 3.9+ พร้อมไลบรารี: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript พร้อม Node.js และไลบรารี: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API และ GitHub Models
- Jupyter Notebooks สำหรับการเรียนรู้แบบโต้ตอบ
- Dev Containers สำหรับสภาพแวดล้อมการพัฒนาที่สม่ำเสมอ

**โครงสร้างของคลัง:**
- โฟลเดอร์บทเรียนที่มีหมายเลข 21 โฟลเดอร์ (00-21) ซึ่งมีไฟล์ README, ตัวอย่างโค้ด และงานที่มอบหมาย
- การใช้งานหลายรูปแบบ: Python, TypeScript และบางครั้งตัวอย่าง .NET
- โฟลเดอร์แปลภาษา พร้อมเวอร์ชันในกว่า 40 ภาษา
- การตั้งค่ากลางผ่านไฟล์ `.env` (ใช้ `.env.copy` เป็นแม่แบบ)

## คำสั่งการตั้งค่า

### การตั้งค่าคลังครั้งแรก

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### การตั้งค่าสภาพแวดล้อม Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### การตั้งค่า Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### การตั้งค่า Dev Container (แนะนำ)

คลังนี้มีการตั้งค่า `.devcontainer` สำหรับ GitHub Codespaces หรือ VS Code Dev Containers:

1. เปิดคลังใน GitHub Codespaces หรือ VS Code พร้อมส่วนขยาย Dev Containers
2. Dev Container จะดำเนินการโดยอัตโนมัติ:
   - ติดตั้งไลบรารี Python จาก `requirements.txt`
   - รันสคริปต์หลังการสร้าง (`.devcontainer/post-create.sh`)
   - ตั้งค่า Jupyter kernel

## เวิร์กโฟลว์การพัฒนา

### ตัวแปรสภาพแวดล้อม

บทเรียนทั้งหมดที่ต้องการการเข้าถึง API ใช้ตัวแปรสภาพแวดล้อมที่กำหนดใน `.env`:

- `OPENAI_API_KEY` - สำหรับ OpenAI API
- `AZURE_OPENAI_API_KEY` - สำหรับ Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL ของ Azure OpenAI endpoint
- `AZURE_OPENAI_DEPLOYMENT` - ชื่อการปรับใช้โมเดล Chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - ชื่อการปรับใช้โมเดล Embeddings
- `AZURE_OPENAI_API_VERSION` - เวอร์ชัน API (ค่าเริ่มต้น: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - สำหรับโมเดล Hugging Face
- `GITHUB_TOKEN` - สำหรับ GitHub Models

### การรันตัวอย่าง Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### การรันตัวอย่าง TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### การรัน Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### การทำงานกับประเภทบทเรียนต่างๆ

- **บทเรียน "Learn"**: เน้นที่เอกสาร README.md และแนวคิด
- **บทเรียน "Build"**: รวมตัวอย่างโค้ดที่ใช้งานได้ใน Python และ TypeScript
- แต่ละบทเรียนมี README.md พร้อมทฤษฎี การอธิบายโค้ด และลิงก์ไปยังเนื้อหาวิดีโอ

## แนวทางการเขียนโค้ด

### Python

- ใช้ `python-dotenv` สำหรับการจัดการตัวแปรสภาพแวดล้อม
- นำเข้าไลบรารี `openai` สำหรับการโต้ตอบกับ API
- ใช้ `pylint` สำหรับการตรวจสอบโค้ด (บางตัวอย่างมี `# pylint: disable=all` เพื่อความเรียบง่าย)
- ปฏิบัติตามการตั้งชื่อของ PEP 8
- เก็บข้อมูลรับรอง API ในไฟล์ `.env` ไม่ใช่ในโค้ด

### TypeScript

- ใช้แพ็กเกจ `dotenv` สำหรับตัวแปรสภาพแวดล้อม
- การตั้งค่า TypeScript ใน `tsconfig.json` สำหรับแต่ละแอป
- ใช้ `@azure/openai` หรือ `@azure-rest/ai-inference` สำหรับบริการ Azure
- ใช้ `nodemon` สำหรับการพัฒนาด้วยการรีโหลดอัตโนมัติ
- สร้างก่อนรัน: `npm run build` แล้ว `npm start`

### แนวทางทั่วไป

- รักษาตัวอย่างโค้ดให้เรียบง่ายและให้ความรู้
- รวมความคิดเห็นที่อธิบายแนวคิดสำคัญ
- โค้ดของแต่ละบทเรียนควรเป็นแบบแยกส่วนและสามารถรันได้
- ใช้การตั้งชื่อที่สม่ำเสมอ: คำนำหน้า `aoai-` สำหรับ Azure OpenAI, `oai-` สำหรับ OpenAI API, `githubmodels-` สำหรับ GitHub Models

## แนวทางการเขียนเอกสาร

### สไตล์ Markdown

- URL ทั้งหมดต้องอยู่ในรูปแบบ `[text](../../url)` โดยไม่มีช่องว่างเพิ่มเติม
- ลิงก์สัมพัทธ์ต้องเริ่มต้นด้วย `./` หรือ `../`
- ลิงก์ทั้งหมดไปยังโดเมนของ Microsoft ต้องมี Tracking ID: `?WT.mc_id=academic-105485-koreyst`
- ห้ามใช้โลเคลเฉพาะประเทศใน URL (หลีกเลี่ยง `/en-us/`)
- รูปภาพเก็บไว้ในโฟลเดอร์ `./images` พร้อมชื่อที่อธิบายได้
- ใช้อักขระภาษาอังกฤษ ตัวเลข และขีดกลางในชื่อไฟล์

### การสนับสนุนการแปลภาษา

- คลังรองรับกว่า 40 ภาษาโดยใช้ GitHub Actions อัตโนมัติ
- การแปลเก็บไว้ในโฟลเดอร์ `translations/`
- ห้ามส่งการแปลบางส่วน
- ไม่รับการแปลด้วยเครื่อง
- รูปภาพที่แปลเก็บไว้ในโฟลเดอร์ `translated_images/`

## การทดสอบและการตรวจสอบ

### การตรวจสอบก่อนส่ง

คลังนี้ใช้ GitHub Actions สำหรับการตรวจสอบ ก่อนส่ง PR:

1. **ตรวจสอบลิงก์ Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **การทดสอบด้วยตนเอง**:
   - ทดสอบตัวอย่าง Python: เปิดใช้งาน venv และรันสคริปต์
   - ทดสอบตัวอย่าง TypeScript: `npm install`, `npm run build`, `npm start`
   - ตรวจสอบว่าตัวแปรสภาพแวดล้อมถูกตั้งค่าอย่างถูกต้อง
   - ตรวจสอบว่า API keys ใช้งานได้กับตัวอย่างโค้ด

3. **ตัวอย่างโค้ด**:
   - ตรวจสอบว่าโค้ดทั้งหมดรันได้โดยไม่มีข้อผิดพลาด
   - ทดสอบกับทั้ง Azure OpenAI และ OpenAI API เมื่อสามารถทำได้
   - ตรวจสอบว่าตัวอย่างใช้งานได้กับ GitHub Models ในกรณีที่รองรับ

### ไม่มีการทดสอบอัตโนมัติ

นี่เป็นคลังการศึกษาที่เน้นบทเรียนและตัวอย่าง ไม่มีการทดสอบหน่วยหรือการทดสอบการรวม การตรวจสอบส่วนใหญ่คือ:
- การทดสอบโค้ดด้วยตนเอง
- GitHub Actions สำหรับการตรวจสอบ Markdown
- การตรวจสอบเนื้อหาการศึกษาโดยชุมชน

## แนวทางการส่ง Pull Request

### ก่อนส่ง

1. ทดสอบการเปลี่ยนแปลงโค้ดทั้งใน Python และ TypeScript เมื่อสามารถทำได้
2. รันการตรวจสอบ Markdown (เริ่มต้นโดยอัตโนมัติเมื่อส่ง PR)
3. ตรวจสอบว่า Tracking IDs มีอยู่ใน URL ของ Microsoft ทั้งหมด
4. ตรวจสอบว่าลิงก์สัมพัทธ์ถูกต้อง
5. ตรวจสอบว่ารูปภาพถูกอ้างอิงอย่างถูกต้อง

### รูปแบบชื่อ PR

- ใช้ชื่อที่อธิบายได้: `[Lesson 06] Fix Python example typo` หรือ `Update README for lesson 08`
- อ้างอิงหมายเลขปัญหาเมื่อสามารถทำได้: `Fixes #123`

### คำอธิบาย PR

- อธิบายสิ่งที่เปลี่ยนแปลงและเหตุผล
- ลิงก์ไปยังปัญหาที่เกี่ยวข้อง
- สำหรับการเปลี่ยนแปลงโค้ด ระบุว่าตัวอย่างใดที่ได้รับการทดสอบ
- สำหรับ PR การแปล รวมไฟล์ทั้งหมดสำหรับการแปลที่สมบูรณ์

### ข้อกำหนดการมีส่วนร่วม

- ลงนาม Microsoft CLA (อัตโนมัติเมื่อส่ง PR ครั้งแรก)
- Fork คลังไปยังบัญชีของคุณก่อนทำการเปลี่ยนแปลง
- หนึ่ง PR ต่อการเปลี่ยนแปลงที่มีเหตุผล (อย่ารวมการแก้ไขที่ไม่เกี่ยวข้อง)
- รักษา PR ให้เน้นและเล็กที่สุดเมื่อสามารถทำได้

## เวิร์กโฟลว์ทั่วไป

### การเพิ่มตัวอย่างโค้ดใหม่

1. ไปยังโฟลเดอร์บทเรียนที่เหมาะสม
2. สร้างตัวอย่างในไดเรกทอรี `python/` หรือ `typescript/`
3. ปฏิบัติตามการตั้งชื่อ: `{provider}-{example-name}.{py|ts|js}`
4. ทดสอบด้วยข้อมูลรับรอง API จริง
5. เอกสารตัวแปรสภาพแวดล้อมใหม่ใน README ของบทเรียน

### การอัปเดตเอกสาร

1. แก้ไข README.md ในโฟลเดอร์บทเรียน
2. ปฏิบัติตามแนวทาง Markdown (Tracking IDs, ลิงก์สัมพัทธ์)
3. การอัปเดตการแปลจัดการโดย GitHub Actions (อย่าแก้ไขด้วยตนเอง)
4. ทดสอบว่าลิงก์ทั้งหมดถูกต้อง

### การทำงานกับ Dev Containers

1. คลังนี้มี `.devcontainer/devcontainer.json`
2. สคริปต์หลังการสร้างติดตั้งไลบรารี Python โดยอัตโนมัติ
3. ส่วนขยายสำหรับ Python และ Jupyter ถูกตั้งค่าไว้ล่วงหน้า
4. สภาพแวดล้อมอิงตาม `mcr.microsoft.com/devcontainers/universal:2.11.2`

## การเผยแพร่และการใช้งาน

นี่เป็นคลังการเรียนรู้ - ไม่มีกระบวนการเผยแพร่ หลักสูตรนี้ถูกใช้งานโดย:

1. **GitHub Repository**: เข้าถึงโค้ดและเอกสารโดยตรง
2. **GitHub Codespaces**: สภาพแวดล้อมการพัฒนาทันทีพร้อมการตั้งค่าล่วงหน้า
3. **Microsoft Learn**: เนื้อหาอาจถูกเผยแพร่ไปยังแพลตฟอร์มการเรียนรู้อย่างเป็นทางการ
4. **docsify**: เว็บไซต์เอกสารที่สร้างจาก Markdown (ดู `docsifytopdf.js` และ `package.json`)

### การสร้างเว็บไซต์เอกสาร

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## การแก้ไขปัญหา

### ปัญหาทั่วไป

**ข้อผิดพลาดการนำเข้า Python**:
- ตรวจสอบว่าสภาพแวดล้อมเสมือนถูกเปิดใช้งาน
- รัน `pip install -r requirements.txt`
- ตรวจสอบว่าเวอร์ชัน Python คือ 3.9+

**ข้อผิดพลาดการสร้าง TypeScript**:
- รัน `npm install` ในไดเรกทอรีแอปเฉพาะ
- ตรวจสอบว่าเวอร์ชัน Node.js เข้ากันได้
- ล้าง `node_modules` และติดตั้งใหม่หากจำเป็น

**ข้อผิดพลาดการตรวจสอบสิทธิ์ API**:
- ตรวจสอบว่าไฟล์ `.env` มีอยู่และมีค่าที่ถูกต้อง
- ตรวจสอบว่า API keys ใช้งานได้และไม่หมดอายุ
- ตรวจสอบว่า URL endpoint ถูกต้องสำหรับภูมิภาคของคุณ

**ตัวแปรสภาพแวดล้อมที่หายไป**:
- คัดลอก `.env.copy` ไปยัง `.env`
- เติมค่าที่จำเป็นทั้งหมดสำหรับบทเรียนที่คุณกำลังทำงาน
- รีสตาร์ทแอปพลิเคชันของคุณหลังจากอัปเดต `.env`

## แหล่งข้อมูลเพิ่มเติม

- [คู่มือการตั้งค่าหลักสูตร](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [แนวทางการมีส่วนร่วม](./CONTRIBUTING.md)
- [จรรยาบรรณ](./CODE_OF_CONDUCT.md)
- [นโยบายความปลอดภัย](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [คอลเลกชันตัวอย่างโค้ดขั้นสูง](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## หมายเหตุเฉพาะโปรเจกต์

- นี่เป็น **คลังการศึกษา** ที่เน้นการเรียนรู้ ไม่ใช่โค้ดสำหรับการผลิต
- ตัวอย่างถูกออกแบบให้เรียบง่ายและเน้นการสอนแนวคิด
- คุณภาพของโค้ดถูกปรับสมดุลกับความชัดเจนในการศึกษา
- แต่ละบทเรียนเป็นแบบแยกส่วนและสามารถทำได้อย่างอิสระ
- คลังรองรับผู้ให้บริการ API หลายราย: Azure OpenAI, OpenAI และ GitHub Models
- เนื้อหาเป็นแบบหลายภาษา พร้อมเวิร์กโฟลว์การแปลอัตโนมัติ
- ชุมชนที่ใช้งานบน Discord สำหรับคำถามและการสนับสนุน

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้