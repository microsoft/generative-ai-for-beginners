<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:38:29+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sl"
}
-->
# Nastavite svoje razvojno okolje

Ta repozitorij in tečaj smo nastavili z [razvojnim kontejnerjem](https://containers.dev?WT.mc_id=academic-105485-koreyst), ki ima univerzalno okolje za izvajanje, ki podpira razvoj v Python3, .NET, Node.js in Javi. Sorodna konfiguracija je definirana v datoteki `devcontainer.json`, ki se nahaja v mapi `.devcontainer/` v korenu tega repozitorija.

Za aktivacijo razvojnega kontejnerja ga zaženite v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za oblačno gostovano okolje) ali v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za lokalno gostovano okolje). Za več podrobnosti o delovanju razvojnih kontejnerjev v VS Code preberite [to dokumentacijo](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).  

> [!TIP]  
> Priporočamo uporabo GitHub Codespaces za hiter začetek z minimalnim trudom. Ponuja velikodušno [brezplačno kvoto](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za osebne račune. Nastavite [časovne omejitve](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), da se neaktivni codespaces ustavijo ali izbrišejo in tako kar najbolje izkoristite svojo kvoto.

## 1. Izvajanje nalog

Vsaka lekcija bo imela _neobvezne_ naloge, ki so lahko na voljo v enem ali več programskih jezikih, vključno s: Python, .NET/C#, Java in JavaScript/TypeScript. Ta razdelek ponuja splošna navodila za izvajanje teh nalog.

### 1.1 Python naloge

Python naloge so na voljo bodisi kot aplikacije (`.py` datoteke) ali Jupyter zvezki (`.ipynb` datoteke).  
- Za zagon zvezka ga odprite v Visual Studio Code, nato kliknite _Select Kernel_ (zgoraj desno) in izberite privzeto možnost Python 3. Sedaj lahko kliknete _Run All_ za izvedbo celotnega zvezka.  
- Za zagon Python aplikacij iz ukazne vrstice sledite navodilom, specifičnim za nalogo, da zagotovite izbiro pravih datotek in podate zahtevane argumente.

## 2. Nastavitev ponudnikov

Naloge **lahko** zahtevajo delo z enim ali več Large Language Model (LLM) sistemi preko podprtih ponudnikov storitev, kot so OpenAI, Azure ali Hugging Face. Ti ponudniki nudijo _gostujočo končno točko_ (API), do katere lahko dostopamo programatsko z ustreznimi poverilnicami (API ključ ali žeton). V tem tečaju obravnavamo naslednje ponudnike:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z različnimi modeli, vključno z osnovno serijo GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s poudarkom na pripravljenosti za podjetja  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za inferenco

**Za te vaje boste morali uporabiti svoje lastne račune**. Naloge so neobvezne, zato lahko izberete nastavitev enega, vseh ali nobenega ponudnika glede na svoje interese. Nekaj napotkov za prijavo:

| Prijava | Cena | API ključ | Igralnica | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Brez kode, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Več modelov na voljo |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio hitri začetek](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Dostop je treba predhodno zaprositi](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni žetoni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sledite spodnjim navodilom za _nastavitev_ tega repozitorija za uporabo z različnimi ponudniki. Naloge, ki zahtevajo določenega ponudnika, bodo v imenu datoteke vsebovale eno od teh oznak:  
 - `aoai` - zahteva Azure OpenAI končno točko in ključ  
 - `oai` - zahteva OpenAI končno točko in ključ  
 - `hf` - zahteva Hugging Face žeton

Lahko nastavite enega, nobenega ali vse ponudnike. Naloge, ki zahtevajo določenega ponudnika, bodo ob manjkajočih poverilnicah preprosto vrgle napako.

###  2.1. Ustvarite `.env` datoteko

Predpostavljamo, da ste prebrali zgornja navodila, se prijavili pri ustreznem ponudniku in pridobili potrebne poverilnice za avtentikacijo (API_KEY ali žeton). V primeru Azure OpenAI predpostavljamo tudi, da imate veljavno namestitev Azure OpenAI storitve (končna točka) z vsaj enim GPT modelom za klepet.

Naslednji korak je nastavitev vaših **lokalnih okoljskih spremenljivk** na naslednji način:

1. V korenski mapi poiščite datoteko `.env.copy`, ki vsebuje nekaj takega:

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

2. Kopirajte to datoteko v `.env` z naslednjim ukazom. Ta datoteka je _gitignore-ana_, kar pomeni, da skrivnosti ostanejo varne.

   ```bash
   cp .env.copy .env
   ```

3. Izpolnite vrednosti (zamenjajte nadomestne znake na desni strani `=`) kot je opisano v naslednjem razdelku.

3. (Opcijsko) Če uporabljate GitHub Codespaces, lahko okoljske spremenljivke shranite kot _Codespaces skrivnosti_, povezane s tem repozitorijem. V tem primeru lokalne `.env` datoteke ne boste potrebovali. **Vendar pa ta možnost deluje samo, če uporabljate GitHub Codespaces.** Če uporabljate Docker Desktop, boste še vedno morali nastaviti `.env` datoteko.

### 2.2. Izpolnite `.env` datoteko

Poglejmo si hitro imena spremenljivk, da razumemo, kaj predstavljajo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je uporabniški dostopni žeton, ki ste ga nastavili v svojem profilu |
| OPENAI_API_KEY | To je avtentikacijski ključ za uporabo storitve za ne-Azure OpenAI končne točke |
| AZURE_OPENAI_API_KEY | To je avtentikacijski ključ za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je nameščena končna točka za Azure OpenAI vir |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka za namestitev modela za _generiranje besedila_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka za namestitev modela za _vektorske predstavitve besedila_ |
| | |

Opomba: Zadnji dve spremenljivki za Azure OpenAI predstavljata privzeti model za klepet (generiranje besedila) in iskanje po vektorjih (embeddingi). Navodila za njihovo nastavitev bodo podana v ustreznih nalogah.

### 2.3 Nastavitev Azure: iz portala

Vrednosti za Azure OpenAI končno točko in ključ boste našli v [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Obiščite [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Kliknite možnost **Keys and Endpoint** v stranski vrstici (meni na levi).  
1. Kliknite **Show Keys** - videli boste: KEY 1, KEY 2 in Endpoint.  
1. Za `AZURE_OPENAI_API_KEY` uporabite vrednost KEY 1.  
1. Za `AZURE_OPENAI_ENDPOINT` uporabite vrednost Endpoint.

Nato potrebujemo končne točke za specifične modele, ki smo jih namestili.

1. Kliknite možnost **Model deployments** v stranski vrstici (meni na levi) za Azure OpenAI vir.  
1. Na ciljni strani kliknite **Manage Deployments**.

To vas bo pripeljalo do spletnega mesta Azure OpenAI Studio, kjer bomo našli ostale vrednosti, kot je opisano spodaj.

### 2.4 Nastavitev Azure: iz studia

1. Pojdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašega vira**, kot je opisano zgoraj.  
1. Kliknite zavihek **Deployments** (stranska vrstica, levo), da si ogledate trenutno nameščene modele.  
1. Če želenega modela ni nameščenega, uporabite **Create new deployment** za namestitev.  
1. Potrebovali boste model za _generiranje besedila_ - priporočamo: **gpt-35-turbo**  
1. Potrebovali boste model za _vektorske predstavitve besedila_ - priporočamo **text-embedding-ada-002**

Sedaj posodobite okoljske spremenljivke, da odražajo _ime namestitve_ (Deployment name), ki ste ga uporabili. Običajno je enako imenu modela, razen če ste ga izrecno spremenili. Na primer, lahko imate:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne pozabite shraniti `.env` datoteke, ko končate**. Sedaj lahko zaprete datoteko in se vrnete k navodilom za zagon zvezka.

### 2.5 Nastavitev OpenAI: iz profila

Vaš OpenAI API ključ najdete v svojem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga še nimate, se lahko prijavite in ustvarite API ključ. Ko imate ključ, ga lahko uporabite za izpolnitev spremenljivke `OPENAI_API_KEY` v `.env` datoteki.

### 2.6 Nastavitev Hugging Face: iz profila

Vaš Hugging Face žeton najdete v svojem profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte jih ali delite javno. Namesto tega ustvarite nov žeton za uporabo v tem projektu in ga kopirajte v `.env` datoteko pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ Tehnično to ni API ključ, vendar se uporablja za avtentikacijo, zato ohranjamo to poimenovanje zaradi doslednosti.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.