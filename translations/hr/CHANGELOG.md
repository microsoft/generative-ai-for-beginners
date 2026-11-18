# Dnevnik promjena

Sve značajne promjene u kurikulumu Generativna umjetna inteligencija za početnike dokumentirane su u ovom datoteci.

Format je baziran na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Budući da je ovo
obrazovni kurikulum, a ne verzijski softverski paket, unosi su grupirani po datumu.

## [2026-07-16] — Validacija sadržaja + Grafički elementi lekcije 09

### Promijenjeno

- **Lekcija 10 (nisko-kodne AI aplikacije):** ažurirane dvije zastarjele `docs.microsoft.com/powerapps/...` Dataverse
  poveznice na trenutne `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (provjereno uživo).
- **Lekcija 17 (AI agenti):** moderniziran zastarjeli primjer modela (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) i ime za implementaciju zamjenskog primjera u Agent Framework-u
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** dodan nedostajući `?WT.mc_id=academic-105485-koreyst` identifikator praćenja na
  poveznicu *Microsoft for Startups*.
- **Grafički elementi lekcije 09** regenerirani s modelom `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` i
  `images/startup.png` (prije/poslije primjer uređivanja proizveden je stvarnim
  pozivom `client.images.edit` s generiranom maskom).

### Validirano

- Provjereni README-ovi za lekcije 01, 03, 05, 12, 14 i 16 — svi aktualni (ispravno Microsoft Foundry
  imenovanje i poveznice); nisu potrebne promjene.
- Provedena potpuna validacija markdowna kroz svih 41 markdown datoteka u repozitoriju (bez prijevoda) za
  zastarjele putanje dokumentacije, `/en-us/` Microsoft lokalitete, zastarjele nazive proizvoda/modela, nedostajuće identifikatore praćenja,
  i nepovezane relativne poveznice/grafike. Jedini problematični identifikator bio je kod *Microsoft for Startups*;
  svi ostali su potvrđeni kao lažni alarmi (automatski generirane poveznice za prijevod,
  komentirani placeholderi i strukturalni URL-ovi trećih strana `/en/`).

## [2026-07-15] — Lekcija 09 (Primjene slika) Prepisano za GPT model slika

### Promijenjeno

- **Prepisana lekcija 09 "Izrada aplikacija za generiranje slika"** oko trenutnog **`gpt-image`**
  obitelj modela (zadano **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` također GA), zamjenjujući
  naslijeđeni sadržaj DALL·E 2/3. Ključne ispravke:
  - `gpt-image` modeli vraćaju sliku kao **base64 (`b64_json`)**, a ne URL. Ažurirani su svi primjeri za
    `base64.b64decode(...)` umjesto preuzimanja `url` s `requests`.
  - Povećana verzija slike API-ja na `2025-04-01-preview`.
  - Zamijenjen izmišljeni odjeljak "temperature" (modeli slika ne prihvaćaju `temperature`) i
    sadržaj varijacija slika samo za DALL·E-2 sa sekcijom **uređivanja slika** (maska/retuširanje).
  - Ažurirani `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    zadatka u bilježnicama (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) i .NET `.dib` bilježnica.

### Uklonjeno

- Izbrisani zastarjeli primjeri `python/aoai-app-variation.py` i `python/oai-app-variation.py`
  (`images.create_variation` je samo za DALL·E-2 i nije podržan u `gpt-image`).
- Izbrisane 4 napuštene slikovne datoteke vezane uz uklonjeni odjeljak usporedbe temperature
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Uklonjena nepotrebna ovisnost `requests` iz Python primjera i zahtjeva lekcije.

### Provjereno

- Pokrenut `aoai-app.py` end-to-end na implementiranom `gpt-image-1.5` modelu i potvrđeno da base64
  dekodiranje/spremanje proizvodi PNG. Bilježnice su potvrđene kao valjani JSON.

## [2026-07-14] — Ažuriranje zadanim modelom + vođenje modela rezoniranja

### Promijenjeno

- **Zadani chat model `gpt-4o-mini` → `gpt-5-mini`** u svim izvodiocim primjerima,
  dokumentaciji i konfiguraciji. To je bilo uvjetovano statusom životnog ciklusa modela: na Microsoft Foundry-u,
  `gpt-4o-mini` (povlači se 2026-10-01) i cijela obitelj `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, povlačenje 2026-10-14) su **zastarijevajući**, dok je obitelj **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) općenito dostupna** (povlačenje 2027-02-06). Ažurirano:
  - `.env.copy`, `00-course-setup/03-providers.md` (preporučena implementacija i `az cognitiveservices`
    implementacijski naredbe), i README dokumenti za lekcije 04, 06, 07 i 15.
  - Python primjeri u lekciji 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) i skripte lekcije 08.
  - TypeScript / JavaScript primjeri u lekcijama 06, 07 i 11, te `.dib` .NET bilježnice za
    lekcije 06 i 07.
  - Zadani bilježnički primjeri u lekcijama 04, 06, 07 i 11 (ćelije koda), plus `shared/python/api_utils.py`
    primjeri docstringova.
- **Vodič za parametar reasoning-model (novi).** `gpt-5-mini` je *reasoning* model: on **ne**
  podržava `temperature`/`top_p`, i koristi `max_completion_tokens` (chat dopune) /
  `max_output_tokens` (Responses API) umjesto `max_tokens`. Sukladno tome:
  - Uklonjeno `temperature`/`top_p`/`max_tokens` iz primjera koji sada zadano koriste `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcija 15 RAG README).
  - Dodana bilješka **"Razumski modeli ne koriste `temperature`"** u lekciju 06, objašnjavajući da
    se razumski modeli upravljaju putem **prompt inženjeringa + kontrola razuma** umjesto
    kontrola uzoraka, dok `temperature`/`top_p` ostaju valjani na modelima koji nisu za rezoniranje
    (GPT-4.x, Mistral, Llama, Phi, otvoreni modeli).
- **`gpt-5-mini` se ne koristi u vodiču za fino podešavanje (lekcija 18).** GPT-5 podržava
  samo pojačano fino podešavanje (RFT); vodič za nadzirano fino podešavanje (SFT) u lekciji 18 zadržava
  `gpt-4.1-mini`, koji podržava SFT/DPO.
- **Demo temperature koriste Llama model.** Da bi se nastavilo podučavanje `temperature` (što razumski modeli
  odbacuju), koristi se `Llama-3.3-70B-Instruct` model putem Foundry Models endpointa. Dodana je nova
  `AZURE_INFERENCE_CHAT_MODEL` varijabla u `.env.copy`; bilježnice lekcija 04/06 `githubmodels` i
  primjer `06` `js-githubmodels` ju čitaju (povratak na `Llama-3.3-70B-Instruct`) i održavaju svoje
  demo-e `temperature`/`top_p`/`max_tokens`.
- **JavaScript / .NET primjeri ažurirani za GPT-5.** Uklonjeno `temperature`/`top_p`/`max_tokens` iz GPT-5
  primjera (`06` `recipe-app` TypeScript, `06` `.dib` .NET - što također uklanja `MaxOutputTokenCount`
  da rezultat rezoniranja ne bude skraćen). Primjer `06` `js-githubmodels` sada koristi Llamu da bi
  sačuvao demo temperature. `.dib` bilježi da je kombinacija `Azure.AI.Inference` + Llama model način za
  demonstraciju `Temperature` u .NET-u.
- Ostavili smo `gpt-4o-mini` / `gpt-5-mini` na mjestima gdje su točni: reference token-kodiranja `tiktoken`,
  liste dostupnosti model-kataloga i modela za govor u lekciji 02 (`gpt-4o-transcribe`).
- Primjeri za lekcije 20 (Mistral) i 21 (Meta) zadržavaju `temperature`/`max_tokens` jer ciljaju
  Mistral/Llama modele koji podržavaju te parametre.

## [2026-07-06] — Osvježenje modernizacije sadržaja

Široko osvježenje za održavanje točnosti kurikuluma za 2026: moderni API-ji, trenutni nazivi proizvoda i
nazivi modela, ažurirani vodiči za pružatelje usluga i novi alati za iskustvo programera.

### Dodano

- Sekcija **Microsoft Agent Framework** u lekciji `17-ai-agents` koja pokriva jedinstvene chat agente,
  alate/pozivanje funkcija, konfiguraciju Azure OpenAI (Microsoft Foundry) te višestruke agente
  i orkestraciju tijeka rada (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentiran kao offline / lokalni pružatelj usluga (uz Ollamu) u
  `00-course-setup/03-providers.md` i lekciji `19-slm`.
- **Tijekovi kontinuirane integracije**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (primjenjivano u održavanom `shared/`
    modulu, preporuke za ostali kurikulum), inspekcija ESLint i pytest zadatak.
  - `.github/workflows/security.yml` — CodeQL analiza (Python + JavaScript/TypeScript) i
    pregled ovisnosti na pull zahtjevima.
- **Testni set** pod `tests/` — 41 pytest test pokrivajući zajednički modul alata.
- **Azure OpenAI → Responses API vještina migracije** pod
  `.github/skills/azure-openai-to-responses/` koji vodi migraciju API-ja.

### Promijenjeno

- **Chat Completions API → Responses API** u svim Python i TypeScript chat primjerima
  (`client.responses.create(...)` → `response.output_text`), uključujući lekcije 04, 06, 07, 11,
  15 i 18, plus njihove README datoteke.
- **GitHub Models → Microsoft Foundry Models** širom teksta, linkova i primjera. GitHub Models
  se povlači krajem srpnja 2026; primjeri sada upućuju na Microsoft Foundry katalog modela i koriste
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` varijable okoline.
- **`.env.copy`, `AGENTS.md` i dokumentacija pružatelja usluga** ažurirani da odražavaju kako je Azure OpenAI sada dio
  Microsoft Foundryja, a zadana verzija API-ja podignuta na `2024-10-21`.
- **TypeScript primjeri** (lekcije 06, 07, 08, 11) migrirani s ukinute beta SDK `@azure/openai`
  na paket `openai` (chat aplikacije koriste Responses API; aplikacija za pretraživanje koristi
  embeddings klijenta).
- **.NET bilježnice** (`dotnet/*.dib`) standardizirane na `Azure.AI.OpenAI` **2.1.0**: lekcije 06 i 07
  koriste `ChatClient` API, lekcija 08 koristi `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), a
  lekcija 09 koristi `ImageClient` (`GenerateImage`) s `gpt-image-1`, zamjenjujući zastarjeli
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` iz `1.0.0-beta.9`.
- **Modernizacija naziva proizvoda**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcije 14, 16, 17) i "Bing" → **Microsoft Copilot** (lekcija 12), gdje se odnosi na
  postojeće proizvode.
- **DevContainer** (`.devcontainer/`) sada dolazi s ekstenzijama Pylance, Black, Ruff, ESLint, Prettier i Copilot,
  omogućava automatsko formatiranje pri spremanju i instalira `ruff`, `black`, `mypy` i `pytest` kako bi se CI
  provjere mogle reproducirati lokalno.
- **Generiranje slike** (lekcija 09) preporučuje `gpt-image-1` za Azure (Azure katalog je uklonio
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ažuriran da odražava dovršeni rad (migracija API-ja, CI,
  DevContainer, testovi) i trenutne činjenice (prijevodi se automatski proizvode pomoću
  Azure Co-op Translatora; Assistants API je zamijenjen Responses API-jem).

### Ispravljeno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sada vraća
  prazan niz za unos koji sadrži samo razmake umjesto da baci "prekratka" pogreška (dosljedno s
  slučajem `None`). Pronađeno i pokriveno novim setom testova.
- **Primjeri slika u lekciji 09** — ispravljene stvarne pogreške: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  i varijabla koja je zasjenila modul `openai`.
- **Bilježnica RAG iz lekcije 15** — popravljeno postavljanje klijenta, zamijenjen uklonjeni `DataFrame.append`
  s `pd.concat`, i modernizirano korištenje zastarjelog SDK-a.
- Zastarjela / povučena imena modela (`gpt-3.5-turbo`, `gpt-35-turbo`) zamijenjena s `gpt-4o-mini`
  u aktivnim primjerima; povijesni rezultati podešavanja u lekciji 18 sačuvani i označeni
  umjesto da su prepisani.

### Zastarjelo / Napomene

- **Primjeri Microsoft Foundry Modela** koji koriste `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — primjeri `githubmodels-*` i `js-githubmodels` te lekcije 19, 20,
  i 21 — ostaju na Model Inference API-ju, koji **ne** podržava Responses API. Oni su
  namjerno ostavljeni na tom SDK-u.
- `AzureOpenAI()` je namjerno zadržan gdje je još prikladan (ugrađivanja i generiranje slika),
  jer ti tijekovi rada nisu dio migracije na Responses API.
- Reference `text-embedding-ada-002` su zadržane gdje o njima ovisi unaprijed izračunati indeks ugradnji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->