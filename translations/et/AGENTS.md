# AGENTS.md

## Projekti ülevaade

See hoidla sisaldab põhjalikku 21-õppeüksuse õppekava, mis õpetab generatiivse tehisintellekti põhialuseid ja rakenduste arendust. Kursus on mõeldud algajatele ja käsitleb kõike alates põhimõistetest kuni tootmiseks valmis rakenduste ehitamiseni.

**Põhilised tehnoloogiad:**
- Python 3.9+ koos teekidega: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js-ga ja teekidega: `openai` (Azure OpenAI v1 lõpp-punkti ja Responses API kaudu), `@azure-rest/ai-inference` (Microsoft Foundry mudelid)
- Azure OpenAI teenus, OpenAI API ja Microsoft Foundry mudelid (GitHubi mudelid lõpetavad tuge 2026. aasta juuli lõpus)
- Jupyter märkmikud interaktiivseks õppimiseks
- Dev konteinerid ühtlase arenduskeskkonna jaoks

**Hoidla struktuur:**
- 21 nummerdatud õppetükki (00–21) sisaldavad READMEd, koodinäiteid ja ülesandeid
- Mitmed teostused: Python, TypeScript ja mõnikord .NET näited
- Tõlkekataloog üle 40 keeleversiooniga
- Keskne konfiguratsioon `.env` failis (kasutage `.env.copy` mallina)

## Seadistamise käsud

### Hoidla algne seadistamine

```bash
# Klooni hoidla
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopeeri keskkonna mall
cp .env.copy .env
# Muuda .env oma API võtmete ja lõpp-punktidega
```

### Pythoni keskkonna seadistamine

```bash
# Loo virtuaalne keskkond
python3 -m venv venv

# Aktiveeri virtuaalne keskkond
# macOS/Linuxil:`
source venv/bin/activate
# Windowsil:
venv\Scripts\activate

# Paigalda sõltuvused
pip install -r requirements.txt
```

### Node.js/TypeScript seadistamine

```bash
# Paigalda juurdepõhised sõltuvused (dokumentatsiooni tööriistade jaoks)
npm install

# Üksikute õppetükkide TypeScripti näidete jaoks liigu konkreetse õppetüki kausta:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev konteineri seadistamine (soovitatav)

Hoidla sisaldab `.devcontainer` konfiguratsiooni GitHub Codespaces või VS Code Dev konteinerite jaoks:

1. Ava hoidla GitHub Codespaces’is või VS Code’is koos Dev konteinerite laiendusega
2. Dev konteiner installib automaatselt:
   - Pythoni sõltuvused `requirements.txt` failist
   - Käivitab post-create skripti (`.devcontainer/post-create.sh`)
   - Seadistab Jupyter tuuma

## Arendusprotsess

### Keskkonnamuutujad

Kõik õppetükid, mis vajavad API ligipääsu, kasutavad `.env` failis määratletud keskkonnamuutujaid:

- `OPENAI_API_KEY` - OpenAI API jaoks
- `AZURE_OPENAI_API_KEY` - Azure OpenAI jaoks Microsoft Foundry raames (Azure OpenAI Service on nüüd osa Microsoft Foundry’st: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI lõpp-punkti URL (Foundry ressursi lõpp-punkt)
- `AZURE_OPENAI_DEPLOYMENT` - Chat-komplekteerimise mudeli levitamisnimi (kursuse vaikimisi: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Manuste mudeli levitamisnimi (kursuse vaikimisi: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API versioon (vaikimisi: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face mudelite jaoks
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry mudelite lõpp-punkt (mitmekülgne mudelitelogistika)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry mudelite API võti (asendab lõpetava `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Loogiliselt mitte põhinev mudel (nt `Llama-3.3-70B-Instruct`), mida kasutavad `temperature` näited, kuna loogikamudelid ei toeta proovimise juhtnuppe

### Mudeli konventsioonid (tähtis)

- **Vaikimisi jutustamismudel on `gpt-5-mini`** - ajakohane, mitte aegunud **loogikamudel**. Alates 2026. aastast lõpetatakse vanemad temperatuuriga mini-mudelid (`gpt-4o-mini`, `gpt-4.1-mini`), seega standardiseerib õppekava GPT-5 perekonnale.
- **Loogikamudelid ei luba `temperature` ega `top_p`;** need kasutavad `max_output_tokens` (Responses API) / `max_completion_tokens` (chat-komplekteerimises) `max_tokens` asemel. Ärge lisage `temperature`/`top_p`/`max_tokens` näidetele, mis kutsuvad `gpt-5-mini`.
- **`temperature` demonstreerimiseks** kasutatakse **Llama** mudelit (`Llama-3.3-70B-Instruct`) Microsoft Foundry mudelite lõpp-punkti kaudu (`AZURE_INFERENCE_CHAT_MODEL`). Loogikamudeleid juhitakse prompt-insenerimise ja loogikakontrollidega, mitte proovimise juhtnuppudega.
- **Peenhäälestus (õppetund 18)** hoiab `gpt-4.1-mini`: GPT-5 toetab ainult tugevdatud peenhäälestust (RFT), mitte seal näidatud järelevalve all olevat peenhäälestust (SFT).
- Õppetunnid 20 (Mistral) ja 21 (Meta) hoiavad `temperature`/`max_tokens`, kuna nad kasutavad Mistral/Llama mudeleid, mis neid toetavad.

### Python näidete käivitamine

```bash
# Liigu õppetüki kataloogi
cd 06-text-generation-apps/python

# Käivita Python skript
python aoai-app.py
```

### TypeScript näidete käivitamine

```bash
# Liigu TypeScript rakenduse kausta
cd 06-text-generation-apps/typescript/recipe-app

# Koosta TypeScript kood
npm run build

# Käivita rakendus
npm start
```

### Jupyter märkmike käivitamine

```bash
# Käivita Jupyter hoidla juurkataloogis
jupyter notebook

# Või kasuta VS Code'i koos Jupyter laiendusega
```

### Töötamine erinevat tüüpi õppetükkidega

- **"Õpi" õppetunnid**: keskenduvad README.md dokumentatsioonile ja mõistetele
- **"Ehituse" õppetunnid**: sisaldavad töötavaid koodinäiteid Pythonis ja TypeScriptis
- Igal õppetunnil on README.md teooria, kood-samm-sammult ja videosisu lingid

## Koodi stiilijuhised

### Python

- Kasuta `python-dotenv` keskkonnamuutujate haldamiseks
- Impordi `openai` teek API interaktsioonide jaoks
- Kasuta `pylint` lintimiseks (mõned näited sisaldavad lihtsustamiseks `# pylint: disable=all`)
- Järgi PEP 8 nimetamiskonventsioone
- Hoia API võtmed `.env` failis, mitte kunagi koodis

### TypeScript

- Kasuta `dotenv` paketti keskkonnamuutujate jaoks
- TypeScript konfiguratsioon `tsconfig.json` iga rakenduse jaoks
- Kasuta `openai` paketti Azure OpenAI jaoks (suuna klient `/openai/v1/` lõpp-punkti ja kutsu `client.responses.create`); kasuta `@azure-rest/ai-inference` Microsoft Foundry mudelite jaoks
- Arendamisel kasuta `nodemon` automaatse taaskäivitusega
- Enne käivitamist ehita: `npm run build`, seejärel `npm start`

### Üldised konventsioonid

- Hoia koodinäited lihtsad ja õppeeesmärkidega
- Lisa kommentaarid, mis selgitavad peamisi mõisteid
- Iga õppetüki kood peaks olema iseseisev ja täidetav
- Kasuta järjepidevat nimetamist: `aoai-` egiidi all Azure OpenAI jaoks, `oai-` OpenAI API jaoks, `githubmodels-` Microsoft Foundry mudelite jaoks (pärandprefix GitHubi mudelite ajastust)

## Dokumentatsiooni juhised

### Markdown stiil

- Kõik URL-id peavad olema vormindatud `[tekst](../../url)` kujul ilma täiendavate tühikuteta
- Suhtelised lingid peavad algama `./` või `../`
- Kõik lingid Microsofti domeenidele peavad sisaldama jälgimis-ID-d: `?WT.mc_id=academic-105485-koreyst`
- Ärge kasutage riigipõhiseid keelekode URL-ides (vältige `/en-us/`)
- Pildid hoitakse `./images` kaustas kirjeldavate nimedega
- Kasutage failinimedes inglise tähti, numbreid ja kriipse

### Tõlke tugi

- Hoidla toetab 40+ keelt automatiseeritud GitHub Actions kaudu
- Tõlked asuvad kataloogis `translations/`
- Ärge esitage osalisi tõlkeid
- Masintõlked ei ole aktsepteeritud
- Tõlgitud pildid hoiustatakse kataloogis `translated_images/`

## Testimine ja valideerimine

### Enne esitamist tehtavad kontrollid

See hoidla kasutab valideerimiseks GitHub Actions’i. Enne PR-i esitamist:

1. **Kontrolli Markdown linke**:
   ```bash
   # validate-markdown.yml töövoog kontrollib:
   # - Katkised suhtelised teed
   # - Puuduvad jälgimis-ID-d teedel
   # - Puuduvad jälgimis-ID-d URL-idel
   # - URL-id riigi kohandusega
   # - Katkised välised URL-id
   ```

2. **Manuaalne testimine**:
   - Testi Python näiteid: aktiveeri venv ja käivita skriptid
   - Testi TypeScripti näiteid: `npm install`, `npm run build`, `npm start`
   - Veendu, et keskkonnamuutujad on õigesti seadistatud
   - Kontrolli API võtmete toimimist näidete juures

3. **Koodi näited**:
   - Veendu, et kogu kood töötab ilma vigadeta
   - Testi nii Azure OpenAI kui ka OpenAI API kasutamist, kus see on võimalik
   - Veendu, et näited töötavad seal, kus on Microsoft Foundry mudelite tugi

### Automaatseid teste ei ole

See on hariduslik hoidla, mis keskendub juhenditele ja näidetele. Üksusteste ega integratsiooniteste ei ole. Valideerimine põhineb peamiselt:
- Koodinäidete manuaalsel testimisel
- GitHub Actions’i kasutamisel Markdown valideerimiseks
- Haridusliku sisu kogukonna ülevaatel

## Pull Requesti juhised

### Enne esitamist

1. Testi koodi muudatusi nii Pythonis kui TypeScriptis, kui võimalik
2. Käivita Markdown valideerimine (käivitatakse automaatselt PR-i korral)
3. Veendu, et kõik Microsofti URL-id sisaldavad jälgimis-ID-sid
4. Kontrolli, et suhtelised lingid on kehtivad
5. Veendu, et pildid on õigesti viidatud

### PR pealkirja formaat

- Kasuta kirjeldavaid pealkirju: `[Lesson 06] Paranda Python näite kirjaviga` või `Uuenda README-d õppetunni 08 jaoks`
- Viita vajadusel arvetele: `Fixes #123`

### PR kirjeldus

- Selgita, mida muudeti ja miks
- Lisa siduvad arved
- Koodi muudatuste korral täpsusta, millised näited testiti
- Tõlke PR-ide puhul lisa kõik failid täielikuks tõlkeks

### Panusnõuded

- Allkirjasta Microsoft CLA (automaatne esimesel PR-il)
- Tee fork oma kontole enne muudatuste tegemist
- Üks PR ühe loogilise muudatuse kohta (ära ühenda mittevastavaid parandusi)
- Hoia PR-id fookustatud ja võimaluse korral väikesed

## Levinumad töövood

### Uue koodinäite lisamine

1. Liigu õige õppetüki kataloogi
2. Loo näide alamkataloogi `python/` või `typescript/` all
3. Järgi nimetamiskonventsiooni: `{provider}-{example-name}.{py|ts|js}`
4. Testi tegelike API volitustega
5. Dokumenteeri kõik uued keskkonnamuutujad õppetüki README-s

### Dokumentatsiooni uuendamine

1. Muuda README.md faili õppetüki kataloogis
2. Järgi Markdown juhiseid (jälgimis-ID-d, suhtelised lingid)
3. Tõlked uuenevad GitHub Actions’iga automaatselt (ära toimetage käsitsi)
4. Testi, et kõik lingid on kehtivad

### Töötamine Dev konteineritega

1. Hoidla sisaldab `.devcontainer/devcontainer.json` faili
2. Post-create skript paigaldab Pythoni sõltuvused automaatselt
3. Pythonile ja Jupytrile on laiendused eelkonfigureeritud
4. Keskkond põhineb `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Väljastamine ja avaldamine

See on õppehoidla - siin pole väljastamise protsessi. Õppekava tarbitakse:

1. **GitHubi hoidla**: otsepääs koodile ja dokumentatsioonile
2. **GitHub Codespaces**: kohene arenduskeskkond eelseadistusega
3. **Microsoft Learn**: sisu võib jõuda ametlikule õppimisplatvormile
4. **docsify**: dokumentatsioonisait ehitatud Markdownist (vaata `docsifytopdf.js` ja `package.json`)

### Dokumentatsiooni saidi ehitamine

```bash
# Genereeri PDF dokumentatsioonist (kui vajalik)
npm run convert
```

## Tõrkeotsing

### Levinud probleemid

**Pythoni importimisvead**:
- Veendu, et virtuaal keskkond on aktiveeritud
- Käivita `pip install -r requirements.txt`
- Kontrolli Pythoni versiooni 3.9+ peal

**TypeScripti ehitusvead**:
- Käivita `npm install` vastavas rakenduse kataloogis
- Kontrolli, et Node.js versioon on sobiv
- Vajadusel kustuta `node_modules` ja paigalda uuesti

**API autentimisvead**:
- Kontrolli, et `.env` fail on olemas ja õigesti täidetud
- Kontrolli API võtmete kehtivust ja aegumata olekut
- Veendu, et lõpp-punkti URL-id on sinu regiooni jaoks õiged

**Puuduvad keskkonnamuutujad**:
- Kopeeri `.env.copy` nimega `.env`
- Täida kõik vajalikud väärtused aktiivse õppetüki jaoks
- Taaskäivita rakendus peale `.env` uuendamist

## Lisavahendid

- [Kursuse seadistamise juhend](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Panustamise juhised](./CONTRIBUTING.md)
- [Käitumiskoodeks](./CODE_OF_CONDUCT.md)
- [Turvapoliitika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Täpsemate koodinäidete kogu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekti spetsiifilised märkused

- See on **hariduslik hoidla**, mis keskendub õppimisele, mitte tootmiskoodile
- Näited on teadlikult lihtsad ja keskenduvad kontseptsioonide õpetamisele
- Koodikvaliteet on tasakaalus haridusliku selgusega
- Iga õppetükk on iseseisev ja võimalik sõltumatult lõpetada
- Hoidla toetab mitut API pakkujat: Azure OpenAI, OpenAI, Microsoft Foundry mudelid ja võrguühenduseta pakkujad nagu Foundry Local ja Ollama
- Sisu on mitmekeelne automatiseeritud tõlketöövoogudega
- Aktiivne kogukond Discordis küsimuste ja toe jaoks

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->