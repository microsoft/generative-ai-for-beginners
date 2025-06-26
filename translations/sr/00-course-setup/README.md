<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T09:00:45+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sr"
}
-->
# Почетак курса

Veoma smo uzbuđeni što počinjete ovaj kurs i jedva čekamo da vidimo šta ćete inspirisano generativnom veštačkom inteligencijom izgraditi!

Da bismo osigurali vaš uspeh, ova stranica opisuje korake za postavljanje, tehničke zahteve i gde možete dobiti pomoć ako vam je potrebna.

## Koraci za postavljanje

Da biste počeli sa ovim kursom, potrebno je da izvršite sledeće korake.

### 1. Forkujte ovaj Repo

[Forkujte ceo repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub nalog kako biste mogli da menjate kod i završite izazove. Takođe možete [zvezdati (🌟) ovaj repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli zajedno sa povezanim repozitorijumima.

### 2. Kreirajte kodni prostor

Da biste izbegli probleme sa zavisnostima prilikom pokretanja koda, preporučujemo da pokrenete ovaj kurs u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ovo se može kreirati izborom opcije `Code` na vašoj forkovanoj verziji ovog repoa i izborom opcije **Codespaces**.

![Dijalog koji prikazuje dugmad za kreiranje kodnog prostora](../../../00-course-setup/images/who-will-pay.webp)

### 3. Čuvanje vaših API ključeva

Čuvanje vaših API ključeva bezbednim i sigurnim je važno kada gradite bilo koju vrstu aplikacije. Preporučujemo da ne čuvate API ključeve direktno u kodu. Čuvanje tih detalja u javnom repozitorijumu može dovesti do sigurnosnih problema i neželjenih troškova ako ih koristi loš akter.
Evo vodiča korak po korak o tome kako kreirati `.env` datoteku za Python i dodati `GITHUB_TOKEN`:

1. **Navigirajte do direktorijuma vašeg projekta**: Otvorite terminal ili komandnu liniju i navigirajte do korenskog direktorijuma vašeg projekta gde želite da kreirate `.env` datoteku.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte `.env` datoteku**: Koristite svoj omiljeni uređivač teksta da kreirate novu datoteku pod nazivom `.env`. Ako koristite komandnu liniju, možete koristiti `touch` (on Unix-based systems) or `echo` (na Windows-u):

   Sistemi zasnovani na Unix-u:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Izmenite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr., VS Code, Notepad++ ili bilo koji drugi uređivač). Dodajte sledeći red u datoteku, zamenjujući `your_github_token_here` sa vašim stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sačuvajte datoteku**: Sačuvajte promene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` paket za učitavanje varijabli okruženja iz `.env` datoteke u vašu Python aplikaciju. Možete ga instalirati koristeći `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okruženja u vaš Python skript**: U vašem Python skriptu koristite `python-dotenv` paket za učitavanje varijabli okruženja iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno ste kreirali `.env` datoteku, dodali vaš GitHub token i učitali ga u vašu Python aplikaciju.

## Kako pokrenuti lokalno na vašem računaru

Da biste pokrenuli kod lokalno na vašem računaru, potrebno je da imate neku verziju [Python-a instaliranu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Da biste koristili repozitorijum, potrebno je da ga klonirate:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kada sve proverite, možete početi!

## Opcionalni koraci

### Instaliranje Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalator za instaliranje [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-a, kao i nekoliko paketa.
Conda je menadžer paketa, koji olakšava postavljanje i prebacivanje između različitih Python [**virtuelnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Takođe je korisno za instaliranje paketa koji nisu dostupni putem `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Nastavite i popunite vašu datoteku okruženja sa isječkom ispod:

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

Ako dobijete greške prilikom korišćenja conda, možete ručno instalirati Microsoft AI biblioteke koristeći sledeću komandu u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okruženja navodi zavisnosti koje su nam potrebne. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je najnovija glavna verzija Python-a.

Kada to završite, možete nastaviti i kreirati vaše Conda okruženje pokretanjem komandi ispod u vašoj komandnoj liniji/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pogledajte [Vodič za Conda okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na bilo kakve probleme.

### Korišćenje Visual Studio Code-a sa ekstenzijom za podršku Python-a

Preporučujemo korišćenje [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) uređivača sa instaliranom [ekstenzijom za podršku Python-a](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj kurs. Ovo je, međutim, više preporuka nego definitivni zahtev.

> **Napomena**: Otvaranjem repozitorijuma kursa u VS Code-u, imate opciju da postavite projekat unutar kontejnera. To je zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorijuma koji se nalazi unutar repozitorijuma kursa. Više o tome kasnije.

> **Napomena**: Kada klonirate i otvorite direktorijum u VS Code-u, automatski će vam predložiti da instalirate ekstenziju za podršku Python-a.

> **Napomena**: Ako vam VS Code predloži da ponovo otvorite repozitorijum u kontejneru, odbijte ovaj zahtev kako biste koristili lokalno instaliranu verziju Python-a.

### Korišćenje Jupyter-a u pretraživaču

Takođe možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direktno u vašem pretraživaču. I klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju prilično prijatno razvojno okruženje sa funkcijama kao što su automatsko dovršavanje, isticanje koda, itd.

Da biste pokrenuli Jupyter lokalno, idite na terminal/komandnu liniju, navigirajte do direktorijuma kursa i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu, a URL za pristup će biti prikazan u prozoru komandne linije.

Kada pristupite URL-u, trebalo bi da vidite okvir kursa i budete u mogućnosti da navigirate do bilo koje `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` datoteke gde možete videti kod i izlaze.

## Korišćenje Azure OpenAI servisa po prvi put

Ako je ovo vaš prvi put da radite sa Azure OpenAI servisom, molimo vas da pratite ovaj vodič o tome kako [kreirati i implementirati resurs Azure OpenAI servisa.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korišćenje OpenAI API-ja po prvi put

Ako je ovo vaš prvi put da radite sa OpenAI API-jem, molimo vas da pratite vodič o tome kako [kreirati i koristiti Interfejs.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge učenike

Kreirali smo kanale na našem zvaničnom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih učenika. Ovo je odličan način da se povežete sa drugim preduzetnicima, graditeljima, studentima i svima koji žele da unaprede svoje znanje u Generativnoj veštačkoj inteligenciji.

[![Pridružite se Discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim projekta će takođe biti na ovom Discord serveru da pomogne učenicima.

## Doprinos

Ovaj kurs je inicijativa otvorenog koda. Ako vidite oblasti za poboljšanje ili probleme, molimo vas da kreirate [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim projekta će pratiti sve doprinose. Doprinos otvorenom kodu je neverovatan način da izgradite svoju karijeru u Generativnoj veštačkoj inteligenciji.

Većina doprinosa zahteva od vas da se složite sa Sporazumom o licenci za doprinos (CLA) koji potvrđuje da imate pravo i zapravo dajete nam prava da koristimo vaš doprinos. Za detalje, posetite [CLA, web stranicu Sporazuma o licenci za doprinos](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: kada prevodite tekst u ovom repo-u, molimo vas da se pobrinete da ne koristite mašinski prevod. Prevod ćemo proveriti putem zajednice, pa vas molimo da se prijavite za prevode samo na jezicima na kojima ste stručni.

Kada podnesete pull request, CLA-bot će automatski utvrditi da li treba da obezbedite CLA i odgovarajuće ukrasiti PR (npr., oznaka, komentar). Jednostavno pratite uputstva koja vam pruža bot. Ovo ćete morati učiniti samo jednom za sve repozitorijume koji koriste naš CLA.

Ovaj projekat je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o Kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) sa bilo kakvim dodatnim pitanjima ili komentarima.

## Hajde da počnemo

Sada kada ste završili potrebne korake za završetak ovog kursa, hajde da počnemo sa [uvodom u Generativnu veštačku inteligenciju i LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ограничење одговорности**:  
Овај документ је преведен користећи услугу превођења путем вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални људски превод. Нисмо одговорни за било каква погрешна схватања или погрешна тумачења која произилазе из употребе овог превода.