<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:36:01+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a tešíme sa, čo vás inšpiruje vytvoriť pomocou generatívnej AI!

Aby sme vám zabezpečili úspech, táto stránka obsahuje kroky nastavenia, technické požiadavky a informácie, kde získať pomoc, ak je to potrebné.

## Kroky nastavenia

Na začiatok tohto kurzu budete musieť dokončiť nasledujúce kroky.

### 1. Forknite toto repo

[Forknite celé toto repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho GitHub účtu, aby ste mohli meniť kód a dokončiť výzvy. Môžete tiež [označiť toto repo hviezdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby ste ho a súvisiace repozitáre našli ľahšie.

### 2. Vytvorte codespace

Aby ste sa vyhli problémom so závislosťami pri spúšťaní kódu, odporúčame spustiť tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To môžete vytvoriť výberom možnosti `Code` vo svojej forkovej verzii tohto repozitára a výberom možnosti **Codespaces**.

![Dialóg zobrazujúci tlačidlá na vytvorenie codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Uloženie vašich API kľúčov

Udržiavanie vašich API kľúčov v bezpečí a zabezpečení je dôležité pri budovaní akejkoľvek aplikácie. Odporúčame neukladať žiadne API kľúče priamo v kóde. Zverejnenie týchto údajov v verejnom repozitári môže viesť k bezpečnostným problémom a dokonca k nechceným nákladom, ak ich použije zlý aktér. Tu je krok za krokom, ako vytvoriť súbor `.env` pre Python a pridať `GITHUB_TOKEN`:

1. **Prejdite do adresára vášho projektu**: Otvorte svoj terminál alebo príkazový riadok a prejdite do koreňového adresára vášho projektu, kde chcete vytvoriť súbor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvorte súbor `.env`**: Použite svoj preferovaný textový editor na vytvorenie nového súboru s názvom `.env`. Ak používate príkazový riadok, môžete použiť `touch` (on Unix-based systems) or `echo` (na Windows):

   Systémy založené na Unixe:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++ alebo inom editore). Pridajte nasledujúci riadok do súboru a nahraďte `your_github_token_here` svojím skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte balík `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, aby ste mohli načítať environmentálne premenné zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte environmentálne premenné vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv`, aby ste načítali environmentálne premenné zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

A to je všetko! Úspešne ste vytvorili súbor `.env`, pridali váš GitHub token a načítali ho do vašej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Aby ste mohli kód spustiť lokálne na vašom počítači, budete potrebovať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Potom potrebujete repozitár naklonovať:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď máte všetko stiahnuté, môžete začať!

## Voliteľné kroky 

### Inštalácia Miniconda 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor pre inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíkov. Conda sama o sebe je správca balíkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Tiež sa hodí pri inštalácii balíkov, ktoré nie sú dostupné cez `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Pokračujte a vyplňte svoj environmentálny súbor nasledujúcim úryvkom:

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

Ak narazíte na chyby pri používaní conda, môžete manuálne nainštalovať Microsoft AI Libraries pomocou nasledujúceho príkazu v termináli. 

```
conda install -c microsoft azure-ai-ml
```

Environmentálny súbor špecifikuje závislosti, ktoré potrebujeme. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovšia hlavná verzia Pythonu.

S týmto hotovým môžete pokračovať a vytvoriť svoje Conda prostredie spustením nasledujúcich príkazov vo vašom príkazovom riadku/termináli

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ak narazíte na akékoľvek problémy, pozrite si [príručku o prostrediach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Používanie Visual Studio Code s rozšírením pre podporu Pythonu

Odporúčame použiť editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením pre podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Toto je však skôr odporúčanie a nie definitívna požiadavka.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt v kontajneri. Je to kvôli [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) nachádzajúcemu sa v repozitári kurzu. Viac o tom neskôr.

> **Poznámka**: Po naklonovaní a otvorení adresára vo VS Code vám automaticky navrhne nainštalovať rozšírenie pre podporu Pythonu.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, odmietnite túto žiadosť, aby ste mohli použiť lokálne nainštalovanú verziu Pythonu.

### Používanie Jupyter v prehliadači

Na projekte môžete pracovať aj pomocou [prostredia Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú príjemné vývojové prostredie s funkciami ako automatické dopĺňanie, zvýrazňovanie kódu atď.

Na spustenie Jupyter lokálne, prejdite do terminálu/príkazového riadku, prejdite do adresára kurzu a vykonajte:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Týmto sa spustí inštancia Jupyter a URL na prístup k nej bude zobrazená v okne príkazového riadku.

Keď získate prístup k URL, mali by ste vidieť osnovu kurzu a byť schopní navigovať k akémukoľvek súboru `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, kde môžete zobraziť kód a výstupy.

## Používanie služby Azure OpenAI po prvýkrát

Ak je toto váš prvýkrát pri práci so službou Azure OpenAI, postupujte podľa tejto príručky, ako [vytvoriť a nasadiť zdroj služby Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Používanie OpenAI API po prvýkrát

Ak je toto váš prvýkrát pri práci s OpenAI API, postupujte podľa príručky, ako [vytvoriť a používať rozhranie.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Stretnite sa s ďalšími účastníkmi

Vytvorili sme kanály na našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pre stretnutie s ďalšími účastníkmi. Toto je skvelý spôsob, ako sa spojiť s ďalšími podnikateľmi, tvorcami, študentmi a každým, kto sa chce zlepšiť v generatívnej AI.

[![Pripojte sa k discord kanálu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tím projektu bude tiež na tomto Discord serveri, aby pomohol účastníkom.

## Prispieť

Tento kurz je iniciatíva s otvoreným zdrojovým kódom. Ak vidíte oblasti na zlepšenie alebo problémy, prosím, vytvorte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo zaznamenajte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tím projektu bude sledovať všetky príspevky. Prispievanie do otvoreného zdroja je úžasný spôsob, ako budovať svoju kariéru v generatívnej AI.

Väčšina príspevkov vyžaduje, aby ste súhlasili s dohodou o licencii prispievateľa (CLA), ktorá vyhlasuje, že máte právo a skutočne udeľujete nám práva na používanie vášho príspevku. Pre podrobnosti navštívte [webovú stránku CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textu v tomto repozitári sa uistite, že nepoužívate strojový preklad. Preklady overíme cez komunitu, preto sa prosím hláste len na preklady v jazykoch, v ktorých ste zdatní.

Keď odošlete pull request, CLA-bot automaticky určí, či potrebujete poskytnúť CLA a správne označí PR (napr. označenie, komentár). Stačí sledovať pokyny poskytnuté botom. Toto budete musieť urobiť len raz vo všetkých repozitároch používajúcich našu CLA.

Tento projekt prijal [Kódex správania otvoreného zdrojového kódu spoločnosti Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte FAQ o kódexe správania alebo kontaktujte [Email opencode](opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo komentármi.

## Začnime

Teraz, keď ste dokončili potrebné kroky na absolvovanie tohto kurzu, poďme začať s [úvodom do generatívnej AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.