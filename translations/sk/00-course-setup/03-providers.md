<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:03:59+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sk"
}
-->
# Výber a nastavenie poskytovateľa LLM 🔑

Úlohy **môžu** byť nastavené tak, aby fungovali s jedným alebo viacerými nasadeniami Large Language Model (LLM) cez podporovaného poskytovateľa služieb, ako je OpenAI, Azure alebo Hugging Face. Títo poskytovatelia ponúkajú _hostovaný endpoint_ (API), ku ktorému sa dá pristupovať programovo s použitím správnych prihlasovacích údajov (API kľúč alebo token). V tomto kurze sa venujeme týmto poskytovateľom:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s rôznymi modelmi vrátane hlavnej série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pre OpenAI modely s dôrazom na podnikové využitie
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pre open-source modely a inference server

**Na tieto cvičenia budete potrebovať vlastné účty.** Úlohy sú voliteľné, takže si môžete nastaviť jedného, všetkých – alebo žiadneho – poskytovateľa podľa vlastného záujmu. Tu je niekoľko tipov k registrácii:

| Registrácia | Cena | API kľúč | Playground | Komentáre |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cenník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Podľa projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | K dispozícii viacero modelov |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cenník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Je potrebné požiadať o prístup vopred](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cenník](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má obmedzený počet modelov](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podľa pokynov nižšie na _nastavenie_ tohto repozitára pre použitie s rôznymi poskytovateľmi. Úlohy, ktoré vyžadujú konkrétneho poskytovateľa, budú mať v názve súboru jeden z týchto tagov:

- `aoai` - vyžaduje Azure OpenAI endpoint, kľúč
- `oai` - vyžaduje OpenAI endpoint, kľúč
- `hf` - vyžaduje Hugging Face token

Môžete nastaviť jedného, žiadneho alebo všetkých poskytovateľov. Súvisiace úlohy jednoducho zlyhajú, ak chýbajú prihlasovacie údaje.

## Vytvorenie súboru `.env`

Predpokladáme, že ste si už prečítali vyššie uvedené pokyny, zaregistrovali sa u relevantného poskytovateľa a získali potrebné autentifikačné údaje (API_KEY alebo token). V prípade Azure OpenAI predpokladáme, že máte aj platné nasadenie služby Azure OpenAI (endpoint) s aspoň jedným GPT modelom nasadeným pre chat completion.

Ďalším krokom je nastavenie **lokálnych environmentálnych premenných** nasledovne:

1. V koreňovom adresári vyhľadajte súbor `.env.copy`, ktorý by mal obsahovať niečo takéto:

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

2. Skopírujte tento súbor na `.env` pomocou nasledujúceho príkazu. Tento súbor je _gitignore-d_, takže vaše tajné údaje zostanú v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Doplňte hodnoty (nahraďte zástupné znaky na pravej strane `=`) podľa popisu v ďalšej sekcii.

4. (Voliteľné) Ak používate GitHub Codespaces, máte možnosť uložiť environmentálne premenné ako _Codespaces secrets_ priradené k tomuto repozitáru. V takom prípade nemusíte nastavovať lokálny .env súbor. **Upozornenie: Táto možnosť funguje len ak používate GitHub Codespaces.** Ak používate Docker Desktop, .env súbor musíte nastaviť aj tak.

## Vyplnenie súboru `.env`

Pozrime sa rýchlo na názvy premenných, aby sme pochopili, čo znamenajú:

| Premenná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je užívateľský access token, ktorý ste si nastavili vo svojom profile |
| OPENAI_API_KEY | Toto je autorizačný kľúč na používanie služby pre ne-Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizačný kľúč na používanie tejto služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasadený endpoint pre Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasadenia modelu na _generovanie textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasadenia modelu na _textové embeddingy_ |
| | |

Poznámka: Posledné dve Azure OpenAI premenné odrážajú predvolený model pre chat completion (generovanie textu) a vektorové vyhľadávanie (embeddingy). Pokyny na ich nastavenie budú uvedené v príslušných úlohách.

## Nastavenie Azure: Cez Portal

Hodnoty endpointu a kľúča pre Azure OpenAI nájdete v [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), takže začnime tam.

1. Prejdite na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknite na možnosť **Keys and Endpoint** v bočnom paneli (menu vľavo).
1. Kliknite na **Show Keys** – mali by ste vidieť: KEY 1, KEY 2 a Endpoint.
1. Hodnotu KEY 1 použite pre AZURE_OPENAI_API_KEY
1. Hodnotu Endpoint použite pre AZURE_OPENAI_ENDPOINT

Ďalej potrebujeme endpointy pre konkrétne modely, ktoré ste nasadili.

1. Kliknite na možnosť **Model deployments** v bočnom paneli (menu vľavo) pre Azure OpenAI resource.
1. Na cieľovej stránke kliknite na **Manage Deployments**

Tým sa dostanete na web Azure OpenAI Studio, kde nájdete ďalšie hodnoty podľa popisu nižšie.

## Nastavenie Azure: Cez Studio

1. Prejdite do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **zo svojho resource** podľa vyššie uvedeného postupu.
1. Kliknite na záložku **Deployments** (bočný panel vľavo), kde uvidíte aktuálne nasadené modely.
1. Ak požadovaný model nie je nasadený, použite **Create new deployment** na jeho nasadenie.
1. Potrebujete model na _generovanie textu_ – odporúčame: **gpt-35-turbo**
1. Potrebujete model na _embeddingy textu_ – odporúčame **text-embedding-ada-002**

Teraz aktualizujte environmentálne premenné podľa názvu _Deployment name_, ktorý ste použili. Ten je zvyčajne rovnaký ako názov modelu, pokiaľ ste ho výslovne nezmenili. Napríklad môžete mať:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezabudnite súbor .env po úpravách uložiť.** Teraz môžete súbor zatvoriť a pokračovať podľa inštrukcií na spustenie notebooku.

## Nastavenie OpenAI: Cez Profil

Váš OpenAI API kľúč nájdete vo svojom [OpenAI účte](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ak ho nemáte, zaregistrujte si účet a vytvorte API kľúč. Keď ho získate, použite ho na vyplnenie premennej `OPENAI_API_KEY` v súbore `.env`.

## Nastavenie Hugging Face: Cez Profil

Váš Hugging Face token nájdete vo svojom profile v sekcii [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nikdy ich nezverejňujte ani nezdieľajte. Vytvorte si nový token pre tento projekt a skopírujte ho do súboru `.env` pod premennú `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky nejde o API kľúč, ale používa sa na autentifikáciu, takže zachovávame tento názov pre konzistenciu.

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.