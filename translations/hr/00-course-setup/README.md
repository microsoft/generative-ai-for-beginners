<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T09:01:17+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hr"
}
-->
# Početak s ovim tečajem

Vrlo smo uzbuđeni što započinjete ovaj tečaj i vidjeti što ćete biti inspirirani izgraditi s Generativnom AI!

Kako bismo osigurali vaš uspjeh, ova stranica opisuje korake postavljanja, tehničke zahtjeve i gdje možete dobiti pomoć ako je potrebna.

## Koraci postavljanja

Da biste započeli s ovim tečajem, trebate dovršiti sljedeće korake.

### 1. Forkajte ovaj repozitorij

[Forkajte cijeli ovaj repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati bilo koji kod i završiti izazove. Također možete [dodati zvjezdicu (🌟) ovom repozitoriju](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli i srodne repozitorije.

### 2. Kreirajte codespace

Kako biste izbjegli probleme s ovisnostima pri pokretanju koda, preporučujemo pokretanje ovog tečaja u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ovo možete kreirati odabirom opcije `Code` na vašoj forkanoj verziji ovog repozitorija i odabirom opcije **Codespaces**.

![Dijalog koji prikazuje gumbe za kreiranje codespacea](../../../00-course-setup/images/who-will-pay.webp)

### 3. Pohrana vaših API ključeva

Važno je držati vaše API ključeve sigurnima kada gradite bilo koju vrstu aplikacije. Preporučujemo da ne pohranjujete API ključeve izravno u vašem kodu. Predaja tih podataka u javni repozitorij može rezultirati sigurnosnim problemima pa čak i neželjenim troškovima ako ih zlonamjerna osoba iskoristi.
Evo vodiča korak po korak kako kreirati `.env` datoteku za Python i dodati `GITHUB_TOKEN`:

1. **Navigirajte do direktorija vašeg projekta**: Otvorite svoj terminal ili naredbeni redak i navigirajte do korijenskog direktorija vašeg projekta gdje želite kreirati `.env` datoteku.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte `.env` datoteku**: Koristite svoj omiljeni tekst editor za kreiranje nove datoteke nazvane `.env`. Ako koristite naredbeni redak, možete koristiti `touch` (on Unix-based systems) or `echo` (na Windowsima):

   Sustavi temeljeni na Unixu:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u tekst editoru (npr. VS Code, Notepad++ ili bilo kojem drugom editoru). Dodajte sljedeći redak u datoteku, zamjenjujući `your_github_token_here` s vašim stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite tekst editor.

5. **Instalirajte `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` paket kako biste učitali varijable okruženja iz `.env` datoteke u vašu Python aplikaciju. Možete ga instalirati koristeći `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okruženja u vašem Python skriptu**: U vašem Python skriptu, koristite `python-dotenv` paket za učitavanje varijabli okruženja iz `.env` datoteke:

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

## Kako pokrenuti lokalno na vašem računalu

Da biste pokrenuli kod lokalno na vašem računalu, trebali biste imati neku verziju [Pythona instaliranu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kako biste zatim koristili repozitorij, trebate ga klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kada sve provjerite, možete početi!

## Opcionalni koraci

### Instaliranje Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski paket za instaliranje [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.
Conda je sam po sebi upravitelj paketa, koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instaliranje paketa koji nisu dostupni putem `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Nastavite i popunite svoju datoteku okruženja s donjim isječkom:

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

Datoteka okruženja specificira ovisnosti koje trebamo. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovija glavna verzija Pythona.

Kada to učinite, možete kreirati svoje Conda okruženje pokretanjem dolje navedenih naredbi u vašem naredbenom retku/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pogledajte [vodič za Conda okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na bilo kakve probleme.

### Korištenje Visual Studio Code s ekstenzijom za podršku Pythonu

Preporučujemo korištenje [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) urednika s instaliranom [ekstenzijom za podršku Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Ovo je, međutim, više preporuka, a ne strogi zahtjev.

> **Napomena**: Otvaranjem repozitorija tečaja u VS Code, imate mogućnost postaviti projekt unutar kontejnera. To je zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija pronađenog unutar repozitorija tečaja. Više o tome kasnije.

> **Napomena**: Kada klonirate i otvorite direktorij u VS Code, automatski će vam predložiti instaliranje ekstenzije za podršku Pythonu.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u kontejneru, odbijte ovaj zahtjev kako biste koristili lokalno instaliranu verziju Pythona.

### Korištenje Jupyter-a u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) izravno u vašem pregledniku. Klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju vrlo ugodno razvojno okruženje s funkcijama kao što su automatsko dovršavanje, isticanje koda itd.

Da biste pokrenuli Jupyter lokalno, idite na terminal/naredbeni redak, navigirajte do direktorija tečaja i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu, a URL za pristup bit će prikazan unutar prozora naredbenog retka.

Kada pristupite URL-u, trebali biste vidjeti okvir tečaja i moći navigirati do bilo koje `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` datoteke gdje možete pregledati kod i rezultate.

## Korištenje Azure OpenAI usluge po prvi put

Ako je ovo vaš prvi put da radite s Azure OpenAI uslugom, molimo slijedite ovaj vodič kako [kreirati i implementirati Azure OpenAI uslugu.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korištenje OpenAI API-ja po prvi put

Ako je ovo vaš prvi put da radite s OpenAI API-jem, molimo slijedite vodič kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge polaznike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih polaznika. Ovo je odličan način za umrežavanje s drugim poduzetnicima, graditeljima, studentima i svima koji žele unaprijediti svoje znanje u Generativnoj AI.

[![Pridružite se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektni tim će također biti na ovom Discord serveru kako bi pomogao svim polaznicima.

## Doprinos

Ovaj tečaj je inicijativa otvorenog koda. Ako vidite područja za poboljšanje ili probleme, molimo kreirajte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektni tim će pratiti sve doprinose. Doprinos otvorenom kodu je nevjerojatan način za izgradnju vaše karijere u Generativnoj AI.

Većina doprinosa zahtijeva da se složite s Ugovorom o licenci za suradnike (CLA) koji izjavljuje da imate pravo i zapravo dodjeljujete nam prava da koristimo vaš doprinos. Za detalje posjetite [CLA, web stranica Ugovora o licenci za suradnike](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: kada prevodite tekst u ovom repozitoriju, molimo osigurajte da ne koristite strojno prevođenje. Provjerit ćemo prijevode putem zajednice, stoga molimo da se prijavite za prijevode samo na jezicima na kojima ste stručni.

Kada pošaljete pull request, CLA-bot će automatski odrediti trebate li pružiti CLA i prikladno ukrasiti PR (npr. oznaka, komentar). Jednostavno slijedite upute koje daje bot. To ćete trebati učiniti samo jednom u svim repozitorijima koji koriste naš CLA.

Ovaj projekt je usvojio [Microsoftov Kodeks ponašanja za otvoreni kod](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte Često postavljana pitanja o Kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) s bilo kojim dodatnim pitanjima ili komentarima.

## Počnimo

Sada kada ste završili potrebne korake za dovršetak ovog tečaja, započnimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.