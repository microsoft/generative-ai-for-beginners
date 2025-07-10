<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:15:27+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hu"
}
-->
# Kezdés ezzel a tanfolyammal

Nagyon izgatottak vagyunk, hogy elkezded ezt a tanfolyamot, és meglátod, milyen inspiráló dolgokat hozhatsz létre a Generatív MI segítségével!

A sikered érdekében ezen az oldalon összefoglaltuk a beállítási lépéseket, a technikai követelményeket, valamint azt, hogy hol kérhetsz segítséget, ha szükséges.

## Beállítási lépések

A tanfolyam elkezdéséhez a következő lépéseket kell elvégezned.

### 1. Forkold ezt a repót

[Forkold le az egész repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy módosíthasd a kódot és teljesíthesd a kihívásokat. Emellett [csillagozhatod (🌟) is ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld ezt és a kapcsolódó repókat.

### 2. Hozz létre egy codespace-t

A függőségi problémák elkerülése érdekében javasoljuk, hogy a tanfolyamot [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) környezetben futtasd.

Ezt úgy hozhatod létre, hogy a forkolt repódnál kiválasztod a `Code` opciót, majd a **Codespaces** lehetőséget.

![Dialógus, amely a codespace létrehozására szolgáló gombokat mutatja](../../../00-course-setup/images/who-will-pay.webp)

### 3. API kulcsok tárolása

Fontos, hogy az API kulcsaidat biztonságban tartsd, amikor bármilyen alkalmazást fejlesztesz. Nem ajánljuk, hogy az API kulcsokat közvetlenül a kódban tárold. Ha ezeket nyilvános repóba commitálod, az biztonsági problémákhoz és akár nem kívánt költségekhez is vezethet, ha rosszindulatú személy használja fel őket.
Íme egy lépésről lépésre útmutató, hogyan készíts `.env` fájlt Pythonhoz, és hogyan add hozzá a `GITHUB_TOKEN`-t:

1. **Navigálj a projekt könyvtáradba**: Nyisd meg a terminált vagy parancssort, és lépj be a projekt gyökérkönyvtárába, ahol létre szeretnéd hozni a `.env` fájlt.

   ```bash
   cd path/to/your/project
   ```

2. **Hozd létre a `.env` fájlt**: Használd a kedvenc szövegszerkesztődet egy új `.env` nevű fájl létrehozásához. Parancssorból Unix-alapú rendszereken a `touch`, Windows-on az `echo` parancs használható:

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++, vagy bármely más szerkesztő). Add hozzá a következő sort, a `your_github_token_here` helyére a saját GitHub tokenedet írva:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentés**: Mentsd el a fájlt és zárd be a szerkesztőt.

5. **Telepítsd a `python-dotenv` csomagot**: Ha még nem tetted meg, telepítened kell a `python-dotenv` csomagot, hogy a `.env` fájlban tárolt környezeti változókat be tudd tölteni a Python alkalmazásodba. Telepítheted a `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Környezeti változók betöltése a Python szkriptben**: A Python szkriptedben használd a `python-dotenv` csomagot a `.env` fájlban lévő környezeti változók betöltéséhez:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi az egész! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a GitHub tokenedet, és betöltötted azt a Python alkalmazásodba.

## Hogyan futtasd helyben a számítógépeden

Ahhoz, hogy helyben futtasd a kódot a számítógépeden, szükséged lesz valamilyen [Python verzió telepítésére](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ezután a repót le kell klónoznod:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Miután mindent letöltöttél, kezdődhet a munka!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python és néhány csomag telepítéséhez.
A Conda egy csomagkezelő, amely megkönnyíti különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Hasznos lehet olyan csomagok telepítéséhez is, amelyek nem érhetők el `pip`-en keresztül.

Kövesd a [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) a beállításhoz.

Miután telepítetted a Minicondát, klónozd le a [repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ha még nem tetted meg).

Ezután létre kell hoznod egy virtuális környezetet. Conda használatával készíts egy új környezeti fájlt (_environment.yml_). Ha Codespaces-t használsz, ezt a `.devcontainer` könyvtárban hozd létre, tehát `.devcontainer/environment.yml`.

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

Ha Conda használata közben hibákba ütközöl, manuálisan is telepítheted a Microsoft AI könyvtárakat a következő parancs futtatásával a terminálban:

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl tartalmazza a szükséges függőségeket. Az `<environment-name>` a Conda környezeted nevét jelöli, az `<python-version>` pedig a Python verzióját, például a `3` a legfrissebb főverzió.

Ezek után hozd létre a Conda környezetet az alábbi parancsok futtatásával a parancssorban/terminálban:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ha problémákba ütközöl, nézd meg a [Conda környezetek útmutatóját](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata a Python támogatás kiterjesztéssel

Javasoljuk, hogy a tanfolyamhoz a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztőt használd a [Python támogatás kiterjesztéssel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Ez azonban inkább ajánlás, nem kötelező követelmény.

> **Megjegyzés**: Ha megnyitod a tanfolyam repóját VS Code-ban, lehetőséged van a projektet konténerben futtatni. Ennek oka a repóban található [különleges `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappa. Erről később még szó lesz.

> **Megjegyzés**: Amint klónozod és megnyitod a könyvtárat VS Code-ban, automatikusan felajánlja a Python támogatás kiterjesztés telepítését.

> **Megjegyzés**: Ha a VS Code azt javasolja, hogy nyisd meg újra a repót konténerben, utasítsd el ezt a kérést, ha a helyileg telepített Python verziót szeretnéd használni.

### Jupyter használata böngészőben

A projektet a [Jupyter környezetben](https://jupyter.org?WT.mc_id=academic-105485-koreyst) is fejlesztheted közvetlenül a böngésződben. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kellemes fejlesztői környezetet biztosít, például automatikus kiegészítéssel, kódszínezéssel stb.

A Jupyter helyi indításához nyisd meg a terminált/parancssort, navigálj a tanfolyam könyvtárába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és a hozzáférési URL megjelenik a parancssor ablakában.

Ha megnyitod az URL-t, látnod kell a tanfolyam vázlatát, és navigálhatsz bármely `*.ipynb` fájlhoz. Például: `08-building-search-applications/python/oai-solution.ipynb`.

### Futtatás konténerben

Alternatív megoldásként a számítógépen vagy Codespace-ben való beállítás helyett használhatsz egy [konténert](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A tanfolyam repójában található különleges `.devcontainer` mappa lehetővé teszi, hogy a VS Code konténerben állítsa be a projektet. Codespaces-en kívül ehhez Docker telepítése szükséges, és őszintén szólva, ez egy kicsit bonyolultabb, ezért ezt csak azoknak ajánljuk, akik már jártasak a konténerek használatában.

Az API kulcsaid biztonságának megőrzésének egyik legjobb módja GitHub Codespaces használata esetén a Codespace Secrets alkalmazása. Kérjük, kövesd a [Codespaces titkok kezeléséről szóló útmutatót](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) a részletekért.

## Tananyagok és technikai követelmények

A tanfolyam 6 elméleti és 6 gyakorlati leckéből áll.

A gyakorlati leckékhez az Azure OpenAI szolgáltatást használjuk. Ehhez hozzáférésre és API kulcsra lesz szükséged. Hozzáférést az [ezen az űrlapon keresztül](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) igényelhetsz.

Amíg az igénylésed feldolgozás alatt áll, minden gyakorlati leckéhez tartozik egy `README.md` fájl, ahol megtekintheted a kódot és az eredményeket.

## Azure OpenAI szolgáltatás első használata

Ha most használod először az Azure OpenAI szolgáltatást, kérjük, kövesd ezt az útmutatót az [Azure OpenAI szolgáltatás létrehozásához és telepítéséhez.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API első használata

Ha most használod először az OpenAI API-t, kérjük, kövesd az útmutatót az [API létrehozásához és használatához.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Ismerkedj meg más tanulókkal

Hivatalos [AI Community Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) létrehoztunk csatornákat, ahol találkozhatsz más tanulókkal. Ez remek lehetőség, hogy kapcsolatokat építs hasonló gondolkodású vállalkozókkal, fejlesztőkkel, diákokkal, és bárkivel, aki szeretne fejlődni a Generatív MI területén.

[![Csatlakozás a discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata is jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Hozzájárulás

Ez a tanfolyam egy nyílt forráskódú kezdeményezés. Ha javítási javaslatod vagy hibát találsz, kérjük, hozz létre egy [Pull Request-et](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy jelentkezz egy [GitHub issue-val](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata nyomon követi az összes hozzájárulást. A nyílt forráskódú projektekhez való hozzájárulás nagyszerű módja a karriered építésének a Generatív MI területén.

A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement-et (CLA), amelyben kijelented, hogy jogod van a hozzájárulásod használatára, és valóban megadod ezt a jogot. Részletekért látogass el a [CLA, Contributor License Agreement weboldalra](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: amikor szöveget fordítasz ebben a repóban, kérjük, ne használj gépi fordítást. A fordításokat a közösség ellenőrzi, ezért csak olyan nyelveken vállalj fordítást, amelyben jártas vagy.

Amikor pull request-et nyújtasz be, egy CLA-bot automatikusan megállapítja, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően jelöli meg a PR-t (pl. címke, komment). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned az összes CLA-t használó repóban.

Ez a projekt elfogadta a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) irányelveit. További információért olvasd el a Code of Conduct GYIK-et, vagy írj az [opencode@microsoft.com](mailto:opencode@microsoft.com) címre kérdéseiddel vagy észrevételeiddel.

## Kezdjünk hozzá

Most, hogy elvégezted a tanfolyam teljesítéséhez szükséges lépéseket, kezdjük azzal, hogy megismerkedsz a [Generatív MI és a nagy nyelvi modellek (LLM-ek) alapjaival](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.