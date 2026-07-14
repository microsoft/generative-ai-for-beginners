# Kezdés ezzel a tanfolyammal

Nagyon izgatottak vagyunk, hogy elkezded ezt a tanfolyamot, és meglátod, milyen inspiráló dolgokat tudsz létrehozni generatív MI-vel!

A sikered érdekében ez az oldal ismerteti a telepítési lépéseket, a műszaki követelményeket, és azt, hogy hol kérhetsz segítséget, ha szükséges.

## Telepítési lépések

A tanfolyam elkezdéséhez el kell végezned az alábbi lépéseket.

### 1. Repozitórium fork-olása

[Fork-old ezt a teljes repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy módosítani tudd a kódot és teljesíthesd a feladatokat. Emellett [meg is jelölheted csillaggal (🌟) ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld, valamint kapcsolódó repókat.

### 2. Hozz létre egy codespace-t

A kód futtatásakor felmerülő függőségi problémák elkerülése érdekében javasoljuk, hogy ebben a tanfolyamban a [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) használatával dolgozz.

A saját forkodban: **Code -> Codespaces -> New on main**

![Dialógus, amely a codespace létrehozásához szükséges gombokat mutatja](../../../translated_images/hu/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adj hozzá egy titkot

1. ⚙️ Fogaskerék ikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nevezd el OPENAI_API_KEY-nek, illeszd be a kulcsodat, és mentsd el.

### 3. Mi a következő lépés?

| Szeretném…          | Ugrás ide…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Kezdeni az 1. leckét | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline dolgozni    | [`setup-local.md`](02-setup-local.md)                                   |
| LLM szolgáltatót beállítani | [`providers.md`](03-providers.md)                                    |
| Megismerkedni más tanulókkal | [Csatlakozz a Discordunkhoz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Hibakeresés


| Tünet                                     | Megoldás                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| A konténer építése > 10 percig fennakad   | **Codespaces ➜ „Rebuild Container”**                            |
| `python: command not found`                 | A terminál nem csatlakozott; kattints a **+** ➜ *bash*          |
| `401 Unauthorized` az OpenAI-tól            | Hibás vagy lejárt `OPENAI_API_KEY`                              |
| VS Code „Dev container mounting…” üzenetet mutat | Frissítsd a böngészőfület – a Codespaces néha elveszíti a kapcsolatot |
| Hiányzik a notebook kernel                 | Notebook menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++ vagy bármilyen más szerkesztő). Add hozzá az alábbi sorokat, helyettesítve a helykitöltőket a valódi Microsoft Foundry Models végpontoddal és kulcsoddal (lásd a [`providers.md`](03-providers.md) fájlt, hogyan szerezheted be ezeket):

   > **Megjegyzés:** A GitHub Models (és az ehhez tartozó `GITHUB_TOKEN` változó) 2026 július végén megszűnik. Ehelyett használd a [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) szolgáltatást.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Mentsd el a fájlt**: Mentsd el a módosításokat, majd zárd be a szerkesztőt.

5. **Telepítsd a `python-dotenv` csomagot**: Ha még nem telepítetted, telepítened kell a `python-dotenv` csomagot, hogy a `.env` fájlból betölthesd a környezeti változókat a Python alkalmazásodba. Telepítheted `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Környezeti változók betöltése a Python szkriptben**: A Python szkriptedben használd a `python-dotenv` csomagot, hogy betöltsd a `.env` fájlban tárolt környezeti változókat:

   ```python
   from dotenv import load_dotenv
   import os

   # Környezeti változók betöltése a .env fájlból
   load_dotenv()

   # Hozzáférés a Microsoft Foundry Models változókhoz
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ennyi az egész! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a Microsoft Foundry Models hitelesítő adataidat, és betöltötted őket a Python alkalmazásodba.

## Hogyan futtatható helyileg a számítógépeden

A kód helyi futtatásához a számítógépeden szükséged lesz valamilyen [Python verzió telepítésére](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ezt követően le kell klónoznod a repót:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ha mindent letöltöttél, kezdhetsz is dolgozni!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), a Python és néhány csomag telepítéséhez.
Maga a Conda csomagkezelő, amely megkönnyíti különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Hasznos továbbá kevésbé elterjedt csomagok telepítéséhez, amelyek nem érhetők el `pip` segítségével.

Kövesd a [Miniconda telepítési útmutatóját](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) a telepítéshez.

Ha telepítetted a Minicondát, klónozd le a [tárolót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ha még nem tetted meg).

Ezután létre kell hoznod egy virtuális környezetet. Conda használata esetén hozz létre egy új környezeti fájlt (_environment.yml_). Ha Codespaces-ben dolgozol, helyezd el ezt a `.devcontainer` mappában, azaz `.devcontainer/environment.yml` fájlként.

Töltsd fel a környezeti fájlt a lenti példával:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Ha conda használata közben hibákat tapasztalsz, manuálisan is telepítheted a Microsoft AI Könyvtárakat az alábbi parancs futtatásával egy terminálban.

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl tartalmazza a szükséges függőségeket. A `<environment-name>` helyére írd a Conda környezet kívánt nevét, a `<python-version>` helyére pedig a kívánt Python verziót, például a `3` a legújabb fő verzió.

Ezután létrehozhatod a Conda környezeted a következő parancsok lefuttatásával a parancssorban/terminálban:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # A .devcontainer alkönyvtár csak a Codespace beállításokra érvényes
conda activate ai4beg
```

Ha problémába ütközöl, nézd meg a [Conda környezeti útmutatóját](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata Python támogatással

Javasoljuk, hogy ehhez a tanfolyamhoz a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztőt használd a [Python támogatást nyújtó bővítménnyel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Ez azonban inkább ajánlás, nem kötelező.

> **Megjegyzés**: Ha megnyitod a tanfolyam repóját VS Code-ban, lehetőséged van a projektet konténerben is beállítani. Ez az oka a [különleges `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappának a repóban. Erről később lesz szó.

> **Megjegyzés**: Amint leklónozod és megnyitod a mappát VS Code-ban, az automatikusan felajánlja a Python támogatású bővítmény telepítését.

> **Megjegyzés**: Ha a VS Code azt javasolja, hogy nyisd újra a repót konténerben, akkor ezt utasítsd el, ha a helyileg telepített Python verziót szeretnéd használni.

### Jupyter használata böngészőben

A projektet a [Jupyter környezetben](https://jupyter.org?WT.mc_id=academic-105485-koreyst) is fejlesztheted közvetlenül a böngészőből. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kellemes fejlesztési élményt nyújt, például automatikus kiegészítést, kódkiemelést és egyebeket.

A helyi indításhoz menj a terminálba/parancssorba, navigálj a tanfolyam könyvtárába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és a hozzáférés URL-je megjelenik a parancssor ablakában.

Amint elérted az URL-t, látnod kell a tanfolyam vázlatát és navigálhatsz bármely `*.ipynb` fájlhoz. Például: `08-building-search-applications/python/oai-solution.ipynb`.

### Futtatás konténerben

Az alternatíva a saját gépen vagy Codespace-ben való beállítás helyett az, hogy egy [konténert](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) használsz. A tanfolyam repójában található különleges `.devcontainer` mappa lehetővé teszi, hogy a VS Code projektet konténerben állítsa be. Codespaces-en kívül ehhez Docker telepítése szükséges, ami egy kissé bonyolult, ezért csak konténerekkel tapasztalattal rendelkezőknek ajánljuk.

Az API kulcsaid biztonságos tárolásának egyik legjobb módja GitHub Codespaces esetén a Codespace Secrets használata. Erről a [Codespaces titkok kezeléséről](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) találhatsz útmutatót.


## Leckék és technikai követelmények

A tanfolyam 6 elméleti és 6 programozási leckéből áll.

A programozási leckékhez az Azure OpenAI szolgáltatást használjuk. Ehhez szükséged lesz hozzáférésre az Azure OpenAI szolgáltatáshoz és API kulcsra. Hozzáférést az [űrlap kitöltésével igényelhetsz](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Amíg a kérelmed feldolgozás alatt áll, a programozási leckékhez mellékelt `README.md` fájlokból megtekintheted a kódot és az eredményeket.

## Azure OpenAI szolgáltatás első használata

Ha először használod az Azure OpenAI szolgáltatást, kérjük, kövesd ezt az útmutatót a [szolgáltatás létrehozásához és telepítéséhez](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## OpenAI API első használata

Ha először dolgozol az OpenAI API-val, kérjük, kövesd a [gyors kezdő útmutatót az interfész használatához](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Ismerkedj meg más tanulókkal

Létrehoztunk csatornákat az [AI Community Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), ahol találkozhatsz más tanulókkal. Ez remek lehetőség, hogy kapcsolatokat építs más hasonló gondolkodású vállalkozókkal, fejlesztőkkel, diákokkal, és mindenkivel, aki fejlődni szeretne a generatív MI terén.

[![Csatlakozás a discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata is jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Közreműködés

Ez a tanfolyam nyílt forráskódú kezdeményezés. Ha javítási lehetőségeket vagy hibákat találsz, kérjük, hozz létre egy [Pull Request-et](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy jelents hibát a [GitHub issue-k között](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata figyelemmel kíséri az összes hozzájárulást. A nyílt forráskódhoz való hozzájárulás remek módja annak, hogy karriert építs a generatív MI területén.

A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement (CLA) licencmegállapodást, amelyben kijelented, hogy jogod van hozzájárulni, és valóban megadod számunkra a jogokat a használathoz. Részletekért látogass el a [CLA, Contributor License Agreement weboldalára](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: ebben a repóban szöveg fordításakor kérjük, kerüld a gépi fordítást. A fordításokat közösségi ellenőrzésnek vetjük alá, ezért csak olyan nyelvek esetén támogasd a fordítást, amelyekben jártas vagy.

Amikor pull request-et nyújtasz be, a CLA-bot automatikusan eldönti, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően jelöli meg a PR-t (címke, megjegyzés). Csak egyszer kell ezt megtenned az összes repót érintően, amely a CLA-t használja.


Ez a projekt elfogadta a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). További információkért olvassa el a Magatartási Kódex GYIK-jét, vagy forduljon az [opencode e-mail címhez](opencode@microsoft.com) további kérdésekkel vagy észrevételekkel.

## Kezdjünk hozzá

Most, hogy elvégezte a tanfolyam befejezéséhez szükséges lépéseket, kezdjük azzal, hogy megismerkedünk a [Generatív mesterséges intelligencia és nagy nyelvi modellek bevezetésével](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->