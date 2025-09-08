<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:47:35+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Začetek s tem tečajem

Zelo smo veseli, da začenjaš ta tečaj in komaj čakamo, da vidimo, kaj te bo navdihnilo za ustvarjanje z generativno umetno inteligenco!

Da boš uspešen, smo na tej strani zbrali navodila za pripravo, tehnične zahteve in informacije, kje lahko dobiš pomoč, če jo potrebuješ.

## Koraki za pripravo

Za začetek tečaja moraš opraviti naslednje korake.

### 1. Forkaj ta repozitorij

[Forkaj celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) v svoj GitHub račun, da boš lahko spreminjal kodo in reševal izzive. Lahko tudi [dodaš zvezdico (🌟) temu repozitoriju](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga boš lažje našel skupaj s sorodnimi repozitoriji.

### 2. Ustvari codespace

Da se izogneš težavam z odvisnostmi pri poganjanju kode, priporočamo, da tečaj opravljaš v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

V svojem forku: **Code -> Codespaces -> New on main**

![Pogovorno okno z gumbi za ustvarjanje codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Dodaj skrivnost

1. ⚙️ Ikona zobnika -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Poimenuj OPENAI_API_KEY, prilepi svoj ključ, Shrani.

### 3.  Kaj sledi?

| Želim ...           | Pojdi na ...                                                             |
|---------------------|--------------------------------------------------------------------------|
| Začni z lekcijo 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Delo brez povezave  | [`setup-local.md`](02-setup-local.md)                                    |
| Nastavi ponudnika LLM | [`providers.md`](providers.md)                                         |
| Spoznaj druge udeležence | [Pridruži se Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Reševanje težav

| Simptom                                   | Rešitev                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| Gradnja kontejnerja traja več kot 10 min  | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Terminal se ni povezal; klikni **+** ➜ *bash*                    |
| `401 Unauthorized` iz OpenAI              | Napačen / potekel `OPENAI_API_KEY`                               |
| VS Code prikazuje “Dev container mounting…” | Osveži zavihek brskalnika—Codespaces včasih izgubi povezavo      |
| Manjka jedro za Notebook                  | Meni Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Sistemi na osnovi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredi datoteko `.env`**: Odpri datoteko `.env` v urejevalniku besedila (npr. VS Code, Notepad++ ali katerem koli drugem urejevalniku). Dodaj naslednjo vrstico v datoteko, pri tem zamenjaj `your_github_token_here` s svojim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shrani datoteko**: Shrani spremembe in zapri urejevalnik besedila.

5. **Namesti `python-dotenv`**: Če še nisi, moraš namestiti paket `python-dotenv`, da boš lahko naložil okoljske spremenljivke iz datoteke `.env` v svojo Python aplikacijo. Namestiš ga lahko s `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naloži okoljske spremenljivke v svojem Python skriptu**: V svojem Python skriptu uporabi paket `python-dotenv`, da naložiš okoljske spremenljivke iz datoteke `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno si ustvaril datoteko `.env`, dodal svoj GitHub žeton in ga naložil v svojo Python aplikacijo.

## Kako poganjati lokalno na svojem računalniku

Da boš kodo poganjal lokalno na svojem računalniku, moraš imeti nameščeno neko različico [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Za uporabo repozitorija ga moraš najprej klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imaš vse pripravljeno, lahko začneš!

## Dodatni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python in nekaj paketov.
Conda je upravljalnik paketov, ki olajša nastavitev in preklapljanje med različnimi [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporaben za namestitev paketov, ki niso na voljo prek `pip`.

Sledi [navodilom za namestitev MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), da ga nastaviš.

Ko imaš Minicondo nameščeno, moraš klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (če ga še nisi).

Nato moraš ustvariti virtualno okolje. Če uporabljaš Condo, ustvari novo datoteko okolja (_environment.yml_). Če slediš navodilom v Codespaces, jo ustvari v mapi `.devcontainer`, torej `.devcontainer/environment.yml`.

V datoteko okolja dodaj spodnji izsek:

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

Če naletiš na napake pri uporabi conde, lahko Microsoftove AI knjižnice ročno namestiš z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa potrebne odvisnosti. `<environment-name>` je ime, ki ga želiš uporabiti za svoje Conda okolje, `<python-version>` pa je različica Pythona, ki jo želiš uporabiti, na primer, `3` je najnovejša glavna različica Pythona.

Ko to opraviš, lahko ustvariš svoje Conda okolje z naslednjimi ukazi v ukazni vrstici/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Če naletiš na težave, si oglej [navodila za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code z razširitvijo za Python

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. To je priporočilo, ni pa nujno.

> **Note**: Če odpreš repozitorij tečaja v VS Code, lahko projekt nastaviš v kontejnerju. To omogoča posebna mapa [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitoriju tečaja. Več o tem kasneje.

> **Note**: Ko kloniraš in odpreš mapo v VS Code, ti bo program samodejno predlagal namestitev razširitve za Python.

> **Note**: Če ti VS Code predlaga, da ponovno odpreš repozitorij v kontejnerju, to zavrni, da boš uporabljal lokalno nameščeno različico Pythona.

### Uporaba Jupyterja v brskalniku

Projekt lahko razvijaš tudi v [Jupyter okolju](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ponujata prijetno razvojno okolje s funkcijami, kot so samodejno dopolnjevanje, poudarjanje kode itd.

Za zagon Jupyterja lokalno pojdi v terminal/ukazno vrstico, se premakni v mapo tečaja in zaženi:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

S tem boš zagnal Jupyter in URL za dostop bo prikazan v oknu ukazne vrstice.

Ko odpreš URL, boš videl strukturo tečaja in se lahko premikaš do katerekoli datoteke `*.ipynb`. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

### Poganjanje v kontejnerju

Alternativa nastavitvi na računalniku ali v Codespace je uporaba [kontejnerja](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna mapa `.devcontainer` v repozitoriju tečaja omogoča, da VS Code projekt nastavi v kontejnerju. Če ne uporabljaš Codespaces, boš moral namestiti Docker, kar zahteva nekaj dodatnega dela, zato to priporočamo le tistim, ki imajo izkušnje z delom v kontejnerjih.

Eden najboljših načinov za varno shranjevanje API ključev pri uporabi GitHub Codespaces je uporaba Codespace Secrets. Sledi [navodilom za upravljanje Codespaces skrivnosti](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), da izveš več o tem.

## Lekcije in tehnične zahteve

Tečaj vsebuje 6 konceptualnih lekcij in 6 programerskih lekcij.

Za programerske lekcije uporabljamo Azure OpenAI Service. Za poganjanje kode boš potreboval dostop do Azure OpenAI storitve in API ključ. Dostop lahko pridobiš tako, da [izpolniš prijavo](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medtem ko čakaš na obdelavo prijave, ima vsaka programerska lekcija tudi datoteko `README.md`, kjer si lahko ogledaš kodo in rezultate.

## Prvič uporabljaš Azure OpenAI Service

Če prvič delaš z Azure OpenAI storitvijo, sledi navodilom, kako [ustvariš in namestiš Azure OpenAI Service vir.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvič uporabljaš OpenAI API

Če prvič delaš z OpenAI API, sledi navodilom, kako [ustvariš in uporabljaš vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznaj druge udeležence

Ustvarili smo kanale na uradnem [AI Community Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), kjer lahko spoznaš druge udeležence. To je odlična priložnost za mreženje z drugimi podjetniki, razvijalci, študenti in vsemi, ki želijo napredovati v generativni umetni inteligenci.

[![Pridruži se Discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ekipa projekta bo prav tako prisotna na tem Discord strežniku in bo pomagala udeležencem.

## Prispevaj

Ta tečaj je odprtokratna pobuda. Če opaziš možnosti za izboljšave ali težave, ustvari [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavi [GitHub težavo](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Ekipa projekta bo spremljala vse prispevke. Prispevanje k odprtokodnim projektom je odličen način za razvoj kariere v generativni umetni inteligenci.

Večina prispevkov zahteva, da se strinjaš s Contributor License Agreement (CLA), s katerim potrdiš, da imaš pravico in dejansko dovoljuješ uporabo svojega prispevka. Več informacij najdeš na [spletni strani CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedil v tem repozitoriju ne uporabljaj strojnega prevajanja. Prevod bomo preverili v skupnosti, zato se za prevode prijavi le v jezikih, ki jih resnično obvladaš.

Ko oddaš pull request, bo CLA-bot samodejno preveril, ali moraš podati CLA in ustrezno označil PR (npr. z oznako, komentarjem). Sledi navodilom bota. To moraš storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

Ta projekt je sprejel [Microsoftov odprtokodni kodeks ravnanja](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Več informacij najdeš v pogostih vprašanjih o kodeksu ravnanja ali piši na [Email opencode](opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Začnimo!
Zdaj, ko ste opravili potrebne korake za dokončanje tega tečaja, začnimo z [uvodom v generativno umetno inteligenco in velike jezikovne modele (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.