# Izbira in konfiguracija ponudnika LLM 🔑

Naloge **lahko** nastavite tudi za delo z enim ali več razporeditvami velikih jezikovnih modelov (LLM) prek podprtega ponudnika storitev, kot so OpenAI, Azure ali Hugging Face. Ti zagotavljajo _gostujočo končno točko_ (API), do katere lahko dostopamo programsko z ustreznimi poverilnicami (API ključ ali žeton). V tem tečaju obravnavamo te ponudnike:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z različnimi modeli, vključno z osnovno serijo GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s poudarkom na pripravljenosti za podjetja
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za sklepanje

**Za te vaje boste morali uporabiti svoje račune**. Naloge so neobvezne, zato lahko izberete nastavitev enega, vseh ali nobenega ponudnika glede na vaše interese. Nekaj navodil za prijavo:

| Prijava | Stroški | API ključ | Igralnica | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekt osnovan](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Brez kode, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Več modelov na voljo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Dostop je treba predhodno zaprositi](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni žetoni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sledite spodnjim navodilom za _konfiguracijo_ tega repozitorija za uporabo z različnimi ponudniki. Naloge, ki zahtevajo določenega ponudnika, bodo v imenu datoteke vsebovale eno od teh oznak:

- `aoai` - zahteva Azure OpenAI končno točko, ključ
- `oai` - zahteva OpenAI končno točko, ključ
- `hf` - zahteva Hugging Face žeton

Lahko konfigurirate enega, nobenega ali vse ponudnike. Sorodne naloge bodo preprosto javljale napako ob manjkajočih poverilnicah.

## Ustvarite datoteko `.env`

Predpostavljamo, da ste že prebrali zgornja navodila, se prijavili pri ustreznem ponudniku in pridobili zahtevane poverilnice za avtentikacijo (API_KEY ali žeton). V primeru Azure OpenAI predpostavljamo tudi, da imate veljavno razporeditev storitve Azure OpenAI (končna točka) z vsaj enim GPT modelom za dokončanje klepeta.

Naslednji korak je konfiguracija vaših **lokalnih okoljskih spremenljivk** na naslednji način:

1. Poiščite v korenski mapi datoteko `.env.copy`, ki naj bi vsebovala nekaj takega:

   ```bash
   # Ponudnik OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Privzeto je nastavljeno!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopirajte to datoteko v `.env` z naslednjim ukazom. Ta datoteka je _gitignore-ana_, kar varuje skrivnosti.

   ```bash
   cp .env.copy .env
   ```

3. Izpolnite vrednosti (zamenjajte nadomestne znake na desni strani `=`) kot je opisano v naslednjem razdelku.

4. (Opcijsko) Če uporabljate GitHub Codespaces, imate možnost shraniti okoljske spremenljivke kot _Codespaces skrivnosti_, povezane s tem repozitorijem. V tem primeru ne boste potrebovali lokalne datoteke .env. **Vendar pa ta možnost deluje samo, če uporabljate GitHub Codespaces.** Datoteko .env boste morali nastaviti, če uporabljate Docker Desktop.

## Izpolnite datoteko `.env`

Poglejmo hitro imena spremenljivk, da razumemo, kaj predstavljajo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je uporabniški dostopni žeton, ki ste ga nastavili v svojem profilu |
| OPENAI_API_KEY | To je avtentikacijski ključ za uporabo storitve za ne-Azure OpenAI končne točke |
| AZURE_OPENAI_API_KEY | To je avtentikacijski ključ za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je razporejena končna točka za Azure OpenAI vir |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka razporeditve modela za _generiranje besedila_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka razporeditve modela za _vdelave besedila_ |
| | |

Opomba: Zadnji dve spremenljivki Azure OpenAI predstavljata privzeti model za dokončanje klepeta (generiranje besedila) in iskanje vektorjev (vdelave). Navodila za njihovo nastavitev bodo opredeljena v ustreznih nalogah.

## Konfiguracija Azure: iz portala

Vrednosti končne točke in ključa Azure OpenAI boste našli v [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Pojdite na [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite možnost **Ključi in končna točka** v stranski vrstici (meni na levi).
1. Kliknite **Prikaži ključe** - videti bi morali naslednje: KLJUČ 1, KLJUČ 2 in Končna točka.
1. Uporabite vrednost KLJUČ 1 za AZURE_OPENAI_API_KEY
1. Uporabite vrednost Končna točka za AZURE_OPENAI_ENDPOINT

Nato potrebujemo končne točke za specifične modele, ki smo jih razporedili.

1. Kliknite možnost **Razporeditve modelov** v stranski vrstici (levi meni) za Azure OpenAI vir.
1. Na ciljni strani kliknite **Upravljanje razporeditev**

To vas bo pripeljalo do spletnega mesta Azure OpenAI Studio, kjer bomo našli ostale vrednosti, kot je opisano spodaj.

## Konfiguracija Azure: iz studia

1. Pojdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašega vira**, kot je opisano zgoraj.
1. Kliknite zavihek **Razporeditve** (stranska vrstica, levo), da si ogledate trenutno razporejene modele.
1. Če vaš želeni model ni razporejen, uporabite **Ustvari novo razporeditev**, da ga razporedite.
1. Potrebovali boste model za _generiranje besedila_ - priporočamo: **gpt-35-turbo**
1. Potrebovali boste model za _vdelave besedila_ - priporočamo **text-embedding-ada-002**

Zdaj posodobite okoljske spremenljivke, da odražajo uporabljeno _ime razporeditve_. To bo običajno enako imenu modela, razen če ste ga izrecno spremenili. Na primer, lahko imate:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne pozabite shraniti datoteke .env, ko končate**. Sedaj lahko zaprete datoteko in se vrnete k navodilom za zagon zvezka.

## Konfiguracija OpenAI: iz profila

Vaš OpenAI API ključ najdete v svojem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga nimate, se lahko prijavite in ustvarite API ključ. Ko imate ključ, ga lahko uporabite za izpolnitev spremenljivke `OPENAI_API_KEY` v datoteki `.env`.

## Konfiguracija Hugging Face: iz profila

Vaš Hugging Face žeton najdete v svojem profilu pod [Dostopnimi žetoni](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte jih ali delite javno. Namesto tega ustvarite nov žeton za uporabo v tem projektu in ga kopirajte v datoteko `.env` pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ Tehnično to ni API ključ, vendar se uporablja za avtentikacijo, zato ohranjamo to poimenovanje zaradi doslednosti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->