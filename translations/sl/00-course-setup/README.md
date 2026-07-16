# Začetek s tem tečajem

Veselimo se, da boste začeli ta tečaj in videli, kaj vas bo navdihnilo za ustvarjanje z Generativno AI!

Za zagotovitev vašega uspeha ta stran opiše korake nastavitve, tehnične zahteve in kje poiskati pomoč, če jo potrebujete.

## Koraki nastavitve

Za začetek tega tečaja boste morali opraviti naslednje korake.

### 1. Razvezi ta repozitorij

[Razvezi ta celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj račun GitHub, da boste lahko spreminjali kodo in opravljali izzive. Prav tako lahko [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga boste lažje našli skupaj z drugimi sorodnimi repozitoriji.

### 2. Ustvari codespace

Da bi se izognili težavam z odvisnostmi pri zagonu kode, priporočamo, da ta tečaj izvajate v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

V svojem razvezenem repozitoriju: **Koda -> Codespaces -> Novo na glavnem**

![Dialog, ki prikazuje gumbe za ustvarjanje codespace](../../../translated_images/sl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodaj skrivnost

1. ⚙️ Ikona zobnika -> Ukazna paleta -> Codespaces : Upravljanje uporabniških skrivnosti -> Dodaj novo skrivnost.
2. Ime OPENAI_API_KEY, prilepi svoj ključ, Shrani.

### 3. Kaj sledi?

| Želim...           | Pojdi na...                                                            |
|---------------------|-------------------------------------------------------------------------|
| Začeti lekcijo 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Delati brez povezave | [`setup-local.md`](02-setup-local.md)                                   |
| Nastaviti ponudnika LLM | [`providers.md`](03-providers.md)                                        |
| Spoznati druge udeležence | [Pridruži se našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Reševanje težav


| Simptom                                  | Popravek                                                       |
|------------------------------------------|-----------------------------------------------------------------|
| Gradnja kontejnerja zastala > 10 min     | **Codespaces ➜ “Ponovno zgradi kontejner”**                     |
| `python: command not found`               | Terminal se ni povezal; klikni **+** ➜ *bash*                   |
| `401 Unauthorized` od OpenAI              | Napačen / potekel `OPENAI_API_KEY`                               |
| VS Code prikazuje “Dev container mounting…” | Osveži zavihek brskalnika – Codespaces včasih izgubi povezavo  |
| Jedro zapiska manjka                      | Meni zapiska ➜ **Jedro ▸ Izberi jedro ▸ Python 3**              |

   Sistemi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredi datoteko `.env`**: Odpri datoteko `.env` v urejevalniku besedila (npr. VS Code, Notepad++ ali kateremkoli drugem urejevalniku). V datoteko dodaj spodnje vrstice, pri čemer nadomesti rezervirana mesta z dejanskim končnim naslovom in ključem Microsoft Foundry Models (glej [`providers.md`](03-providers.md) za navodila, kako jih dobiti):

   > **Opomba:** GitHub Models (in spremenljivka `GITHUB_TOKEN`) bosta prenehala delovati konec julija 2026. Namesto tega uporabljajte [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Shrani datoteko**: Shrani spremembe in zapri urejevalnik besedila.

5. **Namesti `python-dotenv`**: Če ga še niste, boste morali namestiti paket `python-dotenv`, da boste lahko naložili spremenljivke okolja iz datoteke `.env` v svojo Python aplikacijo. Namesti ga lahko z ukazom `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naloži spremenljivke okolja v Python skripti**: V svoji Python skripti uporabi paket `python-dotenv` za nalaganje spremenljivk okolja iz datoteke `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Naloži okoljske spremenljivke iz datoteke .env
   load_dotenv()

   # Dostop do spremenljivk Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je to! Uspešno ste ustvarili datoteko `.env`, dodali podatke za Microsoft Foundry Models in jih naložili v svojo Python aplikacijo.

## Kako zagnati lokalno na svojem računalniku

Za lokalni zagon kode na svojem računalniku boste morali imeti nameščeno neko različico [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Nato morate repozitorij klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imate vse pripravljeno, lahko začnete!

## Izbirni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahka namestitvena rešitev za namestitev [Conde](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona in nekaj paketov.
Conda je upravitelj paketov, ki omogoča enostavno nastavljanje in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporaben za nameščanje paketov, ki niso dostopni preko `pip`.

Sledite [navodilom za namestitev MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), da jo nastavite.

Ko je Miniconda nameščen, morate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (če tega še niste storili)

Nato morate ustvariti virtualno okolje. To naredite s pomočjo Conde tako, da ustvarite novo datoteko za okolje (_environment.yml_). Če sledite z uporabo Codespaces, jo ustvarite v imeniku `.devcontainer`, torej `.devcontainer/environment.yml`.

Vstavite naslednjo vsebino v svojo datoteko okolja:

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

Če imate težave z uporabo conde, lahko ročno namestite Microsoft AI knjižnice z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa potrebne odvisnosti. `<environment-name>` je ime, ki ga želite uporabiti za svoje Conda okolje, `<python-version>` pa različica Pythona, ki jo želite uporabiti, na primer `3` je najnovejša glavna različica Pythona.


Ko je to opravljeno, lahko nadaljujete in ustvarite svoje Conda okolje tako, da zaženete spodnje ukaze v ukazni vrstici/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podpot .devcontainer velja samo za nastavitev Codespace
conda activate ai4beg
```

Če naletite na težave, si oglejte [vodnik za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code z razširitvijo za podporo Pythona

Priporočamo uporabo urednika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za podporo Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. Vendar je to bolj priporočilo kot obvezen pogoj

> **Opomba**: Če v VS Code odprete skladišče tečaja, imate možnost, da projekt nastavite znotraj kontejnerja. To je zaradi [posebne mape `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), ki se nahaja v skladišču tečaja. Več o tem kasneje.

> **Opomba**: Ko klonirate in odprete imenik v VS Code, vam bo samodejno predlagal namestitev razširitve za podporo Pythona.

> **Opomba**: Če vam VS Code predlaga ponovno odprtje skladišča v kontejnerju, to zahtevo zavrnite, da boste uporabljali lokalno nameščeno različico Pythona.

### Uporaba Jupyterja v brskalniku

Prav tako lahko delate na projektu z uporabo [Jupyter okolja](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v vašem brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ponujata zelo prijazno razvojno okolje z funkcijami, kot so samodejno dokončanje, poudarjanje kode itd.

Za zagon Jupyterja lokalno odprite terminal/ukazno vrstico, se pomaknite v imenik tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

S tem boste zagnali primer Jupyterja, URL za dostop bo prikazan v oknu ukazne vrstice.

Ko dostopate do URL-ja, bi morali videti pregled tečaja in imeti možnost krmarjenja do katere koli datoteke `*.ipynb`. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

### Zagon znotraj kontejnerja

Alternativa nastavitvi vsega na vašem računalniku ali v Codespace je uporaba [kontejnerja](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna mapa `.devcontainer` v skladišču tečaja omogoča, da VS Code nastavi projekt znotraj kontejnerja. Izven Codespaces bo to zahtevalo namestitev Dockerja, kar je kar zahtevno delo, zato to priporočamo le tistim z izkušnjami dela s kontejnerji.

Eden najboljših načinov za varno shranjevanje vaših API ključev pri uporabi GitHub Codespaces je uporaba Codespace Secrets. Prosimo, sledite [vodniku za upravljanje skrivnosti v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), da se o tem naučite več.


## Lekcije in tehnične zahteve

Tečaj vsebuje 6 konceptualnih lekcij in 6 programerskih lekcij.

Za programerske lekcije uporabljamo Azure OpenAI storitev. Za izvajanje kode boste potrebovali dostop do Azure OpenAI storitve in API ključ. Dostop lahko zaprosite z [izpolnitvijo te prijave](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medtem ko čakate na obdelavo vaše prijave, vsaka programerska lekcija vključuje tudi datoteko `README.md`, kjer si lahko ogledate kodo in rezultate.

## Prva uporaba Azure OpenAI storitve

Če tokrat prvič delate z Azure OpenAI storitvijo, sledite temu vodniku o tem, kako [ustvariti in implementirati Azure OpenAI Service virov.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prva uporaba OpenAI API-ja

Če tokrat prvič delate z OpenAI API-jem, sledite vodniku o tem, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte druge učence

Ustvarili smo kanale na našem uradnem [AI Community Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za srečanja z drugimi učenci. To je odličen način za mreženje z drugimi podjetniki, ustvarjalci, študenti in vsakim, ki želi napredovati na področju generativne umetne inteligence.

[![Pridružite se Discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektna ekipa bo prav tako na tem Discord strežniku na voljo za pomoč učencem.

## Prispevajte

Ta tečaj je odprtokodna pobuda. Če opazite možnosti izboljšav ali težave, prosimo, ustvarite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavite [GitHub problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektna ekipa bo spremljala vse prispevke. Prispevanje v odprto kodo je odličen način za razvoj vaše kariere v generativni umetni inteligenci.

Večina prispevkov zahteva, da se strinjate z Pogodbo o licenci prispevka (CLA), ki potrjuje, da imate pravico in dejansko dajete pravice za uporabo vašega prispevka. Za podrobnosti obiščite [CLA, spletno stran pogodbe o licenci prispevka](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedila v tem repozitoriju prosimo, da ne uporabljate strojnega prevajanja. Prevode bomo preverjali preko skupnosti, zato prosim prevajajte le v jezikih, ki jih obvladate.


Ko oddate pull request, bo CLA-bot samodejno ugotovil, ali morate zagotoviti CLA, in ustrezno označil PR (npr. nalepka, komentar). Preprosto sledite navodilom, ki jih poda bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.


Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprto kodo](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite Pogosta vprašanja o kodeksu ravnanja ali kontaktirajte [Email opencode](opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Začnimo

Zdaj, ko ste opravili potrebne korake za zaključek tega tečaja, začnimo z [uvodom v generativno umetno inteligenco in velike jezikovne modele](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->