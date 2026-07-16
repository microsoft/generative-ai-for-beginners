# Configurare Cloud ☁️ – GitHub Codespaces

**Folosește acest ghid dacă nu vrei să instalezi nimic local.**  
Codespaces îți oferă o instanță VS Code gratuită, în browser, cu toate dependențele preinstalate.

---

## 1. De ce Codespaces?

| Beneficiu | Ce înseamnă pentru tine |
|---------|--------------------------|
| ✅ Fără instalări | Funcționează pe Chromebook, iPad, PC-uri de laborator școlar… |
| ✅ Container dev preconstruit | Python 3, Node.js, .NET, Java deja incluse |
| ✅ Cotă gratuită | Conturile personale primesc **120 ore CPU / 60 GB-oră pe lună** |

> 💡 **Sfat**  
> Menține-ți cota sănătoasă prin **oprirea** sau **ștergerea** codespaces inactivi  
> (Vizualizează ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2. Creează un Codespace (un singur clic)

1. **Fork** acest repo (butonul **Fork** din dreapta sus).  
2. În forkul tău, apasă **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog care arată butoanele pentru crearea unui codespace](../../../translated_images/ro/who-will-pay.4c0609b1c7780f44.webp)

✅ Se deschide o fereastră VS Code în browser și începe construirea containerului dev.
Acest proces durează **~2 minute** prima dată.

## 3. Adaugă cheia API (în mod sigur)

### Opțiunea A Secrets Codespaces — Recomandat

1. ⚙️ Iconița setări -> Command Palette-> Codespaces : Manage user secret -> Add a new secret.
2. Nume: OPENAI_API_KEY
3. Valoare: lipește cheia → Add secret

Gata—codul nostru o va prelua automat.

### Opțiunea B fișier .env (doar dacă chiar ai nevoie)

```bash
cp .env.copy .env
code .env         # completați OPENAI_API_KEY=cheia_dumneavoastră_aici
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->