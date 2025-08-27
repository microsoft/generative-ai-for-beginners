<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:48:35+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hu"
}
-->
# A kurzus elkezdése

Nagyon örülünk, hogy elkezded ezt a kurzust, és kíváncsian várjuk, milyen ötleteket kapsz a Generatív MI segítségével!

Azért, hogy sikeresen haladj, ezen az oldalon összefoglaltuk a beállítási lépéseket, technikai követelményeket, és azt is, hol kérhetsz segítséget, ha szükséges.

## Beállítási lépések

A kurzus elkezdéséhez az alábbi lépéseket kell elvégezned.

### 1. Forkold ezt a repót

[Forkold ezt a teljes repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy módosíthasd a kódot és megoldhasd a kihívásokat. Emellett [csillagozhatod (🌟) is a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld ezt és a kapcsolódó repókat.

### 2. Hozz létre egy codespace-et

A függőségi problémák elkerülése érdekében javasoljuk, hogy a kurzust [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) környezetben futtasd.

A saját forkodban: **Code -> Codespaces -> New on main**

![Párbeszédablak, ahol codespace-et lehet létrehozni](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Titkos kulcs hozzáadása

1. ⚙️ Fogaskerék ikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nevezd el OPENAI_API_KEY-nek, illeszd be a kulcsodat, majd mentsd el.

### 3. Mi következik?

| Ezt szeretném…      | Menj ide…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Első lecke kezdése  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Offline munka       | [`setup-local.md`](02-setup-local.md)                                    |
| LLM szolgáltató beállítása | [`providers.md`](providers.md)                                   |
| Találkozni más tanulókkal | [Csatlakozz a Discordhoz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Hibakeresés

| Jelenség                                   | Megoldás                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| Konténer építése elakadt > 10 perc         | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                | A terminál nem csatlakozott; kattints a **+** ➜ *bash*          |
| `401 Unauthorized` az OpenAI-tól           | Hibás vagy lejárt `OPENAI_API_KEY`                              |
| VS Code “Dev container mounting…” üzenet   | Frissítsd a böngésző fület—Codespaces néha megszakítja a kapcsolatot |
| Notebook kernel hiányzik                   | Notebook menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++, vagy bármelyik másik). Add hozzá az alábbi sort, ahol a `your_github_token_here` helyére a saját GitHub tokenedet írd:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentsd el a fájlt**: Mentsd el a módosításokat és zárd be a szerkesztőt.

5. **Telepítsd a `python-dotenv` csomagot**: Ha még nincs telepítve, telepítsd a `python-dotenv` csomagot, hogy a környezeti változókat be tudd tölteni a `.env` fájlból a Python alkalmazásodba. Telepítés `pip`-pel:

   ```bash
   pip install python-dotenv
   ```

6. **Környezeti változók betöltése a Python szkriptben**: A Python szkriptedben a `python-dotenv` csomaggal töltsd be a `.env` fájlban lévő változókat:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Kész is! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a GitHub tokenedet, és betöltötted azt a Python alkalmazásodba.

## Hogyan futtasd helyben a gépeden

Ha helyben szeretnéd futtatni a kódot, szükséged lesz valamilyen [Python verzióra](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

A repó használatához először klónoznod kell:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ha mindent letöltöttél, már kezdheted is!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő, amivel [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python és néhány csomag telepíthető.
A Conda egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok kezelését. Akkor is jól jön, ha olyan csomagokat kell telepíteni, amelyek nem érhetők el `pip`-pel.

A [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) követve tudod beállítani.

Ha már telepítetted a Minicondát, klónozd a [repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ha még nem tetted meg).

Ezután hozz létre egy virtuális környezetet. Ehhez Condával készíts egy új környezeti fájlt (_environment.yml_). Ha Codespaces-t használsz, ezt a `.devcontainer` könyvtárban hozd létre, tehát `.devcontainer/environment.yml`.

Töltsd fel a környezeti fájlt az alábbi kódrészlettel:

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

Ha hibát kapsz a conda használatakor, manuálisan is telepítheted a Microsoft AI könyvtárakat az alábbi parancs segítségével a terminálban.

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl tartalmazza a szükséges függőségeket. Az `<environment-name>` a Conda környezeted neve, a `<python-version>` pedig a kívánt Python verzió, például `3` a legfrissebb főverzió.

Ha ezzel megvagy, a következő parancsokkal hozhatod létre a Conda környezetet a parancssorban/terminálban:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ha problémád adódik, nézd meg a [Conda környezetek útmutatóját](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata Python támogatással

Javasoljuk, hogy a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztőt használd a [Python támogatás bővítménnyel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ehhez a kurzushoz. Ez csak ajánlás, nem feltétlenül kötelező.

> **Note**: Ha megnyitod a kurzus repóját VS Code-ban, lehetőséged van konténerben beállítani a projektet. Ez a repóban található [speciális `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) könyvtárnak köszönhető. Erről később még lesz szó.

> **Note**: Ha klónozod és megnyitod a könyvtárat VS Code-ban, automatikusan felajánlja a Python támogatás bővítmény telepítését.

> **Note**: Ha a VS Code azt javasolja, hogy nyisd meg a repót konténerben, utasítsd el ezt, hogy a helyben telepített Python verziót használhasd.

### Jupyter használata böngészőben

A projekten dolgozhatsz [Jupyter környezetben](https://jupyter.org?WT.mc_id=academic-105485-koreyst) is, közvetlenül a böngészőből. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kényelmes fejlesztési környezetet nyújt automatikus kiegészítéssel, kódkiemeléssel stb.

A Jupyter helyi indításához nyisd meg a terminált/parancssort, navigálj a kurzus könyvtárába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindítja a Jupyter-t, és a hozzáférési URL megjelenik a parancssorban.

Ha megnyitod az URL-t, látni fogod a kurzus felépítését, és bármelyik `*.ipynb` fájlhoz navigálhatsz. Például: `08-building-search-applications/python/oai-solution.ipynb`.

### Futtatás konténerben

Alternatív megoldásként a projektet futtathatod [konténerben](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) is, akár a gépeden, akár Codespace-ben. A kurzus repójában található speciális `.devcontainer` mappa lehetővé teszi, hogy a VS Code konténerben állítsa be a projektet. Codespaces-en kívül ehhez Docker telepítése szükséges, és némi extra munka, ezért ezt inkább azoknak ajánljuk, akik már dolgoztak konténerekkel.

Az egyik legjobb módja annak, hogy az API kulcsaid biztonságban legyenek GitHub Codespaces használatakor, ha Codespace Secrets-et használsz. Erről bővebben a [Codespaces titkok kezelése](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) útmutatóban olvashatsz.


## Leckék és technikai követelmények

A kurzus 6 elméleti és 6 gyakorlati leckéből áll.

A gyakorlati leckékhez az Azure OpenAI Service-t használjuk. A kód futtatásához szükséged lesz hozzáférésre az Azure OpenAI szolgáltatáshoz és egy API kulcsra. Hozzáférést [ezen a jelentkezési űrlapon](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) kérhetsz.

Amíg vársz a jelentkezésed elbírálására, minden gyakorlati leckéhez tartozik egy `README.md` fájl, ahol megnézheted a kódot és a kimeneteket.

## Azure OpenAI Service első használata

Ha most dolgozol először az Azure OpenAI szolgáltatással, kövesd ezt az útmutatót, hogy [létrehozz és telepíts egy Azure OpenAI Service erőforrást.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API első használata

Ha most dolgozol először az OpenAI API-val, kövesd ezt az útmutatót, hogy [létrehozd és használd az interfészt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Találkozz más tanulókkal

Az [AI Community Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) külön csatornákat hoztunk létre, hogy találkozhass más tanulókkal. Ez remek lehetőség, hogy kapcsolatot építs hasonló gondolkodású vállalkozókkal, fejlesztőkkel, diákokkal, vagy bárkivel, aki szeretne fejlődni a Generatív MI területén.

[![Csatlakozz a Discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata is jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Közreműködés

Ez a kurzus nyílt forráskódú kezdeményezés. Ha javítanál valamin vagy hibát találsz, hozz létre egy [Pull Requestet](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy írj egy [GitHub hibajegyet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata minden hozzájárulást nyomon követ. A nyílt forráskódhoz való hozzájárulás nagyszerű lehetőség, hogy építsd a karriered a Generatív MI területén.

A legtöbb hozzájárulás esetén el kell fogadnod egy Contributor License Agreement-et (CLA), amelyben kijelented, hogy jogodban áll, és ténylegesen megadod nekünk a jogot a hozzájárulásod felhasználására. Részletekért látogasd meg a [CLA, Contributor License Agreement weboldalt](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: ha szöveget fordítasz ebben a repóban, kérjük, ne használj gépi fordítást. A fordításokat a közösség ellenőrzi, ezért csak olyan nyelvre vállalj fordítást, amelyben jártas vagy.

Ha beküldesz egy pull requestet, a CLA-bot automatikusan eldönti, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően megjelöli a PR-t (pl. címke, komment). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned minden repóban, amely a CLA-t használja.

Ez a projekt a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) szabályzatot követi. További információért olvasd el a Code of Conduct GYIK-et, vagy írj az [Email opencode](opencode@microsoft.com) címre, ha kérdésed vagy észrevételed van.

## Kezdjük el!
Most, hogy elvégezted a tanfolyamhoz szükséges lépéseket, kezdjük azzal, hogy megismerkedünk a [Generatív MI és a nagy nyelvi modellek alapjaival](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Jogi nyilatkozat**:
Ez a dokumentum AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.