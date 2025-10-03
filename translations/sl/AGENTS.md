<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:13:20+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sl"
}
-->
# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje obsežen učni načrt s 21 lekcijami, ki poučuje osnove generativne umetne inteligence in razvoj aplikacij. Tečaj je zasnovan za začetnike in pokriva vse od osnovnih konceptov do izdelave aplikacij, pripravljenih za produkcijo.

**Ključne tehnologije:**
- Python 3.9+ z knjižnicami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript z Node.js in knjižnicami: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API in GitHub Models
- Jupyter Notebooks za interaktivno učenje
- Dev Containers za dosledno razvojno okolje

**Struktura repozitorija:**
- 21 oštevilčenih direktorijev lekcij (00-21), ki vsebujejo README datoteke, primere kode in naloge
- Več implementacij: Python, TypeScript in včasih .NET primeri
- Direktorij prevodov z več kot 40 jezikovnimi različicami
- Centralizirana konfiguracija prek `.env` datoteke (uporabite `.env.copy` kot predlogo)

## Ukazi za nastavitev

### Začetna nastavitev repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Nastavitev Python okolja

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

### Nastavitev Node.js/TypeScript okolja

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavitev Dev Container (priporočeno)

Repozitorij vključuje konfiguracijo `.devcontainer` za GitHub Codespaces ali VS Code Dev Containers:

1. Odprite repozitorij v GitHub Codespaces ali VS Code z razširitvijo Dev Containers
2. Dev Container bo samodejno:
   - Namestil Python odvisnosti iz `requirements.txt`
   - Zagnal skripto po ustvarjanju (`.devcontainer/post-create.sh`)
   - Nastavil Jupyter kernel

## Potek razvoja

### Spremenljivke okolja

Vse lekcije, ki zahtevajo dostop do API-jev, uporabljajo spremenljivke okolja, definirane v `.env`:

- `OPENAI_API_KEY` - Za OpenAI API
- `AZURE_OPENAI_API_KEY` - Za Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL končne točke Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Ime modela za dokončanje pogovorov
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Ime modela za vdelave
- `AZURE_OPENAI_API_VERSION` - Različica API-ja (privzeto: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Za modele Hugging Face
- `GITHUB_TOKEN` - Za GitHub Models

### Zagon Python primerov

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Zagon TypeScript primerov

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Zagon Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Delo z različnimi vrstami lekcij

- **Lekcije "Learn"**: Osredotočajo se na README.md dokumentacijo in koncepte
- **Lekcije "Build"**: Vključujejo delujoče primere kode v Pythonu in TypeScriptu
- Vsaka lekcija ima README.md z teorijo, pregledom kode in povezavami do video vsebin

## Smernice za slog kode

### Python

- Uporabite `python-dotenv` za upravljanje spremenljivk okolja
- Uvozite knjižnico `openai` za interakcije z API-jem
- Uporabite `pylint` za preverjanje kode (nekateri primeri vključujejo `# pylint: disable=all` za preprostost)
- Upoštevajte konvencije po PEP 8
- Shranite API poverilnice v `.env` datoteko, nikoli v kodo

### TypeScript

- Uporabite paket `dotenv` za spremenljivke okolja
- Konfiguracija TypeScript v `tsconfig.json` za vsako aplikacijo
- Uporabite `@azure/openai` ali `@azure-rest/ai-inference` za Azure storitve
- Uporabite `nodemon` za razvoj z samodejnim ponovnim zagonom
- Pred zagonom izvedite gradnjo: `npm run build` nato `npm start`

### Splošne konvencije

- Ohranite primere kode preproste in poučne
- Vključite komentarje, ki pojasnjujejo ključne koncepte
- Koda vsake lekcije mora biti samostojna in izvedljiva
- Uporabite dosledno poimenovanje: `aoai-` za Azure OpenAI, `oai-` za OpenAI API, `githubmodels-` za GitHub Models

## Smernice za dokumentacijo

### Slog Markdown

- Vsi URL-ji morajo biti oviti v format `[besedilo](../../url)` brez dodatnih presledkov
- Relativne povezave morajo začeti z `./` ali `../`
- Vse povezave do Microsoft domen morajo vključevati ID za sledenje: `?WT.mc_id=academic-105485-koreyst`
- Brez lokaliziranih URL-jev (izogibajte se `/en-us/`)
- Slike shranjene v mapi `./images` z opisnimi imeni
- Uporabite angleške znake, številke in vezaje v imenih datotek

### Podpora za prevode

- Repozitorij podpira več kot 40 jezikov prek avtomatiziranih GitHub Actions
- Prevodi so shranjeni v direktoriju `translations/`
- Ne oddajajte delnih prevodov
- Strojni prevodi niso sprejeti
- Prevedene slike so shranjene v direktoriju `translated_images/`

## Testiranje in validacija

### Preverjanja pred oddajo

Ta repozitorij uporablja GitHub Actions za validacijo. Pred oddajo PR-jev:

1. **Preverite povezave v Markdownu**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Ročno testiranje**:
   - Testirajte Python primere: Aktivirajte venv in zaženite skripte
   - Testirajte TypeScript primere: `npm install`, `npm run build`, `npm start`
   - Preverite, da so spremenljivke okolja pravilno nastavljene
   - Preverite, da API ključi delujejo s primeri kode

3. **Primeri kode**:
   - Preverite, da vsa koda deluje brez napak
   - Testirajte z Azure OpenAI in OpenAI API, kjer je to primerno
   - Preverite, da primeri delujejo z GitHub Models, kjer je to podprto

### Brez avtomatiziranih testov

To je izobraževalni repozitorij, osredotočen na vadnice in primere. Ni enotnih testov ali integracijskih testov za zagon. Validacija je predvsem:
- Ročno testiranje primerov kode
- GitHub Actions za validacijo Markdowna
- Pregled izobraževalne vsebine s strani skupnosti

## Smernice za Pull Requeste

### Pred oddajo

1. Testirajte spremembe kode v Pythonu in TypeScriptu, kjer je to primerno
2. Zaženite validacijo Markdowna (samodejno sprožena ob PR)
3. Preverite, da so ID-ji za sledenje prisotni na vseh Microsoft URL-jih
4. Preverite, da so relativne povezave veljavne
5. Preverite, da so slike pravilno referencirane

### Format naslova PR

- Uporabite opisne naslove: `[Lekcija 06] Popravek tipkarske napake v Python primeru` ali `Posodobitev README za lekcijo 08`
- Navedite številke težav, kjer je to primerno: `Odpravljeno #123`

### Opis PR

- Pojasnite, kaj je bilo spremenjeno in zakaj
- Povezava na povezane težave
- Za spremembe kode navedite, kateri primeri so bili testirani
- Za prevodne PR-je vključite vse datoteke za popoln prevod

### Zahteve za prispevanje

- Podpišite Microsoft CLA (samodejno ob prvem PR)
- Pred spremembami forkajte repozitorij na svoj račun
- En PR na logično spremembo (ne združujte nepovezanih popravkov)
- PR naj bo osredotočen in čim manjši

## Pogosti postopki

### Dodajanje novega primera kode

1. Pojdite v ustrezen direktorij lekcije
2. Ustvarite primer v poddirektoriju `python/` ali `typescript/`
3. Upoštevajte konvencijo poimenovanja: `{ponudnik}-{ime-primerka}.{py|ts|js}`
4. Testirajte z dejanskimi API poverilnicami
5. Dokumentirajte vse nove spremenljivke okolja v README lekcije

### Posodabljanje dokumentacije

1. Uredite README.md v direktoriju lekcije
2. Upoštevajte smernice za Markdown (ID-ji za sledenje, relativne povezave)
3. Posodobitve prevodov obravnavajo GitHub Actions (ne urejajte ročno)
4. Preverite, da so vse povezave veljavne

### Delo z Dev Containers

1. Repozitorij vključuje `.devcontainer/devcontainer.json`
2. Skripta po ustvarjanju samodejno namesti Python odvisnosti
3. Razširitve za Python in Jupyter so predhodno konfigurirane
4. Okolje temelji na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Namestitev in objava

To je izobraževalni repozitorij - ni postopka za namestitev. Učni načrt se uporablja prek:

1. **GitHub repozitorij**: Neposreden dostop do kode in dokumentacije
2. **GitHub Codespaces**: Takojšnje razvojno okolje s predhodno konfiguracijo
3. **Microsoft Learn**: Vsebina je lahko objavljena na uradni učni platformi
4. **docsify**: Spletno mesto dokumentacije, zgrajeno iz Markdown datotek (glejte `docsifytopdf.js` in `package.json`)

### Gradnja spletnega mesta dokumentacije

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Odpravljanje težav

### Pogoste težave

**Napake pri uvozu v Pythonu**:
- Preverite, da je virtualno okolje aktivirano
- Zaženite `pip install -r requirements.txt`
- Preverite, da je različica Pythona 3.9+

**Napake pri gradnji TypeScript**:
- Zaženite `npm install` v specifičnem direktoriju aplikacije
- Preverite, da je različica Node.js združljiva
- Po potrebi izbrišite `node_modules` in ponovno namestite

**Napake pri avtentikaciji API-ja**:
- Preverite, da `.env` datoteka obstaja in ima pravilne vrednosti
- Preverite, da so API ključi veljavni in niso potekli
- Preverite, da so URL-ji končnih točk pravilni za vašo regijo

**Manjkajoče spremenljivke okolja**:
- Kopirajte `.env.copy` v `.env`
- Izpolnite vse zahtevane vrednosti za lekcijo, na kateri delate
- Po posodobitvi `.env` znova zaženite aplikacijo

## Dodatni viri

- [Vodnik za nastavitev tečaja](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Smernice za prispevanje](./CONTRIBUTING.md)
- [Kodeks ravnanja](./CODE_OF_CONDUCT.md)
- [Varnostna politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbirka naprednih primerov kode](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Opombe o projektu

- To je **izobraževalni repozitorij**, osredotočen na učenje, ne na produkcijsko kodo
- Primeri so namerno preprosti in osredotočeni na poučevanje konceptov
- Kakovost kode je uravnotežena z izobraževalno jasnostjo
- Vsaka lekcija je samostojna in jo je mogoče zaključiti neodvisno
- Repozitorij podpira več ponudnikov API-jev: Azure OpenAI, OpenAI in GitHub Models
- Vsebina je večjezična z avtomatiziranimi delovnimi tokovi za prevajanje
- Aktivna skupnost na Discordu za vprašanja in podporo

---

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.