# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a uvidíte, čo vás inšpiruje vytvoriť s Generatívnou AI!

Aby sme vám zabezpečili úspech, táto stránka obsahuje kroky nastavenia, technické požiadavky a kde získať pomoc, ak ju budete potrebovať.

## Kroky nastavenia

Na začatie tohto kurzu budete musieť dokončiť nasledovné kroky.

### 1. Vytvorte forknutie tohto repozitára

[Vytvorte forknutie celého tohto repozitára](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj vlastný GitHub účet, aby ste mohli meniť akýkoľvek kód a dokončiť výzvy. Môžete tiež [označiť tento repozitár hviezdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pre ľahšie jeho a príbuzných repozitárov nájdenie.

### 2. Vytvorte codespace

Aby ste sa vyhli problémom so závislosťami pri spúšťaní kódu, odporúčame používať tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Vo svojom forknutí: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sk/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Pridajte tajný kľúč

1. ⚙️ Ikona ozubeného kolieska -> Príkazová paleta -> Codespaces : Spravovať používateľské tajomstvá -> Pridať nové tajomstvo.
2. Názov OPENAI_API_KEY, vložte svoj kľúč, Uložiť.

### 3. Čo ďalej?

| Chcem…              | Ísť na…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Začať Lekciu 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracovať offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Nastaviť poskytovateľa LLM | [`providers.md`](03-providers.md)                                        |
| Spoznávať ostatných študentov | [Pridajte sa k nášmu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Riešenie problémov

| Symptóm                                    | Riešenie                                                        |
|--------------------------------------------|----------------------------------------------------------------|
| Stavba kontajnera zamrznutá > 10 min       | **Codespaces ➜ „Rebuild Container“**                           |
| `python: command not found`                 | Terminál sa nepripojil; kliknite **+** ➜ *bash*                |
| `401 Unauthorized` od OpenAI                | Nesprávny / expirovaný `OPENAI_API_KEY`                       |
| VS Code ukazuje „Dev container mounting…“  | Obnovte záložku prehliadača — Codespaces niekedy stratí spojenie |
| Chýba kernel v Notebooku                    | Menu Notebooku ➜ **Kernel ▸ Vyber Kernel ▸ Python 3**           |

   Systémy založené na Unixe:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++ alebo inom editore). Pridajte nasledujúci riadok do súboru a nahraďte `your_github_token_here` svojim skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte `python-dotenv`**: Ak ste tak ešte nespravili, budete potrebovať nainštalovať balík `python-dotenv`, ktorý načíta premenné prostredia zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načítať premenné prostredia zo súboru .env
   load_dotenv()

   # Prístup k premennej GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je všetko! Úspešne ste vytvorili súbor `.env`, pridali svoj GitHub token a načítali ho do vašej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Ak chcete spustiť kód lokálne na vašom počítači, musíte mať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Na ďalšie použitie repozitára je potrebné ho naklonovať:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď máte všetko pripravené, môžete začať!

## Nepovinné kroky

### Inštalácia Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Condy](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíkov. Conda je manažér balíkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Je tiež užitočná na inštaláciu balíkov, ktoré nie sú dostupné cez `pip`.

Môžete sa riadiť [inštalačným návodom MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) na jej nastavenie.

Po inštalácii Minicondy je potrebné naklonovať [repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ak ste tak ešte nespravili)

Ďalej je potrebné vytvoriť virtuálne prostredie. Na to vytvorte nový súbor prostredia (_environment.yml_). Ak používate Codespaces, vytvorte ho v priečinku `.devcontainer`, teda `.devcontainer/environment.yml`.

Vyplňte svoj súbor prostredia nasledujúcim úryvkom:

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

Ak máte problémy s Condou, môžete manuálne nainštalovať knižnice Microsoft AI pomocou nasledujúceho príkazu v termináli.

```
conda install -c microsoft azure-ai-ml
```

Súbor prostredia špecifikuje závislosti, ktoré potrebujeme. `<environment-name>` označuje názov, ktorý chcete použiť pre svoje Conda prostredie, a `<python-version>` je verzia Pythonu, ktorú chcete použiť, napríklad `3` je najnovšia hlavná verzia Pythonu.

Keď je to hotové, môžete svoje Conda prostredie vytvoriť spustením nasledujúcich príkazov v príkazovom riadku/termináli

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podcesta .devcontainer sa vzťahuje iba na nastavenia Codespace
conda activate ai4beg
```

V prípade problémov si pozrite [návod na prácu s Conda prostrediami](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použitie Visual Studio Code s rozšírením pre Python

Na tento kurz odporúčame používať editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením pre podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Nie je to však povinné, iba odporúčané.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt v kontajneri. Je to možné vďaka [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitári kurzu. Viac o tom neskôr.

> **Poznámka**: Po naklonovaní a otvorení priečinka vo VS Code sa vám automaticky navrhne nainštalovať rozšírenie pre podporu Pythonu.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, odmietnite túto požiadavku, ak chcete používať lokálne nainštalovanú verziu Pythonu.

### Použitie Jupyter v prehliadači

Na projekte môžete pracovať aj pomocou prostredia [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasické Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú príjemné vývojové prostredie s funkciami ako automatické dopĺňanie, zvýrazňovanie kódu a podobne.

Na spustenie Jupyter lokálne otvorte terminál/príkazový riadok, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Týmto sa spustí inštancia Jupyter a URL na prístup k nej bude zobrazená v okne príkazového riadku.

Po zadaní URL by ste mali vidieť osnovu kurzu a môžete prechádzať k akémukoľvek súboru `*.ipynb`. Napríklad `08-building-search-applications/python/oai-solution.ipynb`.

### Spúšťanie v kontajneri

Alternatívou ku nastaveniu všetkého na vašom počítači alebo Codespace je použitie [kontajnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Špeciálny priečinok `.devcontainer` v repozitári kurzu umožňuje VS Code nastaviť projekt v kontajneri. Mimo Codespaces to vyžaduje inštaláciu Dockeru a celkovo to vyžaduje isté skúsenosti s kontajnermi, preto to odporúčame len skúseným používateľom.

Jedným z najlepších spôsobov, ako bezpečne spravovať API kľúče pri používaní GitHub Codespaces, je používať Tajomstvá v Codespaces. Prosím, riaďte sa [návodom na správu tajomstiev v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lekcie a technické požiadavky

Kurz obsahuje 6 konceptuálnych lekcií a 6 kódovacích lekcií.

Pre kódovacie lekcie používame službu Azure OpenAI. Potrebujete mať prístup k Azure OpenAI service a API kľúč na spustenie tohto kódu. Prístup môžete získať vyplnením [tohto formulára](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kým čakáte na spracovanie vašej žiadosti, každá kódovacia lekcia obsahuje tiež súbor `README.md`, kde si môžete prezrieť kód a výstupy.

## Použitie Azure OpenAI služieb prvýkrát

Ak s Azure OpenAI službou pracujete prvýkrát, prosím, riaďte sa týmto návodom, ako [vytvoriť a nasadiť Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použitie OpenAI API prvýkrát

Ak s OpenAI API pracujete prvýkrát, prosím, riaďte sa týmto návodom, ako [vytvoriť a používať rozhranie.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznávať ostatných študentov

Vytvorili sme kanály v našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pre spoznávanie ostatných študentov. Je to skvelý spôsob, ako sa spojiť s inými podnikateľmi, tvorcami, študentmi a každým, kto chce zlepšiť svoje schopnosti v Generatívnej AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektový tím bude tiež na tomto Discord serveri na pomoc študentom.

## Prispievajte

Tento kurz je otvorenou iniciatívou. Ak vidíte možné zlepšenia alebo problémy, prosím, vytvorte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo zaznamenajte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektový tím bude sledovať všetky príspevky. Prispievanie do open source je výborný spôsob, ako rozvíjať svoju kariéru v Generatívnej AI.

Väčšina príspevkov si vyžaduje súhlas so Zmluvou o licencii prispievateľa (CLA), ktorá deklaruje, že máte právo a skutočne udeľujete práva na použitie vášho príspevku. Podrobnosti nájdete na [webovej stránke CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textov v tomto repozitári prosím nepoužívajte strojový preklad. Preklady budeme overovať cez komunitu, preto prosím dobrovoľte prekladať len do jazykov, ktorým rozumiete.

Keď odošlete pull request, CLA-bot automaticky vyhodnotí, či potrebujete dodať CLA a podľa toho PR označí (napr. štítok, komentár). Jednoducho postupujte podľa pokynov bota. Toto stačí urobiť iba raz pre všetky repozitáre využívajúce našu CLA.

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte FAQ k Code of Conduct alebo kontaktujte [Email opencode](opencode@microsoft.com) s akýmikoľvek otázkami či pripomienkami.

## Poďme na to!
Teraz, keď ste dokončili potrebné kroky na absolvovanie tohto kurzu, poďme začať tým, že získame [úvod do Generatívnej AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->