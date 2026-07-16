# Továbbfejlesztett funkciók és fejlesztési ütemterv

Ez a dokumentum a Generative AI for Beginners tananyagra vonatkozó javasolt fejlesztéseket és fejlesztéseket vázolja fel, egy átfogó kódáttekintés és az iparági legjobb gyakorlatok elemzése alapján.

## Vezetői összefoglaló

A kódbázist biztonság, kódminőség és oktatási hatékonyság szempontjából elemeztük. Ez a dokumentum ajánlásokat nyújt az azonnali javításokra, rövid távú fejlesztésekre és jövőbeni fejlesztésekre.

---

## 1. Biztonsági fejlesztések (Prioritás: Kritikus)

### 1.1 Azonnali javítások (Elkészült)

| Probléma | Érintett fájlok | Állapot |
|-------|----------------|--------|
| Keménykódolt SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Javítva |
| Hiányzó környezeti változó ellenőrzés | Több JS/TS fájl | Javítva |
| Nem biztonságos függvényhívások | `11-integrating-with-function-calling/js-githubmodels/app.js` | Javítva |
| Fájlkezelő szivárgások | `08-building-search-applications/scripts/` | Javítva |
| Hiányzó kérési timeoutok | `09-building-image-applications/python/` | Javítva |

### 1.2 Ajánlott további biztonsági funkciók

1. **Ratelimiting példák**
   - Példakód hozzáadása az API hívásokratelimitelésének megvalósítására
   - Exponenciális visszalépési minták bemutatása

2. **API kulcs forgatás**
   - Dokumentáció az API kulcsok forgatásának legjobb gyakorlatairól
   - Példák Azure Key Vault vagy hasonló szolgáltatások használatára

3. **Tartalom-biztonság integráció**
   - Példák Azure Content Safety API használatára
   - Bemenet/kimenet moderációs minták bemutatása

---

## 2. Kódminőség fejlesztések

### 2.1 Konfigurációs fájlok hozzáadva

| Fájl | Cél |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript lint szabályok |
| `.prettierrc` | Kódformázási szabványok |
| `pyproject.toml` | Python eszközkonfiguráció (Black, Ruff, mypy) |

### 2.2 Megosztott segédprogramok létrehozva

Új `shared/python/` modul:
- `env_utils.py` - Környezeti változó kezelése
- `input_validation.py` - Bemenet érvényesítés és tisztítás
- `api_utils.py` - Biztonságos API kérés wrapper-ek

### 2.3 Ajánlott kódfejlesztések

1. **Típusjelzések lefedettsége**
   - Típusjelzések hozzáadása minden Python fájlhoz
   - Szigorú TypeScript mód engedélyezése minden TS projektben

2. **Dokumentációs szabványok**
   - Docstringek hozzáadása minden Python függvényhez
   - JSDoc kommentek hozzáadása minden JavaScript/TypeScript függvényhez

3. **Tesztelési keretrendszer**
   - pytest konfiguráció és példa tesztek hozzáadása _(elvégezve: pytest konfiguráció a `pyproject.toml`-ban; példa tesztek a megosztott segédprogramokhoz a [`tests/`](../../../tests) mappában, CI-ben futtatva)_
   - Jest konfiguráció hozzáadása JavaScript/TypeScript-hez

---

## 3. Oktatási fejlesztések

### 3.1 Új lecketémák

1. **Biztonság az AI alkalmazásokban** (Javasolt 22. lecke)
   - Prompt befecskendezési támadások és védekezések
   - API kulcs kezelés
   - Tartalom moderáció
   - Ratelimit a visszaélések megelőzésére

2. **Produktív környezetbe telepítés** (Javasolt 23. lecke)
   - Docker konténerizáció
   - CI/CD folyamatok
   - Monitoring és naplózás
   - Költségmenedzsment

3. **Haladó RAG technikák** (Javasolt 24. lecke)
   - Hibrid keresés (kulcsszó + szemantikus)
   - Újrarangsorolási stratégiák
   - Többmodalitású RAG
   - Értékelési metrikák

### 3.2 Meglévő lecke fejlesztések

| Lecke | Ajánlott fejlesztés |
|--------|------------------------|
| 06 - Szöveg generálás | Streaming válasz példák hozzáadása |
| 07 - Csevegőalkalmazások | Beszélgetés memória minták hozzáadása |
| 08 - Keresőalkalmazások | Vektor adatbázis összehasonlítás hozzáadása |
| 09 - Kép generálás | Kép szerkesztési/változtatási példák hozzáadása |
| 11 - Függvényhívás | Párhuzamos függvényhívás hozzáadása |
| 15 - RAG | Bontási stratégia összehasonlítás hozzáadása |
| 17 - AI ügynökök | Többügynökös koordináció hozzáadása |

---

## 4. API modernizáció

### 4.1 Elavult API minták (Migráció elkészült)

Minden Python és TypeScript **chat** példa át lett migrálva a Chat Completions API-ról a **Responses API**-ra (`client.responses.create(...)` → `response.output_text`).

| Régi minta | Új minta | Állapot |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Elkészült |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Elkészült |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` csomag `client.responses.create()` → `response.output_text` | Elkészült |
| `df.append()` (pandas) | `pd.concat()` | Elkészült |

> **Megjegyzés:** A Microsoft Foundry Modellek, amelyek az `azure-ai-inference` / `@azure-rest/ai-inference` SDK-t (`client.complete()`) használják, megmaradnak a Model Inference API-n, amely nem támogatja a Responses API-t. Az `AzureOpenAI()` szándékosan megtartva ott, ahol még érvényes (beágyazások és képalkotás).

### 4.2 Bemutatandó új API funkciók

1. **Strukturált kimenetek** (OpenAI)
   - JSON mód
   - Szigorú séma szerinti függvényhívás

2. **Látási képességek**
   - Kép elemzés GPT-4o (látás) használatával
   - Többmodalitású promptok

3. **Responses API beépített eszközei** (felváltja a régi Assistants API-t)
   - Kód interpreter
   - Fájlkeresés
   - Webkeresés és egyéni eszközök

---

## 5. Infrastruktúra fejlesztések

### 5.1 CI/CD fejlesztések

Megvalósítva a [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml) fájlban: Python lintelés/formázás (Ruff + Black) **kötelező** a karbantartott `shared/` segédprogram modulon, és **ajánlott** a tananyag többi részén, plusz egy ajánlott ESLint áttekintés JavaScript/TypeScript-re. Az illusztratív alapvonal:

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

Megvalósítva a [`.github/workflows/security.yml`](../../../.github/workflows/security.yml) fájlban: CodeQL elemzés Python és JavaScript/TypeScript nyelvekre (push, pull kérés, és heti ütemezés szerint), valamint függőségellenőrzés pull kéréskor. Az illusztratív alapvonal:

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

## 6. Fejlesztői élmény fejlesztések

### 6.1 DevContainer fejlesztések

Megvalósítva a [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) és [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh) fájlokban: a konténer most már tartalmazza a Pylance-t, a Black formázót, Ruffot, ESLint-et, Prettier-t és Copilot kiterjesztéseket, engedélyezi a mentéskor formázást, amely össze van kötve a repo Black/Prettier konfigurációjával, és telepíti a fejlesztői eszközöket (`ruff`, `black`, `mypy`, `pytest`), így a [code-quality workflow](../../../.github/workflows/code-quality.yml) helyileg reprodukálható. Az `mcr.microsoft.com/devcontainers/universal` alap kép már tartalmazza a Pythont és Node-ot, így további funkciók nem szükségesek. Az illusztratív alapvonal:

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

### 6.2 Interaktív játéktér

Érdemes fontolóra venni a következőket:
- Jupyter notebookok előre kitöltött API kulcsokkal (környezeti változókon keresztül)
- Gradio/Streamlit demók vizuális tanulók számára
- Interaktív kvízek a tudás felmérésére

---

## 7. Többnyelvű támogatás

### 7.1 Jelenlegi nyelvi lefedettség

| Technológia | Lefedett leckék | Állapot |
|------------|-----------------|--------|
| Python | Mind | Teljes |
| TypeScript | 06-09, 11 | Részleges |
| JavaScript | 06-08, 11 | Részleges |
| .NET/C# | Néhány | Részleges |

### 7.2 Ajánlott kiegészítések

1. **Go** - Növekvő AI/ML eszközökkel
2. **Rust** - Teljesítménykritikus alkalmazások
3. **Java/Kotlin** - Vállalati alkalmazások

---

## 8. Teljesítményoptimalizálások

### 8.1 Kód szintű optimalizálások

1. **Async/Await minták**
   - Async példák hozzáadása kötegelt feldolgozásra
   - Párhuzamos API hívások bemutatása

2. **Gyorsítótárazási stratégiák**
   - Beágyazás gyorsítótárazási példák hozzáadása
   - Válasz gyorsítótárazási minták bemutatása

3. **Token optimalizálás**
   - tiktoken használati példák hozzáadása
   - Prompt tömörítési technikák bemutatása

### 8.2 Költségoptimalizálási példák

Példák hozzáadása, amelyek bemutatják:
- Modell kiválasztása a feladat komplexitása alapján
- Prompt mérnökség a token hatékonyság érdekében
- Kötegelt feldolgozás nagy mennyiségű művelethez

---

## 9. Akadálymentesítés és nemzetköziesítés

### 9.1 Jelenlegi fordítási állapot

Minden fordítás **készen áll** és automatikusan készül az [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) segítségével, amely több mint 50 nyelvű verzióban tartja szinkronban a tananyagot az angol forrással. A fordított tartalom a `translations/` alatt található, a lokalizált képek pedig a `translated_images/` mappában; az elérhető nyelvek teljes listája a repository README-jének tetején található.

| Szempont | Állapot |
|--------|--------|
| Fordítás lefedettség | Teljes — 50+ nyelv, minden lecke |
| Fordítási módszer | Automatikus, az [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) által |
| Szinkron az angol forrással | Igen — automatikusan újragenerálva |

### 9.2 Akadálymentesítési fejlesztések

1. Alt szöveg hozzáadása minden képhez
2. Biztosítani, hogy a kódpéldák megfelelő szintaxiskiemeléssel rendelkezzenek
3. Videó átiratok hozzáadása minden videós tartalomhoz
4. A színkontraszt megfeleltetése a WCAG irányelveknek

---

## 10. Megvalósítási prioritás

### 1. fázis: Azonnali (1-2. hét)
- [x] Kritikus biztonsági problémák javítása
- [x] Kódminőség konfiguráció hozzáadása
- [x] Megosztott segédprogramok létrehozása
- [x] Biztonsági irányelvek dokumentálása

### 2. fázis: Rövid táv (3-4. hét)
- [x] Elavult API minták frissítése (Chat Completions → Responses API, Python + TypeScript)
- [ ] Minden Python fájlhoz típusjelzések hozzáadása (elvégezve a karbantartott `shared/` modulon; a leckeminták egyszerűek maradtak)
- [x] CI/CD munkafolyamatok hozzáadása a kódminőségért
- [x] Biztonsági vizsgálati munkafolyamat létrehozása

### 3. fázis: Középtáv (2-3. hónap)
- [ ] Új biztonsági lecke hozzáadása
- [ ] Termelési környezetbe telepítés leckéje
- [x] DevContainer beállítás javítása
- [ ] Interaktív demók hozzáadása

### 4. fázis: Hosszú táv (4. hónap+)
- [ ] Haladó RAG lecke hozzáadása
- [ ] Nyelvi lefedettség bővítése
- [ ] Átfogó tesztcsomag hozzáadása
- [ ] Tanúsítási program létrehozása

---

## Összegzés

Ez az ütemterv strukturált megközelítést kínál a Generative AI for Beginners tananyag fejlesztésére. A biztonsági kérdések kezelése, az API-k modernizálása és az oktatási tartalom bővítése révén a kurzus jobban fel fogja készíteni a diákokat a valós AI alkalmazásfejlesztésre.

Kérdések vagy hozzájárulások esetén kérjük, nyisson egy issue-t a GitHub tárolóban.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->