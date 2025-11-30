<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:56:14+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "cs"
}
-->
# Lokální nastavení 🖥️

**Použijte tento návod, pokud chcete vše spouštět na svém vlastním notebooku.**  
Máte dvě možnosti: **(A) nativní Python + virtual-env** nebo **(B) VS Code Dev Container s Dockerem**.  
Vyberte si, co vám vyhovuje víc—obě cesty vedou ke stejným lekcím.

## 1.  Požadavky

| Nástroj            | Verze / Poznámky                                                                 |
|--------------------|----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (stáhněte z <https://python.org>)                                         |
| **Git**            | Nejnovější (součástí Xcode / Git for Windows / správce balíčků na Linuxu)        |
| **VS Code**        | Volitelné, ale doporučené <https://code.visualstudio.com>                        |
| **Docker Desktop** | *Pouze* pro možnost B. Zdarma: <https://docs.docker.com/desktop/>                |

> 💡 **Tip** – Ověřte si nástroje v terminálu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnost A – Nativní Python (nejrychlejší)

### Krok 1  Naklonujte toto repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Krok 2 Vytvořte a aktivujte virtuální prostředí

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Výzva v terminálu by teď měla začínat (.venv)—to znamená, že jste uvnitř prostředí.

### Krok 3 Nainstalujte závislosti

```bash
pip install -r requirements.txt
```

Přeskočte na sekci 3 o [API klíčích](../../../00-course-setup)

## 2. Možnost B – VS Code Dev Container (Docker)

Toto repozitář a kurz jsme připravili s [vývojovým kontejnerem](https://containers.dev?WT.mc_id=academic-105485-koreyst), který má univerzální runtime podporující Python3, .NET, Node.js a Javu. Související konfigurace je v souboru `devcontainer.json` ve složce `.devcontainer/` v kořeni repozitáře.

>**Proč zvolit tuto možnost?**
>Identické prostředí jako Codespaces; žádné rozdíly v závislostech.

### Krok 0 Nainstalujte potřebné doplňky

Docker Desktop – ověřte, že ```docker --version``` funguje.
VS Code Remote – Containers rozšíření (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otevřete repo ve VS Code

Soubor ▸ Otevřít složku…  → generative-ai-for-beginners

VS Code detekuje .devcontainer/ a zobrazí výzvu.

### Krok 2 Otevřete znovu v kontejneru

Klikněte na “Reopen in Container”. Docker vytvoří image (první spuštění ≈ 3 min).
Jakmile se objeví výzva v terminálu, jste uvnitř kontejneru.

## 2.  Možnost C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je odlehčený instalátor pro [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python a několik balíčků.
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Hodí se také pro instalaci balíčků, které nejsou dostupné přes `pip`.

### Krok 0  Instalujte Miniconda

Postupujte podle [MiniConda instalačního průvodce](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Vytvořte virtuální prostředí

Vytvořte nový soubor prostředí (*environment.yml*). Pokud postupujete podle návodu v Codespaces, vytvořte ho ve složce `.devcontainer`, tedy `.devcontainer/environment.yml`.

### Krok 2  Vyplňte soubor prostředí

Přidejte následující úryvek do svého `environment.yml`

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

Spusťte níže uvedené příkazy v příkazové řádce/terminálu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pokud narazíte na problémy, podívejte se do [průvodce prostředími Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnost D – Klasický Jupyter / Jupyter Lab (ve vašem prohlížeči)

> **Pro koho to je?**  
> Pro každého, kdo má rád klasické rozhraní Jupyter nebo chce spouštět notebooky bez VS Code.  

### Krok 1  Ověřte, že máte nainstalovaný Jupyter

Pro spuštění Jupyteru lokálně otevřete terminál/příkazovou řádku, přejděte do složky s kurzem a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím spustíte instanci Jupyteru a v příkazové řádce se zobrazí URL pro přístup.

Po otevření URL byste měli vidět osnovu kurzu a můžete přejít do libovolného `*.ipynb` souboru. Například `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Přidejte své API klíče

Udržet své API klíče v bezpečí je důležité při vývoji jakékoliv aplikace. Nedoporučujeme ukládat API klíče přímo do kódu. Pokud byste je omylem nahráli do veřejného repozitáře, mohlo by to vést k bezpečnostním problémům a nechtěným nákladům, pokud by je někdo zneužil.
Zde je postup, jak vytvořit soubor `.env` pro Python a přidat `GITHUB_TOKEN`:

1. **Přejděte do složky projektu**: Otevřete terminál nebo příkazovou řádku a přejděte do kořenové složky projektu, kde chcete vytvořit soubor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvořte soubor `.env`**: Použijte svůj oblíbený textový editor k vytvoření nového souboru s názvem `.env`. Pokud používáte příkazovou řádku, můžete použít `touch` (na Unix systémech) nebo `echo` (na Windows):

   Unix systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiném). Přidejte do souboru následující řádek a nahraďte `your_github_token_here` svým skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste to ještě neudělali, nainstalujte balíček `python-dotenv`, který načte proměnné prostředí ze souboru `.env` do vaší Python aplikace. Instalace přes `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve svém Python skriptu**: Ve svém Python skriptu použijte balíček `python-dotenv` pro načtení proměnných prostředí ze souboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hotovo! Úspěšně jste vytvořili soubor `.env`, přidali svůj GitHub token a načetli ho do své Python aplikace.

🔐 Nikdy neukládejte .env do repozitáře—už je v .gitignore.
Kompletní instrukce k poskytovatelům najdete v [`providers.md`](03-providers.md).

## 4. Co dál?

| Chci…               | Pokračujte na…                                                           |
|---------------------|--------------------------------------------------------------------------|
| Začít lekci 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Nastavit LLM poskytovatele | [`providers.md`](03-providers.md)                                  |
| Poznat další studenty | [Připojte se na Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Řešení problémů

| Problém                                   | Řešení                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Přidejte Python do PATH nebo znovu otevřete terminál po instalaci|
| `pip` nemůže sestavit wheels (Windows)    | `pip install --upgrade pip setuptools wheel` a zkuste znovu.    |
| `ModuleNotFoundError: dotenv`             | Spusťte `pip install -r requirements.txt` (prostředí nebylo nainstalováno).|
| Selhání Docker buildu *No space left*     | Docker Desktop ▸ *Nastavení* ▸ *Zdroje* → zvětšete disk.        |
| VS Code stále nabízí znovuotevření        | Možná máte aktivní obě možnosti; vyberte jednu (venv **nebo** kontejner)|
| OpenAI 401 / 429 chyby                    | Zkontrolujte hodnotu `OPENAI_API_KEY` / limity požadavků.       |
| Chyby při použití Conda                   | Instalujte Microsoft AI knihovny pomocí `conda install -c microsoft azure-ai-ml`|

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.