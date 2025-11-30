<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:47:31+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "hu"
}
-->
# Felhőalapú beállítás ☁️ – GitHub Codespaces

**Ezt az útmutatót használd, ha nem szeretnél semmit telepíteni a saját gépedre.**  
A Codespaces egy ingyenes, böngészőalapú VS Code példányt ad, ahol minden szükséges függőség előre telepítve van.

---

## 1.  Miért érdemes a Codespaces-t választani?

| Előny | Mit jelent ez számodra |
|-------|-----------------------|
| ✅ Nincs szükség telepítésre | Működik Chromebookon, iPaden, iskolai gépeken… |
| ✅ Előre elkészített fejlesztői konténer | Python 3, Node.js, .NET, Java már benne van |
| ✅ Ingyenes kvóta | Személyes fiókoknak **120 magóra / 60 GB-óra havonta** jár |

> 💡 **Tipp**  
> Vigyázz a kvótádra: **állítsd le** vagy **töröld** a nem használt codespace-eket  
> (Nézet ▸ Parancspaletta ▸ *Codespaces: Stop Codespace*).

---

## 2.  Codespace létrehozása (egy kattintás)

1. **Forkold** ezt a repót (jobb felső sarokban a **Fork** gomb).  
2. A saját forkodban kattints: **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Párbeszédablak, ahol codespace-et lehet létrehozni](../../../00-course-setup/images/who-will-pay.webp)

✅ Megnyílik egy böngészős VS Code ablak, és elindul a fejlesztői konténer építése.
Ez első alkalommal **kb. 2 percet** vesz igénybe.

## 3. Add hozzá az API kulcsodat (biztonságosan)

### A lehetőség: Codespaces Secrets — Ajánlott

1. ⚙️ Fogaskerék ikon -> Parancspaletta -> Codespaces : Manage user secret -> Add a new secret.
2. Név: OPENAI_API_KEY
3. Érték: másold be a kulcsodat → Add secret

Ennyi az egész—a kód automatikusan felismeri majd.

### B lehetőség: .env fájl (ha tényleg szükséged van rá)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Jogi nyilatkozat**:
Ez a dokumentum AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.