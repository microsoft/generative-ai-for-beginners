<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:07:13+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "th"
}
-->
# การเลือกและตั้งค่า LLM Provider 🔑

โจทย์ **อาจ** ถูกตั้งค่าให้ใช้งานกับการ Deploy Large Language Model (LLM) ผ่านผู้ให้บริการที่รองรับ เช่น OpenAI, Azure หรือ Hugging Face ซึ่งจะมี _hosted endpoint_ (API) ที่เราสามารถเข้าถึงได้ด้วยข้อมูลรับรองที่ถูกต้อง (API key หรือ token) ในคอร์สนี้ เราจะพูดถึงผู้ให้บริการเหล่านี้:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ที่มีโมเดลหลากหลาย รวมถึงซีรีส์ GPT หลัก
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) สำหรับโมเดล OpenAI ที่เน้นความพร้อมใช้งานในองค์กร
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) สำหรับโมเดลโอเพ่นซอร์สและ inference server

**คุณต้องใช้บัญชีของตัวเองสำหรับแบบฝึกหัดเหล่านี้** โจทย์เป็นทางเลือก คุณสามารถเลือกตั้งค่าผู้ให้บริการหนึ่งราย หลายราย หรือไม่ตั้งค่าเลยก็ได้ ขึ้นอยู่กับความสนใจของคุณ คำแนะนำสำหรับการสมัคร:

| สมัคร | ค่าใช้จ่าย | API Key | Playground | หมายเหตุ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ราคาค่าใช้บริการ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [แบบ Project](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | มีโมเดลให้เลือกหลายแบบ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ราคาค่าใช้บริการ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ต้องสมัครขอใช้งานล่วงหน้า](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ราคาค่าใช้บริการ](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat มีโมเดลให้เลือกจำกัด](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ทำตามขั้นตอนด้านล่างเพื่อ _ตั้งค่า_ repository นี้ให้ใช้งานกับผู้ให้บริการต่าง ๆ โจทย์ที่ต้องการผู้ให้บริการเฉพาะจะมี tag เหล่านี้ในชื่อไฟล์:

- `aoai` - ต้องใช้ Azure OpenAI endpoint และ key
- `oai` - ต้องใช้ OpenAI endpoint และ key
- `hf` - ต้องใช้ Hugging Face token

คุณจะตั้งค่าผู้ให้บริการหนึ่งราย ไม่ตั้งค่า หรือทุกเจ้าเลยก็ได้ โจทย์ที่เกี่ยวข้องจะ error หากไม่มีข้อมูลรับรอง

## สร้างไฟล์ `.env`

เราถือว่าคุณได้อ่านคำแนะนำข้างต้นและสมัครกับผู้ให้บริการที่เกี่ยวข้อง พร้อมรับข้อมูลรับรองสำหรับการยืนยันตัวตน (API_KEY หรือ token) ในกรณี Azure OpenAI เราถือว่าคุณมีการ deploy Azure OpenAI Service (endpoint) ที่มีอย่างน้อยหนึ่ง GPT model สำหรับ chat completion แล้ว

ขั้นตอนถัดไปคือการตั้งค่า **local environment variables** ตามนี้:

1. ดูในโฟลเดอร์หลัก จะมีไฟล์ `.env.copy` ที่มีเนื้อหาแบบนี้:

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

2. คัดลอกไฟล์นั้นเป็น `.env` ด้วยคำสั่งด้านล่าง ไฟล์นี้จะถูก _gitignore_ เพื่อป้องกันข้อมูลลับรั่วไหล

   ```bash
   cp .env.copy .env
   ```

3. กรอกค่า (แทนที่ placeholder ด้านขวาของ `=`) ตามที่อธิบายในหัวข้อถัดไป

4. (ทางเลือก) ถ้าใช้ GitHub Codespaces คุณสามารถบันทึก environment variables เป็น _Codespaces secrets_ ที่ผูกกับ repository นี้ได้ กรณีนี้คุณไม่ต้องตั้งค่าไฟล์ .env ในเครื่อง **แต่โปรดทราบว่าทางเลือกนี้ใช้ได้เฉพาะกับ GitHub Codespaces เท่านั้น** ถ้าใช้ Docker Desktop ยังต้องตั้งค่าไฟล์ .env เหมือนเดิม

## กรอกข้อมูลในไฟล์ `.env`

มาดูชื่อของตัวแปรแต่ละตัวเพื่อเข้าใจความหมายกัน:

| ตัวแปร  | คำอธิบาย  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | คือ access token ที่คุณตั้งค่าในโปรไฟล์ |
| OPENAI_API_KEY | คือ authorization key สำหรับใช้บริการ OpenAI (ที่ไม่ใช่ Azure) |
| AZURE_OPENAI_API_KEY | คือ authorization key สำหรับใช้บริการนี้ |
| AZURE_OPENAI_ENDPOINT | คือ endpoint ที่ deploy สำหรับ Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | คือ endpoint สำหรับโมเดล _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | คือ endpoint สำหรับโมเดล _text embeddings_ |
| | |

หมายเหตุ: ตัวแปรสองตัวสุดท้ายของ Azure OpenAI จะเป็นโมเดลเริ่มต้นสำหรับ chat completion (text generation) และ vector search (embeddings) ตามลำดับ วิธีการตั้งค่าจะอธิบายในโจทย์ที่เกี่ยวข้อง

## ตั้งค่า Azure: จาก Portal

ค่า endpoint และ key ของ Azure OpenAI จะหาได้จาก [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ดังนั้นเริ่มจากตรงนี้

1. ไปที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. คลิกที่ตัวเลือก **Keys and Endpoint** ใน sidebar (เมนูด้านซ้าย)
1. คลิก **Show Keys** - จะเห็น KEY 1, KEY 2 และ Endpoint
1. ใช้ค่า KEY 1 สำหรับ AZURE_OPENAI_API_KEY
1. ใช้ค่า Endpoint สำหรับ AZURE_OPENAI_ENDPOINT

ถัดไป เราต้องการ endpoint สำหรับโมเดลที่เรา deploy

1. คลิกที่ตัวเลือก **Model deployments** ใน sidebar (เมนูซ้าย) ของ Azure OpenAI resource
1. ในหน้าที่ไปถึง คลิก **Manage Deployments**

จะนำคุณไปที่เว็บไซต์ Azure OpenAI Studio ซึ่งจะหา value อื่น ๆ ตามที่อธิบายด้านล่าง

## ตั้งค่า Azure: จาก Studio

1. ไปที่ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **จาก resource ของคุณ** ตามที่อธิบายข้างบน
1. คลิกที่แท็บ **Deployments** (sidebar ซ้าย) เพื่อดูโมเดลที่ deploy อยู่
1. ถ้าโมเดลที่ต้องการยังไม่ได้ deploy ให้ใช้ **Create new deployment** เพื่อ deploy
1. คุณต้องมีโมเดล _text-generation_ - แนะนำ: **gpt-35-turbo**
1. คุณต้องมีโมเดล _text-embedding_ - แนะนำ **text-embedding-ada-002**

จากนั้นอัปเดต environment variables ให้ตรงกับ _Deployment name_ ที่ใช้ ซึ่งโดยปกติจะตรงกับชื่อโมเดลถ้าไม่ได้เปลี่ยนชื่อเอง ตัวอย่างเช่น คุณอาจมี:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**อย่าลืมบันทึกไฟล์ .env เมื่อกรอกข้อมูลเสร็จ** จากนั้นออกจากไฟล์และกลับไปทำตามคำแนะนำสำหรับรัน notebook

## ตั้งค่า OpenAI: จากโปรไฟล์

API key ของ OpenAI จะหาได้ใน [บัญชี OpenAI ของคุณ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ถ้ายังไม่มี ให้สมัครบัญชีและสร้าง API key เมื่อได้ key แล้ว ให้นำไปกรอกในตัวแปร `OPENAI_API_KEY` ในไฟล์ `.env`

## ตั้งค่า Hugging Face: จากโปรไฟล์

Token ของ Hugging Face จะหาได้ในโปรไฟล์ที่ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) อย่าโพสต์หรือแชร์ token นี้สาธารณะ ให้สร้าง token ใหม่สำหรับโปรเจกต์นี้และคัดลอกไปใส่ในไฟล์ `.env` ที่ตัวแปร `HUGGING_FACE_API_KEY` _หมายเหตุ:_ จริง ๆ แล้วนี่ไม่ใช่ API key แต่ใช้สำหรับ authentication ดังนั้นจึงใช้ชื่อแบบนี้เพื่อความสอดคล้อง

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้