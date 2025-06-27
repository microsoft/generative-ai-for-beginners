<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:27:01+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hu"
}
-->
# Állítsd be a fejlesztői környezeted

Ezt a tárolót és kurzust egy [fejlesztői konténerrel](https://containers.dev?WT.mc_id=academic-105485-koreyst) állítottuk be, amely egy univerzális futtatókörnyezetet tartalmaz, és támogatja a Python3, .NET, Node.js és Java fejlesztést. A kapcsolódó konfiguráció az `devcontainer.json` fájlban van definiálva, amely az `.devcontainer/` mappában található a tároló gyökerében.

A fejlesztői konténer aktiválásához indítsd el a [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (felhőalapú futtatókörnyezethez) vagy a [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (helyi eszközön futtatott környezethez) segítségével. Olvasd el [ezt a dokumentációt](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst), hogy részletesebben megismerd, hogyan működnek a fejlesztői konténerek a VS Code-ban.

> [!TIP]  
> Javasoljuk a GitHub Codespaces használatát a gyors kezdéshez minimális erőfeszítéssel. Ez egy bőséges [ingyenes használati kvótát](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) biztosít személyes fiókok számára. Állítsd be a [leállási időket](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), hogy maximalizáld a kvótád használatát az inaktív codespaces leállításával vagy törlésével.

## 1. Feladatok végrehajtása

Minden leckéhez tartoznak _opcionális_ feladatok, amelyeket egy vagy több programozási nyelven is meg lehet oldani, például: Python, .NET/C#, Java és JavaScript/TypeScript. Ez a szakasz általános útmutatást nyújt a feladatok végrehajtásával kapcsolatban.

### 1.1 Python feladatok

A Python feladatok alkalmazások (`.py` fájlok) vagy Jupyter notebookok (`.ipynb` fájlok) formájában vannak megadva.
- A notebook futtatásához nyisd meg a Visual Studio Code-ban, majd kattints a _Select Kernel_ (jobb felső sarokban) gombra, és válaszd ki az alapértelmezett Python 3 opciót. Most már használhatod a _Run All_ funkciót a notebook futtatásához.
- Python alkalmazások parancssorból történő futtatásához kövesd a feladatspecifikus utasításokat, hogy a megfelelő fájlokat válaszd ki, és megadd a szükséges argumentumokat.

## 2. Szolgáltatók konfigurálása

A feladatok **esetlegesen** úgy is beállíthatók, hogy egy vagy több Nagy Nyelvi Modell (LLM) telepítése ellen dolgozzanak egy támogatott szolgáltatón keresztül, mint például az OpenAI, Azure vagy Hugging Face. Ezek egy _hostolt végpontot_ (API) biztosítanak, amelyet programozottan elérhetünk a megfelelő hitelesítő adatokkal (API kulcs vagy token). Ebben a kurzusban ezeket a szolgáltatókat tárgyaljuk:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) különféle modellekkel, beleértve a GPT sorozatot.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) az OpenAI modellekhez, vállalati készenlétre fókuszálva
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) nyílt forráskódú modellekhez és előrejelzési szerverhez

**Ezekhez a gyakorlatokhoz saját fiókokra lesz szükséged**. A feladatok opcionálisak, így dönthetsz úgy, hogy egyet, mindet vagy egyet sem állítasz be a szolgáltatók közül az érdeklődésed alapján. Néhány útmutató a regisztrációhoz:

| Regisztráció | Költség | API kulcs | Játszótér | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekt alapú](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kódmentes, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Több modell elérhető |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Gyorsindítás](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Stúdió Gyorsindítás](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Előzetes jelentkezés szükséges a hozzáféréshez](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [A Hugging Chat korlátozott modellekkel rendelkezik](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Kövesd az alábbi utasításokat, hogy _konfiguráld_ ezt a tárolót különböző szolgáltatók használatához. Azok a feladatok, amelyek egy adott szolgáltatót igényelnek, az alábbi címkéket tartalmazzák a fájlneveikben:
- `aoai` - Azure OpenAI végpontot, kulcsot igényel
- `oai` - OpenAI végpontot, kulcsot igényel
- `hf` - Hugging Face tokent igényel

Konfigurálhatsz egyet, egyet sem, vagy mindegyiket. A kapcsolódó feladatok egyszerűen hibát jeleznek a hiányzó hitelesítő adatok miatt.

### 2.1. Hozz létre `.env` fájlt

Feltételezzük, hogy már elolvastad a fenti útmutatót, és regisztráltál a megfelelő szolgáltatónál, valamint megszerezted a szükséges hitelesítő adatokat (API_KEY vagy token). Az Azure OpenAI esetében feltételezzük, hogy van egy érvényes Azure OpenAI Szolgáltatás telepítésed (végpont) legalább egy GPT modellel a chat befejezéséhez.

A következő lépés a **helyi környezeti változók** konfigurálása az alábbiak szerint:

1. Keresd meg a gyökérmappában az `.env.copy` fájlt, amelynek a következő tartalommal kell rendelkeznie:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Másold át ezt a fájlt `.env` néven az alábbi parancs segítségével. Ez a fájl _gitignore-d_, így a titkok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltsd ki az értékeket (cseréld ki a helyettesítőket az `=` jobb oldalán), ahogy a következő szakaszban le van írva.

3. (Opció) Ha GitHub Codespaces-t használsz, lehetőséged van környezeti változókat _Codespaces titkokként_ menteni ehhez a tárolóhoz társítva. Ebben az esetben nem kell helyi .env fájlt beállítanod. **Azonban vedd figyelembe, hogy ez az opció csak akkor működik, ha a GitHub Codespaces-t használod.** Továbbra is be kell állítanod a .env fájlt, ha a Docker Desktopot használod.

### 2.2. Töltsd ki az `.env` fájlt

Nézzük meg gyorsan a változóneveket, hogy megértsük, mit képviselnek:

| Változó  | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez a felhasználói hozzáférési token, amelyet a profilodban állítottál be |
| OPENAI_API_KEY | Ez a szolgáltatás használatának engedélyezési kulcsa nem-Azure OpenAI végpontokhoz |
| AZURE_OPENAI_API_KEY | Ez a szolgáltatás használatának engedélyezési kulcsa |
| AZURE_OPENAI_ENDPOINT | Ez egy Azure OpenAI erőforrás telepített végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveg generálás_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg beágyazások_ modell telepítési végpontja |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó egy alapértelmezett modellt tükröz a chat befejezéséhez (szöveg generálás) és vektorkereséshez (beágyazások). Az ezek beállítására vonatkozó utasítások a releváns feladatokban lesznek meghatározva.

### 2.3 Azure konfigurálása: A portálról

Az Azure OpenAI végpont és kulcs értékek a [Azure Portálon](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) találhatók, így kezdjük ott.

1. Menj a [Azure Portálra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kattints a **Kulcsok és Végpont** opcióra az oldalsávban (bal oldali menü).
1. Kattints a **Kulcsok megjelenítése** gombra - a következőt kell látnod: KULCS 1, KULCS 2 és Végpont.
1. Használd a KULCS 1 értéket az AZURE_OPENAI_API_KEY-hez
1. Használd a Végpont értéket az AZURE_OPENAI_ENDPOINT-hoz

Ezután szükségünk van a konkrét modellek telepítési végpontjaira.

1. Kattints a **Modellek telepítése** opcióra az Azure OpenAI erőforrás oldalsávjában (bal menü).
1. Az adott oldalon kattints a **Telepítések kezelése** gombra

Ez elvisz az Azure OpenAI Studio weboldalra, ahol megtaláljuk a többi értéket, ahogy az alábbiakban le van írva.

### 2.4 Azure konfigurálása: A Stúdióból

1. Navigálj az [Azure OpenAI Stúdióba](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **az erőforrásodból** a fent leírtak szerint.
1. Kattints a **Telepítések** fülre (oldalsáv, bal) az aktuálisan telepített modellek megtekintéséhez.
1. Ha a kívánt modell nincs telepítve, használd a **Új telepítés létrehozása** lehetőséget a telepítéséhez.
1. Szükséged lesz egy _szöveg-generálás_ modellre - javasoljuk: **gpt-35-turbo**
1. Szükséged lesz egy _szöveg-beágyazás_ modellre - javasoljuk: **text-embedding-ada-002**

Most frissítsd a környezeti változókat, hogy tükrözzék a használt _Telepítési nevet_. Ez általában megegyezik a modell nevével, hacsak nem változtattad meg kifejezetten. Tehát például lehet, hogy:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne felejtsd el menteni a .env fájlt, amikor kész**. Most kiléphetsz a fájlból, és visszatérhetsz a notebook futtatására vonatkozó utasításokhoz.

### 2.5 OpenAI konfigurálása: A Profilból

Az OpenAI API kulcsod megtalálható az [OpenAI fiókodban](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ha nincs, regisztrálhatsz egy fiókot és létrehozhatsz egy API kulcsot. Miután megvan a kulcs, használhatod az `OPENAI_API_KEY` változó kitöltésére az `.env` fájlban.

### 2.6 Hugging Face konfigurálása: A Profilból

A Hugging Face tokened megtalálható a profilodban a [Hozzáférési tokenek](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alatt. Ne oszd meg vagy tedd közzé ezeket nyilvánosan. Ehelyett hozz létre egy új tokent ennek a projektnek a használatához, és másold be az `.env` fájlba a `HUGGING_FACE_API_KEY` változó alá. _Megjegyzés:_ Technikai értelemben ez nem egy API kulcs, de hitelesítéshez használjuk, ezért megtartjuk ezt az elnevezési konvenciót a következetesség érdekében.

**Jogi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás használatával készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.