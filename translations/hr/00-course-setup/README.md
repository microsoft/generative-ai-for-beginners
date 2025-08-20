<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:18:23+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hr"
}
-->
# Početak rada s ovim tečajem

Jako smo uzbuđeni što ćete započeti ovaj tečaj i vidjeti što ćete sve biti inspirirani izgraditi uz Generativnu AI!

Kako bismo osigurali vaš uspjeh, ova stranica opisuje korake postavljanja, tehničke zahtjeve i gdje potražiti pomoć ako vam zatreba.

## Koraci postavljanja

Za početak ovog tečaja, potrebno je dovršiti sljedeće korake.

### 1. Forkajte ovaj repozitorij

[Forkajte cijeli ovaj repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun kako biste mogli mijenjati kod i rješavati izazove. Također možete [označiti (🌟) ovaj repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) kako biste ga lakše pronašli zajedno s povezanim repozitorijima.

### 2. Kreirajte codespace

Kako biste izbjegli probleme s ovisnostima prilikom pokretanja koda, preporučujemo da ovaj tečaj pokrenete u [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To možete napraviti tako da na svojoj forkanoj verziji repozitorija odaberete opciju `Code` i zatim odaberete opciju **Codespaces**.

![Dijalog koji prikazuje gumbe za kreiranje codespacea](../../../00-course-setup/images/who-will-pay.webp)

### 3. Pohrana vaših API ključeva

Važno je čuvati vaše API ključeve sigurno kada gradite bilo koju vrstu aplikacije. Preporučujemo da ne pohranjujete API ključeve direktno u kod. Ako te podatke pošaljete u javni repozitorij, to može dovesti do sigurnosnih problema pa čak i neželjenih troškova ako ih netko zloupotrijebi.  
Evo vodiča korak po korak kako napraviti `.env` datoteku za Python i dodati `GITHUB_TOKEN`:

1. **Idite u direktorij vašeg projekta**: Otvorite terminal ili naredbeni redak i idite u korijenski direktorij projekta gdje želite kreirati `.env` datoteku.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte `.env` datoteku**: Koristite svoj omiljeni uređivač teksta za kreiranje nove datoteke nazvane `.env`. Ako koristite naredbeni redak, možete koristiti `touch` (na Unix sustavima) ili `echo` (na Windowsu):

   Unix sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++ ili bilo kojem drugom). Dodajte sljedeći redak u datoteku, zamjenjujući `your_github_token_here` stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako već niste, trebate instalirati paket `python-dotenv` kako biste mogli učitati varijable okoline iz `.env` datoteke u vašu Python aplikaciju. Možete ga instalirati pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okoline u vaš Python skript**: U vašem Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okoline iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoj GitHub token i učitali ga u Python aplikaciju.

## Kako pokrenuti lokalno na vašem računalu

Da biste pokrenuli kod lokalno na svom računalu, potrebno je imati instaliranu neku verziju [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Zatim, da biste koristili repozitorij, potrebno ga je klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kad sve to imate, možete započeti!

## Opcionalni koraci

### Instalacija Miniconde

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conde](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona i nekoliko paketa.  
Conda je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni putem `pip`.

Možete pratiti [MiniConda vodič za instalaciju](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

Nakon instalacije Miniconde, trebate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ako to već niste napravili).

Zatim trebate kreirati virtualno okruženje. Da biste to napravili s Condom, kreirajte novu datoteku za okruženje (_environment.yml_). Ako pratite tečaj koristeći Codespaces, kreirajte ju unutar direktorija `.devcontainer`, dakle `.devcontainer/environment.yml`.

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

Ako naiđete na greške pri korištenju conde, možete ručno instalirati Microsoft AI biblioteke koristeći sljedeću naredbu u terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okruženja specificira potrebne ovisnosti. `<environment-name>` označava ime koje želite dati svom Conda okruženju, a `<python-version>` verziju Pythona koju želite koristiti, na primjer, `3` je najnovija glavna verzija Pythona.

Kad to napravite, možete kreirati Conda okruženje pokretanjem naredbi u naredbenom retku/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ako naiđete na probleme, pogledajte [Conda vodič za upravljanje okruženjima](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Korištenje Visual Studio Code s Python podrškom

Preporučujemo korištenje [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) uređivača s instaliranim [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ovaj tečaj. Ovo je preporuka, ali nije obavezno.

> **Napomena**: Otvaranjem repozitorija tečaja u VS Code imate opciju postaviti projekt unutar containera. To je moguće zahvaljujući [posebnom `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) direktoriju unutar repozitorija tečaja. O tome ćemo više kasnije.

> **Napomena**: Nakon što klonirate i otvorite direktorij u VS Code, automatski će vam se predložiti instalacija Python podrške.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u containeru, odbijte taj zahtjev ako želite koristiti lokalno instaliranu verziju Pythona.

### Korištenje Jupyter-a u pregledniku

Također možete raditi na projektu koristeći [Jupyter okruženje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direktno u pregledniku. I klasični Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nude ugodno razvojno okruženje s funkcijama poput automatskog dovršavanja, isticanja koda i slično.

Za pokretanje Jupyter-a lokalno, otvorite terminal/naredbeni redak, idite u direktorij tečaja i pokrenite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu, a URL za pristup bit će prikazan u prozoru naredbenog retka.

Kad pristupite URL-u, trebali biste vidjeti strukturu tečaja i moći otvoriti bilo koju `*.ipynb` datoteku. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

### Pokretanje u containeru

Alternativa postavljanju svega na vašem računalu ili Codespaceu je korištenje [containera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna `.devcontainer` mapa unutar repozitorija tečaja omogućuje VS Code-u da postavi projekt unutar containera. Izvan Codespacesa, to zahtijeva instalaciju Dockera i, iskreno, uključuje malo više posla, pa to preporučujemo samo onima koji imaju iskustva s containerima.

Jedan od najboljih načina da zaštitite svoje API ključeve prilikom korištenja GitHub Codespaces je korištenje Codespace Secrets. Molimo pratite vodič za [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) za više informacija.

## Lekcije i tehnički zahtjevi

Tečaj sadrži 6 konceptualnih lekcija i 6 lekcija kodiranja.

Za lekcije kodiranja koristimo Azure OpenAI Service. Trebat će vam pristup Azure OpenAI servisu i API ključ za pokretanje ovog koda. Možete se prijaviti za pristup [ispunjavajući ovu prijavu](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Dok čekate obradu svoje prijave, svaka lekcija kodiranja također uključuje `README.md` datoteku u kojoj možete pregledati kod i rezultate.

## Prvi put koristite Azure OpenAI Service

Ako prvi put radite s Azure OpenAI servisom, molimo slijedite ovaj vodič o tome kako [kreirati i implementirati Azure OpenAI Service resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvi put koristite OpenAI API

Ako prvi put radite s OpenAI API-jem, molimo slijedite vodič o tome kako [kreirati i koristiti sučelje.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Upoznajte druge polaznike

Kreirali smo kanale na našem službenom [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za upoznavanje drugih polaznika. Ovo je odličan način za umrežavanje s drugim poduzetnicima, graditeljima, studentima i svima koji žele napredovati u Generativnoj AI.

[![Pridruži se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim projekta također će biti prisutan na ovom Discord serveru kako bi pomogao polaznicima.

## Doprinos

Ovaj tečaj je open-source inicijativa. Ako primijetite područja za poboljšanje ili probleme, molimo kreirajte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ili prijavite [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim projekta prati sve doprinose. Doprinos open source projektima je izvrstan način za razvoj karijere u Generativnoj AI.

Većina doprinosa zahtijeva da se složite s Contributor License Agreement (CLA) koji potvrđuje da imate pravo i doista dajete prava za korištenje vašeg doprinosa. Za detalje posjetite [CLA, Contributor License Agreement web stranicu](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Važno: prilikom prevođenja teksta u ovom repozitoriju, molimo vas da ne koristite strojno prevođenje. Provjeravat ćemo prijevode putem zajednice, stoga se prijavljujte za prijevode samo ako ste u tom jeziku vješti.

Kada pošaljete pull request, CLA-bot će automatski utvrditi trebate li dostaviti CLA i označiti PR na odgovarajući način (npr. oznaka, komentar). Jednostavno slijedite upute bota. Ovo ćete morati napraviti samo jednom za sve repozitorije koji koriste naš CLA.

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za više informacija pročitajte FAQ o Code of Conduct ili kontaktirajte [Email opencode](opencode@microsoft.com) za dodatna pitanja ili komentare.

## Krenimo

Sada kada ste dovršili potrebne korake za ovaj tečaj, krenimo s [uvodom u Generativnu AI i LLM-ove](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.