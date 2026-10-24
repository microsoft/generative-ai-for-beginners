# Zmeny

Všetky významné zmeny v učebnom pláne Generatívnej AI pre začiatočníkov sú zdokumentované v tomto súbore.

Formát je založený na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Pretože ide o
učebný plán a nie o verzovaný softvérový balíček, zápisy sú zoskupené podľa dátumu.

## [2026-07-16] — Validácia obsahu + obrázkové zdroje lekcie 09

### Zmenené

- **Lekcia 10 (low-code AI aplikácie):** aktualizované dva vyradené odkazy `docs.microsoft.com/powerapps/...` Dataverse
  na aktuálne `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (overené naživo).
- **Lekcia 17 (AI agenti):** modernizovaný zastaralý príklad modelu (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) a zástupný názov nasadenia v ukážke Agent Frameworku
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** pridané chýbajúce sledovacie ID `?WT.mc_id=academic-105485-koreyst` do
  odkazu *Microsoft for Startups*.
- **Obrázkové zdroje lekcie 09** znovu vygenerované pomocou modelu `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` a
  `images/startup.png` (príklad úpravy bol vytvorený skutočným
  volaním `client.images.edit` s generovanou maskou).

### Overené

- Skontrolované README súbory lekcií 01, 03, 05, 12, 14 a 16 — všetky aktuálne (správne pomenovanie Microsoft Foundry
  a odkazy); žiadne zmeny neboli potrebné.
- Spustená kompletná validácia markdownu naprieč všetkými 41 markdown súbormi v repozitári (okrem prekladov)
  na neaktuálne cesty dokumentácie, `/en-us/` Microsoft lokality, zastarané názvy produktov/modelov,
  chýbajúce tracking ID a nefunkčné relatívne odkazy/obrázky. Len chýbajúce tracking-ID v odkaze *Microsoft for Startups* bolo
  relevantné; všetky ostatné hlásenia boli potvrdené ako falošné poplachy (automaticky generované prekladové odkazy,
  zakomentované zástupné miesta a štrukturálne URL tretích strán `/en/`).

## [2026-07-15] — Prepísanie lekcie 09 (Obrázkové aplikácie) pre GPT obrazové modely

### Zmenené

- **Prepísaná lekcia 09 "Vytváranie aplikácií generujúcich obrázky"** okolo aktuálnej rodiny modelov **`gpt-image`**
  (predvolený **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` tiež GA), nahrádzajúca
  starší obsah DALL·E 2/3. Kľúčové opravy:
  - Modely `gpt-image` vracajú obrázok ako **base64 (`b64_json`)**, nie ako URL. Aktualizované všetky ukážky tak, aby používali
    `base64.b64decode(...)` namiesto sťahovania súboru `url` s `requests`.
  - Zvýšená verzia obrázkovej API na `2025-04-01-preview`.
  - Nahradená vymyslená časť s "teplotou" (obrázkové modely nepracujú s `temperature`) a obsah o
    variáciách obrázkov pre DALL·E-2 iba sekciou o **úprave obrázkov** (maskovanie/inpainting).
  - Aktualizované `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    zadávacie poznámkové bloky (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), a .NET `.dib` poznámkový blok.

### Odstránené

- Odstránené zastarané ukážky `python/aoai-app-variation.py` a `python/oai-app-variation.py`
  (`images.create_variation` je len pre DALL·E-2 a nie je podporovaný `gpt-image`).
- Odstránené 4 opustené obrázkové súbory súvisiace s odstránenou sekciou porovnania teplôt
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Odstránená nepotrebná závislosť `requests` z pythonovských ukážok a požiadaviek lekcie.

### Overené

- Spustený `aoai-app.py` od začiatku do konca voči nasadenému modelu `gpt-image-1.5` a potvrdené, že dekódovanie/uloženie base64
  vytvára PNG. Poznámkové bloky potvrdené ako platný JSON.

## [2026-07-14] — Aktualizácia predvoleného modelu + usmernenie k modelu uvažovania

### Zmeny

- **Predvolený chatovací model `gpt-4o-mini` → `gpt-5-mini`** v rámci spustiteľných ukážok kurikula,
  dokumentácie a konfigurácie. Dôvodom bol stav životného cyklu modelu: na Microsoft Foundry,
  `gpt-4o-mini` (ukončenie 2026-10-01) a celá rodina `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, ukončenie 2026-10-14) sú **v procese zastarávania**, zatiaľ čo rodina **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) je všeobecne dostupná** (ukončenie 2027-02-06). Aktualizované:
  - `.env.copy`, `00-course-setup/03-providers.md` (odporúčané nasadenie a `az cognitiveservices`
    príkazy na nasadenie), a README pre lekcie 04, 06, 07 a 15.
  - Python ukážky v lekcii 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) a skripty lekcie 08.
  - TypeScript / JavaScript ukážky v lekciách 06, 07 a 11, a `.dib` .NET poznámkové bloky pre
    lekcie 06 a 07.
  - Zadávacie poznámkové bloky v lekciách 04, 06, 07 a 11 (kódové bunky), plus `shared/python/api_utils.py`
    príklady v docstringoch.
- **Návod k parametrom modelu uvažovania (nové).** `gpt-5-mini` je *model uvažovania*: nepodporuje
  `temperature`/`top_p`, a používa `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) namiesto `max_tokens`. Podľa toho:
  - Odstránené `temperature`/`top_p`/`max_tokens` z príkladov, ktoré teraz štandardne používajú `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcia 15 RAG README).
  - Pridaná poznámka **"Reasoning models nepoužívajú `temperature`"** do lekcie 06, vysvetľujúca, že
    reasoning modely sú riadené pomocou **prompt engineering + reasoning controls** namiesto
    vzorkovacích prvkov, zatiaľ čo `temperature`/`top_p` zostávajú platné pre nemodely na reasoning
    (GPT-4.x, Mistral, Llama, Phi, open models).
- **`gpt-5-mini` sa nevyužíva v návode na doladenie (lekcia 18).** GPT-5 podporuje len
  reinforcement fine-tuning (RFT); prehliadka supervidovaného doladenia (SFT) v lekcii 18 ponecháva
  `gpt-4.1-mini`, ktorá podporuje SFT/DPO.
- **Demonštrácie teploty používajú model Llama.** Aby sa zachovala výučba `temperature` (ktorú reasoning modely
  odmietajú), používa sa model `Llama-3.3-70B-Instruct` cez endpoint Foundry Models. Pridaná nová
  premenná `AZURE_INFERENCE_CHAT_MODEL` do `.env.copy`; notové bloky lekcie 04/06 `githubmodels` a
  príklad `06` `js-githubmodels` ju načítavajú (s návratom na `Llama-3.3-70B-Instruct`) a udržiavajú svoje
  demonštrácie `temperature`/`top_p`/`max_tokens`.
- **Aktualizované príklady JS / .NET pre GPT-5.** Odstránené `temperature`/`top_p`/`max_tokens` z GPT-5
  príkladov (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ktoré tiež riešia `MaxOutputTokenCount`,
  aby výstup reasoning nebol orezaný). Príklad `06` `js-githubmodels` teraz používa Llamu na zachovanie
  demonštrácie teploty. `.dib` poznamenáva, že `Azure.AI.Inference` + model Llama je spôsob,
  ako demonštrovať `Temperature` v .NET.
- Ponechané `gpt-4o-mini` / `gpt-5-mini` tam, kde zostávajú presné: odkazy na kódovanie tokenov `tiktoken`,
  zoznamy dostupnosti v katalógu modelov a modely reči v lekcii 02 (`gpt-4o-transcribe`).
- Príklady z lekcií 20 (Mistral) a 21 (Meta) si ponechávajú `temperature`/`max_tokens`, pretože
  cílili na modely Mistral/Llama, ktoré tieto parametre podporujú.

## [2026-07-06] — Obnovenie modernizácie obsahu

Rozsiahle obnovenie pre zabezpečenie presnosti kurikula pre rok 2026: moderné API, aktuálne názvy produktov a
názvy modelov, aktualizované pokyny pre poskytovateľov a nové nástroje pre skúsenosť vývojára.

### Pridané

- Sekcia **Microsoft Agent Framework** v lekcii `17-ai-agents` pokrývajúca samostatných chat agentov,
  nástroje/volanie funkcií, konfiguráciu Azure OpenAI (Microsoft Foundry) a viacagentovú
  orchestráciu procesu (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** zdokumentované ako offline / zariadením poskytovateľ (vedľa Ollama) v
  `00-course-setup/03-providers.md` a lekcii `19-slm`.
- **Workflows kontinuálnej integrácie**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (vynútené na udržiavanom module `shared/`,
    odporúčané v celom kurikule), aj prehliadka ESLint a job pytest.
  - `.github/workflows/security.yml` — analýza CodeQL (Python + JavaScript/TypeScript) a
    prehľad závislostí pri požiadavkách na zlúčenie.
- **Testovací súbor** pod `tests/` — 41 testov pytest pokrývajúcich zdieľaný modul utilít.
- **Schopnosť migrácie z Azure OpenAI → Responses API** pod
  `.github/skills/azure-openai-to-responses/` použitá na navigáciu migrácie API.

### Zmenené

- **Chat Completions API → Responses API** vo všetkých príkladoch chatu pre Python a TypeScript
  (`client.responses.create(...)` → `response.output_text`), vrátane lekcií 04, 06, 07, 11,
  15 a 18, plus ich README.
- **GitHub Models → Microsoft Foundry Models** v celom texte, odkazoch a príkladoch. GitHub Models
  končí na konci júla 2026; príklady teraz odkazujú na katalóg modelov Microsoft Foundry a používajú
  premenné prostredia `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Aktualizované **`.env.copy`, `AGENTS.md` a dokumentácia poskytovateľa** na odraz toho, že Azure OpenAI je teraz súčasťou
  Microsoft Foundry a predvolená verzia API bola zvýšená na `2024-10-21`.
- **TypeScript príklady** (lekcie 06, 07, 08, 11) presunuté z zastaralého beta SDK `@azure/openai`
  na balík `openai` (chat aplikácie používajú Responses API; vyhľadávacia aplikácia používa
  embedding klienta).
- **.NET notebočky** (`dotnet/*.dib`) štandardizované na verzio `Azure.AI.OpenAI` **2.1.0**: lekcie 06 a 07
  používajú API `ChatClient`, lekcia 08 používa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), a
  lekcia 09 používa `ImageClient` (`GenerateImage`) s `gpt-image-1`, nahrádzajúc dedičné
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` z `1.0.0-beta.9`.
- **Modernizácia názvov produktov**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcie 14, 16, 17) a "Bing" → **Microsoft Copilot** (lekcia 12), kde sa tieto vzťahujú na
  aktuálne produkty.
- **DevContainer** (`.devcontainer/`) teraz obsahuje rozšírenia Pylance, Black, Ruff, ESLint, Prettier a Copilot,
  zapína formátovanie pri ukladaní a inštaluje `ruff`, `black`, `mypy` a `pytest`, aby bolo možné testy CI
  reprodukovať lokálne.
- **Generovanie obrazov** (lekcia 09) odporúča `gpt-image-1` pre Azure (Azure katalóg odstránil
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** aktualizované tak, aby odrážalo dokončenú prácu (migrácia API, CI,
  DevContainer, testy) a aktuálne fakty (preklady sú automaticky generované prostredníctvom
  Azure Co-op Translator; Assistants API bolo nahradené Responses API).

### Opravené

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` teraz vracia
  prázdny reťazec pre vstup pozostávajúci iba z medzier namiesto vyvolania chyby „príliš krátky“ (v súlade s prípadom
  `None`). Nájdnuté a pokryté novou testovacou sadou.
- **Vzorové obrázky zo lekcie 09** — opravené skutočné chyby: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  a premenná, ktorá zatienila modul `openai`.
- **Zápisník RAG z lekcie 15** — opravené nastavenie klienta, nahradená odstránená `DataFrame.append`
  s `pd.concat` a modernizované použitie starého SDK.
- Zastaralé / vyradené názvy modelov (`gpt-3.5-turbo`, `gpt-35-turbo`) nahradené `gpt-4o-mini`
  v aktívnych príkladoch; historické výstupy jemného ladenia v lekcii 18 boli zachované a anotované
  namiesto prepísania.

### Zastaralé / Poznámky

- **Príklady modelov Microsoft Foundry** používajúce `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — príklady `githubmodels-*` a `js-githubmodels` a lekcie 19, 20,
  a 21 — zostávajú na Model Inference API, ktoré **nepodporuje** Responses API. Tieto zostávajú
  zámerne na tomto SDK.
- `AzureOpenAI()` je zámerne zachované tam, kde je stále vhodné (embeddingy a generovanie obrázkov),
  pretože tieto pracovné postupy nie sú súčasťou migrácie na Responses API.
- Odkazy `text-embedding-ada-002` sú zachované tam, kde od nich závisí predpočítaný index embeddingov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->