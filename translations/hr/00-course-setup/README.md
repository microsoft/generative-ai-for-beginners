# Početak s ovim tečajem

Vrlo smo uzbuđeni što započinjete ovaj tečaj i vidjeti što ćete biti inspirirani izgraditi s Generativnom AI!

Kako bismo osigurali vaš uspjeh, ova stranica daje pregled koraka za postavljanje, tehničkih zahtjeva i gdje potražiti pomoć ako je potrebna.

## Koraci postavljanja

Da biste započeli s ovim tečajem, trebate dovršiti sljedeće korake.

### 1. Forkajte ovaj Repo

[Forkajte cijeli ovaj repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati bilo koji kod i dovršiti izazove. Također možete [označiti ovaj repo zvjezdicom (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) da biste ga lakše pronašli zajedno s povezanim repozitorijima.

### 2. Kreirajte codespace

Kako biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo izvođenje ovog tečaja u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

U vašem fork-u: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/hr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodajte tajnu

1. ⚙️ Ikona postavki -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Naziv OPENAI_API_KEY, zalijepite vaš ključ, Spremi.

### 3. Što slijedi?

| Želim...          | Idem na...                                                             |
|---------------------|-------------------------------------------------------------------------|
| Započeti Lekciju 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Raditi offline      | [`setup-local.md`](02-setup-local.md)                                   |
| Postaviti LLM Providera | [`providers.md`](03-providers.md)                                    |
| Upoznati druge polaznike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rješavanje problema


| Simptom                                   | Rješenje                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Gradnja kontejnera stoji > 10 min         | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                | Terminal se nije priključio; kliknite **+** ➜ *bash*            |
| `401 Unauthorized` s OpenAI                | Pogrešan / istekao `OPENAI_API_KEY`                              |
| VS Code prikazuje “Dev container mounting…” | Osvježite karticu preglednika—Codespaces ponekad gubi vezu    |
| Nedostaje kernel u bilježnici              | Izbornik bilježnice ➜ **Kernel ▸ Select Kernel ▸ Python 3**      |

   Sustavi temeljeni na Unixu:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++ ili bilo koji drugi uređivač). Dodajte sljedeće redove u datoteku, zamjenjujući mjesta za unos sa stvarnim Microsoft Foundry Models endpointom i ključem (pogledajte [`providers.md`](03-providers.md) za upute kako ih dobiti):

   > **Napomena:** GitHub Models (i njegova varijabla `GITHUB_TOKEN`) se povlači krajem srpnja 2026. Koristite umjesto toga [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako već niste, trebate instalirati paket `python-dotenv` za učitavanje varijabli okoline iz `.env` datoteke u vašu Python aplikaciju. Možete ga instalirati pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okoline u vaš Python skript**: U vašem Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okoline iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Učitaj varijable okoline iz .env datoteke
   load_dotenv()

   # Pristupi varijablama Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoje vjerodajnice Microsoft Foundry Modelsa i učitali ih u vašu Python aplikaciju.

## Kako pokrenuti lokalno na vašem računalu

Da biste pokrenuli kod lokalno na vašem računalu, trebate imati instaliranu neku verziju [Python-a](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Da biste potom koristili repozitorij, trebate ga klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kad sve imate spremno, možete započeti!

## Opcionalni Koraci

### Instaliranje Minicone

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.
Sam Conda je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni putem `pip`.

Možete slijediti [MiniConda vodič za instalaciju](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za njegovo postavljanje.

Nakon instalacije Minicone, trebate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ako to već niste učinili)

Zatim morate kreirati virtualno okruženje. Da biste to napravili s Condom, kreirajte novu environment datoteku (_environment.yml_). Ako pratite koristeći Codespaces, kreirajte ju unutar `.devcontainer` direktorija, tj. `.devcontainer/environment.yml`.

Slobodno ispunite vašu environment datoteku sljedećim isječkom:

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

Ako imate problema s korištenjem conde, možete ručno instalirati Microsoft AI biblioteke koristeći sljedeću naredbu u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Environment datoteka određuje potrebne ovisnosti. `<environment-name>` označava naziv koji želite koristiti za svoje Conda okruženje, a `<python-version>` je verzija Pythona koju želite koristiti, primjerice, `3` je najnovija glavna verzija Pythona.

Kad ste to napravili, možete kreirati svoje Conda okruženje pokretanjem sljedećih naredbi u command line/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podputanja primjenjuje se samo na Codespace postavke
conda activate ai4beg
```

Pogledajte [Vodič za Conda okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na probleme.

### Korištenje Visual Studio Code-a s dodatkom za podršku Pythona

Preporučujemo korištenje [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) uređivača s instaliranim [dodatkom za podršku Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Ovo je preporuka, a ne obveza.

> **Napomena**: Otvaranjem repozitorija tečaja u VS Code-u imate opciju postaviti projekt unutar kontejnera. To je zbog [posebne `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mape unutar repozitorija tečaja. Više o tome kasnije.

> **Napomena**: Kad klonirate i otvorite direktorij u VS Code-u, automatski će vam predložiti da instalirate dodatak za podršku Pythona.

> **Napomena**: Ako vam VS Code predloži da ponovno otvorite repozitorij unutar kontejnera, odbijte taj zahtjev kako biste koristili lokalno instaliranu verziju Pythona.

### Korištenje Jupytera u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) izravno u pregledniku. I klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju ugodno razvojno okruženje s mogućnostima kao što su automatsko dovršavanje, isticanje koda itd.

Za pokretanje Jupytera lokalno, otvorite terminal/command line, dođite do direktorija tečaja, i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter primjerak, a URL za pristup bit će prikazan u prozoru naredbenog retka.

Kad pristupite URL-u, trebali biste vidjeti sadržaj tečaja i moći navigirati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

### Pokretanje u kontejneru

Alternativa postavljanju svega na vašem računalu ili Codespace-u je korištenje [kontejnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna `.devcontainer` mapa unutar repozitorija tečaja omogućuje VS Code-u postavljanje projekta unutar kontejnera. Izvan Codespacesa, to zahtijeva instalaciju Dockera, a iskreno, uključuje dosta posla, stoga to preporučujemo samo onima koji imaju iskustva s kontejnerima.

Jedan od najboljih načina za sigurno čuvanje vaših API ključeva kada koristite GitHub Codespaces je korištenje Codespace Secrets. Molimo pratite vodič [Codespaces upravljanje tajnama](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) za više informacija o tome.


## Lekcije i tehnički zahtjevi

Tečaj sadrži "Nauči" lekcije koje objašnjavaju koncepte Generativne AI i "Izgradi" lekcije s praktičnim primjerima koda u **Pythonu** i **TypeScriptu** gdje je to moguće.

Za lekcije kodiranja koristimo Azure OpenAI u Microsoft Foundry. Trebat će vam Azure pretplata i API ključ. Pristup je otvoren - nije potrebna prijava - tako da možete [kreirati Microsoft Foundry resurs i postaviti model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) za dobivanje vašeg endpointa i ključa.

Svaka lekcija kodiranja također uključuje `README.md` datoteku u kojoj možete pregledati kod i izlaze bez pokretanja.

## Prvi put korištenje Azure OpenAI usluge

Ako prvi put radite s Azure OpenAI uslugom, molimo pratite ovaj vodič kako [kreirati i postaviti Azure OpenAI servisni resurs.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvi put korištenje OpenAI API

Ako prvi put radite s OpenAI API-jem, pratite vodič kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge polaznike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih polaznika. Ovo je sjajan način za umrežavanje s drugim poduzetnicima, kreatorima, studentima i svima koji žele napredovati u Generativnoj AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektni tim također će biti na ovom Discord serveru kako bi pomogao polaznicima.

## Doprinosejte

Ovaj tečaj je inicijativa otvorenog koda. Ako pronađete prostor za poboljšanja ili probleme, molimo kreirajte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektni tim prati sve doprinose. Doprinos u open source zajednici je izvrstan način za izgradnju vaše karijere u Generativnoj AI.

Većina doprinosa zahtijeva da se složite s Ugovorom o licenciranju doprinositelja (CLA) kojim izjavljujete da imate pravo i zapravo dajete pravo na korištenje vašeg doprinosa. Za detalje posjetite [CLA, Contributor License Agreement web stranicu](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: pri prevođenju teksta u ovom repozitoriju molimo osigurajte da NE koristite strojno prevođenje. Provjeravat ćemo prijevode putem zajednice, stoga molimo volontirajte za prijevode samo za jezike kojima ste vješti.


Kada pošaljete zahtjev za povlačenje, CLA-bot će automatski odrediti trebate li pružiti CLA i odgovarajuće označiti PR (npr. oznaka, komentar). Jednostavno slijedite upute koje daje bot. Ovo ćete morati napraviti samo jednom za sve repozitorije koji koriste naš CLA.

Ovaj projekt usvojio je [Microsoftov kodeks ponašanja za otvoreni izvor](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) za dodatna pitanja ili komentare.

## Krenimo

Sada kada ste dovršili potrebne korake za završetak ovog tečaja, krenimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->