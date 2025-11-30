<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T21:38:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Začínáme s tímto kurzem

Jsme nadšeni, že začínáte tento kurz, a těšíme se, co vás inspiruje k vytvoření s Generativní AI!

Abychom zajistili váš úspěch, tato stránka obsahuje kroky nastavení, technické požadavky a informace, kde získat pomoc, pokud ji budete potřebovat.

## Kroky nastavení

Abyste mohli začít s tímto kurzem, je třeba dokončit následující kroky.

### 1. Forkněte tento repozitář

[Forkněte celý tento repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svého GitHub účtu, abyste mohli měnit kód a plnit úkoly. Můžete také [označit hvězdičkou (🌟) tento repozitář](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste jej a související repozitáře snadněji našli.

### 2. Vytvořte Codespace

Aby se předešlo problémům se závislostmi při spuštění kódu, doporučujeme spustit tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ve vašem forku: **Code -> Codespaces -> New on main**

![Dialog zobrazující tlačítka pro vytvoření Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Přidejte tajný klíč

1. ⚙️ Ikona ozubeného kola -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.
2. Pojmenujte OPENAI_API_KEY, vložte svůj klíč, Uložte.

### 3. Co dál?

| Chci…               | Přejít na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Začít lekci 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracovat offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Nastavit poskytovatele LLM | [`providers.md`](03-providers.md)                                        |
| Seznámit se s ostatními studenty | [Připojte se k našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Řešení problémů

| Příznak                                   | Řešení                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Sestavení kontejneru trvá > 10 minut      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminál se nepřipojil; klikněte **+** ➜ *bash*                 |
| `401 Unauthorized` od OpenAI              | Nesprávný / vypršel `OPENAI_API_KEY`                            |
| VS Code ukazuje “Dev container mounting…” | Obnovte záložku prohlížeče—Codespaces někdy ztrácí připojení    |
| Chybí jádro notebooku                     | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiném editoru). Přidejte následující řádek do souboru, nahraďte `your_github_token_here` svým skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete textový editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste to ještě neudělali, budete muset nainstalovat balíček `python-dotenv`, aby se environmentální proměnné ze souboru `.env` načetly do vaší Python aplikace. Můžete jej nainstalovat pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte environmentální proměnné ve svém Python skriptu**: Ve svém Python skriptu použijte balíček `python-dotenv` k načtení environmentálních proměnných ze souboru `.env`:

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

## Jak spustit lokálně na vašem počítači

Abyste mohli kód spustit lokálně na svém počítači, budete potřebovat nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Poté, abyste mohli používat repozitář, je třeba jej naklonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte vše staženo, můžete začít!

## Volitelné kroky

### Instalace Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků.
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Je také užitečný pro instalaci balíčků, které nejsou dostupné přes `pip`.

Můžete postupovat podle [instalačního průvodce MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), abyste jej nastavili.

Po instalaci Miniconda je třeba naklonovat [repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (pokud jste to ještě neudělali).

Dále je třeba vytvořit virtuální prostředí. K tomu použijte Conda a vytvořte nový soubor prostředí (_environment.yml_). Pokud postupujete podle pokynů v Codespaces, vytvořte tento soubor ve složce `.devcontainer`, tedy `.devcontainer/environment.yml`.

Vyplňte svůj soubor prostředí následujícím úryvkem:

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

Pokud narazíte na chyby při používání conda, můžete ručně nainstalovat knihovny Microsoft AI pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje potřebné závislosti. `<environment-name>` označuje název, který chcete použít pro své Conda prostředí, a `<python-version>` je verze Pythonu, kterou chcete použít, například `3` je nejnovější hlavní verze Pythonu.

Jakmile to dokončíte, můžete vytvořit své Conda prostředí spuštěním následujících příkazů v příkazovém řádku/terminálu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pokud narazíte na problémy, podívejte se na [průvodce prostředími Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Používání Visual Studio Code s rozšířením pro podporu Pythonu

Doporučujeme používat editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pro tento kurz. Toto je však spíše doporučení než nutnost.

> **Poznámka**: Otevřením repozitáře kurzu ve VS Code máte možnost nastavit projekt v rámci kontejneru. To je možné díky [speciální složce `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) nalezené v repozitáři kurzu. Více o tom později.

> **Poznámka**: Jakmile naklonujete a otevřete adresář ve VS Code, automaticky vám bude doporučeno nainstalovat rozšíření pro podporu Pythonu.

> **Poznámka**: Pokud vám VS Code doporučí znovu otevřít repozitář v kontejneru, odmítněte tuto žádost, abyste mohli používat lokálně nainstalovanou verzi Pythonu.

### Používání Jupyteru v prohlížeči

Na projektu můžete pracovat také pomocí [prostředí Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve vašem prohlížeči. Klasický Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytují příjemné vývojové prostředí s funkcemi jako automatické doplňování, zvýraznění kódu atd.

Chcete-li spustit Jupyter lokálně, přejděte do terminálu/příkazového řádku, přesuňte se do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím se spustí instance Jupyteru a URL pro přístup k ní bude zobrazena v okně příkazového řádku.

Jakmile přistoupíte k URL, měli byste vidět osnovu kurzu a být schopni navigovat k jakémukoliv souboru `*.ipynb`. Například `08-building-search-applications/python/oai-solution.ipynb`.

### Spuštění v kontejneru

Alternativou k nastavení všeho na vašem počítači nebo Codespace je použití [kontejneru](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Speciální složka `.devcontainer` v repozitáři kurzu umožňuje VS Code nastavit projekt v rámci kontejneru. Mimo Codespaces to bude vyžadovat instalaci Dockeru, což je poměrně náročné, takže to doporučujeme pouze těm, kteří mají zkušenosti s prací s kontejnery.

Jedním z nejlepších způsobů, jak udržet vaše API klíče v bezpečí při používání GitHub Codespaces, je použití Codespace Secrets. Postupujte podle [průvodce správou tajných klíčů Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), abyste se dozvěděli více.

## Lekce a technické požadavky

Kurz obsahuje 6 konceptuálních lekcí a 6 lekcí zaměřených na kódování.

Pro lekce zaměřené na kódování používáme službu Azure OpenAI. Abyste mohli spustit tento kód, budete potřebovat přístup ke službě Azure OpenAI a API klíč. Můžete požádat o přístup [vyplněním této žádosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Zatímco čekáte na zpracování vaší žádosti, každá lekce zaměřená na kódování obsahuje také soubor `README.md`, kde si můžete prohlédnout kód a výstupy.

## Používání služby Azure OpenAI poprvé

Pokud je to poprvé, co pracujete se službou Azure OpenAI, postupujte podle tohoto průvodce, jak [vytvořit a nasadit zdroj služby Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Používání OpenAI API poprvé

Pokud je to poprvé, co pracujete s OpenAI API, postupujte podle průvodce, jak [vytvořit a používat rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními studenty

Vytvořili jsme kanály na našem oficiálním [Discord serveru AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pro setkání s ostatními studenty. Je to skvělý způsob, jak se propojit s ostatními podobně smýšlejícími podnikateli, tvůrci, studenty a každým, kdo se chce zlepšit v Generativní AI.

[![Připojte se k Discord kanálu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektový tým bude také na tomto Discord serveru, aby pomohl studentům.

## Přispějte

Tento kurz je iniciativa s otevřeným zdrojovým kódem. Pokud vidíte oblasti ke zlepšení nebo problémy, vytvořte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo zaregistrujte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektový tým bude sledovat všechny příspěvky. Přispívání do open source je úžasný způsob, jak budovat svou kariéru v Generativní AI.

Většina příspěvků vyžaduje, abyste souhlasili s Licenční smlouvou přispěvatele (CLA), která deklaruje, že máte právo a skutečně udělujete nám práva používat váš příspěvek. Podrobnosti najdete na [webu CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překládání textu v tomto repozitáři se ujistěte, že nepoužíváte strojový překlad. Překlady ověříme prostřednictvím komunity, takže se prosím dobrovolně hlaste k překladům pouze v jazycích, ve kterých jste zdatní.

Když odešlete pull request, CLA-bot automaticky určí, zda je potřeba poskytnout CLA, a označí PR odpovídajícím způsobem (např. štítek, komentář). Jednoduše postupujte podle pokynů poskytovaných botem. Toto budete muset udělat pouze jednou napříč všemi repozitáři používajícími naše CLA.

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte FAQ o Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s jakýmikoliv dalšími otázkami nebo komentáři.

## Začněme!
Nyní, když jste dokončili potřebné kroky k absolvování tohoto kurzu, pojďme začít s [úvodem do generativní AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.