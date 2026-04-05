# Lokálne nastavenie 🖥️

**Použite tento návod, ak uprednostňujete spúšťať všetko na vlastnom notebooku.**  
Máte dve možnosti: **(A) natívny Python + virtual-env** alebo **(B) VS Code Dev Container s Dockerom**.  
Vyberte si, čo vám príde jednoduchšie – obe vedú k rovnakým lekciám.

## 1.  Požiadavky

| Nástroj            | Verzia / Poznámky                                                                    |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (stiahnite z <https://python.org>)                                            |
| **Git**            | Najnovšia (súčasť Xcode / Git pre Windows / správca balíkov Linuxu)                   |
| **VS Code**        | Voliteľné, ale odporúčané <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Iba* pre možnosť B. Bezplatná inštalácia: <https://docs.docker.com/desktop/>        |

> 💡 **Tip** – Overte nástroje v termináli:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnosť A – Natívny Python (najrýchlejšie)

### Krok 1  Naklonujte tento repozitár

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Krok 2 Vytvorte a aktivujte virtuálne prostredie

```bash
python -m venv .venv          # vytvoriť jeden
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Príkazový riadok by mal teraz začínať na (.venv)—to znamená, že ste vo vnútri prostredia.

### Krok 3 Nainštalujte závislosti

```bash
pip install -r requirements.txt
```

Preskočte na Sekciu 3 o [API kľúčoch](../../../00-course-setup)

## 2. Možnosť B – VS Code Dev Container (Docker)

Tento repozitár a kurz sme nastavili s [vývojovým kontajnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ktorý má univerzálne runtime prostredie podporujúce Python3, .NET, Node.js a Java vývoj. Súvisiaca konfigurácia je definovaná v súbore `devcontainer.json` umiestnenom v priečinku `.devcontainer/` v koreňovom adresári tohto repozitára.

>**Prečo si vybrať toto?**  
>Identické prostredie ako Codespaces; žiadne problémy s nezhodou závislostí.

### Krok 0 Nainštalujte doplnky

Docker Desktop – overte, že príkaz ```docker --version``` funguje.  
VS Code Remote – Containers rozšírenie (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otvorte repozitár vo VS Code

Súbor ▸ Otvoriť priečinok… → generative-ai-for-beginners

VS Code detekuje .devcontainer/ a zobrazí výzvu.

### Krok 2 Znova otvorte v kontajneri

Kliknite na „Reopen in Container“. Docker zostaví obraz (≈ 3 minúty pri prvom spustení).  
Keď sa zobrazí príkazový riadok, ste vo vnútri kontajnera.

## 2.  Možnosť C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíkov.  
Conda je správca balíkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Tiež je užitočný na inštaláciu balíkov, ktoré nie sú dostupné cez `pip`.

### Krok 0  Nainštalujte Miniconda

Postupujte podľa [návodu na inštaláciu MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Vytvorte virtuálne prostredie

Vytvorte nový súbor prostredia (*environment.yml*). Ak používate Codespaces, vytvorte ho v priečinku `.devcontainer`, teda `.devcontainer/environment.yml`.

### Krok 2  Naplňte súbor prostredia

Pridajte nasledujúci úryvok do vášho `environment.yml`

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

### Krok 3 Vytvorte svoje Conda prostredie

Spustite nasledujúce príkazy v príkazovom riadku/termináli

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podcesta .devcontainer sa vzťahuje iba na nastavenia Codespace
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na správu Conda prostredí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnosť D – Klasický Jupyter / Jupyter Lab (vo vašom prehliadači)

> **Pre koho je to určené?**  
> Pre každého, kto má rád klasické rozhranie Jupyter alebo chce spúšťať notebooky bez VS Code.

### Krok 1  Overte, či je Jupyter nainštalovaný

Na spustenie Jupyter lokálne otvorte terminál/príkazový riadok, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Tým sa spustí inštancia Jupyter a URL na prístup k nej sa zobrazí v okne príkazového riadku.

Po prístupe na URL by ste mali vidieť osnovu kurzu a môžete prechádzať do ľubovoľného súboru `*.ipynb`. Napríklad, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Pridajte svoje API kľúče

Je dôležité bezpečne uchovávať svoje API kľúče pri tvorbe akejkoľvek aplikácie. Odporúčame neukladať API kľúče priamo v kóde. Ich zverejnenie v repozitári by mohlo viesť k bezpečnostným problémom a neželaným nákladom, ak by ich zneužil niekto iný.  
Tu je krok za krokom návod, ako vytvoriť `.env` súbor pre Python a pridať `GITHUB_TOKEN`:

1. **Prejdite do adresára svojho projektu**: Otvorte terminál alebo príkazový riadok a prejdite do koreňového adresára projektu, kde chcete vytvoriť `.env` súbor.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvorte `.env` súbor**: Použite svoj obľúbený textový editor na vytvorenie nového súboru s názvom `.env`. Ak používate príkazový riadok, môžete použiť `touch` (na Unixových systémoch) alebo `echo` (na Windows):

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte `.env` súbor**: Otvorte `.env` súbor v textovom editore (napr. VS Code, Notepad++ alebo inom editore). Pridajte nasledujúci riadok, pričom `your_github_token_here` nahraďte vaším skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte `python-dotenv`**: Ak ste tak ešte neurobili, nainštalujte balík `python-dotenv`, ktorý načíta premenné prostredia zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načítať premenné prostredia zo súboru .env
   load_dotenv()

   # Prístup k premennej GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hotovo! Úspešne ste vytvorili `.env` súbor, pridali GitHub token a načítali ho do vašej Python aplikácie.

🔐 Nikdy necommitujte `.env` – je už v `.gitignore`.  
Úplné pokyny poskytovateľa nájdete v [`providers.md`](03-providers.md).

## 4. Čo ďalej?

| Chcem…              | Ísť na…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Začať Lekciu 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nastaviť poskytovateľa LLM | [`providers.md`](03-providers.md)                                       |
| Spoznajte ostatných študentov | [Pridajte sa na náš Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Riešenie problémov

| Príznak                                   | Riešenie                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Pridajte Python do PATH alebo znova otvorte terminál po inštalácii |
| `pip` nemôže zostaviť wheels (Windows)   | `pip install --upgrade pip setuptools wheel` a skúste znova.    |
| `ModuleNotFoundError: dotenv`             | Spustite `pip install -r requirements.txt` (prostredie nebolo nainštalované). |
| Docker build zlyhá *No space left*        | Docker Desktop ▸ *Nastavenia* ▸ *Zdroje* → zväčšite veľkosť disku. |
| VS Code stále vyzýva na znovuotvorenie    | Môžete mať aktívne obe možnosti; vyberte jednu (venv **alebo** kontajner) |
| OpenAI 401 / 429 chyby                     | Skontrolujte hodnotu `OPENAI_API_KEY` / limity požiadaviek.      |
| Chyby pri používaní Conda                  | Nainštalujte Microsoft AI knižnice pomocou `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->