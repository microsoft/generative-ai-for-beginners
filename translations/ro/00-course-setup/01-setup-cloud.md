<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T19:11:30+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "ro"
}
-->
# Configurare în cloud ☁️ – GitHub Codespaces

**Folosește acest ghid dacă nu vrei să instalezi nimic local.**  
Codespaces îți oferă gratuit o instanță VS Code direct în browser, cu toate dependențele deja instalate.

---

## 1.  De ce Codespaces?

| Beneficiu | Ce înseamnă pentru tine |
|-----------|------------------------|
| ✅ Fără instalări | Funcționează pe Chromebook, iPad, PC-uri din laboratorul școlii… |
| ✅ Container de dezvoltare preconfigurat | Python 3, Node.js, .NET, Java sunt deja incluse |
| ✅ Cotă gratuită | Conturile personale primesc **120 core-hours / 60 GB-hours pe lună** |

> 💡 **Tip**  
> Menține-ți cota în limite oprind sau ștergând codespaces nefolosite  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Creează un Codespace (un singur click)

1. **Fork-uiește** acest repo (butonul **Fork** din dreapta sus).  
2. În fork-ul tău, apasă **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog care arată butoanele pentru crearea unui codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Se va deschide o fereastră VS Code în browser și containerul de dezvoltare va începe să se construiască.
Prima dată durează **~2 minute**.

## 3. Adaugă cheia ta API (în siguranță)

### Opțiunea A Secrete Codespaces — Recomandat

1. ⚙️ Iconița de setări -> Command Palette-> Codespaces : Manage user secret -> Add a new secret.
2. Nume: OPENAI_API_KEY
3. Valoare: lipește cheia ta → Add secret

Gata—codul nostru o va detecta automat.

### Opțiunea B Fișier .env (dacă chiar ai nevoie)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.