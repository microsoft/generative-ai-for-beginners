# Helyi beállítás 🖥️

**Használd ezt az útmutatót, ha mindent a saját laptopodon szeretnél futtatni.**  
Két lehetőséged van: **(A) natív Python + virtual-env** vagy **(B) VS Code Dev Container Dockerrel**.  
Válaszd azt, amelyik könnyebbnek tűnik—mindkettő ugyanahhoz a tananyaghoz vezet.

## 1. Előfeltételek

| Eszköz             | Verzió / Megjegyzések                                                               |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10+ (letölthető innen: <https://python.org>)                                      |
| **Git**            | Legfrissebb (Xcode / Git Windowsra / Linux csomagkezelő részeként érhető el)         |
| **VS Code**        | Opcionális, de ajánlott <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Csak* a B opcióhoz. Ingyenes telepítés: <https://docs.docker.com/desktop/>         |

> 💡 **Tipp** – Ellenőrizd az eszközöket terminálban:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Opció A – Natív Python (leggyorsabb)

### 1. lépés Klónozd ezt a repót

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2. lépés Hozz létre és aktiválj egy virtuális környezetet

```bash
python -m venv .venv          # készíts egyet
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ A promptnak most (.venv)-vel kell kezdődnie — ez azt jelenti, hogy bent vagy a környezetben.

### 3. lépés Telepítsd a függőségeket

```bash
pip install -r requirements.txt
```

Ugorj a 3. szakaszra az [API kulcsok hozzáadása](../../../00-course-setup) részhez

## 2. Opció B – VS Code Dev Container (Docker)

Ezt a repót és tanfolyamot egy [fejlesztői konténerrel](https://containers.dev?WT.mc_id=academic-105485-koreyst) állítottuk be, amely egy univerzális futtatókörnyezetet biztosít Python3, .NET, Node.js és Java fejlesztéshez. A kapcsolódó konfiguráció a `devcontainer.json` fájlban található, a `.devcontainer/` mappában, a repó gyökerében.

>**Miért válaszd ezt?**  
>Ugyanaz a környezet, mint a Codespaces-ben; nincs függőségeltérés.

### 0. lépés Telepítsd a kiegészítőket

Docker Desktop – ellenőrizd, hogy a ```docker --version``` működik.  
VS Code Remote – Containers bővítmény (ID: ms-vscode-remote.remote-containers).

### 1. lépés Nyisd meg a repót VS Code-ban

File ▸ Open Folder…  → generative-ai-for-beginners

A VS Code észleli a .devcontainer/ mappát és felugrik egy ablak.

### 2. lépés Nyisd meg újra a konténerben

Kattints a „Reopen in Container” gombra. A Docker felépíti a képet (első alkalommal kb. 3 perc).  
Amikor megjelenik a terminál prompt, bent vagy a konténerben.

## 2. Opció C – Miniconda

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python és néhány csomag telepítéséhez.  
A Conda egy csomagkezelő, amely megkönnyíti különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok beállítását és váltását. Hasznos olyan csomagok telepítéséhez is, amelyek nem érhetők el `pip`-en keresztül.

### 0. lépés Telepítsd a Minicondát

Kövesd a [MiniConda telepítési útmutatót](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### 1. lépés Hozz létre egy virtuális környezetet

Hozz létre egy új környezeti fájlt (*environment.yml*). Ha Codespaces-t használsz, hozd létre a `.devcontainer` könyvtárban, tehát `.devcontainer/environment.yml` néven.

### 2. lépés Töltsd fel a környezeti fájlt

Add hozzá a következő részletet az `environment.yml` fájlhoz

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

### 3. lépés Hozd létre a Conda környezeted

Futtasd az alábbi parancsokat a parancssorban/terminálban

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # A .devcontainer alkönyvtár csak a Codespace beállításokra vonatkozik
conda activate ai4beg
```

Ha problémába ütközöl, nézd meg a [Conda környezetek útmutatóját](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. Opció D – Klasszikus Jupyter / Jupyter Lab (böngészőben)

> **Kinek ajánlott?**  
> Akik szeretik a klasszikus Jupyter felületet, vagy VS Code nélkül szeretnének notebookokat futtatni.

### 1. lépés Győződj meg róla, hogy a Jupyter telepítve van

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

## 3. Add hozzá az API kulcsaidat

Fontos, hogy az API kulcsaid biztonságban legyenek, amikor bármilyen alkalmazást építesz. Ajánlott, hogy ne tárold az API kulcsokat közvetlenül a kódban. Ha ezeket nyilvános repóba commitálod, az biztonsági problémákhoz és akár nem kívánt költségekhez is vezethet, ha rosszindulatú személy használja őket.  
Íme egy lépésről lépésre útmutató, hogyan hozz létre egy `.env` fájlt Pythonhoz és hogyan add hozzá a `GITHUB_TOKEN`-t:

1. **Navigálj a projekt könyvtáradba**: Nyisd meg a terminált vagy parancssort, és lépj be a projekt gyökérkönyvtárába, ahol létre szeretnéd hozni a `.env` fájlt.

   ```bash
   cd path/to/your/project
   ```

2. **Hozd létre a `.env` fájlt**: Használd a kedvenc szövegszerkesztődet egy új `.env` nevű fájl létrehozásához. Ha parancssort használsz, Unix-alapú rendszeren a `touch`, Windows-on az `echo` parancsot használhatod:

   Unix-alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt egy szövegszerkesztőben (pl. VS Code, Notepad++ vagy bármely más szerkesztő). Add hozzá a következő sort, a `your_github_token_here` helyére a saját GitHub tokenedet írva:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Mentsd el a fájlt**: Mentsd el a változtatásokat és zárd be a szerkesztőt.

5. **Telepítsd a `python-dotenv` csomagot**: Ha még nem tetted meg, telepítened kell a `python-dotenv` csomagot, hogy a `.env` fájlból betölthesd a környezeti változókat a Python alkalmazásodba. Telepítheted a `pip` segítségével:

   ```bash
   pip install python-dotenv
   ```

6. **Töltsd be a környezeti változókat a Python scriptedben**: A Python scriptedben használd a `python-dotenv` csomagot, hogy betöltsd a `.env` fájlban lévő környezeti változókat:

   ```python
   from dotenv import load_dotenv
   import os

   # Környezeti változók betöltése a .env fájlból
   load_dotenv()

   # A GITHUB_TOKEN változó elérése
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ennyi! Sikeresen létrehoztál egy `.env` fájlt, hozzáadtad a GitHub tokenedet, és betöltötted a Python alkalmazásodba.

🔐 Soha ne commitáld a .env fájlt — már benne van a .gitignore-ban.  
A szolgáltatók teljes útmutatói a [`providers.md`](03-providers.md) fájlban találhatók.

## 4. Mi a következő lépés?

| Mit szeretnék…       | Ugrás ide…                                                             |
|---------------------|------------------------------------------------------------------------|
| Kezdeni az 1. leckét | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Beállítani egy LLM szolgáltatót | [`providers.md`](03-providers.md)                              |
| Megismerni más tanulókat | [Csatlakozz a Discord szerverünkhöz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Hibakeresés

| Tünet                                    | Megoldás                                                        |
|------------------------------------------|----------------------------------------------------------------|
| `python not found`                       | Add hozzá a Pythont a PATH-hoz vagy nyisd meg újra a terminált telepítés után |
| `pip` nem tud kereket építeni (Windows) | Futtasd: `pip install --upgrade pip setuptools wheel`, majd próbáld újra. |
| `ModuleNotFoundError: dotenv`            | Futtasd: `pip install -r requirements.txt` (a környezet nem volt telepítve). |
| Docker build hibák *Nincs hely*           | Docker Desktop ▸ *Settings* ▸ *Resources* → növeld a lemezméretet. |
| VS Code folyton újranyitásra kér          | Lehet, hogy mindkét opció aktív; válassz egyet (venv **vagy** konténer) |
| OpenAI 401 / 429 hibák                   | Ellenőrizd az `OPENAI_API_KEY` értékét / kéréskorlátokat.       |
| Hibák Conda használatakor                | Telepítsd a Microsoft AI könyvtárakat: `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->