# Početak s ovim kolegijem

Vrlo smo uzbuđeni što ćete započeti ovaj kolegij i vidjeti što ćete biti inspirirani izgraditi s Generativnom AI!

Kako bismo osigurali vaš uspjeh, ova stranica opisuje korake postavljanja, tehničke zahtjeve i gdje potražiti pomoć ako je potrebna.

## Koraci postavljanja

Za početak ovog kolegija trebate završiti sljedeće korake.

### 1. Forkajte ovaj repozitorij

[Forkajte cijeli ovaj repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati bilo koji kod i uspješno dovršiti izazove. Također možete [označiti (🌟) ovaj repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) za lakše pronalaženje njega i srodnih repozitorija.

### 2. Kreirajte codespace

Kako biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo korištenje [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) za ovaj kolegij.

U svom fork-u: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/hr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodajte tajnu (secret)

1. ⚙️ Ikona zupčanika -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nazovite ju OPENAI_API_KEY, zalijepite svoj ključ, Spremi.

### 3. Što dalje?

| Želim…              | Idite na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Početi Lekciju 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Raditi offline      | [`setup-local.md`](02-setup-local.md)                                   |
| Postaviti LLM pružatelja | [`providers.md`](03-providers.md)                                        |
| Upoznati druge polaznike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rješavanje problema

| Simptom                                   | Rješenje                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Gradnja containera zaglavila se > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal se nije povezao; kliknite **+** ➜ *bash*               |
| `401 Unauthorized` iz OpenAI              | Pogrešan / istekao `OPENAI_API_KEY`                             |
| VS Code prikazuje “Dev container mounting…” | Osvježite karticu preglednika—Codespaces ponekad gubi vezu      |
| Nedostaje kernel bilježnice                | Izbornik bilježnice ➜ **Kernel ▸ Select Kernel ▸ Python 3**     |

   Unix-based sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u tekstualnom uređivaču (npr. VS Code, Notepad++ ili bilo kojem drugom). Dodajte sljedeći redak u datoteku, zamijenivši `your_github_token_here` stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite tekstualni uređivač.

5. **Instalirajte `python-dotenv`**: Ako već niste, instalirajte paket `python-dotenv` kako biste mogli učitati varijable okoline iz `.env` datoteke u Python aplikaciju. Možete ga instalirati koristeći `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okoline u svom Python skriptu**: U Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okoline iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Učitaj varijable okoline iz .env datoteke
   load_dotenv()

   # Pristupi varijabli GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoj GitHub token i učitali ga u Python aplikaciju.

## Kako pokrenuti lokalno na svom računalu

Da biste pokrenuli kôd lokalno na svom računalu, trebate imati instaliranu neku verziju [Python-a](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Zatim, za korištenje repozitorija, potrebno ga je klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kada sve to imate, možete započeti!

## Opcionalni koraci

### Instalacija Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.  
Conda sama po sebi je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također pomaže pri instalaciji paketa koji nisu dostupni putem `pip`.

Možete pratiti [MiniConda vodič za instalaciju](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

Nakon instalacije Miniconda, trebate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ako već niste).

Dalje, trebate kreirati virtualno okruženje. Da biste to napravili s Condom, kreirajte novu datoteku okruženja (_environment.yml_). Ako pratite kolegij koristeći Codespaces, kreirajte ju unutar `.devcontainer` direktorija, to jest `.devcontainer/environment.yml`.

Popunite svoju datoteku okruženja sljedećim isječkom:

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

Ako naiđete na pogreške pri korištenju conda, možete ručno instalirati Microsoft AI biblioteku koristeći sljedeću naredbu u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okruženja specificira ovisnosti koje trebamo. `<environment-name>` se odnosi na ime koje želite koristiti za svoje Conda okruženje, a `<python-version>` na verziju Pythona koju želite koristiti, npr. `3` je najnovija glavna verzija Pythona.

Kada to učinite, možete kreirati Conda okruženje pokretanjem naredbi u terminalu/komandnoj liniji:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podputanja se odnosi samo na Codespace postavke
conda activate ai4beg
```

Pogledajte [Conda vodič za upravljanje okruženjima](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na probleme.

### Korištenje Visual Studio Code s Python podrškom

Preporučujemo da za ovaj kolegij koristite [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) uređivač s instaliranim [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Ovo je, međutim, samo preporuka, a ne strogi zahtjev.

> **Napomena**: Otvaranjem repozitorija kolegija u VS Code imate opciju postaviti projekt unutar containera. To je moguće zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija unutar repozitorija kolegija. O tome ćemo više kasnije.

> **Napomena**: Kad klonirate i otvorite direktorij u VS Code, automatski će vam predložiti da instalirate Python support extension.

> **Napomena**: Ako vam VS Code predloži da ponovno otvorite repozitorij u containeru, odbijte taj zahtjev ako želite koristiti lokalno instaliranu verziju Pythona.

### Korištenje Jupyter-a u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direktno u pregledniku. I klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju jako ugodno razvojno okruženje s funkcijama poput automatskog dovršavanja, isticanja koda itd.

Za pokretanje Jupyter-a lokalno, otvorite terminal/komandnu liniju, dođite do direktorija kolegija i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu, a URL za pristup će biti prikazan u komandnoj liniji.

Kada pristupite URL-u, trebali biste vidjeti okvir kolegija i moći navigirati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

### Pokretanje u containeru

Alternativa za postavljanje svega na svom računalu ili Codespaceu je korištenje [containera](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna `.devcontainer` mapa u repozitoriju omogućuje VS Code-u postavljanje projekta unutar containera. Izvan Codespaces ovo zahtijeva instalaciju Dockera i, iskreno govoreći, uključuje malo posla, stoga preporučujemo ovo samo iskusnim korisnicima koji već rade s containerima.

Jedan od najboljih načina da zaštitite svoje API ključeve pri korištenju GitHub Codespaces-a jest korištenje Codespace Secrets. Molimo pratite vodič za [upravljanje tajnama u Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kako biste saznali više.

## Lekcije i tehnički zahtjevi

Kolegij ima 6 konceptualnih lekcija i 6 lekcija programiranja.

Za lekcije programiranja koristimo Azure OpenAI servis. Trebat će vam pristup Azure OpenAI servisu i API ključ za pokretanje ovog koda. Možete se prijaviti za pristup [ispunjavajući ovaj zahtjev](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Dok čekate da vam se zahtjev obradi, svaka lekcija programiranja također uključuje `README.md` datoteku u kojoj možete pregledati kod i izlaze.

## Korištenje Azure OpenAI servisa po prvi put

Ako prvi put radite s Azure OpenAI servisom, molimo pratite ovaj vodič o tome kako [kreirati i postaviti Azure OpenAI Service resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korištenje OpenAI API-ja po prvi put

Ako prvi put radite s OpenAI API-jem, pratite vodič o tome kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge polaznike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih polaznika. Ovo je sjajan način umrežavanja s drugim istomišljenicima, poduzetnicima, developerima, studentima i svima koji žele napredovati u Generativnoj AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim projekta također će biti na ovom Discord serveru da pomogne polaznicima.

## Doprinos

Ovaj kolegij je inicijativa otvorenog koda. Ako vidite mogućnosti za poboljšanje ili probleme, molimo kreirajte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim projekta će pratiti sve doprinose. Doprinos open source projektu je izvrstan način za razvoj karijere u Generativnoj AI.

Većina doprinosa zahtijeva da pristajete na Contributor License Agreement (CLA) kojim izjavljujete da imate prava i stvarno dajete prava korištenja vašeg doprinosa. Za detalje posjetite [CLA, Contributor License Agreement web stranicu](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: kod prevođenja teksta u ovom repozitoriju, molimo osigurajte da ne koristite strojno prevođenje. Provjeravat ćemo prijevode putem zajednice, stoga volontirajte za prijevode samo jezika u kojima ste vješti.

Kada pošaljete pull request, CLA-bot će automatski određivati trebate li dati CLA i pravilno označiti PR (npr. labelu, komentar). Jednostavno slijedite upute koje bot daje. Ovo je potrebno napraviti samo jednom za sve repozitorije koji koriste naš CLA.

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o Kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) s dodatnim pitanjima ili komentarima.

## Krenimo!
Sada kada ste dovršili potrebne korake za završetak ovog tečaja, krenimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI prevodilačke usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se stručni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->