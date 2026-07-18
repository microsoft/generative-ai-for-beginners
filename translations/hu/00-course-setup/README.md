# Első lépések a tanfolyammal

Nagyon izgatottak vagyunk, hogy elkezdheted ezt a tanfolyamot, és megnézheted, hogyan inspirálódhatsz a Generatív MI-vel való alkotáshoz!

A sikered érdekében ezen az oldalon összefoglaljuk a beállítási lépéseket, a technikai követelményeket és azt, hogy hol kérhetsz segítséget szükség esetén.

## Beállítási lépések

A tanfolyam megkezdéséhez a következő lépéseket kell végrehajtanod.

### 1. Forkold ezt a repót

[Forkold le ezt az egész repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy módosíthasd a kódot és teljesíthesd a kihívásokat. Ezenkívül [csillagozhatod (🌟) ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld ezt és a kapcsolódó repókat.

### 2. Hozz létre egy codespace-et

A kód futtatásakor felmerülő függőségi problémák elkerülése érdekében azt javasoljuk, hogy a tanfolyamot a [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) használatával futtasd.

A forkodban: **Code -> Codespaces -> New on main**

![A dialógus, amely gombokat mutat a codespace létrehozásához](../../../translated_images/hu/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adj hozzá egy titkot

1. ⚙️ Fogaskerék ikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nevezd el OPENAI_API_KEY-nek, illeszd be a kulcsod, Mentés.

### 3. Mi a következő lépés?

| Szeretném…          | Menj ide…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Elkezdeni az 1. leckét| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline dolgozni     | [`setup-local.md`](02-setup-local.md)                                   |
| LLM szolgáltató beállítása | [`providers.md`](03-providers.md)                                        |
| Más tanulókkal találkozni | [Csatlakozz a Discord csatornánkhoz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Hibakeresés


| Tünet                                   | Javítás                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Konténer építése beragadt > 10 perc | **Codespaces ➜ „Rebuild Container”**                            |
| `python: command not found`               | A terminál nem csatlakozott; kattints a **+** ➜ *bash*                    |
| `401 Unauthorized` az OpenAI-tól           | Hibás / lejárt `OPENAI_API_KEY`                                |
| VS Code „Dev container mounting…” üzenetet mutat | Frissítsd a böngészőfület—néha a Codespaces kapcsolat megszakad   |
| Notebook kernel hiányzik                   | Notebook menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++, vagy bármilyen más szerkesztő). Add hozzá az alábbi sorokat, az adott helyekre a saját Microsoft Foundry Models végpontod és kulcsod beillesztésével (lásd a [`providers.md`](03-providers.md) fájlt, hogy hogyan szerezheted meg ezeket):

   > **Megjegyzés:** A GitHub Models (és a `GITHUB_TOKEN` változó) 2026 július végén megszűnik. Helyette használd a [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Mentés**: Mentsd el a változtatásokat, majd zárd be a szövegszerkesztőt.

5. **Telepítsd a `python-dotenv` csomagot**: Ha még nem tetted meg, szükséged lesz a `python-dotenv` csomagra, hogy betölthesd a `.env` fájlban definiált környezeti változókat a Python alkalmazásodba. Telepítheted a `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Töltsd be a környezeti változókat a Python szkriptben**: A Python kódodban használd a `python-dotenv` csomagot a `.env` fájlban lévő változók betöltéséhez:

   ```python
   from dotenv import load_dotenv
   import os

   # Környezeti változók betöltése a .env fájlból
   load_dotenv()

   # A Microsoft Foundry Models változók elérése
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ennyi az egész! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a Microsoft Foundry Models hitelesítő adataidat, és betöltötted őket a Python alkalmazásodba.

## Hogyan futtasd a kódot helyben a számítógépeden

A kód helyi futtatásához szükséged lesz valamilyen [Python verzió telepítésére](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ezután klónoznod kell a repót:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ha mindent letöltöttél, kezdődhet a munka!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python és néhány csomag telepítéséhez.
Maga a Conda egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Hasznos azoknak a csomagoknak a telepítéséhez is, amelyek nem érhetők el a `pip` segítségével.

Kövesd a [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) a beállításhoz.

Miniconda telepítése után klónozd a [repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ha még nem tetted meg)

Ezután létre kell hoznod egy virtuális környezetet. Erre Conda használatával hozz létre egy új környezeti fájlt (_environment.yml_). Ha Codespaces-t használsz, ezt a `.devcontainer` mappában hozd létre, tehát `.devcontainer/environment.yml`.

Töltsd fel a környezeti fájlt az alábbi részlettel:

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

Ha conda használata közben hibák jelentkeznek, manuálisan is telepítheted a Microsoft AI Könyvtárakat a következő terminál parancs segítségével.

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl meghatározza a szükséges függőségeket. A `<environment-name>` a Conda környezeted nevét jelenti, a `<python-version>` pedig a Python verzióját, például a `3` a Python legújabb fő verziója.

Ezzel elkészültél, most futtasd az alábbi parancsokat a parancssorban/terminálban a Conda környezet létrehozásához

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alútvonal csak a Codespace beállításokra vonatkozik
conda activate ai4beg
```

Ha problémáid vannak, nézd meg a [Conda környezetkezelési útmutatót](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata a Python támogatással

Ajánljuk a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztőt a [Python támogatás kiterjesztésével](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ehhez a tanfolyamhoz. Ez egy ajánlás, nem kötelező követelmény.

> **Megjegyzés**: Ha a tanfolyam repót megnyitod VS Code-ban, lehetőséged van a projekt konfigurálására konténeren belül is. Ez a tanfolyam repóban található különleges `.devcontainer` mappának köszönhető. Ennek részleteit később tárgyaljuk.

> **Megjegyzés**: Amint klónozod és megnyitod a repót VS Code-ban, automatikusan javasolni fogja egy Python támogatási kiterjesztés telepítését.

> **Megjegyzés**: Ha a VS Code egy konténerben való újranyitást javasol, utasítsd el, ha a helyi Python verziót szeretnéd használni.

### Jupyter használata a böngészőben

A projektet a [Jupyter környezetben](https://jupyter.org?WT.mc_id=academic-105485-koreyst) is fejlesztheted közvetlenül a böngészőből. A klasszikus Jupyter és a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) is kellemes fejlesztési környezetet kínál, például automatikus kiegészítéssel, kódszínezéssel stb.

Helyi Jupyter indításához lépj a terminál/parancssorba, navigálj a tanfolyam mappájába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindítja a Jupyter-t, a hozzáférési URL pedig megjelenik a parancssor ablakában.

Ha hozzáférsz az URL-hez, látnod kell a tanfolyam tartalomjegyzékét, és bármelyik `*.ipynb` fájl megnyitható, például `08-building-search-applications/python/oai-solution.ipynb`.

### Konténerben futtatás

A számítógépen vagy Codespace-ben való beállítás helyett használhatsz [konténert](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A tanfolyam repóban található `.devcontainer` mappának köszönhetően a VS Code képes a projektet konténerben felállítani. Codespaces-en kívül ez Docker telepítését igényli, és őszintén szólva, némi munkával jár, ezért csak tapasztalt konténerhasználóknak ajánljuk.

Az egyik legjobb módja az API kulcsaid biztonságos tárolásának GitHub Codespaces használata esetén a Codespace Secrets alkalmazása. Kérjük, kövesd a [Codespaces titokkezelés](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) útmutatót a további információkért.


## Leckék és technikai követelmények

A tanfolyam „Tanulj” leckékből áll, amelyek bemutatják a Generatív MI fogalmait, és „Építs” leckékből, amelyek kézzel fogható kódpéldákat tartalmaznak **Python** és **TypeScript** nyelveken, ahol csak lehetséges.

A kódolós leckéknél az Azure OpenAI szolgáltatást használjuk a Microsoft Foundry-ben. Szükséged lesz egy Azure előfizetésre és egy API kulcsra. Az elérés nyitott - nem kell engedélyt kérni -, ezért [hozz létre egy Microsoft Foundry erőforrást és telepíts egy modellt](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), hogy megkapd a végpontodat és kulcsodat.

Minden kódolós leckének van egy `README.md` fájlja is, ahol megtekintheted a kódot és az eredményeket anélkül, hogy futtatnál bármit.

## Az Azure OpenAI szolgáltatás első használata

Ha ez az első alkalom, hogy az Azure OpenAI szolgáltatást használod, kérjük, kövesd ezt az útmutatót, hogyan [hozz létre és telepíts egy Azure OpenAI szolgáltatás erőforrást.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Az OpenAI API első használata

Ha először használod az OpenAI API-t, kérjük, kövesd az útmutatót, hogyan [hozz létre és használj interfészt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Ismerkedj meg más tanulókkal

Létrehoztunk csatornákat a hivatalos [AI közösségi Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), hogy más tanulókkal találkozhass. Ez remek lehetőség, hogy kapcsolatokat építs más hasonló érdeklődésű vállalkozókkal, fejlesztőkkel, hallgatókkal, és bárkivel, aki fejlődni szeretne a Generatív MI terén.

[![Csatlakozz a discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata is jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Hozzájárulás

Ez a tanfolyam egy nyílt forráskódú kezdeményezés. Ha javítási javaslatod vagy hibajegyzésed van, kérjük, hozz létre egy [Pull Request-et](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst), vagy jelentkezz egy [GitHub hibával](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata nyomon követi az összes hozzájárulást. A nyílt forráskódú munkához való hozzájárulás kiváló lehetőség karriered építésére a Generatív MI területén.

A legtöbb hozzájáruláshoz szükség van arra, hogy elfogadd a Contributor License Agreement-et (CLA), amely igazolja, hogy jogod van hozzájárulásodat ilyen módon használni, és valóban megadod nekünk a használati jogokat. Részletekért látogass el a [CLA, Contributor License Agreement weboldalra](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: amikor ebben a repóban szöveget fordítasz, kérjük, ne használj gépi fordítást. A fordításokat a közösség ellenőrizni fogja, ezért csak olyan nyelven vállalj fordítást, amelyben jártas vagy.


Amikor benyújt egy pull requestet, egy CLA-bot automatikusan megállapítja, hogy szükséges-e CLA-t biztosítania, és ennek megfelelően díszíti a PR-t (például címke, megjegyzés). Egyszerűen kövesse a bot által adott utasításokat. Mindezt csak egyszer kell megtennie az összes CLA-t használó tároló esetén.

Ez a projekt elfogadta a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). További információkért olvassa el a Magatartási Kódex GYIK-jét, vagy vegye fel a kapcsolatot a [Email opencode](opencode@microsoft.com) címen bármilyen további kérdéssel vagy megjegyzéssel.

## Kezdjünk neki

Most, hogy elvégezte a szükséges lépéseket a kurzus befejezéséhez, kezdjük azzal, hogy megismerkedünk egy [bevezetővel a Generatív MI és a LLM-ek világába](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->