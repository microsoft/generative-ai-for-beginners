# Kezdés a tanfolyammal

Nagyon izgatottak vagyunk, hogy elkezdheted ezt a tanfolyamot, és meglátod, milyen inspiráló dolgokat építhetsz Generatív MI-vel!

A sikered érdekében ez az oldal összefoglalja a beállítási lépéseket, a technikai követelményeket, valamint, hogy hol kérhetsz segítséget, ha szükséges.

## Beállítási lépések

A tanfolyam megkezdéséhez el kell végezned az alábbi lépéseket.

### 1. Forkold ezt a tárat

[Forkold ezt a teljes tárat](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy módosíthasd a kódot és teljesíthesd a kihívásokat. Emellett [csillaggal is megjelölheted (🌟) ezt a tárat](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld ezt és a kapcsolódó tárakat.

### 2. Hozz létre egy codespace-t

Az esetleges függőségi problémák elkerülése érdekében javasoljuk, hogy a kurzust a [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) környezetben futtasd.

A forkodban: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/hu/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adj hozzá egy titkot

1. ⚙️ Fogaskerék ikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nevezd el OPENAI_API_KEY-nek, illeszd be a kulcsodat, Mentsd el.

### 3. Mi a következő?

| Szeretném…             | Ugrás ide…                                                              |
|-----------------------|------------------------------------------------------------------------|
| Elkezdni az 1. leckét  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline dolgozni       | [`setup-local.md`](02-setup-local.md)                                   |
| LLM szolgáltató beállítása | [`providers.md`](03-providers.md)                                        |
| Más tanulókkal találkozni | [Csatlakozás a Discord szerverünkhöz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Hibakeresés


| Tünet                                     | Javítás                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Konténer build több, mint 10 percig tart  | **Codespaces ➜ „Rebuild Container”**                             |
| `python: command not found`                | A terminál nem csatlakozott; kattints a **+** ➜ *bash*-ra       |
| `401 Unauthorized` az OpenAI-tól            | Hibás / lejárt `OPENAI_API_KEY`                                 |
| A VS Code „Dev container mounting…” üzenetet mutat | Frissítsd a böngészőfület — a Codespaces néha elveszti a kapcsolatot |
| Hiányzik a notebook kernel                 | Notebook menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++ vagy más szerkesztő). Add hozzá ezt a sort a fájlhoz, a `your_github_token_here` helyére a saját GitHub tokenedet illeszd be:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentsd el a fájlt**: Mentsd el a változtatásokat és zárd be a szerkesztőt.

5. **Telepítsd a `python-dotenv`-t**: Ha még nem telepítetted, szükséged lesz a `python-dotenv` csomagra, hogy a környezeti változókat betöltse a `.env` fájlból a Python alkalmazásodba. Telepítheted a `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Töltsd be a környezeti változókat a Python scriptedben**: A Python scriptedben használd a `python-dotenv` csomagot, hogy betöltsd a környezeti változókat a `.env` fájlból:

   ```python
   from dotenv import load_dotenv
   import os

   # Környezeti változók betöltése a .env fájlból
   load_dotenv()

   # A GITHUB_TOKEN változó elérése
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi az egész! Sikeresen létrehoztál egy `.env` fájlt, hozzáadtad a GitHub tokenedet, és betöltötted azt a Python alkalmazásodba.

## Hogyan futtassuk helyben a számítógépeden

A kód helyi futtatásához a gépeden szükséged lesz valamelyik [Python verzió telepítésére](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

A tár használatához klónoznod kell a repót:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Miután mindent lemásoltál, elkezdheted a munkát!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, valamint néhány csomag telepítéséhez.  
A Conda egy csomagkezelő, amely megkönnyíti különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok létrehozását és váltását. Emellett jól használható olyan csomagok telepítésére is, amelyek nem érhetők el a `pip`-pel.

Kövesd a [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) a telepítéshez.

A Miniconda telepítése után klónozd a [tárat](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ha még nem tetted meg).

Ezután létre kell hoznod egy virtuális környezetet. Ehhez Conda-val hozz létre egy új környezeti fájlt (_environment.yml_)-t. Ha Codespaces környezetben dolgozol, hozd létre a `.devcontainer` könyvtáron belül, azaz `.devcontainer/environment.yml`-ként.

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

Ha Conda használata közben hibákba ütközöl, manuálisan is telepítheted a Microsoft AI Könyvtárakat az alábbi terminálparancs használatával.

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl megadja a szükséges függőségeket. A `<environment-name>` a Conda környezeted neve, a `<python-version>` pedig a használandó Python verzió, például `3`, ami a legújabb főverzió.

Ha ezzel megvagy, hozz létre egy Conda környezetet az alábbi parancsok lefuttatásával a parancssorodban/terminálban:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alkönyvtár csak a Codespace beállításokra vonatkozik
conda activate ai4beg
```

Ha problémába ütköznél, keresd fel a [Conda környezetek kezelése útmutatót](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### A Visual Studio Code használata a Python támogatás kiterjesztéssel

Javasoljuk a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztő használatát a [Python támogatás kiterjesztéssel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ehhez a tanfolyamhoz. Ez azonban inkább ajánlás, nem kötelező követelmény.

> **Megjegyzés**: Amikor megnyitod a tanfolyam tárát VS Code-ban, lehetőséged van a projekt konténeren belüli beállítására. Ez a tanfolyam tárában található [speciális `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappának köszönhető. Ezzel később még foglalkozunk.

> **Megjegyzés**: Ha klónozod és megnyitod a könyvtárat VS Code-ban, automatikusan fel fogja ajánlani egy Python támogatás kiterjesztés telepítését.

> **Megjegyzés**: Ha a VS Code azt javasolja, hogy nyisd meg újra a repót konténerben, helyben telepített Python használatához ezt az ajánlatot utasítsd el.

### Jupyter használata böngészőben

A projektet a [Jupyter környezetben](https://jupyter.org?WT.mc_id=academic-105485-koreyst) is fejlesztheted közvetlenül a böngészőben. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kényelmes fejlesztési környezetet biztosít funkciókkal, mint az automatikus kiegészítés, szintaxiskiemelés stb.

A helyi Jupyter indításához nyisd meg a terminált/parancssort, navigálj a tanfolyam könyvtárába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter instance-t, és a hozzáférési URL-t megjeleníti a parancssor ablakában.

Az URL elérésével láthatod a tanfolyam vázlatát, és bármely `*.ipynb` fájlra navigálhatsz. Például az `08-building-search-applications/python/oai-solution.ipynb` fájlra.

### Konténerben futtatás

Alternatív megoldásként a számítógépen vagy Codespace-ben való telepítés helyett használhatsz egy [konténert](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A tanfolyam tárában található speciális `.devcontainer` mappa lehetővé teszi, hogy a VS Code konténerben állítsa be a projektet. Codespaces-en kívül ehhez Docker telepítése szükséges, és nem kevés előkészületet igényel, így ezt inkább azoknak ajánljuk, akik már rendelkeznek tapasztalattal konténerek használatában.

Az API kulcsok biztonságos kezelése érdekében GitHub Codespaces használatakor célszerű a Codespace Secrets funkciót alkalmazni. Ehhez kérjük, kövesd a [Codespaces titkok kezeléséről szóló útmutatót](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Leckék és technikai követelmények

A tanfolyam 6 elméleti és 6 kódolási leckéből áll.

A kódolási leckéknél az Azure OpenAI szolgáltatást használjuk. Ehhez szükséged lesz hozzáférésre az Azure OpenAI szolgáltatáshoz és egy API kulcsra. Hozzáférésért jelentkezhetsz a [jelentkezési űrlap kitöltésével](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Amíg a jelentkezésed feldolgozás alatt áll, a kódolási leckék mindegyike tartalmaz egy `README.md` fájlt, ahol meg tudod nézni a kódot és az eredményeket.

## Az Azure OpenAI szolgáltatás első használata

Ha először dolgozol az Azure OpenAI szolgáltatással, kövesd ezt az útmutatót arról, hogyan kell [létrehozni és telepíteni egy Azure OpenAI szolgáltatás erőforrást.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Az OpenAI API első használata

Ha először dolgozol az OpenAI API-val, kövesd az útmutatót, hogyan kell [létrehozni és használni a felületet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Találkozz más tanulókkal

A hivatalos [AI Community Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) létrehoztunk olyan csatornákat, ahol találkozhatsz más tanulókkal. Kiváló lehetőség arra, hogy kapcsolatokat építs hasonló gondolkodású vállalkozókkal, fejlesztőkkel, diákokkal és bárkivel, aki szeretne fejlődni Generatív MI területen.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata is jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Közreműködés

Ez a tanfolyam nyílt forráskódú kezdeményezés. Ha fejlesztési lehetőségeket vagy hibákat találsz, kérünk, hozz létre egy [Pull Request-et](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy jelents hibát a [GitHub Issues](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) oldalon.

A projekt csapata figyelemmel kíséri az összes hozzájárulást. A nyílt forráskódhoz való hozzájárulás kiváló lehetőség a karriered építésére Generatív MI területen.

A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement (CLA) megállapodást, melyben kijelented, hogy jogod van hozzájárulni, és valójában meg is adod nekünk a jogaidat a hozzájárulás használatára. Részletek a [CLA, Contributor License Agreement weboldalon](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: ha ebben a repóban szöveget fordítasz, kérjük, hogy ne használj gépi fordítást. A fordításokat a közösségen keresztül ellenőrizzük, ezért csak olyan nyelveken vállalj fordítást, amelyekben jártas vagy.

Pull request benyújtásakor egy CLA-bot automatikusan megállapítja, hogy szükséges-e CLA-t benyújtanod, és megfelelően ellátja a PR-t (pl. címkével, kommenttel). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned minden CLA-t használó repóban.

Ez a projekt a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) alkalmazza. További információért olvasd el a Magatartási Kódex GYIK-ot, vagy írj az [Email opencode](opencode@microsoft.com) címre további kérdésekkel vagy észrevételekkel.

## Kezdjünk neki!
Most, hogy befejezted a szükséges lépéseket a tanfolyam elvégzéséhez, kezdjük azzal, hogy megismerkedsz a [generatív MI-vel és a nagy nyelvi modellekkel](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén profi emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->