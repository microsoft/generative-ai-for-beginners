<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T19:46:45+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "sl"
}
-->
# Nastavitev v oblaku ☁️ – GitHub Codespaces

**Uporabite ta vodič, če ne želite ničesar nameščati lokalno.**  
Codespaces vam omogoča brezplačno uporabo VS Code v brskalniku, kjer so vse potrebne odvisnosti že nameščene.

---

## 1.  Zakaj Codespaces?

| Prednost | Kaj to pomeni za vas |
|----------|---------------------|
| ✅ Brez nameščanja | Deluje na Chromebooku, iPadu, šolskih računalnikih… |
| ✅ Vnaprej pripravljen razvojni container | Python 3, Node.js, .NET, Java so že vključeni |
| ✅ Brezplačna kvota | Osebni računi dobijo **120 core-ur / 60 GB-ur na mesec** |

> 💡 **Tip**  
> Ohranite kvoto tako, da **ustavite** ali **izbrišete** neaktivne codespace  
> (Pogled ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Ustvarite Codespace (z enim klikom)

1. **Forkajte** ta repozitorij (zgoraj desno gumb **Fork**).  
2. V svojem forku kliknite **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Pogovorno okno z gumbi za ustvarjanje codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Odpre se okno VS Code v brskalniku in razvojni container se začne graditi.
Prvič to traja **~2 minuti**.

## 3. Dodajte svoj API ključ (na varen način)

### Možnost A Codespaces Secrets — Priporočeno

1. ⚙️ Ikona zobnika -> Command Pallete-> Codespaces : Manage user secret -> Dodajte novo skrivnost.
2. Ime: OPENAI_API_KEY
3. Vrednost: prilepite svoj ključ → Add secret

To je vse—naša koda bo ključ samodejno zaznala.

### Možnost B .env datoteka (če jo res potrebujete)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.