<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:03:33+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "sk"
}
-->
# Lokálne nastavenie 🖥️

**Použite tento návod, ak chcete všetko spúšťať na svojom vlastnom notebooku.**  
Máte dve možnosti: **(A) natívny Python + virtual-env** alebo **(B) VS Code Dev Container s Dockerom**.  
Vyberte si, čo vám viac vyhovuje—obe cesty vedú k rovnakým lekciám.

## 1.  Požiadavky

| Nástroj            | Verzia / Poznámky                                                                 |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (stiahnite z <https://python.org>)                                         |
| **Git**            | Najnovší (súčasť Xcode / Git for Windows / správca balíčkov v Linuxe)             |
| **VS Code**        | Voliteľné, ale odporúčané <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Len* pre možnosť B. Bezplatná inštalácia: <https://docs.docker.com/desktop/>     |

> 💡 **Tip** – Overte si nástroje v termináli:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnosť A – Natívny Python (najrýchlejšie)

### Krok 1  Naklonujte toto repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Krok 2 Vytvorte a aktivujte virtuálne prostredie

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Výzva v termináli by teraz mala začínať (.venv)—to znamená, že ste vo virtuálnom prostredí.

### Krok 3 Nainštalujte závislosti

```bash
pip install -r requirements.txt
```

Preskočte na časť 3 o [API kľúčoch](../../../00-course-setup)

## 2. Možnosť B – VS Code Dev Container (Docker)

Tento repozitár a kurz sme pripravili s [vývojovým kontajnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ktorý má univerzálne prostredie podporujúce Python3, .NET, Node.js aj Java vývoj. Súvisiaca konfigurácia je v súbore `devcontainer.json` v priečinku `.devcontainer/` v koreňovom adresári repozitára.

>**Prečo si vybrať toto?**
>Identické prostredie ako Codespaces; žiadne rozdiely v závislostiach.

### Krok 0 Nainštalujte doplnky

Docker Desktop – overte, že ```docker --version``` funguje.
VS Code Remote – Containers rozšírenie (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otvorte repo vo VS Code

Súbor ▸ Otvoriť priečinok…  → generative-ai-for-beginners

VS Code rozpozná .devcontainer/ a zobrazí výzvu.

### Krok 2 Otvorte v kontajneri

Kliknite na “Reopen in Container”. Docker vytvorí image (prvýkrát to trvá asi 3 minúty).
Keď sa objaví výzva v termináli, ste vo vnútri kontajnera.

## 2.  Možnosť C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je odľahčený inštalátor na inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíčkov.
Conda je správca balíčkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčkami. Hodí sa aj na inštaláciu balíčkov, ktoré nie sú dostupné cez `pip`.

### Krok 0  Inštalujte Miniconda

Postupujte podľa [návodu na inštaláciu MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Vytvorte virtuálne prostredie

Vytvorte nový súbor prostredia (*environment.yml*). Ak pracujete v Codespaces, vytvorte ho v priečinku `.devcontainer`, teda `.devcontainer/environment.yml`.

### Krok 2  Vyplňte súbor prostredia

Pridajte nasledujúci úryvok do svojho `environment.yml`

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

### Krok 3 Vytvorte Conda prostredie

Spustite nasledujúce príkazy v príkazovom riadku/termináli

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na prostredia Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnosť D – Klasický Jupyter / Jupyter Lab (vo vašom prehliadači)

> **Pre koho je to určené?**  
> Pre každého, kto má rád klasické rozhranie Jupyter alebo chce spúšťať notebooky bez VS Code.  

### Krok 1  Skontrolujte, či je Jupyter nainštalovaný

Na spustenie Jupyteru lokálne prejdite do terminálu/príkazového riadku, prejdite do priečinka s kurzom a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Tým sa spustí inštancia Jupyteru a v príkazovom riadku sa zobrazí URL na prístup.

Po otvorení tejto URL by ste mali vidieť osnovu kurzu a môžete prechádzať do ľubovoľného `*.ipynb` súboru. Napríklad `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Pridajte svoje API kľúče

Udržiavať svoje API kľúče v bezpečí je dôležité pri vývoji akýchkoľvek aplikácií. Odporúčame neukladať API kľúče priamo do kódu. Ak by ste ich omylom zverejnili v repozitári, mohlo by to viesť k bezpečnostným problémom a nechceným nákladom, ak by ich niekto zneužil.
Tu je postup, ako vytvoriť súbor `.env` pre Python a pridať `GITHUB_TOKEN`:

1. **Prejdite do priečinka projektu**: Otvorte terminál alebo príkazový riadok a prejdite do koreňového adresára projektu, kde chcete vytvoriť súbor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvorte súbor `.env`**: Použite svoj obľúbený textový editor na vytvorenie nového súboru s názvom `.env`. Ak používate príkazový riadok, môžete použiť `touch` (na Unix systémoch) alebo `echo` (na Windows):

   Unix systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++ alebo inom). Pridajte do súboru nasledujúci riadok, kde `your_github_token_here` nahraďte vaším skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte editor.

5. **Nainštalujte `python-dotenv`**: Ak ste ešte nenainštalovali, potrebujete balíček `python-dotenv`, ktorý načíta premenné prostredia zo súboru `.env` do vašej Python aplikácie. Nainštalujte ho cez `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Python skripte**: Vo vašom Python skripte použite balíček `python-dotenv` na načítanie premenných zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hotovo! Úspešne ste vytvorili súbor `.env`, pridali svoj GitHub token a načítali ho do Python aplikácie.

🔐 Nikdy nekomitujte .env—už je v .gitignore.
Kompletné inštrukcie k poskytovateľom nájdete v [`providers.md`](03-providers.md).

## 4. Čo ďalej?

| Chcem…              | Prejsť na…                                                                |
|---------------------|---------------------------------------------------------------------------|
| Začať lekciu 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Nastaviť LLM poskytovateľa | [`providers.md`](03-providers.md)                                 |
| Spoznajte ďalších študentov | [Pridajte sa na Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Riešenie problémov

| Príznak                                   | Riešenie                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Pridajte Python do PATH alebo reštartujte terminál po inštalácii|
| `pip` nevie vytvoriť wheels (Windows)     | `pip install --upgrade pip setuptools wheel` a skúste znova.    |
| `ModuleNotFoundError: dotenv`             | Spustite `pip install -r requirements.txt` (env nebol nainštalovaný).|
| Zlyhá Docker build *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → zvýšte veľkosť disku.|
| VS Code stále vyzýva na reopen            | Možno máte aktívne obe možnosti; vyberte jednu (venv **alebo** kontajner)|
| OpenAI 401 / 429 chyby                    | Skontrolujte hodnotu `OPENAI_API_KEY` / limity požiadaviek.     |
| Chyby pri používaní Conda                 | Inštalujte Microsoft AI knižnice cez `conda install -c microsoft azure-ai-ml`|

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho natívnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.