# LLM-szolgáltató kiválasztása és konfigurálása 🔑

A feladatok **akár** beállíthatók úgy is, hogy egy vagy több nagy nyelvi modell (LLM) telepítés ellen dolgozzanak egy támogatott szolgáltató, például az OpenAI, Azure vagy Hugging Face által. Ezek egy _tárhelyes végpontot_ (API-t) biztosítanak, amelyhez programozottan hozzáférhetünk a megfelelő hitelesítő adatokkal (API-kulcs vagy token). Ebben a tanfolyamban ezeket a szolgáltatókat tárgyaljuk:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) sokféle modelljeivel, beleértve a GPT alapvető sorozatot.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) az OpenAI modellek vállalati felkészültséggel
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) egyetlen végponttal és API-kulccsal, amely több száz modellt ér el az OpenAI, Meta, Mistral, Cohere, Microsoft és más szolgáltatóktól (helyettesíti a GitHub Models-t, amely 2026 júliusának végén megszűnik)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) nyílt forráskódú modellek és inferencia szerverek esetén
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) vagy [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), ha inkább helyben, teljesen offline futtatnád a modelleket a saját eszközödön, felhő előfizetés nélkül

**Ezekhez a gyakorlatokhoz a saját fiókjaidat kell használnod**. A feladatok opcionálisak, így eldöntheted, hogy egyet, mindegyiket - vagy egyiket sem - állítasz be az érdeklődésed szerint. Néhány útmutató a regisztrációhoz:

| Regisztráció | Költség | API kulcs | Gyakorló környezet | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekt alapú](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kód nélküli, webes](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Több modell áll rendelkezésre |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK gyorsstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio gyorsstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Előzetes engedély szükséges a hozzáféréshez](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Árazás](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projekt áttekintő oldal](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry gyakorló környezet](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Elérhető ingyenes szint; egy végpont + kulcs számos modellel szemben |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [A Hugging Chat korlátozott modelleket tartalmaz](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Ingyenes (a saját eszközödön fut) | Nem szükséges | [Helyi CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Teljesen offline, OpenAI-kompatibilis végpont |
| | | | | |

Kövesd az alábbi utasításokat az adattár beállításához különböző szolgáltatók használatához. Az adott szolgáltatót igénylő feladatok fájlnevében az alábbi címkék egyikét fogod találni:

- `aoai` - Azure OpenAI végpont és kulcs szükséges
- `oai` - OpenAI végpont és kulcs szükséges
- `hf` - Hugging Face token szükséges
- `githubmodels` - Microsoft Foundry Models végpont és kulcs szükséges (a GitHub Models 2026 júliusának végén megszűnik)

Beállíthatsz egyet, egyiket sem vagy mindet. A kapcsolódó feladatok hitelesítő adatok hiányában hibát fognak jelezni.

## `.env` fájl létrehozása

Feltételezzük, hogy már elolvastad a fenti útmutatót, regisztráltál a megfelelő szolgáltatónál, és beszerezted a szükséges hitelesítő adatokat (API_KULCS vagy token). Azure OpenAI esetén feltételezzük továbbá, hogy rendelkezel egy érvényes Azure OpenAI szolgáltatás (végpont) telepítéssel, és legalább egy GPT modellt telepítettél csevegéses kiegészítéshez.

A következő lépés a **helyi környezeti változók** beállítása a következőképpen:

1. Keress a gyökérmappában egy `.env.copy` fájlt, melynek tartalma valahogy így néz ki:

   ```bash
   # OpenAI Szolgáltató
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI a Microsoft Foundry-ban
   ## (Az Azure OpenAI Szolgáltatás mostantól a Microsoft Foundry része: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Alapértelmezett beállítva! (aktuális stabil GA API verzió)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modellek (többszolgáltatós modell katalógus, helyettesíti a GitHub Modelleket, amelyek 2026 július végén nyugdíjba mennek)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Másold ezt a fájlt `.env` néven a következő parancs segítségével. Ez a fájl _gitignore-olva van_, így a titkok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltsd ki az értékeket (cseréld ki a jobb oldali helyőrzőket) a következő szakaszban leírtak szerint.

4. (Választható) Ha GitHub Codespaces-t használsz, beállíthatod a környezeti változókat _Codespaces titkokként_ ehhez a tárolóhoz kapcsolódóan. Ebben az esetben nem kell helyi .env fájlt létrehoznod. **Azonban vedd figyelembe, hogy ez az opció csak akkor működik, ha GitHub Codespaces-t használsz.** Docker Desktop esetén mindenképpen be kell állítanod a .env fájlt.

## `.env` fájl feltöltése

Nézzük gyorsan át a változóneveket, hogy megértsük, mit jelentenek:

| Változó  | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez a felhasználói hozzáférési token, amelyet a profilodban állítasz be |
| OPENAI_API_KEY | Ez a szolgáltatás használatához szükséges engedélyezési kulcs nem-Azure OpenAI végpontok esetén |
| AZURE_OPENAI_API_KEY | Ez a szolgáltatás használatához szükséges engedélyezési kulcs |
| AZURE_OPENAI_ENDPOINT | Az Azure OpenAI erőforrás telepített végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveggenerálás_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg-beágyazás_ modell telepítési végpontja |
| AZURE_INFERENCE_ENDPOINT | Ez a Microsoft Foundry projekthez tartozó végpont, a Microsoft Foundry Models használatához |
| AZURE_INFERENCE_CREDENTIAL | Ez a Microsoft Foundry projekthez tartozó API-kulcs |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó alapértelmezett modellekhez kapcsolódik: csevegés kiegészítéséhez (szöveggenerálás) és vektorkereséshez (beágyazások). Ezek beállítására vonatkozó utasításokat a releváns feladatokban találod majd.

## Azure OpenAI konfigurálása: Portálról

> **Megjegyzés:** Az Azure OpenAI szolgáltatás most a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) része. Az erőforrások és telepítések továbbra is megjelennek az Azure Portálon, de a napi modellkezelés (telepítések, gyakorlókörnyezet, monitorozás) már a Foundry portálon történik az önálló "Azure OpenAI Studio" helyett.

Az Azure OpenAI végpont és kulcs értékeit az [Azure Portálon](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) találod, kezdjük hát ott.

1. Menj az [Azure Portálra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kattints a **Kulcsok és végpont** opcióra az oldalsávban (bal oldali menü).
1. Kattints a **Kulcsok megjelenítése** gombra - ilyenkor a következőt kell látnod: KULCS 1, KULCS 2 és Végpont.
1. Használd a KULCS 1 értékét az AZURE_OPENAI_API_KEY-hez
1. Használd a Végpont értékét az AZURE_OPENAI_ENDPOINT-hez

Ezután szükségünk van a telepített modellek végpontjaira.

1. Kattints a **Modell telepítések** opcióra az oldalsávban (bal menü) az Azure OpenAI erőforrásnál.
1. A céloldalon kattints a **Microsoft Foundry portálhoz** gombra (vagy **Telepítések kezelése**, az erőforrás típusától függően)

Ez elvisz a Microsoft Foundry portálra, ahol az alábbiak szerint megtaláljuk a további értékeket.

## Azure OpenAI konfigurálása: Microsoft Foundry portálról

1. Navigálj a [Microsoft Foundry portálra](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **az erőforrásodból**, ahogy fentebb leírtuk.
1. Kattints a **Telepítések** fülre (oldalsáv, balra), hogy lásd az aktuálisan telepített modelleket.
1. Ha a kívánt modell nincs telepítve, használd a **Modell telepítése** funkciót a [modell katalógusból](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Szükséged lesz egy _szöveggenerálás_ modellre - ajánlott például: **gpt-4o-mini**
1. Szükséged lesz egy _szöveg-beágyazás_ modellre - ajánlott például a **text-embedding-3-small**

Ezután frissítsd a környezeti változókat a használt _telepítés neve_ szerint. Ez általában megegyezik a modell nevével, kivéve, ha kifejezetten megváltoztattad. Például lehet:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ne felejtsd el elmenteni a .env fájlt a végén**. Most kiléphetsz a fájlból, és folytathatod a jegyzet futtatására vonatkozó utasításokat.

## OpenAI konfigurálása: Profilból

Az OpenAI API kulcsodat megtalálod az [OpenAI fiókodban](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ha nincs még, regisztrálj egy fiókot, és hozz létre egy API kulcsot. Miután megvagy a kulccsal, ezt használhatod a `OPENAI_API_KEY` változó kitöltésére a `.env` fájlban.

## Hugging Face konfigurálása: Profilból

A Hugging Face tokened megtalálod a profilodban az [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alatt. Ezeket ne posztold vagy oszd meg nyilvánosan. Ehelyett hozz létre egy új tokent ehhez a projekthez, és másold be a `.env` fájl `HUGGING_FACE_API_KEY` változójába. _Megjegyzés:_ Technikai értelemben ez nem API-kulcs, de hitelesítésre használatos, ezért a következetesség kedvéért ezt a névhasználatot tartjuk meg.

## Microsoft Foundry Models konfigurálása: Portálról

> **Megjegyzés:** A GitHub Models 2026 júliusának végén megszűnik. A Microsoft Foundry Models az közvetlen helyettesítő, ugyanazzal az ingyenes kipróbálási model katalógussal és Azure AI Inferencia SDK / OpenAI SDK élménnyel.

1. Menj a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) oldalra, és hozz létre (vagy nyiss meg) egy Foundry projektet.
1. Böngészd a [modell katalógust](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), és telepíts egy modellt, pl. `gpt-4o-mini`.
1. A projekt **Áttekintő** oldalán másold ki a **végpontot** és az **API kulcsot**.
1. Használd a végpont értékét az `AZURE_INFERENCE_ENDPOINT` és a kulcs értékét az `AZURE_INFERENCE_CREDENTIAL` változóhoz a `.env` fájlban.

## Offline / Helyi szolgáltatók

Ha egyáltalán nem szeretnél felhő előfizetést használni, akkor futtathatsz kompatibilis nyílt modelleket közvetlenül a saját eszközödön:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft eszközön futó környezet. Automatikusan kiválasztja a legjobb végrehajtó szolgáltatót (NPU, GPU vagy CPU), és OpenAI-kompatibilis végpontot biztosít, így e kurzus legtöbb példa kódját minimális módosítással felhasználhatod. A kezdéshez lásd a [Foundry Local dokumentációt](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), vagy telepítsd a `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) parancsokkal.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - népszerű alternatíva a Llama, Phi, Mistral és Gemma helyi futtatására nyílt modellekkel.


Lásd a [19. lecke: Építés SLM-ekkel](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) részt a kézzelfogható példákért mindkét opció használatával.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->