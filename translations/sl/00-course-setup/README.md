# Začetek tega tečaja

Zelo smo veseli, da boste začeli ta tečaj in videli, kaj vas bo navdihnilo za izdelavo z Generativno AI!

Za zagotovitev vašega uspeha ta stran opisuje korake nastavitve, tehnične zahteve in kje poiskati pomoč, če jo potrebujete.

## Koraki nastavitve

Za začetek tega tečaja boste morali dokončati naslednje korake.

### 1. Razvezi ta repozitorij

[Razvezi celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun, da boste lahko spreminjali kodo in dokončali izzive. Prav tako lahko [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga boste lažje našli skupaj s sorodnimi repozitoriji.

### 2. Ustvari codespace

Da se izognete težavam z odvisnostmi pri zagonu kode, priporočamo, da ta tečaj izvajate v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

V svoji razvezi: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodaj skrivnost

1. ⚙️ Ikona zobnika -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Poimenuj OPENAI_API_KEY, prilepi svoj ključ, Shrani.

### 3. Kaj sledi?

| Želim…             | Pojdi na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Začetek Lekcije 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Delo brez povezave  | [`setup-local.md`](02-setup-local.md)                                   |
| Nastavi ponudnika LLM | [`providers.md`](03-providers.md)                                        |
| Spoznaj druge učence | [Pridruži se našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Odpravljanje težav


| Simptom                                   | Popravek                                                      |
|-------------------------------------------|-------------------------------------------------------------|
| Gradnja kontejnerja se zatakne > 10 min  | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | Terminal ni bil pritrjen; klikni **+** ➜ *bash*              |
| `401 Unauthorized` iz OpenAI              | Napačen / potekel `OPENAI_API_KEY`                            |
| VS Code prikazuje “Dev container mounting…” | Osveži zavihke v brskalniku — Codespaces včasih izgubi povezavo |
| Jedro zvezka manjka                       | Meni zvezka ➜ **Kernel ▸ Izberi jedro ▸ Python 3**            |

   Sistemi na osnovi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredi `.env` datoteko**: Odpri `.env` datoteko v urejevalniku besedila (npr. VS Code, Notepad++ ali kateremkoli urejevalniku). Dodaj naslednje vrstice v datoteko, pri čemer nadomesti nadomestne oznake z dejanskim končnim naslovom in ključem Microsoft Foundry Models (glej [`providers.md`](03-providers.md) za navodila, kako jih pridobiti):

   > **Opomba:** GitHub Models (in njegov spremenljivka `GITHUB_TOKEN`) se upokojita konec julija 2026. Namesto tega uporabljajte [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Shrani datoteko**: Shrani spremembe in zapri urejevalnik besedila.

5. **Namesti `python-dotenv`**: Če še nisi, moraš namestiti paket `python-dotenv`, da naložiš okoljske spremenljivke iz `.env` datoteke v svojo Python aplikacijo. Namesti ga lahko z `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naloži okoljske spremenljivke v svojem Python skriptu**: V svojem Python skriptu uporabi paket `python-dotenv`, da naložiš okoljske spremenljivke iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Naloži spremenljivke okolja iz datoteke .env
   load_dotenv()

   # Dostop do spremenljivk Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je to! Uspešno si ustvaril `.env` datoteko, dodal poverilnice Microsoft Foundry Models in jih naložil v svojo Python aplikacijo.

## Kako pognati lokalno na svojem računalniku

Za zagon kode lokalno na svojem računalniku moraš imeti nameščeno eno od različic [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Da nato uporabiš repozitorij, ga moraš klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imaš vse pripravljeno, lahko začneš!

## Izbirni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahka namestitvena aplikacija za namestitev [Conde](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona in nekaj paketov.
Conda je upravitelj paketov, ki olajša nastavitev in preklapljanje med različnimi [navideznimi okolji](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona in paketi. Prav tako pride prav za namestitev paketov, ki niso na voljo prek `pip`.

Sledi [vodniku za namestitev Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), da jo nastaviš.

Ko imaš nameščen Miniconda, moraš klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (če tega še nisi storil)

Nato moraš ustvariti navidezno okolje. Za to z Condo ustvari novo datoteko okolja (_environment.yml_). Če slediš tečaju z uporabo Codespaces, jo ustvari v mapi `.devcontainer`, torej `.devcontainer/environment.yml`.

Napolni svojo datoteko okolja s spodnjo vsebino:

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

Če pride do napak pri uporabi conde, lahko ročno namestiš Microsoft AI Libraries z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa odvisnosti, ki jih potrebujemo. `<environment-name>` je ime, ki ga želiš uporabiti za svoje Conda okolje, `<python-version>` pa je različica Pythona, ki jo želiš uporabljati, na primer `3` je najnovejša glavna različica Pythona.

Ko to narediš, ustvari Conda okolje tako, da spodnje ukaze zaženeš v ukazni vrstici/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podpot .devcontainer velja samo za nastavitve Codespace
conda activate ai4beg
```

Če naletiš na težave, glej [vodnik za upravljanje Conda okolij](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code s podporo za Python

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) skupaj z [razširitvijo za podporo Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. Vendar je to le priporočilo in ne obvezen pogoj.

> **Opomba**: Z odpiranjem tečajnega repozitorija v VS Code imaš možnost, da projekt nastaviš znotraj kontejnerja. To omogoča posebna mapa [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), ki se nahaja v repozitoriju tečaja. Več o tem kasneje.

> **Opomba**: Ko kloniraš in odpreš imenik v VS Code, ti bo samodejno predlagal namestitev razširitve za podporo Pythonu.

> **Opomba**: Če ti VS Code predlaga, da ponovno odpreš repozitorij znotraj kontejnerja, to zahtevo zavrni, če želiš uporabljati lokalno nameščeno različico Pythona.

### Uporaba Jupyterja v brskalniku

Projekt lahko tudi razvijaš z uporabo [Jupyter okolja](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nudita prijetno razvojno okolje z funkcijami, kot so samodejno dokončanje, osvetlitev kode ipd.

Če želiš zagnati Jupyter lokalno, odpri terminal/ukazno vrstico, pojdi v imenik tečaja in zaženi:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

To bo zagnalo Jupyter instanco, URL za dostop pa bo prikazan v terminalskem oknu.

Ko dostopaš do URL, boš videl načrt tečaja in lahko dostopaš do katere koli datoteke `*.ipynb`. Na primer `08-building-search-applications/python/oai-solution.ipynb`.

### Zagon v kontejnerju

Alternativa nastavitvi vsega na tvojem računalniku ali Codespace-u je uporaba [kontejnerja](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna mapa `.devcontainer` v repozitoriju tečaja omogoča, da VS Code nastavi projekt znotraj kontejnerja. Izven Codespaces bo to zahtevalo namestitev Dockerja, kar je nekoliko zahtevno, zato to priporočamo le izkušenim uporabnikom kontejnerjev.

Eden najboljših načinov za varno shranjevanje API ključev pri uporabi GitHub Codespaces je preko Codespace skrivnosti (Secrets). Prosimo, sledite [vodniku za upravljanje skrivnosti v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) za več informacij.


## Lekcije in tehnične zahteve

Tečaj vsebuje "Learn" lekcije, ki razlagajo koncepte Generativne AI, in "Build" lekcije s praktičnimi primeri kode v **Pythonu** in po potrebi v **TypeScriptu**.

Za lekcije s programiranjem uporabljamo Azure OpenAI v Microsoft Foundry. Potrebuješ naročnino Azure in API ključ. Dostop je odprt - brez potrebe po prijavi - zato lahko [ustvariš Microsoft Foundry vir in razporediš model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), da dobiš svoj končni naslov in ključ.

Vsaka lekcija s kodo vključuje tudi datoteko `README.md`, kjer si lahko ogledaš kodo in rezultate brez zagona.

## Prvič uporabiš Azure OpenAI storitev

Če prvič uporabljaš Azure OpenAI storitev, prosimo, sledi temu vodniku, kako [ustvariti in razporediti Azure OpenAI storitev.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvič uporabiš OpenAI API

Če prvič uporabljaš OpenAI API, sledi vodniku, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznaj druge učence

Ustvarili smo kanale v našem uradnem [AI skupnostnem Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za spoznavanje drugih učencev. To je odličen način za povezovanje z drugimi podjetniki, razvijalci, študenti in vsakim, ki želi nadgraditi svoje znanje Generativne AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektna ekipa bo prav tako na tem Discord strežniku, da pomaga učencem.

## Prispevaj

Ta tečaj je odprtokodna pobuda. Če opaziš možnosti za izboljšave ali težave, prosimo, ustvari [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavi [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektna ekipa bo spremljala vse prispevke. Prispevati odprti kodi je odličen način za razvoj kariere v Generativni AI.

Večina prispevkov zahteva, da se strinjaš z Licenčno pogodbo za prispevke (CLA), ki izjavlja, da imaš pravico in dejansko omogočaš uporabo tvojega prispevka. Za podrobnosti obišči [CLA, Contributor License Agreement spletno stran](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedila v tem repozitoriju prosimo, da ne uporabljaš strojnih prevodov. Prevode bomo preverjali preko skupnosti, zato prosimo, da se prijavite na prevajanje le, če ste v jeziku dovolj spretni.


Ko pošljete pull request, bo CLA-bot samodejno ugotovil, ali morate zagotoviti CLA in ustrezno označil PR (npr. oznaka, komentar). Preprosto sledite navodilom, ki jih poda bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

Ta projekt je sprejel [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite Pogosta vprašanja o kodeksu ravnanja ali se obrnite na [Email opencode](opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Začnimo

Zdaj, ko ste opravili potrebne korake za dokončanje tega tečaja, začnimo z [uvodom v generativno umetno inteligenco in LLM-je](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->