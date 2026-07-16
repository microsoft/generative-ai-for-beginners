# Cloud Setup ☁️ – GitHub Codespaces

**Gamitin ang gabay na ito kung ayaw mong mag-install ng ano man sa lokal.**  
Nagbibigay ang Codespaces ng libre, browser-based na VS Code instance na may lahat ng dependencies na naka-install na.

---

## 1.  Bakit Codespaces?

| Benepisyo | Ano ang ibig sabihin nito para sa iyo |
|---------|-----------------------------|
| ✅ Walang kailangang i-install | Gumagana sa Chromebook, iPad, school lab PCs… |
| ✅ Pre-built na dev container | Python 3, Node.js, .NET, Java ay nakapaloob na |
| ✅ Libreng quota | Nakakakuha ang personal accounts ng **120 core-hours / 60 GB-hours bawat buwan** |

> 💡 **Tip**  
> Panatilihing malusog ang iyong quota sa pamamagitan ng **pagtigil** o **pag-delete** ng mga idle codespaces  
> (Tumingin ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Gumawa ng Codespace (isang click lang)

1. **I-fork** ang repo na ito (nasa itaas-kanang bahagi ang **Fork** button).  
2. Sa iyong fork, i-click ang **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/tl/who-will-pay.4c0609b1c7780f44.webp)

✅ Magbubukas ang browser VS Code window at magsisimula ang pag-build ng dev container.
Tatagal ito ng **~2 minuto** sa unang pagkakataon.

## 3. Idagdag ang iyong API key (ang ligtas na paraan)

### Option A Codespaces Secrets — Inirerekomenda

1. ⚙️ Gear icon -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Pangalan: OPENAI_API_KEY
3. Halaga: i-paste ang iyong key → Add secret

Iyan na—kusang kukunin ito ng aming code.

### Option B .env file (kung talagang kailangan mo)

```bash
cp .env.copy .env
code .env         # punan ang OPENAI_API_KEY=ang_iyong_susi_dito
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->