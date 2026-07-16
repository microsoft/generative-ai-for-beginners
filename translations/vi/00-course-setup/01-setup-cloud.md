# Thiết lập trên đám mây ☁️ – GitHub Codespaces

**Sử dụng hướng dẫn này nếu bạn không muốn cài đặt gì trên máy cục bộ.**  
Codespaces cung cấp cho bạn một phiên bản VS Code miễn phí trên trình duyệt với tất cả các phụ thuộc đã được cài đặt sẵn.

---

## 1.  Tại sao chọn Codespaces?

| Lợi ích | Ý nghĩa đối với bạn |
|---------|----------------------|
| ✅ Không cần cài đặt | Hoạt động trên Chromebook, iPad, máy tính phòng lab trường học… |
| ✅ Container phát triển được xây dựng sẵn | Bao gồm Python 3, Node.js, .NET, Java |
| ✅ Hạn mức miễn phí | Tài khoản cá nhân nhận được **120 giờ lõi / 60 GB-giờ mỗi tháng** |

> 💡 **Mẹo**  
> Giữ hạn mức của bạn khỏe mạnh bằng cách **dừng** hoặc **xóa** các codespaces không sử dụng  
> (Chọn ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Tạo Codespace (một cú nhấp)

1. **Fork** repo này (nút **Fork** bên trên bên phải).  
2. Trong kho fork của bạn, nhấn **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Hộp thoại hiển thị các nút để tạo codespace](../../../translated_images/vi/who-will-pay.4c0609b1c7780f44.webp)

✅ Một cửa sổ VS Code trên trình duyệt sẽ mở ra và container phát triển sẽ bắt đầu xây dựng.
Việc này mất khoảng **~2 phút** lần đầu tiên.

## 3. Thêm khóa API của bạn (cách an toàn)

### Lựa chọn A Codespaces Secrets — Khuyên dùng

1. ⚙️ Biểu tượng bánh răng -> Command Palette -> Codespaces: Manage user secret -> Thêm bí mật mới.
2. Tên: OPENAI_API_KEY
3. Giá trị: dán khóa của bạn → Thêm bí mật

Xong—mã của chúng tôi sẽ tự động nhận khóa.

### Lựa chọn B Tệp .env (nếu bạn thực sự cần)

```bash
cp .env.copy .env
code .env         # điền vào OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->