<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T21:26:29+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hu"
}
-->
# A kurzus kezdete

Nagyon izgatottak vagyunk, hogy elkezded ezt a kurzust, és kíváncsian várjuk, milyen inspirációt merítesz a Generatív Mesterséges Intelligenciával való építkezéshez!

A sikered érdekében ezen az oldalon bemutatjuk a beállítási lépéseket, technikai követelményeket, és azt, hogy hol kaphatsz segítséget, ha szükséged van rá.

## Beállítási lépések

A kurzus elkezdéséhez az alábbi lépéseket kell elvégezned.

### 1. Forkold ezt a repót

[Forkold az egész repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy módosíthasd a kódot és teljesíthesd a kihívásokat. Ezen kívül [csillagozhatod (🌟) ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld ezt és a kapcsolódó repókat.

### 2. Hozz létre egy Codespace-t

Annak érdekében, hogy elkerüld a függőségi problémákat a kód futtatása során, javasoljuk, hogy a kurzust [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) környezetben futtasd.

A forkodban: **Code -> Codespaces -> New on main**

![Párbeszédablak, amely a Codespace létrehozás gombjait mutatja](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adj hozzá egy titkot

1. ⚙️ Fogaskerék ikon -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nevezd el OPENAI_API_KEY-nek, illeszd be a kulcsodat, majd mentsd el.

### 3. Mi következik?

| Ezt szeretném…      | Menj ide…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Az 1. leckét elkezdeni | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline dolgozni    | [`setup-local.md`](02-setup-local.md)                                   |
| LLM szolgáltatót beállítani | [`providers.md`](03-providers.md)                                        |
| Más tanulókkal találkozni | [Csatlakozz a Discordunkhoz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Hibakeresés

| Tünet                                    | Megoldás                                                        |
|------------------------------------------|-----------------------------------------------------------------|
| Konténer építése > 10 percig tart        | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | A terminál nem csatlakozott; kattints **+** ➜ *bash*            |
| `401 Unauthorized` az OpenAI-tól         | Hibás / lejárt `OPENAI_API_KEY`                                 |
| VS Code “Dev container mounting…” üzenetet mutat | Frissítsd a böngésző lapot—Codespaces néha elveszíti a kapcsolatot |
| Notebook kernel hiányzik                 | Notebook menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++ vagy bármely más szerkesztő). Add hozzá a következő sort a fájlhoz, cseréld ki `your_github_token_here`-t a tényleges GitHub tokenedre:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentsd el a fájlt**: Mentsd el a változtatásokat, és zárd be a szövegszerkesztőt.

5. **Telepítsd a `python-dotenv`-et**: Ha még nem tetted meg, telepítened kell a `python-dotenv` csomagot, hogy a `.env` fájlból betöltsd a környezeti változókat a Python alkalmazásodba. Telepítheted `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Környezeti változók betöltése a Python szkriptedbe**: A Python szkriptedben használd a `python-dotenv` csomagot, hogy betöltsd a környezeti változókat a `.env` fájlból:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi! Sikeresen létrehoztál egy `.env` fájlt, hozzáadtad a GitHub tokenedet, és betöltötted azt a Python alkalmazásodba.

## Hogyan futtassuk helyben a számítógépen

Ahhoz, hogy helyben futtathasd a kódot a számítógépeden, szükséged lesz valamilyen [Python verzióra](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ezután a repót klónoznod kell:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Miután mindent letöltöttél, kezdheted is!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, valamint néhány csomag telepítéséhez. Maga a Conda egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Hasznos lehet olyan csomagok telepítéséhez is, amelyek nem érhetők el `pip` segítségével.

Kövesd a [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) a beállításhoz.

Miután telepítetted a Minicondát, klónozd a [repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ha még nem tetted meg).

Ezután létre kell hoznod egy virtuális környezetet. Ehhez a Conda segítségével hozz létre egy új környezetfájlt (_environment.yml_). Ha Codespaces-t használsz, hozd létre ezt a `.devcontainer` könyvtárban, tehát `.devcontainer/environment.yml`.

Töltsd ki a környezetfájlt az alábbi kódrészlettel:

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

Ha hibákat tapasztalsz a Conda használata során, manuálisan is telepítheted a Microsoft AI könyvtárakat az alábbi parancs segítségével a terminálban.

```
conda install -c microsoft azure-ai-ml
```

A környezetfájl meghatározza a szükséges függőségeket. `<environment-name>` a Conda környezeted nevére utal, míg `<python-version>` a Python verziójára, például `3` a legújabb főverzió.

Ha ezzel megvagy, létrehozhatod a Conda környezetedet az alábbi parancsok futtatásával a parancssorban/terminálban:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ha problémákba ütközöl, nézd meg a [Conda környezetek útmutatót](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata Python támogatással

Javasoljuk, hogy a kurzushoz használd a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztőt a [Python támogatás bővítménnyel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Ez azonban inkább ajánlás, nem kötelező követelmény.

> **Megjegyzés**: Ha megnyitod a kurzus repóját a VS Code-ban, lehetőséged van a projektet konténerben beállítani. Ez a kurzus repójában található [speciális `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) könyvtárnak köszönhető. Erről később bővebben.

> **Megjegyzés**: Ha klónozod és megnyitod a könyvtárat a VS Code-ban, automatikusan javasolni fogja a Python támogatás bővítmény telepítését.

> **Megjegyzés**: Ha a VS Code azt javasolja, hogy nyisd meg a repót egy konténerben, utasítsd vissza ezt a kérést, hogy a helyileg telepített Python verziót használhasd.

### Jupyter használata a böngészőben

A projekten dolgozhatsz a [Jupyter környezetben](https://jupyter.org?WT.mc_id=academic-105485-koreyst) közvetlenül a böngésződben. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kellemes fejlesztési környezetet biztosít olyan funkciókkal, mint az automatikus kiegészítés, kódkiemelés stb.

A Jupyter helyi indításához menj a terminálba/parancssorba, navigálj a kurzus könyvtárába, és hajtsd végre:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és az URL, amelyen elérheted, megjelenik a parancssor ablakában.

Miután elérted az URL-t, látnod kell a kurzus vázlatát, és navigálhatsz bármely `*.ipynb` fájlhoz. Például: `08-building-search-applications/python/oai-solution.ipynb`.

### Konténerben futtatás

Alternatívája annak, hogy mindent a számítógépen vagy Codespace-ben állíts be, az, hogy [konténert](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) használsz. A kurzus repójában található speciális `.devcontainer` mappa lehetővé teszi, hogy a VS Code konténerben állítsa be a projektet. Codespaces-en kívül ez a Docker telepítését igényli, és őszintén szólva, ez némi munkát igényel, így ezt csak azoknak ajánljuk, akik tapasztaltak a konténerekkel való munkában.

Az egyik legjobb módja annak, hogy az API kulcsaidat biztonságban tartsd a GitHub Codespaces használata során, az a Codespace Secrets használata. Kérjük, kövesd a [Codespaces titkok kezelésére vonatkozó útmutatót](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), hogy többet megtudj erről.

## Leckék és technikai követelmények

A kurzus 6 koncepcióleckét és 6 kódolási leckét tartalmaz.

A kódolási leckékhez az Azure OpenAI szolgáltatást használjuk. Szükséged lesz hozzáférésre az Azure OpenAI szolgáltatáshoz és egy API kulcsra, hogy futtathasd a kódot. Hozzáférésért [töltsd ki ezt a jelentkezést](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Amíg vársz a jelentkezésed feldolgozására, minden kódolási lecke tartalmaz egy `README.md` fájlt, ahol megtekintheted a kódot és az eredményeket.

## Az Azure OpenAI szolgáltatás első használata

Ha először dolgozol az Azure OpenAI szolgáltatással, kövesd ezt az útmutatót arról, hogyan [hozz létre és telepíts egy Azure OpenAI Service erőforrást.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Az OpenAI API első használata

Ha először dolgozol az OpenAI API-val, kövesd az útmutatót arról, hogyan [hozz létre és használd az interfészt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Találkozz más tanulókkal

Létrehoztunk csatornákat a hivatalos [AI Community Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), hogy találkozhass más tanulókkal. Ez egy remek lehetőség arra, hogy kapcsolatot építs más hasonló gondolkodású vállalkozókkal, építőkkel, diákokkal, és bárkivel, aki szeretne fejlődni a Generatív AI területén.

[![Csatlakozz a Discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata szintén elérhető lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Hozzájárulás

Ez a kurzus egy nyílt forráskódú kezdeményezés. Ha javítási lehetőségeket vagy problémákat észlelsz, hozz létre egy [Pull Requestet](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy jelentkezz egy [GitHub problémával](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata nyomon követi az összes hozzájárulást. A nyílt forráskódhoz való hozzájárulás csodálatos módja annak, hogy karriert építs a Generatív AI területén.

A legtöbb hozzájárulás megköveteli, hogy elfogadj egy Hozzájárulói Licencszerződést (CLA), amely kijelenti, hogy jogod van és ténylegesen megadod nekünk a jogokat a hozzájárulásod használatához. Részletekért látogass el a [CLA, Contributor License Agreement weboldalra](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: amikor szöveget fordítasz ebben a repóban, győződj meg róla, hogy nem használsz gépi fordítást. A fordításokat a közösség ellenőrzi, ezért csak olyan nyelveken vállalj fordítást, amelyeken jártas vagy.

Amikor benyújtasz egy pull requestet, egy CLA-bot automatikusan meghatározza, hogy szükséges-e CLA-t biztosítanod, és megfelelően megjelöli a PR-t (pl. címke, megjegyzés). Egyszerűen kövesd a bot által adott utasításokat. Ezt csak egyszer kell megtenned minden olyan repó esetében, amely a CLA-t használja.

Ez a projekt elfogadta a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) irányelveit. További információért olvasd el a Code of Conduct GYIK-et, vagy lépj kapcsolatba [Email opencode](opencode@microsoft.com) címen bármilyen további kérdéssel vagy megjegyzéssel.

## Kezdjük el!
Most, hogy elvégezted a szükséges lépéseket a kurzus befejezéséhez, kezdjük azzal, hogy megismerkedünk a [Generatív AI-val és LLM-ekkel](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.