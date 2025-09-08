<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:39:18+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hr"
}
-->
# Početak rada s ovim tečajem

Jako nam je drago što započinjete ovaj tečaj i veselimo se vidjeti što ćete izgraditi uz pomoć Generativne AI!

Kako bismo vam olakšali uspjeh, na ovoj stranici su opisani koraci za postavljanje, tehnički zahtjevi i gdje možete potražiti pomoć ako zatreba.

## Koraci za postavljanje

Da biste započeli s ovim tečajem, potrebno je napraviti sljedeće korake.

### 1. Forkajte ovaj repozitorij

[Forkajte cijeli repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati kod i rješavati izazove. Također možete [zvjezdicom (🌟) označiti repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli, kao i povezane repozitorije.

### 2. Kreirajte codespace

Da biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo da ovaj tečaj radite u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

U svom forku: **Code -> Codespaces -> New on main**

![Dijalog s gumbima za kreiranje codespace-a](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Dodajte tajnu (secret)

1. ⚙️ Ikona zupčanika -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nazovite OPENAI_API_KEY, zalijepite svoj ključ, Spremite.

### 3.  Što dalje?

| Želim…               | Idi na…                                                                |
|----------------------|------------------------------------------------------------------------|
| Započeti lekciju 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Raditi offline       | [`setup-local.md`](02-setup-local.md)                                  |
| Postaviti LLM Provider | [`providers.md`](providers.md)                                       |
| Upoznati druge polaznike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Rješavanje problema


| Simptom                                   | Rješenje                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build stoji > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal nije povezan; kliknite **+** ➜ *bash*                  |
| `401 Unauthorized` od OpenAI              | Pogrešan / istekao `OPENAI_API_KEY`                             |
| VS Code prikazuje “Dev container mounting…” | Osvježite karticu preglednika—Codespaces ponekad izgubi vezu   |
| Nedostaje kernel za Notebook              | Notebook izbornik ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++ ili bilo kojem drugom editoru). Dodajte sljedeći redak u datoteku, zamijenite `your_github_token_here` sa svojim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako već niste, trebate instalirati paket `python-dotenv` kako biste učitali varijable okruženja iz `.env` datoteke u svoju Python aplikaciju. Instalirajte ga pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okruženja u svom Python skriptu**: U Python skripti koristite paket `python-dotenv` za učitavanje varijabli okruženja iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoj GitHub token i učitali ga u svoju Python aplikaciju.

## Kako pokrenuti lokalno na svom računalu

Da biste pokrenuli kod lokalno na svom računalu, trebate imati instaliranu neku verziju [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Zatim, da biste koristili repozitorij, trebate ga klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kada ste sve preuzeli, možete početi!

## Opcionalni koraci

### Instalacija Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona i nekoliko paketa.
Conda je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni putem `pip`.

Slijedite [MiniConda vodič za instalaciju](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

Nakon što ste instalirali Miniconda, trebate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ako već niste).

Zatim trebate kreirati virtualno okruženje. Da biste to napravili s Conda, kreirajte novu datoteku okruženja (_environment.yml_). Ako radite u Codespaces, kreirajte je unutar `.devcontainer` direktorija, dakle `.devcontainer/environment.yml`.

Popunite datoteku okruženja sljedećim isječkom:

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

Ako naiđete na greške s conda, Microsoft AI Libraries možete ručno instalirati sljedećom naredbom u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okruženja navodi potrebne ovisnosti. `<environment-name>` je naziv koji želite koristiti za svoje Conda okruženje, a `<python-version>` je verzija Pythona koju želite koristiti, npr. `3` je najnovija glavna verzija Pythona.

Kada ste to napravili, možete kreirati svoje Conda okruženje pokretanjem sljedećih naredbi u naredbenom retku/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ako naiđete na probleme, pogledajte [Conda vodič za okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Korištenje Visual Studio Code s ekstenzijom za Python

Preporučujemo korištenje [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) uređivača s instaliranom [ekstenzijom za Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Ovo je preporuka, nije obavezno.

> **Note**: Otvaranjem repozitorija tečaja u VS Code-u, imate mogućnost postaviti projekt unutar kontejnera. To je omogućeno zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija u repozitoriju tečaja. Više o tome kasnije.

> **Note**: Kada klonirate i otvorite direktorij u VS Code-u, automatski će vam predložiti instalaciju ekstenzije za Python.

> **Note**: Ako vam VS Code predloži da ponovno otvorite repozitorij u kontejneru, odbijte taj zahtjev kako biste koristili lokalno instaliranu verziju Pythona.

### Korištenje Jupytera u pregledniku

Projekt možete raditi i u [Jupyter okruženju](https://jupyter.org?WT.mc_id=academic-105485-koreyst) izravno u pregledniku. Klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nude ugodno razvojno okruženje s funkcijama poput automatskog dovršavanja, isticanja koda itd.

Za pokretanje Jupytera lokalno, otvorite terminal/naredbeni redak, idite u direktorij tečaja i pokrenite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instance, a URL za pristup bit će prikazan u prozoru naredbenog retka.

Kada otvorite URL, trebali biste vidjeti strukturu tečaja i moći se kretati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

### Pokretanje u kontejneru

Alternativa postavljanju svega na računalu ili Codespaceu je korištenje [kontejnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna `.devcontainer` mapa u repozitoriju tečaja omogućuje VS Code-u da postavi projekt unutar kontejnera. Izvan Codespaces-a, ovo zahtijeva instalaciju Dockera, i iskreno, uključuje malo više posla, pa ovo preporučujemo samo onima s iskustvom rada s kontejnerima.

Jedan od najboljih načina za zaštitu svojih API ključeva pri korištenju GitHub Codespaces je korištenje Codespace Secrets. Slijedite [vodič za upravljanje Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) za više informacija.


## Lekcije i tehnički zahtjevi

Tečaj sadrži 6 konceptualnih lekcija i 6 lekcija kodiranja.

Za lekcije kodiranja koristimo Azure OpenAI Service. Trebat će vam pristup Azure OpenAI servisu i API ključ za pokretanje koda. Pristup možete zatražiti [ispunjavanjem ove prijave](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Dok čekate obradu prijave, svaka lekcija kodiranja sadrži i `README.md` datoteku u kojoj možete vidjeti kod i rezultate.

## Prvo korištenje Azure OpenAI Service-a

Ako prvi put radite s Azure OpenAI servisom, slijedite ovaj vodič kako biste [kreirali i implementirali Azure OpenAI Service resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvo korištenje OpenAI API-ja

Ako prvi put radite s OpenAI API-jem, slijedite vodič kako biste [kreirali i koristili sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge polaznike

Na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kreirali smo kanale za upoznavanje drugih polaznika. Ovo je odličan način za umrežavanje s drugim poduzetnicima, graditeljima, studentima i svima koji žele napredovati u Generativnoj AI.

[![Pridruži se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim projekta također će biti na ovom Discord serveru kako bi pomogao polaznicima.

## Doprinos

Ovaj tečaj je open-source inicijativa. Ako primijetite mogućnosti za poboljšanje ili probleme, slobodno napravite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim projekta prati sve doprinose. Doprinos open source-u je odličan način za izgradnju karijere u Generativnoj AI.

Većina doprinosa zahtijeva da se složite s Contributor License Agreement (CLA) kojim potvrđujete da imate pravo i zapravo dajete prava za korištenje vašeg doprinosa. Više informacija na [CLA, Contributor License Agreement web stranici](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: prilikom prevođenja teksta u ovom repozitoriju, molimo vas da ne koristite strojno prevođenje. Prijevod će provjeriti zajednica, pa se prijavite za prijevod samo za jezike koje dobro poznajete.

Kada pošaljete pull request, CLA-bot će automatski provjeriti trebate li potpisati CLA i označiti PR (npr. oznaka, komentar). Slijedite upute koje bot daje. Ovo trebate napraviti samo jednom za sve repozitorije koji koriste naš CLA.

Ovaj projekt koristi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o Kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) za dodatna pitanja ili komentare.

## Krenimo!
Sada kada ste završili potrebne korake za ovaj tečaj, krenimo s [uvodom u Generativnu umjetnu inteligenciju i velike jezične modele (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.