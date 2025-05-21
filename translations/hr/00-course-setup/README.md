<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:38:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hr"
}
-->
# Početak rada s ovim tečajem

Vrlo smo uzbuđeni što započinjete ovaj tečaj i jedva čekamo vidjeti što ćete inspirirano izgraditi s Generativnom umjetnom inteligencijom!

Kako bismo osigurali vaš uspjeh, ova stranica opisuje korake za postavljanje, tehničke zahtjeve i gdje potražiti pomoć ako je potrebna.

## Koraci za postavljanje

Da biste započeli s ovim tečajem, trebate dovršiti sljedeće korake.

### 1. Forkajte ovaj repozitorij

[Forkajte cijeli ovaj repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati bilo koji kod i dovršiti izazove. Također možete [označiti (🌟) ovaj repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli zajedno s povezanim repozitorijima.

### 2. Kreirajte Codespace

Kako biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo pokretanje ovog tečaja u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ovo možete kreirati odabirom opcije `Code` na svojoj forkanoj verziji ovog repozitorija i odabirom opcije **Codespaces**.

![Dijalog koji prikazuje gumbe za kreiranje codespace-a](../../../00-course-setup/images/who-will-pay.webp)

### 3. Pohrana vaših API ključeva

Čuvanje vaših API ključeva sigurnim i zaštićenim je važno prilikom izrade bilo koje vrste aplikacije. Preporučujemo da ne pohranjujete API ključeve izravno u vašem kodu. Objavljivanje tih detalja u javnom repozitoriju moglo bi rezultirati sigurnosnim problemima i neželjenim troškovima ako ih zlonamjerni korisnik iskoristi.
Evo korak-po-korak vodiča o tome kako kreirati datoteku `.env` za Python i dodati `GITHUB_TOKEN`:

1. **Navigirajte do direktorija vašeg projekta**: Otvorite terminal ili naredbeni redak i navigirajte do korijenskog direktorija vašeg projekta gdje želite kreirati datoteku `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte datoteku `.env`**: Koristite svoj omiljeni tekstualni urednik za kreiranje nove datoteke nazvane `.env`. Ako koristite naredbeni redak, možete koristiti `touch` (on Unix-based systems) or `echo` (na Windowsu):

   Unix-based sustavi:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Uredite datoteku `.env`**: Otvorite datoteku `.env` u tekstualnom uredniku (npr. VS Code, Notepad++ ili bilo kojem drugom uredniku). Dodajte sljedeći redak u datoteku, zamjenjujući `your_github_token_here` s vašim stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite tekstualni urednik.

5. **Instalirajte paket `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` za učitavanje varijabli okruženja iz datoteke `.env` u vašu Python aplikaciju. Možete ga instalirati pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okruženja u vašem Python skriptu**: U vašem Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okruženja iz datoteke `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspješno ste kreirali datoteku `.env`, dodali svoj GitHub token i učitali ga u svoju Python aplikaciju.

## Kako pokrenuti lokalno na vašem računalu

Da biste pokrenuli kod lokalno na vašem računalu, trebali biste imati neku verziju [Pythona instaliranu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Zatim, da biste koristili repozitorij, trebate ga klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kada sve imate provjereno, možete početi!

## Opcionalni koraci

### Instaliranje Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instaliranje [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.
Conda je sama po sebi upravitelj paketa, što olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je korisna za instaliranje paketa koji nisu dostupni putem `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Ispunite svoju datoteku okruženja s isječkom ispod:

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

Ako naiđete na greške koristeći conda, možete ručno instalirati Microsoft AI Libraries koristeći sljedeću naredbu u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okruženja specificira potrebne ovisnosti. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovija glavna verzija Pythona.

Kada to napravite, možete kreirati svoje Conda okruženje pokretanjem naredbi ispod u vašem naredbenom retku/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pogledajte [Conda vodič za okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na bilo kakve probleme.

### Korištenje Visual Studio Code-a s ekstenzijom za Python

Preporučujemo korištenje uređivača [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s instaliranom [ekstenzijom za Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Međutim, ovo je više preporuka nego zahtjev.

> **Napomena**: Otvaranjem repozitorija tečaja u VS Code-u, imate opciju postaviti projekt unutar kontejnera. Ovo je zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija pronađenog unutar repozitorija tečaja. Više o tome kasnije.

> **Napomena**: Kada klonirate i otvorite direktorij u VS Code-u, automatski će vam predložiti instalaciju ekstenzije za Python.

> **Napomena**: Ako vam VS Code predloži da ponovno otvorite repozitorij u kontejneru, odbijte ovaj zahtjev kako biste koristili lokalno instaliranu verziju Pythona.

### Korištenje Jupyter-a u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direktno u vašem pregledniku. Klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju ugodno razvojno okruženje s funkcijama kao što su automatsko dovršavanje, isticanje koda itd.

Za pokretanje Jupyter-a lokalno, otvorite terminal/naredbeni redak, navigirajte do direktorija tečaja i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu i URL za pristup bit će prikazan unutar prozora naredbenog retka.

Kada pristupite URL-u, trebali biste vidjeti pregled tečaja i moći navigirati do bilo koje `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` datoteke gdje možete pregledati kod i izlaze.

## Korištenje Azure OpenAI servisa po prvi put

Ako je ovo vaš prvi put da radite s Azure OpenAI servisom, slijedite ovaj vodič o tome kako [kreirati i implementirati Azure OpenAI servisni resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korištenje OpenAI API-ja po prvi put

Ako je ovo vaš prvi put da radite s OpenAI API-jem, slijedite vodič o tome kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge učenike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih učenika. Ovo je sjajan način za umrežavanje s drugim poduzetnicima, graditeljima, studentima i svima koji žele napredovati u Generativnoj umjetnoj inteligenciji.

[![Pridružite se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim projekta također će biti na ovom Discord serveru kako bi pomogao svim učenicima.

## Doprinesite

Ovaj tečaj je inicijativa otvorenog koda. Ako vidite područja za poboljšanje ili probleme, molimo vas da kreirate [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim projekta će pratiti sve doprinose. Doprinos otvorenom kodu je nevjerojatan način za izgradnju vaše karijere u Generativnoj umjetnoj inteligenciji.

Većina doprinosa zahtijeva da se složite s Ugovorom o licenciranju suradnika (CLA) kojim izjavljujete da imate pravo i stvarno nam dajete prava za korištenje vašeg doprinosa. Za detalje, posjetite [CLA, web stranicu Ugovora o licenciranju suradnika](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: prilikom prevođenja teksta u ovom repozitoriju, molimo osigurajte da ne koristite strojno prevođenje. Provjerit ćemo prijevode putem zajednice, stoga molimo da se prijavite za prevođenje samo na jezicima u kojima ste vješti.

Kada pošaljete pull request, CLA-bot će automatski odrediti trebate li osigurati CLA i prikladno ukrasiti PR (npr. oznaka, komentar). Jednostavno slijedite upute koje vam bot daje. Ovo trebate napraviti samo jednom za sve repozitorije koji koriste naš CLA.

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o Kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) s bilo kakvim dodatnim pitanjima ili komentarima.

## Započnimo

Sada kada ste završili potrebne korake za završetak ovog tečaja, krenimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo ka točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.