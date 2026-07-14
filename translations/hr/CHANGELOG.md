# Dnevnik promjena

Sve značajne promjene u kurikulumu Generativna AI za početnike dokumentirane su u ovoj datoteci.

Format je temeljen na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Budući da se radi o
kurikulumu za učenje, a ne verzioniranom softverskom paketu, unosi su grupirani prema datumu.

## [2026-07-06] — Modernizacija sadržaja

Opsežan osvježavanje za održavanje točnosti kurikuluma za 2026: moderni API-ji, trenutačna imena proizvoda i
imena modela, ažurirane smjernice pružatelja i novi alati za iskustvo programera.

### Dodano

- Sekcija **Microsoft Agent Framework** u lekciji `17-ai-agents` koja pokriva agente za pojedinačni chat,
  alate/pozivanje funkcija, konfiguraciju Azure OpenAI (Microsoft Foundry) i višestruku orkestraciju
  tijekova rada (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentiran kao offline / na uređaju pružatelj (zajedno s Ollama) u
  `00-course-setup/03-providers.md` i lekciji `19-slm`.
- **Tijekovi kontinuirane integracije**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (primjenjivano na održavani `shared/`
    modul, savjetodavno u ostatku kurikuluma), savjetodavni ESLint prolaz i pytest zadatak.
  - `.github/workflows/security.yml` — CodeQL analiza (Python + JavaScript/TypeScript) i
    pregled ovisnosti na zahtjevima za povlačenje.
- **Skup testova** pod `tests/` — 41 pytest test pokrivajući zajednički korisnički modul.
- **Vještina migracije Azure OpenAI → Responses API** pod
  `.github/skills/azure-openai-to-responses/` korištena za vođenje migracije API-ja.

### Promijenjeno

- **Chat Completions API → Responses API** u svim Python i TypeScript chat primjerima
  (`client.responses.create(...)` → `response.output_text`), uključujući lekcije 04, 06, 07, 11,
  15 i 18 te njihove README datoteke.
- **GitHub modeli → Microsoft Foundry modeli** kroz tekst, poveznice i primjere. GitHub modeli
  se povlače krajem srpnja 2026; primjeri sada pokazuju na katalog Microsoft Foundry modela i koriste
  varijable okoline `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` i dokumentacija pružatelja** ažurirani da odražavaju da je Azure OpenAI sada dio
  Microsoft Foundry, a zadana verzija API-ja je podignuta na `2024-10-21`.
- **TypeScript primjeri** (lekcije 06, 07, 08, 11) migrirani s zastarjelog beta SDK `@azure/openai`
  na paket `openai` (chat aplikacije koriste Responses API; aplikacija za pretraživanje koristi
  klijenta za ugradnju).
- **.NET bilježnice** (`dotnet/*.dib`) standardizirane na `Azure.AI.OpenAI` **2.1.0**: lekcije 06 i 07
  koriste `ChatClient` API, lekcija 08 koristi `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), i
  lekcija 09 koristi `ImageClient` (`GenerateImage`) s `gpt-image-1`, zamjenjujući naslijeđeni
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` iz `1.0.0-beta.9`.
- **Modernizacija imena proizvoda**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcije 14, 16, 17) i "Bing" → **Microsoft Copilot** (lekcija 12), gdje se odnose na
  aktualne proizvode.
- **DevContainer** (`.devcontainer/`) sada uključuje Pylance, Black, Ruff, ESLint, Prettier i Copilot
  ekstenzije, omogućuje automatsko formatiranje pri spremanju i instalira `ruff`, `black`, `mypy` i `pytest` tako da se CI
  provjere mogu reproducirati lokalno.
- **Generiranje slika** (lekcija 09) preporučuje `gpt-image-1` za Azure (katalog Azure je povukao
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ažuriran da odražava izvršeni rad (migracija API-ja, CI,
  DevContainer, testovi) i trenutačne informacije (prijevodi se automatski proizvode putem
  Azure Co-op Translatora; Assistants API je zamijenjen Responses API-jem).

### Ispravljeno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sada vraća
  prazan niz za unos koji je samo razmak umjesto da baci grešku "prekratak unos" (dosljedno s
  slučajem `None`). Pronađeno i obuhvaćeno novim skupom testova.
- **Primjeri za slike u lekciji 09** — ispravljene stvarne pogreške: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  i varijabla koja je zasjenjivala `openai` modul.
- **Bilježnica RAG u lekciji 15** — popravljen setup klijenta, zamijenjen uklonjeni `DataFrame.append`
  s `pd.concat` i modernizirana upotreba naslijeđenog SDK-ja.
- Zastarjela / povučena imena modela (`gpt-3.5-turbo`, `gpt-35-turbo`) zamijenjena s `gpt-4o-mini`
  u aktivnim primjerima; povijesni rezultati prilagođavanja u lekciji 18 sačuvani i označeni
  umjesto prepravljeni.

### Zastarjelo / Napomene

- Primjeri **Microsoft Foundry Models** koji koriste SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — primjeri `githubmodels-*` i `js-githubmodels` i lekcije 19, 20,
  i 21 — ostaju na Model Inference API-ju koji **ne podržava** Responses API. Namjerno su
  ostavljeni na tom SDK-ju.
- `AzureOpenAI()` ostaje zadržan gdje je još prikladno (ugradnje i generiranje slika),
  jer ti tijekovi rada nisu dio migracije Responses API-ja.
- Reference na `text-embedding-ada-002` zadržane su gdje o njima ovisi unaprijed izračunat indeks ugradnje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->