# AGENTS.md

## Projekt áttekintése

Ez a tároló egy átfogó, 21 leckéből álló tananyagot tartalmaz, amely a Generatív mesterséges intelligencia alapjait és alkalmazásfejlesztést tanít. A tanfolyam kezdőknek készült, és mindent lefed az alapvető fogalmaktól a gyártásra kész alkalmazások létrehozásáig.

**Főbb technológiák:**
- Python 3.9+ könyvtárakkal: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js-sel és könyvtárakkal: `openai` (Azure OpenAI a v1 végponton keresztül + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry modellek)
- Azure OpenAI Service, OpenAI API és Microsoft Foundry Modellek (a GitHub Models 2026 július végén megszűnik)
- Jupyter notebookok az interaktív tanuláshoz
- Dev Containerek az egységes fejlesztői környezethez

**Tároló szerkezete:**
- 21 számozott lecke mappa (00-21), melyek README-ket, kódpéldákat és feladatokat tartalmaznak
- Több megvalósítás: Python, TypeScript és néha .NET példák
- Fordításokat tartalmazó mappa 40+ nyelvi változattal
- Központosított konfiguráció `.env` fájlon keresztül (a `.env.copy` sablonként használható)

## Telepítési parancsok

### Kezdeti tároló beállítás

```bash
# Klónozd a tárhelyet
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Másold a környezeti sablont
cp .env.copy .env
# Szerkeszd a .env fájlt az API kulcsaiddal és végpontjaiddal
```

### Python környezet beállítása

```bash
# Virtuális környezet létrehozása
python3 -m venv venv

# Virtuális környezet aktiválása
# macOS/Linux rendszeren:
source venv/bin/activate
# Windows rendszeren:
venv\Scripts\activate

# Függőségek telepítése
pip install -r requirements.txt
```

### Node.js/TypeScript beállítás

```bash
# Telepítse a rendszerszintű függőségeket (a dokumentációs eszközökhöz)
npm install

# Egyedi lecke TypeScript példákhoz navigáljon az adott leckéhez:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container beállítása (ajánlott)

A tároló tartalmaz `.devcontainer` konfigurációt GitHub Codespaces vagy VS Code Dev Containerek használatához:

1. Nyisd meg a tárolót GitHub Codespaces-ben vagy VS Code-ban a Dev Containers bővítménnyel
2. A Dev Container automatikusan:
   - Telepíti a Python függőségeket a `requirements.txt` alapján
   - Lefuttatja a post-create szkriptet (`.devcontainer/post-create.sh`)
   - Beállítja a Jupyter kernelt

## Fejlesztési munkafolyamat

### Környezeti változók

Minden olyan lecke, amely API hozzáférést igényel, `.env` fájlban definiált környezeti változókat használ:

- `OPENAI_API_KEY` - OpenAI API-hoz
- `AZURE_OPENAI_API_KEY` - Azure OpenAI-hoz a Microsoft Foundry-n belül (az Azure OpenAI Service már a Microsoft Foundry része: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI végpont URL-je (Foundry erőforrás-végpont)
- `AZURE_OPENAI_DEPLOYMENT` - Chat befejező modell telepítés neve
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Beágyazó modell telepítés neve
- `AZURE_OPENAI_API_VERSION` - API verzió (alapértelmezett: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face modellekhez
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modellek végpontja (több szolgáltató modellkatalógusa)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Modellek API kulcs (helyettesíti a megszűnő `GITHUB_TOKEN`-t)

### Python példák futtatása

```bash
# Navigáljon a lecke könyvtárba
cd 06-text-generation-apps/python

# Futtasson egy Python szkriptet
python aoai-app.py
```

### TypeScript példák futtatása

```bash
# Navigálás a TypeScript alkalmazás könyvtárába
cd 06-text-generation-apps/typescript/recipe-app

# A TypeScript kód fordítása
npm run build

# Az alkalmazás futtatása
npm start
```

### Jupyter notebookok futtatása

```bash
# Indítsa el a Jupyter-t a repozitórium gyökérkönyvtárában
jupyter notebook

# Vagy használja a VS Code-ot a Jupyter kiterjesztéssel
```

### Különböző lecke típusok kezelése

- **"Learn" leckék**: A README.md dokumentációra és alapelvekre fókuszálnak
- **"Build" leckék**: Működő kódpéldákat tartalmaznak Pythonban és TypeScriptben
- Minden leckének van egy README.md-je elmélettel, kódmagyarázatokkal és videós tartalmak linkjeivel

## Kódstílus irányelvek

### Python

- Használd a `python-dotenv`-et a környezeti változók kezelésére
- Importáld az `openai` könyvtárat az API műveletekhez
- Használd a `pylint`-et linteléshez (egyes példákban egyszerűsítésként `# pylint: disable=all` van)
- Kövesd a PEP 8 elnevezési konvenciókat
- Az API hitelesítő adatokat soha ne a kódban tárold, csak `.env` fájlban

### TypeScript

- Használd a `dotenv` csomagot a környezeti változók kezelésére
- TypeScript konfiguráció az `tsconfig.json`-ban minden alkalmazáshoz
- Használd az `openai` csomagot Azure OpenAI-hoz (ügyfél irányítása a `/openai/v1/` végpontra, hívás `client.responses.create`); használd az `@azure-rest/ai-inference`-t Microsoft Foundry modellekhez
- Használd a `nodemon`-t fejlesztéshez automatikus újratöltéssel
- Építsd a kódot futtatás előtt: `npm run build` majd `npm start`

### Általános konvenciók

- Tartsd a kódpéldákat egyszerűnek és oktatónak
- Tartalmazzanak kommenteket, amelyek kulcsfontosságú fogalmakat magyaráznak
- Minden lecke kódja legyen önálló és futtatható
- Használj következetes elnevezést: `aoai-` prefix Azure OpenAI-hoz, `oai-` az OpenAI API-hoz, `githubmodels-` a Microsoft Foundry modellekhez (a GitHub Models korszakból származó régi prefix megtartva)

## Dokumentációs irányelvek

### Markdown stílus

- Minden URL-nek `[text](../../url)` formátumban kell lennie, szóköz nélkül
- A relatív linkek `./` vagy `../`-val kezdődjenek
- Minden Microsoft domain link tartalmazza a követési azonosítót: `?WT.mc_id=academic-105485-koreyst`
- Ne legyenek ország-specifikus lokalizációk az URL-ben (kerüld a `/en-us/`-t)
- A képek a `./images` mappában legyenek leíró nevekkel
- Fájlnévben angol karaktereket, számokat és kötőjeleket használj

### Fordítás támogatása

- A tároló automatizált GitHub Actions segítségével támogat több mint 40 nyelvet
- A fordítások a `translations/` könyvtárban tárolódnak
- Ne küldj be részleges fordításokat
- Gépi fordításokat nem fogadunk el
- A lefordított képek a `translated_images/` könyvtárban vannak

## Tesztelés és validálás

### Beküldés előtti ellenőrzések

Ez a tároló GitHub Actions-t használ validálásra. PR beküldése előtt:

1. **Markdown hivatkozások ellenőrzése**:
   ```bash
   # A validate-markdown.yml munkafolyamat ellenőrzi:
   # - Törött relatív útvonalak
   # - Hiányzó követési azonosítók az útvonalakon
   # - Hiányzó követési azonosítók az URL-eken
   # - Ország szerinti helyi beállítású URL-ek
   # - Törött külső URL-ek
   ```

2. **Kézi tesztelés**:
   - Teszteld a Python példákat: aktiváld a venv-t és futtasd a szkripteket
   - Teszteld a TypeScript példákat: `npm install`, `npm run build`, `npm start`
   - Ellenőrizd a környezeti változók helyes beállítását
   - Ellenőrizd, hogy az API kulcsok működnek a kódpéldákkal

3. **Kódpéldák**:
   - Biztosítsd, hogy minden kód hiba nélkül fusson
   - Teszteld mind Azure OpenAI-vel, mind OpenAI API-val, ahol alkalmazható
   - Ellenőrizd, hogy a példák működnek Microsoft Foundry modellekkel, ahol támogatott

### Nincsenek automatizált tesztek

Ez egy oktatási tároló, amely oktatóanyagokra és példákra fókuszál. Nincsenek futtatható egység- vagy integrációs tesztek. A validáció főként:
- Kézi tesztelés a kódpéldákon
- GitHub Actions a Markdown validációhoz
- A közösség általi oktatási tartalom véleményezése

## Pull Request irányelvek

### Beküldés előtt

1. Teszteld a kód módosításokat Pythonban és TypeScriptben, ahol lehetséges
2. Futtasd a Markdown validálást (PR beküldésekor automatikusan indul)
3. Győződj meg arról, hogy minden Microsoft URL-en megvan a követési azonosító
4. Ellenőrizd, hogy a relatív linkek érvényesek
5. Ellenőrizd, hogy a képek helyesen hivatkozottak

### PR cím formátum

- Használj leíró címeket: `[Lesson 06] Python példa elírás javítása` vagy `README frissítés a 08. leckéhez`
- Hivatkozz issueszámokra, ha van: `Fixes #123`

### PR leírás

- Magyarázd el, mi változott és miért
- Linkelj kapcsolódó issue-kat
- Kódváltozásoknál jelöld, mely példákat tesztelted
- Fordítási PR-eknél csatolj minden fájlt a teljes fordításhoz

### Hozzájárulási követelmények

- Írd alá a Microsoft CLA-t (automatikusan az első PR-nél)
- Forkold a tárolót a saját fiókodba, mielőtt változtatnál
- Egy PR egy logikai változtatásra (ne kombinálj nem kapcsolódó javításokat)
- Amikor lehet, tartsd a PR-eket fókuszáltak és kicsik

## Gyakori munkafolyamatok

### Új kódpélda hozzáadása

1. Navigálj a megfelelő lecke mappába
2. Hozz létre példát a `python/` vagy `typescript/` almappában
3. Kövesd az elnevezési konvenciót: `{provider}-{example-name}.{py|ts|js}`
4. Teszteld a tényleges API kulcsokkal
5. Dokumentáld az új környezeti változókat a lecke README-jében

### Dokumentáció frissítése

1. Szerkeszd a README.md-t a lecke mappában
2. Kövesd a Markdown irányelveket (követési azonosítók, relatív linkek)
3. A fordításokat a GitHub Actions kezeli (ne szerkeszd kézzel)
4. Teszteld az összes hivatkozás érvényességét

### Dev Containerekkel való munka

1. A tároló tartalmaz `.devcontainer/devcontainer.json`-t
2. A post-create szkript automatikusan telepíti a Python függőségeket
3. A Python és Jupyter bővítmények előre konfiguráltak
4. A környezet a `mcr.microsoft.com/devcontainers/universal:2.11.2`-re épül

## Telepítés és közzététel

Ez egy tanulási tároló - nincs telepítési folyamat. A tananyagot a felhasználók a következő módokon használják:

1. **GitHub tároló**: Közvetlen hozzáférés a kódhoz és dokumentációhoz
2. **GitHub Codespaces**: Azonnali fejlesztői környezet előre konfigurált beállítással
3. **Microsoft Learn**: A tartalom esetlegesen megjelenik az hivatalos tanulási platformon
4. **docsify**: Dokumentációs oldal Markdownból építve (lásd `docsifytopdf.js` és `package.json`)

### Dokumentációs oldal építése

```bash
# PDF generálása a dokumentációból (ha szükséges)
npm run convert
```

## Hibakeresés

### Gyakori problémák

**Python import hibák**:
- Ellenőrizd, hogy a virtuális környezet aktiválva van
- Futtasd a `pip install -r requirements.txt` parancsot
- Ellenőrizd a Python verziót, legyen 3.9 vagy újabb

**TypeScript build hibák**:
- Futtasd az `npm install`-t az adott alkalmazás könyvtárában
- Ellenőrizd a Node.js verzió kompatibilitását
- Töröld a `node_modules` mappát és telepítsd újra, ha kell

**API hitelesítési hibák**:
- Ellenőrizd, hogy a `.env` fájl létezik és helyes értékeket tartalmaz
- Ellenőrizd, hogy az API kulcsok érvényesek és nincsenek lejárva
- Győződj meg, hogy a végpont URL-ek helyesek a régiódnak megfelelően

**Hiányzó környezeti változók**:
- Másold a `.env.copy`-t `.env`-re
- Töltsd ki az összes szükséges értéket a dolgozott leckéhez
- Indítsd újra az alkalmazást `.env` frissítés után

## Egyéb források

- [Tanfolyam beállítási útmutató](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Hozzájárulási irányelvek](./CONTRIBUTING.md)
- [Magatartási kódex](./CODE_OF_CONDUCT.md)
- [Biztonsági szabályzat](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Fejlett kódminták gyűjteménye](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektre jellemző megjegyzések

- Ez egy **oktatási tároló**, amely a tanulásra fókuszál, nem éles kódra
- A példák szándékosan egyszerűek, a fogalmak oktatását szolgálják
- A kód minősége az oktatási érthetőséget hivatott egyensúlyozni
- Minden lecke önálló, egymástól függetlenül teljesíthető
- A tároló több API szolgáltatót támogat: Azure OpenAI, OpenAI, Microsoft Foundry modellek és offline szolgáltatók, mint a Foundry Local és Ollama
- A tartalom többnyelvű, automatizált fordítási munkafolyamatokkal
- Aktív közösség Discordon kérdésekhez és támogatáshoz

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->