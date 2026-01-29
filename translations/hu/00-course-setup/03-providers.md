# LLM szolgáltató kiválasztása és konfigurálása 🔑

A feladatok **esetleg** beállíthatók úgy is, hogy egy vagy több Nagy Nyelvi Modell (LLM) telepítés ellen dolgozzanak egy támogatott szolgáltatón keresztül, mint például az OpenAI, Azure vagy Hugging Face. Ezek egy _hosztolt végpontot_ (API-t) biztosítanak, amelyhez a megfelelő hitelesítő adatokkal (API kulcs vagy token) programozottan hozzáférhetünk. Ebben a tanfolyamban az alábbi szolgáltatókat tárgyaljuk:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) különféle modellekkel, beleértve a GPT sorozatot.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI modellekhez, vállalati felkészültséggel
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) nyílt forráskódú modellekhez és inferencia szerverhez

**Ezekhez a gyakorlatokhoz saját fiókokat kell használnod**. A feladatok opcionálisak, így eldöntheted, hogy egy, mindegyik vagy egyik szolgáltatót sem állítod be érdeklődésed szerint. Néhány útmutató a regisztrációhoz:

| Regisztráció | Költség | API kulcs | Játékterem | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekt alapú](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kód nélküli, webes](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Több modell elérhető |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK gyorsindítás](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio gyorsindítás](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Előzetes engedélykérés szükséges](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat korlátozott modellekkel](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Kövesd az alábbi utasításokat a _tárház_ konfigurálásához különböző szolgáltatók használatához. Az adott szolgáltatót igénylő feladatok fájlnevében az alábbi címkék egyikét találod:

- `aoai` - Azure OpenAI végpontot, kulcsot igényel
- `oai` - OpenAI végpontot, kulcsot igényel
- `hf` - Hugging Face tokent igényel

Beállíthatsz egy, semelyik vagy mindhárom szolgáltatót. A kapcsolódó feladatok hibát jeleznek hiányzó hitelesítő adatok esetén.

## `.env` fájl létrehozása

Feltételezzük, hogy már elolvastad a fentieket, regisztráltál a megfelelő szolgáltatónál, és megszerezted a szükséges hitelesítő adatokat (API_KEY vagy token). Azure OpenAI esetén feltételezzük, hogy van érvényes telepítésed egy Azure OpenAI szolgáltatásból (végpont), legalább egy GPT modelllel chat befejezéshez.

A következő lépés a **helyi környezeti változók** beállítása az alábbiak szerint:

1. Nézd meg a gyökérmappában a `.env.copy` fájlt, amelynek tartalma valahogy így néz ki:

   ```bash
   # OpenAI Szolgáltató
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Alapértelmezett beállítva!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Másold át ezt a fájlt `.env` néven az alábbi parancs segítségével. Ez a fájl _gitignore-olva_ van, így a titkok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltsd ki az értékeket (cseréld ki a jobb oldali helyőrzőket az `=` után) a következő szakaszban leírtak szerint.

4. (Opcionális) Ha GitHub Codespaces-t használsz, lehetőséged van a környezeti változókat _Codespaces titkokként_ elmenteni ehhez a tárhoz. Ebben az esetben nem kell helyi .env fájlt beállítanod. **Fontos, hogy ez az opció csak GitHub Codespaces használata esetén működik.** Docker Desktop használata esetén továbbra is szükséges a .env fájl beállítása.

## `.env` fájl kitöltése

Nézzük meg gyorsan a változóneveket, hogy megértsük, mit jelentenek:

| Változó  | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez a felhasználói hozzáférési token, amelyet a profilodban állítottál be |
| OPENAI_API_KEY | Ez az engedélyező kulcs a nem Azure OpenAI végpontok használatához |
| AZURE_OPENAI_API_KEY | Ez az engedélyező kulcs az Azure OpenAI szolgáltatás használatához |
| AZURE_OPENAI_ENDPOINT | Ez az Azure OpenAI erőforrás telepített végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveg generálás_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg beágyazás_ modell telepítési végpontja |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó egy alapértelmezett modellt tükröz chat befejezéshez (szöveg generálás) és vektor kereséshez (beágyazások). Ezek beállítására vonatkozó utasításokat a kapcsolódó feladatokban találod.

## Azure konfigurálása: Portálról

Az Azure OpenAI végpont és kulcs értékei az [Azure Portálon](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) találhatók, kezdjük ott.

1. Lépj be az [Azure Portálra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kattints a bal oldali menüben a **Kulcsok és végpont** opcióra.
1. Kattints a **Kulcsok megjelenítése** gombra - a következőt kell látnod: 1. KULCS, 2. KULCS és Végpont.
1. Az 1. KULCS értékét használd az AZURE_OPENAI_API_KEY-hez
1. A Végpont értékét használd az AZURE_OPENAI_ENDPOINT-hez

Ezután szükségünk van a telepített modellek végpontjaira.

1. Kattints a bal oldali menüben az **Modellek telepítése** opcióra az Azure OpenAI erőforrásnál.
1. A megjelenő oldalon kattints a **Telepítések kezelése** gombra

Ez elvisz az Azure OpenAI Studio webhelyre, ahol megtaláljuk a további értékeket az alábbiak szerint.

## Azure konfigurálása: Studioból

1. Navigálj az [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) oldalra **az erőforrásodból** a fentiek szerint.
1. Kattints a **Telepítések** fülre (bal oldali menü), hogy lásd a jelenleg telepített modelleket.
1. Ha a kívánt modell nincs telepítve, használd az **Új telepítés létrehozása** opciót a telepítéshez.
1. Szükséged lesz egy _szöveg-generáló_ modellre - ajánlott: **gpt-35-turbo**
1. Szükséged lesz egy _szöveg-beágyazó_ modellre - ajánlott: **text-embedding-ada-002**

Most frissítsd a környezeti változókat, hogy tükrözzék a használt _Telepítés nevét_. Ez általában megegyezik a modell nevével, hacsak nem változtattad meg kifejezetten. Például:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne felejtsd el elmenteni a .env fájlt a befejezés után**. Most kiléphetsz a fájlból, és folytathatod a jegyzet futtatására vonatkozó utasításokat.

## OpenAI konfigurálása: Profilból

Az OpenAI API kulcsod megtalálható az [OpenAI fiókodban](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ha még nincs, regisztrálhatsz és létrehozhatsz egy API kulcsot. Miután megvan a kulcs, kitöltheted vele az `OPENAI_API_KEY` változót a `.env` fájlban.

## Hugging Face konfigurálása: Profilból

A Hugging Face tokened megtalálható a profilodban az [Hozzáférési tokenek](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alatt. Ne tedd közzé vagy oszd meg nyilvánosan. Ehelyett hozz létre egy új tokent ehhez a projekthez, és másold be a `.env` fájl `HUGGING_FACE_API_KEY` változójába. _Megjegyzés:_ Ez technikailag nem API kulcs, de hitelesítésre használjuk, ezért megtartjuk ezt az elnevezést a következetesség érdekében.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->