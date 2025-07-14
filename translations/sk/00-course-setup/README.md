<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:16:26+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a uvidíte, čo vás inšpiruje vytvoriť s Generatívnou AI!

Aby sme vám pomohli uspieť, táto stránka popisuje kroky nastavenia, technické požiadavky a kde získať pomoc, ak ju budete potrebovať.

## Kroky nastavenia

Na začatie tohto kurzu je potrebné dokončiť nasledujúce kroky.

### 1. Vytvorte fork tohto repozitára

[Vytvorte fork celého tohto repozitára](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho GitHub účtu, aby ste mohli meniť kód a plniť úlohy. Môžete si tiež [pridať tento repozitár medzi obľúbené (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby ste ho a súvisiace repozitáre ľahšie našli.

### 2. Vytvorte codespace

Aby ste predišli problémom s knižnicami pri spúšťaní kódu, odporúčame spúšťať tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Codespace vytvoríte výberom možnosti `Code` vo vašom forknutom repozitári a následným výberom **Codespaces**.

![Dialóg zobrazujúci tlačidlá na vytvorenie codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Ukladanie vašich API kľúčov

Je dôležité bezpečne uchovávať vaše API kľúče pri tvorbe akejkoľvek aplikácie. Odporúčame neukladať API kľúče priamo v kóde. Ak by ste ich uložili do verejného repozitára, mohlo by to viesť k bezpečnostným problémom a neželaným nákladom, ak by ich zneužil niekto s nečestnými úmyslami.  
Tu je krok za krokom návod, ako vytvoriť `.env` súbor pre Python a pridať `GITHUB_TOKEN`:

1. **Prejdite do adresára vášho projektu**: Otvorte terminál alebo príkazový riadok a prejdite do koreňového adresára projektu, kde chcete vytvoriť `.env` súbor.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvorte `.env` súbor**: Použite svoj obľúbený textový editor na vytvorenie nového súboru s názvom `.env`. Ak používate príkazový riadok, môžete použiť `touch` (na Unixových systémoch) alebo `echo` (na Windows):

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte `.env` súbor**: Otvorte `.env` súbor v textovom editore (napr. VS Code, Notepad++ alebo inom). Pridajte nasledujúci riadok, pričom `your_github_token_here` nahraďte vaším skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte editor.

5. **Nainštalujte `python-dotenv`**: Ak ste tak ešte neurobili, nainštalujte balík `python-dotenv`, ktorý umožňuje načítavať premenné prostredia zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hotovo! Úspešne ste vytvorili `.env` súbor, pridali GitHub token a načítali ho do vašej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Ak chcete spustiť kód lokálne na vašom počítači, musíte mať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Na použitie repozitára ho najskôr naklonujte:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď máte všetko pripravené, môžete začať!

## Voliteľné kroky

### Inštalácia Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Condy](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíkov.  
Conda je správca balíkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Tiež je užitočná na inštaláciu balíkov, ktoré nie sú dostupné cez `pip`.

Môžete postupovať podľa [návodu na inštaláciu Minicondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po inštalácii Minicondy je potrebné naklonovať [repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ak ste tak ešte neurobili).

Ďalej je potrebné vytvoriť virtuálne prostredie. Ak používate Condu, vytvorte nový súbor prostredia (_environment.yml_). Ak pracujete v Codespaces, vytvorte ho v adresári `.devcontainer`, teda `.devcontainer/environment.yml`.

Vyplňte súbor prostredia nasledujúcim úryvkom:

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

Ak sa pri používaní Condy vyskytnú chyby, môžete manuálne nainštalovať Microsoft AI knižnice pomocou nasledujúceho príkazu v termináli.

```
conda install -c microsoft azure-ai-ml
```

Súbor prostredia špecifikuje závislosti, ktoré potrebujeme. `<environment-name>` je názov, ktorý chcete použiť pre vaše Conda prostredie, a `<python-version>` je verzia Pythonu, ktorú chcete použiť, napríklad `3` je najnovšia hlavná verzia Pythonu.

Keď máte všetko pripravené, vytvorte Conda prostredie spustením nasledujúcich príkazov v príkazovom riadku/termináli:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na správu Conda prostredí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použitie Visual Studio Code s rozšírením pre Python

Odporúčame použiť editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením pre Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Ide však skôr o odporúčanie než povinnosť.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt v kontajneri. Je to vďaka [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitári kurzu. O tom viac neskôr.

> **Poznámka**: Po naklonovaní a otvorení adresára vo VS Code vám editor automaticky navrhne nainštalovať rozšírenie pre Python.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, odmietnite túto ponuku, ak chcete používať lokálne nainštalovaný Python.

### Použitie Jupyter v prehliadači

Projekt môžete tiež vyvíjať pomocou [Jupyter prostredia](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú príjemné vývojové prostredie s funkciami ako automatické dopĺňanie, zvýrazňovanie kódu a podobne.

Na spustenie Jupyter lokálne otvorte terminál/príkazový riadok, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Tým sa spustí inštancia Jupyter a URL adresa na prístup bude zobrazená v okne terminálu.

Po otvorení URL by ste mali vidieť osnovu kurzu a môžete prechádzať do ľubovoľného `*.ipynb` súboru, napríklad `08-building-search-applications/python/oai-solution.ipynb`.

### Spustenie v kontajneri

Alternatívou k nastaveniu všetkého na vašom počítači alebo v Codespace je použitie [kontajnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Špeciálny adresár `.devcontainer` v repozitári kurzu umožňuje VS Code nastaviť projekt v kontajneri. Mimo Codespaces to však vyžaduje inštaláciu Dockeru a celkovo to vyžaduje trochu skúseností, preto to odporúčame len používateľom, ktorí majú skúsenosti s kontajnermi.

Jedným z najlepších spôsobov, ako bezpečne uchovať API kľúče pri používaní GitHub Codespaces, je využitie Codespace Secrets. Pre viac informácií si prečítajte [návod na správu Codespaces tajomstiev](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lekcie a technické požiadavky

Kurz obsahuje 6 teoretických lekcií a 6 programovacích lekcií.

Na programovacie lekcie používame Azure OpenAI Service. Budete potrebovať prístup k Azure OpenAI službe a API kľúč na spustenie kódu. Prístup môžete získať [vyplnením tejto žiadosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kým čakáte na spracovanie vašej žiadosti, každá programovacia lekcia obsahuje aj súbor `README.md`, kde si môžete pozrieť kód a výstupy.

## Použitie Azure OpenAI Service po prvýkrát

Ak pracujete s Azure OpenAI službou prvýkrát, postupujte podľa tohto návodu, ako [vytvoriť a nasadiť Azure OpenAI Service zdroj.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použitie OpenAI API po prvýkrát

Ak pracujete s OpenAI API prvýkrát, postupujte podľa návodu, ako [vytvoriť a používať rozhranie.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte ostatných študentov

Vytvorili sme kanály v našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) na spoznávanie ostatných študentov. Je to skvelý spôsob, ako nadviazať kontakty s ďalšími podnikateľmi, tvorcami, študentmi a každým, kto chce posunúť svoje znalosti v Generatívnej AI na vyššiu úroveň.

[![Pripojiť sa na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tím projektu bude tiež na tomto Discord serveri, aby pomohol všetkým študentom.

## Prispieť

Tento kurz je open-source iniciatíva. Ak vidíte možnosti na zlepšenie alebo chyby, vytvorte prosím [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo nahláste [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tím projektu bude sledovať všetky príspevky. Prispievanie do open source je skvelý spôsob, ako rozvíjať svoju kariéru v Generatívnej AI.

Väčšina príspevkov vyžaduje súhlas s Contributor License Agreement (CLA), ktorý potvrdzuje, že máte právo a skutočne udeľujete práva na použitie vášho príspevku. Pre viac informácií navštívte [web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textov v tomto repozitári sa uistite, že nepoužívate strojový preklad. Preklady budú overované komunitou, preto prosím prekladajte len do jazykov, ktorým dobre rozumiete.

Keď odošlete pull request, CLA-bot automaticky zistí, či je potrebné poskytnúť CLA, a označí PR príslušným štítkom alebo komentárom. Stačí postupovať podľa pokynov bota. Toto je potrebné urobiť len raz pre všetky repozitáre používajúce náš CLA.

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte FAQ k Code of Conduct alebo kontaktujte [Email opencode](opencode@microsoft.com) s ďalšími otázkami či pripomienkami.

## Poďme začať

Keď ste dokončili potrebné kroky na absolvovanie tohto kurzu, poďme začať s [úvodom do Generatívnej AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.