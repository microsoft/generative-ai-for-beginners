# Lokální nastavení 🖥️

**Použijte tento návod, pokud raději všechno spouštíte na svém vlastním notebooku.**   
Máte dvě možnosti: **(A) nativní Python + virtual-env** nebo **(B) VS Code Dev Container s Dockerem**.  
Zvolte, co je vám pohodlnější—obě vedou ke stejným lekcím.

## 1.  Požadavky

| Nástroj             | Verze / Poznámky                                                                   |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (získejte na <https://python.org>)                                          |
| **Git**            | Nejnovější (součástí Xcode / Git pro Windows / správce balíčků Linuxu)              |
| **VS Code**        | Volitelný, ale doporučený <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Pouze* pro možnost B. Zdarma ke stažení: <https://docs.docker.com/desktop/>       |

> 💡 **Tip** – Ověřte nástroje v terminálu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnost A – Nativní Python (nejrychlejší)

### Krok 1  Klonujte tento repozitář

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

✅ Výzva by nyní měla začínat (.venv)—to znamená, že jste v prostředí.

### Krok 3 Nainstalujte závislosti

```bash
pip install -r requirements.txt
```

Přejděte k Sekci 3 o [API klíčích](#3-přidání-vašich-api-klíčů)

## 2. Možnost B – VS Code Dev Container (Docker)

Tento repozitář a kurz jsme nastavili s [vývojovým kontejnerem](https://containers.dev?WT.mc_id=academic-105485-koreyst), který má univerzální runtime podporující vývoj v Python3, .NET, Node.js a Javě. Příslušná konfigurace je definovaná v souboru `devcontainer.json` ve složce `.devcontainer/` v kořeni repozitáře.

>**Proč zvolit toto?**
>Identické prostředí jako Codespaces; žádný drift závislostí.

### Krok 0 Nainstalujte doplňky

Docker Desktop – ověřte, že `docker --version` funguje.
Rozšíření VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otevřete repozitář ve VS Code

Soubor ▸ Otevřít složku… → generative-ai-for-beginners

VS Code detekuje .devcontainer/ a objeví se výzva.

### Krok 2 Otevřete znovu v kontejneru

Klikněte na “Otevřít znovu v kontejneru”. Docker sestaví obraz (≈ 3 min při prvním spuštění).
Když se objeví terminálová výzva, jste uvnitř kontejneru.

## 2.  Možnost C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalační program pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků.
Conda sama je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Je užitečná také pro instalaci balíčků, které nejsou dostupné přes `pip`.

### Krok 0  Nainstalujte Miniconda

Postupujte podle [návodu na instalaci MiniCondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Vytvořte virtuální prostředí

Vytvořte nový soubor prostředí (*environment.yml*). Pokud pracujete v Codespaces, vytvořte ho ve složce `.devcontainer`, tedy `.devcontainer/environment.yml`.

### Krok 2  Naplňte soubor prostředí

Přidejte následující ukázkový kód do svého souboru `environment.yml`

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

Spusťte níže uvedené příkazy ve svém příkazovém řádku/terminálu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podsložka .devcontainer platí pouze pro nastavení Codespace
conda activate ai4beg
```

Pokud narazíte na problémy, nahlédněte do [návodu na Conda prostředí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnost D – Klasický Jupyter / Jupyter Lab (v prohlížeči)

> **Pro koho je to vhodné?**  
> Pro všechny, kdo mají rádi klasické rozhraní Jupyter nebo chtějí spustit notebooky bez VS Code.  

### Krok 1  Ověřte, že je Jupyter nainstalovaný

Pro spuštění Jupyteru lokálně přejděte do terminálu/příkazové řádky, přesuňte se do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím se spustí instance Jupyteru a URL pro přístup bude zobrazená v příkazovém okně.

Po přístupu na URL uvidíte osnovu kurzu a můžete navigovat do jakéhokoli souboru `*.ipynb`. Například `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Přidání vašich API klíčů

Je důležité mít API klíče bezpečně uložené při budování aplikace. Nedoporučujeme ukládat API klíče přímo v kódu. Komitování těchto dat do veřejného repozitáře může vést k bezpečnostním rizikům a i nechtěným nákladům, pokud je někdo zneužije.
Zde je krok za krokem návod, jak vytvořit soubor `.env` pro Python a přidat své přihlašovací údaje Microsoft Foundry Models:

> **Poznámka:** GitHub Models (a jeho proměnná `GITHUB_TOKEN`) bude ukončeno koncem července 2026. Tento návod používá místo toho [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Chcete pracovat plně offline? Podívejte se na [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Přejděte do adresáře svého projektu**: Otevřete terminál nebo příkazový řádek a přejděte do kořenového adresáře projektu, kde chcete vytvořit soubor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvořte soubor `.env`**: Pomocí svého oblíbeného textového editoru vytvořte nový soubor s názvem `.env`. Pokud používáte příkazový řádek, můžete použít `touch` (na Unixových systémech) nebo `echo` (ve Windows):

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiný editor). Přidejte do něj následující řádky, přičemž nahraďte zástupné hodnoty skutečným endpointem a API klíčem Microsoft Foundry projektu:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste to ještě neudělali, je třeba nainstalovat balíček `python-dotenv` pro načítání proměnných prostředí ze souboru `.env` do vaší Python aplikace. Nainstalujte jej pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve vašem Python skriptu**: Ve svém Python skriptu použitím balíčku `python-dotenv` načtěte proměnné prostředí ze souboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načíst proměnné prostředí ze souboru .env
   load_dotenv()

   # Přístup k proměnným Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je vše! Úspěšně jste vytvořili `.env` soubor, přidali přihlašovací údaje Microsoft Foundry Models a načetli je do své Python aplikace.

🔐 Nikdy necommitujte `.env`—je již zahrnut v `.gitignore`.
Kompletní instrukce poskytovatele najdete v [`providers.md`](03-providers.md).

## 4. Co dál?

| Chci…             | Jít na…                                                                |
|---------------------|------------------------------------------------------------------------|
| Začít Lekci 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nastavit poskytovatele LLM | [`providers.md`](03-providers.md)                                    |
| Seznámit se s ostatními studenty | [Připojit se na náš Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Odstraňování potíží

| Příznak                                  | Oprava                                                          |
|------------------------------------------|----------------------------------------------------------------|
| `python nenalezen`                      | Přidejte Python do PATH nebo znovu otevřete terminál po instalaci |
| `pip` nedokáže sestavit wheels (Windows) | `pip install --upgrade pip setuptools wheel` a zkuste znovu.     |
| `ModuleNotFoundError: dotenv`            | Spusťte `pip install -r requirements.txt` (prostředí nebylo nainstalováno). |
| Docker build selže *Není místo*           | Docker Desktop ▸ *Nastavení* ▸ *Zdroje* → zvětšete velikost disku. |
| VS Code opakovaně nabízí znovu otevřít   | Můžete mít aktivní obě možnosti; zvolte jednu (venv **nebo** kontejner)|
| OpenAI chyby 401 / 429                    | Zkontrolujte hodnotu `OPENAI_API_KEY` / limity požadavků.        |
| Chyby při používání Conda                  | Nainstalujte Microsoft AI knihovny pomocí `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->