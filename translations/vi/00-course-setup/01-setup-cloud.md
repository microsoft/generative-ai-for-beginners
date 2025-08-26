<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:05:42+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "vi"
}
-->
# Thiết lập trên đám mây ☁️ – GitHub Codespaces

**Hãy dùng hướng dẫn này nếu bạn không muốn cài đặt gì trên máy tính cá nhân.**  
Codespaces cung cấp cho bạn một phiên bản VS Code trên trình duyệt, với mọi thư viện cần thiết đã được cài sẵn.

---

## 1.  Tại sao nên dùng Codespaces?

| Lợi ích | Ý nghĩa với bạn |
|---------|----------------|
| ✅ Không cần cài đặt | Dùng được trên Chromebook, iPad, máy tính phòng lab ở trường… |
| ✅ Môi trường phát triển dựng sẵn | Python 3, Node.js, .NET, Java đã có sẵn bên trong |
| ✅ Miễn phí một mức nhất định | Tài khoản cá nhân được **120 core-giờ / 60 GB-giờ mỗi tháng** |

> 💡 **Mẹo**  
> Giữ quota của bạn luôn ổn định bằng cách **dừng** hoặc **xóa** các codespace không dùng đến  
> (Xem ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Tạo Codespace (chỉ một cú nhấp)

1. **Fork** repo này (góc trên bên phải, nút **Fork**).  
2. Trong repo của bạn, nhấn **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Hộp thoại hiển thị các nút để tạo codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Một cửa sổ VS Code trên trình duyệt sẽ mở ra và môi trường phát triển bắt đầu được dựng.  
Lần đầu tiên sẽ mất khoảng **2 phút**.

## 3. Thêm API key của bạn (cách an toàn)

### Cách A: Codespaces Secrets — Khuyến nghị

1. ⚙️ Biểu tượng bánh răng -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Tên: OPENAI_API_KEY
3. Giá trị: dán key của bạn → Add secret

Xong rồi—code của chúng ta sẽ tự động nhận key này.

### Cách B: Tạo file .env (nếu bạn thực sự cần)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.