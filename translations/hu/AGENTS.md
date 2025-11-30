<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:09:24+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hu"
}
-->
# AGENTS.md

## Projektáttekintés

Ez a tároló egy átfogó, 21 leckéből álló tananyagot tartalmaz, amely a generatív mesterséges intelligencia alapjait és alkalmazásfejlesztését tanítja. A kurzus kezdőknek készült, és a legfontosabb fogalmaktól a gyártásra kész alkalmazások építéséig mindent lefed.

**Kulcstechnológiák:**
- Python 3.9+ könyvtárakkal: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js-szel és könyvtárakkal: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API és GitHub Modellek
- Jupyter Notebooks interaktív tanuláshoz
- Dev Containers az egységes fejlesztési környezethez

**Tároló felépítése:**
- 21 számozott lecke könyvtár (00-21), amelyek README fájlokat, kódpéldákat és feladatokat tartalmaznak
- Többféle megvalósítás: Python, TypeScript, és néha .NET példák
- Fordítások könyvtára több mint 40 nyelvi verzióval
- Központosított konfiguráció `.env` fájlon keresztül (használja a `.env.copy` sablont)

## Beállítási parancsok

### Tároló kezdeti beállítása

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python környezet beállítása

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript beállítása

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container beállítása (ajánlott)

A tároló tartalmaz egy `.devcontainer` konfigurációt GitHub Codespaces vagy VS Code Dev Containers számára:

1. Nyissa meg a tárolót GitHub Codespaces-ben vagy VS Code-ban a Dev Containers bővítménnyel
2. A Dev Container automatikusan:
   - Telepíti a Python függőségeket a `requirements.txt` fájlból
   - Lefuttatja a post-create scriptet (`.devcontainer/post-create.sh`)
   - Beállítja a Jupyter kernelt

## Fejlesztési munkafolyamat

### Környezeti változók

Minden API-hozzáférést igénylő lecke a `.env` fájlban definiált környezeti változókat használja:

- `OPENAI_API_KEY` - OpenAI API-hoz
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service-hez
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI végpont URL-je
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion modell telepítési neve
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings modell telepítési neve
- `AZURE_OPENAI_API_VERSION` - API verzió (alapértelmezett: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face modellekhez
- `GITHUB_TOKEN` - GitHub Modellekhez

### Python példák futtatása

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript példák futtatása

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks futtatása

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Különböző lecketípusokkal való munka

- **"Learn" leckék**: README.md dokumentációra és fogalmakra fókuszálnak
- **"Build" leckék**: Működő kódpéldákat tartalmaznak Pythonban és TypeScriptben
- Minden lecke tartalmaz egy README.md fájlt elmélettel, kódismertetőkkel és videós tartalmakra mutató hivatkozásokkal

## Kódstílus irányelvek

### Python

- Használja a `python-dotenv` könyvtárat a környezeti változók kezeléséhez
- Importálja az `openai` könyvtárat az API interakciókhoz
- Használja a `pylint` eszközt linteléshez (néhány példa tartalmazza a `# pylint: disable=all` megjegyzést az egyszerűség kedvéért)
- Kövesse a PEP 8 elnevezési konvenciókat
- API hitelesítő adatokat `.env` fájlban tárolja, soha ne a kódban

### TypeScript

- Használja a `dotenv` csomagot a környezeti változókhoz
- TypeScript konfiguráció `tsconfig.json` fájlban minden alkalmazáshoz
- Használja az `@azure/openai` vagy `@azure-rest/ai-inference` könyvtárakat az Azure szolgáltatásokhoz
- Használja a `nodemon` eszközt automatikus újratöltéssel a fejlesztéshez
- Építse meg a futtatás előtt: `npm run build`, majd `npm start`

### Általános konvenciók

- Tartsa a kódpéldákat egyszerűnek és oktatónak
- Tartalmazzon megjegyzéseket a kulcsfogalmak magyarázatához
- Minden lecke kódja legyen önállóan futtatható
- Használjon következetes elnevezést: `aoai-` előtag az Azure OpenAI-hoz, `oai-` az OpenAI API-hoz, `githubmodels-` a GitHub Modellekhez

## Dokumentációs irányelvek

### Markdown stílus

- Minden URL-t `[szöveg](../../url)` formátumban kell megadni, extra szóközök nélkül
- Relatív hivatkozásoknak `./` vagy `../`-vel kell kezdődniük
- Minden Microsoft domainre mutató hivatkozásnak tartalmaznia kell követési azonosítót: `?WT.mc_id=academic-105485-koreyst`
- Ne használjon ország-specifikus lokalizációkat az URL-ekben (kerülje a `/en-us/`-t)
- Képek a `./images` mappában tárolva, leíró nevekkel
- Fájlnévben csak angol karakterek, számok és kötőjelek legyenek

### Fordítási támogatás

- A tároló több mint 40 nyelvet támogat automatikus GitHub Actions segítségével
- Fordítások a `translations/` könyvtárban tárolva
- Ne küldjön be részleges fordításokat
- Gépi fordításokat nem fogadunk el
- Fordított képek a `translated_images/` könyvtárban tárolva

## Tesztelés és validálás

### Beküldés előtti ellenőrzések

Ez a tároló GitHub Actions-t használ validáláshoz. PR beküldése előtt:

1. **Markdown hivatkozások ellenőrzése**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuális tesztelés**:
   - Python példák tesztelése: Aktiválja a venv-et és futtassa a szkripteket
   - TypeScript példák tesztelése: `npm install`, `npm run build`, `npm start`
   - Ellenőrizze, hogy a környezeti változók megfelelően vannak konfigurálva
   - Győződjön meg róla, hogy az API kulcsok működnek a kódpéldákkal

3. **Kódpéldák**:
   - Győződjön meg róla, hogy minden kód hiba nélkül fut
   - Tesztelje az Azure OpenAI és OpenAI API-val, ahol alkalmazható
   - Ellenőrizze, hogy a példák működnek-e a GitHub Modellekkel, ahol támogatott

### Nincs automatizált tesztelés

Ez egy oktatási tároló, amely oktatóanyagokra és példákra fókuszál. Nincsenek egységtesztek vagy integrációs tesztek. A validálás főként:
- Kódpéldák manuális tesztelése
- GitHub Actions Markdown validáláshoz
- Közösségi véleményezés az oktatási tartalomról

## Pull Request irányelvek

### Beküldés előtt

1. Tesztelje a kódváltoztatásokat Pythonban és TypeScriptben, ahol alkalmazható
2. Futtassa a Markdown validálást (automatikusan elindul PR esetén)
3. Győződjön meg róla, hogy minden Microsoft URL tartalmaz követési azonosítót
4. Ellenőrizze, hogy a relatív hivatkozások érvényesek
5. Ellenőrizze, hogy a képek megfelelően vannak hivatkozva

### PR cím formátuma

- Használjon leíró címeket: `[Lecke 06] Python példa elírás javítása` vagy `README frissítése a 08-as leckéhez`
- Hivatkozzon probléma számokra, ahol alkalmazható: `Fixes #123`

### PR leírás

- Magyarázza el, mi változott és miért
- Linkeljen kapcsolódó problémákra
- Kódváltoztatások esetén adja meg, mely példákat tesztelte
- Fordítási PR-ek esetén tartalmazza az összes fájlt a teljes fordításhoz

### Hozzájárulási követelmények

- Írja alá a Microsoft CLA-t (automatikus az első PR-nél)
- Forkolja a tárolót a saját fiókjába, mielőtt változtatásokat végez
- Egy PR logikai változtatásonként (ne kombináljon nem kapcsolódó javításokat)
- Tartsa a PR-eket fókuszáltan és kicsiben, ha lehetséges

## Gyakori munkafolyamatok

### Új kódpélda hozzáadása

1. Navigáljon a megfelelő lecke könyvtárba
2. Hozzon létre példát a `python/` vagy `typescript/` alkönyvtárban
3. Kövesse az elnevezési konvenciót: `{provider}-{example-name}.{py|ts|js}`
4. Tesztelje valódi API hitelesítő adatokkal
5. Dokumentálja az új környezeti változókat a lecke README fájljában

### Dokumentáció frissítése

1. Szerkessze a README.md fájlt a lecke könyvtárában
2. Kövesse a Markdown irányelveket (követési azonosítók, relatív hivatkozások)
3. A fordítások GitHub Actions által kezelve (ne szerkessze manuálisan)
4. Tesztelje, hogy minden hivatkozás érvényes

### Dev Containers használata

1. A tároló tartalmazza a `.devcontainer/devcontainer.json` fájlt
2. A post-create script automatikusan telepíti a Python függőségeket
3. Python és Jupyter bővítmények előre konfigurálva
4. A környezet az `mcr.microsoft.com/devcontainers/universal:2.11.2` alapú

## Telepítés és publikálás

Ez egy oktatási tároló - nincs telepítési folyamat. A tananyagot az alábbiak használják:

1. **GitHub tároló**: Közvetlen hozzáférés a kódhoz és dokumentációhoz
2. **GitHub Codespaces**: Azonnali fejlesztési környezet előre konfigurált beállítással
3. **Microsoft Learn**: Tartalom szindikálása az hivatalos tanulási platformra
4. **docsify**: Dokumentációs oldal Markdown alapján (lásd `docsifytopdf.js` és `package.json`)

### Dokumentációs oldal építése

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Hibakeresés

### Gyakori problémák

**Python importálási hibák**:
- Győződjön meg róla, hogy a virtuális környezet aktiválva van
- Futtassa a `pip install -r requirements.txt` parancsot
- Ellenőrizze, hogy a Python verzió 3.9+

**TypeScript build hibák**:
- Futtassa az `npm install` parancsot az adott alkalmazás könyvtárában
- Ellenőrizze, hogy a Node.js verzió kompatibilis
- Törölje a `node_modules` könyvtárat, és telepítse újra, ha szükséges

**API hitelesítési hibák**:
- Ellenőrizze, hogy a `.env` fájl létezik és helyes értékeket tartalmaz
- Győződjön meg róla, hogy az API kulcsok érvényesek és nem jártak le
- Ellenőrizze, hogy a végpont URL-ek helyesek az Ön régiójában

**Hiányzó környezeti változók**:
- Másolja a `.env.copy` fájlt `.env` néven
- Töltse ki az összes szükséges értéket az aktuális leckéhez
- Indítsa újra az alkalmazást a `.env` frissítése után

## További források

- [Kurzus beállítási útmutató](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Hozzájárulási irányelvek](./CONTRIBUTING.md)
- [Magatartási kódex](./CODE_OF_CONDUCT.md)
- [Biztonsági irányelvek](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Haladó kódminták gyűjteménye](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekt-specifikus megjegyzések

- Ez egy **oktatási tároló**, amely a tanulásra fókuszál, nem gyártási kódra
- A példák szándékosan egyszerűek és oktatási célokat szolgálnak
- A kódminőség az oktatási érthetőséggel van egyensúlyban
- Minden lecke önálló, és külön-külön elvégezhető
- A tároló több API szolgáltatót támogat: Azure OpenAI, OpenAI és GitHub Modellek
- A tartalom többnyelvű, automatikus fordítási munkafolyamatokkal
- Aktív közösség a Discordon kérdések és támogatás céljából

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.