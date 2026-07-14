# Nastavitev v oblaku ☁️ – GitHub Codespaces

**Uporabite ta vodič, če ničesar ne želite nameščati lokalno.**  
Codespaces vam nudi brezplačen primerek VS Code, ki teče v brskalniku, z vsemi vnaprej nameščenimi odvisnostmi.

---

## 1.  Zakaj Codespaces?

| Prednost | Kaj to pomeni za vas |
|---------|---------------------|
| ✅ Brez nameščanja | Deluje na Chromebooku, iPadu, računalnikih šolskih laboratorijev… |
| ✅ Vnaprej izdelan razvojni zaboj | Vsebuje Python 3, Node.js, .NET, Java |
| ✅ Brezplačna kvota | Osebni računi prejmejo **120 jeder-ur / 60 GB-ur mesečno** |

> 💡 **Nasvet**  
> Ohranite svojo kvoto zdravo tako, da **ustavite** ali **izbrišete** neaktivne codespace-e  
> (Poglejte ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Ustvarite Codespace (z enim klikom)

1. **Razvejajte (forkajte)** ta repozitorij (zgoraj desno gumb **Fork**).  
2. V svojem forku kliknite **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog prikazuje gumbe za ustvarjanje codespace-a](../../../translated_images/sl/who-will-pay.4c0609b1c7780f44.webp)

✅ Odpre se okno VS Code v brskalniku in razvojni zaboj se začne graditi.
To običajno traja **~2 minuti** ob prvem zagonu.

## 3. Dodajte vaš API ključ (varen način)

### Možnost A Codespaces Secrets — Priporočeno

1. ⚙️ Ikona zobnika -> Command Pallete -> Codespaces : Manage user secret -> Dodaj nov skrivni ključ.
2. Ime: OPENAI_API_KEY
3. Vrednost: prilepite vaš ključ → Dodaj skrivnost

To je to—naša koda bo samodejno uporabila ta ključ.

### Možnost B datoteka .env (če jo res potrebujete)

```bash
cp .env.copy .env
code .env         # vnesite OPENAI_API_KEY=vaš_ključ_tukaj
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->