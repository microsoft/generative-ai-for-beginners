# Odabir i konfiguracija LLM pružatelja usluga 🔑

Zadaci **mogu** se također postaviti da rade s jednom ili više implementacija velikih jezičnih modela (LLM) putem podržanog pružatelja usluga poput OpenAI, Azure ili Hugging Face. Oni pružaju _hostanu pristupnu točku_ (API) kojoj možemo pristupiti programski uz odgovarajuće vjerodajnice (API ključ ili token). U ovom tečaju raspravljamo o sljedećim pružateljima:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznim modelima uključujući osnovnu GPT seriju.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s naglaskom na spremnost za poduzeća
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) za jedinstvenu pristupnu točku i API ključ za pristup stotinama modela iz OpenAI, Meta, Mistral, Cohere, Microsoft i drugih (zamjenjuje GitHub Models, koji se ukida krajem srpnja 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za open-source modele i inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ili [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ako biste radije pokretali modele u potpunosti offline na vlastitom uređaju, bez potrebe za pretplatom na oblak

**Za ove vježbe trebate koristiti vlastite račune**. Zadaci su neobvezni tako da možete odabrati postavljanje jednog, svih ili nijednog pružatelja usluga sukladno vašim interesima. Nekoliko smjernica za registraciju:

| Registracija | Trošak | API ključ | Playground | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cijene](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na temelju projekata](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bezkodni, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupno više modela |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cijene](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Početak](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Prijava za pristup je potrebna](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cijene](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Stranica Pregled projekta](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Dostupan je besplatni sloj; jedna pristupna točka + ključ za mnoge pružatelje modela |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cijene](https://huggingface.co/pricing) | [Pristupni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Besplatno (radi na vašem uređaju) | Nije potrebno | [Lokalni CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Potpuno offline, kompatibilna OpenAI pristupna točka |
| | | | | |

Slijedite upute u nastavku za _konfiguriranje_ ovog spremišta za korištenje s različitim pružateljima usluga. Zadaci koji zahtijevaju određenog pružatelja sadržavat će jedan od sljedećih oznaka u nazivu datoteke:

- `aoai` - zahtijeva Azure OpenAI pristupnu točku, ključ
- `oai` - zahtijeva OpenAI pristupnu točku, ključ
- `hf` - zahtijeva Hugging Face token
- `githubmodels` - zahtijeva Microsoft Foundry Models pristupnu točku, ključ (GitHub Models se ukida krajem srpnja 2026)

Možete konfigurirati jednog, nijednog ili sve pružatelje. Povezani zadaci će jednostavno prijaviti grešku ako nedostaju vjerodajnice.

## Kreirajte `.env` datoteku

Pretpostavljamo da ste već pročitali gornje upute, registrirali se kod odgovarajućeg pružatelja i pribavili potrebne vjerodajnice za autentikaciju (API_KEY ili token). U slučaju Azure OpenAI pretpostavljamo da također imate važeću implementaciju Azure OpenAI usluge (pristupnu točku) s barem jednim GPT modelom implementiranim za chat dovršavanje.

Sljedeći korak je konfiguracija vaših **lokalnih varijabli okruženja** na sljedeći način:

1. Pogledajte u korijenski direktorij za `.env.copy` datoteku koja bi trebala sadržavati nešto ovako:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI u Microsoft Foundry
   ## (Azure OpenAI usluga je sada dio Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Zadano je postavljeno! (trenutna stabilna GA verzija API-ja)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry modeli (katalog modela s više pružatelja, zamjenjuje GitHub modele, koji se povlače krajem srpnja 2026.)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopirajte tu datoteku u `.env` koristeći naredbu ispod. Ova datoteka je na .gitignore popisu, čuvajući tajne sigurno.

   ```bash
   cp .env.copy .env
   ```

3. Ispunite vrijednosti (zamijenite zamjenske oznake s desne strane znaka `=`) kako je opisano u sljedećem odlomku.

4. (Opcionalno) Ako koristite GitHub Codespaces, imate mogućnost spremiti varijable okruženja kao _Codespaces tajne_ povezane s ovim spremištem. U tom slučaju nećete trebati postavljati lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija radi samo ako koristite GitHub Codespaces.** Još uvijek ćete trebati postaviti .env datoteku ako koristite Docker Desktop.

## Popunite `.env` datoteku

Pogledajmo ukratko nazive varijabli kako bismo razumjeli što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje usluge za ne-Azure OpenAI pristupne točke |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje te usluge |
| AZURE_OPENAI_ENDPOINT | Ovo je implementirana pristupna točka za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je pristupna točka implementacije modela za _generiranje teksta_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je pristupna točka implementacije modela za _tekstualne ugnježdenja_ |
| AZURE_INFERENCE_ENDPOINT | Ovo je pristupna točka vašeg Microsoft Foundry projekta, koristi se za Microsoft Foundry modele |
| AZURE_INFERENCE_CREDENTIAL | Ovo je API ključ vašeg Microsoft Foundry projekta |
| | |

Napomena: Posljednje dvije Azure OpenAI varijable odražavaju zadani model za dovršavanje chata (generiranje teksta) i pretraživanje vektora (ugnježdenja) redom. Upute za njihovo postavljanje bit će definirane u odgovarajućim zadacima.

## Konfiguracija Azure OpenAI: Iz portala

> **Napomena:** Azure OpenAI Service sada je dio [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resursi i implementacije još uvijek se prikazuju u Azure Portalu, ali svakodnevno upravljanje modelima (implementacije, playground, nadzor) sada se odvija u Foundry portalu umjesto u starom samostalnom "Azure OpenAI Studiju".

Vrijednosti pristupne točke i ključa za Azure OpenAI pronaći ćete u [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), pa krenimo od tamo.

1. Posjetite [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnoj traci (izbornik lijevo).
1. Kliknite **Show Keys** - trebali biste vidjeti sljedeće: KEY 1, KEY 2 i Endpoint.
1. Koristite vrijednost KEY 1 za AZURE_OPENAI_API_KEY
1. Koristite vrijednost Endpoint za AZURE_OPENAI_ENDPOINT

Zatim trebamo pristupne točke za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnoj traci (lijevi izbornik) za Azure OpenAI resurs.
1. Na odredišnoj stranici kliknite **Go to Microsoft Foundry portal** (ili **Manage Deployments**, ovisno o vašem tipu resursa)

Ovo će vas odvesti do Microsoft Foundry portala, gdje ćemo pronaći ostale vrijednosti kako je opisano u nastavku.

## Konfiguracija Azure OpenAI: Iz Microsoft Foundry portala

1. Idite na [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašeg resursa** kao što je gore opisano.
1. Kliknite karticu **Deployments** (bočna traka, lijevo) da biste vidjeli trenutno implementirane modele.
1. Ako vaš željeni model nije implementiran, koristite **Deploy model** da ga implementirate iz [kataloga modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Trebat će vam _model za generiranje teksta_ - preporučujemo: **gpt-4o-mini**
1. Trebat će vam _model za tekstualna ugnježdenja_ - preporučujemo **text-embedding-3-small**

Sada ažurirajte varijable okruženja da odražavaju korišteno _Ime implementacije_. Obično će to biti isto kao naziv modela osim ako ga niste izričito promijenili. Kao primjer, mogli biste imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ne zaboravite spremiti .env datoteku kada završite**. Sada možete izaći iz datoteke i vratiti se upute za pokretanje bilježnice.

## Konfiguracija OpenAI: Iz profila

Vaš OpenAI API ključ možete pronaći u svom [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se registrirati i stvoriti API ključ. Kad imate ključ, možete ga upotrijebiti za popunjavanje varijable `OPENAI_API_KEY` u `.env` datoteci.

## Konfiguracija Hugging Face: Iz profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih javno objavljivati ili dijeliti. Umjesto toga, stvorite novi token za korištenje u ovom projektu i kopirajte ga u `.env` datoteku pod varijablu `HUGGING_FACE_API_KEY`. _Napomena:_ Tehnički ovo nije API ključ, ali se koristi za autentikaciju pa zadržavamo tu konvenciju naziva radi dosljednosti.

## Konfiguracija Microsoft Foundry Models: Iz portala

> **Napomena:** GitHub Models se ukida krajem srpnja 2026. Microsoft Foundry Models je direktna zamjena, nudeći isti katalog modela besplatan za isprobavanje i iskustvo Azure AI Inference SDK / OpenAI SDK.

1. Posjetite [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) i kreirajte (ili otvorite) Foundry projekt.
1. Pregledajte [katalog modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i implementirajte model, na primjer `gpt-4o-mini`.
1. Na stranici **Pregled** projekta, kopirajte **pristupnu točku** i **API ključ**.
1. Koristite vrijednost pristupne točke za `AZURE_INFERENCE_ENDPOINT` i vrijednost ključa za `AZURE_INFERENCE_CREDENTIAL` u svojoj `.env` datoteci.

## Offline / Lokalni pružatelji usluga

Ako ne želite koristiti pretplatu na oblak uopće, možete pokretati kompatibilne otvorene modele izravno na vlastitom uređaju:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftov runtime na uređaju. Automatski odabire najbolji izvršni pružatelj usluge (NPU, GPU ili CPU) i izlaže OpenAI kompatibilnu pristupnu točku, tako da možete ponovno koristiti većinu primjernog koda u ovom tečaju s minimalnim promjenama. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak ili instalirajte s `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - popularna alternativa za lokalno pokretanje otvorenih modela poput Llama, Phi, Mistral i Gemma.


Pogledajte [Lekciju 19: Izgradnja sa SLM-ovima](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) za praktične primjere koji koriste obje opcije.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->