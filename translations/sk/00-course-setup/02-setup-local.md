# Miestne nastavenie 🖥️

**Použite tento návod, ak dávate prednosť spusteniu všetkého na vlastnom notebooku.**   
Máte dve možnosti: **(A) natívny Python + virtual-env** alebo **(B) VS Code Dev Container s Dockerom**.  
Vyberte si, čo vám príde jednoduchšie—obe vedú k rovnakým lekciám.

## 1.  Požiadavky

| Nástroj            | Verzia / Poznámky                                                                  |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10+ (stiahnite z <https://python.org>)                                          |
| **Git**            | Najnovšia (súčasť Xcode / Git pre Windows / balíček správcu Linuxu)                |
| **VS Code**        | Voliteľný, ale odporúčaný <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Len* pre možnosť B. Bezplatná inštalácia: <https://docs.docker.com/desktop/>     |

> 💡 **Tip** – Overte nástroje v termináli:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnosť A – natívny Python (najrýchlejšie)

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

✅ Výzva by teraz mala začínať na (.venv)—to znamená, že ste vo vnútri prostredia.

### Krok 3 Nainštalujte závislosti

```bash
pip install -r requirements.txt
```

Preskočte na Sekciu 3 o [API kľúčoch](#3-pridajte-svoje-api-kľúče)

## 2. Možnosť B – VS Code Dev Container (Docker)

Tento repozitár a kurz sme nastavili s [development containerom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ktorý má univerzálne prostredie podporujúce Python3, .NET, Node.js a Java vývoj. Súvisiaca konfigurácia je definovaná v súbore `devcontainer.json` v priečinku `.devcontainer/` v koreňovom adresári tohto repozitára.

>**Prečo si to vybrať?**
>Identické prostredie ako Codespaces; žiadne posuny v závislostiach.

### Krok 0 Inštalujte dodatočné nástroje

Docker Desktop – overte, že príkaz ```docker --version``` funguje.
Rozšírenie VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otvorte repozitár vo VS Code

Súbor ▸ Otvoriť priečinok…  → generative-ai-for-beginners

VS Code rozpozná `.devcontainer/` a zobrazí výzvu.

### Krok 2 Otvorte znova v konteineri

Kliknite na „Reopen in Container“. Docker najprv zostaví obraz (≈ 3 min pri prvom spustení).
Keď sa objaví výzva v termináli, ste vo vnútri kontajnera.

## 2.  Možnosť C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor pre inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu, ako aj niekoľkých balíčkov.
Conda je správca balíčkov, ktorý uľahčuje vytváranie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčkami. Je tiež užitočný pri inštalácii balíčkov, ktoré nie sú dostupné cez `pip`.

### Krok 0  Nainštalujte Miniconda

Postupujte podľa [návodu na inštaláciu MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Vytvorte virtuálne prostredie

Vytvorte nový súbor pre prostredie (*environment.yml*). Ak používate Codespaces, vytvorte ho v priečinku `.devcontainer`, teda `.devcontainer/environment.yml`.

### Krok 2  Naplňte váš environment file

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

Spustite nižšie uvedené príkazy v termináli/príkazovom riadku

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podcesta .devcontainer sa vzťahuje iba na nastavenia Codespace
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na správu Conda prostredí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnosť D – Klasický Jupyter / Jupyter Lab (vo vašom prehliadači)

> **Pre koho je to určené?**  
> Pre všetkých, ktorí milujú klasické rozhranie Jupyter alebo chcú spustiť notebooky bez VS Code.  

### Krok 1  Uistite sa, že máte nainštalovaný Jupyter

Pre spustenie Jupyter lokálne otvorte terminál/príkazový riadok, prejdite do adresára kurzu a vykonajte:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Spustí sa inštancia Jupyter a URL na prístup k nej sa zobrazí v okne terminálu.

Po prístupe na URL by ste mali vidieť osnovu kurzu a môžete prechádzať k ľubovoľnému súboru `*.ipynb`. Napríklad, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Pridajte svoje API kľúče

Je dôležité udržiavať vaše API kľúče bezpečné pri tvorbe akejkoľvek aplikácie. Odporúčame neukladať žiadne API kľúče priamo v kóde. Uloženie týchto údajov do verejného repozitára by mohlo viesť k bezpečnostným problémom a dokonca neželaným nákladom, ak by ich zneužil niekto s zlým úmyslom.
Tu je krok za krokom návod, ako vytvoriť `.env` súbor pre Python a pridať svoje prihlasovacie údaje pre Microsoft Foundry Models:

> **Poznámka:** GitHub Models (a jeho premenná `GITHUB_TOKEN`) budú ukončené koncom júla 2026. Tento návod používa namiesto toho [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Preferujete prácu úplne offline? Pozrite sa na [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Prejdite do adresára svojho projektu**: Otvorte terminál alebo príkazový riadok a prejdite do koreňového adresára projektu, kde chcete vytvoriť `.env` súbor.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvorte `.env` súbor**: Použite preferovaný textový editor na vytvorenie nového súboru s názvom `.env`. Ak používate príkazový riadok, môžete použiť `touch` (na Unixových systémoch) alebo `echo` (na Windows):

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte `.env` súbor**: Otvorte `.env` súbor v textovom editore (napr. VS Code, Notepad++ alebo akýkoľvek iný editor). Pridajte do súboru nasledujúce riadky a nahraďte zástupné hodnoty vaším skutočným koncovým bodom projektu Microsoft Foundry a API kľúčom:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte `python-dotenv`**: Ak ste tak ešte neurobili, budete potrebovať nainštalovať balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env` do vášho Python skriptu. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načítajte premenné prostredia zo súboru .env
   load_dotenv()

   # Prístup k premenným Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je všetko! Úspešne ste vytvorili `.env` súbor, pridali svoje prihlasovacie údaje Microsoft Foundry Models a načítali ich vo vašej Python aplikácii.

🔐 Nikdy necommitujte `.env`—je už v `.gitignore`.
Kompletné pokyny poskytovateľa nájdete v [`providers.md`](03-providers.md).

## 4. Čo ďalej?

| Chcem…              | Ísť na…                                                                |
|---------------------|------------------------------------------------------------------------|
| Začať Lekciu 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nastaviť poskytovateľa LLM | [`providers.md`](03-providers.md)                                       |
| Stretnúť ďalších študentov | [Pridajte sa k nášmu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Riešenie problémov

| Príznak                                   | Riešenie                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Pridajte Python do PATH alebo znova otvorte terminál po inštalácii|
| `pip` nemôže vytvoriť wheels (Windows)   | `pip install --upgrade pip setuptools wheel` a potom skúste znova.|
| `ModuleNotFoundError: dotenv`             | Spustite `pip install -r requirements.txt` (env nebolo nainštalované).|
| Zlyhanie Docker buildu *No space left*    | Docker Desktop ▸ *Settings* ▸ *Resources* → zväčšite diskovú šírku.|
| VS Code stále žiada opätovné otvorenie    | Môžete mať aktivované obe možnosti; vyberte si jednu (venv **alebo** kontajner)|
| OpenAI chyby 401 / 429                    | Skontrolujte hodnotu `OPENAI_API_KEY` / limity požiadaviek.       |
| Chyby pri používaní Conda                 | Nainštalujte Microsoft AI knižnice cez `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->