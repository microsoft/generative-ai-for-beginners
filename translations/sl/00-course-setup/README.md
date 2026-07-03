# Začetek s tem tečajem

Zelo smo navdušeni, da začnete ta tečaj in vidite, kaj vas bo navdihnilo za gradnjo z Generativno umetno inteligenco!

Da zagotovimo vaš uspeh, ta stran navaja korake nastavitve, tehnične zahteve in kje poiskati pomoč, če je to potrebno.

## Koraki nastavitve

Za začetek tečaja morate izvesti naslednje korake.

### 1. Razvezi ta repozitorij

[Razveži ta celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) v svoj GitHub račun, da boste lahko spreminjali kodo in dokončali izzive. Prav tako lahko [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga lažje najdete skupaj s sorodnimi repozitoriji.

### 2. Ustvari codespace

Da se izognete težavam z odvisnostmi pri izvajanju kode, priporočamo, da tečaj izvajate v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

V svojem razvejenem repozitoriju: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodaj skrivnost

1. ⚙️ Ikona nastavitev -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Poimenujte OPENAI_API_KEY, prilepite svoj ključ, Shrani.

### 3. Kaj sledi?

| Želim…               | Pojdi na…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Začetek Lekcije 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Delati brez povezave | [`setup-local.md`](02-setup-local.md)                                   |
| Nastaviti ponudnika LLM | [`providers.md`](03-providers.md)                                        |
| Spoznati druge učence | [Pridruži se našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Reševanje težav


| Simptom                                   | Popravek                                                       |
|-------------------------------------------|----------------------------------------------------------------|
| Gradnja vsebnika je zastala > 10 min      | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`               | Terminal ni bil povezan; kliknite **+** ➜ *bash*               |
| `401 Unauthorized` iz OpenAI              | Napačen / potekel `OPENAI_API_KEY`                             |
| VS Code kaže “Dev container mounting…”   | Osvežite zavihek brskalnika—Codespaces kdaj izgubi povezavo    |
| Manjka jedro zvezka                      | Meni zvezka ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Sistemi na osnovi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredi datoteko `.env`**: Odprite datoteko `.env` v tekstovnem urejevalniku (npr. VS Code, Notepad++ ali katerem koli drugem urejevalniku). Dodajte naslednjo vrstico, kjer `your_github_token_here` zamenjajte s svojim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shrani datoteko**: Shrani spremembe in zapri tekstovni urejevalnik.

5. **Namesti `python-dotenv`**: Če še niste, namestite paket `python-dotenv` za nalaganje okoljskih spremenljivk iz datoteke `.env` v vašo Python aplikacijo. Namestite ga lahko prek `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naloži okoljske spremenljivke v vaš Python skript**: V vašem Python skriptu uporabite paket `python-dotenv`, da naložite okoljske spremenljivke iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Naloži okoljske spremenljivke iz .env datoteke
   load_dotenv()

   # Dostop do spremenljivke GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno ste ustvarili `.env` datoteko, dodali svoj GitHub žeton in ga naložili v svojo Python aplikacijo.

## Kako zagnati lokalno na svojem računalniku

Za lokalno izvajanje kode na vašem računalniku morate imeti nameščeno kakšno različico [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Za uporabo repozitorija ga morate nato sklonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imate vse pripravljeno, lahko začnete!

## Neobvezni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za namestitev [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona in nekaj paketov.
Conda je upravitelj paketov, ki olajša nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporabna za namestitev paketov, ki niso dostopni prek `pip`.

Lahko sledite [navodilu za namestitev MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po namestitvi Miniconda morate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (če to še niste storili).

Nato morate ustvariti virtualno okolje. Za to lahko s Conda ustvarite novo datoteko okolja (_environment.yml_). Če sledite navodilom v Codespaces, ustvarite to znotraj mape `.devcontainer`, torej `.devcontainer/environment.yml`.

Napolnite svojo datoteko okolja z naslednjo vsebino:

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

Če se pri uporabi conda pojavljajo napake, lahko ročno namestite Microsoft AI knjižnice s sledečim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa potrebne odvisnosti. `<environment-name>` je ime, ki ga želite uporabiti za svoje Conda okolje, `<python-version>` pa je različica Pythona, ki jo želite imeti, na primer `3` je najnovejša glavna različica Pythona.

Ko je to pripravljeno, lahko s spodnjimi ukazi v terminalu ustvarite Conda okolje.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podpot .devcontainer velja samo za nastavitve Codespace
conda activate ai4beg
```

Če naletite na težave, si oglejte [navodila za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code z razširitvijo za Python

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za podporo Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. Gre za priporočilo, ne obvezen pogoj.

> **Opomba**: Če odprete repozitorij tečaja v VS Code, imate možnost postaviti projekt znotraj vsebnika. To je omogočeno zaradi posebne mape [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitoriju. O tem več kasneje.

> **Opomba**: Ko klonirate in odprete mapo v VS Code, vam bo samodejno predlagal namestitev razširitve za Python.

> **Opomba**: Če vam VS Code predlaga ponovno odpiranje repozitorija v vsebniku, to zahtevo zavrnite, če želite uporabiti lokalno nameščeno različico Pythona.

### Uporaba Jupyter v brskalniku

Projekt lahko upravljate tudi s [Jupyter okoljem](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v vašem brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nudita prijetno razvojno okolje z možnostmi kot so samodejno dokončanje, označevanje kode ipd.

Za zagon Jupyter lokalno odprite terminal/ukazno vrstico, se pomaknite do mape tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

Ta ukaz bo zagnal Jupyter instanco, URL za dostop pa bo prikazan v ukazni vrstici.

Ko dostopate do URL-ja, boste videli načrt tečaja in lahko dostopali do katere koli datoteke `*.ipynb`. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

### Zagon v vsebniku

Alternativa nastavitvi vsega na vašem računalniku ali Codespace je uporaba [vsebnikov](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna mapa `.devcontainer` v repozitoriju omogoča VS Code, da nastavi projekt znotraj vsebnika. Izven Codespaces bo to zahtevalo namestitev Dockerja, in iskreno rečeno, zahteva nekaj dela, zato to priporočamo le tistim z izkušnjami z vsebniki.

Eden najboljših načinov, da ohranite varnost svojih API ključev pri uporabi GitHub Codespaces, je uporaba Codespace Secrets. Prosimo, sledite vodiču za [upravljanje skrivnosti v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) za več informacij.


## Lekcije in tehnične zahteve

Tečaj vsebuje 6 konceptnih in 6 programerskih lekcij.

Za programerske lekcije uporabljamo Azure OpenAI Service. Potrebovali boste dostop do Azure OpenAI storitve in API ključ za zagon kode. Dostop lahko zaprosite tako, da [izpolnite to prijavo](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medtem ko čakate na obdelavo vaše prijave, ima vsaka programerska lekcija tudi `README.md` datoteko, kjer si lahko ogledate kodo in izhode.

## Prvič uporabljate Azure OpenAI Service?

Če prvič delate z Azure OpenAI storitvijo, sledite temu vodiču, kako [ustvariti in namestiti Azure OpenAI Service vir.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvič uporabljate OpenAI API?

Če prvič delate z OpenAI API, sledite vodiču, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte druge učence

Ustvarili smo kanale na našem uradnem [AI Community Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za spoznavanje drugih učencev. To je odličen način za mreženje z drugimi podjetniki, razvijalci, študenti in vsakim, ki želi napredovati na področju Generativne AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektna ekipa bo prav tako na tem Discord strežniku za pomoč učencem.

## Prispevajte

Ta tečaj je odprtokodna iniciativa. Če opazite možnosti za izboljšave ali težave, prosimo, ustvarite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavite [GitHub težavo](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektna ekipa bo spremljala vse prispevke. Prispevanje k odprtokodni kodi je odličen način za razvoj kariere v Generativni AI.

Večina prispevkov zahteva, da se strinjate s Pogodbo o prispevku (CLA), s katero izjavite, da imate pravico in dejansko omogočate uporabo vašega prispevka. Za podrobnosti obiščite [CLA, Contributor License Agreement spletno stran](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju vsebin v tem repozitoriju poskrbite, da ne uporabljate strojnega prevajanja. Prevode bomo preverjali preko skupnosti, zato se prostovoljno prijavite za prevode samo v jezikih, kjer imate ustrezno znanje.

Ko oddate pull request, bo CLA-bot samodejno preveril, ali morate zagotoviti CLA in ustrezno označil PR (npr. z nalepko, komentarjem). Sledite navodilom, ki jih da bot. To boste morali storiti le enkrat za vse repozitorije z našo CLA.

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprtokodno programsko opremo](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite Pogosta vprašanja o kodeksu ravnanja ali kontaktirajte [Email opencode](opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Začnimo!
Zdaj, ko ste zaključili potrebne korake za dokončanje tega tečaja, začnimo z [uvodom v generativno umetno inteligenco in velike jezikovne modele (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo nobene odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->