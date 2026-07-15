# การตั้งค่า Cloud ☁️ – GitHub Codespaces

**ใช้คำแนะนำนี้หากคุณไม่ต้องการติดตั้งอะไรในเครื่องของคุณ**  
Codespaces ให้คุณใช้งาน VS Code บนเบราว์เซอร์ได้ฟรี โดยมีการติดตั้ง dependency ทุกอย่างล่วงหน้าแล้ว

---

## 1. ทำไมต้อง Codespaces?

| ประโยชน์ | ความหมายสำหรับคุณ |
|---------|----------------------|
| ✅ ไม่ต้องติดตั้ง | ใช้งานได้บน Chromebook, iPad, คอมพิวเตอร์ห้องเรียน… |
| ✅ dev container ติดตั้งไว้ล่วงหน้า | มี Python 3, Node.js, .NET, Java ภายในแล้ว |
| ✅ โควต้าฟรี | บัญชีส่วนตัวจะได้รับ **120 core-hours / 60 GB-hours ต่อเดือน** |

> 💡 **เคล็ดลับ**  
> รักษาโควต้าของคุณให้ดีโดยการ **หยุด** หรือ **ลบ** codespaces ที่ไม่ได้ใช้งาน  
> (ดูได้ที่ ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2. สร้าง Codespace (คลิกครั้งเดียว)

1. **Fork** รีโปนี้ (ปุ่ม **Fork** ด้านบนขวา)  
2. ในรีโปของคุณ คลิก **Code ▸ Codespaces ▸ Create codespace on main**  
   ![Dialog showing buttons to create a codespace](../../../translated_images/th/who-will-pay.4c0609b1c7780f44.webp)

✅ หน้าต่าง VS Code บนเบราว์เซอร์จะเปิดและเริ่มสร้าง dev container
ขั้นตอนนี้ใช้เวลาประมาณ **~2 นาที** ในครั้งแรก

## 3. เพิ่ม API key ของคุณ (วิธีที่ปลอดภัย)

### ตัวเลือก A Codespaces Secrets — แนะนำ

1. ⚙️ ไอคอนรูปเฟือง -> Command Palette-> Codespaces : Manage user secret -> Add a new secret
2. ชื่อ: OPENAI_API_KEY
3. ค่า: วางคีย์ของคุณ → Add secret

เพียงเท่านี้—โค้ดของเราจะดึงค่าไปใช้อัตโนมัติ

### ตัวเลือก B ไฟล์ .env (ถ้าคุณต้องการจริงๆ)

```bash
cp .env.copy .env
code .env         # กรอก OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->