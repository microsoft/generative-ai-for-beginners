<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:38:04+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hr"
}
-->
# Postavljanje vašeg razvojog okruženja

Ovaj repozitorij i tečaj postavljeni su s [razvojnim kontejnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalno runtime okruženje koje podržava razvoj u Python3, .NET, Node.js i Javi. Povezana konfiguracija definirana je u datoteci `devcontainer.json` koja se nalazi u mapi `.devcontainer/` u korijenu ovog repozitorija.

Za aktivaciju razvojnog kontejnera, pokrenite ga u [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za runtime u oblaku) ili u [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za lokalni runtime na uređaju). Pročitajte [ovu dokumentaciju](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) za više detalja o radu razvojnih kontejnera unutar VS Code-a.

> [!TIP]  
> Preporučujemo korištenje GitHub Codespaces za brz početak s minimalnim naporom. Nudi velikodušan [besplatni kvotu korištenja](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za osobne račune. Konfigurirajte [timeout-e](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) za zaustavljanje ili brisanje neaktivnih codespaces-a kako biste maksimalno iskoristili kvotu.

## 1. Izvršavanje zadataka

Svaka lekcija može imati _neobavezne_ zadatke koji mogu biti dostupni u jednom ili više programskih jezika, uključujući: Python, .NET/C#, Java i JavaScript/TypeScript. Ovaj odjeljak daje opće smjernice vezane uz izvršavanje tih zadataka.

### 1.1 Python zadaci

Python zadaci su dostupni kao aplikacije (`.py` datoteke) ili Jupyter bilježnice (`.ipynb` datoteke).  
- Za pokretanje bilježnice, otvorite je u Visual Studio Code-u, zatim kliknite na _Select Kernel_ (u gornjem desnom kutu) i odaberite zadanu opciju Python 3. Sada možete kliknuti na _Run All_ za izvršavanje bilježnice.  
- Za pokretanje Python aplikacija iz komandne linije, slijedite upute specifične za zadatak kako biste odabrali ispravne datoteke i unijeli potrebne argumente.

## 2. Konfiguriranje pružatelja usluga

Zadaci **mogu** biti postavljeni da rade s jednim ili više Large Language Model (LLM) servisa putem podržanih pružatelja usluga poput OpenAI, Azure ili Hugging Face. Oni nude _hostani endpoint_ (API) kojem možemo pristupiti programatski s odgovarajućim vjerodajnicama (API ključ ili token). U ovom tečaju obrađujemo sljedeće pružatelje:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznolikim modelima uključujući osnovnu GPT seriju.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s fokusom na spremnost za poduzeća  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i inference server

**Za ove vježbe trebat ćete koristiti vlastite račune**. Zadaci su neobavezni pa možete odabrati postavljanje jednog, svih ili nijednog pružatelja, ovisno o vašim interesima. Evo nekoliko smjernica za registraciju:

| Registracija | Cijena | API ključ | Playground | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Cijene](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Na razini projekta](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupno više modela |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Cijene](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Potrebna je prethodna prijava za pristup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cijene](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Slijedite upute u nastavku za _konfiguriranje_ ovog repozitorija za rad s različitim pružateljima. Zadaci koji zahtijevaju određenog pružatelja imat će jedan od ovih tagova u nazivu datoteke:  
 - `aoai` - zahtijeva Azure OpenAI endpoint i ključ  
 - `oai` - zahtijeva OpenAI endpoint i ključ  
 - `hf` - zahtijeva Hugging Face token

Možete konfigurirati jednog, nijednog ili sve pružatelje. Zadaci koji zahtijevaju određene vjerodajnice jednostavno će prijaviti grešku ako ih nema.

### 2.1. Kreiranje `.env` datoteke

Pretpostavljamo da ste već pročitali gore navedene upute, registrirali se kod relevantnog pružatelja i dobili potrebne vjerodajnice za autentifikaciju (API_KEY ili token). U slučaju Azure OpenAI, pretpostavljamo da imate valjanu implementaciju Azure OpenAI servisa (endpoint) s barem jednim GPT modelom za chat completion.

Sljedeći korak je konfigurirati vaše **lokalne varijable okruženja** na sljedeći način:

1. Potražite u korijenskoj mapi datoteku `.env.copy` koja bi trebala sadržavati nešto poput ovoga:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopirajte tu datoteku u `.env` koristeći naredbu ispod. Ova datoteka je _gitignore-ana_, što znači da tajne ostaju sigurne.

   ```bash
   cp .env.copy .env
   ```

3. Ispunite vrijednosti (zamijenite oznake s desne strane znaka `=`) kako je opisano u sljedećem odjeljku.

3. (Opcionalno) Ako koristite GitHub Codespaces, imate opciju spremanja varijabli okruženja kao _Codespaces secrets_ povezanih s ovim repozitorijem. U tom slučaju nećete morati postavljati lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** I dalje ćete morati postaviti .env datoteku ako koristite Docker Desktop.

### 2.2. Popunjavanje `.env` datoteke

Pogledajmo brzo nazive varijabli da bismo razumjeli što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje servisa za ne-Azure OpenAI endpoint-e |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje Azure OpenAI servisa |
| AZURE_OPENAI_ENDPOINT | Ovo je endpoint implementiranog Azure OpenAI resursa |
| AZURE_OPENAI_DEPLOYMENT | Ovo je endpoint implementacije modela za _generiranje teksta_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je endpoint implementacije modela za _tekstualne embeddings_ |
| | |

Napomena: Posljednje dvije Azure OpenAI varijable odnose se na zadani model za chat completion (generiranje teksta) i pretraživanje vektora (embeddings). Upute za njihovo postavljanje bit će definirane u relevantnim zadacima.

### 2.3. Konfiguriranje Azure: Iz portala

Vrijednosti za Azure OpenAI endpoint i ključ možete pronaći u [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), pa krenimo od tamo.

1. Idite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Kliknite na opciju **Keys and Endpoint** u bočnoj traci (izbornik lijevo).  
3. Kliknite na **Show Keys** - trebali biste vidjeti sljedeće: KEY 1, KEY 2 i Endpoint.  
4. Koristite vrijednost KEY 1 za AZURE_OPENAI_API_KEY  
5. Koristite vrijednost Endpoint za AZURE_OPENAI_ENDPOINT

Sljedeće, trebamo endpoint-e za specifične modele koje smo implementirali.

1. Kliknite na opciju **Model deployments** u bočnoj traci (lijevi izbornik) za Azure OpenAI resurs.  
2. Na odredišnoj stranici kliknite na **Manage Deployments**

Ovo će vas odvesti na web stranicu Azure OpenAI Studija, gdje ćemo pronaći ostale vrijednosti kako je opisano u nastavku.

### 2.4. Konfiguriranje Azure: Iz Studija

1. Idite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašeg resursa** kao što je gore opisano.  
2. Kliknite na karticu **Deployments** (bočna traka, lijevo) da vidite trenutno implementirane modele.  
3. Ako željeni model nije implementiran, koristite opciju **Create new deployment** za njegovu implementaciju.  
4. Trebat će vam model za _generiranje teksta_ - preporučujemo: **gpt-35-turbo**  
5. Trebat će vam model za _tekstualne embeddings_ - preporučujemo **text-embedding-ada-002**

Sada ažurirajte varijable okruženja da odražavaju _Deployment name_ koji koristite. To će obično biti isto kao ime modela, osim ako ste ga eksplicitno promijenili. Na primjer, mogli biste imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne zaboravite spremiti .env datoteku kada završite**. Sada možete zatvoriti datoteku i vratiti se upute za pokretanje bilježnice.

### 2.5. Konfiguriranje OpenAI: Iz profila

Vaš OpenAI API ključ možete pronaći u svom [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se registrirati i kreirati API ključ. Nakon što dobijete ključ, upotrijebite ga za popunjavanje varijable `OPENAI_API_KEY` u `.env` datoteci.

### 2.6. Konfiguriranje Hugging Face: Iz profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih objavljivati ili dijeliti javno. Umjesto toga, kreirajte novi token za ovu upotrebu projekta i kopirajte ga u `.env` datoteku pod varijablom `HUGGING_FACE_API_KEY`. _Napomena:_ Tehnički ovo nije API ključ, ali se koristi za autentifikaciju pa zadržavamo ovaj naziv radi konzistentnosti.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.