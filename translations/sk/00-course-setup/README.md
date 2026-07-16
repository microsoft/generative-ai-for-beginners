# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a uvidíte, čo vás inšpiruje vytvoriť s pomocou generatívnej umelej inteligencie!

Aby ste boli úspešní, táto stránka uvádza kroky nastavenia, technické požiadavky a miesto, kde môžete získať pomoc, ak to bude potrebné.

## Kroky nastavenia

Na začatie tohto kurzu je potrebné dokončiť nasledujúce kroky.

### 1. Vytvorte si fork tohto repozitára

[Vytvorte si fork celého tohto repozitára](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho vlastného GitHub účtu, aby ste mohli meniť akýkoľvek kód a plniť úlohy. Môžete tiež [označiť tento repozitár hviezdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby ste ho a súvisiace repozitáre našli jednoduchšie.

### 2. Vytvorte Codespace

Aby ste sa vyhli problémom s závislosťami pri spúšťaní kódu, odporúčame spúšťať tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Vo vašom forku: **Code -> Codespaces -> New on main**

![Dialog zobrazujúci tlačidlá pre vytvorenie codespace](../../../translated_images/sk/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Pridajte tajomstvo (secret)

1. ⚙️ Ikona ozubeného kolieska -> Command Pallete -> Codespaces : Manage user secret -> Pridať nové tajomstvo.
2. Názov OPENAI_API_KEY, vložte svoj kľúč, Uložiť.

### 3. Čo ďalej?

| Chcem…             | Prejsť na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Začať Lekciu 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Pracovať offline   | [`setup-local.md`](02-setup-local.md)                                    |
| Nastaviť poskytovateľa LLM | [`providers.md`](03-providers.md)                                    |
| Stretnúť sa s inými študentmi | [Pripojte sa k nášmu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Riešenie problémov


| Príznak                                  | Riešenie                                                      |
|----------------------------------------|----------------------------------------------------------------|
| Stavba kontajnera zablokovaná > 10 min | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`              | Terminál sa nepripojil; kliknite **+** ➜ *bash*                |
| `401 Unauthorized` od OpenAI             | Nesprávny / expirovaný `OPENAI_API_KEY`                         |
| VS Code zobrazuje „Dev container mounting…“ | Aktualizujte záložku prehliadača—Codespaces niekedy stratí spojenie |
| Notebook kernel chýba                    | Ponuka Notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Pre unixové systémy:

   ```bash
   touch .env
   ```

   Pre Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++ alebo inom editore). Pridajte do súboru nasledujúce riadky, pričom nahraďte zástupné znaky za váš skutočný endpoint a kľúč Microsoft Foundry Models (pozri [`providers.md`](03-providers.md) pre získanie týchto údajov):

   > **Poznámka:** GitHub Models (a premenná `GITHUB_TOKEN`) sa na konci júla 2026 ukončí. Namiesto nich používajte [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte `python-dotenv`**: Ak ste to ešte neurobili, budete musieť nainštalovať balík `python-dotenv`, ktorý načíta premenné prostredia zo súboru `.env` do vašej Python aplikácie. Inštalovať ho môžete cez `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Pythone skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načítať premenné prostredia zo súboru .env
   load_dotenv()

   # Prístup k premenným modelov Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je všetko! Úspešne ste vytvorili súbor `.env`, pridali vaše prihlasovacie údaje pre Microsoft Foundry Models a načítali ich do vašej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Ak chcete spustiť kód lokálne na vašom počítači, potrebujete mať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Na použitie repozitára je potom potrebné si ho naklonovať:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď máte všetko stiahnuté, môžete začať!

## Voliteľné kroky

### Inštalácia Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Condy](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu, ako aj niekoľkých balíkov.
Conda samotná je správca balíčkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Tiež je veľmi užitočná pri inštalácii balíkov, ktoré nie sú dostupné cez `pip`.

Môžete sa riadiť [návodom na inštaláciu MiniCondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po inštalácii Minicondy je potrebné naklonovať [repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ak ste to ešte neurobili)

Ďalej je potrebné vytvoriť virtuálne prostredie. Ak to robíte cez Condu, vytvorte nový súbor environment (_environment.yml_). Ak nasledujete kurz pomocou Codespaces, vytvorte ho v adresári `.devcontainer`, teda `.devcontainer/environment.yml`.

Vyplňte súbor environment nasledujúcim útržkom:

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

Ak máte problémy s Condou, môžete manuálne nainštalovať knižnice Microsoft AI pomocou príkazu v termináli nižšie.

```
conda install -c microsoft azure-ai-ml
```

Súbor environment špecifikuje závislosti, ktoré potrebujeme. `<environment-name>` je názov, ktorý chcete použiť pre svoje Conda prostredie, a `<python-version>` je verzia Pythonu, ktorú chcete použiť, napríklad `3` je najnovšia hlavná verzia Pythonu.

Po vytvorení súboru môžete spustiť príkazy na vytvorenie Conda prostredia v príkazovom riadku/termináli

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podriešenie platí len pre nastavenia Codespace
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na správu Conda prostredí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Používanie Visual Studio Code s Python rozšírením

Odporúčame používať editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Toto je však skôr odporúčanie než povinnosť.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt vo vnútri kontajnera. Je to možné vďaka [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitári kurzu. Viac o tom neskôr.

> **Poznámka**: Keď klonujete a otvoríte adresár vo VS Code, automaticky vám navrhne nainštalovať Python support extension.

> **Poznámka**: Ak VS Code navrhne znovu otvoriť repozitár v kontajneri, odmietnite túto možnosť, ak chcete použiť lokálne nainštalovaný Python.

### Používanie Jupyteru v prehliadači

Môžete tiež pracovať na projekte pomocou [Jupyter prostredia](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú veľmi príjemné vývojové prostredie s funkciami ako automatické dopĺňanie, zvýrazňovanie kódu a pod.

Ak chcete spustiť Jupyter lokálne, otvorte terminál/príkazový riadok, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Toto spustí inštanciu Jupyter a URL adresa pre prístup bude zobrazená v okne terminálu.

Po prístupe na URL by ste mali vidieť osnovu kurzu a môžete prechádzať do akéhokoľvek súboru `*.ipynb`. Napríklad, `08-building-search-applications/python/oai-solution.ipynb`.

### Spúšťanie v kontajneri

Alternatívou nastavenia všetkého na vašom počítači alebo v Codespace je použitie [kontajnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Špeciálny `.devcontainer` priečinok v repozitári kurzu umožňuje VS Code nastaviť projekt vo vnútri kontajnera. Mimo Codespaces to vyžaduje inštaláciu Dockeru a pravdupovediac, je to dosť náročné, preto to odporúčame len tým, ktorí majú skúsenosti s kontajnermi.

Jedným z najlepších spôsobov, ako udržať vaše kľúče API v bezpečí pri používaní GitHub Codespaces, je použiť Codespace Secrets. Prosím, prečítajte si [návod na správu tajomstiev v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Lekcie a technické požiadavky

Kurz má 6 teoretických lekcií a 6 programovacích lekcií.

Pre programovacie lekcie používame Azure OpenAI Service. Budete potrebovať prístup k Azure OpenAI službe a API kľúč na spustenie tohto kódu. Môžete požiadať o prístup vyplnením [tohto formulára](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kým čakáte na spracovanie vašej žiadosti, každá programovacia lekcia obsahuje tiež súbor `README.md`, kde si môžete pozrieť kód a výstupy.

## Použitie Azure OpenAI Service prvýkrát

Ak pracujete s Azure OpenAI službou prvýkrát, prosím, postupujte podľa tohto návodu, ako [vytvoriť a nasadiť zdroj Azure OpenAI služby.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použitie OpenAI API prvýkrát

Ak pracujete s OpenAI API prvýkrát, prosím, postupujte podľa návodu, ako [vytvoriť a používať rozhranie.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Stretnite sa s ostatnými študentmi

Vytvorili sme kanály na našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) na stretnutie s inými študentmi. Je to skvelý spôsob, ako nadviazať kontakty s podobne zmýšľajúcimi podnikateľmi, tvorcami, študentmi a s každým, kto chce posunúť svoje znalosti v generatívnej umelej inteligencii.

[![Pripojte sa na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tím projektu bude tiež na tomto Discord serveri, aby pomohol každému študentovi.

## Prispievajte

Tento kurz je open-source iniciatíva. Ak vidíte možnosti na zlepšenie alebo nejaké problémy, vytvorte, prosím, [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo zaregistrujte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tím projektu bude sledovať všetky príspevky. Prispievanie do open-source je skvelý spôsob, ako budovať kariéru v generatívnej umelej inteligencii.

Väčšina príspevkov vyžaduje, aby ste súhlasili s Dohodou o licencii prispievateľa (CLA), ktorá deklaruje, že máte právo a skutočne udeľujete práva na použitie vášho príspevku. Podrobnosti nájdete na stránke [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textov v tomto repozitári sa uistite, že nepoužívate strojový preklad. Preklady budeme overovať cez komunitu, preto sa prosím dobrovoľne prihlasujte len pre jazyky, ktorým dobre rozumiete.

Keď odošlete pull request, CLA-bot automaticky určí, či musíte poskytnúť CLA a označí PR primerane (napr. štítok, komentár). Jednoducho postupujte podľa pokynov bota. Toto budete musieť urobiť iba raz pre všetky repozitáre používajúce našu CLA.


Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte FAQ k Code of Conduct alebo kontaktujte [Email opencode](opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo pripomienkami.

## Poďme začať

Teraz, keď ste vykonali potrebné kroky na dokončenie tohto kurzu, začnime úvodom do [Generatívnej AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->