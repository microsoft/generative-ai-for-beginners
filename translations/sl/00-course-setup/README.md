<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T01:41:14+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Začetek tega tečaja

Zelo smo navdušeni, da začnete ta tečaj in vidimo, kaj vas bo navdihnilo za ustvarjanje z generativno umetno inteligenco!

Da zagotovimo vaš uspeh, ta stran opisuje korake za nastavitev, tehnične zahteve in kje poiskati pomoč, če jo potrebujete.

## Koraki za nastavitev

Za začetek tega tečaja morate izvesti naslednje korake.

### 1. Forkajte ta repozitorij

[Forkajte celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) v svoj GitHub račun, da boste lahko spreminjali kodo in dokončali izzive. Prav tako lahko [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga lažje najdete skupaj s povezanimi repozitoriji.

### 2. Ustvarite Codespace

Da se izognete težavam z odvisnostmi pri zagonu kode, priporočamo, da ta tečaj izvajate v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

V vašem fork-u: **Code -> Codespaces -> New on main**

![Dialog, ki prikazuje gumbe za ustvarjanje Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Dodajte skrivnost

1. ⚙️ Ikona zobnika -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Ime OPENAI_API_KEY, prilepite svoj ključ, Shrani.

### 3. Kaj sledi?

| Želim…              | Pojdi na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Začeti lekcijo 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Delati brez povezave| [`setup-local.md`](02-setup-local.md)                                   |
| Nastaviti ponudnika LLM | [`providers.md`](03-providers.md)                                        |
| Spoznati druge učence | [Pridružite se našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Odpravljanje težav

| Simptom                                   | Rešitev                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Gradnja kontejnerja se zatakne > 10 min   | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal ni povezan; kliknite **+** ➜ *bash*                    |
| `401 Unauthorized` od OpenAI              | Napačen / potekel `OPENAI_API_KEY`                              |
| VS Code prikazuje “Dev container mounting…” | Osvežite zavihek brskalnika—Codespaces včasih izgubi povezavo   |
| Manjka jedro za zvezek                    | Meni zvezka ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   Sistemi, ki temeljijo na Unixu:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite datoteko `.env`**: Odprite datoteko `.env` v urejevalniku besedila (npr. VS Code, Notepad++ ali katerem koli drugem urejevalniku). Dodajte naslednjo vrstico v datoteko, pri čemer zamenjajte `your_github_token_here` s svojim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shrani datoteko**: Shranite spremembe in zaprite urejevalnik besedila.

5. **Namestite `python-dotenv`**: Če tega še niste storili, boste morali namestiti paket `python-dotenv`, da naložite okoljske spremenljivke iz datoteke `.env` v svojo Python aplikacijo. Namestite ga lahko z uporabo `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite okoljske spremenljivke v svoj Python skript**: V svojem Python skriptu uporabite paket `python-dotenv`, da naložite okoljske spremenljivke iz datoteke `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno ste ustvarili datoteko `.env`, dodali svoj GitHub žeton in ga naložili v svojo Python aplikacijo.

## Kako zagnati lokalno na svojem računalniku

Za lokalni zagon kode na svojem računalniku morate imeti nameščeno neko različico [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Za uporabo repozitorija ga morate klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imate vse preneseno, lahko začnete!

## Dodatni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za namestitev [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-a, kot tudi nekaj paketov.
Conda je upravitelj paketov, ki omogoča enostavno nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporabna za namestitev paketov, ki niso na voljo prek `pip`.

Sledite [vodniku za namestitev MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), da ga nastavite.

Ko je Miniconda nameščena, morate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (če tega še niste storili).

Nato morate ustvariti virtualno okolje. Če želite to narediti s Conda, ustvarite novo datoteko okolja (_environment.yml_). Če sledite tečaju v Codespaces, jo ustvarite znotraj imenika `.devcontainer`, torej `.devcontainer/environment.yml`.

Datoteko okolja napolnite z naslednjim delčkom kode:

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

Če naletite na napake pri uporabi conda, lahko ročno namestite Microsoft AI knjižnice z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa potrebne odvisnosti. `<environment-name>` se nanaša na ime, ki ga želite uporabiti za svoje Conda okolje, in `<python-version>` je različica Python-a, ki jo želite uporabiti, na primer `3`, kar je najnovejša glavna različica Python-a.

Ko to storite, lahko ustvarite svoje Conda okolje z naslednjimi ukazi v ukazni vrstici/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Če naletite na težave, si oglejte [vodnik za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code z razširitvijo za podporo Python-a

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za podporo Python-a](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. To je sicer bolj priporočilo kot pa zahteva.

> **Opomba**: Z odpiranjem repozitorija tečaja v VS Code imate možnost nastaviti projekt znotraj kontejnerja. To je mogoče zaradi [posebnega imenika `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), ki ga najdete v repozitoriju tečaja. Več o tem kasneje.

> **Opomba**: Ko klonirate in odprete imenik v VS Code, vam bo samodejno predlagal namestitev razširitve za podporo Python-a.

> **Opomba**: Če vam VS Code predlaga, da ponovno odprete repozitorij v kontejnerju, zavrnite to zahtevo, da uporabite lokalno nameščeno različico Python-a.

### Uporaba Jupyterja v brskalniku

Na projektu lahko delate tudi z uporabo [okolja Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ponujata prijetno razvojno okolje s funkcijami, kot so samodejno dokončanje, označevanje kode itd.

Za zagon Jupyterja lokalno pojdite v terminal/ukazno vrstico, se pomaknite do imenika tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

To bo zagnalo Jupyter instanco, URL za dostop pa bo prikazan v oknu ukazne vrstice.

Ko dostopate do URL-ja, bi morali videti vsebino tečaja in se lahko premikati do katere koli datoteke `*.ipynb`. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

### Zagon v kontejnerju

Alternativa nastavitvi vsega na vašem računalniku ali v Codespace je uporaba [kontejnerja](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna mapa `.devcontainer` znotraj repozitorija tečaja omogoča, da VS Code nastavi projekt znotraj kontejnerja. Zunaj Codespaces bo to zahtevalo namestitev Dockerja, kar je nekoliko bolj zapleteno, zato to priporočamo le tistim, ki imajo izkušnje z delom s kontejnerji.

Eden najboljših načinov za varno shranjevanje vaših API ključev pri uporabi GitHub Codespaces je uporaba Codespace Secrets. Prosimo, sledite [vodniku za upravljanje skrivnosti v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), da izveste več o tem.

## Lekcije in tehnične zahteve

Tečaj vključuje 6 konceptualnih lekcij in 6 lekcij kodiranja.

Za lekcije kodiranja uporabljamo Azure OpenAI Service. Za zagon te kode boste potrebovali dostop do storitve Azure OpenAI in API ključ. Dostop lahko pridobite z [izpolnitvijo te prijave](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medtem ko čakate na obdelavo vaše prijave, vsaka lekcija kodiranja vključuje tudi datoteko `README.md`, kjer si lahko ogledate kodo in rezultate.

## Uporaba storitve Azure OpenAI prvič

Če prvič delate s storitvijo Azure OpenAI, sledite temu vodniku o tem, kako [ustvariti in namestiti vir storitve Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Uporaba OpenAI API prvič

Če prvič delate z OpenAI API, sledite vodniku o tem, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte druge učence

Na našem uradnem [Discord strežniku AI skupnosti](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) smo ustvarili kanale za spoznavanje drugih učencev. To je odličen način za mreženje z drugimi podobno mislečimi podjetniki, ustvarjalci, študenti in vsemi, ki želijo napredovati v generativni umetni inteligenci.

[![Pridružite se Discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektna ekipa bo prav tako prisotna na tem Discord strežniku, da pomaga učencem.

## Prispevajte

Ta tečaj je odprtokratna pobuda. Če opazite področja za izboljšave ali težave, prosimo, ustvarite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavite [GitHub težavo](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektna ekipa bo spremljala vse prispevke. Prispevanje k odprtokodnim projektom je odličen način za gradnjo vaše kariere v generativni umetni inteligenci.

Večina prispevkov zahteva, da se strinjate s Pogodbo o licenciranju prispevkov (CLA), ki potrjuje, da imate pravico in dejansko podeljujete pravice za uporabo vašega prispevka. Za podrobnosti obiščite [spletno stran CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedila v tem repozitoriju se prepričajte, da ne uporabljate strojnega prevajanja. Prevod bomo preverili prek skupnosti, zato prosimo, da prostovoljno prevajate le v jezike, v katerih ste vešči.

Ko oddate pull request, bo CLA-bot samodejno določil, ali morate predložiti CLA, in ustrezno označil PR (npr. oznaka, komentar). Preprosto sledite navodilom, ki jih zagotovi bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprtokodne projekte](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite pogosta vprašanja o kodeksu ravnanja ali se obrnite na [Email opencode](opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Začnimo!
Zdaj, ko ste zaključili potrebne korake za dokončanje tega tečaja, začnimo z [uvodom v generativno umetno inteligenco in LLM-je](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.