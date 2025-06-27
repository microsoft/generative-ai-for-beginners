<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:31:05+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hr"
}
-->
# Postavite svoje razvojno okruženje

Postavili smo ovaj repozitorij i tečaj s [razvojnim kontejnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalno okruženje koje može podržati razvoj u Python3, .NET, Node.js i Javi. Povezana konfiguracija definirana je u datoteci `devcontainer.json` smještenoj u mapi `.devcontainer/` na korijenu ovog repozitorija.

Da biste aktivirali razvojni kontejner, pokrenite ga u [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za okruženje u oblaku) ili u [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za lokalno okruženje). Pročitajte [ovu dokumentaciju](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) za više detalja o tome kako razvojni kontejneri rade unutar VS Code-a.

> [!TIP]  
> Preporučujemo korištenje GitHub Codespaces za brzi početak uz minimalan trud. Pruža velikodušnu [kvotu besplatne upotrebe](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za osobne račune. Konfigurirajte [vrijeme čekanja](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) za zaustavljanje ili brisanje neaktivnih codespacesa kako biste maksimalno iskoristili svoju kvotu.

## 1. Izvršavanje zadataka

Svaka lekcija će imati _opcionalne_ zadatke koji mogu biti dostupni na jednom ili više programskih jezika uključujući: Python, .NET/C#, Java i JavaScript/TypeScript. Ovaj odjeljak pruža opće smjernice vezane uz izvršavanje tih zadataka.

### 1.1 Python zadaci

Python zadaci su dostupni ili kao aplikacije (datoteke `.py`) ili Jupyter bilježnice (datoteke `.ipynb`).
- Za pokretanje bilježnice, otvorite je u Visual Studio Code, zatim kliknite _Select Kernel_ (gore desno) i odaberite zadanu Python 3 opciju koja je prikazana. Sada možete odabrati _Run All_ za izvršavanje bilježnice.
- Za pokretanje Python aplikacija iz naredbenog retka, slijedite specifične upute za zadatak kako biste bili sigurni da ste odabrali prave datoteke i osigurali potrebne argumente.

## 2. Konfiguriranje pružatelja usluga

Zadaci **mogu** također biti postavljeni za rad protiv jedne ili više implementacija velikih jezičnih modela (LLM) putem podržanog pružatelja usluga kao što su OpenAI, Azure ili Hugging Face. Oni pružaju _hostirani endpoint_ (API) kojem možemo pristupiti programski s pravim vjerodajnicama (API ključ ili token). U ovom tečaju raspravljamo o ovim pružateljima:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznolikim modelima uključujući osnovnu GPT seriju.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s fokusom na poslovnu spremnost
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i poslužitelj za inferenciju

**Trebate koristiti svoje vlastite račune za ove vježbe**. Zadaci su opcionalni pa možete odabrati postaviti jednog, sve - ili nijednog - od pružatelja prema vašim interesima. Neke smjernice za prijavu:

| Prijava | Trošak | API ključ | Playground | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cijene](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na bazi projekta](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez koda, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupno više modela |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cijene](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Brzi početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Brzi početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Morate unaprijed aplicirati za pristup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cijene](https://huggingface.co/pricing) | [Pristupni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Slijedite dolje navedene upute za _konfiguriranje_ ovog repozitorija za upotrebu s različitim pružateljima. Zadaci koji zahtijevaju specifičnog pružatelja će sadržavati jedan od ovih oznaka u svom imenu datoteke:
 - `aoai` - zahtijeva Azure OpenAI endpoint, ključ
 - `oai` - zahtijeva OpenAI endpoint, ključ
 - `hf` - zahtijeva Hugging Face token

Možete konfigurirati jednog, nijednog ili sve pružatelje. Povezani zadaci će jednostavno prijaviti grešku zbog nedostatka vjerodajnica.

### 2.1. Kreirajte datoteku `.env`

Pretpostavljamo da ste već pročitali gornje smjernice i prijavili se kod relevantnog pružatelja te dobili potrebne vjerodajnice za autentifikaciju (API_KEY ili token). U slučaju Azure OpenAI, pretpostavljamo da također imate valjanu implementaciju Azure OpenAI usluge (endpoint) s barem jednim GPT modelom implementiranim za završavanje razgovora.

Sljedeći korak je konfiguriranje vaših **lokalnih varijabli okruženja** kako slijedi:

1. Potražite u korijenskoj mapi datoteku `.env.copy` koja bi trebala imati sadržaj poput ovog:

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

2. Kopirajte tu datoteku u `.env` koristeći donju naredbu. Ova datoteka je _gitignore-d_, čuvajući tajne sigurno.

   ```bash
   cp .env.copy .env
   ```

3. Popunite vrijednosti (zamijenite rezervirana mjesta na desnoj strani `=`) kako je opisano u sljedećem odjeljku.

3. (Opcija) Ako koristite GitHub Codespaces, imate mogućnost spremanja varijabli okruženja kao _Codespaces tajne_ povezane s ovim repozitorijem. U tom slučaju, nećete trebati postaviti lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** I dalje ćete trebati postaviti .env datoteku ako koristite Docker Desktop.

### 2.2. Popunite datoteku `.env`

Pogledajmo brzo imena varijabli kako bismo razumjeli što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je pristupni token korisnika koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje usluge za ne-Azure OpenAI endpointove |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje te usluge |
| AZURE_OPENAI_ENDPOINT | Ovo je implementirani endpoint za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je _text generation_ endpoint za implementaciju modela |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je _text embeddings_ endpoint za implementaciju modela |
| | |

Napomena: Posljednje dvije Azure OpenAI varijable odražavaju zadani model za završavanje razgovora (generiranje teksta) i pretraživanje vektora (ugrađivanje) respektivno. Upute za njihovo postavljanje bit će definirane u relevantnim zadacima.

### 2.3 Konfigurirajte Azure: Iz portala

Vrijednosti Azure OpenAI endpointa i ključa mogu se pronaći u [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) pa krenimo od tamo.

1. Idite na [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnoj traci (izbornik s lijeve strane).
1. Kliknite **Show Keys** - trebali biste vidjeti sljedeće: KEY 1, KEY 2 i Endpoint.
1. Koristite vrijednost KEY 1 za AZURE_OPENAI_API_KEY
1. Koristite vrijednost Endpoint za AZURE_OPENAI_ENDPOINT

Sljedeće, trebamo endpointove za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnoj traci (lijevi izbornik) za Azure OpenAI resurs.
1. Na odredišnoj stranici, kliknite **Manage Deployments**

Ovo će vas odvesti na web stranicu Azure OpenAI Studio, gdje ćemo pronaći ostale vrijednosti kako je opisano u nastavku.

### 2.4 Konfigurirajte Azure: Iz Studija

1. Idite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz svog resursa** kako je gore opisano.
1. Kliknite karticu **Deployments** (bočna traka, lijevo) za pregled trenutno implementiranih modela.
1. Ako vaš željeni model nije implementiran, koristite **Create new deployment** za njegovu implementaciju.
1. Trebat će vam _text-generation_ model - preporučujemo: **gpt-35-turbo**
1. Trebat će vam _text-embedding_ model - preporučujemo **text-embedding-ada-002**

Sada ažurirajte varijable okruženja kako bi odražavale _Deployment name_ koji ste koristili. Ovo će obično biti isto kao i ime modela osim ako ga niste eksplicitno promijenili. Dakle, kao primjer, mogli biste imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne zaboravite spremiti .env datoteku kada završite**. Sada možete zatvoriti datoteku i vratiti se upute za pokretanje bilježnice.

### 2.5 Konfigurirajte OpenAI: Iz profila

Vaš OpenAI API ključ može se pronaći na vašem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se prijaviti za račun i stvoriti API ključ. Kada imate ključ, možete ga koristiti za popunjavanje varijable `OPENAI_API_KEY` u datoteci `.env`.

### 2.6 Konfigurirajte Hugging Face: Iz profila

Vaš Hugging Face token može se pronaći u vašem profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih javno objavljivati ili dijeliti. Umjesto toga, stvorite novi token za korištenje ovog projekta i kopirajte ga u datoteku `.env` pod varijablu `HUGGING_FACE_API_KEY`. _Napomena:_ Ovo tehnički nije API ključ, ali se koristi za autentifikaciju pa zadržavamo tu konvenciju imenovanja radi konzistentnosti.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.