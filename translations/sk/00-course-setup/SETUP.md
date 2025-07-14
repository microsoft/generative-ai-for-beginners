<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:36:23+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sk"
}
-->
# Nastavenie vývojového prostredia

Tento repozitár a kurz sme nastavili s [vývojovým kontajnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ktorý obsahuje univerzálne runtime prostredie podporujúce Python3, .NET, Node.js a Java vývoj. Súvisiaca konfigurácia je definovaná v súbore `devcontainer.json`, ktorý sa nachádza v priečinku `.devcontainer/` v koreňovom adresári tohto repozitára.

Na aktiváciu vývojového kontajnera ho spustite v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pre cloudové runtime) alebo v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pre lokálne runtime na vašom zariadení). Pre viac informácií o fungovaní vývojových kontajnerov vo VS Code si prečítajte [túto dokumentáciu](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).  

> [!TIP]  
> Odporúčame použiť GitHub Codespaces pre rýchly štart s minimálnym úsilím. Poskytuje štedrú [bezplatnú kvótu](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pre osobné účty. Nastavte [timeouty](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) na zastavenie alebo vymazanie neaktívnych codespaces, aby ste čo najlepšie využili svoju kvótu.


## 1. Spúšťanie úloh

Každá lekcia bude mať _voliteľné_ úlohy, ktoré môžu byť poskytnuté v jednom alebo viacerých programovacích jazykoch vrátane: Python, .NET/C#, Java a JavaScript/TypeScript. Táto sekcia poskytuje všeobecné pokyny týkajúce sa spúšťania týchto úloh.

### 1.1 Python úlohy

Python úlohy sú poskytované buď ako aplikácie (`.py` súbory) alebo Jupyter notebooky (`.ipynb` súbory).  
- Na spustenie notebooku ho otvorte vo Visual Studio Code, kliknite na _Select Kernel_ (vpravo hore) a vyberte predvolenú možnosť Python 3. Teraz môžete použiť _Run All_ na spustenie celého notebooku.  
- Na spustenie Python aplikácií z príkazového riadku postupujte podľa inštrukcií konkrétnej úlohy, aby ste vybrali správne súbory a zadali potrebné argumenty.

## 2. Konfigurácia poskytovateľov

Úlohy **môžu** byť tiež nastavené na prácu s jedným alebo viacerými nasadeniami veľkých jazykových modelov (LLM) cez podporovaného poskytovateľa služieb ako OpenAI, Azure alebo Hugging Face. Tieto poskytujú _hostovaný endpoint_ (API), ku ktorému môžeme programovo pristupovať s platnými povereniami (API kľúč alebo token). V tomto kurze sa venujeme týmto poskytovateľom:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznymi modelmi vrátane základnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pre OpenAI modely so zameraním na podnikové použitie.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a inference server.

**Na tieto cvičenia budete potrebovať vlastné účty**. Úlohy sú voliteľné, takže si môžete vybrať nastavenie jedného, všetkých alebo žiadneho z poskytovateľov podľa svojich záujmov. Niekoľko rád pre registráciu:

| Registrácia | Cena | API kľúč | Playground | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektové kľúče](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Viacero dostupných modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rýchly štart SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rýchly štart Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Nutné požiadať o prístup vopred](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenník](https://huggingface.co/pricing) | [Prístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzený počet modelov](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podľa nasledujúcich pokynov na _konfiguráciu_ tohto repozitára pre použitie s rôznymi poskytovateľmi. Úlohy, ktoré vyžadujú konkrétneho poskytovateľa, budú mať v názve súboru jednu z týchto značiek:
 - `aoai` - vyžaduje Azure OpenAI endpoint a kľúč
 - `oai` - vyžaduje OpenAI endpoint a kľúč
 - `hf` - vyžaduje Hugging Face token

Môžete nakonfigurovať jedného, žiadneho alebo všetkých poskytovateľov. Súvisiace úlohy jednoducho zlyhajú, ak chýbajú poverenia.

###  2.1. Vytvorenie súboru `.env`

Predpokladáme, že ste si prečítali vyššie uvedené pokyny, zaregistrovali sa u príslušného poskytovateľa a získali potrebné autentifikačné údaje (API_KEY alebo token). V prípade Azure OpenAI predpokladáme, že máte platné nasadenie služby Azure OpenAI (endpoint) s aspoň jedným GPT modelom nasadeným pre chat completion.

Ďalším krokom je nastavenie **lokálnych premenných prostredia** nasledovne:


1. V koreňovom priečinku nájdite súbor `.env.copy`, ktorý by mal obsahovať niečo takéto:

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

2. Skopírujte tento súbor do `.env` pomocou nasledujúceho príkazu. Tento súbor je _gitignore-ovaný_, takže tajné údaje zostanú v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly napravo od `=`) podľa popisu v nasledujúcej sekcii.

3. (Voliteľné) Ak používate GitHub Codespaces, môžete si uložiť premenné prostredia ako _Codespaces secrets_ priradené k tomuto repozitáru. V takom prípade nemusíte nastavovať lokálny súbor .env. **Táto možnosť však funguje iba pri použití GitHub Codespaces.** Ak používate Docker Desktop, stále budete musieť nastaviť súbor .env.


### 2.2. Vyplnenie súboru `.env`

Pozrime sa rýchlo na názvy premenných, aby sme pochopili, čo predstavujú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je používateľský prístupový token, ktorý si nastavíte vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč pre použitie služby mimo Azure OpenAI endpointov |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč pre použitie Azure OpenAI služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený endpoint pre Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasadenia modelu pre _generovanie textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasadenia modelu pre _textové embeddingy_ |
| | |

Poznámka: Posledné dve premenné pre Azure OpenAI odrážajú predvolený model pre chat completion (generovanie textu) a vyhľadávanie vektorov (embeddingy). Inštrukcie na ich nastavenie budú uvedené v príslušných úlohách.


### 2.3 Konfigurácia Azure: cez Portal

Hodnoty endpointu a kľúča pre Azure OpenAI nájdete v [Azure Portáli](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začnime teda tam.

1. Prejdite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Keys and Endpoint** v bočnom menu (vľavo).
1. Kliknite na **Show Keys** - mali by ste vidieť: KEY 1, KEY 2 a Endpoint.
1. Použite hodnotu KEY 1 pre AZURE_OPENAI_API_KEY
1. Použite hodnotu Endpoint pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme endpointy pre konkrétne modely, ktoré sme nasadili.

1. Kliknite na možnosť **Model deployments** v bočnom menu (vľavo) pre Azure OpenAI zdroj.
1. Na cieľovej stránke kliknite na **Manage Deployments**

Tým sa dostanete na web Azure OpenAI Studio, kde nájdeme ďalšie hodnoty podľa popisu nižšie.

### 2.4 Konfigurácia Azure: cez Studio

1. Prejdite do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **cez svoj zdroj** ako bolo popísané vyššie.
1. Kliknite na záložku **Deployments** (bočné menu vľavo) pre zobrazenie aktuálne nasadených modelov.
1. Ak váš požadovaný model nie je nasadený, použite **Create new deployment** na jeho nasadenie.
1. Budete potrebovať model pre _generovanie textu_ - odporúčame: **gpt-35-turbo**
1. Budete potrebovať model pre _textové embeddingy_ - odporúčame **text-embedding-ada-002**

Teraz aktualizujte premenné prostredia tak, aby odrážali názov _nasadenia_ (Deployment name), ktorý ste použili. Zvyčajne to bude rovnaké ako názov modelu, pokiaľ ste ho výslovne nezmenili. Napríklad môžete mať:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezabudnite súbor .env uložiť po úprave**. Teraz môžete súbor zatvoriť a pokračovať podľa inštrukcií na spustenie notebooku.

### 2.5 Konfigurácia OpenAI: cez profil

Váš OpenAI API kľúč nájdete vo svojom [OpenAI účte](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ho ešte nemáte, môžete si vytvoriť účet a vygenerovať API kľúč. Po získaní kľúča ho použite na vyplnenie premennej `OPENAI_API_KEY` v súbore `.env`.

### 2.6 Konfigurácia Hugging Face: cez profil

Váš Hugging Face token nájdete vo svojom profile pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezverejňujte ho ani nezdieľajte verejne. Namiesto toho si vytvorte nový token pre použitie v tomto projekte a skopírujte ho do súboru `.env` pod premennú `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky nejde o API kľúč, ale používa sa na autentifikáciu, preto sme zachovali tento názov pre konzistenciu.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.