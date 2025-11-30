<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-11T11:11:23+00:00",
  "source_file": "AGENTS.md",
  "language_code": "et"
}
-->
# AGENTS.md

## Projekti ülevaade

See repositoorium sisaldab põhjalikku 21-õppetunnist koosnevat õppekava, mis õpetab generatiivse tehisintellekti aluseid ja rakenduste arendamist. Kursus on mõeldud algajatele ning hõlmab kõike alates põhimõistetest kuni tootmiskõlblike rakenduste loomiseni.

**Peamised tehnoloogiad:**
- Python 3.9+ koos järgmiste teekidega: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript koos Node.js ja teekidega: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API ja GitHub Models
- Jupyter Notebooks interaktiivseks õppimiseks
- Dev Containers ühtlase arenduskeskkonna tagamiseks

**Repositooriumi struktuur:**
- 21 nummerdatud õppetunni kausta (00-21), mis sisaldavad README-sid, koodinäiteid ja ülesandeid
- Mitu teostust: Python, TypeScript ja mõnikord .NET näited
- Tõlgete kaust, mis sisaldab üle 40 keeleversiooni
- Keskne konfiguratsioon `.env` faili kaudu (kasutage mallina `.env.copy`)

## Seadistamise käsud

### Esmane repositooriumi seadistamine

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python keskkonna seadistamine

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript seadistamine

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Containeri seadistamine (soovitatav)

Repositoorium sisaldab `.devcontainer` konfiguratsiooni GitHub Codespaces'i või VS Code Dev Containers'i jaoks:

1. Avage repositoorium GitHub Codespaces'is või VS Code'is Dev Containers laiendiga
2. Dev Container teeb automaatselt järgmist:
   - Installib Python'i sõltuvused failist `requirements.txt`
   - Käivitab post-loome skripti (`.devcontainer/post-create.sh`)
   - Seadistab Jupyter kernel'i

## Arendustöövoog

### Keskkonnamuutujad

Kõik õppetunnid, mis vajavad API ligipääsu, kasutavad `.env` failis määratletud keskkonnamuutujaid:

- `OPENAI_API_KEY` - OpenAI API jaoks
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service jaoks
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI lõpp-punkti URL
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion mudeli juurutamise nimi
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings mudeli juurutamise nimi
- `AZURE_OPENAI_API_VERSION` - API versioon (vaikimisi: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face mudelite jaoks
- `GITHUB_TOKEN` - GitHub Models jaoks

### Python näidete käivitamine

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript näidete käivitamine

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebookide kasutamine

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Erinevate õppetüüpidega töötamine

- **"Learn" õppetunnid**: Keskenduvad README.md dokumentatsioonile ja kontseptsioonidele
- **"Build" õppetunnid**: Sisaldavad töötavaid koodinäiteid Pythonis ja TypeScriptis
- Igal õppetunnil on README.md, mis sisaldab teooriat, koodi ülevaateid ja linke videomaterjalidele

## Koodistiili juhised

### Python

- Kasutage keskkonnamuutujate haldamiseks `python-dotenv`
- Importige API interaktsioonideks `openai` teek
- Kasutage lintimiseks `pylint` (mõned näited sisaldavad lihtsuse huvides `# pylint: disable=all`)
- Järgige PEP 8 nimetamisreegleid
- Salvestage API mandaadid `.env` faili, mitte koodi

### TypeScript

- Kasutage keskkonnamuutujate jaoks `dotenv` paketti
- TypeScripti konfiguratsioon failis `tsconfig.json` iga rakenduse jaoks
- Kasutage Azure teenuste jaoks `@azure/openai` või `@azure-rest/ai-inference`
- Kasutage arendamiseks automaatse taaskäivitusega `nodemon`
- Enne käivitamist kompileerige: `npm run build`, seejärel `npm start`

### Üldised tavad

- Hoidke koodinäited lihtsad ja harivad
- Lisage kommentaare, mis selgitavad põhikontseptsioone
- Iga õppetunni kood peaks olema iseseisev ja käivitatav
- Kasutage järjepidevaid nimetusi: `aoai-` Azure OpenAI jaoks, `oai-` OpenAI API jaoks, `githubmodels-` GitHub Models jaoks

## Dokumentatsiooni juhised

### Markdown stiil

- Kõik URL-id peavad olema vormingus `[tekst](../../url)` ilma lisatühikuteta
- Suhtelised lingid peavad algama `./` või `../`
- Kõik Microsofti domeenide lingid peavad sisaldama jälgimis-ID-d: `?WT.mc_id=academic-105485-koreyst`
- URL-ides ei tohi olla riigispetsiifilisi lokaale (vältige `/en-us/`)
- Pildid tuleb salvestada kausta `./images` kirjeldavate nimedega
- Failinimedes kasutage ainult inglise tähti, numbreid ja kriipse

### Tõlke tugi

- Repositoorium toetab üle 40 keele automaatsete GitHub Actions tõlgete kaudu
- Tõlked salvestatakse kausta `translations/`
- Osalisi tõlkeid ei aktsepteerita
- Masintõlkeid ei aktsepteerita
- Tõlgitud pildid salvestatakse kausta `translated_images/`

## Testimine ja valideerimine

### Enne esitamist kontrollige

See repositoorium kasutab valideerimiseks GitHub Actions'i. Enne PR-ide esitamist:

1. **Kontrollige Markdown linke**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuaalne testimine**:
   - Testige Python'i näiteid: aktiveerige venv ja käivitage skriptid
   - Testige TypeScript'i näiteid: `npm install`, `npm run build`, `npm start`
   - Veenduge, et keskkonnamuutujad on õigesti seadistatud
   - Kontrollige, et API võtmed töötavad koodinäidetega

3. **Koodinäited**:
   - Veenduge, et kogu kood töötab vigadeta
   - Testige nii Azure OpenAI kui ka OpenAI API-ga, kui see on asjakohane
   - Kontrollige, et näited töötavad toetatud GitHub Models'iga

### Automaatseid teste ei ole

See on hariduslik repositoorium, mis keskendub õpetustele ja näidetele. Üksustestid või integreerimistestid puuduvad. Valideerimine toimub peamiselt:
- Koodinäidete manuaalne testimine
- GitHub Actions Markdown'i valideerimiseks
- Kogukonna ülevaated haridusliku sisu kohta

## Pull Request'i juhised

### Enne esitamist

1. Testige koodimuudatusi nii Pythonis kui ka TypeScriptis, kui see on asjakohane
2. Käivitage Markdown'i valideerimine (käivitatakse automaatselt PR-is)
3. Veenduge, et kõik Microsofti URL-id sisaldavad jälgimis-ID-d
4. Kontrollige, et suhtelised lingid on kehtivad
5. Veenduge, et pildid on õigesti viidatud

### PR-i pealkirja formaat

- Kasutage kirjeldavaid pealkirju: `[Lesson 06] Parandage Python'i näite viga` või `Uuendage README õppetunni 08 jaoks`
- Viidake vajadusel probleeminumbritele: `Fixes #123`

### PR-i kirjeldus

- Selgitage, mida muudeti ja miks
- Linkige seotud probleemidega
- Koodimuudatuste puhul täpsustage, milliseid näiteid testiti
- Tõlke PR-ide puhul lisage kõik failid täieliku tõlke jaoks

### Kaastöö nõuded

- Allkirjastage Microsoft CLA (automaatselt esimesel PR-il)
- Forkige repositoorium oma kontole enne muudatuste tegemist
- Üks PR iga loogilise muudatuse kohta (ärge ühendage mitteseotud parandusi)
- Hoidke PR-id keskendunud ja võimalusel väikesed

## Tavalised töövood

### Uue koodinäite lisamine

1. Navigeerige sobivasse õppetunni kausta
2. Looge näide kaustas `python/` või `typescript/`
3. Järgige nimetamisreeglit: `{provider}-{example-name}.{py|ts|js}`
4. Testige tegelike API mandaadidega
5. Dokumenteerige kõik uued keskkonnamuutujad õppetunni README-s

### Dokumentatsiooni uuendamine

1. Redigeerige README.md faili õppetunni kaustas
2. Järgige Markdown'i juhiseid (jälgimis-ID-d, suhtelised lingid)
3. Tõlkeid haldab GitHub Actions (ärge muutke käsitsi)
4. Testige, et kõik lingid on kehtivad

### Dev Containeritega töötamine

1. Repositoorium sisaldab `.devcontainer/devcontainer.json` faili
2. Post-loome skript installib automaatselt Python'i sõltuvused
3. Laiendused Python'i ja Jupyter'i jaoks on eelkonfigureeritud
4. Keskkond põhineb `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Juurutamine ja avaldamine

See on õpperepositoorium - juurutamisprotsessi ei ole. Õppekava kasutatakse järgmiselt:

1. **GitHub repositoorium**: Otsene juurdepääs koodile ja dokumentatsioonile
2. **GitHub Codespaces**: Kohene arenduskeskkond eelkonfigureeritud seadistusega
3. **Microsoft Learn**: Sisu võib olla sünkroniseeritud ametlikule õppeplatvormile
4. **docsify**: Dokumentatsioonisait, mis on ehitatud Markdown'ist (vt `docsifytopdf.js` ja `package.json`)

### Dokumentatsioonisaidi ehitamine

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Tõrkeotsing

### Levinud probleemid

**Python'i impordivead**:
- Veenduge, et virtuaalne keskkond on aktiveeritud
- Käivitage `pip install -r requirements.txt`
- Kontrollige, et Python'i versioon on 3.9+

**TypeScript'i kompileerimisvead**:
- Käivitage `npm install` vastavas rakenduse kaustas
- Kontrollige, et Node.js versioon on ühilduv
- Tühjendage `node_modules` ja installige uuesti, kui vaja

**API autentimisvead**:
- Veenduge, et `.env` fail eksisteerib ja sisaldab õigeid väärtusi
- Kontrollige, et API võtmed on kehtivad ja mitte aegunud
- Veenduge, et lõpp-punkti URL-id on teie piirkonna jaoks õiged

**Puuduvad keskkonnamuutujad**:
- Kopeerige `.env.copy` fail `.env`-iks
- Täitke kõik vajalikud väärtused õppetunni jaoks, millega töötate
- Taaskäivitage oma rakendus pärast `.env` uuendamist

## Lisamaterjalid

- [Kursuse seadistamise juhend](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Kaastöö juhised](./CONTRIBUTING.md)
- [Käitumisjuhend](./CODE_OF_CONDUCT.md)
- [Turvapoliitika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Kogumik edasijõudnute koodinäidetest](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekti erimärkused

- See on **õpperepositoorium**, mis keskendub õppimisele, mitte tootmiskoodile
- Näited on tahtlikult lihtsad ja keskenduvad kontseptsioonide õpetamisele
- Koodikvaliteet on tasakaalus haridusliku selgusega
- Iga õppetund on iseseisev ja seda saab eraldi läbida
- Repositoorium toetab mitut API pakkujat: Azure OpenAI, OpenAI ja GitHub Models
- Sisu on mitmekeelne, kasutades automatiseeritud tõlke töövooge
- Aktiivne kogukond Discordis küsimuste ja toe jaoks

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.