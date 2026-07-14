# Felhő beállítása ☁️ – GitHub Codespaces

**Használd ezt az útmutatót, ha nem akarsz semmit helyileg telepíteni.**  
A Codespaces ingyenes, böngésző-alapú VS Code példányt ad, minden függőséggel előre telepítve.

---

## 1.  Miért Codespaces?

| Előny | Mit jelent ez neked |
|---------|----------------------|
| ✅ Telepítés nélkül | Chromebookon, iPad-en, iskolai labor PC-ken működik… |
| ✅ Előre elkészített fejlesztői konténer | Python 3, Node.js, .NET, Java már bent van |
| ✅ Ingyenes kvóta | Személyes fiókok havi **120 mag-óra / 60 GB-óra** kvótát kapnak |

> 💡 **Tipp**  
> Tartsd egészségesen a kvótádat azzal, hogy **leállítod** vagy **törlöd** az inaktív codespace-eket  
> (Nézd meg ▸ Parancs paletta ▸ *Codespaces: Stop Codespace*).

---

## 2.  Készíts Codespace-et (egy kattintás)

1. **Forkold** ezt a tárolót (jobb felső **Fork** gomb).  
2. A forkolt példányodban kattints **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/hu/who-will-pay.4c0609b1c7780f44.webp)

✅ Megnyílik egy böngészőbeli VS Code ablak és elindul a fejlesztői konténer építése.
Ez az első alkalommal **kb. 2 percet** vesz igénybe.

## 3. Add meg az API kulcsodat (biztonságos mód)

### A lehetőség Codespaces Secrets — Ajánlott

1. ⚙️ Fogaskerék ikon -> Parancs paletta -> Codespaces : Manage user secret -> Új titok hozzáadása.
2. Név: OPENAI_API_KEY
3. Érték: illeszd be a kulcsod → Titok hozzáadása

Ennyi az egész — a kódunk automatikusan megtalálja.

### B lehetőség .env fájl (ha tényleg szükséged van rá)

```bash
cp .env.copy .env
code .env         # töltsd ki OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->