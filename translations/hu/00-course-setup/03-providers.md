<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:48:05+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "hu"
}
-->
# LLM szolgáltató kiválasztása és beállítása 🔑

A feladatokat **lehetőség szerint** úgy is be lehet állítani, hogy egy vagy több nagy nyelvi modell (LLM) telepítésével működjenek, egy támogatott szolgáltatón keresztül, mint például az OpenAI, Azure vagy Hugging Face. Ezek _hosztolt végpontot_ (API-t) biztosítanak, amelyhez megfelelő hitelesítő adatokkal (API kulcs vagy token) programozottan hozzáférhetünk. Ebben a kurzusban az alábbi szolgáltatókat tárgyaljuk:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), amely számos modellt kínál, köztük a fő GPT sorozatot.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst), amely az OpenAI modelleket vállalati szintű szolgáltatásokkal kínálja
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst), amely nyílt forráskódú modelleket és inferencia szervert biztosít

**Ezekhez a gyakorlati feladatokhoz saját fiókra lesz szükséged.** A feladatok opcionálisak, így eldöntheted, hogy egyet, mindet, vagy egyiket sem állítod be, érdeklődésed szerint. Néhány tipp a regisztrációhoz:

| Regisztráció | Költség | API kulcs | Playground | Megjegyzések |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Árazás](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekthez kötött](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Többféle modell elérhető |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Árazás](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Gyorsindítás](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Gyorsindítás](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Előzetes jelentkezés szükséges](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Árazás](https://huggingface.co/pricing) | [Hozzáférési tokenek](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [A Hugging Chat csak korlátozott modelleket kínál](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Az alábbi lépéseket követve _konfigurálhatod_ ezt a repót a különböző szolgáltatók használatához. Azok a feladatok, amelyek egy adott szolgáltatót igényelnek, a fájlnevükben az alábbi címkék egyikét tartalmazzák:

- `aoai` - Azure OpenAI végpont és kulcs szükséges
- `oai` - OpenAI végpont és kulcs szükséges
- `hf` - Hugging Face token szükséges

Beállíthatsz egyet, egyiket sem, vagy mindegyik szolgáltatót. Az érintett feladatok hibát fognak jelezni, ha hiányoznak a hitelesítő adatok.

## `.env` fájl létrehozása

Feltételezzük, hogy már elolvastad a fenti útmutatót, regisztráltál a megfelelő szolgáltatónál, és megszerezted a szükséges hitelesítő adatokat (API_KEY vagy token). Az Azure OpenAI esetén feltételezzük, hogy már van érvényes Azure OpenAI Service telepítésed (végpont), legalább egy GPT modellel, amely chat completion-re van telepítve.

A következő lépés, hogy beállítsd a **helyi környezeti változókat** az alábbiak szerint:

1. Keresd meg a gyökérkönyvtárban a `.env.copy` fájlt, amelynek tartalma ehhez hasonló:

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

2. Másold át ezt a fájlt `.env` néven az alábbi paranccsal. Ez a fájl _gitignore-olt_, így a titkos adatok biztonságban maradnak.

   ```bash
   cp .env.copy .env
   ```

3. Töltsd ki az értékeket (cseréld le a jobb oldali helyőrzőket az `=` jel után) a következő szakaszban leírtak szerint.

4. (Opcionális) Ha GitHub Codespaces-t használsz, lehetőséged van a környezeti változókat _Codespaces secrets_-ként elmenteni ehhez a repóhoz. Ebben az esetben nem kell helyi .env fájlt beállítanod. **Fontos azonban, hogy ez a lehetőség csak akkor működik, ha GitHub Codespaces-t használsz.** Ha helyette Docker Desktopot használsz, akkor továbbra is szükség lesz a .env fájl beállítására.

## `.env` fájl kitöltése

Nézzük át gyorsan a változóneveket, hogy megértsük, mit jelentenek:

| Változó  | Leírás  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ez az a felhasználói hozzáférési token, amit a profilodban állítottál be |
| OPENAI_API_KEY | Ez a szolgáltatás használatához szükséges hitelesítési kulcs, nem-Azure OpenAI végpontokhoz |
| AZURE_OPENAI_API_KEY | Ez a szolgáltatás használatához szükséges hitelesítési kulcs |
| AZURE_OPENAI_ENDPOINT | Ez az Azure OpenAI erőforrás telepített végpontja |
| AZURE_OPENAI_DEPLOYMENT | Ez a _szöveg generálás_ modell telepítési végpontja |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ez a _szöveg beágyazás_ modell telepítési végpontja |
| | |

Megjegyzés: Az utolsó két Azure OpenAI változó alapértelmezett modellt jelöl chat completion (szöveg generálás) és vektoros keresés (beágyazás) céljára. Ezek beállítására vonatkozó utasításokat a kapcsolódó feladatokban találod.

## Azure beállítása: Portálról

Az Azure OpenAI végpont és kulcs értékeit az [Azure Portálon](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) találod, kezdjük tehát ott.

1. Lépj be az [Azure Portálra](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kattints a bal oldali menüben a **Keys and Endpoint** lehetőségre.
1. Kattints a **Show Keys** gombra – itt látni fogod: KEY 1, KEY 2 és Endpoint.
1. Az AZURE_OPENAI_API_KEY-hez használd a KEY 1 értékét
1. Az AZURE_OPENAI_ENDPOINT-hoz használd az Endpoint értékét

Ezután szükségünk lesz a telepített modellek végpontjaira is.

1. Kattints a bal oldali menüben az **Model deployments** lehetőségre az Azure OpenAI erőforrásnál.
1. Az oldalon kattints a **Manage Deployments** gombra

Ez átirányít az Azure OpenAI Studio weboldalára, ahol a további értékeket találod, ahogy lentebb leírjuk.

## Azure beállítása: Studio-ból

1. Navigálj az [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) oldalra **a saját erőforrásodból**, ahogy fentebb leírtuk.
1. Kattints a bal oldali menüben a **Deployments** fülre, hogy lásd a jelenleg telepített modelleket.
1. Ha a kívánt modell nincs telepítve, használd a **Create new deployment** lehetőséget a telepítéshez.
1. Szükséged lesz egy _szöveg-generáló_ modellre – ajánlott: **gpt-35-turbo**
1. Szükséged lesz egy _szöveg-beágyazó_ modellre – ajánlott: **text-embedding-ada-002**

Most frissítsd a környezeti változókat a használt _Deployment name_-nek megfelelően. Ez általában megegyezik a modell nevével, hacsak nem változtattad meg. Például így nézhet ki:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne felejtsd el elmenteni a .env fájlt, ha végeztél!** Ezután kiléphetsz a fájlból, és visszatérhetsz a notebook futtatására vonatkozó utasításokhoz.

## OpenAI beállítása: Profilból

Az OpenAI API kulcsodat a [OpenAI fiókodban](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) találod. Ha még nincs ilyen kulcsod, regisztrálj egy fiókot, és hozz létre egy API kulcsot. Ha már megvan a kulcs, ezt kell beírnod a `.env` fájlban az `OPENAI_API_KEY` változóhoz.

## Hugging Face beállítása: Profilból

A Hugging Face tokenedet a profilodban, az [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alatt találod. Ezeket ne tedd közzé és ne oszd meg nyilvánosan. Ehelyett hozz létre egy új tokent ehhez a projekthez, és másold be a `.env` fájlba a `HUGGING_FACE_API_KEY` változóhoz. _Megjegyzés:_ Ez technikailag nem API kulcs, de hitelesítésre használjuk, ezért a névhasználatot egységesen megtartjuk.

---

**Jogi nyilatkozat**:
Ez a dokumentum AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.