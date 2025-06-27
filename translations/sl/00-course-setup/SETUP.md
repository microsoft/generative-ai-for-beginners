<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:31:48+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sl"
}
-->
# Nastavitev vašega razvojnega okolja

To repozitorij in tečaj smo nastavili z [razvojnim vsebnikom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ki ima univerzalno izvajalno okolje, ki podpira razvoj v Python3, .NET, Node.js in Java. Povezana konfiguracija je opredeljena v datoteki `devcontainer.json`, ki se nahaja v mapi `.devcontainer/` na korenskem nivoju tega repozitorija.

Za aktivacijo razvojnega vsebnika ga zaženite v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za izvajalno okolje v oblaku) ali v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za izvajalno okolje na lokalni napravi). Preberite [to dokumentacijo](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) za več podrobnosti o delovanju razvojnih vsebnikov znotraj VS Code.

> [!TIP]  
> Priporočamo uporabo GitHub Codespaces za hiter začetek z minimalnim naporom. Ponuja velikodušno [kvoto brezplačne uporabe](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za osebne račune. Nastavite [časovne omejitve](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) za zaustavitev ali brisanje neaktivnih codespaces, da čim bolj izkoristite svojo kvoto.

## 1. Izvajanje nalog

Vsaka lekcija bo imela _neobvezne_ naloge, ki so lahko na voljo v enem ali več programskih jezikih, vključno z: Python, .NET/C#, Java in JavaScript/TypeScript. Ta del ponuja splošne smernice v zvezi z izvajanjem teh nalog.

### 1.1 Python naloge

Python naloge so na voljo bodisi kot aplikacije (datoteke `.py`) ali Jupyter beležnice (datoteke `.ipynb`).
- Za zagon beležnice jo odprite v Visual Studio Code, nato kliknite _Select Kernel_ (zgoraj desno) in izberite privzeto možnost Python 3, ki je prikazana. Sedaj lahko izberete _Run All_ za izvedbo beležnice.
- Za zagon Python aplikacij iz ukazne vrstice sledite navodilom, specifičnim za nalogo, da zagotovite pravilno izbiro datotek in zagotovitev zahtevanih argumentov.

## 2. Konfiguracija ponudnikov

Naloge **lahko** nastavite tudi za delo proti eni ali več namestitvam Velikih Jezikovnih Modelov (LLM) prek podprtega ponudnika storitev, kot so OpenAI, Azure ali Hugging Face. Ti zagotavljajo _gostiteljsko končno točko_ (API), do katere lahko dostopamo programsko z ustreznimi poverilnicami (API ključ ali žeton). V tem tečaju razpravljamo o teh ponudnikih:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z raznolikimi modeli, vključno z osnovno serijo GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za OpenAI modele s poudarkom na pripravljenosti za podjetja.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za sklepanje.

**Za te vaje boste morali uporabiti svoje račune**. Naloge so neobvezne, zato se lahko odločite za nastavitev enega, vseh - ali nobenega - od ponudnikov glede na vaše interese. Nekaj smernic za prijavo:

| Prijava | Strošek | API ključ | Igralnica | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na podlagi projekta](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Brez kode, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Na voljo več modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Hitri začetek SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Hitri začetek studia](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Potrebna je predhodna prijava za dostop](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni žetoni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sledite spodnjim navodilom za _konfiguracijo_ tega repozitorija za uporabo z različnimi ponudniki. Naloge, ki zahtevajo določenega ponudnika, bodo vsebovale enega od teh oznak v svojem imenu datoteke:
- `aoai` - zahteva Azure OpenAI končno točko, ključ
- `oai` - zahteva OpenAI končno točko, ključ
- `hf` - zahteva Hugging Face žeton

Lahko konfigurirate enega, nobenega ali vse ponudnike. Povezane naloge bodo preprosto javljale napako ob manjkajočih poverilnicah.

### 2.1. Ustvarite datoteko `.env`

Predpostavljamo, da ste že prebrali zgornje smernice, se prijavili pri ustreznem ponudniku in pridobili potrebne poverilnice za preverjanje pristnosti (API_KEY ali žeton). V primeru Azure OpenAI predpostavljamo, da imate tudi veljavno namestitev Azure OpenAI storitve (končna točka) z vsaj enim GPT modelom, nameščenim za dokončanje klepeta.

Naslednji korak je konfiguracija vaših **lokalnih spremenljivk okolja** na naslednji način:

1. Poiščite datoteko `.env.copy` v korenski mapi, ki bi morala imeti vsebino, kot je ta:

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

2. Kopirajte to datoteko v `.env` z uporabo spodnjega ukaza. Ta datoteka je _gitignore-d_, kar ohranja skrivnosti varne.

   ```bash
   cp .env.copy .env
   ```

3. Izpolnite vrednosti (zamenjajte nadomestne znake na desni strani `=`), kot je opisano v naslednjem razdelku.

3. (Možnost) Če uporabljate GitHub Codespaces, imate možnost shraniti spremenljivke okolja kot _Codespaces skrivnosti_, povezane s tem repozitorijem. V tem primeru vam ne bo treba nastaviti lokalne .env datoteke. **Vendar pa ta možnost deluje le, če uporabljate GitHub Codespaces.** Še vedno boste morali nastaviti .env datoteko, če uporabljate Docker Desktop.

### 2.2. Izpolnite datoteko `.env`

Poglejmo hitro imena spremenljivk, da razumemo, kaj predstavljajo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je uporabniški dostopni žeton, ki ste ga nastavili v svojem profilu |
| OPENAI_API_KEY | To je ključ za avtorizacijo za uporabo storitve za ne-Azure OpenAI končne točke |
| AZURE_OPENAI_API_KEY | To je ključ za avtorizacijo za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je nameščena končna točka za Azure OpenAI vir |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka za nameščanje modela za _generiranje besedila_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka za nameščanje modela za _besedilne vdelave_ |
| | |

Opomba: Zadnji dve spremenljivki Azure OpenAI odražata privzeti model za dokončanje klepeta (generiranje besedila) in iskanje vektorjev (vdelave). Navodila za njihovo nastavitev bodo opredeljena v ustreznih nalogah.

### 2.3 Konfiguracija Azure: Iz portala

Vrednosti za Azure OpenAI končno točko in ključ bodo najdene v [Azure Portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Pojdite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite možnost **Ključi in končna točka** v stranski vrstici (meni na levi).
1. Kliknite **Pokaži ključe** - morali bi videti naslednje: KLJUČ 1, KLJUČ 2 in Končna točka.
1. Uporabite vrednost KLJUČA 1 za AZURE_OPENAI_API_KEY
1. Uporabite vrednost Končne točke za AZURE_OPENAI_ENDPOINT

Naslednji korak je pridobitev končnih točk za specifične modele, ki smo jih namestili.

1. Kliknite možnost **Nameščanje modelov** v stranski vrstici (levi meni) za Azure OpenAI vir.
1. Na ciljni strani kliknite **Upravljanje nameščanj**

To vas bo pripeljalo na spletno stran Azure OpenAI Studio, kjer bomo našli druge vrednosti, kot je opisano spodaj.

### 2.4 Konfiguracija Azure: Iz studia

1. Pomaknite se do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz vašega vira**, kot je opisano zgoraj.
1. Kliknite zavihek **Nameščanja** (stranska vrstica, levo), da si ogledate trenutno nameščene modele.
1. Če vaš želeni model ni nameščen, uporabite **Ustvari novo nameščanje**, da ga namestite.
1. Potrebovali boste model za _generiranje besedila_ - priporočamo: **gpt-35-turbo**
1. Potrebovali boste model za _besedilne vdelave_ - priporočamo **text-embedding-ada-002**

Zdaj posodobite spremenljivke okolja, da odražajo _Ime nameščanja_, ki ste ga uporabili. To bo običajno enako imenu modela, razen če ste ga izrecno spremenili. Tako bi lahko na primer imeli:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne pozabite shraniti .env datoteke, ko končate**. Zdaj lahko zapustite datoteko in se vrnete k navodilom za zagon beležnice.

### 2.5 Konfiguracija OpenAI: Iz profila

Vaš OpenAI API ključ lahko najdete v vašem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga nimate, se lahko prijavite za račun in ustvarite API ključ. Ko imate ključ, ga lahko uporabite za izpolnitev spremenljivke `OPENAI_API_KEY` v datoteki `.env`.

### 2.6 Konfiguracija Hugging Face: Iz profila

Vaš Hugging Face žeton lahko najdete v vašem profilu pod [Dostopni žetoni](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte ali delite teh javno. Namesto tega ustvarite nov žeton za uporabo tega projekta in ga kopirajte v datoteko `.env` pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ To tehnično ni API ključ, ampak se uporablja za preverjanje pristnosti, zato ohranjamo to poimenovanje za doslednost.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.