<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T19:38:29+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "hr"
}
-->
# Postavljanje u oblaku ☁️ – GitHub Codespaces

**Koristi ovaj vodič ako ne želiš ništa instalirati lokalno.**  
Codespaces ti omogućuje besplatno korištenje VS Code-a u pregledniku, sa svim unaprijed instaliranim ovisnostima.

---

## 1.  Zašto Codespaces?

| Prednost | Što to znači za tebe |
|----------|---------------------|
| ✅ Bez instalacija | Radi na Chromebooku, iPadu, školskim računalima… |
| ✅ Unaprijed pripremljen dev container | Python 3, Node.js, .NET, Java su već unutra |
| ✅ Besplatna kvota | Osobni računi dobivaju **120 core-sati / 60 GB-sati mjesečno** |

> 💡 **Savjet**  
> Očuvaj svoju kvotu tako da **zaustaviš** ili **obrišeš** neaktivne codespaceove  
> (Pogledaj ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Kreiraj Codespace (jedan klik)

1. **Forkaj** ovaj repozitorij (gore desno gumb **Fork**).  
2. U svom forku klikni **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dijalog s gumbima za kreiranje codespacea](../../../00-course-setup/images/who-will-pay.webp)

✅ Otvorit će se VS Code prozor u pregledniku i dev container će se početi graditi.
Prvi put ovo traje **oko 2 minute**.

## 3. Dodaj svoj API ključ (na siguran način)

### Opcija A Codespaces Secrets — Preporučeno

1. ⚙️ Ikona zupčanika -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Naziv: OPENAI_API_KEY
3. Vrijednost: zalijepi svoj ključ → Add secret

To je to—naš kod će ga automatski prepoznati.

### Opcija B .env datoteka (ako ti stvarno treba)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.