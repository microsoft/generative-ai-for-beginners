# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a uvidíte, čo vás inšpiruje vytvoriť s Generatívnou AI!

Aby sme zabezpečili váš úspech, táto stránka obsahuje kroky nastavenia, technické požiadavky a miesta, kde môžete získať pomoc, ak ju budete potrebovať.

## Kroky nastavenia

Na začatie tohto kurzu je potrebné dokončiť nasledujúce kroky.

### 1. Vytvorte forka tohto repozitára

[Vytvorte forka celého tohto repozitára](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho vlastného GitHub účtu, aby ste mohli meniť kód a dokončiť úlohy. Môžete tiež [pridať tento repozitár do obľúbených (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby ste ho a súvisiace repozitáre ľahšie našli.

### 2. Vytvorte Codespace

Aby ste sa vyhli problémom so závislosťami pri spúšťaní kódu, odporúčame vám spustiť tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Vo vašom forku: **Code -> Codespaces -> New on main**

![Dialóg zobrazujúci tlačidlá na vytvorenie codespace](../../../translated_images/sk/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Pridajte tajný kľúč

1. ⚙️ Ikona ozubeného kolieska -> Command Pallete-> Codespaces : Manage user secret -> Pridať nový tajný kľúč.
2. Názov OPENAI_API_KEY, vložte váš kľúč, Uložiť.

### 3. Čo ďalej?

| Chcem…             | Prejsť na…                                                                   |
|---------------------|-----------------------------------------------------------------------------|
| Začať Lekciu 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)          |
| Pracovať offline    | [`setup-local.md`](02-setup-local.md)                                       |
| Nastaviť poskytovateľa LLM | [`providers.md`](03-providers.md)                                        |
| Stretnúť iných študentov | [Pripojiť sa k nášmu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)        |

## Riešenie problémov


| Symptóm                                   | Riešenie                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Stavba kontajnera uviazla > 10 min        | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                | Terminál sa nepripojil; kliknite na **+** ➜ *bash*               |
| `401 Unauthorized` od OpenAI                | Nesprávny / expirovaný `OPENAI_API_KEY`                         |
| VS Code zobrazuje "Dev container mounting…" | Obnovte kartu prehliadača — Codespaces niekedy stratí pripojenie |
| Chýba jadro notebooku                      | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++, alebo inom editore). Pridajte do súboru nasledujúce riadky, pričom nahraďte zástupné symboly svojim reálnym endpointom a kľúčom Microsoft Foundry Models (pozrite [`providers.md`](03-providers.md) ako ich získať):

   > **Poznámka:** GitHub Models (a jeho premenná `GITHUB_TOKEN`) bude ukončený koncom júla 2026. Namiesto toho používajte [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte `python-dotenv`**: Ak ste tak ešte neurobili, budete potrebovať nainštalovať balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať cez `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte premenné prostredia vo vašom Python skripte**: Vo svojom Python skripte použite balík `python-dotenv` na načítanie premenných prostredia zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Načítajte premenné prostredia zo súboru .env
   load_dotenv()

   # Prístup k premenným Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je všetko! Úspešne ste vytvorili súbor `.env`, pridali prihlasovacie údaje Microsoft Foundry Models a načítali ich do vašej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Ak chcete spustiť kód lokálne na vašom počítači, budete potrebovať mať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Na použitie repozitára ho musíte naklonovať:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď máte všetko naklonované, môžete začať!

## Nepovinné kroky

### Inštalácia Minicondy

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Condy](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a niekoľkých balíčkov.
Conda je správca balíčkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčkami. Tiež je užitočný pre inštaláciu balíčkov, ktoré nie sú dostupné cez `pip`.

Môžete nasledovať [inštalačný návod Minicondy](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) na jej nastavenie.

Po inštalácii Minicondy je potrebné naklonovať [repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ak ste to ešte nespravili).

Ďalej je potrebné vytvoriť virtuálne prostredie. Ak používate Condu, vytvorte nový súbor prostredia (_environment.yml_). Ak používate Codespaces, vytvorte ho v priečinku `.devcontainer`, teda `.devcontainer/environment.yml`.

Vyplňte súbor prostredia nasledujúcim útržkom:

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

Ak dostávate chyby pri použití kondy, môžete manuálne nainštalovať Microsoft AI knižnice pomocou nasledujúceho príkazu v termináli.

```
conda install -c microsoft azure-ai-ml
```

Súbor prostredia určuje závislosti, ktoré potrebujeme. `<environment-name>` je názov vašho Conda prostredia a `<python-version>` je verzia Pythonu, ktorú chcete použiť, napríklad `3` je najnovšia hlavná verzia.

Keď to máte pripravené, vytvorte Conda prostredie spustením príkazov nižšie v príkazovom riadku/termináli

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podcesta platí len pre nastavenia Codespace
conda activate ai4beg
```

Ak narazíte na nejaké problémy, pozrite si [návod na správu Conda prostredí](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použitie Visual Studio Code s rozšírením pre Python

Odporúčame použiť editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením pre Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Toto je však odporúčanie, nie prísna požiadavka.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt vnútri kontajnera. Je to vďaka [špeciálnemu priečinku `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitári kurzu. O tom neskôr.

> **Poznámka**: Po naklonovaní a otvorení adresára vo VS Code vám editor automaticky navrhne inštaláciu rozšírenia pre Python.

> **Poznámka**: Ak VS Code navrhne znovu otvoriť repozitár v kontajneri, odmietnite to pre použitie lokálne nainštalovaného Pythonu.

### Použitie Jupyter v prehliadači

Môžete tiež pracovať na projekte pomocou prostredia [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú príjemné prostredie na vývoj s funkciami ako automatické dokončovanie, zvýrazňovanie kódu a pod.

Na spustenie Jupyter lokálne prejdite do terminálu/príkazového riadku, navigujte do adresára kurzu a vykonajte:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Týmto sa spustí Jupyter inštancia a URL na prístup k nej sa zobrazí v okne príkazového riadku.

Po prístupe na URL by ste mali vidieť osnovu kurzu a môcť navigovať do akéhokoľvek `*.ipynb` súboru. Napríklad `08-building-search-applications/python/oai-solution.ipynb`.

### Spustenie v kontajneri

Alternatívou k nastaveniu všetkého na vašom počítači alebo Codespace je použiť [kontajner](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Špeciálny priečinok `.devcontainer` v repozitári kurzu umožňuje VS Code nastaviť projekt v kontajneri. Mimo Codespaces to vyžaduje inštaláciu Dockeru a pravdupovediac to vyžaduje trochu práce, preto to odporúčame len skúseným používateľom kontajnerov.

Jedným z najlepších spôsobov, ako udržať vaše API kľúče bezpečné pri použití GitHub Codespaces, je používanie Codespace tajomstiev (Secrets). Prosím, postupujte podľa návodu [Manažment tajomstiev v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Lekcie a technické požiadavky

Kurz obsahuje „Learn“ lekcie, ktoré vysvetľujú koncepty Generatívnej AI a „Build“ lekcie s praktickými ukážkami kódu v **Pythone** a **TypeScripte** tam, kde je to možné.

Pre programovanie používame Azure OpenAI v Microsoft Foundry. Budete potrebovať Azure predplatné a API kľúč. Prístup je otvorený - nie je potrebná žiadna žiadosť - takže si môžete [vytvoriť Microsoft Foundry zdroj a nasadiť model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) a získať svoj endpoint a kľúč.

Každá lekcia s kódom obsahuje tiež súbor `README.md`, kde môžete vidieť kód a výstupy bez spustenia čohokoľvek.

## Použitie služby Azure OpenAI prvýkrát

Ak pracujete so službou Azure OpenAI prvýkrát, prosím, postupujte podľa návodu, ako [vytvoriť a nasadiť Azure OpenAI Service zdroj.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použitie OpenAI API prvýkrát

Ak pracujete s OpenAI API prvýkrát, prosím, postupujte podľa návodu, ako [vytvoriť a používať rozhranie.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Stretnúť iných študentov

Vytvorili sme kanály na našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) na stretnutie s inými študentmi. Je to skvelý spôsob, ako nadviazať kontakty s inými podnikateľmi, tvorcami, študentmi a každým, kto chce napredovať v GenAI.

[![Pripojiť sa k discord kanálu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tím projektu bude tiež na tomto Discord serveri k dispozícii na pomoc študentom.

## Prispieť do projektu

Tento kurz je open-source iniciatíva. Ak vidíte miesta na zlepšenie alebo problémy, prosím, vytvorte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo zaznamenajte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tím projektu bude sledovať všetky príspevky. Prispievanie do open source je skvelý spôsob, ako si vybudovať kariéru v Generatívnej AI.

Väčšina príspevkov vyžaduje súhlas s Dohodou o licencii prispievateľa (CLA), ktorá deklaruje, že máte právo a skutočne udeľujete práva na použitie svojho príspevku. Pre podrobnosti navštívte [CLA, Contributor License Agreement webstránku](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri preklade textu v tomto repozitári zabezpečte, že nepoužívate strojový preklad. Preklady budeme overovať cez komunitu, preto sa prosím zapojte do prekladov len v jazykoch, ktorým úplne rozumiete.


Keď odošlete pull request, CLA-bot automaticky určí, či musíte poskytnúť CLA, a vhodne označí PR (napr. štítok, komentár). Jednoducho postupujte podľa inštrukcií, ktoré poskytne bot. Toto budete musieť urobiť iba raz pre všetky repozitáre používajúce náš CLA.

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte Časté otázky o Kodexe správania alebo kontaktujte [Email opencode](opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo pripomienkami.

## Poďme začať

Keďže ste už dokončili potrebné kroky na úspešné absolvovanie tohto kurzu, poďme začať s [úvodom do Generatívnej AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->