<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:57:21+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hu"
}
-->
# Fejlesztői környezet beállítása

Ezt a tárolót és tanfolyamot egy [fejlesztői konténerrel](https://containers.dev?WT.mc_id=academic-105485-koreyst) állítottuk be, amely univerzális futási környezetet biztosít a Python3, .NET, Node.js és Java fejlesztéshez. A kapcsolódó konfiguráció az `devcontainer.json` fájlban van meghatározva, amely az `.devcontainer/` mappában található a tároló gyökerénél.

A fejlesztői konténer aktiválásához indítsa el a [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (felhőalapú futási környezethez) vagy a [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (helyi eszközön futó futási környezethez). Olvassa el [ezt a dokumentációt](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) további részletekért arról, hogyan működnek a fejlesztői konténerek a VS Code-ban.

> [!TIP]  
> Javasoljuk a GitHub Codespaces használatát a gyors kezdéshez minimális erőfeszítéssel. Nagylelkű [ingyenes használati kvótát](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) biztosít személyes fiókokhoz. Konfigurálja az [időtúllépéseket](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), hogy leállítsa vagy törölje az inaktív codespaceseket a kvóta használatának maximalizálása érdekében.

## 1. Feladatok végrehajtása

Minden leckéhez _opcionális_ feladatok tartoznak, amelyek több programozási nyelven is elérhetők, például: Python, .NET/C#, Java és JavaScript/TypeScript. Ez a rész általános útmutatást ad a feladatok végrehajtásához.

### 1.1 Python feladatok

A Python feladatok alkalmazásokként (`.py` fájlok) vagy Jupyter notebookokként (`.ipynb` fájlok) vannak megadva.
- A notebook futtatásához nyissa meg a Visual Studio Code-ban, majd kattintson a _Select Kernel_ (jobb felső sarokban) és válassza ki az alapértelmezett Python 3 opciót. Most már futtathatja a _Run All_-t a notebook végrehajtásához.
- Python alkalmazások parancssori futtatásához kövesse a feladat-specifikus utasításokat, hogy biztosan a megfelelő fájlokat válassza ki, és megadja a szükséges argumentumokat.

## 2. Szolgáltatók konfigurálása

A feladatok **esetleg** úgy is beállíthatók, hogy egy vagy több Nagy Nyelvi Modell (LLM) telepítéssel működjenek egy támogatott szolgáltató, például OpenAI, Azure vagy Hugging Face révén. Ezek _hostolt végpontot_ (API) biztosítanak, amelyet programozottan elérhetünk a megfelelő hitelesítési adatokkal (API kulcs vagy token). Ebben a tanfolyamban ezekről a szolgáltatókról beszélünk:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) különféle modellekkel, beleértve a GPT sorozatot.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) az OpenAI modellekhez, vállalati készenléttel a fókuszban
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) nyílt forráskódú modellekhez és következtetési szerverhez

**Saját fiókokat kell használnia ezekhez a gyakorlatokhoz**. A feladatok opcionálisak, így dönthet úgy, hogy egyet, mindet - vagy egyet sem - állít be a szolgáltatók közül az érdeklődése alapján. Néhány útmutató a regisztrációhoz:

| Regisztráció | Költség | API Kulcs | Játszótér | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekt alapú](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Több modell elérhető |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Gyors kezdés](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Stúdió Gyors kezdés](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Előzetes jelentkezés szükséges a hozzáféréshez](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési Tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [A Hugging Chat korlátozott modelleket tartalmaz](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Kövesse az alábbi utasításokat a tároló _konfigurálásához_ különböző szolgáltatókkal való használatra. Azok a feladatok, amelyekhez egy adott szolgáltató szükséges, a fájlnevében az alábbi címkék egyikét fogják tartalmazni:
 - `aoai` - Azure OpenAI végpontot, kulcsot igényel
 - `oai` - OpenAI végpontot, kulcsot igényel
 - `hf` - Hugging Face tokent igényel

Beállíthat egyet, semmit vagy minden szolgáltatót. A kapcsolódó feladatok egyszerűen hibát jeleznek a hiányzó hitelesítési adatok miatt.

### 2.1. `.env` fájl létrehozása

Feltételezzük, hogy már elolvasta a fenti útmutatót, és regisztrált a megfelelő szolgáltatónál, valamint megszerezte a szükséges hitelesítési adatokat (API_KULCS vagy token). Az Azure OpenAI esetében feltételezzük, hogy van egy érvényes Azure OpenAI Szolgáltatás telepítése (végpont), amelyen legalább egy GPT modell telepítve van a csevegés befejezéséhez.

A következő lépés az **helyi környezeti változók** konfigurálása az alábbiak szerint:

1. Keresse meg a gyökérmappában az `.env.copy` fájlt, amelynek tartalma ilyen:

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

2. Másolja ezt a fájlt `.env` néven az alábbi paranccsal. Ez a fájl _gitignore-d_, így a titkok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltse ki az értékeket (cserélje ki a helyőrzőket az `=` jobb oldalán) a következő szakaszban leírtak szerint.

3. (Opcionális) Ha GitHub Codespaces-t használ, lehetősége van a környezeti változókat _Codespaces titokként_ elmenteni ehhez a tárolóhoz társítva. Ebben az esetben nem kell helyi .env fájlt beállítania. **Megjegyzés: ez az opció csak akkor működik, ha GitHub Codespaces-t használ.** Továbbra is be kell állítania a .env fájlt, ha Docker Desktopot használ.

### 2.2. `.env` fájl kitöltése

Nézzük meg gyorsan a változóneveket, hogy megértsük, mit képviselnek:

| Változó  | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez a felhasználói hozzáférési token, amelyet a profiljában állít be |
| OPENAI_API_KEY | Ez a szolgáltatás használatának engedélyezési kulcsa nem-Azure OpenAI végpontokhoz |
| AZURE_OPENAI_API_KEY | Ez a szolgáltatás használatának engedélyezési kulcsa |
| AZURE_OPENAI_ENDPOINT | Ez az Azure OpenAI erőforrás telepített végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveg generálási_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg beágyazási_ modell telepítési végpontja |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó egy alapértelmezett modellt tükröz a csevegés befejezéséhez (szöveg generálás) és a vektorkereséshez (beágyazások) megfelelően. A beállításukra vonatkozó utasítások a releváns feladatokban lesznek meghatározva.

### 2.3 Azure konfigurálása: a Portálról

Az Azure OpenAI végpont és kulcsértékek az [Azure Portálon](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) találhatók, így kezdjük ott.

1. Menjen az [Azure Portálra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kattintson a **Kulcsok és végpont** opcióra az oldalsávban (menü bal oldalon).
1. Kattintson a **Kulcsok megjelenítése** - látni fogja a következőket: KULCS 1, KULCS 2 és Végpont.
1. Használja a KULCS 1 értéket az AZURE_OPENAI_API_KEY-hez
1. Használja a Végpont értéket az AZURE_OPENAI_ENDPOINT-hoz

Ezután szükségünk van a telepített modellek konkrét végpontjaira.

1. Kattintson az **Model telepítések** opcióra az oldalsávban (bal menü) az Azure OpenAI erőforráshoz.
1. A céloldalon kattintson a **Telepítések kezelése** gombra

Ez elviszi az Azure OpenAI Stúdió webhelyére, ahol megtaláljuk a többi értéket az alábbiakban leírtak szerint.

### 2.4 Azure konfigurálása: a Stúdióból

1. Navigáljon az [Azure OpenAI Stúdióba](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **az erőforrásából** az előzőekben leírtak szerint.
1. Kattintson a **Telepítések** fülre (oldalsáv, bal) a jelenleg telepített modellek megtekintéséhez.
1. Ha a kívánt modell nincs telepítve, használja a **Új telepítés létrehozása** lehetőséget a telepítéséhez.
1. Szüksége lesz egy _szöveg-generálási_ modellre - javasoljuk: **gpt-35-turbo**
1. Szüksége lesz egy _szöveg-beágyazási_ modellre - javasoljuk **text-embedding-ada-002**

Most frissítse a környezeti változókat, hogy tükrözzék a használt _Telepítési nevet_. Ez általában megegyezik a modell névvel, hacsak nem változtatta meg kifejezetten. Tehát például lehet, hogy:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne felejtse el menteni a .env fájlt, amikor elkészült**. Most kiléphet a fájlból, és visszatérhet a notebook futtatására vonatkozó utasításokhoz.

### 2.5 OpenAI konfigurálása: a Profilból

Az OpenAI API kulcsa megtalálható az [OpenAI fiókjában](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ha még nincs, regisztrálhat egy fiókot és létrehozhat egy API kulcsot. Miután megvan a kulcs, használhatja az `OPENAI_API_KEY` változó kitöltéséhez az `.env` fájlban.

### 2.6 Hugging Face konfigurálása: a Profilból

A Hugging Face tokenje megtalálható a profiljában az [Hozzáférési Tokenek](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alatt. Ne tegye közzé vagy ossza meg ezeket nyilvánosan. Ehelyett hozzon létre egy új tokent ehhez a projekt használatához, és másolja azt az `.env` fájlba a `HUGGING_FACE_API_KEY` változó alatt. _Megjegyzés:_ Technikailag ez nem egy API kulcs, de hitelesítéshez használják, ezért megtartjuk ezt a névkonvenciót a konzisztencia érdekében.

**Jogi nyilatkozat**:  
Ezt a dokumentumot a [Co-op Translator](https://github.com/Azure/co-op-translator) mesterséges intelligencia fordítási szolgáltatásával fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.