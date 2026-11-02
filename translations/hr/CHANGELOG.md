# Dnevnik promjena

Sve značajne promjene u programu Generative AI za početnike dokumentirane su u ovoj datoteci.

Format je temeljen na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Budući da se radi o
obrazovnom programu, a ne o verzioniranom softverskom paketu, unosi su grupirani po datumima.

## [2026-07-16] — Validacija sadržaja + slike za lekciju 09

### Promijenjeno

- **Lekcija 10 (AI aplikacije s malo koda):** ažurirane su dvije zastarjele veze `docs.microsoft.com/powerapps/...` Dataverse
  na trenutni `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (provjereno uživo).
- **Lekcija 17 (AI agenti):** moderniziran je zastarjeli primjer modela (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) i rezervno ime za implementaciju u uzorku Agent Frameworka
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Korijenski `README.md`:** dodan je nedostajući `?WT.mc_id=academic-105485-koreyst` identifikator za praćenje na
  *Microsoft for Startups* poveznici.
- **Slike za lekciju 09** ponovno generirane s modelom `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` i
  `images/startup.png` (par prije/poslije primjera uređivanja proizveden je stvarnim
  `client.images.edit` pozivom s generiranom maskom).

### Validirano

- Pregledani su README-ovi za lekcije 01, 03, 05, 12, 14 i 16 — svi su aktualni (ispravan Microsoft Foundry
  naziv i veze); nisu potrebne promjene.
- Provedena je potpuna validacija markdown datoteka svih 41 datoteka u repozitoriju (bez prijevoda) radi
  zastarjelih staza dokumenata, `/en-us/` Microsoft lokaliteta, zastarjelih naziva proizvoda/modela, nedostajućih identifikatora praćenja,
  i neispravnih relativnih veza/slika. Jedina problematična stvar bila je
  praznina u identifikatoru praćenja *Microsoft for Startups*; svi ostali znakovi potvrđeni su kao netočne pozitivne dojave (automatski generirane veze za prijevod,
  komentirani rezervirani nazivi, i URL-ovi trećih strana `/en/` strukture).

## [2026-07-15] — Lekcija 09 (Aplikacije za slike) Prepis za GPT modele slika

### Promijenjeno

- **Prepisana lekcija 09 "Izgradnja aplikacija za generiranje slika"** oko trenutnog **`gpt-image`**
  obiteljski model (zadano **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` također GA), zamjenjujući
  naslijeđeni DALL·E 2/3 sadržaj. Ključne ispravke:
  - `gpt-image` modeli vraćaju sliku kao **base64 (`b64_json`)**, a ne URL. Ažurirani svi primjeri da koriste
    `base64.b64decode(...)` umjesto preuzimanja `url` s `requests`.
  - Povećana verzija API-ja za slike na `2025-04-01-preview`.
  - Zamijenjen izmišljeni odjeljak "temperature" (modeli za slike ne koriste `temperature`) i
    sadržaj DALL·E-2-ključnih varijacija slika sa sekcijom **uređivanja slike** (maskiranje/ispunjavanje).
  - Ažurirani `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    dodijeljena notesa (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), i .NET `.dib` notes.

### Uklonjeno

- Izbrisani zastarjeli primjeri `python/aoai-app-variation.py` i `python/oai-app-variation.py`
  (`images.create_variation` je samo za DALL·E-2 i nije podržan u `gpt-image`).
- Izbrisani 4 napuštena grafička sredstva vezana uz uklonjeni odjeljak o usporedbi temperature
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Uklonjena nepotrebna zavisnost `requests` iz Python primjera i zahtjeva lekcije.

### Validirano

- Pokrenut `aoai-app.py` end-to-end na implementiranom `gpt-image-1.5` modelu i potvrđeno da base64
  dekodiranje/spremanje proizvodi PNG. Notes potvrđeni kao valjani JSON.

## [2026-07-14] — Ažuriranje zadane verzije modela + vođenje modela za rezoniranje

### Promijenjeno

- **Zadani chat model `gpt-4o-mini` → `gpt-5-mini`** kroz sve pokretne primjere
  u kurikulumu, dokumentaciji i konfiguraciji. Ovu promjenu je potaknulo stanje životnog ciklusa modela: na Microsoft Foundry,
  `gpt-4o-mini` (povlačenje 01.10.2026.) i cijela `gpt-4.1` obitelj (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, povlačenje 14.10.2026.) su **zastarjeli**, dok je **GPT-5 obitelj
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) općenito dostupna** (povlačenje 06.02.2027.). Ažurirano:
  - `.env.copy`, `00-course-setup/03-providers.md` (preporučena implementacija i `az cognitiveservices`
    naredbe za implementaciju), te README datoteke za lekcije 04, 06, 07 i 15.
  - Python primjeri u lekciji 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) i skripte lekcije 08.
  - TypeScript / JavaScript primjeri u lekcijama 06, 07 i 11, te `.dib` .NET bilježnice za
    lekcije 06 i 07.
  - Bilježnice zadataka u lekcijama 04, 06, 07 i 11 (ćelije koda), plus `shared/python/api_utils.py`
    primjeri docstringova.
- **Vodič za parametar reasoning-model (novo).** `gpt-5-mini` je *reasoning* model: on **ne**
  podržava `temperature`/`top_p`, i koristi `max_completion_tokens` (chat dovršetke) /
  `max_output_tokens` (Responses API) umjesto `max_tokens`. Sukladno tome:
  - Uklonjeno `temperature`/`top_p`/`max_tokens` iz primjera koji sada prema zadanim postavkama koriste `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcija 15 RAG README).
  - Dodana je bilješka **"Modeli rezoniranja ne koriste `temperature`"** u lekciju 06, objašnjavajući da
    se modeli rezoniranja usmjeravaju pomoću **prompt inženjeringa + kontrola rezoniranja** umjesto
    podešavanja uzorkovanja, dok `temperature`/`top_p` ostaju važeći za modele koji nisu modeli rezoniranja
    (GPT-4.x, Mistral, Llama, Phi, otvoreni modeli).
- **`gpt-5-mini` se ne koristi za tutorijal finog podešavanja (lekcija 18).** GPT-5 podržava samo
  pojačano fino podešavanje (RFT); tutorijal za nadzirano fino podešavanje (SFT) u lekciji 18 zadržava
  `gpt-4.1-mini`, koji podržava SFT/DPO.
- **Prezentacije temperature koriste Llama model.** Kako bi se nastavilo podučavati `temperature` (koji modeli rezoniranja
  odbacuju), koristi se `Llama-3.3-70B-Instruct` model preko Foundry Models krajnje točke. Dodana je nova
  `AZURE_INFERENCE_CHAT_MODEL` varijabla u `.env.copy`; lekcije 04/06 `githubmodels` bilježnice i
  uzorak `06` `js-githubmodels` pročitan je (s povratkom na `Llama-3.3-70B-Instruct`) i čuvaju njihove
  `temperature`/`top_p`/`max_tokens` demonstracije.
- **JS / .NET uzorci su ažurirani za GPT-5.** Uklonjeno `temperature`/`top_p`/`max_tokens` iz GPT-5
  uzoraka (`06` `recipe-app` TypeScript, `06` `.dib` .NET - što također podiže `MaxOutputTokenCount`
  tako da se izlaz rezoniranja ne skraćuje). `06` `js-githubmodels` uzorak sada koristi Llamu za zadržavanje
  demonstracije temperature. `.dib` ističe da je `Azure.AI.Inference` + Llama model način za
  demonstraciju `Temperature` u .NET-u.
- Ostavljeni `gpt-4o-mini` / `gpt-5-mini` na mjestu gdje ostaju točni: `tiktoken` reference enkodiranja tokena,
  liste dostupnosti kataloga modela i modeli govora u lekciji 02 (`gpt-4o-transcribe`).
- Uzorci lekcija 20 (Mistral) i 21 (Meta) zadržavaju `temperature`/`max_tokens` jer ciljaju
  Mistral/Llama modele koji podržavaju te parametre.

## [2026-07-06] — Osvježenje modernizacije sadržaja

Široko osvježenje za održavanje nastavnog plana točnim za 2026: moderni API-ji, trenutni nazivi proizvoda i
nazivi modela, ažurirane smjernice za pružatelje i novi alati za razvojno iskustvo.

### Dodano

- **Microsoft Agent Framework** sekcija u lekciji `17-ai-agents` koja pokriva jednostruke chat agente,
  alate/pozivanje funkcija, Azure OpenAI (Microsoft Foundry) konfiguraciju i multi-agent
  orkestracija tijeka rada (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentirano kao offline / na uređaju davatelj (uz Ollama) u
  `00-course-setup/03-providers.md` i lekciji `19-slm`.
- **Tijekovi kontinuirane integracije**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (primjenjuje se na održavani `shared/`
    modul, savjetodavni za ostatak kurikuluma), savjetodavna ESLint provjera, i pytest posao.
  - `.github/workflows/security.yml` — CodeQL analiza (Python + JavaScript/TypeScript) i
    pregled ovisnosti na pull zahtjevima.
- **Testni skup** pod `tests/` — 41 pytest test koji pokriva zajednički pomoćni modul.
- **Azure OpenAI → vještina migracije Responses API-ja** pod
  `.github/skills/azure-openai-to-responses/` koja služi za vođenje migracije API-ja.

### Promijenjeno

- **Chat Completions API → Responses API** u svim Python i TypeScript chat primjerima
  (`client.responses.create(...)` → `response.output_text`), uključujući lekcije 04, 06, 07, 11,
  15 i 18, plus njihove README datoteke.
- **GitHub Models → Microsoft Foundry Models** u cjelokupnom tekstu, linkovima i primjerima. GitHub Models
  prestaje s krajem srpnja 2026.; primjeri sada upućuju na Microsoft Foundry katalog modela i koriste
  varijable okoline `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` i dokumentacija davatelja** ažurirani da odražavaju da je Azure OpenAI sada dio
  Microsoft Foundry, a zadana verzija API-ja je podignuta na `2024-10-21`.
- **TypeScript primjeri** (lekcije 06, 07, 08, 11) migrirani s zastarjelog `@azure/openai`
  beta SDK-a na `openai` paket (chat aplikacije koriste Responses API; aplikacija za pretraživanje koristi
  embeddings klijent).
- **.NET bilježnice** (`dotnet/*.dib`) standardizirane na `Azure.AI.OpenAI` **2.1.0**: lekcije 06 i 07
  koriste `ChatClient` API, lekcija 08 koristi `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), i
  lekcija 09 koristi `ImageClient` (`GenerateImage`) s `gpt-image-1`, zamjenjujući zastarjeli
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` iz `1.0.0-beta.9`.
- **Modernizacija imena proizvoda**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcije 14, 16, 17) i "Bing" → **Microsoft Copilot** (lekcija 12), gdje su se ti pojmovi odnosili na
  aktualne proizvode.
- **DevContainer** (`.devcontainer/`) sada dolazi s Pylance, Black, Ruff, ESLint, Prettier i Copilot
  ekstenzijama, omogućuje formatiranje pri spremanju i instalira `ruff`, `black`, `mypy` i `pytest` kako bi CI
  provjere mogle biti reproducirane lokalno.
- **Generiranje slika** (lekcija 09) preporučuje `gpt-image-1` za Azure (Azure katalog je uklonio
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ažuriran da odražava završeni rad (migracija API-ja, CI,
  DevContainer, testovi) i trenutne činjenice (prijevodi se automatski proizvode pomoću
  Azure Co-op Translatora; Assistants API je zamijenjen Responses API-jem).

### Ispravljeno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sada vraća
  prazan niz za unos koji sadrži samo razmake umjesto da baca grešku "preslabo" (konzistentno s
  `None` slučaj). Pronađeno i pokriveno novim skupom testova.
- **Primjeri slika iz lekcije 09** — ispravljene stvarne greške: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  i varijabla koja je zasjenila `openai` modul.
- **Bilježnica lekcije 15 RAG** — popravljena konfiguracija klijenta, zamijenjen uklonjeni `DataFrame.append`
  s `pd.concat`, i modernizirano korištenje zastarjelog SDK-a.
- Zastarjeli / povučeni nazivi modela (`gpt-3.5-turbo`, `gpt-35-turbo`) zamijenjeni s `gpt-4o-mini`
  u aktivnim primjerima; povijesni outputi finog podešavanja u lekciji 18 sačuvani i označeni,
  a nisu prepisani.

### Zastarjelo / Bilješke

- **Primjeri Microsoft Foundry modela** koji koriste `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — primjeri `githubmodels-*` i `js-githubmodels` te lekcije 19, 20,
  i 21 — ostaju na Model Inference API-ju, koji **ne** podržava Responses API. To je
  namjerno ostavljeno na tom SDK-u.
- `AzureOpenAI()` je namjerno zadržan gdje je još primjenjiv (ugradnje i generiranje slika),
  budući da ti tijekovi rada nisu dio migracije na Responses API.
- `text-embedding-ada-002` reference se održavaju gdje o njima ovisi unaprijed izračunati indeks ugradnje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->