# การเลือกและการกำหนดค่าผู้ให้บริการ LLM 🔑

การบ้าน **อาจ** ถูกตั้งค่าให้ทำงานร่วมกับการปรับใช้ Large Language Model (LLM) หนึ่งหรือหลายตัวผ่านผู้ให้บริการที่รองรับ เช่น OpenAI, Azure หรือ Hugging Face ซึ่งให้ _โฮสต์เอนด์พอยต์_ (API) ที่เราสามารถเข้าถึงได้แบบโปรแกรมโดยใช้ข้อมูลรับรองที่ถูกต้อง (API key หรือ token) ในหลักสูตรนี้ เราจะพูดถึงผู้ให้บริการเหล่านี้:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) พร้อมกับโมเดลที่หลากหลายรวมถึงซีรีส์ GPT หลัก
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) สำหรับโมเดล OpenAI ที่มุ่งเน้นการพร้อมใช้งานระดับองค์กร
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) สำหรับเอนด์พอยต์และ API key เดียวเพื่อเข้าถึงโมเดลนับร้อยจาก OpenAI, Meta, Mistral, Cohere, Microsoft และอื่น ๆ (แทนที่ GitHub Models ซึ่งจะเลิกใช้สิ้นสุดเดือนกรกฎาคม 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) สำหรับโมเดลโอเพนซอร์สและเซิร์ฟเวอร์อินเฟอเรนซ์
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) หรือ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) หากคุณต้องการรันโมเดลแบบออฟไลน์เต็มรูปแบบบนอุปกรณ์ของคุณเองโดยไม่ต้องใช้การสมัครคลาวด์

**คุณจะต้องใช้บัญชีของคุณเองสำหรับแบบฝึกหัดเหล่านี้** การบ้านเป็นทางเลือกดังนั้นคุณสามารถเลือกตั้งค่าแค่หนึ่ง, ทั้งหมด หรือไม่มีเลยก็ได้ตามความสนใจของคุณ คู่มือสำหรับการสมัครสมาชิก:

| สมัครสมาชิก | ค่าใช้จ่าย | API Key | Playground | ความคิดเห็น |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ราคา](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ตามโปรเจกต์](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, เว็บ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | มีโมเดลหลากหลาย |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ราคา](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [เริ่มต้นใช้งาน SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [เริ่มต้นใช้งาน Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [ต้องสมัครล่วงหน้าเพื่อรับสิทธิ์](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ราคา](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [หน้าภาพรวมโปรเจกต์](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | มีชั้นฟรี ให้เอนด์พอยต์ + key เดียวสำหรับผู้ให้บริการโมเดลหลายราย |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ราคา](https://huggingface.co/pricing) | [โทเค็นเข้าถึง](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat มีโมเดลจำกัด](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ฟรี (รันบนอุปกรณ์ของคุณ) | ไม่ต้องใช้ | [CLI/SDK ท้องถิ่น](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ออฟไลน์เต็มที่, เอนด์พอยต์เข้ากันได้กับ OpenAI |
| | | | | |

ทำตามคำแนะนำด้านล่างเพื่อ _กำหนดค่า_ รีโพซิทอรีนี้สำหรับใช้กับผู้ให้บริการต่าง ๆ การบ้านที่ต้องใช้ผู้ให้บริการเฉพาะจะมีแท็กเหล่านี้ในชื่อไฟล์:

- `aoai` - ต้องใช้ Azure OpenAI เอนด์พอยต์, key
- `oai` - ต้องใช้ OpenAI เอนด์พอยต์, key
- `hf` - ต้องใช้โทเค็น Hugging Face
- `githubmodels` - ต้องใช้ Microsoft Foundry Models เอนด์พอยต์, key (GitHub Models จะเลิกใช้สิ้นเดือนกรกฎาคม 2026)

คุณสามารถกำหนดค่าได้หนึ่ง, ไม่มี หรือทุกผู้ให้บริการ งานที่เกี่ยวข้องจะเกิดข้อผิดพลาดหากขาดข้อมูลรับรอง

## สร้างไฟล์ `.env`

เราสมมติว่าคุณได้อ่านคำแนะนำข้างต้นและสมัครสมาชิกกับผู้ให้บริการที่เกี่ยวข้องแล้ว พร้อมได้รับข้อมูลรับรองการพิสูจน์ตัวตนที่จำเป็น (API_KEY หรือ token) สำหรับ Azure OpenAI เราสมมติว่าคุณยังมีการปรับใช้ Azure OpenAI Service (เอนด์พอยต์) ที่ถูกต้องโดยมีโมเดล GPT อย่างน้อยหนึ่งโมเดลสำหรับการสนทนา

ขั้นตอนต่อไปคือการกำหนดค่า **ตัวแปรสภาพแวดล้อมท้องถิ่น** ของคุณดังนี้:

1. มองหาไฟล์ `.env.copy` ในโฟลเดอร์หลัก ซึ่งจะมีเนื้อหาเช่นนี้:

   ```bash
   # ผู้ให้บริการ OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI ใน Microsoft Foundry
   ## (บริการ Azure OpenAI ตอนนี้เป็นส่วนหนึ่งของ Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ตั้งค่าเริ่มต้นแล้ว! (เวอร์ชัน API ที่เสถียร GA ปัจจุบัน)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## โมเดล Microsoft Foundry (แคตตาล็อกโมเดลจากหลายผู้ให้บริการ แทนที่ GitHub Models ที่จะเลิกใช้งานสิ้นเดือนกรกฎาคม 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. คัดลอกไฟล์นั้นเป็น `.env` โดยใช้คำสั่งด้านล่าง ไฟล์นี้จะถูก _gitignore_ เพื่อรักษาความลับให้ปลอดภัย

   ```bash
   cp .env.copy .env
   ```

3. กรอกค่า (แทนที่ตัวแทนที่อยู่ทางขวาของ `=`) ตามที่อธิบายในส่วนถัดไป

4. (ตัวเลือก) หากคุณใช้ GitHub Codespaces คุณสามารถเลือกบันทึกตัวแปรสภาพแวดล้อมเป็น _Codespaces secrets_ ที่เกี่ยวข้องกับรีโพซิทอรีนี้ ในกรณีนั้น คุณไม่จำเป็นต้องตั้งค่าไฟล์ .env ท้องถิ่น แต่โปรดทราบว่า ตัวเลือกนี้ใช้งานได้เฉพาะหากคุณใช้ GitHub Codespaces เท่านั้น คุณยังคงต้องตั้งค่าไฟล์ .env หากใช้ Docker Desktop แทน

## เติมไฟล์ `.env`

มาดูชื่อของตัวแปรเพื่อเข้าใจว่ามีความหมายอย่างไร:

| ตัวแปร  | คำอธิบาย  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | นี่คือโทเค็นเข้าถึงของผู้ใช้ที่คุณตั้งค่าในโปรไฟล์ของคุณ |
| OPENAI_API_KEY | นี่คือคีย์อนุญาตสำหรับใช้บริการสำหรับเอนด์พอยต์ OpenAI ที่ไม่ใช่ Azure |
| AZURE_OPENAI_API_KEY | นี่คือคีย์อนุญาตสำหรับใช้บริการนั้น |
| AZURE_OPENAI_ENDPOINT | นี่คือเอนด์พอยต์ที่ปรับใช้สำหรับทรัพยากร Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | นี่คือเอนด์พอยต์การปรับใช้โมเดล _สร้างข้อความ_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | นี่คือเอนด์พอยต์การปรับใช้โมเดล _ข้อความฝังตัว_ |
| AZURE_INFERENCE_ENDPOINT | นี่คือเอนด์พอยต์ของโปรเจกต์ Microsoft Foundry ของคุณ ใช้กับ Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | นี่คือ API key สำหรับโปรเจกต์ Microsoft Foundry ของคุณ |
| | |

หมายเหตุ: ตัวแปร Azure OpenAI สองตัวสุดท้ายสะท้อนโมเดลเริ่มต้นสำหรับการสนทนา (สร้างข้อความ) และค้นหาแบบเวกเตอร์ (ฝังตัว) ตามลำดับ คำแนะนำในการตั้งค่าจะระบุในงานที่เกี่ยวข้อง

## กำหนดค่า Azure OpenAI: จากพอร์ทัล

> **หมายเหตุ:** บริการ Azure OpenAI ตอนนี้เป็นส่วนหนึ่งของ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ทรัพยากรและการปรับใช้ยังคงแสดงใน Azure Portal แต่การจัดการโมเดลในชีวิตประจำวัน (การปรับใช้, playground, การตรวจสอบ) จะดำเนินการในพอร์ทัล Foundry แทน "Azure OpenAI Studio" แบบเดิมแยกออกมาต่างหาก

ค่าของ Azure OpenAI เอนด์พอยต์และคีย์จะพบได้ที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ดังนั้นให้เริ่มจากตรงนั้น

1. ไปที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. คลิกตัวเลือก **Keys and Endpoint** ในแถบด้านข้าง (เมนูซ้าย)
1. คลิก **Show Keys** - คุณจะเห็นดังนี้: KEY 1, KEY 2 และ Endpoint
1. ใช้ค่า KEY 1 สำหรับ AZURE_OPENAI_API_KEY
1. ใช้ค่าของ Endpoint สำหรับ AZURE_OPENAI_ENDPOINT

ต่อไป เราต้องการเอนด์พอยต์สำหรับโมเดลที่เราปรับใช้เฉพาะ

1. คลิกตัวเลือก **Model deployments** ในแถบด้านข้าง (เมนูซ้าย) สำหรับทรัพยากร Azure OpenAI
1. ในหน้าปลายทาง คลิก **Go to Microsoft Foundry portal** (หรือตัวเลือก **Manage Deployments** ขึ้นอยู่กับประเภททรัพยากรของคุณ)

นี่จะนำคุณไปที่พอร์ทัล Microsoft Foundry ซึ่งเราจะหาค่าที่เหลือตามที่อธิบายไว้ด้านล่าง

## กำหนดค่า Azure OpenAI: จากพอร์ทัล Microsoft Foundry

1. ไปที่ [พอร์ทัล Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **จากทรัพยากรของคุณ** ตามที่อธิบายไว้ข้างต้น
1. คลิกแท็บ **Deployments** (แถบด้านข้าง ซ้าย) เพื่อดูโมเดลที่ปรับใช้ในปัจจุบัน
1. ถ้าโมเดลที่ต้องการยังไม่ถูกปรับใช้ ให้ใช้ **Deploy model** เพื่อปรับใช้จาก [แค็ตตาล็อกโมเดล](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)
1. คุณจะต้องมีโมเดล _สร้างข้อความ_ — เราแนะนำ **gpt-4o-mini**
1. คุณจะต้องมีโมเดล _ฝังตัวข้อความ_ — เราแนะนำ **text-embedding-3-small**

ตอนนี้อัปเดตตัวแปรสภาพแวดล้อมให้สะท้อน _ชื่อการปรับใช้_ ที่ใช้ โดยทั่วไปจะเป็นชื่อเดียวกับชื่อโมเดลเว้นแต่คุณเปลี่ยนแปลงเอง เช่น ตัวอย่างเช่น คุณอาจมี:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**อย่าลืมบันทึกไฟล์ .env เมื่อทำเสร็จ** คุณสามารถออกจากไฟล์และกลับไปยังคำแนะนำสำหรับการรันโน้ตบุ๊กได้

## กำหนดค่า OpenAI: จากโปรไฟล์

คุณสามารถค้นหา API key ของ OpenAI ได้ใน [บัญชี OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ของคุณ หากยังไม่มี คุณสามารถสมัครบัญชีและสร้าง API key ได้ เมื่อคุณมีคีย์แล้ว คุณสามารถใช้เพื่อกรอกตัวแปร `OPENAI_API_KEY` ในไฟล์ `.env`

## กำหนดค่า Hugging Face: จากโปรไฟล์

โทเค็น Hugging Face ของคุณจะพบได้ในโปรไฟล์ของคุณภายใต้ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) อย่าโพสต์หรือแชร์โดยสาธารณะ ให้สร้างโทเค็นใหม่สำหรับการใช้งานโปรเจกต์นี้และคัดลอกมาใส่ไฟล์ `.env` ในตัวแปร `HUGGING_FACE_API_KEY` _หมายเหตุ:_ นี่ไม่ใช่ API key ทางเทคนิค แต่ใช้สำหรับการพิสูจน์ตัวตน จึงใช้ชื่อนี้เพื่อความสอดคล้อง

## กำหนดค่า Microsoft Foundry Models: จากพอร์ทัล

> **หมายเหตุ:** GitHub Models จะเลิกใช้สิ้นเดือนกรกฎาคม 2026 Microsoft Foundry Models เป็นตัวแทนโดยตรง โดยให้แค็ตตาล็อกโมเดลฟรีทดลองและประสบการณ์ Azure AI Inference SDK / OpenAI SDK เดียวกัน

1. ไปที่ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) และสร้าง (หรือเปิด) โปรเจกต์ Foundry
1. เรียกดู [แค็ตตาล็อกโมเดล](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) และปรับใช้โมเดล เช่น `gpt-4o-mini`
1. บนหน้าของโปรเจกต์ **ภาพรวม** คัดลอก **เอนด์พอยต์** และ **API key**
1. ใช้ค่าเอนด์พอยต์สำหรับ `AZURE_INFERENCE_ENDPOINT` และค่า key สำหรับ `AZURE_INFERENCE_CREDENTIAL` ในไฟล์ `.env` ของคุณ

## ผู้ให้บริการออฟไลน์/ท้องถิ่น

หากคุณไม่ต้องการใช้การสมัครคลาวด์เลย คุณสามารถรันโมเดลที่เข้ากันได้แบบโอเพนซอร์สตรงบนอุปกรณ์ของคุณ:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - รันไทม์บนอุปกรณ์ของ Microsoft เลือกผู้ให้บริการดำเนินการที่ดีที่สุดโดยอัตโนมัติ (NPU, GPU หรือ CPU) และเผยเอนด์พอยต์ที่เข้ากันได้กับ OpenAI ซึ่งคุณสามารถใช้โค้ดตัวอย่างส่วนใหญ่ในหลักสูตรนี้ซ้ำได้โดยแทบไม่ต้องแก้ไข ดู [เอกสาร Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) เพื่อเริ่มต้น หรือติดตั้งด้วย `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS)
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - ทางเลือกยอดนิยมสำหรับการรันโมเดลโอเพนเช่น Llama, Phi, Mistral และ Gemma บนเครื่องท้องถิ่น


ดู [บทเรียนที่ 19: การสร้างด้วย SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) สำหรับตัวอย่างปฏิบัติที่ใช้ทั้งสองตัวเลือก

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->