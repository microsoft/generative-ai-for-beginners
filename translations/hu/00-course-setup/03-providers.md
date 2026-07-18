# LLM Szolgáltató kiválasztása és konfigurálása 🔑

A feladatokat **szintén** be lehet állítani úgy, hogy egy vagy több nagy nyelvi modell (LLM) telepítések ellen dolgozzanak támogatott szolgáltatókon keresztül, mint például az OpenAI, Azure vagy Hugging Face. Ezek biztosítanak egy _hosztolt végpontot_ (API), amelyhez a megfelelő hitelesítő adatokkal (API kulcs vagy token) programozottan hozzáférhetünk. Ebben a tanfolyamban ezeket a szolgáltatókat tárgyaljuk:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) különféle modellekkel, beleértve a GPT sorozat alapmodelljeit is.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst), amely az OpenAI modelleket vállalati felkészültséggel kínálja
 - [Microsoft Foundry modellek](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) egyetlen végponton és API kulccsal elérve több száz modellt az OpenAI, Meta, Mistral, Cohere, Microsoft és mások szolgáltatásából (helyettesíti a GitHub Modelleket, amely 2026 júliusának végén megszűnik)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) nyílt forráskódú modellekhez és lekérdező szerverhez
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) vagy [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), ha inkább teljesen offline, saját eszközön futtatnád a modelleket, felhő előfizetés nélkül

**Ezekhez a gyakorlatokhoz saját fiókokat kell használnod**. A feladatok opcionálisak, így választhatsz, hogy egyet, mindet vagy egyiket sem állítod be az érdeklődésed szerint. Néhány útmutató a regisztrációhoz:

| Regisztráció | Költség | API kulcs | Játszótér (Playground) | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektalapú](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kód nélküli, webes](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Többféle modell elérhető |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK kezdő lépések](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Stúdió kezdő lépések](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Előzetes engedélykérés kötelező](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Árazás](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projekt áttekintő oldal](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Játszótér](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Ingyenes szint elérhető; egy végpont + kulcs sok modell szolgáltatóhoz |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [A Hugging Chat korlátozott modellekkel rendelkezik](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Ingyenes (a te eszközödön fut) | Nem szükséges | [Helyi CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Teljesen offline, OpenAI-kompatibilis végpont |
| | | | | |

Kövesd az alábbi utasításokat a _repository_ konfigurálásához különböző szolgáltatók használatához. Az adott szolgáltatót igénylő feladatokban a fájlnév tartalmazni fogja az alábbi címkék egyikét:

- `aoai` - Azure OpenAI végpontot és kulcsot igényel
- `oai` - OpenAI végpontot és kulcsot igényel
- `hf` - Hugging Face tokent igényel
- `githubmodels` - Microsoft Foundry modellek végpontot és kulcsot igényel (a GitHub Modellek 2026 júliusának végén megszűnnek)

Beállíthatsz egyet, egyiket sem vagy mindegyik szolgáltatót. A kapcsolódó feladatok hibát jeleznek hiányzó hitelesítő adatok esetén.

## `.env` fájl létrehozása

Feltételezzük, hogy elolvastad a fenti útmutatót, regisztráltál a megfelelő szolgáltatónál, és megszerezted a szükséges hitelesítési adatokat (API_KEY vagy token). Az Azure OpenAI esetén feltételezzük azt is, hogy van egy élő Azure OpenAI szolgáltatás (végpont) telepítésed legalább egy GPT modellel csevegéshez.

A következő lépés, hogy konfiguráld a **helyi környezeti változókat** a következő módon:

1. Nézd meg a gyökérkönyvtárban a `.env.copy` fájlt, amelynek tartalma hasonló lehet ehhez:

   ```bash
   # OpenAI Szolgáltató
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI a Microsoft Foundry-ban
   ## (Az Azure OpenAI Szolgáltatás mostantól a Microsoft Foundry része: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Alapértelmezett beállítva! (jelenlegi stabil GA API verzió)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modellek (többszolgáltatós modell katalógus, helyettesíti a GitHub Modelleket, amelyek 2026 júliusának végén megszűnnek)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Másold át ezt a fájlt `.env` néven az alábbi parancs segítségével. Ez a fájl _gitignore-ban_ van, így a titkok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltsd ki az értékeket (cseréld ki a jobb oldali helyőrzőket az `=` után) az alábbi részben leírtak szerint.

4. (Opcionális) Ha GitHub Codespaces-t használsz, elmentheted a környezeti változókat is _Codespaces titkoként_, amelyek ebben a repóban lesznek elérhetők. Ebben az esetben nem kell helyileg létrehozni `.env` fájlt. **Fontos: Ez az opció csak akkor működik, ha GitHub Codespaces-t használsz.** Docker Desktop esetén továbbra is szükséges a `.env` fájl beállítása.

## `.env` fájl kitöltése

Vegyük gyorsan át a változóneveket, hogy értsük, mit jelentenek:

| Változó | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez a felhasználói hozzáférési token, amit a profilodban állítottál be |
| OPENAI_API_KEY | Ez az engedélyező kulcs az Azure-on kívüli OpenAI végpontok használatához |
| AZURE_OPENAI_API_KEY | Ez az engedélyező kulcs az Azure OpenAI szolgáltatáshoz |
| AZURE_OPENAI_ENDPOINT | Ez az Azure OpenAI erőforrás végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveg generálás_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg beágyazás_ modell telepítési végpontja |
| AZURE_INFERENCE_ENDPOINT | Ez a végpont a Microsoft Foundry projekthez, melyet a Microsoft Foundry modellekhez használnak |
| AZURE_INFERENCE_CREDENTIAL | Ez az API kulcs a Microsoft Foundry projekthez |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó egy alapértelmezett modellt tükröz a csevegéshez (szöveg generálás) és vektoros kereséshez (beágyazások). Az ezek beállítására vonatkozó utasítások a kapcsolódó feladatokban lesznek megadva.

## Azure OpenAI konfigurálása: Portálról

> **Megjegyzés:** Az Azure OpenAI szolgáltatás immár a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) része. Az erőforrások és telepítések továbbra is megjelennek az Azure Portalban, de a napi modellkezelés (telepítések, játszótér, monitorozás) a Foundry portálon történik, a régi önálló "Azure OpenAI Stúdió" helyett.

Az Azure OpenAI végpont és kulcs adatokat az [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) oldalon találod, kezdjük ott.

1. Lépj be az [Azure Portalra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kattints a **Kulcsok és végpont** opcióra az oldalsávon (bal menü).
1. Kattints a **Kulcsok megjelenítése** gombra – a következőket kell látnod: KEY 1, KEY 2 és Végpont.
1. Használd a KEY 1 értéket az `AZURE_OPENAI_API_KEY`-hez
1. Használd a Végpont értéket az `AZURE_OPENAI_ENDPOINT`-hez

Most szükségünk van a telepített modellek specifikus végpontjaira.

1. Kattints a **Model telepítések** lehetőségre az oldalsávon (bal menü) az Azure OpenAI erőforrásnál.
1. A megjelenő oldalon kattints a **Microsoft Foundry portálra** való továbblépéshez (vagy **Telepítések kezelése** az erőforrás típusától függően)

Ez elvisz a Microsoft Foundry portálra, ahol az alábbi módon megszerezzük a további értékeket.

## Azure OpenAI konfigurálása: Microsoft Foundry portálról

1. Navigálj a [Microsoft Foundry portálra](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **az erőforrásodból** a fentiek szerint.
1. Kattints a **Telepítések** fülre (oldalsáv, bal oldalon) az aktuálisan telepített modellek megtekintéséhez.
1. Ha a kívánt modell nincs telepítve, használd a **Modell telepítése** funkciót a [modell katalógusból](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Szükséged lesz egy _szöveg generáló_ modellre – ajánlott: **gpt-5-mini**
1. Szükséged lesz egy _szöveg beágyazó_ modellre – ajánlott: **text-embedding-3-small**

Most frissítsd a környezeti változókat az _Telepítési név_-nek megfelelően, amit használsz. Ez általában megegyezik a modell nevével, hacsak nem változtattad meg kifejezetten. Például:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ne felejtsd el elmenteni a `.env` fájlt a módosítások után**. Most kiléphetsz a fájlból és folytathatod a jegyzet futtatási utasításaival.

## OpenAI konfigurálása: Profilból

Az OpenAI API kulcsodat megtalálod az [OpenAI fiókodban](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ha nincs még, regisztrálhatsz egy fiókot és létrehozhatsz API kulcsot. Miután megszerezted, használd a kulcsot a `.env` fájl `OPENAI_API_KEY` változójának kitöltéséhez.

## Hugging Face konfigurálása: Profilból

A Hugging Face tokened a profilodban az [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alatt található. Ne posztold vagy oszd meg nyilvánosan. Helyette hozz létre egy új tokent erre a projektre és másold be a `.env` fájl `HUGGING_FACE_API_KEY` változójába. _Megjegyzés:_ Ez technikailag nem API kulcs, de hitelesítésre használjuk, ezért követjük ezt az elnevezési konvenciót a konzisztencia érdekében.

## Microsoft Foundry modellek konfigurálása: Portálról

> **Megjegyzés:** A GitHub Modellek 2026 júliusának végén megszűnnek. A Microsoft Foundry modellek közvetlen helyettesítők, ugyanolyan ingyenesen kipróbálható modell katalógust és Azure AI Inference SDK / OpenAI SDK élményt kínálnak.

1. Menj a [Microsoft Foundry oldalra](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) és hozz létre (vagy nyiss meg) egy Foundry projektet.
1. Böngészd át a [modell katalógust](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) és telepíts egy modellt, például a `gpt-5-mini`-t.
1. A projekt **Áttekintő** oldalán másold ki a **végpont** és **API kulcs** értékeket.
1. Használd a végpont értéket az `AZURE_INFERENCE_ENDPOINT`, a kulcs értéket pedig az `AZURE_INFERENCE_CREDENTIAL` változókhoz a `.env` fájlban.

## Offline / helyi szolgáltatók

Ha egyáltalán nem szeretnél felhő előfizetést használni, kompatibilis nyílt modell futtatható közvetlenül a saját eszközödön:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – a Microsoft helyi futtatókörnyezete. Automatikusan kiválasztja a legjobb végrehajtási szolgáltatót (NPU, GPU vagy CPU), és egy OpenAI-kompatibilis végpontot biztosít, így a tanfolyam kódmintái minimális módosítással újrahasznosíthatók. Nézd meg a [Foundry Local dokumentációját](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) a kezdéshez, vagy telepítsd a `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) paranccsal.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – népszerű alternatíva nyílt modellek, például Llama, Phi, Mistral és Gemma helyi futtatásához.


Lásd a [19. lecke: Építés SLM-ekkel](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) a gyakorlatias példákért mindkét opció használatával.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->