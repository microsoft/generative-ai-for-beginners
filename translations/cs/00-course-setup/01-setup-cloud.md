# Nastavení v cloudu ☁️ – GitHub Codespaces

**Použijte tento návod, pokud nechcete nic instalovat lokálně.**  
Codespaces vám poskytne bezplatnou instanci VS Code v prohlížeči se všemi předinstalovanými závislostmi.

---

## 1.  Proč Codespaces?

| Výhoda | Co to pro vás znamená |
|---------|----------------------|
| ✅ Žádné instalace | Funguje na Chromebooku, iPadu, školních počítačích… |
| ✅ Předpřipravený vývojový kontejner | Python 3, Node.js, .NET, Java už uvnitř |
| ✅ Zdarma kvóta | Osobní účty mají **120 core-hodin / 60 GB-hodin za měsíc** |

> 💡 **Tip**  
> Udržujte svou kvótu zdravou tím, že **zastavíte** nebo **smažete** neaktivní codespaces  
> (Zobrazit ▸ Příkazová paleta ▸ *Codespaces: Stop Codespace*).

---

## 2.  Vytvoření Codespace (jedno kliknutí)

1. **Forkněte** tento repozitář (vpravo nahoře tlačítko **Fork**).  
2. Ve svém forku klikněte na **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog ukazující tlačítka pro vytvoření codespace](../../../translated_images/cs/who-will-pay.4c0609b1c7780f44.webp)

✅ Otevře se okno VS Code v prohlížeči a začne se stavět vývojový kontejner.
Tento proces trvá **~2 minuty** napoprvé.

## 3. Přidejte svůj API klíč (bezpečným způsobem)

### Možnost A Secrets Codespaces — Doporučeno

1. ⚙️ Ikona ozubeného kolečka -> Příkazová paleta -> Codespaces : Spravovat uživatelské tajemství -> Přidat nové tajemství.
2. Název: OPENAI_API_KEY
3. Hodnota: vložte svůj klíč → Přidat tajemství

Tím je hotovo – náš kód si ho automaticky načte.

### Možnost B .env soubor (pokud ho opravdu potřebujete)

```bash
cp .env.copy .env
code .env         # vyplňte OPENAI_API_KEY=váš_klíč_zde
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->