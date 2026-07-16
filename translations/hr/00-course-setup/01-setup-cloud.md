# Cloud postavljanje ☁️ – GitHub Codespaces

**Koristite ovaj vodič ako ne želite ništa instalirati lokalno.**  
Codespaces vam daje besplatnu VS Code instancu u pregledniku sa svim unaprijed instaliranim ovisnostima.

---

## 1.  Zašto Codespaces?

| Prednost | Što to znači za vas |
|---------|----------------------|
| ✅ Nema instalacija | Radi na Chromebooku, iPadu, školskim računalima… |
| ✅ Unaprijed izgrađeni razvojni kontejner | Python 3, Node.js, .NET, Java već unutra |
| ✅ Besplatna kvota | Osobni računi imaju **120 sati procesora / 60 GB-sati mjesečno** |

> 💡 **Savjet**  
> Održavajte svoju kvotu zdravom **zaustavljanjem** ili **brisanje** neaktivnih codespacesa  
> (Pogledajte ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Kreirajte Codespace (jedan klik)

1. **Forkajte** ovaj repozitorij (gore desno dugme **Fork**).  
2. U svom forku kliknite **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dijalog koji pokazuje gumbe za kreiranje codespacea](../../../translated_images/hr/who-will-pay.4c0609b1c7780f44.webp)

✅ Otvara se VS Code prozor u pregledniku i razvojni kontejner počinje se graditi.
Ovo traje **~2 minute** prvi put.

## 3. Dodajte svoj API ključ (siguran način)

### Opcija A Codespaces Secrets — Preporučeno

1. ⚙️ Ikona zupčanika -> Command Palette -> Codespaces : Manage user secret -> Dodaj novi secret.
2. Naziv: OPENAI_API_KEY
3. Vrijednost: zalijepite svoj ključ → Dodaj secret

To je to—naš će kod automatski pročitati ključ.

### Opcija B .env datoteka (ako vam baš treba)

```bash
cp .env.copy .env
code .env         # unesite OPENAI_API_KEY=vaš_kljuć_ovdje
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->