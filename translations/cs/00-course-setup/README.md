# Začínáme s tímto kurzem

Jsme velmi nadšeni, že začínáte tento kurz a uvidíte, co vás inspiruje k tvoření s generativní AI!

Abychom zajistili váš úspěch, tato stránka popisuje kroky nastavení, technické požadavky a kde získat pomoc, pokud ji budete potřebovat.

## Kroky nastavení

Pro zahájení tohoto kurzu budete muset dokončit následující kroky.

### 1. Vytvořte fork tohoto repozitáře

[Vytvořte fork celého repozitáře](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svého vlastního účtu na GitHubu, abyste mohli měnit kód a dokončovat úkoly. Můžete také [repozitář označit hvězdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste jej a související repozitáře snáze našli.

### 2. Vytvořte codespace

Aby nedocházelo k problémům s závislostmi při běhu kódu, doporučujeme spouštět tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ve vašem forku: **Code -> Codespaces -> New on main**

![Dialog zobrazující tlačítka pro vytvoření codespace](../../../translated_images/cs/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Přidejte tajemství

1. ⚙️ Ikona ozubeného kola -> Command Palette -> Codespaces : Manage user secret -> Přidat nové tajemství.
2. Pojmenujte ho OPENAI_API_KEY, vložte svůj klíč a uložte.

### 3. Co dál?

| Chci…             | Jít na…                                                               |
|---------------------|----------------------------------------------------------------------|
| Začít Lekci 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| Pracovat offline   | [`setup-local.md`](02-setup-local.md)                                |
| Nastavit poskytovatele LLM | [`providers.md`](03-providers.md)                             |
| Seznámit se s ostatními studenty | [Připojit se na Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)     |

## Řešení problémů


| Příznak                                   | Řešení                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Stavba kontejneru zamrzla > 10 min         | **Codespaces ➜ „Rebuild Container“**                          |
| `python: command not found`                | Terminál se nepřipojil; klikněte na **+** ➜ *bash*             |
| `401 Unauthorized` z OpenAI                 | Špatný / prošlý `OPENAI_API_KEY`                               |
| VS Code zobrazuje „Dev container mounting…“ | Obnovte záložku prohlížeče — Codespaces někdy ztratí připojení  |
| Chybí kernel v notebooku                    | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jakémkoli jiném editoru). Přidejte následující řádky do souboru, nahraďte zástupné hodnoty skutečným koncovým bodem a klíčem Microsoft Foundry Models (viz [`providers.md`](03-providers.md) pro informace, jak je získat):

   > **Poznámka:** GitHub Models (a jeho proměnná `GITHUB_TOKEN`) bude ukončen koncem července 2026. Místo toho používejte [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete textový editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste tak ještě neučinili, budete muset nainstalovat balíček `python-dotenv` pro načítání proměnných prostředí ze souboru `.env` do vaší Python aplikace. Můžete jej nainstalovat pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve vašem Python skriptu**: Ve vašem Python skriptu použijte balíček `python-dotenv`, abyste načetli proměnné prostředí ze souboru `.env`:

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

Hotovo! Úspěšně jste vytvořili `.env` soubor, přidali přihlašovací údaje Microsoft Foundry Models a načetli je do vaší Python aplikace.

## Jak spustit lokálně na vašem počítači

Pro lokální spuštění kódu na vašem počítači budete potřebovat mít nainstalovanou nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pro použití repozitáře je pak třeba jej naklonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile budete mít vše staženo, můžete začít!

## Nepovinné kroky

### Instalace Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Condy](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků.
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Je také užitečná pro instalaci balíčků, které nejsou dostupné přes `pip`.

Postupujte podle [návodu k instalaci Minicondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), abyste ji nastavili.

Po instalaci Minicondy je třeba naklonovat [repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (pokud jste tak ještě neučinili)

Dále je potřeba vytvořit virtuální prostředí. Pro Condu vytvořte nový soubor prostředí (_environment.yml_). Pokud používáte Codespaces, umístěte jej do adresáře `.devcontainer`, tedy `.devcontainer/environment.yml`.

Do souboru vložte níže uvedený úryvek:

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

Pokud vám s Condou vznikají chyby, můžete ručně nainstalovat Microsoft AI knihovny pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje závislosti, které potřebujeme. `<environment-name>` je název, který chcete pro své Conda prostředí použít, a `<python-version>` je verze Pythonu, kterou chcete používat, například `3` je nejnovější hlavní verze Pythonu.

S tímto hotovo můžete vytvořit Conda prostředí spuštěním příkazů níže v příkazovém řádku/terminálu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podcesta platí pouze pro nastavení Codespace
conda activate ai4beg
```

Pokud narazíte na problémy, podívejte se na [návod k prostředím Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použití Visual Studio Code s rozšířením pro Python

Doporučujeme použít editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pro tento kurz. Toto je však spíše doporučení než povinná podmínka.

> **Poznámka**: Otevřením repozitáře kurzu ve VS Code máte možnost nastavit projekt v kontejneru. Je to díky [speciálnímu adresáři `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitáři kurzu. O tom později více.

> **Poznámka**: Po naklonování a otevření adresáře ve VS Code automaticky nabídne instalaci rozšíření Python.

> **Poznámka**: Pokud VS Code nabídne znovuotevření repozitáře v kontejneru, odmítněte to, abyste mohli použít lokálně nainstalovaný Python.

### Použití Jupyteru v prohlížeči

Projekt můžete také vyvíjet pomocí [prostředí Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve vašem prohlížeči. Klasický Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytují příjemné vývojové prostředí s funkcemi jako automatické doplňování, zvýraznění kódu atd.

Chcete-li spustit Jupyter lokálně, otevřete terminál/příkazový řádek, přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím spustíte instanci Jupyter a URL k ní bude zobrazena v okně příkazového řádku.

Po přístupu na URL byste měli vidět osnovu kurzu a moci navigovat k libovolnému souboru `*.ipynb`, například `08-building-search-applications/python/oai-solution.ipynb`.

### Spuštění v kontejneru

Alternativou k nastavení všeho na počítači nebo Codespace je použití [kontejneru](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Speciální složka `.devcontainer` v repozitáři kurzu umožňuje VS Code nastavit projekt v rámci kontejneru. Mimo Codespaces to vyžaduje instalaci Dockeru a upřímně řečeno, trochu práce, takže to doporučujeme pouze zkušeným uživatelům kontejnerů.

Jedním z nejlepších způsobů, jak bezpečně uchovat své API klíče při používání GitHub Codespaces, je použití Codespace Secrets. Následujte prosím [návod pro správu tajemství v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), kde se o tom dozvíte více.


## Lekce a technické požadavky

Kurz obsahuje „Learn“ lekce, které vysvětlují koncepty generativní AI, a „Build“ lekce s praktickými příklady kódu v **Pythonu** a kde je to možné i ve **TypeScriptu**.

Pro kódovací lekce používáme Azure OpenAI v Microsoft Foundry. Budete potřebovat Azure předplatné a API klíč. Přístup je otevřený – není třeba žádná žádost – takže můžete [vytvořit Microsoft Foundry zdroj a nasadit model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) a získat svůj endpoint a klíč.

Každá kódovací lekce také obsahuje soubor `README.md`, kde můžete bez spuštění kódu prohlédnout kód a výstupy.

## Používání Azure OpenAI služby poprvé

Pokud poprvé pracujete se službou Azure OpenAI, postupujte podle tohoto návodu, jak [vytvořit a nasadit Azure OpenAI Service zdroj.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Používání OpenAI API poprvé

Pokud pracujete s OpenAI API poprvé, řiďte se návodem, jak [vytvořit a použít rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními studenty

Vytvořili jsme kanály na našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), kde můžete potkat ostatní studenty. Je to skvělý způsob, jak navázat kontakty s dalšími podnikateli, vývojáři, studenty a všemi, kdo se chtějí zlepšovat v generativní AI.

[![Připojit se na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tým projektu bude také na tomto Discord serveru, aby pomáhal studentům.

## Přispějte

Tento kurz je open-source iniciativa. Pokud vidíte oblasti ke zlepšení nebo chyby, vytvořte prosím [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo nahlašte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tým projektu sleduje všechny příspěvky. Přispívání do open-source je skvělý způsob, jak budovat kariéru v generativní AI.

Většina příspěvků vyžaduje, abyste souhlasili s Contributor License Agreement (CLA), který potvrzuje, že máte právo a skutečně udělujete práva používání vašeho příspěvku. Podrobnosti najdete na [CLA, Contributor License Agreement webu](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překladu textů v tomto repozitáři prosím nepoužívejte strojový překlad. Překlady ověřujeme komunitou, proto se přihlašujte k překládání pouze do jazyků, kterými skutečně ovládáte.


Když odešlete pull request, CLA-bot automaticky určí, zda potřebujete poskytnout CLA, a náležitě označí PR (např. štítek, komentář). Stačí, když budete postupovat podle pokynů bota. Toto budete muset udělat pouze jednou napříč všemi repozitáři, které používají náš CLA.

Tento projekt přijal [Kodex chování Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte Často kladené dotazy ke Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s jakýmikoli dalšími dotazy či připomínkami.

## Začněme

Nyní, když jste dokončili potřebné kroky k absolvování tohoto kurzu, pojďme začít s [úvodem do generativní umělé inteligence a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->