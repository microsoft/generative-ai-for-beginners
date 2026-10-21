# Muudatuste logi

Kõik olulised muudatused Generative AI for Beginners õppekavas on dokumenteeritud selles failis.

Vorming põhineb [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) vormingul. Kuna see on õppematerjal, mitte versioonihalduses tarkvarapakett, on sissekanded rühmitatud kuupäeva järgi.


## [2026-07-16] — Sisu valideerimine + Õppetüki 09 pildifailid

### Muudetud

- **Õppetund 10 (madal-koodiga tehisintellekti rakendused):** uuendatud kaks pensionile jäänud `docs.microsoft.com/powerapps/...` Dataverse
  linki kehtiva `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` juurde
  (elusolevalt kontrollitud).
- **Õppetund 17 (tehisintellekti agendid):** moderniseeritud aegunud mudelinäide (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) ja kohatäitepaigutuse nimi Agent Framework näites
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** lisatud puuduolev `?WT.mc_id=academic-105485-koreyst` jälgimise ID
  *Microsoft for Startups* lingile.
- **Õppetunni 09 pildivarad** genereeritud uuesti mudeliga `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, ja
  `images/startup.png` (redigeerimise näite enne/pärast paar loodi reaalse
  `client.images.edit` kõne abil koos genereeritud maskiga).

### Kinnitatud

- Vaadatud üle READMEd õppetundide 01, 03, 05, 12, 14 ja 16 jaoks — kõik ajakohased (õiged Microsoft Foundry
  nimetused ja lingid); muudatusi ei olnud vaja.
- Läbitud täielik markdowni valideerimine kõigi 41 repo-sisese markdowni faili (välja arvatud tõlked) jaoks
  vananenud dokumentide teede, `/en-us/` Microsofti keeleversioonide,
  aegunud tootemudelite nimede, puuduolevate jälgimis-IDde ja vigaste suhteliste linkide/piltide osas.
  Tegevust nõudis vaid üksik *Microsoft for Startups* jälgimis-ID puudumine; kõik teised hoiatused osutusid vääradeks positiivideks (automaatselt genereeritud tõlkelingid,
  kommentaaridest välja jäetud kohatäited ja kolmandate osapoolte `/en/` struktureeritud URL-id).

## [2026-07-15] — Õppetund 09 (pildirakendused) ümberkirjutus GPT pildimudelite jaoks

### Muudetud

- **Kirjutasin ümber õppetunni 09 "Pildigeneratsiooni rakenduste loomine"** praeguse **`gpt-image`**
  mudelifamiliaari ümber (vaikimisi **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` samuti GA), asendades
  vananenud DALL·E 2/3 sisu. Põhikorrektsioonid:
  - `gpt-image` mudelid tagastavad pildi kui **base64 (`b64_json`)**, mitte URL-i. Uuendatud kõik näited, et
    kasutada `base64.b64decode(...)`, mitte `url` allalaadimist koos `requests`.
  - Pildi API versioon viidud `2025-04-01-preview`.
  - Asendatud väljamõeldud "temperatuuri" osa (pildimudelid ei kasuta `temperature`) ning
    ainult DALL·E-2 pildierinevuste sisu **pildi redigeerimise** (maskimine / täitmine) osaga.
  - Uuendatud `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, nii
    ülesande märkmikud (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), kui ka .NET `.dib` märkmik.

### Eemaldatud

- Kustutatud aegunud `python/aoai-app-variation.py` ja `python/oai-app-variation.py` näited
  (`images.create_variation` on ainult DALL·E-2 jaoks ja seda ei toeta `gpt-image`).
- Kustutatud 4 kasutamata jäänud pildiressurssi, mis olid seotud eemaldatud temperatuuri võrdluse osaga
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Eemaldatud tarbetu `requests` sõltuvus õppetunni Pythoni näidetes ja nõuetes.

### Kinnitatud

- Käidud kogu`aoai-app.py` voog läbi juurutatud `gpt-image-1.5` mudeli peal ja kinnitatud, et base64 dekodeerimine/salvestamine toodab PNG faili. Märkmikud kinnitatud kehtivaks JSON-iks.


## [2026-07-14] — Vaikimisi mudeli uuendus + mõttemudeli juhendamine

### Muutunud

- **Vaikimisi vestlusmudel `gpt-4o-mini` → `gpt-5-mini`** kogu õppekava käivitatavates näidetes,
  dokumentatsioonis ja konfiguratsioonis. Selle tingis mudeli elutsükli staatus: Microsoft Foundry's,
  `gpt-4o-mini` (pensionile jääb 2026-10-01) ja kogu `gpt-4.1` perekond (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pensionile jäävad 2026-10-14) on **vähendamas toetust**, samas kui **GPT-5 perekond
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) on üldiselt saadaval** (vähendab toetust alates 2027-02-06). Uuendatud:
  - `.env.copy`, `00-course-setup/03-providers.md` (soovitatud juurutamise ja `az cognitiveservices`
    juurutamiskäsklused), ning õppetundide 04, 06, 07 ja 15 LUGEGE MINU KOHTA faile.
  - Pythoni näited õppetunnis 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) ja õppetunni 08 skriptid.
  - TypeScript / JavaScript näited õppetundides 06, 07 ja 11, ning `.dib` .NET märkmikud
    õppetundidele 06 ja 07.
  - Kodutöö märkmikud õppetundides 04, 06, 07 ja 11 (koodirakud), pluss `shared/python/api_utils.py`
    dokstringi näited.
- **Põhjenduspõhise mudeli parameetrite juhend (uus).** `gpt-5-mini` on *põhjendav* mudel: see ei toeta
  `temperature`/`top_p`, ning kasutab `max_completion_tokens` (vestluse lõpetused) /
  `max_output_tokens` (Responses API) asemel `max_tokens`. Vastavalt:
  - Eemaldatud `temperature`/`top_p`/`max_tokens` näidetest, mis nüüd vaikimisi kasutavad `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, õppetund 15 RAG README).
  - Lisatud õppetunni 06 juurde **"Põhjendamismudelid ei kasuta `temperature`"** märkus, mis selgitab,
    et põhjendamismudeleid juhitakse **põhjusinsenerluse + põhjendusjuhtimisega** mitte proovi valikuga,
    samas kui `temperature`/`top_p` kehtivad endiselt mitte-põhjendamismudelitel
    (GPT-4.x, Mistral, Llama, Phi, avatud mudelid).
- **`gpt-5-mini` ei kasutata peenhäälestamise juhendis (õppetund 18).** GPT-5 toetab ainult
  tugevdusõppe peenhäälestamist (RFT); õppetunni 18 juhendis hoitakse alles
  `gpt-4.1-mini`, mis toetab SFT/DPO-d.
- **Temperatuuri demo puhul kasutatakse Llama mudelit.** `temperature` õpetamise jätkamiseks (mida põhjendamismudelid
  ei aktsepteeri), kasutatakse Foundry mudelite otsapunkti kaudu `Llama-3.3-70B-Instruct` mudelit. Lisatud uus
  `AZURE_INFERENCE_CHAT_MODEL` muutuja `.env.copy`; õppetundide 04/06 `githubmodels` märkmikud ja
  `06` `js-githubmodels` näidis loevad seda (koos varuvalikuga `Llama-3.3-70B-Instruct`) ja säilitavad oma
  `temperature`/`top_p`/`max_tokens` demo.
- **JS / .NET näited on uuendatud GPT-5 jaoks.** Eemaldatud `temperature`/`top_p`/`max_tokens` GPT-5
  näidetest (`06` `recipe-app` TypeScript, `06` `.dib` .NET - mis tõstab samuti `MaxOutputTokenCount`
  et põhjendusväljund ei lühendataks). `06` `js-githubmodels` näide kasutab nüüd Llama mudelit, et säilitada oma
  temperatuuri demo. `.dib` märkused, et `Azure.AI.Inference` + Llama mudel on viis demonstreerida
  `Temperature` .NET keskkonnas.
- Vasakpoolne `gpt-4o-mini` / `gpt-5-mini` kohas, kus need jäävad täpselt õigeks: `tiktoken` token-kodeerimise
  viited, mudeli kataloogi saadavuse nimekirjad ja õppetund 02 kõnemudelid (`gpt-4o-transcribe`).
- Õppetund 20 (Mistral) ja 21 (Meta) näited hoiavad `temperature`/`max_tokens`, kuna need sihivad
  Mistral/Llama mudeleid, mis toetavad neid parameetreid.

## [2026-07-06] — Sisu uuenduse värskendus

Lai värskendus, et hoida õppekava täpne aastaks 2026: kaasaegsed API-d, praegused tootetooted ja
mudelinimed, värskendatud pakkujate juhised ja uus arendajakogemuse tööriistad.

### Lisatud

- **Microsoft Agent Framework** jaotis õppetunnis `17-ai-agents`, mis käsitleb ühekordseid vestlusagente,
  tööriistu/funktsioonide kutsumist, Azure OpenAI (Microsoft Foundry) konfiguratsiooni ja mitmeagendi
  töövoo korraldust (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumenteeritud kui võrguühenduseta / seadmesisene pakkuja (koos Ollamaga) aadressil
  `00-course-setup/03-providers.md` ja õppetunnis `19-slm`.
- **Jooksvad integreerimiste töövood**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (jõustatud hooldatud `shared/` moodulil,
    soovitused kogu ülejäänud õppekavas), nõustav ESLint kontroll ja pytest töö.
  - `.github/workflows/security.yml` — CodeQL analüüs (Python + JavaScript/TypeScript) ja
    sõltuvuste ülevaatus tõmbepäringutel.
- **Testikomplekt** aadressil `tests/` — 41 pytest testi, mis katavad jagatud abimoodulit.
- **Azure OpenAI → Responses API migratsiooni oskus** aadressil
  `.github/skills/azure-openai-to-responses/`, mida kasutatakse API migratsiooni suunamiseks.

### Muudetud

- **Chat Completions API → Responses API** kõigis Python ja TypeScript vestlusnäidetes
  (`client.responses.create(...)` → `response.output_text`), sh õppetundides 04, 06, 07, 11,
  15 ja 18 ning nende README-failides.
- **GitHub Models → Microsoft Foundry Models** kogu teksti, linkide ja näidete ulatuses. GitHub Models
  lõpetab tegevuse 2026. aasta juuli lõpus; näited suunavad nüüd Microsoft Foundry mudelikataloogi ja kasutavad
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` keskkonnamuutujaid.
- **`.env.copy`, `AGENTS.md` ja pakkuja dokumentatsioonid** ajakohastatud, et kajastada, et Azure OpenAI on nüüd osa
  Microsoft Foundry'st ning vaikimisi API versioon on tõstetud `2024-10-21`-le.
- **TypeScript näited** (õppetunnid 06, 07, 08, 11) on migreeritud pensionile läinud `@azure/openai`
  beeta SDK-st paketile `openai` (vestlusrakendused kasutavad Responses API-d; otsingurakendus kasutab
  embeddingu klienti).
- **.NET märkmikud** (`dotnet/*.dib`) on standardiseeritud `Azure.AI.OpenAI` versioonile **2.1.0**: õppetunnid 06 ja 07
  kasutavad `ChatClient` API-d, õppetund 08 kasutab `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`) ja
  õppetund 09 kasutab `ImageClient` (`GenerateImage`) koos `gpt-image-1`, asendades pärandatud
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` aadressil `1.0.0-beta.9`.
- **Tootenime uuendus**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (õppetunnid 14, 16, 17) ja "Bing" → **Microsoft Copilot** (õppetund 12), kus need viitasid
  praegustele toodetele.
- **DevContainer** (`.devcontainer/`) sisaldab nüüd Pylance'i, Blacki, Rufi, ESLinti, Prettierit ja Copilot'i
  laiendusi, lubab salvestamisel automaatse vormindamise ja installeerib `ruff`, `black`, `mypy` ja `pytest`,
  et CI kontrollid oleksid kohalikult taasesitatavad.
- **Pildigenereerimine** (õppetund 09) soovitab Azure jaoks `gpt-image-1` (Azure kataloog on eemaldanud
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** uuendatud, et kajastada tehtud tööd (API migratsioon, CI,
  DevContainer, testid) ja praeguseid fakte (tõlked genereeritakse automaatselt Azure Co-op Translatori poolt;
  Assistants API on asendatud Responses API-ga).

### Parandatud

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` tagastab nüüd tühja stringi ainult tühikut sisaldava sisendi puhul, selle asemel et visata "liiga lühike" viga (kooskõlas
  `None` juhtumiga). Leitud ja kaetud uue testikomplektiga.
- **Õppetunni 09 pildinäited** — parandatud päris vead: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  ja muutuja, mis varjas `openai` moodulit.
- **Õppetunni 15 RAG märkmik** — parandatud kliendi seadistus, asendatud eemaldatud `DataFrame.append`
  `pd.concat`-ga ja moderniseeritud pärand SDK kasutus.
- Välja arvatud / pensionile jäänud mudelinimed (`gpt-3.5-turbo`, `gpt-35-turbo`) asendatud aktiivsetes näidetes `gpt-4o-mini`-ga;
  ajaloolised peenhäälestuse väljundid õppetunnis 18 säilitati ja märgistati,
  mitte ümber kirjutatud.




- **Microsoft Foundry mudelite näited**, mis kasutavad `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK-d (`client.complete()`) — `githubmodels-*` ja `js-githubmodels` näited ning 19., 20.,
  ja 21. õppetund jäävad Model Inference API-le, mis **ei toeta** Responses API-d. Need jäävadki
  tahtlikult sellele SDK-le.
- `AzureOpenAI()` säilitatakse tahtlikult seal, kus see endiselt sobib (manused ja pildi loomine),
  kuna need töövood ei ole Responses API migratsiooni osa.
- `text-embedding-ada-002` viited jäetakse alles seal, kus arvutatud manusesisendindeks sõltub neist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->