<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T17:23:45+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "hr"
}
-->
# Odabir i konfiguracija LLM pružatelja usluga 🔑

Zadaci **mogu** biti postavljeni da rade s jednim ili više Large Language Model (LLM) implementacija putem podržanog pružatelja usluga poput OpenAI, Azure ili Hugging Face. Oni pružaju _hostanu krajnju točku_ (API) kojoj možemo pristupiti programski s odgovarajućim vjerodajnicama (API ključ ili token). U ovom tečaju raspravljamo o ovim pružateljima:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznolikim modelima uključujući osnovnu GPT seriju.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s fokusom na spremnost za poduzeća
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i poslužitelj za izvođenje

**Za ove vježbe morat ćete koristiti vlastite račune**. Zadaci su opcionalni pa možete odabrati postavljanje jednog, svih - ili nijednog - pružatelja usluga prema vašim interesima. Nekoliko smjernica za prijavu:

| Prijava | Trošak | API ključ | Igralište | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cijene](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na razini projekta](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez koda, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Više dostupnih modela |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cijene](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Brzi početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Brzi početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Potrebna prijava za pristup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cijene](https://huggingface.co/pricing) | [Pristupni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Slijedite upute u nastavku za _konfiguraciju_ ovog repozitorija za rad s različitim pružateljima. Zadaci koji zahtijevaju određenog pružatelja sadržavat će jedan od ovih oznaka u nazivu datoteke:

- `aoai` - zahtijeva Azure OpenAI krajnju točku, ključ
- `oai` - zahtijeva OpenAI krajnju točku, ključ
- `hf` - zahtijeva Hugging Face token

Možete konfigurirati jednog, nijednog ili sve pružatelje. Povezani zadaci će jednostavno prijaviti grešku ako nedostaju vjerodajnice.

## Kreirajte `.env` datoteku

Pretpostavljamo da ste već pročitali gore navedene upute, prijavili se kod relevantnog pružatelja i dobili potrebne vjerodajnice za autentifikaciju (API_KEY ili token). U slučaju Azure OpenAI, pretpostavljamo da imate i valjanu implementaciju Azure OpenAI usluge (krajnju točku) s barem jednim GPT modelom implementiranim za chat dovršavanje.

Sljedeći korak je konfigurirati vaše **lokalne varijable okoline** na sljedeći način:

1. Potražite u korijenskoj mapi datoteku `.env.copy` koja bi trebala sadržavati nešto poput ovoga:

   ```bash
   # OpenAI pružatelj usluga
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Zadano je postavljeno!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopirajte tu datoteku u `.env` koristeći naredbu ispod. Ova datoteka je _gitignore-irana_, čuvajući tajne sigurno.

   ```bash
   cp .env.copy .env
   ```

3. Ispunite vrijednosti (zamijenite rezervirana mjesta s desne strane `=`) kako je opisano u sljedećem odjeljku.

4. (Opcija) Ako koristite GitHub Codespaces, imate opciju spremiti varijable okoline kao _Codespaces tajne_ povezane s ovim repozitorijem. U tom slučaju nećete morati postavljati lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** Još uvijek ćete morati postaviti .env datoteku ako koristite Docker Desktop.

## Popunite `.env` datoteku

Pogledajmo brzo nazive varijabli da bismo razumjeli što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje usluge za ne-Azure OpenAI krajnje točke |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje te usluge |
| AZURE_OPENAI_ENDPOINT | Ovo je implementirana krajnja točka za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je krajnja točka implementacije modela za _generiranje teksta_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je krajnja točka implementacije modela za _ugradnju teksta_ |
| | |

Napomena: Posljednje dvije Azure OpenAI varijable odražavaju zadani model za chat dovršavanje (generiranje teksta) i pretraživanje vektora (ugradnje) redom. Upute za njihovo postavljanje bit će definirane u relevantnim zadacima.

## Konfigurirajte Azure: Iz portala

Vrijednosti Azure OpenAI krajnje točke i ključa pronaći ćete u [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), pa krenimo od tamo.

1. Idite na [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnoj traci (izbornik lijevo).
1. Kliknite **Show Keys** - trebali biste vidjeti sljedeće: KEY 1, KEY 2 i Endpoint.
1. Koristite vrijednost KEY 1 za AZURE_OPENAI_API_KEY
1. Koristite vrijednost Endpoint za AZURE_OPENAI_ENDPOINT

Sljedeće, trebamo krajnje točke za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnoj traci (lijevi izbornik) za Azure OpenAI resurs.
1. Na odredišnoj stranici kliknite **Manage Deployments**

Ovo će vas odvesti na web stranicu Azure OpenAI Studija, gdje ćemo pronaći ostale vrijednosti kako je opisano u nastavku.

## Konfigurirajte Azure: Iz Studija

1. Idite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašeg resursa** kao što je gore opisano.
1. Kliknite karticu **Deployments** (bočna traka, lijevo) da vidite trenutno implementirane modele.
1. Ako željeni model nije implementiran, koristite **Create new deployment** za njegovu implementaciju.
1. Trebat će vam model za _generiranje teksta_ - preporučujemo: **gpt-35-turbo**
1. Trebat će vam model za _ugradnju teksta_ - preporučujemo **text-embedding-ada-002**

Sada ažurirajte varijable okoline da odražavaju korišteni _Deployment name_. To će obično biti isto kao ime modela osim ako ga niste eksplicitno promijenili. Dakle, na primjer, mogli biste imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne zaboravite spremiti .env datoteku kada završite**. Sada možete izaći iz datoteke i vratiti se u upute za pokretanje bilježnice.

## Konfigurirajte OpenAI: Iz profila

Vaš OpenAI API ključ možete pronaći u svom [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se prijaviti za račun i stvoriti API ključ. Nakon što imate ključ, možete ga koristiti za popunjavanje varijable `OPENAI_API_KEY` u `.env` datoteci.

## Konfigurirajte Hugging Face: Iz profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih objavljivati ili dijeliti javno. Umjesto toga, stvorite novi token za ovu upotrebu projekta i kopirajte ga u `.env` datoteku pod varijablom `HUGGING_FACE_API_KEY`. _Napomena:_ Tehnički ovo nije API ključ, ali se koristi za autentifikaciju pa zadržavamo tu konvenciju imenovanja radi dosljednosti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->