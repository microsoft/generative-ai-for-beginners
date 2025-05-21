<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:58:45+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sk"
}
-->
# Nastavenie vášho vývojového prostredia

Tento repozitár a kurz sme nastavili s [vývojovým kontajnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst), ktorý má univerzálny runtime podporujúci vývoj v Python3, .NET, Node.js a Java. Súvisiaca konfigurácia je definovaná v súbore `devcontainer.json` umiestnenom v priečinku `.devcontainer/` v koreňovom adresári tohto repozitára.

Na aktiváciu vývojového kontajnera ho spustite v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pre cloud-hostovaný runtime) alebo v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pre lokálne hostovaný runtime). Prečítajte si [túto dokumentáciu](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pre viac podrobností o tom, ako vývojové kontajnery fungujú vo VS Code.  

> [!TIP]  
> Odporúčame použiť GitHub Codespaces pre rýchly štart s minimálnym úsilím. Poskytuje štedrú [kvótu bezplatného používania](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pre osobné účty. Nastavte [časové limity](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) na zastavenie alebo odstránenie neaktívnych codespaces, aby ste maximalizovali využitie svojej kvóty.

## 1. Vykonávanie úloh

Každá lekcia bude mať _nepovinné_ úlohy, ktoré môžu byť poskytnuté v jednom alebo viacerých programovacích jazykoch vrátane: Python, .NET/C#, Java a JavaScript/TypeScript. Táto časť poskytuje všeobecné pokyny týkajúce sa vykonávania týchto úloh.

### 1.1 Úlohy v Pythone

Úlohy v Pythone sú poskytnuté buď ako aplikácie (súbory `.py`) alebo Jupyter notebooky (súbory `.ipynb`). 
- Ak chcete spustiť notebook, otvorte ho vo Visual Studio Code a potom kliknite na _Select Kernel_ (vpravo hore) a vyberte predvolenú možnosť Python 3. Teraz môžete zvoliť _Run All_ na vykonanie notebooku.
- Na spustenie Python aplikácií z príkazového riadku postupujte podľa pokynov špecifických pre úlohu, aby ste sa uistili, že vyberáte správne súbory a poskytujete potrebné argumenty.

## 2. Konfigurácia poskytovateľov

Úlohy **môžu** byť tiež nastavené tak, aby fungovali proti jednému alebo viacerým nasadeniam veľkých jazykových modelov (LLM) prostredníctvom podporovaného poskytovateľa služieb ako OpenAI, Azure alebo Hugging Face. Tieto poskytujú _hostovaný endpoint_ (API), ktorý môžeme programovo pristupovať s príslušnými povereniami (API kľúč alebo token). V tomto kurze sa zaoberáme týmito poskytovateľmi:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznymi modelmi vrátane hlavnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pre OpenAI modely s dôrazom na pripravenosť pre podniky
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a server na inferenciu

**Budete potrebovať použiť svoje vlastné účty pre tieto cvičenia**. Úlohy sú nepovinné, takže si môžete vybrať nastavenie jedného, všetkých - alebo žiadneho - z poskytovateľov na základe vašich záujmov. Niektoré pokyny na registráciu:

| Registrácia | Náklady | API Kľúč | Ihrisko | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceny](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na základe projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupné viacero modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceny](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rýchly štart SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rýchly štart v štúdiu](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Je potrebné požiadať o prístup vopred](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceny](https://huggingface.co/pricing) | [Prístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podľa nižšie uvedených pokynov na _konfiguráciu_ tohto repozitára pre použitie s rôznymi poskytovateľmi. Úlohy, ktoré vyžadujú konkrétneho poskytovateľa, budú obsahovať jednu z týchto značiek vo svojom názve súboru:
 - `aoai` - vyžaduje Azure OpenAI endpoint, kľúč
 - `oai` - vyžaduje OpenAI endpoint, kľúč
 - `hf` - vyžaduje Hugging Face token

Môžete nakonfigurovať jedného, žiadneho alebo všetkých poskytovateľov. Súvisiace úlohy jednoducho skončia s chybou pri chýbajúcich povereniach.

###  2.1. Vytvorte súbor `.env`

Predpokladáme, že ste si už prečítali vyššie uvedené pokyny a zaregistrovali sa u príslušného poskytovateľa a získali potrebné autentifikačné poverenia (API_KEY alebo token). V prípade Azure OpenAI predpokladáme, že máte tiež platné nasadenie služby Azure OpenAI (endpoint) s nasadeným aspoň jedným GPT modelom pre dokončenie chatu.

Ďalším krokom je nakonfigurovať vaše **lokálne premenné prostredia** nasledovne:

1. Pozrite sa do koreňového priečinka na súbor `.env.copy`, ktorý by mal obsahovať niečo takéto:

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

2. Skopírujte tento súbor do `.env` pomocou nižšie uvedeného príkazu. Tento súbor je _gitignore-d_, čím sa tajomstvá uchovávajú v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly na pravej strane `=`) podľa popisu v nasledujúcej časti.

3. (Voliteľné) Ak používate GitHub Codespaces, máte možnosť uložiť premenné prostredia ako _tajomstvá Codespaces_ spojené s týmto repozitárom. V takom prípade nebudete potrebovať nastaviť lokálny súbor .env. **Avšak, všimnite si, že táto možnosť funguje iba ak používate GitHub Codespaces.** Budete stále potrebovať nastaviť súbor .env, ak používate Docker Desktop.

### 2.2. Naplňte súbor `.env`

Pozrime sa rýchlo na názvy premenných, aby sme pochopili, čo predstavujú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je užívateľský prístupový token, ktorý ste nastavili vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč pre používanie služby pre non-Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč pre používanie tej služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený endpoint pre Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasadenia modelu _generovania textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasadenia modelu _embeddingov textu_ |
| | |

Poznámka: Posledné dve premenné Azure OpenAI odrážajú predvolený model pre dokončenie chatu (generovanie textu) a vyhľadávanie vektorov (embeddingy) zodpovedajúco. Pokyny na ich nastavenie budú definované v príslušných úlohách.

### 2.3 Konfigurácia Azure: Z portálu

Hodnoty endpointu a kľúča Azure OpenAI nájdete v [Azure Portáli](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), takže začnime tam.

1. Prejdite na [Azure Portál](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Keys and Endpoint** v bočnom paneli (menu vľavo).
1. Kliknite na **Show Keys** - mali by ste vidieť nasledujúce: KEY 1, KEY 2 a Endpoint.
1. Použite hodnotu KEY 1 pre AZURE_OPENAI_API_KEY
1. Použite hodnotu Endpoint pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme endpointy pre konkrétne modely, ktoré sme nasadili.

1. Kliknite na možnosť **Model deployments** v bočnom paneli (menu vľavo) pre zdroj Azure OpenAI.
1. Na cieľovej stránke kliknite na **Manage Deployments**

To vás zavedie na webovú stránku Azure OpenAI Studio, kde nájdeme ďalšie hodnoty, ako je opísané nižšie.

### 2.4 Konfigurácia Azure: Zo štúdia

1. Prejdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **zo svojho zdroja** ako je opísané vyššie.
1. Kliknite na kartu **Deployments** (bočný panel, vľavo) na zobrazenie aktuálne nasadených modelov.
1. Ak váš požadovaný model nie je nasadený, použite **Create new deployment** na jeho nasadenie.
1. Budete potrebovať model _generovania textu_ - odporúčame: **gpt-35-turbo**
1. Budete potrebovať model _embeddingov textu_ - odporúčame **text-embedding-ada-002**

Teraz aktualizujte premenné prostredia, aby odrážali _Deployment name_ použitý. Toto bude typicky rovnaké ako názov modelu, pokiaľ ste ho výslovne nezmenili. Takže, ako príklad, môžete mať:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezabudnite uložiť súbor .env po dokončení**. Teraz môžete opustiť súbor a vrátiť sa k pokynom na spustenie notebooku.

### 2.5 Konfigurácia OpenAI: Z profilu

Váš OpenAI API kľúč nájdete vo vašom [OpenAI účte](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ho nemáte, môžete sa zaregistrovať na účet a vytvoriť API kľúč. Akonáhle máte kľúč, môžete ho použiť na vyplnenie premennej `OPENAI_API_KEY` v súbore `.env`.

### 2.6 Konfigurácia Hugging Face: Z profilu

Váš Hugging Face token nájdete vo vašom profile pod [Prístupovými tokenmi](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Neposielajte ani nezdieľajte ich verejne. Namiesto toho vytvorte nový token pre tento projekt a skopírujte ho do súboru `.env` pod premennú `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to nie je API kľúč, ale používa sa na autentifikáciu, takže túto názvoslovnú konvenciu zachovávame pre konzistenciu.

**Upozornenie**:  
Tento dokument bol preložený pomocou služby pre automatizovaný preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.