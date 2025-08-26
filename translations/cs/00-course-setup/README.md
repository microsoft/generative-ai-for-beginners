<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:56:56+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Začínáme s tímto kurzem

Jsme moc rádi, že začínáte tento kurz a těšíme se, co vás inspiruje k tvorbě s Generativní AI!

Abychom vám pomohli uspět, na této stránce najdete kroky k nastavení, technické požadavky a informace, kde získat pomoc, pokud ji budete potřebovat.

## Kroky k nastavení

Abyste mohli začít s tímto kurzem, je potřeba splnit následující kroky.

### 1. Forkněte tento repozitář

[Forkněte celý tento repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svého GitHub účtu, abyste mohli upravovat kód a plnit úkoly. Můžete si také [repozitař označit hvězdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste jej a související repozitáře snadno našli.

### 2. Vytvořte codespace

Aby nedocházelo k problémům se závislostmi při spouštění kódu, doporučujeme kurz spouštět v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ve svém forku: **Code -> Codespaces -> New on main**

![Dialog zobrazující tlačítka pro vytvoření codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Přidejte secret

1. ⚙️ Ikona ozubeného kola -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Název OPENAI_API_KEY, vložte svůj klíč, Uložit.

### 3.  Co dál?

| Chci…                | Pokračujte na…                                                         |
|----------------------|------------------------------------------------------------------------|
| Začít lekci 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Pracovat offline     | [`setup-local.md`](02-setup-local.md)                                  |
| Nastavit LLM poskytovatele | [`providers.md`](providers.md)                                   |
| Seznámit se s ostatními | [Připojte se na Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Řešení problémů

| Problém                                   | Řešení                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Sestavení kontejneru trvá > 10 min        | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminál se nepřipojil; klikněte na **+** ➜ *bash*              |
| `401 Unauthorized` od OpenAI              | Špatný / expirovaný `OPENAI_API_KEY`                            |
| VS Code ukazuje “Dev container mounting…” | Obnovte záložku v prohlížeči—Codespaces občas ztratí spojení    |
| Chybí kernel v notebooku                  | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiném). Přidejte do souboru následující řádek, kde `your_github_token_here` nahradíte svým skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete editor.

5. **Nainstalujte `python-dotenv`**: Pokud ještě nemáte, nainstalujte balíček `python-dotenv`, abyste mohli načítat proměnné prostředí ze souboru `.env` do své Python aplikace. Instalace přes `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve svém Python skriptu**: Ve svém Python skriptu použijte balíček `python-dotenv` k načtení proměnných prostředí ze souboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

A je to! Úspěšně jste vytvořili soubor `.env`, přidali svůj GitHub token a načetli jej do své Python aplikace.

## Jak spustit lokálně na svém počítači

Abyste mohli kód spustit lokálně, musíte mít nainstalovanou nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Repozitář si pak stáhnete pomocí:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte vše stažené, můžete začít!

## Volitelné kroky

### Instalace Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je odlehčený instalátor pro [Condu](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python a několik balíčků.
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Hodí se také pro instalaci balíčků, které nejsou dostupné přes `pip`.

Postupujte podle [návodu na instalaci MiniCondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po instalaci Minicondy si naklonujte [repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (pokud jste to ještě neudělali).

Dále je potřeba vytvořit virtuální prostředí. S Condou to uděláte tak, že vytvoříte nový soubor prostředí (_environment.yml_). Pokud pracujete v Codespaces, vytvořte jej ve složce `.devcontainer`, tedy `.devcontainer/environment.yml`.

Soubor prostředí naplňte tímto obsahem:

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

Pokud narazíte na chyby při používání condy, můžete knihovny Microsoft AI nainstalovat ručně tímto příkazem v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí určuje potřebné závislosti. `<environment-name>` je název, který chcete použít pro své Conda prostředí, a `<python-version>` je verze Pythonu, kterou chcete použít, například `3` je nejnovější hlavní verze Pythonu.

Poté můžete vytvořit Conda prostředí spuštěním těchto příkazů v příkazové řádce/terminálu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pokud narazíte na problémy, podívejte se do [průvodce prostředími Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použití Visual Studio Code s rozšířením pro Python

Doporučujeme používat editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pro tento kurz. Je to ale pouze doporučení, není to nutná podmínka.

> **Poznámka**: Otevřením repozitáře kurzu ve VS Code máte možnost nastavit projekt v kontejneru. Je to díky [speciální složce `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitáři kurzu. Více o tom později.

> **Poznámka**: Po naklonování a otevření složky ve VS Code vám editor automaticky nabídne instalaci rozšíření pro Python.

> **Poznámka**: Pokud vám VS Code nabídne znovu otevřít repozitář v kontejneru, odmítněte tuto možnost, abyste mohli použít lokálně nainstalovaný Python.

### Použití Jupyteru v prohlížeči

Na projektu můžete pracovat také v [prostředí Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve svém prohlížeči. Klasický Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nabízejí příjemné vývojové prostředí s funkcemi jako automatické doplňování, zvýraznění kódu apod.

Pro spuštění Jupyteru lokálně otevřete terminál/příkazovou řádku, přejděte do složky s kurzem a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím spustíte instanci Jupyteru a v příkazovém okně se zobrazí URL pro přístup.

Po otevření této adresy byste měli vidět osnovu kurzu a můžete procházet libovolné soubory `*.ipynb`. Například `08-building-search-applications/python/oai-solution.ipynb`.

### Spuštění v kontejneru

Alternativou k nastavování všeho na svém počítači nebo v Codespace je použití [kontejneru](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Speciální složka `.devcontainer` v repozitáři kurzu umožňuje VS Code nastavit projekt v kontejneru. Mimo Codespaces to ale vyžaduje instalaci Dockeru a je to trochu složitější, proto to doporučujeme spíše zkušenějším uživatelům.

Jedním z nejlepších způsobů, jak udržet své API klíče v bezpečí při používání GitHub Codespaces, je využití Codespace Secrets. Podívejte se na [průvodce správou secrets v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), kde se dozvíte více.

## Lekce a technické požadavky

Kurz obsahuje 6 koncepčních lekcí a 6 programovacích lekcí.

Pro programovací lekce používáme Azure OpenAI Service. Pro spuštění kódu budete potřebovat přístup k Azure OpenAI službě a API klíč. O přístup můžete požádat [vyplněním této žádosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Než bude vaše žádost zpracována, každá programovací lekce obsahuje také soubor `README.md`, kde si můžete prohlédnout kód a výstupy.

## První použití Azure OpenAI Service

Pokud s Azure OpenAI službou pracujete poprvé, postupujte podle tohoto návodu, jak [vytvořit a nasadit Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## První použití OpenAI API

Pokud s OpenAI API pracujete poprvé, postupujte podle návodu, jak [vytvořit a používat rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními účastníky

Vytvořili jsme kanály na našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), kde se můžete seznámit s ostatními účastníky. Je to skvělá příležitost navázat kontakty s dalšími podnikateli, vývojáři, studenty a všemi, kdo se chtějí zlepšit v Generativní AI.

[![Připojte se na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tým projektu bude také na tomto Discord serveru a pomůže všem účastníkům.

## Přispějte

Tento kurz je open-source iniciativa. Pokud najdete prostor pro zlepšení nebo narazíte na problém, vytvořte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo založte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tým projektu bude sledovat všechny příspěvky. Přispívání do open source je skvělý způsob, jak si budovat kariéru v oblasti Generativní AI.

Většina příspěvků vyžaduje, abyste souhlasili s Contributor License Agreement (CLA), kde prohlašujete, že máte právo a skutečně nám udělujete práva k použití vašeho příspěvku. Podrobnosti najdete na [webu CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překládání textů v tomto repozitáři prosím nepoužívejte strojový překlad. Překlady budeme ověřovat komunitou, proto se hlaste pouze na jazyky, které opravdu ovládáte.

Když odešlete pull request, CLA-bot automaticky zjistí, zda musíte podepsat CLA, a podle toho pull request označí (např. štítkem, komentářem). Stačí postupovat podle pokynů bota. Toto stačí udělat pouze jednou napříč všemi repozitáři využívajícími naše CLA.

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Další informace najdete v FAQ ke Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s případnými dotazy či připomínkami.

## Pojďme začít
Nyní, když jste dokončili potřebné kroky k absolvování tohoto kurzu, pojďme začít tím, že si přečteme [úvod do generativní AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.