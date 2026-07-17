# Odabir i konfiguracija pružatelja LLM-a 🔑

Zadaci **mogu** biti postavljeni da rade prema jednom ili više implementacija Velikih jezičnih modela (LLM) putem podržanog pružatelja usluge poput OpenAI, Azure ili Hugging Face. Oni pružaju _hostanu krajnju točku_ (API) kojoj možemo pristupiti programatski s odgovarajućim vjerodajnicama (API ključ ili token). U ovom tečaju raspravljamo o ovim pružateljima:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s raznovrsnim modelima uključujući osnovni GPT niz.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s naglaskom na spremnost za poduzeća
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) za jednu krajnju točku i API ključ za pristup stotinama modela iz OpenAI, Meta, Mistral, Cohere, Microsoft i drugih (zamjenjuje GitHub Models, koji se povlači krajem srpnja 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za modele otvorenog koda i poslužitelj za izvođenje
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ili [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ako biste radije pokretali modele potpuno offline na vlastitom uređaju, bez potrebe za pretplatom na oblak

**Morat ćete koristiti vlastite račune za ove vježbe**. Zadaci su opcionalni pa možete odlučiti postaviti jednog, sve - ili nijednog - od pružatelja usluga prema vašim interesima. Nekoliko uputa za prijavu:

| Prijava | Trošak | API ključ | Igralište | Komentari |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cijene](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na temelju projekta](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez koda, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupno više modela |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cijene](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Početak](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Početak](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Potrebno unaprijed zatražiti pristup](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cijene](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Pregled projekta](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Igralište](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Besplatni sloj dostupan; jedna krajnja točka + ključ za mnoge pružatelje modela |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cijene](https://huggingface.co/pricing) | [Pristupni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima ograničene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Besplatno (radi na vašem uređaju) | Nije potrebno | [Lokalni CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Potpuno offline, OpenAI-kompatibilna krajnja točka |
| | | | | |

Slijedite upute u nastavku da _konfigurirate_ ovaj repozitorij za upotrebu s različitim pružateljima. Zadaci koji zahtijevaju određenog pružatelja sadržavat će jedan od ovih tagova u nazivu datoteke:

- `aoai` - zahtijeva Azure OpenAI krajnju točku, ključ
- `oai` - zahtijeva OpenAI krajnju točku, ključ
- `hf` - zahtijeva Hugging Face token
- `githubmodels` - zahtijeva Microsoft Foundry Models krajnju točku, ključ (GitHub Models se povlači krajem srpnja 2026)

Možete konfigurirati jednog, nijednog ili sve pružatelje. Povezani zadaci jednostavno će dati grešku kod nedostatka vjerodajnica.

## Kreirajte `.env` datoteku

Pretpostavljamo da ste već pročitali gornje upute i registrirali se kod odgovarajućeg pružatelja te dobili potrebne vjerodajnice za autentikaciju (API_KEY ili token). U slučaju Azure OpenAI, pretpostavljamo da također imate valjanu implementaciju Azure OpenAI servisa (krajnju točku) s barem jednim GPT modelom implementiranim za chat dovršetak.

Sljedeći korak je konfiguriranje vaših **lokalnih varijabli okruženja** na sljedeći način:

1. Potražite u glavnoj mapi `.env.copy` datoteku koja bi trebala sadržavati ovakve podatke:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI u Microsoft Foundry
   ## (Azure OpenAI servis je sada dio Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Zadano je postavljeno! (trenutna stabilna GA verzija API-ja)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry modeli (katalog modela s više pružatelja, zamjenjuje GitHub modele koji se ukidaju krajem srpnja 2026.)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopirajte tu datoteku u `.env` korištenjem naredbe u nastavku. Ova datoteka je _gitignore-ana_, čime se čuvaju tajne.

   ```bash
   cp .env.copy .env
   ```

3. Ispunite vrijednosti (zamijenite zamjenske oznake desno od `=`) kako je opisano u sljedećem dijelu.

4. (Opcionalno) Ako koristite GitHub Codespaces, imate opciju spremanja varijabli okruženja kao _Codespaces tajni_ povezanih s ovim repozitorijem. U tom slučaju, nećete trebati postavljati lokalnu .env datoteku. **Međutim, imajte na umu da ova opcija funkcionira samo ako koristite GitHub Codespaces.** I dalje ćete trebati postaviti .env datoteku ako koristite Docker Desktop.

## Popunite `.env` datoteku

Pogledajmo brzo nazive varijabli da bismo razumjeli što predstavljaju:

| Varijabla  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ovo je korisnički pristupni token koji ste postavili u svom profilu |
| OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje servisa za ne-Azure OpenAI krajnje točke |
| AZURE_OPENAI_API_KEY | Ovo je autorizacijski ključ za korištenje tog servisa |
| AZURE_OPENAI_ENDPOINT | Ovo je implementirana krajnja točka za Azure OpenAI resurs |
| AZURE_OPENAI_DEPLOYMENT | Ovo je krajnja točka implementacije modela za _generiranje teksta_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ovo je krajnja točka implementacije modela za _ugrađivanje teksta_ |
| AZURE_INFERENCE_ENDPOINT | Ovo je krajnja točka za vaš Microsoft Foundry projekt, koristi se za Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ovo je API ključ za vaš Microsoft Foundry projekt |
| | |

Napomena: Posljednje dvije Azure OpenAI varijable odražavaju zadani model za chat dovršetak (generiranje teksta) i pretraživanje vektora (ugrađivanje) respektivno. Upute za njihovo postavljanje bit će definirane u relevantnim zadacima.

## Konfigurirajte Azure OpenAI: Iz Portala

> **Napomena:** Azure OpenAI servis je sada dio [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resursi i implementacije se još uvijek prikazuju u Azure Portalu, ali svakodnevno upravljanje modelima (implementacije, igralište, nadzor) sada se odvija u Foundry portalu umjesto starog samostalnog "Azure OpenAI Studija".

Azure OpenAI krajnju točku i vrijednosti ključa možete pronaći u [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) pa krenimo od tamo.

1. Idite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite opciju **Keys and Endpoint** u bočnoj traci (izbornik lijevo).
1. Kliknite **Show Keys** - trebali biste vidjeti sljedeće: KEY 1, KEY 2 i Endpoint.
1. Koristite vrijednost KEY 1 za AZURE_OPENAI_API_KEY
1. Koristite vrijednost Endpoint za AZURE_OPENAI_ENDPOINT

Sljedeće, trebamo krajnje točke za specifične modele koje smo implementirali.

1. Kliknite opciju **Model deployments** u bočnoj traci (lijevi izbornik) za Azure OpenAI resurs.
1. Na odredišnoj stranici kliknite **Go to Microsoft Foundry portal** (ili **Manage Deployments**, ovisno o tipu resursa)

Ovo će vas odvesti na Microsoft Foundry portal, gdje ćemo pronaći ostale vrijednosti kako je opisano u nastavku.

## Konfigurirajte Azure OpenAI: Iz Microsoft Foundry portala

1. Navigirajte do [Microsoft Foundry portala](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašeg resursa** kako je opisano gore.
1. Kliknite na karticu **Deployments** (bočna traka, lijevo) za pregled trenutno implementiranih modela.
1. Ako željeni model nije implementiran, koristite **Deploy model** da ga implementirate iz [kataloga modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Trebat će vam _model za generiranje teksta_ - preporučujemo: **gpt-5-mini**
1. Trebat će vam _model za ugradnju teksta_ - preporučujemo **text-embedding-3-small**

Sada ažurirajte varijable okruženja da odražavaju korišteni _Naziv implementacije_. To će obično biti isto kao naziv modela osim ako ga niste eksplicitno promijenili. Dakle, kao primjer, mogli biste imati:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ne zaboravite spremiti .env datoteku kada završite**. Sada možete izaći iz datoteke i vratiti se u upute za pokretanje bilježnice.

## Konfigurirajte OpenAI: Iz profila

Vaš OpenAI API ključ možete pronaći u svom [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ako ga nemate, možete se registrirati i kreirati API ključ. Nakon što imate ključ, možete ga iskoristiti za popunjavanje varijable `OPENAI_API_KEY` u `.env` datoteci.

## Konfigurirajte Hugging Face: Iz profila

Vaš Hugging Face token možete pronaći u svom profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nemojte ih objavljivati ili dijeliti javno. Umjesto toga, kreirajte novi token za ovu projektnu upotrebu i kopirajte ga u `.env` datoteku pod varijablu `HUGGING_FACE_API_KEY`. _Napomena:_ Tehnički, ovo nije API ključ, ali se koristi za autentifikaciju pa zadržavamo taj naziv radi konzistentnosti.

## Konfigurirajte Microsoft Foundry Models: Iz portala

> **Napomena:** GitHub Models se povlači krajem srpnja 2026. Microsoft Foundry Models je izravna zamjena koja nudi isti katalog modela za besplatno isprobavanje i iskustvo Azure AI Inference SDK / OpenAI SDK.

1. Idite na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) i kreirajte (ili otvorite) Foundry projekt.
1. Pregledajte [katalog modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i implementirajte model, na primjer `gpt-5-mini`.
1. Na stranici **Pregled** projekta kopirajte **krajnju točku** i **API ključ**.
1. Koristite vrijednost krajnje točke za `AZURE_INFERENCE_ENDPOINT` i vrijednost ključa za `AZURE_INFERENCE_CREDENTIAL` u svojoj `.env` datoteci.

## Offline / Lokalni pružatelji

Ako ne želite koristiti pretplatu na oblak, možete pokretati kompatibilne otvorene modele izravno na svom uređaju:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftov runtime na uređaju. Automatski odabire najboljeg izvođačkog pružatelja (NPU, GPU ili CPU) i izlaže OpenAI-kompatibilnu krajnju točku, pa možete ponovno koristiti većinu uzoraka koda u ovom tečaju uz minimalne promjene. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak, ili instalirajte s `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - popularna alternativa za lokalno pokretanje otvorenih modela poput Llama, Phi, Mistral i Gemma.


Pogledajte [Lekcija 19: Izgradnja pomoću SLM-ova](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) za praktične primjere korištenja oba pristupa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->