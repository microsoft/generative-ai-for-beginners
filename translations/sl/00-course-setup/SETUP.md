<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T13:02:11+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sl"
}
-->
# Postavite svoje razvojno okolje

To repozitorij in tečaj smo nastavili z [razvojnim vsebnikom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ki ima univerzalno okolje za razvoj v Python3, .NET, Node.js in Java. Povezana konfiguracija je opredeljena v datoteki `devcontainer.json`, ki se nahaja v mapi `.devcontainer/` na korenu tega repozitorija.

Za aktivacijo razvojnega vsebnika ga zaženite v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (za okolje, gostovano v oblaku) ali v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (za okolje, gostovano na lokalni napravi). Preberite [to dokumentacijo](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) za več podrobnosti o delovanju razvojnih vsebnikov v VS Code.

> [!TIP]  
> Priporočamo uporabo GitHub Codespaces za hiter začetek z minimalnim naporom. Ponuja velikodušno [kvoto brezplačne uporabe](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) za osebne račune. Nastavite [časovne omejitve](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) za zaustavitev ali izbris neaktivnih kodnih prostorov, da maksimizirate uporabo svoje kvote.

## 1. Izvajanje nalog

Vsaka lekcija bo imela _neobvezne_ naloge, ki so lahko na voljo v enem ali več programskih jezikih, vključno z: Python, .NET/C#, Java in JavaScript/TypeScript. Ta del ponuja splošne smernice za izvajanje teh nalog.

### 1.1 Naloge v Pythonu

Naloge v Pythonu so na voljo bodisi kot aplikacije (datoteke `.py`) ali kot Jupyter beležke (datoteke `.ipynb`). 
- Za zagon beležke jo odprite v Visual Studio Code in nato kliknite _Izberi jedro_ (zgoraj desno) ter izberite privzeto možnost Python 3. Sedaj lahko uporabite _Zaženi vse_ za izvedbo beležke.
- Za zagon aplikacij Python iz ukazne vrstice sledite navodilom, specifičnim za nalogo, da zagotovite izbiro pravih datotek in zagotovite potrebne argumente.

## 2. Konfiguracija ponudnikov

Naloge **lahko** nastavite tudi za delo z enim ali več uvedbami Velikih Jezikovnih Modelov (LLM) prek podprtega ponudnika storitev, kot so OpenAI, Azure ali Hugging Face. Ti zagotavljajo _gostovan končni točki_ (API), do katerega lahko dostopamo programsko s pravimi poverilnicami (API ključ ali žeton). V tem tečaju obravnavamo te ponudnike:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z različnimi modeli, vključno z glavno serijo GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) za modele OpenAI s poudarkom na pripravljenosti za podjetja
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) za odprtokodne modele in strežnik za inferenco

**Za te vaje boste morali uporabiti svoje račune**. Naloge so neobvezne, tako da lahko izberete nastavitev enega, vseh - ali nobenega - od ponudnikov, glede na vaše interese. Nekaj smernic za prijavo:

| Prijava | Strošek | API ključ | Igralnica | Komentarji |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na podlagi projekta](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Brez kode, splet](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Na voljo več modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Hiter začetek SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Hiter začetek studia](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Treba se je prijaviti vnaprej za dostop](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenik](https://huggingface.co/pricing) | [Dostopni žetoni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ima omejene modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sledite spodnjim navodilom za _konfiguracijo_ tega repozitorija za uporabo z različnimi ponudniki. Naloge, ki zahtevajo določenega ponudnika, bodo v svojem imenu vsebovale enega od teh oznak:
 - `aoai` - zahteva Azure OpenAI končni točki, ključ
 - `oai` - zahteva OpenAI končni točki, ključ
 - `hf` - zahteva Hugging Face žeton

Lahko konfigurirate enega, nobenega ali vse ponudnike. Povezane naloge bodo preprosto javljale napako pri manjkajočih poverilnicah.

###  2.1. Ustvarite datoteko `.env`

Predvidevamo, da ste že prebrali zgornje smernice in se prijavili pri ustreznem ponudniku ter pridobili potrebne poverilnice za avtentikacijo (API_KEY ali žeton). V primeru Azure OpenAI predvidevamo, da imate tudi veljavno uvedbo storitve Azure OpenAI (končni točki) z vsaj enim GPT modelom, uvedenim za dokončanje klepeta.

Naslednji korak je konfiguracija vaših **lokalnih okoljskih spremenljivk** na naslednji način:

1. V korenski mapi poiščite datoteko `.env.copy`, ki bi morala imeti vsebino, kot je ta:

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

3. Izpolnite vrednosti (zamenjajte nadomestna mesta na desni strani `=`) kot je opisano v naslednjem razdelku.

3. (Opcija) Če uporabljate GitHub Codespaces, imate možnost shraniti okoljske spremenljivke kot _Codespaces skrivnosti_ povezane s tem repozitorijem. V tem primeru vam ne bo treba nastaviti lokalne .env datoteke. **Vendar upoštevajte, da ta možnost deluje le, če uporabljate GitHub Codespaces.** Še vedno boste morali nastaviti .env datoteko, če uporabljate Docker Desktop.

### 2.2. Izpolnite datoteko `.env`

Poglejmo hitro imena spremenljivk, da razumemo, kaj predstavljajo:

| Spremenljivka  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To je uporabniški dostopni žeton, ki ste ga nastavili v svojem profilu |
| OPENAI_API_KEY | To je avtorizacijski ključ za uporabo storitve za ne-Azure OpenAI končne točke |
| AZURE_OPENAI_API_KEY | To je avtorizacijski ključ za uporabo te storitve |
| AZURE_OPENAI_ENDPOINT | To je uvedena končna točka za vir Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | To je končna točka za uvedbo modela za generiranje besedila |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To je končna točka za uvedbo modela za vdelavo besedila |
| | |

Opomba: Zadnji dve spremenljivki Azure OpenAI odražata privzeti model za dokončanje klepeta (generiranje besedila) in iskanje vektorjev (vdelave) oziroma. Navodila za njihovo nastavitev bodo opredeljena v ustreznih nalogah.

### 2.3 Konfigurirajte Azure: Iz portala

Vrednosti končne točke in ključa Azure OpenAI boste našli v [Azure portalu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), zato začnimo tam.

1. Pojdite na [Azure portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite možnost **Ključi in končna točka** v stranski vrstici (meni na levi).
1. Kliknite **Prikaži ključe** - videli boste naslednje: KLJUČ 1, KLJUČ 2 in Končna točka.
1. Uporabite vrednost KLJUČA 1 za AZURE_OPENAI_API_KEY
1. Uporabite vrednost končne točke za AZURE_OPENAI_ENDPOINT

Nato potrebujemo končne točke za specifične modele, ki smo jih uvedli.

1. Kliknite možnost **Modelne uvedbe** v stranski vrstici (levi meni) za vir Azure OpenAI.
1. Na ciljni strani kliknite **Upravljanje uvedb**

To vas bo popeljalo na spletno mesto Azure OpenAI Studio, kjer bomo našli druge vrednosti, kot je opisano spodaj.

### 2.4 Konfigurirajte Azure: Iz studia

1. Pojdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iz svojega vira**, kot je opisano zgoraj.
1. Kliknite zavihek **Uvedbe** (stranska vrstica, levo), da si ogledate trenutno uvedene modele.
1. Če vaš želeni model ni uveden, uporabite **Ustvari novo uvedbo** za njegovo uvedbo.
1. Potrebovali boste model za _generiranje besedila_ - priporočamo: **gpt-35-turbo**
1. Potrebovali boste model za _vdelavo besedila_ - priporočamo **text-embedding-ada-002**

Sedaj posodobite okoljske spremenljivke, da odražajo _Ime uvedbe_, ki ste ga uporabili. To bo običajno enako imenu modela, razen če ste ga izrecno spremenili. Tako boste imeli na primer:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ne pozabite shraniti datoteke .env, ko končate**. Sedaj lahko zapustite datoteko in se vrnete k navodilom za zagon beležke.

### 2.5 Konfigurirajte OpenAI: Iz profila

Vaš OpenAI API ključ lahko najdete v vašem [OpenAI računu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Če ga nimate, se lahko prijavite za račun in ustvarite API ključ. Ko imate ključ, ga lahko uporabite za izpolnitev spremenljivke `OPENAI_API_KEY` v datoteki `.env`.

### 2.6 Konfigurirajte Hugging Face: Iz profila

Vaš Hugging Face žeton lahko najdete v svojem profilu pod [Dostopni žetoni](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne objavljajte ali delite teh javno. Namesto tega ustvarite nov žeton za uporabo v tem projektu in ga kopirajte v datoteko `.env` pod spremenljivko `HUGGING_FACE_API_KEY`. _Opomba:_ Tehnično to ni API ključ, ampak se uporablja za avtentikacijo, zato ohranjamo to poimenovalno konvencijo za doslednost.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, bodite pozorni, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.