<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:47:16+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sl"
}
-->
# Izbira in nastavitev ponudnika LLM 🔑

Naloge **lahko** nastavite tako, da delujejo z eno ali več namestitvami velikih jezikovnih modelov (LLM) prek podprtega ponudnika storitev, kot so OpenAI, Azure ali Hugging Face. Ti ponudniki omogočajo _gostovan končni točki_ (API), do katere lahko dostopamo programsko z ustreznimi poverilnicami (API ključ ali žeton). V tem tečaju obravnavamo naslednje ponudnike:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z različnimi modeli, vključno z glavno serijo GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s poudarkom na pripravljenosti za podjetja
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za inferenco

**Za te vaje boste potrebovali svoje račune.** Naloge so neobvezne, zato se lahko odločite, da nastavite enega, vse ali nobenega od ponudnikov, odvisno od vaših interesov. Nekaj napotkov za prijavo:

| Prijava | Strošek | API ključ | Playground | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Na voljo več modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Dostop je treba predhodno odobriti](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni žetoni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejeno število modelov](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sledite spodnjim navodilom za _nastavitev_ tega repozitorija za uporabo z različnimi ponudniki. Naloge, ki zahtevajo določenega ponudnika, bodo v imenu datoteke vsebovale enega od teh oznak:

- `aoai` - zahteva Azure OpenAI končno točko in ključ
- `oai` - zahteva OpenAI končno točko in ključ
- `hf` - zahteva Hugging Face žeton

Nastavite lahko enega, nobenega ali vse ponudnike. Povezane naloge bodo v primeru manjkajočih poverilnic preprosto javljale napako.

## Ustvarite datoteko `.env`

Predpostavljamo, da ste že prebrali zgornja navodila, se prijavili pri ustreznem ponudniku in pridobili potrebne avtentikacijske podatke (API_KEY ali žeton). V primeru Azure OpenAI predpostavljamo, da imate tudi veljavno namestitev storitve Azure OpenAI (končna točka) z vsaj enim GPT modelom, nameščenim za chat completion.

Naslednji korak je nastavitev **lokalnih okoljskih spremenljivk**:

1. V korenski mapi poiščite datoteko `.env.copy`, ki naj bi vsebovala nekaj takega:

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

2. To datoteko kopirajte v `.env` z naslednjim ukazom. Ta datoteka je _gitignore-d_, kar pomeni, da so podatki varni.

   ```bash
   cp .env.copy .env
   ```

3. Vnesite vrednosti (zamenjajte nadomestne vrednosti na desni strani `=`), kot je opisano v naslednjem razdelku.

4. (Možnost) Če uporabljate GitHub Codespaces, lahko okoljske spremenljivke shranite kot _Codespaces secrets_, povezane s tem repozitorijem. V tem primeru vam ni treba nastaviti lokalne .env datoteke. **Vendar pa ta možnost deluje le, če uporabljate GitHub Codespaces.** Če uporabljate Docker Desktop, boste še vedno morali nastaviti datoteko .env.

## Izpolnite datoteko `.env`

Poglejmo si hitro imena spremenljivk, da razumemo, kaj pomenijo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je uporabniški dostopni žeton, ki ga nastavite v svojem profilu |
| OPENAI_API_KEY | To je avtorizacijski ključ za uporabo storitve za ne-Azure OpenAI končne točke |
| AZURE_OPENAI_API_KEY | To je avtorizacijski ključ za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je nameščena končna točka za Azure OpenAI vir |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka za namestitev _modela za generiranje besedila_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka za namestitev _modela za vdelave besedila_ |
| | |

Opomba: Zadnji dve spremenljivki za Azure OpenAI predstavljata privzeti model za chat completion (generiranje besedila) in iskanje po vektorjih (vdelave) oz. Navodila za nastavitev bodo podana v ustreznih nalogah.

## Nastavitev Azure: prek Portala

Vrednosti za Azure OpenAI končno točko in ključ boste našli v [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Odprite [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. V stranskem meniju (levo) kliknite možnost **Keys and Endpoint**.
1. Kliknite **Show Keys** - prikazali se bodo: KEY 1, KEY 2 in Endpoint.
1. Vrednost KEY 1 uporabite za AZURE_OPENAI_API_KEY
1. Vrednost Endpoint uporabite za AZURE_OPENAI_ENDPOINT

Nato potrebujemo končne točke za posamezne modele, ki smo jih namestili.

1. V stranskem meniju (levo) za Azure OpenAI vir kliknite možnost **Model deployments**.
1. Na ciljni strani kliknite **Manage Deployments**

To vas bo preusmerilo na spletno stran Azure OpenAI Studio, kjer bomo našli ostale vrednosti, kot je opisano spodaj.

## Nastavitev Azure: prek Studia

1. Pojdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz svojega vira**, kot je opisano zgoraj.
1. Kliknite zavihek **Deployments** (stranski meni, levo), da si ogledate trenutno nameščene modele.
1. Če želeni model ni nameščen, uporabite **Create new deployment** za namestitev.
1. Potrebovali boste _model za generiranje besedila_ - priporočamo: **gpt-35-turbo**
1. Potrebovali boste _model za vdelave besedila_ - priporočamo **text-embedding-ada-002**

Zdaj posodobite okoljske spremenljivke, da odražajo _ime namestitve_, ki ste ga uporabili. To je običajno enako imenu modela, razen če ste ga izrecno spremenili. Na primer, lahko imate:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne pozabite shraniti datoteke .env, ko končate.** Zdaj lahko zaprete datoteko in se vrnete k navodilom za zagon zvezka.

## Nastavitev OpenAI: prek profila

Vaš OpenAI API ključ najdete v [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga še nimate, se lahko prijavite in ustvarite API ključ. Ko imate ključ, ga vnesite v spremenljivko `OPENAI_API_KEY` v datoteki `.env`.

## Nastavitev Hugging Face: prek profila

Vaš Hugging Face žeton najdete v svojem profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte ali delite teh podatkov javno. Namesto tega ustvarite nov žeton za uporabo v tem projektu in ga kopirajte v datoteko `.env` pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ Tehnično to ni API ključ, vendar se uporablja za avtentikacijo, zato ohranjamo to poimenovanje zaradi doslednosti.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.