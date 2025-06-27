<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:19:51+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "th"
}
-->
# ตั้งค่าสภาพแวดล้อมการพัฒนา

เราได้ตั้งค่ารีโพสิทอรีและคอร์สนี้ด้วย [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ที่มี Universal runtime ซึ่งสามารถรองรับการพัฒนา Python3, .NET, Node.js และ Java การกำหนดค่าที่เกี่ยวข้องถูกกำหนดไว้ในไฟล์ `devcontainer.json` ที่อยู่ในโฟลเดอร์ `.devcontainer/` ที่รูทของรีโพสิทอรีนี้

ในการเปิดใช้งาน dev container ให้เปิดใน [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (สำหรับ runtime ที่โฮสต์บนคลาวด์) หรือใน [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (สำหรับ runtime ที่โฮสต์บนอุปกรณ์ท้องถิ่น) อ่าน [เอกสารนี้](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับการทำงานของ dev containers ใน VS Code

> [!TIP]  
> เราแนะนำให้ใช้ GitHub Codespaces สำหรับการเริ่มต้นอย่างรวดเร็วด้วยความพยายามน้อยที่สุด มันมี [โควต้าใช้งานฟรี](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) สำหรับบัญชีส่วนบุคคล ตั้งค่า [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อหยุดหรือลบ codespaces ที่ไม่ได้ใช้งานเพื่อเพิ่มการใช้โควต้าให้มากที่สุด

## 1. การทำงานของงานที่มอบหมาย

แต่ละบทเรียนจะมีงานที่มอบหมาย _ไม่บังคับ_ ที่อาจมีในหนึ่งหรือหลายภาษาโปรแกรมรวมถึง: Python, .NET/C#, Java และ JavaScript/TypeScript ส่วนนี้ให้คำแนะนำทั่วไปที่เกี่ยวข้องกับการทำงานของงานที่มอบหมายเหล่านั้น

### 1.1 งานที่มอบหมาย Python

งานที่มอบหมาย Python จะมีให้เป็นแอปพลิเคชัน (ไฟล์ `.py`) หรือ Jupyter notebooks (ไฟล์ `.ipynb`)
- ในการรัน notebook ให้เปิดใน Visual Studio Code แล้วคลิก _Select Kernel_ (ที่มุมบนขวา) และเลือกตัวเลือก Python 3 ที่แสดงเป็นค่าเริ่มต้น คุณสามารถ _Run All_ เพื่อรัน notebook ได้
- ในการรันแอปพลิเคชัน Python จาก command-line ให้ทำตามคำแนะนำเฉพาะของงานที่มอบหมายเพื่อให้แน่ใจว่าคุณเลือกไฟล์ที่ถูกต้องและให้พารามิเตอร์ที่จำเป็น

## 2. การตั้งค่าผู้ให้บริการ

งานที่มอบหมาย **อาจ** ถูกตั้งค่าให้ทำงานกับการใช้งาน Large Language Model (LLM) หนึ่งหรือมากกว่าผ่านผู้ให้บริการที่รองรับ เช่น OpenAI, Azure หรือ Hugging Face ซึ่งให้ _hosted endpoint_ (API) ที่เราสามารถเข้าถึงได้ด้วยโปรแกรมโดยใช้ข้อมูลรับรองที่ถูกต้อง (API key หรือ token) ในคอร์สนี้ เราจะพูดถึงผู้ให้บริการเหล่านี้:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) กับโมเดลหลากหลายรวมถึงซีรีส์ GPT หลัก
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) สำหรับโมเดล OpenAI ที่มีการเตรียมพร้อมสำหรับองค์กร
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) สำหรับโมเดลโอเพนซอร์สและเซิร์ฟเวอร์การประมวลผล

**คุณจะต้องใช้บัญชีของคุณเองสำหรับการฝึกปฏิบัติเหล่านี้** งานที่มอบหมายเป็นทางเลือกดังนั้นคุณสามารถเลือกที่จะตั้งค่าหนึ่งหรือทั้งหมด - หรือไม่มีเลย - ของผู้ให้บริการตามความสนใจของคุณ คำแนะนำบางส่วนสำหรับการสมัคร:

| การสมัคร | ค่าใช้จ่าย | API Key | Playground | ความคิดเห็น |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | มีโมเดลหลายแบบให้เลือก |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ต้องสมัครล่วงหน้าเพื่อเข้าถึง](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat มีโมเดลจำกัด](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ทำตามคำแนะนำด้านล่างเพื่อ _ตั้งค่า_ รีโพสิทอรีนี้สำหรับการใช้งานกับผู้ให้บริการที่แตกต่างกัน งานที่มอบหมายที่ต้องการผู้ให้บริการเฉพาะจะมีหนึ่งในแท็กเหล่านี้ในชื่อไฟล์:
- `aoai` - ต้องการ Azure OpenAI endpoint, key
- `oai` - ต้องการ OpenAI endpoint, key
- `hf` - ต้องการ Hugging Face token

คุณสามารถตั้งค่าหนึ่ง, ไม่มีเลย, หรือทั้งหมดของผู้ให้บริการ งานที่มอบหมายที่เกี่ยวข้องจะมีข้อผิดพลาดหากขาดข้อมูลรับรอง

### 2.1 สร้างไฟล์ `.env`

เราสมมติว่าคุณได้อ่านคำแนะนำข้างต้นและสมัครกับผู้ให้บริการที่เกี่ยวข้องและได้รับข้อมูลรับรองการตรวจสอบสิทธิ์ที่จำเป็น (API_KEY หรือ token) ในกรณีของ Azure OpenAI เราสมมติว่าคุณมีการใช้งาน Azure OpenAI Service (endpoint) ที่ถูกต้องพร้อมกับการใช้งานโมเดล GPT อย่างน้อยหนึ่งตัวสำหรับการสนทนา

ขั้นตอนต่อไปคือการตั้งค่า **ตัวแปรสภาพแวดล้อมท้องถิ่น** ของคุณดังนี้:

1. มองหาไฟล์ `.env.copy` ในโฟลเดอร์รูทซึ่งควรมีเนื้อหาดังนี้:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. คัดลอกไฟล์นั้นไปยัง `.env` โดยใช้คำสั่งด้านล่าง ไฟล์นี้จะ _gitignore-d_ เพื่อรักษาความลับให้ปลอดภัย

   ```bash
   cp .env.copy .env
   ```

3. กรอกค่าต่างๆ (แทนที่ตัวแทนทางขวาของ `=`) ตามที่อธิบายไว้ในส่วนถัดไป

3. (ตัวเลือก) หากคุณใช้ GitHub Codespaces คุณมีตัวเลือกในการบันทึกตัวแปรสภาพแวดล้อมเป็น _Codespaces secrets_ ที่เกี่ยวข้องกับรีโพสิทอรีนี้ ในกรณีนั้นคุณไม่จำเป็นต้องตั้งค่าไฟล์ .env ท้องถิ่น **อย่างไรก็ตาม โปรดทราบว่าตัวเลือกนี้ใช้ได้เฉพาะหากคุณใช้ GitHub Codespaces เท่านั้น** คุณยังคงต้องตั้งค่าไฟล์ .env หากคุณใช้ Docker Desktop แทน

### 2.2 กรอกไฟล์ `.env`

มาดูชื่อของตัวแปรเพื่อทำความเข้าใจว่ามันแทนอะไร:

| ตัวแปร | คำอธิบาย |
| :--- | :--- |
| HUGGING_FACE_API_KEY | นี่คือตัวเข้าถึงที่คุณตั้งค่าในโปรไฟล์ของคุณ |
| OPENAI_API_KEY | นี่คือคีย์การอนุญาตสำหรับการใช้บริการสำหรับ endpoint OpenAI ที่ไม่ใช่ Azure |
| AZURE_OPENAI_API_KEY | นี่คือคีย์การอนุญาตสำหรับการใช้บริการนั้น |
| AZURE_OPENAI_ENDPOINT | นี่คือ endpoint ที่ใช้งานสำหรับทรัพยากร Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | นี่คือ endpoint การใช้งานโมเดล _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | นี่คือ endpoint การใช้งานโมเดล _text embeddings_ |
| | |

หมายเหตุ: ตัวแปร Azure OpenAI สองตัวสุดท้ายสะท้อนโมเดลค่าเริ่มต้นสำหรับการสนทนา (text generation) และการค้นหาเวกเตอร์ (embeddings) ตามลำดับ คำแนะนำสำหรับการตั้งค่าจะถูกกำหนดในงานที่มอบหมายที่เกี่ยวข้อง

### 2.3 ตั้งค่า Azure: จากพอร์ทัล

ค่า endpoint และ key ของ Azure OpenAI จะพบได้ใน [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ดังนั้นให้เริ่มที่นั่น

1. ไปที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. คลิกตัวเลือก **Keys and Endpoint** ในแถบด้านข้าง (เมนูทางซ้าย)
1. คลิก **Show Keys** - คุณควรเห็นดังนี้: KEY 1, KEY 2 และ Endpoint
1. ใช้ค่า KEY 1 สำหรับ AZURE_OPENAI_API_KEY
1. ใช้ค่า Endpoint สำหรับ AZURE_OPENAI_ENDPOINT

ต่อไป เราต้องการ endpoints สำหรับโมเดลเฉพาะที่เราได้ใช้งาน

1. คลิกตัวเลือก **Model deployments** ในแถบด้านข้าง (เมนูทางซ้าย) สำหรับทรัพยากร Azure OpenAI
1. ในหน้าปลายทาง คลิก **Manage Deployments**

สิ่งนี้จะนำคุณไปยังเว็บไซต์ Azure OpenAI Studio ซึ่งเราจะหาค่าอื่นๆ ตามที่อธิบายด้านล่าง

### 2.4 ตั้งค่า Azure: จาก Studio

1. ไปที่ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **จากทรัพยากรของคุณ** ตามที่อธิบายข้างต้น
1. คลิกแท็บ **Deployments** (แถบด้านข้าง, ซ้าย) เพื่อดูโมเดลที่ใช้งานอยู่ในปัจจุบัน
1. หากโมเดลที่คุณต้องการไม่ได้ใช้งาน ให้ใช้ **Create new deployment** เพื่อใช้งานมัน
1. คุณจะต้องมีโมเดล _text-generation_ - เราแนะนำ: **gpt-35-turbo**
1. คุณจะต้องมีโมเดล _text-embedding_ - เราแนะนำ **text-embedding-ada-002**

ตอนนี้อัปเดตตัวแปรสภาพแวดล้อมให้สะท้อนชื่อการใช้งาน _Deployment name_ ที่ใช้ ซึ่งจะเป็นชื่อเดียวกับชื่อโมเดลเว้นแต่คุณจะเปลี่ยนมันอย่างชัดเจน ดังนั้น ตัวอย่างเช่น คุณอาจมี:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**อย่าลืมบันทึกไฟล์ .env เมื่อเสร็จสิ้น** คุณสามารถออกจากไฟล์และกลับไปที่คำแนะนำสำหรับการรัน notebook ได้

### 2.5 ตั้งค่า OpenAI: จากโปรไฟล์

คุณสามารถหาคีย์ API ของ OpenAI ได้ใน [บัญชี OpenAI ของคุณ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) หากคุณไม่มี คุณสามารถสมัครบัญชีและสร้างคีย์ API ได้ เมื่อคุณมีคีย์แล้ว คุณสามารถใช้มันเพื่อเติมตัวแปร `OPENAI_API_KEY` ในไฟล์ `.env`

### 2.6 ตั้งค่า Hugging Face: จากโปรไฟล์

คุณสามารถหาตัวเข้าถึง Hugging Face ได้ในโปรไฟล์ของคุณภายใต้ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) อย่าโพสต์หรือแชร์สิ่งเหล่านี้ต่อสาธารณะ ให้สร้างตัวใหม่สำหรับการใช้งานโปรเจกต์นี้และคัดลอกไปยังไฟล์ `.env` ภายใต้ตัวแปร `HUGGING_FACE_API_KEY` _หมายเหตุ:_ นี่ไม่ใช่คีย์ API จริงๆ แต่ใช้สำหรับการตรวจสอบสิทธิ์ดังนั้นเราจึงรักษาการตั้งชื่อนี้เพื่อความสอดคล้องกัน

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาที่ใช้อยู่ควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้