<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:49:25+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "th"
}
-->
# ตั้งค่าสภาพแวดล้อมการพัฒนา

เราได้ตั้งค่าที่เก็บและคอร์สนี้ด้วย [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ที่มี Universal runtime ที่สามารถรองรับการพัฒนา Python3, .NET, Node.js และ Java การตั้งค่าที่เกี่ยวข้องถูกกำหนดไว้ในไฟล์ `devcontainer.json` ที่อยู่ในโฟลเดอร์ `.devcontainer/` ที่รากของที่เก็บนี้

เพื่อเปิดใช้งาน dev container ให้เปิดใน [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (สำหรับ runtime ที่โฮสต์บนคลาวด์) หรือใน [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (สำหรับ runtime ที่โฮสต์บนอุปกรณ์ท้องถิ่น) อ่าน [เอกสารนี้](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับวิธีการทำงานของ dev containers ภายใน VS Code

> [!TIP]  
> เราแนะนำให้ใช้ GitHub Codespaces สำหรับการเริ่มต้นอย่างรวดเร็วและง่ายดาย มันมี [โควต้าใช้งานฟรี](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ที่เพียงพอสำหรับบัญชีส่วนบุคคล ตั้งค่า [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อหยุดหรือลบ codespaces ที่ไม่ได้ใช้งานเพื่อเพิ่มประสิทธิภาพการใช้งานโควต้าของคุณ


## 1. การทำงานของการบ้าน

แต่ละบทเรียนจะมีการบ้าน _ตัวเลือก_ ที่อาจจะมีให้ในหนึ่งหรือมากกว่าหนึ่งภาษาโปรแกรมรวมถึง: Python, .NET/C#, Java และ JavaScript/TypeScript ส่วนนี้ให้คำแนะนำทั่วไปที่เกี่ยวข้องกับการทำงานของการบ้านเหล่านั้น

### 1.1 การบ้าน Python

การบ้าน Python จะมีให้ทั้งในรูปแบบแอปพลิเคชัน (ไฟล์ `.py`) หรือ Jupyter notebooks (ไฟล์ `.ipynb`)
- เพื่อรัน notebook ให้เปิดใน Visual Studio Code แล้วคลิก _Select Kernel_ (ที่มุมขวาบน) และเลือกตัวเลือก Python 3 ที่แสดงเป็นค่าเริ่มต้น จากนั้นคุณสามารถ _Run All_ เพื่อรัน notebook
- เพื่อรันแอปพลิเคชัน Python จาก command-line ให้ทำตามคำแนะนำเฉพาะของการบ้านเพื่อให้แน่ใจว่าคุณเลือกไฟล์ที่ถูกต้องและให้ argument ที่จำเป็น

## 2. การตั้งค่าผู้ให้บริการ

การบ้าน **อาจ** ถูกตั้งค่าให้ทำงานกับการปรับใช้ Large Language Model (LLM) หนึ่งหรือมากกว่าหนึ่งโดยผ่านผู้ให้บริการที่รองรับเช่น OpenAI, Azure หรือ Hugging Face ซึ่งจะให้ _hosted endpoint_ (API) ที่เราสามารถเข้าถึงโปรแกรมได้ด้วยข้อมูลรับรองที่ถูกต้อง (API key หรือ token) ในคอร์สนี้เราจะพูดถึงผู้ให้บริการเหล่านี้:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) พร้อมด้วยโมเดลหลากหลายรวมถึงซีรีส์ GPT หลัก
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) สำหรับโมเดล OpenAI ที่เน้นความพร้อมใช้งานในองค์กร
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) สำหรับโมเดลโอเพ่นซอร์สและเซิร์ฟเวอร์การอนุมาน

**คุณจะต้องใช้บัญชีของคุณเองสำหรับการฝึกฝนเหล่านี้** การบ้านเป็นตัวเลือกดังนั้นคุณสามารถเลือกที่จะตั้งค่าหนึ่ง, ทั้งหมด - หรือไม่มี - ผู้ให้บริการตามความสนใจของคุณ คำแนะนำบางส่วนสำหรับการสมัคร:

| สมัคร | ค่าใช้จ่าย | API Key | Playground | ความคิดเห็น |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | มีหลายโมเดลให้เลือก |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ต้องสมัครล่วงหน้าเพื่อเข้าถึง](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat มีโมเดลจำกัด](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ทำตามคำแนะนำด้านล่างเพื่อ _ตั้งค่า_ ที่เก็บนี้สำหรับการใช้งานกับผู้ให้บริการที่แตกต่างกัน การบ้านที่ต้องการผู้ให้บริการเฉพาะจะมีหนึ่งในแท็กเหล่านี้ในชื่อไฟล์:
 - `aoai` - ต้องการ Azure OpenAI endpoint, key
 - `oai` - ต้องการ OpenAI endpoint, key
 - `hf` - ต้องการ Hugging Face token

คุณสามารถตั้งค่าหนึ่ง, ไม่มี, หรือทั้งหมดผู้ให้บริการ การบ้านที่เกี่ยวข้องจะเกิดข้อผิดพลาดเมื่อไม่มีข้อมูลรับรอง

### 2.1 สร้างไฟล์ `.env`

เราสันนิษฐานว่าคุณได้อ่านคำแนะนำข้างต้นและสมัครกับผู้ให้บริการที่เกี่ยวข้องแล้ว และได้รับข้อมูลรับรองการตรวจสอบสิทธิ์ที่จำเป็น (API_KEY หรือ token) ในกรณีของ Azure OpenAI เราสันนิษฐานว่าคุณมีการปรับใช้ Azure OpenAI Service (endpoint) ที่ถูกต้องพร้อมกับโมเดล GPT อย่างน้อยหนึ่งตัวที่ปรับใช้สำหรับการเติมเต็มการสนทนา

ขั้นตอนต่อไปคือการตั้งค่าตัวแปรสภาพแวดล้อม **ท้องถิ่น** ของคุณดังนี้:


1. ดูในโฟลเดอร์รากสำหรับไฟล์ `.env.copy` ที่ควรมีเนื้อหาเช่นนี้:

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

2. คัดลอกไฟล์นั้นไปยัง `.env` โดยใช้คำสั่งด้านล่าง ไฟล์นี้ถูก _gitignore-d_ เพื่อเก็บความลับให้ปลอดภัย

   ```bash
   cp .env.copy .env
   ```

3. เติมค่า (แทนที่ตัวแทนทางด้านขวาของ `=`) ตามที่อธิบายในส่วนถัดไป

3. (ตัวเลือก) หากคุณใช้ GitHub Codespaces คุณมีตัวเลือกในการบันทึกตัวแปรสภาพแวดล้อมเป็น _Codespaces secrets_ ที่เกี่ยวข้องกับที่เก็บนี้ ในกรณีนั้นคุณไม่จำเป็นต้องตั้งค่าไฟล์ .env ท้องถิ่น **อย่างไรก็ตาม โปรดทราบว่าตัวเลือกนี้ใช้งานได้เฉพาะเมื่อคุณใช้ GitHub Codespaces** คุณยังคงต้องตั้งค่าไฟล์ .env หากคุณใช้ Docker Desktop แทน


### 2.2 เติมไฟล์ `.env`

มาดูชื่อของตัวแปรเพื่อเข้าใจว่าพวกมันแสดงถึงอะไร:

| ตัวแปร  | คำอธิบาย  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | นี่คือตัวเข้าถึงที่คุณตั้งค่าในโปรไฟล์ของคุณ |
| OPENAI_API_KEY | นี่คือคีย์การตรวจสอบสิทธิ์สำหรับการใช้บริการสำหรับ endpoint ที่ไม่ใช่ Azure OpenAI |
| AZURE_OPENAI_API_KEY | นี่คือคีย์การตรวจสอบสิทธิ์สำหรับการใช้บริการนั้น |
| AZURE_OPENAI_ENDPOINT | นี่คือ endpoint ที่ปรับใช้สำหรับทรัพยากร Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | นี่คือ endpoint การปรับใช้โมเดล _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | นี่คือ endpoint การปรับใช้โมเดล _text embeddings_ |
| | |

หมายเหตุ: ตัวแปร Azure OpenAI สองตัวสุดท้ายสะท้อนถึงโมเดลเริ่มต้นสำหรับการเติมเต็มการสนทนา (text generation) และการค้นหาเวกเตอร์ (embeddings) ตามลำดับ คำแนะนำสำหรับการตั้งค่าจะถูกกำหนดในการบ้านที่เกี่ยวข้อง


### 2.3 ตั้งค่า Azure: จาก Portal

ค่าของ endpoint และ key ของ Azure OpenAI จะพบได้ใน [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ดังนั้นเรามาเริ่มที่นี่

1. ไปที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. คลิกที่ตัวเลือก **Keys and Endpoint** ในแถบด้านข้าง (เมนูด้านซ้าย)
1. คลิก **Show Keys** - คุณควรเห็นดังนี้: KEY 1, KEY 2 และ Endpoint
1. ใช้ค่าของ KEY 1 สำหรับ AZURE_OPENAI_API_KEY
1. ใช้ค่าของ Endpoint สำหรับ AZURE_OPENAI_ENDPOINT

ถัดไป เราต้องการ endpoints สำหรับโมเดลเฉพาะที่เราได้ปรับใช้

1. คลิกที่ตัวเลือก **Model deployments** ในแถบด้านข้าง (เมนูด้านซ้าย) สำหรับทรัพยากร Azure OpenAI
1. ในหน้าปลายทาง คลิก **Manage Deployments**

นี่จะพาคุณไปที่เว็บไซต์ Azure OpenAI Studio ซึ่งเราจะพบค่าที่เหลือดังที่อธิบายด้านล่าง

### 2.4 ตั้งค่า Azure: จาก Studio

1. ไปที่ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **จากทรัพยากรของคุณ** ตามที่อธิบายด้านบน
1. คลิกที่แท็บ **Deployments** (แถบด้านข้าง, ซ้าย) เพื่อดูโมเดลที่ปรับใช้ปัจจุบัน
1. หากโมเดลที่คุณต้องการไม่ได้ปรับใช้ ใช้ **Create new deployment** เพื่อปรับใช้มัน
1. คุณจะต้องการโมเดล _text-generation_ - เราแนะนำ: **gpt-35-turbo**
1. คุณจะต้องการโมเดล _text-embedding_ - เราแนะนำ **text-embedding-ada-002**

ตอนนี้อัปเดตตัวแปรสภาพแวดล้อมให้สะท้อนถึง _ชื่อการปรับใช้_ ที่ใช้ โดยปกติจะเป็นชื่อเดียวกับโมเดลเว้นแต่คุณจะเปลี่ยนมันอย่างชัดเจน ดังนั้นเป็นตัวอย่าง คุณอาจมี:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**อย่าลืมบันทึกไฟล์ .env เมื่อเสร็จสิ้น** คุณสามารถออกจากไฟล์และกลับไปยังคำแนะนำสำหรับการรัน notebook

### 2.5 ตั้งค่า OpenAI: จากโปรไฟล์

คีย์ API ของ OpenAI ของคุณสามารถพบได้ใน [บัญชี OpenAI ของคุณ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) หากคุณไม่มี คุณสามารถสมัครบัญชีและสร้างคีย์ API เมื่อคุณมีคีย์แล้ว คุณสามารถใช้มันเพื่อเติมตัวแปร `OPENAI_API_KEY` ในไฟล์ `.env`

### 2.6 ตั้งค่า Hugging Face: จากโปรไฟล์

token ของ Hugging Face ของคุณสามารถพบได้ในโปรไฟล์ของคุณภายใต้ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) อย่าโพสต์หรือแชร์พวกมันในที่สาธารณะ ให้สร้าง token ใหม่สำหรับการใช้งานโปรเจ็กต์นี้และคัดลอกนั้นไปยังไฟล์ `.env` ภายใต้ตัวแปร `HUGGING_FACE_API_KEY` _หมายเหตุ:_ นี่ไม่ใช่คีย์ API โดยเทคนิค แต่ถูกใช้สำหรับการตรวจสอบสิทธิ์ดังนั้นเราจึงคงชื่อแบบนั้นเพื่อความสอดคล้อง

**คำปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้เกิดความถูกต้องแม่นยำ แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดอันเกิดจากการใช้การแปลนี้