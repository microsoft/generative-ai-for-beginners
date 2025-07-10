<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:30:45+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "th"
}
-->
# ตั้งค่าสภาพแวดล้อมสำหรับนักพัฒนา

เราตั้งค่าที่เก็บนี้และคอร์สด้วย [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ที่มี Universal runtime รองรับการพัฒนา Python3, .NET, Node.js และ Java การตั้งค่าที่เกี่ยวข้องถูกกำหนดไว้ในไฟล์ `devcontainer.json` ซึ่งอยู่ในโฟลเดอร์ `.devcontainer/` ที่รูทของที่เก็บนี้

เพื่อเปิดใช้งาน dev container ให้เปิดใน [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (สำหรับ runtime ที่โฮสต์บนคลาวด์) หรือใน [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (สำหรับ runtime ที่โฮสต์บนเครื่องท้องถิ่น) อ่าน [เอกสารนี้](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) เพื่อดูรายละเอียดเพิ่มเติมเกี่ยวกับการทำงานของ dev containers ใน VS Code  

> [!TIP]  
> เราแนะนำให้ใช้ GitHub Codespaces เพื่อเริ่มต้นอย่างรวดเร็วและง่ายดาย โดยมี [โควต้าการใช้งานฟรี](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ที่มากพอสำหรับบัญชีส่วนตัว ตั้งค่า [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อหยุดหรือยกเลิก codespaces ที่ไม่ใช้งาน เพื่อใช้โควต้าให้คุ้มค่าที่สุด


## 1. การรันงานที่ได้รับมอบหมาย

แต่ละบทเรียนจะมีงานที่ _ไม่บังคับ_ ซึ่งอาจมีให้ในหนึ่งหรือหลายภาษาโปรแกรม เช่น Python, .NET/C#, Java และ JavaScript/TypeScript ส่วนนี้ให้คำแนะนำทั่วไปเกี่ยวกับการรันงานเหล่านั้น

### 1.1 งาน Python

งาน Python จะมีให้ในรูปแบบแอปพลิเคชัน (`.py` ไฟล์) หรือ Jupyter notebooks (`.ipynb` ไฟล์)  
- ในการรัน notebook ให้เปิดใน Visual Studio Code แล้วคลิก _Select Kernel_ (มุมบนขวา) และเลือกตัวเลือก Python 3 เริ่มต้น จากนั้นคุณสามารถ _Run All_ เพื่อรัน notebook ได้เลย  
- ในการรันแอป Python จาก command-line ให้ทำตามคำแนะนำเฉพาะของงานเพื่อเลือกไฟล์ที่ถูกต้องและใส่อาร์กิวเมนต์ที่จำเป็น

## 2. การตั้งค่าผู้ให้บริการ

งานที่ได้รับมอบหมาย **อาจ** ถูกตั้งค่าให้ทำงานกับการใช้งาน Large Language Model (LLM) ผ่านผู้ให้บริการที่รองรับ เช่น OpenAI, Azure หรือ Hugging Face ซึ่งให้ _hosted endpoint_ (API) ที่เราสามารถเข้าถึงได้โดยโปรแกรมด้วยข้อมูลรับรองที่ถูกต้อง (API key หรือ token) ในคอร์สนี้ เราจะพูดถึงผู้ให้บริการเหล่านี้:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ที่มีโมเดลหลากหลายรวมถึงซีรีส์ GPT หลัก
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) สำหรับโมเดล OpenAI ที่เน้นความพร้อมใช้งานในองค์กร
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) สำหรับโมเดลโอเพ่นซอร์สและ inference server

**คุณจะต้องใช้บัญชีของตัวเองสำหรับแบบฝึกหัดเหล่านี้** งานที่ได้รับมอบหมายเป็นแบบไม่บังคับ คุณสามารถเลือกตั้งค่าเพียงหนึ่ง รายการทั้งหมด หรือไม่ตั้งค่าเลยก็ได้ตามความสนใจ คำแนะนำสำหรับการสมัคร:

| สมัคร | ค่าใช้จ่าย | API Key | Playground | หมายเหตุ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ราคา](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ตามโปรเจกต์](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ไม่ต้องเขียนโค้ด, เว็บ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | มีโมเดลหลายตัวให้เลือก |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ราคา](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [เริ่มต้นด้วย SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [เริ่มต้นด้วย Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ต้องสมัครล่วงหน้าเพื่อขอสิทธิ์](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ราคา](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat มีโมเดลจำกัด](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ทำตามคำแนะนำด้านล่างเพื่อ _ตั้งค่า_ ที่เก็บนี้ให้ใช้งานกับผู้ให้บริการต่างๆ งานที่ต้องการผู้ให้บริการเฉพาะจะมีแท็กเหล่านี้ในชื่อไฟล์:
 - `aoai` - ต้องใช้ Azure OpenAI endpoint และ key
 - `oai` - ต้องใช้ OpenAI endpoint และ key
 - `hf` - ต้องใช้ Hugging Face token

คุณสามารถตั้งค่าได้หนึ่ง รายการทั้งหมด หรือไม่ตั้งค่าเลย งานที่เกี่ยวข้องจะเกิดข้อผิดพลาดหากขาดข้อมูลรับรอง

###  2.1. สร้างไฟล์ `.env`

เราสมมติว่าคุณได้อ่านคำแนะนำข้างต้นและสมัครผู้ให้บริการที่เกี่ยวข้องแล้ว พร้อมได้รับข้อมูลรับรองการยืนยันตัวตนที่จำเป็น (API_KEY หรือ token) สำหรับ Azure OpenAI เราสมมติว่าคุณมีการใช้งาน Azure OpenAI Service (endpoint) ที่ถูกตั้งค่าและมีโมเดล GPT อย่างน้อยหนึ่งตัวสำหรับ chat completion

ขั้นตอนถัดไปคือการตั้งค่า **ตัวแปรสภาพแวดล้อมในเครื่อง** ดังนี้:


1. มองหาไฟล์ `.env.copy` ในโฟลเดอร์รูท ซึ่งควรมีเนื้อหาประมาณนี้:

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

2. คัดลอกไฟล์นั้นเป็น `.env` โดยใช้คำสั่งด้านล่าง ไฟล์นี้จะถูก _gitignore_ เพื่อเก็บความลับให้ปลอดภัย

   ```bash
   cp .env.copy .env
   ```

3. กรอกค่าต่างๆ (แทนที่ตัวแทนที่อยู่ข้างขวาของ `=`) ตามที่อธิบายในส่วนถัดไป

3. (ตัวเลือก) หากคุณใช้ GitHub Codespaces คุณสามารถบันทึกตัวแปรสภาพแวดล้อมเป็น _Codespaces secrets_ ที่เชื่อมโยงกับที่เก็บนี้ได้ ในกรณีนั้นคุณไม่จำเป็นต้องตั้งค่าไฟล์ .env ในเครื่อง **แต่โปรดทราบว่าตัวเลือกนี้ใช้ได้เฉพาะกับ GitHub Codespaces เท่านั้น** หากใช้ Docker Desktop คุณยังต้องตั้งค่าไฟล์ .env ในเครื่องอยู่


### 2.2. กรอกข้อมูลในไฟล์ `.env`

มาดูชื่อของตัวแปรเพื่อเข้าใจว่ามีความหมายอย่างไร:

| ตัวแปร  | คำอธิบาย  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | คือ token การเข้าถึงของผู้ใช้ที่คุณตั้งค่าในโปรไฟล์ |
| OPENAI_API_KEY | คือคีย์อนุญาตสำหรับใช้บริการ OpenAI ที่ไม่ใช่ Azure |
| AZURE_OPENAI_API_KEY | คือคีย์อนุญาตสำหรับใช้บริการ Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | คือ endpoint ที่ถูก deploy สำหรับ Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | คือ endpoint สำหรับโมเดล _text generation_ ที่ deploy |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | คือ endpoint สำหรับโมเดล _text embeddings_ ที่ deploy |
| | |

หมายเหตุ: ตัวแปร Azure OpenAI สองตัวสุดท้ายนี้ใช้สำหรับโมเดลเริ่มต้นที่ใช้ในการ chat completion (text generation) และการค้นหาเวกเตอร์ (embeddings) ตามลำดับ คำแนะนำการตั้งค่าจะระบุไว้ในงานที่เกี่ยวข้อง


### 2.3 ตั้งค่า Azure: จาก Portal

ค่าของ Azure OpenAI endpoint และ key จะพบได้ใน [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ดังนั้นเริ่มต้นที่นั่น

1. ไปที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. คลิกที่ตัวเลือก **Keys and Endpoint** ในแถบเมนูด้านข้าง (เมนูซ้าย)
1. คลิก **Show Keys** - คุณจะเห็น KEY 1, KEY 2 และ Endpoint
1. ใช้ค่า KEY 1 สำหรับ AZURE_OPENAI_API_KEY
1. ใช้ค่า Endpoint สำหรับ AZURE_OPENAI_ENDPOINT

ถัดไป เราต้องการ endpoint สำหรับโมเดลที่เราติดตั้งไว้

1. คลิกตัวเลือก **Model deployments** ในแถบเมนูด้านข้าง (เมนูซ้าย) ของ Azure OpenAI resource
1. ในหน้าปลายทาง คลิก **Manage Deployments**

จะพาคุณไปยังเว็บไซต์ Azure OpenAI Studio ซึ่งเราจะหาค่าที่เหลือตามที่อธิบายด้านล่าง

### 2.4 ตั้งค่า Azure: จาก Studio

1. ไปที่ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **จาก resource ของคุณ** ตามที่อธิบายไว้ข้างต้น
1. คลิกแท็บ **Deployments** (แถบด้านข้างซ้าย) เพื่อดูโมเดลที่ติดตั้งอยู่ในปัจจุบัน
1. หากโมเดลที่ต้องการยังไม่ได้ติดตั้ง ให้ใช้ **Create new deployment** เพื่อติดตั้งโมเดลนั้น
1. คุณจะต้องมีโมเดล _text-generation_ — เราแนะนำ: **gpt-35-turbo**
1. คุณจะต้องมีโมเดล _text-embedding_ — เราแนะนำ **text-embedding-ada-002**

ตอนนี้อัปเดตตัวแปรสภาพแวดล้อมให้ตรงกับชื่อ _Deployment name_ ที่ใช้ โดยปกติจะเหมือนกับชื่อโมเดล เว้นแต่คุณจะเปลี่ยนชื่อเอง เช่น:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**อย่าลืมบันทึกไฟล์ .env เมื่อเสร็จแล้ว** คุณสามารถปิดไฟล์และกลับไปทำตามคำแนะนำสำหรับการรัน notebook ต่อได้

### 2.5 ตั้งค่า OpenAI: จากโปรไฟล์

คีย์ API ของ OpenAI ของคุณจะพบได้ใน [บัญชี OpenAI ของคุณ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) หากยังไม่มี คุณสามารถสมัครบัญชีและสร้าง API key ได้ เมื่อได้คีย์แล้ว ให้นำไปกรอกในตัวแปร `OPENAI_API_KEY` ในไฟล์ `.env`

### 2.6 ตั้งค่า Hugging Face: จากโปรไฟล์

token ของ Hugging Face จะพบได้ในโปรไฟล์ของคุณที่ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) อย่าโพสต์หรือแชร์ token เหล่านี้สู่สาธารณะ ให้สร้าง token ใหม่สำหรับใช้งานในโปรเจกต์นี้และคัดลอกไปใส่ในไฟล์ `.env` ในตัวแปร `HUGGING_FACE_API_KEY` _หมายเหตุ:_ นี่ไม่ใช่ API key จริงๆ แต่ใช้สำหรับการยืนยันตัวตน ดังนั้นจึงใช้ชื่อนี้เพื่อความสอดคล้องกัน

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้