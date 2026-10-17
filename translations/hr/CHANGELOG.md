# Dnevnik promjena

Sve značajne promjene u nastavnom planu Generative AI for Beginners dokumentirane su u ovoj datoteci.

Format je temeljen na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Budući da se radi o
nastavnom planu, a ne o programskoj paketu s verzijama, unosi su grupirani prema datumu.

## [2026-07-16] — Validacija sadržaja + Slikovni resursi za Lekciju 09

### Promijenjeno

- **Lekcija 10 (AI aplikacije s malo koda):** ažurirane su dvije zastarjele `docs.microsoft.com/powerapps/...` Dataverse
  poveznice na trenutne `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (provjereno uživo).
- **Lekcija 17 (AI agenti):** moderniziran zastarjeli primjer modela (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) i naziv za postavljanje u uzorku Agent Frameworka
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Korijenski `README.md`:** dodan nedostajući `?WT.mc_id=academic-105485-koreyst` ID za praćenje u
  poveznici *Microsoft for Startups*.
- **Slikovni resursi za Lekciju 09** ponovno su generirani s modelom `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, i
  `images/startup.png` (primjer uređivanja prije i nakon proizveden je stvarnim
  `client.images.edit` pozivom s generiranom maskom).

### Validirano

- Pregledani README-ovi za lekcije 01, 03, 05, 12, 14 i 16 — svi ažurirani (točni Microsoft Foundry
  nazivi i poveznice); nije bilo potrebno mijenjati ništa.
- Pokrenuta je potpuna provjera markdowna kroz svih 41 markdown datoteka u repozitoriju (izuzimajući prijevode),
  tražeći zastarjele putanje dokumenata, `/en-us/` Microsoft lokalitete, zastarjele nazive proizvoda/modela,
  nedostajuće ID-ove za praćenje i neispravne relativne poveznice/slike. Jedini problem bio je manjak ID-a za praćenje u
  *Microsoft for Startups* poveznici; svi ostali su potvrđeni kao lažni alarmi (automatski generirane poveznice za prijevode,
  privremeni komentari i strukturalni URL-ovi trećih strana `/en/`).

## [2026-07-15] — Preprava Lekcije 09 (Aplikacije za slike) za GPT slikovne modele

### Promijenjeno

- **Prepravljena lekcija 09 "Izgradnja aplikacija za generiranje slika"** oko trenutačne obitelji modela **`gpt-image`**
  (zadani **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` također GA), zamijenivši
  zastarjeli sadržaj za DALL·E 2/3. Ključne ispravke:
  - `gpt-image` modeli vraćaju sliku kao **base64 (`b64_json`)**, a ne URL. Ažurirani su svi primjeri za
    `base64.b64decode(...)` umjesto preuzimanja `url` s `requests`.
  - Povišena je verzija slikovnog API-ja na `2025-04-01-preview`.
  - Zamijenjen je izmišljeni odjeljak "temperature" (slikovni modeli ne koriste `temperature`) i
    sadržaj slikovnih **varijacija** koji je bio samo za DALL·E-2 s odjeljkom za **uređivanje slika** (maskiranje / inpainting).
  - Ažurirani su `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    zadatka u bilježnicama (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) i .NET bilježnica `.dib`.

### Uklonjeno

- Izbrisani su zastarjeli primjeri `python/aoai-app-variation.py` i `python/oai-app-variation.py`
  (`images.create_variation` je samo za DALL·E-2 i nije podržan u `gpt-image`).
- Izbrisano je 4 napuštena slikovna resursa vezana uz uklonjeni odjeljak usporedbe temperature
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Uklonjena je nepotrebna ovisnost `requests` iz Python primjera i zahtjeva u lekciji.

### Validirano

- Pokrenut je `aoai-app.py` end-to-end test na raspoređenom modelu `gpt-image-1.5` i potvrđeno da base64
  dekodiranje/spremanje proizvodi PNG. Bilježnice su potvrđene kao valjani JSON.

## [2026-07-14] — Ažuriranje zadane verzije modela + Smjernice za model zaključivanja

### Promijenjeno

- **Zadani chat model `gpt-4o-mini` → `gpt-5-mini`** kroz sve izvršne primjere u nastavnom planu,
  dokumentaciju i konfiguraciju. Ovo je rezultat životnog ciklusa modela: na Microsoft Foundryju,
  `gpt-4o-mini` (povlači se 2026-10-01) i cijela obitelj `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, povlače se 2026-10-14) se povlače, dok je obitelj **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) općenito dostupna** (povlačenje 2027-02-06). Ažurirano:
  - `.env.copy`, `00-course-setup/03-providers.md` (preporučene naredbe za raspoređivanje i `az cognitiveservices`),
    i README-ovi za lekcije 04, 06, 07 i 15.
  - Python primjeri u lekciji 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) te skripte lekcije 08.
  - TypeScript / JavaScript primjeri u lekcijama 06, 07 i 11, te `.dib` .NET bilježnice za
    lekcije 06 i 07.
  - Zadani bilježnice u lekcijama 04, 06, 07 i 11 (kod ćelije), plus `shared/python/api_utils.py`
    primjeri docstringova.
- **Smjernice za parametre modela zaključivanja (novo).** `gpt-5-mini` je *model zaključivanja*: on **ne**
  podržava `temperature`/`top_p`, i koristi `max_completion_tokens` (chat dovršenje) /
  `max_output_tokens` (Responses API) umjesto `max_tokens`. Sukladno tome:
  - Uklonjeno `temperature`/`top_p`/`max_tokens` iz primjera koji sada podrazumijevaju `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcija 15 RAG README).
  - Dodana je **bilješka "Razumski modeli ne koriste `temperature`"** u lekciju 06, objašnjavajući da
    se razumski modeli usmjeravaju s **prompt inženjeringom + kontrolama razmišljanja** umjesto
    kontrola uzorkovanja, dok su `temperature`/`top_p` i dalje valjani za modele koji nisu razumski
    (GPT-4.x, Mistral, Llama, Phi, otvoreni modeli).
- **`gpt-5-mini` se ne koristi za tutorijal fino podešavanje (lekcija 18).** GPT-5 podržava samo
  pojačano fino podešavanje (RFT); vodič kroz lekciju 18 za nadzirano fino podešavanje (SFT) zadržava
  `gpt-4.1-mini`, koji podržava SFT/DPO.
- **Demo s temperaturom koristi Llama model.** Da bi se nastavilo podučavanje `temperature` (koje razumski modeli
  odbacuju), koristi se `Llama-3.3-70B-Instruct` model putem Foundry Models krajnje točke. Dodana je nova
  `AZURE_INFERENCE_CHAT_MODEL` varijabla u `.env.copy`; lekcije 04/06 `githubmodels` bilježnice i
  `06` `js-githubmodels` primjer ih čitaju (uz povratak na `Llama-3.3-70B-Instruct`) i zadržavaju svoje
  `temperature`/`top_p`/`max_tokens` demonstracije.
- **JS / .NET primjeri ažurirani za GPT-5.** Uklonjeno `temperature`/`top_p`/`max_tokens` iz GPT-5
  primjera (`06` `recipe-app` TypeScript, `06` `.dib` .NET - što također rješava problem `MaxOutputTokenCount`
  tako da se izlaz razmišljanja ne skraćuje). `06` `js-githubmodels` primjer sada koristi Llama za održavanje
  demo s temperaturom. `.dib` napominje da je `Azure.AI.Inference` + Llama model način
  demonstriranja `Temperature` u .NET.
- Ostavljen je `gpt-4o-mini` / `gpt-5-mini` tamo gdje su točni: reference na kodiranje tokena `tiktoken`,
  liste dostupnosti kataloga modela i modeli govora u lekciji 02 (`gpt-4o-transcribe`).
- Primjeri za lekciju 20 (Mistral) i 21 (Meta) zadržavaju `temperature`/`max_tokens` jer ciljaju
  Mistral/Llama modele, koji podržavaju te parametre.

## [2026-07-06] — Osvježenje modernizacije sadržaja

Opsežno osvježenje za održavanje točnosti kurikuluma za 2026: moderni API-ji, trenutna imena proizvoda i
imena modela, ažurirane smjernice davatelja i novi alati za razvojničko iskustvo.

### Dodano

- Sekcija **Microsoft Agent Framework** u lekciji `17-ai-agents` obuhvaća pojedinačne chat agente,
  alate/pozivanje funkcija, Azure OpenAI (Microsoft Foundry) konfiguraciju i orkestraciju višestrukih
  agenata (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentiran kao offline / lokalni davatelj (uz Ollama) u
  `00-course-setup/03-providers.md` i lekciji `19-slm`.
- **Radni tijekovi kontinuirane integracije**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (primijenjeno na održavani `shared/`
    modul, savjetodavno na ostatku kurikuluma), savjetodavni ESLint pregled i pytest zadatak.
  - `.github/workflows/security.yml` — CodeQL analiza (Python + JavaScript/TypeScript) i
    pregled ovisnosti na pull zahtjevima.
- **Testni paket** pod `tests/` — 41 pytest testova koji pokrivaju zajednički modul utiliteta.
- **Vještina migracije s Azure OpenAI na Responses API** pod
  `.github/skills/azure-openai-to-responses/` koji služi za vođenje migracije API-ja.

### Promijenjeno

- **Chat Completions API → Responses API** u svim Python i TypeScript chat primjerima
  (`client.responses.create(...)` → `response.output_text`), uključujući lekcije 04, 06, 07, 11,
  15 i 18, kao i njihove README datoteke.
- **GitHub Models → Microsoft Foundry Models** u cijelom tekstu, linkovima i primjerima. GitHub Models
  odlazi iz upotrebe krajem srpnja 2026; primjeri sada upućuju na katalog modela Microsoft Foundry i koriste
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` varijable okruženja.
- **`.env.copy`, `AGENTS.md` i dokumentacija davatelja** ažurirani su kako bi reflektirali da je Azure OpenAI sada dio
  Microsoft Foundry, i zadana verzija API-ja podignuta na `2024-10-21`.
- **TypeScript primjeri** (lekcije 06, 07, 08, 11) migrirani s zastarjelog beta SDK-a `@azure/openai`
  na paket `openai` (chat aplikacije koriste Responses API; aplikacija za pretraživanje koristi
  embeddings klijent).
- **.NET bilježnice** (`dotnet/*.dib`) standardizirane na `Azure.AI.OpenAI` **2.1.0**: lekcije 06 i 07
  koriste `ChatClient` API, lekcija 08 koristi `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), a
  lekcija 09 koristi `ImageClient` (`GenerateImage`) s `gpt-image-1`, zamjenjujući zastarjeli
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` iz `1.0.0-beta.9`.
- **Modernizacija imena proizvoda**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcije 14, 16, 17) i "Bing" → **Microsoft Copilot** (lekcija 12), gdje se odnosi na
  aktualne proizvode.
- **DevContainer** (`.devcontainer/`) sada dolazi s Pylance, Black, Ruff, ESLint, Prettier i Copilot
  ekstenzijama, omogućuje automatsko formatiranje pri spremanju i instalira `ruff`, `black`, `mypy` i `pytest` kako bi se CI
  provjere mogle reproducirati lokalno.
- **Generiranje slika** (lekcija 09) preporučuje `gpt-image-1` za Azure (Azure katalog je uklonio
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ažurirano kako bi odražavalo dovršeni rad (migracija API-ja, CI,
  DevContainer, testovi) i trenutne činjenice (prijevodi se automatski proizvode putem
  Azure Co-op Translatora; Assistants API je zamijenjen Responses API-jem).

### Ispravljeno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sada vraća
  prazan niz za unos koji sadrži samo razmake, umjesto da podiže pogrešku "prekratak" (u skladu s
  slučajem `None`). Pronađeno i pokriveno novim testnim paketom.
- **Primjeri slika iz lekcije 09** — ispravljene stvarne greške: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  i varijabla koja je zasjenjivala modul `openai`.
- **Bilježnica RAG lekcije 15** — popravljeno postavljanje klijenta, zamijenjen uklonjeni `DataFrame.append`
  s `pd.concat`, i modernizirana uporaba zastarjelog SDK-a.
- Zastarjeli / povučeni nazivi modela (`gpt-3.5-turbo`, `gpt-35-turbo`) zamijenjeni s `gpt-4o-mini`
  u aktivnim primjerima; povijesni rezultati finog podešavanja u lekciji 18 su sačuvani i označeni
  umjesto da su prepisani.

### Zastarjelo / Bilješke

- **Primjeri Microsoft Foundry modela** koji koriste `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — primjeri `githubmodels-*` i `js-githubmodels` te lekcije 19, 20,
  i 21 — ostaju na Model Inference API-ju, koji **ne podržava** Responses API. Namjerno su
  ostavljeni na tom SDK-ju.
- `AzureOpenAI()` je namjerno zadržan gdje je još prikladan (ugradnje i generiranje slika),
  jer ti radni tijekovi nisu dio migracije na Responses API.
- `text-embedding-ada-002` reference su zadržane gdje o njima ovisi unaprijed izračunati indeks ugrađivanja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->