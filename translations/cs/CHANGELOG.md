# Změny

Veškeré důležité změny v učebním plánu Generativní AI pro začátečníky jsou zdokumentovány v tomto souboru.

Formát je založen na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Protože se jedná o
učební plán, nikoliv o verzovaný softwarový balíček, položky jsou seskupeny podle data.

## [2026-07-16] — Validace obsahu + obrázkové zdroje ve lekci 09

### Změněno

- **Lekce 10 (low-code AI aplikace):** aktualizovány dva neaktivní odkazy `docs.microsoft.com/powerapps/...` Dataverse
  na aktuální `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (ověřeno živě).
- **Lekce 17 (AI agenti):** modernizován zastaralý příklad modelu (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) a jméno zástupného nasazení ve vzorci Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** přidáno chybějící sledovací ID `?WT.mc_id=academic-105485-koreyst` do
  odkazu *Microsoft for Startups*.
- Obrázkové zdroje pro lekci 09 regenerovány modelem `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` a
  `images/startup.png` (příklad úpravy před/po byl vytvořen pomocí skutečného
  volání `client.images.edit` s generovanou maskou).

### Ověřeno

- Prošly kontrolou README soubory lekcí 01, 03, 05, 12, 14 a 16 — všechny aktuální (správné názvy a odkazy Microsoft Foundry);
  nebyly potřeba žádné změny.
- Provedena úplná kontrola všech 41 markdown souborů v repozitáři (bez překladu) kvůli
  zastaralým cestám dokumentace, `/en-us/` lokalizacím Microsoft, zastaralým názvům produktů/modelů, chybějícím sledovacím
  ID a nefunkčním relativním odkazům/obrázkům. Pouze jediná mezera ve sledovacím ID pro *Microsoft for Startups* byla
  k nápravě; ostatní výstrahy byly potvrzeny jako falešné poplachy (automaticky generované překladové odkazy,
  komentované zástupné texty a strukturované URL třetích stran `/en/`).

## [2026-07-15] — Přepis lekce 09 (Obrázkové aplikace) pro GPT obrazové modely

### Změněno

- **Přepracována lekce 09 "Vytváření aplikací pro generování obrázků"** kolem současné rodiny modelů **`gpt-image`**
  (výchozí **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` taktéž GA), nahrazující
  zastaralý obsah DALL·E 2/3. Klíčové opravy:
  - `gpt-image` modely vracejí obrázek jako **base64 (`b64_json`)**, nikoliv URL. Všechny příklady aktualizovány na
    `base64.b64decode(...)` místo stahování `url` pomocí `requests`.
  - Zvýšena verze obrázkového API na `2025-04-01-preview`.
  - Nahrazena vymyšlená sekce "temperature" (obrázkové modely nepřijímají `temperature`) a obsah obrazových **variací** pouze pro DALL·E-2 sekcí
    o **úpravě obrázku** (maskování / doplňování).
  - Aktualizovány `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    úkolové poznámkové bloky (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) a .NET `.dib` poznámkový blok.

### Odebráno

- Odstraněny zastaralé příklady `python/aoai-app-variation.py` a `python/oai-app-variation.py`
  (`images.create_variation` je DALL·E-2 pouze a nepodporovaný `gpt-image`).
- Odstraněny 4 opuštěné obrázkové zdroje spojené s odstraněnou sekcí porovnání teploty
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Vyřazena nepotřebná závislost `requests` z pythonových příkladů a požadavků lekce.

### Ověřeno

- Proveden `aoai-app.py` end-to-end test nasazeného `gpt-image-1.5` modelu a potvrzena base64
  dekódovací/ukládací cesta produkuje PNG. Poznámkové bloky potvrzeny jako validní JSON.

## [2026-07-14] — Aktualizace výchozího modelu + návody k modelu pro odvozování

### Změněno

- **Výchozí chatovací model `gpt-4o-mini` → `gpt-5-mini`** napříč spustitelnými příklady v učebním plánu,
  dokumentací a konfigurací. Bylo to způsobeno stavem životního cyklu modelu: na Microsoft Foundry,
  `gpt-4o-mini` (ukončen 2026-10-01) a celá rodina `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, ukončena 2026-10-14) jsou **vypínány**, zatímco rodina **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) je obecně dostupná** (ukončení 2027-02-06). Aktualizováno:
  - `.env.copy`, `00-course-setup/03-providers.md` (doporučené příkazy nasazení a `az cognitiveservices`)
    nasazení) a README pro lekce 04, 06, 07 a 15.
  - Pythonové příklady v lekci 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) a skripty v lekci 08.
  - TypeScript / JavaScript příklady v lekcích 06, 07 a 11 a `.dib` .NET poznámkové bloky
    pro lekce 06 a 07.
  - Úkolové poznámkové bloky v lekcích 04, 06, 07 a 11 (kódové buňky) a příklady docstringů `shared/python/api_utils.py`.
- **Návody k parametrům modelu pro odvozování (nové).** `gpt-5-mini` je *reasoning* model: nepodporuje
  `temperature`/`top_p` a používá `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) místo `max_tokens`. Podle toho:
  - Odebráno `temperature`/`top_p`/`max_tokens` z příkladů, které nyní ve výchozím nastavení používají `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README RAG lekce 15).
  - Přidána poznámka **"Modely pro odvozování nepoužívají `temperature`"** do lekce 06,
    že modely pro odvozování se ovládají pomocí **prompt engineering + řízení odvozování** místo
    parametrů vzorkování, zatímco `temperature`/`top_p` zůstávají platné u nerezonujících modelů
    (GPT-4.x, Mistral, Llama, Phi, open models).
- **`gpt-5-mini` není použit pro návod na doladění (lekce 18).** GPT-5 podporuje pouze posilované doladění (RFT);
  návod na supervidované doladění (SFT) v lekci 18 stále používá `gpt-4.1-mini`, který SFT/DPO podporuje.
- **Ukázky teplotních demo používají model Llama.** Aby bylo možné vyučovat `temperature` (který modely pro odvozování
  odmítají), používá se model `Llama-3.3-70B-Instruct` přes Foundry Models endpoint. Přidána nová
  proměnná `AZURE_INFERENCE_CHAT_MODEL` do `.env.copy`; poznámkové bloky lekcí 04/06 s `githubmodels` a
  ukázka `06` `js-githubmodels` to čtou (s návratem k `Llama-3.3-70B-Instruct`) a zachovávají
  svá demo `temperature`/`top_p`/`max_tokens`.
- **JS / .NET příklady aktualizovány pro GPT-5.** Odebrány `temperature`/`top_p`/`max_tokens`
  z příkladů GPT-5 (`06` `recipe-app` TypeScript, `06` `.dib` .NET - který také zvedá `MaxOutputTokenCount`,
  takže výstup odvozování není oříznutý). `06` `js-githubmodels` příklad nyní používá Llamu, aby zachoval své
  teplotní demo. `.dib` poznámky, že `Azure.AI.Inference` + model Llama je správný způsob,
  jak na `Temperature` ukázat v .NET.
- `gpt-4o-mini` / `gpt-5-mini` ponechány tam, kde jsou stále správné: odkazy na kódování tokenů `tiktoken`,
  seznamy dostupnosti v katalogu modelů a řečové modely lekce 02 (`gpt-4o-transcribe`).
- Vzorky lekcí 20 (Mistral) a 21 (Meta) zachovávají `temperature`/`max_tokens`, protože cílí
  na modely Mistral/Llama, které tyto parametry podporují.

## [2026-07-06] — Aktualizace modernizace obsahu

Široké osvěžení pro zachování přesnosti učebního plánu pro rok 2026: moderní API, aktuální názvy produktů a


### Přidáno

### Přidáno

- Sekce **Microsoft Agent Framework** v lekci `17-ai-agents` pokrývající jednotlivé chatovací agenty,
  nástroje/vyvolávání funkcí, konfiguraci Azure OpenAI (Microsoft Foundry) a orchestraci pracovních toků
  více agentů (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentován jako offline / na zařízení poskytovatel (vedle Ollama) v
  `00-course-setup/03-providers.md` a lekci `19-slm`.
- **Pracovní toky kontinuální integrace**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (vynucováno na udržovaném modulu `shared/`,
    doporučení v celém zbytku kurikula), doporučující průchod ESLint a úloha pytest.
  - `.github/workflows/security.yml` — Analýza CodeQL (Python + JavaScript/TypeScript) a přezkum závislostí při požadavcích na sloučení.
- **Testovací sada** pod `tests/` — 41 testů pytest pokrývajících sdílený uživatelský modul.
- **Azure OpenAI → Responses API migrační dovednost** pod
  `.github/skills/azure-openai-to-responses/` používaná k vedení migrace API.




  (`client.responses.create(...)` → `response.output_text`), včetně lekcí 04, 06, 07, 11,
  15 a 18, plus jejich README.
- **GitHub Models → Microsoft Foundry Models** napříč textem, odkazy a příklady. GitHub Models
  bude ukončen koncem července 2026; příklady nyní odkazují na katalog modelů Microsoft Foundry a používají
  proměnné prostředí `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **Dokumentace k `.env.copy`, `AGENTS.md` a poskytovateli** aktualizována tak, aby odrážela, že Azure OpenAI je nyní součástí
  Microsoft Foundry, a výchozí verze API byla navýšena na `2024-10-21`.
- **Příklady v TypeScriptu** (lekce 06, 07, 08, 11) převedeny z zastaralého beta SDK `@azure/openai`
  na balíček `openai` (chat aplikace používají Responses API; vyhledávací aplikace používá
  embeddings klienta).
- **.NET poznámkové bloky** (`dotnet/*.dib`) standardizovány na `Azure.AI.OpenAI` **2.1.0**: lekce 06 a 07
  používají `ChatClient` API, lekce 08 používá `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), a
  lekce 09 používá `ImageClient` (`GenerateImage`) s `gpt-image-1`, nahrazující zastaralé
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` z `1.0.0-beta.9`.
- **Modernizace názvů produktů**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekce 14, 16, 17) a "Bing" → **Microsoft Copilot** (lekce 12), pokud se jednalo o
  současné produkty.
  aktuální produkty.
- **DevContainer** (`.devcontainer/`) nyní obsahuje rozšíření Pylance, Black, Ruff, ESLint, Prettier a Copilot,
  povoluje formátování při ukládání a instaluje `ruff`, `black`, `mypy` a `pytest`, takže kontrola CI
  může být reprodukována lokálně.
- **Generování obrázků** (lekce 09) doporučuje `gpt-image-1` pro Azure (katalog Azure zrušil
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** aktualizováno tak, aby odráželo dokončenou práci (migrace API, CI,
  DevContainer, testy) a aktuální fakta (překlady jsou automaticky vytvářeny Azure Co-op Translator; Assistants API je nahrazeno Responses API).


### Opraveno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` nyní vrací
  prázdný řetězec pro vstup obsahující pouze bílé znaky místo vyvolání chyby „příliš krátký“ (v souladu s případem
  `None`). Nalezeno a pokryto novou sadou testů.
- **Ukázky obrázků v lekci 09** — opraveny skutečné chyby: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  a proměnná, která zastínila modul `openai`.
- **Notebook lekce 15 RAG** — opraveno nastavení klienta, nahrazen odstraněný `DataFrame.append`
  za `pd.concat` a modernizováno používání staršího SDK.
- Zastaralá / ukončená jména modelů (`gpt-3.5-turbo`, `gpt-35-turbo`) nahrazena `gpt-4o-mini`
  v aktivních ukázkách; historické výstupy fine-tuningu v lekci 18 byly zachovány a komentovány
  místo přepisování.

### Zastaralé / Poznámky

- **Ukázky Microsoft Foundry Models**, které používají `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ukázky `githubmodels-*` a `js-githubmodels` a lekce 19, 20,
  a 21 — zůstávají na Model Inference API, které **nepodporuje** Responses API. Tyto byly
  záměrně ponechány v tomto SDK.
- `AzureOpenAI()` je záměrně zachováno, kde je to stále vhodné (embeddingy a generování obrázků),
  protože tyto workflow nejsou součástí migrace na Responses API.
- Odkazy na `text-embedding-ada-002` jsou uchovány tam, kde na nich závisí předpočítaný embedding index.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->