<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T01:31:33+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hr"
}
-->
# Početak s ovim tečajem

Jako smo uzbuđeni što započinjete ovaj tečaj i jedva čekamo vidjeti što ćete inspirirani izgraditi s Generativnom umjetnom inteligencijom!

Kako bismo osigurali vaš uspjeh, na ovoj stranici su navedeni koraci za postavljanje, tehnički zahtjevi i gdje možete dobiti pomoć ako je potrebno.

## Koraci za postavljanje

Da biste započeli s ovim tečajem, trebate dovršiti sljedeće korake.

### 1. Forkajte ovaj repozitorij

[Forkajte cijeli ovaj repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati kod i rješavati izazove. Također možete [označiti zvjezdicom (🌟) ovaj repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli, kao i povezane repozitorije.

### 2. Kreirajte Codespace

Kako biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo da ovaj tečaj pokrećete u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

U svom fork-u: **Code -> Codespaces -> New on main**

![Dijalog koji prikazuje gumbe za kreiranje Codespace-a](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Dodajte tajnu

1. ⚙️ Ikona zupčanika -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.  
2. Nazovite je OPENAI_API_KEY, zalijepite svoj ključ, Spremite.

### 3. Što dalje?

| Želim…              | Idi na…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Započeti lekciju 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Raditi offline      | [`setup-local.md`](02-setup-local.md)                                   |
| Postaviti LLM pružatelja | [`providers.md`](03-providers.md)                                        |
| Upoznati druge polaznike | [Pridružite se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rješavanje problema

| Simptom                                   | Rješenje                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Izgradnja kontejnera traje > 10 min       | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal nije povezan; kliknite **+** ➜ *bash*                  |
| `401 Unauthorized` od OpenAI              | Pogrešan / istekao `OPENAI_API_KEY`                             |
| VS Code prikazuje “Dev container mounting…” | Osvježite karticu preglednika—Codespaces ponekad gubi vezu      |
| Nedostaje kernel za Notebook              | Izbornik Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-bazirani sustavi:

   ```bash
   touch .env
   ```
  
   Windows:

   ```cmd
   echo . > .env
   ```
  
3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++ ili bilo kojem drugom uređivaču). Dodajte sljedeći redak u datoteku, zamjenjujući `your_github_token_here` svojim stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```
  
4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako već niste, trebate instalirati paket `python-dotenv` kako biste učitali varijable okruženja iz `.env` datoteke u svoju Python aplikaciju. Možete ga instalirati pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```
  
6. **Učitajte varijable okruženja u svoj Python skript**: U svom Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okruženja iz `.env` datoteke:

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

Da biste pokrenuli kod lokalno na svom računalu, trebate imati neku verziju [Python instaliranog](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Zatim, kako biste koristili repozitorij, trebate ga klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```
  
Kada sve preuzmete, možete početi!

## Opcionalni koraci

### Instalacija Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.  
Conda je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni putem `pip`.

Možete slijediti [vodič za instalaciju MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kako biste ga postavili.

Nakon instalacije Miniconda, trebate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ako već niste).

Zatim trebate kreirati virtualno okruženje. Da biste to učinili s Conda, kreirajte novu datoteku okruženja (_environment.yml_). Ako pratite upute koristeći Codespaces, kreirajte ovu datoteku unutar direktorija `.devcontainer`, dakle `.devcontainer/environment.yml`.

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
  
Ako naiđete na greške koristeći conda, možete ručno instalirati Microsoft AI Libraries koristeći sljedeću naredbu u terminalu.

```
conda install -c microsoft azure-ai-ml
```
  
Datoteka okruženja specificira potrebne ovisnosti. `<environment-name>` odnosi se na ime koje želite koristiti za svoje Conda okruženje, a `<python-version>` je verzija Pythona koju želite koristiti, na primjer, `3` je najnovija glavna verzija Pythona.

Kada to završite, možete kreirati svoje Conda okruženje pokretanjem sljedećih naredbi u naredbenom retku/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```
  
Pogledajte [vodič za Conda okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na bilo kakve probleme.

### Korištenje Visual Studio Code-a s ekstenzijom za Python

Preporučujemo korištenje uređivača [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s instaliranom [ekstenzijom za podršku Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Međutim, ovo je samo preporuka, a ne obavezan zahtjev.

> **Napomena**: Otvaranjem repozitorija tečaja u VS Code-u, imate opciju postaviti projekt unutar kontejnera. To je moguće zbog [posebnog `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktorija koji se nalazi unutar repozitorija tečaja. Više o tome kasnije.

> **Napomena**: Kada klonirate i otvorite direktorij u VS Code-u, automatski će vam se predložiti instalacija ekstenzije za podršku Pythona.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u kontejneru, odbijte taj zahtjev kako biste koristili lokalno instaliranu verziju Pythona.

### Korištenje Jupytera u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) izravno u svom pregledniku. I klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pružaju ugodno razvojno okruženje s funkcijama poput automatskog dovršavanja, isticanja koda itd.

Za pokretanje Jupytera lokalno, otvorite terminal/naredbeni redak, idite u direktorij tečaja i izvršite:

```bash
jupyter notebook
```
  
ili

```bash
jupyterhub
```
  
Ovo će pokrenuti Jupyter instancu, a URL za pristup bit će prikazan unutar prozora naredbenog retka.

Kada pristupite URL-u, trebali biste vidjeti sadržaj tečaja i moći navigirati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

### Pokretanje u kontejneru

Alternativa postavljanju svega na svom računalu ili Codespace-u je korištenje [kontejnera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Poseban `.devcontainer` direktorij unutar repozitorija tečaja omogućuje VS Code-u postavljanje projekta unutar kontejnera. Izvan Codespaces-a, to će zahtijevati instalaciju Dockera, i iskreno, uključuje malo više posla, pa to preporučujemo samo onima s iskustvom u radu s kontejnerima.

Jedan od najboljih načina za zaštitu vaših API ključeva prilikom korištenja GitHub Codespaces-a je korištenje Codespace Secrets. Slijedite [vodič za upravljanje tajnama u Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kako biste saznali više o tome.

## Lekcije i tehnički zahtjevi

Tečaj sadrži 6 konceptualnih lekcija i 6 lekcija kodiranja.

Za lekcije kodiranja koristimo Azure OpenAI Service. Trebat će vam pristup Azure OpenAI servisu i API ključ za pokretanje ovog koda. Možete se prijaviti za pristup [ispunjavanjem ove prijave](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Dok čekate da vaša prijava bude obrađena, svaka lekcija kodiranja također uključuje `README.md` datoteku u kojoj možete pregledati kod i rezultate.

## Korištenje Azure OpenAI servisa po prvi put

Ako prvi put radite s Azure OpenAI servisom, slijedite ovaj vodič o tome kako [kreirati i implementirati resurs Azure OpenAI servisa.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korištenje OpenAI API-ja po prvi put

Ako prvi put radite s OpenAI API-jem, slijedite vodič o tome kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge polaznike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje s drugim polaznicima. Ovo je sjajan način za umrežavanje s drugim poduzetnicima, graditeljima, studentima i svima koji žele unaprijediti svoje znanje o Generativnoj umjetnoj inteligenciji.

[![Pridružite se Discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim projekta također će biti prisutan na ovom Discord serveru kako bi pomogao polaznicima.

## Doprinesite

Ovaj tečaj je inicijativa otvorenog koda. Ako primijetite područja za poboljšanje ili probleme, slobodno kreirajte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim projekta će pratiti sve doprinose. Doprinos otvorenom kodu je sjajan način za izgradnju vaše karijere u području Generativne umjetne inteligencije.

Većina doprinosa zahtijeva da se složite s Ugovorom o licenci za suradnike (CLA) kojim izjavljujete da imate pravo i stvarno dajete prava za korištenje vašeg doprinosa. Za detalje, posjetite [CLA, web stranicu Ugovora o licenci za suradnike](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: prilikom prevođenja teksta u ovom repozitoriju, molimo vas da ne koristite strojno prevođenje. Provjerit ćemo prijevode putem zajednice, stoga se prijavite za prijevod samo na jezicima na kojima ste stručni.

Kada pošaljete pull request, CLA-bot će automatski odrediti trebate li dostaviti CLA i označiti PR na odgovarajući način (npr. oznakom, komentarom). Jednostavno slijedite upute koje pruža bot. To ćete trebati učiniti samo jednom za sve repozitorije koji koriste naš CLA.

Ovaj projekt je usvojio [Microsoftov Kodeks ponašanja za otvoreni kod](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o Kodeksu ponašanja ili kontaktirajte [Email opencode](opencode@microsoft.com) s dodatnim pitanjima ili komentarima.

## Krenimo!
Sada kada ste završili potrebne korake za završetak ovog tečaja, krenimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.