# Izbira in konfiguracija ponudnika LLM 🔑

Naloge **lahko** tudi nastavite tako, da delujejo prek enega ali več izvajanih velikih jezikovnih modelov (LLM) preko podprtega ponudnika storitev, kot so OpenAI, Azure ali Hugging Face. Ti ponudijo _gostujočo točko za dostop_ (API), do katere imamo programatični dostop z ustreznimi poverilnicami (API ključ ali žeton). V tem tečaju obravnavamo naslednje ponudnike:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z različnimi modeli, vključno z osnovno serijo GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele, osredotočen na pripravljenost za podjetja
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) za eno samo točko končne povezave in API ključ za dostop do stotin modelov od OpenAI, Meta, Mistral, Cohere, Microsoft in drugih (nadomešča GitHub Models, ki se upokojuje konec julija 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za sklepanje
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ali [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), če raje modele poganjate popolnoma lokalno na svoji napravi, brez naročnine v oblaku

**Za te vaje boste morali uporabiti lastne račune**. Naloge so neobvezne, zato lahko izberete nastavitev enega, vseh ali nobenega izmed ponudnikov glede na vaše interese. Nekaj navodil za registracijo:

| Registracija | Cena | API ključ | Igralnica | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektno osnovan](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Brez kode, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Več modelov na voljo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Predhodna prijava za dostop](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cenik](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Stran Pregled projekta](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Igralnica](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Na voljo brezplačni sloj; ena točka + ključ za več ponudnikov modelov |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni žetoni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Brezplačno (deluje na vaši napravi) | Ni potrebno | [Lokalni CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Popolnoma brez povezave, endpoint združljiv z OpenAI |
| | | | | |

Sledite spodnjim navodilom, da _konfigurirate_ to repozitorij za uporabo z različnimi ponudniki. Naloge, ki zahtevajo določenega ponudnika, bodo imele eno od teh oznak v imenu datoteke:

- `aoai` - zahteva Azure OpenAI končno točko, ključ
- `oai` - zahteva OpenAI končno točko, ključ
- `hf` - zahteva Hugging Face žeton
- `githubmodels` - zahteva Microsoft Foundry Models končno točko, ključ (GitHub Models se bo umaknil konec julija 2026)

Lahko konfigurirate enega, nobenega ali vse ponudnike. Sorodne naloge bodo preprosto javile napako zaradi manjkajočih poverilnic.

## Ustvarite `.env` datoteko

Predvidevamo, da ste že prebrali zgornja navodila in se prijavili pri ustreznem ponudniku ter pridobili potrebne avtentikacijske poverilnice (API_KEY ali žeton). V primeru Azure OpenAI predvidevamo tudi, da imate veljavno namestitev storitve Azure OpenAI (končna točka) z vsaj enim GPT modelom, nameščenim za dokončanje klepeta.

Naslednji korak je, da konfigurirate vaše **lokalne sistemske spremenljivke** na naslednji način:

1. Poiščite v korenski mapi datoteko `.env.copy`, ki naj ima podobno vsebino kot ta:

   ```bash
   # OpenAI Ponudnik
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI v Microsoft Foundry
   ## (Azure OpenAI storitev je zdaj del Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Privzeto je nastavljeno! (trenutna stabilna GA verzija API-ja)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry modeli (več ponudniški katalog modelov, nadomešča GitHub modele, ki se upokojijo konec julija 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Datoteko kopirajte v `.env` z naslednjim ukazom. Ta datoteka je _v .gitignore_, da varuje skrivnosti.

   ```bash
   cp .env.copy .env
   ```

3. Izpolnite vrednosti (zamenjajte označene dele na desni strani `=`), kot je opisano v naslednjem delu.

4. (Opcijsko) Če uporabljate GitHub Codespaces, imate možnost shraniti spremenljivke okolja kot _Codespaces skrivnosti_, povezane s tem repozitorijem. V tem primeru vam ni treba nastavljati lokalne .env datoteke. **Vendar pa ta možnost deluje samo, če uporabljate GitHub Codespaces.** Če uporabljate Docker Desktop, boste morali datoteko .env vseeno nastaviti.

## Izpolnite `.env` datoteko

Hitro si poglejmo imena spremenljivk, da razumemo, kaj predstavljajo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je uporabniški dostopni žeton, ki ste ga nastavili v svojem profilu |
| OPENAI_API_KEY | To je avtentikacijski ključ za uporabo storitve za OpenAI končne točke, ki niso Azure |
| AZURE_OPENAI_API_KEY | To je avtentikacijski ključ za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je nameščena končna točka za Azure OpenAI vir |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka nameščene različice modela za _generiranje besedila_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka nameščene različice modela za _ugnezdene predstavitve_ besedila |
| AZURE_INFERENCE_ENDPOINT | To je končna točka za vaš Microsoft Foundry projekt, ki se uporablja za Microsoft Foundry modele |
| AZURE_INFERENCE_CREDENTIAL | To je API ključ za vaš Microsoft Foundry projekt |
| | |

Opomba: Zadnji dve spremenljivki Azure OpenAI predstavljata privzeti model za dokončanje klepetov (generiranje besedila) in iskanje po vektorskem prostoru (ugnezdene predstavitve). Navodila za nastavitev bodo podana v ustreznih nalogah.

## Konfiguracija Azure OpenAI: iz portala

> **Opomba:** Azure OpenAI storitev je zdaj del [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Viri in namestitve so še vedno vidni v Azure portalu, vendar se vsakodnevno upravljanje modelov (namestitve, igralnica, spremljanje) zdaj izvaja v Foundry portalu namesto stare samostojne "Azure OpenAI Studio".

Vrednosti za Azure OpenAI končno točko in ključ najdete v [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Obiščite [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite možnost **Ključi in končna točka** v stranski vrstici (meni na levi).
1. Kliknite **Pokaži ključe** - videli boste naslednje: KLJUČ 1, KLJUČ 2 in Končna točka.
1. Uporabite vrednost KLJUČ 1 za AZURE_OPENAI_API_KEY
1. Uporabite vrednost končne točke za AZURE_OPENAI_ENDPOINT

Nato potrebujemo končne točke za specifične modele, ki smo jih namestili.

1. Kliknite možnost **Namestitve modelov** v stranski vrstici (levi meni) za Azure OpenAI vir.
1. Na ciljni strani kliknite **Pojdi na Microsoft Foundry portal** (ali **Upravljanje namestitev**, glede na tip vira)

To vas bo odpeljalo do Microsoft Foundry portala, kjer bomo našli ostale vrednosti, kot je opisano spodaj.

## Konfiguracija Azure OpenAI: iz Microsoft Foundry portala

1. Pojdite na [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **prek vašega vira**, kot je opisano zgoraj.
1. Kliknite zavihek **Namestitve** (stranska vrstica, levo), da si ogledate trenutno nameščene modele.
1. Če želen model ni nameščen, uporabite **Namesti model**, da ga namestite iz [kataloga modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Potrebovali boste _model za generiranje besedila_ - priporočamo: **gpt-4o-mini**
1. Potrebovali boste _model za ugnezdene predstavitve besedila_ - priporočamo **text-embedding-3-small**

Sedaj posodobite sistemske spremenljivke, da odražajo _ime namestitve_, ki ste ga uporabili. To bo običajno enako imenu modela, razen če ste ga izrecno spremenili. Na primer, lahko imate:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ne pozabite shraniti .env datoteke, ko končate**. Sedaj lahko zaprete datoteko in se vrnete k navodilom za zagon beležnice.

## Konfiguracija OpenAI: iz profila

Vaš OpenAI API ključ najdete v svojem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga še nimate, se lahko registrirate in ustvarite API ključ. Ko imate ključ, ga lahko uporabite za izpolnitev spremenljivke `OPENAI_API_KEY` v `.env` datoteki.

## Konfiguracija Hugging Face: iz profila

Vaš Hugging Face žeton najdete v svojem profilu pod [Dostopnimi žetoni](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte jih ali delite javno. Namesto tega ustvarite nov žeton za uporabo v tem projektu in ga kopirajte v `.env` datoteko pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ Tehnično to ni API ključ, vendar se uporablja za avtentikacijo, zato ohranjamo to poimenovanje zaradi doslednosti.

## Konfiguracija Microsoft Foundry Models: iz portala

> **Opomba:** GitHub Models se umika konec julija 2026. Microsoft Foundry Models je neposredna zamenjava, ki ponuja isti brezplačni katalog modelov in izkušnjo Azure AI Inference SDK / OpenAI SDK.

1. Pojdite na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) in ustvarite (ali odprite) Foundry projekt.
1. Prebrskajte [katalog modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) in namestite model, na primer `gpt-4o-mini`.
1. Na strani **Pregled** projekta kopirajte **končno točko** in **API ključ**.
1. Uporabite vrednost končne točke za `AZURE_INFERENCE_ENDPOINT` in vrednost ključa za `AZURE_INFERENCE_CREDENTIAL` v vaši `.env` datoteki.

## Ponudniki brez povezave / lokalni ponudniki

Če ne želite uporabljati naročnine v oblaku, lahko združljive odprtokodne modele zaženete neposredno na lastni napravi:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftovo izvajalno okolje na napravi. Samodejno izbere najboljšega izvajalnega ponudnika (NPU, GPU ali CPU) in ponuja končno točko, združljivo z OpenAI, tako da lahko večino vzorčne kode v tem tečaju ponovno uporabite z minimalnimi spremembami. Za začetek glejte [dokumentacijo Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ali ga namestite z `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - priljubljena alternativa za lokalno poganjanje odprtokodnih modelov, kot so Llama, Phi, Mistral in Gemma.


Oglejte si [Lekcija 19: Gradnja z SLM-ji](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) za praktične primere uporabe obeh možnosti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->