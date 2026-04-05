# Začínáme s tímto kurzem

Jsme velmi nadšení, že začínáte tento kurz a uvidíte, co vás inspiruje vytvořit s Generativní AI!

Abychom zajistili váš úspěch, tato stránka popisuje kroky nastavení, technické požadavky a kde získat pomoc, pokud bude potřeba.

## Kroky nastavení

Pro zahájení tohoto kurzu budete muset dokončit následující kroky.

### 1. Vytvořte fork tohoto repozitáře

[Vytvořte fork celého tohoto repozitáře](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svého vlastního účtu GitHub, abyste mohli měnit kód a dokončit úkoly. Také můžete [repozitář označit hvězdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste jej a související repozitáře snáze našli.

### 2. Vytvořte codespace

Aby nedocházelo k problémům se závislostmi při spouštění kódu, doporučujeme spouštět tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ve vašem forku: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/cs/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Přidejte tajný klíč

1. ⚙️ Klikněte na ikonu ozubeného kola -> Command Pallette -> Codespaces : Manage user secret -> Přidat nový tajný klíč.
2. Pojmenujte ho OPENAI_API_KEY, vložte svůj klíč, Uložit.

### 3. Co dál?

| Chci…               | Jít do…                                                                |
|---------------------|------------------------------------------------------------------------|
| Začít Lekci 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracovat offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Nastavit poskytovatele LLM | [`providers.md`](03-providers.md)                                        |
| Setkat se s ostatními studenty | [Připojit se k našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Řešení problémů

| Příznak                                      | Řešení                                                           |
|----------------------------------------------|------------------------------------------------------------------|
| Stavba kontejneru trvá déle než 10 minut    | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                  | Terminál není připojen; klikněte na **+** ➜ *bash*              |
| `401 Unauthorized` od OpenAI                 | Nesprávný / expirující `OPENAI_API_KEY`                          |
| VS Code ukazuje “Dev container mounting…”   | Obnovte záložku prohlížeče – Codespaces někdy ztratí spojení     |
| Absence jádra notebooku                      | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiný editor). Přidejte následující řádek do souboru, kde `your_github_token_here` nahraďte svým skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete textový editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste tak ještě neučinili, budete potřebovat nainstalovat balíček `python-dotenv` pro načítání proměnných prostředí ze souboru `.env` do vaší Python aplikace. Můžete jej nainstalovat pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve svém Python skriptu**: Ve svém Python skriptu použijte balíček `python-dotenv` k načtení proměnných prostředí ze souboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načíst proměnné prostředí ze souboru .env
   load_dotenv()

   # Přístup k proměnné GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je vše! Úspěšně jste vytvořili `.env` soubor, přidali svůj GitHub token a načetli ho do vaší Python aplikace.

## Jak spustit lokálně na vašem počítači

Pro lokální spuštění kódu na vašem počítači budete potřebovat mít nainstalovanou nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pro použití repozitáře je pak potřeba ho naklonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte všechno stažené, můžete začít!

## Nepovinné kroky

### Instalace Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků. 
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Je také užitečný pro instalaci balíčků, které nejsou dostupné přes `pip`.

Můžete postupovat podle [návodu na instalaci Minicondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) k jejímu nastavení.

Po instalaci Minicondy je třeba naklonovat [repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (pokud jste to ještě neudělali).

Poté je potřeba vytvořit virtuální prostředí. Pro Conda to uděláte vytvořením souboru prostředí (_environment.yml_). Pokud pracujete v Codespaces, vytvořte jej uvnitř adresáře `.devcontainer`, tedy `.devcontainer/environment.yml`.

Soubor prostředí naplňte následujícím kódem:

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

Pokud narazíte na chyby při použití condy, můžete ručně nainstalovat Microsoft AI knihovny pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje závislosti, které potřebujeme. `<environment-name>` označuje název, který chcete použít pro své Conda prostředí, a `<python-version>` je verze Pythonu, kterou chcete použít, např. `3` je nejnovější hlavní verze Pythonu.

Po dokončení můžete vytvořit Conda prostředí tak, že v příkazové řádce/terminálu spustíte následující příkazy:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podcesta .devcontainer platí pouze pro nastavení Codespace
conda activate ai4beg
```

Pokud narazíte na potíže, podívejte se do [návodu na správu Conda prostředí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použití Visual Studio Code s rozšířením podpory Pythonu

Pro tento kurz doporučujeme používat editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením podpory Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Toto je však spíše doporučení než definitivní požadavek.

> **Poznámka**: Po otevření repozitáře kurzu ve VS Code máte možnost nastavit projekt uvnitř kontejneru díky [speciálnímu adresáři `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitáři kurzu. O tom více později.

> **Poznámka**: Jakmile naklonujete a otevřete adresář ve VS Code, automaticky vám bude nabídnuto nainstalovat rozšíření podpory Pythonu.

> **Poznámka**: Pokud VS Code doporučí znovu otevřít repozitář v kontejneru, odmítněte tuto žádost, chcete-li používat lokálně nainstalovanou verzi Pythonu.

### Použití Jupyter v prohlížeči

Můžete také pracovat na projektu pomocí prostředí [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve svém prohlížeči. Jak klasický Jupyter, tak [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytují příjemné vývojové prostředí s funkcemi jako automatické dokončování, zvýraznění kódu apod.

Pro spuštění Jupytera lokálně přejděte do terminálu/příkazového řádku, přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím spustíte instanci Jupytera a URL pro přístup k ní bude zobrazeno v okně příkazové řádky.

Po vstupu na tuto URL byste měli vidět osnovu kurzu a být schopni přistupovat k libovolnému souboru `*.ipynb`. Například `08-building-search-applications/python/oai-solution.ipynb`.

### Spouštění v kontejneru

Alternativou k nastavení všeho na vašem počítači nebo v Codespace je použití [kontejneru](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Speciální složka `.devcontainer` v repozitáři kurzu umožňuje VS Code nastavit projekt uvnitř kontejneru. Mimo Codespaces to vyžaduje instalaci Dockeru a upřímně řečeno, je to trochu práce, proto to doporučujeme pouze těm, kdo mají zkušenosti s kontejnery.

Jedním z nejlepších způsobů, jak zabezpečit své API klíče při používání GitHub Codespaces, je použití Codespace Secrets. Podrobnosti naleznete v průvodci [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lekce a technické požadavky

Kurz má 6 koncepčních lekcí a 6 lekcí s kódováním.

Pro lekce s kódováním používáme Azure OpenAI Service. Budete potřebovat přístup k Azure OpenAI službě a API klíč pro spuštění tohoto kódu. O přístup můžete požádat [vyplněním této žádosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Zatímco čekáte na vyřízení vaší žádosti, každá lekce s kódováním obsahuje také soubor `README.md`, kde můžete zobrazit kód a výstupy.

## Použití Azure OpenAI Service poprvé

Pokud s Azure OpenAI službou pracujete poprvé, postupujte podle tohoto návodu, jak [vytvořit a nasadit Azure OpenAI Service zdroj.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použití OpenAI API poprvé

Pokud pracujete s OpenAI API poprvé, postupujte podle návodu, jak [vytvořit a používat rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Setkejte se s ostatními studenty

Vytvořili jsme kanály v našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pro setkání s ostatními studenty. Je to skvělý způsob, jak navázat kontakty s dalšími podobně smýšlejícími podnikateli, vývojáři, studenty a kýmkoliv, kdo se chce posunout v generativní AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektový tým bude také na tomto Discord serveru, aby pomáhal všem studentům.

## Přispívejte

Tento kurz je otevřený open-source projekt. Pokud vidíte oblasti ke zlepšení nebo problémy, vytvořte prosím [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo nahlaste [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektový tým bude sledovat všechny příspěvky. Přispívání do open source je skvělý způsob, jak budovat svou kariéru v oblasti Generativní AI.

Většina příspěvků vyžaduje souhlas s Licenční smlouvou přispěvatele (Contributor License Agreement, CLA), která potvrzuje, že máte právo a skutečně nám udělujete práva používat váš příspěvek. Pro detaily navštivte [web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překladu textu v tomto repozitáři prosím nepoužívejte strojový překlad. Překlady budou ověřovány komunitou, proto se přihlašujte pouze k překladům do jazyků, ve kterých jste zdatní.

Při odeslání pull requestu automaticky CLA-bot zjistí, zda je potřeba dodat CLA a příslušně označí PR (např. štítek, komentář). Stačí následovat pokyny bota. Toto budete muset udělat pouze jednou napříč všemi repozitáři, které používají naše CLA.

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte FAQ k pravidlům chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s dalšími dotazy či komentáři.

## Pojďme začít!
Nyní, když jste dokončili potřebné kroky k dokončení tohoto kurzu, pojďme začít tím, že získáme [úvod do Generativní AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->