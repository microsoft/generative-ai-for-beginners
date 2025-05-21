<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:39:18+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Začetek tega tečaja

Zelo smo navdušeni, da začnete ta tečaj in vidite, kaj vas bo navdihnilo za ustvarjanje z generativno umetno inteligenco!

Da zagotovimo vaš uspeh, ta stran opisuje korake za nastavitev, tehnične zahteve in kje poiskati pomoč, če jo potrebujete.

## Koraki za nastavitev

Za začetek tečaja morate opraviti naslednje korake.

### 1. Forkajte ta repozitorij

[Forkajte celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun, da boste lahko spreminjali kodo in reševali izzive. Lahko tudi [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga boste lažje našli in povezane repozitorije.

### 2. Ustvarite codespace

Da se izognete težavam z odvisnostmi pri izvajanju kode, priporočamo, da ta tečaj izvajate v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To lahko ustvarite tako, da izberete možnost `Code` na vaši forkani različici tega repozitorija in izberete možnost **Codespaces**.

![Dialog, ki prikazuje gumbe za ustvarjanje codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Shranjevanje API ključev

Ohranjanje vaših API ključev varnih in zaščitenih je pomembno pri gradnji kakršnekoli aplikacije. Priporočamo, da ne shranjujete nobenih API ključev neposredno v vaši kodi. Če te podatke zavežete v javni repozitorij, lahko pride do varnostnih težav in celo neželenih stroškov, če jih uporabi zlonamerni akter.
Tukaj je korak-po-korak vodnik o tem, kako ustvariti datoteko `.env` za Python in dodati `GITHUB_TOKEN`:

1. **Navigirajte do svojega projektnega direktorija**: Odprite terminal ali ukazno vrstico in navigirajte do korenskega direktorija vašega projekta, kjer želite ustvariti datoteko `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Ustvarite datoteko `.env`**: Uporabite svoj najljubši urejevalnik besedila za ustvarjanje nove datoteke z imenom `.env`. Če uporabljate ukazno vrstico, lahko uporabite `touch` (on Unix-based systems) or `echo` (na Windows):

   Sistemi, ki temeljijo na Unixu:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Uredite datoteko `.env`**: Odprite datoteko `.env` v urejevalniku besedila (npr. VS Code, Notepad++ ali kateri koli drug urejevalnik). Dodajte naslednjo vrstico v datoteko, zamenjajte `your_github_token_here` z vašim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shranjevanje datoteke**: Shranite spremembe in zaprite urejevalnik besedila.

5. **Namestite paket `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, da naložite okoljske spremenljivke iz datoteke `.env` v vašo Python aplikacijo. Namestite ga lahko z `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite okoljske spremenljivke v vaš Python skript**: V vašem Python skriptu uporabite paket `python-dotenv`, da naložite okoljske spremenljivke iz datoteke `.env`:

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

## Kako lokalno zagnati na vašem računalniku

Za lokalno izvajanje kode na vašem računalniku morate imeti nameščeno neko različico [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Da nato uporabite repozitorij, ga morate klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imate vse preverjeno, lahko začnete!

## Neobvezni koraki 

### Namestitev Miniconda 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahki namestitveni program za namestitev [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, kot tudi nekaj paketov.
Conda sama je upravitelj paketov, ki omogoča enostavno nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporabna za namestitev paketov, ki niso na voljo preko `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Napolnite svojo datoteko okolja z spodnjim odlomkom:

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

Če imate težave pri uporabi conda, lahko ročno namestite Microsoft AI Libraries z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa potrebne odvisnosti. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovejša večja različica Pythona.

Ko je to opravljeno, lahko nadaljujete in ustvarite svoje Conda okolje z izvajanjem spodnjih ukazov v vaši ukazni vrstici/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Če naletite na težave, si oglejte [vodnik za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code z razširitvijo za podporo Python

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za podporo Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. To je sicer bolj priporočilo in ne dokončna zahteva.

> **Opomba**: Z odprtjem repozitorija tečaja v VS Code imate možnost nastaviti projekt v okviru kontejnerja. To je zaradi [posebnega `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija, ki se nahaja znotraj repozitorija tečaja. Več o tem kasneje.

> **Opomba**: Ko klonirate in odprete direktorij v VS Code, vam bo samodejno predlagal namestitev razširitve za podporo Python.

> **Opomba**: Če vam VS Code predlaga ponovno odprtje repozitorija v kontejnerju, zavrnite to zahtevo, da uporabite lokalno nameščeno različico Pythona.

### Uporaba Jupyter v brskalniku

Projekt lahko razvijate tudi z uporabo [okolja Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v vašem brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ponujata prijetno razvojno okolje s funkcijami, kot so samodejno dopolnjevanje, označevanje kode itd.

Za zagon Jupyter lokalno pojdite v terminal/ukazno vrstico, navigirajte do direktorija tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

To bo zagnalo instanco Jupyter in URL za dostop bo prikazan v oknu ukazne vrstice.

Ko dostopate do URL-ja, bi morali videti obris tečaja in se lahko pomikati do katere koli datoteke `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, kjer lahko vidite kodo in rezultate.

## Prva uporaba Azure OpenAI storitve

Če prvič delate z Azure OpenAI storitvijo, prosimo sledite temu vodniku o tem, kako [ustvariti in namestiti vir Azure OpenAI storitve.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prva uporaba OpenAI API-ja

Če prvič delate z OpenAI API-jem, prosimo sledite vodniku o tem, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte druge učence

Ustvarili smo kanale na našem uradnem [AI Community Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za spoznavanje drugih učencev. To je odličen način za mreženje z drugimi podobno mislečimi podjetniki, ustvarjalci, študenti in vsakim, ki želi napredovati v generativni umetni inteligenci.

[![Pridružite se Discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektna ekipa bo prav tako na tem Discord strežniku, da pomaga učencem.

## Prispevajte

Ta tečaj je odprtokodna pobuda. Če vidite področja za izboljšave ali težave, prosimo ustvarite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavite [GitHub težavo](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektna ekipa bo spremljala vse prispevke. Prispevanje k odprti kodi je izjemen način za gradnjo vaše kariere v generativni umetni inteligenci.

Večina prispevkov zahteva, da se strinjate s pogodbo o licenci za prispevanje (CLA), ki potrjuje, da imate pravico in dejansko podeljujete pravice za uporabo vašega prispevka. Za podrobnosti obiščite [spletno stran CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedila v tem repozitoriju prosimo zagotovite, da ne uporabljate strojnega prevajanja. Prevajanja bomo preverili preko skupnosti, zato prosimo, da se prijavite za prevajanje le v jezike, v katerih ste vešči.

Ko oddate pull request, bo CLA-bot samodejno določil, ali morate zagotoviti CLA in ustrezno okrasil PR (npr. oznaka, komentar). Preprosto sledite navodilom, ki jih zagotovi bot. To boste morali storiti le enkrat v vseh repozitorijih, ki uporabljajo naš CLA.

Ta projekt je sprejel [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite FAQ o kodeksu ravnanja ali kontaktirajte [Email opencode](opencode@microsoft.com) z dodatnimi vprašanji ali komentarji.

## Začnimo

Zdaj, ko ste opravili potrebne korake za dokončanje tega tečaja, začnimo z [uvodom v generativno umetno inteligenco in LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku bi moral veljati za avtoritativni vir. Za kritične informacije je priporočljiv profesionalni človeški prevod. Ne odgovarjamo za kakršne koli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.