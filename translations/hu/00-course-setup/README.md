<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:34:36+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hu"
}
-->
# Kezdés ezzel a kurzussal

Nagyon izgatottak vagyunk, hogy elkezded ezt a kurzust, és látjuk, mi mindent inspirál téged az építésre a Generatív MI-vel!

A sikered érdekében ez az oldal felvázolja a beállítási lépéseket, a technikai követelményeket, és hogy hol kérhetsz segítséget, ha szükséges.

## Beállítási lépések

A kurzus megkezdéséhez a következő lépéseket kell végrehajtanod.

### 1. Forkold ezt a repót

[Forkold az egész repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy megváltoztathasd a kódot és teljesíthesd a kihívásokat. Emellett [csillagozhatod (🌟) is ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld ezt és a kapcsolódó repókat.

### 2. Hozz létre egy codespace-t

A kódfuttatás közbeni függőségi problémák elkerülése érdekében javasoljuk, hogy ezt a kurzust [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) használatával futtasd.

Ez létrehozható, ha a forkolt repódban kiválasztod a `Code` opciót, majd a **Codespaces** lehetőséget.

![Párbeszédablak, amely a codespace létrehozásához szükséges gombokat mutatja](../../../00-course-setup/images/who-will-pay.webp)

### 3. API kulcsok tárolása

Az API kulcsok biztonságos tárolása fontos bármilyen alkalmazás építésekor. Javasoljuk, hogy ne tárold közvetlenül a kódodban az API kulcsokat. Ha ezeket az adatokat egy nyilvános repóba kötelezed, az biztonsági problémákat okozhat, és nem kívánt költségeket is eredményezhet, ha egy rosszindulatú szereplő használja fel őket.
Íme egy lépésről-lépésre útmutató, hogyan hozz létre egy `.env` fájlt Pythonhoz és add hozzá a `GITHUB_TOKEN`:

1. **Navigálj a projekt könyvtáradba**: Nyisd meg a terminálodat vagy a parancssort, és navigálj a projekt gyökérkönyvtárába, ahol létre szeretnéd hozni a `.env` fájlt.

   ```bash
   cd path/to/your/project
   ```

2. **Hozd létre a `.env` fájlt**: Használd a kedvenc szövegszerkesztődet egy új fájl létrehozásához, amelynek neve `.env`. Ha a parancssort használod, használhatod a `touch` (on Unix-based systems) or `echo` parancsot (Windows-on):

   Unix-alapú rendszerek:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++ vagy bármely más szerkesztő). Add hozzá a következő sort a fájlhoz, cserélve a `your_github_token_here` értéket a saját GitHub tokenedre:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentés**: Mentsd el a változtatásokat és zárd be a szövegszerkesztőt.

5. **Telepítsd a `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` csomagot, hogy betöltsd a környezeti változókat a `.env` fájlból a Python alkalmazásodba. Telepítheted a `pip` használatával:

   ```bash
   pip install python-dotenv
   ```

6. **Környezeti változók betöltése a Python szkriptedben**: A Python szkriptedben használd a `python-dotenv` csomagot, hogy betöltsd a környezeti változókat a `.env` fájlból:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a GitHub tokened, és betöltötted a Python alkalmazásodba.

## Hogyan futtasd helyileg a számítógépeden

Ahhoz, hogy a kódot helyileg futtasd a számítógépeden, szükséged lesz valamilyen verzióra a [Python telepítve](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ezután, hogy használd a repót, klónoznod kell azt:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ha mindent ellenőriztél, kezdheted is!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), a Python, valamint néhány csomag telepítésére.
A Conda maga egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Emellett hasznos lehet olyan csomagok telepítésére, amelyek nem érhetők el `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` által.

Töltsd fel a környezeti fájlodat az alábbi kódrészlettel:

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

Ha hibákat tapasztalsz a conda használata során, manuálisan is telepítheted a Microsoft AI Könyvtárakat a következő parancs használatával a terminálban.

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl meghatározza a szükséges függőségeket. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` a Python legújabb fő verziója.

Ezek után létrehozhatod a Conda környezeted az alábbi parancsok futtatásával a parancssorban/terminálban

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ha problémákba ütközöl, tekintsd meg a [Conda környezetek útmutatót](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata a Python támogatási bővítménnyel

Javasoljuk a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztő használatát a [Python támogatási bővítménnyel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) telepítve ehhez a kurzushoz. Ez azonban inkább ajánlás, nem pedig kötelező követelmény.

> **Megjegyzés**: Ha megnyitod a kurzus repóját a VS Code-ban, lehetőséged van a projekt beállítására egy konténeren belül. Ez a kurzus repójában található [különleges `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) könyvtár miatt van. Erről később bővebben.

> **Megjegyzés**: Miután klónoztad és megnyitottad a könyvtárat a VS Code-ban, automatikusan javasolni fogja, hogy telepíts egy Python támogatási bővítményt.

> **Megjegyzés**: Ha a VS Code javasolja, hogy nyisd meg a repót egy konténerben, utasítsd el ezt a kérést, hogy a helyileg telepített Python verziót használd.

### Jupyter használata a böngészőben

A projektet a [Jupyter környezet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) használatával is dolgozhatod a böngésződben. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kellemes fejlesztési környezetet biztosít olyan funkciókkal, mint az automatikus kiegészítés, kódkiemelés stb.

A Jupyter helyi indításához nyisd meg a terminált/parancssort, navigálj a kurzus könyvtárába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és a hozzáférési URL megjelenik a parancssor ablakában.

Miután hozzáférsz az URL-hez, látnod kell a kurzus felépítését, és navigálhatsz bármely `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` fájlhoz, ahol megtekintheted a kódot és a kimeneteket.

## Az Azure OpenAI Szolgáltatás első használata

Ha ez az első alkalom, hogy az Azure OpenAI szolgáltatással dolgozol, kérjük, kövesd ezt az útmutatót az [Azure OpenAI Szolgáltatás erőforrás létrehozásához és telepítéséhez.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Az OpenAI API első használata

Ha ez az első alkalom, hogy az OpenAI API-val dolgozol, kérjük, kövesd az útmutatót az [Interfész létrehozásához és használatához.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Találkozz más tanulókkal

Létrehoztunk csatornákat a hivatalos [AI Közösségi Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) más tanulókkal való találkozásra. Ez nagyszerű módja annak, hogy kapcsolatba lépj más hasonló gondolkodású vállalkozókkal, építőkkel, diákokkal, és bárkivel, aki szeretné fejleszteni a tudását a Generatív MI területén.

[![Csatlakozz a Discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata szintén jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Hozzájárulás

Ez a kurzus egy nyílt forráskódú kezdeményezés. Ha látsz javítandó területeket vagy problémákat, kérjük, hozz létre egy [Pull Requestet](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy jelents egy [GitHub problémát](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata követni fogja az összes hozzájárulást. A nyílt forráskódhoz való hozzájárulás nagyszerű módja annak, hogy építsd a karriered a Generatív MI területén.

A legtöbb hozzájárulás megköveteli, hogy elfogadj egy Hozzájárulói Licencszerződést (CLA), amely kijelenti, hogy jogod van és ténylegesen megadod nekünk a jogot a hozzájárulásod használatára. Részletekért látogasd meg a [CLA, Hozzájárulói Licencszerződés weboldalt](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: amikor fordítást végzel ebben a repóban, kérjük, biztosítsd, hogy ne használj gépi fordítást. A fordításokat a közösség fogja ellenőrizni, ezért kérjük, csak olyan nyelvekre vállalkozz, amelyekben jártas vagy.

Amikor beküldesz egy pull requestet, egy CLA-bot automatikusan meghatározza, hogy szükséges-e CLA-t biztosítanod, és ennek megfelelően megjelöli a PR-t (pl. címke, megjegyzés). Egyszerűen kövesd a bot által adott utasításokat. Ezt csak egyszer kell megtenned az összes repó esetében, amely a CLA-t használja.

Ez a projekt a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) fogadta el. További információkért olvasd el a Magatartási Kódex GYIK-ját vagy lépj kapcsolatba az [Email opencode](opencode@microsoft.com) címre bármilyen további kérdéssel vagy megjegyzéssel.

## Kezdjük el

Most, hogy elvégezted a szükséges lépéseket a kurzus teljesítéséhez, kezdjük el egy [bevezetővel a Generatív MI-ről és LLM-ekről](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Felelősség kizárása**:  
Ezt a dokumentumot az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.