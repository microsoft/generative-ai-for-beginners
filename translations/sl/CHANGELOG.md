# Dnevnik sprememb

Vse pomembne spremembe v učnem načrtu Generativne umetne inteligence za začetnike so dokumentirane v tej datoteki.

Oblika temelji na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Ker gre za učni načrt in ne za programsko opremo z različicami, so vnosi razvrščeni po datumih.






  povezavi na trenutno `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (preverjeno v živo).
- **Lekcija 17 (AI agenti):** posodobljen zastarel primer modela (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, in Llama 3.3`) in nadomestno ime za nameščanje v vzorcu Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Glavni `README.md`:** dodan manjkajoči ID sledenja `?WT.mc_id=academic-105485-koreyst` na povezavo
  *Microsoft for Startups*.
- **Slikovne zbirke Lekcije 09** so bile ponovno ustvarjene z modelom `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` in
  `images/startup.png` (pred/po primer za urejanje je bil ustvarjen z dejanskim
  klicem `client.images.edit` in generirano masko).




  poimenovanja in povezave); spremembe niso potrebne.
- Opravljen popoln pregled markdowna vseh 41 markdown datotek v repozitoriju (razen prevodov) zaradi
  zastarelih potek dokumentacije, `/en-us/` Microsoft lokalizacij, zastarelih imen izdelkov/modelov,
  manjkajočih ID-jev za sledenje in zlomljenih relativnih povezav/slik. Obvladljiv je bil le en
  manjkajoči ID sledenja pri *Microsoft for Startups*; vse ostale oznake so bile potrjene kot
  napačne pozitivne (samodejno ustvarjene povezave za prevode, skriti rezervirani elementi in
  tretjišolske `/en/` strukturne URL-je).

## [2026-07-15] — Prepis lekcije 09 (Uporaba slik) za GPT slikovne modele

### Spremenjeno

- **Prepisana lekcija 09 "Ustvarjanje aplikacij za generiranje slik"** okoli trenutne družine modelov **`gpt-image`**
  (privzeti **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` sta tudi GA), s nadomestitvijo
  zastarele vsebine DALL·E 2/3. Ključne popravke:
  - modeli `gpt-image` vračajo sliko kot **base64 (`b64_json`)**, ne URL. Vsi primeri so posodobljeni, da
    uporabljajo `base64.b64decode(...)` namesto nalaganja URL z `requests`.
  - Posodobljena različica slikovnega API-ja na `2025-04-01-preview`.
  - Nadomeščena izmislena sekcija "temperature" (slikovni modeli ne uporabljajo `temperature`) in
    vsebina o variacijah slik (samo za DALL·E-2) z razdelkom o **urejanju slike** (maskiranje/retuširanje).
  - Posodobljeni `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    notebok za naloge (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) in .NET `.dib` notebok.

### Odstranjeno

- Izbrisani zastareli primeri `python/aoai-app-variation.py` in `python/oai-app-variation.py`
  (`images.create_variation` je samo za DALL·E-2 in ni podprt pri `gpt-image`).
- Izbrisane 4 zapuščene slikovne datoteke povezane s sekcijo o primerjavah temperature
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Odstranjena nepotrebna odvisnost `requests` iz Python primerov in zahtev lekcije.

### Preverjeno

- Zagnan `aoai-app.py` kompletno na nameščenem modelu `gpt-image-1.5` in potrjeno, da proces dekodiranja/shranjevanja base64
  ustvari PNG sliko. Noteboki potrjeni kot veljavni JSON.

## [2026-07-14] — Posodobitev privzetega modela + navodila za model razmišljanja

### Spremenjeno

- **Privzeti klepetalni model `gpt-4o-mini` → `gpt-5-mini`** v vseh zagonljivih primerih učnega načrta,
  dokumentaciji in konfiguraciji. To je bilo povzročeno z življenjskim ciklom modela: na Microsoft Foundry,
  je `gpt-4o-mini` (upokoji se 2026-10-01) in celotna družina `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, se upokojijo 2026-10-14) **v postopku ukinjanja**, medtem ko je družina **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) splošno dostopna** (upokojitev 2027-02-06). Posodobljeno:
  - `.env.copy`, `00-course-setup/03-providers.md` (priporočena nameščanja in ukazi `az cognitiveservices`
    za nameščanje) in README-ji za lekcije 04, 06, 07 in 15.
  - Python primeri v lekciji 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) ter skripte lekcije 08.
  - TypeScript / JavaScript primeri v lekcijah 06, 07 in 11 ter `.dib` .NET noteboki za
    lekcije 06 in 07.
  - Noteboki za naloge v lekcijah 04, 06, 07 in 11 (kode celic), plus primere v `shared/python/api_utils.py`
    docstring.
- **Navodila za parametre modela razmišljanja (novo).** `gpt-5-mini` je *model za razmišljanje*: ne podpira
  `temperature`/`top_p`, uporablja `max_completion_tokens` (klepetalne dokončnice) /
  `max_output_tokens` (Responses API) namesto `max_tokens`. V skladu s tem:
  - Odstranjeno `temperature`/`top_p`/`max_tokens` iz primerov, ki zdaj privzeto uporabljajo `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcija 15 RAG README).
  - Dodana opomba **"Modeli za sklepanja ne uporabljajo `temperature`"** v lekcijo 06, ki pojasnjuje, da
    se modeli za sklepanja usmerjajo z **prompt inženiringom + kontrolami sklepov** namesto
    nastavitvami vzorčenja, medtem ko `temperature`/`top_p` ostajata veljavna na modelih brez sklepov
    (GPT-4.x, Mistral, Llama, Phi, odprti modeli).
- **`gpt-5-mini` se ne uporablja za vadnico fino prilagajanje (lekcija 18).** GPT-5 podpira
  samo krepitveno fino prilagajanje (RFT); vodnik lekcije 18 za nadzorovano fino prilagajanje (SFT) ostaja
  z `gpt-4.1-mini`, ki podpira SFT/DPO.
- **Demonstracije temperature uporabljajo model Llama.** Da se ohranja predavanje o `temperature` (ki ga modeli za sklepanja
  zavračajo), se uporablja model `Llama-3.3-70B-Instruct` prek vmesnika Foundry Models. Dodana nova
  spremenljivka `AZURE_INFERENCE_CHAT_MODEL` v `.env.copy`; zvezki z lekcij 04/06 `githubmodels` in
  vzorec `06` `js-githubmodels` jo berejo (z vračanjem na `Llama-3.3-70B-Instruct`) in ohranjajo svoje
  demonstracije `temperature`/`top_p`/`max_tokens`.
- **JS / .NET primeri posodobljeni za GPT-5.** Odstranjeno `temperature`/`top_p`/`max_tokens` iz primerov GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ki tudi povečuje `MaxOutputTokenCount`,
  da izhod sklepov ni skrajšan). Vzorec `06` `js-githubmodels` zdaj uporablja Llama za ohranitev
  demonstracije temperature. `.dib` navaja, da je `Azure.AI.Inference` + Llama model način za
  prikaz `Temperature` v .NET.
- Ostaneta `gpt-4o-mini` / `gpt-5-mini` tam, kjer ostajata natančna: reference kodiranja tokenov `tiktoken`,
  seznami razpoložljivosti kataloga modelov in govornih modelov lekcije 02 (`gpt-4o-transcribe`).
- Vzorce lekcij 20 (Mistral) in 21 (Meta) ohranjata `temperature`/`max_tokens`, ker ciljata
  modele Mistral/Llama, ki podpirajo te parametre.

## [2026-07-06] — Osvežitev posodobitve vsebine

Obsežna osvežitev za ohranitev točnosti učnega načrta za leto 2026: sodobni API-ji, trenutna imena izdelkov in
imen modelov, posodobljena navodila za ponudnike in nova orodja za razvijalce.

### Dodano

- Razdelek **Microsoft Agent Framework** v lekciji `17-ai-agents`, ki zajema posamezne klepetalne agente,
  orodja/klice funkcij, konfiguracijo Azure OpenAI (Microsoft Foundry) in večagentno
  orkestracijo delovnih tokov (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentiran kot ponudnik brez povezave / na napravah (ob Ollami) v
  `00-course-setup/03-providers.md` in lekciji `19-slm`.
- **Delovni tokovi za neprekinjeno integracijo**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (prisilno na vzdrževanem modulu `shared/`,
    opozorilo za preostali učni načrt), preverjanje ESLint in opravilo pytest.
  - `.github/workflows/security.yml` — analiza CodeQL (Python + JavaScript/TypeScript) in
    pregled odvisnosti pri pull requestih.
- **Testni niz** pod `tests/` — 41 pytest testov, ki pokrivajo skupni uporabniški modul.
- **Sposobnost migracije Azure OpenAI → Responses API** pod
  `.github/skills/azure-openai-to-responses/`, ki vodi pri migraciji API-ja.

### Spremenjeno

- **Chat Completions API → Responses API** v vseh Python in TypeScript primerih klepetov
  (`client.responses.create(...)` → `response.output_text`), vključno z lekcijami 04, 06, 07, 11,
  15 in 18, ter njihovimi READMEs.
- **GitHub Models → Microsoft Foundry Models** v celotnem besedilu, povezavah in primerih. GitHub Models
  se upokojijo konec julija 2026; primeri zdaj kažejo na katalog modelov Microsoft Foundry in uporabljajo
  okoljske spremenljivke `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` in dokumentacija za ponudnike** posodobljeni, da odražajo, da je Azure OpenAI zdaj del
  Microsoft Foundry in privzeta različica API-ja je zvišana na `2024-10-21`.
- **TypeScript primeri** (lekcije 06, 07, 08, 11) so migrirani s starega `@azure/openai`
  beta SDK-ja na paket `openai` (klepetalne aplikacije uporabljajo Responses API; iskalna aplikacija uporablja
  embeddings klient).
- **.NET zvezki** (`dotnet/*.dib`) standardizirani na `Azure.AI.OpenAI` **2.1.0**: lekcije 06 in 07
  uporabljajo `ChatClient` API, lekcija 08 uporablja `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), in
  lekcija 09 uporablja `ImageClient` (`GenerateImage`) z `gpt-image-1`, ki nadomesti legendarni
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` iz `1.0.0-beta.9`.
- **Posodobitev imen izdelkov**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcije 14, 16, 17) in "Bing" → **Microsoft Copilot** (lekcija 12), kjer so ti izrazi označevali
  trenutne izdelke.
- **DevContainer** (`.devcontainer/`) zdaj vsebuje razširitve Pylance, Black, Ruff, ESLint, Prettier in Copilot,
  omogoča formatiranje ob shranjevanju in namesti `ruff`, `black`, `mypy` in `pytest`, da se
  lokalno reproducirajo CI kontrole.
- **Generiranje slik** (lekcija 09) priporoča `gpt-image-1` za Azure (katalog Azure je odstranil
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** posodobljen za odraz opravljenega dela (migracija API, CI,
  DevContainer, testi) in trenutnih dejstev (prevodi nastajajo samodejno prek
  Azure Co-op Translator; API za asistente je nadomeščen z API za odgovore).

### Popravljeno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` zdaj vrne
  prazen niz za vnos, ki vsebuje samo presledke, namesto da sproži napako "prekratko" (skladno s primerom `None`).
  Najdeno in zajeto z novo zbirko testov.
- **Primeri slik pri Lekciji 09** — popravljene resnične napake: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  in spremenljivka, ki je prekrila modul `openai`.
- **Lekcija 15 RAG zvezek** — popravljen nastavitev odjemalca, zamenjan odstranjeni `DataFrame.append`
  z `pd.concat` in posodobljena uporaba starega SDK.
- Zastarele / upokojene oznake modelov (`gpt-3.5-turbo`, `gpt-35-turbo`) zamenjane z `gpt-4o-mini`
  v aktivnih primerih; zgodovinski izhodi finotuningov v lekciji 18 so ostali ohranjeni in označeni,
  namesto da bi jih prepisali.

### Zastarelo / Opombe

- **Vzorec Microsoft Foundry modelov**, ki uporablja `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — vzorci `githubmodels-*` in `js-githubmodels` ter lekcije 19, 20,
  in 21 — ostajajo na Model Inference API, ki **ne** podpira Responses API. Ti so
  namensko pustjeni na tem SDK.
- `AzureOpenAI()` je namensko ohranjen tam, kjer je še primeren (ugnezditve in generiranje slik),
  saj ti poteki dela niso del migracije na Responses API.
- Reference `text-embedding-ada-002` so ohranjene, kjer je indeks predračunanih ugnjezditev odvisen od njih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->