# Pakeitimų žurnalas

Visas reikšmingas pakeitimas Generative AI for Beginners mokymų programoje dokumentuojamos šiame faile.

Šis formatas yra paremtas [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Kadangi tai yra
mokymų programa, o ne versijuojama programinė įranga, įrašai grupuojami pagal datą.

## [2026-07-16] — Turinys patvirtinimas + 9 pamokos atvaizdų turtas

### Pakeista

- **10 pamoka (mažai koduojamos AI programos):** atnaujintos dvi nebenaudojamos `docs.microsoft.com/powerapps/...` Dataverse
  nuorodos į dabartinę `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (patikrinta tiesiogiai).
- **17 pamoka (AI agentai):** atnaujintas pasenęs modelio pavyzdys (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o ir Llama 3.3`) ir laikinojo įgyvendinimo pavadinimas Agent Framework pavyzdyje
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Pagrindinis README.md:** pridėtas trūkstamas sekimo ID `?WT.mc_id=academic-105485-koreyst` prie
  *Microsoft for Startups* nuorodos.
- **9 pamokos atvaizdų turtas** atnaujintas naudojant `gpt-image` modelį: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` ir
  `images/startup.png` (redagavimo pavyzdžio prieš ir po pora buvo sukurta tikru
  `client.images.edit` kvietimu su generuota kauke).

### Patvirtinta

- Patikrinti README failai 1, 3, 5, 12, 14 ir 16 pamokoms — visi dabartiniai (teisingi Microsoft Foundry
  pavadinimai ir nuorodos); jokių pakeitimų nereikia.
- Atliktas pilnas markdown validavimas visiems 41 įrašytiems markdown failams (be vertimų) dėl
  pasenusių dokumentų kelių, `/en-us/` Microsoft lokalizacijų, pasenusį produktų/modelių pavadinimų,
  trūkstamų sekimo ID ir neveikiančių santykinių nuorodų/atvaizdų. Tik vienas trūkstamas *Microsoft for Startups*
  sekimo ID buvo reikšmingas; visi kiti žymėjimai patvirtinti klaidingais teigiamais (automatiškai generuotos
  vertimų nuorodos, komentarais uždaryti rezerviniai elementai ir trečių šalių `/en/` struktūriniai URL).

## [2026-07-15] — 9 pamokos (Atvaizdų programos) pertvarkymas GPT Atvaizdų modeliams

### Pakeista

- **Perrašyta 9 pamoka "Vaizdų generavimo programų kūrimas"** naudojant dabartinius **`gpt-image`**
  modelių šeimą (numatytasis **`gpt-image-2`**; taip pat GA `gpt-image-1.5` / `gpt-image-1-mini`), pakeičiant
  pasenusią DALL·E 2/3 turinį. Pagrindiniai pakeitimai:
  - `gpt-image` modeliai grąžina vaizdą kaip **base64 (`b64_json`)**, o ne URL. Atnaujinti visi pavyzdžiai,
    kad naudojamas `base64.b64decode(...)`, vietoje `url` siuntimo per `requests`.
  - Pakelta atvaizdų API versija į `2025-04-01-preview`.
  - Pakeista išgalvota "temperatūros" dalis (vaizdų modeliai nekontroliuoja `temperature`) ir DALL·E-2
    specifinės vaizdų **variacijų** dalies turinys į **vaizdų redagavimo** (kaukių / įdėjimo) skyrių.
  - Atnaujinti `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, abi
    užduočių užrašinės (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) ir .NET `.dib` užrašinė.

### Pašalinta

- Ištrinti pasenę `python/aoai-app-variation.py` ir `python/oai-app-variation.py` pavyzdžiai
  (`images.create_variation` yra tik DALL·E-2 ir nepalaikomas `gpt-image` modeliuose).
- Ištrinti 4 nenaudojami atvaizdų failai, susiję su pašalinta temperatūros palyginimo dalimi
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Pašalintas nereikalingas `requests` priklausomybės modulis iš pamokos Python pavyzdžių ir reikalavimų.

### Patvirtinta

- Vykdytas `aoai-app.py` pilnas testavimas su įdiegtu `gpt-image-1.5` modeliu, patvirtinant base64
  dekodavimo / saugojimo srautą, kuris sukuria PNG formatą. Užrašinės patvirtintos kaip teisingas JSON.

## [2026-07-14] — Numatyto modelio atnaujinimas + loginio modelio gairės

### Pakeista

- **Numatytasis pokalbių modelis `gpt-4o-mini` → `gpt-5-mini`** visoje mokymo programoje pavyzdžiuose,
  dokumentacijoje ir konfigūracijoje. Tai lėmė modelio gyvavimo ciklo statusas: Microsoft Foundry,
  `gpt-4o-mini` (pasitraukia 2026-10-01) ir visa `gpt-4.1` šeima (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pasitraukia 2026-10-14) yra **atsisakoma**, tuo tarpu **GPT-5 šeima
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) yra visuotinai prieinama** (pasitrauks 2027-02-06). Atnaujinta:
  - `.env.copy`, `00-course-setup/03-providers.md` (rekomenduojamas diegimas ir `az cognitiveservices`
    diegimo komandos), ir README failai pamokoms 04, 06, 07 ir 15.
  - Python pavyzdžiai 6 pamokoje (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) ir 8 pamokos scenarijai.
  - TypeScript / JavaScript pavyzdžiai 6, 7 ir 11 pamokose, bei .NET `.dib` užrašinės pamokoms
    6 ir 7.
  - Užduočių užrašinės 4, 6, 7 ir 11 pamokose (kodo ląstelės), taip pat `shared/python/api_utils.py`
    docstring pavyzdžiai.
- **Loginio modelio parametrų gairės (naujas).** `gpt-5-mini` yra *loginis* modelis: jis **nepalaiko**
  `temperature`/`top_p`, ir vietoje `max_tokens` naudoja `max_completion_tokens` (pokalbių baigimams) /
  `max_output_tokens` (Atsakymų API). Todėl:

  - Pašalinti `temperature`/`top_p`/`max_tokens` iš pavyzdžių, kurie dabar naudoja numatytąją reikšmę `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, pamoka 15 RAG README).
  - Pridėta pastaba **"Priežastis, kodėl apmąstymo modeliai nenaudoja `temperature`"** pamokoje 06, paaiškinanti, kad
    apmąstymo modeliai valdomi per **užklausų inžineriją + apmąstymo valdiklius**, o ne
    mėginių ėmimo parametrus, tuo tarpu `temperature`/`top_p` išlieka galiojantys neapmąstymo modeliuose
    (GPT-4.x, Mistral, Llama, Phi, atviri modeliai).
- **`gpt-5-mini` nenaudojamas derinimo pamokai (pamoka 18).** GPT-5 palaiko
  tik pastiprinamojo derinimo (RFT); pamokos 18 prižiūrimo derinimo (SFT) apžvalga naudoja
  `gpt-4.1-mini`, kuris palaiko SFT/DPO.
- **Temperatūros demonstracijos naudoja Llama modelį.** Norint tęsti `temperature` mokymą (kurį apmąstymo modeliai atmeta),
  naudojamas `Llama-3.3-70B-Instruct` modelis per Foundry Models galinį tašką. Pridėtas naujas
  `AZURE_INFERENCE_CHAT_MODEL` kintamasis `.env.copy` faile; pamokų 04/06 `githubmodels` užrašų knygelės ir
  `06` `js-githubmodels` pavyzdys jį skaito (grįžta į `Llama-3.3-70B-Instruct`) ir išlaiko jų
  `temperature`/`top_p`/`max_tokens` demonstracijas.
- **JS / .NET pavyzdžiai atnaujinti GPT-5.** Pašalinti `temperature`/`top_p`/`max_tokens` iš GPT-5
  pavyzdžių (`06` `recipe-app` TypeScript, `06` `.dib` .NET – kuris taip pat pakelia `MaxOutputTokenCount`,
  kad apmąstymo išvestis nebūtų sutrumpinta). `06` `js-githubmodels` pavyzdyje dabar naudojama Llama temperatūros demonstracijai.
  `.dib` užrašuose nurodoma, kad `Azure.AI.Inference` + Llama modelis yra būdas
  demonstracijai `Temperature` .NET aplinkoje.
- Palikti `gpt-4o-mini` / `gpt-5-mini` ten, kur jie išlieka teisingi: `tiktoken` žodžių kodavimo
  nuorodose, modelių katalogo prieinamumo sąrašuose ir pamokos 02 kalbos modeliuose (`gpt-4o-transcribe`).
- Pamokos 20 (Mistral) ir 21 (Meta) pavyzdžiai palaiko `temperature`/`max_tokens`, nes jie orientuoti į
  Mistral/Llama modelius, kurie palaiko šiuos parametrus.

## [2026-07-06] — Turinys atnaujintas pagal naujausias tendencijas

Platus atnaujinimas, siekiant išlaikyti mokymo programą tikslią 2026 metams: modernizuoti API, dabartinės produkto pavadinimai ir
modelių pavadinimai, atnaujintos paslaugų teikėjo gairės ir naujos kūrėjo patirties įrankių priemonės.

### Pridėta

- **Microsoft Agent Framework** skiltis pamokoje `17-ai-agents`, apimanti vieno pokalbio agentus,
  įrankius/funkcijų kvietimą, Azure OpenAI (Microsoft Foundry) konfigūraciją ir daugiaagentį
  darbo eigų valdymą (`SequentialBuilder` / `ConcurrentBuilder`).

- **Foundry Local** dokumentuota kaip neprisijungęs / įrenginyje esantis tiekėjas (kartu su Ollama) faile
  `00-course-setup/03-providers.md` ir pamokoje `19-slm`.
- **Nuolatinės integracijos darbo eigos**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (taikoma prižiūrimam `shared/`
    moduliui, rekomendacinis kitiems kurso dalių moduliams), rekomendacinis ESLint praeinamumas ir pytest užduotis.
  - `.github/workflows/security.yml` — CodeQL analizė (Python + JavaScript/TypeScript) ir
    priklausomybių peržiūra pull užklausose.
- **Testų rinkinys** kataloge `tests/` — 41 pytest testas, apimantis bendrą utilitinių modulių naudojimą.
- **Azure OpenAI → Responses API migracijos įgūdis** kataloge
  `.github/skills/azure-openai-to-responses/`, naudojamas vadovauti API migracijai.

### Pakeitimai

- **Chat Completions API → Responses API** visose Python ir TypeScript pokalbių pavyzdžiuose
  (`client.responses.create(...)` → `response.output_text`), įskaitant pamokas 04, 06, 07, 11,
  15 ir 18, taip pat jų README failus.
- **GitHub modeliai → Microsoft Foundry modeliai** tekste, nuorodose ir pavyzdžiuose. GitHub modeliai
  pensijuojami 2026 m. liepos pabaigoje; pavyzdžiai dabar nurodo Microsoft Foundry modelių katalogą ir naudoja
  aplinkos kintamuosius `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` ir tiekėjo dokumentacija** atnaujinti, kad atspindėtų, jog Azure OpenAI dabar yra
  Microsoft Foundry dalis, ir numatytoji API versija pakelta iki `2024-10-21`.
- **TypeScript pavyzdžiai** (pamokos 06, 07, 08, 11) perkelti nuo pasenusių `@azure/openai`
  beta SDK prie `openai` paketo (pokalbių programėlės naudoja Responses API; paieškos programa naudoja
  embeddings klientą).
- **.NET užrašų knygelės** (`dotnet/*.dib`) standartizuotos su `Azure.AI.OpenAI` **2.1.0**: pamokos 06 ir 07
  naudoja `ChatClient` API, pamoka 08 naudoja `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), o
  pamoka 09 naudoja `ImageClient` (`GenerateImage`) su `gpt-image-1`, pakeičiant senąjį
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` iš `1.0.0-beta.9`.
- **Produkto pavadinimo modernizavimas**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (pamokos 14, 16, 17) ir "Bing" → **Microsoft Copilot** (pamoka 12), ten, kur buvo kalbama apie
  esamus produktus.
- **DevContainer** (`.devcontainer/`) dabar siūlo Pylance, Black, Ruff, ESLint, Prettier ir Copilot
  plėtinius, įjungia formatavimą išsaugant ir įdiegia `ruff`, `black`, `mypy` bei `pytest`,
  kad CI patikrinimai būtų atkuriami lokaliai.
- **Vaizdų generavimas** (pamoka 09) rekomenduoja `gpt-image-1` Azure (Azure kataloge pašalintas
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** atnaujinta atspindinti atliktus darbus (API migracija, CI,
  DevContainer, testai) ir dabartines aplinkybes (vertimai generuojami automatiškai per
  Azure Co-op Translator; Assistants API pakeistas Responses API).

### Ištaisyta

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` dabar grąžina
  tuščią eilutę, jei įvestis susideda tik iš tarpelio, užuot išmetęs klaidą „per trumpa“ (atitinka
  `None` atvejį). Surasta ir padengta naujų testų rinkiniu.
- **9 pamokos paveikslėlių pavyzdžiai** — ištaisyti tikri klaidų atvejai: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  ir kintamasis, kuris užgožė `openai` modulį.
- **15 pamokos RAG sąsiuvinis** — sutvarkytas kliento nustatymas, pašalintas pašalintas `DataFrame.append`
  pakeistas `pd.concat`, atnaujinta senstelėjusi SDK naudojimo dalis.
- Nebenaudojamų / pasenusių modelių pavadinimai (`gpt-3.5-turbo`, `gpt-35-turbo`) pakeisti į `gpt-4o-mini`
  aktyviuose pavyzdžiuose; istoriniai fine-tuning rezultatai 18 pamokoje išlaikyti ir pažymėti,
  bet neperrašyti.

### Pasenę / Pastabos

- **Microsoft Foundry modelių pavyzdžiai**, naudojantys `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — `githubmodels-*` ir `js-githubmodels` pavyzdžiai bei 19, 20,
  ir 21 pamokos — išlieka su Model Inference API, kuris **nepalaiko** Responses API. Šie
  tyčia palikti ant to SDK.
- `AzureOpenAI()` tyčia išlaikytas ten, kur dar tinkamas (embeddingai ir paveikslėlių generavimas),
  nes šie procesai nėra dalis Responses API migracijos.
- `text-embedding-ada-002` nuorodos išlaikytos ten, kur iš anksto apskaičiuotas embedding indeksas nuo jų priklauso.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->