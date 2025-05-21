<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T13:01:35+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hr"
}
-->
# Postavite svoj razvojni okoliš

Postavili smo ovaj repozitorij i tečaj s [razvojnim kontejnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalni runtime koji može podržavati razvoj za Python3, .NET, Node.js i Java. Srodna konfiguracija definirana je u datoteci `devcontainer.json` koja se nalazi u mapi `.devcontainer/` na korijenu ovog repozitorija.

Da biste aktivirali razvojni kontejner, pokrenite ga u [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za runtime u oblaku) ili u [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za lokalni runtime). Pročitajte [ovu dokumentaciju](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) za više detalja o tome kako razvojni kontejneri rade unutar VS Code.

> [!TIP]  
> Preporučujemo korištenje GitHub Codespaces za brz početak s minimalnim naporom. Pruža velikodušnu [kvotu za besplatno korištenje](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za osobne račune. Konfigurirajte [vrijeme neaktivnosti](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) kako biste zaustavili ili izbrisali neaktivne codespaces i maksimalno iskoristili svoju kvotu.

## 1. Izvršavanje zadataka

Svaka lekcija će imati _neobavezne_ zadatke koji mogu biti dostupni u jednom ili više programskih jezika uključujući: Python, .NET/C#, Java i JavaScript/TypeScript. Ovaj odjeljak pruža opće smjernice vezane uz izvršavanje tih zadataka.

### 1.1 Python zadaci

Python zadaci se pružaju ili kao aplikacije (datoteke `.py`) ili Jupyter bilježnice (datoteke `.ipynb`).
- Da biste pokrenuli bilježnicu, otvorite je u Visual Studio Code, zatim kliknite _Select Kernel_ (gore desno) i odaberite zadanu opciju Python 3. Sada možete _Run All_ za izvršavanje bilježnice.
- Da biste pokrenuli Python aplikacije s komandne linije, slijedite specifične upute za zadatak kako biste bili sigurni da ste odabrali prave datoteke i dali potrebne argumente.

## 2. Konfiguriranje pružatelja usluga

Zadaci **mogu** biti postavljeni za rad protiv jedne ili više implementacija velikih jezičnih modela (LLM) putem podržanog pružatelja usluga poput OpenAI, Azure ili Hugging Face. Oni pružaju _hostirani endpoint_ (API) kojem možemo pristupiti programatski s ispravnim vjerodajnicama (API ključ ili token). U ovom tečaju raspravljamo o ovim pružateljima:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznim modelima uključujući osnovnu seriju GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s fokusom na spremnost za poduzeća.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i server za inferenciju.

**Morat ćete koristiti svoje račune za ove vježbe**. Zadatci su neobavezni pa možete odlučiti postaviti jednog, sve - ili nijednog - od pružatelja usluga ovisno o vašim interesima. Neke smjernice za prijavu:

| Prijava | Trošak | API ključ | Igralište | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cijene](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekt-bazirano](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez koda, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupni višestruki modeli |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cijene](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Morate unaprijed aplicirati za pristup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cijene](https://huggingface.co/pricing) | [Pristupni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Slijedite dolje navedene upute za _konfiguriranje_ ovog repozitorija za korištenje s različitim pružateljima usluga. Zadatci koji zahtijevaju određenog pružatelja usluga će sadržavati jednu od ovih oznaka u svom nazivu datoteke:
- `aoai` - zahtijeva Azure OpenAI endpoint, ključ
- `oai` - zahtijeva OpenAI endpoint, ključ
- `hf` - zahtijeva Hugging Face token

Možete konfigurirati jednog, nijednog ili sve pružatelje usluga. Srodni zadatci će jednostavno prijaviti grešku na nedostajuće vjerodajnice.

### 2.1. Kreirajte datoteku `.env`

Pretpostavljamo da ste već pročitali gore navedene smjernice i prijavili se kod relevantnog pružatelja usluga te dobili potrebne vjerodajnice za autentifikaciju (API_KEY ili token). U slučaju Azure OpenAI, pretpostavljamo da također imate valjanu implementaciju Azure OpenAI usluge (endpoint) s barem jednim GPT modelom implementiranim za završetak razgovora.

Sljedeći korak je konfiguriranje vaših **lokalnih varijabli okruženja** na sljedeći način:

1. Pogledajte u korijensku mapu za datoteku `.env.copy` koja bi trebala imati sadržaj poput ovog:

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

2. Kopirajte tu datoteku u `.env` koristeći naredbu ispod. Ova datoteka je _gitignore-d_, čuvajući tajne sigurno.

   ```bash
   cp .env.copy .env
   ```

3. Popunite vrijednosti (zamijenite rezervirane oznake na desnoj strani `=`) kako je opisano u sljedećem odjeljku.

3. (Opcija) Ako koristite GitHub Codespaces, imate opciju spremanja varijabli okruženja kao _Codespaces tajni_ povezane s ovim repozitorijem. U tom slučaju, nećete trebati postaviti lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** I dalje ćete morati postaviti .env datoteku ako koristite Docker Desktop umjesto toga.

### 2.2. Popunite datoteku `.env`

Pogledajmo brzo nazive varijabli da bismo razumjeli što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje usluge za ne-Azure OpenAI endpoint |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje te usluge |
| AZURE_OPENAI_ENDPOINT | Ovo je implementirani endpoint za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je endpoint za _generiranje teksta_ modela implementacije |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je endpoint za _ugrađivanje teksta_ modela implementacije |
| | |

Napomena: Posljednje dvije Azure OpenAI varijable odražavaju zadani model za završetak razgovora (generiranje teksta) i pretraživanje vektora (ugrađivanje) respektivno. Upute za njihovo postavljanje bit će definirane u relevantnim zadacima.

### 2.3 Konfigurirajte Azure: Iz portala

Vrijednosti za Azure OpenAI endpoint i ključ će se pronaći u [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) pa krenimo od tamo.

1. Idite na [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnom izborniku (izbornik lijevo).
1. Kliknite **Show Keys** - trebali biste vidjeti sljedeće: KLJUČ 1, KLJUČ 2 i Endpoint.
1. Koristite vrijednost KLJUČA 1 za AZURE_OPENAI_API_KEY
1. Koristite vrijednost Endpoint za AZURE_OPENAI_ENDPOINT

Sljedeće, trebamo endpoint za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnom izborniku (izbornik lijevo) za Azure OpenAI resurs.
1. Na odredišnoj stranici kliknite **Manage Deployments**

Ovo će vas odvesti na web stranicu Azure OpenAI Studio, gdje ćemo pronaći ostale vrijednosti kako je opisano dolje.

### 2.4 Konfigurirajte Azure: Iz studija

1. Navigirajte do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašeg resursa** kako je opisano gore.
1. Kliknite karticu **Deployments** (bočni izbornik, lijevo) za pregled trenutno implementiranih modela.
1. Ako vaš željeni model nije implementiran, koristite **Create new deployment** za implementaciju.
1. Trebat će vam _model za generiranje teksta_ - preporučujemo: **gpt-35-turbo**
1. Trebat će vam _model za ugrađivanje teksta_ - preporučujemo **text-embedding-ada-002**

Sada ažurirajte varijable okruženja kako bi odražavale _Ime implementacije_ koje ste koristili. Ovo će obično biti isto kao ime modela osim ako ste ga eksplicitno promijenili. Dakle, kao primjer, mogli biste imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne zaboravite spremiti .env datoteku kad završite**. Sada možete izaći iz datoteke i vratiti se na upute za pokretanje bilježnice.

### 2.5 Konfigurirajte OpenAI: Iz profila

Vaš OpenAI API ključ možete pronaći u svom [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se prijaviti za račun i kreirati API ključ. Kada imate ključ, možete ga koristiti za popunjavanje varijable `OPENAI_API_KEY` u datoteci `.env`.

### 2.6 Konfigurirajte Hugging Face: Iz profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Pristupni tokeni](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih objavljivati ili dijeliti javno. Umjesto toga, kreirajte novi token za ovu upotrebu projekta i kopirajte ga u datoteku `.env` pod varijablom `HUGGING_FACE_API_KEY`. _Napomena:_ Tehnički, ovo nije API ključ, ali se koristi za autentifikaciju pa zadržavamo tu konvenciju imenovanja radi dosljednosti.

**Odricanje odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo za točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.