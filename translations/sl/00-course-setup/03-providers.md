# Izbira in konfiguracija ponudnika LLM 🔑

Naloge **lahko** tudi nastavite za delovanje z enim ali več večjimi jezikovnimi modeli (LLM) preko podprtega ponudnika storitev, kot so OpenAI, Azure ali Hugging Face. Ti zagotavljajo _gostujočo končno točko_ (API), do katere lahko dostopamo programsko z ustreznimi poverilnicami (API ključ ali token). V tem tečaju obravnavamo naslednje ponudnike:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z različnimi modeli, vključno z osnovno serijo GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s poudarkom na pripravljenosti za podjetja
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) za eno končno točko in API ključ za dostop do stotin modelov OpenAI, Meta, Mistral, Cohere, Microsoft in drugih (nadomešča GitHub Models, ki se bo upokojil konec julija 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za sklepanje
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ali [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), če raje zaženete modele popolnoma lokalno na svoji napravi, brez potrebe po naročnini v oblaku

**Za te vaje boste potrebovali lastne račune**. Naloge so neobvezne, tako da lahko izberete nastavitev enega, vseh ali nobenega ponudnika glede na vaše interese. Nekaj napotkov za prijavo:

| Prijava | Stroški | API ključ | Igralnica | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Brez kode, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Več modelov na voljo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK hitri začetek](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio hitri začetek](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Dostop je treba predhodno zaprositi](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cenik](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Stran pregleda projekta](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry igralnica](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Na voljo brezplačen nivo; ena končna točka + ključ za veliko ponudnikov modelov |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Brezplačno (deluje na vaši napravi) | Ni potrebno | [Lokalni CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Popolnoma brez povezave, OpenAI združljiva končna točka |
| | | | | |

Sledite spodnjim navodilom za _konfiguracijo_ te zbirke za uporabo z različnimi ponudniki. Naloge, ki zahtevajo specifičnega ponudnika, bodo imele eno od teh oznak v imenu datoteke:

- `aoai` - zahteva Azure OpenAI končno točko, ključ
- `oai` - zahteva OpenAI končno točko, ključ
- `hf` - zahteva Hugging Face token
- `githubmodels` - zahteva Microsoft Foundry Models končno točko, ključ (GitHub Models se bo upokojil konec julija 2026)

Lahko konfigurirate enega, nobenega ali vse ponudnike. Sorodne naloge bodo preprosto vrgle napako zaradi manjkajočih poverilnic.

## Ustvarite datoteko `.env`

Predvidevamo, da ste že prebrali zgornja navodila, se prijavili pri ustreznem ponudniku in pridobili potrebne avtentikacijske poverilnice (API_KEY ali token). V primeru Azure OpenAI predpostavljamo, da imate tudi veljavno namestitev Azure OpenAI storitve (končna točka) z vsaj enim GPT modelom, nameščenim za dokončanje pogovora.

Naslednji korak je konfiguracija vaših **lokalnih spremenljivk okolja** na naslednji način:

1. Poglejte v korensko mapo za datoteko `.env.copy`, ki naj vsebuje nekaj takega:

   ```bash
   # OpenAI ponudnik
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI v Microsoft Foundry
   ## (Azure OpenAI storitev je zdaj del Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Privzeto je nastavljeno! (trenutna stabilna GA različica API-ja)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry modeli (večponudniški katalog modelov, nadomešča GitHub modele, ki prenehajo ob koncu julija 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopirajte to datoteko v `.env` z naslednjim ukazom. Ta datoteka je _gitignore-irana_, da so skrivnosti varne.

   ```bash
   cp .env.copy .env
   ```

3. Izpolnite vrednosti (zamenjajte oznake na desni strani znaka `=`), kot je opisano v naslednjem razdelku.

4. (Izbirno) Če uporabljate GitHub Codespaces, imate možnost shranjevanja spremenljivk okolja kot _Codespaces skrivnosti_ povezanih s to zbirko. V tem primeru ne boste potrebovali nastaviti lokalne .env datoteke. **Vendar pa ta možnost deluje samo, če uporabljate GitHub Codespaces.** Če uporabljate Docker Desktop, boste še vedno morali nastaviti .env datoteko.

## Izpolnite datoteko `.env`

Oglejmo si na hitro imena spremenljivk, da razumemo, kaj predstavljajo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je dostopni token uporabnika, ki ga nastavite v svojem profilu |
| OPENAI_API_KEY | To je pooblastitveni ključ za uporabo storitve za ne-Azure OpenAI končne točke |
| AZURE_OPENAI_API_KEY | To je pooblastitveni ključ za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je nameščena končna točka za Azure OpenAI vir |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka namestitve modela za _generiranje besedila_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka namestitve modela za _vdelavo besedila_ |
| AZURE_INFERENCE_ENDPOINT | To je končna točka vašega Microsoft Foundry projekta, uporabljena za Microsoft Foundry modele |
| AZURE_INFERENCE_CREDENTIAL | To je API ključ za vaš Microsoft Foundry projekt |
| | |

Opomba: Zadnji dve spremenljivki Azure OpenAI odražata privzeti model za dokončanje pogovora (generiranje besedila) in iskanje po vektorjih (vdelave) ločeno. Navodila za njihovo nastavitev bodo opredeljena v sorodnih nalogah.

## Konfiguracija Azure OpenAI: iz portala

> **Opomba:** Azure OpenAI storitev je zdaj del [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Viri in namestitve se še vedno prikazujejo v Azure Portalu, a vsakodnevno upravljanje modelov (namestitve, igralnica, spremljanje) zdaj poteka v Foundry portalu namesto stare samostojne "Azure OpenAI Studio".

Vrednosti za Azure OpenAI končno točko in ključ boste našli v [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Obiščite [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite možnost **Keys and Endpoint** v stranski vrstici (meni levo).
1. Kliknite **Show Keys** – videti bi morali naslednje: KEY 1, KEY 2 in Endpoint.
1. Uporabite vrednost KEY 1 za AZURE_OPENAI_API_KEY
1. Uporabite vrednost Endpoint za AZURE_OPENAI_ENDPOINT

Naslednji korak so končne točke za specifične modele, ki smo jih namestili.

1. Kliknite možnost **Model deployments** v stranski vrstici (levi meni) za Azure OpenAI vir.
1. Na ciljni strani kliknite **Go to Microsoft Foundry portal** (ali **Manage Deployments**, odvisno od tipa vira)

To vas bo pripeljalo do Microsoft Foundry portala, kjer bomo našli ostale vrednosti, kot je opisano spodaj.

## Konfiguracija Azure OpenAI: iz Microsoft Foundry portala

1. Odprite [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **iz svojega vira**, kot je opisano zgoraj.
1. Kliknite zavihek **Deployments** (stranski meni, levo) za ogled trenutno nameščenih modelov.
1. Če željenega modela ni nameščenega, uporabite **Deploy model**, da ga namestite iz [kataloga modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Potrebovali boste _model za generiranje besedila_ – priporočamo: **gpt-5-mini**
1. Potrebovali boste _model za vdelavo besedila_ – priporočamo **text-embedding-3-small**

Zdaj posodobite spremenljivke okolja, da odražajo _Ime namestitve_ uporabljeno. To bo običajno enako imenu modela, razen če ste ga izrecno spremenili. Na primer, lahko imate:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ne pozabite shraniti .env datoteke, ko končate**. Zdaj lahko zaprete datoteko in se vrnete k navodilom za zagon zvezka.

## Konfiguracija OpenAI: Iz profila

Vaš OpenAI API ključ najdete v svojem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga še nimate, se lahko prijavite in ustvarite API ključ. Ko imate ključ, ga uporabite za izpolnitev spremenljivke `OPENAI_API_KEY` v `.env` datoteki.

## Konfiguracija Hugging Face: Iz profila

Vaš Hugging Face token najdete v svojem profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte jih ali delite javno. Namesto tega ustvarite nov token za uporabo v tem projektu in ga kopirajte v `.env` datoteko pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ Tehnično to ni API ključ, ampak se uporablja za avtentikacijo, zato ohranjamo to konvencijo poimenovanja zaradi konsistence.

## Konfiguracija Microsoft Foundry Models: Iz portala

> **Opomba:** GitHub Models se bo upokojil konec julija 2026. Microsoft Foundry Models je neposredna zamenjava, ki ponuja enak katalog modelov za brezplačno preizkušnjo in izkušnjo z Azure AI Inference SDK / OpenAI SDK.

1. Obiščite [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) in ustvarite (ali odprite) Foundry projekt.
1. Brskajte po [katalogu modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) in namestite model, na primer `gpt-5-mini`.
1. Na strani **Pregled** projekta kopirajte **končno točko** in **API ključ**.
1. Uporabite vrednost končne točke za `AZURE_INFERENCE_ENDPOINT` in vrednost ključa za `AZURE_INFERENCE_CREDENTIAL` v vaši `.env` datoteki.

## Ponudniki brez povezave / lokalni ponudniki

Če raje ne uporabljate naročniškega oblaka, lahko združljive odprtokodne modele zaženete neposredno na svoji napravi:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftovo okolje za zaganjanje na napravi. Samodejno izbere najboljšega izvajalca (NPU, GPU ali CPU) in ponuja OpenAI združljivo končno točko, tako da lahko uporabite večino primerov kode iz tega tečaja z minimalnimi spremembami. Za začetek si oglejte [Foundry Local dokumentacijo](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ali namestite z `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - priljubljena alternativa za lokalni zagon odprtokodnih modelov, kot so Llama, Phi, Mistral in Gemma.


Oglejte si [Lekcija 19: Gradnja z SLM-ji](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) za praktične primere uporabe obeh možnosti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->