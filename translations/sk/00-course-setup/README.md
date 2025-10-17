<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T21:55:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Začíname s týmto kurzom

Sme veľmi nadšení, že začínate tento kurz a tešíme sa na to, čo vás inšpiruje vytvoriť s Generatívnou AI!

Aby sme zabezpečili váš úspech, táto stránka obsahuje kroky nastavenia, technické požiadavky a informácie, kde môžete získať pomoc, ak ju budete potrebovať.

## Kroky nastavenia

Aby ste mohli začať tento kurz, musíte dokončiť nasledujúce kroky.

### 1. Forknite tento repozitár

[Urobte fork celého repozitára](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do svojho vlastného GitHub účtu, aby ste mohli meniť kód a plniť výzvy. Môžete tiež [označiť tento repozitár hviezdičkou (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby ste ho a súvisiace repozitáre ľahšie našli.

### 2. Vytvorte Codespace

Aby ste sa vyhli problémom so závislosťami pri spúšťaní kódu, odporúčame vám spustiť tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Vo vašom forku: **Code -> Codespaces -> New on main**

![Dialógové okno zobrazujúce tlačidlá na vytvorenie Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Pridajte tajný kľúč

1. ⚙️ Ikona ozubeného kolesa -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.
2. Názov OPENAI_API_KEY, vložte svoj kľúč, Uložiť.

### 3. Čo ďalej?

| Chcem…              | Prejsť na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Začať lekciu 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracovať offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Nastaviť poskytovateľa LLM | [`providers.md`](03-providers.md)                                        |
| Spojiť sa s ostatnými študentmi | [Pripojiť sa na náš Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Riešenie problémov

| Príznak                                   | Riešenie                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Kontajner sa stavia viac ako 10 minút     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminál sa nepripojil; kliknite **+** ➜ *bash*                 |
| `401 Unauthorized` od OpenAI              | Nesprávny / expirovaný `OPENAI_API_KEY`                         |
| VS Code ukazuje “Dev container mounting…” | Obnovte kartu prehliadača—Codespaces niekedy stráca spojenie    |
| Chýba kernel v notebooku                  | Menu notebooku ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-based systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte súbor `.env`**: Otvorte súbor `.env` v textovom editore (napr. VS Code, Notepad++ alebo akýkoľvek iný editor). Pridajte nasledujúci riadok do súboru, pričom `your_github_token_here` nahraďte vaším skutočným GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte súbor**: Uložte zmeny a zatvorte textový editor.

5. **Nainštalujte `python-dotenv`**: Ak ste tak ešte neurobili, budete musieť nainštalovať balík `python-dotenv`, aby ste mohli načítať environmentálne premenné zo súboru `.env` do vašej Python aplikácie. Môžete ho nainštalovať pomocou `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načítajte environmentálne premenné vo vašom Python skripte**: Vo vašom Python skripte použite balík `python-dotenv` na načítanie environmentálnych premenných zo súboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je všetko! Úspešne ste vytvorili súbor `.env`, pridali váš GitHub token a načítali ho do vašej Python aplikácie.

## Ako spustiť lokálne na vašom počítači

Aby ste mohli spustiť kód lokálne na vašom počítači, budete potrebovať nainštalovanú nejakú verziu [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Potom, aby ste mohli používať repozitár, musíte ho klonovať:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Keď budete mať všetko stiahnuté, môžete začať!

## Voliteľné kroky

### Inštalácia Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je ľahký inštalátor na inštaláciu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu, ako aj niekoľkých balíkov.
Conda je správca balíkov, ktorý uľahčuje nastavenie a prepínanie medzi rôznymi Python [**virtuálnymi prostrediami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíkmi. Je tiež užitočný na inštaláciu balíkov, ktoré nie sú dostupné cez `pip`.

Môžete postupovať podľa [návodu na inštaláciu MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), aby ste ho nastavili.

Po inštalácii Miniconda musíte klonovať [repozitár](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ak ste tak ešte neurobili).

Ďalej musíte vytvoriť virtuálne prostredie. Na to použite Conda a vytvorte nový súbor prostredia (_environment.yml_). Ak postupujete podľa pokynov v Codespaces, vytvorte tento súbor v adresári `.devcontainer`, teda `.devcontainer/environment.yml`.

Naplnite váš súbor prostredia nasledujúcim úryvkom:

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

Súbor prostredia špecifikuje potrebné závislosti. `<environment-name>` označuje názov, ktorý chcete použiť pre vaše Conda prostredie, a `<python-version>` je verzia Pythonu, ktorú chcete použiť, napríklad `3` je najnovšia hlavná verzia Pythonu.

Keď to dokončíte, môžete vytvoriť vaše Conda prostredie spustením nasledujúcich príkazov v príkazovom riadku/termináli:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ak narazíte na problémy, pozrite si [návod na prostredia Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Používanie Visual Studio Code s rozšírením na podporu Pythonu

Odporúčame používať editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainštalovaným [rozšírením na podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pre tento kurz. Toto je však len odporúčanie, nie povinnosť.

> **Poznámka**: Otvorením repozitára kurzu vo VS Code máte možnosť nastaviť projekt v kontajneri. Je to možné vďaka [špeciálnemu adresáru `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) nachádzajúcemu sa v repozitári kurzu. Viac o tom neskôr.

> **Poznámka**: Po klonovaní a otvorení adresára vo VS Code vám automaticky navrhne nainštalovať rozšírenie na podporu Pythonu.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, odmietnite túto požiadavku, aby ste mohli používať lokálne nainštalovanú verziu Pythonu.

### Používanie Jupyter v prehliadači

Na projekte môžete pracovať aj pomocou [prostredia Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) priamo vo vašom prehliadači. Klasický Jupyter aj [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytujú príjemné vývojové prostredie s funkciami ako automatické dopĺňanie, zvýrazňovanie kódu, atď.

Ak chcete spustiť Jupyter lokálne, prejdite do terminálu/príkazového riadku, navigujte do adresára kurzu a spustite:

```bash
jupyter notebook
```

alebo

```bash
jupyterhub
```

Tým sa spustí inštancia Jupyter a URL na prístup k nej sa zobrazí v okne príkazového riadku.

Po prístupe na URL by ste mali vidieť osnovu kurzu a byť schopní navigovať k akémukoľvek súboru `*.ipynb`. Napríklad, `08-building-search-applications/python/oai-solution.ipynb`.

### Spúšťanie v kontajneri

Alternatívou k nastaveniu všetkého na vašom počítači alebo Codespace je použitie [kontajnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Špeciálny adresár `.devcontainer` v repozitári kurzu umožňuje VS Code nastaviť projekt v kontajneri. Mimo Codespaces to bude vyžadovať inštaláciu Dockeru, a úprimne povedané, zahŕňa to trochu práce, takže to odporúčame len tým, ktorí majú skúsenosti s prácou s kontajnermi.

Jedným z najlepších spôsobov, ako udržať vaše API kľúče bezpečné pri používaní GitHub Codespaces, je použitie Codespace Secrets. Prosím, postupujte podľa [návodu na správu tajných kľúčov v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby ste sa dozvedeli viac.

## Lekcie a technické požiadavky

Kurz obsahuje 6 konceptuálnych lekcií a 6 lekcií zameraných na kódovanie.

Pre lekcie zamerané na kódovanie používame Azure OpenAI Service. Na spustenie tohto kódu budete potrebovať prístup k Azure OpenAI Service a API kľúč. Môžete požiadať o prístup [vyplnením tejto žiadosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kým čakáte na spracovanie vašej žiadosti, každá lekcia zameraná na kódovanie obsahuje aj súbor `README.md`, kde si môžete prezrieť kód a výstupy.

## Používanie Azure OpenAI Service po prvýkrát

Ak je to váš prvýkrát, čo pracujete s Azure OpenAI Service, prosím, postupujte podľa tohto návodu na [vytvorenie a nasadenie zdroja Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Používanie OpenAI API po prvýkrát

Ak je to váš prvýkrát, čo pracujete s OpenAI API, prosím, postupujte podľa návodu na [vytvorenie a používanie rozhrania.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spojte sa s ostatnými študentmi

Vytvorili sme kanály na našom oficiálnom [AI Community Discord serveri](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) na stretnutie s ostatnými študentmi. Je to skvelý spôsob, ako sa spojiť s podobne zmýšľajúcimi podnikateľmi, tvorcami, študentmi a každým, kto sa chce zlepšiť v Generatívnej AI.

[![Pripojiť sa na Discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tím projektu bude tiež na tomto Discord serveri, aby pomohol študentom.

## Prispievajte

Tento kurz je iniciatíva otvoreného zdroja. Ak vidíte oblasti na zlepšenie alebo problémy, prosím, vytvorte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) alebo zaznamenajte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tím projektu bude sledovať všetky príspevky. Prispievanie do open source je úžasný spôsob, ako si budovať kariéru v Generatívnej AI.

Väčšina príspevkov vyžaduje, aby ste súhlasili s Licenčnou zmluvou prispievateľa (CLA), ktorá deklaruje, že máte právo a skutočne udeľujete práva na používanie vášho príspevku. Podrobnosti nájdete na [webovej stránke CLA, Licenčná zmluva prispievateľa](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Dôležité: pri prekladaní textu v tomto repozitári sa prosím uistite, že nepoužívate strojový preklad. Preklady overíme prostredníctvom komunity, takže prosím dobrovoľne prekladajte len do jazykov, v ktorých ste zdatní.

Keď odošlete pull request, CLA-bot automaticky určí, či musíte poskytnúť CLA a označí PR vhodne (napr. štítok, komentár). Jednoducho postupujte podľa pokynov poskytnutých botom. Toto budete musieť urobiť len raz vo všetkých repozitároch používajúcich našu CLA.

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pre viac informácií si prečítajte FAQ o Kódexe správania alebo kontaktujte [Email opencode](opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo komentármi.

## Začnime!
Teraz, keď ste dokončili potrebné kroky na absolvovanie tohto kurzu, začnime s [úvodom do generatívnej AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.