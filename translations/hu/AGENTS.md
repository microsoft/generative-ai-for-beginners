# AGENTS.md

## Projekt áttekintés

Ez a tárhely egy átfogó, 21 leckéből álló tananyagot tartalmaz, amely a Generatív AI alapjait és alkalmazásfejlesztést tanít. A kurzus kezdőknek készült, és mindent lefed az alapfogalmaktól a termelésre kész alkalmazások elkészítéséig.

**Fő technológiák:**
- Python 3.9+ könyvtárakkal: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js-sel és könyvtárakkal: `openai` (Azure OpenAI a v1 végponton + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry modellek)
- Azure OpenAI Szolgáltatás, OpenAI API és Microsoft Foundry Modellek (a GitHub Modellek 2026 július végén megszűnnek)
- Jupyter jegyzetfüzetek interaktív tanuláshoz
- Fejlesztői konténerek az egységes fejlesztőkörnyezetért

**A tárhely szerkezete:**
- 21 számozott lecke könyvtár (00-21), amelyek README-ket, kód példákat és feladatokat tartalmaznak
- Több megvalósítás: Python, TypeScript és néha .NET példák
- Fordítások könyvtár 40+ nyelvi verzióval
- Központi konfiguráció `.env` fájlban (használd a `.env.copy` sablonként)

## Beállító parancsok

### Kezdeti tárhely beállítás

```bash
# Klónozd a tárat
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Másold az környezeti sablont
cp .env.copy .env
# Szerkeszd a .env fájlt az API kulcsaid és végpontjaid megadásával
```

### Python környezet beállítása

```bash
# Virtuális környezet létrehozása
python3 -m venv venv

# Virtuális környezet aktiválása
# macOS/Linux esetén:
source venv/bin/activate
# Windows esetén:
venv\Scripts\activate

# Függőségek telepítése
pip install -r requirements.txt
```

### Node.js/TypeScript környezet beállítása

```bash
# Telepítse a root szintű függőségeket (a dokumentációs eszközökhöz)
npm install

# Az egyes leckék TypeScript példáihoz navigáljon a konkrét leckéhez:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container beállítás (ajánlott)

A tárhely tartalmaz `.devcontainer` konfigurációt GitHub Codespaces vagy VS Code Dev Containers használatához:

1. Nyisd meg a tárhelyet GitHub Codespaces-ben vagy VS Code-ban a Dev Containers kiterjesztéssel
2. A Dev Container automatikusan:
   - Telepíti a Python függőségeket a `requirements.txt` alapján
   - Lefuttatja a létrehozás utáni scriptet (`.devcontainer/post-create.sh`)
   - Beállítja a Jupyter kernelt

## Fejlesztési munkafolyamat

### Környezeti változók

Minden API-hozzáférést igénylő lecke környezeti változókat használ, amelyek a `.env` fájlban vannak definiálva:

- `OPENAI_API_KEY` - OpenAI API kulcs
- `AZURE_OPENAI_API_KEY` - Azure OpenAI a Microsoft Foundry-ban (az Azure OpenAI szolgáltatás most a Microsoft Foundry része: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI végpont URL (Foundry erőforrás végpont)
- `AZURE_OPENAI_DEPLOYMENT` - Chat kiegészítés modell telepítés neve (kurzus alapértelmezés: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Beágyazások modell telepítés neve (kurzus alapértelmezés: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API verzió (alapértelmezett: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face modellekhez
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modellek végpont (többszolgáltatós modell katalógus)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Modellek API kulcs (helyettesíti a megszűnő `GITHUB_TOKEN`-t)
- `AZURE_INFERENCE_CHAT_MODEL` - Egy nem következtető modell (pl. `Llama-3.3-70B-Instruct`), amelyet a `temperature` példák használnak, mivel a következtetéses modellek nem támogatják a mintavétel vezérlőket

### Modell konvenciók (fontos)

- **Az alapértelmezett chat modell a `gpt-5-mini`** - egy aktuális, nem elavult **következtető** modell. 2026-tól a régebbi, hőmérséklet-állítható "mini" modellek (`gpt-4o-mini`, `gpt-4.1-mini`) *elavulnak*, ezért a tananyag a GPT-5 családra szabványosít.
- **A következtető modellek elutasítják a `temperature` és `top_p` paramétereket**, helyette `max_output_tokens`-t (Responses API) / `max_completion_tokens`-t (chat kiegészítések) használnak a `max_tokens` helyett. Ne adj hozzá `temperature`/`top_p`/`max_tokens` értéket azokhoz a mintákhoz, amelyek a `gpt-5-mini`-t hívják.
- **A `temperature` demonstrálásához** a példák egy **Llama** modellt használnak (`Llama-3.3-70B-Instruct`) a Microsoft Foundry Modellek végpontján keresztül (`AZURE_INFERENCE_CHAT_MODEL`). Kövesd a következtetéses modelleket prompt tervezéssel és következtetési vezérlésekkel, ne mintavétel szabályozókkal.
- **Finomhangolás (18. lecke)** megtartja a `gpt-4.1-mini`-t: a GPT-5 csak megerősítéses finomhangolást (RFT) támogat, nem a felügyelt finomhangolást (SFT), amely ott szerepel.
- A 20. (Mistral) és 21. (Meta) leckék megtartják a `temperature`/`max_tokens` használatot, mert Mistral/Llama modelleket céloznak, amelyek támogatják ezt.

### Python példák futtatása

```bash
# Navigáljon a tanfolyam könyvtárába
cd 06-text-generation-apps/python

# Futtasson egy Python szkriptet
python aoai-app.py
```

### TypeScript példák futtatása

```bash
# Navigáljon a TypeScript alkalmazás könyvtárába
cd 06-text-generation-apps/typescript/recipe-app

# Fordítsa le a TypeScript kódot
npm run build

# Futtassa az alkalmazást
npm start
```

### Jupyter jegyzetfüzetek futtatása

```bash
# Indítsa el a Jupytert a tároló gyökérkönyvtárában
jupyter notebook

# Vagy használja a VS Code-ot Jupyter kiterjesztéssel
```

### Különféle lecketípusok kezelése

- **"Learn" leckék**: A README.md dokumentációra és fogalmakra fókuszálnak
- **"Build" leckék**: Működő kód példákat tartalmaznak Pythonban és TypeScriptben
- Minden leckének van egy README.md-je elmélettel, kódmagyarázatokkal és videós tartalom linkekkel

## Kódstílus irányelvek

### Python

- Használd a `python-dotenv`-t a környezeti változók kezelésére
- Importáld az `openai` könyvtárat az API-hívásokhoz
- Használd a `pylint`-et a linteléshez (néhány példában szerepel `# pylint: disable=all` az egyszerűség kedvéért)
- Kövesd a PEP 8 elnevezési szabványokat
- Az API-kulcsokat tárold `.env` fájlban, soha ne a kódban

### TypeScript

- Használd a `dotenv` csomagot a környezeti változókhoz
- TypeScript konfiguráció alkalmazásonként a `tsconfig.json` fájlban
- Használd az `openai` csomagot az Azure OpenAI-hoz (irányítsd a klienst a `/openai/v1/` végpontra és hívd a `client.responses.create` metódust); használd a `@azure-rest/ai-inference`-t a Microsoft Foundry Modellekhez
- Fejlesztéshez használd a `nodemon`-t automatikus újratöltéssel
- Futtatás előtt építsd meg: `npm run build`, majd `npm start`

### Általános konvenciók

- Tartsd a kód példákat egyszerűnek és oktatónak
- Kommentáld a kulcsfontosságú fogalmakat
- Minden lecke kódja önálló és futtatható legyen
- Használj következetes elnevezést: `aoai-` az Azure OpenAI-hoz, `oai-` az OpenAI API-hoz, `githubmodels-` a Microsoft Foundry Modellekhez (a GitHub Modellek korszakából származó régi előtag megtartva)

## Dokumentációs irányelvek

### Markdown stílus

- Minden URL legyen `[text](../../url)` formátumban, szóközök nélkül
- A relatív linkek `./` vagy `../`-val kezdődjenek
- Minden Microsoft domainhez tartozó link tartalmazza a követési azonosítót: `?WT.mc_id=academic-105485-koreyst`
- Ne használj ország-specifikus helyi beállítást az URL-ekben (kerüld az `/en-us/`-t)
- Képeket a `./images` mappában tárolj leíró nevekkel
- Használj angol karaktereket, számokat és kötőjeleket a fájlnevekben

### Fordítás támogatás

- A tárhely 40+ nyelvet támogat automatizált GitHub Actions segítségével
- A fordítások a `translations/` könyvtárban vannak tárolva
- Ne nyújts részleges fordításokat
- Gépi fordításokat ne fogadunk el
- A lefordított képek a `translated_images/` könyvtárban találhatók

## Tesztelés és validáció

### Beküldés előtti ellenőrzések

Ez a tárhely GitHub Actions-t használ validációra. PR beküldés előtt:

1. **Markdown linkek ellenőrzése**:
   ```bash
   # A validate-markdown.yml munkafolyamat ellenőrzi:
   # - Sérült relatív elérési útvonalak
   # - Hiányzó nyomonkövetési azonosítók az elérési útvonalakon
   # - Hiányzó nyomonkövetési azonosítók URL-eken
   # - Ország szerinti lokalizációval rendelkező URL-ek
   # - Sérült külső URL-ek
   ```

2. **Kézi tesztelés**:
   - Teszteld a Python példákat: Aktiváld a venv-t és futtasd a szkripteket
   - Teszteld a TypeScript példákat: `npm install`, `npm run build`, `npm start`
   - Ellenőrizd a környezeti változók megfelelő beállítását
   - Győződj meg róla, hogy az API kulcsok működnek a kód példákban

3. **Kód példák**:
   - Biztosítsd, hogy minden kód hibamentesen fusson
   - Teszteld mind Azure OpenAI-val, mind OpenAI API-val, ahol alkalmazható
   - Ellenőrizd a példák kompatibilitását a Microsoft Foundry Modellekkel, ahol támogatott

### Nincs automatizált teszt

Ez egy oktató jellegű tárhely, amely oktatóanyagokra és példákra fókuszál. Nincsenek egység- vagy integrációs tesztek. Az ellenőrzés elsősorban:
- a kód példák kézi tesztelése
- GitHub Actions a Markdown validációhoz
- a közösségi véleményezés az oktatóanyag minőségéhez

## Pull Request irányelvek

### Beküldés előtt

1. Teszteld a kódváltozásokat Pythonban és TypeScriptben, ahol alkalmazható
2. Futtasd a Markdown validációt (PR beküldésekor automatikusan elindul)
3. Ellenőrizd, hogy minden Microsoft URL tartalmazza a követési azonosítót
4. Győződj meg a relatív linkek helyességéről
5. Ellenőrizd, hogy a képek helyesen vannak-e hivatkozva

### PR cím formátuma

- Használj leíró címeket: `[Lesson 06] Javítás Python példa elírás` vagy `README frissítése a 08. leckéhez`
- Hivatkozz hibaszámokra, ha van: `Fixes #123`

### PR leírása

- Írd le, mi változott és miért
- Linkelj kapcsolódó problémákra
- Kódváltozás esetén részletezd, mely példák lettek tesztelve
- Fordítási PR esetén tartalmazd az összes fájlt a teljes fordításhoz

### Hozzájárulási követelmények

- Írd alá a Microsoft CLA-t (automatikus az első PR-nál)
- Forkold a tárhelyet a saját fiókodba, mielőtt változtatnál
- Egy PR egy logikai változtatás legyen (ne kombinalj nem összefüggő javításokat)
- Tartsd a PR-eket fókuszáltan és kicsin, ha lehetséges

## Gyakori munkafolyamatok

### Új kód példa hozzáadása

1. Navigálj a megfelelő lecke könyvtárba
2. Hozd létre a példát a `python/` vagy `typescript/` alkönyvtárban
3. Kövesd az elnevezési szabványt: `{provider}-{example-name}.{py|ts|js}`
4. Teszteld valódi API hitelesítő adatokkal
5. Dokumentáld az új környezeti változókat a lecke README-jében

### Dokumentáció frissítése

1. Szerkeszd a lecke könyvtárában a README.md fájlt
2. Kövesd a Markdown irányelveket (követési azonosítók, relatív linkek)
3. A fordítások frissítése GitHub Actions által történik (ne szerkeszd kézzel)
4. Teszteld az összes linket, hogy érvényesek-e

### Dev Containerekkel való munka

1. A tárhely tartalmazza a `.devcontainer/devcontainer.json` fájlt
2. A létrehozás utáni script automatikusan telepíti a Python függőségeket
3. A Python és Jupyter kiterjesztések előre konfiguráltak
4. A környezet a `mcr.microsoft.com/devcontainers/universal:2.11.2` alapú

## Telepítés és publikálás

Ez egy tanulási tárhely - nincs telepítési folyamat. A tananyagot az alábbi módokon használják:

1. **GitHub tárhely**: közvetlen hozzáférés a kódhoz és dokumentációhoz
2. **GitHub Codespaces**: azonnali fejlesztői környezet előre konfigurált setup-pal
3. **Microsoft Learn**: a tartalom hivatalos tanulási platformon is elérhető lehet
4. **docsify**: Markdown alapú dokumentációs oldal (lásd `docsifytopdf.js` és `package.json`)

### Dokumentációs oldal építése

```bash
# PDF generálása a dokumentációból (ha szükséges)
npm run convert
```

## Hibakeresés

### Gyakori problémák

**Python import hibák**:
- Győződj meg, hogy a virtuális környezet aktivált
- Fuss le `pip install -r requirements.txt` parancsot
- Ellenőrizd, hogy a Python verzió 3.9 vagy újabb

**TypeScript build hibák**:
- Fuss `npm install` az adott alkalmazás könyvtárában
- Ellenőrizd, hogy a Node.js verzió kompatibilis
- Töröld a `node_modules` könyvtárat és telepítsd újra, ha szükséges

**API hitelesítési hibák**:
- Ellenőrizd, hogy létezik a `.env` fájl és helyes értékeket tartalmaz
- Győződj meg, hogy az API kulcsok érvényesek és nem jártak le
- Ellenőrizd, hogy a végpont URL-ek régiódnak megfelelőek

**Hiányzó környezeti változók**:
- Másold a `.env.copy`-t `.env`-re
- Töltsd ki az adott lecke összes szükséges értékét
- Indítsd újra az alkalmazást a `.env` frissítése után

## További források

- [Kurzus beállítási útmutató](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Hozzájárulási irányelvek](./CONTRIBUTING.md)
- [Magatartási kódex](./CODE_OF_CONDUCT.md)
- [Biztonsági irányelvek](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Haladó kód minták gyűjteménye](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektre vonatkozó megjegyzések

- Ez egy **oktató tárhely**, a tanulásra fókuszál, nem termelési kódra
- A példák szándékosan egyszerűek és a fogalmak oktatására koncentrálnak
- A kódminőség kiegyensúlyozott az oktatási tisztasággal
- Minden lecke önálló és önállóan elvégezhető
- A tárhely több API szolgáltatót támogat: Azure OpenAI, OpenAI, Microsoft Foundry Modellek és offline szolgáltatók, mint a Foundry Local és Ollama
- A tartalom többnyelvű, automatizált fordítási munkafolyamatokkal
- Aktív közösség Discord-on kérdésekre és támogatásra

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->