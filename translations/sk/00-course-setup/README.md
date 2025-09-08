<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:04:20+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Začíname s týmto kurzom

Sme nadšení, že začínate tento kurz a tešíme sa, čo vás inšpiruje vytvoriť pomocou Generatívnej AI!

Aby ste boli úspešní, na tejto stránke nájdete kroky na nastavenie, technické požiadavky a informácie, kde hľadať pomoc, ak ju budete potrebovať.

## Kroky na nastavenie

Aby ste mohli začať s kurzom, je potrebné splniť nasledujúce kroky.

### 1. Forknite tento repozitár

[Forknite celý tento repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho GitHub účtu, aby ste mohli upravovať kód a plniť výzvy. Môžete si ho tiež [označiť hviezdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby ste ho a súvisiace repozitáre ľahšie našli.

### 2. Vytvorte codespace

Aby ste sa vyhli problémom so závislosťami pri spúšťaní kódu, odporúčame absolvovať kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Vo vašom forku: **Code -> Codespaces -> New on main**

![Dialóg zobrazujúci tlačidlá na vytvorenie codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Pridajte tajomstvo

1. ⚙️ Ikona ozubeného kolieska -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Pomenujte OPENAI_API_KEY, vložte svoj kľúč, Uložte.

### 3.  Čo ďalej?

| Chcem…               | Prejsť na…                                                              |
|----------------------|-------------------------------------------------------------------------|
| Začať lekciu 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracovať offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Nastaviť poskytovateľa LLM | [`providers.md`](providers.md)                                   |
| Spoznávať ďalších študentov | [Pripojte sa na Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Riešenie problémov

| Príznak                                   | Riešenie                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Kontajner sa stavia > 10 minút            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminál sa nepripojil; kliknite **+** ➜ *bash*                 |
| `401 Unauthorized` od OpenAI              | Nesprávny / expirovaný `OPENAI_API_KEY`                         |
| VS Code zobrazuje “Dev container mounting…” | Obnovte záložku prehliadača—Codespaces občas stráca spojenie   |
| Chýba kernel v notebooku                  | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++, alebo inom). Pridajte nasledujúci riadok, kde `your_github_token_here` nahradíte vaším skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte editor.

5. **Nainštalujte `python-dotenv`**: Ak ste to ešte neurobili, nainštalujte balík `python-dotenv`, aby ste mohli načítať environmentálne premenné zo súboru `.env` do vašej Python aplikácie. Nainštalujete ho cez `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte environmentálne premenné vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie premenných zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hotovo! Úspešne ste vytvorili súbor `.env`, pridali svoj GitHub token a načítali ho do svojej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Ak chcete spúšťať kód lokálne, potrebujete mať nainštalovaný [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Potom si repozitár naklonujte:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď máte všetko pripravené, môžete začať!

## Voliteľné kroky

### Inštalácia Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíkov.
Conda je správca balíkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Hodí sa aj na inštaláciu balíkov, ktoré nie sú dostupné cez `pip`.

Postupujte podľa [návodu na inštaláciu MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po inštalácii Miniconda si naklonujte [repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ak ste to ešte neurobili).

Ďalej je potrebné vytvoriť virtuálne prostredie. S Conda to spravíte vytvorením nového súboru prostredia (_environment.yml_). Ak pracujete v Codespaces, vytvorte ho v adresári `.devcontainer`, teda `.devcontainer/environment.yml`.

Súbor prostredia naplňte týmto úryvkom:

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

Ak narazíte na chyby pri používaní conda, môžete Microsoft AI knižnice nainštalovať manuálne pomocou nasledujúceho príkazu v termináli.

```
conda install -c microsoft azure-ai-ml
```

Súbor prostredia určuje potrebné závislosti. `<environment-name>` je názov, ktorý chcete použiť pre vaše Conda prostredie, a `<python-version>` je verzia Pythonu, ktorú chcete použiť, napríklad `3` je najnovšia hlavná verzia Pythonu.

Potom môžete vytvoriť Conda prostredie spustením týchto príkazov v príkazovom riadku/termináli

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na Conda prostredia](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Používanie Visual Studio Code s rozšírením pre Python

Odporúčame editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením pre Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Je to však len odporúčanie, nie povinnosť.

> **Note**: Po otvorení repozitára kurzu vo VS Code máte možnosť nastaviť projekt v kontajneri. Je to vďaka [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitári kurzu. Viac o tom neskôr.

> **Note**: Po naklonovaní a otvorení adresára vo VS Code vám editor automaticky navrhne inštaláciu rozšírenia pre Python.

> **Note**: Ak vám VS Code navrhne otvoriť repozitár v kontajneri, odmietnite túto možnosť, aby ste mohli použiť lokálne nainštalovaný Python.

### Používanie Jupyteru v prehliadači

Na projekte môžete pracovať aj v [Jupyter prostredí](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo v prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ponúkajú príjemné vývojové prostredie s funkciami ako automatické dopĺňanie, zvýrazňovanie kódu a pod.

Na spustenie Jupyteru lokálne prejdite do terminálu/príkazového riadku, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Tým spustíte Jupyter a v príkazovom okne sa zobrazí URL na prístup.

Po otvorení URL by ste mali vidieť osnovu kurzu a môžete prechádzať na ľubovoľný súbor `*.ipynb`. Napríklad `08-building-search-applications/python/oai-solution.ipynb`.

### Spúšťanie v kontajneri

Alternatívou k nastavovaniu všetkého na vašom počítači alebo v Codespace je použitie [kontajnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Špeciálny adresár `.devcontainer` v repozitári kurzu umožňuje VS Code nastaviť projekt v kontajneri. Mimo Codespaces je potrebné nainštalovať Docker, čo je trochu zložitejšie, preto to odporúčame len tým, ktorí už majú skúsenosti s kontajnermi.

Jedným z najlepších spôsobov, ako uchovať vaše API kľúče v bezpečí pri používaní GitHub Codespaces, je využitie Codespace Secrets. Viac sa dozviete v [návode na správu tajomstiev v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lekcie a technické požiadavky

Kurz obsahuje 6 koncepčných lekcií a 6 programovacích lekcií.

Na programovacie lekcie používame Azure OpenAI Service. Na spustenie kódu budete potrebovať prístup k Azure OpenAI službe a API kľúč. Prístup môžete získať [vyplnením tejto žiadosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kým čakáte na spracovanie žiadosti, každá programovacia lekcia obsahuje aj súbor `README.md`, kde si môžete pozrieť kód a výstupy.

## Prvé použitie Azure OpenAI Service

Ak s Azure OpenAI službou pracujete prvýkrát, postupujte podľa tohto návodu, ako [vytvoriť a nasadiť Azure OpenAI Service zdroj.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvé použitie OpenAI API

Ak s OpenAI API pracujete prvýkrát, postupujte podľa návodu, ako [vytvoriť a používať rozhranie.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte ďalších študentov

Vytvorili sme kanály na našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), kde sa môžete zoznámiť s ďalšími študentmi. Je to skvelý spôsob, ako sa spojiť s ďalšími podnikateľmi, tvorcami, študentmi a každým, kto sa chce zlepšiť v Generatívnej AI.

[![Pripojte sa na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tím projektu bude tiež na tomto Discord serveri, aby pomohol študentom.

## Prispievajte

Tento kurz je open-source iniciatíva. Ak vidíte možnosti na zlepšenie alebo narazíte na problém, vytvorte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo nahláste [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tím projektu bude sledovať všetky príspevky. Prispievanie do open source je skvelý spôsob, ako si vybudovať kariéru v Generatívnej AI.

Väčšina príspevkov vyžaduje súhlas s Contributor License Agreement (CLA), kde potvrdzujete, že máte právo a skutočne udeľujete práva na použitie vášho príspevku. Viac informácií nájdete na [stránke CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textov v tomto repozitári nepoužívajte strojový preklad. Preklady budeme overovať cez komunitu, preto sa hláste len na jazyky, ktoré ovládate.

Keď odošlete pull request, CLA-bot automaticky zistí, či musíte poskytnúť CLA a označí PR (napr. štítkom, komentárom). Stačí postupovať podľa pokynov bota. Toto stačí spraviť len raz pre všetky repozitáre používajúce náš CLA.

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Viac informácií nájdete v FAQ alebo kontaktujte [Email opencode](opencode@microsoft.com) s ďalšími otázkami či komentármi.

## Poďme na to
Teraz, keď ste dokončili potrebné kroky na absolvovanie tohto kurzu, poďme začať s [úvodom do generatívnej AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho natívnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.