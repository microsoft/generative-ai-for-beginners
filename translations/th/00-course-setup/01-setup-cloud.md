<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:06:43+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "th"
}
-->
# ตั้งค่าบนคลาวด์ ☁️ – GitHub Codespaces

**ใช้คู่มือนี้ถ้าคุณไม่อยากติดตั้งอะไรในเครื่องเลย**  
Codespaces ให้คุณใช้งาน VS Code ผ่านเบราว์เซอร์ฟรี พร้อมติดตั้งทุก dependency ไว้ให้แล้ว

---

## 1.  ทำไมต้องใช้ Codespaces?

| ข้อดี | หมายถึงอะไรสำหรับคุณ |
|---------|----------------------|
| ✅ ไม่ต้องติดตั้งอะไรเลย | ใช้งานได้บน Chromebook, iPad, คอมในห้องแล็บโรงเรียน… |
| ✅ มี dev container สำเร็จรูป | มี Python 3, Node.js, .NET, Java ให้พร้อมใช้งาน |
| ✅ มีโควต้าฟรี | บัญชีส่วนตัวจะได้ **120 core-hours / 60 GB-hours ต่อเดือน** |

> 💡 **เคล็ดลับ**  
> รักษาโควต้าของคุณให้ดีด้วยการ **หยุด** หรือ **ลบ** codespace ที่ไม่ได้ใช้งาน  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*)

---

## 2.  สร้าง Codespace (คลิกเดียวจบ)

1. **Fork** repo นี้ (ปุ่ม **Fork** มุมขวาบน)  
2. ใน repo ที่คุณ fork ไป ให้คลิก **Code ▸ Codespaces ▸ Create codespace on main**  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ หน้าต่าง VS Code ในเบราว์เซอร์จะเปิดขึ้น และ dev container จะเริ่มสร้าง  
ครั้งแรกจะใช้เวลา **~2 นาที**

## 3. เพิ่ม API key ของคุณ (วิธีที่ปลอดภัย)

### ตัวเลือก A Codespaces Secrets — แนะนำ

1. ⚙️ ไอคอนรูปเฟือง -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret
2. Name: OPENAI_API_KEY
3. Value: วาง key ของคุณ → Add secret

แค่นี้เอง—โค้ดของเราจะดึงมาใช้ให้อัตโนมัติ

### ตัวเลือก B ไฟล์ .env (ถ้าคุณจำเป็นต้องใช้จริง ๆ)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องแม่นยำ แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้