<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T13:00:55+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sr"
}
-->
# Podesite svoje razvojno okruženje

Ovaj repozitorijum i kurs smo postavili sa [razvojnim kontejnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalno okruženje koje može podržati razvoj u Python3, .NET, Node.js i Java. Povezana konfiguracija je definisana u `devcontainer.json` fajlu koji se nalazi u `.devcontainer/` folderu na početku ovog repozitorijuma.

Da biste aktivirali razvojni kontejner, pokrenite ga u [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za okruženje hostovano u oblaku) ili u [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za lokalno okruženje na uređaju). Pročitajte [ovu dokumentaciju](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) za više detalja o tome kako razvojni kontejneri rade unutar VS Code.

> [!TIP]  
> Preporučujemo korišćenje GitHub Codespaces za brz početak sa minimalnim naporom. Pruža velikodušnu [besplatnu kvotu](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za lične naloge. Konfigurišite [vremenske limite](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) da zaustavite ili obrišete neaktivne kodspese kako biste maksimalno iskoristili svoju kvotu.


## 1. Izvršavanje zadataka

Svaka lekcija će imati _opciono_ zadatke koji mogu biti dati u jednom ili više programskih jezika uključujući: Python, .NET/C#, Java i JavaScript/TypeScript. Ovaj deo pruža opšte smernice vezane za izvršavanje tih zadataka.

### 1.1 Python zadaci

Python zadaci su dati ili kao aplikacije (`.py` fajlovi) ili Jupyter sveske (`.ipynb` fajlovi).
- Da biste pokrenuli svesku, otvorite je u Visual Studio Code, zatim kliknite _Select Kernel_ (gore desno) i izaberite podrazumevanu Python 3 opciju koja se prikazuje. Sada možete _Run All_ da izvršite svesku.
- Da biste pokrenuli Python aplikacije sa komandne linije, pratite instrukcije specifične za zadatak kako biste osigurali da izaberete prave fajlove i obezbedite potrebne argumente.

## 2. Konfigurisanje provajdera

Zadaci **mogu** biti postavljeni da rade sa jednim ili više Large Language Model (LLM) implementacija putem podržanog provajdera usluga kao što su OpenAI, Azure ili Hugging Face. Oni pružaju _hostovan endpoint_ (API) kojem možemo pristupiti programatski sa pravim akreditivima (API ključ ili token). U ovom kursu, razmatramo ove provajdere:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) sa raznovrsnim modelima uključujući osnovnu GPT seriju.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele sa fokusom na spremnost za preduzeća.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i server za inferencu.

**Trebaće vam sopstveni nalozi za ove vežbe**. Zadaci su opcioni, tako da možete izabrati da postavite jednog, sve - ili nijednog - provajdera, u zavisnosti od vaših interesa. Neke smernice za prijavu:

| Prijava | Trošak | API ključ | Igralište | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cena](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Bazirano na projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez koda, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Više modela dostupno |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cena](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Brzi početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Brzi početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Morate se unapred prijaviti za pristup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cena](https://huggingface.co/pricing) | [Pristupni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Pratite dole navedene upute za _konfigurisanje_ ovog repozitorijuma za upotrebu sa različitim provajderima. Zadaci koji zahtevaju određenog provajdera će sadržati jedan od ovih tagova u svom imenu fajla:
- `aoai` - zahteva Azure OpenAI endpoint, ključ
- `oai` - zahteva OpenAI endpoint, ključ
- `hf` - zahteva Hugging Face token

Možete konfigurisati jednog, nijednog ili sve provajdere. Povezani zadaci će jednostavno prijaviti grešku na nedostajućim akreditivima.

### 2.1. Kreirajte `.env` fajl

Pretpostavljamo da ste već pročitali smernice iznad i prijavili se kod relevantnog provajdera, te dobili potrebne akreditivne podatke (API_KEY ili token). U slučaju Azure OpenAI, pretpostavljamo da imate validnu implementaciju Azure OpenAI servisa (endpoint) sa barem jednim GPT modelom implementiranim za završavanje razgovora.

Sledeći korak je da konfigurišete svoje **lokalne varijable okruženja** na sledeći način:

1. Potražite u osnovnom folderu `.env.copy` fajl koji bi trebalo da ima sadržaj poput ovog:

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

2. Kopirajte taj fajl u `.env` koristeći komandu ispod. Ovaj fajl je _gitignore-d_, čuvajući tajne bezbednim.

   ```bash
   cp .env.copy .env
   ```

3. Popunite vrednosti (zamenite rezervisana mesta na desnoj strani `=`) kao što je opisano u sledećem delu.

3. (Opcija) Ako koristite GitHub Codespaces, imate opciju da sačuvate varijable okruženja kao _Codespaces tajne_ povezane sa ovim repozitorijumom. U tom slučaju, nećete morati da postavljate lokalni .env fajl. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** I dalje ćete morati da postavite .env fajl ako koristite Docker Desktop.

### 2.2. Popunite `.env` fajl

Pogledajmo brzo nazive varijabli da bismo razumeli šta predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacioni ključ za korišćenje servisa za ne-Azure OpenAI endpoint |
| AZURE_OPENAI_API_KEY | Ovo je autorizacioni ključ za korišćenje tog servisa |
| AZURE_OPENAI_ENDPOINT | Ovo je implementirani endpoint za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je _text generation_ model implementacioni endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je _text embeddings_ model implementacioni endpoint |
| | |

Napomena: Poslednje dve Azure OpenAI varijable odražavaju podrazumevani model za završavanje razgovora (generisanje teksta) i pretragu vektora (embeddings) respektivno. Uputstva za njihovo postavljanje biće definisana u relevantnim zadacima.

### 2.3 Konfigurišite Azure: Sa Portala

Azure OpenAI endpoint i ključ vrednosti će se naći na [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), pa krenimo odatle.

1. Idite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnom panelu (meni levo).
1. Kliknite **Show Keys** - trebalo bi da vidite sledeće: KEY 1, KEY 2 i Endpoint.
1. Koristite KEY 1 vrednost za AZURE_OPENAI_API_KEY
1. Koristite Endpoint vrednost za AZURE_OPENAI_ENDPOINT

Dalje, trebaće nam endpointi za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnom panelu (meni levo) za Azure OpenAI resurs.
1. Na odredišnoj stranici kliknite **Manage Deployments**

Ovo će vas odvesti na Azure OpenAI Studio web stranicu, gde ćemo naći druge vrednosti kao što je opisano ispod.

### 2.4 Konfigurišite Azure: Sa Studija

1. Idite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašeg resursa** kao što je opisano iznad.
1. Kliknite na karticu **Deployments** (bočni panel, levo) da biste videli trenutno implementirane modele.
1. Ako vaš željeni model nije implementiran, koristite **Create new deployment** da ga implementirate.
1. Trebaće vam _text-generation_ model - preporučujemo: **gpt-35-turbo**
1. Trebaće vam _text-embedding_ model - preporučujemo **text-embedding-ada-002**

Sada ažurirajte varijable okruženja da odražavaju _Deployment name_ koji ste koristili. Ovo će obično biti isto kao ime modela osim ako ga niste eksplicitno promenili. Dakle, kao primer, možda imate:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne zaboravite da sačuvate .env fajl kada završite**. Sada možete zatvoriti fajl i vratiti se uputstvima za pokretanje sveske.

### 2.5 Konfigurišite OpenAI: Sa profila

Vaš OpenAI API ključ možete pronaći na svom [OpenAI nalogu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se prijaviti za nalog i kreirati API ključ. Kada imate ključ, možete ga koristiti za popunjavanje `OPENAI_API_KEY` varijable u `.env` fajlu.

### 2.6 Konfigurišite Hugging Face: Sa profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih objavljivati ili deliti javno. Umesto toga, kreirajte novi token za upotrebu u ovom projektu i kopirajte ga u `.env` fajl pod varijablom `HUGGING_FACE_API_KEY`. _Napomena:_ Ovo tehnički nije API ključ, ali se koristi za autentifikaciju, tako da zadržavamo tu konvenciju imenovanja radi doslednosti.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо ка тачности, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални људски превод. Нисмо одговорни за било каква погрешна разумевања или погрешна тумачења која произилазе из коришћења овог превода.