# Lokální nastavení 🖥️

**Použijte tento návod, pokud dáváte přednost spuštění všeho na vlastním notebooku.**  
Máte dvě možnosti: **(A) nativní Python + virtual-env** nebo **(B) VS Code Dev Container s Dockerem**.  
Vyberte si, co vám přijde jednodušší – obě cesty vedou ke stejným lekcím.

## 1.  Požadavky

| Nástroj            | Verze / Poznámky                                                                    |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (stáhněte z <https://python.org>)                                           |
| **Git**            | Nejnovější (součástí Xcode / Git pro Windows / správce balíčků Linuxu)              |
| **VS Code**        | Volitelný, ale doporučený <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Pouze* pro možnost B. Zdarma ke stažení: <https://docs.docker.com/desktop/>        |

> 💡 **Tip** – Ověřte nástroje v terminálu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnost A – Nativní Python (nejrychlejší)

### Krok 1  Naklonujte tento repozitář

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Krok 2 Vytvořte a aktivujte virtuální prostředí

```bash
python -m venv .venv          # vytvořit jeden
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Výzva by nyní měla začínat (.venv) – to znamená, že jste uvnitř prostředí.

### Krok 3 Nainstalujte závislosti

```bash
pip install -r requirements.txt
```

Přejděte k Sekci 3 o [API klíčích](../../../00-course-setup)

## 2. Možnost B – VS Code Dev Container (Docker)

Tento repozitář a kurz jsme nastavili s [vývojovým kontejnerem](https://containers.dev?WT.mc_id=academic-105485-koreyst), který má univerzální runtime podporující Python3, .NET, Node.js a Java vývoj. Související konfigurace je definována v souboru `devcontainer.json` umístěném ve složce `.devcontainer/` v kořenovém adresáři tohoto repozitáře.

>**Proč tuto možnost?**  
>Identické prostředí jako Codespaces; žádný drift závislostí.

### Krok 0 Nainstalujte doplňky

Docker Desktop – ověřte, že funguje příkaz ```docker --version```.  
VS Code Remote – Containers rozšíření (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otevřete repozitář ve VS Code

Soubor ▸ Otevřít složku… → generative-ai-for-beginners

VS Code detekuje .devcontainer/ a zobrazí výzvu.

### Krok 2 Znovu otevřete v kontejneru

Klikněte na „Reopen in Container“. Docker sestaví image (≈ 3 minuty při prvním spuštění).  
Když se objeví terminálová výzva, jste uvnitř kontejneru.

## 2.  Možnost C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků.  
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Hodí se také pro instalaci balíčků, které nejsou dostupné přes `pip`.

### Krok 0  Nainstalujte Miniconda

Postupujte podle [návodu na instalaci MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Vytvořte virtuální prostředí

Vytvořte nový soubor prostředí (*environment.yml*). Pokud používáte Codespaces, vytvořte ho ve složce `.devcontainer`, tedy `.devcontainer/environment.yml`.

### Krok 2  Naplňte soubor prostředí

Přidejte následující úryvek do vašeho `environment.yml`

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

### Krok 3 Vytvořte Conda prostředí

Spusťte níže uvedené příkazy v příkazovém řádku/terminálu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podcesta .devcontainer platí pouze pro nastavení Codespace
conda activate ai4beg
```

Pokud narazíte na problémy, podívejte se do [návodu na Conda prostředí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnost D – Klasický Jupyter / Jupyter Lab (v prohlížeči)

> **Pro koho je to?**  
> Pro každého, kdo miluje klasické rozhraní Jupyter nebo chce spouštět notebooky bez VS Code.

### Krok 1  Ujistěte se, že máte Jupyter nainstalovaný

Pro spuštění Jupyter lokálně přejděte do terminálu/příkazového řádku, přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím se spustí instance Jupyter a URL pro přístup bude zobrazena v příkazovém řádku.

Po přístupu na URL byste měli vidět osnovu kurzu a můžete procházet jakýkoli soubor `*.ipynb`. Například `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Přidejte své API klíče

Je důležité uchovávat své API klíče v bezpečí při tvorbě jakékoli aplikace. Doporučujeme neukládat API klíče přímo v kódu. Pokud byste tyto údaje commitovali do veřejného repozitáře, mohlo by to vést k bezpečnostním problémům a nežádoucím nákladům, pokud by je zneužil někdo nepovolaný.  
Zde je krok za krokem návod, jak vytvořit `.env` soubor pro Python a přidat `GITHUB_TOKEN`:

1. **Přejděte do adresáře projektu**: Otevřete terminál nebo příkazový řádek a přejděte do kořenového adresáře projektu, kde chcete `.env` soubor vytvořit.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvořte `.env` soubor**: Použijte svůj oblíbený textový editor k vytvoření nového souboru s názvem `.env`. Pokud používáte příkazový řádek, můžete použít `touch` (na systémech Unix) nebo `echo` (na Windows):

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte `.env` soubor**: Otevřete `.env` soubor v textovém editoru (např. VS Code, Notepad++ nebo jiný editor). Přidejte následující řádek, kde `your_github_token_here` nahraďte svým skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste tak ještě neučinili, budete potřebovat nainstalovat balíček `python-dotenv`, který načte proměnné prostředí ze souboru `.env` do vaší Python aplikace. Nainstalujete ho pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve svém Python skriptu**: Ve svém Python skriptu použijte balíček `python-dotenv` k načtení proměnných prostředí ze souboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načíst proměnné prostředí ze souboru .env
   load_dotenv()

   # Přistupovat k proměnné GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je vše! Úspěšně jste vytvořili `.env` soubor, přidali GitHub token a načetli ho do své Python aplikace.

🔐 Nikdy necommitujte `.env` – je již v `.gitignore`.  
Kompletní instrukce poskytovatelů najdete v [`providers.md`](03-providers.md).

## 4. Co dál?

| Chci…               | Jít na…                                                                |
|---------------------|------------------------------------------------------------------------|
| Začít Lekci 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nastavit poskytovatele LLM | [`providers.md`](03-providers.md)                                   |
| Seznámit se s ostatními studenty | [Připojit se na náš Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Řešení problémů

| Příznak                                   | Řešení                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Přidejte Python do PATH nebo znovu otevřete terminál po instalaci|
| `pip` nemůže sestavit wheels (Windows)   | `pip install --upgrade pip setuptools wheel` a zkuste znovu.    |
| `ModuleNotFoundError: dotenv`             | Spusťte `pip install -r requirements.txt` (prostředí nebylo nainstalováno). |
| Docker build selže *No space left*        | Docker Desktop ▸ *Nastavení* ▸ *Zdroje* → zvětšete velikost disku.|
| VS Code stále nabízí znovu otevřít        | Můžete mít aktivní obě možnosti; vyberte jednu (venv **nebo** kontejner)|
| OpenAI 401 / 429 chyby                     | Zkontrolujte hodnotu `OPENAI_API_KEY` / limity požadavků.        |
| Chyby při použití Conda                    | Nainstalujte Microsoft AI knihovny pomocí `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->