# Zoznam zmien

Všetky významné zmeny v učebnom pláne Generatívnej AI pre začiatočníkov sú zdokumentované v tomto súbore.

Formát je založený na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Keďže ide o
učebný plán a nie o verzovaný softvérový balík, záznamy sú zoskupené podľa dátumu.

## [2026-07-16] — Validácia obsahu + Obrázkové zdroje lekcie 09

### Zmenené

- **Lekcia 10 (low-code AI aplikácie):** aktualizované dva vyradené odkazy `docs.microsoft.com/powerapps/...` Dataverse
  na aktuálne `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (overené online).
- **Lekcia 17 (AI agenti):** modernizovaný zastaraný príklad modelu (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) a meno náhradného nasadenia v ukážke Agent Frameworku
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** pridané chýbajúce sledovacie ID `?WT.mc_id=academic-105485-koreyst` k
  odkazu *Microsoft for Startups*.
- **Obrázkové zdroje lekcie 09** regenerované pomocou modelu `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, a
  `images/startup.png` (pred/po pár príkladu editácie bol vytvorený pomocou reálneho
  volania `client.images.edit` s generovanou maskou).

### Validované

- Overené README pre lekcie 01, 03, 05, 12, 14, a 16 — všetky aktuálne (správne pomenovanie a odkazy Microsoft Foundry);
  zmeny neboli potrebné.
- Vykonaná kompletná validácia markdownu vo všetkých 41 markdown súboroch v repozitári (okrem prekladov) na
  zastarané cesty k dokumentom, `/en-us/` lokalizácie Microsoftu, zastarané názvy produktov/modelov, chýbajúce sledovacie
  ID a nefunkčné relatívne odkazy/obrázky. Jediný medzera v sledovacom ID pre *Microsoft for Startups* bola
  riešiteľná; všetky ostatné upozornenia boli potvrdené ako falošné poplachy (automaticky generované prekladové odkazy,
  zakomentované zástupné symboly a štrukturálne URL tretích strán `/en/`).

## [2026-07-15] — Lekcia 09 (Aplikácie s obrázkami) Prepis pre GPT obrazové modely

### Zmeny

- **Prepísaná lekcia 09 "Budovanie aplikácií na generovanie obrázkov"** okolo aktuálneho **`gpt-image`**
  rodina modelov (predvolený **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` tiež GA), nahrádzajúca
  starší obsah DALL·E 2/3. Kľúčové opravy:
  - Modely `gpt-image` vracajú obrázok ako **base64 (`b64_json`)**, nie URL. Aktualizované všetky príklady tak,
    aby používali `base64.b64decode(...)` namiesto sťahovania `url` cez `requests`.
  - Zvýšená verzia obrazového API na `2025-04-01-preview`.
  - Nahradená vymyslená sekcia "temperature" (obrazové modely neberú `temperature`) a obsah DALL·E-2 výhradne
    pre obrazové **variácie** sekciou o **úpravách obrázkov** (maskovanie/inpainting).
  - Aktualizované `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, obe
    pracovné zošity pre zadania (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), a .NET `.dib` zošit.

### Odstránené

- Vymazané zastarané príklady `python/aoai-app-variation.py` a `python/oai-app-variation.py`
  (`images.create_variation` je DALL·E-2 výhradne a nepodporovaný v `gpt-image`).
- Vymazané 4 opustené obrázkové zdroje viazané na odstránenú sekciu porovnania teplôt
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Odstránená zbytočná závislosť `requests` z Python príkladov a požiadaviek lekcie.

### Validované

- Spustené `aoai-app.py` od začiatku do konca na nasadenom modeli `gpt-image-1.5` a potvrdené, že base64
  dekódovanie/uloženie vytvára PNG. Zošity potvrdené ako platný JSON.

## [2026-07-14] — Aktualizácia predvoleného modelu + Usmernenie pre model odvodzovania

### Zmenené

- **Predvolený chat model `gpt-4o-mini` → `gpt-5-mini`** v celom učebnom pláne vrátane spustiteľných príkladov,
  dokumentácie a konfigurácie. Toto bolo motivované stavom životného cyklu modelu: na Microsoft Foundry,
  `gpt-4o-mini` (ukončenie 2026-10-01) a celá rodina `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, ukončenie 2026-10-14) sú **v procese zastarania**, zatiaľ čo rodina **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) je všeobecne dostupná** (ukončenie 2027-02-06). Aktualizované:
  - `.env.copy`, `00-course-setup/03-providers.md` (odporúčané nasadenie a `az cognitiveservices`
    príkazy deploy), a README pre lekcie 04, 06, 07 a 15.
  - Python príklady v lekcii 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) a skripty lekcie 08.
  - TypeScript / JavaScript príklady v lekciách 06, 07 a 11 a `.dib` .NET notebooky pre
    lekcie 06 a 07.
  - Notebooky na zadania v lekciách 04, 06, 07 a 11 (kódové bunky), plus `shared/python/api_utils.py`
    príklady docstringov.
- **Pokyny k parametru reasoning-model (nové).** `gpt-5-mini` je *reasoning* model: **nepodporuje**
  `temperature`/`top_p` a používa `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) namiesto `max_tokens`. V dôsledku toho:
  - Odstránené `temperature`/`top_p`/`max_tokens` zo vzorov, ktoré teraz štandardne používajú `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcia 15 RAG README).
  - Pridaná poznámka **"Reasoning models don't use `temperature`"** do lekcie 06, ktorá vysvetľuje, že
    reasoning modely sa riadia **prompt engineering + reasoning controls** namiesto
    sampling ovládačov, zatiaľ čo `temperature`/`top_p` platia pre modely bez reasoning
    (GPT-4.x, Mistral, Llama, Phi, open modely).
- **`gpt-5-mini` sa nepoužíva pre tutoriál jemného doladzovania (lekcia 18).** GPT-5 podporuje
  iba reinforcement fine-tuning (RFT); prehliadka supervised fine-tuningu (SFT) v lekcii 18 zostáva
  `gpt-4.1-mini`, ktorý podporuje SFT/DPO.
- **Ukážky s teplotou používajú model Llama.** Na udržanie vyučovania `temperature` (ktoré odmietajú modely
  odvodzovania), sa používa model `Llama-3.3-70B-Instruct` cez endpoint Foundry Models. Pridaná nová
  premenná `AZURE_INFERENCE_CHAT_MODEL` do `.env.copy`; notebooky lekcie 04/06 `githubmodels` a
  ukážka `06` `js-githubmodels` ju čítajú (s možnosťou návratu k `Llama-3.3-70B-Instruct`) a udržiavajú svoje
  `temperature`/`top_p`/`max_tokens` ukážky.
- **Ukážky JS / .NET aktualizované pre GPT-5.** Z GPT-5 boli odstránené `temperature`/`top_p`/`max_tokens`
  príklady (`06` `recipe-app` TypeScript, `06` `.dib` .NET - čo tiež spôsobuje zvýšenie `MaxOutputTokenCount`
  takže výstup uvažovania nie je orezaný). `06` `js-githubmodels` príklad teraz používa Llama na udržanie svojej
  ukážky teploty. `.dib` uvádza, že `Azure.AI.Inference` + model Llama je cesta, ako
  demonštrovať `Temperature` v .NET.
- Špecifikácia `gpt-4o-mini` / `gpt-5-mini` na mieste, kde zostávajú presné: `tiktoken` token-encoding
  odkazy, zoznamy dostupnosti modelov v katalógu a modely reči z lekcie 02 (`gpt-4o-transcribe`).
- Ukážky z lekcie 20 (Mistral) a 21 (Meta) si ponechávajú `temperature`/`max_tokens`, pretože sú zamerané na
  Mistral/Llama modely, ktoré tieto parametre podporujú.

## [2026-07-06] — Obnova modernizácie obsahu

Rozsiahla obnova, aby bol obsah kurikula presný pre rok 2026: moderné API, aktuálne názvy produktov a
názvy modelov, aktualizované odporúčania poskytovateľov a nové nástroje pre vývojársku skúsenosť.

### Pridané

- Sekcia **Microsoft Agent Framework** v lekcii `17-ai-agents` pokrývajúca jednopoužívateľských chat agentov,
  nástroje/volanie funkcií, konfiguráciu Azure OpenAI (Microsoft Foundry) a orchestráciu pracovných tokov
  viacerých agentov (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** zdokumentovaný ako offline / lokálny poskytovateľ (spolu s Ollama) v
  `00-course-setup/03-providers.md` a lekcii `19-slm`.
- **Workflows kontinuálnej integrácie**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (vynucované na udržiavanom module `shared/`,
    odporúčania pre zvyšok kurikula), kontrola ESLint a pracovná úloha pytest.
  - `.github/workflows/security.yml` — CodeQL analýza (Python + JavaScript/TypeScript) a
    prehliadka závislostí pri pull requestoch.
- **Testovací balík** v rámci `tests/` — 41 pytest testov pokrývajúcich spoločný utilitárny modul.
- **Migračná zručnosť Azure OpenAI → Responses API** pod
  `.github/skills/azure-openai-to-responses/` používaná na usmernenie migrácie API.

### Zmenené

- **Chat Completions API → Responses API** vo všetkých Python a TypeScript chat ukážkach
  (`client.responses.create(...)` → `response.output_text`), vrátane lekcií 04, 06, 07, 11,
  15 a 18, plus ich README súborov.
- **GitHub Models → Microsoft Foundry Models** v celom texte, odkazoch a ukážkach. GitHub Models
  končia ku koncu júla 2026; ukážky teraz odkazujú na katalóg modelov Microsoft Foundry a používajú
  premenné prostredia `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Aktualizované **`.env.copy`, `AGENTS.md` a dokumentácia poskytovateľa** aby odrážala, že Azure OpenAI je teraz súčasťou
  Microsoft Foundry, a predvolená verzia API bola zvýšená na `2024-10-21`.
- **TypeScript ukážky** (lekcie 06, 07, 08, 11) migrované z zastaraného beta SDK `@azure/openai`
  na balík `openai` (chat aplikácie používajú Responses API; vyhľadávacia aplikácia používa
  klienta embeddings).
- **.NET notebooky** (`dotnet/*.dib`) štandardizované na verziu `Azure.AI.OpenAI` **2.1.0**: lekcie 06 a 07
  používajú API `ChatClient`, lekcia 08 používa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), a
  lekcia 09 používa `ImageClient` (`GenerateImage`) s `gpt-image-1`, nahrádzajúc starý
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` z `1.0.0-beta.9`.
- **Modernizácia názvov produktov**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcie 14, 16, 17) a "Bing" → **Microsoft Copilot** (lekcia 12), kde tieto pomenovania odkazovali na
  aktuálne produkty.
- **DevContainer** (`.devcontainer/`) teraz obsahuje rozšírenia Pylance, Black, Ruff, ESLint, Prettier a Copilot,
  povoľuje formátovanie pri ukladaní a inštaluje `ruff`, `black`, `mypy` a `pytest`, aby sa mohli lokálne
  replikovať kontroly CI.
- **Generovanie obrázkov** (lekcia 09) odporúča `gpt-image-1` pre Azure (katalóg Azure odstránil
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** aktualizované tak, aby odrážalo dokončenú prácu (migrácia API, CI,
  DevContainer, testy) a aktuálne fakty (preklady sú generované automaticky pomocou
  Azure Co-op Translator; API asistenta je nahradené API odpovedí).

### Opravené

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` teraz vracia
  prázdny reťazec pre vstup obsahujúci iba medzery namiesto vyvolania chyby "príliš krátky" (konzistentné s
  prípadom `None`). Nájdene a pokryté novou testovacou sadou.
- **Ukážky obrázkov v lekcii 09** — opravené skutočné chyby: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  a premenná, ktorá tieňovala modul `openai`.
- **Blok poznámok lekcie 15 RAG** — opravené nastavenie klienta, nahradený zmazaný `DataFrame.append`
  za `pd.concat` a zmodernizované použitie staršieho SDK.
- Zastarané / vyradené názvy modelov (`gpt-3.5-turbo`, `gpt-35-turbo`) nahradené `gpt-4o-mini`
  v aktívnych ukážkach; historické výsledky doladenia v lekcii 18 boli zachované a označené
  namiesto prepísania.

### Zastarané / Poznámky

- **Ukážky Microsoft Foundry Models**, ktoré používajú `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ukážky `githubmodels-*` a `js-githubmodels` a lekcie 19, 20,
  a 21 zostávajú na Model Inference API, ktoré **nepodporuje** API odpovedí. Tieto sú
  zámerne ponechané na danom SDK.
- `AzureOpenAI()` je zámerne zachovaný tam, kde je to stále vhodné (vkladanie a generovanie obrázkov),
  keďže tieto pracovné postupy nie sú súčasťou migrácie na API odpovedí.
- Referencie `text-embedding-ada-002` sú zachované tam, kde na nich závisí vopred vypočítaný index vkladania.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->