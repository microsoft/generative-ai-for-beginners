<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:56:06+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "cs"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**Použijte tento návod, pokud nechcete nic instalovat na svůj počítač.**  
Codespaces vám nabízí zdarma VS Code v prohlížeči se všemi potřebnými závislostmi už předinstalovanými.

---

## 1.  Proč Codespaces?

| Výhoda | Co to znamená pro vás |
|--------|----------------------|
| ✅ Žádné instalace | Funguje na Chromebooku, iPadu, školních počítačích… |
| ✅ Předpřipravený vývojový kontejner | Python 3, Node.js, .NET, Java už uvnitř |
| ✅ Zdarma limit | Osobní účty mají **120 core-hodin / 60 GB-hodin měsíčně** |

> 💡 **Tip**  
> Šetřete svůj limit tím, že budete **zastavovat** nebo **mazat** neaktivní codespaces  
> (Zobrazit ▸ Příkazová paleta ▸ *Codespaces: Stop Codespace*).

---

## 2.  Vytvoření Codespace (jedním kliknutím)

1. **Forkněte** tento repozitář (vpravo nahoře tlačítko **Fork**).  
2. Ve svém forku klikněte na **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog s tlačítky pro vytvoření codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Otevře se okno VS Code v prohlížeči a začne se stavět vývojový kontejner.
Poprvé to trvá **asi 2 minuty**.

## 3. Přidejte svůj API klíč (bezpečně)

### Možnost A Codespaces Secrets — Doporučeno

1. ⚙️ Ikona ozubeného kola -> Příkazová paleta -> Codespaces : Manage user secret -> Add a new secret.
2. Název: OPENAI_API_KEY
3. Hodnota: vložte svůj klíč → Add secret

Hotovo—náš kód si klíč automaticky načte.

### Možnost B .env soubor (pokud ho opravdu potřebujete)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.