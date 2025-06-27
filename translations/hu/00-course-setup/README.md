<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:57:30+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hu"
}
-->
# A kurzus elkezdése

Nagyon izgatottak vagyunk, hogy elkezdheted ezt a kurzust, és meglátod, milyen inspirációt kapsz az Generatív MI-vel való építéshez!

A sikered érdekében ezen az oldalon vázoljuk a beállítási lépéseket, a technikai követelményeket, és azt, hogy hol kaphatsz segítséget, ha szükséges.

## Beállítási lépések

A kurzus elkezdéséhez a következő lépéseket kell végrehajtanod.

### 1. Villázd ezt a repót

[Villázd az egész repót](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a saját GitHub fiókodba, hogy képes legyél bármilyen kódot megváltoztatni és teljesíteni a kihívásokat. Szintén [csillagozhatod (🌟) ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), hogy könnyebben megtaláld és más kapcsolódó repókat.

### 2. Hozz létre egy kódteret

Annak érdekében, hogy elkerüld a függőségi problémákat a kód futtatása során, javasoljuk, hogy futtasd ezt a kurzust egy [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) környezetben.

Ezt úgy hozhatod létre, hogy a villázott verziódban kiválasztod a `Code` opciót, majd a **Codespaces** lehetőséget.

![Párbeszédablak, amely a kódterek létrehozásához szükséges gombokat mutatja](../../../00-course-setup/images/who-will-pay.webp)

### 3. Az API kulcsok tárolása

Fontos, hogy az API kulcsokat biztonságban tartsd bármilyen alkalmazás építésekor. Javasoljuk, hogy ne tárold az API kulcsokat közvetlenül a kódban. Ha ezeket az adatokat nyilvános repóban közzéteszed, az biztonsági problémákhoz és akár nem kívánt költségekhez is vezethet, ha rossz szándékú személyek használják fel őket.
Íme egy lépésről-lépésre útmutató arról, hogyan hozhatsz létre egy `.env` fájlt Pythonhoz, és hogyan adhatod hozzá a `GITHUB_TOKEN`-t:

1. **Navigálj a projekt könyvtáradba**: Nyisd meg a terminált vagy a parancssort, és navigálj a projekted gyökérkönyvtárába, ahol létre szeretnéd hozni a `.env` fájlt.

   ```bash
   cd path/to/your/project
   ```

2. **Hozd létre a `.env` fájlt**: Használj egy tetszőleges szövegszerkesztőt egy új fájl létrehozásához, amelynek neve `.env`. Ha parancssort használsz, a `touch` (on Unix-based systems) or `echo` parancsot használhatod (Windows esetén):

   Unix alapú rendszerek:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++, vagy bármely más szerkesztő). Add hozzá a következő sort a fájlhoz, kicserélve a `your_github_token_here` részt a tényleges GitHub tokenedre:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentés**: Mentsd el a változtatásokat, és zárd be a szövegszerkesztőt.

5. **Telepítsd a `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` csomagot, hogy betölthesd a környezeti változókat a `.env` fájlból a Python alkalmazásodba. Telepítheted a `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Környezeti változók betöltése a Python szkriptedbe**: A Python szkriptedben használd a `python-dotenv` csomagot, hogy betölthesd a környezeti változókat a `.env` fájlból:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi! Sikeresen létrehoztál egy `.env` fájlt, hozzáadtad a GitHub tokened, és betöltötted a Python alkalmazásodba.

## Helyi futtatás a számítógépeden

Ahhoz, hogy a kódot helyben futtasd a számítógépeden, szükséged lesz valamilyen verzióra a [Python telepítéséből](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ezután a repót klónoznod kell:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Miután mindent ellenőriztél, elkezdheted!

## Opcionális lépések

### Miniconda telepítése

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), a Python, valamint néhány csomag telepítéséhez.
A Conda maga egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Hasznos lehet olyan csomagok telepítéséhez is, amelyek nem érhetők el a `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` segítségével.

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

Ha hibákba ütközöl a conda használata során, manuálisan is telepítheted a Microsoft AI könyvtárakat az alábbi parancs segítségével a terminálban.

```
conda install -c microsoft azure-ai-ml
```

A környezeti fájl meghatározza a szükséges függőségeket. Az `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` a Python legújabb főverziója.

Ha ez kész, létrehozhatod a Conda környezeted az alábbi parancsok futtatásával a parancssorban/terminálban

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ha problémákba ütközöl, tekintsd meg a [Conda környezetek útmutatót](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code használata a Python támogatási bővítménnyel

Javasoljuk a [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) szerkesztő használatát a [Python támogatási bővítménnyel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) telepítve ehhez a kurzushoz. Ez azonban inkább egy ajánlás, és nem kötelező követelmény.

> **Megjegyzés**: Ha megnyitod a kurzus repóját a VS Code-ban, lehetőséged van beállítani a projektet egy konténerben. Ennek oka a [speciális `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) könyvtár, amely a kurzus repójában található. Erről később bővebben.

> **Megjegyzés**: Amint klónozod és megnyitod a könyvtárat a VS Code-ban, az automatikusan javasolni fogja egy Python támogatási bővítmény telepítését.

> **Megjegyzés**: Ha a VS Code javasolja, hogy nyisd meg újra a repót egy konténerben, utasítsd vissza ezt a kérést, hogy a helyileg telepített Python verziót használhasd.

### Jupyter használata a böngészőben

A projektet a [Jupyter környezet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) használatával is megmunkálhatod közvetlenül a böngésződben. Mind a klasszikus Jupyter, mind a [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) kellemes fejlesztési környezetet biztosít olyan funkciókkal, mint az automatikus kiegészítés, kódkiemelés stb.

A Jupyter helyi indításához menj a terminálra/parancssorra, navigálj a kurzus könyvtárába, és hajtsd végre:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és a hozzáférési URL-t megjeleníti a parancssor ablakában.

Amint hozzáférsz az URL-hez, látnod kell a kurzus vázlatát, és navigálhatsz bármely `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` fájlra, ahol megtekintheted a kódot és a kimeneteket.

## Az Azure OpenAI szolgáltatás első használata

Ha ez az első alkalom, hogy az Azure OpenAI szolgáltatással dolgozol, kérjük, kövesd ezt az útmutatót arról, hogyan [hozhatsz létre és telepíthetsz egy Azure OpenAI szolgáltatás erőforrást.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Az OpenAI API első használata

Ha ez az első alkalom, hogy az OpenAI API-val dolgozol, kérjük, kövesd az útmutatót arról, hogyan [hozhatsz létre és használhatsz egy interfészt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Találkozz más tanulókkal

Létrehoztunk csatornákat a hivatalos [AI Community Discord szerverünkön](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) a többi tanulóval való találkozásra. Ez egy nagyszerű módja annak, hogy kapcsolatot építs más hasonló gondolkodású vállalkozókkal, építőkkel, diákokkal, és bárkivel, aki szeretne fejlődni a Generatív MI területén.

[![Csatlakozz a discord csatornához](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A projekt csapata szintén jelen lesz ezen a Discord szerveren, hogy segítsen a tanulóknak.

## Közreműködés

Ez a kurzus egy nyílt forráskódú kezdeményezés. Ha javítási lehetőségeket vagy problémákat látsz, kérjük, hozz létre egy [Pull Request-et](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) vagy logolj egy [GitHub problémát](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A projekt csapata nyomon követi az összes közreműködést. A nyílt forráskódú hozzájárulás nagyszerű módja a karrierépítésnek a Generatív MI területén.

A legtöbb hozzájárulás esetén meg kell egyeznie egy Közreműködői Licencszerződésben (CLA), amely kijelenti, hogy jogod van a hozzájárulásod felhasználására, és ténylegesen megadod nekünk a jogot, hogy felhasználjuk azt. Részletekért látogass el a [CLA, Közreműködői Licencszerződés weboldalra](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Fontos: amikor szöveget fordítasz ebben a repóban, kérjük, ügyelj arra, hogy ne használj gépi fordítást. A fordításokat a közösség ellenőrzi, ezért kérjük, csak olyan nyelvek fordítására jelentkezz, amelyeket folyékonyan beszélsz.

Amikor benyújtasz egy pull requestet, egy CLA-bot automatikusan megállapítja, hogy szükséges-e egy CLA-t biztosítanod, és ennek megfelelően díszíti a PR-t (pl. címke, megjegyzés). Egyszerűen kövesd a bot által adott utasításokat. Ezt csak egyszer kell megtenned az összes repóban, amely a CLA-nkat használja.

Ez a projekt a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) fogadta el. További információért olvasd el a Magatartási Kódex GYIK-et, vagy lépj kapcsolatba az [Email opencode](opencode@microsoft.com) címen bármilyen további kérdéssel vagy észrevétellel.

## Kezdjünk neki

Most, hogy elvégezted a szükséges lépéseket a kurzus teljesítéséhez, kezdjük el az [Generatív MI és LLM-ek bevezetésével](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén ajánlott a professzionális emberi fordítás. Nem vállalunk felelősséget semmilyen félreértésért vagy félremagyarázásért, amely a fordítás használatából ered.