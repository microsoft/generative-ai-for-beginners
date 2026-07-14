# Helyi beállítás 🖥️

**Használd ezt az útmutatót, ha inkább a saját laptopodon futtatnád az egészet.**   
Két utad van: **(A) natív Python + virtual-env** vagy **(B) VS Code fejlesztői konténer Dockerrel**.  
Válaszd azt, amelyik könnyebbnek tűnik — mindkettő ugyanahhoz a leckéhez vezet.

## 1. Előfeltételek

| Eszköz            | Verzió / Megjegyzés                                                                |
|-------------------|------------------------------------------------------------------------------------|
| **Python**        | 3.10 + (letölthető innen: <https://python.org>)                                    |
| **Git**           | Legfrissebb (az Xcode / Git for Windows / Linux csomagkezelő részeként érkezik)    |
| **VS Code**       | Opcionális, de ajánlott <https://code.visualstudio.com>                             |
| **Docker Desktop**| *Csak* a B opcióhoz. Ingyenes telepítés: <https://docs.docker.com/desktop/>        |

> 💡 **Tipp** – Ellenőrizd az eszközöket terminálban:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. A lehetőség – A opción Native Python (leggyorsabb)

### 1. lépés  Klónozd ezt a repót

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2. lépés Hozz létre és aktiválj egy virtuális környezetet

```bash
python -m venv .venv          # csinálj egyet
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ A promptnak most (.venv)-nel kell kezdődnie — ez azt jelenti, hogy benne vagy a környezetben.

### 3. lépés Telepítsd a függőségeket

```bash
pip install -r requirements.txt
```

Ugorj a 3. szakaszhoz az [API kulcsok](#3-add-meg-az-api-kulcsaidat) részhez

## 2. B lehetőség – VS Code fejlesztői konténer (Docker)

Ezt a repót és kurzust egy [fejlesztői konténer](https://containers.dev?WT.mc_id=academic-105485-koreyst) segítségével állítottuk be, amely egy univerzális futtatókörnyezetet biztosít Python3, .NET, Node.js és Java fejlesztéshez. A vonatkozó konfiguráció a `devcontainer.json` fájlban van definiálva, ami a `.devcontainer/` mappában található, ezen repó gyökerében.

>**Miért válaszd ezt?**
>Ugyanaz a környezet, mint a Codespaces-ben; nincs függőségeltolódás.

### 0. lépés Telepítsd a kiegészítőket

Docker Desktop – győződj meg róla, hogy a ```docker --version``` működik.
VS Code Remote – Containers kiegészítő (ID: ms-vscode-remote.remote-containers).

### 1. lépés Nyisd meg a repót VS Code-ban

Fájl ▸ Mappa megnyitása…  → generative-ai-for-beginners

A VS Code érzékeli a .devcontainer/ mappát és felugró ablakot jelenít meg.

### 2. lépés Nyisd meg újra a konténerben

Kattints a „Reopen in Container” gombra. A Docker először összeállítja a képet (kb. 3 perc első alkalommal).
Amikor megjelenik a terminál prompt, már benne vagy a konténerben.

## 2. C lehetőség – Miniconda

A [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) egy könnyű telepítő a [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python és néhány csomag telepítéséhez.
A Conda maga egy csomagkezelő, amely megkönnyíti a különböző Python [**virtuális környezetek**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) és csomagok létrehozását és váltását. Hasznos lehet olyan csomagok telepítéséhez is, amelyek nem érhetőek el a `pip`-en keresztül.

### 0. lépés Telepítsd a Minicondát

Kövesd a [MiniConda telepítési útmutatóját](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### 1. lépés Hozz létre egy virtuális környezetet

Hozz létre egy új környezeti fájlt (*environment.yml*). Ha Codespaces-t használsz, hozd létre a `.devcontainer` mappán belül, azaz `.devcontainer/environment.yml` néven.

### 2. lépés Töltsd fel a környezeti fájlodat

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

### 3. lépés Hozd létre a Conda környezetedet

Futtasd a parancsokat a parancssorban/terminálban

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # A .devcontainer alútvonal csak a Codespace beállításokra vonatkozik
conda activate ai4beg
```

Hiba esetén lásd a [Conda környezetek útmutatóját](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. D lehetőség – Klasszikus Jupyter / Jupyter Lab (böngészőben)

> **Kinek való ez?**  
> Akinek a klasszikus Jupyter felület a kedvence, vagy aki nem szeretne VS Code-ot használni a jegyzetfüzetekhez.  

### 1. lépés Győződj meg róla, hogy Jupyter telepítve van

A helyi Jupyter indításához nyisd meg a terminált/parancssort, navigálj el a kurzus könyvtárához, és futtasd:

```bash
jupyter notebook
```

vagy

```bash
jupyterhub
```

Ez elindít egy Jupyter példányt, és a hozzáférési URL megjelenik a parancssor ablakában.

Amint megnyitod az URL-t, látnod kell a kurzus vázlatát, és bármelyik `*.ipynb` fájlra navigálhatsz, például `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Add meg az API kulcsaidat

Az API kulcsok biztonságos tárolása fontos bármilyen alkalmazás építésekor. Ajánlott, hogy ne tárold az API kulcsokat közvetlenül a kódodban. Ha publikus repóba kerülnek, az biztonsági gondokat és nem kívánt költségeket okozhat rosszindulatú használat esetén.
Íme egy lépésről lépésre útmutató, hogyan készíts `.env` fájlt Pythonhoz és hogyan add hozzá a Microsoft Foundry Models hitelesítő adataidat:

> **Megjegyzés:** A GitHub Models (és a `GITHUB_TOKEN` változó) 2026 július végén megszűnik. Ez az útmutató helyette a [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) használatát ajánlja. Ha teljesen offline szeretnél dolgozni, nézd meg a [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) megoldást.

1. **Navigálj a projekt könyvtáradba**: Nyisd meg a terminált vagy parancssort, és menj abba a mappába, ahol létre akarod hozni a `.env` fájlt.

   ```bash
   cd path/to/your/project
   ```

2. **Készítsd el a `.env` fájlt**: Használd kedvenc szövegszerkesztődet egy új `.env` nevű fájl létrehozásához. Parancssorban Unix rendszereken használhatod a `touch` parancsot, Windows-on az `echo`-t:

   Unix alapú rendszerek:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Szerkeszd a `.env` fájlt**: Nyisd meg a `.env` fájlt szövegszerkesztőben (pl. VS Code, Notepad++, vagy bármely más). Add hozzá az alábbi sorokat, a címkéket cseréld ki a saját Microsoft Foundry projekt végpontod és API kulcsodra:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Mentsd a fájlt**: Mentsd el a módosításokat és zárd be a szövegszerkesztőt.

5. **Telepítsd a `python-dotenv`-et**: Ha még nem tetted, telepítened kell a `python-dotenv` csomagot, hogy a környezeti változókat betölthesd a `.env` fájlból a Python alkalmazásodba. Telepítheted a `pip`-pel:

   ```bash
   pip install python-dotenv
   ```

6. **Töltsd be a környezeti változókat a Python scriptedben**: A Python scriptedben használd a `python-dotenv` csomagot a `.env` fájlban lévő környezeti változók betöltéséhez:

   ```python
   from dotenv import load_dotenv
   import os

   # Környezeti változók betöltése a .env fájlból
   load_dotenv()

   # Hozzáférés a Microsoft Foundry Models változóihoz
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ennyi! Sikeresen létrehoztad a `.env` fájlt, hozzáadtad a Microsoft Foundry Models hitelesítő adataidat, és betöltötted azokat a Python alkalmazásodba.

🔐 Soha ne küldd be a `.env` fájlt verziókezelőbe — már benne van a `.gitignore`-ban.
A szolgáltató részletes útmutatója megtalálható a [`providers.md`](03-providers.md) fájlban.

## 4. Mi a következő lépés?

| Szeretném…           | Ugrás ide…                                                               |
|----------------------|-------------------------------------------------------------------------|
| Kezdeni az 1. leckét  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Beállítani egy LLM szolgáltatót | [`providers.md`](03-providers.md)                               |
| Megismerni más tanulókat | [Csatlakozz a Discord szerverünkhöz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Hibakeresés

| Tünet                                    | Megoldás                                                        |
|------------------------------------------|----------------------------------------------------------------|
| `python nem található`                     | Add hozzá a Pythont a PATH változóhoz, vagy indítsd újra a terminált telepítés után |
| `pip` nem tud kereket építeni (Windows)   | Futtasd: `pip install --upgrade pip setuptools wheel`, majd próbáld újra.           |
| `ModuleNotFoundError: dotenv`              | Futtasd a `pip install -r requirements.txt` parancsot (nincs telepítve az env).    |
| Docker build hibák *Nincs hely*             | Docker Desktop ▸ *Beállítások* ▸ *Erőforrások* → növeld a lemezméretet.           |
| A VS Code folyamatosan újbóli megnyitásra kér | Lehet, hogy mindkét opció aktív; válassz egyet (venv **vagy** konténer)            |
| OpenAI 401 / 429 hibák                      | Ellenőrizd az `OPENAI_API_KEY` értéket / a lekérések sebességét.                   |
| Problémák Conda használatakor              | Telepítsd a Microsoft AI könyvtárakat a `conda install -c microsoft azure-ai-ml` parancsal |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->