# Változásnapló

A Generatív AI kezdőknek tananyag minden jelentős változása ebben a fájlban van dokumentálva.

A formátum a [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) alapján készült. Mivel ez egy
tanulási tananyag, nem pedig verziózott szoftvercsomag, a bejegyzések dátum szerint vannak csoportosítva.

## [2026-07-16] — Tartalom ellenőrzése + 09. lecke képi elemei

### Megváltozott

- **10. lecke (alacsony kódú AI alkalmazások):** frissítve két nyugdíjazott `docs.microsoft.com/powerapps/...` Dataverse
  link a jelenlegi `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`-re
  (élőben ellenőrizve).
- **17. lecke (AI ügynökök):** korszerűsítve egy elavult modell példa (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) és egy helyőrző telepítési név az Agent Framework példában
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** hozzáadva a hiányzó `?WT.mc_id=academic-105485-koreyst` követési azonosító a
  *Microsoft for Startups* linkhez.
- **09. lecke képanyagok** újragenerálva a `gpt-image` modellel: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` és
  `images/startup.png` (a szerkesztési példa előtte/utána páros egy valódi
  `client.images.edit` hívással készült, generált maszkkal).

### Ellenőrizve

- Átvizsgáltuk az 01, 03, 05, 12, 14 és 16 leckék README-fájljait — mind aktuálisak (helyes Microsoft Foundry
  elnevezések és linkek); változtatás nem szükséges.
- Végigfuttattunk teljes markdown ellenőrzést az összes 41 repository-ban lévő markdown fájlon (a fordítások kivételével)
  lejárt dokumentációs útvonalak, `/en-us/` Microsoft lokalizációk, elavult termék/modell nevek, hiányzó követési
  azonosítók és törött relatív linkek/képek miatt. Csak az egyetlen *Microsoft for Startups* követési azonosító hiány volt
  javítható; minden más jelzés hamis pozitív volt (automatikusan generált fordítási linkek,
  kommentált helyőrzők és külső `/en/` struktúrájú URL-ek).

## [2026-07-15] — 09. lecke (Képalkalmazások) átírás GPT képi modellekhez

### Változtatások

- **Újraírtuk a 09. leckét "Kép generálási alkalmazások építése"** a jelenlegi **`gpt-image`**
  modell család köré (alapértelmezett **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` szintén GA), lecserélve
  a régi DALL·E 2/3 tartalmat. Főbb javítások:
  - `gpt-image` modellek az képet **base64 (`b64_json`)** formátumban adják vissza, nem URL-ként. Minden mintát frissítettünk, hogy
    `base64.b64decode(...)` helyett `url` letöltése `requests`-vel.
  - Emeltük a kép API verzióját `2025-04-01-preview`-ra.
  - Lecseréltük a kitalált "hőmérséklet" részt (a képmodellek nem fogadnak `temperature`-t), és a
    kizárólag DALL·E-2-höz tartozó kép **variációk** tartalmat egy **képszerkesztés** (maszk/festés) szekcióra.
  - Frissítettük `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, mindkét
    gyakorlat jegyzetfüzetet (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) és a .NET `.dib` jegyzetfüzetet.

### Eltávolítva

- Törölve az elavult `python/aoai-app-variation.py` és `python/oai-app-variation.py` példák
  (`images.create_variation` kizárólag DALL·E-2-höz van, és nincs támogatva `gpt-image` által).
- Törölve 4 elárvult képállomány, amely a törölt hőmérséklet-összehasonlító szakaszhoz kötődött
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Eltávolítva a szükségtelen `requests` függőség a lecke Python példáiból és követelményekből.

### Érvényesítve

- Lefuttatva `aoai-app.py` végig egy telepített `gpt-image-1.5` modellen, és megerősítve, hogy a base64
  dekódolás/mentés folyamat PNG-t eredményez. A jegyzetfüzetek érvényes JSON-nak bizonyultak.

## [2026-07-14] — Alapértelmezett modellfrissítés + érvelő modell útmutatás

### Változás

- **Alapértelmezett chatmodell `gpt-4o-mini` → `gpt-5-mini`** minden futtatható mintán, dokumentáción és konfiguráción keresztül a tananyagban.
  Ezt a modell életciklus státusza vezérelte: a Microsoft Foundry-n a
  `gpt-4o-mini` (2026-10-01-től kivezetendő) és az egész `gpt-4.1` család (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, 2026-10-14-től kivezetendő) **kivezetés alatt állnak**, míg a **GPT-5 család**
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) általánosan elérhető** (2027-02-06-ig lesz támogatott).
  Frissítve:
  - `.env.copy`, `00-course-setup/03-providers.md` (ajánlott telepítés és `az cognitiveservices`
    telepítési parancsok), valamint a 04, 06, 07 és 15-ös leckék README fájljai.
  - Python példák a 06-os leckében (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) és a 08-as lecke szkriptjei.
  - TypeScript / JavaScript példák a 06, 07 és 11-es leckékben, valamint az `.dib` .NET jegyzetfüzetek a 06 és 07-es leckéhez.
  - Feladat jegyzetfüzetek a 04, 06, 07 és 11-es leckékben (kód cellák), plusz `shared/python/api_utils.py`
    docstring példák.
- **Érvelő modell paraméter útmutatás (új).** `gpt-5-mini` egy *érvelő* modell: nem támogatja az `temperature`/`top_p`,
  és használja az `max_completion_tokens` (chat kiegészítések) /
  `max_output_tokens` (Válasz API) helyett a `max_tokens`-t. Ennek megfelelően:
  - Eltávolítva `temperature`/`top_p`/`max_tokens` azokról a példákról, amelyek most alapértelmezetten `gpt-5-mini`-t használnak
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, a 15-ös lecke RAG README-je).
  - Hozzáadva egy **"A következtető modellek nem használják `temperature`"** megjegyzés a 06-os leckéhez, amely elmagyarázza, hogy
    a következtető modelleket **prompt mérnökséggel + következtető szabályozókkal** irányítják, nem pedig mintavételi gombokkal,
    míg `temperature`/`top_p` továbbra is érvényes nem következtető modelleken
    (GPT-4.x, Mistral, Llama, Phi, nyílt modellek).
- **`gpt-5-mini` nem használatos a finomhangolási oktatóanyagban (18. lecke).** A GPT-5 csak
  megerősítéses finomhangolást (RFT) támogat; a 18. lecke felügyelt finomhangolás (SFT) bemutatója megtartja
  `gpt-4.1-mini`, amely támogatja az SFT/DPO-t.
- **A hőmérséklet bemutatók Llama modellel készülnek.** Az oktatás `temperature` megtartása érdekében (amit a következtető modellek
  elutasítanak), egy `Llama-3.3-70B-Instruct` modellt használnak a Foundry Models végponton keresztül. Hozzáadva egy új
  `AZURE_INFERENCE_CHAT_MODEL` változó `.env.copy`-hoz; a 04/06-os leckék `githubmodels` notebookjai és
  a `06` `js-githubmodels` minta ezt olvassák be (visszaesve `Llama-3.3-70B-Instruct`-re), és megtartják a
  `temperature`/`top_p`/`max_tokens` bemutatóikat.
- **JS / .NET példák frissítve GPT-5-re.** Eltávolítva `temperature`/`top_p`/`max_tokens` a GPT-5
  példákból (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ami
  szintén okoz `MaxOutputTokenCount`-t, hogy a következtető kimenet ne legyen levágva). A `06` `js-githubmodels`
  minta most Llama modellt használ a hőmérséklet bemutató megtartásához. A `.dib` megjegyzi, hogy a `Azure.AI.Inference` + egy Llama modell
  az út a `Temperature` bemutatásához .NET-ben.
- Meghagyva `gpt-4o-mini` / `gpt-5-mini` ott, ahol pontosak maradnak: `tiktoken` token-kódolási
  hivatkozások, modellkatalógus elérhetőségi listák, és a 02-es lecke beszédmodellek (`gpt-4o-transcribe`).
- A 20-as (Mistral) és 21-es (Meta) leckék példái megtartják `temperature`/`max_tokens`, mert ezek
  Mistral/Llama modellekre céloznak, amelyek támogatják ezeket a paramétereket.

## [2026-07-06] — Tartalom modernizálási frissítés

Egy átfogó frissítés a tananyag pontosságának fenntartására 2026-ra: modern API-k, aktuális terméknév és
modellnevek, frissített szolgáltató irányelvek és új fejlesztői élmény eszközök.

### Hozzáadva

- **Microsoft Agent Framework** szekció a `17-ai-agents` leckében, amely lefedi az egyetlen chat ügynököket,
  eszközök/funkcióhívásokat, Azure OpenAI (Microsoft Foundry) konfigurációt és több ügynök
  munkafolyamat-összehangolást (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentálva offline / eszközön futó szolgáltatóként (az Ollama mellett) a
  `00-course-setup/03-providers.md`-ben és a `19-slm` leckében.
- **Folyamatos integrációs munkafolyamatok**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (a fenntartott `shared/`
    modulban érvényesítve, tanácsadó az egész tananyagban), egy tanácsadó ESLint futtatás, és egy pytest munka.
  - `.github/workflows/security.yml` — CodeQL elemzés (Python + JavaScript/TypeScript) és
    függőség áttekintés a pull requesteken.
- **Tesztcsomag** a `tests/` alatt — 41 pytest teszt a megosztott segédmodult lefedve.
- **Azure OpenAI → Responses API migrációs készség** a
  `.github/skills/azure-openai-to-responses/` alatt, amely az API migráció irányítására szolgál.

### Megváltozott

- **Chat Completions API → Responses API** az összes Python és TypeScript chat példában
  (`client.responses.create(...)` → `response.output_text`), beleértve a 04., 06., 07., 11.,
  15. és 18. leckéket, valamint azok README fájljait.
- **GitHub Models → Microsoft Foundry Models** a szövegben, hivatkozásokban és példákban egyaránt. A GitHub Models
  2026 júliusának végén megszűnik; a példák most a Microsoft Foundry modell katalógusára mutatnak, és használják
  az `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` környezeti változókat.
- **`.env.copy`, `AGENTS.md` és a szolgáltató dokumentációi** frissültek, hogy tükrözzék, hogy az Azure OpenAI most a Microsoft Foundry része,
  és az alapértelmezett API verzió `2024-10-21`-ra emelkedett.
- **TypeScript példák** (06, 07, 08, 11. leckék) átköltöztek a már nem támogatott `@azure/openai`
  béta SDK-ról az `openai` csomagra (a chat alkalmazások a Responses API-t használják; a kereső alkalmazás az
  embeddings klienset).
- **.NET notebookok** (`dotnet/*.dib`) egységesítették az `Azure.AI.OpenAI` **2.1.0** verzióját: 06 és 07. leckék
  használja az `ChatClient` API-t, a 08-as lecke a `EmbeddingClient`-t (`GenerateEmbedding` / `ToFloats`), és
  a 09-es lecke a `ImageClient`-t (`GenerateImage`) használja `gpt-image-1`-vel, lecserélve a hagyományos
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync`-t az `1.0.0-beta.9`-ból.
- **Terméknév modernizálás**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (14., 16., 17. lecke) és "Bing" → **Microsoft Copilot** (12. lecke), ahol ezek hivatkoztak a
  aktuális termékek.
- A **DevContainer** (`.devcontainer/`) most tartalmazza a Pylance, Black, Ruff, ESLint, Prettier és Copilot
  bővítményeket, engedélyezi a mentéskor történő formázást, és telepíti a `ruff`, `black`, `mypy` és `pytest` csomagokat, hogy a CI
  ellenőrzések helyileg reprodukálhatók legyenek.
- A **Kép generálás** (09. lecke) az `gpt-image-1` használatát javasolja Azure-hoz (az Azure katalógus eltávolította 
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** frissítve a befejezett munkák (API migráció, CI,
  DevContainer, tesztek) és a jelenlegi tények (a fordításokat automatikusan az
  Azure Co-op Translator készíti; az Assistants API-t a Responses API váltotta fel) tükrözésére.

### Javítva

- **`shared/python/input_validation.py`** — az `validate_text_input(allow_empty=True)` mostantól üres stringgel tér vissza
  fehér karaktereket tartalmazó bemenet esetén a "túl rövid" hiba helyett (összhangban az
  `None` esettel). Új tesztcsomag fedezte fel és lefedte.
- **09. leckéhez tartozó képminták** — valódi hibák javítva: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  valamint egy változó, ami árnyékolta a `openai` modult.
- **15. leckében lévő RAG jegyzetfüzet** — javítva a kliens beállítás, kicserélve az eltávolított `DataFrame.append`
  `pd.concat`-ra, és korszerűsítve a régi SDK használatát.
- Elavult / kivont modellnevek (`gpt-3.5-turbo`, `gpt-35-turbo`) helyettesítve `gpt-4o-mini`-vel
  aktív mintákban; a történelmi finomhangolási eredmények a 18. leckében megmaradtak és megjelölve
  lettek, nem átírva.

### Elavult / Megjegyzések

- **Microsoft Foundry Models minták**, amelyek az `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK-t (`client.complete()`) használják — a `githubmodels-*` és `js-githubmodels` minták és a 19., 20.
  és 21. lecke — a Model Inference API-n maradnak, amely **nem** támogatja a Responses API-t. Ezek
  szándékosan az adott SDK-n maradnak.
- `AzureOpenAI()` szándékosan meg van tartva, ahol még mindig releváns (beágyazások és képgenerálás),
  mivel ezek a munkafolyamatok nem részei a Responses API migrációnak.
- `text-embedding-ada-002` hivatkozások megmaradnak, ahol egy előre kiszámított beágyazás index függ tőlük.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->