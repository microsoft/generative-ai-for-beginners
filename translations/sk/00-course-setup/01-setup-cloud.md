<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T19:03:24+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "sk"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**Použite tento návod, ak nechcete nič inštalovať na svoj počítač.**  
Codespaces vám poskytuje bezplatné VS Code v prehliadači so všetkými závislosťami už predinštalovanými.

---

## 1.  Prečo Codespaces?

| Výhoda | Čo to znamená pre vás |
|--------|----------------------|
| ✅ Žiadne inštalácie | Funguje na Chromebooku, iPade, školských PC… |
| ✅ Predpripravený vývojársky kontajner | Python 3, Node.js, .NET, Java už sú súčasťou |
| ✅ Bezplatná kvóta | Osobné účty majú **120 core-hodín / 60 GB-hodín mesačne** |

> 💡 **Tip**  
> Udržujte si kvótu v poriadku tým, že **zastavíte** alebo **vymažete** neaktívne codespaces  
> (Zobraziť ▸ Príkazová paleta ▸ *Codespaces: Stop Codespace*).

---

## 2.  Vytvorte Codespace (jedným klikom)

1. **Forknite** tento repozitár (vpravo hore tlačidlo **Fork**).  
2. Vo svojom forku kliknite na **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialógové okno s tlačidlami na vytvorenie codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Otvorí sa okno VS Code v prehliadači a začne sa budovať vývojársky kontajner.
Prvýkrát to trvá **približne 2 minúty**.

## 3. Pridajte svoj API kľúč (bezpečne)

### Možnosť A Codespaces Secrets — Odporúčané

1. ⚙️ Ikona ozubeného kolieska -> Príkazová paleta -> Codespaces : Manage user secret -> Pridať nový secret.
2. Názov: OPENAI_API_KEY
3. Hodnota: vložte svoj kľúč → Pridať secret

Hotovo—náš kód ho automaticky rozpozná.

### Možnosť B .env súbor (ak ho naozaj potrebujete)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho natívnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.