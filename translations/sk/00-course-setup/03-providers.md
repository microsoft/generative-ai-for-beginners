<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T16:53:29+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sk"
}
-->
# Výber a konfigurácia poskytovateľa LLM 🔑

Úlohy **môžu** byť tiež nastavené tak, aby pracovali s jedným alebo viacerými nasadeniami veľkých jazykových modelov (LLM) prostredníctvom podporovaného poskytovateľa služieb ako OpenAI, Azure alebo Hugging Face. Tieto poskytujú _hostovaný endpoint_ (API), ku ktorému môžeme programovo pristupovať s príslušnými povereniami (API kľúč alebo token). V tomto kurze sa venujeme týmto poskytovateľom:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznymi modelmi vrátane základnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pre modely OpenAI so zameraním na pripravenosť pre podniky
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a inference server

**Pre tieto cvičenia budete potrebovať vlastné účty**. Úlohy sú voliteľné, takže si môžete vybrať nastavenie jedného, všetkých alebo žiadneho z poskytovateľov podľa svojich záujmov. Niekoľko rád pre registráciu:

| Registrácia | Cena | API kľúč | Playground | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na základe projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Viacero dostupných modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rýchly štart SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rýchly štart Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Nutné požiadať o prístup vopred](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenník](https://huggingface.co/pricing) | [Prístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podľa nižšie uvedených pokynov na _konfiguráciu_ tohto repozitára pre použitie s rôznymi poskytovateľmi. Úlohy, ktoré vyžadujú konkrétneho poskytovateľa, budú mať v názve súboru jednu z týchto značiek:

- `aoai` - vyžaduje Azure OpenAI endpoint, kľúč
- `oai` - vyžaduje OpenAI endpoint, kľúč
- `hf` - vyžaduje Hugging Face token

Môžete nakonfigurovať jedného, žiadneho alebo všetkých poskytovateľov. Súvisiace úlohy jednoducho zlyhajú pri chýbajúcich povereniach.

## Vytvorenie súboru `.env`

Predpokladáme, že ste si už prečítali vyššie uvedené pokyny, zaregistrovali sa u príslušného poskytovateľa a získali potrebné autentifikačné poverenia (API_KEY alebo token). V prípade Azure OpenAI predpokladáme, že máte tiež platné nasadenie služby Azure OpenAI (endpoint) s aspoň jedným GPT modelom nasadeným pre chatovacie dokončenie.

Ďalším krokom je nastavenie vašich **lokálnych premenných prostredia** nasledovne:

1. Pozrite sa v koreňovom priečinku na súbor `.env.copy`, ktorý by mal obsahovať niečo takéto:

   ```bash
   # Poskytovateľ OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Predvolené je nastavené!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopírujte tento súbor do `.env` pomocou nasledujúceho príkazu. Tento súbor je _gitignore-ovaný_, aby boli tajomstvá v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly napravo od `=`) podľa popisu v nasledujúcej sekcii.

4. (Voliteľné) Ak používate GitHub Codespaces, máte možnosť uložiť premenné prostredia ako _Codespaces secrets_ priradené k tomuto repozitáru. V takom prípade nebudete musieť nastavovať lokálny súbor .env. **Avšak, táto možnosť funguje iba ak používate GitHub Codespaces.** Ak používate Docker Desktop, stále budete musieť nastaviť súbor .env.

## Vyplnenie súboru `.env`

Pozrime sa rýchlo na názvy premenných, aby sme pochopili, čo predstavujú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je používateľský prístupový token, ktorý ste nastavili vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč pre používanie služby mimo Azure OpenAI endpointov |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč pre používanie tejto služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený endpoint pre Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasadenia modelu pre _generovanie textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasadenia modelu pre _textové vektory (embeddings)_ |
| | |

Poznámka: Posledné dve premenné Azure OpenAI odrážajú predvolený model pre chatovacie dokončenie (generovanie textu) a vyhľadávanie vektorov (embeddings). Pokyny na ich nastavenie budú definované v príslušných úlohách.

## Konfigurácia Azure: z portálu

Hodnoty endpointu a kľúča Azure OpenAI nájdete v [Azure Portáli](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začnime teda tam.

1. Prejdite na [Azure Portál](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Kľúče a endpoint** v bočnom paneli (menu vľavo).
1. Kliknite na **Zobraziť kľúče** - mali by ste vidieť: KĽÚČ 1, KĽÚČ 2 a Endpoint.
1. Použite hodnotu KĽÚČ 1 pre AZURE_OPENAI_API_KEY
1. Použite hodnotu Endpoint pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme endpointy pre konkrétne modely, ktoré sme nasadili.

1. Kliknite na možnosť **Nasadenia modelov** v bočnom paneli (ľavé menu) pre Azure OpenAI zdroj.
1. Na cieľovej stránke kliknite na **Spravovať nasadenia**

Tým sa dostanete na web Azure OpenAI Studio, kde nájdeme ďalšie hodnoty, ako je popísané nižšie.

## Konfigurácia Azure: zo Studio

1. Prejdite na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **zo svojho zdroja** podľa vyššie uvedeného postupu.
1. Kliknite na záložku **Nasadenia** (bočný panel, vľavo) pre zobrazenie aktuálne nasadených modelov.
1. Ak váš požadovaný model nie je nasadený, použite **Vytvoriť nové nasadenie** na jeho nasadenie.
1. Budete potrebovať model _text-generation_ - odporúčame: **gpt-35-turbo**
1. Budete potrebovať model _text-embedding_ - odporúčame **text-embedding-ada-002**

Teraz aktualizujte premenné prostredia tak, aby odrážali použité _Meno nasadenia_. Zvyčajne to bude rovnaké ako názov modelu, pokiaľ ste ho explicitne nezmenili. Napríklad môžete mať:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezabudnite uložiť súbor .env po dokončení**. Teraz môžete súbor zatvoriť a vrátiť sa k pokynom na spustenie notebooku.

## Konfigurácia OpenAI: z profilu

Váš OpenAI API kľúč nájdete vo svojom [OpenAI účte](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ho ešte nemáte, môžete si vytvoriť účet a vygenerovať API kľúč. Po získaní kľúča ho môžete použiť na vyplnenie premennej `OPENAI_API_KEY` v súbore `.env`.

## Konfigurácia Hugging Face: z profilu

Váš Hugging Face token nájdete vo svojom profile pod [Prístupové tokeny](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezverejňujte ich ani nezdieľajte verejne. Namiesto toho si vytvorte nový token pre použitie v tomto projekte a skopírujte ho do súboru `.env` pod premennú `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to nie je API kľúč, ale používa sa na autentifikáciu, preto zachovávame toto pomenovanie pre konzistenciu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->