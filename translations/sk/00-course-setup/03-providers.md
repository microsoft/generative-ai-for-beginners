# Výber a konfigurácia poskytovateľa LLM 🔑

Zadania **môžu** byť tiež nastavené tak, aby pracovali s jedným alebo viacerými nasadeniami veľkých jazykových modelov (LLM) cez podporovaného poskytovateľa služieb, ako sú OpenAI, Azure alebo Hugging Face. Tieto poskytujú _hostovaný koncový bod_ (API), ku ktorému môžeme programovo pristupovať s použitím správnych poverení (API kľúč alebo token). V tomto kurze sa venujeme týmto poskytovateľom:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznorodými modelmi vrátane základnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pre OpenAI modely so zameraním na podnikové pripravenie
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) pre jeden koncový bod a API kľúč na prístup k stovkám modelov od OpenAI, Meta, Mistral, Cohere, Microsoft a ďalších (nahrádza GitHub Models, ktoré sa končí na konci júla 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) alebo [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), ak radšej spustíte modely plne offline na svojom vlastnom zariadení bez potreby cloudových služieb

**Na tieto cvičenia budete potrebovať vlastné účty**. Zadania sú voliteľné, takže si môžete nastaviť jedného, všetkých alebo žiadneho poskytovateľa podľa vašich záujmov. Niekoľko rád k registrácii:

| Registrácia | Cena | API kľúč | Playground | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekty](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Viacero dostupných modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Rýchly štart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Rýchly štart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Nutné požiadať o prístup vopred](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cenník](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Stránka prehľadu projektu](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | K dispozícii bezplatná úroveň; jeden koncový bod + kľúč pre viacerých poskytovateľov modelov |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenník](https://huggingface.co/pricing) | [Prístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Zdarma (beží na vašom zariadení) | Nie je potrebné | [Lokálny CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Plne offline, OpenAI-kompatibilný koncový bod |
| | | | | |

Postupujte podľa nasledujúcich pokynov na _konfiguráciu_ tohto repozitára pre použitie s rôznymi poskytovateľmi. Zadania, ktoré vyžadujú konkrétneho poskytovateľa, budú mať v názve súboru jednu z týchto značiek:

- `aoai` - vyžaduje Azure OpenAI koncový bod, kľúč
- `oai` - vyžaduje OpenAI koncový bod, kľúč
- `hf` - vyžaduje Hugging Face token
- `githubmodels` - vyžaduje Microsoft Foundry Models koncový bod, kľúč (GitHub Models končí na konci júla 2026)

Môžete nakonfigurovať jedného, žiadneho alebo všetkých poskytovateľov. Súvisiace zadania jednoducho zlyhajú pri chýbajúcich povereniach.

## Vytvorenie súboru `.env`

Predpokladáme, že ste už čítali vyššie pokyny, zaregistrovali sa u relevantného poskytovateľa a získali požadované autentifikačné poverenia (API_KĽÚČ alebo token). V prípade Azure OpenAI predpokladáme, že máte tiež platné nasadenie služby Azure OpenAI (koncový bod) s aspoň jedným nasadeným GPT modelom pre chatovacie dokončovanie.

Ďalším krokom je nakonfigurovať vaše **miestne premenné prostredia** takto:

1. Pozrite sa do koreňového priečinka na súbor `.env.copy`, ktorý by mal obsahovať niečo takéto:

   ```bash
   # Poskytovateľ OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI v Microsoft Foundry
   ## (Služba Azure OpenAI je teraz súčasťou Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Predvolené je nastavené! (aktuálna stabilná GA verzia API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modely Microsoft Foundry (katalóg modelov viacerých poskytovateľov, nahrádza GitHub Modely, ktoré skončia koncom júla 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopírujte tento súbor do `.env` pomocou nasledujúceho príkazu. Tento súbor je _gitignore-ovaný_, aby boli tajné údaje v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly napravo od `=`) podľa opisu v nasledujúcej sekcii.

4. (Voliteľné) Ak používate GitHub Codespaces, môžete si uložiť premenné prostredia ako _Codespaces tajomstvá_ viazané na tento repozitár. V takom prípade nemusíte nastavovať lokálny súbor .env. **Poznámka: Táto možnosť funguje iba ak používate GitHub Codespaces.** Súbor .env však budete musieť nastaviť, ak používate Docker Desktop.

## Vyplnenie súboru `.env`

Pozrime sa rýchlo na názvy premenných, aby sme pochopili, čo predstavujú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je používateľský prístupový token, ktorý si nastavíte vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč na používanie služby pre ne-Azure OpenAI koncové body |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč na používanie tejto služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený koncový bod pre Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je koncový bod nasadenia _modelu generovania textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je koncový bod nasadenia _modelu textových vektorov (embeddingov)_ |
| AZURE_INFERENCE_ENDPOINT | Toto je koncový bod vášho projektu Microsoft Foundry, používaný pre Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Toto je API kľúč vášho projektu Microsoft Foundry |
| | |

Poznámka: Posledné dve premenné pre Azure OpenAI zodpovedajú predvolenému modelu pre chatové dokončenie (generovanie textu) a vyhľadávanie vektorov (embeddingy). Pokyny na ich nastavenie budú definované v príslušných zadaniach.

## Konfigurácia Azure OpenAI: Z Portálu

> **Poznámka:** Azure OpenAI služba je teraz súčasťou [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Zdroje a nasadenia sa stále zobrazujú v Azure Portáli, ale každodenná správa modelov (nasadenia, playground, monitorovanie) sa teraz vykonáva v portáli Foundry namiesto starej samostatnej aplikácie "Azure OpenAI Studio".

Hodnoty koncového bodu a kľúča Azure OpenAI nájdete v [Azure Portáli](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), tak začnime tam.

1. Choďte do [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Kľúče a koncový bod** v postrannom paneli (menu vľavo).
1. Kliknite na **Zobraziť kľúče** - mali by ste vidieť nasledujúce: KĽÚČ 1, KĽÚČ 2 a Koncový bod.
1. Použite hodnotu KĽÚČ 1 pre AZURE_OPENAI_API_KEY
1. Použite hodnotu Koncového bodu pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme koncové body pre konkrétne modely, ktoré sme nasadili.

1. Kliknite na možnosť **Nasadenia modelov** v postrannom paneli (ľavé menu) pre zdroj Azure OpenAI.
1. Na cieľovej stránke kliknite na **Prejsť do Microsoft Foundry portálu** (alebo **Spravovať nasadenia**, podľa typu vášho zdroja)

Toto vás presmeruje do portálu Microsoft Foundry, kde nájdeme ďalšie hodnoty, ako je popísané nižšie.

## Konfigurácia Azure OpenAI: Z Microsoft Foundry portálu

1. Prejdite na [Microsoft Foundry portál](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **zo svojho zdroja**, ako bolo uvedené vyššie.
1. Kliknite na kartu **Nasadenia** (postranný panel, vľavo) pre zobrazenie aktuálne nasadených modelov.
1. Ak váš želaný model nie je nasadený, použite **Nasadiť model** na jeho nasadenie z [katalógu modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Budete potrebovať _model generovania textu_ – odporúčame: **gpt-4o-mini**
1. Budete potrebovať _model textových embeddingov_ – odporúčame **text-embedding-3-small**

Teraz aktualizujte premenné prostredia tak, aby odrážali použité _meno nasadenia_. Zvyčajne bude rovnaké ako názov modelu, pokiaľ ste ho explicitne nezmenili. Ako príklad môžete mať:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nezabudnite uložiť súbor .env po dokončení**. Súbor môžete teraz zatvoriť a vrátiť sa k pokynom na spustenie notebooku.

## Konfigurácia OpenAI: Z profilu

Váš OpenAI API kľúč nájdete vo svojom [účte OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ho nemáte, zaregistrujte sa a vytvorte si API kľúč. Akonáhle kľúč máte, môžete ho použiť na vyplnenie premennej `OPENAI_API_KEY` v súbore `.env`.

## Konfigurácia Hugging Face: Z profilu

Váš Hugging Face token nájdete vo svojom profile pod [Prístupové tokeny](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezverejňujte ich ani nesdielajte verejne. Namiesto toho vytvorte nový token pre použitie v tomto projekte a skopírujte ho do súboru `.env` do premennej `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to nie je API kľúč, ale používa sa na autentifikáciu, preto si zachovávame túto konvenciu názvu pre konzistenciu.

## Konfigurácia Microsoft Foundry Models: Z portálu

> **Poznámka:** GitHub Models sa končia na konci júla 2026. Microsoft Foundry Models je ich priamou náhradou, ktorá ponúka rovnaký bezplatný katalóg modelov na vyskúšanie a skúsenosť s Azure AI Inference SDK / OpenAI SDK.

1. Choďte na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) a vytvorte (alebo otvorte) Foundry projekt.
1. Prezrite si [katalóg modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) a nasadzujte model, napríklad `gpt-4o-mini`.
1. Na stránke **Prehľad** projektu skopírujte **koncový bod** a **API kľúč**.
1. Použite hodnotu koncového bodu pre `AZURE_INFERENCE_ENDPOINT` a hodnotu kľúča pre `AZURE_INFERENCE_CREDENTIAL` vo vašom súbore `.env`.

## Offline / Lokálni poskytovatelia

Ak radšej nechcete vôbec používať cloudové predplatné, môžete spustiť kompatibilné open modely priamo na vlastnom zariadení:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftov runtime na zariadení. Automaticky vyberá najlepší vykonávací poskytovateľ (NPU, GPU alebo CPU) a vystavuje OpenAI-kompatibilný koncový bod, takže môžete znova použiť väčšinu ukážkového kódu v tomto kurze s minimálnymi zmenami. Pozrite si [dokumentáciu Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) na začiatok, alebo nainštalujte pomocou `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - populárna alternatíva pre lokálne spúšťanie open modelov ako Llama, Phi, Mistral a Gemma.


Pozrite si [Lekciu 19: Budovanie so SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pre praktické príklady použitia oboch možností.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->