<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:58:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a tešíme sa, čo vás inšpiruje vytvoriť s Generatívnou AI!

Aby sme zabezpečili váš úspech, táto stránka načrtáva kroky nastavenia, technické požiadavky a kde získať pomoc, ak je to potrebné.

## Kroky nastavenia

Na začatie tohto kurzu budete musieť dokončiť nasledujúce kroky.

### 1. Forknite toto repo

[Forknite celý tento repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho vlastného GitHub účtu, aby ste mohli meniť akýkoľvek kód a dokončiť výzvy. Môžete tiež [označiť hviezdičkou (🌟) tento repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pre ľahšie nájdenie a príbuzné repozitáre.

### 2. Vytvorte codespace

Aby ste sa vyhli akýmkoľvek problémom so závislosťami pri spúšťaní kódu, odporúčame spustiť tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Toto môže byť vytvorené výberom možnosti `Code` vo vašej forkovej verzii tohto repo a výberom možnosti **Codespaces**.

![Dialóg ukazujúci tlačidlá na vytvorenie codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Ukladanie vašich API kľúčov

Udržiavanie vašich API kľúčov v bezpečí je dôležité pri vytváraní akéhokoľvek typu aplikácie. Odporúčame neukladať žiadne API kľúče priamo vo vašom kóde. Zverejnenie týchto detailov v verejnom repozitári by mohlo viesť k bezpečnostným problémom a dokonca nechceným nákladom, ak by ich použil zlý aktér.
Tu je krok za krokom návod, ako vytvoriť súbor `.env` pre Python a pridať `GITHUB_TOKEN`:

1. **Navigujte do adresára vášho projektu**: Otvorte svoj terminál alebo príkazový riadok a prejdite do koreňového adresára vášho projektu, kde chcete vytvoriť súbor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvorte súbor `.env`**: Použite svoj obľúbený textový editor na vytvorenie nového súboru s názvom `.env`. Ak používate príkazový riadok, môžete použiť `touch` (on Unix-based systems) or `echo` (na Windows):

   Systémy založené na Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++ alebo akýkoľvek iný editor). Pridajte nasledujúci riadok do súboru, nahradzujúc `your_github_token_here` vaším skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte balíček `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, aby ste načítali environmentálne premenné zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte environmentálne premenné vo vašom Python skripte**: Vo vašom Python skripte použite balíček `python-dotenv` na načítanie environmentálnych premenných zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

A je to! Úspešne ste vytvorili súbor `.env`, pridali svoj GitHub token a načítali ho do svojej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Aby ste mohli spustiť kód lokálne na vašom počítači, budete potrebovať mať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Aby ste potom mohli použiť repozitár, potrebujete ho klonovať:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Akonáhle máte všetko skontrolované, môžete začať!

## Voliteľné kroky

### Inštalácia Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor pre inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu, ako aj niekoľkých balíčkov.
Conda sama o sebe je správca balíčkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčkami. Tiež je užitočná pri inštalácii balíčkov, ktoré nie sú dostupné cez `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Pokračujte a naplňte svoj environmentálny súbor nižšie uvedeným úryvkom:

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

Ak zistíte, že dostávate chyby pri použití conda, môžete manuálne nainštalovať Microsoft AI knižnice pomocou nasledujúceho príkazu v termináli.

```
conda install -c microsoft azure-ai-ml
```

Environmentálny súbor špecifikuje závislosti, ktoré potrebujeme. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovšia hlavná verzia Pythonu.

Keď to máte hotové, môžete pokračovať a vytvoriť svoje Conda prostredie spustením príkazov nižšie vo svojom príkazovom riadku/termináli

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pozrite si [príručku o Conda prostrediach](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), ak narazíte na nejaké problémy.

### Použitie Visual Studio Code s rozšírením pre podporu Pythonu

Odporúčame používať editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením pre podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Toto je však viac odporúčanie a nie definitívna požiadavka.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt v rámci kontajnera. Je to kvôli [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) nájdenému v rámci repozitára kurzu. Viac o tom neskôr.

> **Poznámka**: Akonáhle klonujete a otvoríte adresár vo VS Code, automaticky vám navrhne nainštalovať rozšírenie pre podporu Pythonu.

> **Poznámka**: Ak vám VS Code navrhne znova otvoriť repozitár v kontajneri, odmietnite túto požiadavku, aby ste mohli používať lokálne nainštalovanú verziu Pythonu.

### Použitie Jupyter v prehliadači

Môžete tiež pracovať na projekte pomocou [prostredia Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú príjemné vývojové prostredie s funkciami ako automatické dokončovanie, zvýrazňovanie kódu, atď.

Na spustenie Jupyter lokálne, prejdite do terminálu/príkazového riadku, navigujte do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Týmto sa spustí Jupyter inštancia a URL na prístup k nej bude zobrazená v okne príkazového riadku.

Akonáhle získate prístup k URL, mali by ste vidieť osnovu kurzu a byť schopní navigovať do akéhokoľvek súboru `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, kde môžete zobraziť kód a výstupy.

## Použitie Azure OpenAI služby po prvýkrát

Ak je toto váš prvýkrát, keď pracujete so službou Azure OpenAI, postupujte podľa tohto návodu na [vytvorenie a nasadenie zdroja služby Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použitie OpenAI API po prvýkrát

Ak je toto váš prvýkrát, keď pracujete s OpenAI API, postupujte podľa návodu na [vytvorenie a použitie rozhrania.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Stretnite sa s ostatnými študentmi

Vytvorili sme kanály na našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pre stretnutie s ostatnými študentmi. Toto je skvelý spôsob, ako sa spojiť s inými podnikateľmi, tvorcami, študentmi a každým, kto sa chce zlepšiť v Generatívnej AI.

[![Pripojte sa k discord kanálu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektový tím bude tiež na tomto Discord serveri, aby pomohol akýmkoľvek študentom.

## Prispieť

Tento kurz je iniciatíva otvoreného zdroja. Ak vidíte oblasti na zlepšenie alebo problémy, prosím vytvorte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo zaznamenajte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektový tím bude sledovať všetky príspevky. Prispievanie k otvorenému zdroju je úžasný spôsob, ako budovať svoju kariéru v Generatívnej AI.

Väčšina príspevkov vyžaduje, aby ste súhlasili s Licenčnou zmluvou pre prispievateľov (CLA), v ktorej vyhlasujete, že máte právo a skutočne nám udeľujete práva na použitie vášho príspevku. Pre detaily navštívte [CLA, webová stránka Licenčnej zmluvy pre prispievateľov](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textu v tomto repozitári sa prosím uistite, že nepoužívate strojový preklad. Preklady overíme prostredníctvom komunity, preto sa prosím dobrovoľne hláste na preklady iba v jazykoch, v ktorých ste zdatní.

Keď podáte pull request, CLA-bot automaticky určí, či potrebujete poskytnúť CLA a správne označí PR (napr. štítok, komentár). Jednoducho postupujte podľa pokynov poskytnutých botom. Toto budete musieť urobiť len raz vo všetkých repozitároch používajúcich našu CLA.

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte FAQ kódexu správania alebo kontaktujte [Email opencode](opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo pripomienkami.

## Začnime

Teraz, keď ste dokončili potrebné kroky na dokončenie tohto kurzu, poďme začať s [úvodom do Generatívnej AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.