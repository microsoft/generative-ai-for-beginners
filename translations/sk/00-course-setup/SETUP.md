<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:28:23+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sk"
}
-->
# Nastavenie vášho vývojového prostredia

Tento repozitár a kurz sme nastavili s [vývojovým kontajnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ktorý má univerzálny runtime podporujúci vývoj v Python3, .NET, Node.js a Java. Súvisiaca konfigurácia je definovaná v súbore `devcontainer.json` umiestnenom v priečinku `.devcontainer/` na koreňovej úrovni tohto repozitára.

Na aktiváciu vývojového kontajnera ho spustite v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pre cloud-hostovaný runtime) alebo v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pre lokálne hostovaný runtime). Prečítajte si [túto dokumentáciu](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pre viac detailov o fungovaní vývojových kontajnerov vo VS Code.  

> [!TIP]  
> Odporúčame používať GitHub Codespaces pre rýchly štart s minimálnym úsilím. Poskytuje štedrú [bezplatnú kvótu použitia](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pre osobné účty. Nastavte [časové limity](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) na zastavenie alebo odstránenie neaktívnych codespaces, aby ste maximalizovali využitie vašej kvóty.


## 1. Vykonávanie úloh

Každá lekcia bude mať _voliteľné_ úlohy, ktoré môžu byť poskytnuté v jednom alebo viacerých programovacích jazykoch vrátane: Python, .NET/C#, Java a JavaScript/TypeScript. Táto sekcia poskytuje všeobecné pokyny týkajúce sa vykonávania týchto úloh.

### 1.1 Úlohy v Pythone

Úlohy v Pythone sú poskytované buď ako aplikácie (súbory `.py`) alebo Jupyter notebooky (súbory `.ipynb`). 
- Na spustenie notebooku ho otvorte vo Visual Studio Code a potom kliknite na _Select Kernel_ (vpravo hore) a vyberte predvolenú možnosť Python 3. Teraz môžete kliknúť na _Run All_ na vykonanie notebooku.
- Na spustenie Python aplikácií z príkazového riadku, postupujte podľa pokynov špecifických pre úlohu, aby ste sa uistili, že vyberiete správne súbory a poskytnete požadované argumenty.

## 2. Konfigurácia poskytovateľov

Úlohy **môžu** byť tiež nastavené na prácu s jedným alebo viacerými nasadeniami Large Language Model (LLM) prostredníctvom podporovaného poskytovateľa služieb ako OpenAI, Azure alebo Hugging Face. Tieto poskytujú _hostovaný endpoint_ (API), ku ktorému môžeme programovo pristupovať so správnymi povereniami (API kľúč alebo token). V tomto kurze diskutujeme o týchto poskytovateľoch:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznymi modelmi vrátane základnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pre OpenAI modely so zameraním na pripravenosť pre podniky.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a inferenčný server.

**Budete potrebovať používať vlastné účty pre tieto cvičenia**. Úlohy sú voliteľné, takže sa môžete rozhodnúť nastaviť jedného, všetkých - alebo žiadneho - z poskytovateľov na základe vašich záujmov. Niekoľko pokynov pre registráciu:

| Registrácia | Cena | API kľúč | Playground | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektovo založené](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupné viaceré modely |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Musíte požiadať vopred o prístup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenník](https://huggingface.co/pricing) | [Prístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podľa pokynov nižšie na _konfiguráciu_ tohto repozitára pre použitie s rôznymi poskytovateľmi. Úlohy, ktoré vyžadujú konkrétneho poskytovateľa, budú obsahovať jeden z týchto tagov vo svojom názve súboru:
 - `aoai` - vyžaduje Azure OpenAI endpoint, kľúč
 - `oai` - vyžaduje OpenAI endpoint, kľúč
 - `hf` - vyžaduje Hugging Face token

Môžete konfigurovať jedného, žiadneho, alebo všetkých poskytovateľov. Súvisiace úlohy jednoducho zlyhajú na chýbajúcich povereniach.

###  2.1. Vytvorenie súboru `.env`

Predpokladáme, že ste už prečítali vyššie uvedené pokyny a zaregistrovali sa u relevantného poskytovateľa a získali požadované autentifikačné poverenia (API_KEY alebo token). V prípade Azure OpenAI predpokladáme, že máte tiež platné nasadenie Azure OpenAI služby (endpoint) s aspoň jedným GPT modelom nasadeným pre chat completion.

Ďalším krokom je nastavenie vašich **lokálnych environmentálnych premenných** nasledovne:


1. Pozrite sa do koreňového priečinka na súbor `.env.copy`, ktorý by mal mať obsah ako tento:

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

2. Skopírujte tento súbor do `.env` pomocou príkazu nižšie. Tento súbor je _gitignore-d_, čo udržuje tajomstvá v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly na pravej strane `=`) ako je popísané v nasledujúcej sekcii.

3. (Voliteľné) Ak používate GitHub Codespaces, máte možnosť uložiť environmentálne premenné ako _Codespaces secrets_ spojené s týmto repozitárom. V takom prípade nebudete potrebovať nastaviť lokálny .env súbor. **Avšak, všimnite si, že táto možnosť funguje len ak používate GitHub Codespaces.** Stále budete potrebovať nastaviť .env súbor, ak používate Docker Desktop.


### 2.2. Naplnenie súboru `.env`

Pozrime sa rýchlo na názvy premenných, aby sme pochopili, čo predstavujú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je prístupový token používateľa, ktorý ste nastavili vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč pre používanie služby pre ne-Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč pre používanie tej služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený endpoint pre Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je _text-generating_ model nasadenie endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je _text embeddings_ model nasadenie endpoint |
| | |

Poznámka: Posledné dve premenné Azure OpenAI odrážajú predvolený model pre chat completion (text generovanie) a vektorové vyhľadávanie (embeddings) respektíve. Pokyny na ich nastavenie budú definované v relevantných úlohách.


### 2.3 Konfigurácia Azure: Z portálu

Hodnoty endpointu a kľúča Azure OpenAI nájdete v [Azure Portáli](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), takže začnime tam.

1. Prejdite na [Azure Portál](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Keys and Endpoint** v postrannom paneli (menu naľavo).
1. Kliknite na **Show Keys** - mali by ste vidieť nasledovné: KEY 1, KEY 2 a Endpoint.
1. Použite hodnotu KEY 1 pre AZURE_OPENAI_API_KEY
1. Použite hodnotu Endpoint pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme endpointy pre konkrétne modely, ktoré sme nasadili.

1. Kliknite na možnosť **Model deployments** v postrannom paneli (ľavé menu) pre Azure OpenAI zdroj.
1. Na cieľovej stránke kliknite na **Manage Deployments**

To vás zavedie na webovú stránku Azure OpenAI Studio, kde nájdeme ďalšie hodnoty ako je popísané nižšie.

### 2.4 Konfigurácia Azure: Zo štúdia

1. Prejdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **zo svojho zdroja** ako je popísané vyššie.
1. Kliknite na záložku **Deployments** (postranný panel, vľavo) na zobrazenie aktuálne nasadených modelov.
1. Ak váš požadovaný model nie je nasadený, použite **Create new deployment** na jeho nasadenie.
1. Budete potrebovať _text-generating_ model - odporúčame: **gpt-35-turbo**
1. Budete potrebovať _text-embedding_ model - odporúčame **text-embedding-ada-002**

Teraz aktualizujte environmentálne premenné tak, aby odrážali _Deployment name_ použité. To bude typicky rovnaké ako názov modelu, pokiaľ ste ho explicitne nezmenili. Takže, ako príklad, môžete mať:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezabudnite uložiť súbor .env po dokončení**. Teraz môžete opustiť súbor a vrátiť sa k pokynom na spustenie notebooku.

### 2.5 Konfigurácia OpenAI: Z profilu

Váš OpenAI API kľúč nájdete vo vašom [OpenAI účte](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ho nemáte, môžete sa zaregistrovať na účet a vytvoriť API kľúč. Akonáhle máte kľúč, môžete ho použiť na vyplnenie premenné `OPENAI_API_KEY` v súbore `.env`.

### 2.6 Konfigurácia Hugging Face: Z profilu

Váš Hugging Face token nájdete vo svojom profile pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nepublikujte ani nezdieľajte tieto verejne. Namiesto toho vytvorte nový token pre použitie tohto projektu a skopírujte ho do súboru `.env` pod premennú `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to nie je API kľúč, ale používa sa na autentifikáciu, takže zachovávame túto konvenciu pomenovania pre konzistenciu.

**Vylúčenie zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.