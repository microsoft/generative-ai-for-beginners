# Fejlesztett funkciók és fejlesztési ütemterv

Ez a dokumentum a Generatív AI kezdőknek tananyaghoz javasolt fejlesztéseket és javításokat vázolja fel, átfogó kódáttekintés és iparági legjobb gyakorlatok elemzése alapján.

## Vezetői összefoglaló

A kódalap biztonságát, kódminőségét és oktatási hatékonyságát elemeztük. Ez a dokumentum javaslatokat nyújt az azonnali javításokra, rövid távú fejlesztésekre és hosszú távú fejlesztésekre.

---

## 1. Biztonsági fejlesztések (Prioritás: Kritikus)

### 1.1 Azonnali javítások (Teljesítve)

| Probléma | Érintett fájlok | Állapot |
|----------|-----------------|---------|
| Keménykódolt SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Javítva |
| Hiányzó környezeti validáció | Több JS/TS fájl | Javítva |
| Biztonságtalan függvényhívások | `11-integrating-with-function-calling/js-githubmodels/app.js` | Javítva |
| Fájllekérdezési szivárgások | `08-building-search-applications/scripts/` | Javítva |
| Hiányzó kérések időkorlátja | `09-building-image-applications/python/` | Javítva |

### 1.2 Javasolt további biztonsági funkciók

1. **Korlátozási példák**
   - Példakód hozzáadása az API hívások korlátozására
   - Exponenciális visszaléptetési minták bemutatása

2. **API kulcs forgatás**
   - Dokumentáció hozzáadása az API kulcsok legjobb forgatási gyakorlatairól
   - Azure Key Vault vagy hasonló szolgáltatások használatának példái

3. **Tartalombiztonsági integráció**
   - Példák hozzáadása az Azure Content Safety API használatára
   - Bemenet/kimenet moderációs minták demonstrálása

---

## 2. Kódminőség javítások

### 2.1 Konfigurációs fájlok hozzáadva

| Fájl | Cél |
|-------|-----|
| `.eslintrc.json` | JavaScript/TypeScript lintelési szabályok |
| `.prettierrc` | Kódformázási szabványok |
| `pyproject.toml` | Python eszközkonfiguráció (Black, Ruff, mypy) |

### 2.2 Megosztott segédprogramok létrehozva

Új `shared/python/` modul:
- `env_utils.py` - Környezeti változók kezelése
- `input_validation.py` - Bemenet érvényesítés és tisztítás
- `api_utils.py` - Biztonságos API kéréscsomagok

### 2.3 Javasolt kódfejlesztések

1. **Típusjelölések lefedettsége**
   - Típusjelölések hozzáadása minden Python fájlhoz
   - Szigorú TypeScript mód engedélyezése minden TS projektben

2. **Dokumentációs szabványok**
   - Docstringek hozzáadása minden Python függvényhez
   - JSDoc kommentek hozzáadása minden JavaScript/TypeScript függvényhez

3. **Tesztelési keretrendszer**
   - Pytest konfiguráció és példatesztek hozzáadása
   - Jest konfiguráció hozzáadása JavaScript/TypeScript-hez

---

## 3. Oktatási fejlesztések

### 3.1 Új lecketémák

1. **Biztonság az AI alkalmazásokban** (javasolt 22. lecke)
   - Prompt injekciós támadások és védekezések
   - API kulcs kezelés
   - Tartalom moderáció
   - Korlátozás és visszaélés-megelőzés

2. **Termelési környezet telepítése** (javasolt 23. lecke)
   - Konténerizáció Dockerrel
   - CI/CD folyamatok
   - Monitorozás és naplózás
   - Költségkezelés

3. **Haladó RAG technikák** (javasolt 24. lecke)
   - Hibrid keresés (kulcsszó + szemantikus)
   - Újrangsorolási stratégiák
   - Többmodalitású RAG
   - Értékelési mutatók

### 3.2 Meglévő lecke fejlesztések

| Lecke | Javasolt fejlesztés |
|--------|---------------------|
| 06 - Szöveg generálás | Streaming válasz példák hozzáadása |
| 07 - Csevegőalkalmazások | Beszélgetésmemória minták hozzáadása |
| 08 - Keresőalkalmazások | Vektoradatbázis összehasonlítás hozzáadása |
| 09 - Kép generálás | Kép szerkesztési/variációs példák hozzáadása |
| 11 - Függvényhívás | Párhuzamos függvényhívás hozzáadása |
| 15 - RAG | Darabolási stratégia összehasonlítás hozzáadása |
| 17 - AI Ügynökök | Többügynökös koordináció hozzáadása |

---

## 4. API modernizáció

### 4.1 Frissítendő elavult API minták

| Régi minta | Új minta | Érintett fájlok |
|------------|----------|-----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` kliens | Több szkript a `08-building-search-applications/` könyvtárban |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Több jegyzetfüzet |
| `df.append()` (pandas) | `pd.concat()` | RAG jegyzetfüzet |

### 4.2 Új API funkciók bemutatása

1. **Strukturált kimenetek** (OpenAI)
   - JSON mód
   - Függvényhívás szigorú sémákkal

2. **Látási képességek**
   - Kép elemzés GPT-4V-vel
   - Többmodalitású promptok

3. **Asszisztensek API**
   - Kódértelmező
   - Fájlkeresés
   - Egyedi eszközök

---

## 5. Infrastruktúra fejlesztések

### 5.1 CI/CD fejlesztések

A jelenlegi munkafolyamatok markdown érvényesítést végeznek. Javasolt kiegészítések:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Biztonsági vizsgálat

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Fejlesztői élmény javítások

### 6.1 DevContainer fejlesztések

Frissítés `.devcontainer/devcontainer.json` fájlban:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Interaktív játszótér

Érdemes megfontolni:
- Jupyter jegyzetfüzetek előre kitöltött API kulcsokkal (környezeti változókon keresztül)
- Gradio/Streamlit demók vizuális tanulók számára
- Interaktív kvízek tudásfelméréshez

---

## 7. Többnyelvű támogatás

### 7.1 Jelenlegi nyelvi lefedettség

| Technológia | Lefedett leckék | Állapot |
|-------------|-----------------|---------|
| Python | Mind | Teljes |
| TypeScript | 06-09, 11 | Részleges |
| JavaScript | 06-08, 11 | Részleges |
| .NET/C# | Néhány | Részleges |

### 7.2 Javasolt kiegészítések

1. **Go** - Növekvő AI/ML eszköztámogatás
2. **Rust** - Teljesítménykritikus alkalmazások
3. **Java/Kotlin** - Vállalati alkalmazások

---

## 8. Teljesítményoptimalizálások

### 8.1 Kód szintű optimalizálások

1. **Async/Await minták**
   - Async példák hozzáadása tömeges feldolgozáshoz
   - Párhuzamos API hívások demonstrálása

2. **Gyorsítótárazási stratégiák**
   - Egyedi beágyazás gyorsítótár példák hozzáadása
   - Válaszgyorsítótárazási minták bemutatása

3. **Token optimalizálás**
   - Tiktoken használati példák hozzáadása
   - Prompt tömörítési technikák bemutatása

### 8.2 Költségoptimalizációs példák

Példák hozzáadása:
- Modellek kiválasztása a feladat összetettsége alapján
- Prompt tervezés a tokenhatékonyság érdekében
- Tömeges feldolgozás a költségek csökkentésére

---

## 9. Akadálymentesítés és internacionalizáció

### 9.1 Jelenlegi fordítási állapot

| Nyelv | Állapot |
|--------|---------|
| Angol | Teljes |
| Kínai (egyszerűsített) | Teljes |
| Japán | Teljes |
| Koreai | Teljes |
| Spanyol | Részleges |
| Portugál | Részleges |
| Török | Részleges |
| Lengyel | Részleges |

### 9.2 Akadálymentesítési fejlesztések

1. Minden képhez alt szöveg hozzáadása
2. Kódrészletek megfelelő szintaxiskiemelése
3. Videótartalmakhoz átiratok hozzáadása
4. Színkontraszt megfeleltetése WCAG irányelveknek

---

## 10. Megvalósítási prioritások

### 1. fázis: Azonnali (1-2. hét)
- [x] Kritikus biztonsági problémák javítása
- [x] Kódminőség konfiguráció hozzáadása
- [x] Megosztott segédprogramok létrehozása
- [x] Biztonsági irányelvek dokumentálása

### 2. fázis: Rövid távú (3-4. hét)
- [ ] Elavult API minták frissítése
- [ ] Típusjelölések hozzáadása minden Python fájlhoz
- [ ] CI/CD munkafolyamatok hozzáadása kódminőséghez
- [ ] Biztonsági vizsgálati munkafolyamat létrehozása

### 3. fázis: Középtávú (2-3. hónap)
- [ ] Új biztonsági lecke hozzáadása
- [ ] Termelési környezet telepítési lecke hozzáadása
- [ ] DevContainer beállítás fejlesztése
- [ ] Interaktív demók hozzáadása

### 4. fázis: Hosszú távú (4. hónap+)
- [ ] Haladó RAG lecke hozzáadása
- [ ] Nyelvi lefedettség bővítése
- [ ] Átfogó tesztcsomag létrehozása
- [ ] Tanúsítási program kidolgozása

---

## Összefoglalás

Ez az ütemterv strukturált megközelítést nyújt a Generatív AI kezdőknek tananyag fejlesztéséhez. A biztonsági problémák kezelése, az API-k modernizálása és az oktatási tartalom bővítése révén a kurzus jobban felkészíti a tanulókat a valós AI alkalmazásfejlesztésre.

Kérdések vagy hozzájárulások esetén kérjük, nyisson egy issue-t a GitHub tárházban.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felmentés**:
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) mesterséges intelligencia fordító szolgáltatás segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén profi, emberi fordítást javaslunk. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->