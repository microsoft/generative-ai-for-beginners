<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T16:47:05+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "tr"
}
-->
# Bulut Kurulumu ☁️ – GitHub Codespaces

**Hiçbir şeyi yerel olarak kurmak istemiyorsanız bu rehberi kullanın.**  
Codespaces, tüm bağımlılıkları önceden yüklenmiş, tarayıcı tabanlı ücretsiz bir VS Code ortamı sunar.

---

## 1.  Neden Codespaces?

| Avantaj | Sizin için anlamı |
|---------|-------------------|
| ✅ Sıfır kurulum | Chromebook, iPad, okul laboratuvar bilgisayarlarında çalışır… |
| ✅ Önceden hazırlanmış geliştirme konteyneri | Python 3, Node.js, .NET, Java zaten içinde |
| ✅ Ücretsiz kota | Kişisel hesaplar **ayda 120 çekirdek-saat / 60 GB-saat** alır |

> 💡 **İpucu**  
> Kotanızı korumak için boşta kalan codespace’leri **durdurun** veya **silin**  
> (Görünüm ▸ Komut Paleti ▸ *Codespaces: Codespace’i Durdur*).

---

## 2.  Codespace Oluşturun (tek tıkla)

1. Bu repoyu **fork’layın** (sağ üstteki **Fork** butonu).  
2. Fork’unuzda **Code ▸ Codespaces ▸ Create codespace on main**’e tıklayın.  
   ![Codespace oluşturma butonlarını gösteren diyalog](../../../00-course-setup/images/who-will-pay.webp)

✅ Tarayıcıda bir VS Code penceresi açılır ve geliştirme konteyneri başlatılır.
İlk seferde bu işlem **~2 dakika** sürer.

## 3. API anahtarınızı ekleyin (güvenli yol)

### Seçenek A Codespaces Secrets — Tavsiye Edilen

1. ⚙️ Dişli simgesi -> Komut Paleti-> Codespaces : Kullanıcı gizli anahtarını yönet -> Yeni bir gizli anahtar ekle.
2. Ad: OPENAI_API_KEY
3. Değer: anahtarınızı yapıştırın → Gizli anahtar ekle

Hepsi bu—kodumuz anahtarı otomatik olarak bulacak.

### Seçenek B .env dosyası (gerçekten gerekliyse)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar bulunabilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.