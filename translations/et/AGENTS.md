# AGENTS.md

## Projekti Ülevaade

See hoidla sisaldab põhjalikku 21-peatükilist õppekava, mis õpetab Generatiivse tehisintellekti põhitõdesid ja rakenduste arendamist. Kursus on mõeldud algajatele ja käsitleb kõike alates põhimõistetest kuni tootmisvalmis rakenduste ehitamiseni.

**Peamised Tehnoloogiad:**
- Python 3.9+ koos teekidega: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js-ga ja teekidega: `openai` (Azure OpenAI läbi v1 lõpp-punkti + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry mudelid)
- Azure OpenAI teenus, OpenAI API ja Microsoft Foundry mudelid (GitHub Models lõpetab juuli 2026 lõpus)
- Jupyteri sülearvutid interaktiivseks õppimiseks
- Dev Containerid ühtlase arenduskeskkonna tagamiseks

**Hoidla Struktuur:**
- 21 numbriga tähistatud peatüki kataloogi (00-21), sisaldades READMEsid, koodinäiteid ja ülesandeid
- Mitmed rakendused: Python, TypeScript ja vahel .NET näited
- Tõlketööd kaustas 40+ keeles
- Keskne konfiguratsioon `.env` faili kaudu (kasuta `.env.copy` mallina)

## Seadistuskäsud

### Hoidla Alglaadimine

```bash
# Klooni hoidla
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopeeri keskkonna mall
cp .env.copy .env
# Muuda .env oma API võtmete ja otsapunktidega
```

### Python Keskkonna Seadistamine

```bash
# Loo virtuaalne keskkond
python3 -m venv venv

# Aktiveeri virtuaalne keskkond
# macOS/Linuxil:
source venv/bin/activate
# Windowsil:
venv\Scripts\activate

# Paigalda sõltuvused
pip install -r requirements.txt
```

### Node.js/TypeScript Seadistamine

```bash
# Paigalda juurtaseme sõltuvused (dokumentatsiooni tööriistade jaoks)
npm install

# Individuaalsete õppetükkide TypeScripti näidiste jaoks liigu konkreetse õppetüki juurde:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Containeri Seadistamine (Soovitatav)

Hoidla sisaldab `.devcontainer` konfiguratsiooni GitHub Codespaces või VS Code Dev Containerite jaoks:

1. Ava hoidla GitHub Codespaces või VS Code Dev Containers laiendusega
2. Dev Container teeb automaatselt:
   - Paigaldab Python sõltuvused `requirements.txt` failist
   - Käivitab post-create skripti (`.devcontainer/post-create.sh`)
   - Seadistab Jupyteri kernel’i

## Arendusvoog

### Keskkonnamuutujad

Kõik peatükid, mis vajavad API ligipääsu, kasutavad `.env` failis määratletud keskkonnamuutujaid:

- `OPENAI_API_KEY` - OpenAI API jaoks
- `AZURE_OPENAI_API_KEY` - Azure OpenAI jaoks Microsoft Foundry’s (Azure OpenAI teenus on nüüd osa Microsoft Foundry'st: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI lõpp-punkti URL (Foundry ressursi lõpp-punkt)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion mudeli juurutuse nimi
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings mudeli juurutuse nimi
- `AZURE_OPENAI_API_VERSION` - API versioon (vaikimisi: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face mudelite jaoks
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry mudelite lõpp-punkt (mitme pakkuja mudelikataloog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry mudelite API võti (asendab lõppeva `GITHUB_TOKEN`)

### Python Näidete Käivitamine

```bash
# Liigu õppetüki kataloogi
cd 06-text-generation-apps/python

# Käivita Pythoni skript
python aoai-app.py
```

### TypeScript Näidete Käivitamine

```bash
# Liigu TypeScript rakenduse kausta
cd 06-text-generation-apps/typescript/recipe-app

# Koosta TypeScript kood
npm run build

# Käivita rakendus
npm start
```

### Jupyteri Sülearvutite Käivitamine

```bash
# Käivita Jupyter hoidla juurest
jupyter notebook

# Või kasuta VS Code'i koos Jupyteri laiendiga
```

### Töö erinevate peatükkide tüüpidega

- **"Õpi" peatükid**: Keskenduvad README.md dokumentatsioonile ja mõistetele
- **"Ehita" peatükid**: Sisaldavad töötavaid koodinäiteid Pythonis ja TypeScriptis
- Igal peatükil on README.md koos teooria, koodikõndidega ja videosisu linkidega

## Koodistiili Juhised

### Python

- Kasuta `python-dotenv` keskkonnamuutujate haldamiseks
- Impordi `openai` teek API interaktsioonide jaoks
- Kasuta `pylint` lintimiseks (mõned näited sisaldavad `# pylint: disable=all` lihtsuse huvides)
- Järgi PEP 8 nimetamise konventsioone
- Hoia API volitused `.env` failis, mitte kunagi koodis

### TypeScript

- Kasuta `dotenv` paketti keskkonnamuutujate jaoks
- TypeScript konfiguratsioon asub iga rakenduse `tsconfig.json` failis
- Kasuta `openai` paketti Azure OpenAI jaoks (suuna klient `/openai/v1/` lõpp-punktile ja kutsu `client.responses.create`); kasuta `@azure-rest/ai-inference` Microsoft Foundry mudelite jaoks
- Kasuta arenduses `nodemon` automaatseks taaskäivituseks
- Enne käivitamist tee build: `npm run build` siis `npm start`

### Üldised Konventsioonid

- Hoia koodinäited lihtsate ja harivatena
- Lisa kommentaarid, mis selgitavad võtmekontseptsioone
- Iga peatüki kood peaks olema iseseisev ja jooksutatav
- Kasuta järjepidevaid nimetusi: `aoai-` eesliide Azure OpenAI jaoks, `oai-` OpenAI API jaoks, `githubmodels-` Microsoft Foundry mudelite jaoks (pärand eesliide GitHub Modelsi ajastust)

## Dokumentatsiooni Juhised

### Markdown Stiil

- Kõik URL-id peavad olema vormindatud `[tekst](../../url)` kujul ilma täiendavate tühikuteta
- Relatiivsed lingid peavad algama `./` või `../`
- Kõik lingid Microsofti domeenidesse peavad sisaldama jälgimis-ID-d: `?WT.mc_id=academic-105485-koreyst`
- URL-id ei tohi sisaldada riigipõhiseid lokaliseeringuid (väldi `/en-us/`)
- Pildid hoitakse kaustas `./images` kirjeldusega failinimedega
- Kasuta failinimedes inglise tähti, numbreid ja sidekriipsu

### Tõlke Toetus

- Hoidla toetab 40+ keelt automatiseeritud GitHub Actionsi kaudu
- Tõlked hoitakse kaustas `translations/`
- Ei tohi esitada osalisi tõlkeid
- Masintõlked ei ole aktsepteeritud
- Tõlgitud pildid on kaustas `translated_images/`

## Testimine ja Kinnitamine

### Enne Esitamist Kontrollimine

See hoidla kasutab valideerimiseks GitHub Actionsit. Enne PR esitamist:

1. **Kontrolli Markdown linke**:
   ```bash
   # validate-markdown.yml töövoog kontrollib:
   # - Katkised suhtelised teed
   # - Puuduvad jälgimis-ID-d teedel
   # - Puuduvad jälgimis-ID-d URL-ides
   # - URL-id riigi kohalikuga
   # - Katkised välised URL-id
   ```

2. **Käsitsi testimine**:
   - Testi Python näiteid: aktiveeri venv ja käivita skriptid
   - Testi TypeScript näiteid: `npm install`, `npm run build`, `npm start`
   - Kontrolli, et keskkonnamuutujad oleks õigesti seadistatud
   - Kontrolli, et API võtmed töötaksid koodinäidetega

3. **Koodinäited**:
   - Veendu, et kogu kood jookseb ilma vigadeta
   - Testi nii Azure OpenAI kui OpenAI API-ga, kui see on asjakohane
   - Kontrolli, et näited töötavad Microsoft Foundry mudelitega, kus see toetatud

### Automaatseid Teste Ei Ole

See on hariduslik hoidla, mis keskendub õppetundidele ja näidetele. Ühikuteste ega integreerimisteste ei ole. Kinnitus põhineb peamiselt:
- Käsitsi testimine koodinäidetega
- GitHub Actions Markdown valideerimiseks
- Kogukonna ülevaatus haridusliku sisu osas

## Pull Requesti Juhised

### Enne Esitamist

1. Testi koodimuudatusi nii Pythonis kui TypeScriptis, kui see on asjakohane
2. Käivita Markdown valideerimine (käivitatakse automaatselt PR ajal)
3. Veendu, et kõigil Microsofti URLidel on olemas jälgimis-ID-d
4. Kontrolli, et relatiivsed lingid on korrektsed
5. Veendu, et pildid on õigesti viidatud

### PR Pealkirja Vorming

- Kasuta kirjeldavaid pealkirju: `[Lesson 06] Paranda Python näite trükiviga` või `Uuenda README peatüki 08 jaoks`
- Viita probleeminumbritele, kui see on asjakohane: `Fixes #123`

### PR Kirjeldus

- Selgita, mis muudatused tehti ja miks
- Lisa lingid seotud probleemidele
- Koodimuudatuste korral täpsusta, milliseid näiteid testiti
- Tõlke PR-ide puhul lisa kõik failid täieliku tõlke jaoks

### Panustamise Nõuded

- Allkirjasta Microsofti CLA (automaatne esimesel PR-il)
- Loo enne muutuste tegemist hoidla oma kontosse
- Üks PR ühele loogilisele muutusele (ära ühenda mitteseotud parandusi)
- Hoia PR-id võimalikult fookustatud ja väikesed

## Tavalised Töövood

### Uue Koodinäite Lisamine

1. Liigu vastavasse peatüki kataloogi
2. Loo näide `python/` või `typescript/` alamkaustas
3. Järgi nimetamisreeglit: `{provider}-{example-name}.{py|ts|js}`
4. Testi koos tegelike API volitustega
5. Dokumenteeri kõik uued keskkonnamuutujad peatüki README-s

### Dokumentatsiooni Uuendamine

1. Muuda README.md faili peatüki kataloogis
2. Järgi Markdown juhiseid (jälgimis-ID-d, relatiivsed lingid)
3. Tõlkeid haldavad GitHub Actionsid (ära muuda käsitsi)
4. Kontrolli, et kõik lingid on kehtivad

### Töö Dev Containeritega

1. Hoidla sisaldab `.devcontainer/devcontainer.json` faili
2. Post-create skript paigaldab Python sõltuvused automaatselt
3. Python ja Jupyteri laiendused on eelkonfigureeritud
4. Keskkond põhineb `mcr.microsoft.com/devcontainers/universal:2.11.2` baasil

## Lõpetamine ja Avaldamine

See on õppehoidla - sellel puudub juurutusprotsess. Õppekava kasutatakse järgmiste kaudu:

1. **GitHub Repository**: Otsene ligipääs koodile ja dokumentatsioonile
2. **GitHub Codespaces**: Kohene arenduskeskkond eelkonfigureeritud seadistusega
3. **Microsoft Learn**: Sisu võib olla seotud ametliku õppeplatvormiga
4. **docsify**: Dokumentatsiooni sait ehitatud Markdownist (vt `docsifytopdf.js` ja `package.json`)

### Dokumentatsiooni saidi ehitamine

```bash
# Genereeri PDF dokumentatsioonist (vajadusel)
npm run convert
```

## Probleemide Lahendamine

### Tavalised Probleemid

**Python Importimise Vead**:
- Veendu, et virtuaalkeskkond on aktiveeritud
- Käivita `pip install -r requirements.txt`
- Kontrolli, et Python versioon on 3.9 või uuem

**TypeScript Build Vead**:
- Käivita `npm install` vastavas rakenduse kataloogis
- Kontrolli Node.js versiooni sobivust
- Tühjenda `node_modules` ja paigalda uuesti, kui vaja

**API Autentimise Vead**:
- Veendu, et `.env` fail eksisteerib ja väärtused on õiged
- Kontrolli, et API võtmed on kehtivad ja pole aegunud
- Veendu, et lõpp-punktide URL-id on regiooni jaoks õiged

**Puuduvad Keskkonnamuutujad**:
- Kopeeri `.env.copy` faili `.env` alla
- Täida kõik vajaminevad väärtused peatüki jaoks, millega töötad
- Taaskäivita rakendus pärast `.env` uuendamist

## Täiendavad Ressursid

- [Kursuse Seadistamisjuhend](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Panustamise Juhised](./CONTRIBUTING.md)
- [Käitumisjuhend](./CODE_OF_CONDUCT.md)
- [Turvapoliitika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Täiustatud Koodinäidete Kogu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekti Spetsiifilised Märkmed

- See on **hariduslik hoidla**, keskendudes õppimisele, mitte tootmiskoodile
- Näited on teadlikult lihtsad ja mõistete õpetamisele orienteeritud
- Koodi kvaliteet on tasakaalus haridusliku selgusega
- Iga peatükk on iseseisev ja saab sooritada sõltumatult
- Hoidla toetab mitut API pakkujat: Azure OpenAI, OpenAI, Microsoft Foundry mudelid ja ka võrguühenduseta pakkujaid nagu Foundry Local ja Ollama
- Sisu on mitmekeelne automatiseeritud tõketöövoogudega
- Aktiivne kogukond Discordis küsimuste ja toe jaoks

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->