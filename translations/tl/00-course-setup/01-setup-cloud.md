<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:29:20+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "tl"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**Gamitin ang gabay na ito kung ayaw mong mag-install ng kahit ano sa iyong computer.**  
Nagbibigay ang Codespaces ng libreng, browser-based na VS Code na may lahat ng kailangan na naka-install na.

---

## 1.  Bakit Codespaces?

| Benepisyo | Ano ang ibig sabihin nito para sa iyo |
|-----------|--------------------------------------|
| ✅ Walang kailangang i-install | Gumagana sa Chromebook, iPad, school lab PCs… |
| ✅ Pre-built na dev container | May Python 3, Node.js, .NET, Java na agad |
| ✅ Libreng quota | Personal na account ay may **120 core-hours / 60 GB-hours bawat buwan** |

> 💡 **Tip**  
> Panatilihing maayos ang iyong quota sa pamamagitan ng **pag-stop** o **pag-delete** ng mga codespace na hindi ginagamit  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Gumawa ng Codespace (isang click lang)

1. **Fork** ang repo na ito (i-click ang **Fork** button sa itaas-kanan).  
2. Sa iyong fork, i-click ang **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Magbubukas ang VS Code sa browser at magsisimula ang pagbuo ng dev container.
Tumatagal ito ng **~2 minuto** sa unang beses.

## 3. Ilagay ang iyong API key (ang ligtas na paraan)

### Option A Codespaces Secrets — Inirerekomenda

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: i-paste ang iyong key → Add secret

Ayan na—awtomatikong makikita ito ng ating code.

### Option B .env file (kung talagang kailangan mo)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.