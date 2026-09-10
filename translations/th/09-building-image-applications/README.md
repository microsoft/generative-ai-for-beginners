# การสร้างแอปพลิเคชันสร้างภาพ

[![การสร้างแอปพลิเคชันสร้างภาพ](../../../translated_images/th/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs มีความสามารถมากกว่าการสร้างข้อความ คุณยังสามารถสร้างภาพจากคำอธิบายข้อความได้ ภาพในรูปแบบนี้มีประโยชน์ในหลากหลายสาขา เช่น MedTech สถาปัตยกรรม การท่องเที่ยว การพัฒนาเกม การตลาด และอื่น ๆ ในบทเรียนนี้เราจะมาดูโมเดล **GPT Image** ในปัจจุบันและสร้างแอปพลิเคชันสร้างภาพ

## บทนำ

การสร้างภาพจะช่วยให้คุณเปลี่ยนคำสั่งภาษาธรรมชาติเป็นภาพได้ ในบทเรียนนี้เราจะใช้โมเดลตระกูล **`gpt-image`** จาก OpenAI - เจเนอเรชันปัจจุบันของโมเดลภาพที่มีอยู่ใน **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** และแพลตฟอร์ม OpenAI โมเดลเหล่านี้มาแทนที่โมเดล DALL·E รุ่นเก่า (DALL·E 2/3 เป็นของเก่า)

ตลอดบทเรียน เราจะใช้บริษัทสมมติชื่อ **Edu4All** ที่สร้างเครื่องมือการเรียนรู้ ทีมงานต้องการสร้างภาพประกอบสำหรับงานมอบหมายและเอกสารการศึกษา

## เป้าหมายการเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายว่าการสร้างภาพคืออะไรและมีประโยชน์ในด้านใดบ้าง
- เข้าใจตระกูลโมเดล `gpt-image` และความแตกต่างจากโมเดล DALL·E เก่า
- สร้างแอปพลิเคชันสร้างภาพใน Python (และ TypeScript / .NET)
- แก้ไขภาพและใช้มาตรการรักษาความปลอดภัยด้วย metaprompts

## การสร้างภาพคืออะไร?

โมเดลการสร้างภาพสร้างภาพจากคำสั่งข้อความ โมเดลสมัยใหม่เช่น `gpt-image` ใช้เทคนิค transformer + diffusion: โมเดลจะเรียนรู้ความสัมพันธ์ระหว่างข้อความกับภาพในระหว่างการฝึก จากนั้นเมื่อได้รับคำสั่ง จะทำการ "ลดเสียงรบกวน" จากสัญญาณสุ่มทีละน้อยจนออกมาเป็นภาพตรงตามคำอธิบาย

โมเดลภาพสองตระกูลที่รู้จักกันดีได้แก่:

- **`gpt-image` (OpenAI)** - เจเนอเรชันปัจจุบัน ใช้ในบทเรียนนี้ รองรับการสร้างภาพจากข้อความและแก้ไขภาพ (วาดเติมส่วนที่มีมาสก์)
- **Midjourney** - โมเดลของบุคคลที่สามยอดนิยม พร้อมบริการและเวิร์กโฟลว์บน Discord

> โมเดลภาพ OpenAI รุ่นเก่า - **DALL·E 2** และ **DALL·E 3** - เป็นรุ่นเก่า DALL·E 3 ไม่สามารถใช้งานใหม่ได้อีกต่อไป และฟีเจอร์เช่น `create_variation` มีใน DALL·E 2 เท่านั้น ให้ใช้โมเดล `gpt-image` สำหรับแอปใหม่

### ควรใช้โมเดล `gpt-image` รุ่นใด?

บน Microsoft Foundry มีโมเดลดังต่อไปนี้ **พร้อมใช้งานทั่วไป**:

| โมเดล | หมายเหตุ |
| --- | --- |
| **`gpt-image-2`** | โมเดลภาพล่าสุดและมีความสามารถสูงสุด - แนะนำให้ใช้เป็นค่าเริ่มต้น |
| `gpt-image-1.5` | พร้อมใช้งานทั่วไป; คุณภาพดีในราคาต่ำกว่า |
| `gpt-image-1-mini` | พร้อมใช้งานทั่วไป; เร็วที่สุด / ราคาต่ำสุด |
| `gpt-image-1` | รุ่นดูตัวอย่างเท่านั้น |

ตรวจสอบเสมอที่ [รายชื่อโมเดลภาพ Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) สำหรับสถานะและภูมิภาค

> **สำคัญ:** โมเดล `gpt-image` จะส่งคืนภาพที่สร้างเป็น **base64** (`b64_json`) ไม่ใช่ URL โค้ดของคุณต้องถอดรหัสสตริง base64 เป็นไบต์และบันทึกไว้ - ไม่มี URL ภาพให้ดาวน์โหลด

## การตั้งค่า

คุณสามารถรันตัวอย่างกับ **Azure OpenAI บน Microsoft Foundry** (ตัวอย่าง `aoai-*`) หรือ **แพลตฟอร์ม OpenAI** (ตัวอย่าง `oai-*`)

### 1. สร้างและปรับใช้โมเดล

ทำตามคำแนะนำ [สร้างทรัพยากร](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) เพื่อสร้างทรัพยากร Microsoft Foundry จากนั้นปรับใช้โมเดลภาพ - แนะนำให้ใช้ **`gpt-image-2`**

### 2. กำหนดค่า `.env` ของคุณ

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

ค้นหาค่านี้ได้ที่หน้าการ **Deployments** ในทรัพยากรของคุณใน [พอร์ทัล Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)

### 3. ติดตั้งไลบรารี

สร้างไฟล์ `requirements.txt`:

```text
python-dotenv
openai
pillow
```

จากนั้นสร้างและเปิดใช้งานสภาพแวดล้อมเสมือนและติดตั้ง:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## สร้างแอป

สร้างไฟล์ `app.py` ด้วยโค้ดต่อไปนี้ มันจะสร้างภาพและบันทึกเป็นไฟล์ PNG

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# ชี้ไคลเอ็นต์ไปยังแหล่งข้อมูล Azure OpenAI (Microsoft Foundry) ของคุณ
# โมเดลภาพต้องใช้เวอร์ชัน API ล่าสุด - ตรวจสอบเอกสาร Foundry สำหรับเวอร์ชันที่โมเดลของคุณต้องการ
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # ตัวอย่างเช่น "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # ยังรองรับ 1536x1024 (แนวนอน), 1024x1536 (แนวตั้ง), หรือ "อัตโนมัติ"
    n=1,
)

# โมเดล gpt-image ส่งกลับข้อมูล base64 (b64_json) ไม่ใช่ URL - ต้องถอดรหัสเป็นไบต์
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

รันด้วยคำสั่ง `python app.py` คุณจะได้ไฟล์ PNG บันทึกอยู่ในโฟลเดอร์ `images/`

> ทุกครั้งที่เรียก `images.generate` จะได้ภาพที่แตกต่างกันสำหรับคำสั่งเดียวกัน - โมเดลภาพไม่มีพารามิเตอร์ `temperature` (เป็นการควบคุมสำหรับการสร้างข้อความ) หากต้องการภาพหลากหลายให้เรียก API ซ้ำ ๆ หากต้องการลดความหลากหลาย ให้กำหนดคำสั่งให้เจาะจงมากขึ้น

## การแก้ไขภาพ

โมเดล `gpt-image` สามารถ **แก้ไข** ภาพที่มีอยู่ได้: ให้ภาพต้นฉบับ มาสก์ (ถ้ามี) ที่ระบุพื้นที่ที่จะเปลี่ยน และคำสั่งบรรยายการเปลี่ยนแปลง เช่นเดียวกับการสร้างภาพ การแก้ไขจะคืนค่าเป็น base64

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/th/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/th/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/th/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## การตั้งขอบเขตด้วย metaprompts

เมื่อคุณสามารถสร้างภาพได้แล้ว คุณต้องมีแนวทางป้องกันเพื่อไม่ให้แอปของคุณสร้างเนื้อหาที่ไม่ปลอดภัยหรือไม่เหมาะสม **metaprompt** คือข้อความที่คุณเพิ่มไปข้างหน้าคำสั่งของผู้ใช้เพื่อจำกัดผลลัพธ์ของโมเดล

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# ส่ง `prompt` ไปยัง client.images.generate(...)
```

ภาพทุกภาพจะถูกสร้างภายในขอบเขตที่ metaprompt กำหนด รวมกับตัวกรองเนื้อหาที่ฝังอยู่ใน Microsoft Foundry เพื่อป้องกันในหลายชั้น

## งานมอบหมาย - ให้โอกาสนักเรียน

นักเรียน Edu4All ต้องการภาพสำหรับการประเมิน สร้างแอปที่สร้างภาพของ **อนุสาวรีย์** (เลือกอนุสาวรีย์ได้ตามสะดวก) ในบริบทที่สร้างสรรค์ต่าง ๆ - เช่นแลนด์มาร์คชื่อดังตอนพระอาทิตย์ตกพร้อมเด็กคนหนึ่งชมวิว

ลองทำเอง จากนั้นเปรียบเทียบกับโซลูชันตัวอย่าง:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) แอปเต็มรูปแบบ: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

ทำงานผ่านโน้ตบุ๊กใน [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` สำหรับ Azure, `oai-assignment.ipynb` สำหรับ OpenAI) ด้วย

## ทำได้ดีมาก! เรียนรู้ต่อไป

หลังจากจบบทเรียนนี้แล้ว อย่าลืมดูที่ [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ด้าน Generative AI ของคุณต่อไป!

ไปที่บทเรียน 10 เพื่อเรียนรู้ต่อได้เลย

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->