<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T09:01:55+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Začetek tega tečaja

Zelo smo navdušeni, da začnete ta tečaj in vidimo, kaj vas bo navdihnilo za ustvarjanje z Generativno umetno inteligenco!

Da bi zagotovili vaš uspeh, ta stran opisuje korake za nastavitev, tehnične zahteve in kje poiskati pomoč, če je potrebna.

## Koraki za nastavitev

Za začetek tega tečaja morate izvesti naslednje korake.

### 1. Forkajte ta repozitorij

[Forkajte celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) v svoj GitHub račun, da boste lahko spreminjali kodo in izpolnjevali izzive. Lahko tudi [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga boste lažje našli skupaj z drugimi povezanimi repozitoriji.

### 2. Ustvarite kodni prostor

Da bi se izognili težavam z odvisnostmi pri izvajanju kode, priporočamo izvajanje tega tečaja v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To lahko ustvarite tako, da izberete možnost `Code` na svoji forkani različici tega repozitorija in izberete možnost **Codespaces**.

![Dialog, ki prikazuje gumbe za ustvarjanje kodnega prostora](../../../00-course-setup/images/who-will-pay.webp)

### 3. Shranjevanje vaših API ključev

Ohranjanje varnosti in zaščite vaših API ključev je pomembno pri ustvarjanju katere koli vrste aplikacije. Priporočamo, da API ključev ne shranjujete neposredno v kodo. Objavljanje teh podatkov v javnem repozitoriju lahko povzroči varnostne težave in celo neželene stroške, če jih uporabi zlonamerna oseba. Tukaj je vodnik po korakih, kako ustvariti datoteko `.env` za Python in dodati `GITHUB_TOKEN`:

1. **Pomik do imenika vašega projekta**: Odprite terminal ali ukazno vrstico in se pomaknite do korenskega imenika vašega projekta, kjer želite ustvariti datoteko `.env`.

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

3. **Uredite datoteko `.env`**: Odprite datoteko `.env` v urejevalniku besedila (npr. VS Code, Notepad++ ali katerem koli drugem urejevalniku). Dodajte naslednjo vrstico v datoteko in zamenjajte `your_github_token_here` s svojim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shrani datoteko**: Shranite spremembe in zaprite urejevalnik besedila.

5. **Namestite paket `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, da naložite okoljske spremenljivke iz datoteke `.env` v svojo Python aplikacijo. Namestite ga lahko z uporabo `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite okoljske spremenljivke v svojem Python skriptu**: V svojem Python skriptu uporabite paket `python-dotenv` za nalaganje okoljskih spremenljivk iz datoteke `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

In to je to! Uspešno ste ustvarili datoteko `.env`, dodali svoj GitHub žeton in ga naložili v svojo Python aplikacijo.

## Kako zagnati lokalno na svojem računalniku

Za lokalno izvajanje kode na svojem računalniku morate imeti nameščeno neko različico [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Če želite nato uporabiti repozitorij, ga morate klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imate vse preneseno, lahko začnete!

## Dodatni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za namestitev [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona in nekaj paketov. Conda sama je upravljalnik paketov, ki olajša nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporabna za namestitev paketov, ki niso na voljo preko `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Izpolnite svojo okoljsko datoteko s spodnjim odlomkom:

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

Če se pojavijo napake pri uporabi conda, lahko ročno namestite knjižnice Microsoft AI z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Okoljska datoteka določa potrebne odvisnosti. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovejša glavna različica Pythona.

Ko je to narejeno, lahko ustvarite svoje Conda okolje z izvajanjem spodnjih ukazov v svoji ukazni vrstici/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Oglejte si [vodnik po Conda okoljih](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), če naletite na težave.

### Uporaba Visual Studio Code z razširitvijo za podporo Pythona

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za podporo Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. To je sicer bolj priporočilo kot pa nujna zahteva.

> **Opomba**: Z odpiranjem repozitorija tečaja v VS Code imate možnost nastavitve projekta znotraj kontejnerja. To je zaradi [posebnega imenika `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), ki se nahaja znotraj repozitorija tečaja. Več o tem kasneje.

> **Opomba**: Ko klonirate in odprete imenik v VS Code, vam bo samodejno predlagano, da namestite razširitev za podporo Pythona.

> **Opomba**: Če vam VS Code predlaga ponovno odpiranje repozitorija v kontejnerju, zavrnite to zahtevo, da boste lahko uporabili lokalno nameščeno različico Pythona.

### Uporaba Jupyter v brskalniku

Na projektu lahko delate tudi z uporabo [okolja Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v vašem brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nudita prijetno razvojno okolje z lastnostmi, kot so samodejno dokončanje, poudarjanje kode itd.

Za začetek Jupyter lokalno pojdite v terminal/ukazno vrstico, se pomaknite do imenika tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

To bo zagnalo Jupyter instanco in URL za dostop bo prikazan v oknu ukazne vrstice.

Ko dostopite do URL-ja, bi morali videti oris tečaja in se lahko pomaknete do katere koli datoteke `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, kjer si lahko ogledate kodo in izhode.

## Uporaba Azure OpenAI storitve prvič

Če prvič delate z Azure OpenAI storitvijo, sledite temu vodniku, kako [ustvariti in uvesti vir Azure OpenAI storitve.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Uporaba OpenAI API prvič

Če prvič delate z OpenAI API, sledite vodniku, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte druge učence

Ustvarili smo kanale v našem uradnem [AI Community Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za srečanje z drugimi učenci. To je odličen način za mreženje z drugimi podjetniki, graditelji, študenti in vsakim, ki želi napredovati v Generativni umetni inteligenci.

[![Pridružite se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektna ekipa bo prav tako prisotna na tem Discord strežniku, da pomaga učencem.

## Prispevajte

Ta tečaj je pobuda odprte kode. Če vidite področja za izboljšave ali težave, ustvarite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavite [GitHub težavo](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektna ekipa bo spremljala vse prispevke. Prispevanje k odprti kodi je odličen način za gradnjo kariere v Generativni umetni inteligenci.

Večina prispevkov zahteva, da se strinjate s Pogodbo o licenciranju prispevkov (CLA), ki izjavlja, da imate pravico in dejansko podelite pravice za uporabo vašega prispevka. Za podrobnosti obiščite [CLA, spletno mesto Pogodbe o licenciranju prispevkov](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedila v tem repozitoriju se prepričajte, da ne uporabljate strojnega prevajanja. Prevajanje bomo preverili preko skupnosti, zato se prostovoljno prijavite za prevode le v jezike, kjer ste vešči.

Ko pošljete zahtevo za združitev, bo CLA-bot samodejno določil, ali morate zagotoviti CLA in ustrezno označil PR (npr. oznaka, komentar). Preprosto sledite navodilom, ki jih zagotovi bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

Ta projekt je sprejel [Kodeks ravnanja odprte kode Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite pogosta vprašanja o kodeksu ravnanja ali se obrnite na [Email opencode](opencode@microsoft.com) z dodatnimi vprašanji ali komentarji.

## Začnimo

Zdaj, ko ste zaključili potrebne korake za dokončanje tega tečaja, začnimo z [uvodom v Generativno umetno inteligenco in LLM-je](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.