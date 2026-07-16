# Začínáme s tímto kurzem

Jsme velmi nadšeni, že jste se rozhodli začít tento kurz a uvidíte, co vás inspiruje k tvorbě s Generativní AI!

Abychom zajistili váš úspěch, tato stránka uvádí kroky nastavení, technické požadavky a kde získat pomoc, pokud ji budete potřebovat.

## Kroky nastavení

Pro zahájení tohoto kurzu budete muset dokončit následující kroky.

### 1. Vytvořte fork tohoto repozitáře

[Vytvořte fork celého tohoto repozitáře](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svůj vlastní GitHub účet, abyste mohli měnit jakýkoli kód a plnit výzvy. Můžete také [označit (🌟) tento repozitář hvězdičkou](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste jej a související repozitáře snáze našli.

### 2. Vytvořte codespace

Aby nedocházelo k problémům se závislostmi při spouštění kódu, doporučujeme spustit tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ve svém fork repozitáři: **Code -> Codespaces -> New on main**

![Dialog s tlačítky pro vytvoření codespace](../../../translated_images/cs/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Přidejte secret

1. ⚙️ Ikona ozubeného kola -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Název OPENAI_API_KEY, vložte svůj klíč, Uložit.

### 3. Co dál?

| Chci…              | Jít do…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Začít Lekci 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracovat offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Nastavit poskytovatele LLM | [`providers.md`](03-providers.md)                                   |
| Setkat se s ostatními studenty | [Připojit se na náš Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Řešení problémů


| Příznak                                  | Řešení                                                         |
|-----------------------------------------|-----------------------------------------------------------------|
| Build kontejneru trvá déle než 10 min   | **Codespaces ➜ „Rebuild Container“**                            |
| `python: command not found`               | Terminál se nepřipojil; klikněte na **+** ➜ *bash*              |
| `401 Unauthorized` od OpenAI              | Špatný / expirovaný `OPENAI_API_KEY`                            |
| VS Code zobrazuje „Dev container mounting…“ | Obnovte záložku prohlížeče—Codespaces někdy ztratí spojení        |
| Chybí kernel v notebooku                 | Menu notebooku ➜ **Kernel ▸ Vybrat kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jakémkoli jiném editoru). Přidejte do souboru následující řádky, přičemž nahraďte zástupné symboly vlastním koncovým bodem a klíčem Microsoft Foundry Models (viz [`providers.md`](03-providers.md) pro informace, jak je získat):

   > **Poznámka:** GitHub Models (a jeho proměnná `GITHUB_TOKEN`) bude ukončen ke konci července 2026. Používejte místo toho [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete textový editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste tak ještě neučinili, budete muset nainstalovat balíček `python-dotenv`, který načte proměnné prostředí ze souboru `.env` do vaší Python aplikace. Instalaci provedete pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve svém Python skriptu**: Ve svém Python skriptu použijte balíček `python-dotenv` k načtení proměnných prostředí ze souboru `.env`:

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

Hotovo! Úspěšně jste vytvořili soubor `.env`, přidali své přihlašovací údaje Microsoft Foundry Models a načetli je do své Python aplikace.

## Jak spustit lokálně na svém počítači

Pro spuštění kódu lokálně na svém počítači budete potřebovat mít nainstalovanou nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pro použití repozitáře jej musíte naklonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte vše stažené, můžete začít!

## Nepovinné kroky

### Instalace Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků.
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Je také užitečný pro instalaci balíčků, které nejsou dostupné přes `pip`.

Můžete postupovat podle [návodu k instalaci MiniCondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po instalaci Minicondy naklonujte [repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (pokud jste tak již neučinili).

Dále je potřeba vytvořit virtuální prostředí. U Condy vytvořte nový soubor prostředí (_environment.yml_). Pokud projekt sledujete v Codespaces, vytvořte jej ve složce `.devcontainer`, tedy `.devcontainer/environment.yml`.

Naplňte svůj soubor prostředí následujícím snippetem:

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

Pokud se Vám při použití Condy objevují chyby, můžete ručně nainstalovat Microsoft AI knihovny pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje závislosti, které potřebujeme. `<environment-name>` označuje název, který chcete použít pro své Conda prostředí, a `<python-version>` je verze Pythonu, kterou chcete použít, například `3` je nejnovější hlavní verze Pythonu.

Poté můžete vytvořit své Conda prostředí spuštěním níže uvedených příkazů v příkazovém řádku / terminálu.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podcesta .devcontainer se používá pouze u nastavení Codespace
conda activate ai4beg
```

V případě problémů se podívejte na [návod k prostředím Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použití Visual Studio Code s rozšířením pro Python

Doporučujeme pro tento kurz používat editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Toto je však spíše doporučení než striktní požadavek.

> **Poznámka**: Při otevření repozitáře kurzu ve VS Code máte možnost nastavit projekt uvnitř kontejneru. Je to díky speciální složce [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) uvnitř repozitáře kurzu. O tomto si povíme více později.

> **Poznámka**: Po naklonování a otevření složky ve VS Code vám editor automaticky nabídne instalaci rozšíření pro Python.

> **Poznámka**: Pokud vám VS Code doporučí znovu otevřít repozitář v kontejneru, tuto volbu odmítněte, pokud chcete použít lokálně nainstalovanou verzi Pythonu.

### Použití Jupyter v prohlížeči

Projekt můžete také rozvíjet pomocí prostředí [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve webovém prohlížeči. Jak klasický Jupyter, tak [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nabízí příjemné prostředí s funkcemi jako automatické dokončování, zvýraznění kódu atd.

Pro spuštění Jupytera lokálně otevřete terminál / příkazový řádek, přejděte do složky kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím se spustí instance Jupytera a její URL bude zobrazeno v příkazovém okně.

Po přístupu na uvedenou adresu uvidíte osnovu kurzu a budete moci navigovat k jakémukoli souboru `*.ipynb`, například `08-building-search-applications/python/oai-solution.ipynb`.

### Spuštění v kontejneru

Alternativou k nastavení všeho na vašem počítači nebo v Codespace je použití [kontejneru](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Speciální složka `.devcontainer` v repozitáři kurzu umožňuje VS Code nastavit projekt uvnitř kontejneru. Mimo Codespaces to vyžaduje instalaci Dockeru a vyžaduje to trochu práce, proto to doporučujeme jen zkušeným uživatelům kontejnerů.

Jedním z nejlepších způsobů, jak zabezpečit své API klíče při použití GitHub Codespaces, je využití Codespace Secrets. Přečtěte si prosím [návod na správu tajemství v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), kde se o tom dozvíte více.


## Lekce a technické požadavky

Kurz obsahuje 6 konceptuálních lekcí a 6 lekcí s kódováním.

Pro lekce s kódováním používáme Azure OpenAI Service. Budete potřebovat přístup k Azure OpenAI služby a API klíč, abyste mohli tento kód spustit. Můžete požádat o přístup vyplněním [kéžadosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Zatímco čekáte na zpracování žádosti, každá lekce s kódováním obsahuje také soubor `README.md`, kde si můžete prohlédnout kód a výstupy.

## Poprvé používáte Azure OpenAI Service

Pokud Azure OpenAI Service používáte poprvé, postupujte podle tohoto průvodce, jak [vytvořit a nasadit zdroj Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Poprvé používáte OpenAI API

Pokud OpenAI API používáte poprvé, přečtěte si průvodce, jak [vytvořit a používat Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními studenty

Vytvořili jsme kanály na našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pro seznamování s ostatními studenty. Je to skvělý způsob, jak navázat kontakty s ostatními podnikateli, tvůrci, studenty a kýmkoli, kdo chce zlepšit své znalosti v oblasti Generativní AI.

[![Připojit se na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tým projektu bude také na tomto Discord serveru k dispozici pro pomoc všem studentům.

## Přispějte

Tento kurz je iniciativa s otevřeným zdrojovým kódem. Pokud uvidíte možnosti zlepšení nebo chyby, vytvořte prosím [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo nahlaste [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tým projektu bude sledovat všechny příspěvky. Přispívání do open source je skvělý způsob, jak budovat svou kariéru v oblasti Generativní AI.

Většina příspěvků vyžaduje souhlas s Contributor License Agreement (CLA), který prohlašuje, že máte právo a skutečně nám udělujete práva k použití svého příspěvku. Podrobnosti najdete na [webu CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překládání textu v tomto repozitáři prosím nepoužívejte strojový překlad. Překlady budeme ověřovat prostřednictvím komunity, proto prosím překládejte pouze do jazyků, ve kterých jste odborně zdatní.

Při odeslání pull requestu automaticky CLA-bot zjistí, zda je potřeba dodat CLA a podle toho PR označí (např. štítkem, komentářem). Stačí postupovat podle pokynů bota. Toto je potřeba udělat jen jednou u všech repozitářů používajících náš CLA.


Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte Často kladené otázky ke Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s jakýmikoli dalšími dotazy či připomínkami.

## Začněme

Nyní, když jste dokončili potřebné kroky k dokončení tohoto kurzu, pojďme začít se [seznámením s Generativní AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->