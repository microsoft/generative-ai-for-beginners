# Cloud Setup ☁️ – GitHub Codespaces

**Použite tento návod, ak si nechcete nič inštalovať lokálne.**  
Codespaces vám poskytuje bezplatnú inštanciu VS Code priamo v prehliadači so všetkými predinštalovanými závislosťami.

---

## 1.  Prečo Codespaces?

| Výhoda | Čo to znamená pre vás |
|---------|----------------------|
| ✅ Žiadne inštalácie | Funguje na Chromebooku, iPade, počítačoch v školskej učebni... |
| ✅ Predpripravený vývojový kontajner | Python 3, Node.js, .NET, Java už vo vnútri |
| ✅ Bezplatná kvóta | Osobné účty dostávajú **120 jadro-hodín / 60 GB-hodín mesačne** |

> 💡 **Tip**  
> Udržiavajte svoju kvótu zdravú tým, že **zastavíte** alebo **vymažete** nečinné codespace  
> (Zobraziť ▸ Príkazovú paletu ▸ *Codespaces: Stop Codespace*).

---

## 2.  Vytvorte Codespace (jedným klikom)

1. **Vytvorte fork** tohto repozitára (hore vpravo tlačidlo **Fork**).  
2. Vo svojom forku kliknite na **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialóg zobrazujúci tlačidlá na vytvorenie codespace](../../../translated_images/sk/who-will-pay.4c0609b1c7780f44.webp)

✅ Otvorí sa okno VS Code v prehliadači a začne sa budovať vývojový kontajner.
Tento proces prvýkrát trvá **~2 minúty**.

## 3. Pridajte svoj API kľúč (bezpečná cesta)

### Možnosť A Tajomstvá Codespaces — Odporúčané

1. ⚙️ Ikona ozubeného kolieska -> Príkazová paleta -> Codespaces : Spravovať používateľské tajomstvo -> Pridať nové tajomstvo.
2. Názov: OPENAI_API_KEY
3. Hodnota: vložte svoj kľúč → Pridať tajomstvo

To je všetko — náš kód ho automaticky načíta.

### Možnosť B .env súbor (ak ho naozaj potrebujete)

```bash
cp .env.copy .env
code .env         # vyplňte OPENAI_API_KEY=vaš_klúč_tu
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->