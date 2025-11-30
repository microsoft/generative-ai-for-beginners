<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:47:42+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "hu"
}
-->
# Helyi beállítás 🖥️

**Ezt az útmutatót akkor használd, ha mindent a saját laptopodon szeretnél futtatni.**  
Két lehetőséged van: **(A) natív Python + virtuális környezet** vagy **(B) VS Code Dev Container Dockerrel**.  
Válaszd azt, amelyik egyszerűbbnek tűnik—mindkettő ugyanazokra a leckékre vezet.

## 1. Előfeltételek

| Eszköz              | Verzió / Megjegyzés                                                                |
|---------------------|------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (letölthető innen: <https://python.org>)                                    |
| **Git**             | Legfrissebb (Xcode / Git for Windows / Linux csomagkezelő tartalmazza)             |
| **VS Code**         | Opcionális, de ajánlott <https://code.visualstudio.com>                            |
| **Docker Desktop**  | *Csak* a B opcióhoz. Ingyenes telepítés: <https://docs.docker.com/desktop/>        |

> 💡 **Tipp** – Ellenőrizd az eszközöket terminálban:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. A opció – Natív Python (leggyorsabb)

### 1. lépés  Klónozd ezt a repót

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2. lépés Hozz létre és aktiválj egy virtuális környezetet

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ A prompt most (.venv)-vel kezdődik—ez azt jelenti, hogy a környezeten belül vagy.

### 3. lépés Telepítsd a függőségeket

```bash
pip install -r requirements.txt
```

Ugorj a 3. szakaszra az [API kulcsoknál](../../../00-course-setup)

## 2. B opció – VS Code Dev Container (Docker)

Ezt a repót és kurzust egy [fejlesztői konténerrel](https://containers.dev?WT.mc_id=academic-105485-koreyst) állítottuk be, amely univerzális futtatókörnyezetet biztosít Python3, .NET, Node.js és Java fejlesztéshez. A kapcsolódó konfiguráció a `devcontainer.json` fájlban van definiálva, amely a `.devcontainer/` mappában található a repó gyökerében.

>**Miért válaszd ezt?**
>Ugyanaz a környezet, mint a Codespaces-ben; nincs függőségi eltérés.

### 0. lépés Telepítsd a kiegészítőket

Docker Desktop – ellenőrizd, hogy a ```docker --version``` működik.
VS Code Remote – Containers bővítmény (ID: ms-vscode-remote.remote-containers).

### 1. lépés Nyisd meg a repót VS Code-ban

Fájl ▸ Mappa megnyitása…  → generative-ai-for-beginners

A VS Code érzékeli a .devcontainer/-t és felugró ablakot jelenít meg.

### 2. lépés Újraindítás konténerben

Kattints a “Reopen in Container” gombra. A Docker felépíti a képet (≈ 3 perc első alkalommal).
Amikor megjelenik a terminál prompt, már a konténeren belül vagy.

## 2. C opció – Miniconda

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python és néhány csomag telepítéséhez.
A Conda egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Akkor is jól jön, ha olyan csomagot kell telepítened, ami `pip`-pel nem érhető el.

### 0. lépés  Telepítsd a Minicondát

Kövesd a [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) a beállításhoz.

```bash
conda --version
```

### 1. lépés Hozz létre virtuális környezetet

Hozz létre egy új környezetfájlt (*environment.yml*). Ha Codespaces-t használsz, ezt a `.devcontainer` könyvtárban hozd létre, tehát `.devcontainer/environment.yml`.

### 2. lépés  Töltsd fel a környezetfájlt

Add hozzá az alábbi kódrészletet az `environment.yml`-hez

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

### 3. lépés Hozd létre a Conda környezetet

Futtasd az alábbi parancsokat a parancssorban/terminálban

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ha problémába ütközöl, nézd meg a [Conda környezetek útmutatót](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. D opció – Klasszikus Jupyter / Jupyter Lab (böngészőben)

> **Kinek ajánlott?**  
> Akik szeretik a klasszikus Jupyter felületet, vagy jegyzetfüzeteket akarnak futtatni VS Code nélkül.  

### 1. lépés  Ellenőrizd, hogy a Jupyter telepítve van

A Jupyter helyi indításához nyisd meg a terminált/parancssort, navigálj a kurzus könyvtárába, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és a hozzáférési URL megjelenik a parancssor ablakban.

Az URL elérésével láthatod a kurzus felépítését, és navigálhatsz bármelyik `*.ipynb` fájlhoz. Például: `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Add hozzá az API kulcsaidat

Az API kulcsok biztonságos tárolása nagyon fontos bármilyen alkalmazás fejlesztésekor. Nem ajánljuk, hogy az API kulcsokat közvetlenül a kódban tárold. Ha ezeket nyilvános repóba töltöd fel, biztonsági problémákhoz és akár nem kívánt költségekhez is vezethet, ha illetéktelenek használják fel.
Íme egy lépésről-lépésre útmutató, hogyan hozhatsz létre `.env` fájlt Pythonhoz, és hogyan adhatod hozzá a `GITHUB_TOKEN`-t:

1. **Navigálj a projekt könyvtáradba**: Nyisd meg a terminált vagy parancssort, és lépj arra a könyvtárra, ahol a `.env` fájlt létre szeretnéd hozni.

   ```bash
   cd path/to/your/project
   ```

2. **Hozd létre a `.env` fájlt**: Használd a kedvenc szövegszerkesztődet egy új `.env` nevű fájl létrehozásához. Parancssorból `touch` (Unix-alapú rendszereken) vagy `echo` (Windows-on):

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++, vagy bármelyik másik). Írd be az alábbi sort, ahol a `your_github_token_here` helyére a saját GitHub tokenedet írd:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentsd el a fájlt**: Mentsd el a módosításokat, és zárd be a szerkesztőt.

5. **Telepítsd a `python-dotenv`-et**: Ha még nem tetted meg, telepítsd a `python-dotenv` csomagot, hogy a környezeti változókat a `.env` fájlból be tudd tölteni a Python alkalmazásodba. Telepítheted `pip`-pel:

   ```bash
   pip install python-dotenv
   ```

6. **Töltsd be a környezeti változókat a Python szkriptedben**: A Python szkriptedben a `python-dotenv` csomaggal töltheted be a `.env` fájlból a környezeti változókat:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a GitHub tokenedet, és betöltötted azt a Python alkalmazásodba.

🔐 Soha ne töltsd fel a .env fájlt—már benne van a .gitignore-ban.
A teljes szolgáltatói útmutató a [`providers.md`](03-providers.md) fájlban található.

## 4. Hogyan tovább?

| Ezt szeretném…      | Menj ide…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Első lecke indítása | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| LLM szolgáltató beállítása | [`providers.md`](03-providers.md)                                  |
| Találkozz más tanulókkal | [Csatlakozz a Discordhoz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Hibakeresés

| Tünet                                      | Megoldás                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| `python not found`                         | Add hozzá a Python-t a PATH-hoz, vagy indítsd újra a terminált  |
| `pip` nem tud kerekeket építeni (Windows)  | `pip install --upgrade pip setuptools wheel` majd próbáld újra. |
| `ModuleNotFoundError: dotenv`              | Futtasd: `pip install -r requirements.txt` (a környezet nem volt telepítve). |
| Docker build hibát ad *Nincs hely*         | Docker Desktop ▸ *Beállítások* ▸ *Erőforrások* → növeld a lemez méretét. |
| VS Code folyamatosan újranyitást kér       | Lehet, hogy mindkét opció aktív; válassz egyet (venv **vagy** konténer)|
| OpenAI 401 / 429 hibák                     | Ellenőrizd az `OPENAI_API_KEY` értékét / kérés limitet.         |
| Hibák Conda használatakor                  | Telepítsd a Microsoft AI könyvtárakat: `conda install -c microsoft azure-ai-ml`|

---

**Jogi nyilatkozat**:
Ez a dokumentum AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.