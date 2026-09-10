# การเลือกและการกำหนดค่าโปรไวเดอร์ LLM 🔑

แบบฝึกหัด **อาจจะ** ถูกตั้งค่าให้ทำงานกับการปรับใช้ Large Language Model (LLM) หนึ่งตัวขึ้นไปผ่านโปรไวเดอร์บริการที่รองรับเช่น OpenAI, Azure หรือ Hugging Face ซึ่งโปรไวเดอร์เหล่านี้จัดเตรียม _endpoint โฮสต์_ (API) ที่เราสามารถเข้าถึงได้โดยโปรแกรมด้วยข้อมูลรับรองที่ถูกต้อง (API key หรือ token) ในคอร์สนี้ เราจะพูดถึงโปรไวเดอร์เหล่านี้:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) พร้อมโมเดลหลากหลายรวมถึงซีรีส์หลัก GPT
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) สำหรับโมเดล OpenAI ที่เน้นความพร้อมใช้งานในองค์กร
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) สำหรับ endpoint เดียวและ API key เพื่อเข้าถึงโมเดลนับร้อยจาก OpenAI, Meta, Mistral, Cohere, Microsoft และอื่น ๆ (แทนที่ GitHub Models ซึ่งจะยุติให้บริการในปลายเดือนกรกฎาคม 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) สำหรับโมเดลโอเพนซอร์สและเซิร์ฟเวอร์สืบค้น
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) หรือ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) หากคุณต้องการรันโมเดลแบบออฟไลน์เต็มรูปแบบบนอุปกรณ์ของคุณเองโดยไม่ต้องสมัครสมาชิกคลาวด์

**คุณจะต้องใช้บัญชีของคุณเองสำหรับแบบฝึกหัดเหล่านี้** แบบฝึกหัดเป็นทางเลือก ดังนั้นคุณสามารถเลือกตั้งค่าโปรไวเดอร์หนึ่งตัว ทั้งหมด หรือไม่มีเลย ตามความสนใจของคุณ แนะแนวสำหรับการสมัครใช้งาน:

| สมัครใช้ | ค่าใช้จ่าย | API Key | Playground | หมายเหตุ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [ราคาค่าบริการ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [โครงการเฉพาะ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [แบบไม่ต้องเขียนโค้ด, เว็บ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | มีโมเดลหลายตัวให้เลือก |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [ราคาค่าบริการ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [เริ่มต้น SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [เริ่มต้น Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [ต้องสมัครล่วงหน้าสำหรับการเข้าถึง](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) |
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ราคาค่าบริการ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [หน้าภาพรวมโครงการ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | มีระดับฟรี; endpoint + key เดียวสำหรับโปรไวเดอร์โมเดลหลายตัว |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ราคาค่าบริการ](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat มีโมเดลจำกัด](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ฟรี (รันบนอุปกรณ์คุณ) | ไม่ต้องใช้ | [CLI/SDK ท้องถิ่น](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ออฟไลน์เต็มรูปแบบ, endpoint เข้ากันได้กับ OpenAI |
| | | | | |

ทำตามคำแนะนำด้านล่างเพื่อ _กำหนดค่า_ ที่เก็บนี้สำหรับใช้งานกับโปรไวเดอร์ต่าง ๆ แบบฝึกหัดที่ต้องการโปรไวเดอร์เฉพาะจะมีหนึ่งในแท็กเหล่านี้ในชื่อไฟล์:

- `aoai` - ต้องใช้ Azure OpenAI endpoint, key
- `oai` - ต้องใช้ OpenAI endpoint, key
- `hf` - ต้องใช้ Hugging Face token
- `githubmodels` - ต้องใช้ Microsoft Foundry Models endpoint, key (GitHub Models จะยุติในปลายเดือนกรกฎาคม 2026)

คุณสามารถกำหนดค่าโปรไวเดอร์หนึ่งตัว ไม่มีเลย หรือทั้งหมด แบบฝึกหัดที่เกี่ยวข้องจะแจ้งข้อผิดพลาดหากไม่มีข้อมูลรับรอง

## สร้างไฟล์ `.env`

เราสมมติว่าคุณได้อ่านคำแนะนำข้างต้นและสมัครใช้โปรไวเดอร์ที่เกี่ยวข้องแล้ว พร้อมได้รับข้อมูลรับรองการตรวจสอบสิทธิ์ที่จำเป็น (API_KEY หรือ token) ในกรณีของ Azure OpenAI เราสมมติว่าคุณมีการปรับใช้บริการ Azure OpenAI ที่ถูกต้อง (endpoint) พร้อมโมเดล GPT อย่างน้อยหนึ่งโมเดลสำหรับการสร้างการสนทนา

ขั้นตอนถัดไปคือการกำหนดค่า **ตัวแปรสภาพแวดล้อมท้องถิ่นของคุณ** ดังนี้:

1. มองหาไฟล์ `.env.copy` ในโฟลเดอร์หลักที่ควรมีเนื้อหาเช่นนี้:

   ```bash
   # ผู้ให้บริการ OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI ใน Microsoft Foundry
   ## (บริการ Azure OpenAI ตอนนี้เป็นส่วนหนึ่งของ Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ตั้งค่าเริ่มต้นแล้ว! (เวอร์ชัน API สเถียร GA ปัจจุบัน)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## โมเดล Microsoft Foundry (แค็ตตาล็อกโมเดลผู้ให้บริการหลายราย แทนที่ GitHub Models ซึ่งจะยุติให้บริการสิ้นเดือนกรกฎาคม 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. คัดลอกไฟล์นั้นเป็น `.env` โดยใช้คำสั่งด้านล่าง ไฟล์นี้ถูก _gitignore_ เพื่อเก็บความลับอย่างปลอดภัย

   ```bash
   cp .env.copy .env
   ```

3. กรอกค่าลงไป (แทนที่ช่องว่างทางขวาของ `=`) ตามที่อธิบายในส่วนถัดไป

4. (ทางเลือก) หากคุณใช้ GitHub Codespaces คุณสามารถบันทึกตัวแปรสภาพแวดล้อมเป็น _ความลับของ Codespaces_ ที่เกี่ยวข้องกับที่เก็บนี้ได้ ในกรณีนั้น คุณจะไม่ต้องตั้งค่าไฟล์ .env ท้องถิ่น แต่ควรทราบว่า ตัวเลือกนี้ใช้ได้เฉพาะถ้าคุณใช้ GitHub Codespaces เท่านั้น คุณยังต้องตั้งค่าไฟล์ .env หากคุณใช้ Docker Desktop แทน

## เติมไฟล์ `.env`

มาดูตัวแปรต่าง ๆ เพื่อเข้าใจว่าแต่ละตัวแทนอะไร:

| ตัวแปร | คำอธิบาย |
| :--- | :--- |
| HUGGING_FACE_API_KEY | นี่คือตัว token การเข้าถึงผู้ใช้ที่คุณตั้งค่าในโปรไฟล์ของคุณ |
| OPENAI_API_KEY | นี่คือคีย์อนุญาตสำหรับใช้บริการสำหรับ endpoint OpenAI ที่ไม่ใช่ Azure |
| AZURE_OPENAI_API_KEY | นี่คือคีย์อนุญาตสำหรับใช้บริการนั้น |
| AZURE_OPENAI_ENDPOINT | นี่คือ endpoint ที่ปรับใช้สำหรับทรัพยากร Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | นี่คือ endpoint การปรับใช้โมเดล _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | นี่คือ endpoint การปรับใช้โมเดล _text embeddings_ |
| AZURE_INFERENCE_ENDPOINT | นี่คือ endpoint สำหรับโครงการ Microsoft Foundry ของคุณ ใช้สำหรับ Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | นี่คือ API key สำหรับโครงการ Microsoft Foundry ของคุณ |
| | |

หมายเหตุ: ตัวแปร Azure OpenAI สองตัวสุดท้ายเป็นตัวแทนโมเดลเริ่มต้นสำหรับการสร้างการสนทนา (text generation) และการค้นหาวกเตอร์ (embeddings) ตามลำดับ คำแนะนำในการตั้งค่าจะถูกกำหนดในแบบฝึกหัดที่เกี่ยวข้อง

## กำหนดค่า Azure OpenAI: จาก Portal

> **หมายเหตุ:** บริการ Azure OpenAI ตอนนี้เป็นส่วนหนึ่งของ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ทรัพยากรและการปรับใช้ยังปรากฏใน Azure Portal แต่การจัดการโมเดลในชีวิตประจำวัน (การปรับใช้, playground, การติดตาม) จะเกิดใน Foundry portal แทน "Azure OpenAI Studio" รุ่นเก่า

ค่าของ endpoint และคีย์ของ Azure OpenAI จะพบได้ใน [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ดังนั้นเรามาเริ่มต้นที่นั่น

1. ไปที่ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. คลิกตัวเลือก **Keys and Endpoint** ในแถบด้านข้าง (เมนูด้านซ้าย)
1. คลิก **Show Keys** - คุณจะเห็นดังนี้: KEY 1, KEY 2 และ Endpoint
1. ใช้ค่า KEY 1 สำหรับ AZURE_OPENAI_API_KEY
1. ใช้ค่า Endpoint สำหรับ AZURE_OPENAI_ENDPOINT

ต่อไป เราต้องการ endpoint ของโมเดลเฉพาะที่เราปรับใช้

1. คลิกตัวเลือก **Model deployments** ในแถบด้านข้าง (เมนูซ้าย) สำหรับทรัพยากร Azure OpenAI
1. ในหน้าปลายทาง คลิก **Go to Microsoft Foundry portal** (หรือ **Manage Deployments** ขึ้นกับประเภททรัพยากรของคุณ)

สิ่งนี้จะพาคุณไปยัง Microsoft Foundry portal ที่ซึ่งเราจะค้นหาค่าอื่น ๆ ตามที่อธิบายด้านล่าง

## กำหนดค่า Azure OpenAI: จาก Microsoft Foundry portal

1. ไปที่ [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **จากทรัพยากรของคุณ** ตามที่อธิบายข้างต้น
1. คลิกแท็บ **Deployments** (แถบด้านข้างซ้าย) เพื่อดูโมเดลที่ปรับใช้ในปัจจุบัน
1. หากโมเดลที่ต้องการยังไม่ถูกปรับใช้ ให้ใช้ **Deploy model** เพื่อปรับใช้จาก [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)
1. คุณจะต้องใช้โมเดล _text-generation_ – เราแนะนำ: **gpt-5-mini**
1. คุณจะต้องใช้โมเดล _text-embedding_ – เราแนะนำ **text-embedding-3-small**

ตอนนี้อัปเดตตัวแปรสภาพแวดล้อมให้สะท้อนชื่อ _Deployment name_ ที่ใช้ ซึ่งโดยปกติจะเหมือนกับชื่อโมเดล เว้นแต่คุณจะเปลี่ยน explicitly ดังนั้นตัวอย่างเช่น คุณอาจมี:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**อย่าลืมบันทึกไฟล์ .env เมื่อเสร็จ** คุณสามารถปิดไฟล์และกลับไปอ่านคำแนะนำสำหรับการรันโน้ตบุ๊กได้

## กำหนดค่า OpenAI: จากโปรไฟล์

คุณสามารถหาคีย์ API ของ OpenAI ได้ใน [บัญชี OpenAI ของคุณ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) หากคุณยังไม่มี ให้สมัครบัญชีและสร้างคีย์ API เมื่อต้องการใช้คีย์นี้เพื่อเติมค่าในตัวแปร `OPENAI_API_KEY` ในไฟล์ `.env`

## กำหนดค่า Hugging Face: จากโปรไฟล์

คุณสามารถหาตัว token ของ Hugging Face ในโปรไฟล์ภายใต้ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) อย่าโพสต์หรือแชร์สาธารณะ ให้สร้าง token ใหม่สำหรับโปรเจกต์นี้และคัดลอกไปใส่ในไฟล์ `.env` ใต้ตัวแปร `HUGGING_FACE_API_KEY` _หมายเหตุ:_ เทคนิคนี่ไม่ใช่คีย์ API แต่ใช้สำหรับการตรวจสอบสิทธิ์ ดังนั้นเรายังคงใช้ชื่อแบบนี้เพื่อความสอดคล้อง

## กำหนดค่า Microsoft Foundry Models: จาก Portal

> **หมายเหตุ:** GitHub Models จะยุติในปลายเดือนกรกฎาคม 2026 Microsoft Foundry Models เป็นการทดแทนโดยตรง โดยให้ประสบการณ์การใช้งานชุดโมเดลทดลองใช้ฟรีและ Azure AI Inference SDK / OpenAI SDK เหมือนเดิม

1. ไปที่ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) และสร้าง (หรือเปิด) โครงการ Foundry
1. เรียกดู [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) และปรับใช้โมเดล เช่น `gpt-5-mini`
1. ในหน้าภาพรวมโครงการ คัดลอก **endpoint** และ **API key**
1. ใช้ค่า endpoint สำหรับ `AZURE_INFERENCE_ENDPOINT` และค่า key สำหรับ `AZURE_INFERENCE_CREDENTIAL` ในไฟล์ `.env` ของคุณ

## โปรไวเดอร์ออฟไลน์ / ท้องถิ่น

หากคุณไม่ต้องการใช้การสมัครสมาชิกคลาวด์เลย คุณสามารถรันโมเดลเปิดที่เข้ากันได้โดยตรงบนอุปกรณ์ของคุณเอง:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – runtime บนอุปกรณ์ของ Microsoft ที่เลือกโปรไวเดอร์ประมวลผลที่ดีที่สุดโดยอัตโนมัติ (NPU, GPU หรือ CPU) และสร้าง endpoint ที่เข้ากันได้กับ OpenAI ดังนั้นคุณจึงสามารถใช้ซ้ำโค้ดตัวอย่างในคอร์สนี้ได้แทบไม่ต้องปรับแก้ เริ่มต้นได้ที่ [เอกสาร Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) หรือติดตั้งด้วยคำสั่ง `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS)
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – ทางเลือกยอดนิยมสำหรับรันโมเดลเปิดเช่น Llama, Phi, Mistral และ Gemma บนเครื่องท้องถิ่น


ดู [บทเรียนที่ 19: การสร้างด้วย SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) สำหรับตัวอย่างการใช้งานจริงที่ใช้ทั้งสองตัวเลือก

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->