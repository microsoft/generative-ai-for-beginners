# Početak rada s ovim tečajem

Jako smo uzbuđeni što ćete započeti ovaj tečaj i vidjeti što ćete biti inspirirani izgraditi s Generativnom AI!

Kako bismo osigurali vaš uspjeh, ova stranica opisuje korake postavljanja, tehničke uvjete i gdje potražiti pomoć ako je potrebna.

## Koraci postavljanja

Za početak ovog tečaja potrebno je dovršiti sljedeće korake.

### 1. Forkajte ovaj Repo

[Forkajte cijeli ovaj repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati kod i dovršavati izazove. Također možete [označiti (🌟) ovaj repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli zajedno sa srodnim repozitorijima.

### 2. Kreirajte codespace

Kako biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo pokretanje ovog tečaja u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

U vašem forku: **Code -> Codespaces -> New on main**

![Dialog koji prikazuje gumbe za kreiranje codespacea](../../../translated_images/hr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodajte secret

1. ⚙️ Ikona zupčanika -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nazovite OPENAI_API_KEY, zalijepite svoj ključ, Spremi.

### 3. Što slijedi?

| Želim…               | Idem na…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Započeti Lekciju 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Raditi offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Postaviti LLM Provider | [`providers.md`](03-providers.md)                                        |
| Upoznati druge učenike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rješavanje problema


| Simptom                                   | Rješenje                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Izgradnja kontejnera traje > 10 minuta    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal nije povezan; kliknite **+** ➜ *bash*                    |
| `401 Unauthorized` od OpenAI              | Pogrešan / istekao `OPENAI_API_KEY`                              |
| VS Code prikazuje “Dev container mounting…” | Osvježite karticu preglednika — Codespaces ponekad gube vezu   |
| Nedostaje kernel u notebooku               | Izbornik notebooka ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-based sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++ ili bilo kojem drugom uređivaču). Dodajte sljedeće retke, zamijenivši oznake stvarnim Microsoft Foundry Models endpointom i ključem (pogledajte [`providers.md`](03-providers.md) za upute kako ih dobiti):

   > **Napomena:** GitHub Models (i njegova varijabla `GITHUB_TOKEN`) prestaju s radom krajem srpnja 2026. Umjesto toga koristite [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako još niste, potrebno je instalirati paket `python-dotenv` kako bi se varijable iz `.env` datoteke učitale u Python aplikaciju. Možete ga instalirati koristeći `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okoline u Python skriptu**: U vašem Python skriptu koristite `python-dotenv` paket za učitavanje varijabli okoline iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Učitaj varijable okoline iz .env datoteke
   load_dotenv()

   # Pristupi Microsoft Foundry Models varijablama
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoje Microsoft Foundry Models vjerodajnice i učitali ih u Python aplikaciju.

## Kako pokrenuti lokalno na vašem računalu

Da biste pokrenuli kod lokalno na svom računalu, potrebno je da imate instaliranu neku verziju [Python-a](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Za korištenje repozitorija potrebno ga je klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kada ste sve dohvatili, možete započeti!

## Neobavezni koraci

### Instalacija Miniconde

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conde](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.
Conda je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni preko `pip`.

Možete pratiti [MiniConda vodič za instalaciju](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

Nakon instalacije Miniconde, trebate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ako već niste).

Zatim trebate kreirati virtualno okruženje. Da biste to učinili koristeći Condu, napravite novu datoteku za okruženje (_environment.yml_). Ako koristite Codespaces, stavite ovu datoteku unutar `.devcontainer` direktorija, dakle `.devcontainer/environment.yml`.

Slobodno popunite svoju datoteku okruženja sljedećim isječkom:

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

Ako dobijete greške pri korištenju conde, možete ručno instalirati Microsoft AI biblioteke pomoću sljedeće naredbe u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okruženja specificira ovisnosti koje trebamo. `<environment-name>` je naziv koji želite koristiti za svoje Conda okruženje, a `<python-version>` je verzija Pythona koju želite koristiti, na primjer, `3` je najnovija glavna verzija Pythona.

Kada je to gotovo, možete kreirati Conda okruženje pokretanjem sljedećih naredbi u komandnoj liniji/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podstaza vrijedi samo za Codespace postavke
conda activate ai4beg
```

Pogledajte [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na bilo kakve probleme.

### Korištenje Visual Studio Code s Python support ekstenzijom

Preporučujemo korištenje [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) uređivača s instaliranom [Python support ekstenzijom](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Ovo je, međutim, samo preporuka, a ne striktni zahtjev.

> **Napomena**: Otvaranjem repozitorija tečaja u VS Code-u imate mogućnost postaviti projekt unutar kontejnera. To je moguće zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija unutar repozitorija tečaja. Više o tome kasnije.

> **Napomena**: Kad klonirate i otvorite direktorij u VS Code-u, automatski će vam se predložiti instalacija Python support ekstenzije.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u kontejneru, odbijte ovaj zahtjev ako želite koristiti lokalno instaliranu verziju Pythona.

### Korištenje Jupyter-a u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direktno u vašem pregledniku. I klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju vrlo ugodno razvojno okruženje s funkcijama poput automatskog dovršavanja, isticanja koda itd.

Da biste pokrenuli Jupyter lokalno, otvorite terminal/komandnu liniju, navigirajte do direktorija tečaja i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu i URL za pristup prikazat će se u prozoru komandne linije.

Nakon što pristupite URL-u, trebali biste vidjeti plan tečaja i moći navigirati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

### Pokretanje u kontejneru

Alternativa postavljanju svega na vašem računalu ili Codespaceu je korištenje [kontejnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna `.devcontainer` mapa unutar repozitorija tečaja omogućuje VS Code-u postavljanje projekta unutar kontejnera. Izvan Codespacesa, to zahtijeva instalaciju Dockera i, iskreno, uključuje određeni posao, stoga to preporučujemo samo onima s iskustvom u radu s kontejnerima.

Jedan od najboljih načina kako zaštititi vaše API ključeve pri korištenju GitHub Codespaces je korištenjem Codespace tajni. Molimo slijedite vodič za [Codespaces upravljanje tajnama](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) za više informacija.


## Lekcije i tehnički uvjeti

Tečaj sadrži 6 konceptualnih lekcija i 6 lekcija programiranja.

Za lekcije programiranja koristimo Azure OpenAI Service. Trebat će vam pristup Azure OpenAI serviceu i API ključ za pokretanje ovog koda. Možete se prijaviti za pristup [ispunjavanjem ove prijave](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Dok čekate obradu svoje prijave, svaka lekcija programiranja uključuje i `README.md` datoteku u kojoj možete pregledati kod i rezultate.

## Prvi put koristite Azure OpenAI Service

Ako prvi put radite s Azure OpenAI servisom, molimo slijedite ovaj vodič o tome kako [kreirati i implementirati Azure OpenAI Service resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvi put koristite OpenAI API

Ako prvi put radite s OpenAI API-jem, molimo slijedite vodič o tome kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge učenike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih učenika. Ovo je izvrstan način za umrežavanje s drugim poduzetnicima, graditeljima, studentima i svima koji žele napredovati u Generativnoj AI.

[![Pridruži se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektni tim će također biti aktivan na ovom Discord serveru kako bi pomogao svim učenicima.

## Doprni

Ovaj tečaj je open-source inicijativa. Ako vidite područja za poboljšanje ili probleme, molimo kreirajte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili otvorite [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektni tim će pratiti sve doprinose. Doprinos open source projektima je izvrstan način za razvoj vaše karijere u Generativnoj AI.

Većina doprinosa zahtijeva da se složite s Contributor License Agreement (CLA) u kojem izjavljujete da imate pravo i zaista dajete nam prava na korištenje vašeg doprinosa. Za detalje posjetite [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: prilikom prevođenja teksta u ovom repozitoriju, molimo osigurajte da ne koristite strojni prijevod. Provjerit ćemo prijevode putem zajednice, stoga se molimo prijavite za prijevode samo za jezike u kojima ste stručni.

Prilikom slanja pull requesta, CLA-bot će automatski odrediti trebate li dostaviti CLA i označiti PR odgovarajuće (npr., oznaka, komentar). Jednostavno slijedite upute koje daje bot. Ovo ćete trebati napraviti samo jednom za sve repozitorije koji koriste naš CLA.


Ovaj projekt je usvojio [Microsoftov Kodeks ponašanja za otvoreni izvor](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ Kodeksa ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) s bilo kakvim dodatnim pitanjima ili komentarima.

## Započnimo

Sada kada ste dovršili potrebne korake za završetak ovog tečaja, započnimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->