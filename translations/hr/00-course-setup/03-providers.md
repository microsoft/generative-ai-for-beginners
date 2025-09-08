<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:38:58+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "hr"
}
-->
# Odabir i konfiguracija LLM pružatelja usluga 🔑

Zadaci se **mogu** postaviti tako da rade s jednom ili više implementacija Velikih jezičnih modela (LLM) putem podržanih pružatelja usluga kao što su OpenAI, Azure ili Hugging Face. Oni nude _hostirani endpoint_ (API) kojem možemo pristupiti programatski uz odgovarajuće vjerodajnice (API ključ ili token). U ovom tečaju obrađujemo ove pružatelje:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznovrsnim modelima uključujući osnovnu GPT seriju.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s naglaskom na poslovnu primjenu
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i server za inferenciju

**Za ove vježbe ćete trebati koristiti vlastite račune**. Zadaci su opcionalni pa možete odabrati postaviti jednog, sve - ili nijednog - pružatelja, ovisno o vašim interesima. Evo nekoliko savjeta za prijavu:

| Prijava | Cijena | API ključ | Playground | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cjenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Po projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupno više modela |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cjenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Potrebno unaprijed zatražiti pristup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cjenik](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničen broj modela](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Slijedite upute u nastavku za _konfiguraciju_ ovog repozitorija za korištenje s različitim pružateljima. Zadaci koji zahtijevaju određenog pružatelja imat će jednu od ovih oznaka u nazivu datoteke:

- `aoai` - zahtijeva Azure OpenAI endpoint i ključ
- `oai` - zahtijeva OpenAI endpoint i ključ
- `hf` - zahtijeva Hugging Face token

Možete konfigurirati jednog, nijednog ili sve pružatelje. Povezani zadaci će jednostavno javiti grešku ako nedostaju vjerodajnice.

## Kreirajte `.env` datoteku

Pretpostavljamo da ste već pročitali gore navedene upute, prijavili se kod relevantnog pružatelja i dobili potrebne vjerodajnice za autentifikaciju (API_KEY ili token). Za Azure OpenAI pretpostavljamo da imate valjanu implementaciju Azure OpenAI usluge (endpoint) s barem jednim GPT modelom postavljenim za chat completion.

Sljedeći korak je konfigurirati **lokalne varijable okruženja** na sljedeći način:

1. U korijenskoj mapi pronađite datoteku `.env.copy` koja bi trebala sadržavati nešto ovako:

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

2. Kopirajte tu datoteku u `.env` pomoću naredbe ispod. Ova datoteka je _gitignore-ana_, čuvajući tajne podatke sigurnima.

   ```bash
   cp .env.copy .env
   ```

3. Unesite vrijednosti (zamijenite placeholder-e s desne strane `=`) kako je opisano u sljedećem odjeljku.

4. (Opcija) Ako koristite GitHub Codespaces, možete spremiti varijable okruženja kao _Codespaces secrets_ povezane s ovim repozitorijem. U tom slučaju nećete morati postavljati lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** I dalje ćete morati postaviti .env datoteku ako koristite Docker Desktop.

## Popunite `.env` datoteku

Pogledajmo brzo nazive varijabli da shvatimo što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje usluge za ne-Azure OpenAI endpoint-e |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje te usluge |
| AZURE_OPENAI_ENDPOINT | Ovo je postavljeni endpoint za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je endpoint za _generiranje teksta_ modela |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je endpoint za _ugradnju teksta_ modela |
| | |

Napomena: Zadnje dvije Azure OpenAI varijable odnose se na zadani model za chat completion (generiranje teksta) i pretraživanje vektora (ugradnje) redom. Upute za njihovo postavljanje bit će definirane u relevantnim zadacima.

## Konfigurirajte Azure: Preko Portala

Vrijednosti za Azure OpenAI endpoint i ključ pronaći ćete u [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), pa krenimo od tamo.

1. Idite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnom izborniku (lijevo).
1. Kliknite **Show Keys** - trebali biste vidjeti: KEY 1, KEY 2 i Endpoint.
1. Za AZURE_OPENAI_API_KEY koristite vrijednost KEY 1
1. Za AZURE_OPENAI_ENDPOINT koristite vrijednost Endpoint

Sljedeće, trebamo endpoint-e za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnom izborniku (lijevo) za Azure OpenAI resurs.
1. Na odredišnoj stranici kliknite **Manage Deployments**

To će vas odvesti na Azure OpenAI Studio web stranicu, gdje ćemo pronaći ostale vrijednosti kako je opisano dolje.

## Konfigurirajte Azure: Preko Studija

1. Idite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz svog resursa** kako je gore opisano.
1. Kliknite karticu **Deployments** (bočni izbornik, lijevo) za pregled trenutno implementiranih modela.
1. Ako željeni model nije implementiran, koristite **Create new deployment** za implementaciju.
1. Trebat će vam model za _generiranje teksta_ - preporučujemo: **gpt-35-turbo**
1. Trebat će vam model za _ugradnju teksta_ - preporučujemo **text-embedding-ada-002**

Sada ažurirajte varijable okruženja tako da odražavaju _Deployment name_ koji ste koristili. To će obično biti isto kao i naziv modela, osim ako ga niste eksplicitno promijenili. Na primjer, možete imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne zaboravite spremiti .env datoteku kad završite**. Sada možete izaći iz datoteke i vratiti se na upute za pokretanje bilježnice.

## Konfigurirajte OpenAI: Preko profila

Vaš OpenAI API ključ možete pronaći u svom [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se prijaviti i kreirati API ključ. Kad dobijete ključ, možete ga upisati u varijablu `OPENAI_API_KEY` u `.env` datoteci.

## Konfigurirajte Hugging Face: Preko profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih javno objavljivati ili dijeliti. Umjesto toga, kreirajte novi token za korištenje u ovom projektu i kopirajte ga u `.env` datoteku pod varijablu `HUGGING_FACE_API_KEY`. _Napomena:_ Tehnički, ovo nije API ključ, ali se koristi za autentifikaciju pa zadržavamo tu konvenciju imenovanja radi dosljednosti.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.