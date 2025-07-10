<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:35:28+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hu"
}
-->
# Fejlesztői környezet beállítása

Ehhez a tárhelyhez és tanfolyamhoz egy [fejlesztői konténert](https://containers.dev?WT.mc_id=academic-105485-koreyst) állítottunk be, amely egy univerzális futtatókörnyezetet biztosít Python3, .NET, Node.js és Java fejlesztéshez. A kapcsolódó konfiguráció a `devcontainer.json` fájlban található, amely a `.devcontainer/` mappában van a tárhely gyökérkönyvtárában.

A fejlesztői konténer aktiválásához indítsd el [GitHub Codespaces-ben](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (felhőalapú futtatókörnyezethez) vagy [Docker Desktopban](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (helyi gépen futtatott környezethez). További részletekért olvasd el [ezt a dokumentációt](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) arról, hogyan működnek a fejlesztői konténerek a VS Code-ban.

> [!TIP]  
> Ajánljuk a GitHub Codespaces használatát a gyors és egyszerű kezdéshez. Személyes fiókok számára bőséges [ingyenes használati keretet](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) biztosít. Állítsd be a [timeoutokat](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), hogy az inaktív codespace-ek leálljanak vagy törlődjenek, így maximalizálhatod a kereted kihasználtságát.

## 1. Feladatok végrehajtása

Minden leckéhez tartozhatnak _opcionális_ feladatok, amelyeket egy vagy több programozási nyelven biztosítunk, például Python, .NET/C#, Java és JavaScript/TypeScript. Ez a rész általános útmutatást ad a feladatok végrehajtásához.

### 1.1 Python feladatok

A Python feladatok vagy alkalmazásként (`.py` fájlok), vagy Jupyter notebookként (`.ipynb` fájlok) érhetők el.  
- A notebook futtatásához nyisd meg Visual Studio Code-ban, majd kattints a _Select Kernel_-re (jobb felső sarokban), és válaszd ki az alapértelmezett Python 3 opciót. Ezután használhatod a _Run All_ parancsot a notebook futtatásához.  
- Parancssorból Python alkalmazások futtatásához kövesd az adott feladathoz tartozó utasításokat, hogy a megfelelő fájlokat válaszd ki és megadd a szükséges argumentumokat.

## 2. Szolgáltatók konfigurálása

A feladatok **lehetnek** úgy beállítva, hogy egy vagy több Nagy Nyelvi Modell (LLM) telepítésével működjenek egy támogatott szolgáltatón keresztül, mint például OpenAI, Azure vagy Hugging Face. Ezek egy _hosztolt végpontot_ (API-t) biztosítanak, amelyhez programozottan hozzáférhetünk a megfelelő hitelesítő adatokkal (API kulcs vagy token). Ebben a tanfolyamban az alábbi szolgáltatókat tárgyaljuk:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) különféle modellekkel, beleértve a GPT alapú sorozatot.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst), amely az OpenAI modelleket vállalati szintű felkészültséggel kínálja.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) nyílt forráskódú modellekhez és inferencia szerverhez.

**Ezekhez a gyakorlatokhoz saját fiókok használata szükséges.** A feladatok opcionálisak, így eldöntheted, hogy egy, mindegyik vagy egyik szolgáltatót sem állítod be az érdeklődésed szerint. Néhány útmutató a regisztrációhoz:

| Regisztráció | Költség | API kulcs | Playground | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Projekt alapú](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kód nélküli, webes](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Több modell elérhető |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK gyorsindító](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio gyorsindító](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Előzetes hozzáférési kérelem szükséges](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat korlátozott modellekkel rendelkezik](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Kövesd az alábbi utasításokat, hogy _konfiguráld_ ezt a tárhelyet a különböző szolgáltatók használatához. Azok a feladatok, amelyek egy adott szolgáltatót igényelnek, a fájlneveikben az alábbi címkék egyikét tartalmazzák:  
 - `aoai` - Azure OpenAI végpont és kulcs szükséges  
 - `oai` - OpenAI végpont és kulcs szükséges  
 - `hf` - Hugging Face token szükséges  

Beállíthatsz egyet, többet vagy egyiket sem. A kapcsolódó feladatok hibát jeleznek, ha hiányoznak a hitelesítő adatok.

###  2.1. `.env` fájl létrehozása

Feltételezzük, hogy már elolvastad a fentieket, regisztráltál a megfelelő szolgáltatónál, és megszerezted a szükséges hitelesítő adatokat (API_KEY vagy token). Azure OpenAI esetén feltételezzük, hogy rendelkezel egy érvényes Azure OpenAI Szolgáltatás telepítéssel (végponttal), amelyen legalább egy GPT modell fut chat befejezéshez.

A következő lépés a **helyi környezeti változók** beállítása az alábbiak szerint:

1. Nézd meg a gyökérkönyvtárban található `.env.copy` fájlt, amelynek tartalma valahogy így néz ki:

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

2. Másold le ezt a fájlt `.env` néven az alábbi parancs segítségével. Ez a fájl _gitignore-olva_ van, így a titkos adatok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltsd ki az értékeket (cseréld ki a jobb oldali helyőrzőket) a következő szakaszban leírtak szerint.

3. (Opcionális) Ha GitHub Codespaces-t használsz, lehetőséged van a környezeti változókat _Codespaces titkokként_ elmenteni, amelyek ehhez a tárhelyhez kapcsolódnak. Ebben az esetben nem kell helyi .env fájlt létrehoznod. **Fontos azonban, hogy ez az opció csak GitHub Codespaces használata esetén működik.** Docker Desktop használata esetén továbbra is szükséges a .env fájl beállítása.

### 2.2. `.env` fájl kitöltése

Nézzük meg gyorsan a változóneveket, hogy mit jelentenek:

| Változó  | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez a felhasználói hozzáférési token, amelyet a profilodban állítottál be |
| OPENAI_API_KEY | Ez az engedélyező kulcs a nem Azure OpenAI végpontok használatához |
| AZURE_OPENAI_API_KEY | Ez az engedélyező kulcs az Azure OpenAI szolgáltatáshoz |
| AZURE_OPENAI_ENDPOINT | Ez az Azure OpenAI erőforrás telepített végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveg generálás_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg beágyazás_ modell telepítési végpontja |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó egy alapértelmezett modellt tükröz a chat befejezéshez (szöveg generálás) és a vektoros kereséshez (beágyazások). Ezek beállítására vonatkozó utasításokat a kapcsolódó feladatokban találod majd.

### 2.3 Azure konfigurálása: Portálról

Az Azure OpenAI végpont és kulcs értékei az [Azure Portálon](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) találhatók, kezdjük ott.

1. Lépj be az [Azure Portálra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Kattints a bal oldali menüben a **Keys and Endpoint** opcióra.  
1. Kattints a **Show Keys** gombra – meg kell jelennie a következőknek: KEY 1, KEY 2 és Endpoint.  
1. Az AZURE_OPENAI_API_KEY értékéhez használd a KEY 1-et.  
1. Az AZURE_OPENAI_ENDPOINT értékéhez használd az Endpointot.

Ezután szükségünk van a telepített modellek végpontjaira.

1. Kattints az Azure OpenAI erőforrás bal oldali menüjében a **Model deployments** opcióra.  
1. A megnyíló oldalon válaszd a **Manage Deployments** lehetőséget.

Ez az Azure OpenAI Studio weboldalára visz, ahol a további értékeket megtaláljuk az alábbiak szerint.

### 2.4 Azure konfigurálása: Studioból

1. Navigálj az [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) oldalra **az erőforrásodból** az előző pont szerint.  
1. Kattints a bal oldali menüben a **Deployments** fülre, hogy lásd a jelenleg telepített modelleket.  
1. Ha a kívánt modell nincs telepítve, használd a **Create new deployment** lehetőséget a telepítéshez.  
1. Szükséged lesz egy _szöveg generáló_ modellre – ajánlott: **gpt-35-turbo**  
1. Szükséged lesz egy _szöveg beágyazó_ modellre – ajánlott: **text-embedding-ada-002**

Frissítsd a környezeti változókat a használt _Deployment name_-nel. Ez általában megegyezik a modell nevével, hacsak nem változtattad meg kifejezetten. Például:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne felejtsd el elmenteni a .env fájlt a módosítások után!** Ezután kiléphetsz a fájlból, és folytathatod a notebook futtatására vonatkozó utasításokat.

### 2.5 OpenAI konfigurálása: Profilból

Az OpenAI API kulcsodat megtalálod az [OpenAI fiókodban](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ha még nincs, regisztrálj, és hozz létre egy API kulcsot. Miután megvan a kulcs, töltsd ki vele az `OPENAI_API_KEY` változót a `.env` fájlban.

### 2.6 Hugging Face konfigurálása: Profilból

A Hugging Face tokenedet a profilodban találod az [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) menüpont alatt. Ne oszd meg nyilvánosan! Hozz létre egy új tokent erre a projektre, és másold be a `.env` fájl `HUGGING_FACE_API_KEY` változójába. _Megjegyzés:_ Ez technikailag nem API kulcs, de hitelesítésre szolgál, ezért a következetesség kedvéért ezt a nevet használjuk.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.