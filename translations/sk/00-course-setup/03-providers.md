# Výber a konfigurácia poskytovateľa LLM 🔑

Zadania **môžu** byť tiež nastavené na prácu s jedným alebo viacerými nasadeniami veľkých jazykových modelov (LLM) prostredníctvom podporovaného poskytovateľa služieb ako OpenAI, Azure alebo Hugging Face. Títo poskytujú _hostovaný koncový bod_ (API), ku ktorému máme programový prístup s príslušnými povereniami (API kľúč alebo token). V tomto kurze rozoberáme týchto poskytovateľov:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznymi modelmi vrátane základnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) pre modely OpenAI so zameraním na podnikové nasadenie
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) s jedným koncovým bodom a API kľúčom na prístup k stovkám modelov od OpenAI, Meta, Mistral, Cohere, Microsoft a ďalších (nahrádza GitHub Models, ktoré končia koncom júla 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) alebo [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), ak by ste radšej spúšťali modely úplne offline na vlastnom zariadení bez potreby cloudového predplatného

**Na tieto cvičenia budete potrebovať vlastné účty**. Zadania sú nepovinné, takže si môžete vybrať nastavenie jedného, všetkých alebo žiadneho z poskytovateľov podľa záujmu. Niekoľko tipov na registráciu:

| Registrácia | Cena | API kľúč | Playground | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektové](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Viacero dostupných modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rýchly štart SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rýchly štart Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Pred prístupom sa treba zaregistrovať](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cenník](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Prehľad projektu](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | K dispozícii bezplatná úroveň; jeden endpoint + kľúč pre viacerých poskytovateľov modelov |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenník](https://huggingface.co/pricing) | [Prístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzený počet modelov](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Zdarma (beží na vašom zariadení) | Nie je potrebný | [Lokálne CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Úplne offline, OpenAI-kompatibilný endpoint |
| | | | | |

Postupujte podľa nižšie uvedených pokynov, ako _konfigurovať_ tento repozitár na používanie rôznych poskytovateľov. Zadania, ktoré vyžadujú konkrétneho poskytovateľa, budú mať v názve súboru niektorý z týchto tagov:

- `aoai` - vyžaduje Azure OpenAI endpoint a kľúč
- `oai` - vyžaduje OpenAI endpoint a kľúč
- `hf` - vyžaduje Hugging Face token
- `githubmodels` - vyžaduje Microsoft Foundry Models endpoint a kľúč (GitHub Models končí koncom júla 2026)

Môžete nakonfigurovať jedného, žiadneho alebo všetkých poskytovateľov. Súvisiace zadania sa jednoducho ukážu chybou pri chýbajúcich povereniach.

## Vytvorte súbor `.env`

Predpokladáme, že ste si už prečítali vyššie uvedené pokyny, zaregistrovali sa u príslušného poskytovateľa a získali potrebné autentifikačné poverenia (API_KEY alebo token). V prípade Azure OpenAI predpokladáme, že máte taktiež platné nasadenie služby Azure OpenAI (endpoint) s aspoň jedným GPT modelom nasadeným pre chat completion.

Ďalším krokom je nakonfigurovať **lokálne premenné prostredia** nasledovne:

1. Nájdite v koreňovom adresári súbor `.env.copy`, ktorý by mal obsahovať niečo takéto:

   ```bash
   # Poskytovateľ OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI v Microsoft Foundry
   ## (Služba Azure OpenAI je teraz súčasťou Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Predvolené je nastavené! (aktuálna stabilná verzia GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modely Microsoft Foundry (katalóg modelov viacerých poskytovateľov, nahrádza GitHub Modely, ktoré sa ukončia koncom júla 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopírujte tento súbor do `.env` pomocou príkazu nižšie. Tento súbor je _gitignore-ovaný_, takže tajomstvá sú v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly vpravo od `=`) ako je popísané v nasledujúcej sekcii.

4. (Voliteľné) Ak používate GitHub Codespaces, môžete si uložiť premenné prostredia ako _Codespaces secrets_ priradené k tomuto repozitáru. V takom prípade nemusíte nastavovať lokálny .env súbor. **Táto možnosť však funguje iba pri používaní GitHub Codespaces.** Ak používate Docker Desktop, budete musieť .env súbor nastaviť.

## Vyplnenie súboru `.env`

Pozrime sa stručne na názvy premenných, aby sme pochopili, čo znamenajú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je používateľský prístupový token, ktorý si nastavíte vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč na používanie služby pre ne-Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč na používanie tejto služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený endpoint pre Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasadenia modelu _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasadenia modelu _text embeddings_ |
| AZURE_INFERENCE_ENDPOINT | Toto je endpoint pre váš Microsoft Foundry projekt, používa sa pre Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Toto je API kľúč pre váš Microsoft Foundry projekt |
| | |

Poznámka: Posledné dve premenné Azure OpenAI zodpovedajú predvolenému modelu pre chat completion (text generation) a vyhľadávaniu vektorov (embeddings). Pokyny na ich nastavenie budú súčasťou príslušných zadaní.

## Konfigurácia Azure OpenAI: cez portál

> **Poznámka:** Služba Azure OpenAI je teraz súčasťou [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Zdroje a nasadenia sa stále zobrazujú v Azure Porte, ale každodenná správa modelov (nasadenia, playground, monitoring) prebieha teraz v Foundry portáli namiesto starého samostatného "Azure OpenAI Studio".

Hodnoty endpointu a kľúča Azure OpenAI nájdete v [Azure Porte](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začnime teda tam.

1. Choďte do [Azure portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Kľúče a endpointy** v bočnom paneli (menu vľavo).
1. Kliknite na **Zobraziť kľúče** - mali by ste vidieť nasledujúce: KĽÚČ 1, KĽÚČ 2 a Endpoint.
1. Použite hodnotu KĽÚČA 1 pre AZURE_OPENAI_API_KEY
1. Použite hodnotu Endpoint pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme endpointy pre konkrétne modely, ktoré sme nasadili.

1. Kliknite na možnosť **Nasadenia modelu** v bočnom paneli (ľavé menu) pre Azure OpenAI zdroj.
1. Na cieľovej stránke kliknite na **Prejsť do Microsoft Foundry portálu** (alebo **Spravovať nasadenia**, podľa typu vášho zdroja)

Tým sa dostanete do Microsoft Foundry portálu, kde nájdeme ďalšie hodnoty podľa popisu nižšie.

## Konfigurácia Azure OpenAI: cez Microsoft Foundry portál

1. Prejdite do [Microsoft Foundry portálu](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **z vášho zdroja** ako sme uviedli vyššie.
1. Kliknite na záložku **Nasadenia** (bočný panel vľavo) a zobrazte aktuálne nasadené modely.
1. Ak váš žiadaný model nie je nasadený, použite **Deploy model** na nasadenie z [katalógu modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Budete potrebovať model _text-generation_ - odporúčame: **gpt-5-mini**
1. Budete potrebovať model _text-embedding_ - odporúčame **text-embedding-3-small**

Teraz aktualizujte premenné prostredia tak, aby odrážali používateľom definovaný _Názov nasadenia_. Typicky je to rovnaké ako názov modelu, pokiaľ ste ho výslovne nezmenili. Príklad môže vyzerať takto:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nezabudnite uložiť .env súbor po dokončení**. Teraz môžete súbor zavrieť a vrátiť sa k pokynom na spustenie poznámkového bloku.

## Konfigurácia OpenAI: z profilu

Váš OpenAI API kľúč nájdete vo vašom [OpenAI účte](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ešte nemáte účet, môžete sa zaregistrovať a vytvoriť API kľúč. Keď budete mať kľúč, môžete ho použiť na vyplnenie premennej `OPENAI_API_KEY` v `.env` súbore.

## Konfigurácia Hugging Face: z profilu

Váš token Hugging Face nájdete v profile pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezverejňujte ich ani nezdieľajte verejne. Namiesto toho vytvorte nový token pre použitie v tomto projekte a skopírujte ho do `.env` súboru pod premennú `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky nejde o API kľúč, ale používa sa na autentifikáciu, preto držíme túto pomenovaciu konvenciu pre konzistentnosť.

## Konfigurácia Microsoft Foundry Models: cez portál

> **Poznámka:** GitHub Models končí koncom júla 2026. Microsoft Foundry Models je jeho priamym nástupcom, ktorý ponúka rovnaký katalóg modelov na bezplatné skúšanie a skúsenosť s Azure AI Inference SDK / OpenAI SDK.

1. Prejdite na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) a vytvorte (alebo otvorte) Foundry projekt.
1. Prezrite si [katalóg modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) a nasadte model, napríklad `gpt-5-mini`.
1. Na stránke projektu **Prehľad** skopírujte **endpoint** a **API kľúč**.
1. Použite hodnotu endpointu ako `AZURE_INFERENCE_ENDPOINT` a hodnotu kľúča ako `AZURE_INFERENCE_CREDENTIAL` vo vašom `.env` súbore.

## Offline / lokálni poskytovatelia

Ak nechcete vôbec používať cloudové predplatné, môžete spúšťať kompatibilné open modely priamo na vlastnom zariadení:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftov runtime na zariadení. Automaticky vyberá najlepší výkonový poskytovateľ (NPU, GPU alebo CPU) a poskytuje OpenAI-kompatibilný endpoint, takže väčšinu ukážkového kódu z tohto kurzu môžete znovu použiť s minimálnymi zmenami. Viac nájdete v [Foundry Local dokumentácii](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) alebo si ho nainštalujte cez `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - populárna alternatíva na spúšťanie open modelov ako Llama, Phi, Mistral a Gemma lokálne.


Pozrite si [Lekcia 19: Stavba so SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pre praktické príklady použitia oboch možností.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->