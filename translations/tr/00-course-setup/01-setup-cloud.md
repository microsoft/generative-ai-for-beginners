# Bulut Kurulumu ☁️ – GitHub Codespaces

**Yerel olarak herhangi bir şey yüklemek istemiyorsanız bu rehberi kullanın.**  
Codespaces, tüm bağımlılıkların önceden yüklü olduğu, tarayıcı tabanlı ücretsiz bir VS Code örneği sunar.

---

## 1.  Neden Codespaces?

| Avantaj | Sizin için anlamı |
|---------|----------------------|
| ✅ Sıfır kurulum | Chromebook, iPad, okul laboratuvarı bilgisayarlarında çalışır… |
| ✅ Önceden oluşturulmuş geliştirme konteyneri | Python 3, Node.js, .NET, Java zaten içinde |
| ✅ Ücretsiz kota | Kişisel hesaplara aylık **120 çekirdek-saat / 60 GB-saat** verilir |

> 💡 **İpucu**  
> Kodalanmayan codespaces'leri **durdurarak** veya **silerek** kotanızı sağlıklı tutun  
> (Görünüm ▸ Komut Paleti ▸ *Codespaces: Codespace Durdur*).

---

## 2.  Bir Codespace Oluşturun (tek tıkla)

1. Bu depoyu **Fork**layın (sağ üstteki **Fork** düğmesi).  
2. Fork'unuzda, **Kod ▸ Codespaces ▸ main üzerinde bir codespace oluştur**‘a tıklayın.  
   ![Codespace oluşturma butonlarını gösteren dialog](../../../translated_images/tr/who-will-pay.4c0609b1c7780f44.webp)

✅ Bir tarayıcı VS Code penceresi açılır ve geliştirme konteyneri oluşturmaya başlar.
Bu ilk seferde **~2 dakika** sürer.

## 3. API anahtarınızı ekleyin (güvenli yol)

### Seçenek A Codespaces Secrets — Tavsiye edilen

1. ⚙️ Dişli simgesi -> Komut Paleti -> Codespaces : Kullanıcı gizliliğini yönet -> Yeni gizli bilgi ekle.
2. İsim: OPENAI_API_KEY
3. Değer: anahtarınızı yapıştır → Gizli bilgiyi ekle

Hepsi bu—kodumuz bunu otomatik olarak alacak.

### Seçenek B .env dosyası (gerçekten gerekirse)

```bash
cp .env.copy .env
code .env         # OPENAI_API_KEY=anahtarınız_buraya olarak doldurun
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->